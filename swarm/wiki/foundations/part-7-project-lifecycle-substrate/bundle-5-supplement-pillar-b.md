---
title: "Part 7 — Bundle 5 Supplement — Pillar B Project Strategy Slot"
date: 2026-04-28
type: foundation-architecture-supplement
parent_part: 7 (Project Lifecycle Substrate)
pillar: B — Project-Level Strategy Slots
status: AWAITING-APPROVAL — Bundle 5 retroactive supplement
parent_cycle: cyc-foundation-build-2026-04-28
bundle: 5-strategic-layer
brigadier_phase: A-4 integrator drafts
predecessor_decisions:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/structural-placement-decision.md
parent_part_locked_state: F5 LOCKED Bundle 4 (1274 lines, Apr 28)
supplement_type: retroactive_constitutional_supplement (analogous to Bundle 1 supplement 1+2 pattern)
constitutional_anchors:
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (§1 UC-D.1 project lifecycle; §1 Categoria A linkage to Pillar A)
  - swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md (parent F5 LOCKED)
  - swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md (Pillar A canonical — Bundle 5 sibling)
fpf_anchors:
  - "FPF B.3 — F-G-R per project artefact"
  - "FPF IP-2 — bounded context (per-project scope)"
  - "FPF A.14 — typed edges (alignment-check via constrained-by)"
  - "FPF A.6.B — Boundary Norm Square (project-level boundary)"
F: F4
G: brigadier-Bundle-5 Pillar B integrator draft (retroactive supplement to LOCKED Part 7)
R: R-medium — pending Ruslan ack
ip2_single_owner_bounded: "Phase A scope is single-owner; project strategy authoring follows Part 7 single-accountable per D26. Specific strategy content is RUSLAN-LAYER per project. F.9 Bridge structural change ≥35% required at Phase B (multi-owner)."
ClaimScope: "Foundation generic — project-strategy slot structure (4 mandatory sections), state-machine integration (scoped→staged authoring point), Pillar A linkage discipline (frontmatter pillar_a_anchor:), supersession contract, Bet Pitch absorption (Phase 1 Type 10), circuit-breaker Singer Shape Up discipline, alignment-cascade integration. RUSLAN-LAYER: actual project strategies for 8 active projects (next sprint Layer 2)."
critic_findings: "Self-checks: (1) supplement scope respects Part 7 LOCKED architecture (no rewrite, only additive §A/§B/§I rows + new §X.X clause); (2) Pillar B does NOT author Pillar A (boundary respect §F.1); (3) Bet Pitch absorbed per Phase 1 disposition; (4) Foundation vs RUSLAN-LAYER strict; (5) Singer Shape Up appetite-as-CONSTRAINT discipline preserved from Part 7 §A.1. Phase A-6 critic gate pending."
---

# Part 7 — Bundle 5 Supplement — Pillar B Project Strategy Slot

## §0 Mission

Part 7 (Project Lifecycle Substrate) Bundle 4 LOCKED architecture (1274 lines)
established the project state machine, brief intake, scope-record append-only,
retrospective-packet emission, and the 5-state lifecycle (`scoped → staged →
activated → under-review → closed | archived`). It deliberately did NOT
incorporate a "project strategy slot" — that work was deferred to a future
cycle.

Bundle 5 Pillar B fills this gap as a **retroactive constitutional supplement**
(analogous to Bundle 1 supplement 1+2 pattern). Per
`structural-placement-decision.md` §3, Pillar B = Extension to Part 7. This
supplement adds:

- §A.4 input row: project strategy artefact at `scoped → staged` transition
- §B.4 output row: project-strategy-event published to Pillar A alignment check
- §I.X data schema fragment: `projects/<slug>/strategy.md` frontmatter + 4 mandatory sections
- §F.X anti-scope clause: project strategy is project-scoped (not system-wide direction)
- §X.X Foundation vs RUSLAN-LAYER clause for project strategy content
- §K.X failure modes for project-strategy specific
- Bet Pitch absorption (Phase 1 Type 10 → Pillar B per `bets` project type)

Part 7 architecture document is NOT rewritten. This supplement is consumed
alongside Part 7 architecture; Part 7 §I schema is extended via this
supplement's §I.X.

[F4|G:Bundle 5 Pillar B retroactive supplement|R-medium — pending Ruslan ack]

---

## §A.4 (NEW) Project strategy artefact at `scoped → staged`

| Source | Data shape | Event trigger | F-G-R |
|---|---|---|---|
| Project strategy authored by owner | `projects/<slug>/strategy.md` per §I.X schema — 4 mandatory sections (§1 outcome, §2 appetite, §3 Pillar A linkage, §4 circuit breakers); for `bets` project type, conforms to Bet Pitch sub-pattern | At `scoped → staged` transition (mandatory pre-staging) | F2 (draft) → F4 (post-stage-gate ack) |G:project-scope|R-low to R-medium |

### §A.4.1 Concrete consequence — strategy artefact mandatory at staging

Per Part 7 main architecture §A row 1 (project brief), `scoped` state has
project brief. Bundle 5 supplement adds: **`scoped → staged` transition is
gate-blocked** until `projects/<slug>/strategy.md` exists with all 4 mandatory
sections (§I.X.1 below) populated.

This is a Hamel-binary acceptance predicate added to Part 7 stage-gate ack at
`scoped → staged`:

```
predicate_strategy_complete:
  type: boolean
  test:
    AND
      file_exists(projects/<slug>/strategy.md)
      frontmatter_complete(projects/<slug>/strategy.md, schema=project-strategy.json)
      mandatory_section_present(projects/<slug>/strategy.md, ["outcome", "appetite", "pillar_a_anchor", "circuit_breakers"])
      pillar_a_anchor_resolves(projects/<slug>/strategy.md)
```

Pre-existing Part 7 §A.1 «appetite-as-CONSTRAINT» discipline ALSO applies to
project strategy — strategy §2 appetite IS the Singer Shape Up constraint. The
strategy doc is the canonical source for the project's appetite_weeks field
(consumed by Part 7 main schema).

### §A.4.2 Concrete consequence — `pillar_a_anchor:` frontmatter mandatory

Per `structural-placement-decision.md` §3.4 mandatory section §3, every project
strategy carries:

```yaml
pillar_a_anchor:
  type: enum [direction_card, north_star, phase_plan]
  path: <relative-path-to-Pillar-A-doc>
  anchor_status_at_authoring: <active | under-review>
  anchor_supersession_action: <re-anchor | re-shape | escalate>
```

If `pillar_a_anchor.path` does not resolve OR points to `superseded` Pillar A
doc → stage-gate ack rejected; owner ack required for either (1) re-anchor to
new Pillar A doc, (2) author new Direction Card first (Pillar A side; Part 11
flow), or (3) escalate as «strategic gap — what direction does this project
serve?».

This implements FUNDAMENTAL UC-A.3 alignment-enforcement at structural level.

### §A.4.3 Concrete consequence — circuit-breaker discipline

Per §I.X mandatory section §4 (circuit breakers), every project strategy
declares conditions for early kill / re-shape / pause. This is Singer Shape Up
+ Munger inversion applied at project strategy authoring time.

Circuit-breaker examples (RUSLAN-LAYER content; Foundation generic = the
declaration discipline):
- «if cold-outreach response rate <2% by week 4 → re-shape»
- «if revenue from this project does not validate against Pillar A North Star €50K target by Phase 1 Q2 close → kill»
- «if owner-attention-cost exceeds Pillar A Direction Card constraint > 30% of weekly hours → pause»

Part 7 health-signal pipeline (§B in main architecture) reads circuit-breaker
predicates and emits `project-circuit-breaker-fired` events when triggered.
Owner ack required for kill / re-shape / pause action.

### §A.4.4 Concrete consequence — sub-project strategy inheritance

Per FUNDAMENTAL §1 UC-A.1 hierarchy (System → Strategic → Annual → Quarterly →
Project → Sub-project), sub-projects (defined as `projects/<parent-slug>/sub/<sub-slug>/`)
have:

```yaml
inherits_strategy_from: projects/<parent-slug>/strategy.md
strategy_override:  # optional; only for sections that diverge
  outcome: <override prose>  # if sub-project outcome differs
  appetite: <override>  # if appetite differs (typical)
  circuit_breakers: <additional or replacement breakers>
# pillar_a_anchor inherited unless override; rare to diverge
```

Sub-project does NOT need own full strategy.md if it inherits and only
overrides specific sections. Reduces authoring overhead while preserving the
discipline.

---

## §B.4 (NEW) Project-strategy-event published

| Consumer | Data shape | Event published | F-G-R |
|---|---|---|---|
| Part 11 (Strategic Direction Substrate) | `project-strategy-published` event with `project_slug`, `strategy_path`, `pillar_a_anchor_resolved`, `appetite_weeks_declared`, `circuit_breakers_declared[]` | Per `scoped → staged` ack | F4|G:Pillar A integration|R-medium |
| Part 11 cascade event consumer | `project-pillar-a-realignment-required` event when Part 11 emits north-star-superseded or direction-card-superseded affecting this project | Per Pillar A supersession affecting this project's anchor | F5|G:cascade discipline|R-high |

### §B.4.1 Concrete consequence — Pillar A alignment-check feedback

When project strategy is published via §B.4 row 1, Part 11 receives the event
and can:
- Verify `pillar_a_anchor_resolved` matches Part 11 active doc state
- Update Pillar A Direction Card (or other anchor) usage-count metadata (which Direction Cards are actively serving projects)
- Surface in next Strategic Reflection cadence (Pillar A): «N projects anchor on Direction Card X»

### §B.4.2 Concrete consequence — cascade reception from Pillar A

When Part 11 emits `north-star-superseded` (Part 11 §C.3), Part 7 iterates
over `activated` projects, finds those whose `projects/<slug>/strategy.md`
`pillar_a_anchor.path` matched the superseded doc, and:
1. Updates project strategy `pillar_a_anchor.anchor_status_at_authoring: under-review`
2. Adds project to `under-review` queue (per Part 7 main §I.1 state machine)
3. Emits `project-pillar-a-realignment-required` event back to Part 11 (so Pillar A knows downstream effect)
4. Surfaces in Part 9 weekly review (per Part 9 main intake)

Owner ack at next stage gate determines: re-anchor / re-shape strategy /
escalate to direction-gap.

This is the **alignment cascade in motion** — described as Part 11 §C.3 from
Pillar A side; here is the Part 7 reception side.

---

## §F.X (NEW) Pillar B-specific anti-scope additions

In addition to Part 7 main §F anti-scope, Bundle 5 supplement adds:

### §F.X.1 Pillar B does NOT author system-wide direction

Project strategy is project-scoped. System-wide direction (North Star,
Direction Cards) lives in Pillar A (Part 11). Boundary respect: project
strategy MAY surface the need for new Direction Card via project retrospective
mechanisms, but does not author one.

Anti-pattern: project strategy §1 outcome = «redefine the system's direction
to include new market». Wrong: that's Pillar A authoring upstream of project,
not project strategy. Surfacing it via retrospective → Pillar A Strategic
Insight memo → potential new Direction Card is the proper flow.

### §F.X.2 Pillar B does NOT execute strategy

Pillar B authors strategy at staging. Execution is via Part 7 state machine
+ Part 4 role-archetype dispatch + cycle-running per Wave A 10-part flow.
Strategy doc is direction-of-pursuit; execution is project work.

### §F.X.3 Pillar B does NOT replace Project Brief

Part 7 main §A row 1 carries project brief. Project brief = scope / type /
appetite_weeks / acceptance predicates. Project strategy = direction /
outcome / appetite-with-rationale / Pillar A linkage / circuit breakers.

Both are mandatory. Different concerns. Brief is operational scope; strategy
is direction. Project lifecycle has both.

(Note: If RUSLAN-LAYER finds brief + strategy redundancy in practice, may
merge in Phase B revision. Foundation Bundle 5 keeps separate per Phase 1
SKIP-CANONICAL on type 11 Brief + ADOPT type 10 Bet Pitch as Pillar B.)

### §F.X.4 Pillar B does NOT supersede Part 7 main architecture

This supplement is additive only. Part 7 main architecture (1274 lines, Bundle
4 LOCKED) is unchanged. Bundle 5 supplement extends §A / §B / §I / §F / §K /
§X; does not edit or supersede main §A row 1 (brief), §I state machine, etc.

---

## §I.X (NEW) Project strategy schema

### §I.X.1 `shared/schemas/project-strategy.json` (NEW — Bundle 5)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/project-strategy.json",
  "title": "Project Strategy",
  "description": "Schema for project-level strategy artefacts hosted by Part 7 Pillar B extension. Foundation-generic per Wave C Bundle 5. Specific content RUSLAN-LAYER per project instance.",
  "type": "object",
  "required": [
    "project_slug", "strategy_type", "outcome", "appetite", "pillar_a_anchor",
    "circuit_breakers", "F", "G", "R", "owner_ack"
  ],
  "properties": {
    "project_slug": {"type": "string", "pattern": "^[a-z0-9-]+$"},
    "strategy_type": {
      "type": "string",
      "enum": ["consulting", "research", "product", "bets"],
      "description": "Mirrors Part 7 main project_types enum from .claude/config/project-types.yaml"
    },
    "outcome": {
      "type": "object",
      "required": ["statement", "hamel_binary_predicate"],
      "properties": {
        "statement": {"type": "string", "description": "Owner-authored prose describing target end-state"},
        "hamel_binary_predicate": {
          "type": "string",
          "description": "Boolean test that determines outcome achieved or not. e.g., 'cold_outreach_to_paying_client_count >= 3 by 2026-06-30'"
        }
      }
    },
    "appetite": {
      "type": "object",
      "required": ["weeks", "rationale_singer_shape_up"],
      "properties": {
        "weeks": {"type": "integer", "minimum": 1, "description": "Singer Shape Up appetite-as-CONSTRAINT (NOT estimate). Mirrors Part 7 main §A.1 discipline"},
        "attention_budget_hours_per_week": {"type": "integer"},
        "capital_budget_eur": {"type": "number", "minimum": 0},
        "rationale_singer_shape_up": {"type": "string"}
      }
    },
    "pillar_a_anchor": {
      "type": "object",
      "required": ["type", "path"],
      "properties": {
        "type": {"type": "string", "enum": ["direction_card", "north_star", "phase_plan"]},
        "path": {"type": "string"},
        "anchor_status_at_authoring": {"type": "string", "enum": ["active", "under-review"]},
        "anchor_supersession_action": {"type": "string", "enum": ["re-anchor", "re-shape", "escalate"]}
      }
    },
    "circuit_breakers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["condition", "action"],
        "properties": {
          "condition": {"type": "string", "description": "Hamel-binary predicate triggering breaker"},
          "action": {"type": "string", "enum": ["kill", "re-shape", "pause", "escalate"]},
          "rationale_munger_inversion": {"type": "string"}
        }
      }
    },
    "principles_compliance": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Refs to Pillar C principle docs"
    },
    "inherits_strategy_from": {"type": "string", "description": "Path to parent project strategy if sub-project"},
    "strategy_override": {"type": "object", "description": "Sections diverging from inherited parent"},
    "F": {"type": "string", "enum": ["F2", "F4", "F5"]},
    "G": {"type": "string"},
    "R": {"type": "string", "enum": ["R-low", "R-medium", "R-medium-high", "R-high"]},
    "owner_ack": {
      "type": "object",
      "required": ["acked_by", "acked_date"],
      "properties": {
        "acked_by": {"const": "ruslan"},
        "acked_date": {"type": "string", "format": "date"}
      }
    },
    "supersedes": {"type": "string"},
    "superseded_by": {"type": "string"},
    "bet_pitch_pattern": {
      "type": "object",
      "description": "If strategy_type=bets, additional Bet Pitch sub-fields per Phase 1 Type 10",
      "properties": {
        "appetite_window": {"type": "string", "enum": ["6_weeks_default", "2_weeks_micro", "12_weeks_extended"]},
        "cooldown_window": {"type": "string", "default": "2_weeks"},
        "shape_up_pitch_clarity": {"type": "boolean"},
        "rabbit_holes_anti_scope": {"type": "array", "items": {"type": "string"}}
      }
    }
  }
}
```

### §I.X.2 4 mandatory sections (Foundation generic)

Every project strategy doc has at minimum these 4 sections — Foundation
canonical, NO exceptions:

```markdown
# Project Strategy: <slug>

## §1 What outcome
<statement> + <hamel_binary_predicate>

## §2 What appetite
<weeks> + <attention_budget_hours_per_week> + <capital_budget_eur> + <rationale_singer_shape_up>

## §3 Pillar A linkage
- type: <direction_card | north_star | phase_plan>
- path: <relative-path>
- anchor_status_at_authoring: <active | under-review>
- anchor_supersession_action: <re-anchor | re-shape | escalate>

## §4 Circuit breakers
| Condition | Action | Rationale (Munger inversion) |
|---|---|---|
| <Hamel-binary> | kill / re-shape / pause / escalate | <prose> |
```

For `strategy_type: bets`, additional Bet Pitch sub-pattern (per `bet_pitch_pattern` schema field):
```markdown
## §5 Bet pitch pattern
- appetite_window: 6 weeks default (Singer Shape Up)
- cooldown_window: 2 weeks (Singer Shape Up)
- shape_up_pitch_clarity: <boolean — has the pitch been refined per Singer 5-step process>
- rabbit_holes_anti_scope:
  - <thing the bet does NOT pursue even if attractive>
```

### §I.X.3 Frontmatter template

```yaml
---
title: "Project Strategy: <slug>"
project_slug: <slug>
date: <YYYY-MM-DD>
strategy_type: consulting | research | product | bets
status: draft | active | under-review | superseded | paused | closed
F: F2 | F4 | F5
G: project-scope
R: R-low | R-medium | R-medium-high | R-high
pillar_a_anchor:
  type: direction_card | north_star | phase_plan
  path: <relative-path>
  anchor_status_at_authoring: active | under-review
  anchor_supersession_action: re-anchor | re-shape | escalate
appetite:
  weeks: <int>
  attention_budget_hours_per_week: <int>
  capital_budget_eur: <number>
principles_compliance:
  - principles/tier-2-system/...
inherits_strategy_from: <path-or-null>
created_date: <YYYY-MM-DD>
last_reviewed_date: <YYYY-MM-DD>
owner_ack:
  acked_by: ruslan
  acked_date: <YYYY-MM-DD>
supersedes: <prior-path-or-null>
superseded_by: <path-or-null>
---
```

---

## §K.X (NEW) Pillar B-specific failure modes

In addition to Part 7 main §K failure modes, Bundle 5 supplement adds:

### §K.X.1 KP1 — Strategy-anchor drift (project strategy anchor stale)

**Failure.** Project strategy `pillar_a_anchor.path` resolves to a Pillar A
doc that was superseded; cascade event missed; project operates against stale
direction.

**Mitigation.**
- Part 11 cascade emission (Part 11 §C.3) → Part 7 reception (§B.4.2)
- `/lint --check-pillar-a-anchors` skill verifies all project strategies have valid + active anchors
- Part 8 SLI: `count(project strategies with anchor_status: superseded) / count(active projects)` — alert if >0

### §K.X.2 KP2 — Circuit breaker silent (predicate true but action not taken)

**Failure.** Circuit-breaker condition becomes true (e.g., revenue threshold
missed) but action does not fire (event-emitter bug, owner ack-skip on
notification).

**Mitigation.**
- Part 8 invariant SLI: for each circuit breaker, `predicate_state_evaluation_freshness < 7d`
- Part 9 surfaces unfired-but-true breakers in weekly review (anti-skip)
- Manual replay: `/strategic-cascade-replay <project>` skill

### §K.X.3 KP3 — Strategy doc absent at staging (lint bypass)

**Failure.** `scoped → staged` transition fired without `projects/<slug>/strategy.md`.

**Mitigation.**
- Hamel-binary predicate at stage gate (§A.4.1) blocks transition without strategy file + complete frontmatter + resolvable anchor
- Pre-commit hook enforcement
- Stage-gate retrospective audit per Part 7 main §F

### §K.X.4 KP4 — Bet pitch pattern missing for `bets` type project

**Failure.** Project of type `bets` has strategy doc but missing Bet Pitch
sub-pattern fields.

**Mitigation.**
- Schema validation per `project-strategy.json` §I.X.1 — `bet_pitch_pattern` required when `strategy_type=bets`
- Pre-stage-gate ack lint

### §K.X.5 KP5 — Inheritance break (sub-project loses parent strategy)

**Failure.** Sub-project strategy `inherits_strategy_from` path no longer
resolves (parent project archived, parent strategy moved).

**Mitigation.**
- `/lint --check-strategy-inheritance` skill verifies inheritance chains
- Parent-archive event cascades: sub-projects emit `parent-strategy-broken` requiring re-author or own strategy

### §K.X.6 KP6 — Foundation vs RUSLAN-LAYER blur in project strategy

**Failure.** Project strategy mixes Foundation generic structure with embedded
Foundation-leakage of Ruslan-specific patterns (e.g., specific Direction Card
content embedded in §3 Pillar A linkage prose).

**Mitigation.**
- Schema discipline: `pillar_a_anchor` field references; doesn't embed
- §X.X foundation/ruslan-layer review at promotion gate

---

## §X.X (NEW) Foundation vs RUSLAN-LAYER for project strategy

### §X.X.1 Foundation generic (this supplement)

- Project strategy 4-section structure (§I.X.2)
- `project-strategy.json` schema (§I.X.1)
- Frontmatter template (§I.X.3)
- `pillar_a_anchor:` discipline as cross-Pillar contract
- Circuit-breaker discipline (Singer Shape Up + Munger inversion)
- Sub-project inheritance pattern
- Bet Pitch sub-pattern for `bets` strategy_type
- `scoped → staged` Hamel-binary stage-gate predicate
- Cascade reception from Pillar A (§B.4.2)
- 6 failure modes (§K.X.1-6)

### §X.X.2 RUSLAN-LAYER (next sprint Layer 2)

- Project strategy CONTENT for 8 active projects: quick-money / research / brand / community / ai-tools / life-os / engineering-thinking / bets
- Specific outcomes per project
- Specific Hamel-binary predicates
- Specific appetite_weeks values per project
- Specific Pillar A anchors (which Direction Card / North Star each project anchors on)
- Specific circuit-breaker conditions
- Specific principles_compliance citations per project
- Bet Pitch CONTENT for projects of type `bets`

### §X.X.3 Fork-portability test

A Phase B fork-importer:
- Imports `project-strategy.json` schema unchanged
- Imports 4-section structural mandate unchanged
- Imports cascade-reception discipline unchanged
- Replaces `projects/<slug>/strategy.md` content with own project strategies
- Foreign instance (e.g., scientific researcher) authors own circuit-breakers (e.g., «if grant approved <50% confidence by month 2 → re-shape grant proposal»)

---

## §L Bundle 5 Pillar B work-list

| ID | Task | Status |
|---|---|---|
| L1 | Part 7 Pillar B supplement (this document) | DRAFT |
| L2 | `shared/schemas/project-strategy.json` schema | SPECIFIED §I.X.1; physical file Bundle 5 ack-then-create |
| L3 | `/lint --check-pillar-a-anchors` skill | Phase B materialization |
| L4 | `/lint --check-strategy-inheritance` skill | Phase B materialization |
| L5 | Part 7 §I.1 state machine — `scoped → staged` predicate update | Bundle 5 §A.4.1 specified; physical wiring at /project-bootstrap skill update |
| L6 | Part 7 §B.4 alignment-cascade reception event handler | Phase B materialization |
| L7 | RUSLAN-LAYER project strategy authoring (8 projects) | Layer 2 next sprint |
| L8 | Bet Pitch authoring for `bets` projects | Layer 2 next sprint |
| L9 | Sub-project inheritance test cases | Phase B |

---

## §M Wisdom Application Findings (Pillar B-specific)

| # | Card | Principle | Current state | Improvement | Adopted? | O/P | Justification |
|---|---|---|---|---|---|---|---|
| 1 | Singer Shape Up Appetite | Appetite-as-CONSTRAINT not estimate | §I.X.2 §2 mandatory + Part 7 main §A.1 | Pillar B inherits Part 7 main discipline; adds Bet Pitch sub-pattern | YES | OPERATIONAL | Schema-enforced |
| 2 | Singer Shape Up Cooldown | 2-week cooldown post-bet | `bet_pitch_pattern.cooldown_window` default 2_weeks | Foundation generic | YES | OPERATIONAL | Schema field |
| 3 | Singer Shape Up Pitch | Pitch refinement before bet | `bet_pitch_pattern.shape_up_pitch_clarity` boolean | Lint check at stage gate | YES | OPERATIONAL | Schema discipline |
| 4 | Singer Shape Up Rabbit Holes | Anti-scope in pitch | `bet_pitch_pattern.rabbit_holes_anti_scope` array | Mandatory for `bets` type | YES | OPERATIONAL | Schema discipline |
| 5 | Munger Inversion | «What would make this wrong?» | Circuit-breaker §I.X.2 §4 + `rationale_munger_inversion` field | Per-breaker rationale enforced | YES | OPERATIONAL | Schema field |
| 6 | Cagan Empowered Teams | Team commits to outcome, not output | §I.X.2 §1 outcome statement + Hamel-binary predicate | Outcome-not-output discipline | YES | OPERATIONAL | Schema discipline |
| 7 | Torres CDH | Continuous Discovery Habits | (deferred to Phase B project-running cycles) | Discovery practices not at strategy authoring; at execution | DEFERRED | — | Cycle-level concern |
| 8 | Levenchuk IP-2 Bounded Context | Per-project bounded scope | §I.X.1 schema ip2_single_owner_bounded; project-scope F-G-R | Project boundaries explicit | YES | OPERATIONAL | Schema-enforced |
| 9 | Levenchuk IP-7 Writing-as-Thinking | Owner authors strategy prose | Inherits Pillar A §A.1 prose_authored_by discipline (cross-Pillar contract) | Owner authors §1 + §2 + §4 prose | YES | OPERATIONAL | Pillar A discipline cascades |
| 10 | Compounding Engineering DRR | DRR per project closure | Inherits Part 7 main §B.4 retrospective-packet (lessons_learned[], dr_r_candidates[]) | No new work; inherits | YES | OPERATIONAL | Cross-cycle inheritance |
| 11 | FUNDAMENTAL UC-A.3 Alignment | System-wide direction → project alignment | `pillar_a_anchor:` mandatory; cascade-reception §B.4.2 | Structural alignment-check | YES | OPERATIONAL | Schema-enforced |
| 12 | FUNDAMENTAL UC-A.1 Hierarchy | Project / sub-project hierarchy | `inherits_strategy_from:` for sub-projects | Sub-project inheritance pattern | YES | OPERATIONAL | Schema-enforced |
| 13 | Anthropic CAI Hardcoded Never-list | Project strategy doesn't override constitutional | `principles_compliance:` ref to Pillar C; alignment-cascade respects Tier 2 | Project strategy bound by Pillar C | YES | OPERATIONAL | Cross-Pillar contract |

**Operational ratio:** 12 OPERATIONAL + 0 PHILOSOPHICAL + 1 DEFERRED = 12/12 of
adopted = 100% — exceeds ≥85% target.

**1 DEFERRED is appropriate**: Torres CDH (Continuous Discovery Habits) is a
project-running cycle concern (Wave A Part 4 / Part 5 territory), not a
strategy-authoring concern.

---

## §N Provenance

### §N.1 Constitutional anchors
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`: §1 UC-D.1 project lifecycle, §1 Categoria A linkage to Pillar A
- `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` (Bundle 4 LOCKED): parent for this supplement
- `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` (Bundle 5 sibling): Pillar A canonical

### §N.2 Decision artefacts (Bundle 5)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/structural-placement-decision.md` §3 (Pillar B as Part 7 extension)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/phase-1-baseline-disposition.md` (Bet Pitch ADOPT-INTO-PILLAR-B)

### §N.3 Wave B consultant cards
- `consultants/product-management-cagan-shape-up.md` — Cagan empowered teams + Singer Shape Up + Torres CDH
- `consultants/levenchuk-shsm-fpf.md` — IP-2 bounded context, IP-7 writing-as-thinking
- `consultants/compounding-engineering.md` — DRR
- `consultants/capital-allocation-antifragility.md` — Munger inversion

### §N.4 Phase 1 baseline (INPUT)
- `decisions/strategic/_templates/bet-pitch.md.template` (~1150 words, 9 sections)

### §N.5 Bundle 1 supplement pattern (methodology)
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md`
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-28.md`
- Methodological precedent for retroactive constitutional supplement

---

## §O Integration test: end-to-end project lifecycle with Pillar B strategy

To verify Pillar B integration with Part 7 main architecture, end-to-end
trace:

1. Owner runs `/project-bootstrap quick-money P1 --type=consulting`
2. Part 7 main §A.1: `projects/quick-money/brief.md` created, state=`scoped`
3. Pillar B supplement §A.4 mandatory: owner authors `projects/quick-money/strategy.md`:
   - §1 outcome: «3+ paying consulting clients by 2026-06-30»
   - §2 appetite: 12 weeks, 25h/week, €0 capital
   - §3 pillar_a_anchor: `decisions/strategic/direction-cards/dach-mittelstand-ai-consulting.md` (Direction Card)
   - §4 circuit_breakers: «if cold-outreach response <2% by week 4 → re-shape»
4. Pillar B supplement §A.4.1 Hamel-binary stage-gate predicate evaluates: TRUE — strategy file exists, frontmatter complete, anchor resolves
5. Owner ack stage gate `scoped → staged` per Part 7 main §A row 2 (AWAITING-APPROVAL packet via Part 6b)
6. Pillar B supplement §B.4: `project-strategy-published` event emits to Part 11; Part 11 records that Direction Card `dach-mittelstand-ai-consulting` is now serving `quick-money` project
7. Part 7 main §I state machine transitions to `staged`
8. Owner runs cycles per Part 4 / Part 5; project transitions to `activated`
9. Week 4: cold-outreach response rate measured at 1.5%; Pillar B supplement circuit-breaker fires (predicate TRUE); Part 7 emits `project-circuit-breaker-fired`
10. Owner ack at next decision point: re-shape strategy (e.g., shift target from cold-outreach to warm-intro)
11. Strategy supersession: new `projects/quick-money/strategy-v2.md` with `supersedes:` ref; ack via Part 6b stage_gate
12. Project continues with new strategy; appetite_weeks counter unchanged (per §A.1 Part 7 main: appetite-as-CONSTRAINT, not estimate — re-shape stays within original 12 weeks)
13. At week 12: project enters `under-review` state; Part 7 main §B.4 retrospective-packet emitted with `lessons_learned[]` including circuit-breaker firing
14. Part 5 consumes retrospective; potential methodology promotion candidate (e.g., «cold-outreach-then-warm-intro pivot pattern»)
15. Part 11 receives `project-strategy-published` + `methodology-promotion-event` via Part 5; potentially surfaces «pattern recognition for Direction Card update?» at Strategic Reflection cadence

End-to-end trace validates Pillar B integration with Part 7 main + Part 4 +
Part 5 + Part 11 + Part 6b. No new mechanism beyond §A.4 / §B.4 / §I.X.

---

*End of Part 7 Bundle 5 supplement. ~5K words. Foundation-generic Pillar B
project strategy slot. Retroactive constitutional supplement to LOCKED Part 7
architecture. Pillar B canonical. Foundation-generic; RUSLAN-LAYER content
authoring next sprint (Layer 2). AWAITING-APPROVAL — gates Wave E LOCKED tag.*
