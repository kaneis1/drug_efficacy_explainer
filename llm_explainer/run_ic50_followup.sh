#!/usr/bin/env bash
# Follow-up pipeline for the log10(IC50) retrain.
#
# Consumes results_ic50/tuning/shap_values.parquet + results_ic50/rf_plots/*
# and produces:
#   * llm_explainer/knn_curated_ic50.csv            (25 outliers + 25 normals, k=20)
#   * llm_explainer/knn_residuals_ic50.csv          (full per-sample residual table)
#   * llm_explainer/shap_sample_reports_ic50.jsonl  (full diverse-25 bundle)
#   * llm_explainer/shap_sample_reports_ic50.md
#   * llm_explainer/shap_sample_reports_ic50_knn50.jsonl  (50 curated KNN cases)
#   * llm_explainer/shap_sample_reports_ic50_knn50.md
#
# Intended to be chained after train/run_ic50_pipeline.sh via:
#   bsub -w "ended(<TRAIN_JOBID>)" ...
#
# Usage (local or inside LSF):
#   ./llm_explainer/run_ic50_followup.sh
#   LSF_SUBMIT=1 TRAIN_JOBID=238822772 ./llm_explainer/run_ic50_followup.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="${PYTHON:-/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python}"

DATA_DIR="${DATA_DIR:-data/processed}"
PAIRS_FILE="${PAIRS_FILE:-pairs_ic50.csv}"
PAIRS_PATH="${PAIRS_PATH:-data/processed/pairs_ic50.csv}"
CELL_FEATURES="${CELL_FEATURES:-cell_features_selected_l1000_union.csv}"
DRUG_FINGERPRINTS="${DRUG_FINGERPRINTS:-drug_fingerprints.csv}"
RESULTS_ROOT="${RESULTS_ROOT:-results_ic50}"
SHAP_VALUES="$RESULTS_ROOT/tuning/shap_values.parquet"
PER_DRUG_R2="$RESULTS_ROOT/rf_plots/per_drug_r2.csv"
GENE_SIGS="$RESULTS_ROOT/rf_plots/gene_signature_counts.csv"
CELL_META="data/CTRPv2/v21.meta.per_cell_line.txt"
CPD_META="data/CTRPv2/v21.meta.per_compound.txt"
CELL_FEAT_PATH="data/processed/$CELL_FEATURES"

N_JOBS="${N_JOBS:-16}"
KNN_K="${KNN_K:-20}"
KNN_OUTLIER="${KNN_OUTLIER:-25}"
KNN_NORMAL="${KNN_NORMAL:-25}"
TARGET_LABEL="${TARGET_LABEL:-log10(IC50)}"

KNN_CSV="${KNN_CSV:-llm_explainer/knn_curated_ic50.csv}"
KNN_ALL_CSV="${KNN_ALL_CSV:-llm_explainer/knn_residuals_ic50.csv}"
OUT_JSONL_FULL="${OUT_JSONL_FULL:-llm_explainer/shap_sample_reports_ic50.jsonl}"
OUT_MD_FULL="${OUT_MD_FULL:-llm_explainer/shap_sample_reports_ic50.md}"
OUT_JSONL_KNN="${OUT_JSONL_KNN:-llm_explainer/shap_sample_reports_ic50_knn50.jsonl}"
OUT_MD_KNN="${OUT_MD_KNN:-llm_explainer/shap_sample_reports_ic50_knn50.md}"

LSF_SUBMIT="${LSF_SUBMIT:-0}"
TRAIN_JOBID="${TRAIN_JOBID:-}"

# Important: clear the submit flag *before* calling bsub so that the copy of
# this script that LSF runs inside the dependent job does NOT re-enter the
# submit branch and infinitely chain-submit itself.
if [[ "$LSF_SUBMIT" == "1" ]]; then
  QUEUE="${QUEUE:-premium}"
  PROJECT="${PROJECT:-acc_lin_lab}"
  LOG_DIR="${LOG_DIR:-$ROOT/llm_explainer/logs}"
  mkdir -p "$LOG_DIR"
  SELF="$(readlink -f "${BASH_SOURCE[0]}")"
  FOLLOW_N_JOBS="${FOLLOW_N_JOBS:-8}"
  FOLLOW_MEM_MB="${FOLLOW_MEM_MB:-65536}"
  FOLLOW_WALL_MIN="${FOLLOW_WALL_MIN:-360}"

  dep=""
  if [[ -n "$TRAIN_JOBID" ]]; then
    # Use 'ended' so we still attempt the followup even if a stage silently
    # errors — the downstream scripts will fail fast and surface the problem.
    dep="-w ended(${TRAIN_JOBID})"
  fi

  unset LSF_SUBMIT
  export LSF_SUBMIT=0

  # shellcheck disable=SC2086
  bsub \
    -P "$PROJECT" \
    -q "$QUEUE" \
    -J ic50_followup \
    -n "$FOLLOW_N_JOBS" \
    -W "$FOLLOW_WALL_MIN" \
    -R "span[hosts=1] rusage[mem=${FOLLOW_MEM_MB}]" \
    -oo "$LOG_DIR/ic50-followup.%J.out" \
    -eo "$LOG_DIR/ic50-followup.%J.err" \
    -env "none" \
    $dep \
    bash "$SELF"
  exit 0
fi

cd "$ROOT"

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1

echo "[$(date +%T)] ROOT=$ROOT"
echo "[$(date +%T)] SHAP_VALUES=$SHAP_VALUES"
echo "[$(date +%T)] PER_DRUG_R2=$PER_DRUG_R2"
echo "[$(date +%T)] PAIRS=$PAIRS_PATH"

missing=0
for f in "$SHAP_VALUES" "$PER_DRUG_R2" "$GENE_SIGS" "$PAIRS_PATH" "$CELL_META" "$CPD_META" "$CELL_FEAT_PATH"; do
  if [[ ! -s "$f" ]]; then
    echo "MISSING: $f" >&2
    missing=1
  fi
done
if [[ "$missing" == "1" ]]; then
  echo "[$(date +%T)] Training outputs not present yet — aborting follow-up." >&2
  exit 2
fi

echo "[$(date +%T)] === 1. select_knn_cases.py (k=${KNN_K}) ==="
"$PYTHON" llm_explainer/select_knn_cases.py \
  --data-dir "$DATA_DIR" \
  --pairs "$PAIRS_FILE" \
  --cell-features "$CELL_FEATURES" \
  --drug-fingerprints "$DRUG_FINGERPRINTS" \
  --target-label "$TARGET_LABEL" \
  --k "$KNN_K" \
  --n-outlier "$KNN_OUTLIER" \
  --n-normal "$KNN_NORMAL" \
  --n-jobs "$N_JOBS" \
  --out-csv "$KNN_CSV" \
  --out-all-csv "$KNN_ALL_CSV"

echo "[$(date +%T)] === 2. build_shap_reports.py (full diverse bundle) ==="
"$PYTHON" llm_explainer/build_shap_reports.py \
  --shap-values "$SHAP_VALUES" \
  --pairs "$PAIRS_PATH" \
  --per-drug-r2 "$PER_DRUG_R2" \
  --gene-signatures "$GENE_SIGS" \
  --cell-features "$CELL_FEAT_PATH" \
  --target-label "$TARGET_LABEL" \
  --out-jsonl "$OUT_JSONL_FULL" \
  --out-md "$OUT_MD_FULL"

echo "[$(date +%T)] === 3. build_shap_reports.py (KNN-curated 50 cases) ==="
"$PYTHON" llm_explainer/build_shap_reports.py \
  --shap-values "$SHAP_VALUES" \
  --pairs "$PAIRS_PATH" \
  --per-drug-r2 "$PER_DRUG_R2" \
  --gene-signatures "$GENE_SIGS" \
  --cell-features "$CELL_FEAT_PATH" \
  --target-label "$TARGET_LABEL" \
  --selection-mode from_csv \
  --selection-csv "$KNN_CSV" \
  --num-reports 0 \
  --out-jsonl "$OUT_JSONL_KNN" \
  --out-md "$OUT_MD_KNN"

echo "[$(date +%T)] Follow-up done. Summary:"
for f in "$KNN_CSV" "$OUT_JSONL_FULL" "$OUT_JSONL_KNN"; do
  if [[ -f "$f" ]]; then
    lines=$(wc -l < "$f")
    echo "  $f  ($lines lines)"
  fi
done
