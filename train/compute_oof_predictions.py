#!/usr/bin/env python3
"""
Produce out-of-fold (OOF) predictions for the RF log10(IC50) model.

Each sample gets a prediction from a model that was *not* trained on it, so
``y_obs - y_hat`` is a clean residual we can use downstream (e.g. for picking
"the model was wrong here" samples to explain with an LLM).

Usage (from repo root):

    python train/compute_oof_predictions.py \
        --data-dir data/processed \
        --pairs pairs_ic50.csv \
        --cell-features cell_features_selected_l1000_union.csv \
        --drug-fingerprints drug_fingerprints.csv \
        --n-estimators 100 --max-depth 10 \
        --n-splits 5 --n-jobs 16 \
        --out-csv results_ic50/oof_predictions.csv

Output CSV columns: master_ccl_id, master_cpd_id, y_obs, y_pred, fold, residual.
"""
from __future__ import annotations

import argparse
import functools
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

print = functools.partial(print, flush=True)  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from train.load_data import load_merged  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="5-fold OOF predictions for the RF IC50 model.")
    p.add_argument("--data-dir", default="data/processed")
    p.add_argument("--pairs", default="pairs_ic50.csv")
    p.add_argument("--cell-features", default="cell_features_selected_l1000_union.csv")
    p.add_argument("--drug-fingerprints", default="drug_fingerprints.csv")
    p.add_argument("--n-estimators", type=int, default=100)
    p.add_argument("--max-depth", type=int, default=10)
    p.add_argument("--n-splits", type=int, default=5)
    p.add_argument("--n-jobs", type=int, default=-1)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument(
        "--out-csv",
        default="results_ic50/oof_predictions.csv",
        help="Output CSV with per-sample OOF predictions + residuals.",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import KFold
    from sklearn.metrics import r2_score

    print(f"[{time.strftime('%T')}] Loading merged features ...")
    X, y, feat_cols, cell_feat_cols, drug_feat_cols, meta = load_merged(
        args.data_dir,
        pairs_file=args.pairs,
        cell_features_file=args.cell_features,
        drug_fingerprints_file=args.drug_fingerprints,
        return_metadata=True,
    )
    print(
        f"  X shape={X.shape}  cell_feats={len(cell_feat_cols)}  drug_feats={len(drug_feat_cols)}"
    )

    n = len(y)
    y_pred = np.full(n, np.nan, dtype=np.float64)
    fold_id = np.full(n, -1, dtype=np.int32)

    kf = KFold(n_splits=args.n_splits, shuffle=True, random_state=args.seed)
    fold_r2 = []

    for fold, (train_idx, test_idx) in enumerate(kf.split(X)):
        print(
            f"[{time.strftime('%T')}] Fold {fold + 1}/{args.n_splits}: "
            f"train={len(train_idx):,}  test={len(test_idx):,}"
        )
        model = RandomForestRegressor(
            n_estimators=args.n_estimators,
            max_depth=args.max_depth,
            random_state=args.seed + fold,
            n_jobs=args.n_jobs,
        )
        model.fit(X[train_idx], y[train_idx])
        yp = model.predict(X[test_idx])
        y_pred[test_idx] = yp
        fold_id[test_idx] = fold
        r2 = r2_score(y[test_idx], yp)
        fold_r2.append(r2)
        print(f"  fold {fold + 1} test R² = {r2:.4f}")

    overall_r2 = r2_score(y, y_pred)
    print(
        f"[{time.strftime('%T')}] Done. per-fold R²={[f'{r:.4f}' for r in fold_r2]}  "
        f"overall_oof_r2={overall_r2:.4f}"
    )

    out = meta.reset_index(drop=True).copy()
    out["y_obs"] = y
    out["y_pred"] = y_pred
    out["fold"] = fold_id
    out["residual"] = out["y_obs"] - out["y_pred"]

    keep = [c for c in ("master_ccl_id", "master_cpd_id", "ModelID", "cpd_name") if c in out.columns]
    keep += ["y_obs", "y_pred", "fold", "residual"]
    out = out[keep]

    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_csv, index=False)
    print(f"Wrote OOF predictions: {out_csv}  ({len(out):,} rows)")


if __name__ == "__main__":
    main()
