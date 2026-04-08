#!/usr/bin/env python3
"""
Tune max_depth only (fixed n_estimators). Fast 1D grid search.
Saves tuning_results_max_depth.csv and tuning_r2_vs_max_depth.png.

Usage:
  python train/tune_max_depth.py --data-dir data/processed --out-dir results/tuning --n-estimators 100
  python train/tune_max_depth.py --n-estimators 150 --max-depth-min 1 --max-depth-max 25
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import sys
if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
from load_data import load_merged


def main() -> None:
    parser = argparse.ArgumentParser(description="Tune max_depth with fixed n_estimators.")
    parser.add_argument("--data-dir", default="data/processed", help="Directory with pairs, cell_features, drug_fingerprints.")
    parser.add_argument("--pairs", default="pairs.csv")
    parser.add_argument("--cell-features", default="cell_features_selected.csv")
    parser.add_argument("--drug-fingerprints", default="drug_fingerprints.csv")
    parser.add_argument("--out-dir", default="results/tuning", help="Output directory.")
    parser.add_argument("--n-estimators", type=int, default=100, help="Fixed n_estimators for all runs.")
    parser.add_argument("--max-depth-min", type=int, default=1)
    parser.add_argument("--max-depth-max", type=int, default=20)
    parser.add_argument("--max-depth-step", type=int, default=1)
    parser.add_argument("--train-frac", type=float, default=0.8, help="Fraction of data for training (rest for test R²).")
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

    max_depths = list(range(args.max_depth_min, args.max_depth_max + 1, args.max_depth_step))

    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, train_size=args.train_frac, random_state=args.seed, shuffle=True
    )
    results: list[dict] = []

    for i, max_depth in enumerate(max_depths):
        print(f"  {i + 1}/{len(max_depths)}: max_depth={max_depth}")
        model = RandomForestRegressor(
            n_estimators=args.n_estimators,
            max_depth=max_depth,
            random_state=args.seed,
            n_jobs=args.n_jobs,
        )
        model.fit(X_tr, y_tr)
        y_pred = model.predict(X_te)
        r2 = r2_score(y_te, y_pred)
        results.append({
            "max_depth": max_depth,
            "n_estimators": args.n_estimators,
            "r2": float(r2),
        })

    df = pd.DataFrame(results)
    out_csv = out_dir / "tuning_results_max_depth.csv"
    df.to_csv(out_csv, index=False)
    print(f"Saved: {out_csv}")

    best = df.loc[df["r2"].idxmax()]
    print(f"Best: max_depth={int(best['max_depth'])}, test R²={best['r2']:.4f}")

    # Plot R² vs max_depth
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(df["max_depth"], df["r2"], "o-")
    ax.set_xlabel("max_depth")
    ax.set_ylabel("Test R²")
    ax.set_title(f"Test R² vs max_depth (n_estimators={args.n_estimators} fixed)")
    fig.tight_layout()
    out_png = out_dir / "tuning_r2_vs_max_depth.png"
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_png}")
    print("Done.")


if __name__ == "__main__":
    main()
