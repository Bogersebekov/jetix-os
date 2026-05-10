---
title: Voice Pipeline Improved — Phase 1 Plan
type: brigadier-plan
created: 2026-05-10
phase: 1-of-2 (planning)
phase_2_status: awaiting-ack
branch: claude/jolly-margulis-915d34
input_corpus: 47 memos (audio_587@01-05-2026 → audio_633@10-05-2026)
F: F4
G: voice-pipeline-redesign
R: refuted_if_phase_2_outputs_collide_with_canonical_or_silently_merge_to_wiki
constitutional_anchor:
  - Tier 2 Rule 1 (no AI strategizing — extraction only)
  - Tier 2 Rule 2 (no architectural changes без gate — wiki candidates только, не writes)
  - Tier 2 Rule 6 (provenance per item)
  - Append-only (existing review_2026-05-01-* preserved)
  - Default-Deny (two-gate: Phase 1 ack → Phase 2 → ack → optional merge)
source_brief: prompts/server-cc-voice-pipeline-improved-2026-05-10.md
---

# Voice Pipeline Improved — Phase 1 Plan

> **Status.** Phase 1 design complete. Awaiting Ruslan ack on this PLAN.md → fires Phase 2.
>
> **Source brief.** `prompts/server-cc-voice-pipeline-improved-2026-05-10.md` (2-phase brigadier).
>
> **Branch.** `claude/jolly-margulis-915d34` (NOT main, NOT tagged).
>
> **Constitutional posture.** Two-gate workflow per Default-Deny: (1) ack PLAN.md → write Phase 2 deliverables; (2) ack Phase 2 deliverables → optional merge to main + optional wiki/ candidate promotions. Wiki writes are NEVER auto — proposals only.

---

## §0 Context

**Problem.** 47 new voice memos (`audio_587-633`, 01-10.05.2026) sit in `raw/voice-memos/`. Existing pipeline (`tools/run_pipeline.sh`: transcribe → extract → filter → review_report) executes mechanically but produced unusable output last cycle: `reports/review_2026-05-01.md` = 1 MB raw + 17 KB structured + 6 KB backlog = "каша". Items duplicated 5-10× (cross-memo dedup never ran — filter.py hit API cap at batch 13/17), provenance opaque (citations exist but unmappable to transcript line/timestamp), categories incomplete (Decisions/Questions/Claims missing as separate views), per-memo grouping abandoned (3,109 rows flattened), no consensus/frequency signal, auto-CRM artefacts pollute output, DEEP variant works for 10 memos but breaks at 197.

**Goal.** A 7-stage orchestration over the existing scripts (NOT replacing them — current scripts are idempotent and work) that produces a multi-deliverable structured output: separate files for clean structured / per-note breakdown / current-lens actionables / wiki candidates / backlog / meta-analysis / discipline-log. Each item cited to source memo:line. Wiki candidates flagged, never silently merged.

**Outcome of Phase 2 (after ack).** 8-file deliverable bundle in `reports/voice-pipeline-2026-05-10/`, ≤500 KB total, every memo accounted for, full provenance, current-lens-scored top-N, wiki candidate list pending separate Ruslan ack.

---

## §1 P.1 — What was wrong / suboptimal в `review_2026-05-01-*`

Seven concrete weaknesses, traced to specific stages of the previous run:

### W.1 No cross-memo deduplication

Items #1, #11, #134 in the 1 MB report = identical text "Описать целевых людей… audio_393@09-04-2026_04-00-41" — same source memo, same content, repeated 3× in a 200-row section. Pattern continues across 3,109 rows: ≈100+ identical items.

**Root cause.** `filter.py` Stage 3 was supposed to dedup. It batches at THRESHOLD=100, BATCH_SIZE=50. On the 197-memo run it hit a rate-limit cap at batch 13/17 — partial-save survived but final merge never executed, so what shipped to `review_report.py` was the raw extract output dressed as "filtered". Mitigation: Stage 3 in new pipeline.

### W.2 Opaque provenance

Citations like `audio_393@09-04-2026_04-00-41` exist but can't be navigated. No transcript line reference, no audio timestamp, no clickable path. STRUCTURED variant (17 KB) added line refs (`raw/transcripts/audio_582@30-04-2026_18-12-09.txt:L6`) for 5 themes only. DEEP added audio timestamps (`audio_582 18:12-18:47`) for 10 memos only — neither scaled. Mitigation: Stage 4 + Stage 7 + open question §6.5.

### W.3 Incomplete category capture

Schema in `extract.py` covers 12 categories (Видение / Решения / Инсайты / Стратегические гипотезы / Задачи / Идеи для проектов / Идеи / Открытые вопросы / Контакты / Ресурсы / Личные наблюдения / Принципы). Brief asked for: idea / task / question / hypothesis / claim / observation / decision. Coverage is mostly OK but: **Решения** never gets its own top-level view in `review_report.py` (buried in row #161 of a 200-item table); **claim** doesn't exist as separate category (folded into Инсайты); **contradiction** is only surfaced in filter.py meta_analysis aggregate, not per-item. Mitigation: Stage 4 explicit category-level views + Stage 7 multi-output split.

### W.4 Per-memo structure abandoned

`review_2026-05-01.md` (1 MB) flattens 3,109 rows across 197 memos into one giant table. Discovery is grep-only. `review_2026-04-26-DEEP.md` did per-memo § (audio_530, 531, …) — readable but ten times the size if scaled to 197 memos. Mitigation: Stage 4 hierarchical (per-memo section with summarized items + at-most-one verbatim quote per memo).

### W.5 No frequency / consensus signal

If "Описать целевых людей" appears across 8 memos in 5 days, that's a strong signal. Current pipeline treats each occurrence as an isolated row. STRUCTURED variant compressed 47 items → 5 themes (10:1) but lost the per-memo backing. Mitigation: Stage 3 post-process annotates `appeared_in_memos: [list]` per item; Stage 6 uses frequency as a scoring component.

### W.6 CRM auto-drafts pollute output

`extract.py` Stage 2b heuristic creates `crm/people/<slug>-DRAFT.md` (status=`draft_from_voice`) for any name in voice memo. Both STRUCTURED and BACKLOG-FLAG referenced "Ilon Mask draft" + "Dima draft" — auto-generated noise mixed with real content review. Mitigation: Stage 7 segregates into `05-backlog-flagged.md` under explicit "CRM Drafts" header — NEVER auto-promote.

### W.7 DEEP format scale-break

`review_2026-04-26-DEEP.md` (112 KB for 10 memos) showed the right structure: per-memo § + Theme numbering + verbatim quotes + cross-references. Linear scale to 197 memos = ~2 MB — unreadable. Mitigation: hierarchical pattern — Stage 4 per-memo summaries (cap ~80 KB for 47 memos); Stage 6 top-N ≤20 actionables; full transcripts available on-demand via the existing `raw/transcripts/<stem>.txt` path.

---

## §2 P.2 — New pipeline 7 stages

Each stage wraps existing scripts (per brief §3 "НЕ перезаписывать"). All LLM calls via `tools/lib/cc_helper.py` → `claude -p` headless (Max sub, no API key — aligns with `feedback_no_api_keys.md`).

### Stage 1 — Transcribe (existing — wrap)

| Field | Value |
|---|---|
| **Input** | 47 ogg in `raw/voice-memos/` (already moved by prior partial run); pre-flight: ensure `raw/transcripts/<stem>.txt` exists for each, else copy back to `inbox/voice/` and run `transcribe.py` |
| **Output** | 47 transcripts in `raw/transcripts/` |
| **Quality criterion** | ≥95% transcribe rate; total minutes captured; lang=ru |
| **Tooling** | `tools/transcribe.py` (existing, idempotent — skips if `.txt` exists) + thin Bash pre-flight wrapper |
| **Estimated time** | 10-25 min (depends on memo length; idempotent skip if cached) |

### Stage 2 — Extract (existing — wrap, validate schema)

| Field | Value |
|---|---|
| **Input** | 47 transcripts |
| **Output** | 47 extraction JSONs in `inbox/processed/extractions/` (12-cat schema + optional `crm_items`) |
| **Quality criterion** | every memo gets ≥1 item OR explicit `nothing-extractable` marker; 12-cat schema honored |
| **Tooling** | `tools/extract.py` (existing) + post-process Python validator that flags empty extractions and inserts `nothing-extractable` marker in a separate companion file |
| **Estimated time** | 15-35 min (Sonnet 4.6 via cc_helper) |

### Stage 3 — Cross-memo dedup + frequency annotation (existing filter.py — IMPROVE wrapping)

| Field | Value |
|---|---|
| **Input** | 47 extraction JSONs (≈300-1500 items est.) |
| **Output** | `inbox/processed/filtered/batch_2026-05-10.json` with new `appeared_in_memos: [list]` field per item; dedup ratio recorded in companion `discipline-log` line |
| **Quality criterion** | dedup ratio ≥30% (target — items reduce by ≥30% from raw); each item has frequency count; partial-save resumes if interrupted |
| **Tooling** | `tools/filter.py` (existing, Opus 4.7 batched) + post-process Python that walks `groups_by_project` and `sources` fields and annotates frequency |
| **Estimated time** | 15-25 min (default resume mode; `--restart` if Ruslan asks) |

### Stage 4 — Per-note deep breakdown (NEW)

| Field | Value |
|---|---|
| **Input** | 47 extractions + filtered batch |
| **Output** | `01-per-note-breakdown.md` — one §-section per memo with: timestamp, length (mm:ss), top-3 items as summaries, categories tagged, link to `raw/transcripts/<stem>.txt:L#` for each item, optional 1 verbatim quote per memo if memo length >5 min |
| **Quality criterion** | every memo §-section present; ≥1 item or `nothing-extractable` tag; transcript line refs cited; size cap ~80 KB |
| **Tooling** | Python orchestrator + Claude Sonnet 4.6 via cc_helper.py (one batched call per ~5 memos summarizing per-memo block) |
| **Estimated time** | 20-35 min |

### Stage 5 — Wiki candidates extraction (NEW)

| Field | Value |
|---|---|
| **Input** | filtered items |
| **Output** | `04-wiki-candidates.md` — for each candidate-worthy item: `match-to-existing` (with wiki page path + match-score) OR `propose-new` (with proposed slug + entity type from 9 wiki types: concepts/entities/sources/topics/ideas/experiments/claims/summaries/foundations) |
| **Quality criterion** | ≥30% items get a `match-to-existing` decision (not invented matches); each candidate cited to memo:line; **NEVER auto-write to `wiki/`** — proposals only; size cap ~25 KB |
| **Tooling** | Python + Claude Sonnet via cc_helper; uses `grep wiki/index.md` snapshot + `wiki/_templates/` schema to constrain propositions; match-score from Claude Sonnet rating (proxy for cosine) |
| **Estimated time** | 20-35 min |

### Stage 6 — Through-current-lens filter (NEW)

| Field | Value |
|---|---|
| **Input** | filtered items |
| **Output** | `03-current-lens-actionables.md` — top-N=20 items scored via 4-component formula |
| **Scoring** | `relevance_score = 0.40 × keyword_match + 0.35 × semantic_distance + 0.15 × workshop_element_weight + 0.10 × recency_vs_canonical`; threshold ≥0.60 |
| **Lens anchors** | Tseren / Цэрэн / видео Цэрэну / synergy / ШСМ / Levenchuk / $100K / Phase 1 / Workshop / TRM / Foundation v1.0 / Document 1A / Document 1B / 8-step roadmap / L0-L5 ladder / Mittelstand / Reed's Law (Tier 1 — high relevance); methodologies / AI leverage / knowledge management / client engagement / partner role structuring (Tier 2 — medium); long-term vision / anti-pattern discussions / personal development (Tier 3 — low) |
| **Quality criterion** | every top-N item has provenance + score breakdown + why-relevant rationale (1 sentence); items linked to specific roadmap step (1-8); size cap ~15 KB |
| **Tooling** | Python keyword scorer (Tier 1/2/3 keyword lists) + Claude Sonnet pass for semantic distance + roadmap step linkage |
| **Estimated time** | 15-25 min |

### Stage 7 — Multi-output report assembly (NEW)

| Field | Value |
|---|---|
| **Input** | all stage outputs |
| **Output** | 8 files in `reports/voice-pipeline-2026-05-10/` per §3 below |
| **Quality criterion** | all 8 files present; navigation INDEX traverses all; no single file >150 KB; total folder <500 KB; `07-discipline-log.md` captures pass/fail per stage with honest tags |
| **Tooling** | Python orchestrator (single script, deterministic) |
| **Estimated time** | 10-15 min |

**Total Phase 2 time estimate.** 1.75-3 hours (matches brief §4 budget 1.5-2.5h with upper-edge contingency for first-run inefficiency on Stage 4-6).

---

## §3 P.3 — Output deliverables structure

```
reports/voice-pipeline-2026-05-10/
├── PLAN.md                          (this Phase 1 plan)
├── 00-MASTER-INDEX.md               (navigation; one paragraph per file with line counts + size + brief description)
├── 01-per-note-breakdown.md         (47 memo sections; size cap ~80 KB)
├── 02-structured-clean.md           (deduplicated items by category; 12-cat groupings; size cap ~30 KB)
├── 03-current-lens-actionables.md   (top-N=20 default; Stage 6 output; size cap ~15 KB)
├── 04-wiki-candidates.md            (match-to-existing OR propose-new; Stage 5 output; size cap ~25 KB)
├── 05-backlog-flagged.md            (deferred items + reason; CRM drafts segregated; size cap ~10 KB)
├── 06-meta-analysis.md              (themes / contradictions / patterns from filter.py meta + cross-memo synthesis; size cap ~15 KB)
└── 07-discipline-log.md             (per-stage pass/fail verdict; provenance density; quality criteria check; size cap ~20 KB)
```

**Total deliverable folder.** ≤500 KB — vs. 1 MB caша. Each file scoped + navigable.

---

## §4 P.4 — Quality criteria for Phase 2 self-evaluation

End-of-Phase-2 self-eval, written into `07-discipline-log.md`:

1. All 47 memos processed; transcribe ≥95% success rate
2. Every memo has §-section in `01-per-note-breakdown.md` with ≥1 item or `nothing-extractable` tag
3. `04-wiki-candidates.md`: ≥30% match-to-existing rate (suggesting candidate corpus diversity, not invention)
4. `03-current-lens-actionables.md`: each top-N item has provenance + scoring breakdown + roadmap-step linkage
5. No silent merges to `wiki/` — only candidate proposals (verify: `git diff --stat origin/main` shows zero `wiki/` changes)
6. Append-only: `reports/review_2026-05-01-*.md`, `2026-04-26-*.md`, `2026-04-24.md`, `2026-04-21.md` preserved untouched (verify: `git log --follow` shows no modifications)
7. `07-discipline-log.md` shows pass/fail per criterion above; honest tags on failures (no glossing — if Stage X failed at criterion Y, log explicit `FAIL: <reason>` not silent omission)
8. No file >150 KB; total deliverable folder <500 KB

---

## §5 P.5 — Constitutional cross-check

| Anchor | Application | Compliance plan |
|---|---|---|
| **Tier 2 R1** (no AI strategizing) | AI extracts + structures + categorizes. AI does NOT decide which items become decisions or shift roadmap. | ✅ Phase 2 outputs are scribing artifacts. Ruslan reads `03-current-lens-actionables.md` + decides. |
| **Tier 2 R2** (no architectural changes без gate) | Phase 1 plan → ack → Phase 2 → ack → merge. | ✅ Two-gate. Wiki candidates ≠ wiki writes; `wiki/` untouched in Phase 2. |
| **Tier 2 R6** (no unstructured long-term memory aggregation) | All extracted items provenance-cited (memo:line). | ✅ `07-discipline-log.md` final, `01-per-note-breakdown.md` per-memo cites. |
| **Append-only** | New folder; old reports preserved. | ✅ `reports/voice-pipeline-2026-05-10/` is new; existing `review_*` files untouched. |
| **Default-Deny** | Two-gate; wiki writes deferred to a third Ruslan ack after Phase 2 review. | ✅ Phase 1 ack → Phase 2 → ack → optional merge to main → optional separate ack for wiki/ candidate promotions. |
| **No API keys** (per `feedback_no_api_keys.md`) | All LLM calls via `cc_helper.py` → `claude -p` headless (Max sub). | ✅ No `ANTHROPIC_API_KEY` / `GROQ_API_KEY` env vars touched (Groq stays in `transcribe.py` existing script — already Ruslan-approved). |

---

## §6 P.6 — Open questions for Ruslan

The following are flagged for ack before Phase 2 fires. Defaults shown — Ruslan can override individual items in ack message, or just say "all defaults".

### §6.1 Top-N for `03-current-lens-actionables.md`?

- **Default.** N=20.
- **Alternatives.** 10 (tighter focus), 50 (broader scan).
- **Trade.** 20 fits ~15 KB cap; 50 risks redundancy with `02-structured-clean.md`.

### §6.2 Wiki match-to-existing confidence threshold?

- **Default.** ≥0.7 cosine-style match (Claude Sonnet rating proxy); below = `propose-new`.
- **Alternatives.** ≥0.5 (more matches, more false positives) | ≥0.85 (fewer matches, near-only true matches).
- **Trade.** Lower threshold = more `match-to-existing` (good for ≥30% target) but higher noise.

### §6.3 Frequency threshold for "consensus theme" in `06-meta-analysis.md`?

- **Default.** ≥3 memos.
- **Alternatives.** ≥2 (more themes, more noise) | ≥5 (only strong consensus).
- **Trade.** With 47 memos and 5-10 days range, ≥3 captures persistent thinking; ≥5 may be too restrictive.

### §6.4 Stage 4 verbatim quotes vs summaries-only?

- **Default.** Top-3 items per memo as summaries + 1 verbatim quote per memo if memo length >5 min.
- **Alternatives.** Summaries-only (smaller file) | full DEEP-style with all quotes (larger file, ~150 KB risk).
- **Trade.** Default keeps `01-per-note-breakdown.md` ≤80 KB while preserving navigability via quote anchor.

### §6.5 Audio timestamp provenance (e.g. `audio_582 18:12-18:47`)?

- **Default.** NO for Phase 2.
- **Reason.** `transcribe.py` doesn't currently store Whisper segment data; adding it = modifying transcribe.py = out of scope per brief §3 "НЕ перезаписывать". Could add as Phase 3 extension.
- **Alternative.** Inclusion would require `transcribe.py` modification — flag for separate Ruslan decision.

### §6.6 CRM auto-drafts (`draft_from_voice` stubs from extract.py Stage 2b)?

- **Default.** List in `05-backlog-flagged.md` under explicit header "CRM Drafts (auto-generated, awaiting promotion)" — DO NOT auto-promote.
- **Alternative.** Sweep + delete drafts not referenced by other items (more aggressive cleanup).
- **Trade.** Default is conservative; aggressive cleanup is risky if Ruslan wanted to keep some drafts.

### §6.7 Idempotency on partial Phase 2 run

- **Default.** Resume — leverage existing `filter.py` partial-save in `.partials/`.
- **Alternative.** `--restart` flag for clean run if Ruslan suspects prior partial state corrupt.
- **Trade.** Resume saves time; restart is safer if state uncertain.

---

## §7 Phase 2 execution flow (after ack)

For reference — exact ops Phase 2 will perform:

1. Run Stage 1 (transcribe wrapper) → log to `07-discipline-log.md`
2. Run Stage 2 (extract + validate) → log
3. Run Stage 3 (filter + frequency annotation) → log
4. Run Stage 4 (per-note breakdown) → write `01-per-note-breakdown.md`
5. Run Stage 5 (wiki candidates) → write `04-wiki-candidates.md`
6. Run Stage 6 (current-lens filter) → write `03-current-lens-actionables.md`
7. Run Stage 7 (assembly + INDEX + structured-clean + backlog + meta-analysis) → write `00`, `02`, `05`, `06`
8. Self-eval against §4 criteria → write final `07-discipline-log.md` verdict block
9. `git add reports/voice-pipeline-2026-05-10/` (excluding PLAN.md already committed)
10. `git commit -m "[voice-pipeline] Phase 2 execute — 47 memos processed, 7-deliverable structured output (Ruslan ack pending merge)"`
11. `git push origin claude/jolly-margulis-915d34`
12. **Signal Ruslan** with branch + commit SHA + file inventory + line counts + self-eval pass/fail + provenance density. **STOP.** Do NOT push to main, do NOT tag, do NOT promote wiki candidates.

---

## §8 Critical files referenced

### Wrap, do NOT edit
- `tools/run_pipeline.sh` — orchestration script
- `tools/transcribe.py:21-104` — Groq Whisper, idempotent
- `tools/extract.py:53-110` (12-cat system prompt), `:127-149` (output JSON shape), `:195-246` (CRM aggregation)
- `tools/filter.py:38` (THRESHOLD=100), `:37` (BATCH_SIZE=50), `:115-159` (partial-save), `:308-326` (output schema)
- `tools/review_report.py:51` (input filtered batch), `:86-142` (7 sections), `:144-146` (output path + symlink)
- `tools/lib/cc_helper.py:89-126` — Max-sub headless dispatch (no API key)
- `config/context.md` — preloaded by extract + filter (project names guard)

### Read for context (Stage 5 + Stage 6)
- `wiki/index.md` + `wiki/_templates/` — Stage 5 wiki candidate matching
- `decisions/JETIX-CORPORATION-2026-05-05.md` (Doc 1B) — Stage 6 lens anchor
- `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` (Doc 1A) — Stage 6 lens anchor
- `swarm/wiki/synthesis/diagrams-2026-05-07/workshop-deep/v4-system-boundary.md` — Stage 6 boundary anchor

### Files NOT to touch (Phase 1 + Phase 2)
- `tools/transcribe.py` / `extract.py` / `filter.py` / `review_report.py` — wrap, don't edit (per brief §3)
- `reports/review_2026-05-01-*.md` / `2026-04-26-*.md` / `2026-04-24.md` / `2026-04-21.md` — append-only history
- `wiki/**` — Phase 2 produces candidates only; merges = third Ruslan ack
- `main` branch — push to `claude/jolly-margulis-915d34` only
- Any LOCKED canonical doc (Foundation Parts 1-11, Pillar C, Document 1A/1B, etc.)

---

## §9 Verification (how to test Phase 2 success)

Post-Phase-2 commands Ruslan can run to verify:

```bash
# 1. All 8 files present + size cap
wc -l reports/voice-pipeline-2026-05-10/*.md
du -h reports/voice-pipeline-2026-05-10/

# 2. 47 memo sections in per-note breakdown
grep -c '^## audio_' reports/voice-pipeline-2026-05-10/01-per-note-breakdown.md
# expect 47

# 3. nothing-extractable count (some memos may be empty)
grep -c 'nothing-extractable' reports/voice-pipeline-2026-05-10/01-per-note-breakdown.md

# 4. wiki match-vs-propose ratio
grep -c 'match-to-existing' reports/voice-pipeline-2026-05-10/04-wiki-candidates.md
grep -c 'propose-new' reports/voice-pipeline-2026-05-10/04-wiki-candidates.md
# expect match ≥30% of total

# 5. current-lens top-N ≤20
grep -c '^## ' reports/voice-pipeline-2026-05-10/03-current-lens-actionables.md
# expect ≤20 with score breakdown each

# 6. discipline-log verdict
cat reports/voice-pipeline-2026-05-10/07-discipline-log.md | head -50
# expect 8-line verdict block per quality criterion

# 7. no wiki/ writes, no main push
git diff --stat origin/main -- 'wiki/**'
# expect empty

# 8. last 2 commits
git log --oneline -2
# expect [voice-pipeline] Phase 2 execute … and [voice-pipeline] Phase 1 plan …
```

---

## §10 What this plan does NOT do

- Phase 2 execution itself (deferred until ack of this PLAN.md)
- Modifications to `transcribe.py / extract.py / filter.py / review_report.py`
- Auto-merge of wiki candidates into `wiki/`
- Any push to `main` or tag creation
- Audio timestamp provenance (Whisper segments) — Phase 3 extension only
- Per-memo full-verbatim transcripts in `01-per-note-breakdown.md` (DEEP-style at 47-memo scale risks 150 KB cap; default = top-3 summaries + 1 quote if memo >5 min)
- Resurrection of `distribute.py.bak` — stays archived per CLAUDE.md voice-pipeline DRAFT-only RUSLAN-LAYER override
- Promotion of any `crm/people/<slug>-DRAFT.md` — segregated in `05-backlog-flagged.md` only

---

## §11 Awaiting Ruslan ack

- **Ack format.** "ack — execute plan" + (optional) per-question overrides for §6.1-§6.7, or "all defaults"
- **Channel.** Cloud cowork bridge (this chat)
- **Then.** Phase 2 fires autonomously. Final signal post-Phase 2 with branch + SHA + file inventory + self-eval verdict + ready-for-merge.
- **No ack = no Phase 2.** Halt-Log-Alert if any agent attempts.

**Brigadier signature.** Acting_as `voice-pipeline-redesign-orchestration-role`. F4 / G voice-pipeline-redesign / R refuted_if_phase_2_outputs_collide_with_canonical_or_silently_merge_to_wiki.
