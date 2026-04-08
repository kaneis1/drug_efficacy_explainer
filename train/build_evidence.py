#!/usr/bin/env python3
"""Build grounded evidence objects from DEM leaf-kernel neighborhoods."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from kernel import topk_leaf_agreement
from load_data import load_merged


def _tree_col_key(col: str) -> int:
    m = re.match(r"tree_(\d+)_leaf$", col)
    return int(m.group(1)) if m else 10**12


def _parse_query_indices(
    mode: str, n_samples: int, y: np.ndarray, count: int, seed: int
) -> np.ndarray:
    count = int(max(1, min(count, n_samples)))
    if mode == "random":
        rng = np.random.default_rng(seed)
        return np.sort(rng.choice(n_samples, size=count, replace=False))
    if mode == "extremes":
        half = count // 2
        low = np.argsort(y)[:half]
        high = np.argsort(y)[-max(1, count - half) :]
        return np.unique(np.concatenate([low, high]))[:count]
    # "head"
    return np.arange(count, dtype=np.int64)


def _clean_value(v):
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.floating,)):
        return float(v)
    if isinstance(v, (np.bool_,)):
        return bool(v)
    return v


def _metadata_row(sample_meta: pd.DataFrame, idx: int) -> dict:
    row = sample_meta.iloc[idx].to_dict()
    return {k: _clean_value(v) for k, v in row.items()}


def _global_feature_stats(X: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    std = np.where(std < 1e-12, 1.0, std)
    return mean, std


def _distinguishing_features(
    X: np.ndarray,
    feat_cols: list[str],
    query_idx: int,
    neighbor_idx: np.ndarray,
    neighbor_scores: np.ndarray,
    global_mean: np.ndarray,
    global_std: np.ndarray,
    top_n: int,
) -> list[dict]:
    weights = neighbor_scores.astype(np.float64)
    if np.sum(weights) <= 0:
        weights = np.ones_like(weights, dtype=np.float64)
    weights = weights / np.sum(weights)

    neigh_mean = np.average(X[neighbor_idx], axis=0, weights=weights)
    delta = neigh_mean - global_mean
    z = delta / global_std

    n = min(top_n, len(feat_cols))
    chosen = np.argpartition(np.abs(z), -n)[-n:]
    chosen = chosen[np.argsort(-np.abs(z[chosen]))]

    out: list[dict] = []
    for j in chosen:
        out.append(
            {
                "feature": feat_cols[j],
                "direction": "higher" if delta[j] >= 0 else "lower",
                "z_score": float(z[j]),
                "delta_vs_global": float(delta[j]),
                "global_mean": float(global_mean[j]),
                "neighborhood_mean": float(neigh_mean[j]),
                "query_value": float(X[query_idx, j]),
            }
        )
    return out


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build evidence.jsonl from leaf-kernel neighborhoods."
    )
    parser.add_argument("--data-dir", default="data/processed")
    parser.add_argument("--pairs", default="pairs.csv")
    parser.add_argument("--cell-features", default="cell_features_selected.csv")
    parser.add_argument("--drug-fingerprints", default="drug_fingerprints.csv")
    parser.add_argument("--leaves-parquet", default="results/dem/leaf_assignments.parquet")
    parser.add_argument("--kernel-meta", default="results/dem/kernel_meta.npz")
    parser.add_argument("--out-evidence", default="results/dem/evidence.jsonl")
    parser.add_argument("--query-mode", choices=["random", "extremes", "head"], default="extremes")
    parser.add_argument("--num-queries", type=int, default=10)
    parser.add_argument("--top-k-neighbors", type=int, default=200)
    parser.add_argument("--top-features", type=int, default=12)
    parser.add_argument("--train-batch-size", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    out_path = Path(args.out_evidence).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print("Loading merged features and metadata...")
    X, y, feat_cols, _cell_feat_cols, _drug_feat_cols, sample_meta = load_merged(
        args.data_dir,
        args.pairs,
        args.cell_features,
        args.drug_fingerprints,
        return_metadata=True,
    )

    print("Loading leaf assignments...")
    leaf_df = pd.read_parquet(args.leaves_parquet)
    tree_cols = sorted(
        [c for c in leaf_df.columns if re.match(r"tree_\d+_leaf$", c)],
        key=_tree_col_key,
    )
    if not tree_cols:
        raise ValueError("No tree leaf columns found in leaves parquet.")

    train_leaves = leaf_df[tree_cols].to_numpy(dtype=np.int64, copy=False)
    if train_leaves.shape[0] != X.shape[0]:
        raise ValueError(
            f"Row mismatch: leaves has {train_leaves.shape[0]} rows, merged data has {X.shape[0]}."
        )

    query_idx = _parse_query_indices(
        mode=args.query_mode,
        n_samples=X.shape[0],
        y=y,
        count=args.num_queries,
        seed=args.seed,
    )
    print(f"Selected {len(query_idx)} query samples.")

    tree_weights = None
    query_depths = None
    max_depths = None
    kernel_meta_path = Path(args.kernel_meta).resolve()
    if kernel_meta_path.exists():
        print(f"Loading kernel metadata from {kernel_meta_path}...")
        km = np.load(kernel_meta_path)
        tree_weights = km["tree_weights"]
        max_depths = km["max_depths"]
        depth_matrix = km["depth_matrix"]
        query_depths = depth_matrix[query_idx]
        print(
            f"  Using tree weights (mean={tree_weights.mean():.4f}) "
            f"and depth-aware kernel (max depths {max_depths.min():.0f}–{max_depths.max():.0f})"
        )
    else:
        print("No kernel_meta.npz found — using unweighted leaf-agreement kernel.")

    print("Computing top-k kernel neighbors...")
    query_leaves = train_leaves[query_idx]
    topk_scores, topk_indices = topk_leaf_agreement(
        query_leaves=query_leaves,
        train_leaves=train_leaves,
        k=args.top_k_neighbors,
        train_batch_size=args.train_batch_size,
        exclude_self_indices=query_idx,
        tree_weights=tree_weights,
        query_depths=query_depths,
        max_depths=max_depths,
    )

    global_mean, global_std = _global_feature_stats(X)
    y_global = {
        "mean": float(np.mean(y)),
        "std": float(np.std(y)),
        "q10": float(np.quantile(y, 0.10)),
        "q50": float(np.quantile(y, 0.50)),
        "q90": float(np.quantile(y, 0.90)),
    }

    print(f"Writing evidence to {out_path} ...")
    with out_path.open("w", encoding="utf-8") as f:
        for rank, qidx in enumerate(query_idx, start=1):
            nbr_idx = topk_indices[rank - 1]
            nbr_scores = topk_scores[rank - 1]
            valid = nbr_idx >= 0
            nbr_idx = nbr_idx[valid]
            nbr_scores = nbr_scores[valid]
            nbr_y = y[nbr_idx]

            weights = nbr_scores.astype(np.float64)
            if np.sum(weights) <= 0:
                weights = np.ones_like(weights, dtype=np.float64)
            weights = weights / np.sum(weights)
            y_weighted_mean = float(np.sum(weights * nbr_y))

            dist_features = _distinguishing_features(
                X=X,
                feat_cols=feat_cols,
                query_idx=int(qidx),
                neighbor_idx=nbr_idx,
                neighbor_scores=nbr_scores,
                global_mean=global_mean,
                global_std=global_std,
                top_n=args.top_features,
            )

            neighbor_examples = []
            for i in range(min(5, len(nbr_idx))):
                nidx = int(nbr_idx[i])
                nmeta = _metadata_row(sample_meta, nidx)
                neighbor_examples.append(
                    {
                        "sample_idx": nidx,
                        "kernel_score": float(nbr_scores[i]),
                        "y": float(y[nidx]),
                        "meta": nmeta,
                    }
                )

            rec = {
                "evidence_id": f"EV-{rank:06d}",
                "type": "kernel_neighborhood",
                "query": {
                    "sample_idx": int(qidx),
                    "y_true": float(y[qidx]),
                    "meta": _metadata_row(sample_meta, int(qidx)),
                },
                "kernel": {
                    "top_k": int(len(nbr_idx)),
                    "score_mean": float(np.mean(nbr_scores)),
                    "score_max": float(np.max(nbr_scores)),
                    "score_min": float(np.min(nbr_scores)),
                },
                "response_distribution": {
                    "global": y_global,
                    "neighbors": {
                        "mean": float(np.mean(nbr_y)),
                        "weighted_mean": y_weighted_mean,
                        "std": float(np.std(nbr_y)),
                        "q10": float(np.quantile(nbr_y, 0.10)),
                        "q50": float(np.quantile(nbr_y, 0.50)),
                        "q90": float(np.quantile(nbr_y, 0.90)),
                        "min": float(np.min(nbr_y)),
                        "max": float(np.max(nbr_y)),
                    },
                },
                "top_distinguishing_features": dist_features,
                "neighbor_examples": neighbor_examples,
                "provenance": {
                    "leaves_parquet": str(Path(args.leaves_parquet).resolve()),
                    "data_dir": str(Path(args.data_dir).resolve()),
                },
            }
            f.write(json.dumps(rec, ensure_ascii=True) + "\n")

    print("Done.")
    print(f"Evidence file: {out_path}")


if __name__ == "__main__":
    main()
