---
id: improvement-system-level
title: System-Level Improvements (cross-agent + brigadier-meta)
type: improvement
layer: 4
expert: system-level
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
tier: core
produced_by: brigadier
written_by: brigadier            # single-writer per Q2; T5 + R6 collapse per D12
sources: []                      # populated as cycles compound
related: []
topics: []
tags: [#type/improvement]
improvement_target: protocol     # default; specific entries may override
validation_status: proposed
proposed_by: brigadier
applied_by:
applied_at:
---

<!-- T5 + R6 collapse: this file is brigadier-write only. Per-agent
improvements live in agents/<expert>/strategies.md (Layer 2, self-write);
cross-agent + brigadier-meta improvements live here (Layer 4,
brigadier-write per Q2). -->

# System-Level Improvements

Append-only log of improvements that affect the swarm at the
system level — i.e. changes that touch the brigadier itself, the
shared-protocols runtime contract, the wiki schema, or invariants that
span ≥2 experts.

## Entry format

Each entry uses the 4-part DRR format per E-9 + Evolution sub-block.
See `agents/brigadier/strategies.md` for the canonical template.
Cross-references between strategies entries and improvement entries
are mandatory: every improvement here cites at least one
`agents/<id>/strategies.md` entry that motivated it.

## Entries

### 2026-04-23 — MP-1 "executor-not-wired" is the dominant system-level pattern; named hooks + evals are the single highest-leverage fix

- **Decision:** Adopt MP-1 "executor-not-wired" as a first-class observability target. The pattern surfaced in 5/5 cells' Phase-1 extractions (α/β/γ/δ/ε) and again in ζ cross-pollination; systems × critic called it Meadows L6 dominance; philosophy × integrator named it EC-6.
- **Reasoning:** Hooks wired (OPP-02) + eval harness (OPP-01) are the two fixes this cycle identified to close the gap. Both approved at Gate 2. Beyond this cycle, brigadier should continue treating "executor-not-wired" as a red-flag class across the wiki (spec files without executors, schemas without validators, protocols without enforcement).
- **Result:** Gate 2 approved both fixes. MP-1 instance count: OPP-01 closes (measurement executor), OPP-02 closes (mode + tool + verifier executors), OPP-04 closes (schema executor). Four MP-1 manifestations closed this cycle.
- **Review:** validated empirically by cross-cell agreement (5/5 cells surfaced independently). Watch for Cycle-2: does MP-1 instance count trend down once the three structural fixes ship?

#### Evolution
- changelog:
  - 2026-04-23 — created
- last-review: 2026-04-23
- expected-evolution:
  - cycle_5: MP-1 instance count measurable via edges.jsonl "executor-missing" edge-type; Cycle-5 target ≤3 instances
  - cycle_50: pattern may dissolve if hook+eval infrastructure is mature; or may reappear at wiki-v3-v4 transition
  - cycle_200: MP-1 remains a permanent observability class; Phase-B adds "executor-coverage" as a named health counter

### 2026-04-23 — Matrix 5×4 full coverage is viable in a single cycle under parallel-dispatch discipline

- **Decision:** First real cycle fired all 20 (expert, mode) cells at least once. Brigadier should aspire to full-matrix exercise in future M-class self-improvement cycles (not R/T tactical cycles which use Chat or sub-cell dispatch).
- **Reasoning:** Rule-of-4 knee violation (α context; 5 experts vs 4-agent working-memory ceiling) argued via Ashby requisite variety. Empirically this cycle: 17 cell invocations across 4 modes + all 5 experts, each cell returned ≤500-turn packets, each packet actionable. No coordination collapse observed.
- **Result:** Full-matrix cycle produced 2 shippable Gate packets + 2 Decision documents + ~3000 lines of design detail + 4 drafted opportunities + experimental design for baseline. Wall-clock ~3 hours.
- **Review:** validated once. Worth replicating on next M-class cycle (e.g., when OPP-01+OPP-02+OPP-04 actual implementations are M-classed for the following cycle).

#### Evolution
- changelog:
  - 2026-04-23 — created
- last-review: 2026-04-23
- expected-evolution:
  - cycle_5: second M-class full-matrix cycle to confirm; measure coordination overhead vs Cycle-1 baseline
  - cycle_50: catalogue which (expert, mode) pairs are systematically under-exercised; M-class cycles may stop being the only trigger
  - cycle_200: Phase-B Ashby capacity re-evaluated; if intake >10/week, full-matrix M-cycles become ritual pattern, not opportunity

### 2026-04-23 — E-5 dissent-preservation works in practice; averaging temptation resisted

- **Decision:** 7 dissents preserved with (F, ClaimScope, R) triples in integrator outputs (5 from mgmt × integrator + 2 from philosophy × integrator meta-sanity). No integrator averaged. Every dissent carries resolution-path + refutation-conditions + acceptance-conditions.
- **Reasoning:** brigadier §5.5 AP-6 hard lock. Before this cycle, E-5 was a spec claim; now it has empirical footprint. The 5-dissent pattern emerged organically from 47-hypothesis dedup process.
- **Result:** Document 1 §7 enumerates all 7 dissents with full (F, ClaimScope, R) discipline. Gate-1 packet referenced them; Ruslan acked Option C informed by dissent landscape. Gate-2 packet preserved them for Cycle-5 revisit.
- **Review:** validated — dissent preservation produced better gate-ack discipline (Ruslan could see cross-expert tensions); no averaging-temptation observed in either integrator pass. Watch: do dissents actually resolve at Cycle-5 with empirical data, or do they proliferate (indicating dissent-preservation is being used as a ceremony rather than as an active resolution-path)?

#### Evolution
- changelog:
  - 2026-04-23 — created
- last-review: 2026-04-23
- expected-evolution:
  - cycle_5: revisit all 7 dissents; mark resolved/refuted/still-open with empirical evidence
  - cycle_50: dissent accretion rate vs resolution rate — if accretion outpaces resolution by >2×, dissent-preservation needs reform (maybe hit a cap, or require forced-resolution ritual)
  - cycle_200: Phase-B may require a dedicated "dissent-resolver" cadence independent of cycle-close

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold `system-level-improvements.md` per Шаг 2.2.4
  Phase 2.3 critic-gate1 H-2 fix.
- **Reasoning:** D1 §1.4 #14 lists 7 bootstrap files under
  `swarm/wiki/meta/agent-improvements/`; brigadier §8.3 dispatches
  improvements writes during Compound (α-1 `approved → compounded`).
  The brigadier needs a writeable scaffold from Day 0; otherwise the
  first compound step fails on the missing file.
- **Result:** file lint-valid, brigadier-write rule active, T5 +
  R6 collapse honored, Phase A bootstrap unblocked.
- **Review:** scaffolding only; first real entry on first cycle that
  surfaces a system-level improvement (likely α-4 #1 or #2).

#### Evolution
- changelog:
  - 2026-04-23 — created (scaffolding)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: first real cross-agent improvement entry from observed cycle behaviour
  - cycle_50: 5–10 entries including ≥2 protocol-level proposals (likely shared-protocols revisions)
  - cycle_200: stable rate ~1 entry per 5 cycles; majority `validation_status: accepted`
