---
title: Voice pipeline 2026-05-16 batch — MASTER INDEX
type: pipeline-output-index
date: 2026-05-16
batch_id: voice-pipeline-2026-05-16-batch
total_audio: 38
common_batch: 14 audio (raw/voice-memos-2026-05-16-batch/)
reflection_batch: 24 audio (raw/voice-memos-2026-05-16-reflection/)
source_commit: 2483e09
processing: claude-code-builtin-tools (no Anthropic API rerank — Tier 2 R no-direct-api)
three_output_split: REFLECTION-INBOX / SELF-OS-SPEC / Jetix-standard (this dir)
classification_per: prompts/voice-reflection-pipeline-deep-prompt-2026-05-16.md §6
language: russian
---

# 🎯 Voice pipeline 2026-05-16 batch — MASTER INDEX

> **Three-output split.** Этот директорий = Output Stream 3 (standard Jetix). Outputs 1 + 2:
> - [decisions/REFLECTION-INBOX-2026-05-16.md](../../decisions/REFLECTION-INBOX-2026-05-16.md) — личное / эмоции / patterns / tasks под себя
> - [decisions/SELF-MANAGEMENT-SYSTEM-SPEC-v0-2026-05-16.md](../../decisions/SELF-MANAGEMENT-SYSTEM-SPEC-v0-2026-05-16.md) — spec Self-OS системы работы с собой

## Quick stats

| Metric | Value |
|---|---|
| Total audio processed | 38 (14 common + 24 reflection) |
| Date range | 10.04.2026 → 16.05.2026 |
| Transcription model | whisper-large-v3 (Groq) |
| Items surfaced (across 3 streams) | ~60 distinct items + ~12 dual-routed |
| Jetix-stream wiki-candidates | 12 (see [04-wiki-candidates.md](04-wiki-candidates.md)) |
| Jetix-stream CRM signals | 2 contacts (Антон-учитель, Цэрэн) |
| Reflection-stream items | ~30 (see REFLECTION-INBOX-2026-05-16.md) |
| Self-OS-stream principles | 9 (P-1..P-9 + 7 inspiration refs) |

## Files in this batch

- `00-MASTER-INDEX.md` (this file) — navigation
- `01-per-note-breakdown.md` — per-audio summary + classification routing
- `04-wiki-candidates.md` — surfaced wiki entries / ideas (no auto-merge per Tier 2 R2)
- `06-meta-analysis.md` — meta observations: themes / clusters / recurrence patterns
- `checkpoint-summary.md` — quick completion record

## Processing methodology

**Differs from prior batches.** Prior batches (2026-05-10 / -11 / -13-14) used `tools/voice-pipeline-orchestrator.py` Stage 5 LLM rerank
(direct Anthropic API). This batch processed via Claude Code built-in Read/Write tools per memory rule `feedback_no_api_keys`
(Max subscription covers tool usage; direct API calls forbidden).

**Pipeline applied:**
1. Stage 1 — Groq Whisper transcription (authorized — see deep prompt §0 / explicit user ack)
2. Stage 2 — Read all 38 transcripts via Claude Code built-in Read tool
3. Stage 3 — three-way classification per deep prompt §6
4. Stages 4-6 — Write three output streams (this dir + decisions/REFLECTION-INBOX + decisions/SELF-OS-SPEC)
5. Stage 7 — Verification + git commit + push

**Not performed (vs prior batches):**
- No LLM-driven `04-wiki-candidates` rerank into Tier A/B/C with cosine-similarity scores
- No `_filtered-annotated.json` machine-readable sidecar
- No `_stage5_*_rerun.log.md` API trace

For this batch wiki candidates = manually curated list (Markdown table) without similarity-scores.
Bulk-ack via `/wiki-bulk-ack` will need to read MD format directly or generate JSON sidecar at acquisition time.

## Three-output routing logic (per deep prompt §6)

```
For each transcript / item:
  is_reflection = check_personal_emotion_observation_pattern_task_health
  is_self_os = check_thinking_about_system_for_working_with_self
  is_jetix = check_methodology_business_partnership_product_sales

  if is_reflection AND NOT is_self_os AND NOT is_jetix → Reflection-Inbox only
  elif is_self_os → Self-OS-spec (+ Reflection if also personal observation)
  elif is_jetix AND NOT is_reflection → this dir only
  elif dual_relevant → split fragments OR cross-reference in both
```

**Conservative bias.** Когда unsure — duplicate с cross-reference. Loss > duplication.

## Counts breakdown

| Origin batch | → Reflection-Inbox | → Self-OS | → this dir (Jetix) | Dual-routed |
|---|---|---|---|---|
| Common (14 audio) | 5 fragments | 8 fragments | 14 audio | 6 |
| Reflection (24 audio) | 24 audio | 16 fragments | 4 fragments | 8 |
| **Total signals** | ~30 | ~26 | ~18 | ~14 |

## Provenance

- All transcripts: `raw/transcripts/audio_{87-110,655-668}@*.txt`
- Audio archived: `raw/voice-memos/audio_{87-110,655-668}@*.ogg` (also originals in `raw/voice-memos-2026-05-16-{batch,reflection}/`)
- Tier 2 R6: ✓ per-item provenance в каждом output
- Tier 2 R11 Default-Deny: ✓ uncategorized items → kept in transcripts, flagged in §H Open Questions
- Tier 2 R12 Anti-Extraction: ✓ no extrapolation beyond what Ruslan voiced
