#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert teacher-generated instruction pairs into SFT-friendly JSONL formats."
    )
    parser.add_argument(
        "--train-pairs",
        required=True,
        help="Instruction-pair JSONL for the training split.",
    )
    parser.add_argument(
        "--val-pairs",
        default="",
        help="Optional instruction-pair JSONL for the validation split.",
    )
    parser.add_argument(
        "--out-dir",
        default="llm_explainer/sft_dataset",
        help="Output directory for the exported SFT datasets.",
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


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as fout:
        for row in rows:
            fout.write(json.dumps(row, ensure_ascii=True) + "\n")


def normalize_pairs(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cleaned: list[dict[str, Any]] = []
    for row in rows:
        output = str(row.get("output", "")).strip()
        if not output:
            continue
        cleaned.append(row)
    return cleaned


def to_messages(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    output_rows: list[dict[str, Any]] = []
    for row in rows:
        output_rows.append(
            {
                "report_id": row["report_id"],
                "report_title": row.get("report_title", row["report_id"]),
                "split": row.get("split", ""),
                "messages": [
                    {"role": "system", "content": row["system_prompt"]},
                    {"role": "user", "content": row["input"]},
                    {"role": "assistant", "content": row["output"]},
                ],
            }
        )
    return output_rows


def to_alpaca(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    output_rows: list[dict[str, Any]] = []
    for row in rows:
        output_rows.append(
            {
                "report_id": row["report_id"],
                "report_title": row.get("report_title", row["report_id"]),
                "split": row.get("split", ""),
                "instruction": row["system_prompt"],
                "input": row["input"],
                "output": row["output"],
            }
        )
    return output_rows


def main() -> None:
    args = parse_args()

    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    train_rows = normalize_pairs(read_jsonl(Path(args.train_pairs).resolve()))
    val_rows = normalize_pairs(read_jsonl(Path(args.val_pairs).resolve())) if args.val_pairs else []

    write_jsonl(out_dir / "train_messages.jsonl", to_messages(train_rows))
    write_jsonl(out_dir / "train_alpaca.jsonl", to_alpaca(train_rows))

    if val_rows:
        write_jsonl(out_dir / "val_messages.jsonl", to_messages(val_rows))
        write_jsonl(out_dir / "val_alpaca.jsonl", to_alpaca(val_rows))

    summary = {
        "train_examples": len(train_rows),
        "val_examples": len(val_rows),
        "train_pairs_path": str(Path(args.train_pairs).resolve()),
        "val_pairs_path": str(Path(args.val_pairs).resolve()) if args.val_pairs else "",
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
