#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
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
        description="Normalize report_markdown fields from existing llm_explainer outputs."
    )
    parser.add_argument(
        "--outputs-root",
        default="llm_explainer/outputs",
        help="Root folder containing per-model output directories.",
    )
    parser.add_argument(
        "--model-key",
        action="append",
        default=[],
        help="Optional model directory name to normalize. Repeat to target multiple models.",
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


def cleanup_text(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"^\s*assistant\s*:?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^\s*```(?:markdown)?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```\s*$", "", cleaned)
    cleaned = cleaned.replace("<|endoftext|>", "").replace("<|eot_id|>", "")
    cleaned = re.sub(r"(?is)^.*?assistantfinal\s*", "", cleaned)
    heading_positions = [cleaned.find(heading) for heading in REQUIRED_HEADINGS if heading in cleaned]
    if heading_positions:
        cleaned = cleaned[min(heading_positions):]
    return cleaned.strip()


def build_run_markdown(model_key: str, records: list[dict[str, Any]]) -> str:
    lines = [f"# Generated Reports - {model_key}", ""]
    for rec in records:
        lines.append(f"## {rec['report_title']}")
        lines.append(f"_Source evidence: {rec['evidence_id']}_")
        lines.append("")
        lines.append(rec["report_markdown"].strip())
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    outputs_root = Path(args.outputs_root).resolve()
    target_dirs = {name for name in args.model_key}

    for model_dir in sorted(outputs_root.iterdir()) if outputs_root.exists() else []:
        if target_dirs and model_dir.name not in target_dirs:
            continue
        jsonl_path = model_dir / "reports.jsonl"
        if not jsonl_path.exists():
            continue
        rows = read_jsonl(jsonl_path)
        if not rows:
            continue

        for row in rows:
            source_text = row.get("raw_output") or row.get("report_markdown", "")
            row["report_markdown"] = cleanup_text(str(source_text))

        jsonl_path.write_text(
            "\n".join(json.dumps(row, ensure_ascii=True) for row in rows) + "\n",
            encoding="utf-8",
        )
        (model_dir / "reports.md").write_text(
            build_run_markdown(rows[0].get("model_key", model_dir.name), rows),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
