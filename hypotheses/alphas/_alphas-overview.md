---
title: OMG Essence alpha-machinery — overview (Layer 6)
date: 2026-05-20
type: documentation
parent_layer: 6
sources:
  - "Левенчук А., Методология 2025, Гл. 4 (MG4 ⭐⭐⭐)"
  - "OMG Essence 2.0:2024 standard"
  - research/levenchuk-books-distillation-2026-05-20/06-cross-link-к-jetix-substrate.md §2.10 + §3.1
  - hypotheses/_schema/alphas.yaml
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: hypotheses-alpha-machinery
R: low
---

# Layer 6 — OMG Essence Alpha-Machinery

> Layer 6 of 7. 7 essential progress alphas + state-graphs per hypothesis tracking.
> Per Левенчук Методология 2025 Гл. 4 (MG4 ⭐⭐⭐) — core method-tracking primitive.
> Cross-cite: SEMAT Kernel / OMG Essence 2.0:2024.

## §1 What are Essence Alphas

**Alpha** = essential progress dimension of any endeavor.

OMG Essence 2.0:2024 defines **7 alphas** that together capture state of any
software-development или methodological endeavor. Per Левенчук Методология 2025,
alphas являются first-class progress-tracking primitive — НЕ activities, НЕ artifacts,
а **state of essential things** that change as work progresses.

| Alpha | Domain |
|---|---|
| **Stakeholder** | Entities affected by / interested в outcome |
| **Opportunity** | Reason for endeavor / problem space |
| **Requirements** | What outcome must achieve |
| **Software-System** | Software / artifact being created (adapted: any Jetix artefact) |
| **Work** | Activity being undertaken |
| **Team** | Group performing работу |
| **Way-of-Working** | Practices / methods / tools used |

## §2 State-graphs

Каждая alpha имеет ordered **state graph** — sequence states которые работа проходит:

- **Stakeholder:** recognized → represented → involved → in_agreement → satisfied_for_deployment → satisfied_in_use
- **Opportunity:** identified → solution_needed → value_established → viable → addressed → benefit_accrued
- **Requirements:** conceived → bounded → coherent → acceptable → addressed → fulfilled
- **Software-System:** architecture_selected → demonstrable → usable → ready → operational → retired
- **Work:** initiated → prepared → started → under_control → concluded → closed
- **Team:** seeded → formed → collaborating → performing → adjourned
- **Way-of-Working:** principles_established → foundation_established → in_use → in_place → working_well → retired

State graphs МНК canonical per OMG Essence 2.0:2024 (mermaid diagrams в `state-graphs/`).

## §3 Adaptation к Jetix substrate

**Software-System alpha** обобщён для Jetix:
- agents (.claude/agents/)
- wikis (wiki/concepts/, wiki/ideas/)
- pipelines (tools/run_pipeline.sh, voice pipeline)
- decks / one-pagers (pitch artefacts)
- decisions / Foundation Parts

**Team alpha** охватывает:
- Ruslan (solo founder)
- ROY swarm agents (5 experts + brigadier)
- Partner-handles (Левенчук, Karpathy, Balaji, etc.)
- Founding Circle members (future)

**Way-of-Working alpha** captures:
- Method-systems-thinking
- FPF practices (F-G-R / Bridge / etc.)
- Hypothesis substrate (recursive!)
- Левенчук Метод-Steward practices

## §4 Per-hypothesis alpha usage

Hypothesis frontmatter `alphas:` list:

```yaml
alphas:
  - alpha: work
    state: started
  - alpha: way-of-working
    state: in_use
```

**Not every hypothesis needs all 7 alphas tracked.** Choose 1-3 most relevant
для its phase. E.g.:
- Outreach hypothesis → `stakeholder` + `opportunity`
- Method hypothesis → `way-of-working` + `work`
- Engineering hypothesis → `software-system` + `requirements`
- Personal-dev hypothesis → `team` (just Ruslan) + `way-of-working`

Skill `/hypothesis-alpha-state H-NNN --alpha X --state Y` validates transitions
+ appends к alpha-trail markdown в `state-graphs/<H-NNN>-alpha-trail.md`.

## §5 Cross-link с 5 регионов стратегирования (Левенчук Гл. 6)

Per `hypotheses/_schema/fpf-strategic-regions.yaml`, hypothesis frontmatter
`strategic_region:` complement к alphas. Region влияет на стиль alpha state interpretation:

| Region | Alpha implications |
|---|---|
| **robinson** (Робинзон) | `stakeholder` alpha minimal (just self); `team` alpha may be skipped |
| **catallactic** (каталлактика) | Full alpha tracking; `stakeholder` central; mutual-benefit framing |
| **war** (война) | `stakeholder` adversarial; opponent's `opportunity` matters too |
| **game-theory** | Multi-party `stakeholder` matrix; equilibrium analysis |
| **unknown** | `opportunity` alpha слабо defined; tracking exploration vs optimization |

## §6 Why this matters (per Левенчук)

Per Методология 2025 Гл. 4 — alpha-machinery solves «what state is this endeavor in?»
**better than activity-based или artifact-based tracking** because:

1. **Activities are leaky** — «running tests» doesn't tell you progress
2. **Artifacts are misleading** — «100-page document» doesn't mean «requirements coherent»
3. **Alpha state IS the progress** — «requirements: coherent» = unambiguous state predicate

For Jetix hypothesis substrate:
- Hypothesis F-G-R = formal trust calculus (Layer 5)
- Hypothesis alpha states = method-tracking calculus (Layer 6)
- Together → comprehensive cycle tracking

**GAP (per Левенчук distillation §3.1):** Jetix doesn't yet have OMG Essence integrated. Layer 6 closes this GAP via hypothesis substrate.

## §7 Roster (file map)

```
hypotheses/alphas/
├── _alphas-overview.md            ← this file
├── stakeholder.md
├── opportunity.md
├── requirements.md
├── software-system.md
├── work.md
├── team.md
├── way-of-working.md
└── state-graphs/
    ├── stakeholder-state-graph.md
    ├── opportunity-state-graph.md
    ├── requirements-state-graph.md
    ├── software-system-state-graph.md
    ├── work-state-graph.md
    ├── team-state-graph.md
    └── way-of-working-state-graph.md
```

Per-hypothesis alpha trails: `state-graphs/<H-NNN>-alpha-trail.md` (Phase 8 sample).

## §8 Cross-refs

- **Primary source:** Левенчук Методология 2025 Гл. 4 (MG4 ⭐⭐⭐)
- **OMG Essence:** OMG Essence 2.0:2024 standard
- **Schema:** `hypotheses/_schema/alphas.yaml`
- **5 regions:** `hypotheses/_schema/fpf-strategic-regions.yaml` + Гл. 6
- **Skill:** `.claude/skills/hypothesis-alpha-state.md`
- **Distillation:** `research/levenchuk-books-distillation-2026-05-20/06-cross-link-к-jetix-substrate.md` §2.10 + §3.1 (alpha-machinery GAP closed)
- **Wiki:** `wiki/concepts/method-systems-thinking.md` §APPEND batch-8
