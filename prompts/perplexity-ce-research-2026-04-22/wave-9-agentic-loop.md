---
type: perplexity-research-prompt
wave: 9
topic: Agentic Loop — internal mechanics, variants (ReAct/Reflexion/CodeAct), production implementations
created: 2026-04-21
target: Perplexity Pro Search (Comet desktop or web)
estimated-perplexity-time: 5-15 min
output-target: raw/research/compounding-engineering-2026-04-22/R-9-agentic-loop.md
---

# Perplexity Prompt — Wave 9: Agentic Loop deep dive

## Instructions для Ruslan (НЕ для Perplexity)

1. Откройте Perplexity (Comet desktop или Pro web — https://perplexity.ai)
2. Включите **Pro Search mode** (deep research, НЕ Quick Search)
3. Скопируйте всё ниже разделителя `═══` в Perplexity (включая `# Role + Context` и ниже)
4. Дождитесь completion (5-15 min)
5. Optional: задайте 2-3 follow-up questions (см. ниже) для probing depth
6. Сохраните output в `raw/research/compounding-engineering-2026-04-22/R-9-agentic-loop.md`

## Recommended follow-up questions (после initial answer)

1. "Show me a step-by-step trace of one ReAct iteration с actual tool calls — real
   transcript from a production system, не pseudocode."
2. "What's the simplest possible agentic loop I can implement в Claude Code as a
   solo founder? Minimal viable loop, concrete code/config."
3. "Where do most production agentic loops break down — specific failure cases with
   post-mortems or published traces?"

═══════════════════════════════════════════════════════════════════
THE PROMPT (copy below this line into Perplexity)
═══════════════════════════════════════════════════════════════════

# Role + Context

You are a senior research analyst conducting deep technical due diligence on the
**agentic loop** — the canonical execution cycle used by LLM-based agents — for a
Berlin-based AI consultancy (Jetix) building a multi-agent operational system
(currently 11 Claude-based agents across 6 departments). The output will be used to
make a critical architecture decision: **should Jetix's 11-agent architecture adopt
specific agentic loop patterns (ReAct / Reflexion / Plan-and-Execute / CodeAct /
Tree-of-Thoughts / Voyager) and which specifically, with what termination conditions
and what coordination model between agents?**

This is **deep research**, not a summary. Depth > breadth. Specific > vague.
Multi-source > single-source. Recent (2024-2026) > older. Verbatim quotes and
concrete traces strongly preferred over paraphrase.

# Research Questions (answer ALL, in order, with specifics)

1. **Canonical definition(s) of "agentic loop".** Enumerate definitions from the
   most authoritative sources: Anthropic (Claude Code / Anthropic engineering blog),
   OpenAI (function-calling / Assistants API docs), LangGraph / LangChain, the
   ReAct paper (Yao et al. 2022 — arXiv:2210.03629), and recent 2024-2026 sources
   (AI Engineer Summit talks, Dwarkesh interviews, Latent Space episodes). Cite each
   with URL.
2. **Core internal concepts.** How exactly is the observe → think → act → reflect
   cycle implemented? Which parts live в the LLM prompt vs в harness/scaffolding?
   Name the concrete artifacts (system prompt, scratchpad, tool schema, observation
   channel, stop conditions).
3. **Tool-use cycle внутри agentic loop.** Invocation mechanics, argument
   validation, error handling, retry patterns. How do Claude / OpenAI / Gemini
   function-calling implementations differ structurally? Which patterns do
   practitioners recommend для robustness (e.g., schema validation, idempotency,
   dry-run tools)?
4. **Loop variants — head-to-head comparison.** Describe mechanics of each, then
   compare when to use which:
   - **ReAct** (Yao et al. 2022) — interleaved reasoning+action
   - **Reflexion** (Shinn et al. 2023) — self-critique + retry
   - **Plan-and-Execute** (LangChain/LangGraph) — upfront plan, then execute
   - **Tree-of-Thoughts** (Yao et al. 2023) — branching search
   - **CodeAct** (Wang et al. 2024) — code as action space
   - **Voyager** (Wang et al. 2023) — skill library accumulation
   - **Self-Refine** / **Self-Consistency** / **AutoGPT-style** — if relevant
   For each: original paper URL, production adoption, empirical strengths/weaknesses.
5. **Claude Code's agentic loop — internal mechanics.** How does Claude Code's
   main-session loop actually work? Sub-agent spawning via Task tool, tool-use
   cycle, message-passing between main and sub-agents, context inheritance, result
   returning. Find Anthropic's published descriptions (Boris Cherny talks/tweets,
   Anthropic engineering blog, Claude Code docs) and quote verbatim where possible.
6. **Devin's agentic loop architecture (Cognition Labs).** Published descriptions
   of Devin's loop: planning phase, execution phase, self-correction, sandbox
   integration. Cite Cognition blog posts, Scott Wu/Steven Hao interviews, benchmark
   reports.
7. **Cursor / Cline / Continue / Aider — loop designs.** For each:
   - Loop architecture (single-turn, multi-turn, agent mode)
   - How planning is separated from execution (if at all)
   - Tool invocation model (apply-diff, file-edit, shell)
   - Differences from Claude Code's loop
8. **Termination conditions.** How do production systems avoid infinite loops?
   Concrete mechanisms: max iterations, token budget, convergence detection
   (unchanged scratchpad), LLM-self-declared completion, external judge, timeout.
   Which work в practice? Failure cases where termination broke.
9. **Common patterns inside the loop.** Parallel tool calls (how Claude/OpenAI
   implement), sub-agent spawning, memory writeback between iterations, deferred
   tool discovery, observation → action timing (sync vs async), context compaction
   mid-loop.
10. **Anti-patterns.** Tool-call storms, hallucinated tool arguments, context
    exhaustion, infinite self-reflection ("doom loops"), premature completion,
    tool-use amnesia. Name concrete cases from published traces, tweets, or
    post-mortems.
11. **Cost dynamics.** Tokens per iteration, total iterations to task completion —
    comparisons across Claude Sonnet / Opus / Haiku / GPT-4o / Gemini 1.5/2.0
    where data exists. Anthropic's own "~15× tokens for multi-agent" figure as an
    anchor. How cost scales with loop depth and branching factor.
12. **Latest research papers 2024-2026 on agentic loop optimization.** Top 5-10
    papers with URL + key contribution. Candidates: Reflexion, Voyager, AutoGen,
    MetaGPT, SWE-agent, OpenHands, Magentic-One, WebArena evaluations, AgentBench,
    etc. Distinguish empirical wins vs theoretical.
13. **Multi-agent loops — coordination mechanics.** How does the loop differ when
    multiple agents coordinate vs single agent? Shared scratchpad? Blackboard?
    Message-passing? Sub-agent result aggregation? How are conflicts resolved?
    Published multi-agent loop architectures (AutoGen, CrewAI, MetaGPT,
    Magentic-One, Anthropic's multi-agent research).
14. **Anthropic-specific best practices для Claude Code agentic loop design.**
    Official recommendations from Anthropic docs, Boris Cherny, the Claude Code
    team. Concrete: how to structure CLAUDE.md для loops, when to use sub-agents,
    when to use skills vs tools, how to handle long-running tasks.
15. **Quality metrics.** How do practitioners measure the quality of an agentic
    loop? Task completion rate, iterations-to-convergence, tool-call efficiency,
    cost-per-task, trajectory correctness, partial-credit scoring. Which metrics
    correlate с real user value vs gaming?

# Required Output Format

Structure your response as a **structured markdown report** with these sections:

## Executive Summary (300-500 words)

Synthesis answering: what is the agentic loop, which variants matter, which does
Claude Code use, should a Berlin AI consultancy with 11 agents adopt a specific
variant? Top 5 key findings as a bullet list.

## Section 1 — Canonical Definitions & Core Concepts

Answer Q1, Q2. Definitions from Anthropic, OpenAI, LangGraph, ReAct paper, 2024-2026
sources. Core internal cycle mechanics.

## Section 2 — Tool-Use Cycle Mechanics

Answer Q3. Invocation, validation, retry, error handling. Claude/OpenAI/Gemini
differences.

## Section 3 — Loop Variants Comparison

Answer Q4. ReAct vs Reflexion vs Plan-and-Execute vs ToT vs CodeAct vs Voyager.
Side-by-side table + narrative. When to use which.

## Section 4 — Production Implementations

Answer Q5, Q6, Q7. Claude Code / Devin / Cursor / Cline / Continue / Aider. Loop
architectures, concrete mechanics, differences.

## Section 5 — Termination, Patterns, Anti-patterns

Answer Q8, Q9, Q10. Termination conditions. Common patterns. Anti-patterns с named
cases.

## Section 6 — Economics & Research Frontier

Answer Q11, Q12. Cost dynamics across models. Latest papers 2024-2026 (top 5-10).

## Section 7 — Multi-Agent Loops & Best Practices

Answer Q13, Q14, Q15. Multi-agent coordination mechanics. Anthropic best practices.
Quality metrics.

## Specific Production Examples

5+ named systems (Claude Code, Devin, Cursor, AutoGen, MetaGPT, OpenHands, etc) с
URL + 1-2 line descriptor of their loop architecture. Bulleted list.

## Critical Assessment

- **Pros** of each major variant (specific, evidence-backed, source-cited)
- **Cons + failure modes** (specific, evidence-backed, source-cited)
- **When to use vs avoid** (decision rules for a solo founder building 11-agent
  Claude Code system)

## Comparison к Anthropic ecosystem

How each loop variant maps (or doesn't) to Claude Code / Claude Agent SDK / Claude
API. Which are natively supported, which require external scaffolding (LangGraph
etc.).

## Sources List

Numbered list of ALL URLs cited inline, с author + publication date when available.
Format: `[N] Author, "Title" (Publication, YYYY-MM-DD). URL`.

# Quality Requirements

- **Citations inline** ([1], [2], etc) + full URL list at end
- **Multi-source:** minimum 5 different sources, prefer 10+
- **Specificity:** "Claude Code uses Task tool to spawn sub-agents that inherit
  CLAUDE.md но NOT conversation history" NOT "Claude Code has sub-agents"
- **Verbatim traces strongly preferred** — if a published ReAct trace or Claude
  Code transcript exists, reproduce it literally
- **Critical lens:** include criticism of each loop variant (ReAct's verbosity,
  Reflexion's cost, Plan-and-Execute's brittleness, etc)
- **Recency:** 2024-2026 sources primary (2022-2023 acceptable for foundational
  ReAct/Reflexion/ToT papers)
- **Authoritative sources:** arXiv papers, Anthropic/OpenAI/Google DeepMind
  engineering blogs, Cognition Labs posts, GitHub repos of named systems (AutoGen,
  MetaGPT, OpenHands), podcast transcripts (Latent Space, Dwarkesh) > random blog
  spam
- **Verbatim quotes:** when Boris Cherny / Scott Wu / Shunyu Yao / Harrison Chase
  makes a claim, quote them directly
- **Length:** comprehensive — likely 10-30 pages markdown

# What to AVOID

- Generic "agents follow observe-act cycle" prose without specifics
- Marketing claims from framework vendors as truth (LangChain, AutoGen marketing
  needs critical lens)
- Conflating "agentic loop" with generic "LLM chain" — preserve distinction (loops
  have state feedback; chains don't)
- Single-source dependencies (one LangChain docs page = insufficient)
- Aged sources (pre-2022 unless foundational — but ReAct is 2022 so fine)
- Speculation about internal Anthropic implementation when not publicly disclosed —
  flag explicitly as "internal, not public" rather than guessing
- Pseudocode masquerading as real production traces
