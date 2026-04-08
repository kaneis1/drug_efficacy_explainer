#!/usr/bin/env python3
"""
Build training tables for CTRP + DepMap integration.

Outputs:
  - pairs.parquet
  - cell_features.parquet
  - drug_fingerprints.parquet
  - schema.md
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path

import pandas as pd


def norm_name(value: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", (value or "").strip().upper())


def build_pairs(auc_path: Path) -> tuple[pd.DataFrame, dict[str, int]]:
    auc = pd.read_csv(
        auc_path,
        sep="\t",
        usecols=["experiment_id", "area_under_curve", "master_cpd_id", "master_ccl_id"],
    )
    auc = auc.rename(columns={"area_under_curve": "y"}).dropna(subset=["y"])
    auc["master_ccl_id"] = pd.to_numeric(auc["master_ccl_id"], errors="coerce")
    auc["master_cpd_id"] = pd.to_numeric(auc["master_cpd_id"], errors="coerce")
    auc["y"] = pd.to_numeric(auc["y"], errors="coerce")
    auc = auc.dropna(subset=["master_ccl_id", "master_cpd_id", "y"])

    grouped = (
        auc.groupby(["master_ccl_id", "master_cpd_id"], as_index=False)
        .agg(y=("y", "mean"), n_experiments=("experiment_id", "nunique"))
        .astype({"master_ccl_id": "int64", "master_cpd_id": "int64"})
    )
    stats = {
        "auc_rows_in": int(len(auc)),
        "pairs_rows_out": int(len(grouped)),
    }
    return grouped, stats


def build_cell_to_model_map(cell_meta_path: Path, model_path: Path) -> pd.DataFrame:
    cell_meta = pd.read_csv(
        cell_meta_path,
        sep="\t",
        usecols=["master_ccl_id", "ccl_name"],
        dtype={"master_ccl_id": "int64", "ccl_name": "string"},
    )
    model = pd.read_csv(
        model_path,
        usecols=["ModelID", "CellLineName", "StrippedCellLineName"],
        dtype="string",
    )

    stripped_map: dict[str, list[str]] = {}
    cellline_map: dict[str, list[str]] = {}
    for _, row in model.iterrows():
        mid = row["ModelID"]
        s = norm_name(row["StrippedCellLineName"] or "")
        c = norm_name(row["CellLineName"] or "")
        if s:
            stripped_map.setdefault(s, []).append(mid)
        if c:
            cellline_map.setdefault(c, []).append(mid)

    def pick_model(ccl_name: str) -> str | None:
        key = norm_name(ccl_name)
        s_hits = sorted(set(stripped_map.get(key, [])))
        if len(s_hits) == 1:
            return s_hits[0]
        c_hits = sorted(set(cellline_map.get(key, [])))
        if len(c_hits) == 1:
            return c_hits[0]
        return None

    mapped = cell_meta.copy()
    mapped["ModelID"] = mapped["ccl_name"].map(pick_model)
    mapped = mapped.dropna(subset=["ModelID"])
    return mapped


def build_cell_features(
    expr_path: Path, cell_model_map: pd.DataFrame
) -> tuple[pd.DataFrame, dict[str, int]]:
    expr = pd.read_csv(expr_path, dtype="string")
    if "IsDefaultEntryForModel" in expr.columns:
        expr = expr[expr["IsDefaultEntryForModel"].str.upper() == "YES"]
    expr = expr.drop_duplicates(subset=["ModelID"], keep="first")

    keep_model_ids = set(cell_model_map["ModelID"].astype(str))
    expr = expr[expr["ModelID"].isin(keep_model_ids)].copy()

    drop_cols = {
        "",
        "Unnamed: 0",
        "SequencingID",
        "ModelID",
        "IsDefaultEntryForModel",
        "ModelConditionID",
        "IsDefaultEntryForMC",
    }
    feature_cols = [c for c in expr.columns if c not in drop_cols]
    for col in feature_cols:
        expr[col] = pd.to_numeric(expr[col], errors="coerce")

    merged = cell_model_map.merge(expr, on="ModelID", how="inner")
    out = merged[["master_ccl_id", "ModelID", *feature_cols]].copy()
    out = out.drop_duplicates(subset=["master_ccl_id"], keep="first")

    stats = {
        "cell_ids_with_model_map": int(cell_model_map["master_ccl_id"].nunique()),
        "cell_feature_rows_out": int(len(out)),
        "cell_feature_dims": int(len(feature_cols)),
    }
    return out, stats


def morgan_or_fallback_bits(smiles: str, n_bits: int, radius: int) -> list[int] | None:
    try:
        from rdkit import Chem
        from rdkit.Chem import AllChem

        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        bitvect = AllChem.GetMorganFingerprintAsBitVect(mol, radius=radius, nBits=n_bits)
        return list(bitvect)
    except Exception:
        if not smiles or not smiles.strip():
            return None
        bits = [0] * n_bits
        s = smiles.strip()
        # Simple deterministic fallback: hashed character 3-grams.
        grams = {s[i : i + 3] for i in range(max(1, len(s) - 2))}
        for g in grams:
            h = int(hashlib.sha256(g.encode("utf-8")).hexdigest(), 16)
            bits[h % n_bits] = 1
        return bits


def build_drug_fingerprints(
    compound_meta_path: Path, n_bits: int = 1024, radius: int = 2
) -> tuple[pd.DataFrame, dict[str, int | str]]:
    cpd = pd.read_csv(
        compound_meta_path,
        sep="\t",
        usecols=["master_cpd_id", "cpd_smiles"],
        dtype={"master_cpd_id": "int64", "cpd_smiles": "string"},
    )
    cpd = cpd.dropna(subset=["cpd_smiles"]).copy()
    cpd["cpd_smiles"] = cpd["cpd_smiles"].str.strip()
    cpd = cpd[cpd["cpd_smiles"] != ""]

    fps = []
    valid_ids = []
    for _, row in cpd.iterrows():
        bits = morgan_or_fallback_bits(str(row["cpd_smiles"]), n_bits=n_bits, radius=radius)
        if bits is None:
            continue
        valid_ids.append(int(row["master_cpd_id"]))
        fps.append(bits)

    fp_cols = [f"fp_{i:04d}" for i in range(n_bits)]
    fp_df = pd.DataFrame(fps, columns=fp_cols)
    out = pd.concat(
        [pd.DataFrame({"master_cpd_id": valid_ids}, dtype="int64"), fp_df.astype("uint8")],
        axis=1,
    )

    method = "morgan_rdkit_if_available_else_hashed_3gram_fallback"
    stats = {
        "drug_rows_out": int(len(out)),
        "drug_fp_bits": int(n_bits),
        "drug_fp_method": method,
    }
    return out, stats


def write_schema_md(
    path: Path,
    pairs_stats: dict[str, int],
    cell_stats: dict[str, int],
    drug_stats: dict[str, int | str],
) -> None:
    content = f"""# Schema

## Data Sources
- `data/CTRPv2/v21.data.auc_sensitivities.txt`
- `data/CTRPv2/v21.meta.per_cell_line.txt`
- `data/CTRPv2/v21.meta.per_compound.txt`
- `data/DepMap/Model.csv`
- `data/DepMap/OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv`

## Join Keys
- Label pairs: `master_ccl_id`, `master_cpd_id`
- Cell mapping:
  - `v21.meta.per_cell_line.txt.master_ccl_id`
  - -> `v21.meta.per_cell_line.txt.ccl_name`
  - -> `Model.csv.StrippedCellLineName` (normalized exact, preferred)
  - fallback -> `Model.csv.CellLineName` (normalized exact)
  - -> `Model.csv.ModelID`
  - -> `OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv.ModelID`
- Drug mapping:
  - `v21.meta.per_compound.txt.master_cpd_id`, `cpd_smiles`

## Output Shapes
- `pairs.parquet`: {pairs_stats["pairs_rows_out"]} rows
- `cell_features.parquet`: {cell_stats["cell_feature_rows_out"]} rows x {cell_stats["cell_feature_dims"]} features (+ ids)
- `drug_fingerprints.parquet`: {drug_stats["drug_rows_out"]} rows x {drug_stats["drug_fp_bits"]} bits (+ id)

## Feature Definitions
- Cell features: DepMap expression features (gene columns), default entries only (`IsDefaultEntryForModel == "Yes"`), metadata columns removed.
- Drug features: fingerprint bits from `cpd_smiles` using method:
  - `{drug_stats["drug_fp_method"]}`

## Label Definition
- `y`: `area_under_curve` from CTRP AUC table.

## Filtering and Aggregation Rules
- Labels:
  - drop rows with missing `area_under_curve`
  - aggregate repeated `(master_ccl_id, master_cpd_id)` by mean `area_under_curve`
  - keep `n_experiments` as count of unique `experiment_id`
- Cells:
  - keep matched cell lines with mapped `ModelID`
  - keep default expression entries only
- Drugs:
  - drop missing/empty SMILES
  - drop invalid SMILES when parser cannot build fingerprint
"""
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build training tables as parquet files.")
    parser.add_argument(
        "--base-dir",
        default=".",
        help="Project root containing data/ and preprocess/ (default: current directory).",
    )
    parser.add_argument(
        "--out-dir",
        default="data/processed",
        help="Output directory for generated files (default: data/processed).",
    )
    parser.add_argument("--fp-bits", type=int, default=1024, help="Fingerprint bits.")
    parser.add_argument("--fp-radius", type=int, default=2, help="Morgan radius.")
    args = parser.parse_args()

    base = Path(args.base_dir).resolve()
    out_dir = (base / args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    auc_path = base / "data/CTRPv2/v21.data.auc_sensitivities.txt"
    cell_meta_path = base / "data/CTRPv2/v21.meta.per_cell_line.txt"
    compound_meta_path = base / "data/CTRPv2/v21.meta.per_compound.txt"
    model_path = base / "data/DepMap/Model.csv"
    expr_path = base / "data/DepMap/OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv"

    pairs_df, pairs_stats = build_pairs(auc_path)
    pairs_out = out_dir / "pairs.parquet"
    pairs_df.to_parquet(pairs_out, index=False)

    cell_model_map = build_cell_to_model_map(cell_meta_path, model_path)
    cell_df, cell_stats = build_cell_features(expr_path, cell_model_map)
    cell_out = out_dir / "cell_features.parquet"
    cell_df.to_parquet(cell_out, index=False)

    drug_df, drug_stats = build_drug_fingerprints(
        compound_meta_path, n_bits=args.fp_bits, radius=args.fp_radius
    )
    drug_out = out_dir / "drug_fingerprints.parquet"
    drug_df.to_parquet(drug_out, index=False)

    schema_out = out_dir / "schema.md"
    write_schema_md(schema_out, pairs_stats, cell_stats, drug_stats)

    print("Wrote files:")
    print(f"  - {pairs_out}")
    print(f"  - {cell_out}")
    print(f"  - {drug_out}")
    print(f"  - {schema_out}")
    print("Shapes:")
    print(f"  pairs: {pairs_df.shape}")
    print(f"  cell_features: {cell_df.shape}")
    print(f"  drug_fingerprints: {drug_df.shape}")


if __name__ == "__main__":
    main()
