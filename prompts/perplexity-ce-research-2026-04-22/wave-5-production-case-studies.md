---
type: perplexity-research-prompt
wave: 5
topic: Production case studies — Devin, Cursor, Sweep, Aider, Wispr, Replit, Copilot, Anthropic
created: 2026-04-21
target: Perplexity Pro Search (Comet desktop or web)
estimated-perplexity-time: 5-15 min
output-target: raw/research/compounding-engineering-2026-04-22/R-5-production-case-studies.md
---

# Perplexity Prompt — Wave 5: Production Case Studies (General)

## Instructions для Ruslan (НЕ для Perplexity)

1. Откройте Perplexity (Comet desktop или Pro web — https://perplexity.ai)
2. Включите **Pro Search mode** (deep research, НЕ Quick Search)
3. Скопируйте всё ниже разделителя `═══` в Perplexity
4. Дождитесь completion (5-15 min)
5. Optional: задайте 2-3 follow-up questions (см. ниже)
6. Сохраните output в `raw/research/compounding-engineering-2026-04-22/R-5-production-case-studies.md`

## Recommended follow-up questions (после initial answer)

1. "What's the single most successful production multi-agent system today by
   revenue / ARR? Show source."
2. "Which of these products would you copy directly for a solo Berlin AI consultancy
   building internal operations tooling? Rank with rationale."
3. "Which of these products moved AWAY from multi-agent in 2025-2026 and back toward
   single-agent? Any public reasoning?"

═══════════════════════════════════════════════════════════════════
THE PROMPT (copy below this line into Perplexity)
═══════════════════════════════════════════════════════════════════

# Role + Context

You are a senior research analyst conducting deep product due diligence on the
**leading production multi-agent / CE / AI-coding products of 2024-2026** for a
Berlin-based AI consultancy (Jetix). The output will inform architecture choices
for our internal 12-agent operational system.

This is **deep research**, not a summary. For each product: architecture, results,
controversies, open source vs proprietary. Depth > breadth. Specific > vague.
Multi-source > single-source. Recent (2024-2026) > older.

# Research Questions (answer ALL, in order, with specifics)

For each product below, provide: (a) Founding team + funding, (b) Architecture
(single-agent / multi-agent / swarm / hierarchical / compound), (c) Public
metrics (revenue/ARR, user count, task success rate, benchmark performance),
(d) Controversies / critiques, (e) Recent changes 2025-2026, (f) Open source
or proprietary.

1. **Devin (Cognition Labs).** Full architecture. Pokemon benchmark controversy
   (March 2024 launch). SWE-Bench performance. Funding. Recent developments
   including Devin 2.0 if applicable.
2. **Cursor (Anysphere).** Multi-agent features (sub-agents, background agents).
   Composer. Agent mode vs chat mode. Production usage stats. Revenue rumors.
3. **Sweep.dev.** How their "swarm of agents" works. Architecture. Metrics. Is
   Sweep still active in 2026?
4. **Aider.** Solo-but-iterative model. Paul Gauthier's design choices. Why
   single-agent-with-memory rather than multi-agent. Benchmark results. Lessons.
5. **Wispr Flow.** Voice-to-action multi-agent design. Architecture. Target user.
   Pricing. Growth.
6. **GitHub Copilot Workspace.** Multi-agent architecture. Preview → GA timeline.
   Adoption data.
7. **Replit Agent.** Design. Adoption metrics. How it combines IDE + agents.
   Recent Replit Ghostwriter evolution.
8. **Anthropic's own production agents.** Claude Code, Claude Computer Use, Claude
   in Slack — architecture details. How Anthropic dogfooded its own multi-agent
   thinking.
9. **Lovable / v0 / Bolt.** Design-tool agents. Architecture (single vs multi).
   User base. Which are winning 2026.
10. **Continue.** Open-source agent architecture. Community stats. How it compares
    to Cursor/Aider.
11. **Comparison matrix across all above.** Table: product × (architecture type:
    swarm / hierarchy / compound / hybrid / single, license, price, team size,
    revenue/users).
12. **Commercial/pricing models.** What pricing works for multi-agent products?
    Usage-based vs subscription vs per-task? Cite actual pricing pages.
13. **User feedback patterns.** What users love / hate about each product. Sample
    Reddit, HN, Twitter threads with quotes.
14. **Engineering team sizes.** Behind each product, how many engineers built it?
    This informs whether solo founders can realistically build equivalent.
15. **Open source vs proprietary dynamics.** Which products are open source +
    thriving? Which proprietary + winning? Is there a pattern?

# Required Output Format

Structure your response as a **structured markdown report** with these sections:

## Executive Summary (300-500 words)

Single-paragraph synthesis + top 5 key findings (which product design is winning
commercially, which architecturally, which is best template for solo founder).

## Section 1 — Devin (Cognition Labs)

Full deep dive. Architecture, Pokemon controversy, SWE-Bench, funding, current state.

## Section 2 — Cursor (Anysphere)

Full deep dive. Composer, sub-agents, background agents, revenue, recent moves.

## Section 3 — Open-Source Coding Agents: Sweep, Aider, Continue

Answer Q3, Q4, Q10. Architecture comparison, community, design philosophy.

## Section 4 — Design / Vibe-Coding Agents: Lovable, v0, Bolt, Replit

Answer Q7, Q9. Market comparison, adoption, winner analysis.

## Section 5 — Voice & Workflow: Wispr, Copilot Workspace

Answer Q5, Q6. Voice-first design; Microsoft's Copilot approach.

## Section 6 — Anthropic's Own Production Agents

Answer Q8. Claude Code, Computer Use, Claude in Slack. How Anthropic dogfoods.

## Section 7 — Comparison Matrix & Commercial Dynamics

Answer Q11, Q12, Q14, Q15. Cross-product comparison table; pricing; team sizes;
open source vs proprietary patterns.

## Section 8 — User Feedback & Community

Answer Q13. Representative quotes from Reddit / HN / Twitter, what users love/hate.

## Specific Production Examples (Cross-Reference)

5+ named entities as bulleted list, each with URL and 1-2 line descriptor. Include
links to their architecture blogs / engineering posts where they've explained internals.

## Critical Assessment

- **What works commercially in 2026** (pattern-level conclusions)
- **What's abandoned or deprecated** (products that pivoted away from multi-agent)
- **Templates suitable for solo founder** (which to copy, which not to)

## Comparison к Anthropic ecosystem

Which of these products build on Claude? On Claude Code primitives? On MCP?
What's Anthropic's official partnership / integration story?

## Sources List

Numbered list of ALL URLs cited inline, with author + date when available.
Format: `[N] Author, "Title" (Publication, YYYY-MM-DD). URL`.

# Quality Requirements

- **Citations inline** ([1], [2], etc) + full URL list at end
- **Multi-source:** minimum 5 different sources, prefer 10+
- **Specificity:** "Cursor Composer uses Claude 4.6 Sonnet with custom streaming
  diff format" NOT "Cursor uses some AI model"
- **Named metrics:** revenue figures, user counts, benchmark scores with dates
- **Critical lens:** controversies, critiques, failures included
- **Recency:** 2024-2026 sources primary
- **Authoritative sources:** founder blog posts, engineering tech talks, funding
  announcements, official docs, reputable tech press (The Information, TechCrunch,
  The Verge) > random tech blog
- **Verbatim quotes:** when source makes specific claim, quote it directly
- **Length:** comprehensive — likely 15-30 pages markdown

# What to AVOID

- Marketing fluff from company websites as primary source (cross-verify)
- Generic product descriptions ("powerful AI coding assistant")
- Single-source dependencies
- Aged sources (pre-2023 unless foundational)
- Hallucinated stats — if you don't find the number, say so explicitly
- Missing products — if one of the listed products is unclear, explicitly note
  "could not find authoritative source on X"
