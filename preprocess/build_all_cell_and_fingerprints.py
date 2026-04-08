#!/usr/bin/env python3
"""
Build all three cell_features_selected variants (variance, model, l1000_union) and
all three fingerprint variants (morgan, cdk, morgan_cdk).

- Cell features: written to preprocess/ (cell_features_selected_<method>.parquet/.csv).
- Fingerprints: written to data/processed/ (drug_fingerprints_<method>.parquet/.csv).

Requires: data/processed/cell_features.csv, data/processed/pairs.csv for gene selection;
          data/CTRPv2/v21.meta.per_compound.txt for fingerprints.

Usage:
  python preprocess/build_all_cell_and_fingerprints.py
  python preprocess/build_all_cell_and_fingerprints.py --base-dir /path/to/project
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build 3 cell feature sets (preprocess/) and 3 fingerprint sets (data/processed/)."
    )
    parser.add_argument("--base-dir", default=".", help="Project base directory.")
    parser.add_argument("--top-n", type=int, default=1000, help="Target number of genes for cell features.")
    parser.add_argument("--skip-cell", action="store_true", help="Skip cell feature selection.")
    parser.add_argument("--skip-fingerprints", action="store_true", help="Skip fingerprint building.")
    args = parser.parse_args()

    base = Path(args.base_dir).resolve()
    preprocess_dir = base / "preprocess"
    data_processed = base / "data" / "processed"
    preprocess_dir.mkdir(parents=True, exist_ok=True)
    data_processed.mkdir(parents=True, exist_ok=True)

    script_dir = Path(__file__).resolve().parent

    # --- 1. Cell features: variance, model, l1000_union -> preprocess/ ---
    if not args.skip_cell:
        cell_features_src = data_processed / "cell_features.csv"
        cell_features_parquet = data_processed / "cell_features.parquet"
        if not cell_features_src.exists() and cell_features_parquet.exists():
            cell_features_src = cell_features_parquet
        if not cell_features_src.exists():
            print("Warning: cell_features.csv/parquet not found in data/processed. Skipping cell feature selection.", file=sys.stderr)
        else:
            for method, suffix in [
                ("variance", "variance"),
                ("model", "model"),
                ("l1000_union", "l1000_union"),
            ]:
                cmd = [
                    sys.executable,
                    str(script_dir / "gene_selection.py"),
                    "--base-dir", str(base),
                    "--cell-features", str(cell_features_src.relative_to(base)),
                    "--pairs", "data/processed/pairs.csv",
                    "--out-dir", "preprocess",
                    "--method", method,
                    "--out-suffix", suffix,
                    "--top-n", str(args.top_n),
                ]
                print(f"Running: {' '.join(cmd)}")
                r = subprocess.run(cmd, cwd=str(base))
                if r.returncode != 0:
                    sys.exit(r.returncode)
            print("Cell feature selection (variance, model, l1000_union) done -> preprocess/")
    else:
        print("Skipping cell feature selection.")

    # --- 2. Fingerprints: morgan, cdk, morgan_cdk -> data/processed/ ---
    if not args.skip_fingerprints:
        for method in ["morgan", "cdk", "morgan_cdk"]:
            cmd = [
                sys.executable,
                str(script_dir / "molecular_featurization.py"),
                "--base-dir", str(base),
                "--compound-meta", "data/CTRPv2/v21.meta.per_compound.txt",
                "--out-dir", "data/processed",
                "--method", method,
            ]
            print(f"Running: {' '.join(cmd)}")
            r = subprocess.run(cmd, cwd=str(base))
            if r.returncode != 0:
                sys.exit(r.returncode)
        print("Fingerprints (morgan, cdk, morgan_cdk) done -> data/processed/")
    else:
        print("Skipping fingerprint building.")

    print("All done.")


if __name__ == "__main__":
    main()
