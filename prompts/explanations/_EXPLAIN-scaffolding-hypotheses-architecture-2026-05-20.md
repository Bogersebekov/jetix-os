---
title: EXPLAIN — Hypotheses-Tables Architecture Scaffolding (Op-2+Op-4+Op-5 HYBRID + Excel + alpha-machinery)
date: 2026-05-20 evening
type: prompt-explanation
parent_prompt: prompts/scaffolding-hypotheses-architecture-2026-05-20.md
parent_decision: decisions/REFLECTION-INBOX-2026-05-16.md §APPEND-2026-05-20-evening-hypothesis-tables-decision
prose_authored_by: brigadier-scribe (Cloud Cowork)
target_audience: Ruslan (≤3-min read; уже acked launch)
constitutional_posture: R1 + R2 + R6 + R11 + R12 + EP-5 + append-only + FPF-lens-FIRST
F: F2
G: hypotheses-scaffolding-explain
---

# EXPLAIN — Hypotheses Architecture Scaffolding

> **TL;DR.** Per Ruslan ack 2026-05-20 evening «самый ебейший вариант — Op-2 + альфы Левенчук всё подряд + Excel + CRM-style + inline daily log». Server CC autonomous scaffolds **7-layer architecture** for 500-1000+ hypothesis tracking в filesystem + Excel/CSV + skills + alpha-machinery + FPF F-G-R integration.

---

## §1 Что у нас есть СЕЙЧАС

**Decision committed:** Op-2 + Op-4 + Op-5 HYBRID + Excel + alpha-machinery + FPF integration (REFLECTION-INBOX §APPEND 2026-05-20 evening)

**Substrate ready:**
- `wiki/concepts/method-systems-thinking.md` §APPEND batch-8 (meta-method + hypothesis cycle)
- Левенчук distillation §2.1 (MG4 ⭐⭐⭐ метод как объект 1-го класса)
- Левенчук distillation §3.1 (GAP-1: OMG Essence 2.0:2024 alpha-machinery)
- Левенчук distillation §2.10 (Альфы + state-graphs)
- Foundation Part 5 (compound learning substrate)
- Foundation Part 7 (Project Lifecycle Substrate — stage-gates analogous)
- Pillar C §4.2 (max 20 attention budget — discipline guardrail)
- 5 acked concept docs F2 + Platform v2 + 9+3+4 Tier A wikis
- FPF spec (3758 lines) + F-G-R schemas (`shared/schemas/`)
- CRM tooling pattern (`crm/_schema/` + `/crm-add`) — analogous template

---

## §2 Что делает prompt (одним абзацем)

Server CC autonomous: (a) **Layer 1 first-class `hypotheses/`** dir + schema (FPF F-G-R native) + 3 lifecycle templates; (b) **Layer 2 9 skills** (`/hypothesis-add/update/close/dash/search/stuck/link/build-table/alpha-state`); (c) **Layer 3 CRM-style overlay** — frontmatter `linked_hypotheses` field + `tools/build-hypothesis-views.py`; (d) **Layer 4 inline daily log** — template addition для `_PLAN-OF-DAY` workflow; (e) **Layer 5 FPF F-G-R integration** — frontmatter mandatory F/G/R triple per hypothesis; (f) **Layer 6 OMG Essence alpha-machinery** — `alphas/` subdir с 7 Essence alphas (Stakeholder / Opportunity / Requirements / Software-System / Work / Team / Way-of-Working) + state-graphs per Левенчук Методология Гл. 4 + 5 регионов стратегирования (Robinson Crusoe / каталлактика / война / теория игр / неизвестное); (g) **Layer 7 Excel/CSV table layer** — `tables/hypotheses.xlsx` + `.csv` mirror + `_build-table.py` (openpyxl/pandas); (h) **Sample data**: 3-5 starter H-NNN hypotheses migrated from existing pool (O-99 hypothesis-cycle + outreach test + meta-method validation); (i) **2 mermaid diagrams** + documentation.

**НЕ делает:** Notion DB integration (per Ruslan SKIP «похуй» 2026-05-20) / Foundation modifications / strategic prose authoring (R1).

---

## §3 Что берёт на вход

- `wiki/concepts/method-systems-thinking.md` §APPEND batch-8 (meta-method + hypothesis cycle conceptual basis)
- `research/levenchuk-books-distillation-2026-05-20/06-cross-link-к-jetix-substrate.md` §2.1, §2.10, §3.1 (Левенчук meta-method + alphas + alpha-machinery GAP)
- `raw/external/levenchuk-books-2026-05-20/converted/03-metodologiya-2025.md` (Методология 2025 Гл. 4 verbatim text)
- `crm/_schema/` + `crm/_templates/` (analogous structure — copy-pattern)
- `shared/schemas/` (FPF F-G-R schemas + Foundation contracts)
- `tools/transcribe.py` + existing Python tooling pattern (openpyxl / pandas may need install)
- Foundation Part 5 + Part 7 (cross-ref existing learning + stage-gate substrate)
- REFLECTION-INBOX §APPEND-2026-05-20-evening-hypothesis-tables-decision (architecture spec)

---

## §4 9 phases

| # | Phase | Time | Commit |
|---|---|---|---|
| 0 | Pre-flight + FPF lens + read all substrate | 10-15m | `[hypotheses-scaffold] Phase 0 pre-flight + substrate read` |
| 1 | **Layer 1**: `hypotheses/` dir + `_schema/` + 3 lifecycle templates | 60-90m | `[hypotheses-scaffold] Phase 1 Layer 1 dir + schema + templates` |
| 2 | **Layer 2**: 9 canonical skills (CRM-analogous) | 120-180m | `[hypotheses-scaffold] Phase 2 Layer 2 9 skills` |
| 3 | **Layer 5**: FPF F-G-R integration in schema (frontmatter mandatory triple) | 30-45m | `[hypotheses-scaffold] Phase 3 Layer 5 FPF F-G-R` |
| 4 | **Layer 6**: OMG Essence alpha-machinery (`alphas/` + 7 alphas + 5 регионов стратегирования + state-graphs) | 60-90m | `[hypotheses-scaffold] Phase 4 Layer 6 alpha-machinery` |
| 5 | **Layer 7**: Excel/CSV table layer + `_build-table.py` (openpyxl/pandas) | 45-60m | `[hypotheses-scaffold] Phase 5 Layer 7 tables xlsx/csv` |
| 6 | **Layer 3**: CRM-style overlay frontmatter + `tools/build-hypothesis-views.py` | 45-60m | `[hypotheses-scaffold] Phase 6 Layer 3 CRM frontmatter overlay` |
| 7 | **Layer 4**: Inline daily log integration template | 15-30m | `[hypotheses-scaffold] Phase 7 Layer 4 daily log inline` |
| 8 | Sample data + 2 mermaid + documentation + Summary + push | 30-45m | `[hypotheses-scaffold] Phase 8 sample data + docs + push` |

**Total: ~7-12h server CC autonomous; <€5 (built-in tools + possible pip install openpyxl/pandas).**

---

## §5 Что получим на выходе (file map)

```
hypotheses/                                      ⭐ NEW first-class directory
├── _index.md (auto-generated dashboard)
├── _schema/
│   ├── hypothesis.schema.yaml                   (FPF F-G-R frontmatter)
│   ├── status.yaml                              (active / testing / confirmed / refuted / paused)
│   ├── categories.yaml                          (outreach / engineering / method / pitch / business / personal-dev / partnership / fpf-extension)
│   ├── alphas.yaml                              (7 Essence alphas + state definitions)
│   ├── ownership.yaml                           (Ruslan / brigadier / specific agent / partner)
│   ├── outputs.yaml                             (deliverable types)
│   ├── resources.yaml                           (per Platform v2 §3 32-resource framework)
│   ├── fpf-strategic-regions.yaml               (5 регионов стратегирования Левенчук Гл. 6)
│   └── fgr-triple.yaml                          (FPF B.3 F-G-R schema reference)
├── _templates/
│   ├── hypothesis.md                            (base template — короткий цикл)
│   ├── hypothesis-short.md                      (1-7 days lifecycle)
│   ├── hypothesis-medium.md                     (1-3 months)
│   └── hypothesis-long.md                       (3-6+ months)
├── active/                                       (status dir)
├── testing/                                      (status dir)
├── confirmed/                                    (status dir)
├── refuted/                                      (status dir)
├── paused/                                       (status dir)
├── _log.md                                       (append-only audit trail)
├── alphas/                                       ⭐ NEW OMG Essence
│   ├── _alphas-overview.md
│   ├── stakeholder.md
│   ├── opportunity.md
│   ├── requirements.md
│   ├── software-system.md
│   ├── work.md
│   ├── team.md
│   ├── way-of-working.md
│   └── state-graphs/                             (per-alpha state transitions)
├── tables/                                       ⭐ NEW Excel/CSV layer
│   ├── hypotheses.xlsx                          (master Excel; filtered views built-in)
│   ├── hypotheses.csv                           (filesystem-friendly mirror)
│   ├── alphas-state-graph.xlsx                  (OMG Essence alpha tracking)
│   ├── _build-table.py                          (rebuild script — openpyxl/pandas)
│   └── README.md                                (usage docs)
├── samples/                                      (3-5 starter H-NNN)
│   ├── H-001-meta-method-success-formula-applicable-cross-domain.md
│   ├── H-002-partnership-frame-better-than-cheatcode-l2.md
│   ├── H-003-3tier-funnel-3to6-months-optimal.md
│   ├── H-004-imagination-as-intellect-component.md
│   └── H-005-method-as-1st-class-object-recursive-engine.md
└── docs/
    ├── architecture-overview.md                  (7-layer architecture)
    ├── workflow-guide.md                         (how to add / update / close)
    ├── fpf-integration.md                        (F-G-R triple usage)
    ├── alpha-machinery-guide.md                  (OMG Essence application)
    ├── excel-table-usage.md                      (xlsx/csv workflow)
    └── diagrams/
        ├── 01-7-layer-architecture.md            (mermaid)
        └── 02-hypothesis-lifecycle.md            (mermaid)

.claude/skills/                                  ⭐ NEW 9 skills
├── hypothesis-add.md
├── hypothesis-update.md
├── hypothesis-close.md
├── hypothesis-dash.md
├── hypothesis-search.md
├── hypothesis-stuck.md
├── hypothesis-link.md
├── hypothesis-build-table.md
└── hypothesis-alpha-state.md

tools/
└── build-hypothesis-views.py                    ⭐ NEW CRM-style aggregation

daily-logs/                                       ⭐ template extension
└── _PLAN-OF-DAY-template.md (updated с inline hypothesis section)

§APPEND (existing — append-only):
├── reports/phase-0-fpf-scope/01-jetix-objects-inventory.md (§28 hypotheses architecture)
├── decisions/REFLECTION-INBOX-2026-05-16.md (already done — decision recorded)
├── wiki/log.md (architecture launch entry)
└── daily-logs/_DAILY-LOG-2026-05-20.md (§APPEND hypotheses scaffolding execution)
```

**Total NEW files estimate: ~50-70 files** (schema + templates + skills + alphas + tables + samples + docs).

---

## §6 Hypothesis frontmatter schema (Layer 1 + 5 + 6 detail)

```yaml
---
id: H-NNN                                          # unique
title: <short statement>
slug: <kebab-case>
status: active | testing | confirmed | refuted | paused
category: outreach | engineering | method | pitch | business | personal-dev | partnership | fpf-extension
lifecycle: short | medium | long                   # 1-7d / 1-3mo / 3-6mo+
created: 2026-05-20
updated: 2026-05-20
owner: ruslan | brigadier | <agent-id> | <partner-handle>

# FPF F-G-R triple (Layer 5)
fpf_F: F2 | F3 | F4 | F5 | F6 | F8                 # Formality grade per FPF B.3
fpf_G: <group-scope>                               # G — scope of claim
fpf_R: low | medium | high                         # R — reliability

# OMG Essence alpha (Layer 6)
alphas:
  - alpha: stakeholder | opportunity | requirements | software-system | work | team | way-of-working
    state: identified | accepted | involved | satisfied  # per alpha state-graph
  # multiple alphas possible

# 5 регионов стратегирования (Левенчук Методология Гл. 6)
strategic_region: robinson | catallactic | war | game-theory | unknown

# Resources (per Platform v2 §3 32-resource framework)
resources_needed:
  - resource: <name>
    estimate: <amount>
  
# Cross-link (Layer 3 — CRM-style overlay)
linked_artefacts:
  - <path/to/concept-doc.md>
  - <path/to/wiki.md>
linked_hypotheses:
  - H-NNN                                          # related hypothesis

# Test method
test_method: <description>
test_scope: <where applicable>
success_criteria: <observable / verifiable>
refutation_criteria: <what would falsify>

# Outputs (post-closure)
outcome: <if status=confirmed/refuted/paused>
learning_extracted: <if compound learning applies>
---

## Гипотеза
[body — Russian primary, FPF-aligned]

## Метод теста
[steps]

## Результаты (post-closure)
[outcomes]

## Cross-cite Левенчук (optional)
[if relevant — Методология Гл. X / СМ Т Y Гл. Z]
```

---

## §7 К чему ведёт

After scaffolding complete:
1. **Filesystem ready** для 500-1000+ hypotheses (status dirs scale)
2. **Excel/CSV layer** для visual/filter (Claude Code edits через openpyxl)
3. **9 skills готовы** — `/hypothesis-add` etc. за 2-3 min per hypothesis
4. **OMG Essence alpha-machinery** integrated — Левенчук-direct method tracking
5. **FPF F-G-R native** — Foundation-compatible primitives
6. **CRM-style overlay** — cross-substrate aggregation
7. **3-5 starter hypotheses** migrated from existing pool (Tier B candidates O-99 / outreach / etc.)
8. **Sample workflow validated**

**Next step после scaffolding:**
- Ruslan reviews architecture overview + 3-5 samples (~10-15 min)
- Adjust schema/skills if needed
- Migration: 22 Tier B pool candidates + 17 DR pool items → review для hypothesis conversion
- Daily workflow: `/hypothesis-add` per emerging idea / question / claim

---

## §8 Mermaid

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TB
    subgraph "7-Layer Architecture"
        L1[Layer 1: hypotheses/ first-class dir<br/>schema + templates + status dirs]
        L2[Layer 2: 9 canonical skills<br/>/hypothesis-add /update /close /dash /search /stuck /link /build-table /alpha-state]
        L3[Layer 3: CRM-style overlay<br/>linked_hypotheses frontmatter + build-views.py]
        L4[Layer 4: Inline daily log<br/>_PLAN-OF-DAY hypothesis section]
        L5[Layer 5: FPF F-G-R integration<br/>frontmatter mandatory F/G/R triple]
        L6[Layer 6: OMG Essence alpha-machinery ⭐<br/>7 alphas + state-graphs + 5 регионов стратегирования]
        L7[Layer 7: Excel/CSV table layer<br/>hypotheses.xlsx + .csv mirror + _build-table.py]
    end

    subgraph "Substrate refs"
        FOUND[Foundation Part 5 + Part 7]
        WIKI[Tier A wikis 12 + ideas 1]
        LEV[Левенчук Методология Гл. 4+6]
        FPF[FPF B.3 F-G-R schemas]
        CRM[CRM analogous tooling]
    end

    subgraph "Workflow"
        ADD[/hypothesis-add → scaffolds H-NNN]
        TRACK[/hypothesis-update → status]
        CLOSE[/hypothesis-close → archive + log]
        DASH[/hypothesis-dash weekly]
        BUILD[/hypothesis-build-table → xlsx/csv]
    end

    L1 --> L2 --> L3 --> L4
    L5 -.frontmatter.-> L1
    L6 -.alpha overlay.-> L1
    L7 -.derived.-> L1

    FOUND -.substrate.-> L1 & L6
    WIKI -.cross-link.-> L1 & L3
    LEV -.alpha-machinery + 5 regions.-> L6
    FPF -.F-G-R primitives.-> L5
    CRM -.skill pattern.-> L2 & L3

    ADD --> TRACK --> CLOSE --> DASH
    DASH -.weekly view.-> BUILD

    style L6 fill:#d6f0d6,color:#000
    style L7 fill:#ffe0a0,color:#000
    style ADD fill:#ffd6d6,color:#000
```

---

## §9 Constitutional posture

- **R1 surface.** Brigadier-scribe scaffolding + structure; strategic prose / hypothesis content = Ruslan
- **R2.** Foundation read-only; NEW namespace `hypotheses/` + skills + tools
- **R6.** Per-hypothesis provenance (created / updated / linked_artefacts)
- **R11.** Default-Deny — only canonical skill patterns (analogous /crm-*); no novel actions auto-launched
- **R12.** Hypothesis substrate ≠ extraction; testing process anti-extraction-compatible
- **EP-5 F-grade.** Mandatory F/G/R frontmatter triple per hypothesis
- **Append-only.** _log.md audit trail; status moves = file moves + log entry
- **FPF lens FIRST.** Phase 0 mandatory; Layer 5 integration
- **Filesystem authoritative.** No Notion (Op-3 SKIPPED per Ruslan ack)

---

## §10 Cost + runtime

- **Runtime:** ~7-12h server CC autonomous (9 phases; biggest = Layer 2 9 skills 2-3h)
- **Cost:** <€5 (built-in tools mostly; possible `pip install openpyxl pandas` if not available)
- **Per-phase commit + push** preserves recoverability

---

*EXPLAIN closure 2026-05-20 evening. Ruslan acked launch — «ебашь это prompt и пусть уже ебашит всё что только можно». Per memory `feedback_prompt_explanation_required.md` + `feedback_cowork_can_push.md`.*
