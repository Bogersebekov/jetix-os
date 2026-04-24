#!/usr/bin/env bash
# .claude/hooks/verify-packet.sh
# OPP-02 sub-component 3 — return-packet verifier (4 within-file completeness checks).
# Usage: bash .claude/hooks/verify-packet.sh <draft-path>
# Filter: runs only on swarm/wiki/drafts/*.md (other paths short-circuit).
# Cycle-2 mode = log-only (warn + exit 0). Cycle-3+ may flip to exit 1 on AP-1.
# Reference: OPP-02 artefact §3.3; cycle-2-impl §B.3.
set -euo pipefail

DRAFT="${1:-}"
if [[ -z "$DRAFT" ]]; then
  echo "Usage: $0 <draft-path>" >&2
  exit 2
fi

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
EVENTS_LOG="${ROOT}/swarm/evals/cells/hook-layer/events.jsonl"
mkdir -p "$(dirname "$EVENTS_LOG")"
ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

# Filter — only inspect swarm/wiki/drafts/ paths
case "$DRAFT" in
  *swarm/wiki/drafts/*) ;;
  *)
    # Non-drafts paths pass through silently in cycle-2; not our target.
    exit 0 ;;
esac

[[ -f "$DRAFT" ]] || {
  printf '{"ts":"%s","component":"verify-packet","result":"warn","draft":"%s","evidence":"file-absent"}\n' \
    "$ts" "$DRAFT" >> "$EVENTS_LOG"
  echo "[WARN cycle-2 log-only] verify-packet: file absent $DRAFT" >&2
  exit 0
}

violations=()

# Check 1 — sources[] non-empty
# Look at 3 lines following `^sources:` and require at least one starts with "- ".
src_non_empty=false
if grep -q "^sources:" "$DRAFT"; then
  # grab up to 10 lines after `^sources:`; stop at first blank or non-indented
  awk '/^sources:/{flag=1;next} flag{if ($0 ~ /^[^[:space:]-]/ || NF==0) exit; print}' "$DRAFT" \
    | grep -qE '^\s*-\s+' && src_non_empty=true
fi
[[ "$src_non_empty" == true ]] || violations+=("sources[] empty or absent")

# Check 2 — confidence_method present + non-empty
grep -qE "^confidence_method:[[:space:]]*\S+" "$DRAFT" \
  || violations+=("confidence_method absent or empty")

# Check 3 — type present + non-empty
grep -qE "^type:[[:space:]]*\S+" "$DRAFT" \
  || violations+=("type field absent or empty")

# Check 4 — AP-1 lock: body-length > 500 chars AND sources empty = inlined-source-in-prompt pattern.
# Body length measured from first `^---` close to EOF.
body_chars=$(awk 'c==1{print;next} /^---$/{c+=1}' "$DRAFT" | wc -c | tr -d ' ')
if [[ "$src_non_empty" == false && "${body_chars:-0}" -gt 500 ]]; then
  violations+=("AP-1 candidate: body_chars=$body_chars AND sources[] empty")
fi

if (( ${#violations[@]} == 0 )); then
  printf '{"ts":"%s","component":"verify-packet","result":"pass","draft":"%s"}\n' \
    "$ts" "$DRAFT" >> "$EVENTS_LOG"
  exit 0
fi

# One warn event per violation (cycle-2 = log-only)
for v in "${violations[@]}"; do
  ev=$(printf '%s' "$v" | sed 's/"/\\"/g')
  printf '{"ts":"%s","component":"verify-packet","result":"warn","draft":"%s","evidence":"%s"}\n' \
    "$ts" "$DRAFT" "$ev" >> "$EVENTS_LOG"
  echo "[WARN cycle-2 log-only] verify-packet $DRAFT: $v" >&2
done
exit 0
