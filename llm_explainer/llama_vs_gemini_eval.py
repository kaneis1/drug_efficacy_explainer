#!/usr/bin/env python3
"""Run a same-prompt Llama vs Gemini evaluation for AZD7762 / A-204."""
from __future__ import annotations

import argparse
import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from generate_reports import (
    MODEL_REGISTRY,
    configure_tokenizer,
    load_model_for_generation,
    load_transformers,
    resolve_dtype,
    resolve_local_model_path,
    slugify,
    tokenize_prompt,
)


DEFAULT_CASES = "llm_explainer/llama_vs_gemini_azd7762_a204_cases.md"
DEFAULT_OUT = "llm_explainer/llama_vs_gemini_azd7762_a204.md"
DEFAULT_PROMPT_DIR = "llm_explainer/llama_vs_gemini_azd7762_a204_prompts"
DEFAULT_MODELS = "Meta-Llama-3.1-8B-Instruct,Llama-3.3-70B-Instruct"

CASE_RE = re.compile(
    r"<!-- CASE (?P<meta>\{.*?\}) -->\s*"
    r"## Prompt\s*```text\n(?P<prompt>.*?)\n```\s*"
    r"## Gemini Response\s*```text\n(?P<gemini>.*?)\n```\s*"
    r"<!-- END_CASE -->",
    flags=re.DOTALL,
)
TAG_RE = re.compile(r"\[(?P<kind>Evidence|Stats|Context):\s*(?P<value>[^\]]+)\]")
NUMBER_RE = re.compile(r"(?<![A-Za-z0-9])[-+]?\d+(?:\.\d+)?(?![A-Za-z0-9])")
STRUCTURAL_RE = re.compile(
    r"\b(structural|structure|scaffold|chemical|moa|mechanism|inhibitor|binding)\b",
    flags=re.IGNORECASE,
)
PROBLEM_DETECTION_RE = re.compile(
    r"\b(shuffled|mismatch|mismatched|wrong drug|inconsistent|incongruent|"
    r"unreliable|cannot determine|insufficient|does not match|not supported)\b",
    flags=re.IGNORECASE,
)
TAGGED_FACT_RE = re.compile(r"\[(Evidence|Stats|Context):\s*[^\]]+\]")


@dataclass
class EvalCase:
    case_id: str
    label: str
    probe: str
    allowed_genes: list[str]
    allowed_evidence_tags: list[str]
    required_sentence_count: int
    prompt: str
    gemini_response: str


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Compare Gemini responses with Llama responses on identical raw prompts."
    )
    p.add_argument("--cases-md", default=DEFAULT_CASES, help="Markdown case file.")
    p.add_argument("--out-md", default=DEFAULT_OUT, help="Presentation-ready Markdown output.")
    p.add_argument(
        "--prompt-dir",
        default=DEFAULT_PROMPT_DIR,
        help="Directory where rendered prompts are written for inspection.",
    )
    p.add_argument(
        "--models",
        default=DEFAULT_MODELS,
        help="Comma-separated Llama model keys from generate_reports.MODEL_REGISTRY.",
    )
    p.add_argument("--max-new-tokens", type=int, default=384)
    p.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Use 0 for deterministic generation. Values >0 enable sampling.",
    )
    p.add_argument("--top-p", type=float, default=1.0)
    p.add_argument("--dry-run", action="store_true", help="Write prompts/audit Gemini only.")
    return p.parse_args()


def load_cases(path: Path) -> list[EvalCase]:
    text = path.read_text(encoding="utf-8")
    cases: list[EvalCase] = []
    for match in CASE_RE.finditer(text):
        meta = json.loads(match.group("meta"))
        cases.append(
            EvalCase(
                case_id=str(meta["id"]),
                label=str(meta["label"]),
                probe=str(meta["probe"]),
                allowed_genes=list(meta["allowed_genes"]),
                allowed_evidence_tags=list(meta["allowed_evidence_tags"]),
                required_sentence_count=int(meta.get("required_sentence_count", 3)),
                prompt=match.group("prompt").strip(),
                gemini_response=match.group("gemini").strip(),
            )
        )
    if not cases:
        raise ValueError(f"No cases found in {path}")
    return cases


def cleanup_raw_generation(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"^\s*assistant\s*:?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^\s*```(?:text|markdown)?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```\s*$", "", cleaned)
    cleaned = cleaned.replace("<|endoftext|>", "").replace("<|eot_id|>", "")
    return cleaned.strip()


def split_sentences(text: str) -> list[str]:
    stripped = re.sub(r"\s+", " ", text.strip())
    if not stripped:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", stripped)
    return [part.strip() for part in parts if part.strip()]


def normalize_number(value: str) -> str:
    try:
        return f"{float(value):.8g}"
    except ValueError:
        return value.lstrip("+")


def extract_numbers(text: str) -> set[str]:
    return {normalize_number(m.group(0)) for m in NUMBER_RE.finditer(text)}


def symbol_mentions(text: str, symbols: set[str]) -> set[str]:
    mentions: set[str] = set()
    for symbol in sorted(symbols, key=len, reverse=True):
        pattern = rf"(?<![A-Za-z0-9]){re.escape(symbol)}(?![A-Za-z0-9])"
        if re.search(pattern, text):
            mentions.add(symbol)
    return mentions


def audit_response(case: EvalCase, model_name: str, response: str, all_symbols: set[str]) -> dict[str, Any]:
    if not response or response.startswith("_Dry run only"):
        return {
            "model": model_name,
            "case_id": case.case_id,
            "generated": False,
            "sentence_count": 0,
            "sentence_count_ok": False,
            "evidence_tag_present": False,
            "median_ic50_tag_present": False,
            "context_disease_tag_present": False,
            "structural_tag_required": False,
            "structural_tag_present": False,
            "unexpected_evidence_tags": [],
            "unsupported_gene_mentions": [],
            "new_numeric_claims": [],
            "untagged_sentence_count": 0,
            "verdict": "Not generated.",
            "pass": False,
        }

    sentences = split_sentences(response)
    tags = list(TAG_RE.finditer(response))
    evidence_tags = [m.group("value").strip() for m in tags if m.group("kind") == "Evidence"]
    stats_tags = [m.group("value").strip() for m in tags if m.group("kind") == "Stats"]
    context_tags = [m.group("value").strip() for m in tags if m.group("kind") == "Context"]

    allowed_evidence = set(case.allowed_evidence_tags)
    allowed_genes = set(case.allowed_genes)
    unexpected_evidence_tags = sorted(set(evidence_tags) - allowed_evidence)
    unsupported_gene_mentions = sorted(symbol_mentions(response, all_symbols) - allowed_genes)

    prompt_numbers = extract_numbers(case.prompt)
    response_numbers = extract_numbers(response)
    new_numeric_claims = sorted(response_numbers - prompt_numbers)

    structural_required = bool(STRUCTURAL_RE.search(response))
    untagged_sentences = [s for s in sentences if not TAGGED_FACT_RE.search(s)]

    generated_pass = (
        len(sentences) == case.required_sentence_count
        and bool(evidence_tags)
        and "Median_IC50" in stats_tags
        and "Disease" in context_tags
        and (not structural_required or "Structural_Feature" in stats_tags)
        and not unexpected_evidence_tags
        and not unsupported_gene_mentions
        and not new_numeric_claims
        and not untagged_sentences
    )

    return {
        "model": model_name,
        "case_id": case.case_id,
        "generated": True,
        "sentence_count": len(sentences),
        "sentence_count_ok": len(sentences) == case.required_sentence_count,
        "evidence_tag_present": bool(evidence_tags),
        "median_ic50_tag_present": "Median_IC50" in stats_tags,
        "context_disease_tag_present": "Disease" in context_tags,
        "structural_tag_required": structural_required,
        "structural_tag_present": "Structural_Feature" in stats_tags,
        "unexpected_evidence_tags": unexpected_evidence_tags,
        "unsupported_gene_mentions": unsupported_gene_mentions,
        "new_numeric_claims": new_numeric_claims,
        "untagged_sentence_count": len(untagged_sentences),
        "verdict": probe_verdict(case, response),
        "pass": generated_pass,
    }


def probe_verdict(case: EvalCase, response: str) -> str:
    if case.probe == "sanity_check":
        return "Sanity check: evaluate citation compliance and evidence grounding."

    detects_problem = bool(PROBLEM_DETECTION_RE.search(response))
    if detects_problem:
        return "Detects or flags degraded evidence/mismatch."

    mentions = symbol_mentions(response, set(case.allowed_genes))
    target_like = {"CHEK1", "CHEK2", "EHMT1", "EHMT2"}
    non_target_mentions = mentions - target_like

    if case.probe == "shuffled_features":
        if non_target_mentions:
            return "Confidently rationalizes shuffled gene evidence; hallucination risk."
        return "Avoids shuffled genes, but does not explicitly flag degradation."

    if case.probe == "wrong_drug":
        return "Rationalizes substituted wrong-drug metadata as coherent evidence."

    return "No probe verdict configured."


def render_raw_prompt(tokenizer, prompt_text: str) -> tuple[str, bool]:
    if getattr(tokenizer, "chat_template", None):
        try:
            return (
                tokenizer.apply_chat_template(
                    [{"role": "user", "content": prompt_text}],
                    tokenize=False,
                    add_generation_prompt=True,
                ),
                True,
            )
        except Exception:
            pass
    return prompt_text, False


def model_paths(model_key: str) -> tuple[Path, Path]:
    spec = MODEL_REGISTRY[model_key]
    raw_path = Path(spec["path"]).resolve()
    path = resolve_local_model_path(raw_path)
    return path, path


def write_prompts(
    cases: list[EvalCase],
    model_key: str,
    tokenizer,
    prompt_dir: Path,
) -> list[dict[str, Any]]:
    rendered: list[dict[str, Any]] = []
    model_dir = prompt_dir / slugify(model_key)
    model_dir.mkdir(parents=True, exist_ok=True)
    for case in cases:
        rendered_prompt, used_chat = render_raw_prompt(tokenizer, case.prompt)
        prompt_file = model_dir / f"{case.case_id}.txt"
        prompt_file.write_text(case.prompt + "\n", encoding="utf-8")
        token_count = len(tokenizer(rendered_prompt, add_special_tokens=False)["input_ids"])
        rendered.append(
            {
                "case": case,
                "rendered_prompt": rendered_prompt,
                "used_chat_template": used_chat,
                "prompt_token_count": token_count,
                "prompt_file": prompt_file,
            }
        )
    return rendered


def generate_model_responses(
    cases: list[EvalCase],
    model_key: str,
    prompt_dir: Path,
    *,
    max_new_tokens: int,
    temperature: float,
    top_p: float,
    dry_run: bool,
) -> dict[str, dict[str, Any]]:
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

    import torch

    spec = MODEL_REGISTRY[model_key]
    base_model_path, tokenizer_path = model_paths(model_key)
    _AutoModelForCausalLM, AutoTokenizer = load_transformers()
    tokenizer = AutoTokenizer.from_pretrained(
        tokenizer_path,
        local_files_only=True,
        trust_remote_code=True,
    )
    configure_tokenizer(tokenizer, tokenizer_path)
    prompt_payloads = write_prompts(cases, model_key, tokenizer, prompt_dir)

    if dry_run:
        return {
            payload["case"].case_id: {
                "model": model_key,
                "response": "_Dry run only: prompt written, generation skipped._",
                "raw_output": "",
                "prompt_token_count": payload["prompt_token_count"],
                "used_chat_template": payload["used_chat_template"],
            }
            for payload in prompt_payloads
        }

    dtype = resolve_dtype(torch)
    AutoModelForCausalLM, _AutoTokenizer = load_transformers()
    model = load_model_for_generation(
        AutoModelForCausalLM=AutoModelForCausalLM,
        base_model_path=base_model_path,
        adapter_path=None,
        spec=spec,
        dtype=dtype,
        torch_module=torch,
    )

    generate_kwargs: dict[str, Any] = {
        "max_new_tokens": max_new_tokens,
        "pad_token_id": tokenizer.pad_token_id,
        "eos_token_id": tokenizer.eos_token_id,
        "repetition_penalty": float(spec["generation"].get("repetition_penalty", 1.0)),
        "do_sample": temperature > 0,
    }
    if temperature > 0:
        generate_kwargs.update({"temperature": temperature, "top_p": top_p})

    responses: dict[str, dict[str, Any]] = {}
    for payload in prompt_payloads:
        context_window = spec.get("context_window")
        max_input_tokens = None
        if context_window:
            max_input_tokens = max(256, int(context_window) - max_new_tokens - 32)
        encoded = tokenize_prompt(tokenizer, payload["rendered_prompt"], max_input_tokens)
        input_ids = encoded["input_ids"]
        attention_mask = encoded["attention_mask"]
        input_length = int(input_ids.shape[-1])
        if torch.cuda.is_available():
            input_ids = input_ids.to("cuda:0")
            attention_mask = attention_mask.to("cuda:0")
        with torch.inference_mode():
            output_ids = model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                **generate_kwargs,
            )
        raw_output = tokenizer.decode(output_ids[0, input_length:], skip_special_tokens=True)
        response = cleanup_raw_generation(raw_output)
        responses[payload["case"].case_id] = {
            "model": model_key,
            "response": response,
            "raw_output": raw_output,
            "prompt_token_count": payload["prompt_token_count"],
            "input_token_count": input_length,
            "used_chat_template": payload["used_chat_template"],
        }

    del model
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    return responses


def pass_mark(value: bool) -> str:
    return "PASS" if value else "FAIL"


def compact_list(values: list[str], empty: str = "-") -> str:
    return ", ".join(values) if values else empty


def build_markdown(
    cases: list[EvalCase],
    responses_by_model: dict[str, dict[str, dict[str, Any]]],
    audits: dict[tuple[str, str], dict[str, Any]],
    *,
    model_keys: list[str],
    max_new_tokens: int,
    temperature: float,
    dry_run: bool,
) -> str:
    generated_at = time.strftime("%Y-%m-%d %H:%M:%S %Z")
    display_models = ["Gemini"] + model_keys
    lines: list[str] = [
        "# Llama vs Gemini Same-Prompt Evaluation",
        "",
        f"Generated: {generated_at}",
        "",
        "## Configuration",
        "",
        "- Sample: AZD7762 / A-204 degraded-evidence probe.",
        f"- Llama models: {', '.join(model_keys)}.",
        f"- Deterministic decoding: temperature={temperature}, max_new_tokens={max_new_tokens}.",
        f"- Dry run: {dry_run}.",
        "- Gemini responses are copied from the supplied baseline report; Gemini is not regenerated.",
        "",
        "## Audit Summary",
        "",
        "| Condition | Model | Pass | Sentences | Required Tags | Unexpected Evidence Tags | Unsupported Genes | New Numbers | Probe Verdict |",
        "|---|---|---:|---:|---|---|---|---|---|",
    ]

    for case in cases:
        for model in display_models:
            audit = audits[(case.case_id, model)]
            required_tags = [
                "Evidence" if audit["evidence_tag_present"] else "missing Evidence",
                "Median_IC50" if audit["median_ic50_tag_present"] else "missing Median_IC50",
                "Disease" if audit["context_disease_tag_present"] else "missing Disease",
            ]
            if audit["structural_tag_required"]:
                required_tags.append(
                    "Structural_Feature"
                    if audit["structural_tag_present"]
                    else "missing Structural_Feature"
                )
            lines.append(
                "| "
                + " | ".join(
                    [
                        case.case_id,
                        model,
                        pass_mark(audit["pass"]),
                        str(audit["sentence_count"]),
                        ", ".join(required_tags),
                        compact_list(audit["unexpected_evidence_tags"]),
                        compact_list(audit["unsupported_gene_mentions"]),
                        compact_list(audit["new_numeric_claims"]),
                        audit["verdict"],
                    ]
                )
                + " |"
            )

    for case in cases:
        lines.extend(
            [
                "",
                f"## {case.label}",
                "",
                f"Probe type: `{case.probe}`",
                "",
                "<details>",
                "<summary>Prompt sent to each model</summary>",
                "",
                "```text",
                case.prompt,
                "```",
                "",
                "</details>",
                "",
            ]
        )
        for model in display_models:
            if model == "Gemini":
                response = case.gemini_response
            else:
                response = responses_by_model[model][case.case_id]["response"]
            audit = audits[(case.case_id, model)]
            lines.extend(
                [
                    f"### {model}",
                    "",
                    response.strip(),
                    "",
                    (
                        f"Audit: **{pass_mark(audit['pass'])}**; "
                        f"sentences={audit['sentence_count']}; "
                        f"unexpected Evidence tags={compact_list(audit['unexpected_evidence_tags'])}; "
                        f"unsupported genes={compact_list(audit['unsupported_gene_mentions'])}; "
                        f"new numbers={compact_list(audit['new_numeric_claims'])}."
                    ),
                    "",
                ]
            )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    model_keys = [m.strip() for m in args.models.split(",") if m.strip()]
    missing = [m for m in model_keys if m not in MODEL_REGISTRY]
    if missing:
        raise ValueError(f"Unknown model key(s): {missing}")

    cases_path = Path(args.cases_md).resolve()
    out_md = Path(args.out_md).resolve()
    prompt_dir = Path(args.prompt_dir).resolve()
    prompt_dir.mkdir(parents=True, exist_ok=True)

    cases = load_cases(cases_path)
    all_symbols = {symbol for case in cases for symbol in case.allowed_genes}

    responses_by_model: dict[str, dict[str, dict[str, Any]]] = {}
    for model_key in model_keys:
        responses_by_model[model_key] = generate_model_responses(
            cases,
            model_key,
            prompt_dir,
            max_new_tokens=args.max_new_tokens,
            temperature=args.temperature,
            top_p=args.top_p,
            dry_run=args.dry_run,
        )

    audits: dict[tuple[str, str], dict[str, Any]] = {}
    for case in cases:
        audits[(case.case_id, "Gemini")] = audit_response(
            case, "Gemini", case.gemini_response, all_symbols
        )
        for model_key in model_keys:
            audits[(case.case_id, model_key)] = audit_response(
                case,
                model_key,
                responses_by_model[model_key][case.case_id]["response"],
                all_symbols,
            )

    out_md.write_text(
        build_markdown(
            cases,
            responses_by_model,
            audits,
            model_keys=model_keys,
            max_new_tokens=args.max_new_tokens,
            temperature=args.temperature,
            dry_run=args.dry_run,
        ),
        encoding="utf-8",
    )
    print(f"Wrote Markdown comparison: {out_md}")
    print(f"Wrote rendered prompts under: {prompt_dir}")


if __name__ == "__main__":
    main()
