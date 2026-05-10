---
agent: autoresearch-brigadier
type: strategies
created: 2026-05-11
updated: 2026-05-11
---

# Стратегии autoresearch-brigadier

Format: "When I encounter X, I do Y, because Z."
Append new strategies after each non-trivial cycle (newest on top).

This is the System Prompt Learning layer. Strategies accumulate from experience
and during major refactors migrate back into `system.md`.

## 2026-05-11 — Cycle 1 close (Ruslan ack post-pilot D.2 voice-lens)

Ruslan ack is the gated cycle close per Tier 2 R9. The following strategies
are promoted from the pilot experience (81 experiments, 8 KEEPs, 0 violations,
4 pause-restarts).

- **When propose loop hits N consecutive failures**, do not hard-halt: emit
  AWAITING-APPROVAL per Q9, then apply `diversity_jolt` (full weight reshuffle
  + threshold reset + ≥2 tier swaps) to escape local optimum. Because pure
  greedy single-operator mutation creates Karpathy's "creativity ceiling"
  pattern — escape requires mechanically distinct (not micro-tweak) moves.
  Validated in pilot: each of 4 pause-restarts produced ≥1 subsequent KEEP.

- **When recording DRR candidates**, never edit own `strategies.md`
  in-loop. Land them under `reports/autoresearch-*/drr-candidates/` as
  per-experiment markdown. Promotion into `strategies.md` only via gated
  cycle close (this entry counts). Because Tier 2 R9 + Part 6b §I.4 require
  human-gated self-modification.

- **When primary metric improves but secondary metrics regress**, REVERT
  (not KEEP) even if greedy primary delta is positive. Because Goodhart-style
  evaluator gaming is the foundational risk; secondary guard rails are the
  cheapest defense. Validated: 8/8 KEEPs improved primary *and* held or
  improved source diversity; no monkey-paw KEEPs surfaced.

- **When LLM share is 0.0 (programmatic-only)**, expect keep_ratio ≈ 10%
  on small mutation operators. Higher ratios suggest the mutation operator
  is too conservative (every change is locally good) → diversify. Lower
  ratios suggest the search space is too noisy or the regression guard is
  too tight → loosen.

- **Promotion shortlist** (Q-pilot-1 ack 2026-05-11) for D.2 voice-lens
  cycle 1: v00048, v00052, v00065, v00069 (top-4 by primary delta + secondary
  diversity improvement). These are queued for ≥3-cycle validation per Q4
  threshold; **no methodology promotion attempted at cycle 1**.

- **Next steps** (Ruslan-acked 2026-05-11):
  - Schedule D.2 cycles 2 + 3 to validate the 4-variant shortlist.
  - Re-run with `--llm-share 0.10` for LLM-creative mutation comparison.
  - D.4 / D.11 expansion deferred until D.2 hits Q4 threshold.

## 2026-05-11 (initial — Phase 1 MVP bootstrap)

- Q4 threshold for methodology promotion = ≥3 validated cycles (RUSLAN ack
  2026-05-11). Until that threshold is met, DRR candidates accumulate
  unpromoted.
- Tier 2 R9 prohibition reminder: this file is edited only via gated cycle
  close, never autonomously during the propose→eval loop.
