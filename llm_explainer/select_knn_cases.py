#!/usr/bin/env python3
"""
Curate an "outliers + normals" bundle of drug-cell samples via k-nearest-neighbors
in the RF feature space (standardised gene expression + Morgan fingerprints).

For each sample i:

    neighbor_mean_y[i] = mean of the k nearest samples' observed `y` (excluding i)
    residual[i]        = y[i] - neighbor_mean_y[i]

We then pick:
  * `--n-outlier` samples with the largest |residual|  (tagged `outlier_knn`)
  * `--n-normal`  samples with the smallest |residual| (tagged `normal_knn`)

The output CSV is consumable by `llm_explainer/build_shap_reports.py --selection-mode from_csv`.

Typical use (from repo root):

    python llm_explainer/select_knn_cases.py \
        --data-dir data/processed \
        --pairs pairs_ic50.csv \
        --cell-features cell_features_selected_l1000_union.csv \
        --drug-fingerprints drug_fingerprints.csv \
        --k 20 \
        --n-outlier 25 --n-normal 25 \
        --target-label 'log10(IC50)' \
        --out-csv llm_explainer/knn_curated_ic50.csv
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import functools

import numpy as np
import pandas as pd

# Force every print() to flush immediately, otherwise LSF-captured stdout sits
# in a 4-8 KB buffer for the full loading + kneighbors duration and we get no
# live progress.
print = functools.partial(print, flush=True)  # type: ignore[assignment]

# Allow running this script directly from the repo root.
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from train.load_data import load_merged  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Curate outlier + normal samples via KNN in RF feature space."
    )
    parser.add_argument("--data-dir", default="data/processed")
    parser.add_argument(
        "--pairs",
        default="pairs_ic50.csv",
        help="Merged response table with `master_ccl_id`, `master_cpd_id`, `y`.",
    )
    parser.add_argument(
        "--cell-features",
        default="cell_features_selected_l1000_union.csv",
    )
    parser.add_argument(
        "--drug-fingerprints",
        default="drug_fingerprints.csv",
    )
    parser.add_argument(
        "--target-label",
        default="log10(IC50)",
        help="Human-readable target label, used only inside selection_reason strings.",
    )
    parser.add_argument(
        "--k",
        type=int,
        default=20,
        help="Number of nearest neighbors per sample (excluding self).",
    )
    parser.add_argument(
        "--n-outlier",
        type=int,
        default=25,
        help="Number of outlier samples to keep (largest |y - mean(neighbor y)|).",
    )
    parser.add_argument(
        "--n-normal",
        type=int,
        default=25,
        help="Number of normal samples to keep (smallest |y - mean(neighbor y)|).",
    )
    parser.add_argument(
        "--metric",
        choices=["euclidean", "cosine"],
        default="euclidean",
        help="Distance metric over standardised features.",
    )
    parser.add_argument(
        "--algorithm",
        choices=["brute", "ball_tree", "kd_tree", "auto"],
        default="brute",
        help="sklearn NearestNeighbors backend. For high-dim data (d>>20) "
             "'brute' is the only parallelisable choice; the tree backends "
             "are single-threaded in sklearn.",
    )
    parser.add_argument(
        "--query-batch",
        type=int,
        default=4096,
        help="Query batch size when computing nearest neighbors in chunks.",
    )
    parser.add_argument(
        "--n-jobs",
        type=int,
        default=-1,
        help="n_jobs passed to sklearn's NearestNeighbors (use -1 for all cores).",
    )
    parser.add_argument(
        "--diversity-max-per-drug",
        type=int,
        default=0,
        help="If >0, cap the number of picks per drug within each bucket.",
    )
    parser.add_argument(
        "--diversity-max-per-cell",
        type=int,
        default=0,
        help="If >0, cap the number of picks per cell line within each bucket.",
    )
    parser.add_argument(
        "--min-neighbor-std-y",
        type=float,
        default=0.0,
        help="Minimum neighbor-y std required to treat a sample as an outlier "
             "(protects against neighborhoods that are uniformly strange).",
    )
    parser.add_argument(
        "--out-csv",
        default="llm_explainer/knn_curated.csv",
        help="Output CSV consumed by build_shap_reports.py --selection-mode from_csv.",
    )
    parser.add_argument(
        "--out-all-csv",
        default=None,
        help="Optional: also write the full per-sample residual table here.",
    )
    parser.add_argument("--seed", type=int, default=0)
    return parser.parse_args()


def _standardise(X: np.ndarray) -> np.ndarray:
    mu = X.mean(axis=0, keepdims=True)
    sd = X.std(axis=0, keepdims=True)
    sd[sd == 0] = 1.0
    return ((X - mu) / sd).astype(np.float32, copy=False)


def _enforce_diversity(
    df: pd.DataFrame,
    *,
    limit: int,
    max_per_drug: int,
    max_per_cell: int,
) -> pd.DataFrame:
    """Greedy cap selection at ``limit`` respecting per-drug/per-cell caps."""
    if limit <= 0 or df.empty:
        return df.iloc[0:0].copy()

    drug_counts: dict[int, int] = {}
    cell_counts: dict[int, int] = {}
    kept_idx: list[int] = []

    for idx, row in df.iterrows():
        if len(kept_idx) >= limit:
            break
        cpd_id = int(row["master_cpd_id"])
        ccl_id = int(row["master_ccl_id"])
        if max_per_drug > 0 and drug_counts.get(cpd_id, 0) >= max_per_drug:
            continue
        if max_per_cell > 0 and cell_counts.get(ccl_id, 0) >= max_per_cell:
            continue
        kept_idx.append(idx)
        drug_counts[cpd_id] = drug_counts.get(cpd_id, 0) + 1
        cell_counts[ccl_id] = cell_counts.get(ccl_id, 0) + 1

    if len(kept_idx) < limit:
        remaining = df.drop(index=kept_idx)
        for idx, _ in remaining.iterrows():
            if len(kept_idx) >= limit:
                break
            kept_idx.append(idx)

    return df.loc[kept_idx].copy()


def main() -> None:
    args = parse_args()
    rng = np.random.default_rng(args.seed)  # noqa: F841 (reserved for future tie-breaks)

    print(f"[{time.strftime('%T')}] Loading features via train.load_data.load_merged ...")
    X, y, feat_cols, cell_feat_cols, drug_feat_cols, meta = load_merged(
        args.data_dir,
        pairs_file=args.pairs,
        cell_features_file=args.cell_features,
        drug_fingerprints_file=args.drug_fingerprints,
        return_metadata=True,
    )
    print(
        f"  X shape={X.shape}  |  cell_feats={len(cell_feat_cols)}  drug_feats={len(drug_feat_cols)}"
    )

    meta = meta.reset_index(drop=True).copy()
    meta["sample_idx"] = np.arange(len(meta), dtype=np.int64)
    meta["y"] = y

    if args.metric == "cosine":
        norms = np.linalg.norm(X, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        X_std = (X / norms).astype(np.float32, copy=False)
    else:
        print(f"[{time.strftime('%T')}] Standardising features (z-score) ...")
        X_std = _standardise(X)
    print(f"  standardised dtype={X_std.dtype}")

    k = int(args.k)
    if k <= 0:
        raise ValueError("--k must be positive")

    print(
        f"[{time.strftime('%T')}] Fitting NearestNeighbors(k={k}, metric={args.metric}, "
        f"algorithm={args.algorithm}, n_jobs={args.n_jobs}) ..."
    )
    from sklearn.neighbors import NearestNeighbors

    nn = NearestNeighbors(
        n_neighbors=k + 1,
        algorithm=args.algorithm,
        metric=args.metric,
        n_jobs=args.n_jobs,
    )
    nn.fit(X_std)
    print(f"[{time.strftime('%T')}] Fit complete. Starting batched kneighbors() ...")

    n = len(X_std)
    neighbor_mean_y = np.empty(n, dtype=np.float64)
    neighbor_std_y = np.empty(n, dtype=np.float64)
    batch = max(1, int(args.query_batch))

    y_arr = np.asarray(y, dtype=np.float64)
    print(
        f"[{time.strftime('%T')}] Querying k-NN in batches of {batch} "
        f"({int(np.ceil(n / batch))} batches) ..."
    )
    t0 = time.time()
    for start in range(0, n, batch):
        stop = min(n, start + batch)
        _, idx = nn.kneighbors(X_std[start:stop], n_neighbors=k + 1, return_distance=True)
        # First column is self; drop it.
        neighbors = idx[:, 1 : k + 1]
        nn_y = y_arr[neighbors]
        neighbor_mean_y[start:stop] = nn_y.mean(axis=1)
        neighbor_std_y[start:stop] = nn_y.std(axis=1)
        if start % (batch * 5) == 0 or stop == n:
            elapsed = time.time() - t0
            done = stop / n
            eta = elapsed / max(done, 1e-9) - elapsed
            print(
                f"  [{time.strftime('%T')}] {stop:>8}/{n}  "
                f"({100*done:5.1f}% | elapsed {elapsed/60:5.1f}m | eta {eta/60:5.1f}m)"
            )

    residual = y_arr - neighbor_mean_y
    abs_residual = np.abs(residual)

    full = meta.copy()
    full["neighbor_mean_y"] = neighbor_mean_y
    full["neighbor_std_y"] = neighbor_std_y
    full["residual"] = residual
    full["abs_residual"] = abs_residual

    if args.out_all_csv:
        out_all = Path(args.out_all_csv)
        out_all.parent.mkdir(parents=True, exist_ok=True)
        full.to_csv(out_all, index=False)
        print(f"Wrote full residual table: {out_all}")

    eligible_out = full[full["neighbor_std_y"] >= float(args.min_neighbor_std_y)].copy()

    outliers_sorted = eligible_out.sort_values(
        ["abs_residual", "sample_idx"], ascending=[False, True]
    )
    outliers = _enforce_diversity(
        outliers_sorted,
        limit=args.n_outlier,
        max_per_drug=args.diversity_max_per_drug,
        max_per_cell=args.diversity_max_per_cell,
    )

    normals_sorted = full.sort_values(
        ["abs_residual", "sample_idx"], ascending=[True, True]
    )
    # Exclude samples already chosen as outliers.
    if not outliers.empty:
        normals_sorted = normals_sorted[~normals_sorted["sample_idx"].isin(outliers["sample_idx"])]
    normals = _enforce_diversity(
        normals_sorted,
        limit=args.n_normal,
        max_per_drug=args.diversity_max_per_drug,
        max_per_cell=args.diversity_max_per_cell,
    )

    label = args.target_label
    outliers = outliers.assign(
        selection_tag="outlier_knn",
        selection_reason=[
            f"curated outlier: observed {label}={yv:+.3f} vs {k}-NN "
            f"mean={nm:+.3f} (|Δ|={abs(abs_r):.3f})"
            for yv, nm, abs_r in zip(outliers["y"], outliers["neighbor_mean_y"], outliers["abs_residual"])
        ],
        rank=list(range(1, len(outliers) + 1)),
    )
    normals = normals.assign(
        selection_tag="normal_knn",
        selection_reason=[
            f"curated normal: observed {label}={yv:+.3f} matches {k}-NN "
            f"mean={nm:+.3f} (|Δ|={abs(abs_r):.3f})"
            for yv, nm, abs_r in zip(normals["y"], normals["neighbor_mean_y"], normals["abs_residual"])
        ],
        rank=list(range(len(outliers) + 1, len(outliers) + 1 + len(normals))),
    )

    keep_cols = [
        "rank",
        "selection_tag",
        "selection_reason",
        "master_ccl_id",
        "master_cpd_id",
        "y",
        "neighbor_mean_y",
        "neighbor_std_y",
        "residual",
        "abs_residual",
    ]
    if "ModelID" in full.columns:
        keep_cols.append("ModelID")
    if "cpd_name" in full.columns:
        keep_cols.append("cpd_name")

    curated = pd.concat(
        [outliers[keep_cols], normals[keep_cols]],
        ignore_index=True,
    )

    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    curated.to_csv(out_csv, index=False)
    print(
        f"Wrote curated bundle ({len(outliers)} outliers + {len(normals)} normals): {out_csv}"
    )

    # Print a short distribution summary for quick sanity checking.
    desc = full["abs_residual"].describe()
    print(
        "\nabs_residual stats over all samples:\n"
        f"  n={int(desc['count'])}  mean={desc['mean']:.3f}  std={desc['std']:.3f}\n"
        f"  q25={desc['25%']:.3f}  q50={desc['50%']:.3f}  q75={desc['75%']:.3f}\n"
        f"  q95={full['abs_residual'].quantile(0.95):.3f}  "
        f"q99={full['abs_residual'].quantile(0.99):.3f}  max={desc['max']:.3f}"
    )
    print(
        f"Outliers  |Δ| range: "
        f"{outliers['abs_residual'].min():.3f} — {outliers['abs_residual'].max():.3f}"
    )
    print(
        f"Normals   |Δ| range: "
        f"{normals['abs_residual'].min():.4f} — {normals['abs_residual'].max():.4f}"
    )


if __name__ == "__main__":
    main()
