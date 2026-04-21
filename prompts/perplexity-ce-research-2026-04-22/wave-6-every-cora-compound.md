---
type: perplexity-research-prompt
wave: 6
topic: Every / Cora / Compound — Dan Shipper, Plan → Work → Review×12 architecture
created: 2026-04-21
target: Perplexity Pro Search (Comet desktop or web)
estimated-perplexity-time: 5-15 min
output-target: raw/research/compounding-engineering-2026-04-22/R-6-every-cora-compound.md
---

# Perplexity Prompt — Wave 6: Every / Cora / Compound Deep Dive

## Instructions для Ruslan (НЕ для Perplexity)

1. Откройте Perplexity (Comet desktop или Pro web — https://perplexity.ai)
2. Включите **Pro Search mode** (deep research, НЕ Quick Search)
3. Скопируйте всё ниже разделителя `═══` в Perplexity
4. Дождитесь completion (5-15 min)
5. Optional: задайте 2-3 follow-up questions (см. ниже)
6. Сохраните output в `raw/research/compounding-engineering-2026-04-22/R-6-every-cora-compound.md`

## Recommended follow-up questions (после initial answer)

1. "Show me a concrete error → rule → subagent → skill cycle example from Cora
   — an actual traced case with inputs and outputs, not a conceptual description."
2. "What's the smallest compound architecture (Plan / Work / Review cycle) I can
   replicate as a solo dev in under a week? Point to specific repos or guides."
3. "Where does Compound break down or fail? What tasks is it bad at, and what has
   Every / Dan Shipper publicly acknowledged as limits?"

═══════════════════════════════════════════════════════════════════
THE PROMPT (copy below this line into Perplexity)
═══════════════════════════════════════════════════════════════════

# Role + Context

You are a senior research analyst conducting deep due diligence on **Every.to**
(the AI-focused publication), its **Cora email assistant product**, and specifically
the **"Compound" architecture** that Every's team has publicized (Plan agent → Work
agents → Review agents × 12 → Compound cycle, where errors become rules become
subagents become skills).

The consumer is a Berlin-based AI consultancy (Jetix) deciding whether to adopt
Compound as the core methodology for their internal 12-agent operational system.

This is **deep research**, not a summary. Depth > breadth. Specific > vague.
Multi-source > single-source. Recent (2024-2026) > older.

# Research Questions (answer ALL, in order, with specifics)

1. **Every.to history.** When founded, by whom, funding, current business model.
   Key writers today (Dan Shipper, Nathan Baschez, others — list). Paid subscription
   structure. URL to about page.
2. **Every.to thesis on AI.** What is Every's core intellectual thesis about AI
   tools and agents? Quote from their editorial manifestos or key essays.
3. **Cora email assistant — product.** Full product description: what it does, who
   it's for, price, distribution model. Founded when. Current state (beta / GA /
   deprecated). URL.
4. **Cora technical architecture.** What stack? (Anthropic Claude? OpenAI? custom
   orchestration?) How do agents work internally? Any published architecture
   diagrams or engineering blog posts? URL each.
5. **Compound concept — mechanics.** Detailed description of the Plan → Work →
   Review × 12 → Compound cycle. How many agents, what roles, how they hand off,
   what state is shared. Find the canonical source describing this — blog post,
   podcast, talk. Quote verbatim.
6. **"Errors become rules become subagents become skills".** Knowledge-learns-from-
   errors pipeline — how exactly does it work? Trace a specific example from Every's
   published material where an error turned into a rule turned into a subagent.
7. **Dan Shipper's essays on compound / agents (2024-2026).** Comprehensive list:
   title, date, URL, 1-2 line summary of key idea. Include essays like "Vibe check",
   "How I use AI", agent-focused Every posts, etc.
8. **Podcasts / interviews where Compound discussed.** AI Daily Brief, Latent Space,
   Dan Shipper's own podcast ("How Do You Use ChatGPT?"). For each relevant episode:
   guests, date, URL, key Compound-related quotes.
9. **AI Daily, AI Labs, other Every properties.** Beyond Cora, what AI properties
   does Every run? Short description of each.
10. **Compound vs Devin's planning.** How does Compound architecture differ from
    Devin's (Cognition) planning-then-execution model? Explicit comparison with
    named differences.
11. **Tooling stack.** Does Compound use Anthropic's Claude Agent SDK? Custom
    orchestration? LangGraph? Has Every published any code, open-source components,
    or engineering details?
12. **Critical reception.** Who has challenged Compound's claims publicly? Critiques,
    skeptical podcast discussions, Twitter threads. Name critics with URLs.
13. **Adoption of Cora.** How many users, growth rate, retention, revenue
    (if published). Distinguish public vs rumored.
14. **Open source components.** Has Every open-sourced any part of Compound or Cora?
    GitHub repos?
15. **Future direction of Every / Compound.** Where is Every taking Compound 2026-
    2027? Founder public statements.

# Required Output Format

Structure your response as a **structured markdown report** with these sections:

## Executive Summary (300-500 words)

Single-paragraph synthesis + top 5 key findings (is Compound a real pattern or
a marketing frame; should Jetix adopt it).

## Section 1 — Every.to: Publication, Team, Thesis

Answer Q1, Q2, Q9. History, writers, AI thesis, other properties.

## Section 2 — Cora: Product & Architecture

Answer Q3, Q4. Product description, pricing, architecture stack, engineering blog posts.

## Section 3 — Compound Architecture: Mechanics

Answer Q5, Q6. Detailed breakdown of Plan → Work → Review × 12 cycle; errors-to-skills
pipeline with specific traced example.

## Section 4 — Dan Shipper Writings & Talks

Answer Q7, Q8. Comprehensive essays list; podcasts/interviews; key verbatim quotes.

## Section 5 — Comparison to Other Architectures

Answer Q10, Q11. Compound vs Devin explicit comparison; tooling stack; any open
source components.

## Section 6 — Critical Reception & Adoption

Answer Q12, Q13, Q14. Named critics; user/revenue metrics; open source.

## Section 7 — Future Direction

Answer Q15.

## Specific Production Examples (Cross-Reference)

- Every.to homepage + manifesto URLs
- Cora product page + pricing
- 3+ key Dan Shipper essays with URLs
- 2+ podcast appearances discussing Compound with URLs
- Any GitHub repos associated with Every/Cora

## Critical Assessment

- **Pros** (where Compound is a genuine architectural contribution — evidence-backed)
- **Cons + failure modes** (where Compound is likely over-marketed or limited)
- **When to use vs avoid** (decision rules for Jetix adoption)

## Comparison к Anthropic ecosystem

Does Cora use Claude Code primitives? MCP? Claude Agent SDK? What's the integration
level with Anthropic's stack vs custom tooling?

## Sources List

Numbered list of ALL URLs cited inline, with author + date when available.
Format: `[N] Author, "Title" (Publication, YYYY-MM-DD). URL`.

# Quality Requirements

- **Citations inline** ([1], [2], etc) + full URL list at end
- **Multi-source:** minimum 5 different sources, prefer 10+
- **Specificity:** "Compound uses a Planner agent calling 12 Worker agents with
  a Reviewer layer running on Claude 4.6 Sonnet" NOT "Compound has multiple agents"
- **Verbatim quotes** from Dan Shipper and Every team — essential for this wave
- **Critical lens:** include pros AND cons, name critics
- **Recency:** 2024-2026 sources primary
- **Authoritative sources:** Every.to essays, Dan Shipper podcasts/talks, Cora
  product pages, engineering blogs, HN discussions > random blog spam
- **Length:** comprehensive — likely 10-25 pages markdown

# What to AVOID

- Marketing fluff from Every's own pages as sole evidence (cross-verify with
  third parties)
- Generic "Compound is a new approach" prose without the mechanism
- Single-source dependencies (Every writing about Every)
- Aged sources (pre-2023)
- Confusing Every/Compound with other "compound" terms (Buffett's compound interest,
  compound components in React, etc — disambiguate)
- Speculation without source attribution
