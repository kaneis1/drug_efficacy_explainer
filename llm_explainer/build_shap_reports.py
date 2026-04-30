#!/usr/bin/env python3
"""
Build SHAP-grounded report inputs for the local LLM explainer.

This script turns the full Random Forest TreeSHAP export into:
1. a structured JSONL bundle for `llm_explainer/generate_reports.py`
2. a human-readable Markdown summary similar to `results/dem/sample_reports.md`

The bundle is grounded in:
- per-sample TreeSHAP values from `results/tuning/shap_values.parquet`
- CTRPv2 drug and cell-line metadata
- local cohort statistics from `data/processed/pairs.csv`
- local feature context from selected cell-expression and fingerprint matrices
- local "knowledge support" from per-drug RF predictability and recurring genes
"""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any

import pandas as pd


FP_RE = re.compile(r"^fp_(\d+)$")
GENE_RE = re.compile(r"^(.+?)\s*\((\d+)\)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build SHAP-grounded report inputs for the local LLM explainer."
    )
    parser.add_argument(
        "--shap-values",
        default="results/tuning/shap_values.parquet",
        help="Full SHAP parquet written by train/top_fingerprints.py.",
    )
    parser.add_argument(
        "--pairs",
        default="data/processed/pairs.csv",
        help="Merged drug-cell response table used for cohort context.",
    )
    parser.add_argument(
        "--target-label",
        default="AUC",
        help="Human-readable target label used throughout the narrative "
             "(e.g. 'AUC' for area-under-curve or 'log10(IC50)' in log10 µM).",
    )
    parser.add_argument(
        "--interpretation-scale",
        type=float,
        default=None,
        help="Scale factor for the `interpret_case` thresholds. "
             "If unset, defaults to 1.0 for AUC and to std(y) / 2.6 for any other "
             "target (2.6 is roughly the AUC std in CTRPv2.1).",
    )
    parser.add_argument(
        "--compound-meta",
        default="data/CTRPv2/v21.meta.per_compound.txt",
        help="CTRP compound metadata TSV.",
    )
    parser.add_argument(
        "--cell-meta",
        default="data/CTRPv2/v21.meta.per_cell_line.txt",
        help="CTRP cell-line metadata TSV.",
    )
    parser.add_argument(
        "--cell-features",
        default="data/processed/cell_features_selected_l1000_union.csv",
        help="Selected cell-expression features used by the RF model.",
    )
    parser.add_argument(
        "--per-drug-r2",
        default="results/rf_plots/per_drug_r2.csv",
        help="Per-drug cross-validated RF predictability summary.",
    )
    parser.add_argument(
        "--gene-signatures",
        default="results/rf_plots/gene_signature_counts.csv",
        help="Recurring-gene counts across predictable per-drug models.",
    )
    parser.add_argument(
        "--out-jsonl",
        default="llm_explainer/shap_sample_reports.jsonl",
        help="Structured report bundle for the LLM stage.",
    )
    parser.add_argument(
        "--out-md",
        default="llm_explainer/shap_sample_reports.md",
        help="Human-readable summary of the selected SHAP cases.",
    )
    parser.add_argument(
        "--fp-cache",
        default="llm_explainer/cache/fingerprint_bit_metadata.json",
        help="Cache file for decoded Morgan fingerprint metadata.",
    )
    parser.add_argument(
        "--num-reports",
        type=int,
        default=25,
        help="How many SHAP-grounded cases to select. Use 0 to keep all available cases.",
    )
    parser.add_argument(
        "--selection-mode",
        choices=["diverse", "top_error", "all", "from_csv"],
        default="diverse",
        help="How to choose cases from the SHAP export. Use 'from_csv' together "
             "with --selection-csv to import a pre-curated set (e.g. KNN outliers).",
    )
    parser.add_argument(
        "--selection-csv",
        default=None,
        help="CSV of pre-selected cases. Required columns: "
             "`master_ccl_id`,`master_cpd_id`. Optional: `selection_tag`, "
             "`selection_reason`, `rank`. Only used when --selection-mode=from_csv.",
    )
    parser.add_argument(
        "--knowledge-sources",
        default=None,
        help="Comma-separated list of knowledge-source paths to embed in each "
             "payload. When unset a default list pointing at the AUC pipeline is used.",
    )
    parser.add_argument(
        "--top-k-features",
        type=int,
        default=8,
        help="How many top-|SHAP| features to include per case.",
    )
    parser.add_argument(
        "--same-drug-examples",
        type=int,
        default=4,
        help="How many same-drug cohort examples to include per case.",
    )
    parser.add_argument(
        "--same-cell-examples",
        type=int,
        default=4,
        help="How many same-cell cohort examples to include per case.",
    )
    parser.add_argument(
        "--max-per-drug",
        type=int,
        default=2,
        help="Selection diversity cap per drug.",
    )
    parser.add_argument(
        "--max-per-cell",
        type=int,
        default=2,
        help="Selection diversity cap per cell line.",
    )
    parser.add_argument(
        "--max-per-tissue",
        type=int,
        default=4,
        help="Selection diversity cap per tissue.",
    )
    parser.add_argument(
        "--morgan-bits",
        type=int,
        default=1024,
        help="Morgan fingerprint length used for the RF features.",
    )
    parser.add_argument(
        "--morgan-radius",
        type=int,
        default=2,
        help="Morgan fingerprint radius used for bit decoding.",
    )
    return parser.parse_args()


def _safe_str(val: Any, default: str = "") -> str:
    if pd.isna(val):
        return default
    return str(val).strip()


def _load_compound_meta(path: Path) -> dict[int, dict[str, Any]]:
    df = pd.read_csv(path, sep="\t")
    lookup: dict[int, dict[str, Any]] = {}
    for _, row in df.iterrows():
        cpd_id = int(row["master_cpd_id"])
        lookup[cpd_id] = {
            "cpd_name": _safe_str(row.get("cpd_name"), f"cpd_{cpd_id}"),
            "gene_target": _safe_str(row.get("gene_symbol_of_protein_target")),
            "mechanism": _safe_str(row.get("target_or_activity_of_compound")),
            "smiles": _safe_str(row.get("cpd_smiles")),
        }
    return lookup


def _load_cell_meta(path: Path) -> dict[int, dict[str, Any]]:
    df = pd.read_csv(path, sep="\t")
    lookup: dict[int, dict[str, Any]] = {}
    for _, row in df.iterrows():
        ccl_id = int(row["master_ccl_id"])
        lookup[ccl_id] = {
            "ccl_name": _safe_str(row.get("ccl_name"), f"ccl_{ccl_id}"),
            "primary_site": _safe_str(row.get("ccle_primary_site")).replace("_", " "),
            "histology": _safe_str(row.get("ccle_primary_hist")).replace("_", " "),
            "subtype": _safe_str(row.get("ccle_hist_subtype_1")).replace("_", " "),
        }
    return lookup


def _drug_info(cpd_id: int | None, compound_meta: dict[int, dict[str, Any]]) -> dict[str, Any]:
    if cpd_id is None:
        return {"cpd_name": "unknown", "gene_target": "", "mechanism": "", "smiles": ""}
    return compound_meta.get(
        int(cpd_id),
        {"cpd_name": f"cpd_{cpd_id}", "gene_target": "", "mechanism": "", "smiles": ""},
    )


def _cell_info(ccl_id: int | None, cell_meta: dict[int, dict[str, Any]]) -> dict[str, Any]:
    if ccl_id is None:
        return {"ccl_name": "unknown", "primary_site": "", "histology": "", "subtype": ""}
    return cell_meta.get(
        int(ccl_id),
        {"ccl_name": f"ccl_{ccl_id}", "primary_site": "", "histology": "", "subtype": ""},
    )


def _build_fp_bit_descriptions(
    compound_meta: dict[int, dict[str, Any]],
    *,
    n_bits: int = 1024,
    radius: int = 2,
) -> dict[str, dict[str, Any]]:
    try:
        from rdkit import Chem
        from rdkit.Chem import AllChem
    except ImportError:
        print("Warning: RDKit not available; fingerprint SMARTS annotations will be skipped.")
        return {}

    bit_smarts: dict[int, dict[str, int]] = {}
    bit_drugs: dict[int, list[str]] = {}

    for cpd_id, info in compound_meta.items():
        smiles = info.get("smiles", "")
        if not smiles:
            continue
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            continue

        bit_info: dict[int, list[tuple[int, int]]] = {}
        AllChem.GetMorganFingerprintAsBitVect(
            mol, radius=radius, nBits=n_bits, bitInfo=bit_info
        )
        drug_name = info.get("cpd_name", f"cpd_{cpd_id}")
        for bit_idx, envs in bit_info.items():
            bit_smarts.setdefault(bit_idx, {})
            bit_drugs.setdefault(bit_idx, []).append(drug_name)
            for atom_idx, env_radius in envs:
                env = Chem.FindAtomEnvironmentOfRadiusN(mol, env_radius, atom_idx)
                if env:
                    submol = Chem.PathToSubmol(mol, env)
                    smarts = Chem.MolToSmarts(submol)
                else:
                    smarts = mol.GetAtomWithIdx(atom_idx).GetSymbol()
                bit_smarts[bit_idx][smarts] = bit_smarts[bit_idx].get(smarts, 0) + 1

    n_total = max(1, len([v for v in compound_meta.values() if v.get("smiles")]))
    result: dict[str, dict[str, Any]] = {}
    for bit_idx, smarts_counts in bit_smarts.items():
        top_smarts = max(smarts_counts, key=smarts_counts.get) if smarts_counts else ""
        drugs = bit_drugs.get(bit_idx, [])
        result[f"fp_{bit_idx:04d}"] = {
            "smarts": top_smarts,
            "example_drugs": drugs[:5],
            "n_drugs_with_bit": len(drugs),
            "pct_drugs": len(drugs) / n_total * 100.0,
        }
    return result


def load_or_build_fp_metadata(
    *,
    compound_meta: dict[int, dict[str, Any]],
    cache_path: Path,
    n_bits: int,
    radius: int,
) -> dict[str, dict[str, Any]]:
    if cache_path.exists():
        with cache_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    fp_info = _build_fp_bit_descriptions(compound_meta, n_bits=n_bits, radius=radius)
    cache_path.write_text(json.dumps(fp_info, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    return fp_info


def normalize_fp_name(feature: str) -> str:
    match = FP_RE.match(str(feature))
    if not match:
        return str(feature)
    return f"fp_{int(match.group(1)):04d}"


def parse_gene_feature(feature: str) -> tuple[str, str]:
    match = GENE_RE.match(str(feature))
    if not match:
        return str(feature), ""
    return match.group(1).strip(), match.group(2).strip()


def split_targets(value: str) -> set[str]:
    if not value:
        return set()
    return {token.strip() for token in value.split(";") if token.strip()}


def load_gene_stats(path: Path) -> dict[str, dict[str, float]]:
    df = pd.read_csv(path)
    id_cols = {"master_ccl_id", "ModelID"}
    gene_cols = [col for col in df.columns if col not in id_cols]
    means = df[gene_cols].mean()
    stds = df[gene_cols].std(ddof=0).fillna(0.0)
    return {
        col: {"mean": float(means[col]), "std": float(stds[col])}
        for col in gene_cols
    }


def load_gene_support(path: Path) -> tuple[dict[str, int], dict[str, int]]:
    df = pd.read_csv(path, index_col=0)
    if "n_drugs" not in df.columns:
        raise ValueError(f"{path} must contain an n_drugs column.")

    exact: dict[str, int] = {}
    symbol: dict[str, int] = {}
    for feature_name, value in df["n_drugs"].items():
        feature_name = str(feature_name)
        count = int(value)
        exact[feature_name] = count
        gene_symbol, _ = parse_gene_feature(feature_name)
        symbol[gene_symbol] = max(symbol.get(gene_symbol, 0), count)
    return exact, symbol


def quantile10(series: pd.Series) -> float:
    return float(series.quantile(0.10))


def quantile90(series: pd.Series) -> float:
    return float(series.quantile(0.90))


def build_group_stats(
    pairs: pd.DataFrame,
    group_col: str,
) -> pd.DataFrame:
    return (
        pairs.groupby(group_col)["y"]
        .agg(n="size", mean="mean", q10=quantile10, q50="median", q90=quantile90)
        .reset_index()
    )


def percentile_leq(series: pd.Series, value: float) -> float:
    if series.empty:
        return float("nan")
    return float((series <= value).mean() * 100.0)


def greedy_take(
    candidates: pd.DataFrame,
    *,
    needed: int,
    selected_sample_ids: set[int],
    counts_by_drug: Counter[int],
    counts_by_cell: Counter[int],
    counts_by_tissue: Counter[str],
    max_per_drug: int,
    max_per_cell: int,
    max_per_tissue: int,
    enforce_drug: bool = True,
    enforce_cell: bool = True,
    enforce_tissue: bool = True,
) -> list[int]:
    chosen: list[int] = []
    for _, row in candidates.iterrows():
        sample_idx = int(row["sample_idx"])
        if sample_idx in selected_sample_ids:
            continue
        cpd_id = int(row["master_cpd_id"])
        ccl_id = int(row["master_ccl_id"])
        tissue = _safe_str(row.get("tissue"), "unknown") or "unknown"
        if enforce_drug and counts_by_drug[cpd_id] >= max_per_drug:
            continue
        if enforce_cell and counts_by_cell[ccl_id] >= max_per_cell:
            continue
        if enforce_tissue and counts_by_tissue[tissue] >= max_per_tissue:
            continue
        chosen.append(sample_idx)
        selected_sample_ids.add(sample_idx)
        counts_by_drug[cpd_id] += 1
        counts_by_cell[ccl_id] += 1
        counts_by_tissue[tissue] += 1
        if len(chosen) >= needed:
            break
    return chosen


def select_diverse_cases(
    sample_summary: pd.DataFrame,
    *,
    num_reports: int,
    max_per_drug: int,
    max_per_cell: int,
    max_per_tissue: int,
) -> list[int]:
    sample_summary = sample_summary.sort_values("abs_error", ascending=False).reset_index(drop=True)
    more_resistant = sample_summary[sample_summary["prediction_error"] > 0].copy()
    more_sensitive = sample_summary[sample_summary["prediction_error"] < 0].copy()

    selected_ids: set[int] = set()
    counts_by_drug: Counter[int] = Counter()
    counts_by_cell: Counter[int] = Counter()
    counts_by_tissue: Counter[str] = Counter()

    resistant_target = math.ceil(num_reports / 2)
    sensitive_target = num_reports - resistant_target

    resistant_selected = greedy_take(
        more_resistant,
        needed=resistant_target,
        selected_sample_ids=selected_ids,
        counts_by_drug=counts_by_drug,
        counts_by_cell=counts_by_cell,
        counts_by_tissue=counts_by_tissue,
        max_per_drug=max_per_drug,
        max_per_cell=max_per_cell,
        max_per_tissue=max_per_tissue,
    )
    sensitive_selected = greedy_take(
        more_sensitive,
        needed=sensitive_target,
        selected_sample_ids=selected_ids,
        counts_by_drug=counts_by_drug,
        counts_by_cell=counts_by_cell,
        counts_by_tissue=counts_by_tissue,
        max_per_drug=max_per_drug,
        max_per_cell=max_per_cell,
        max_per_tissue=max_per_tissue,
    )

    ordered: list[int] = []
    max_len = max(len(resistant_selected), len(sensitive_selected))
    for idx in range(max_len):
        if idx < len(resistant_selected):
            ordered.append(resistant_selected[idx])
        if idx < len(sensitive_selected):
            ordered.append(sensitive_selected[idx])

    remaining_needed = num_reports - len(ordered)
    if remaining_needed > 0:
        remaining = sample_summary[~sample_summary["sample_idx"].isin(selected_ids)]
        for flags in (
            (True, True, False),
            (True, False, False),
            (False, False, False),
        ):
            fill = greedy_take(
                remaining,
                needed=remaining_needed,
                selected_sample_ids=selected_ids,
                counts_by_drug=counts_by_drug,
                counts_by_cell=counts_by_cell,
                counts_by_tissue=counts_by_tissue,
                max_per_drug=max_per_drug,
                max_per_cell=max_per_cell,
                max_per_tissue=max_per_tissue,
                enforce_drug=flags[0],
                enforce_cell=flags[1],
                enforce_tissue=flags[2],
            )
            ordered.extend(fill)
            remaining_needed = num_reports - len(ordered)
            if remaining_needed <= 0:
                break

    return ordered[:num_reports]


def select_case_ids(
    sample_summary: pd.DataFrame,
    *,
    selection_mode: str,
    num_reports: int,
    max_per_drug: int,
    max_per_cell: int,
    max_per_tissue: int,
    selection_csv: str | Path | None = None,
) -> tuple[list[int], dict[int, dict[str, Any]]]:
    """
    Return (sample_idx list, per-sample override dict).

    The override dict may contain per-case `selection_tag` / `selection_reason`
    values that bypass the default `selection_reason_text` narrative.
    """
    overrides: dict[int, dict[str, Any]] = {}

    if selection_mode == "from_csv":
        if selection_csv is None:
            raise ValueError("--selection-mode=from_csv requires --selection-csv")
        sel = pd.read_csv(selection_csv)
        needed_cols = {"master_ccl_id", "master_cpd_id"}
        missing = needed_cols - set(sel.columns)
        if missing:
            raise ValueError(
                f"--selection-csv {selection_csv} is missing columns: {sorted(missing)}"
            )
        sel["master_ccl_id"] = sel["master_ccl_id"].astype(int)
        sel["master_cpd_id"] = sel["master_cpd_id"].astype(int)
        merged = sel.merge(
            sample_summary[["sample_idx", "master_ccl_id", "master_cpd_id"]],
            on=["master_ccl_id", "master_cpd_id"],
            how="left",
        )
        missing_rows = merged[merged["sample_idx"].isna()]
        if len(missing_rows):
            preview = missing_rows[["master_ccl_id", "master_cpd_id"]].head(5).to_dict("records")
            raise ValueError(
                f"{len(missing_rows)} rows in --selection-csv had no matching "
                f"sample in shap_values.parquet; e.g. {preview}"
            )
        if "rank" in merged.columns:
            merged = merged.sort_values("rank", kind="stable")
        sample_ids: list[int] = []
        for _, row in merged.iterrows():
            sid = int(row["sample_idx"])
            sample_ids.append(sid)
            rec: dict[str, Any] = {}
            if "selection_tag" in merged.columns and pd.notna(row.get("selection_tag")):
                rec["selection_tag"] = str(row["selection_tag"])
            if "selection_reason" in merged.columns and pd.notna(row.get("selection_reason")):
                rec["selection_reason"] = str(row["selection_reason"])
            if rec:
                overrides[sid] = rec
        if num_reports > 0:
            sample_ids = sample_ids[:num_reports]
        return sample_ids, overrides

    ordered = sample_summary.sort_values(["abs_error", "sample_idx"], ascending=[False, True])
    if selection_mode == "all":
        if num_reports > 0:
            return ordered["sample_idx"].head(num_reports).astype(int).tolist(), overrides
        return ordered["sample_idx"].astype(int).tolist(), overrides
    if selection_mode == "top_error":
        target = num_reports if num_reports > 0 else len(ordered)
        return ordered["sample_idx"].head(target).astype(int).tolist(), overrides

    target = num_reports if num_reports > 0 else len(ordered)
    ids = select_diverse_cases(
        sample_summary=sample_summary,
        num_reports=target,
        max_per_drug=max_per_drug,
        max_per_cell=max_per_cell,
        max_per_tissue=max_per_tissue,
    )
    return ids, overrides


def feature_effect_text(shap_value: float, target_label: str = "AUC") -> str:
    # Both AUC and log10(IC50) are *higher-is-more-resistant* targets, so the
    # directional narrative is the same — only the label changes.
    if shap_value > 0:
        return f"pushes the prediction toward higher {target_label} (relative resistance)"
    if shap_value < 0:
        return f"pushes the prediction toward lower {target_label} (relative sensitivity)"
    return "has little directional effect on the prediction"


def expression_context(zscore: float | None) -> str:
    if zscore is None or math.isnan(zscore):
        return "expression context unavailable"
    if zscore >= 2.0:
        return "markedly above the cross-cell-line mean"
    if zscore >= 1.0:
        return "above the cross-cell-line mean"
    if zscore <= -2.0:
        return "markedly below the cross-cell-line mean"
    if zscore <= -1.0:
        return "below the cross-cell-line mean"
    return "near the cross-cell-line mean"


def interpret_case(
    *,
    observed_auc: float,
    predicted_auc: float,
    global_mean_auc: float,
    drug_mean_auc: float | None,
    cell_mean_auc: float | None,
    interpretation_scale: float = 1.0,
) -> str:
    """
    Qualitative interpretation of the sample's response.

    `interpretation_scale` rescales the two absolute thresholds (5.0 and 2.0)
    that were originally tuned against the CTRPv2.1 AUC distribution
    (std ~ 2.6). For other targets (e.g. log10(IC50), std ~ 1.3) pass a smaller
    scale so the "exceptional" bucket remains informative.
    """
    comparison_points = [predicted_auc, global_mean_auc]
    if drug_mean_auc is not None and not math.isnan(drug_mean_auc):
        comparison_points.append(drug_mean_auc)
    if cell_mean_auc is not None and not math.isnan(cell_mean_auc):
        comparison_points.append(cell_mean_auc)

    max_ref = max(comparison_points)
    min_ref = min(comparison_points)
    error = observed_auc - predicted_auc

    exceptional_thr = 5.0 * interpretation_scale
    local_thr = 2.0 * interpretation_scale

    if observed_auc <= min_ref - exceptional_thr:
        return "exceptionally sensitive relative to the SHAP-predicted response and cohort baselines"
    if observed_auc >= max_ref + exceptional_thr:
        return "exceptionally resistant relative to the SHAP-predicted response and cohort baselines"
    if error <= -local_thr:
        return "more sensitive than the model predicted"
    if error >= local_thr:
        return "more resistant than the model predicted"
    return "close to the model prediction and cohort baselines"


def selection_reason_text(prediction_error: float) -> str:
    if prediction_error > 0:
        return "selected for a large positive prediction error (observed resistance above the model prediction)"
    if prediction_error < 0:
        return "selected for a large negative prediction error (observed sensitivity below the model prediction)"
    return "selected for overall prediction error magnitude"


def build_same_drug_examples(
    *,
    pairs: pd.DataFrame,
    cpd_id: int,
    query_ccl_id: int,
    compound_meta: dict[int, dict[str, Any]],
    cell_meta: dict[int, dict[str, Any]],
    limit: int,
) -> list[dict[str, Any]]:
    cohort = pairs[pairs["master_cpd_id"] == cpd_id].copy()
    cohort = cohort[cohort["master_ccl_id"] != query_ccl_id]
    if cohort.empty:
        return []

    cohort = cohort.sort_values("y")
    low = cohort.head(max(1, limit // 2))
    high = cohort.tail(max(1, limit - len(low)))
    chosen = pd.concat([low, high]).drop_duplicates(subset=["master_ccl_id"]).head(limit)

    examples: list[dict[str, Any]] = []
    for _, row in chosen.iterrows():
        cell = _cell_info(int(row["master_ccl_id"]), cell_meta)
        examples.append(
            {
                "master_ccl_id": int(row["master_ccl_id"]),
                "cell_line": cell.get("ccl_name", ""),
                "tissue": cell.get("primary_site", ""),
                "histology": cell.get("histology", ""),
                "y": float(row["y"]),
                "profile": "more sensitive" if float(row["y"]) <= float(cohort["y"].median()) else "more resistant",
            }
        )
    return examples


def build_same_cell_examples(
    *,
    pairs: pd.DataFrame,
    ccl_id: int,
    query_cpd_id: int,
    compound_meta: dict[int, dict[str, Any]],
    limit: int,
) -> list[dict[str, Any]]:
    cohort = pairs[pairs["master_ccl_id"] == ccl_id].copy()
    cohort = cohort[cohort["master_cpd_id"] != query_cpd_id]
    if cohort.empty:
        return []

    cohort = cohort.sort_values("y")
    low = cohort.head(max(1, limit // 2))
    high = cohort.tail(max(1, limit - len(low)))
    chosen = pd.concat([low, high]).drop_duplicates(subset=["master_cpd_id"]).head(limit)

    examples: list[dict[str, Any]] = []
    for _, row in chosen.iterrows():
        drug = _drug_info(int(row["master_cpd_id"]), compound_meta)
        examples.append(
            {
                "master_cpd_id": int(row["master_cpd_id"]),
                "drug_name": drug.get("cpd_name", ""),
                "gene_target": drug.get("gene_target", ""),
                "mechanism": drug.get("mechanism", ""),
                "y": float(row["y"]),
                "profile": "more sensitive" if float(row["y"]) <= float(cohort["y"].median()) else "more resistant",
            }
        )
    return examples


def enrich_feature_row(
    row: pd.Series,
    *,
    drug_targets: set[str],
    fp_info: dict[str, dict[str, Any]],
    gene_stats: dict[str, dict[str, float]],
    gene_support_exact: dict[str, int],
    gene_support_symbol: dict[str, int],
    target_label: str = "AUC",
) -> dict[str, Any]:
    raw_feature = str(row["feature"])
    shap_value = float(row["shap_value"])
    abs_shap_value = float(row["abs_shap_value"])
    feature_value = float(row["feature_value"])
    effect_text = feature_effect_text(shap_value, target_label=target_label)

    if FP_RE.match(raw_feature):
        feature = normalize_fp_name(raw_feature)
        info = fp_info.get(feature, {})
        knowledge_parts: list[str] = []
        if info.get("smarts"):
            knowledge_parts.append(f"representative SMARTS `{info['smarts']}`")
        pct = info.get("pct_drugs")
        if pct is not None:
            knowledge_parts.append(f"present in {pct:.1f}% of CTRPv2 compounds")
        examples = info.get("example_drugs", [])[:3]
        if examples:
            knowledge_parts.append(f"example compounds: {', '.join(examples)}")

        return {
            "feature": feature,
            "feature_type": "fingerprint_bit",
            "direction": effect_text,
            "shap_value": shap_value,
            "abs_shap_value": abs_shap_value,
            "feature_value": feature_value,
            "presence": "present" if feature_value >= 0.5 else "absent",
            "substructure_smarts": info.get("smarts", ""),
            "example_drugs": examples,
            "pct_drugs_with_bit": round(float(pct), 1) if pct is not None else None,
            "knowledge_note": "; ".join(knowledge_parts) if knowledge_parts else "no local fingerprint annotation available",
        }

    gene_symbol, entrez_id = parse_gene_feature(raw_feature)
    stats = gene_stats.get(raw_feature, {})
    std = float(stats.get("std", 0.0))
    zscore = None
    if std > 0:
        zscore = (feature_value - float(stats.get("mean", 0.0))) / std
    support = gene_support_exact.get(raw_feature, gene_support_symbol.get(gene_symbol, 0))
    target_match = gene_symbol in drug_targets

    knowledge_parts = [expression_context(zscore)]
    if support:
        knowledge_parts.append(f"recurs in {support} predictable-drug RF signatures")
    if target_match:
        knowledge_parts.append("matches a reported target gene for this compound")

    return {
        "feature": raw_feature,
        "feature_type": "gene_expression",
        "gene_symbol": gene_symbol,
        "entrez_id": entrez_id,
        "direction": effect_text,
        "shap_value": shap_value,
        "abs_shap_value": abs_shap_value,
        "feature_value": feature_value,
        "feature_zscore": round(float(zscore), 3) if zscore is not None and not math.isnan(zscore) else None,
        "matches_reported_drug_target": bool(target_match),
        "supporting_drug_count": int(support),
        "knowledge_note": "; ".join(knowledge_parts),
    }


def build_framework_components(payload: dict[str, Any], target_label: str = "AUC") -> dict[str, str]:
    drug = payload["drug"]["name"]
    cell = payload["cell_line"]["name"]
    return {
        "component_1_sample_context": (
            f"Explain the observed response of {drug} on {cell} using observed {target_label}, "
            f"the RF-predicted {target_label}, and the local drug/cell cohort baselines."
        ),
        "component_2_shap_evidence": (
            f"Prioritize the top TreeSHAP features, explicitly stating whether each feature pushes the prediction "
            f"toward higher {target_label}/resistance or lower {target_label}/sensitivity."
        ),
        "component_3_metadata_grounding": (
            "Ground feature descriptions in local metadata only: gene recurrence counts, target matches, "
            "fingerprint SMARTS annotations, prevalence across compounds, and same-drug/same-cell cohort examples."
        ),
        "component_4_scope_and_caveats": (
            "Keep conclusions non-causal, note that SHAP explains the RF prediction rather than biology directly, "
            "and separate local case evidence from global training diagnostics."
        ),
    }


def render_feature_md(feature: dict[str, Any]) -> str:
    base = (
        f"**{feature['feature']}** ({feature['feature_type']}; "
        f"SHAP={feature['shap_value']:+.4f}, |SHAP|={feature['abs_shap_value']:.4f})"
    )
    if feature["feature_type"] == "fingerprint_bit":
        presence = feature.get("presence", "n/a")
        note = feature.get("knowledge_note", "")
        return f"{base}  \n  _{presence}; {note}_"

    value = feature.get("feature_value", 0.0)
    zscore = feature.get("feature_zscore")
    zscore_text = f", z={zscore:+.2f}" if zscore is not None else ""
    note = feature.get("knowledge_note", "")
    return f"{base}  \n  _value={value:.4f}{zscore_text}; {note}_"


def render_examples_table(
    *,
    title: str,
    rows: list[dict[str, Any]],
    columns: list[tuple[str, str]],
) -> list[str]:
    lines: list[str] = [title]
    if not rows:
        lines.append("_None available_")
        lines.append("")
        return lines

    lines.append("| " + " | ".join(label for label, _ in columns) + " |")
    lines.append("|" + "|".join(["---"] * len(columns)) + "|")
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(key, "")) for _, key in columns) + " |")
    lines.append("")
    return lines


def render_markdown_report(payload: dict[str, Any]) -> str:
    drug = payload["drug"]
    cell = payload["cell_line"]
    drug_cohort = payload["drug_cohort"]
    cell_cohort = payload["cell_cohort"]
    target_label = payload.get("target_label", "AUC")

    lines: list[str] = []
    lines.append(f"## {payload['report_id']} - {drug['name']} on {cell['name']}")
    lines.append(f"*Evidence: {payload['evidence_id']}*")
    lines.append("")
    lines.append("### Sample Identity")
    lines.append("| Property | Value |")
    lines.append("|---|---|")
    lines.append(f"| Drug | **{drug['name']}** (master_cpd_id={drug['master_cpd_id']}) |")
    lines.append(f"| Gene Target | {drug.get('gene_target', '') or 'n/a'} |")
    lines.append(f"| Mechanism / Activity | {drug.get('mechanism', '') or 'n/a'} |")
    lines.append(f"| Cell Line | **{cell['name']}** (master_ccl_id={cell['master_ccl_id']}) |")
    lines.append(f"| Tissue | {cell.get('tissue', '') or 'n/a'} |")
    lines.append(f"| Histology | {cell.get('histology', '') or 'n/a'} |")
    lines.append(f"| Subtype | {cell.get('subtype', '') or 'n/a'} |")
    lines.append("")

    lines.append("### Response Summary")
    lines.append(f"- Observed {target_label}: **{payload['query_y_true']:.4f}**")
    lines.append(f"- RF-predicted {target_label}: **{payload['model_predicted_auc']:.4f}**")
    lines.append(f"- Prediction error (observed - predicted): **{payload['prediction_error']:+.4f}**")
    lines.append(f"- Global mean {target_label} across all pairs: **{payload['global_mean_auc']:.4f}**")
    lines.append(
        f"- Drug cohort ({drug_cohort['n']} pairs): mean={drug_cohort['mean_auc']:.4f}, "
        f"q10={drug_cohort['q10_auc']:.4f}, median={drug_cohort['q50_auc']:.4f}, "
        f"q90={drug_cohort['q90_auc']:.4f}, sample percentile={drug_cohort['auc_percentile']:.1f}"
    )
    lines.append(
        f"- Cell cohort ({cell_cohort['n']} pairs): mean={cell_cohort['mean_auc']:.4f}, "
        f"q10={cell_cohort['q10_auc']:.4f}, median={cell_cohort['q50_auc']:.4f}, "
        f"q90={cell_cohort['q90_auc']:.4f}, sample percentile={cell_cohort['auc_percentile']:.1f}"
    )
    lines.append(f"- Interpretation: **{payload['interpretation']}**")
    lines.append(f"- Selection reason: {payload['selection_reason']}")
    lines.append("")

    lines.append("### Top TreeSHAP Features")
    for idx, feature in enumerate(payload["enriched_features"], start=1):
        lines.append(f"{idx}. {render_feature_md(feature)}")
    lines.append("")

    lines.extend(
        render_examples_table(
            title="### Same-Drug Cohort Examples",
            rows=payload["same_drug_examples"],
            columns=[
                ("Cell Line", "cell_line"),
                ("Tissue", "tissue"),
                ("AUC", "y"),
                ("Profile", "profile"),
            ],
        )
    )
    lines.extend(
        render_examples_table(
            title="### Same-Cell Cohort Examples",
            rows=payload["same_cell_examples"],
            columns=[
                ("Drug", "drug_name"),
                ("Gene Target", "gene_target"),
                ("AUC", "y"),
                ("Profile", "profile"),
            ],
        )
    )

    lines.append("### Scope and Constraints")
    lines.append("- TreeSHAP values explain the fitted Random Forest prediction for this sample; they are not direct causal evidence.")
    lines.append("- Molecular descriptions are grounded in local CTRPv2 metadata, local feature tables, and local cohort summaries only.")
    lines.append("- Any global model metrics referenced downstream should be treated as training diagnostics rather than held-out performance.")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def build_payload_for_case(
    *,
    report_id: str,
    evidence_id: str,
    case_row: pd.Series,
    feature_rows: pd.DataFrame,
    pairs: pd.DataFrame,
    compound_meta: dict[int, dict[str, Any]],
    cell_meta: dict[int, dict[str, Any]],
    fp_info: dict[str, dict[str, Any]],
    gene_stats: dict[str, dict[str, float]],
    gene_support_exact: dict[str, int],
    gene_support_symbol: dict[str, int],
    per_drug_r2_lookup: dict[int, dict[str, Any]],
    drug_stats_lookup: dict[int, dict[str, Any]],
    cell_stats_lookup: dict[int, dict[str, Any]],
    global_mean_auc: float,
    same_drug_examples: int,
    same_cell_examples: int,
    top_k_features: int,
    target_label: str = "AUC",
    interpretation_scale: float = 1.0,
    knowledge_sources: list[str] | None = None,
    selection_tag: str | None = None,
    selection_reason_override: str | None = None,
) -> dict[str, Any]:
    cpd_id = int(case_row["master_cpd_id"])
    ccl_id = int(case_row["master_ccl_id"])
    observed_auc = float(case_row["y_true"])
    predicted_auc = float(case_row["y_pred"])
    prediction_error = observed_auc - predicted_auc

    drug = _drug_info(cpd_id, compound_meta)
    cell = _cell_info(ccl_id, cell_meta)
    drug_targets = split_targets(drug.get("gene_target", ""))

    drug_stats = drug_stats_lookup.get(cpd_id, {})
    cell_stats = cell_stats_lookup.get(ccl_id, {})

    drug_group = pairs[pairs["master_cpd_id"] == cpd_id]["y"]
    cell_group = pairs[pairs["master_ccl_id"] == ccl_id]["y"]

    same_drug = build_same_drug_examples(
        pairs=pairs,
        cpd_id=cpd_id,
        query_ccl_id=ccl_id,
        compound_meta=compound_meta,
        cell_meta=cell_meta,
        limit=same_drug_examples,
    )
    same_cell = build_same_cell_examples(
        pairs=pairs,
        ccl_id=ccl_id,
        query_cpd_id=cpd_id,
        compound_meta=compound_meta,
        limit=same_cell_examples,
    )

    enriched_features = [
        enrich_feature_row(
            row,
            drug_targets=drug_targets,
            fp_info=fp_info,
            gene_stats=gene_stats,
            gene_support_exact=gene_support_exact,
            gene_support_symbol=gene_support_symbol,
            target_label=target_label,
        )
        for _, row in feature_rows.head(top_k_features).iterrows()
    ]

    payload: dict[str, Any] = {
        "report_id": report_id,
        "evidence_id": evidence_id,
        "source_type": "tree_shap_rf",
        "selection_reason": (
            selection_reason_override
            if selection_reason_override
            else selection_reason_text(prediction_error)
        ),
        "drug": {
            "master_cpd_id": cpd_id,
            "name": drug.get("cpd_name", ""),
            "gene_target": drug.get("gene_target", ""),
            "mechanism": drug.get("mechanism", ""),
            "per_drug_cv_r2": (
                float(per_drug_r2_lookup[cpd_id]["r2"])
                if cpd_id in per_drug_r2_lookup
                else None
            ),
        },
        "cell_line": {
            "master_ccl_id": ccl_id,
            "name": cell.get("ccl_name", ""),
            "tissue": cell.get("primary_site", ""),
            "histology": cell.get("histology", ""),
            "subtype": cell.get("subtype", ""),
        },
        "query_y_true": observed_auc,
        "model_predicted_auc": predicted_auc,
        "prediction_error": prediction_error,
        "abs_error": abs(prediction_error),
        "global_mean_auc": global_mean_auc,
        "drug_cohort": {
            "n": int(drug_stats.get("n", 0)),
            "mean_auc": float(drug_stats.get("mean", float("nan"))),
            "q10_auc": float(drug_stats.get("q10", float("nan"))),
            "q50_auc": float(drug_stats.get("q50", float("nan"))),
            "q90_auc": float(drug_stats.get("q90", float("nan"))),
            "auc_percentile": percentile_leq(drug_group, observed_auc),
        },
        "cell_cohort": {
            "n": int(cell_stats.get("n", 0)),
            "mean_auc": float(cell_stats.get("mean", float("nan"))),
            "q10_auc": float(cell_stats.get("q10", float("nan"))),
            "q50_auc": float(cell_stats.get("q50", float("nan"))),
            "q90_auc": float(cell_stats.get("q90", float("nan"))),
            "auc_percentile": percentile_leq(cell_group, observed_auc),
        },
        "interpretation": interpret_case(
            observed_auc=observed_auc,
            predicted_auc=predicted_auc,
            global_mean_auc=global_mean_auc,
            drug_mean_auc=float(drug_stats.get("mean", float("nan"))),
            cell_mean_auc=float(cell_stats.get("mean", float("nan"))),
            interpretation_scale=interpretation_scale,
        ),
        "enriched_features": enriched_features,
        "same_drug_examples": same_drug,
        "same_cell_examples": same_cell,
        "target_label": target_label,
        "knowledge_sources": knowledge_sources or [
            "results/tuning/shap_values.parquet",
            "data/CTRPv2/v21.meta.per_compound.txt",
            "data/CTRPv2/v21.meta.per_cell_line.txt",
            "results/rf_plots/per_drug_r2.csv",
            "results/rf_plots/gene_signature_counts.csv",
            "data/processed/pairs.csv",
        ],
    }
    if selection_tag is not None:
        payload["selection_tag"] = selection_tag
    payload["framework_components"] = build_framework_components(payload, target_label=target_label)
    return payload


def main() -> None:
    args = parse_args()

    shap_path = Path(args.shap_values).resolve()
    pairs_path = Path(args.pairs).resolve()
    compound_meta_path = Path(args.compound_meta).resolve()
    cell_meta_path = Path(args.cell_meta).resolve()
    cell_features_path = Path(args.cell_features).resolve()
    per_drug_r2_path = Path(args.per_drug_r2).resolve()
    gene_signatures_path = Path(args.gene_signatures).resolve()
    out_jsonl = Path(args.out_jsonl).resolve()
    out_md = Path(args.out_md).resolve()
    fp_cache = Path(args.fp_cache).resolve()

    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)

    target_label = args.target_label

    print("Loading metadata...")
    compound_meta = _load_compound_meta(compound_meta_path)
    cell_meta = _load_cell_meta(cell_meta_path)
    gene_stats = load_gene_stats(cell_features_path)
    gene_support_exact, gene_support_symbol = load_gene_support(gene_signatures_path)

    print("Loading cohort statistics...")
    if str(pairs_path).endswith(".parquet"):
        pairs = pd.read_parquet(pairs_path)
    else:
        pairs = pd.read_csv(pairs_path)
    global_mean_auc = float(pairs["y"].mean())

    if args.interpretation_scale is not None:
        interpretation_scale = float(args.interpretation_scale)
    elif target_label.strip().upper() == "AUC":
        interpretation_scale = 1.0
    else:
        interpretation_scale = max(0.1, float(pairs["y"].std()) / 2.6)
    print(
        f"  target_label={target_label!r}, interpretation_scale={interpretation_scale:.4f} "
        f"(exceptional threshold = {5.0 * interpretation_scale:.2f}, "
        f"local threshold = {2.0 * interpretation_scale:.2f})"
    )
    drug_stats = build_group_stats(pairs, "master_cpd_id")
    cell_stats = build_group_stats(pairs, "master_ccl_id")
    drug_stats_lookup = {
        int(row["master_cpd_id"]): row
        for row in drug_stats.to_dict(orient="records")
    }
    cell_stats_lookup = {
        int(row["master_ccl_id"]): row
        for row in cell_stats.to_dict(orient="records")
    }

    per_drug_r2_df = pd.read_csv(per_drug_r2_path)
    per_drug_r2_lookup = {
        int(row["master_cpd_id"]): {
            "master_cpd_id": int(row["master_cpd_id"]),
            "r2": float(row["r2"]),
            "cpd_name": str(row["cpd_name"]),
        }
        for _, row in per_drug_r2_df.iterrows()
    }

    print("Loading TreeSHAP export...")
    shap_df = pd.read_parquet(shap_path)
    shap_df["feature"] = shap_df["feature"].astype(str)
    shap_df["cell_line"] = shap_df["cell_line"].astype(str)
    shap_df["drug"] = shap_df["drug"].astype(str)

    print("Building / loading fingerprint metadata cache...")
    fp_info = load_or_build_fp_metadata(
        compound_meta=compound_meta,
        cache_path=fp_cache,
        n_bits=args.morgan_bits,
        radius=args.morgan_radius,
    )

    sample_summary = (
        shap_df.groupby("sample_idx")[["y_true", "y_pred", "master_ccl_id", "master_cpd_id", "cell_line", "drug"]]
        .first()
        .reset_index()
    )
    sample_summary["prediction_error"] = sample_summary["y_true"] - sample_summary["y_pred"]
    sample_summary["abs_error"] = sample_summary["prediction_error"].abs()
    sample_summary["tissue"] = sample_summary["master_ccl_id"].map(
        lambda ccl_id: _cell_info(int(ccl_id), cell_meta).get("primary_site", "") or "unknown"
    )

    total_requested = args.num_reports if args.num_reports > 0 else len(sample_summary)
    print(
        f"Selecting {total_requested} SHAP-grounded cases "
        f"with selection mode `{args.selection_mode}`..."
    )
    selected_sample_ids, selection_overrides = select_case_ids(
        sample_summary,
        selection_mode=args.selection_mode,
        num_reports=args.num_reports,
        max_per_drug=args.max_per_drug,
        max_per_cell=args.max_per_cell,
        max_per_tissue=args.max_per_tissue,
        selection_csv=args.selection_csv,
    )
    if args.selection_mode != "from_csv" and len(selected_sample_ids) < total_requested:
        raise RuntimeError(
            f"Only selected {len(selected_sample_ids)} cases; expected {total_requested}."
        )

    knowledge_sources: list[str] | None = None
    if args.knowledge_sources:
        knowledge_sources = [
            s.strip() for s in str(args.knowledge_sources).split(",") if s.strip()
        ]

    md_parts = [f"# SHAP-Grounded Sample Reports ({target_label})", ""]
    with out_jsonl.open("w", encoding="utf-8") as fout:
        for idx, sample_idx in enumerate(selected_sample_ids, start=1):
            report_id = f"RPT-{idx:04d}"
            evidence_id = f"SHAP-{idx:04d}"
            case_row = sample_summary.loc[sample_summary["sample_idx"] == sample_idx].iloc[0]
            feature_rows = shap_df.loc[shap_df["sample_idx"] == sample_idx].sort_values(
                ["feature_rank", "abs_shap_value"], ascending=[True, False]
            )
            override = selection_overrides.get(int(sample_idx), {})
            payload = build_payload_for_case(
                report_id=report_id,
                evidence_id=evidence_id,
                case_row=case_row,
                feature_rows=feature_rows,
                pairs=pairs,
                compound_meta=compound_meta,
                cell_meta=cell_meta,
                fp_info=fp_info,
                gene_stats=gene_stats,
                gene_support_exact=gene_support_exact,
                gene_support_symbol=gene_support_symbol,
                per_drug_r2_lookup=per_drug_r2_lookup,
                drug_stats_lookup=drug_stats_lookup,
                cell_stats_lookup=cell_stats_lookup,
                global_mean_auc=global_mean_auc,
                same_drug_examples=args.same_drug_examples,
                same_cell_examples=args.same_cell_examples,
                top_k_features=args.top_k_features,
                target_label=target_label,
                interpretation_scale=interpretation_scale,
                knowledge_sources=knowledge_sources,
                selection_tag=override.get("selection_tag"),
                selection_reason_override=override.get("selection_reason"),
            )
            fout.write(json.dumps(payload, ensure_ascii=True) + "\n")
            md_parts.append(render_markdown_report(payload))

    out_md.write_text("\n".join(md_parts), encoding="utf-8")
    print(f"Wrote {len(selected_sample_ids)} structured SHAP reports to {out_jsonl}")
    print(f"Wrote Markdown summary to {out_md}")


if __name__ == "__main__":
    main()
