---
title: Phase 0 — FPF-линза + scope + чтение субстрата (Notion 3-Layers Architecture v2)
date: 2026-05-25
type: phase-report-fpf-lens-substrate
parent_prompt: prompts/notion-templates-3-layers-architecture-v2-2026-05-25.md
parent_main: decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md
supersedes_ref: reports/notion-templates-4-layers-architecture-2026-05-25/01-fpf-lens-scope.md (v1 — DELTA reference)
phase: 0
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-notion-templates-3-layers-architecture-v2-2026-05-25
R: low
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + IP-1 STRICT + R12 paired-frame STRICT (Layer 2 Jetix overlay) + append-only
language: russian primary
---

# Phase 0 — FPF-линза + scope + чтение субстрата (v2)

> **Что в этой фазе.** Кладём общий понятийный фундамент перед тем как проектировать 3 уровня:
> что такое «слой Notion» на языке FPF, что такое поток между слоями, кого обслуживаем, и —
> два новых для v2 принципа — **STANDALONE** (каждый слой работает один) и **SIMPLIFICATION**
> (baseline минимален, расширения вынесены в sidebar). Это рамка для Phase 1–13.

---

## §0 Что изменилось vs v1 (DELTA — read first)

v1 (`prompts/notion-templates-4-layers-architecture-2026-05-25.md`) был прогнан полностью
(14 фазовых отчётов + 10 схем). v2 — **принципиальное упрощение и переструктура** по голосовому
фидбэку Руслана 25.05 вечером.

| Что | v1 (4 слоя) | v2 (3 слоя) |
|---|---|---|
| Число слоёв | 4 | **3** (Layer 2 «Personal Expanded» УДАЛЁН — будет отдельным «инструменты + skills» слоем в другой итерации) |
| Layer 1 | Personal Core | Personal Core **REVISED** (Daily Log enhancements + Reviews + Strategic sub) |
| Layer 2 | Personal Expanded | → стал **Team Collaboration** (бывший L3): Generic baseline + **Jetix overlay отдельным template** + Brand pattern |
| Layer 3 | Team Collaboration | → стал **Universal Business Foundation** (бывший L4): simplified + Hypotheses + Vision/Goals страницы; Jetix overlay **deferred** |
| Layer 4 | Universal Business + §5.X Jetix overlay внутри | удалён как отдельный слой; Jetix overlay **вынесен** из base |
| Шаблоны внутри | «задрочено», 50+ полей per DB | **SIMPLIFICATION**: minimum baseline + «🔧 что можно добавить» sidebar отдельно |
| Связь слоёв | строгая лестница L1→L2→L3 + L4 standalone | **STANDALONE каждый** + fast-connect opt-in |
| AI Tools | — | **NEW отдельный mega-page** (15+ инструментов) |

**Источник DELTA:** прямая речь Руслана — «слои интересно, а внутри шаблоны так вообще пиздец
блять настолько задрочено… Максимально просто для первых этапов, потом можно усложнять».
Отсюда два новых мандата ниже.

---

## §1 FPF-линза: «Что такое слой Notion в терминах FPF?»

FPF (Foundational Practices Framework, конституционная спека Jetix) различает четыре сущности,
и каждый из 3 уровней раскладывается на них чисто. Это снимает путаницу «слой = таблица» —
слой это **система целиком**, а таблицы внутри — артефакты.

| Сущность FPF | На человеческом | Где в архитектуре v2 |
|---|---|---|
| **Система** | замкнутый контур, который что-то делает и держит состояние | каждый из 3 слоёв = отдельная система (standalone) |
| **Под-система** | часть системы со своей функцией | биржа навыков, движок брифинга, weekly-review engine — под-системы внутри слоя |
| **Артефакт** | типизированный рабочий продукт / запись, которая версионируется | каждая **база Notion** = контейнер артефактов; строка = артефакт; поле = атрибут |
| **Контейнер роли** | абстрактный тип-роль (U.Episteme) с правами/обязанностями | «Лидер», «Контрибьютор», «Основатель» = роли; **не** конкретные люди |

**Главный вывод (IP-1 STRICT):** описываем **роли-типы**, не людей. «PM» = контейнер роли;
«Ruslan, действующий как PM» = *binding* исполнителя к роли в RUSLAN-LAYER, не в generic-схеме.
Поэтому Layer 2 Generic описывает абстрактные слоты ролей; Jetix overlay (отдельный template)
добавляет конкретные 10 ролей и имена-примеры.

**3 слоя как системы:**

- **Layer 1 Personal Core** — одно-агентная система: человек + Claude Code как помощник. Контур
  замкнут на одном. Артефакты: ~8 баз (упрощённых). Роль одна (владелец). **Standalone.**
- **Layer 2 Team Collaboration** — мульти-агентная система: N людей в общем workspace. Generic
  baseline (абстрактные слоты ролей) + Jetix overlay (10 ролей + R12 + Mondragón) **отдельным
  fork-able template**. **Standalone** (любая команда без Personal OS под капотом).
- **Layer 3 Universal Business Foundation** — исполнительный контур над всей деятельностью.
  Generic (любой бизнес). 12 групп баз + Hypotheses + Vision/Goals страницы. Jetix overlay =
  next iteration (НЕ в этом run'е). **Standalone.**

---

## §2 FPF-линза: «Что такое поток между слоями?» (для v2 — все потоки opt-in)

Потоки между уровнями — не «копирование данных». На языке FPF + кибернетики это типы связи,
которые нельзя путать, иначе ломается приватность. В v2 **все потоки = opt-in** (STANDALONE мандат).

| Тип потока FPF | Кибернетика | Пример в v2 | Направление |
|---|---|---|---|
| **Наблюдение** | сенсор без управления | Personal → Team: человек публикует выбранное (opt-in) | вверх |
| **Сигнал** | вход в Part 2 (Signal Ingestion) | Team → Personal: уведомления, назначения роли | вниз |
| **Агрегация** | сумматор наблюдений | Team → Business: метрики когорт → KPI бизнеса | вверх |
| **Контроль** | управляющий сигнал (Part 11) | Business → Team: стратегическое направление, R12-аудит | вниз |
| **Изоляция** | разрыв контура | личные финансы / Daily Log / Life Pulse **никогда** не текут наверх | нет потока |

**Закон приватности (красная линия):** вверх — **только по явному решению человека** (opt-in
publish). Вниз — сигналы/контроль, но **не** копирование чужих приватных данных. Наследие Team
OS §3 «изоляция данных» + Pillar C «файлы = источник истины».

**Где это в Foundation:** наблюдение/сигнал вверх ↔ Part 2; контроль вниз ↔ Part 11; внешние
гости ↔ Part 10; права+роли ↔ Part 4; ревью владельцу ↔ Part 9. Все LOCKED — только ссылки (R2 STRICT).

---

## §3 ⭐ Два новых мандата v2

### §3.1 STANDALONE-capable принцип

**Определение:** каждый из 3 слоёв = самодостаточная система, которую можно взять **отдельно**,
не разворачивая остальные.

- Layer 1 один = «навести порядок в своей жизни». Не требует команды или бизнеса.
- Layer 2 один = команда координируется в общем workspace. Не требует, чтобы у каждого был
  Personal OS под капотом.
- Layer 3 один = founder видит весь бизнес с одной страницы. Не требует Layer 1/2.

**Fast-connect = opt-in, не дефолт.** Если человек хочет соединить (например founder: Layer 1
personal daily + Layer 3 business management) — мы продумываем механику соединения (linked views,
synced blocks), но это **опция**, а не обязательство. По умолчанию — три независимых системы.

**Почему это правильно (philosophy-expert линза):** требовать «сначала разверни всё» = высокий
порог входа + хрупкость (одна точка отказа). Standalone = низкий порог + композируемость
(Unix-философия: маленькие самодостаточные части, соединяемые по желанию).

### §3.2 SIMPLIFICATION принцип

**Определение:** каждая база = **минимум полей baseline** + отдельный sidebar «🔧 Что можно ещё
добавить» (как инструкция, не как живые поля).

- НЕ 50+ полей per DB. Baseline = столько полей, сколько нужно, чтобы база заработала сегодня.
- Всё «продвинутое» (аналитика, формулы, advanced tracking) → в инструкцию-sidebar «добавь когда
  дорастёшь».
- Density мы вкладываем в **объяснения / примеры / схемы / cross-layer механику / AI tools**, а
  **НЕ** в количество полей.

**Почему (engineering-expert + systems-expert линза):** over-engineered шаблон с 50 полями =
никто не заполняет → база мёртвая. Минимальный baseline, который заполняется за минуту →
привычка закрепляется → потом наращиваешь. Прогрессивное раскрытие сложности (progressive
disclosure) бьёт «всё сразу» на порядок по adoption.

---

## §4 Аудитория по слоям (кого обслуживаем)

| Слой | Главный пользователь | Что держит в голове | Время на старт (simplified baseline) |
|---|---|---|---|
| **Layer 1** | любой человек (форк за час) | «как навести порядок в своей жизни/работе» | ≤30 мин |
| **Layer 2** | команда из N человек с общим котлом | «как честно работать вместе, не запирая друг друга» | 1 неделя онбординга / baseline за день |
| **Layer 3** | **любой founder/executive любого бизнеса** | «как видеть весь бизнес с одной страницы» | 2–2.5 часа на минимум |

**Критично (per Ruslan voice):** аудитория Layer 3 — это **не Jetix**. Это владелец консалтинга,
основатель SaaS, директор агентства, координатор кооператива. Jetix = частный пример,
наслаиваемый сверху как optional overlay в **следующей итерации**, не сейчас. Тон base —
«вот универсальный шаблон для управления бизнесом», не «вот наша корпорация Jetix».

---

## §5 Прочитанный субстрат (inventory)

| Документ | Что взято | Роль в v2 |
|---|---|---|
| **v1 prompt + 14 фазовых отчётов** (`reports/notion-templates-4-layers-architecture-2026-05-25/`) | вся структура, контент слоёв, 10 схем, voice | **DELTA-база v2** (адаптируем, упрощаем, переструктурируем) |
| `PERSONAL-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md` (671 строк) | 14 баз-кандидатов, LITE/STANDARD/FULL, 8 шаблонов ревью, 2-слойный fork | **Layer 1 baseline** |
| `TEAM-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md` (758 строк) | 10 ролей, матрица прав, Project Catalog, Skills/Needs, Charter, 4 monetization, onboarding 7 дней, R12 | **Layer 2 baseline** |
| `PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md` (463 строк) | Build/Run/Scale, 4 типа партнёров × этап, R12-риск растёт | **Roadmap (Phase 9) + R12 sweep (Phase 10)** |
| `DOCS-CLASSIFICATION-2026-05-25.md` (317 строк) | 4 категории документов baseline | **Стиль + Layer 3 Documents Hub** |
| `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md` | 75/25, тиры, Mondragón 5:1, triple-role, fork-and-leave, plain-Russian стиль | **Стиль + Layer 2 Jetix overlay** |

Foundation parts (read как reference, R2 STRICT, не тронуты): Part 2/4/9/10/11 + Pillar C
(12 правил + R12). Все LOCKED — только ссылки.

---

## §6 Constitutional posture Phase 0

- **R1 surface only** — линза + scope; никаких стратегических решений; всё surfaced для Ruslan.
- **R2 STRICT** — Foundation / LOCKED / principles / shared/schemas читаются как материал, не тронуты.
- **R6** — каждый тезис привязан к источнику (§5 inventory).
- **R11 Default-Deny** — Notion API НЕ зовётся; это спека, не реализация; NO sample real data.
- **R12 paired-frame STRICT** — активируется только на Layer 2 Jetix overlay (Phase 3 Part B + Phase 10).
- **IP-1 STRICT** — слой = система; база = артефакт; роль = контейнер; человек = binding (RUSLAN-LAYER).
- **Append-only** — новые файлы; v1 output сохраняется (Phase 13 deprecation note, не удаление).

---

*Phase 0 closure (v2). FPF-линза: 3 слоя = 3 standalone-системы; базы = артефакты; роли =
контейнеры (IP-1); потоки = наблюдение/сигнал/агрегация/контроль/изоляция, все opt-in. Два новых
мандата: STANDALONE (каждый слой один) + SIMPLIFICATION (baseline минимум + sidebar расширений).
Аудитория Layer 3 = любой бизнес; Jetix overlay deferred. Субстрат прочитан (v1 = DELTA-база).
Дальше Phase 1 — обзор 3 слоёв + STANDALONE + fast-connect + 2 схемы.*
