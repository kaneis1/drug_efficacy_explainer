#!/usr/bin/env python3
"""
Tune n_estimators only (fixed max_depth). Fast 1D grid search.
Saves tuning_results_n_estimators.csv and tuning_r2_vs_n_estimators.png.

Usage:
  python train/tune_n_estimators.py --data-dir data/processed --out-dir results/tuning --max-depth 10
  python train/tune_n_estimators.py --max-depth 5 --n-estimators-max 200 --n-estimators-step 25
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

# Allow running from project root: python train/tune_n_estimators.py
import sys
if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
from load_data import load_merged


def main() -> None:
    parser = argparse.ArgumentParser(description="Tune n_estimators with fixed max_depth.")
    parser.add_argument("--data-dir", default="data/processed", help="Directory with pairs, cell_features, drug_fingerprints.")
    parser.add_argument("--pairs", default="pairs.csv")
    parser.add_argument("--cell-features", default="cell_features_selected.csv")
    parser.add_argument("--drug-fingerprints", default="drug_fingerprints.csv")
    parser.add_argument("--out-dir", default="results/tuning", help="Output directory.")
    parser.add_argument("--max-depth", type=int, default=10, help="Fixed max_depth for all runs.")
    parser.add_argument("--n-estimators-min", type=int, default=10)
    parser.add_argument("--n-estimators-max", type=int, default=250)
    parser.add_argument("--n-estimators-step", type=int, default=25)
    parser.add_argument("--cv-folds", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--n-jobs", type=int, default=1)
    args = parser.parse_args()

    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Loading data...")
    X, y, feat_cols, cell_feat_cols, drug_feat_cols = load_merged(
        args.data_dir, args.pairs, args.cell_features, args.drug_fingerprints
    )
    print(f"X: {X.shape}, y: {y.shape}")

    n_est_list = list(range(args.n_estimators_min, args.n_estimators_max + 1, args.n_estimators_step))
    if args.n_estimators_max not in n_est_list:
        n_est_list.append(args.n_estimators_max)
    n_est_list = sorted(set(n_est_list))

    kf = KFold(n_splits=args.cv_folds, shuffle=True, random_state=args.seed)
    results: list[dict] = []

    for i, n_estimators in enumerate(n_est_list):
        
        print(f"  {i + 1}/{len(n_est_list)}: n_estimators={n_estimators}")
        r2_folds = []
        for tr_idx, te_idx in kf.split(X):
            model = RandomForestRegressor(
                n_estimators=n_estimators,
                max_depth=args.max_depth,
                random_state=args.seed,
                n_jobs=args.n_jobs,
            )
            model.fit(X[tr_idx], y[tr_idx])
            y_pred = model.predict(X[te_idx])
            r2_folds.append(r2_score(y[te_idx], y_pred))
        results.append({
            "max_depth": args.max_depth,
            "n_estimators": n_estimators,
            "mean_r2": float(np.mean(r2_folds)),
            "std_r2": float(np.std(r2_folds)),
        })

    df = pd.DataFrame(results)
    out_csv = out_dir / "tuning_results_n_estimators.csv"
    df.to_csv(out_csv, index=False)
    print(f"Saved: {out_csv}")

    best = df.loc[df["mean_r2"].idxmax()]
    print(f"Best: n_estimators={int(best['n_estimators'])}, mean R²={best['mean_r2']:.4f}")

    # Plot R² vs n_estimators
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.errorbar(df["n_estimators"], df["mean_r2"], yerr=df["std_r2"], capsize=2)
    ax.set_xlabel("n_estimators")
    ax.set_ylabel("Cross-validated R²")
    ax.set_title(f"R² vs n_estimators (max_depth={args.max_depth} fixed)")
    fig.tight_layout()
    out_png = out_dir / "tuning_r2_vs_n_estimators.png"
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_png}")
    print("Done.")


if __name__ == "__main__":
    main()
