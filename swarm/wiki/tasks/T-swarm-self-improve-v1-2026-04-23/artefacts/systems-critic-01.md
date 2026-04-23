---
type: systems-critic
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
mode: critic
agent: systems-expert
created: 2026-04-23
pipeline: drafted
state: drafted
confidence: medium
confidence_method: pattern-match
sources:
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/beta-current-agents.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/delta-memory-sota.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md
  - swarm/wiki/foundations/swarm-alphas.md
acceptance_predicate: >
  count(distinct_systems_hypotheses) >= 8
  AND each_hypothesis has polarity AND leverage_point_rung AND evidence_kpi
  AND count(feedback_loops_named with polarity) >= 2
  AND system_boundary named with >=3 out_of_system_items
  AND requisite_variety_budget present in frontmatter
  AND count(alternatives) >= 2 with kill_conditions
requisite_variety_budget:
  captured: >
    5-domain-expert dispatch matrix (5×4 cells), brigadier orchestration loop,
    wiki artefact lifecycle (alpha-2 state machine), strategies-rule lifecycle
    (alpha-3), cycle lifecycle (alpha-4). Feedback loops captured: architect-
    produces-docs loop, brigadier-dispatches-integrates loop. Leverage points
    captured: 4 Meadows rungs (L4 information-delay, L6 information-structure,
    L8 rules, L9 goals). Phase-A canonical sources: alpha, beta, gamma, delta,
    epsilon, zeta extractions.
  actual_estimate: >
    Full task variety of an AI consulting operation: client-facing delivery
    loops (absent), capital-allocation feedback (absent), human-calendar
    interrupt dynamics (absent), inter-agent emergent deadlock patterns (not
    yet observed), cross-cycle compounding loops (cycle count = 0), external
    regulatory/market loops (absent Phase A), HITL latency variance (absent).
    Captured variety is roughly 15-20% of actual system variety; the captured
    20% covers the architectural skeleton but misses all runtime dynamics
    because zero cycles have closed.
niche: meta
---

# Systems Critic — Swarm Phase-A Self-Model
## Artefact: The Phase-A Jetix Swarm as a System

---

## Conformance Checklist (5 binary checks)

**Check 1 — Every leverage-point claim carries observable evidence.**

FAIL. The six input extractions name numerous leverage points — mode-prefix
hook (AP-5), provenance-gate automation, F/ClaimScope/R frontmatter — but
NONE carries an observable KPI. Alpha says "2× improvement surfaces" but
defines no baseline measurable. Epsilon says "2× = `/compound` produces ≥1
candidate skill per week" — this is the ONLY KPI-backed claim across all
six inputs. The swarm system model cannot be said to identify leverage points
correctly when five of the six extractions produce leverage proposals without
an observable attached. [alpha:61-75; beta:432-490; gamma:218-291; delta:59-162; epsilon:264-286]

**Check 2 — Every feedback loop has both polarity (+/-) declared.**

FAIL. Zero input extractions declare a named feedback loop with explicit
polarity. Zeta names "executor-not-wired" (MP-1), "drift-across-siblings"
(MP-2), "measurement-void" (MP-3), "contract-without-consumer" (MP-4) — but
these are META-PATTERNS, not feedback loops with named polarity. The
reinforcing loop (brigadier dispatches → artefact produced → strategies.md
grows → brigadier dispatches better) is never stated as a + loop. The
balancing loop (HITL gate → delay → approval → resumption) is never stated
as a − loop. The swarm is over-documented at the architectural level and
has no declared dynamic model. [zeta:93-117; alpha:27-59; gamma:46-49]

**Check 3 — Every emergent claim has ≥1 counter-sample considered.**

FAIL. Zeta identifies MP-1 ("executor-not-wired" is emergent across all 5
extractions) as itself an emergent meta-pattern [zeta:93-100]. No counter-
sample is named. The claim is: if specification depth exceeds execution, all
five extraction domains will surface "contract without executor" independently.
Counter-sample needed: name one swarm system of comparable FPF-complexity where
deep specification DID NOT produce the executor-gap emergence. Not named.

Zeta also claims U-1 (PPR over mailboxes = AP-1 detector) as an unexpected
emergent connection [zeta:121-125]. Counter-sample: a swarm where file-ref
discipline is enforced structurally (not via PPR anomaly detection) and still
produces AP-1. Not named.

**Check 4 — Every system boundary has explicit out-of-system items named.**

FAIL. None of the six extractions explicitly declares what is OUTSIDE the
swarm system boundary. The inputs treat the system as: "brigadier + 5 experts
+ wiki v3 + skills". But the following are never named as explicitly excluded:
(1) Ruslan's cognitive bandwidth and attention (treated as infinite in all
six extractions), (2) the v2 `wiki/` legacy tree (coexistence not modelled
as a dynamic), (3) Notion (mentioned as a UI tool but not excluded from the
system boundary), (4) external AI providers (Anthropic API latency variance),
(5) the git remote (brigadier "publishes" but the remote is never drawn into
or excluded from the system). ≥5 items are out-of-system but none are named.

**Check 5 — Every model declares its requisite-variety budget.**

FAIL in the inputs (none of α/β/γ/δ/ε/ζ carry a variety budget); PASS for
this critic artefact (see frontmatter `requisite_variety_budget` above). The
inputs themselves present a variety-management failure: the system is being
specified at high variety (4730-line spec, 18 FPF E-items, 12-type edge enum,
5 swarm alphas) but the controller (brigadier + Ruslan) has not declared what
variety they can actually exercise. Ashby predicts: a controller whose variety
is less than the system's will fail to regulate — specifically, it will
regulate the dimensions it tracks and let the others drift. The drift patterns
in β (7 inconsistencies), γ (9 D-deliverables contracted, 0 executed), ε
(7 of 8 α-3 steps not wired) are all predicted by Ashby variety mismatch.
[beta:228-306; gamma:46-49; epsilon:238-249]

---

## Acceptance Predicate

`count(distinct_systems_hypotheses with polarity AND leverage_rung AND KPI) >= 8
AND system_boundary has >=3 explicit out_of_system_items
AND requisite_variety_budget(captured, actual_estimate) present
AND count(named_feedback_loops with polarity in {+,-}) >= 2
AND count(alternatives with kill_condition) >= 2`

---

## Specific failures found

1. **AP-SYS-1 (feedback-loop-unvalidated)** — The reinforcing loop "spec
   grows → complexity → drift → more spec" is the dominant loop in the
   current swarm. It is named nowhere in any of the six inputs as a loop,
   let alone with KPI evidence. [zeta:93-100; alpha:46-59; gamma:46-49]

2. **AP-SYS-3 (scale-projection-without-gate-risk-table)** — No input
   attempts a BOSC-A-T-X decomposition for the swarm itself. The swarm
   is the system being modelled; its scale triggers are uncharted. This
   is the systems-expert's scalability mode scope; but the absence is a
   critic finding because the design claims production-readiness.

3. **AP-SYS-2 (emergence-claim-without-base-rate)** — MP-1 ("executor-
   not-wired") is treated as an explanatory emergent pattern. No counter-
   sample (a comparably-specified swarm that IS wired) is given. Without
   a counter-sample, MP-1 is a description, not a systems explanation.

4. **AP-SYS-8 (emergence-claim-without-substrate)** — Zeta's U-5 ("Rule-
   of-4 knee violation becomes a loader problem") asserts an emergent
   reframing but names no substrate. What is the substrate from which the
   Rule-of-4 cognitive-load constraint emerges? Not named. [zeta:144-148]

5. **AP-SYS-5 (dual-own-collision-with-philosophy)** — Beta's claim that
   "6-phrasing drift of default-mode fallback" is a problem carries an
   implicit epistemic assertion: "the correct phrasing exists and is
   determinable by inspection." This is an epistemic consistency claim that
   touches philosophy's territory (which phrasing is correct, and by what
   standard?). Flagged; not arbitrated here.

6. **AP-SYS-7 (leverage-point-mistaken-for-symptom)** — All six inputs
   treat the hook layer (UserPromptSubmit/PostToolUse) as the primary
   leverage point. Senge L1: today's problems come from yesterday's
   solutions. The hook layer is itself a solution that was available when
   the system was built and was consciously deferred (Phase B stub).
   If the deferred hook is THE leverage, the question is why it was deferred
   — and whether deferring it again (to "Phase A feasibility: high") is
   the same solution being re-applied. This is a Senge L1 candidate.
   [alpha:48; zeta:57; epsilon:110]

7. **AP-SYS-10 (ashby-variety-mismatch-unflagged)** — The swarm's
   controller is brigadier (a single-expert sequential orchestrator).
   The system variety includes: 20 cells, 5 swarm alphas, 9 entity types,
   12 edge types, 24 locks, 18 FPF E-items, 5 BOSC-A-T-X gates per cell.
   The variety of the controller does NOT match the variety of the system
   it controls. No compensating mechanism (e.g. meta-agent weekly sweep,
   automated lint, closed-cycle mover) is wired. Ashby predicts: brigadier
   will regulate the most salient dimensions (mode dispatch, write gate)
   and let the rest drift. Beta confirms: 7 inconsistencies found in a
   single pass that brigadier had not caught. [beta:228-306; shared-protocols:145-152]

8. **Missing AP row in own §8 (β finding S-4, acknowledged)** — Beta
   explicitly flags: systems-expert §8 has no cells-calling-cells row
   (AP-SYS-11), while all four peer experts have an equivalent row.
   [beta:456-460]. This systems-expert ACKNOWLEDGES the finding. The
   dispute is: is this self-blindness or deliberate domain narrowing?
   Assessment: it is self-blindness. The systems-expert's §8 models
   "this expert's anti-patterns when producing artefacts." The
   anti-pattern of a systems-expert who calls peers directly via Task()
   is a real failure mode that the role contract forbids; it belongs in
   §8 as AP-SYS-11. The absence is a systems-design gap, not a narrowing.
   The prior critique from β was correct; this critic endorses it as a
   defect in the current manifest.

---

## ≥8 Systems-Domain Hypotheses About 2×-Improvable Weaknesses

Each hypothesis names: system substrate, feedback loop (+ or −), Meadows
leverage rung, observable KPI, kill-condition.

---

### H-1. The Spec-Accumulation Reinforcing Loop (L9 — Goals)

**Substrate:** Brigadier + 5 experts + FPF E-1..E-18 design process.

**Feedback loop (+):** Each cycle of design produces more specification
(FPF E-items, locks, AP tables, mode activation stubs) which sets the
goal for the next design cycle ("make it more complete"). More specification
→ more items to enforce → more enforcement debt → more specification to
close the debt. This is a reinforcing (positive) loop that was seeded at
the first design cycle and has now produced a 40-50k-word blueprint with
zero running executors. [alpha:31; zeta:93-100]

**Meadows rung:** L9 (goals of the system). The system's implicit goal is
"achieve completeness of specification." This goal was never explicitly set;
it is the emergent product of the FPF discipline applied iteratively. Until
the goal shifts from "completeness" to "executability," the loop runs.

**Observable KPI:** spec-lines-added / executor-lines-added ratio per cycle.
Currently: ~8077 lines specification, ~0 lines executor code (zero hooks,
zero BFS, zero alpha-movers). Ratio ≈ ∞. 2× improvement: ratio drops below
10:1 within 3 cycles.

**Kill-condition:** If the ratio drops below 10:1 across 3 consecutive cycles
without a corresponding drop in artefact quality, H-1 is killed (the spec-
accumulation loop was not dominant).

---

### H-2. The Variety-Mismatch Balancing Loop That Cannot Balance (L4 — Delays)

**Substrate:** Brigadier as sole controller + swarm as 20-cell system.

**Feedback loop (−):** Brigadier dispatches → errors accumulate in wiki →
brigadier review finds errors → brigadier corrects → next dispatch is more
careful. This is a balancing loop in theory. In practice the loop has a FATAL
delay: brigadier's error-detection depends on manual review (no hooks, no lint
scheduler). Error-detection delay is unbounded. With unbounded delay, the
balancing loop overshoots or never corrects. Beta found 7 inconsistencies
that brigadier missed across 6 agent files. [beta:228-306; gamma:46-49]

**Meadows rung:** L4 (delays). The correction delay in the balancing loop is
the leverage point. Reducing it (via PostToolUse lint hook) would dramatically
improve the loop's ability to balance. This is a L4 intervention, not a L8
(rules change), not a L6 (information structure change) — both are
downstream of delay.

**Observable KPI:** median time-to-detection of a wiki inconsistency, measured
in cycles. Currently: unbounded (no lint scheduled). 2× improvement: ≤1 cycle
detection latency.

**Kill-condition:** If a PostToolUse lint hook is wired and inconsistency
rate still grows (new inconsistencies appear faster than lint catches them),
the delay hypothesis is wrong — the problem is variety mismatch, not delay.

---

### H-3. The Missing Compounding Loop (L8 — Rules of the System)

**Substrate:** strategies.md × alpha-3 skill pipeline × compound step.

**Feedback loop (+, ABSENT):** The intended reinforcing loop is: cycle closes
→ compound step extracts rules → strategies.md grows → next cycle's brigadier
dispatches with better rules → artefact quality rises → faster cycles → more
cycles closed. This loop DOES NOT EXIST because (a) zero cycles have closed
[gamma:240], (b) alpha-3 pipeline has never fired [epsilon:50-55], (c)
compound step is ad-hoc [epsilon:196-201]. The swarm has the anatomy for
compounding but the connective tissue (movers) is absent.

**Meadows rung:** L8 (rules of the system). The rule "after every closed
cycle, run compound step and extract ≥1 DRR rule" is not enforced. Adding
this rule adds the compounding loop. Without it, the swarm cannot improve.

**Observable KPI:** strategies.md DRR entries per closed cycle. Currently: 0
(scaffolding only). 2× improvement: ≥1 entry per cycle by cycle 3.

**Kill-condition:** If strategies.md grows ≥1 DRR entry per cycle but artefact
quality (acceptance-predicate pass rate) does not improve across 10 cycles,
H-3 is killed (compounding loop is not the dominant mechanism for quality gain).

---

### H-4. The Adjacent-Possible Constraint (Kauffman) — Phase B is Not Adjacent

**Substrate:** Phase A → Phase B transition design.

**Pattern (Kauffman adjacent-possible):** A system can only reach states
adjacent to its current configuration. Phase B assumes: "Phase A bootstrap
complete → Phase B activates Tier-4 books, typed-BFS, community detection,
split triggers, 400-label golden sets." But the current Phase A state has:
zero closed cycles, zero edges, zero compounding, zero alpha-3 transitions,
zero working hooks. Phase B sits multiple hops away from the current state,
not adjacent. The adjacent states from the current configuration are:
(1) first cycle closed, (2) first hook wired, (3) first edge written,
(4) first strategy rule extracted. Phase B cannot be reached without passing
through all four. [gamma:46-49; epsilon:50-55; alpha:59]

**Meadows rung:** L9 (goals). The goal of "Phase B activation" is too far
from the current state to serve as a leverage point. Reformulating the goal
as "close first cycle with ≥1 DRR rule and ≥1 hook wired" makes it adjacent.

**Observable KPI:** count of adjacent-state prerequisites met (0/4 currently).
2× improvement: ≥2/4 prerequisites met by end of next cycle.

**Kill-condition:** If Phase B activates from the current state (zero
prerequisites) without the adjacent steps AND quality does not degrade,
the Kauffman adjacent-possible constraint is not binding here.

---

### H-5. Requisite Variety Mismatch Between Brigadier and Swarm (Ashby)

**Substrate:** Brigadier single-node orchestration + swarm's 20-cell variety.

**Feedback loop (−, overloaded):** Brigadier must regulate: wiki writes,
mode dispatch, provenance gate, edge consistency, alpha-2 lifecycle, alpha-3
lifecycle, alpha-4 lifecycle, HITL gate, 24-lock compliance, FPF E-1..E-18.
Ashby: controller variety must equal system variety. Brigadier has 1-node
sequential variety. Swarm variety is 20 cells × 4 modes × 5 alphas × 12 edge
types × 24 locks. The mismatch ratio is approximately 1:500. [beta:228-306;
shared-protocols:145-152]

**Meadows rung:** L6 (structure of information flows). The information
brigadier uses to control the system (manual inspection of artefacts) is
structurally insufficient. Adding automated information flows (lint hooks,
alpha-4 mover, health.md live counters) would reduce brigadier's effective
variety-demand by offloading routine regulation.

**Observable KPI:** brigadier review-failure rate (inconsistencies found per
brigadier cycle that brigadier missed). Currently: 7/7 cross-agent inconsistencies
missed until beta cell inspected. 2× improvement: ≤3 per cycle within 5 cycles.

**Kill-condition:** If automated lint catches ≤50% of brigadier-missed
inconsistencies (tool is no more effective than manual), then the L6
information-flow hypothesis is wrong — the problem is brigadier intelligence
(an L3/L2 problem), not information structure.

---

### H-6. The VSM Level-3 Audit Function is Absent (Beer)

**Substrate:** Swarm meta-governance.

**VSM mapping:**
- Level 1 (operations): 5 expert cells producing drafts.
- Level 2 (coordination): brigadier dispatching, integrating, running provenance gate.
- Level 3 (audit/optimisation): ABSENT. The meta-agent exists as a file
  (`.claude/agents/meta-agent.md` per CLAUDE.md roster) but has never run
  a cycle; `meta/health.md` counters are frozen at 0; no weekly sweep fires.
  [gamma:64; epsilon:50-55]
- Level 4 (intelligence/futures): partially covered by scalability modes.
- Level 5 (identity/policy): FPF + shared-protocols is the identity; human (Ruslan) holds Level 5.

**The Level-3 gap predicts:** the swarm optimises within individual cells
(expert modes work correctly in isolation) but does not optimise the swarm
itself (no agent is measuring cell-quality over time, no feedback from outcome
to strategy). The strategies.md files are the ANATOMY of Level-3 but without
the compound step running, they carry no physiology.

**Feedback loop (−, absent):** meta-agent audits → health.md updated →
brigadier adjusts dispatch policy → cell quality improves → meta-agent audits
confirm. This loop is fully specified but never instantiated.

**Meadows rung:** L8 (rules). The rule "meta-agent runs weekly sweep" is
specified but not enforced.

**Observable KPI:** meta/health.md `active_skills_count` and `closed_cycles_count`.
Both are 0. 2× improvement: both non-zero by cycle 5.

**Kill-condition:** If meta-agent weekly sweep fires but health.md counters
do not move (the mover code has bugs), H-6 is killed (the problem is
implementation, not Level-3 absence).

---

### H-7. Senge L1 — Today's Phase-A Solution Will Produce Phase-B Pathology

**Substrate:** Soft mode-prefix design decision.

**Senge L1:** "Today's problems come from yesterday's solutions." The decision
to use soft mode-prefix (AP-5-acknowledged as a prompt-level soft constraint)
was made to keep agent files simpler and defer hook engineering to Phase B.
The predicted Phase-B pathology: hook engineering in Phase B must retrofit
against 20 cells that have each developed local default-mode conventions
(beta found 6 phrasings already). Retrofitting is more expensive than
building-in. The Phase-A soft-prefix decision is generating the Phase-B
mode-confusion debt. [alpha:48; beta:266-285; zeta:44]

**A second Senge L1 candidate:** The decision to NOT write alpha-4 closed-
cycle movers in Phase A (deferred to "Phase B automation") means every cycle
that closes will require manual brigadier action. Each manually-closed cycle
reinforces the "manual is fine" convention, making the eventual automation
harder to introduce (convention debt compounds). [gamma:240; epsilon:238-249]

**Feedback loop (+ reinforcing, pathological):** deferred automation → manual
convention established → next design phase must fight established convention →
automation deferred again. This is a reinforcing loop in the wrong direction.

**Meadows rung:** L9 (goals). The goal "keep Phase A simple, automate Phase B"
produces the pathology. Reformulating as "automate exactly what will cost 5×
more to retrofit" is a goal-level leverage shift.

**Observable KPI:** count of manual brigadier actions per cycle that are spec'd
as "Phase B automations." Currently: every cycle close, every alpha-4
transition, every provenance gate check, every lint pass = ≥4 manual actions
per cycle. 2× improvement: ≤2 by cycle 10 (≥2 automations wired).

**Kill-condition:** If Phase B automation is installed WITHOUT significant
rework of existing manual conventions, H-7 is killed (convention debt was
not actually compounding).

---

### H-8. The Measurement Void is Itself the Dominant Leverage Point (L6 — Information)

**Substrate:** All feedback loops in the swarm.

**Pattern:** Every feedback loop in the swarm requires information to close.
The reinforcing compounding loop requires "did artefact quality improve?"
The balancing correction loop requires "how many inconsistencies appeared?"
The Level-3 audit loop requires "what is the cell pass-rate?" None of these
information signals exist. Meta/health.md counters are frozen. No FPAR
computed. No golden-set pass-rate tracked. Zeta names this as MP-3
"measurement-void" [zeta:108-112] but does not frame it as a SYSTEMS
LEVERAGE POINT.

**Feedback loop (−, severed):** Every balancing loop in the swarm requires a
sensor. There are no sensors. The system is running open-loop: actions are
taken (specs written, artefacts drafted) but no feedback on outcomes reaches
any controller (brigadier, meta-agent, or Ruslan between cycles).

**Meadows rung:** L6 (structure of information flows). A severed feedback
loop at L6 is more fundamental than any L8/L9 intervention, because L8 rules
and L9 goals that are based on no information produce random walk, not
improvement. The measurement-void is the most upstream failure.

**Observable KPI:** count of closed feedback loops in meta/health.md with
non-null current values. Currently: 0/5 (all counters null or 0). 2× improvement:
≥3/5 counters live by cycle 5.

**Kill-condition:** If health.md counters are populated but swarm behaviour
does not improve across 10 cycles (decisions are not being taken based on
the numbers), H-8 is killed (information was not the bottleneck — decision-
taking based on information is the missing step).

---

### H-9. The Single-Writer Rule Creates a Single-Point-of-Failure at Level 2 (Beer VSM)

**Substrate:** Q2 single-writer brigadier rule.

**Pattern (Beer VSM Level 2):** At VSM Level 2, coordination between Level-1
operations depends on the capacity of the coordination layer. The single-
writer rule concentrates ALL wiki-write throughput through a single sequential
node (brigadier). This is correct for Phase A (quality control), but it
creates a Level-2 coordination bottleneck. At current scale (1 closed cycle),
the bottleneck is invisible. At 10× scale (10 parallel tasks, 50 cells active),
brigadier becomes the system's rate-limiting step.

**Feedback loop (− balancing, self-limiting):** brigadier throughput is
finite → queue of expert drafts pending promotion grows → brigadier promotes
fewer artefacts per cycle → expert cells produce drafts that accumulate in
`drafts/` → expert cycle velocity drops. This is a classic Beer VSM Level-2
coordination-capacity balancing loop that will bind as scale grows.

**Meadows rung:** L2 (size of buffers, stocks). The `swarm/wiki/drafts/` is
the buffer. At current scale it is nearly empty (zero drafts promoted from
real cycles). The buffer-capacity hypothesis predicts the bottleneck emerges
at the transition from 1-task to 5-parallel-task operation.

**Observable KPI:** draft-promotion latency (time from cell-draft to brigadier-
promotes). Currently: ≤1 hour (single task). 2× improvement at 10× scale:
promotion latency should not exceed 4× current latency (i.e., should not
grow faster than linear with task count).

**Kill-condition:** If at 5 parallel tasks promotion latency grows < 2× from
single-task baseline, the single-writer bottleneck is not binding at this
scale and H-9 is killed (the coordination capacity is sufficient).

---

## ≥2 Alternatives + Status Quo

| Alternative | Description | Kill-condition |
|---|---|---|
| Alt-1: Swarm quality is bottlenecked at the INFORMATION layer (H-8, L6) | The dominant failure is severed feedback loops (no sensors, no counters, no eval harness). Fix measurement first; everything else is downstream. Predicts: wiring health.md live counters + FPAR produces improvement in ALL other loops simultaneously. | Killed if: health.md counters wired AND artefact quality does not improve across 5 cycles (information was not the bottleneck). |
| Alt-2: Swarm quality is bottlenecked at the GOAL layer (H-1, L9) | The dominant failure is the implicit goal of "completeness-of-specification" running the reinforcing spec-accumulation loop. Fix the goal (shift to "executability-first") and the information deficit and the executor deficit resolve together. Predicts: a single policy directive ("no new spec line without a paired executor") produces more improvement than wiring sensors. | Killed if: executability-first rule adopted AND the spec-accumulation loop does not decelerate (i.e., new spec still appears at prior rate), suggesting the goal is not driving the behaviour. |
| Status quo: Swarm quality is bottlenecked at the EXECUTOR layer (MP-1, all extractions) | The dominant failure is missing hook code, alpha-movers, BFS executor. Fix the 3-5 bash scripts and 80% of the system comes online. Predicts: each script written unblocks a specific feedback loop. | Killed if: 3-5 executors are wired AND the system does not measurably improve (the bottleneck was elsewhere — perhaps the controller variety mismatch of H-5 dominates). |

**Loop-dominance hypothesis:** H-8 (measurement void) is likely dominant
because it is upstream of all other loops. H-1 (spec-accumulation) is the
generator. Status quo (executor gap) is the most visible symptom. The systems
prediction is: fix H-8 first (sensors), then H-3 (compounding), then status
quo (executors). Intervening at the executor level without measurement will
produce executors that don't compound.

**Time horizon:** hypotheses hold within Phase A (cycles 1-10). Loop dominance
is expected to shift at cycle 20+ as the compounding loop (H-3) begins to
produce accumulated strategy rules that change cell behaviour.

---

## Anti-scope

This critique does NOT:
- Score code-level architecture quality of any agent file — that is
  engineering-expert territory.
- Arbitrate whether the FPF ontology is epistemically correct — that is
  philosophy-expert territory.
- Recommend capital allocation between Phase A and Phase B investments —
  that is investor-expert territory.
- Prioritise the 2× improvement surfaces across each other from a delivery-
  schedule standpoint — that is mgmt-expert territory.
- Evaluate whether the Every compound-engineering-plugin is a good software
  choice — that is engineering-expert × critic territory.
- Adjudicate the €50K / €200K horizon-gate discrepancy between investor and
  peer experts — that is investor-expert × critic territory.

This critique IS limited to: system boundary, feedback loops (polarity,
substrate, delay, dominance), leverage points (Meadows rung), requisite
variety (Ashby), VSM recursion (Beer), emergence (substrate + counter-sample),
adjacent-possible (Kauffman), Senge 11 laws as a critic checklist.

---

## Recommended Changes

**RC-1.** Declare the swarm's system boundary explicitly. Name ≥5 out-of-
system items (Ruslan's calendar, v2 wiki, Notion, Anthropic API latency,
git remote latency). Without an explicit boundary, every "improvement" might
be acting inside or outside the relevant system.

**RC-2.** Wire health.md live counters before any other Phase-A improvement
(H-8 is upstream of all loops). Measurable criterion: `closed_cycles_count`,
`active_skills_count`, `fpar_log` non-null by next cycle.

**RC-3.** Name and declare the dominant reinforcing loop (H-3: cycles-closed
→ compound → strategies-grow → quality-rises) and the dominant balancing loop
(H-2: errors-accumulate → brigadier-detects → correction) as first-class
artefacts in the swarm model. Assign a polarity (+/−) and a time-constant.
Without this, the swarm system model is implicit and unverifiable.

**RC-4.** Add AP-SYS-11 (cells-calling-cells) to systems-expert §8 per beta's
finding S-4. The absence is a self-blindness defect, acknowledged above.

**RC-5.** For each Phase-A "improvement surface" across the six extractions,
require a paired baseline KPI before the surface is declared 2×-improvable.
Currently, 5 of 6 extractions name improvements without baselines. Without a
baseline, the 2× claim cannot be verified.

**RC-6.** Articulate the Senge L1 debt explicitly in a decisions/ artefact:
"Phase-A deferred automation choices that will generate Phase-B rework cost."
This forces the goal-level (L9) question — is the rework cost acceptable? —
to be made consciously rather than inherited.

---

## Acceptance Test (passable by next revision)

`count(named_feedback_loops with polarity in {+,-} AND substrate AND time_horizon) >= 2
AND count(leverage_points with Meadows_rung AND observable_KPI) >= 4
AND system_boundary declared with >=3 explicit out_of_system_items
AND meta/health.md has >=1 non-zero counter (measurement loop opened)
AND AP-SYS-11 added to systems-expert §8`
