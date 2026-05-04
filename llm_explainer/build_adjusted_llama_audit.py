#!/usr/bin/env python3
"""Build a presentation-friendly adjusted audit from a same-prompt report."""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

from llama_vs_gemini_eval import (
    EvalCase,
    audit_response,
    load_cases,
    split_sentences,
)


DEFAULT_SOURCE = "llm_explainer/llama_vs_gemini_azd7762_a204_8b.md"
DEFAULT_CASES = "llm_explainer/llama_vs_gemini_azd7762_a204_cases.md"
DEFAULT_OUT = "llm_explainer/llama_vs_gemini_azd7762_a204_8b_adjusted_audit.md"

CONDITION_RE = re.compile(
    r"## (?P<label>Condition #[^\n]+)\n(?P<body>.*?)(?=\n## Condition #|\Z)",
    flags=re.DOTALL,
)
MODEL_RE = re.compile(
    r"### (?P<model>[^\n]+)\n\n(?P<response>.*?)(?=\nAudit: \*\*)",
    flags=re.DOTALL,
)
ANY_TAG_RE = re.compile(r"\[(?P<kind>[A-Za-z_]+):\s*(?P<value>[^\]]+)\]")
ENTREZ_SUFFIX_RE = re.compile(r"\s*\(\d+\)\s*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create an adjusted audit table for Llama/Gemini degraded-evidence results."
    )
    parser.add_argument("--source-md", default=DEFAULT_SOURCE)
    parser.add_argument("--cases-md", default=DEFAULT_CASES)
    parser.add_argument("--out-md", default=DEFAULT_OUT)
    return parser.parse_args()


def normalize_evidence(value: str) -> str:
    return ENTREZ_SUFFIX_RE.sub("", value.strip())


def extract_responses(source_md: Path, cases: list[EvalCase]) -> dict[tuple[str, str], str]:
    text = source_md.read_text(encoding="utf-8")
    label_to_case = {case.label: case.case_id for case in cases}
    responses: dict[tuple[str, str], str] = {}
    for condition in CONDITION_RE.finditer(text):
        case_id = label_to_case.get(condition.group("label").strip())
        if not case_id:
            continue
        for model_match in MODEL_RE.finditer(condition.group("body")):
            model = model_match.group("model").strip()
            response = model_match.group("response").strip()
            responses[(case_id, model)] = response
    missing = [
        (case.case_id, model)
        for case in cases
        for model in ("Gemini", "Meta-Llama-3.1-8B-Instruct")
        if (case.case_id, model) not in responses
    ]
    if missing:
        raise ValueError(f"Could not parse responses for: {missing}")
    return responses


def adjusted_audit(case: EvalCase, response: str) -> dict[str, Any]:
    tags = list(ANY_TAG_RE.finditer(response))
    raw_evidence_tags = [
        m.group("value").strip()
        for m in tags
        if m.group("kind") == "Evidence"
    ]
    evidence_tags = [
        normalize_evidence(value)
        for value in raw_evidence_tags
    ]
    normalized_evidence_notes = sorted(
        {
            f"{raw} -> {normalize_evidence(raw)}"
            for raw in raw_evidence_tags
            if raw != normalize_evidence(raw)
        }
    )
    stats_tags = [m.group("value").strip() for m in tags if m.group("kind") == "Stats"]
    context_tags = [m.group("value").strip() for m in tags if m.group("kind") == "Context"]
    invalid_tag_kinds = sorted(
        {
            m.group("kind")
            for m in tags
            if m.group("kind") not in {"Evidence", "Stats", "Context"}
        }
    )
    allowed = set(case.allowed_evidence_tags)
    unexpected = sorted(set(evidence_tags) - allowed)
    sentence_count = len(split_sentences(response))
    required_tags_ok = (
        bool(evidence_tags)
        and "Median_IC50" in stats_tags
        and "Disease" in context_tags
        and (
            "Structural_Feature" in stats_tags
            or not re.search(r"\b(structural|scaffold|chemical|mechanism|inhibitor)\b", response, re.I)
        )
    )
    citation_grounding_ok = required_tags_ok and not unexpected

    detects_problem = re.search(
        r"\b(shuffled|mismatch|wrong drug|inconsistent|unreliable|not supported|cannot determine)\b",
        response,
        flags=re.I,
    )
    uses_non_target_gene = bool(
        set(re.findall(r"\[Evidence:\s*([A-Za-z0-9]+)", response))
        - {"CHEK1", "CHEK2", "EHMT1", "EHMT2"}
    )
    if case.probe == "sanity_check":
        probe_status = "not applicable"
    elif detects_problem:
        probe_status = "detects degraded evidence"
    elif case.probe == "shuffled_features" and uses_non_target_gene:
        probe_status = "rationalizes shuffled feature"
    else:
        probe_status = "rationalizes mismatch"

    if case.probe == "sanity_check":
        if citation_grounding_ok and sentence_count == case.required_sentence_count and not invalid_tag_kinds:
            adjusted_status = "PASS"
        elif citation_grounding_ok:
            adjusted_status = "PARTIAL"
        else:
            adjusted_status = "FAIL"
    else:
        adjusted_status = "PASS" if probe_status == "detects degraded evidence" else "FAIL"

    return {
        "adjusted_status": adjusted_status,
        "sentence_count": sentence_count,
        "sentence_ok": sentence_count == case.required_sentence_count,
        "citation_grounding_ok": citation_grounding_ok,
        "normalized_unexpected_evidence": unexpected,
        "normalized_evidence_notes": normalized_evidence_notes,
        "invalid_tag_kinds": invalid_tag_kinds,
        "probe_status": probe_status,
    }


def fmt_bool(value: bool) -> str:
    return "yes" if value else "no"


def fmt_list(values: list[str]) -> str:
    return ", ".join(values) if values else "-"


def build_markdown(
    cases: list[EvalCase],
    responses: dict[tuple[str, str], str],
    strict: dict[tuple[str, str], dict[str, Any]],
    adjusted: dict[tuple[str, str], dict[str, Any]],
    source_md: Path,
) -> str:
    models = ["Gemini", "Meta-Llama-3.1-8B-Instruct"]
    try:
        source_display = source_md.relative_to(Path.cwd())
    except ValueError:
        source_display = source_md
    lines = [
        "# Adjusted Llama vs Gemini Audit",
        "",
        f"Source report: `{source_display}`",
        "",
        "## How To Read This",
        "",
        "- **Strict pass** keeps the original machine-contract rule: exactly 3 sentences, exact tag spelling, no unsupported Evidence tags, no new numbers.",
        "- **Adjusted status** separates presentation interpretation from strict formatting. Entrez suffixes in Evidence tags are normalized, and sentence-count mistakes become format warnings.",
        "- Degraded conditions still fail if the model confidently rationalizes shuffled features or the wrong-drug setup.",
        "",
        "## Adjusted Summary",
        "",
        "| Condition | Model | Strict Pass | Adjusted Status | Sentences | Citation Grounding | Format / Tag Warnings | Probe Status |",
        "|---|---|---:|---:|---:|---:|---|---|",
    ]
    for case in cases:
        for model in models:
            key = (case.case_id, model)
            adj = adjusted[key]
            warnings: list[str] = []
            if not adj["sentence_ok"]:
                warnings.append(f"expected 3 sentences, got {adj['sentence_count']}")
            if adj["invalid_tag_kinds"]:
                warnings.append(f"invalid tag kind(s): {fmt_list(adj['invalid_tag_kinds'])}")
            if adj["normalized_unexpected_evidence"]:
                warnings.append(
                    f"unexpected Evidence: {fmt_list(adj['normalized_unexpected_evidence'])}"
                )
            if adj["normalized_evidence_notes"]:
                warnings.append(f"normalized Evidence tag(s): {fmt_list(adj['normalized_evidence_notes'])}")
            lines.append(
                "| "
                + " | ".join(
                    [
                        case.case_id,
                        model,
                        "PASS" if strict[key]["pass"] else "FAIL",
                        adj["adjusted_status"],
                        str(adj["sentence_count"]),
                        fmt_bool(adj["citation_grounding_ok"]),
                        "; ".join(warnings) if warnings else "-",
                        adj["probe_status"],
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- **Real features:** Gemini passes the strict contract. Llama is **PARTIAL**: it copied the key IC50/tag evidence and did not introduce new numbers, but it ignored the exact 3-sentence constraint and used a non-contract `[Mechanism: ...]` tag.",
            "- **Shuffled features:** both models fail the scientific probe because they give confident explanations from shuffled gene evidence instead of flagging the degraded input.",
            "- **Wrong drug:** both models fail the scientific probe because they rationalize the substituted UNC0638 setup rather than detecting the metadata mismatch.",
            "",
            "## Bottom Line For Slide",
            "",
            "Gemini follows the requested output format better, but both Gemini and Llama are vulnerable to degraded-evidence probes. Llama 8B is especially weak on instruction following: it over-generates, uses non-contract tags, and sometimes includes Entrez IDs inside `[Evidence: ...]` tags.",
            "",
            "## Responses",
            "",
        ]
    )
    for case in cases:
        lines.extend([f"### {case.label}", ""])
        for model in models:
            key = (case.case_id, model)
            lines.extend(
                [
                    f"#### {model}",
                    "",
                    responses[key].strip(),
                    "",
                    (
                        f"Adjusted status: **{adjusted[key]['adjusted_status']}**; "
                        f"strict pass: **{'PASS' if strict[key]['pass'] else 'FAIL'}**."
                    ),
                    "",
                ]
            )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    cases = load_cases(Path(args.cases_md).resolve())
    source_md = Path(args.source_md).resolve()
    responses = extract_responses(source_md, cases)
    all_symbols = {symbol for case in cases for symbol in case.allowed_genes}

    strict: dict[tuple[str, str], dict[str, Any]] = {}
    adjusted: dict[tuple[str, str], dict[str, Any]] = {}
    for case in cases:
        for model in ("Gemini", "Meta-Llama-3.1-8B-Instruct"):
            key = (case.case_id, model)
            strict[key] = audit_response(case, model, responses[key], all_symbols)
            adjusted[key] = adjusted_audit(case, responses[key])

    out_md = Path(args.out_md).resolve()
    out_md.write_text(build_markdown(cases, responses, strict, adjusted, source_md), encoding="utf-8")
    print(f"Wrote adjusted audit: {out_md}")


if __name__ == "__main__":
    main()
