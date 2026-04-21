---
type: perplexity-research-prompt
wave: 4
topic: Failure modes + critique — where CE / swarm / self-improving NOT work
created: 2026-04-21
target: Perplexity Pro Search (Comet desktop or web)
estimated-perplexity-time: 5-15 min
output-target: raw/research/compounding-engineering-2026-04-22/R-4-failure-modes-critique.md
---

# Perplexity Prompt — Wave 4: Failure Modes + Critique

## Instructions для Ruslan (НЕ для Perplexity)

1. Откройте Perplexity (Comet desktop или Pro web — https://perplexity.ai)
2. Включите **Pro Search mode** (deep research, НЕ Quick Search)
3. Скопируйте всё ниже разделителя `═══` в Perplexity
4. Дождитесь completion (5-15 min)
5. Optional: задайте 2-3 follow-up questions (см. ниже)
6. Сохраните output в `raw/research/compounding-engineering-2026-04-22/R-4-failure-modes-critique.md`

## Recommended follow-up questions (после initial answer)

1. "What's the most damaging publicly-documented multi-agent system failure to date?
   Give me the specific case — company, date, what broke, loss magnitude."
2. "Where would you NEVER use a multi-agent / swarm / compounding architecture today?
   List the hard veto domains with reasoning."
3. "Single-agent Claude 4.6 beats multi-agent Claude 4.6 on which benchmarks? Cite
   the specific papers/reports with numbers."

═══════════════════════════════════════════════════════════════════
THE PROMPT (copy below this line into Perplexity)
═══════════════════════════════════════════════════════════════════

# Role + Context

You are a senior research analyst conducting **adversarial** due diligence on AI
multi-agent / swarm / compounding-engineering / self-improving systems. Your task is
**not** to confirm these approaches work — it is to surface everywhere they fail,
everyone who has publicly criticized them, and every documented production incident.

The consumer of this research is a Berlin AI consultancy (Jetix) deciding whether to
build its 12-agent operational system on these patterns. They already have heard the
pro-case. They need the strongest anti-case to avoid a costly architecture mistake.

This is **deep research**, not a summary. Depth > breadth. Specific > vague.
Multi-source > single-source. Recent (2024-2026) > older. Named critics with URLs > vague references.

# Research Questions (answer ALL, in order, with specifics)

1. **Documented production failures.** Find 5+ named publicly-documented production
   failures of multi-agent / swarm / CE systems. For each: company, date,
   description of failure, business impact, source URL. Post-mortems preferred.
2. **Prompt injection between agents.** What vulnerabilities exist when one agent's
   output becomes another agent's input? Find actual documented exploits (CVEs,
   security research, proof-of-concepts) published 2024-2026. Cite Simon Willison,
   HiddenLayer, PromptArmor, etc.
3. **Compound errors — quantitative.** If each agent has error rate p, multi-agent
   pipeline compounds error. Find empirical measurements: "errors compounded at
   rate X in Y-step pipeline". Name specific studies/benchmarks with numbers.
4. **Coordination overhead thresholds.** At what agent count / task complexity does
   coordination overhead exceed benefit? Cite specific observed thresholds with
   numbers (e.g., "beyond 5 agents, latency grew 4× per added agent, with no
   accuracy improvement").
5. **Sycophancy in agent reviewers.** Known failure mode: "reviewer" agents agree
   with "producer" agents rather than catching errors. Find documented cases +
   proposed mitigations. Cite Anthropic/OpenAI/academic research on AI sycophancy.
6. **Named critics of CE / swarm / self-improvement.** List publicly critical voices
   (researchers, practitioners, bloggers): Yann LeCun, Gary Marcus, François Chollet,
   Simon Willison, Timnit Gebru, Anatoly Levenchuk, Nathan Lambert, others. For each:
   their specific critique with date + URL.
7. **Levenchuk's "agents don't strategize" argument.** Full reconstruction of
   Anatoly Levenchuk's (Russian systems-thinking school) critique: why he argues
   LLM agents cannot strategize. Find his essays, lectures, posts in Russian or
   English. Steelman the argument.
8. **Public post-mortems of CE regret.** Teams or individuals who adopted CE /
   multi-agent / swarm and publicly regretted it — roll-back stories. Find 2-3 with
   URLs.
9. **Debugging difficulty.** Why are multi-agent systems hard to debug? Name
   specific pain points (nondeterminism, hidden state, cascading retries, etc) +
   specific tooling gaps. Cite production reports.
10. **Reproducibility crisis.** Same prompt produces different agent behavior —
    how bad is this for multi-agent systems specifically? Find empirical
    measurements.
11. **Latency multiplication.** UX impact when multi-agent pipelines add seconds
    or minutes to response time. Cite specific product latency numbers (Devin,
    Cursor agent mode, Cora).
12. **Single-agent baselines winning.** Find published benchmarks where a single
    powerful model (e.g., Claude 4.6 Sonnet / Opus with long context) beats a
    multi-agent pipeline on the same task. Cite papers/reports with numbers.
13. **Tooling immaturity.** State of debugging / observability / testing for
    multi-agent systems in 2025-2026. What's missing? Cite tooling-gap reports
    (Langfuse, LangSmith, Helicone, Braintrust, Phoenix, etc).
14. **Anthropic's own published warnings.** Find any official Anthropic docs,
    blog posts, or research papers that caution against multi-agent patterns or
    warn about specific risks. URLs required.
15. **Cost overruns.** Documented cases where teams adopted multi-agent and saw
    token/$/latency spend explode 5-15× without commensurate quality gains. Cite
    2-3 cases.

# Required Output Format

Structure your response as a **structured markdown report** with these sections:

## Executive Summary (300-500 words)

Single-paragraph synthesis of the adversarial case + top 5 most damaging findings.

## Section 1 — Documented Production Failures

Answer Q1, Q8, Q15. Named failures, rollbacks, cost overruns.

## Section 2 — Technical Failure Modes

Answer Q3, Q4, Q5. Compound errors (quantified), coordination overhead thresholds,
sycophancy in reviewer agents.

## Section 3 — Security: Prompt Injection Between Agents

Answer Q2. Vulnerabilities, exploits, CVEs, security researchers. Explicit threat model.

## Section 4 — Operational Pain: Debugging, Reproducibility, Latency

Answer Q9, Q10, Q11. Why these systems are hard to operate in production.

## Section 5 — Named Critics & Their Arguments

Answer Q6, Q7. Critic-by-critic: name, affiliation, specific critique, URL. Include
Levenchuk in full.

## Section 6 — Single-Agent Baselines & Tooling Immaturity

Answer Q12, Q13. When single-agent wins; tooling gaps in observability/testing.

## Section 7 — Anthropic's Own Cautions

Answer Q14. Official warnings and limitations.

## Specific Production Failures

Aggregate 5+ named failures with company, date, loss, source URL. Bulleted for
easy scanning.

## Critical Assessment

- **When multi-agent / CE / swarm FAILS** (explicit scenarios with evidence)
- **Hard veto domains** (where you should never use these patterns)
- **Yellow-flag domains** (use with extreme caution + specific mitigations)

## Comparison к Anthropic ecosystem

How do Claude Code / Claude Agent SDK mitigate (or not) these failure modes?
Does Anthropic have official guidance on avoiding pitfalls?

## Sources List

Numbered list of ALL URLs cited inline, with author + date when available.
Format: `[N] Author, "Title" (Publication, YYYY-MM-DD). URL`.

# Quality Requirements

- **Adversarial posture:** this report is about what fails, not what works
- **Citations inline** ([1], [2], etc) + full URL list at end
- **Multi-source:** minimum 5 different sources, prefer 10+
- **Specificity:** "Prompt injection via indirect tool output — PoC by Simon Willison
  2025-03" NOT "there are security issues"
- **Named entities:** every failure/critique must name people/companies/dates
- **Recency:** 2024-2026 priority
- **Authoritative sources:** security research, academic papers, founder post-mortems,
  official docs > random hot takes
- **Verbatim quotes:** when critic makes claim, quote them directly
- **Length:** comprehensive — likely 10-30 pages markdown

# What to AVOID

- Marketing fluff (even inverted — don't just say "AI is bad")
- Generic "agents have issues" prose without mechanism
- Unattributed criticism ("some say...")
- Single-source dependencies
- Aged sources (pre-2023 unless foundational)
- Strawman versions of critics (steelman their arguments)
- Conflating model-level issues (hallucination in base LLMs) with agent-architecture-level
  issues (coordination, compound errors) — preserve the distinction
