---
type: perplexity-research-prompt
wave: 1
topic: Compounding Engineering core — definitions, origins, practitioners, patterns
created: 2026-04-21
target: Perplexity Pro Search (Comet desktop or web)
estimated-perplexity-time: 5-15 min
output-target: raw/research/compounding-engineering-2026-04-22/R-1-compounding-engineering-core.md
---

# Perplexity Prompt — Wave 1: Compounding Engineering core

## Instructions для Ruslan (НЕ для Perplexity)

1. Откройте Perplexity (Comet desktop или Pro web — https://perplexity.ai)
2. Включите **Pro Search mode** (deep research, НЕ Quick Search)
3. Скопируйте всё ниже разделителя `═══` в Perplexity (включая `# Role + Context` и ниже)
4. Дождитесь completion (5-15 min)
5. Optional: задайте 2-3 follow-up questions (см. ниже) для probing depth
6. Сохраните output в `raw/research/compounding-engineering-2026-04-22/R-1-compounding-engineering-core.md`

## Recommended follow-up questions (после initial answer)

1. "Show me a specific code example or workflow snippet of compounding engineering
   in action — actual repo / actual commands, not conceptual."
2. "What's the smallest-scale operational example I can study as a solo founder —
   one person + Claude Code? Who has documented this?"
3. "Critique from skeptics — who has publicly argued that 'compounding engineering'
   is overhyped or marketing repackaging of older ideas? Name them + their arguments."

═══════════════════════════════════════════════════════════════════
THE PROMPT (copy below this line into Perplexity)
═══════════════════════════════════════════════════════════════════

# Role + Context

You are a senior research analyst conducting deep technical due diligence on
**Compounding Engineering** (CE) — a term/practice that has emerged 2024-2026 around
AI-native development workflows — for a Berlin-based AI consultancy (Jetix) building a
multi-agent operational system. The output will be used to make a critical architecture
decision: should we adopt a compounding engineering pattern as the core methodology for
our internal 12-agent operational platform?

This is **deep research**, not a summary. Depth > breadth. Specific > vague.
Multi-source > single-source. Recent (2024-2026) > older.

# Research Questions (answer ALL, in order, with specifics)

1. **Definition(s).** What exactly is "compounding engineering" as a term and as a
   practice? Provide the canonical definition(s) as used by its most prominent
   practitioners. If multiple definitions co-exist, enumerate them with attribution.
2. **Origin.** Where did the term originate? Candidates to investigate: Anthropic
   (Boris Cherny / Claude Code team), Cognition Labs (Devin), Every (Dan Shipper),
   Kent Beck, Karpathy, or community/Twitter origin. Trace first public mention with
   date + URL.
3. **Canonical practitioners.** Who are the 5-10 people most associated with CE?
   For each: name, affiliation, their most important writing/talk on CE, URL.
4. **Core patterns.** Enumerate and describe the concrete patterns CE practitioners
   invoke: (a) memory accumulation across sessions, (b) pattern reuse / skill
   creation, (c) agent specialization, (d) meta-learning / agents-improving-agents,
   (e) recursive self-improvement, (f) error → rule → skill pipeline. Define each
   with a specific example from a known practitioner.
5. **Tooling.** Which tools and platforms claim to enable CE? Cover at minimum:
   Claude Agent SDK, Claude Code, Cursor, Devin, Sweep.dev, Continue, Aider,
   Lovable, v0, Bolt. For each: what specifically do they implement that counts as
   CE, and what do they *not* implement?
6. **Production case studies.** Identify 3-5 concrete production deployments of CE
   with named results (revenue, user count, velocity metrics, error reduction, etc).
   Cite the source of each metric.
7. **CE vs "good multi-agent design".** Is there a substantive distinction between
   CE and generic multi-agent orchestration, or is CE primarily a marketing frame?
   Surface the strongest argument on each side with named advocates.
8. **Failure modes.** Where and when does CE NOT work? What are the documented
   failure patterns? Include at least 3 specific cases with post-mortem content
   (blog, talk, tweet thread) where teams or solo devs regretted adopting CE.
9. **Cost dynamics.** Quantitatively: how does CE token/$/latency spend compare to
   single-agent baselines? Anthropic's own published figures ("~15× tokens for
   multi-agent" etc) are a good anchor — find the actual source and any follow-up
   data from practitioners.
10. **Adoption curve.** Is CE currently production practice or still research/hype?
    What companies have publicly reported CE in production with customer impact?
    Distinguish internal tooling vs customer-facing.
11. **Solo-founder applicability.** Is CE viable for a solo developer + Claude Code,
    or does it require team scale? Find case studies specifically on the solo scale.
12. **Metaphor analysis.** "Compounding" is borrowed from Buffett (financial) and
    Naval (leverage). How accurate is the metaphor technically? Where does it break?
    Find critiques of the metaphor itself.
13. **Measurement.** What metrics do CE practitioners use to measure the "compounding
    effect"? (Velocity deltas across months? Error rate per task over time? Skill
    count growth?) Give named practitioner + their specific metric.
14. **Failure post-mortems.** Find 2-3 publicly-documented post-mortems where CE
    approaches were abandoned or rolled back. Transparency examples preferred.
15. **Future direction.** Where do CE practitioners predict the practice is headed
    2026-2027? Cite concrete predictions with attribution (who, when, URL).

# Required Output Format

Structure your response as a **structured markdown report** with these sections:

## Executive Summary (300-500 words)

Single-paragraph synthesis answering: What is CE, who practices it, does it work,
should a solo Berlin AI consultancy adopt it? Then top 5 key findings as a bullet list.

## Section 1 — Definition, Origin, Canonical Practitioners

Answer Q1-Q3. Give a crisp definition (or enumerate competing definitions); trace
first public mention with date + URL; list 5-10 canonical practitioners with links.

## Section 2 — Core Patterns of Compounding Engineering

Answer Q4. Enumerate patterns (a)-(f) with concrete examples. Include code/workflow
snippets where findable.

## Section 3 — Tooling Landscape

Answer Q5. Platform-by-platform: Claude Code, Claude Agent SDK, Cursor, Devin,
Sweep.dev, Continue, Aider, plus any others. Map each to CE patterns implemented.

## Section 4 — Production Case Studies

Answer Q6, Q10. Named companies, named metrics, cited sources. Internal tooling
vs customer-facing distinction.

## Section 5 — Critical Assessment

Answer Q7, Q8, Q12, Q14. Is CE substantive or marketing? Failure modes (≥3).
Metaphor critique. Post-mortems.

## Section 6 — Economics & Adoption

Answer Q9, Q11, Q13. Token/$/latency economics. Solo-founder viability. Metrics
used. Adoption curve.

## Section 7 — Future Direction

Answer Q15.

## Specific Production Examples

Aggregate 5+ named entities (companies/products/people) from above sections with
URLs and 1-2 line descriptor each. Bulleted list for easy scanning.

## Critical Assessment

- **Pros** (specific, evidence-backed, source-cited)
- **Cons + failure modes** (specific, evidence-backed, source-cited)
- **When to use vs avoid** (decision rules with rationale)

## Comparison к Anthropic ecosystem

How CE relates specifically to Claude / Claude Code / Claude Agent SDK. Is
Anthropic officially endorsing CE? Have Anthropic researchers written about it?

## Sources List

Numbered list of ALL URLs cited inline, with author + publication date when
available. Format: `[N] Author, "Title" (Publication, YYYY-MM-DD). URL`.

# Quality Requirements

- **Citations inline** ([1], [2], etc) + full URL list at end
- **Multi-source:** minimum 5 different sources, prefer 10+
- **Specificity:** "Devin uses LangGraph for orchestration" NOT "Devin uses some framework"
- **Critical lens:** include pros AND cons, NOT marketing claims as truth
- **Recency:** prefer 2024-2026 sources (acceptable: 2023 if foundational)
- **Authoritative sources:** academic papers, founder blog posts, podcast transcripts,
  github repos, official documentation > random blog spam
- **Verbatim quotes:** when source makes claim, quote it directly (don't paraphrase)
- **Length:** comprehensive — likely 10-30 pages markdown when copied to file

# What to AVOID

- Marketing fluff ("revolutionary", "game-changing" without evidence)
- Generic "AI agents are powerful" prose
- Single-source dependencies (one blog post citation = insufficient)
- Aged sources (pre-2023 unless foundational paper)
- Speculation without source attribution
- Conflating "compounding engineering" with generic "continuous improvement" or
  "DevOps" (they are different — preserve the distinction and interrogate it)
