#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="/sc/arion/work/cuiz02/conda-envs/envs/drug/bin/python"
QUEUE="${QUEUE:-gpuexpress}"
CPU_QUEUE="${CPU_QUEUE:-express}"
PROJECT="${PROJECT:-acc_lin_lab}"
REPORTS="${REPORTS:-$ROOT/llm_explainer/shap_sample_reports.jsonl}"
RESULTS_ROOT="${RESULTS_ROOT:-$ROOT/results}"
OUTPUT_ROOT="${OUTPUT_ROOT:-$ROOT/llm_explainer/outputs}"
LOG_DIR="${LOG_DIR:-$ROOT/llm_explainer/logs}"
JOB_MANIFEST="$ROOT/llm_explainer/job_manifest.tsv"

mkdir -p "$OUTPUT_ROOT" "$LOG_DIR"

if [[ ! -f "$REPORTS" ]]; then
  echo "Missing input bundle: $REPORTS" >&2
  echo "Build it first with: $PYTHON $ROOT/llm_explainer/build_shap_reports.py" >&2
  exit 1
fi

MODELS_ENV="${MODELS:-}"
if [[ -n "$MODELS_ENV" ]]; then
  IFS=',' read -r -a MODELS <<< "$MODELS_ENV"
else
  MODELS=(
    "BioMistral-7B"
    "Meditron-7b"
    "Meta-Llama-3.1-8B-Instruct"
    "Qwen2.5-32B-Instruct"
    "gpt-oss-20b"
  )
fi

declare -A GPU_MEM=(
  ["BioMistral-7B"]="20G"
  ["Meditron-7b"]="20G"
  ["Meta-Llama-3.1-8B-Instruct"]="24G"
  ["Qwen2.5-32B-Instruct"]="70G"
  ["gpt-oss-20b"]="70G"
)

declare -A HOST_MEM=(
  ["BioMistral-7B"]="48G"
  ["Meditron-7b"]="48G"
  ["Meta-Llama-3.1-8B-Instruct"]="64G"
  ["Qwen2.5-32B-Instruct"]="96G"
  ["gpt-oss-20b"]="96G"
)

declare -A WALL_MIN=(
  ["BioMistral-7B"]="240"
  ["Meditron-7b"]="240"
  ["Meta-Llama-3.1-8B-Instruct"]="240"
  ["Qwen2.5-32B-Instruct"]="360"
  ["gpt-oss-20b"]="360"
)

printf "model_key\tjob_id\tqueue\tgpu_mem\thost_mem\twall_minutes\n" > "$JOB_MANIFEST"

dep_terms=()
for model in "${MODELS[@]}"; do
  slug="$(python - <<'PY' "$model"
import re, sys
print(re.sub(r"[^A-Za-z0-9]+", "-", sys.argv[1]).strip("-").lower())
PY
)"
  job_name="llmexp_${slug}"
  stdout_file="$LOG_DIR/${slug}.%J.out"
  stderr_file="$LOG_DIR/${slug}.%J.err"
  cmd="$PYTHON $ROOT/llm_explainer/generate_reports.py --model-key \"$model\" --reports \"$REPORTS\" --results-root \"$RESULTS_ROOT\" --output-root \"$OUTPUT_ROOT\" --overwrite"

  submit_out="$(
    bsub \
      -P "$PROJECT" \
      -q "$QUEUE" \
      -J "$job_name" \
      -n 4 \
      -W "${WALL_MIN[$model]}" \
      -R "span[hosts=1] rusage[mem=${HOST_MEM[$model]}]" \
      -gpu "num=1:mode=exclusive_process:gmem=${GPU_MEM[$model]}" \
      -oo "$stdout_file" \
      -eo "$stderr_file" \
      "$cmd"
  )"

  job_id="$(echo "$submit_out" | sed -n 's/Job <\([0-9]\+\)>.*/\1/p')"
  printf "%s\t%s\t%s\t%s\t%s\t%s\n" \
    "$model" "$job_id" "$QUEUE" "${GPU_MEM[$model]}" "${HOST_MEM[$model]}" "${WALL_MIN[$model]}" \
    >> "$JOB_MANIFEST"
  dep_terms+=("done(${job_id})")
  echo "$submit_out"
done

dependency=""
for term in "${dep_terms[@]}"; do
  if [[ -n "$dependency" ]]; then
    dependency+=" && "
  fi
  dependency+="$term"
done
summary_out="$(
  bsub \
    -P "$PROJECT" \
    -q "$CPU_QUEUE" \
    -J llmexp_compare \
    -w "$dependency" \
    -n 1 \
    -W 30 \
    -R "rusage[mem=8G]" \
    -oo "$LOG_DIR/model-comparison.%J.out" \
    -eo "$LOG_DIR/model-comparison.%J.err" \
    "$PYTHON $ROOT/llm_explainer/build_comparison.py --reports \"$REPORTS\" --outputs-root \"$OUTPUT_ROOT\" --out-file \"$ROOT/llm_explainer/model_comparison.md\""
)"
echo "$summary_out"
echo "Wrote job manifest to $JOB_MANIFEST"
