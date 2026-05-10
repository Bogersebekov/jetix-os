---
title: AutoResearch program — D.2 voice-pipeline lens configs
domain: D.2-voice-lens-config
authored_by: ruslan
last_modified: 2026-05-11
parent_hypothesis: config/autoresearch-hypothesis-2026-05-11-d2-voice-lens.yaml
canonical_anchors:
  - swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md
  - reports/autoresearch-karpathy-integration-2026-05-11/PLAN.md
---

# AutoResearch program — D.2 voice-pipeline lens

## Objective

Improve the lens-config scoring such that the top-N actionable output
faithfully surfaces the items Ruslan most wants to see for the current
focus. "Better" = primary metric **tier-1 anchor coverage** rises without
regressing source diversity or concentrating top-N output on one memo
source.

Baseline (tseren lens 2026-05-10 on the 1627-item filtered corpus):
- tier1_coverage ≈ 0.129 (~4 of 31 tier-1 keywords appear in top-20)
- source_diversity_ratio ≈ 0.55
- max_source_concentration ≈ 0.15

Stretch target: tier1_coverage ≥ 0.50 within Phase 1 budget (80 experiments),
while keeping source_diversity_ratio ≥ 0.50 and max_source_concentration ≤ 0.35
(Hamel-binary PASS predicate).

## Constraints

- **LOCKED.** The filtered corpus (`inbox/processed/filtered/batch_2026-05-10.json`)
  and the scoring-formula structure (`tools/jetix-autoresearch/evaluator/voice_lens.py`)
  may not be mutated. Variants only change the lens config:
  `config/voice-pipeline-lens-2026-05-10-tseren.yaml`.
- **No new package installs.** Pure Python stdlib + already-imported deps.
- **No keyword stuffing.** Adding 100 keywords to tier-1 to brute-force coverage
  is Goodhart-trivial; the simplicity prior penalizes it. Tier-1 keyword count
  may grow by no more than +50% over baseline (31 → 47 max).
- **Renormalization.** `scoring_weights.{keyword,semantic,domain_element,recency}`
  must sum to 1.0 after every mutation.
- **No regression.** A KEEP requires no regression on source_diversity_ratio
  beyond 85% of baseline AND max_source_concentration ≤ 0.45.

## Research directions (priority order)

1. **Weight rebalancing.** Try lowering w_semantic (currently 0.35) and raising
   w_keyword (currently 0.40) — the dominant signal in this corpus is keyword
   match; semantic proxy via priority is noisy.
2. **Threshold lowering.** Baseline threshold 0.60 may be too aggressive given
   the keyword distribution; lowering to 0.45–0.55 may surface more tier-1-anchored
   items without polluting top-N.
3. **Top-N expansion.** Current top_n=20. Test 25/30. If Hamel predicates
   still pass at larger N, the value-density of the output increases.
4. **Tier promotion of high-signal Russian variants.** Tier-2 contains
   "методология / methodology"; promoting to tier-1 may close coverage gaps
   when Russian-named items dominate the corpus.
5. **Domain weight tuning.** Some `domain_element_weights.*` entries may be
   miscalibrated; small ±0.10–0.15 perturbations may surface workshop/TRM-
   relevant items more reliably.

## Success criteria (Hamel-binary)

PRIMARY (acceptance predicate per `voice_lens.evaluate.hamel_binary_verdict`):

    PASS iff
       tier1_coverage          >= 0.80
       source_diversity_ratio  >= 0.50
       max_source_concentration <= 0.35

GREEDY KEEP rule (looser; what the orchestrator uses turn-by-turn):

    KEEP iff
       new_primary_metric > current_primary_metric AND
       source_diversity_ratio >= 0.85 × baseline AND
       max_source_concentration <= 0.45

## Anti-patterns (don't re-propose)

- **Top-N inflation to 60.** Inflates tier1_coverage trivially but explodes
  the top-N attention surface and defeats the purpose. Cap top_n at 30.
- **Tier-1 keyword bloat.** Adding 50+ keywords to tier-1 brute-forces
  coverage without selection quality. Max tier-1 growth = +50% over baseline.
- **Threshold collapse to 0.00.** Lets every item pass the threshold, kills
  signal. Lower bound = 0.20.
- **Single-keyword stuffing.** Adding the same keyword multiple times under
  different cases — no signal gain, anti-pattern by construction.
- **Domain weight uniformization.** Setting all `domain_element_weights.*`
  to the same value defeats the domain-element signal entirely.

## Notes on Q8 hybrid authorship

Per Q8 ack 2026-05-11: this `program.md` is **Ruslan-authored**. Agents may
draft a `program/d2-voice-lens.md.draft` for review during cycle close, but
the canonical file is promoted only via standard Ruslan ack.
