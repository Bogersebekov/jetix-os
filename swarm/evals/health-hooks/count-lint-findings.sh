#!/usr/bin/env bash
# swarm/evals/health-hooks/count-lint-findings.sh
# Emit the count of /lint findings in the most-recent run_id group of
# swarm/evals/lint-findings.jsonl. Emits 0 if the file is absent (empty-corpus safe).
# Used by cycle-close ritual to update swarm/wiki/meta/health.md lint_findings_count.
# Max-subscription discipline: pure Bash + Python stdlib.
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
LINT_FILE="${ROOT}/swarm/evals/lint-findings.jsonl"

if [[ ! -f "${LINT_FILE}" ]]; then
  echo "0"
  exit 0
fi

# Count lines in the most-recent run_id group.
# Each line: {"run_id":"...", ...}. Find the last run_id seen; count records matching.
python3 - "${LINT_FILE}" <<'PY'
import sys, json
path = sys.argv[1]
last_run = None
per_run = {}
try:
    with open(path, 'r', encoding='utf-8') as fh:
        for raw in fh:
            raw = raw.strip()
            if not raw or raw.startswith('#'):
                continue
            try:
                rec = json.loads(raw)
            except Exception:
                continue
            rid = rec.get('run_id') or rec.get('runId') or ''
            if not rid:
                continue
            last_run = rid
            per_run[rid] = per_run.get(rid, 0) + 1
    print(per_run.get(last_run, 0))
except FileNotFoundError:
    print(0)
PY
exit 0
