#!/usr/bin/env bash
# Stage 2A overnight launcher — invokes v3 rerun, generates comparison report,
# commits + pushes. Single entry point for `nohup ... &` background launch.
#
# Plan-doc: reports/wiki-rebuild-stage-2A-plan-2026-05-11.md
# Triggered: 2026-05-11 ~04:00 CEST (override of §11 22:00 target).

set -u  # NOT -e — we want to handle non-zero exits from rerun script

ROOT="/home/ruslan/jetix-os"
cd "$ROOT" || exit 99

LOG="/tmp/stage2a_launcher.log"
PID_FILE="/tmp/stage2a.pid"
DISCIPLINE_LOG="reports/voice-pipeline-2026-05-10/_stage5_v3_rerun.log.md"

echo "$$" > "$PID_FILE"
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Stage 2A launcher START (pid=$$)" >> "$LOG"

# ── 1. Run live LLM rerank ──
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] invoking _rerun_stage5_v3 (live)" >> "$LOG"
python3 -m tools.wiki_integration._rerun_stage5_v3 >> "$LOG" 2>&1
RC=$?
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] rerun exit code: $RC" >> "$LOG"

# ── 2. Match-rate comparison v2 → v3 ──
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] generating match-rate-comparison-v3.md" >> "$LOG"
python3 tools/wiki_integration/_compare_v2_v3.py >> "$LOG" 2>&1 || \
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] comparison script failed (non-fatal)" >> "$LOG"

# ── 3. Read final tier counts for commit message ──
SIDECAR="$ROOT/reports/voice-pipeline-2026-05-10/04-wiki-candidates-v3.json"
SUMMARY="$ROOT/reports/voice-pipeline-2026-05-10/checkpoint-summary.md"

if [ -f "$SIDECAR" ]; then
  A=$(python3 -c "import json; d=json.load(open('$SIDECAR')); print(d.get('tier_a_count', '?'))")
  B=$(python3 -c "import json; d=json.load(open('$SIDECAR')); print(d.get('tier_b_count', '?'))")
  C=$(python3 -c "import json; d=json.load(open('$SIDECAR')); print(d.get('tier_c_count', '?'))")
  MR=$(python3 -c "import json; d=json.load(open('$SIDECAR')); print(f\"{d.get('match_rate', 0)*100:.1f}\")")
  TOTAL=$(python3 -c "import json; d=json.load(open('$SIDECAR')); print(d.get('total_candidates', '?'))")
  BATCHES=$(( (TOTAL + 7) / 8 ))
else
  A=?; B=?; C=?; MR=?; BATCHES=?
fi

NOW_BERLIN=$(TZ='Europe/Berlin' date +%H:%M)

# ── 4. Commit + push ──
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] git add + commit + push" >> "$LOG"
git -C "$ROOT" add reports/voice-pipeline-2026-05-10/04-wiki-candidates-v3.md \
                   reports/voice-pipeline-2026-05-10/04-wiki-candidates-v3.json \
                   reports/voice-pipeline-2026-05-10/_stage5_v3_rerun.log.md \
                   reports/voice-pipeline-2026-05-10/checkpoint-summary.md \
                   reports/wiki-integration-redesign-2026-05-10/match-rate-comparison-v3.md \
                   2>>"$LOG"

# Stage tool/orchestrator/llm_ranker patches separately
git -C "$ROOT" add tools/voice-pipeline-orchestrator.py \
                   tools/wiki_integration/llm_ranker.py \
                   tools/wiki_integration/_rerun_stage5_v3.py \
                   tools/wiki_integration/_stage2a_launcher.sh \
                   tools/wiki_integration/_compare_v2_v3.py \
                   2>>"$LOG"

if [ "$RC" -eq 0 ]; then
  MSG="[wiki-rebuild] Stage 2A v3 done — ${BATCHES} batches, ${A}/${B}/${C}, ${MR}% (v2 50.1% → v3 ${MR}%)"
else
  MSG="[wiki-rebuild] Stage 2A HALT — exit=${RC} at ${NOW_BERLIN} CEST, checkpoint preserved"
fi

git -C "$ROOT" commit -m "$MSG" 2>>"$LOG"
git -C "$ROOT" push origin main 2>>"$LOG"
PUSH_RC=$?
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] push rc: $PUSH_RC | msg: $MSG" >> "$LOG"

# ── 5. Discipline log append (idempotent) ──
echo "- $(date -u +%Y-%m-%dT%H:%M:%SZ) | Stage 2A launcher END (rc=$RC, push=$PUSH_RC) | $MSG" >> "$DISCIPLINE_LOG" 2>/dev/null || true

rm -f "$PID_FILE"
exit "$RC"
