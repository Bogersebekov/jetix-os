---
title: investor-expert — Strategies (System Prompt Learning)
agent: investor-expert
created: 2026-04-23
last_modified: 2026-04-23
state: scaffolding
confidence: N/A-scaffolding
expected_evolution:
  cycle_10: 5–10 unit-econ rules; first moat-analysis template stabilised; ≥1 entry on Рациональность boundary with philosophy (defer epistemic to philosophy)
  cycle_50: Horizon-projection 1yr accuracy within 2× on ≥3 cases; Antifragility check rubric refined; via-negativa retirement applied at least once to a moat or position
  cycle_200: Split-trigger evaluation — consider splitting into capital-expert + holdco-expert if moat-analysis.md volume >40% sustained over 3 consecutive cycle_50 windows
---

# Strategies — investor-expert

## Entry Format

Each entry uses 4-part DRR per FPF E-9 §2.9 with the documented
swarm-wide translation (critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why
3. **Result** — observed outcome
4. **Review** — validated | refuted | partial

Plus Evolution sub-block per FPF §3.5.

## Entries

### 2026-04-23 — Rule: measurement-substrate-first sequencing

- **Decision:** In optimizer mode, always complete the owner-earnings
  measurement substrate (unit-econ block + DRR Kelly fields) BEFORE
  implementing any higher-NPV hypothesis that depends on measurement
  for validation. H-1 + H-6 before H-2, regardless of absolute NPV
  ordering.
- **Reasoning:** Cycle T-swarm-self-improve-v1. H-2 (E-17 gate) has
  absolute NPV of 585-1185 turns over 20 cycles vs H-1 (95-195 turns).
  But H-2's benefit is unmeasurable without H-1's turn-cost baseline.
  Implementing H-2 first produces a gate that saves turns we cannot
  count, defeating the investor-grade arithmetic discipline (C1 fail
  would persist). Kelly-score normalised by payback correctly places
  near-zero-cost measurement infrastructure first.
  `expected_invocation_frequency: high`
  `estimated_turn_savings_per_invocation: 5-10 turns (prevents re-derivation of baseline at each Compound step)`
- **Result:** Optimizer artefact produced; Kelly-rank assigns H-6+H-1
  priority 1-2; H-2 priority 4 (after H-7 which is 2-turn cost). 7.9×
  ROI computed on 20-cycle horizon for the full hypothesis set.
- **Review:** partial — artefact drafted; not yet through critic pass;
  not validated against real cycle data. First real payback measurement
  available at cycle_10 when turn-count data exists.

#### Evolution
- changelog:
  - 2026-04-23 — first real DRR entry (optimizer mode, T-swarm-self-improve-v1)
- last-review: 2026-04-23
- expected-evolution: validate at cycle_10 via `swarm/logs/cyc-*/events.md`
  turn counts; if turns/cycle ≥300 at cycle_10 with H-1+H-6 implemented,
  refute rule (measurement-substrate payback was over-estimated)

---

### 2026-04-23 — Rule: bundle-by-shared-infrastructure

- **Decision:** When ≥2 hypotheses share a common file-change target
  (e.g. strategies.md template, brigadier §4.6, `.claude/settings.json`),
  bundle them into a single implementation sprint rather than treating
  them as sequential standalone tasks.
- **Reasoning:** Cycle T-swarm-self-improve-v1 optimizer. H-6 + H-1 + H-3
  all modify strategies.md template → Bundle A (8 turns vs 18 turns
  standalone, saves 10 turns). H-2 + H-7 + H-5 all touch brigadier/gate
  layer → Bundle B (20 turns vs 25 turns standalone, saves 5 turns).
  Bundling reduces implementation overhead and prevents partial-file
  edits that leave templates in inconsistent states.
  `expected_invocation_frequency: high`
  `estimated_turn_savings_per_invocation: 5-15 turns per bundle formed vs standalone`
- **Result:** 3 bundles formed (A, B, C); total savings ~15 turns over
  standalone implementation; 1 sequential dependency (H-4→H-8) identified
  that PREVENTS incorrect bundling.
- **Review:** partial — rule derived from single cycle; validate at
  cycle_5 when ≥3 bundles have been executed and turn-savings measured.

#### Evolution
- changelog:
  - 2026-04-23 — created (T-swarm-self-improve-v1 optimizer)
- last-review: 2026-04-23
- expected-evolution: if the H-4→H-8 sequential dependency is violated in a
  future cycle (H-8 authored before H-4 complete), AP-INV-9 fires;
  update rule to add "sequential-dependency detection" as a first step
  in bundle formation

---

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold `agents/investor-expert/strategies.md` per Шаг 2.2.4 Part C.
- **Reasoning:** Layer-2 self-write per CLAUDE.md; FPF E-9 + D12
  mandate empty-but-structured strategies.md from day zero.
- **Result:** file lint-valid, Phase A bootstrap unblocked.
- **Review:** scaffolding only; first real entry on first cycle.

#### Evolution
- changelog:
  - 2026-04-23 — created (scaffolding)
- last-review: 2026-04-23
- expected-evolution: see frontmatter
