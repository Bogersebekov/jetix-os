---
title: "Strategic Layer — Hierarchy, Cadences, Owner Matrix (Etap 2 of Генеральная чистка)"
date: 2026-04-28
type: research-output
phase: research-phase-3-hierarchy-cadences
author: Cloud Code (server) — direct integrator-mode synthesis
purpose: >
  For the 7 PROPOSE types from Phase 2 — define hierarchy roles, parent dependencies,
  cadences, owners (per FUNDAMENTAL §7.4 5-tier model), triggers, audiences, F-level
  defaults, and Foundation-part cross-references. Output: dependency graph + cadence
  calendar + owner matrix. Used as input for Phase 4 (structural templates).
F: F2
G: "Strategic Layer scoping for Etap 2; not constitutional. Subject to Ruslan ack."
R: "Refuted if Ruslan walkthrough finds the dependency graph requires ≥2 missing edges OR if cadences are off by ≥1 zoom-level (e.g., declared 'quarterly' but should be 'event-driven')."
inputs:
  - decisions/strategic/_research/landscape-strategic-docs-2026-04-28.md (Phase 1)
  - decisions/strategic/_research/jetix-fit-filtering-2026-04-28.md (Phase 2 — 7 PROPOSE list)
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md §7.4 5-tier access model + §8 phasing
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md (10 Foundation Parts — for cross-references)
  - design/JETIX-FPF.md (skim — A.14 typed-edge vocabulary for the dependency graph)
honest_limits:
  - >
    Cadences for Type 14 Mentor Brief are per-mentor — corpus has only the deferred
    "Антон" mention; sample size N=1. The "event-driven (per call) + per-mentor
    cadence" declaration assumes pattern emerges; Ruslan should validate or override.
  - >
    The dependency graph uses **typed A.14 edges** at low resolution (overlays /
    pulls-from / contains / synthesizes-from / candidates-promotion-to). FPF A.14
    canonical edges (ComponentOf, ConstituentOf, PortionOf, PhaseOf, MemberOf,
    AspectOf) are too narrow for these strategic-doc relations; Jetix-introduced
    edges (creates, operates-in, methodologically-uses, constrained-by per
    Levenchuk consultant card §4 P4) cover most. Honest flag: this is
    less-rigorous-than-FPF; tighten in Phase 4 if Ruslan requires.
---

# Strategic Layer — Hierarchy, Cadences, Owner Matrix

## §0 PROPOSE cohort recap (from Phase 2)

| # | Type | Slug |
|---|---|---|
| 03 | Locks Ledger Entry | `lock-entry` |
| 04 | Founder Overlay (RUSLAN-LAYER) | `founder-overlay` |
| 05 | North Star / DoT | `north-star` |
| 06 | Strategic Insight Memo | `strategic-insight` |
| 07 | Direction / Pillar Card | `direction-card` |
| 10 | Bet Pitch / Shape-Up Pitch | `bet-pitch` |
| 14 | Mentor / Stakeholder Briefing Pack | `mentor-brief` |

Slugs are used in Phase 4 template filenames (`<type-slug>.md.template`).

---

## §1 Dependency graph

ASCII rendering (typed-edge labels in lowercase between nodes; nodes carry their
canonical type-name + slug):

```
                              ┌──────────────────────────────────────┐
                              │ Type 01  Foundation Vision           │  (LOCKED v1.0 —
                              │          (FUNDAMENTAL)                │   managed in
                              │   `decisions/JETIX-VISION-…2026-04-27`│   _index.md;
                              └──────────────┬───────────────────────┘   not Strategic
                                             │ overlays                  Layer template)
                                             ▼
                              ┌──────────────────────────────────────┐
                              │ Type 04  Founder Overlay             │
                              │           (RUSLAN-LAYER)              │
                              │   slug: `founder-overlay`             │
                              └──────┬───────────────────────┬────────┘
                                     │ positions             │ informs
                                     ▼                       ▼
        ┌──────────────────────────────────────┐    ┌─────────────────────────────────┐
        │ Type 05  North Star / DoT            │    │ Type 03  Locks Ledger Entry     │
        │   slug: `north-star`                 │    │   slug: `lock-entry`             │
        │                                      │    │   (append-only ledger;          │
        │   gravity well for Directions        │    │    referenced by every other    │
        │                                      │    │    strategic doc)               │
        └──────────────┬───────────────────────┘    └────────▲────────────────────────┘
                       │ pulls                              │ candidate-promotion
                       ▼                                    │
        ┌──────────────────────────────────────┐    ┌───────┴───────────────────────┐
        │ Type 07  Direction / Pillar Card     │    │ Type 06  Strategic Insight    │
        │   slug: `direction-card`             │◄───┤          Memo                  │
        │                                      │ candidate-promotion (or stay one-  │
        │   (multiple instances —              │    │   shot if not Direction-class)│
        │    active / deferred-Phase-2+ /      │    │   slug: `strategic-insight`   │
        │    archived)                          │    └───────────────────────────────┘
        └──────────────┬───────────────────────┘
                       │ contains-shaped-bets
                       ▼
        ┌──────────────────────────────────────┐
        │ Type 10  Bet Pitch / Shape-Up Pitch  │
        │   slug: `bet-pitch`                  │
        │                                      │
        │   (per-cycle 6w + 2w cooldown)       │
        └──────────────┬───────────────────────┘
                       │ instantiates
                       ▼
        ┌──────────────────────────────────────┐
        │ Type 11  Project Brief               │  ← Foundation Layer
        │   (NOT Strategic Layer template)     │     `swarm/wiki/_templates/
        └──────────────────────────────────────┘      project-{4 types}/`

        ┌──────────────────────────────────────┐
        │ Type 14  Mentor / Stakeholder Brief  │
        │   slug: `mentor-brief`               │
        │                                      │
        │   synthesizes-from: Types 03, 04,    │
        │   05, 07, 10 + current Phase status  │
        │   (sanitization gate per §6.4)        │
        └──────────────────────────────────────┘
```

**Edge-type vocabulary used (low-resolution; FPF A.14 strict-typing tightened in
Phase 4 if Ruslan requires):**

- `overlays` — Type 04 overlays Type 01 (instance overlay over generic spec)
- `positions` — overlay positions the North Star (geographic anchor)
- `informs` — overlay informs Locks (what's locked depends on positioning)
- `pulls` — Direction Card pulls from North Star (gravity well)
- `contains-shaped-bets` — Direction Card contains Bet Pitches as the operating
  unit
- `instantiates` — Bet Pitch instantiates a Project Brief (cross-layer to
  Foundation)
- `candidate-promotion` — Strategic Insight Memo can be promoted to Direction
  Card OR Lock Ledger Entry (one-way arrow)
- `synthesizes-from` — Mentor Brief synthesizes from multiple upstream types
  (multi-source read-only relation)

**Foundation-edge note.** No edge in the graph crosses *into* Strategic Layer from
Foundation Layer; the relation is one-way (Strategic Layer → Foundation Layer).
This is intentional: Strategic Layer constrains Foundation Layer execution; not
the reverse.

---

## §2 Cadence calendar

| Type | Annual | Quarterly | Monthly | Event-driven | Append-only |
|---|:-:|:-:|:-:|:-:|:-:|
| 03 lock-entry | — | review-coherence | — | ✓ creation | ✓ |
| 04 founder-overlay | ✓ baseline | review | — | ✓ Phase-transition | — |
| 05 north-star | ✓ major-review | ✓ soft-update | — | ✓ Phase-transition | — |
| 06 strategic-insight | — | — | — | ✓ creation | — |
| 07 direction-card | — | ✓ activation/deferral | — | ✓ status-change | — |
| 10 bet-pitch | — | — | — | ✓ per-cycle (6w+2w) | — |
| 14 mentor-brief | — | — | — | ✓ per-call | — |

**Reading the table:**

- ✓ in **Annual** column = the type has a *yearly* mandatory ritual (e.g., North Star
  major review at Phase boundary or year-end). Empty = no annual obligation.
- ✓ in **Quarterly** column = quarterly review/update touch.
- **Event-driven** column = the *primary* cadence for most types — they fire when
  a trigger arrives, not on a calendar.
- **Append-only** column flags types where the artifact accumulates rather than gets
  rewritten (Type 03 Locks is the canonical case; addenda over time).

**Calendar layout (illustrative — first 12 months from Phase-1 start):**

```
Month  →  M1  M2  M3  M4  M5  M6  M7  M8  M9 M10 M11 M12
North-Star ★              ◇                ◇              ★    (★=major; ◇=soft-update)
Founder-Overlay ★              ◇                ◇                ★    (★=annual baseline)
Direction quarterly review            ◇            ◇            ◇    (✓quarterly)
Lock coherence audit                  ◇            ◇            ◇    (✓ FPF-Steward IP-4)
Bet Pitch cycle    ✦__cooldown__✦__cooldown__✦__cooldown__✦__cool   (✦=cycle close)
Strategic Insight     ▴   ▴ ▴      ▴       ▴ ▴ ▴      ▴           (▴=event-driven N≈1-2/wk peak)
Mentor brief                ▾                  ▾              ▾    (▾=per call)
Lock entry creation        ▴      ▴       ▴     ▴       ▴ ▴       (▴=event-driven, sparse)
```

---

## §3 Owner matrix

Per FUNDAMENTAL §7.4 5-tier access model: T0 Founder / T1 Trusted-core agents /
T2 Specialised agents / T3 Inner stakeholders / T4 Outer stakeholders.

| Type | Author | Approver | Reader (primary) | Reader (secondary) |
|---|---|---|---|---|
| 03 lock-entry | T0 (drafted) + T2 (proposal-class draft) | **T0 mandatory** | T0 + T1 + T2 (all agents reference) | T3 mentor at quarterly |
| 04 founder-overlay | T0 author + T2 structuring-support | T0 | T0 + T1 + T2 (every cycle reads) | T3 mentor for strategic discussion |
| 05 north-star | T0 author + T2 multi-chat-synthesis-support | T0 | T0 + T1 (gravitational reference) | T3 mentor + T4 partners (sanitized) |
| 06 strategic-insight | T0 + T2 drafting | T0 | T0 + T1 (memos referenced) | T3 mentor (selected) |
| 07 direction-card | T0 + T2 drafting | T0 | T0 + T1 + T2 mini-swarm operating in Direction | T3 mentor at quarterly |
| 10 bet-pitch | T0 shaping + T2 drafting-support | T0 (betting-table ritual T0-only) | T0 + T1 + T2 in Direction mini-swarm | — |
| 14 mentor-brief | T0 + T2 drafting + T2 sanitization-check | T0 (incl. sanitization ack) | T0 + T3 mentor | — |

**Key principles preserved:**

- **T0 final-ack on every Author/Approver cell** — operationalizes
  `feedback_ai_does_not_strategize` (AI proposes, Ruslan decides) per inferred
  memory.
- **No T2-only authoring** — every type carries T0 author or T0+T2 partnership;
  no "agent-only" output reaches Approver column.
- **Sanitization checkpoint on Mentor Brief** — operationalizes §6.4 privacy
  boundary in template form.
- **Mentor (T3) reads but does not approve** — preserves §7.4 tier discipline
  (mentor influences thinking but never holds approval authority).

---

## §4 Per-type field declarations

For each PROPOSE type — frontmatter fields ready for Phase 4 templates:

### 4.1 Type 03 — `lock-entry`

| Field | Default value |
|---|---|
| Hierarchy role | standalone (each Lock self-contained); referenced by all |
| Parent dependency | Type 01 Foundation Vision §6 anti-scope (Lock must respect) |
| Cadence | append-only; event-driven creation |
| Owner | ruslan-only authority on creation/reversal; agent-draft proposed; T0 ack mandatory |
| Trigger | significant decision warranting irreversibility status; cycle-pattern accumulation; mentor-call lock-candidate |
| Audience | T0/T1/T2 internal-primary; T3 mentor on request; never T4 public |
| F default | F4 (operational convention across multiple cycles) → F5 (peer-reviewed via mentor) |
| Foundation cross-refs | Part 6 (governance gate consumes); Part 1 (state persistence stores); Part 8 (health monitor checks coherence) |

### 4.2 Type 04 — `founder-overlay`

| Field | Default value |
|---|---|
| Hierarchy role | child of Type 01 (overlays) |
| Parent dependency | Type 01 Foundation Vision LOCKED |
| Cadence | annual baseline + event-driven amendments at Phase transitions |
| Owner | T0 author + T2 structuring-support; T0 ack |
| Trigger | Phase transition / major positioning shift / significant Direction activation |
| Audience | T0/T1/T2 internal-primary; T3 mentor for strategic discussion |
| F default | F3 (single-author scoping) → F4 once Phase-validated |
| Foundation cross-refs | Part 6 (governance gate ack); Part 4 (role taxonomy bind via overlay); Part 9 (owner interaction scaffold consumes) |

### 4.3 Type 05 — `north-star`

| Field | Default value |
|---|---|
| Hierarchy role | standalone (gravity well); pulls from Type 04 + Type 01 §1 |
| Parent dependency | Type 04 Founder Overlay (positioning anchors) + Type 01 §1 use cases |
| Cadence | annual major review + quarterly soft updates; major rewrite at Phase transitions |
| Owner | T0 only with multi-chat methodology (5-chat per `methodology_multi_chat_review_for_critical_docs`); T2 synthesis-support; T0 ack |
| Trigger | annual review / Phase transition / major external signal (e.g., AI-BIOS Moment-class) |
| Audience | T0/T1 internal + T3 mentor; T4 partners get sanitized variant only |
| F default | F3 (aspirational anchor) → F4 once mentor-reviewed |
| Foundation cross-refs | Type 07 Directions (cards pull from); Part 9 (owner interaction surfaces North Star at quarterly) |

### 4.4 Type 06 — `strategic-insight`

| Field | Default value |
|---|---|
| Hierarchy role | standalone; can candidate-promote → Type 03 Lock OR Type 07 Direction |
| Parent dependency | Type 04 + Type 05 + Type 01 §6 anti-scope check |
| Cadence | event-driven (concept-arrival); ~1-2/week during high-insight periods, sparse otherwise |
| Owner | T0 + T2 drafting; T0 ack |
| Trigger | research-trigger + voice-brainstorm combination; insight wanting to be written |
| Audience | T0/T1 internal; selected memos T3 mentor |
| F default | F2 (insight-stage) → F3-F4 once accepted |
| Foundation cross-refs | Part 2 (signal ingestion produces input); Part 3 (KB consumes upon promotion); Part 6 (gate for promotion to Lock) |

### 4.5 Type 07 — `direction-card`

| Field | Default value |
|---|---|
| Hierarchy role | child of Type 05 North Star; parent of Type 10 Bet Pitches |
| Parent dependency | Type 05 North Star (Direction inherits gravity); Type 03 Locks (Direction respects) |
| Cadence | quarterly review for activation/deferral; event-driven status changes in-quarter |
| Owner | T0 defines + activates/deactivates; T1/T2 mini-swarm operates within active Direction; T3 mentor consults at quarterly review |
| Trigger | quarterly review / Phase transition / Strategic Insight crystallization (Type 06 → Type 07) |
| Audience | T0/T1/T2 internal-primary + T3 mentor at quarterly review |
| F default | F3 (active hypothesis) → F4 once cycle-validated |
| Foundation cross-refs | Part 4 (role taxonomy — Direction has dedicated executor binding); Part 7 (project lifecycle runs inside Direction); Part 9 (quarterly review surfaces Direction status) |

### 4.6 Type 10 — `bet-pitch`

| Field | Default value |
|---|---|
| Hierarchy role | child of Type 07 Direction; parent of Type 11 Project Brief (Foundation Layer) |
| Parent dependency | Type 07 Direction Card (Bet shaped inside active Direction) |
| Cadence | per-cycle (Singer 6-week + 2-week cooldown) |
| Owner | T0 shaping + T2 drafting-support; betting-table ritual T0-only |
| Trigger | cycle boundary / unshaped idea reaching shape-readiness / capacity available |
| Audience | T0/T1/T2 internal-only |
| F default | F2 (shaped pitch) → archived at cycle-close (kept for evidence) |
| Foundation cross-refs | Part 7 (Project Lifecycle — Bet → Project); Part 5 (Compound Learning — cycle compound captures learnings) |

### 4.7 Type 14 — `mentor-brief`

| Field | Default value |
|---|---|
| Hierarchy role | standalone synthesizer; reads-from Types 03, 04, 05, 07, 10 + current Phase status |
| Parent dependency | none specifically; reads-from many |
| Cadence | event-driven (per mentor call); per-mentor cadence (weekly / monthly / quarterly) |
| Owner | T0 + T2 drafting + T2 sanitization-check; T0 ack incl. sanitization ack |
| Trigger | mentor call scheduled / quarterly mentor check-in |
| Audience | T3 inner stakeholder (mentor) — sanitized version |
| F default | F2 (snapshot-of-state) |
| Foundation cross-refs | Part 9 (owner interaction); Part 10 (external touchpoints); Part 6 (governance — sanitization gate) |

---

## §5 Honest declarations

### 5.1 Cadence-flexibility flag

Cadence declarations are **defaults**. Specific instances may deviate:
- A Strategic Insight that lands in the middle of a Phase transition might land
  as a Lock candidate the same week (event-driven path is short).
- A Direction Card might have a special-trigger review mid-quarter (e.g., M&A
  Direction shifts from `deferred-phase-2-plus` if Mittelstand succession opportunity
  surfaces concretely). Templates encode defaults; Ruslan overrides per-instance.

### 5.2 5-tier model abstraction concern

The 5-tier model (T0-T4) was articulated in FUNDAMENTAL §7.4 as a *generic* access
model. Phase 1 of Jetix is solo — only T0 (Ruslan) + T1/T2 agents + T3 (1-3 mentors) +
no T4 yet. Owner matrix above uses all 5 tiers proactively for Phase B+ readiness.
If Ruslan prefers Phase-1-realistic compression to T0 + agent-tier + mentor-tier,
templates can collapse — declare in walkthrough.

### 5.3 Foundation-cross-reference precision

Cross-references to Foundation Parts (Part 1-10) are at *part-level granularity*. The
Wave B manifest §2 matrix gives part-by-framework precision; Phase 3 of this scope
does not refine to interface-card level. Phase 4 templates can either inherit
part-level refs (sufficient for Strategic Layer scope) or hand off to Wave C interface
cards if implementation requires.

### 5.4 Dependency-graph edge-typing

The 7 edge-labels used (`overlays / positions / informs / pulls / contains-shaped-bets
/ instantiates / candidate-promotion / synthesizes-from`) are *Strategic-Layer-internal
vocabulary*; they are *not* canonical FPF A.14 edges. Phase 4 templates can either:
(a) keep these informal edge labels, OR (b) tighten to FPF-canonical (ComponentOf,
ConstituentOf, etc.) per Levenchuk consultant card §4 P4 — but the FPF-canonical set
is not a clean fit for these strategic-doc relations. Recommendation: keep informal
labels; document the deviation in `_index.md` manifest.

### 5.5 Type 11 Project Brief Foundation-ref

Type 11 (Project Brief) appears in §1 graph as the downstream of Type 10 Bet Pitch.
Type 11 is **Foundation Layer**, not Strategic Layer — its template lives in
`swarm/wiki/_templates/project-{type}/`. Strategic Layer Phase 4 includes a *reference*
to Type 11 from Bet Pitch template (as cross-layer dependency declaration), not a
Type 11 template itself.

---

## §6 Output handover to Phase 4

Phase 4 receives §4 per-type field declarations + §1 dependency graph + §2 cadence
calendar + §3 owner matrix and produces:

- 7 `decisions/strategic/_templates/<type-slug>.md.template` files
- 1 `decisions/strategic/_index.md` manifest

**Templates structure (per brief §2 Phase 4):**
- Frontmatter complete (per §4 declarations above)
- 4-8 sections (not too sparse, not too verbose)
- Each section 1-2 sentence example fragment (NOT content — illustrative only)
- Anti-scope explicit
- F-G-R defaults
- Cross-references to Foundation parts where applicable

**Manifest structure (`_index.md`):**
- Catalogue list of 7 templates (PROPOSE)
- 4 SKIP/DEFER types with rationale-pointer to Phase 2 doc
- Dependency graph reproduced
- Cadence calendar reproduced
- Owner matrix reproduced
- Governance protocol for Type 01 (FUNDAMENTAL — already LOCKED) and Type 02 (FPF — upstream-tracked) — these are referenced rather than templated.

---

## §7 Provenance + commits

- All hierarchy claims traceable to Phase 1 §3.1 sketch + Phase 2 §3 rationale.
- Cadence claims traceable to consultant cards (Singer Shape Up 6+2w, Doerr
  quarterly OKR but DEFER'd, FUNDAMENTAL §8.6 semi-annual+ vertical evolution).
- Owner-matrix claims traceable to FUNDAMENTAL §7.4 5-tier model + memory
  `feedback_ai_does_not_strategize` (sole-strategist preserved across all
  Author/Approver cells).
- Word count: ~2.5K (target 1-2K — slightly over due to honest-declaration §5;
  acceptable).
- F2.

---

*End of Phase 3 hierarchy + cadences.*
