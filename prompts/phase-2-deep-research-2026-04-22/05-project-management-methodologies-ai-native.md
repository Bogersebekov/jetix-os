---
id: phase-2-05-project-management-ai-native
title: Project Management Methodologies for AI-Native Teams 2026 — Perplexity Deep Research
author: cloud-cowork
date: 2026-04-22
tool: Perplexity Pro Deep Research
priority: P2
gap-coverage: New Domain 9 (Project + Product Management) — not covered in Phase 1
ruslan-directive: "collect best practices + combine с CE + code-writing = new unified Jetix philosophy"
status: ready-to-run
---

# Project Management Methodologies for AI-Native Teams — Perplexity Deep Research Prompt

## Как использовать

1. Открой Perplexity Pro в **Deep Research** режиме
2. Скопируй блок ниже от `===BEGIN PROMPT TO PASTE===` до `===END PROMPT TO PASTE===`
3. Paste + submit. Wait 25-30 минут.
4. Сохрани output в `raw/research/phase-2-deep-research-2026-04-22/RESULT-05-pm-methodologies.md`
5. Скажи Cloud Cowork — Phase 3 synthesis начнётся.

## Context для понимания (не копируй в Perplexity)

Ruslan's directive 2026-04-22: "Собери best practices по PM + combine с CE + code-writing = новая unified Jetix philosophy управления работой." Текущая Jetix architecture использует CE (Plan-Work-Review-Compound) loop + ad-hoc sprints; нет принятой PM methodology. Phase 2+ scaling требует системного подхода — особенно когда roy-replication добавит 10+ concurrent operator'ов (Decision 21).

Special sub-question: Shape Up 6-week cycle ↔ CE Plan-Work-Review-Compound loop — mapping уже кто-то сделал?

Связанные материалы (не повторять):
- Every CE canonical guide (Apr 22) — loop structure, но не PM-methodology-adjacent
- R-6 Every/Cora — 12-reviewer fan-out, но это product-engineering а не PM

---

## ===BEGIN PROMPT TO PASTE===

I need a deep synthesis research on **project management methodologies as they apply to AI-native teams in 2026** — teams where LLM agents, AI-assisted engineering, and Compounding Engineering are part of the standard workflow. The goal: understand which PM frameworks survive translation to AI-augmented contexts, which break, and what's emerging. Cite every claim. Prefer 2025-2026 primary sources. Admit uncertainty. No hype.

## Background

"AI-native team" for this research = a team (1-50 people, including hybrid human+AI) where:
- A significant portion (>30%) of individual contributor output is AI-augmented or AI-generated
- Agents and sub-agents participate in work execution (not just chat)
- Compounding Engineering (Every, Kieran Klaassen) or equivalent practice is in use
- The team uses Claude Code / Cursor / GitHub Copilot / similar as first-class tooling

The solo-founder → small-team → holding-company arc is a specific shape of interest.

## Research scope — 8 concrete sub-domains

For each sub-domain: executive summary / top 5 references (primary sources with URLs + 1-sentence description) / 5-10 findings with citations / how this methodology fails or adapts in AI-native teams.

### Sub-domain A — Shape Up (Basecamp / Ryan Singer, 2019)

Shape Up: 6-week cycles, 2-week cooldown, appetite-based scoping, hill charts, betting table, shaped vs. unshaped work, circuit breaker, fat-marker sketches.

- Has anyone adapted Shape Up to AI-native teams? Who, with citations? Basecamp's own 2025-2026 statements if they've spoken about AI in Shape Up
- Shape Up at 37signals in 2026 — has it changed with AI adoption?
- Companies claiming to use Shape Up with AI: named list with links
- Shape Up for solo founder (not 37signals-scale): known patterns?
- **Critical sub-question**: Does the 6-week cycle compress or expand in AI-native teams? Primary-source evidence either way.
- **Critical sub-question**: Has anyone mapped Shape Up's "shape → bet → build → cooldown" to CE's "Plan → Work → Review → Compound"? Named sources.

### Sub-domain B — Scrum / Kanban / Agile (XP, Lean Kanban)

- Scrum in AI-native teams 2025-2026: what breaks? What adapts?
  - Sprint ceremonies when AI is doing 40% of implementation
  - Story points when AI can ship in minutes
  - Sprint review when the "team" includes agents
  - Scaled agile (SAFe, LeSS, Nexus) in AI-augmented orgs
- Kanban in AI-native teams: WIP limits when agents are parallel workers
- XP (Extreme Programming) pair programming → human-AI pair programming
- Modern Agile (2016) and Disciplined Agile Delivery (DAD) — relevance?
- Primary sources: agilealliance.org 2025-2026 content, scrumalliance.org blog, key practitioners (Jeff Sutherland, Ron Jeffries, David Anderson, Mike Burrows) on AI-Agile

### Sub-domain C — Linear Method (Linear.app team, 2020-2026)

The Linear Method (linear.app/method): complete documentation as published by the Linear team.

- Full principles enumerated with citations (linear.app/method pages)
- How Linear itself uses the Linear Method internally (Linear employees' blog posts, CEO Karri Saarinen interviews)
- Linear Method vs. Scrum / Kanban / Shape Up — stated differentiators
- Linear Method in AI-native teams — how Linear's own AI features (Linear MCP, Feb 2026) change the workflow
- Adoption: named companies using Linear Method; sample size of public case studies
- Criticisms of the Linear Method from practitioners

### Sub-domain D — Lean / Theory of Constraints / Goldratt

- Eliyahu Goldratt "The Goal" / "Critical Chain" — bottleneck thinking
- Lean Software Development (Mary Poppendieck): 7 principles
- "The Phoenix Project" (Gene Kim) — fiction-based DevOps / Three Ways
- "The Unicorn Project" — successor
- Lean / TOC in AI-native teams: where is the bottleneck now? Human review time? Context window? Tool latency?
- Applying Goldratt's 5 focusing steps to AI-augmented engineering
- Primary sources: Lean Enterprise Institute, DevOps Research and Assessment (DORA) reports 2024-2026

### Sub-domain E — Enterprise frameworks (SAFe, PRINCE2, PMBOK, ITIL)

- SAFe 6.0 — relevant for a solo founder scaling to holding? Or enterprise-only?
- PRINCE2 Agile — UK gov origin, PRINCE2 7 (2023)
- PMI PMBOK 7th Edition (2021) — still canonical 2026?
- ITIL 4 (2019/2020) — service management in AI-native contexts
- "Project to Product" (Mik Kersten, 2018) — Flow Framework, still relevant?
- Enterprise AI adoption case studies 2025-2026 that reference these frameworks
- Is there a documented pathway from solo-founder to holding that uses any of these frameworks at scale?

### Sub-domain F — Emerging 2024-2026 AI-native methodologies

- Specifically named 2024-2026 methodologies designed for AI-native teams (not retrofitted)
- "Compound Engineering" (Every / Kieran Klaassen, 2024-2026) — this is CE; how has it codified project management beyond the build loop?
- "Agent-augmented sprint" concepts from AI Engineer Summit, Lenny's Podcast, Latent Space podcast
- "Vibe coding" vs. structured AI-native PM — Andrej Karpathy framing 2025
- YC / Lenny Rachitsky / Every Inc. / Builder.io — PM adaptations published 2025-2026
- Notion 3.4 Custom Agents + PM adoption patterns
- Linear + Claude Code integration patterns as an implicit methodology

### Sub-domain G — Solo-founder PM at scale

- How does a solo founder running 5-15 AI agents + 2-10 rev-share partners actually plan and track work?
- Named solo founders who've documented their PM approach: Justin Welsh, Pieter Levels, Tony Dinh, Marc Lou, Danny Postma, Arvid Kahl, Rob Walling
- Blogs / podcasts / YouTube where they describe their day-to-day planning
- Tools in the actual solo-founder stack (Notion + Linear + a spreadsheet + mental model)
- Community wisdom (Indie Hackers, r/Entrepreneurs, MicroConf)

### Sub-domain H — Compounding Engineering meets PM — the synthesis question

The Every CE pattern (Plan → Work → Review → Compound; $100 rule; 50/50 rule; 80/20 time split):

- Has anyone explicitly cross-mapped CE to Shape Up / Scrum / Linear Method / Lean?
- Named publications 2024-2026 that bridge CE with a PM framework
- Kieran Klaassen, Dan Shipper public statements on project management in their own Every practice
- Gap analysis: what does CE cover that PM doesn't? What does PM cover that CE doesn't?

## Specifically required deliverables

### D1. Comparative matrix

Rows: methodologies (Shape Up / Scrum / Kanban / Linear Method / Lean-TOC / SAFe / CE / Vibe-coding)
Columns:
- Origin year / author
- Core unit of planning (sprint / cycle / flow / feature / batch / task-compound)
- Unit of shipping (increment / feature / story / MR / PR)
- Feedback loop length (week? 6 weeks? continuous?)
- AI-native adaptation maturity (high / medium / low / none)
- Solo-founder fit (yes / conditional / no)
- Holding-scale fit (yes / conditional / no)
- Primary-source quality (strong / moderate / weak)

### D2. The Shape Up ↔ CE mapping

Specifically answer: has anyone written this mapping?

- If yes: cite them, extract their mapping structure, critique gaps
- If no: sketch a first-principles mapping — Shape Up's "shaping / betting / building / cooldown" → CE's "plan / work / review / compound" with a concrete mapping table
- Identify where they conflict (e.g., Shape Up's 6-week commitment vs. CE's "skill-as-code" continuous compound)

### D3. Top 10 methodology practices for AI-native solo-to-small teams

Ranked list of individual practices (not whole frameworks) that a solo-founder AI-native team should adopt, pulled from all methodologies. For each:

- Practice name and origin framework
- Why it works in AI-native context (specific mechanism)
- Evidence of adoption (case studies)
- Cost to adopt
- When to skip

Examples of candidates:
- Appetite-based scoping (Shape Up)
- Hill charts for uncertainty-vs-progress visibility (Shape Up)
- WIP limits (Kanban)
- Cycle time measurement (Linear Method)
- Standups structured around agent outputs (modified Scrum)
- Postmortem discipline (SRE / DORA)
- Pairing rituals adapted to human-AI pairs (XP)
- Compound-ledger: track codifications as a first-class backlog item (CE)
- Theory of Constraints bottleneck identification (Goldratt)
- "Done is better than perfect" heuristic (Lean / Gumroad)
- "Write it down" discipline (37signals / Stripe writing culture)

### D4. Top 10 methodology traps to avoid

Ranked list of common mistakes when applying classical PM to AI-native work. For each:

- Trap description
- Case studies where this failed (citations)
- Why AI-native context amplifies the failure mode
- How to detect early
- Correction path

Examples:
- Estimating story points for AI-generated work (breaks)
- Running sprint reviews that ignore agent-produced artifacts
- Defining "done" without agent-readable acceptance criteria
- Over-scaling ceremonies for a 1-3 person + agents team
- Using Gantt charts for non-linear compound work
- Treating agents as "resources" instead of active participants
- Assuming AI-generated code needs the same review cadence as human-written code
- Mistaking speed-of-first-draft for velocity

### D5. Proposed Jetix-unified framework (sketch, not prescriptive)

Based on the research above, sketch the **skeleton of a unified framework** that combines:

- CE loop (Plan → Work → Review → Compound) as inner loop
- Shape Up-like outer loop (cycles of ~6 weeks, appetite-based)
- Linear Method-like cadence (continuous, cycle-based, not sprint-based)
- Theory-of-Constraints bottleneck tracking

Note: this is a synthesis-stub. Detailed design is Phase 3 synthesis work. Here you produce a 1-2 page outline that names each component, its source methodology, and the gap it fills.

### D6. Honest assessment

Close with:

1. **Is there an existing 2025-2026 published framework that fully addresses AI-native PM?** (Yes / No / Partial — name it)
2. **What's the most important practice a solo-founder AI-native team should adopt immediately?**
3. **What's most overrated** in legacy PM literature when translated to AI-native contexts?
4. **What's the open research question** in 2026 PM theory?
5. **If you had 90 minutes to teach a new AI-native team the essentials of PM**, what 10 concepts would you cover?

## Output requirements

- Each sub-domain A-H: executive summary + top 5 refs + 5-10 findings + gaps (200-800 words each)
- Deliverables D1-D6: complete
- Length target: 10,000-18,000 words
- Citations: every claim; date-stamped; primary sources marked [PRIMARY], secondary [SECONDARY], practitioner-anecdote [ANECDOTE]
- 2024-2026 preferred; flag 2019-2023 as "possibly dated, verify 2026 relevance"
- No hype — if a methodology claims "AI-powered" but doesn't ship differently in AI-native teams, say so

## Constraints

- Primary sources: 37signals (Basecamp), Linear team blog, Jeff Sutherland official, David Anderson (Kanban), Eliyahu Goldratt texts, Mary Poppendieck, PMI.org official docs, Mik Kersten, Every Inc. (CE), direct podcast / newsletter / YouTube content
- Secondary sources OK for case studies where primary is inaccessible
- If a claim has no supporting source, say so
- Do not conflate "Agile" (manifesto) with Scrum (specific framework) — treat them distinctly
- Any methodology with no 2024+ published commentary is flagged as possibly legacy

## ===END PROMPT TO PASTE===

---

## Alternative: split into 2 focused prompts (optional)

1. **Prompt A — Classical methodologies + Shape Up + Lean** (sub-domains A-E + D1) — ~15 min
2. **Prompt B — AI-native PM + CE mapping + Jetix synthesis** (sub-domains F-H + D2-D6) — ~15 min

## After Perplexity returns

1. Save raw output to `raw/research/phase-2-deep-research-2026-04-22/RESULT-05-pm-methodologies.md`
2. Flag Cloud Cowork — Phase 3 synthesis combines this with File 06 (Product Mgmt) and File 07 (Management Philosophy) into a unified Jetix PM/PDM philosophy document
3. Cross-reference against existing Jetix CE adoption plan (`raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md`)

---

*END PROMPT 05 — Project Management Methodologies*
