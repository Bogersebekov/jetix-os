---
id: opportunity-M3-solo-vs-matrix-baseline
title: "M3 — Solo-brigadier vs 6-cell matrix golden-set baseline (commissioned at Gate 1)"
type: opportunity-artefact
cluster_id: S-05
tier: T2-commissioned
lead_domain: investor
co_domains: [philosophy, systems, mgmt]
dissents_addressed: [D-03, ADD-D-06 partial]
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: investor-expert
mode: integrator
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: arithmetic + judgment
niche: meta
provenance_inline: true
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-critic-01.md", range: "140-165"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-optimizer-01.md", range: "253-262"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-critic-01.md", range: "139-191"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-integrator-01.md", range: "130-145"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md", range: "1-50"}
  - {path: "decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md", range: "178-195"}
---

# M3 — Solo-brigadier vs 6-cell Matrix Golden-Set Baseline

**Opportunity ID:** M3  
**Cluster:** S-05  
**Tier:** T2-commissioned (Gate-1 Option C, Phase-5 deliverable)  
**Lead domain:** investor-expert (owns the 2× claim validation, H-4
arithmetic, margin-of-safety 0.30 knife-edge)  
**Co-domains:** philosophy (Popper-falsifiability rubric), systems
(substrate for golden-set storage), mgmt (experiment design governance)  
**Dissents addressed:** D-03 (engineering-first vs philosophy-first
measurability), ADD-D-06 (scoring-weight paradigm)

---

## §1 Background and rationale

The swarm investment thesis rests on a 2–3× quality gain claim
attributed to Boris Cherny: "Claude performs dramatically better when
it can verify its own work." [src: investor-critic-01.md:80-86]
investor-critic-01.md (H-4) established that this claim has
**margin-of-safety exactly 0.30** — the Graham minimum floor — under
the arithmetic:

```
MoS = (expected_return − opportunity_cost − ruin_floor) / opportunity_cost
    = (1.5 × solo_turns − solo_turns − 0.2 × solo_turns) / solo_turns
    = 0.30
```

Below a 1.5× quality delta, MoS goes negative. There are currently
zero Hamel-validated golden-set comparisons proving that the 6-cell
matrix exceeds solo-brigadier by ≥1.5×. [src: investor-critic-01.md:141-155]

philosophy-critic-01.md (H-1, H-2) classifies the "2× improvement"
claim as **F1** (assertion; no measurement baseline) and **AP-PHIL-1**
(non-falsifiable as written). [src: philosophy-critic-01.md:148-165]

D-03 (SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md §7) preserves
the dispute: engineering says "install eval harness first (OPP-01)
and 2× will be calibrated"; philosophy says "proceeding with F1 claim
risks encoding false anchor in KPIs." The operational resolution in
D-03 is that no T1/T2 cluster uses "2×" as a Hamel-binary acceptance
predicate — the claim is demoted to provenance context. But D-03 does
not eliminate the need to test the claim; it only delays the harm of
treating it as settled. [src: SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md:238-243]

investor-optimizer-01.md (Bundle C, §5) commissioned this comparison
as H-4, ranked fifth by Kelly-score (E=8, P=7, Payback=3–5 cycles)
and identified as the gateway that unlocks H-8 (paid-API transition
memo). [src: investor-optimizer-01.md:253-262]

**This artefact is the experimental design for that comparison.** It
is not itself the measurement; it specifies the protocol that will
produce a measurement. The measurement is produced when the experiment
is executed (post-Gate-2 per the brief).

---

## §2 Problem statement

**Claim to test (H0 / H1):**

- **H0 (null):** A 6-cell matrix invocation does NOT produce quality
  ≥ 2× solo-brigadier quality on a representative toy task, for ≥3 of
  5 quality rubric items. (The "2× improvement" claim is false at this
  task distribution.)
- **H1 (alternative):** A 6-cell matrix invocation produces quality
  ≥ 2× solo-brigadier quality on a representative toy task, for ≥3 of
  5 quality rubric items. (The "2× improvement" claim is true at this
  task distribution.)

**Rejection criterion:** H0 is rejected if ≥3 of 5 rubric items show
a 2× or better quality delta (Run B vs Run A). H0 is not rejected if
<3 of 5 items show a 2× delta.

**Ambiguous zone:** If delta is ≥1.5× but <2× on ≥3 items, that is
the 1.5–2× zone. Per §2 margin-of-safety arithmetic (MoS=0.30 exactly
at 1.5×), this zone constitutes "insufficient evidence" — the
investment is ON the margin, not above it. Action: revisit at cycle-5
with n=3 repeated trials before deciding.

**Falsifiability check (Popper, philosophy-critic-01 H-1 rubric):**
The H1 claim is falsified if ≥3 of 5 rubric items show delta <2×.
The falsifier is: "observed quality delta on ≥3 rubric items is <2×."
Observable in `swarm/evals/golden/solo-vs-matrix/results.jsonl` after
run execution. This satisfies philosophy's AP-PHIL-1 requirement.
[src: philosophy-critic-01.md:148-165]

---

## §3 Proposed implementation

### §3.1 Toy-task specification

**Design constraint (from brief):** ≤15 solo-brigadier turns to
complete; representative (not cherry-picked to favour the matrix).

**Candidate toy tasks (brigadier picks one post-Gate-2):**

---

**Candidate T-A — Moat analysis of one named tech stack**

- *Description:* "Produce a moat analysis for Cursor (AI code editor)
  as a business. Include: (a) three moat candidates with ≥2
  kill-conditions each; (b) an invert section (how does the moat fail?)
  placed first; (c) a margin-of-safety floor computation on the moat
  durability claim; (d) opportunity-cost of building a competing
  product. Output: one draft artefact ≤600 words."
- *Done predicate (Hamel-binary):* "Artefact is present at the
  designated path AND contains ≥3 named moat candidates AND ≥2
  kill-conditions per candidate AND an invert section appearing before
  the positive case AND an explicit margin-of-safety number (not prose)."
- *Inputs:* the task brief above (≤50 words); no additional context
  files loaded.
- *Expected output:* a single markdown artefact ≤600 words.
- *Solo-brigadier turn estimate:* 8–12 turns.
- *Representativeness argument:* Moat analysis is investor-expert's
  primary artefact type, requires multi-domain reasoning (capital +
  tech + second-level thinking), and is non-trivially checkable via
  rubric. Not cherry-picked: no prior moat analysis exists in the swarm
  that would give the matrix an unfair advantage.
- *Representativeness risk:* moat analysis may be investor-domain-
  dominant, benefiting the matrix more than a generalist task would.
  Mitigation: the done-predicate is enforced identically on both runs.

---

**Candidate T-B — Unit-economics arithmetic for a 3-month consulting
retainer**

- *Description:* "Given: a solo consultant charges €5,000/month for
  an AI-services retainer; cost of delivery is 40 founder-hours/month;
  founder's opportunity cost is €120/hr (equivalent consulting rate);
  1 client = ~5% of monthly revenue. Produce: (a) an owner-earnings
  block (owner-earnings ≠ GAAP revenue; show the three line-items);
  (b) a margin-of-safety computation vs the T-bill alternative at 4%
  annual; (c) a risk-of-ruin floor statement; (d) a second-level
  thinking paragraph on what the market has already priced into
  consulting rates. Output: one artefact ≤500 words."
- *Done predicate (Hamel-binary):* "Artefact is present AND contains
  an owner-earnings block with ≥3 named line-items (GAAP earnings,
  depreciation/maintenance capex, working-capital delta) AND a numeric
  margin-of-safety (not prose 'we have margin') AND a risk-of-ruin
  probability with a runway-impact number AND a second-level thinking
  paragraph."
- *Inputs:* the brief above (≤60 words); no additional context files.
- *Expected output:* single markdown artefact ≤500 words.
- *Solo-brigadier turn estimate:* 6–10 turns.
- *Representativeness argument:* Unit-econ arithmetic is the most
  commonly recurring investor-expert task and the most structurally
  constrained (concrete numbers, not narrative). A 5-cell matrix on
  unit-econ adds philosophy (epistemic quality of the model), systems
  (feedback loops in revenue retention), mgmt (delivery-time costing),
  and engineering (automation feasibility) — domains genuinely relevant
  to the task. If the matrix cannot beat solo here, it cannot beat solo
  anywhere.
- *Representativeness risk:* the arithmetic is fully deterministic once
  inputs are fixed; the matrix advantage may be smaller on mechanical
  arithmetic tasks than on open-ended synthesis. This is a valid concern
  — see §8 anti-scope.

---

**Candidate T-C — Horizon projection for the €50K → €200K gate**

- *Description:* "Produce a horizon projection artefact for the €50K →
  €200K gate transition (per JETIX-ARCHITECTURE-BRIEF §5.1). Include:
  (a) BOSC-A-T-X first-trigger at €200K; (b) a gate risk table (top
  risk per gate, likelihood, mitigation); (c) a via-negativa retirement
  list (≥2 positions to retire at the €50K → €200K transition); (d)
  a degraded-mode specification for both S-A excess and INT excess.
  Output: one artefact ≤700 words."
- *Done predicate (Hamel-binary):* "Artefact is present AND contains
  a BOSC-A-T-X first-trigger label for €200K AND a gate risk table with
  ≥2 rows AND a retirement list with ≥2 named positions AND a
  degraded-mode spec with both failure modes named."
- *Inputs:* the brief above (≤60 words) + one reference: the relevant
  §6.1 row from investor-expert.md (provided as a 10-line extract in
  the task brief; no full file load).
- *Expected output:* single markdown artefact ≤700 words.
- *Solo-brigadier turn estimate:* 10–14 turns.
- *Representativeness argument:* Horizon projection is multi-domain by
  nature (capital + systems + mgmt strategy + philosophical coherence of
  the gate framing). It maps directly onto a known investor-expert
  deliverable type (§6.5 output schema). High real-world relevance —
  this artefact type will actually be used at the €200K gate decision.
- *Representativeness risk:* this is the most complex of the three
  candidates; solo-brigadier may struggle with ≤15 turns. If solo-
  brigadier under-performs due to complexity ceiling, the comparison
  may inflate the matrix advantage unfairly. Mitigation: cap solo-
  brigadier at 15 turns; if it hits the cap without completing, that IS
  data (the matrix advantage on complex tasks is the hypothesis).

---

**Brigadier selection note:** After Gate-2 approval, brigadier selects
one candidate. Selection criterion: the candidate that is LEAST likely
to cherry-pick toward the matrix. Recommended selection order:
T-B (deterministic arithmetic, hardest for matrix to show advantage)
then T-A (structural analysis, moderate) then T-C (complex synthesis,
easiest for matrix to show advantage). If the objective is maximum
information-per-turn, T-B is preferred. If the objective is
demonstrating value to Ruslan on a real task, T-C is preferred.

---

### §3.2 Run A — Solo-brigadier protocol

**Setup:** brigadier is invoked directly on the toy task (the brief
from §3.1 for the selected candidate). No expert cells are dispatched.
Brigadier produces the artefact without decomposition.

**Constraints:**
- Maximum 15 turns.
- No additional context files beyond what is specified in the task
  brief.
- brigadier writes the artefact to `swarm/evals/golden/solo-vs-matrix/run-A-<task-slug>.md`.
- Turn count is logged: `{turns_used: N, started_at: <ts>, completed_at: <ts>}`.
- The artefact is evaluated against the quality rubric (§3.4) immediately
  after completion. Rubric is applied by a separate evaluator call
  (philosophy-expert × critic mode, reading the artefact and returning
  a structured pass/fail per rubric item). The evaluator does NOT know
  whether the artefact came from Run A or Run B at evaluation time
  (double-blind on labelling — both artefacts are passed with labels
  "Artefact-X" and "Artefact-Y"; the evaluator scores both without
  seeing the producer identity).

**Turn-cost logging entry format:**

```jsonl
{"run": "A", "task": "<slug>", "turns": N, "artefact_path": "swarm/evals/golden/solo-vs-matrix/run-A-<slug>.md", "ts": "2026-MM-DD"}
```

---

### §3.3 Run B — 6-cell matrix-lite protocol

**Setup:** brigadier decomposes the same toy task into cell dispatches.
Minimum 3 cells, maximum 5 cells (matrix-lite per brief). The
dispatched cells must include investor-expert × critic (mandatory, as
investor owns this artefact type) plus at least two of: philosophy ×
critic, systems × scalability, mgmt × integrator.

**Constraints:**
- Each cell has a budget of ≤8 turns per dispatch.
- brigadier integration pass: ≤5 turns.
- Total matrix-lite turn budget: ≤45 turns (3 cells × 8 + integration 5
  + brigadier decompose 2 + brigadier compose 5 = ≤43 turns; round to
  45 for safety).
- All cells receive identical task brief (same inputs as Run A — no
  additional context). The purpose is to measure quality lift from
  multi-perspective analysis, not from additional context loading.
- brigadier writes the integrated artefact to
  `swarm/evals/golden/solo-vs-matrix/run-B-<task-slug>.md`.
- Turn count is logged per cell and total.

**Rationale for matrix-lite (3–5 cells) rather than full 5×4:**
Full 5×4 dispatch on a 15-turn toy task would produce a 300-turn
invocation where coordination overhead dominates the signal. The
comparison would measure "brigadier decomposition overhead" not
"cell-quality premium." Matrix-lite (3–5 cells) is the minimum viable
multi-expert invocation that still tests the quality-premium claim.
[src: investor-optimizer-01.md:148-155]

**Turn-cost logging entry format:**

```jsonl
{"run": "B", "task": "<slug>", "cells_dispatched": N, "total_turns": N, "artefact_path": "swarm/evals/golden/solo-vs-matrix/run-B-<slug>.md", "ts": "2026-MM-DD"}
```

---

### §3.4 Quality rubric (5 binary checks)

The rubric is applied identically to Run A and Run B outputs. Each
check is pass (1) or fail (0). Evaluator is philosophy-expert × critic
(blind to producer identity per §3.2 double-blind protocol).

**RC-1 — Conformance to done-predicate (task completion).**
"Does the artefact satisfy the Hamel-binary done-predicate for the
selected candidate task (T-A, T-B, or T-C)?" Pass = done-predicate
fully satisfied. Fail = any done-predicate condition not met.
This is the hardest check: no partial credit. An artefact that misses
one condition (e.g., moat analysis with only 1 kill-condition instead of
≥2) fails RC-1 entirely.

**RC-2 — Absence of narrative-fallacy (AP-INV-8).**
"Does the artefact contain arithmetic (numbers, formulas, computed
values) as the primary justification, NOT a story?" Pass = primary
justification is arithmetic with at least one computed value per major
claim. Fail = primary justification is narrative ("this is important
because..."; "the market is growing"; "AI changes everything") without
accompanying arithmetic.
Motivation: AP-INV-8 (narrative-fallacy-investing) is the most common
failure mode in solo-brigadier capital artefacts (8/8 conformance
checks failed on it in investor-critic-01). If the matrix improves RC-2
but not RC-1, that is informative.

**RC-3 — Second-level thinking present (Marks pattern P3).**
"Does the artefact state what is ALREADY priced in / already assumed /
already known — not just what the first-level analysis says?" Pass =
explicit "already priced in" or "already assumed" language with at least
one named assumption that the market/consensus holds. Fail = pure
first-level analysis throughout.
Motivation: C7 check from the investor critic rubric; one of the 8
conformance failures in investor-critic-01.

**RC-4 — Invert section present and positioned correctly.**
"Does the artefact contain a failure-mode section that appears BEFORE
the positive case, with ≥2 named failure modes?" Pass = invert/failure
section is the first substantive content block AND lists ≥2 distinct
failure modes. Fail = no failure section, or failure section is after
the positive case, or fewer than 2 failure modes named.
Motivation: C8 check; another of the 8 conformance failures.

**RC-5 — Epistemic-level labelling (F/ClaimScope/R) on at least one
claim.**
"Does the artefact label at least one major claim with (a) a confidence
level or F-level, (b) a scope (where it applies / does not apply), and
(c) a refutation condition?" Pass = ≥1 claim in the artefact carries
all three elements (even informally stated). Fail = no claim carries
these elements.
Motivation: philosophy-critic-01 H-1 (non-falsifiable claims); this is
the philosophy co-domain's contribution to the rubric. A solo-brigadier
pass often omits epistemic labelling; the matrix benefits from the
philosophy-expert × critic dispatched in Run B.

**Rubric total score:** 0–5. Reported separately for Run A and Run B.
**Quality delta = Run B score / Run A score** (or "undefined" if Run A
score = 0; in that case, Run A = 0 is itself the primary finding —
solo-brigadier cannot complete the task).

**2× threshold test:** For ≥3 of 5 checks: Run B passes AND Run A
fails. Specifically: if Run B = 5/5 and Run A = 2/5, then 3 of 5
items show a quality delta (run B pass where run A fails). That
satisfies H1.

---

### §3.5 Measurement protocol summary

| Step | Actor | Output | Location |
|---|---|---|---|
| 1. Run A execution | brigadier solo | artefact | `swarm/evals/golden/solo-vs-matrix/run-A-<slug>.md` |
| 2. Run B execution | brigadier + 3–5 cells | artefact | `swarm/evals/golden/solo-vs-matrix/run-B-<slug>.md` |
| 3. Blind evaluation | philosophy × critic (blind) | rubric JSONL | `swarm/evals/golden/solo-vs-matrix/rubric-eval.jsonl` |
| 4. Turn-cost log | brigadier | JSONL entry × 2 | `swarm/evals/golden/solo-vs-matrix/results.jsonl` |
| 5. Decision table check | investor × integrator (this artefact) | decision | appended to `results.jsonl` |

---

## §4 Null hypothesis / alternative hypothesis (formal)

```yaml
H0:
  claim: >
    The 6-cell matrix does NOT produce quality ≥ 2× solo-brigadier on
    the selected toy task; specifically, ≥3 of 5 rubric items (RC-1..RC-5)
    do NOT show a quality delta (Run B pass where Run A fails).
  F: F1 (assertion; prior to measurement this is the null by convention)
  falsifier: >
    H0 is falsified if Run B passes ≥3 of 5 rubric items where Run A fails
    (quality delta ≥2× on ≥3 items simultaneously).
  ClaimScope:
    holds_when: "measurement substrate exists (swarm/evals/ populated) AND both runs complete AND evaluator is blind to producer"
    not_valid_when: "runs completed on different inputs OR evaluator was not blind"
  R:
    refuted_if: "Run B passes ≥3 of 5 RC checks where Run A fails; receipt: rubric-eval.jsonl"
    accepted_if: "Run B passes <3 of 5 RC checks where Run A fails; receipt: rubric-eval.jsonl"

H1:
  claim: >
    The 6-cell matrix produces quality ≥ 2× solo-brigadier on the
    selected toy task; specifically, ≥3 of 5 rubric items show a quality
    delta (Run B pass where Run A fails).
  F: F1 (assertion; prior to measurement; elevated to F5 if confirmed)
  falsifier: >
    H1 is falsified if Run B passes <3 of 5 rubric items where Run A fails.
  ClaimScope:
    holds_when: "toy task is representative (not cherry-picked toward matrix); matrix-lite ≥3 cells"
    not_valid_when: "toy task is selected for its matrix-friendliness; OR <3 cells dispatched"
  R:
    refuted_if: "quality delta <2× on ≥3 of 5 rubric items; receipt: rubric-eval.jsonl"
    accepted_if: "quality delta ≥2× on ≥3 of 5 rubric items across ≥3 repeated runs (n=3 for full confirmation)"
```

---

## §5 Decision table

| Result | Criterion | Action |
|---|---|---|
| **H0 rejected (H1 supported)** | Run B passes ≥3 of 5 RC items where Run A fails | Proceed with full matrix investment; update MoS from 0.30 to 0.40+ (quality gain confirmed ≥1.5×, above knife-edge); H-8 paid-API memo is unblocked; Bundle C closed. |
| **H0 not rejected** | Run B passes <3 of 5 RC items where Run A fails | Phase-B re-scope: reduce matrix complexity (fewer cells per cycle); consider 1-agent-loop Alternative A from investor-critic-01; HITL escalation — MoS goes negative (ruin floor triggered); investor-expert §1d `escalation-trigger` row "unit-econ-arithmetic produces margin-of-safety ≤0" fires. |
| **Ambiguous: 1.5–2× zone** | Run B passes ≥3 items but delta is <2× (Run A also passes some items that Run B passes) | Revisit at cycle-5 with n=3 repeated trials on different toy tasks; do NOT conclude H1 or retain H0; MoS remains at exactly 0.30 (knife-edge); no new capital deployment; maintain status-quo allocation. |
| **Run A score = 0 (solo fails entirely)** | Run A fails all 5 RC items (solo-brigadier cannot complete the task) | This is a special case: matrix advantage is guaranteed but the baseline is degenerate. Record as "matrix-advantage-on-degenerate-solo" — informative but not the primary H1 confirmation. Re-run with a simpler toy task (T-B if T-A selected). |

---

## §6 Storage — golden-set JSONL schema

All runs are stored in `swarm/evals/golden/solo-vs-matrix/`.

**Directory structure:**

```
swarm/evals/golden/solo-vs-matrix/
  README.md                          (schema documentation)
  results.jsonl                      (one record per run + decision)
  run-A-<task-slug>.md               (Run A artefact)
  run-B-<task-slug>.md               (Run B artefact)
  rubric-eval.jsonl                  (per-item rubric scores from blind evaluator)
```

**results.jsonl schema (per record):**

```jsonl
{
  "record_type": "run | rubric | decision",
  "run": "A | B | eval | decision",
  "task_slug": "<slug>",
  "task_candidate": "T-A | T-B | T-C",
  "cells_dispatched": N,
  "turns_used": N,
  "artefact_path": "<path>",
  "rubric_scores": {"RC-1": 0|1, "RC-2": 0|1, "RC-3": 0|1, "RC-4": 0|1, "RC-5": 0|1},
  "total_score": N,
  "quality_delta": "<float or 'undefined'>",
  "h0_rejected": true|false|null,
  "decision": "proceed | re-scope | ambiguous | degenerate-solo",
  "evaluator_blind": true|false,
  "ts": "2026-MM-DD",
  "cycle_id": "<cycle-id>",
  "notes": ""
}
```

**Relationship to OPP-01 (C-02 Measurement Void):**
This golden set is built ON the OPP-01 substrate (`swarm/evals/`
directory, `run.sh` runner). OPP-01 must ship first. This artefact is
therefore a SEQUENTIAL DEPENDENCY on OPP-01 — same as H-4 is sequenced
after H-1 in Bundle C of investor-optimizer-01.
[src: investor-optimizer-01.md:253-262; SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md:180-186]

---

## §7 Estimated total turns

**Conservative upper-bound estimate:**

| Phase | Actor | Turns |
|---|---|---|
| Experiment setup (create directory, README, schema) | brigadier | 3 |
| Run A execution (solo-brigadier; capped at 15) | brigadier | 15 |
| Run B execution — decompose task | brigadier | 3 |
| Run B execution — 3 cell dispatches × 8 turns each | 3 cells × 8 | 24 |
| Run B execution — brigadier integration | brigadier | 5 |
| Run B execution — brigadier compose final artefact | brigadier | 4 |
| Blind evaluation — philosophy × critic reads both artefacts | philosophy-expert | 10 |
| Turn-cost logging and JSONL writes | brigadier | 3 |
| Decision table evaluation (this investor × integrator artefact already written) | — | 0 |
| **Total conservative upper-bound** | | **67 turns** |

**Note on the 67-turn estimate:** this is a conservative (upper-bound)
figure. In practice, if the toy task selected is T-B (unit-econ
arithmetic, most deterministic), Run A may complete in 8 turns and
Run B cells may average 6 turns each. Lower-bound estimate:
3 + 8 + 3 + 18 + 4 + 3 + 8 + 2 = **49 turns**.

**Relative cost to total cycle turn budget:** the current cycle (T-swarm-
self-improve-v1) is estimated at 370 turns. This experiment at 49–67
turns is 13–18% of a single cycle's turn budget. Kelly-score of the
experiment: E=8, P=7, Payback=3–5 cycles → Kelly = 8 × 7 / 4 = **14.0**
(mid-range; correctly ranked fifth by Kelly in investor-optimizer-01
because measurement infrastructure hypotheses H-6 and H-1 rank higher).
[src: investor-optimizer-01.md:100-118]

---

## §8 Anti-scope (what this experiment DOES NOT claim)

1. **NOT a claim that 6 cells are always better than solo.** The
   experiment tests ONE toy task. Generalisation to all task types
   requires ≥5 different toy tasks spanning different domains and
   complexity levels. One result is one data point.

2. **NOT a claim about information-loading advantage.** Both runs
   receive IDENTICAL inputs. Any quality delta is attributable to
   multi-perspective analysis, not to different context loading. If the
   matrix advantage disappears when inputs are equalised, that is the
   finding.

3. **NOT a claim that the quality rubric (RC-1..RC-5) captures all
   relevant quality dimensions.** The rubric is specifically calibrated
   to investor-expert domain outputs (moat analysis / unit-econ /
   horizon projection). It does not measure: creative insight, novelty,
   communication clarity, or user-rated satisfaction. A different rubric
   on the same artefacts could yield different results.

4. **NOT a claim that 3–5 cells is the optimal matrix size.** Matrix-
   lite (3–5 cells) is chosen for experimental tractability. Full 5×4
   dispatch (20 cells) may show a larger quality premium but at
   proportionally higher turn cost. The experiment measures matrix-lite,
   not the full matrix.

5. **NOT a falsification of H-2 (E-17 Decompose-or-Chat gate).** The
   experiment deliberately runs the matrix on a task that PASSES the
   E-17 threshold (complexity = medium-high; adversarial review needed).
   It does not test whether the gate is correctly calibrated for simple
   tasks.

6. **NOT a claim that the evaluator (philosophy × critic) is the
   authoritative arbiter of quality.** The blind evaluation uses the
   same rubric as the investor critic conformance checklist (C1..C8
   subset). Ruslan's own rating of the artefacts is the ultimate quality
   arbiter. The evaluator produces a structured score; Ruslan may
   disagree with it.

7. **NOT a permanent replacement for ongoing measurement.** One result
   at cycle N is not a sufficient basis for permanent resource allocation.
   If H1 is confirmed here, the experiment should be repeated with ≥2
   additional toy tasks and the results averaged before the swarm
   investment MoS is updated from 0.30 to 0.40+.

---

## §9 Alignment with D-03 and ADD-D-06

**D-03 resolution condition:**
D-03 states the operational resolution is that "no T1/T2 cluster uses
'2×' as a Hamel-binary AP." This experiment is the mechanism by which
the D-03 claim is eventually promoted from F1 (assertion) to F5
(measurement-backed). If H1 is confirmed, the "2×" claim can become
F5 with the following ClaimScope:
- `holds_when: "toy task is investor-domain synthesis; matrix-lite ≥3 cells; inputs are identical across runs; evaluator is blind"`
- `not_valid_when: "task is mechanical arithmetic or code execution (narrow domain); OR matrix dispatches are made with different inputs than solo run"`
D-03 specifically cites philosophy-critic-01 H-1 and engineering-first
path as the two poles. This experiment operationalises the engineering-
first path (install eval harness first, then measure). Philosophy's
requirement (F-level labelling, falsifiability) is satisfied by the
design of §4 (formal H0/H1 with Popper-falsifier) and §3.4 rubric item
RC-5 (epistemic labelling). Both poles of D-03 are addressed.
[src: SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md:238-243]

**ADD-D-06 resolution condition (partial):**
ADD-D-06 disputes the scoring weights (sys 0.35 / kelly 0.25) in the
combined-score formula. This experiment contributes evidence to
ADD-D-06 in the following narrow way: if H0 is rejected (matrix quality
≥2× solo), the Kelly score for the matrix investment increases above
90.0 (currently anchored to an unverified quality gain). If H0 is not
rejected, the Kelly score falls — and the combined-score formula's
Kelly weight should decrease. ADD-D-06 cannot be fully resolved without
≥5 repeated trials across different task types. This experiment is a
necessary input to that resolution, not the resolution itself.
[src: philosophy-integrator-01.md:182-208]

---

## §10 Dissents preserved

Two dissents from the input artefacts that bear on this experiment
design are preserved per §5.3 (investor × integrator dissent
preservation).

**Dissent preserved from D-03 (philosophy position):**
```yaml
position: >
  Even if H1 is confirmed, any future cluster AP that cites "2×" must
  still carry a measurement_substrate field and a baseline_value field
  per philosophy-optimizer B-1 schema. A single golden-set comparison
  does not license general citation of "2×" without these fields in
  the citing artefact.
held_by: philosophy-expert (philosophy-critic-01 H-1; phil-integrator D-03)
F: F4
ClaimScope:
  holds_when: "any artefact cites '2×' as an acceptance predicate or architectural rationale"
  not_valid_when: "the citation is provenance context only (not a gate criterion)"
R:
  refuted_if: "an artefact citing '2×' as a gate criterion includes measurement_substrate + baseline_value fields AND both resolve to non-null paths"
  accepted_if: "any artefact uses '2×' as a gate without those fields; AP-PHIL-1 fires"
  receipt: "swarm/wiki/tasks/<task-id>/artefacts/<cell>-*.md frontmatter on first post-M3 cycle"
```

**Dissent preserved from investor-optimizer-01 internal (H-2 NPV-first):**
```yaml
position: >
  H-4 (this experiment, M3) should have ranked higher than fifth by
  Kelly-score if the ruin-floor consequence of NOT measuring the 2× claim
  is properly priced. At MoS=0.30 knife-edge, the cost of one additional
  cycle without measurement is not 3–5 turns of deferred payback — it
  is 1 cycle of swarm deployment at uncertain quality, which may contaminate
  consulting deliverables. The experiment should be executed at cycle-2,
  not cycle-5.
held_by: investor-expert (internal; investor-optimizer §13 dissent thread)
F: F4
ClaimScope:
  holds_when: "swarm is being used for consulting-adjacent deliverables before H-4 is complete"
  not_valid_when: "all swarm output is internal (no consulting-deliverable exposure) until H-4 complete"
R:
  refuted_if: "consulting deliverables show no quality deficit from swarm assistance before H-4 completes"
  accepted_if: "a consulting deliverable is identified post-mortem as having a quality gap traceable to unvalidated swarm rules"
  receipt: "swarm/wiki/meta/agent-improvements/ post-delivery reviews"
```

**Resolution of the above dissents for this artefact:**
The experiment design satisfies philosophy's B-1 schema requirement by
constructing the measurement substrate before any "2×" citation. The
investor-internal dissent about timing is preserved; the decision on
whether to run M3 at cycle-2 vs cycle-5 belongs to brigadier (post
OPP-01 delivery) and ultimately Ruslan. This artefact specifies the
design; brigadier decides the timing.

---

## §11 Preconditions and blocking dependencies

| Precondition | Required for | Status at artefact creation | Blocking severity |
|---|---|---|---|
| `swarm/evals/` directory exists with `run.sh` runner | Run A and Run B output storage | ABSENT (OPP-01 not yet delivered) | Hard block — experiment cannot run without OPP-01 |
| brigadier §3.0 Decompose-or-Chat gate is operational | Run B to have a documented gate-pass evaluation | Prose-only (H-2 not yet delivered) | Soft block — experiment can run without H-2 but lacks gate-evaluation audit trail |
| Toy task selected by brigadier post-Gate-2 | Both runs | Not yet selected | Hard block — both runs require a selected task |
| philosophy-expert × critic is available for blind evaluation | Step 3 of measurement protocol (§3.5) | Available (existing mode) | No block |
| Golden-set JSONL schema agreed (this §6) | Storage integrity | Defined in this artefact | No block once this artefact is accepted |

**Recommended execution sequence:**
1. OPP-01 (eval harness) ships → creates `swarm/evals/` with `run.sh`.
2. Brigadier selects toy task (T-A, T-B, or T-C) at cycle-2 or cycle-3.
3. M3 experiment runs (67 turns max).
4. Results written to `results.jsonl`.
5. Decision table (§5) applied.
6. Strategies.md entry written under Bundle C (investor-expert, this
   cycle) with the DRR format + Kelly fields per H-6.

---

## §12 Via-negativa (retirement list for the experiment design itself)

Per §6.4 (antifragility check) and Taleb pattern P5 (via-negativa first),
what should be REMOVED from the experiment design before execution:

1. **Remove the "full 5×4" option.** The brief specifies "matrix-lite
   (3–5 cells minimum)." Adding a third run with full 5×4 dispatch
   would increase turn cost by 200–300 turns and introduce orchestration-
   overhead noise into the quality comparison. Removed: full 5×4 option.

2. **Remove the evaluator-knowledge option.** An "informed evaluator"
   (who knows which run is matrix and which is solo) introduces
   confirmation bias risk. The blind protocol is more expensive
   (philosophy × critic must read both artefacts without producer labels)
   but produces cleaner data. Removed: non-blind evaluation option.

3. **Remove repeated-trial averaging from the first run.** n=3 averaging
   is reserved for the ambiguous-zone case (§5 decision table). Running
   3 trials on the first execution costs 3× the turns. Start with n=1;
   upgrade to n=3 only if the result lands in the ambiguous zone.
   Removed: n=3 default; replaced with n=1 default + n=3 conditional.

4. **Remove cross-domain context loading in Run B.** Some matrix designs
   give each cell additional domain-specific context files not given to
   solo-brigadier. This conflates "multi-perspective analysis advantage"
   with "information-loading advantage." The experiment design above
   eliminates this confound. Removed: per-cell additional context loading.

---

## §13 Output packet (shared-protocols §3)

```yaml
summary: >
  Investor × integrator artefact: complete experimental design for M3
  solo-brigadier vs 6-cell matrix golden-set comparison (Gate-1 Option C
  commission). 12 sections covering: background (H-4 MoS=0.30
  knife-edge), problem statement with formal H0/H1 and Popper-falsifier,
  3 toy-task candidates (T-A moat analysis / T-B unit-econ arithmetic /
  T-C horizon projection) for brigadier to select post-Gate-2, Run A and
  Run B protocols, 5-item binary quality rubric (RC-1..RC-5), decision
  table (reject H0 → proceed; not-reject → Phase-B re-scope; ambiguous
  1.5-2× → n=3 at cycle-5), golden-set JSONL schema under
  swarm/evals/golden/solo-vs-matrix/, conservative turn estimate 49–67,
  anti-scope (8 items), D-03/ADD-D-06 alignment, 2 dissents preserved
  (philosophy B-1 schema + investor timing dissent), preconditions
  (OPP-01 hard block), via-negativa retirement of 4 design antipatterns.

proposed_writes:
  - path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-M3-solo-vs-matrix-baseline.md"
    frontmatter:
      id: opportunity-M3-solo-vs-matrix-baseline
      title: "M3 — Solo-brigadier vs 6-cell matrix golden-set baseline (commissioned at Gate 1)"
      type: opportunity-artefact
      cluster_id: S-05
      tier: T2-commissioned
      lead_domain: investor
      co_domains: [philosophy, systems, mgmt]
      dissents_addressed: [D-03, "ADD-D-06 partial"]
      task_id: T-swarm-self-improve-v1-2026-04-23
      produced_by: investor-expert
      mode: integrator
      created: 2026-04-23
      pipeline: ingested
      state: drafted
      confidence: medium
      confidence_method: "arithmetic + judgment"
    body: "(this file)"
    edges_to_add:
      - {from: "opportunity-M3-solo-vs-matrix-baseline", to: "investor-critic-01", type: "derived_from", note: "H-4 MoS=0.30 arithmetic is the motivation"}
      - {from: "opportunity-M3-solo-vs-matrix-baseline", to: "investor-optimizer-01", type: "derived_from", note: "Bundle C H-4→H-8 sequencing logic"}
      - {from: "opportunity-M3-solo-vs-matrix-baseline", to: "philosophy-critic-01", type: "implements", note: "Popper-falsifier requirement on 2× claim (H-1, AP-PHIL-1)"}
      - {from: "opportunity-M3-solo-vs-matrix-baseline", to: "philosophy-integrator-01", type: "addresses", note: "D-03 resolution path + ADD-D-06 partial input"}
      - {from: "opportunity-M3-solo-vs-matrix-baseline", to: "mgmt-integrator-01", type: "derived_from", note: "S-05 cluster identification; M3 hypothesis row"}

provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-critic-01.md", range: "140-165", quote: "MoS = (1.5×150 - 150 - 30)/150 = 0.30 — exactly at the minimum threshold"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/investor-optimizer-01.md", range: "253-262", quote: "H-4→H-8 sequential dependency; H-4 opens the gate for H-8; attempting H-8 before H-4 produces AP-INV-9"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-critic-01.md", range: "139-191", quote: "2× improvement claim F1; AP-PHIL-1; measurement substrate absent; non-falsifiable as written"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-integrator-01.md", range: "130-145", quote: "D-03: operationally resolved — no cluster uses 2× as Hamel-binary AP; philosophy's concern satisfied by scope-restriction"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/mgmt-integrator-01.md", range: "1-50", quote: "S-05 cluster M3: solo-brigadier vs 6-cell matrix golden-set comparison; impact 4; effort 3; risk 2"}
  - {path: "decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md", range: "178-195", quote: "M3 S-05 inv-H4: run once-off comparison; store in swarm/evals/golden/solo-vs-matrix.jsonl"}

confidence: medium
confidence_method: arithmetic + judgment

escalations:
  - trigger: peer-input-needed
    requested: "brigadier selects toy task (T-A, T-B, or T-C) post-Gate-2 per §3.1 selection criterion"
    context_path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-M3-solo-vs-matrix-baseline.md"
  - trigger: peer-input-needed
    requested: "OPP-01 (swarm/evals/ harness) must ship before M3 can execute — hard block declared in §11"
    context_path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-M3-solo-vs-matrix-baseline.md"

dissents:
  - position: "Philosophy B-1 schema requires measurement_substrate + baseline_value on any future artefact that cites 2× as a gate criterion, even after H1 is confirmed here."
    held_by: philosophy-expert (D-03)
    F: F4
    ClaimScope:
      holds_when: "2× cited as Hamel-binary acceptance predicate in any artefact"
      not_valid_when: "cited as provenance context only"
    R:
      refuted_if: "artefact cites 2× as gate with measurement_substrate + baseline_value fields both non-null"
      accepted_if: "artefact cites 2× as gate without those fields; AP-PHIL-1 fires"
      receipt: "swarm/wiki/tasks/<post-M3-cycle>/artefacts/ frontmatter scan"
  - position: "M3 experiment should run at cycle-2, not cycle-5; MoS knife-edge risk is not adequately priced by deferring to cycle-5."
    held_by: investor-expert (internal; investor-optimizer §13)
    F: F4
    ClaimScope:
      holds_when: "swarm is used for consulting-adjacent deliverables before M3 completes"
      not_valid_when: "all output is internal-only until M3 complete"
    R:
      refuted_if: "no consulting quality deficit detected before M3 completes"
      accepted_if: "post-delivery review identifies quality gap traceable to unvalidated swarm rules"
      receipt: "swarm/wiki/meta/agent-improvements/ post-delivery reviews"
```

---

*Investor-expert. Mode: integrator. Cycle: cyc-swarm-self-improve-v1-2026-04-23.*
*Lead domain: investor. Co-domains: philosophy, systems, mgmt.*
*Dissents addressed: D-03 (§9), ADD-D-06 partial (§9). Dissents preserved: 2 (§10).*
*Blocking dependency: OPP-01 (swarm/evals/ harness). Hard block declared §11.*
*Turns used: within ap_budget of 60.*
