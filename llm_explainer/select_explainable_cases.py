#!/usr/bin/env python3
"""
Curate an "explainable abnormal + explainable normal" bundle for LLM narration.

This is Option B from the IC50 report-curation discussion: combine the RF
model residual and the KNN-in-feature-space residual, gate by data-quality
and interpretability filters, then pick tails with a diversity cap so an LLM
can actually reason about the cases.

For every sample we compute:

    model_res[i] = y_obs[i] - y_pred_oof[i]   (from results_ic50/oof_predictions.csv)
    knn_res[i]   = y_obs[i] - mean(y over k-NN in feature space)
                   (from llm_explainer/knn_residuals_ic50.csv, produced by
                    select_knn_cases.py)
    score[i]     = z(|model_res|) + z(|knn_res|)

After applying quality filters (below), we take the 25 largest-score samples
as "abnormal_combined" and the 25 smallest-score samples as "normal_combined".

Quality filters (all must hold):
  * ``n_experiments >= 1 and log10_ic50_std < max_replicate_std`` (stable
    curve fits; single-replicate pairs pass because their std is 0 by
    definition).
  * the drug has a per-drug R² >= ``min_per_drug_r2`` in per_drug_r2.csv
    (the model actually has signal on this drug, so a residual is
    meaningful).
  * the compound has an annotated target / MoA in v21.meta.per_compound.txt
    (not just ``screening hit``) AND a real ``cpd_name``.
  * the cell line has a non-empty ``OncotreeLineage`` in DepMap Model.csv.

Diversity caps per bucket (abnormal / normal):
  * ``--max-per-drug``   (default 2)
  * ``--max-per-lineage`` (default 2)
  * ``--max-per-drug-lineage`` (default 1, stops duplicate drug-in-lineage)

Output CSV matches the schema consumed by
``build_shap_reports.py --selection-mode from_csv``.

Example (from repo root):

    python llm_explainer/select_explainable_cases.py \
        --pairs data/processed/pairs_ic50.parquet \
        --oof-predictions results_ic50/oof_predictions.csv \
        --knn-residuals llm_explainer/knn_residuals_ic50.csv \
        --per-drug-r2 results_ic50/rf_plots/per_drug_r2.csv \
        --compound-meta data/CTRPv2/v21.meta.per_compound.txt \
        --model-csv data/DepMap/Model.csv \
        --out-csv llm_explainer/explainable_curated_ic50.csv
"""
from __future__ import annotations

import argparse
import functools
from pathlib import Path

import numpy as np
import pandas as pd

print = functools.partial(print, flush=True)  # type: ignore[assignment]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Combine RF-residual + KNN-residual with quality gates "
        "to curate explainable abnormal + normal samples."
    )
    p.add_argument(
        "--pairs",
        default="data/processed/pairs_ic50.parquet",
        help="Merged pair table with master_ccl_id, master_cpd_id, y, "
             "n_experiments, log10_ic50_std, ModelID, cpd_name.",
    )
    p.add_argument(
        "--oof-predictions",
        default="results_ic50/oof_predictions.csv",
        help="Output of train/compute_oof_predictions.py.",
    )
    p.add_argument(
        "--knn-residuals",
        default="llm_explainer/knn_residuals_ic50.csv",
        help="Full residual table written by select_knn_cases.py --out-all-csv.",
    )
    p.add_argument(
        "--per-drug-r2",
        default="results_ic50/rf_plots/per_drug_r2.csv",
    )
    p.add_argument(
        "--compound-meta",
        default="data/CTRPv2/v21.meta.per_compound.txt",
    )
    p.add_argument(
        "--model-csv",
        default="data/DepMap/Model.csv",
    )
    p.add_argument(
        "--target-label",
        default="log10(IC50)",
        help="Human-readable target label for selection_reason strings.",
    )
    p.add_argument("--n-abnormal", type=int, default=25)
    p.add_argument("--n-normal", type=int, default=25)
    # Quality gates
    p.add_argument(
        "--max-replicate-std",
        type=float,
        default=0.5,
        help="Drop pairs whose within-group log10_ic50 std exceeds this "
             "(only relevant when n_experiments >= 2).",
    )
    p.add_argument(
        "--min-per-drug-r2",
        type=float,
        default=0.20,
        help="Drop drugs whose per-drug R² is below this threshold.",
    )
    p.add_argument(
        "--require-annotated-target",
        action="store_true",
        default=True,
        help="Require gene_symbol_of_protein_target to be non-null "
             "(default on). Pass --no-require-annotated-target to disable.",
    )
    p.add_argument("--no-require-annotated-target", action="store_false",
                   dest="require_annotated_target")
    p.add_argument(
        "--drop-screening-hits",
        action="store_true",
        default=True,
        help="Drop compounds whose target_or_activity_of_compound is "
             "``screening hit`` (default on). Pass --keep-screening-hits "
             "to disable.",
    )
    p.add_argument("--keep-screening-hits", action="store_false",
                   dest="drop_screening_hits")
    p.add_argument(
        "--require-lineage",
        action="store_true",
        default=True,
        help="Require OncotreeLineage non-null (default on).",
    )
    p.add_argument("--no-require-lineage", action="store_false",
                   dest="require_lineage")
    # Diversity caps
    p.add_argument("--max-per-drug", type=int, default=2)
    p.add_argument("--max-per-lineage", type=int, default=2)
    p.add_argument("--max-per-drug-lineage", type=int, default=1)
    # Outputs
    p.add_argument(
        "--out-csv",
        default="llm_explainer/explainable_curated_ic50.csv",
        help="Selected 25 + 25 cases in build_shap_reports.py CSV schema.",
    )
    p.add_argument(
        "--out-all-csv",
        default="llm_explainer/explainable_scored_ic50.csv",
        help="Full scored table (all eligible samples, ranked).",
    )
    return p.parse_args()


def _read_pairs(path: str) -> pd.DataFrame:
    path_l = path.lower()
    if path_l.endswith(".parquet"):
        return pd.read_parquet(path)
    return pd.read_csv(path)


def _z(x: pd.Series) -> pd.Series:
    x = x.astype(float)
    mu = float(x.mean())
    sd = float(x.std())
    if not np.isfinite(sd) or sd == 0:
        return x - mu
    return (x - mu) / sd


def _enforce_diversity(
    df: pd.DataFrame,
    *,
    limit: int,
    max_per_drug: int,
    max_per_lineage: int,
    max_per_drug_lineage: int,
) -> pd.DataFrame:
    if limit <= 0 or df.empty:
        return df.iloc[0:0].copy()

    drug_count: dict = {}
    lin_count: dict = {}
    dl_count: dict = {}
    kept_idx: list = []

    for idx, row in df.iterrows():
        if len(kept_idx) >= limit:
            break
        cpd = int(row["master_cpd_id"])
        ccl = int(row["master_ccl_id"])
        lin = row.get("OncotreeLineage", "") or ""
        if max_per_drug > 0 and drug_count.get(cpd, 0) >= max_per_drug:
            continue
        if max_per_lineage > 0 and lin_count.get(lin, 0) >= max_per_lineage:
            continue
        if max_per_drug_lineage > 0 and dl_count.get((cpd, lin), 0) >= max_per_drug_lineage:
            continue
        kept_idx.append(idx)
        drug_count[cpd] = drug_count.get(cpd, 0) + 1
        lin_count[lin] = lin_count.get(lin, 0) + 1
        dl_count[(cpd, lin)] = dl_count.get((cpd, lin), 0) + 1

    # Backfill if diversity caps starved the bucket.
    if len(kept_idx) < limit:
        remaining = df.drop(index=kept_idx)
        for idx, _ in remaining.iterrows():
            if len(kept_idx) >= limit:
                break
            kept_idx.append(idx)

    return df.loc[kept_idx].copy()


def main() -> None:
    args = parse_args()

    print(f"Loading pairs        : {args.pairs}")
    pairs = _read_pairs(args.pairs)
    required_pair_cols = {"master_ccl_id", "master_cpd_id", "y", "log10_ic50_std"}
    missing = required_pair_cols - set(pairs.columns)
    if missing:
        raise ValueError(f"Pairs file missing required columns: {missing}")
    pairs = pairs[list(pairs.columns)].copy()

    print(f"Loading OOF preds    : {args.oof_predictions}")
    oof = pd.read_csv(args.oof_predictions)
    if not {"master_ccl_id", "master_cpd_id", "y_pred"}.issubset(oof.columns):
        raise ValueError("OOF predictions CSV must have master_ccl_id, master_cpd_id, y_pred")
    oof = oof[["master_ccl_id", "master_cpd_id", "y_pred", "fold"]].copy()

    print(f"Loading KNN residuals: {args.knn_residuals}")
    knn = pd.read_csv(args.knn_residuals)
    knn = knn[
        ["master_ccl_id", "master_cpd_id", "neighbor_mean_y", "neighbor_std_y"]
    ].copy()

    print(f"Loading per-drug R²  : {args.per_drug_r2}")
    drug_r2 = pd.read_csv(args.per_drug_r2)
    if "master_cpd_id" not in drug_r2.columns or "r2" not in drug_r2.columns:
        raise ValueError("per_drug_r2.csv must have master_cpd_id + r2")
    drug_r2 = drug_r2[["master_cpd_id", "r2"]].rename(columns={"r2": "per_drug_r2"})

    print(f"Loading compound meta: {args.compound_meta}")
    cpd_meta = pd.read_csv(args.compound_meta, sep="\t")
    cpd_keep = [
        "master_cpd_id",
        "cpd_name",
        "gene_symbol_of_protein_target",
        "target_or_activity_of_compound",
    ]
    cpd_meta = cpd_meta[cpd_keep].copy()

    print(f"Loading Model.csv    : {args.model_csv}")
    mdl = pd.read_csv(args.model_csv)
    mdl_keep = ["ModelID", "OncotreeLineage", "OncotreePrimaryDisease", "OncotreeSubtype"]
    mdl_keep = [c for c in mdl_keep if c in mdl.columns]
    mdl = mdl[mdl_keep].copy()

    # ----- Merge everything on (master_ccl_id, master_cpd_id) -----
    df = pairs.merge(oof, on=["master_ccl_id", "master_cpd_id"], how="inner")
    df = df.merge(knn, on=["master_ccl_id", "master_cpd_id"], how="inner")
    df = df.merge(drug_r2, on="master_cpd_id", how="left")
    df = df.merge(cpd_meta, on=["master_cpd_id", "cpd_name"], how="left")
    if "ModelID" in df.columns:
        df = df.merge(mdl, on="ModelID", how="left")
    print(f"Merged rows: {len(df):,}")

    # ----- Residuals -----
    df["model_res"] = df["y"] - df["y_pred"]
    df["model_abs_res"] = df["model_res"].abs()
    df["knn_res"] = df["y"] - df["neighbor_mean_y"]
    df["knn_abs_res"] = df["knn_res"].abs()

    # ----- Quality filters -----
    eligible = df.copy()

    # Replicate stability.
    rep_mask = eligible["log10_ic50_std"].fillna(0.0) < args.max_replicate_std
    print(
        f"  replicate_std < {args.max_replicate_std}: keep "
        f"{int(rep_mask.sum()):,}/{len(eligible):,}"
    )
    eligible = eligible[rep_mask]

    # Per-drug R².
    r2_mask = eligible["per_drug_r2"].fillna(-np.inf) >= args.min_per_drug_r2
    print(
        f"  per_drug_r2 >= {args.min_per_drug_r2}: keep "
        f"{int(r2_mask.sum()):,}/{len(eligible):,}"
    )
    eligible = eligible[r2_mask]

    # Compound annotation.
    if args.require_annotated_target:
        tgt_mask = eligible["gene_symbol_of_protein_target"].notna()
        print(
            f"  has gene_symbol_of_protein_target: keep "
            f"{int(tgt_mask.sum()):,}/{len(eligible):,}"
        )
        eligible = eligible[tgt_mask]
    if args.drop_screening_hits:
        moa_series = eligible["target_or_activity_of_compound"].fillna("").str.lower()
        moa_mask = ~moa_series.str.contains("screening hit")
        print(
            f"  drop 'screening hit' MoA: keep "
            f"{int(moa_mask.sum()):,}/{len(eligible):,}"
        )
        eligible = eligible[moa_mask]

    # Lineage annotation.
    if args.require_lineage and "OncotreeLineage" in eligible.columns:
        lin_mask = eligible["OncotreeLineage"].notna()
        print(
            f"  OncotreeLineage non-null: keep "
            f"{int(lin_mask.sum()):,}/{len(eligible):,}"
        )
        eligible = eligible[lin_mask]

    if eligible.empty:
        raise RuntimeError("No samples survived the quality filters.")

    # ----- Combined score -----
    eligible = eligible.copy()
    eligible["z_model"] = _z(eligible["model_abs_res"])
    eligible["z_knn"] = _z(eligible["knn_abs_res"])
    eligible["combined_score"] = eligible["z_model"] + eligible["z_knn"]

    # Full ranked table for later inspection.
    full_sorted = eligible.sort_values("combined_score", ascending=False).reset_index(drop=True)
    full_sorted["rank_abnormal"] = np.arange(1, len(full_sorted) + 1)
    out_all = Path(args.out_all_csv)
    out_all.parent.mkdir(parents=True, exist_ok=True)
    full_sorted.to_csv(out_all, index=False)
    print(f"Wrote full scored table: {out_all}  ({len(full_sorted):,} rows)")

    # ----- Pick buckets with diversity caps -----
    abn_sorted = eligible.sort_values("combined_score", ascending=False)
    abnormal = _enforce_diversity(
        abn_sorted,
        limit=args.n_abnormal,
        max_per_drug=args.max_per_drug,
        max_per_lineage=args.max_per_lineage,
        max_per_drug_lineage=args.max_per_drug_lineage,
    )

    # Exclude abnormal from normal pool to avoid double-picking.
    remaining = eligible.drop(index=abnormal.index)
    nor_sorted = remaining.sort_values("combined_score", ascending=True)
    normal = _enforce_diversity(
        nor_sorted,
        limit=args.n_normal,
        max_per_drug=args.max_per_drug,
        max_per_lineage=args.max_per_lineage,
        max_per_drug_lineage=args.max_per_drug_lineage,
    )

    label = args.target_label

    def _reason_row(row: pd.Series, tag: str) -> str:
        target_txt = row.get("gene_symbol_of_protein_target") or row.get(
            "target_or_activity_of_compound"
        ) or "unannotated"
        lineage_txt = row.get("OncotreeLineage") or "n/a"
        disease_txt = row.get("OncotreePrimaryDisease") or "n/a"
        y_obs = row["y"]
        y_pred = row["y_pred"]
        nbr_mean = row["neighbor_mean_y"]
        m_res = row["model_res"]
        k_res = row["knn_res"]
        per_r2 = row.get("per_drug_r2")
        per_r2_txt = f"{per_r2:.2f}" if pd.notna(per_r2) else "n/a"

        if tag == "abnormal_combined":
            headline = (
                f"LLM-explainable abnormal: observed {label}={y_obs:+.3f}, "
                f"RF OOF predicted {y_pred:+.3f} (Δ_model={m_res:+.3f}), "
                f"20-NN mean={nbr_mean:+.3f} (Δ_knn={k_res:+.3f})."
            )
        else:
            headline = (
                f"LLM-explainable normal: observed {label}={y_obs:+.3f}, "
                f"RF OOF predicted {y_pred:+.3f} (Δ_model={m_res:+.3f}), "
                f"20-NN mean={nbr_mean:+.3f} (Δ_knn={k_res:+.3f})."
            )
        context = (
            f" Drug target: {target_txt}. "
            f"Cell lineage: {lineage_txt} / {disease_txt}. "
            f"Per-drug R² on held-out cells = {per_r2_txt}."
        )
        return headline + context

    abnormal = abnormal.assign(
        selection_tag="abnormal_combined",
        selection_reason=[
            _reason_row(r, "abnormal_combined") for _, r in abnormal.iterrows()
        ],
        rank=list(range(1, len(abnormal) + 1)),
    )
    normal = normal.assign(
        selection_tag="normal_combined",
        selection_reason=[
            _reason_row(r, "normal_combined") for _, r in normal.iterrows()
        ],
        rank=list(range(len(abnormal) + 1, len(abnormal) + 1 + len(normal))),
    )

    keep_cols = [
        "rank",
        "selection_tag",
        "selection_reason",
        "master_ccl_id",
        "master_cpd_id",
        "y",
        "y_pred",
        "model_res",
        "neighbor_mean_y",
        "knn_res",
        "z_model",
        "z_knn",
        "combined_score",
        "per_drug_r2",
        "log10_ic50_std",
        "ModelID",
        "cpd_name",
        "gene_symbol_of_protein_target",
        "target_or_activity_of_compound",
        "OncotreeLineage",
        "OncotreePrimaryDisease",
        "OncotreeSubtype",
    ]
    keep_cols = [c for c in keep_cols if c in abnormal.columns]

    curated = pd.concat([abnormal[keep_cols], normal[keep_cols]], ignore_index=True)
    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    curated.to_csv(out_csv, index=False)
    print(
        f"Wrote curated bundle ({len(abnormal)} abnormal + {len(normal)} normal): {out_csv}"
    )

    # ----- Summary -----
    def _summary(df: pd.DataFrame, lbl: str) -> None:
        if df.empty:
            print(f"  {lbl}: empty bucket")
            return
        print(
            f"  {lbl}: "
            f"|Δ_model| {df['model_abs_res'].min():.3f}–{df['model_abs_res'].max():.3f} | "
            f"|Δ_knn| {df['knn_abs_res'].min():.3f}–{df['knn_abs_res'].max():.3f} | "
            f"combined_score {df['combined_score'].min():.2f}–{df['combined_score'].max():.2f}"
        )
        by_lin = df["OncotreeLineage"].value_counts().head(6).to_dict()
        print(f"    top lineages: {by_lin}")
        by_drug = df["cpd_name"].value_counts().head(6).to_dict()
        print(f"    top drugs   : {by_drug}")

    _summary(abnormal, "abnormal_combined")
    _summary(normal, "normal_combined  ")


if __name__ == "__main__":
    main()
