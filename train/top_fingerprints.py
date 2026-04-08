#!/usr/bin/env python3
"""
Fit one RF with given (or best from tuning CSV) max_depth and n_estimators,
then compute and plot top drug fingerprint importances.
Also exports per-sample SHAP values for downstream LLM explanations.
No grid search — fast.

Usage:
  python train/top_fingerprints.py --data-dir data/processed --out-dir results/tuning --max-depth 10 --n-estimators 100
  python train/top_fingerprints.py --tuning-results results/tuning/tuning_results_n_estimators.csv  # use best from that CSV
  python train/top_fingerprints.py --tuning-results results/tuning/tuning_results.csv  # from full 2D tuning
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import shap
from sklearn.ensemble import RandomForestRegressor

import sys
if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
from load_data import load_merged


def _read_tuning_best(path: Path) -> tuple[int, int, float, str]:
    df_tune = pd.read_csv(path)
    if "mean_r2" in df_tune.columns:
        score_col = "mean_r2"
    elif "r2" in df_tune.columns:
        score_col = "r2"
    else:
        raise ValueError(f"{path} must contain either 'mean_r2' or 'r2'.")
    for req in ("max_depth", "n_estimators"):
        if req not in df_tune.columns:
            raise ValueError(f"{path} is missing required column '{req}'.")
    best_row = df_tune.loc[df_tune[score_col].idxmax()]
    return int(best_row["max_depth"]), int(best_row["n_estimators"]), float(best_row[score_col]), score_col


def _build_sample_labels(sample_meta: pd.DataFrame, compound_meta_file: str) -> tuple[pd.Series, pd.Series]:
    cell_label = None
    for col in ("cell_line", "cell_line_name", "ModelID"):
        if col in sample_meta.columns:
            cell_label = sample_meta[col].astype(str)
            break
    if cell_label is None:
        if "master_ccl_id" in sample_meta.columns:
            cell_label = sample_meta["master_ccl_id"].astype(str)
        else:
            cell_label = pd.Series(np.arange(len(sample_meta)).astype(str), index=sample_meta.index)

    drug_label = None
    for col in ("drug", "drug_name", "cpd_name"):
        if col in sample_meta.columns:
            drug_label = sample_meta[col].astype(str)
            break

    if drug_label is None:
        drug_label = None
        if "master_cpd_id" in sample_meta.columns and compound_meta_file:
            cmeta_path = Path(compound_meta_file)
            if cmeta_path.exists():
                cmeta = pd.read_csv(
                    cmeta_path,
                    sep="\t",
                    usecols=["master_cpd_id", "cpd_name"],
                    dtype={"master_cpd_id": "int64", "cpd_name": "string"},
                ).drop_duplicates(subset=["master_cpd_id"])
                cmeta_map = dict(zip(cmeta["master_cpd_id"], cmeta["cpd_name"].astype(str)))
                drug_label = sample_meta["master_cpd_id"].map(cmeta_map).fillna(sample_meta["master_cpd_id"].astype(str))
    if drug_label is None:
        if "master_cpd_id" in sample_meta.columns:
            drug_label = sample_meta["master_cpd_id"].astype(str)
        else:
            drug_label = pd.Series(np.arange(len(sample_meta)).astype(str), index=sample_meta.index)
    return cell_label, drug_label


def _build_shap_long_df(
    shap_values: np.ndarray,
    X: np.ndarray,
    y: np.ndarray,
    y_pred: np.ndarray,
    feat_cols: list[str],
    sample_meta: pd.DataFrame,
    top_k: int,
    compound_meta_file: str,
) -> pd.DataFrame:
    n_samples, n_features = shap_values.shape
    if top_k <= 0:
        raise ValueError("--top-k-shap must be > 0")
    k = min(top_k, n_features)

    abs_vals = np.abs(shap_values)
    topk_unsorted = np.argpartition(abs_vals, kth=n_features - k, axis=1)[:, -k:]
    row_ix = np.arange(n_samples)[:, None]
    topk_abs = abs_vals[row_ix, topk_unsorted]
    order = np.argsort(-topk_abs, axis=1)
    topk_idx = topk_unsorted[row_ix, order]

    sample_meta = sample_meta.reset_index(drop=True)
    cell_label, drug_label = _build_sample_labels(sample_meta, compound_meta_file)

    rows: list[dict] = []
    for i in range(n_samples):
        meta = sample_meta.iloc[i].to_dict()
        for rank, j in enumerate(topk_idx[i], start=1):
            rec = {
                "sample_idx": i,
                "cell_line": cell_label.iloc[i],
                "drug": drug_label.iloc[i],
                "y_true": float(y[i]),
                "y_pred": float(y_pred[i]),
                "feature_rank": rank,
                "feature": feat_cols[j],
                "feature_value": float(X[i, j]),
                "shap_value": float(shap_values[i, j]),
                "abs_shap_value": float(abs_vals[i, j]),
            }
            rec.update(meta)
            rows.append(rec)
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Get top drug fingerprint features from one RF fit.")
    parser.add_argument("--data-dir", default="data/processed")
    parser.add_argument("--pairs", default="pairs.csv")
    parser.add_argument("--cell-features", default="cell_features_selected.csv")
    parser.add_argument("--drug-fingerprints", default="drug_fingerprints.csv")
    parser.add_argument("--out-dir", default="results/tuning")
    parser.add_argument("--max-depth", type=int, default=10, help="RF max_depth (required unless --tuning-results).")
    parser.add_argument("--n-estimators", type=int, default=100, help="RF n_estimators (required unless --tuning-results).")
    parser.add_argument(
        "--tuning-results",
        type=str,
        default=None,
        help="CSV from tune_n_estimators.py or tune_max_depth.py or full tuning; use best row for max_depth and n_estimators.",
    )
    parser.add_argument("--compound-meta", default="data/CTRPv2/v21.meta.per_compound.txt")
    parser.add_argument(
        "--top-k-shap",
        type=int,
        default=20,
        help="Store top-K |SHAP| features per sample in shap_values.parquet.",
    )
    parser.add_argument("--top-n-fingerprints", type=int, default=30)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--n-jobs", type=int, default=1)
    args = parser.parse_args()

    if args.tuning_results is not None:
        path = Path(args.tuning_results)
        if not path.exists():
            raise FileNotFoundError(f"Not found: {path}")
        max_depth, n_estimators, score, score_col = _read_tuning_best(path)
        print(
            f"From {path.name}: best max_depth={max_depth}, "
            f"n_estimators={n_estimators}, {score_col}={score:.4f}"
        )
    else:
        if args.max_depth is None or args.n_estimators is None:
            raise ValueError("Provide both --max-depth and --n-estimators, or --tuning-results CSV.")
        max_depth = args.max_depth
        n_estimators = args.n_estimators

    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Loading data...")
    X, y, feat_cols, cell_feat_cols, drug_feat_cols, sample_meta = load_merged(
        args.data_dir, args.pairs, args.cell_features, args.drug_fingerprints, return_metadata=True
    )
    print(f"X: {X.shape}, y: {y.shape}")

    print("Fitting RF on full data for feature importances and SHAP...")
    model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=args.seed,
        n_jobs=args.n_jobs,
    )
    model.fit(X, y)
    y_pred = model.predict(X)

    imp = pd.Series(model.feature_importances_, index=feat_cols)
    drug_imp = imp[drug_feat_cols].sort_values(ascending=False)
    out_csv = out_dir / "fingerprint_importances.csv"
    drug_imp.to_csv(out_csv)
    print(f"Saved: {out_csv}")

    top_fp = drug_imp.head(args.top_n_fingerprints)

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7, 8))
    y_pos = range(len(top_fp))[::-1]
    ax.barh(y_pos, top_fp.values, color="teal", alpha=0.85)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(top_fp.index.tolist(), fontsize=8)
    ax.set_xlabel("Feature importance")
    ax.set_title(f"Top {args.top_n_fingerprints} Drug Fingerprint Features (max_depth={max_depth}, n_est={n_estimators})")
    fig.tight_layout()
    out_png = out_dir / "top_fingerprint_features.png"
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_png}")

    print("Computing SHAP values...")
    explainer = shap.TreeExplainer(model)
    shap_raw = explainer.shap_values(X)
    shap_values = shap_raw[0] if isinstance(shap_raw, list) else shap_raw
    if shap_values.ndim != 2:
        raise ValueError(f"Expected 2D SHAP array for regression, got shape={shap_values.shape}")

    shap_long = _build_shap_long_df(
        shap_values=shap_values,
        X=X,
        y=y,
        y_pred=y_pred,
        feat_cols=feat_cols,
        sample_meta=sample_meta,
        top_k=args.top_k_shap,
        compound_meta_file=args.compound_meta,
    )
    out_shap = out_dir / "shap_values.parquet"
    shap_long.to_parquet(out_shap, index=False)
    print(f"Saved: {out_shap}")
    print("Done.")


if __name__ == "__main__":
    main()
