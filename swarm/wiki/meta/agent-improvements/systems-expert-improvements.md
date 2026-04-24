---
id: improvement-systems-expert
title: systems-expert — Agent Improvements (cross-agent observations)
type: improvement
layer: 4
expert: systems
target_agent: systems-expert
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
tier: core
produced_by: brigadier
written_by: brigadier
sources: []
related: []
topics: []
tags: [#type/improvement]
improvement_target: prompt
validation_status: proposed
proposed_by: brigadier
applied_by:
applied_at:
---

<!-- T5 + R6 collapse: this file is brigadier-write only. Per-agent
improvements observed by OTHER agents during integration land here;
self-observations by systems-expert land in agents/systems-expert/
strategies.md (Layer-2 self-write). -->

# Improvements — systems-expert

Append-only log of systems-expert-improvement proposals surfaced by
OTHER agents.

## Entry format

4-part DRR per FPF E-9 with documented swarm-wide translation
(critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why
3. **Result** — observed outcome
4. **Review** — validated | refuted | partial

## Entries

### 2026-04-25 — systems × integrator + scalability-mode both productive in single cycle with heterogeneous §§ (cyc-layer-6-community-deep-dive Wave-A/B)

- **Decision:** Three systems × integrator cells (§4 5-Criteria Filter 4962w; §5 Alliance Architecture 7843w — largest systems-expert cell to date, 3 legal-structure options A/B/C × {governance + IP + revenue + membership tiers + phase fit + risks}; §6 Matchmaker Mechanics 4052w — 3 phases × migration triggers + KPI table). Plus one systems × scalability cell (§11 Evolution per Gate 5817w — 10×5 master table + G1→G5 narratives + Meadows/Ashby/VSM/Senge cross-gate view + antifragility check PASS). Four systems-expert cells in single cycle = new upper bound. All landed с F-G-R tags ≥3 per cell + zero §5.5.5 rejects. §5 Alliance cell produced brigadier-recommended Option C Hybrid (4-lock convergence D13+D20+D21+D27) — Ruslan acked recommendation first-read (Q-01).
- **Reasoning:** Systems-expert's §5 integrator rubric (Meadows leverage + Ashby requisite variety + feedback-loop mapping + Beer VSM) maps natively to Alliance legal-structure analysis (each option = distinct socio-technical system с own boundary, loops, VSM levels) and to matchmaker phase-by-phase (same VSM structure, different controller variety across phases — Ashby). Scalability-mode §11 evolution per gate = natural scalability-lens application (where does variety budget break? which Meadows rung is pliable per gate? what Beer VSM level shifts at each gate?). Brief provided explicit "systems lens authentically applied — Meadows / Ashby / Beer / Senge — pick what fits, don't name-drop" — all cells respected discipline, applying 1-2 frames per §§ без name-dropping all four.
- **Result:** All 4 systems-expert cells passed §5.5.5 on first submission; §11 antifragility check PASS (G1→G2 requires additive component-expansion not ≥30% replacement); 7 preserved dissents (S4 3: over-engineering / Adequate self-report / filter correlation; S5 2: Option A trust premium + Option B patent moat; S6 2: Ruslan-bottleneck vs platform-timing + Shifting-the-Burden; S11 2: Alliance timing vs D15 + matchmaker portrait-density prerequisite). Dissents legitimate per AP-6 — no averaging. Voice-2 Ruslan verbatim («могу уже сейчас делать одному») correctly cited in §6 as F5 founder-statement anchoring Phase-1 manual-mode.
- **Review:** validated. **Generalize:** systems × integrator scales to 3 primary cells + 1 scalability-mode cell per cycle when cells map distinct systems (5-criteria as membrane / Alliance as multi-VSM-option / Matchmaker as VSM System-3 variety-scaling) and scalability-mode cell has natural evolution-per-gate frame (§11). **Proposal:** pair systems × integrator + systems × scalability in same cycle as default for layer-deep-dive documents — integrator handles snapshot structure + scalability handles trajectory evolution. Both modes benefit from brigadier pre-brief listing F-level anchors in existing source material (intake §6 Ruslan clarifications, LOCKS-D25-D28). Upper bound testing pending L5 (9 product directions may stress systems-expert if each direction needs own VSM analysis).

### 2026-04-24 — systems × integrator identifies dominant leverage points + feedback loops at layer level (cyc-jetix-system-overview Wave-1/3 L1/L3/L-R)

- **Decision:** Three systems × integrator cells landed L1 Knowledge (3513w, 2 dissents) / L3 Synthesis (2297w) / L-R Resource (3404w, 2 dissents). L1 maps sequenced-migration trajectory A1→A2→A3 with measurable triggers + dominant reinforcing loop (expert-reads-wiki → better-output → feeds-wiki) and balancing loop (D28 anchor-filter). L-R identifies OPP-01 ap_cost instrumentation as Meadows-L6 information-flow gap — single highest-leverage intervention across all 5 resources. L3 names CE 40/10/40/10 cadence + sandbox-черновик protocol.
- **Reasoning:** Systems-expert's integrator mode §5 rubric (Meadows leverage + Ashby requisite variety + feedback-loop mapping) applies natively to layer descriptions where layer IS a system. Brief included explicit "systems-mode rigor — identify feedback loops (reinforcing / balancing)" — cell produced explicit loop maps with polarity notation.
- **Result:** All 3 drafts passed §5.5.5 gate; 4 preserved dissents across 3 drafts (L-R/L-P energy-boundary; G1-vs-G2 dashboard timing; L1 Path-B-vs-Path-C capital judgment; L1 dominant-loop-shift at G3). Dissents legitimate domain-disagreements per AP-6.
- **Review:** validated. Generalize: layer-description briefs should include systems-mode rigor prompt when layer has feedback-loop structure. Cross-layer leverage analysis is emergent capability — L-R's OPP-01 identification would not have surfaced without explicit "systems-mode" framing.

### 2026-04-24 — systems × integrator with philosophy × critic in parallel produces a more complete evaluator than either alone (cyc-km-materialization Part C)

- **Decision:** Wave-1 systems × integrator (Part C: B3 stage-gates merged into B2) produced 65 KB of spec covering DSL grammar (4-atom), tools/stage-gate-eval.py evaluator (≤193 LoC pure-Python+stdlib+pyyaml), /lint --check-stage-gates daily-cron algorithm, auto-spawn protocol, /project-de-morph reversibility skill, /project-promote SG-4-gated skill, 8 canonical example blocks. Meadows-leverage-points + Ashby-requisite-variety framings explicit in §1.
- **Reasoning:** systems-expert's §5 integrator rubric (feedback-loop-map-style synthesis of ingredients under variety-preservation constraints) mapped to a deterministic offline evaluator + 2 consequential skills + autospawn protocol. The DSL design (4 atoms, deterministic, non-Turing-complete) carries Ashby-requisite-variety floor explicitly.
- **Result:** Draft promoted after brigadier-applied philosophy-critic-1 fixes to DSL grammar + evaluator + examples (METRIC_ANCHORED_RE vs METRIC_BARE_RE; /lint --validate-predicate sub-flag with 18-banned-phrase regex list; 3 canonical example blocks rewritten to file-anchored forms). CC-10 DSL coverage gap (Popperian refutation) resolved by reusing existing `count(<glob>:<marker>)` form — no new primitive added.
- **Review:** validated. Pattern worth preserving: **systems × integrator writes the grammar; philosophy × critic writes the guard-rails; brigadier merges at integration time.** The evaluator implements grammar (systems), the validator enforces anti-regex list (philosophy). Neither could produce the other's half alone. **Improvement proposal:** integrator-mode self-check gains "every example in your §Example blocks must pass your own grammar's parse_predicate() without the BARE-reject diagnostic firing" — this would have caught the 3 example-block bare-metric forms the cell emitted.

### 2026-04-23 — systems × critic identified loop-dominance correctly — measurement void IS the root node

- **Decision:** systems-critic-01 H-8 (measurement void) was scored highest (sys 35.0) and every subsequent integrator pass confirmed this was the correct root-node identification. OPP-01 is the derivative implementation.
- **Reasoning:** systems-expert's §3 critic rubric invokes Meadows leverage points + Beer VSM levels. Empirically H-8 (information-flow absent) = Meadows L6; systems-expert correctly identified that no other intervention in the 47-hypothesis set was structurally upstream of H-8.
- **Result:** OPP-01 became the unambiguous #1 priority; even investor Kelly ranked it at 90.0 independent of systems. Cross-domain convergence validated systems-critic's leverage-point assessment.
- **Review:** validated. Pattern worth preserving: "systems × critic's Meadows-rung assignment IS the correct sequencing prior for all structural fixes." Engineering/mgmt/investor each have their own orderings, but structural-precedence goes to systems.

### 2026-04-23 — systems × scalability's Janus degraded-mode specs are the missing third column in opportunity assessment

- **Decision:** systems-scalability-01 §4 produced Janus degraded-mode projections (S-A excess / INT excess paths + recovery binary) for each of 4 OPPs. This is the first time any cell has named explicit failure-mode paths beyond "hypothetical risk #N."
- **Reasoning:** Scalability mode's §6 rubric mandates Janus dualism; most mode outputs focus on horizon trigger predicates. The S-A / INT axis was the unique contribution.
- **Result:** OPP-02 revealed as "highest S-A excess risk" (hook layer could dominate Phase-A thinking if it becomes the swarm's identity); OPP-04 revealed as "highest INT excess safety" (schema field integrates naturally). These are actionable insights for Cycle-2 scheduling.
- **Review:** validated. Systems × scalability should fire on every Phase-5 opportunity-drafting cycle; its cost (50 turns) is low relative to its signal quality.

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold per Шаг 2.2.4 Part C.
- **Reasoning:** D12 + R6 collapse; T5 mandates per-agent-improvements
  under `swarm/wiki/meta/`; brigadier-write rule per Q2.
- **Result:** file lint-valid.
- **Review:** scaffolding only.
