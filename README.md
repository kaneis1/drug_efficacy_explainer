# drug_efficacy_explainer

Reproduce drug_efficacy and use an LLM to explain the Random Forest /
TreeSHAP outputs.

## Pipelines

### AUC (legacy)

* Inputs: `data/processed/pairs.csv` (AUC target)
* Training scripts: `train/*.py`
* Outputs: `results/tuning/`, `results/rf_plots/`, `results/dem/`

### log10(IC50) (current)

* Preprocessing: [`preprocess/build_ic50_pairs.py`](preprocess/build_ic50_pairs.py)
  joins CTRPv2.0 curve-fit parameters (`v20.data.curves_post_qc.txt`) with the
  v21 per-compound/per-cell metadata and DepMap `Model.csv`, applies the
  `_crosses_50 & _valid_math` filter, and computes
  `log10_ic50 = (p1 + log10(p3/(0.5-p4) - 1)/p2) * log10(2)` before averaging
  per `(ModelID, cpd_name)` pair. Output: `data/processed/pairs_ic50.{parquet,csv}`.
* Training + SHAP + DEM: [`train/run_ic50_pipeline.sh`](train/run_ic50_pipeline.sh)
  wires every step of the existing `train/` scripts onto the IC50 pairs and
  writes all artifacts under `results_ic50/`. Run it locally or submit with
  `./train/run_ic50_pipeline.sh --submit` (single LSF job, 128 GB / 8 cores).
* LLM explainer: see [`llm_explainer/README.md`](llm_explainer/README.md), in
  particular the "IC50 pipeline (log10(IC50) target)" section, which covers
  both the standard 25-case diverse bundle and the
  `select_knn_cases.py`-powered 25 outlier + 25 normal curated bundle.
