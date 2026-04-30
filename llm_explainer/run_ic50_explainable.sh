#!/usr/bin/env bash
# End-to-end pipeline for the "Option B" curated bundle on log10(IC50):
#   1. compute OOF RF predictions (5-fold CV)
#   2. combine OOF residuals + KNN residuals + quality filters + diversity caps
#      -> llm_explainer/explainable_curated_ic50.csv
#   3. rebuild SHAP report bundle from that CSV

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="${PYTHON:-/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python}"

DATA_DIR="${DATA_DIR:-data/processed}"
PAIRS_FILE="${PAIRS_FILE:-pairs_ic50.csv}"
PAIRS_PATH="${PAIRS_PATH:-data/processed/pairs_ic50.parquet}"
CELL_FEATURES="${CELL_FEATURES:-cell_features_selected_l1000_union.csv}"
DRUG_FINGERPRINTS="${DRUG_FINGERPRINTS:-drug_fingerprints.csv}"
CELL_FEAT_PATH="data/processed/$CELL_FEATURES"

RESULTS_ROOT="${RESULTS_ROOT:-results_ic50}"
SHAP_VALUES="$RESULTS_ROOT/tuning/shap_values.parquet"
PER_DRUG_R2="$RESULTS_ROOT/rf_plots/per_drug_r2.csv"
GENE_SIGS="$RESULTS_ROOT/rf_plots/gene_signature_counts.csv"
OOF_CSV="${OOF_CSV:-$RESULTS_ROOT/oof_predictions.csv}"

KNN_RESIDUALS="${KNN_RESIDUALS:-llm_explainer/knn_residuals_ic50.csv}"
COMPOUND_META="${COMPOUND_META:-data/CTRPv2/v21.meta.per_compound.txt}"
MODEL_CSV="${MODEL_CSV:-data/DepMap/Model.csv}"

TARGET_LABEL="${TARGET_LABEL:-log10(IC50)}"
N_JOBS="${N_JOBS:-16}"
N_ESTIMATORS="${N_ESTIMATORS:-100}"
MAX_DEPTH="${MAX_DEPTH:-10}"
N_SPLITS="${N_SPLITS:-5}"

CURATED_CSV="${CURATED_CSV:-llm_explainer/explainable_curated_ic50.csv}"
SCORED_CSV="${SCORED_CSV:-llm_explainer/explainable_scored_ic50.csv}"
OUT_JSONL="${OUT_JSONL:-llm_explainer/shap_sample_reports_ic50_explainable50.jsonl}"
OUT_MD="${OUT_MD:-llm_explainer/shap_sample_reports_ic50_explainable50.md}"

LSF_SUBMIT="${LSF_SUBMIT:-0}"
if [[ "$LSF_SUBMIT" == "1" ]]; then
  QUEUE="${QUEUE:-premium}"
  PROJECT="${PROJECT:-acc_lin_lab}"
  LOG_DIR="${LOG_DIR:-$ROOT/llm_explainer/logs}"
  mkdir -p "$LOG_DIR"
  SELF="$(readlink -f "${BASH_SOURCE[0]}")"
  FOLLOW_N_JOBS="${FOLLOW_N_JOBS:-16}"
  FOLLOW_MEM_MB="${FOLLOW_MEM_MB:-65536}"
  FOLLOW_WALL_MIN="${FOLLOW_WALL_MIN:-240}"

  unset LSF_SUBMIT
  export LSF_SUBMIT=0

  bsub \
    -P "$PROJECT" \
    -q "$QUEUE" \
    -J ic50_explainable \
    -n "$FOLLOW_N_JOBS" \
    -W "$FOLLOW_WALL_MIN" \
    -R "span[hosts=1] rusage[mem=${FOLLOW_MEM_MB}]" \
    -oo "$LOG_DIR/ic50-explainable.%J.out" \
    -eo "$LOG_DIR/ic50-explainable.%J.err" \
    -env "none" \
    bash "$SELF"
  exit 0
fi

cd "$ROOT"
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1

echo "[$(date +%T)] ROOT=$ROOT  N_JOBS=$N_JOBS"
echo "[$(date +%T)] OOF target: $OOF_CSV"

# ----- 1. OOF predictions -----
if [[ -s "$OOF_CSV" && -z "${FORCE_OOF:-}" ]]; then
  echo "[$(date +%T)] Reusing existing OOF predictions: $OOF_CSV (set FORCE_OOF=1 to recompute)"
else
  echo "[$(date +%T)] === 1. compute_oof_predictions.py ==="
  "$PYTHON" train/compute_oof_predictions.py \
    --data-dir "$DATA_DIR" \
    --pairs "$PAIRS_FILE" \
    --cell-features "$CELL_FEATURES" \
    --drug-fingerprints "$DRUG_FINGERPRINTS" \
    --n-estimators "$N_ESTIMATORS" \
    --max-depth "$MAX_DEPTH" \
    --n-splits "$N_SPLITS" \
    --n-jobs "$N_JOBS" \
    --out-csv "$OOF_CSV"
fi

# ----- 2. combined-residual selector -----
echo "[$(date +%T)] === 2. select_explainable_cases.py ==="
"$PYTHON" llm_explainer/select_explainable_cases.py \
  --pairs "$PAIRS_PATH" \
  --oof-predictions "$OOF_CSV" \
  --knn-residuals "$KNN_RESIDUALS" \
  --per-drug-r2 "$PER_DRUG_R2" \
  --compound-meta "$COMPOUND_META" \
  --model-csv "$MODEL_CSV" \
  --target-label "$TARGET_LABEL" \
  --out-csv "$CURATED_CSV" \
  --out-all-csv "$SCORED_CSV"

# ----- 3. rebuild SHAP report bundle -----
echo "[$(date +%T)] === 3. build_shap_reports.py (explainable curated 50) ==="
"$PYTHON" llm_explainer/build_shap_reports.py \
  --shap-values "$SHAP_VALUES" \
  --pairs "data/processed/pairs_ic50.csv" \
  --per-drug-r2 "$PER_DRUG_R2" \
  --gene-signatures "$GENE_SIGS" \
  --cell-features "$CELL_FEAT_PATH" \
  --target-label "$TARGET_LABEL" \
  --selection-mode from_csv \
  --selection-csv "$CURATED_CSV" \
  --num-reports 0 \
  --out-jsonl "$OUT_JSONL" \
  --out-md "$OUT_MD"

echo "[$(date +%T)] Done. Outputs:"
for f in "$OOF_CSV" "$CURATED_CSV" "$SCORED_CSV" "$OUT_JSONL" "$OUT_MD"; do
  [[ -f "$f" ]] && printf "  %s  (%d lines)\n" "$f" "$(wc -l < "$f")"
done
