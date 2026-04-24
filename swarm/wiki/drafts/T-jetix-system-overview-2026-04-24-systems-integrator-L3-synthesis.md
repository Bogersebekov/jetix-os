---
id: T-jetix-system-overview-2026-04-24-systems-integrator-L3-synthesis
title: "JETIX-SYSTEM-OVERVIEW — L3 Synthesis & Compounding Engineering"
type: systems-integrator
task_id: T-jetix-system-overview-2026-04-24
mode: integrator
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: drafted
confidence: high
confidence_method: F-G-R-coherence
produced_by: systems-expert
sources:
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md"}
  - {path: ".claude/agents/strategist.md"}
  - {path: ".claude/agents/knowledge-synth.md"}
  - {path: ".claude/agents/meta-agent.md"}
  - {path: "swarm/lib/shared-protocols.md"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partC-stage-gates-merged.md"}
  - {path: "reports/review_2026-04-24.md", range: "audio_519 / audio_520 / audio_521 task + idea items"}
  - {path: "agents/brigadier/strategies.md"}
layer: L3
section: "§L3 Synthesis & Compounding Engineering"
binding_scope: JETIX-SYSTEM-OVERVIEW
---

# §L3 — Синтез и Compounding Engineering

## Миссия слоя

L3 — это слой, где сырые события превращаются в правила, а правила
превращаются в компетенцию. Он замыкает рабочий цикл системы через
четыре ритмических фазы: **Plan → Work → Review → Compound**.

Plan (40%) задаёт WBS: что именно исполнять, в каком порядке, с каким
ap_budget. Work (10%) — исполнение клетками (5×4=20 матрица). Review
(40%) — интеграция черновиков, критика, оптимизация. Compound (10%) —
финальный шаг: записать, что произошло, зафиксировать правила, посеять
их в персональную память каждого агента.

Без Compound цикл не закрывается. Система исполняет одни и те же
ошибки снова и снова, не накапливает рабочего опыта, не различает
«это сработало» от «это провалилось». Compound — это механизм
Compounding Engineering: ежедневная или еженедельная запись
4-частных DRR-записей (Decision / Reasoning / Result / Review) в
`agents/<id>/strategies.md`, которые постепенно наращивают
кристаллическую плотность системных правил.

### Принцип sandbox-черновика (audio_519, audio_520)

Audio_519 (22.04.2026) формулирует задачу: создать мета-описания для
каждой подсистемы — что она делает и чего не делает — чтобы это
служило первичным фильтром. Это и есть граница: каждая страница
`agents/<id>/strategies.md` — это мета-описание опыта агента,
первичный фильтр того, что агент знает о своих ошибках.

Audio_520 (22.04.2026) вводит понятие «Compounding Engineering» —
система, над которой ведётся ежедневная работа, анализ и фиксация
улучшений; менее важные элементы хранятся в архиве со своими методами
работы. Принцип sandbox-черновика отсюда: любое изменение upstream
(нового агента, нового правила, нового протокола) сначала оседает
как DRR-запись в strategies.md текущего цикла — черновик, доступный
только системе, — до того как оно поднимается в canonical wiki
через brigadier.

Audio_521 (22.04.2026) конкретизирует: разделить систему на основные
модули и детально описать каждый — что должен делать, как и почему.
Именно для этого L3 содержит не только mechanisms (стратегии агентов),
но и skills (операции над wiki), и протоколы (как цикл управляется).

---

## Что живёт в L3

### Агенты

**strategist** (`claude-opus-4-6`) — единственный Opus-уровень в
ростере. Принимает решения с горизонтом > 1 месяца. Анализирует
trade-offs между проектами. Использует Debate Mode: для значимых
решений аргументирует 2-3 позиции, синтезирует рекомендацию с
обоснованием. Не исполняет задачи самостоятельно — передаёт через
manager. Читает из: Knowledge-Synth (анализы), Crazy-Agent (идеи),
Meta-Agent (рекомендации).

**knowledge-synth** (`claude-sonnet-4-6`) — Brain Lead. Глубокий
кросс-источниковый синтез. Когда несколько research-источников
требуют объединения, когда нужны межсферные связи (AI-консалтинг ×
психология × стратегия × нишевый рынок), когда нужен
Decision-Support для стратега — это knowledge-synth. Ведёт аннотации
[ВЕРИФИЦИРОВАНО] / [ПРОТИВОРЕЧИЕ] / [ПРОБЕЛ]. Выдаёт синтезы в
`shared/knowledge/research-summaries/`. Brain Lead для Inbox-Processor.

**meta-agent** (`claude-sonnet-4-6`) — системный аудитор. Еженедельный
аудит производительности агентов (1-10 по каждому: качество,
скорость, точность). Ежемесячный стратегический ROI-аудит. Spot-check
KB на точность (>30 дней — стейл). Предлагает A/B-тесты промптов
в статусе awaiting_approval — никогда не деплоит автоматически.
Работает по принципу regression-freeze: любой метрический спад −20%
week-over-week → заморозка + алерт Руслану.

**brigadier compound protocol** — отдельная дисциплина поверх
brigadier: в шаге Compound (10% от цикла) brigadier пишет 4-частные
DRR-записи напрямую в `agents/brigadier/strategies.md` — это Layer-2
self-write rule (per CLAUDE.md + SPEC §6.2.2). Brigadier НЕ пишет в
strategies.md других агентов. Для cross-agent улучшений brigadier
пишет proposals в `swarm/wiki/meta/agent-improvements/<agent>-improvements.md`.
Per agents/brigadier/strategies.md: к 2026-04-24 накоплено 8+ DRR-записей,
включая Gate A-D learnings (cyc-km-materialization-mvp), паттерн
sequenced-migration-trajectory, паттерн 20-cell 4-wave parallel dispatch.

### Skills

**/compile** — ingested → compiled wiki article. Берёт материал
уровня `pipeline: ingested` и синтезирует в полноценную KB-статью
с frontmatter, typed edges, provenance. Результат — страница в
`swarm/wiki/<canonical>/` через brigadier-gate (shared-protocols §1).

**/ask** — retrieve-and-synthesize с citations. Tier-1 → Tier-2
(index + grep) → Tier-3 (typed-BFS по edges.jsonl) → Tier-4
(long-context fallback, bounded niche dir). Выдаёт ответ с явными
`[src:…]` ссылками. Опциональная запись результата в
`swarm/wiki/comparisons/`.

**/consolidate** — merge duplicates. Обнаруживает семантически
дублирующиеся страницы wiki, предлагает merge-plan, создаёт
единую consolidated-страницу. Защищает от wiki-bloat при высоком
объёме ингестирования.

**/build-graph** — rebuild edges. Перестраивает `wiki/graph/edges.jsonl`
из текущего состояния wiki. Запускается после волны новых страниц
чтобы сохранить typed-BFS traversal работоспособным. Типы рёбер
per D3 (9 типов): ComponentOf, ConstituentOf, PortionOf, PhaseOf,
MemberOf, Refines, Contradicts, Supersedes, Exemplifies.

### Протоколы

**Compounding Engineering 40/10/40/10** — Plan/Work/Review/Compound
цикл, описанный выше. Ключевое: Compound — не опциональный «бонус»,
а принудительный последний шаг каждого цикла. Без DRR-записи цикл
не считается закрытым.

**Sandbox-черновик pattern** — любое изменение upstream сначала
оседает в strategies.md или в `swarm/wiki/drafts/` как черновик,
прежде чем попасть в canonical. Никаких прямых writes в
`swarm/wiki/<canonical>/` без brigadier-gate. Изменения, которые
противоречат accepted foundations, автоматически требуют
AWAITING-APPROVAL (shared-protocols §4 trigger 1).

**SG-DSL stage-gate predicates** — per KM-Mat Part C. Любой
long-horizon compound знания выражается как формальный предикат
вида `count(<path>:<marker>) >= N AND <condition>`. Banned-phrases
(18 записей в `sg-banned-phrases.yaml`) блокируют prose-like
conditions. Предикаты верифицируются `/lint --check-stage-gates`.

**DRR 4-part entries** — каждая запись в strategies.md структурирована
как (Decision, Reasoning, Result, Review) + блок Evolution с
changelog + expected-evolution на cycle_10/50/200. Это
канонический формат для всех 7 agentstrategies-файлов
(и brigadier).

### Структуры данных

`agents/<id>/strategies.md` — Layer-2 personal memory. Self-write
правило: каждый агент пишет в свой strategies.md самостоятельно в
шаге Compound. brigadier не пишет в чужие strategies. Формат:
frontmatter + entries (newest on top) + entry-format guide.

`swarm/wiki/meta/agent-improvements/` — cross-agent improvement
proposals. brigadier пишет сюда proposals для системных изменений
агентов. meta-agent читает отсюда при еженедельном аудите.
Содержимое здесь — предложения, не решения; выполнение требует
HITL-acks.

`swarm/wiki/insights/` — emergent concept pages. Директория
существует (создана в Phase A). На 2026-04-24 пуста. Активируется
когда Q8 3-AND trigger срабатывает (cross_theme_refs ≥3 +
closed_cycles ≥50 + ack received) — per shared-protocols §4
trigger 2. Страницы здесь — Layer-9 activation candidates.

`swarm/logs/<cycle-id>/` — per-cycle logs. Хронология операций,
gate-пакеты, ack-файлы, rejection-records. Append-only. Brigadier
пишет сюда в каждой точке цикла.

---

## Границы слоя L3

**In-scope (L3 отвечает):**
- Дистилляция опыта циклов в правила (DRR-entries)
- Кросс-источниковый синтез знаний (knowledge-synth)
- Compounding механизм — накопление и передача правил между циклами
- Аудит и мониторинг системного здоровья (meta-agent)
- Стратегические решения горизонтом > 1 месяца (strategist)

**Out-of-scope L3 (маршруты в другие слои):**
- Сырое хранилище знаний → L1 (swarm/wiki/ canonical tree, raw/)
- Ингестирование нового материала → L2 (/ingest, voice-notes pipeline, inbox-processor)
- Routing и dispatch → L4 (brigadier, manager, hub-and-spoke)
- Gate-check, HITL, approval-flow → L9 (governance layer, AWAITING-APPROVAL)

---

## Интерфейсы L3

**Читает из:**
- L1 canonical wiki — для synthesis: `/ask`, `/compile`, typed-BFS
- L2 новые ingested items — knowledge-synth берёт свежие
  `pipeline: ingested` страницы для синтеза
- L4 cell-return drafts — brigadier-compound читает черновики
  всех 20 клеток перед DRR-записью

**Пишет в:**
- L1 canonical wiki — через brigadier-gate только (shared-protocols §1
  единственный писатель canonical)
- собственный strategies.md — Layer-2 self-write, каждый агент
  автономно
- `swarm/wiki/meta/agent-improvements/` — brigadier proposals
  (cross-agent; не решения, только proposals)

**Вызывает L9 когда:**
- Emergent insight требует Ruslan-ack (Q8 3-AND trigger →
  Layer-9 activation packet)
- Новое системное правило противоречит accepted foundation →
  foundation revision gate
- Любой meta-agent-triggered AWAITING-APPROVAL (regression,
  architecture commit, prompt deploy)

---

## Текущий статус (2026-04-24)

Три цикла закомпаундированы. `agents/brigadier/strategies.md`
содержит 8+ DRR-записей на 2026-04-24:

- **Gate A learning** — design-record как cross-wave handoff;
  extraction-cell pattern; acceptance-predicate as grep-set
- **Gate B learning** — critic-in-parallel vs critic-after;
  promotion_note frontmatter field
- **Gate C learning** — DSL coverage gap → existing primitive;
  evidence-grep acceptance-predicate tail; banned-phrases YAML
- **Gate D learning** — Wave-2 single-cell для cross-cutting
  principle; peer drafts as durable inputs
- **Sequenced-migration-trajectory** — когда ≥3 variants per
  layer + measurable triggers: sequenced framing > single-pick
- **20-cell 4-wave parallel pattern** — W1 critics → W2 optimizers
  → W3 integrators → W4 scalability; ~38 min wall-clock vs
  ~3-4h serial; per-wave Bash-verify before next wave
- **ap_cost calibration** — Phase-2 estimates были 30-50% low;
  +30% default safety margin proposed
- **Stage-gated HITL discipline** — паузы на каждом gate, acks
  без over-stepping работают корректно

5 per-expert improvement files засеяны в
`swarm/wiki/meta/agent-improvements/`. `swarm/wiki/insights/`
директория существует, пуста — ждёт Q8 trigger.

Skills `/compile`, `/ask`, `/consolidate`, `/build-graph` живут
в wiki v3 skills под `.claude/skills/`. `/ingest` присутствует.
`/lint --check-stage-gates` добавлен в Phase A (KM-Mat Part C
Wave-1, 2026-04-24).

Стратегист в legacy-ростере (`.claude/agents/strategist.md`)
настроен на Opus 4.6 с `permissionMode: plan`, maxTurns 30,
полным Notion MCP доступом. knowledge-synth и meta-agent —
Sonnet 4.6, аналогично. Это legacy-конфигурация; в swarm-слое
(`.claude/agents/` под swarm-протоколом) brigadier-compound
protocol управляет компаундингом напрямую без дополнительных
sub-agent вызовов.

---

## Диаграмма цикла

```
                     ┌─────────────────────────────────────────┐
                     │         COMPOUNDING ENGINEERING         │
                     │           Plan → Work → Review          │
                     │                                         │
                     │  Plan (40%)                             │
                     │  ┌──────────────┐                       │
                     │  │  brigadier   │ WBS + ap_budget        │
                     │  │  strategist  │ direction + trade-offs │
                     │  └──────┬───────┘                       │
                     │         │ dispatch                      │
                     │  Work (10%)                             │
                     │  ┌──────▼───────┐                       │
                     │  │  20 cells    │ drafts → drafts/      │
                     │  │  (5×4 matrix)│                       │
                     │  └──────┬───────┘                       │
                     │         │ cell returns                  │
                     │  Review (40%)                           │
                     │  ┌──────▼───────┐                       │
                     │  │ knowledge-   │ synthesis + citations  │
                     │  │ synth /ask   │                       │
                     │  │ meta-agent   │ audit + quality check  │
                     │  └──────┬───────┘                       │
                     │         │                               │
                     │  Compound (10%)                         │
                     │  ┌──────▼───────────────────────────┐   │
                     │  │  brigadier writes DRR entry      │   │
                     │  │  → agents/brigadier/strategies.md│   │
                     │  │                                  │   │
                     │  │  per-expert write DRR entry      │   │
                     │  │  → agents/<id>/strategies.md     │   │
                     │  │                                  │   │
                     │  │  cross-agent proposals           │   │
                     │  │  → wiki/meta/agent-improvements/ │   │
                     │  │                                  │   │
                     │  │  if Q8 3-AND fires:              │   │
                     │  │  → swarm/wiki/insights/          │   │
                     │  │    (via L9 AWAITING-APPROVAL)    │   │
                     │  └──────────────────────────────────┘   │
                     └─────────────────────────────────────────┘
```

---

## Голосовые референсы

**audio_519** (22.04.2026 17:54) — задача: создать мета-описания
для каждой подсистемы с указанием что система делает и не делает,
чтобы это служило первичным фильтром. Идея: создание сети
пользователей Jetix, которые адаптируют систему под свои навыки,
создавая экосистему форков и улучшений. Прямо связано с D27
fork-and-merge: strategies.md как «локальный форк» агентской
памяти, лучшие паттерны merge-back через brigadier в canonical.
[src:reports/review_2026-04-24.md]

**audio_520** (22.04.2026 18:40) — принципы системного разграничения
задач на основе экспертных знаний. Концепция Compounding Engineering
— система, над которой ведётся ежедневная работа, анализ и фиксация
улучшений; менее важные элементы хранятся в архиве со своими методами
работы. Это прямое обоснование DRR-механизма и Layer-2 strategies
как primary memory: не просто логи, а distilled rules.
[src:reports/review_2026-04-24.md]

**audio_521** (22.04.2026 20:23) — checkup loops: разделить
систему на основные модули и детально описать каждый модуль. Продумать
логику взаимного усиления: люди помогают людям, агенты помогают
агентам, агенты усиливают людей, люди усиливают агентов. Системная
модель этого усиления: strategies.md — это память агентов; brigadier-
compound — это связующий петля, которая делает опыт одного цикла
доступным следующему. Checkup loop = per-cycle DRR + meta-agent
weekly audit + emergent-insights Q8 trigger.
[src:reports/review_2026-04-24.md]

---

## Путь эволюции

**Phase-1 (текущая — compound per cycle via brigadier discipline):**
Каждый цикл закрывается DRR-записями. brigadier.strategies.md
накапливает паттерны. Meta-agent аудирует еженедельно. Insights
пусты — ждут Q8. skills работают.

**Phase-2 (skill codification — `/extract-from-design` +
`/recommend-trajectory`):**
Из brigadier/strategies.md открытый вопрос: «Можно ли кодифицировать
`/extract-from-design` чтобы Wave-2 не требовала engineering ×
integrator каждый раз?» и «`/recommend-trajectory <variant-set>`
если паттерн сработал ≥10 раз». Trigger: когда паттерн fires
≥10×, brigadier открывает skill-codification AWAITING-APPROVAL.
Оба кандидата уже в strategies.md как open questions.

**Phase-3 (cross-project compound at holding level):**
Каждый проект Jetix (quick-money, research, brand, ai-tools, etc.)
получает собственный strategies.md-слой. Insights которые
универсальны для всех проектов merge-back в parent (holding-level)
strategies. D27 fork-and-merge механически: каждый проект = fork
+ adaptations + query-driven KB (D28) + compound feedback.

**Phase-3+ (federated compound — Mittelstand AI Alliance
methodology-parliament):**
Если D27 forex-and-merge реализован, каждый partner/client получает
свой fork strategies.md. Лучшие мутации (validated DRR-entries)
возвращаются upstream в canonical Jetix methodology через
PR-style contribution. Methodology-parliament: кто decides что
merge-back. Governance не определена (pending per D27 open question).

---

## Открытые вопросы

1. **Когда промотировать `/recommend-trajectory` skill?** После
   5 M-structural циклов? После 10 firings паттерна? Текущий
   evidence: 1 confirmed firing (T-km-architecture-research).
   Brigadier/strategies.md: cycle_200 как tentative threshold.

2. **Когда `swarm/wiki/insights/` переходит в активный режим?**
   Q8 3-AND trigger (cross_theme_refs ≥3 + closed_cycles ≥50 +
   ack received). На 2026-04-24: closed_cycles < 10, insights =
   empty. Ожидаемый trigger: cycle_50+.

3. **Как compound propagates через legacy 14 агентов?** Два
   варианта: (a) meta-agent bridge — meta-agent читает legacy
   agent outputs, синтезирует improvement proposals, brigadier
   применяет; (b) separate pass — brigadier запускает
   writing-support invocations на legacy agents для
   strategies.md scaffolding. Оба не имеют принятого решения.
   Phase A = meta-agent-bridge как default (meta-agent weekly
   audit охватывает все agents).

4. **Boundary condition для DRR-записи:** что считается «циклом»
   для компаундирования — завершённый Task или завершённый
   brigadier-orchestrated wave? Текущая практика: compound step
   происходит после каждого полного brigadier cycle (все waves
   закрыты + gate acked). Single-Task DRR не автоматичен.

---

## Синтетические claims (F / ClaimScope / R)

- **claim:** DRR-compound mechanism является leverage point L5
  (Meadows — цели системы) для Jetix: он определяет что система
  «хочет учить» в следующем цикле.
  **F:** F4 (operational convention; 3 cycles of evidence)
  **ClaimScope:** holds для swarm-internal cycles; не верифицировано
  для legacy 14-agent roster; не верифицировано при >5 parallel
  cycles.
  **R:** refuted если через 10 cycles brigadier/strategies.md
  не показывает изменения в behaviour (decision-making patterns
  unchanged despite entries); accepted если Gate-learnings
  measurably reduce retry-rate or ap_cost over time.

- **claim:** sandbox-черновик pattern (audio_520) создаёт
  balancing loop (−): pressure for upstream changes → DRR
  draft → brigadier gate → canonical promotion. Loop prevents
  drift by slowing unchecked changes.
  **F:** F3 (multi-case pattern; confirmed across 4 gates
  A-B-C-D of cyc-km-materialization-mvp)
  **ClaimScope:** holds для swarm-internal changes; выход за
  boundary (external API changes, Anthropic model updates) вне
  контроля этого loop.
  **R:** refuted если одна canonical write происходит без
  DRR-entry или brigadier-gate (AP detection).

---

## Dissents preserved (per E-5)

Диссентов по данному synthesis нет: все входящие источники
согласованны в описании механизма. Потенциальное несоответствие
между legacy-agent roster (CLAUDE.md MGMT/OPS/Brain departments)
и swarm-expert roster (5 domain experts) зафиксировано как
информационный разрыв, не диссент — это два слоя одной системы
в Phase A, не конкурирующие архитектуры.

---

*End of §L3 synthesis draft.*
*Return path: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-systems-integrator-L3-synthesis.md*
