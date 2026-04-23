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
