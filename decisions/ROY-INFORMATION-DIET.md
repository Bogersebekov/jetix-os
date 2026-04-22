---
id: roy-information-diet
title: ROY Information Diet — what the swarm reads, how, and in what order
date: 2026-04-22
author: cloud-cowork (draft v2 с Ruslan правками)
status: draft-v2
parent: decisions/METHOD-OF-DEVELOPMENT.md (future)
related:
  - Notion: Создание метода разработки + самого метода (34a2496333bf810f9058fc783ce179e2)
---

# 🎯 TWO-LAYER DISTILLATION (v3 — Ruslan directive)

Рой читает 17 subcategory'ев. Из ВСЕХ знаний ДОЛЖЕН distill'ить в **два
параллельных слоя** (orthogonal к base/overlay split §1.1).

## Layer α — Philosophical Layer
**Что:** Как система ДОЛЖНА БЫТЬ. Первые принципы. Quality / cleanliness /
integrity / epistemic discipline. Strategic navigation lens.

**Источники (pull from):** 3.1 CE (50/50, $100 rule) + 3.7 Management
Philosophy (Drucker, 37signals, Laloux) + 3.8 Systems Thinking
(Meadows/Senge/Levenchuk/FPF) + 3.9 Cybernetics (Ashby, Beer VSM) + 3.11
Investing (Munger, Taleb antifragile) + 3.12 Mental Models (Kahneman, Deutsch,
Ahrens Zettelkasten) + 3.13 Biology/Evolution (Dennett universal algorithm) +
3.14 Philosophical Strategic (Naval, Stoic, Tao, Finite/Infinite Games) + 3.15
Philosophy of Science (Popper falsifiability, Kuhn paradigms, Lakatos
programmes)

**Deliverable для роя:** `decisions/PHILOSOPHICAL-LAYER-DISTILLATION.md` —
20-40 first principles что делают систему чистой/качественной/evolvable.

**Применение:** когда architecture/tactics conflict — philosophical layer
breaks tie.

## Layer β — System + Code Layer
**Что:** Как система ПОСТРОЕНА. Architecture. Engineering practices. Code
quality. Concrete patterns.

**Источники (pull from):** 3.1 CE (agents / skills / Plan-Work-Review-Compound
loop) + 3.2 AI-native OS + 3.3 Linux / Unix Philosophy (Raymond, Kernighan) +
3.4 Clean Code (Ousterhout, Pragmatic Programmer, Refactoring) + 3.5 PM (Shape
Up workflow) + 3.6 Product Mgmt (Discovery → Delivery loops) + 3.9 Cybernetics
(VSM implementation) + 3.10 Complexity (Scale laws, networks) + 3.16
Engineering Foundations (Koen heuristics, Vincenti knowledge, Petroski
failure, TRIZ, first principles) + 3.17 Agent primary sources

**Deliverable для роя:** `decisions/SYSTEM-CODE-LAYER-DISTILLATION.md` —
concrete engineering patterns + architectural primitives.

**Применение:** implementation decisions — какие patterns / tools / structures
использовать.

## Overlap (намеренный)
Некоторые domains (3.8 Systems Thinking, 3.9 Cybernetics) питают ОБА слоя —
это OK. Рой сам решает какой aspect куда.

## Ortho check
- **§1.1 Layer 1/2 = WHAT we build** (meta-system base / Jetix overlay)
- **§α/β = HOW we think about it** (philosophical / system-code)
- Independent axes. Результат роя должен explicitly adress оба.

---

# ⚠️ КРИТИЧЕСКИЕ UPDATES v2 (Ruslan 2026-04-22)

1. **Мета-система сначала, Jetix overlay потом.** Рой ДОЛЖЕН сперва построить
   **универсальную мета-систему** (operating system для solo-founder / systems
   thinker — Jetix-agnostic), потом на неё **наложить Jetix overlay**
   (philosophy + 24 Locks + archetypes + trajectory). Это base/overlay pattern.
   D1 Vision §4 + V1 Conservative §3 уже хинтуют этот подход (`jetix-os/` =
   универсальное ядро).
2. **Locks/Principles** = 24 LOCKED decisions Ruslan утвердил на Stages 2/2B.
   Лежат в 3 файлах TENSIONS-*.md. Рой НЕ изобретает новые Locks — использует
   existing, может challenge'ить конкретные с evidence.
3. **Human-in-the-loop обязательно.** Рой должен поддерживать ДВА режима:
   (A) Full auto — работает autonomously, Ruslan review'ит финальный deliverable;
   (B) Stage-gated — на каждом meaningful stage рой pauses, Ruslan review'ит,
   корректирует, направляет. Ruslan выбирает режим per-iteration.
4. **Deeper OUR REQUEST** — раскрыто подробно ниже (§Category 1 v2).
5. **Multiple domain experts communicate через wiki/** — подтверждено. Subagent
   per domain, все пишут structured summaries в wiki/foundations/, brigadier
   читает summaries.
6. **Full versions only** — Ruslan сам достанет все raw books. Никаких summaries
   instead of full (summaries как supplement OK).
7. **Category 3 updates:**
   - REMOVED: Sales (но система должна быть sales-ready overlay'ем)
   - REMOVED: Law
   - ADDED: Biology + Evolution (P1 — для self-evolving system pattern)
   - ADDED: Naval Ravikant philosophy layer (в Mental Models + отдельный
     philosophical/strategic layer)
   - ADDED: Philosophical Strategic layer — Naval + system-wide strategic
     navigation lens

---

# Information Diet для Роя

> **Цель документа.** Определить **что именно рой должен прочитать** до того как
> начать строить Jetix архитектуру. Разделено на 3 категории (запрос / self /
> specific). Всё с prioritization: MUST / SHOULD / MAY.

---

## Разделение на 3 категории

1. **OUR REQUEST (наш запрос)** — цели, success criteria, constraints, что мы
   ждём на выходе
2. **SELF-KNOWLEDGE (о нас)** — все документы про Jetix: vision / philosophy /
   plan / architecture / locks / wiki / current state
3. **SPECIFIC KNOWLEDGE (внешние знания)** — всё что не про Jetix но критично
   для построения правильной архитектуры (CE / PM / systems / Linux / etc.)

---

## Category 1 — OUR REQUEST (v2 — deeper, со всех сторон)

Рой получает explicit контракт. Описан со всех сторон: сверху (vision),
снизу (implementation), середины (workflow), сзади (constraints),
меета-сверху (what is "success").

### 1.1 Mission — two layers

**Layer 1 — Universal Meta-System (base, Jetix-agnostic):**

Построить **универсальную operating system** для solo-founder / systems-thinker
/ предпринимателя управляющего:
- **Проектами** (multiple concurrent work streams)
- **Жизнью** (life OS: health / learning / relationships / finances)
- **Знаниями** (wiki / memory / compounding knowledge)
- **Агентами** (AI swarm doing work, stigmergic coord)
- **Коммуникацией** (human↔agents + agents↔agents + human↔human)

Эта система должна быть **universal** — её можно натянуть на любую
философию / vision / startup / holding. Jetix-agnostic core.

**Layer 2 — Jetix overlay (specific application):**

Натянуть на универсальную meta-system:
- Jetix philosophy (D2: anti-attention / cascading-leverage / engineering-faith /
  investment-fund / predator-outside / gentleman-inside / и т.д.)
- 24 LOCKED decisions
- 11 archetypes ICP + 5 criteria filter
- Phase-trajectory €0 → €50K → €200K → €1M → $1T
- Investment-fund operating philosophy
- Identity patterns (gentleman/predator, open/closed, layered)
- USB-C positioning (Phase 3+)
- Methodology as durable asset (Westinghouse analog)

Deliverable должен clearly показать boundary: **что base (universal) / что
overlay (Jetix-specific)**. Overlay можно заменить на другую философию — base
работает.

### 1.2 Success criteria (expanded v2)

Рой выдаёт успешный результат если:

**Base (Universal) criteria:**
- ✅ Clear base/overlay separation (как файлы, не только doc-level)
- ✅ Base system runnable без Jetix overlay (теоретический test: если overlay
  убрать, base всё равно работает)
- ✅ Base поддерживает любую overlay-philosophy (pluggable)
- ✅ Domains покрыты: проекты / жизнь / знания / агенты / коммуникация
- ✅ System evolvable: self-improving, learning from its own work (biology /
  evolution pattern)

**Jetix-specific criteria:**
- ✅ Все 24 LOCKED decisions respected ИЛИ explicitly challenged с
  justification (если challenge — argue с evidence, не просто override)
- ✅ Каждое architectural choice обосновано ≥2 research citations
- ✅ Anti-patterns (16 штук, D4 §7) НЕ присутствуют
- ✅ Phase-1 ship-able (7-14 дней launch)
- ✅ Phase-3 scalable (≤30% refactor at each 10× gate)
- ✅ Cost <€800/mo при baseline использовании
- ✅ Top-20 insights (Master Inventory Part 4) integrated ИЛИ отвергнуты с
  reason
- ✅ Minimum 3 variants (not 1) — чтобы Ruslan мог выбрать
- ✅ Sales-ready как **overlay pattern** (система готова принять sales overlay
  когда понадобится, но он не часть base Phase 1)

**Workflow criteria (human-in-the-loop):**
- ✅ Система поддерживает ДВА режима работы (см. §1.5 ниже)

### 1.3 Что НЕ делать

- ❌ НЕ изобретать новые Locks / Principles — использовать existing 24 Locks
- ❌ НЕ дублировать existing research — cite instead
- ❌ НЕ предлагать 11-agent roster если нет evidence что Rule of 4 для Jetix
  неприменим
- ❌ НЕ предлагать complex multi-agent там где single-agent работает (Walden
  Yan warning)
- ❌ НЕ делать hand-waving («trust me, this scales») — нужна explicit math
- ❌ НЕ игнорировать $47K incident pattern — cost cap ON BILLING LEVEL
- ❌ НЕ мешать base и overlay — держать boundary явно
- ❌ НЕ строить sales / law / HR subsystems Phase 1 (только base + Jetix
  overlay)

### 1.4 Deliverable format

- `decisions/META-SYSTEM-UNIVERSAL-BASE.md` — базовая универсальная мета-система
  описание (новый документ, рой создаёт)
- `decisions/JETIX-OVERLAY-ON-META-SYSTEM.md` — Jetix overlay applied к base
  (новый документ)
- `decisions/JETIX-FINAL-SYSTEM-SYNTHESIS-iteration-N.md` — 3-5 variants (base +
  overlay) с rationale + evidence
- Scoring table (10 axes × N variants)
- Migration plan от current state к выбранной variant
- Risk register (concrete + mitigations)
- `prompts/next-iteration/` — prompts для следующего compound cycle

### 1.5 Two operating modes (CRITICAL — human-in-the-loop)

**Mode A — Full Auto (для простых задач):**
- Brigadier делегирует → эксперты делают → brigadier синтезирует → commit
- Ruslan review'ит финальный deliverable
- Compound в wiki/ automatically
- Используется для: routine tasks, well-defined scope, low-stakes decisions

**Mode B — Stage-Gated Interactive (для стратегических):**
- Brigadier делит задачу на **named stages** (minimum 3-5 stages)
- После КАЖДОГО stage рой pauses → commits intermediate deliverable →
  уведомляет Ruslan
- Ruslan может:
  - **Approve** → рой идёт дальше
  - **Redirect** → изменить направление / constraints
  - **Drill-down** → запросить deeper investigation конкретного aspect
  - **Abort** → остановить и сохранить current state
- Protocol: specific file pattern `stage-<N>-<name>-AWAITING-APPROVAL.md` +
  `stage-<N>-<name>-DECISION.md` для Ruslan response
- Используется для: architecture decisions, strategic pivots, new patterns,
  anything touching 24 Locks

**Meta-mode selector:** Ruslan выбирает режим при запуске задачи. Default для
architecture работы = Mode B. Default для routine refactor = Mode A.

### 1.6 Communication channels (human↔swarm)

Помимо file-based stages, рой должен поддерживать:
- **Telegram/Slack notifications** когда stage completed + waiting
- **Comment thread** в specific intermediate file (Ruslan пишет comments, рой
  read'ит в next iteration)
- **Voice memo ingestion** (existing pipeline: voice → transcript → /ingest)
- **Notion page updates** для high-level status (mirror git state)

### 1.2 Success criteria

Рой выдаёт успешный результат если:
- ✅ Все 24 LOCKED decisions respected ИЛИ explicitly challenged с justification
- ✅ Каждое architectural choice обосновано ≥2 research citations (не только
  opinion)
- ✅ Anti-patterns (16 штук, D4 §7) не присутствуют
- ✅ Phase-1 ship-able (7-14 дней launch)
- ✅ Phase-3 scalable (≤30% refactor at each 10× gate)
- ✅ Cost verifiably <€800/mo при baseline использовании
- ✅ Top-20 insights (из Master Inventory Part 4) integrated либо explicitly
  отвергнуты с reason
- ✅ Minimum 3 variants (not 1) — чтобы Ruslan мог выбрать

### 1.3 Что НЕ делать

- ❌ Не изобретать новые Locks / Principles (использовать existing)
- ❌ Не дублировать existing research — cite instead
- ❌ Не предлагать 11-agent roster если нет evidence что Rule of 4 для Jetix
  неприменим
- ❌ Не предлагать complex multi-agent там где single-agent работает (Walden
  Yan warning)
- ❌ Не делать hand-waving ("trust me, this scales") — нужна explicit math
- ❌ Не игнорировать $47K incident pattern — cost cap ON BILLING LEVEL

### 1.4 Deliverable format

- `decisions/JETIX-FINAL-SYSTEM-SYNTHESIS-iteration-N.md` (3-5 variants, каждый
  с rationale + evidence)
- Scoring table (10 axes × N variants)
- Migration plan от current state к выбранной variant
- Risk register (concrete + mitigations)
- `prompts/next-iteration/` — prompts для следующего compound cycle

---

## Category 2 — SELF-KNOWLEDGE

Всё про Jetix. **MUST read fully.** Читается целиком — не скимить.

### 2.1 Foundation (APPROVED)

- `decisions/JETIX-VISION.md` (D1, 495 lines) — identity, 11 archetypes, $1T
  trajectory
- `decisions/JETIX-PHILOSOPHY.md` (D2, 983 lines) — operating principles +
  mental models
- `decisions/JETIX-PLAN.md` (D3, 923 lines) — phased roadmap + revenue gates
- `decisions/JETIX-ARCHITECTURE-BRIEF.md` (D4, 842 lines) — tech skeleton +
  10-axes rubric + 16 architect questions
- `design/JETIX-FPF.md` (3758 lines constitutional — skim ToC + §1-4 + key
  sections)

### 2.2 24 LOCKED decisions (non-negotiable)

- `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md`
  (Locks 1-8)
- `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md`
  (Locks 9-18)
- `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md`
  (Locks 19-24)

### 2.3 Current system state

- `CLAUDE.md` (master config, ~170 lines)
- `.claude/rules/global.md`
- `.claude/agents/` (14 current agent definitions)
- `.claude/skills/` (11 active skills)
- `design/AGENT-PROTOCOLS.md` (852 lines — per-agent protocols)
- `design/DATA-FLOWS.md` (1091 lines — how data moves)

### 2.4 Voice of Ruslan (primary source)

- `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-FULL-DIGEST.md`
  (805 lines — top 50 quotes)
- `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md`
  (367 quotes, 1477 lines)
- `raw/voice-memos-text/holding-vision-2026-04-21.md` (6 primary text notes
  driving Locks 19-24)

### 2.5 Previous attempts (inputs, NOT candidates)

- `decisions/variants/JETIX-ARCH-V1-V5.md` (5 Stage 6 variants — reference
  only, рой может предложить своё)
- `decisions/variants/_STAGE-7-SCORING-AND-SUMMARIES.md` (cross-audit scoring)

### 2.6 Historical context (skim)

- `decisions/2026-04-19-architecture-v2-approval.md` (ADR Chunks 1-8)
- `raw/research/architecture-variants-2026-04-22/ATOM-REGISTRY.md` (3626 atoms —
  SEARCHABLE backup, не linear read)
- `raw/research/architecture-variants-2026-04-22/KNOT-MAP.md` (navigation)

---

## Category 3 — SPECIFIC KNOWLEDGE (external)

Это **самый большой** блок. Разделён на 12 субкатегорий. Для каждой: MUST /
SHOULD / MAY priority.

### 3.1 Compounding Engineering (MUST, уже в repo)

**Priority:** P0 (foundation of the method)

- `raw/articles/2026-04-22-every-compound-engineering-guide.md` — canonical
  Every / Kieran Klaassen guide
- `raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md`
  (synthesis v2)
- `raw/research/compounding-engineering-2026-04-22/R-1..R-11.md` — 11 research
  files (prioritize R-2 swarm, R-7 Boris Cherny, R-8 Skills, R-9 agentic
  loop, R-10 continual learning)

### 3.2 Multi-agent / AI-native OS (MUST, уже в repo)

**Priority:** P0

- `raw/research/perplexity-market-ai-native-2026-04-22/executive-brief.md`
  (TL;DR + 10 bullets + 3 decisions)
- `raw/research/perplexity-market-ai-native-2026-04-22/perplexity-output.md`
  (full, 6 domains, 350KB — skim executive sections per domain)
- [Future Phase 2] `prompts/phase-2-deep-research-2026-04-22/` outputs когда
  готовы

### 3.3 Linux / Unix philosophy (ADD, need to acquire)

**Priority:** P1 (foundational для filesystem-centric stigmergic design)

- **The Art of Unix Programming** (Eric Raymond, 2003) — 17 rules of Unix
  philosophy, каждый rule = insight для stigmergic design
  - Free online: http://www.catb.org/~esr/writings/taoup/
  - Save to: `raw/books-external/art-of-unix-programming-raymond.md`
- **The Unix Programming Environment** (Kernighan & Pike, 1984) — canonical
  pipelines + composability
- **Linux Philosophy for SysAdmins** (David Both, 2018) — современное
  переосмысление Unix для systems engineers
- **The Pragmatic Programmer** (Hunt & Thomas, 20th anniv ed 2019) — pragmatic
  disciplines, "broken windows", orthogonality — applies directly к Jetix
  agent design

### 3.4 Clean Code / Software Engineering (ADD)

**Priority:** P1

- **A Philosophy of Software Design** (John Ousterhout, 2nd ed 2021) — deep
  modules vs shallow, strategic vs tactical programming — ключ для agent
  boundary design
- **Clean Code** (Robert Martin, 2008) — classic, каждый code review agent
  должен это знать
- **Code Complete** (Steve McConnell, 2004) — comprehensive construction
  practices
- **The Mythical Man-Month** (Fred Brooks, 1975 + 1995 anniv) — "adding
  manpower to a late project makes it later" — применяется к multi-agent
  scaling
- **Refactoring** (Martin Fowler, 2nd ed 2018) — pattern catalog для code
  evolution

### 3.5 Project Management (ADD, основа для Phase 2 research)

**Priority:** P1

- **Shape Up** (Ryan Singer / Basecamp, 2019) — 6-week cycles, appetite, hill
  charts, betting table. **Free online:** https://basecamp.com/shapeup
- **PMBOK Guide 7th Edition** (PMI, 2021) — canonical reference
- **Scrum Guide** (Schwaber & Sutherland, 2020) — 13 pages, ключевой baseline
- **The Phoenix Project** (Gene Kim, 2013) — DevOps novel, Theory of
  Constraints applied to IT
- **The Goal** (Eliyahu Goldratt, 1984) — Theory of Constraints original
- **Linear Method** (Linear.app public docs) — modern alternative to Scrum

### 3.6 Product Management (ADD)

**Priority:** P1

- **Inspired** (Marty Cagan, 2nd ed 2017) — empowered product teams
- **Empowered** (Cagan & Jones, 2020) — how to build empowered teams
- **Continuous Discovery Habits** (Teresa Torres, 2021) — opportunity
  solution tree + weekly customer contact
- **The Lean Startup** (Eric Ries, 2011) — build-measure-learn, MVP, pivots
- **Jobs to Be Done** (Clay Christensen + Ulwick) — outcome-driven innovation
- **Measure What Matters** (John Doerr, 2018) — OKRs canonical
- **Hooked** (Nir Eyal, 2014) — habit-forming products

### 3.7 Management Philosophy (ADD)

**Priority:** P1

- **High Output Management** (Andy Grove, 1983 rev 1995) — canonical,
  1-on-1s, task-relevant maturity, meetings
- **Shape Up + It Doesn't Have to Be Crazy at Work + Rework + Remote**
  (37signals collection) — complete Basecamp philosophy
- **Netflix Culture Deck** (McCord, 2009 + No Rules Rules 2020) — talent
  density + candor + remove controls
- **First 90 Days** (Michael Watkins, 2013) — onboarding
- **The Hard Thing About Hard Things** (Ben Horowitz, 2014) — wartime CEO
- **The Effective Executive** (Peter Drucker, 1967) — still canonical
- **Reinventing Organizations** (Frederic Laloux, 2014) — teal organizations,
  self-management

### 3.8 Systems Thinking + Левенчук (MUST)

**Priority:** P0 (мы уже построены на этой базе — FPF)

- **Наш FPF + Левенчук корпус (уже в repo):**
  - `raw/research/levenchuk-deep-research-2026-04-18.md` (Левенчук body)
  - `raw/research/levenchuk-for-ai-deep-research-2026-04-19.md` (ШСМ для AI,
    1041 lines)
  - `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md` (FPF KB, 2456
    lines)
  - `raw/research/levenchuk-fpf-research-2026-04-20/R-A..R-E` (5 sub-researches)
  - `design/JETIX-FPF.md` (constitutional doc, 3758 lines)
- **External classics (ADD):**
  - **Thinking in Systems** (Donella Meadows, 2008) — primer, 240 pages,
    foundational
  - **The Fifth Discipline** (Peter Senge, 1990) — organizational systems
    thinking + learning organization
  - **Systems Thinking: Creative Holism for Managers** (Michael Jackson, 2003)
  - **Russell Ackoff** essays — "Systems Thinking for Curious Managers"
  - **Gerald Weinberg** — "An Introduction to General Systems Thinking"

### 3.9 Cybernetics (ADD, foundational)

**Priority:** P1

- **Cybernetics: Or Control and Communication in the Animal and the Machine**
  (Norbert Wiener, 1948 rev 1961) — original source
- **An Introduction to Cybernetics** (W. Ross Ashby, 1956) — Law of Requisite
  Variety, homeostasis — direct application к multi-agent coordination
  - Free online: http://pcp.vub.ac.be/books/IntroCyb.pdf
- **Brain of the Firm** (Stafford Beer, 1972) — Viable System Model (VSM),
  5 systems of viable org — almost literally applicable к Jetix
- **The Heart of Enterprise** (Stafford Beer, 1979) — VSM applied
- **Understanding Understanding** (Heinz von Foerster, 2003) — second-order
  cybernetics, observer в системе
- **Out of Control** (Kevin Kelly, 1994) — biological complexity, distributed
  systems, emergence

### 3.10 Complexity Science (ADD)

**Priority:** P2

- **Complexity: A Guided Tour** (Melanie Mitchell, 2009) — Santa Fe Institute
  primer
- **The Origin of Wealth** (Eric Beinhocker, 2006) — complex adaptive systems
  applied to economy
- **Scale** (Geoffrey West, 2017) — universal scaling laws, power laws —
  applicable к startup trajectory
- **Emergence** (Steven Johnson, 2001) — bottom-up systems, ant colonies,
  cities
- **Link** (Albert-László Barabási, 2002) — network theory basics

### 3.11 Investing / Value Thinking (ADD)

**Priority:** P2 (поможет для Jetix Investment-Fund direction + Ruslan decisions)

- **The Intelligent Investor** (Benjamin Graham, rev ed Zweig) — value
  investing canonical
- **Common Stocks and Uncommon Profits** (Philip Fisher, 1958) — quality
  growth investing
- **Poor Charlie's Almanack** (Charlie Munger) — mental models, multidisciplinary
  thinking
- **The Most Important Thing** (Howard Marks, 2011) — risk + cycles
- **Warren Buffett Shareholder Letters** (1977–present, annualletters.com)
- **The Essays of Warren Buffett** (Cunningham, compiled)
- **Fortune's Formula** (William Poundstone, 2005) — Kelly criterion,
  position sizing
- **Antifragile** (Nassim Taleb, 2012) — antifragility, optionality, via
  negativa — directly applicable к Jetix resilience design
- **Skin in the Game** (Taleb, 2018)

### 3.12 Mental Models / Meta-Science (ADD)

**Priority:** P2

- **Thinking, Fast and Slow** (Daniel Kahneman, 2011) — System 1/2, cognitive
  biases
- **Superforecasting** (Philip Tetlock, 2015) — forecasting practices
- **How to Take Smart Notes** (Sönke Ahrens, 2017) — Zettelkasten — directly
  applicable к wiki/ design
- **The Beginning of Infinity** (David Deutsch, 2011) — epistemology,
  explanatory knowledge
- **Structure and Interpretation of Computer Programs** (SICP, Abelson &
  Sussman, 1996) — composition, abstraction — foundational computational
  thinking
- **Goedel, Escher, Bach** (Hofstadter, 1979) — self-reference, strange
  loops — applicable к recursive self-improvement

### 3.13 Biology / Evolution (ADD — P1, Ruslan directive v2)

**Priority:** P1 — чтобы система понимала что она сама будет эволюционировать;
использовать biological/evolutionary patterns как design hints.

- **The Selfish Gene** (Richard Dawkins, 1976, rev ed) — replicators, units of
  selection, memes — applicable к skill propagation / knowledge transfer в
  agent systems
- **The Blind Watchmaker** (Dawkins, 1986) — cumulative selection / design
  without designer — прямо applicable к recursive self-improvement pattern
- **At Home in the Universe** (Stuart Kauffman, 1995) — self-organization,
  order for free, edge of chaos — для emergence patterns в multi-agent
- **The Origins of Order** (Kauffman, 1993, техническая) — complex adaptive
  systems theory
- **Darwin's Dangerous Idea** (Daniel Dennett, 1995) — evolution as universal
  algorithm; design space exploration
- **Signals and Boundaries** (John Holland, 2012) — complex adaptive systems
  foundational (Santa Fe Institute)
- **Nonzero** (Robert Wright, 2000) — non-zero-sum cooperation patterns in
  evolution → applicable к agent-to-agent + human-to-agent cooperation
- **The Major Transitions in Evolution** (Maynard Smith & Szathmáry, 1995) —
  how new levels of complexity emerge (replicators → cells → multicellular →
  societies) — template для Jetix phase transitions $1M → $100M → $1B → $1T

**Design takeaway для Jetix:** system как evolvable organism, не как static
architecture. Variation + selection + replication loop built-in.

### 3.14 Philosophical Strategic Layer (ADD — P1, Ruslan directive v2)

**Priority:** P1 — направляющий стратегический слой. Это не "что читать" а "как
думать о целом". Meta-navigation layer.

**Naval Ravikant — комплексно:**

- **The Almanack of Naval Ravikant** (Eric Jorgenson, 2020) — free PDF
  https://www.navalmanack.com/ — comprehensive compilation
- **Naval Podcast "How to Get Rich (Without Getting Lucky)"** — tweet storm 40
  ключевых принципов: https://nav.al/rich
- **Naval Podcast "Becoming Happy"** — philosophy layer
- **Naval Podcast "How to Think Clearly"** — mental models applied
- **4 forms of leverage:** labor / capital / code / media (permissionless vs
  permissioned) — **directly applicable к Jetix Phase 1-3 leverage stacking**
- **Specific knowledge** concept — unique unscalable skill + rare combinations
  (applicable к 11 archetypes filter)
- **Product + media leverage** as foundation для solo-to-holding trajectory

**Дополнительно philosophical:**

- **Meditations** (Marcus Aurelius) — stoic operational philosophy
- **The Daily Stoic** (Ryan Holiday, 2016) — applied stoicism
- **Tao Te Ching** (Lao Tzu) — wu-wei, strategic non-action, minimal
  interference — applicable к stigmergic coordination
- **The Art of Strategy** (Dixit & Nalebuff, 1991) — game theory applied
- **The 48 Laws of Power** (Greene, 1998) — for predator-outside awareness
- **Finite and Infinite Games** (James Carse, 1986) — infinite games framing
  for $1T trajectory

**Design takeaway для Jetix:** this layer доминирует над всем остальным при
strategic tradeoffs. Когда tactics contradicting — philosophical layer
breaks tie.

### 3.15 Philosophy of Science (ADD — P1, Ruslan directive v3)

**Priority:** P1 — epistemology + falsifiability как basis для decision-making
и для того как рой отличает знание от мнения.

- **The Logic of Scientific Discovery** (Karl Popper, 1959) — falsifiability,
  demarcation problem, risky predictions
- **Conjectures and Refutations** (Popper, 1963) — applied falsificationism
- **The Structure of Scientific Revolutions** (Thomas Kuhn, 1962) — paradigm
  shifts, normal vs revolutionary science
- **Against Method** (Paul Feyerabend, 1975) — anything goes, methodological
  pluralism — critical counterweight
- **Proofs and Refutations** (Imre Lakatos, 1976) — research programmes
  (progressive vs degenerating)
- **The Beginning of Infinity** (Deutsch, уже в §3.12) — explanatory
  knowledge, good explanations as hard-to-vary

**Design takeaway:** каждая claim в outputs роя должна быть falsifiable.
Если research programme degenerating — reject / revise. No unfalsifiable
hand-waving.

### 3.16 Engineering Foundations (ADD — P1, Ruslan directive v3)

**Priority:** P1 — базовый инженерный подход как мышление.

- **Discussion of the Method** (Billy Vaughn Koen, 2003) — heuristics-based
  engineering, state-of-the-art (SOTA), "engineering method = use best
  heuristics available"
- **What Engineers Know and How They Know It** (Walter Vincenti, 1990) —
  engineering knowledge как distinct от scientific knowledge; six categories
  of engineering knowledge
- **To Engineer is Human** (Henry Petroski, 1985) — role of failure в
  engineering design
- **The Evolution of Useful Things** (Petroski, 1992) — incremental design
  evolution
- **Technological Revolutions and Financial Capital** (Carlota Perez, 2003) —
  long-wave technological cycles
- **TRIZ основы** (Genrich Altshuller, "Creativity as an Exact Science" 1984) —
  inventive problem solving, 40 principles, contradiction matrix
- **First Principles Thinking** (Elon Musk stanford talks / Aristotle /
  Descartes method) — reasoning from first principles vs analogy

**Design takeaway:** engineering ≠ science. Engineering = применение
state-of-the-art heuristics under constraints. Рой должен знать что "good
engineering" = appropriate heuristic selection, не proof.

### 3.17 Bonus — Agent / AI primary sources (ADD for deeper context)

**Priority:** P1

- **Anthropic engineering blog** (all posts 2024-2026)
- **Karpathy tweets + blog + YouTube** (LLM OS + LLM Wiki + System Prompt
  Learning + Software is Changing Again — YC Jun 2025)
- **Paul Gauthier (Aider) blog** — single-agent AI practices
- **Boris Cherny talks + Builder.io interview** — Claude Code architect voice
- **Walden Yan "Don't Build Multi-Agents"** (cognition.ai blog)
- **Kim et al. arXiv:2512.08296** — 260 configs study
- **Cemri et al. arXiv:2503.13657** — MAST 14 failure modes
- **Anthropic "Building Effective Agents"** (Dec 2024)

---

## Reading order (recommended sequence)

**Week 1 (orientation):**
1. Category 1 (OUR REQUEST) — full read, 30 min
2. Category 2 (SELF-KNOWLEDGE) sections 2.1-2.2 (D1-D4 + Locks) — full, 3 h
3. Category 3.1 (CE) + 3.2 (AI-native) already-in-repo synthesis — 2 h
4. Category 2 section 2.3-2.6 (current state + voice) — skim, 2 h

**Week 2 (core methodology):**
5. Category 3.8 (Systems Thinking + Левенчук) — full, 5 h
6. Category 3.3 (Linux) — 3 h
7. Category 3.4 (Clean Code — Ousterhout + Pragmatic Programmer) — 4 h

**Week 3 (management layer):**
8. Category 3.5 (PM) — 6 h
9. Category 3.6 (Product Mgmt) — 6 h
10. Category 3.7 (Management philosophy) — 5 h

**Week 4 (foundational layer):**
11. Category 3.9 (Cybernetics) — 4 h (Ashby + Beer VSM focus)
12. Category 3.10 (Complexity) — 3 h
13. Category 3.11 (Investing) — 3 h
14. Category 3.12 (Meta-models) — 3 h
15. Category 3.13 (Agent primary sources) — 3 h

**Total:** ~55-60 hours reading time for full depth. Можно параллельно /
sub-agent delegated reading.

---

## Ruslan decisions v2 (resolved)

- ✅ **Full versions only** — Ruslan сам достанет raw books. No summaries вместо
  full (summaries allowed как supplement).
- ✅ **Subagent experts per domain** подтверждено (Q5). Каждый expert
  специализируется на своей category, пишет structured summaries в wiki/,
  brigadier читает summaries + selectively drills-down.
- ✅ Sales — **REMOVED** (but system must be sales-ready overlay)
- ✅ Law — **REMOVED**
- ✅ Biology / Evolution — **ADDED** §3.13 (P1)
- ✅ Naval Ravikant + philosophical layer — **ADDED** §3.14 (P1)

## Expert-per-domain mapping (Ruslan decision Q5)

Каждая category в §3 получает dedicated subagent-expert. Experts взаимодействуют
**только через wiki/** (stigmergic — не direct messaging):

| Expert | Owns categories | Output path |
|---|---|---|
| `ce-expert` | 3.1 Compounding Engineering | `wiki/foundations/ce/` |
| `ai-native-expert` | 3.2 Multi-agent / AI-native OS + 3.15 agent primary | `wiki/foundations/ai-native/` |
| `unix-expert` | 3.3 Linux / Unix philosophy + 3.4 Clean Code | `wiki/foundations/engineering/` |
| `pm-expert` | 3.5 PM + 3.6 Product Mgmt | `wiki/foundations/pm/` |
| `mgmt-expert` | 3.7 Management philosophy | `wiki/foundations/mgmt/` |
| `systems-expert` | 3.8 Systems Thinking + Левенчук + 3.9 Cybernetics + 3.10 Complexity | `wiki/foundations/systems/` |
| `investor-expert` | 3.11 Investing / Value | `wiki/foundations/investing/` |
| `meta-expert` | 3.12 Mental Models + 3.13 Biology/Evolution | `wiki/foundations/meta/` |
| `philosophy-expert` | 3.14 Philosophical Strategic Layer (Naval + др.) | `wiki/foundations/philosophy/` |

**Brigadier** читает summaries из wiki/foundations/, synthesizes, делегирует
drill-downs при необходимости. Experts могут читать друг друга через wiki (не
pinging напрямую).

## Acquisition status (v2 — simple)

- **Free online** (рой может сразу начать): Shape Up, Ashby Cybernetics,
  Art of Unix Programming, Naval Almanack, Меditations, Tao Te Ching, все
  наши уже-в-repo материалы (CE guide, Perplexity, research)
- **Ruslan достанет FULL versions** остальных:
  - High Output Management (Grove)
  - Inspired + Empowered (Cagan)
  - Thinking in Systems (Meadows)
  - The Fifth Discipline (Senge)
  - Pragmatic Programmer
  - A Philosophy of Software Design (Ousterhout)
  - Selfish Gene + Blind Watchmaker (Dawkins)
  - At Home in the Universe (Kauffman)
  - The Major Transitions in Evolution (Maynard Smith)
  - Continuous Discovery Habits (Torres)
  - Measure What Matters (Doerr)
  - 37signals collection (Shape Up already + ReWork + Crazy + Remote)
  - Stoic canon, Buffett letters, Munger almanack
  - [Full list fully in §3 above]
- Save to: `raw/books-external/<subcategory>/<slug>.pdf` or `.md`

## Open questions для обсуждения (Ruslan — остались только эти)

### Q1 — Scope приоритет
v2 диета ~60-70 часов. Слишком много? Режем до P0+P1 only (~35-40h)?

### Q2 — Что ещё добавить?
- **Economics** (Hayek / Coase / Ostrom governance commons) — для holding
  Phase 3?
- **Philosophy of Science** (Popper / Lakatos / Feyerabend) — для
  falsifiability / research methodology?
- **Design / UX** (Norman / Rams) — для surface design когда дойдём?
- Другое?

### Q3 — Mode A vs Mode B default
Default operating mode для next iteration:
- Mode A (full auto) — для скорости
- Mode B (stage-gated) — для safety + learning
- Mixed — начинаем в B, переключаем в A когда доверие накоплено?

---

## Next steps

1. **Ruslan review** — ответить на Q1-Q6 выше
2. **Finalize diet** — v2 based on feedback
3. **Acquisition plan** — что free / что paid / что summaries
4. **Delegate reading** — через subagents (брать paths, возвращать
   structured notes в `wiki/foundations/<topic>.md`)
5. **Proceed к Шагу 2** (baseline swarm setup) с полной diet готовой
