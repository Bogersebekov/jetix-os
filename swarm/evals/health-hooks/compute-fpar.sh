#!/usr/bin/env bash
# swarm/evals/health-hooks/compute-fpar.sh
# Compute FPAR = sum(pass=true) / sum(total) across swarm/evals/cells/*/results.jsonl.
# Emits "0.00" on empty corpus (no records anywhere); else a 2-decimal float.
# Used by cycle-close ritual to append to swarm/wiki/meta/health.md fpar_log.
# Max-subscription discipline: pure Bash + Python stdlib.
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
CELLS_ROOT="${ROOT}/swarm/evals/cells"

if [[ ! -d "${CELLS_ROOT}" ]]; then
  echo "0.00"
  exit 0
fi

python3 - "${CELLS_ROOT}" <<'PY'
import sys, os, json
root = sys.argv[1]
total = 0
passed = 0
for dirpath, _dirs, files in os.walk(root):
    if 'results.jsonl' in files:
        fp = os.path.join(dirpath, 'results.jsonl')
        try:
            with open(fp, 'r', encoding='utf-8') as fh:
                for raw in fh:
                    raw = raw.strip()
                    if not raw or raw.startswith('#'):
                        continue
                    try:
                        rec = json.loads(raw)
                    except Exception:
                        continue
                    total += 1
                    if rec.get('pass') is True:
                        passed += 1
        except OSError:
            continue
if total == 0:
    print("0.00")
else:
    print(f"{passed/total:.2f}")
PY
exit 0
