---
id: roy-information-diet
title: ROY Information Diet — what the swarm reads, how, and in what order
date: 2026-04-22
author: cloud-cowork (draft for Ruslan review)
status: draft-v1
parent: decisions/METHOD-OF-DEVELOPMENT.md (future)
related:
  - Notion: Создание метода разработки + самого метода (34a2496333bf810f9058fc783ce179e2)
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

## Category 1 — OUR REQUEST

Рой должен получить explicit контракт: что мы хотим, чего НЕ хотим, как
меряется успех.

### 1.1 Mission statement

Создать **несколько вариантов адекватной системы** для:
- Управления проектами Jetix
- Управления Jetix как holding (Phase 3+)
- Управления самими агентами
- Коммуникации между агентами (stigmergic, не direct messaging)

Система должна:
- Работать в рамках €800/mo Phase-1 budget
- Поддерживать trajectory Phase 0 (€0) → Phase 1 (€50K) → Phase 2 (€200K) →
  Phase 3 (€1M+) без fundamental rewrite
- Integrated с CE main loop (Plan → Work → Review → Compound)
- Rule-of-4 compatible (3-4 active + fan-out reviewers)
- Stigmergic coordination через filesystem + git
- Evidence-first: каждая claim с citation

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

### 3.13 Bonus — Agent / AI primary sources (ADD for deeper context)

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

## Open questions для обсуждения (Ruslan)

### Q1 — Scope creep check
55-60 часов reading diet = too much? Режем до MUST only (~20 h)?

### Q2 — Специфические добавки
Что я упустил из того что ты имел в виду:
- **"базовые науки"** — что именно? Math? Physics? Biology?
- **"методологии"** кроме PM/PdM/CE?
- **Кибернетика** — я включил Wiener + Ashby + Beer. Достаточно?

### Q3 — Acquisition path
- Shape Up + Ashby + Unix Philosophy — FREE online, можно сразу добавить в
  `raw/books-external/`
- High Output Management / Inspired / Thinking in Systems / etc. — нужны
  купленные PDF/EPUB. Как достаём?
- Альтернатива: summaries от Farnam Street / derekshanks / Readwise —
  быстрее но поверхностнее

### Q4 — Priority recalibration
P0 = CE + AI-native + Левенчук/FPF + Self-knowledge. Согласен?
P1 = Linux + Clean Code + PM + PdM + Mgmt philosophy + Cybernetics + Agents.
P2 = Complexity + Investing + Mental Models.

### Q5 — Читают люди (рой) или subagents
Brigadier читает всё? Или раздаём:
- Systems-thinker expert → 3.8-3.10
- PM expert → 3.5-3.7
- Software expert → 3.3-3.4 + 3.13
- Investor expert → 3.11
- Meta expert → 3.12 + coordination
Все пишут summaries в wiki/, brigadier читает summaries.

### Q6 — Missed categories?
- **Biology / Evolution** (Dawkins / Kauffman) — для emergence patterns?
- **Economics** (Hayek / Coase / Ostrom) — для governance?
- **Philosophy** (Popper / Lakatos) — для scientific method / falsifiability?
- **Law** — для EU AI Act compliance?
- **Design** (Don Norman / Dieter Rams) — для UI/UX?
- **Marketing / Sales** (April Dunford / Blair Enns) — для positioning?

---

## Next steps

1. **Ruslan review** — ответить на Q1-Q6 выше
2. **Finalize diet** — v2 based on feedback
3. **Acquisition plan** — что free / что paid / что summaries
4. **Delegate reading** — через subagents (брать paths, возвращать
   structured notes в `wiki/foundations/<topic>.md`)
5. **Proceed к Шагу 2** (baseline swarm setup) с полной diet готовой
