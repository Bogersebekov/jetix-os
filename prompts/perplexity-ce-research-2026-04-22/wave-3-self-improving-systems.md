---
type: perplexity-research-prompt
wave: 3
topic: Self-improving / recursive agent systems — meta-agents, SPL, Constitutional AI
created: 2026-04-21
target: Perplexity Pro Search (Comet desktop or web)
estimated-perplexity-time: 5-15 min
output-target: raw/research/compounding-engineering-2026-04-22/R-3-self-improving-systems.md
---

# Perplexity Prompt — Wave 3: Self-Improving / Recursive Systems

## Instructions для Ruslan (НЕ для Perplexity)

1. Откройте Perplexity (Comet desktop или Pro web — https://perplexity.ai)
2. Включите **Pro Search mode** (deep research, НЕ Quick Search)
3. Скопируйте всё ниже разделителя `═══` в Perplexity
4. Дождитесь completion (5-15 min)
5. Optional: задайте 2-3 follow-up questions (см. ниже)
6. Сохраните output в `raw/research/compounding-engineering-2026-04-22/R-3-self-improving-systems.md`

## Recommended follow-up questions (после initial answer)

1. "What's the canonical production example of recursive agent self-improvement
   today? Give me name + architecture + measurable improvement curve."
2. "What goes wrong when agents try to improve themselves? Documented incidents
   of drift, degradation, or over-fitting in production."
3. "Is there a 'System Prompt Learning' paper or repo I can study directly?
   Karpathy's original formulation — where is it exactly?"

═══════════════════════════════════════════════════════════════════
THE PROMPT (copy below this line into Perplexity)
═══════════════════════════════════════════════════════════════════

# Role + Context

You are a senior research analyst conducting deep technical due diligence on
**self-improving and recursive agent systems** for a Berlin-based AI consultancy
(Jetix) building a multi-agent operational system. The output will be used to make a
critical architecture decision: should Jetix's meta-agent actively improve other agents'
system prompts and skill libraries over time (weekly/monthly cycles)?

This is **deep research**, not a summary. We are NOT asking about AGI or speculative
recursive self-improvement. We are asking about **practical, production-grade agent
improvement loops** that work today in 2024-2026.

Depth > breadth. Specific > vague. Multi-source > single-source. Recent > older.

# Research Questions (answer ALL, in order, with specifics)

1. **Definition in production context.** What does "self-improving agent system"
   mean in practice today (2024-2026)? Draw a clear line between (a) AGI hype /
   recursive self-improvement theory, and (b) concrete operational patterns shipping
   in production. Focus on (b).
2. **System Prompt Learning (SPL).** How does an agent accumulate patterns into its
   own system prompt? Cite Karpathy's original formulation (essay, tweet, talk —
   URL + date). Find production implementations that do this (Claude Code skills,
   Cursor rules, other).
3. **Constitutional AI mechanism.** Explain Anthropic's Constitutional AI
   technically: CAI paper, RLAIF, principles-based self-critique. What is the
   current 2025-2026 evolution (e.g., IBC, Claude's character)? Cite the primary
   papers with URLs.
4. **RLHF / DPO / iterative refinement.** Summarize post-training improvement
   techniques relevant to agent systems (not base models): how teams iteratively
   refine agent behavior in production. Name companies doing this + public details.
5. **Meta-agents that audit other agents.** Production cases of agent-A that
   reviews/audits/improves agent-B's outputs or prompts. Find 3-5 named examples
   with architectural details.
6. **Skill creation patterns.** How are "skills" (reusable agent capabilities)
   created — automated extraction vs human curation? Who does which? Specifically:
   Claude Code's skills system, Cursor rules, GitHub Copilot custom instructions,
   Every/Cora subagent creation — compare the creation lifecycle.
7. **Karpathy's writings.** Collect Andrej Karpathy's relevant essays/talks/tweets
   on agent improvement, Software 2.0/3.0, System Prompt Learning. For each:
   title, date, URL, key idea in 1-2 sentences.
8. **Failure modes of self-improvement.** Documented cases of recursive
   degradation, drift, over-fitting to narrow task distributions, or catastrophic
   forgetting during prompt evolution. Cite specific incidents.
9. **Production wins.** 5+ named production deployments where self-improving loops
   demonstrably improved agent performance over time. Include the metric + time
   horizon + source.
10. **Measurement.** How do teams measure "self-improvement" in agents? Task
    success rate deltas? Skill count growth? Reduced human-correction rate?
    Name metric + practitioner + URL for each.
11. **Time horizons.** Daily / weekly / monthly / quarterly improvement cycles —
    what's the reported optimal cadence? Cite examples.
12. **Human-in-loop vs fully autonomous improvement.** Production systems run the
    spectrum from fully-manual (human curates every skill) to fully-autonomous
    (agent writes its own skills). Map 3-5 named systems onto this spectrum with
    justification.
13. **Anthropic vs OpenAI vs Cognition approaches.** Each lab's philosophy on
    agent self-improvement — compare explicitly with citations. Who is most
    permissive? Who most conservative?
14. **Solo founder applicability.** Can a solo dev + Claude Code run a
    self-improvement loop at small scale? Find 2-3 blog posts from solo devs
    documenting their setup + results.
15. **Critique applicable here.** Anatoly Levenchuk (Russian systems-thinking
    school) has argued "agents don't strategize" — does that critique apply to
    self-improving agents? Find his actual formulations with URL, then map to
    this context.

# Required Output Format

Structure your response as a **structured markdown report** with these sections:

## Executive Summary (300-500 words)

Single-paragraph synthesis + top 5 key findings.

## Section 1 — Definition: Production Self-Improvement vs AGI Hype

Answer Q1. Draw the line clearly. Cite voices from both camps.

## Section 2 — Core Mechanisms

Answer Q2, Q3, Q4. System Prompt Learning; Constitutional AI; RLHF/DPO in agent context.

## Section 3 — Meta-Agents & Skill Creation Patterns

Answer Q5, Q6, Q12. Agent-auditing-agent; skill creation lifecycle; human-in-loop spectrum.

## Section 4 — Karpathy & Canonical Writings

Answer Q7. Karpathy essays/talks/tweets with dates and URLs.

## Section 5 — Production Case Studies & Metrics

Answer Q9, Q10, Q11. Named production wins with metrics and time horizons.

## Section 6 — Failure Modes & Critique

Answer Q8, Q15. Drift, over-fitting, degradation. Levenchuk critique mapped.

## Section 7 — Philosophies Compared + Solo Applicability

Answer Q13, Q14. Anthropic vs OpenAI vs Cognition; solo-founder setup examples.

## Specific Production Examples

5+ named entities/products/papers/people with URLs, 1-2 line descriptor each.

## Critical Assessment

- **Pros** (when self-improvement helps — evidence-backed)
- **Cons + failure modes** (drift, over-fitting, recursive degradation — evidence-backed)
- **When to use vs avoid** (explicit decision rules with rationale)

## Comparison к Anthropic ecosystem

How does Claude / Claude Code / Claude Agent SDK support (or constrain)
self-improvement loops? What are the official Anthropic best practices?

## Sources List

Numbered list of ALL URLs cited inline, with author + date when available.
Format: `[N] Author, "Title" (Publication, YYYY-MM-DD). URL`.

# Quality Requirements

- **Citations inline** ([1], [2], etc) + full URL list at end
- **Multi-source:** minimum 5 different sources, prefer 10+
- **Specificity:** "Claude Code skills loaded from ~/.claude/skills/ via markdown frontmatter"
  NOT "Claude has skills somewhere"
- **Critical lens:** include pros AND cons
- **Recency:** prefer 2024-2026 (acceptable: 2023 if foundational — e.g., original CAI paper)
- **Authoritative sources:** research papers, Karpathy writings, Anthropic/OpenAI docs,
  founder blog posts > random blog spam
- **Verbatim quotes:** when source makes claim, quote it directly (don't paraphrase)
- **Length:** comprehensive — likely 10-30 pages markdown when copied to file

# What to AVOID

- AGI / recursive-self-improvement sci-fi framing (we want production reality)
- Marketing fluff
- Generic "agents learn" prose with no mechanism
- Single-source dependencies
- Aged sources (pre-2023 unless foundational — e.g., original CAI paper is acceptable)
- Speculation without source attribution
- Conflating base-model training (RLHF on LLM weights) with agent-level improvement
  (system prompts, skills, rules) — these are different; preserve the distinction
