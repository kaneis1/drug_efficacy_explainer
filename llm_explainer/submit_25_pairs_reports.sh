#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="${PYTHON:-/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python}"

PROJECT="${PROJECT:-acc_lin_lab}"
QUEUE="${QUEUE:-gpuexpress}"
JOB_NAME="${JOB_NAME:-llm_25_pairs_reports}"
LOG_DIR="${LOG_DIR:-$ROOT/llm_explainer/logs}"

MODEL_KEY="${MODEL_KEY:-Llama-3.3-70B-Instruct}"
REPORTS="${REPORTS:-$ROOT/llm_explainer/shap_reports_25_pairs_ic50.jsonl}"
RESULTS_ROOT="${RESULTS_ROOT:-$ROOT/results_ic50}"
OUTPUT_ROOT="${OUTPUT_ROOT:-$ROOT/llm_explainer/outputs_25_pairs_ic50}"
TEMPERATURE="${TEMPERATURE:-0}"
MAX_NEW_TOKENS="${MAX_NEW_TOKENS:-0}"

GPU_NUM="${GPU_NUM:-1}"
GPU_MEM="${GPU_MEM:-70G}"
HOST_MEM="${HOST_MEM:-256G}"
WALL_MIN="${WALL_MIN:-720}"
N_CORES="${N_CORES:-4}"

mkdir -p "$LOG_DIR" "$OUTPUT_ROOT"

CMD=(
  "$PYTHON"
  "$ROOT/llm_explainer/generate_reports.py"
  --model-key "$MODEL_KEY"
  --reports "$REPORTS"
  --results-root "$RESULTS_ROOT"
  --output-root "$OUTPUT_ROOT"
  --temperature "$TEMPERATURE"
  --overwrite
)

if [[ "$MAX_NEW_TOKENS" != "0" ]]; then
  CMD+=(--max-new-tokens "$MAX_NEW_TOKENS")
fi

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  CMD+=(--dry-run)
fi

printf 'Submitting %s (%s) to %s with %s GPU memory\n' "$JOB_NAME" "$MODEL_KEY" "$QUEUE" "$GPU_MEM"
printf 'Command:'
printf ' %q' "${CMD[@]}"
printf '\n'

if [[ "${PRINT_ONLY:-0}" == "1" ]]; then
  exit 0
fi

bsub \
  -P "$PROJECT" \
  -q "$QUEUE" \
  -J "$JOB_NAME" \
  -n "$N_CORES" \
  -W "$WALL_MIN" \
  -R "span[hosts=1] rusage[mem=$HOST_MEM]" \
  -gpu "num=$GPU_NUM:mode=exclusive_process:gmem=$GPU_MEM" \
  -oo "$LOG_DIR/25-pairs-reports.%J.out" \
  -eo "$LOG_DIR/25-pairs-reports.%J.err" \
  "${CMD[@]}"
