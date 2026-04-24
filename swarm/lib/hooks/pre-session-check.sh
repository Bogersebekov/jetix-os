#!/usr/bin/env bash
# swarm/lib/hooks/pre-session-check.sh
# Jetix swarm hook-layer fallback (OPP-02 Alternative B) — invoked by brigadier
# at the start of every session when the Claude Code hook API is unavailable.
# Runs sub-components 2 + 3 against the current repo state. Sub-component 1
# (mode-prefix) is enforced at DISPATCH time (brigadier §4.2 addition).
# Cycle-2 mode = log-only: warns on any violation but never fails the session.
# Max-subscription discipline: pure Bash.
# Reference: OPP-02 artefact §3.4; cycle-2-impl §B.5 Alt-B.
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
HOOK_DIR="${ROOT}/.claude/hooks"
TS_FILE="${ROOT}/swarm/lib/hooks/.last-run"

echo "[hook-layer] Running pre-session enforcement checks (cycle-2 log-only)..."

# Sub-component 2 pre-condition — verify write_scope_glob present in all 5 expert files
for expert in engineering-expert mgmt-expert systems-expert philosophy-expert investor-expert; do
  f="${ROOT}/.claude/agents/${expert}.md"
  if [[ ! -f "$f" ]]; then
    echo "[WARN] expert file missing: $f" >&2
    continue
  fi
  if ! grep -qE "^write_scope_glob:" "$f"; then
    echo "[WARN cycle-2 log-only] $expert lacks write_scope_glob in frontmatter (role-matrix fail-safe)" >&2
  fi
done

# Sub-component 3 — verify pending drafts have within-file completeness
shopt -s nullglob
drafts_count=0
for draft in "${ROOT}"/swarm/wiki/drafts/*.md; do
  drafts_count=$((drafts_count + 1))
  bash "${HOOK_DIR}/verify-packet.sh" "$draft" || true
done

# Stamp last-run timestamp (used by the /lint timestamp-check per OPP-02 §3.4)
date -u +"%Y-%m-%dT%H:%M:%SZ" > "$TS_FILE"

echo "[hook-layer] Pre-session checks complete. drafts_inspected=${drafts_count}"
exit 0
