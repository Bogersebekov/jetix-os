---
type: perplexity-research-prompt
wave: 11
topic: Evals — frameworks (Anthropic/OpenAI/LangSmith/Inspect AI/Braintrust), benchmarks (SWE-bench/AgentBench/GAIA), LLM-as-judge, Jetix application
created: 2026-04-21
target: Perplexity Pro Search (Comet desktop or web)
estimated-perplexity-time: 5-15 min
output-target: raw/research/compounding-engineering-2026-04-22/R-11-evals.md
---

# Perplexity Prompt — Wave 11: Evals — agent quality measurement frameworks

## Instructions для Ruslan (НЕ для Perplexity)

1. Откройте Perplexity (Comet desktop или Pro web — https://perplexity.ai)
2. Включите **Pro Search mode** (deep research, НЕ Quick Search)
3. Скопируйте всё ниже разделителя `═══` в Perplexity (включая `# Role + Context` и ниже)
4. Дождитесь completion (5-15 min)
5. Optional: задайте 2-3 follow-up questions (см. ниже) для probing depth
6. Сохраните output в `raw/research/compounding-engineering-2026-04-22/R-11-evals.md`

## Recommended follow-up questions (после initial answer)

1. "Build me a minimal eval setup для a solo founder с 11 Claude agents — concrete
   tool choices + workflow + CI/CD integration, нет abstraction, just ship-able
   steps."
2. "How do I avoid eval gaming and Goodhart's law failure когда LLM-as-judge
   evaluates my LLM-agent outputs? Specific mitigation techniques from production
   teams."
3. "Show me Anthropic's published eval methodology для their own products (Claude
   Code, Claude API) — what do they actually measure internally, по published
   sources?"

═══════════════════════════════════════════════════════════════════
THE PROMPT (copy below this line into Perplexity)
═══════════════════════════════════════════════════════════════════

# Role + Context

You are a senior research analyst conducting deep technical due diligence on
**evals (evaluations) для LLM agents and agent systems** — frameworks, benchmarks,
LLM-as-judge best practices, production patterns — for a Berlin-based AI
consultancy (Jetix) building a multi-agent operational system (currently 11
Claude-based agents across 6 departments). The output will be used to make a
critical architecture decision: **what minimum viable eval setup should Jetix
implement Phase 1 to measure (a) the quality of each of the 11 agents, (b) D-level
document writing quality, and (c) compound learning / improvement over time?**

Jetix-specific eval targets:
- 11 agents across departments (manager, personal-assistant, system-admin, sales-
  lead, sales-researcher, sales-outreach, inbox-processor, crazy-agent, knowledge-
  synth, strategist, life-coach, meta-agent)
- D-document writing (replacing manual Stage B reviewers)
- FPF (First-Principle Framework) compliance в agent outputs
- Compound learning (improvement metrics over months)

This is **deep research**, not a summary. Depth > breadth. Specific > vague.
Multi-source > single-source. Recent (2024-2026) > older. Production patterns
and case studies strongly preferred over vendor marketing.

# Research Questions (answer ALL, in order, with specifics)

1. **Canonical definition of "evals" в LLM/agent context.** What distinguishes
   evals from traditional unit tests, integration tests, QA testing? Historical
   origin of the term (OpenAI Evals repo 2023? earlier?). Cite URLs.
2. **Eval types taxonomy.** Describe each, when to use which:
   - Deterministic (exact-match, regex, schema validation)
   - Reference-based (BLEU, ROUGE, BERTScore)
   - LLM-as-judge (single-model, ensemble, pairwise)
   - Human-in-loop (SME review, crowd-sourced)
   - A/B testing (production traffic comparison)
   - Multi-turn / trajectory evaluation (agent sequences)
   - Rubric-based scoring (multi-dimensional)
   Empirical correctness of each type (where each breaks down).
3. **Latest 2024-2026 frameworks — deep dive each.** Per framework: architecture,
   strengths, weaknesses, pricing/licensing, integration pattern, maturity
   indicators (GitHub stars, production adopters):
   - **Anthropic Evals** (if released as separate product — else Anthropic Console
     evals)
   - **OpenAI Evals** (github.com/openai/evals) + OpenAI API evals feature
   - **LangSmith** (LangChain ecosystem) — evaluators + production monitoring
   - **LangFuse** — open source observability + evals
   - **Promptfoo** (promptfoo.dev) — CLI-first eval framework
   - **DeepEval** (github.com/confident-ai/deepeval) — pytest-like
   - **Inspect AI** (UK AI Safety Institute, inspect.ai-safety-institute.org.uk) —
     research-grade
   - **Braintrust** (braintrust.dev) — commercial SaaS
   - **Humanloop** (humanloop.com) — workflow integration
   - **Helicone** (helicone.ai) — observability + evals
   - **Phoenix / Arize** (phoenix.arize.com) — open source
   - **Galileo** (galileo.ai) — agent evaluation specifically
   - **Ragas** (ragas.io) — RAG-specific evaluation
   - **TruLens** (trulens.org) — Snowflake ecosystem
4. **Benchmarks для agent quality.** Deep dive each:
   - **SWE-bench / SWE-bench Verified** (coding agent benchmark)
   - **MMLU** / **MMLU-Pro** (general knowledge)
   - **HumanEval** / **MBPP** (code)
   - **AgentBench** (Liu et al. multi-env)
   - **ToolLLM / ToolBench**
   - **GAIA** (General AI Assistant benchmark)
   - **OSWorld** / **WebArena** / **VisualWebArena** (web/desktop agents)
   - **MLE-bench** (ML engineering, OpenAI)
   - **τ-bench** (tau-bench, tool use w/ user simulation)
   - **BrowseComp** (if exists)
   Strengths, weaknesses, what each does/doesn't measure, contamination status.
5. **LLM-as-judge — deep dive.**
   - Best practices для prompt design (rubric specification, reference anchoring,
     chain-of-thought, calibration)
   - Known biases: position bias, length bias, self-enhancement bias, verbosity
     preference, sycophancy, style-over-substance bias
   - Calibration techniques (few-shot anchoring, pairwise forcing, debiasing
     rounds)
   - Multi-judge ensembles vs single judge — empirical comparison
   - When LLM-as-judge fails categorically vs succeeds (vs human baseline
     correlation studies)
   - Cited sources: "Judging LLM-as-a-Judge" (Zheng et al.), recent 2024-2026
     papers на judge reliability
6. **Agent trajectory evaluation.** How to evaluate multi-step reasoning, tool-use
   correctness, sub-agent coordination quality, partial credit. Specific
   techniques: trajectory overlap, key-action matching, goal achievement scoring,
   counterfactual evaluation. Named frameworks that do this well.
7. **Production eval pipelines.** How production teams build eval systems: offline
   golden sets, CI/CD integration (pre-deploy gates), shadow traffic, production
   monitoring, regression detection, drift alerts. Concrete architectures from
   published engineering blogs.
8. **Real production case studies (5+ named systems с metrics).**
   - **Anthropic** — how they eval Claude (published methodology, AI Safety Level,
     RSP testing)
   - **Cognition Labs / Devin** — how Devin is evaluated (SWE-bench + internal)
   - **Cursor** — eval approach (published or inferred from blog)
   - **Replit Agent** — eval approach
   - **Sweep / Aider** — open benchmarks they run
   - **OpenAI** — eval для GPT models (simple-evals, system cards)
   - **Google DeepMind** — Gemini eval methodology
   - Additional named teams (Harvey, Sierra, Decagon, Klarna AI) if data available
9. **Failure modes в evals themselves.** Eval gaming, Goodhart's law ("target
   becomes measure becomes target"), dataset contamination (eval set leaked into
   pretraining), eval-train leakage, sycophancy в LLM-judges, rubric overfit.
   Named cases с published post-mortems.
10. **Cost dynamics.** Typical ratio eval tokens : production tokens. Cost of LLM-
    as-judge at scale (per evaluation cycle). Cost of running SWE-bench full. How
    teams control eval cost в CI/CD.
11. **Solo-founder applicable setup.** Minimum viable eval setup для Jetix Phase 1
    (no dedicated eval team, 11 agents, limited budget). Concrete tool choice +
    golden set size + CI integration + frequency. What's realistic vs aspirational.
12. **Specific Jetix application — concrete recommendations для each eval target:**
    - **Per-agent eval:** how to evaluate each of the 11 agents (manager,
      knowledge-synth, strategist, meta-agent, sales-lead, life-coach etc) — what
      to measure для each type (what's different between evaluating sales-researcher
      vs meta-agent vs life-coach)?
    - **D-document eval:** how to evaluate D-document writing quality (instead of
      manual Stage B reviewers) — rubric dimensions, judge model choice,
      calibration approach
    - **Compound learning eval:** how to measure improvement over time — velocity
      metrics, error rate decay, skill count growth, which actually correlate с
      real value
    - **FPF compliance eval:** how to verify First-Principle Framework compliance
      в agent outputs — rubric-based LLM-judge? deterministic structural check?
13. **Integration с Claude Agent SDK / Claude Code.** Native eval features (if
    any). Anthropic Console evals capabilities. How to wire evals into Claude Code
    hooks / skills / CLAUDE.md workflow. Concrete integration pattern.
14. **Eval-driven development pattern.** Does "EDD" apply к agent system
    development the way TDD applied to traditional code? Named practitioners who
    advocate this (Hamel Husain, Shreya Shankar, Eugene Yan и др). Their concrete
    workflows.
15. **Open questions / unsolved problems в agent evals 2026.** Where does the field
    currently lack good answers? (Multi-turn reward shaping, trajectory credit
    assignment, cross-agent coordination eval, long-horizon eval cost, judge-model
    circularity.) Cite researchers acknowledging these gaps.

# Required Output Format

Structure your response as a **structured markdown report** with these sections:

## Executive Summary (300-500 words)

Synthesis: what are evals 2026, which frameworks dominate, what's the minimum viable
setup для a solo founder with 11 Claude agents, top risks (gaming / contamination /
judge bias). Top 5 key findings as bullet list.

## Section 1 — Definitions & Eval Types

Answer Q1, Q2. What is "evals", distinction from testing, taxonomy с trade-offs.

## Section 2 — Frameworks Deep Dive

Answer Q3. Per-framework: architecture, strengths, weaknesses, pricing, maturity.
Comparison table at end of section. Cover Anthropic/OpenAI/LangSmith/LangFuse/
Promptfoo/DeepEval/Inspect AI/Braintrust/Humanloop/Helicone/Phoenix/Galileo/Ragas/
TruLens.

## Section 3 — Benchmarks Landscape

Answer Q4. SWE-bench/AgentBench/GAIA/OSWorld/WebArena/τ-bench/MLE-bench. What each
measures, contamination status, relevance для agent systems.

## Section 4 — LLM-as-Judge Best Practices

Answer Q5. Prompt design, biases, calibration, ensembles, failure categories.
Cite "Judging LLM-as-a-Judge" and 2024-2026 follow-ups.

## Section 5 — Trajectory Eval & Production Pipelines

Answer Q6, Q7. Multi-step eval techniques. Production pipeline architectures.

## Section 6 — Production Case Studies

Answer Q8. 5+ named systems с published metrics/methodology.

## Section 7 — Failure Modes & Economics

Answer Q9, Q10. Gaming, Goodhart, contamination, leakage, sycophancy. Cost ratios.

## Section 8 — Solo-Founder Setup & Jetix Application

Answer Q11, Q12. MVP setup. Per-agent eval design. D-document eval. Compound
learning eval. FPF compliance eval.

## Section 9 — Claude Ecosystem Integration & Future

Answer Q13, Q14, Q15. Claude Code/SDK integration. EDD practitioners and workflows.
Open research questions 2026.

## Specific Production Examples

5+ named systems/companies (Anthropic, Cognition, Cursor, Replit, OpenAI, DeepMind,
Harvey, Sierra etc) с URL + 1-2 line descriptor of their eval approach. Bulleted
list.

## Critical Assessment

- **Pros** of each major framework/approach (cited evidence)
- **Cons + failure modes** (cited)
- **When to use vs avoid** (decision rules для solo founder с 11 Claude agents)

## Comparison к Anthropic ecosystem

How each framework integrates (or doesn't) with Claude API / Claude Code / Claude
Agent SDK. Anthropic Console evals scope and limits. Native vs external trade-off
для a team already committed to the Claude stack.

## Sources List

Numbered list of ALL URLs cited inline, с author + publication date when available.
Format: `[N] Author, "Title" (Publication, YYYY-MM-DD). URL`.

# Quality Requirements

- **Citations inline** ([1], [2], etc) + full URL list at end
- **Multi-source:** minimum 5 different sources, prefer 10+
- **Specificity:** "Braintrust charges $X per eval run, supports LangChain tracing,
  integrates with pytest via braintrust-py" NOT "Braintrust is a commercial eval
  platform"
- **Empirical > vendor claims:** benchmark paper numbers > marketing site claims
- **Critical lens:** every framework has failure modes — surface them
- **Recency:** 2024-2026 sources primary (2023 acceptable для foundational "Judging
  LLM-as-a-Judge" paper)
- **Authoritative sources:** arXiv papers, framework GitHub repos (check commit
  activity и stars), founder blog posts, Hamel Husain / Shreya Shankar / Eugene
  Yan practitioner writing, Anthropic/OpenAI official docs > random Medium posts
- **Verbatim quotes:** when Anthropic publishes methodology, quote it directly
- **Length:** comprehensive — likely 10-30 pages markdown

# What to AVOID

- Vendor marketing ("best eval platform", "100% accurate judge") without evidence
- Generic "test your LLM" advice without naming frameworks/benchmarks
- Conflating "evals" с "monitoring" — related but distinct (evals are controlled;
  monitoring is passive)
- Conflating "benchmarks" с "custom evals" — both matter but serve different
  purposes
- Single-source dependencies (one LangChain blog post = insufficient)
- Aged sources (pre-2023 unless foundational like BLEU/ROUGE context)
- Missing Anthropic-specific eval tooling (if Anthropic Evals or Console evals have
  been formally released — search hard, this is critical для Jetix decision)
- Treating LLM-as-judge as a silver bullet — surface biases and failures
- Speculation about internal eval methodologies at closed-source labs without source
  — flag as "undisclosed" rather than guess
