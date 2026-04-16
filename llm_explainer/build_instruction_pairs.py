#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any
from urllib import error, request


if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_reports import (  # noqa: E402
    MODEL_REGISTRY,
    build_aux_context,
    build_system_prompt,
    build_user_prompt,
    cleanup_text,
    load_global_context,
    read_jsonl,
    report_title,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build instruction pairs from SHAP reports by calling an "
            "OpenAI-compatible API model."
        )
    )
    parser.add_argument(
        "--reports-md",
        default="llm_explainer/shap_sample_reports.md",
        help="Markdown report bundle containing `## RPT-XXXX - ...` sections.",
    )
    parser.add_argument(
        "--reports-jsonl",
        default="llm_explainer/shap_sample_reports.jsonl",
        help="Structured JSONL bundle aligned to the markdown report sections.",
    )
    parser.add_argument(
        "--results-root",
        default="results",
        help="Root folder that contains dem/, tuning/, and rf_plots/.",
    )
    parser.add_argument(
        "--model",
        default="models--meta-llama--Llama-3.3-70B-Instruct",
        help="Remote API model name to call.",
    )
    parser.add_argument(
        "--api-base-url",
        default=os.environ.get("LLM_API_BASE_URL", os.environ.get("OPENAI_BASE_URL", "")).strip(),
        help="OpenAI-compatible base URL, e.g. https://host/v1.",
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("LLM_API_KEY", os.environ.get("OPENAI_API_KEY", "")).strip(),
        help="API key for the OpenAI-compatible endpoint.",
    )
    parser.add_argument(
        "--prompt-model-key",
        default="Meta-Llama-3.1-8B-Instruct",
        choices=sorted(MODEL_REGISTRY),
        help="Reuse this local prompt template when building the system prompt.",
    )
    parser.add_argument(
        "--out-jsonl",
        default="llm_explainer/llama33_70b_instruction_pairs.jsonl",
        help="Instruction-pair dataset output path.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite an existing output file instead of resuming.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Optional cap on the number of reports to process (0 = all).",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature for the API call.",
    )
    parser.add_argument(
        "--top-p",
        type=float,
        default=1.0,
        help="Top-p sampling cutoff for the API call.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=900,
        help="Maximum completion tokens per report.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=180,
        help="HTTP timeout in seconds.",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=4,
        help="How many times to retry transient API failures.",
    )
    parser.add_argument(
        "--delay-seconds",
        type=float,
        default=0.0,
        help="Optional delay between successful API calls.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write prompt/input scaffolding only and skip remote API calls.",
    )
    return parser.parse_args()


def extract_markdown_sections(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    sections: dict[str, list[str]] = {}
    current_id: str | None = None
    current_lines: list[str] = []

    for line in lines:
        if line.startswith("## RPT-"):
            if current_id is not None:
                sections[current_id] = current_lines[:]
            current_id = line.split(" ", 2)[1]
            current_lines = [line]
            continue
        if current_id is not None:
            current_lines.append(line)

    if current_id is not None:
        sections[current_id] = current_lines[:]

    return {
        report_id: "\n".join(section_lines).strip()
        for report_id, section_lines in sections.items()
    }


def build_training_input(
    *,
    report: dict[str, Any],
    report_markdown: str | None,
    global_context: Any,
    prompt_model_key: str,
) -> tuple[str, str]:
    prompt_profile = MODEL_REGISTRY[prompt_model_key]["prompt_profile"]
    system_prompt = build_system_prompt(prompt_model_key)

    if report_markdown:
        evidence_block = "\n".join(
            [
                "Structured SHAP-grounded report:",
                report_markdown,
                "",
                build_aux_context(report, global_context, prompt_profile),
                "",
                "Generate a grounded explanation using the required section headings.",
            ]
        )
    else:
        evidence_block = build_user_prompt(report, global_context, prompt_model_key)

    return system_prompt, evidence_block


def call_openai_compatible_chat(
    *,
    base_url: str,
    api_key: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
    top_p: float,
    max_tokens: int,
    timeout_seconds: int,
    max_retries: int,
) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
    }

    headers = {
        "Content-Type": "application/json",
    }
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    body = json.dumps(payload).encode("utf-8")
    last_error: str | None = None

    for attempt in range(max_retries):
        req = request.Request(url, data=body, headers=headers, method="POST")
        try:
            with request.urlopen(req, timeout=timeout_seconds) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return str(data["choices"][0]["message"]["content"])
        except error.HTTPError as exc:
            details = exc.read().decode("utf-8", errors="replace")
            last_error = f"HTTP {exc.code}: {details}"
        except Exception as exc:  # noqa: BLE001
            last_error = str(exc)

        if attempt < max_retries - 1:
            time.sleep(2 ** attempt)

    raise RuntimeError(f"API request failed after {max_retries} attempts: {last_error}")


def load_completed_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    completed: set[str] = set()
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            report_id = row.get("report_id")
            if report_id:
                completed.add(str(report_id))
    return completed


def main() -> None:
    args = parse_args()

    reports_md = Path(args.reports_md).resolve()
    reports_jsonl = Path(args.reports_jsonl).resolve()
    results_root = Path(args.results_root).resolve()
    out_jsonl = Path(args.out_jsonl).resolve()
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)

    if not reports_jsonl.exists():
        raise FileNotFoundError(f"Structured report bundle not found: {reports_jsonl}")

    if not reports_md.exists():
        print(
            f"Warning: markdown bundle not found at {reports_md}; "
            "falling back to JSONL-built structured prompts."
        )

    if not args.dry_run and not args.api_base_url:
        raise RuntimeError(
            "Set --api-base-url or LLM_API_BASE_URL / OPENAI_BASE_URL before calling the remote model."
        )

    reports = read_jsonl(reports_jsonl)
    if args.limit > 0:
        reports = reports[: args.limit]
    reports_by_id = {row["report_id"]: row for row in reports}
    markdown_sections = extract_markdown_sections(reports_md) if reports_md.exists() else {}

    global_context = load_global_context(results_root)

    mode = "w" if args.overwrite else "a"
    completed_ids = set() if args.overwrite else load_completed_ids(out_jsonl)

    with out_jsonl.open(mode, encoding="utf-8") as fout:
        for report in reports:
            report_id = str(report["report_id"])
            if report_id in completed_ids:
                continue

            report_markdown = markdown_sections.get(report_id)
            system_prompt, structured_input = build_training_input(
                report=report,
                report_markdown=report_markdown,
                global_context=global_context,
                prompt_model_key=args.prompt_model_key,
            )

            if args.dry_run:
                llm_output = ""
            else:
                raw_output = call_openai_compatible_chat(
                    base_url=args.api_base_url,
                    api_key=args.api_key,
                    model=args.model,
                    system_prompt=system_prompt,
                    user_prompt=structured_input,
                    temperature=args.temperature,
                    top_p=args.top_p,
                    max_tokens=args.max_tokens,
                    timeout_seconds=args.timeout_seconds,
                    max_retries=args.max_retries,
                )
                llm_output = cleanup_text(raw_output)

            record = {
                "report_id": report_id,
                "report_title": report_title(report),
                "model": args.model,
                "input": structured_input,
                "output": llm_output,
                "system_prompt": system_prompt,
                "source_markdown_path": str(reports_md) if report_markdown else "",
                "source_jsonl_path": str(reports_jsonl),
                "generated_at_unix": time.time(),
            }
            fout.write(json.dumps(record, ensure_ascii=True) + "\n")
            fout.flush()

            if args.delay_seconds > 0 and not args.dry_run:
                time.sleep(args.delay_seconds)

    print(f"Wrote instruction pairs to {out_jsonl}")


if __name__ == "__main__":
    main()
