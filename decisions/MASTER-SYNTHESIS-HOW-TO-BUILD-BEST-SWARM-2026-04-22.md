---
title: Master Synthesis — How to Build the Best Swarm 2026
date: 2026-04-22
status: draft (Part 1 drafted; Parts 2-6 pending)
target: decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md
branch: claude/jolly-margulis-915d34
phase: A (baseline swarm creation)
scope: Tier 1 deep + Tier 2 constraints + Tier 3 skim; Tier 4 books explicitly excluded
inputs:
  - raw/research/step-2-1-extractions/EXTRACTION-A-ontology-R1-R6.md
  - raw/research/step-2-1-extractions/EXTRACTION-B-evidence-R7-R11-synthesis.md
  - raw/research/step-2-1-extractions/EXTRACTION-C-market-perplexity.md
  - raw/research/step-2-1-extractions/EXTRACTION-D-pm-product-mgmt.md
  - raw/research/step-2-1-extractions/EXTRACTION-E-constraints-24-locks.md
  - decisions/ROY-ALIGNMENT-2026-04-22.md
  - decisions/ROY-INFORMATION-DIET.md
  - decisions/JETIX-ARCHITECTURE-BRIEF.md
  - raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md
  - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md
  - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md
parts:
  - 1-ontology
  - 2-evidence
  - 3-anti-patterns
  - 4-jetix-matrix-patterns
  - 5-implementation-primitives
  - 6-testing-validation
citation_convention: "file § anchor" where file is shorthand (R-1..R-11, SYNTHESIS, Every, EXEC, RESULT-05/06/07, ALIGN, DIET, PRE, ST2, ST2B, Brief) and anchor is section/§/Q number; sub-agent extractions cited as EXT-A..EXT-E.
---

# MASTER SYNTHESIS — HOW TO BUILD THE BEST SWARM 2026

**Purpose.** Blueprint for the Jetix baseline swarm (5 domain experts × 4
role-modes + 1 brigadier), written to enable system-prompt drafting without
further research. Evidence-dense, citation-annotated, anti-pattern-aware.
Every Tier-1 claim traces back to a specific source file and section; every
Jetix-specific term is explicitly labelled as a synthesis.

**Structure.** Six parts: Ontology (conceptual vocabulary), Evidence
(production patterns), Anti-patterns (failure modes + prevention),
Jetix-specific patterns (5×4 matrix in full), Implementation primitives (how
to write the prompts), Testing & validation (smoke, eval, regression).

**Reading guidance.** The compliance-check matrix in Part 4 and Part 5
verifies every claim against the 24 Locked decisions; tensions are flagged,
not papered over. Russian is used only for verbatim Ruslan voice-anchors;
technical prose is English.

---

# PART 1 — ONTOLOGY

## 1.0 Orientation

A swarm is a coordination device, not a buzzword. This ontology fixes the
vocabulary before anything else in the blueprint is written. Three sources
of drift are eliminated up-front:

1. **Marketing overload.** The word "swarm" is routinely applied to
   hierarchical hub-and-spoke systems that share none of the classical
   swarm's defining properties. We use it only in the strict sense and
   provide the production-accurate term (multi-agent system) for the
   non-strict case. See §1.1.
2. **Jetix-internal terms that are not attested in Tier-1 research.**
   "Brigadier / expert / role-mode", "matrix 5×4 pattern", "termination
   stack as a unified 4-layer concept", "stage-gated vs full-auto",
   "mailbox", "attention budget" — none appear verbatim in R-1..R-11 or
   Perplexity. They are labelled here as Jetix synthesis and grounded on
   the closest evidence-backed neighbours (EXT-A §5 notes). This is
   deliberate: downstream prompt writers must know when they are deploying
   a well-attested primitive versus when they are extending vocabulary.
3. **False precision.** Where a number is given (e.g., Rule of 4 peaks at
   3–4 agents), we cite the study; where a value is Jetix-chosen (e.g.,
   maxTurns = 15), we label it as an operational starting point to be
   calibrated, not a derived optimum.

Every term below carries: (a) synthesized definition; (b) primary source
attribution; (c) example from source; (d) relations to adjacent terms;
(e) Jetix-applicability note. Terms unattested in Tier-1 carry an
`[unattested in Tier-1]` marker and an explicit grounding proposal.

---

## 1.1 Swarm (strict) vs "swarm" (marketing)

**Definition.** A *strict* swarm (Bonabeau/Dorigo/Theraulaz 1999, relayed
R-2 §1.1) requires three simultaneous properties: decentralized control,
relative agent homogeneity, and global behaviour emergent from local rules
"unknown to the individual agents." Production "swarm" usage in 2024–2026
is almost uniformly a marketing overload: R-2 §1.2 concludes that *none*
of the reviewed frameworks — OpenAI Swarm, CrewAI, claude-flow, LangGraph
Supervisor, MetaGPT — satisfies the triple constraint. OpenAI's own
"Swarm" project has been deprecated (EXT-C §3). The correct production
term is **multi-agent system (MAS)** with a specified topology.

**Example.** *"ruvnet/claude-flow calls itself a 'hive-mind' while
implementing queen-led hierarchical coordination — the architectural
opposite of decentralization"* (R-2 Exec Summary, via EXT-A §1 term 1).

**Relations.** Multi-agent system, stigmergy, hub-and-spoke, homogeneity.

**Jetix-applicability.** Jetix is not a strict swarm. It is a hub-and-spoke
multi-agent system with stigmergic substrate. The term "roy" is used
colloquially by Ruslan; the documentation should keep "swarm" for
communication but qualify as "swarm (production sense: hub-and-spoke MAS
with stigmergic coordination)."

---

## 1.2 Multi-agent system (MAS), sub-agent, fan-out, hub-and-spoke

**Multi-agent system.** Wooldridge (via R-2 §1.1): "an agent is a computer
system capable of autonomous action… Social ability is interaction via
cooperation, coordination, and negotiation." The Jetix swarm is a MAS in
this sense.

**Sub-agent (Claude Code sense).** A separate Claude invocation in a fresh
context window with scoped tools, defined via `.claude/agents/*.md`,
invoked by a parent; crucially, *sub-agents cannot spawn further
sub-agents* (R-3 §3.1 Case 1; EXT-A §1 term 2). Only the prompt string
passes down and only the final message returns (R-7 §5.1).

**Fan-out.** Parallelizing the same parametric task. Canonical example:
*"`claude -p "Migrate $file"` shell loop for 2,000 files"* (R-2 §4.3 item
4). Anthropic's "Best Practices for Agentic Coding" endorses this as the
simplest production MAS pattern.

**Hub-and-spoke (orchestrator-worker).** One heterogeneous lead decomposes
a task; N homogeneous workers execute with independent context windows;
lead synthesizes (R-2 §5.2 Pattern 1; R-5 §6). Anthropic's own
multi-agent Research: *"one Opus 4 lead agent receives the query… Sonnet 4
subagents run in parallel with independent context windows… They do not
communicate with each other"* (R-2 §5.2). Production frequency: R-2 §4.1
lists Anthropic Research, Cursor, Replit Agent, Factory, Sierra, LangGraph
Supervisor, MetaGPT all as variants of this shape. +90.2% measured lift
over single-agent Opus-4 on breadth-first research at 15× token cost
(R-9 §Q15; R-2 §3.2; EXT-B §1). It is the single most production-validated
MAS pattern.

**Relations.** Swarm (strict), stigmergy, Rule of 4, termination stack.

**Jetix-applicability.** Jetix topology = hub-and-spoke. Brigadier = hub;
5 domain experts = spokes. Each invocation of an expert × role-mode is
effectively a scoped sub-agent call (fresh context, scoped tools, prompt
in / message out).

---

## 1.3 Brigadier / expert / role-mode (Jetix terminology)

**Status.** `[unattested in Tier-1]` The three-level Jetix terminology
does not appear in R-1..R-11 or Perplexity. Closest ontological neighbours:

- **Brigadier** ≈ lead-agent / orchestrator (R-2 §5.2; Anthropic Opus lead;
  Replit "Manager Agent" R-5 §4; Devin "manager Devin" R-5 §1; Factory
  Coordinator R-2 §5.2 Pattern 2).
- **Expert** ≈ role-specialized specialist-subagent. Every ships 12+
  reviewer subagents (`ce-security-reviewer`, `ce-performance-reviewer`,
  `ce-correctness-reviewer`, `ce-kieran-rails-reviewer`, etc. — R-6 §3;
  EXT-A §1 term 3). Factory Droids (Code/Review/Docs/Test/Knowledge) are
  the closest commercial parallel (R-2 §5.2 Pattern 2).
- **Role-mode** ≈ an activation profile that reframes the same expert's
  domain lens. No Tier-1 author uses this term. Closest evidence-backed
  primitives: (a) Agent Skills progressive-disclosure via `when_to_use`
  frontmatter (R-1 §2(b); R-8 §1.1–1.3; EXT-B §1); (b) Anthropic's five
  canonical workflow patterns used as framing lenses (R-2 §4.3: Prompt
  Chaining / Routing / Parallelization / Orchestrator-Workers /
  Evaluator-Optimizer); (c) Grove's Task-Relevant Maturity (TRM) — three
  postures per task-class (RESULT-07 §A; EXT-D §1 Grove).

**Grounding proposal.** A role-mode is an **activation profile inside a
domain-expert system prompt** that (1) selects a subset of canonical
sources to prioritise, (2) selects a subset of decision heuristics, (3)
selects a rubric (critic rubric vs optimizer rubric etc.), and (4)
applies a calibrated TRM-style posture (structured / supportive /
objective). Implementation: a `mode: critic | optimizer | integrator |
scalability` parameter in the Task invocation triggers an `if mode == X`
branch in the system prompt that reveals the relevant sub-sections.

**Jetix-applicability.** See Part 4 for full treatment. In short: 5 domain
experts × 4 role-modes = 20 invocation cells; brigadier sits outside the
matrix.

---

## 1.4 Stigmergy, shared environment, mailbox, wiki-based coordination

**Stigmergy.** Grassé 1959 (via R-2 §1.3): coordination via cumulative
modification of a shared medium, without direct agent-to-agent
communication. Four properties: no direct comms; coordination via
environmental modification; self-organization; environment = both
communication medium *and* work product.

**Shared environment in AI practice.** CLAUDE.md + filesystem + git are
the dominant pheromone layer. Boris Cherny (R-2 §1.4; EXT-A §1 term 4):
*"Our team shares a single CLAUDE.md… we commit it to git… whenever Claude
behaves incorrectly, we add a note to CLAUDE.md so it learns not to repeat
the mistake."* CrewAI's `Memory` class and claude-flow's SQLite pheromone
store with typed TTLs (R-2 §1.4 Examples 2–3) are explicit stigmergic
designs. R-10 §7.1–7.2 and Karpathy's LLM Wiki (April 2026) endorse
file-based semantic memory as "the dominant production pattern as of
2025–2026" (EXT-B §1).

**Artifact pattern.** Anthropic production primitive (R-2 §5.1, §4.3;
EXT-A §1 term 9): *"Subagents call tools to store their work in external
systems, then pass lightweight references back to the coordinator…
prevents information loss during multi-stage processing."* This is how
stigmergy is implemented at subagent boundaries when full message-passing
would blow up context.

**Mailbox.** `[unattested in Tier-1 with this label]` The Jetix mailbox
pattern (JSONL files in `comms/mailboxes/{agent}.jsonl`) is a legitimate
stigmergic substrate *provided* mailboxes are: (a) append-only; (b)
git-tracked; (c) carry provenance headers (see §1.9). The closest
Tier-1 analogues are (i) append-only session logs in Anthropic Managed
Agents (R-1 §3 table; EXT-A §1 term 4); (ii) artifact-pattern filesystem
writes; (iii) CrewAI Memory + TTL decay. A mailbox with these three
properties passes R-2 §1.3's stigmergy definition; without them, it
degenerates into direct messaging that Yan (June 2025, R-9 §Q14;
EXT-B §2) warns against.

**Wiki-based coordination.** `[unattested as a term]` Closest: Devin Wiki
auto-indexed repos (R-5 §1); Every's AGENTS.md-as-shared-state; Karpathy
LLM Wiki (April 2026, EXT-B §1). The Jetix `wiki/` directory with
filesystem-as-SoT (Lock 17) + typed edges + niche symlinks per agent
implements this pattern with stronger provenance than any Tier-1
analogue.

**Relations.** Memory accumulation, artifact pattern, fungible agent,
provenance.

**Jetix-applicability.** Stigmergy is the primary coordination substrate.
Mailboxes carry events (append-only JSONL); wiki carries accumulated
knowledge (markdown + edges.jsonl). Experts do not ping each other
directly; they write to mailbox / wiki and the brigadier composes.

---

## 1.5 Compounding Engineering (CE) and the Plan–Work–Review–Compound loop

**Definition.** Coined by Kieran Klaassen, popularized by Dan Shipper at
Every Inc. (R-1 §1.2; R-6 §3 Q5; Every §Main Loop): *"each unit of
engineering work should make subsequent units easier — not harder."* The
canonical four-step loop: **Plan → Work → Review → Compound**, with
time allocation approximately 40/10/40/10 and the Every "80/20 rule"
(plan + review ≈ 80% of wall-clock; work + compound ≈ 20%). The fourth
step (Compound) is "the money step" — codifying learnings into
agent-readable instructions.

**Canonical Every example.** Cora (Every's AI email chief-of-staff)
feature velocity moved from >1 week to 1–3 days; inference cost per user
fell from $25–35/mo to <$5/mo; PRs from days to hours (Every guide; R-6;
EXT-B §1). The `/ce-compound` command writes Error → Rule → Skill
pipelines into `AGENTS.md`; `/ce-learnings-researcher` pulls rules
forward when a subsequent task matches (R-6 §3 Q5 Step 3).

**Boris Cherny endorsement.** R-1 §1.1: *"[@claude on PRs to update
CLAUDE.md] is our version of @danshipper's Compounding Engineering."*

**Shipper verbatim (R-6 §4 Q8).** *"In compounding engineering, your goal
is to make sure that each feature makes the next feature easier to build.
We do that in this loop. The loop has four steps… the last step which is
I think the most interesting one is codify."*

**Metric.** Verification loops give 2–3× quality gain (Boris, R-7 §6.1;
EXT-B §1). Error → Rule → Skill: Anthropic self-rewriting tool-desc agent
achieved −40% task completion time for future agents (R-1 §2(d); EXT-A §1
term 5).

**Constraint.** CE was designed for greenfield small-team Rails/TS; HN
evidence (R-6 §6; EXT-A §3) shows degradation on legacy spaghetti
codebases. At Jetix scale the loop is intended to be fractal — the *same*
Plan-Work-Review-Compound applied inside each expert invocation and
across the overall brigadier cycle.

**Relations.** System Prompt Learning (R-3 §2.1), error→rule→skill
pipeline, verifier (§1.7), Shape Up outer cycle (RESULT-05 §A; EXT-D §1).

**Jetix-applicability.** CE is the **inner loop** that every expert runs,
and also the **outer loop** that the brigadier runs across a task. Part 5
details both loops and their nesting inside Shape Up.

---

## 1.6 Rule of 4, context window, context rot, attention budget

**Rule of 4.** Kim et al. arXiv:2512.08296 (260 agent configurations,
relayed R-2 §3.5; R-1 §6.2; EXT-A §1 term 6): under current token
economics, effective multi-agent team sizes peak at 3–4 agents; additional
agents yield diminishing or negative returns. β = −0.408, p < 0.001.
Aggregate mean across 180 DeepMind experiments: **−3.5% multi-agent vs
single-agent** (95% CI [−18.6, +25.7], σ = 45.2%). A "45% capability
ceiling" is observed: once a single-agent baseline exceeds ~45% accuracy
on a task, adding agents tends to hurt (EXT-B §1; EXT-C §2). Qian et al.
(R-2 §3.5) extend: logistic scaling on DAG topologies saturates around
2⁴ = 16 agents but only in closed-verification regimes.

**Context window (Apr 2026).** Claude Opus 4.7 / Sonnet 4.6: 1M tokens;
Haiku 4.5: 200K (R-1 §6.1; EXT-A §4).

**Context rot.** Accuracy decreases as context length grows, even well
inside nominal limits; all 18 frontier models in Chroma 2025 study
degrade (R-10 §5.2; EXT-B §3). Folkman Oct 2025: CLAUDE.md summarization
from 18,282 → 122 tokens at step 47 drove accuracy 66.7% → 57.1% (R-3
§6.1.6; EXT-A §3).

**Attention budget.** `[unattested as a term]` Jetix framing. Grounded on
three empirical primitives:
1. **Rule of 4** for agent count per task.
2. **5–10 tools per agent** optimum (LangGraph evidence, R-1 §6.2);
   ≥16 tools is where every MAS underperforms single-agent (EXT-C §5).
3. **Context window target <100 lines** for root CLAUDE.md (Tian Pan);
   <60 (HumanLayer); <200 (Anthropic internal) — compliance degrades
   past ~150–200 lines (R-8 §2.3; EXT-B §1).

The attention budget of a swarm is the composite of these limits:
agents × tools × context size × task depth. Exceeding any one produces
measurable quality loss.

**Relations.** MAS saturation, coordination overhead, context collapse
(§1.7 termination layer 4), compaction anti-pattern (Part 3).

**Jetix-applicability.** The 5-expert baseline sits exactly on the Rule
of 4 knee (one over). This is tolerable because (a) experts are
heterogeneous by design — each owns a distinct domain with non-overlapping
canonical sources (see Part 4); (b) only a subset is invoked per task;
(c) the matrix role-mode mechanism effectively yields 20 narrow
activation profiles, each of which is a focused specialist, keeping any
single invocation well inside the tool/context limits.

---

## 1.7 Termination stack (four layers)

**Status.** `[unified concept unattested in Tier-1]` Each layer is
individually attested; the 4-layer stack is a Jetix synthesis.

**Layer 1 — maxTurns / max-message.** AutoGen's `MaxMessageTermination`
and `TextMentionTermination("APPROVE")` / `FunctionCallTermination`
(R-3 §3.1 Case 3; EXT-A §1 term 7). Devin uses 45-min caps on SWE-bench
runs (R-5 §1). Proposed Jetix defaults (Part 5): Plan mode ≤10; Work
mode 15–30 depending on domain; Review ≤25; Compound ≤12.

**Layer 2 — Budget.** Explicit token/ACU/spend budget. Devin 2.0: 1 ACU
≈ 15 minutes at $2.25 (R-5 §1). Anthropic multi-agent = 15× chat tokens,
~4× single-agent loop (R-9 §Q11; EXT-B §4). SWE-Effi Token Snowball:
failed runs burn 8.8M tokens vs success 1.8M (4.9× cost premium, 18×
cost/quality differential; R-9 §Q11). In Jetix's Max-subscription cost
model, budget is measured in **turns and session duration**, not $
(ALIGN §6; see §1.10).

**Layer 3 — Verifier / evaluator-optimizer / judge.** A machine-verifiable
predicate closes the loop. Anthropic Inspector pattern: 96.4% error
recovery (R-2 §3.6). Boris Cherny: *"Claude performs dramatically better
when it can verify its own work"* (R-1 §2(f)) — 2–3× quality gain.
Hamel Critique Shadowing for judge calibration (R-11 §4; EXT-B §1):
binary pass/fail, one criterion per call, ≥20–30 domain labels. Without
a verifier, independent MAS amplifies errors 17.2× over single-agent
baseline (R-1 §5.2; R-2 §3.6).

**Layer 4 — HITL (human-in-the-loop).** Five-point spectrum (R-3 §3.3;
EXT-A §1 term 7): manual rules → skills (AI-drafts, human-approves) →
closed-env autonomy (Voyager) → structurally-constrained (Letta
sleep-time) → fully autonomous (AutoGPT/BabyAGI — *failed*). Anthropic's
own practice caps fully-autonomous delegation at 0–20% (EXT-C §1, §5).
Willison's Lethal Trifecta / Meta's Rule of Two (R-4 §3.1; R-3 §6.1.8):
agents should satisfy at most two of {private data, untrusted input,
external communication}.

**Termination-stack invariant.** Every Jetix agent invocation has *all
four* layers set. A missing layer is a bug. Part 5 specifies the
YAML-frontmatter template that enforces this.

**Jetix-applicability.** Covered in full in Part 5 §implementation.

---

## 1.8 Matrix agent pattern (5 × 4) — Jetix-specific

**Status.** `[unattested in Tier-1 as a named pattern]` The Jetix 5×4
matrix — 5 domain experts × 4 role-modes = 20 invocation cells, with a
brigadier outside the matrix — is a synthesis grounded on four Tier-1
neighbours (EXT-A §1 term 8; ALIGN §3):

1. **Every's CE plugin** ships 26–50 agents × 23–42 skills × 12+ reviewer
   sub-agents — multi-dimensional by construction (R-1 §2(b); R-6 §3 Q5).
2. **Claude Code's 5-primitive composition.** Skills / Agents / Hooks /
   Plugins / MCP = a 5-primitive layer (R-5 §6 table; R-8). Any of the
   five primitives can be scoped to a role-mode.
3. **Anthropic's five canonical workflow patterns.** Prompt Chaining /
   Routing / Parallelization / Orchestrator-Workers / Evaluator-Optimizer
   (R-2 §4.3; R-5 §6). These map loosely onto the 4 role-modes:
   Evaluator-Optimizer ↔ critic; Parallelization ↔ optimizer across
   candidates; Orchestrator-Workers ↔ integrator; Routing ↔ scalability.
4. **Factory AI Droids.** Coordinator + 5 role-scoped specialists
   (Code / Review / Docs / Test / Knowledge) — a production 1+5 structure
   at commercial scale (R-2 §5.2; EXT-C §1).

**Grounding proposal.** The matrix is: one axis = domain (engineering /
mgmt / systems / philosophy / investor), one axis = role-mode
(critic / optimizer / integrator / scalability-architect). The two axes
are orthogonal: domain = *what canonical sources I own*; role-mode =
*what lens I apply*. Same expert in different modes returns different
outputs because the activation profile changes the rubric, not the
knowledge base.

**Critical tension to acknowledge.** Walden Yan (Cognition, June 2025;
R-9 §Q14; EXT-B §2): *"In 2025, running multiple agents in collaboration
only results in fragile systems. The decision-making ends up being too
dispersed and context isn't able to be shared thoroughly enough."* Yan's
two principles: (1) share FULL traces not summaries; (2) actions carry
implicit decisions. Reconciliation with Anthropic's +90.2% multi-agent
lift (R-9 §Q15): *parallel review of a single artifact is safe; parallel
code generation that hands off summaries is the Flappy Bird trap.* The
Jetix matrix survives this critique if and only if:

- Matrix invocations that pass results to other cells pass **full traces**
  (artifact files, not summaries).
- The brigadier reads **full** expert outputs, not compressed recaps.
- Compound step writes to append-only structured entries (ACE pattern,
  R-3 §6.1.6; +10.6% improvement) rather than summarizing into CLAUDE.md.

**Relations.** Brigadier, role-mode, Agent Skills, canonical Anthropic
patterns.

**Jetix-applicability.** Full treatment in Part 4.

---

## 1.9 Stage-gated vs Full-Auto mode

**Status.** `[exact labels unattested in Tier-1]` Closest evidence-backed
primitives (EXT-A §1 term 9):

- **Karpathy autonomy slider** (R-3 §4 item 5, Software 3.0 talk):
  *"Cursor Tab → Cmd+K → Cmd+L → Cmd+I (agent mode) — a spectrum of
  autonomy, not binary."* Explicit call for "partial autonomy, custom
  GUIs and autonomy sliders."
- **Anthropic Plan Mode vs Normal Mode** (R-2 §4.3): read-only plan
  review before code-writing.
- **HITL 5-point spectrum** (R-3 §3.3) and **Every's HITL-at-every-step**
  (R-6 §5 Q10).
- **Cagan empowered-team + Netflix Context-not-Control** (EXT-D §2): the
  mgmt-literature analogue — brigadier provides context, expert decides
  within role-local authority; escalation on SIP-class signals (Grove,
  RESULT-07 §A; EXT-D §1).

**Stage-Gated mode.** The swarm stops and writes
`decisions/AWAITING-APPROVAL-<topic>-<date>.md` on key architectural
decisions (ALIGN §4, §8). Gate content: context / options / recommendation
/ rationale / risk register. Ruslan responds with one of four signals:
Approve / Redirect / Drill-down / Abort (DIET §1.5). Resume on approval.

**Full-Auto mode.** Swarm runs to completion; Ruslan reviews final
output only. Reserved for smoke tests, validated patterns, well-defined
scope (ALIGN §4). **Defense in depth:** even Full-Auto invocations have
the full termination stack active (layer 4 = HITL interrupt on
irreversible ops).

**Choice rule.** Per-task decision (ALIGN §4). Default for large
architecture synthesis / first swarm launch = Stage-Gated. Default for
routine refactor or validated pattern = Full-Auto.

**Trigger list (ALIGN §8).** Stage-Gated fires on: >1-month-impact
decision, trade-off between projects/resources/directions, new framework
proposal, agent or skill add/remove, cost escalation, conflict with 24
Locks. Non-triggers: research inventory, draft synthesis, cleanup/refactor,
wiki-entry creation, routine review.

**Jetix-applicability.** This blueprint itself is being produced in
Stage-Gated mode; gate files at end of Parts 4 and 6.

---

## 1.10 Provenance, citation, evidence-based claim

**Definition.** Provenance is the traceability of every swarm-written
output (rule, wiki entry, recommendation) back to a specific observed
artefact (file, quote, metric, failure). Every rule in CLAUDE.md must
trace back to a specific observed failure (R-6 §3 Q6; EXT-A §1 term 9).

**Mechanisms attested in Tier-1.**
- **Code citations in agent output.** Factory Knowledge Droid indexes
  repos with code citations; Devin Search offers natural-language
  codebase queries with code citations (R-3 §5.1 Case 8; R-5 §1).
- **Artifact pattern** (§1.4): subagents write to external storage;
  lightweight references pass back to coordinator (R-2 §5.1).
- **Git as ground truth** (R-2 §5.1 item 1; R-5 §3 Aider; R-5 §4 Replit
  auto-commit per step).
- **ACE append-only entries with IDs + ✓/✗ counters** — the only
  empirically-validated CLAUDE.md maintenance pattern that resists
  context collapse (R-3 §6.1.6; +10.6% accuracy).
- **YAML frontmatter** on Skills and Agent definitions (R-1 §2(b); R-8
  §1.1).

**Jetix-applicability.** Every wiki page and every rule in CLAUDE.md
carries (a) `sources:` frontmatter with at least one file path; (b)
inline `[src:filename]` at the end of claims; (c) git history tying the
entry to the commit that produced it. Compound step refuses to persist
an entry that lacks provenance (Part 5 §compound-gate).

**Relations.** Stigmergy, artifact pattern, CE Compound step, anti-patterns
of context collapse and false-memory consolidation (Part 3).

---

## 1.11 Anti-pattern, failure mode, post-mortem

**Definitions.** An *anti-pattern* is a named design/usage mistake with
recurring root cause. A *failure mode* is a class of failures (e.g.,
context collapse, sycophancy, tool-call storm). A *post-mortem* is a
public retrospective documenting a specific incident.

**Unified taxonomy.** MAST (Cemri et al. arXiv:2503.13657, 1,600+ traces,
7 frameworks — R-1 §5.2; R-2 §3.3; R-4 §2.1): 14 failure modes in 3
categories — **Specification Issues 41.77%** (unclear goals, missing
success criteria); **Inter-Agent Misalignment 36.94%** (coordination
failures, handoff losses); **Task Verification 21.30%** (no/incomplete
verification).

**Source-to-mitigation mapping.** For each Part-3 anti-pattern we provide:
root cause, detection signal, and prevention. Part 3 lists ≥15 distinct
anti-patterns; the catalog below previews the load-bearing ones:

- Flappy Bird / parallel-subagent divergence (Cognition, R-1 §5.1)
- Summary-passing fragility (Yan, R-9 §Q14)
- Context compaction collapse (Folkman Oct 2025)
- Unbounded loop / $47K incident (Dev.to Mar 2026, EXT-C §4)
- 2.3M API calls retry storm (EXT-C §4)
- Replit DB wipe (Jul 2025, EXT-C §1)
- Sycophancy collapse rate 86.36% (R-4 §2.3)
- Tool-space interference (≥16 tools, EXT-C §5)
- Agent self-report unreliability (Replit, EXT-C §2)
- MCP tool poisoning / registry 32.8% staleness (EXT-C §4)

**Relations.** Termination stack (prevention layer); compliance matrix
(Part 5); smoke tests (Part 6 check against known anti-patterns).

**Jetix-applicability.** Each of the 16 Brief §7 anti-patterns and the
MAST 14 must be explicitly addressed in Part 4 (for Jetix-specific cases)
and Part 5 (for implementation primitives that prevent them).

---

## 1.12 Additional terms promoted to first-class

Three more terms are load-bearing enough to define now rather than
introduce implicitly later:

**1.12.a Compound ledger.** The append-only record of Error → Rule →
Skill entries written during the Compound step of CE. Physically: a
structured markdown file per domain expert (`agents/<expert>/
strategies.md`) that accumulates learnings with IDs, provenance, and ✓/✗
counters per ACE (R-3 §6.1.6). Read at the Plan step of every subsequent
task. Pruned on a compound-cycle boundary via the `/consolidate` skill.

**1.12.b Two-way door.** Boris Cherny's phrase for a decision that can
be unwound without irreversible cost (R-7 §3.1; EXT-B §2). Boris's team
rewrites Claude Code from scratch ~every 3–4 weeks because every
rewrite is a two-way door. Jetix applies this: any design choice that
would require >30% refactor at a scale gate (Brief §5.1) is a one-way
door and requires Stage-Gated approval; everything else is two-way and
proceeds.

**1.12.c Skill (Claude Code sense).** A markdown file in
`.claude/skills/` with YAML frontmatter (`name`, `description`,
`when_to_use`) that implements a repeatable capability. Three-level
progressive disclosure (R-1 §2(b); R-8 §1.1–1.3; EXT-B §1): metadata
~100 tokens always loaded → body <5,000 tokens on invoke → attached
files on demand. Caps: 1,536 chars per skill; 15,000 chars total across
all skills (silent truncation past this). 20 skills therefore ≈ 2,000
tokens of overhead vs 40,000 if eagerly loaded.

---

## 1.13 Cross-reference map

To orient the prompt writer: the core terms cluster into four families.

- **Topology family.** Swarm (strict) / MAS / hub-and-spoke / sub-agent /
  fan-out / matrix 5×4 / brigadier / expert / role-mode.
- **Coordination-substrate family.** Stigmergy / shared environment /
  artifact pattern / mailbox / wiki-based coordination / provenance /
  compound ledger.
- **Loop family.** CE Plan-Work-Review-Compound / Shape Up outer cycle /
  two-way door / Compound ledger / Skill.
- **Safety family.** Termination stack (4 layers) / Stage-gated vs
  Full-Auto / HITL spectrum / Rule of 4 / attention budget / anti-pattern /
  post-mortem.

Each downstream Part references these four families to keep vocabulary
consistent.

---

## 1.14 Scope boundary — what this ontology does NOT define

Three classes of term are deliberately omitted and deferred:

1. **Domain-internal vocabulary of each of the 5 experts.** The specific
   canonical terms from Ousterhout (deep modules / strategic programming),
   Ashby (requisite variety), Cagan (four risks), Popper (falsifiability),
   Buffett (circle of competence) belong inside each expert's system
   prompt. Loading them here would collapse the tier discipline Phase A
   enforces.
2. **Business-layer vocabulary.** ICP criteria, archetypes, token-model
   options, matchmaker taxonomy — these are in Locks (Part 5 compliance
   matrix) but not ontology. They are *what Jetix does*, not *how the
   swarm is built*.
3. **UI / dashboard / notification terminology.** Reserved for Phase B+.

---

## 1.15 Summary table

| Term | Status | Primary source | Part 4/5 use |
|---|---|---|---|
| Swarm (strict) / MAS | evidence-backed | R-2 §1.1–1.2 | Topology framing |
| Sub-agent | evidence-backed | R-3 §3.1; R-7 §5.1 | Invocation mechanic |
| Fan-out | evidence-backed | R-2 §4.3; Anthropic | Smoke-test pattern |
| Hub-and-spoke | evidence-backed | R-2 §5.2; R-5 §6 | Jetix topology |
| Brigadier | Jetix term | lead-agent (R-2 §5.2) | Orchestration role |
| Expert | Jetix term | specialist-subagent (R-1 §2(c); R-6 §3) | 5 domain cells |
| Role-mode | Jetix term | Skills frontmatter + Grove TRM + Anthropic patterns | 4 activation profiles |
| Stigmergy | evidence-backed | R-2 §1.3–1.4; Grassé | Coordination substrate |
| Mailbox | Jetix term | append-only log + artifact pattern | Inter-agent events |
| Wiki-based coord | Jetix term | Karpathy LLM Wiki; Devin Wiki | Accumulated knowledge |
| CE loop | evidence-backed | R-1 §2; R-6 §3 Q5; Shipper | Inner loop |
| Rule of 4 | evidence-backed | R-2 §3.5; Kim et al. | Agent-count discipline |
| Context rot | evidence-backed | R-10 §5.2; Chroma 2025 | Context-budget limit |
| Attention budget | Jetix term | Rule of 4 + 5–10 tools + CLAUDE.md <200 | Composite budget rule |
| Termination stack (4L) | Jetix synthesis | R-3 §3.1+§3.3; R-2 §3.6; R-4 §3.1 | YAML frontmatter |
| Matrix 5×4 | Jetix synthesis | CE plugin × CC primitives × Anthropic patterns | Core design element |
| Stage-gated / Full-Auto | Jetix term | Karpathy slider + HITL 5-point | Operating-mode selector |
| Provenance | evidence-backed | R-6 §3 Q6; Anthropic artifact pattern | Compound-step gate |
| Anti-pattern / MAST | evidence-backed | MAST (Cemri et al.) | Part 3 catalog |
| Compound ledger | Jetix synthesis | CE Compound step + ACE | Per-expert state |
| Two-way door | evidence-backed | R-7 §3.1 (Boris Cherny) | Decision-reversibility rule |
| Skill (CC sense) | evidence-backed | R-1 §2(b); R-8 §1 | Role-mode implementation |

**End of Part 1.** Parts 2–6 build on this vocabulary.

---

