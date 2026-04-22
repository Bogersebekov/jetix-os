---
title: Wiki v3 Mechanics Resolver — resolve 9 open design questions
date: 2026-04-23
status: ready-for-launch
target_executor: Claude Code on server (Opus 4.7 1M, extended thinking)
estimated_duration: 1-2 hours
output: decisions/AWAITING-APPROVAL-wiki-v3-mechanics-2026-04-23.md
context: Шаг 2.2.3 Стадия B — resolve open questions before full architecture spec (Стадия C)
---

# WIKI V3 MECHANICS RESOLVER — Шаг 2.2.3 Стадия B

## Mission

Resolve **9 open design questions** about Wiki v3 mechanics by searching
existing repo documents for answers, recommending the best option per
question with evidence from those documents, and optionally proposing
new variants found during the search. The output is a **recommendations
document** that Ruslan approves — NOT the full architecture spec (that
is Стадия C).

**Scope discipline:** search existing repo content only. No external
web research. No new books. No Tier 4 book reads. Compact focused
deliverable, not sprawling research.

## Context — what's already locked

The vision for Wiki v3 is captured in
`design/ROY-WIKI-V3-GOALS-2026-04-23.md` — 12 decisions (W-1..W-12)
already locked by Ruslan. **Do NOT challenge those decisions.** Your
job is to resolve the 9 mechanics questions that sit on top of those
decisions.

Key locked decisions you must respect:
- W-1 Multi-layer architecture (9 layers hypothesized)
- W-2 Brigadier has own Wiki (Layer 2)
- W-4 Agent-improvement Wiki as separate layer (Layer 4)
- W-5 Two-level Compound Engineering (per-agent + system-level)
- W-6 Git branches as version control
- W-7 Two parallel task layers (knowledge-α + operational-β)
- W-11 Wiki = cognitive infrastructure (not storage)
- W-12 1000% depth requirement

Also respect:
- ROY-ALIGNMENT (5 experts + brigadier, matrix 5×4, Stage-Gated default)
- ROY-BUILD-LOGIC (location: `.claude/agents/` for agents + `swarm/` for runtime data; communication: Task tool + stigmergic wiki + mailbox fallback; single-session brigadier entry)
- MASTER-SYNTHESIS Part 5 §5.5 (existing wiki protocol — base layer we're extending)
- FPF-ENHANCEMENT Part 4 (5 swarm-alphas already defined) + Part 10 (preparatory artefacts specified)

## Inputs — what to read

### Tier 1 — PRIMARY (read deeply, extract evidence)

**Main knowledge architecture research (THE central source):**
```
raw/research/knowledge-architecture-deep-research-2026-04-19.md  (828 lines)
  Part A — KB patterns (Karpathy / GraphRAG / HippoRAG / MemGPT / Letta / Mem0 / Claude Code Memory / Obsidian-Logseq-Foam-Dendron / Zettelkasten / Tiago Forte BASB)
  Part B — Retrieval patterns (dense → agentic RAG / HippoRAG PPR / HyDE / long-context vs retrieval)
  Part C — Memory Systems Taxonomy (Tulving × Kahneman × AI / writeback / conflict resolution)
  Part D — KB ↔ Alpha Lifecycle Integration
  Part E — Source of truth boundaries (wiki / CRM / Projects / Decisions)
  Part F — Knowledge Compounding + writeback + insight loop
```

**Karpathy LLM Wiki canonical source:**
```
raw/articles/karpathy-llm-wiki-gist-2026-04.md
raw/notion-pages/architecture-memory-kb-karpathy-2026-04-16.md
wiki/sources/2026-04-16-architecture-memory-kb-karpathy.md
```

**Our locked vision doc (constraint):**
```
design/ROY-WIKI-V3-GOALS-2026-04-23.md  (537 lines)
```

### Tier 2 — CONTEXT (scan for current state + protocols)

**Existing wiki v2 infrastructure:**
```
wiki/overview.md
wiki/index.md
wiki/log.md
wiki/_templates/  (source, concept, entity, claim, idea, topic, experiment, summary, foundation)
wiki/graph/edges.jsonl  (current edge types)
CLAUDE.md  (Wiki Architecture v2 section — current protocol)
```

**Skills related (Wiki integration surface):**
```
.claude/skills/ingest.md
.claude/skills/ask.md
.claude/skills/lint.md
.claude/skills/compile.md
.claude/skills/consolidate.md
.claude/skills/build-graph.md
.claude/skills/search-kb.md
.claude/skills/sweep-notion-bank.md
```

**Downstream constraints (already-approved specs that wiki mechanics must fit):**
```
decisions/ROY-ALIGNMENT-2026-04-22.md
design/ROY-BUILD-LOGIC-2026-04-23.md
decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md  (focus on §5.5 wiki protocol)
decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md  (Part 4 swarm alphas, Part 10 preparatory)
```

### Tier 3 — OUT OF SCOPE (do not read)

- `raw/books-md/` (393 books) — Phase B fuel, not for this pass
- External web research
- Business-domain research files
- Levenchuk / FPF files beyond what's already summarized in FPF-ENHANCEMENT

## The 9 open questions to resolve

**IMPORTANT:** For each question, produce (a) recommended answer,
(b) evidence citations from Tier 1 sources, (c) alternatives considered
+ why rejected, (d) tradeoffs accepted, (e) applicability constraints.

### Q1 — Retrieval mechanism primary
Which retrieval approach is the default that agents use?
Candidates (per knowledge-architecture-deep-research Parts A + B):
- Filesystem grep/glob (Claude Code agentic search — §A.6 + §B.4)
- Semantic embeddings (dense retrieval — §B.1)
- GraphRAG typed graph traversal (§A.2)
- HippoRAG Personalized PageRank (§A.3 / §B.2)
- HyDE hypothetical documents (§B.5)

Constraints: Max-subscription cost model (no paid embeddings Phase A);
single-session brigadier (expensive retrieval blocks brigadier); Phase A
simplicity.

### Q2 — Write serialization model
With 9 layers, who writes to which layer?
Candidates:
- Single-writer brigadier (master synthesis default, Phase A simple)
- Per-layer owners (brigadier owns some; each expert owns own; crazy-agent owns insights)
- Hybrid (brigadier owns shared + orchestration layers; experts own own)

Constraints: Phase A simplicity; AP-18 (false memory consolidation) prevention;
W-4 (agent-improvement shared but written by multiple agents?); concurrent
write safety (no CRDT until Phase B per ALIGN §10).

### Q3 — Cross-reference format between layers
How are wikilinks + typed edges represented?
Candidates (per Part A + existing wiki v2 templates):
- Markdown wikilinks `[[concept]]` (Obsidian / existing wiki v2 style)
- YAML frontmatter typed edges (Part A.2 GraphRAG style)
- `wiki/graph/edges.jsonl` dedicated graph file (current infra)
- Combined

Constraints: existing `wiki/_templates/` use frontmatter + markdown
links; must not break existing `wiki/graph/edges.jsonl` consumers.

### Q4 — Task-scoped Wiki context population
When brigadier initializes `swarm/wiki/tasks/<task-id>/context/`,
what material is pulled automatically vs manually?
Candidates:
- Brigadier manual pick (all reasoning on brigadier)
- Auto by tags (Lock subset matching, keyword hits)
- Auto by domain-expert list (mgmt-expert invoked → pull mgmt theme-wiki)
- HippoRAG-style PPR seeded from task description (§B.2)
- Hybrid

Constraints: BUILD §4.2 already hints at brigadier populating
context/ with domain-filtered slice; FPF Part 10 specifies α-1 Task
alpha with state transitions; cost model (no paid embeddings Phase A).

### Q5 — Rot / staleness detection signals
How is a stale entry detected?
Candidates (per Part F + existing `/lint` skill):
- Time-based (not read/cited for X days)
- Version-based (superseded flag by newer entry)
- Contradiction-based (new claim conflicts existing entry)
- Manual tag (`status: stale` in frontmatter)
- Combination

Constraints: AP-3 (wiki rot) + AP-27 (KB/embedding rot) prevention;
existing `/lint` skill runs weekly; Phase A no automatic semantic
contradiction detection (would need embeddings).

### Q6 — Skill learning pipeline (from candidate → active)
Concrete flow for introducing new skills into the swarm.
Candidates (per existing `.claude/skills/` + master synthesis §5.10 + §6):
- Ad-hoc addition (file dropped in `.claude/skills/` — current v2 approach)
- Formalized: Candidate → Draft → Eval (golden-set pass) → Activation → Usage monitoring → Deprecation
- Who owns each stage? (brigadier proposes, an expert drafts, brigadier evals, activates)

Constraints: W-9 locked (skill as first-class wiki layer); skills integrate
with `swarm/wiki/skills/` layer (Layer 8); CE Plan-Work-Review-Compound
loop surrounds skill learning (§2.1.1).

### Q7 — Git branches naming convention
Final naming schema for long-horizon project iterations + forks.
Candidates:
- `roy/<task-id>/iter-v1` / `iter-v2` / `fork-<variant>`
- `roy/task-<id>/v1` (shorter)
- `roy/<project-slug>/main` + `iter/vN` + `fork/X`
- Other

Constraints: W-6 (git branches as version control); must not collide
with existing branch naming (`claude/jolly-margulis-915d34`); CI/CD
compatibility.

### Q8 — Layer 9 (Insights / Crazy-agent) Phase B activation trigger
When does crazy-agent get activated to operate on Layer 9?
Candidates:
- After N swarm cycles (e.g., 20, 50, 100)
- After theme-wiki depth threshold (e.g., 50 concepts per theme)
- After detectable cross-theme candidate density
- Manual Ruslan trigger
- Combination

Constraints: W-10 (deferred to Phase B+); structure must not preclude;
cost/complexity of running crazy-agent.

### Q9 — Existing `wiki/` top-level v2 vs new `swarm/wiki/` v3
Relationship between existing `wiki/` (Karpathy v2 — 9 entity types + edges
+ templates) and new `swarm/wiki/` v3 (9 layers).
Candidates:
- Coexist (`wiki/` unchanged, `swarm/wiki/` new; no merge Phase A)
- Migrate (move `wiki/` → `swarm/wiki/global/` or similar)
- Merge (incorporate into `swarm/wiki/` top structure)
- Hybrid (share templates + edges; separate content paths)

Constraints: existing `wiki/` has 47+ entries (per `git ls-tree`), working
skills (/ingest, /ask, /lint, /consolidate, /build-graph) depend on it;
BUILD §1.3 says not to break existing `wiki/`; W-9 says skill layer
integrates; migration cost.

## Sub-agent strategy

This is a **smaller scope** than Шаг 2.1 or Шаг 2.2.2. 3 parallel
sub-agents is sufficient.

**Sub-agent W-1** — read `knowledge-architecture-deep-research-2026-04-19.md`
full. Extract concrete evidence per Part A/B/C/F that bears on each of
Q1, Q3, Q4, Q5, Q6.

**Sub-agent W-2** — read `ROY-WIKI-V3-GOALS-2026-04-23.md` full +
`MASTER-SYNTHESIS` Part 5 §5.5 + `ROY-BUILD-LOGIC` §2–§4 +
`FPF-ENHANCEMENT` Part 4 + Part 10. Extract all locked constraints
+ already-resolved mechanics that wiki must fit. List what's fully
resolved vs partially resolved vs open.

**Sub-agent W-3** — read existing `wiki/` infrastructure (templates,
graph/edges.jsonl, overview.md, index.md, 3-5 sample entries) +
`.claude/skills/` wiki-related (ingest/ask/lint/compile/consolidate/
build-graph/search-kb). Document current protocol concretely. Extract
what would break if we migrated vs coexist.

Each returns structured extraction (≤2,500 words).

Then main agent integrates and answers each of Q1..Q9.

## Output structure

Target: `decisions/AWAITING-APPROVAL-wiki-v3-mechanics-2026-04-23.md`
Length: 3,500–6,000 words. Compact, not sprawling. Focus on answerability.

### Part 1 — Summary table

One-liner answer per question (Q1 → recommended: X; Q2 → recommended: Y;
…). Ruslan reads this first.

### Part 2 — Per-question resolution (9 sections)

For each question:
- **Question restated** (one sentence)
- **Recommended answer** (one paragraph)
- **Evidence** (citations from Tier 1 sources)
- **Alternatives considered** (bullet list, why each rejected)
- **Tradeoffs accepted** (what we give up)
- **Applicability constraint** (Phase A scope; when revisit)
- **New variants found** (if any — Ruslan wanted this explicitly)

### Part 3 — Cross-question coherence check

Do the 9 answers combine into a coherent mechanics spec? Flag any
tensions. Propose resolutions if found.

### Part 4 — Compliance with locked decisions

Explicit table: for each W-1..W-12 + ROY-ALIGNMENT items, confirm the
proposed mechanics are compliant or flag a tension.

### Part 5 — Ready-for-Стадия-C checklist

What's now resolved vs still open. What the Стадия C prompt (full
architecture spec) needs to incorporate from these decisions. If
anything else comes up during resolution that needs Ruslan's decision
before Стадия C, enumerate it here.

## Quality criteria

- Every recommendation cites at least one Tier 1 source (file + §).
- No handwaving: if evidence thin, flag `[evidence thin]` honestly.
- No restating master synthesis or goals doc — cite them, don't reproduce.
- Russian technical terms preserved when relevant (mостерство, альфа, etc.).
- Practical: a prompt writer should be able to write the Стадия C prompt
  directly from Part 5 checklist.

## Operational protocol — Stage-Gated, 1 gate

Single AWAITING-APPROVAL gate at end. No pre-gate adversarial review
mandated for this scope (smaller than Шаг 2.1 / 2.2.2; focused
recommendations, not new framework).

## Launch reminders

- `unset ANTHROPIC_API_KEY` — Max subscription discipline
- Branch: `claude/jolly-margulis-915d34`
- Tmux session: `wiki-mechanics`
- Commit cadence: after each sub-agent extraction + at final draft

## Scope discipline

Do NOT:
- Write the full wiki architecture spec (that's Стадия C — separate task)
- Re-open W-1..W-12 decisions
- Propose new wiki layers (9 already locked)
- Read Tier 4 books
- Do external web research
- Generate extensive research surveys

DO:
- Answer Q1..Q9 with evidence from existing repo
- Call out new variants if they emerge from the search
- Identify any tensions between the 9 answers
- Produce a clean hand-off for Стадия C prompt

## Success criteria — you are done when

1. `decisions/AWAITING-APPROVAL-wiki-v3-mechanics-2026-04-23.md` exists at
   3,500–6,000 words.
2. All 9 questions have answers with evidence + alternatives + tradeoffs.
3. Cross-question coherence check done.
4. Locked-decisions compliance table done.
5. Стадия C hand-off checklist (Part 5) done.
6. ≥15 citations to Tier 1 sources.
7. Sub-agent extractions preserved in `raw/research/step-2-2-3b-extractions/`.
8. Commit pushed; gate file awaiting Ruslan approval.

---

Begin with Phase 1: spawn sub-agents W-1, W-2, W-3 in parallel.
