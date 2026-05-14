"""Stage 5 LLM rerank for voice-batch 2026-05-13/14 (10 new transcripts).

Adapted from _rerun_stage5_may_batch.py. Operates on:
  - Input: reports/voice-pipeline-2026-05-13-14-batch/_filtered-annotated.json
    (125 items from 10 new files only — no filter dedup; built directly from
    inbox/processed/extractions/ JSONs)
  - Output: reports/voice-pipeline-2026-05-13-14-batch/04-wiki-candidates-2026-05-13-14-batch.{md,json}
  - Methodology: same as may-batch — BM25 prefilter top-10 + Claude Sonnet 4.6 LLM rerank
    batch=8, thresholds A>=0.85 / B>=0.60, output suffix=2026-05-13-14-batch.

Usage:
    python3 -m tools.wiki_integration._rerun_stage5_2026_05_13_14_batch [--dry-run]
    (or python3 tools/wiki_integration/_rerun_stage5_2026-05-13-14-batch.py)
"""

import importlib.util
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path("/home/ruslan/jetix-os")
sys.path.insert(0, str(ROOT))

OUTPUT_DIR = ROOT / "reports" / "voice-pipeline-2026-05-13-14-batch"
CKPT_PATH = OUTPUT_DIR / "_checkpoint_2026-05-13-14-batch.json"
SUMMARY_PATH = OUTPUT_DIR / "checkpoint-summary-2026-05-13-14-batch.md"
ANNOTATED_PATH = OUTPUT_DIR / "_filtered-annotated.json"
DISCIPLINE_LOG_PATH = OUTPUT_DIR / "_stage5_2026-05-13-14-batch_rerun.log.md"


def _now_utc() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _now_berlin() -> str:
    return time.strftime("%Y-%m-%dT%H:%M %z (Berlin)", time.localtime())


def _append_log(line: str) -> None:
    DISCIPLINE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with DISCIPLINE_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"- {_now_utc()} | {line}\n")


def _write_summary(state: str, stats: dict) -> None:
    body = [
        "---",
        f"title: Stage 5 voice-batch-2026-05-13-14 Checkpoint Summary - {state}",
        "type: audit-summary",
        f"created: {_now_utc()}",
        f"created_berlin: {_now_berlin()}",
        f"state: {state}",
        "---",
        "",
        f"# Stage 5 voice-batch-2026-05-13-14 Checkpoint Summary - {state}",
        "",
        f"- **Started (UTC):** {stats.get('started_at', '-')}",
        f"- **Completed (UTC):** {stats.get('ended_at', '-')}",
        f"- **Elapsed:** {stats.get('elapsed_sec', '-')} sec",
        f"- **State:** {state}",
        "",
        "## Tier counts (voice-batch-2026-05-13-14)",
        "",
        f"- Tier A: {stats.get('tier_a', '-')}",
        f"- Tier B: {stats.get('tier_b', '-')}",
        f"- Tier C: {stats.get('tier_c', '-')}",
        f"- Skipped (Kontakti / Zadachi): {stats.get('skipped', '-')}",
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
                f"@ {e.get('ts_utc')} - signal: {e.get('signal', '')[:120]}"
            )
    body.extend([
        "",
        "## Halt condition (if any)",
        "",
        f"- {stats.get('halt_reason', '(no halt)')}",
        "",
    ])
    SUMMARY_PATH.write_text("\n".join(body) + "\n", encoding="utf-8")


def _live_run() -> int:
    started_at = _now_utc()
    started_mono = time.monotonic()

    if not ANNOTATED_PATH.exists():
        msg = f"ERROR: baseline annotated missing: {ANNOTATED_PATH}"
        print(msg)
        _append_log(msg)
        return 1

    os.environ["STAGE5_SKIP_LLM"] = "0"
    os.environ["STAGE5_LLM_BATCH"] = os.environ.get("STAGE5_LLM_BATCH", "8")
    os.environ["STAGE5_CHECKPOINT_EVERY"] = os.environ.get("STAGE5_CHECKPOINT_EVERY", "25")
    os.environ["STAGE5_OUTPUT_SUFFIX"] = "2026-05-13-14-batch"
    os.environ["STAGE5_CHECKPOINT_PATH"] = str(CKPT_PATH)

    orch_path = ROOT / "tools" / "voice-pipeline-orchestrator.py"
    spec = importlib.util.spec_from_file_location("voice_pipeline_orchestrator", orch_path)
    orch = importlib.util.module_from_spec(spec)
    sys.modules["voice_pipeline_orchestrator"] = orch
    spec.loader.exec_module(orch)

    filtered_data = json.loads(ANNOTATED_PATH.read_text(encoding="utf-8"))

    lens = {
        "lens_name": "voice-pipeline-2026-05-13-14-batch",
        "wiki_match_threshold_high": 0.85,
        "wiki_match_threshold_medium": 0.60,
        "wiki_match_top_k_prefilter": 10,
        "wiki_match_skip_below_bm25": 1.0,
        "wiki_propose_new_min_frequency": 1,
    }

    log = orch.DisciplineLog(OUTPUT_DIR / "_stage5_2026-05-13-14-batch_rerun")
    log.path = DISCIPLINE_LOG_PATH

    _append_log(f"Stage 5 voice-batch-2026-05-13-14 LIVE START - {len(filtered_data.get('items', []))} items "
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
        _append_log(f"HALT - {halt_reason}")

    elapsed_sec = int(time.monotonic() - started_mono)
    ended_at = _now_utc()

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
    _append_log(f"Stage 5 voice-batch-2026-05-13-14 LIVE END - state={state} elapsed={elapsed_sec}s")
    return 1 if halt_reason else 0


def main(argv: list[str]) -> int:
    if "--dry-run" in argv:
        print("[dry-run] would process:", ANNOTATED_PATH)
        print(f"[dry-run] output suffix: 2026-05-13-14-batch")
        print(f"[dry-run] checkpoint: {CKPT_PATH}")
        return 0
    return _live_run()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
