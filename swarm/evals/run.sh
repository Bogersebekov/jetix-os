#!/usr/bin/env bash
# swarm/evals/run.sh
# OPP-01 eval runner — walks swarm/evals/cells/*/golden-set.jsonl; for each
# record runs a structural acceptance predicate; appends result to the cell's
# results.jsonl (append-only per OPP-01 §3 IDEM invariant).
#
# Usage:
#   bash swarm/evals/run.sh                # all cells
#   bash swarm/evals/run.sh --cell <id>    # filter to a single cell
#   bash swarm/evals/run.sh --dry-run      # no writes to results.jsonl
#
# Exit code semantics:
#   0 — empty corpus OR all-pass
#   1 — any FAIL
#
# Max-subscription discipline (shared-protocols §9): pure Bash + Python stdlib.
# Zero paid tooling, zero provider SDKs, zero env-var references.

set -euo pipefail

EVALS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CELLS_ROOT="${EVALS_ROOT}/cells"
PASS=0
FAIL=0
SKIP=0
TOTAL_ENTRIES=0
MIN_ENTRIES=20

# Argument parsing
CELL_FILTER=""
DRY_RUN=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --cell)    CELL_FILTER="$2"; shift 2 ;;
    --dry-run) DRY_RUN=true;     shift   ;;
    -h|--help)
      echo "Usage: $0 [--cell <cell-id>] [--dry-run]"
      exit 0 ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

# Empty-corpus guard — cells dir absent or no golden-set files
if [[ ! -d "${CELLS_ROOT}" ]]; then
  echo "PASS=0 FAIL=0 SKIP=0 (empty corpus — ${CELLS_ROOT} absent)"
  exit 0
fi

# Discover cell directories
shopt -s nullglob
for cell_dir in "${CELLS_ROOT}"/*/; do
  cell_id="$(basename "${cell_dir}")"
  if [[ -n "${CELL_FILTER}" && "${cell_id}" != "${CELL_FILTER}" ]]; then
    continue
  fi
  golden="${cell_dir}golden-set.jsonl"
  if [[ ! -f "${golden}" ]]; then
    continue
  fi
  results="${cell_dir}results.jsonl"
  # Ensure results file exists (may be a no-op touch on first run)
  [[ -f "${results}" ]] || { [[ "${DRY_RUN}" == false ]] && : > "${results}" || true; }

  while IFS= read -r line || [[ -n "${line}" ]]; do
    # Skip blank / comment lines
    [[ -z "${line}" ]] && continue
    case "${line}" in \#*) continue ;; esac
    TOTAL_ENTRIES=$((TOTAL_ENTRIES + 1))

    # Extract fields via Python stdlib (no jq dependency required)
    test_id=$(printf '%s' "${line}" | python3 -c "import sys,json; d=json.loads(sys.stdin.read()); print(d.get('test_id',''))")
    expected_path=$(printf '%s' "${line}" | python3 -c "import sys,json; d=json.loads(sys.stdin.read()); print(d.get('expected_output_path',''))")

    # Minimal structural acceptance predicate: expected_output file exists + non-empty
    if [[ -n "${expected_path}" && -f "${expected_path}" && -s "${expected_path}" ]]; then
      pass_val=true
      PASS=$((PASS + 1))
    else
      pass_val=false
      FAIL=$((FAIL + 1))
    fi

    if [[ "${DRY_RUN}" == false ]]; then
      ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
      # Append-only (IDEM); no overwrite of existing records
      printf '{"cell_id":"%s","test_id":"%s","pass":%s,"timestamp":"%s"}\n' \
        "${cell_id}" "${test_id}" "${pass_val}" "${ts}" >> "${results}"
    fi
  done < "${golden}"
done

# min_entries warning (OPP-01 §3 line 292-294) — does NOT fail the run
if (( TOTAL_ENTRIES < MIN_ENTRIES )); then
  echo "WARN: golden-set floor not reached (have ${TOTAL_ENTRIES}, need ${MIN_ENTRIES}); measurements not yet statistically meaningful" >&2
fi

echo "PASS=${PASS} FAIL=${FAIL} SKIP=${SKIP}"

# Exit 0 on empty corpus (no work = not a failure) OR on all-pass.
# Exit 1 if any FAIL.
if (( FAIL == 0 )); then
  exit 0
else
  exit 1
fi
