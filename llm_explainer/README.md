# LLM Explainer

This folder runs local Hugging Face models against the DEM report bundle in `results/`.

Files:

- `build_shap_reports.py`
  Builds a SHAP-grounded 25-case input bundle from `results/tuning/shap_values.parquet` and writes:
  - `llm_explainer/shap_sample_reports.jsonl`
  - `llm_explainer/shap_sample_reports.md`
- `build_instruction_pairs.py`
  Reads each `RPT` section from `llm_explainer/shap_sample_reports.md`, combines it with the structured JSONL metadata, calls an OpenAI-compatible API model such as `models--meta-llama--Llama-3.3-70B-Instruct`, and writes instruction pairs to JSONL.
- `generate_reports.py`
  Runs one local model against the structured SHAP-grounded bundle and writes per-model outputs under `llm_explainer/outputs/<model-slug>/`.
- `build_comparison.py`
  Merges all completed per-model outputs into one side-by-side markdown file at `llm_explainer/model_comparison.md`.
- `submit_all_models.sh`
  Submits five LSF jobs in parallel, one GPU per model, plus a dependent CPU job that builds the final comparison markdown after all model jobs finish.

Typical usage:

```bash
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python llm_explainer/build_shap_reports.py
./llm_explainer/submit_all_models.sh
```

To build instruction pairs through an external API:

```bash
export LLM_API_BASE_URL="https://your-host.example/v1"
export LLM_API_KEY="your-key"
/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python \
  llm_explainer/build_instruction_pairs.py \
  --model models--meta-llama--Llama-3.3-70B-Instruct
```

Outputs:

- `llm_explainer/outputs/<model-slug>/reports.jsonl`
- `llm_explainer/outputs/<model-slug>/reports.md`
- `llm_explainer/outputs/<model-slug>/run_metadata.json`
- `llm_explainer/model_comparison.md`
- `llm_explainer/job_manifest.tsv`
- `llm_explainer/logs/*.out`
- `llm_explainer/logs/*.err`

Notes:

- All model weights are loaded from `/sc/arion/scratch/cuiz02/hf_cache/transformers`.
- The default input is `llm_explainer/shap_sample_reports.jsonl`, which is built from TreeSHAP outputs plus local metadata and cohort summaries.
- The prompt uses the structured report bundle plus auxiliary metrics from `results/tuning` and `results/rf_plots`.
- The generator treats `metrics_dem.json` as training-fit context only, not held-out model performance.
