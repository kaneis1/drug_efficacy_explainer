#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="${PYTHON:-/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python}"
QUEUE="${QUEUE:-gpuexpress}"
PROJECT="${PROJECT:-acc_lin_lab}"
EXPERIMENT_DIR="${EXPERIMENT_DIR:-$ROOT/llm_explainer/sft_experiment_500}"
OUT_DIR="${OUT_DIR:-$EXPERIMENT_DIR/teacher_pairs_local}"
LOG_DIR="${LOG_DIR:-$ROOT/llm_explainer/logs}"
MODEL_KEY="${MODEL_KEY:-Llama-3.3-70B-Instruct}"
NUM_GPUS="${NUM_GPUS:-5}"
GPU_MEM="${GPU_MEM:-70G}"
HOST_MEM="${HOST_MEM:-256G}"
WALL_MIN="${WALL_MIN:-720}"
MAX_REPORTS_PER_SPLIT="${MAX_REPORTS_PER_SPLIT:-0}"
OVERWRITE_FLAG="${OVERWRITE_FLAG:---overwrite}"

mkdir -p "$OUT_DIR" "$LOG_DIR"

if [[ ! -d "$EXPERIMENT_DIR/teacher_requests" ]]; then
  echo "Missing teacher request directory: $EXPERIMENT_DIR/teacher_requests" >&2
  echo "Build it first with prepare_sft_data.py" >&2
  exit 1
fi

stdout_file="$LOG_DIR/teacher-local.%J.out"
stderr_file="$LOG_DIR/teacher-local.%J.err"
cmd="$PYTHON $ROOT/llm_explainer/generate_teacher_pairs_local.py --experiment-dir \"$EXPERIMENT_DIR\" --teacher-model-key \"$MODEL_KEY\" --out-dir \"$OUT_DIR\" --max-reports-per-split \"$MAX_REPORTS_PER_SPLIT\" $OVERWRITE_FLAG"

bsub \
  -P "$PROJECT" \
  -q "$QUEUE" \
  -J llmexp_teacher70b \
  -n 20 \
  -W "$WALL_MIN" \
  -R "span[hosts=1] rusage[mem=$HOST_MEM]" \
  -gpu "num=$NUM_GPUS:mode=exclusive_process:gmem=$GPU_MEM" \
  -oo "$stdout_file" \
  -eo "$stderr_file" \
  "$cmd"
