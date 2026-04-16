#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import pandas as pd


MODEL_REGISTRY: dict[str, dict[str, Any]] = {
    "BioMistral-7B": {
        "path": "/sc/arion/scratch/cuiz02/hf_cache/transformers/BioMistral-7B",
        "gpu_mem": "20G",
        "host_mem": "48G",
        "wall_minutes": 240,
        "style": "chat_merge_system",
        "load_strategy": "auto",
        "context_window": 32768,
        "prompt_profile": {
            "feature_limit": 6,
            "neighbor_limit": 5,
            "fingerprint_limit": 6,
            "gene_limit": 6,
            "include_feature_smarts": True,
            "include_feature_examples": False,
            "word_limit": 450,
        },
        "generation": {
            "max_new_tokens": 450,
            "temperature": 0.1,
            "top_p": 0.9,
            "repetition_penalty": 1.05,
            "context_margin": 32,
        },
    },
    "Meditron-7b": {
        "path": "/sc/arion/scratch/cuiz02/hf_cache/transformers/Meditron-7b",
        "gpu_mem": "20G",
        "host_mem": "48G",
        "wall_minutes": 240,
        "style": "plain_base_model",
        "load_strategy": "auto",
        "context_window": 2048,
        "prompt_profile": {
            "feature_limit": 4,
            "neighbor_limit": 3,
            "fingerprint_limit": 4,
            "gene_limit": 4,
            "include_feature_smarts": False,
            "include_feature_examples": False,
            "word_limit": 300,
        },
        "generation": {
            "max_new_tokens": 256,
            "temperature": 0.0,
            "top_p": 1.0,
            "repetition_penalty": 1.18,
            "no_repeat_ngram_size": 5,
            "context_margin": 32,
        },
    },
    "Meta-Llama-3.1-8B-Instruct": {
        "path": "/sc/arion/scratch/cuiz02/hf_cache/transformers/Meta-Llama-3.1-8B-Instruct",
        "gpu_mem": "24G",
        "host_mem": "64G",
        "wall_minutes": 240,
        "style": "chat",
        "load_strategy": "auto",
        "context_window": 131072,
        "prompt_profile": {
            "feature_limit": 6,
            "neighbor_limit": 5,
            "fingerprint_limit": 8,
            "gene_limit": 8,
            "include_feature_smarts": True,
            "include_feature_examples": True,
            "word_limit": 550,
        },
        "generation": {
            "max_new_tokens": 650,
            "temperature": 0.15,
            "top_p": 0.9,
            "repetition_penalty": 1.02,
            "context_margin": 32,
        },
    },
    "Qwen2.5-32B-Instruct": {
        "path": "/sc/arion/scratch/cuiz02/hf_cache/transformers/Qwen2.5-32B-Instruct",
        "gpu_mem": "70G",
        "host_mem": "96G",
        "wall_minutes": 360,
        "style": "chat",
        "load_strategy": "auto",
        "context_window": 32768,
        "prompt_profile": {
            "feature_limit": 6,
            "neighbor_limit": 5,
            "fingerprint_limit": 8,
            "gene_limit": 8,
            "include_feature_smarts": True,
            "include_feature_examples": True,
            "word_limit": 550,
        },
        "generation": {
            "max_new_tokens": 650,
            "temperature": 0.15,
            "top_p": 0.9,
            "repetition_penalty": 1.02,
            "context_margin": 32,
        },
    },
    "gpt-oss-20b": {
        "path": "/sc/arion/scratch/cuiz02/hf_cache/transformers/gpt-oss-20b",
        "gpu_mem": "70G",
        "host_mem": "96G",
        "wall_minutes": 360,
        "style": "chat",
        "load_strategy": "single_gpu",
        "context_window": 131072,
        "prompt_profile": {
            "feature_limit": 6,
            "neighbor_limit": 5,
            "fingerprint_limit": 8,
            "gene_limit": 8,
            "include_feature_smarts": True,
            "include_feature_examples": True,
            "word_limit": 550,
        },
        "generation": {
            "max_new_tokens": 650,
            "temperature": 0.1,
            "top_p": 0.9,
            "repetition_penalty": 1.02,
            "context_margin": 32,
        },
    },
}

REQUIRED_HEADINGS = [
    "## Executive Summary",
    "## Evidence-Based Interpretation",
    "## Feature and Neighborhood Analysis",
    "## Model-Level Context",
    "## Confidence and Caveats",
]


@dataclass
class GlobalContext:
    metrics_dem: dict[str, Any]
    best_depth: dict[str, Any]
    best_n_estimators: dict[str, Any]
    top_fingerprints: list[dict[str, Any]]
    per_drug_r2: dict[int, dict[str, Any]]
    top_gene_signatures: list[dict[str, Any]]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate grounded LLM reports from structured pharmacogenomics evidence using local HF models."
    )
    parser.add_argument(
        "--model-key",
        required=True,
        choices=sorted(MODEL_REGISTRY),
        help="Logical model key from the local registry.",
    )
    parser.add_argument(
        "--reports",
        default="llm_explainer/shap_sample_reports.jsonl",
        help="Input structured reports JSONL.",
    )
    parser.add_argument(
        "--results-root",
        default="results",
        help="Root folder that contains dem/, tuning/, and rf_plots/.",
    )
    parser.add_argument(
        "--output-root",
        default="llm_explainer/outputs",
        help="Where per-model outputs are written.",
    )
    parser.add_argument(
        "--max-reports",
        type=int,
        default=0,
        help="Optional cap on number of reports (0 = all).",
    )
    parser.add_argument(
        "--max-new-tokens",
        type=int,
        default=0,
        help="Generation length cap. Use 0 to accept the model-specific default.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=-1.0,
        help="Sampling temperature. Use a negative value to accept the model-specific default.",
    )
    parser.add_argument(
        "--top-p",
        type=float,
        default=0.0,
        help="Top-p sampling cutoff when temperature > 0. Use 0 to accept the model-specific default.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing output files for this model.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build prompts and metadata only; skip model loading and generation.",
    )
    return parser.parse_args()


def slugify(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def ensure_output_dir(path: Path, overwrite: bool) -> None:
    path.mkdir(parents=True, exist_ok=True)
    if not overwrite:
        existing = list(path.glob("*.json")) + list(path.glob("*.jsonl")) + list(path.glob("*.md"))
        if existing:
            raise FileExistsError(
                f"{path} already contains outputs. Re-run with --overwrite to replace them."
            )


def load_global_context(results_root: Path) -> GlobalContext:
    metrics_path = results_root / "dem" / "metrics_dem.json"
    depth_path = results_root / "tuning" / "tuning_results_max_depth.csv"
    n_est_path = results_root / "tuning" / "tuning_results_n_estimators.csv"
    fp_path = results_root / "tuning" / "fingerprint_importances.csv"
    per_drug_path = results_root / "rf_plots" / "per_drug_r2.csv"
    gene_sig_path = results_root / "rf_plots" / "gene_signature_counts.csv"

    with metrics_path.open("r", encoding="utf-8") as f:
        metrics_dem = json.load(f)

    depth_df = pd.read_csv(depth_path)
    best_depth_row = depth_df.loc[depth_df["r2"].idxmax()].to_dict()

    n_est_df = pd.read_csv(n_est_path)
    best_n_est_row = n_est_df.loc[n_est_df["mean_r2"].idxmax()].to_dict()

    fp_df = pd.read_csv(fp_path, index_col=0).reset_index()
    fp_df.columns = ["feature", "importance"]
    top_fingerprints = fp_df.head(12).to_dict(orient="records")

    per_drug_df = pd.read_csv(per_drug_path)
    per_drug_r2 = {
        int(row["master_cpd_id"]): {
            "master_cpd_id": int(row["master_cpd_id"]),
            "r2": float(row["r2"]),
            "cpd_name": str(row["cpd_name"]),
        }
        for _, row in per_drug_df.iterrows()
    }

    gene_sig_df = pd.read_csv(gene_sig_path, index_col=0).reset_index()
    gene_sig_df.columns = ["gene", "n_drugs"]
    top_gene_signatures = gene_sig_df.head(12).to_dict(orient="records")

    return GlobalContext(
        metrics_dem=metrics_dem,
        best_depth=best_depth_row,
        best_n_estimators=best_n_est_row,
        top_fingerprints=top_fingerprints,
        per_drug_r2=per_drug_r2,
        top_gene_signatures=top_gene_signatures,
    )


def report_title(report: dict[str, Any]) -> str:
    drug_name = report.get("drug", {}).get("name", "unknown drug")
    cell_name = report.get("cell_line", {}).get("name", "unknown cell line")
    return f"{report.get('report_id', 'RPT-UNK')} - {drug_name} on {cell_name}"


def compact_dem_feature_lines(
    features: list[dict[str, Any]],
    limit: int = 6,
    *,
    include_smarts: bool = True,
    include_examples: bool = True,
) -> list[str]:
    lines: list[str] = []
    for idx, feat in enumerate(features[:limit], start=1):
        smarts = feat.get("substructure_smarts", "")
        examples = feat.get("example_drugs", [])[:3]
        example_str = ", ".join(examples) if examples else "n/a"
        pct = feat.get("pct_drugs_with_bit", "n/a")
        pieces = [
            f"{idx}. {feat['feature']}",
            feat["direction"],
            f"z={feat['z_score']:.2f}",
            f"query={feat['query_value']:.3f}",
            f"neighborhood={feat['neighborhood_mean']:.3f}",
            f"global={feat['global_mean']:.3f}",
        ]
        if include_smarts:
            pieces.append(f"SMARTS={smarts or 'n/a'}")
        if include_examples:
            pieces.append(f"example_drugs={example_str}")
        pieces.append(f"pct_drugs={pct}")
        lines.append(" | ".join(pieces))
    return lines


def compact_shap_feature_lines(
    features: list[dict[str, Any]],
    limit: int = 6,
    *,
    include_smarts: bool = True,
    include_examples: bool = True,
) -> list[str]:
    lines: list[str] = []
    for idx, feat in enumerate(features[:limit], start=1):
        pieces = [
            f"{idx}. {feat.get('feature', 'unknown')}",
            f"type={feat.get('feature_type', 'unknown')}",
            feat.get("direction", "n/a"),
            f"shap={float(feat.get('shap_value', 0.0)):+.4f}",
            f"abs_shap={float(feat.get('abs_shap_value', 0.0)):.4f}",
            f"value={float(feat.get('feature_value', 0.0)):.4f}",
        ]
        if feat.get("feature_type") == "gene_expression":
            zscore = feat.get("feature_zscore")
            if zscore is not None:
                pieces.append(f"z={float(zscore):+.2f}")
            support = int(feat.get("supporting_drug_count", 0))
            if support:
                pieces.append(f"supporting_drugs={support}")
            if feat.get("matches_reported_drug_target"):
                pieces.append("target_match=yes")
        else:
            pct = feat.get("pct_drugs_with_bit")
            if pct is not None:
                pieces.append(f"pct_drugs={float(pct):.1f}")
            if include_smarts:
                pieces.append(f"SMARTS={feat.get('substructure_smarts', '') or 'n/a'}")
            if include_examples:
                examples = feat.get("example_drugs", [])[:3]
                pieces.append(f"example_drugs={', '.join(examples) if examples else 'n/a'}")
        note = feat.get("knowledge_note")
        if note:
            pieces.append(f"note={note}")
        lines.append(" | ".join(pieces))
    return lines


def compact_neighbor_lines(neighbors: list[dict[str, Any]], limit: int = 5) -> list[str]:
    lines: list[str] = []
    for idx, item in enumerate(neighbors[:limit], start=1):
        lines.append(
            f"{idx}. drug={item.get('drug_name', '?')} | cell={item.get('cell_line', '?')} | "
            f"tissue={item.get('tissue', '?')} | auc={item.get('y', 0):.4f} | "
            f"kernel_score={item.get('kernel_score', 0):.4f}"
        )
    return lines


def compact_cohort_lines(
    items: list[dict[str, Any]],
    limit: int = 4,
    *,
    group_kind: str,
) -> list[str]:
    lines: list[str] = []
    for idx, item in enumerate(items[:limit], start=1):
        if group_kind == "same_drug":
            lines.append(
                f"{idx}. cell={item.get('cell_line', '?')} | tissue={item.get('tissue', '?')} | "
                f"auc={float(item.get('y', 0.0)):.4f} | profile={item.get('profile', 'n/a')}"
            )
        else:
            lines.append(
                f"{idx}. drug={item.get('drug_name', '?')} | target={item.get('gene_target', '') or 'n/a'} | "
                f"auc={float(item.get('y', 0.0)):.4f} | profile={item.get('profile', 'n/a')}"
            )
    return lines


def is_shap_report(report: dict[str, Any]) -> bool:
    return report.get("source_type") == "tree_shap_rf" or "model_predicted_auc" in report


def build_aux_context(
    report: dict[str, Any],
    context: GlobalContext,
    prompt_profile: dict[str, Any],
) -> str:
    drug = report.get("drug", {})
    cell = report.get("cell_line", {})
    drug_id = drug.get("master_cpd_id")
    per_drug = context.per_drug_r2.get(int(drug_id)) if drug_id is not None else None

    metrics = context.metrics_dem
    best_depth = context.best_depth
    best_n_est = context.best_n_estimators

    fp_lines = [
        f"{row['feature']} ({row['importance']:.5f})"
        for row in context.top_fingerprints[: int(prompt_profile.get("fingerprint_limit", 8))]
    ]
    gene_lines = [
        f"{row['gene']} ({int(row['n_drugs'])} drugs)"
        for row in context.top_gene_signatures[: int(prompt_profile.get("gene_limit", 8))]
    ]

    pieces = [
        "Global model context:",
        (
            f"- DEM training fit only: n_samples={metrics['n_samples']}, "
            f"n_features={metrics['n_features']}, train_r2={metrics['train_r2']:.4f}, "
            f"train_rmse={metrics['train_rmse']:.4f}, train_corr={metrics['train_corr']:.4f}. "
            "Treat these as training diagnostics, not held-out generalization."
        ),
        (
            f"- Max-depth tuning best row: max_depth={int(best_depth['max_depth'])}, "
            f"n_estimators={int(best_depth['n_estimators'])}, r2={float(best_depth['r2']):.4f}."
        ),
        (
            f"- N-estimator tuning best row: max_depth={int(best_n_est['max_depth'])}, "
            f"n_estimators={int(best_n_est['n_estimators'])}, "
            f"mean_r2={float(best_n_est['mean_r2']):.4f}, std_r2={float(best_n_est['std_r2']):.4f}."
        ),
        f"- Top global fingerprint features: {', '.join(fp_lines)}.",
        f"- Most common genes across predictable per-drug models: {', '.join(gene_lines)}.",
    ]

    if per_drug is not None:
        pieces.append(
            f"- Per-drug cross-validated predictability for {per_drug['cpd_name']}: "
            f"R2={per_drug['r2']:.4f}."
        )
    else:
        pieces.append(
            f"- No per-drug cross-validated predictability entry was found for "
            f"{drug.get('name', 'this drug')}."
        )

    if cell.get("subtype"):
        pieces.append(f"- Cell subtype metadata is available: {cell['subtype']}.")

    return "\n".join(pieces)


def build_system_prompt(model_key: str) -> str:
    prompt_profile = MODEL_REGISTRY[model_key]["prompt_profile"]
    word_limit = int(prompt_profile.get("word_limit", 550))
    base = (
        "You are a careful pharmacogenomics model explainer.\n"
        "Write a grounded report from structured evidence only.\n"
        "Rules:\n"
        "1. Lower AUC means greater sensitivity; higher AUC means greater resistance.\n"
        "2. For SHAP inputs, positive SHAP values push the prediction toward higher AUC/resistance and negative SHAP values push toward lower AUC/sensitivity.\n"
        "3. Separate local evidence for this sample from global model context.\n"
        "4. Treat train_r2, train_rmse, and train_corr as training-fit diagnostics only.\n"
        "5. Do not invent pathways, biomarkers, or mechanisms that are not supported by the prompt.\n"
        "6. If a field is missing, say it is unavailable.\n"
        "7. Do not give clinical advice.\n"
        "8. Return only markdown for the final report.\n"
        f"9. Use short paragraphs and keep the report under {word_limit} words.\n"
        "10. Follow the Lee-style four-part grounding flow: sample context, SHAP/feature evidence, metadata-backed support, and caveats.\n"
        "11. Use these exact section headings:\n"
        + "\n".join(REQUIRED_HEADINGS)
    )
    if model_key == "gpt-oss-20b":
        return base + "\nReasoning: medium. Do not expose hidden reasoning."
    return base


def build_user_prompt(report: dict[str, Any], context: GlobalContext, model_key: str) -> str:
    drug = report.get("drug", {})
    cell = report.get("cell_line", {})
    prompt_profile = MODEL_REGISTRY[model_key]["prompt_profile"]
    subtype = cell.get("subtype", "") or "n/a"

    if is_shap_report(report):
        features = compact_shap_feature_lines(
            report.get("enriched_features", []),
            limit=int(prompt_profile.get("feature_limit", 6)),
            include_smarts=bool(prompt_profile.get("include_feature_smarts", True)),
            include_examples=bool(prompt_profile.get("include_feature_examples", True)),
        )
        same_drug_examples = compact_cohort_lines(
            report.get("same_drug_examples", []),
            limit=int(prompt_profile.get("neighbor_limit", 5)),
            group_kind="same_drug",
        )
        same_cell_examples = compact_cohort_lines(
            report.get("same_cell_examples", []),
            limit=int(prompt_profile.get("neighbor_limit", 5)),
            group_kind="same_cell",
        )
        drug_cohort = report.get("drug_cohort", {})
        cell_cohort = report.get("cell_cohort", {})
        framework = report.get("framework_components", {})

        return "\n".join(
            [
                f"Case: {report_title(report)}",
                "",
                "Lee-style grounding components:",
                f"1. sample_context: {framework.get('component_1_sample_context', 'n/a')}",
                f"2. shap_evidence: {framework.get('component_2_shap_evidence', 'n/a')}",
                f"3. metadata_grounding: {framework.get('component_3_metadata_grounding', 'n/a')}",
                f"4. scope_and_caveats: {framework.get('component_4_scope_and_caveats', 'n/a')}",
                "",
                "Case-level evidence:",
                f"- source_type: {report.get('source_type', 'n/a')}",
                f"- report_id: {report.get('report_id')}",
                f"- evidence_id: {report.get('evidence_id')}",
                f"- drug_name: {drug.get('name', 'n/a')}",
                f"- drug_id: {drug.get('master_cpd_id', 'n/a')}",
                f"- gene_target: {drug.get('gene_target', '') or 'n/a'}",
                f"- mechanism: {drug.get('mechanism', '') or 'n/a'}",
                f"- per_drug_cv_r2: {drug.get('per_drug_cv_r2') if drug.get('per_drug_cv_r2') is not None else 'n/a'}",
                f"- cell_line: {cell.get('name', 'n/a')}",
                f"- tissue: {cell.get('tissue', 'n/a')}",
                f"- histology: {cell.get('histology', 'n/a')}",
                f"- subtype: {subtype}",
                f"- observed_auc: {report.get('query_y_true', 0):.4f}",
                f"- model_predicted_auc: {report.get('model_predicted_auc', 0):.4f}",
                f"- prediction_error: {report.get('prediction_error', 0):+.4f}",
                f"- abs_error: {report.get('abs_error', 0):.4f}",
                f"- global_mean_auc: {report.get('global_mean_auc', 0):.4f}",
                f"- interpretation: {report.get('interpretation', 'n/a')}",
                f"- selection_reason: {report.get('selection_reason', 'n/a')}",
                "",
                "Drug cohort context:",
                (
                    f"- n={drug_cohort.get('n', 'n/a')} | mean_auc={float(drug_cohort.get('mean_auc', 0.0)):.4f} | "
                    f"q10={float(drug_cohort.get('q10_auc', 0.0)):.4f} | "
                    f"median={float(drug_cohort.get('q50_auc', 0.0)):.4f} | "
                    f"q90={float(drug_cohort.get('q90_auc', 0.0)):.4f} | "
                    f"sample_percentile={float(drug_cohort.get('auc_percentile', 0.0)):.1f}"
                ),
                "Cell cohort context:",
                (
                    f"- n={cell_cohort.get('n', 'n/a')} | mean_auc={float(cell_cohort.get('mean_auc', 0.0)):.4f} | "
                    f"q10={float(cell_cohort.get('q10_auc', 0.0)):.4f} | "
                    f"median={float(cell_cohort.get('q50_auc', 0.0)):.4f} | "
                    f"q90={float(cell_cohort.get('q90_auc', 0.0)):.4f} | "
                    f"sample_percentile={float(cell_cohort.get('auc_percentile', 0.0)):.1f}"
                ),
                "",
                "Top TreeSHAP features:",
                *(features if features else ["- none"]),
                "",
                "Same-drug cohort examples:",
                *(same_drug_examples if same_drug_examples else ["- none"]),
                "",
                "Same-cell cohort examples:",
                *(same_cell_examples if same_cell_examples else ["- none"]),
                "",
                "Knowledge sources:",
                *[
                    f"- {src}"
                    for src in report.get("knowledge_sources", [])
                ],
                "",
                build_aux_context(report, context, prompt_profile),
                "",
                "Write one grounded markdown report with the required section headings.",
            ]
        )

    features = compact_dem_feature_lines(
        report.get("enriched_features", []),
        limit=int(prompt_profile.get("feature_limit", 6)),
        include_smarts=bool(prompt_profile.get("include_feature_smarts", True)),
        include_examples=bool(prompt_profile.get("include_feature_examples", True)),
    )
    neighbors = compact_neighbor_lines(
        report.get("neighbor_details", []),
        limit=int(prompt_profile.get("neighbor_limit", 5)),
    )

    return "\n".join(
        [
            f"Case: {report_title(report)}",
            "",
            "Case-level evidence:",
            f"- report_id: {report.get('report_id')}",
            f"- evidence_id: {report.get('evidence_id')}",
            f"- drug_name: {drug.get('name', 'n/a')}",
            f"- drug_id: {drug.get('master_cpd_id', 'n/a')}",
            f"- gene_target: {drug.get('gene_target', '') or 'n/a'}",
            f"- mechanism: {drug.get('mechanism', '') or 'n/a'}",
            f"- cell_line: {cell.get('name', 'n/a')}",
            f"- tissue: {cell.get('tissue', 'n/a')}",
            f"- histology: {cell.get('histology', 'n/a')}",
            f"- subtype: {subtype}",
            f"- observed_auc: {report.get('query_y_true', 0):.4f}",
            f"- neighborhood_weighted_auc: {report.get('neighborhood_y_weighted_mean', 0):.4f}",
            f"- abs_gap: {report.get('abs_gap', 0):.4f}",
            f"- provided_interpretation: {report.get('interpretation', 'n/a')}",
            "",
            "Top distinguishing features:",
            *(features if features else ["- none"]),
            "",
            "Nearest neighbors:",
            *(neighbors if neighbors else ["- none"]),
            "",
            build_aux_context(report, context, prompt_profile),
            "",
            "Write one grounded markdown report with the required section headings.",
        ]
    )


def load_transformers():
    from transformers import AutoModelForCausalLM, AutoTokenizer

    return AutoModelForCausalLM, AutoTokenizer


def resolve_dtype(torch_module) -> Any:
    if torch_module.cuda.is_available():
        if torch_module.cuda.is_bf16_supported():
            return torch_module.bfloat16
        return torch_module.float16
    return torch_module.float32


def configure_tokenizer(tokenizer, model_path: Path) -> None:
    if tokenizer.pad_token_id is None and tokenizer.eos_token_id is not None:
        tokenizer.pad_token = tokenizer.eos_token
    if getattr(tokenizer, "chat_template", None):
        return
    chat_template_path = model_path / "chat_template.jinja"
    if chat_template_path.exists():
        tokenizer.chat_template = chat_template_path.read_text(encoding="utf-8")


def build_payload(
    tokenizer,
    model_key: str,
    system_prompt: str,
    user_prompt: str,
) -> tuple[str, bool]:
    style = MODEL_REGISTRY[model_key]["style"]
    if style == "plain_base_model":
        prompt = (
            "### Task\n"
            "You are writing a grounded biomedical machine-learning report.\n\n"
            f"{system_prompt}\n\n"
            "### Input\n"
            f"{user_prompt}\n\n"
            "### Report\n"
        )
        return prompt, False

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    if getattr(tokenizer, "chat_template", None):
        try:
            rendered = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
            )
            return rendered, True
        except Exception:
            pass

    merged_user = f"{system_prompt}\n\n{user_prompt}"
    merged_messages = [{"role": "user", "content": merged_user}]
    if getattr(tokenizer, "chat_template", None):
        try:
            rendered = tokenizer.apply_chat_template(
                merged_messages,
                tokenize=False,
                add_generation_prompt=True,
            )
            return rendered, True
        except Exception:
            pass

    plain = (
        "### Instructions\n"
        f"{system_prompt}\n\n"
        "### Evidence\n"
        f"{user_prompt}\n\n"
        "### Report\n"
    )
    return plain, False


def extract_text(output: Any) -> str:
    if isinstance(output, str):
        return output
    if isinstance(output, list) and output:
        last = output[-1]
        if isinstance(last, dict) and "content" in last:
            return str(last["content"])
        return str(last)
    return str(output)


def cleanup_text(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"^\s*assistant\s*:?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^\s*```(?:markdown)?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```\s*$", "", cleaned)
    cleaned = cleaned.replace("<|endoftext|>", "").replace("<|eot_id|>", "")
    cleaned = re.sub(r"(?is)^.*?assistantfinal\s*", "", cleaned)
    heading_positions = [cleaned.find(heading) for heading in REQUIRED_HEADINGS if heading in cleaned]
    if heading_positions:
        cleaned = cleaned[min(heading_positions):]
    return cleaned.strip()


def resolve_generation_settings(args: argparse.Namespace, model_key: str) -> dict[str, Any]:
    generation = MODEL_REGISTRY[model_key]["generation"]
    max_new_tokens = args.max_new_tokens if args.max_new_tokens > 0 else generation["max_new_tokens"]
    temperature = args.temperature if args.temperature >= 0 else generation["temperature"]
    top_p = args.top_p if args.top_p > 0 else generation["top_p"]
    settings: dict[str, Any] = {
        "max_new_tokens": int(max_new_tokens),
        "temperature": float(temperature),
        "top_p": float(top_p),
        "repetition_penalty": float(generation.get("repetition_penalty", 1.0)),
        "no_repeat_ngram_size": int(generation.get("no_repeat_ngram_size", 0)),
        "context_margin": int(generation.get("context_margin", 32)),
    }
    return settings


def tokenize_prompt(tokenizer, prompt_text: str, max_input_tokens: int | None):
    old_side = getattr(tokenizer, "truncation_side", "right")
    if max_input_tokens is not None:
        tokenizer.truncation_side = "left"
    try:
        return tokenizer(
            prompt_text,
            return_tensors="pt",
            truncation=max_input_tokens is not None,
            max_length=max_input_tokens,
        )
    finally:
        tokenizer.truncation_side = old_side


def resolve_model_load_kwargs(spec: dict[str, Any], dtype: Any, torch_module) -> dict[str, Any]:
    kwargs: dict[str, Any] = {
        "local_files_only": True,
        "trust_remote_code": True,
        "dtype": dtype,
        "low_cpu_mem_usage": True,
    }
    if torch_module.cuda.is_available():
        if spec.get("load_strategy") == "single_gpu":
            kwargs["device_map"] = {"": 0}
        else:
            kwargs["device_map"] = "auto"
    return kwargs


def build_run_markdown(model_key: str, records: list[dict[str, Any]]) -> str:
    lines = [f"# Generated Reports - {model_key}", ""]
    for rec in records:
        lines.append(f"## {rec['report_title']}")
        lines.append(f"_Source evidence: {rec['evidence_id']}_")
        lines.append("")
        lines.append(rec["report_markdown"].strip())
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = parse_args()

    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

    spec = MODEL_REGISTRY[args.model_key]
    model_path = Path(spec["path"]).resolve()
    reports_path = Path(args.reports).resolve()
    results_root = Path(args.results_root).resolve()
    output_dir = Path(args.output_root).resolve() / slugify(args.model_key)
    prompts_dir = output_dir / "prompts"

    ensure_output_dir(output_dir, overwrite=args.overwrite)
    prompts_dir.mkdir(parents=True, exist_ok=True)

    reports = read_jsonl(reports_path)
    if args.max_reports > 0:
        reports = reports[: args.max_reports]
    context = load_global_context(results_root)
    generation_settings = resolve_generation_settings(args, args.model_key)

    run_meta: dict[str, Any] = {
        "model_key": args.model_key,
        "model_path": str(model_path),
        "reports_path": str(reports_path),
        "results_root": str(results_root),
        "max_reports": len(reports),
        "max_new_tokens": generation_settings["max_new_tokens"],
        "temperature": generation_settings["temperature"],
        "top_p": generation_settings["top_p"],
        "dry_run": bool(args.dry_run),
        "started_at_unix": time.time(),
        "global_context": asdict(context),
        "prompt_profile": spec["prompt_profile"],
        "generation_profile": generation_settings,
    }

    import torch

    AutoModelForCausalLM, AutoTokenizer = load_transformers()
    tokenizer = AutoTokenizer.from_pretrained(
        model_path,
        local_files_only=True,
        trust_remote_code=True,
    )
    configure_tokenizer(tokenizer, model_path)

    prompt_payloads: list[dict[str, Any]] = []
    for report in reports:
        system_prompt = build_system_prompt(args.model_key)
        user_prompt = build_user_prompt(report, context, args.model_key)
        rendered_prompt, used_chat = build_payload(
            tokenizer=tokenizer,
            model_key=args.model_key,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )
        prompt_token_count = len(
            tokenizer(rendered_prompt, add_special_tokens=False)["input_ids"]
        )
        prompt_payloads.append(
            {
                "report_id": report["report_id"],
                "title": report_title(report),
                "evidence_id": report["evidence_id"],
                "source_report": report,
                "system_prompt": system_prompt,
                "user_prompt": user_prompt,
                "rendered_prompt": rendered_prompt,
                "used_chat_payload": bool(used_chat),
                "prompt_token_count": int(prompt_token_count),
            }
        )

    for payload in prompt_payloads:
        prompt_file = prompts_dir / f"{payload['report_id']}.txt"
        prompt_file.write_text(
            f"[SYSTEM]\n{payload['system_prompt']}\n\n[USER]\n{payload['user_prompt']}\n",
            encoding="utf-8",
        )

    if args.dry_run:
        dryrun_records = [
            {
                "report_id": payload["report_id"],
                "evidence_id": payload["evidence_id"],
                "report_title": payload["title"],
                "model_key": args.model_key,
                "prompt_token_count": payload["prompt_token_count"],
                "report_markdown": "_Dry run only: prompt written, generation skipped._",
            }
            for payload in prompt_payloads
        ]
        (output_dir / "reports.jsonl").write_text(
            "\n".join(json.dumps(rec, ensure_ascii=True) for rec in dryrun_records) + "\n",
            encoding="utf-8",
        )
        (output_dir / "reports.md").write_text(
            build_run_markdown(args.model_key, dryrun_records),
            encoding="utf-8",
        )
        run_meta["finished_at_unix"] = time.time()
        run_meta["status"] = "dry_run"
        (output_dir / "run_metadata.json").write_text(
            json.dumps(run_meta, indent=2) + "\n",
            encoding="utf-8",
        )
        return

    dtype = resolve_dtype(torch)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        **resolve_model_load_kwargs(spec, dtype, torch),
    )

    run_meta["torch_version"] = torch.__version__
    run_meta["cuda_available"] = bool(torch.cuda.is_available())
    run_meta["device_count"] = int(torch.cuda.device_count())
    if torch.cuda.is_available():
        run_meta["devices"] = [
            {
                "index": idx,
                "name": torch.cuda.get_device_name(idx),
                "total_memory": int(torch.cuda.get_device_properties(idx).total_memory),
            }
            for idx in range(torch.cuda.device_count())
        ]

    generate_kwargs: dict[str, Any] = {
        "max_new_tokens": generation_settings["max_new_tokens"],
        "pad_token_id": tokenizer.pad_token_id,
        "eos_token_id": tokenizer.eos_token_id,
        "repetition_penalty": generation_settings["repetition_penalty"],
    }
    if generation_settings["no_repeat_ngram_size"] > 0:
        generate_kwargs["no_repeat_ngram_size"] = generation_settings["no_repeat_ngram_size"]
    if generation_settings["temperature"] > 0:
        generate_kwargs.update(
            {
                "do_sample": True,
                "temperature": generation_settings["temperature"],
                "top_p": generation_settings["top_p"],
            }
        )
    else:
        generate_kwargs["do_sample"] = False

    records: list[dict[str, Any]] = []
    jsonl_path = output_dir / "reports.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as fout:
        for payload in prompt_payloads:
            context_window = spec.get("context_window")
            max_input_tokens = None
            if context_window:
                max_input_tokens = max(
                    256,
                    int(context_window) - generate_kwargs["max_new_tokens"] - generation_settings["context_margin"],
                )

            encoded = tokenize_prompt(tokenizer, payload["rendered_prompt"], max_input_tokens)
            input_ids = encoded["input_ids"]
            attention_mask = encoded["attention_mask"]
            input_length = int(input_ids.shape[-1])

            effective_max_new_tokens = generate_kwargs["max_new_tokens"]
            if context_window:
                room = int(context_window) - input_length - generation_settings["context_margin"]
                effective_max_new_tokens = max(64, min(effective_max_new_tokens, room))

            call_kwargs = dict(generate_kwargs)
            call_kwargs["max_new_tokens"] = effective_max_new_tokens
            if torch.cuda.is_available():
                input_ids = input_ids.to("cuda:0")
                attention_mask = attention_mask.to("cuda:0")

            with torch.inference_mode():
                output_ids = model.generate(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    **call_kwargs,
                )

            new_tokens = output_ids[0, input_length:]
            raw_output = tokenizer.decode(new_tokens, skip_special_tokens=True)
            report_markdown = cleanup_text(raw_output)

            record = {
                "report_id": payload["report_id"],
                "evidence_id": payload["evidence_id"],
                "report_title": payload["title"],
                "model_key": args.model_key,
                "model_path": str(model_path),
                "report_markdown": report_markdown,
                "raw_output": raw_output,
                "used_chat_payload": payload["used_chat_payload"],
                "prompt_token_count": payload["prompt_token_count"],
                "input_token_count": input_length,
                "max_new_tokens_used": effective_max_new_tokens,
                "generated_at_unix": time.time(),
            }
            fout.write(json.dumps(record, ensure_ascii=True) + "\n")
            records.append(record)

    markdown_path = output_dir / "reports.md"
    markdown_path.write_text(build_run_markdown(args.model_key, records), encoding="utf-8")

    run_meta["finished_at_unix"] = time.time()
    run_meta["status"] = "completed"
    run_meta["n_reports_written"] = len(records)
    (output_dir / "run_metadata.json").write_text(
        json.dumps(run_meta, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
