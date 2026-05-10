---
title: Server CC Brigadier — Voice Pipeline Improved (2-phase, Plan Mode + Ultrathink)
type: brigadier-prompt
created: 2026-05-10
author: cloud-cowork (Ruslan ack)
target_executor: server-cc on branch claude/jolly-margulis-915d34 (or successor)
authority: Ruslan ack via cloud cowork chat 2026-05-10
phase_1_mode: Plan Mode + Ultrathink (CC plans, await Ruslan ack)
phase_2_mode: Execute approved plan (autonomous brigadier)
push_policy: draft commits на свою ветку, await Ruslan merge ack
F: F4
G: voice-pipeline-deep-redesign
R: refuted_if_outputs_не_actionable_or_wiki_candidates_collide_silently
constitutional_anchor:
  - Tier 2 Rule 1 (no AI strategizing) — voice notes = scribing + structuring, ideas extraction. Ruslan = sole strategist, decides what to use.
  - Tier 2 Rule 2 (no architectural changes без gate) — wiki candidates pending Ruslan ack, не auto-merge в wiki/
  - Tier 2 Rule 6 (provenance) — каждый extracted item cited к source voice memo + timestamp/segment
  - Append-only — existing review_2026-05-01-*.md preserved, новые outputs в новый folder
  - Default-Deny — Phase 1 plan published → Ruslan ack → Phase 2 execution
estimated_effort: Phase 1 = 30-45 min Plan Mode / Phase 2 = 1.5-2.5 hours autonomous
---

# Voice Pipeline Improved — 2-Phase Brigadier

> **Контекст.** 47 новых voice memos (`audio_587-633`, 01-10.05.2026) загружены в `raw/voice-memos/`.
> Текущий pipeline (`tools/run_pipeline.sh`: transcribe → extract → filter → review_report) — work, но
> output (`reports/review_2026-05-01-*.md`) был «каша» — 1 MB raw + 17 KB structured + 6 KB backlog.
> Ruslan хочет deep redesign — multiple targeted deliverables, current-lens filter, wiki candidates.
>
> **Workflow:** Phase 1 ты PLANS (in Plan Mode + Ultrathink), Ruslan acks plan, Phase 2 executes.

---

## §1 PHASE 1 — Plan Mode + Ultrathink (FIRST)

### §1.1 Inputs to study

A.1 **Previous review artifacts** (что было сделано):
   - `reports/review_2026-05-01.md` (1 MB full)
   - `reports/review_2026-05-01-STRUCTURED.md` (17 KB clean)
   - `reports/review_2026-05-01-BACKLOG-FLAG.md` (6 KB)
   - `reports/review_2026-04-26-DEEP.md`
   - `reports/review_2026-04-26.md`
   - `reports/review_2026-04-24.md`
   - `reports/review_2026-04-21.md`

A.2 **Pipeline scripts**:
   - `tools/run_pipeline.sh`
   - `tools/transcribe.py`
   - `tools/extract.py`
   - `tools/filter.py`
   - `tools/review_report.py`
   - `tools/distribute.py.bak` (archived per CLAUDE.md — не auto-runs)

A.3 **Current canonical context** (чтобы знать «через какую призму»):
   - `canonical/INDEX.md` — все active LOCKED docs
   - `decisions/JETIX-CORPORATION-2026-05-05.md` (Document 1B)
   - `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` (Document 1A)
   - `swarm/wiki/synthesis/diagrams-2026-05-07/workshop-deep/v4-system-boundary.md` (current diagram)
   - **Current focus:** видео Цэрэну (см. Daily Log 2026-05-08 Notion subpage `🎬 Tseren Video Recording 2026-05-08`)

A.4 **Wiki structure to consider for candidates**:
   - `wiki/concepts/`, `wiki/ideas/`, `wiki/entities/`, `wiki/topics/`, `wiki/sources/`, `wiki/claims/`, `wiki/foundations/`
   - `wiki/index.md` (catalog)
   - `wiki/log.md` (chronology)
   - `wiki/_templates/`

A.5 **Voice memos to process** (47 files):
   - `raw/voice-memos/audio_587@01-05-2026_*.ogg` ... `audio_633@10-05-2026_*.ogg`

### §1.2 Plan Mode deliverable — `reports/voice-pipeline-2026-05-10/PLAN.md`

Server CC produces **comprehensive pipeline redesign plan** answering:

**P.1 What was wrong / suboptimal в previous pipeline (review_2026-05-01-*)?**
- Какие categories of items были потеряны / mis-classified?
- Где были duplicates / noise / wasted Ruslan attention?
- Какие deliverables Ruslan не использовал → можно убрать?

**P.2 New pipeline stages design:**

Suggest 5-7 stages, для каждой declare:
- Input
- Output
- Quality criterion (как verify что stage достиг цели)
- Tooling (Python? Claude API? grep? template?)
- Estimated time

Examples из требования Ruslan'а:
- Stage 1: Transcribe (existing — keep)
- Stage 2: Extract structured items (extend — категории = idea / task / question / hypothesis / claim / observation / decision / похоже-на-existing-wiki / contradiction)
- Stage 3: Dedup + meta-analysis (existing — improve criteria)
- Stage 4: Per-note deep breakdown (NEW — каждый memo получает свою sub-section в master report с full structured items)
- Stage 5: Wiki candidates extraction (NEW — match items to existing wiki entries или propose new entries; output: `wiki-candidates-2026-05-10.md` со списком)
- Stage 6: Through-current-lens filter (NEW — score каждый item по relevance к текущему focus = видео Цэрэну + immediate Phase 1 priorities; top-N items в `current-lens-actionables-2026-05-10.md`)
- Stage 7: Multi-output report assembly (clean structured / backlog flagged / per-note deep / wiki candidates / current-lens — separate files, не «каша 1 MB»)

**P.3 Output deliverables structure:**

```
reports/voice-pipeline-2026-05-10/
├── PLAN.md                          (this Phase 1 plan output)
├── 00-MASTER-INDEX.md               (navigation)
├── 01-per-note-breakdown.md         (per-memo sub-sections, full structured items)
├── 02-structured-clean.md           (curated items, deduplicated, by category)
├── 03-current-lens-actionables.md   (top-N для immediate use — видео Цэрэну / Phase 1)
├── 04-wiki-candidates.md            (match to existing OR propose new)
├── 05-backlog-flagged.md            (defer items, reasons)
├── 06-meta-analysis.md              (patterns / themes / cross-memo connections)
└── 07-discipline-log.md             (provenance: which item → which memo:line)
```

**P.4 Quality criteria for Phase 2 self-evaluation:**

CC should run criteria check at end of Phase 2:
- All 47 memos processed (transcribe success rate ≥95%)
- Per-note breakdown contains ≥1 structured item per memo (or explicit `nothing-extractable` tag)
- Wiki candidates include match-to-existing for ≥30% items
- Current-lens score is provenance-cited (why this item is now-actionable)
- No silent merges to wiki/ (only candidate proposals, Ruslan acks)
- Append-only: existing review_2026-05-01-* preserved untouched

**P.5 Constitutional check Phase 2 will satisfy:**

- Tier 2 Rule 1: AI extracts + structures, not strategizes which items to act on
- Tier 2 Rule 2: wiki/ writes pending Ruslan ack (each candidate flagged)
- Tier 2 Rule 6: provenance per item (memo:line:timestamp)
- Append-only: новый folder `reports/voice-pipeline-2026-05-10/`, существующие preserved
- Default-Deny: pipeline-plan published → Ruslan acks → Phase 2 fires

**P.6 Open questions for Ruslan to answer before Phase 2:**

Если CC обнаруживает ambiguities (что считать «current lens» / какой threshold для wiki candidate / etc.) — list them в PLAN.md §6 для Ruslan ack.

### §1.3 Phase 1 deliverable & wait

After PLAN.md created and pushed на свою ветку:
- `git commit -m "[voice-pipeline] Phase 1 plan — improved pipeline design awaiting Ruslan ack"`
- `git push origin HEAD` (НЕ main)
- Signal Ruslan через cloud cowork bridge — ready for review
- **WAIT for Ruslan ack** — не начинай Phase 2 без explicit «ack — execute plan»

---

## §2 PHASE 2 — Execute approved plan (after Ruslan ack)

После Ruslan ack of PLAN.md:

### §2.1 Execute the 5-7 stages

For each stage from PLAN.md:
- Run + capture output
- Validate against quality criteria
- Log execution в `07-discipline-log.md`
- If stage fails — pause + signal Ruslan, не auto-retry

### §2.2 Outputs to produce

All files в `reports/voice-pipeline-2026-05-10/` per PLAN.md §P.3 structure.

### §2.3 Self-evaluation

At end:
- Run criteria check (PLAN.md §P.4)
- Output `07-discipline-log.md` с pass/fail verdict per criterion
- If any criterion failed — explicit honest tag

### §2.4 Final push

```bash
git add reports/voice-pipeline-2026-05-10/
git commit -m "[voice-pipeline] Phase 2 execute — 47 memos processed, 7-deliverable structured output (Ruslan ack pending merge)"
git push origin HEAD
```

**НЕ push to main.** **НЕ tag.** Wait Ruslan ack для merge.

---

## §3 What NOT to do

- ❌ НЕ перезаписывать `tools/transcribe.py` / `extract.py` / etc. — current scripts work; новый pipeline = new orchestration over them, не replacement
- ❌ НЕ удалять `reports/review_2026-05-01-*.md` — append-only history
- ❌ НЕ делать silent merges в `wiki/` — только candidate proposals
- ❌ НЕ интерпретировать voice content как «Ruslan меняет strategy» — это scribing extraction, Ruslan читает + decides
- ❌ НЕ запускать Phase 2 без Ruslan ack of Phase 1 plan
- ❌ НЕ push to main, НЕ tag

---

## §4 Time budget

- Phase 1 (Plan Mode + Ultrathink + study previous + design + write PLAN.md): **30-45 min**
- Wait for Ruslan ack: variable (likely <1 hour)
- Phase 2 (execute): **1.5-2.5 hours** depending на complexity (47 memos × 5-7 stages)

Total: **2-3.5 hours** brigadier autonomous.

---

## §5 Constitutional cross-check

| Rule | Application | Compliance |
|---|---|---|
| Tier 2 Rule 1 | Pipeline = scribing + structuring + categorizing. AI не decide strategy. | ✅ |
| Tier 2 Rule 2 | Phase 1 plan → Ruslan ack → Phase 2. Wiki writes = candidates only. | ✅ |
| Tier 2 Rule 6 | Provenance per item (memo:line). Discipline log final. | ✅ |
| Append-only | New folder, old preserved. | ✅ |
| Default-Deny | Phase 1 → ack → Phase 2 → ack → merge. Two gates. | ✅ |

---

## §6 Final signal к Ruslan

After Phase 1 push:
- Branch + commit SHA
- PLAN.md path
- Open questions count (если есть)
- Phase 2 estimated duration

After Phase 2 push:
- Branch + commit SHA
- Files produced (counts + line counts)
- Self-evaluation criteria pass/fail
- Provenance density
- Ready для merge ack

Ruslan acks → push to main + optional tag `voice-pipeline-improved-2026-05-10`.

---

**Brigadier signature.** Acting_as voice-pipeline-redesign-orchestration-role.
Ultrathink + Plan Mode required для Phase 1.
Ruslan = sole strategist (decides what to use, what to wiki-add, what to ignore).
