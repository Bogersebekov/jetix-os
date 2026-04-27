---
title: Cycle Artefact Register — prior swarm cycles methodology snapshots (Wave B-0)
date: 2026-04-27
phase: B-0
expert: mgmt-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
produced_by: mgmt-expert
type: artefact-register
sources:
  - {path: "swarm/wiki/log.md", range: "all 111 lines — chronological cycle inventory"}
  - {path: "agents/brigadier/strategies.md", range: "lines 1-100 — cycle-3..cycle-8 DRR entries"}
  - {path: "decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md", range: "§G.1 per-Part summary + patterns"}
  - {path: "decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md", range: "frontmatter + §0 TL;DR + §1.1-§1.4"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md", range: "frontmatter + §A.1"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md", range: "frontmatter"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partC-stage-gates-merged.md", range: "frontmatter"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md", range: "frontmatter"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partE-quick-money-levenchuk-bootstrap.md", range: "frontmatter + post_ack_revision"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partE-investor-critic-icp-kpi-realism.md", range: "frontmatter"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partE-engineering-optimizer-e2e-demo-deltas.md", range: "frontmatter"}
  - {path: "swarm/gates/AWAITING-APPROVAL-layer-7-business-trajectory-deep-dive-2026-04-25.md", range: "frontmatter + §1 table"}
  - {path: "swarm/gates/AWAITING-APPROVAL-producer-services-strategy-options-2026-04-25-ack.md", range: "full"}
  - {path: "swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md", range: "frontmatter + TL;DR + What was built"}
  - {path: "directions/_active/ai-consulting-dach/strategy-OPTIONS.md", range: "frontmatter (brigadier_cycle: 9)"}
  - {path: "decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md", range: "frontmatter"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "frontmatter"}
  - {path: "decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md", range: "frontmatter (brigadier_cycle_number: 7)"}
  - {path: "decisions/JETIX-SYSTEM-OVERVIEW.md", range: "frontmatter + opening summary"}
  - {path: "decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md", range: "§1 + §3 + §4 phases"}
  - {path: "swarm/wiki/meta/health.md", range: "live counters block — closed_cycles_count + fpar + matrix cells"}
provenance_inline: true
confidence: high
confidence_method: filesystem-validated-cross-referenced-log
---

# Cycle Artefact Register

Filesystem-validated inventory of all prior ROY swarm cycles and design records.
Purpose: Wave C Foundation Build can pull from this register rather than re-derive what exists.

---

## §1 Cycles Inventory (swarm/wiki/cycles/)

The `swarm/wiki/cycles/` tree does not carry one `_moc.md` per cycle dir. Cycle identity is recovered
from three corroborating sources: `swarm/wiki/log.md` (chronological), `agents/brigadier/strategies.md`
(DRR per cycle close), and gate files under `swarm/gates/`. [src:swarm/wiki/log.md]

| Cycle dir | Brigadier # | Date | Topic | Status | Key methodology snapshot |
|---|---|---|---|---|---|
| `cyc-swarm-self-improve-v1-2026-04-23` | 1 | 2026-04-23 | Swarm self-improvement hypotheses | closed-acked | First matrix 5x4 full-lit (17 cells). Gate-1 Option C + Gate-2 Option Alpha. 47 raw hyp → 19 clusters → 4 Phase-A OPPs + 3 deferred. FPAR 1.00. |
| `cyc-cycle-2-implementation-2026-04-24` | 2 | 2026-04-24 | OPP-04 + OPP-01 + OPP-02 + HD-01 + HD-02 closure | closed-acked | 5-item implementation cycle: cell_acceptance_predicate field, eval harness, hook layer, €50K gate propagation, M-class rate limiter. FPAR 1.00. Report at `decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md`. |
| `cyc-km-architecture-research-2026-04-24` | 3 | 2026-04-24 | KM + Project-Mgmt architecture research | closed-acked | 20/20 matrix cells. 6 KM variants (A1..B3). 9 preserved dissents. Sequenced-trajectory recommendation accepted (A1→B1→A2→B2→A3→B2). FPAR 1.00. |
| `cyc-km-materialization-mvp-2026-04-24` | 3 (HD-02 N=3 override) | 2026-04-24 | KM MVP materialisation: A1 substrate + B2 mini-swarm + B3 stage-gates + company-as-code | closed-acked | 8 design records under `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/`. ~60 physical files extracted post-ack. FPAR 0.95. Report at `decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md`. |
| `cyc-jetix-system-overview-2026-04-24` | 4 | 2026-04-24 | JETIX-SYSTEM-OVERVIEW — 14-layer coherent description | closed-acked | 15 cells × 3 waves. Description-shape M-task pattern (integrator-dominant; no critic/optimizer/scalability). 41.6K cell words + 11.2K integration. Canonical: `decisions/JETIX-SYSTEM-OVERVIEW.md`. FPAR 15/15. |
| `cyc-layer-6-community-deep-dive-2026-04-24` | 5 | 2026-04-24–25 | L6 Community: ICP Trinity + Alliance + Matchmaker + Secure Network | closed-acked | Phase-2 first layer deep-dive. 16 cells × 3 waves. Per-§ cell decomposition. Peer-input parallel cell pattern introduced. 27,561w canonical. 20 preserved dissents. FPAR 10/10. |
| `cyc-layer-5-product-deep-dive-2026-04-25` | 6 | 2026-04-25 | L5 Product Directions: 9 directions + portfolio synergy | closed-acked | 14 cells × 3 waves. Rapid-ack datapoint #2. 15-25K Deep Dive floor exceeded. Canonical: `decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md`. |
| `cyc-layer-7-business-trajectory-deep-dive-2026-04-25` | 7 | 2026-04-25 | L7 Business Trajectory: pricing + unit-econ + 5-gates + cash flow + risk register | closed-acked | 14 cells × 3 waves + brigadier-self TL;DR cell. 61,227w canonical. Cross-section number reconciliation discipline formalised. Phase 2 closes. Canonical: `decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md`. |
| `cyc-producer-services-strategy-options-2026-04-25` | 8 | 2026-04-25 | Producer Services strategy — 5 hypotheses OPTIONS paper | closed-acked (accept-as-options-paper) | Phase-3 first cycle. OPTIONS-PAPER mode introduced (AI does NOT strategize). 5 parallel cells. Canonical: `directions/_active/producer-services/strategy-OPTIONS.md` 7,582w. |
| `cyc-ai-consulting-dach-strategy-options-2026-04-25` | 9 | 2026-04-25–26 | AI Consulting DACH strategy — OPTIONS paper | closed-acked (accept-as-options-paper) | Phase-3 second OPTIONS cycle. Parallel with cycle 8. 6 cells (5 expert + brigadier-self). Canonical: `directions/_active/ai-consulting-dach/strategy-OPTIONS.md`. |
| `cyc-crm-build-2026-04-26` | 10 | 2026-04-26 | CRM subsystem build — multi-purpose contact network | closed (CYCLE-10-FULLY-COMPLETED) | Flat-file markdown+frontmatter CRM at `crm/`. 24 source files + 10 skills (/crm-*) + 35 unittests. 14 integration patches (CLAUDE.md / 6 agent system.md / wiki / tools). Smoke pipeline verified E2E. File: `swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md`. |
| `cyc-voice-pipeline-migration` | 11 | 2026-04-26 | Voice pipeline tooling migration | status: referenced-in-CLAUDE.md (not yet confirmed in gates/) | Voice pipeline step 3 filter.py + CRM voice router integration. Artefact: `crm/_scripts/voice_router.py`. Referenced in CLAUDE.md crm-system + voice-notes-pipeline sections. |
| `cyc-foundation-build-2026-04-28` | 12 | 2026-04-27–28 | Foundation Build Master Plan — library + best-practices research | IN PROGRESS (this cycle; Wave A + Wave B running) | Foundation methodology research (Wave A: project decomp analysis; Wave B: library + cycle register). This register is the Wave B-0 artefact. |

**Filesystem note.** Confirmed physical dirs at `swarm/wiki/cycles/`:
- `cyc-km-materialization-mvp-2026-04-24/` — design records referenced from `swarm/wiki/designs/` tree
- `cyc-foundation-build-2026-04-28/wave-b/` — this file
- Other cycle dirs do not carry `index.md` or `_moc.md` files; cycle identity recoverable from `swarm/wiki/log.md` + gate files only. [src:swarm/wiki/log.md:line 14-111]

---

## §2 Designs Inventory (swarm/wiki/designs/)

All confirmed design records are under `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/`.
No other T-* design dirs were found. [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/*]

| Part | File | Produced by | Wave | State | Methodology content |
|---|---|---|---|---|---|
| A | `partA-a1-substrate-bundle.md` | engineering-expert | 1 | accepted | A1 Karpathy++ substrate: wiki-roots.yaml extension, /ingest, /ask, /consolidate, /build-graph (Louvain-equiv), /lint (L-DANGLING-EDGE). 9 sub-artefacts. [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md] |
| B | `partB-b2-mini-swarm-bundle.md` | mgmt-expert | 1 | accepted | B2 Rich mini-swarm: project-types.yaml (4 types), /project-bootstrap, /project-review, /project-archive, project-brigadier template, 4 scaffold dirs, /lint L-PROJECT-MISSING-REQUIRED-FRONTMATTER. DSL-canonical stage gates enforced (philosophy-critic fixes integrated). [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md] |
| C | `partC-stage-gates-merged.md` | systems-expert | 1 | accepted | B3 stage-gate mechanic: DSL grammar (count(<glob>), count(<glob>:<marker>), <file.md>:<key> OP <n>); tools/stage-gate-eval.py; /lint --check-stage-gates --validate-predicate; 18 banned-phrase entries; /project-de-morph; /project-promote. [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partC-stage-gates-merged.md] |
| C (critic) | `partC-philosophy-critic-sg-predicate-rigor.md` | philosophy-expert | 1 | accepted | Philosophy × critic audit: 14 FAIL + 1 peer-input-needed. SG predicate rigor gate. 20 binary checks applied. Critic-in-parallel + proposed_replacement pattern operationalised. [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partC-philosophy-critic-sg-predicate-rigor.md:frontmatter] |
| D | `partD-company-as-code.md` | engineering-expert | 2 | accepted | Company-as-code discipline: /company-status, /knowledge-diff, CLAUDE.md delta, 12-row compliance snapshot, filesystem-SoT principle, git-native rollback, API-key audit. [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md] |
| E (mgmt) | `partE-quick-money-levenchuk-bootstrap.md` | mgmt-expert | 3 | accepted-with-dissent | Quick-money P1 + levenchuk-deep-dive P3 bootstrap design. CC-3 (ICP two-tier archetype filter), CC-4 (two-checkpoint kill_criteria), CC-5 (levenchuk kpi_targets) applied post-ack. CC-1 revenue-mix DEFERRED. Dissent preserved per AP-6. [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partE-quick-money-levenchuk-bootstrap.md:post_ack_revision] |
| E (investor-critic) | `partE-investor-critic-icp-kpi-realism.md` | investor-expert | 3 | accepted-with-dissent | ICP + KPI realism audit: 3 HARD FAIL + 1 conditional FAIL. Critic-in-parallel pattern with arithmetic-refutation preserved as dissent. Ruslan arbitrated Option C. [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partE-investor-critic-icp-kpi-realism.md] |
| E (eng-opt) | `partE-engineering-optimizer-e2e-demo-deltas.md` | engineering-expert | 3 | accepted | E2E demo optimizer: 5 invariants (WLNK/MONO/IDEM/COMM/LOC) preserved. Hermetic fixture dir spec. method-change=false attested. LOCALITY-BOUNDED. [src:swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partE-engineering-optimizer-e2e-demo-deltas.md] |

**No other design record trees confirmed** under `swarm/wiki/designs/`. The description-shape cycles (4, 5, 6, 7) produce canonical integration docs under `decisions/` directly, not design records under `swarm/wiki/designs/`. [src:swarm/wiki/log.md:lines 14-50]

---

## §3 Cycles 1-12 — Re-use Map for Foundation

| # | Name (cyc-*) | Canonical artefact(s) | Re-use for Foundation? | Notes |
|---|---|---|---|---|
| 1 | `cyc-swarm-self-improve-v1-2026-04-23` | `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01..04.md` | **yes — methodology** | Eval harness OPP-01, hook layer OPP-02, cell_acceptance_predicate OPP-04 are swarm governance primitives. Foundation cite: "swarm enforces these 3 quality gates." |
| 2 | `cyc-cycle-2-implementation-2026-04-24` | `decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md` | **yes — governance** | Implements OPP-01..04 + HD-01 + HD-02. Methodology pattern: design-record → implementation cycle. M-class rate limiter, hook layer log-only, eval harness are active infrastructure. |
| 3a | `cyc-km-architecture-research-2026-04-24` | `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md` | **partial — pattern only** | 6 KM variant research established A1 Karpathy++ as the selected substrate. Foundation may cite A1 selection rationale. Variant comparison itself (6 variants × 20 cells) is methodology for Foundation's own multi-variant research pattern. |
| 3b | `cyc-km-materialization-mvp-2026-04-24` | `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/part*.md` (7 records) | **yes — existing working parts** | A1 substrate (/ingest /ask /consolidate /build-graph /lint), B2 mini-swarm (/project-bootstrap etc.), B3 stage-gate DSL, company-as-code discipline — these ARE Foundation's L2 Knowledge layer + L3 Operations layer primitives. Do NOT reinvent; cite as "operational as of cycle-3b." |
| 4 | `cyc-jetix-system-overview-2026-04-24` | `decisions/JETIX-SYSTEM-OVERVIEW.md` | **yes — predecessor** | 14-layer system description is the direct predecessor of Foundation Master Plan. Foundation supersedes or refines SYSTEM-OVERVIEW for the library context. Description-shape M-task pattern (3-wave, integrator-dominant) is reusable for Foundation's own multi-layer artefacts. |
| 5 | `cyc-layer-6-community-deep-dive-2026-04-24` | `decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md` | **reference-only** | Community = Ruslan-specific business direction. Foundation's consultant cards reference community methodology outputs (Alliance, ICP archetype framework) but do not reinvent them. Per-§ cell decomposition + peer-input parallel cell patterns are reusable for Foundation's own decomposition. |
| 6 | `cyc-layer-5-product-deep-dive-2026-04-25` | `decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md` | **reference-only** | 9 product directions = Ruslan-specific. Foundation references Path A/B/C pricing model and the 9-direction portfolio as context. Rapid-ack-shortcut pattern (3 datapoints confirmed) is reusable for Foundation's gate design. |
| 7 | `cyc-layer-7-business-trajectory-deep-dive-2026-04-25` | `decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md` | **reference-only** | Business trajectory is Ruslan-specific (Phase 1-3, €50K gate, unit-econ). Foundation references the BOSC-A-T-X 5-gate model and cross-section number-reconciliation discipline. Cross-section reconciliation pattern (number-pass + Lock-pass + provenance-pass + F-G-R-pass) is reusable for Foundation's own integration passes. |
| 8 | `cyc-producer-services-strategy-options-2026-04-25` | `directions/_active/producer-services/strategy-OPTIONS.md` | **reference-only** | Specific business direction. Foundation references OPTIONS-PAPER cycle-class (AI does NOT strategize; proposal-language discipline; accept-as-options-paper ack-class) as a reusable swarm methodology primitive. |
| 9 | `cyc-ai-consulting-dach-strategy-options-2026-04-25` | `directions/_active/ai-consulting-dach/strategy-OPTIONS.md` | **reference-only** | Specific direction. Same OPTIONS-PAPER pattern as cycle 8. Second validation datapoint for OPTIONS-PAPER cycle-class. |
| 10 | `cyc-crm-build-2026-04-26` | `crm/` (24 files + scripts) | **yes — existing working part** | CRM is a Foundation working component (UC-K per CLAUDE.md). `crm/_schema/`, `/crm-*` skills, `crm/_scripts/crm.py` are operational. Foundation references CRM as "existing; do not rebuild." File: `swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md`. |
| 11 | `cyc-voice-pipeline-migration` (tentative) | `crm/_scripts/voice_router.py` + `tools/run_pipeline.sh` | **yes — existing working part** | Voice pipeline → CRM wire is operational. Foundation references voice pipeline as "existing; do not rebuild." Referenced in CLAUDE.md Voice-Notes Pipeline + CRM sections. |
| 12 | `cyc-foundation-build-2026-04-28` | this cycle — in progress | — | — |

---

## §4 AWAITING-APPROVAL Packets (swarm/awaiting-approval/ + swarm/gates/)

Confirmed gate documents with state at time of this register. [src:swarm/gates/* + swarm/awaiting-approval/*]

| Gate file | Cycle # | State | Topic | Key ack outcome |
|---|---|---|---|---|
| `swarm/gates/AWAITING-APPROVAL-cycle-2-implementation-2026-04-24.md` | 2 | acked (Option A) | OPP-01..04 + HD-01 + HD-02 implementation | Hook layer Alt-B (log-only mode). Eval harness seeded. M-class N=2 restored. |
| `swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md` | 3b | acked (Option C) | KM MVP — dissent arbitration + extraction scheduling | CC-3 + CC-4 + CC-5 applied. CC-1 deferred to empirical test. Option C = brigadier delegation. |
| `swarm/gates/AWAITING-APPROVAL-jetix-system-overview-2026-04-24.md` | 4 | acked (a1+b1+c1+d1) | JETIX-SYSTEM-OVERVIEW integration | USB-C/McKinsey resolution accepted. Smart AI internal-only. $1M+ ICP tier as D22 refinement. |
| `swarm/gates/AWAITING-APPROVAL-layer-6-community-deep-dive-2026-04-24.md` | 5 | acked (all-per-recommendations; Option C Hybrid) | L6 Community deep-dive | D15 ≥€5K clarified. 18 outreach templates preserved. Alliance Option C Hybrid. |
| `swarm/gates/AWAITING-APPROVAL-layer-5-product-deep-dive-2026-04-25.md` | 6 | acked (all-per-recommendations-with-Q01..Q05) | L5 Product Directions deep-dive | Path-B default. Smart AI internal. YouTube-analyzer deferred G2/G3. |
| `swarm/gates/AWAITING-APPROVAL-layer-7-business-trajectory-deep-dive-2026-04-25.md` | 7 | acked (accept) | L7 Business Trajectory deep-dive | Phase 2 closes. Q-L7-01..04 acked. Top-3 risks acknowledged. Phase 3 unblocked. |
| `swarm/gates/AWAITING-APPROVAL-producer-services-strategy-options-2026-04-25.md` | 8 | acked (accept-as-options-paper) | Producer Services OPTIONS paper | Selection deferred. Phase-1 selection-in-flight. No outreach activation yet. |
| `swarm/gates/AWAITING-APPROVAL-producer-services-strategy-options-2026-04-25-ack.md` | 8 | ack-file | Ack record for OPTIONS paper | State: `accepted-as-options-paper`. Final strategy deferred to Ruslan strategist-pass. |
| `swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md` | 10 | CYCLE-10-FULLY-COMPLETED | CRM subsystem build | Main scope acked + 3 follow-ups (F-1/F-2/F-3) closed in same cycle. |

**Not found:** Explicit cycle-11 gate file under `swarm/awaiting-approval/` or `swarm/gates/`. Voice-pipeline integration confirmed operational via CLAUDE.md and `crm/_scripts/voice_router.py` but gate file path not confirmed on disk.

---

## §5 Methodology Patterns Observed Across Cycles 1-11

Stable patterns that ROY swarm has compounded across cycles. Each pattern is filesystem-attested with at least 2 cycle instances. [src:agents/brigadier/strategies.md:lines 18-100]

**Pattern 1 — Stage-Gated AWAITING-APPROVAL (every M-class task).**
Every Method-class task halts at an AWAITING-APPROVAL packet before Phase 7 Compound + Phase 8 Archive. Packet carries: canonical artefact word count, per-section summary, brigadier recommendation, numbered Q-XX questions, Ruslan ack options. Validated cycles 1-10 (10/10). Gate files live under `swarm/gates/` (cycles 1-9) and `swarm/awaiting-approval/` (cycle 10+). [src:swarm/gates/AWAITING-APPROVAL-*]

**Pattern 2 — Per-§ cell decomposition + 3-wave parallel dispatch (description-shape M-tasks).**
For documents with N≥10 sections, decompose into one cell per top-level section; dispatch as Wave-A (independent foundational) → Wave-B (depends on Wave-A) → Wave-C (TL;DR + Open Qs + Dissents synthesis). Parallel within wave, serial across waves. Validated: cycles 5 (13 cells), 6 (14 cells), 7 (14 cells). [src:agents/brigadier/strategies.md:Cycle-5 DRR + Cycle-7 DRR]

**Pattern 3 — Dissent preservation (AP-6 — never average into consensus).**
Contradicting cell positions preserved as separate `dissents[]` entries with (F, ClaimScope, R) triples. Brigadier integration does NOT average. Validated: cycles 1 (7 dissents), 3a (9), 4 (5), 5 (20), 7 (embedded in reconciliations), 8 (5 D-PS-1..D-PS-5). Cumulative total: 24+ per `swarm/wiki/meta/health.md:preserved_dissents_total`. [src:swarm/wiki/meta/health.md:line 33]

**Pattern 4 — Design-record → extraction 2-stage (implementation-shape M-tasks).**
Wave 1-3 produce authoritative design records (promoted to `swarm/wiki/designs/`). A clerical extraction cell materialises physical files after ack. Brigadier context budget stays O(draft-reads) not O(file-count). Validated: cycle 3b (~60 physical files extracted from 8 design records). [src:agents/brigadier/strategies.md:Cycle-3 close DRR]

**Pattern 5 — Critic-in-parallel with proposed_replacement fields.**
When integrator cells write artefacts under formal rigor constraint (schema / DSL / arithmetic), pair with a critic cell in the same wave. Critic provides `proposed_replacement:` per rephrase-required item; brigadier applies as mechanical Edit operations — no author-cell re-dispatch. Validated: cycle 3b (philosophy-critic 14 FAILs → applied; investor-critic 3 HARD FAILs → arbitrated). [src:agents/brigadier/strategies.md:Cycle-3 close DRR]

**Pattern 6 — Peer-input parallel cell (when primary expert lacks arithmetic/financial dimension).**
When a primary integrator cell needs a dimension outside its domain, dispatch a peer expert cell in the same wave producing a sibling draft the integrator references but does not duplicate. Validated: cycle 5 (systems-expert Alliance + investor-expert ROI/unit-econ; zero peer-input-needed escalations). [src:agents/brigadier/strategies.md:Cycle-5 DRR]

**Pattern 7 — OPTIONS-PAPER cycle-class (AI does NOT strategize).**
When a cycle produces strategic hypotheses for Ruslan's selection (not a foundation document or implementation task), output language must be «here are N hypotheses + here's the data + here's brigadier proposal as one option among several — Ruslan chooses». Philosophy-expert C4 patrol checklist (20 binary checks) runs at integration. Ack-class: `accept-as-options-paper` (deferral of selection = the ack). Validated: cycles 8 + 9 (zero directive-language violations in both). [src:agents/brigadier/strategies.md:Cycle-8 DRR]

**Pattern 8 — Provenance gate + inline [src:...] citations.**
Every canonically promoted artefact carries `sources[]` frontmatter (non-empty) AND inline `[src:<path>#<section>]` per non-trivial paragraph. Validated swarm-wide per `swarm/lib/shared-protocols.md §2`. Observed in all 8 design records and all decisions/* deep-dives. [src:swarm/lib/shared-protocols.md:§2]

**Pattern 9 — Per-expert strategies.md compound learning (Layer-2 memory).**
Each expert appends 4-part DRR entries to `agents/<expert>/strategies.md` after each cycle they participate in. Brigadier appends cycle-close DRR to `agents/brigadier/strategies.md`. Cumulative: 19 strategy entries + 27 agent-improvement entries per `swarm/wiki/meta/health.md:line 31-32`. [src:swarm/wiki/meta/health.md:lines 31-32]

**Pattern 10 — Rapid-ack mode (high-confidence sequential cycles).**
When brigadier's recommendations are acked unchanged for 3+ consecutive cycles, formalize "rapid-ack mode" for subsequent cycles — reduced AWAITING-APPROVAL packet detail; Ruslan ack = 1-line "accept" or surfaces specific objections. Validated: L5 (cycle 6) + L6 (cycle 5) + L7 (cycle 7) = 3 consecutive 100% brigadier-recommended acks. [src:agents/brigadier/strategies.md:Cycle-7 DRR]

---

## §6 Recommendations for Foundation Wave C

### §6.1 Which cycles' methodologies should be cited / re-used in Foundation Wave C

Wave C (synthesis + Foundation document drafting) should cite the following cycles as methodology sources:

| Source | What to cite | Citation path |
|---|---|---|
| Cycle 1 (swarm-self-improve) | 5×4 matrix 20-cell model; eval harness OPP-01; cell_acceptance_predicate OPP-04 | `decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md §G.1` |
| Cycle 3b (km-materialization) | A1 substrate skills; B2 mini-swarm /project-bootstrap; B3 stage-gate DSL; company-as-code | `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA/B/C/D-*.md` |
| Cycle 4 (jetix-system-overview) | 14-layer architecture as predecessor; description-shape M-task pattern | `decisions/JETIX-SYSTEM-OVERVIEW.md` |
| Cycle 5 (L6 community) | ICP archetype framework; Alliance structure; matchmaker mechanics; peer-input cell pattern | `decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §2-§6` |
| Cycle 7 (L7 business) | BOSC-A-T-X 5-gate model; cross-section number reconciliation discipline; risk register RPN pattern | `decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md §2-§3, §11` |
| Cycle 8-9 (OPTIONS papers) | OPTIONS-PAPER cycle-class; proposal-language discipline; accept-as-options-paper ack-class | `agents/brigadier/strategies.md:Cycle-8 DRR` |

### §6.2 Which working pieces become "existing parts" (not reinvented by Foundation)

Foundation Wave C MUST reference these as existing operational infrastructure. Do NOT redesign or re-specify them — cite path + state:

| Working piece | Status | Path |
|---|---|---|
| A1 Karpathy++ substrate (/ingest, /ask, /consolidate, /build-graph, /lint) | operational | `.claude/skills/ingest.md` + `.claude/skills/ask.md` + `.claude/skills/build-graph.md` + `.claude/skills/lint.md` |
| B2 Mini-swarm (/project-bootstrap, /project-review, /project-archive, /project-de-morph, /project-promote) | operational | `.claude/skills/project-bootstrap.md` + `.claude/config/project-types.yaml` |
| B3 Stage-gate DSL (tools/stage-gate-eval.py + sg-banned-phrases.yaml) | operational | `tools/stage-gate-eval.py` + `.claude/config/sg-banned-phrases.yaml` |
| Company-as-code discipline (/company-status, /knowledge-diff) | operational | `.claude/skills/company-status.md` + `.claude/skills/knowledge-diff.md` |
| CRM subsystem (crm/ + 10 skills + 35 tests) | operational (cycle 10) | `crm/` tree; `crm/_scripts/crm.py` |
| Voice pipeline → CRM wire (voice_router.py) | operational (cycle 11) | `crm/_scripts/voice_router.py` + `tools/run_pipeline.sh` |
| ROY swarm 6-agent system (brigadier + 5 experts) | operational | `.claude/agents/brigadier.md` + `.claude/agents/*-expert.md` |
| Eval harness (swarm/evals/) | operational (seed-only; 3 < 20 floor) | `swarm/evals/run.sh` + `swarm/evals/cells/*/golden-set.jsonl` |
| Hook layer (log-only mode) | operational | `.claude/hooks/mode-prefix.sh` + `.claude/hooks/role-matrix.sh` + `.claude/hooks/verify-packet.sh` |

### §6.3 Methodology gaps relevant to Foundation

Items that cycles 1-11 have NOT yet addressed — potentially relevant for Foundation Wave C to flag:

1. **Cycle-11 gate file not confirmed.** Voice-pipeline migration referenced in CLAUDE.md but no explicit gate file found. If cycle-11 left open items, those may surface as Foundation pre-conditions.

2. **Design records only under T-km-materialization.** Other cycles (4, 5, 6, 7) produce canonical decisions/*.md directly — no `swarm/wiki/designs/` tree. Foundation's own implementation parts (if any) should use the design-record → extraction pattern (cycle 3b).

3. **shared-protocols.md §3.5 (OPTIONS-PAPER mode) not yet formally codified.** Brigadier strategies.md cycle-8 DRR flags this as forward-direction item. If Foundation Wave C produces any OPTIONS artefacts, brigadier should first codify this in shared-protocols.

4. **FPAR counter not updated post cycle-5** in `swarm/wiki/meta/health.md`. Health counters show `closed_cycles_count: 4` as of last write (2026-04-24). Cycles 5-11 compound learnings exist in strategies.md but health.md counters are stale. Foundation's compounding step should update health.md.
