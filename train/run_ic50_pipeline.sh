#!/usr/bin/env bash
# Retrain the full RF / SHAP / DEM pipeline on the log10(IC50) target.
#
# Inputs:
#   data/processed/pairs_ic50.csv            (from preprocess/build_ic50_pairs.py)
#   data/processed/cell_features_selected_l1000_union.csv
#   data/processed/drug_fingerprints.csv
#
# Outputs:
#   results_ic50/tuning/  (tuning CSVs + shap_values.parquet + fingerprint_importances)
#   results_ic50/rf_plots/  (per_drug_r2.csv, gene_signature_counts.csv, plots)
#   results_ic50/dem/  (dem_model.pkl, leaf_assignments, evidence.jsonl, sample_reports.jsonl)
#
# Usage:
#   ./train/run_ic50_pipeline.sh                 # run sequentially on the current host
#   ./train/run_ic50_pipeline.sh --submit        # submit as a single LSF job

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="${PYTHON:-/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python}"

DATA_DIR="${DATA_DIR:-data/processed}"
PAIRS_FILE="${PAIRS_FILE:-pairs_ic50.csv}"
CELL_FEATURES="${CELL_FEATURES:-cell_features_selected_l1000_union.csv}"
DRUG_FINGERPRINTS="${DRUG_FINGERPRINTS:-drug_fingerprints.csv}"
RESULTS_ROOT="${RESULTS_ROOT:-results_ic50}"
N_JOBS="${N_JOBS:-80}"
LSF_MEM_MB="${LSF_MEM_MB:-262144}"
LSF_WALL_MIN="${LSF_WALL_MIN:-1440}"
MAX_DEPTH="${MAX_DEPTH:-10}"
N_ESTIMATORS="${N_ESTIMATORS:-100}"
MIN_SAMPLES_PER_DRUG="${MIN_SAMPLES_PER_DRUG:-20}"

TUNING_DIR="$RESULTS_ROOT/tuning"
RF_PLOTS_DIR="$RESULTS_ROOT/rf_plots"
DEM_DIR="$RESULTS_ROOT/dem"

SUBMIT=0
for arg in "$@"; do
  case "$arg" in
    --submit) SUBMIT=1 ;;
    *) echo "Unknown arg: $arg" >&2; exit 2 ;;
  esac
done

if [[ "$SUBMIT" -eq 1 ]]; then
  QUEUE="${QUEUE:-premium}"
  PROJECT="${PROJECT:-acc_lin_lab}"
  LOG_DIR="${LOG_DIR:-$ROOT/train/logs}"
  mkdir -p "$LOG_DIR"
  SELF="$(readlink -f "${BASH_SOURCE[0]}")"
  bsub \
    -P "$PROJECT" \
    -q "$QUEUE" \
    -J ic50_rf_pipeline \
    -n "$N_JOBS" \
    -W "$LSF_WALL_MIN" \
    -R "span[hosts=1] rusage[mem=${LSF_MEM_MB}]" \
    -oo "$LOG_DIR/ic50-pipeline.%J.out" \
    -eo "$LOG_DIR/ic50-pipeline.%J.err" \
    bash "$SELF"
  exit 0
fi

cd "$ROOT"

# When sklearn uses joblib n_jobs=$N_JOBS, each worker can still fan out across
# all cores through OMP / OpenBLAS / MKL. Pin inner thread pools to 1 so we
# actually get $N_JOBS sklearn workers × 1 BLAS thread each.
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1

echo "[$(date +%T)] ROOT=$ROOT"
echo "[$(date +%T)] PAIRS_FILE=$PAIRS_FILE  RESULTS_ROOT=$RESULTS_ROOT  N_JOBS=$N_JOBS"
echo "[$(date +%T)] OMP/MKL/OPENBLAS threads pinned to 1 (sklearn n_jobs=$N_JOBS)"

mkdir -p "$TUNING_DIR" "$RF_PLOTS_DIR" "$DEM_DIR"

echo "[$(date +%T)] === 1. tune_max_depth.py ==="
"$PYTHON" train/tune_max_depth.py \
  --data-dir "$DATA_DIR" \
  --pairs "$PAIRS_FILE" \
  --cell-features "$CELL_FEATURES" \
  --drug-fingerprints "$DRUG_FINGERPRINTS" \
  --out-dir "$TUNING_DIR" \
  --n-jobs "$N_JOBS"

echo "[$(date +%T)] === 2. tune_n_estimators.py ==="
"$PYTHON" train/tune_n_estimators.py \
  --data-dir "$DATA_DIR" \
  --pairs "$PAIRS_FILE" \
  --cell-features "$CELL_FEATURES" \
  --drug-fingerprints "$DRUG_FINGERPRINTS" \
  --out-dir "$TUNING_DIR" \
  --n-jobs "$N_JOBS"

echo "[$(date +%T)] === 3. top_fingerprints.py (SHAP export) ==="
"$PYTHON" train/top_fingerprints.py \
  --data-dir "$DATA_DIR" \
  --pairs "$PAIRS_FILE" \
  --cell-features "$CELL_FEATURES" \
  --drug-fingerprints "$DRUG_FINGERPRINTS" \
  --out-dir "$TUNING_DIR" \
  --max-depth "$MAX_DEPTH" \
  --n-estimators "$N_ESTIMATORS" \
  --n-jobs "$N_JOBS"

echo "[$(date +%T)] === 4. generate_top_feature.py (per-drug R² + gene signature counts) ==="
"$PYTHON" train/generate_top_feature.py \
  --data-dir "$DATA_DIR" \
  --pairs "$PAIRS_FILE" \
  --cell-features "$CELL_FEATURES" \
  --out-dir "$RF_PLOTS_DIR" \
  --n-estimators "$N_ESTIMATORS" \
  --max-depth "$MAX_DEPTH" \
  --min-samples "$MIN_SAMPLES_PER_DRUG" \
  --n-jobs "$N_JOBS"

echo "[$(date +%T)] === 5. export_dem_model.py (DEM forest + leaves) ==="
"$PYTHON" train/export_dem_model.py \
  --data-dir "$DATA_DIR" \
  --pairs "$PAIRS_FILE" \
  --cell-features "$CELL_FEATURES" \
  --drug-fingerprints "$DRUG_FINGERPRINTS" \
  --out-dir "$DEM_DIR" \
  --max-depth "$MAX_DEPTH" \
  --n-estimators "$N_ESTIMATORS" \
  --n-jobs "$N_JOBS"

echo "[$(date +%T)] === 6. build_evidence.py (kernel neighborhoods) ==="
"$PYTHON" train/build_evidence.py \
  --data-dir "$DATA_DIR" \
  --pairs "$PAIRS_FILE" \
  --cell-features "$CELL_FEATURES" \
  --drug-fingerprints "$DRUG_FINGERPRINTS" \
  --leaves-parquet "$DEM_DIR/leaf_assignments.parquet" \
  --kernel-meta "$DEM_DIR/kernel_meta.npz" \
  --out-evidence "$DEM_DIR/evidence.jsonl"

echo "[$(date +%T)] === 7. report_generator.py (enriched JSONL + MD) ==="
"$PYTHON" train/report_generator.py \
  --evidence "$DEM_DIR/evidence.jsonl" \
  --out-md "$DEM_DIR/sample_reports.md" \
  --out-jsonl "$DEM_DIR/sample_reports.jsonl"

echo "[$(date +%T)] Done."
echo "Artifacts under: $RESULTS_ROOT"
