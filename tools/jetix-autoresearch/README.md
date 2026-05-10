# Jetix AutoResearch — Phase 1 MVP (D.2 voice-lens pilot)

> **Status.** Phase 1 implementation per Ruslan ack 2026-05-11.
> Pilot domain: D.2 voice-pipeline lens configs.
> All inference via `tools/lib/cc_helper.py` (Max-sub headless; no `ANTHROPIC_API_KEY`).
> Constitutional discipline: pre-mutation Default-Deny + draft_promotion gate.

## Canonical anchors

- Plan: `reports/autoresearch-karpathy-integration-2026-05-11/PLAN.md`
- Karpathy reference: https://github.com/karpathy/autoresearch
- Part 5 (compound learning + DRR ledger): `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md`
- Part 6b (human gate + Default-Deny F8): `swarm/wiki/foundations/part-6b-human-gate/architecture.md`
- Voice-pipeline canonical: `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md`
- Hypothesis config: `config/autoresearch-hypothesis-2026-05-11-d2-voice-lens.yaml`
- Research agenda: `program/d2-voice-lens.md`

## Files

```
tools/jetix-autoresearch/
├── README.md                 (this file)
├── __init__.py
├── orchestrator.py           propose→eval→keep-or-revert loop (~210 LOC)
├── mutation_generator.py     programmatic + LLM (via cc_helper) propose
├── constitutional_gate.py    Default-Deny lookup + AWAITING-APPROVAL emit
├── results_store.py          TSV + DRR-candidate markdown emit
├── cost_tracker.py           daily €10 cap (Q2 ack) + 80% soft alert
├── evaluator/
│   ├── __init__.py
│   └── voice_lens.py         D.2 deterministic evaluator (Hamel-binary)
└── results/                  output ledgers (cost-ledger/, health-signals.jsonl)
```

## Usage

```bash
python3 tools/jetix-autoresearch/orchestrator.py \
  --hypothesis config/autoresearch-hypothesis-2026-05-11-d2-voice-lens.yaml \
  --max-experiments 80 \
  --output-dir reports/autoresearch-karpathy-integration-2026-05-11/ \
  --llm-share 0.0
```

Outputs:

- `reports/.../pilot-d2-results.tsv` — one row per experiment
- `reports/.../pilot-d2-summary.json` — final summary
- `reports/.../drr-candidates/*.md` — one DRR candidate per KEEP variant
- `tools/jetix-autoresearch/results/cost-ledger/<date>.jsonl` — cost trail
- `tools/jetix-autoresearch/results/health-signals.jsonl` — gate / halt events
- `swarm/approvals/log.jsonl` — AWAITING-APPROVAL packets on cap breach / consecutive failures

## Constitutional invariants honoured

- **Tier 2 R1.** No strategic decisions made by agents. Hypothesis +
  program.md authored by Ruslan; methodology promotion requires Ruslan ack.
- **Tier 2 R2.** Mutation scope hard-limited to declared
  `mutable_substrate.files`. Foundation paths excluded. Violation →
  `halt_log_alert` (F8) per Part 6b §I.2.
- **Tier 2 R6.** Memory persists only via TSV / DRR markdown /
  git history. No vector store, no embedding cache.
- **Tier 2 R9.** No agent self-modifies own `system.md` / `strategies.md`
  at runtime. DRR entries emitted as draft candidates under
  `reports/.../drr-candidates/` for cycle-close brigadier review.
- **Tier 2 R11.** Every mutation carries `blast_radius`. Uncategorized →
  halt_log_alert.

## Phase 1 success criteria (per PLAN §5.1)

- 50+ experiments without constitutional violations.
- ≥1 validated DRR entry (KEEP variant + delta > 0).
- Daily cost ≤ €10 hard cap.
- Ruslan can read `pilot-d2-summary.md` + DRR ledger to form take.
