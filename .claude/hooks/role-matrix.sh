#!/usr/bin/env bash
# .claude/hooks/role-matrix.sh
# OPP-02 sub-component 2 — write-scope-guard pre-check.
# Usage: bash .claude/hooks/role-matrix.sh [<role>] [<path>]
#   $1 or $CLAUDE_AGENT_ROLE  — agent role name
#   $2 or $CLAUDE_TOOL_INPUT_PATH — the path the agent intends to write
# Cycle-2 mode = log-only (warn + exit 0). Cycle-3+ may flip to exit 1.
# Max-subscription discipline: pure Bash. Reference: OPP-02 §3.2.
set -euo pipefail

ROLE="${CLAUDE_AGENT_ROLE:-${1:-unknown}}"
WRITE_PATH="${CLAUDE_TOOL_INPUT_PATH:-${2:-}}"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
EVENTS_LOG="${ROOT}/swarm/evals/cells/hook-layer/events.jsonl"
PARSE_FIELD="${ROOT}/swarm/lib/hooks/parse-frontmatter-field.sh"

mkdir -p "$(dirname "$EVENTS_LOG")"
ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

emit_event() {
  local result="$1" evidence="$2"
  local ev
  ev=$(printf '%s' "$evidence" | sed 's/"/\\"/g')
  printf '{"ts":"%s","component":"role-matrix","result":"%s","agent":"%s","path":"%s","evidence":"%s"}\n' \
    "$ts" "$result" "$ROLE" "$WRITE_PATH" "$ev" >> "$EVENTS_LOG"
}

# brigadier short-circuit (full write access per shared-protocols §5)
if [[ "$ROLE" == "brigadier" ]]; then
  emit_event "pass" "brigadier-full-access"
  exit 0
fi

# Empty path or no agent file → pass-through (cycle-2 fail-safe per OPP-02 §8 row 6)
agent_file="${ROOT}/.claude/agents/${ROLE}.md"
if [[ -z "$WRITE_PATH" || ! -f "$agent_file" ]]; then
  emit_event "pass" "passthrough-no-scope-to-check"
  exit 0
fi

# Extract write_scope_glob from the agent frontmatter (single-line scalar)
glob=""
if [[ -x "$PARSE_FIELD" ]]; then
  glob="$(bash "$PARSE_FIELD" "$agent_file" write_scope_glob || echo '')"
fi

# Empty glob → log WARN + exit 0 (cycle-2 fail-safe; cycle-3+ may tighten)
if [[ -z "$glob" ]]; then
  emit_event "warn" "write_scope_glob absent from $agent_file"
  echo "[WARN cycle-2 log-only] role-matrix no write_scope_glob for role=$ROLE (fail-safe passthrough)" >&2
  exit 0
fi

# Glob match using shopt extglob + case (more expressive than plain glob)
shopt -s extglob
matched=false
# Support multi-glob values separated by comma or space
IFS=', ' read -r -a globs <<< "$glob"
for g in "${globs[@]}"; do
  [[ -z "$g" ]] && continue
  case "$WRITE_PATH" in
    $g) matched=true; break ;;
  esac
done

if [[ "$matched" == true ]]; then
  emit_event "pass" "matched-glob:$glob"
else
  # Cycle-2: warn-only; path considered out of declared scope
  emit_event "warn" "out-of-scope write: path=$WRITE_PATH glob=$glob"
  echo "[WARN cycle-2 log-only] role-matrix out-of-scope role=$ROLE path=$WRITE_PATH glob=$glob" >&2
fi
exit 0
