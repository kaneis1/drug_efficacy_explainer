#!/usr/bin/env python3
"""
Generate RF results plots: Top 20 drugs by predictability (R²) and Top 20 genes across predictable drugs.

Method: Agg. by drug — train one Random Forest per drug (cell/gene features only), 5-fold CV;
report cross-validated R² per drug and, for drugs with R² > 0, count how many drugs each gene
appears in (using top-K genes by importance as that drug's "signature").

Usage:
  python train/generate_top_feature.py --data-dir data/processed --out-dir results/rf_plots
  python train/generate_top_feature.py --min-samples 30 --top-k-signature 50
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt


def parse_gene_col(col: str) -> str:
    """Format gene column as 'GENE (ENTREZ)' for display, or return as-is."""
    s = (col or "").strip()
    if not s:
        return col
    m = re.match(r"^([A-Za-z0-9\-\.]+)\s*\((\d+)\)\s*$", s)
    if m:
        return f"{m.group(1)} ({m.group(2)})"
    return s


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Per-drug RF (gene features), then plot Top 20 drugs by R² and Top 20 genes in signatures."
    )
    parser.add_argument("--data-dir", default="data/processed", help="Directory with pairs and cell_features.")
    parser.add_argument("--pairs", default="pairs.csv", help="Pairs file.")
    parser.add_argument("--cell-features", default=".csv", help="Cell/gene features.")
    parser.add_argument("--compound-meta", default="data/CTRPv2/v21.meta.per_compound.txt",
                        help="Compound metadata with master_cpd_id, cpd_name (tab-sep).")
    parser.add_argument("--out-dir", default="results/rf_plots", help="Output directory for plots and tables.")
    parser.add_argument("--cv-folds", type=int, default=5)
    parser.add_argument("--min-samples", type=int, default=20,
                        help="Minimum (cell line) samples per drug to include.")
    parser.add_argument("--top-k-signature", type=int, default=50,
                        help="Top K genes by importance count as drug 'signature' (for gene count plot).")
    parser.add_argument("--top-n-drugs", type=int, default=20, help="Number of drugs in bar chart.")
    parser.add_argument("--top-n-genes", type=int, default=20, help="Number of genes in bar chart.")
    parser.add_argument("--n-estimators", type=int, default=100)
    parser.add_argument("--max-depth", type=int, default=8)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--n-jobs", type=int, default=10)
    args = parser.parse_args()

    base = Path(args.data_dir).resolve()
    pairs_path = base / args.pairs
    cell_path = base / args.cell_features
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    for p in [pairs_path, cell_path]:
        if not p.exists():
            raise FileNotFoundError(f"Not found: {p}")

    print("Loading pairs and cell features...")
    pairs = pd.read_parquet(pairs_path) if str(pairs_path).endswith(".parquet") else pd.read_csv(pairs_path)
    if str(cell_path).endswith(".parquet"):
        cell = pd.read_parquet(cell_path)
    else:
        cell = pd.read_csv(cell_path)

    cell_id_col = "master_ccl_id"
    drug_id_col = "master_cpd_id"
    gene_cols = [c for c in cell.columns if c not in (cell_id_col, "ModelID")]
    if not gene_cols:
        raise ValueError("No gene columns found in cell features.")

    # Drug names (optional)
    cpd_name_map: dict[int, str] = {}
    compound_meta_path = Path(args.compound_meta)
    if compound_meta_path.exists():
        cpd_meta = pd.read_csv(compound_meta_path, sep="\t", usecols=["master_cpd_id", "cpd_name"], dtype={"master_cpd_id": "int64", "cpd_name": "string"})
        cpd_name_map = dict(zip(cpd_meta["master_cpd_id"], cpd_meta["cpd_name"].astype(str)))

    merged = pairs.merge(
        cell[[cell_id_col] + gene_cols],
        on=cell_id_col,
        how="inner",
    )
    drugs = merged[drug_id_col].value_counts()
    drugs = drugs[drugs >= args.min_samples].index.tolist()
    print(f"Drugs with >= {args.min_samples} samples: {len(drugs)}")

    kf = KFold(n_splits=args.cv_folds, shuffle=True, random_state=args.seed)
    per_drug_r2: list[float] = []
    per_drug_id: list[int] = []
    per_drug_importance: list[dict[str, float]] = []  # gene_col -> mean importance

    for i, cpd_id in enumerate(drugs):
        if (i + 1) % 100 == 0 or i == 0:
            print(f"  Processing drug {i + 1}/{len(drugs)} (master_cpd_id={cpd_id})")
        sub = merged[merged[drug_id_col] == cpd_id].drop_duplicates(subset=[cell_id_col], keep="first")
        X = sub[gene_cols].values.astype(np.float32)
        y = sub["y"].values.astype(np.float32)
        if len(y) < args.min_samples:
            continue
        r2_folds: list[float] = []
        imp_folds: list[np.ndarray] = []
        for tr_idx, te_idx in kf.split(X):
            X_tr, X_te = X[tr_idx], X[te_idx]
            y_tr, y_te = y[tr_idx], y[te_idx]
            model = RandomForestRegressor(
                n_estimators=args.n_estimators,
                max_depth=args.max_depth,
                random_state=args.seed,
                n_jobs=args.n_jobs,
            )
            model.fit(X_tr, y_tr)
            y_pred = model.predict(X_te)
            r2_folds.append(r2_score(y_te, y_pred))
            imp_folds.append(model.feature_importances_)
        r2_mean = float(np.mean(r2_folds))
        imp_mean = np.mean(imp_folds, axis=0)
        per_drug_r2.append(r2_mean)
        per_drug_id.append(int(cpd_id))
        per_drug_importance.append(dict(zip(gene_cols, imp_mean)))

    df_r2 = pd.DataFrame({"master_cpd_id": per_drug_id, "r2": per_drug_r2})
    df_r2["cpd_name"] = df_r2["master_cpd_id"].map(lambda x: cpd_name_map.get(x, str(x)))
    df_r2 = df_r2.sort_values("r2", ascending=False).reset_index(drop=True)
    df_r2.to_csv(out_dir / "per_drug_r2.csv", index=False)
    print(f"Saved per-drug R²: {out_dir / 'per_drug_r2.csv'}")

    # Genes in signature: for each drug with R² > 0, top top_k_signature genes; count per gene
    predictable = df_r2[df_r2["r2"] > 0]
    gene_count: dict[str, int] = {}
    for _, row in predictable.iterrows():
        idx = per_drug_id.index(row["master_cpd_id"])
        imp = per_drug_importance[idx]
        top_genes = sorted(imp.keys(), key=lambda g: imp[g], reverse=True)[: args.top_k_signature]
        for g in top_genes:
            gene_count[g] = gene_count.get(g, 0) + 1

    gene_count_series = pd.Series(gene_count).sort_values(ascending=False)
    gene_count_series.to_csv(out_dir / "gene_signature_counts.csv", header=["n_drugs"])
    print(f"Saved gene signature counts: {out_dir / 'gene_signature_counts.csv'}")

    # --- Plot 1: Top N drugs by R² ---
    top_drugs = df_r2.head(args.top_n_drugs)
    labels = top_drugs["cpd_name"].str.strip().str.lower()
    fig, ax = plt.subplots(figsize=(7, 6))
    y_pos = np.arange(len(labels))[::-1]
    bars = ax.barh(y_pos, top_drugs["r2"].values, color="steelblue", alpha=0.85)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel("Cross-validated R²")
    ax.set_title("Top 20 Drugs by Predictability")
    ax.set_xlim(0, max(top_drugs["r2"].max() * 1.1, 0.05))
    fig.tight_layout()
    fig.savefig(out_dir / "top_drugs_by_r2.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_dir / 'top_drugs_by_r2.png'}")

    # --- Plot 2: Top N genes across predictable drugs ---
    top_genes = gene_count_series.head(args.top_n_genes)
    gene_labels = [parse_gene_col(g) for g in top_genes.index]
    fig, ax = plt.subplots(figsize=(7, 6))
    y_pos = np.arange(len(gene_labels))[::-1]
    ax.barh(y_pos, top_genes.values, color="coral", alpha=0.85)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(gene_labels, fontsize=9)
    ax.set_xlabel("Number of drugs where gene is in signature")
    ax.set_title("Top 20 Genes Across Predictable Drugs (R² > 0)")
    fig.tight_layout()
    fig.savefig(out_dir / "top_genes_across_drugs.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_dir / 'top_genes_across_drugs.png'}")

    print("Done.")


if __name__ == "__main__":
    main()
