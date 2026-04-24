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

## Entries (newest on top)

### 2026-04-24 — description-shape M-task as 5th task-shape (addition to brigadier §3.2 matrix) — compound learning from cyc-jetix-system-overview

- **Decision:** brigadier §3.2 task-shape matrix currently has 4 shapes (design / review / optimize / scale-project). Cycle-4 introduces a 5th: **description** — task that produces coherent prose description of an existing system (vs designing new, reviewing existing, optimizing delta, projecting horizon). Description-shape uses integrator-dominant dispatch (N cells in M waves, where N=layer-count and M=3 natural grouping); critic reserved for Part F coherence; optimizer irrelevant (no existing to optimize); scalability absorbed into per-cell Evolution-path sub-section.
- **Reasoning:** Cycle-4 T-jetix-system-overview required 14 layer descriptions. Matrix 5×4=20 literal dispatch would require 20 cells (4 modes × 5 experts), but description doesn't need critic/optimizer/scalability on each — these modes are reviewing/optimizing/projecting existing drafts, not producing primary description. Empirical compound: 3-wave × 4-5 parallel integrator cells + 1 critic (deferred to Part F) delivered 41K primary-research words in ~50 min wall-clock vs estimated 3-4h serial.
- **Result:** 14 layer drafts passed §5.5.5 gate with 5 legitimate preserved dissents; integration pass assembled 11.2K-word SYSTEM-OVERVIEW; Ruslan acked A1+B1+C1+D1 without modifications. Second confirmation (after Cycle-3 sequenced-trajectory) that task-shape dispatch heuristics compound meaningfully.
- **Review:** partial — pattern operative on 1 cycle; propose re-baseline of brigadier §3.2 table in next Phase-B self-revision to add `description` row with `default cells: <expert>×integrator (4-5 cells, 3 waves); optional cells: philosophy×critic for Part F coherence; forbidden: optimizer (nothing to optimize); scalability (absorbed into integrator Evolution-path sub-section)`.

### 2026-04-24 — Derivative-integration artefact word-floor distinction validated 2nd datapoint (cross-cycle pattern from Cycle-3 + Cycle-4)

- **Decision:** Integration-derivative artefacts (brigadier-authored assembly over primary-research cell drafts) consistently land at 50-70% of primary-research word-floors when honest synthesis is used (vs padding to meet floor mechanically). Cycle-3: cell drafts 5436w avg (above 4500 floor); consolidated doc 8231w (below 15K floor); Ruslan acked "Substance OK". Cycle-4: cell drafts 2970w avg (above 800 floor); integration sections 540w avg (below 800 floor); total 11.2K (below 15K). Ruslan acked D1 "accept integration per-layer word counts as-is (primary drafts carry the depth)".
- **Reasoning:** Primary-research cells produce expanded exploration; integration-derivative compresses + cross-references + eliminates redundancy. Padding integration to match cell-floor would re-state draft content without value-add (AP-1 summary-compression anti-pattern).
- **Result:** Cross-cycle pattern confirmed. Execution-prompt templates for future M-tasks should distinguish "primary-research floor" (cell drafts) from "integration-derivative floor" (brigadier assembly).
- **Review:** partial — 2 cycles compound. Propose for standard execution-prompt template update: explicit 2-tier word-floor specification.

### 2026-04-24 — Defense-in-depth STACK preferred over single-mechanism for STRATEGIC-DIFFERENTIATOR use cases (UC-9 + UC-10 architectural-proof)

- **Decision:** When a use case is a STRATEGIC differentiator (per execution-prompt taxonomy: structural vs strategic; UC-9 client-isolation + UC-10 offline-first inference are strategic for Jetix per Strategic Insight 2026-04-24), brigadier's preferred architectural-proof shape is a DEFENSE-IN-DEPTH STACK (≥3 thin layers; each layer enforced by independent mechanism) — NOT a single thick mechanism. This rule was enacted in T-km-architecture-research-2026-04-24 §11 recommendation: UC-9 proof = env-var (engineering Δ1) + directory namespace (mgmt Δ4) + 13th `holon-ref` edge (systems Δ1) + Phase-B OS UNIX permissions; UC-10 proof = T-Offline (structured-excerpt) + T-Hybrid (HITL opt-in) + per-client `inference-stack.yaml` (ollama+Mistral default).
- **Reasoning:** Per philosophy × integrator's §3 meta-decision arbitration in cyc-km-architecture-2026-04-24: Lakatos protective-belt logic — multiple thin layers > single thick layer for strategic moat preservation. Single-mechanism failures are SINGLE-POINT-OF-FAILURE; defense-in-depth STACK degrades gracefully (one layer breach surfaces signal but is contained). Per BIOS-clone-wars research §11 Урок 1: single-point-of-control fails in multilayer systems. Per Cycle-3 evidence: each of 5 expert lenses surfaced a different UC-9 mechanism (engineering session-level / mgmt directory-namespace / systems graph-edge / philosophy supersession-chain / investor capital-flow gate) — STACKING them is strictly stronger than any single one.
- **Result:** Ruslan acked the STACK-recommendation Option A on first read; no rejection. Future M-tasks where a strategic-differentiator use case must be proved should default to defense-in-depth STACK with explicit ≥3 layers + per-layer fallback failure mode + per-layer audit-log signal.
- **Review:** validated once empirically (Cycle-3 close). Cross-references: `agents/brigadier/strategies.md` 2026-04-24 entry on sequenced-trajectory framing; `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-integrator-epistemic-overlay.md` §3. Watch: does the STACK pattern hold for non-architectural strategic differentiators (e.g., a future strategic-differentiator UC for matchmaker Lock-21 or Mittelstand AI Alliance governance)?

#### Evolution
- changelog:
  - 2026-04-24 — created (T-km-architecture-research cycle close)
- last-review: 2026-04-24
- expected-evolution:
  - cycle_5: pattern fires 1× more on Mittelstand AI Alliance governance design (if that becomes a strategic-differentiator UC); confirm STACK-vs-single discipline
  - cycle_50: codify as a brigadier rule "strategic-differentiator UCs require ≥3-layer STACK with named per-layer mechanism" added to `.claude/agents/brigadier.md §3.2 task-shape-cell-selection-matrix`
  - cycle_200: STACK depth may extend to 5+ layers as Alliance methodology parliament (per philosophy-scalability §7) adds governance-level enforcement

### 2026-04-24 — OPP-04 cell_acceptance_predicate proved load-bearing at scale; rate-limited refusal NOT NEEDED in Cycle-3

- **Decision:** Cycle-3 dispatched 20 cells with cell_acceptance_predicate per OPP-04 (cycle-2 implementation); zero cells were refused at dispatch for trivial-predicate violations; zero return-packet schema violations. The predicate field correctly DETERRED label-only outputs by being explicit at brief-time about what counts as success per cell.
- **Reasoning:** Pre-OPP-04 cycles risked AP-2 vacuous-critic (returns "looks good" without ≥5 binary checks). With OPP-04, every cell brief named the binary success-condition (e.g., "Returns ≥5 binary Conformance Checks AND ≥2 Alternatives per check AND explicit Anti-scope AND each row F-G-R triple"). All 20 returns met the predicate. The protection was structural-prevention not runtime-rejection — predicate-shaping at brief-time was sufficient.
- **Result:** 20/20 cells returned schema-valid packets with substantive bodies (per V12 + V14 verification checks: UC-9 markers 9-25/variant; UC-10 markers 13-29/variant; Strategic Insight + BIOS citations 1-2/variant). Cell-draft prose 108,712 words; quality high across all 5 experts × 4 modes.
- **Review:** validated. OPP-04 is doing the work it was designed for. Predicates ARE pedagogical — they shape cell outputs at brief-time, not via runtime rejection. Cross-reference: cycle-2 OPP-04 implementation report at `decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md`.

#### Evolution
- changelog:
  - 2026-04-24 — created (T-km-architecture-research cycle close)
- last-review: 2026-04-24
- expected-evolution:
  - cycle_5: 2nd full-matrix M-cycle confirms predicate-shaping efficacy; measure refusal-rate trend
  - cycle_50: predicate library codified — common predicates per (expert, mode) pair stored at `swarm/wiki/_templates/cell-predicates/<expert>-<mode>.md` for brigadier to reuse
  - cycle_200: predicate-evaluator skill `/lint --check-cell-predicates` added if Phase-B brigadier dispatches start producing trivial predicates under volume

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
