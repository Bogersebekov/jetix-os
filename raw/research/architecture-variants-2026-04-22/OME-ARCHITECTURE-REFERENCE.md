---
id: ome-architecture-reference-2026-04-17
title: OME Architecture Reference (conceptual map from Automatica)
date: 2026-04-17
added_to_registry: 2026-04-21
type: inspiration-reference
status: reference
binding: no — inspiration only, NOT a locked decision
source: Ruslan shared visual "Как устроен OME" (Automatica, 2026-04-17)
purpose: |
  Concept map Ruslan найденный созвучным архитектуре Jetix. Writers D1/D2/D3
  и Stage 6 architects должны прочитать этот reference и УЧИТЫВАТЬ при дизайне,
  но это НЕ overriding locked decision — это inspiration-level guidance.
---

# OME Architecture Reference

> **Status:** Inspiration reference, NOT binding decision. Ruslan share'нул 2026-04-21 с комментарием: *"У нас, в принципе, система будет такая же, ну, в какой-то степени"*.
>
> **Use by:** D1 / D2 / D3 writers (Stage 3), D4 compressor (Stage 4), 6 architects (Stage 6). Read + учитывать + not override locks.

---

## Визуальная структура (concept map)

Ruslan's описание показывает 6 layers архитектуры ОМЕ (Автоматика):

### Layer 1: Центр — Владелец-архитектор

**В самом центре** — "Владелец-архитектор".

НЕ просто "founder" / "solo owner" — а **роль архитектора**. Эта роль явно выделена и labeled — сигнал что центральная функция = designing + maintaining system, не execution.

### Layer 2: Human decision orbit (что владелец НЕ делегирует)

Вокруг владельца-архитектора — **6 non-delegatable функций**:
- **Стратегия** (strategic direction)
- **Вкус** (taste / judgment на качество)
- **Ответственность** (accountability / skin-in-game)
- **Утверждение** (approval / sign-off)
- **Эскалация** (escalation paths)
- **Отношения** (key relationships)

Это decisions + judgment layer — владелец сам. Agents не могут это делать.

### Layer 3: Agent orbit (6 делегируемых функций)

Дальше — **6 agent roles** (каждый помечен "АГЕНТ"):
- **Продукт** (product agent)
- **Операции** (operations agent)
- **Исследования** (research agent)
- **Продажи** (sales agent)
- **Контент** (content agent)
- **Поддержка** (support agent)

Это execution layer — делегируется agents (AI-agents или комбинация AI+human).

### Layer 4: Reserve (failover layer)

**Слева** — "Резерв" — запасные провайдеры и маршруты:
- Второй провайдер моделей (Anthropic fallback → OpenAI / Google etc)
- Дублирующие подрядчики
- Сохранённые снимки состояния (state snapshots)

Это **resilience / antifragility layer** — если primary отказывает, fallback активируется.

### Layer 5: Temp workers (on-demand specialist layer)

**Справа** — "Временные сотрудники":
- Дизайнер, юрист, монтажёр
- Эксперт под конкретную задачу
- Подключаются на короткий срок

Это **on-demand specialist pool** — не постоянная команда, не agent (human-only). Для specific skills которые не надо автоматизировать.

### Layer 6: Foundation (shared infrastructure)

**Под** всей orbit structure — **Фундамент**:
- **Протоколы** (protocols)
- **Контракты** (contracts / взаимодействия между agents)
- **Память** (memory / knowledge base)
- **Оценки** (evaluations / metrics)
- **Логи** (logs / audit trail)

Это common infrastructure layer — на чём все остальные layers работают.

**Detailed Foundation breakdown** (из второго visual "Главный актив OME" от Automatica 2026-04-17):

| Элемент | Что в нём |
|---|---|
| **Контракты агентов** | За что отвечает каждый агент: вход, выход, критерий готовности, зона влияния |
| **Контракты подрядчиков** | Формат задачи, критерии приёмки, канал связи, момент включения результата в общий поток |
| **Протоколы передачи** | Как работа переходит между шагами: что считается законченным, какие артефакты сопровождают передачу |
| **Протокол эскалации** | Когда система зовёт основателя: низкая уверенность модели, нестандартный запрос, высокий риск |
| **Общая память** | Контекст между итерациями: факты о клиентах, решения, история правок, открытые вопросы |
| **Метрики качества** | По каким характеристикам каждый процесс измеряется. Проверка идёт непрерывно, на каждой итерации |
| **Приборная панель** | Что видно каждую неделю: зависимость от основателя, выручка на час, частота сбоев |
| **Резервные маршруты** | Что делает система при отказе провайдера: запасной путь, деградированный режим, уведомление |

**Ключевой insight:** OME trata Foundation layer не как "набор tools", а как **главный актив** системы. То есть **не agents, не владелец, не клиенты — сам Foundation является main asset** потому что без него всё ломается.

**Implications для Jetix:**
- **Контракты агентов** — каждый наш agent (11 в CLAUDE.md) должен иметь formal contract: вход / выход / готовность / зона влияния. Сейчас этого нет — это D4 Architecture-Brief requirement.
- **Контракты подрядчиков** — для "временных сотрудников" (Decision 11 продюсерский центр ecosystem) — formal briefing + acceptance criteria + integration point.
- **Протоколы передачи** — handoff между Phase 0 → Phase 1 → Phase 2, между агентами, между Ruslan и future team members (Decision 2 team-ready-scaffolding). Это governance layer.
- **Протокол эскалации** — конкретные triggers когда AI / agents делегируют обратно Ruslan: low confidence / non-standard request / high risk. Это делает Decision 2 operational.
- **Общая память** — maps на нашу wiki/ + ATOM-REGISTRY + CLAUDE.md (per D17: filesystem source of truth).
- **Метрики качества** — continuous, не periodic. Каждая iteration проверяется. Это **критично для D2 Philosophy** (quality fundamentals + фрактальность).
- **Приборная панель** — weekly review с фиксированными метриками (совпадает с Layer 7 dashboard).
- **Резервные маршруты** — multi-provider + degraded mode + notification. Operational resilience.

### Layer 7: Dashboard metrics (health monitoring)

**Самый низ** — "Панель показателей":
- **Часы архитектора / неделя:** 18 ч
- **Зависимость от основателя:** <30%
- **Выручка в месяц:** ↑ (target metric)
- **Частота сбоев / MTTR:** 3 · 42 мин

Это **health dashboard** — ключевые KPIs операционного здоровья системы.

---

## Resonance с 18 locked decisions

### Strong resonance (mapped)

| OME element | Jetix locked decision | Notes |
|---|---|---|
| **Владелец-архитектор** как central role | Decision 2 (Solo-now-with-team-ready-scaffolding) | Ruslan = architect, не просто founder. Scaffolding для подключения 2-3rd pilot. |
| **Зависимость от основателя <30%** metric | Decision 2 | Concrete measurement of team-ready-scaffolding success |
| **Human decision orbit** (6 non-delegatable) | Decision 2 + Decision 8 (layered identity) | Strategy / taste / accountability — архитекторская роль Ruslan'а preserved как layered identity |
| **Agents orbit** (6 роли) | CLAUDE.md current 11-agent roster | Jetix имеет analogous structure (manager, sales-lead, researcher, etc) |
| **Резерв / failover** | D17 (filesystem source of truth) + universality criterion | Filesystem resilience + multi-vendor fallback |
| **Временные сотрудники** | Decision 11 (продюсерский центр + временные контракты) | Sub-contractors for specific skills, не full employees |
| **Фундамент: Протоколы / Контракты / Память / Оценки / Логи** | D4 Architecture-Brief requirements | Maps 1:1 на D4 architects нужны для design |
| **Foundation = main asset** frame | D2 Philosophy (quality fundamentals) + D4 architecture | Jetix Foundation (wiki + ATOM-REGISTRY + protocols) тоже primary asset |
| **Контракты агентов / подрядчиков formal** | D4 Architecture-Brief — обязательный input | Writers D4 должны include formal agent contracts + handoff protocols |
| **Протокол эскалации** (low confidence / non-std / high risk) | Decision 2 operationalization | Makes "solo-with-team-ready-scaffolding" concrete through escalation triggers |
| **Метрики качества continuous** | D2 фрактальность качества + D15 revenue-gated | Continuous validation, not periodic checkpoint |
| **Dashboard metrics** | D15 (revenue-gated spend) + D2 (solo-team scaling) | Measurable thresholds triggering decisions |

### Возможные divergences (Jetix-specific)

OME концепт — **operations-facing**. Jetix добавляет layers OME не имеет:
- **Community / Secure Network** layer (Phase 2+ per D5 и D16) — OME не показывает community как first-class layer
- **Investment-fund philosophy** (D11) как meta-frame — OME operates на фиксированном budget, Jetix operates на Resource-Allocation Engine mentality
- **Layered identity** (D8) — Jetix имеет multiple faces (company / network / corporation / etc), OME — один face
- **200-year civilizational vision** — не присутствует в OME frame

---

## Implications для writers / architects

### D1 Vision writer

- Добавь reference к "Владелец-архитектор" концепту в секции "Operating model" — это укрепляет Decision 2 phrasing
- **Dashboard metrics** можно упомянуть как aspirational measures в Phase milestones

### D2 Philosophy writer

- **Human decision orbit** (Strategy / Taste / Accountability / Approval / Escalation / Relationships) = **non-delegatable core** — это operating principle. Write это явно как принцип.
- **Foundation layer** (протоколы / контракты / память / оценки / логи) aligns с Ruslan'овской Methodology-as-Product frame + Левенчук FPF

### D3 Plan writer

- **Dashboard metrics** — прямой источник health checkpoint metrics для Phase transitions (часы архитектора / dependency / revenue / failures)
- **Reserve + Temp workers** layers — guidance для Phase 1/2 team structure (agents + temp specialists + reserve providers)

### D4 Architecture-Brief (Stage 4) + 6 architects (Stage 6)

- **OME 6-layer structure** (Center / Decision orbit / Agent orbit / Reserve / Temp / Foundation) — сильный **reference model** для Jetix architecture
- НО — Jetix добавляет Community layer + layered identity mechanics. Architects не копируют OME, а **расширяют**
- **Protocols / Contracts / Memory / Evals / Logs** = mandatory foundation layers для Jetix architecture

---

## Key insight для Ruslan voice

Ruslan сказал: *"система будет такая же, ну, в какой-то степени"*.

**"В какой-то степени"** — это ключ. OME — **inspiration pattern**, не copy. Jetix наследует structural wisdom (layered architecture, non-delegatable decisions, dashboard metrics), но расширяет:
- Multi-face identity (Decision 8)
- Community platform (Phase 2+)
- Investment-fund philosophy
- Civilizational horizon

---

## How to use this file

- **Stage 3 writers (D1/D2/D3):** Read как one из mandatory inputs. Используйте для inform выбора секций + принципов + метрик. НЕ переписывайте OME дословно — integrate reference.
- **Stage 4 compressor (D4):** Include summary OME mapping table в D4 brief — architects должны видеть resonance.
- **Stage 6 architects:** Use OME структуру как **variant basis**. Not all 6 variants должны копировать OME — но at least 1-2 variants должны heavily inspired.

**Binding status:** NOT binding (не override locks). But mandatory reading.
