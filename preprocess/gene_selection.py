#!/usr/bin/env python3
"""
Gene selection (~1,000-1,500 genes) for cell features.

- Preprocessing: drop duplicated genes, near-zero variance, low-quality
- Variance-based: top N genes by variance
- Model-based: top N by RF feature importance (optional)
- LINCS L1000 overlap: union of L1000 landmark genes + top variance/model genes

Usage:
  python preprocess/gene_selection.py --method variance --top-n 1000
  python preprocess/gene_selection.py --method l1000_union --top-n 1000
  python preprocess/gene_selection.py --method variance --out-dir preprocess --out-suffix variance  # -> preprocess/cell_features_selected_variance.parquet
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd


def parse_gene_col(col: str) -> str | None:
    """Extract gene symbol from 'GENE (ENTREZ)' or 'GENE' format."""
    s = (col or "").strip()
    if not s:
        return None
    m = re.match(r"^([A-Za-z0-9\-\.]+)\s*\(\d+\)\s*$", s)
    if m:
        return m.group(1).upper()
    if re.match(r"^ENSG\d+$", s):
        return None
    return s.upper()


def get_gene_symbols_from_columns(cols: list[str]) -> dict[str, str]:
    """Map column name -> gene symbol; handle duplicates (keep first)."""
    out = {}
    seen_symbols = set()
    for c in cols:
        sym = parse_gene_col(c)
        if sym and sym not in seen_symbols:
            out[c] = sym
            seen_symbols.add(sym)
    return out


def load_l1000_genes(path: Path | None) -> set[str]:
    """Load LINCS L1000 landmark gene symbols. Returns empty if file missing."""
    if path is None or not path.exists():
        return set()
    genes = set()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            tok = line.split("\t")
            if tok:
                genes.add(tok[0].upper())
    return genes


def select_genes_variance(
    X: pd.DataFrame, cols: list[str], top_n: int, min_var: float = 1e-10
) -> list[str]:
    """Variance-based: top N genes by variance. Drop near-zero first."""
    var = X[cols].var()
    valid = var[var >= min_var].sort_values(ascending=False)
    return valid.head(top_n).index.tolist()


def select_genes_model(
    X: pd.DataFrame,
    y: pd.Series,
    cols: list[str],
    top_n: int,
    n_estimators: int = 50,
    max_depth: int = 8,
    random_state: int = 42,
) -> list[str]:
    """Model-based: top N genes by RF feature importance."""
    from sklearn.ensemble import RandomForestRegressor

    rf = RandomForestRegressor(
        n_estimators=n_estimators, max_depth=max_depth, random_state=random_state, n_jobs=1
    )
    rf.fit(X[cols], y)
    imp = pd.Series(rf.feature_importances_, index=cols).sort_values(ascending=False)
    return imp.head(top_n).index.tolist()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Select ~1000-1500 genes from cell expression features."
    )
    parser.add_argument(
        "--cell-features",
        default="data/processed/cell_features.csv",
        help="Path to cell_features CSV or parquet.",
    )
    parser.add_argument(
        "--pairs",
        default="data/processed/pairs.csv",
        help="Path to pairs (for model-based, needs y).",
    )
    parser.add_argument(
        "--out-dir",
        default="data/processed",
        help="Output directory.",
    )
    parser.add_argument(
        "--method",
        choices=["variance", "model", "l1000_union", "variance_then_model"],
        default="variance",
        help="Selection method.",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=1000,
        help="Target number of genes (default: 1000).",
    )
    parser.add_argument(
        "--l1000-file",
        default="data/lincs_l1000_landmark_genes.txt",
        help="LINCS L1000 gene list (one symbol per line). Optional.",
    )
    parser.add_argument(
        "--model-top",
        type=int,
        default=5000,
        help="For model-based: use top N by variance first (default: 5000).",
    )
    parser.add_argument(
        "--out-suffix",
        default="",
        help="Suffix for output files (e.g. 'variance' -> cell_features_selected_variance.parquet).",
    )
    parser.add_argument("--base-dir", default=".", help="Project base directory.")
    args = parser.parse_args()

    base = Path(args.base_dir).resolve()
    cell_path = base / args.cell_features
    pairs_path = base / args.pairs
    out_dir = base / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    l1000_path = base / args.l1000_file

    print("Loading cell features...")
    if str(cell_path).endswith(".parquet"):
        cell = pd.read_parquet(cell_path)
    else:
        cell = pd.read_csv(cell_path)
    id_cols = ["master_ccl_id", "ModelID"]
    all_gene_cols = [c for c in cell.columns if c not in id_cols]
    col_to_symbol = get_gene_symbols_from_columns(all_gene_cols)

    # Deduplicate: if multiple columns map to same symbol, keep first
    symbol_to_col = {}
    for c in all_gene_cols:
        sym = col_to_symbol.get(c)
        if sym and sym not in symbol_to_col:
            symbol_to_col[sym] = c
    unique_cols = list(symbol_to_col.values())
    if len(unique_cols) < len(all_gene_cols):
        print(f"Removed {len(all_gene_cols) - len(unique_cols)} duplicate gene mappings")

    # Near-zero variance
    var = cell[unique_cols].var()
    min_var = 1e-10
    good_cols = var[var >= min_var].index.tolist()
    if len(good_cols) < len(unique_cols):
        print(f"Removed {len(unique_cols) - len(good_cols)} near-zero variance genes")

    if args.method == "variance":
        selected = select_genes_variance(cell, good_cols, args.top_n)
    elif args.method == "model":
        print("Loading pairs for y...")
        pairs = pd.read_csv(pairs_path) if str(pairs_path).endswith(".csv") else pd.read_parquet(pairs_path)
        merged = cell.merge(
            pairs[["master_ccl_id", "master_cpd_id", "y"]],
            on="master_ccl_id",
            how="inner",
        )
        merged = merged.drop_duplicates(subset=["master_ccl_id", "master_cpd_id"], keep="first")
        y = merged["y"]
        X = merged[good_cols]
        prelim = select_genes_variance(cell, good_cols, min(args.model_top, len(good_cols)))
        selected = select_genes_model(X, y, prelim, args.top_n)
    elif args.method == "l1000_union":
        l1000 = load_l1000_genes(l1000_path)
        var_ranked = select_genes_variance(cell, good_cols, len(good_cols))
        var_symbols = {col_to_symbol.get(c, c) for c in var_ranked[: args.top_n]}
        overlap = l1000 & {col_to_symbol.get(c, c) for c in good_cols}
        selected = []
        for sym in l1000:
            if sym in symbol_to_col and symbol_to_col[sym] in good_cols:
                selected.append(symbol_to_col[sym])
        for c in var_ranked:
            if c not in selected:
                selected.append(c)
            if len(selected) >= args.top_n:
                break
        selected = selected[: args.top_n]
        print(f"LINCS L1000 in file: {len(l1000)}; in our data: {len(overlap)}; selected: {len(selected)}")
    else:  # variance_then_model
        prelim = select_genes_variance(cell, good_cols, min(args.model_top, len(good_cols)))
        print("Loading pairs for model-based refinement...")
        pairs = pd.read_csv(pairs_path) if str(pairs_path).endswith(".csv") else pd.read_parquet(pairs_path)
        merged = cell.merge(
            pairs[["master_ccl_id", "master_cpd_id", "y"]],
            on="master_ccl_id",
            how="inner",
        )
        merged = merged.drop_duplicates(subset=["master_ccl_id", "master_cpd_id"], keep="first")
        y = merged["y"]
        selected = select_genes_model(merged, y, prelim, args.top_n)

    out_cols = [c for c in cell.columns if c in id_cols or c in selected]
    out_df = cell[out_cols].copy()
    name_base = "cell_features_selected" + (f"_{args.out_suffix}" if args.out_suffix else "")
    out_parquet = out_dir / f"{name_base}.parquet"
    out_csv = out_dir / f"{name_base}.csv"
    genes_out = out_dir / f"selected_genes{'_' + args.out_suffix if args.out_suffix else ''}.txt"
    out_df.to_parquet(out_parquet, index=False)
    out_df.to_csv(out_csv, index=False)
    genes_out.write_text("\n".join(sorted(selected)), encoding="utf-8")
    print(f"Selected {len(selected)} genes")
    print(f"Wrote: {out_parquet}, {out_csv}, {genes_out}")


if __name__ == "__main__":
    main()
