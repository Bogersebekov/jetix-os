---
title: FUNDAMENTAL Vision Hierarchy Decision (Bundle 5 — Pillar A)
date: 2026-04-28
type: decision-artefact
status: AWAITING-APPROVAL
parent_cycle: cyc-foundation-build-2026-04-28
bundle: 5-strategic-layer
phase: A-3 Joint Design synthesis
F: F4
G: brigadier Bundle 5 Pillar A hierarchy decision; gates Part 11 architecture drafting
R: R-medium — pending Ruslan ack
---

# §0 Mission

FUNDAMENTAL Vision LOCKED v1.0 (`decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`)
is currently the canonical Foundation Vision document. Pillar A (Main Strategic
Documents) introduces strategic-direction artefact types that may overlap with
FUNDAMENTAL. This document declares the canonical hierarchy.

# §1 Options

| Option | Description | Verdict |
|---|---|---|
| 1 | FUNDAMENTAL = Pillar A canonical artefact (no new docs; Pillar A is "place where FUNDAMENTAL lives" + supplementary memos) | Reject |
| 2 | FUNDAMENTAL = constitutional CONTAINER; Pillar A introduces SUBORDINATE strategic-direction docs that elaborate FUNDAMENTAL into actionable direction | **ADOPT** |
| 3 | FUNDAMENTAL = constitutional/architectural; Pillar A = fully separate strategic direction docs (parallel hierarchies, no inheritance) | Reject |

# §2 Adopted rationale (Option 2)

## §2.1 Genre distinction

**FUNDAMENTAL Vision genre** = constitutional / architectural / "what the system
IS and DOES at first principles". Vacuum-sealed, sector-agnostic. Answers «what
must any Jetix instance be capable of?»

**Pillar A genre** = strategic direction / "where the owner is going". Owner-specific
focus, time-bound (annual / quarterly / event-driven), supersedable. Answers
«what is THIS owner / instance pursuing right now?»

Different genres → can't merge (Option 1 fails). Different abstraction layers →
can't be parallel without contradiction risk (Option 3 fails). Subordinate
elaboration → coherent (Option 2).

## §2.2 Hierarchy (canonical)

```
                 FUNDAMENTAL Vision (constitutional baseline — sector-agnostic)
                                  │
                                  │ elaborates-into
                                  ▼
                  ┌───────────────────────────────────┐
                  │   PILLAR A STRATEGIC DIRECTION    │
                  │   (owner-specific, time-bound)    │
                  │                                   │
                  │   ┌──────────────────────┐        │
                  │   │ Phase Plan           │        │
                  │   │ (multi-phase horizon)│        │
                  │   └──────────────────────┘        │
                  │              │                    │
                  │              ▼                    │
                  │   ┌──────────────────────┐        │
                  │   │ North Star / DoT     │        │
                  │   │ (annual + quarterly) │        │
                  │   └──────────────────────┘        │
                  │              │                    │
                  │              ▼                    │
                  │   ┌──────────────────────┐        │
                  │   │ Direction Card       │        │
                  │   │ (standing direction) │        │
                  │   └──────────────────────┘        │
                  │       │            │              │
                  │       ▼            ▼              │
                  │  ┌────────┐  ┌────────────────┐   │
                  │  │ Insight│  │ Lock Entry     │   │
                  │  │ Memo   │  │ (governance)   │   │
                  │  └────────┘  └────────────────┘   │
                  │                                   │
                  │   ┌──────────────────────┐        │
                  │   │ Strategic Reflection │        │
                  │   │ (annual / quarterly  │        │
                  │   │  retrospective)      │        │
                  │   └──────────────────────┘        │
                  └───────────────┬───────────────────┘
                                  │ instantiates
                                  ▼
                       ┌──────────────────────┐
                       │ PILLAR B PROJECT     │
                       │ STRATEGY             │
                       │ (project-scoped)     │
                       └──────────────────────┘
```

## §2.3 Inheritance rules

**1. Pillar A docs do NOT modify FUNDAMENTAL.** FUNDAMENTAL is constitutional;
modification = constitutional revision (stop_gate per Part 6b §I.4 F8).

**2. Pillar A docs cite FUNDAMENTAL as upstream context.** Frontmatter pattern:
```yaml
constitutional_anchors:
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (LOCKED v1.0)
  - design/JETIX-FPF.md (Constitutional Spec)
elaborates_uc:
  - UC-A.1 (multi-level strategic doc hosting)
  - UC-A.3 (alignment enforcement)
```

**3. FUNDAMENTAL revision propagates DOWNWARD.** If FUNDAMENTAL §X changes (per
Ruslan note 28.04 evening «они как бы окей они есть, но мы их потом еще раз
будем перерабатывать»), Pillar A docs that anchor §X enter `under-review` state.
Owner ack required before re-LOCK.

**4. Pillar A doc supersession does NOT touch FUNDAMENTAL.** New North Star
supersedes old North Star via `supersedes: <prior-path>` ref; FUNDAMENTAL
unchanged.

## §2.4 Phase 1 special case — FUNDAMENTAL is "provisional canonical"

Per Ruslan 28.04 evening: «FUNDAMENTAL они как бы окей они есть, но мы их потом
еще раз будем перерабатывать».

**Implication for Pillar A:**
- Pillar A architecture cites FUNDAMENTAL as upstream baseline
- Pillar A does NOT depend on FUNDAMENTAL §X being immutable forever
- If FUNDAMENTAL §X is revised in Layer 2 phase, Pillar A docs anchoring §X enter under-review
- Pillar A docs that DO NOT anchor specific FUNDAMENTAL sections (most direction-content) survive FUNDAMENTAL revision unchanged

**This is preferable to Options 1 / 3:**
- Option 1 (FUNDAMENTAL = Pillar A canonical) would force Pillar A to inherit FUNDAMENTAL's revision risk
- Option 3 (parallel) would silence FUNDAMENTAL revisions from informing strategic direction — wrong direction-of-arrows

## §2.5 What FUNDAMENTAL is NOT (anti-conflation)

FUNDAMENTAL Vision is NOT:
- A North Star (FUNDAMENTAL is sector-agnostic; North Star is owner-specific direction)
- A Direction Card (FUNDAMENTAL is constitutional architecture; Direction Card is standing focus)
- A Phase Plan (FUNDAMENTAL is timeless; Phase Plan is time-bound)
- A Strategic Insight Memo (FUNDAMENTAL is canonical baseline; Insight Memo is event-driven thinking artefact)

These are 4 distinct Pillar A doc types each filling a Pillar A slot that
FUNDAMENTAL does not occupy.

## §2.6 What Pillar A is NOT (anti-conflation)

Pillar A is NOT:
- A re-write of FUNDAMENTAL Vision
- A FPF supplement (FPF is `design/JETIX-FPF.md`; constitutional spec)
- A constitutional revision authority
- A locks-ledger replacement (Lock Entry within Pillar A is the locks-ledger format)

# §3 FPF relationship

`design/JETIX-FPF.md` (3758 lines) is the **constitutional spec** — methodology /
discipline / pattern library. Distinct from FUNDAMENTAL Vision (which is
use-case + capability surface).

Pillar A doc relationship to FPF:
- Pillar A docs cite FPF anchors in frontmatter `fpf_anchors:` field
- Pillar A docs do not modify FPF
- FPF supersession follows FPF-Steward governance (per FUNDAMENTAL §8.6 vertical-axis revision)

# §4 Decisions DB consumption (UC-A.4)

FUNDAMENTAL §1 UC-A.4 introduces Decisions tracking & recall. This use case is
**multi-Pillar consumer**:

- Pillar A artefacts (Lock Entry, Strategic Insight, Direction Card, etc.) are themselves first-class decisions tracked per UC-A.4
- Pillar B project strategy decisions tracked per UC-A.4
- Pillar C principle-supersession events tracked per UC-A.4

UC-A.4 implementation MAY land in Part 11 (Pillar A) OR be its own sub-system.
Bundle 5 recommendation: **decisions DB is Part 11 component** — strategic and
governance decisions concentrate in Part 11; project-level decisions index via
Part 7 cross-references.

This decision deferred to Part 11 architecture §I (decisions DB schema) — not
finalized at Joint Design layer.

# §5 Open questions

| Q | Question |
|---|---|
| OQ-V1 | FUNDAMENTAL revision in Layer 2 phase — does revision invalidate Pillar A docs anchoring §X, or do Pillar A docs survive with updated anchor? Recommend: under-review state + owner ack |
| OQ-V2 | Decisions DB (UC-A.4) placement in Part 11 vs separate sub-system. Recommend: Part 11 component, evaluate at Part 11 architecture §I |
| OQ-V3 | FPF supersession — should FPF revision trigger Pillar A re-review (analogous to FUNDAMENTAL)? Recommend: yes, FPF-Steward emits supersession event |

# §6 Provenance

- FUNDAMENTAL Vision §0 two-layer pattern (Layer 1 FUNDAMENTAL + Layer 2 RUSLAN-LAYER) [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§0]
- FUNDAMENTAL §1 Categoria A (UC-A.1, A.2, A.3, A.4): Pillar A use cases [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§1]
- FUNDAMENTAL §6.2 founder-agency [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.2]
- Ruslan note 28.04 evening provisional-canonical FUNDAMENTAL
- Bundle 1 supplement 1+2 pattern: retroactive constitutional revision via stop_gate

---

*End of FUNDAMENTAL Vision hierarchy decision. Pillar A architecture (Part 11) consumes this as input.*
