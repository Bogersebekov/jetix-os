---
title: philosophy-expert — Strategies (System Prompt Learning)
agent: philosophy-expert
created: 2026-04-23
last_modified: 2026-04-24
state: active
confidence: N/A-scaffolding
expected_evolution:
  cycle_10: 5–10 epistemic-audit rules; first-principles-reset template stabilised; ≥1 entry on Рациональность boundary with investor (defer instrumental to investor)
  cycle_50: Epistemic-flag acceptance-rate >50% stabilised; Popper/Kuhn/Munger rubric-cell boundary refined; BA-Cycle lite invoked on at least 5 ethical-surface tasks
  cycle_200: Split-trigger evaluation — consider splitting into epistemology-expert + ethics-expert if BA-Cycle volume >40% sustained over 3 consecutive cycle_50 windows
---

# Strategies — philosophy-expert

## Entry Format

Each entry uses 4-part DRR per FPF E-9 §2.9 with the documented
swarm-wide translation (critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why
3. **Result** — observed outcome
4. **Review** — validated | refuted | partial

Plus Evolution sub-block per FPF §3.5.

## Entries

### 2026-04-24 — Arithmetic flags must not be logged as dissents (C-13 §14)

- **Decision:** When a claimed "dissent" reduces to an arithmetic inconsistency (not a values conflict), reclassify as arithmetic-correction-flag and issue a correction-instruction to the source cell. Do NOT preserve arithmetic errors as (F, ClaimScope, R) dissents.
- **Reasoning:** D-price-4 (Educational floor €3K vs €5K arithmetic minimum) was initially logged as a dissent by §2 (C-01). Philosophy-expert review in C-13 (§14) identified it as arithmetic: 10-learner cohort × €500 cost/learner = €5K required to clear the stated €3K margin/learner gate. Preserving it as a dissent would misrepresent it as a legitimate values disagreement. Alternatives considered: (a) preserve as dissent — kill-condition: creates false equivalence between arithmetic errors and values positions; (b) silently correct — kill-condition: source cell author loses visibility of the error; (c) reclassify + correction-instruction — no kill-condition identified. Option (c) selected.
- **Result:** D-price-4 reclassified in §14 with correction-instruction to raise §2 stated floor to €5K. Arithmetic error surfaced without inflating the dissent register.
- **Review:** validated — pattern is consistent with AP-PHIL-1 (Popper: arithmetic claims are falsifiable, not merely positional).

#### Evolution
- changelog:
  - 2026-04-24 — created (C-13 §14 cycle)
- last-review: 2026-04-24
- expected-evolution:
  - cycle_10: apply reclassification to ≥3 arithmetic flags caught in future cells
  - cycle_50: build a two-column taxonomy in critic mode (arithmetic-flags | values-dissents)

---

### 2026-04-24 — Prefer more falsifiable operational definition (T-L7-1 pattern)

- **Decision:** When two operational definitions coexist for the same trigger or threshold, apply Popper P1 (falsifiability): prefer the definition that admits a clearer refutation observation. Name the reasoning explicitly in the critic return.
- **Reasoning:** T-L7-1 surfaced a conflict between §4's "3-month sustained run-rate ≥€1M" (G2→G3 gate) and L6 §11.2's "€1M cumulative." The "cumulative" definition admits passage by a single large contract; the "sustained run-rate" definition requires observable stability. "Cumulative" is more easily satisfied but harder to falsify (a spike is undetectable after the fact). "3-month sustained run-rate" fails if any month in the 3-window falls below threshold — clear falsifier, easy to verify. Alternatives considered: (a) defer to HITL — kill-condition: unnecessarily escalates a definitional preference that has a principled resolution; (b) accept both as equivalent — kill-condition: creates gate ambiguity that could allow premature Phase promotion; (c) prefer more falsifiable — no kill-condition identified.
- **Result:** T-L7-1 brigadier recommendation issued: reconcile canonical to "3-month sustained run-rate ≥€1M." Reasoning stated explicitly in §14.4.
- **Review:** validated — applying Popper P1 to resolve definitional conflicts is epistemically correct and produces actionable brigadier recommendations.

#### Evolution
- changelog:
  - 2026-04-24 — created (C-13 §14 cycle)
- last-review: 2026-04-24
- expected-evolution:
  - cycle_10: apply to ≥2 more definitional conflicts in upcoming deep-dives
  - cycle_50: build a "definitional preference rubric" that applies P1 + IDEM (idempotency) to all threshold definitions

---

### 2026-04-24 — Sequencing dependency map as standard critic sub-artefact

- **Decision:** In any critic or integrator pass synthesizing ≥5 cells, produce a sequencing dependency map as a standard sub-artefact. The map must name what blocks what and identify the critical path to the next gate.
- **Reasoning:** §14.6 sequencing map identified a critical path (Ruslan ack Q-L7-01 + Q-L7-04 → T-L7-1 reconciliation → Phase-3 writable) that brigadier would have discovered serially. Without the map, each ack would have been a separate HITL event with lead time. Explicit mapping collapses serial discovery into a single presentation. Alternatives considered: (a) skip sequencing map — kill-condition: brigadier discovers ack dependencies one at a time (adds cycle latency); (b) produce informal prose — kill-condition: not parseable; brigadier cannot extract the critical path without reading full prose; (c) structured dependency map — no kill-condition identified for this task load.
- **Result:** §14.6 map produced; two Ruslan acks identified as bottleneck; one brigadier reconciliation identified as secondary bottleneck. Map is machine-parseable (indented tree format).
- **Review:** validated — dependency maps reduce HITL load by batching acks; consistent with Stoic P5 (identify what is in our control = the map; what is not = Ruslan's response timing).

#### Evolution
- changelog:
  - 2026-04-24 — created (C-13 §14 cycle)
- last-review: 2026-04-24
- expected-evolution:
  - cycle_10: standardize map format (tree vs DAG vs table); evaluate which is most parseable for brigadier
  - cycle_50: if brigadier integrates maps into its own planning pass, refine the format to match brigadier's intake schema

---

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold `agents/philosophy-expert/strategies.md` per Шаг 2.2.4 Part C.
- **Reasoning:** Layer-2 self-write per CLAUDE.md; FPF E-9 + D12
  mandate empty-but-structured strategies.md from day zero.
- **Result:** file lint-valid, Phase A bootstrap unblocked.
- **Review:** scaffolding only; first real entry on first cycle.

#### Evolution
- changelog:
  - 2026-04-23 — created (scaffolding)
- last-review: 2026-04-23
- expected-evolution: see frontmatter
