#!/usr/bin/env bash
# swarm/lib/hooks/r12-paired-frame-check.sh
# Jetix swarm cycle hook — R12 paired-frame enforcement check
# Created 2026-05-24 per book-driven-agents Stage 6 (execution prompt
# prompts/execute-book-driven-agents-stage-2-6-2026-05-24.md).
# Authority: Ruslan ack MAX-8 (decisions/RUSLAN-ACK-BOOK-DRIVEN-AGENTS-2026-05-24.md)
# Operationalizes: Tier 2 R12 + RUSLAN-LAYER 4 extraction action classes.
#
# What it does:
#   For each session/cycle, scans dispatch-log (or fallback: recent draft files)
#   to verify that any dispatch of propaganda-expert / recruitment-dynamics-expert /
#   nlp-expert / gamification-engagement-expert was PAIRED with
#   influence-ethics-expert (receiver direction).
#   Missing pair → emit Halt-Log-Alert F4 to swarm/approvals/log.jsonl
#   (per Part 6b §I.2 LOCKED enforcement).
#
# Cycle-2 mode: log-only (warns, does not fail session).
# Max-subscription discipline: pure Bash.
# IP-1 strict: operates on role-archetype slugs only.
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
LOG_PATH="${ROOT}/swarm/approvals/log.jsonl"
DRAFTS_DIR="${ROOT}/swarm/wiki/drafts"

# 4 trigger agents that REQUIRE influence-ethics-expert pairing
TRIGGER_AGENTS=("propaganda-expert" "recruitment-dynamics-expert" "nlp-expert" "gamification-engagement-expert")
RECEIVER_AGENT="influence-ethics-expert"

echo "[r12-hook] Running R12 paired-frame enforcement check (cycle-2 log-only)..."

mkdir -p "$(dirname "$LOG_PATH")"

violations=0
shopt -s nullglob

for trigger in "${TRIGGER_AGENTS[@]}"; do
  # Find any draft file referencing this trigger agent
  for draft in "${DRAFTS_DIR}"/*"${trigger}"*.md; do
    [[ -f "$draft" ]] || continue
    # Check whether companion influence-ethics-expert draft exists for same task-id
    task_id=$(basename "$draft" | sed -E "s/-${trigger}-.*//")
    companion="${DRAFTS_DIR}/${task_id}-${RECEIVER_AGENT}-"*.md
    if ! ls $companion 2>/dev/null | head -n 1 >/dev/null; then
      ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
      msg="[WARN cycle-2 log-only] R12 paired-frame missing: ${trigger} draft (${draft}) without ${RECEIVER_AGENT} companion for task-id=${task_id}"
      echo "$msg" >&2
      # Emit Halt-Log-Alert F4 entry (log-only in cycle-2)
      printf '{"ts":"%s","alert_grade":"F4","rule":"R12-paired-frame-missing","trigger_agent":"%s","receiver_agent_missing":"%s","draft_path":"%s","task_id":"%s","mode":"log-only-cycle-2"}\n' \
        "$ts" "$trigger" "$RECEIVER_AGENT" "$draft" "$task_id" >> "$LOG_PATH"
      violations=$((violations + 1))
    fi
  done
done

if [[ $violations -gt 0 ]]; then
  echo "[r12-hook] $violations R12 paired-frame violation(s) logged to $LOG_PATH (cycle-2 log-only)" >&2
else
  echo "[r12-hook] R12 paired-frame discipline preserved (0 violations)"
fi

exit 0
