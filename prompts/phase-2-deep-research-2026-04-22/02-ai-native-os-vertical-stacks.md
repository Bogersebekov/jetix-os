---
id: phase-2-02-ai-native-os-vertical-stacks
title: Opinionated AI-Native OS Stacks (Solo → Holding) — Perplexity Deep Research
author: cloud-cowork
date: 2026-04-22
tool: Perplexity Pro Deep Research
priority: P1
gap-coverage: Domain 4 MAJOR #1 (no packaged AI-native OS for solo→holding), Domain 4 MAJOR #2 (Anthropic internal storage layer opaque)
related-locks: Decision 19 (holding $1T), Decision 20 (USB-C positioning + enterprise-fast), Decision 24 (open-source research direction)
status: ready-to-run
---

# Opinionated AI-Native OS Stacks — Perplexity Deep Research Prompt

## Как использовать

1. Открой Perplexity Pro в **Deep Research** режиме
2. Скопируй блок ниже от `===BEGIN PROMPT TO PASTE===` до `===END PROMPT TO PASTE===`
3. Paste + submit. Wait 20-30 минут.
4. Сохрани output в `raw/research/phase-2-deep-research-2026-04-22/RESULT-02-ai-native-os.md`
5. Скажи Cloud Cowork — Phase 3 synthesis начнётся.

## Context для понимания (не копируй в Perplexity)

Perplexity Apr 22 "Honest Assessment" сформулировала: "No one has built this as a packaged product. The pieces exist; they are not assembled into a coherent system that a solo founder can install and operate." Decision 24 (locked 2026-04-21) ставит Jetix Phase 2+ в позицию "open-source research direction" — ideally это emerges из задокументированного analog. Нам нужно 2-5 named projects где кто-то пытался собрать **opinionated vertical AI-native OS** публично (даже imperfectly) с retrospective analysis.

Phase 1 master inventory (2026-04-22) зафиксировал эту MAJOR gap — нельзя Phase 2+ позиционироваться как "research direction" не имея case study "кто-то уже пробовал и вот что вышло". Существующая Apr 22 Perplexity research перечислила 18 AI-native companies, но **ни одна из них не packaged для solo→holding**.

Связанные материалы (не повторять поверхностно):
- Perplexity Apr 22 Domain 1 (18 profiled: Karpathy / Anthropic / Cursor / Cognition / Replit / Factory / Builder.io / Sierra / Decagon / Cresta / Relevance AI / Lindy / Gumloop / Every / Aider / Sweep / Mentat / Mem0)
- R-5 production case studies (Aider, Replit, Cursor, Devin)
- Every Inc. master plan (operating model, not product)
- Reddit r/Entrepreneurs Mar 2026 "7 AI agents running business" (undocumented)

---

## ===BEGIN PROMPT TO PASTE===

I need deep production research on **opinionated AI-native operating-system stacks** — specifically, packaged, documented, assembled configurations that a solo founder could install and operate to scale from sole proprietorship toward holding-company structure. This is for an architectural decision on whether to build, fork, or buy. Cite every claim. Prefer 2025-2026 primary sources. Admit uncertainty. No hype.

## What counts as "opinionated AI-native OS" (vs. building blocks)

**IN-SCOPE (find real named projects):**

1. **Vertical AI-native OS**: a system packaged for a specific industry (legal AI firm of one, indie dev, finance advisor, healthcare consultant, real estate broker, consulting micro-firm) that assembles Claude-or-equivalent + task queue + memory + workflow + billing into one installable configuration.

2. **Horizontal AI-native OS with opinion**: packages like Sierra, Decagon, Lindy, Relevance AI — not just "you can build agents here" but "here is the assembled stack with opinionated defaults for X business shape."

3. **Solo-founder OS attempts**: closed-source products OR GitHub projects >5,000 stars that explicitly target "AI-native operating system for solo founder / indie / one-person consultancy."

4. **Open-source candidates**: GitHub projects a solo founder could fork or study as a starting skeleton (not a building block like LangChain, but an assembled system).

**OUT-OF-SCOPE (do NOT cover — already covered in Apr 22 Perplexity):**

- Cursor, Claude Code, Aider, Copilot, Devin (engineering assistants, not operating systems)
- LangChain, LangGraph, LlamaIndex, AutoGen (building blocks)
- Pure task trackers (Linear, Notion, Asana, ClickUp)
- Pure memory systems (mem0, Zep, Letta) — evaluated separately in Phase 1 Domain 3
- Cloud infrastructure (AWS, Temporal, Inngest) — building blocks

**KEY QUESTION the research must answer**: has anyone (company or open-source project or individual) built an **opinionated, packaged, documented AI-native OS that a solo founder could install today and operate without assembling 20 primitives themselves**? If yes, who? If no, why not?

## Research scope — 8 concrete sub-domains

For each sub-domain below, provide: executive summary (3-5 sentences) / top 5 named projects with URLs + 1-sentence description / 5-10 findings with citations / what each project fails to solve.

### Sub-domain A — Vertical AI-native OS for legal firms of one

- Projects targeting solo attorney / small legal consultancy: Harvey AI (enterprise, not solo), CaseText CoCounsel → Thomson Reuters, Spellbook (contracts), Lex Machina, Clearbrief, EvenUp
- Specifically solo-lawyer OS packages (not enterprise): who has built one?
- Legal-specific workflows pre-packaged: intake → discovery → drafting → e-filing → billing
- 2025-2026 entrants; ABA Legal Tech Report 2025-2026; Stanford CodeX program alumni projects

### Sub-domain B — Vertical AI-native OS for indie finance / tax / accounting

- Solo tax preparer / small accounting practice stacks: Keeper Tax, Puzzle, Digits, Pilot, Bench
- AI-first financial advisor OS: Vise AI (shut down 2024), Range, Farther, Betterment advisor-platform
- Accounting firm automation stacks: BILL Spend & Expense, Pry, Vena
- Specifically solo-founder-packaged not enterprise-only

### Sub-domain C — Vertical AI-native OS for healthcare micro-practices

- Solo physician / tele-health practice stacks: Abridge, Suki AI, DeepScribe, Nuance DAX (enterprise)
- Mental-health solo practitioner OS: Heidi Health, Headspace Health, SonderMind, Thrive
- Healthcare-solo-specific AI OS with documented installability — does one exist?

### Sub-domain D — Vertical AI-native OS for real estate / broker-of-one

- EPIQUE AI, HouseCanary, Compass Rex, RealScout, Clever Real Estate
- Solo-broker or team-of-two OS: anyone packaged this?

### Sub-domain E — Vertical AI-native OS for consulting micro-firms

- McKinsey "Lilli" (internal, closed), BCG GENE (internal, closed), Bain Sage (internal)
- Open-source / SaaS "consulting OS" attempts: Decisio, Scio, Every Inc.-like operating models packaged
- Andrew Dunn "productize your AI consulting offer in 2026" — is there an OS package corresponding to this playbook?
- Solo-consulting-firm OS: documented attempts with post-mortem

### Sub-domain F — Horizontal AI-native OS: Sierra, Decagon, Lindy, Relevance AI — deep architecture

For each of these four specifically:

- Sierra (Bret Taylor): $100M ARR in 21 months. What is the internal architecture? What's public from Sierra engineering blog, Sierra conference talks, LinkedIn posts of Sierra engineers? What failure modes do they publish?
- Decagon: customer-support vertical. Architecture disclosures 2025-2026.
- Lindy (Flo Crivello, Charley.ai): no-code agents for solo. GitHub issues and Lindy user Reddit threads for architectural signals.
- Relevance AI (Daniel Vassallo / Nelson Brown): Workforce Canvas. 40,000 agents created Jan 2026. How does the runtime work? What's public from their engineering blog?
- For each: retention metrics (not just "agents created"), churn rate, what they'd build differently if starting 2026

### Sub-domain G — Solo-founder OS attempts (publicly documented)

- Karpathy "LLM Wiki" Gist Apr 2026 — the conceptual reference; has anyone extended it into a packaged OS?
- Every Inc. master plan (Dan Shipper): 15 people, 5 products, named AI agents — is the Every operating model documented as a packageable OS or only as a case study?
- Greg Isenberg "Late Checkout" holdco model — is there an OS package corresponding to the 35-step playbook?
- Justin Welsh LinkedIn solopreneur stack — documented configurations?
- Danny Postma / Marc Lou / Pieter Levels / Tony Dinh — have any of them published their actual OS configuration or is it just screenshots and tweets?
- Anyone fork-able on GitHub at >5K stars positioned as "AI OS for one"?

### Sub-domain H — Open-source projects Jetix-shape could fork

- activepieces/activepieces (Zapier-alternative, 15K stars) — AI-native enough?
- n8n/n8n — AI nodes added 2024-2025, is there an "AI-OS" overlay?
- AnythingLLM (Mintplex Labs) — multi-user LLM workspace
- LibreChat, OpenWebUI — chat interfaces vs. OS
- AutoGPT, BabyAGI legacy — what emerged from their ashes that's OS-shaped?
- Chatwoot, Botpress — customer-support OS that generalizes?
- Focus on packages with >5,000 stars + active maintenance as of 2026-04

## Specifically required deliverables

### D1. Top 10 "opinionated AI-native OS for solo-to-small" named projects

Rank by: completeness of package (is it installable or a kit of parts?) × documentation quality × retention evidence × open-vs-closed × fit for solo-founder-scaling-to-holding.

For each top-10:

- Project name + URL + owner + founding year
- Target shape (vertical? horizontal? business-shape?)
- What's bundled: task queue / memory / agents / workflows / billing / integrations
- Installability: one-click deploy, Docker, "contact sales", SaaS-only
- Retention evidence: paid customers count, activity, churn if public
- Public post-mortems / regrets by founders
- Opinion score: "good skeleton to study" / "good case study of what not to do" / "irrelevant"

### D2. The Every Inc. model, packaged

- Every Inc. is repeatedly cited (Apr 22 Perplexity) as the closest operational analog
- Detailed extraction of Every's operating model from every.to/on-every posts, Dan Shipper Lenny's Podcast / Twenty Minute VC appearances 2025-2026
- Named AI agents at Every ("Friday", "Charlie", etc.) — what do they do, which tools back them, how were they built?
- Is Every packaged? If not, what would packaging look like? Is Jetix's direction the "packaging of Every"?

### D3. The "7 AI agents running a business" Reddit case

- https://www.reddit.com/r/Entrepreneurs/comments/1rxw979/running_my_business_with_ai_agents_instead_of/ — cited in Apr 22 Perplexity as closest functional prototype
- Verify the thread is still accessible; extract technical details the poster shared
- Search Reddit/X for similar undocumented-but-real cases 2025-2026
- What architecture pattern emerges? How representative is this of the "solo + AI agents" population?

### D4. Build-vs-fork-vs-buy decision tree for Jetix

Based on D1-D3, produce a decision tree:

- IF any project in D1 covers >70% of Jetix Decision 19-24 architecture scope → fork
- IF multiple projects cover 30-70% each, composable → compose + wrap
- IF <30% coverage → build (Jetix's current trajectory)

Return a specific estimate percentage and citation logic.

### D5. "Opinionated vs. building blocks" spectrum analysis

Locate the "opinionated OS" problem on a 3-axis spectrum:

- Axis 1: vertical-specific (real estate / legal / consulting) vs. horizontal
- Axis 2: open-source vs. closed
- Axis 3: installable-immediately vs. kit-of-parts

Plot the top-10 projects from D1 on this spectrum. Identify the empty quadrants — they represent the gap Jetix could fill.

### D6. Closed-source hints from Anthropic / OpenAI / Cursor / Devin internal ops

- Any public hints about how Anthropic, OpenAI, Cursor, Cognition, Factory internally coordinate their own agentic work? Blog posts, engineering all-hands leaks, SREcon talks?
- Specifically: Anthropic's internal storage layer for multi-agent Research system — is there any 2025-2026 disclosure beyond the Jun 2025 "How we built our multi-agent research system"?

### D7. Failure patterns in "assemble your own OS" attempts

- Reddit / HN / founder-tweets where someone tried to assemble their own AI-OS and abandoned it — what triggered abandonment?
- LangChain post-mortems (Octoclaw and others)
- AutoGPT/BabyAGI graveyard — what killed them?
- "I built my own AI OS for 6 months then deleted it" threads — aggregate the top 5

### D8. Honest assessment

Close with:

1. **Has anyone packaged "AI-native OS for solo→holding"?** (Yes / No / Approximations — name them with confidence scoring high/medium/low)
2. **If no, why not?** Structural reasons (configuration vs. product), market-size reasons, lack of founder coalition, or simply "too new"?
3. **What's the closest fork-able skeleton** a solo founder could use as a starting point TODAY (April 2026)?
4. **What's the 20% that's always custom** regardless of how opinionated the OS gets (the business-operations layer — client context ingestion, proposal generation from institutional memory, retainer-client state tracking without manual effort)?
5. **Would a Jetix-shaped "opinionated vertical stack for solo AI consultant with path to holding" have a credible market** (cite evidence of founders who would buy, expected ARR trajectory, competitive positioning)?

## Output requirements

- **Each sub-domain A-H**: executive summary + top-5 refs + 5-10 findings + gaps
- **Deliverables D1-D8**: complete
- **Closing**: top 10 actionable items + top 10 projects to deep-investigate + the honest assessment above
- **Length target**: 8,000-15,000 words
- **Citation discipline**: every claim cited; URL + 1-sentence description; mark secondary vs primary; flag possibly-stale 2023-2024 sources
- **No hype**: a project with 50K stars but no documented users should be flagged as such
- **Admit uncertainty**: rate each claim high/medium/low confidence

## Constraints

- Prefer primary sources: engineering blogs, conference talks, founder interviews with specifics
- 2025-2026 strongly preferred; flag 2023-2024 as "potentially outdated"
- Verify claimed stack components with actual source (repo, docs, not press releases)
- If a project claims "for solo founders" but requires enterprise contract → call out the mismatch
- If a project's README is aspirational but active contributors are 1 person last commit >6 mo → call out

## ===END PROMPT TO PASTE===

---

## Alternative: split into 2 focused prompts (optional)

1. **Prompt A — Vertical OS by industry** (sub-domains A-E + D1 + D5) — ~20 min
2. **Prompt B — Horizontal OS + solo-founder attempts + fork-candidates** (sub-domains F-H + D2-D4 + D6-D8) — ~20 min

## After Perplexity returns

1. Save raw output to `raw/research/phase-2-deep-research-2026-04-22/RESULT-02-ai-native-os.md`
2. Flag Cloud Cowork — Phase 3 synthesis will cross-reference D1-D8 against Decision 24 (open-source research direction) + Decision 19 (holding trajectory) + Decision 20 (USB-C positioning)
3. If D4 decision-tree identifies a >70% coverage fork candidate, queue immediate deep-dive research on that specific project

---

*END PROMPT 02 — Opinionated AI-Native OS Stacks*
