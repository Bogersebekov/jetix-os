---
type: perplexity-research-prompt
wave: 7
topic: Boris Cherny + Claude Code — design philosophy, replaceable agents, CLAUDE.md
created: 2026-04-21
target: Perplexity Pro Search (Comet desktop or web)
estimated-perplexity-time: 5-15 min
output-target: raw/research/compounding-engineering-2026-04-22/R-7-boris-cherny-claude-code.md
---

# Perplexity Prompt — Wave 7: Boris Cherny + Claude Code Design Philosophy

## Instructions для Ruslan (НЕ для Perplexity)

1. Откройте Perplexity (Comet desktop или Pro web — https://perplexity.ai)
2. Включите **Pro Search mode** (deep research, НЕ Quick Search)
3. Скопируйте всё ниже разделителя `═══` в Perplexity
4. Дождитесь completion (5-15 min)
5. Optional: задайте 2-3 follow-up questions (см. ниже)
6. Сохраните output в `raw/research/compounding-engineering-2026-04-22/R-7-boris-cherny-claude-code.md`

## Recommended follow-up questions (после initial answer)

1. "What's Boris Cherny's most important single essay or talk about agent design?
   Pick the one source I should study deeply, with reasoning."
2. "What does Boris say about NOT using swarm or multi-agent patterns — where has
   he cautioned against them?"
3. "Boris's specific advice for solo developers using Claude Code — concrete
   recommendations, not general principles."

═══════════════════════════════════════════════════════════════════
THE PROMPT (copy below this line into Perplexity)
═══════════════════════════════════════════════════════════════════

# Role + Context

You are a senior research analyst conducting a comprehensive profile of
**Boris Cherny** (creator of Claude Code at Anthropic) and the **design philosophy
of Claude Code**. The goal is to extract the deepest available signal on Boris's
specific views: replaceable agents, CLAUDE.md as shared context, sub-agents, hooks,
skills, MCP, and the broader agent-design philosophy he has publicly articulated
2024-2026.

The consumer is a Berlin-based AI consultancy (Jetix) deciding whether to adopt
Claude Code's architectural patterns as the foundation for their internal 12-agent
operational system. They need Boris's actual reasoning — not interpretations of it.

This is **deep research**, not a summary. Depth > breadth. Specific > vague.
Multi-source > single-source. Recent (2024-2026) > older. Verbatim quotes strongly
preferred.

# Research Questions (answer ALL, in order, with specifics)

1. **Boris Cherny biography + role at Anthropic.** Background, education, prior
   companies (he worked at Stripe, Facebook, was TypeScript book author —
   confirm/expand). Current title at Anthropic. Team size. URL to official bio
   if available.
2. **All Boris's public writings — comprehensive list.** Twitter/X: @bcherny.
   Blog: does he have a personal blog? Anthropic engineering blog posts with his
   byline. Books: "Programming TypeScript" O'Reilly. For each writing: title,
   date, URL, 1-2 line summary.
3. **Boris's podcast appearances.** Latent Space (swyx + Alessio), Dwarkesh Patel,
   Lex Fridman, AI Daily Brief, How Do You Use ChatGPT (Dan Shipper), AI Engineer
   Summit talks. For each: host, date, episode title, URL, key quotes specifically
   about agent design.
4. **Boris's conference talks.** AI Engineer Summit, Anthropic's own events, anywhere
   else. List title, date, venue, URL if recorded.
5. **Claude Code architecture decisions.** Why swarm over hierarchy? Boris's
   explicit reasoning — find the source where he explains this design choice
   verbatim.
6. **Replaceable agents principle.** Boris has stated (where exactly?) that in
   Claude Code "any sub-agent can do any task" / agents are replaceable. Find the
   exact phrasing + source + surrounding context. What is his reasoning?
7. **CLAUDE.md as shared context.** Design rationale. Why markdown? Why project-
   level + user-level? Why hierarchical override? Find Boris's explicit statements
   on CLAUDE.md design.
8. **Sub-agent system in Claude Code.** Mechanics: how sub-agents are spawned,
   what context they inherit, how they report back. Best practices Boris has
   articulated. Use cases (when to use sub-agents, when not to).
9. **Hooks system.** Settings.json hooks, lifecycle hooks (user-prompt-submit-hook,
   etc). Full design. Why this interface? Security model. What hooks enable that
   slash commands don't.
10. **Skills feature.** Newer (2025-2026). How it works, location (~/.claude/skills/),
    format, discovery. Boris's intent behind Skills. How Skills differ from
    slash commands and sub-agents.
11. **MCP (Model Context Protocol).** Boris's role in MCP — was he involved?
    Design rationale from his perspective. How MCP integrates with Claude Code.
12. **Broader agent-design philosophy.** Beyond Claude Code specifics, what general
    principles does Boris advocate? Things like: keep it simple, markdown > JSON,
    human-readable configs, context over control, etc. Quote verbatim where possible.
13. **Anthropic research papers with Boris's involvement.** Co-authored papers,
    technical reports, or major blog posts. List with dates + URLs.
14. **Public criticism Boris has faced.** Criticism of Claude Code's design —
    complaints, counter-arguments, debates on Twitter/HN. Name critics + their
    arguments + Boris's responses.
15. **Future direction Boris hints at for Claude Code.** Recent statements about
    where Claude Code is heading 2026-2027. Features on roadmap. Quote verbatim
    where possible.

# Required Output Format

Structure your response as a **structured markdown report** with these sections:

## Executive Summary (300-500 words)

Single-paragraph synthesis of Boris's design philosophy + top 5 key findings.

## Section 1 — Boris Cherny: Profile & Writings

Answer Q1, Q2. Biography, role, comprehensive writings list with URLs.

## Section 2 — Talks, Podcasts, Interviews

Answer Q3, Q4. Podcast-by-podcast quotes; conference talks; verbatim extracts
specifically about agent design.

## Section 3 — Claude Code Architecture: The Core Decisions

Answer Q5, Q6. Swarm over hierarchy reasoning; replaceable agents principle
verbatim + reasoning.

## Section 4 — CLAUDE.md Design Rationale

Answer Q7. Why markdown, why hierarchical, why project+user, override rules.
Boris's explicit statements.

## Section 5 — Sub-agents, Hooks, Skills, MCP

Answer Q8, Q9, Q10, Q11. Each feature's mechanics, design rationale, Boris's
intent, best practices.

## Section 6 — Broader Philosophy

Answer Q12, Q13. General agent-design principles; co-authored research.

## Section 7 — Criticism & Future Direction

Answer Q14, Q15. Named critics + arguments; future roadmap hints.

## Specific Sources (Cross-Reference)

Boris's key sources as a bulleted list for easy scanning:
- Twitter/X handle + any pinned threads
- Personal website / blog (if exists)
- Top 3-5 Anthropic blog posts authored or co-authored
- Top 3-5 podcast appearances
- Top 3-5 conference talks
- Book (Programming TypeScript)

## Critical Assessment

- **Boris's strongest design arguments** (where his reasoning is compelling + evidence)
- **Weaknesses in his stated philosophy** (where critics have surfaced real gaps)
- **When Claude Code's design is RIGHT for a use case** vs when it's not (decision rules)

## Comparison к other agent design philosophies

How does Boris's view contrast with:
- Cognition Labs (Devin) planning-first philosophy
- Every.to Compound architecture
- CrewAI / AutoGen hierarchical coordination
- Levenchuk's systems-thinking critique

## Sources List

Numbered list of ALL URLs cited inline, with author + date when available.
Format: `[N] Author, "Title" (Publication, YYYY-MM-DD). URL`.

# Quality Requirements

- **Citations inline** ([1], [2], etc) + full URL list at end
- **Multi-source:** minimum 5 different sources, prefer 10+
- **Verbatim quotes are critical** for this wave — when Boris says something,
  quote him directly
- **Specificity:** "Boris said on Latent Space podcast 2025-03-12 that CLAUDE.md
  should be 'curated, not scraped'" NOT "Boris has said things about CLAUDE.md"
- **Critical lens:** include criticisms of Boris's positions
- **Recency:** 2024-2026 sources primary
- **Authoritative sources:** Boris's own Twitter/blog/podcasts/talks > secondary
  interpretations
- **Length:** comprehensive — likely 10-25 pages markdown

# What to AVOID

- Marketing fluff from Anthropic press releases alone
- Paraphrase when verbatim is available
- Secondary sources when primary Boris statements exist
- Single-source dependencies
- Aged sources (pre-2023 — Claude Code launched 2024)
- Conflating Boris's views with Anthropic's official views (they may align but
  are not identical)
- Fabrication — if you can't find a Boris statement on a topic, explicitly say
  "no public Boris statement found on this specific question"
