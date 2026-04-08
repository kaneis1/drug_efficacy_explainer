#!/usr/bin/env python3
"""
Hyperparameter tuning for Random Forest (max_depth 1–20, n_estimators 1–250) and plots:
  - Tuning: heatmap + line plots of CV R² vs max_depth and n_estimators.
  - Top drug fingerprint features from the best model (global RF on cell + drug features).

Usage:
  python train/tune_rf_and_plot_fingerprints.py --data-dir data/processed --out-dir results/tuning
  python train/tune_rf_and_plot_fingerprints.py --max-depth-step 2 --n-estimators-step 50  # coarser grid
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt


def main() -> None:
    parser = argparse.ArgumentParser(
        description="RF hyperparameter tuning (max_depth, n_estimators) and top fingerprint features plot."
    )
    parser.add_argument("--data-dir", default="data/processed", help="Directory with pairs, cell_features, drug_fingerprints.")
    parser.add_argument("--pairs", default="pairs.csv", help="Pairs file.")
    parser.add_argument("--cell-features", default="cell_features_selected.csv", help="Cell features.")
    parser.add_argument("--drug-fingerprints", default="drug_fingerprints.csv", help="Drug fingerprints.")
    parser.add_argument("--out-dir", default="results/tuning", help="Output directory for tuning results and plots.")
    parser.add_argument("--cv-folds", type=int, default=5)
    parser.add_argument("--max-depth-min", type=int, default=1)
    parser.add_argument("--max-depth-max", type=int, default=20)
    parser.add_argument("--max-depth-step", type=int, default=1)
    parser.add_argument("--n-estimators-min", type=int, default=1)
    parser.add_argument("--n-estimators-max", type=int, default=250)
    parser.add_argument("--n-estimators-step", type=int, default=25,
                        help="Step for n_estimators grid (e.g. 25 -> 1,26,51,...,226).")
    parser.add_argument("--top-n-fingerprints", type=int, default=30, help="Top N fingerprint features to plot.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--n-jobs", type=int, default=1)
    args = parser.parse_args()

    base = Path(args.data_dir).resolve()
    pairs_path = base / args.pairs
    cell_path = base / args.cell_features
    drug_path = base / args.drug_fingerprints
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    for p in [pairs_path, cell_path, drug_path]:
        if not p.exists():
            raise FileNotFoundError(f"Not found: {p}")

    print("Loading data...")
    pairs = pd.read_parquet(pairs_path) if str(pairs_path).endswith(".parquet") else pd.read_csv(pairs_path)
    cell = pd.read_parquet(cell_path) if str(cell_path).endswith(".parquet") else pd.read_csv(cell_path)
    drug = pd.read_parquet(drug_path) if str(drug_path).endswith(".parquet") else pd.read_csv(drug_path)

    cell_id_col = "master_ccl_id"
    drug_id_col = "master_cpd_id"
    cell_feat_cols = [c for c in cell.columns if c not in (cell_id_col, "ModelID")]
    drug_feat_cols = [c for c in drug.columns if c != drug_id_col]
    feat_cols = cell_feat_cols + drug_feat_cols

    merged = (
        pairs.merge(cell[[cell_id_col] + cell_feat_cols], on=cell_id_col, how="inner")
        .merge(drug[[drug_id_col] + drug_feat_cols], on=drug_id_col, how="inner")
    )
    X = merged[feat_cols].values.astype(np.float32)
    y = merged["y"].values.astype(np.float32)
    print(f"Shapes - X: {X.shape}, y: {y.shape} (cell feats: {len(cell_feat_cols)}, drug feats: {len(drug_feat_cols)})")

    max_depths = list(range(args.max_depth_min, args.max_depth_max + 1, args.max_depth_step))
    n_est_list = list(range(args.n_estimators_min, args.n_estimators_max + 1, args.n_estimators_step))
    if args.n_estimators_max not in n_est_list:
        n_est_list.append(args.n_estimators_max)
    n_est_list = sorted(set(n_est_list))

    kf = KFold(n_splits=args.cv_folds, shuffle=True, random_state=args.seed)
    grid_results: list[dict] = []

    total = len(max_depths) * len(n_est_list)
    run = 0
    for max_depth in max_depths:
        for n_estimators in n_est_list:
            run += 1
            if run % 50 == 0 or run == 1:
                print(f"  Grid {run}/{total}: max_depth={max_depth}, n_estimators={n_estimators}")
            r2_folds = []
            for tr_idx, te_idx in kf.split(X):
                model = RandomForestRegressor(
                    n_estimators=n_estimators,
                    max_depth=max_depth,
                    random_state=args.seed,
                    n_jobs=args.n_jobs,
                )
                model.fit(X[tr_idx], y[tr_idx])
                y_pred = model.predict(X[te_idx])
                r2_folds.append(r2_score(y[te_idx], y_pred))
            grid_results.append({
                "max_depth": max_depth,
                "n_estimators": n_estimators,
                "mean_r2": float(np.mean(r2_folds)),
                "std_r2": float(np.std(r2_folds)),
            })

    df_tune = pd.DataFrame(grid_results)
    df_tune.to_csv(out_dir / "tuning_results.csv", index=False)
    print(f"Saved: {out_dir / 'tuning_results.csv'}")

    best_row = df_tune.loc[df_tune["mean_r2"].idxmax()]
    best_max_depth = int(best_row["max_depth"])
    best_n_estimators = int(best_row["n_estimators"])
    print(f"Best: max_depth={best_max_depth}, n_estimators={best_n_estimators}, mean R²={best_row['mean_r2']:.4f}")

    # --- Tuning plot 1: Heatmap R² vs (max_depth, n_estimators) ---
    pivot = df_tune.pivot(index="max_depth", columns="n_estimators", values="mean_r2")
    fig, ax = plt.subplots(figsize=(10, 6))
    im = ax.imshow(pivot.values, aspect="auto", cmap="viridis",
                   extent=[pivot.columns.min() - 0.5, pivot.columns.max() + 0.5,
                           pivot.index.max() + 0.5, pivot.index.min() - 0.5])
    ax.set_xlabel("n_estimators")
    ax.set_ylabel("max_depth")
    ax.set_title("Cross-validated R² vs max_depth and n_estimators")
    # Show a subset of ticks if grid is large
    n_est_ticks = pivot.columns
    md_ticks = pivot.index
    if len(n_est_ticks) > 15:
        ax.set_xticks(n_est_ticks[:: max(1, len(n_est_ticks) // 12)])
    else:
        ax.set_xticks(n_est_ticks)
    if len(md_ticks) > 15:
        ax.set_yticks(md_ticks[:: max(1, len(md_ticks) // 10)])
    else:
        ax.set_yticks(md_ticks)
    plt.colorbar(im, ax=ax, label="R²")
    fig.tight_layout()
    fig.savefig(out_dir / "tuning_heatmap_r2.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_dir / 'tuning_heatmap_r2.png'}")

    # --- Tuning plot 2: R² vs max_depth for a few n_estimators ---
    fig, ax = plt.subplots(figsize=(7, 5))
    indices = [0, len(n_est_list) // 2, -1]
    for n_est in [n_est_list[i] for i in indices]:
        sub = df_tune[df_tune["n_estimators"] == n_est].sort_values("max_depth")
        ax.errorbar(sub["max_depth"], sub["mean_r2"], yerr=sub["std_r2"], label=f"n_estimators={n_est}", capsize=2)
    ax.set_xlabel("max_depth")
    ax.set_ylabel("Cross-validated R²")
    ax.set_title("R² vs max_depth (selected n_estimators)")
    ax.legend()
    ax.set_xlim(args.max_depth_min - 0.5, args.max_depth_max + 0.5)
    fig.tight_layout()
    fig.savefig(out_dir / "tuning_r2_vs_max_depth.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_dir / 'tuning_r2_vs_max_depth.png'}")

    # --- Tuning plot 3: R² vs n_estimators for a few max_depths ---
    fig, ax = plt.subplots(figsize=(7, 5))
    for md in [max_depths[i] for i in [0, len(max_depths) // 2, -1]]:
        sub = df_tune[df_tune["max_depth"] == md].sort_values("n_estimators")
        ax.errorbar(sub["n_estimators"], sub["mean_r2"], yerr=sub["std_r2"], label=f"max_depth={md}", capsize=2)
    ax.set_xlabel("n_estimators")
    ax.set_ylabel("Cross-validated R²")
    ax.set_title("R² vs n_estimators (selected max_depth)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_dir / "tuning_r2_vs_n_estimators.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_dir / 'tuning_r2_vs_n_estimators.png'}")

    # --- Top fingerprint features: refit best model on full data, get importances ---
    print("Fitting best model on full data for feature importances...")
    model_best = RandomForestRegressor(
        n_estimators=best_n_estimators,
        max_depth=best_max_depth,
        random_state=args.seed,
        n_jobs=args.n_jobs,
    )
    model_best.fit(X, y)
    imp = pd.Series(model_best.feature_importances_, index=feat_cols)

    drug_imp = imp[drug_feat_cols].sort_values(ascending=False)
    drug_imp.to_csv(out_dir / "fingerprint_importances.csv")
    top_fp = drug_imp.head(args.top_n_fingerprints)

    fig, ax = plt.subplots(figsize=(7, 8))
    y_pos = np.arange(len(top_fp))[::-1]
    ax.barh(y_pos, top_fp.values, color="teal", alpha=0.85)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(top_fp.index.tolist(), fontsize=8)
    ax.set_xlabel("Feature importance")
    ax.set_title(f"Top {args.top_n_fingerprints} Drug Fingerprint Features (best model: max_depth={best_max_depth}, n_est={best_n_estimators})")
    fig.tight_layout()
    fig.savefig(out_dir / "top_fingerprint_features.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_dir / 'top_fingerprint_features.png'}")

    print("Done.")


if __name__ == "__main__":
    main()
