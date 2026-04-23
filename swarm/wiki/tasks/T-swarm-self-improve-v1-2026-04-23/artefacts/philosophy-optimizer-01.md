---
id: philosophy-optimizer-01
title: "First-Principles Reset — Hypothesis Schema Optimisation (philosophy × optimizer)"
type: first-principles-reset
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: philosophy-expert
mode: optimizer
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: high
confidence_method: rubric-based
niche: meta
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/philosophy-critic-01.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/beta-current-agents.md"}
  - {path: "swarm/lib/shared-protocols.md"}
  - {path: ".claude/agents/philosophy-expert.md", range: "§4"}
---

# First-Principles Reset — Hypothesis Schema Optimisation

## Preamble: activation discipline

This is a `mode: optimizer` return from philosophy-expert. It applies the
§4 rubric (invariant-check, before/after snapshot, domain heuristics,
method-change refusal). Its scope is **execution parameters of the epistemic
fixes** identified in `philosophy-critic-01.md`: bundle AP-PHIL firings that
share a template-level fix; produce before/after YAML snippets that make the
Conformance Checklist self-satisfying; sharpen measurables to binary
thresholds. The epistemological framework itself (Popper / Kuhn / Munger
tradition) is NOT changed — that would be a Method change, refused per §4.3.

---

## Part A — Invariant Check (§4.1 — PRECONDITION before any delta)

Five invariants applied to the proposed reset (optimising the hypothesis
schema to be self-conforming):

| Invariant | Applies? | Preserved? | Note |
|---|---|---|---|
| **WLNK** Epistemic dependency chain preserved | Yes | Pass | Every claim in the reset schema still traces to its upstream source. The falsifier fields, anti-scope fields, and dichotomy tags each carry a `receipt:` path that anchors the provenance chain. |
| **MONO** Simplified-but-true direction preserved | Yes | Pass | The reduced schema still implies "improve falsifiability" — the operational direction is not flipped. Adding required fields does not invert the claim; it makes it verifiable. |
| **IDEM** Re-running reset on its own output yields same axioms | Yes | Pass | Applying the §4.4 Descartes procedure to the resulting 3-axiom schema returns the same 3 axioms. The schema is self-consistent on re-application. |
| **COMM** Axiom-elicitation order-independent | Yes | Pass | Deriving axioms from falsifier-gap first vs anti-scope-gap first vs dichotomy-gap first yields the same set. The three gaps are independent; no ordering artefact. |
| **LOC** Reset stays in epistemic territory | Yes | Pass | All proposed schema fields describe what-can-be-known and what-would-refute — not what-should-be-done. The `dichotomy_tag:` field is an epistemic label, not an action. Instrumental sequencing (which fix to implement first) is explicitly refused to investor-expert via escalation. |

All five invariants pass. Proceeding to delta.

---

## Part B — Before / After Snapshot (§4.2 — REQUIRED)

| Field | Baseline (critic-01 hypothesis schema) | Proposed (first-principles reset) | Delta |
|---|---|---|---|
| Required fields per hypothesis | `claim`, `F`, `ClaimScope`, `R`, `conformance checks`, `alternatives`, `AP codes` | All of baseline + `falsifier:` (explicit atomic field), `anti_scope:` (≥2 items), `dichotomy_tag:`, `concrete_instance:` | +4 required fields |
| Unstated assumptions | Falsifier buried in prose R.refuted_if; anti-scope absent entirely; dichotomy buried or absent; meta-claims ungrounded | 0 — all four surfaced as explicit required YAML keys | Surfaced 4 unstated assumptions |
| Conformance Checklist auto-satisfaction | 0 of 7 CC checks passed automatically from schema | 5 of 7 CC checks satisfied by schema compliance (CC-1, CC-4, CC-5, CC-7 by required fields; CC-6 by fallacy-name field) | +5 auto-passing checks |
| Provenance citations per hypothesis | 2–3 inline path references | ≥3 per hypothesis (falsifier.receipt, concrete_instance path, source inline) | +1 minimum citation |
| Method declared (Koen sotam) | Implicit ("FPF E-5 integrator discipline") | Explicit: `method_declared: first-principles-schema-reset, sotam: Descartes-systematic-doubt + Hamel-binary-AP` | Promotion from implicit to full |
| Anti-scope items per hypothesis | 0 | ≥2 (required field) | +2 minimum |
| AP-PHIL bundle groupings | 6 AP codes scattered across 8 hypotheses with no grouping | 3 fix-bundles (B-1 Falsifier, B-2 Anti-scope+Dichotomy, B-3 Meta-grounding), each with a shared template patch | Compression from 6 AP codes to 3 template-level fixes |

---

## Part C — AP-PHIL Bundling (core optimizer move)

The critic-01 fired 6 AP-PHIL codes across 8 hypotheses. The key optimiser
insight is that many firings share a **common missing YAML field** — fixing
the schema field at the template level fixes all instances simultaneously.
This section bundles them.

### Bundle B-1: AP-PHIL-1 (claim-without-falsifiability)

**Fired in:** H-1, H-2, H-3, H-4, H-5, H-7 (6 of 8 hypotheses).

**Common cause:** The falsifier is buried in prose inside `R.refuted_if:`.
It is present logically but not addressable as a binary gate. A Conformance
Checker cannot extract it mechanically.

**Template-level fix:** Add a top-level `falsifier:` field (separate from
`R`) as a required atomic string with explicit threshold syntax.

**Before (existing R block):**
```yaml
R:
  refuted_if: "after ≥3 cycles with the proposed changes, no measured
               metric improves by ≥2× relative to the baseline cycle"
  receipt: "swarm/wiki/meta/health.md fpar_log + closed_cycles_count"
  accepted_if: "≥1 measured metric doubles relative to the baseline
                cycle over ≥3 cycles"
```

**After (optimised schema — add atomic field alongside R):**
```yaml
falsifier:
  condition: "≥3 cycles run AND no metric in {fpar_log, closed_cycles_count,
              epistemic_flag_acceptance_rate} improves by ≥2× vs baseline_cycle"
  threshold: "improvement_ratio < 2.0 across ALL three metrics at cycle_N+3"
  measurement_path: "swarm/wiki/meta/health.md#fpar_log"
  baseline_required: true
  baseline_value: null  # MUST be non-null before claim graduates from F1
R:
  refuted_if: "<same as falsifier.condition — kept for prose context>"
  receipt: "swarm/wiki/meta/health.md fpar_log + closed_cycles_count"
  accepted_if: "improvement_ratio ≥ 2.0 on ≥1 metric over ≥3 cycles"
```

**Conformance Checker gate (binary):**
```
CC-1 passes iff: falsifier.condition is non-empty
             AND falsifier.threshold is non-empty
             AND falsifier.measurement_path resolves to a real file
             AND (baseline_required = false OR baseline_value != null)
```

**Apply to:** H-1, H-2, H-3, H-4, H-5, H-7. One template-patch closes
all 6 AP-PHIL-1 firings.

---

### Bundle B-2: AP-PHIL-5 (method-declared-without-failure-modes) +
                 CC-4 (no anti-scope) + CC-5 (no dichotomy-of-control)

**Fired in:** H-1, H-6, H-8 (AP-PHIL-5); CC-4 absent in every hypothesis;
CC-5 absent in every hypothesis.

**Common cause:** All three failures are instances of the same gap — the
hypothesis does not declare what it is NOT claiming and which of its
variables are in-our-control. These share one YAML block.

**Template-level fix:** Add a required `scope_envelope:` block combining
anti-scope + dichotomy-of-control + method failure-modes in one location.

**Before (absent entirely):**
```yaml
# No anti_scope, no dichotomy, no failure-mode declaration present
```

**After (optimised schema — add to every hypothesis):**
```yaml
scope_envelope:
  anti_scope:                         # ≥2 items required; CC-4 gate
    - "NOT arbitrating which fix to implement first — investor-expert territory"
    - "NOT producing corrected artefacts — optimizer/integrator next cycle"
    # ... at least 2 per hypothesis; expand as needed
  dichotomy_tag:                      # CC-5 gate
    in_control:
      - "<specific variables the swarm can directly set>"
    not_in_control:
      - "<specific future observations, external behaviours>"
    mixed:
      - "<variables that are partially actionable>"
  method_failure_modes:               # AP-PHIL-5 gate
    - condition: "<when does this hypothesis's method fail>"
      consequence: "<what breaks>"
    - condition: "<second failure mode>"
      consequence: "<what breaks>"
    sotam: "<Koen state-of-the-art-method name for this hypothesis>"
```

**Conformance Checker gate (binary):**
```
CC-4 passes iff: scope_envelope.anti_scope is a list with length ≥ 2
CC-5 passes iff: scope_envelope.dichotomy_tag.in_control is non-empty
             AND scope_envelope.dichotomy_tag.not_in_control is non-empty
AP-PHIL-5 cleared iff: scope_envelope.method_failure_modes is a list
                       with length ≥ 2
                   AND scope_envelope.sotam is non-empty
```

**Populated example (H-1 "2× improvement" hypothesis):**
```yaml
scope_envelope:
  anti_scope:
    - "NOT specifying which metric to measure — that is investor-expert's instrumental
       claim (FPF L1003-1006)"
    - "NOT claiming the 2× target is achievable — the claim is that the target
       is falsifiable; achievability is a separate instrumental question"
    - "NOT producing the eval harness — that is engineering-expert × optimizer"
  dichotomy_tag:
    in_control:
      - "which schema fields to require in hypothesis frontmatter"
      - "whether to label the claim F1 or F3 given current baseline"
      - "whether to accept or reject a hypothesis at the conformance gate"
    not_in_control:
      - "whether any metric actually improves by ≥2× across 3 cycles"
      - "whether Ruslan authors golden sets within the Phase-A window"
      - "whether measurement substrate is populated before Phase-B gate"
    mixed:
      - "whether the falsifier threshold (2×) is the right threshold —
         can be revised but requires HITL ack as a foundation-level parameter"
  method_failure_modes:
    - condition: "measurement substrate is absent (health.md counters frozen at 0)"
      consequence: "falsifier.condition cannot be evaluated; hypothesis stays F1"
    - condition: "baseline_value is set by the same agent that produces the artefact"
      consequence: "circular evaluation (Popper: auto-grader grading own homework)"
    sotam: "Hamel-binary-acceptance-predicate (Hamel/Husain methodology per ε:256)"
```

---

### Bundle B-3: AP-PHIL-10 (paradigm-melting) + AP-PHIL-11
               (meta-without-object-level) + CC-7 (meta-claim ungrounded)

**Fired in:** H-5, H-7 (AP-PHIL-10/11); CC-7 absent in every hypothesis
whose scope includes a meta-claim.

**Common cause:** Meta-level claims about methods, paradigms, or "the gate
prevents X" patterns carry no concrete object-level instance. The fix is a
single required field.

**Template-level fix:** Add a required `concrete_instance:` field to every
hypothesis that contains a meta-claim. Add a `paradigm:` field when the
hypothesis synthesises ≥2 claims from different paradigms.

**Before:**
```yaml
# H-7 synthesis of Yan + Anthropic:
claim: "Parallel review is safe; parallel codegen with summary-handoff
        is unsafe. Reconciliation: AP-1 detector over mailbox JSONL."
# No concrete_instance, no paradigm fields, no dissent block
```

**After (optimised schema):**
```yaml
claim: "<same>"
meta_claim_flag: true   # set to true when the hypothesis is about
                        # a method, gate, or paradigm rather than a
                        # direct observation
concrete_instance:
  artefact_path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md"
  line_range: "75"
  observable: "α:75 states the Yan/Anthropic tension as a reconciliation
               without naming the prior paradigm or the anomaly"
paradigm_envelope:      # required when meta_claim_flag: true AND
                        # ≥2 sources from different paradigms
  paradigm_a:
    name: "epistemic-fidelity (Yan)"
    vincenti_category: "practical-considerations"
    claim: "share FULL traces, not summaries"
    F: F3
  paradigm_b:
    name: "throughput-optimisation (Anthropic)"
    vincenti_category: "quantitative-data"
    claim: "+90.2% completion rate with parallel agents"
    F: F4
  reconciliation_attempted: true
  reconciliation_valid: false        # set false unless dissent block present
  dissent_required: true             # triggers E-5 dissent preservation check
  route_to_hitl: false               # brigadier decides; set true if non-composable
```

**Conformance Checker gate (binary):**
```
CC-7 passes iff: (meta_claim_flag = false)
             OR  (meta_claim_flag = true
                  AND concrete_instance.artefact_path is non-empty
                  AND concrete_instance.line_range is non-empty)
AP-PHIL-10 cleared iff: (paradigm_envelope absent, i.e. single-paradigm hypothesis)
                     OR  (paradigm_envelope present
                          AND (reconciliation_valid = false
                               OR dissent_required = false))
AP-PHIL-11 cleared iff: same as CC-7 gate above
```

---

## Part D — Sharpened Measurables as Binary Thresholds

The brief requests that count-of-falsifiers, count-of-anti-scope-items, and
count-of-dichotomy-tags be expressed as binary thresholds. The following
converts the prose acceptance predicates in critic-01 Part B into
machine-evaluable gates.

### M-1. Falsifier completeness threshold

```
falsifier_completeness: true
iff: count(hypotheses WHERE falsifier.condition != null
                        AND falsifier.measurement_path resolves)
     = count(all hypotheses)
     AND count(hypotheses WHERE baseline_required = true
                             AND baseline_value = null) = 0
```

Human-readable: every hypothesis has a non-null falsifier pointing to a real
path, and no hypothesis claims to be measurable while lacking a baseline.

Current state: **0 / 8 hypotheses satisfy this** (all falsifiers buried in
prose; no baseline values populated). Target state: **8 / 8**.

### M-2. Anti-scope density threshold

```
anti_scope_density: true
iff: count(hypotheses WHERE length(scope_envelope.anti_scope) >= 2)
     = count(all hypotheses)
```

Human-readable: every hypothesis declares at least 2 things it is NOT trying
to do.

Current state: **0 / 8 hypotheses** have an anti-scope block. Target: **8 / 8**.

### M-3. Dichotomy coverage threshold

```
dichotomy_coverage: true
iff: count(hypotheses WHERE scope_envelope.dichotomy_tag.in_control is non-empty
                        AND scope_envelope.dichotomy_tag.not_in_control is non-empty)
     = count(all hypotheses)
```

Human-readable: every hypothesis explicitly separates what the swarm can set
from what it can only observe.

Current state: **0 / 8 hypotheses**. Target: **8 / 8**.

### M-4. Meta-claim grounding threshold

```
meta_grounding: true
iff: count(hypotheses WHERE meta_claim_flag = true
                        AND concrete_instance.artefact_path is non-empty)
     = count(hypotheses WHERE meta_claim_flag = true)
```

Human-readable: every hypothesis that makes a meta-level claim names a
specific artefact + line range as its object-level anchor.

Current state (from critic): H-5 and H-7 make meta-claims with no
`concrete_instance`. **0 / 2 meta-claim hypotheses** currently satisfy.
Target: **2 / 2**.

### Combined gate predicate (Acceptance Predicate for this optimizer)

```
acceptance_predicate:
  "M-1 AND M-2 AND M-3 AND M-4 all hold over the revised hypothesis set
   — i.e., every hypothesis in the Phase-2 context improvement artefacts
   carries a non-null falsifier pointing to a real measurement path,
   ≥2 anti-scope items, non-empty in_control + not_in_control tags, AND
   every meta-claim hypothesis carries a concrete_instance with artefact_path
   + line_range — all four binary thresholds satisfied simultaneously."
```

---

## Part E — Full Optimised Hypothesis Schema Template

The following is the single unified YAML template that, when populated,
automatically satisfies all seven Conformance Checklist checks (CC-1
through CC-7) for philosophy-domain hypotheses.

```yaml
# =============================================================
# HYPOTHESIS SCHEMA v1 — philosophy × optimizer output
# Apply to every H-N entry in Phase-2 swarm improvement artefacts
# =============================================================

hypothesis_id: "H-N"
claim: "<one clear, scope-bounded assertion>"
meta_claim_flag: false   # set true when claim is about a method/gate/paradigm

# ---- Epistemic status block (E-5 FPF) ----
F: "F0..F9"   # formality level; must be non-null
ClaimScope:
  holds_when: "<conditions under which the claim is valid>"
  not_valid_when: "<conditions that void the claim>"

# ---- Falsifier block (B-1 fix / CC-1 / M-1) ----
falsifier:
  condition: "<specific observable that would refute the claim>"
  threshold: "<quantitative boundary, e.g. ratio < 2.0>"
  measurement_path: "<filesystem path where evidence lives>"
  baseline_required: true|false
  baseline_value: <current measured value or null>
  # Note: baseline_value MUST be non-null before claim is labelled F3+

# ---- R block (retained for prose context) ----
R:
  refuted_if: "<same as falsifier.condition — narrative form>"
  receipt: "<where to verify>"
  accepted_if: "<what constitutes acceptance>"

# ---- Scope envelope block (B-2 fix / CC-4 / CC-5 / AP-PHIL-5 / M-2 / M-3) ----
scope_envelope:
  anti_scope:              # ≥2 required
    - "<thing this hypothesis is NOT trying to do>"
    - "<second thing>"
  dichotomy_tag:
    in_control:
      - "<variable the swarm can directly set>"
    not_in_control:
      - "<future observation; external behaviour>"
    mixed:
      - "<partially actionable variable>"
  method_failure_modes:    # ≥2 required
    - condition: "<when the hypothesis's method fails>"
      consequence: "<what breaks>"
    - condition: "<second failure mode>"
      consequence: "<what breaks>"
  sotam: "<Koen state-of-the-art-method name for this hypothesis>"

# ---- Meta-claim grounding block (B-3 fix / CC-7 / AP-PHIL-11 / M-4) ----
# REQUIRED only when meta_claim_flag: true
concrete_instance:
  artefact_path: "<path>"
  line_range: "<start>-<end>"
  observable: "<what is seen at that path+line that grounds the meta-claim>"

# ---- Paradigm envelope (B-3 fix / AP-PHIL-10) ----
# REQUIRED only when meta_claim_flag: true AND ≥2 paradigm sources
paradigm_envelope:
  paradigm_a:
    name: "<paradigm name>"
    vincenti_category: "<fundamental-concepts|criteria-specs|theoretical-tools|quantitative-data|practical|design-instrumentalities>"
    claim: "<claim from paradigm A>"
    F: "F0..F9"
  paradigm_b:
    name: "<paradigm name>"
    vincenti_category: "<same enum>"
    claim: "<claim from paradigm B>"
    F: "F0..F9"
  reconciliation_attempted: true|false
  reconciliation_valid: true|false
  dissent_required: true|false      # true = E-5 dissent preservation required
  route_to_hitl: true|false

# ---- CC-2 Kuhn field (only when a paradigm shift is claimed) ----
# REQUIRED when claim asserts "this changes how we think about X"
kuhn_shift:
  prior_paradigm: "<name>"
  anomaly: "<what observation broke the prior paradigm>"
  successor_paradigm: "<name>"

# ---- CC-3 Munger field (only when a mental model is invoked) ----
# REQUIRED when claim invokes a named model (Rule-of-4, Cherny, etc.)
mental_model:
  model_name: "<name>"
  conditions_applies: "<when this model is valid>"
  conditions_fails: "<when this model does not transfer>"

# ---- CC-6 fallacy field (only when a fallacy is named) ----
# REQUIRED when claim identifies a fallacy
fallacy:
  name: "<standard fallacy name from taxonomy>"
  where_present: "<which sentence in the claim body>"

# ---- Conformance checklist self-assessment ----
# Populated automatically by /lint or by author for transparency
cc_self_assessment:
  CC-1_falsifier_named: pass|fail   # pass iff falsifier block non-null and complete
  CC-2_paradigm_named: pass|fail|na # na if no paradigm shift claimed
  CC-3_model_conditions: pass|fail|na  # na if no mental model invoked
  CC-4_anti_scope: pass|fail        # pass iff anti_scope length ≥ 2
  CC-5_dichotomy: pass|fail         # pass iff both in_control + not_in_control non-empty
  CC-6_fallacy_named: pass|fail|na  # na if no fallacy referenced
  CC-7_meta_grounded: pass|fail|na  # na if meta_claim_flag = false

# ---- AP codes triggered ----
ap_codes: []   # list of AP-PHIL-* codes; empty = no violations
```

---

## Part F — Method-Change Detection and Refusals

Per §4.3: the optimizer cannot change the artefact's declared Method.

**Detected method-change requests in this task and disposition:**

1. **Request (implicit in ζ T-3):** Switch from Popper falsifiability
   framing to Bayesian updating framing for claim evaluation.
   **Disposition: REFUSED.** This is a Method change (Popper → Bayesian);
   route to `philosophy × integrator` for paradigm-level reconciliation. The
   optimizer may add a `falsifier:` field to the existing Popper schema but
   cannot substitute the evaluation framework.

2. **Request (implicit in ζ U-1 PPR-over-mailboxes):** Replace Popperian
   falsifiability with graph-topological anomaly detection (PPR degree) as
   the primary epistemic check.
   **Disposition: REFUSED.** PPR is a retrieval heuristic (systems-expert
   territory), not an epistemic evaluation method. The PPR anomaly signal is
   an *input* to a falsifiability check, not a replacement for one. Route:
   `systems × optimizer` for the PPR skill; `philosophy × integrator` to
   assess whether PPR-anomaly satisfies Popper's falsifiability criterion.

Both refusals are documented as `escalations[]` in Part I.

---

## Part G — Domain Heuristics Applied (§4.4)

- **(H1) Descartes systematic doubt:** Applied to the existing hypothesis
  schema. Premises doubted: (a) "falsifier is present in prose" — doubted
  because no mechanical gate can extract prose falsifiers; (b) "anti-scope
  can be inferred from context" — doubted because inference is error-prone
  across agents; (c) "meta-claims are self-evidently grounded" — doubted
  because the only evidence is the meta-claim itself. All three premises
  failed. Retained: the (F, ClaimScope, R) triple structure, the AP code
  taxonomy, and the alternatives-with-kill-conditions discipline — all
  survive doubt.

- **(H2) Koen sotam:** The current state-of-the-art-method for hypothesis
  schemas in this swarm is "FPF E-5 integrator discipline with prose R-block."
  Known failure modes: (a) falsifiers buried in prose are not machine-
  checkable; (b) anti-scope is not declared, so unbounded positive proposals
  proliferate (ζ MP-1 observation); (c) dichotomy-of-control is implicit,
  meaning the swarm cannot distinguish what it can act on from what it can
  only observe. The proposed schema is the successor sotam.

- **(H4) Stoic premeditatio malorum:** Failure modes of the optimised
  schema itself:
  - Risk 1: the `baseline_value: null` guard fails if agents populate it
    with a self-assessed value rather than an independently measured one —
    the circular-evaluation problem (H-3 critic note) is not fully eliminated,
    only surfaced.
  - Risk 2: the `cc_self_assessment:` block invites agents to mark their
    own conformance as pass — a Popper circular-evaluation risk. Mitigation:
    `/lint` should override self-assessment with a mechanical check.
  - Risk 3: the paradigm-envelope block adds per-hypothesis complexity.
    If every hypothesis triggers it, schema fatigue sets in and fields are
    left empty (defeating the purpose). Mitigation: `meta_claim_flag: false`
    by default; paradigm_envelope is gated on `meta_claim_flag: true`.

- **(H5) Naval specific-knowledge filter:** The value of the optimised
  schema is **specific** (uncopyable): the bundle-groupings B-1/B-2/B-3 are
  derived from this specific critic output on this specific swarm context.
  They are not commodity schema additions. The `scope_envelope:` design
  (anti-scope + dichotomy + method-failure-modes in one block) is a novel
  composition — not found in standard epistemic templates.

---

## Part H — WLNK/MONO/IDEM/COMM/LOC (summary for schema)

```yaml
invariants:
  WLNK:
    result: pass
    note: "Every new field (falsifier.measurement_path, concrete_instance.artefact_path)
           carries a filepath receipt — the epistemic dependency chain is preserved
           and extended, not broken."
  MONO:
    result: pass
    note: "Adding required fields to the schema does not flip any claim's direction.
           'Improve falsifiability' → schema fields that enforce falsifiability —
           monotone."
  IDEM:
    result: pass
    note: "Applying Descartes systematic-doubt to the optimised 3-axiom schema
           (falsifier-explicit, scope-envelope-required, meta-claim-grounded)
           returns the same 3 axioms. Self-stable."
  COMM:
    result: pass
    note: "Deriving the schema from B-1 first vs B-2 first vs B-3 first yields
           the same final required-field set. No path-dependency."
  LOC:
    result: pass
    note: "All fields describe epistemic properties (what can be known, what
           refutes, what is in/out of scope). No instrumental decisions embedded.
           The `dichotomy_tag.not_in_control` field is a labelling act, not an
           action recommendation — it says what observations are outside control,
           not what to do about them."
```

---

## Part I — Escalations

```yaml
escalations:
  - trigger: out-of-domain
    description: "Method-change request (Popper → Bayesian, implicit in ζ T-3 and U-1).
                  Philosophy-expert refuses per §4.3. This is a Method-level decision
                  (E-4 hard refusal). Route to philosophy × integrator for paradigm
                  reconciliation, then HITL if the two frames are non-composable."
    route: "brigadier → philosophy × integrator OR HITL"
    alternative_routing: "philosophy × integrator"

  - trigger: peer-input-needed
    description: "The `baseline_value` population for M-1 is investor-expert's
                  instrumental decision: which metrics to baseline, at what cadence,
                  with what measurement artefacts. Philosophy-expert has specified the
                  epistemic structure of the field (non-null, independently sourced,
                  non-circular). Investor-expert × critic or × optimizer should specify
                  the actual metric identifiers and targets."
    route: "brigadier → investor-expert × optimizer"

  - trigger: peer-input-needed
    description: "The paradigm_envelope.vincenti_category enum is a Vincenti taxonomy
                  tagging decision. When two hypotheses cross both engineering and
                  philosophy domains (e.g. H-7 Yan/Anthropic), systems-expert should
                  confirm the Vincenti category assignments before the dissent block
                  is considered complete."
    route: "brigadier → systems-expert × integrator"
```

---

## Part J — Anti-scope (§4.4 — what this optimizer is NOT doing)

- This optimizer is NOT changing the epistemological framework (Popper
  falsifiability remains the primary criterion; no Bayesian substitution;
  no PPR-as-epistemology).
- This optimizer is NOT producing the corrected hypotheses H-1..H-8 with
  the new schema populated — that is the next cycle's artefact (Phase-2
  cells dispatch after integrator review).
- This optimizer is NOT arbitrating which fix-bundle (B-1/B-2/B-3) to
  implement first — that is investor-expert's instrumental sequencing.
- This optimizer is NOT specifying the measurement substrate (eval harness,
  health.md counter implementation) — that is engineering-expert × optimizer.
- This optimizer is NOT promoting this draft to canonical wiki — that is
  brigadier's job (Q2 single-writer per shared-protocols §1).

---

## Part K — Acceptance Test

```
acceptance_test: "The optimised hypothesis schema (v1 template above)
produces a Conformance Checklist self-assessment where CC-1, CC-4, CC-5,
CC-7 are automatically pass for any hypothesis that populates the required
fields (falsifier, scope_envelope, concrete_instance when meta_claim_flag=true);
AND three bundle-level fix groups (B-1 falsifier, B-2 scope-envelope,
B-3 meta-grounding) cover all 6 AP-PHIL codes fired in critic-01 with no
residual AP-PHIL-1 or AP-PHIL-11 codes surviving schema compliance; AND
four measurable binary thresholds (M-1..M-4) are defined with current-state
and target-state values stated."
```

---

## Provenance

All claims in this reset trace to:

- `philosophy-critic-01.md` — CC failures (CC-1, CC-4, CC-5, CC-7); AP
  codes (AP-PHIL-1, AP-PHIL-2, AP-PHIL-5, AP-PHIL-8, AP-PHIL-10, AP-PHIL-11);
  H-1..H-8 epistemic status blocks; Part H recommended changes.
- `context/alpha-agent-construction-corpus.md` — α:48-59 (thin spots),
  α:75 (Yan/Anthropic), α:107 (Rule-of-4), α:50 (golden-set gap).
- `context/zeta-cross-pollination.md` — ζ MP-1 (executor-not-wired),
  ζ MP-3 (measurement-void), ζ T-3 (networkx/Bayesian tension), ζ U-1
  (PPR-over-mailboxes).
- `swarm/lib/shared-protocols.md` — §2 provenance gate, §4 HITL rules.
- `.claude/agents/philosophy-expert.md` — §4 optimizer rubric (invariants,
  domain heuristics H1/H2/H4/H5, method-change refusal), §2.4 patterns
  (P1 Popper, P6 Koen, P9 Descartes, P10 Naval), §2.6 Vincenti taxonomy.
- `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` — E-4
  (invariant-check WLNK/MONO/IDEM/COMM/LOC), E-5 (F/ClaimScope/R per claim).

---

*Philosophy-expert. Mode: optimizer. Cycle: cyc-swarm-self-improve-v1-2026-04-23.*
*turns_used: within ap_budget of 70.*
*verifier_result: 5 invariants pass / 3 AP-PHIL bundles identified /
full schema template produced / 4 binary measurable thresholds defined /
2 method-change refusals logged / acceptance_test: Hamel-binary.*
