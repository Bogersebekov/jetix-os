---
id: phase-2-01-matchmaker-capability-capsule
title: Matchmaker + Capability-Capsule Production Systems — Perplexity Deep Research
author: cloud-cowork
date: 2026-04-22
tool: Perplexity Pro Deep Research
priority: P1
gap-coverage: Domain 2 MAJOR #1 (matchmaker at scale), Domain 6 MAJOR #1 (10+ operator governance)
related-locks: Decision 21 (Jetix Matchmaker + Roy-Replication), Decision 19 (holding $1T), Decision 20 (USB-C positioning)
status: ready-to-run
---

# Matchmaker + Capability-Capsule Production — Perplexity Deep Research Prompt

## Как использовать

1. Открой Perplexity Pro в **Deep Research** режиме
2. Скопируй блок ниже от `===BEGIN PROMPT TO PASTE===` до `===END PROMPT TO PASTE===`
3. Paste + submit. Wait 20-30 минут.
4. Сохрани output в `raw/research/phase-2-deep-research-2026-04-22/RESULT-01-matchmaker.md` (сохраняй всё включая URL-цитаты)
5. Скажи Cloud Cowork — начнётся Phase 3 synthesis

## Context для понимания (не копируй в Perplexity)

Jetix OS Decision 21 (locked 2026-04-21): партнёрская matchmaker-сеть + roy-replication — основной механизм масштабирования от solo-founder к holding ($1T trajectory). Текущая архитектура описывает algorithm + quality-gate + contract-fixation + metrics modules, но **нет production analog у которого >1M tasks/mo или >10 активных operators работает через matchmaker/capability-capsule routing БЕЗ supervisor fallback**. Phase 1 master inventory (2026-04-22) зафиксировал это как Domain 2 MAJOR gap. До Phase 4 (baseline swarm construction) нужна референс-реализация — иначе recursive-swarm развернётся на непроверенном паттерне.

Связанные уже-имеющиеся материалы (не повторять):
- R-2 swarm intelligence (рассматривает 5 paradigm'ов, но не production matchmaker at scale)
- Perplexity Apr 22 Domain 2 (hub-spoke deep-dive, mailbox, hub/swarm; matchmaker — только концептуально)
- Anthropic Opus-lead multi-agent Research system (central coordinator, NOT matchmaker)
- CrewAI 2B executions (hub-and-spoke)

---

## ===BEGIN PROMPT TO PASTE===

I need deep production research on **matchmaker, dispatcher, registry-based, and capability-capsule multi-agent orchestration systems running at scale**. This is for architectural adoption — findings will be used to choose whether and how to implement a partnership-matchmaker layer in a real production system. Cite every claim. Prefer 2025-2026 primary sources. Admit uncertainty.

## What counts as "matchmaker / capability-capsule" (vs other paradigms)

**IN-SCOPE paradigms (find real production examples):**

1. **Matchmaker / task-broker**: a central registry where agents or task-specialists publish capability descriptors; incoming tasks are matched to the best-fit executor by a scoring function (not by a fixed handoff chain). Examples of the idea: IBM ACL matchmaking, FIPA contract-net, OpenAI Agents SDK handoff-by-capability, Ray Serve dynamic dispatch.

2. **Capability-capsule / registry bid**: tasks enter a queue; agents "bid" based on declared capabilities and load; an auctioneer or matcher allocates; agents self-organize via protocol (not via a coordinator agent issuing imperatives). Examples of the idea: blackboard systems, contract-net protocol, agent marketplaces.

3. **Dynamic dispatcher with capability registry**: tasks routed at runtime by capability lookup, not by hard-coded graph. Ray Serve, Temporal.io dynamic workflow routing, LangGraph dynamic handoff, Inngest step routing.

**OUT-OF-SCOPE (do NOT spend tokens on these — already covered):**

- Pure hub-and-spoke with fixed supervisor (e.g., CrewAI default, LangGraph supervisor with fixed graph, Anthropic Research system's Opus-lead)
- Pure flat peer-to-peer without a registry (e.g., Microsoft AutoGen GroupChat default)
- Human-in-loop router (Linear, Notion, Zapier)

**KEY QUESTION the research must answer**: does any production multi-agent system at >1M tasks/month OR >10 concurrent specialist-operators route work through a genuine matchmaker/capability-capsule layer **without a supervisor fallback**? If yes, who? If no, what's the closest approximation and why has no one crossed that threshold?

## Research scope — 8 concrete sub-domains

For each sub-domain below, provide: executive summary (3-5 sentences) / top 5 named systems or projects with URLs + 1-sentence description + why relevant / 5-10 findings with individual citations / gaps or uncertainties.

### Sub-domain A — Ray Serve + Ray agents for dynamic dispatch

- Anyscale Ray Serve production deployments with capability-based agent routing (not batch-serve of models)
- Ray Actor patterns for task-specialist agents: who is using this in production? at what scale?
- Sub-question: can Ray Serve Autoscaler + named actor references implement a matchmaker? Are there public examples?
- Primary sources: Anyscale blog 2025-2026, Ray Summit talks, GitHub ray-project/ray issues tagged "agent" or "llm"
- Known: Ray Serve powers some inference stacks at scale; unknown if anyone uses it as a matchmaker

### Sub-domain B — Temporal.io dynamic routing for agent work

- Temporal workflows with runtime-determined activity routing (Temporal supports dynamic workflow registration + dynamic activity selection)
- Who uses Temporal as a matchmaker vs. as a pure durability layer? OpenAI Codex, Replit Agent, Cursor all run on Temporal — do any of them route by capability or just by workflow definition?
- Temporal blog Nov 2025 "Of Course You Can Build Dynamic AI Agents with Temporal" — extract the concrete dynamic-dispatch patterns described
- Primary sources: temporal.io/blog, Temporal Replay conference talks 2025-2026, github.com/temporalio samples

### Sub-domain C — OpenAI Agents SDK handoff-by-capability + Swarm legacy

- OpenAI Agents SDK (successor to Swarm, Nov 2024): `handoffs` mechanism — how is this routing decided? Is it capability-descriptor match or fixed supervisor decision?
- Production deployments using OpenAI Agents SDK in handoff-chain >3 agents
- Swarm → Agents SDK migration: what lessons from Swarm's peer-bidding experiments did OpenAI publicize?
- Primary sources: platform.openai.com/docs/guides/agents, github.com/openai/openai-agents-python, OpenAI Dev Day 2025, OpenAI forum threads

### Sub-domain D — LangGraph + LangChain supervisor-alternatives

- LangGraph `Command(goto=...)` dynamic routing at runtime
- LangGraph `Send()` for fan-out capability dispatch
- Multi-agent swarm pre-built architecture: https://langchain-ai.github.io/langgraph/how-tos/multi_agent/agent_supervisor/
- Is anyone running LangGraph swarm/supervisor-less in production at >1M runs/month? What do they report?
- Primary sources: langchain-ai.github.io, LangSmith case studies, github.com/langchain-ai/langgraph discussions

### Sub-domain E — Inngest, Trigger.dev, Hatchet — capability-based job routers

- Inngest has "matching" and "concurrency" primitives that can route work by function label
- Trigger.dev v3 queues + tasks — any capability-registry layer?
- Hatchet (hatchet.run) — directed-acyclic-graph workflows with dynamic routing
- Used by any AI-agent stack as a matchmaker substitute?
- Primary sources: inngest.com/docs, trigger.dev/docs, hatchet.run/docs, their customer case studies 2025-2026

### Sub-domain F — Blackboard + contract-net revival in LLM-era agents

- Classic blackboard architectures (HEARSAY-II, BB1, GBB) — has anyone ported these to LLM agents 2025-2026?
- FIPA contract-net protocol in modern LLM frameworks — named implementations?
- Academic papers 2025-2026 on capability-capsule / bid-based multi-LLM coordination
- ArXiv searches: "capability-based task routing", "agent marketplace LLM", "contract net protocol LLM"

### Sub-domain G — Production agent marketplaces at scale

- Upwork + AI agents on Upwork: does Upwork have any capability-routing for AI-agent workers, or is it all human + Zapier?
- Fiverr "Neo" AI marketplace — architecture disclosures
- Lindy marketplace, Relevance AI template gallery, CrewAI cloud "Agent Marketplace" — do any of these route work by capability rather than by user selection?
- Coinbase / Algorand agent-marketplace experiments

### Sub-domain H — Industrial multi-agent dispatchers (non-LLM) that LLM systems could copy

- DoorDash "Dasher assignment" / Uber dispatch / Amazon Flex — capability-based real-time matching at >1M tasks/day — architecture lessons that generalize to LLM agent routing?
- AWS Step Functions "Map state" with dynamic branch selection at production scale
- Kubernetes scheduler as a matchmaker for pods by capability (taints/tolerations/node-selectors) — analog for agents?
- Microsoft Azure Durable Functions "fan-out / fan-in" patterns

## Specifically required deliverables

### D1. Top 10 named systems with matchmaker / capability-capsule characteristics

Rank by: evidence of production scale (tasks/month, concurrent operators) × evidence that routing is genuinely capability-based (not fixed supervisor or fixed graph) × public architectural transparency. For each top-10:

- Name + URL + owner (company / open-source / research)
- Paradigm classification (pure matchmaker / registry-dispatch / hybrid with supervisor fallback)
- Scale numbers with primary-source citation (not PR blog claims — actual metrics)
- Architecture: how does task → executor matching happen? What's the scoring function? Is there a supervisor fallback?
- Failure modes documented by practitioners (Reddit / HN / conference post-mortems)
- Public assets: GitHub repo, docs URL, talk link

### D2. Comparison table

Systems across rows; axes across columns:
- Supervisor fallback (Y/N)
- Capability descriptor format (free-text / typed schema / vector embedding / OpenAPI-like)
- Dispatch latency at 99p
- Concurrent-agent limit published
- Tasks/month published
- Open-source vs closed
- Production use vs demo-only

### D3. Governance at 10+ operators — 5 named case studies

For the Jetix roy-replication / 10+ partnership-specialist layer:

- 5 case studies of systems coordinating **10+ independent specialist-operators** (human, AI, hybrid)
- How is capability registered? Who updates capability? How is quality enforced? How is payment/compensation tracked?
- Specifically: Toptal, Upwork agencies, Toptal's internal matching algorithm, Braintrust (blockchain talent network), AWS re:Post expert network, Gigster, Stripe Press playbook for talent networks
- Failure modes: talent drift, quality decay, governance overhead, trust breakdown — with citations

### D4. Compensation / rev-share / contract-fixation patterns

- How do matchmaker networks compensate specialists? Flat fee / rev-share / equity / token / reputation-scored?
- Braintrust Network token model — successes and failures
- Toptal / Gigster / Andela / X-Team hourly-markup model
- Creator-economy "Substack" model adapted for specialist networks
- Any blockchain-based talent-network with working compensation layer >12 months in production?

### D5. Quality-gate mechanisms at scale

- How does a production matchmaker network enforce quality without a human supervisor looking at each output?
- Reputation systems (Stack Overflow style), test-based gates (LeetCode-for-specialists), client-side grading, automated eval against rubric
- Which mechanisms survive >10,000 transactions without degrading? Which collapse under scale?
- Cite primary sources from Upwork/Fiverr/Braintrust engineering blogs

### D6. Failure modes / anti-patterns specific to matchmaker systems

- Task-specialist mismatch drift over time
- Cold-start (new specialist has no reputation)
- Gaming the scoring function (specialists over-claiming capabilities)
- Supervisor-fallback becoming the default (matchmaker → de-facto hub-and-spoke)
- "Matchmaker rot" — descriptors go stale faster than they're updated
- Specifically seek post-mortems where "we tried matchmaker, reverted to fixed assignment" — this is high-signal negative data

### D7. 2025-2026 specific updates

- Any Anthropic / OpenAI / DeepMind / Microsoft publication or talk 2025-2026 explicitly on capability-based LLM agent routing?
- Any arXiv paper 2025-2026 on multi-LLM routing that measures capability-match vs. round-robin vs. static assignment?
- Any startup raising in 2025-2026 pitching "capability-capsule for AI agents" — credibility assessment
- Notable patent filings 2025-2026 in this space

### D8. Honest assessment

Close the research with these honest answers:

1. **Does a production matchmaker/capability-capsule LLM system exist at >1M tasks/mo WITHOUT supervisor fallback?** (Yes/No/Approximations exist — name them)
2. **What is the closest credible analog** a solo founder could study?
3. **What's the smallest number of concurrent agents** at which pure capability-capsule routing has been shown to outperform a supervisor?
4. **What governance patterns at 10+ specialist operators** survived ≥12 months in production (with citations)?
5. **What's missing from the public record** that a research team (or a roy partnership) would need to contribute to close the gap?

## Output requirements

- **Each sub-domain A-H**: executive summary + top-5 refs + 5-10 findings + gaps
- **Deliverables D1-D8**: complete
- **Closing**: top 10 actionable items for a solo founder building a matchmaker layer + top 10 projects to deep-investigate + the honest assessment above
- **Length target**: 8,000-15,000 words
- **Citation discipline**: every claim cited; URL + 1-sentence description of source; flag secondary vs primary; mark 2023-2024 sources as "possibly stale"
- **No hype**: if a project claims "AI marketplace" but has no public production metrics, say so explicitly
- **Admit uncertainty**: if private / undocumented / rumored, say so and rate confidence (high/medium/low)

## Constraints

- Prefer primary sources: conference talks (YouTube + slides), engineering blogs, arXiv, GitHub issues/discussions, founder tweets with specifics
- 2025-2026 strongly preferred; flag 2023-2024 as "potentially outdated"
- No listicles unless they cite primary sources themselves
- Scale claims MUST have a source — "X runs at scale" without a number is rejected
- If you cannot answer a question with any evidence, write "no evidence found" rather than speculating

## ===END PROMPT TO PASTE===

---

## Alternative: split into 2 focused prompts (optional)

If the single prompt returns surface-level output, split into:

1. **Prompt A — Production matchmaker systems** (sub-domains A-F + D1-D2 + D6-D8) — ~15 min Deep Research
2. **Prompt B — 10+ operator governance + compensation** (sub-domain G + D3-D5) — ~15 min Deep Research

## After Perplexity returns

1. Save raw output to `raw/research/phase-2-deep-research-2026-04-22/RESULT-01-matchmaker.md`
2. Flag Cloud Cowork in Telegram or via mailbox — Phase 3 synthesis will cross-reference against Decision 21 (Matchmaker + Roy-Replication) + Q9/Q10/Q15 of D4 architecture brief
3. If any named system looks Jetix-adoptable, queue a second focused research pass on that system specifically

---

*END PROMPT 01 — Matchmaker + Capability-Capsule Production*
