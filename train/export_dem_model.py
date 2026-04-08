#!/usr/bin/env python3
"""Fit one DEM random forest and export model, leaves, and metrics."""
from __future__ import annotations

import argparse
import json
import pickle
import sys
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from kernel import (
    compute_leaf_assignments,
    compute_depth_matrix,
    compute_tree_weights,
    save_leaf_assignments,
)
from load_data import load_merged


def _corrcoef_safe(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    if len(y_true) <= 1:
        return 0.0
    corr = np.corrcoef(y_true, y_pred)[0, 1]
    return float(0.0 if not np.isfinite(corr) else corr)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fit one DEM random forest and export leaf assignments."
    )
    parser.add_argument("--data-dir", default="data/processed")
    parser.add_argument("--pairs", default="pairs.csv")
    parser.add_argument("--cell-features", default="cell_features_selected.csv")
    parser.add_argument("--drug-fingerprints", default="drug_fingerprints.csv")
    parser.add_argument("--out-dir", default="results/dem")
    parser.add_argument("--n-estimators", type=int, default=100)
    parser.add_argument("--max-depth", type=int, default=10)
    parser.add_argument("--n-jobs", type=int, default=1)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Loading merged training data...")
    X, y, feat_cols, cell_feat_cols, drug_feat_cols, sample_meta = load_merged(
        args.data_dir,
        args.pairs,
        args.cell_features,
        args.drug_fingerprints,
        return_metadata=True,
    )
    print(
        f"Loaded X={X.shape}, y={y.shape} "
        f"(cell features={len(cell_feat_cols)}, drug features={len(drug_feat_cols)})"
    )

    print("Fitting DEM random forest on full dataset...")
    model = RandomForestRegressor(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        random_state=args.seed,
        n_jobs=args.n_jobs,
    )
    model.fit(X, y)

    print("Scoring fitted model...")
    y_pred = model.predict(X)
    rmse = float(np.sqrt(mean_squared_error(y, y_pred)))
    metrics = {
        "target": "y",
        "n_samples": int(X.shape[0]),
        "n_features": int(X.shape[1]),
        "n_cell_features": int(len(cell_feat_cols)),
        "n_drug_features": int(len(drug_feat_cols)),
        "n_estimators": int(args.n_estimators),
        "max_depth": int(args.max_depth),
        "seed": int(args.seed),
        "train_r2": float(r2_score(y, y_pred)),
        "train_rmse": rmse,
        "train_corr": _corrcoef_safe(y, y_pred),
    }

    print("Computing per-sample leaf assignments...")
    leaf_assignments = compute_leaf_assignments(model, X)

    print("Computing per-tree OOB weights...")
    tree_weights = compute_tree_weights(model, X, y)
    print(
        f"  Tree weight stats: mean={tree_weights.mean():.4f}, "
        f"std={tree_weights.std():.4f}, min={tree_weights.min():.4f}, "
        f"max={tree_weights.max():.4f}"
    )

    print("Computing leaf depth matrix...")
    depth_matrix, max_depths = compute_depth_matrix(model, leaf_assignments)
    print(
        f"  Max tree depths: min={max_depths.min():.0f}, "
        f"max={max_depths.max():.0f}, mean={max_depths.mean():.1f}"
    )

    export_meta = sample_meta.copy()
    export_meta.insert(0, "sample_idx", np.arange(len(export_meta), dtype=np.int64))
    export_meta["y_true"] = y.astype(float)
    export_meta["y_pred"] = y_pred.astype(float)

    model_path = out_dir / "dem_model.pkl"
    leaves_path = out_dir / "leaf_assignments.parquet"
    kernel_meta_path = out_dir / "kernel_meta.npz"
    metrics_path = out_dir / "metrics_dem.json"

    print(f"Saving model to {model_path}...")
    with model_path.open("wb") as f:
        pickle.dump(
            {
                "model": model,
                "feature_names": feat_cols,
                "cell_feature_names": cell_feat_cols,
                "drug_feature_names": drug_feat_cols,
            },
            f,
        )

    print(f"Saving leaves to {leaves_path}...")
    save_leaf_assignments(leaves_path, leaf_assignments, sample_meta=export_meta)

    print(f"Saving kernel metadata to {kernel_meta_path}...")
    np.savez(
        kernel_meta_path,
        tree_weights=tree_weights,
        depth_matrix=depth_matrix,
        max_depths=max_depths,
    )

    print(f"Saving metrics to {metrics_path}...")
    with metrics_path.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
        f.write("\n")

    print("Done.")
    print(f"Model:       {model_path}")
    print(f"Leaves:      {leaves_path}")
    print(f"Kernel meta: {kernel_meta_path}")
    print(f"Metrics:     {metrics_path}")


if __name__ == "__main__":
    main()
