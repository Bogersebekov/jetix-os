---
type: perplexity-research-prompt
wave: 8
topic: Skills + CLAUDE.md + knowledge storage — native Claude Code mechanisms
created: 2026-04-21
target: Perplexity Pro Search (Comet desktop or web)
estimated-perplexity-time: 5-15 min
output-target: raw/research/compounding-engineering-2026-04-22/R-8-skills-claudemd-knowledge.md
---

# Perplexity Prompt — Wave 8: Skills + CLAUDE.md + Knowledge Storage

## Instructions для Ruslan (НЕ для Perplexity)

1. Откройте Perplexity (Comet desktop или Pro web — https://perplexity.ai)
2. Включите **Pro Search mode** (deep research, НЕ Quick Search)
3. Скопируйте всё ниже разделителя `═══` в Perplexity
4. Дождитесь completion (5-15 min)
5. Optional: задайте 2-3 follow-up questions (см. ниже)
6. Сохраните output в `raw/research/compounding-engineering-2026-04-22/R-8-skills-claudemd-knowledge.md`

## Recommended follow-up questions (после initial answer)

1. "Show me the canonical example of an excellent CLAUDE.md — a public repo that
   the community agrees has a well-crafted CLAUDE.md. Link + reasoning."
2. "What's the precise relationship between Skills, Sub-agents, and Slash Commands
   in Claude Code? When should each be used? Give a decision tree."
3. "Where do most teams reinvent something Claude Code already provides? List the
   top 3 anti-patterns with named projects that fell into them."

═══════════════════════════════════════════════════════════════════
THE PROMPT (copy below this line into Perplexity)
═══════════════════════════════════════════════════════════════════

# Role + Context

You are a senior research analyst conducting deep technical due diligence on
**Claude Code's native knowledge mechanisms** — Skills, CLAUDE.md files, plugins,
MCP servers, slash commands, memory systems — for a Berlin-based AI consultancy
(Jetix) currently running a custom wiki + per-agent strategies.md system.

The question: should Jetix replace (or supplement) its custom knowledge layer with
native Claude Code primitives? Where do the native mechanisms excel, where do they
fall short, and what are the community-validated best practices?

This is **deep research**, not a summary. Depth > breadth. Specific > vague.
Multi-source > single-source. Recent (2024-2026) > older. Official documentation
URLs required for each feature.

# Research Questions (answer ALL, in order, with specifics)

1. **Skills system — full documentation.** What is the Skills feature in Claude
   Code? File format (markdown + YAML frontmatter?). Required fields. Location
   conventions (~/.claude/skills/, project-level .claude/skills/, plugin skills).
   Link to official docs.
2. **Skills discovery.** How does Claude Code know which skills are available?
   Is it scan-on-startup? On-demand? What signals trigger skill loading into
   context? How is ambiguity between similarly-named skills resolved?
3. **Skills inheritance & scope.** User-level vs project-level vs plugin skills —
   how do they interact? Override rules? Namespace collisions? Plugin-provided
   skills (e.g., `plugin:skill` form) — how invoked?
4. **anthropic-skills package.** Is there an official "anthropic-skills" package /
   repository? What's in it? Canonical examples of well-written skills. GitHub
   URLs.
5. **CLAUDE.md best practices — user-level.** ~/.claude/CLAUDE.md: what belongs
   there vs project-level? Community-validated patterns. Size guidelines. Common
   contents (tone preferences, memory rules, tool preferences).
6. **CLAUDE.md best practices — project-level.** ./CLAUDE.md: what belongs there?
   Examples from well-known public repos. Common contents (codebase conventions,
   testing commands, architectural notes).
7. **CLAUDE.md hierarchy + override rules.** If user-level and project-level
   CLAUDE.md both exist, how does Claude Code merge them? Is there a precedence
   order? Subdirectory CLAUDE.md (CLAUDE.md in nested dirs) — how does that work?
8. **CLAUDE.md size limits & performance.** Is there a token budget for CLAUDE.md?
   Truncation behavior? Chunking strategies. Community advice on keeping
   CLAUDE.md small.
9. **Memory systems.** Auto-memory feature in Claude Code (persistent file-based
   memory like ~/.claude/projects/<slug>/memory/). How it works. Session memory
   vs persistent memory. When each used. Official docs URL.
10. **Per-agent / per-subagent memory layering.** Are sub-agents given isolated
    memory or shared? How do patterns like per-agent strategies.md fit with
    Claude Code's native memory?
11. **Plugins ecosystem.** Claude Code plugin marketplace. Installable packages.
    Examples: claude-code-guide, other named plugins. How plugins are installed
    and managed. Official docs.
12. **MCP servers integration.** How MCP servers store and expose knowledge
    across sessions. Canonical MCP servers (notion, github, filesystem, memory).
    Integration with Claude Code specifically.
13. **Slash commands & their relation to skills.** Slash commands — how defined,
    where stored (.claude/commands/). Difference from skills. When to use each.
    Community best practices.
14. **Best community-curated examples.** Awesome-Claude-Code lists, GitHub
    stars, popular plugins. Provide URLs to the best community resources.
15. **Common mistakes & anti-patterns.** What do teams reinvent that Claude Code
    already provides? What mistakes to avoid in CLAUDE.md / Skills / plugins?
    Named examples of projects that fell into these traps and public
    post-mortems if any.

# Required Output Format

Structure your response as a **structured markdown report** with these sections:

## Executive Summary (300-500 words)

Single-paragraph synthesis + top 5 key findings (is native Claude Code enough,
or should custom layer be added).

## Section 1 — Skills System: Full Documentation

Answer Q1, Q2, Q3, Q4. Format, discovery, scope, official examples. Include code
snippets of well-formed skills.

## Section 2 — CLAUDE.md: Best Practices & Hierarchy

Answer Q5, Q6, Q7, Q8. User vs project vs subdirectory; size limits; override
rules; examples from public repos.

## Section 3 — Memory & Per-Agent Layering

Answer Q9, Q10. Auto-memory mechanism; persistent vs session; per-subagent
patterns; comparison with custom per-agent strategies.md approach.

## Section 4 — Plugins, MCP Servers, Slash Commands

Answer Q11, Q12, Q13. Each primitive: what it is, when to use, best practices,
official docs URLs.

## Section 5 — Community Resources

Answer Q14. Awesome lists, popular plugins, canonical example repos. Concrete URLs.

## Section 6 — Anti-Patterns & Comparison to Custom Solutions

Answer Q15. Common mistakes; teams that reinvented native features; when custom
knowledge layer (like Jetix's wiki + strategies.md) makes sense vs when native
mechanisms are sufficient.

## Specific Production Examples (Cross-Reference)

- Top 5 public repos with excellent CLAUDE.md files (URLs)
- Top 5 skills examples (URLs to actual skill files or plugin repos)
- Top 5 MCP servers for knowledge management (official + community)
- Top 3 community-curated plugin lists

## Critical Assessment

- **Native mechanisms excel at** (specific use cases with evidence)
- **Native mechanisms fall short at** (specific gaps with evidence)
- **When to use Claude Code native vs build custom** (decision rules)
- **When to use both together** (hybrid pattern examples)

## Comparison к custom knowledge layer (Jetix-specific)

Jetix currently runs: wiki/ (9 entity types, edges graph), per-agent strategies.md,
niche symlinks, custom skills (/ingest, /ask, /lint). Where does this overlap
with native Claude Code? Where is it additive? What should Jetix consider
migrating to native?

## Sources List

Numbered list of ALL URLs cited inline, with author + date when available.
Format: `[N] Author, "Title" (Publication, YYYY-MM-DD). URL`.

# Quality Requirements

- **Official documentation URLs required** for every Claude Code feature described
- **Citations inline** ([1], [2], etc) + full URL list at end
- **Multi-source:** minimum 5 different sources, prefer 10+ (official docs +
  community blog posts + example repos)
- **Specificity:** "Skills live in ~/.claude/skills/<name>/SKILL.md with YAML
  frontmatter requiring `description` field" NOT "Skills are configuration files"
- **Code snippets:** show actual skill / CLAUDE.md examples, not conceptual only
- **Recency:** 2024-2026 sources primary (Claude Code evolves rapidly; 2023 may
  be outdated)
- **Authoritative sources:** Anthropic official docs, Boris Cherny Twitter/blog,
  widely-starred community repos, founder blog posts > random tutorial spam
- **Length:** comprehensive — likely 15-30 pages markdown

# What to AVOID

- Outdated documentation (Claude Code features evolved rapidly 2024-2026 — verify
  currency)
- Marketing-only prose without mechanism
- Generic "Claude is configurable" statements
- Single-source dependencies
- Confusing Claude (the model) with Claude Code (the CLI) — disambiguate everywhere
- Confusing Claude Code native features with third-party extensions — label clearly
- Hallucinating features that don't exist (if unsure a feature is real, say so
  explicitly)
