#!/usr/bin/env python3
"""
Build an IC50-target version of `pairs` using CTRPv2.0 curve-fit parameters.

CTRPv2.0 4-parameter dose-response model:

    viability(log2_conc) = p4_baseline
                         + p3_total_decline / (1 + exp(p2_slope * (log2_conc - p1_center)))

where `p3_total_decline = 1 - p4_baseline` (per the CTRPv2.0 column docs, p3 is not
a free parameter). Inverting at v = 0.5 gives:

    log2(IC50) = p1_center + log( p3_total_decline / (0.5 - p4_baseline) - 1 ) / p2_slope

which the user specified as the canonical computation. To match the user's exact
formula we use `log10(...)` in the inner log term and then convert to log10 via
multiplication by `log10(2)`:

    sub["log10_ic50"] = (
        sub["p1_center"]
        + np.log10(_inner.clip(lower=1e-30)) / sub["p2_slope"]
    ) * np.log10(2)

Valid samples must (a) have a mathematically defined inverse (`_valid_math`) and
(b) actually cross 50% viability over the dose-response curve (`_crosses_50`).

The per-experiment log10(IC50) values are averaged per (ModelID, cpd_name) and
projected back onto (master_ccl_id, master_cpd_id) so the output is a drop-in
replacement for `data/processed/pairs.parquet`, but with `y = log10_ic50`.

Outputs:
  - `<out_dir>/pairs_ic50.parquet`
  - `<out_dir>/pairs_ic50.csv`
  - `<out_dir>/pairs_ic50_schema.md`
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd


def _norm_name(value: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", (value or "").strip().upper())


def _build_cell_to_model_map(cell_meta_path: Path, model_path: Path) -> pd.DataFrame:
    """Map CTRP master_ccl_id -> DepMap ModelID via stripped/full cell-line name."""
    cell_meta = pd.read_csv(
        cell_meta_path,
        sep="\t",
        usecols=["master_ccl_id", "ccl_name"],
        dtype={"master_ccl_id": "int64", "ccl_name": "string"},
    )
    model = pd.read_csv(
        model_path,
        usecols=["ModelID", "CellLineName", "StrippedCellLineName"],
        dtype="string",
    )

    stripped_map: dict[str, list[str]] = {}
    cellline_map: dict[str, list[str]] = {}
    for _, row in model.iterrows():
        mid = row["ModelID"]
        s = _norm_name(row["StrippedCellLineName"] or "")
        c = _norm_name(row["CellLineName"] or "")
        if s:
            stripped_map.setdefault(s, []).append(mid)
        if c:
            cellline_map.setdefault(c, []).append(mid)

    def pick_model(ccl_name: str) -> str | None:
        key = _norm_name(ccl_name)
        s_hits = sorted(set(stripped_map.get(key, [])))
        if len(s_hits) == 1:
            return s_hits[0]
        c_hits = sorted(set(cellline_map.get(key, [])))
        if len(c_hits) == 1:
            return c_hits[0]
        return None

    mapped = cell_meta.copy()
    mapped["ModelID"] = mapped["ccl_name"].map(pick_model)
    mapped = mapped.dropna(subset=["ModelID"]).reset_index(drop=True)
    return mapped


def _load_per_experiment(path: Path) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        sep="\t",
        usecols=["experiment_id", "master_ccl_id"],
        dtype={"experiment_id": "int64", "master_ccl_id": "int64"},
    )
    return df.drop_duplicates(subset=["experiment_id"])


def _load_per_compound(path: Path) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        sep="\t",
        usecols=["master_cpd_id", "cpd_name"],
        dtype={"master_cpd_id": "int64", "cpd_name": "string"},
    )
    return df.dropna(subset=["cpd_name"]).drop_duplicates(subset=["master_cpd_id"])


def _load_curves(path: Path) -> pd.DataFrame:
    keep = [
        "experiment_id",
        "master_cpd_id",
        "p1_center",
        "p2_slope",
        "p3_total_decline",
        "p4_baseline",
        "apparent_ec50_umol",
    ]
    df = pd.read_csv(path, sep="\t", usecols=keep)
    df["experiment_id"] = pd.to_numeric(df["experiment_id"], errors="coerce").astype("Int64")
    df["master_cpd_id"] = pd.to_numeric(df["master_cpd_id"], errors="coerce").astype("Int64")
    for c in ("p1_center", "p2_slope", "p3_total_decline", "p4_baseline", "apparent_ec50_umol"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(
        subset=["experiment_id", "master_cpd_id", "p1_center", "p2_slope", "p3_total_decline", "p4_baseline"]
    )
    df["experiment_id"] = df["experiment_id"].astype("int64")
    df["master_cpd_id"] = df["master_cpd_id"].astype("int64")
    return df.reset_index(drop=True)


def compute_log10_ic50(
    sub: pd.DataFrame,
    *,
    min_abs_slope: float = 1e-2,
    max_abs_log10_ic50: float | None = 4.0,
) -> pd.DataFrame:
    """
    Apply the canonical IC50 formula. Expects a DataFrame with columns
    `p1_center`, `p2_slope`, `p3_total_decline`, `p4_baseline`. Adds:
        - `_crosses_50`
        - `_valid_math`
        - `log10_ic50`
    and returns the filtered rows (only those where both flags are True and, if
    `max_abs_log10_ic50` is set, |log10_ic50| is within range).

    `min_abs_slope` removes near-flat curves (|p2_slope| < threshold), which
    produce numerically explosive IC50 estimates even when the formula is
    technically defined. CTRPv2.0 also reports many curves with |p2_slope| ~ 1e-3
    that imply IC50 values outside the physically tested concentration range.
    """
    sub = sub.copy()

    p3 = sub["p3_total_decline"]
    p4 = sub["p4_baseline"]
    p2 = sub["p2_slope"]

    # Curve crosses 50% viability somewhere in tested range.
    # Low-dose viability limit = p4 + p3 (~ 1.0 in CTRPv2.0, since p3 = 1 - p4);
    # high-dose viability limit = p4. Require p4 < 0.5 < p4 + p3.
    sub["_crosses_50"] = (p4 < 0.5) & ((p4 + p3) > 0.5)

    # Mathematically invertible at v = 0.5: p3 / (0.5 - p4) - 1 > 0, all params finite,
    # and |p2_slope| is not too close to zero (flat curves produce absurd IC50 values).
    denom = 0.5 - p4
    inner_raw = np.where(denom != 0, p3 / denom - 1.0, np.nan)
    finite_all = (
        np.isfinite(sub["p1_center"])
        & np.isfinite(p2)
        & np.isfinite(p3)
        & np.isfinite(p4)
    )
    sub["_valid_math"] = finite_all & (p2.abs() >= min_abs_slope) & (inner_raw > 0)

    sub = sub[sub["_crosses_50"] & sub["_valid_math"]].copy()

    _inner = sub["p3_total_decline"] / (0.5 - sub["p4_baseline"]) - 1.0
    sub["log10_ic50"] = (
        sub["p1_center"]
        + np.log10(_inner.clip(lower=1e-30)) / sub["p2_slope"]
    ) * np.log10(2)

    if max_abs_log10_ic50 is not None:
        before = len(sub)
        sub = sub[sub["log10_ic50"].abs() <= float(max_abs_log10_ic50)].copy()
        dropped = before - len(sub)
        if dropped:
            print(
                f"  dropped {dropped:,} rows with |log10_ic50| > {max_abs_log10_ic50} "
                f"(remaining: {len(sub):,})"
            )
    return sub


def main() -> None:
    parser = argparse.ArgumentParser(description="Build pairs_ic50 parquet from CTRPv2.0 curves.")
    parser.add_argument("--base-dir", default=".", help="Project root containing data/.")
    parser.add_argument(
        "--curves",
        default="data/CTRPv2.0/v20.data.curves_post_qc.txt",
        help="CTRPv2.0 curves_post_qc file (has p1..p4 per experiment x compound).",
    )
    parser.add_argument(
        "--per-experiment",
        default="data/CTRPv2.0/v20.meta.per_experiment.txt",
        help="CTRPv2.0 per-experiment meta (experiment_id -> master_ccl_id).",
    )
    parser.add_argument(
        "--per-compound",
        default="data/CTRPv2/v21.meta.per_compound.txt",
        help="CTRP compound meta (master_cpd_id -> cpd_name). "
             "v21 is preferred because it matches the rest of the pipeline.",
    )
    parser.add_argument(
        "--cell-meta",
        default="data/CTRPv2/v21.meta.per_cell_line.txt",
        help="CTRP cell-line meta (master_ccl_id -> ccl_name).",
    )
    parser.add_argument(
        "--model-meta",
        default="data/DepMap/Model.csv",
        help="DepMap Model.csv (CellLineName / StrippedCellLineName -> ModelID).",
    )
    parser.add_argument(
        "--out-dir",
        default="data/processed",
        help="Output directory. `pairs_ic50.{parquet,csv}` and schema written here.",
    )
    parser.add_argument(
        "--out-prefix",
        default="pairs_ic50",
        help="Output file stem (e.g. `pairs_ic50` -> pairs_ic50.parquet).",
    )
    parser.add_argument(
        "--keep-per-experiment",
        action="store_true",
        help="Also write `<out_prefix>_per_experiment.parquet` with the per-experiment log10_ic50 rows (for neighbor analysis or debugging).",
    )
    parser.add_argument(
        "--min-abs-slope",
        type=float,
        default=1e-2,
        help="Minimum |p2_slope| for a curve to be considered well-defined "
             "(drops near-flat curves that produce explosive IC50 estimates).",
    )
    parser.add_argument(
        "--max-abs-log10-ic50",
        type=float,
        default=4.0,
        help="Clip |log10_ic50| to this bound (in log10 µM). "
             "Set to a negative value to disable clipping.",
    )
    args = parser.parse_args()
    max_abs = None if args.max_abs_log10_ic50 < 0 else args.max_abs_log10_ic50

    base = Path(args.base_dir).resolve()
    curves_path = (base / args.curves).resolve()
    per_exp_path = (base / args.per_experiment).resolve()
    cpd_path = (base / args.per_compound).resolve()
    cell_path = (base / args.cell_meta).resolve()
    model_path = (base / args.model_meta).resolve()
    out_dir = (base / args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    for p in (curves_path, per_exp_path, cpd_path, cell_path, model_path):
        if not p.exists():
            raise FileNotFoundError(f"Not found: {p}")

    print(f"Loading curves from {curves_path.name} ...")
    curves = _load_curves(curves_path)
    print(f"  curves rows (finite p1..p4): {len(curves):,}")

    print(f"Loading per-experiment meta from {per_exp_path.name} ...")
    per_exp = _load_per_experiment(per_exp_path)
    print(f"  experiments with master_ccl_id: {len(per_exp):,}")

    print(f"Loading per-compound meta from {cpd_path.name} ...")
    per_cpd = _load_per_compound(cpd_path)
    print(f"  compounds with cpd_name: {len(per_cpd):,}")

    print(f"Loading CTRP cell-line meta from {cell_path.name} ...")
    print(f"Loading DepMap Model.csv from {model_path.name} ...")
    cell_to_model = _build_cell_to_model_map(cell_path, model_path)
    print(f"  master_ccl_id -> ModelID mapped: {len(cell_to_model):,}")

    print("Joining curves with experiment -> ccl_id, compound -> cpd_name, ccl_id -> ModelID ...")
    merged = (
        curves.merge(per_exp, on="experiment_id", how="inner")
        .merge(per_cpd, on="master_cpd_id", how="inner")
        .merge(cell_to_model[["master_ccl_id", "ModelID"]], on="master_ccl_id", how="inner")
    )
    print(f"  after join: {len(merged):,} rows")

    print("Computing log10(IC50) and filtering on _crosses_50 & _valid_math ...")
    filtered = compute_log10_ic50(
        merged,
        min_abs_slope=args.min_abs_slope,
        max_abs_log10_ic50=max_abs,
    )
    print(f"  rows with valid log10_ic50: {len(filtered):,}")

    print("Aggregating per (ModelID, cpd_name): mean(log10_ic50), N ...")
    grouped = (
        filtered.groupby(["ModelID", "cpd_name"], as_index=False)
        .agg(
            y=("log10_ic50", "mean"),
            log10_ic50_std=("log10_ic50", "std"),
            n_experiments=("experiment_id", "nunique"),
        )
    )
    grouped["log10_ic50_std"] = grouped["log10_ic50_std"].fillna(0.0)
    print(f"  unique (ModelID, cpd_name) pairs: {len(grouped):,}")

    # Project back onto (master_ccl_id, master_cpd_id) so downstream scripts
    # (train/load_data.py etc.) continue to work unchanged.
    ccl_lookup = (
        filtered[["ModelID", "master_ccl_id"]]
        .drop_duplicates()
        .groupby("ModelID")["master_ccl_id"].first()
    )
    cpd_lookup = (
        filtered[["cpd_name", "master_cpd_id"]]
        .drop_duplicates()
        .groupby("cpd_name")["master_cpd_id"].first()
    )
    grouped["master_ccl_id"] = grouped["ModelID"].map(ccl_lookup).astype("int64")
    grouped["master_cpd_id"] = grouped["cpd_name"].map(cpd_lookup).astype("int64")

    out = grouped[
        [
            "master_ccl_id",
            "master_cpd_id",
            "y",
            "n_experiments",
            "ModelID",
            "cpd_name",
            "log10_ic50_std",
        ]
    ].copy()

    out_parquet = out_dir / f"{args.out_prefix}.parquet"
    out_csv = out_dir / f"{args.out_prefix}.csv"
    out.to_parquet(out_parquet, index=False)
    out.to_csv(out_csv, index=False)
    print(f"Wrote: {out_parquet}")
    print(f"Wrote: {out_csv}")

    if args.keep_per_experiment:
        out_pe = out_dir / f"{args.out_prefix}_per_experiment.parquet"
        filtered[
            [
                "experiment_id",
                "master_ccl_id",
                "master_cpd_id",
                "ModelID",
                "cpd_name",
                "p1_center",
                "p2_slope",
                "p3_total_decline",
                "p4_baseline",
                "apparent_ec50_umol",
                "log10_ic50",
            ]
        ].to_parquet(out_pe, index=False)
        print(f"Wrote: {out_pe}")

    schema_path = out_dir / f"{args.out_prefix}_schema.md"
    schema = f"""# IC50 Pairs Schema

## Input files
- `{curves_path.relative_to(base) if curves_path.is_relative_to(base) else curves_path}` — CTRPv2.0 4-parameter curve fits
- `{per_exp_path.relative_to(base) if per_exp_path.is_relative_to(base) else per_exp_path}` — experiment_id -> master_ccl_id
- `{cpd_path.relative_to(base) if cpd_path.is_relative_to(base) else cpd_path}` — master_cpd_id -> cpd_name
- `{cell_path.relative_to(base) if cell_path.is_relative_to(base) else cell_path}` — master_ccl_id -> ccl_name
- `{model_path.relative_to(base) if model_path.is_relative_to(base) else model_path}` — ccl_name -> ModelID

## Target definition
`y = mean(log10_ic50)` per `(ModelID, cpd_name)`, computed per experiment as

    log10_ic50 = (p1_center + log10(p3/(0.5 - p4) - 1) / p2_slope) * log10(2)

and filtered to rows where the fitted curve crosses 50% viability
(`p4_baseline < 0.5 < p4_baseline + p3_total_decline`) and the math is defined
(`p3 / (0.5 - p4) - 1 > 0`, p2 finite and non-zero).

Units: log10 of IC50 in µM (same axis as `log10(apparent_ec50_umol)`).

## Columns
- `master_ccl_id` — CTRP cell-line id (kept for downstream joins)
- `master_cpd_id` — CTRP compound id (kept for downstream joins)
- `y` — mean log10(IC50) across replicate experiments
- `n_experiments` — number of unique `experiment_id` contributing to this pair
- `ModelID` — DepMap ModelID (used by `cell_features_*.csv`)
- `cpd_name` — CTRP compound name
- `log10_ic50_std` — std of log10(IC50) across contributing experiments (0 if single experiment)

## Output shapes
- `{args.out_prefix}.parquet`: {len(out):,} rows
"""
    schema_path.write_text(schema, encoding="utf-8")
    print(f"Wrote: {schema_path}")


if __name__ == "__main__":
    main()
