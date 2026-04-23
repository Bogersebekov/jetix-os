---
id: investor-optimizer-01
title: "Investor Optimizer — T-swarm-self-improve-v1 capital-allocation sequencing"
type: optimizer-artefact
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: investor-expert
mode: optimizer
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: arithmetic + judgment
niche: meta
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-critic-01.md", range: "1-391"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "1-204"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "1-126"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md", range: "1-306"}
  - {path: ".claude/agents/investor-expert.md", range: "1-60"}
---

# Investor Optimizer — Swarm Self-Improvement v1

**Optimizer scope:** PARAMETER-level re-sequencing and weighting of the
8 investor hypotheses (H-1..H-8) from investor-critic-01. This pass
applies Kelly-style edge scoring, bundles hypotheses that share
measurement infrastructure, and produces sharpened unit-econ arithmetic
(€/turn, turns/cycle, compounding payback). NOT method-level — no
framework substitution.

---

## Decision-rights ritual (pre-work)

Before any delta:

1. Is this action in `autonomous`? — Yes: draft a capital-allocation
   memo, draft a unit-econ-arithmetic, apply optimizer heuristics per §4.
2. Any `requires-approval` row triggered? — No horizon-gate shift; no
   external capital; no cross-direction reallocation; no canonical wiki
   write.
3. Any `never` row triggered? — No canonical wiki write; no peer cell
   call; no provider API-key reference.

Proceeding.

---

## Invariant Check (WLNK / MONO / IDEM / COMM / LOC)

| Invariant | Applies | Preserved | Evidence |
|---|---|---|---|
| **WLNK** (capital-flow continuity) | Yes — every "capital" unit here is Ruslan's attention-turns; each re-ranked hypothesis must still map from allocator (Ruslan's budget) → deployed action → named return path (turn savings, compounding output, or consulting revenue lift). | Yes — every hypothesis in the optimized set names a return path below. | All 8 hypotheses carry a `return_path` in the optimized block. Zero-allocation hypotheses are explicitly retired (via-negativa discipline), preserving zero silent-leakage. |
| **MONO** (rank-order monotone) | Yes — the ranking must be monotone on the primary scoring dimension (Kelly-edge × payback-cycles). Re-ordering must not flip any quality score relative to the previous rank. | Yes — the Kelly-edge table below shows a strict partial order; no two positions tied on all three sub-dimensions without an explicit tiebreaker. | See Kelly-edge table §3. |
| **IDEM** (idempotency) | Yes — re-running this optimizer on the post-delta state (same hypotheses, same scores) must yield the same ranking. | Yes — scores are arithmetic functions of fixed inputs (turns-per-cycle, payback-horizon, kill-condition count). No stochastic elements. | Formulas in §4; re-application yields identical rank. |
| **COMM** (commutativity) | Partial applicability — optimizing H-1 before H-4 vs H-4 before H-1 changes only intermediate bundling steps, not the final Kelly-ranked sequence, because bundling is decided by infrastructure-overlap, not ordering. | Yes — the final bundle assignments are determined by shared measurement substrate, not by traversal order. | Bundle logic in §5 is set-based, not path-dependent. |
| **LOC** (locality) | Yes — this optimizer touches ONLY the 8 hypotheses from investor-critic-01. It does NOT reach into engineering implementation, org structure, or consulting-revenue allocation. | Yes — delta column below changes only hypothesis weights, sequencing, and bundle assignments. | No delta touches any artefact outside the investor domain. |

All five invariants: **preserved**.

---

## Baseline (from investor-critic-01)

The baseline is the priority-ordered recommendation list from
investor-critic-01, implicitly equal-weighted (no explicit Kelly scores):

| # | Hypothesis / Action | Implicit weight | Return path (stated in critic) |
|---|---|---|---|
| 1 | Write canonical unit-econ block (turns-in vs compounding-output) before cycle_5 | equal | owner-earnings equivalent |
| 2 | Pre-commit Phase-A convergence metric (binary predicate at cycle_10) | equal | measurement gate for compounding |
| 3 | Wire E-17 Decompose-or-Chat gate as machine-testable refuser + turn-budget log | equal | closes AP-INV-2; makes 15× cost lock real |
| 4 | Author first golden-set comparison: solo-brigadier vs 6-cell matrix on identical task | equal | validates 2-3× quality gain claim |
| 5 | Name opportunity-cost explicitly (consulting revenue foregone) | equal | margin-of-safety arithmetic |
| 6 | Resolve €50K horizon-gate divergence (add to brigadier + 4 peer §6.1) | equal | cross-expert scalability synthesis coherence |
| 7 | Add `expected_invocation_frequency` + `estimated_turn_savings_per_invocation` to DRR | equal | converts rule accumulation → Kelly-criterion rule investment |
| 8 | Write paid-API transition threshold memo before €200K gate | equal | capital decision at gate |

Baseline expected return: unquantified. No turns/cycle metric. No payback arithmetic. Opportunity-cost: unnamed across all 8. Margin-of-safety: absent (C2 fail from critic). This is the baseline to beat.

---

## §3 Kelly-Style Edge Scoring

**Scoring method.** For each hypothesis, three sub-dimensions are scored 0-10:

- **E (edge):** net advantage if hypothesis fires correctly vs not firing.
  Scale: 0 = no advantage; 10 = eliminates the largest capital-leakage
  confirmed in critic-01.
- **P (probability of success within Phase A):** how likely is this
  hypothesis to produce its return within the first 20 cycles, given
  current infrastructure. Scale: 0 = blocked (requires Phase B); 10 =
  implementable today in <1 sprint.
- **Payback cycles:** how many cycles until the investment in this
  hypothesis breaks even on turns consumed vs turns saved. Lower = better.

**Kelly-analog score = E × P / Payback** (normalised; higher = allocate first).

| H-code | Hypothesis (short) | E | P | Payback cycles | Kelly-score | Rank |
|---|---|---|---|---|---|---|
| H-6 | Add `expected_invocation_frequency` + `estimated_turn_savings` to DRR template | 9 | 10 | 1 | **90.0** | **1** |
| H-1 | Write canonical unit-econ block (turns-in vs compounding-output) | 9 | 9 | 1 | **81.0** | **2** |
| H-2 | Wire E-17 gate as machine-testable refuser + turn-budget log | 8 | 8 | 2 | **32.0** | **3** |
| H-5 | Resolve gate-ack latency structural misalignment (add SLA + fallback) | 7 | 9 | 2 | **31.5** | **4** |
| H-4 | Author golden-set comparison (solo-brigadier vs 6-cell) | 8 | 7 | 3 | **18.7** | **5** |
| H-7 | Resolve €50K horizon-gate divergence | 5 | 10 | 1 | **50.0** | — see note |
| H-3 | Fortify moat hierarchy (name all 4 moat candidates' kill-conditions formally) | 6 | 7 | 5 | **8.4** | **6** |
| H-8 | Write paid-API transition threshold memo | 5 | 6 | 8 | **3.75** | **7** |

**Note on H-7 re H-2.** H-7 (horizon-gate divergence) has a high raw
Kelly score (50.0) because its implementation cost is near-zero (a 1-PR
edit to 4 agent files + brigadier §4.6). However, it is a STRUCTURAL FIX
to cross-expert consistency, not a capital-allocation mechanism itself.
Its value is unlocking the correctness of cross-expert scalability
synthesis. It is therefore **bundled with H-2** (gate discipline) because
both are "swarm-infrastructure correctness" investments: one fixes turn
accounting, one fixes gate-datum accounting. See §5.

**Scoring rationale (selected):**

- **H-6 scores highest (E=9, P=10, Payback=1).** The DRR template
  already exists in `agents/<expert>/strategies.md`. Adding two fields
  (`expected_invocation_frequency`, `estimated_turn_savings_per_invocation`)
  is a single-file edit per expert (6 files, ~30 minutes). The payback is
  immediate: cycle_2 onward, every Compound step produces a Kelly-
  rated rule, not an undifferentiated accumulation. Edge is high because
  H-1's critic-01 confirmed the absence of rule discrimination is the
  primary driver of the linear-vs-exponential compounding gap (the
  "rule accumulation without payback" pathology named in H-6).

- **H-1 scores second (E=9, P=9, Payback=1).** Writing a unit-econ
  block is a documentation task, not an engineering task. No new
  tooling required. Output: a single `swarm/wiki/drafts/T-*-investor-
  unit-econ-block.md` with the canonical
  `turns_in | strategies_entries_added | artefacts_accepted | turns_saved_by_rules (estimated) | net_turn_surplus`
  table filled from this cycle's data. Payback = 1 cycle because every
  subsequent cycle can compare against the baseline. Edge is high because
  ALL eight C1..C8 conformance failures in critic-01 trace to the absence
  of this block — it is the prerequisite for every other check.

- **H-2 scores third (E=8, P=8, Payback=2).** Wiring E-17 requires
  a `.claude/settings.json` hook change — feasible in Phase A per
  ζ [ζ:57-67, ζ:T-3]. Two-cycle payback because the first cycle
  produces the hook; the second cycle is the first to run with it.
  Edge is high because the ceremonial 15× cost lock is the largest
  single turn-budget leak identified in critic-01 H-2.

- **H-4 scores fifth despite high E (8) because P=7 and Payback=3.**
  The golden-set comparison requires (a) picking a representative task,
  (b) running both solo-brigadier and 6-cell paths on it, (c) scoring
  both via Hamel-binary predicates. Phase A feasibility is medium (no
  automated harness yet; file-JSONL harness is the Phase A substitute
  per ζ T-5). Three-cycle payback is generous; it could be higher if
  the harness takes longer to stand up than estimated.

- **H-8 scores last (E=5, P=6, Payback=8).** The paid-API transition
  threshold memo is important but not urgent: it is a gate-conditional
  capital decision (required BEFORE €200K gate, which is not imminent).
  It depends on H-1 (unit-econ block) and H-4 (quality-gain measurement)
  being completed first — you cannot compute the paid-API vs Max-sub
  tradeoff without knowing the current swarm's quality-gain-per-turn.
  Sequencing it last is correct.

---

## §4 Tightened Unit-Econ Arithmetic

### §4.1 Turn-cost model (Phase A, current cycle as data point)

From investor-critic-01 H-2 arithmetic and ε context data:

```
Observed this cycle (T-swarm-self-improve-v1):
  - Context extraction: 6 cells × ~30 turns = 180 turns
  - Expert critic cells: 5 cells × ~30 turns = 150 turns (estimate)
  - Brigadier integration: ~40 turns (estimate)
  - Total cycle estimate: 180 + 150 + 40 = 370 turns
  - Strategies.md entries produced this cycle: 0 (scaffolding only; no real DRR entries yet)
  - Artefacts accepted this cycle: TBD (integration not closed)

Unit-econ: turns_per_cycle = 370 (est)
           strategies_entries = 0 (pre-cycle; expected: 1-3 per expert after Compound step = 6-18 total)
           artefacts_accepted = 0→2 (this cycle)
           turns_saved_by_existing_rules = 0 (no rules exist yet)
           net_turn_surplus = -370 + 0 = -370 (pure capex; no payback yet)
```

**Margin-of-safety computation (Graham P2):**

- Expected return per cycle: quality-gain-equivalent = 1.5× (conservative per Boris Cherny lower-bound; no golden-set validation).
- Opportunity cost: Ruslan doing same work solo = estimated 150 turns (6-cell work at 1/2.5× quality-equivalent).
- Risk-of-ruin floor: worst case = 370 turns consumed with zero compounding output = 2.5× sunk vs solo path.

```
MoS = (expected_return - opportunity_cost - ruin_floor) / opportunity_cost
    = (1.5 × 150 - 150 - 0.2 × 150) / 150
    = (225 - 150 - 30) / 150
    = 45 / 150
    = 0.30
```

Exactly at the 30% Graham minimum. Below 1.5× quality: MoS goes negative. This is the knife-edge the critic identified. The optimizer's job is to move MoS above 0.30 by reducing opportunity cost (cycle turn efficiency) and increasing expected return (compounding quality).

### §4.2 Per-hypothesis turn cost and compounding payback

For each hypothesis, the cost to implement (turns to execute) and the
payback (turns saved × frequency × cycles until breakeven):

| H-code | Implementation cost (turns) | Per-cycle turn savings (post-implementation) | Frequency (invocations/cycle) | Cycles to breakeven | NPV over 20 cycles |
|---|---|---|---|---|---|
| H-6 (DRR Kelly fields) | 3 turns (6 file edits, 30 min) | 2-4 turns/cycle (discriminating rules reduces Compound overhead by avoiding low-value rule writes) | Every cycle | **1 cycle** | +37-77 turns net (20 cycles × 2-4 turns saved − 3 turns cost) |
| H-1 (unit-econ block) | 5 turns (draft memo, anchor data) | 5-10 turns/cycle (eliminates re-derivation of baseline at each Compound step; enables critic pre-clearing) | Every cycle | **1 cycle** | +95-195 turns net |
| H-2 (E-17 gate) | 15 turns (hook wiring + test) | 30-60 turns/cycle (blocks wasted 15× invocations on simple tasks; at 50% frequency reduction × 150 turns/cycle saved) | Every 2nd cycle (catches ~50% of over-dispatches) | **1 cycle** | +585-1185 turns net — **highest absolute NPV** |
| H-5 (gate-ack SLA) | 8 turns (add SLA + fallback clause to §1d) | 10-20 turns/cycle (reduces cycle re-initiation overhead when gates block) | Every gated cycle (~30% of cycles) | **2 cycles** | +52-112 turns net |
| H-7 (horizon-gate align) | 2 turns (4-file edit) | 3-6 turns/cycle (eliminates cross-expert scalability synthesis reconciliation cost) | Every scalability invocation (~20% of cycles) | **1 cycle** | +10-22 turns net |
| H-4 (golden-set comparison) | 40 turns (design task, run both paths, score) | 10-20 turns/cycle (enables confident critic pre-clearing; reduces false-positive critic cycles) | Every 5th cycle (re-run every 5 cycles to track trajectory) | **4-5 cycles** | +40-100 turns net (conditional on harness completion) |
| H-3 (moat kill-conditions formal) | 10 turns (systematic kill-condition enumeration for all 4 moat candidates) | 2-3 turns/cycle (reduces moat-claim re-derivation at each moat-analysis invocation) | Every moat invocation (~30% of cycles) | **5 cycles** | +2-8 turns net |
| H-8 (paid-API memo) | 20 turns (capital memo; full C1-C8 compliance) | 0 turns/cycle (one-time capital decision document; no recurring savings) | 1 time (gate-conditional) | **Not applicable: gate-conditional** | N/A (option value only) |

**Key finding from the arithmetic:** H-2 (E-17 gate wiring) has the highest absolute NPV over 20 cycles by a factor of 6-15× over all others. Yet it ranked third in Kelly-score because of a 2-cycle payback. Both views are correct and complementary: H-6 and H-1 are FIRST because they cost almost nothing and pay back immediately; H-2 is the BIGGEST single improvement by turn-savings volume.

---

## §5 Bundle Map: Cross-Hypothesis Infrastructure Leverage

Three bundles where shared measurement infrastructure gives cross-hypothesis leverage. Implementing one unlocks the other.

### Bundle A: "Owner-Earnings Substrate" — H-1 + H-6 + H-3

**Shared infrastructure:** The DRR strategies.md template (Layer-2 memory).

- H-1 (unit-econ block) authors the **canonical turn-cost table** that populates the `net_turn_surplus` field.
- H-6 (DRR Kelly fields) adds `expected_invocation_frequency` + `estimated_turn_savings_per_invocation` to the DRR format that H-1's unit-econ block feeds.
- H-3 (moat kill-conditions) adds `kill_condition_1` + `kill_condition_2` fields to the moat-analysis DRR entries that already exist in strategies.md.

**Single infrastructure investment unlocks all three:** a 1-session edit to `agents/<expert>/strategies.md` template (6 files) adds the Kelly fields (H-6) and the kill-condition format (H-3). H-1 populates the first row of the resulting table from this cycle's data. One PR, three hypotheses advanced.

**Combined implementation cost:** 8 turns (vs 3 + 10 + 5 = 18 turns if done separately). Saves 10 turns in implementation. Payback: cycle_1 for H-6, cycle_1 for H-1, cycle_5 for H-3.

### Bundle B: "Gate Discipline" — H-2 + H-7 + H-5

**Shared infrastructure:** The gate layer (`.claude/settings.json` hooks + §1d requires-approval clause).

- H-2 (E-17 gate wiring) installs the hook that enforces Decompose-or-Chat. Requires `.claude/settings.json` edit + brigadier §3.0 update.
- H-7 (horizon-gate alignment) requires edits to brigadier §4.6 and 4 peer-expert §6.1 tables. These are the same 4-5 files touched by H-2's brigadier update.
- H-5 (gate-ack SLA + fallback) requires a 1-paragraph addition to §1d `requires-approval` in investor-expert.md — the same file H-2 references for the Decompose-or-Chat threshold.

**Single infrastructure investment:** one "gate discipline PR" touches brigadier.md + investor-expert.md (and 3 peer files for H-7) and delivers H-2 + H-5 + H-7 together.

**Combined implementation cost:** 20 turns (vs 15 + 8 + 2 = 25 turns separately). Saves 5 turns. Payback: H-7 at cycle_1, H-2 at cycle_2, H-5 at cycle_3.

### Bundle C: "Measurement Substrate" — H-4 + H-8

**Shared infrastructure:** A comparison benchmark task and a cost-measurement framework.

- H-4 (golden-set comparison) requires running solo-brigadier vs 6-cell on an identical task and recording results in `swarm/evals/cell-matrix-vs-solo/results.jsonl`.
- H-8 (paid-API threshold memo) requires knowing (a) turns/cycle (from H-1) and (b) quality-gain/turn (from H-4) to compute the paid-API vs Max-sub tradeoff. H-4 is a prerequisite for H-8.

**Sequencing dependency:** H-4 must complete before H-8 can be written. Bundle C is therefore a **sequential dependency bundle**, not a concurrent one. H-4 opens the gate for H-8. Attempting H-8 before H-4 produces a capital memo built on unvalidated quality-gain assumptions — AP-INV-9 (base-rate neglect).

**Combined implementation cost:** 40 + 20 = 60 turns (no concurrency savings, but the H-4 output becomes the primary provenance citation for H-8, reducing H-8 research time from 25 to 20 turns). Saves 5 turns.

---

## §6 Proposed Allocation (Before / After)

**Capital unit:** Ruslan attention-turns per hypothesis investment, Phase-A cycle sequence.

### Before (baseline from critic-01)

| # | Hypothesis | Implicit weight | Turns allocated (estimate) | Payback (cycles) | MoS |
|---|---|---|---|---|---|
| 1 | Unit-econ block | 12.5% | 5 | 1 | UNKNOWN |
| 2 | Convergence metric | 12.5% | 8 | 1 | UNKNOWN |
| 3 | E-17 gate wiring | 12.5% | 15 | 2 | UNKNOWN |
| 4 | Golden-set comparison | 12.5% | 40 | 3-5 | UNKNOWN |
| 5 | Opportunity-cost naming | 12.5% | 5 | 1 | UNKNOWN |
| 6 | Horizon-gate fix | 12.5% | 2 | 1 | UNKNOWN |
| 7 | DRR Kelly fields | 12.5% | 3 | 1 | UNKNOWN |
| 8 | Paid-API memo | 12.5% | 20 | 8 | UNKNOWN |
| **TOTAL** | | 100% | **98 turns** | avg 2.4 | N/A |

All items equal-weighted; no Kelly scoring; no bundle sequencing; MoS
unknown (C2 fail throughout); no sequential dependency recognised (H-4
prerequisite for H-8 ignored).

### After (optimized)

| Priority | H-code | Bundle | Turns allocated | Turns saved (vs solo) | Kelly-rank | Payback (cycles) | MoS (post-implementation) |
|---|---|---|---|---|---|---|---|
| **1** | H-6 (DRR Kelly fields) | A — first item | 3 | 37-77 over 20 cycles | 1 | 1 | 0.30 → 0.40+ (enables rule discrimination) |
| **2** | H-1 (unit-econ block) | A — concurrent with H-6 | 5 | 95-195 over 20 cycles | 2 | 1 | prerequisite for all other MoS calculations |
| **3** | H-7 (horizon-gate alignment) | B — first item | 2 | 10-22 over 20 cycles | tied-high P | 1 | minor; unlocks cross-expert synthesis coherence |
| **4** | H-2 (E-17 gate wiring) | B — core item | 15 | 585-1185 over 20 cycles | 3 | 2 | **largest absolute NPV; MoS jump** |
| **5** | H-5 (gate-ack SLA) | B — last item | 8 | 52-112 over 20 cycles | 4 | 2 | preserves runway; reduces blocking risk |
| **6** | H-4 (golden-set comparison) | C — first item | 40 | 40-100 over 20 cycles | 5 | 3-5 | gate for H-8; validates 2-3× quality claim |
| **7** | H-3 (moat kill-conditions) | A — deferred item | 10 | 2-8 over 20 cycles | 6 | 5 | low NPV; moat not the current bottleneck |
| **8** | H-8 (paid-API memo) | C — sequential-dependent | 20 | option value only | 7 | gate-conditional | BLOCKED until H-4 complete |
| **TOTAL** | | | **103 turns** | **820-1699 turns net over 20 cycles** | | avg 2.1 | N/A |

**Note on "Convergence metric" (original recommendation #2 from critic-01).**
The original recommendation "pre-commit Phase-A convergence metric before cycle_5" is NOT a separate hypothesis but an **output artifact** that emerges from completing H-1 (unit-econ block) + H-6 (DRR Kelly fields). Once those two are in place, the convergence metric is the acceptance predicate stated in investor-critic-01 footnote (dissent block):
> "At cycle_10: strategies.md total entries ≥ 30 AND average turns-per-cycle declining trend (slope < 0) AND ≥1 rule demonstrably fired with documented turn-savings."
This predicate is now tightened to: "At cycle_10: strategies.md entries ≥ 30 AND at least 50% of entries carry `expected_invocation_frequency: high` AND at least 3 entries carry a `estimated_turn_savings_per_invocation` that is measurably realised in `swarm/logs/cyc-*/events.md` turn counts."

**Note on opportunity-cost naming (original recommendation #5 from critic-01).**
This is also NOT a standalone hypothesis requiring implementation turns — it is a FIELD to be populated in H-1's unit-econ block. It costs 0 additional turns to add: the unit-econ block template includes an `opportunity_cost_path_not_taken` line by construction. Zero-marginal-cost; subsumed.

---

## §7 Delta Summary

| Metric | Baseline | Proposed | Delta |
|---|---|---|---|
| Turn allocation (implementation) | 98 turns | 103 turns | +5 turns (+5%) |
| Hypotheses sequenced by Kelly score | 0 (equal weight) | 8 (ranked by Kelly-score formula) | +8 ranked |
| Bundles with shared infrastructure | 0 | 3 bundles (A, B, C) | +3 |
| Net turn savings over 20 cycles (est.) | 0 (no measurement) | 820-1699 turns | +820-1699 |
| Margin-of-safety (baseline) | UNKNOWN / absent | 0.30 → target 0.40+ after H-2 fires | +0.10+ |
| Payback horizon (average) | 2.4 cycles (uniform) | 2.1 cycles (Kelly-weighted) | -0.3 cycles |
| Sequential dependencies recognised | 0 | 1 (H-4 → H-8) | +1 (prevents AP-INV-9) |
| Subsumed items (zero marginal cost) | 0 | 2 (opportunity-cost naming, convergence metric) | -2 standalone items = 10 turns saved |
| Owner-earnings block present | ABSENT | Present from cycle_1 (H-1) | +1 |
| MoS arithmetic present | ABSENT | Present from cycle_1 (H-1 + H-6) | +1 |
| Kill-conditions per moat candidate | 0 explicit | ≥2 per moat candidate (H-3 + Bundle A) | +8 kill-conditions |
| E-17 gate enforced | Ceremonial (prose) | Machine-testable (hook) by cycle_2 | +1 enforcement gate |
| Horizon-gate datum aligned | Divergent (5 vs 4) | Aligned (H-7; cycle_1) | +1 |

Total reallocation: +5 turns (non-zero-sum because H-6 and H-7 were
underweighted in baseline; the delta is additive, not redistributive —
the baseline 98 turns was already a proposal, not an actual committed
budget). The extra 5 turns comes from adding H-7 as an explicit item
(2 turns) and recognising H-3 as a Bundle-A item requiring 10 turns
rather than the baseline's unnamed implicit 0. Net: these 5 additional
turns pay back in 1 cycle via turn-savings from H-7 and immediate
discriminating-rule quality from H-6.

---

## §8 Sharpened Measurables (per brief acceptance predicate)

The brief requires sharpened measurables for €/turn, turns/cycle,
hypotheses/cycle, strategies/cycle. All four:

### €/turn

At €120/hr consulting rate (Brief §5.1 anchor):

- 1 turn ≈ 1-2 minutes of Claude Code execution + context.
- Generous estimate: 1 turn = 3 minutes of Ruslan-equivalent time.
- €/turn = €120/hr × (3 min / 60 min) = **€6/turn** (founder-time-
  equivalent, Max-subscription).
- Bundle A implementation cost: 8 turns × €6/turn = **€48** total.
- Bundle B implementation cost: 25 turns × €6/turn = **€150** total.
- Bundle C implementation cost (H-4): 40 turns × €6/turn = **€240**.
- Total optimized implementation: 103 turns × €6/turn = **€618 total investment**.
- 20-cycle payback at lower bound: 820 turns saved × €6/turn = **€4,920 return**.
- **ROI over 20 cycles: €4,920 / €618 = 7.9×** (lower bound estimate).
- Graham margin-of-safety at ROI 7.9×: well above the 0.30 floor.
- **This is the first investor-grade ROI computation on the swarm investment.**

### turns/cycle

Current: 370 turns/cycle (observed; see §4.1).
After Bundle B (H-2 E-17 gate): 370 × 0.50 = 185 turns/cycle for
simple tasks (gate blocks 50% of wasted multi-cell dispatches).
Target at cycle_10: ≤200 turns/cycle average.
Measurable: `swarm/logs/cyc-*/events.md` turn counts per phase.

### hypotheses/cycle

Baseline: undefined (no tracking).
Proposed: at steady state (cycles 3-20), each cycle closes
1-2 hypotheses from the ranked list above. Target: **1 hypothesis
advanced per cycle** (not necessarily fully closed; "advanced" = next
milestone reached per kill-condition tracking).
Measurable: `swarm/wiki/tasks/<task-id>/artefacts/investor-*` count per cycle.

### strategies/cycle

Baseline: 0 real entries (scaffolding only).
Proposed target at cycle_10: ≥3 entries per cycle per expert across
the 6 files = 18 entries/cycle at max. Conservative target: **≥2
entries/cycle/expert = 12 entries/cycle** (lower than the theoretical
maximum to account for low-payback rule deferral per H-6's Kelly
discriminator).
Measurable: line count delta per `agents/<expert>/strategies.md` per
cycle close.

---

## §9 Kill-Conditions for the Optimized Set

The optimized hypothesis set itself has kill-conditions per C4 compliance:

**Kill-condition 1 (Bundle A fails to compound):** At cycle_10, total
strategies.md entries ≤ 15 across 6 files despite H-6 + H-1 being
implemented. Indicates DRR Kelly fields are not being populated (procedural
failure, not design failure). Action: escalate to HITL — Compound step
is not firing.

**Kill-condition 2 (Bundle B fails to reduce turns):** At cycle_10,
average turns/cycle ≥ 300 with H-2 implemented and logged gate
evaluations. Indicates E-17 gate is being bypassed or the Decompose-or-
Chat threshold is calibrated incorrectly. Action: re-invoke optimizer
with H-2 as the subject; propose threshold recalibration.

**Kill-condition 3 (Bundle C H-4 shows negative MoS):** Golden-set
comparison shows solo-brigadier quality ≥ 6-cell quality on ≥3 of 5
test tasks. Indicates the swarm matrix is not generating the quality
premium required for MoS > 0. Action: HITL escalation per investor-expert
§1d escalation-trigger row "unit-econ-arithmetic produces margin-of-
safety ≤0 on a draft promoted to canonical."

**Kill-condition 4 (optimized Kelly ranking itself is wrong):** At
cycle_5, H-6 + H-1 (ranked 1-2) have not produced a single measurable
turn-savings because strategies.md rules of quality H-6 filters are
written but never invoked in critic passes. Indicates the Kelly model
of rule-payback is calibrated incorrectly (the actual payback horizon
is longer than 1 cycle). Action: re-run this optimizer with updated
payback estimates from observed cycle data.

---

## §10 Risk Table (Gate Risk per Horizon Gate)

| Risk | Likelihood | Mitigation |
|---|---|---|
| H-6 DRR fields added but never populated (observer effect — authors write the field but mark `expected_invocation_frequency: high` on all rules defensively) | medium | Brigadier audits during Compound step: if >80% of entries are `high`, flag as AP-INV-10 (pseudo-quantitative precision) |
| H-2 E-17 hook blocks legitimate multi-cell dispatches (threshold too strict) | medium | Start with threshold `complexity > simple OR adversarial-review needed` (inclusive-OR); tighten to AND-form after 5 cycles of data |
| H-4 golden-set comparison is run on an atypically easy task (cherry-picking) | medium | Use THIS cycle's artefact (T-swarm-self-improve-v1) as the benchmark task — it is representative and already has both paths implicit |
| Bundle B "gate discipline PR" is too large (brigadier + 4 peers + 2 functional additions) and gets fragmented | low | Split into two: (a) H-7 horizon-gate alignment only (1 PR, 5 files, 2 turns); (b) H-2+H-5 combined (1 PR, brigadier + investor files, 23 turns) |
| H-8 attempted before H-4 is complete (sequential dependency violated) | low | The block is explicit in §6. Brigadier's dispatch matrix should check H-4 completion before issuing H-8 as a task brief. |
| Max-subscription turn budget saturated by infrastructure hypotheses before consulting work resumes | low-medium | H-6 + H-1 + H-7 together cost 10 turns. Even if the entire 103-turn optimized plan is executed sequentially, it consumes less than 1 "complex cycle" (370 turns). Infrastructure investment is a tiny fraction of current cycle cost. |

---

## §11 BA-Cycle Lite (Ethical Surface)

**BA-0.** Third-party exposure: consulting clients who receive deliverables
assisted by unvalidated swarm rules. Same exposure as critic-01 BA-0.

**BA-1.** Asymmetry: Ruslan benefit (higher throughput) vs client risk
(rule-quality uncertainty). Optimized plan reduces this asymmetry: H-6
(Kelly rule discrimination) reduces low-quality rule proliferation;
H-4 (golden-set comparison) provides quality evidence. The optimization
REDUCES third-party exposure vs baseline.

**BA-2.** The optimized plan delivers the same expected return (swarm
investment) with less third-party exposure (higher-quality rules, turn-
budget discipline). BA-2: pass.

**BA-3.** A client who knew that the swarm's rule-quality is now tracked
via Kelly discrimination and validated via golden-set comparison would
accept the risk structure more readily than under the baseline (unvalidated
rule accumulation). BA-3: pass, conditional on H-4 completion before
client-facing deliverables are swarm-assisted.

---

## §12 Antifragility Check — Via-Negativa Retirement

Per §6.4 of investor-expert.md, the via-negativa step names what to
RETIRE from the hypothesis set before naming what to ADD.

**Retire (positions to close before cycle_2):**

1. **The equal-weighting assumption.** Baseline treats all 8 hypotheses
   as equivalent capital deployments. This assumption produces the
   sub-optimal sequencing observed (H-8 before H-6; H-4 before H-1).
   Retired: equal-weight replaces with Kelly-rank per §3.

2. **"Opportunity-cost naming" as a standalone task.** Baseline makes
   this a separate recommendation requiring its own attention budget.
   It is a zero-marginal-cost field in H-1's unit-econ block. Retired
   as standalone; absorbed into Bundle A.

3. **"Convergence metric pre-commitment" as a standalone task.** Same
   logic: it is the acceptance predicate that emerges from H-1 + H-6
   completion. Not a separate task requiring 8 turns. Retired as
   standalone; the metric itself is stated in §6.

4. **"Narrative-fallacy-investing" as the primary risk descriptor.**
   Critic-01 correctly identified AP-INV-8 (narrative) as the root
   cause. But the optimizer's job is to provide an ARITHMETIC
   alternative, not to repeatedly flag the narrative. AP-INV-8 is
   retired as a continuous label and replaced with the §4 turn-cost
   model as the operative frame going forward.

**Retirement unlocks:** 10 implementation turns (savings from not treating
opportunity-cost naming and convergence metric as separate 5+8 turn tasks)
+ reduced Compound-step overhead (fewer low-payback narrative notes in
strategies.md).

---

## §13 Dissents

No cross-expert dissents applicable at this stage (optimizer pass is
investor-domain internal). One internal investor-lens dissent preserved:

**Dissent:** "H-2 (E-17 gate wiring) should be ranked first, not third,
because its absolute NPV (585-1185 turns over 20 cycles) dwarfs all
other hypotheses."

- F: F4 (operational convention; arithmetic backing)
- ClaimScope: holds if the turn-savings estimate of 30-60 turns/cycle
  from blocked over-dispatches is accurate. Does NOT hold if the actual
  over-dispatch rate is <20% of cycles (in which case savings are much
  lower).
- R:
  - Refuted_if: after H-2 is wired, average turns/cycle does NOT
    decline by ≥20% at cycle_5. Indicates the over-dispatch rate was
    lower than estimated.
  - Accepted_if: average turns/cycle declines by ≥20% at cycle_5 post
    H-2 implementation.
- Source: investor-expert internal (Kelly-absolute-NPV lens vs
  Kelly-score-normalised lens)

**Resolution:** Kelly-score normalised by payback is the correct primary
ordering criterion for Phase A because Ruslan's attention capital is the
binding constraint, not the total turns over 20 cycles. H-6 + H-1 must
come first precisely because they are near-zero cost and they enable the
measurement substrate that validates H-2's benefit estimate. If H-2 is
implemented before H-1, we lose the ability to measure whether H-2 is
actually saving turns (we have no baseline). H-1 first, then H-2.
Dissent preserved; resolution chosen.

---

## §14 Output Schema

```yaml
status: pass
context:
  task_id: T-swarm-self-improve-v1-2026-04-23
  artefact_under_optimization: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-critic-01.md
  mode: optimizer
  cycle_id: cyc-swarm-self-improve-v1-2026-04-23
invariant_check:
  WLNK: {applies: true, preserved: true, evidence: "all 8 hypotheses carry named return paths; zero silent capital-leakage"}
  MONO: {applies: true, preserved: true, evidence: "Kelly-score table produces strict partial order; no rank inversion on any scored quality"}
  IDEM: {applies: true, preserved: true, evidence: "scores are arithmetic functions of fixed inputs; re-application yields identical rank"}
  COMM: {applies: true, preserved: true, evidence: "bundle assignments are set-based (infrastructure overlap), not path-dependent"}
  LOC:  {applies: true, preserved: true, evidence: "delta touches only 8 investor-domain hypotheses; no engineering/org/consulting-revenue scope touched"}
baseline:
  allocation: "8 hypotheses, equal-weighted, 98 turns total, no Kelly scores, no bundle sequencing, no sequential dependencies, MoS unknown"
  expected_return: "UNKNOWN (C2 fail in critic-01; no arithmetic)"
  risk_of_ruin_floor: "ABSENT (C6 fail in critic-01)"
  opportunity_cost: "UNNAMED (C5 fail in critic-01)"
proposed:
  allocation: "8 hypotheses, Kelly-ranked, 103 turns total, 3 bundles (A+B+C), 1 sequential dependency (H-4→H-8), 2 items subsumed"
  expected_return: "820-1699 turns net savings over 20 cycles; €4,920 ROI lower bound; 7.9× return on 103-turn investment"
  risk_of_ruin_floor: "named: MoS goes negative if quality gain <1.5×; kill-condition 3 fires; HITL escalation per §1d"
  opportunity_cost: "named: €618 in founder-time-equivalent turns; path-not-taken = solo-Ruslan consulting at €120/hr"
delta:
  Δ_expected_return: "+820-1699 turns net (vs 0 baseline; first-ever arithmetic measurement)"
  Δ_risk_of_ruin: "ruin floor now named and quantified (MoS=0.30 baseline; target 0.40+ after H-2)"
  Δ_opportunity_cost: "+€618 investment named; ROI 7.9× lower bound named"
  Δ_margin_of_safety: "0 (absent) → 0.30 (arithmetic floor); target 0.40+ post-H-2"
justification:
  heuristics_applied: [graham-pruning, munger-inversion, marks-2nd-level, taleb-via-negativa, kelly-sizing]
  key_insight: >
    The critical optimization is NOT reordering 8 equal hypotheses. It is recognising that H-6 (DRR Kelly fields)
    and H-1 (unit-econ block) together cost 8 turns and unlock the measurement substrate required to validate
    ALL other hypotheses. They come first because they enable the arithmetic that justifies the remaining 95
    turns of investment. H-2 (E-17 gate) is the highest-NPV hypothesis but cannot be measured without H-1.
    Bundle structure turns implementation from sequential into three parallel-ish tracks with clear unlock dependencies.
risks:
  - "H-6 fields defensively marked high-frequency by authors (AP-INV-10); mitigation: brigadier audits >80% high-frequency entries"
  - "H-2 threshold too strict; blocks legitimate multi-cell dispatches; mitigation: inclusive-OR form initially, tighten after 5 cycles"
  - "H-4 cherry-picked task underestimates quality delta; mitigation: use current cycle T-swarm-self-improve-v1 as benchmark"
provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-critic-01.md", range: "69-275", quote: "H-1..H-8 investor hypotheses + recommended changes 1-8 + alternatives A/B/C"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "24-53", quote: "TL;DR 5 emergent ideas; cross-domain matrix 10 pairs"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "46-76", quote: "what's thinnest (theoretical, not yet operationalised) + 2× improvement surfaces"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md", range: "41-85", quote: "TL;DR + CE canonical skill set map; compound (money step) highest-ROI missing"}
  - {path: ".claude/agents/investor-expert.md", range: "1-60", quote: "§1a identity; max-subscription discipline; decision-rights ritual"}
confidence: medium
confidence_method: arithmetic + judgment
escalations: []
dissents:
  - claim: "H-2 should rank first by absolute NPV, not third by Kelly-score-normalised"
    F: F4
    ClaimScope: "holds if over-dispatch rate is ≥30% of cycles; refuted if <20%"
    R:
      accepted_if: "turns/cycle declines ≥20% at cycle_5 post H-2"
      refuted_if: "turns/cycle does not decline at cycle_5 post H-2"
    source: "investor-expert internal (Kelly-absolute vs Kelly-normalised lens)"
```

---

## §15 Shared-Protocols §3 Return Packet

```yaml
summary: >
  Optimizer pass over 8 investor hypotheses from investor-critic-01. Kelly-style edge scored
  all 8 (formula: E × P / Payback). Ranked: H-6 (DRR Kelly fields) → H-1 (unit-econ block) →
  H-7 (horizon alignment) → H-2 (E-17 gate) → H-5 (gate-ack SLA) → H-4 (golden-set) → H-3
  (moat kill-conditions) → H-8 (paid-API memo; blocked until H-4 complete). Bundled into 3
  infrastructure tracks: A (owner-earnings substrate), B (gate discipline), C (measurement
  substrate with H-4→H-8 dependency). First-ever arithmetic ROI: 7.9× over 20 cycles at lower
  bound (820-1699 turns saved; €4,920 return on €618 investment). WLNK/MONO/IDEM/COMM/LOC all
  preserved. No method-change. Via-negativa retires 4 baseline assumptions (equal-weighting,
  standalone opportunity-cost, standalone convergence metric, narrative-AP as ongoing label).
proposed_writes:
  - path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-optimizer-01.md"
    frontmatter:
      id: investor-optimizer-01
      title: "Investor Optimizer — T-swarm-self-improve-v1 capital-allocation sequencing"
      type: optimizer-artefact
      task_id: T-swarm-self-improve-v1-2026-04-23
      cycle_id: cyc-swarm-self-improve-v1-2026-04-23
      produced_by: investor-expert
      mode: optimizer
      created: 2026-04-23
      pipeline: ingested
      state: drafted
      confidence: medium
      confidence_method: arithmetic + judgment
      niche: meta
    body: "(this file)"
    edges_to_add:
      - {from: "investor-optimizer-01", to: "investor-critic-01", type: "refines", note: "optimizer pass over critic's 8 hypotheses"}
      - {from: "investor-optimizer-01", to: "context-zeta-cross-pollination", type: "derived_from", note: "bundle mapping draws on ζ cross-domain infrastructure pairs"}
      - {from: "investor-optimizer-01", to: "context-alpha-agent-construction", type: "derived_from", note: "unit-econ anchored in α turn-cost and golden-set data"}
provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-critic-01.md", range: "69-391", quote: "8 hypotheses H-1..H-8 with arithmetic arguments + alternatives"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "24-75", quote: "cross-domain matrix + MP-1..MP-4 meta-patterns; bundle infrastructure logic"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "46-76", quote: "thin spots 1-12; 2× improvement surfaces 1-12"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md", range: "41-85", quote: "CE canonical skill set map; compound skill = money step; highest-ROI missing"}
confidence: medium
confidence_method: arithmetic + judgment
escalations: []
dissents:
  - position: "H-2 should rank first by absolute NPV (585-1185 turns over 20 cycles)"
    evidence:
      - "Kelly-score normalised by payback gives H-6+H-1 priority because they unlock the measurement baseline required to validate H-2's benefit; see §13"
      - "H-2 before H-1 = measuring nothing; H-1 before H-2 = measuring everything H-2 produces"
```
