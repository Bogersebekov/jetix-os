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

## 2026-05-11 (initial — Phase 1 MVP bootstrap)

- (empty — accumulates after first 50-100 experiments on D.2 voice-lens pilot)
- DRR candidates emitted by the orchestrator land in
  `reports/autoresearch-karpathy-integration-2026-05-11/drr-candidates/` —
  NOT in this file directly. Promotion to this file happens via gated cycle close.
- Q4 threshold for methodology promotion = ≥3 validated cycles (RUSLAN ack
  2026-05-11). Until that threshold is met, DRR candidates accumulate
  unpromoted.
- Tier 2 R9 prohibition reminder: this file is edited only via gated cycle
  close, never autonomously during the propose→eval loop.
