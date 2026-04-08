#!/usr/bin/env python3
"""
Generate grounded biomedical explanations from enriched reports via Gemini 2.5.

Reads enriched sample_reports.jsonl, sends each to Gemini with a structured
prompt, and writes LLM-generated explanations as JSONL + Markdown.

Requirements:
  export GEMINI_API_KEY=your_key_here
  pip install openai   (already in environment.yml)

Usage:
  python train/generate_explanations.py
  python train/generate_explanations.py --model gemini-2.5-pro-preview-03-25 --num-reports 5
"""
from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

from openai import OpenAI


GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

SYSTEM_PROMPT = """\
You are a pharmacogenomics expert writing grounded biomedical explanations of \
drug efficacy predictions. Every claim must be traceable to the data provided. \
Do not speculate beyond the evidence. Use precise molecular and clinical terminology.\
"""

REPORT_TEMPLATE = """\
Given this drug efficacy prediction report, write a grounded biomedical explanation.

## Sample Identity
- Drug: {drug_name} ({mechanism})
- Gene Target: {gene_target}
- Cell Line: {cell_line} ({tissue} — {histology}{subtype_str})

## Response Data
- Observed AUC: {y_true:.4f}
- Kernel neighborhood weighted AUC: {y_pred:.4f}
- Global mean AUC: 12.8613
- Interpretation: {interpretation}

## Key Distinguishing Molecular Features (ranked by z-score)
{feature_block}

## Nearest Neighbors
{neighbor_block}

---

Write a 3-paragraph explanation:
1. **Prediction summary**: Is this drug effective on this cell line? How does \
the observed AUC compare to the neighborhood and global baselines? What does \
this mean biologically?
2. **Feature analysis**: How do the top molecular substructure features relate \
to the drug's known mechanism and the cell line's cancer biology? Be specific \
about which SMARTS patterns or functional groups may be pharmacologically relevant.
3. **Confidence and limitations**: How strong is the neighborhood evidence \
(kernel scores, number of neighbors, consistency of neighbor AUCs)? What are \
the caveats of this analysis?

Be specific about molecular mechanisms. Ground every claim in the data above.\
"""


def _build_feature_block(features: list[dict]) -> str:
    lines = []
    for i, f in enumerate(features, 1):
        fname = f["feature"]
        smarts = f.get("substructure_smarts", "")
        examples = f.get("example_drugs", [])
        pct = f.get("pct_drugs_with_bit", 0)
        line = (
            f"{i}. **{fname}** ({f['direction']}; z={f['z_score']:.2f}, "
            f"neighborhood={f['neighborhood_mean']:.3f} vs global={f['global_mean']:.3f})"
        )
        extras = []
        if smarts:
            extras.append(f"SMARTS: {smarts}")
        if examples:
            extras.append(f"e.g. {', '.join(examples[:3])}")
        if pct:
            extras.append(f"{pct:.0f}% of drugs")
        if extras:
            line += f"\n   [{'; '.join(extras)}]"
        lines.append(line)
    return "\n".join(lines) if lines else "(none)"


def _build_neighbor_block(neighbors: list[dict]) -> str:
    if not neighbors:
        return "(none)"
    lines = ["| Drug | Cell Line | Tissue | AUC | Kernel Score |",
             "|------|-----------|--------|-----|-------------|"]
    for n in neighbors:
        lines.append(
            f"| {n.get('drug_name', '?')} "
            f"| {n.get('cell_line', '?')} "
            f"| {n.get('tissue', '')} "
            f"| {n.get('y', 0):.4f} "
            f"| {n.get('kernel_score', 0):.4f} |"
        )
    return "\n".join(lines)


def build_prompt(report: dict) -> str:
    drug = report.get("drug", {})
    cell = report.get("cell_line", {})
    subtype = cell.get("subtype", "")
    subtype_str = f", {subtype}" if subtype else ""

    return REPORT_TEMPLATE.format(
        drug_name=drug.get("name", "unknown"),
        mechanism=drug.get("mechanism", "unknown"),
        gene_target=drug.get("gene_target", "unknown"),
        cell_line=cell.get("name", "unknown"),
        tissue=cell.get("tissue", "unknown"),
        histology=cell.get("histology", "unknown"),
        subtype_str=subtype_str,
        y_true=report.get("query_y_true", 0),
        y_pred=report.get("neighborhood_y_weighted_mean", 0),
        interpretation=report.get("interpretation", ""),
        feature_block=_build_feature_block(
            report.get("enriched_features", [])
        ),
        neighbor_block=_build_neighbor_block(
            report.get("neighbor_details", [])
        ),
    )


def call_gemini(
    client: OpenAI,
    prompt: str,
    model: str,
    temperature: float = 0.3,
    max_tokens: int = 2048,
    max_retries: int = 3,
) -> str:
    for attempt in range(max_retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return resp.choices[0].message.content
        except Exception as e:
            wait = 2 ** (attempt + 1)
            print(f"  Attempt {attempt + 1} failed: {e}. Retrying in {wait}s...")
            time.sleep(wait)
    raise RuntimeError(f"Failed after {max_retries} attempts")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate biomedical explanations via Gemini 2.5."
    )
    parser.add_argument(
        "--reports", default="results/dem/sample_reports.jsonl",
        help="Enriched reports JSONL from report_generator.py.",
    )
    parser.add_argument(
        "--out-jsonl", default="results/dem/explanations.jsonl",
    )
    parser.add_argument(
        "--out-md", default="results/dem/explanations.md",
    )
    parser.add_argument(
        "--model", default="gemini-2.5-flash-preview-04-17",
        help="Gemini model name.",
    )
    parser.add_argument("--num-reports", type=int, default=0,
                        help="Limit reports to process (0 = all).")
    parser.add_argument("--temperature", type=float, default=0.3)
    parser.add_argument("--max-tokens", type=int, default=2048)
    parser.add_argument("--delay", type=float, default=1.0,
                        help="Seconds between API calls (rate limiting).")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Set GEMINI_API_KEY or GOOGLE_API_KEY environment variable.\n"
            "Get a key at https://aistudio.google.com/apikey"
        )

    client = OpenAI(api_key=api_key, base_url=GEMINI_BASE_URL)

    reports_path = Path(args.reports).resolve()
    out_jsonl = Path(args.out_jsonl).resolve()
    out_md = Path(args.out_md).resolve()
    out_md.parent.mkdir(parents=True, exist_ok=True)

    print(f"Loading reports from {reports_path}...")
    with reports_path.open() as f:
        reports = [json.loads(line) for line in f if line.strip()]

    if args.num_reports > 0:
        reports = reports[: args.num_reports]
    print(f"Processing {len(reports)} reports with {args.model}...")

    md_parts = ["# LLM-Generated Biomedical Explanations", ""]
    results: list[dict] = []

    for i, report in enumerate(reports, 1):
        rid = report.get("report_id", f"RPT-{i:04d}")
        drug_name = report.get("drug", {}).get("name", "?")
        cell_name = report.get("cell_line", {}).get("name", "?")
        print(f"  [{i}/{len(reports)}] {rid}: {drug_name} on {cell_name}...")

        prompt = build_prompt(report)
        explanation = call_gemini(
            client, prompt, args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
        )

        results.append({
            "report_id": rid,
            "evidence_id": report.get("evidence_id", ""),
            "drug": drug_name,
            "cell_line": cell_name,
            "prompt": prompt,
            "explanation": explanation,
            "model": args.model,
        })

        md_parts.append(f"## {rid} — {drug_name} on {cell_name}")
        md_parts.append(f"*Model: {args.model}*\n")
        md_parts.append(explanation)
        md_parts.append("\n---\n")

        if i < len(reports):
            time.sleep(args.delay)

    with out_jsonl.open("w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=True) + "\n")

    out_md.write_text("\n".join(md_parts), encoding="utf-8")
    print(f"\nWrote: {out_jsonl}")
    print(f"Wrote: {out_md}")
    print("Done.")


if __name__ == "__main__":
    main()
