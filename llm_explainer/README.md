# LLM Explainer

This folder runs local Hugging Face models against the DEM report bundle in `results/`.

Files:

- `build_shap_reports.py`
  Builds a SHAP-grounded 25-case input bundle from `results/tuning/shap_values.parquet` and writes:
  - `llm_explainer/shap_sample_reports.jsonl`
  - `llm_explainer/shap_sample_reports.md`

  Accepts `--target-label` (e.g. `"log10(IC50)"`) so the same script can generate
  reports against either the legacy AUC target or the new IC50 pipeline. Pair
  `--target-label` with `--interpretation-scale` to rescale the "exceptional /
  local" response-interpretation thresholds when the target std differs from
  the AUC baseline (~2.6). When unset, the scale defaults to `1.0` for AUC and
  to `std(y) / 2.6` for anything else. Use `--selection-mode from_csv
  --selection-csv <path>` to load a pre-curated case list (see
  `select_knn_cases.py` below); each row in that CSV may carry its own
  `selection_tag` and `selection_reason` values.
- `select_knn_cases.py`
  Rebuilds the RF feature matrix (standardised gene expression + Morgan
  fingerprints via `train.load_data.load_merged`), computes `k`-nearest-
  neighbor mean response per sample, and writes a curated CSV of
  `outlier_knn` + `normal_knn` cases directly consumable by
  `build_shap_reports.py --selection-mode from_csv`. Defaults to `k=20`,
  25 outliers + 25 normals.
- `select_explainable_cases.py`
  The preferred curation for LLM-written reports on log10(IC50). Combines the
  RF out-of-fold residual (from `train/compute_oof_predictions.py`) with the
  KNN-in-feature-space residual (from `select_knn_cases.py`) as a z-score
  sum, applies quality filters (`replicate_std < 0.5`, `per_drug_r2 ≥ 0.20`,
  drug must have an annotated `gene_symbol_of_protein_target`, cell line must
  have a non-null `OncotreeLineage`), and enforces diversity caps
  (≤2 per drug, ≤2 per lineage, ≤1 per drug-lineage pair). Emits
  `abnormal_combined` (largest score; model *and* neighborhood were both
  surprised) + `normal_combined` (smallest; both got it right) rows in the
  same CSV schema as `select_knn_cases.py`. See
  `run_ic50_explainable.sh` for the end-to-end LSF wrapper.
- `build_instruction_pairs.py`
  Reads each `RPT` section from `llm_explainer/shap_sample_reports.md`, combines it with the structured JSONL metadata, calls an OpenAI-compatible API model such as `models--meta-llama--Llama-3.3-70B-Instruct`, and writes instruction pairs to JSONL.
- `prepare_sft_data.py`
  Splits a larger SHAP-grounded report bundle into train/val/test, keeps the input in RPT markdown format, and writes teacher-generation request bundles for held-out SFT experiments.
- `generate_teacher_pairs_local.py`
  Loads one local teacher model once, reads split-specific request bundles from `prepare_sft_data.py`, and writes split-specific instruction-pair JSONL plus markdown outputs.
- `build_sft_dataset.py`
  Converts teacher-generated instruction pairs into chat-style and Alpaca-style JSONL exports for SFT.
- `generate_reports.py`
  Runs one local model against the structured SHAP-grounded bundle and writes per-model outputs under `llm_explainer/outputs/<model-slug>/`. It can also evaluate a fine-tuned checkpoint or PEFT adapter through `--model-path` / `--adapter-path`.
- `build_comparison.py`
  Merges all completed per-model outputs into one side-by-side markdown file at `llm_explainer/model_comparison.md`.
- `compare_sft_runs.py`
  Compares a base-model held-out run against an SFT held-out run and optionally scores both against teacher references.
- `submit_all_models.sh`
  Submits five LSF jobs in parallel, one GPU per model, plus a dependent CPU job that builds the final comparison markdown after all model jobs finish.
- `submit_teacher_local.sh`
  Submits one 5-GPU LSF job that runs the local 70B teacher over the prepared `train` / `val` / `test` request splits.

Typical usage:

```bash
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python llm_explainer/build_shap_reports.py
./llm_explainer/submit_all_models.sh
```

### IC50 pipeline (log10(IC50) target)

The IC50 retraining run lives under `results_ic50/` (see
`train/run_ic50_pipeline.sh` and `preprocess/build_ic50_pairs.py`). Once that
pipeline has finished, build the SHAP-grounded explainer bundle for the new
target:

```bash
# Full set of diverse cases (same selection logic as AUC, new target label).
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/build_shap_reports.py \
  --shap-values results_ic50/tuning/shap_values.parquet \
  --pairs data/processed/pairs_ic50.csv \
  --per-drug-r2 results_ic50/rf_plots/per_drug_r2.csv \
  --gene-signatures results_ic50/rf_plots/gene_signature_counts.csv \
  --target-label 'log10(IC50)' \
  --out-jsonl llm_explainer/shap_sample_reports_ic50.jsonl \
  --out-md    llm_explainer/shap_sample_reports_ic50.md
```

And the 25-outlier + 25-normal KNN-curated bundle (k=20 in the RF feature
space, as a separate deliverable alongside the standard 25-case bundle):

```bash
# 1. Compute KNN residuals and export the curated case list.
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/select_knn_cases.py \
  --data-dir data/processed \
  --pairs pairs_ic50.csv \
  --cell-features cell_features_selected_l1000_union.csv \
  --drug-fingerprints drug_fingerprints.csv \
  --target-label 'log10(IC50)' \
  --k 20 --n-outlier 25 --n-normal 25 \
  --out-csv llm_explainer/knn_curated_ic50.csv \
  --out-all-csv llm_explainer/knn_residuals_ic50.csv

# 2. Build the SHAP-grounded report bundle off of that curated list.
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/build_shap_reports.py \
  --shap-values results_ic50/tuning/shap_values.parquet \
  --pairs data/processed/pairs_ic50.csv \
  --per-drug-r2 results_ic50/rf_plots/per_drug_r2.csv \
  --gene-signatures results_ic50/rf_plots/gene_signature_counts.csv \
  --target-label 'log10(IC50)' \
   --selection-mode from_csv \
  --selection-csv llm_explainer/knn_curated_ic50.csv \
  --num-reports 0 \
  --out-jsonl llm_explainer/shap_sample_reports_ic50_knn50.jsonl \
  --out-md    llm_explainer/shap_sample_reports_ic50_knn50.md
```

Each case in `shap_sample_reports_ic50_knn50.jsonl` carries
`"selection_tag": "outlier_knn"` or `"normal_knn"` plus a
`selection_reason` that records the observed `log10(IC50)` vs. its 20-NN
neighbor mean, so downstream prompts can contrast the two buckets.

### Preferred bundle for LLM narration: combined-residual curation

The `outlier_knn` bucket above often selects curve-fit artifacts on obscure
probe compounds (extreme `|Δ|` but uninterpretable drug), which is bad input
for an LLM asked to explain *why* the cell responded unexpectedly. The
`select_explainable_cases.py` pipeline fixes that by requiring the model
residual, the neighborhood residual, and the drug+lineage metadata to all be
informative. Run end-to-end via LSF:

```bash
LSF_SUBMIT=1 FOLLOW_N_JOBS=16 FOLLOW_MEM_MB=65536 \
  ./llm_explainer/run_ic50_explainable.sh
```

Or step-by-step from the repo root:

```bash
# 1. Out-of-fold RF predictions (5-fold CV, same hyperparams as the retrain).
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  train/compute_oof_predictions.py \
  --data-dir data/processed --pairs pairs_ic50.csv \
  --cell-features cell_features_selected_l1000_union.csv \
  --drug-fingerprints drug_fingerprints.csv \
  --n-estimators 100 --max-depth 10 --n-splits 5 --n-jobs 16 \
  --out-csv results_ic50/oof_predictions.csv

# 2. Combined-residual selector (reuses KNN residuals from select_knn_cases.py).
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/select_explainable_cases.py \
  --pairs data/processed/pairs_ic50.parquet \
  --oof-predictions results_ic50/oof_predictions.csv \
  --knn-residuals llm_explainer/knn_residuals_ic50.csv \
  --per-drug-r2 results_ic50/rf_plots/per_drug_r2.csv \
  --compound-meta data/CTRPv2/v21.meta.per_compound.txt \
  --model-csv data/DepMap/Model.csv \
  --target-label 'log10(IC50)' \
  --out-csv llm_explainer/explainable_curated_ic50.csv \
  --out-all-csv llm_explainer/explainable_scored_ic50.csv

# 3. Build the LLM-ready 50-case SHAP report bundle.
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/build_shap_reports.py \
  --shap-values results_ic50/tuning/shap_values.parquet \
  --pairs data/processed/pairs_ic50.csv \
  --per-drug-r2 results_ic50/rf_plots/per_drug_r2.csv \
  --gene-signatures results_ic50/rf_plots/gene_signature_counts.csv \
  --cell-features data/processed/cell_features_selected_l1000_union.csv \
  --target-label 'log10(IC50)' \
  --selection-mode from_csv \
  --selection-csv llm_explainer/explainable_curated_ic50.csv \
  --num-reports 0 \
  --out-jsonl llm_explainer/shap_sample_reports_ic50_explainable50.jsonl \
  --out-md    llm_explainer/shap_sample_reports_ic50_explainable50.md
```

Tunable knobs on the selector:

- `--min-per-drug-r2` (default 0.20) — raise to require stronger model signal.
- `--max-replicate-std` (default 0.5) — lower to drop noisier curve fits.
- `--no-require-annotated-target` — keep compounds without a gene target.
- `--max-per-drug`, `--max-per-lineage`, `--max-per-drug-lineage` — diversity
  caps inside each 25-case bucket.

Each row in the curated CSV (and the downstream JSONL) carries
`selection_tag ∈ {"abnormal_combined", "normal_combined"}` plus a
`selection_reason` that reports observed vs. OOF prediction vs. 20-NN mean,
the drug's known target, the cell line's lineage/disease, and the drug's
held-out per-drug R². That context is directly useful in the LLM prompt.

To build instruction pairs through an external API:

```bash
export LLM_API_BASE_URL="https://your-host.example/v1"
export LLM_API_KEY="your-key"
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/build_instruction_pairs.py \
  --model models--meta-llama--Llama-3.3-70B-Instruct
```

To prepare a larger teacher/SFT experiment with shorter RPT prompts:

```bash
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/build_shap_reports.py \
  --selection-mode top_error \
  --num-reports 500 \
  --out-jsonl llm_explainer/shap_teacher_500.jsonl \
  --out-md llm_explainer/shap_teacher_500.md

/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/prepare_sft_data.py \
  --reports-jsonl llm_explainer/shap_teacher_500.jsonl \
  --out-dir llm_explainer/sft_experiment_500 \
  --prompt-style short_rpt
```

Then call the teacher model on the split-specific request bundles.

External API route:

```bash
export LLM_API_BASE_URL="https://your-host.example/v1"
export LLM_API_KEY="your-key"
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/build_instruction_pairs.py \
  --prepared-requests-jsonl llm_explainer/sft_experiment_500/teacher_requests/train.jsonl \
  --out-jsonl llm_explainer/sft_experiment_500/teacher_pairs_train.jsonl \
  --model models--meta-llama--Llama-3.3-70B-Instruct
```

Local 70B route on this server:

```bash
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/generate_teacher_pairs_local.py \
  --experiment-dir llm_explainer/sft_experiment_500 \
  --teacher-model-key Llama-3.3-70B-Instruct \
  --out-dir llm_explainer/sft_experiment_500/teacher_pairs_local

./llm_explainer/submit_teacher_local.sh
```

After teacher generation, export SFT-ready JSONL:

```bash
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/build_sft_dataset.py \
  --train-pairs llm_explainer/sft_experiment_500/teacher_pairs_local/train.jsonl \
  --val-pairs llm_explainer/sft_experiment_500/teacher_pairs_local/val.jsonl \
  --out-dir llm_explainer/sft_experiment_500/sft_dataset
```

To compare a base run against an SFT adapter on the held-out test split:

```bash
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/generate_reports.py \
  --model-key Meta-Llama-3.1-8B-Instruct \
  --reports llm_explainer/sft_experiment_500/reports/test.jsonl \
  --output-subdir llama31_base_test \
  --run-label "Llama-3.1-8B Base Test"

/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/generate_reports.py \
  --model-key Meta-Llama-3.1-8B-Instruct \
  --reports llm_explainer/sft_experiment_500/reports/test.jsonl \
  --adapter-path /path/to/your/lora_adapter \
  --output-subdir llama31_sft_test \
  --run-label "Llama-3.1-8B SFT Test"

/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/compare_sft_runs.py \
  --reports llm_explainer/sft_experiment_500/reports/test.jsonl \
  --base-reports-jsonl llm_explainer/outputs/llama31_base_test/reports.jsonl \
  --sft-reports-jsonl llm_explainer/outputs/llama31_sft_test/reports.jsonl \
  --reference-pairs-jsonl llm_explainer/sft_experiment_500/teacher_pairs_local/test.jsonl \
  --base-label "Base" \
  --sft-label "SFT" \
  --out-file llm_explainer/sft_experiment_500/sft_vs_base.md
```

Outputs:

- `llm_explainer/outputs/<model-slug>/reports.jsonl`
- `llm_explainer/outputs/<model-slug>/reports.md`
- `llm_explainer/outputs/<model-slug>/run_metadata.json`
- `llm_explainer/model_comparison.md`
- `llm_explainer/job_manifest.tsv`
- `llm_explainer/logs/*.out`
- `llm_explainer/logs/*.err`
- `llm_explainer/sft_experiment*/split_manifest.json`
- `llm_explainer/sft_experiment*/teacher_requests/*.jsonl`
- `llm_explainer/sft_experiment*/teacher_pairs_local/*.jsonl`
- `llm_explainer/sft_experiment*/teacher_pairs_local/*.md`
- `llm_explainer/sft_experiment*/sft_dataset/*.jsonl`
- `llm_explainer/sft_experiment*/sft_vs_base.md`

Notes:

- All model weights are loaded from `/sc/arion/scratch/cuiz02/hf_cache/transformers`.
- The default input is `llm_explainer/shap_sample_reports.jsonl`, which is built from TreeSHAP outputs plus local metadata and cohort summaries.
- The prompt uses the structured report bundle plus auxiliary metrics from `results/tuning` and `results/rf_plots`.
- The generator treats `metrics_dem.json` as training-fit context only, not held-out model performance.
- For SFT experiments, prefer `prepare_sft_data.py --prompt-style short_rpt` so the student model learns on a shorter but still RPT-shaped input format.
- For honest evaluation, compare base and SFT runs on `reports/test.jsonl`, not on the train/val splits used to build the teacher dataset.
- Cache-style Hugging Face directories such as `models--meta-llama--Llama-3.3-70B-Instruct` are resolved automatically to their active snapshot path.
- The checked conda environment had `torch`, `transformers`, `datasets`, and `accelerate`, but not `peft` or `trl`, so adapter training itself still needs those runtime dependencies installed.
