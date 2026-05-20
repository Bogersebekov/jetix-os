---
title: 🔬 Hypothesis-Tables Architecture Decision — 5 Options Deep Analysis (A-3)
date: 2026-05-20 evening
type: strategic-decision-substrate
parent: daily-logs/_EXECUTION-PLAN-FINAL-2026-05-20-evening.md (A-3)
trigger: Ruslan voice audio_704 — «hypothesis-tables в Jetix substrate»
prose_authored_by: brigadier-scribe (Cloud Cowork — surface only; Ruslan = sole strategist)
constitutional_posture: R1 surface + R6 + R11 + breadth-NOT-selection + AP-6
target_audience: Ruslan (sole strategist on architecture decision)
status: DECISION-PENDING-RUSLAN
---

# 🔬 Hypothesis-Tables Architecture — 5 Options Deep Analysis

> **R1 enforced.** Brigadier surface 5 options + key questions. **Ruslan picks** (R1 sole strategist). NO recommendation.

---

## §0 Контекст (background)

### Что surface'нул voice (audio_704)

Ruslan explicit request — **hypothesis-tables в Jetix substrate** — concrete artefact tracking method-state evolution. Из batch-8 Phase 4:

- **Hypothesis cycle** = system-life signature (O-99 Tier B pool item):
  - Каждая итерация метода = тест гипотезы
  - Результат → revise method OR proceed
  - Tracking требует substrate (table / db / structured doc)
- **Связь с Левенчук Методология 2025 Гл. 4** (MG4 ⭐⭐⭐): «метод как объект 1-го класса» с state graph
- **Связь с Foundation Part 5** (compound learning) — substrate уже есть для general learning, но без hypothesis-specific structure

### Что hypothesis-tables конкретно делают (use cases)

Каждая запись в hypothesis-table:
- **ID** (H-NNN unique)
- **Гипотеза** (предположение что верно)
- **Метод теста** (как проверим)
- **Условия / scope** (где применимо)
- **Status** (active / testing / confirmed / refuted / paused)
- **Результат** (если closed)
- **Linked artefacts** (что породило / что использует)
- **Created / Updated** timestamps

Примеры применений:
- Outreach hypothesis: «O-75 partnership frame работает лучше O-83 cheat-code для L2 audience» → testing through KA-01/02 sends
- Engineering hypothesis: «3-tier funnel сертификации 3-6 мес = optimal length» → testing through first cohort
- Method hypothesis: «meta-method success formula применима к non-engineering domains» → testing through Education Layer
- Pitch hypothesis: «Левенчук-direct cross-cite increases response rate» → A/B test KA-01

### Вопрос decision

Какая **architecture** для hypothesis-tables в Jetix substrate? 5 options surfaced batch-8 Phase 4 §B.1.

---

## §1 Quick reference table — 5 options

| Op | Architecture | Path / venue | Effort init | Maintenance | Visibility | Best for |
|---|---|---|---|---|---|---|
| **Op-1** | Extension к `wiki/experiments/` | `wiki/experiments/_hypothesis-tables/` | LOW (1-2h) | LOW | Wiki readers | Простые гипотезы; few-per-month volume |
| **Op-2** | New top-level `hypotheses/` dir + skill | `hypotheses/` + `/hypothesis-add` skill | MEDIUM (4-6h scaffolding) | LOW-MEDIUM | Direct dir browsing | Дисциплинированный tracking; many hypotheses |
| **Op-3** | Notion DB + filesystem twin | Notion view + repo MD twin | HIGH (8-12h integration) | MEDIUM (sync) | Notion UI + filesystem | Visual database; non-tech audience |
| **Op-4** | CRM-style frontmatter в existing substrate | YAML tags / `crm/hypothesis-views/` | LOW-MEDIUM (3-4h) | LOW | Cross-substrate aggregation | Hypotheses tied к concrete people/projects |
| **Op-5** | Inline tracking через `_PLAN-OF-DAY` | Per-day inline section | NONE (uses existing) | NONE | Daily logs only | Lightweight; defer architecture |

---

## §2 Op-1 — Extension к `wiki/experiments/` directory

### Что это

Использовать existing `wiki/experiments/` substrate. Создать subdirectory `wiki/experiments/_hypothesis-tables/` с files-per-hypothesis pattern.

### Архитектура

```
wiki/experiments/_hypothesis-tables/
├── H-001-partnership-vs-cheatcode-l2.md
├── H-002-3tier-funnel-duration-optimal.md
├── H-003-levenchuk-cite-response-rate.md
├── ... (one file per hypothesis)
└── _index.md (auto-generated table summary)
```

Каждый file = YAML frontmatter + markdown body:
```yaml
---
id: H-001
title: O-75 partnership frame > O-83 cheat-code (L2 audience)
status: active
created: 2026-05-20
test_method: A/B 20 outreach touches (10 each frame)
scope: L2 amplifiers only
linked_artefacts:
  - decisions/strategic/JETIX-OUTREACH-SCALABLE-2026-05-18.md
  - wiki/concepts/pre-existing-partnership-positioning.md
  - wiki/ideas/cheat-code-positioning.md
---

## Гипотеза
[body...]

## Метод теста
[steps...]

## Результаты (post-closure)
[outcomes...]
```

### Workflow lifecycle

1. **Создание:** Ruslan / brigadier creates H-NNN file через template (5-10 min)
2. **Active phase:** status=active, link к ongoing experiments
3. **Testing:** status=testing, document partial results
4. **Closure:** status=confirmed / refuted / paused, document outcomes
5. **Cross-cite:** linked_artefacts auto-updated через `/lint` (if extension to existing lint)

### Pros

- ✅ **Reuses existing infrastructure** — `wiki/experiments/` namespace already in Foundation
- ✅ **Low scaffolding effort** — 1-2h create template + first H-001
- ✅ **Markdown-native** — searchable through grep / git history
- ✅ **R6 provenance natural** — file-per-hypothesis = clear attribution
- ✅ **Skill /lint compatible** — can extend existing lint rules

### Cons

- ❌ **No dedicated skill** — no `/hypothesis-add` shortcut; manual file create each time
- ❌ **Auto-index требует custom build** — need `/build-hypothesis-index` skill OR manual maintenance `_index.md`
- ❌ **Volume bottleneck** — если >50 hypotheses, file listing становится unwieldy
- ❌ **Cross-substrate aggregation manual** — chart of all hypotheses across substrate = manual compile

### Effort breakdown

- Setup: 1-2h (create template + first hypothesis + lint extension)
- Per-hypothesis create: 5-10 min
- Maintenance: LOW (markdown + git)
- Migration к Op-2 потом: EASY (rename dir, add skill)

### Dependencies

- Foundation `wiki/experiments/` exists ✓
- `/lint` skill exists ✓
- Optional: `/build-hypothesis-index` skill (NEW, ~2h)

### Use cases

- ✅ Per-experiment hypothesis tracking
- ✅ Long-form hypothesis documentation
- 🟡 Cross-hypothesis aggregation (manual)
- ❌ Real-time dashboard view

### Migration paths

- → Op-2: trivial (dir rename + skill add)
- → Op-3: medium (export to Notion + sync)
- → Op-4: medium (extract frontmatter → CRM view)

---

## §3 Op-2 — New top-level `hypotheses/` directory + skill

### Что это

Создать **first-class** `hypotheses/` directory как peer к `decisions/`, `wiki/`, `crm/`. Plus dedicated **`/hypothesis-add`** skill (analogous `/crm-add`).

### Архитектура

```
hypotheses/
├── _index.md (auto-generated dashboard)
├── _schema/
│   ├── hypothesis.schema.yaml (frontmatter schema)
│   ├── status.yaml (active / testing / confirmed / refuted / paused)
│   └── categories.yaml (outreach / engineering / method / pitch / business)
├── _templates/
│   └── hypothesis.md
├── active/
│   ├── H-001-...
│   └── H-NNN-...
├── confirmed/
│   └── H-NNN-... (moved on closure)
├── refuted/
│   └── H-NNN-...
├── paused/
│   └── ...
└── _log.md (append-only history)
```

Plus skills (canonical, analogous `/crm-*`):
- `/hypothesis-add <slug>` — scaffolds new hypothesis с template
- `/hypothesis-update <id>` — status change + reason
- `/hypothesis-close <id> <outcome>` — moves к confirmed/refuted/paused
- `/hypothesis-dash` — dashboard view (active / by category / stuck)
- `/hypothesis-search` — grep across all
- `/hypothesis-stuck` — surfaces hypotheses >14d no update

### Workflow lifecycle

1. **`/hypothesis-add partnership-vs-cheatcode-l2`** → scaffolds H-NNN file в `active/`
2. Ruslan / brigadier fills body + frontmatter
3. **`/hypothesis-update H-NNN --status testing`** → moves к testing
4. **`/hypothesis-close H-NNN --outcome confirmed`** → moves к `confirmed/` + logs to `_log.md`
5. **`/hypothesis-dash`** weekly → status of all active

### Pros

- ✅ **First-class citizenship** — hypothesis-tracking = top concern Jetix
- ✅ **Dedicated skills** — fast workflow (analogous /crm-*)
- ✅ **Status-directories** = file system shows state at glance
- ✅ **Scalable** — schema + skills support 100s of hypotheses
- ✅ **Foundation-friendly** — Pillar C-aligned (methodology discipline)
- ✅ **Compound learning explicit** — `_log.md` = audit trail (Part 5 compatible)
- ✅ **Cross-substrate ref** — frontmatter linked_artefacts canonical

### Cons

- ❌ **Higher init effort** — 4-6h scaffolding (schema + skills + templates + first H)
- ❌ **Yet another top-level dir** — adds cognitive overhead
- ❌ **Skill development cost** — 4-5 NEW skills к maintain
- ❌ **Possible overlap с Foundation Part 5** — needs clear demarcation

### Effort breakdown

- Setup: 4-6h (schema + skills + templates + first 1-2 hypotheses)
- Per-hypothesis create: 2-3 min (via `/hypothesis-add` skill)
- Maintenance: LOW-MEDIUM (skill ops + lint)
- Migration: HARDEST (first-class structure хочешь preserve)

### Dependencies

- Foundation read access (cross-substrate ref via linked_artefacts)
- Optional: integration с Foundation Part 5 compound learning (если hypothesis closes → learning extract)

### Use cases

- ✅ High-volume hypothesis tracking (>20 active concurrently)
- ✅ Discipline-driven (methodology adherence requires tracking)
- ✅ Cross-domain hypotheses (outreach + engineering + method одновременно)
- ✅ Hypothesis-cycle as system-life signature (O-99 operationalization)

### Migration paths

- ← from Op-1: easy (dir rename + skills add)
- → Op-3: easy export к Notion if needed
- ← from inline (Op-5): manual extraction (one-time)

---

## §4 Op-3 — Notion DB + filesystem twin

### Что это

Использовать **Notion database** как primary visualization layer + **filesystem MD twin** для git-versioning. Bidirectional sync (Notion → markdown + markdown → Notion).

### Архитектура

```
Notion side:
- Database «Jetix Hypotheses»
  - Properties: ID / Title / Status / Category / Test Method / Created / Updated / Linked artefacts
  - Views: Active / By category / By person / Stuck >14d
  - Filters / sorts / grouping = visual

Filesystem side:
- hypotheses-notion-twin/
  - H-001-partnership-vs-cheatcode.md (Notion-export twin)
  - H-NNN-...
  - _sync-log.md (sync history)

Sync tool:
- tools/notion-hypothesis-sync.py (bidirectional)
  - Notion API → MD update on filesystem
  - MD update → Notion API on commit/push
```

### Workflow lifecycle

1. Create в Notion UI (rich editor + properties)
2. `python3 tools/notion-hypothesis-sync.py --pull` → MD twin created
3. Git commit MD twin
4. Update в Notion → sync pull → git commit
5. Search via Notion UI (rich filter) OR grep filesystem

### Pros

- ✅ **Rich UI** — best visual experience (dashboard / kanban / calendar views)
- ✅ **Non-tech audience accessible** — partners / investors can view directly
- ✅ **Filters / sorts** — Notion does heavy lifting
- ✅ **Real-time collaboration** — multiple people edit simultaneously
- ✅ **Mobile** — Notion app convenient on phone

### Cons

- ❌ **Highest init effort** — 8-12h (Notion DB setup + sync tool + bidirectional API integration)
- ❌ **Per memory `feedback_cowork_can_push`:** Filesystem = source of truth; Notion = view. Bidirectional sync **violates this принцип** OR requires careful design.
- ❌ **Sync complexity** — conflict resolution / API rate limits / merge edge cases
- ❌ **External dependency** — Notion outage breaks workflow
- ❌ **Less suitable для Foundation-aligned discipline** (Pillar C — Filesystem authoritative)

### Effort breakdown

- Setup: 8-12h (Notion DB schema + sync tool + testing + first hypotheses migrate)
- Per-hypothesis create: 1-2 min (Notion UI fast)
- Maintenance: MEDIUM (sync runs / conflict resolution)
- Migration: COMPLEX (extract from Notion = needs API)

### Dependencies

- Notion API access + token (already have for other Notion ops)
- `tools/notion-*.py` infrastructure (partially exists)
- Conflict resolution policy

### Use cases

- ✅ Mobile / on-the-go hypothesis updates
- ✅ Visual dashboard daily / weekly
- ✅ Partner / investor visibility
- 🟡 Engineering workflow (filesystem still preferred for git ops)
- ❌ Air-gapped / offline work (Notion required online)

### Migration paths

- → Op-1 / Op-2: hard (export Notion → MD then reorganize)
- ← from Op-1 / Op-2: easy (import MDs to Notion)

---

## §5 Op-4 — CRM-style frontmatter в existing substrate

### Что это

**No new directory.** Add **YAML tag/frontmatter** `hypothesis_id: H-NNN` к existing files (wiki concepts / decisions / outreach docs / etc) → aggregate через **virtual view** в `crm/hypothesis-views/`.

### Архитектура

```
В existing files (например wiki/concepts/pre-existing-partnership-positioning.md):
---
title: ...
hypothesis_ids:
  - H-001
  - H-003
hypotheses_active:
  - H-001 status=testing
---

[body]

Plus:
crm/hypothesis-views/ (auto-generated)
├── active.md (aggregates files с hypothesis_ids active)
├── by-category.md
├── stuck.md
└── _build.py (rebuild script)
```

Plus skill `/build-hypothesis-views` — rebuilds aggregation through grep frontmatter всех md files.

### Workflow lifecycle

1. Hypothesis emerges → identify primary artefact (concept / decision / outreach pack / wiki claim)
2. Edit that file's frontmatter: add `hypothesis_ids: [H-NNN]` + body sub-section с hypothesis detail
3. `/build-hypothesis-views` → regenerates aggregation в `crm/hypothesis-views/`
4. Update status в primary file → rebuild

### Pros

- ✅ **Hypothesis-coupled-к-substrate** — гипотеза живёт там где её primary content
- ✅ **No new top-level dir** — extends existing
- ✅ **Cross-substrate native** — aggregation across wiki + decisions + outreach + CRM
- ✅ **Low effort** — 3-4h (frontmatter schema + build script)
- ✅ **CRM-style discoverability** — analogous strategy hooks pattern

### Cons

- ❌ **No standalone file per hypothesis** — harder to find если primary file unclear
- ❌ **Fragmented documentation** — hypothesis state spread через multiple files
- ❌ **Body sub-sections feel grafted** — content awkward в host file
- ❌ **Rebuild dependency** — aggregation always derived (stale until rebuild)

### Effort breakdown

- Setup: 3-4h (schema + build script + sample hypotheses)
- Per-hypothesis: 5-10 min (edit existing file + frontmatter)
- Maintenance: LOW (rebuild script)
- Migration: HARDEST (extract from multiple files)

### Dependencies

- Existing CRM tooling (`/crm-rebuild-index` analogy)
- Lint integration

### Use cases

- ✅ Hypothesis tightly tied к concept / decision artefact
- ✅ Cross-substrate insight tracking
- 🟡 Standalone hypothesis (без obvious host artefact) — awkward
- ❌ Many hypotheses per primary artefact (frontmatter grows)

### Migration paths

- → Op-1 / Op-2: hard (extract from many files)
- ← from inline (Op-5): medium (locate host artefact + frontmatter add)

---

## §6 Op-5 — Inline tracking через `_PLAN-OF-DAY` workflow

### Что это

**Defer architecture decision.** Track hypotheses inline в daily / weekly planning docs. No new infrastructure.

### Архитектура

```
daily-logs/_PLAN-OF-DAY-YYYY-MM-DD.md:

## §X Hypothesis tracking (inline)

### Active
- H-INL-001 (2026-05-21): O-75 partnership > O-83 cheat-code (L2)
  - Status: testing
  - Notes: started А/Б; 5 sends each
- H-INL-002 (2026-05-19): 3-tier funnel duration 3-6мес optimal
  - Status: active (no test yet)

### Closed last week
- H-INL-003: ... [confirmed]
- H-INL-004: ... [refuted]
```

OR в weekly reflection ritual (A-7):

```
daily-logs/_WEEKLY-REFLECTION-YYYY-MM-DD.md:

## Hypothesis tracking summary
- Active: N
- Closed week: N (confirmed: N, refuted: N)
- Stuck (>14d no update): N
```

### Workflow lifecycle

1. Ruslan mentions hypothesis в voice / daily log
2. Inline tracking в `_PLAN-OF-DAY` OR weekly reflection
3. Status updates inline
4. Closed hypotheses archived в weekly reflection retrospective

### Pros

- ✅ **Zero infrastructure cost**
- ✅ **Lightweight** — works for early stage low-volume
- ✅ **Integrated с daily workflow** — no context switching
- ✅ **Pragmatic** — defer architecture until volume justifies

### Cons

- ❌ **No structured aggregation** — hypotheses scattered across daily logs
- ❌ **Hard to query** — «show all active hypotheses» requires grep
- ❌ **Lost over time** — archived в old daily logs, easy to forget
- ❌ **No status tracking discipline** — informal
- ❌ **Doesn't operationalize O-99 hypothesis-cycle-as-system-life**
- ❌ **Левенчук alpha-machinery vision NOT implemented**

### Effort breakdown

- Setup: 0h
- Per-hypothesis: 30 sec (inline note)
- Maintenance: 0h (until you want aggregation, then high)
- Migration: HARDEST (extract from many daily logs)

### Dependencies

- Existing daily log workflow ✓

### Use cases

- ✅ <5 hypotheses ever
- ✅ Solo work, no scale
- 🟡 Early prototype phase
- ❌ Discipline-driven methodology
- ❌ Multi-person team
- ❌ Compound learning (impossible to aggregate)

### Migration paths

- → any other option: HARDEST (extract from daily logs)

---

## §7 Mermaid — 5 options compared

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
quadrantChart
    title 5 Hypothesis-Tables Options × Init Effort × Long-term Value
    x-axis Low effort --> High effort
    y-axis Low long-term value --> High long-term value
    quadrant-1 Major project (high effort, high value)
    quadrant-2 Quick wins (low effort, high value)
    quadrant-3 Defer (low effort, low value)
    quadrant-4 Reconsider (high effort, low value)

    Op-1 wiki experiments ext: [0.2, 0.55]
    Op-2 new hypotheses dir + skills: [0.5, 0.9]
    Op-3 Notion DB + twin: [0.85, 0.65]
    Op-4 CRM-style frontmatter: [0.35, 0.6]
    Op-5 inline daily-log: [0.05, 0.2]
```

---

## §8 Key questions для Ruslan decision

Эти вопросы surface critical decision dimensions. Ответы на них = clarity которая option fits.

### Q1: Expected volume (per month)

- A) **1-5 hypotheses/month** — Op-5 (inline) или Op-1 (wiki ext) подходит
- B) **5-20 hypotheses/month** — Op-1 или Op-2 (skills make difference)
- C) **20+ hypotheses/month** — Op-2 (first-class) или Op-3 (Notion visual)

### Q2: Who reads hypothesis-tables?

- A) **Только Ruslan** — Op-1, Op-2, Op-5 (technical)
- B) **Brigadier agents (для compound learning)** — Op-1, Op-2, Op-4 (structured frontmatter)
- C) **Partners / investors via outreach docs** — Op-3 (Notion visual) OR Op-4 (cross-substrate)
- D) **Public via dashboard** — Op-3 (Notion shared link)

### Q3: Lifecycle longevity expected

- A) **Hypothesis закрывается в 1-2 недели** — Op-5 (inline) OK
- B) **Hypothesis runs 1-3 месяца** — Op-1 / Op-2 (file-based)
- C) **Hypothesis ongoing 6+ месяцев** — Op-2 (status dirs) или Op-3 (Notion long-term)

### Q4: Coupling к existing substrate

- A) **Hypotheses standalone** (рожаются independently) — Op-2 первое-class дир
- B) **Hypotheses всегда tied к concept / decision** — Op-4 (frontmatter в host)
- C) **Mix** — Op-1 (wiki) OR Op-2 (с linked_artefacts) с cross-ref

### Q5: Хотите ли OMG Essence alpha-machinery overlay?

(Per Левенчук cross-link distillation §3.1 GAP-1)

- A) **Да, sometime soon** — Op-2 (scaffolding в дальнейшем поддерживает alpha-states)
- B) **Defer alpha-machinery** — Op-1, Op-4, Op-5 sufficient for current stage
- C) **Параллельно research DR-23 first** — defer architecture, launch DR-23

### Q6: Mobile / on-the-go updates important?

- A) **Yes critically** — Op-3 (Notion mobile app)
- B) **Nice to have** — Op-3 OR Op-1/Op-2 с git client mobile
- C) **No, desktop only** — Op-1, Op-2, Op-4, Op-5

### Q7: Migration risk tolerance

- A) **Low — pick option I'll stick with** — Op-2 (first-class, hardest to migrate)
- B) **Medium — start simple, migrate later** — Op-5 → Op-1 → Op-2 progression
- C) **High — willing to refactor если нужно** — start с anything, change later

### Q8: Discipline-driven adoption likely?

- A) **Yes, я буду disciplined каждую hypothesis tracking** — Op-2 (skills payoff)
- B) **Medium, sometimes forget** — Op-1 (simple file create when remember)
- C) **Spotty, only sometimes** — Op-4 (couples к host artefact, harder to forget) OR Op-5 (inline at minimum)

---

## §9 Common decision patterns (precedent paths)

### Pattern A — Pragmatic start, scale later
**Op-5 (now) → Op-1 (3 months) → Op-2 (12 months если scale).**
- Pros: lowest cost now; defer architecture
- Cons: migration cost при transition

### Pattern B — Discipline-first
**Op-2 (now) — invest 4-6h scaffolding upfront.**
- Pros: skills payoff long-term; first-class citizen
- Cons: 4-6h up-front investment; possible over-engineering early

### Pattern C — Visual / shared
**Op-3 (now) — Notion DB primary.**
- Pros: visual; mobile; sharable с partners
- Cons: filesystem-authoritative violation; sync complexity

### Pattern D — Substrate-tied
**Op-4 (now) — hypotheses в frontmatter существующих artefacts.**
- Pros: hypothesis lives where its content lives
- Cons: fragmented; harder query

### Pattern E — Wiki-extending
**Op-1 (now) — extend `wiki/experiments/`.**
- Pros: reuses Foundation infra; clear file-per-hypothesis
- Cons: no dedicated skills (initially)

---

## §10 Constitutional check per option

| Op | R1 surface | R2 read-only | R6 provenance | R11 default-deny | R12 anti-extraction | Filesystem authoritative |
|---|---|---|---|---|---|---|
| Op-1 | ✅ markdown body | ✅ extends existing | ✅ file per hypothesis | ✅ standard ops | ✅ no extraction risk | ✅ filesystem primary |
| Op-2 | ✅ structured frontmatter + body | ✅ new namespace | ✅ file + log + skills audit | ✅ canonical skills | ✅ no extraction | ✅ filesystem primary |
| Op-3 | 🟡 Notion UI dominant | ✅ filesystem twin | 🟡 sync log required | 🟡 sync API novel | ✅ no extraction | ⚠️ **Notion primary, filesystem twin** — partial violation Pillar C-aligned principle |
| Op-4 | ✅ frontmatter в host | ✅ extends existing | ✅ через host file provenance | ✅ standard | ✅ no extraction | ✅ filesystem primary |
| Op-5 | ✅ inline daily log | ✅ uses existing | 🟡 distributed across daily logs | ✅ none | ✅ no extraction | ✅ filesystem primary |

---

## §11 Reflection prompts для Ruslan (10-15 min)

1. **Vol estimate:** сколько hypotheses на текущей стадии (Q3 2026) обычно tracking simultaneously? (1-5 / 5-20 / 20+?)
2. **Audience:** ты сам читаешь / brigadier тоже / partners тоже / public dashboard?
3. **Daily anchor:** ты хочешь видеть «active hypotheses» в daily review (Friday) OR ad-hoc grep?
4. **Mobile:** updates в Telegram-style on-the-go важно?
5. **Discipline self-assessment:** будешь ли disciplined запускать new H-NNN каждую гипотезу или ленивый?
6. **OMG Essence alpha-machinery:** хочешь Левенчук-style alpha-tracking сейчас (Op-2 паттерн его поддерживает) OR defer?
7. **Migration tolerance:** готов refactor через 3-6 месяцев или хочешь choose-once-and-forget?

После ответа на эти 7 вопросов — option становится obvious.

---

## §12 Decision template

После reflection — записать в REFLECTION-INBOX:

```markdown
## §APPEND-2026-05-20-evening-hypothesis-tables-decision

**Decision:** Op-N [Op-1 / Op-2 / Op-3 / Op-4 / Op-5 / Hybrid]

**Rationale:**
- Q1 volume: [answer]
- Q2 audience: [answer]
- Q3 lifecycle: [answer]
- Q4 coupling: [answer]
- Q5 alpha-machinery: [answer]
- Q6 mobile: [answer]
- Q7 migration: [answer]
- Q8 discipline: [answer]

**Implementation next step:**
- [Если Op-1: scaffolding wiki/experiments/_hypothesis-tables/ template]
- [Если Op-2: write scaffolding prompt + first 1-2 hypotheses]
- [Если Op-3: Notion DB schema + sync tool prompt]
- [Если Op-4: frontmatter schema + build-views script]
- [Если Op-5: inline section template для _PLAN-OF-DAY-YYYY-MM-DD]

**Migration path planned (если applicable):**
- [Future migration trigger condition]
```

---

## §13 What happens after decision

### Если Op-1 picked
- Brigadier scaffolds `wiki/experiments/_hypothesis-tables/` template (1-2h)
- First 1-2 hypotheses migrated from existing pool ideas (O-99 hypothesis cycle as system-life surface)
- Cross-link к `wiki/concepts/method-systems-thinking.md` §APPEND batch-8

### Если Op-2 picked
- Brigadier scaffolds `hypotheses/` first-class dir + schema + templates (4-6h)
- 4-5 NEW skills written (`/hypothesis-add`, `/hypothesis-update`, `/hypothesis-close`, `/hypothesis-dash`, `/hypothesis-stuck`)
- DR-23 research (prior art) optionally launched parallel

### Если Op-3 picked
- Notion DB schema designed (1-2h)
- `tools/notion-hypothesis-sync.py` написан (4-6h)
- First hypotheses imported

### Если Op-4 picked
- Frontmatter schema added (1h)
- `tools/build-hypothesis-views.py` script (2-3h)
- Existing wikis tagged с hypothesis_ids retroactively

### Если Op-5 picked (defer)
- No infrastructure change
- Inline section template для `_PLAN-OF-DAY` (15 min)
- Decision revisited через 3 months OR при volume trigger

---

## §14 Closure

**5 options surfaced + key questions для decision = ready для Ruslan reflection.**

**Per Ruslan voice ack «глубоко прорабатываем»** — deep analysis per option done. Ruslan picks (R1).

**Time budget:** 15-30 min reflection answering Q1-Q8 → decision committed → next implementation step triggers.

---

*Phase 7 Updated Execution Plan A-3 substrate. R1 surface only; Ruslan = sole strategist on architecture choice. R6 + R11 + research-pool-pattern preserved.*
