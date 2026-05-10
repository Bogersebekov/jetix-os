---
experiment_id: exp-2026-05-11-d2-voice-lens-pilot
variant_name: v00069
type: drr-candidate
schema: Part-5-FPF-E-9
verdict: KEEP
validated_in_cycles: 1
ack_state: pending_brigadier_cycle_close
created: 2026-05-10T23:44:11
---

# DRR candidate — exp-2026-05-11-d2-voice-lens-pilot / v00069

## Decision
- **Hypothesis tested:** Karpathy-style propose→evaluate→keep-or-revert loop on the
voice-pipeline lens config (scoring weights × thresholds × tier
composition) can improve tier-1 anchor coverage on the 1627-item
filtered corpus from 2026-05-10 without regressing source diversity
or concentrating top-N output on a single memo source.

- **Mutation changes:**
  - tier_swap.Total Resource Management: tier_1 → tier_2

## Reasoning
- Experiment proposed under deterministic mutation operator + LLM-creative fallback.
- Search space = lens-config weights / thresholds / tier composition.
- Selection pressure = greedy keep-if-better on Hamel-binary primary metric.

## Result

| metric | before | after | delta |
|--------|--------|-------|-------|
| avg_top_score | 0.7646 | 0.7711 | +0.0065 |
| high_prio_share | 0.8000 | 1.0000 | +0.2000 |
| items_above_threshold | 48.0000 | 43.0000 | -5.0000 |
| max_source_concentration | 0.1500 | 0.1200 | -0.0300 |
| no_single_source_concentration_pass | 1.0000 | 1.0000 | +0.0000 |
| source_diversity_ratio | 0.5500 | 0.6800 | +0.1300 |
| tier1_coverage | 0.1290 | 0.2400 | +0.1110 |
| top_n_actual | 20.0000 | 25.0000 | +5.0000 |

## Review
- **Verdict:** `KEEP`
- **Validated in cycles:** 1
- **Methodology-promotion eligibility:** Q4 threshold is ≥3 validated cycles.
  Below that → stays in DRR ledger; no draft_promotion gate emission.
- **Ruslan ack required for promotion to canonical methodology.**
