#!/usr/bin/env python3
"""Resolve a drug/cell manifest into build_shap_reports.py selection CSV schema."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import pandas as pd


REQUIRED_MANIFEST_COLUMNS = {
    "report_id",
    "group",
    "cpd_name",
    "ModelID",
    "cell_line_name",
    "lineage",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Join a compact report manifest on data/processed/pairs_ic50.csv and "
            "emit a selection CSV consumable by build_shap_reports.py."
        )
    )
    parser.add_argument("--manifest", default="25_pairs.csv")
    parser.add_argument("--pairs", default="data/processed/pairs_ic50.csv")
    parser.add_argument("--out-csv", default="llm_explainer/selected_25_pairs_ic50.csv")
    parser.add_argument(
        "--missing-csv",
        default="llm_explainer/selected_25_pairs_ic50_missing.csv",
        help="Rows from the manifest that could not be resolved in --pairs.",
    )
    parser.add_argument("--target-label", default="log10(IC50)")
    return parser.parse_args()


def fmt_report_id(value: Any) -> str:
    try:
        return f"RPT-{int(value):04d}"
    except (TypeError, ValueError):
        text = str(value).strip()
        return text if text.startswith("RPT-") else f"RPT-{text}"


def main() -> None:
    args = parse_args()
    manifest_path = Path(args.manifest).resolve()
    pairs_path = Path(args.pairs).resolve()
    out_csv = Path(args.out_csv).resolve()
    missing_csv = Path(args.missing_csv).resolve()

    manifest = pd.read_csv(manifest_path)
    missing_cols = REQUIRED_MANIFEST_COLUMNS - set(manifest.columns)
    if missing_cols:
        raise ValueError(f"{manifest_path} is missing columns: {sorted(missing_cols)}")

    if pairs_path.suffix == ".parquet":
        pairs = pd.read_parquet(pairs_path)
    else:
        pairs = pd.read_csv(pairs_path)

    pair_cols = [
        "master_ccl_id",
        "master_cpd_id",
        "ModelID",
        "cpd_name",
        "y",
        "n_experiments",
        "log10_ic50_std",
    ]
    pair_lookup = pairs[pair_cols].drop_duplicates(subset=["ModelID", "cpd_name"])
    merged = manifest.merge(pair_lookup, on=["ModelID", "cpd_name"], how="left", indicator=True)

    resolved = merged[merged["_merge"] == "both"].copy()
    unresolved = merged[merged["_merge"] != "both"].copy()

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    missing_csv.parent.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, Any]] = []
    for _, row in resolved.iterrows():
        source_id = int(row["report_id"])
        y = float(row["y"])
        rows.append(
            {
                "rank": source_id,
                "report_id": fmt_report_id(source_id),
                "evidence_id": f"SHAP-{source_id:04d}",
                "selection_tag": str(row["group"]),
                "selection_reason": (
                    f"Manifest {manifest_path.name} row {source_id} ({row['group']}): "
                    f"{row['cpd_name']} on {row['cell_line_name']} / {row['ModelID']} "
                    f"({row['lineage']}); observed {args.target_label}={y:+.4f}."
                ),
                "master_ccl_id": int(row["master_ccl_id"]),
                "master_cpd_id": int(row["master_cpd_id"]),
                "ModelID": str(row["ModelID"]),
                "cpd_name": str(row["cpd_name"]),
                "cell_line_name": str(row["cell_line_name"]),
                "lineage": str(row["lineage"]),
                "observed_y": y,
                "n_experiments": int(row["n_experiments"]),
                "log10_ic50_std": float(row["log10_ic50_std"]),
            }
        )

    selection = pd.DataFrame(rows).sort_values("rank", kind="stable")
    selection.to_csv(out_csv, index=False)

    if not unresolved.empty:
        missing_out = unresolved.drop(columns=["_merge"]).copy()
        missing_out["missing_reason"] = "No matching ModelID + cpd_name row in response pairs file"
        missing_out.to_csv(missing_csv, index=False)
    elif missing_csv.exists():
        missing_csv.unlink()

    print(f"Resolved {len(selection)} / {len(manifest)} manifest rows.")
    print(f"Wrote selection CSV: {out_csv}")
    if not unresolved.empty:
        preview = unresolved[["report_id", "cpd_name", "ModelID", "cell_line_name"]].to_dict("records")
        print(f"Wrote missing CSV: {missing_csv}")
        print(f"Unresolved rows: {preview}")


if __name__ == "__main__":
    main()
