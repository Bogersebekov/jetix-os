---
id: horizon-convergence
title: Horizon Convergence (S-06)
type: meta-metric
layer: spine
niche: meta
created: 2026-04-24
last_modified: 2026-04-24
pipeline: ingested
state: drafted
confidence: high
confidence_method: brigadier-attested-with-3-supports
tier: core
produced_by: brigadier
sources:
  - {path: "decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md", range: "§6 HD-01"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-scalability-01.md", range: "§6 5-gate vs 4-gate"}
  - {path: "prompts/cycle-2-implementation-2026-04-24.md", range: "Part D D.4"}
related: []
binding_scope: swarm-wide
purpose: "Track convergence of horizon-gate references across all 5 expert agents + brigadier per HD-01 Option C."
---

# Horizon Convergence (S-06)

Per **HD-01 Option C** (Ruslan ack 2026-04-24, cycle-2-impl): every
scalability-mode agent references the same 5-gate set — **€50K (current
baseline) / €200K / €1M / $100M / $1T**. Investor-expert already aligned
on 5 gates pre-cycle-2; the 4 peer experts + brigadier acquired the €50K
gate in cycle-2-impl Part D.

## S-06 convergence table

| Agent | €50K | €200K | €1M | $100M | $1T | Convergence |
|---|---|---|---|---|---|---|
| brigadier | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 |
| engineering-expert | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 |
| mgmt-expert | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 |
| systems-expert | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 |
| philosophy-expert | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 |
| investor-expert | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 (aligned pre-cycle-2) |

**Status (cycle-2-impl 2026-04-24):** S-06 convergence = **6/6 agents on
5/5 gates** after HD-01 Option C landed.

## Rationale

**Why €50K is Ruslan's single committed absolute date (Q2 2026):** per
`decisions/JETIX-PLAN.md` D3. Every scalability projection names a home
gate at €50K so the swarm is explicitly anchored to the current state
(solo-founder + Max-subscription + 6-agent Phase A), not projecting from
an undated "Phase A" into future gates only.

**Why 5 gates, not 4:** per `systems-scalability-01.md` §6 verdict — the
5-gate model is more scalability-coherent: every OPP has a named home
gate, BOSC-A-T-X first-trigger statements are grounded in the current
capital reality, and the cross-expert integration risk (investor-critic
H-7 + mgmt-integrator D-05 horizon-gate divergence) is eliminated.

**Cost:** one nominal state declaration. Not a blocking gate-ack; just a
named anchor.

## Verification

After cycle-2-impl Part D commit, the following predicates hold:

```bash
# All 6 agent files reference €50K
test "$(grep -lE '€50K' .claude/agents/{brigadier,engineering-expert,mgmt-expert,systems-expert,philosophy-expert,investor-expert}.md | wc -l)" -eq 6

# All 4 peer experts + brigadier now reference the 5-gate string in §6 predicates
# and BOSC-A-T-X tables; investor-expert pre-aligned on 5 gates (unchanged).
```

Part F-CHECK-5 validates this. Subsequent cycles should monitor that no
drift occurs (e.g., a future edit that accidentally removes €50K from one
agent). Lint check addition is a cycle-3+ sweep.
