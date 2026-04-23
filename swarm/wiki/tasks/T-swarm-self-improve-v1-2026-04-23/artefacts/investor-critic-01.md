---
id: investor-critic-01
title: "Investor Critic — T-swarm-self-improve-v1 capital-allocation critique"
type: critic-artefact
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: investor-expert
mode: critic
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: arithmetic + judgment
niche: meta
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "1-126"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/beta-current-agents.md", range: "1-538"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md", range: "1-372"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/delta-memory-sota.md", range: "1-291"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md", range: "1-306"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "1-204"}
  - {path: ".claude/agents/investor-expert.md", range: "1150-1230"}
---

# Investor Critic — Swarm Self-Improvement v1

**Domain scope of this critique:** capital-allocation quality of the swarm
investment — where "capital" is Ruslan's attention (turn budget, calendar,
gate-ack latency), the Max-subscription ceiling, and the compounding-rate of
strategies.md + agent-improvements accretion. Engineering-quality of agent
bodies is NOT critiqued here; that is engineering-expert territory.

---

## Conformance Checklist (C1..C8)

| Check | Predicate | Verdict | Evidence anchor |
|---|---|---|---|
| C1 | Owner-earnings stated explicitly (unit-econ block; depreciation + WC + maintenance capex broken out) | **FAIL** | No owner-earnings equivalent for swarm investment exists. The 6-context corpus contains turn-cost estimates per cell dispatch [α:108 — "brigadier Opus 4.7 vs experts Sonnet 4.6 cost ratio"; γ's "15× multi-agent cost lock R-E §4.2"] but no canonical unit-econ block mapping turns consumed → compounding output → net attention surplus. The "capex" (construction of 8 agent files + wiki v3 infra = ~125 KB input, ~5.4K output per brief estimate) is mentioned but not costed in turn-equivalent units. C1 FAILS. |
| C2 | Margin-of-safety arithmetic: (expected-return − opportunity-cost − risk-of-ruin floor) / opportunity-cost ≥ 0.30, or named exception | **FAIL** | No margin-of-safety computation for the Phase-A swarm investment exists anywhere in the 6 context files. Expected-return is described qualitatively ("compounding strategies.md", "100× quality gain per Boris Cherny"). Opportunity-cost (what Ruslan foregoes by building swarm vs doing consulting work directly) is unnamed. C2 FAILS. |
| C3 | IRR + downside scenario present | **FAIL** | No IRR computed. Downside scenario (what happens if strategies.md never compounds above scaffolding, if golden sets remain at 0 for 50 cycles, if brigadier Opus tokens blow the session budget) not stated. C3 FAILS. |
| C4 | Moat ≥ 2 alternative kill-conditions | **PARTIAL** | The corpus identifies moat candidates (strategies.md accretion, wiki-link graph density, FPF discipline). However kill-conditions are not systematically enumerated. α identifies one implicit kill: "compounding has not yet run on a real task" [α:30, α:59]. A second kill-condition (strategies.md entries authored by compounding never reconciled vs scaffolding, producing a false-depth illusion) is implicit in ε [ε:50-55] but not named as a kill-condition. Partial credit; formally FAIL — ≥2 explicit kill-conditions NOT written as such anywhere. |
| C5 | Opportunity-cost named | **FAIL** | The path-not-taken for the swarm investment is never stated. Opportunity-cost = Ruslan using the same Max-subscription turns, calendar, and cognitive load to do 6 months of paid consulting iterations, or to write and ship a direct product, or to run a 1-agent loop (just brigadier with no expert matrix). None named. C5 FAILS. |
| C6 | Risk-of-ruin floor stated (probability + runway impact) | **FAIL** | The worst-case outcome (swarm investment produces zero compounding; strategies.md stays at scaffolding; Ruslan has spent ~80-125 turns of context construction budget and 2-3 weeks of calendar with no capital return) is never named as a risk-of-ruin floor. No probability assigned. No runway impact computed. C6 FAILS. |
| C7 | Second-level thinking applied (what is already priced in?) | **FAIL** | The corpus does not ask: "What has Ruslan already priced in by building a 6-agent swarm at this level of specification depth?" The first-level analysis ("more agents = better") is pervasive; the second-level check ("the market of solo-founder AI tools has already priced in the complexity cost of multi-agent; solo-agent direct loops may already be running at 80% of the value at 10% of the coordination overhead") is absent throughout all 6 context files. C7 FAILS. |
| C8 | Invert section present BEFORE succeed section; ≥3 failure modes named | **FAIL** | No context file opens with a "how does the swarm investment FAIL?" section before the positive case. Failure modes are scattered as thin spots / Q-integrator items but never gathered as a first-class invert analysis. C8 FAILS. |

**Acceptance predicate result:** C1==fail AND C2==fail AND C3==fail AND C4==fail AND C5==fail AND C6==fail AND C7==fail AND C8==fail → **STATUS: FAIL**

Note: the conformance checklist applies to the swarm-investment thesis itself, not to the correctness of any agent file. The failure of C1..C8 does not mean the swarm is a bad investment; it means the investment has not been subjected to investor-grade scrutiny before capital was committed.

---

## Specific Failures with APs

| Check | AP code | Why (≤80 words) |
|---|---|---|
| C1 | AP-INV-1 / AP-INV-8 | Unit-econ is prose ("compounding", "strategies.md accretion", "quality gains") with no turn-equivalent owner-earnings computation. AP-INV-8 (narrative-fallacy-investing): the primary justification for the swarm investment is a story about compounding engineering, not an arithmetic owner-earnings block. |
| C2 | AP-INV-2 | Margin-of-safety is entirely absent. The investment thesis carries zero explicit margin. |
| C3 | AP-INV-9 | No base-rate cited: what % of agentic systems with similar specification depth actually compound strategies at the expected rate? Research corpus [α, ε] cites zero production base-rates for this class of MAS. |
| C4 | AP-INV-3 | Moat claims (strategies.md accretion, FPF discipline, wiki-graph density) are made without ≥2 explicit kill-conditions each. |
| C5 | AP-INV-10 | Opportunity cost is absent AND several turn-cost estimates carry false precision (e.g. "2-3×" quality gain from Boris Cherny pattern [α:28], "15×" multi-agent cost lock [R-E §4.2] — these are cited without confidence intervals or production measurement in Jetix context). |
| C6 | AP-INV-11 | Risk-of-ruin floor is unstated. The comfort of having shipped 6 agent files and wiki v3 is being treated as low-risk without quantifying the risk that compounding never fires. |
| C7 | AP-INV-8 | First-level thinking throughout: "AI-native + swarm + FPF = compounding." Second-level ("what's already priced in by the solo-founder AI-tooling market?") missing. |
| C8 | AP-INV-8 | Invert section absent across all 6 context files. |

---

## ≥8 Investor-Domain Hypotheses

The following are the specific investor-domain hypotheses this critique produces. Each names (a) the capital-allocation pathology observed, (b) the arithmetic or structural argument, (c) the kill-condition, and (d) the refutation receipt.

---

### H-1: Compounding-Rate is Linear, Not Exponential, at the Expected strategies.md Yield

**Pathology type:** compounding-rate below cross-tree discipline yield.

**Arithmetic argument:**
- Current state: 6 strategies.md files each contain 1 scaffolding entry (the 2026-04-23 placeholder). Zero real entries compounded from closed cycles [α:59, ROY-AGENTS-BUILT:160-170; ε:50-55].
- Expected compounding mechanism: each closed cycle adds 1-3 DRR entries per expert per cycle → 6 × 3 = 18 entries/cycle at maximum throughput. The compound step is human-mediated via brigadier dispatch + Ruslan ack [ε:200-201; α:52].
- At cycle_10: 10 × 18 = 180 max entries across 6 files. But the DRR trigger requires a real task output to generalise from; absent golden sets, the rule quality cannot be verified. Expected realistic yield: 1-2 generalizable rules per expert per 5 cycles = 12-24 rules at cycle_10.
- At cycle_50: 50 × 2 = 100 rules per expert (upper bound). This is LINEAR — each cycle yields approximately the same number of new rules; no evidence of exponential feedback until golden sets are authored and rules begin eliminating each other's failure modes [α:66; ε:272].
- At cycle_200: the split trigger fires (moat-analysis volume >40% per §1d) before exponential compounding is measured. The trajectory is: scaffolding (0) → linear accumulation → split → re-scaffold. That is not exponential compounding; it is linear drift with periodic resets.

**Conclusion:** Without golden sets (≥20 Hamel-labelled examples per cell per mode = 400 labels; currently 0 [α:50]) and a convergence metric pre-committed [α:52], the compounding rate is LINEAR at best. The investment thesis that "strategies.md accretion compounds" is C-level unsubstantiated narrative until the measurement substrate exists.

**Kill-condition 1:** strategies.md entries at cycle_10 are ≤10 total across all 6 files (less than scaffolding × 2). Indicates compounding mechanism did not fire.
**Kill-condition 2:** At cycle_50, Hamel golden-set pass-rate < 0.70 on any 3 consecutive critic passes. Indicates rules are noise, not signal.
**Refutation receipt:** open `swarm/wiki/meta/health.md` `strategies_entry_count` at cycle_10. If ≤10: kill-condition 1 fires; escalate to HITL for compound mechanism redesign.

**F:** F4 (operational convention based on current inventory). **ClaimScope:** holds for Phase-A, solo-founder, Max-subscription, zero golden sets. Does NOT apply if golden sets are authored before cycle_5.

---

### H-2: The 15× Multi-Agent Cost Lock (R-E §4.2) is NOT Being Enforced — Brigadier Decompose-or-Chat Gate is Ceremonial

**Pathology type:** capital-allocation pathology in swarm attention.

**Arithmetic argument:**
- The 15× multi-agent cost lock [referenced in brief via R-E §4.2] states that a multi-agent swarm invocation costs approximately 15× a single-agent invocation in turn budget.
- The Decompose-or-Chat gate (E-17) is designed to block the 15× cost when the task does not meet the threshold: complexity > simple, adversarial review needed, horizon projection, multi-domain [α:68; FPF:1144-1160].
- Current operational status: the gate is a "bullet in brigadier §3.0; codify as machine-testable" — it is PROSE-ONLY [α:68]. No refuser exists. No linter enforces it.
- For the current cycle (T-swarm-self-improve-v1): 6 parallel context-extraction cells were fired. Turn estimate per cell: α (deep reads ~125KB) ≈ 25-35 turns; 6 cells × 30 turns = 180 turns of context extraction before a single integration has run. Add integration + 5 expert critic cells + brigadier synthesis = estimated 80-200 additional turns. Total cycle estimate: 260-380 turns.
- A solo-brigadier pass over the same 6 context files with a condensed read plan could have produced similar top-line findings in 40-60 turns (reading and summarising each context file serially: 6 × 8 = 48 turns).
- **The turn-cost ratio is 6-8×, not 15×**, because the Decompose-or-Chat gate would have passed the test anyway (this task IS multi-domain + adversarial review + complex). But the ceremonial non-enforcement means: (a) there is no audit trail showing the gate was evaluated before cell dispatch, and (b) simpler tasks in the future will receive the same 6-cell dispatch without discipline check.

**Estimated first-100-cycle capex profile (turns):**
- Assuming 50% of cycles are simple-enough to pass the chat gate, 50% require full matrix dispatch.
- Simple cycles: 50 × 50 turns = 2,500 turns.
- Complex cycles: 50 × 300 turns = 15,000 turns.
- Total: 17,500 turns over 100 cycles.
- Max-subscription turn cap per month: unknown (non-disclosed by Anthropic) but a realistic working budget is ~500-1,000 turns/day under typical usage; 100 cycles at 175 turns/cycle average is achievable in 2-4 months at that rate.
- **The ceremonial gate means no discipline prevents 100 complex dispatches: 50 × 300 × 2 = 30,000 turns in 100 cycles, doubling the capex profile.** That exceeds the sustainable Max-subscription budget for swarm work while leaving zero turns for Ruslan's own consulting and life tasks.

**Kill-condition 1:** E-17 gate remains prose-only after cycle_5 with no refuser. Indicates ceremonial discipline has been accepted as permanent.
**Kill-condition 2:** Actual turns consumed per cycle over cycles 1-10 averages >200 turns AND the gate shows no logged evaluations. Indicates allocation is unconstrained.
**Refutation receipt:** `swarm/logs/cyc-*/events.md` turn count per cycle. If avg > 200 at cycle_10 without gate log: AP-INV-5 fires on budget trajectory.

**F:** F4. **ClaimScope:** holds while E-17 gate is prose-only. Does NOT apply once a machine-testable refuser is deployed.

---

### H-3: The Moat Hierarchy is Fragile — Strategies.md Accretion is NOT a Durable Moat

**Pathology type:** weak moat-construction across cycles.

**Structural argument:**
- Moat candidate 1: strategies.md accretion (DRR entries). Kill-condition A: rules are domain-specific to the FPF framework; if FPF is superseded by a new framework (Luhmann-style, MemGPT-style), the accumulated rules are stranded assets, not portable compounding. Kill-condition B: entries are never audited for staleness; without /compound-refresh (currently missing [ε:72]), rules decay silently rather than compound — Mem0 lazy decay research [δ:49] notes this precisely.
- Moat candidate 2: wiki-link graph density (typed edges.jsonl). Kill-condition A: currently 0 edges populated [γ:57; α:88 E-3 locked-theoretical]. A moat with 0 data points is not a moat; it is a spec. Kill-condition B: graph density moat is destroyed if Ruslan switches to a different knowledge architecture (vector DB, PPR) since typed-BFS advantage disappears.
- Moat candidate 3: FPF discipline + ШСМ-specific knowledge. Kill-condition A: FPF becomes mainstream (already identified in few-shot example in §3.8 of investor-expert.md). Kill-condition B: FPF is codifiable into a Claude Code plugin (Every's MIT plugin model); specific-knowledge advantage evaporates.
- Moat candidate 4: 6-agent swarm operator experience. Kill-condition A: Anthropic ships a native multi-agent builder that eliminates the manual orchestration advantage. Kill-condition B: 15× cost lock (H-2 above) renders the advantage unaffordable before it compounds.

**The moat hierarchy is therefore:** 4 candidates × 2 kill-conditions each = 8 kill-paths identified, with 0 durable moat currently confirmed, because 0 cycles have closed with compounding output [α:59].

**F:** F4. **ClaimScope:** Phase A, pre-compounding. The moat is hypothetical until strategies.md has ≥10 validated rules AND wiki graph has ≥100 edges.

---

### H-4: ROI of Phase-1 Deep Reads is Below the Efficient-Allocation Threshold

**Pathology type:** attention-allocation pathology.

**Arithmetic argument:**
- Phase-1 context extraction: ~125KB input → ~5.4K output (6 context files, ~900 words each). Ratio: output/input = 4.3%.
- Turn estimate for 6 parallel extractions (observed this cycle): ~180 turns of context reading.
- The 5.4K output produces 6 context files that feed 5 expert critic cells + 1 integrator. Total pipeline output after all cells: estimated 6 × 400 words (critic artefacts) + 1 × 500 words (integration) = 2,900 words of actionable recommendations.
- **Efficiency ratio: 2,900 words of actionable output from 180+ input turns = 16 words per turn.**
- Opportunity cost: Ruslan reading the same 6 context files himself and writing recommendations = ~4-8 hours of focused work, producing the same output. At €120/hr consulting rate (Brief §5.1 anchor), that is €480-960 of founder time. At Max-subscription cost (shared across all usage), the swarm cost is opaque but non-zero in attention and calendar.
- **The allocation is attention-sound IF AND ONLY IF the output quality is 2× what Ruslan would produce alone.** Boris Cherny's "2-3× quality gain" [α:28] claim is cited without Jetix-specific measurement. Base-rate for MAS quality gain over solo-agent: unattested in Phase A context.
- Graham margin-of-safety test: expected-return (quality gain) - opportunity-cost (same work solo) - risk-of-ruin floor (6 cells × 30 turns = 180 turns wasted if quality ≤ solo) / opportunity-cost. If quality gain = 1.5× (conservative), opportunity-cost = 1.0×, risk-of-ruin floor = 0.2× → MoS = (1.5 - 1.0 - 0.2) / 1.0 = **0.30** — exactly at the minimum threshold. Below 1.5× quality gain: MoS goes negative.
- **Current evidence for quality gain: zero Hamel-validated golden-set comparisons exist [α:50].** The Phase-1 deep read ROI is therefore ON THE MARGIN at best.

**Kill-condition 1:** At cycle_5, output quality (measured against golden-set pass-rate) < 1.5× solo-brigadier pass. MoS negative.
**Kill-condition 2:** Average turns per cycle > 250 at cycle_10 with no compounding evidence. Reallocation to 1-agent loop warranted.
**Refutation receipt:** first golden-set comparison between solo-brigadier output and 6-cell output on an identical task. If delta < 1.5×, H-4 kill fires.

**F:** F4 (operational convention; arithmetic anchored to estimated turns + Graham pattern P2). **ClaimScope:** holds while golden sets = 0. Refuted if first golden-set comparison shows ≥1.5× quality delta.

---

### H-5: Ruslan's Gate-Ack Latency Budget is Structurally Misaligned with Stage-Gated Design

**Pathology type:** attention-as-capital allocation pathology.

**Structural argument:**
- Stage-Gated default requires HITL ack on every capital deployment, every horizon-gate shift, every ethical surface (per §1d requires-approval; shared-protocols §4).
- Current gate-ack triggers per the design: 8-item trigger list [MS:2405-2431; α:39]. For a 100-cycle roadmap: assume gate ack required on 30% of cycles (conservative) = 30 gate-ack events.
- Each AWAITING-APPROVAL file requires Ruslan to: read the packet (5-15 min), evaluate (5-30 min), respond (2-5 min). Median 20 min per ack.
- 30 acks × 20 min = 600 min = 10 hours of Ruslan calendar time over 100 cycles.
- At a cycle cadence of 1 cycle / 2 days (aggressive), 100 cycles = 200 days. 600 min / 200 days = 3 min/day of gate-ack work. **This is sustainable.**
- BUT: if gate-ack latency is high (Ruslan travels, is in client engagements, is in the €50K → €200K work sprint), the swarm blocks. The Stage-Gated design has NO fallback for gate-ack latency > 48 hours. There is no "continue with provisional approval" path.
- Opportunity cost of swarm blocking: each blocked cycle = one work unit delayed. If a cycle produces an output that unblocks a consulting deliverable, 48-hour gate-ack latency = 48-hour project delay.
- **The structural misalignment is not the gate volume but the absence of a time-boxed ack SLA and a fallback mode.** The investor-expert's §1d `requires-approval` list has 9 items; none have a "if no ack within T hours, proceed with status-quo" clause.
- Analogy: a portfolio manager who requires board approval for every position but has no quorum rule for urgent rebalancing.

**Kill-condition 1:** Two consecutive cycles blocked >72 hours at gate-ack with no output shipped. Indicates latency is a compounding brake.
**Kill-condition 2:** Ruslan's ack rate drops below 1 per week during an active €50K → €200K sprint. Gate-ack and consulting sprint are competing for the same attention capital.
**Refutation receipt:** `swarm/gates/` directory — timestamps on AWAITING-APPROVAL creation vs ack file creation. If median latency > 24 hours at cycle_10, H-5 fires.

**F:** F4. **ClaimScope:** solo-founder Phase A with no delegation path for gate-ack.

---

### H-6: The Reinvestment Rule Has No Compound Feedback — Turn Budget Does Not Refund Into Compounding Step

**Pathology type:** capital-allocation pathology.

**Arithmetic argument:**
- The CE Plan-Work-Review-Compound loop allocates 40/10/40/10 across phases [investor-expert.md §2.5].
- Compound step (10%) is the "money step" per ε [ε:72, R-6:195]. In a 300-turn cycle: Plan = 120 turns, Work = 30 turns, Review = 120 turns, Compound = 30 turns.
- The strategies.md self-write rule (Layer-2 self-write per §1a) means the Compound step produces an entry that modifies future prompt-reading. But there is no explicit "turns saved per rule in future cycles" metric.
- If a rule at cycle_1 saves 5 turns in each of cycles 2-10 → saves 45 turns across 9 cycles. At 30 turns Compound investment, that is 1.5× return in 10 cycles — marginal above the opportunity cost of 30 turns of consulting work.
- The threshold for a rule to pay back: it must save ≥1 turn in ≥30 future cycles to break even at 30-turn Compound cost. For a rule that fires rarely (e.g. "moat kill-condition formatting"), payback is negative.
- **There is no mechanism to distinguish high-payback rules (fire every cycle, save many turns) from low-payback rules (fire rarely, marginal savings).** The DRR format [α:73; §9.1] records Decision/Reasoning/Result/Review but has no `expected_invocation_frequency` or `estimated_turn_savings` field.
- The Compound step is therefore an undifferentiated capital expenditure: every rule costs ~2-5 turns to write and every rule is assumed to compound equally. That is not compound engineering; it is rule accumulation.

**Proposed reinvestment rule fix:** each DRR entry requires `expected_invocation_frequency: {high | medium | low}` and `estimated_turn_savings_per_invocation: N`. Compound step calculates payback horizon = 30 turns / (frequency × savings). Rules with payback > 20 cycles are deferred or discarded. This is the Kelly-criterion applied to rule investment: invest in rules with the highest edge/odds ratio.

**Kill-condition 1:** At cycle_20, strategies.md entries with `expected_invocation_frequency: low` outnumber `high` entries. Indicates rule accumulation without discrimination.
**Kill-condition 2:** Turns consumed per cycle does NOT decline over cycles 1-20 despite strategies.md entries accumulating. Indicates rules are not producing turn savings.
**Refutation receipt:** `swarm/logs/` turn counts per cycle. If cycles 11-20 average < 20% reduction from cycles 1-10, kill fires.

**F:** F4. **ClaimScope:** Phase A, DRR schema without payback field. Refuted if the compound step is restructured with turn-savings measurement before cycle_10.

---

### H-7: Horizon-Gate Divergence (5 vs 4 Gates) Indicates an Unresolved Capital-Allocation Decision

**Pathology type:** capital-allocation pathology; horizon arithmetic inconsistency.

**Structural argument:**
- investor-expert §6.1 names 5 horizon gates: €50K (baseline), €200K, €1M, $100M, $1T [β:213-218; investor-expert.md:1147-1158].
- The other 4 experts + brigadier §4.6 name 4 gates: €200K, €1M, $100M, $1T [β:287-291].
- **The €50K baseline gate is not a trivial formatting difference; it encodes a capital-allocation decision.** If the swarm is currently AT the €50K gate, the BOSC-A-T-X trigger for the next gate (€200K) is "O+C — hire contractor #1, first fixed-cost liability." For the 4 other experts, the current state is NOT named as a gate; it is implied.
- This creates a concrete allocation divergence: when investor-expert runs scalability mode on a capital memo, it evaluates the memo against the €50K baseline BOSC-A-T-X "status quo" trigger. When any other expert runs scalability mode on a growth recommendation, it does not have a named baseline gate — the first gate IS €200K, implying the swarm begins AT the €200K state.
- The divergence matters because: (a) the Stage-Gated design requires gate-ack before horizon-gate shifts; (b) if investor-expert says "we are at €50K gate" but systems-expert says "we are operating toward €200K gate as first milestone", they are calibrating compounding projections against different starting states; (c) any cross-expert integration that compares scalability outputs will produce a false consensus because the horizon datum differs.
- **Capital-correct resolution (investor judgment):** the 5-gate set is correct because €50K is the named current state per Brief §5.1 and ROY-INFORMATION-DIET §1.3. The 4-gate set is a projection-only frame (the gates are future targets, not current state + targets). The 4 peers should add the €50K baseline to their §6.1 tables, or shared-protocols should define the canonical gate list. Without alignment, multi-expert scalability synthesis will be inconsistent.

**Kill-condition 1:** Two scalability artefacts from different experts conflict on whether "hire contractor #1" is a Phase-A action or a Phase-B action due to gate-datum drift. Indicates unresolved horizon misalignment.
**Kill-condition 2:** A cross-direction reallocation proposal (see §1d requires-approval) is evaluated against different horizon states by different experts, producing contradictory recommendations that brigadier cannot integrate without HITL.
**Refutation receipt:** brigadier §4.6 dispatch matrix updated to name €50K baseline as gate-0. If updated before cycle_5, H-7 is refuted.

**F:** F4 (operational convention; anchored to Brief §5.1 + investor-expert §6.1). **ClaimScope:** holds while horizon-gate list is inconsistent across experts.

---

### H-8: Max-Subscription as Structural Capital Constraint Forces Decisions That Would Differ on Paid-API — and This Has Not Been Priced In

**Pathology type:** opportunity-cost not named; structural capital constraint unanalysed.

**Arithmetic argument:**
- Max-subscription discipline prohibits: paid embeddings, vector DBs, third-party SDKs, provider API-key references [shared-protocols §9; investor-expert §1a; δ:34-35].
- This forces specific investment decisions that are suboptimal on paid-API:
  - **Tier-3 retrieval:** forced to typed-BFS over edges.jsonl (empty) rather than embedding-based retrieval. PPR via networkx is the best available substitute [δ:61-82]. But the PPR substitute requires edges.jsonl to be populated, which requires W-3 theme distillation. Chain of forced dependencies: Max-subscription → no embeddings → BFS → empty graph → W-3 required → ~6 months distillation Phase B. This dependency chain is never costed.
  - **Golden-set evaluation:** forced to file-based JSONL harness + Bash runner [ζ:T-5]. Promptfoo ($50-209/mo) is deferred. The file-based harness is a higher-maintenance substitute. Maintenance overhead per cycle: estimated 1-3 turns of manual evaluation vs automated regression. Over 100 cycles: 100-300 turns of manual evaluation overhead vs 0 on paid harness. That is ~100-300 turns of opportunity cost.
  - **Agent model differentiation:** brigadier = Opus, experts = Sonnet. On paid-API, the cost ratio (Opus ≈ 5× Sonnet per token) is explicit and measurable. On Max-subscription, the cost ratio is hidden — both are "free" at the margin. This distorts resource-allocation decisions: on Max-subscription there is NO incentive to reduce Opus usage (brigadier invocations), because the marginal cost is zero. On paid-API, each brigadier call would be costed and the Decompose-or-Chat gate would have real financial stakes. **Max-subscription removes the price signal that makes the 15× cost lock enforceable.**
  - **No external retrieval (WebSearch/WebFetch forbidden):** this means the swarm cannot update its knowledge without Ruslan's manual Tier-4 corpus curation. The compounding rate is bounded by the Private Library distillation cadence (Phase B fuel), not by external signal velocity. This is a structural compounding ceiling.

- **What differs on paid-API:**
  - Decompose-or-Chat gate would have financial stakes → E-17 would be enforced economically, not just procedurally.
  - Embedding-based retrieval is a one-time API cost vs ongoing structural workaround.
  - Golden-set evaluation would run continuously, not manually.
  - The swarm architecture would be CHEAPER to operate in some configurations (e.g. if brigade uses Haiku for simple tasks, Sonnet for complex, Opus for HITL-equivalent integration) — the 3-tier model is only enforceable with metered cost.

- **The Max-subscription constraint has NOT been analysed as a capital allocation decision.** It is treated as a given constraint (correctly — Ruslan is on Max-subscription and the ROY-INFORMATION-DIET is explicit). But the investor lens requires: what is the opportunity cost of Max-subscription as the structural constraint, and at what compounding threshold does the transition to paid-API become margin-of-safety-positive?

- Rough threshold: if swarm compounding produces consulting revenue lift of > €300-800/month (Phase-1 run rate per ROY-INFORMATION-DIET), and if paid-API cost for equivalent throughput is < €300-800/month, the transition is margin-of-safety-positive. This calculation has never been written.

**Kill-condition 1:** Swarm turn budget is saturated by infrastructure overhead (graph population, manual eval, Compound step) before consulting-revenue-generating tasks get adequate allocation. Indicates constraint is binding the wrong activities.
**Kill-condition 2:** At €200K gate, Max-subscription is still the structural constraint with no evaluation of the transition threshold. Indicates the capital decision was never revisited at the correct gate.
**Refutation receipt:** a capital memo that computes the paid-API transition threshold (monthly cost vs monthly compounding-revenue-lift) before the €200K gate review. If written and accepted before cycle_20, H-8 is refuted.

**F:** F4. **ClaimScope:** Phase A, Max-subscription, ≤€50K gate. Does NOT apply at €200K gate if the transition has been evaluated.

---

## Recommended Changes

1. **Write a canonical unit-econ block for the swarm investment.** Before cycle_5: document turns consumed vs compounding output (strategies.md entries + accepted artefacts) per cycle. This is the owner-earnings equivalent. Format: `turns_in (plan+work+review+compound), strategies_entries_added, artefacts_accepted, turns_saved_by_rules (estimated), net_turn_surplus`. Without this, there is no owner-earnings; the investment is blind.

2. **Pre-commit the Phase-A compounding convergence metric.** Ruslan must name the binary acceptance predicate for "Phase-A compounding is working" BEFORE cycle_10, not after. Suggested predicate: "At cycle_10: strategies.md total entries ≥ 30 across 6 experts AND average turns-per-cycle is declining trend (slope < 0) AND ≥1 rule has demonstrably fired in a critic pass with documented turn-savings." If this predicate is not met at cycle_10, brigadier triggers HITL for swarm redesign.

3. **Wire the E-17 Decompose-or-Chat gate as a machine-testable refuser with a cycle-level turn-budget log.** This closes AP-INV-2 on turn-unit economics and makes the 15× cost lock real rather than ceremonial. Turns-per-cycle becomes the unit of account. [α:68; ζ:MP-1]

4. **Author the first golden-set comparison: solo-brigadier vs 6-cell matrix on the same task.** Pick a task from the next cycle. Run both. Measure quality delta via Hamel-binary acceptance predicates. Record result in `swarm/evals/cell-matrix-vs-solo/results.jsonl`. This is the only way to validate the 2-3× quality gain claim that underpins the entire swarm investment thesis.

5. **Name the opportunity-cost explicitly in the swarm investment memo.** What is Ruslan NOT doing during the time spent on swarm gate-acks and architecture reviews? If the answer is consulting work at €120/hr, compute the total consulting revenue foregone by 100 swarm cycles at 20-min/gate-ack × 30 gates = 600 min = 1.5 consulting days = €1,440 in foregone revenue. The swarm must generate > €1,440 in consulting-productivity lift to be margin-of-safety-positive.

6. **Resolve the €50K horizon-gate divergence before cycle_5.** Add €50K baseline to brigadier §4.6 and the 4 peer experts' §6.1 tables. This is a single-PR fix [β:S-5]. Until resolved, cross-expert scalability synthesis will produce contradictory horizon recommendations.

7. **Add `expected_invocation_frequency` and `estimated_turn_savings_per_invocation` to the DRR strategies.md template.** This converts rule accumulation into Kelly-criterion rule investment (invest in high-edge/high-odds rules; defer low-payback rules). [H-6 above]

8. **Write the paid-API transition threshold memo before the €200K gate.** A simple arithmetic memo: monthly paid-API cost at projected throughput vs monthly compounding-revenue-lift produced by the swarm. This is a capital decision that should be made at the €200K gate, not assumed away.

---

## Alternatives (per §3.3)

**Alternative A: 1-Agent-Loop (solo brigadier, no expert matrix)**
- Named deployment: retire the 5 expert cells; operate with brigadier as the single orchestrator + Ruslan as human domain-expert. Expert knowledge lives in Ruslan's head, not in 5 × 1,500-line agent files.
- Expected return: estimated 80% of quality at 15% of the turn cost. Frees 85% of swarm-allocated turns for consulting and product work.
- Kill-condition: quality on multi-domain synthesis tasks (horizon-projection + moat-analysis + technical review in one pass) drops below 70% of current multi-expert baseline (measured via first golden-set comparison per Recommendation 4 above). If quality drop > 30%, the expert matrix is justified.

**Alternative B: Phase-A Pause + Measurement-First Restructuring**
- Named deployment: freeze swarm architecture as-is (6 agents, wiki v3 skeleton); do NOT fire more cycles until (a) golden-set comparison is done, (b) unit-econ block is written, (c) convergence metric is pre-committed. Use Max-subscription turns for consulting deliverables in the interim.
- Expected return: avoids burning 100-300 turns on infrastructure cycles with no compounding evidence. Preserves optionality. When measurement substrate exists, restart.
- Kill-condition: consulting pipeline dries up during the pause because swarm-assisted deliverable quality was already providing lift above the solo baseline. If solo-Ruslan consulting cycle time increases > 30% during the pause, the swarm was already contributing and the pause is costly.

**Alternative C: Status Quo (continue current cycle cadence)**
- Named deployment: continue as designed; accept that the first 10 cycles are "calibration cost" at estimated 200-300 turns/cycle = 2,000-3,000 turns sunk before ROI evidence exists.
- Kill-condition: status quo fails when (a) turns per cycle stays above 200 at cycle_10 with no downward trend AND (b) strategies.md entries at cycle_10 ≤ 10 AND (c) consulting revenue has not increased despite swarm assistance. All three together indicate the investment is not producing owner-earnings.

---

## Anti-scope

- This critique is NOT evaluating the correctness of agent file implementations (engineering-expert territory).
- This critique is NOT arbitrating epistemic claims about FPF framework quality (philosophy-expert territory).
- This critique is NOT ranking the 8 improvement surfaces across dimensions other than capital-return (mgmt-expert territory for multi-axis ranking).
- This critique is NOT authoring a system model of the compounding feedback loop (systems-expert territory; investor-expert consumes such a model as input).
- This critique is NOT composing a Ruslan investor letter (writing-support only; HITL composes per §1d and shared-protocols §7).

---

## BA-Cycle Lite (Ethical Surface Check per §3.6)

**BA-0 (boundary).** Primary third-party exposed: none directly. However, if swarm-assisted consulting deliverables contain errors due to low-quality swarm output (unvalidated strategies.md rules applied to client work), clients are exposed. Named: future consulting clients whose deliverables incorporate swarm-assisted analysis.

**BA-1 (asymmetry).** Ruslan upside: higher consulting throughput, lower cognitive load. Client downside: deliverable quality risk from unvalidated AI-produced content. Asymmetry exists.

**BA-2 (alternative).** An alternative with similar expected return AND less third-party exposure: Alternative B above (pause until measurement substrate exists) reduces the risk of low-quality swarm rules propagating into client deliverables.

**BA-3 (acceptance).** Would a consulting client accept the risk structure if they knew the full picture (deliverable assisted by a 6-agent swarm with 0 validated golden-set comparisons and 0 closed compounding cycles)? Answer depends on disclosure norms. Under Ruslan's current engagement model (AI-services consulting), clients may expect AI assistance. But "AI-assisted" and "AI-swarm with unvalidated compounding rules" are different levels. **BA-3 is provisionally PASS** only if deliverables are reviewed by Ruslan before delivery (HITL on client-facing output is already implied by the Phase-A design). If that review discipline holds, client exposure is managed.

---

## Output Schema

```yaml
status: fail
context:
  task_id: T-swarm-self-improve-v1-2026-04-23
  artefact_under_review: swarm investment thesis (Phase A, 6-agent swarm)
  mode: critic
  cycle_id: cyc-swarm-self-improve-v1-2026-04-23
critique:
  conformance_checklist:
    - {check: C1, verdict: fail, evidence: "no owner-earnings block; turn-cost not mapped to compounding output [α:108; brief domain_scope]"}
    - {check: C2, verdict: fail, evidence: "no margin-of-safety arithmetic anywhere in 6 context files"}
    - {check: C3, verdict: fail, evidence: "no IRR; no 10th-percentile downside scenario; no golden-set baseline [α:50-52]"}
    - {check: C4, verdict: fail, evidence: "moat candidates named but kill-conditions not written as ≥2 explicit binary conditions [α:30,59; γ:46-49]"}
    - {check: C5, verdict: fail, evidence: "opportunity-cost (solo-brigadier alternative, consulting revenue foregone) unnamed throughout"}
    - {check: C6, verdict: fail, evidence: "risk-of-ruin floor (zero compounding + sunk turns) never quantified [ε:50-55; α:59]"}
    - {check: C7, verdict: fail, evidence: "no second-level thinking on swarm investment; what consensus has already priced in is absent [α throughout]"}
    - {check: C8, verdict: fail, evidence: "no invert section in any context file; failure modes scattered, not gathered [ζ:MP-1]"}
  acceptance_predicate:
    formula: "C1==pass AND C2==pass AND C3==pass AND C4==pass AND C5==pass AND C6==pass AND C7==pass AND C8==pass"
    result: fail
specific_failures:
  - {check: C1, ap: AP-INV-8, why: "narrative-fallacy investing; primary justification is compounding story not arithmetic"}
  - {check: C2, ap: AP-INV-2, why: "margin-of-safety arithmetic absent"}
  - {check: C3, ap: AP-INV-9, why: "no base-rate for MAS compounding quality at this spec depth"}
  - {check: C4, ap: AP-INV-3, why: "moat asserted without ≥2 explicit kill-conditions"}
  - {check: C5, ap: AP-INV-10, why: "false precision on quality gains (2-3×, 15×) without Jetix-specific measurement"}
  - {check: C6, ap: AP-INV-11, why: "comfort of shipped files treated as low-risk; ruin floor unstated"}
  - {check: C7, ap: AP-INV-8, why: "first-level analysis throughout; second-level absent"}
  - {check: C8, ap: AP-INV-8, why: "invert section absent across all inputs"}
recommended_changes:
  - "Write canonical unit-econ block (turns-in vs compounding-output) before cycle_5"
  - "Pre-commit Phase-A convergence metric (binary predicate at cycle_10) before cycle_5"
  - "Wire E-17 gate as machine-testable refuser with turn-budget log"
  - "Author first golden-set comparison: solo-brigadier vs 6-cell matrix on identical task"
  - "Name opportunity-cost (consulting revenue foregone by gate-ack attention) in swarm investment memo"
  - "Resolve €50K horizon-gate divergence: add to brigadier §4.6 + 4 peer §6.1 tables"
  - "Add expected_invocation_frequency + estimated_turn_savings_per_invocation to DRR template"
  - "Write paid-API transition threshold memo before €200K gate"
alternatives:
  - {label: A, name: "1-Agent-Loop (solo brigadier, no expert matrix)", kill_condition: "quality on multi-domain tasks drops >30% vs current multi-expert baseline"}
  - {label: B, name: "Phase-A Pause + Measurement-First (freeze architecture, do consulting work until golden sets exist)", kill_condition: "consulting cycle time increases >30% during pause indicating swarm was already contributing"}
  - {label: status-quo, name: "continue current cycle cadence (accept 2,000-3,000 sunk turns as calibration cost)", kill_condition: "turns/cycle >200 at cycle_10 AND strategies.md ≤10 entries AND consulting revenue unchanged"}
anti_scope:
  - "engineering correctness of agent files (engineering-expert)"
  - "epistemic claims about FPF quality (philosophy-expert)"
  - "multi-axis improvement ranking beyond capital-return (mgmt-expert)"
  - "system model of compounding feedback loop (systems-expert)"
  - "Ruslan investor letter composition (writing-support only; HITL composes)"
provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "25-126", quote: "compounding has not yet run on a real task [ROY-AGENTS-BUILT:160-170]"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "50-52", quote: "Golden sets per cell are empty ... 400 labels minimum, none authored"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/beta-current-agents.md", range: "213-227", quote: "investor §6.0 names €50K baseline / €200K / ... DIFFERENT from the 4 other experts"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md", range: "46-49", quote: "architecture is a contract, not a running machine"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md", range: "132-143", quote: "swarm/wiki/graph/edges.jsonl is 4 lines, all # comments ... no typed-BFS implementation"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/delta-memory-sota.md", range: "34-35", quote: "Five are implementable under Phase-A Max-subscription lock ... Four require Phase B"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md", range: "50-55", quote: "α-3 state machine ... never fired ... swarm/wiki/skills/ are empty"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md", range: "72", quote: "highest-ROI missing per SYNTHESIS:167-175 ROI-table item 5 + 'the money step'"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "93-100", quote: "MP-1 ... Jetix is over-specified and under-executed"}
  - {path: ".claude/agents/investor-expert.md", range: "1150-1158", quote: "€50K baseline / €200K / €1M / $100M / $1T ... BOSC-A-T-X trigger per gate"}
confidence: medium
confidence_method: judgment + arithmetic
escalations: []
dissents:
  - claim: "The swarm investment is worthwhile even without pre-committed metrics because the first cycle itself produces measurement infrastructure."
    F: F4
    ClaimScope: holds if the current cycle (T-swarm-self-improve-v1) outputs the convergence metric spec as an accepted artefact before the cycle closes.
    R:
      accepted_if: convergence metric (binary predicate at cycle_10) is written and accepted as a gate artefact before this cycle closes.
      refuted_if: convergence metric not written; cycle closes with only improvement recommendations but no acceptance predicate for Phase A.
    source: investor-expert integrator-lens (alternative framing of Alternative C)
```
