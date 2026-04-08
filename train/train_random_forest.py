#!/usr/bin/env python3
"""DEM Reproduction: Train Random Forest on AUC, report RMSE/R²/correlation, 5-fold CV."""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold


def main() -> None:
    parser = argparse.ArgumentParser(
        description="DEM Reproduction: Random Forest on AUC with 5-fold CV."
    )
    parser.add_argument("--data-dir", default="data/processed", help="Directory with pairs, cell_features, drug_fingerprints.")
    parser.add_argument("--pairs", default="pairs.csv", help="Pairs file.")
    parser.add_argument("--cell-features", default="cell_features_selected.csv", help="Cell features file.")
    parser.add_argument("--drug-fingerprints", default="drug_fingerprints.csv", help="Drug fingerprints file.")
    parser.add_argument("--cv-folds", type=int, default=5, help="Number of CV folds.")
    parser.add_argument("--n-chunks", type=int, default=1, help="Chunks for merge (saves memory).")
    parser.add_argument("--n-estimators", type=int, default=100, help="Number of trees.")
    parser.add_argument("--max-depth", type=int, default=5, help="Max tree depth.")
    parser.add_argument("--n-jobs", type=int, default=1, help="Parallel jobs for RandomForest.")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    base = Path(args.data_dir).resolve()
    pairs_path = base / args.pairs
    cell_path = base / args.cell_features
    drug_path = base / args.drug_fingerprints
    for p in [pairs_path, cell_path, drug_path]:
        if not p.exists():
            raise FileNotFoundError(f"Not found: {p}")

    print("Loading pairs...")
    pairs = pd.read_csv(pairs_path)
    print("Loading cell features...")
    cell = pd.read_csv(cell_path)
    print("Loading drug fingerprints...")
    drug = pd.read_csv(drug_path)

    cell_id_col = "master_ccl_id"
    drug_id_col = "master_cpd_id"
    cell_feat_cols = [c for c in cell.columns if c not in (cell_id_col, "ModelID")]
    drug_feat_cols = [c for c in drug.columns if c != drug_id_col]
    feat_cols = cell_feat_cols + drug_feat_cols

    n_chunks = max(1, args.n_chunks)

    
        
    print("Merging (full)...")
    merged = (
        pairs.merge(cell[[cell_id_col] + cell_feat_cols], on=cell_id_col, how="inner")
        .merge(drug[[drug_id_col] + drug_feat_cols], on=drug_id_col, how="inner")
    )
    print("Preparing feature matrix X and target vector y...")
    X = merged[feat_cols].values.astype(np.float64)
    y = merged["y"].values.astype(np.float64)
    # CDK (and other) descriptors can be inf/nan or overflow float32; sanitize for sklearn
    np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0, copy=False)
    f32_max, f32_min = np.finfo(np.float32).max, np.finfo(np.float32).min
    np.clip(X, f32_min, f32_max, out=X)
    X = X.astype(np.float32)
    y = y.astype(np.float32)
    print(f"Shapes - X: {X.shape}, y: {y.shape}")
    print("Setting up KFold cross-validation...")
    kf = KFold(n_splits=args.cv_folds, shuffle=True, random_state=args.seed)
    r2_scores, rmse_scores, corr_scores = [], [], []
    for fold, (tr_idx, te_idx) in enumerate(kf.split(X)):
        print(f"Starting fold {fold + 1}/{args.cv_folds}")
        print(f"  Train indices: {len(tr_idx)} samples, Test indices: {len(te_idx)} samples")
        X_train, X_test = X[tr_idx], X[te_idx]
        y_train, y_test = y[tr_idx], y[te_idx]
        print("  Initializing RandomForestRegressor...")
        model = RandomForestRegressor(
            n_estimators=args.n_estimators,
            max_depth=args.max_depth,
            random_state=args.seed + fold,
            n_jobs=args.n_jobs,
        )
        print("  Training RandomForestRegressor...")
        model.fit(X_train, y_train)

        # Evaluate on training data
        print("  Predicting on training set...")
        y_train_pred = model.predict(X_train)
        r2_train = r2_score(y_train, y_train_pred)
        rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
        corr_train = np.corrcoef(y_train, y_train_pred)[0, 1] if len(y_train) > 1 else 0.0

        # Evaluate on test data
        print("  Predicting on test set...")
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        corr = np.corrcoef(y_test, y_pred)[0, 1] if len(y_test) > 1 else 0.0

        r2_scores.append(r2)
        rmse_scores.append(rmse)
        corr_scores.append(corr)

        print(f"  Fold {fold + 1}/{args.cv_folds} complete:")
        print(f"    Train: R²={r2_train:.4f}  RMSE={rmse_train:.4f}  Corr={corr_train:.4f}")
        print(f"    Test:  R²={r2:.4f}  RMSE={rmse:.4f}  Corr={corr:.4f}")
        print("-" * 40)

    r2_mean, r2_std = np.mean(r2_scores), np.std(r2_scores)
    rmse_mean, rmse_std = np.mean(rmse_scores), np.std(rmse_scores)
    corr_mean, corr_std = np.mean(corr_scores), np.std(corr_scores)
    print(f"\n--- {args.cv_folds}-fold CV (mean ± std) ---")
    print(f"R²:       {r2_mean:.4f} ± {r2_std:.4f}")
    print(f"RMSE:     {rmse_mean:.4f} ± {rmse_std:.4f}")
    print(f"Corr:     {corr_mean:.4f} ± {corr_std:.4f}")


if __name__ == "__main__":
    main()
