"""
Shared data loading for RF tuning and fingerprint scripts.
Loads pairs + cell features + drug fingerprints, merges, returns X, y and column names.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def load_merged(
    data_dir: str | Path,
    pairs_file: str = "pairs.csv",
    cell_features_file: str = "cell_features_selected.csv",
    drug_fingerprints_file: str = "drug_fingerprints.csv",
    return_metadata: bool = False,
) -> tuple[np.ndarray, np.ndarray, list[str], list[str], list[str]] | tuple[
    np.ndarray, np.ndarray, list[str], list[str], list[str], pd.DataFrame
]:
    """
    Load pairs, cell features, drug fingerprints; merge and return arrays and column names.

    Returns:
        X: (n_samples, n_features) float64, non-finite values replaced by column median
        y: (n_samples,) float64
        feat_cols: all feature column names (cell + drug)
        cell_feat_cols: cell feature column names
        drug_feat_cols: drug fingerprint column names
        sample_meta: per-row metadata aligned to X/y (only when return_metadata=True)
    """
    base = Path(data_dir).resolve()
    pairs_path = base / pairs_file
    cell_path = base / cell_features_file
    drug_path = base / drug_fingerprints_file

    for p in [pairs_path, cell_path, drug_path]:
        if not p.exists():
            raise FileNotFoundError(f"Not found: {p}")

    def _read(path: Path) -> pd.DataFrame:
        if str(path).endswith(".parquet"):
            return pd.read_parquet(path)
        return pd.read_csv(path)

    pairs = _read(pairs_path)
    cell = _read(cell_path)
    drug = _read(drug_path)

    cell_id_col = "master_ccl_id"
    drug_id_col = "master_cpd_id"
    cell_feat_cols = [c for c in cell.columns if c not in (cell_id_col, "ModelID")]
    drug_feat_cols = [c for c in drug.columns if c != drug_id_col]
    feat_cols = cell_feat_cols + drug_feat_cols

    merged = (
        pairs.merge(cell[[cell_id_col] + cell_feat_cols], on=cell_id_col, how="inner")
        .merge(drug[[drug_id_col] + drug_feat_cols], on=drug_id_col, how="inner")
    )
    # Use float64 to avoid overflow (float32 can produce inf for large values)
    X = np.asarray(merged[feat_cols].values, dtype=np.float64)
    y = np.asarray(merged["y"].values, dtype=np.float64)

    # Replace inf/-inf and NaN so sklearn accepts X
    if not np.isfinite(X).all():
        bad = ~np.isfinite(X)
        X = np.where(bad, np.nan, X)
        col_med = np.nanmedian(X, axis=0)
        np.putmask(col_med, ~np.isfinite(col_med), 0.0)
        for j in range(X.shape[1]):
            X[np.isnan(X[:, j]), j] = col_med[j]

    # Clip to float32 range so sklearn's internal cast (e.g. in tree code) does not overflow
    f32_max = np.finfo(np.float32).max
    f32_min = np.finfo(np.float32).min
    X = np.clip(X, f32_min, f32_max)

    if not return_metadata:
        return X, y, feat_cols, cell_feat_cols, drug_feat_cols

    preferred_meta_cols = [
        "master_ccl_id",
        "master_cpd_id",
        "ModelID",
        "cell_line",
        "cell_line_name",
        "drug",
        "drug_name",
        "cpd_name",
    ]
    meta_cols = [c for c in preferred_meta_cols if c in merged.columns]
    if not meta_cols:
        # Keep at least one column to preserve row alignment in downstream outputs.
        sample_meta = pd.DataFrame({"row_index": np.arange(len(merged), dtype=np.int64)})
    else:
        sample_meta = merged[meta_cols].reset_index(drop=True).copy()

    return X, y, feat_cols, cell_feat_cols, drug_feat_cols, sample_meta
