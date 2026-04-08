#!/usr/bin/env python3
"""
Molecular featurization for drugs: Morgan, CDK-like descriptors, or both.

- Morgan: ECFP4 (radius=2, nBits=1024/2048)
- CDK: RDKit descriptors (constitutional, topological) as CDK-like
- Morgan+CDK: concatenated feature vectors

Usage:
  python preprocess/molecular_featurization.py --method morgan
  python preprocess/molecular_featurization.py --method cdk
  python preprocess/molecular_featurization.py --method morgan_cdk
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd


def morgan_fp(smiles: str, n_bits: int = 1024, radius: int = 2) -> list[int] | None:
    """Morgan (ECFP) fingerprint. Uses RDKit if available, else hashed fallback."""
    try:
        from rdkit import Chem
        from rdkit.Chem import AllChem

        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        bitvect = AllChem.GetMorganFingerprintAsBitVect(mol, radius=radius, nBits=n_bits)
        return list(bitvect)
    except ImportError:
        return _morgan_fallback(smiles, n_bits)
    except Exception:
        return _morgan_fallback(smiles, n_bits)


def _morgan_fallback(smiles: str, n_bits: int) -> list[int] | None:
    """Fallback when RDKit unavailable: hashed 3-grams."""
    import hashlib

    if not smiles or not str(smiles).strip():
        return None
    s = str(smiles).strip()
    bits = [0] * n_bits
    for i in range(max(1, len(s) - 2)):
        g = s[i : i + 3]
        h = int(hashlib.sha256(g.encode()).hexdigest(), 16)
        bits[h % n_bits] = 1
    return bits


def cdk_descriptors(smiles: str) -> dict[str, float] | None:
    """CDK-like descriptors via RDKit (constitutional, topological)."""
    try:
        from rdkit import Chem
        from rdkit.Chem import Descriptors

        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        out = {}
        for name, func in Descriptors.descList:
            try:
                v = func(mol)
                out[name] = float(v) if not (isinstance(v, float) and np.isnan(v)) else 0.0
            except Exception:
                out[name] = 0.0
        return out
    except ImportError:
        raise ImportError("RDKit required for CDK descriptors. Install: conda install -c conda-forge rdkit")
    except Exception:
        return None


def build_morgan(
    compound_path: Path, n_bits: int = 1024, radius: int = 2
) -> tuple[pd.DataFrame, list[str]]:
    """Build Morgan-only fingerprints."""
    cpd = pd.read_csv(compound_path, sep="\t", usecols=["master_cpd_id", "cpd_smiles"], dtype={"master_cpd_id": "int64", "cpd_smiles": "string"})
    cpd = cpd.dropna(subset=["cpd_smiles"]).copy()
    cpd["cpd_smiles"] = cpd["cpd_smiles"].str.strip()
    cpd = cpd[cpd["cpd_smiles"] != ""]
    rows = []
    for _, r in cpd.iterrows():
        bits = morgan_fp(str(r["cpd_smiles"]), n_bits=n_bits, radius=radius)
        if bits is None:
            continue
        rows.append({"master_cpd_id": int(r["master_cpd_id"]), **{f"fp_{i}": b for i, b in enumerate(bits)}})
    if not rows:
        raise ValueError("No valid SMILES produced Morgan fingerprints.")
    df = pd.DataFrame(rows)
    feat_cols = [c for c in df.columns if c != "master_cpd_id"]
    return df, feat_cols


def build_cdk(compound_path: Path) -> tuple[pd.DataFrame, list[str]]:
    """Build CDK-like (RDKit) descriptors only."""
    cpd = pd.read_csv(compound_path, sep="\t", usecols=["master_cpd_id", "cpd_smiles"], dtype={"master_cpd_id": "int64", "cpd_smiles": "string"})
    cpd = cpd.dropna(subset=["cpd_smiles"]).copy()
    cpd["cpd_smiles"] = cpd["cpd_smiles"].str.strip()
    cpd = cpd[cpd["cpd_smiles"] != ""]
    rows = []
    desc_names = None
    for _, r in cpd.iterrows():
        d = cdk_descriptors(str(r["cpd_smiles"]))
        if d is None:
            continue
        if desc_names is None:
            desc_names = sorted(d.keys())
        row = {"master_cpd_id": int(r["master_cpd_id"])}
        for k in desc_names:
            row[k] = d.get(k, 0.0)
        rows.append(row)
    if not rows:
        raise ValueError("No valid SMILES produced CDK descriptors.")
    df = pd.DataFrame(rows)
    feat_cols = [c for c in df.columns if c != "master_cpd_id"]
    return df, feat_cols


def build_morgan_cdk(
    compound_path: Path, n_bits: int = 1024, radius: int = 2
) -> tuple[pd.DataFrame, list[str]]:
    """Build Morgan + CDK concatenated features."""
    m_df, m_cols = build_morgan(compound_path, n_bits=n_bits, radius=radius)
    c_df, c_cols = build_cdk(compound_path)
    merged = m_df.merge(c_df, on="master_cpd_id", how="inner")
    feat_cols = m_cols + c_cols
    return merged, feat_cols


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Molecular featurization: Morgan, CDK, or Morgan+CDK."
    )
    parser.add_argument(
        "--compound-meta",
        default="data/CTRPv2/v21.meta.per_compound.txt",
        help="Path to compound metadata with cpd_smiles.",
    )
    parser.add_argument(
        "--out-dir",
        default="data/processed",
        help="Output directory.",
    )
    parser.add_argument(
        "--method",
        choices=["morgan", "cdk", "morgan_cdk"],
        default="morgan",
        help="Featurization method.",
    )
    parser.add_argument("--n-bits", type=int, default=1024, help="Morgan fingerprint bits.")
    parser.add_argument("--radius", type=int, default=2, help="Morgan radius (ECFP4=2).")
    parser.add_argument("--base-dir", default=".", help="Project base directory.")
    args = parser.parse_args()

    base = Path(args.base_dir).resolve()
    compound_path = base / args.compound_meta
    out_dir = base / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.method == "morgan":
        df, feat_cols = build_morgan(compound_path, n_bits=args.n_bits, radius=args.radius)
        suffix = "morgan"
    elif args.method == "cdk":
        df, feat_cols = build_cdk(compound_path)
        suffix = "cdk"
    else:
        df, feat_cols = build_morgan_cdk(compound_path, n_bits=args.n_bits, radius=args.radius)
        suffix = "morgan_cdk"

    out_parquet = out_dir / f"drug_fingerprints_{suffix}.parquet"
    out_csv = out_dir / f"drug_fingerprints_{suffix}.csv"
    df.to_parquet(out_parquet, index=False)
    df.to_csv(out_csv, index=False)
    print(f"Method: {args.method}, features: {len(feat_cols)}, compounds: {len(df)}")
    print(f"Wrote: {out_parquet}, {out_csv}")


if __name__ == "__main__":
    main()
