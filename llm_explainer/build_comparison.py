#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from statistics import mean
from pathlib import Path
from typing import Any

REQUIRED_HEADINGS = [
    "## Executive Summary",
    "## Evidence-Based Interpretation",
    "## Feature and Neighborhood Analysis",
    "## Model-Level Context",
    "## Confidence and Caveats",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a side-by-side markdown comparison from per-model report outputs."
    )
    parser.add_argument(
        "--reports",
        default="llm_explainer/shap_sample_reports.jsonl",
        help="Source structured reports JSONL.",
    )
    parser.add_argument(
        "--outputs-root",
        default="llm_explainer/outputs",
        help="Folder containing per-model output subdirectories.",
    )
    parser.add_argument(
        "--out-file",
        default="llm_explainer/model_comparison.md",
        help="Final comparison markdown file.",
    )
    return parser.parse_args()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def title_for_report(report: dict[str, Any]) -> str:
    drug = report.get("drug", {}).get("name", "unknown drug")
    cell = report.get("cell_line", {}).get("name", "unknown cell line")
    return f"{report.get('report_id', 'RPT-UNK')} - {drug} on {cell}"


def build_source_snapshot(report: dict[str, Any]) -> list[str]:
    cell = report.get("cell_line", {})
    lines = [
        f"- source_type: {report.get('source_type', 'dem_neighbor_bundle')}",
        f"- evidence_id: {report.get('evidence_id', 'n/a')}",
        f"- observed_auc: {report.get('query_y_true', 0):.4f}",
        f"- interpretation: {report.get('interpretation', 'n/a')}",
        f"- tissue / histology: {cell.get('tissue', 'n/a')} / {cell.get('histology', 'n/a')}",
    ]
    if "model_predicted_auc" in report:
        lines.append(f"- model_predicted_auc: {report.get('model_predicted_auc', 0):.4f}")
        lines.append(f"- prediction_error: {report.get('prediction_error', 0):+.4f}")
        lines.append(f"- selection_reason: {report.get('selection_reason', 'n/a')}")
    else:
        lines.append(f"- neighborhood_weighted_auc: {report.get('neighborhood_y_weighted_mean', 0):.4f}")
    return lines


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def heading_coverage(text: str) -> float:
    present = 0
    for heading in REQUIRED_HEADINGS:
        pattern = rf"(?m)^{re.escape(heading)}\s*$"
        if re.search(pattern, text):
            present += 1
    return present / len(REQUIRED_HEADINGS)


def unique_line_ratio(text: str) -> float:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return 0.0
    return len(set(lines)) / len(lines)


def report_score(text: str) -> float:
    words = word_count(text)
    word_factor = min(words / 250.0, 1.0)
    return 100.0 * heading_coverage(text) * unique_line_ratio(text) * word_factor


def summary_note(
    reports_present: int,
    expected_reports: int,
    avg_heading_coverage: float,
    avg_unique_ratio: float,
    avg_words: float,
) -> str:
    if reports_present < expected_reports:
        return "missing outputs"
    if avg_heading_coverage < 0.6:
        return "weak format following"
    if avg_unique_ratio < 0.45:
        return "heavy repetition"
    if avg_words < 120:
        return "too short"
    return "usable"


def summarize_model(
    model_key: str,
    rows_by_report: dict[str, dict[str, Any]],
    expected_reports: int,
) -> dict[str, Any]:
    texts = [row.get("report_markdown", "") for row in rows_by_report.values()]
    avg_words = mean(word_count(text) for text in texts) if texts else 0.0
    avg_heading = mean(heading_coverage(text) for text in texts) if texts else 0.0
    avg_unique = mean(unique_line_ratio(text) for text in texts) if texts else 0.0
    avg_score = mean(report_score(text) for text in texts) if texts else 0.0
    return {
        "model_key": model_key,
        "reports_present": len(rows_by_report),
        "expected_reports": expected_reports,
        "avg_words": avg_words,
        "avg_heading_coverage": avg_heading,
        "avg_unique_ratio": avg_unique,
        "avg_score": avg_score,
        "note": summary_note(len(rows_by_report), expected_reports, avg_heading, avg_unique, avg_words),
    }


def main() -> None:
    args = parse_args()
    reports_path = Path(args.reports).resolve()
    outputs_root = Path(args.outputs_root).resolve()
    out_file = Path(args.out_file).resolve()
    out_file.parent.mkdir(parents=True, exist_ok=True)

    source_reports = read_jsonl(reports_path)
    reports_by_id = {row["report_id"]: row for row in source_reports}

    model_outputs: dict[str, dict[str, dict[str, Any]]] = {}
    for model_dir in sorted(outputs_root.iterdir()) if outputs_root.exists() else []:
        jsonl_path = model_dir / "reports.jsonl"
        if not jsonl_path.exists():
            continue
        rows = read_jsonl(jsonl_path)
        if not rows:
            continue
        model_key = rows[0].get("model_key", model_dir.name)
        model_outputs[model_key] = {row["report_id"]: row for row in rows}

    lines: list[str] = ["# Model Comparison", ""]
    lines.append("This file collates the generated markdown reports for each model.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("The heuristic score below is a rough quality indicator based on section coverage, output length, and repetition. Higher is better.")
    lines.append("")

    summaries = sorted(
        (
            summarize_model(model_key, rows_by_report, len(reports_by_id))
            for model_key, rows_by_report in model_outputs.items()
        ),
        key=lambda row: row["avg_score"],
        reverse=True,
    )
    lines.append("| Model | Reports | Avg Words | Heading Coverage | Unique-Line Ratio | Heuristic Score | Note |")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: | --- |")
    for summary in summaries:
        lines.append(
            "| "
            f"{summary['model_key']} | "
            f"{summary['reports_present']}/{summary['expected_reports']} | "
            f"{summary['avg_words']:.1f} | "
            f"{summary['avg_heading_coverage']:.2f} | "
            f"{summary['avg_unique_ratio']:.2f} | "
            f"{summary['avg_score']:.1f} | "
            f"{summary['note']} |"
        )
    if not summaries:
        lines.append("| none | 0/0 | 0.0 | 0.00 | 0.00 | 0.0 | no outputs |")
    lines.append("")
    lines.append("## Models Present")
    for model_key in [summary["model_key"] for summary in summaries]:
        lines.append(f"- {model_key}")
    if not model_outputs:
        lines.append("- none")
    lines.append("")

    for report_id in sorted(reports_by_id):
        src = reports_by_id[report_id]
        lines.append(f"## {title_for_report(src)}")
        lines.append("")
        lines.append("### Source Snapshot")
        lines.extend(build_source_snapshot(src))
        lines.append("")
        for model_key in sorted(model_outputs):
            row = model_outputs[model_key].get(report_id)
            if row is None:
                lines.append(f"### {model_key}")
                lines.append("_No output found for this report._")
                lines.append("")
                continue
            text = row.get("report_markdown", "")
            lines.append(
                f"### {model_key} "
                f"(score={report_score(text):.1f}, words={word_count(text)}, headings={heading_coverage(text):.2f})"
            )
            row = model_outputs[model_key].get(report_id)
            lines.append(text.strip() or "_Empty output._")
            lines.append("")
        lines.append("---")
        lines.append("")

    out_file.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
