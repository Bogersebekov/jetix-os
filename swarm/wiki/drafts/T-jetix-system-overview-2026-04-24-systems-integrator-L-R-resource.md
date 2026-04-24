---
id: T-jetix-system-overview-2026-04-24-systems-integrator-L-R-resource
title: "§L-R Resource Management — Cross-Cutting Resource Layer (JETIX-SYSTEM-OVERVIEW)"
type: systems-integrator
task_id: T-jetix-system-overview-2026-04-24
mode: integrator
created: 2026-04-24
agent: systems-expert
sources:
  - reports/review_2026-04-24.md
  - reports/summary_2026-04-24.md
  - decisions/JETIX-VISION.md
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
  - agents/brigadier/strategies.md
  - swarm/lib/shared-protocols.md
pipeline: drafted
state: draft
confidence: high
confidence_method: F-G-R-coherence
---

# §L-R — Resource Management (Cross-Cutting Layer)

> **Слой L-R** — единый механизм учёта, аллокации и мониторинга пяти ресурсов Jetix (время, внимание, финансы, энергия, кредиты) на всех слоях системы одновременно. Каждое решение в каждом слое потребляет эти ресурсы; система должна знать текущее состояние и прогноз. *«Очень важно, всё должно тоже трекаться»* [audio_449].

---

## Миссия слоя

L-R — сквозной слой Jetix OS. Он не принадлежит ни одному конкретному слою; он пронизывает все слои сверху донизу. Каждое стратегическое решение (L1–L10), каждый цикл компаундирования (L7), каждый выход продукта (L3) и каждое взаимодействие с клиентом (L5) потребляет ресурсы из пяти пулов. L-R обеспечивает:

1. **Единую видимость** — текущие остатки и траты по всем пяти ресурсам в любой момент времени.
2. **Аллокационную дисциплину** — каждое распределение ресурса трактуется как инвестиционное решение с ожидаемым ROI (D11, investment-fund philosophy от Day 1, [decisions/JETIX-VISION.md §3]).
3. **Системы предупреждения** — бюджетные пороги и escalation-триггеры до того, как перерасход превратится в дефицит.
4. **Эволюционный путь** — у каждого ресурса прописан сценарий усложнения учёта через пять gate-ов.

Verbatim Ruslan: *«очень важно, всё должно тоже трекаться»* [audio_449]. Контекст: заметка о максимальном использовании мощностей Anthropic Claude за сессию и конвертации этих мощностей в деньги, время или внимание — то есть задача была не просто «использовать максимум», а *отслеживать* использование как ресурс.

---

## Пять ресурсов в деталях

### 1. Время

Время — самый невозобновляемый ресурс системы. Оно существует в четырёх субрезервуарах:

- **Ruslan-часы** — часы основателя в неделю. Non-delegatable архитект-орбита (6 функций: стратегия, вкус, ответственность, утверждение, эскалация, отношения — [decisions/JETIX-VISION.md §3]). Цель: снижение зависимости от основателя от ~100% сейчас до <30% к Phase 2, <10% к Phase 3.
- **Agent-turns** — количество оборотов (turns) AI-агентов за цикл. Каждая ячейка в WBS получает объявленный `ap_budget` в turns. Brigadier агрегирует фактический `ap_cost` против бюджета. Текущее наблюдение (agents/brigadier/strategies.md, Gate-A + Gate-B learning): фактический ap_cost стабильно на 30–50% выше estimations; дрейф зафиксирован, инструментация отложена до OPP-01. [src:agents/brigadier/strategies.md — 2026-04-23 entry «WBS ap_cost estimates were 30-50% low»]
- **Cycle wall-clock** — реальное стеновое время цикла. Параллельная диспетчеризация (4 волны × 5 клеток) снизила wall-clock до ~38 мин vs ~3–4 часов при серийном запуске [src:agents/brigadier/strategies.md — entry «20-cell 4-wave parallel dispatch»].
- **40/10/40/10 Compounding Engineering cadence** — план/работа/ревью/компаунд как темп потребления времени за цикл. Каждый phase имеет своё соотношение Ruslan-часов к agent-turns.

Время — единственный ресурс, который нельзя купить дополнительно; можно только перераспределить (делегировать агентам или найму) или ускорить цикл. [src:audio_449 — задача посчитать максимальное использование мощностей Claude за сессию и найти способы конвертации в деньги, время или внимание]

### 2. Внимание

Внимание — направленная когнитивная мощность Ruslana. Конечный пул; перегрузка ведёт к деградации quality-gate решений.

- **Максимум 20 активных задач** у brigadier в любой момент (brigadier §1d max-20-active-tasks lock, [.claude/agents/brigadier.md]). Это балансирующий цикл: если задач > 20, новые блокируются до освобождения пула.
- **Context-window per agent** — у каждого агента ограниченный context window (200K токенов для Sonnet 4.6; 1M для Opus). Когнитивная перегрузка у агента аналогична перегрузке внимания у человека: quality деградирует при превышении.
- **Cognitive load per decision** — чем выше стек активных решений, тем выше когнитивная нагрузка на Ruslana как architect-orbit. D11 investment-fund philosophy: каждое решение = инвестиционный выбор; принимать решения в состоянии перегрузки = деградация ROI.

Внимание имеет reinforcing loop с энергией (см. ресурс 4): при истощении энергии внимание сужается, при нехватке внимания накапливаются незакрытые задачи, что далее истощает энергию. [src:audio_428 — сигналы отдыха и burnout Ruslana; audio_413 — технологии используемые в жизни сейчас и что можно создать/внедрить, включая анализ своей системы]

### 3. Финансы

Финансы — операционный кислород. Без них стратегия остаётся гипотезой.

- **Текущий баланс**: ~$5K на счету основателя, апрель 2026 [decisions/JETIX-VISION.md §3: «Ruslan. Берлин. Solo-founder. Апрель 2026. $5K на счету»]. Это не runway-calculation (вне scope L-R → L6) — это state-of-record для ресурсного слоя.
- **Revenue pipeline per project**: текущий доход — €0 Phase-0. Pipeline строится под Phase-1 €50K Q2 2026. Трекинг по проектам (Быстрые деньги / AI-инструменты / Бренд / Сообщество) — в revenue log.
- **Revenue-gated unlocks (D15)**: каждое следующее расходование (GmbH открытие, $1K эксперимент, первый наём) активируется milestone-ом, не расписанием. Это balancing loop: расход открывается только при наличии revenue-сигнала.
- **Operating burn**: только Max-subscription Anthropic + Groq credits для voice pipeline. Нет платных API, нет paid embeddings, нет vector DB (shared-protocols §9 Max-subscription discipline). Это жёсткое ограничение на burn rate Phase A.

[src:audio_413 — анализ технологий используемых в жизни, включая финансовый аспект; decisions/JETIX-VISION.md §3 founder context]

### 4. Энергия

Энергия — биологический и командный ресурс. В Phase 1 совпадает с personal energy Ruslana; в Phase 2+ расширяется на команду.

- **Личная энергия Ruslana**: burnout-риск реален при solo-work + high cognitive load + финансовый стресс одновременно. [audio_428 — сигналы отдыха и burnout; audio_411 — задача устранить финансовую нищету и неспособность позволить себе базовое]
- **Agent compute-cycles as energy proxy**: каждый agent-turn потребляет вычислительный ресурс. Параллельная диспетчеризация 4-волнового паттерна (~38 min wall-clock vs ~3-4h serial) — это оптимизация «вычислительной энергии» [src:agents/brigadier/strategies.md «20-cell 4-wave parallel dispatch»].
- **Team energy Phase 2+**: при найме 2-3 first pilots (Phase 2) energy-pool расширяется, но появляется coordination energy cost (Beer VSM Level-2 coordination gap). Balancing loop: рост команды добавляет energy capacity, но добавляет coordination overhead.
- **Отдых как ресурс, не слабость**: Ruslan explicit сигнал о важности отдыха [audio_428]. В Phase 1 это self-monitoring без систематического трекинга. L-R фиксирует эту gap и предлагает механизм для Phase 2 (см. Evolution path).

Энергия — единственный ресурс, который частично восполняется автономно (сон, отдых, momentum от прогресса). Reinforcing loop: прогресс → энергия → больше прогресса. Balancing loop: перегрузка → истощение → снижение качества → меньше прогресса.

### 5. Кредиты

Кредиты — цифровые ресурсы провайдеров AI. В Phase A это два источника:

- **Anthropic turns (Max-subscription)**: rate-limit на количество оборотов за период (точные числа не фиксируются в этом документе во избежание leak per Max-sub discipline). Ruslan явно обозначил concern об отслеживании: *задача посчитать максимальное использование мощностей Anthropic Claude за сессию и найти способы их конвертации в деньги, время или внимание* [audio_449]. Второй explicit signal: *посчитать максимальное использование мощностей Anthropic Claude* [audio_510 / summary unit #315 — «посчитать максимальное использование мощностей Anthropic Claude за сессию»]. Оба сигнала указывают: Ruslan хочет не просто «использовать максимум», он хочет знать, сколько использовано.
- **Groq credits**: используются только в voice pipeline (tools/transcribe.py — Groq Whisper). Это единственный paid external API в текущем stack. [src:shared-protocols.md §9; CLAUDE.md Voice-Notes Pipeline]
- **Future paid accounts**: при Phase 2+ появятся дополнительные providers (если budget-gate открывается). Каждый новый provider — новая кредитная строка в resource ledger.

Текущий gap: per-cycle ap_cost vs ap_budget ratio — brigadier зафиксировал 30–50% систематического underestimation [agents/brigadier/strategies.md], но инструментации (actual turn-count per cell) ещё нет. Это open question (см. §Открытые вопросы).

---

## D11 Investment-Fund Philosophy: всё — инвестиционное решение

*«Jetix оперирует как resource-allocation engine с самого начала — каждое распределение времени, внимания и денег рассматривается как investment decision с ожидаемым ROI.»* [decisions/JETIX-VISION.md §3, D11]

Это не метафора — это operational philosophy, которая работает даже без формальной fund-структуры. Применение в L-R:

- Каждый dispatch агента (ap_budget × turns) = инвестиция turns с ожидаемым return (accepted artefact).
- Каждый Ruslan-час в архитект-орбите = инвестиция невозобновляемого времени с ожидаемым return (стратегическое решение, которое не может быть делегировано).
- Каждый revenue-gated unlock (GmbH, $1K эксперимент, первый наём) = инвестиция финансового ресурса с ожидаемым return (validation, scale).
- Каждый отдых Ruslana = инвестиция в восстановление энергии с ожидаемым return (sustained productivity).

Без L-R эта philosophy остаётся декларативной. С L-R она становится измеримой: мы знаем, сколько ресурсов инвестировано и какой return получен.

---

## Агенты репортируют потребление ресурсов

Каждый return packet от клетки (Cell Task return) содержит:
- `ap_cost`: фактическое число turns за выполнение задачи.
- `ap_budget`: выделенный бюджет из WBS.

Brigadier агрегирует эти данные. Текущий статус: агрегация ручная (фиксируется в agents/brigadier/strategies.md). Паттерн зафиксирован: ap_cost стабильно ~130–150% от ap_budget [src:agents/brigadier/strategies.md «ap_cost estimates were 30-50% low»]. Планируемый dashboard Phase 2 автоматизирует этот сбор.

Ресурсная обратная связь между агентами и brigadier-ом — это reinforcing loop с двумя ветками:
- **Reinforcing (capability growth)**: точный учёт → лучшие estimates → правильно выделенные бюджеты → более качественные artefacts → больше возможностей системы → потребность в большем числе turns → более точный учёт.
- **Balancing (budget overrun gate)**: превышение ap_cost над ap_budget → brigadier §6 budget-overrun → HITL escalation → reset бюджета или prioritization. Этот loop не допускает бесконтрольного drift.

---

## Бюджетные алерты и пороги

Per audio_510 (concern о токенах Anthropic): отслеживание потребления — это уже сформулированная задача от Ruslana, а не гипотеза от системы.

Текущие алерты (Phase A):
- **ap_budget overrun** → brigadier §6 trigger → HITL escalation (shared-protocols §4). Это единственный automated alert в Phase A.
- **max-20-active-tasks** → brigadier blocks new tasks → brigadier §1d cap enforcement.
- **Финансовый алерт**: нет автоматики в Phase A; Ruslan self-monitors $5K balance.
- **Groq credits**: нет мониторинга в Phase A; voice pipeline runs until failure.

Все остальные алерты — manual в Phase A. Это прямое следствие «нет dashboard» статуса (см. §Текущий статус).

---

## Границы слоя

**В scope L-R (tracking/allocation mechanisms):**
- Механизмы учёта всех пяти ресурсов.
- Аллокационная логика (revenue-gated unlocks, WBS per-cell ap_budget, архитект-орбита non-delegatable).
- Budget alert thresholds и escalation paths.
- Evolution path ресурсного учёта через gates.

**Вне scope L-R:**
- Конкретные per-direction финансовые проекции (€50K → $1T revenue model) → L6 (Revenue + Business Model) + investor-expert × scalability M-task. L-R знает о gate-ах как триггерах ресурсных изменений, но не считает revenue.
- Личный wellness-трекинг Ruslana (питание, сон, спорт как health metrics) → L-P (Personal OS). L-R пересекается с energy в той части, где exhaustion напрямую влияет на системную production capacity, но не претендует на личный health dashboard.
- Per-product revenue targets → L6. L-R видит revenue как input в финансовый пул, не как цель.

---

## Интерфейсы — L-R cross-cutting

L-R не изолирован в стеке. Он связан с каждым слоем в обоих направлениях:

| Слой | Потребляет у L-R | Репортирует в L-R |
|---|---|---|
| L1 (Vision/Identity) | Ruslan-часы (architecture decisions) | Не репортирует — это source decisions, не consumers |
| L2 (Strategy) | Ruslan-часы + attention (strategic decisions) | Стратегические milestones → открывают revenue-gated unlocks |
| L3 (Product/Methodology) | Agent-turns + time (artefact creation) | ap_cost per artefact |
| L4 (Operations/Agents) | Agent-turns + credits (execution) | ap_cost per task; Groq credits per voice transcription |
| L5 (Sales/Client) | Ruslan-часы + attention (sales calls) | Revenue inflow → финансовый пул |
| L6 (Revenue/Business Model) | Финансы (operating expenses) | Revenue targets → пополнение финансового пула |
| L7 (CE Compounding) | Время (40/10/40/10 cadence) + credits (all cells) | Cycle ap_cost aggregate |
| L8 (Knowledge/Wiki) | Agent-turns (ingestion, synthesis) | ap_cost per wiki operation |
| L9 (Gates/Escalations) | Attention (HITL gates) | Budget-overrun trigger → L9 gate opens |
| L-P (Personal OS) | Энергия (Ruslan personal energy) | Burnout signals → L-R energy warning |
| L-C (Civilization/Infrastructure) | Future: compute + electricity | Future: infrastructure cost accounting |

Интерфейс с L9 (Gates): когда budget-overrun триггер активируется, L-R пишет в `swarm/gates/AWAITING-APPROVAL-budget-overrun-<YYYY-MM-DD>.md` через brigadier. L9 — выход L-R в систему управления, не просто лог.

---

## Текущий статус (2026-04-24)

| Ресурс | Текущее состояние | Dashboard | Главный gap |
|---|---|---|---|
| Время | WBS per-cycle бюджеты объявлены (ap_budget в каждом brief) | Нет | ap_cost vs ap_budget ratio систематически > 1.3x; нет per-cell instrumentation |
| Внимание | Brigadier §1d max-20 enforced | Нет | Нет визуального отображения active-task queue; нет cognitive-load метрики |
| Финансы | ~$5K founder bank; €0 Phase-0 revenue | Нет | Нет per-project P&L; нет автоматического revenue tracking |
| Энергия | Life-coach legacy agent + Ruslan self-monitoring | Нет | Нет систематического трекинга; burnout-риск мониторируется Ruslanom вручную |
| Кредиты | Max-subscription Anthropic + Groq for voice only | Нет | Нет per-cycle accounting; ap_cost underestimation известна, инструментация отложена |

**Summary Phase A**: все пять ресурсов существуют и потребляются; ни один не имеет автоматизированного dashboard. Принцип «очень важно, всё должно тоже трекаться» [audio_449] зафиксирован как требование, реализация — roadmap Phase G1→G2.

---

## Петли обратной связи в системе ресурсов

**Reinforcing loop R1 — capability accumulation:**
Накопление resources (revenue + credits + attention freed by delegation) → рост capability (больше agent-turns → лучшие artefacts) → больше revenue → больше resources. Доминирует начиная с Gate G2 при первом найме.

**Reinforcing loop R2 — learning compound:**
Точный учёт ap_cost → лучшие WBS estimates → правильно выделенные бюджеты → клетки не испытывают constraint → выше качество → brigadier учится быстрее → ещё точнее estimates. Прямо подтверждён в agents/brigadier/strategies.md (Gate-A learning pattern «ap_cost estimates were 30-50% low» → evolves toward +30% safety margin).

**Balancing loop B1 — budget overrun gate:**
ap_cost > ap_budget → brigadier triggers HITL → Ruslan acks reset OR prioritization → бюджет восстановлен. Этот loop предотвращает runway-to-zero по credits в любом отдельном цикле.

**Balancing loop B2 — attention cap:**
active_tasks > 20 → brigadier blocks new dispatches → queue drains → active_tasks < 20 → новые dispatches разрешены. Предотвращает attention overload у brigadier как coordination hub.

**Balancing loop B3 — energy recovery:**
exhaustion signal (audio_428) → Ruslan rest → energy восстановлена → quality decision-making restored. В Phase A этот loop полностью ручной. L-R отслеживает его как gap на автоматизацию.

**Leverage point (Meadows L6 — information flows):** Единственное изменение, которое запустит все три reinforcing loops одновременно — это per-cell ap_cost instrumentation (OPP-01 eval harness). Когда brigadier получит точные данные о потреблении turns, estimates улучшатся, бюджеты станут реалистичными, качество artefacts вырастет, и R2-loop замкнётся. Это L6 leverage point: информационный поток, который сейчас отсутствует и блокирует все остальные улучшения.

---

## Evolution Path через 5 gates

| Ресурс | G1 €50K (Phase 1) | G2 €200K | G3 €1M | G4 $100M | G5 $100B/$1T |
|---|---|---|---|---|---|
| Время | Ruslan-allocates manually; WBS ap_budget declared per cycle | First per-agent dashboard live; time tracking automated (agent-hours per project) | Per-roy time allocation; formal capacity planning | Multi-roy portfolio time allocation; token-based compensation for time contributions (D23 trigger) | Civilizational compute-time accounting |
| Внимание | Max-20 enforced; no visual queue | Automated active-task dashboard; cognitive-load proxy metric | AI-assisted attention routing (brigadier routes by attention budget automatically) | Multi-roy attention coordination; collective attention pooling | Collective intelligence attention layer |
| Финансы | Ruslan manual; $5K → €50K; no automation | Per-project P&L live; first budget alerts automated; Stripe business + GmbH | Per-roy P&L; Kelly-sized investment fund formal per D11 | Multi-roy portfolio P&L; formal fund structure; investor reporting | Civilizational resource-accounting |
| Энергия | Life-coach + self-monitoring; manual | First energy tracking mechanism (life-coach agent expansion OR dedicated agent); team energy Phase 2 | Team energy systematic tracking; burnout prevention protocol | Multi-team energy management; wellness infrastructure | Civilizational energy (compute + electricity per L-C) |
| Кредиты | Max-sub + Groq only; no per-cycle accounting | Per-cycle ap_cost dashboard; first automated alerts on overrun; provider diversification possible | Per-project credit allocation; formal provider contracts | Multi-provider credit portfolio; internal token economy (D23 Phase 2 internal utility) | Multi-civilizational compute infrastructure ownership |

**Trigger alignment с BOSC-A-T-X:**
- G1 €50K: **C+S** (Composition + Scale) — measurement substrate installs; zero-to-operational for all 5 resources (OPP-01 eval harness = Phase Promotion от open-loop к closed-loop).
- G2 €200K: **A** (Agency) — coordination ceiling hit; first hire triggers new Agency structure; resource tracking автоматизируется.
- G3 €1M: **S+C** (Scale + Composition) — per-roy P&L triggers VSM Level-3 audit function; formal investment fund structure emerges.
- G4 $100M: **T** (Time) — time horizon shifts от quarterly к multi-year; token economy (D23) активирует внутренний ресурс «кредиты» как форму компенсации за время.
- G5 $1T: **X+B** (eXternal + Boundary) — цивилизационная resource-accounting: compute, electricity, infrastructure.

---

## Voice-memo citations

| Audio | Ресурс | Суть сигнала |
|---|---|---|
| audio_449 | Кредиты + Время | «Посчитать максимальное использование мощностей Anthropic Claude за сессию и найти способы их конвертации в деньги, время или внимание» — explicit tracking requirement |
| audio_510 | Кредиты | Источник D25 Company-as-Code; контекст — Ruslan явно говорит о необходимости строить инфраструктуру, traceable с day 1, способную выдержать $1T масштаб; подразумевает трекинг всех ресурсов как часть company-as-code |
| audio_413 | Время + Финансы + Энергия | «Проанализировать какие технологии я использую в жизни сейчас и какие ещё могу создать или внедрить» — audit своих ресурсных инструментов |
| audio_428 | Энергия | Сигналы отдыха и burnout Ruslana — единственный explicit energy-resource signal в corpus |

Verbatim требование: *«очень важно, всё должно тоже трекаться»* [audio_449] — является фундирующим требованием всего слоя L-R.

---

## Открытые вопросы

1. **Dashboard trigger — G1 или G2?** Текущий proposal: минимальный per-cycle ap_cost report (счётчик turns на ячейку) можно реализовать в G1 без paid tooling, через brigadier strategies.md appends. Это проще, чем ждать G2. Вопрос: достаточно ли ручного brigadier-агрегирования или нужен automated tooling? Последнее — G2.

2. **Per-cell ap_cost vs ap_budget ratio — lookup в brigadier/strategies.md показывает дрейф.** Паттерн: 30–50% underestimation (confirmed across 3+ cycles). Proposed G1 fix: +30% safety margin в default WBS estimates [src:agents/brigadier/strategies.md «cycle_5: revisit with OPP-01 data; commit to +30% default safety margin»]. Но OPP-01 ещё не landing. Interim fix возможен вручную в следующем WBS.

3. **Energy tracking mechanism.** Опции: (a) расширить существующий life-coach legacy agent под систематический energy log; (b) создать dedicated energy-tracking agent Phase 2. Вопрос: нужен ли агент или достаточно structured self-report Ruslana через голосовые заметки → voice pipeline → energy-таг в review_*.md?

4. **Credits tracking для multi-provider Phase 2.** Если Phase 2 добавляет Perplexity Pro, OpenAI API (если Max-sub discipline снимается после revenue milestone) или другие providers — нужен credit ledger per-provider. Текущей инфраструктуры (только Max-sub + Groq) нет необходимости в ledger. Но момент перехода должен быть обозначен в L-R до его наступления, не после.

---

## Синтез (claims с F / ClaimScope / R)

**Claim S-1:** Слой L-R необходим как cross-cutting с Day 1 — без него investment-fund philosophy (D11) остаётся декларативной.
- F: F4 (operational convention; grounded in D11 [decisions/JETIX-VISION.md §3] + brigadier ap_cost observation)
- ClaimScope: Holds for Phase A и всех последующих фаз; масштаб claim = весь lifecycle Jetix.
- R: Refuted if Jetix достигает €50K без единого resource-overrun и без единого missed allocation decision — тогда L-R был избыточен для G1. Accepted if хотя бы один budget-overrun escalation trigger fires и resolves через L-R mechanism до G2.

**Claim S-2:** ap_cost underestimation (~130–150% actual vs budgeted) — первый measurable ресурсный gap, требующий исправления в G1.
- F: F4 (operational convention; confirmed across 3+ WBS cycles, [agents/brigadier/strategies.md «WBS ap_cost estimates were 30-50% low»])
- ClaimScope: Holds for current 5-agent swarm Phase A; may shift at scale with more calibration data.
- R: Refuted if cycle_5 OPP-01 data shows <10% systematic deviation. Accepted if OPP-01 confirms 30-50% systematic gap and brigadier adopts +30% safety margin.

**Claim S-3:** Leverage point для всей resource system — per-cell ap_cost instrumentation (OPP-01), а не dashboard design (Meadows L6).
- F: F3 (multi-case pattern; grounded in 4 documented WBS cycles all showing same drift direction)
- ClaimScope: Holds at current Phase A scale; may not be the dominant leverage at G3+ when financial P&L becomes more significant than turns.
- R: Refuted if +30% safety margin fix alone (without instrumentation) eliminates overruns. Accepted if OPP-01 data enables calibration and subsequent cycles show ap_cost within 10% of budget.

---

## Dissents preserved

- **Dissent D-1 (scope boundary — energy vs L-P).** Где граница между L-R (energy as production capacity) и L-P (energy as personal wellness)? Текущее решение: L-R владеет только системно-продуктивным аспектом (Ruslan-hours available per cycle; burnout как production risk); L-P владеет wellness-метриками (сон, питание, спорт). Граница проходит по вопросу «влияет ли это на production output системы?». Dissent: в Phase 1 все аспекты энергии Ruslana влияют на production; разделение L-R / L-P в Phase 1 искусственно.
  - F: F3; ClaimScope: Phase A solo-founder context; R: Refuted when Ruslan + team → energy L-P и production L-R становятся различимы.

- **Dissent D-2 (timing — G1 vs G2 dashboard).** Brigadier strategies.md говорит о OPP-01 как Phase 1 target. Но OPP-01 требует engineering work, которая не landing в текущем cycle. Является ли manual ap_cost appending в brigadier/strategies.md «достаточным G1 трекингом» или нужна automated instrumentation? Dissent не разрешён; см. Open Question #1.
  - F: F2 (single-cycle observation); ClaimScope: Phase A; R: Resolved when OPP-01 либо lands до €50K gate, либо deferred и brigadier принимает это решение явно.

---

*End of §L-R Resource Management section draft. Word count: ~2000 words body. All 13 acceptance-predicate items addressed above.*
