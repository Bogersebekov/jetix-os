---
task_id: swarm-self-improve-v1
date: 2026-04-23
status: task-brief-ready
operating_mode: Stage-Gated
target_executor: Jetix swarm (brigadier + 5 experts) on server
estimated_duration: 6-10 hours (2 gates)
issued_by: Ruslan
---

# TASK — Swarm Self-Improvement v1 (First Real Swarm Cycle)

## Mission

Read the existing Jetix research corpus about agent construction, wiki
infrastructure, memory patterns, and skills. Assemble a task-scoped
wiki under this task. Generate concrete hypotheses about how to
**double the quality of the current Phase A swarm** using insights
from this corpus. Distil hypotheses into **≥5 implement-now
opportunities** with concrete action plans. Deliver as multiple
documents Ruslan will review and pick which to implement.

**Primary goal:** not just read — **synthesise + generate
implementable improvements**. Don't produce a literature summary;
produce a punch-list of concrete upgrades to brigadier + 5 experts +
wiki v3 + skills infrastructure.

**Secondary goal:** validate the swarm actually works. This is the
first real swarm cycle. Matrix 5×4 must demonstrably activate (≥4
cells × ≥2 modes). Task-scoped wiki assembly (W-7, Layer α) must
happen. Two-level Compound Engineering (W-5) — per-agent Level-1
compound + system-level Level-2 meta-compound — must execute and
leave traces in `swarm/wiki/meta/agent-improvements/`.

## Inputs — what to read (tiered)

### Tier 1 — PRIMARY (deep read, cite extensively)

**Agent construction research corpus (the blueprints that built you):**
```
decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md  (26K words, 6 parts)
decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md  (18 E-items, 5 alphas)
prompts/step-2-2-4-agent-construction-2026-04-23.md  (construction prompt)
decisions/ROY-AGENTS-BUILT-2026-04-23.md  (final consolidation)
```

**The 6 agent files themselves (current state — what's being improved):**
```
.claude/agents/brigadier.md  (1005 lines)
.claude/agents/engineering-expert.md  (989 lines)
.claude/agents/mgmt-expert.md  (1530 lines)
.claude/agents/systems-expert.md  (1562 lines)
.claude/agents/philosophy-expert.md  (1462 lines)
.claude/agents/investor-expert.md  (1529 lines)
```

**Wiki v3 architecture (the memory your improvements land in):**
```
design/ROY-WIKI-V3-GOALS-2026-04-23.md  (W-1..W-12, 12 decisions)
decisions/WIKI-V3-MECHANICS-2026-04-23.md  (Q1..Q9, R1..R8, T1..T5)
design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md  (4730 lines, 12 deliverables)
```

**Memory research (best patterns for agent memory):**
```
raw/research/knowledge-architecture-deep-research-2026-04-19.md  (828 lines, Parts A-F covering Karpathy/GraphRAG/HippoRAG/MemGPT/Mem0/Zettelkasten/Tiago Forte BASB)
raw/articles/karpathy-llm-wiki-gist-2026-04.md
```

**Skills research (best skill patterns + current skill inventory):**
```
raw/research/compounding-engineering-2026-04-22/R-1.md ... R-11.md  (11 files)
raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md
.claude/skills/README.md  (symlink convention)
.claude/skills/ingest.md
.claude/skills/ask.md
.claude/skills/lint.md
.claude/skills/compile.md
.claude/skills/consolidate.md
.claude/skills/build-graph.md
.claude/skills/search-kb.md
.claude/skills/sweep-notion-bank.md
.claude/skills/plan-day.md
.claude/skills/close-day.md
.claude/skills/focus.md
```

### Tier 2 — CONSTRAINTS (respect, do not re-open)

```
decisions/ROY-ALIGNMENT-2026-04-22.md  (5×4 matrix, Stage-Gated, Max subscription)
design/ROY-BUILD-LOGIC-2026-04-23.md  (location + communication + launch)
raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md  (Locks D1-D8)
raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md  (Locks D9-D18)
raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md  (Locks D19-D24)
swarm/lib/shared-protocols.md  (runtime contract)
swarm/wiki/foundations/swarm-alphas.md  (5 alpha state machines)
```

### Tier 3 — OUT OF SCOPE

- `raw/books-md/` (393 books) — Phase B fuel, **do not read** in this task
- External web — no WebSearch, no WebFetch
- Architecture variants V1-V5 (legacy 12-agent pattern, rejected)
- Business-domain research (consulting, sales, community, etc.)

## What to produce — 3 deliverable documents

### Document 1 — Hypotheses list (broad, before filtering)

**File:** `decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md`

**Content:** structured list of improvement hypotheses across 4 target
dimensions. Each hypothesis has:
- One-line statement
- Source evidence (which research + which section)
- Current state observation (what's there now)
- Proposed improvement
- Expected impact rating (1-5)
- Effort rating (1-5)
- Risk rating (1-5)
- Which existing locked decision it touches (if any)

**Target count:** 25-50 hypotheses across 4 dimensions:
- Agents (brigadier + 5 experts) — system prompt improvements, mode activation, shared protocol gaps
- Wiki v3 — layer structure, retrieval, provenance, write protocol, edge enum
- Memory — strategies.md pipeline, Compound step, agent-improvements layer usage
- Skills — missing skills, better versions of existing skills, SOTA patterns not yet adopted

### Document 2 — 5+ Implement-Now Opportunities

**File:** `decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md`

**Content:** top 5-8 implement-now opportunities distilled from hypotheses.
Each opportunity:
- Name + 1-sentence pitch
- Problem it solves (observed from current state)
- Proposed implementation (concrete files to edit, diffs conceptualised)
- Expected 2× improvement claim with measurable criterion
- Implementation effort estimate (hours)
- Dependencies / prerequisites
- Which locked decision(s) it honors or touches
- Risk of regression + mitigation
- Phase-A feasibility (implement now) vs Phase-B (defer) classification

**Constraint:** each opportunity must be implement-now (Phase A), not
Phase-B deferrals. Opportunities requiring Tier 4 books → flag + defer.

### Document 3 — Task-scoped wiki contents (assembled during work)

**Path:** `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/`
- `context/` — domain-filtered material extracted from Tier 1 sources
- `artefacts/` — expert outputs (each cell invocation produces one)
- `decisions/` — brigadier integration decisions
- `open-questions.md` — anything flagged for Ruslan

This demonstrates task-scoped wiki assembly per W-7 (Layer α). Must be
populated during Phase 1/2 reads, referenced during integration.

### Side-effect — agent-improvements writes

Per W-5 Level-2 Compound Engineering: brigadier writes 1-3 entries to
`swarm/wiki/meta/agent-improvements/<expert>-improvements.md` files
based on patterns observed during this cycle (not the hypothesis list
from Document 1 — those are proposals; this is observations about how
the cells behaved during this very run).

## How the swarm operates on this task

### Phase 1 — Parallel deep reads (6 sub-agents)

Brigadier spawns 6 concurrent sub-agents (single message, multiple Task
calls). Each has a specific extraction brief:

- **Sub-agent α** — Agent construction corpus: master synthesis +
  FPF enhancement + agent construction prompt + ROY-AGENTS-BUILT.
  Extract: what's good, what's thin, what could be 2× better.
- **Sub-agent β** — 6 current agent files themselves. Extract:
  section-by-section observations about current state. Flag
  weaknesses, gaps, redundancies across 6 files.
- **Sub-agent γ** — Wiki v3 architecture (goals + mechanics + spec).
  Extract: which deliverables are theoretical vs implemented, where
  gaps exist, what retrieval / write / edge patterns could be
  strengthened.
- **Sub-agent δ** — Memory research (knowledge-architecture + karpathy).
  Extract: SOTA memory patterns NOT yet adopted in Phase A (e.g.,
  HippoRAG PPR deferred, Mem0 lazy decay, Tiago Forte CODE loops,
  sleep-time compute).
- **Sub-agent ε** — Skills research (CE R-1..R-11 + SYNTHESIS) +
  current 11 skills in `.claude/skills/`. Extract: missing skills
  (e.g., CE canonical /plan /work /review /compound /lfg /
  resolve_pr_parallel), existing skill weaknesses, skill-learning
  pipeline gaps.
- **Sub-agent ζ** — Cross-pollination. Given the other five
  extractions: identify emergent improvement ideas that appear when
  memory + skills + agents insights combine. Flag unexpected
  combinations.

Each sub-agent produces a structured extraction in
`swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/` with
provenance.

### Phase 2 — Hypothesis generation (matrix 5×4 demo)

**Round 1 — 5 critics in parallel** (one cell per expert × critic mode):
each expert criticises the current state **in its own domain**:

- `engineering × critic` — technical weaknesses in current 6 agents +
  wiki implementation
- `mgmt × critic` — process / workflow / PM-lens weaknesses
- `systems × critic` — systems thinking gaps, feedback loop failures
- `philosophy × critic` — epistemic weaknesses, unfalsifiable claims
- `investor × critic` — capital-allocation-of-swarm-attention issues

Each writes to `artefacts/<expert>-critic-01.md`.

**Round 2 — 5 optimizers in parallel**: each expert proposes
simplifications / improvements in its own domain. Writes to
`artefacts/<expert>-optimizer-01.md`.

**Round 3 — 2-3 integrators** (pick best-fit experts): synthesise
critic + optimizer outputs into unified hypothesis list. Writes to
`artefacts/<expert>-integrator-01.md`.

**This is the matrix 5×4 demonstration.** ≥4 cells × ≥2 modes must
fire. If the swarm doesn't naturally get there, the test is failing.

### Phase 3 — Hypothesis filtering → Opportunity distillation

Brigadier collects all hypotheses from Phase 2, scores each against:
- Impact (1-5)
- Effort (1-5)
- Risk (1-5)
- Phase-A feasibility

Filters to top 5-8 Phase-A implement-now opportunities. Optional
scalability-architect invocation on top candidates (Phase 3 gate on
long-term compound effect).

### Phase 4 — Gate 1 (hypothesis review)

Brigadier commits `decisions/AWAITING-APPROVAL-swarm-self-improve-gate1-2026-04-23.md`
summarising:
- Hypothesis count per dimension (agents / wiki / memory / skills)
- Top 10 hypotheses by impact × effort
- Recommendation: which to carry into opportunity distillation
- 4 possible responses (approve / redirect / drill-down / abort)

**Pause. Await Ruslan ack.**

### Phase 5 — Opportunity drafting (post-Gate-1 approval)

Brigadier finalises Document 2 (5+ opportunities). Each opportunity
receives:
- Integrator mode pass for coherence
- Optionally: scalability-architect mode pass for Phase-3 defense

### Phase 6 — Gate 2 (opportunity approval)

Brigadier commits `decisions/AWAITING-APPROVAL-swarm-self-improve-gate2-2026-04-23.md`
with the full opportunity list. Ruslan picks which to implement.

**Pause. Await Ruslan ack.**

### Phase 7 — Compound step

Once Ruslan approves Document 2: brigadier runs Compound step.
- 1-3 Level-1 rules per cell that fired → written to appropriate
  `agents/<expert>/strategies.md`
- 1-3 Level-2 system observations → written to
  `swarm/wiki/meta/agent-improvements/<target>-improvements.md`
- Cycle log written to `swarm/wiki/operations/T-swarm-self-improve-v1-2026-04-23/cycle-01.md`

### Phase 8 — Cycle closure

Brigadier commits `[decisions] SWARM-SELF-IMPROVE-v1 — cycle complete,
N opportunities approved, compound applied` and halts. Ruslan decides
next step separately (implement one or more opportunities = new
cycles).

## Operating mode: Stage-Gated

Two mandatory gates (Phase 4 + Phase 6). Brigadier does not proceed
past either gate without Ruslan's ack.

Default ack inline (`ack A`). Redirect / drill-down / abort available
as alternatives per shared-protocols §4.

Cost: Max subscription, `unset ANTHROPIC_API_KEY`, tmux session.

## Constraints

- Matrix 5×4 must demonstrably activate (≥4 cells × ≥2 modes fired)
- Task-scoped wiki must physically exist at
  `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/`
- Every opportunity must cite ≥1 Tier-1 source
- Every hypothesis must have measurable impact claim
- No Tier 4 book reads
- Respect all locked decisions: 24 Locks, W-1..W-12, Q1..Q9, R1..R8,
  T1..T5, FPF E-1..E-18, ROY-AGENTS-BUILT disposition
- 14 legacy agents untouched
- v2 `wiki/` untouched

## Success criteria

1. 3 deliverables produced: Hypotheses / Opportunities / task-scoped wiki
2. ≥25 hypotheses generated across 4 dimensions
3. ≥5 Phase-A-implementable opportunities distilled
4. Both gates passed (Ruslan-acked)
5. Compound step applied (Level-1 + Level-2 writes visible in git)
6. Cycle log committed
7. Matrix 5×4 demonstration: git history shows ≥4 × ≥2 cell invocations
8. Task-scoped wiki populated (context / artefacts / decisions / open-questions)
9. Agent-improvements files received ≥1 new entry each (Level-2 Compound)
10. No locked decision re-opened

## What to do if stuck

Per shared-protocols §4 HITL escalation: write AWAITING-APPROVAL-*.md
with context / options / recommendation / risk. Do NOT abandon.

---

**Begin with Phase 1: spawn 6 parallel sub-agents.**

Branch: `claude/jolly-margulis-915d34`.
