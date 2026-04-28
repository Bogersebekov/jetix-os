---
title: "Strategic Layer — Manifest (Etap 2 of Генеральная чистка)"
date: 2026-04-28
type: strategic-layer-manifest
status: AWAITING-APPROVAL
F: F2
G: "Strategic Layer scoping output for Etap 2; manifest of 7 PROPOSE templates + governance refs for SKIP/DEFER types. Subject to Ruslan ack before content writing begins (next sprint with 5-chat methodology per inferred memory)."
R: R-medium
last_updated: 2026-04-28
research_phases:
  phase_1_landscape: decisions/strategic/_research/landscape-strategic-docs-2026-04-28.md
  phase_2_filtering: decisions/strategic/_research/jetix-fit-filtering-2026-04-28.md
  phase_3_hierarchy: decisions/strategic/_research/hierarchy-cadences-2026-04-28.md
  phase_4_templates: decisions/strategic/_templates/ (this manifest enumerates)
  phase_5_awaiting_approval: decisions/AWAITING-APPROVAL-strategic-layer-templates-2026-04-28.md
---

# Strategic Layer — Manifest

## §0 Purpose

This manifest catalogues the 7 PROPOSE structural templates produced in Phase 4 of
the Strategic Layer scoping work (Etap 2 of Генеральная чистка), plus governance
references for the 4 SKIP types (already covered) and 4 DEFER types (premature for
Phase 1 — reactivate at Phase B+ trigger). Templates are STRUCTURAL only — content
authoring is the next sprint with 5-chat multi-session methodology per inferred memory
`methodology_multi_chat_review_for_critical_docs`.

---

## §1 Templates (7 PROPOSE)

| # | Type | Slug | Template path | Cadence | Owner |
|---|---|---|---|---|---|
| 1 | Locks Ledger Entry | `lock-entry` | `decisions/strategic/_templates/lock-entry.md.template` | append-only; event-driven | ruslan-plus-agent |
| 2 | Founder Overlay (RUSLAN-LAYER) | `founder-overlay` | `decisions/strategic/_templates/founder-overlay.md.template` | annual baseline + event-driven amendments | ruslan-plus-agent |
| 3 | North Star / DoT | `north-star` | `decisions/strategic/_templates/north-star.md.template` | annual major review + quarterly soft updates; major rewrite at Phase transitions | ruslan-only (multi-chat methodology) |
| 4 | Strategic Insight Memo | `strategic-insight` | `decisions/strategic/_templates/strategic-insight.md.template` | event-driven | ruslan-plus-agent |
| 5 | Direction / Pillar Card | `direction-card` | `decisions/strategic/_templates/direction-card.md.template` | quarterly review for activation/deferral; event-driven status changes | ruslan-plus-agent |
| 6 | Bet Pitch / Shape-Up Pitch | `bet-pitch` | `decisions/strategic/_templates/bet-pitch.md.template` | per-cycle (6w + 2w cooldown by default) | ruslan-plus-agent (T0-only betting) |
| 7 | Mentor / Stakeholder Briefing Pack | `mentor-brief` | `decisions/strategic/_templates/mentor-brief.md.template` | event-driven (per call) | ruslan-plus-agent (sanitization-check mandatory) |

---

## §2 Dependency graph (reproduced from Phase 3)

```
Type 01 Foundation Vision (LOCKED v1.0; managed in §4 below)
   ▼ overlays
Type 04 Founder Overlay (RUSLAN-LAYER)
   ├─ positions ──▶ Type 05 North Star / DoT
   │                    ▼ pulls
   │                Type 07 Direction / Pillar Card
   │                    ▼ contains-shaped-bets
   │                Type 10 Bet Pitch / Shape-Up
   │                    ▼ instantiates
   │                Type 11 Project Brief (Foundation Layer; not Strategic)
   │
   └─ informs ───▶ Type 03 Locks Ledger Entry
                          ▲ candidate-promotion
                          │
                  Type 06 Strategic Insight Memo
                          │ candidate-promotion
                          └────▶ Type 07 Direction / Pillar Card

Type 14 Mentor Brief — synthesizes-from Types 03, 04, 05, 07, 10 (sanitization gate)
```

---

## §3 Cadence calendar (reproduced from Phase 3)

| Type | Annual | Quarterly | Event-driven | Append-only |
|---|:-:|:-:|:-:|:-:|
| 03 lock-entry | — | review-coherence | ✓ creation | ✓ |
| 04 founder-overlay | ✓ baseline | review | ✓ Phase-transition | — |
| 05 north-star | ✓ major-review | ✓ soft-update | ✓ Phase-transition | — |
| 06 strategic-insight | — | — | ✓ creation | — |
| 07 direction-card | — | ✓ activation/deferral | ✓ status-change | — |
| 10 bet-pitch | — | — | ✓ per-cycle (6w+2w) | — |
| 14 mentor-brief | — | — | ✓ per-call | — |

---

## §4 SKIP types — governance references (no template; pointer-only)

These types were Phase-2-filtered as **SKIP** because adequate canonical artifacts
already exist. The Strategic Layer references them; does not recreate.

### SKIP-1 — Type 01 Foundation Vision

- **Canonical artifact:** `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0)
- **Governance protocol:** Vertical-axis revision per FUNDAMENTAL §8.6 — semi-annual+ review with architectural-review gate. Triggers (per FUNDAMENTAL §4.7): pattern accumulation, best-practice discovery, architecture stress-test failure, community-push (D27). NOT triggered by: convenience, single frustration, competitive FOMO, без data.
- **Authority:** T0 (sole strategist) with mandatory architectural review.

### SKIP-2 — Type 02 Constitutional Specification (FPF)

- **Canonical artifact:** `design/JETIX-FPF.md` (3758 lines, 14 sections; IP-1..IP-8 + A.14 + B.3 + F.6 + 8 true alphas)
- **Upstream:** `raw/external/ailev-FPF/FPF-Spec.md` (62K lines, 300+ patterns) — `https://github.com/ailev/FPF`
- **Governance protocol:** Quarterly check against ailev/FPF for new patterns per Wave B manifest §1. Selective pull per D27 Fork-and-merge — never auto-sync. Internal Jetix-FPF stable; revisions tracked via line-level pattern IDs.
- **Authority:** T0 ack on any Jetix-FPF amendment; FPF-Steward function (IP-4) audits coherence quarterly.

### SKIP-3 — Type 11 Project Brief

- **Canonical artifact:** `swarm/wiki/_templates/project-{consulting,research,product,bets}/` (4 template trees, 9-stub files each per CLAUDE.md KM MVP section)
- **Foundation Layer location:** Part 7 (Project Lifecycle Substrate); Wave C interface card
- **Note:** PM consultant card §6 OQ-1 + OQ-2 flag *gaps* in existing templates (`appetite:` and `outcome:` fields missing) — these are **Foundation Layer Wave C materialization issues**, not Strategic Layer template scope. Strategic Layer Bet Pitch (Type 10) sits *upstream* of Project Brief; together they bridge the gap.

### SKIP-4 — Type 12 DRR / Compound Cycle Retrospective

- **Canonical artifact:** `agents/<expert>/strategies.md` per-agent files (operational per CE consultant card §3 Foundation Part Mapping)
- **Foundation Layer location:** Part 5 (Compound Learning & Methodology Capture); Wave C interface card
- **Format:** Append-only DRR (Decision/Reasoning/Result/Review) with `rule_slug`, `version`, `ratio: {hits, misses}`, `expected_evolution` per CE card P2.

---

## §5 DEFER types — Phase B+ reactivation predicates (no template; reactivation criteria)

These types were Phase-2-filtered as **DEFER Phase B+** because premature for current
Phase 1 €50K context. The Strategic Layer documents the reactivation criteria; does
not produce templates until reactivation triggers fire.

### DEFER-1 — Type 08 Phase Plan

- **Current substitute:** `decisions/JETIX-PLAN.md` serves Phase 1 adequately
- **Reactivation predicate:** Phase 1 → Phase 2 transition (€50K Q2 2026 gate reached). At that trigger, JETIX-PLAN.md will need rewrite or extension; template authoring becomes warranted then.

### DEFER-2 — Type 09 Quarterly Plan / OKRs

- **Current substitute:** Phase Plan (Type 08) + Bet Pitch (Type 10 — appetite + outcome) + North Star (Type 05) trajectory milestones cover the OKR function in solo-founder context
- **Reactivation predicate:** Team grows past N=1 (~Phase 2+). Doerr canonical OKR pattern was designed for team-coordination at Intel under Grove; solo-founder OKRs add ceremony without information.

### DEFER-3 — Type 13 Capital / Investment Memo

- **Current substitute:** Bet Pitch (appetite-as-time-capital declaration) + Phase Plan (budget + milestones) cover capital-allocation in solo-founder Phase 1
- **Reactivation predicate:** Phase 2+ when revenue/headcount/ad-spend create meaningful $-allocation decisions OR when a single allocation event >€20K warrants the discipline. Memory `feedback_no_solo_founder_downgrade` (substituted) preserves enterprise-baseline expectation by reactivating, not skipping.

### DEFER-4 — Type 15 Strategic Reflection / Writing-as-Thinking Note

- **Current substitute:** `daily-log/` infrastructure + Strategic Insight Memo (Type 06) for crystallized reflections
- **Reactivation predicate:** Pattern emerges where structured-reflection format would capture content that the current free-form approach cannot. Currently rejected on Criterion 2 (AI-augment fails per Levenchuk IP-7 anti-pattern: "если и сам текст пишет LLM — исчезает 'мышление письмом' как когнитивный процесс").

---

## §6 Anti-scope of this Strategic Layer

Mandatory boundary declaration. Per FUNDAMENTAL §6 anti-scope discipline applied to
the layer itself (not just to individual docs).

The Strategic Layer **DOES NOT**:
- Define implementation specs → Foundation Layer (Parts 1-10)
- Replace existing canonical artifacts (Types 01, 02, 11, 12) — references them
- Author content for any document — templates STRUCTURAL only; content is next sprint
- Conflate with Operational Layer (`crm/`, `daily-log/`, `inbox/`) — Strategic Layer is upstream
- Become a "all strategic docs go here" catch-all — only the 7 PROPOSE types in §1; SKIP/DEFER types stay where they are

---

## §7 Provenance + cycle

- **Cycle:** Strategic Layer scoping (Etap 2 of Генеральная чистка), 2026-04-28
- **Phases produced:**
  - Phase 1 landscape catalogue (15 types) — `decisions/strategic/_research/landscape-strategic-docs-2026-04-28.md`
  - Phase 2 filtering (7 PROPOSE + 8 SKIP/DEFER) — `decisions/strategic/_research/jetix-fit-filtering-2026-04-28.md`
  - Phase 3 hierarchy + cadences + owner matrix — `decisions/strategic/_research/hierarchy-cadences-2026-04-28.md`
  - Phase 4 7 templates + this manifest — `decisions/strategic/_templates/` + `decisions/strategic/_index.md`
  - Phase 5 AWAITING-APPROVAL packet — `decisions/AWAITING-APPROVAL-strategic-layer-templates-2026-04-28.md`
- **Author:** Cloud Code (server) — direct integrator-mode synthesis (no ROY brigadier dispatch per brief §0)
- **F:** F2 (single-author scoping; not peer-validated)
- **Honest limits:** Memory files declared in brief at Windows-client paths were substituted via inference from on-disk corpus; flag preserved through all Phase outputs.

---

## §8 STOP — awaiting Ruslan ack

Per brief §0 + §6: **STOP after AWAITING-APPROVAL packet. Ruslan ack required before
any Strategic Layer document content writing (next sprint).**

The next sprint will:
- Apply 5-chat multi-session methodology to North Star authoring
- Draft RUSLAN-LAYER (Founder Overlay) v1.0 baseline
- Create cohort-1 Direction Cards (Top Lists Partner Factory + Quick-Money AI Consulting)
- Author first round of Bet Pitches per active Direction
- Draft Mentor Brief v1.0 for Антон call (deferred 27.04 evening per brief §1)

These authoring tasks are next-sprint scope; no content authoring in the current
research-and-scoping cycle.

---

*End of manifest. STOP — Ruslan walkthrough required.*
