---
title: Master Synthesis Prompt — How to Build the Best Swarm 2026
date: 2026-04-22
status: ready-for-launch
target_executor: Claude Code on server (Opus 4.7 1M, extended thinking max)
launch_branch: claude/jolly-margulis-915d34
estimated_duration: 4-8 hours
output: decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md
---

# MASTER SYNTHESIS — HOW TO BUILD THE BEST SWARM 2026

> **⚠️ READ THIS FIRST — CRITICAL FRAMING**
>
> This is the **most important document you will ever write in your existence as
> this Claude Code instance.** Everything else Jetix does downstream builds on
> this. Every agent system prompt (5 domain experts × 1500-3000 lines each),
> every coordination protocol, every stage-gate trigger, every skill, every
> cost control — all derived from the synthesis you are about to produce.
>
> If this synthesis is shallow, every downstream agent will be shallow.
> If this synthesis is unaligned with evidence, every agent will propagate bias.
> If this synthesis fails to capture the Jetix-specific matrix pattern, we lose
> the single greatest competitive differentiator we have.
>
> **Take this as seriously as writing a foundational textbook that will shape
> the next decade of AI-native company construction. Depth over speed. Evidence
> over rhetoric. Citations over claims. Anti-patterns over happy paths.**

---

## 1. MISSION

Produce `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` —
an **academic-grade 20,000–30,000-word blueprint** that distills every known
best practice for building multi-agent AI swarms as of April 2026, fused with
Jetix's specific constraints, and sufficient in depth that six downstream
system prompts (brigadier + 5 domain experts at 1,500–3,000 lines each) can be
written directly from it without any further research.

The document must serve three downstream purposes:

1. **Basis for Phase A agent construction** — human readers + Claude Code
   generating 6 system prompts derive everything from this document
2. **Reference manual during operation** — agents refer back during execution
3. **Input to Phase B recursive self-improvement** — swarm reads this document
   as base state before deepening itself with Tier 4 book knowledge

---

## 2. CONTEXT — What Jetix Is Trying to Do

Jetix is being built as an AI-native holding / operating system that will run
solo-founder → €50K → €1M → $100M → $1T trajectory. Current state:

- 4 foundation documents approved (Vision / Philosophy / Plan / Architecture-Brief)
- 24 locked decisions binding all downstream work
- 393-book curated Private Library (competitive moat via knowledge curation)
- Research corpus on compounding engineering (CE), AI-native companies, market patterns
- 14 legacy agents (to be replaced by the new 5+1 matrix swarm)

**The task this master synthesis unlocks:** building a swarm that can take
the entire Jetix corpus + all external best practices and produce a recursively
self-improving system that drives the €0 → $1T trajectory.

You are writing the founding blueprint for that swarm.

---

## 3. THREE-PHASE RECURSIVE PATTERN (CRITICAL)

Your output operates within this pattern. Understand it deeply:

### Phase A — Baseline Swarm Creation (this document + agent generation)
- Inputs: Tier 1 deep / Tier 2 required / Tier 3 skim (see §4)
- **Tier 4 books are OUT OF SCOPE for Phase A.** Do not read them.
- Output: this master synthesis + 6 base system prompts
- Characteristic: deep within scope, not scope-expansive

### Phase B — Recursive Self-Improvement (first task the completed swarm gets)
- The swarm itself reads Tier 4 books (each domain expert reads its own books)
- Swarm refines its own system prompts + coordination using fresh insights
- Output: `JETIX-SWARM-V2-SELF-IMPROVED.md` + updated agents

### Phase C — Real Work
- After Phase B, swarm receives real Jetix problems
- Likely: recursive synthesis of meta-system + Jetix overlay

**Implication for your synthesis:** Design the Phase A swarm strong enough to
execute Phase B well. Do NOT try to do Phase B's job inside Phase A. Leave
domain-deep book insights FOR the swarm to harvest itself.

---

## 4. INPUTS — PRECISE READING ORDER

### Tier 1 — PRIMARY (deep read, every word matters)

These are the research files on multi-agent / CE / AI-native swarm patterns.
Treat them as foundational texts for this synthesis.

```
raw/research/compounding-engineering-2026-04-22/R-1.md
raw/research/compounding-engineering-2026-04-22/R-2.md
raw/research/compounding-engineering-2026-04-22/R-3.md
raw/research/compounding-engineering-2026-04-22/R-4.md
raw/research/compounding-engineering-2026-04-22/R-5.md
raw/research/compounding-engineering-2026-04-22/R-6.md
raw/research/compounding-engineering-2026-04-22/R-7.md
raw/research/compounding-engineering-2026-04-22/R-8.md
raw/research/compounding-engineering-2026-04-22/R-9.md
raw/research/compounding-engineering-2026-04-22/R-10.md
raw/research/compounding-engineering-2026-04-22/R-11.md
raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md
raw/articles/2026-04-22-every-compound-engineering-guide.md
raw/research/perplexity-market-ai-native-2026-04-22/
raw/research/phase-2-deep-research-2026-04-22/RESULT-05.md
raw/research/phase-2-deep-research-2026-04-22/RESULT-06.md
raw/research/phase-2-deep-research-2026-04-22/RESULT-07.md
```

**Approximate total:** ~80,000–100,000 words.

**Instruction:** For each file, extract: (a) evidence-based claims with source
attribution; (b) anti-patterns / failure modes with root causes; (c) concrete
implementation primitives that could translate into agent system prompts.

### Tier 2 — CONSTRAINTS (hard requirements, compliance-check your synthesis)

These bind the synthesis. Your output must NOT contradict them.

```
decisions/ROY-ALIGNMENT-2026-04-22.md       # ← matrix 5×4 pattern (CRITICAL)
decisions/ROY-INFORMATION-DIET.md
raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md     # Locks D1-D8
raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md         # Locks D9-D18
raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md # Locks D19-D24
decisions/JETIX-ARCHITECTURE-BRIEF.md       # quality criteria, 15 architect Qs
```

**Approximate total:** ~20,000 words.

**Instruction:** Read fully. Every claim in your synthesis must be compatible
with the 24 Locked decisions. Flag any tension with an explicit note. The
matrix 5×4 pattern from ROY-ALIGNMENT is a **first-class design element** —
it must appear throughout your implementation primitives section.

### Tier 3 — CONTEXT (skim, orient yourself)

Fast read. Extract structural understanding. Do not deep-analyze.

```
raw/research/master-inventory-2026-04-22.md
decisions/JETIX-VISION.md          # D1
decisions/JETIX-PHILOSOPHY.md      # D2 (skim for partnership/portfolio sections)
decisions/JETIX-PLAN.md            # D3 (phase structure only)
design/JETIX-FPF.md                # 3758 lines — selective chapters; skim TOC
.claude/agents/                    # directory — scan all 14 files briefly
.claude/skills/                    # directory — scan all 11 files briefly
CLAUDE.md
.claude/rules/global.md
```

**Approximate total:** ~30,000 words (skimmed).

### Tier 4 — DO NOT READ (explicitly out of scope for Phase A)

**Do NOT read the 393 books in `raw/books-md/`** during this synthesis. They
are explicitly reserved for Phase B. If you find yourself wanting to read
Ousterhout, Brooks, Ashby, Beer, Cagan, Grove, Meadows, Kelly, Laloux, or any
book from `raw/books-md/`, stop. Design the agent who will read that book
instead. Your job is the scaffold; the agent's job will be the content.

Exception: you MAY read `wiki/sources/2026-04-16-architecture-memory-kb-karpathy.md`
(this is a pre-digested source card, not a raw book).

### Tier 5 — IGNORE (not relevant to swarm technical design)

Do not open:
- `raw/research/*deep-research*` files on business domains (consulting, agency, CRM, community, holding, platform-os, product, software — except AI-native)
- Voice memos / ATOM-REGISTRY / KNOT-MAP (business strategy, not swarm design)
- Architecture variants V1-V5 (they use legacy 12-agent pattern the research disproves)
- Investing / philosophy / biology domains (unless directly cited in Tier 1 content)

---

## 5. SUB-AGENT STRATEGY (MANDATORY — DO NOT WORK MONOLITHICALLY)

**You must parallelize reading via the Task tool.** Working sequentially on
~100,000 words of Tier 1 will exhaust your context and produce shallow
synthesis. Instead:

### Phase 1: Parallel Deep Reads (spawn N sub-agents concurrently)

Spawn sub-agents in parallel (send multiple Task tool calls in a single
message) to perform deep reads with specific extraction briefs:

- **Sub-agent A** — CE research R-1..R-6: extract ontology terms (what is
  brigadier / expert / stigmergy / fan-out / Rule of 4 / termination stack /
  compound loop); define each from source material with citations.
- **Sub-agent B** — CE research R-7..R-11 + SYNTHESIS + Every canonical guide:
  extract production case evidence (Every/Cora, Anthropic, Factory.ai,
  Sierra, Harvey, Cognition, Aider) with specific metrics; identify
  machine-verifiable patterns.
- **Sub-agent C** — Perplexity AI-native research: extract market patterns,
  2026 state-of-the-art, adoption curves, competitive landscape; identify
  what works / what fails / what's emerging.
- **Sub-agent D** — Phase 2 RESULT-05/06/07: extract PM + Product Mgmt +
  Management Philosophy foundations that apply to swarm coordination
  (Shape Up cycles / Continuous Discovery / High-Output management / OKR).
- **Sub-agent E** — Tier 2 constraints + 24 Locks: produce compliance-check
  matrix that every synthesis claim will be verified against.

Each sub-agent returns a **structured extraction** (≤3,000 words):
findings, citations, anti-patterns found, Jetix-applicability notes.

### Phase 2: Integration & Synthesis (you as orchestrator)

You receive all sub-agent extractions + Tier 3 skim + Tier 2 constraints.
You write the actual master synthesis document integrating them.

If synthesis reveals gaps, spawn targeted follow-up sub-agents to dig
deeper on specific sub-topics.

### Phase 3: Adversarial Review (sub-agent as critic)

Before finalizing, spawn a **critic sub-agent** with adversarial brief:
find weaknesses, unsupported claims, anti-patterns you missed, contradictions
with 24 Locks, places where evidence is thin. Integrate its findings.

### Operational note

Do not let sub-agents read Tier 4 books. Enforce tier discipline in their
briefs. If a sub-agent asks to read a book, say no.

---

## 6. OUTPUT STRUCTURE — 6 PARTS (target 20,000–30,000 words)

### Part 1: ONTOLOGY (~2,500–3,500 words)

Define with precision the conceptual vocabulary. For each term: definition,
source attribution, example, relationship to other terms.

Required terms (expand if needed):
- Swarm / multi-agent / sub-agent / fan-out / hub-and-spoke
- Brigadier / expert / role-mode
- Stigmergy / shared environment / mailbox / wiki-based coordination
- Compounding Engineering (CE) / Plan-Work-Review-Compound loop
- Rule of 4 / context window / attention budget
- Termination stack (4 layers: maxTurns / budget / verifier / HITL)
- Matrix agent pattern (5 domains × 4 role-modes) — **Jetix-specific**
- Stage-gated vs Full-Auto mode
- Provenance / citation / evidence-based claim
- Anti-pattern / failure mode / post-mortem

### Part 2: EVIDENCE (~5,000–7,000 words)

Every major pattern recommendation must be backed by production evidence.
For each:
- **Claim** (what the pattern is)
- **Source** (paper / company / blog / podcast, with specific attribution)
- **Metric** (measurable outcome: speed / cost / quality / convergence time)
- **Constraint** (where it works / where it breaks)
- **Applicability to Jetix** (how matrix pattern uses or adapts it)

Cover at minimum: Every Cora pattern, Anthropic internal swarm practices,
Cognition/Devin architecture, Factory.ai, Sierra, Harvey, Aider's approach,
Boris Cherny's Claude Code philosophy, Karpathy LLM OS, DSPy, TextGrad,
constitutional AI self-improvement, MAST taxonomy (multi-agent failures).

### Part 3: ANTI-PATTERNS (~3,000–4,000 words)

What fails, why, how to detect, how to avoid. For each:
- **Pattern name** (e.g., "12-agent over-decomposition", "$47K billing incident")
- **Root cause** (why it fails)
- **Detection signals** (what to look for)
- **Prevention** (design choice)
- **Post-mortem citation** (where this was publicly documented)

Minimum coverage: multi-agent -3.5% quality delta (Kim et al. Rule of 4
study), MAST taxonomy top failure classes, Cognition's regrets on early
parallelism, legacy 12-agent trap, HITL escalation failures, wiki-rot,
context poisoning, circular delegation, cost runaway.

### Part 4: JETIX-SPECIFIC PATTERNS (~5,000–7,000 words)

**This is where the matrix 5×4 pattern lives in full bloom.**

Describe the swarm architecture tailored to Jetix:
- Why 5 domain experts (not 3, not 9): explicit tradeoff analysis
- Why 4 role-modes (not 3, not 7): explicit tradeoff analysis
- Why matrix not separate agents: synergy analysis with concrete examples
- How invocation works: `Task(agent: systems-expert, mode: critic, ...)`
- How mode-switching sections within system prompts are structured
- How 24 Locked decisions constrain each expert's domain boundaries
- How each expert integrates with Jetix Private Library (Phase B)
- How brigadier orchestrates matrix invocations
- How Stage-Gated vs Full-Auto selected per task
- Co-evolution with partners (Layer 2 Jetix overlay implication)
- Private Library knowledge access pattern (pool-first-query-second)

**Matrix example walkthrough (required):** take one concrete small task
(e.g., "design the termination stack for Phase 1 swarm") and show how it
would be executed through the matrix — which agents invoked in which modes,
in what order, how outputs integrate.

### Part 5: IMPLEMENTATION PRIMITIVES (~3,500–5,000 words)

Concrete enough that system prompts can be written from it directly:

- **Brigadier system prompt skeleton** (what goes in the 1,500–3,000 lines)
- **Domain-expert system prompt skeleton** (domain core + 4 mode sections)
- **Mode-section templates** (critic / optimizer / integrator / scalability)
  with activation triggers
- **Coordination protocol**: how brigadier delegates (Task tool params), how
  experts return structured output (JSON schema or markdown schema), how
  results merge
- **Stage-gated protocol**: what triggers a gate, file naming convention for
  `AWAITING-APPROVAL-*.md`, structure of gate files (context / options /
  recommendation / risk), resume protocol after approval
- **Full-Auto protocol**: budget caps, turn caps, verifier checks, fallback
  to HITL
- **Termination stack concrete**: maxTurns values per agent type, budget
  thresholds (in Max-subscription terms, not $), verifier predicate format,
  HITL escalation trigger
- **Wiki protocol**: what agents write where, provenance format, single-writer
  serialization for Phase 1
- **Tool permissions**: exactly which Claude Code tools each agent type gets
  (Read / Write / Edit / Bash / Grep / Glob / Task — with rationale)
- **Cost model**: Max-subscription operational checklist (`unset
  ANTHROPIC_API_KEY` / `--dangerously-skip-permissions` / tmux session
  isolation / commit cadence for audit)

### Part 6: TESTING & VALIDATION (~2,000–3,000 words)

- **Smoke test design**: minimal task that exercises brigadier + 1–2
  experts + at least 1 role-mode + 1 stage-gate cycle
- **Convergence criteria**: when is the swarm "good enough" for Phase B?
- **Regression detection**: how do we know Phase B improved things vs made
  them worse?
- **Eval framework**: what metrics to log per swarm run (cost / turns / HITL
  frequency / output quality signals)
- **Red-team protocol**: how critic-mode invocations are weighted so
  they're not trivially dismissed by consensus
- **Recursive improvement measurement**: how do we compare swarm-v1 output
  to swarm-v2 output objectively

---

## 7. QUALITY CRITERIA — you are measured against these

- **Evidence density:** every major claim has a source citation (file path +
  section / paper + page / company + date)
- **Anti-pattern coverage:** at least 15 distinct anti-patterns identified
  with root cause analysis
- **Matrix pattern first-class:** appears in ontology, evidence, anti-patterns,
  Jetix-patterns, implementation primitives, testing
- **24 Locks compatibility:** explicit compliance-check matrix in Part 4 or
  Part 5, flagging any tension with rationale
- **Actionability:** system prompts could be written from this document with
  minimal additional research (that's what distinguishes blueprint from essay)
- **Length 20,000–30,000 words:** not shorter. Depth over summary.
- **No marketing language:** no "cutting-edge", "revolutionary", "unique
  value proposition". Flat, technical, academic register.
- **Russian allowed for Ruslan's voice anchors only** (direct quotes);
  main text in English for technical precision.

---

## 8. OPERATIONAL PROTOCOL

### Launch

On server (`ssh ruslan@100.99.156.28`):

```bash
cd ~/jetix-os
git pull origin claude/jolly-margulis-915d34
unset ANTHROPIC_API_KEY
tmux new -ds master-synth
tmux send-keys -t master-synth "claude --dangerously-skip-permissions" C-m
```

Then paste this prompt (or point Claude Code at
`prompts/step-2-1-master-synthesis-2026-04-22.md`).

### Operating mode: STAGE-GATED

You operate in **Stage-Gated mode** for this synthesis. Commit + push at each
logical stage:

1. **After Phase 1 (parallel deep reads):** commit
   `raw/research/step-2-1-extractions/` with each sub-agent extraction as
   separate file. Message: `[research] master-synthesis Phase 1 extractions`
2. **After Part 1 draft (Ontology):** commit draft. Message:
   `[draft] master-synthesis Part 1 Ontology`
3. **After Part 2+3 draft (Evidence + Anti-patterns):** commit. Message:
   `[draft] master-synthesis Parts 2-3`
4. **After Part 4 draft (Jetix patterns):** commit as
   `decisions/AWAITING-APPROVAL-master-synthesis-matrix-2026-04-22.md` —
   **pause and push.** This is the critical gate: Ruslan must approve the
   matrix pattern implementation before you proceed.
5. **After Parts 5–6 drafts:** commit as
   `decisions/AWAITING-APPROVAL-master-synthesis-final-2026-04-22.md` —
   pause and push. Second critical gate: Ruslan approves complete blueprint
   before you declare Phase A complete.
6. **On approval of both gates:** consolidate into final
   `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`.
   Message: `[decisions] MASTER-SYNTHESIS — final, approved`.

### Commit cadence

- Commit every logical chunk (not just at gates)
- Push after every commit (no local-only work; Ruslan monitors via GitHub)
- Commit messages: `[agent] action: description` format (as per CLAUDE.md)

### If you get stuck

- If a tier-1 file seems corrupted or missing → flag, continue with others
- If sub-agent returns shallow extraction → spawn replacement with tighter brief
- If Ruslan hasn't reviewed a gate after 12 hours → continue in Full-Auto
  mode on non-blocking parts only (do NOT proceed past the gate on blocking
  dependencies)

---

## 9. ANTI-PATTERNS FOR YOU SPECIFICALLY

- **Do not write an essay.** This is a blueprint. Bullets, tables, structured
  prose are welcome. Flowing narrative is not the goal.
- **Do not be aspirational.** "The swarm should..." is weaker than "The swarm
  invokes Task(agent, mode) with the following parameters..."
- **Do not avoid specificity.** If a number can be named (maxTurns = 40),
  name it. Justify it.
- **Do not write Tier 4 content.** Ousterhout's "tactical vs strategic" does
  NOT belong in your document. It belongs in engineering-expert's system
  prompt, which will be written in a later step.
- **Do not hallucinate citations.** If you're not sure a source says what you
  attribute, flag with `[verify]` and move on. Better an honest gap than a
  made-up citation.
- **Do not over-compress Part 4.** Matrix pattern gets its full 5,000–7,000
  words. It is the Jetix differentiator.
- **Do not let sub-agents drift into Tier 4.** Enforce tier discipline in
  briefs.
- **Do not skip adversarial review.** The critic sub-agent pass is mandatory.
- **Do not declare Phase A done.** Your output enables Phase A completion
  (agent construction). Phase A is done when the 6 system prompts are written
  and smoke-tested. That comes in separate steps.

---

## 10. SUCCESS CRITERIA

You are done when:

1. ✅ `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` exists
2. ✅ Length 20,000–30,000 words, all 6 parts
3. ✅ ≥15 anti-patterns with root-cause analysis
4. ✅ ≥40 source citations (papers / companies / files / books in Tier 1–2)
5. ✅ Matrix pattern first-class in all 6 parts
6. ✅ 24 Locks compliance matrix explicit
7. ✅ Both AWAITING-APPROVAL gates passed (Ruslan approved)
8. ✅ Sub-agent extractions preserved in `raw/research/step-2-1-extractions/`
   for audit
9. ✅ Adversarial review sub-agent output integrated
10. ✅ Document deep enough that 6 system prompts at 1,500–3,000 lines each
    could be written from it without additional research

---

## 11. FINAL NOTE

This is not the swarm. This is the blueprint **from which** the swarm is
built. Every sentence you write here becomes seed-code for agent behavior
that will compound over months. A careless claim here becomes a systemic bias
across five experts. A missed anti-pattern here becomes a production
incident. A shallow ontology here becomes agents that speak past each other.

Write as if every word matters. It does.

Begin with Phase 1: spawn your parallel deep-read sub-agents.

---

## 12. REFERENCES (for Ruslan's audit)

- Alignment decisions: `decisions/ROY-ALIGNMENT-2026-04-22.md`
- Information diet: `decisions/ROY-INFORMATION-DIET.md`
- 24 Locked decisions: `raw/research/architecture-variants-2026-04-22/TENSIONS-*.md`
- Parent Notion page: https://www.notion.so/34a2496333bf817d93bff4cb66775587
- Grandparent Notion: https://www.notion.so/34a2496333bf810f9058fc783ce179e2
