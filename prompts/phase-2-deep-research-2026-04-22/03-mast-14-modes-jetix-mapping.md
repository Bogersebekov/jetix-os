---
id: phase-2-03-mast-14-modes-jetix-mapping
title: MAST 14 Failure Modes × Jetix Agent Matrix — Perplexity Deep Research
author: cloud-cowork
date: 2026-04-22
tool: Perplexity Pro Deep Research
priority: P1
gap-coverage: Domain 7 MAJOR #1 (EU AI Act + compliance audit), Domain 7 MINOR #1 (MAST cross-reference)
related-locks: Decision 15 (revenue-gated compliance), Phase 4 baseline swarm readiness
status: ready-to-run
---

# MAST 14-Mode Failure Matrix × Jetix Agents — Perplexity Deep Research Prompt

## Как использовать

1. Открой Perplexity Pro в **Deep Research** режиме
2. Скопируй блок ниже от `===BEGIN PROMPT TO PASTE===` до `===END PROMPT TO PASTE===`
3. Paste + submit. Wait 25-35 минут (synthesis-heavy).
4. Сохрани output в `raw/research/phase-2-deep-research-2026-04-22/RESULT-03-mast-matrix.md`
5. Скажи Cloud Cowork — начнётся Phase 3 synthesis.

## Context для понимания (не копируй в Perplexity)

MAST (Multi-Agent System failure Taxonomy) из Cemri et al. "Why Do Multi-Agent LLM Systems Fail?" arXiv:2503.13657 идентифицирует 14 failure mode'ов на основе 1,600+ production traces с 7 frameworks. Jetix Phase 4 baseline swarm construction требует failure-mode-by-agent preventive matrix — иначе recursive-swarm усилит latent MAST-режимы (Kim et al. 17.2× error amplification).

Prompt асимметричный: **Perplexity делает research по MAST + prevention literature (НЕ делает Jetix-specific mapping — Jetix-mapping делает потом Cloud Cowork/synthesizer)**. Здесь нужна evidence-based база per MAST mode: definitions, documented failures, prevention mechanisms with cost/accuracy tradeoffs, 2025-2026 latest primary sources.

Связанные уже-имеющиеся материалы (не повторять):
- R-4 failure-modes-critique (616 lines) — MAST упомянут, но нет full 14-mode treatment
- Perplexity Apr 22 Domain 6 (15 anti-patterns + 6 post-mortems) — concrete cases, но не MAST-структурно
- Kim et al. arXiv:2512.08296, Walden Yan "Don't Build Multi-Agents", Agentic Misalignment Anthropic Jun 2025, Folkman context collapse — уже captured

---

## ===BEGIN PROMPT TO PASTE===

I need a deep production-grade research on the **MAST (Multi-Agent System failure Taxonomy)** from Cemri et al. "Why Do Multi-Agent LLM Systems Fail?" (arXiv:2503.13657, Mar 2025) — specifically: a per-mode complete reference with definitions, production examples, prevention mechanisms, and evidence-based recommendations. This is for architectural audit of an 11-agent multi-agent system before Phase 4 production launch. Cite every claim. Prefer 2025-2026 primary sources. Admit uncertainty.

## Background

The MAST paper analyzed 1,600+ traces across 7 multi-agent frameworks (MetaGPT, ChatDev, AG2, HyperAgent, Multi-Agent Collaboration, AppWorld, Magentic-One) and identified **14 failure modes** grouped into 3 categories:

- **Category 1: Specification and System Design** (5 modes) — disobey task spec, disobey role spec, step repetition, loss of conversation history, unaware of termination conditions
- **Category 2: Inter-Agent Misalignment** (7 modes) — conversation reset, fail to ask for clarification, task derailment, information withholding, ignored other agent's input, action-reasoning mismatch, premature termination
- **Category 3: Task Verification and Termination** (2 modes) — no or incomplete verification, incorrect verification

**If my enumeration of MAST 14 modes above is inaccurate, correct it from the paper and proceed with the corrected list.** I want the true MAST taxonomy as published, not my possibly-misremembered version.

## Research scope

For **each of the 14 MAST failure modes**, produce a standardized per-mode dossier. This is the primary deliverable. Additionally, produce 4 cross-cutting deliverables (C1-C4) at the end.

### Per-mode dossier structure (repeat 14 times, one per mode)

For each of the 14 MAST modes, produce:

**1. Canonical definition** — the MAST paper's definition, verbatim where possible, with section reference.

**2. Category and severity** — MAST category 1/2/3; severity rating from the paper (if provided); percentage of traces in Cemri et al. showing this mode.

**3. Concrete production examples (2-3 documented cases)**

For each case: what system, what happened, source link. Bias toward 2025-2026 primary sources. Must include cases from outside the MAST paper itself — post-2025 production reports. Examples to draw from:

- Anthropic public post-mortems (e.g., agentic misalignment Jun 2025, Claude Code incidents)
- OpenAI outage reports referencing agent behavior
- DeepMind "Science of Scaling Agent Systems" Dec 2025
- CrewAI 2B executions lessons (blog.crewai.com/lessons-from-2-billion-agentic-workflows)
- Replit Agent post-mortems (database deletion Jul 2025)
- AutoGen / Microsoft Agent Framework 1.0 issue threads on GitHub
- LangGraph / LangChain production post-mortems
- Devin post-mortems (the 13.86% SWE-bench, "last 30% problem")
- Cognition / Walden Yan "Don't Build Multi-Agents" specifics
- Hacker News threads where practitioners self-report

**4. Prevention mechanisms documented in literature**

Enumerate 2-5 documented prevention mechanisms with evidence. For each:

- Mechanism name and one-sentence description
- Reference implementation (paper / framework / production-deployed system)
- Cost profile (qualitative: cheap/moderate/expensive in tokens, engineering time, latency)
- Evidence quality (RCT / measured in production / anecdotal / theoretical)
- Known limitations or failure of the prevention mechanism itself
- Concrete citations

**5. Evidence-based recommendation for a solo-founder 11-agent system**

Given the cost of each prevention mechanism, what is the evidence-supported recommendation for a solo-founder-scale 11-agent production system operating on a modest budget (€500-2000/mo inference)? Specifically:

- Which prevention mechanism has the best evidence?
- Which prevention mechanism is most cost-effective?
- Which prevention mechanism is "overkill" at this scale?
- What's the minimum-viable mitigation?

**6. Jetix-relevant trigger context (the questioner will apply this to their agents — just identify typical triggers)**

Identify the types of agent roles or task shapes most susceptible to this failure mode. Examples: "hub coordinator agents" are especially prone to mode X; "verifier agents" are especially prone to mode Y; "long-running autonomous research agents" to mode Z. This helps the reader map the mode to their agent roster without you needing to know the roster.

**7. Open research questions / uncertainty**

What's genuinely unknown or contested in the 2025-2026 literature about this mode? Where do Cemri et al., Kim et al., DeepMind, Anthropic, CrewAI data disagree?

### Cross-cutting deliverables

#### C1. Failure-mode cascade analysis

MAST modes do not occur in isolation — they often cascade. Which pairs / triples of MAST modes most commonly co-occur in Cemri et al.'s dataset and in 2025-2026 production post-mortems? Example: "conversation reset" + "loss of conversation history" + "premature termination" as a known cascade. Produce a cascade table with frequency data where available.

#### C2. Prevention-mechanism ROI ranking

Across all 14 modes, rank the top 10 prevention mechanisms by expected ROI for a solo-founder-scale system (cost vs. incident-reduction). Cite evidence.

Candidates to rank (expand beyond this list):
- Structured JSON schema for inter-agent messages
- Per-agent working-memory file (scratchpad.md pattern)
- Message-ledger / mailbox persistence (JSONL)
- Role-specification in every sub-agent system prompt
- Explicit termination conditions in every agent contract
- Verification-agent per sub-task (Every Cora 12-reviewer pattern)
- Hard turn-limits / recursion-depth caps
- Cost caps at the billing provider level
- Human-in-loop gate at each phase transition
- Constitutional AI critique-revise layer
- Eval harness running on every change (Promptfoo / Langfuse)
- Deterministic hooks (`.claude/hooks`) vs. advisory CLAUDE.md
- Context compression / ACE append-only structured entries
- Periodic full-context re-grounding vs. rolling summary
- Strict single-agent default with escalation to multi-agent only when simpler solutions demonstrably fail

#### C3. Compliance and regulatory overlay

Map each of the 14 MAST modes to:

- EU AI Act tier implications (Article 14 human oversight; Article 26 transparency; "high-risk" vs "limited-risk" classification)
- GDPR Article 17 (right to erasure) implications if the failure mode causes persistent data misuse
- Article 22 (automated decisions, WP251rev.01) implications where a failure affects human data subjects
- DACH / Germany-specific legal implications (BDSG, DS-Anpassungs-G) if distinct
- UK AI white paper Oct 2025 framing
- US OMB M-24-10 / executive order context
- Concrete documentation templates a Berlin-based GmbH would need in its DPIA

**Specific question**: which MAST modes, when they materialize in a customer-facing agent, trigger EU AI Act "high-risk" re-classification? Which are benign?

#### C4. Benchmark re-run status for post-2025 models

The MAST paper was based on traces from models available in Mar 2025 (Claude 3.5 Sonnet, GPT-4, Gemini 1.5 era). The 45% capability threshold and 17.2× error amplification from Kim et al. were similarly dated.

- Has anyone re-run the 14-mode taxonomy frequency analysis on GPT-5, Claude Opus 4.x, Gemini 2.5 Pro, Llama 4 — and what shifted?
- Did any MAST modes become less frequent (e.g., long-context reduces loss-of-conversation-history)?
- Did any become more frequent (e.g., more autonomous agents amplify task-derailment)?
- Has anyone published a 2025-2026 update to MAST taxonomy itself (e.g., adding new failure modes observed with Opus 4.x reasoning loops)?

## Output requirements

- **For each of the 14 MAST modes**: the 7-field dossier above, 300-800 words each
- **Cross-cutting C1-C4**: each 500-1500 words
- **Final summary table**: 14 rows (modes) × 6 columns (category / severity / top prevention / cost / compliance flag / post-2025 status change)
- **Top 10 prevention actions** a solo-founder building an 11-agent system should take in priority order, with citation
- **Honest assessment**: which of the 14 modes are structurally unsolvable in a solo-founder budget, which are mitigable, which are table-stakes-already-mitigated-in-Claude-Code-baseline
- **Length target**: 15,000-25,000 words (this is a reference artifact, not a summary)
- **Citations**: every claim; primary > secondary; flag 2023-2024 as potentially outdated; flag 2025-2026 as current

## Constraints

- Prefer arXiv, engineering blogs, conference talks, framework-maintainer statements
- If a prevention mechanism has no evidence beyond blog claims, say so
- If the MAST paper has been cited-and-corrected, surface the correction
- If a later paper supersedes MAST (e.g., DeepMind's "Science of Scaling" Dec 2025 proposes a different taxonomy), flag the overlap and disagreements
- No hype; flag any vendor claim that cannot be independently verified

## Required primary sources to consult (not exhaustive)

- Cemri et al. arXiv:2503.13657 (the MAST paper itself)
- Kim et al. arXiv:2512.08296 (Dec 2025, 180 experiments, 17.2× amplification)
- DeepMind "Towards a Science of Scaling Agent Systems" Dec 2025
- Anthropic "Building Effective Agents" (Dec 2024)
- Anthropic "How we built our multi-agent research system" (Jun 2025)
- Anthropic "Agentic Misalignment" (Jun 2025)
- CrewAI "Lessons from 2 Billion Agentic Workflows" (Jan 2026)
- Walden Yan / Cognition "Don't Build Multi-Agents"
- Folkman Oct 2025 context collapse (66.7% → 57.1%)
- Stanford ACE (Agentic Context Engineering) paper
- Anthropic "Constitutional Classifiers" Feb 2025 (86% → 4.4% jailbreak)
- AutoGen / Microsoft Agent Framework 1.0 migration notes
- LangChain / LangGraph production post-mortems (Octoclaw etc.)
- EU AI Act official text (high-risk Annex III), Article 14, Article 26
- GDPR Articles 17, 22
- Anthropic Claude Code engineering post series
- Replit Agent post-mortem (Jul 2025 database deletion, Reddit r/Futurology)
- OpenAI Agents SDK docs + GitHub issues
- $47K API incident (dev.to Utibe Okodi Mar 2026)

## ===END PROMPT TO PASTE===

---

## Alternative: split into 3 focused prompts (optional)

If the single mega-prompt returns uneven depth:

1. **Prompt A — MAST 14 modes dossiers (modes 1-7)** — ~20 min Deep Research
2. **Prompt B — MAST 14 modes dossiers (modes 8-14)** — ~20 min Deep Research
3. **Prompt C — Cross-cutting C1-C4 + top-10 prevention** — ~15 min Deep Research

## After Perplexity returns

1. Save raw output to `raw/research/phase-2-deep-research-2026-04-22/RESULT-03-mast-matrix.md`
2. Flag Cloud Cowork — Phase 3 synthesis will produce the Jetix-specific matrix: 14 MAST modes × 11 Jetix agents × current mitigation coverage × residual risk × compliance implications.
3. Jetix-specific mapping (NOT done by Perplexity, done by synthesis layer) will cross-reference:
   - `.claude/agents/*.md` roster (agent definitions)
   - `design/AGENT-PROTOCOLS.md` (per-agent protocols)
   - `decisions/JETIX-ARCHITECTURE-BRIEF.md` Q2 (agent roster reconciliation), Q6 (compliance membrane), Q13 (escalation routing)
   - `R-4-failure-modes-critique.md` (existing Jetix-specific analysis)
4. Output of Phase 3 synthesis: `design/MAST-JETIX-MATRIX-v1.md` — per-agent × per-mode × current mitigation × residual risk × compliance flag.

---

*END PROMPT 03 — MAST 14 Modes × Jetix Matrix*
