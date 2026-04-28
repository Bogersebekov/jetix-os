---
title: Strategic Layer Structural Placement Decision (Bundle 5 Joint Design)
date: 2026-04-28
type: decision-artefact
status: AWAITING-APPROVAL
parent_cycle: cyc-foundation-build-2026-04-28
bundle: 5-strategic-layer
phase: A-3 Joint Design synthesis
F: F4
G: brigadier Bundle 5 Joint Design output; gates Pillar A/B/C architecture drafting
R: R-medium — pending Ruslan ack at AWAITING-APPROVAL packet review
---

# §0 Mission

Joint Design synthesis (Phase A-3) for Strategic Layer Foundation Bundle 5. Three
Pillars (A Main Direction / B Project Strategy / C Principles two-tier) require
coherent structural placement within Foundation Architecture (10 LOCKED parts).

This document declares the canonical placement decisions + cross-Pillar coherence
contract. Per F8 schemas, Foundation parts are the system's typed surface area;
adding Strategic Layer mandates either extension to existing parts OR a new part.

Pillar-specific decision artefacts:
- `fundamental-vision-hierarchy-decision.md` — Pillar A relationship to FUNDAMENTAL Vision LOCKED v1.0
- `claude-md-reframing-decision.md` — Pillar C re-framing of CLAUDE.md

# §1 Decision summary

| Pillar | Decision | New surface area |
|---|---|---|
| **Pillar A — Main Strategic Documents** | **NEW Foundation Part 11 — Strategic Direction Substrate** | `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` (canonical) + `decisions/strategic/` (artefact home) |
| **Pillar B — Project-Level Strategy Slots** | **EXTENSION to Part 7 — Project Lifecycle Substrate** | `projects/<slug>/strategy.md` artefact slot at `scoped → staged` transition; Part 7 architecture supplement (retroactive) |
| **Pillar C — Principles Two-Tier** | **STANDALONE Foundation sub-system — Principles Substrate** with internal two-tier structure (Tier 1 manager + Tier 2 system) | `principles/` directory (Foundation canonical) + `swarm/wiki/foundations/principles/architecture.md` (sub-system architecture, NOT a numbered Part — see §3) |

# §2 Pillar A — NEW Part 11

## §2.1 Options analyzed

| Option | Description | Verdict |
|---|---|---|
| A.1 | NEW Foundation Part 11 — Strategic Direction Substrate | **ADOPT** |
| A.2 | Extension to Part 9 (Owner Interaction Scaffold) | Reject — Part 9 §F anti-scope §481-488 explicitly defers UC-A.1/A.2 strategic doc HOSTING |
| A.3 | Extension to Part 7 (treat "system direction" as root project) | Reject — system-direction blast radius ≠ project blast radius; conflates ownership |
| A.4 | Cross-cutting concern (woven through Parts 5/7/9) | Reject — diffuses ownership, breaks F-G-R authority, violates Wave A dependency-graph clarity |

## §2.2 Adopted rationale

**1. FUNDAMENTAL §1 Categoria A is its own LAYER.** UC-A.1 (multi-level strategic
document hosting), UC-A.2 (creation assistance), UC-A.3 (alignment enforcement),
UC-A.4 (decisions tracking & recall) — these are 4 use cases with system-scope
blast radius. None map to existing 10 parts:
- Part 7 = project-scope (per project, not system)
- Part 9 = owner interaction surface (defers strategic doc hosting per §F anti-scope)
- Part 5 = compound learning (consumes from Pillar A but does not host strategic docs)
- Part 6a/6b = provenance/gate (enforce on Pillar A artefacts but do not host)

**2. Part 9 explicitly defers.** Architecture line 481-488: «Part 9 does NOT define
strategic document content (UC-A.2 strategic document...)». This is a structural
gap that Pillar A fills.

**3. Separation of concerns.** Pillar B fits naturally as Part 7 extension
(project strategy = project artefact). If Pillar A also lived in Part 7, the part
would conflate system-scope and project-scope artefacts — violates Part 7 §F
anti-scope «does NOT author strategic decisions».

**4. F-G-R authority clarity.** Part 11 owns: F4-F8 strategic-doc artefacts,
G:Pillar-A-canonical, R:owner-only-ack-required. Distinct from Part 7 G:per-project-lifecycle.

**5. Wave A dependency-graph fit.** Strategic Direction Substrate is a clear
producer node (emits strategic docs consumed by Parts 4/5/7/9) and consumer node
(consumes from Part 5 compound-learning + Part 9 owner-direction-input). Adding
Part 11 fills a clean dependency-graph node.

**6. Fork-portability.** A fork-importer creating Jetix instance for medical
research / e-commerce / scientific lab needs a "strategic direction" place that
isn't conflated with project-lifecycle. Part 11 is the universal slot.

## §2.3 Part 11 scope

- Hosts: 6 Foundation-level strategic-doc types from Phase 1 disposition (Lock Entry, North Star, Strategic Insight, Direction Card, Phase Plan, Strategic Reflection)
- Lifecycle: authoring, supersession (append-only), ack authority (owner-only per FUNDAMENTAL §6.2), cadence (event-driven + calendar-driven mix per type)
- Integration: produces strategic-doc-events consumed by Part 4 (role coordination), Part 5 (compound learning), Part 7 (project-strategy alignment check), Part 8 (strategic-alignment SLI), Part 9 (owner reflection surface)
- Foundation generic: structural placement + lifecycle + cadence + ack discipline + integration contracts
- RUSLAN-LAYER: actual strategic-doc content (Ruslan's Direction Cards, North Star, Insight memos)

# §3 Pillar B — EXTENSION to Part 7

## §3.1 Options analyzed

| Option | Description | Verdict |
|---|---|---|
| B.1 | Extension to Part 7 (Project Lifecycle Substrate) | **ADOPT** |
| B.2 | New sub-system | Reject — fragments project-artefact ownership |

## §3.2 Adopted rationale

**1. Project strategy IS a project artefact.** It belongs alongside `brief.md`,
`scope-record.jsonl`, `retrospective.md` in `projects/<slug>/`. Part 7 already owns
this directory.

**2. Lifecycle alignment.** Part 7 state machine: `scoped → staged → activated →
under-review → closed | archived`. Project strategy is authored at `scoped → staged`
gate (when project commits to direction) and reviewed at every subsequent stage
gate. Natural fit.

**3. Sub-projects inherit by reference.** Per FUNDAMENTAL UC-A.1 hierarchical pattern
(System → Strategic → Annual → Quarterly → Project → Sub-project), sub-projects
reference parent project's strategy via frontmatter `inherits_strategy_from:
<parent-slug>`. Stays in Part 7's existing schema discipline.

**4. Pillar A consumption.** Project strategy alignment-check fires when project
brief references a Pillar A Direction Card; alignment logged via Part 7 `under-review`
gate. Cross-Pillar coherence preserved without new sub-system.

**5. Bet Pitch absorption.** Phase 1 Type 10 Bet Pitch (Singer Shape Up appetite
+ circuit-breaker) lands here as Pillar B canonical pattern. Bet Pitch = project
strategy variant for `bets` project type per `.claude/config/project-types.yaml`.

## §3.3 Pillar B as Part 7 supplement

Part 7 Bundle 4 architecture is LOCKED. Pillar B extension is a **retroactive
constitutional supplement** analogous to OQ-B2-A pattern (Bundle 1 supplement 1+2):

- Adds §A.4 input row: project strategy artefact at scoped→staged
- Adds §B.4 output row: project-strategy-event published to Part 11 alignment check
- Adds §I.4 schema fragment: `projects/<slug>/strategy.md` frontmatter schema (4 mandatory sections per §3.4 below)
- Adds §X.X clause: project strategy structure is Foundation generic; content RUSLAN-LAYER

Part 7 architecture document is NOT rewritten. The supplement is appended via a
Bundle 5 supplement file: `swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md`.

## §3.4 Project strategy mandatory sections (Foundation generic)

Per Foundation discipline, every project strategy answers these 4 questions:

| § | Question | Source framework |
|---|---|---|
| §1 What outcome | What state of the world does this project produce by close? Hamel-binary acceptance predicate | Part 7 §I.1 stage-gate predicates discipline |
| §2 What appetite | Time + attention + capital appetite. Singer Shape Up: appetite-as-CONSTRAINT not estimate | Cagan Shape Up consultant card §4 P1 |
| §3 Pillar A linkage | Which Pillar A Direction Card / North Star / Phase Plan does this serve? Path reference | FUNDAMENTAL UC-A.3 alignment enforcement |
| §4 Circuit breakers | What conditions trigger early kill / re-shape / pause? | Singer Shape Up + Munger inversion |

Foundation-generic structure. Per-instance content (e.g., specific outcomes, specific
appetite weeks, specific Direction Card refs) = RUSLAN-LAYER per project.

# §4 Pillar C — STANDALONE Foundation sub-system

## §4.1 Options analyzed

| Option | Description | Verdict |
|---|---|---|
| C.1 | Extension to Part 6b (already houses constitutional_never_list) | Reject — Part 6b is enforcement-side; conflating authoring + enforcement violates anti-scope |
| C.2 | Standalone Foundation sub-system referenced by Part 6b + Part 9 + CLAUDE.md, with internal two-tier structure | **ADOPT** |
| C.3 | Two separate sub-systems (Tier 1 + Tier 2) | Reject — splits coherent thing; consumers want one principle source |

## §4.2 Adopted rationale

**1. Authoring vs enforcement separation.** Part 6b §F anti-scope «Part 6b does
not author principles — it enforces them via Default-Deny + Halt-Log-Alert».
Conflating authoring violates Bundle 1 RUSLAN-ACK clarity contract.

**2. Tier 1 doesn't belong in Part 6b.** Tier 1 (manager principles like «развитие
общества», «честность», «long-term thinking») is owner-values, not gate-enforcement.
Part 6b architecture is gate-mechanic; absorbing Tier 1 violates §H deep-module
discipline.

**3. Two-tier internal cohesion.** Splitting Tier 1 (C.3) into separate sub-systems
fragments principle authority. Consumers need one place to look up «what does this
system value». Cross-Pillar contracts simpler with one principles substrate.

**4. Tier 2 enforcement contract.** Part 6b §I.2 `constitutional_never_list:` 11
entries become **derived** from Pillar C Tier 2 master list. Pillar C is upstream
producer; Part 6b stays downstream enforcement. Lint check: `count(Tier-2 hard rules
in Pillar C) == count(constitutional_never_list entries in Part 6b)`.

**5. Sub-system, not numbered Part.** Per Wave A 10-part decomposition, Part numbering
captures domain-distinct concerns at peer level. Pillar C Principles Substrate is
**cross-cutting subordinate** to Foundation Architecture: it's CONSUMED by 5+ parts
(6a, 6b, 7, 9, 11) and CLAUDE.md. Numbering it as Part 12 would imply peer-status
with Parts 1-11. Sub-system status is more honest.

(Alternative naming: brigadier may propose «Foundation Annex P-Principles» if
Ruslan prefers numbered surface area.)

**6. CLAUDE.md re-framing.** Per Ruslan «принципы это такой как бы мега CLAUDE.md
для всей системы», Pillar C absorbs the principles content currently scattered
in CLAUDE.md. CLAUDE.md re-framing per `claude-md-reframing-decision.md`: HYBRID
split — operational config stays in CLAUDE.md, Pillar C principles canonical, with
critical Tier-2 inlined for boot context.

## §4.3 Pillar C internal two-tier structure

```
principles/
├── _index.md                          # MOC for both tiers
├── tier-1-manager/
│   ├── _index.md                      # Tier 1 catalogue (RUSLAN-LAYER content per fork)
│   ├── _template.md                   # Foundation-generic structural template
│   └── <slug>.md per principle        # RUSLAN-LAYER content; example: long-term-thinking.md
├── tier-2-system/
│   ├── _index.md                      # Tier 2 catalogue (Foundation-generic + RUSLAN-LAYER overrides)
│   ├── _template.md                   # Foundation-generic structural template
│   ├── foundation-generic/            # 11 Tier-2 hard rules (mirror of Part 6b constitutional_never_list)
│   │   └── <slug>.md per rule         # e.g., ai-does-not-strategize.md
│   └── ruslan-layer-overrides/        # RUSLAN-LAYER instance-specific Tier-2 rules
└── _governance.md                     # Authoring authority, supersession, audit cadence
```

**Tier 1 (manager / owner principles):**
- Foundation-generic: STRUCTURE + governance discipline (authoring authority = owner; supersession = append-only; audit cadence)
- RUSLAN-LAYER: actual values (e.g., «развитие общества», «честность», «long-term thinking», «не deciding для другого человека»)

**Tier 2 (AI / system / agent principles):**
- Foundation-generic: 11 hard rules from FUNDAMENTAL §6.1 (mirrored to Part 6b constitutional_never_list) + cross-rule structural pattern
- RUSLAN-LAYER overrides: instance-specific Tier-2 rules (e.g., «no API key exposure» specific to keys Ruslan uses; «Russian for content» specific to Ruslan's lang preference)

# §5 Cross-Pillar coherence contract

## §5.1 How Pillar A informs Pillar B

- Project strategy (Pillar B) §3 Pillar A linkage = mandatory frontmatter ref to Direction Card or Phase Plan
- Part 7 stage-gate ack at `staged → activated` runs Pillar A alignment-check predicate: if no Pillar A ref OR ref points to superseded artefact → escalate to owner
- Pillar A North Star supersession event triggers **all active project strategies under review** (Part 7 emits scope-change-request for each `activated` project; owner ack required)

## §5.2 How Pillar A informs Pillar C

- Pillar A Direction Cards may reference Tier 1 principles (e.g., «this Direction is grounded in Tier 1 principle: long-term thinking»)
- Pillar A Lock Entry promotion may cite Tier 2 principle violation history (locks created BECAUSE tier-2 was violated → prevention rule)
- Pillar C principles do NOT auto-supersede when Pillar A docs change; principles change is constitutional event (stop_gate per Part 6b §I.4 LOCKED)

## §5.3 How Pillar C constrains Pillar A + B

- Every Pillar A artefact (North Star, Direction Card, etc.) carries frontmatter `principles_compliance:` field listing Tier 1 + Tier 2 principles asserted
- Every Pillar B project strategy carries same field
- Part 6b enforces Tier 2 derived constitutional_never_list at gate time; if Pillar A or B artefact violates Tier 2 → halt_log_alert
- Tier 1 violation surfaces at Pillar A authoring time (owner self-ack); not gate-enforced (owner authority)

## §5.4 Foundation vs RUSLAN-LAYER strict per Pillar

| Pillar | Foundation generic | RUSLAN-LAYER |
|---|---|---|
| A | Part 11 architecture, 6 strategic-doc types structure, lifecycle, cadence, ack discipline, FUNDAMENTAL hierarchy | Actual content of strategic docs (Ruslan's Direction Cards, North Star, etc.) |
| B | `projects/<slug>/strategy.md` 4-section structure, Part 7 state-machine integration, Pillar A linkage rule, circuit-breaker discipline | Actual project strategies for 8 active projects |
| C | Two-tier structure, principle-doc template, governance discipline, Part 6b consumption contract, CLAUDE.md re-framing structure | Actual Tier 1 + Tier 2 content (Ruslan's values, instance-specific Tier 2) |

# §6 Output paths

| Pillar | Architecture | Templates | Schemas |
|---|---|---|---|
| A | `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` | (decisions/strategic/_templates/ retained as exemplar archive; canonical inside Part 11 §I) | `shared/schemas/strategic-direction-doc.json` |
| B | `swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md` (supplement to LOCKED Part 7) | Inline §I of supplement | `shared/schemas/project-strategy.json` |
| C | `swarm/wiki/foundations/principles/architecture.md` (sub-system, not numbered Part) | `principles/_template.md` (Foundation-generic, both tiers) + sub-templates in tier-1-manager/ and tier-2-system/ | `shared/schemas/principle-doc.json` |

# §7 Open questions raised

| Q | Question |
|---|---|
| OQ-S1 | Pillar A as NEW Part 11 — confirm numbered surface vs sub-system status. Recommend: numbered Part 11 (peer-status with Parts 1-10) |
| OQ-S2 | Pillar C as sub-system vs Annex P-Principles vs Part 12. Recommend: sub-system (cross-cutting subordinate) |
| OQ-S3 | Part 7 Bundle 5 supplement — supersedes Part 7 architecture as F8 LOCKED, or stays as Pillar B annex? Recommend: supplement (analogous to Bundle 1 supplement pattern) |
| OQ-S4 | Should `decisions/strategic/` directory move under `swarm/wiki/foundations/part-11-...`? Recommend: keep `decisions/strategic/` for owner-facing docs (per Part 9 surface conventions); Part 11 references decisions/strategic/ as artefact home |
| OQ-S5 | RUSLAN-LAYER overrides directory naming — `ruslan-layer-overrides/` per Phase A vs `instance-specific/` per fork-portable. Recommend: `ruslan-layer-overrides/` symbolic; fork-importer renames per Phase B |

# §8 Provenance

- FUNDAMENTAL Vision LOCKED v1.0 §1 Categoria A (UC-A.1 / A.2 / A.3 / A.4): Pillar A use cases
- FUNDAMENTAL Vision LOCKED v1.0 §6.1: Pillar C Tier 2 constitutional 11 hard rules
- Part 7 architecture §F anti-scope (line 428-430): Part 7 does NOT author strategic decisions
- Part 9 architecture §F anti-scope (line 481-488): Part 9 does NOT define strategic document content
- Part 6b architecture §I.2 (line 997-1054): constitutional_never_list 11-entry enum (Pillar C Tier 2 derived enforcement)
- Part 6b architecture §F anti-scope: Part 6b enforces, does not author
- Wave A dependency-graph: Strategic Direction Substrate as new producer/consumer node
- Phase 1 baseline disposition: 6 ADOPT-INTO-PILLAR-A + 1 ADOPT-INTO-PILLAR-B confirmed
- Bundle 1 supplement 1+2 pattern: retroactive constitutional supplement methodology

---

*End of structural placement decision. Pillar A/B/C architectures consume this decision as input.*
