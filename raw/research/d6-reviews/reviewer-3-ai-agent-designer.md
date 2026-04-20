---
id: reviewer-3-ai-agent-designer
title: Reviewer 3 — AI-Agent Designer Critique of D6 JETIX-FPF v1
date: 2026-04-20
stage: B3 (reviewer)
reviewer-lens: AI-Agent Designer
reviewer: claude-opus-4-7 (fresh session, extended thinking max)
target: design/JETIX-FPF.md v1 (commit 2a41927, 2599 lines)
scope: operational readiness for 11 Claude-agent roster + 5 Ruslan sub-roles
formality: F2
reliability: R-medium
claim-scope: jetix/stage-B3/ai-agent-design-review
---

# Reviewer 3 — AI-Agent Designer Critique

## Executive summary

**AI-agent-readiness verdict: CONDITIONAL-PASS (with 5 P1 blockers + 7 P2
gaps).** D6 is ontologically strong and agent-aspirational, but **as-delivered
it is not yet actionable by the 11 Claude-agents** without companion artifacts
(executor-binding.yaml schema, agency-chr.yaml schema, agent_onboarding
full example, runtime enforcement plan for IP-9 + J-level matrix). An agent
instance booting today cannot answer "what am I authorized to decide?" and
"what triggers escalation?" purely from D6 text. The document is a **primary
reference (correct role per §Preamble)** but requires 5 bridging policy
docs that D6 itself only references, not provides.

### Top 3 strengths (AI-agent lens)

1. **Role ≠ Executor strict separation (IP-1, §5.1)** — cleanly enforces
   agent holder/role swap discipline; solves Haiku-5.x upgrade-without-
   re-architecting problem. Quoted: *"Holder (agent instance) может change
   (Claude Haiku 4.5 → Haiku 5.x upgrade) — role remains stable"* (§2.2).
2. **Past-participle state machines + Hook 4 (IP-5, §5.5)** — binary, machine-
   verifiable reasoning surface. `IF Client.state == "qualified" THEN ...`
   is unambiguous for LLM reasoning. Eliminates Jira-style gerund ambiguity
   that silently bifurcates agent inference paths.
3. **Nested Holonic Structure with A.14 typed edges (§3.5)** — gives agents
   a principled answer to "which relation is this?" — `ComponentOf` vs
   `MemberOf` vs `PhaseOf` disambiguates what a bare Jira parent-link never
   could. FPF-Steward Q-audit (§5.4) promises to keep edges honest.

### Top 5 concerns (P1 blockers for Phase 1 Day-1 agent execution)

1. **OT5 Full-FPF-Permeation economics unexamined** (FP1) — D6 7-10K tokens
   × 11 agents × ~50 invocations/day × §11 Haiku vs Sonnet vs Opus cost
   differential = **daily Phase 1 burn rate uncomputed**. D6 Section 1.5
   commits to "full 7-10K tokens" in every agent's system.md without
   per-model cost model.
2. **J-level matrix is 1-dimensional, not agent × decision-category × J**
   (FP4) — §2.2 Table maps each agent to one J-level. Real operations
   require 3-dimensional matrix. Today an agent reading D6 cannot answer
   "is opening a hypothesis J-Auto or J-Approve for me?".
3. **Dynamic role-switching prevention has no runtime enforcer** (FP5) —
   §5.9 states the rule but §14.4 lists no Hook that enforces it, no
   manager-agent monitoring pattern, no pre-commit check. Rule without
   enforcement = not a constraint.
4. **Agency-CHR (A.13:4.3, Rec-08) has no schema/location** (FP10) —
   §2.1 mentions `default 1.0 founder / 0.4 agents`, but **no YAML schema,
   no storage path decided**, and D6 §14.4 mentions 3 possible locations
   (executor-binding.yaml field, agent-promotion-chr.yaml, separate
   agency-chr.yaml). Agent cannot populate what is not specified.
5. **Agent_onboarding has no concrete example** (FP3) — §5.8 gives a 3-line
   bullet list (`initial_context_pack`, `warm_up_tasks`,
   `calibration_checkpoint`). Zero filled-in example executor-binding.yaml
   for e.g. sales-lead Day-1. D3 is not yet written. Agent-implementer
   blocked.

### Reality-check: current repo state (ground-truth gap)

I verified against filesystem state `2026-04-20`:

- **`executors/` directory does NOT exist.** D6 §2.1 references
  `executors/ruslan.yaml` with `multi-role-binding: true`. Not there.
- **`decisions/policy/` directory does NOT exist.** D6 cites 10 policy
  docs (§14.4) — none exist.
- **`decisions/fpf-stewardship/` does NOT exist.** D6 §5.4 + Rec-22 require
  `decisions/fpf-stewardship/YYYY-QN-ontology-audit.md` — blank slate.
- **Current `agents/*/system.md` files are 50-100 lines.** Loading 2599-line
  D6 = **30× inflation** per agent. No migration plan stated.
- **`agents/strategist/` exists; D6 calls it `strategy-support-analyst`** (§2.2).
  **Name mismatch** — agent routing would break on Day 1.
- **`agents/life-coach/` still exists;** D6 §1.3 decrees it "migrated к
  Life-OS (per Chunk 6 Area 7)". D6 is inconsistent with repo.
- **`shared/schemas/message.schema.json` enum** lists 13 agents including
  `sales-researcher`. D6 §2.2 lists `sales-research` (no trailing `-er`).
  **Inter-agent messages would fail schema validation.**

These five ground-truth gaps between D6 prescription and repo state indicate
D6 was written ahead of the operational substrate. Normal for a constitutional
document — but agent-readiness is **conditional on Day 5-14 rollout**
delivering the missing scaffolding.

---

## Section 1 — Full-FPF-Permeation effectiveness (FP1)

**D6 commitment (§1.5):**
> *"JETIX-FPF full-text loaded в каждый agent system.md (OT5 Scenario A,
> full 7-10K tokens)"*

And §Preamble: *"D6 — primary reference для всех 18 role-manifests. Агенты
загружают полный текст D6 в system.md (OT5 Scenario A — full-text везде)."*

**Measurement.** D6 is 2599 lines. Measuring via `wc -w` proxy: ~30-45 pages,
~7-10K tokens (confirmed via FP1 framing). Plus per-agent overhead:
- role.md (5-block, D3 target ~200-400 lines each) ≈ 1-2K tokens
- scratchpad.md ≈ 0-2K tokens
- niche/ symlinks to wiki/niches/ ≈ 2-5K tokens depending on niche
- per-task context-pack ≈ 5-20K tokens

**Per-invocation load estimate: 15-40K tokens before task input.**

### 1.1 Per-model verdicts

**Haiku 4.5 (200K ctx, priced ~$1/$5 per M tokens in/out):**
- D6 load = 5-7K tokens = 3-4% of context. Fits easily.
- Cost per invocation: ~$0.01-0.04 for D6 portion alone (input).
- **BUT**: 5 Haiku agents (personal-assistant, system-admin, sales-research,
  sales-outreach, inbox-processor) at high frequency — inbox-processor e.g.
  processes every voice note. If 100 invocations/day × 5 agents × $0.03 =
  **~$15/day just for D6 loading**, independent of work.
- **Verdict: OK technically, wasteful operationally.** Haiku agents do
  narrow work that doesn't need full D6. `inbox-processor` classifying a
  voice note does not need A.14 mereology edges. **Recommend: distilled-
  essence (500-1000 token summary) for Haiku agents, not full-text.**

**Sonnet 4.6 (200K ctx, priced ~$3/$15 per M tokens):**
- D6 load = 3-4% of context. Fits.
- Cost: ~$0.03-0.12 per invocation for D6 portion.
- 6 Sonnet agents (manager, sales-lead, crazy-agent, knowledge-synth, meta-
  agent, life-coach-if-retained). Manager invocations ~30-50/day (morning
  + evening pipeline + routing). If 40/day × 6 Sonnet × $0.10 =
  **~$24/day for D6 loading**.
- **Verdict: OK at Phase 1 scale but inspect monthly.** Sonnet agents
  benefit from D6 more (coordination, synthesis). Keep full-text; add
  **caching discipline** — load D6 once per session, not per turn.

**Opus 4.6/4.7 (1M ctx, priced ~$15/$75 per M tokens):**
- D6 load = 1% of context.
- Cost: ~$0.15-0.75 per invocation just for D6 portion.
- Only `strategy-support-analyst` uses Opus. Invocation count — TBD; see
  FP11 below. If 2-5/day × $0.50 avg = **~$1-3/day Opus D6 loading**.
- **Verdict: OK economically (Opus invocations rare) but verify cost model.**

### 1.2 Aggregate burn estimate

Back-of-envelope Phase 1 daily D6-loading cost: **$40-60/day = €1100-1650/mo
before any useful work**. This is **3-8% of €50K Q2 revenue target**
consumed by ontology-permeation overhead alone.

D6 §1.5 does not model this. P7 Compute budget (per decisions) should
absorb it, but D6 provides no explicit figure.

### 1.3 Alternatives agent-implementer should consider

1. **Tiered loading:**
   - **Full-text** (OT5 Scenario A): manager, knowledge-synth, meta-agent,
     FPF-Steward, strategy-support-analyst — these *use* the ontology.
   - **Distilled-essence (500-1000 tokens)**: sales agents, inbox-processor,
     personal-assistant, system-admin — these *execute* narrow tasks.
   - **Reference-only-with-on-demand-section-fetch**: life-coach (if
     retained), sales-outreach — agents that rarely reason over methodology.
2. **Section-indexed fetching:** load D6 Table-of-Contents + Section-to-
   filename map as default; fetch specific sections when task triggers.
   Costs ~300 tokens baseline + targeted section pulls.
3. **Prompt caching:** Anthropic prompt-cache TTL 5min. All agents share
   identical D6 preamble → **single cache entry amortizes**. If manager
   invokes 40×/day and each hits cache, D6 input cost drops ~90%.

### 1.4 D6 agent-implementation recommendation

Add **Section 1.5.1 "Per-agent loading tier"** to D6 with 3-column table
(agent / tier / rationale). This is the single highest-leverage D6 change
for agent-operational cost discipline. Without it, OT5 Scenario A is a
principle without an implementation plan.

---

## Section 2 — Agent onboarding patterns (FP3, Rec-15)

**D6 §5.8 IP-8 text** (full quote):
> *"executor-binding.yaml получает agent_onboarding section с:
>   - initial_context_pack (wiki refs, role ref, alpha refs).
>   - warm_up_tasks (calibration tasks, trivial success criteria).
>   - calibration_checkpoint (meta-agent reviews output quality).
>   - F.6 6-step cycle retrospective (30/90/180-day)."*

**That is it.** Four bullet points. No field types. No example. No path.

### 2.1 F.6 6-step mapping test

F.6 defines M1 Locate → M2 Stance → M3 Qualify → M4 Bind/Assert → M5
Evidence → M6 Conclude (per FPF-Spec §F.6:6). D6 §5.8 mentions the cycle
but **does not map each step to an executor-binding.yaml field or onboarding
activity**. For example:

- **M1 Locate** = which `U.BoundedContext` does this role-assignment live in?
  → should be `context: jetix/sales/dach-mittelstand` field.
- **M2 Stance** = design vs run stance → `stance: run` field? Missing.
- **M3 Qualify** = Holder eligibility check → Who runs it?
  meta-agent? Missing.
- **M4 Bind/Assert** = the assignment itself → which artifact `Window W` is
  stamped on? Missing.
- **M5 Evidence** = Σ(Context) evidence shape → Does the warm-up task
  define this? Not specified.
- **M6 Conclude** = confidence γ ∈ [0,1] threshold for promotion → Missing.

**Verdict: D6 cites F.6 but does not operationalize it.** Rec-15 approved
full adoption (per gap-analysis-2026-04-20 Step 4), but D6 is the document
where the operationalization belongs — it is the "constitutional" doc.

### 2.2 Concrete example D6 should include

D6 Section 5.8 needs an **Annex 1: sales-lead Day-1 onboarding example**:

```yaml
# executors/sales-lead/executor-binding-v1.yaml
holder:
  kind: claude-agent
  model: claude-sonnet-4-6
  instance_id: sales-lead-claude-sonnet-4-6-v1
role_ref: roles/sales-lead/role.md
context: jetix/l4-revenue/dach-mittelstand
stance: run  # F.6 M2
window:
  start: 2026-04-25
  end: open
agency_profile:           # Rec-08 A.13:4.3
  default: 0.4
  overrides:
    - decision_class: outbound-email-draft
      value: 0.7
    - decision_class: discount-above-10-pct
      value: 0.0  # must escalate
  bmc: 0.6  # Boundary Maintenance Capacity estimate
  ph: 0.4   # Predictive Horizon (1-2 day window)
  mp: 0.2   # Model Plasticity (fixed Sonnet weights)
  per: 0.7  # Policy Enactment Reliability
  oc: 0.5   # Objective Complexity
  agency_grade: 2  # didactic summary
  evidence_ref: decisions/fpf-stewardship/2026-Q2-agency-chr-bootstrap.md
agent_onboarding:
  initial_context_pack:
    - design/JETIX-FPF.md                    # D6 full (Sonnet tier)
    - roles/sales-lead/role.md
    - alphas/client/*.yaml
    - alphas/deal/*.yaml
    - directions/_active/ai-consulting-dach/direction.md
    - wiki/niches/sales/_moc.md
  warm_up_tasks:
    - id: wu-01
      description: Classify 3 mock leads via MECE → qualified/unqualified
      success_criteria:
        - each decision has L/A/D/E line
        - each state uses past-participle
        - evidence shape Σ stated
    - id: wu-02
      description: Draft proposal from template с A.6.B lanes, no executor details
      success_criteria:
        - L section cites ≥1 DACH-legal source
        - E section has SLA metric
  calibration_checkpoint:
    reviewer: meta-agent (FPF-Steward sub-role)
    at_n_tasks: 5
    pass_threshold:
      past_participle_violation_rate: 0
      role_executor_conflation_count: 0
      f_g_r_missing_rate: < 0.1
  retrospective:
    intervals_days: [30, 90, 180]
    format: decisions/fpf-stewardship/YYYY-MM-DD-<agent>-retro.md
    items:
      - warm_up_to_live_drift
      - agency_chr_re_measurement
      - method_description_updates
```

**Without this annex, D3 writers and future agent-implementers will each
invent their own fields** → terminology drift at the first use (P-6 Lexical
Stratification violation). **P1 blocker.**

### 2.3 Who drives onboarding?

D6 §5.8 says "meta-agent reviews output quality". But **meta-agent's
system.md today (verified) does not contain onboarding review responsibility**.
FPF-Steward sub-role (§5.4) scope is quarterly audit, not per-agent
onboarding. **Gap: the "onboarder role" is not assigned** to any specific
actor in D6 §2.2's 11-agent table.

Recommended: **Add to meta-agent role.md Block 5 (Evolution)**:
`autonomous: [calibration-checkpoint-review, retrospective-aggregation]`.

---

## Section 3 — FPF-Steward sub-role (R12, FP2)

**D6 §5.4 scope list:**

12 audit items (Alpha/WP/Entity classification; past-participle; concept
duplication; role-manifest integrity; direction-concept boundary;
frontmatter schema; UTS review; F-G-R compliance; A.14 edge-type
verification; CHR space integrity; Viewpoint Bundle correspondences;
semi-annual FPF upstream sync).

**Separation trigger:** *"30+ agents OR 1+ human meta-hire OR quarterly
audit burden >4h"* (§5.4).

### 3.1 Realism check

Ruslan's Q2 budget: 4h per quarter for FPF-Steward. 12 scope items in 4
hours = **20 min per item**. Each item requires:

- **Past-participle scan** of all `state.yaml` files (automated by Hook 4 —
  if implemented; see §7 below) — 5 min if Hook 4 exists, 60 min if manual.
- **Concept duplication detection** across wiki/ (grep + manual review of
  top-10 suspicious clusters) — 30 min minimum, realistic.
- **UTS review** (30-50 rows × re-check Bridges, CL, SenseCells) — 45 min
  minimum for serious review. Already over budget.
- **F-G-R compliance check** across all ADRs + deliverables Q2 — if 20-30
  ADRs, 2-min each = 60 min.

**Realistic Q2 audit burden: 6-8 hours, not 4.** Separation trigger hits
almost immediately → FPF-Steward should separate at end of Q2, not
"Phase 2b".

### 3.2 Trigger-driven mode absent

FP2 asks: should FPF-Steward have **trigger-driven mode** mirroring §7.2
strategizing trigger-driven-not-scheduled principle?

**Yes — but D6 does not say so.** Triggers for FPF-Steward ad-hoc audit:
- Hook 4 fires >N false-positives in a week → edge-type rule needs revision.
- ADR mentions new U-Type not in UTS → UTS sync needed.
- Client deliverable bounces back due to Viewpoint inconsistency → MVPK
  correspondences need audit.

**Recommendation:** D6 §5.4 add subsection "Trigger-driven ad-hoc audits"
mirroring §7.2 pattern. Otherwise FPF-Steward backlog accumulates silently
between Q-cycles.

### 3.3 Bias-Audit Cycle integration

D6 §12.10 lists Jetix bias-audit Phase 1 as BA-0/BA-1/BA-3 (no BA-2 Panel).
**Where does bias-audit live in FPF-Steward scope?** Not listed in §5.4's
12 items. §12.10 says "D.5 integration" but doesn't resolve ownership.
The agent reading D6 today cannot answer: *"when I close a client audit
with bias-register.yaml, does FPF-Steward audit it quarterly, or does it
live in a separate pipeline?"*

**Recommendation:** Add item 13 to §5.4: *"Bias-audit register aggregate
review (quarterly roll-up across client deliverables)"*.

### 3.4 Drift detection mechanisms

D6 §5.4 mentions "concept duplication detection" but not **how** — grep?
embedding-similarity? human review? The meta-agent (Sonnet 4.6) has no
embedding tooling. Without concrete mechanism, drift detection = manual
reading. For 100+ wiki pages that is **hours, not minutes**.

**Recommendation:** D6 annex concrete tool list: `tools/wiki-dedup.py`,
`tools/past-participle-lint.py`, `tools/uts-drift-check.py`. Without them,
§5.4 is aspirational.

---

## Section 4 — Agency-CHR operational (A.13:4.3, Rec-08, FP10)

**D6 §2.1 commitment:**
> *"Agency profile (per Rec-08 A.13:4.3 Agency-CHR fallback): Ruslan
> default agency 1.0 (founder full-stack); agents default 0.4 with override
> per decision class."*

**D6 §14.4 mentions:** `decisions/policy/agent-promotion-chr.yaml`.

### 4.1 Storage-location ambiguity

Possible locations (inferred from D6):
- A. `agents/<id>/agency-chr.yaml` (not mentioned in D6)
- B. Field inside `executor-binding.yaml` (consistent with §2.2 "per-binding")
- C. Separate `decisions/policy/agent-promotion-chr.yaml` (§14.4)
- D. Hybrid: static defaults in (C), per-binding overrides in (B)

**D6 says nothing.** Agent-implementer must guess.

**Recommendation: Option D.**
- `decisions/policy/agent-promotion-chr.yaml` = default matrix per role
  (e.g., all sales-researcher agents default BMC=0.5, PH=0.2).
- `executors/<id>/executor-binding.yaml` has `agency_profile:` block
  overriding defaults per-holder.

### 4.2 Schema example (missing from D6, proposed)

```yaml
# decisions/policy/agent-promotion-chr.yaml (default CHR by role)
version: v1
default_by_role:
  sales-lead:
    bmc: 0.6
    ph:  0.5
    mp:  0.3
    per: 0.7
    oc:  0.5
    agency_grade: 2
    evidence_ref: null  # must be populated before J-Approve claim
  manager:
    bmc: 0.7; ph: 0.4; mp: 0.2; per: 0.8; oc: 0.4
    agency_grade: 2
  strategy-support-analyst:
    bmc: 0.5; ph: 0.7; mp: 0.1; per: 0.6; oc: 0.8
    agency_grade: 3  # per A.13 A.13:4.4 "Adaptive"
promotion_rules:
  promote_to_j_strategic:
    ruling: "never for AI agents (hard rule per §5.10.4)"
    exception: "Ruslan only"
  promote_to_j_approve:
    threshold:
      bmc: ">= 0.5"
      per: ">= 0.6"
      evidence_tasks_passed: ">= 10"
```

**D6 should include this in §2.1 or Annex** — 30 lines of YAML that unblock
3 agents (sales-lead, manager, strategy-support-analyst) from Day 1.

### 4.3 Per-decision-category override mechanism

D6 §2.1 says *"override per decision class"* but lists **zero decision
classes**. An agent reading D6 cannot enumerate what decision-classes
exist. FP4 (see Section 9 below) expands on the same gap.

### 4.4 Context-dependent agency shifts

FPF A.13:4.3.1 talks about *"context-bounded task-family specialization"* —
an agent may have Agency-CHR = X in task-family A and Y in task-family B.
**D6 does not surface this.** Agents will default to single global profile
→ wrong when e.g. sales-lead is highly reliable for "discovery calls" but
low-reliability for "German-language contract negotiation".

**Recommendation:** D6 §2.1 add note: *"Agency-CHR is per-task-family, not
per-agent-global. See schema template for per-task-family overrides."*

### 4.5 CC-A13.3 (CHR Evidence) compliance

FPF CC-A13.3: *"Any claim about an Agent's grade or level of autonomy MUST
be substantiated by an auditable Agency-CHR profile with Evidence Graph
Ref (A.10)."*

**D6 §2.1 declares default `0.4` without evidence_ref.** Strictly this
violates CC-A13.3. Acceptable at Phase 1 Day-1 bootstrap if flagged as
`R-low, evidence_ref: pending`, but **D6 does not flag it**. FPF-Steward
will raise this in Q2 audit. Pre-emptive fix in D6: add footnote to §2.1.

---

## Section 5 — Role ≠ Executor separation (IP-1, §5.1 + §5.6 + §5.9)

**Strongest section of D6.** P2 (Role ≠ Executor strict) is clean, well-
grounded (A.2.1 U.RoleAssignment), and the 5-block role.md is a usable
template for agent self-reference.

### 5.1 role.md purity check

D6 §5.6 Block 3 template:
```yaml
primary_method: value-based-pricing-mece-qualification
method_description_ref: wiki/methodologies/mece-sales.md
deliverable_kinds: [Client-in-Negotiated-state, Deal-in-Signed-state]
state_graph_ref: alphas/deal/states.yaml
```

**✅ No executor details** (no model name, no Anthropic API config, no
instance ID). Clean separation.

**Minor concern:** `deliverable_kinds: [Client-in-Negotiated-state, ...]` uses
hyphenated past-participle cleverly, but "Negotiated" vs "in-Negotiated"
vs "In-Negotiation" wouldn't an agent reading D6 §5.5 table infer this?
No — table shows `qualified`, `in-negotiation`, `won`. D6 §6.2 Client state
machine uses `in-negotiation` (gerund-ish!). **Self-inconsistency.**
Past-participle of "negotiate" = "negotiated". The state should be
`negotiated` not `in-negotiation`. Hook 4 would fire on D6 itself.

→ **P2 bug in D6: Client.state "in-negotiation" violates own IP-5 rule.**
(see §7 below for full Hook 4 feasibility analysis).

### 5.2 executor-binding.yaml completeness

D6 does **not** define the executor-binding.yaml schema in a single place.
Pieces scattered:
- §2.2: "executor-binding.yaml bound to defined role.md"
- §2.1: "executors/ruslan.yaml с multi-role-binding: true"
- §5.8: "agent_onboarding section"
- §14.4: "`decisions/policy/agent-promotion-chr.yaml`" (adjacent)

**No canonical schema definition.** D6 should include in §5.1 or §14.4 a
full `executor-binding.yaml` schema with all fields (holder / role_ref /
context / stance / window / agency_profile / agent_onboarding /
compute_contract / mailbox_address / …). Without it, 11 agents × N humans
= N+11 different bindings.

### 5.3 5-block role.md usable for agent self-reference?

**Test:** can sales-lead agent, reading its own role.md + D6 as system.md,
answer "what am I allowed to decide today?"

- Block 5 "Evolution" gives `autonomous: [draft-proposal, schedule-call,
  send-DPA]` + `approve_required: [discount-offer-above-10%]` +
  `never: [sign-contract]`. ✅ Sufficient for common ops.
- BUT what about decisions **not listed** in any category? E.g., "Should I
  add a new prospect to CRM without pre-qualification?" D6 §5.6 template
  has no **default rule for unlisted actions**. Agent defaults to...?

**Recommendation:** D6 §5.6 Block 5 add field
`default_for_unlisted: escalate-to-approve` (conservative) or `autonomous`
(permissive). Without it, agent behavior is undefined at edge cases.

### 5.4 Dynamic role-switching prevention (§5.9, FP5)

**Rule:** *"Agent cannot dynamically switch role during task execution."*
**Founder exception:** Ruslan `multi-role-binding: true`.

**But who enforces it at runtime?**

- **Pre-commit hook on what artifact?** Role switch is not a git event — it is
  an in-session agent decision. Hook cannot catch it.
- **Manager agent monitoring mailbox?** Manager would have to detect e.g.
  a message from sales-lead containing "I'll also draft the contract
  (normally sales-closer role)". Requires NLP pattern on every message.
- **Ruslan manual review?** 500+ agent messages/day. Not scalable.

**Verdict: FP5 stands. §5.9 is an unenforced rule.**

**Recommendation options:**

1. **Role-tagged mailbox protocol.** Every agent message carries
   `acting_as: <role-id>` field. If message's acting_as does not match
   executor-binding.yaml's role_ref → flagged. Add to `shared/schemas/
   message.schema.json` (currently has no such field).
2. **Meta-agent periodic scan** over mailbox deltas, looking for role-
   switch patterns. Delegates detection to LLM, costs tokens.
3. **Accept as soft rule + FPF-Steward quarterly review.**

Option 1 is cheap and mechanistic. **Recommend adding to D6 §5.9 as the
canonical enforcement pattern**, plus update `message.schema.json`.

---

## Section 6 — Context management (Левенчук Part 3 #1)

**D6 Preamble and §1.5 do not explicitly state the 25K exocortex
reservation.** This is the Левенчук Part 3 #1 specification — it is
mentioned in §14.3 D5 cross-ref *"25K exocortex reservation"* — but **not
elaborated in D6 §1.5 operational architecture**.

### 6.1 25K exocortex "hard" reservation

Interpretation: per agent, 25K of context window is reserved for exocortex
(accessible KB, wiki/, role-manifests). Additional 25K soft budget for
task-specific context. Total 50K commitment.

**D6 silence on this creates ambiguity.** Haiku agent with 200K ctx — is 25K
reserved for exocortex or for wiki/niches/ subset or for D6 itself? If D6
is already 10K, does it count against 25K exocortex?

**Recommendation:** D6 add §1.5a "Per-agent context budget":

| Layer | Budget | Content |
|-------|--------|---------|
| System preamble | 1K | role.md Blocks 1-2 |
| D6 full-text (OT5) | 10K | This document |
| Exocortex hard | 25K | Accessible wiki/ slices via niche/ |
| Task context soft | 25K | per-task KB-pulls, prior messages |
| Working | ~20K | reasoning + output |
| **Total** | **~80K of 200K** | ~40% ctx floor |

Without this budget table, agents can't plan retrieval strategy.

### 6.2 Agent-accessible Context loading

Current `agents/<id>/niche/` symlinks to `wiki/niches/<slug>/`. D6 §1.5
mentions this pattern but does not define how agent instantiates it at
session start. Claude Code subagents inherit tool config from system.md
frontmatter; they do **not** auto-load a directory tree. Agent has to
explicitly Read each file.

**Recommendation:** D6 add note: *"Session startup sequence: Read
role.md → Read D6 (Section 1-14) → glob niche/ + Read index.md → proceed
to task."* This is what Haiku agent actually has to do; D6 should say so.

---

## Section 7 — Past-participle state machines (IP-5, Hook 4, FP8)

Strongest single agent-operational feature of D6. Machine-verifiable states
are exactly what LLM reasoning needs — no ambiguity between "in-progress"
and "started" to resolve on every inference.

### 7.1 Agent reasoning quality with past-participle

`IF Client.state == "qualified"` is unambiguous for an LLM. Eliminates a
class of hallucinations (agent reading "qualifying" and inferring *state*
vs *activity* incorrectly). **Large win.**

### 7.2 Hook 4 implementation feasibility (FP8)

**English past-participle:** regex heuristic:
- Block: `-ing$` endings in `state:` YAML values.
- Allow: explicit whitelist of known past-participles (qualified, closed,
  delivered, archived, …).
- Edge cases: `ongoing` (whitelisted legacy? no, block). `in-progress`
  (should block and remap to `started`).

**Russian (FP8):**
- Russian has no gerund per se. Agent ambiguity: *"квалифицируется"* =
  reflexive present-tense, not state. *"квалифицирован"* = краткое причастие
  = past-participle. **Correct target.**
- Regex for краткое причастие: endings `-ан/-ена/-ено/-аны` (e.g.
  квалифицирован, активирована, закрыто, доставлены).
- False negatives: verbs not matching pattern (e.g. *"перевед-ён"* →
  "переведён"). Regex alone will miss.

**Recommended hybrid:**

1. **Regex pass** — fast, catches 80%.
2. **Small whitelist + blacklist** in `decisions/policy/past-participle-
   dictionary.yaml` (~50 Russian verbs × 3 forms, ~50 English).
3. **Human escalation** for non-matching states → Ruslan 1-click approve
   or reject.
4. **NLP POS-tagger** (e.g. `pymorphy3` for Russian, spaCy en-core-web-sm)
   as optional deeper check — adds 2-3 sec to hook latency.

**D6 §5.5 does not specify implementation.** Hook 4 is referenced 5+ times
but left for D8 (Instructions) to implement. At minimum D6 should pin the
language-coverage commitment (RU + EN) and punt only on tool choice.

### 7.3 D6 self-violation (discovered in §5 above)

D6 §6.2 Client state machine: `lead-identified → qualified → proposed →
in-negotiation → won/lost → churned`.

**"in-negotiation" is NOT past-participle.** Past-participle of "negotiate"
is "negotiated". D6 violates its own IP-5.

Hook 4 (if implemented) would flag D6 itself. **P2 bug.**

### 7.4 Russian state machine alignment

D6 §5.5 gives Russian: *"квалифицирован", "активирован", "начат",
"доставлен", "закрыт"*. But §6.2 state tables are English only. There is
no Russian mirror table.

**Recommendation:** D6 §6.2 add Russian column next to each state. Enables
Russian-language ADR writing + client-facing deliverables without translation
drift.

---

## Section 8 — Multi-agent coordination (FP6)

**D6 does NOT include multi-agent communication protocols.** §2.2 lists
agents + J-level; §5.6 Block 4 uses `depends_on_roles: [sales-lead,
sales-research]`. That is the full extent.

### 8.1 What is missing

For an AI-agent-ready design, agents need:
1. **Mailbox protocol / schema** — D6 does not reference
   `shared/schemas/message.schema.json` or specify which `type:` enum
   values agents are expected to send.
2. **Addressing conventions** — "hub-and-spoke: subagents report to Dept
   Lead, not Manager" is in `CLAUDE.md` but **not in D6**. Should be
   constitutional.
3. **Escalation paths** — when sales-lead cannot decide, escalate to
   Manager? Strategist? Ruslan? `comms/escalation.jsonl` is used today
   but undocumented in D6.
4. **Inter-agent dependency resolution** — sales-lead depends_on
   sales-research. What if sales-research mailbox is backed up 3 days?
   Does sales-lead block (synchronous) or proceed with stale data
   (eventually-consistent)?

### 8.2 Is this properly relegated to D8?

FP6 asks: D6 or D8 (Instructions)?

**Answer: high-level coordination principles belong in D6 (constitutional),
implementation in D8.** D6 §2.2 should add subsection "§2.2a Coordination
principles":

- **Hub-and-spoke discipline** (CLAUDE.md rule #8): subagents → Dept Lead
  → Manager. No skip-level unless escalation.
- **Message schema reference** to `shared/schemas/message.schema.json`.
- **Escalation taxonomy** (dept-internal / cross-dept / strategic / safety).
- **Async default; sync only for named synchronous points** (e.g., proposal-
  signing).
- **Stale-dependency timeout** (e.g., if `depends_on_roles` not responding
  in 48h, agent emits `escalation` type message).

This is ~200-400 words and unblocks Phase 1 operational Day 1.

### 8.3 Ground-truth verification

**Current schema enum includes `sales-researcher` but D6 uses
`sales-research`.** If D6 is authoritative, schema must update. If schema
is authoritative, D6 must fix. **No stated resolution.** Day 1 inter-agent
messages will fail validation.

**Recommendation:** D6 §2.2 footnote: *"Canonical agent IDs match
`shared/schemas/message.schema.json` from field enum."* Then reconcile
the D6 table to the schema (or vice versa, updating schema).

---

## Section 9 — Decision authority per J-level (FP4, FP7)

**D6 §2.2 Table column "J-level"** assigns each agent **one** J-level.
This is the single most operationally consequential defect.

### 9.1 Why 1D mapping is insufficient

`manager → J-Approve` makes sense for cross-dept task routing. But manager
also:
- Routes inbox items (trivial: should be J-Auto).
- Decides compute budget allocation (strategic: J-Strategic).

**Real operational matrix is agent × decision-category × J-level.** D6 §2.2
offers no such matrix.

### 9.2 Concrete example construction

For sales-lead (D6 §2.2: J-Approve globally), realistic breakdown:

| Decision category | J-level | Rationale |
|-------------------|---------|-----------|
| Draft proposal | J-Auto | Template-governed, L/A/D/E enforced |
| Schedule call | J-Auto | Calendar action, reversible |
| Send DPA | J-Auto (FIRST send: J-Approve) | Low risk after template validated |
| Discount 0-10% | J-Approve | Revenue-relevant |
| Discount >10% | J-Strategic | Pricing integrity |
| Custom terms | J-Strategic | Precedent-setting |
| Sign contract | J-Strategic | Founder only |
| Withdraw from deal | J-Strategic | Strategic signal |

**8 decision-categories for one agent.** Across 11 agents × ~5-8 categories
= **50-90 cells**. D6 assigns 11. **~80% under-specified.**

### 9.3 D7 Career Levels — can D6 delegate?

FP4 asks: is the full matrix OK to delegate to D7?

**Partial delegation acceptable if D6 names the dimensions.**
D6 §2.2 should say:
> *"Each agent's role.md Block 5 MUST enumerate decision-categories with
> per-category J-level. D6 Table §2.2 shows default global bucket; per-
> role overrides in D3 role.md. D7 Career Levels defines promotion-path
> transitions across J-levels."*

Without this bridging sentence, D7 writers won't know the matrix is their
responsibility. Current D6 text reads as if §2.2 is the complete J-level
specification.

### 9.4 Section 6.3.8 Direction authority + 12.8 CSLC flow (FP7)

**D6 §6.3.8:**
- Open hypothesis direction: J-Auto (strategy-support-analyst may propose)
- Activate direction: J-Strategic (Ruslan only)
- Archive direction: J-Strategic (Ruslan only, с post-mortem)

**D6 §12.8 CSLC:** SKU pricing CHR + direction kill CHR + agent promotion
CHR (all Gap 3 adoptions).

**Missing: the end-to-end operational flow.** Agent reading D6 asks: "I'm
strategy-support-analyst. I see a pattern that `ai-consulting-dach` might
be underperforming. What's the sequence?"

D6 needs **§7.2a Direction-level CSLC flow**:

1. strategy-support-analyst detects kill-CHR threshold breach (CSLC
   measurement).
2. Writes abductive prompt artifact (B.5.2.0) to `decisions/strategy/
   YYYY-MM-DD-direction-underperformance-<slug>.md`.
3. Emits `escalation` type message to manager + Ruslan.
4. Meta-agent reviews FPF compliance (ontology integrity of artifact).
5. Ruslan reads → strategizing event triggered (§7.2 trigger-driven).
6. DRR write-up (§12.14).
7. state.yaml transition (e.g. `activated` → `plateaued` or `dropped`).

**6 steps — none explicit in D6.** FP7 verdict stands: gap, and not
cleanly relegatable because the flow touches 4 roles (strategy-support,
meta-agent, Ruslan, manager). D7+D8 cannot invent it; D6 must specify
cross-role sequence.

---

## Section 10 — Critical AI-agent findings (P1/P2/P3)

### 10.1 P1 — must-fix before agent-implementer starts D3

| # | Finding | Location | Fix |
|---|---------|----------|-----|
| **P1-1** | OT5 per-model cost model absent | §1.5 | Add tiered-loading table (full / distilled / reference) per agent |
| **P1-2** | J-level matrix 1D | §2.2 | Add agent × decision-category × J explicit (or dim-naming sentence punting to D3 Block 5 + D7) |
| **P1-3** | Agency-CHR schema + location undecided | §2.1, §14.4 | Add schema block + storage path (recommended: `decisions/policy/agent-promotion-chr.yaml` + override in executor-binding.yaml) |
| **P1-4** | agent_onboarding no example | §5.8 | Add full sales-lead Day-1 executor-binding example (~50 lines YAML) |
| **P1-5** | Dynamic role-switching unenforced | §5.9 | Add `acting_as:` field to message.schema.json + reference in D6 |
| **P1-6** | Multi-agent coordination missing from D6 | §2.2 | Add §2.2a Coordination principles (hub-and-spoke, message-schema ref, escalation, stale-dep timeout) |
| **P1-7** | Ground-truth drift (life-coach exists; strategist vs strategy-support-analyst; sales-researcher vs sales-research) | §2.2 | Reconcile names + update `message.schema.json` enum |

### 10.2 P2 — should-fix before Phase 1 Day 14

| # | Finding | Location | Fix |
|---|---------|----------|-----|
| **P2-1** | D6 §6.2 Client state "in-negotiation" violates own IP-5 | §5.5 vs §6.2 | Rename to `negotiated` or `in-negotiation` documented whitelist exception |
| **P2-2** | FPF-Steward quarterly 4h budget unrealistic | §5.4 | Revise to 6-8h OR add trigger-driven mode |
| **P2-3** | Hook 4 RU/EN implementation strategy undefined | §5.5 | Hybrid regex + dictionary + POS-tag option in D6 or D8 annex |
| **P2-4** | Bias-audit ownership unassigned | §12.10 | Add to §5.4 FPF-Steward scope |
| **P2-5** | Context budget (25K exocortex) not in D6 | §1.5 | Add budget table |
| **P2-6** | Direction-level CSLC flow missing | §6.3.8 + §12.8 | Add §7.2a end-to-end flow |
| **P2-7** | Russian state-machine column missing | §6.2 | Add Russian past-participles alongside English |

### 10.3 P3 — nice-to-have

| # | Finding | Fix |
|---|---------|-----|
| **P3-1** | Agency-CHR per-task-family overrides unsurfaced | Note in §2.1 referring to A.13:4.3.1 |
| **P3-2** | CC-A13.3 evidence_ref pending at Phase 1 | Footnote in §2.1 acknowledging R-low bootstrap |
| **P3-3** | Concrete drift-detection tools unnamed | Annex tool list for FPF-Steward §5.4 |
| **P3-4** | `default_for_unlisted` rule in role.md Block 5 missing | Template update in §5.6 |
| **P3-5** | Cost model per-agent invocation absent | Add §P7 Compute table (or ref to D8) |

---

## Section 11 — Strengths to preserve

1. **Role ≠ Executor (IP-1, §5.1):** Core separation is clean and fully
   grounded (A.2.1 + Левенчук). Do **not** water down during D3 writing
   when pressure to short-circuit arises.
2. **Past-participle state-machines (IP-5, §5.5):** Highest-value agent-
   readability discipline. Keep the hard rule + extend Hook 4 across
   languages.
3. **Nested Holonic Structure + A.14 typed edges (§1.7 + §3.5):** Gives
   agents principled vocabulary for relations. `ComponentOf` vs
   `MemberOf` vs `PhaseOf` disambiguates at commit time.
4. **5-block role.md (§5.6):** Usable template. Identity / Ontological /
   Method / Dependencies / Evolution is a clean information-architecture
   for self-reference.
5. **FPF-Steward sub-role (§5.4):** Immune-system pattern is the right
   prophylactic. 12-item scope is ambitious; execution discipline will
   determine success.
6. **Self-reference of D6 as Way-of-Working alpha instance (§6.3.7):** D6
   is explicit that it is a WoW-alpha. Elegant — enables D6 itself to
   transition through `drafted → in-review → implemented` state, which
   Hook 4 can lint.
7. **Full-FPF-Permeation principle (OT5):** Correct target architecturally.
   Implementation economics need tiered loading, but the target (shared
   ontology across agents) is right. Without it agents drift.
8. **Trigger-driven strategizing (§7.2):** Hard rule against scheduled
   strategizing event. Prevents performance-ritual drift. Aligns with
   Левенчук §1.4 correctly.
9. **Attribution discipline (§14.9, §9.5 FPF ≠ JETIX-FPF):** Clean
   separation of canonical FPF vs Jetix adaptation. Prevents
   misrepresentation and enables future upstream-sync.

---

## Section 12 — Recommended changes for Stage C

### 12.1 Must-do (P1) before Stage C approval

D6 v1 → v1.1:

1. **§1.5 add §1.5.1 "Per-agent loading tier"** — 3-tier table.
2. **§2.1 add §2.1a "Agency-CHR schema + storage"** — YAML example +
   storage-path decision.
3. **§2.2 fix agent-ID mismatches** — reconcile with
   `message.schema.json`. Update the schema in same commit (coordinate).
4. **§2.2 add §2.2a "Coordination principles"** — hub-and-spoke, schema
   ref, escalation paths, stale-dep timeout.
5. **§5.8 add Annex A "sales-lead Day-1 onboarding example"** — full
   executor-binding.yaml (~50-80 lines).
6. **§5.9 add "Enforcement"** — `acting_as:` message field + meta-agent
   quarterly scan.
7. **§6.2 fix "in-negotiation"** → `negotiated` (or documented whitelist).
8. **§2.2 add J-level dimension sentence** punting matrix to D3 Block 5
   + D7.

### 12.2 Should-do (P2) during Stage C

9. **§1.5a context budget table.**
10. **§5.4 add trigger-driven mode + bias-audit scope item.**
11. **§5.5 Hook 4 hybrid-implementation spec (regex + dictionary + POS).**
12. **§7.2a direction-level CSLC operational flow** (6-step sequence).
13. **§6.2 Russian state-machine column.**

### 12.3 Nice-to-do (P3) at any time

14. **Annex B: FPF-Steward tool list.**
15. **§5.6 template add `default_for_unlisted`.**
16. **§2.1 footnote CC-A13.3 evidence_ref pending acknowledgment.**
17. **§2.1 note per-task-family Agency-CHR overrides per A.13:4.3.1.**

### 12.4 Stage C entry criteria for D6

From an AI-agent-designer lens, D6 is **Stage-C-ready when**:

- [ ] All P1 items resolved (items 1-8 above).
- [ ] Executor-binding.yaml canonical schema exists (can live in
      `shared/schemas/executor-binding.schema.json`) and D6 references
      it.
- [ ] `agents/<id>/system.md` migration plan documented (who replaces
      existing 50-100 line files with D6-derived preamble; cost impact
      of sudden 30× inflation; rollback).
- [ ] `shared/schemas/message.schema.json` updated to match D6 agent IDs
      + `acting_as:` field added.
- [ ] `decisions/policy/agent-promotion-chr.yaml` stub exists (can be
      `status: draft` initially).
- [ ] Hook 4 implementation plan in D8 or companion doc.

Without these six, agent-implementer for D3 will end up writing 11
different flavors of executor-binding → P-6 Lexical Stratification
violation at Phase 1 Day 1.

### 12.5 Closing thought — "think as agent"

D6 v1 is excellent as **constitutional document for human architects +
FPF scholars**. It is **not yet constitutional for an LLM booting up
Sunday morning to close an ai-consulting-dach pipeline task**.

The gap is not conceptual — D6 concepts are correct. The gap is that the
document treats agents as **readers**, not **boot-targets**. Readers
tolerate hand-waves ("agent_onboarding section with initial_context_pack,
warm_up_tasks, calibration_checkpoint"). Boot-targets do not — they need
the schema, the path, the example.

Apply the 17 recommendations above and D6 v1.1 becomes agent-executable.
Fundamental direction is right; finishing discipline is what the
ontology itself requires.

---

**END REVIEWER 3 — AI-AGENT DESIGNER CRITIQUE**

*Written 2026-04-20 by Claude Opus 4.7 (1M context) fresh session, ~1.75h
extended thinking. Verified ground-truth against repo state (agent
system.md files, executors/ absence, schema enum, FPF-Spec F.6 + A.13:4.3).
Next artifact: Stage C synthesis of Reviewers 1-4 findings.*
