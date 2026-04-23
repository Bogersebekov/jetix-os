---
title: engineering-expert — Strategies (System Prompt Learning)
agent: engineering-expert
created: 2026-04-23
last_modified: 2026-04-23
state: scaffolding
confidence: N/A-scaffolding
expected_evolution:
  cycle_10: 5–10 refactor-rules accumulated; critic false-positive rate baselined; ≥1 entry on optimizer-vs-critic mode-confusion observed-in-cycle
  cycle_50: First mode-confusion audit; §3/§4 rubrics refined from observed critic-vs-optimizer drift; Ousterhout deep-module checklist adjusted on per-domain feedback
  cycle_200: Split-trigger evaluation per §1d — consider splitting into code-expert + architecture-expert if artefact-mix >60/40 sustained over 3 consecutive cycle_50 windows AND dispatch-rate >20 cells/week × 3 weeks
---

# Strategies — engineering-expert

## Entry Format

Each entry uses 4-part DRR per FPF E-9 §2.9 with the documented
swarm-wide translation (critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why (≈ FPF `context`)
3. **Result** — observed outcome (alternatives subsumed in Reasoning's
   why-not rationale)
4. **Review** — validated | refuted | partial (≈ FPF `review-checkpoint`)

Plus Evolution sub-block per FPF §3.5.

## Entries

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold `agents/engineering-expert/strategies.md` per
  Шаг 2.2.4 Part C.
- **Reasoning:** Layer-2 self-write rule per CLAUDE.md; FPF E-9 + D12
  mandate empty-but-structured strategies.md from day zero.
- **Result:** file lint-valid, Phase A bootstrap unblocked.
- **Review:** scaffolding only; first real entry on first cycle this
  expert participates in.

#### Evolution
- changelog:
  - 2026-04-23 — created (scaffolding)
- last-review: 2026-04-23
- expected-evolution: see frontmatter
