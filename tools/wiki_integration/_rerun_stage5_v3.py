"""Stage 2A overnight rerun (v3) — LLM precision rerank for wiki candidates.

Plan-doc: reports/wiki-rebuild-stage-2A-plan-2026-05-11.md
Trigger:  "поехали Stage 2A" (Ruslan, 2026-05-11 ~04:00 CEST override)

This script:
  - Loads existing _filtered-annotated.json (1627 items from v2 2026-05-10)
  - Runs Stage 5 with STAGE5_SKIP_LLM=0, batch=8, claude-sonnet-4-6
  - Writes 04-wiki-candidates-v3.{md,json} (v2 untouched per Q3 ack)
  - Checkpoint every 50 batches → _checkpoint_v3.json (gitignored)
  - 3×30min auto-retry on throttle → halt-for-Ruslan after exhaustion
  - Final audit → checkpoint-summary.md (committed)

Delta-Stages 1-4 and PG-list overrides are NOT implemented tonight (deferred
to bulk-ack workflow tomorrow). Plan-doc §3 PG-criteria will be applied
during /wiki-bulk-ack as override-rules; v3 reports carry raw LLM scores.

Usage:
    python3 -m tools.wiki_integration._rerun_stage5_v3 [--dry-run]
"""

import importlib.util
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path("/home/ruslan/jetix-os")
sys.path.insert(0, str(ROOT))

OUTPUT_DIR = ROOT / "reports" / "voice-pipeline-2026-05-10"
CKPT_PATH = OUTPUT_DIR / "_checkpoint_v3.json"
SUMMARY_PATH = OUTPUT_DIR / "checkpoint-summary.md"
ANNOTATED_PATH = OUTPUT_DIR / "_filtered-annotated.json"
DISCIPLINE_LOG_PATH = OUTPUT_DIR / "_stage5_v3_rerun.log.md"


def _now_utc() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _now_berlin() -> str:
    # CEST = UTC+2 (DST). Plan-doc target window in Berlin time.
    return time.strftime("%Y-%m-%dT%H:%M %z (Berlin)", time.localtime())


def _append_log(line: str) -> None:
    DISCIPLINE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with DISCIPLINE_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"- {_now_utc()} | {line}\n")


def _write_summary(state: str, stats: dict) -> None:
    body = [
        "---",
        f"title: Stage 2A Checkpoint Summary v3 — {state}",
        "type: audit-summary",
        f"created: {_now_utc()}",
        f"created_berlin: {_now_berlin()}",
        "plan_doc: reports/wiki-rebuild-stage-2A-plan-2026-05-11.md",
        f"state: {state}",
        "---",
        "",
        f"# Stage 2A Checkpoint Summary v3 — {state}",
        "",
        f"- **Started (UTC):** {stats.get('started_at', '-')}",
        f"- **Completed (UTC):** {stats.get('ended_at', '-')}",
        f"- **Elapsed:** {stats.get('elapsed_sec', '-')} sec",
        f"- **State:** {state}",
        "",
        "## Tier counts (v3)",
        "",
        f"- Tier A: {stats.get('tier_a', '-')}",
        f"- Tier B: {stats.get('tier_b', '-')}",
        f"- Tier C: {stats.get('tier_c', '-')}",
        f"- Skipped (Контакты / Задачи): {stats.get('skipped', '-')}",
        f"- Match rate (A+B): {stats.get('match_rate', '-')}",
        "",
        "## Throttle / retry events",
        "",
    ]
    events = stats.get("retry_events") or []
    if not events:
        body.append("- (none)")
    else:
        for e in events:
            body.append(
                f"- batch {e.get('batch_idx')} attempt {e.get('attempt')} "
                f"@ {e.get('ts_utc')} — signal: {e.get('signal', '')[:120]}"
            )
    body.extend([
        "",
        "## Halt condition (if any)",
        "",
        f"- {stats.get('halt_reason', '(no halt)')}",
        "",
        "## Deviations from plan-doc",
        "",
        "- **PG-list overrides (plan §3) — deferred** to /wiki-bulk-ack workflow",
        "  next morning. v3 reports carry raw LLM tier classification; preserve-set",
        "  integrity check + override-to-Tier-C will apply during bulk-ack.",
        "- **Delta Stages 1-4 (plan §4.2) — skipped** for tonight. Rerun operates",
        "  on existing 1627 filtered items from 2026-05-10 batch.",
        "- **Quality filters QF-1..QF-5 (plan §2) — not applied** to delta (no delta).",
        "  Existing 1627 items preserve v2 Stage 3 quality status.",
        "",
        "Plan-doc commits these as next-day tasks under Ruslan ack-gate.",
        "",
    ])
    SUMMARY_PATH.write_text("\n".join(body) + "\n", encoding="utf-8")


def _dry_run() -> int:
    """Report delta count + token estimate. No LLM calls. No writes."""
    import subprocess
    print("=" * 70)
    print("Stage 2A DRY-RUN  (no LLM calls, no writes)")
    print(f"  UTC: {_now_utc()}   Berlin: {_now_berlin()}")
    print("=" * 70)

    if not ANNOTATED_PATH.exists():
        print(f"ERROR: baseline annotated missing: {ANNOTATED_PATH}")
        return 1
    annotated = json.loads(ANNOTATED_PATH.read_text(encoding="utf-8"))
    n_items = len(annotated.get("items", []))
    print(f"Baseline annotated items: {n_items}")

    # Delta detection via git log on raw/transcripts/
    cutoff = "2026-05-10 23:46"
    res = subprocess.run(
        ["git", "log", f"--since={cutoff}", "--name-only", "--pretty=format:",
         "--", "raw/transcripts/", "inbox/voice/"],
        cwd=ROOT, capture_output=True, text=True,
    )
    delta_files = [
        l for l in res.stdout.splitlines()
        if l.strip() and ("raw/transcripts/" in l or "inbox/voice/" in l)
    ]
    unique_delta = sorted(set(delta_files))
    print(f"Delta files since {cutoff}: {len(unique_delta)}")
    for f in unique_delta[:10]:
        print(f"  - {f}")
    if len(unique_delta) > 10:
        print(f"  ... ({len(unique_delta) - 10} more)")

    # Existing v2 candidate count from sidecar
    v2_sidecar = OUTPUT_DIR / "04-wiki-candidates-v2.json"
    if v2_sidecar.exists():
        v2 = json.loads(v2_sidecar.read_text(encoding="utf-8"))
        total_cand = v2.get("total_candidates", "?")
        print(f"v2 sidecar — total candidates: {total_cand}, "
              f"A:{v2.get('tier_a_count')} B:{v2.get('tier_b_count')} "
              f"C:{v2.get('tier_c_count')} match%:{v2.get('match_rate')}")
    else:
        print("v2 sidecar missing — cannot derive expected token volume from history")
        total_cand = 1262  # plan-doc estimate

    eligible_estimate = int(total_cand) if isinstance(total_cand, int) else 1262
    batches = (eligible_estimate + 7) // 8
    tokens_in = batches * 14_000
    tokens_out = batches * 1_000
    print(f"\nEstimate (batch=8):")
    print(f"  batches: {batches}")
    print(f"  tokens in: ~{tokens_in:,}  (plan-doc §5.1 ceiling ~2.3M)")
    print(f"  tokens out: ~{tokens_out:,}  (plan-doc §5.1 ceiling ~163K)")
    print(f"  wall-clock @ 30s/batch: ~{batches * 30 // 60} min")
    print(f"  wall-clock @ 60s/batch: ~{batches * 60 // 60} min")

    # Anomaly gates per Ruslan auto-proceed policy:
    #   delta_count <= 20 AND token estimate within plan §5.1
    anomaly = []
    if len(unique_delta) > 20:
        anomaly.append(f"delta {len(unique_delta)} > 20 threshold")
    if tokens_in > 2_400_000:
        anomaly.append(f"tokens_in {tokens_in} > 2.4M ceiling")
    if tokens_out > 200_000:
        anomaly.append(f"tokens_out {tokens_out} > 200K ceiling")
    if anomaly:
        print(f"\nANOMALY — auto-proceed BLOCKED: {anomaly}")
        return 2
    print("\nOK — within auto-proceed gates. Proceed to live run.")
    return 0


def _live_run() -> int:
    """Live LLM rerank. Idempotent — resumes from _checkpoint_v3.json if present."""
    started_at = _now_utc()
    started_mono = time.monotonic()

    if not ANNOTATED_PATH.exists():
        msg = f"ERROR: baseline annotated missing: {ANNOTATED_PATH}"
        print(msg)
        _append_log(msg)
        return 1

    # Set env vars for orchestrator stage_5_wiki_candidates
    os.environ["STAGE5_SKIP_LLM"] = "0"
    os.environ["STAGE5_LLM_BATCH"] = os.environ.get("STAGE5_LLM_BATCH", "8")
    os.environ["STAGE5_CHECKPOINT_EVERY"] = os.environ.get("STAGE5_CHECKPOINT_EVERY", "50")
    os.environ["STAGE5_OUTPUT_SUFFIX"] = "v3"
    os.environ["STAGE5_CHECKPOINT_PATH"] = str(CKPT_PATH)

    # Load orchestrator dynamically (filename has hyphen)
    orch_path = ROOT / "tools" / "voice-pipeline-orchestrator.py"
    spec = importlib.util.spec_from_file_location("voice_pipeline_orchestrator", orch_path)
    orch = importlib.util.module_from_spec(spec)
    sys.modules["voice_pipeline_orchestrator"] = orch
    spec.loader.exec_module(orch)

    filtered_data = json.loads(ANNOTATED_PATH.read_text(encoding="utf-8"))

    lens = {
        "lens_name": "voice-pipeline-2026-05-10-v3",
        "wiki_match_threshold_high": 0.85,
        "wiki_match_threshold_medium": 0.60,
        "wiki_match_top_k_prefilter": 10,
        "wiki_match_skip_below_bm25": 1.0,
        "wiki_propose_new_min_frequency": 1,
    }

    log = orch.DisciplineLog(OUTPUT_DIR / "_stage5_v3_rerun")
    log.path = DISCIPLINE_LOG_PATH

    _append_log(f"Stage 2A v3 LIVE START — {len(filtered_data.get('items', []))} items "
                 f"batch={os.environ['STAGE5_LLM_BATCH']} ckpt_every={os.environ['STAGE5_CHECKPOINT_EVERY']}")
    _append_log(f"checkpoint: {CKPT_PATH}")

    halt_reason = None
    result = None
    try:
        result = orch.stage_5_wiki_candidates(filtered_data, OUTPUT_DIR, log, lens=lens)
        log.write(lens, OUTPUT_DIR)
    except Exception as exc:
        from tools.wiki_integration.llm_ranker import ThrottleError
        if isinstance(exc, ThrottleError):
            halt_reason = f"THROTTLE_EXHAUSTED: {exc}"
        else:
            halt_reason = f"FATAL: {type(exc).__name__}: {exc}"
        _append_log(f"HALT — {halt_reason}")
        # Try Telegram via inbox-processor mailbox (best-effort, file-only)
        try:
            _telegram_halt(halt_reason)
        except Exception as te:
            _append_log(f"telegram dispatch failed: {te}")

    elapsed_sec = int(time.monotonic() - started_mono)
    ended_at = _now_utc()

    # Read checkpoint for retry_events
    retry_events = []
    if CKPT_PATH.exists():
        try:
            ckpt = json.loads(CKPT_PATH.read_text(encoding="utf-8"))
            retry_events = ckpt.get("retry_events", [])
        except Exception:
            pass

    stats = {
        "started_at": started_at,
        "ended_at": ended_at,
        "elapsed_sec": elapsed_sec,
        "retry_events": retry_events,
        "halt_reason": halt_reason,
    }
    if result:
        stats.update({
            "tier_a": result.get("tier_a"),
            "tier_b": result.get("tier_b"),
            "tier_c": result.get("tier_c"),
            "skipped": result.get("skipped"),
            "match_rate": f"{result.get('match_rate', 0):.1%}",
        })

    state = "HALT" if halt_reason else "COMPLETED"
    _write_summary(state, stats)
    _append_log(f"Stage 2A v3 LIVE END — state={state} elapsed={elapsed_sec}s")
    return 1 if halt_reason else 0


def _telegram_halt(reason: str) -> None:
    """Best-effort halt notification via inbox-processor mailbox file."""
    mb_dir = ROOT / "comms" / "mailboxes"
    mb_dir.mkdir(parents=True, exist_ok=True)
    msg = {
        "msg_id": f"msg-stage2a-halt-{int(time.time())}",
        "from": "wiki-rerank-worker",
        "to": "inbox-processor",
        "ts": _now_utc(),
        "subject": "[Stage 2A HALT]",
        "body": (
            f"Stage 2A v3 HALT — {reason}.\n"
            f"Checkpoint: {CKPT_PATH}.\n"
            f"Discipline log: {DISCIPLINE_LOG_PATH}.\n"
            f"Plan-doc: reports/wiki-rebuild-stage-2A-plan-2026-05-11.md.\n"
            "Telegram push if available; else file-only per plan §5.4.3 Tier-2."
        ),
        "tier": 2,
    }
    line = json.dumps(msg, ensure_ascii=False) + "\n"
    target = mb_dir / "inbox-processor.jsonl"
    with target.open("a", encoding="utf-8") as f:
        f.write(line)


def main(argv: list[str]) -> int:
    if "--dry-run" in argv or os.environ.get("STAGE5_DRY_RUN") == "1":
        return _dry_run()
    return _live_run()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
