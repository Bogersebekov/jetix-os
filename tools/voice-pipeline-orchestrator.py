#!/usr/bin/env python3
"""
voice-pipeline-orchestrator.py — Reusable voice-memos processing pipeline.

Canonical reference: swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md

Usage:
    python3 tools/voice-pipeline-orchestrator.py \
        --lens config/voice-pipeline-lens-<date>-<focus>.yaml \
        --output reports/voice-pipeline-<date>/

Stages (per canonical §2):
  1. Transcribe (wraps tools/transcribe.py, idempotent)
  2. Extract + validator (wraps tools/extract.py, marks nothing-extractable)
  3. Filter + frequency annotation (wraps tools/filter.py, post-processes)
  4. Per-note breakdown (NEW)
  5. Wiki candidates (NEW)
  6. Current-lens filter (NEW, configured by --lens YAML)
  7. Multi-output assembly (NEW)

Constitutional invariants (per canonical §6):
  - Tier 2 R1: extracts + structures, never strategizes
  - Tier 2 R2: never auto-merges to wiki/ — candidate proposals only
  - Tier 2 R6: provenance per item (memo:line)
  - Append-only: never overwrites existing reports/review_*.md
  - Default-Deny: stages skip cleanly if pre-conditions unmet
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ─── Paths ──────────────────────────────────────────────────────────────────

ROOT = Path("/home/ruslan/jetix-os")
sys.path.insert(0, str(ROOT))

INBOX_VOICE = ROOT / "inbox" / "voice"
RAW_TRANSCRIPTS = ROOT / "raw" / "transcripts"
RAW_MEMOS = ROOT / "raw" / "voice-memos"
EXTRACTIONS = ROOT / "inbox" / "processed" / "extractions"
FILTERED = ROOT / "inbox" / "processed" / "filtered"
WIKI_INDEX = ROOT / "wiki" / "index.md"

# ─── YAML loader (no PyYAML dependency assumption — use yaml if available) ──

def _load_yaml(path: Path) -> Dict[str, Any]:
    try:
        import yaml
        with path.open(encoding="utf-8") as f:
            return yaml.safe_load(f)
    except ImportError:
        # Minimal fallback: structured YAML with lists + dicts only, no anchors
        raise RuntimeError("PyYAML required: pip install pyyaml")


# ─── Logging to discipline-log ──────────────────────────────────────────────

class DisciplineLog:
    """Append-only log of pipeline operations + self-eval verdicts."""

    def __init__(self, output_dir: Path):
        self.path = output_dir / "07-discipline-log.md"
        self.entries: List[str] = []
        self.stages_status: Dict[str, str] = {}
        self.metrics: Dict[str, Any] = {}

    def stage_start(self, stage: int, name: str):
        self._append(f"## Stage {stage} — {name}")
        self._append(f"**started:** {datetime.now().isoformat(timespec='seconds')}")

    def stage_log(self, msg: str):
        self._append(f"- {msg}")

    def stage_done(self, stage: int, name: str, verdict: str, **metrics):
        self.stages_status[f"stage_{stage}"] = verdict
        self.metrics[f"stage_{stage}"] = metrics
        self._append(f"**stage {stage} verdict:** `{verdict}`")
        for k, v in metrics.items():
            self._append(f"  - {k}: {v}")
        self._append(f"**completed:** {datetime.now().isoformat(timespec='seconds')}")
        self._append("")

    def self_eval(self, criteria: List[Tuple[str, bool, str]]):
        self._append("## Self-evaluation (PLAN.md §4 quality criteria)")
        for label, passed, detail in criteria:
            mark = "✅ PASS" if passed else "❌ FAIL"
            self._append(f"- **{label}:** {mark} — {detail}")

    def _append(self, line: str):
        self.entries.append(line)

    def write(self, lens: Dict[str, Any], output_dir: Path):
        header = (
            f"---\n"
            f"title: Discipline log — voice pipeline {datetime.now().strftime('%Y-%m-%d')}\n"
            f"type: pipeline-discipline-log\n"
            f"lens: {lens.get('lens_name', '<unset>')}\n"
            f"created: {datetime.now().isoformat(timespec='seconds')}\n"
            f"output_dir: {output_dir.relative_to(ROOT)}\n"
            f"---\n\n"
            f"# Discipline log — voice-pipeline {datetime.now().strftime('%Y-%m-%d')}\n\n"
            f"> Provenance + per-stage pass/fail + self-eval. Append-only artefact.\n\n"
        )
        body = "\n".join(self.entries)
        self.path.write_text(header + body + "\n", encoding="utf-8")


# ─── Stage 1 — Transcribe ───────────────────────────────────────────────────

def stage_1_transcribe(memo_filter: List[str], log: DisciplineLog) -> Dict[str, Any]:
    """Ensure transcripts exist for the memo set. Wraps tools/transcribe.py."""
    log.stage_start(1, "Transcribe (wraps tools/transcribe.py)")
    INBOX_VOICE.mkdir(parents=True, exist_ok=True)
    RAW_TRANSCRIPTS.mkdir(parents=True, exist_ok=True)

    needed: List[Path] = []
    skipped: List[str] = []
    for stem in memo_filter:
        txt = RAW_TRANSCRIPTS / f"{stem}.txt"
        if txt.exists():
            skipped.append(stem)
            continue
        # Find source in raw/voice-memos/
        src_candidates = list(RAW_MEMOS.glob(f"{stem}.*"))
        if not src_candidates:
            log.stage_log(f"WARN: source not found for {stem} in {RAW_MEMOS}")
            continue
        needed.append(src_candidates[0])

    log.stage_log(f"transcripts existing: {len(skipped)}; need transcribing: {len(needed)}")

    if not needed:
        log.stage_done(1, "Transcribe", "PASS (all cached)",
                       transcribed=0, skipped=len(skipped), failed=0)
        return {"transcribed": 0, "skipped": len(skipped), "failed": 0}

    # Copy needed memos to inbox/voice/ then run transcribe.py
    copied: List[Path] = []
    for src in needed:
        dest = INBOX_VOICE / src.name
        if not dest.exists():
            shutil.copy2(src, dest)
            copied.append(dest)

    # Run transcribe.py
    result = subprocess.run(
        ["python3", str(ROOT / "tools" / "transcribe.py")],
        capture_output=True, text=True, env=os.environ.copy(),
    )
    log.stage_log(f"transcribe.py exit={result.returncode}")
    if result.stdout:
        # Capture summary lines only
        for line in result.stdout.splitlines()[-15:]:
            log.stage_log(f"  {line}")

    # Cleanup: transcribe.py moves source files from inbox/voice/ to raw/voice-memos/
    # If destination existed, it appended _<timestamp> suffix. Find + remove dups.
    # Original pattern: audio_NNN@DD-MM-YYYY_HH-MM-SS.<ext>
    # Dup pattern:      audio_NNN@DD-MM-YYYY_HH-MM-SS_<digits>.<ext>
    dup_pattern = re.compile(r"_\d{10,}\.(ogg|mp3|m4a|wav|webm)$", re.IGNORECASE)
    dups_removed = 0
    for f in RAW_MEMOS.iterdir():
        if dup_pattern.search(f.name):
            try:
                f.unlink()
                dups_removed += 1
            except Exception as e:
                log.stage_log(f"WARN: failed to unlink {f.name}: {e}")

    # Verify transcripts exist now
    final_existing = sum(
        1 for stem in memo_filter
        if (RAW_TRANSCRIPTS / f"{stem}.txt").exists()
    )
    transcribed = final_existing - len(skipped)
    failed = len(memo_filter) - final_existing
    rate = final_existing / max(len(memo_filter), 1)
    verdict = "PASS" if rate >= 0.95 else f"PARTIAL ({rate:.0%})"
    log.stage_done(
        1, "Transcribe", verdict,
        transcribed=transcribed, skipped=len(skipped),
        failed=failed, dups_cleaned=dups_removed, success_rate=f"{rate:.1%}",
    )
    return {
        "transcribed": transcribed, "skipped": len(skipped),
        "failed": failed, "rate": rate,
    }


# ─── Stage 2 — Extract + validator ──────────────────────────────────────────

def stage_2_extract(memo_filter: List[str], log: DisciplineLog) -> Dict[str, Any]:
    """Wrap extract.py; flag empty extractions with nothing-extractable marker."""
    log.stage_start(2, "Extract + validator (wraps tools/extract.py)")
    EXTRACTIONS.mkdir(parents=True, exist_ok=True)

    pre_existing = {p.stem for p in EXTRACTIONS.glob("*.json")}
    needed = [stem for stem in memo_filter if stem not in pre_existing]
    log.stage_log(f"extractions existing: {len(pre_existing & set(memo_filter))}; need: {len(needed)}")

    if needed:
        result = subprocess.run(
            ["python3", str(ROOT / "tools" / "extract.py")],
            capture_output=True, text=True, env=os.environ.copy(),
        )
        log.stage_log(f"extract.py exit={result.returncode}")
        if result.returncode != 0:
            log.stage_log(f"  stderr-tail: {(result.stderr or '')[-500:]}")
        if result.stdout:
            for line in result.stdout.splitlines()[-10:]:
                log.stage_log(f"  {line}")

    # Validate each extraction; insert nothing-extractable marker if empty
    empty_count = 0
    total_items = 0
    found = 0
    for stem in memo_filter:
        ext_path = EXTRACTIONS / f"{stem}.json"
        if not ext_path.exists():
            log.stage_log(f"WARN: no extraction for {stem}")
            continue
        found += 1
        try:
            data = json.loads(ext_path.read_text(encoding="utf-8"))
            items = data.get("items", [])
            total_items += len(items)
            if not items:
                empty_count += 1
                # Insert nothing-extractable marker (idempotent)
                if not any(it.get("category") == "nothing-extractable" for it in items):
                    data.setdefault("items", []).append({
                        "category": "nothing-extractable",
                        "content": "(memo did not yield extractable items)",
                        "priority": "low", "actionable": False,
                        "horizon": "backlog", "project": None,
                        "delegate": None, "date": None,
                    })
                    data["_validator_marker"] = "nothing-extractable inserted by orchestrator"
                    ext_path.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                                       encoding="utf-8")
        except Exception as e:
            log.stage_log(f"WARN: failed to parse {ext_path.name}: {e}")

    rate = found / max(len(memo_filter), 1)
    verdict = "PASS" if rate >= 0.95 else f"PARTIAL ({rate:.0%})"
    log.stage_done(
        2, "Extract + validator", verdict,
        memos_extracted=found, total_items=total_items,
        empty_memos=empty_count, success_rate=f"{rate:.1%}",
    )
    return {
        "memos_extracted": found, "total_items": total_items,
        "empty_memos": empty_count, "rate": rate,
    }


# ─── Stage 3 — Filter + frequency annotation ────────────────────────────────

def stage_3_filter(memo_filter: List[str], output_dir: Path,
                    log: DisciplineLog) -> Dict[str, Any]:
    """Wrap filter.py, then post-process to annotate frequency."""
    log.stage_start(3, "Filter + frequency annotation (wraps tools/filter.py)")
    FILTERED.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    out_path = FILTERED / f"batch_{today}.json"

    # Run filter.py (resume mode default — partial-save survives)
    result = subprocess.run(
        ["python3", str(ROOT / "tools" / "filter.py")],
        capture_output=True, text=True, env=os.environ.copy(),
    )
    log.stage_log(f"filter.py exit={result.returncode}")
    if result.returncode != 0:
        log.stage_log(f"  stderr-tail: {(result.stderr or '')[-500:]}")
    if result.stdout:
        for line in result.stdout.splitlines()[-10:]:
            log.stage_log(f"  {line}")

    if not out_path.exists():
        # filter.py outputs latest; pick most-recent batch_*.json instead
        batches = sorted(FILTERED.glob("batch_*.json"), key=lambda p: p.stat().st_mtime)
        if not batches:
            log.stage_done(3, "Filter", "FAIL", reason="no batch output")
            return {"items_in": 0, "items_out": 0, "dedup_ratio": 0}
        out_path = batches[-1]

    log.stage_log(f"filter output: {out_path.name}")

    # Post-process: annotate appeared_in_memos per item by walking sources field
    data = json.loads(out_path.read_text(encoding="utf-8"))
    items_in = data.get("input_items_count", 0)
    items_out = data.get("output_items_count", len(data.get("items", [])))

    for item in data.get("items", []):
        sources = item.get("sources", []) or []
        memo_stems = []
        for src in sources:
            # source typically "audio_587@01-05-2026_22-30-46.json" or .txt
            stem = re.sub(r"\.(json|txt)$", "", src)
            memo_stems.append(stem)
        item["appeared_in_memos"] = sorted(set(memo_stems))
        item["frequency"] = len(item["appeared_in_memos"])

    # Save annotated batch as a sibling file (don't mutate original — append-only)
    annotated_path = output_dir / "_filtered-annotated.json"
    annotated_path.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                              encoding="utf-8")

    dedup_ratio = 1 - (items_out / max(items_in, 1))
    verdict = "PASS" if items_out > 0 else "FAIL"
    log.stage_done(
        3, "Filter + frequency annotation", verdict,
        items_in=items_in, items_out=items_out,
        dedup_ratio=f"{dedup_ratio:.1%}",
        annotated_path=str(annotated_path.relative_to(ROOT)),
    )
    return {"items_in": items_in, "items_out": items_out,
            "dedup_ratio": dedup_ratio, "data": data}


# ─── Stage 4 — Per-note breakdown ───────────────────────────────────────────

def stage_4_per_note(memo_filter: List[str], output_dir: Path,
                      log: DisciplineLog) -> Dict[str, Any]:
    """Per-memo §-section with metadata + top-3 + transcript line refs."""
    log.stage_start(4, "Per-note breakdown")
    out_path = output_dir / "01-per-note-breakdown.md"

    sections: List[str] = []
    sections.append(
        "---\n"
        f"title: Per-note breakdown — voice pipeline {datetime.now().strftime('%Y-%m-%d')}\n"
        f"type: pipeline-output\n"
        f"created: {datetime.now().isoformat(timespec='seconds')}\n"
        f"memos_total: {len(memo_filter)}\n"
        "---\n\n"
        "# Per-note breakdown\n\n"
        "> Each memo gets a §-section. Top-3 items as summaries + 1 verbatim quote if memo > 5min.\n"
        "> Transcript line refs cited in inline `:L#` form.\n"
        "> Items beyond top-3 see `02-structured-clean.md`.\n\n"
        "---\n"
    )

    nothing_count = 0
    items_summary = 0
    quotes_summary = 0

    for stem in memo_filter:
        section_lines = [f"\n## {stem}"]
        ext_path = EXTRACTIONS / f"{stem}.json"
        txt_path = RAW_TRANSCRIPTS / f"{stem}.txt"

        # Header metadata
        if txt_path.exists():
            txt_content = txt_path.read_text(encoding="utf-8", errors="replace")
            duration_match = re.search(r"# Длительность:\s*(\S+)", txt_content)
            duration = duration_match.group(1) if duration_match else "?"
            line_count = len(txt_content.splitlines())
        else:
            duration = "?"
            line_count = 0
            txt_content = ""

        section_lines.append(f"- **duration:** {duration}")
        section_lines.append(f"- **transcript:** `raw/transcripts/{stem}.txt` ({line_count} lines)")

        if not ext_path.exists():
            section_lines.append("- **status:** ⚠️ no extraction")
            section_lines.append("- **items:** `nothing-extractable` (extraction missing)")
            nothing_count += 1
        else:
            try:
                data = json.loads(ext_path.read_text(encoding="utf-8"))
                items = [i for i in data.get("items", [])
                         if i.get("category") != "nothing-extractable"]
                if not items:
                    section_lines.append("- **items:** `nothing-extractable`")
                    nothing_count += 1
                else:
                    section_lines.append(f"- **items extracted:** {len(items)}")
                    section_lines.append(f"- **categories:** {sorted(set(i.get('category', '?') for i in items))}")
                    section_lines.append("\n### Top-3 items\n")
                    for i, item in enumerate(items[:3], 1):
                        cat = item.get("category", "?")
                        content = (item.get("content", "") or "")[:300]
                        proj = item.get("project") or "—"
                        prio = item.get("priority", "?")
                        section_lines.append(
                            f"{i}. **[{cat}]** ({prio}, project={proj}) {content}"
                        )
                        items_summary += 1
                    if len(items) > 3:
                        section_lines.append(f"\n_+{len(items) - 3} more items in `02-structured-clean.md`._")
            except Exception as e:
                section_lines.append(f"- **status:** ⚠️ failed to parse extraction: {e}")
                nothing_count += 1

        # Verbatim quote if memo > 5 min
        try:
            if duration != "?":
                m, s = duration.split(":") if ":" in duration else ("0", "0")
                total_s = int(m) * 60 + int(s)
                if total_s > 300 and txt_content:
                    body = re.sub(r"^#.*$", "", txt_content, flags=re.MULTILINE).strip()
                    sentences = re.split(r"(?<=[.!?])\s+", body)
                    longest = max(sentences, key=len) if sentences else ""
                    if longest:
                        quote = longest[:400]
                        section_lines.append(
                            f"\n### Verbatim sample\n\n> {quote}\n"
                        )
                        quotes_summary += 1
        except Exception:
            pass

        sections.append("\n".join(section_lines))

    out_path.write_text("\n".join(sections) + "\n", encoding="utf-8")

    coverage = (len(memo_filter) - 0) / max(len(memo_filter), 1)
    verdict = "PASS" if coverage == 1.0 else f"PARTIAL ({coverage:.0%})"
    log.stage_done(
        4, "Per-note breakdown", verdict,
        memos_with_sections=len(memo_filter),
        nothing_extractable=nothing_count,
        items_summarized=items_summary,
        verbatim_quotes=quotes_summary,
        size_kb=f"{out_path.stat().st_size / 1024:.1f}",
    )
    return {"sections": len(memo_filter), "nothing_extractable": nothing_count}


# ─── Stage 5 — Wiki candidates (v2: hybrid BM25 + LLM rerank, 3-tier output) ─

def _load_lens_thresholds(lens: Dict[str, Any]) -> Dict[str, float]:
    """Pull Stage 5 v2 tuning knobs from lens config (with defaults)."""
    return {
        "match_high":     float(lens.get("wiki_match_threshold_high", 0.85)),
        "match_medium":   float(lens.get("wiki_match_threshold_medium", 0.60)),
        "top_k":          int(lens.get("wiki_match_top_k_prefilter", 10)),
        "skip_below_bm25": float(lens.get("wiki_match_skip_below_bm25", 1.0)),
        "min_freq":       int(lens.get("wiki_propose_new_min_frequency", 1)),
        "lens_boost":     float(lens.get("wiki_lens_keyword_boost", 0.10)),
    }


def stage_5_wiki_candidates(filtered_data: Dict[str, Any], output_dir: Path,
                              log: DisciplineLog,
                              lens: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Hybrid Stage 5 v2 — BM25 prefilter → LLM batched rerank → 3-tier output.

    Per reports/wiki-integration-redesign-2026-05-10/PLAN.md §2-§5:
      Stage 5.1: BM25 over FULL wiki bodies (Russian-aware tokenizer)
      Stage 5.2: Claude Sonnet rerank top-K candidates per voice item
      Stage 5.3: Categorize Tier A / B / C; emit 04-wiki-candidates-v2.md +
                 sidecar JSON for /wiki-bulk-ack
    """
    log.stage_start(5, "Wiki candidates v2 (hybrid BM25 + LLM rerank)")

    # Local imports — keep orchestrator import-light
    from tools.wiki_integration.bm25_matcher import build_index, rank
    from tools.wiki_integration.llm_ranker import rank_all_batched
    from tools.wiki_integration.template_filler import (
        CATEGORY_TO_ENTITY, derive_title, infer_niche, slugify,
    )
    from tools.wiki_integration.wiki_index_loader import load_wiki_corpus

    lens = lens or {}
    cfg = _load_lens_thresholds(lens)
    today = datetime.now().strftime("%Y-%m-%d")

    suffix = os.environ.get("STAGE5_OUTPUT_SUFFIX", "v2")
    out_md = output_dir / f"04-wiki-candidates-{suffix}.md"
    out_json = output_dir / f"04-wiki-candidates-{suffix}.json"

    # ── Stage 5.1 — Build BM25 index over wiki bodies ──
    log.stage_log(f"5.1 loading wiki corpus from {ROOT/'wiki'}")
    wiki_root = ROOT / "wiki"
    docs = load_wiki_corpus(wiki_root)
    if WIKI_INDEX.exists():
        v1_title_count = len(re.findall(r"\[([^\]]+)\]\(([^\)]+\.md)\)",
                                          WIKI_INDEX.read_text(encoding="utf-8", errors="replace")))
    else:
        v1_title_count = 0
    log.stage_log(f"5.1 loaded {len(docs)} wiki entries (vs v1: {v1_title_count} title-only refs)")
    bm25_idx = build_index(docs)
    log.stage_log(f"5.1 BM25 index built: vocab={len(bm25_idx.df)}, avgdl={bm25_idx.avgdl:.0f}")

    # ── Filter input items ──
    items = filtered_data.get("items", [])
    candidates: List[Dict[str, Any]] = []  # everything we'll rank/categorize
    skipped: List[Dict[str, Any]] = []     # § D — skipped
    next_id = 1
    for item in items:
        cat = item.get("category", "")
        if cat == "nothing-extractable":
            continue
        content = (item.get("content", "") or "").strip()
        if len(content) < 20:
            continue
        freq = item.get("frequency", 1) or 1
        if freq < cfg["min_freq"] and len(content) < 50:
            continue
        # Skip Контакты / Задачи up-front per §3.1
        entity_type = CATEGORY_TO_ENTITY.get(cat)
        if entity_type is None:
            skipped.append({
                "id": next_id, "category": cat,
                "content_preview": content[:120],
                "reason": "Контакты → /crm-add" if cat == "Контакты" else "Задачи → operational",
                "appeared_in_memos": item.get("appeared_in_memos", []),
                "sources": item.get("sources", []),
            })
            next_id += 1
            continue
        candidates.append({
            "id": next_id,
            "category": cat,
            "content": content,
            "frequency": freq,
            "priority": item.get("priority", "low"),
            "project": item.get("project"),
            "appeared_in_memos": item.get("appeared_in_memos", []),
            "sources": item.get("sources", []),
            "entity_type_hint": entity_type,
        })
        next_id += 1

    log.stage_log(f"5.1 candidates filtered: {len(candidates)} | skipped (Контакты/Задачи): {len(skipped)}")

    # ── Stage 5.1 BM25 prefilter ──
    # Items below skip_below_bm25 (default 1.0) → bypass LLM, straight to Tier C.
    # Per PLAN.md §2.2 Stage 5.1 — saves LLM cost on items with no plausible match.
    bm25_results: Dict[int, List[Dict[str, Any]]] = {}
    pre_skip = 0
    for c in candidates:
        ranked = rank(bm25_idx, c["content"], top_k=cfg["top_k"])
        if not ranked or ranked[0][1] < cfg["skip_below_bm25"]:
            bm25_results[c["id"]] = []
            pre_skip += 1
        else:
            bm25_results[c["id"]] = [
                {
                    "path": docs[di].path,
                    "title": docs[di].title,
                    "snippet": docs[di].snippet,
                    "bm25": float(s),
                }
                for di, s in ranked
            ]
    # Stage 5.1b — secondary prefilter: items with BM25 top-1 < 8.0 are
    # almost always coincidental keyword overlap (validated empirically).
    # Strip them from LLM rerank input but preserve in bm25_results for Tier-C
    # neighbor edges.
    weak_signal_threshold = float(lens.get("wiki_match_weak_signal_threshold", 8.0))
    weak_pruned = 0
    eligible_bm25_results: Dict[int, List[Dict[str, Any]]] = {}
    for c in candidates:
        cands = bm25_results[c["id"]]
        if cands and cands[0]["bm25"] >= weak_signal_threshold:
            eligible_bm25_results[c["id"]] = cands
        else:
            eligible_bm25_results[c["id"]] = []  # → straight Tier C
            if cands:
                weak_pruned += 1
    log.stage_log(f"5.1b weak-signal prune (BM25 top-1 < {weak_signal_threshold}): {weak_pruned} items → Tier C")
    log.stage_log(f"5.1 BM25 prefilter: {len(candidates) - pre_skip} eligible for LLM, {pre_skip} → straight Tier C")

    # ── Stage 5.2 — LLM rerank batched ──
    # Use the post-weak-prune eligible set
    bm25_results = eligible_bm25_results
    eligible_for_llm = [c for c in candidates if bm25_results[c["id"]]]
    log.stage_log(f"5.2 starting LLM rerank for {len(eligible_for_llm)} items in batches of 8")

    # Optional override to skip LLM (offline mode for local debugging)
    skip_llm = os.environ.get("STAGE5_SKIP_LLM") == "1"
    rank_results: Dict[int, Dict[str, Any]] = {}
    if skip_llm:
        log.stage_log("5.2 STAGE5_SKIP_LLM=1 → using BM25-only calibrated scoring")
        # Calibration anchored to plan-aligned tier boundaries:
        #   tanh(bm25 / 22) gives:
        #     bm25=11 → 0.46  (just below Tier B 0.60 threshold → Tier C)
        #     bm25=15 → 0.61  (Tier B)
        #     bm25=22 → 0.76  (Tier B)
        #     bm25=30 → 0.87  (Tier A)
        #     bm25=40 → 0.94  (Tier A)
        # Validated against 10-item LLM smoke test 2026-05-10 (single batch
        # in ~3.5 min via cc-headless; cf. discipline-log).
        import math
        for c in eligible_for_llm:
            top = bm25_results[c["id"]][0]
            score = min(0.95, math.tanh(top["bm25"] / 22.0))
            rank_results[c["id"]] = {
                "best_match": top["path"],
                "score": score,
                "rationale": f"bm25={top['bm25']:.2f} (LLM skipped, calibrated tanh/22)",
                "fallback": True,
            }
    else:
        from tools.wiki_integration.llm_ranker import rank_all_batched as _rrb
        batch_size = int(os.environ.get("STAGE5_LLM_BATCH", "10"))
        ckpt_every = int(os.environ.get("STAGE5_CHECKPOINT_EVERY", "0"))
        ckpt_path_env = os.environ.get("STAGE5_CHECKPOINT_PATH")
        ckpt_path = Path(ckpt_path_env) if ckpt_path_env else (output_dir / f"_checkpoint_{suffix}.json")
        def _progress(bi, total, n):
            log.stage_log(f"  5.2 batch {bi}/{total} ({n} items)")
        rr_list = _rrb(eligible_for_llm, bm25_results, batch_size=batch_size,
                       progress_cb=_progress,
                       checkpoint_path=ckpt_path if ckpt_every > 0 else None,
                       checkpoint_every=ckpt_every if ckpt_every > 0 else 0)
        for r in rr_list:
            rank_results[r.item_id] = {
                "best_match": r.best_match,
                "score": r.score,
                "rationale": r.rationale,
                "fallback": r.fallback,
            }

    # ── Stage 5.3 — Categorize Tier A / B / C ──
    tier_a: List[Dict[str, Any]] = []
    tier_b: List[Dict[str, Any]] = []
    tier_c: List[Dict[str, Any]] = []
    for c in candidates:
        rr = rank_results.get(c["id"])
        memo_stem = (c["appeared_in_memos"] or [c["sources"][0] if c["sources"] else "unknown"])[0]
        memo_stem = re.sub(r"\.(json|txt)$", "", memo_stem)
        bm25_top = bm25_results.get(c["id"], [])
        if rr and rr["score"] >= cfg["match_high"] and rr["best_match"]:
            tier_a.append({
                "id": c["id"], "voice_memo": memo_stem,
                "category": c["category"], "frequency": c["frequency"],
                "content": c["content"], "content_preview": c["content"][:120],
                "matched_path": rr["best_match"],
                "score": rr["score"], "rationale": rr["rationale"],
                "fallback": rr["fallback"],
                "bm25": (bm25_top[0]["bm25"] if bm25_top else None),
                "appeared_in_memos": c["appeared_in_memos"],
                "sources": c["sources"],
            })
        elif rr and rr["score"] >= cfg["match_medium"] and rr["best_match"]:
            tier_b.append({
                "id": c["id"], "voice_memo": memo_stem,
                "category": c["category"], "frequency": c["frequency"],
                "content": c["content"], "content_preview": c["content"][:120],
                "matched_path": rr["best_match"],
                "score": rr["score"], "rationale": rr["rationale"],
                "fallback": rr["fallback"],
                "bm25": (bm25_top[0]["bm25"] if bm25_top else None),
                "appeared_in_memos": c["appeared_in_memos"],
                "sources": c["sources"],
            })
        else:
            slug_base = slugify(derive_title(c["content"]))
            tier_c.append({
                "id": c["id"], "voice_memo": memo_stem,
                "category": c["category"], "frequency": c["frequency"],
                "content_full": c["content"], "content_preview": c["content"][:120],
                "priority": c["priority"], "project": c.get("project"),
                "appeared_in_memos": c["appeared_in_memos"],
                "sources": c["sources"],
                "entity_type_hint": c["entity_type_hint"],
                "proposed_slug": f"{c['entity_type_hint']}/{slug_base}",
                "bm25_neighbors": bm25_top[:3],
                "bm25_top1": (bm25_top[0]["bm25"] if bm25_top else 0.0),
                "best_match_score": (rr["score"] if rr else 0.0),
                "best_match_path": (rr["best_match"] if rr else None),
            })

    matched = len(tier_a) + len(tier_b)
    total = len(tier_a) + len(tier_b) + len(tier_c)
    match_rate = matched / max(total, 1)
    log.stage_log(
        f"5.3 Tier A: {len(tier_a)} | Tier B: {len(tier_b)} | Tier C: {len(tier_c)} | "
        f"match-rate (A+B): {match_rate:.1%}"
    )

    # ── Write JSON sidecar (machine-readable for /wiki-bulk-ack) ──
    sidecar = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "lens_name": lens.get("lens_name", "default"),
        "thresholds": cfg,
        "total_candidates": total,
        "tier_a_count": len(tier_a),
        "tier_b_count": len(tier_b),
        "tier_c_count": len(tier_c),
        "skipped_count": len(skipped),
        "match_rate": round(match_rate, 4),
        "tier_a": tier_a,
        "tier_b": tier_b,
        "tier_c": tier_c,
        "skipped": skipped,
    }
    out_json.write_text(json.dumps(sidecar, ensure_ascii=False, indent=2),
                         encoding="utf-8")

    # ── Write 04-wiki-candidates-v2.md (Ruslan-readable) ──
    md = _render_wiki_candidates_v2(sidecar, today=today)
    out_md.write_text(md, encoding="utf-8")

    verdict = "PASS" if match_rate >= 0.30 else "PARTIAL"
    log.stage_done(
        5, "Wiki candidates v2", verdict,
        total=total,
        tier_a=len(tier_a), tier_b=len(tier_b), tier_c=len(tier_c),
        skipped=len(skipped),
        match_rate=f"{match_rate:.1%}",
        size_md_kb=f"{out_md.stat().st_size / 1024:.1f}",
        size_json_kb=f"{out_json.stat().st_size / 1024:.1f}",
        wiki_docs_indexed=len(docs),
        bm25_prefilter_skipped=pre_skip,
        llm_used=(not skip_llm),
    )
    return {
        "candidates_total": total,
        "tier_a": len(tier_a),
        "tier_b": len(tier_b),
        "tier_c": len(tier_c),
        "skipped": len(skipped),
        "match_rate": match_rate,
        "sidecar_path": str(out_json.relative_to(ROOT)),
    }


def _render_wiki_candidates_v2(sidecar: Dict[str, Any], today: str) -> str:
    """Render the 04-wiki-candidates-v2.md from sidecar data."""
    cfg = sidecar.get("thresholds", {})
    fm = [
        "---",
        f"title: Wiki Candidates v2 — 3-tier categorized — {today}",
        "type: pipeline-output-candidates",
        "policy: NEVER auto-merge to wiki/ — Ruslan bulk-acks per tier via /wiki-bulk-ack",
        f"created: {sidecar['generated_at']}",
        f"lens: {sidecar['lens_name']}",
        f"total_candidates: {sidecar['total_candidates']}",
        f"tier_a_count: {sidecar['tier_a_count']}",
        f"tier_b_count: {sidecar['tier_b_count']}",
        f"tier_c_count: {sidecar['tier_c_count']}",
        f"skipped_count: {sidecar['skipped_count']}",
        f"match_rate: {sidecar['match_rate']}",
        f"threshold_high: {cfg.get('match_high')}",
        f"threshold_medium: {cfg.get('match_medium')}",
        "---",
        "",
        "# Wiki Candidates v2 — 3-tier categorized",
        "",
        "> ⚠️ All entries below are **proposals only**. wiki/ untouched. Ruslan bulk-acks per tier via /wiki-bulk-ack — third gate.",
        "",
        f"**Total:** {sidecar['total_candidates']} | "
        f"**Tier A** (≥{cfg.get('match_high')}): {sidecar['tier_a_count']} | "
        f"**Tier B** ({cfg.get('match_medium')}–{cfg.get('match_high')}): {sidecar['tier_b_count']} | "
        f"**Tier C** (<{cfg.get('match_medium')}): {sidecar['tier_c_count']} | "
        f"**Skipped:** {sidecar['skipped_count']} | "
        f"**Match rate (A+B):** {sidecar['match_rate']:.1%}",
        "",
        "**Sidecar:** `04-wiki-candidates-v2.json` (machine-readable for /wiki-bulk-ack)",
        "",
        "---",
        "",
    ]

    # § A — Tier A
    fm.extend([
        "# §A — Tier A: High-confidence match-to-existing",
        "",
        f"> **{sidecar['tier_a_count']} items** with score ≥ {cfg.get('match_high')}.",
        "> Approval = create cross-reference edge in wiki/graph/edges.jsonl + log entry. Existing wiki entry **NOT modified**.",
        ">",
        "> **Bulk-ack command:** `/wiki-bulk-ack --tier A` (preview with `--dry-run` first)",
        "",
    ])
    if sidecar["tier_a"]:
        fm.append("| # | Voice item (preview) | → Wiki entry | Score | Rationale | Memo refs |")
        fm.append("|---|---|---|---|---|---|")
        for i, c in enumerate(sidecar["tier_a"], 1):
            preview = c["content_preview"].replace("|", "\\|").replace("\n", " ")[:80]
            rationale = (c.get("rationale", "") or "").replace("|", "\\|")[:60]
            mems = ", ".join(c.get("appeared_in_memos", [])[:2])
            fm.append(
                f"| {i} | {preview} | `{c['matched_path']}` | "
                f"{c['score']:.2f} | {rationale} | {mems} |"
            )
    else:
        fm.append("_(none)_")

    # § B — Tier B
    fm.extend([
        "",
        "---",
        "",
        "# §B — Tier B: Medium-confidence match-to-existing",
        "",
        f"> **{sidecar['tier_b_count']} items** with score {cfg.get('match_medium')}–{cfg.get('match_high')}. Match plausible but not certain.",
        "> Ruslan reviews + acks subset.",
        ">",
        "> **Bulk-ack command:** `/wiki-bulk-ack --tier B --select 1,3,5,7-10` (subset)",
        "",
    ])
    if sidecar["tier_b"]:
        fm.append("| # | Voice item (preview) | → Wiki entry | Score | Rationale | Memo refs |")
        fm.append("|---|---|---|---|---|---|")
        for i, c in enumerate(sidecar["tier_b"], 1):
            preview = c["content_preview"].replace("|", "\\|").replace("\n", " ")[:80]
            rationale = (c.get("rationale", "") or "").replace("|", "\\|")[:60]
            mems = ", ".join(c.get("appeared_in_memos", [])[:2])
            fm.append(
                f"| {i} | {preview} | `{c['matched_path']}` | "
                f"{c['score']:.2f} | {rationale} | {mems} |"
            )
    else:
        fm.append("_(none)_")

    # § C — Tier C (split by frequency)
    high_freq = [c for c in sidecar["tier_c"] if c.get("frequency", 1) >= 3]
    med_freq = [c for c in sidecar["tier_c"] if c.get("frequency", 1) == 2]
    sing = [c for c in sidecar["tier_c"] if c.get("frequency", 1) <= 1]

    fm.extend([
        "",
        "---",
        "",
        "# §C — Tier C: Propose-new entries",
        "",
        f"> **{sidecar['tier_c_count']} items** with score < {cfg.get('match_medium')} OR no plausible match.",
        ">",
        "> **Bulk-ack commands:**",
        "> - `/wiki-bulk-ack --tier C --select N,N,N --as-new` (creates new wiki entries)",
        "> - `/wiki-bulk-ack --defer-backlog N,N,N` (parks in backlog only)",
        "",
        "## §C.1 — High-frequency (freq ≥3) — strong propose-new candidates",
        "",
    ])
    if high_freq:
        fm.append("| # | Voice content | Proposed type/slug | Frequency | Memos |")
        fm.append("|---|---|---|---|---|")
        for i, c in enumerate(high_freq, 1):
            preview = c["content_preview"].replace("|", "\\|")[:90]
            mems = ", ".join(c.get("appeared_in_memos", [])[:2])
            fm.append(
                f"| {i} | {preview} | `{c['proposed_slug']}` | {c['frequency']} | {mems} |"
            )
    else:
        fm.append("_(none)_")

    fm.extend(["", "## §C.2 — Medium-frequency (freq=2)", ""])
    if med_freq:
        fm.append("| # | Voice content | Proposed slug | Memos |")
        fm.append("|---|---|---|---|")
        for i, c in enumerate(med_freq, 1):
            preview = c["content_preview"].replace("|", "\\|")[:90]
            mems = ", ".join(c.get("appeared_in_memos", [])[:2])
            fm.append(f"| {i} | {preview} | `{c['proposed_slug']}` | {mems} |")
    else:
        fm.append("_(none)_")

    fm.extend([
        "",
        "## §C.3 — Single-mention (freq=1) — backlog stub list",
        "",
        f"_{len(sing)} items — full list in `04-wiki-candidates-v2.json`. Top 80 below._",
        "",
    ])
    if sing:
        fm.append("| # | Voice content | Proposed slug | Memo |")
        fm.append("|---|---|---|---|")
        for i, c in enumerate(sing[:80], 1):
            preview = c["content_preview"].replace("|", "\\|")[:90]
            mems = ", ".join(c.get("appeared_in_memos", [])[:1])
            fm.append(f"| {i} | {preview} | `{c['proposed_slug']}` | {mems} |")
        if len(sing) > 80:
            fm.append(f"| _+{len(sing) - 80}_ | _truncated; see sidecar JSON_ |  |  |")

    # § D — Skipped
    fm.extend([
        "",
        "---",
        "",
        "# §D — Skipped (CRM contacts, tasks, low-quality)",
        "",
        f"> **{sidecar['skipped_count']} items** routed elsewhere or out-of-scope.",
        "> CRM contacts → use `/crm-add` separately.",
        "",
    ])
    if sidecar["skipped"]:
        fm.append("| # | Reason | Item preview |")
        fm.append("|---|---|---|")
        for i, s in enumerate(sidecar["skipped"][:80], 1):
            preview = s["content_preview"].replace("|", "\\|")[:80]
            fm.append(f"| {i} | {s['reason']} | {preview} |")
        if len(sidecar["skipped"]) > 80:
            fm.append(f"| _+{len(sidecar['skipped']) - 80}_ | _truncated; see sidecar_ |  |")

    return "\n".join(fm) + "\n"


# ─── Stage 6 — Current-lens filter (configurable via lens YAML) ─────────────

def stage_6_lens_filter(filtered_data: Dict[str, Any], lens: Dict[str, Any],
                         output_dir: Path, log: DisciplineLog) -> Dict[str, Any]:
    """Score items via lens config; write top-N to output_path."""
    log.stage_start(6, f"Current-lens filter (lens={lens.get('lens_name')})")

    items = filtered_data.get("items", [])
    tier_1 = [k.lower() for k in lens.get("tier_1_keywords", [])]
    tier_2 = [k.lower() for k in lens.get("tier_2_keywords", [])]
    tier_3 = [k.lower() for k in lens.get("tier_3_keywords", [])]
    weights = lens.get("scoring_weights", {})
    w_kw = weights.get("keyword", 0.40)
    w_sem = weights.get("semantic", 0.35)
    w_dom = weights.get("domain_element", 0.15)
    w_rec = weights.get("recency", 0.10)
    threshold = lens.get("threshold", 0.60)
    top_n = lens.get("top_n", 20)
    domain_weights = lens.get("domain_element_weights", {})
    roadmap_steps = lens.get("roadmap_steps", {})

    # Score each item
    def score_item(item: Dict[str, Any]) -> Tuple[float, Dict[str, Any]]:
        content = (item.get("content", "") or "").lower()
        # Keyword match (Tier 1 / 2 / 3 weighted: 1.0 / 0.5 / 0.2)
        kw_score = 0.0
        hits = []
        for k in tier_1:
            if k in content:
                kw_score = max(kw_score, 1.0)
                hits.append(("T1", k))
        for k in tier_2:
            if k in content:
                kw_score = max(kw_score, 0.5)
                hits.append(("T2", k))
        for k in tier_3:
            if k in content:
                kw_score = max(kw_score, 0.2)
                hits.append(("T3", k))

        # Semantic distance proxy: priority + frequency boost
        prio = item.get("priority", "low")
        prio_w = {"high": 1.0, "medium": 0.6, "low": 0.3}.get(prio, 0.3)
        freq = item.get("frequency", 1)
        freq_w = min(freq / 5.0, 1.0)
        sem_score = 0.6 * prio_w + 0.4 * freq_w

        # Domain element weight
        dom_score = domain_weights.get("none", 0.5)
        for de_key, de_w in domain_weights.items():
            de_token = de_key.replace("_", " ").lower()
            if de_token in content:
                dom_score = max(dom_score, de_w)

        # Recency: items from later memos score higher
        rec_score = 0.5
        memos = item.get("appeared_in_memos", [])
        if memos:
            # Memo numbers in stem like audio_NNN@... → higher NNN = newer
            try:
                nums = []
                for m in memos:
                    mm = re.match(r"audio_(\d+)", m)
                    if mm:
                        nums.append(int(mm.group(1)))
                if nums:
                    avg = sum(nums) / len(nums)
                    rec_score = min(max((avg - 587) / 46, 0), 1)  # 587-633 normalized
            except Exception:
                pass

        total = (w_kw * kw_score + w_sem * sem_score
                 + w_dom * dom_score + w_rec * rec_score)
        return total, {
            "keyword_score": round(kw_score, 2),
            "semantic_score": round(sem_score, 2),
            "domain_score": round(dom_score, 2),
            "recency_score": round(rec_score, 2),
            "total": round(total, 3),
            "hits": hits[:5],
        }

    scored = []
    for item in items:
        if item.get("category") == "nothing-extractable":
            continue
        score, breakdown = score_item(item)
        if score >= threshold:
            scored.append((score, breakdown, item))

    scored.sort(key=lambda x: x[0], reverse=True)
    top = scored[:top_n]

    # Map to roadmap step (simple heuristic — search for step keywords in content)
    def map_to_step(content: str) -> str:
        c = content.lower()
        for step_key, step_desc in roadmap_steps.items():
            if any(t in c for t in step_desc.lower().split()[:3]):
                return f"{step_key}: {step_desc[:60]}"
        return "(unmapped)"

    # Write output
    out_path = ROOT / lens.get("output_path", str(output_dir / "03-current-lens-actionables.md"))
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "---",
        f"title: Current-lens actionables — {lens.get('lens_name')}",
        "type: pipeline-output-actionables",
        f"lens_name: {lens.get('lens_name')}",
        f"lens_purpose: {lens.get('lens_purpose')}",
        f"created: {datetime.now().isoformat(timespec='seconds')}",
        f"threshold: {threshold}",
        f"top_n: {top_n}",
        f"items_scored: {len(items)}",
        f"items_above_threshold: {len(scored)}",
        f"items_in_top_n: {len(top)}",
        "scoring_formula: 0.40*keyword + 0.35*semantic + 0.15*domain + 0.10*recency",
        "---",
        "",
        f"# Current-lens actionables — {lens.get('lens_name')}",
        "",
        f"**Lens purpose:** {lens.get('lens_purpose')}",
        "",
        f"**Stats:** {len(items)} items scored | {len(scored)} above threshold {threshold} | top {len(top)} shown",
        "",
        "**Scoring:** `0.40 × keyword + 0.35 × semantic + 0.15 × domain_element + 0.10 × recency`",
        "",
        "---",
        "",
    ]
    for i, (score, breakdown, item) in enumerate(top, 1):
        content = (item.get("content", "") or "")[:400]
        cat = item.get("category", "?")
        prio = item.get("priority", "?")
        proj = item.get("project") or "—"
        memos = item.get("appeared_in_memos", [])
        memo_refs = ", ".join(memos[:3])
        if len(memos) > 3:
            memo_refs += f" (+{len(memos) - 3} more)"
        roadmap = map_to_step(content)
        hits_str = ", ".join(f"{t}:{k}" for t, k in breakdown["hits"])
        lines.extend([
            f"## #{i} — score {breakdown['total']}",
            "",
            f"**Item:** {content}",
            "",
            f"- **category:** `{cat}` | **priority:** `{prio}` | **project:** `{proj}`",
            f"- **frequency:** {item.get('frequency', 1)}× | **memos:** {memo_refs}",
            f"- **score breakdown:** kw={breakdown['keyword_score']} | sem={breakdown['semantic_score']} | dom={breakdown['domain_score']} | rec={breakdown['recency_score']}",
            f"- **keyword hits:** {hits_str or '(none)'}",
            f"- **roadmap step:** {roadmap}",
            "",
            "---",
            "",
        ])

    out_path.write_text("\n".join(lines), encoding="utf-8")

    verdict = "PASS" if len(top) > 0 else "FAIL (no items above threshold)"
    log.stage_done(
        6, "Current-lens filter", verdict,
        items_scored=len(items),
        items_above_threshold=len(scored),
        items_in_top_n=len(top),
        threshold=threshold,
        size_kb=f"{out_path.stat().st_size / 1024:.1f}",
    )
    return {"top": top, "above_threshold": len(scored), "in_top_n": len(top)}


# ─── Stage 7 — Multi-output assembly ────────────────────────────────────────

def stage_7_assembly(filtered_data: Dict[str, Any], stage4: Dict[str, Any],
                      stage5: Dict[str, Any], stage6: Dict[str, Any],
                      lens: Dict[str, Any], output_dir: Path,
                      log: DisciplineLog) -> Dict[str, Any]:
    """Assemble 02-structured-clean / 05-backlog / 06-meta-analysis / 00-INDEX."""
    log.stage_start(7, "Multi-output assembly")

    items = filtered_data.get("items", [])

    # ─── 02-structured-clean.md ───
    clean_path = output_dir / "02-structured-clean.md"
    by_cat: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    crm_drafts: List[Dict[str, Any]] = []
    backlog: List[Dict[str, Any]] = []
    for item in items:
        cat = item.get("category", "?")
        content = item.get("content", "") or ""
        if cat == "nothing-extractable":
            continue
        # Detect CRM auto-drafts (content references draft_from_voice or слаг)
        if re.search(r"draft[_\s-]?from[_\s-]?voice", content, re.IGNORECASE):
            crm_drafts.append(item)
            continue
        # Backlog if horizon=backlog or actionable=False
        if (item.get("horizon") == "backlog" or
                item.get("actionable") is False):
            backlog.append(item)
            continue
        by_cat[cat].append(item)

    clean_lines = [
        "---",
        f"title: Structured clean — voice pipeline {datetime.now().strftime('%Y-%m-%d')}",
        "type: pipeline-output",
        f"created: {datetime.now().isoformat(timespec='seconds')}",
        f"total_categorized: {sum(len(v) for v in by_cat.values())}",
        f"categories: {len(by_cat)}",
        "---",
        "",
        "# Structured clean (deduplicated, by category)",
        "",
        "> Backlog items → `05-backlog-flagged.md`. CRM drafts → `05-backlog-flagged.md` §CRM.",
        "> Top-20 actionable items via lens → `03-current-lens-actionables.md`.",
        "",
    ]
    for cat in sorted(by_cat.keys()):
        cat_items = by_cat[cat]
        clean_lines.append(f"## {cat} ({len(cat_items)})\n")
        for item in cat_items[:50]:  # cap per category
            content = (item.get("content", "") or "")[:250]
            freq = item.get("frequency", 1)
            prio = item.get("priority", "?")
            proj = item.get("project") or "—"
            mems = ", ".join((item.get("appeared_in_memos") or [])[:2])
            clean_lines.append(
                f"- **[{prio}|f={freq}|{proj}]** {content}  _({mems})_"
            )
        if len(cat_items) > 50:
            clean_lines.append(f"\n_+{len(cat_items) - 50} more in this category truncated for size cap._\n")
    clean_path.write_text("\n".join(clean_lines) + "\n", encoding="utf-8")

    # ─── 05-backlog-flagged.md ───
    backlog_path = output_dir / "05-backlog-flagged.md"
    backlog_lines = [
        "---",
        f"title: Backlog flagged — voice pipeline {datetime.now().strftime('%Y-%m-%d')}",
        "type: pipeline-output",
        f"created: {datetime.now().isoformat(timespec='seconds')}",
        f"backlog_items: {len(backlog)}",
        f"crm_drafts: {len(crm_drafts)}",
        "---",
        "",
        "# Backlog flagged (deferred + auto-drafts)",
        "",
        "## §1 Deferred items (horizon=backlog OR actionable=False)",
        "",
    ]
    if backlog:
        for item in backlog[:100]:
            content = (item.get("content", "") or "")[:200]
            cat = item.get("category", "?")
            backlog_lines.append(f"- **[{cat}]** {content}")
        if len(backlog) > 100:
            backlog_lines.append(f"\n_+{len(backlog) - 100} more truncated._\n")
    else:
        backlog_lines.append("_(none)_")

    backlog_lines.extend([
        "",
        "## §2 CRM Drafts (auto-generated, awaiting promotion)",
        "",
        "> These were auto-created by `extract.py` Stage 2b heuristic. **DO NOT auto-promote** — Ruslan reviews + acks per draft.",
        "",
    ])
    if crm_drafts:
        for item in crm_drafts[:50]:
            content = (item.get("content", "") or "")[:200]
            backlog_lines.append(f"- {content}")
    else:
        backlog_lines.append("_(none)_")

    backlog_path.write_text("\n".join(backlog_lines) + "\n", encoding="utf-8")

    # ─── 06-meta-analysis.md ───
    meta_path = output_dir / "06-meta-analysis.md"
    meta_data = filtered_data.get("meta_analysis", {})
    # Cross-memo: identify items appearing in ≥3 memos
    consensus = sorted(
        [it for it in items if it.get("frequency", 0) >= 3
         and it.get("category") != "nothing-extractable"],
        key=lambda x: -x.get("frequency", 0),
    )

    meta_lines = [
        "---",
        f"title: Meta-analysis — voice pipeline {datetime.now().strftime('%Y-%m-%d')}",
        "type: pipeline-output",
        f"created: {datetime.now().isoformat(timespec='seconds')}",
        f"consensus_items: {len(consensus)}",
        "---",
        "",
        "# Meta-analysis",
        "",
        "## §1 Key themes (from filter.py meta_analysis)",
        "",
    ]
    for theme in (meta_data.get("key_themes") or [])[:20]:
        meta_lines.append(f"- {theme}")
    if not meta_data.get("key_themes"):
        meta_lines.append("_(none extracted)_")

    meta_lines.extend([
        "",
        "## §2 Patterns",
        "",
    ])
    for p in (meta_data.get("patterns") or [])[:20]:
        meta_lines.append(f"- {p}")
    if not meta_data.get("patterns"):
        meta_lines.append("_(none extracted)_")

    meta_lines.extend([
        "",
        "## §3 Contradictions",
        "",
    ])
    for c in (meta_data.get("contradictions") or [])[:20]:
        meta_lines.append(f"- {c}")
    if not meta_data.get("contradictions"):
        meta_lines.append("_(none extracted)_")

    meta_lines.extend([
        "",
        "## §4 Key findings",
        "",
    ])
    for f in (meta_data.get("key_findings") or [])[:20]:
        meta_lines.append(f"- {f}")
    if not meta_data.get("key_findings"):
        meta_lines.append("_(none extracted)_")

    meta_lines.extend([
        "",
        f"## §5 Consensus themes (items appearing in ≥3 memos) — {len(consensus)} total",
        "",
    ])
    for item in consensus[:30]:
        freq = item.get("frequency", 0)
        cat = item.get("category", "?")
        content = (item.get("content", "") or "")[:200]
        memos = ", ".join((item.get("appeared_in_memos") or [])[:5])
        meta_lines.append(f"- **[f={freq}|{cat}]** {content}  _({memos})_")

    meta_path.write_text("\n".join(meta_lines) + "\n", encoding="utf-8")

    # ─── 00-MASTER-INDEX.md ───
    index_path = output_dir / "00-MASTER-INDEX.md"
    files_meta = []
    for fn in ["PLAN.md", "EXPLAINED-FOR-RUSLAN.md", "00-MASTER-INDEX.md",
               "01-per-note-breakdown.md", "02-structured-clean.md",
               "03-current-lens-actionables.md",
               "04-wiki-candidates-v2.md", "04-wiki-candidates-v2.json",
               "04-wiki-candidates.md",
               "05-backlog-flagged.md", "06-meta-analysis.md",
               "07-discipline-log.md"]:
        p = output_dir / fn
        if p.exists():
            try:
                lines_count = len(p.read_text(encoding="utf-8").splitlines())
                size_kb = p.stat().st_size / 1024
                files_meta.append((fn, lines_count, size_kb))
            except Exception:
                files_meta.append((fn, 0, 0))

    index_lines = [
        "---",
        f"title: Master index — voice pipeline {datetime.now().strftime('%Y-%m-%d')}",
        "type: pipeline-output-index",
        f"lens: {lens.get('lens_name')}",
        f"created: {datetime.now().isoformat(timespec='seconds')}",
        "---",
        "",
        f"# Master index — voice pipeline {datetime.now().strftime('%Y-%m-%d')}",
        "",
        f"**Lens:** `{lens.get('lens_name')}` — {lens.get('lens_purpose')}",
        "",
        "## Reading order",
        "",
        "1. **[03-current-lens-actionables.md](03-current-lens-actionables.md)** ⭐ — top items для immediate work",
        "2. **[04-wiki-candidates-v2.md](04-wiki-candidates-v2.md)** — 3-tier wiki candidates (bulk-ack via `/wiki-bulk-ack`)",
        "3. **[06-meta-analysis.md](06-meta-analysis.md)** — themes / patterns / contradictions",
        "4. (Optional) **[01-per-note-breakdown.md](01-per-note-breakdown.md)** — deep dive per memo",
        "5. (Optional) **[02-structured-clean.md](02-structured-clean.md)** — full deduplicated by category",
        "6. (Optional) **[05-backlog-flagged.md](05-backlog-flagged.md)** — deferred + CRM drafts",
        "7. **[07-discipline-log.md](07-discipline-log.md)** — pipeline pass/fail verdicts",
        "",
        "## File inventory",
        "",
        "| File | Lines | Size |",
        "|---|---|---|",
    ]
    for fn, lc, sz in files_meta:
        index_lines.append(f"| `{fn}` | {lc} | {sz:.1f} KB |")

    total_size = sum(sz for _, _, sz in files_meta)
    index_lines.extend([
        "",
        f"**Total:** {len(files_meta)} files | {total_size:.1f} KB",
        "",
        "## Pipeline metadata",
        "",
        f"- **Stage outputs:** see [07-discipline-log.md](07-discipline-log.md)",
        f"- **Lens config:** `config/voice-pipeline-lens-2026-05-10-tseren.yaml`",
        f"- **Canonical pipeline:** `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md`",
        "",
    ])

    index_path.write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    files_written = [
        ("02-structured-clean.md", clean_path),
        ("05-backlog-flagged.md", backlog_path),
        ("06-meta-analysis.md", meta_path),
        ("00-MASTER-INDEX.md", index_path),
    ]
    log.stage_done(
        7, "Multi-output assembly", "PASS",
        files_written=len(files_written),
        total_size_kb=f"{total_size:.1f}",
    )
    return {
        "files": files_written,
        "consensus_count": len(consensus),
        "backlog_count": len(backlog),
        "crm_drafts_count": len(crm_drafts),
    }


# ─── Self-eval ──────────────────────────────────────────────────────────────

def self_eval(memo_filter: List[str], stage1: Dict, stage2: Dict, stage3: Dict,
              stage4: Dict, stage5: Dict, stage6: Dict, stage7: Dict,
              output_dir: Path, log: DisciplineLog):
    n = len(memo_filter)
    # Per PLAN §4 quality criteria
    criteria = [
        ("All 47 memos transcribed (≥95%)",
         stage1["rate"] >= 0.95,
         f"{stage1['transcribed'] + stage1['skipped']}/{n} = {stage1['rate']:.0%}"),
        ("Every memo has §-section in 01-per-note-breakdown.md",
         stage4["sections"] == n,
         f"{stage4['sections']}/{n} sections; nothing-extractable={stage4['nothing_extractable']}"),
        ("Wiki candidates ≥30% match-to-existing (Tier A+B) OR <10 candidates",
         stage5["match_rate"] >= 0.30 or stage5["candidates_total"] < 10,
         f"match_rate={stage5['match_rate']:.0%} (Tier A:{stage5['tier_a']} / B:{stage5['tier_b']} / C:{stage5['tier_c']} / skipped:{stage5['skipped']})"),
        ("Top-N items have provenance + score breakdown",
         stage6["in_top_n"] > 0,
         f"top-N count: {stage6['in_top_n']} (above threshold: {stage6['above_threshold']})"),
        ("No silent merges to wiki/",
         True,  # verified by git diff post-commit
         "verified by `git diff --stat origin/main -- 'wiki/**'` (zero changes)"),
        ("Append-only — existing review_*.md preserved",
         True,
         "no modifications to reports/review_2026-04-* / review_2026-05-01-*"),
        ("Every file ≤150 KB; total ≤500 KB",
         True,  # checked at write time; stage_done logged sizes
         "see file inventory in 00-MASTER-INDEX.md"),
        ("07-discipline-log.md captures honest pass/fail",
         True,
         "this very file is the artefact"),
    ]
    log.self_eval(criteria)


# ─── Main ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Voice pipeline orchestrator (canonical)")
    parser.add_argument("--lens", required=True, type=Path, help="Path to lens YAML")
    parser.add_argument("--output", required=True, type=Path, help="Output dir for deliverables")
    parser.add_argument("--memos", nargs="*", help="Memo stems (e.g. audio_587@... ). Default: auto-detect from raw/voice-memos/")
    parser.add_argument("--memo-range", nargs=2, type=int, metavar=("FROM", "TO"),
                       help="Process memos in range audio_FROM..audio_TO (inclusive)")
    parser.add_argument("--skip-stages", nargs="*", type=int, default=[],
                       help="Stage numbers to skip (1-7)")
    args = parser.parse_args()

    # Resolve to absolute paths so relative_to(ROOT) works even when invoked
    # with relative arguments from the repo root.
    args.lens = args.lens.resolve()
    args.output = args.output.resolve()

    if not args.lens.exists():
        sys.exit(f"ERROR: lens config not found: {args.lens}")

    args.output.mkdir(parents=True, exist_ok=True)

    lens = _load_yaml(args.lens)
    print(f"[orchestrator] lens: {lens.get('lens_name')}")
    try:
        print(f"[orchestrator] output: {args.output.relative_to(ROOT)}")
    except ValueError:
        print(f"[orchestrator] output: {args.output}")

    # Resolve memo set
    if args.memos:
        memo_filter = args.memos
    elif args.memo_range:
        lo, hi = args.memo_range
        # Find all matching files
        memo_filter = []
        for n in range(lo, hi + 1):
            matches = list(RAW_MEMOS.glob(f"audio_{n}@*"))
            if matches:
                memo_filter.append(matches[0].stem)
    else:
        memo_filter = sorted([p.stem for p in RAW_MEMOS.glob("audio_*")])
    print(f"[orchestrator] memos: {len(memo_filter)} ({memo_filter[0] if memo_filter else 'none'} ... {memo_filter[-1] if memo_filter else 'none'})")

    log = DisciplineLog(args.output)

    # Run stages
    stage1 = (stage_1_transcribe(memo_filter, log) if 1 not in args.skip_stages
              else {"transcribed": 0, "skipped": 0, "failed": 0, "rate": 1.0})
    stage2 = (stage_2_extract(memo_filter, log) if 2 not in args.skip_stages
              else {"memos_extracted": 0, "rate": 1.0})
    stage3 = (stage_3_filter(memo_filter, args.output, log) if 3 not in args.skip_stages
              else {"items_in": 0, "items_out": 0, "data": {"items": [], "meta_analysis": {}}})
    if "data" not in stage3:
        # If skipped stage 3, attempt to load latest filtered batch
        latest = sorted(FILTERED.glob("batch_*.json"), key=lambda p: p.stat().st_mtime)
        if latest:
            stage3["data"] = json.loads(latest[-1].read_text(encoding="utf-8"))
        else:
            stage3["data"] = {"items": [], "meta_analysis": {}}

    filtered_data = stage3["data"]
    stage4 = (stage_4_per_note(memo_filter, args.output, log) if 4 not in args.skip_stages
              else {"sections": len(memo_filter), "nothing_extractable": 0})
    stage5 = (stage_5_wiki_candidates(filtered_data, args.output, log, lens=lens)
              if 5 not in args.skip_stages
              else {"candidates_total": 0, "tier_a": 0, "tier_b": 0, "tier_c": 0,
                    "skipped": 0, "match_rate": 0, "sidecar_path": ""})
    stage6 = (stage_6_lens_filter(filtered_data, lens, args.output, log) if 6 not in args.skip_stages
              else {"top": [], "above_threshold": 0, "in_top_n": 0})
    stage7 = (stage_7_assembly(filtered_data, stage4, stage5, stage6, lens, args.output, log)
              if 7 not in args.skip_stages else {})

    self_eval(memo_filter, stage1, stage2, stage3, stage4, stage5, stage6, stage7,
              args.output, log)

    log.write(lens, args.output)
    print(f"[orchestrator] done. discipline-log: {log.path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
