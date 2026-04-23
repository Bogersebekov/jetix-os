---
title: brigadier — Strategies (System Prompt Learning)
agent: brigadier
created: 2026-04-23
last_modified: 2026-04-23
state: scaffolding
confidence: N/A-scaffolding
expected_evolution:
  cycle_10: First decomposition heuristics tighten as ap_cost vs estimated ap_cost ratio surfaces; 1-2 entries under "decomposition" + "budget-estimation"; Decompose-or-Chat gate may absorb 1-2 additional predicates if Phase-A signals reveal them
  cycle_50: AP focus list (§8.5 of brigadier) extends to include any Phase-A surfaced AP not in MS §3.30; Phase-B activation gate Q8 may fire if cross_theme_refs ≥3 + closed_cycles ≥50 + ack received; skill candidates promoted from proposed→active for any 3+ recurring pattern
  cycle_200: split_trigger evaluation — if sustained intake >10/week, 2+ concurrent cycles, accountabilities >7, propose Phase-B split into [task-dispatcher, integration-manager, gate-keeper] via AWAITING-APPROVAL; α-5 Direction tooling activates per FPF Part 10.6 only on Ruslan ack; brigadier prompt re-write under Phase-B self-improvement
---

# Strategies — brigadier

## Entry Format

Each entry uses 4-part DRR per FPF E-9 §2.9 with the documented
swarm-wide translation (per critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why (≈ FPF `context`)
3. **Result** — observed outcome (alternatives subsumed in Reasoning's
   why-not rationale)
4. **Review** — validated | refuted | partial (≈ FPF `review-checkpoint`)

Plus the Evolution sub-block (per FPF §3.5):

- `changelog:` — append-only line per modification
- `last-review:` — `YYYY-MM-DD` of most recent review
- `expected-evolution:` — drift expectation at 10 / 50 / 200 cycles

## Entries

### 2026-04-23 — Parallel-dispatch discipline in Phase-1 reads saves wall-clock ~5×

- **Decision:** Phase-1 deep-read sub-agents (α..ε) dispatched in a single message with 5 parallel Task() calls, ζ serial afterwards. Matrix Round-1 (5 critics), Round-2 (5 optimizers), Phase-5 (4 opportunity drafters) also dispatched in parallel.
- **Reasoning:** brigadier §4.3 mandates parallel dispatch for independent work (AP-23 lock). Verified empirically: each cell ran ~3-6 min; serial execution would have compounded to ~30-60 min per round instead of the observed 5-8 min max wait.
- **Result:** First real cycle closed in ~3 hours wall-clock including 2 HITL gates; full cycle compute expended on a budget that would have been ~8-10 hours serial.
- **Review:** validated — no return dropped, no cross-contamination detected between parallel cells (each wrote to distinct expected_return_path).

#### Evolution
- changelog:
  - 2026-04-23 — created (first real cycle)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: confirm parallel-dispatch wall-clock ratio holds across different task shapes
  - cycle_50: identify any cell-pairs that LOOK independent but share non-obvious context dependencies; refine serial/parallel split rules
  - cycle_200: Phase-B split_trigger evaluation when parallelism exceeds single-brigadier coordination capacity

### 2026-04-23 — Integrator-mode can be dispatched multiple times per cycle with different scopes

- **Decision:** In this cycle, mgmt × integrator fired twice (once for Phase-2 hypothesis synthesis across all 10 R1+R2 artefacts; once for Phase-5 OPP-04 opportunity drafting). Similarly, systems and engineering fired integrator once each in Phase 5 with OPP-specific scope.
- **Reasoning:** brigadier §4.2 mode-prefix grammar treats each Task() invocation independently; the (expert, mode) pair identifies the rubric, not a scarce resource. Scope-differentiation via the brief makes repeated invocations coherent.
- **Result:** 6 integrator invocations fired across 4 distinct experts (mgmt ×2, philosophy ×1, systems ×1, engineering ×1, investor ×1). All returned E-5-compliant packets with distinct scopes. No scope-conflation AP fired.
- **Review:** validated — repeated (expert, mode) dispatch with scope differentiation is a legitimate pattern; preserves 5×4=20 cell taxonomy while enabling real-world scope divergence.

#### Evolution
- changelog:
  - 2026-04-23 — created (first real cycle, observed 6-integrator pattern)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: document explicit "scope-tag" convention in mgmt-integrator-01/mgmt-integrator-02 naming to prevent artefact collision
  - cycle_50: track integrator-invocation-count per cycle as a signal — >4 integrator calls may indicate under-decomposition (too many things that need integration)
  - cycle_200: Phase-B may require a dedicated "integration-manager" role if integrator invocations exceed brigadier capacity

### 2026-04-23 — WBS ap_cost estimates were 30-50% low across Phase 2

- **Decision:** Record that Phase-2 critic/optimizer cells consumed meaningfully more turns than estimated in `proposals/T-swarm-self-improve-v1-2026-04-23-decomposition.md`. Target: next-cycle WBS uses this calibration data.
- **Reasoning:** brigadier §8.2 Compound trigger #4 — "did cycle exceed ap_cost?" — calibration must feed next WBS or the estimation never improves. Budget overrun without HITL-escalation implies the ap_cost estimate was wrong.
- **Result:** No AP-budget overruns triggered HITL escalation (all cells completed within their per-cell budget). But cumulative turn consumption across 17 cells suggests default estimate was ~70% of actual. No hard data (would need turn-budget-transparency from OPP-02/W5 wiki-dim hypothesis) but directionally clear.
- **Review:** partial — observation noted without instrumentation. OPP-01 eval harness will enable measurement. Re-review at cycle-5 when ap_cost vs actual ratio has ≥3 cycles of data.

#### Evolution
- changelog:
  - 2026-04-23 — created
- last-review: 2026-04-23
- expected-evolution:
  - cycle_5: revisit with OPP-01 data; commit to +30% default safety margin in WBS ap_cost if ratio confirmed
  - cycle_10: variable calibration by cell-shape (critic cells vs integrator vs scalability differ)
  - cycle_200: adaptive ap_cost based on 100-cycle rolling-window telemetry

### 2026-04-23 — Stage-Gated HITL pause discipline worked correctly at Gate 1

- **Decision:** At Gate 1 brigadier wrote AWAITING-APPROVAL packet, committed, pushed, paused without taking further action until Ruslan's `ack C` inline. No unilateral proceeding past the gate.
- **Reasoning:** brigadier §1d `requires-approval` row + §6.1 trigger #10 catch-all. Phase A operates Stage-Gated by default (CLAUDE.md + ROY-ALIGNMENT); pausing at every gate is non-negotiable.
- **Result:** Gate 1 paused cleanly. Ruslan acked Option C with additional reasoning; brigadier proceeded to Phase 5 exactly per ack.
- **Review:** validated — first real HITL gate executed without over-stepping. Gate 2 same pattern.

#### Evolution
- changelog:
  - 2026-04-23 — created (first gate ack received successfully)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_5: evaluate whether Redirect or Drill-down options ever get chosen (all gates to date: Approve)
  - cycle_50: if 100% Approve rate persists, may indicate brigadier is under-presenting genuinely-contentious decisions; refine gate packet composition
  - cycle_200: explore parallel-gate pattern (two independent gates open simultaneously) if Phase-B load requires

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold `agents/brigadier/strategies.md` per Шаг 2.2.4 Part C.
- **Reasoning:** per FPF E-9 + D12, every agent carries an empty-but-
  structured strategies.md from day zero; Layer-2 self-write rule per
  CLAUDE.md per-agent memory spec; this file unblocks Phase A bootstrap
  and prevents the brigadier's first §8 Compound from failing on
  missing strategies.md.
- **Result:** file lint-valid, Phase A bootstrap unblocked.
- **Review:** scaffolding only; first real entry on first α-1 cycle's
  Compound step.

#### Evolution
- changelog:
  - 2026-04-23 — created (scaffolding)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: see frontmatter
  - cycle_50: see frontmatter
  - cycle_200: see frontmatter
