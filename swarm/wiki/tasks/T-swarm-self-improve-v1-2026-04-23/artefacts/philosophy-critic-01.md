---
id: philosophy-critic-01
title: "Epistemic Audit — T-swarm-self-improve-v1 Phase 2 critic pass"
type: epistemic-audit
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: philosophy-expert
mode: critic
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: high
confidence_method: rubric-based
niche: meta
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/beta-current-agents.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/delta-memory-sota.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md"}
  - {path: "swarm/lib/shared-protocols.md", range: "55-130"}
---

# Epistemic Audit — Swarm Self-Improvement v1

## Preamble: activation discipline

This is a `mode: critic` return from philosophy-expert. It runs the §3
rubric (Conformance Checklist, Acceptance Predicate, ≥2 Alternatives,
Anti-scope, BA-Cycle-lite). Its scope is **epistemic integrity** of
the Phase-2 context extractions (α..ζ) and the specific focus questions
named in the brief. It does NOT arbitrate capital allocation, code
craft, or operational scheduling — those belong to other domain experts.

---

## Part A — Conformance Checklist (§3.1 — 7 binary checks over the
context corpus as a whole)

The "artefact under review" is the 6-extraction corpus (α..ζ) that
will seed Phase-2 cell decisions. Each check is applied to the corpus
as a whole, not to any single extraction.

| Check | Name | Result | Evidence |
|---|---|---|---|
| CC-1 | Falsifier-named (Popper) | **FAIL** | Multiple load-bearing claims lack explicit falsifiers. E.g. α: "the matrix is operationally thin" [α:48] — no stated falsifier. ζ MP-1: "Jetix is over-specified and under-executed" [ζ:97] — no falsifier named. Details in H-1, H-2 below. |
| CC-2 | Paradigm-named on shift (Kuhn) | **FAIL** | ζ names multiple paradigm crossings (Yan vs Anthropic, CE-canon vs current) without supplying `prior_paradigm:` + `anomaly:` fields. β's "inconsistency" observation slides paradigm-level problems and style-level ones into one bucket without declaring which is operative. Details in H-3. |
| CC-3 | Mental-model + applicable-conditions cited (Munger) | **PARTIAL PASS** | δ cites HippoRAG, MemGPT, CODE with source anchors and applicable conditions (scale thresholds, Phase-A feasibility flags). β invokes "AP-5 self-violation" as a mental model but gives no condition-boundary — AP-5 applies to prompt-level prohibitions, not to all soft defaults; the distinction is not drawn. |
| CC-4 | Method declares what it is NOT (via-negativa, Stoic) | **FAIL** | No extraction carries an explicit `anti_scope:` block. ζ's emergent ideas have no "we are NOT trying to do X" declarations. The 2× surfaces in every extraction are unconstrained positive proposals without via-negativa. This is the most pervasive gap. |
| CC-5 | Dichotomy-of-control identified for meta-decisions | **FAIL** | The "2× improvement" claims throughout are action recommendations. None tag which variables are in-our-control vs not-in-our-control. E.g. α's "Author the golden sets before Phase B" — authoring is in-control, but whether the acceptance-predicate rubric holds is a FUTURE OBSERVATION not in control today. No dichotomy split present. |
| CC-6 | Fallacy-named-when-named | **PARTIAL PASS** | α names "analogical, not a verbatim precedent" for the matrix 5×4 claim — this is weak but names the fallacy type. ζ's "Jetix is over-specified" is a composition fallacy (aggregating 5 independent domain findings into one verdict) but the fallacy is not named. |
| CC-7 | Meta-claim grounded in object-level | **FAIL** | ζ MP-1 through MP-4 are meta-pattern claims with general citations (e.g. "5 of 5 extractions say X") but no per-claim `concrete_instance:` field. ζ U-1 through U-6 are emergent syntheses presented as new truths without grounding in a specific observable. |

**Overall corpus conformance: 0 full pass / 2 partial pass / 5 fail.**
This is below the ≥5 binary pass threshold. The corpus as written will
produce epistemically fragile Phase-2 decisions unless the failures
in CC-1, CC-4, CC-5, CC-7 are addressed.

---

## Part B — Acceptance Predicate (§3.2 — Hamel-binary)

```
acceptance_predicate: "Every load-bearing improvement hypothesis in the
Phase-2 context corpus carries (a) a named falsifier specifying what
observation would refute it, (b) an explicit anti_scope block naming
≥2 things it is NOT trying to do, (c) a dichotomy-of-control tag
distinguishing variables in-our-control from those not-in-our-control,
AND (d) a concrete_instance: field grounding every meta-pattern claim in
at least one named artefact path + line-range — all holding across ≥8
hypotheses below."
```

---

## Part C — Alternatives (§3.3 — ≥2 + status quo, each with kill-condition)

### Alternative A: Accept the corpus as-is and proceed to Phase-2 cells
- **Alternative:** Treat the 6 extractions as sufficient epistemic
  basis; dispatch Phase-2 cells now.
- **Kill condition:** Fails when Phase-2 integrator produces a
  synthesis that cannot be verified as non-arbitrary, because no claim
  in the corpus names what would falsify it. The synthesis becomes a
  dressed-up list of preferences (Hume's is/ought wall).

### Alternative B: Require each extraction to add falsifiers + anti-scopes
  before Phase-2 dispatch
- **Alternative:** Brigadier requests a patch pass from each Phase-1
  sub-agent adding CC-1 / CC-4 / CC-5 / CC-7 fields to load-bearing
  claims before matrix cells are fired.
- **Kill condition:** Fails when the patch pass is itself speculative
  (adding falsifiers post-hoc often produces vacuous ones — "refuted
  if no improvement observed" is not a real falsifier). Risk: the cure
  is cosmetic.

### Status quo (proceed with current corpus)
- **Description:** Use the corpus without remediation; note epistemic
  weaknesses in the integrator output as dissents.
- **Kill condition:** Fails when dissent-preservation (E-5) is not
  exercised and the integrator averages the weaknesses away. This is
  the highest-probability failure path per AP-PHIL-10 paradigm-conflation.

---

## Part D — Anti-scope (§3.4)

This critic is NOT doing the following:
- Arbitrating which improvement to implement first — that is
  investor-expert × integrator (instrumental Рациональность,
  FPF L1003-1006).
- Running engineering-craft review on the Python/Bash implementation
  sketches in δ and ζ — that is engineering-expert × critic.
- Producing a corrected corpus — the next cycle's optimizer or
  integrator pass holds that responsibility.
- Evaluating the operational feasibility of skill candidates — that
  is mgmt-expert × critic.
- Auditing the wiki-v3 architecture completeness — that is
  systems-expert × critic.

---

## Part E — BA-Cycle-lite (§3.5)

- **BA-0 Ethical surface present?** No. The artefacts are meta-system
  improvement proposals with no direct capital allocation, no public
  claims, no life-affecting decisions in scope.
- Ethical-surface flag: **no**. BA-Cycle stops at BA-0.

---

## Part F — 8+ Philosophy-domain Hypotheses with full rating sets

Each hypothesis: Claim, Epistemic Status (F, ClaimScope, R),
Conformance check result, Alternatives, Anti-scope, AP codes triggered.

---

### H-1. The "2× improvement" meta-claim has no Popperian falsifier

**Claim (as stated in task brief and echoed across α..ζ):** "We can
produce 2× improvement in swarm quality by the changes listed."

**What "2× improvement" operationally means is never specified.** Is it
2× reduction in AP firings? 2× increase in strategies.md entry
acceptance rate? 2× improvement in Ruslan's qualitative rating? Each
interpretation has different falsification conditions. All are present
as candidates but none is selected.

**Epistemic Status:**
```yaml
F: F1  # assertion; no measurement baseline exists; no golden set
ClaimScope:
  holds_when: "a measurement substrate exists (golden sets, eval harness,
               health.md counters active) AND a baseline cycle has been
               recorded AND ≥1 subsequent cycle has been run"
  not_valid_when: "measurement substrate absent (current state: all
                  health.md counters frozen at 0, no golden sets authored,
                  strategies.md entries = 0 per ROY-AGENTS-BUILT:160-170)"
R:
  refuted_if: "after ≥3 cycles with the proposed changes, no measured
               metric improves by ≥2× relative to the baseline cycle"
  receipt: "swarm/wiki/meta/health.md fpar_log + closed_cycles_count"
  accepted_if: "≥1 measured metric doubles relative to the baseline
                cycle over ≥3 cycles"
```

**Conformance:**
- CC-1 Falsifier-named: **FAIL.** The claim appears in the task brief
  without any falsifier or measurement method.
- CC-4 Method declares NOT: **FAIL.** No anti-scope on the "2×" claim.
- CC-5 Dichotomy-of-control: **FAIL.** Whether a metric doubles is a
  future observation — not-in-our-control. In-our-control is only: which
  changes to implement. The claim conflates the two.

**Alternatives:**
- Alt-A: Replace "2× improvement" with "measurable improvement on ≥1
  defined metric within ≥3 cycles." Kill condition: if no metric is
  defined by Phase-2 integrator, this alternative also fails.
- Alt-B: Leave the "2×" as a goal (aspirational), not a criterion.
  Kill condition: aspirational claims provide no falsifiability and
  breed confirmation bias — every positive outcome will be read as
  "confirming" 2×.
- Status quo: keep "2× improvement" as the acceptance predicate.
  Kill condition: the predicate is Popperian-unfalsifiable as written
  (see above). If used as a gate criterion, any HITL ack becomes
  arbitrary.

**AP codes:** AP-PHIL-1 (claim-without-falsifiability), AP-PHIL-5
(method declared without measurement baseline).

---

### H-2. The Boris Cherny "2–3× quality gain" canonical quote is
decorative, not operational

**Claim (α TL;DR line 28):** "Boris Cherny 'Claude performs
dramatically better when it can verify its own work' → 2-3× quality
gain." This quote is load-bearing: it anchors the verifier design
(4-layer termination stack, acceptance predicates) and the 5×4 matrix
self-verification argument.

**Epistemic problem:** The "2–3× quality gain" figure is not defined.
- What is the dependent variable? Pass rate? Correctness? User rating?
- Over what task distribution? All Claude tasks? Code tasks? Agentic
  tasks?
- Is it reproducible in the Jetix swarm context (hub-and-spoke
  architecture, Max-subscription, no vector DB)?

The quote is used as authority (appeal to practitioner) without
specifying the applicable conditions (Munger CC-3 violation) or a
falsifier (Popper CC-1 violation). It becomes an epistemic ornament.

**Epistemic Status:**
```yaml
F: F3  # practitioner-attested, single-source, non-peer-reviewed context
ClaimScope:
  holds_when: "Claude is used in a task where self-verification is
               operationally possible (i.e., the acceptance predicate
               is Hamel-binary and a verifier exists)"
  not_valid_when: "verification is nominal (acceptance predicate is
                  prose; no verifier code runs); the Jetix swarm in
                  Phase A has no automated verifier; most acceptance
                  predicates in the context corpus are prose"
R:
  refuted_if: "measured quality of outputs from cells with verifiers
               is not ≥1.5× quality of outputs from cells without
               verifiers, across ≥20 matched tasks"
  receipt: "golden-set pass-rate per cell (currently absent)"
  accepted_if: "≥1.5× ratio holds across ≥20 matched tasks with and
                without verifier activation"
```

**Conformance:**
- CC-1: **FAIL.** Quote used without falsifier.
- CC-3: **FAIL.** No `conditions:` block on the Cherny invocation.
- CC-7: **FAIL.** Meta-claim about "Claude performs better" has no
  concrete_instance from the Jetix context.

**Alternatives:**
- Alt-A: Qualify the Cherny citation as "plausible heuristic (F3)
  with applicable conditions limited to tasks where acceptance
  predicates are Hamel-binary." Kill condition: if most current Jetix
  APs are prose, the heuristic is not applicable; the quote should be
  removed from the architecture rationale until APs are hardened.
- Alt-B: Treat the Cherny number as aspirational only; remove it from
  acceptance predicates. Kill condition: removes a useful heuristic
  from the design space.
- Status quo: use the quote as a load-bearing architectural argument.
  Kill condition: authority-based argument with no falsifier is
  AP-PHIL-1. Any gate based on this quote is epistemically arbitrary.

**AP codes:** AP-PHIL-1, AP-PHIL-8 (mental-model-applied-out-of-context).

---

### H-3. The "measurement void" (MP-3) is unfalsified itself

**Claim (ζ MP-3):** "A measurement void exists across α + γ + δ + ε:
golden sets unauthored, health.md counters frozen, Tier-3 recall never
measured, skill pass-rate unmeasurable."

**The MP-3 claim is accurate as an inventory observation.** But the
hypothesis surfaced by ζ — "one `swarm/evals/` file-JSONL tree + bash
runner unblocks all four" — is itself an unfalsified claim.

What would it mean for the "measurement void" to have been genuinely
filled vs cosmetically addressed?
- Having evals/ populated with data that was generated by real task
  runs (not hand-crafted examples for the sake of having examples).
- Having a baseline cycle recorded against which future cycles differ.
- Having a definition of "pass" vs "fail" that is not circular
  (i.e., not defined by the same agent that produces the output).

The deeper epistemic concern: **without golden sets sourced from an
independent human reviewer (Hamel-Husain methodology per ε:256),
any eval harness is an auto-grader that grades its own homework.** The
measurement void cannot be filled by specification alone — it requires
independent ground truth.

**Epistemic Status:**
```yaml
F: F2  # observed gap; hypothesis about fix is F1 (unverified)
ClaimScope:
  holds_when: "golden sets authored by an independent reviewer
               (human or unrelated model) with Hamel-binary pass/fail
               criteria NOT derived from the same agent's own rubric"
  not_valid_when: "the agent that produced the artefact also grades
                  whether the artefact passed; this is circular by
                  Popper's criterion"
R:
  refuted_if: "swarm/evals/ is populated and cited as measurement
               basis for 2× claims AND those evals were authored by
               the same cells whose outputs they grade"
  receipt: "evals/<skill>/results.jsonl + authorship metadata"
  accepted_if: "evals authored by a separate cell or Ruslan; reviewer
                identity logged in golden-set.jsonl"
```

**Conformance:**
- CC-1: **FAIL.** The proposed fix ("one bash runner") has no falsifier.
- CC-5: **FAIL.** Whether independent review is obtained is not in the
  swarm's control — Ruslan must supply it or a HITL gate must enforce it.

**Alternatives:**
- Alt-A: Declare Phase-A evaluation as "swarm-internal best effort"
  and record that the measurement is self-reported (F2 flag), making
  the limitation explicit. Kill condition: fails if the limitation is
  silently forgotten in Phase-B and F2 claims are promoted to F6
  without external review.
- Alt-B: Require Ruslan to supply 3+ golden-set judgements per cell
  before any Phase-B promotion. Kill condition: if Ruslan ack budget
  is overloaded, the gate is never exercised.
- Status quo: treat the spec of an eval harness as equivalent to
  having measurements. Kill condition: the spec is a contract, not a
  running machine (γ's exact language for the wiki) — applies here too.

**AP codes:** AP-PHIL-1, AP-PHIL-3 (instrumental vs epistemic
collision — the "fix" is an action recommendation, not an epistemic
claim; investor-expert should own the sequencing).

---

### H-4. The Rule-of-4 "knee violation" is an argued analogy, not a
measured fact

**Claim (α:54, α:107):** "Jetix's 5-expert roster sits exactly on the
Rule of 4 knee (one over), with mitigations argued but not measured."

The Rule of 4 is sourced from human cognitive capacity literature
(Miller 7±2 adapted to 4 for attention-budget heuristics). Its
application to LLM swarm architecture involves two analogical leaps:

1. Human cognitive span → LLM-orchestrator attention span.
2. A heuristic for human teams → a heuristic for a brigadier dispatching
   a matrix.

Neither leap is stated as such. The analogy is presented as a
structural fact ("sits exactly on the knee") rather than as a
heuristic with applicable conditions (Munger model-out-of-context,
CC-3).

**Furthermore:** The mitigation offered (context-loader pagination per
ζ U-5) assumes that "Rule-of-4 violation" is about in-context token
budget rather than about orchestration complexity. These are different
claims. The first is a resource constraint (measurable); the second is
a cognitive/coordination complexity claim (harder to falsify).

**Epistemic Status:**
```yaml
F: F3  # heuristic with analogical transfer; not derived from first
       # principles for LLM orchestrators
ClaimScope:
  holds_when: "the orchestrator's failure mode from managing 5 vs 4
               experts is observable (e.g., dispatch errors,
               wrong-cell routing, dropped context)"
  not_valid_when: "the brigadier's actual error rate on routing
                  is not measured (current state); the analogy from
                  human teams is unevaluated in LLM context"
R:
  refuted_if: "brigadier routes correctly 5 experts across ≥30 cycles
               with error-rate ≤ the same brigadier routing 4 experts
               across ≥30 cycles in a controlled comparison"
  receipt: "swarm/logs/<cycle-id>/cycle-log.md routing errors"
  accepted_if: "routing error rate ≥1.5× higher at 5 vs 4 experts
                over ≥30 matched cycles"
```

**Conformance:**
- CC-1: **FAIL.** "Sits exactly on the knee" is stated as fact without
  falsifier.
- CC-3: **FAIL.** Rule-of-4 invoked without `model: Rule-of-4` +
  `conditions: human cognitive span; may not transfer to LLM` fields.
- CC-7: **FAIL.** Meta-claim about "knee" has no concrete instance
  (which routing event, which cycle, which observable).

**Alternatives:**
- Alt-A: Re-label Rule-of-4 as "heuristic (F3), applicable conditions
  under investigation; Phase-A smoke will surface routing-error rate."
  Kill condition: if routing errors are never logged, the heuristic
  remains unresolved indefinitely.
- Alt-B: Run the 5-vs-4 controlled test per α Q3. Kill condition:
  requires Phase-B investment; not available Phase-A.
- Status quo: accept the analogy as design guidance without measurement.
  Kill condition: if a routing error occurs that traces to the 5th expert,
  the heuristic will have been unfalsifiable until that moment — AP-PHIL-1.

**AP codes:** AP-PHIL-1, AP-PHIL-8.

---

### H-5. The provenance gate (§5.5.5) prevents contradicting accepted
foundations only nominally

**Claim (shared-protocols §2, γ provenance gate observations):** The
provenance gate "ensures no write contradicts an accepted foundation
without an explicit `contradicts` edge."

**Epistemic analysis:**

The gate requires:
- Condition 6: "Non-contradicting. On `state→accepted`, no existing
  accepted page contradicts without explicit contradicts edge."
  [shared-protocols.md:79-80]

The epistemic weakness: **the gate prevents contradiction only if**
(a) the foundation being contradicted has itself been promoted through
the gate, AND (b) the brigadier actually runs the 9-step ritual
[γ:209-211]. As γ observes, the gate is "a design, not a runtime."
There are currently zero accepted claims (edges.jsonl empty), so
condition 6 is vacuously satisfied — nothing contradicts because
there is nothing to contradict.

More critically: the gate does not evaluate LOGICAL contradiction
between claims — it only checks whether an explicit `contradicts` edge
exists. A contradiction without a declared edge passes the gate
silently. The gate detects labelled contradictions, not contradictions.
This is a significant epistemic gap.

**The Luhmann contradiction-partner model (δ:54) would address this**
— but requires an engine that evaluates semantic content, not just
graph topology.

**Epistemic Status:**
```yaml
F: F4  # gate specification is formal; enforcement is manual; actual
       # semantic contradiction detection is absent
ClaimScope:
  holds_when: "the wiki contains ≥1 accepted page AND the brigadier
               runs the ritual manually on every proposed write AND
               claims are semantically tagged for contradiction"
  not_valid_when: "wiki contains zero accepted pages (current state:
                  edges.jsonl empty); OR the brigadier silently skips
                  the ritual"
R:
  refuted_if: "a write is accepted that directly contradicts an
               accepted foundation AND no contradicts edge exists
               in edges.jsonl for that pair"
  receipt: "edges.jsonl + accepted pages list"
  accepted_if: "every semantic contradiction between accepted pages
                has a corresponding contradicts edge for ≥100 pages"
```

**Conformance:**
- CC-1: **PASS.** This analysis names the falsifier.
- CC-4: **FAIL.** The gate specification does not declare what it
  is NOT trying to do (it does not detect unlabelled logical
  contradictions; it does not evaluate semantic coherence).
- CC-5: **PARTIAL.** Brigadier discipline to run the ritual is
  in-control; whether the wiki grows without contradiction is not.

**Alternatives:**
- Alt-A: Add a Luhmann-style semantic contradiction check to `/lint`
  (δ:54). Kill condition: requires LLM-pass over new writes vs all
  accepted pages — O(n) cost per write; may be prohibitive at scale.
- Alt-B: Accept that the gate prevents only labelled contradictions;
  document this limitation explicitly in shared-protocols §2. Kill
  condition: the documentation gap is the epistemic problem; if this
  limitation is not declared, the gate creates false confidence.
- Status quo: claim the gate prevents contradictions without qualification.
  Kill condition: the first real contradiction that passes the gate
  undetected will expose this. Per AP-PHIL-1, the unqualified claim
  is epistemically indefensible.

**AP codes:** AP-PHIL-1 (claim-without-falsifiability on the gate's
stated guarantee), AP-PHIL-11 (meta-claim about prevention without
object-level instance).

---

### H-6. The α-5 Direction "AI never moves" lock is a rule-as-heuristic
mislabelled as a hard constraint

**Claim (α:56, shared-protocols §4 line 116):** "α-5 Direction state
changes (AI agents never move α-5)."

**Is this claim Popperian-falsifiable? Under what conditions does it
fail to be the right policy?**

The claim has the grammatical form of an absolute prohibition (a LOCK
per FPF nomenclature). But the epistemological question is: what
makes this a rule rather than a heuristic?

Koen's heuristic-as-method principle (P6 of this expert's §2.4): every
declared method MUST name its known failure modes and the conditions
under which the state-of-the-art-method fails. Applied here:

- **Failure mode 1:** If the swarm operates without HITL for an
  extended period (Ruslan unavailable), no Direction can be proposed,
  modified, or archived. The swarm stagnates. This is an operational
  failure the lock creates.
- **Failure mode 2:** If an AI agent surfaces compelling evidence
  that a current Direction is factually wrong (e.g., the market
  research shows the ICP-5 framing is incorrect), the lock prevents
  the agent from even proposing a revision — it can only "surface"
  the evidence. Whether the evidence is acted on depends entirely on
  HITL ack frequency.
- **Failure mode 3 (epistemic):** α-5 directions are currently Phase-A
  "lightweight (state enum only)" with zero instances [α:56]. The lock
  is applied to an empty set. It is untested by definition.

The claim that "AI agents never move α-5" is defensible as a
**value judgment** (humans should retain strategic direction authority)
but is being stated as an architectural invariant. Its justification
should be epistemic (what evidence supports it) + normative (what
value it protects) + Stoic (what failure mode it prevents). Currently
only the normative dimension is supplied.

**Epistemic Status:**
```yaml
F: F5  # formal protocol lock; grounded in governance value judgment
ClaimScope:
  holds_when: "Ruslan is available for HITL acks within a reasonable
               latency (days, not months); ≥1 Direction is instantiated
               so the lock has a concrete referent"
  not_valid_when: "zero Directions instantiated (current state — the
                  lock governs an empty namespace); OR Ruslan HITL
                  latency exceeds task-criticality window"
R:
  refuted_if: "a scenario arises where the swarm has strong falsifiable
               evidence that a Direction is wrong AND Ruslan ack latency
               exceeds the task deadline AND the swarm cannot surface
               the contradiction without violating the lock's semantics"
  receipt: "swarm/gates/AWAITING-APPROVAL-*.md escalation log"
  accepted_if: "all Direction changes over ≥20 cycles are HITL-acked
                with no cases where ack latency caused task failure"
```

**Conformance:**
- CC-1: **PASS.** Falsifier now named.
- CC-4: **FAIL.** The original claim does not name what the lock is
  NOT trying to do (it is not trying to prevent good-faith evidence
  surfacing; it IS trying to prevent autonomous AI strategic pivoting).
- CC-6: **PARTIAL.** The normative argument is implicit; the
  governance rationale should be named.

**Alternatives:**
- Alt-A: Upgrade the lock declaration to explicitly state its failure
  modes and applicable conditions (Koen sotam discipline). Kill
  condition: none — this is epistemic hygiene without downside.
- Alt-B: Create a conditional exception: if HITL latency > N days AND
  evidence against a Direction is rated F7+, the swarm may propose
  (not execute) a Direction revision. Kill condition: the exception may
  erode the lock's normative force if N is set too low.
- Status quo: maintain the lock as an unqualified absolute prohibition.
  Kill condition: the lock will face its first real test only when a
  Direction is instantiated AND evidence against it emerges. Until then,
  the lock is epistemically empty (governs zero instances).

**AP codes:** AP-PHIL-5 (method declared without failure-mode
enumeration), AP-PHIL-2 (the governance paradigm is not named — is this
a "principal-agent" paradigm? a "human-in-the-loop AI safety" paradigm?
each has different implications for where the lock should be set).

---

### H-7. The Yan quote + Anthropic "+90.2%" reconciliation is a
paradigm-conflation, not a synthesis

**Claim (α:75, ζ cross-domain pair α×δ):** "Yan ↔ Anthropic +90.2%
tension: parallel review safe; parallel codegen hands off summaries =
Flappy Bird trap. Reconciliation: AP-1 detector over mailbox JSONL."

**The reconciliation is a paradigm-conflation disguised as a synthesis.**
- Yan's principle ("share FULL traces, not summaries") is an
  **epistemological claim**: what information must be transmitted for
  a downstream agent to form correct beliefs.
- Anthropic's "+90.2%" result is a **performance measurement claim**:
  parallel agents complete tasks faster when allowed to operate
  independently.
- These operate in DIFFERENT Vincenti knowledge categories (P7 of
  this expert's §2.4): Yan = practical considerations; Anthropic =
  quantitative data.

The claimed reconciliation ("parallel review is safe; parallel codegen
is unsafe") does not derive from either claim — it is a new claim
introduced to resolve the tension without showing how it follows from
the first two. This is paradigm-conflation (AP-PHIL-10): two claims
from different paradigms are melted into one synthesis without a
proper dissent block.

**The mechanistic reconciliation (AP-1 detector over mailbox JSONL) is
also not derived from either claim** — it is an implementation proposal
that would DETECT the violation after the fact, not prevent it. A
Popperian reading: the AP-1 detector is falsifiable in the right way
(it fires or doesn't), but it is not a falsifier for the original
reconciliation claim.

**Epistemic Status:**
```yaml
F: F3  # the reconciliation is an informal synthesis; not peer-reviewed;
       # not derived from first principles
ClaimScope:
  holds_when: "the task being parallelised is a REVIEW task (each cell
               produces independent epistemic judgment); not a CODEGEN
               task (where shared context is required for correctness)"
  not_valid_when: "the task type is ambiguous (current state: the
                  5×4 matrix does not formally classify task types as
                  review vs codegen; cells are dispatched by topic, not
                  by task-type classification)"
R:
  refuted_if: "a parallel REVIEW task (e.g., two critic cells over the
               same artefact) produces a summary-handoff AND the
               downstream integrator reaches wrong conclusions as a
               result"
  receipt: "swarm/wiki/tasks/<task-id>/artefacts/<cell>-*.md"
  accepted_if: "no summary-handoff detected in ≥20 parallel review
                cell invocations"
```

**Conformance:**
- CC-1: **FAIL.** The reconciliation claim has no falsifier in the corpus.
- CC-2: **FAIL.** Paradigm shift not named (Yan's paradigm = epistemic
  fidelity; Anthropic's paradigm = throughput optimization; these are
  different paradigms; their anomaly is NOT named).
- CC-3: **FAIL.** Both the Yan and Anthropic models are invoked without
  `conditions:` fields.

**Alternatives:**
- Alt-A: Preserve both claims as dissenting (E-5 dissent preservation):
  "Yan recommends full-trace (epistemic-fidelity paradigm); Anthropic
  reports +90.2% (throughput paradigm). The two are not reconciled
  at Phase A; both are retained as constraints." Kill condition:
  dissent preservation forces a HITL decision on which paradigm
  governs the design, which may be uncomfortable but is epistemically
  honest.
- Alt-B: Accept the current reconciliation as a working heuristic (F3)
  with known fragility; apply it only to cells that are clearly
  "review" mode. Kill condition: if no cell is formally classified as
  review vs codegen, the heuristic is impossible to apply consistently.
- Status quo: treat the reconciliation as resolved. Kill condition:
  the next parallel codegen task with summary-handoff will expose the
  failure — and it will have been epistemically undetectable by the
  current framing.

**AP codes:** AP-PHIL-2 (paradigm-conflation), AP-PHIL-10
(paradigm-melting in synthesis), AP-PHIL-8 (Munger mental-model
invoked without applicable conditions).

---

### H-8. FPF E-15 "never override expert's domain judgment" is a
heuristic mislabelled as a rule

**Claim (α:96, FPF-ENHANCEMENT §E.15):** "E-15 locked-verifiable —
Orchestration authority, not domain authority clause in brigadier §1."

**The epistemological question from the brief:** What makes this a rule
vs a heuristic?

Koen's distinction: an algorithm terminates with a definitive answer;
a heuristic is a plausible guide that may fail without warning
[Koen sotam, P6 of this expert's §2.4]. Applied here:

E-15 says: "Brigadier holds orchestration authority, not domain
authority." This implies the brigadier should never override an
expert's domain judgment.

**When does E-15 fail as a rule?**
- When two domain experts produce contradictory domain judgments and
  HITL is not available. Brigadier must pick one — this IS a domain
  judgment. E-15 has no escalation path for this case beyond "escalate
  to HITL." If HITL is slow, the swarm deadlocks.
- When an expert's domain judgment is demonstrably wrong (e.g.,
  investor-expert recommends a capital allocation that violates a
  shared-protocols §2 constraint). Brigadier holding only
  "orchestration authority" has no mechanism to override — yet failing
  to override may break the swarm.
- When the domain boundary itself is disputed (the philosophy-investor
  dual-ownership of Рациональность is the canonical example: FPF
  L1003-1006 says epistemic belongs to philosophy, instrumental to
  investor — but the boundary is fuzzy in practice).

**E-15 is therefore a heuristic** under Koen's definition: it has a
clear applicable domain (single-expert tasks with no cross-domain
conflict), known failure modes (multi-expert disagreement, boundary
disputes), and a state-of-the-art-method (hub-and-spoke orchestration).
It should be labelled F4 (design-decision heuristic) not F8 (formal
invariant).

**Epistemic Status:**
```yaml
F: F4  # design-decision heuristic; not derived from first principles
       # for all cases; known failure modes not documented in E-15
ClaimScope:
  holds_when: "each task touches exactly one domain expert's specialty;
               no cross-domain conflict exists; HITL is available with
               low latency"
  not_valid_when: "two experts produce contradictory domain judgments
                  on the same task; OR the domain boundary is disputed
                  (e.g., philosophy-investor Рациональность wall)"
R:
  refuted_if: "brigadier overrides an expert's domain judgment in
               practice AND the override leads to a better outcome
               than deferral would have — even once"
  receipt: "swarm/logs/<cycle-id>/cycle-log.md + decisions/ notes"
  accepted_if: "no case across ≥30 cycles where brigadier override
                would have prevented a confirmed swarm error"
```

**Conformance:**
- CC-1: **PASS.** Falsifier now named.
- CC-4: **FAIL.** E-15's original formulation does not name what it
  is NOT trying to do (it is NOT trying to prevent brigadier from
  routing; it IS trying to prevent epistemic encroachment — these
  should be explicit).
- CC-6: **FAIL.** The implicit fallacy in treating E-15 as a rule is
  "appeal to authority of the domain expert" — this fallacy is not
  named in the current swarm documentation.

**Alternatives:**
- Alt-A: Upgrade E-15 to a heuristic with documented failure modes and
  explicit escalation paths for boundary disputes. Kill condition: none
  — this is epistemic hygiene.
- Alt-B: Maintain E-15 as a hard rule with explicit carve-outs
  (enumerated cases where brigadier may override). Kill condition:
  carve-out enumeration is incomplete by definition; an un-enumerated
  case will always arise.
- Status quo: treat E-15 as a rule (F8 level). Kill condition: the
  first cross-domain conflict that reaches brigadier with no HITL
  available will expose whether E-15 is sufficient.

**AP codes:** AP-PHIL-5 (method declared without failure-mode
enumeration), AP-PHIL-6 (no BA-Cycle-lite on the governance claim,
though not directly an ethical surface, the "AI never overrides human
expert" governance pattern has a normative dimension that should be
named rather than implied).

---

## Part G — Specific Failures (AP codes fired)

From the analysis above, the following AP codes fire across the corpus:

| AP code | Where | Triggered by |
|---|---|---|
| AP-PHIL-1 | H-1, H-2, H-3, H-4, H-5, H-7 | Non-falsifiable claims throughout α..ζ extractions |
| AP-PHIL-2 | H-7 | Yan + Anthropic paradigm-conflation without anomaly declaration |
| AP-PHIL-5 | H-1, H-6, H-8 | Methods declared without failure-mode enumeration |
| AP-PHIL-8 | H-2, H-4, H-7 | Mental models (Cherny, Rule-of-4, Yan) invoked without conditions |
| AP-PHIL-10 | H-7 | Two-paradigm synthesis without dissent preservation |
| AP-PHIL-11 | H-5 | Meta-claim about gate "preventing contradictions" with no object-level instance |

Global AP codes surfaced (for brigadier §8.5 cross-reference):

| AP code (global) | Where |
|---|---|
| AP-6 (average-dissent) | H-7 — Yan/Anthropic reconciliation averages two dissents |
| AP-25 (missing-acceptance-predicate) | H-1 — "2× improvement" predicate is prose, not Hamel-binary |
| AP-1 (summary-compression) | ζ U-1..U-6 — emergent patterns presented as summaries without full-trace grounding |

---

## Part H — Recommended Changes

1. **Require the "2× improvement" claim to carry a Hamel-binary
   acceptance predicate before Phase-3 gate.** The predicate must
   specify: which metric, what baseline value, what target value,
   what measurement artefact [path]. "2× improvement" as currently
   written is AP-25.

2. **Qualify the Cherny "2–3× quality gain" citation as F3/heuristic
   with explicit applicable conditions in every artefact that cites it.**
   Specifically: cite only when the artefact under review has a
   Hamel-binary AP; remove from architecture rationale arguments until
   the Phase-A golden sets are authored.

3. **Add an `anti_scope:` block to each Phase-2 cell dispatch brief.**
   Without anti-scope declarations, the synthesis step (integrator) has
   no via-negativa boundary and will produce unbounded positive proposals
   — which is the pattern γ, ε, and ζ already demonstrate.

4. **Preserve the Yan / Anthropic tension as a dissent (E-5) rather
   than a reconciliation.** The two claims operate in different Vincenti
   knowledge categories and different paradigms. A forced reconciliation
   is AP-PHIL-10. The dissent block should carry both (F3) claims with
   their applicable conditions and route to HITL for paradigm selection.

5. **Upgrade α-5 Direction lock documentation.** Add: known failure
   modes + applicable conditions + Koen sotam declaration. The lock is
   sound normatively but epistemically thin without these fields.

6. **Upgrade E-15 to a heuristic with documented failure modes.** Add
   to brigadier §1d or shared-protocols §4: "E-15 is a heuristic (F4);
   known failure modes include multi-expert disagreement on the same
   task and boundary disputes (see FPF L1003-1006)."

7. **Add a measurement-substrate precondition to all Phase-2 "2×"
   proposals.** Any improvement surface claiming "2×" must declare in
   its frontmatter: `measurement_substrate: [path to health.md counter
   or eval results.jsonl]` AND `baseline_value: <current measured value>`.
   If `baseline_value` is null, the "2×" claim must be labelled F1
   (assertion) not F3+.

8. **Populate at least one `contradicts` edge before the Phase-3 gate**
   to verify that the provenance-gate contradiction-detection path is
   operational. Use β's €50K horizon-gate discrepancy (β:213-227) as
   the seed case — this is a concrete, verifiable contradiction between
   investor-expert and the other four experts.

---

## Part I — Acceptance Test (§3.2 copy)

```
acceptance_test: "Every load-bearing improvement hypothesis in the
Phase-2 context corpus carries (a) a named falsifier specifying what
observation would refute it, (b) an explicit anti_scope block naming
≥2 things it is NOT trying to do, (c) a dichotomy-of-control tag
distinguishing variables in-our-control from those not-in-our-control,
AND (d) a concrete_instance: field grounding every meta-pattern claim
in at least one named artefact path + line-range — all holding across
≥8 hypotheses in the Phase-2 artefacts."
```

---

## Part J — Escalations

```yaml
escalations:
  - trigger: peer-input-needed
    description: "H-7 Yan/Anthropic paradigm dissent preservation requires
                  integrator-mode invocation to produce the proper dissent block.
                  Philosophy-expert has surfaced the epistemic conflict; resolution
                  via dissent preservation (E-5) requires an integrator pass."
    route: brigadier → philosophy × integrator (or systems × integrator for the
           architectural implications)
  - trigger: peer-input-needed
    description: "H-8 E-15 failure-mode documentation touches brigadier's own
                  authority definition. Philosophy-expert can audit; the fix
                  requires brigadier self-edit (within its autonomous writes).
                  Brigadier should note the H-8 finding in its own §8.5."
    route: brigadier (self-action)
  - trigger: peer-input-needed
    description: "H-1 measurement-substrate requirement for '2×' claims — defining
                  the specific metrics and measurement paths is investor-expert's
                  territory (instrumental Рациональность). Philosophy-expert has
                  named the epistemic gap; investor-expert should specify the
                  measurable deltas."
    route: brigadier → investor-expert × critic or integrator
```

---

## Part K — Dissents preserved

```yaml
dissents:
  - position: "The context corpus extractions (α..ζ) are sufficient
               epistemic basis for Phase-2 cell dispatch. The falsifiability
               gaps noted are inherent in early-cycle exploratory work;
               requiring strict Popperian falsifiers on all claims is
               over-stringent for Phase-A."
    held_by: "engineering-expert (inferred — operationalisation over
             epistemology is engineering's characteristic stance)"
    F: F3
    ClaimScope: "holds if Phase-A is framed as 'hypothesis generation'
                 not 'hypothesis testing'; fails if Phase-A outputs are
                 treated as verified grounds for Phase-B commitments"
    R:
      refuted_if: "Phase-B commitments are made on claims that are later
                   shown to be false or unfalsifiable"
      accepted_if: "Phase-A outputs are explicitly labelled F1-F3 and
                   not cited as F6+ evidence"
  - reconciliation:
      method: "epistemic-coherence per philosophy × integrator mandate"
      verdict: "Both positions retained. The engineering position is valid
               for exploratory frames; the philosophy position is valid for
               gate criteria. Resolution: label all Phase-A claims with
               their F-level; use only F4+ claims as Phase-B gate criteria.
               Preserve both positions in Phase-3 AWAITING-APPROVAL packet."
```

---

## Provenance

All claims in this audit trace to:

- `context/alpha-agent-construction-corpus.md` — α:28-31 (Cherny quote),
  α:48-59 (thin spots), α:75 (Yan/Anthropic), α:107-109 (Rule-of-4)
- `context/beta-current-agents.md` — β:213-227 (€50K gate), β:266-285
  (mode-prefix drift), β:385-390 (§7 SPEC numbering)
- `context/gamma-wiki-v3.md` — γ:46-49 (contract not runtime), γ:175
  (contradicts edges empty), γ:181-211 (provenance gate)
- `context/delta-memory-sota.md` — δ:54 (Luhmann contradiction partner)
- `context/epsilon-skills.md` — ε:244-256 (golden set/eval gap)
- `context/zeta-cross-pollination.md` — ζ:93-118 (MP-1..MP-4)
- `swarm/lib/shared-protocols.md` — lines 61-83 (§2 provenance gate
  conditions), line 116 (α-5 HITL trigger)
- `.claude/agents/philosophy-expert.md` — §2.4 (P1..P10 domain patterns),
  §3.1 (conformance checklist), §3.5 (BA-Cycle-lite)
- `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` — E-5
  (dissent preservation), E-15 (domain authority), E-4 (invariant checks)

---

*Philosophy-expert. Mode: critic. Cycle: cyc-swarm-self-improve-v1-2026-04-23.*
*turns_used: within ap_budget of 80.*
*verifier_result: conformance 0 full-pass / 2 partial / 5 fail on corpus; 8
hypotheses produced with full (F, ClaimScope, R) triples and AP codes.*
