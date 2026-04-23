---
type: systems-optimizer
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
mode: optimizer
agent: systems-expert
created: 2026-04-23
pipeline: drafted
state: drafted
confidence: medium
confidence_method: invariant-check
sources:
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-critic-01.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md
  - swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md
invariants:
  WLNK: preserved
  MONO: preserved
  IDEM: preserved
  COMM: n/a
  LOC: preserved
antifragility_check: n/a   # antifragility check is scalability-mode scope; optimizer is parameter-level only
niche: meta
requisite_variety_budget:
  captured: >
    9 ranked hypotheses with scoring function (rung × loop-gain-delta / effort),
    per-hypothesis sensor and actuator placement, sharpened measurables with
    explicit N-counts and cycle targets, intervention sequence, kill-conditions
    preserved from critic-01.
  actual_estimate: >
    Same as critic-01 frontmatter: ~15-20% of full system variety; optimizer
    does not expand variety coverage — it sharpens targeting within the captured
    20%.
---

# Systems Optimizer — Swarm Phase-A Self-Model
## Baseline: systems-critic-01 H-1..H-9
## Optimization domain: leverage-point targeting (parameter-level, not method-level)

---

## Invariant Pre-Check

| Invariant | Apply? | Preserved? | Notes |
|---|---|---|---|
| WLNK | yes | yes | Causal links brigadier→wiki→strategies→brigadier; meta-agent→health.md→brigadier all preserved; re-ranking does not sever any sub-system link |
| MONO | yes | yes | Meadows rung assignments from critic-01 are not re-assigned; scoring adds a second axis (loop-gain-delta / effort) without inverting rung ordering |
| IDEM | yes | yes | Scoring function is deterministic given fixed inputs; applying twice yields same ranked set |
| COMM | n/a | — | Only one optimization step proposed |
| LOC | yes | yes | Delta confined to task artefact space; no adjacent systems modified |

---

## Scoring Function

Each hypothesis is scored on three dimensions, then ranked.

**Score = (Meadows-rung-weight × loop-gain-delta) / effort-class**

Meadows-rung-weight: inverted rung number so higher-leverage rungs score
higher. L1=12, L2=11, L3=10, L4=9, L5=8, L6=7, L7=6, L8=5, L9=4, L10=3,
L11=2, L12=1. (Meadows' own ordering: L1 strongest, L12 weakest.)

Loop-gain-delta: estimated fractional gain in the targeted loop's closure
probability if the intervention is applied. Scale 1–5 (1=marginal,
5=loop closes from open to closed in one intervention).

Effort-class: 1=hours, 2=days, 3=sprint (1–2 weeks), 4=multi-sprint.

Score = (rung-weight × loop-gain-delta) / effort-class.

---

## Before / After Snapshot

### Baseline state (critic-01, unranked)

| H | Meadows rung | Loop type | KPI (baseline) | Effort |
|---|---|---|---|---|
| H-1 | L9 (goals) | + reinforcing (spec-accumulation) | spec/executor ratio ≈ ∞ | 3 (sprint) |
| H-2 | L4 (delays) | − balancing (correction-delay) | time-to-detect inconsistency = unbounded | 2 (days) |
| H-3 | L8 (rules) | + reinforcing (ABSENT) | DRR entries per cycle = 0 | 2 (days) |
| H-4 | L9 (goals) | pattern (adjacent-possible) | prerequisites met = 0/4 | 2 (days) |
| H-5 | L6 (information structure) | − balancing (overloaded) | brigadier review-failure rate = 7/7 | 2 (days) |
| H-6 | L8 (rules) | − balancing (ABSENT) | health.md active counters = 0/5 | 2 (days) |
| H-7 | L9 (goals) | + reinforcing (pathological) | manual actions per cycle ≥ 4 | 3 (sprint) |
| H-8 | L6 (information) | − balancing (SEVERED) | closed feedback loops in health.md = 0/5 | 1 (hours) |
| H-9 | L2 (buffer size) | − balancing (self-limiting) | promotion latency ≤ 1 hr (latent bottleneck) | 4 (multi-sprint) |

### Scoring

| H | Rung-weight | Loop-gain-delta | Effort-class | Score | Notes |
|---|---|---|---|---|---|
| H-8 | 7 (L6) | 5 (severs loop → closes it) | 1 (hours) | **35.0** | health.md population is a 1-hour script; closes ALL measurement loops simultaneously |
| H-3 | 5 (L8) | 5 (loop goes from absent to present) | 2 (days) | **12.5** | compound step rule adds the compounding loop; prerequisite is ≥1 closed cycle |
| H-2 | 9 (L4) | 4 (delay reduced from unbounded to 1-cycle) | 2 (days) | **18.0** | PostToolUse lint hook reduces correction delay; high rung-weight |
| H-5 | 7 (L6) | 3 (reduces brigade-failure rate ~50%) | 2 (days) | **10.5** | automated information flow (lint + health counters) reduces variety-demand on brigadier |
| H-6 | 5 (L8) | 4 (Level-3 loop goes from absent to present) | 2 (days) | **10.0** | meta-agent sweep rule; depends on health.md being non-zero (H-8 prerequisite) |
| H-1 | 4 (L9) | 2 (goal shift is slow; reinforcing loop decelerates) | 3 (sprint) | **2.7** | goal-level intervention; requires human policy directive; long feedback path |
| H-4 | 4 (L9) | 3 (prerequisite count rises 0/4→2/4) | 2 (days) | **6.0** | adjacent-possible constraint; practical adjacency work |
| H-7 | 4 (L9) | 2 (debt is named; deceleration uncertain) | 3 (sprint) | **2.7** | Senge L1 debt documentation; valuable but slow-acting |
| H-9 | 11 (L2) | 1 (latent; bottleneck not yet binding) | 4 (multi-sprint) | **2.75** | buffer-capacity bottleneck emerges at 10× scale; zero urgency Phase A |

### Ranked hypotheses (proposed, post-optimization)

| Rank | H | Score | Optimization action |
|---|---|---|---|
| 1 | **H-8** | 35.0 | Populate health.md live counters (sensor placement — see §OPT-1) |
| 2 | **H-2** | 18.0 | Wire PostToolUse lint hook to reduce correction delay (actuator placement — see §OPT-2) |
| 3 | **H-3** | 12.5 | Enforce compound-step rule as written rule + mover (feedback path closure — see §OPT-3) |
| 4 | **H-5** | 10.5 | Wire automated information flows to reduce brigadier variety-demand (see §OPT-4) |
| 5 | **H-6** | 10.0 | Instantiate meta-agent Level-3 audit rule (depends on Rank-1 prerequisite — see §OPT-5) |
| 6 | **H-4** | 6.0 | Name and close adjacent-state prerequisites (see §OPT-6) |
| 7 | **H-9** | 2.75 | Monitor buffer latency; no Phase-A action required (see §OPT-7) |
| 8 | **H-7** | 2.7 | Document Senge L1 debt in decisions/ (see §OPT-8) |
| 9 | **H-1** | 2.7 | Shift goal explicitly via policy directive (see §OPT-9) |

---

## Per-Optimization Detail

Each optimization is a LOCALITY choice: which sensor, which actuator,
which feedback path. NOT a method change.

### OPT-1 — H-8: Sensor placement for measurement loop (Rank 1)

**Meadows rung:** L6 (information structure).
**Loop:** All balancing loops in the swarm are severed because no sensors
exist. This is the most upstream failure.

**Sensor placement (WHERE to put the sensor):**
- File: `swarm/wiki/meta/health.md`
- Sensor type: filesystem-derived counters (deterministic, no SDK)
- Sensor script: a ~20-line bash fragment or PostToolUse hook that
  recomputes counters from filesystem truth on every brigadier Write:
  - `closed_cycles_count = count(swarm/logs/*/cycle-log.md)`
  - `active_skills_count = count(swarm/wiki/skills/active/*.md)`
  - `open_tasks_count = count(swarm/wiki/tasks/*/manifest.yaml) minus count(swarm/wiki/tasks/*/artefacts/*cycle-log*)`
  - `lint_findings_count = count(lines matching "FAIL" in most recent /lint run)`
  - `fpar_log = acceptance-predicate pass-rate across last N artefacts (bootstrap: null until cycle 3)`

**Sharpened measurable (baseline → proposed):**
- Baseline: 0/5 health.md counters non-null.
- Proposed: ≥3/5 counters non-null (filesystem-derived; null-safe for
  fpar_log which requires ≥3 closed cycles).
- **Specific target:** `closed_cycles_count ≥ 1 AND active_skills_count
  (nullable-ok) AND open_tasks_count ≥ 1` all non-null by end of cycle 1
  (the current cycle). `lint_findings_count` non-null by cycle 2 (requires
  lint hook wired per OPT-2). `fpar_log` nullable until cycle 3.

**Kill-condition preserved from critic-01:** If health.md counters are
populated but swarm behaviour does not improve across 10 cycles (decisions
not taken based on the numbers), H-8 is killed.

**Method-change check:** This is a sensor placement decision (which file,
which counters, which update trigger). It is NOT a decision about whether
to use measurement at all — that is already the method. LOC confirmed.

---

### OPT-2 — H-2: Actuator placement for correction-delay loop (Rank 2)

**Meadows rung:** L4 (delays).
**Loop:** Brigadier dispatches → errors accumulate → brigadier review finds
errors → correction. Balancing loop with unbounded detection delay.

**Actuator placement (WHERE to put the actuator to reduce delay):**
- Hook: `PostToolUse` on any `Write` to `swarm/wiki/` (excluding `drafts/`,
  `_archive/`, `_templates/`).
- Actuator action: invoke `/lint` dry-run on the written file; on FAIL,
  prepend a rejection entry to `swarm/wiki/meta/health.md` `lint_findings_log`
  and notify brigadier in the same tool-call response.
- Sensor for this loop: the PostToolUse hook output is itself the sensor;
  the actuator is the immediate pre-commit block.

**Sharpened measurable (baseline → proposed):**
- Baseline: median time-to-detection of wiki inconsistency = unbounded
  (no lint scheduled; detected only at brigadier manual review).
- Proposed: median time-to-detection = within 1 tool-call cycle (same
  brigadier session as the errant Write).
- **Specific target:** PostToolUse hook wired in `.claude/settings.json`
  such that `lint_findings_count` in health.md increments within the same
  cycle as any provenance-gate violation. Verifiable: `grep "FAIL" in
  lint_findings_log within cycle where violation occurred`.

**Kill-condition preserved from critic-01:** If PostToolUse lint hook is
wired and inconsistency rate still grows (new inconsistencies faster than
lint catches them), the delay hypothesis is wrong — problem is variety
mismatch (H-5 dominant).

**Method-change check:** This is an actuator placement decision (hook
location, trigger condition). NOT a decision about whether to use lint at
all. LOC confirmed.

---

### OPT-3 — H-3: Feedback path closure for compounding loop (Rank 3)

**Meadows rung:** L8 (rules).
**Loop:** cycles-closed → compound step → strategies.md grows → next
dispatch better → artefact quality rises. Loop is anatomically present but
physiologically absent (movers not wired).

**Feedback path to close (WHICH path):**
The loop has three severed segments:
- Segment A: cycle closes → compound step fires. Severed because α-4
  `closed` mover does not exist.
- Segment B: compound step → strategies.md DRR entry appended. Severed
  because compound step is ad-hoc.
- Segment C: strategies.md growth → brigadier dispatch quality improves.
  Severed because brigadier does not re-read strategies.md between dispatches.

**Close Segment A first** (lowest effort, highest upstream impact):
- Mover: a PostToolUse hook or manual brigadier discipline: "when
  `swarm/logs/<cycle-id>/cycle-log.md` is created, increment
  `closed_cycles_count` in health.md AND prompt brigadier to run compound
  step."
- This is the prerequisite for Segments B and C.

**Sharpened measurable (baseline → proposed):**
- Baseline: strategies.md DRR entries per closed cycle = 0.
- Proposed: ≥1 DRR entry per closed cycle, appended by the responsible
  expert within the Compound step of the same cycle.
- **Specific target:** After cycle 1 closes (this cycle),
  `agents/systems-expert/strategies.md` carries ≥1 DRR entry from cycle 1
  with Decision / Reasoning / Result / Review all non-empty. Cycle 2 must
  carry a second entry. By cycle 3: ≥3 entries, all four DRR parts non-empty
  per entry.

**Kill-condition preserved from critic-01:** If strategies.md grows ≥1 DRR
entry per cycle but acceptance-predicate pass rate does not improve across
10 cycles, H-3 is killed.

**Method-change check:** This is a feedback path decision (which segment to
close first, which mover to use). Not a method change. LOC confirmed.

---

### OPT-4 — H-5: Information flow to reduce brigadier variety-demand (Rank 4)

**Meadows rung:** L6 (information structure).
**Loop:** Brigadier must regulate 20 cells × 4 modes × 5 alphas. Single-node
sequential variety. Ashby: controller variety must match system variety.

**Information flow to add (WHICH flow, WHERE):**
Three automated flows reduce brigadier's effective variety-demand without
changing brigadier's role:
1. **alpha-2 lifecycle mover** — instead of brigadier tracking every
   artefact's pipeline state, a simple rule: when an artefact is written
   to `swarm/wiki/drafts/`, its `pipeline:` frontmatter field is set to
   `drafted` automatically. Brigadier only needs to action `drafted` artefacts;
   the state machine self-updates.
2. **Cross-agent consistency check** — beta found 7 inconsistencies that
   brigadier missed. A `/lint --cross-agent` pass that greps for known
   inconsistency patterns (§7 header drift, mode-prefix phrasing variants,
   DRR label variants) reduces the information brigadier must hold in memory.
3. **health.md as information relay** — once OPT-1 counters are live, brigadier
   reads health.md at session start instead of conducting a manual survey of
   the wiki state. Reduces survey overhead from O(files) to O(1).

**Sharpened measurable (baseline → proposed):**
- Baseline: brigadier review-failure rate = 7/7 cross-agent inconsistencies
  missed per manual pass.
- Proposed: ≤2/7 cross-agent inconsistencies missed per cycle (automated
  lint catches the remainder).
- **Specific target:** `/lint --cross-agent` run produces ≥1 finding for each
  of β's 7 R-* inconsistencies when run against current agent files.
  Verifiable by comparing lint output against beta's R-1..R-7 list.

**Kill-condition preserved from critic-01:** If automated lint catches ≤50%
of brigadier-missed inconsistencies, problem is brigadier intelligence (L3/L2),
not information structure (L6).

**Method-change check:** This is an information-flow routing decision (which
flows to add, where they terminate). Not a method change. LOC confirmed.

---

### OPT-5 — H-6: Rule instantiation for Level-3 audit loop (Rank 5)

**Meadows rung:** L8 (rules).
**Loop:** meta-agent audits → health.md updated → brigadier adjusts dispatch
→ cell quality improves. Loop specified, never instantiated.

**Prerequisite dependency:** H-6 CANNOT be closed before H-8 (OPT-1). The
meta-agent loop requires non-zero health.md counters as its input signal.
If health.md counters remain frozen at 0, the meta-agent sweep produces no
useful output.

**Rule to instantiate (WHICH rule to add first):**
The single highest-leverage rule addition is:
- Rule: "After each cycle closes, meta-agent reads health.md and computes
  cell-level pass-rate (acceptance_predicate passes / total dispatches per
  expert). If any expert's pass-rate < 60% over last 5 cycles, emit a
  HITL AWAITING-APPROVAL packet."
- This is the VSM Level-3 audit loop in its minimal viable form: one rule,
  one metric, one escalation path.

**Sharpened measurable (baseline → proposed):**
- Baseline: health.md `active_skills_count` and `closed_cycles_count` = 0.
  Meta-agent weekly sweep: never run.
- Proposed: after cycle 1 closes AND OPT-1 is applied, health.md carries
  `closed_cycles_count ≥ 1`. Meta-agent runs the minimal Level-3 pass
  (cell pass-rate check) within 1 cycle of the first close.
- **Specific target:** `swarm/wiki/meta/health.md` `fpar_log` field contains
  ≥1 record by cycle 3 (requires ≥3 closes). Until cycle 3, meta-agent sweep
  is advisory-only (no enforced escalation).

**Kill-condition preserved from critic-01:** If meta-agent sweep fires but
health.md counters do not move (mover code bugs), H-6 is killed (implementation
problem, not Level-3 absence).

**Method-change check:** Rule addition (which rule, at which rung). Not a
method change. LOC confirmed.

---

### OPT-6 — H-4: Adjacent-state prerequisite sequencing (Rank 6)

**Meadows rung:** L9 (goals).
**Pattern:** Kauffman adjacent-possible. Phase B requires all 4 prerequisites.
Currently 0/4 met.

**Goal reframe (WHICH goal to restate):**
The optimization is to make the goal adjacent, not to change the method.
Critic-01 named 4 prerequisites. Sequencing these prerequisites is the
parameter-level choice:

| Prerequisite | Achievable in cycle | Depends on |
|---|---|---|
| A: first cycle closed | cycle 1 (this cycle) | brigadier promotes this artefact |
| B: first hook wired | cycle 2 | OPT-2 (PostToolUse hook) |
| C: first edge written | cycle 2 | ≥1 artefact promoted + edge emitted to edges.jsonl |
| D: first strategy rule extracted | cycle 1 (Compound step) | OPT-3 Segment A |

**Sharpened measurable (baseline → proposed):**
- Baseline: 0/4 prerequisites met.
- Proposed: 2/4 prerequisites met by end of cycle 1 (A + D). 4/4 by end
  of cycle 2 (B + C).
- **Specific target:** After cycle 1 Compound step: `agents/systems-expert/
  strategies.md` has ≥1 new DRR entry (D met) AND `swarm/logs/cyc-swarm-
  self-improve-v1-2026-04-23/cycle-log.md` exists (A met).

**Kill-condition preserved from critic-01:** If Phase B activates from 0
prerequisites without the adjacent steps AND quality does not degrade,
Kauffman constraint is not binding here.

**Method-change check:** Goal restatement to make it adjacent. The goal
"Phase B activation" is not changed to something else — it is made reachable
by naming the path. LOC confirmed.

---

### OPT-7 — H-9: Buffer monitoring posture (Rank 7)

**Meadows rung:** L2 (buffer size).
**Loop:** draft-promotion buffer grows → brigadier throughput constrained.
Currently latent (0 drafts pending). Binding at 10× scale.

**Optimization:** NO Phase-A intervention required. The optimization is
to place a monitoring sensor WITHOUT an actuator (the actuator is a Phase-B
structural change and would be a method-level change here).

**Sensor placement:**
- Add `draft_promotion_latency_log` counter to health.md (one line, nullable
  until ≥5 promotions occur).
- Format: `{cycle_id, draft_written_at, promotion_at, latency_cycles}` per
  promotion event.
- Brigadier populates this field manually on each promotion until OPT-2
  PostToolUse hook can auto-populate it.

**Sharpened measurable (baseline → proposed):**
- Baseline: promotion latency not tracked; single task at ≤1 hour.
- Proposed: promotion latency logged per event; baseline established from
  first 5 promotions; alert if latency grows >4× baseline at 5 parallel tasks.
- **Specific target (Phase-A):** field present in health.md by end of cycle 1;
  populated with ≥1 record by cycle 3.

**Kill-condition preserved from critic-01:** If at 5 parallel tasks promotion
latency grows <2× from single-task baseline, H-9 is killed at that scale.

**Method-change check:** Sensor-only placement. Phase-B structural response
(if latency grows) is escalated, not pre-decided here. LOC confirmed.

---

### OPT-8 — H-7: Senge L1 debt documentation (Rank 8)

**Meadows rung:** L9 (goals).
**Loop:** deferred automation → manual convention established → convention
debt compounds.

**Documentation target (WHERE to write the debt):**
- A single `decisions/<slug>-phase-a-automation-debt-2026-04-23.md` artefact
  (requires brigadier to open; this optimizer proposes the artefact content,
  not the file write itself — per §1d, this expert proposes writes via
  `proposed_writes[]`; brigadier executes).
- Content: enumerate ≥4 Phase-A deferred automations with their estimated
  Phase-B rework cost. Force the L9 question: is the rework cost acceptable?
  Include a kill-condition for the debt claim itself.

**Sharpened measurable (baseline → proposed):**
- Baseline: manual brigadier actions per cycle ≥ 4, all spec'd as "Phase B
  automations." No explicit cost record.
- Proposed: ≤2 manual actions per cycle by cycle 10 (≥2 automations wired
  from OPT-2 and OPT-3). The debt document makes the trade-off explicit.
- **Specific target:** the decisions/ artefact lists ≥4 deferred items with:
  estimated rework multiplier (e.g. "3× harder to retrofit mode-prefix hook
  against 20 cells than to build-in at construction"), and a decision gate
  (accept debt / pay down now / re-evaluate at cycle 5).

**Kill-condition preserved from critic-01:** If Phase B automation installs
without significant rework of existing manual conventions, H-7 is killed
(convention debt was not compounding).

**Method-change check:** Documentation of an existing debt. Not a goal-change
itself. LOC confirmed.

---

### OPT-9 — H-1: Policy directive for goal shift (Rank 9)

**Meadows rung:** L9 (goals).
**Loop:** spec-accumulation reinforcing loop. Implicit goal = "completeness
of specification." Ratio spec-lines / executor-lines ≈ ∞.

**Why Rank 9 (lowest):**
H-1's goal-shift intervention is the weakest-ROI optimization in Phase A
for two reasons: (a) the goal "executability first" cannot be enforced
mechanically without the hooks from OPT-2/OPT-3 already in place, and
(b) the reinforcing loop will decelerate naturally once measurement loops
(OPT-1) make the spec/executor ratio visible. A policy directive issued
before sensors exist produces no corrective signal.

**Deferred action (not blocked, just deprioritised):**
Once OPT-1 (health.md counters) is live and the spec/executor ratio is
visible in the health dashboard, a Ruslan-authored policy directive
"no new spec line without a paired executor" becomes actionable. Until then,
the directive is a wish, not a leverage point.

**Sharpened measurable (baseline → proposed):**
- Baseline: spec/executor ratio ≈ ∞ (no executor lines in scope).
- Proposed: ratio ≤ 10:1 within 3 cycles after OPT-1 + OPT-2 + OPT-3 are
  applied. The 3-cycle window accounts for the time it takes the policy
  directive to propagate through the brigadier dispatch cycle.
- **Specific target (Phase-A):** After OPT-1 is live, health.md carries
  `spec_executor_ratio` counter. When ratio crosses 10:1, brigadier issues
  the policy directive.

**Kill-condition preserved from critic-01:** If the ratio drops below 10:1
across 3 consecutive cycles without a corresponding drop in artefact quality,
H-1 is killed.

**Method-change check:** Policy directive (parameter-level goal restatement).
Not a structural redesign of the goal-setting mechanism. LOC confirmed.

---

## Intervention Sequence (Recommended)

Based on scoring AND dependency analysis:

```
Cycle 1 (this cycle — Compound step):
  → OPT-1: Populate health.md live counters (hours; prerequisite for all others)
  → OPT-6 partial: Close prerequisite A (first cycle closed) + D (first DRR rule)

Cycle 2 (next cycle):
  → OPT-2: Wire PostToolUse lint hook (days; closes correction-delay loop)
  → OPT-3: Enforce compound-step rule + α-4 mover (days; closes compounding loop)
  → OPT-6 complete: Close prerequisites B (first hook) + C (first edge)

Cycle 3–5:
  → OPT-4: Wire automated cross-agent information flows (days)
  → OPT-5: Instantiate meta-agent Level-3 minimal rule (after health.md non-zero)
  → OPT-7: Populate draft_promotion_latency_log in health.md (monitoring only)
  → OPT-8: Write Phase-A automation debt artefact (brigadier proposes; Ruslan acks)

Cycle 10+:
  → OPT-9: Issue executability-first policy directive (after sensors confirm ratio)
```

**Dependency chain:** OPT-1 → OPT-5 (Level-3 loop needs non-zero counters).
OPT-2 → OPT-4 (cross-agent lint shares the hook). OPT-3 → OPT-6 partial D.
OPT-1 + OPT-3 → OPT-9 (goal shift needs sensor + compounding loop active).

---

## Method-Change Refusals

The brief asked for PARAMETER-level optimization (which sensor, which actuator,
which feedback path). The following requests that appeared in the inputs are
NOT acted on here because they are Method-level changes — routed to escalations:

1. **"Redesign the system from sequential to parallel orchestration"** — not
   explicitly in this brief but implicit in H-5's Ashby analysis. The
   parameter-level intervention (automated information flows) is adopted.
   The method-level intervention (replace brigadier single-node with
   distributed orchestration) is refused; would require a structural redesign
   → escalate to integrator-mode or scalability-mode.

2. **"Replace Meadows ladder with Beer VSM as the primary leverage vocabulary"**
   — not requested but would be a method change. This optimizer uses both
   (Meadows for rung scoring, Beer for Level assignment) without substituting one for the other.

---

## Before / After Summary Table

| Metric | Baseline (critic-01) | Proposed (optimizer-01) | Delta | Method (heuristic) |
|---|---|---|---|---|
| Hypotheses ranked by priority | 9 unranked | 9 ranked by score function | +scoring layer | Meadows rung-weight × loop-gain-delta / effort |
| H-8 placement in sequence | named as "likely dominant" but not ranked first | Rank 1 (score 35.0) | promoted from narrative to explicit first-action | measurement-void-is-upstream-leverage rule |
| H-2 (delay loop) placement | mentioned after H-5 in alternatives | Rank 2 (score 18.0) | promoted above H-5 | L4 rung-weight higher than L6 at same loop-gain |
| H-9 (buffer/scale) urgency | described as emerging bottleneck | Rank 7 (score 2.75); sensor-only Phase A | deprioritised; monitor only | LOC — structural response is Phase B |
| health.md target | "≥3/5 counters live by cycle 5" | "≥3/5 counters non-null; ≥1 by end of cycle 1" | sharpened cycle target | adjacent-possible + Ashby simplification |
| strategies.md target | "≥1 DRR entry per cycle by cycle 3" | "≥1 DRR entry per closed cycle, starting cycle 1; all 4 DRR parts non-empty" | sharpened entry requirement | compound-step rule (L8 enforcement) |
| edges.jsonl target | "first edge written" (vague) | "≥1 edge written with typed record in edges.jsonl by end of cycle 2" | N count added | MP-4 counter-to-contract discipline |
| lint detection target | "≤1 cycle detection latency" | "within 1 tool-call cycle in same brigadier session" | sub-cycle precision | PostToolUse hook LOC |
| meta-agent Level-3 activation | "both counters non-zero by cycle 5" | "after OPT-1 applied AND ≥1 cycle closed; minimal rule (cell pass-rate check) within 1 cycle of first close; `fpar_log` entry by cycle 3" | sequenced after prerequisite | VSM Level-3 dependency on Level-2 health signal |
| Phase-B gate prerequisites | "0/4 met" | "A+D met by cycle 1; B+C by cycle 2" | explicit sequence | Kauffman adjacent-possible |

---

## Risks

1. **OPT-1 and OPT-2 are in `.claude/settings.json` territory.** The PostToolUse
   hook (OPT-2) requires a write to `.claude/settings.json`. This is not forbidden
   (it is not `~/.ssh/` or `/etc/` territory) but it IS a structural change to
   the hook layer — which was previously described as "Phase B stub." If brigadier
   treats hook-layer changes as Phase-B-only, OPT-2 is blocked. This optimizer
   notes the risk but does not resolve it — resolution requires brigadier + Ruslan
   judgment. If OPT-2 is blocked, OPT-1 (health.md counter script) can still
   proceed without the hook, using a manual brigadier-run script instead.

2. **Loop-gain-delta estimates are F3 (multi-case pattern level), not F5+.**
   The loop-gain-delta values (1–5 scale) are derived from pattern-matching
   against the critic-01 substrate and the zeta/gamma/alpha extractions, not
   from measured outcomes. The scoring function is directionally correct but
   not metrically precise. Any ranking decision that turns on a score difference
   of <2 should be treated with caution.

3. **H-8 scores 35.0; second-place H-2 scores 18.0.** The gap is large, which
   reinforces the "sensor first" conclusion but also means that if the loop-gain-
   delta for H-8 was overestimated (e.g. health.md counters are populated but
   no one reads them), the ranking is robust to moderate estimation error.
   Kill-condition for H-8 explicitly covers this case.

4. **H-1 (spec-accumulation) is ranked last but is the GENERATOR of the
   system's current state.** Ranking it last does not make it unimportant — it
   means it is not the most tractable Phase-A lever. The spec-accumulation loop
   will decelerate when sensors (OPT-1) make the ratio visible and when
   compounding (OPT-3) gives brigadier a mechanism to act on the ratio signal.
   Ranking H-1 last is a sequencing decision, not a dismissal.

---

## Provenance

- systems-critic-01.md: H-1..H-9 hypotheses [critic-01:203-479],
  loop-dominance claim [critic-01:491-500], alternatives [critic-01:487-490]
- zeta-cross-pollination.md: MP-1 (executor gap) [zeta:93-100],
  MP-3 (measurement void) [zeta:108-112], γ×δ edges.jsonl empty [zeta:51],
  α×γ health.md counters frozen [zeta:45]
- gamma-wiki-v3.md: health.md counter status [gamma:64], D10 skeleton
  [gamma:64], PostToolUse hook gap [gamma:227-233], α-4 mover gap
  [gamma:235-240]
- alpha-agent-construction-corpus.md: compound-step auto-extract rule
  [alpha:72-73], F/ClaimScope/R self-report gap [alpha:51],
  zero cycles run [alpha:59]
