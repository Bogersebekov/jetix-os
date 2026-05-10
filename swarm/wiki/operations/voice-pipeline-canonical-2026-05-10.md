---
title: Voice Pipeline Canonical — Reusable workflow для обработки voice memos
date: 2026-05-10
type: operational-canon
status: living
purpose: операционный canon для regular voice notes processing — НЕ одноразовый script, а **reusable pipeline** с параметризованной "lens"
parent_plan: reports/voice-pipeline-2026-05-10/PLAN.md
parent_explained: reports/voice-pipeline-2026-05-10/EXPLAINED-FOR-RUSLAN.md
applies_to:
  - All future voice notes batches (любые .ogg/.mp3 в raw/voice-memos/)
  - Any focus / lens / objective (не only Tseren video)
versioning:
  current: v1.0
  changelog:
    - 2026-05-10 v1.0 — initial canonical (extracted from voice-pipeline-2026-05-10/PLAN.md)
F: F4
G: tooling-canonical-pipeline
R: refuted_if_lens_hardcoded_or_pipeline_collapses_per_use_case
---

# 🎬 Voice Pipeline Canonical — Reusable Workflow

> **Что это.** Operational canon для обработки voice memos. **Reusable** — каждый запуск использует свой "lens" (фокус / фильтр) для current-context priorities. Pipeline сам не меняется, **меняется только lens config** на каждый run.

---

## §1 Главный принцип

**Pipeline = stable.** **Lens = configurable.**

Каждый раз когда у тебя накопились voice memos:
1. Загружаешь `.ogg` в `raw/voice-memos/`
2. **Создаёшь lens config** под текущий фокус (что важно сейчас — Цэрэн / Mittelstand outreach / Phase 2 planning / health system / etc.)
3. Запускаешь pipeline → 8 deliverable файлов в `reports/voice-pipeline-YYYY-MM-DD/`
4. Читаешь `03-current-lens-actionables.md` (top-N items relevant to lens) + `04-wiki-candidates.md`
5. Acks → проводишь принятие решений / wiki updates / actions

**Pipeline НЕ переделывается.** Только меняешь `lens_config.yaml`.

---

## §2 7 stages pipeline (общая структура)

| # | Stage | Что делает | Состояние |
|---|---|---|---|
| 1 | Transcribe | OGG → TXT (Groq Whisper) | Existing: `tools/transcribe.py` |
| 2 | Extract | TXT → 12-cat structured items JSON (Claude Sonnet) | Existing: `tools/extract.py` + validator |
| 3 | Filter + Frequency | Cross-memo dedup + frequency annotation | Existing: `tools/filter.py` (improved) |
| 4 | Per-note breakdown | Каждый memo → §-section с top-3 + line refs | NEW |
| 5 | Wiki candidates | Match-to-existing OR propose-new (НЕ auto-merge) | NEW |
| 6 | **Current-lens filter** ⭐ | **Top-N scored через lens config** | NEW (configurable) |
| 7 | Multi-output assembly | 8 файлов output | NEW |

**Stages 1-5, 7 — universal.** Изменяется только Stage 6 через lens config.

---

## §3 8 Deliverables (universal structure)

```
reports/voice-pipeline-YYYY-MM-DD/
├── PLAN.md                          (для каждого run — Phase 1 plan если ultrathink mode)
├── 00-MASTER-INDEX.md               (navigation)
├── 01-per-note-breakdown.md         (каждый memo top-3 + line refs)
├── 02-structured-clean.md           (deduplicated by 12-cat)
├── 03-current-lens-actionables.md   ⭐ (top-N через lens — main output)
├── 04-wiki-candidates.md            (match/propose, НЕ auto-merge)
├── 05-backlog-flagged.md            (deferred + CRM drafts)
├── 06-meta-analysis.md              (themes / patterns / contradictions)
└── 07-discipline-log.md             (provenance + quality criteria pass/fail)
```

---

## §4 LENS CONFIG — главный rebuilable component ⭐

### §4.1 Что такое lens

**Lens = "через какую призму смотреть на накопленные voice items".**

Lens определяет:
- **Tier 1 keywords** (high relevance — главный фокус)
- **Tier 2 keywords** (medium relevance — secondary)
- **Tier 3 keywords** (low relevance — background)
- **Scoring weights** (формула relevance)
- **Threshold** (минимальный score для inclusion)
- **Top-N** (сколько items в final actionables)

### §4.2 Scoring formula (default — можно override в config)

```
relevance_score = w1 × keyword_match
                + w2 × semantic_distance
                + w3 × domain_element_weight
                + w4 × recency_vs_canonical
```

Default weights:
- `w1 = 0.40` (keyword)
- `w2 = 0.35` (semantic)
- `w3 = 0.15` (domain element — например Workshop element)
- `w4 = 0.10` (recency)

Default threshold: `≥0.60`
Default top-N: `20`

### §4.3 Lens config template

```yaml
# config/voice-pipeline-lens-template.yaml
lens_name: "<descriptive name e.g. 'tseren-video-2026-05-10' or 'phase-2-planning' or 'health-q3'>"
lens_purpose: "<one-line — что хочешь вытянуть из voice notes>"
created: <YYYY-MM-DD>
canonical_anchors:  # Optional — pointers на canonical docs которые задают frame
  - <path-to-doc-1>
  - <path-to-doc-2>

# 3-tier keyword anchors (high/medium/low relevance)
tier_1_keywords:  # main focus — items containing эти получают highest score
  - <keyword>
  - <keyword>
tier_2_keywords:  # secondary
  - <keyword>
tier_3_keywords:  # background
  - <keyword>

# Scoring config (default values shown — override if needed)
scoring_weights:
  keyword: 0.40
  semantic: 0.35
  domain_element: 0.15
  recency: 0.10

threshold: 0.60
top_n: 20

# Optional — domain element weights (если есть особый weight для Workshop/TRM elements)
domain_element_weights:
  workshop_master: 1.0
  workshop_storage: 0.8
  workshop_other: 0.6
  trm_resource: 0.9
  none: 0.5

# Output spec
output_path: reports/voice-pipeline-<YYYY-MM-DD>/03-current-lens-actionables.md
```

### §4.4 Example lens — Tseren Video 2026-05-10

```yaml
lens_name: "tseren-video-2026-05-10"
lens_purpose: "Top-N items для записи видео proposal Цэрэну + Phase 1 priorities"
created: 2026-05-10
canonical_anchors:
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md
  - swarm/wiki/synthesis/diagrams-2026-05-07/workshop-deep/v4-system-boundary.md

tier_1_keywords:
  - Tseren
  - Цэрэн
  - видео Цэрэну
  - synergy
  - ШСМ
  - Levenchuk
  - Левенчук
  - $100K
  - Phase 1
  - Workshop
  - TRM
  - Foundation v1.0
  - Document 1A
  - Document 1B
  - 8-step roadmap
  - L0-L5 ladder
  - Mittelstand
  - Reed's Law

tier_2_keywords:
  - methodology
  - AI leverage
  - knowledge management
  - client engagement
  - partner role
  - structuring
  - audience
  - founder

tier_3_keywords:
  - long-term vision
  - anti-pattern
  - personal development
  - hypothesis

scoring_weights:
  keyword: 0.40
  semantic: 0.35
  domain_element: 0.15
  recency: 0.10

threshold: 0.60
top_n: 20

output_path: reports/voice-pipeline-2026-05-10/03-current-lens-actionables.md
```

### §4.5 Future lens examples

Каждый раз когда фокус меняется — копируешь template, заполняешь, run pipeline.

**Phase 2 planning lens (hypothetical):**
```yaml
lens_name: "phase-2-planning-2026-XX"
lens_purpose: "Items для preparation Phase 2 — first 5 clients onboarding"
tier_1_keywords:
  - first client
  - onboarding
  - L0 diagnostic
  - €3K offer
  - 5 first partners
  - retainer
  ...
```

**Health system lens:**
```yaml
lens_name: "health-system-q3"
lens_purpose: "Items для health pipeline (Toggl + sleep + spirit)"
tier_1_keywords:
  - sleep quality
  - energy patterns
  - спорт
  - recovery
  ...
```

**Anything else — same pattern.** Pipeline reusable forever.

---

## §5 How to run pipeline (canonical commands)

### §5.1 First time setup

```bash
# Create lens config (one-time per run)
cp config/voice-pipeline-lens-template.yaml config/voice-pipeline-lens-<YYYY-MM-DD>-<focus>.yaml
# Edit config — fill anchors / keywords / threshold

# Upload memos (если ещё не uploaded)
scp local-folder/*.ogg ruslan@server:/home/ruslan/jetix-os/raw/voice-memos/
```

### §5.2 Run

```bash
# В Claude Code (server CC) запустить через 2-phase brigadier:
# Phase 1 (Plan Mode + Ultrathink) → CC produces PLAN.md adapted под текущую lens
# Phase 2 (after Ruslan ack) → execute pipeline

# Manual run (если skipping Plan Mode):
cd ~/jetix-os
python3 tools/voice-pipeline-orchestrator.py --lens config/voice-pipeline-lens-<date>-<focus>.yaml --output reports/voice-pipeline-<date>/

# (orchestrator.py - to be created during Phase 2 execution)
```

### §5.3 Read output

Order:
1. `00-MASTER-INDEX.md` — navigation
2. `03-current-lens-actionables.md` ⭐ — top-N для immediate work
3. `04-wiki-candidates.md` — wiki updates (твой ack отдельно)
4. `06-meta-analysis.md` — patterns / themes
5. (Optional) `01-per-note-breakdown.md` — deep dive per memo
6. (Optional) `05-backlog-flagged.md` — deferred items

---

## §6 Constitutional invariants (любой run)

| Anchor | Application |
|---|---|
| Tier 2 R1 (no AI strategizing) | Pipeline = scribing + structuring + filtering. Ruslan = sole strategist (decides actions) |
| Tier 2 R2 (no architectural changes без gate) | Two-gate: Phase 1 ack → Phase 2 → ack → optional merge / wiki promotions |
| Tier 2 R6 (provenance) | Каждый item cited к memo:line. discipline-log final |
| Append-only | Existing review_*.md preserved untouched. New folder per run |
| Default-Deny | Wiki writes = third ack отдельно. Auto-merge wiki — НИКОГДА |

---

## §7 Lens design tips

### What makes good lens

- **Specific** — not "general business" but "first-5-Mittelstand-clients-onboarding-q2"
- **Tier 1 keywords concrete** — names / paths / specific terms (not "growth")
- **Anchor canonical docs** — даёт CC frame для semantic distance
- **Threshold balanced** — слишком низкий = noise, слишком высокий = miss items

### When to override defaults

- **Lower threshold** (0.5) — если хочешь broader scan для new domain
- **Higher top-N** (50) — если знаешь что много накопилось
- **Different weights** — if recency более important чем keywords (e.g., for Phase 1 daily standups)

### Reusability check

Каждый раз перед run — задай себе вопрос:
- Что **именно** хочу вытянуть?
- Какие 5-15 keywords дадут мне те items?
- Какой threshold отсечёт noise?

Если ответ ясен → lens готов. Если нет → потрать 5 min на definition.

---

## §8 Versioning lens configs

Каждый lens config храни **навсегда** — это исторический snapshot priorities на тот момент. Format:

```
config/voice-pipeline-lens-<YYYY-MM-DD>-<focus>.yaml
```

Examples (после нескольких runs):
- `config/voice-pipeline-lens-2026-05-10-tseren.yaml`
- `config/voice-pipeline-lens-2026-05-25-phase-2-planning.yaml`
- `config/voice-pipeline-lens-2026-06-15-health-q3.yaml`

Ruslan может ПОЗЖЕ replicate run с тем же lens (e.g., "что я думал про Цэрэн в мае?" — re-run на 2026-05-10 lens config с current-day batch memos).

---

## §9 Sources / changelog

- **2026-05-10 v1.0** — initial canonical extracted from `reports/voice-pipeline-2026-05-10/PLAN.md` Stage 6 design + Ruslan ack 2026-05-10 (cloud cowork chat) для generalize-not-one-shot
- *(future entries)*

## §10 Related

- `reports/voice-pipeline-2026-05-10/PLAN.md` — first instantiation (Tseren lens) — historical record
- `reports/voice-pipeline-2026-05-10/EXPLAINED-FOR-RUSLAN.md` — companion на человеческом
- `tools/transcribe.py` / `extract.py` / `filter.py` / `review_report.py` — wrapped (НЕ редактировать)
- `tools/voice-pipeline-orchestrator.py` (TBD — created during Phase 2)
- `config/voice-pipeline-lens-template.yaml` (TBD — created during Phase 2)
- `config/voice-pipeline-lens-2026-05-10-tseren.yaml` (TBD — created during Phase 2)
- `wiki/_templates/` — wiki schemas для Stage 5 candidate matching
