#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from statistics import mean
from typing import Any

from build_comparison import (
    build_source_snapshot,
    heading_coverage,
    report_score,
    title_for_report,
    unique_line_ratio,
    word_count,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare base and SFT report generations on a held-out report bundle."
    )
    parser.add_argument(
        "--reports",
        required=True,
        help="Held-out structured reports JSONL.",
    )
    parser.add_argument(
        "--base-reports-jsonl",
        required=True,
        help="Base-model generated reports JSONL for the held-out split.",
    )
    parser.add_argument(
        "--sft-reports-jsonl",
        required=True,
        help="SFT-model generated reports JSONL for the held-out split.",
    )
    parser.add_argument(
        "--reference-pairs-jsonl",
        default="",
        help="Optional teacher/reference instruction-pairs JSONL for the same held-out split.",
    )
    parser.add_argument(
        "--base-label",
        default="Base",
        help="Display label for the base model run.",
    )
    parser.add_argument(
        "--sft-label",
        default="SFT",
        help="Display label for the SFT run.",
    )
    parser.add_argument(
        "--out-file",
        default="llm_explainer/sft_vs_base_comparison.md",
        help="Output markdown report.",
    )
    return parser.parse_args()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def normalize_tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9_]+", text.lower())


def token_f1(prediction: str, reference: str) -> float:
    pred_tokens = normalize_tokens(prediction)
    ref_tokens = normalize_tokens(reference)
    if not pred_tokens or not ref_tokens:
        return 0.0
    pred_counts = Counter(pred_tokens)
    ref_counts = Counter(ref_tokens)
    overlap = sum(min(pred_counts[token], ref_counts[token]) for token in pred_counts)
    precision = overlap / max(1, len(pred_tokens))
    recall = overlap / max(1, len(ref_tokens))
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def summarize_run(
    *,
    label: str,
    rows_by_report: dict[str, dict[str, Any]],
    report_ids: list[str],
    reference_by_report: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    texts = [rows_by_report.get(report_id, {}).get("report_markdown", "") for report_id in report_ids]
    ref_scores: list[float] = []
    for report_id in report_ids:
        row = rows_by_report.get(report_id)
        ref = reference_by_report.get(report_id)
        if row is None or ref is None:
            continue
        ref_scores.append(token_f1(row.get("report_markdown", ""), ref.get("output", "")))

    return {
        "label": label,
        "reports_present": sum(1 for report_id in report_ids if report_id in rows_by_report),
        "expected_reports": len(report_ids),
        "avg_words": mean(word_count(text) for text in texts) if texts else 0.0,
        "avg_heading_coverage": mean(heading_coverage(text) for text in texts) if texts else 0.0,
        "avg_unique_ratio": mean(unique_line_ratio(text) for text in texts) if texts else 0.0,
        "avg_score": mean(report_score(text) for text in texts) if texts else 0.0,
        "avg_reference_f1": mean(ref_scores) if ref_scores else 0.0,
    }


def describe_winner(base_summary: dict[str, Any], sft_summary: dict[str, Any]) -> str:
    wins = 0
    if sft_summary["avg_score"] > base_summary["avg_score"]:
        wins += 1
    if sft_summary["avg_heading_coverage"] > base_summary["avg_heading_coverage"]:
        wins += 1
    if sft_summary["avg_reference_f1"] > base_summary["avg_reference_f1"]:
        wins += 1
    if wins >= 2:
        return f"{sft_summary['label']} looks stronger on the held-out split."
    return f"{base_summary['label']} remains competitive on the held-out split."


def main() -> None:
    args = parse_args()

    reports = read_jsonl(Path(args.reports).resolve())
    report_ids = [row["report_id"] for row in reports]
    reports_by_id = {row["report_id"]: row for row in reports}

    base_rows = read_jsonl(Path(args.base_reports_jsonl).resolve())
    sft_rows = read_jsonl(Path(args.sft_reports_jsonl).resolve())
    base_by_report = {row["report_id"]: row for row in base_rows}
    sft_by_report = {row["report_id"]: row for row in sft_rows}

    reference_by_report: dict[str, dict[str, Any]] = {}
    if args.reference_pairs_jsonl:
        reference_rows = read_jsonl(Path(args.reference_pairs_jsonl).resolve())
        reference_by_report = {row["report_id"]: row for row in reference_rows}

    base_summary = summarize_run(
        label=args.base_label,
        rows_by_report=base_by_report,
        report_ids=report_ids,
        reference_by_report=reference_by_report,
    )
    sft_summary = summarize_run(
        label=args.sft_label,
        rows_by_report=sft_by_report,
        report_ids=report_ids,
        reference_by_report=reference_by_report,
    )

    lines: list[str] = [
        "# SFT vs Base Comparison",
        "",
        describe_winner(base_summary, sft_summary),
        "",
        "## Summary",
        "",
        "| Run | Reports | Avg Words | Heading Coverage | Unique-Line Ratio | Heuristic Score | Teacher Token-F1 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {base_summary['label']} | {base_summary['reports_present']}/{base_summary['expected_reports']} | "
            f"{base_summary['avg_words']:.1f} | {base_summary['avg_heading_coverage']:.2f} | "
            f"{base_summary['avg_unique_ratio']:.2f} | {base_summary['avg_score']:.1f} | "
            f"{base_summary['avg_reference_f1']:.3f} |"
        ),
        (
            f"| {sft_summary['label']} | {sft_summary['reports_present']}/{sft_summary['expected_reports']} | "
            f"{sft_summary['avg_words']:.1f} | {sft_summary['avg_heading_coverage']:.2f} | "
            f"{sft_summary['avg_unique_ratio']:.2f} | {sft_summary['avg_score']:.1f} | "
            f"{sft_summary['avg_reference_f1']:.3f} |"
        ),
        "",
    ]

    for report_id in sorted(report_ids):
        source_report = reports_by_id[report_id]
        base_row = base_by_report.get(report_id, {})
        sft_row = sft_by_report.get(report_id, {})
        ref_row = reference_by_report.get(report_id, {})

        lines.append(f"## {title_for_report(source_report)}")
        lines.append("")
        lines.append("### Source Snapshot")
        lines.extend(build_source_snapshot(source_report))
        lines.append("")
        if ref_row:
            lines.append("### Teacher Reference")
            lines.append(ref_row.get("output", "").strip() or "_No teacher output found._")
            lines.append("")
        lines.append(
            f"### {args.base_label} "
            f"(score={report_score(base_row.get('report_markdown', '')):.1f}, "
            f"words={word_count(base_row.get('report_markdown', ''))})"
        )
        lines.append(base_row.get("report_markdown", "").strip() or "_No base output found._")
        lines.append("")
        lines.append(
            f"### {args.sft_label} "
            f"(score={report_score(sft_row.get('report_markdown', '')):.1f}, "
            f"words={word_count(sft_row.get('report_markdown', ''))})"
        )
        lines.append(sft_row.get("report_markdown", "").strip() or "_No SFT output found._")
        lines.append("")
        lines.append("---")
        lines.append("")

    out_file = Path(args.out_file).resolve()
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
