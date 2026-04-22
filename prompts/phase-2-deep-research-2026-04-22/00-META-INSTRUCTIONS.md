---
id: phase-2-meta-instructions-2026-04-22
title: META — Instructions for Server CC to WRITE Phase 2 Deep Research Prompts
author: cloud-cowork
date: 2026-04-22
audience: server-cc (Opus 4.7 1M, extended thinking max)
expected-duration: 2-3h
status: active
depends-on: raw/research/master-inventory-2026-04-22.md (Phase 1 done)
---

# META — Write Phase 2 Deep Research Prompts

## Role

Ты — **prompt architect**. Твоя задача — НЕ делать research. Твоя задача — написать
**8 deep research prompts** (ready-to-paste в Perplexity Pro Deep Research / Claude
Deep Research) которые закроют gap'ы выявленные Phase 1 Master Inventory и
расширят coverage на новый домен (Project + Product Management).

**Ruslan потом copy-paste'ит каждый prompt в Perplexity и сохранит output** — он
запускает research, не ты. Ты пишешь CONTENT of prompts. Каждый prompt должен
работать standalone (никакого контекста из этого chat'а у Perplexity нет).

## Context

- **Phase 1 Inventory:** `raw/research/master-inventory-2026-04-22.md` — 7/8 domains
  STRONG. 4×P1 + 3×P2 + 3×P3 gap priorities identified.
- **Existing Perplexity output (2026-04-22):** `raw/research/perplexity-market-ai-native-2026-04-22/perplexity-output.md`
  + `executive-brief.md` — 6 domains covered. Не дублировать. Новые prompts
  **закрывают gaps**, не повторяют.
- **Reference prompt style:** `prompts/research-market-ai-native-companies/01-perplexity-deep-research.md`
  (первый Perplexity prompt, well-formatted, с `===BEGIN PROMPT TO PASTE===` /
  `===END===` markers).
- **24 locked decisions** + D1-D4 foundation — учитываются при scoping каждого prompt.

## Required reading (before writing prompts)

1. `raw/research/master-inventory-2026-04-22.md` — ВЕСЬ, особенно Part 5 (gaps) + Part 6 (priorities)
2. `raw/research/perplexity-market-ai-native-2026-04-22/executive-brief.md` — чтобы понять уже-covered territory
3. `prompts/research-market-ai-native-companies/01-perplexity-deep-research.md` — reference style для new prompts
4. `decisions/JETIX-ARCHITECTURE-BRIEF.md` §10 (16 architect questions) + 24 locks list (Locks 19-24 особенно важны для P1-1 и P1-2)

Skim only:
- `raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md` — чтобы не повторять CE findings
- `raw/articles/2026-04-22-every-compound-engineering-guide.md` — чтобы не повторять Every guide

## Deliverables (8 prompts + 1 launcher + 1 raw-sources spec)

Путь: `prompts/phase-2-deep-research-2026-04-22/`

### File 01 — `01-matchmaker-capability-capsule-production.md`

**Gap:** Phase 1 Part 5 Domain 2 MAJOR — matchmaker + capability-capsule production
examples >1M tasks/mo без supervisor fallback. **Критично для Decision 21**
(Jetix Matchmaker + Roy-Replication).

**Scope for the prompt:**
- Production multi-agent systems using **matchmaker / dispatcher / registry-based**
  task routing (not central coordinator, not flat peer-to-peer)
- Named examples with scale metrics: >1M tasks/mo OR >10 operators concurrent
- Architectures: Ray Serve / Temporal.io dynamic / OpenAI Agents SDK handoff /
  LangGraph supervisor OR alternatives
- **Capability-capsule** pattern (V5 Emergent): tasks match capability registries,
  agents bid for work, self-organize. Specifically find production deployments.
- Failure modes + scaling limits documented by practitioners

**Required output sections:** top 10 named systems + architecture summaries +
scale metrics + citations + what each doesn't solve.

### File 02 — `02-ai-native-os-vertical-stacks.md`

**Gap:** Phase 1 Part 5 Domain 4 MAJOR — opinionated AI-native OS для solo→holding
(no packaged solution exists). **Критично для Decision 24** (open-source research
direction Phase 2+).

**Scope for the prompt:**
- Vertical AI-native OS stacks targeting specific industries (legal / finance /
  healthcare / real estate / consulting)
- Horizontal AI-native OS стеки (Sierra, Decagon, Lindy, Relevance AI) — deep-dive
  их внутренней архитектуры где public
- Solo-founder OS attempts (closed-source products + GitHub projects >5K stars)
- **Gap question:** кто-то ещё пытался сделать «operating system для solo AI
  consultant с path к holding»? Если да — кто? Если нет — почему?
- Open-source candidates Jetix could fork/study

### File 03 — `03-mast-14-modes-jetix-mapping.md`

**Gap:** Phase 1 Part 5 Domain 7 MAJOR — MAST 14-mode taxonomy (Cemri et al.
arXiv:2503.13657) explicit mapping к Jetix 11 agents (failure-mode prevention
matrix). **Критично для compliance + resilience**.

**Scope for the prompt:**
- Full enumeration MAST 14 failure modes с definitions + examples
- For each mode: prevention mechanisms documented in literature (Anthropic,
  DeepMind, CrewAI, AutoGen post-mortems)
- Evidence-based per-mode recommendations (what works, what doesn't, cost
  implications)
- 2-3 documented cases for каждого mode — где это failed production

**Output:** per-mode table: Mode / Description / Jetix-relevant trigger / Prevention
mechanism / Evidence cite / Implementation cost.

### File 04 — `04-anthropic-mailbox-pattern-primary-sources.md`

**Gap:** Phase 1 Part 5 Domain 2 MAJOR — Anthropic mailbox pattern primary-source
verification. Jetix mailboxes.jsonl architecture based on this — нужна ground truth.

**Scope for the prompt:**
- Primary sources: Anthropic engineering blog posts, conference talks (YouTube),
  arXiv papers, official docs, leaked materials (WaveSpeed Apr 2026 if confirmable)
- Mailbox / message-queue patterns в multi-agent systems production
- JSONL queue patterns (not just in-memory) — scaling properties, failure modes
- Alternatives: Temporal durable execution / Inngest / Kafka-based agent queues
- **Specific output:** direct quotes from Anthropic engineers + URL + date of
  each claim. Verification for WaveSpeed leak — real or fake?

### File 05 — `05-project-management-methodologies-ai-native.md`

**New domain (9):** Project management methodologies для AI-native teams 2026.
**Ruslan directive:** collect best practices + combine с CE + code-writing = new
unified Jetix philosophy.

**Scope for the prompt:**
- **Shape Up (Basecamp):** 6-week cycles, betting table, hill charts, appetite —
  как адаптируется к AI-native teams?
- **Scrum / Kanban / Agile:** still relevant 2026 в AI contexts? Where does it
  break?
- **Linear Method** (Linear.app blog): modern alternative to Scrum, built for
  software teams — full documentation
- **Lean / Theory of Constraints** (Goldratt) — bottleneck thinking + AI
- **SAFe / PRINCE2 / PMBOK:** enterprise methodologies — relevant для solo
  founder path к holding?
- **Emerging 2026 methodologies:** specifically AI-native team management patterns
  (any named?)

**Special sub-question:** как Shape Up 6-week cycle ↔ CE Plan→Work→Review→Compound
loop combine? Кто-то уже делал этот mapping?

### File 06 — `06-product-management-methodologies-ai-native.md`

**New domain (9 cont.):** Product management.

**Scope for the prompt:**
- **Marty Cagan:** Inspired / Empowered / TRANSFORMED books — empowered product
  teams, discovery vs delivery, outcomes over outputs. Detailed treatment.
- **Teresa Torres — Continuous Discovery Habits:** opportunity solution tree,
  story mapping, weekly customer contact. Specific practices.
- **Jobs-to-be-Done (Christensen / Ulwick):** outcome-driven innovation,
  switch interview method
- **Lean Startup (Ries):** build-measure-learn, MVP, pivots — still relevant
  в AI era?
- **OKRs (Doerr Measure What Matters):** vs KPIs vs North Star Framework
- **ICE / RICE / WSJF prioritization** — which works в AI workflows?
- **Product-led growth** (OpenView, Pendo)
- **Category design** (Lochhead «Play Bigger» / Wiegers)

**Special sub-question:** how does PM practice integrate with CE's $100 rule and
50/50 rule? Какой role Product Manager имеет в compound-engineering team? Кто
писал про это?

### File 07 — `07-management-philosophy-deep.md`

**New domain (9 cont.):** Management philosophy + organizational design.

**Scope for the prompt:**
- **Andy Grove — High Output Management:** still canonical 2026? OKRs origin,
  1-on-1s, task-relevant maturity, meetings
- **37signals (Basecamp):** Shape Up book, «It Doesn't Have to Be Crazy at
  Work», «Remote», «Rework» — complete philosophy distillation
- **Netflix culture deck** (Hastings / McCord) — radical transparency, informed
  captain, keeper test
- **Stripe playbook** (Rails for Startups, Increment magazine archives) — engineering
  excellence + writing culture
- **Peter Drucker:** effectiveness vs efficiency, knowledge worker, results
  orientation — still applicable?
- **Michael Watkins First 90 Days:** onboarding new roles — applicable к solo
  founder wearing 10 hats?
- **Reed Hastings «No Rules Rules»:** talent density, candor, remove controls
- **Ben Horowitz «Hard Thing About Hard Things»:** hard parts scaling, wartime
  CEO, team building
- **Frederic Laloux «Reinventing Organizations»:** teal organizations,
  self-management, evolutionary purpose

**Special sub-question:** synthesis — какие **3-5 universal management principles**
проходят через ВСЕ 9 источников выше? Что каждая школа добавляет уникального?

### File 08 — `08-raw-primary-sources-catalog.md`

**Special task:** caption list of primary-source material Ruslan должен найти и
добавить в `raw/books-pm/` и `raw/articles/`. Prompt этот — НЕ Perplexity query,
а bibliography spec.

**Format:**
```markdown
## Books to acquire

### Project Management
1. **Shape Up** (Basecamp, Ryan Singer, 2019)
   - Free online: https://basecamp.com/shapeup
   - Download options: PDF, HTML, Kindle
   - Save to: raw/books-pm/shape-up-basecamp-2019.md
   - Priority: P1

2. **High Output Management** (Andy Grove, 1983 rev 1995)
   - Amazon: [ISBN 0679762884]
   - Summary worth capturing: Farnam Street / Ben Horowitz's notes
   - Save to: raw/books-pm/high-output-management-grove.md (summary + key quotes)
   - Priority: P1
...
```

Minimum 15 books + 10 canonical essays/posts. Organized by: PM / Product Mgmt /
Management Philosophy / CE-adjacent (compound engineering additional reading) /
Multi-agent theory.

### File 09 — `LAUNCHER.md`

Launcher instructions для Ruslan:
- Order приоритета запуска (P1 → P2 → P3)
- Per-prompt ETA в Perplexity Deep Research mode
- Куда сохранять output (`raw/research/phase-2-deep-research-2026-04-22/RESULT-XX.md`)
- Когда все 7 results получены — git push → Cloud Cowork начинает Фазу 3 synthesis

## Prompt structure (КАК ПИСАТЬ каждый prompt 01-07)

Каждый prompt follows reference template
`prompts/research-market-ai-native-companies/01-perplexity-deep-research.md`:

```markdown
---
id: phase-2-XX-<domain>
title: ...
tool: Perplexity Pro Deep Research
status: ready-to-run
---

# <Domain> — Perplexity Deep Research Prompt

## Как использовать
1. Открой Perplexity Pro Deep Research mode
2. Скопируй секцию ===BEGIN PROMPT TO PASTE=== до ===END===
3. Paste + submit. Wait 5-30 минут.
4. Сохрани output в `raw/research/phase-2-deep-research-2026-04-22/RESULT-XX.md`
5. Скажи Cloud Cowork

## Context для понимания (не копируй в Perplexity)
[why this matters для Jetix — 3-5 предложений]

## ===BEGIN PROMPT TO PASTE===

[Deep, specific, multi-section prompt with:]
- I need a deep research on [domain]. For production use in [context]. Цитируй каждый claim.
- Research scope: 5-8 concrete sub-domains с названиями систем/компаний/авторов
- Output requirements: per sub-domain: executive summary + top 5 refs + 5-10 findings + gaps
- Constraints: primary sources preferred, 2025-2026 dates preferred, admit uncertainty, no hype
- End with: top 10 actionable items + top 10 projects/sources to investigate deeper + honest
  assessment of gaps

## ===END PROMPT TO PASTE===

## Alternative: split into N focused prompts (optional)

## After Perplexity returns
1. Save в raw/research/phase-2-deep-research-2026-04-22/RESULT-XX.md
2. Flag Cloud Cowork
```

## Quality criteria for each prompt

- **Specific:** named systems / authors / papers, не abstract concepts
- **Evidence-first:** each output section requires citations
- **Date-aware:** 2025-2026 preferred (flag if older)
- **Honest:** prompt explicitly asks Perplexity admit uncertainty
- **Actionable:** output includes top-10 actionable items
- **Length:** each prompt 1500-3000 слов (standalone)
- **Deduplication:** doesn't repeat existing Perplexity research от Apr 22

## Success criteria for YOUR task

- ✅ 7 Perplexity prompts (01-07) written + 1 bibliography spec (08) + LAUNCHER (09)
- ✅ Каждый prompt ready-to-paste (no editing needed by Ruslan)
- ✅ Каждый закрывает specific gap из Phase 1 Part 5 OR расширяет на PM domain
- ✅ Цитируемые reference-lists in bibliography (File 08)
- ✅ Commit + push per template below

## Workflow (2-3 часа)

1. Read required inputs (30-45 min)
2. Write 01-matchmaker (20 min)
3. Write 02-ai-native-os (20 min)
4. Write 03-mast-jetix (20 min)
5. Write 04-anthropic-mailbox (20 min)
6. Write 05-project-mgmt (25 min)
7. Write 06-product-mgmt (25 min)
8. Write 07-management-philosophy (25 min)
9. Write 08-raw-sources-bibliography (30 min)
10. Write 09-LAUNCHER (15 min)
11. Self-review: each prompt deduplicates existing, ready-to-paste, cites primary sources? (15 min)
12. Commit + push

## Commit template

```
git add prompts/phase-2-deep-research-2026-04-22/
git commit -m "[prompts] Phase 2 — 7 Perplexity deep research prompts + bibliography + launcher"
git push origin claude/jolly-margulis-915d34
```

## Anti-patterns

- ❌ НЕ делай actual research (не ищи ответы — пишешь prompts)
- ❌ НЕ дублируй existing Perplexity coverage (6 domains Apr 22)
- ❌ НЕ добавляй новые Locks / decisions
- ❌ НЕ переводи prompt content на русский — Perplexity лучше работает на English
- ❌ НЕ делай prompts короче 1500 слов (они будут поверхностными)

---

*END META-INSTRUCTIONS*
