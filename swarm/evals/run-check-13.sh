#!/usr/bin/env bash
# swarm/evals/run-check-13.sh
# /lint check #13 runner — cell_acceptance_predicate present + non-trivial.
# Usage: bash swarm/evals/run-check-13.sh <decomposition-file>
# Exits 0 on pass; exits 1 on FAIL with slug + evidence emitted to stderr.
# Max-subscription discipline: pure Bash.
# Reference: .claude/skills/lint.md §13; OPP-04 artefact §3.3;
# cycle-2-implementation-2026-04-24.md §C.3.
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <decomposition-file>" >&2
  exit 2
fi
file="$1"
if [[ ! -f "$file" ]]; then
  echo "ERROR: file not found: $file" >&2
  exit 2
fi

cells=$(grep -c "^ *- cell:" "$file" || true)
preds=$(grep -c "^ *cell_acceptance_predicate:" "$file" || true)

if (( preds < cells )); then
  echo "FAIL cell-ap-missing: $file ($preds of $cells cells carry field)" >&2
  exit 1
fi

# Extract every predicate value and validate length + anti-regex.
# NOTE: awk-based extraction avoids sed portability issues; strips leading
# indentation + optional surrounding double-quotes + inline comments.
while IFS= read -r val; do
  [[ -z "$val" ]] && continue
  len=${#val}
  if (( len < 20 || len > 200 )); then
    echo "FAIL cell-ap-trivial: $file — predicate length $len (want 20..200): $val" >&2
    exit 1
  fi
  if printf '%s' "$val" | grep -qEi '^(artefact exists|file is non-empty|file exists|expected_artefact returned|non-empty file|returns output|2[x×])'; then
    echo "FAIL cell-ap-trivial: $file — predicate matches anti-regex: $val" >&2
    exit 1
  fi
done < <(
  awk '
    /^ *cell_acceptance_predicate:/ {
      # strip everything up to first colon, then leading space + optional quote
      sub(/^ *cell_acceptance_predicate: */, "", $0)
      # strip trailing inline "# comment" (but only when preceded by space)
      sub(/ +#.*$/, "", $0)
      # strip surrounding double-quotes
      if (match($0, /^".*"$/)) { $0 = substr($0, 2, length($0) - 2) }
      print
    }
  ' "$file"
)

echo "OK"
exit 0
