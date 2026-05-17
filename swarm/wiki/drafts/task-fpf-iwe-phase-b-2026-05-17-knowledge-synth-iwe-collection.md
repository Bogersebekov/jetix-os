---
title: "IWE Deep Collection — FMT-exocortex-template Synthesis"
type: deep-synthesis
expert: knowledge-synth
task_id: task-fpf-iwe-phase-b-2026-05-17
date: 2026-05-17
F: F4
G: distillation-3
R: refuted-if-iwe-mis-encoded
prose_authored_by: claude-scribe
confidence: medium
confidence_method: artefact-direct-read
primary_source: raw/external/tseren-github-2026-05-17/FMT-exocortex-template/
phase_a_base: reports/fpf-iwe-distillation-2026-05-17/02-u-episteme-and-iwe.md
note: >
  Paid IWE platform (aisystant.system-school.ru) still blocked per
  corpus-inventory §3 blocker 3. This synthesis is ENTIRELY from the
  public FMT-exocortex-template GitHub repo (314 files) + Phase A
  conceptual base. Empirical IWE AI-guide interaction not available.
---

# IWE Deep Collection — FMT-exocortex-template Synthesis

> **Rubric coverage:** sections 1-8 per brigadier brief.
> **Constitutional posture:** R1 scribe — surface what IWE IS, not whether it is good.
> Contradictions and definition gaps surfaced as plain facts.

---

## §1 IWE Verbatim Definitions

### 1.1 IWE (Intellectual Work Environment)

**Primary definition (English):**
> «An operating system for intellectual work. Your knowledge. Your experience.
> Your environment — runs on top of any AI platform.»
`[README.en.md L7]`

**Formal expansion:**
> «**IWE (Intellectual Work Environment)** — an intellectual work environment. Just
> as an IDE combines editor, compiler, and debugger into one environment for a
> programmer — IWE combines knowledge, planning, and AI agents into one environment
> for thinking.»
`[README.en.md L29-31]`

**Russian version (verbatim):**
> «**IWE (Intellectual Work Environment)** — интеллектуальная рабочая среда.»
`[README.md L29]`

**ONTOLOGY abbreviation entry:**
> `IWE | Среда интеллектуальной работы | Intellect Work Environment | Pack`
`[ONTOLOGY.md L79]`

**LEARNING-PATH definition:**
> «IWE — персональная система для интеллектуальной работы и развития. Как IDE
> объединяет редактор, компилятор и дебаггер в одну среду для программиста — так
> IWE объединяет знания, планирование и ИИ-агентов в одну среду для мышления.»
`[docs/LEARNING-PATH.md L29]`

**Pack-referenced conceptual anchor:**
> `Среда (IWE) | Environment (IWE) | DP.CONCEPT.002 | Корневое понятие — шаблон развёртывает IWE`
`[ONTOLOGY.md §2 row 1]`

### 1.2 Exocortex (Экзокортекс)

**Glossary definition (README.en.md):**
> «**Exocortex** | Your external memory — files with plans, context, conclusions
> that Claude reads in every session»
`[README.en.md L49]`

**Russian README:**
> «**Экзокортекс** | Ваша внешняя память — файлы с планами, контекстом, выводами,
> которые Claude читает в каждой сессии»
`[README.md L48]`

**ONTOLOGY entry:**
> `Экзокортекс-интерфейс | Exocortex Interface | DP.EXOCORTEX.001 | CLAUDE.md + memory/ — ядро шаблона`
`[ONTOLOGY.md §2 row 2]`

**Memory layer description:**
> «Слой памяти | Memory Layer | Уровень хранения инструкций экзокортекса
> (Layer 1: MEMORY.md, Layer 2: CLAUDE.md, Layer 3: memory/*.md) | DP.EXOCORTEX.001»
`[ONTOLOGY.md §3]`

### 1.3 Pack

**Glossary entry (README.en.md):**
> «**Pack** | Formalized knowledge base for your domain — the single
> source-of-truth for domain knowledge»
`[README.en.md L50]`

**CLAUDE.md structural definition:**
> «**Pack** | Паспорт предметной области | Да (пользователь)»
`[CLAUDE.md §1 row 2]`

**Canonical elaboration (README.md):**
> «Pack — единственный source-of-truth для доменного знания.»
`[README.md L80]`

**FAQ answer:**
> «A: Формализованная область знаний — единственный source-of-truth для доменного
> знания.»
`[README.md L216]`

**Position in fallback chain:**
> «Pack = source-of-truth для доменного знания. DS меняется вслед за Pack.»
`[CLAUDE.md §1]`

### 1.4 OWC / ОРЗ (Open → Work → Close)

**Glossary entry (README.en.md):**
> «**OWC** | Open → Work → Close — a ritual for every session and every day,
> prevents context loss»
`[README.en.md L51]`

**Русский вариант:**
> «**ОРЗ** | Открытие → Работа → Закрытие — ритуал для каждой сессии и каждого
> дня, предотвращает потерю контекста»
`[README.md L50]`

**ONTOLOGY term:**
> `ОРЗ | Открытие-Работа-Закрытие | Open-Work-Close | Pack`
`[ONTOLOGY.md L81]`

**ONTOLOGY implementation name:**
> `Ритуал ОРЗ | ORZ Ritual | Реализация протокола сессии: Открытие → Работа → Закрытие | DP.M.003`
`[ONTOLOGY.md §3]`

**Fractal structure (CLAUDE.md):**
> «Три стадии, три масштаба. Пропуск Открытия = незапланированная работа. Пропуск
> Закрытия = незафиксированный результат.»
`[CLAUDE.md §2 — header]`

### 1.5 ArchGate (АрхГейт)

**Glossary entry (README.en.md):**
> «**ArchGate** | Structured evaluation of architectural decisions across 7
> characteristics (instead of "I think it's fine")»
`[README.en.md L52]`

**ONTOLOGY implementation entry:**
> `АрхГейт (ЭМОГССБ) | ArchGate | Обязательная оценка архитектурного решения по 7
> характеристикам, порог ≥8 | DP.M.005`
`[ONTOLOGY.md §3]`

**7 characteristics (ЭМОГССБ acronym):**
> `ЭМОГССБ | 7 арх. характеристик | Evolvability, Scalability, Learnability,
> Generativity, Speed, Modernity, Security | Pack`
`[ONTOLOGY.md L84]`

**CLAUDE.md rule (БЛОКИРУЮЩЕЕ):**
> «Архитектурное решение → /archgate → принципы (DP.ARCH.001 §7) → профиль ЭМОГССБ
> (✅/⚠️/❌) → conjunctive screening. Без агрегатного балла —
> feedback_decision_gates.md.»
`[CLAUDE.md §5]`

### 1.6 Strategist (Стратег, R1)

**Glossary entry (README.en.md):**
> «**Strategist** | AI agent that automatically creates daily/weekly plans and
> tracks progress»
`[README.en.md L53]`

**Role card:**
> «Стратег (R1) | Claude CLI (по расписанию) | Планирование, рефлексия, подготовка
> к сессиям | Каждое утро, вечер, неделя»
`[docs/LEARNING-PATH.md L94]`

**Two modes:**
> «Операционный: Планирует, отслеживает, отчитывается. Горизонт: День → неделя.
> Стратегический: Помогает осознать НЭП, выбрать методы. Горизонт: Неделя → месяц → год.»
`[roles/strategist/README.md — режимы работы table]`

### 1.7 FMT (Format / Template)

**CLAUDE.md repository type table:**
> «**Base** (Принципы + Форматы) | ZP, FPF, SPF, FMT-* | Да (платформа)»
`[CLAUDE.md §1 row 1]`

**REPO-TYPE.md:**
> «**Тип**: Base/Форматы. **Система (SoI)**: cross-cutting.»
`[REPO-TYPE.md L2-4]`

**ONTOLOGY abbreviation:**
> `FMT | Формат (шаблон) | Format (Template) | Template`
`[ONTOLOGY.md L86]`

### 1.8 ZP (Zero Principles / Нулевые принципы)

**ONTOLOGY:**
> `ZP | Нулевые принципы | Zero Principles | Base`
`[ONTOLOGY.md L99]`

**Hierarchy position (docs/principles-vs-skills.md):**
> «Level 0: ZP | Нулевые принципы (трансдисциплины) | Способность разбираться в
> ЛЮБОМ новом домене | Каждая смена области = начало с нуля»
`[docs/principles-vs-skills.md L17]`

**Generative chain:**
> «ZP (думать) → FPF (описывать) → Pack (знать) → DS (делать)»
`[docs/principles-vs-skills.md L52]`

### 1.9 FPF (First Principles Framework)

**ONTOLOGY:**
> `FPF | Фреймворк первых принципов | First Principles Framework | FPF`
`[ONTOLOGY.md L70]`

**Usage context:**
> «Когда читать FPF: При работе с концепциями Level 1 (мета-онтология); при
> неясности базовых различений (Role/Method/Work, System/Episteme); при создании/
> проверке Pack на соответствие FPF.»
`[memory/fpf-reference.md L19-23]`

**Upstream dependency:**
> «FPF (First Principles Framework)» listed in REPO-TYPE.md L11 as upstream dependency
`[REPO-TYPE.md L11]`

### 1.10 SPF (Second Principles Framework)

**ONTOLOGY:**
> `SPF | Фреймворк вторых принципов | Second Principles Framework | SPF`
`[ONTOLOGY.md L71]`

**Position in hierarchy:**
> «Level 1: FPF | Первые принципы (рамка корректности)… Level 2: Pack | Вторые
> принципы (доменное знание)»
`[docs/principles-vs-skills.md L18-19]`

**Note:** SPF = "Second Principles Framework" in IWE vocabulary; Левенчуковская
FPF Spec uses "FPF" as the master spec. IWE introduces SPF as a distinct
intermediate layer between FPF and Pack. [ПРОБЕЛ: SPF.SPEC.002 text not in
public repo — only referenced.]

### 1.11 DS (Downstream Repository)

**ONTOLOGY:**
> `DS | Downstream-репозиторий | Downstream Repository | Template`
`[ONTOLOGY.md L85]`

**CLAUDE.md definition:**
> «**DS** (instrument/governance/surface) | Код, планы, курсы | Нет (производное от Pack)»
`[CLAUDE.md §1 row 3]`

**Fallback chain position:**
> «Fallback Chain: DS → Pack → Base (SPF → FPF → ZP)»
`[CLAUDE.md §1]`

### 1.12 AR (Agent Rules / Правила агента)

**Definition from CLAUDE.md:**
> «Source-of-truth (WP-272 Ф1, 26 апр): правила формализованы в
> PACK-agent-rules/rules/AR.NNN.md с frontmatter (id, type, priority, triggers,
> tests, hook).»
`[CLAUDE.md §2 — blocking rules preamble]`

**Priority hierarchy:**
> «Иерархия при конфликте: правила пронумерованы по приоритету (= AR-priority в
> Pack). Структурное (1-5) ВСЕГДА перевешивает поведенческое (6-10).»
`[CLAUDE.md §2 — blocking rules preamble]`

### 1.13 WP / РП (Work Product / Рабочий продукт)

**ONTOLOGY abbreviations:**
> `WP | Рабочий продукт | Work Product | SPF`
> `РП | Рабочий продукт (экземпляр) | Work Product (instance) | Pack`
`[ONTOLOGY.md L77, L82]`

**WP Context File entry:**
> `Файл контекста РП | WP Context File | DP.EXOCORTEX.001 | inbox/WP-*.md в DS-strategy`
`[ONTOLOGY.md §2]`

**WP Gate definition:**
> `WP Gate | Блокирующая проверка наличия РП в плане перед началом работы | DP.EXOCORTEX.001`
`[ONTOLOGY.md §3]`

---

## §2 IWE = Production-Applied FPF — Mapping Table

> Per Левенчук TG 2026-05-17: «У Церена IWE, там примерно всё так же устроено.
> Но внутри там интеллект опирается на тот же FPF.»

IWE explicitly loads FPF as upstream. The REPO-TYPE.md lists FPF as an upstream
dependency. The memory/fpf-reference.md is a template-level file that all IWE
users inherit — it maps FPF patterns to IWE usage contexts. Below is the mapping
from Phase A FPF primitives/mechanisms to IWE operational constructs.

### FPF Primitives → IWE Operationalisation

| FPF Primitive (Phase A label) | IWE Operationalisation | IWE File/Construct | Source |
|-------------------------------|------------------------|-------------------|--------|
| **U.System** (holon with 4D boundary) | Экзокортекс, Claude Code CLI, Telegram-bot, MCP servers, Neon DB — each is a System with lifecycle | LEARNING-PATH.md Вид 1 table | `[docs/LEARNING-PATH.md L57-65]` |
| **U.Episteme** (knowledge claim with DescribedEntity + Viewpoint) | Pack-document = formalized episteme per domain. Pack = single source-of-truth so DescribedEntity boundary is bounded-context-scoped | PACK architecture + DP.EXOCORTEX.001 | `[README.en.md L50]` + `[ONTOLOGY.md §2]` |
| **U.BoundedContext** (A.1.1) | Pack = one BC per domain. UL = ontology.md in each Pack. Context Map = typed related: edges. | SOTA-reference SOTA.001 DDD Strategic | `[memory/sota-reference.md L37]` |
| **Role ≠ Method ≠ Work** (A.7 triada) | «IWE as system is examined through 5 viewpoints: Systems, Descriptions, Roles, Methods, Work Products. Central organizing principle — FPF A.7 triada» | LEARNING-PATH.md §1.2 | `[docs/LEARNING-PATH.md L50]` |
| **F-G-R** (trust tags per claim) | SOTA.006 Agentic Development references F-G-R. fpf-reference.md maps F-G-R to: «Факт / предположение / слух — уровень доверия к данным» | memory/fpf-reference.md | `[memory/fpf-reference.md L131]` |
| **ADI Cycle** (Abduction-Deduction-Induction B.5) | ArchGate evaluation uses ADI per fpf-reference: «Гипотеза → проверка логикой → проверка данными» | memory/fpf-reference.md L137 | `[memory/fpf-reference.md L137]` |
| **Multi-View publication (MVPK)** | Five-viewpoint IWE description (§1.2 LEARNING-PATH): Systems / Descriptions / Roles / Methods / Work Products = multi-view per ISO 42010 | LEARNING-PATH.md §1.2 | `[docs/LEARNING-PATH.md L49-50]` |
| **DRR (Decision Record)** | WP Gate + Ритуал согласования = decision record before any WP opens. WP-context files = structured decision records | CLAUDE.md §2 WP Gate | `[CLAUDE.md §2]` |
| **Causal Use CAL (C.28)** | fpf-reference.md §C.28 maps IWE usage: «Активация C.28 — когда утверждение меняет то, что допустимо для публикации, деплоя» | memory/fpf-reference.md L102 | `[memory/fpf-reference.md L88-120]` |
| **Strict Distinction (A.7)** | `.claude/rules/distinctions.md` = IWE's distinctions file; 17+ hard distinctions maintained as enforced rules | `.claude/rules/distinctions.md` | `[.claude/rules/distinctions.md L1-19]` |

### FPF Mechanisms → IWE Implementation

| FPF Mechanism | IWE Implementation | Notes |
|---------------|-------------------|-------|
| Alpha-state tracking (past-participle) | WP Registry: РП with statuses (pending/in_progress/done). WP-context file per РП | `[ONTOLOGY.md — Реестр РП entry]` |
| Competence accumulation loop | OWC protocol at session/day/week/month scale + Capture-to-Pack | `[CLAUDE.md §2 fractal table]` |
| Knowledge formalization | Extractor role (R2) pipeline: Обнаружение → Классификация → Маршрутизация → Формализация → Валидация → Одобрение → Запись | `[roles/extractor/README.md]` |
| Role-executor separation | role.yaml schema: `id:` (FPF role type) ≠ `type: agential|functional` (executor kind). Holder pattern in prompts | `[roles/ROLE-CONTRACT.md L48-66]` |
| Context isolation for verification | Верификатор (R23) loads: артефакт + эталон + чеклист. Does NOT load: задание создателя, историю итераций | `[roles/verifier/README.md L31-37]` |
| Fallback chain for epistemics | DS → Pack → Base (SPF → FPF → ZP). «Если на уровне DS непонятно — поднимаешься к Pack» | `[docs/principles-vs-skills.md L21]` |

---

## §3 IWE Intelligence Amplification — OWC Workflow Map

### 3.1 Core principle

> «**Ключевой принцип: экзоскелет, не протез.** IWE усиливает ваше мышление, а не
> заменяет его. После каждой сессии вы становитесь компетентнее, а не просто
> получаете результат.»
`[README.md L41]`

Three mechanisms of exoskeleton (not prosthesis):
1. **Предъявление, а не генерация** — AI shows user's own knowledge (Pack, memory/, Digital Twin) at the right moment
2. **Вопросы, а не ответы** — WP Gate forces planning before action; Consultation T2-T3 asks «а ты как думаешь?»
3. **Убывающие подмостки (scaffolding)** — Tiers T0→T4: more help at initial levels, less at advanced
`[docs/LEARNING-PATH.md §1.1a L36-46]`

### 3.2 OWC Fractal — Level-by-Level Artifacts

**Fractal rule:** «Три стадии, три масштаба.»
`[CLAUDE.md §2 header]`

| Scale | Open | Work | Close | Artifacts Produced |
|-------|------|------|-------|-------------------|
| **Session** | protocol-open.md § Сессия | protocol-work.md | /run-protocol close | WP-context updates, Capture proposals |
| **Day** | /day-open «открывай» | Between Day Open and Day Close | /run-protocol day-close | DayPlan file, updated MEMORY.md |
| **Week** | — (Monday strategy session) | Между Week opens | /run-protocol week-close | WeekPlan, WeekReport, Memory rotation |
| **Month** | — | Between Month Closes | /month-close (первый Пн месяца) | MonthClose.md, multiplier trend archive |

`[CLAUDE.md §2 — ОРЗ-фрактал table]`

**DayPlan definition:**
> `DayPlan | Дневной план — артефакт Day Open. Handoff Стратег→Человек | DP.M.003`
`[ONTOLOGY.md §3]`

**WeekPlan definition:**
> `WeekPlan | Недельный план — артефакт стратегирования. Содержит РП, бюджеты, фокус | DP.M.003`
`[ONTOLOGY.md §3]`

### 3.3 Capture-to-Pack — Knowledge Extraction at Checkpoints

**Definition:**
> `Capture-to-Pack | Рубежная проверка: есть ли знание для записи в Pack | DP.M.001`
`[ONTOLOGY.md §3]`

**Protocol rule:**
> «**Capture-to-Pack** — на каждом рубеже: есть ли знание для записи? Анонсировать:
> «Capture: [что] → [куда]». Маршрутизация: правило (1-3 строки) → CLAUDE.md,
> доменное → Pack, реализационное → DS docs/, урок → memory/.»
`[CLAUDE.md §2 — Протокол Работы]`

### 3.4 User Learning Path (Tiers)

| Tier | Description | Access Layer |
|------|-------------|-------------|
| T0 | /start in bot, trial 30 дней, базовый поиск | No Git |
| T1 | Регистрация, ассистент | No Git |
| T2 | Программы, Марафон, бот + контент | No Git |
| T3 | Digital Twin, Профиль + цели, Наставник | No Git |
| T4 | setup.sh, Claude Code, Стратег + планы, Со-мыслитель | Git + IWE template |

`[docs/LEARNING-PATH.md §1.3 L162-166]`

**Key invariant:**
> «T0–T3 работают без Git — всё через бот. T4 добавляет Claude Code, Git,
> автоматических агентов.»
`[docs/LEARNING-PATH.md §1.3 L171]`

---

## §4 IWE vs FPF — Additions and Gaps

### 4.1 What IWE ADDS that FPF does NOT contain

| IWE Construct | FPF Analog (if any) | What IWE Adds |
|---------------|---------------------|---------------|
| **Pack** | U.BoundedContext + U.Episteme (abstract) | Concrete distribution format: folder structure, frontmatter schema, SPF pack-template, routing rules. FPF defines boundaries conceptually; Pack operationalises them as Git repos with mandatory ontology.md + manifest + entity cards. |
| **OWC / ОРЗ Fractal** | Alpha-state lifecycle (abstract) | Session/day/week/month ritual binding. FPF describes alpha-states but has no specific temporal ritual for regular knowledge capture. OWC introduces the concrete rhythm. |
| **ArchGate (ЭМОГССБ)** | A.7 lawful comparison (abstract) | 7-characteristic evaluation template + ≥8 pass threshold + conjunctive screening. FPF has lawful comparison patterns but no specific 7-factor checklist for software architecture. |
| **Exocortex memory layers** | U.Episteme + U.Description (abstract) | 3-layer memory implementation: MEMORY.md (Layer 1, hot) / CLAUDE.md (Layer 2, platform) / memory/*.md (Layer 3, warm/cold). Concrete file + frontmatter lifecycle. |
| **DS → Pack → Base fallback chain** | Fallback not explicit in FPF kernel | IWE operationalises fallback as: «if unclear at DS level → go to Pack → SPF → FPF → ZP.» FPF defines holons but not this vertical drill-down sequence. |
| **Strategist role (R1) as automation** | U.RoleAssignment (abstract) | Scheduled launchd/cron agent that generates DayPlan + WeekPlan + WeekReview headlessly. FPF has no operational scheduling construct. |
| **Creative Pipeline** | No FPF analog | «4 стадии превращения мысли в публикацию: заметка → черновик → заготовка → пост. Каждый артефакт обязан продвинуться или быть закрыт в пределах TTL» `[ONTOLOGY.md §3]`. FPF has no publication TTL concept. |
| **Digital Twin (ЦД)** | No FPF analog | «Цифровой двойник | Digital Twin | DP.CONCEPT.001 | MCP ddt — метамодель, цели, самооценка» `[ONTOLOGY.md §2]`. Personalized progress tracking stored in Neon DB. |
| **Harness pattern** | No FPF analog | «IWE как harness для интеллектуальной работы» `[ONTOLOGY.md §2 — DP.D.025]`. The wrapping/harness metaphor for an environment running on top of any AI platform. |
| **4-contour system (L1-L4)** | No FPF analog | Ecosystem → Platform → Template → Personal IWE layering. `[docs/LEARNING-PATH.md §2.1]` |
| **WP Gate (blocking rule)** | No FPF analog | «ЛЮБОЕ задание → протокол Открытия → ДО начала работы.» Formalized work-registration gate before any task. `[CLAUDE.md §2 rule 1]` |
| **TTL on artifacts** | No FPF analog | `TTL | Срок жизни артефакта | Time To Live | Template` `[ONTOLOGY.md L87]` |

### 4.2 What IWE SKIPS from FPF (or defers to advanced tiers)

| FPF Element | IWE Status | Evidence |
|-------------|-----------|---------|
| **Full U.Episteme slot graph** (DescribedEntity / GroundingHolon / ClaimGraph / Viewpoint slots) | Not explicitly surfaced. IWE uses Pack as "domain episteme" but does not enforce four-slot structure on Pack entities. | ONTOLOGY.md references DP.EXOCORTEX.001 but not U.EpistemeSlotGraph |
| **CausalUse-CAL (C.28)** | Present in memory/fpf-reference.md as a warm reference, NOT as a blocking rule in CLAUDE.md. | `[memory/fpf-reference.md L85-120]` — warm, not blocking |
| **Quantum-Like Modeling Lens (C.26/SOTA.020)** | Listed in sota-reference.md as conditional SOTA — only after exhausting classical toolkit. | `[memory/sota-reference.md L31-32]` |
| **D-Ethics / Conflict patterns** | Not surfaced in any IWE rule or protocol. | Absent from CLAUDE.md, ONTOLOGY.md |
| **E-Constitution / Authoring patterns** | Only author_mode: false / true in params.yaml. No FPF Part E authorship protocol. | `[params.yaml L66-69]` |
| **F-Terminology Unification (UTS / Bridges)** | Partially surfaced via hard-distinctions.md, but no formal UTS linkage. | `.claude/rules/distinctions.md` |

---

## §5 IWE Intellectual Lineage — Architectural Layering

### 5.1 The Fallback Chain (explicit)

```
DS (instrument / governance / surface repos)
  └─ Pack (domain knowledge passport — source-of-truth)
       └─ Base: SPF (Second Principles Framework)
              └─ FPF (First Principles Framework)
                    └─ ZP (Zero Principles / transdisciplines)
```

`[CLAUDE.md §1]`, `[docs/principles-vs-skills.md L21]`, `[ONTOLOGY.md L99]`

**Rule:** «Fallback Chain: DS → Pack → Base (SPF → FPF → ZP)»
`[CLAUDE.md §1]`

### 5.2 Generative Hierarchy (not just fallback)

> «ZP (думать) → FPF (описывать) → Pack (знать) → DS (делать)»
> «Каждый уровень **порождает** следующий. Без верхних уровней нижние не возникают
> или возникают медленно и хрупко.»
`[docs/principles-vs-skills.md L52, L59]`

| Level | What it provides | Without it |
|-------|-----------------|-----------|
| ZP | Transfer between domains (transdisciplines) | Every domain change = start from zero |
| FPF | Precision language: Role ≠ Method ≠ Work ≠ Capability | Everything called «process» — confusion |
| Pack | Domain source-of-truth: distinctions, methods, failure modes | Tribal knowledge, every project from scratch |
| DS | Skills, programs, tools — concrete execution | Nothing to do |

`[docs/principles-vs-skills.md L17-19]`

### 5.3 FMT → DS Propagation Chain

**FMT (Format) type:**
> «**Base/Форматы** (FMT) — template distribution. After forking, becomes your personal environment.»
`[README.en.md L9]`

**Distribution model:**
- Upstream FMT-exocortex-template = source-of-truth for template format
- User forks → DS instantiation (L4 Personal IWE)
- `update.sh` delivers Platform-space changes (L1-L3) while preserving User-space
- 3-way merge preserves user's extensions/, params.yaml, §9 CLAUDE.md edits
`[README.en.md L177]`

### 5.4 Pack ONTOLOGY lineage

**ONTOLOGY.md header:**
> «Downstream-онтология по SPF.SPEC.002 §4.3. Ссылается на понятия Pack DP (Digital
> Platform) и SPF. Собственные понятия не вводит — только реализационные.»
`[ONTOLOGY.md L3-5]`

**Upstream dependencies:**
> `SPF (SPF.SPEC.002) | Base | Виды сущностей, правила онтологии, аббревиатуры`
> `PACK-digital-platform (DP) | Pack | Доменные понятия, различения, архитектура платформы`
`[ONTOLOGY.md §1]`

---

## §6 IWE Hard Distinctions (Authored "Жёсткие Различения")

Source: `.claude/rules/distinctions.md`

| Distinction | Formulation (verbatim) | Source |
|-------------|----------------------|--------|
| **IWE name** | «IWE = Intellectual Work Environment (не «Intelligent», не «Working»). Аналогия: IDE.» | `[distinctions.md L3]` |
| **Развитие ≠ Образование** | «Не использовать: «школа», «вуз», «студент», «преподаватель».» | `[distinctions.md L4]` |
| **Скилл ≠ Роль ≠ Протокол** | «Точечное действие / контекст сессии / ритуал ОРЗ.» | `[distinctions.md L5]` |
| **Pack-знание ≠ Реализационное решение** | «(HD #29). Доменная истина → Pack. Технический выбор → DS.» | `[distinctions.md L7]` |
| **OwnerIntegrity** | «Один факт — одно место. Дублирование Pack↔DS = ошибка синхронизации.» | `[distinctions.md L8]` |
| **WP-context ≠ Результат работы** | «Context в governance-репо, результат в целевом DS/Pack.» | `[distinctions.md L9]` |
| **Персона ≠ Память ≠ Контекст** | «(HD #27, DP.D.050). Критерий: writer + owner. Git / Neon / runtime.» | `[distinctions.md L10]` |
| **Проблема ≠ Задача ≠ ФР ≠ Работа** | «(HD #24, DP.D.053). Ступор / метод известен / спецификация / физ.мир.» | `[distinctions.md L11]` |
| **Система ≠ Роль** | «(D.141 PD). Носитель существует независимо; роль = функциональное место, переносима.» | `[distinctions.md L12]` |
| **Экзоскелет ≠ Автопилот** | «(DP.D.046). Усиление мышления / LLM автономно. Тест: можешь объяснить без «ИИ подсказал»?» | `[distinctions.md L13]` |
| **Лог ≠ Инцидент ≠ State file** | «(DP.D.049). Хронология у исполнителя / сбой+разбор в governance / снимок у исполнителя.» | `[distinctions.md L14]` |
| **Скрипт ≠ Агент** | «(DP.D.048). Фиксированный flow / LLM выбирает шаг. Тест: уберу LLM — сломается?» | `[distinctions.md L15]` |
| **Проектировать роль агента в контексте** | «не «проектировать агента» (DP.D.025).» | `[distinctions.md L19]` |

**From README (distinction stated, not in distinctions.md):**
> «IWE — not a collection of prompts. It's a **work culture**: 14 elements
> (protocols, skills, formats)»
`[README.en.md L62]`

> «Obsidian — хранилище заметок. IWE — **рабочая среда** с протоколами, ИИ-агентами
> и формализацией знаний.»
`[README.md FAQ — L222]`

---

## §7 IWE Roadmap Signals from CHANGELOG.md

### 7.1 Recently Added (last 30 days — April 17 → May 17, 2026)

Current version: **0.31.0** (released 2026-05-17)

**0.31.0 (2026-05-17) — same day as this synthesis:**
- Full set of promote scripts: `script-promote.sh`, `hook-promote.sh`, `skill-promote.sh` + `validate-fmt-scripts.sh` (L1-flow WP-5)
- S-44: Telegram reminders promoted to L1 platform rule (rule 8 in CLAUDE.md)
- S-33 (Hooks/Scripts Bypass Gate) promoted to L1 §2 platform rules
- Knowledge Routing Gate (WP-216 Ф4): `routing-vocab.md` fast-path + DP.SC.036
- Cross-platform path leaks detector
- Secret Drift Detector: `iwe-grep-secret.sh` MVP
- S-45 Agent Inbox (WP-324): `extensions/agent-inbox/` structure with 5 prompt templates; status: **testing** (CCR-automation waiting for RemoteTrigger v2 API spec)
- News Lens: step 6a Day Open — Haiku subagent news synthesis
- q-scale of week quality in Week Close
- Agent Fault Profile: process for tracking agent mistakes

`[CHANGELOG.md 0.31.0 lines 9-30]`

**0.30.0 (2026-05-11):**
- S-19/S-20/S-21 promoted from author zone: `week-draft-init.sh`, `week-draft-append.sh`, `check-script-collisions.sh`
- `docs/SCRIPT-PROMOTION.md` — 7-step promotion process
- `knowledge_repo` parameter in params.yaml for weekly post draft accumulation

`[CHANGELOG.md 0.30.0 lines 47-60]`

**0.29.32 → 0.29.29 (2026-05-06):** Multiple WP-294 Sync Gate fixes (WP context actualization on mention), race-guard for state files. `[CHANGELOG.md L61-114]`

**0.29.28 (2026-05-05):** `scripts/template-sync.sh` — author IWE → FMT auto-sync. `[CHANGELOG.md L118-121]`

**0.29.27 (2026-05-05):** Pull-on-Touch rule extended from write to read+write. `[CHANGELOG.md L127-131]`

**0.29.25 (2026-05-04):** Month Close → Strategy Session cycle (WP-196 Ф13) added. `[CHANGELOG.md L142-148]`

**0.29.24 (2026-05-02):** Strategist migration to template-form with placeholders. `[CHANGELOG.md L154-163]`

**0.29.23 (2026-05-01):** `/personal-guide-start` + `/personal-guide-render` skills. `[CHANGELOG.md L166-173]`

**0.29.21 (2026-04-30):** Memory Lifecycle Protocol — 4 validation scripts (`memory-validate.sh`, `memory-health.sh`, `memory-bleed.sh`, `memory-migrate.sh`). `[CHANGELOG.md L190-205]`

### 7.2 Currently in Testing / Staging

**S-45 Agent Inbox (WP-324):**
> «status: testing (CCR-автоматизация ждёт RemoteTrigger v2 API spec)»
`[CHANGELOG.md 0.31.0 L27]`

This is the most significant staging item: an inbox mechanism for agents
(5 prompt templates: analyze-section, scout-daily, evolution-cron, soak-verify,
_template) implementing DP.SC.135 + DP.ROLE.045.

**From CLAUDE.md §8:**
> «Staging-канал (my IWE → FMT-exocortex-template)» — rules in §9 Author zone
> that are being tested before promotion to L1
`[CLAUDE.md §8]`

**Promotion criteria** (from CLAUDE.md §8):
- `validated` in STAGING.md → remove author constants → replace with `{{PLACEHOLDER}}` → move to FMT + commit `feat: promote S-NN from staging`

### 7.3 Recently Promoted to L1

**Promoted in 0.31.0 (same day):**
- S-33 (Hooks/Scripts Bypass Gate) → L1 platform rule §2 p.6
- S-44 (Telegram reminders) → L1 platform rule §2 p.8

**Previously promoted (CLAUDE.md §8 note):**
> «Перенесено в L1 (20 мар): SC Gate, межсистемные процессы, чеклист-верификация.
> Промотировано в FMT (20 апр): S-13 (именование РП = существительное-артефакт),
> S-14 (синхронизация REGISTRY→производные).»
`[CLAUDE.md §8]`

### 7.4 FPF Freshness Signal

Per `raw/external/ailev-FPF/CHANGELOG-2026-04-20-to-2026-05-16.md`:
- FPF-Spec.md grew from 62,202 → 72,800 lines (+17%) between April 20 and May 16
- New: A.6.P sub-pattern (publication discipline linking SEMIO to role-output artifacts)
- New: E.10.SEMIO clarifications (normative vs informative inscription)
- IWE's fpf-reference.md was last updated 2026-04-06 — predates this expansion

**[ПРОБЕЛ]:** IWE fpf-reference.md does not yet include A.6.P or E.10.SEMIO. These are relevant for IWE's role-output artifacts (DayPlan, WeekPlan = role outputs with publication discipline).

---

## §8 Community and Commercial Layer

### 8.1 Pricing Surface

**Claude subscription:**
> «For full installation (Claude Code) — Claude Pro ($20/mo) is recommended. You
> can upgrade to Claude Max (~$100/mo) for unlimited usage.»
`[README.en.md L202-203]`

> «Для полной установки (Claude Code) — рекомендуется Claude Pro ($20/мес). При
> необходимости можно перейти на Claude Max (~$100/мес) для работы без ограничений.»
`[README.md L204]`

**Minimal install (vendor-neutral):**
> «For minimal installation (setup.sh --core) — works with any AI CLI.»
`[README.en.md L203]`

**Community entry:**
> «Вход — через семинар **«IWE для практиков»** (5000₽) в боте @aist_me_bot.»
`[README.md L266]`

### 8.2 Community Structure

**Free channels:**
- GitHub Discussions: questions, ideas, show your setup
- GitHub Issues: bug reports and feature requests

**Premium community (Telegram, Russian-speaking):**
> «Глубокая практика, разборы рабочих продуктов, прямая поддержка. Вход — через
> семинар «IWE для практиков» (5000₽) в боте @aist_me_bot.»
`[README.md L266]`

**What happens in premium community:**
- Work product reviews (real Pack, plans, retrospectives)
- Installation and customization experience sharing
- Method discussions (OWC fractal, ArchGate, Capture-to-Pack in practice)
- Links and SOTA findings that fit IWE philosophy
`[README.md L248-257]`

### 8.3 Vendor-Neutral Knowledge vs Vendor-Locked Automation

**Knowledge is portable:**
> «All knowledge is stored in open formats (Markdown, YAML, Git) — it will survive
> any vendor switch.»
`[README.en.md L205]`

**Automation is Claude-specific:**
> «But automation (OWC protocols, skills, hooks, roles) is built for Claude Code CLI.
> For Codex (OpenAI), Aider, or other AI CLIs, you'll need to adapt .claude/ and
> role scripts.»
`[README.en.md L205-206]`

**Minimal install escape hatch:**
> «Minimal installation (setup.sh --core) works without vendor lock-in.»
`[README.en.md L206]`

### 8.4 Data Architecture (Three Protection Zones)

> «Three protection zones: local, GitHub (private repos), platform (per-user
> isolation).»
`[README.en.md L217]`

**Central invariant:**
> «Обновления платформы (Standard) **никогда** не затрагивают данные пользователя
> (Personal). Твои планы, знания и стратегия принадлежат тебе.»
`[docs/LEARNING-PATH.md §1.3 L173]`

### 8.5 Bot Entry Point

**@aist_me_bot** — Telegram bot serving as:
- Community entry gate (seminar "IWE для практиков")
- Note inbox for exocortex (`.текст заметки`)
- Telegram notifications (Strategist → user)
- Navigator role (R13 Проводник)

`[README.md L266]`, `[docs/QUICK-START.md L113]`, `[docs/LEARNING-PATH.md L96-98]`

---

## §9 Cross-Reference: IWE Roles Roster

| Role | Code | Type | Executor | Function | Trigger |
|------|------|------|----------|----------|---------|
| Стратег | R1 | agential (Grade 3-4) | Claude CLI | Planning, reflection, session prep | Daily morning (cron/launchd), manual |
| Экстрактор | R2 | agential | Claude CLI | Knowledge extraction → Pack | Session Close, on-demand, every 3h |
| Синхронизатор | R8 | functional (bash) | Bash script | Dispatcher, code scan, daily report, Telegram notify | 11x/day via launchd |
| Верификатор | R23 | agential (Haiku) | Sub-agent Haiku | Artifact verification vs standard (context isolation) | Quick Close, Day Close, Session Close |
| Аудитор | R24 | agential (Sonnet) | Sub-agent Sonnet | Cross-context completeness audit | Day Open, Strategy session, on-demand |
| Проводник | R13 | functional | Telegram bot | Navigation guide for users | On user message |
| Пользователь | — | human | Human | Decisions, creation, reflection | Always |

`[docs/LEARNING-PATH.md Вид 3 L92-98]`, `[roles/ROLE-CONTRACT.md L68-80]`

**Role Contract structure** (mandatory files per role directory):
- `role.yaml` — machine-readable manifest (id, type, display_name, runner, install, priority)
- `README.md` — human description
- `install.sh` — entry point (launchd/cron/no-op)

`[roles/ROLE-CONTRACT.md L9-15]`

---

## §10 Definition Gaps and Contradictions (surface only)

### 10.1 Gaps

**[ПРОБЕЛ G1]:** SPF (Second Principles Framework) spec (SPF.SPEC.002) is referenced throughout but not available in public repo. ONTOLOGY.md references it as upstream but the spec itself is not vendored. Cannot verify SPF-specific patterns.

**[ПРОБЕЛ G2]:** PACK-digital-platform (DP.CONCEPT.002, DP.EXOCORTEX.001, etc.) is referenced as upstream for all IWE concepts but is a separate private/semi-public repo. All DP.* references are unverifiable from this synthesis.

**[ПРОБЕЛ G3]:** IWE AI guide on aisystant.system-school.ru (the paid AI assistant described in Phase A as "FPF-applied") is NOT the same artifact as FMT-exocortex-template. Phase A studied the paid AI guide; Phase B studies the template. These are related but distinct: the template is the self-hosted Claude Code setup; the paid AI guide is the platform-hosted assistant. This synthesis is 100% template-based, not platform AI guide-based.

**[ПРОБЕЛ G4]:** FPF-reference.md last updated 2026-04-06. FPF-Spec.md grew by +10,598 lines (A.6.P, E.10.SEMIO) between April 20 and May 16. IWE's FPF reference file is therefore stale by these additions.

**[ПРОБЕЛ G5]:** PACK-agent-rules (AR.NNN.md) files — the formal source-of-truth for blocking rules — are not in the public repo. CLAUDE.md says rules are «formalized in PACK-agent-rules» but the pack itself is not accessible here.

### 10.2 Contradictions

**[ПРОТИВОРЕЧИЕ C1]:** Phase A (02-u-episteme-and-iwe.md §2.1) described IWE as «AI personal guide that tracks learner progress» based on the aisystant MIM curriculum description. The GitHub FMT-exocortex-template is a different product: it's a self-hosted Claude Code template, not a platform AI guide. Левенчуков TG C5 («у Цэрэна IWE … опирается на тот же FPF») likely referred to the platform IWE, not the template. The template is clearly FPF-derived but the Левенчуков claim may specifically reference the AI guide's reasoning, not the template's OWC protocol.

**[ПРОТИВОРЕЧИЕ C2]:** README.en.md presents IWE as «an operating system for intellectual work» `[L7]` and LEARNING-PATH.md presents it as «персональная система для интеллектуальной работы и развития» `[L29]` — but ONTOLOGY.md entry for IWE abbreviation says «Среда интеллектуальной работы | Intellect Work Environment» `[L79]`. Three slightly different framings: OS for intellectual work / personal system / environment. Not contradictory per se, but the "OS" metaphor is the marketing layer while "environment" is the technical ONTOLOGY-backed term.

**[ПРОТИВОРЕЧИЕ C3]:** CLAUDE.md §1 says «Pack = source-of-truth для доменного знания. DS меняется вслед за Pack.» But the template repo (FMT-exocortex-template) IS the source-of-truth for the template format — it is a Base/FMT type repo, not a DS repo. The fallback chain applies to user's DS repos, not to the template itself. This is a scope distinction, not a logical contradiction, but it requires careful reading.

---

## §11 Synthesis Confidence Statement

**Confidence: MEDIUM**

What is high-confidence (directly read from files):
- All verbatim definitions in §1 (file:line cited)
- OWC fractal structure (§3.2)
- Role roster (§9)
- Distinctions list (§6)
- Pricing surface (§8)
- CHANGELOG recent additions (§7)

What is medium-confidence (inferred from indirect sources):
- FPF → IWE mapping (§2): IWE explicitly uses FPF as upstream; the mapping is structural inference based on how FPF concepts appear in IWE files. The canonical mapping document (PACK-digital-platform) is not accessible.
- IWE vs FPF gap analysis (§4): based on absence of explicit FPF patterns in IWE files — absence ≠ non-existence; they may exist in inaccessible PACK-digital-platform or PACK-agent-rules.

What is NOT in this synthesis (paid platform blocked):
- Empirical IWE AI guide behavior (how it actually reasons, cites FPF, surfaces alternatives)
- Residency context (how IWE works inside МИМ learning programs)
- DP.* concept full definitions (PACK-digital-platform not vendored)
- SPF.SPEC.002 content

---

## Provenance Index (minimum 30 entries)

| # | Path | Range | Quote (≤150 chars) |
|---|------|-------|-------------------|
| 1 | README.en.md | L7 | «An operating system for intellectual work. Your knowledge. Your experience. Your environment» |
| 2 | README.en.md | L29-31 | «IWE (Intellectual Work Environment) — an intellectual work environment» |
| 3 | README.en.md | L49 | «Exocortex — Your external memory — files with plans, context, conclusions that Claude reads» |
| 4 | README.en.md | L50 | «Pack — Formalized knowledge base for your domain — the single source-of-truth» |
| 5 | README.en.md | L51 | «OWC — Open → Work → Close — a ritual for every session and every day, prevents context loss» |
| 6 | README.en.md | L52 | «ArchGate — Structured evaluation of architectural decisions across 7 characteristics» |
| 7 | README.en.md | L53 | «Strategist — AI agent that automatically creates daily/weekly plans and tracks progress» |
| 8 | README.en.md | L202-203 | «Claude Pro ($20/mo) is recommended. You can upgrade to Claude Max (~$100/mo)» |
| 9 | README.en.md | L205-206 | «All knowledge is stored in open formats — it will survive any vendor switch» |
| 10 | ONTOLOGY.md | L70 | `FPF | Фреймворк первых принципов | First Principles Framework | FPF` |
| 11 | ONTOLOGY.md | L79 | `IWE | Среда интеллектуальной работы | Intellect Work Environment | Pack` |
| 12 | ONTOLOGY.md | L81 | `ОРЗ | Открытие-Работа-Закрытие | Open-Work-Close | Pack` |
| 13 | ONTOLOGY.md | L84 | `ЭМОГССБ | 7 арх. характеристик | Evolvability, Scalability, Learnability, Generativity, Speed, Modernity, Security` |
| 14 | ONTOLOGY.md | L85 | `DS | Downstream-репозиторий | Downstream Repository | Template` |
| 15 | ONTOLOGY.md | L99 | `ZP | Нулевые принципы | Zero Principles | Base` |
| 16 | ONTOLOGY.md | §3 | «Ритуал ОРЗ — Реализация протокола сессии: Открытие → Работа → Закрытие — DP.M.003» |
| 17 | ONTOLOGY.md | §3 | «АрхГейт (ЭМОГССБ) — Обязательная оценка архитектурного решения по 7 характеристикам, порог ≥8» |
| 18 | CLAUDE.md | §1 | «Fallback Chain: DS → Pack → Base (SPF → FPF → ZP)» |
| 19 | CLAUDE.md | §1 | «Pack = source-of-truth для доменного знания. DS меняется вслед за Pack.» |
| 20 | CLAUDE.md | §2 | «WP Gate: ЛЮБОЕ задание → протокол Открытия → ДО начала работы» |
| 21 | CLAUDE.md | §2 | «Capture-to-Pack — на каждом рубеже: есть ли знание для записи?» |
| 22 | REPO-TYPE.md | L2-4 | «Тип: Base/Форматы. Система (SoI): cross-cutting» |
| 23 | REPO-TYPE.md | L11 | «FPF (First Principles Framework)» as upstream dependency |
| 24 | docs/principles-vs-skills.md | L17-19 | «Level 0: ZP — Level 1: FPF — Level 2: Pack — Level 3: DS» |
| 25 | docs/principles-vs-skills.md | L21 | «Fallback chain: DS → Pack → SPF → FPF → ZP» |
| 26 | docs/principles-vs-skills.md | L52 | «ZP (думать) → FPF (описывать) → Pack (знать) → DS (делать)» |
| 27 | docs/principles-vs-skills.md | L59 | «Каждый уровень порождает следующий. Без верхних уровней нижние не возникают» |
| 28 | docs/LEARNING-PATH.md | L29 | «IWE — персональная система для интеллектуальной работы и развития» |
| 29 | docs/LEARNING-PATH.md | L50 | «Центральный организующий принцип — триада FPF A.7: Роль → Метод → Рабочий продукт» |
| 30 | docs/LEARNING-PATH.md | L94-98 | Role table: R1 Стратег, R2 Экстрактор, R8 Синхронизатор, R13 Проводник |
| 31 | docs/LEARNING-PATH.md | L162-166 | Tiers T0–T4 user path table |
| 32 | docs/LEARNING-PATH.md | §1.1a L36-46 | Three exoskeleton mechanisms: Предъявление / Вопросы / Убывающие подмостки |
| 33 | docs/LEARNING-PATH.md | §2.1 | «L1: Ecosystem → L2: Platform → L3: Template → L4: Personal IWE» |
| 34 | .claude/rules/distinctions.md | L3 | «IWE = Intellectual Work Environment (не «Intelligent», не «Working»). Аналогия: IDE» |
| 35 | .claude/rules/distinctions.md | L5 | «Скилл ≠ Роль ≠ Протокол. Точечное действие / контекст сессии / ритуал ОРЗ» |
| 36 | .claude/rules/distinctions.md | L13 | «Экзоскелет ≠ Автопилот (DP.D.046). Усиление мышления / LLM автономно» |
| 37 | memory/fpf-reference.md | L44-52 | FPF Part C key patterns table (C.11 Decision Theory, C.28 CausalUse-CAL) |
| 38 | memory/fpf-reference.md | L79-83 | FPF principles: A.1 Холонический подход, A.7 Строгие различения, B.5 ADI-цикл |
| 39 | memory/fpf-reference.md | L88-120 | C.28 CausalUse-CAL practical applications in IWE |
| 40 | memory/sota-reference.md | L37 | «SOTA.001 DDD Strategic — Создание Pack, определение BC, словаря, интеграций» |
| 41 | memory/sota-reference.md | L43 | «SOTA.006 Agentic Development: Amdahl Law — multi-agent оправдан ТОЛЬКО при…» |
| 42 | roles/ROLE-CONTRACT.md | L9-15 | Role directory mandatory files: role.yaml, README.md, install.sh |
| 43 | roles/ROLE-CONTRACT.md | L48-66 | role.yaml schema: name, id, type, display_name, runner, install.priority |
| 44 | roles/extractor/README.md | L60-70 | KE pipeline: Обнаружение → Классификация → Маршрутизация → Формализация → Валидация → Одобрение → Запись |
| 45 | roles/verifier/README.md | L31-37 | «Верификатор загружает: Артефакт + Эталон + Чеклист. НЕ загружает: Задание создателя, Историю» |
| 46 | params.yaml | L41 | «capture_autonomy: propose — агент предлагает capture, пользователь подтверждает» |
| 47 | params.yaml | L66-69 | «author_mode: false — разрешает прямое редактирование L1 файлов ТОЛЬКО автору» |
| 48 | README.md | L266 | «Вход — через семинар «IWE для практиков» (5000₽) в боте @aist_me_bot» |
| 49 | CHANGELOG.md | L8-30 | Version 0.31.0 (2026-05-17): S-44 Telegram, S-45 Agent Inbox testing |
| 50 | CHANGELOG.md | L27 | «S-45 Agent Inbox status: testing (CCR-автоматизация ждёт RemoteTrigger v2 API spec)» |

---

*Synthesis complete. Draft ready for brigadier integration into canonical 02-iwe-deep-v2.md.*
*Peer cells: engineering-integrator + philosophy-critic integrate alongside this output.*
