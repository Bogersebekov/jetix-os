---
title: Phase 0 — FPF-линза + чтение субстрата (Notion 4-Layers Architecture)
date: 2026-05-25
type: phase-report-fpf-lens-substrate
parent_prompt: prompts/notion-templates-4-layers-architecture-2026-05-25.md
parent_main: decisions/strategic/NOTION-TEMPLATES-4-LAYERS-ARCHITECTURE-2026-05-25.md
phase: 0
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-notion-templates-4-layers-architecture-2026-05-25
R: low
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + IP-1 STRICT + append-only
language: russian primary
---

# Phase 0 — FPF-линза + scope + чтение субстрата

> **Что в этой фазе.** Прежде чем проектировать 4 уровня, кладём общий понятийный фундамент:
> что такое «слой Notion» на языке FPF (система / под-система / артефакт / контейнер роли),
> что такое «поток между слоями» (наблюдение / контроль / синк), кого мы обслуживаем на
> каждом уровне, и какой субстрат прочитан. Это рамка для Phase 1-14.

---

## §1 FPF-линза: «Что такое слой Notion в терминах FPF?»

FPF (Foundational Practices Framework, конституционная спека Jetix) различает четыре сущности,
и каждый из 4 уровней раскладывается на них чисто. Это снимает путаницу «слой = таблица» —
слой это **система целиком**, а таблицы внутри неё — артефакты.

| Сущность FPF | На человеческом | Где в нашей архитектуре |
|---|---|---|
| **Система (system)** | замкнутый контур, который что-то делает и держит своё состояние | каждый из 4 уровней = отдельная система |
| **Под-система (sub-system)** | часть системы со своей функцией | биржа навыков, дашборд финансов, движок брифинга — под-системы внутри слоя |
| **Артефакт (artefact)** | типизированный рабочий продукт / запись, которая живёт и версионируется | каждая **база данных Notion** = контейнер артефактов; строка = артефакт; поле = атрибут |
| **Контейнер роли (role-container)** | абстрактный тип-роль (U.Episteme), к которому привязаны права и обязанности | «Управляющий», «Инвестор», «Основатель» = роли; **не** конкретные люди |

**Главный вывод линзы (IP-1 STRICT):** в схеме мы описываем **роли-типы**, а не людей. «PM» —
это контейнер роли с правами; «Ruslan, действующий как PM» — это *binding* конкретного
исполнителя к роли, и он живёт в RUSLAN-LAYER, а не в generic-схеме. Поэтому Layer 4 generic
base описывает «Members DB» и «Roles DB» абстрактно; Jetix-overlay (§5.X) добавляет конкретные
10 ролей и конкретные имена-примеры (Ruslan / Дмитрий / Maxim / Сева / Прапион / Левенчук / Цэрэн).

**Каждый из 4 уровней как система:**

- **Layer 1 Personal Core** — одно-агентная система: человек + Claude Code как единственный
  помощник. Контур замкнут на одном человеке. Артефакты: 5-8 баз. Роль одна (владелец).
- **Layer 2 Personal Expanded** — та же система, обогащённая под-системами аналитики и
  гипотез-движка. Не новая система — надстройка наблюдательных контуров над Layer 1.
- **Layer 3 Team Collaboration** — мульти-агентная система: N систем Layer 1+2, соединённых
  общей координирующей под-системой (shared workspace). Здесь появляются роли-контейнеры (10),
  биржа, Charter, учёт вклада.
- **Layer 4 Universal Business Foundation** — система управления бизнесом: исполнительный
  контур над всей деятельностью. Generic (любой бизнес). Артефакты: 12 групп баз (§5.1-§5.12).
  Роли абстрактны (user определяет свои). Jetix — один частный инстанс через overlay.

---

## §2 FPF-линза: «Что такое поток между слоями?»

Потоки между уровнями — это не «копирование данных». На языке FPF + кибернетики (линза
systems-expert) это три разных типа связи, и их нельзя путать, иначе ломается приватность.

| Тип потока FPF | Кибернетика | Пример в архитектуре | Направление |
|---|---|---|---|
| **Наблюдение (observation)** | сенсор без управления | Personal → Team: человек публикует выбранное (opt-in), команда *видит* | вверх |
| **Сигнал (signal ingest)** | вход в Part 2 (Signal Ingestion) | Team → Personal: уведомления, @упоминания, назначения роли | вниз |
| **Агрегация (rollup)** | сумматор наблюдений | Team → Business: метрики когорт сворачиваются в KPI бизнеса | вверх |
| **Контроль (control)** | управляющий сигнал (Part 11) | Business → Team: стратегическое направление, результаты R12-аудита, решения Хранителя | вниз |
| **Изоляция (boundary)** | разрыв контура | личные финансы / Daily Log / Life Pulse **никогда** не текут наверх | нет потока |

**Закон приватности (красная линия):** вверх (личное → командное → бизнес) — **только по
явному решению человека** (opt-in publish). Вниз — сигналы и контроль (уведомления, направление,
аудит), но **не** копирование чужих приватных данных. Это прямое наследие Team OS §3
«изоляция данных» и принципа Pillar C «файлы = источник истины».

**Где это в Foundation:**
- наблюдение/сигнал вверх ↔ Part 2 (Signal Ingestion & Triage);
- контроль вниз ↔ Part 11 (Strategic Direction Substrate);
- внешние гости/партнёры ↔ Part 10 (External Touchpoints);
- права + роли ↔ Part 4 (Role Taxonomy & Coordination Protocol);
- ревью/брифинг владельцу ↔ Part 9 (Owner Interaction Scaffold).

---

## §3 Аудитория по слоям (кого обслуживаем)

| Слой | Главный пользователь | Что он держит в голове | Время на старт |
|---|---|---|---|
| **Layer 1** | любой человек (форк за час) | «как навести порядок в своей жизни/работе» | ≤30 мин |
| **Layer 2** | опытный пользователь Layer 1 | «как извлечь из своих данных аналитику и гипотезы» | +1 неделя add-ons |
| **Layer 3** | команда из N человек с общим котлом | «как честно работать вместе, не запирая друг друга» | 1 неделя онбординга |
| **Layer 4** | **любой founder/executive любого бизнеса** | «как видеть весь бизнес с одной страницы и управлять им» | 2-3 часа на минимум |

**Критично для Layer 4 (per Ruslan voice 25.05):** аудитория Layer 4 — это **не Jetix**. Это
владелец консалтинга, основатель SaaS, директор агентства, координатор кооператива — любой.
Jetix = только один пример применения, наслаиваемый сверху как optional overlay. Тон base должен
звучать «вот универсальный шаблон для управления бизнесом», а не «вот наша корпорация Jetix».

---

## §4 Быстрый скан референсных enterprise-OS систем (sota-tracker линза)

F2-F3 derivative — без нового ресёрча; это общая известная карта, чтобы Layer 4 generic base
не изобретал велосипед, а опирался на проверенные паттерны «компания как операционная система».

| Референс | Паттерн, который берём в Layer 4 generic | Чего избегаем |
|---|---|---|
| **Notion as company OS** (публичные шаблоны Notion для стартапов) | единый воркспейс: стратегия + проекты + люди + знания связаны relations | перегруз 30+ баз для маленькой команды |
| **Linear** | чистая модель «проект → задача → статус» + cycles | жёсткая привязка к разработке ПО (Layer 4 шире) |
| **Coda / ClickUp** | формулы + rollup + связанные таблицы как «живой дашборд» | over-engineering автоматизаций |
| **EOS / Traction (Rocks)** | квартальные «камни» + scorecard метрик + L10 встречи | догматичность одного фреймворка (Layer 4 framework-agnostic) |
| **Mondragón corporate governance** | кооперативный exec-view: ratio-cap, social fund, member councils | применять насильно — это Jetix-overlay, не base |
| **OKR / V2MOM / Hoshin Kanri** | цель → метрика → owner → горизонт | навязывать один framework — Layer 4 даёт слот, user выбирает |

**Вывод:** Layer 4 generic base = «компания как операционная система» в духе Notion-as-company-OS,
но **framework-agnostic** (слот под OKR/V2MOM/EOS/любой) и **governance-agnostic** (слот под
иерархию/плоскую/матрицу/кооператив). Конкретный выбор фреймворка и управления = extension points
внутри каждой базы. Mondragón/R12/кооператив = один из выборов, вынесенный в Jetix-overlay.

---

## §5 Прочитанный субстрат (inventory)

Полностью прочитаны (FULL read, не excerpt):

| Документ | Что взято | Роль в архитектуре |
|---|---|---|
| `PERSONAL-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md` (44K) | 14 баз-кандидатов, LITE/STANDARD/FULL, матрица голоса, 8 шаблонов ревью, 2-слойный fork, 5 ниш | **Layer 1+2 baseline** |
| `TEAM-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md` (57K) | 10 ролей, матрица прав 10×10, Project Catalog 14 полей, Skills/Needs, Charter 6 секций, 4 monetization, Daily Brief, onboarding 7 дней, R12 | **Layer 3 baseline** |
| `PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md` (34K) | Build/Run/Scale, 4 типа партнёров × этап, R12-риск растёт с этапом, 4-недельный план | **Implementation roadmap (Phase 11) + R12 sweep (Phase 12)** |
| `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md` | 75/25, тиры L1-L7, Mondragón 5:1, triple-role, fork-and-leave, стиль | **Стиль + Jetix-overlay §5.X** |
| `ECONOMIC-MODEL-TOKENOMICS-2026-05-22.md` (V10, 22K) | 3-layer recursive 25%, triple-role, Mondragón 60/40 + 5:1, 4 монетизации, Ethereum Phase 2+ | **Jetix-overlay §5.X (финансы + governance)** |
| `EXECUTION-PLAN-FIXATION-2026-05-24.md` (46K) | 4 типа партнёров (T1-T4), 8 вопросов R12, 2 направления, sequencing | **Jetix-overlay + R12 8-questions canonical** |
| `RUSLAN-NOTES-EDUCATION-PARADIGM-2026-05-24.md` (16K) | прошивка vs накопление, adequate intellect, hypothesis-driven learning (O-176..O-185) | **Layer 1+2 Hypotheses DB + Method V2 §J линза** |

Foundation parts (read как reference, не модифицируются — R2 STRICT): Part 2 (Signal Ingestion),
Part 4 (Role Taxonomy), Part 9 (Owner Interaction), Part 10 (External Touchpoints), Part 11
(Strategic Direction), Pillar C (principles / 12 правил + R12). Все LOCKED — только ссылки.

---

## §6 Constitutional posture Phase 0

- **R1 surface only** — линза + scope, никаких стратегических решений; всё surfaced для Ruslan.
- **R2 STRICT** — Foundation/4 LOCKED/principles/shared/schemas читаются как материал, не тронуты.
- **R6** — каждый тезис привязан к источнику (см. §5 inventory).
- **R11 Default-Deny** — Notion API не зовётся; это спека, не реализация.
- **IP-1 STRICT** — слой = система; база = артефакт; роль = контейнер; человек = binding (RUSLAN-LAYER).
- **Append-only** — новый файл.

---

*Phase 0 closure. FPF-линза положена: 4 слоя = 4 системы; базы = артефакты; роли = контейнеры
(IP-1); потоки = наблюдение/сигнал/агрегация/контроль/изоляция. Аудитория Layer 4 = любой бизнес,
Jetix = частный overlay. Субстрат прочитан FULL. Дальше Phase 1 — обзор 4 слоёв + cross-layer matrix.*
