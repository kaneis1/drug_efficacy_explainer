#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="${PYTHON:-/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python}"

PROJECT="${PROJECT:-acc_lin_lab}"
QUEUE="${QUEUE:-gpuexpress}"
JOB_NAME="${JOB_NAME:-llama_vs_gemini_eval}"
LOG_DIR="${LOG_DIR:-$ROOT/llm_explainer/logs}"

GPU_NUM="${GPU_NUM:-1}"
GPU_MEM="${GPU_MEM:-70G}"
HOST_MEM="${HOST_MEM:-256G}"
WALL_MIN="${WALL_MIN:-720}"
N_CORES="${N_CORES:-4}"

MODELS="${MODELS:-Meta-Llama-3.1-8B-Instruct,Llama-3.3-70B-Instruct}"
MAX_NEW_TOKENS="${MAX_NEW_TOKENS:-384}"
TEMPERATURE="${TEMPERATURE:-0}"

mkdir -p "$LOG_DIR"

CMD=(
  "$PYTHON"
  "$ROOT/llm_explainer/llama_vs_gemini_eval.py"
  --models "$MODELS"
  --temperature "$TEMPERATURE"
  --max-new-tokens "$MAX_NEW_TOKENS"
)

if [[ -n "${CASES_MD:-}" ]]; then
  CMD+=(--cases-md "$CASES_MD")
fi

if [[ -n "${OUT_MD:-}" ]]; then
  CMD+=(--out-md "$OUT_MD")
fi

if [[ -n "${PROMPT_DIR:-}" ]]; then
  CMD+=(--prompt-dir "$PROMPT_DIR")
fi

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  CMD+=(--dry-run)
fi

printf 'Submitting %s to queue %s with %s GPU memory\n' "$JOB_NAME" "$QUEUE" "$GPU_MEM"
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
  -oo "$LOG_DIR/llama-vs-gemini.%J.out" \
  -eo "$LOG_DIR/llama-vs-gemini.%J.err" \
  "${CMD[@]}"
