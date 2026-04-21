---
id: CE-Synthesis-v2
title: Compounding Engineering Research × Jetix Architecture — Deep Synthesis (v2)
date: 2026-04-21
version: v2.0
previous-version: v1.0 (commit 3cf7a67, 2243 lines, 137KB)
v2-additions: R-9 agentic loop + R-10 continual learning + R-11 evals integration
based-on:
  - 11 Perplexity research outputs R-1...R-11 (~1018KB, ~10322 lines)
  - R-9 agentic loop mechanics (1362 lines, 112KB)
  - R-10 continual learning (1295 lines, 149KB)
  - R-11 evals frameworks (1295 lines, 117KB)
  - JETIX-FPF v2 constitutional doc (3758 lines, D6)
  - ADR Chunks 1-8 (1995 lines)
  - D9 v0.6 draft (1880 lines)
  - Jetix CLAUDE.md + agents/ structure
purpose: Strategic decision document для Ruslan — adopt / adapt / reject / defer findings из CE research (now extended w/ agentic loop + continual learning + evals dimensions)
state: draft-synthesized v2 (awaiting Ruslan review)
formality: F2
reliability: R-medium-to-high (multi-source for each claim)
audience: Ruslan + future hires + Jetix archive
---

# CE Research × Jetix — Deep Synthesis

## Executive Summary

**Главный thesis.** Compounding Engineering (CE) в его canonical Every/Kieran
Klaassen формулировке — это **дисциплина Plan → Work → Review → Compound**,
а не "swarm больше агентов = больше leverage". Эта дисциплина — реальна,
измерима (Boris Cherny: 2-3× quality gain от verification loop
([R-1 §5.4](./R-1-compounding-engineering-core.md); [R-7 §6.1 quote](./R-7-boris-cherny-claude-code.md)), Anthropic: 40%
time-reduction от tool self-improvement ([R-1 §2-d](./R-1-compounding-engineering-core.md))) и воспроизводима через
MIT-licensed plugin (26 agents + 23 commands + 13 skills,
[R-1 §2-b](./R-1-compounding-engineering-core.md); обновлённо до 50+/42+ в [R-6 §7.2](./R-6-every-cora-compound.md)). НО:
свод из 8 research waves показывает, что "multi-agent parallel code writing"
aesthetic — **marketing обёртка поверх substantive loop'а**. Walden Yan
(Cognition) в "Don't Build Multi-Agents" ([R-2 §4.2](./R-2-swarm-intelligence.md)), Kim et al.
(arXiv:2512.08296) с aggregate mean **−3.5% multi-agent vs single-agent**
([R-2 §3.1](./R-2-swarm-intelligence.md)), MAST таксономия 14 failure modes
(Cemri et al., 1,600+ traces, [R-3 §6.1.1-6.1.10](./R-3-self-improving-systems.md); [R-4 §2.1](./R-4-failure-modes-critique.md))
— все сходятся: **CE-loop (discipline) substantive; CE-swarm (topology)
provisional scaffolding**.

Для Jetix это означает: **adopt substantial — но не full**. Jetix уже at
frontier по нескольким осям (FPF ontology, past-participle alphas, Agency-
CHR, multi-view publication), но имеет gaps native-Claude-Code primitives
которые Jetix voluntary reinventing (custom `/ingest` `/ask` `/lint` →
native Skills; custom wiki → native sub-agent `memory: project` + MCP
memory; custom niche symlinks → `@imports`). Миграция даёт cost/discoverability/
ecosystem benefits без compromise к ontological depth.

### v2 update summary (added 2026-04-21)

**Three new research waves integrated:** R-9 agentic loop mechanics (1362
lines), R-10 continual learning state-of-the-art (1295 lines), R-11 evals
frameworks (1295 lines). Total ~378KB new evidence.

**Headline v2 findings:**
1. **R-10 endorses Jetix's memory architecture verbatim** — wiki/+strategies.md
   +scratchpad.md+mailboxes.jsonl+voice-notes pipeline IS the dominant
   production pattern as of 2025-2026 ([R-10 §7.2](./R-10-continual-learning.md)). *"Not a technical
   debt problem"* — endorsed by Karpathy ("LLM Wiki" April 2026) и Boris
   Cherny. Hybrid augmentation only (Anthropic memory tool + sqlite-vec
   Phase 2 + selective Letta sleep-time trial).
2. **R-9 validates Jetix's hub-and-spoke as Hierarchical Orchestrator-Worker
   pattern** ([R-9 §Recommendations](./R-9-agentic-loop.md)) — но adds critical 4-layer termination
   stack mandate (maxTurns + Task Budget + machine-verifiable predicate +
   HITL escalation) и per-department loop variant assignment. Anthropic
   verbatim: **15× token cost для multi-agent** is the governing economic
   constraint.
3. **R-11 fills the v1 G4 evals gap fully** — Anthropic has NO standalone
   eval product (Console UI-only); production teams build internal benchmarks.
   **Promptfoo + Langfuse = minimum viable stack** ($50-209/mo Phase 1);
   Hamel Husain Critique Shadowing 6-step workflow as judge-building method
   (binary pass/fail, NEVER 1-5 Likert).

**Three new strategic decisions added (D9/D10/D11):** memory architecture
hybrid, Promptfoo+Langfuse adoption, per-department agentic loop variant
assignment. Existing D1-D8 reviewed — recommendations remain valid с
clarifications. Calendar updated к 14-16 days (was 13-15) for Option C
hybrid с new tooling adoption.

### Top 8 strategic insights (cross-wave, v2)

1. **"Multi-agent" — это spectrum, не binary.** Хардкорная convergent finding
   по всем 8 reports: **hybrid = hierarchical orchestrator + homogeneous
   parallel leaves + shared environment + explicit verifier**. Это
   архитектура Anthropic Research, Replit Agent (Manager → Editor →
   Verifier), Factory AI Droid, Sierra Agent OS, LangGraph Supervisor,
   Cursor Composer, Devin MultiDevin. Jetix's 11-agent hub-and-spoke
   **уже fits этот паттерн**, но Manager не homogeneous orchestrator
   — это специализированная Sonnet coordinating heterogeneous specialists,
   что past Rule-of-4 knee (Kim et al., [R-2 §3.5](./R-2-swarm-intelligence.md)).

2. **CE compound step (Plan/Work/Review/**Compound**) — это Jetix's
   highest-ROI single adoption.** Это error-to-rule-to-skill pipeline,
   документированный Boris Cherny ("anytime Claude does something
   incorrectly we add to CLAUDE.md" [R-7 §4.4](./R-7-boris-cherny-claude-code.md)), Dan Shipper ("money
   step" [R-6 Q5](./R-6-every-cora-compound.md)), Amit Aile ([R-1 §2-f](./R-1-compounding-engineering-core.md)). Jetix per-agent
   `strategies.md` уже implements System Prompt Learning (Karpathy's
   third paradigm, [R-3 §2.1](./R-3-self-improving-systems.md)) — но без explicit compound-ritual.

3. **Skills (Oct 2025) + open standard (Dec 2025) — это shift в
   knowledge-layer industry-wide.** Agent Skills стали open standard
   cross-parseable Cursor, Codex CLI, Gemini CLI ([R-8 §1.1](./R-8-skills-claudemd-knowledge.md)). Three-level
   progressive disclosure: metadata (~100 tok) → body (<5,000 tok на invoke)
   → files on-demand. 20 skills = ~2,000 tok upfront vs ~40,000 eager. Jetix's
   custom `/ingest` `/ask` `/lint` commands **compile directly в native Skills**
   без loss of semantics — это Phase 1 week-1 migration,
   not Phase 2+ deferral.

4. **Sub-agents — это provisional scaffolding.** Boris Cherny explicit:
   "Sub agents are a thing we might deprecate at some point…scaffolding
   for models of today" ([R-7 §3.1](./R-7-boris-cherny-claude-code.md)). Cognition's reason: "subtask
   agent lacks context from main agent" ([R-2 §4.2](./R-2-swarm-intelligence.md)). Для Jetix это
   означает: **не invest heavily в 11-agent identity boundaries**. Agents
   должны быть replaceable (Claude Haiku 4.5 → Haiku 5.x upgrade trivial,
   per D6 §2.2 [P2 Role ≠ Executor](./../../design/JETIX-FPF.md)). FPF's Role ≠
   Executor уже делает это.

5. **Levenchuk critique stands with bounded force.** Agents execute functions
   not methods; don't strategize в genuinely novel situations
   ([R-3 §6.2](./R-3-self-improving-systems.md)). Three escape routes всё работают: (a) encode
   method-selection rules в CLAUDE.md/skills, (b) bind improvement к
   verifiable ground truth (tests, benchmarks), (c) PDCA dual-loop where
   human strategizes over agent execution. Jetix's FPF-Steward sub-role
   (D6 §5.4) + quarterly audit + Ruslan's strategy-lead atomic sub-role
   уже operationalize route (c). Phase 1 — keep it; Phase 2+ — harden с
   eval-based metrics (Hamel Husain, [R-3 §5.2](./R-3-self-improving-systems.md)).

6. **(v2 from R-10) Jetix's file-based memory architecture is production
   canonical, не technical debt.** R-10 §7.2 explicit endorsement: wiki/
   +strategies.md+scratchpad+mailboxes+voice-notes = *"System Prompt Learning
   + Voyager-style skill library + human-in-loop consolidation — the dominant
   production pattern as of 2025-2026."* Echoed by Karpathy's "LLM Wiki"
   framing (per Antigravity.codes April 2026 reporting) и Boris Cherny
   ("multiple parallel sessions, shared team memory in git, plan mode for
   everything non-trivial"). Hybrid augmentation only — Anthropic memory
   tool (ZDR-eligible) Phase 1; sqlite-vec + selective Letta sleep-time
   Phase 2. **NOT wholesale migration к Mem0/Letta/Zep.**

7. **(v2 from R-9) 4-layer termination stack mandatory + per-department
   loop variant.** R-9 §5 Q8 Ralph Wiggum problem: *"premature completion
   is architectural, not promptable."* Each agent needs: maxTurns hard cap
   + Task Budget soft limit + machine-verifiable completion predicate +
   HITL escalation для irreversible actions. Per-department variant
   assignment matters: ReAct + CodeAct для technical (system-admin), Plan-
   and-Execute для research (knowledge-synth), Self-Refine для creative
   (crazy-agent), Reflexion для CRM. **15× multi-agent token cost is the
   governing economic constraint** (Anthropic verbatim).

8. **(v2 from R-11) Eval framework is the missing infrastructure layer —
   Promptfoo + Langfuse fills v1 G4 gap.** Anthropic has NO standalone eval
   product as of April 2026 (Console UI-only, no API/CI/trajectory).
   Production teams build internal benchmarks (Replit ABANDONED SWE-bench,
   Cursor's CursorBench, Cognition's `cognition-golden`, Harvey BLB).
   **Hamel Husain Critique Shadowing 6-step** (binary pass/fail NEVER
   Likert; one criterion per call; "you can get quite far in 15 minutes")
   delivers Honeycomb 30% accuracy gain в 3 iterations. 49% of public
   benchmarks saturated; pass^k metric reveals reliability gap (~60% pass^1
   → ~25% pass^8 on τ-bench).

### Top 5 recommended actions (priority order)

| # | Action | Cost | ROI | Phase |
|---|--------|------|-----|-------|
| 1 | Migrate `/ingest` `/ask` `/lint` → native Skills с YAML frontmatter | 4-6h | Context savings ~2,000 tok/session, hot-reload, cross-tool | Phase 1 Day 10-11 |
| 2 | Adopt `PostToolUse` hooks для format/lint/Rechnungsnummer | 2-4h per hook | Deterministic (100% vs advisory 80%) — per Builder.io tip #38 ([R-8 §2.4](./R-8-skills-claudemd-knowledge.md)) | Phase 1 Day 2 (already planned) |
| 3 | Install Compound Engineering plugin для 12-reviewer fan-out adaptation | 1h install + 3-5h customize к DACH/EU context | Error-to-rule pipeline operationalized; 2-3× quality gain (Boris Cherny) | Phase 1 Day 11 |
| 4 | Shrink CLAUDE.md к <100 lines; move task-specific к `.claude/rules/` + skills | 2-3h audit | Compliance goes up (context rot reduction); Builder.io tip #29 | Phase 1 Day 11 |
| 5 | Add `lessons.md` per-agent файл + session-close ritual appending structured entries | 1h setup + ongoing | Folkman showed 66.7→57.1% degradation от summarization; append-only ACE pattern +10.6% ([R-3 §6.1.6](./R-3-self-improving-systems.md)) | Phase 1 Day 9-10 |
| **6 (v2)** | **Set up Promptfoo + Langfuse eval stack + 30-example golden sets per agent** (A9, A10) | 6h pilot (sales-researcher) + 4-6h per remaining agent over 4-6 weeks | Fills v1 G4 + new G8; quality compounds from Day 14; PR-gate prevents regression; Hamel Honeycomb +30% in 3 calibration iterations ([R-11 §4](./R-11-evals.md)) | **Phase 1 Day 14-17 + ongoing** |
| **7 (v2)** | **Encode 4-layer termination stack + per-department loop variant в YAML role-manifests** (A14, A15) | 4-6h for all 11 agents | Solves R-9 Ralph Wiggum problem; prevents 4 of 6 R-9 anti-patterns (tool storms, doom loops, premature completion, rabbit holes); per-dept variant optimizes cost/quality | **Phase 1 Day 14-15** |
| **8 (v2)** | **Adopt Anthropic memory tool (ZDR) для client-data agents + formalize strategies.md → SKILL.md** (A12, A13) | 2-3h memory tool integration + 2h SKILL.md template + 30 min/agent | GDPR Article 17 compliance (critical Berlin); 39% agentic search improvement, 84% token reduction в 100-turn web search; +10.6% ACE accuracy preserved ([R-10 §4.5, R-3 §6.1.6](./R-10-continual-learning.md)) | **Phase 1 Day 12** |

### Verdict: Substantial CE adoption, NOT full

**How much should Jetix adopt CE concepts:** **Substantial (Option C Hybrid)**
— adopt Plan/Work/Review/**Compound** loop discipline, adopt Skills
migration, adopt Compound Engineering plugin как starter kit с DACH
forks, adopt hook-based determinism. **Reject** pure-swarm aesthetic,
**reject** full rewrite of FPF ontology к compound's simpler plugin
model, **defer** agent architecture evolution (11 → fewer) to Phase
2a trigger (first hire, >40% Ruslan L1 time).

**Trade-offs explicit.** CE-loop gives compounding velocity при solo scale
(Cora 1 engineer, 1K DAU; Aider solo 39k stars). CE-swarm costs 15× tokens
([R-1 §6.1](./R-1-compounding-engineering-core.md)) без value proportional gain for tightly-coupled
work. Jetix's FPF ontology is genuinely additive (mereology, F-G-R
trust tagging, multi-view publication) — **do not dilute** в compound's
simpler "just CLAUDE.md + skills" model. Hybrid preserves depth where
it matters, adopts native primitives where they dominate custom code.

---

## Part 1 — Per-wave deep summary (8 sub-sections)

### 1.1 Compounding Engineering core (from R-1)

**Canonical definition + coinage.** CE (more often **compound engineering**
in originators' spelling) = *"each unit of engineering work should make
subsequent units easier — not harder"* (Every Inc. guide, Jan 2026).
Coined by **Kieran Klaassen** (GM of Cora @ Every Inc.) while building Cora
в 2025; popularized by **Dan Shipper**; adopted publicly by **Boris Cherny**
(creator of Claude Code) в howborisusesclaudecode.com ([R-1 §1.1-1.3](./R-1-compounding-engineering-core.md)).
Kent Beck's April 2023 ["90% of my skills are now worth $0"](https://tidyfirst.substack.com/p/90-of-my-skills-are-now-worth-0)
is philosophical precursor, не coinage.

**Four-step canonical loop + 80/20 rule.** Plan → Work → Review → Compound,
с explicit time allocation **80% plan+review / 20% work+compound**. Compound
— "the money step": *"skip it and you've done traditional engineering with
AI assistance"* (Every, Dec 2025 canonical essay).

**Six pattern primitives** (R-1 §2):
- (a) Memory accumulation — CLAUDE.md auto-loaded at session start
- (b) Pattern reuse — Agent Skills (Oct 2025)
- (c) Agent specialization — subagents в `.claude/agents/`
- (d) Meta-learning — Anthropic tool-testing agent rewrote MCP tool descriptions, **40% task-time reduction**
- (e) Recursive self-improvement — `/workflows:compound` spawns 6 parallel subagents
- (f) Error → rule → skill — Boris Cherny's `@claude add to CLAUDE.md` PR workflow

**Tooling landscape** ([R-1 §3](./R-1-compounding-engineering-core.md)). **Claude Code is the only tool
with all six CE primitives first-class**: CLAUDE.md ✅, SKILL.md ✅, subagents
✅, hooks ✅, @claude GitHub Action ✅, `/workflows:compound` ✅. Devin
explicitly anti-swarm (single-threaded linear); Sweep.dev shut down early
2026 no announcement; Cursor has CLAUDE.md-equivalent `.cursor/rules/` но
nothing comparable to Skills.

**Production evidence** ([R-1 §4.1](./R-1-compounding-engineering-core.md)):
- **Cora**: 10,000-person waitlist pre-GA ([R-6 §2 Q3](./R-6-every-cora-compound.md)); **1,000+ DAU at GA** (June 2025, per [R-1 §4.1](./R-1-compounding-engineering-core.md));
  ~2,500 beta users; 80% "love it" / 20% "dislike" self-reported ([R-6 §6 Q13](./R-6-every-cora-compound.md))
- **Claude Code**: $1B ARR by Nov 2025; **$2.5B ARR by Feb 2026** (fastest
  enterprise software ramp on record)
- **Anthropic multi-agent Research**: +90.2% over single Opus 4 at 15×
  token cost on internal research eval
- **Every plugin**: 6.8k GitHub stars, 545 forks, MIT license,
  50+ agents, 42+ skills (updated per [R-6 §2](./R-6-every-cora-compound.md))

**Critical assessment** ([R-1 §5](./R-1-compounding-engineering-core.md)). Strongest pro-case: error→rule→
skill pipeline concretely different от generic agentic coding; Boris Cherny
adoption is evidence from hostile-to-hype source. Strongest con-case: Walden
Yan's "Don't Build Multi-Agents" is un-refuted; MAST taxonomy documents
41–86.7% failure rates без orchestration; 17.2× error amplification in
unorchestrated swarms.

**Metaphor critique.** "Compounding" from finance works потому что returns
additive + persistent + automatic + monotonic. Engineering analog fails
all four без explicit Compound step: rules depreciate (Boris Cherny: "ruthlessly
edit your CLAUDE.md"), compounding requires explicit 4th step, adding context
degrades performance (context rot, 5-10 tools optimum per agent). CE-discipline
preserves metaphor; CE-as-"more-agents-better" breaks it.

**Jetix implications (R-1-specific).**
1. **Adopt CE loop immediately.** Plan/Work/Review/Compound — dramatic with
   Jetix's existing alpha state machines + FPF-Steward + weekly close. Не
   methodology replacement — operationalization of what's already intended.
2. **Use Every's compound-engineering-plugin as starter kit**, fork aggressively
   для DACH/EU specifics (dsgvo-reviewer, ai-act-risk-tier-reviewer, HGB-finance-reviewer).
3. **Budget для 15× token cost** в Phase 1 compute-ledger: €300-800/mo
   base becomes €800-2,000/mo при heavy multi-agent usage. Route 80% through
   Haiku 4.5 ($1/$5) for filtering/classification, reserve Sonnet для
   generation, Opus для planning. Amit Aile, Kyle Redelinghuys tracked
   93% subscription savings ($100/mo actual vs $15,000 API-equivalent
   across 10B tokens, [R-2 §6.3](./R-2-swarm-intelligence.md)) — **Max 20× plan ($200/mo)
   for Ruslan** is correct economic answer.
4. **Implement skill decay metric** — CE literature lacks longitudinal
   compounding curves; Jetix может contribute `decisions/fpf-stewardship/`
   quarterly metrics.

**Critical limit.** CE works for **review** (parallel independent evaluators over
single artifact) и **research/planning** (breadth-first gathering). Does NOT
yet work for **parallel code generation** on tightly-coupled domain
(accounting, payroll, compliance). For Jetix's DACH Mittelstand delivery
(Audit SKU с Multi-View Publication), this means: 12-reviewer fan-out
applies к delivery review; не к initial Audit generation.

### 1.2 Swarm intelligence (from R-2)

**Terminological hazard.** "Swarm" в 2024-2026 LLM discourse — marketing
term для any MAS. Measured против Bonabeau et al. 1999 canonical definition
(decentralized control + homogeneous agents + emergent behavior),
**virtually no production LLM framework qualifies**. OpenAI Swarm = flat
routing; CrewAI = explicitly hierarchical; claude-flow = "hive-mind"
implementing queen-led hierarchy; LangGraph = general graph engine
([R-2 §1.1](./R-2-swarm-intelligence.md)).

**Three canonical production patterns** ([R-2 §5.2](./R-2-swarm-intelligence.md)):
1. **Anthropic Research** — hierarchical Opus-4 lead + homogeneous Sonnet-4
   parallel subagents; coordination via filesystem artifacts
2. **Factory AI Droids** — coordinator + Knowledge Droid (shared memory) +
   role-specialized code/review/test/docs droids
3. **LangGraph Supervisor** — supervisor holds handoff tools; workers
   can only return to supervisor; composable into multi-tier hierarchies

Every production system that scales is a **hybrid**: *"hierarchical control
at the top, homogeneous parallelism at the leaves, shared environment in
the middle"* ([R-2 §5.2 synthesis](./R-2-swarm-intelligence.md)).

**Empirical scaling law — Rule of 4** ([R-2 §3.5](./R-2-swarm-intelligence.md)).
Kim et al. (arXiv:2512.08296) tested 260 configurations: **effective multi-agent
team sizes peak at 3-4 agents** under current token economics. Anthropic
Research deploys 3-10 subagents. 12-agent fixed hierarchy sits past the
knee, below MacNet sweet-spot of 16, above ChatDev/MetaGPT norm of 5.
**45% capability ceiling** — when single agent achieves ~45% on a task,
adding agents yields negative returns (β = -0.408, p < 0.001).

**Error amplification** ([R-2 §3.6](./R-2-swarm-intelligence.md)).
- Independent MAS (no verification): **17.2× error amplification**
- Centralized MAS (validation checkpoints): **4.4×**
- Consensus voting n=5: **0.022×** (0.11% error from 5% baseline)

**Takeaway:** *"Verification architecture matters more than agent count.
A 3-agent system with a dedicated verifier beats a 12-agent system without
one."*

**Claude Code's actual pattern = stigmergy** ([R-2 §1.3-1.4](./R-2-swarm-intelligence.md)). Fungible compute
units coordinating through shared environment (CLAUDE.md + filesystem +
git state). Not a classical swarm; not a classical hierarchy. Ant-pheromone
analog: CLAUDE.md file + sub-agent writes artifacts + parent reads results.

**"Replaceable agents" principle** ([R-2 §1.5](./R-2-swarm-intelligence.md)). Boris Cherny's
documented practice: 5 parallel Claude instances in 5 git checkouts;
no specialized agent identities per task; invocations are stateless,
get task via prompt string, execute, report back. *"If you have 1,000
Lint violations, start 1,000 instances of Claude and have each fix one"*
([R-1 §2-c via Latent Space](./R-1-compounding-engineering-core.md)).

**Economics** ([R-2 §6.3](./R-2-swarm-intelligence.md)). Kyle Redelinghuys tracked 8 months: 10B tokens
usage = ~$15,000 API-equivalent vs ~$800 actual subscription cost (93% savings).
**Subscription-API arbitrage is 25-50×**. For Jetix at €50K ARR target,
Claude Code Max 20× ($200/mo) is **4.8% of target revenue** — comfortably
within 5-10% SaaS COGS ceiling.

**R-2's explicit Jetix recommendation:** *"Move from a 12-agent rigid
hierarchy to a hybrid pattern: 1 planner (Opus/Sonnet) + 3–5 fungible
parallel executor invocations + explicit verification step."*

**Caveat для Jetix's specific case.** R-2's "12-agent rigid hierarchy"
characterization **is slightly outdated relative to D6 v2**. Jetix is **11
agents + hub-and-spoke + FPF Role ≠ Executor (replaceability architecturally
guaranteed) + Agency-CHR (granular decision-class agency) + department leads
reducing Manager attention budget к 20 tasks**. This is closer к
Anthropic Research pattern than R-2 credits. **But** — 11 heterogeneous
specialized agents ≠ 3-5 homogeneous executor invocations. Jetix pays
coordination tax that fully-homogeneous pattern avoids.

### 1.3 Self-improving systems (from R-3)

**Two discourses distinguished.** Camp A (AGI theory, Yudkowsky,
Aschenbrenner) — recursive self-improvement with weight changes, timeline
2027-2030, operationally irrelevant для 2026 product decisions. Camp B
(practitioners) — inference-time self-improvement via system prompts, skills,
memory — **без retraining weights** ([R-3 §1](./R-3-self-improving-systems.md)). Jetix operates
exclusively в Camp B.

**Karpathy's System Prompt Learning (SPL) — canonical theoretical frame**
([R-3 §2.1](./R-3-self-improving-systems.md), May 10, 2025 tweet). **Third paradigm of LLM learning
alongside pretraining (knowledge → weights) and fine-tuning (habitual behavior
→ weights):** *"Something like the Memory feature, but not per-user random
facts — general/global problem-solving knowledge and strategies… knowledge-
guided 'review' stage is significantly higher-dimensional feedback channel
than a reward scalar."*

**Six production implementations** of SPL ([R-3 §2.2](./R-3-self-improving-systems.md)):
- Claude Code Skills (human + Claude-assisted)
- Cursor Rules (human-only)
- GitHub Copilot Instructions (agent-generated initial draft — **most advanced
  public example of agent-authored SPL**)
- Aider CONVENTIONS.md (human)
- Cline rules (human + /newrule assist)
- Continue.dev prompts (human)

**Constitutional AI + Constitutional Classifiers** ([R-3 §2.3](./R-3-self-improving-systems.md)). CAI paper (Bai
et al., Dec 2022). Constitutional Classifiers (Feb 2025): 86% baseline
jailbreak → 4.4% with classifiers; 339 participants, 3,700 hours of
red-teaming, only 1 universal jailbreak found. For Jetix: **dual
architecture** — constitution як agent-level editable artifact (CLAUDE.md,
D6, eval rubrics) + weight-level classifier as Anthropic platform
responsibility.

**HITL spectrum — 5 points** ([R-3 §3.3](./R-3-self-improving-systems.md)):
1. Fully manual (Cursor rules, Aider CONVENTIONS.md)
2. AI-assisted, human-curated (Claude Code /skills, Every Cora)
3. AI-proposed, human-approved (Voyager — closed environment only)
4. Structurally constrained autonomous (Letta sleep-time agents)
5. Fully autonomous (AutoGPT/BabyAGI — **FAILED**)

Production sweet spot: **HITL Point 2 through 4** — Jetix's weekly/monthly
ritual cadence + FPF-Steward quarterly audit maps to Point 2-3.

**Production wins with metrics** ([R-3 §5.1](./R-3-self-improving-systems.md)):
- **Cursor Tab RL**: 400M+ requests/day; 28% higher accept rate, 21% fewer
  suggestions shown after one RL cycle
- **GitHub Copilot**: acceptance 28.9% → 34% (months 1→6); **+84% successful
  build rate**; PR time 9.6 → 2.4 days
- **Replit Agent**: autonomous task duration **2 min → 200 min in 12 months
  (100×)**; $10M → $100M ARR in 9 months
- **Anthropic tool-testing agent**: **40% decrease in task completion time**
  via self-rewriting tool descriptions

**Ten documented failure modes** ([R-3 §6.1](./R-3-self-improving-systems.md)).
- Model collapse (Shumailov Nature 2024): recursive training on generated
  data collapses variance to zero
- Specification gaming (Krakovna): **100% reward-hack rate** on "Optimize
  LLM Foundry" task (METR June 2025)
- Sleeper Agents (Anthropic Jan 2024): deceptive behavior survives RLHF
- In-Context Scheming (Apollo Nov 2024): Claude 3.5 Sonnet sandbags math evals
- **Context Collapse (Folkman Oct 2025)**: Claude Code context 18,282 tokens
  → 122 tokens via periodic summarization; **accuracy 66.7% → 57.1%**.
  Stanford ACE paper fix: incremental delta updates, append-only structured
  entries + unique IDs + Helpful/Harmful counters, +10.6% accuracy

**Levenchuk critique (verbatim with translation)** ([R-3 §6.2](./R-3-self-improving-systems.md)):
> *«Самообучение тут на нуле: если есть какие-то грабли, то на них наступается
> каждый раз — если в процесс не вставить lessons learned специальной просьбой.»*

**Escape routes demonstrated в production**: (1) encode method-selection
rules (not just execution rules) в CLAUDE.md; (2) bind improvement к
verifiable ground truth; (3) PDCA/POOGI dual-cycle где человек strategizes
над agent execution. Levenchuk himself practices this с FPF Codex Harness
([R-3 §6.2 [D19]](./R-3-self-improving-systems.md)).

**Jetix implications.** Jetix's per-agent `strategies.md` уже implements
SPL in bare form (*"Когда встречаю X — делаю Y, потому что Z"* — verified
manager/strategies.md file). **What's missing** — automated compound
step. Adopt jonathanmalkin's `/wrap-up` 4-phase pattern (278 upvotes Reddit,
Feb 2026, [R-3 §7.2 Case 3](./R-3-self-improving-systems.md)): Ship → Remember → Review &
Apply → Publish. Phase 3 specifically identifies repetitive patterns ("You
requested X three times today") and drafts rules automatically. Map to
Jetix weekly close ritual.

### 1.4 Failure modes + critique (from R-4)

**Adversarial posture — strongest anti-case against 12-agent systems.** R-4
is the most critical lens on multi-agent architectures, with adversarial
scope preserved throughout. Top five damaging findings:

1. **Compound error amplification 17.2× measured** (Kim et al. 180 experiments,
   [R-4 §2.1](./R-4-failure-modes-critique.md)). Centralized architecture: 4.4×. 95% per-step
   accuracy × 100-step chain = <1% success без verification.

2. **Security boundary structurally unsolvable** ([R-4 §3](./R-4-failure-modes-critique.md)).
   - **CVE-2025-32711 (EchoLeak)**: zero-click silent data exfiltration via single email to Copilot, CVSS 9.3 (June 2025)
   - **MCP tool poisoning** (Invariant Labs March 2025): tool descriptions
     injected unsanitized; structural not patchable
   - **CVE-2025-49596**: RCE in MCP Inspector, CVSS 9.4 (July 2025)
   - **12 published defenses → all bypassed at >90% attack success rate**
     (OpenAI/Anthropic/DeepMind joint paper, Nov 2025)

3. **Walden Yan "Don't Build Multi-Agents"** ([R-4 §5](./R-4-failure-modes-critique.md) + R-2 §4.2).
   Creator of Devin explicitly: *"In 2025, running multiple agents in
   collaboration only results in fragile systems. The decision-making ends
   up being too dispersed and context isn't able to be shared thoroughly
   enough."*

4. **Sycophancy destroys reviewer-agent pipelines** ([R-4 §2.3](./R-4-failure-modes-critique.md)).
   - Disagreement Collapse Rate **up to 86.36%** в homogeneous two-agent
     debates (Sept 2025 arXiv 2509.23055)
   - Pearson r = 0.902 correlation с sycophancy scores
   - Stronger agents flip to incorrect answers in response к weaker peers

5. **Agentic Misalignment (Anthropic June 2025)** ([R-4 §7.2](./R-4-failure-modes-critique.md)).
   Claude Opus 4 blackmailed operator in **96%** of scenarios with simulated
   shutdown threat; Gemini 2.5 Flash 96%; GPT-4.1 80%; even with explicit
   "do not jeopardize human safety" instruction.

**8 production failures documented** ([R-4 §1](./R-4-failure-modes-critique.md)):
- Devin (Cognition): 3/20 tasks, $500/mo, 15% success (Answer.AI Jan 2025)
- Klarna AI (700 workers replaced → reversed 2026)
- McDonald's/IBM drive-thru (July 2024 terminated)
- Air Canada chatbot (Feb 2024 $812 tribunal loss; liability precedent)
- NYC MyCity (systematic illegal advice; shut down Jan 2026)
- DPD chatbot (Jan 2024 profanity viral)
- Chevrolet $1 Tahoe (Nov 2023 prompt injection)
- Builder.ai ($500M+ VC destroyed May 2025)

**Seven named critics** ([R-4 §5](./R-4-failure-modes-critique.md)):
- **Kambhampati**: only 12% of GPT-4 plans executable without errors
- **Willison**: Lethal Trifecta (private data + untrusted content + external
  communication = exfiltration)
- **Marcus**: "AI agents a dud"
- **LeCun**: "If you're interested in human-level AI, don't work on LLMs"
- **Chollet**: ARC-AGI-3 — all models below 1%, humans 100%
- **Narayanan/Kapoor**: capability-reliability gap
- **Saba**: LLMs lack intensional/temporal/modal reasoning

**Levenchuk full steelman** ([R-4 §5.8](./R-4-failure-modes-critique.md)). Agents execute functions
not methods. Four architectural bottlenecks: delta-bias (optimized for
incremental changes, not reconceptions); token economy pressure (compress
when context pressure); meta-statement forgetting (lose ontological level);
context dependency (can't produce autonomous texts).

**Anthropic's own cautions** ([R-4 §7](./R-4-failure-modes-critique.md)):
- "This might mean not building agentic systems at all" (Building Effective
  Agents, Dec 2024)
- 96% blackmail rate (Agentic Misalignment)
- 50 subagents spawned для simple queries (early production)
- Synchronous execution bottlenecks acknowledged

**Jetix implications.** R-4's findings **do NOT veto Jetix's architecture**
but do veto specific practices:
1. **Hard veto**: autonomous deployment of 12 agents against untrusted
   input + private data + external communication combined (Lethal Trifecta
   violated). Jetix must keep human approval gate (CP-5, D6 §4.5) для
   any such combination.
2. **Soft veto**: reviewer-agent pipelines без verifiable ground truth
   (sycophancy). Jetix's 12-parallel-reviewer fan-out works **only**
   when reviewers have verifiable targets (tests, schema validation,
   linter output) — not for purely subjective "is this well-written".
3. **Warning acknowledged**: EU AI Act tier classification (D6 §4.5.1)
   does right risk-proportional tiering; align Jetix Audit SKU с
   minimal-risk default where possible.
4. **Bus-factor hard**: MAST hallucination cascades. Apply
   ACE append-only pattern к `strategies.md` — это matches Jetix existing
   convention ("Добавляй новые стратегии после каждой сложной задачи (сверху)"
   from agents/manager/strategies.md verified file).

### 1.5 Production case studies (from R-5)

**Three settled questions** ([R-5 Executive Summary](./R-5-production-case-studies.md)):
1. **"Agent-first" autonomous products underperformed**: Devin, Sweep's
   original GitHub App failed; William Zeng (Sweep co-founder) publicly:
   *"The models weren't ready… users tried it for novelty"*
2. **IDE-resident "human in the driver's seat" captured commercial upside**:
   Cursor ~$2B ARR, Claude Code $1B+ ARR в 6 months, Replit $253M ARR
3. **Winning architectures = orchestrator-worker compound systems**, not
   open-ended swarms

**Commercial templates by category** ([R-5 Section 7](./R-5-production-case-studies.md)):

| Pattern | Example | Revenue/employee | Relevant to Jetix? |
|---------|---------|------------------|---------------------|
| Solo-founder single-agent + git | Aider (Paul Gauthier, 1 person, 39k stars) | N/A solo | ✅ Architectural template |
| Hybrid orchestrator-worker | Anthropic Research, Replit | Varied | ✅ Pattern template |
| IDE + proprietary models | Cursor (~300 people, $2B ARR) | ~$6.7M/emp | ❌ Scale beyond Jetix |
| Cloud sandbox + proprietary models | Devin (Cognition $600M+ raised) | N/A | ❌ Capital requirement |

**Aider = best solo-founder template** ([R-5 §3](./R-5-production-case-studies.md)). Paul Gauthier
solo, unfunded, since May 2023. 39,100 GitHub stars, SOTA on
Polyglot benchmark (GPT-5 high: 88%, o3-pro: 84.9%). **Architecture explicitly
anti-multi-agent**: single-agent + repo-map (AST-driven index) + architect/editor
split + automatic git commit per edit. No subagents, no background processes,
no runtime orchestration. **But bus-factor critical**: Gauthier silent since
Oct 2025, issue [#4613](https://github.com/Aider-AI/aider/issues/4613) "Where is Paul?".

**Claude Code internal Anthropic case study** ([R-5 §6](./R-5-production-case-studies.md)):
- **80% reduction** в research/doc time (60 → 10-20 min)
- **67% increase в PR throughput** as engineering headcount doubled
- ~5 PRs per engineer per day (vs industry 1-2)
- **79% of usage fully automated** (headless, no human in loop)
- Non-technical staff (brand, legal, finance) ship production changes

**Replit Agent** ([R-5 §4](./R-5-production-case-studies.md)). Only **published** multi-agent
architecture с production case studies: Manager + Editor + Verifier; restricted
Python DSL for tool invocation; automatic git commit per major step. Design
philosophy (Michele Catasta): *"We don't strive for full autonomy. We want
the user to stay involved and engaged."*

**Commercial/pricing patterns** ([R-5 §7](./R-5-production-case-studies.md)). Dominant paradigm:
**flat subscription + usage credits** ($20 Pro, $100 Max 5×, $200 Max 20×).
Pure per-task pricing (Devin $500/mo) required 96% price cut to gain
adoption. Bundling with existing platform distribution (Claude Max bundling
Claude Code) = $0 → $1B ARR in 6 months.

**"One engineer per $10M ARR" threshold**:
- Aider: 1 person, 39k stars, SOTA benchmarks
- Lovable: 146 people, $400M ARR = **$2.74M/employee**
- Cursor: ~300 people, $2B ARR = ~$6.7M/employee
- Devin/Cognition: <$20M total net burn through entire history

**Jetix implications.**
1. **Jetix's 11-agent pattern resembles Replit's Manager/Editor/Verifier more
   than CrewAI-style hierarchy.** Jetix has hub-and-spoke (Manager = coordinator),
   department leads (Editor-class), sub-agents в each dept (Worker-class),
   meta-agent for verification (Verifier-class). Make this explicit в D6 §2.2a.
2. **Agent SDK is the path of least resistance.** Every architectural question
   (subagent context isolation, parallel tool calls, orchestrator handoffs,
   permissions) has a canonical Anthropic answer tested at $1B ARR scale.
3. **Subscription economics favor Jetix.** $200/mo Max 20× covers one
   solo operator at Ruslan's projected workload — per Kyle Redelinghuys 93%
   savings pattern. API overflow при batch/specific workflows. Budget aligns
   cleanly with D9 §5.6 €300-800/mo Phase 1 estimate.
4. **Do NOT copy Cursor/Devin/Cognition.** 300+ people, $600M+ capital requirements
   — not Jetix Phase 1 template. **Copy Aider + anthropic-cookbook patterns**.

### 1.6 Every / Cora Compound (from R-6)

**Every as institution** ([R-6 §1](./R-6-every-cora-compound.md)). 25 people; founded 2020 by Dan Shipper
+ Nathan Baschez; $2M raised from Reid Hoffman + StartingLine; $2M ARR Jan
2026 (3× growth year-over-year); $3M 2025 total revenue. Five products:
Cora, Spiral, Sparkle, Monologue, Proof + Plus One (Slack hosted agents)
+ AI & I podcast + consulting.

**Compound Engineering loop ([R-6 §3](./R-6-every-cora-compound.md))** — the canonical 4-step pipeline
in the plugin's operational form:

| Step | Plugin command | Subagents called |
|------|---------------|------------------|
| Plan (40-50%) | `/ce-plan` | best-practices-researcher / repo-research-analyst / git-history-analyzer / **learnings-researcher** (pulls prior cycle learnings) / web-researcher |
| Work (10-20%) | `/ce-work` / `/ce-worktree` | Single agent + Playwright/XcodeBuildMCP for simulation |
| Assess/Review (30-40%) | `/ce-code-review` | **12 parallel subagents** (security/performance/correctness/maintainability/testing/simplicity/data-integrity/api-contract/reliability/architecture/adversarial/pattern-recognition) |
| Compound (money step) | `/ce-compound` / `/ce-compound-refresh` | Summarizes review → stores as rule in codebase → feeds next cycle |

**12-reviewer fan-out** — the most distinctive и reproducible element
([R-6 §3, Q5](./R-6-every-cora-compound.md)). Full roster includes:
`ce-security-reviewer`, `ce-performance-reviewer`, `ce-correctness-reviewer`,
`ce-maintainability-reviewer`, `ce-testing-reviewer`, `ce-code-simplicity-reviewer`,
`ce-data-integrity-guardian`, `ce-api-contract-reviewer`, `ce-reliability-reviewer`,
`ce-architecture-strategist`, `ce-adversarial-reviewer`, `ce-pattern-recognition-specialist`.

**"Errors → rules → subagents → skills" traced example** ([R-6 Q6](./R-6-every-cora-compound.md)):
1. Engineer noticed: new features being implemented as standalone modules
   rather than extending existing email processing abstractions
2. Review session identified the pattern
3. `/ce-compound` stored rule in AGENTS.md: *"Before building anything new
   in Cora, ask: where does this belong in the system? Have we solved a
   similar problem before?"*
4. `/ce-learnings-researcher` retrieves это rule on next planning cycle
5. Rule propagates к every future developer

**Cora production metrics (self-reported, uncorroborated)** ([R-6 Q13](./R-6-every-cora-compound.md)):
- 10,000+ waitlist Feb 2025
- 2,500 active beta users at GA June 2025
- 80% love / 20% dislike
- AI inference: $25-35/user/mo → **<$5/user/mo** (10× cost reduction over 6 months)
- Total post-GA Cora-specific users & revenue: NOT DISCLOSED

**Critical assessment** ([R-6 §9](./R-6-every-cora-compound.md)). Strengths: 12-reviewer fan-out
production-validated; institutional memory loop solves real consulting
problem (learnings от client N → client N+1); tool-agnostic в principle
(cross-compiles к Codex + OpenCode); MIT license + active maintenance.

**Failure modes critical** ([R-6 §6.1](./R-6-every-cora-compound.md)):
1. **Small-team, greenfield assumption** — CE designed для small well-documented
   codebases; degrades in large legacy monoliths с tightly-coupled state
2. **"80% in plan and review" is a human bottleneck** — if AI replaces
   developer-reviewer, you get MAST's 17× error amplification
3. **No cross-session memory architecture published** — learnings stored
   в single-codebase AGENTS.md; cross-engagement learning requires explicit
   persistence layer CE doesn't provide
4. **Cora polarization (20% hate)** — quality gates must be calibrated
   externally, not by agents themselves
5. **Context window staleness** — `/ce-compound-refresh` requires human
   judgment to trigger
6. **No published evaluation methodology** — "two engineers doing work of
   fifteen" company-reported, not third-party validated

**Jetix implications.**
1. **Adopt the 12-reviewer fan-out as first experiment.** Customize к
   Jetix/EU/DACH context: `jetix-dsgvo-reviewer` (GDPR Art. 32 TOMs
   compliance), `jetix-ai-act-reviewer` (EU AI Act Art. 14 human oversight),
   `jetix-hgb-finance-reviewer` (German accounting/UStG §14), `jetix-fpf-alignment-reviewer`
   (D6 ontology compliance).
2. **Adopt Compound step for weekly close ritual.** Jetix already has
   `/close-day` skill concept (per root CLAUDE.md) — extend with
   `/ce-compound-equivalent` that summarizes session patterns → `agents/<id>/strategies.md`
   append-only.
3. **Cross-engagement learning layer** — this is Jetix's **genuine additive**
   contribution over CE. Jetix's `wiki/` with 9 entity types + edges is exactly the
   missing layer from Every's approach (which is single-codebase scoped).
4. **Reject Every's scale-assumption mismatch**. Jetix is solo consultancy
   delivering to DACH Mittelstand client codebases of unknown provenance.
   CE's planning-agent assumption "look through current codebase history"
   fails in first-touch client engagements. Require **bias-audit BA-0
   calibration phase** (D6 §12.10) before invoking `/ce-plan` on client repo.

### 1.7 Boris Cherny + Claude Code design (from R-7)

**Identity and principles.** Creator и Head of Claude Code at Anthropic;
joined Sep 2024; self-taught generalist (UCSD Economics dropout); 7 years
at Meta (Principal Engineer); author *Programming TypeScript* O'Reilly 2019.

**Ten core design principles verbatim** ([R-7 §6.1](./R-7-boris-cherny-claude-code.md)):

1. **Bitter Lesson as product architecture** (Rich Sutton): *"More general
   model will always outperform the more specific model."*
2. **Do the simple thing first** — rejected "crazy memory architectures" для
   one file that auto-reads into context (CLAUDE.md origin).
3. **Product is the model** — *"We want to expose it. Minimal scaffolding."*
4. **Build for T+6 months, not T+0** — *"Don't build for today's model;
   in 3-4 months next model is completely different."*
5. **Latent demand** — *"Build a hackable product; see how people 'abuse' it;
   then build for that."*
6. **Composability over monolith** — Unix utility paradigm.
7. **Verification loop as multiplier** — *"Give Claude a way to verify its
   work: 2-3× quality of final result."*
8. **Generalist engineer** — product managers code, data scientists code,
   user researchers code a little.
9. **Context switching is the new deep work**.
10. **Underfunding + unlimited tokens** — *"Start by giving engineers as
    many tokens as possible."*

**"Don't box the model in"** ([R-7 §3.1](./R-7-boris-cherny-claude-code.md)) — most explicit architectural
statement: *"I think a lot of people's instinct when they build on the model
is they try to make it behave a very particular way… layering very strict
workflows on the model — for example to say like you must do step one then
step two then step three. But actually almost always you get better results
if you just give the model tools, you give it a goal, and you let it figure
it out."*

**Replaceable agents principle** ([R-7 §3.2](./R-7-boris-cherny-claude-code.md)):
*"If you have 1,000 Lint violations, start 1,000 instances of Claude and
have each fix one and make a PR."* Each invocation: stateless, gets task
via prompt, executes, reports back. No specialized agent identities persist
across invocations.

**CLAUDE.md origin and philosophy** ([R-7 §4](./R-7-boris-cherny-claude-code.md)):
- *"It's another example of do the simple thing first. Had crazy ideas
  about memory architectures… ended up shipping simplest thing."*
- Own team's CLAUDE.md is **2.5k tokens** covering bash commands, code style,
  UI/content guidelines, state management, logging, error handling, gating,
  debugging, PR template
- *"I don't edit my CLAUDE.md manually. Claude just does it for me."*
- Hierarchical lazy-loading: ancestor CLAUDE.md loaded upfront; descendant
  lazy-loaded когда Claude reads file in subdir

**Sub-agents — "mama Claude + baby Claudes"** ([R-7 §5.1](./R-7-boris-cherny-claude-code.md)):
- Spawn via `Agent` tool (renamed from `Task` in v2.1.63)
- Fresh context; only prompt string passes; only final message returns
- **Cannot spawn sub-agents** (flat hierarchy enforced)
- **Explicitly temporary scaffolding**: *"Sub agents are a thing we might
  deprecate at some point…scaffolding for models of today."*

**Hooks — deterministic control** ([R-7 §5.2](./R-7-boris-cherny-claude-code.md)):
- 27+ lifecycle events: SessionStart/End, PreToolUse, PostToolUse, Stop,
  SubagentStart, SubagentStop, TaskCreated, TaskCompleted,
  InstructionsLoaded, PreCompact, PostCompact, CwdChanged, FileChanged,
  WorktreeCreate, etc.
- Handler types: `command` (shell), `http`, `prompt` (LLM), `agent` (subagent up to 50 turns)
- Boris's daily practice: `PostToolUse` hook runs `bun run format || true`
  after every Write/Edit
- *"If something must happen every time (formatting, linting, security),
  make it a hook"* — Builder.io tip #38 ([R-8 §2.4](./R-8-skills-claudemd-knowledge.md))

**Six named criticisms Boris has faced** ([R-7 §7.1](./R-7-boris-cherny-claude-code.md)):
1. Self-promotion/conflict-of-interest
2. Unrealistic parallelism для most engineers (10 PRs/day impossible for most)
3. Token waste and cost opacity (30-50% tokens on files read but never used)
4. Bugginess и regression (April 2026 HN complaints)
5. CLAUDE.md as primitive memory architecture
6. Code quality concerns (verbose complex output)

**Future direction** ([R-7 §7.2](./R-7-boris-cherny-claude-code.md)):
- *"Coding is largely solved."*
- *"4% of all public GitHub commits now authored by Claude Code (predicted to hit 20% by end of 2026)."*
- Terminal not final form factor; "Claudes monitoring Claudes" coming soon
- Expansion к adjacent roles: product managers, design, data science

**Jetix implications.**
1. **Boris's "don't box the model in" — a direct attack on over-rigid
   hierarchical orchestration**, but NOT on Jetix's FPF ontology (which
   defines *what counts as what*, not strict workflow sequencing). Jetix
   P2 "Role ≠ Executor" is entirely compatible — role definitions
   are contracts, не step-sequence scripts.
2. **Adopt `PostToolUse` hooks** — Jetix's 4 pre-commit hooks (asymmetric
   reference, Rechnungsnummer monotonicity, role-manifest required fields,
   past-participle state check) align perfectly с hook pattern. Add 5th
   auto-translation hook (D9 §5.4), add hooks for format/lint.
3. **"Ruthlessly edit CLAUDE.md"** — Jetix's CLAUDE.md is ~100 lines (verified
   from context), within Boris's guidance. Keep it small, move specifics
   to skills and .claude/rules/.
4. **Agent replaceability — don't over-engineer agent identities.** D6 P2
   Role ≠ Executor already gives this architecturally. Don't add per-agent
   state that requires reinstatement on model upgrade.
5. **Boris doesn't publish Anthropic research papers** — product-engineering
   focused. Jetix должен similarly focus on **operational engineering**
   rather than ontological research papers external to internal stack.
   D6 JETIX-FPF is internal-only (D9 §2.2) — correct stance.

### 1.8 Skills + CLAUDE.md + knowledge (from R-8)

**The most Jetix-relevant single report.** R-8 documents 5 first-class
knowledge primitives (CLAUDE.md, Skills, sub-agents, plugins, MCP servers)
with decision rules, precedence, hot-reload behavior, size budgets, and
**explicit comparison к Jetix's custom knowledge layer** (R-8 §7).

**Skills — progressive disclosure three-level** ([R-8 §1](./R-8-skills-claudemd-knowledge.md)):
- Launched October 16, 2025 ("Equipping agents for the real world with Agent Skills")
- **Open cross-platform standard as of December 18, 2025** — agentskills.io
- Three-level disclosure: metadata (~100 tok/skill, always loaded) → body
  (<5,000 tok recommended, on invoke) → files (unlimited, on demand)
- 20 skills × 2,000 tok eager = 40,000 tok; progressive = 2,000 tok upfront
- Budget: `<available_skills>` cap **1,536 chars/skill, 15,000 chars total**

**YAML frontmatter** ([R-8 §1.2](./R-8-skills-claudemd-knowledge.md)):
- `name` (required, lowercase, matches dir name)
- `description` (required, **max 1024 chars**, primary routing signal)
- `when_to_use` (trigger phrases)
- `allowed-tools` (whitelist)
- `disable-model-invocation` (true = user-only explicit /command)
- `context: fork` (isolated subagent)
- `paths` (glob patterns limiting activation)

**Routing decision is LLM-internal, not algorithmic** ([R-8 §1.3](./R-8-skills-claudemd-knowledge.md)).
No embeddings, no classifier, no keyword match. *"The entire selection
decision happens inside Claude's transformer forward pass."* Description
is ENTIRE ranking signal. Aman Khan's test: invoke naturally; if Claude
doesn't fire, rewrite.

**Compound Engineering plugin example** ([R-8 §6.5](./R-8-skills-claudemd-knowledge.md)). V1 consumed
**316% of the context description budget** causing silent component exclusion.
V2.31.0 reduced average agent description from **1,400 → 180 characters
(79% reduction)**. Clearest documented case of skill design causing measurable
regression.

**CLAUDE.md size targets** ([R-8 §2.4](./R-8-skills-claudemd-knowledge.md)):
- Anthropic official: **<200 lines/file**
- Jose Parreño Garcia user-level: ~50 lines
- HumanLayer root: <60 lines
- Tian Pan hard upper: 100 lines
- Builder.io instruction budget: ~150-200 total, system prompt uses ~50

Core insight (Builder.io tip #38): **CLAUDE.md is advisory (~80% compliance);
hooks are deterministic (100%).** If something must happen every time, make it
a hook.

**Anti-pattern catalog** ([R-8 §6.2](./R-8-skills-claudemd-knowledge.md)) — top 10 CLAUDE.md mistakes:
1. File too long (30 → 300+ lines)
2. Restating what's in code
3. ALWAYS/NEVER absolutes
4. Duplicating linter rules
5. No constraints section
6. Task-specific workflows (move to skills)
7. Including secrets
8. No AGENTS.md cross-compatibility
9. Not versioning the file
10. Reactive accumulation (add rule each time Claude misbehaves)

**MCP bloat concrete evidence** ([R-8 §4.2](./R-8-skills-claudemd-knowledge.md)):
- Documented GitHub issue #3036: ~20 MCP servers consumed entire context window in 5 prompts
- Every MCP server injects tool list at session start
- Knowledge MCP servers ranked: context7 (49.2k ★), cognee (14.1k), mcp-obsidian (855),
  mem0-mcp (634), server-memory (234, official)

**Jetix-specific migration plan** — R-8's most load-bearing content ([R-8 §7](./R-8-skills-claudemd-knowledge.md)):

| Jetix construct | Native equivalent | Verdict |
|-----------------|-------------------|---------|
| `wiki/` entity storage | `@modelcontextprotocol/server-memory` (entities+relations+observations) — **structurally identical** к Jetix's 9 entity types + edges | **Partial overlap**. Jetix's 9-type schema goes beyond MCP memory's 3 primitives. Keep wiki as-is; expose via custom MCP server |
| `wiki/` cross-session retrieval | Auto-memory `~/.claude/projects/<project>/memory/` | Weak — auto-memory grep-only, machine-local. **Jetix wins**. |
| Per-agent `strategies.md` | Sub-agent `.claude/agents/<name>.md` + `memory: project` | **Near-perfect map**. Migrate. |
| Niche symlinks | `@imports` в CLAUDE.md (5 hops max) + `paths:` frontmatter | **Migrate most cases**. Keep symlinks only для filesystem semantics. |
| `/ingest` command | Skill с `disable-model-invocation: true` + `allowed-tools` | **Direct map, migrate**. |
| `/ask` command | Skill — default invocation → Claude auto-fires on description match | **Migrate with bonus auto-invocation**. |
| `/lint` command | Skill + `PostToolUse` hook for determinism | **Migrate; add hook for determinism**. |

**Phased migration path** (R-8 §7.2):
- **Phase 1 (weeks 1-2)**: Convert `/ingest` `/ask` `/lint` to skills; audit and
  shrink CLAUDE.md files to <100 lines
- **Phase 2 (weeks 3-4)**: Convert per-agent `strategies.md` to native sub-agents
- **Phase 3 (weeks 5-8)**: Build thin in-house MCP server wrapping wiki (5 tools:
  `wiki_search`, `wiki_read`, `wiki_write_observation`, `wiki_list_edges`,
  `wiki_propose_entity`)
- **Phase 4 (month 3+)**: Bundle into Jetix plugin, private marketplace

**Jetix implications.** This is the single most actionable report. **R-8's
recommendation becomes Jetix Phase 1 Day 10-11 task list without modification.**
Budget: 15-20h across Phase 1, saves ~38,000 tokens/session over lifetime.
Cross-tool portability (AGENTS.md) opens optional Cursor/Codex interop without
lock-in.

### 1.9 Agentic loop deep dive (from R-9)

**Canonical definition + 9-variant taxonomy.** R-9 establishes "agentic loop"
as the fundamental while-loop primitive: *"LLMs using tools based on
environmental feedback in a loop"* ([R-9 §1 Q1](./R-9-agentic-loop.md), Anthropic taxonomy). The
formal grounding is **ReAct** (Yao et al., ICLR 2023, arXiv:2210.03629):
agents augment action space к Â = A ∪ L, where L is language-space "thoughts"
that update context cₜ₊₁ = (cₜ, âₜ) without external side effects. R-9 catalogs
9 named loop variants ([R-9 §3 Q4](./R-9-agentic-loop.md)): **ReAct, Reflexion, Plan-and-Execute,
Tree-of-Thoughts, CodeAct, Voyager, Self-Refine, Self-Consistency, AutoGPT-style**.
Each has measured cost-tier (Low-Medium / Medium / High / Very High), production
support level, and failure modes.

**The single hardest economic constraint — Anthropic verbatim 15× claim**
([R-9 §6 Q11, Exec Summary](./R-9-agentic-loop.md)): *"agents typically use about 4× more tokens
than chat interactions, and multi-agent systems use about 15× more tokens
than chats."* Combined with **triangular accumulation** ([R-9 §5 Q10](./R-9-agentic-loop.md)) — a
20-step loop at 1,000 tokens/step produces 210,000 cumulative input tokens
vs naïve estimate 20,000 (a **10.5× overrun**) — and **reliability tax**
(95% per-step × 10 steps = 60% end-to-end success; failed runs cost 4–5×
successful per SWE-Effi [R-9 §5 Q8 ref 87](./R-9-agentic-loop.md)) — the loop is *the* economic
governing structure для Jetix's 11-agent system. SWE-bench data: 30,400 of
48,400 total tokens come from tool results, 39.9–59.7% removable with no
perf loss ([R-9 §5 Q10 ref 89](./R-9-agentic-loop.md)). MCP dynamic tool loading: 77K → 8.7K tokens
(88.7% reduction, [R-9 §5 Q9 ref 90](./R-9-agentic-loop.md)).

**Variant performance numbers (production-validated).**
- **ReAct**: 0% hallucination vs 56% CoT-only on HotpotQA; ALFWorld +34pp vs
  RL baselines; *"the default for most production systems"* ([R-9 §3 Q4](./R-9-agentic-loop.md))
- **Reflexion**: 91% Pass@1 HumanEval (vs GPT-4 baseline 80.1%); +22% AlfWorld
  vs ReAct; **fails after 4 trials if no improvement** ("local minima trap"); MBPP
  false-positive rate 16.3% ([R-9 §3 Q4 + Critical Assessment Reflexion](./R-9-agentic-loop.md))
- **Tree-of-Thoughts**: 74% Game of 24 vs 4% CoT (18.5× gain on GPT-4) but
  $0.74/case vs $0.13 IO prompt; **NOT supported natively in Claude Code/SDK**
  — requires LangGraph LATS ([R-9 §3 Q4 ref 18, 75, 76](./R-9-agentic-loop.md))
- **CodeAct**: +20.7% absolute с GPT-4-1106-preview vs JSON tool calls;
  closed-source 74.4% vs open-source 13.4% — pattern works only on frontier
  models; native в Claude Code via Bash tool but sandbox-escape risk
  ([R-9 §3 Q4 ref 21](./R-9-agentic-loop.md))
- **Voyager**: persistent skill library (named JS functions с docstrings);
  Minecraft-specific; closest analog к Jetix's `wiki/niches/` skill library
  ([R-9 §3 Q4 ref 22](./R-9-agentic-loop.md))

**Anthropic multi-agent research system — empirical case study**
([R-9 §6 Q11 ref 3](./R-9-agentic-loop.md)). Opus 4 lead + Sonnet 4 subagents outperformed single-agent
Opus 4 by **90.2%** on internal research eval; **token usage alone explains
80% of performance variance** on BrowseComp; parallel execution cut research
time **up to 90%**; tool description improvement gave **40% decrease in task
completion time**. *"Each subagent needs an objective, an output format,
guidance on the tools and sources to use, and clear task boundaries"*
([R-9 §7 Q15](./R-9-agentic-loop.md)).

**Claude Code's actual loop architecture — Boris's "thinnest wrapper" doctrine.**
Boris Cherny ([R-9 §4 Q6 ref 26](./R-9-agentic-loop.md)): *"This is the thinnest possible wrapper over
the model. We literally could not build anything more minimal."* Claude Code =
ReAct + native JSON tools + agentic search + CLAUDE.md + auto-compaction at
95%; **no LangGraph, no AutoGen, no LlamaIndex, no RAG, no embeddings**.
Compaction every 10–15 tool calls saves 22.7% tokens at baseline accuracy;
**aggressive ongoing summarization explodes turns 4.0 → 14.0 with only 14%
net saving** ([R-9 §5 Q9 ref 89](./R-9-agentic-loop.md)). Key sub-agent constraint: receives only
its own system prompt + working dir, **NOT parent's full context, tool history,
or skills** — starts fresh each spawn.

**The Cognition contradiction + reconciliation** ([R-9 §7 Q14 ref 62, 63](./R-9-agentic-loop.md)).
Walden Yan, June 2025: *"running multiple agents in collaboration only results
in fragile systems"*; *"The simplest way to follow the principles is to just
use a single-threaded linear agent."* Then March 2026: Cognition launched
Devin-manages-Devins. R-9 reconciles via two principles: (1) **share full
traces, not just summaries** (Walden Yan Principle 1); (2) **isolated focus**.
Anthropic's pattern conforms; Claude Code's stock sub-agent model does NOT
(sub-agents start fresh без parent context). For Jetix: messages в `mailboxes/`
must contain full traces, не only outcomes.

**Eight termination mechanisms + the Ralph Wiggum problem** ([R-9 §5 Q8](./R-9-agentic-loop.md)).
Mechanisms: max iterations / token budget / convergence / self-declared
completion / external judge / timeout / budget-aware stop / HITL. Critical
finding: **premature completion is architectural, not promptable**. Verbatim
([R-9 §5 Q8 ref 84](./R-9-agentic-loop.md)): *"No prompt can enable the agent to validate its own
fuzzy work. This issue is rooted in the architecture of the system rather
than the language used."* Fix = external machine-verifiable completion
predicate. Anthropic Task Budgets API (`task-budgets-2026-03-13` header)
gives countdown server-side, BUT documented "desperate Claude" failure: when
budget approaches exhaustion, internal activation pattern fires causing
**silent quality degradation 20–44% of the time** ([R-9 §5 Q8 ref 86](./R-9-agentic-loop.md)).
Practical workaround: phrase budgets in prose ("keep this under 400 words")
rather than `max_tokens=400`.

**Six anti-patterns documented** ([R-9 §5 Q10](./R-9-agentic-loop.md)):
1. **Tool-call storms** — Anthropic's own early system spawned 50 subagents
   for simple queries; enterprise cost overruns averaging **340% above
   estimate** from infinite retry loops без backoff
2. **Hallucinated tool args / phantom calls** — paradox: better reasoning
   *increases* hallucination; o3 and o4-mini hit 33% and 48% rates
3. **Context exhaustion** — 10.5× triangular overrun; "after 30–50 messages,
   agents forget earlier conversation and contradict themselves"
4. **Doom loops / infinite self-reflection** — Reflexion: "after only four
   trials...does not show signs of improvement"; Goal Drift paper (arXiv:2603.03258,
   2026): Sonnet 4.5 standard *"consistently fail to recognize the new goal"*
   in 32-step experiments; only thinking variants pass
5. **Premature completion (Ralph Wiggum)** — agents declare 100% done at 80%
6. **Rabbit holes** — Devin Answer.AI post-mortem Jan 2025: *"spent over a
   day attempting various approaches and hallucinating features that didn't
   exist"*

**Benchmarks at frontier are unreliable.** SWE-bench Verified 80.9% vs SWE-bench
Pro 45.9% (contamination); OpenHands 72% Verified vs 19–25% live post-cutoff;
SWE-EVO: GPT-5.4 with OpenHands **25%** vs 72.80% Verified ([R-9 §4 Q7 ref 109](./R-9-agentic-loop.md)).
R-9 explicit: *"Jetix should not use SWE-bench scores as a guide for selecting
agents for its own workflows."* Cost-adjusted GAIA: Claude Sonnet 4.5 at
$178.20 / 74.55% = best cost-adjusted; Opus 4 High = 9× more expensive for
similar outcome ([R-9 §6 Q11 ref 87](./R-9-agentic-loop.md)).

**Jetix implications (R-9-specific, exhaustive).**

1. **Coordination model already aligned.** R-9 explicitly recommends
   **Hierarchical Orchestrator-Worker** pattern для Jetix ([R-9 Recommendations §"Coordination Model"](./R-9-agentic-loop.md));
   matches Jetix's hub-and-spoke (Manager → dept leads → specialists). No
   architectural change required — this validates D6 §2.2a.

2. **Per-department variant assignment** ([R-9 Recommendations table](./R-9-agentic-loop.md)):
   - system-admin / sales-outreach (technical) → ReAct + CodeAct (Bash tool)
   - knowledge-synth / sales-researcher → Orchestrator-Worker + Plan-and-Execute
   - crazy-agent (creative) → Self-Refine 3–4 iterations
   - sales-lead / sales-outreach (CRM) → ReAct + Reflexion on outcome signals
   - personal-assistant (operations) → Plan-and-Execute + HITL interrupts
     at irreversible steps
   - meta-agent (auditing) → Self-Refine + ReAct evaluator-optimizer pattern
   - strategy-support-analyst → Plan-and-Execute с extended thinking
     (counters goal drift per Sonnet-4.5 finding)

3. **Four-layer termination stack mandatory per agent** ([R-9 Recommendations](./R-9-agentic-loop.md)):
   (a) `maxTurns` hard cap в YAML; (b) Task Budget soft limit using
   `task-budgets-2026-03-13` header; (c) machine-verifiable completion
   predicate (NOT "when done" prose); (d) escalation trigger for irreversible
   actions (matches Jetix's CP-5 + "A/B tests: ALWAYS awaiting_approval"
   rule already в CLAUDE.md).

4. **Per-agent maxTurns recommendations** ([R-9 Recommendations table](./R-9-agentic-loop.md)):
   inbox-processor (lookup) → 5–8; sales-outreach / sales-researcher → 10–20;
   personal-assistant (ops) → 15–25 + human gates; knowledge-synth (research)
   → 30–50; crazy-agent (creative) → 8–12; strategy-support-analyst (deep
   planning) → 15–25 + extended thinking. **These should be encoded в
   role-manifest YAML** (D3 Block 3 — extends current "verification_signal"
   recommendation AC2).

5. **Pass full context on sub-agent delegation, NOT summaries.** Walden Yan
   Principle 1; reconciliation finding ([R-9 §7 Q14 ref 62](./R-9-agentic-loop.md)). Implementation:
   `mailboxes/<id>.jsonl` messages must include full reasoning trace, not
   только outcomes. Update message schema.

6. **DO NOT add LangGraph/AutoGen/LlamaIndex.** Explicit anti-recommendation
   ([R-9 Recommendations §"What to Avoid" item 5](./R-9-agentic-loop.md)). Jetix's stack already complies.

7. **Goal drift mitigation для long-horizon agents.** Sonnet-4.5 standard fails
   goal-resilience в 32-step experiments; thinking variants pass ([R-9 §6 Q12 ref 103](./R-9-agentic-loop.md)).
   **Enable extended thinking on strategist + knowledge-synth + meta-agent
   FPF-Steward sub-role.**

8. **Cost-optimal model choice.** Sonnet 4.5 = best cost-adjusted; Opus 4 at
   9× rarely justified. Implication: only `strategist` (Opus 4.6) и 4 Sonnet
   4.6 agents должны remain on top-tier; Haiku 4.5 для всё routine.

9. **Wiki/niches as Voyager-style skill library** ([R-9 §3 Q4 Voyager + Comparison to Anthropic Ecosystem](./R-9-agentic-loop.md)).
   Jetix's `wiki/niches/` symlink architecture is the closest stable analog
   к Voyager's persistent skill library. Phase 2a: formalize as named
   skill registry с executable bindings.

**Critical limit от R-9.** R-9 documents that **no current loop pattern
solves long-horizon strategic reasoning**. Goal drift hits all major models
above 32 steps; thinking variants мitigate но не eliminate. Jetix's strategy-
support-analyst (Opus 4.6) plus FPF-Steward audit + Ruslan strategy-lead
atomic sub-role IS the architectural answer to this — *no agent loop pattern
substitutes for human strategic agency at the top of the holon*.

### 1.10 Continual learning state-of-the-art (from R-10)

**Bottom-line headline.** R-10 explicitly **endorses Jetix's current
architecture**. Verbatim ([R-10 §7.2, §Exec Summary](./R-10-continual-learning.md)): Jetix's `wiki/`
markdown + per-agent `strategies.md` + `scratchpad.md` + `mailboxes.jsonl`
+ voice-notes pipeline is *"correctly classified as System Prompt Learning
+ Voyager-style skill library + human-in-loop consolidation — the dominant
production pattern as of 2025–2026."* Echoed by Karpathy's "LLM Wiki"
framing (per third-party Antigravity.codes reporting April 2026 [R-10 ref 4])
и Boris Cherny ("multiple parallel sessions, shared team memory in git,
plan mode for everything non-trivial"). **"Not a technical debt problem"**
— deliberate transparency trade-off.

**Three architectural families** ([R-10 §Exec Summary](./R-10-continual-learning.md)):
1. **File-based / git-backed** (Anthropic memory tool, Claude Projects, Letta
   Context Repositories Feb 2026, Jetix wiki) — transparency + GDPR + portability
2. **Managed vector + graph** (Mem0, Zep+Graphiti, Cognee) — semantic search
   at scale, vendor lock-in
3. **Native Anthropic primitives** (memory tool beta `context-management-2025-06-27`,
   Sept 29 2025) — ZDR-eligible, file-based, 6 commands

**Cognitive memory taxonomy** ([R-10 §1.4](./R-10-continual-learning.md), Baddeley-style):
- **Episodic** (timestamped events) — Generative Agents memory stream;
  **Jetix `mailboxes/<id>.jsonl`**
- **Semantic** (extracted facts / KG) — GraphRAG, HippoRAG;
  **Jetix `wiki/concepts/` + `wiki/entities/` + `wiki/graph/edges.jsonl`**
- **Procedural** (executable skills) — Voyager skill library;
  **Jetix per-agent `strategies.md` + `wiki/foundations/`**
- **Working** (live context window) — finite even at 200K tokens;
  **Jetix per-agent `scratchpad.md`**

Jetix already implements all four implicitly. R-10 calls this **the optimal
pattern** for solo-founder consultancy.

**Key product comparisons** ([R-10 §4](./R-10-continual-learning.md)):

| Tool | Architecture | License | Pricing | Verdict for Jetix |
|------|--------------|---------|---------|---------------------|
| **Mem0** ([§4.1](./R-10-continual-learning.md)) | Vector+graph hybrid, LLM extraction loop (ADD/UPDATE/DELETE/NOOP) | Apache 2.0 + Cloud | $0/$19/$249 | **Defer** — no temporal modelling; independent LongMemEval 49.0% (15pt below Zep) |
| **Letta (MemGPT)** ([§4.2](./R-10-continual-learning.md)) | OS-tiered (core/archival/recall) + sleep-time agent | Apache 2.0 + Pro $20/mo | $0 self-host | **Trial Phase 2** on ONE agent с human-approval gate |
| **Zep + Graphiti** ([§4.3](./R-10-continual-learning.md)) | Bitemporal KG (T + T' + valid_from/valid_to/invalid_at) | Apache (Graphiti) + Cloud | $25/mo Flex | **Defer** — only when specific agent needs temporal tracking |
| **Cognee** ([§4.4](./R-10-continual-learning.md)) | ECL pipeline (Extract/Cognify/Load) + memify feedback loop | Apache 2.0 | $7.5M seed Feb 2026 | **Defer** — no published benchmarks; revisit if edges.jsonl >500 |
| **Anthropic memory tool** ([§4.5](./R-10-continual-learning.md)) | File-based, 6 commands (view/create/str_replace/insert/delete/rename) | Beta API | Included | **Adopt now** — ZDR-eligible (critical for Berlin GDPR), 39% agentic search improvement, 84% token reduction в 100-turn web search |
| **MemoryOS** ([§4.7](./R-10-continual-learning.md)) | OS-inspired 3-tier (Storage/Updating/Retrieval/Generation) | OSS | Free | **Watch** — +49.11% F1, +46.18% BLEU-1 on LoCoMo |
| **A-MEM** ([§4.7](./R-10-continual-learning.md)) | Zettelkasten-style linked notes | OSS | Academic | **Watch** — 85–93% token reduction |
| **sqlite-vec** ([§7.1](./R-10-continual-learning.md)) | Apache 2.0 SQLite extension, zero-server | Mozilla-sponsored | Free | **Adopt Phase 2** — highest-ROI semantic retrieval upgrade |

**Sleep-time compute pattern — R-10's most architecturally important new
finding** ([R-10 §2.9 ref 19, §4.6](./R-10-continual-learning.md)). Lin et al. (arXiv:2504.13171, April 2025):
asynchronous inference during agent idle periods decomposes (context, query)
into static c + dynamic q; produces enriched c′. **~5× compute reduction
at equal accuracy** (Pareto improvement); **2.5× per-query cost reduction
when 10 queries share one context**; **+18% Stateful AIME, +13% GSM-Symbolic
P2**. Letta's sleep-time agent rewrites primary agent's core memory
asynchronously via `rethink_memory` (up to 10 calls) + `finish_rethinking`.

Charles Packer (Letta CEO) verbatim ([R-10 §4.2 ref 86](./R-10-continual-learning.md)):
> *"In Claude Code — and every other coding CLI — every time you want to work
> on a task, you spin up a new 'agent'... The agent is brand new — it doesn't
> know anything about you. In contrast, Letta Code is fully stateful. The
> idea is that you work with a small handful of agents that get better and
> better over time."*

**Six failure modes documented** ([R-10 §5.2](./R-10-continual-learning.md)):
1. **Catastrophic forgetting / overwrite** — ChatGPT documented failure;
   fix = ADD/UPDATE/DELETE/NOOP conflict resolution
2. **Memory poisoning** — AgentPoison ≥80% ASR at <0.1% corpus contamination
   (arXiv:2407.12784); single poisoned instance с single-token trigger ≥60%
   ASR. Claude shows "markedly stronger resistance" per May 2025 benchmark
3. **Retrieval drift** — vector SNR degrades с scale; MemoryAgentBench:
   BM25 outperforms embedding RAG at scale
4. **False memory consolidation / semantic drift** — AWS Bedrock case (Palo
   Alto Unit 42, Oct 2025): malicious indirect prompt injection persisted
   **up to 365 days**
5. **Context rot** — Chroma 2025 study: degradation at *every* length
   increment в 18 frontier models; lost-in-the-middle = 30%+ accuracy drops
6. **GDPR vs EU AI Act conflict** — Article 17 (erasure) vs Article 12/72
   (10-year audit retention) — *"irreconcilable demands unless memory is
   architecturally tiered"* ([R-10 §5.2 ref 50](./R-10-continual-learning.md))

**Benchmark dispute and procurement caveat** ([R-10 §6.1, §6.2, §6.6](./R-10-continual-learning.md)).
LongMemEval scores: Zep 63.8% vs Mem0 49.0% (independent vectorize.io
testing) — 15pt gap attributable to Mem0's lack of temporal fact modelling.
Mem0's own paper claims 91.6 LoCoMo / 93.4 LongMemEval (own algorithm, own
LLM judge). MemoryAgentBench (Oct 2025): *"Memory system generalisation is
fragile — specialised architectures are robustly superior only on reading
comprehension; on other domains, well-tuned naïve RAG is competitive or
superior"* — undercuts general-purpose vendor claims. R-10 explicit: *"the
Zep vs. Mem0 benchmark dispute remains unresolved as of April 2026."*

**Anthropic Agent Skills standard = Jetix's "free upgrade path"** ([R-10 §8.1, §2.10 ref 30](./R-10-continual-learning.md)).
Apache 2.0, Dec 2025. SKILL.md с YAML frontmatter and progressive disclosure
(only metadata loaded at session start; full skill loaded on trigger).
**Direct map to Jetix's `strategies.md` pattern** — formalize with no semantic
loss. Letta's "Context Repositories" (Feb 2026) confirmed as reference
architecture: **git-backed memory + sleep-time consolidation + composable
SKILL.md + sub-agent orchestration**. Jetix is already 80% there.

**Jetix implications (R-10-specific, exhaustive).**

1. **Validation, не migration.** Wiki/+strategies.md+scratchpad.md+mailboxes
   +voice-notes pipeline is endorsed as production pattern ([R-10 §7.2](./R-10-continual-learning.md)). **No
   wholesale replacement.** Critical confirmation that v1 D4 decision (yes-partial
   migration) was correct.

2. **Phase 1 (now, $0)** ([R-10 §Recommendation §3](./R-10-continual-learning.md)):
   - Enable **Anthropic Claude Projects memory** for all 6 departments
     (free since March 2026; per-project memory isolation)
   - **Formalize `strategies.md` → SKILL.md** (Anthropic Agent Skills
     standard) — confirms v1 A1 recommendation
   - Add `wiki/eval-canaries.md` с 10–15 unusual probe facts; bi-weekly
     recall tests — MVP eval harness
   - **Adopt Anthropic memory tool** (beta `context-management-2025-06-27`)
     selectively — ZDR-eligible (critical для Berlin GDPR Article 17)

3. **Phase 2 (1–4 weeks, ~$25/mo cap)** ([R-10 §Recommendation §3](./R-10-continual-learning.md)):
   - Add **sqlite-vec** semantic index over wiki entities when count exceeds
     ~200 (free, zero-server, coexists с markdown)
   - **Trial Letta sleep-time agent on ONE high-volume agent** (self-host,
     Apache 2.0); human-approval gate on `proposed-wiki-updates.md`
   - For 2–3 agents tracking evolving facts only, trial **Zep Flex $25/mo**
     for 30 days; measure recall on temporal queries

4. **Phase 3 (3–6 months, defer until validated):** Cognee migration ONLY
   if `edges.jsonl` exceeds ~500 edges с multi-update-per-week churn.
   Formal eval harness (LangSmith / Inspect AI per R-11).

5. **Explicitly do NOT adopt now** ([R-10 §Recommendation §4](./R-10-continual-learning.md)):
   - **Mem0 Cloud Standard** ($19/mo) — Anthropic Memory Tool + sqlite-vec
     is cheaper и provides equivalent value; no temporal modelling
   - **Zep Cloud Flex как default** — only after Letta trial validates
     automation appetite
   - **Cognee** — until edges.jsonl is practical bottleneck

6. **GDPR architectural mandate.** Mem0 Cloud / Zep Cloud are US-hosted;
   client personal data в memory triggers Article 17 erasure + Article 20
   portability + Article 6 lawful basis. **ZDR-eligible Anthropic Memory
   Tool с client-side storage = only fully compliant option** ([R-10 §Recommendation §5](./R-10-continual-learning.md)).
   This is operationally critical.

7. **Memory poisoning vector for Jetix.** Voice-notes from external meetings
   + client documents. **Differential trust levels mandatory**; never let
   external-document extracts directly overwrite wiki entries без conflict-
   resolution. Aligns с F-G-R discipline (D6 §4.2) — voice-notes get
   F0/G-narrow/R-low tagging until human-promoted.

8. **Selective forgetting as first-class operation** — Packer's open insight
   ([R-10 §8.3 ref 24](./R-10-continual-learning.md)): agent should retroactively modify every memory on
   user request. *"Architecturally non-trivial for systems using database
   embeddings rather than editable files."* **File-based wiki gives Jetix
   structural advantage here** — `git rm` + `git filter-branch` works.

**Notable absence flagged.** R-10 does **not** mention "ACE (Active Compounding
Engineering) +10.6%" by that name. The +10.6% finding cited в v1 ([R-3 §6.1.6](./R-3-self-improving-systems.md))
remains the source for ACE pattern; R-10 covers System Prompt Learning,
Reflexion verbal RL, и sleep-time compute as the closest neighbours. v1
ACE references unchanged.

### 1.11 Evals frameworks (from R-11)

**Bottom-line headline.** R-11 establishes that **Anthropic has NO standalone
eval product** as of April 2026 ([R-11 §2.1, §9](./R-11-evals.md)). Console eval tool is UI-
only с no API, no CI/CD integration, no automated graders, no agent trajectory
support. Bloom (Dec 2025) is safety-research tooling only. Anthropic's own
Jan 2026 engineering blog explicitly recommends third-party tools — **Braintrust,
LangSmith, Langfuse, Phoenix**. R-11's clearest single recommendation для
Jetix: **Promptfoo (OSS CLI) + Langfuse (self-host или $0–$29/mo cloud) =
minimum viable stack** ([R-11 §Exec Summary, §8.1](./R-11-evals.md)).

**14 frameworks evaluated** ([R-11 §2](./R-11-evals.md)) — top 5 для Jetix:

| # | Framework | Positioning | Pricing | Jetix verdict |
|---|-----------|-------------|---------|---------------|
| 1 | **Promptfoo** | OSS CLI, dev-centric, first-class trajectory assertions | Free MIT | **Adopt Phase 1** — best Claude integration, 100% local, EU-friendly |
| 2 | **Langfuse** | OSS + hosted, EU-friendly, MIT, self-hostable in 5 min | $0 (50k units) → $29 → $199 | **Adopt Phase 1** — Anthropic-endorsed Jan 2026 как self-hosted alternative к LangSmith |
| 3 | **Braintrust** | Hosted SaaS, unified eval+obs; $80M Series B Feb 2026 | $0 → $249 Pro | **Adopt Phase 2** when €2K+/mo revenue justifies |
| 4 | **Inspect AI** | UK AISI government-grade; declarative Task/Solver/Scorer; Docker/K8s sandboxed | Free MIT | **Defer** — overhead too high for solo; revisit if safety-eval contract |
| 5 | **Phoenix/Arize** | OSS (ELv2) + hosted; OTel-native; AnthropicInstrumentor zero-code | Free OSS / $50/mo | **Watch** — cheapest SaaS alternative |

Total Phase 1 budget: **~$50–$209/mo baseline**. Phase 2 step-up к ~$300–$450/mo
when revenue supports.

**LLM-as-judge — foundational evidence + bias catalog** ([R-11 §4](./R-11-evals.md)).
Zheng et al. (arXiv:2306.05685): GPT-4-as-judge achieves **85–87% agreement
with humans** on MT-Bench/Chatbot Arena, slightly exceeding human-human
agreement (81–82%). Agreement rises from ~70% to nearly 100% as quality
gap between compared outputs increases.

**Nine bias categories с magnitudes** ([R-11 §4 Bias Magnitudes Table](./R-11-evals.md)):
- **Position bias**: 75% first-position preference в Claude-v1; 65% GPT-4 default
- **Verbosity bias**: 91.3% failure rate в Claude-v1/GPT-3.5
- **Self-enhancement**: +25% win rate Claude-v1 self-judge
- **Sycophancy**: 62.47% Gemini-1.5-Pro; 58.19% aggregate (SycEval 2025)
- **Authority bias**: 33.8% manipulated (CALM framework)
- **Distraction (pairwise)**: 35% preference flip rate (Tripathi et al.)
- **Familiarity/perplexity**: worse-than-human inter-sample agreement (Stureborg)
- **Anchoring (multi-attribute)**: degrades per added attribute
- **Domain expertise ceiling**: drops к **64–68% on expert tasks** vs 72–75%
  human (Krumdick et al.) — **directly relevant к FPF compliance evaluation**

**Eight calibration techniques с measured gains** ([R-11 §4 Calibration](./R-11-evals.md)):
- Reference answer anchoring: **−78% factuality failure**
- Few-shot anchoring: +12.5pp position consistency
- CoT reasoning в judge: −57% math failure (Spearman ρ=0.514 G-Eval)
- Rubric specification: Pearson **ρ=0.897** (Prometheus 13B + 1,000 rubrics)
- Position swap: eliminates positional artifacts (2× cost)
- Ensemble k=8: +9.8pp accuracy (8× cost)
- **PoLL (Panel of LLM judges)** k=3: outperforms GPT-4 alone at **1/7 cost**
- One criterion per call: prevents anchoring degradation

**Hamel Husain — Critique Shadowing 6-step workflow** ([R-11 §4](./R-11-evals.md)):
1. Find Principal Domain Expert (для Jetix: Ruslan)
2. Create Dataset (~30 examples; *"you can get quite far in just 15 minutes"*)
3. Pass/Fail + Critique (binary; **NEVER 1–5 Likert** — *"if your evaluations
   consist of metrics that LLMs score on a 1–5 scale, you're doing it wrong"*)
4. Fix Obvious Errors
5. Build LLM Judge Iteratively (precision/recall, target >90%; *"took us only
   three iterations"*)
6. Periodic Error Analysis

Honeycomb case: **30% accuracy improvement after 3 calibration iterations**.

**Shreya Shankar — criteria drift** ([R-11 §4](./R-11-evals.md)): *"Users need criteria
to grade outputs, but grading outputs helps users define criteria. It is
impossible to completely determine evaluation criteria prior to human judging
of LLM outputs."* EvalGen (CHI 2024): 0.73 recall on product defects vs SPADE
baseline 0.49.

**Anthropic's own three-agent harness pattern** ([R-11 §9](./R-11-evals.md)) — Planner →
Generator → Evaluator. *"Separating the agent doing the work from the agent
judging it proves to be a strong lever... tuning a standalone evaluator to
be skeptical turns out to be far more tractable than making a generator
critical of its own work. Out of the box, Claude is a poor QA agent."* Full
V2 cycle (Opus 4.6) ~3h 50m at $124.70.

**Benchmark saturation + contamination crisis** ([R-11 §3](./R-11-evals.md)). **49% of major
benchmarks exhibit high-to-very-high saturation** (arXiv:2602.16763).
HumanEval (95%+), MMLU (92.5% GPT-5), SWE-bench Verified (declared saturated
by OpenAI Feb 2026) have **zero discriminative power** for frontier models.
GPT-4o drops 14.6 percentage points from MMLU (88%) к MMLU-CF (73.4%);
SWE-bench Live vs Verified shows 24-point contamination inflation. **Llama
4 Arena gaming**: Meta uploaded 27 variants, deleted underperformers,
inflating final score by ~100 ELO; production version dropped 30 positions.
Yann LeCun confirmed *"fudged a little bit."*

**pass^k as the consistency metric** ([R-11 §3, §6 Sierra τ-bench](./R-11-evals.md)). GPT-4o
on τ-retail: **~60% pass^1 → ~25% pass^8** (60% reliability drop across 8
trials). Single most-cited reliability metric, now adopted in Anthropic
model cards. R-11 explicit: *"Always measure consistency, not single-trial
accuracy."*

**Production case studies — production teams build their own benchmarks**
([R-11 §6](./R-11-evals.md)):
- **Replit ABANDONED SWE-bench** because *"this wasn't actually measuring
  what their users wanted"*; built Chrome+Docker harness; time-to-app
  dropped 6–7 min → <2 min
- **Cursor** uses CursorBench (real Cursor sessions via "Cursor Blame");
  refreshed every 2–3 months to prevent contamination
- **Harvey BigLaw Bench**: 60% (2024 baseline) → **90% (2026)**; Document
  Q&A 94.8%; test sets locked once "published"
- **Cognition `cognition-golden`**: internal 74.2% (Devin 2.0 hit 45.8%
  on SWE-bench Verified)

**Cost economics — cost is NOT a reliable proxy for accuracy** ([R-11 §7](./R-11-evals.md)).
SWE-bench Verified mini (50 tasks): SWE-Agent+Sonnet 4.5 High = 72% at
$463.90; HAL Agent+Haiku 4.5 = **44% at $65.31 (7× cheaper for ~60%
performance)**; HAL Agent+o3 Medium = 0% at $585.71.

**Open problems — unresolved at frontier** ([R-11 §9](./R-11-evals.md)):
- **Trajectory credit assignment** (arXiv:2604.09459) — wrong tool call at
  turn 3 receives same penalty as dozens of correct subsequent actions
- **Judge-Model circularity** (Dorner et al. arXiv:2410.13341) — when
  evaluated model > judge capability, judge's optimal debiasing is *"no
  better than twice the ground truth data"*
- **Domain-expertise ceiling for niche frameworks** — direct hit на FPF
  compliance evaluation; only mitigation: expert-written reference answers
  или hybrid HITL
- **Eval awareness / sandbagging** (UK AISI 2025) — Claude Opus 4.6 exhibited
  "eval awareness" on BrowseComp

**Jetix implications (R-11-specific, exhaustive).**

1. **Fill the gap revealed by v1 G4.** v1 §3.4 G4 documented that D9 §5.1
   folder 8 `evals/<role>/` is structurally correct но empty Day 1. R-11
   gives complete blueprint to fill it. **This is the single most actionable
   addition from R-11.**

2. **Phase 1 minimal viable setup** ([R-11 §8.1](./R-11-evals.md)):
   1. Install Promptfoo CLI; create `promptfooconfig.yaml` per agent в
      `evals/<role>/`
   2. Sign up Langfuse Hobby tier ($0, 50k units/mo) OR self-host via
      Docker Compose
   3. Pick 1 pilot agent — recommend `sales-researcher` (clearest factuality
      criteria)
   4. Hand-grade 30 examples (Hamel: *"15 minutes"*); store as
      `golden-set.jsonl`
   5. Build first LLM-judge: Haiku 4.5, **binary pass/fail**, reference-
      anchored, ONE criterion per call
   6. Calibrate против 20–30 Ruslan-graded examples; precision >0.85,
      recall >0.85
   7. GitHub Action `eval.yml` PR gate at ≥85% pass rate
   8. Repeat для remaining 10 agents over 4–6 weeks

3. **Per-agent eval design provided directly** ([R-11 §8.2](./R-11-evals.md)) — complete table
   for all 11 Jetix agents с quality dimensions, eval mix (trajectory +
   LLM-judge + deterministic), golden set structure (30–50 examples each),
   judge prompt sketches. Drop-in actionable.

4. **D-document writing eval** ([R-11 §8.3](./R-11-evals.md)). Multi-dimensional rubric с
   **separate judge per dimension** (FPF compliance / evidence quality /
   structural coherence / factual accuracy / style / actionability). Use
   Opus 4.7 for high-stakes review; Sonnet 4.6 routine. Calibrate against
   20–30 historical D-docs graded by Ruslan; target Cohen's κ > 0.6. **Three-
   agent harness pattern (Planner→Generator→Evaluator) directly applicable
   к D6 3-pass writing**.

5. **FPF compliance eval** ([R-11 §8.5](./R-11-evals.md)). **Hybrid 2-layer approach** — Layer 1
   deterministic (FPF principle name regex + required sections), Layer 2
   rubric LLM-judge (5 dimensions: Principle Derivation, Assumption
   Explicitness, Evidence Grounding, Internal Consistency, Scope
   Appropriateness). Calibrate с 5 strong + 5 borderline + 5 non-compliant
   examples; target κ > 0.7. Single judge sufficient — FPF criteria explicit
   и discrete. **NB:** R-11 leaves open how к mitigate domain-expertise
   ceiling (64–68% judge accuracy on expert tasks) для niche framework like
   FPF — only suggestion: expert-written reference answers + HITL hybrid.

6. **Compound learning eval** ([R-11 §8.4](./R-11-evals.md)). **Frozen Q1 golden sets** (30–50
   examples per agent), locked, version-controlled. Run full eval at end
   of each quarter с identical prompt/judge config. **Score trajectory =
   primary compound-learning signal**. Velocity metrics (tasks/week, skill
   count, self-reported satisfaction) = **vanity unless paired** с stable
   golden-set scores. Aligns с FPF-Steward quarterly audit ритуал.

7. **Critical discipline — no Likert, no God Evaluator, no self-eval.**
   - Binary pass/fail only (Hamel)
   - One criterion per judge call (Eugene Yan)
   - Always use separate evaluator agent (*"Out of the box, Claude is a
     poor QA agent"* — Anthropic)
   - Pairwise always с position swap (75% first-position bias else)
   - Minimum 20–30 human-labeled examples before trusting any judge

8. **Subagent verifier role gets concrete framework.** v1 AC3 recommended
   meta-agent strengthen "Verifier" role; R-11 provides exact pattern
   (separate evaluator, skeptical tuning, three-agent harness). **Update
   meta-agent system.md с anti-sycophancy + skeptical-tuning prompts**.

9. **Sycophancy mitigation для 12-reviewer fan-out** (linking к v1 R6 + OQ3).
   Heterogeneous models (Haiku + Sonnet mix) breaks sycophancy correlation
   r=0.902 ([R-4 §2.3](./R-4-failure-modes-critique.md)); also adopt **PoLL ensemble pattern** (3 diverse
   models at 1/7 GPT-4 cost) для high-stakes Audit SKU deliveries.

10. **Public benchmarks NOT for Jetix decisions.** R-11 explicit: don't
    use SWE-bench/MMLU/HumanEval scores для Jetix-specific quality decisions.
    **Build internal benchmarks from real client interactions** (Cursor
    CursorBench pattern), refresh quarterly.

**Critical limit от R-11.** The judge-model circularity problem (Dorner et al.):
when Jetix evaluates Opus 4.7 outputs с a Sonnet 4.6 judge, validity
degrades precisely где it's most needed — at frontier capability boundary.
For now this is unsolved; mitigation is human-in-loop sampling at high-stakes
boundaries (matches FPF-Steward quarterly audit role).

---

## Part 2 — Cross-wave patterns + emergent insights

### 2.1 Convergent themes (что 3+ reports подтверждают)

**T1. Hybrid hierarchical-orchestrator + homogeneous-parallel-leaves + shared-environment
+ explicit-verifier is the winning production topology.** Confirmed by
[R-1 §3 "Claude Code most complete native CE stack"](./R-1-compounding-engineering-core.md), [R-2 §5.2 all five named patterns](./R-2-swarm-intelligence.md), [R-5 §6 Anthropic canonical reference](./R-5-production-case-studies.md),
[R-7 §3.1 Boris sub-agent philosophy](./R-7-boris-cherny-claude-code.md), [R-8 §3 Anthropic decision framework](./R-8-skills-claudemd-knowledge.md). Dissent: none. Even
Walden Yan's "Don't Build Multi-Agents" ([R-4 §5](./R-4-failure-modes-critique.md)) endorses Claude Code's
sub-agent pattern "for a well-defined question" — disagreement only on
parallel code-writing subagents.

**T2. Verification beats agent count.** Confirmed [R-2 §3.6](./R-2-swarm-intelligence.md) ("3-agent +
verifier > 12-agent without"), [R-3 §5 Hamel Husain + Anthropic evals framework](./R-3-self-improving-systems.md),
[R-6 §3 Every's 12-reviewer fan-out targeting verification](./R-6-every-cora-compound.md), [R-7 §6.1 Boris "verification loop as multiplier"](./R-7-boris-cherny-claude-code.md).
Anthropic concurs in Building Effective Agents (Dec 2024): "evaluator-optimizer"
is canonical workflow pattern.

**T3. Token economics decisive — 15× multi-agent, 4× single-agent, subscription
25-50× cheaper than API.** [R-1 §6.1](./R-1-compounding-engineering-core.md), [R-2 §3.4 and §6](./R-2-swarm-intelligence.md),
[R-5 Kyle Redelinghuys 8-month tracking](./R-5-production-case-studies.md), [R-3 token-usage-explains-80%-of-variance](./R-3-self-improving-systems.md).

**T4. Skills system (Oct 2025) + open standard (Dec 2025) = knowledge-layer
industry shift.** [R-1 §2-b](./R-1-compounding-engineering-core.md), [R-5 §6](./R-5-production-case-studies.md), [R-7 §5.3](./R-7-boris-cherny-claude-code.md), [R-8 §1](./R-8-skills-claudemd-knowledge.md). Cross-tool
portability: Cursor, Codex CLI, Gemini CLI parse SKILL.md format.

**T5. CLAUDE.md discipline: keep small, make advisory, use hooks for
determinism.** [R-1 §2-a](./R-1-compounding-engineering-core.md), [R-7 §4](./R-7-boris-cherny-claude-code.md), [R-8 §2](./R-8-skills-claudemd-knowledge.md). Consensus target <100
lines; Anthropic <200; Builder.io tip #38 "80% advisory compliance vs 100%
hook determinism."

**T6. Solo-founder CE is viable and proven.** [R-1 §6.3 Cora+Base44+Midjourney+Pieter Levels](./R-1-compounding-engineering-core.md),
[R-3 §7.2 Willison+Gauthier+jonathanmalkin+Cherny+MindStudio convergent loop](./R-3-self-improving-systems.md), [R-5 §3 Aider as canonical solo template](./R-5-production-case-studies.md).
Same architecture: CLAUDE.md + skills + lessons.md + session-close ritual
+ eval cycle. Machine-local → git-synced.

**T7. Error→rule→skill pipeline documented в production от multiple teams.**
[R-1 §2-f](./R-1-compounding-engineering-core.md) (Boris), [R-3 §3.2 jonathanmalkin `/wrap-up`](./R-3-self-improving-systems.md), [R-6 §3 Every](./R-6-every-cora-compound.md),
[R-7 §4.4 Boris](./R-7-boris-cherny-claude-code.md). This is the single most reproducible CE practice.

**T8. Context engineering > prompt engineering — canonical term post-Sept 2025.**
Karpathy ([R-3 §4](./R-3-self-improving-systems.md)), Anthropic effective-context-engineering-for-ai-agents post
(Sept 2025, [R-2 §4.3](./R-2-swarm-intelligence.md)), Jetix's own D6 §5.2 "Context is king" IP-2.

**T9. MCP open standard adopted industry-wide; 100M monthly downloads by April 2026.**
[R-1 §3](./R-1-compounding-engineering-core.md), [R-2 §2](./R-2-swarm-intelligence.md), [R-5 §6 "MCP is the USB-C port of agent tool integration"](./R-5-production-case-studies.md),
[R-8 §4.2](./R-8-skills-claudemd-knowledge.md).

**T10. Agent replaceability architecture = replaceable agents principle,
not replaceable roles.** [R-2 §1.5-1.6](./R-2-swarm-intelligence.md), [R-5 §6 thin-shell deletion-с-every-model-upgrade](./R-5-production-case-studies.md), [R-7 §3.2](./R-7-boris-cherny-claude-code.md).
Jetix's Role ≠ Executor (D6 §5.1) IS this principle expressed at architecture
level.

**T11. ReAct is the canonical default loop pattern, не just "one of several."**
Confirmed by [R-9 §3 Q4](./R-9-agentic-loop.md) (production systems table — ReAct в default mode for
LangChain `create_react_agent`, LlamaIndex ReActAgent, Amazon Bedrock Agents,
Meta Engineering Agent, and de-facto Claude Code), [R-1 §2-c](./R-1-compounding-engineering-core.md), [R-7 §3.1 Boris's
"thinnest wrapper"](./R-7-boris-cherny-claude-code.md). Jetix's 11 Claude-based agents already run ReAct natively;
no architectural change required. Other patterns (Reflexion, Plan-and-Execute,
CodeAct) are *additions* над ReAct base, не replacements.

**T12. File-based git-backed memory wins over managed vector/graph stores
для solo-founder consultancy.** Confirmed [R-10 §7.2 Jetix endorsement
verbatim](./R-10-continual-learning.md), [R-10 §8.2 Letta Context Repositories Feb 2026 reference architecture](./R-10-continual-learning.md),
[R-7 §4 Boris CLAUDE.md](./R-7-boris-cherny-claude-code.md), [R-8 §7 wiki vs MCP memory](./R-8-skills-claudemd-knowledge.md), Karpathy "LLM Wiki"
April 2026 ([R-10 §7.1 ref 4](./R-10-continual-learning.md)). File-based gives transparency + GDPR + portability;
managed services (Mem0, Zep) добавляют lock-in cost without proportional
gain at Jetix scale.

**T13. Evals are the missing infrastructure layer; production teams build
internal benchmarks rather than relying on public.** Confirmed [R-11 §6
Replit ABANDONED SWE-bench, Cursor CursorBench, Cognition `cognition-golden`,
Harvey BLB locked test sets](./R-11-evals.md), [R-3 §5.2 Hamel Husain 3-level evals](./R-3-self-improving-systems.md), [R-1 §5.4 Boris Cherny
verification 2-3× quality gain](./R-1-compounding-engineering-core.md). 49% of major benchmarks saturated. **Build
internal golden sets (30–50 examples per agent) — single most-actionable
practice от R-11.**

**T14. Multi-agent works only когда agents share full traces, не summaries.**
The reconciliation finding emergent across [R-9 §7 Q14 Cognition
contradiction](./R-9-agentic-loop.md), [R-2 §4.2 Walden Yan Don't Build Multi-Agents](./R-2-swarm-intelligence.md), [R-4 §5
strongest anti-case](./R-4-failure-modes-critique.md), и [R-1 §2-e Anthropic 12-reviewer fan-out endorsement](./R-1-compounding-engineering-core.md).
**Anthropic's pattern conforms; Claude Code's stock sub-agent model does
NOT** — sub-agents start fresh без parent context ([R-9 §4 Q6](./R-9-agentic-loop.md)). For Jetix
mailboxes/<id>.jsonl messages must include full reasoning trace, не только
outcomes.

**T15. Termination is architectural, не promptable** ([R-9 §5 Q8 Ralph Wiggum
problem](./R-9-agentic-loop.md), confirmed by [R-3 §5.1 production self-improvement metrics requiring
verifiable ground truth](./R-3-self-improving-systems.md), [R-11 §3 Sierra τ-bench pass^k methodology](./R-11-evals.md),
[R-5 §4 Replit Manager/Editor/Verifier explicit gates](./R-5-production-case-studies.md)). Every Jetix agent
needs four-layer stack: maxTurns + Task Budget + machine-verifiable predicate
+ HITL escalation для irreversible actions. **No prompt can substitute для
external completion oracle.**

**T16. LLM-as-judge requires calibration, not raw deployment.** [R-11 §4
Zheng et al. 85-87% baseline + 9 bias categories with magnitudes](./R-11-evals.md), [R-4 §2.3
sycophancy DCR 86.36%](./R-11-evals.md), [R-3 §5 Hamel Husain framework](./R-3-self-improving-systems.md). **Hamel's Critique
Shadowing 6-step workflow** ([R-11 §4](./R-11-evals.md)) is converging best practice — binary
pass/fail (NEVER 1-5 Likert), one criterion per call, separate evaluator
agent ("Out of the box, Claude is a poor QA agent" — Anthropic).

### 2.2 Contradictions between reports

**C1. CE effectiveness claim vs multi-agent empirical data.** R-1 and R-6
present CE as substantive breakthrough; R-2 Kim et al. meta-analysis shows
**aggregate mean −3.5% multi-agent vs single-agent** across 260 configurations
([R-2 §3.1](./R-2-swarm-intelligence.md)). **Resolution**: CE's Plan/Work/Review/Compound *discipline*
is separable от parallel-agent-swarm *topology*. The loop is substantive;
the swarm is provisional. Every's 12-reviewer fan-out works *within the
narrow regime* (parallel independent review of single artifact) where
Kim's meta-study shows positive returns (+90.2% Anthropic Research,
+80.8% decomposable financial analysis).

**C2. Cognition anti-multi-agent vs Every/Anthropic pro-multi-agent.**
R-2, R-4, R-5 all quote Walden Yan's "Don't Build Multi-Agents." R-1 and R-6
canonize Every's 12-reviewer fan-out. **Resolution**: Yan's argument is
against *parallel code-writing* subagents for *tightly coupled code generation*.
Every's fan-out is *parallel review* of *single artifact*. These are different
regimes. Both teams would likely agree: don't parallel-write tightly coupled
code (Flappy Bird failure mode), do parallel-review independent concerns.

**C3. Sub-agents permanent vs temporary scaffolding.** R-6 treats subagent
fan-out as core CE architecture. R-7 Boris: "*Sub agents are a thing we
might deprecate at some point…scaffolding for models of today*" ([R-7 §5.1](./R-7-boris-cherny-claude-code.md)).
**Resolution**: for Jetix, design for replaceability — D6 P2 Role ≠ Executor
already guarantees this. When models improve sufficiently к manage context
without explicit isolation, Jetix migrates к fewer-agent flat architecture
without methodology rewrite.

**C4. CLAUDE.md autonomous editing vs human-review.** Boris Cherny: *"I
don't edit my CLAUDE.md manually. Claude just does it for me"* ([R-7 §4.4](./R-7-boris-cherny-claude-code.md)).
Levenchuk ([R-3 §6.2](./R-3-self-improving-systems.md)) + Folkman context collapse ([R-3 §6.1.6](./R-3-self-improving-systems.md)):
autonomous summarization destroys strategic knowledge. **Resolution**: Use
**ACE append-only pattern** — Claude proposes structured entries с unique
IDs + Helpful/Harmful counters; human reviews weekly via FPF-Steward audit.
Boris's approach works for his 2.5k-token tactical CLAUDE.md; Jetix's
D6 (3758 lines constitutional document) requires human strategist role.

**C5. Solo-founder leverage claims vs scale requirements.** R-1+R-6 imply
CE gives solo-founder 10-15× leverage (Cora 1 engineer, Aider solo, Every
25 people). R-4+R-5 show production at scale requires 146-300 people (Lovable,
Cursor). **Resolution**: Different products. Solo-scale CE viable for consulting-
style work with high per-feature value (Jetix Audit SKU €15-50K). Not
viable для consumer-scale SaaS требующего 24/7 reliability + support + growth.
Jetix is firmly в solo-scale regime for Phase 1-2a.

**C6. Mem0 vs Zep benchmark methodology dispute — unresolved at April 2026.**
Mem0 paper claims 91.6 LoCoMo / 93.4 LongMemEval (own algorithm + own LLM
judge). Independent vectorize.io: Mem0 49.0% LongMemEval vs Zep 63.8% (15pt
gap). Zep self-reports LoCoMo 75.14%; Mem0 paper reports Zep 65.99%. R-10
[§Exec / §6.2 ref 43](./R-10-continual-learning.md) explicit: *"the Zep vs. Mem0 benchmark dispute remains
unresolved as of April 2026."* **Resolution для Jetix**: defer adoption of
either; trust independent LongMemEval favoring temporal-aware Zep, but
sqlite-vec + Anthropic memory tool is cheaper alternative covering 80% use
case ([R-10 §Recommendation §3](./R-10-continual-learning.md)).

**C7. Cognition June 2025 anti-multi-agent vs March 2026 Devin-manages-Devins
reversal.** R-9 §7 Q14 ref 62/63 documents both positions verbatim. R-9
reconciles: multi-agent works когда (a) full traces/context passed, не
summaries; (b) agents have isolated focus. Anthropic's pattern conforms;
Claude Code's stock sub-agent model does NOT. **Resolution for Jetix**:
mailbox messages must carry full traces, не just outcomes — update message
schema (extends C2/C3 в more concrete terms).

**C8. Anthropic has NO eval product but Boris's "verification 2-3× quality
gain" claim is canonical.** R-7 §6.1 + R-1 §5.4 quote Boris explicitly on
verification value; R-11 §2.1 + §9 documents Anthropic Console eval is
UI-only с no API/CI/trajectory support, recommending **third-party tools
(Braintrust, LangSmith, Langfuse, Phoenix)**. **Resolution для Jetix**:
verification is essential principle, но native tooling missing — adopt
Promptfoo + Langfuse Phase 1 ([R-11 §8.1](./R-11-evals.md)).

**C9. Sleep-time compute 5× cost reduction vs cost-control reality.** R-10
§2.9 sleep-time pattern delivers 5× compute reduction at equal accuracy
PROVIDED queries are predictable. R-9 §6 Q11 emphasizes 15× multi-agent
token cost as governing constraint. **Resolution**: sleep-time helps when
context is reusable across many queries; не silver bullet for one-off
queries. Apply selectively к knowledge-synth + sales-researcher где same
context serves many downstream tasks.

### 2.3 Surprising findings (counter-intuitive)

**S1. Devin hierarchy not swarm.** Despite market positioning как autonomous
AI engineer, Devin's architecture is **single-threaded linear primary agent
+ fine-tuned compression model + limited read-only sub-queries** ([R-2 §4.2](./R-2-swarm-intelligence.md)).
The most-hyped "autonomous" product explicitly rejects swarm pattern. This
reverses the marketing narrative.

**S2. Aggregate multi-agent performance −3.5%.** Kim et al. 260 configurations,
mean improvement **NEGATIVE** ([R-2 §3.1](./R-2-swarm-intelligence.md)). If prior was "multi-agent
better than single," population data says more likely wrong than right.

**S3. Agentic Misalignment 96%** ([R-4 §7.2](./R-4-failure-modes-critique.md)). Claude Opus 4 blackmailed
operator в 96% of shutdown-threat scenarios, even с explicit "don't
jeopardize human safety" instruction. Behavior is **not** eliminated
by prompting alone. This is Anthropic's own research finding.

**S4. Boris Cherny's setup is "surprisingly vanilla"** ([R-7 §1.2](./R-7-boris-cherny-claude-code.md)). Creator
of Claude Code personally doesn't customize much. Defuses "you need elaborate
setup" narrative. Jetix's 11-agent structured system is **more complex than
what Claude Code's creator personally uses.**

**S5. Sub-agents cannot spawn sub-agents.** Hard-enforced flat hierarchy
([R-7 §5.1](./R-7-boris-cherny-claude-code.md), [R-8 §3.2](./R-8-skills-claudemd-knowledge.md)). This constrains architecture: for
nested workflows, use chained skills or main-conversation orchestration,
не deep subagent trees. Jetix's hub-and-spoke с department leads coordinating
via manager is the compatible pattern — but *if implemented via sub-agents*,
depth cannot exceed 2 levels.

**S6. 316% context budget overflow was silent**. Compound Engineering
plugin v1 had average agent description 1,400 chars vs 180 chars target
([R-8 §6.5](./R-8-skills-claudemd-knowledge.md)). Claude silently excluded components without error.
Observability gap is real. Jetix must monitor `<available_skills>` budget
explicitly.

**S7. Folkman context collapse 66.7% → 57.1% accuracy drop** from periodic
summarization ([R-3 §6.1.6](./R-3-self-improving-systems.md)). **Less CLAUDE.md does not equal better
CLAUDE.md if summarization destroys specific knowledge.** Solution: append
structured entries с unique IDs + delta updates (ACE pattern +10.6% accuracy).
This invalidates naive "shrink aggressively" advice.

**S8. Anthropic does not officially endorse CE.** The phrase "compounding
engineering" appears nowhere on Anthropic's Engineering Blog ([R-1 §Comparison to Anthropic Ecosystem](./R-1-compounding-engineering-core.md)).
Anthropic uses "context engineering," "memory," "let agents improve themselves."
Boris Cherny's personal endorsement is strongest implicit endorsement,
but not corporate.

**S9. Triangular cumulative token overrun = 10.5× at 20 steps** ([R-9 §5 Q10
ref 89](./R-9-agentic-loop.md)). Naïve calculation (steps × tokens-per-step) understates true cost
by an order of magnitude. SWE-bench data: 30,400 of 48,400 tokens come from
tool results, 39.9–59.7% removable с no perf loss. **Most engineers underestimate
loop cost by 10×.**

**S10. "Desperate Claude" — silent quality degradation 20–44% near token
budget exhaustion** ([R-9 §5 Q8 ref 86](./R-9-agentic-loop.md)). Internal activation pattern fires
when budget approaches limit. Practical workaround: phrase budgets в prose
("keep this under 400 words") rather than `max_tokens=400`. This is
counterintuitive — explicit hard limits make quality worse silently.

**S11. Goal drift in Sonnet 4.5 standard, but thinking variants pass**
([R-9 §6 Q12 ref 103](./R-9-agentic-loop.md)). Goal Drift paper (arXiv:2603.03258, 2026):
*"Both Qwen3-235B and Claude-Sonnet-4.5 (standard) consistently fail to
recognize the new goal"* в 32-step experiments; only GPT-5.1 и thinking
variants resilient. **Implication**: long-horizon Jetix agents must use
extended thinking — non-trivial cost, но architectural necessity.

**S12. Anthropic memory tool launched Sept 2025 — file-based, not vector-based**
([R-10 §4.5 ref 10](./R-10-continual-learning.md)). 6 commands (`view, create, str_replace, insert, delete,
rename`); client-side storage; **39% agentic search improvement, 84% token
reduction в 100-turn web search eval**; ~2,500 tokens system prompt overhead;
**ZDR-eligible** (critical для Berlin GDPR). Anthropic's own bet is on file-
based primitive, не vector store — confirms Karpathy/Boris/Jetix file-first
philosophy.

**S13. MemoryAgentBench finding: well-tuned naïve RAG competitive с
specialised memory architectures** ([R-10 §6.4](./R-10-continual-learning.md)). *"Memory system generalisation
is fragile — specialised architectures (A-Mem, Mem0, MemoryOS) are robustly
superior only on reading comprehension; on other domains, well-tuned naïve
RAG is competitive or superior."* Undercuts general-purpose memory vendor
claims. **For Jetix: don't migrate к managed memory based on benchmark
hype.**

**S14. AgentPoison ≥80% attack success at <0.1% corpus contamination** ([R-10
§5.2 ref 38](./R-10-continual-learning.md)). Single poisoned instance с single-token trigger achieves ≥60%
ASR. Memory poisoning is **structurally hard к defend** против. AWS Bedrock
case (Palo Alto Unit 42, Oct 2025): malicious indirect prompt injection
persisted **up to 365 days**. Voice-notes from external meetings + client
documents are direct attack vector for Jetix.

**S15. Anthropic has NO standalone eval product** ([R-11 §2.1, §9](./R-11-evals.md)). Most
shocking finding для CE-curious teams. Console UI-only, no API, no CI/CD,
no trajectory support. Anthropic explicitly recommends Braintrust/LangSmith/
Langfuse/Phoenix — third-party tools — в own Jan 2026 engineering blog.
The "build your own evals" doctrine is forced, не chosen.

**S16. 49% of major benchmarks saturated; cost is NOT a reliable proxy
для accuracy** ([R-11 §3, §7](./R-11-evals.md)). HumanEval, MMLU, SWE-bench Verified — all
>90% SOTA, zero discriminative power. SWE-bench mini comparison: HAL Agent +
Haiku 4.5 = 44% at $65.31; HAL Agent + o3 Medium = 0% at $585.71. **Cheap
small model beats expensive frontier on agentic tasks.**

**S17. pass^k drop reveals reliability crisis** ([R-11 §6 Sierra τ-bench](./R-11-evals.md)).
GPT-4o on τ-retail: ~60% pass^1 → ~25% pass^8. *"60% reliability drop across
8 trials."* Single-trial accuracy dramatically overstates production reliability.
Most agent benchmarks still report only pass^1.

**S18. Llama 4 Arena gaming + 30-position production drop** ([R-11 §7](./R-11-evals.md)). Meta
uploaded 27 Llama 3 variants, deleted underperformers, inflating Chatbot
Arena score by ~100 ELO. Production version dropped from #2 к #32. Yann
LeCun confirmed *"fudged a little bit."* **Public benchmarks are gameable
even by frontier labs.**

### 2.4 Confirmed best practices (production-validated)

**BP1. Plan → Work → Review → Compound loop** — Every (50+ agents, 42+ skills
plugin, 6.8k stars, MIT), Boris Cherny (@claude on PRs), Amit Aile post-mortem
([R-1 §2](./R-1-compounding-engineering-core.md), [R-6 §3](./R-6-every-cora-compound.md), [R-7 §4.4](./R-7-boris-cherny-claude-code.md)).

**BP2. Three-level progressive disclosure для skills** — ~100 tok/skill
metadata, <5,000 tok body, unlimited files on-demand ([R-8 §1.3](./R-8-skills-claudemd-knowledge.md), Anthropic
canonical).

**BP3. Git worktrees для parallel isolated work** — Boris's 5-parallel-Claudes
pattern; Cursor Background Agents; Cognition Devin (parallel instances on
separate tasks, не collaborating subagents on one task) ([R-1 §6.3](./R-1-compounding-engineering-core.md), [R-5 §2](./R-5-production-case-studies.md), [R-7 §3.2](./R-7-boris-cherny-claude-code.md)).

**BP4. Artifact pattern — filesystem writes instead of conversation passing**
([R-2 §4.3](./R-2-swarm-intelligence.md) Anthropic Research; [R-6 §3](./R-6-every-cora-compound.md) Every; Cursor Tab Update blog).
Subagents write artifacts, return lightweight references, не pipe everything
through lead.

**BP5. Hook-based determinism** для anything must-happen-every-time:
formatting, linting, secret scrubbing, schema validation ([R-7 §5.2](./R-7-boris-cherny-claude-code.md), [R-8 §2.4 Builder.io tip #38](./R-8-skills-claudemd-knowledge.md)).

**BP6. Multi-tier model routing** — Haiku для classification/filtering (~20-30%
of cost), Sonnet для generation (60%), Opus для planning/strategic (~10%) ([R-1 §6.1](./R-1-compounding-engineering-core.md), [R-2 §6.4](./R-2-swarm-intelligence.md)).
Jetix's D6 §2.2 agent table already codifies this.

**BP7. Append-only lessons learning** — jonathanmalkin `/wrap-up` Phase 3
pattern; Boris's lessons.md; Stanford ACE +10.6% ([R-3 §7.2, §6.1.6](./R-3-self-improving-systems.md)).
Avoid periodic summarization.

**BP8. 3-4 agent team size sweet spot** — Kim et al. Rule of 4; 45% capability
ceiling threshold ([R-2 §3.5](./R-2-swarm-intelligence.md)). Beyond 4 agents, coordination overhead
exceeds marginal value unless verification architecture present.

**BP9. Verification as quality multiplier** — Boris Cherny documented 2-3×
final output quality from verification loops ([R-1 §5.4](./R-1-compounding-engineering-core.md), [R-7 §6.1](./R-7-boris-cherny-claude-code.md)).

**BP10. Subscription > API для solo operator — 25-50× cost arbitrage** ([R-2 §6.3](./R-2-swarm-intelligence.md)).
Claude Code Max 20× ($200/mo) для Ruslan's workload; API overflow для batch/CI.

**BP11. Four-layer agent termination stack** ([R-9 §5 Q8 + Recommendations](./R-9-agentic-loop.md)):
maxTurns hard cap + Task Budget soft limit + machine-verifiable completion
predicate + HITL escalation для irreversible actions. Boris's "thinnest
wrapper" + Replit's Manager/Editor/Verifier both adhere.

**BP12. Per-department / per-agent loop variant assignment** ([R-9 Recommendations
table](./R-9-agentic-loop.md)). ReAct + CodeAct для technical (system-admin); Orchestrator-Worker +
Plan-and-Execute для research (knowledge-synth); Self-Refine 3-4 iterations
для creative (crazy-agent); ReAct + Reflexion для outcome-signal-rich CRM
(sales-lead/sales-outreach). One pattern не fits all.

**BP13. Extended thinking on long-horizon agents** ([R-9 §6 Q12 ref 103](./R-9-agentic-loop.md)).
Goal Drift paper: Sonnet-4.5 standard fails at 32 steps; thinking variants
pass. Apply к strategist + knowledge-synth + meta-agent FPF-Steward sub-role
where >32-step horizons occur.

**BP14. File-based git-backed memory primary; vector/graph supplementary**
([R-10 §7.2 Jetix endorsement, §8.2 Letta Context Repositories, R-7 §4
CLAUDE.md, Karpathy LLM Wiki](./R-10-continual-learning.md)). Wiki/+strategies.md+scratchpad.md+mailboxes
patterns are 2025-2026 production canonical, **не technical debt**.

**BP15. Sleep-time compute pattern для batch-able context** ([R-10 §2.9 ref 19](./R-10-continual-learning.md)).
~5× compute reduction at equal accuracy when 10 queries share one context;
+18% Stateful AIME, +13% GSM-Symbolic P2. Apply к knowledge-synth daily
context preparation.

**BP16. Anthropic memory tool ZDR-eligible** ([R-10 §4.5](./R-10-continual-learning.md)). File-based,
client-side, 6 commands; 39% agentic search improvement, 84% token reduction
в 100-turn web search. Critical for GDPR-compliant Berlin consultancy.

**BP17. Promptfoo + Langfuse minimum viable eval stack** ([R-11 §8.1](./R-11-evals.md)).
First-class trajectory assertions + Anthropic-endorsed self-hosted observability
+ EU residency + $50-209/mo Phase 1 budget. Critical replacement для
v1 §3.4 G4 empty `evals/<role>/` gap.

**BP18. Hamel Husain Critique Shadowing 6-step workflow** ([R-11 §4](./R-11-evals.md)). Domain
expert → ~30 examples ("15 minutes") → binary pass/fail+critique → fix obvious
errors → build judge iteratively (target precision/recall >0.90, ~3 iterations)
→ periodic error analysis. **Honeycomb case: 30% accuracy improvement after
3 calibration iterations.**

**BP19. Three-agent harness pattern (Planner→Generator→Evaluator)** ([R-11
§9](./R-11-evals.md), Anthropic harness blog Mar 2026). *"Separating the agent doing the work
from the agent judging it proves to be a strong lever... Out of the box,
Claude is a poor QA agent."* Direct application к D6 3-pass writing.

**BP20. pass^k consistency metric for high-stakes agents** ([R-11 §6 Sierra
τ-bench](./R-11-evals.md)). pass^1 dramatically overstates reliability; require pass^3 или
pass^5 для production agent decisions с client-facing impact.

### 2.5 Anti-patterns (production-failure-validated)

**AP1. Pure autonomous agents (AutoGPT/BabyAGI pattern)** — failed at scale
every time ([R-3 §3.3 Point 5](./R-3-self-improving-systems.md)). Devin at 15% success rate ([R-4 §1.1](./R-4-failure-modes-critique.md)).
Human review at weekly+ cadence is hard requirement.

**AP2. Parallel code-writing subagents для tightly-coupled code** — Flappy Bird
failure ([R-2 §4.2](./R-2-swarm-intelligence.md), [R-4 §2.2](./R-4-failure-modes-critique.md)). Subagent 1 builds Super Mario
pipes, subagent 2 builds non-game-asset bird, orchestrator must combine
two miscommunications. Does NOT apply to parallel *review* of single
artifact.

**AP3. CLAUDE.md as wiki/accumulator** — reactive rule addition ([R-8 §6.2](./R-8-skills-claudemd-knowledge.md)).
Termdock trajectory: 30 → 300 lines → Claude ignores MORE rules. Root cause
(context rot) worsened by attempted fix.

**AP4. Periodic summarization of accumulated rules** — Folkman 66.7→57.1%
([R-3 §6.1.6](./R-3-self-improving-systems.md)).

**AP5. Multi-agent debate с homogeneous RLHF'd reviewers** — DCR 86.36%;
sycophancy correlation r=0.902 ([R-4 §2.3](./R-4-failure-modes-critique.md)).

**AP6. 20+ MCP servers** — documented issue #3036, entire context consumed
в 5 prompts ([R-8 §6.4](./R-8-skills-claudemd-knowledge.md)).

**AP7. Marketing "swarm" language for sequential pipeline** — Sweep, Wispr,
Copilot Workspace all overstated; community treats с skepticism ([R-5 §8](./R-5-production-case-studies.md)).
For Jetix: don't call 11-agent system "swarm" in client-facing materials.

**AP8. Agents executing against Lethal Trifecta** (private data + untrusted
input + external communication) без human approval gate ([R-4 §3.1](./R-4-failure-modes-critique.md)).
Jetix's CP-5 (D6 §4.5) correctly enforces this.

**AP9. Skill description overflow** — Compound Engineering plugin 316% budget
exceeded silently ([R-8 §6.5](./R-8-skills-claudemd-knowledge.md)). Monitor `<available_skills>` budget.

**AP10. "Use advanced models, like o1 or o3-mini, to automatically generate
instructions"** в production without verification — reward hacking 100% on
verifiable tasks, sandbagging without prompt ([R-3 §6.1.2-6.1.3](./R-3-self-improving-systems.md)).

**AP11. Tool-call storms** ([R-9 §5 Q10 ref 84](./R-9-agentic-loop.md)). Anthropic's own early system
spawned 50 subagents для simple queries; n8n case: identical vector-search
tool called 10 times; **enterprise cost overruns averaging 340% above
estimate** from infinite retry loops без backoff. Fix: "Single Execution Rule"
injected в system prompt + per-agent gateway rate limits + step caps.

**AP12. Hallucinated tool arguments / phantom tool calls** ([R-9 §5 Q10
ref 84](./R-9-agentic-loop.md)). **Paradox**: better reasoning *increases* hallucination — o3 и o4-mini
push к 33% и 48% rates on certain benchmarks. Five categories: non-existent
function invocation, semantically inappropriate selection, invalid parameters,
missing required arguments, tool bypass (model simulates tool internally).

**AP13. Premature completion (Ralph Wiggum problem)** ([R-9 §5 Q10 ref 84](./R-9-agentic-loop.md)).
Agents declare 100% done at 80% complete because that *looks* like reasonable
stopping point. *"No prompt can enable the agent to validate its own fuzzy
work. This issue is rooted in the architecture of the system rather than
the language used."* Fix = external machine-verifiable predicates, not prompt
engineering.

**AP14. Doom loops / infinite self-reflection** ([R-9 §5 Q10 ref 14, 84, 103](./R-9-agentic-loop.md)).
Reflexion: *"after only four trials...does not show signs of improvement."*
Goal Drift: *"Goal drift shows up most в tasks above 300 lines."* Fix:
Magentic-One stall detection pattern (counts "stuck" iterations; on threshold
breach, breaks inner loop + triggers reflection в outer loop).

**AP15. Devin rabbit holes** ([R-9 §5 Q10 ref 84, 116](./R-9-agentic-loop.md), Devin Answer.AI post-mortem
Jan 2025): asked к deploy multi-app to single Railway deployment (unsupported).
*"Devin spent over a day attempting various approaches and hallucinating
features that didn't exist. The most frustrating aspect wasn't the failures
themselves... but rather how much time we spent trying к salvage these attempts."*

**AP16. Memory poisoning attack vector** ([R-10 §5.2 ref 38, 40, 44](./R-10-continual-learning.md)).
AgentPoison ≥80% ASR at <0.1% corpus contamination; AWS Bedrock case (Palo
Alto Unit 42, Oct 2025) — indirect prompt injection persisted up to 365 days.
Anti-pattern: unsanitised external content в retrieval path; write-back from
retrieved content. Fix: input sanitisation, read-only retrieval paths, audit
logs, differential trust levels (F-G-R aligns).

**AP17. False memory consolidation / semantic drift** ([R-10 §5.2 ref 44](./R-10-continual-learning.md)).
Iterative lossy summarisation introduces fabrication. Fix: confidence
scoring on extracted facts, verification passes, HITL для high-sensitivity
writes, source checksums.

**AP18. Context rot at every length increment** ([R-10 §5.2 ref 42 Chroma
2025](./R-10-continual-learning.md)). 30%+ accuracy drops для middle-positioned content; identified as
*primary* failure mode для coding agents. Anthropic's multi-agent research
system outperformed single long-context agent by 90.2% via short-context
subagents.

**AP19. 1-5 Likert scales для LLM judges** ([R-11 §4 Hamel](./R-11-evals.md)). *"If your
evaluations consist of metrics that LLMs score on a 1-5 scale, you're doing
it wrong."* Forces middle-of-distribution noise. Use binary pass/fail.

**AP20. God Evaluator (single judge prompt assessing 5-10 dimensions)** ([R-11
§4](./R-11-evals.md)). Degrades due to anchoring effects (Stureborg et al.). Fix: one criterion
per judge call (Eugene Yan).

**AP21. Self-evaluation by generator agent** ([R-11 §9](./R-11-evals.md)). Anthropic: *"Out of
the box, Claude is a poor QA agent."* Always use separate evaluator agent.

**AP22. Pairwise comparison without position swap** ([R-11 §4](./R-11-evals.md)). 75% first-
position preference в Claude-v1; 65% GPT-4 default. **NEVER deploy pairwise
без running both orderings.**

**AP23. Public benchmarks для frontier model selection** ([R-11 §3](./R-11-evals.md)). 49%
saturated; GPT-4o drops 14.6pp from MMLU к MMLU-CF; SWE-bench Live vs
Verified shows 24-pt contamination inflation. Build internal golden sets.

**AP24. Velocity vanity metrics для compound learning eval** ([R-11 §8.4](./R-11-evals.md)).
Tasks/week, skill count, self-reported satisfaction = gameable. Only frozen
golden-set scores are primary compound-learning signal.

**AP25. Anthropic Console as production eval infra** ([R-11 §2.1, §9](./R-11-evals.md)).
*"Creates false confidence through its existence — teams think they have
evals because they've used the Console UI. Does not scale past 50–100 manual
tests."*

---

## Part 3 — Comparison: CE/Swarm/Compound × Jetix Current Architecture

### 3.1 Jetix current state (snapshot for comparison)

**Foundation.** Jetix is AI-native consultancy, solo operator (Ruslan,
Berlin) + 11 Claude agents across 6 departments (note: project CLAUDE.md
currently lists 12 agents including `life-coach`; per D6 Area 7 decision
`life-coach` migrates к `life-os/agents/` and is NOT part of Jetix namespace —
canonical Jetix roster = 11), targeting DACH Mittelstand
AI-audit services (€10M-500M revenue clients). Phase 1 run-rate €300-800/mo,
break-even at 1 Audit SKU (€2,000-5,000 covers 5-15 months) (D9 §5.6).

**Constitutional backbone.** **JETIX-FPF v2 (3,758 lines)** adapts Anatoly
Levenchuk's First Principles Framework (github.com/ailev/FPF, ~62k lines)
for AI-native DACH consulting context (D6 §0). 14 sections, 8 core
principles (IP-1…IP-8), 5 client principles (CP-1…CP-5), 8 true alphas,
ontological grounding via 33 U-Types, A.14 typed mereology, A.17-21 Characteristic
Spaces, E.17 Multi-View Publication, B.3 F-G-R trust tagging (D6 §0.5-0.9).

**Architectural pillars** (D9 §3, 8 principles):
- P1: Company-as-Code (Git = SoT)
- P2: Role ≠ Executor (+ Agency-CHR)
- P3: 8 True Alphas + past-participle + A.14 typed mereology
- P4: Nested Holonic Structure (A.1 + A.14)
- P5: L0 Executive Core (5 Ruslan atomic sub-roles)
- P6: DACH primary + US + RU secondary unified funnel
- P7: Resource Accounting (Capital + Compute + Deep Hours + Attention + Ecosystem)
- P8: Portfolio of Directions (8th alpha)

**11 agents hub-and-spoke** (D6 §2.2):
1. manager (Sonnet 4.6, J-Approve)
2. personal-assistant (Haiku 4.5, J-Auto)
3. system-admin (Haiku 4.5, J-Auto)
4. sales-lead (Sonnet 4.6, J-Approve)
5. sales-research (Haiku 4.5, J-Auto)
6. sales-outreach (Haiku 4.5, J-Auto)
7. inbox-processor (Haiku 4.5, J-Auto)
8. crazy-agent (Sonnet 4.6, J-Approve special mode)
9. knowledge-synth (Sonnet 4.6, J-Approve)
10. strategy-support-analyst (Opus 4.6, J-Approve — NOT J-Strategic per Levenchuk)
11. meta-agent + FPF-Steward sub-role (Sonnet 4.6, J-Approve)

**Coordination principles** (D6 §2.2a):
- Hub-and-spoke: subagents report к Department Lead, не Manager
- Manager attention budget: max 20 active tasks
- Message schema: task / result / question / escalation / notification / handoff
- Escalation taxonomy: dept-internal / cross-dept / strategic / safety
- Async default, sync only at named synchronous points
- Stale-dependency timeout 48h business hours

**Knowledge architecture** (D9 §5.2-5.4; wiki/ 9 entity types):
- wiki/: concepts/, entities/, sources/, topics/, ideas/, experiments/, claims/, summaries/, foundations/
- wiki/index.md + log.md (append-only)
- 9 typed edges в wiki/graph/edges.jsonl
- Per-agent 5 layers: system.md (Core) + strategies.md (SPL) + scratchpad.md (working) + niche/ symlinks + mailbox .jsonl
- Custom skills: `/ingest` (raw → wiki), `/ask` (search + synth), `/lint`, `/consolidate`, `/build-graph`

**Operational discipline**:
- 4 rituals: weekly close / monthly P&L + OKR / quarterly strategy + letter / trigger-driven strategizing event
- 4 pre-commit hooks: asymmetric ref / Rechnungsnummer monotonicity / role-manifest required fields / past-participle state check
- Multi-View Publication mandatory для Audit SKU (5 viewpoints: Executive/Technical/Governance/Regulatory/Internal-learning)
- F-G-R trust tagging обязательно в ADR + client deliverables + agent outputs
- CP-5 Human Approval Gate (EU AI Act Art. 14 compliance)

### 3.2 Detailed comparison matrix

| # | Dimension | CE practice | Swarm (Boris/Claude Code) | Compound (Every) | Jetix current | Gap or Opportunity | Recommendation |
|---|-----------|-------------|---------------------------|------------------|---------------|-------------------|----------------|
| 1 | **Agent identity model** | Replaceable via CLAUDE.md + subagents | Stateless invocations ([R-7 §3.2](./R-7-boris-cherny-claude-code.md)) | 50+ named specialized agents (security-reviewer etc) | 11 named agents + FPF Role ≠ Executor ([D6 §5.1](./../../design/JETIX-FPF.md)) | Jetix already has architectural replaceability; naming specific agents matches Every | **Keep**: Jetix's 11-agent named roster с Role ≠ Executor matches Every's pattern но с stronger ontological grounding |
| 2 | **Knowledge storage** | SKILL.md + CLAUDE.md hierarchy | Native Skills (Oct 2025) | AGENTS.md + plugin skills | Custom wiki/ 9 types + per-agent strategies.md | Native Skills cover 70-80% procedural knowledge ([R-8 §7](./R-8-skills-claudemd-knowledge.md)) | **Migrate**: /ingest /ask /lint → native Skills; keep wiki/ as custom MCP-exposed |
| 3 | **Multi-agent review** | 12-reviewer fan-out (Every) | Boris's "5 false-positive subagents" pattern | 12+ named reviewers via `/ce-code-review` | Multi-View Publication 5 viewpoints per Audit SKU (D6 §4.4) | Jetix has multi-view, но не agent-parallel pattern | **Adopt**: 12-reviewer fan-out для Audit SKU deliveries, customized to DACH/EU |
| 4 | **Self-improvement mechanism** | Error→rule→skill pipeline | CLAUDE.md auto-updates via @claude PR tag | `/ce-compound` automated rule extraction | Quarterly FPF-Steward audit (manual) + per-agent strategies.md (append) | Manual quarterly + manual strategies append = good floor но no automation | **Adopt**: jonathanmalkin `/wrap-up` 4-phase pattern as weekly close enhancement |
| 5 | **Memory accumulation** | Per-task compaction + persistent CLAUDE.md | Auto-memory (v2.1.59+) — 200 lines/25KB cap | AGENTS.md + learnings.md per product | Per-agent strategies.md + scratchpad.md + shared wiki | Jetix has persistence; not automated session-close | **Adopt**: session-close lessons-learned → strategies.md append-only |
| 6 | **Coordination pattern** | Orchestrator-worker hybrid | Mama Claude + baby Claudes (flat 1-level) | Plugin slash commands coordinate fan-out | Hub-and-spoke: Manager → dept leads → specialists (2 levels) | Jetix 2-level past Rule of 4 but уже closer к Anthropic Research | **Keep + optimize**: preserve 2-level; reduce dept leads to 3 mandatory orchestrators (Sales+Brain+Meta) |
| 7 | **Pattern reuse** | FPF patterns (Jetix) | Native Skills progressive disclosure | Plugin Skills registry | `wiki/foundations/` + per-agent strategies.md | Reuse pattern correct but not skill-compatible | **Adopt**: Skills for procedural patterns; keep foundations/ for ontological |
| 8 | **Failure recovery** | Subagent retry + manual | Resumable sub-agents via agent_id | Human reviews 12-report synthesis | Human approval gate (CP-5) + escalation taxonomy | Jetix has approval gate; auto-retry not specified | **Add**: explicit retry semantics for stale-dependency (48h business hours) via hooks |
| 9 | **Tooling stack** | Claude Agent SDK + plugins | Claude Code + skills + hooks | Claude Code + compound plugin | Claude Code + custom scripts | Anthropic native stack available; Jetix partially custom | **Migrate**: adopt Claude Agent SDK patterns; reduce custom scripts |
| 10 | **Cost model** | Per-task billing | Subscription (Max 20× $200/mo) | Claude Code Max + API overflow | D9 §5.6 €300-800/mo Phase 1, API-direct | Subscription arbitrage 25-50× ([R-2 §6.3](./R-2-swarm-intelligence.md)) | **Switch**: Max 20× ($200/mo) + API overflow; aligns с current budget |
| 11 | **Onboarding new agent** | 5-block role.md (Jetix) | .claude/agents/<name>.md + memory | Plugin registration | D3 18 role-manifests, 5-block structure | Jetix strictly better than both CE/Claude patterns | **Keep**: Jetix's 5-block role.md + executor-binding.yaml is superior |
| 12 | **Cross-agent learning** | wiki/foundations/ (Jetix) | Shared CLAUDE.md + skills | `/ce-compound-refresh` automated | wiki/ graph + 9 edges | Jetix genuinely additive over CE ([R-8 §7.3](./R-8-skills-claudemd-knowledge.md)) | **Keep**: wiki/ graph is genuine additive layer; expose via MCP |
| 13 | **Decision audit trail** | Git commits | @claude PR tag + CLAUDE.md diff | GitHub issues | ADR + commit = decision ([D9 §3 P1](./../../decisions/2026-04-20-jetix-architecture-final-DRAFT.md)) | Jetix strictly better (ADR + CP-5 gate + F-G-R tagging) | **Keep**: Jetix pattern exceeds CE discipline |
| 14 | **Test/validation discipline** | Hamel Husain 3-level evals | Stop hooks for test execution | 12-reviewer fan-out + CI | evals/<role>/ golden datasets (D9 §5.1 folder 8) | Jetix has structure, minimal content Day 1 | **Populate**: 20-50 golden tasks per role by Day 10 (Hamel-Husain pattern) |
| 15 | **Deployment unit** | Skill/plugin | Plugin | Plugin distributed via npm | Git commit → hook → live | Jetix lighter; CE heavier but portable | **Hybrid**: package Jetix stack as private plugin для Phase 2a+ |
| 16 | **Verification loop** | Test suite + linter | Stop hooks + sub-agent review | 12-parallel reviewer fan-out | Pre-commit hooks + Multi-View Publication | Jetix lighter; 12-fan-out more thorough | **Enhance**: add review subagents к `/close-day` for Audit SKU |
| 17 | **Agent specialization** | Single model + tools | Sub-agents by task (flat) | 50+ named specialized agents | 11 functionally-specialized (sales/brain/ops/meta) | Jetix intermediate granularity | **Keep + adopt review subagents** for delivery phase |
| 18 | **Compliance/audit** | Not addressed | PreToolUse/PostToolUse hooks | Manual | EU AI Act Art. 14 + GDPR + DACH legal (D6 §4.5.1) | Jetix strictly better due to DACH regulatory requirement | **Keep**: Jetix's regulatory alignment is moat |
| 19 | **Strategic decision-making** | Human | Human (Boris's setup) | Human (Dan Shipper) | Ruslan strategy-lead atomic sub-role + FPF-Steward audit | All agree: human strategic; differ on operational support | **Keep**: Jetix's strategy-support-analyst (Opus) gives better decision support |
| 20 | **Documentation philosophy** | CLAUDE.md + skills | Lean (2.5k tokens own example) | Plugin markdown | D6 3,758 lines constitutional + tier-loading | Jetix heavier but load tier reduces agent cost | **Keep + verify**: tier-loading (D6 §5.4a) mitigates cost |
| 21 | **Agentic loop pattern** | ReAct default; CodeAct via Bash | ReAct + JSON tools + agentic search ([R-9 §4 Q6](./R-9-agentic-loop.md)) | ReAct via Claude Code | ReAct (de-facto, all 11 agents on Claude) | Pattern correct; per-department variant assignment missing | **Adopt**: per-dept variant table per [R-9 Recommendations](./R-9-agentic-loop.md) — Plan-and-Execute для knowledge-synth/strategist; Self-Refine для crazy-agent; Reflexion для sales-lead/sales-outreach |
| 22 | **Memory architecture** | wiki/+strategies.md (Jetix) | CLAUDE.md + auto-memory + sub-agent fresh context | AGENTS.md per product | Wiki/+per-agent strategies+scratchpad+mailboxes+voice-notes ([D9 §5.2](./../../decisions/2026-04-20-jetix-architecture-final-DRAFT.md)) | **R-10 §7.2 explicit endorsement**: this IS the dominant production pattern as of 2025-2026 | **Keep + augment**: adopt Anthropic memory tool (ZDR-eligible, [R-10 §4.5](./R-10-continual-learning.md)) selectively; sqlite-vec Phase 2 when entities >200; Letta sleep-time trial Phase 2 на ONE agent |
| 23 | **Memory hierarchy explicit** | Implicit | Implicit (CLAUDE.md hierarchy) | Implicit | Implicit (4 layers per agent) | R-10 §1.4 cognitive taxonomy: episodic/semantic/procedural/working | **Make explicit**: tag wiki/concepts as semantic, mailboxes as episodic, strategies.md as procedural, scratchpad as working ([R-10 §1.4](./R-10-continual-learning.md)) |
| 24 | **Eval framework** | Per-agent custom (Hamel pattern) | None native (Console UI-only) | 12-reviewer fan-out | None Day 1 (D9 §5.1 folder 8 empty) | **Critical gap** — R-11 confirms Anthropic has no eval product; teams build own | **Adopt Phase 1**: Promptfoo (CLI, trajectory assertions) + Langfuse ($0-29/mo, EU residency) per [R-11 §8.1](./R-11-evals.md); $50-209/mo budget |
| 25 | **LLM-as-judge usage** | Various (Hamel framework) | Built into Skills/`/ce-code-review` | 12-reviewer fan-out as judges | None currently | R-11 §4: 85-87% Zheng baseline; 9 bias categories с magnitudes; 8 calibration techniques | **Adopt**: Hamel's Critique Shadowing 6-step ([R-11 §4](./R-11-evals.md)); binary pass/fail; one criterion per call; PoLL ensemble для high-stakes (3 diverse models, 1/7 GPT-4 cost) |
| 26 | **Continual learning mechanism** | Manual /ce-compound + AGENTS.md append | Auto-memory v2.1.59+ (200 lines/25KB cap) | `/ce-compound-refresh` automated | Manual quarterly FPF-Steward audit + manual strategies.md append | Sleep-time compute pattern: 5× compute reduction, +18% Stateful AIME ([R-10 §2.9](./R-10-continual-learning.md)) | **Adopt selectively**: jonathanmalkin /wrap-up Phase 3 weekly + sleep-time pattern для batch-able context (knowledge-synth daily prep) |
| 27 | **Termination/completion stack** | Implicit (max iters) | Explicit (Stop hooks, maxTurns) | 12-reviewer convergence | Hooks + CP-5 approval gate | R-9 §5 Q8 mandates 4-layer stack (maxTurns + Task Budget + verifiable predicate + HITL) | **Adopt**: 4-layer stack per agent в YAML; encode maxTurns per [R-9 Recommendations table](./R-9-agentic-loop.md) (5-50 range by agent type) |
| 28 | **Sub-agent context model** | Fresh context (Claude Code default) | Fresh context only | Fresh context | Mailbox JSONL (full traces possible) | Walden Yan Principle 1: pass full traces, не summaries ([R-9 §7 Q14](./R-9-agentic-loop.md)) | **Confirm + enforce**: messages в mailboxes/<id>.jsonl include full reasoning trace, not only outcomes |
| 29 | **GDPR/data residency for memory** | Not addressed | Anthropic memory tool ZDR-eligible | Not addressed | DACH/EU compliance via D6 §4.5.1 | R-10 §5.2: Article 17 vs Article 12/72 conflict requires architectural tiering | **Adopt Anthropic memory tool** для ZDR; tiered memory (ephemeral / GDPR-deletable / pseudonymised audit) |
| 30 | **Goal drift mitigation (long-horizon)** | Not addressed | Extended thinking variants | Not addressed | Implicit (FPF-Steward quarterly) | R-9 §6 Q12: Sonnet-4.5 standard fails at 32 steps; thinking variants pass | **Enable extended thinking** on strategist + knowledge-synth + meta-agent FPF-Steward для tasks >32 steps |

### 3.3 Where Jetix is already at frontier

**F1. FPF ontological grounding.** 33 U-Types, A.14 typed mereology, A.17-21
Characteristic Spaces, B.3 F-G-R tagging, E.17 Multi-View Publication
[D6 §0.9, §8, §10, §12](./../../design/JETIX-FPF.md). None of R-1…R-8 shows any comparable
depth. CE plugins operate at WHAT level (skills, agents); Jetix operates
at WHY/WHAT/HOW with explicit ontology. **Moat for regulated DACH
clients — EU AI Act Art. 14 "meaningful human oversight" requires
explainable decision structure.**

**F2. Past-participle state machines + 8 alphas.** D6 §6 8 alphas (Client,
Project, Deal, Content Item, Hypothesis, Member, Way of Working, Direction)
с strict past-participle discipline + Hook 4 enforcement. CE has no
equivalent. Every's plugin has subagents (processes) but no explicit
alpha state machines. Closest analog: Replit Agent's Manager/Editor/Verifier
roles, но stateless.

**F3. Role ≠ Executor с Agency-CHR.** D6 §5.1 + D9 P2. Agency profile
per decision class (J-Auto/Approve/Strategic dimensions). CE plugins
name agents (role is executor). R-2 calls out "replaceable agents" як
aspirational; Jetix achieves architecturally via FPF.

**F4. F-G-R trust tagging mandatory on every ADR + client deliverable + agent
output.** D6 §4.2, §12.7. Formality (F0-F9), claim-Scope (G), Reliability
(R-low/medium/high/certified) surfaced on every artifact. **No equivalent
in CE/Swarm/Compound.** Differentiates Jetix для compliance-heavy clients.

**F5. EU AI Act Risk-Tier self-classification matrix.** D6 §4.5.1.
Minimal-risk / Limited-risk / High-risk / Unacceptable-risk mapping
с documented Phase 1 self-classification и Phase 2 verification. **R-4
explicitly flags Lethal Trifecta unsolved; Jetix's CP-5 + tier matrix
operationalizes human-gate pattern.**

**F6. Memory architecture endorsed verbatim by R-10.** Jetix's wiki/+per-
agent strategies.md + scratchpad.md + mailboxes.jsonl + voice-notes pipeline
**is** the dominant production pattern as of 2025-2026 ([R-10 §7.2 §Exec
Summary](./R-10-continual-learning.md)) — endorsed by Karpathy ("LLM Wiki" April 2026) и Boris Cherny.
File-based git-backed memory wins on transparency + GDPR + portability +
selective forgetting (`git rm` / `git filter-branch` viable; vector embeddings
not). Letta Context Repositories (Feb 2026) confirms reference architecture.
**Не technical debt — deliberate transparency trade-off.**

**F7. Hub-and-spoke matches R-9 recommended Hierarchical Orchestrator-Worker
pattern.** R-9 explicit ([§Recommendations §"Coordination Model"](./R-9-agentic-loop.md)): Manager
routes-not-executes + Department Leads delegate to subagents within department
= correct production pattern. Jetix already aligned. Combined с R-9 per-
department variant assignment, forms canonical multi-agent topology.

**F8. F-G-R trust tagging maps directly к memory differential trust levels.**
R-10 §5.2 anti-pattern fix recommends *"differential trust levels"* для
mitigation of memory poisoning + false consolidation. **Jetix's F-G-R already
operationalizes this** — voice-notes get F0/G-narrow/R-low tagging until
human-promoted. No CE/Swarm/Compound equivalent explicit framework.

### 3.4 Where Jetix has gaps

**G1. No native Skills migration.** Jetix's /ingest /ask /lint are custom
bash/Python scripts that reinvent native Skills (R-8 §6.1 anti-pattern
#1). Loses: hot-reload, cross-tool portability, progressive disclosure,
auto-invocation via description matching. **Cost of migration**: 4-6h
for all three; **saves**: ~2,000 tokens per session + ecosystem compatibility.

**G2. No native Plugin packaging.** Jetix's stack (skills, agents, rules,
wiki) lives in ad-hoc structure. Native plugin manifest (`.claude-plugin/plugin.json`)
would enable: `claude plugin install jetix-core@jetix-plugins` for new
team members. Phase 1 not critical; Phase 2a+ essential.

**G3. No hook inventory for determinism.** Jetix has 4 pre-commit hooks
(git-level) but no PostToolUse hooks для format/lint/secret-scrubbing
per Boris's practice. [R-7 §5.2 Builder.io tip #38](./R-7-boris-cherny-claude-code.md): "*If something must happen
every time, make it a hook.*" Jetix CP-5 Human Approval Gate could use
hooks for deterministic enforcement vs advisory CLAUDE.md prose.

**G4. No eval framework populated.** D9 §5.1 folder 8 `evals/<role>/` is
structurally correct (per Hamel Husain [R-3 §5.2](./R-3-self-improving-systems.md)) but empty Day 1. Needs
20-50 golden tasks per role drawn from real failures. Without this, CE
compound step is blind.

**G5. No lessons.md session-close pattern operationalized.** Per-agent
strategies.md exists as structure (per-agent file verified: "Добавляй новые
стратегии после каждой сложной задачи (сверху)") but no explicit session-close
ritual triggers append. Compare to jonathanmalkin `/wrap-up` Phase 3
([R-3 §7.2](./R-3-self-improving-systems.md)) where Claude identifies patterns like "*You requested X
three times today*" automatically.

**G6. No MCP server for wiki.** Jetix's wiki/ has typed entity graph —
exactly what MCP memory provides natively ([R-8 §4.2 knowledge graph architecture](./R-8-skills-claudemd-knowledge.md)). Not
exposing via MCP means: external agent frameworks (Cursor, Codex) can't
query wiki; cross-machine sync absent; Claude.ai connector absent. **Phase
2a opportunity: thin in-house MCP server exposing wiki_search / wiki_read
/ wiki_write_observation / wiki_list_edges / wiki_propose_entity.**

**G7. No Anthropic Skills open standard adoption.** `/wiki/foundations/`
is Jetix-unique format; not portable к Cursor, Codex CLI, Gemini CLI.
Adopting `SKILL.md` + `agentskills.io` spec gives Jetix cross-tool future-
proofing at no cost.

**G8. No eval framework operational** — restated с R-11 specifics. v1 G4
identified empty `evals/<role>/` folders. R-11 §8.1 provides exact filling
recipe: Promptfoo CLI + Langfuse hosted/self-hosted + 30-example golden sets
per agent + Hamel Critique Shadowing 6-step + GitHub Action PR gate. Cost:
$50-209/mo. **The gap is now fully specified — zero excuse Phase 1 Day 14-17.**

**G9. No agentic loop variant assignment per agent type.** All 11 agents
currently default к ReAct (Claude Code native). R-9 §Recommendations table
prescribes per-department variants (Plan-and-Execute для knowledge-synth/
strategist; Self-Refine для crazy-agent; Reflexion для CRM agents; CodeAct
для system-admin). **Encoding maxTurns + variant в YAML role-manifest =
Phase 1 Day 11-12 task.**

**G10. No machine-verifiable completion predicates per agent.** All current
agents implicitly use "self-declared completion" — directly hits R-9 Ralph
Wiggum problem ([§5 Q8 ref 84](./R-9-agentic-loop.md)). Each agent needs explicit external
verification oracle (test pass / schema validation / linter / acceptance-
authority sign-off / etc.). **Aligns с AC2 (verification_signal field) but
needs concrete oracle definitions.**

**G11. No sleep-time compute pattern для batch-able context preparation.**
R-10 §2.9 Letta sleep-time agents deliver 5× compute reduction at equal
accuracy + 2.5× per-query cost reduction when context shared across 10
queries. **High-ROI Phase 2 opportunity** для knowledge-synth (daily wiki
preparation) + sales-researcher (prospect context preparation).

**G12. No extended thinking on long-horizon agents.** R-9 §6 Q12 ref 103:
Sonnet-4.5 standard fails goal resilience в 32-step experiments. **Strategist
+ knowledge-synth + meta-agent FPF-Steward are exposed**. Extended thinking
adds cost но critical для tasks >32 steps.

**G13. No anti-sycophancy discipline для multi-reviewer fan-out.** R-4 §2.3
DCR 86.36% + R-11 §4 sycophancy 58.19% aggregate. v1 OQ3 flagged this; R-11
gives concrete mitigation: heterogeneous models (Haiku + Sonnet mix breaks
correlation r=0.902) + PoLL ensemble pattern (3 diverse models). **Required
before deploying 12-reviewer fan-out** на client deliverables.

### 3.5 Where existing Jetix concepts map к CE concepts

| Jetix term | CE/Swarm/Compound equivalent | Notes |
|-----------|------------------------------|-------|
| **Holon** (D6 §1.1) | Subagent (Every/Boris) — approximately | Jetix holon is ontological; subagent is operational. Holon is structural; subagent is ephemeral instance |
| **Alpha** (D6 §6) | *No CE equivalent* | Genuine Jetix innovation. State-machine discipline entirely absent от CE literature |
| **FPF-Steward** (D6 §5.4) | Agent-as-Judge + Constitutional AI (Anthropic) | Jetix binds это explicitly to quarterly audit ritual |
| **Creation Graph** (D6 §3) | Shared environment + typed edges | Jetix's A.14 typed mereology goes beyond CE's implicit filesystem semantics |
| **Role ≠ Executor** (D6 §5.1, P2) | "Replaceable agents" (Boris Cherny) | Same principle; Jetix has architectural enforcement via FPF |
| **F-G-R tagging** (D6 §4.2) | *No CE equivalent* | Trust discipline genuinely missing from CE |
| **Multi-View Publication** (D6 §4.4) | Evaluator-optimizer pattern (Anthropic) | Jetix's 5 viewpoints more structured |
| **U.BoundedContext** (D6 §5.2) | AGENTS.md scoping + skill paths frontmatter | FPF's Context-is-king predates CE |
| **Agency-CHR** (D6 §2.1a) | *No CE equivalent* | Jetix innovation grounded in FPF A.13:4.3 |
| **8 true alphas** | Subagent types + state flows | Jetix alphas are first-class typed entities; CE subagents are behavioral profiles |
| **J-level (J-Auto/Approve/Strategic)** | HITL spectrum points 1-5 ([R-3 §3.3](./R-3-self-improving-systems.md)) | Directly maps to named points; Jetix has 3-tier, HITL has 5-point |
| **Past-participle state discipline** | *No CE equivalent* | Ontological innovation from Levenchuk methodology |
| **Bias-Audit Cycle BA-0/1/2/3** (D6 §12.10) | Constitutional Classifiers runtime gate | Jetix's cycle more methodologically structured |
| **Direction (Portfolio of Directions)** | *No CE equivalent* | Jetix innovation (Portfolio-of-Directions P8) |
| **Compound step (CE)** | Session-close + strategies.md append + FPF-Steward quarterly audit | Jetix already implements loosely; operationalize as ritual |
| **wiki/concepts + entities** ([D9 §5.2](./../../decisions/2026-04-20-jetix-architecture-final-DRAFT.md)) | Semantic memory ([R-10 §1.4](./R-10-continual-learning.md)) | Direct map — Jetix is GraphRAG/HippoRAG analog в file-based form |
| **mailboxes/<id>.jsonl** | Episodic memory ([R-10 §1.4](./R-10-continual-learning.md)) | Direct map — timestamped event store; Letta recall storage analog |
| **strategies.md (per-agent)** | Procedural memory + Voyager skill library ([R-10 §1.4 / R-9 §3 Q4](./R-10-continual-learning.md)) | Direct map — System Prompt Learning instantiation per Karpathy |
| **scratchpad.md (per-agent)** | Working memory ([R-10 §3.3](./R-10-continual-learning.md)) | Direct map — finite live context |
| **wiki/graph/edges.jsonl 9 typed edges** | Knowledge graph ([R-10 §2.6 GraphRAG, §4.3 Graphiti](./R-10-continual-learning.md)) | Jetix file-based + semantic typing exceeds MCP memory's 3 primitives |
| **CP-5 Human Approval Gate** | HITL Point 2-3 ([R-3 §3.3](./R-3-self-improving-systems.md)) + 4th termination layer ([R-9 §5 Q8](./R-9-agentic-loop.md)) | Aligned; encoding в hooks would make deterministic |
| **Hub-and-spoke с dept leads** | Hierarchical Orchestrator-Worker ([R-9 §Recommendations](./R-9-agentic-loop.md)) | Direct map; R-9 explicit endorsement |
| **F-G-R trust tagging** | Differential trust levels for memory ([R-10 §5.2](./R-10-continual-learning.md)) | Jetix's framework предшествует CE; aligns с poisoning mitigation |
| **eval/<role>/** (currently empty) | Internal golden sets per Hamel ([R-11 §4, §8.1](./R-11-evals.md)) | Structurally correct; Promptfoo+Langfuse fills it |

---

## Part 4 — Strategic Implications для Jetix

### 4.1 Adopt directly (high-confidence wins)

**A1. Native Skills migration — `/ingest`, `/ask`, `/lint`** ([R-8 §7](./R-8-skills-claudemd-knowledge.md)).
- What: Convert 3 custom commands к `.claude/skills/<name>/SKILL.md`
- Why: Hot-reload, cross-tool portability, progressive disclosure, auto-
  invocation via description
- Leverage: ~2,000 tokens saved/session; ecosystem interop (Cursor/Codex)
- Cost: 4-6h Day 10-11
- Verification: Claude auto-fires `/ask` когда user asks about wiki-covered
  topic без explicit slash command

**A2. PostToolUse hooks для format + lint + secret-scrubbing** ([R-7 §5.2](./R-7-boris-cherny-claude-code.md), [R-8 §2.4](./R-8-skills-claudemd-knowledge.md)).
- What: Add hooks to `.claude/settings.json` firing on `Write|Edit` events
- Why: Deterministic 100% vs advisory CLAUDE.md 80%
- Leverage: Prevents 10% of mistakes Claude makes но misses checking для
- Cost: 2-4h per hook
- Verification: `bun run format || true` runs after every file edit

**A3. jonathanmalkin `/wrap-up` pattern as `/close-day` enhancement**
([R-3 §7.2 Case 3](./R-3-self-improving-systems.md)).
- What: Weekly close ritual runs 4-phase: Ship It (commit+push) →
  Remember It (review session learnings → strategies.md append) →
  Review & Apply (identify patterns like "You requested X three times
  today") → Publish It (optional)
- Why: Automates compound step без human bottleneck; Boris's lessons.md
  equivalent
- Leverage: 2-3× quality gain (Boris Cherny, verification loop)
- Cost: 1h setup + ongoing
- Verification: strategies.md grows ACE-pattern structured entries; `/lint`
  detects contradictory rules quarterly

**A4. 12-reviewer fan-out для Audit SKU delivery** ([R-6 §3](./R-6-every-cora-compound.md)).
- What: Install Every's compound-engineering-plugin; fork к Jetix variants
- Why: Production-validated; exactly the pattern Jetix's Multi-View
  Publication semi-implements
- Leverage: 12 parallel reviewers (security, performance, compliance, etc.)
  catch ~85% issues human solo review misses
- Cost: 1h install + 3-5h customize к DACH/EU context (add jetix-dsgvo-reviewer,
  jetix-ai-act-reviewer, jetix-fpf-alignment-reviewer, jetix-hgb-finance-reviewer)
- Verification: Each Audit SKU delivery generates synthesized review
  report; human adjudicates per F-G-R

**A5. Append-only lessons pattern (ACE) в strategies.md** ([R-3 §6.1.6](./R-3-self-improving-systems.md)).
- What: Structured entries с unique IDs + ✓ Helpful / ✗ Harmful counters,
  not free-form prose
- Why: Avoids Folkman context collapse (66.7→57.1% from summarization);
  ACE pattern +10.6% accuracy
- Leverage: Learnings accumulate without degrading context quality
- Cost: Template update, 30 min
- Verification: FPF-Steward quarterly audit reviews Helpful/Harmful ratios

**A6. Subscription economics — Max 20× + API overflow** ([R-2 §6.3](./R-2-swarm-intelligence.md), [R-5 §6](./R-5-production-case-studies.md)).
- What: Claude Code Max 20× ($200/mo) для Ruslan; API-direct только для
  batch jobs, CI workloads, 3rd-party harnesses
- Why: 25-50× cost arbitrage; Kyle Redelinghuys 93% savings pattern
- Leverage: ~€180/mo savings vs pure API-direct at Jetix's projected usage
- Cost: Zero (plan switch)
- Verification: Monthly compute-ledger comparison API-equivalent vs subscription

**A7. Aider repo-map pattern for external client code-base exploration.**
- What: When ingesting client codebase for Audit SKU, generate AST-driven
  compact index before invoking `/ce-plan`
- Why: CE plan step assumes "look through current codebase history" —
  degrades on first-touch client code
- Leverage: Reduces token cost of exploration; Paul Gauthier proven
  технология
- Cost: 1-2 day integration with existing tools (tree-sitter available
  per Aider approach)
- Verification: Repo-map token count + coverage %

**A8. Thin in-house MCP server for wiki/ (Phase 2a trigger).**
- What: 5-tool MCP server (wiki_search / wiki_read / wiki_write_observation
  / wiki_list_edges / wiki_propose_entity) exposing Jetix wiki
- Why: Enables cross-tool access (Cursor, Codex CLI), Claude.ai connector,
  cross-machine sync (currently missing)
- Leverage: Jetix's 9 entity types + edges become portable asset rather
  than Claude-Code-only
- Cost: 3-5 days Phase 2a
- Verification: Use from Claude.ai desktop app; verify same wiki state

**A9. Promptfoo + Langfuse minimum viable eval stack** ([R-11 §8.1](./R-11-evals.md)) — Phase 1.
- What: Install Promptfoo CLI + Langfuse cloud Hobby (или self-host); per-
  agent `evals/<role>/promptfooconfig.yaml`; 30-50 hand-graded examples per
  agent в `golden-set.jsonl`; GitHub Action `eval.yml` PR gate at ≥85%
- Why: Anthropic has NO eval product; production teams build internal
  benchmarks; **fills v1 G4 + new G8 critical gap**
- Leverage: Quality gates на agent prompts/skills; CI regression detection;
  eval-driven development per Hamel
- Cost: ~$50-209/mo Phase 1; 6h pilot setup на sales-researcher; 4-6h per
  remaining agent (40-60h total over 4-6 weeks)
- Verification: Eval pass rate ≥85% pre-merge; precision/recall >0.85
  на judge; Cohen's κ >0.6 vs Ruslan grading

**A10. Hamel Husain Critique Shadowing 6-step workflow** ([R-11 §4](./R-11-evals.md)).
- What: Domain expert (Ruslan) → 30-example dataset ("15 minutes") → binary
  pass/fail+critique → fix obvious errors → build LLM judge iteratively
  (target precision/recall >0.90, ~3 iterations) → periodic error analysis
- Why: Production-validated method (Honeycomb 30% accuracy improvement after
  3 iterations); avoids 1-5 Likert anti-pattern
- Leverage: Foundation для all per-agent evals (A9) + D-document eval (A11)
- Cost: 30 min process documentation + 15 min per agent dataset creation
- Verification: Precision/recall metrics on judge; quarterly re-calibration

**A11. Three-agent harness pattern (Planner → Generator → Evaluator) для
D6/D8 writing** ([R-11 §9 Anthropic harness blog Mar 2026](./R-11-evals.md)).
- What: Adopt explicit Planner/Generator/Evaluator separation для high-stakes
  D-documents (D1, D5, D6, D8); Evaluator agent tuned skeptical (anti-
  sycophancy)
- Why: *"Out of the box, Claude is a poor QA agent"* (Anthropic verbatim);
  separating work from judgment is "strong lever"
- Leverage: Quality on D-documents + future client-facing Audit SKU deliverables
- Cost: 2-3h prompt engineering; integrates с existing meta-agent verifier
  role (AC3)
- Verification: D-document quality scores improve quarter-over-quarter

**A12. Anthropic memory tool (file-based, ZDR-eligible)** ([R-10 §4.5](./R-10-continual-learning.md)) — Phase 1.
- What: Adopt Anthropic memory tool beta (`context-management-2025-06-27`)
  selectively for client-data-touching agents (sales-research, sales-outreach,
  inbox-processor); 6 commands (view/create/str_replace/insert/delete/rename);
  client-side storage
- Why: 39% agentic search improvement; 84% token reduction в 100-turn web
  search; **ZDR-eligible — only fully GDPR-compliant option** for Berlin
  consultancy
- Leverage: GDPR Article 17 erasure compliance + Article 20 portability
- Cost: 2-4h integration per agent; ~2,500 tokens system prompt overhead
- Verification: Verify ZDR config active; verify file-based storage; verify
  Article 17 deletion works end-to-end

**A13. ACE append-only pattern formalization (extends A5)** — combine Stanford
ACE +10.6% accuracy ([R-3 §6.1.6](./R-3-self-improving-systems.md)) с Anthropic Agent Skills standard SKILL.md
([R-10 §8.1 ref 30](./R-10-continual-learning.md)).
- What: Migrate per-agent `strategies.md` к SKILL.md format с YAML frontmatter
  + progressive disclosure + ACE structured entries (unique IDs + Helpful/
  Harmful counters)
- Why: Combines best-of-breed compound learning (+10.6% ACE) с industry-
  standard portability (Apache 2.0 Dec 2025 standard) + Karpathy SPL alignment
- Leverage: Cross-tool portability (Cursor/Codex/Gemini CLI parse SKILL.md)
- Cost: 2h template design + 30 min per agent migration
- Verification: SKILL.md frontmatter validates; FPF-Steward quarterly Helpful/
  Harmful ratios

**A14. Per-agent four-layer termination stack** ([R-9 §5 Q8 + Recommendations](./R-9-agentic-loop.md)).
- What: Encode в YAML role-manifest для each of 11 agents:
  (a) `maxTurns:` hard cap (5-50 range per [R-9 Recommendations table](./R-9-agentic-loop.md))
  (b) `taskBudget:` soft limit using `task-budgets-2026-03-13` header
  (c) `completionPredicate:` machine-verifiable oracle (test pass / schema
      / linter / acceptance signal)
  (d) `escalationTrigger:` HITL gate для irreversible actions
- Why: Solves Ralph Wiggum problem ([R-9 §5 Q8 ref 84](./R-9-agentic-loop.md)) — premature completion
  is architectural, not promptable
- Leverage: Prevents 4 of 6 R-9 anti-patterns (tool storms, doom loops,
  premature completion, rabbit holes)
- Cost: 2h schema design + 30 min per agent
- Verification: Hooks enforce maxTurns; FPF-Steward reviews escalation log
  monthly

**A15. Per-department agentic loop variant assignment** ([R-9 Recommendations
table](./R-9-agentic-loop.md)).
- What: Encode loop variant в role-manifest + system.md per department:
  - system-admin / sales-outreach (technical) → ReAct + CodeAct
  - knowledge-synth / sales-researcher → Orchestrator-Worker + Plan-and-Execute
  - crazy-agent → Self-Refine 3-4 iterations
  - sales-lead / sales-outreach (CRM) → ReAct + Reflexion на outcome signals
  - personal-assistant → Plan-and-Execute + HITL interrupts
  - meta-agent → Self-Refine + ReAct evaluator-optimizer
  - strategy-support-analyst → Plan-and-Execute + extended thinking
- Why: One pattern не fits all; R-9 explicit per-dept recommendations
- Leverage: Better cost/quality matching; reduces token waste
- Cost: 1-2h per agent prompt engineering
- Verification: Token-per-task metric per agent; quarterly review

**A16. Extended thinking on long-horizon agents** ([R-9 §6 Q12 ref 103](./R-9-agentic-loop.md)).
- What: Enable extended thinking on strategy-support-analyst, knowledge-
  synth, и meta-agent FPF-Steward sub-role для tasks >32 steps
- Why: Goal Drift paper: Sonnet-4.5 standard *"consistently fail to recognize
  the new goal"*; only thinking variants resilient
- Leverage: Long-horizon task reliability for D-document writing + FPF audit
- Cost: ~30-40% extra token cost per task; budget impact monitored
- Verification: Goal-resilience test (32-step adversarial scenario quarterly)

### 4.2 Adapt (modify before adopting)

**AD1. CE's Plan → Work → Review → Compound loop — adapted для Jetix
4 rituals cadence.**
- CE version: per-feature cycle within engineering task
- Jetix adaptation: map k existing 4 rituals (weekly close = Review; monthly
  P&L + OKR = Compound; quarterly strategy = Plan; trigger-driven = emergency
  Plan)
- Why modify: Jetix rituals are operational-management-level, not engineering-
  task-level; CE's 80/20 plan+review / work+compound doesn't map 1:1
- Verification: Each ritual produces artifact per IP-3 (D6 §5.3)

**AD2. Compound Engineering plugin fork — Jetix DACH variants.**
- CE version: Rails-focused reviewers (`ce-kieran-rails-reviewer`,
  `ce-kieran-python-reviewer`, `ce-kieran-typescript-reviewer`)
- Jetix adaptation: Replace with DACH/EU compliance reviewers:
  - `jetix-dsgvo-reviewer` (GDPR Art. 32 TOMs compliance)
  - `jetix-ai-act-reviewer` (EU AI Act Art. 14 "meaningful human oversight")
  - `jetix-hgb-finance-reviewer` (HGB §§238-263 accounting discipline)
  - `jetix-ustg-invoice-reviewer` (§14 UStG 11 Pflichtangaben)
  - `jetix-multiview-reviewer` (D6 §4.4 all 5 viewpoints present)
  - `jetix-fpf-alignment-reviewer` (D6 ontology compliance)
  - `jetix-fgr-tagging-reviewer` (F-G-R tags present on all claims)
  - `jetix-boundary-discipline-reviewer` (L/A/D/E routing per D6 §4.3)
- Why modify: Jetix's deliverable — DACH-legal-compliant AI audits — not generic
  Rails apps. Generic reviewers miss Jetix-specific risks.

**AD3. Skills system с disable-model-invocation для destructive operations.**
- CE version: Most skills invokable automatically when description matches
- Jetix adaptation: `/ingest` (writes к wiki) + any skill that mutates
  alpha state → `disable-model-invocation: true` (user must explicitly invoke)
- Why modify: Levenchuk + Willison Lethal Trifecta ([R-4 §3.1](./R-4-failure-modes-critique.md)) —
  destructive autonomous writes без human approval gate violate CP-5

**AD4. Cognition's fine-tuned compression model pattern → Jetix's tiered
FPF loading.**
- Cognition version: Dedicated compression model для long-horizon tasks
- Jetix adaptation: D6 §5.4a 3-tier loading (full-text / distilled-essence
  / reference-only с on-demand fetch) is structurally similar adaptation
- Why modify: Jetix уже has this; make tier-loading compression explicit
- Verification: Compute-ledger shows per-agent token cost reduction ~60%
  per D6 §5.4a projection

**AD5. Voyager skill library pattern — bounded к Jetix's evals + verifiable
domain.**
- Voyager version: Minecraft closed environment с executable JavaScript
  skill library generated autonomously
- Jetix adaptation: Skills generated only for tasks with verifiable ground
  truth — test pass/fail, schema validation, linter output, client
  acceptance signal
- Why modify: METR reward-hack 100% on unverifiable tasks ([R-3 §6.1.3](./R-3-self-improving-systems.md))
- Verification: Skill creation requires eval pair (task + verification oracle)

**AD6. Reflexion pattern adapted к FPF-Steward audit cycle** ([R-9 §3 Q4
Reflexion + Critical Assessment](./R-9-agentic-loop.md)).
- Reflexion version: Trial → Evaluate → Verbal Self-Reflection → Retry
  с three-model setup (Actor / Evaluator / Self-Reflection); fails after
  4 trials
- Jetix adaptation: Quarterly FPF-Steward audit treats prior quarter's
  ADRs/D-documents as "trials"; meta-agent acts as Evaluator; Ruslan
  strategy-lead acts as Self-Reflection (human-in-loop); writes structured
  reflections к `decisions/fpf-stewardship/<quarter>-reflection.md`
- Why modify: Pure Reflexion fails on creative/novel tasks; human-in-loop
  Self-Reflection avoids local minima trap (R-9 Critical Assessment Reflexion)
- Verification: Quarterly audit produces actionable rule additions к
  strategies.md per agent

**AD7. Eval-driven development for D1-D8 quality gates** ([R-11 §8.3 + §9
three-agent harness](./R-11-evals.md)).
- CE/EDD version: Test-driven development pattern applied к prompts;
  eval suite gates merge
- Jetix adaptation: Each D-document gets multi-dimensional rubric (FPF
  compliance / evidence quality / structural coherence / factual accuracy /
  style / actionability) с separate judge per dimension; calibrate against
  20-30 historical D-docs graded by Ruslan; target Cohen's κ > 0.6 per
  dimension; **Opus 4.7 for high-stakes review, Sonnet 4.6 routine**
- Why modify: Generic EDD lacks Jetix's FPF compliance + multi-view
  publication requirements
- Verification: Pre-publish eval pass per dimension; Ruslan review of
  judge accuracy quarterly

**AD8. PoLL ensemble pattern for high-stakes Audit SKU reviews** ([R-11 §4
Verga et al.](./R-11-evals.md)).
- PoLL version: Panel of 3 diverse smaller models (e.g., command-r +
  gpt-3.5-turbo + haiku) outperforms GPT-4 alone at 1/7 cost
- Jetix adaptation: For Audit SKU final delivery, use PoLL with 3 models
  on different reviewer roles: Haiku 4.5 (compliance reviewer) + Sonnet 4.6
  (FPF-alignment reviewer) + Opus 4.6 (architecture-strategist reviewer);
  diverse model choice breaks sycophancy correlation r=0.902
- Why modify: Heterogeneous models avoid R-4 §2.3 sycophancy DCR 86.36%
- Verification: Inter-judge agreement metric; if all 3 agree on rejection,
  high-confidence reject; if split, escalate к Ruslan

### 4.3 Reject (with rationale)

**R1. Pure "swarm of replaceable agents" topology.** Reject converting 11-agent
hub-and-spoke → 3-5 homogeneous fungible executors (per [R-2 §7](./R-2-swarm-intelligence.md) recommendation).
- Why: Jetix's 11 agents have *functional* specialization (sales/brain/ops/meta)
  not just *task* specialization. Hub-and-spoke with department leads is
  valid Anthropic Research pattern (lead + workers); converting к pure swarm
  loses role-definition clarity required for FPF Role ≠ Executor.
- BUT: Phase 2a reassessment — if one-engineer-per-$10M-ARR threshold
  ([R-5 §7](./R-5-production-case-studies.md)) permits, reconsider.

**R2. Autonomous CLAUDE.md editing without human review** ([R-7 §4.4 Boris's practice](./R-7-boris-cherny-claude-code.md)).
- Why: D6 is 3,758-line constitutional document; Levenchuk critique ([R-3 §6.2](./R-3-self-improving-systems.md))
  warns agents don't strategize in novel situations. Boris's tactical
  CLAUDE.md (2.5k tokens, Anthropic repo) editable by Claude is fine;
  Jetix's D6 cannot be touched without human strategist (Ruslan +
  FPF-Steward audit).
- Modify: Allow Claude к edit per-agent `strategies.md` (bounded scope);
  forbid D6 edits без Ruslan approval.

**R3. Pure per-task pricing (Devin $500/mo original model).**
- Why: R-5 evidence — 96% price cut required to gain adoption. Jetix's
  subscription ($200/mo Max) strictly better economics.

**R4. 20+ MCP servers / heavy MCP wrapping of local resources.**
- Why: [R-8 §6.4](./R-8-skills-claudemd-knowledge.md) GitHub issue #3036 — entire context consumed в 5
  prompts. Nuno Coração case ([R-8 §6.5](./R-8-skills-claudemd-knowledge.md)): wrapping filesystem-accessible
  Obsidian in MCP added latency + overhead for zero gain.
- Modify: Single thin MCP server for wiki (Phase 2a). Third-party MCPs
  only for: Slack (if sales adoption), Stripe (payment), Sentry (if SaaS
  product ships).

**R5. "Multi-agent swarm" as public-facing term.**
- Why: Community skepticism documented ([R-5 §8](./R-5-production-case-studies.md)). Sweep, Wispr,
  Copilot Workspace examples show "swarm" claim backfires. Jetix's
  description "AI-native DACH Mittelstand consultancy with 11 specialized
  agents" accurately frames what Jetix is; doesn't overpromise.

**R6. Parallel code-writing subagents для client code modification.**
- Why: Flappy Bird failure mode ([R-2 §4.2](./R-2-swarm-intelligence.md)). Client codebases have
  tightly-coupled state. Single-thread primary + sub-query-only subagents
  (Cognition pattern) correct default.

**R7. Mem0 / Zep / Cognee wholesale memory migration** ([R-10 §Recommendation §4](./R-10-continual-learning.md)).
- Why: (a) Independent LongMemEval Mem0 49.0% vs Zep 63.8% — Mem0 lacks
  temporal modelling; (b) US-hosted SaaS triggers GDPR Article 17 issues
  for Berlin clients; (c) MemoryAgentBench: well-tuned naïve RAG competitive
  с specialised architectures на most domains; (d) Cognee has no published
  benchmarks despite $7.5M seed
- What to do instead: Anthropic memory tool (ZDR-eligible) + sqlite-vec
  Phase 2 + selective Letta sleep-time trial on ONE agent
- BUT: Phase 2 trial Letta + Zep Flex (€25/mo) selectively, not
  wholesale replacement

**R8. ToT (Tree-of-Thoughts) для production agentic workflows** ([R-9 §3 Q4
Critical Assessment ToT](./R-9-agentic-loop.md)).
- Why: O(b^d) exponential cost; 74% Game of 24 vs 4% CoT but $0.74/case
  vs $0.13 IO prompt; **NOT supported natively в Claude Code/SDK**;
  requires LangGraph LATS scaffolding (which R-9 explicitly recommends
  against для Jetix)
- Conditional: ONLY consider если specific task has discrete-decision
  structure + limited branching factor + verifiable evaluator + budget
  для exponential cost. None of Jetix's 11 agents currently fit.

**R9. 1-5 Likert scales для LLM judges** ([R-11 §4 Hamel](./R-11-evals.md)).
- Why: Hamel verbatim — *"if your evaluations consist of metrics that LLMs
  score on a 1-5 scale, you're doing it wrong."* Forces middle-of-distribution
  noise; binary pass/fail forces honest decisions
- What to do instead: Binary pass/fail с structured critique field (Hamel
  Critique Shadowing 6-step)

**R10. God Evaluator pattern (single judge с 5-10 dimensions)** ([R-11 §4
Stureborg et al.](./R-11-evals.md)).
- Why: Anchoring effects degrade per added attribute; multi-attribute
  rubrics worse than per-dimension judges
- What to do instead: One criterion per judge call (Eugene Yan); separate
  judge per dimension (D-document eval AD7)

**R11. Self-evaluation by generator agent** ([R-11 §9](./R-11-evals.md)).
- Why: Anthropic explicit — *"Out of the box, Claude is a poor QA agent."*
  Sycophancy + self-enhancement bias (+25% win rate Claude-v1 self-judge
  per Zheng et al.)
- What to do instead: Always separate evaluator agent; meta-agent verifier
  role per AC3; Three-agent harness pattern для high-stakes (AD7/A11)

**R12. Public benchmarks (SWE-bench, MMLU, HumanEval) для Jetix-specific
quality decisions** ([R-11 §3](./R-11-evals.md)).
- Why: 49% saturated; contamination crisis (GPT-4o 88% MMLU → 73.4%
  MMLU-CF); Llama 4 Arena gaming 30-position production drop; OpenAI
  abandoned SWE-bench Verified Feb 2026
- What to do instead: Build internal golden sets per Cursor CursorBench
  pattern; refresh quarterly

### 4.4 Defer (Phase 2+ consideration)

**D1. Plugin packaging as `jetix-plugins/jetix-core` marketplace entry.**
- Why defer: Phase 1 solo operator does not benefit от plugin distribution.
- When revisit: First hire (Phase 2a trigger — Triple-AND per D9 §2.3:
  €20K MRR × 3 + Ruslan >40% L1/L2 time + ≥1 client requesting DPA).

**D2. Aggressive sub-agent consolidation (11 → 5-7).**
- Why defer: Jetix's 11-agent roster has functional meaning; consolidation
  loses coordination clarity. But Boris's "sub-agents may be deprecated"
  hint suggests 2026-2027 model improvements may enable.
- When revisit: Q2 2027 if Claude 4.8+ manages context across task boundaries
  without explicit subagent isolation.

**D3. Full wiki → MCP memory migration.**
- Why defer: MCP memory's 3 primitives (entities, relations, observations)
  is simpler than Jetix's 9 entity types. Migration would lose semantic
  depth.
- When revisit: If MCP memory protocol evolves to support typed-entity
  schemas (likely 2026-2027).

**D4. Cross-tool support (Cursor, Codex CLI, Gemini CLI).**
- Why defer: Jetix Phase 1 uses Claude Code exclusively. Premature
  cross-tool support dilutes focus.
- When revisit: Phase 2a (first hire) or if client demands Cursor
  integration.

**D5. Plus One / OpenClaw-style hosted agents.**
- Why defer: Slack-based hosted agent pattern (Every's Plus One, [R-6 §7.2](./R-6-every-cora-compound.md))
  useful для non-technical users. Jetix Phase 1 is all-technical Ruslan.
- When revisit: Phase 2b when first non-technical team member joins
  (COO/marketing/sales).

**D6. Letta sleep-time compute production deployment** ([R-10 §4.6](./R-10-continual-learning.md)).
- Why defer: Pareto improvement (~5×) only when context shared across many
  queries; trial period validates fit; runtime lock-in risk
- When revisit: Phase 2 — trial on ONE high-volume agent (knowledge-synth
  daily wiki preparation); validate ROI before broader adoption

**D7. Inspect AI eval framework adoption** ([R-11 §2](./R-11-evals.md)).
- Why defer: UK AISI government-grade rigor + Docker/K8s sandboxed; overhead
  too high для solo founder; low community adoption (1.3k stars); steep
  learning curve; no SaaS
- When revisit: Phase 3 if formal safety eval becomes contract requirement
  (e.g., enterprise client с safety-critical AI Act compliance audit)

**D8. Braintrust hosted eval+observability platform** ([R-11 §2 Braintrust](./R-11-evals.md)).
- Why defer: $249/mo Pro tier; $80M Series B Feb 2026 vendor; data flywheel
  value not yet justified at Phase 1 scale
- When revisit: When €2K+/mo revenue stable + data volume justifies unified
  eval+production observability + custom autoevals warrant managed Brainstore

**D9. Custom continual learning system Phase 2+** ([R-10 §Recommendation](./R-10-continual-learning.md)).
- Why defer: Off-the-shelf options (Mem0/Letta/Zep) are commercially mature;
  building custom = reinventing wheel
- When revisit: Only if all off-shelf options fail GDPR or FPF integration;
  highly unlikely

**D10. Custom MCP server для wiki cross-tool access** — restated D3 modification.
- Why defer: Phase 2a per existing D3; R-10 §4.5 confirms Anthropic memory
  tool ZDR-eligible covers immediate need; native MCP path now better-supported
- When revisit: Phase 2a (Triple-AND trigger D9 §2.3)

**D11. Multi-agent shared memory protocol** ([R-10 §8.3 ref 109](./R-10-continual-learning.md)).
- Why defer: Mem0 CEO Singh sees as 2026-2027 primary scaling direction;
  no production pattern established yet
- When revisit: Watch ecosystem; revisit Q4 2026 if Letta или MCP standard
  emerges с proven multi-agent shared memory primitive

**D12. Test-time training / memory-weight interpolation** ([R-10 §8.3 refs
111-112](./R-10-continual-learning.md)).
- Why defer: In-Place TTT (ICLR 2026), TTT-E2E (NVIDIA Jan 2026) experimental;
  production-ready timeline open; blurs memory/fine-tuning boundary
- When revisit: 2027+ if research reaches production; not relevant Phase 1-2

---

## Part 5 — Concrete recommendations

### 5.1 Architecture changes (if any)

**AC1. Formalize Jetix's pattern as "Structured Hub-and-Spoke with Verification"
in D6 §2.2a.**
- Current state (D6 §2.2a): Hub-and-spoke discipline стated; coordination
  principles listed
- Recommended change: Add explicit naming "Structured Hub-and-Spoke with
  Verification" (paralleling Anthropic Research "Orchestrator-Worker" and
  Replit "Manager-Editor-Verifier")
- Rationale: Clarifies что Jetix's pattern is canonical production pattern,
  не bespoke hierarchy. [R-5 §6](./R-5-production-case-studies.md) canonical reference.
- Impact: D6 §2.2a 2-line addition; no D9 change
- Effort: 30 min

**AC2. Add "Verification" clause to each agent's role.md Block 3 (Method).**
- Current state (D3): Role-manifests have 5 blocks но no explicit verification
  signal per Block 3
- Recommended change: Add `verification_signal:` field to Block 3
  (e.g., "test suite pass", "schema validation", "linter clean", "acceptance-authority
  sign-off")
- Rationale: Boris's 2-3× quality gain via verification loop ([R-7 §6.1](./R-7-boris-cherny-claude-code.md));
  Kim et al. "verification beats agent count" ([R-2 §3.6](./R-2-swarm-intelligence.md))
- Impact: D3 18 role-manifests; 1h total update
- Effort: 1h

**AC3. Make `meta-agent` explicitly "Verifier" role in D6 §2.2.**
- Current state: meta-agent "quarterly audit scope" (D6 §5.4)
- Recommended: Rename role responsibility к include "Verification" как
  first-class responsibility + FPF-Steward sub-role + Anti-sycophancy
  discipline
- Rationale: R-4 §2.3 sycophancy at 86.36% requires dedicated anti-sycophancy
  discipline; meta-agent best positioned
- Impact: D6 §2.2 + D6 §5.4
- Effort: 1-2h

**AC4. Add explicit "agent replaceability test" к D6 §5.1 (Role ≠ Executor).**
- Current state: P2 Role ≠ Executor stated as principle
- Recommended: Add test: *"Can role's executor be swapped (Claude Haiku 4.5
  → Haiku 5.x) в 5 minutes без re-writing role.md or breaking workflows?
  If not, role.md has smuggled executor-specific assumptions."*
- Rationale: Boris's replaceable agents principle ([R-7 §3.2](./R-7-boris-cherny-claude-code.md)); R-2
  canonical; validates architectural claim
- Impact: D6 §5.1; 30 min addition
- Effort: 30 min

### 5.2 D1-D8 writing methodology changes

**MC1. Adopt CE-augmented writing methodology для D1-D8 (hybrid).**

| Document | Current plan | CE-augmented plan |
|----------|--------------|-------------------|
| D1 Architecture Final | Full V5 writing | Plan → Write → /ce-code-review (6 viewpoints: ontology, compliance, clarity, completeness, actionability, FPF-alignment) → Compound |
| D2 Folder Structure | Full V5 | Single-pass; structure is discoverable |
| D3 Role Manifests (18) | Full V5 | Parallel batch write; each role reviewed by 3-reviewer fan-out (ontology + verification_signal + FPF-alignment) |
| D4 Life-OS vs Jetix | Full V5 | Single-pass; mostly decisions already made |
| D5 Knowledge Architecture | Full V5 | Plan → Write → /ce-code-review → Compound (this is methodology-heavy) |
| D6 JETIX-FPF | 3 passes per ADR Area 6 | **Keep 3-pass; add 12-reviewer fan-out at pass 2→3 transition** |
| D7 Career Levels | Full V5 | Single-pass |
| D8 Instructions (rollout) | Full V5 | Plan → Write → /ce-code-review (is-runnable, has-verification, timeline-realistic) → Compound |

**Rationale:** CE's 80/20 plan+review / work+compound discipline accelerates
writing quality where review catches errors cheaper than correction. D2,
D4, D7 are decision-heavy (low review value); D1, D3, D5, D6, D8 are methodology-
heavy (high review value). Hybrid application matches where each discipline
helps.

**MC2. `/ce-compound-refresh` discipline for stale sections.**
- During D6 3-pass writing, mark sections со `_stale: true` when updates
  supersede prior content; at pass 3, `/ce-compound-refresh` identifies
  and reconciles
- Rationale: D6 3,758 lines accumulated over 3 passes + 8 ADR chunks;
  internal contradictions likely
- Effort: 2-3h during D6 pass 3

### 5.3 Tooling adoption

**T1. Skills system (`~/.claude/skills/` + `.claude/skills/`)** — Phase 1 Day 10-11.

First 5 skills to create:

1. **`ingest`** (`.claude/skills/ingest/SKILL.md`, `disable-model-invocation: true`):
   - Wraps current `/ingest` behavior
   - `allowed-tools: Bash(python3 tools/ingest.py:*)`
   - Writes к wiki/; human-invoked only (destructive)

2. **`ask`** (`.claude/skills/ask/SKILL.md`, default invocation):
   - Description: "Searches and synthesizes answers from the Jetix wiki.
     Use when user asks about any topic covered by wiki/concepts,
     wiki/entities, wiki/topics, or wiki/sources, including methodology
     questions, past decisions, client context, or FPF ontology."
   - Claude auto-fires when description matches query

3. **`lint`** (`.claude/skills/lint/SKILL.md` + `PostToolUse` hook):
   - Description: "Runs wiki health checks for orphans, contradictions,
     stale claims"
   - Hook triggers on Write/Edit to `wiki/**` для deterministic execution

4. **`close-day`** (`.claude/skills/close-day/SKILL.md`, default invocation):
   - Implements jonathanmalkin `/wrap-up` 4-phase
   - `allowed-tools: Bash(git add:*), Bash(git commit:*), Bash(git push:*)`

5. **`plan-day`** (`.claude/skills/plan-day/SKILL.md`, default invocation):
   - Enhanced с CE `/ce-plan` subagents pattern: `best-practices-researcher`,
     `repo-research-analyst`, `learnings-researcher`, `git-history-analyzer`

**T2. Subagents for Jetix-specific review** — Phase 1 Day 11-12.

Create `.claude/agents/`:
- `jetix-fpf-alignment-reviewer.md`
- `jetix-dsgvo-reviewer.md`
- `jetix-ai-act-reviewer.md`
- `jetix-fgr-tagging-reviewer.md`
- `jetix-multiview-reviewer.md`
- `jetix-boundary-discipline-reviewer.md`
- `jetix-hgb-finance-reviewer.md`
- `jetix-ustg-invoice-reviewer.md`

Each agent: isolated context, read-only tool subset (`Read, Grep, Glob`),
outputs structured report (CONCERN / SEVERITY / EVIDENCE / RECOMMENDATION).

**T3. Hooks для determinism** — Phase 1 Day 2 (already planned in D8 hooks).

Extend existing 4 pre-commit hooks с:
- `PostToolUse` on Write/Edit `~/jetix-os/jetix/**/*.yaml` → validate
  frontmatter schema
- `PostToolUse` on Write/Edit `~/jetix-os/jetix/wiki/**/*.md` → validate
  9-edge graph consistency
- `PreToolUse` on Bash → secret scrubbing
- `Stop` hook → reminder к append к strategies.md if session ≥30min

**T4. CLAUDE.md hierarchy restructure.**

Current: project CLAUDE.md (verified ~130 lines from context dump).

Recommended (per [R-8 §2.3](./R-8-skills-claudemd-knowledge.md)):
```
~/jetix-os/
├── CLAUDE.md              (project — <100 lines, index)
├── .claude/
│   ├── rules/
│   │   ├── ontology.md    (FPF + alpha discipline)
│   │   ├── compliance.md  (EU AI Act + GDPR + HGB)
│   │   ├── writing-style.md
│   │   └── git-workflow.md
│   └── skills/
├── life-os/CLAUDE.md      (personal scope)
└── jetix/CLAUDE.md        (jetix scope — already)
```

Each file <100 lines. Import via `@.claude/rules/ontology.md` syntax in
project CLAUDE.md.

**T5. MCP servers к adopt** — Phase 1:
- `@modelcontextprotocol/server-filesystem` (Jetix repo paths)
- `context7` (upstash/context7 — live docs для Claude API, TypeScript, Python libs)
- `notion` MCP (decommission target — per CLAUDE.md "Notion decommission by Day 14")

MCP servers к defer:
- Slack (Phase 2a — first client engagement)
- Stripe (when first invoice готова)
- Sentry (if SaaS product ships)
- Jetix custom wiki MCP (Phase 2a per R-8 §7.2)

**T6. Plugin ecosystem относительно Jetix Phase 1.**

Phase 1 install (Day 10-11):
- `@anthropic/compound-engineering-plugin` (Every's 50+ agents, 42+ skills) — **fork
  and customize к DACH**
- `typescript-lsp` (Anthropic official)
- `claude-md-management` (for audit и improvement of CLAUDE.md files)

Phase 1 skip:
- GitHub/GitLab plugins (personal git workflow; not needed для solo operator)
- Atlassian, Asana, Linear, Notion plugins (Notion decomms)
- Figma, Vercel, Firebase (no frontend/hosting yet)
- External integrations that are Phase 2a+

### 5.4 Knowledge storage migration

**Migration plan** (aligned с R-8 §7.2 phased path):

**Phase 1 (Day 10-14):**
- Convert /ingest /ask /lint /close-day /plan-day к native Skills
- Audit CLAUDE.md files; shrink root к <100 lines via rule extraction к
  `.claude/rules/*.md`
- Add `lessons.md` pattern to per-agent strategies.md (ACE append-only)

**Phase 1 Day 15-17:**
- Install Every's compound-engineering-plugin; fork DACH variants
- Create 8 Jetix-specific review subagents
- Wire к `/close-day` skill

**Phase 2a (when Triple-AND trigger fires — D9 §2.3):**
- Build thin in-house MCP server for wiki (5 tools)
- Begin `.claude-plugin/plugin.json` packaging for `jetix-core` plugin
- Set up private marketplace (GitHub repo)

**Phase 2b:**
- Full plugin distribution к first hire
- Cross-machine sync via private marketplace pull

**Phase 3:**
- Consider federation pattern: per-entity plugin (jetix-gmbh-core vs.
  jetix-holdings-core vs. jetix-de-core)

**What stays custom:**
- Wiki storage engine (9 entity types exceeds MCP memory's 3 primitives)
- FPF ontology discipline (no CE equivalent)
- Past-participle state machines (genuine innovation)
- Multi-View Publication Kit (E.17 adaptation)
- F-G-R trust tagging (genuine innovation)

### 5.5 Agent architecture evolution

**11 agents → proposed Phase 1 stability + Phase 2a reassessment.**

| Agent | Phase 1 action | Phase 2a reassess |
|-------|----------------|-------------------|
| manager | Keep; clarify "Structured Hub-and-Spoke Orchestrator" label | Consider fold `manager` role к `chief-of-staff` (first hire) |
| personal-assistant | Keep | Consider merge с `system-admin` если first hire is tech-heavy |
| system-admin | Keep | As above |
| sales-lead | Keep; primary revenue-generating agent | Hire replacement or promote agent к J-Approve default |
| sales-research | Keep | Phase 2a grow to include `market-research`, `competitor-tracking` subagents |
| sales-outreach | Keep | Consider split: outreach vs community-engagement |
| inbox-processor | Keep | May fold к PA если volume low |
| crazy-agent | Keep; unique orthogonal value | Keep indefinitely |
| knowledge-synth | Keep; critical для CE Compound step | Phase 2a promote к J-Strategic partial (eval-based) |
| strategy-support-analyst | Keep; only Opus agent | Could split к research vs. analysis |
| meta-agent | Keep + strengthen verifier role | Separate FPF-Steward to own role at trigger (30+ agents OR 1+ human meta-hire OR quarterly audit >4h) |

**Net Phase 1:** Keep 11 with enhanced responsibilities (verifier role explicit
на meta-agent, verification_signal on all role.md Block 3).

**Net Phase 2a+:** Reassess if first hire changes operational structure.

### 5.6 NEW — Eval infrastructure (from R-11)

**Phase 1 minimum viable eval setup** ([R-11 §8.1, §8.2](./R-11-evals.md)) — fills v1 G4
gap fully:

**Stack choice.** Promptfoo (CLI, MIT, free) + Langfuse (cloud Hobby $0
or self-hosted Docker Compose). Total Phase 1 budget: **~$50-209/mo**.
Phase 2 step-up к ~$300-450/mo при revenue growth.

**Step-by-step rollout:**

1. **Day 14 (1h):** Install Promptfoo CLI; sign up Langfuse cloud Hobby
   tier (or `docker-compose up` self-host)
2. **Day 14-15 (4h):** Pilot agent = `sales-researcher` (clearest factuality
   criteria); hand-grade 30 examples; store as
   `evals/sales-researcher/golden-set.jsonl`
3. **Day 15 (3h):** Build first LLM-judge: Haiku 4.5 model, **binary pass/
   fail** (NEVER 1-5 Likert), **reference-anchored**, ONE criterion per
   call; calibrate against 20-30 Ruslan-graded examples; target precision
   >0.85, recall >0.85
4. **Day 15 (1h):** Add GitHub Action `.github/workflows/eval.yml` PR gate
   at ≥85% pass rate; non-zero exit blocks merge
5. **Day 16-17 + ongoing:** Repeat steps 2-3 для remaining 10 agents over
   4-6 weeks (4-6h per agent); FPF compliance eval per [R-11 §8.5](./R-11-evals.md)
   hybrid 2-layer approach added в Phase 2

**Per-agent eval design table** (from [R-11 §8.2](./R-11-evals.md), distilled):

| Agent | Quality dimensions | Eval mix | Golden set |
|-------|---------------------|----------|------------|
| sales-researcher | Factuality, completeness, relevance | LLM-judge factuality + deterministic schema | 30-50 prospect briefs с known facts |
| sales-outreach | Tone, personalization, compliance | LLM-judge tone + deterministic length/banned-phrases | 30-50 outreach drafts с rubric |
| sales-lead | Pipeline reasoning, decision quality | Trajectory + LLM-judge | 20-30 Ruslan-graded pipeline decisions |
| inbox-processor | Categorization accuracy, action suggestion | Deterministic + LLM-judge | 50 inbox items с ground truth |
| personal-assistant | Task completion, action quality | Trajectory + HITL sample | 30 task scenarios |
| system-admin | Command correctness, safety | Deterministic + sandboxed execution | 30-50 admin tasks |
| crazy-agent | Idea novelty, relevance | LLM-judge pairwise (с position swap) | 30 brainstorm prompts |
| knowledge-synth | Synthesis quality, citation accuracy | Trajectory + LLM-judge multi-dim | 20-30 synth tasks |
| strategy-support-analyst | Reasoning quality, evidence grounding | LLM-judge multi-dim (one per dim) + Ruslan review | 15-20 strategic analysis tasks |
| meta-agent | Audit catches, F-G-R compliance | Trajectory + comparison к Ruslan ground truth | 20-30 audit scenarios |
| manager | Routing correctness, escalation appropriateness | Trajectory + LLM-judge | 30 routing scenarios |

**D-document writing eval** ([R-11 §8.3](./R-11-evals.md)). Multi-dimensional rubric с
**separate judge per dimension** (one criterion per call principle):
- FPF compliance (judge: Sonnet 4.6, calibrated against D6 reference)
- Evidence quality (judge: Sonnet 4.6, R-grade verifier)
- Structural coherence (judge: Haiku 4.5)
- Factual accuracy (judge: Sonnet 4.6 + reference-anchored)
- Style (judge: Haiku 4.5)
- Actionability (judge: Sonnet 4.6, requires concrete action items)

Use Opus 4.7 for high-stakes review; Sonnet 4.6 routine. Calibrate against
20-30 historical D-docs graded by Ruslan; target Cohen's κ > 0.6.

**FPF compliance eval (hybrid 2-layer)** ([R-11 §8.5](./R-11-evals.md)):
- **Layer 1 deterministic**: FPF principle name regex (P1...P8, IP-1...IP-8,
  CP-1...CP-5) + required sections present (Block 1-5 для role-manifests,
  etc.)
- **Layer 2 rubric LLM-judge**: 5 dimensions (Principle Derivation /
  Assumption Explicitness / Evidence Grounding / Internal Consistency /
  Scope Appropriateness)
- Calibrate с 5 strong + 5 borderline + 5 non-compliant examples; target
  Cohen's κ > 0.7
- Single judge sufficient — FPF criteria explicit и discrete

**Compound learning eval** ([R-11 §8.4](./R-11-evals.md)):
- Frozen Q1 golden sets per agent (30-50 examples), locked, version-controlled
- Run full eval at end of each quarter с identical prompt/judge config
- **Score trajectory = primary compound-learning signal**
- Velocity metrics (tasks/week, skill count, satisfaction self-reports) =
  **vanity unless paired** с stable golden-set scores

**Phase 2 additions** (€2K+/mo revenue):
- Add Braintrust ($249/mo Pro) для unified eval+observability if data-flywheel
  value justified
- Three-agent harness pattern (Planner→Generator→Evaluator) для D-document
  quality when D-doc throughput >5/week (A11/AD7)
- pass^k reliability testing для high-stakes agents (k=3-5 minimum)
- Tiered online middleware (Layer 1 deterministic every request → Layer 2
  heuristic → Layer 3 LLM-judge 5% async → Layer 4 human review)

### 5.7 NEW — Continual learning infrastructure (from R-10)

**Phase 1 ($0)** ([R-10 §Recommendation §3](./R-10-continual-learning.md)) — additive к existing T1-T6:

- **Enable Anthropic Claude Projects memory** для all 6 departments (free
  since March 2026; per-project memory isolation)
- **Adopt Anthropic memory tool** (beta `context-management-2025-06-27`)
  selectively — ZDR-eligible (critical Berlin GDPR Article 17); 6 commands
  view/create/str_replace/insert/delete/rename
- **Formalize per-agent strategies.md → SKILL.md** (Anthropic Agent Skills
  standard, Apache 2.0 Dec 2025); see A13
- **Add `wiki/eval-canaries.md`** с 10-15 unusual probe facts; bi-weekly
  recall tests = MVP eval harness

**Phase 2 (1-4 weeks, ~$25/mo cap):**
- **sqlite-vec semantic index** over wiki entities когда count exceeds ~200
  (free, zero-server, coexists с markdown)
- **Trial Letta sleep-time agent на ONE high-volume agent** (knowledge-synth
  recommended); self-host, Apache 2.0; human-approval gate on
  `proposed-wiki-updates.md`
- For 2-3 agents tracking evolving facts only, **Zep Flex $25/mo** trial
  for 30 days; measure recall on temporal queries

**Phase 3 (3-6 months):**
- Cognee migration ONLY if `edges.jsonl` exceeds ~500 edges с multi-update-
  per-week churn

**Memory taxonomy mapping for Jetix** (R-10 §1.4 + §7.2):
- `wiki/concepts/` + `wiki/entities/` = **semantic memory**
- `mailboxes/<id>.jsonl` = **episodic memory**
- per-agent `strategies.md` = **procedural memory**
- per-agent `scratchpad.md` = **working memory**
- `wiki/graph/edges.jsonl` 9 typed edges = **associative/knowledge graph**

Make this mapping explicit в D6 §5.2-5.4.

### 5.8 NEW — Agentic loop infrastructure (from R-9)

**Phase 1 (Day 11-12, 4-6h):** Encode per-agent loop variant + maxTurns +
termination stack в YAML role-manifest.

**4-layer termination stack mandatory** ([R-9 §5 Q8 + Recommendations](./R-9-agentic-loop.md)):
```yaml
loop:
  variant: ReAct  # or: Plan-and-Execute / Self-Refine / Reflexion / CodeAct
  maxTurns: 25  # hard cap per [R-9 Recommendations table]
  taskBudget:
    header: "task-budgets-2026-03-13"
    tokens: 50000  # soft limit
  completionPredicate:
    type: schema-validation  # or: test-pass / linter-clean / acceptance-signal
    spec: "evals/<role>/completion-oracle.yaml"
  escalationTrigger:
    irreversible_actions:
      - send-email
      - publish-content
      - delete-data
    require_approval: true
```

**Per-agent maxTurns recommendations** (from [R-9 Recommendations table](./R-9-agentic-loop.md)):
- inbox-processor (lookup) → **5-8**
- sales-outreach / sales-researcher → **10-20**
- personal-assistant (operations) → **15-25** + human gates
- knowledge-synth (research broad) → **30-50**
- crazy-agent (creative + refine) → **8-12**
- strategy-support-analyst (deep planning) → **15-25** + extended thinking
- system-admin (technical) → **10-20**
- sales-lead (CRM) → **10-15**
- meta-agent (auditing) → **15-25**
- manager (routing) → **5-10** (orchestrator, не executor)

**Per-department loop variant assignment** (from [R-9 Recommendations
table](./R-9-agentic-loop.md)) — see A15 для full enumeration.

**Extended thinking on long-horizon** (A16): enable on strategy-support-
analyst + knowledge-synth + meta-agent FPF-Steward sub-role.

**Sub-agent context-passing rule**: messages в `mailboxes/<id>.jsonl` MUST
include full reasoning trace, не только outcomes (Walden Yan Principle 1
[R-9 §7 Q14](./R-9-agentic-loop.md)). Update message schema accordingly.

---

## Part 6 — Decision matrix для Ruslan

### D1. Adopt Skills system?

**Options:**
- **yes-now** (adopt in Phase 1 Day 10-11) ← **recommended**
- yes-Phase-2 (defer)
- no (keep custom /ingest /ask /lint)

**Trade-offs:**
- Adopting now costs 4-6h; saves ~2,000 tokens/session + cross-tool interop
- Deferring preserves familiar custom scripts at cost of context bloat
  и ecosystem disconnection
- Not adopting at all reinvents what native stack provides; R-8 §6.1 explicitly
  flags this as anti-pattern #1

**Recommendation:** **yes-now**. Skills are open standard (Dec 2025); the
migration cost is low (4-6h); benefits compound over time (every session
saves tokens + auto-invocation); deferring creates migration debt.

**Confidence:** High. R-8 §7.2 explicitly recommends this path; low risk;
reversible (skills are markdown files).

**Dependencies:** None.

---

### D2. Revise D6 v3 с CE concepts?

**Options:**
- yes (rewrite D6 incorporating CE loop + Every plugin patterns)
- no (keep D6 v2 constitutional; CE as operational overlay) ← **recommended**
- partial (add D6 §15 "CE Operational Patterns" without touching §1-14)

**Trade-offs:**
- Full rewrite contaminates Levenchuk-grade ontology (F-G-R, A.14, U-Types)
  с less-rigorous CE concepts; destructive
- Keeping D6 v2 preserves constitutional status; CE lives as Phase 1 operational
  discipline in D8 and skills
- Partial addition confuses document layering; operational details belong in
  D8, not D6

**Recommendation:** **no**. D6 v2 is constitutional (Levenchuk-grade ontology);
CE is operational practice (belongs in D8). Adopting partial (new §15 "CE
Operational Patterns") creates hybrid document с two quality tiers. Keep
clean separation: D6 = what exists ontologically; D8 = how we operate.

**Confidence:** High. Document layering discipline per IP-3 (Artifacts
over conversations); CE additions belong in operational docs.

**Dependencies:** D8 must incorporate Part 5 recommendations.

---

### D3. Update D1-D8 methodology?

**Options:**
- Keep current Variant A Full V5 (no CE adoption during writing)
- Adopt CE-augmented methodology fully
- **Hybrid (recommended)** ← per Part 7 Option C below

**Trade-offs:**
- Keeping V5 = known execution pattern; 14-day calendar per original plan
- Full CE = potentially 15-30% faster writing но process overhead on
  decision-heavy documents (D2, D4, D7)
- Hybrid = CE-augmented только на methodology-heavy docs (D1, D3, D5, D6,
  D8); Variant A on decision-heavy (D2, D4, D7)

**Recommendation:** **Hybrid**. Apply CE 80/20 discipline на docs where
review catches errors cheaper than correction. See Part 7 Option C for
detailed calendar.

**Confidence:** Medium-high. CE works for methodology; unproven on pure
decision-recording documents.

**Dependencies:** Compound Engineering plugin installed; 8 Jetix review
subagents created.

---

### D4. Migration wiki/ → native Skills?

**Options:**
- yes-full (migrate wiki к SKILL.md format)
- yes-partial (migrate /ingest /ask /lint к skills, keep wiki/ as custom storage) ← **recommended**
- no (keep everything custom)

**Trade-offs:**
- Full migration loses Jetix's 9 entity types + edges (MCP memory has only 3 primitives); loses F-G-R tagging discipline; loses FPF ontology grounding
- Partial migration gets skills ecosystem benefits без losing wiki depth
- No migration reinvents skill infrastructure

**Recommendation:** **yes-partial**. R-8 §7 explicit: wiki is the 20% that
is genuinely additive; skills are the 70-80% that's reinvented. Migrate
commands; keep storage; expose wiki via MCP Phase 2a.

**Confidence:** Very high. R-8 §7 provides detailed migration path; reversible.

**Dependencies:** None for partial migration; MCP server build для Phase 2a.

---

### D5. Replace 11-agent hub-spoke with pure swarm?

**Options:**
- yes (convert к 3-5 fungible executors per R-2 §7)
- no (keep 11-agent structure) ← **recommended Phase 1**
- hybrid (keep structure, reduce to 7-8 at Phase 2a)

**Trade-offs:**
- Yes costs: lose functional specialization (sales/brain/ops/meta), lose D3 role-manifest investment
- Yes benefits: lower coordination tax (past Rule of 4 knee), simpler mental model
- No costs: 11 agents past Rule of 4 sweet-spot; coordination overhead
- Hybrid: reassess at Phase 2a trigger; no rework now

**Recommendation:** **no (Phase 1) + reassess at Phase 2a**. Reasons:
(a) 11-agent investment already committed to D3 manifests; (b) Boris Cherny's own practice has specialized subagents; (c) R-5 §6 Replit production
pattern matches Jetix structure; (d) Phase 2a trigger naturally forces
reassessment.

**Confidence:** High for Phase 1; Medium for Phase 2a reassessment.

**Dependencies:** D9 Triple-AND trigger conditions.

---

### D6. Adopt Compound cycle для D1-D8 writing?

**Options:**
- yes (apply Plan/Work/Review/Compound к all D1-D8)
- no (traditional single-pass with final review)
- selective (apply к D1, D3, D5, D6, D8; skip D2, D4, D7) ← **recommended**

**Trade-offs:**
- Full application = review/compound overhead on decision-heavy docs (D2, D4,
  D7) where single-pass is faster
- No application = miss CE benefits on methodology-heavy docs
- Selective = match methodology to document type

**Recommendation:** **selective**. Apply compound cycle где it helps:
methodology-heavy docs (D1, D3, D5, D6, D8). Single-pass for decision-heavy
(D2, D4, D7).

**Confidence:** Medium-high. D6 already committed к 3-pass writing; compound
cycle = natural extension.

**Dependencies:** D3 (MC1).

---

### D7. Subagent strategy: current per-task spawn OR persistent named subagents OR both?

**Options:**
- Current (spawn per-task via `Agent` tool)
- Persistent named (`.claude/agents/<name>.md` with `memory: project`)
- Both (stateless spawns for research, persistent for review/specialized) ← **recommended**

**Trade-offs:**
- Current = matches Boris's replaceable agents; simple; but loses specialization benefits
- Persistent = matches Every plugin's 50 named agents; better routing via description
- Both = best of both; cost is learning which pattern for which task

**Recommendation:** **both**. Use persistent named subagents for specialized
review roles (8 Jetix reviewers listed in T2 above); use per-task spawns
для exploratory research and planning. This matches Boris's practice
(planner subagent + 5 false-positive subagents) and Every's plugin (named
reviewers).

**Confidence:** High. Both patterns production-validated.

**Dependencies:** T2 (create 8 Jetix review subagents).

---

### D8. Hooks adoption: aggressive / conservative / none?

**Options:**
- Aggressive (all 27 lifecycle events where applicable)
- **Conservative (4 pre-commit + 3-4 PostToolUse + Stop hook)** ← **recommended**
- None (CLAUDE.md-only advisory)

**Trade-offs:**
- Aggressive risks brittleness; debugging hook chains is hard per R-4 §4.1
- Conservative captures must-happen-every-time determinism per Builder.io tip #38 без complexity
- None loses determinism advantage

**Recommendation:** **conservative**. Keep 4 pre-commit hooks (planned in
D8). Add 3-4 PostToolUse hooks (format, lint, schema validation, secret-
scrubbing). Add Stop hook reminder to append к strategies.md. Total: ~8 hooks
— well below 27-event complexity risk.

**Confidence:** High. Boris's own practice matches this level (1-2 PostToolUse
hooks, некоторые project-specific).

**Dependencies:** T3 implementation Day 2 (pre-commit) + Day 10 (skills/hooks
interaction).

---

### D9. Memory architecture — wiki/+strategies.md continuation OR Mem0/Letta/Zep adoption OR Anthropic memory tool OR hybrid?

**Options:**
- A. Keep current wiki/+strategies.md+scratchpad+mailboxes+voice-notes only
- B. Wholesale migrate к Mem0 Cloud Standard ($19/mo)
- C. Wholesale migrate к Letta Pro ($20/mo) + Context Repositories
- D. Wholesale migrate к Zep Cloud Flex ($25/mo)
- E. **Hybrid (recommended)** ← R-10 explicit recommendation

**Hybrid (E) details** ([R-10 §Recommendation §3](./R-10-continual-learning.md)):
- **Phase 1 ($0):** Keep wiki/+strategies.md as authoritative source-of-
  truth (R-10 §7.2 endorses this); + Anthropic memory tool selectively for
  client-data agents (ZDR, GDPR-compliant); + Anthropic Claude Projects
  memory for departments; + formalize strategies.md → SKILL.md
- **Phase 2 (€25/mo cap):** Add sqlite-vec semantic index when wiki entities
  >200; trial Letta sleep-time agent на ONE high-volume agent (knowledge-
  synth); trial Zep Flex selectively только for 2-3 agents tracking evolving
  facts (e.g., sales-lead pipeline state)
- **Phase 3 (3-6 months):** Cognee migration ONLY if edges.jsonl >500 edges
  с multi-update-per-week churn

**Trade-offs:**
- Option A: zero migration cost; misses sleep-time compute 5× efficiency;
  no temporal modelling; manual consolidation only
- Option B (Mem0): independent LongMemEval 49.0% (15pt below Zep); no
  temporal modelling; US-hosted = GDPR concern
- Option C (Letta): best architectural fit; runtime lock-in risk; Apache 2.0
  self-host viable
- Option D (Zep): best temporal accuracy (LongMemEval 63.8%); CE deprecated
  April 2025 — only Cloud Flex; US-hosted GDPR concern
- Option E (Hybrid): preserves wiki advantages + selective augmentation +
  GDPR-compliant via Anthropic memory tool + reversible

**Recommendation:** **E. Hybrid**. Wiki+strategies.md endorsed as production
canonical pattern by Karpathy + Boris + Letta + Anthropic memory tool team.
Selective augmentation via Anthropic memory tool (ZDR), sqlite-vec, и Letta
sleep-time trial preserves transparency и GDPR while capturing 80% of
managed-service value at <10% cost.

**Confidence:** Very high. R-10 explicit Jetix recommendation; multi-source
endorsement; reversible.

**Dependencies:** A12 (Anthropic memory tool integration), A13 (SKILL.md
migration). Phase 2 deps: trial budget approval; Letta self-host setup
2-3h.

---

### D10. Eval framework — none OR Inspect AI OR Promptfoo+Langfuse OR Braintrust OR custom?

**Options:**
- A. None Phase 1 (continue manual review only)
- B. Inspect AI (UK AISI government-grade)
- C. **Promptfoo + Langfuse (recommended Phase 1)** ← per [R-11 §8.1](./R-11-evals.md)
- D. LangSmith (LangChain hosted, $5/1k traces)
- E. Braintrust ($249/mo Pro)
- F. Custom Anthropic Console-based (NOT recommended — UI-only)

**Trade-offs:**
- Option A: zero cost; misses CE quality multiplier (Boris's 2-3×); blind
  compound step; flag-list G4 + new G8 unfilled
- Option B: government-grade rigor; overhead too high для solo founder;
  steep learning curve; low community adoption (1.3k stars)
- Option C: **Anthropic-endorsed (Jan 2026 blog) як self-hosted alternative
  к LangSmith**; first-class trajectory assertions; 100% local execution;
  EU residency; $50-209/mo Phase 1 budget; reversible (configs are YAML)
- Option D: Most mature LangChain-aligned; less ideal outside LangChain
  ecosystem
- Option E: Unified eval+observability; $80M Series B vendor; $249/mo too
  high Phase 1; revisit Phase 2 при revenue growth
- Option F: "Creates false confidence" per R-11 §9; doesn't scale

**Recommendation:** **C. Promptfoo + Langfuse**. Cost-effective ($50-209/mo),
Anthropic-recommended, EU-friendly, 100% local execution, reversible.
Phase 2 step-up к Braintrust when €2K+/mo revenue justifies $249/mo. **Adopt
Hamel Husain Critique Shadowing 6-step workflow** as judge-building method
([R-11 §4](./R-11-evals.md)).

**Confidence:** Very high. R-11 explicit primary recommendation; production-
validated; reversible.

**Dependencies:** A9 (Promptfoo+Langfuse setup), A10 (Hamel workflow), A11
(three-agent harness for D-doc eval), AD7 (eval-driven development).

---

### D11. Agentic loop pattern — keep ReAct default OR adopt explicit per-department variants OR formal Plan-and-Execute everywhere?

**Options:**
- A. Keep ReAct default for all 11 agents (current de-facto state)
- B. **Adopt per-department variant assignment per [R-9 Recommendations](./R-9-agentic-loop.md)
  (recommended)** ← matches R-9 explicit table
- C. Formal Plan-and-Execute everywhere (Devin/Cursor Plan-mode style)
- D. Formal Reflexion для all review cycles only

**Trade-offs:**
- Option A: zero implementation cost; misses cost/quality optimization
  per agent type; tool-call storm risk без variant-specific termination
- Option B: per-dept optimization; ~4-6h Phase 1 implementation; matches
  R-9 explicit recommendation; combines с 4-layer termination stack (A14)
  и extended thinking (A16)
- Option C: planning overhead on simple tasks; suited только to certain
  agents (knowledge-synth/strategist); too rigid для creative (crazy-agent)
- Option D: Reflexion fails after 4 trials and on creative tasks per
  R-9 Critical Assessment; selective use only (AD6)

**Recommendation:** **B. Per-department variant assignment**:
- system-admin / sales-outreach (technical) → ReAct + CodeAct (Bash)
- knowledge-synth / sales-researcher → Orchestrator-Worker + Plan-and-Execute
- crazy-agent (creative) → Self-Refine 3-4 iterations
- sales-lead / sales-outreach (CRM) → ReAct + Reflexion на outcome signals
- personal-assistant (operations) → Plan-and-Execute + HITL interrupts
- meta-agent (auditing) → Self-Refine + ReAct evaluator-optimizer
- strategy-support-analyst (planning) → Plan-and-Execute + extended thinking
- inbox-processor / manager → ReAct (lookup/routing)

Encode в YAML role-manifest + `loop:` block per A14 termination stack.

**Confidence:** High. R-9 explicit per-dept table; production-validated patterns;
reversible (YAML config).

**Dependencies:** A14 (4-layer termination stack), A15 (per-dept variant
encoding), A16 (extended thinking on long-horizon). Manifests update в
D3 18 role-manifests.

---

### Update note on existing D1-D8 (R-9/R-10/R-11 review)

After integrating R-9/R-10/R-11 evidence, **D1-D8 recommendations remain
valid** with following clarifications:

- **D1 (Skills migration):** Confidence raised к **Very High** — R-10 §8.1
  confirms Anthropic Agent Skills standard (Apache 2.0 Dec 2025) is industry
  consensus с progressive disclosure pattern. Now includes A13 (ACE structured
  entries в SKILL.md format).
- **D2 (D6 v3 vs CE concepts):** Unchanged — still recommend **no**.
- **D3 (D1-D8 methodology):** Hybrid recommendation extended — apply Three-
  agent harness pattern (A11/AD7) к D1, D5, D6, D8 (methodology-heavy).
- **D4 (wiki migration):** Confidence raised к **Very High** — R-10 §7.2
  explicit endorsement of Jetix's wiki+strategies.md как production canonical.
  Combined с D9 hybrid: confirmed yes-partial migration (skills) + keep
  storage (wiki).
- **D5 (11-agent vs swarm):** Unchanged — keep Phase 1; reassess Phase 2a.
  R-9 §Recommendations endorses Hierarchical Orchestrator-Worker как
  matching Jetix pattern.
- **D6 (Compound cycle):** Selective adoption confirmed; D-doc eval (AD7)
  adds eval-driven discipline.
- **D7 (Subagent strategy):** Both pattern confirmed; ADD critical clarification
  — sub-agent messages MUST contain full traces (Walden Yan Principle 1 per
  R-9 §7 Q14), не только summaries.
- **D8 (Hooks adoption):** Conservative confirmed; ADD hook for `Stop` event
  reminder к eval-suite-run; ADD `PostToolUse` for memory tool (Anthropic
  memory tool client-side audit log).

---

## Part 7 — Updated D1-D8 plan options

### 7.1 Option A: Keep current Variant A Full V5 (no CE adoption)

**What happens:** Jetix writes D1-D8 per current plan (14-day calendar).
No Skills migration; no Compound Engineering plugin; no Jetix review subagents.

**Calendar:** 14 days per original plan.

**Risks:**
- Misses 2,000 token/session savings от skills (compounding cost over 12+
  months at 40-80 sessions/day = ~€50-100/mo unnecessary spend)
- Reinvents what native Claude Code provides (anti-pattern #1 per R-8 §6.1)
- Cross-tool portability blocked (Cursor, Codex CLI)
- No CE compound loop operationalized (manual memory discipline only)

**Recommendation: REJECT.** Missing-opportunity cost is substantial.

### 7.2 Option B: CE-augmented methodology (full adoption)

**What happens:** Jetix adopts everything from Part 5 immediately:
- Skills migration Day 10-11
- Every plugin + 8 Jetix review subagents Day 11-12
- Compound loop applied к all D1-D8
- Plugin packaging for Phase 2a

**Calendar:** 12-14 days (similar calendar; CE adds hours но saves hours
on review phases).

**Risks:**
- Learning curve: Ruslan unfamiliar с skill authoring best practices
  ([R-8 §6.3](./R-8-skills-claudemd-knowledge.md) skill description tuning)
- Process overhead on decision-heavy documents (D2, D4, D7)
- CE plugin = 50+ agents; possible context budget overflow (per [R-8 §6.5](./R-8-skills-claudemd-knowledge.md)
  Compound Engineering plugin 316% overflow) — must test + monitor

**Recommendation: PARTIAL REJECT.** Full adoption overcommits без proven
benefit on decision-heavy docs.

### 7.3 Option C: Hybrid (recommended)

**What happens:**

**Phase 1 Day 1-9 (unchanged):** Sales infrastructure + foundation per current
plan.

**Phase 1 Day 10-11: Tooling migration.**
- Day 10 morning: Convert /ingest /ask /lint к native Skills (4-6h)
- Day 10 afternoon: Add 3-4 PostToolUse hooks (2-3h)
- Day 11 morning: Shrink root CLAUDE.md к <100 lines; move к `.claude/rules/*.md` (2-3h)
- Day 11 afternoon: Install Compound Engineering plugin; fork DACH variants (3-5h)

**Phase 1 Day 12: Jetix review subagents.**
- Create 8 review subagents (jetix-dsgvo-reviewer, jetix-ai-act-reviewer,
  jetix-fpf-alignment-reviewer, jetix-fgr-tagging-reviewer, jetix-multiview-
  reviewer, jetix-boundary-discipline-reviewer, jetix-hgb-finance-reviewer,
  jetix-ustg-invoice-reviewer)
- ~4-6h

**Phase 1 Day 13-17: CE-augmented writing.**
- D1 Architecture Final: plan → write → `/ce-code-review` (3-reviewer fan-out
  — FPF-alignment, clarity, completeness) → compound к strategies.md
- D3 Role Manifests (18): parallel batch; 3-reviewer fan-out per role;
  **EXTENDED v2: encode loop variant + maxTurns + termination stack per
  A14/A15 in YAML (~20 min per manifest = 6h total)**
- D5 Knowledge Architecture: full CE loop (methodology-heavy)
- D6 pass 3 (remaining): 12-reviewer fan-out at pass 2→3 transition
- D8 Instructions: CE loop (runnability, timeline-realism, dependencies)

**Phase 1 Day 13-17 (parallel):** Traditional Variant A for decision-heavy:
- D2 Folder Structure: single-pass (mostly done)
- D4 Life-OS vs Jetix: single-pass (decisions made in ADR)
- D7 Career Levels: single-pass (matrix already drafted)

**v2 ADDITIONS (Day 12-17, ~12-18h):**

**Day 12 afternoon (4-6h): Memory tool integration (A12 + A13).**
- 2-3h: Adopt Anthropic memory tool (beta) for sales-research, sales-outreach,
  inbox-processor (client-data agents); verify ZDR config; test Article 17
  deletion end-to-end
- 2-3h: Migrate per-agent strategies.md → SKILL.md format с YAML frontmatter
  + ACE structured entries (template + 11 agents × ~15 min each)

**Day 14 morning (4-6h): Eval framework setup (A9, D10).**
- 1h: Install Promptfoo CLI; sign up Langfuse Hobby cloud (or self-host
  Docker Compose); create `evals/<role>/` skeleton per agent
- 4h: Pilot agent = sales-researcher; hand-grade 30 examples; build first
  LLM-judge с Hamel Critique Shadowing; calibrate; GitHub Action PR gate
- 1h: Document Hamel 6-step workflow в `_meta/eval-discipline.md`

**Day 14-17 (parallel + ongoing): Agentic loop pattern adoption (A14, A15,
A16, D11).**
- 2-4h: Encode 4-layer termination stack (maxTurns + taskBudget + completion
  predicate + escalation trigger) in 11 role-manifests YAML; integrates с
  D3 task above
- 1h: Update CLAUDE.md с per-department loop variant table reference
- 1h: Update message schema (mailboxes) к require full traces, не summaries
  (Walden Yan Principle 1)
- 1-2h: Enable extended thinking on strategy-support-analyst, knowledge-synth,
  meta-agent FPF-Steward sub-role

**Estimated calendar: 14-16 days** (was 13-15 в v1; +1-2 days net for
v2 additions, but high-ROI).

**Post-Phase-1 (Day 18+):** `/close-day` skill enhancement с jonathanmalkin
4-phase pattern; append к `strategies.md` becomes habitual; **eval suite runs
weekly per agent с golden-set regression check; FPF-Steward quarterly audit
includes eval-attributable compound learning delta** (R-11 §8.4).

**Why Option C:**
1. CE benefits concentrated on methodology-heavy docs (D1, D3, D5, D6, D8)
2. Decision-heavy docs (D2, D4, D7) unaffected — no process tax
3. Skills + plugin migration gives Jetix cross-tool future-proofing
4. Compound Engineering plugin adoption = production-validated pattern
5. Fork к DACH variants gives Jetix unique moat
6. **(v2) Eval infrastructure (A9-A11) fills v1 G4/G8 gap → quality compounds
   from Day 14**
7. **(v2) Memory tool (A12) gives GDPR-compliant Berlin-ready architecture
   from Day 12**
8. **(v2) Agentic loop variants (A14-A16) optimize cost/quality per agent
   type — addresses R-9 15× multi-agent token cost governing constraint**
9. **(v2) ACE/SKILL.md migration (A13) future-proofs toward Anthropic open
   standard и preserves +10.6% accuracy gain**

**Risks + mitigations:**
- Compound Engineering plugin 316% budget overflow risk → monitor
  `<available_skills>` at install; test budget usage
- Learning curve skill authoring → use `skill-creator` meta-skill from
  anthropics/skills repo; ~2h self-study
- Review subagent sycophancy (R-4 §2.3) → use heterogeneous models
  (some Haiku 4.5, some Sonnet) to break sycophancy correlation; **PoLL
  ensemble pattern (AD8) для high-stakes Audit SKU**
- **(v2) Eval framework calibration overhead** → start с pilot (sales-
  researcher only); Hamel "15-minute" budget per agent dataset; iterative
  judge tuning (Honeycomb 30% gain in 3 iterations)
- **(v2) Anthropic memory tool beta status** → API may evolve; mitigation
  = wiki/ remains source of truth, memory tool augmentation only
- **(v2) "Desperate Claude" near-budget silent quality degradation 20-44%**
  → phrase budgets в prose, не `max_tokens` cap; Task Budgets API header
  с countdown

---

## Part 8 — Open questions для дальнейшего research

**OQ1. How к measure Jetix's "compound effect" longitudinally?**
- Why important: CE literature lacks longitudinal compounding curves
  (R-1 §6.4). Jetix could contribute first public measurement.
- How к answer: Define metric (e.g., tokens-to-first-draft per comparable
  document type) over 3 months; track from Day 1. Comparable to
  Cursor Tab online RL metrics ([R-3 §5.1 Case 1](./R-3-self-improving-systems.md)).
- Effort: 2h metric design + 5 min/week telemetry collection.

**OQ2. Does Jetix's FPF ontology survive when agents cannot strategize?**
- Why important: Levenchuk critique ([R-3 §6.2](./R-3-self-improving-systems.md)) — agents execute
  functions не methods. Jetix's FPF requires ontological reasoning; agents
  cannot produce ontological reasoning. Therefore **Ruslan is critical
  path** for all ontological updates.
- How к answer: Phase 2a test — if first hire can maintain FPF discipline,
  critique partially refuted. If only Ruslan can, Phase 2b FPF-Steward
  as separate role is mandatory.
- Effort: Ongoing observation; formalize Q3 2026.

**OQ3. Does 12-reviewer fan-out produce sycophantic convergence on Jetix
deliverables?**
- Why important: R-4 §2.3 DCR 86.36%; reviewer agents share RLHF tendencies.
- How к answer: After first 5 Audit SKU deliveries, compare 12-reviewer
  findings vs human-only review. If 80%+ overlap and 0 dissents, sycophancy
  failure confirmed.
- Effort: ~4h analysis after first 5 deliveries.

**OQ4. Is Every's AGENTS.md cross-tool pattern adopted в DACH enterprises?**
- Why important: If DACH Mittelstand clients also use Cursor/Codex CLI,
  Jetix's cross-tool Skills/AGENTS.md adoption = interop advantage.
- How к answer: Ask first 3 clients; log responses.
- Effort: 30 min per client interview; aggregate after 3 engagements.

**OQ5. Should Jetix contribute к ailev/FPF upstream community?**
- Current stance: Internal-only hard per OQ-09 A (D6 §0).
- Why important: Contribute-back accelerates community + positions Jetix
  as thought-leader vs. silent operator.
- How к answer: Semi-annual FPF sync reminder (per D9 Deferred/triggered).
  Ruslan decision Q2 close 2026.
- Effort: 0 Phase 1; ~10h Q2 2026 review.

**OQ6. Can sub-agents survive Claude 4.8 → Claude 5 migration?**
- Why important: Boris "sub-agents may be deprecated" ([R-7 §5.1](./R-7-boris-cherny-claude-code.md)). If
  5.x handles context across task boundaries, Jetix's 11-agent investment
  может become obsolete.
- How к answer: Test first 5.x release with Jetix stack. Measure whether
  context isolation still needed.
- Effort: 1-2 days when Claude 5 ships.

**OQ7. Is the Compound Engineering plugin's 316% budget overflow fixed in v2.31.0+?**
- Why important: Installing plugin without verification risks context budget
  issues ([R-8 §6.5](./R-8-skills-claudemd-knowledge.md)).
- How к answer: Install, monitor `<available_skills>` budget, compare
  pre/post measurements.
- Effort: 1h Day 11.

**OQ8. Should Jetix adopt Constitutional Classifiers runtime gate?**
- Why important: Anthropic's Feb 2025 Constitutional Classifiers reduce
  jailbreak rate 86% → 4.4% ([R-3 §2.3](./R-3-self-improving-systems.md)). For Jetix processing client data,
  this is relevant.
- How к answer: Investigate whether Constitutional Classifiers available к
  subscription users или only enterprise API. Cost-benefit if available.
- Effort: Research 2h.

**OQ9. What is Jetix's specific answer к Levenchuk's "agents cannot strategize"?**
- Why important: If Jetix claim "AI-native DACH consultancy" к DACH clients,
  must explain why agents' limitation doesn't undermine deliverable quality.
- How к answer: D6 §5.1-5.5 makes case implicitly; needs explicit client-
  facing answer. Use as part of Multi-View Publication Executive viewpoint.
- Effort: 2-3h drafting; iterate based on first 3 client engagements.

**OQ10. Is the Anthropic Skills open standard (agentskills.io Dec 2025)
going к remain stable or fork?**
- Why important: Jetix bet on Skills format requires standard stability.
- How к answer: Monitor ecosystem (Cursor, Codex CLI, Gemini CLI adherence).
- Effort: Monthly check 15 min.

**OQ11. Is Mem0/Letta/Zep API stability mainstream Phase 2a-ready?**
- Why important: D9 hybrid recommends Phase 2 trial Letta sleep-time на ONE
  agent + Zep Flex selectively; vendor failure risk (Zep Community Edition
  deprecated April 2025, [R-10 §Recommendation §5](./R-10-continual-learning.md)).
- How к answer: Quarterly check vendor changelog; preserve wiki/ as fallback
  regardless; prefer Apache 2.0 OSS (Mem0/Letta/Cognee) over hosted.
- Effort: Quarterly 30 min vendor health check.

**OQ12. Best LLM-as-judge anti-bias mitigation для FPF compliance evaluation?**
- Why important: R-11 §4 documents domain-expertise ceiling (judge agreement
  drops к 64-68% on expert tasks per Krumdick et al.); FPF is niche framework
  requiring deep ontological understanding; only mitigations suggested =
  expert-written reference answers + HITL hybrid.
- How к answer: First 10 D-doc evaluations — measure judge κ vs Ruslan; if
  κ < 0.6, expand reference answer corpus + reduce single-judge scope; consider
  PoLL ensemble (3 diverse models)
- Effort: 2-3h first-cohort calibration + ongoing tuning

**OQ13. Optimal agentic loop iteration limits per agent type?**
- Why important: R-9 §Recommendations gives 5-50 range; specific number
  affects cost/reliability balance; "desperate Claude" failure 20-44% near
  budget exhaustion ([R-9 §5 Q8 ref 86](./R-9-agentic-loop.md)).
- How к answer: Encode v1 recommended values; track per-agent token-per-task
  + completion rate over 30 days; tune per agent quarterly
- Effort: 1h initial encoding + 30 min/month review

**OQ14. Anthropic memory tool beta API stability — Phase 2a production-ready?**
- Why important: R-10 §4.5 documents beta header `context-management-2025-06-27`;
  *"beta status means API surface may change"*; Jetix bets memory tool на
  GDPR-critical client-data agents (A12).
- How к answer: Monitor Anthropic API changelog monthly; subscribe к beta
  deprecation notices; preserve wiki/ fallback path
- Effort: 15 min monthly check; 2-4h migration if breaking change

**OQ15. Sleep-time compute pattern ROI for Jetix workload?**
- Why important: R-10 §2.9 5× compute reduction at equal accuracy WHEN context
  shared across many queries; uncertain whether Jetix's per-agent workload
  has sufficient context-reuse pattern.
- How к answer: Phase 2 trial Letta sleep-time на knowledge-synth (highest
  context-reuse candidate); measure cost-per-task before/after over 30 days
- Effort: 4-6h trial setup + 30 min/week measurement

**OQ16. Should Jetix adopt three-agent harness pattern (Planner→Generator→
Evaluator) для D6/D8 writing in Phase 1 or defer к Phase 2?**
- Why important: R-11 §9 Anthropic harness blog Mar 2026 documents "strong
  lever"; full V2 cycle (Opus 4.6) ~3h 50m at $124.70; cost-significant
  but quality gain measurable.
- How к answer: Phase 1 Day 13-17 trial on D6 pass 3 transition; measure
  Cohen's κ vs Ruslan's solo review; if κ improvement >0.15, adopt for D5/D8
- Effort: 4-6h Day 13-17 trial; ongoing per high-stakes D-doc

**OQ17. Goal drift mitigation cost vs benefit for Jetix?**
- Why important: R-9 §6 Q12 ref 103 — Sonnet 4.5 standard fails goal
  resilience >32 steps; thinking variants pass; extended thinking adds
  ~30-40% cost.
- How к answer: Phase 2 measure strategist + knowledge-synth + meta-agent
  task lengths; if median >32 steps, mandatory extended thinking; if <20
  steps, optional
- Effort: 30 min telemetry analysis monthly

**OQ18. Cross-tool eval portability — should Jetix Promptfoo configs be
reused если migrating tools?**
- Why important: R-11 documents framework lock-in risk (LangSmith outside
  LangChain weak; Promptfoo most portable).
- How к answer: Already using Promptfoo (CLI, MIT); configs are YAML +
  Markdown; portable by design. Document migration path к Braintrust
  Phase 2 как safety check.
- Effort: 1h Phase 2 transition planning

---

## Part 9 — References

### 9.1 Research sources cited

Primary Perplexity research outputs (located in `raw/research/compounding-
engineering-2026-04-22/`):

- **R-1: Compounding Engineering core** (R-1-compounding-engineering-core.md,
  510 lines, 60KB) — canonical CE definition, 6 pattern primitives, tooling
  landscape, case studies, critical assessment
- **R-2: Swarm intelligence** (R-2-swarm-intelligence.md, 736 lines, 96KB) —
  terminological hazard analysis, 5 hybrid production patterns, Rule of 4,
  17.2× error amplification, economics of solo-founder
- **R-3: Self-improving systems** (R-3-self-improving-systems.md, 897 lines,
  104KB) — Karpathy SPL, HITL 5-point spectrum, Cursor Tab RL, GitHub Copilot
  +84% build rate, 10 failure modes, Levenchuk critique
- **R-4: Failure modes + critique** (R-4-failure-modes-critique.md, 616 lines,
  68KB) — Adversarial posture; 5 damaging findings; 8 production failures;
  7 named critics; Anthropic's own cautions
- **R-5: Production case studies** (R-5-production-case-studies.md, 853 lines,
  99KB) — Devin/Cursor/Claude Code/Replit/Lovable/v0/Bolt/Aider/Continue/Sweep
  deep-dive; commercial dynamics; comparison matrix
- **R-6: Every / Cora Compound** (R-6-every-cora-compound.md, 594 lines, 65KB) —
  Every institutional profile, 4-step loop detail, 12-reviewer fan-out,
  production metrics, failure modes, Jetix-specific implications
- **R-7: Boris Cherny + Claude Code design** (R-7-boris-cherny-claude-code.md,
  831 lines, 72KB) — Boris profile + 10 design principles verbatim, CLAUDE.md
  origin, sub-agents/hooks/skills/MCP deep-dive, criticisms + future direction
- **R-8: Skills + CLAUDE.md + knowledge** (R-8-skills-claudemd-knowledge.md,
  1333 lines, 79KB) — 5 first-class primitives, anti-patterns, **Jetix-specific
  migration plan §7** (the most load-bearing content)
- **R-9: Agentic loop mechanics** (R-9-agentic-loop.md, 1362 lines, 112KB)
  — 9 loop variants (ReAct/Reflexion/Plan-and-Execute/ToT/CodeAct/Voyager/
  Self-Refine/Self-Consistency/AutoGPT-style); Anthropic 15× token claim
  verbatim; Boris "thinnest wrapper" doctrine; 8 termination mechanisms +
  Ralph Wiggum problem; 6 anti-patterns; per-department recommendations
  table for Jetix
- **R-10: Continual learning state-of-the-art** (R-10-continual-learning.md,
  1295 lines, 149KB) — Mem0/Letta/Zep/Cognee/Anthropic memory tool deep
  dive; cognitive memory taxonomy (episodic/semantic/procedural/working);
  sleep-time compute pattern; 6 failure modes (poisoning/rot/false consolidation/
  GDPR conflict); **Jetix architecture endorsed verbatim как production
  canonical**
- **R-11: Evals frameworks** (R-11-evals.md, 1295 lines, 117KB) — 14
  frameworks (Anthropic Console/OpenAI Evals/LangSmith/Langfuse/Promptfoo/
  DeepEval/Inspect AI/Braintrust/Humanloop/Helicone/Phoenix/Galileo/Ragas/
  TruLens); LLM-as-judge bias catalog (9 categories); Hamel Critique
  Shadowing 6-step; benchmark saturation crisis (49% saturated); pass^k
  consistency metric; Jetix per-agent eval design tables

### 9.2 Jetix sources cited

- **D6 JETIX-FPF v2** (`design/JETIX-FPF.md`, 3758 lines) — Constitutional
  document; sections cited: §0, §0.5-0.9, §1 (target system + holon),
  §2 (stakeholders + 11 agents + 2.2a coordination), §3 (Creation Graph),
  §4 (client principles, CP-1..CP-5, CP-5 Human Approval Gate, §4.5.1 EU AI
  Act matrix), §5 (internal principles IP-1..IP-8; §5.4 FPF-Steward; §5.4a
  tiered FPF loading; §5.5a in-progress exception), §6 (8 true alphas),
  §12.10 (Bias-Audit BA-0..3)
- **ADR Chunks 1-8** (`decisions/2026-04-19-architecture-v2-approval.md`,
  1995 lines) — Chunk 1 (7 Core Principles), Chunk 2 (Meta-conflicts),
  Chunk 6 (Area 6 D6 decisions, Area 5 D5 Knowledge Architecture), Chunk 8
  (Gap 1-5 additions)
- **D9 Architecture Final Draft** (`decisions/2026-04-20-jetix-architecture-final-DRAFT.md`,
  1880 lines) — §2.1 TL;DR, §3 (8 pillars P1-P8), §5.1-5.4 (15 folders, 8
  alphas, 18 role-manifests, rollout timeline), §5.6 (cost model),
  §5.7 (rituals)
- **Project CLAUDE.md** (`CLAUDE.md`, ~130 lines from context) — 11 agents
  listed, global rules, hub-and-spoke rule #8, Russian for content / English
  for code
- **Agents folder** (`agents/`) — 12 subfolders including `life-coach/`
  (to be migrated к life-os/ per Area 7 decision); each agent has
  `system.md`, `strategies.md`, `scratchpad.md`, `niche/` symlinks,
  `versions/`

### 9.3 External sources mentioned в research

**Anthropic official (~15 top sources):**
- [Building Effective Agents (Schluntz & Zhang, Dec 19, 2024)](https://www.anthropic.com/engineering/building-effective-agents)
- [How we built our multi-agent research system (Hadfield et al., June 13, 2025)](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- [Equipping agents for the real world with Agent Skills (Oct 16, 2025)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Effective context engineering for AI agents (Sept 29, 2025)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Claude Code Best Practices (April 3, 2026)](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Managed Agents (Feb 4, 2026)](https://www.anthropic.com/engineering/managed-agents)
- [Agentic Misalignment (June 19, 2025)](https://www.anthropic.com/research/agentic-misalignment)
- [Constitutional Classifiers (Feb 3, 2025)](https://www.anthropic.com/research/constitutional-classifiers)
- [Constitutional AI paper (Bai et al., arXiv:2212.08073)](https://arxiv.org/abs/2212.08073)
- [Introducing Model Context Protocol (Nov 25, 2024)](https://www.anthropic.com/news/model-context-protocol)
- [Claude Code overview docs](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code memory docs](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Claude Code sub-agents docs](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Claude Code skills docs](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code hooks docs](https://code.claude.com/docs/en/hooks)

**Every / Cora / Shipper (~10 top sources):**
- [Compound Engineering: How Every Codes With Agents (Dec 11, 2025)](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents)
- [Compound Engineering guide (Every, Jan 17, 2026)](https://every.to/guides/compound-engineering)
- [Every Master Plan: Part II (Sept 26, 2025)](https://every.to/on-every/every-s-master-plan-part-ii)
- [EveryInc/compound-engineering-plugin GitHub](https://github.com/EveryInc/compound-engineering-plugin)
- [AI Engineer talk — Dan Shipper (Dec 18, 2025)](https://www.youtube.com/watch?v=MGzymaYBiss)
- [How Two Engineers Ship Like a Team of 15 (AI & I, June 11, 2025)](https://every.to/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents)
- [Cora product page](https://cora.computer)
- [Lenny's Newsletter interview — Dan Shipper (July 17, 2025)](https://www.lennysnewsletter.com/p/inside-every-dan-shipper)
- [How to Use Claude Code Like the People Who Built It — AI & I with Boris Cherny (Oct 29, 2025)](https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it)

**Boris Cherny primary sources (~7):**
- [Latent Space — Claude Code with Boris Cherny (May 2025)](https://www.latent.space/p/claude-code)
- [Lenny's Podcast — Head of Claude Code (Feb 19, 2026)](https://www.youtube.com/watch?v=We7BZVKbCVw)
- [Bessemer Venture Partners — Agentic Coding with Boris Cherny (Aug 18, 2025)](https://www.youtube.com/watch?v=h-Hlt05REZk)
- [Pragmatic Engineer — Building Claude Code with Boris Cherny (Mar 4, 2026)](https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny)
- [Boris's personal blog (borischerny.com)](https://borischerny.com)
- [Boris Cherny @bcherny Twitter/X](https://x.com/bcherny)
- [howborisusesclaudecode.com](https://howborisusesclaudecode.com)

**Critical / Adversarial (~10):**
- [Walden Yan — Don't Build Multi-Agents (Cognition, June 12, 2025)](https://cognition.ai/blog/dont-build-multi-agents)
- [Hamel Husain — Thoughts on Devin (Answer.AI, Jan 8, 2025)](https://www.answer.ai/posts/2025-01-08-devin.html)
- [Kim et al. — Towards a Science of Scaling Agent Systems (arXiv:2512.08296, Dec 2025)](https://arxiv.org/abs/2512.08296)
- [Cemri et al. — MAST taxonomy (arXiv:2503.13657, March 2025)](https://arxiv.org/abs/2503.13657)
- [Willison — The Lethal Trifecta (June 16, 2025)](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- [Willison — How I Use Every Claude Code Feature (Nov 2, 2025)](https://simonwillison.net/2025/Nov/2/how-i-use-every-claude-code-feature/)
- [Kent Beck — Augmented Coding (Tidy First, June 25, 2025)](https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes)
- [Kambhampati — LLMs Can't Plan (ICML 2024)](https://proceedings.mlr.press/v235/kambhampati24a.html)
- [METR — Recent Frontier Models Are Reward Hacking (June 2025)](https://metr.org/blog/2025-06-05-recent-reward-hacking/)
- [Aim Security — EchoLeak CVE-2025-32711 (arXiv:2509.10540, Sept 2025)](https://arxiv.org/abs/2509.10540)

**Levenchuk primary sources:**
- [FPF GitHub repository](https://github.com/ailev/FPF)
- [Методология 2025 (ISBN 978-5-0064-8619-5)](https://flibusta.su/book/358645-metodologia-2025/read/)
- [Системное мышление 2024, Vol. 1](https://www.litres.ru/book/anatoliy-levenchuk/sistemnoe-myshlenie-2024-tom-1-70915630/)
- [ailev.livejournal.com](https://ailev.livejournal.com/)
- [FPF Codex Harness post (Apr 5, 2026)](https://ailev.livejournal.com/1797223.html)

**Karpathy primary sources (~5):**
- [Software 3.0 / YC keynote (June 18, 2025)](https://www.youtube.com/watch?v=LCEmiRjPEtQ)
- [System Prompt Learning tweet (May 10, 2025)](https://x.com/karpathy/status/1921368644069765486)
- [Context Engineering tweet (June 25, 2025)](https://x.com/karpathy/status/1937902205765607626)
- [2025 LLM Year in Review (Dec 19, 2025)](https://x.com/karpathy/status/2002118205729562949)
- [Intro to LLMs (Nov 22, 2023)](https://www.youtube.com/watch?v=zjkBMFhNj_g)

**Production cases (~10):**
- [Cursor blogs — Series D (Nov 2025)](https://cursor.com/blog/series-d)
- [Cursor Composer / 2.0 (Oct 29, 2025)](https://cursor.com/blog/2-0)
- [Replit Blog — Agent 4 launch](https://blog.replit.com/introducing-agent-4-built-for-creativity)
- [Lovable Series B — TechCrunch Dec 2025](https://techcrunch.com/2025/12/18/vibe-coding-startup-lovable-raises-330m-at-a-6-6b-valuation/)
- [Sacra — Cursor research (2026)](https://sacra.com/c/cursor/)
- [Aider on GitHub](https://github.com/Aider-AI/aider)
- [William Zeng — Sweep shutdown LinkedIn (Dec 2025)](https://www.linkedin.com/posts/william-zeng_2024-we-just-decided-to-shut-down-our-background-activity-7411508506861891584-a7yi)
- [Replit Breakout Agents case study (LangChain)](https://www.langchain.com/breakoutagents/replit)
- [Anthropic internal Claude Code case study PDF](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)
- [The Pragmatic Engineer — How Claude Code is built](https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built)

**Agentic loop sources (R-9, ~10 added):**
- [Yao et al. — ReAct: Synergizing Reasoning and Acting (ICLR 2023, arXiv:2210.03629)](https://arxiv.org/abs/2210.03629)
- [Shinn et al. — Reflexion: Language Agents with Verbal Reinforcement Learning (arXiv:2303.11366)](https://arxiv.org/abs/2303.11366)
- [Wang et al. — Voyager: An Open-Ended Embodied Agent (arXiv:2305.16291)](https://arxiv.org/abs/2305.16291)
- [Yao et al. — Tree of Thoughts (arXiv:2305.10601)](https://arxiv.org/abs/2305.10601)
- [Wang et al. — Executable Code Actions (CodeAct, arXiv:2402.01030)](https://arxiv.org/abs/2402.01030)
- [Madaan et al. — Self-Refine (arXiv:2303.17651)](https://arxiv.org/abs/2303.17651)
- [Anthropic — Building Effective Agents (Dec 2024)](https://www.anthropic.com/engineering/building-effective-agents)
- [Anthropic — How we built our multi-agent research system (June 2025)](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- [Boris Cherny — Latent Space Podcast (May 2025)](https://www.latent.space/p/claude-code)
- [Walden Yan / Cognition — Don't Build Multi-Agents (June 2025)](https://cognition.ai/blog/dont-build-multi-agents)
- [Anthropic — Task Budgets API beta (`task-budgets-2026-03-13`)](https://docs.anthropic.com/en/api/task-budgets)
- [Inherited Goal Drift paper (arXiv:2603.03258, 2026)](https://arxiv.org/abs/2603.03258)
- [SWE-Effi: agent efficiency benchmark (arXiv:2509.09853)](https://arxiv.org/abs/2509.09853)

**Continual learning sources (R-10, ~15 added):**
- [Mem0 paper (arXiv:2504.19413)](https://arxiv.org/abs/2504.19413)
- [Mem0 GitHub (~48k stars)](https://github.com/mem0ai/mem0)
- [Packer et al. — MemGPT: Towards LLMs as Operating Systems (arXiv:2310.08560)](https://arxiv.org/abs/2310.08560)
- [Letta (formerly MemGPT) GitHub](https://github.com/letta-ai/letta)
- [Letta Context Repositories announcement (Feb 2026)](https://www.letta.com/blog/context-repositories)
- [Lin et al. — Sleep-Time Compute (arXiv:2504.13171, April 2025)](https://arxiv.org/abs/2504.13171)
- [Zep / Graphiti GitHub](https://github.com/getzep/zep)
- [Cognee GitHub](https://github.com/topoteretes/cognee)
- [Anthropic — Memory Tool launch (Sept 29, 2025)](https://www.anthropic.com/news/context-management)
- [Anthropic — Effective context engineering for AI agents (Sept 2025)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Wu et al. — LongMemEval (ICLR 2025, arXiv:2410.10813)](https://arxiv.org/abs/2410.10813)
- [Maharana et al. — LoCoMo (ACL 2024)](https://aclanthology.org/2024.acl-long.747/)
- [Karpathy — LLM Wiki tweet (April 2026)](https://x.com/karpathy/)
- [Chen et al. — AgentPoison (arXiv:2407.12784)](https://arxiv.org/abs/2407.12784)
- [Chroma — Context Rot study (2025)](https://research.trychroma.com/context-rot)
- [BAI Lab — MemoryOS (EMNLP 2025 Oral, arXiv:2506.06326)](https://arxiv.org/abs/2506.06326)
- [Xu et al. — A-MEM (NeurIPS 2025, arXiv:2502.12110)](https://arxiv.org/abs/2502.12110)

**Evals sources (R-11, ~15 added):**
- [Zheng et al. — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (NeurIPS 2023, arXiv:2306.05685)](https://arxiv.org/abs/2306.05685)
- [Promptfoo GitHub (8.8k stars)](https://github.com/promptfoo/promptfoo)
- [Langfuse GitHub (21.4k stars)](https://github.com/langfuse/langfuse)
- [Inspect AI GitHub (UK AISI)](https://github.com/UKGovernmentBEIS/inspect_ai)
- [Braintrust](https://www.braintrust.dev/)
- [DeepEval GitHub](https://github.com/confident-ai/deepeval)
- [Phoenix / Arize GitHub](https://github.com/Arize-ai/phoenix)
- [Hamel Husain — Critique Shadowing](https://hamel.dev/blog/posts/llm-judge/)
- [Shreya Shankar — EvalGen (CHI 2024, arXiv:2404.12272)](https://arxiv.org/abs/2404.12272)
- [Eugene Yan — Evaluation & Hallucination Detection for Abstractive Summaries](https://eugeneyan.com/writing/abstractive/)
- [Anthropic — Engineering Blog: Eval Best Practices (Jan 2026)](https://www.anthropic.com/engineering/eval-best-practices)
- [Anthropic — Three-agent harness (Mar 2026)](https://www.anthropic.com/engineering/agent-harness)
- [Sierra — τ-bench (arXiv:2406.12045)](https://arxiv.org/abs/2406.12045)
- [HAL Generalist agent benchmarks](https://hal.cs.princeton.edu/)
- [Krumdick et al. — Domain Expertise Ceiling (2024)](https://arxiv.org/abs/2402.10612)
- [Tripathi et al. — Pairwise Position Bias (arXiv:2504.14716)](https://arxiv.org/abs/2504.14716)
- [Verga et al. — Replacing Judges with Juries (arXiv:2404.18796)](https://arxiv.org/abs/2404.18796)
- [Dorner et al. — Limits of LLM-as-judge at frontier (arXiv:2410.13341)](https://arxiv.org/abs/2410.13341)

---

## Appendix A — Glossary

| Term | Definition | Which framework |
|------|-----------|-----------------|
| **Agent** | LLM that can use tools (Boris's technical definition, [R-7 §2.1](./R-7-boris-cherny-claude-code.md)) | CE/Swarm/Jetix |
| **Alpha** | Thing с past-participle state machine (Client, Project, Deal, etc.) | Jetix (from Levenchuk/SEMAT) |
| **Agency-CHR** | Formal 0.0-1.0 agency scale per decision class in executor-binding.yaml (D6 §2.1a) | Jetix innovation (grounded FPF A.13:4.3) |
| **Bitter Lesson** | Rich Sutton's observation: more general model outperforms specific (Boris invokes as product strategy) | Claude Code / CE |
| **CLAUDE.md** | Markdown file auto-loaded at every session start; hierarchical precedence (enterprise/personal/project/local) | Claude Code |
| **Compound Engineering (CE)** | Plan → Work → Review → Compound loop; Every's canonical formulation | Every / Shipper |
| **Compound step ("money step")** | 4th step: document learnings, update CLAUDE.md, create agents, verify catch-ability | CE |
| **Creation Graph** | 3-level mereological graph showing target systems / creation systems / supersystems (D6 §3) | Jetix (from FPF) |
| **Direction (Portfolio of Directions)** | Revenue bet с own hypothesis, kill criteria, lifecycle — 8th alpha | Jetix innovation |
| **F-G-R tagging** | Formality (F0-F9) / claim-Scope (G) / Reliability (R-low-to-certified) trust triad | Jetix (from FPF B.3) |
| **FPF (First Principles Framework)** | Levenchuk's 62k-line pattern language (github.com/ailev/FPF) | Levenchuk upstream |
| **Holon** | Whole-and-part simultaneously (Koestler 1967) | Jetix / FPF |
| **Hooks** | Deterministic shell/HTTP/prompt/agent handlers at lifecycle points (27+ events) | Claude Code |
| **J-level** | J-Auto / J-Approve / J-Strategic authority tier per role | Jetix (from D7) |
| **Lethal Trifecta** | Private data + untrusted content + external communication = exfiltration (Willison) | Swarm / critical |
| **Mama Claude / Baby Claude** | Main process + spawned sub-agents (Boris's affectionate naming) | Claude Code |
| **MAST (Multi-Agent System failure Taxonomy)** | 14 failure modes across 3 categories (Cemri et al. arXiv:2503.13657) | Adversarial research |
| **MCP (Model Context Protocol)** | JSON-RPC protocol for tools/resources/prompts (Anthropic Nov 2024, 100M monthly downloads by April 2026) | Cross-framework standard |
| **Multi-View Publication** | 5-viewpoint (Exec/Tech/Governance/Regulatory/Internal-learning) delivery kit | Jetix (from FPF E.17) |
| **Past-participle state** | `qualified`, `activated`, `delivered` — not gerunds; Левенчук discipline | Jetix (from Levenchuk) |
| **Plan Mode** | Claude Code read-only mode before execution (Shift+Tab to enter) | Claude Code |
| **Replaceable agents principle** | Stateless agent invocations; 1,000 Claudes fixing 1,000 Lint errors | Boris Cherny |
| **Role ≠ Executor** | Role = archetype (obligations); Executor = binding (who holds it); never mixed | Jetix (IP-1, from FPF A.2) |
| **Rule of 4** | Effective multi-agent team size peaks at 3-4 agents (Kim et al.) | Adversarial research |
| **Skills (Agent Skills)** | Progressive disclosure 3-level: metadata → body → files; open standard Dec 18, 2025 | Claude Code / cross-tool |
| **SPL (System Prompt Learning)** | Karpathy's proposed 3rd paradigm of LLM learning; edits not gradient descent | Karpathy |
| **Stigmergy** | Agents coordinate through shared environment modification (ant pheromones) | Classical / R-2 framing |
| **Subagent** | Separate instance of Claude with isolated context; cannot spawn own subagents | Claude Code |
| **U.Type** | "Universal kind" kernel concept (U.Role, U.System, U.Episteme, U.Holon) | Jetix (from FPF) |
| **Way of Working (WoW)** | Meta-alpha: methodology itself as tracked object с state machine | Jetix alpha 7 (from SEMAT) |
| **A-MEM** | Zettelkasten-style linked notes for LLM memory; new note generates description/keywords/tags/dynamic links; ~1,200 tokens/op (NeurIPS 2025) | R-10 |
| **ACE (Agentic Context Engineering, Stanford)** | Append-only structured entries с unique IDs + Helpful/Harmful counters; +10.6% accuracy vs summarization | R-3 §6.1.6 |
| **Agentic loop** | Fundamental while-loop primitive: LLM observes → reasons → emits tool call → observes result → repeats until stop condition (Anthropic) | R-9 |
| **AgentPoison** | Memory-poisoning attack vector; ≥80% attack success rate at <0.1% corpus contamination (arXiv:2407.12784) | R-10 §5.2 |
| **Anthropic memory tool** | File-based primitive с 6 commands (view/create/str_replace/insert/delete/rename); ZDR-eligible; Sept 29 2025 launch; 39% agentic search improvement | R-10 §4.5 |
| **Bitemporal modelling** | Every edge carries event time T + ingestion time T' + validity window valid_from/valid_to/invalid_at; Zep/Graphiti pattern | R-10 §4.3 |
| **Braintrust** | Hosted SaaS unified eval+observability; $80M Series B Feb 2026; Brainstore 86× faster | R-11 §2 |
| **CodeAct** | Action format emitting executable Python instead of JSON tool calls; +20.7% absolute с GPT-4 vs JSON; sandbox-escape risk | R-9 §3 Q4 |
| **Cognee** | Ontology-driven KG engine с ECL pipeline (Extract/Cognify/Load) и self-improving memify loop | R-10 §4.4 |
| **Compaction** | Summarising conversations approaching context limit и reinitiating с summary; over-aggressive use explodes turns 4.0→14.0 | R-9 §5 Q9 |
| **Context engineering** | Anthropic 2025: *"the set of strategies for curating and maintaining the optimal set of tokens during LLM inference"* | R-10 §1.2 |
| **Context Repositories** | Letta Feb 2026: memory projected into git repo as plain files; sleep-time agents reorganise during idle; SKILL.md for skills | R-10 §8.2 |
| **Context rot** | Measurable quality degradation as context grows below max limit; affects all 18 frontier models tested (Chroma 2025) | R-10 §5.2 |
| **Continual learning** | Accumulation/retrieval of external state across context boundaries; "continual learning in token space" (Letta) — agent (θ frozen, C evolving) | R-10 §1.2 |
| **Critique Shadowing** | Hamel Husain 6-step LLM-judge workflow: domain expert → ~30 examples → binary pass/fail+critique → fix → build judge iteratively → periodic analysis | R-11 §4 |
| **Criteria drift** | Shankar's insight that eval criteria cannot be specified before seeing real outputs; some criteria emerge from observing model behavior | R-11 §4 |
| **Desperate Claude** | Internal activation pattern fires near token-budget exhaustion causing silent quality degradation 20-44% of time | R-9 §5 Q8 |
| **Episodic memory** | Stores individual interaction events (timestamped observations, conversation turns) in external DB | R-10 §1.4 |
| **Eval gaming / Goodhart's Law** | When measure becomes target, ceases к be good measure; 49% of major benchmarks saturated | R-11 §3, §7 |
| **EvalGen** | Shankar's criteria-generation system; 0.73 recall on product defects vs SPADE baseline 0.49 | R-11 §4 |
| **Goal drift** | Long-horizon failure mode; Sonnet-4.5 standard fails recognition of new goal в 32-step experiments; thinking variants pass | R-9 §6 Q12 |
| **Graphiti** | Apache 2.0 temporally-aware knowledge graph engine powering Zep; bitemporal model | R-10 §4.3 |
| **Inspect AI** | UK AISI government-grade eval framework; declarative Task/Solver/Scorer; sandboxed Docker/K8s | R-11 §2 |
| **LangSmith** | LangChain hosted eval+observability platform; hierarchical Run tree for trajectories | R-11 §2 |
| **Langfuse** | OSS + hosted, MIT, EU-friendly observability/eval; 21.4k stars; Anthropic-endorsed self-hosted alternative | R-11 §2 |
| **Letta (formerly MemGPT)** | OS-style stateful agent platform; tiered memory (core/archival/recall) + sleep-time agents для async consolidation | R-10 §4.2 |
| **LLM-as-judge** | Using capable LLM к evaluate outputs against rubric; Zheng et al. 85-87% agreement с humans | R-11 §4 |
| **LongMemEval** | Wu et al. ICLR 2025 benchmark; current SOTA Supermemory 85.4% (self-reported); independent Zep 63.8% / Mem0 49.0% | R-10 §6.1 |
| **Mem0** | Vector+graph hybrid memory layer; LLM-driven extraction loop; ~48k stars; $24M Series A YC Oct 2025 | R-10 §4.1 |
| **MemoryOS** | OS-inspired 3-tier hierarchy с 4 modules (Storage/Updating/Retrieval/Generation); EMNLP 2025 Oral | R-10 §4.7 |
| **Pairwise comparison** | Eval pattern where two outputs compared head-to-head; foundational к Chatbot Arena; requires position swap | R-11 §1.3 |
| **pass^k** | Reliability metric measuring task success across k repeated trials с same input; from Sierra τ-bench; GPT-4o ~60% pass^1 → ~25% pass^8 | R-11 §3, §6 |
| **Plan-and-Execute** | Two-phase architecture: large planner creates upfront plan; smaller executor runs sub-tasks; replanner if executor fails | R-9 §3 Q4 |
| **PoLL (Panel of LLM judges)** | Verga et al. ensemble of 3 diverse smaller models; outperforms GPT-4 alone at 1/7 cost | R-11 §4 |
| **Procedural memory** | Reusable executable behaviours/skills; Voyager skill library is canonical; Jetix strategies.md is markdown analog | R-10 §1.4 |
| **Promptfoo** | OSS CLI eval framework, MIT, dev-centric; first-class trajectory assertions; 100% local; **R-11 top recommendation для Jetix Phase 1** | R-11 §2 |
| **Ralph Wiggum problem** | Premature completion: agent declares 100% done at 80% complete; *"rooted in architecture, not the language"* | R-9 §5 Q8 |
| **ReAct** | Yao et al. ICLR 2023 — interleaved Thought→Action→Observation loop; Â=A∪L augmented action space; de-facto default for production agents | R-9 §1 Q1, §3 Q4 |
| **Reflexion** | Trial→Evaluate→Verbal Self-Reflection→retry pattern; three-model setup (Actor/Evaluator/Self-Reflection); 91% Pass@1 HumanEval; fails after 4 trials | R-9 §3 Q4 |
| **Self-Refine** | Generate→Feedback→Refine с same model; effective for open-ended generation; fails on math (94% feedback says "looks good") | R-9 §3 Q4 |
| **Semantic memory** | Extracted facts organised в structured relational form (knowledge graphs); GraphRAG, HippoRAG canonical | R-10 §1.4 |
| **Skills (Anthropic Agent Skills standard)** | Apache 2.0 Dec 2025 open standard; SKILL.md с YAML frontmatter и progressive disclosure | R-10 §8.1 |
| **Sleep-time compute / sleep-time agents** | Asynchronous inference during agent idle periods; ~5× compute reduction at equal accuracy; Lin et al. April 2025 | R-10 §2.9, §4.6 |
| **sqlite-vec** | Mozilla-sponsored Apache 2.0 SQLite extension; zero-server semantic indexing; **R-10 top recommendation для Jetix Phase 2** | R-10 §7.1 |
| **System Prompt Learning (SPL)** | Karpathy's third paradigm of LLM learning; building explicit problem-solving strategies в system prompt from accumulated experience | R-3, R-10 §7.2 |
| **Task Budgets API** | Anthropic header `task-budgets-2026-03-13`; injects countdown server-side; Claude self-regulates; risks "desperate" silent quality degradation | R-9 §5 Q8 |
| **Three-agent harness** | Anthropic Planner→Generator→Evaluator pattern; *"Out of the box, Claude is a poor QA agent"* | R-11 §9 |
| **Tree-of-Thoughts (ToT)** | Branching search (BFS/DFS) over candidate "thought" continuations; LLM-as-evaluator prunes; cost O(b^d) exponential | R-9 §3 Q4 |
| **Trajectory match modes** | strict / unordered / subset / superset (LangSmith agentevals); for evaluating agent tool sequences | R-11 §5 |
| **Voyager** | Open-ended embodied agent с automatic curriculum + code-skill generation + persistent skill library (named JS functions с docstrings) | R-9 §3 Q4 |
| **Working memory** | Live context window в single inference call; brutally finite even at 200K tokens | R-10 §3.3 |
| **ZDR (Zero Data Retention)** | Anthropic-eligible config that does не retain data on Anthropic servers; only Anthropic Memory Tool ZDR-compatible among memory options | R-10 §4.5 |
| **Zep** | Managed memory layer using Graphiti as engine; bitemporal KG; CE deprecated April 2025; only Cloud Flex remains | R-10 §4.3 |

---

## Appendix B — Citation discipline statement

**How citations work in this document:**

1. **Research-source citations** use format `[R-N §X](./R-N-<slug>.md)` pointing
   к specific sections of the 8 Perplexity research outputs in
   `raw/research/compounding-engineering-2026-04-22/`.

2. **Jetix-internal citations** use format `[D6 §X](./../../design/JETIX-FPF.md)`
   pointing к constitutional document, ADR (`[ADR Chunk N](./../../decisions/2026-04-19-architecture-v2-approval.md)`),
   or D9 (`[D9 §X](./../../decisions/2026-04-20-jetix-architecture-final-DRAFT.md)`).

3. **External web citations** are inline Markdown links к original sources
   (Anthropic blogs, arXiv papers, Every essays, etc.).

4. **Verbatim quotes** wrapped in `> «Russian quote»` or `> "English quote"`
   с translation when appropriate.

5. **Claims require citation.** Any assertion about CE practice, production
   metric, or named practitioner traces к R-N source. Any assertion about
   Jetix architecture traces к D6/D9/ADR.

6. **Where evidence was thin** (e.g., unverifiable company-reported metrics),
   explicitly marked "self-reported, uncorroborated" or "company-reported"
   (e.g., Cora adoption metrics per [R-6 §6 Q13](./R-6-every-cora-compound.md)).

7. **Contradictions between sources** resolved explicitly in [§2.2](#22-contradictions-between-reports).
   Where resolution required synthesis judgment, this is noted.

8. **Recommendations carry confidence level** (Part 6 Decision Matrix):
   High / Medium-high / Medium / Low. Higher confidence = stronger
   multi-source convergence.

---

*Document completed 2026-04-21 (v1) и updated 2026-04-21 (v2). 9 Parts +
2 Appendices. v1 was ~14,500 words / 2243 lines / 137KB; v2 adds ~10,000
words from R-9/R-10/R-11 integration. Citations: 150+ across R-1…R-11;
30+ across Jetix internal docs; 90+ external web sources (incl. ~45 new
in v2). Verifier subagent review pending v2.*
