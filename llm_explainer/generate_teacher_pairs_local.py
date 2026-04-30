#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any


if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_reports import (  # noqa: E402
    MODEL_REGISTRY,
    build_payload,
    cleanup_text,
    configure_tokenizer,
    load_model_for_generation,
    load_transformers,
    read_jsonl,
    resolve_dtype,
    resolve_local_model_path,
    tokenize_prompt,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate teacher instruction pairs from prepared RPT requests using a local HF model."
        )
    )
    parser.add_argument(
        "--teacher-model-key",
        default="Llama-3.3-70B-Instruct",
        choices=sorted(MODEL_REGISTRY),
        help="Logical model key from the local registry.",
    )
    parser.add_argument(
        "--experiment-dir",
        default="",
        help="Optional experiment directory produced by prepare_sft_data.py. Reads teacher_requests/*.jsonl.",
    )
    parser.add_argument(
        "--requests-jsonl",
        nargs="*",
        default=None,
        help="Optional explicit teacher request JSONL paths.",
    )
    parser.add_argument(
        "--model-path",
        default="",
        help="Optional override for the local model path.",
    )
    parser.add_argument(
        "--tokenizer-path",
        default="",
        help="Optional override for the local tokenizer path.",
    )
    parser.add_argument(
        "--out-dir",
        default="llm_explainer/teacher_pairs_local",
        help="Output folder for split-specific JSONL and markdown files.",
    )
    parser.add_argument(
        "--max-reports-per-split",
        type=int,
        default=0,
        help="Optional cap per split (0 = all reports in each request file).",
    )
    parser.add_argument(
        "--max-new-tokens",
        type=int,
        default=0,
        help="Generation length cap. Use 0 to accept the model-specific default.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=-1.0,
        help="Sampling temperature. Use a negative value to accept the model-specific default.",
    )
    parser.add_argument(
        "--top-p",
        type=float,
        default=0.0,
        help="Top-p sampling cutoff when temperature > 0. Use 0 to accept the model-specific default.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing split outputs instead of resuming.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write empty output scaffolding only; skip local model loading and generation.",
    )
    return parser.parse_args()


def collect_request_files(args: argparse.Namespace) -> list[Path]:
    files: list[Path] = []

    if args.experiment_dir:
        request_dir = Path(args.experiment_dir).resolve() / "teacher_requests"
        files.extend(sorted(request_dir.glob("*.jsonl")))

    if args.requests_jsonl:
        files.extend(Path(path).resolve() for path in args.requests_jsonl)

    unique: list[Path] = []
    seen: set[Path] = set()
    for path in files:
        if path not in seen:
            unique.append(path)
            seen.add(path)
    return unique


def resolve_generation_settings(args: argparse.Namespace, model_key: str) -> dict[str, Any]:
    generation = MODEL_REGISTRY[model_key]["generation"]
    max_new_tokens = args.max_new_tokens if args.max_new_tokens > 0 else generation["max_new_tokens"]
    temperature = args.temperature if args.temperature >= 0 else generation["temperature"]
    top_p = args.top_p if args.top_p > 0 else generation["top_p"]
    return {
        "max_new_tokens": int(max_new_tokens),
        "temperature": float(temperature),
        "top_p": float(top_p),
        "repetition_penalty": float(generation.get("repetition_penalty", 1.0)),
        "no_repeat_ngram_size": int(generation.get("no_repeat_ngram_size", 0)),
        "context_margin": int(generation.get("context_margin", 32)),
    }


def load_completed_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    completed: set[str] = set()
    for row in read_jsonl(path):
        report_id = row.get("report_id")
        if report_id:
            completed.add(str(report_id))
    return completed


def build_markdown(run_label: str, rows: list[dict[str, Any]]) -> str:
    lines = [f"# Teacher Pairs - {run_label}", ""]
    for row in rows:
        lines.append(f"## {row['report_title']}")
        if row.get("split"):
            lines.append(f"_Split: {row['split']}_")
            lines.append("")
        lines.append(row.get("output", "").strip() or "_No output generated._")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def split_name_for_path(path: Path, rows: list[dict[str, Any]]) -> str:
    if rows and rows[0].get("split"):
        return str(rows[0]["split"])
    return path.stem


def main() -> None:
    args = parse_args()

    request_files = collect_request_files(args)
    if not request_files:
        raise FileNotFoundError("No teacher request JSONL files were found.")

    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

    spec = MODEL_REGISTRY[args.teacher_model_key]
    raw_model_path = Path(args.model_path).resolve() if args.model_path else Path(spec["path"]).resolve()
    raw_tokenizer_path = (
        Path(args.tokenizer_path).resolve() if args.tokenizer_path else raw_model_path
    )
    model_path = resolve_local_model_path(raw_model_path)
    tokenizer_path = resolve_local_model_path(raw_tokenizer_path)
    generation_settings = resolve_generation_settings(args, args.teacher_model_key)

    tokenizer = None
    model = None
    torch = None

    if not args.dry_run:
        import torch as torch_module

        torch = torch_module
        AutoModelForCausalLM, AutoTokenizer = load_transformers()
        tokenizer = AutoTokenizer.from_pretrained(
            tokenizer_path,
            local_files_only=True,
            trust_remote_code=True,
        )
        configure_tokenizer(tokenizer, tokenizer_path)
        dtype = resolve_dtype(torch)
        model = load_model_for_generation(
            AutoModelForCausalLM=AutoModelForCausalLM,
            base_model_path=model_path,
            adapter_path=None,
            spec=spec,
            dtype=dtype,
            torch_module=torch,
        )
        if hasattr(model, "eval"):
            model.eval()

    for request_path in request_files:
        rows = read_jsonl(request_path)
        if args.max_reports_per_split > 0:
            rows = rows[: args.max_reports_per_split]

        split_name = split_name_for_path(request_path, rows)
        out_jsonl = out_dir / f"{split_name}.jsonl"
        out_md = out_dir / f"{split_name}.md"

        completed_ids = set() if args.overwrite else load_completed_ids(out_jsonl)
        mode = "w" if args.overwrite else "a"

        with out_jsonl.open(mode, encoding="utf-8") as fout:
            for row in rows:
                report_id = str(row["report_id"])
                if report_id in completed_ids:
                    continue

                if args.dry_run:
                    output_text = ""
                    prompt_token_count = 0
                    input_token_count = 0
                    max_new_tokens_used = generation_settings["max_new_tokens"]
                    used_chat_payload = False
                else:
                    assert tokenizer is not None
                    assert model is not None
                    assert torch is not None

                    rendered_prompt, used_chat_payload = build_payload(
                        tokenizer=tokenizer,
                        model_key=args.teacher_model_key,
                        system_prompt=row["system_prompt"],
                        user_prompt=row["input"],
                    )
                    prompt_token_count = len(
                        tokenizer(rendered_prompt, add_special_tokens=False)["input_ids"]
                    )

                    context_window = spec.get("context_window")
                    max_input_tokens = None
                    if context_window:
                        max_input_tokens = max(
                            256,
                            int(context_window)
                            - generation_settings["max_new_tokens"]
                            - generation_settings["context_margin"],
                        )

                    encoded = tokenize_prompt(tokenizer, rendered_prompt, max_input_tokens)
                    input_ids = encoded["input_ids"]
                    attention_mask = encoded["attention_mask"]
                    input_token_count = int(input_ids.shape[-1])

                    max_new_tokens_used = generation_settings["max_new_tokens"]
                    if context_window:
                        room = int(context_window) - input_token_count - generation_settings["context_margin"]
                        max_new_tokens_used = max(64, min(max_new_tokens_used, room))

                    generate_kwargs: dict[str, Any] = {
                        "max_new_tokens": max_new_tokens_used,
                        "pad_token_id": tokenizer.pad_token_id,
                        "eos_token_id": tokenizer.eos_token_id,
                        "repetition_penalty": generation_settings["repetition_penalty"],
                    }
                    if generation_settings["no_repeat_ngram_size"] > 0:
                        generate_kwargs["no_repeat_ngram_size"] = generation_settings[
                            "no_repeat_ngram_size"
                        ]
                    if generation_settings["temperature"] > 0:
                        generate_kwargs.update(
                            {
                                "do_sample": True,
                                "temperature": generation_settings["temperature"],
                                "top_p": generation_settings["top_p"],
                            }
                        )
                    else:
                        generate_kwargs["do_sample"] = False

                    if torch.cuda.is_available():
                        input_ids = input_ids.to("cuda:0")
                        attention_mask = attention_mask.to("cuda:0")

                    with torch.inference_mode():
                        output_ids = model.generate(
                            input_ids=input_ids,
                            attention_mask=attention_mask,
                            **generate_kwargs,
                        )

                    new_tokens = output_ids[0, input_token_count:]
                    raw_output = tokenizer.decode(new_tokens, skip_special_tokens=True)
                    output_text = cleanup_text(raw_output)

                record = {
                    "report_id": report_id,
                    "report_title": row.get("report_title", report_id),
                    "split": row.get("split", split_name),
                    "teacher_model_key": args.teacher_model_key,
                    "teacher_model_path": str(model_path),
                    "input": row["input"],
                    "output": output_text,
                    "system_prompt": row["system_prompt"],
                    "used_chat_payload": bool(used_chat_payload),
                    "prompt_token_count": int(prompt_token_count),
                    "input_token_count": int(input_token_count),
                    "max_new_tokens_used": int(max_new_tokens_used),
                    "source_requests_jsonl": str(request_path),
                    "generated_at_unix": time.time(),
                }
                fout.write(json.dumps(record, ensure_ascii=True) + "\n")
                fout.flush()

        combined_rows = read_jsonl(out_jsonl)
        out_md.write_text(
            build_markdown(
                run_label=f"{args.teacher_model_key} - {split_name}",
                rows=combined_rows,
            ),
            encoding="utf-8",
        )

        summary = {
            "split": split_name,
            "teacher_model_key": args.teacher_model_key,
            "teacher_model_path": str(model_path),
            "request_path": str(request_path),
            "n_requests": len(rows),
            "n_completed": len(combined_rows),
            "generation_settings": generation_settings,
            "dry_run": bool(args.dry_run),
        }
        (out_dir / f"{split_name}_summary.json").write_text(
            json.dumps(summary, indent=2) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
