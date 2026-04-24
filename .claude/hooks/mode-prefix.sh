#!/usr/bin/env bash
# .claude/hooks/mode-prefix.sh
# OPP-02 sub-component 1 — mode-prefix regex validator.
# Usage: bash .claude/hooks/mode-prefix.sh "<prompt>" "<agent-name>"
# Cycle-2 mode = log-only (warn + exit 0). Cycle-3+ may flip to exit 1.
# Max-subscription discipline: pure Bash.
# Reference: OPP-02 artefact §3.1; cycle-2-impl §B.1.
set -euo pipefail

PROMPT="${1:-}"
AGENT="${2:-unknown}"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
EVENTS_LOG="${ROOT}/swarm/evals/cells/hook-layer/events.jsonl"
ALLOWLIST="${ROOT}/.claude/hooks/mode-prefix-allowlist.txt"

mkdir -p "$(dirname "$EVENTS_LOG")"

# Allowlist short-circuit (5 known legitimate non-matrix agents)
if [[ -f "$ALLOWLIST" ]] && grep -qxF "$AGENT" "$ALLOWLIST" 2>/dev/null; then
  exit 0
fi

# Read first non-blank line of the prompt
first_line=$(printf '%s\n' "$PROMPT" | sed -n '/[^[:space:]]/{p;q;}')
ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

if printf '%s\n' "$first_line" | grep -qE '^mode: (critic|optimizer|integrator|scalability)$'; then
  printf '{"ts":"%s","component":"mode-prefix","result":"pass","agent":"%s"}\n' \
    "$ts" "$AGENT" >> "$EVENTS_LOG"
else
  # Cycle-2: log-only warn; exit 0 so dispatch proceeds
  ev=$(printf '%s' "$first_line" | sed 's/"/\\"/g')
  printf '{"ts":"%s","component":"mode-prefix","result":"warn","agent":"%s","evidence":"%s"}\n' \
    "$ts" "$AGENT" "$ev" >> "$EVENTS_LOG"
  echo "[WARN cycle-2 log-only] mode-prefix mismatch agent=$AGENT first_line=$first_line" >&2
fi
exit 0
