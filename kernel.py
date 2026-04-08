from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def compute_leaf_assignments(model, X: np.ndarray) -> np.ndarray:
    """Return per-sample leaf IDs with shape (n_samples, n_trees)."""
    leaves = model.apply(X)
    leaves = np.asarray(leaves)
    if leaves.ndim == 1:
        leaves = leaves[:, None]
    return leaves.astype(np.int64, copy=False)


def compute_tree_weights(model, X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Per-tree OOB R² as tree quality weights.

    Reconstructs each tree's out-of-bag samples by replaying the same
    bootstrap draw that sklearn used during fitting, then scores the
    single tree on those held-out samples.  Negative R² is clipped to 0.
    Weights are normalized so their mean equals 1.
    """
    try:
        from sklearn.ensemble._forest import _generate_sample_indices
    except ImportError:
        from sklearn.utils import check_random_state

        def _generate_sample_indices(random_state, n_samples, n_samples_bootstrap):
            return check_random_state(random_state).randint(
                0, n_samples, n_samples_bootstrap
            )

    n_samples = X.shape[0]
    n_trees = len(model.estimators_)
    weights = np.ones(n_trees, dtype=np.float64)

    for t, estimator in enumerate(model.estimators_):
        boot_idx = _generate_sample_indices(
            estimator.random_state, n_samples, n_samples
        )
        oob_mask = np.ones(n_samples, dtype=bool)
        oob_mask[np.unique(boot_idx)] = False

        if oob_mask.sum() < 2:
            weights[t] = 0.0
            continue

        y_oob = y[oob_mask]
        y_pred = estimator.predict(X[oob_mask])
        ss_tot = np.sum((y_oob - y_oob.mean()) ** 2)
        if ss_tot < 1e-15:
            weights[t] = 0.0
            continue
        r2 = 1.0 - np.sum((y_oob - y_pred) ** 2) / ss_tot
        weights[t] = max(0.0, float(r2))

    w_mean = weights.mean()
    if w_mean > 0:
        weights /= w_mean
    else:
        weights[:] = 1.0

    return weights


def compute_depth_matrix(
    model, leaf_assignments: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    Per-sample leaf depth for every tree.

    Returns
    -------
    depth_matrix : int16 array, shape (n_samples, n_trees)
        Depth of the leaf each sample lands in.
    max_depths : float32 array, shape (n_trees,)
        Maximum leaf depth in each tree (used to normalize depths to [0, 1]).
    """
    n_samples, n_trees = leaf_assignments.shape
    depth_matrix = np.empty((n_samples, n_trees), dtype=np.int16)
    max_depths = np.empty(n_trees, dtype=np.float32)

    for t, estimator in enumerate(model.estimators_):
        tree = estimator.tree_
        node_depth = np.zeros(tree.node_count, dtype=np.int16)
        stack = [(0, 0)]
        while stack:
            nid, d = stack.pop()
            node_depth[nid] = d
            left = tree.children_left[nid]
            right = tree.children_right[nid]
            if left != -1:
                stack.append((left, d + 1))
                stack.append((right, d + 1))

        depth_matrix[:, t] = node_depth[leaf_assignments[:, t]]
        max_depths[t] = max(float(node_depth.max()), 1.0)

    return depth_matrix, max_depths


def _weighted_agreement(
    agree: np.ndarray,
    tree_weights: np.ndarray | None,
    query_depths_batch: np.ndarray | None,
    max_depths: np.ndarray | None,
    dtype: np.dtype,
) -> np.ndarray:
    """
    Apply tree-weighting and/or depth-aware scaling to a boolean agreement
    tensor of shape (n_q, n_t, n_trees).

    Depth scaling: each tree's agreement is multiplied by
    ``leaf_depth / max_depth_of_tree``, so agreements on deep (specific)
    leaves count more than shallow (broad) ones.

    Tree weighting: each tree's (possibly depth-scaled) agreement is
    multiplied by its quality weight (e.g. OOB R²).

    Returns scores of shape (n_q, n_t).
    """
    scores = agree.astype(np.float32, copy=True)

    if query_depths_batch is not None and max_depths is not None:
        depth_norm = (query_depths_batch.astype(np.float32) / max_depths)[
            :, None, :
        ]
        scores *= depth_norm

    if tree_weights is not None:
        tw = tree_weights.astype(np.float32)[None, None, :]
        scores = (scores * tw).sum(axis=2) / tw.sum()
    else:
        scores = scores.mean(axis=2)

    return scores.astype(dtype, copy=False)


def leaf_agreement_kernel(
    query_leaves: np.ndarray,
    train_leaves: np.ndarray,
    query_batch_size: int = 1024,
    train_batch_size: int | None = None,
    dtype: np.dtype = np.float32,
    tree_weights: np.ndarray | None = None,
    query_depths: np.ndarray | None = None,
    max_depths: np.ndarray | None = None,
) -> np.ndarray:
    """
    Compute query-to-train leaf-agreement scores.

    Without optional arguments the kernel value is the fraction of trees
    in which two samples share a leaf (backward-compatible default).

    Parameters
    ----------
    tree_weights : array of shape (n_trees,), optional
        Per-tree quality weights (e.g. OOB R²).
    query_depths : array of shape (n_query, n_trees), optional
        Leaf depth for each query sample in each tree.
    max_depths : array of shape (n_trees,), optional
        Max leaf depth per tree, used to normalize depth to [0, 1].
    """
    query_leaves = np.asarray(query_leaves)
    train_leaves = np.asarray(train_leaves)
    if query_leaves.ndim != 2 or train_leaves.ndim != 2:
        raise ValueError("query_leaves and train_leaves must both be 2D arrays.")
    if query_leaves.shape[1] != train_leaves.shape[1]:
        raise ValueError(
            "query_leaves and train_leaves must have the same number of trees."
        )

    n_query, n_trees = query_leaves.shape
    n_train = train_leaves.shape[0]
    train_batch_size = train_batch_size or n_train
    out = np.empty((n_query, n_train), dtype=dtype)

    use_weighting = tree_weights is not None or (
        query_depths is not None and max_depths is not None
    )

    for q0 in range(0, n_query, query_batch_size):
        q1 = min(q0 + query_batch_size, n_query)
        q_chunk = query_leaves[q0:q1]
        qd_batch = query_depths[q0:q1] if query_depths is not None else None
        for t0 in range(0, n_train, train_batch_size):
            t1 = min(t0 + train_batch_size, n_train)
            t_chunk = train_leaves[t0:t1]
            agree = q_chunk[:, None, :] == t_chunk[None, :, :]
            if use_weighting:
                out[q0:q1, t0:t1] = _weighted_agreement(
                    agree, tree_weights, qd_batch, max_depths, dtype
                )
            else:
                out[q0:q1, t0:t1] = agree.mean(axis=2).astype(dtype, copy=False)
    return out


def batch_to_train_kernel(
    model,
    X_query: np.ndarray,
    train_leaves: np.ndarray,
    query_batch_size: int = 1024,
    train_batch_size: int | None = None,
    dtype: np.dtype = np.float32,
    tree_weights: np.ndarray | None = None,
    query_depths: np.ndarray | None = None,
    max_depths: np.ndarray | None = None,
) -> np.ndarray:
    """Compute a batch-to-train kernel matrix directly from features."""
    query_leaves = compute_leaf_assignments(model, X_query)
    return leaf_agreement_kernel(
        query_leaves=query_leaves,
        train_leaves=train_leaves,
        query_batch_size=query_batch_size,
        train_batch_size=train_batch_size,
        dtype=dtype,
        tree_weights=tree_weights,
        query_depths=query_depths,
        max_depths=max_depths,
    )


def topk_leaf_agreement(
    query_leaves: np.ndarray,
    train_leaves: np.ndarray,
    k: int = 200,
    train_batch_size: int = 20000,
    exclude_self_indices: np.ndarray | None = None,
    tree_weights: np.ndarray | None = None,
    query_depths: np.ndarray | None = None,
    max_depths: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute top-k query-to-train leaf-agreement neighbors without dense
    output.

    Accepts the same optional weighting parameters as
    ``leaf_agreement_kernel``.

    Returns
    -------
    topk_scores : shape (n_query, k)
    topk_indices : shape (n_query, k)
    """
    query_leaves = np.asarray(query_leaves)
    train_leaves = np.asarray(train_leaves)
    if query_leaves.ndim != 2 or train_leaves.ndim != 2:
        raise ValueError("query_leaves and train_leaves must both be 2D arrays.")
    if query_leaves.shape[1] != train_leaves.shape[1]:
        raise ValueError(
            "query_leaves and train_leaves must have the same number of trees."
        )

    n_query = query_leaves.shape[0]
    n_train = train_leaves.shape[0]
    if n_train == 0:
        raise ValueError("train_leaves must contain at least one row.")
    k = int(max(1, min(k, n_train)))

    if exclude_self_indices is not None:
        exclude_self_indices = np.asarray(exclude_self_indices, dtype=np.int64)
        if exclude_self_indices.shape != (n_query,):
            raise ValueError("exclude_self_indices must have shape (n_query,).")

    use_weighting = tree_weights is not None or (
        query_depths is not None and max_depths is not None
    )

    best_scores = np.full((n_query, k), -np.inf, dtype=np.float32)
    best_indices = np.full((n_query, k), -1, dtype=np.int64)

    for t0 in range(0, n_train, train_batch_size):
        t1 = min(t0 + train_batch_size, n_train)
        t_chunk = train_leaves[t0:t1]
        agree = query_leaves[:, None, :] == t_chunk[None, :, :]

        if use_weighting:
            chunk_scores = _weighted_agreement(
                agree, tree_weights, query_depths, max_depths, np.float32
            )
        else:
            chunk_scores = agree.mean(axis=2).astype(np.float32, copy=False)

        chunk_idx = np.arange(t0, t1, dtype=np.int64)
        chunk_indices = np.broadcast_to(chunk_idx, chunk_scores.shape)

        if exclude_self_indices is not None:
            in_chunk = (exclude_self_indices >= t0) & (exclude_self_indices < t1)
            if np.any(in_chunk):
                rows = np.where(in_chunk)[0]
                cols = exclude_self_indices[rows] - t0
                chunk_scores[rows, cols] = -np.inf

        cand_scores = np.concatenate([best_scores, chunk_scores], axis=1)
        cand_indices = np.concatenate([best_indices, chunk_indices], axis=1)

        take = min(k, cand_scores.shape[1])
        part = np.argpartition(cand_scores, kth=cand_scores.shape[1] - take, axis=1)[
            :, -take:
        ]
        row_idx = np.arange(n_query)[:, None]
        best_scores = cand_scores[row_idx, part]
        best_indices = cand_indices[row_idx, part]

        order = np.argsort(-best_scores, axis=1)
        best_scores = best_scores[row_idx, order]
        best_indices = best_indices[row_idx, order]

    return best_scores, best_indices


def save_leaf_assignments(
    path: str | Path,
    leaf_assignments: np.ndarray,
    sample_meta: pd.DataFrame | None = None,
) -> Path:
    """Write leaf assignments to parquet with optional metadata columns."""
    leaf_assignments = np.asarray(leaf_assignments)
    if leaf_assignments.ndim != 2:
        raise ValueError("leaf_assignments must be a 2D array.")

    leaf_cols = {
        f"tree_{i}_leaf": leaf_assignments[:, i]
        for i in range(leaf_assignments.shape[1])
    }
    leaf_df = pd.DataFrame(leaf_cols)
    if sample_meta is not None:
        sample_meta = sample_meta.reset_index(drop=True).copy()
        if len(sample_meta) != len(leaf_df):
            raise ValueError("sample_meta row count must match leaf_assignments rows.")
        out_df = pd.concat([sample_meta, leaf_df], axis=1)
    else:
        out_df = leaf_df

    out_path = Path(path)
    out_df.to_parquet(out_path, index=False)
    return out_path
