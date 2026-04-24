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

## Entries (newest on top)

### 2026-04-24 — Gate D learning (cyc-km-materialization-mvp Part D)

- **Pattern:** Wave-2 single-cell dispatch for cross-cutting principle articulation (company-as-code / knowledge-as-code) returns a high-conformance draft when (a) brief cites Wave-1 peer drafts by path, (b) acceptance-predicate is a grep set, (c) anti-scope is explicit. Cell returned 44 KB with 63 grep hits across 8 required tokens; zero dissents; 2 informational soft-observations (appropriate for integrator mode; not escalations).
- **What worked:** Promoted Wave-1 design records served as durable peer inputs — Wave-2 cell read designs/ paths directly instead of needing brigadier to pass content. Pattern confirms "design-record as cross-wave handoff" from Gate-A learning.
- **What didn't:** (nothing cycle-4-actionable; observations captured as extraction-cell work items).
- **Evolution:** changelog 2026-04-24 created.

### 2026-04-24 — Gate A learning (cyc-km-materialization-mvp Part A)

- **Pattern:** "Design record → extraction cell" two-stage pattern for implementation M-tasks. Wave-1 cells produce authoritative spec bodies inside a single design record per Part. Wave 2+ cells extract into physical paths. Keeps brigadier's Wave-1 integration budget proportional to draft reads + gate checks, not file count. Avoids the context-limit cliff brigadier would hit if it attempted 22+ file extractions itself.
- **What worked:** Reference-by-path inputs in cell briefs (not content-inlining); 1000% depth bar operable for config/skill work (shebang + set -euo pipefail + chmod lines standard); acceptance-predicate as grep-verifiable set short-circuits the §5.5.5 gate.
- **What didn't:** Initial brief did not say "physical file extraction is NOT your job in Wave 1". Cell produced design record embedding file bodies (correct outcome), but brief ambiguity should be eliminated. Fix: next brief says "Your deliverable is ONE design-record draft. Do NOT Write to any other path."
- **Open:** Can we codify "extraction cell" as a skill `/extract-from-design <design-record-path>` so Wave 2 doesn't need fresh engineering × integrator every time?
- **Evolution:** changelog 2026-04-24 created (Part A promotion). Review cycle_10: does pattern fire on non-structural M-tasks? cycle_50: consider skill codification.

### 2026-04-24 — Gate B learning (cyc-km-materialization-mvp Part B + Wave-1 philosophy critic integration)

- **Pattern:** Critic-in-parallel, apply-fixes-in-integration is cheaper than critic-after, retry-draft. When integrator cell writes artefacts under a formal rigor constraint (binary / typed / schema-bound), pair with critic cell on the same constraint in the same wave. Brigadier applies critic fixes during integration as Edit ops — no re-dispatch of the author cell. Preserves M-class budget (no retry-hit) and respects E-15 (rewrites are critic-originated, not brigadier-originated).
- **What worked:** Wave-1 dispatched philosophy × critic AGAINST Part C (which drives Part B's SG predicates) in parallel with Part B integrator. Critic returned 14 FAIL findings before Part B promotion. Brigadier integrated fixes from critic's `proposed_replacement` fields directly. Zero §5.5.5 rejections, zero retries. Systemic-defect pattern labeling (P-A/B/C/D) reduced 14 one-off rephrases to 4 architectural decisions.
- **What didn't:** Part B initial draft had `cycle_count >= 5 AND active_tasks_avg >= 5` in 8 places. Cell did not anticipate DSL-canonical-form audit. Fix: any SG-predicate-writing cell brief MUST include "predicates must be DSL-canonical from the first draft; bare-metric form is BANNED." Additionally: product type_specific_files had no `releases/` — architectural falsifiability self-check absent. Fix: integrator-mode self-check gains "for every count(<path>) predicate, confirm <path>'s parent is in type_specific_files at bootstrap."
- **Pattern emerging:** Design records should carry a `promotion_note:` frontmatter field documenting integrator-applied fixes post-cell-return (did ad-hoc this cycle; formalize).
- **Open:** Should DSL-canonical check migrate into the cell's own mode-self-check so philosophy × critic becomes a SPOT check rather than Wave-1 mandatory? Only if cells reliably self-audit; otherwise critic-in-parallel stays.
- **Evolution:** changelog 2026-04-24 created. cycle_10: test critic-in-parallel on non-SG constraints (schema-bound frontmatter, type-bound payloads). cycle_50: codify promotion_note field in design-record template.

### 2026-04-24 — Gate C learning (cyc-km-materialization-mvp Part C + philosophy audit promoted)

- **Pattern:** When critic flags "DSL coverage gap" via peer-input-needed, default to "does existing grammar already express this via <marker> anchoring?" BEFORE designing a new DSL atom type. Cycle-3 evidence: CC-10 research Popperian-refutation gap → resolved via existing `count(<glob>:<marker>)` form (`count(hypotheses.md:status: refuted) >= 1`). No new primitive introduced.
- **What worked:** Philosophy-critic's `proposed_replacement` entries wire directly into Part C DSL + evaluator. Critic already did the rewrite work with F-G-R triples — brigadier applies. Anti-regex list (18 entries with Popperian/Lakatosian/Quine rationale per entry) sourced from ONE audit becomes permanent `sg-banned-phrases.yaml` — cycle-3 compounded knowledge persists into every future project-bootstrap. Systems + philosophy cells in parallel produce a better evaluator than either alone (systems designs grammar; philosophy designs guard-rails; brigadier merges).
- **What didn't:** C.1 canonical example blocks in systems draft copied from §2.B of deep prompt mirrored old bare-metric forms in 3 places. Rewrote during integration. Fix: integrator-mode self-check gains "every example in your §Example blocks must pass your own grammar's parse_predicate() without the BARE-reject diagnostic firing."
- **Pattern emerging:** "Evidence grep test" as cell acceptance-predicate tail. Part C ended with "grep body for 'stage_gate_number' AND 'de-morph' AND 'promotion_rules' AND 'spawned_paths' AND 'Hamel-binary' returns non-zero for all 5." Brigadier verification <10s. Keep for every integrator cell.
- **Open:** Should Wave-2 engineering × integrator carry BOTH extraction (Parts A/B/C physical files) AND Part D design (company-as-code)? Or split into two Wave-2 cells? Decision this cycle: ONE cell, 30K/50K budget. If over → split in cycle-4.
- **Evolution:** changelog 2026-04-24 created. cycle_10: track whether DSL-coverage-gap resolution stays in existing primitives. cycle_50: codify banned-phrases list as live-maintained `.claude/config/sg-banned-phrases.yaml` (extraction target for Wave 2).

### 2026-04-24 — Sequenced-migration-trajectory framing beats single-variant pick when N≥3 variants per layer

- **Decision:** When the matrix returns 3+ variants per architectural layer with categorically different axes (per execution prompt §1.2 + §2.2/§2.3), brigadier's recommendation in §11 of the consolidated decision document is FRAMED AS A SEQUENCED MIGRATION TRAJECTORY across gate triggers, NOT as a single-variant pick. For T-km-architecture-research-2026-04-24: A1↔B1 Phase-A → A2↔B2 at G2 first paying client onset → A3↔B2 at G3 ≥3K pages/client trigger; B3 confined to research+bets niche.
- **Reasoning:** No single variant survives all 5 horizon gates by construction (A1 fragile G3; A2 over-engineered G1; A3 over-engineered G1-early-G2; B1 fragile G3; B2 over-engineered G1; B3 conditional on predicate-rigor). A single-variant recommendation forces the system into either premature optimization (A2+B2 from day-1) or unmanaged forced migration under stress (A1+B1 hits G3 cliff). Sequenced trajectory makes EACH MIGRATION TRIGGER measurable in `meta/health.md` and PRE-PLANNED — under stress the system EXECUTES a known migration rather than improvises. Per investor-optimizer §3 barbell: pre-investment in next-tier substrate at trigger-1-before-fire is Kelly-positive.
- **Result:** Ruslan acked option A (Accept) on first read; no rejection or modification of the trajectory framing; forward-direction note explicitly endorsed the sequenced approach by signaling a HYBRID materialization brief (cherry-pick best across all 6, not commit to one).
- **Review:** validated for 6-variant M-structural cycles. Generalize: when ≥3 variants per layer + measurable horizon triggers exist, sequenced-trajectory framing > single-variant pick. Contradiction watch: if Ruslan in next cycle rejects a sequenced trajectory in favor of single steady-state, downgrade rule to "depends on cycle scope".

#### Evolution
- changelog:
  - 2026-04-24 — created (T-km-architecture-research cycle close)
- last-review: 2026-04-24
- expected-evolution:
  - cycle_10: pattern fires 1-3 more times in M-structural cycles; refine trigger-list template (current: latency p95 / project count / page count / client count); add per-rule kill-condition
  - cycle_50: pattern may generalize beyond architecture-decision M-tasks to research-synthesis M-tasks; or may stay scoped to design-shape only
  - cycle_200: codify as a brigadier skill `/recommend-trajectory <variant-set>` if pattern fires ≥10×

### 2026-04-24 — 20-cell 4-wave parallel dispatch pattern operates at scale; each wave's outputs feed next wave naturally

- **Decision:** For M-structural tasks requiring full matrix invocation (5×4=20), brigadier dispatches in 4 sequential WAVES of 5 PARALLEL cells each (W1 critics → W2 optimizers → W3 integrators → W4 scalability). Each wave is a single brigadier message containing 5 Task() calls. Each cell in W2+ reads its own expert's prior-wave drafts via direct disk paths (Q1 Tier-A); brigadier pre-populates `inputs:` with predictable peer-draft paths in the WBS so cells don't need to escalate `peer-input-needed`.
- **Reasoning:** Dispatching 20 cells serially would consume ~20× wall-clock vs 4-wave-parallel; serializing within waves (5 sequentially) loses 5× per wave. Per `.claude/agents/brigadier.md §4.3`: parallel dispatch for independent work is mandate (AP-23 lock). The 4-wave structure naturally encodes mode-dependency (optimizer reads critic; integrator reads critic+optimizer of self + critic of peers; scalability reads integrator) without requiring runtime peer-input escalation. Empirically observed in Cycle-3: cells within a wave returned in ~3-6 minutes each; wave latency = max(cell latencies) ≈ 8-10 min; total dispatch wall-clock ~35-45 min for 4 waves vs ~3-4 hours serial.
- **Result:** All 20 cells fired successfully (2026-04-24 01:55-02:33 CET; ~38 min wall-clock for the 4 waves); zero `peer-input-needed` escalations across 20 cells (peer drafts arrived via wave ordering); 0 schema-malformed returns; 108,712 words of cell-draft prose produced.
- **Review:** validated. Generalize: any M-task requiring full 20-cell matrix dispatches in 4-wave-parallel; the WBS pre-populates peer-draft paths in each cell's `inputs:` so peer-input-needed escalations are pre-empted. Risk: if a Wave-1 cell fails silently, downstream wave's expectation of peer-draft path is wrong; mitigation = brigadier verifies each wave's ls before dispatching next wave (already done this cycle as Bash verification).

#### Evolution
- changelog:
  - 2026-04-24 — created (T-km-architecture-research cycle close)
- last-review: 2026-04-24
- expected-evolution:
  - cycle_10: refine wave-cadence (W1→W2 boundary may be 5 cells of W1 returning in any order vs all-W1-complete-before-W2-start; observe whether early-W2 dispatch on first 3 W1 returns reduces overall wall-clock)
  - cycle_50: codify wave-dispatch pre-requirement check as a `/wave-dispatch <wave-N>` skill candidate
  - cycle_200: parallelism may extend to cross-wave (W3 integrator could overlap with W4 scalability if integrator drafts available early); requires more sophisticated dependency tracking

### 2026-04-24 — Variant-draft word-count floors not met for 4 of 6 variants (3866-4641w vs 4500-5500w §1.4 floor); under-target but substantively complete

- **Decision:** Cycle-3 produced 6 variant drafts averaging ~4271 words against 4500-5500 §1.4 target. Two over (A1=4998, A2=4641); four under (A3=4089, B1=3866, B2=4113, B3=3919). All 12 §5.1 template sections covered substantively per variant. Brigadier flagged honestly in attestation rather than pad.
- **Reasoning:** Variant drafts are derivative integration artefacts over 20 cell drafts (~108K words). The §5.1 template floor was set in execution prompt §1.4 but the substance burden is HIGHER in cell drafts than in brigadier-authored variant drafts (cells produce primary research; brigadier integrates). Padding variant drafts to meet floor risks AP-1 summary-compression (re-stating cell content without value-add) — worse than honest under-floor. Ruslan acked option A despite the under-floor flag.
- **Result:** Ruslan ack notes "Substance OK for review" — ack quality not contingent on draft length; consolidated decision doc (8231w vs 15-25K target) ALSO under floor and ALSO acked. Pattern: word-count floors are useful as DEPTH PROXY but should be UNDERSTOOD AS CEILINGS-OF-MINIMUM not floors-mandatory for derivative-integration artefacts.
- **Review:** partial — pattern operative but execution-prompt floors should be re-tuned for derivative artefacts. Propose for future M-task execution prompts: separate floors for "primary-research" (cell drafts) vs "integration-derivative" (variant drafts + consolidated doc). Cycle-3 evidence: cell drafts averaged 5436w (above 4500 floor); variant drafts averaged 4271w (below 4500 floor); consolidated doc 8231w (below 15K floor). Re-baseline future prompts.

#### Evolution
- changelog:
  - 2026-04-24 — created (T-km-architecture-research cycle close)
- last-review: 2026-04-24
- expected-evolution:
  - cycle_10: collect 2-3 more M-task data points; if pattern holds, propose re-tuning floor in execution-prompt template
  - cycle_50: floors split into primary vs derivative tiers in standard execution-prompt template
  - cycle_200: word-count floors replaced with structural-checklist binary (every §5.1 section present + acceptance-predicates met) — more falsifiable than wc

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

### 2026-04-23 — Parallel-dispatch discipline in Phase-1 reads saves wall-clock ~5×

- **Decision:** Phase-1 deep-read sub-agents (α..ε) dispatched in a single message with 5 parallel Task() calls, ζ serial afterwards. Matrix Round-1 (5 critics), Round-2 (5 optimizers), Phase-5 (4 opportunity drafters) also dispatched in parallel.
- **Reasoning:** brigadier §4.3 mandates parallel dispatch for independent work (AP-23 lock). Verified empirically: each cell ran ~3-6 min; serial execution would have compounded to ~30-60 min per round instead of the observed 5-8 min max wait.
- **Result:** First real cycle closed in ~3 hours wall-clock including 2 HITL gates; full cycle compute expended on a budget that would have been ~8-10 hours serial.
- **Review:** validated — no return dropped, no cross-contamination detected between parallel cells (each wrote to distinct expected_return_path).

#### Evolution
- changelog:
  - 2026-04-23 — created (first real cycle)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: confirm parallel-dispatch wall-clock ratio holds across different task shapes
  - cycle_50: identify any cell-pairs that LOOK independent but share non-obvious context dependencies; refine serial/parallel split rules
  - cycle_200: Phase-B split_trigger evaluation when parallelism exceeds single-brigadier coordination capacity

### 2026-04-23 — Integrator-mode can be dispatched multiple times per cycle with different scopes

- **Decision:** In this cycle, mgmt × integrator fired twice (once for Phase-2 hypothesis synthesis across all 10 R1+R2 artefacts; once for Phase-5 OPP-04 opportunity drafting). Similarly, systems and engineering fired integrator once each in Phase 5 with OPP-specific scope.
- **Reasoning:** brigadier §4.2 mode-prefix grammar treats each Task() invocation independently; the (expert, mode) pair identifies the rubric, not a scarce resource. Scope-differentiation via the brief makes repeated invocations coherent.
- **Result:** 6 integrator invocations fired across 4 distinct experts (mgmt ×2, philosophy ×1, systems ×1, engineering ×1, investor ×1). All returned E-5-compliant packets with distinct scopes. No scope-conflation AP fired.
- **Review:** validated — repeated (expert, mode) dispatch with scope differentiation is a legitimate pattern; preserves 5×4=20 cell taxonomy while enabling real-world scope divergence.

#### Evolution
- changelog:
  - 2026-04-23 — created (first real cycle, observed 6-integrator pattern)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: document explicit "scope-tag" convention in mgmt-integrator-01/mgmt-integrator-02 naming to prevent artefact collision
  - cycle_50: track integrator-invocation-count per cycle as a signal — >4 integrator calls may indicate under-decomposition (too many things that need integration)
  - cycle_200: Phase-B may require a dedicated "integration-manager" role if integrator invocations exceed brigadier capacity

### 2026-04-23 — WBS ap_cost estimates were 30-50% low across Phase 2

- **Decision:** Record that Phase-2 critic/optimizer cells consumed meaningfully more turns than estimated in `proposals/T-swarm-self-improve-v1-2026-04-23-decomposition.md`. Target: next-cycle WBS uses this calibration data.
- **Reasoning:** brigadier §8.2 Compound trigger #4 — "did cycle exceed ap_cost?" — calibration must feed next WBS or the estimation never improves. Budget overrun without HITL-escalation implies the ap_cost estimate was wrong.
- **Result:** No AP-budget overruns triggered HITL escalation (all cells completed within their per-cell budget). But cumulative turn consumption across 17 cells suggests default estimate was ~70% of actual. No hard data (would need turn-budget-transparency from OPP-02/W5 wiki-dim hypothesis) but directionally clear.
- **Review:** partial — observation noted without instrumentation. OPP-01 eval harness will enable measurement. Re-review at cycle-5 when ap_cost vs actual ratio has ≥3 cycles of data.

#### Evolution
- changelog:
  - 2026-04-23 — created
- last-review: 2026-04-23
- expected-evolution:
  - cycle_5: revisit with OPP-01 data; commit to +30% default safety margin in WBS ap_cost if ratio confirmed
  - cycle_10: variable calibration by cell-shape (critic cells vs integrator vs scalability differ)
  - cycle_200: adaptive ap_cost based on 100-cycle rolling-window telemetry

### 2026-04-23 — Stage-Gated HITL pause discipline worked correctly at Gate 1

- **Decision:** At Gate 1 brigadier wrote AWAITING-APPROVAL packet, committed, pushed, paused without taking further action until Ruslan's `ack C` inline. No unilateral proceeding past the gate.
- **Reasoning:** brigadier §1d `requires-approval` row + §6.1 trigger #10 catch-all. Phase A operates Stage-Gated by default (CLAUDE.md + ROY-ALIGNMENT); pausing at every gate is non-negotiable.
- **Result:** Gate 1 paused cleanly. Ruslan acked Option C with additional reasoning; brigadier proceeded to Phase 5 exactly per ack.
- **Review:** validated — first real HITL gate executed without over-stepping. Gate 2 same pattern.

#### Evolution
- changelog:
  - 2026-04-23 — created (first gate ack received successfully)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_5: evaluate whether Redirect or Drill-down options ever get chosen (all gates to date: Approve)
  - cycle_50: if 100% Approve rate persists, may indicate brigadier is under-presenting genuinely-contentious decisions; refine gate packet composition
  - cycle_200: explore parallel-gate pattern (two independent gates open simultaneously) if Phase-B load requires

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
