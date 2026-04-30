#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
import math
import random
from pathlib import Path
from typing import Any

from build_shap_reports import render_markdown_report
from generate_reports import (
    MODEL_REGISTRY,
    build_aux_context,
    build_system_prompt,
    load_global_context,
    read_jsonl,
    report_title,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare a teacher-generation and SFT experiment from structured SHAP reports "
            "using deterministic train/val/test splits."
        )
    )
    parser.add_argument(
        "--reports-jsonl",
        default="llm_explainer/shap_sample_reports.jsonl",
        help="Structured SHAP reports JSONL.",
    )
    parser.add_argument(
        "--results-root",
        default="results",
        help="Root folder that contains dem/, tuning/, and rf_plots/.",
    )
    parser.add_argument(
        "--out-dir",
        default="llm_explainer/sft_experiment",
        help="Experiment output folder.",
    )
    parser.add_argument(
        "--teacher-model",
        default="models--meta-llama--Llama-3.3-70B-Instruct",
        help="Teacher model name recorded in the request bundles.",
    )
    parser.add_argument(
        "--prompt-model-key",
        default="Meta-Llama-3.1-8B-Instruct",
        choices=sorted(MODEL_REGISTRY),
        help="Prompt profile used to build system prompts and global context.",
    )
    parser.add_argument(
        "--prompt-style",
        choices=["short_rpt", "full_rpt"],
        default="short_rpt",
        help="Whether to build compact or full RPT-style inputs.",
    )
    parser.add_argument(
        "--train-fraction",
        type=float,
        default=0.8,
        help="Fraction of reports assigned to the training split.",
    )
    parser.add_argument(
        "--val-fraction",
        type=float,
        default=0.1,
        help="Fraction of reports assigned to the validation split.",
    )
    parser.add_argument(
        "--test-fraction",
        type=float,
        default=0.1,
        help="Fraction of reports assigned to the held-out test split.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=13,
        help="Random seed used for the deterministic split.",
    )
    parser.add_argument(
        "--short-features",
        type=int,
        default=5,
        help="How many top features to keep in short RPT prompts.",
    )
    parser.add_argument(
        "--short-same-drug",
        type=int,
        default=2,
        help="How many same-drug cohort examples to keep in short RPT prompts.",
    )
    parser.add_argument(
        "--short-same-cell",
        type=int,
        default=2,
        help="How many same-cell cohort examples to keep in short RPT prompts.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing experiment directory.",
    )
    return parser.parse_args()


def ensure_empty_dir(path: Path, overwrite: bool) -> None:
    path.mkdir(parents=True, exist_ok=True)
    if not overwrite:
        existing = list(path.iterdir())
        if existing:
            raise FileExistsError(
                f"{path} already contains files. Re-run with --overwrite to replace them."
            )


def stratify_key(report: dict[str, Any]) -> str:
    error = float(report.get("prediction_error", 0.0))
    if error > 0:
        return "resistant"
    if error < 0:
        return "sensitive"
    return "neutral"


def allocate_bucket_counts(
    total: int,
    *,
    train_fraction: float,
    val_fraction: float,
    test_fraction: float,
) -> dict[str, int]:
    train_raw = total * train_fraction
    val_raw = total * val_fraction
    test_raw = total * test_fraction
    train_count = int(math.floor(train_raw))
    val_count = int(math.floor(val_raw))
    test_count = int(math.floor(test_raw))
    remainder = total - train_count - val_count - test_count

    residuals = [
        ("train", train_raw - train_count),
        ("val", val_raw - val_count),
        ("test", test_raw - test_count),
    ]
    residuals.sort(key=lambda item: item[1], reverse=True)
    for idx in range(remainder):
        if idx < len(residuals):
            if residuals[idx][0] == "train":
                train_count += 1
            elif residuals[idx][0] == "val":
                val_count += 1
            else:
                test_count += 1
    return {"train": train_count, "val": val_count, "test": test_count}


def split_reports(
    reports: list[dict[str, Any]],
    *,
    train_fraction: float,
    val_fraction: float,
    test_fraction: float,
    seed: int,
) -> dict[str, list[dict[str, Any]]]:
    by_bucket: dict[str, list[dict[str, Any]]] = {}
    for report in reports:
        by_bucket.setdefault(stratify_key(report), []).append(report)

    rng = random.Random(seed)
    splits: dict[str, list[dict[str, Any]]] = {"train": [], "val": [], "test": []}
    for bucket_reports in by_bucket.values():
        ordered = sorted(bucket_reports, key=lambda row: str(row.get("report_id", "")))
        rng.shuffle(ordered)
        counts = allocate_bucket_counts(
            len(ordered),
            train_fraction=train_fraction,
            val_fraction=val_fraction,
            test_fraction=test_fraction,
        )
        train_end = counts["train"]
        val_end = train_end + counts["val"]
        splits["train"].extend(ordered[:train_end])
        splits["val"].extend(ordered[train_end:val_end])
        splits["test"].extend(ordered[val_end:])

    for split_name in splits:
        splits[split_name] = sorted(splits[split_name], key=lambda row: str(row["report_id"]))
    return splits


def build_rpt_markdown_input(
    report: dict[str, Any],
    *,
    context: Any,
    prompt_model_key: str,
    prompt_style: str,
    short_features: int,
    short_same_drug: int,
    short_same_cell: int,
) -> tuple[str, str]:
    prompt_profile = MODEL_REGISTRY[prompt_model_key]["prompt_profile"]
    system_prompt = build_system_prompt(prompt_model_key)

    rendered_payload = copy.deepcopy(report)
    if prompt_style == "short_rpt":
        rendered_payload["enriched_features"] = rendered_payload.get("enriched_features", [])[
            :short_features
        ]
        rendered_payload["same_drug_examples"] = rendered_payload.get("same_drug_examples", [])[
            :short_same_drug
        ]
        rendered_payload["same_cell_examples"] = rendered_payload.get("same_cell_examples", [])[
            :short_same_cell
        ]

    rpt_markdown = render_markdown_report(rendered_payload).strip()
    evidence_block = "\n".join(
        [
            "Structured SHAP-grounded report:",
            rpt_markdown,
            "",
            build_aux_context(report, context, prompt_profile),
            "",
            "Generate a grounded explanation using the required section headings.",
        ]
    )
    return system_prompt, evidence_block


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as fout:
        for row in rows:
            fout.write(json.dumps(row, ensure_ascii=True) + "\n")


def build_summary_markdown(
    *,
    reports_path: Path,
    out_dir: Path,
    teacher_model: str,
    prompt_style: str,
    split_counts: dict[str, int],
    short_features: int,
    short_same_drug: int,
    short_same_cell: int,
) -> str:
    lines = [
        "# SFT Experiment Prep",
        "",
        f"- Source reports: `{reports_path}`",
        f"- Teacher model: `{teacher_model}`",
        f"- Prompt style: `{prompt_style}`",
        f"- Train reports: {split_counts['train']}",
        f"- Validation reports: {split_counts['val']}",
        f"- Test reports: {split_counts['test']}",
    ]
    if prompt_style == "short_rpt":
        lines.extend(
            [
                f"- Short prompt feature count: {short_features}",
                f"- Short prompt same-drug examples: {short_same_drug}",
                f"- Short prompt same-cell examples: {short_same_cell}",
            ]
        )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            f"- `{out_dir / 'reports' / 'train.jsonl'}`",
            f"- `{out_dir / 'reports' / 'val.jsonl'}`",
            f"- `{out_dir / 'reports' / 'test.jsonl'}`",
            f"- `{out_dir / 'teacher_requests' / 'train.jsonl'}`",
            f"- `{out_dir / 'teacher_requests' / 'val.jsonl'}`",
            f"- `{out_dir / 'teacher_requests' / 'test.jsonl'}`",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()

    fraction_sum = args.train_fraction + args.val_fraction + args.test_fraction
    if abs(fraction_sum - 1.0) > 1e-6:
        raise ValueError("train/val/test fractions must sum to 1.0")

    reports_path = Path(args.reports_jsonl).resolve()
    results_root = Path(args.results_root).resolve()
    out_dir = Path(args.out_dir).resolve()
    reports_dir = out_dir / "reports"
    teacher_dir = out_dir / "teacher_requests"

    ensure_empty_dir(out_dir, overwrite=args.overwrite)
    reports_dir.mkdir(parents=True, exist_ok=True)
    teacher_dir.mkdir(parents=True, exist_ok=True)

    reports = read_jsonl(reports_path)
    context = load_global_context(results_root)
    splits = split_reports(
        reports,
        train_fraction=args.train_fraction,
        val_fraction=args.val_fraction,
        test_fraction=args.test_fraction,
        seed=args.seed,
    )

    manifest = {
        "source_reports_jsonl": str(reports_path),
        "results_root": str(results_root),
        "teacher_model": args.teacher_model,
        "prompt_model_key": args.prompt_model_key,
        "prompt_style": args.prompt_style,
        "seed": args.seed,
        "fractions": {
            "train": args.train_fraction,
            "val": args.val_fraction,
            "test": args.test_fraction,
        },
        "counts": {split_name: len(rows) for split_name, rows in splits.items()},
    }

    for split_name, rows in splits.items():
        write_jsonl(reports_dir / f"{split_name}.jsonl", rows)

        teacher_requests: list[dict[str, Any]] = []
        for report in rows:
            system_prompt, structured_input = build_rpt_markdown_input(
                report,
                context=context,
                prompt_model_key=args.prompt_model_key,
                prompt_style=args.prompt_style,
                short_features=args.short_features,
                short_same_drug=args.short_same_drug,
                short_same_cell=args.short_same_cell,
            )
            teacher_requests.append(
                {
                    "report_id": report["report_id"],
                    "report_title": report_title(report),
                    "split": split_name,
                    "teacher_model": args.teacher_model,
                    "prompt_model_key": args.prompt_model_key,
                    "prompt_style": args.prompt_style,
                    "system_prompt": system_prompt,
                    "input": structured_input,
                    "source_reports_jsonl": str(reports_path),
                }
            )
        write_jsonl(teacher_dir / f"{split_name}.jsonl", teacher_requests)

    (out_dir / "split_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    (out_dir / "README.md").write_text(
        build_summary_markdown(
            reports_path=reports_path,
            out_dir=out_dir,
            teacher_model=args.teacher_model,
            prompt_style=args.prompt_style,
            split_counts=manifest["counts"],
            short_features=args.short_features,
            short_same_drug=args.short_same_drug,
            short_same_cell=args.short_same_cell,
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
