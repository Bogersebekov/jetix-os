---
type: perplexity-research-prompt
wave: 2
topic: Swarm intelligence agents — multi-agent collectives, coordination patterns
created: 2026-04-21
target: Perplexity Pro Search (Comet desktop or web)
estimated-perplexity-time: 5-15 min
output-target: raw/research/compounding-engineering-2026-04-22/R-2-swarm-intelligence.md
---

# Perplexity Prompt — Wave 2: Swarm Intelligence Agents

## Instructions для Ruslan (НЕ для Perplexity)

1. Откройте Perplexity (Comet desktop или Pro web — https://perplexity.ai)
2. Включите **Pro Search mode** (deep research, НЕ Quick Search)
3. Скопируйте всё ниже разделителя `═══` в Perplexity (включая `# Role + Context` и ниже)
4. Дождитесь completion (5-15 min)
5. Optional: задайте 2-3 follow-up questions (см. ниже)
6. Сохраните output в `raw/research/compounding-engineering-2026-04-22/R-2-swarm-intelligence.md`

## Recommended follow-up questions (после initial answer)

1. "What's the production-tested optimal team size for swarm coordination (3 agents?
   7? 20?) — show data, not speculation."
2. "Show me the simplest possible swarm implementation a solo founder can replicate
   in under 200 lines of code — link to the repo."
3. "Where does swarm coordination overhead become prohibitive? Quantify the threshold
   with specific observed token/latency numbers."

═══════════════════════════════════════════════════════════════════
THE PROMPT (copy below this line into Perplexity)
═══════════════════════════════════════════════════════════════════

# Role + Context

You are a senior research analyst conducting deep technical due diligence on
**swarm intelligence patterns in AI agent systems** for a Berlin-based AI consultancy
(Jetix) building a multi-agent operational system. The output will be used to make a
critical architecture decision: should we replace our current hierarchical 12-agent
design (CEO/Strategist → Manager → Leads → Workers) with a swarm pattern (interchangeable
agents + shared context like Claude Code's model)?

This is **deep research**, not a summary. Depth > breadth. Specific > vague.
Multi-source > single-source. Recent (2024-2026) > older.

# Research Questions (answer ALL, in order, with specifics)

1. **Definitions.** Precisely distinguish: **swarm intelligence**, **multi-agent
   system (MAS)**, **hive-mind coordination**, **agent society**, **actor model**.
   Where do these terms overlap and where do they diverge? Cite the canonical
   academic/industrial definition for each.
2. **Stigmergy + indirect coordination.** Explain stigmergy (ant-trail model) and
   how it's implemented in AI agents via **shared environment** (e.g., shared file
   system, CLAUDE.md, blackboard pattern, shared memory store). Provide 2-3 concrete
   production examples.
3. **Framework comparison.** Deep comparison of: **Microsoft AutoGen**, **CrewAI**,
   **LangGraph**, **Anthropic MCP (Model Context Protocol)**, **OpenAI Swarm**
   (released Oct 2024), **Claude Agent SDK**, **Metagpt**, **AutoGPT legacy**.
   For each: coordination primitive, shared state model, replaceability of agents,
   production readiness, adoption.
4. **OpenAI Swarm framework specifically.** What does it teach? What were the
   design choices? Is it still maintained or deprecated? What's the successor?
5. **When swarm wins vs loses.** Enumerate scenarios (task types, team sizes,
   problem structures) where swarm empirically beats sequential/single-agent —
   and where it empirically loses. Cite benchmark studies.
6. **Cost dynamics.** Anthropic's published estimate that multi-agent uses
   "~15× tokens" vs single-agent — find the original source + any follow-up
   measurements. For a solo developer: is the token leverage worth it? At what
   task complexity does the break-even occur?
7. **Coordination overhead.** As agent count grows, when does coordination
   overhead become prohibitive? Is there an observed "sweet spot" team size
   (3, 5, 7, 12, 20)? Cite research or production reports.
8. **Production examples.** Identify 5+ production swarm AI systems with named
   companies + quantitative results. Separate: internal-tooling cases vs customer-
   facing products.
9. **Devin (Cognition Labs) architecture.** Does Devin use swarm or hierarchy?
   Find the most authoritative technical description of its internal agent graph.
10. **Anthropic research papers on multi-agent (2024-2026).** List relevant
    Anthropic technical reports, research blog posts, papers with authors + dates
    + URLs. Extract key empirical findings.
11. **Replaceable agents principle.** "Any agent can do any task" (Boris Cherny's
    phrasing in Claude Code) — what are the actual implementation patterns that
    make this work? What context must be shared, and how?
12. **Compound errors problem.** Each agent in a pipeline introduces some
    hallucination/error rate p; with N agents the cumulative error compounds.
    Find quantitative measurements of this effect (multi-agent output accuracy vs
    single-agent baseline on identical tasks).
13. **Token economics for solo developers.** If Ruslan (solo, $50k revenue goal,
    Berlin) adopts swarm, what are the practical monthly token costs? Cite real
    examples of solo devs reporting their Claude API / Claude Code bill for
    multi-agent workflows.
14. **Hybrid hierarchy+swarm patterns.** Who combines both (planner on top, swarm
    below; or swarm for R&D, hierarchy for execution)? Find 2-3 named examples
    with architectural details.
15. **Future predictions.** Where are swarm AI agents heading 2026-2027? Cite
    researchers + specific predictions (who, when, URL).

# Required Output Format

Structure your response as a **structured markdown report** with these sections:

## Executive Summary (300-500 words)

Single-paragraph synthesis + top 5 key findings.

## Section 1 — Definitions & Distinctions

Answer Q1, Q2. Precisely define swarm / MAS / hive-mind / stigmergy with citations.

## Section 2 — Framework Comparison Matrix

Answer Q3, Q4. Table: framework × (coordination primitive, shared state, replaceability,
production readiness, license, adoption). Include all frameworks listed above.

## Section 3 — Empirical Performance: Swarm vs Sequential

Answer Q5, Q6, Q7, Q12. Where swarm wins/loses; cost dynamics; coordination overhead
sweet spot; compound error quantification.

## Section 4 — Production Deployments

Answer Q8, Q9, Q10. 5+ swarm production systems; Devin's architecture in depth;
Anthropic's published findings.

## Section 5 — Design Patterns

Answer Q11, Q14. Replaceable-agent implementation patterns; hybrid hierarchy+swarm
architectures.

## Section 6 — Solo-Founder Economics

Answer Q13. Real monthly bills, break-even task complexity.

## Section 7 — Future Direction

Answer Q15.

## Specific Production Examples

5+ named entities/products/papers with URLs, 1-2 line descriptor each.

## Critical Assessment

- **Pros** (when swarm is the right choice — evidence-backed)
- **Cons + failure modes** (when swarm hurts — compound errors, cost, debugging)
- **When to use vs avoid** (explicit decision rules)

## Comparison к Anthropic ecosystem

Claude / Claude Code / Claude Agent SDK / MCP — where do these fit in swarm vs
hierarchy spectrum? What does Anthropic officially recommend?

## Sources List

Numbered list of ALL URLs cited inline, with author + date when available.
Format: `[N] Author, "Title" (Publication, YYYY-MM-DD). URL`.

# Quality Requirements

- **Citations inline** ([1], [2], etc) + full URL list at end
- **Multi-source:** minimum 5 different sources, prefer 10+
- **Specificity:** "AutoGen uses nested chat with GroupChatManager" NOT "AutoGen coordinates somehow"
- **Critical lens:** include pros AND cons, NOT marketing claims as truth
- **Recency:** prefer 2024-2026 sources (acceptable: 2023 if foundational)
- **Authoritative sources:** academic papers, framework docs, benchmarks, founder
  writings > random blog spam
- **Verbatim quotes:** when source makes claim, quote it directly (don't paraphrase)
- **Length:** comprehensive — likely 10-30 pages markdown when copied to file

# What to AVOID

- Marketing fluff ("game-changing", "revolutionary" without evidence)
- Generic "agents collaborate" prose with no mechanism
- Single-source dependencies
- Aged sources (pre-2023 unless foundational)
- Conflating "swarm" with any multi-agent system (the distinction matters —
  interrogate it)
- Speculation without source attribution
