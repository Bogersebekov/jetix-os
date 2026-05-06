---
title: Jetix Corporation — концептуальный документ (применение Базовой Системы)
type: decision
status: SKELETON v0.1 (drafting in progress)
version: 0.1
created: 2026-05-05
author: Ruslan + Claude
audience: потенциальные партнёры / клиенты / инвесторы / future Jetix members + сам Ruslan для clarity
purpose: дать читателю полное понимание ЧТО такое Jetix Corp как платформа/корпорация — построенная поверх Базовой Системы Управления. Видение, бизнес-модель, фазы эволюции, предложение партнёрам.
parent_document: decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md (Документ 1A — universal foundation)
relationship: Jetix Corp = applied use case Базовой Системы. Базовая Система — каркас. Jetix Corp — конкретная реализация под конкретный бизнес-кейс.
sources:
  - decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md  # parent — каркас
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md  # Workshop metaphor v1 LOCKED (server)
  - decisions/JETIX-TRM-MODEL-2026-04-30.md  # TRM business model LOCKED (server)
  - swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md
  - swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md  # constitutional anchor
  - reports/retrospective_2025-05_to_2026-04.md  # 12mes journey context
  - Notion: Workshop concept LOCKED (3522496333bf817f836edb0c0a25b28e)
  - Notion: TRM model LOCKED (3522496333bf8107b5dae9e000846747)
  - Notion: Jetix Vision Fundamental (decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md)
INCLUDES:
  - Что такое Jetix как платформа / корпорация
  - Jetix как Мастерская поверх Базовой системы
  - TRM модель (mgmt fee + performance fee)
  - Платформа для проектов (свои → объединение)
  - Управляющая компания
  - Большая афёра века / эксперимент
  - Помощь партнёрам экспериментировать
  - Синергия между участниками
  - 3 фазы эволюции (1 владелец → команда → community)
  - Видение 1/3/10 лет
  - Конкретное предложение партнёрам
  - Roadmap к €50K → €1T trajectory
  - Финансовая модель / unit economics
  - ICP (Mittelstand DACH 50-500 emp manufacturing)
NOT_INCLUDED:
  - Generic foundation principles (это в Документе 1A)
  - Архитектура foundation Parts (это в Документе 1A раздел 4)
  - Adaptable станки general (это в Документе 1A раздел 5)
---

# Jetix Corporation

> *Концептуальный документ. Описание Jetix как платформы / корпорации, построенной поверх Базовой Системы Управления. Видение, бизнес-модель, ICP, предложение партнёрам.*

---

## 📖 Как читать этот документ

> *Документ написан для **3 типов аудитории** — каждому свой путь чтения. Базовая Система описана отдельно (Документ 1A) — там общий каркас. Здесь — что построено на нём конкретно.*

**Если ты:**

- **Потенциальный партнёр / Founder заинтересован в коллаборации** — разделы 1, 2, 5, 9, 10 (что Jetix есть / видение / роли партнёров / предложение / роадмап)
- **Потенциальный клиент** (Mittelstand owner / CEO) — разделы 1, 3, 6, 7 (что Jetix / TRM модель / ICP / value prop)
- **Investor / Capital allocator** — разделы 1, 6, 7, 8, 11 (видение / unit economics / ICP / market / roadmap)
- **Сам Ruslan / future Jetix members** — весь документ (canonical reference на видение и стратегию)

**Длина:** TBD (~1500-2500 строк когда complete).

**Связь с Документом 1A:**
- Базовая Система = **каркас** (универсальный для любого мастера)
- Jetix Corp = **специфическая реализация** этого каркаса под конкретный бизнес-кейс (Mittelstand DACH consulting + TRM)
- Если что-то в этом документе не понятно — почитай Документ 1A на ту же тему

---

## 0. TL;DR (one paragraph)

> *[ЗАПОЛНИТЬ В КОНЦЕ — после написания всех разделов написать абзац который суммирует весь документ. Цель: чтобы прочитав только этот блок, человек уже понимал суть на 70%.]*

---

# 1. 💡 Что такое Jetix Corporation

> **Цель раздела:** дать ясное определение Jetix через **2 главных образа** + **что Jetix делает** + **что НЕ есть** + **связь с Базовой Системой**.
>
> *Ниже — несколько one-liner кандидатов и развёрнутое определение. Финальный canonical one-liner будет выбран после review.*

---

## 1.1 One-liner кандидаты — 4 формулировки

### 🥇 Кандидат A — Мета-мастерская
> **Jetix — это мета-мастерская для профессиональных мастеров со своими мастерскими. Самая большая, самая навороченная, самая быстрая и умная мастерская среди всех других — умная за счёт того, что внутри неё работают другие мастера со своими специализированными мастерскими, каждый в своём направлении.**

### 🥈 Кандидат B — Мастерская по работе с информацией
> **Jetix — это мастерская по работе с информацией. Информация о рынке, о проектах, о клиентах, об инструментах — Jetix лучше всех остальных её собирает, перерабатывает, переиспользует и превращает в действия. Из-за этого Jetix может позволить себе быть лучшим investment fund, лучшим research центром, лучшим educational hub, иметь лучших натренированных кадров — потому что информация = всё, а мы с ней работаем лучше других.**

### 🥉 Кандидат C — Engine за счёт сети мастерских
> **Jetix — это умная мастерская, которая работает с информацией и управляет ресурсами лучше всех остальных, потому что внутри неё работает сеть из специализированных мастеров со своими мастерскими (по AI, кибербезопасности, юр.практике, research, инвестициям). Каждый мастер — лидер в своём направлении; Jetix — оркестратор и хаб, который соединяет их и делает всем 10× leverage.**

### 🏅 Кандидат D — Краткий (для visit-card / outreach)
> **Jetix — мета-мастерская по работе с информацией: управляет ресурсами клиентов, делает heavy research, объединяет лучших мастеров в сеть. Чем лучше работаешь с информацией — тем больше можешь.**

---

## 1.2 Развёрнутое определение

### Главная идея
**Jetix — это мастерская, которая работает с информацией.**

Это **первый принцип**, на котором всё строится. Всё, с чем сталкивается Jetix — информация:
- Информация о **рынке** (тренды, конкуренты, opportunities)
- Информация о **проектах** (свои и партнёрские)
- Информация о **клиентах** (их ресурсы, их боли, их возможности)
- Информация о **технологиях** (AI наработки, новые инструменты, фреймворки)
- Информация о **юридическом ландшафте** (законы, регулирование, contracts)
- Информация о **людях** (мастера, partners, кадры)
- Информация о **самой Jetix** (метрики, патт ерны, обучение)

Вход — информация. Внутри — переработка. Выход — переработанная информация (решения, артефакты, действия в реальном мире).

---

### Уникальность Jetix — мета-мастерская

В отличие от **обычной мастерской одного мастера**, которая хорошо специализируется в одном направлении, **Jetix — мета-мастерская**, объединяющая множество специализированных мастеров со своими мастерскими.

Внутри Jetix:
- Работает мастер по **AI / искусственному интеллекту** в своей мастерской
- Работает мастер по **кибербезопасности** в своей мастерской
- Работает мастер по **юриспруденции / законам** в своей мастерской
- Работает мастер по **research / heavy аналитике** в своей мастерской
- Работает мастер по **investment / финансам** в своей мастерской
- Работает мастер по **education / методологиях** в своей мастерской
- ... и так далее, по любым direction'ам которые нужны

**Каждый из этих мастеров — лидер в своём направлении.** Jetix не пытается быть лучшим в каждом — Jetix **собирает лучших** под одной крышей и **оркестрирует их** через общую infrastructure.

Поэтому одна из формулировок: **«Jetix — это самая большая, самая навороченная, самая быстрая и умная мастерская среди всех других — умная за счёт сети внутри.»**

---

### Что Jetix конкретно делает

Несколько направлений деятельности — все они стoят на том, что мастерская работает с информацией:

#### 🏦 1. Total Resource Management (TRM) — управление ресурсами клиентов
Управляем 6 типами ресурсов клиента (финансы / время CEO / аудитория / знания / compute / команда) одновременно. Mgmt fee + performance fee. Это центральная коммерческая offering.
> *Подробно — раздел 3.*

#### 🔬 2. Heavy research и аналитика
Сложные research проекты, market analysis, deep due diligence. Не "google + summary", а **multi-source synthesis с verifiable claims** — то что обычные команды делают за месяцы, Jetix делает за дни через AI-leverage.
> *Связано с разделом 4.*

#### 🛠️ 3. Управление проектами
Внутренние проекты Jetix + партнёрские проекты + клиентские проекты — все управляются через единую Project Lifecycle Substrate (Foundation Part 7).

#### 🔍 4. Поиск и сбор команд
Не recruitment agency. **Curated talent matching** — для конкретных задач партнёров и клиентов находим людей через сеть мастеров и через выверенные критерии (5 критериев качества).

#### 🎓 5. Консультационная деятельность
От €3K разовых гипотез до €40-60K/мес TRM-full mgmt. Лестница 6 уровней (L0-L5).

#### 📚 6. Образовательная деятельность
Передача накопленной методологии — методология применения AI-leverage / методология построения мастерских / методология TRM.

#### 🤖 7. Внедрение AI-наработок
**Не разработка AI-инструментов с нуля.** Внедрение **уже существующих лучших AI-инструментов** в работу клиентов и партнёров. Jetix = **integrator + curator**, не вендор.

#### 🛡️ 8. Поддержание AI-наработок
После внедрения — мониторинг / maintenance / эволюция / адаптация под новые поколения моделей.

#### 🌐 9. Hub лучших разработок (cross-domain)
Jetix — точка консолидации **самых новых и лучших наработок** в:
- Искусственном интеллекте
- Кибербезопасности
- Юр.практике / законах
- Research methodologies
- И других domain'ах по нужде

Партнёры и клиенты получают доступ к этому hub — через Jetix infrastructure.

---

### Главный механизм value generation

**Информация = всё.** Тот, кто лучше работает с информацией → быстрее принимает решения → имеет преимущество во всём остальном.

Jetix организован так, что **работа с информацией — главная компетенция**. Из этого вытекает:

> *Из-за того что Jetix лучше остальных работает с информацией:*
> - Jetix может быть **лучшим investment fund** (лучше анализирует deal flow / patterns)
> - Jetix может быть **лучшим research центром** (лучше синтезирует / faster cycles)
> - Jetix может быть **лучшим educational hub** (методология построена на verifiable knowledge)
> - Jetix может **иметь лучших натренированных кадров** (лучше обучает на накопленной базе)
> - Jetix может **управлять чужими ресурсами лучше владельцев** (TRM работает потому что мы видим больше patterns)

**Это не "ещё один продукт".** Это **архитектурное преимущество** — все вертикали (consulting / education / investment / research / hub) работают благодаря **общей информационной мастерской**, которая обслуживает все направления.

---

### Layered identity — 8 разных лиц одного объекта

Jetix имеет **разные лица для разных observers** + **разных фаз эволюции**. Это не противоречие — это feature: один объект, разные projections.

| Лицо | Кто видит | Когда |
|------|-----------|-------|
| 🏭 **Methodology + OS** | Сам Ruslan | Всегда |
| 🚀 **Корпорация-стартап** | External world | Phase 1+ |
| 💼 **Consulting / Agency** | Клиенты | Phase 1 |
| 🤝 **Network / Platform / Secure Network** | Партнёры | Phase 2+ |
| 👑 **Club Kingsman inside** | Community | Всегда |
| 🌐 **USB-C universal connector** | Tech ecosystem | Phase 3+ |
| 🏢 **Corporation, "имеет вес"** | Investors / Press | Phase 2+ |
| 🌍 **Civilizational infrastructure** | Future history | Phase 4+ / 200y horizon |

> Источник: D8 LOCKED layered identity, JETIX-VISION §4 Decision 8.

**Главное:** при общении с конкретной аудиторией Jetix представляется **тем лицом, которое им резонирует**. Внутренняя грамматика — единая.

---

## 1.3 Что Jetix НЕ является — короткое summary

> *Подробно с тестами — раздел 12. Здесь — главное.*

Jetix **НЕ**:

- ❌ **НЕ classic consulting firm** (Big 4 / McKinsey) — мы не продаём слайды, мы продаём управление результатом
- ❌ **НЕ AI-стартап с продуктом** — мы не делаем "ещё один tool", мы делаем **методологию применения** AI
- ❌ **НЕ holding / investment fund classic** (BlackRock) — мы управляем не только деньгами, а **6 типами ресурсов** одновременно
- ❌ **НЕ accelerator / incubator** — мы не тренируем founders, мы реальный operational partner
- ❌ **НЕ social network** (LinkedIn / TikTok) — мы curated, anti-attention-economy
- ❌ **НЕ note-taking tool** (Notion / Obsidian) — мы методология поверх любых tools
- ❌ **НЕ pyramid / Oriflame / scam** — engineering-faith, real tools, real methodology, founder skin-in-game
- ❌ **НЕ open mass-market** — для людей с **ресурсами + желанием развиваться** (см. §7)

---

## 1.4 Связь с Базовой Системой Управления (Документ 1A)

> *Каркас vs реализация.*

**Базовая Система Управления** (Документ 1A, LOCKED v1.0 2026-05-05) — это **универсальный архитектурный каркас** персональной мастерской. Foundation v1.0 — 11 функциональных Parts + Pillar C, fork-portable, может быть взят любым человеком и адаптирован под себя.

**Jetix Corporation** — это **конкретная applied реализация** этого каркаса под бизнес-кейс «AI-native operational corporation работающая с информацией и управляющая ресурсами клиентов».

### Что общего
- ✅ Все **11 Foundation Parts** активны в Jetix instance
- ✅ **Pillar C principles** — Tier 1 (manager principles) + Tier 2 (11 hard rules) применимы
- ✅ Метафора **Мастерской** — общая (расширена в §2)
- ✅ Принципы работы с информацией / вниманием / временем / ресурсами — общие
- ✅ Knowledge accumulation 3 уровня — общие

### Что специфично для Jetix (RUSLAN-LAYER)
- 🎯 **TRM business model** (6 ресурсов / mgmt+performance fee / лестница L0-L5)
- 🎯 **3 типа участников** (Solo Indie / средний бизнес / TRM-делегаторы — см. §7)
- 🎯 **Layered identity** D8 (8 лиц per observer × phase)
- 🎯 **Korp-Startup positioning** — responsibility-as-scale (D29)
- 🎯 **$1T trajectory** + 200-year civilizational vision
- 🎯 **Phase 1 markets** — English/US infobiz + indie hackers (DE = legal home only)
- 🎯 **Tseren Tserenov** — first concrete Phase 2 partnership target
- 🎯 **Tools под Jetix specifics** (Top Lists Partner Factory / Producer Center / etc.)
- 🎯 **11 archetypes × 5 critical filter** для ICP

### Принципиально важно
> **Foundation v1.0 = fork-portable.** Завтра другой owner со своей нишей возьмёт Foundation, заменит RUSLAN-LAYER на свою (например, medical-researcher-LAYER) — и поедет дальше. **Каркас одинаков, наполнение разное.** Это и делает Базовую Систему универсальным фундаментом, на котором может быть построено множество специализированных мастерских — Jetix лишь одна из них.

> Источник: foundation-master-overview-human-2026-04-29.md final paragraph + Bundle 5 ack 28.04.

---

## 1.X Финальная формулировка для §1

> *Будет выбрана после review кандидатов A/B/C/D в §1.1. На данный момент — **Кандидат B (Мастерская по работе с информацией)** видится наиболее **универсальным и масштабируемым** для разных типов аудитории. Кандидат A (мета-мастерская) — лучше для партнёров. Кандидат D (короткий) — для outreach materials.*

---

# 2. 🏭 Jetix как Мастерская — расширение метафоры

> **Цель раздела:** показать как универсальная метафора Мастерской из Документа 1A применяется специфически в Jetix через **3 фазы эволюции**: одна мастерская одного владельца → команда работает с одной системой → community мастеров с мастерскими (mega-system).

> **База:** Workshop concept LOCKED 30.04.2026 (`decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`).

---

## 2.1 Phase 1 — Jetix как одна мастерская одного владельца (текущее состояние)

### Что это сейчас
**Сейчас Jetix — это первый, мега-маленький вариант мастерской.** Один владелец (Ruslan) + AI-агенты (12 ролей) + накопленная knowledge база + инструменты. Это уже **довольно охуенная мастерская** — но это **только начало**.

> **Verbatim Ruslan:** *«Это уже довольно охуенная мастерская»* — даже на текущем minimal состоянии Phase 1.
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§6 Phase 1]

### Что эта мастерская может уже сейчас (Phase 1 capabilities)

Несмотря на размер «один мастер» — мастерская позволяет:

#### 📚 Получать информацию от лучших учителей
Через `/ingest` любого источника (книги, статьи, lectures от лучших экспертов мира) → переработка → структурированная информация в твоей wiki. Это как иметь **personal knowledge graph всех лучших учителей по твоим темам**.

#### 💬 Быстро общаться с любыми экспертами (через AI-augmented context)
Plan Mode + натренированные агенты на твоей базе → быстро формулируешь вопрос, быстро получаешь синтез из множества источников, быстро готов к разговору с реальным экспертом (если нужен).

#### 🎓 Быстро обучаться
3 уровня Wikipedia (Personal / Insights / Project) + методология library + writeback patterns → **обучение с compound effect**. Каждое обучение опирается на предыдущее, не начинаешь с нуля.

#### 🧠 Быстро решать сложные задачи
12 натренированных AI-агентов под разные роли (researcher / strategist / writer / analyst / etc.) + adaptable станки → задачи которые solo founder делал бы 2 недели — мастерская делает за 2 дня.

#### 👁️ Видеть картину целиком
Visual / View principle (Foundation Part 8 + dashboards) + state-of-system one-pagers → **в любой момент видишь общее состояние** твоей жизни / бизнеса / проектов.

> *Иными словами:* даже мастерская Phase 1 уровня — **это уже мощная штука**. Один человек с Foundation v1.0 LOCKED + 12 ролей + adaptable станки делает то что обычно требует команды 5-10 человек.

### Специализация мастерской Phase 1
Текущая специализация — **Ruslan-мастер**, который занимается:
- AI-leverage methodology
- Total Resource Management R&D
- Workshop concept development
- Phase 1 €50K consulting + producer center

Другой мастер взял бы Foundation, заменил RUSLAN-LAYER на свою — и поехал бы в свою специализацию (medicine / arts / quant trading / coaching / etc.).

### Что есть в мастерской Phase 1 (станки и инструменты)

> **Verbatim Ruslan:** *«полный набор нахуй мега корпорации в одной в одной блять программки в jetix… лучшая research и лучшая блять аналитика up to date… лучшая crm… лучшая блять автоматизация… сбор твоих знаний… ёбаный нож швейцарский нож в виде в мире с Jetix. Это ебаный космический корабль»*
> [src: voice-extract-workshop-people-2026-05-01.md:§1.1.2, audio_565@27-04-2026]

Конкретные станки (текущий arsenal):
- **D2 diagrams** — text → SVG за минуты (system architecture / process flows)
- **MCP integrations** — Notion / Toggl / GitHub / file system / etc.
- **Plan Mode + ultrathink** — стратегические сессии с AI как scribe
- **Voice pipeline** — диктофон → transcription → extraction → review
- **Time-tracking pipeline** — Toggl + AW + sync + reports + 12-mes baseline
- **12 AI-агентов** — Manager / Personal Assistant / Sales Lead/Researcher/Outreach / Knowledge Synth / Crazy Agent / Strategist / Life Coach / Meta Agent / System Admin / Inbox Processor
- **Karpathy LLM Wiki** + HippoRAG retrieval (9 entity types × 9 edge types × 6 niches)
- **Compound learning pipeline** — каждое решение → урок → правило → методология

### Phase 1 trust structure — closed circle
> **Verbatim Ruslan:** *«именно для начальной стадии вот джекса что мы все-таки будем действовать больше как мафия — то есть мы там собрались какие-то свои ресурсы собрали хорошо бизнес там работа да есть это свободные ресурсы инвестируем»*
> [src: voice-extract:§1.9.4, audio_563@27-04-2026]

**Phase 1 → Phase 2 trust evolution:** closed-circle mafia-style trust в начале → постепенно открывается для curated participants → Phase 3 community.

---

## 2.2 Phase 2 — команда работает с одной мастерской

### Что это
Несколько человек + AI + **одна** Jetix-мастерская. Workflow тот же информация-centric. Цель командная. Система чуть-чуть улучшается под team scenarios.
[src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§6 Phase 2]

### Phase 1 → Phase 2 transition trigger
> **Verbatim Ruslan (audio_562@27-04-2026):** *«Мы сейчас заканчиваем этот фондейшн… это, по сути, уже готовый продукт. Это можно уже давать идти людям.»*
> [src: voice-extract:§1.3.1]

**Trigger:** Foundation v1.0 LOCKED ✅ (это произошло 28.04.2026). Phase 1 → Phase 2 ready.

### Phase 2 mechanism — solo консультант → партнёры приводят
> **Verbatim Ruslan (audio_536):** *«для начала я хочу это вот самостоятельно как такой бизнес-консультант… попутно уже сразу накапливать команду… уже эти партнеры за меня другим партнером помогали — будь то финансами, будь то ресурсами»*
> [src: voice-extract:§1.3.2]

**Phase 2 mechanism:**
1. Ruslan начинает делать TRM-lite консалтинг + producer center
2. Первые партнёры подключаются — приносят свои ресурсы / навыки / клиентов
3. Команда растёт до 5-10 человек + virtual augmentation через AI агентов
4. Все работают **в одной Jetix мастерской**, не своих fork'ах
5. Tseren Tserenov идентифицирован как **first concrete Phase 2 partnership target**

### Что меняется в мастерской на Phase 2
- Расширяется Part 4 (Role Taxonomy) — добавляются human roles в дополнение к AI-агентам
- Расширяется Part 8 (Health Monitoring) — multi-person health signals
- Расширяется Part 10 (External Touchpoints) — больше intеграций под team workflows
- Pillar C Tier 1 (Manager principles) — каждый member читает + соглашается до joining

---

## 2.3 Phase 3 — community мастеров с мастерскими (mega-system) ⭐

### Что это — главная concept мета-мастерской
**Phase 3 — это то самое «Jetix как мета-мастерская среди других мастерских»** (см. §1.1 Кандидат A).

> **Verbatim Ruslan:** *«Когда уже будет комьюнити таких вот мастеров с своими мастерскими, можно будет делать уже мега систему — в которой внутри вот эти мастера у которых есть мастерские смогут между собой коммуницировать и работать над уже более сложными проектами/задачами, для которых одной мастерской даже прям хорошо настроенной но одной мастерской одного человека не хватит.»*
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§8 quote 13]

### Как это работает — model
1. **Каждый мастер** имеет **свой fork Foundation** (свою специализированную мастерскую)
2. Мастер берёт **кусок задачи** (часть большой проблемы) в свою мастерскую
3. Внутри своей мастерской **разбирает / перерабатывает / создаёт** свою деталь
4. Выдаёт **одну качественную деталь** обратно в общий community-уровень
5. Все детали **аггрегируются на верхнем (community) уровне** в **finished product**

> Это тоже информационный flow: получили информацию (часть задачи) → выдали информацию (свой результат). Та же мастерская, тот же principle — только теперь сеть.

### Phase 3 trigger
> **Verbatim Ruslan (audio_576@29-04-2026):** Phase 3 trigger = «когда задачи > одной мастерской» — задачи становятся настолько сложными что одна мастерская одного человека (даже хорошо настроенная) не справляется.
> [src: voice-extract:§1.3.3]

### Какие задачи требуют Phase 3 community
- **Cross-domain research projects** (требуют экспертизы AI + кибербез + юр.практика + research одновременно)
- **Multi-resource TRM full** для крупных клиентов (€670K+/год — требуют network of operators)
- **Civilizational-scale initiatives** (200-year vision — один человек не унесёт)
- **Patent / IP creation** в нескольких domain'ах одновременно
- **Investment due diligence** на портфель из 30+ компаний

### Phase 3 specializations внутри community
Каждый мастер в community может специализироваться по своему направлению:
- 🤖 **AI / искусственный интеллект** — мастер по prompt engineering / agent architectures / model selection
- 🛡️ **Кибербезопасность** — мастер по security audit / penetration / compliance
- ⚖️ **Юриспруденция / законы** — мастер по contracts / regulatory / IP / GDPR
- 🔬 **Research / heavy аналитика** — мастер по market research / scientific literature / synthesis
- 💰 **Investment** — мастер по wealth management / venture / capital allocation
- 📚 **Education / методологии** — мастер по learning design / knowledge transfer
- 👥 **Talent / HR** — мастер по curated talent matching / coaching
- 🎯 **Strategy** — мастер по systemic thinking / vision / scenario planning
- 📢 **Marketing / audience** — мастер по content / community / monetization
- 💻 **Engineering / product** — мастер по building / architecting
- ... и другие domain'ы по нужде

> **Каждая специализация = свой fork Foundation с своей RUSLAN-LAYER replacement.**

### Phase 3 take rate / business model
*Подробно в §3 (TRM) и §4 (Платформа). Кратко:*
- **Take rate с обеих сторон marketplace** (Asset Owners + Resource Operators)
- **15-25% blended** (vs 35-50% у Toptal/Catalant — Jetix берёт меньше для anti-disintermediation)
- **GMV scenarios:** 100 Operators × 3 клиента = €60M GMV / €15M revenue платформы; 1000 × 3 = €600M / €150M

### Critical timing для Phase 3 trigger
> *«Все эти marketplace компании (Toptal / Catalant / Andela) потратили **5-10 лет** в Phase 1+2 прежде, чем перейти в Phase 3. Прыгнуть сразу в платформу не получалось ни у кого. Переход Jetix в Phase 3 — **не раньше 2028-2029**.»*
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§16]

---

## 2.4 Что добавляется поверх Базовой Системы (Jetix-specific станки)

> *Базовая Система имеет универсальные станки. Jetix мастерская добавляет специфические для AI-leverage / TRM / partner ecosystem контекста.*

### Jetix-specific дополнения к Foundation

#### 🏦 Top Lists Partner Factory
Specialized recruitment / curation станок — поиск партнёров через Top Lists методологию (см. memory `project_jetix_partner_factory_top_lists.md`).

#### 🎬 Producer Center
Phase 1 offering — медиа-центр для English-speaking infobiz клиентов. Отдельный workflow от стандартного TRM.

#### 📊 TRM Dashboard
Multi-resource dashboard для каждого клиента (6 ресурсов в одном view). Aggregates Foundation Part 8 visibility под TRM-specific KPIs.

#### 🤝 Mentor / Counterpart Search Pipeline
Workstream для unlock'а Phase 0 isolation as stopper class — поиск partner-in-thinking / mentor / strategist для совместной работы. Релевантно любому solo founder / mastery-track member.

#### 📚 Methodology Publishing Pipeline
Pipeline для конвертации накопленной internal methodology → publishable artifacts (Phase 2+). Каждая отработавшая методология → publishable как case study / framework / book.

#### 🪙 Token Economy Layer
Phase 2 internal / Phase 3+ public — alternative-to-IPO liquidity path. Internal utility (specialist compensation, pooled tokens) → external limited public layer. Designed safe + adequate, **explicitly не crypto-pump style**.

#### 🌐 Cross-Workshop Communication Protocol
Phase 3+ станок — стандарт communication между мастерскими в community (TRM Network platform layer). Standardized contracts / message formats / escrow / dispute resolution между мастерами.

### Что НЕ добавляется (anti-features)
- ❌ **Отдельный custom AI-product** — Jetix не делает свой AI-tool. Использует existing best-in-class через MCP integration.
- ❌ **Vendor lock-in инфраструктура** — Foundation v1.0 fork-portable, открытая архитектура.
- ❌ **Closed ecosystem без partners** — community открыта (curated, но не closed) Phase 2+.

---

## 2.5 Эволюция фаз — сводная таблица

> *3 фазы Workshop концепции в одной таблице. Cross-mapping с TRM phases — в §3.*

| Параметр | Phase 1 (текущее) | Phase 2 (2027-2029) | Phase 3 (2029+) |
|----------|-------------------|---------------------|-----------------|
| **Структура** | Один владелец + AI агенты | Команда 5-10 + AI augmentation | Community мастеров с своими мастерскими |
| **Размер мастерской** | Мега-маленькая, но мощная | Medium | Mega-system / network of workshops |
| **Trust** | Closed circle "mafia-style" | Curated team | Community с входным фильтром |
| **Ключевые triggers** | Foundation v1.0 LOCKED ✅ | First partnerships (Tseren) | Задачи > одной мастерской |
| **Capabilities** | Knowledge от лучших учителей / быстрое решение / видение целиком | + командная работа / распределение ролей | + cross-workshop coordination / mega-projects |
| **Business model** | Phase 1 consulting + producer center | TRM Phase 2 (managing 30+ клиентов) | TRM Phase 3 (двусторонняя marketplace + take rate 15-25%) |
| **Revenue** | €50K Q2 2026 → €200K validation | €1M-€20M ARR | €150M+ revenue / GMV €600M-€1B+ |
| **Timeline** | 2025-04 → 2026-Q4 | 2027-2029 | 2029+ (NOT before) |
| **Главное** | Build foundation + first ship | Scale managing capabilities | Network effects + platform leverage |

---

## 2.6 Visual / View principle в Jetix мастерской

> *Программирование с визуальным редактором — аналогия для Jetix interface к информации.*

> **Verbatim Ruslan:** *«именно система позволяет вот это посмотреть это как бы конкретно то что есть и удобно этим пользоваться, передвигать чтобы не смотреть на все свои дома всех своих людей все свои машины — ты отдельно смотришь на вот этот view который тебе дает система, и тебе это позволяет удобнее этим всем распоряжаться, использовать, мастерить.»*
> [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md:§8 quote 14]

### Two-direction visibility (refinement)
- **Internal** — для владельца / команды быстро войти в любую роль ("записывать где ты кто")
- **External** — public dashboard для accountability + transparency (anti-pyramid signal)

> **Verbatim Ruslan (audio_553):** *«сразу же надо будет сделать сайт получается как раз — смотрите можете по всем метрикам следить за компанией»*
> [src: voice-extract:§1.4.2]

**Phase 1 → 2 → 3:** internal visibility всегда; external visibility начинается с Phase 1 site → Phase 2 detailed metrics dashboard → Phase 3 platform-wide marketplace transparency.

---

## 2.7 Mafia → Community evolution mechanism

> *Critical понимание: Phase 1 закрытая mafia-style trust → Phase 3 open community.*

**Phase 1 (now):** closed circle. Свои ресурсы, своя сеть, никаких randoms.
**Phase 2:** carefully expanded. Партнёры приводятся через **personal vetting** + **track record requirements**.
**Phase 3:** community с входным фильтром (5 critical filter из ICP §7) + reputation system + curated access.

**Это не противоречие.** Это **поэтапное открытие** по мере того как:
1. Foundation становится stable (28.04.2026 ✓)
2. Methodology становится publishable
3. Track record накапливается (€50K → €200K → €1M validation)
4. Защита от disintermediation встроена (7 layers — см. §4.6)

> Преждевременное открытие = scam-like attraction (плохие участники) + dilution качества. Поэтапное = sustainable growth с сохранением quality bar.

---

## 2.8 Какая мастерская у каждого мастера в Phase 3 (illustrative examples)

> *Чтобы было понятно — Phase 3 community будет состоять из specialized мастерских.*

| Мастер | Его мастерская | Что делает в Jetix community |
|--------|---------------|------------------------------|
| 🤖 AI specialist | Foundation + AI tools focus | Внедряет latest AI tools для клиентов platform |
| 🛡️ Cybersec expert | Foundation + security audit станки | Делает security review для всех TRM-клиентов |
| ⚖️ Legal advisor | Foundation + legal templates / contracts | Управляет contract layer для TRM agreements |
| 🔬 Research lead | Foundation + heavy analytics | Делает deep research проекты по запросу |
| 💰 Wealth manager | Foundation + investment tooling | Управляет финансовым ресурсом TRM |
| 🎯 Strategy advisor | Foundation + scenario planning | Помогает clients с strategic decisions |
| 📚 Education designer | Foundation + curriculum tools | Делает educational artifacts из накопленной methodology |
| 📢 Audience operator | Foundation + content / monetization | Управляет audience-ресурсом TRM |
| 💻 Engineering lead | Foundation + dev tooling | Делает custom builds для клиентов |
| 👥 Talent operator | Foundation + curated matching | Управляет team-ресурсом TRM + recruitment |

> **Каждый мастер = эксперт в своём direction.** Jetix как мета-мастерская = их **collective intelligence** через shared infrastructure.

---

# 3. 🏦 TRM — Total Resource Management

> **Цель раздела:** описать центральное коммерческое предложение Jetix — Total Resource Management. **Не одна услуга, а архитектурно новая категория** того что значит «консалтинг» в эпоху AI-агентов.
>
> **База:** `decisions/JETIX-TRM-MODEL-2026-04-30.md` (LOCKED 30.04).

---

## 3.1 Что такое TRM — главный тезис

### Проблема классических управляющих фондов
Классические управляющие компании (BlackRock, Bridgewater, family offices, McKinsey) управляют **только одним типом ресурса** — деньгами или временем или знаниями. У каждого предпринимателя / компании есть **минимум 6 типов** исчерпаемых, монетизируемых ресурсов — но **никто не управляет ими комплексно** и под одним договором.

> *«Никто не отдаст незнакомцу 6 ресурсов сразу. Это белое пятно. Если Jetix туда зайдёт — это новая категория.»*  
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§3.7]

### Что делает Jetix
**Jetix управляет всеми 6 ресурсами одновременно.** Берёт **management fee + performance fee** с каждого. Это превращает консалтинговую модель (продажа часов / отчётов) в **управляющую компанию нового типа** — Total Resource Management (TRM).

### Главная фраза
> **«Jetix не консультирует ваш бизнес. Jetix управляет вашими ресурсами — и делит с вами прирост прибыли.»**

> *Note: Original TRM-MODEL §18 был «Mittelstand-ресурсами» — agnostic переформулировка для domain-independent позиционирования.*

### Главный инсайт
> *«Идея TRM — это не «новый продукт» Jetix. Это **переопределение того, что значит "консалтинг"** в эпоху AI-агентов. Это превращает консалтинг из service business (продажа часов) в asset management business (продажа результата от управляемых активов).»*  
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§9]

---

## 3.2 6 ресурсов TRM — детально

> Каждый ресурс **исчерпаемый, монетизируемый, измеримый**. У каждого свой существующий рынок управления. Jetix объединяет все 6 под одной крышей.

### 1. 💰 Финансы (capital)

**Что значит:** кэш на счетах, инвестиции, рабочий капитал, runway, cashflow.

**Что Jetix делает:**
- Cash management & бюджетирование
- Investment portfolio review (advisory без BaFin license; full management — Phase 3+ с лицензией)
- Cashflow optimization
- Runway projection & scenario modeling

**Аналоги рынка:** Wealth Management (BlackRock, UBS Wealth, Bridgewater) — модель **AUM 0.5-2% + 10-20% performance**.

**Регуляторные ограничения:** BaFin licensing required для full asset management в Phase 3+.

---

### 2. ⏱️ Время CEO/основателя (founder time)

**Что значит:** часы внимания первого лица — **самый дефицитный ресурс**.

**Что Jetix делает:**
- Fractional COO/Integrator pattern
- Освобождение CEO от operational tasks для vision-задач
- Decision routing (что должно дойти до CEO, что не должно)
- Calendar / focus optimization
- AI Chief of Staff role

**Аналоги рынка:** Fractional COO (ScaleUpExec), EOS Integrators (EOS Worldwide — 257K компаний на EOS), Chief of Staff agencies.

**Pricing reference:** Retainer **$5-25k/мес + equity**.

---

### 3. 📢 Аудитория (audience)

**Что значит:** подписчики, контакты, рассылки, репутационный капитал, social media presence, community.

**Что Jetix делает:**
- Content / monetization strategy
- LinkedIn / newsletters / podcast management
- Audience growth + engagement
- Конверсия attention → revenue (sponsored, products, partnerships)

**Аналоги рынка:** Talent / Creator Management Agencies (WME, CAA, UTA, Night Media, Jellysmack, Whalar) — модель **15-25% revenue share**.

---

### 4. 📚 Информация / знания (knowledge)

**Что значит:** внутренние данные компании, экспертиза, накопленные методологии, tribal knowledge, IP.

**Что Jetix делает:**
- Knowledge ops: построение и ведение KB
- Оцифровка tribal knowledge (превращение неявного в явный)
- Methodology library (что работает / не работает по конкретному случаю)
- Research delivery on demand

**Аналоги рынка:** Knowledge Management consulting + Holistic Wealth (extended) — Mercer, Deloitte HC. **Зазор → открытое окно для Jetix** — никто не делает это специализированно как product.

---

### 5. 💻 Вычислительные мощности (compute)

**Что значит:** GPU/CPU, AI-инференс, токены, серверная инфраструктура, AI subscriptions.

**Что Jetix делает:**
- Управление AI-budget клиента
- Brokerage между LLM providers (Anthropic / OpenAI / local)
- Cost optimization (когда какой model)
- Infrastructure планирование

**Аналоги рынка:** AI Compute Brokers / GPUaaS (Together AI, Anyscale, RunPod, Lambda Labs) — **маржа 15-30%**.

---

### 6. 🤝 Команда / человеческий капитал (talent)

**Что значит:** сотрудники, их время, их компетенции, ключевые роли.

**Что Jetix делает:**
- Curated talent matching (через сеть мастеров и партнёров)
- Fractional executives (CMO / CHRO / CTO)
- Performance management
- Onboarding / training через Jetix methodology

**Аналоги рынка:** Talent / HR Outsourcing, Fractional Executives (Toptal, Andela, ADP, Mercer, Deloitte) — **15-30% от ФОТ либо markup**.

---

### Сводка 6 ресурсов

| # | Ресурс | Аналоги рынка | Pricing reference | Status в Jetix Phase 1 |
|---|--------|--------------|-------------------|------------------------|
| 1 | 💰 Финансы | Wealth Mgmt, Family Offices | AUM 0.5-2% + 10-20% perf | Advisory (Phase 3+ с BaFin license — full mgmt) |
| 2 | ⏱️ Время CEO | Fractional COO, EOS Integrator | $5-25k/мес + equity | ✅ доступно Phase 1 (€8k/мес) |
| 3 | 📢 Аудитория | Talent / Creator Agencies (WME, CAA) | 15-25% revenue share | ✅ доступно Phase 1 (15% от monetization) |
| 4 | 📚 Информация | KM + Holistic Wealth | Часть holistic financial planning | ✅ доступно Phase 1 (€36k/год retainer) |
| 5 | 💻 Compute | AI Compute Brokers, GPUaaS | Маржа 15-30% | ✅ доступно Phase 1 (15% margin на €180k/год) |
| 6 | 🤝 Команда | Talent / HR Outsourcing | 15-30% ФОТ | ✅ доступно Phase 1 (€60k/год retainer) |

> **Ни одна компания не делает всё одновременно.** Это **белое пятно** — синтетическая комбинация имеет шанс быть рабочей. Jetix — **первый, кто целит в белое пятно**.

---

## 3.3 Почему TRM работает именно сейчас (3 волны)

### Волна 1 — AI-агенты как операционный слой
Раньше управлять временем 10 CEO одновременно было **физически невозможно** — у одного человека 24 часа в сутки. **AI-агенты** позволяют одному управляющему **+ флоту агентов** параллельно держать в голове состояние десятков клиентов. **Compute стал ресурсом**, который масштабируется — и сам становится продуктом.

### Волна 2 — Бизнес перегружен AI / digital трансформацией
Средние предприятия (любой страны / индустрии) **завалены**:
- AI-внедрением (что выбирать / как использовать)
- Регуляторикой (EU AI Act / GDPR / etc.)
- Talent shortage (где брать AI-grade talent)
- Succession проблемами (next-gen leadership)
- Цифровизацией (legacy → modern stack)

**Им нужен не консультант (который даст отчёт и уйдёт). Им нужен operator** который встанет рядом и реально сделает. **TRM — это offering operator-уровня.**

### Волна 3 — Падающее доверие к классическому консалтингу
Big 4 (McKinsey, BCG, Bain, Deloitte) **продают слайды** + почасовку. Клиенты всё чаще требуют:
- **Skin-in-the-game** консультанта (не fixed fee регardless of результата)
- **Performance-based** модели
- **Реальное участие** в делах, не просто рекомендации

**TRM — финальная форма этого тренда:** «мы не просто внедряем — мы **управляем твоими ресурсами и делим прибыль**».

> *Совпадение всех 3 волн = **окно для new category**. Jetix входит первым.*

---

## 3.4 Бизнес-модель — Mgmt fee + Performance fee

### Структура fees (двойная)

#### A. Management fee (плата за управление, идёт независимо от результата)
- **Финансы:** 0.5-1% годовых от размера ресурса под управлением
- **Время CEO:** $X тыс./мес фиксированно (fractional COO model)
- **Аудитория:** 10-15% от monetization revenue
- **Знания / Compute / Команда:** retainer + per-resource markup

#### B. Performance fee (плата за результат, % от прироста прибыли)
- **15-25% от incremental profit**
- Считается **по сравнению с baseline** (доход клиента до начала управления, индексированный на рост рынка)
- **Только за рост, который вне market trend** (clean alpha)

### Пример расчёта на одном клиенте (TRM-full)

> *Иллюстративный пример на условном клиенте €50M revenue, EBITDA €5M.*

**Jetix берёт под управление:** €5M AUM (финансы), 8h/нед (время CEO), 12k+3k подписчиков (аудитория), вся внутренняя база, €15k/мес AI-инфра, 3 ключевых человека.

| Уровень | Ресурс | Логика | Сумма |
|---------|--------|--------|-------|
| Mgmt | Финансы €5M × 0.75% | стандарт wealth mgmt | €37.5k |
| Mgmt | Время CEO (fractional COO) | €8k × 12 мес | €96k |
| Mgmt | Аудитория | 15% от monetization | €15k |
| Mgmt | Информация | retainer | €36k |
| Mgmt | Compute | 15% маржа на €180k/год | €27k |
| Mgmt | Команда | retainer | €60k |
| **Σ mgmt fee** | | | **€271.5k/год** |
| Performance | 20% от incremental EBITDA (€5M→€7M = +€2M) | | **€400k** |
| **Σ с клиента** | | | **~€670k/год** |

**Comparison vs traditional consulting:** один TRM-full клиент = эквивалент **5-6 классических консалтинговых проектов**.

### Масштабирование
- **10 клиентов TRM** = €5-7M ARR
- **30 клиентов TRM** = €15-20M ARR (территория «AI consulting unicorn»)
- **Recurring revenue + scale с ростом клиента** (а не Jetix) → valuation мультипликатор:
  - 1-3× revenue (классический консалтинг)
  - 5-10× revenue (asset management)
  - 10-20× revenue (платформа)

---

## 3.5 ⭐ Land-and-Expand — Лестница 6 уровней (€3K → €40-60K/мес)

### Главный sales motion
> *«Jetix НЕ продаёт TRM-full. Jetix продаёт **гипотезу за €3k**, а потом **доращивает клиента до TRM** органически.»*  
> [src: decisions/JETIX-TRM-MODEL-2026-04-30.md:§11.4]

**Логика:** никто не отдаст 6 ресурсов незнакомцу сразу. Поэтому Jetix заходит **снизу** — с маленьких задач / гипотез / частей ресурсов, на которых клиент **мало рискует**. По мере того как trust строится — extends to deeper management.

### 6 уровней лестницы

| Уровень | Что | Цена | Условия |
|---------|-----|------|---------|
| **L0** — AI-разведчик (Reconnaissance) | Одна гипотеза / исследование / аналитическая записка | **€1.5-5k/задача** | 1-2 недели |
| **L1** — AI-аналитический отдел (Outsourced Brain) | «Команда из 3 аналитиков, которые держат твои интересы» | **€3-10k/мес** ретейнер | min 6 мес |
| **L2** — Менеджер одного ресурса | Один из 6 ресурсов под управлением (часто аудитория или информация) | **€5-15k/мес** mgmt + 20% performance | min 12 мес |
| **L3** — AI Chief of Staff | «Правая рука» CEO — фильтрует информацию, готовит решения | **€10-25k/мес** | trust-deep relationship |
| **L4** — Партнёр по гипотезам / Venture Operator | Открытие нового бизнеса/направления; revenue share или fee + small equity | **€15-30k/мес** или equity | новые ventures |
| **L5** — TRM-full | Все 6 ресурсов под управлением, deep integration | **€30-60k/мес** mgmt + 20-25% performance | Только для прошедших L1-L4 |

### Реалистичная воронка одного клиента

| Месяц | Уровень | MRR | Что происходит |
|-------|---------|-----|----------------|
| M0 | — | €3k one-time | L0 первая гипотеза |
| M1-3 | L1 | €5k/мес | L1 retainer кикает |
| M6 | L2 | €10k/мес | Один ресурс взят |
| M12 | L3 | €18k/мес | Chief of Staff role |
| M18 | L4 | €25k/мес | Venture partnership |
| **M24** | **L5** | **€40k MRR** | **TRM-full** = €480k ARR |

**От €3k разовой задачи (M0) до €480k/год (M24)** — за 24 месяца.

### Почему лестница работает (психологически)
1. **Низкий start barrier** — €3k = test investment, риск минимальный
2. **Накопление trust** — каждый уровень доказывает Jetix-компетенцию
3. **Постепенное углубление** — клиент привыкает делегировать больше
4. **Ratchet effect** — после L2-L3 откатиться обратно сложно (deep integration)
5. **Performance-driven** — каждый level увеличивает percentage performance fee

---

## 3.6 Варианты реализации TRM (от простого к сложному)

> *Можно строить TRM не сразу как full-resource management. Есть несколько incremental paths.*

| Вариант | Description | Срок | Условия |
|---------|-------------|------|---------|
| **A — TRM-lite (2 ресурса)** | Финансы + время CEO. «Family office for AI-driven CEOs». Низкий регуляторный барьер. | 6-12 мес | 2-3 клиента |
| **B — TRM-3** | Финансы + время + информация. «AI Chief of Staff as a Service». | 12-18 мес | Близко к Jetix HQ |
| **C — TRM-full** | Все 6 ресурсов. Требует команды 30-50 чел, лицензии BaFin (для финансов). | 3-5 лет | Полная модель |
| **D — TRM Alliance** ⭐ | Альянс-модель. Jetix управляет общей AI-инфраструктурой и знанием для 5-10 клиентов **одновременно**. **Самый быстрый путь к scale.** | 12-18 мес | Curated polygon |

> **Variant D (TRM Alliance) — fastest path к meaningful revenue Phase 2.** 5-10 клиентов в альянсе делят инфраструктуру, Jetix управляет общими ресурсами + специфичными per-client. Lower acquisition cost, higher retention через peer network effects.

---

## 3.7 AI Brain on Demand — выделенный L0-L1 product

### Концепция
**Jetix как внешний мозг клиента** — для разбора одного вопроса полностью.

### Экономика
- **Себестоимость одной гипотезы:** ~$50-200 в compute + 2-4ч человеческого времени
- **Цена клиенту:** €1500-5000
- **Маржа:** **70-90%**

### Зазор позиционирования
**Между двумя крайностями:**
- 🔴 Дешёвый AI без контекста (Perplexity Pro €20) — нет глубины, нет привязки к контексту клиента
- 🔴 Дорогой консалтинг без скорости (McKinsey €50-150k за 6-12 нед) — слишком медленно, слишком дорого

**Jetix AI Brain:** глубокий синтез + быстро + 10-30× дешевле.

### Варианты pricing
1. **Per-question** (€1500-5000 за гипотезу) — низкий барьер, транзакционные отношения
2. **Subscription** («10 гипотез/мес за €5k») — recurring revenue
3. **Personal Analytics Department** (€8-15k/мес unlimited) — high-value enterprise

---

## 3.8 Архитектура TRM — каждый ресурс = отдельный модуль (мини-фонд)

```
┌──────────────────────────────────────────────────────────┐
│ JETIX TRM PLATFORM (core)                                 │
│ Единая аналитика, dashboard, отчёты, billing             │
└──────────┬───────────────────────────────────────────────┘
           ↓
┌──────────────────────────────────────────────────────────┐
│ 6 МИНИ-ФОНДОВ (по одному на ресурс)                       │
│  💰 Fin fund   ⏱ Time fund   📢 Aud fund                 │
│  📚 Info fund  💻 Compute fund  🤝 Team fund              │
└──────────┬───────────────────────────────────────────────┘
           ↓
┌──────────────────────────────────────────────────────────┐
│ JETIX OS (12 agents, 6 departments)                       │
│ Operations, Sales, Growth, Support, Leadership, Brain    │
└──────────────────────────────────────────────────────────┘
```

> **Каждый из 6 mini-fund'ов** имеет своего operator (Phase 3 platform — внешний specialist; Phase 1-2 — внутренняя команда + AI агенты). Все стандартизированы через Jetix OS — единая аналитика, billing, reporting.

---

## 3.9 Риски TRM + Mitigations

> *6 главных рисков с конкретными mitigation стратегиями.*

### 1. Регуляторика (BaFin licensure / KAGB / WpHG)
- **Risk:** €730k+ капитальные требования для Asset Management license
- **Mitigation:** cash flow management + advisory only Phase 1, license горизонт 3-5 лет

### 2. Конфликт интересов (10 клиентов, конкуренты)
- **Risk:** insider trading-like risks при cross-client information
- **Mitigation:** non-compete sectoring (1 клиент на отрасль), Chinese walls между Jetix-операторами

### 3. Концентрационный риск (€670k/клиент × 5 = -20% на потерю одного)
- **Risk:** потеря 1-2 клиентов = большой revenue drop в early Phase
- **Mitigation:** долгосрочные контракты 3-5 лет, deeply integrated AI-ops (high switching cost для клиента)

### 4. Доверие (никто не отдаст незнакомцу 6 ресурсов сразу)
- **Risk:** structural — TRM требует deep integration, integration требует track record
- **Mitigation:** **Land-and-Expand лестница** (см. §3.5) — поэтапный onboarding (1 ресурс / 6 мес → расширение)

### 5. Operational complexity (6 несвязанных доменов)
- **Risk:** team needs expertise в финансах + time mgmt + audience + knowledge + compute + HR
- **Mitigation:** **AI-агенты как множитель компетенций** + специализированные операторы Phase 3

### 6. Юридическая структура (договор управления 6 ресурсами одновременно)
- **Risk:** unprecedented contract type — нет templates
- **Mitigation:** чёткие KPI на старте, baseline measurement, neutral arbitration, поэтапное расширение

---

## 3.10 TRM vs Классический консалтинг — сравнительная таблица

| Аспект | Классический консалтинг (Big 4) | TRM (Jetix) |
|--------|--------------------------------|-------------|
| **Что покупает клиент** | Рекомендации, отчёты, presentations | **Управление ресурсами + результат** |
| **Кто несёт ответственность за результат** | Клиент | **Jetix** (через performance fee) |
| **Модель оплаты** | Fixed fee / hourly | **Mgmt fee + performance fee** |
| **Зависимость выручки от успеха клиента** | Минимальная | **Высокая** (растёт с ростом клиента) |
| **Скейл бизнеса** | Линейный (нанимаешь людей) | **Экспоненциальный** (через AI-агентов) |
| **Valuation мультипликатор** | 1-3× revenue | **5-20× revenue** |
| **Барьер на выход клиента** | Низкий (закончил проект — ушёл) | **Очень высокий** (deep integration, switching cost) |
| **Время до результата** | 3-6 мес проект | 6-24 мес до peak L5 |
| **Skin-in-the-game** | Минимальный | **Существенный** (performance fee) |

---

## 3.11 Phase Evolution TRM (3 фазы бизнеса)

> *Cross-mapping с Workshop фазами из §2.*

### Phase 1 — Сервисная компания (2026-2027)
- **Бизнес:** Jetix управляет ресурсами клиентов сам (через Ruslan + AI агенты + первые партнёры)
- **Кто работает:** Ruslan + 1-3 ключевых партнёра + AI агенты
- **Доход:** Mgmt fee + performance fee
- **Скейл:** Линейный (limited по capacity)
- **Цель:** **€50K Q2 2026 → €200K validation → €1M ARR**

### Phase 2 — Управляющая компания (2027-2029)
- **Бизнес:** Jetix управляет 30+ клиентами **через AI-агентов**
- **Кто работает:** Команда 30-50 + флот AI агентов
- **Доход:** Тот же model, кратно больше клиентов
- **Скейл:** Сублинейный (агенты дают рычаг — каждый человек обслуживает 5-10 клиентов вместо 1-2)
- **Цель:** **€5-20M ARR**

### Phase 3 — Платформа TRM Network (2029+)
- **Бизнес:** Jetix **сводит сторонних управляющих** с клиентами (двусторонний marketplace)
- **Кто работает:** Платформа + рамочный персонал + сеть Operators
- **Доход:** **Take rate 15-25%** с обеих сторон (Asset Owners + Resource Operators)
- **Скейл:** **Экспоненциальный** (network effects)
- **Цель:** **€150M+ revenue / GMV €600M-1B+**

> Подробно про Phase 3 платформу + chicken-and-egg solution + 7 layers anti-disintermediation — в **§4 Платформа для проектов**.

---

## 3.12 Уникальная конкурентная позиция Jetix TRM (3 структурных преимущества)

### 1. Resource multidimensionality
Все остальные marketplace'ы / management компании матчат **один тип отношений** (заказчик ⇄ фрилансер; investor ⇄ deals; talent ⇄ hire). **Jetix матчит 6 типов ресурсов одновременно** — это уникальный сетевой эффект.

### 2. AI-native infrastructure с Day 1
Toptal / Catalant / Andela спроектированы для 2010-х (pre-LLM era). **Jetix HQ изначально AI-native** — на одно поколение технологий впереди. Каждая operation использует AI-leverage by design, не bolted on.

### 3. Cross-resource synergy для клиента
**Один клиент имеет 6 операторов внутри Jetix.** Все обмениваются контекстом через платформу. Уход одного оператора = потеря синергии (клиент его потеряет первым). **Это специфическое преимущество TRM-структуры** — отсутствует у Toptal/Catalant.

---

## 3.X Сводка TRM

| Аспект | Кратко |
|--------|--------|
| **Что это** | Total Resource Management — управление 6 ресурсами клиента под одним договором |
| **6 ресурсов** | 💰 Финансы / ⏱️ Время CEO / 📢 Аудитория / 📚 Знания / 💻 Compute / 🤝 Команда |
| **Бизнес-модель** | Mgmt fee + Performance fee |
| **Sales motion** | Land-and-Expand лестница 6 уровней (€3k → €40-60k/мес) |
| **TRM-full клиент** | ~€670k/год = эквивалент 5-6 traditional консалтинг проектов |
| **Архитектура** | Platform core + 6 mini-funds + Jetix OS (12 agents) |
| **3 волны почему сейчас** | AI-агенты / business overload / падение доверия консалтингу |
| **Конкурентное преимущество** | Resource multidimensionality + AI-native + Cross-resource synergy |
| **Phase 1 path** | TRM Alliance (вариант D) — самый быстрый путь к scale |
| **Risk Top-1** | Trust gap → mitigated through L0-L5 ladder |

> **Главный вывод:** TRM — это не «ещё один продукт». Это **архитектурное переопределение того, что значит управление бизнесом** в эпоху AI-агентов.

---

# 4. 🌐 Платформа для проектов — partners ecosystem (Phase 2-3)

> **Цель раздела:** описать центральное Phase 2-3 видение Jetix — **платформу на которой собираются мастера, исполнители, инвесторы и совместно решают всё более сложные / амбициозные проекты**. Это эволюция от service company (Phase 1) → managing company (Phase 2) → **двусторонняя платформа** (Phase 3).
>
> **База:** `decisions/JETIX-TRM-MODEL-2026-04-30.md` §14-§17 + Workshop concept §6 Phase 3 + wiki/concepts.

---

## 4.1 Зачем нужна платформа — главная мотивация

### Главная боль которую платформа решает
Любой амбициозный человек / партнёр / профессионал имеет одну и ту же проблему: **время утекает в рутину и поиск, а не в реальную работу**.

Конкретно:
- 🕒 **Недели тратятся на поиск нужных людей** (исполнителей / экспертов / инвесторов)
- 🕒 Потом ещё недели — на вётинг кого взять / кому доверять
- 🕒 В итоге часто берут **«таких себе людей»** — потому что кончилось терпение / время
- 🕒 А потом **месяцы** — на coordination / коммуникацию / explaining контекста
- 🔥 **Реальная важная работа — остаётся в остатке** (вечерами / выходными / "когда-нибудь потом")

### Что платформа делает
**Платформа Jetix решает эту проблему system-level:**

1. **Автоматизирует рутину** — поиск / вётинг / first contact / coordination → **освобождает время** для глубокой работы
2. **Курирует доступ к реально крутым людям** — не все подряд, а **уже отобранные** через 5 critical filter (см. §7) и track record
3. **Создаёт общий язык** — все участники говорят в одних терминах (Foundation v1.0 grammar) → нет потерь на translation
4. **Стандартизирует workflows** — типовые процессы для типовых задач (proposals / contracts / payments / disputes)
5. **Накапливает knowledge для всех** — каждый проект делает базу всех участников богаче

> **Главная ценность для партнёра:**  
> *«Вместо 70% времени на administrative / search / coordination — 70% времени на important / strategic / creative.»*

### Почему это критично именно сейчас
**Все более сложные / амбициозные проекты** требуют:
- Cross-domain expertise (один человек не может быть экспертом в AI + cybersec + legal + research одновременно)
- Multi-resource management (см. TRM §3 — 6 ресурсов сразу)
- Speed of iteration (AI-era — циклы ускорились 5-10×)

**Один человек или маленькая команда — не справляется.** Нужна **сеть curated профессионалов** с общей инфраструктурой.

---

## 4.2 Что платформа конкретно делает — 5 функций

### 1. 🔧 Управление проектами (cross-participants)
- Каждый проект имеет project journal / state / dependencies / deliverables (Foundation Part 7)
- Все участники видят **одну картину** проекта (Visual / View principle)
- Standard project lifecycle: ideation → scoping → execution → delivery → retro → archive

### 2. 💎 Управление общими ресурсами
- 6 ресурсов TRM (см. §3) — но теперь не одного клиента, а **между участниками платформы**
- Финансы — escrow, billing, automated payouts
- Время — calendar coordination, capacity planning
- Audience — cross-promotion mechanisms
- Knowledge — shared wiki, methodology library
- Compute — shared infrastructure / discounts on tools
- Команда — pool of vetted operators

### 3. 🎭 Роли — каждый может быть в разных
На платформе **один и тот же человек** может играть **разные роли** в разных проектах:
- **Управляющий** одного проекта (driver, decision maker)
- **Исполнитель** другого (specialized contribution)
- **Investor** третьего (capital + advisory)
- **Researcher** четвёртого (deep dive)
- **Mentor / Critic** пятого (review + feedback)

> Это — **mastery в действии**: проф мастер не зацикливается на одной роли, переключается под задачу.

### 4. 🧪 Тестирование гипотез
- Гипотезы (стратегические / продуктовые / market) **тестируются на платформе** через:
  - Quick experiments (€3k AI Brain on Demand формат — см. §3.7)
  - Pilot projects с курируемыми участниками
  - A/B tests across multiple projects
  - Cross-pollination знаний между проектами
- Результаты **накапливаются** в общую methodology library

### 5. 🏛️ Общий язык / standard
- Все участники работают в **Foundation v1.0 grammar** (или совместимом fork)
- Общие conventions (даты / naming / tags / statuses)
- Стандартные форматы (proposals / SOWs / contracts / reports)
- **Translation cost → 0** между участниками

---

## 4.3 4 источника проектов на платформе

> *Это критическая особенность — платформа не просто marketplace. У неё 4 источника входящих проектов. **Источник 4 особенно важен** — это участники Jetix создают свои проекты и сами привлекают клиентов извне.*

### 🏠 Источник 1 — Внутренние Jetix-проекты
- Развитие самой Jetix (Foundation evolution / станки / methodology)
- Internal R&D
- Phase 2-3 transitions
- **Где:** свои проекты, для своих целей; партнёры участвуют либо как owners, либо за compensation

### 🏢 Источник 2 — Проекты Jetix-клиентов (TRM-driven)
- Когда Jetix управляет ресурсами клиента (TRM, см. §3) — у этого клиента возникают **под-проекты**
- Эти под-проекты могут требовать специализированных Operators / экспертов
- Jetix **разбивает** клиентский проект на parts → распределяет между участниками платформы → координирует
- **Кто платит:** клиент Jetix; Jetix берёт margin; участники получают свою долю

### 🌍 Источник 3 — Проекты извне (External Owners)
- **Внешние клиенты / организации** приходят на платформу с проектом
- «У меня есть проект X — нужны такие-то ресурсы / экспертиза. Сделайте.»
- Платформа: подбирает участников + структурирует workflow + курирует execution
- **Кто платит:** external owner; Jetix take rate с обеих сторон (см. §4.5)

### 👤 Источник 4 — Проекты создаваемые внутренними участниками Jetix ⭐

> *Это **отдельный, критически важный источник**. Партнёры / фрилансеры / полу-фрилансеры / свободные мастера, **уже находящиеся внутри Jetix**, могут запускать свои собственные проекты на платформе и сами привлекать клиентов извне.*

#### Как работает
1. **Участник Jetix** (партнёр / фрилансер / свободный мастер) использует платформу как **infrastructure для своего бизнеса**
2. Создаёт **свой проект** на платформе (например: «улучшение operations для X-индустрии бизнеса»)
3. **Сам идёт во внешнюю среду** и привлекает потенциальных клиентов / партнёров (это **не** Jetix их приводит — а сам участник)
4. Jetix даёт участнику **infrastructure для исполнения**:
   - Возможность **собрать команду** через платформу (другие Operators под нужные роли)
   - Доступ к **общим ресурсам** (AI инструменты / методологии / wiki / станки)
   - **Удобные workflow templates** + escrow + billing + dispute resolution
   - **Brand association** Jetix (доверие к участнику ↑)

#### Почему это отдельный источник
**Разница с Источниками 1-3:**
- В Источниках 2-3 — **Jetix приводит клиента** на платформу
- В Источнике 4 — **участник сам приводит клиента**, Jetix только обеспечивает infrastructure

#### Кому подходит этот формат
- Solo консультант / coach — у него уже есть свой outreach / sales
- Полу-фрилансер с собственной нишей и специализацией
- Свободный мастер которому нужна команда под конкретный проект, но не хочет нанимать
- Партнёр-foundеr со своим стартапом — использует Jetix infrastructure для execution
- Любой кто хочет **«внешнее развитие»** через свои каналы, но с Jetix-leverage

#### Бизнес-модель этого источника (компенсация Jetix)

**2 варианта (могут комбинироваться):**

**Вариант A — Revenue share с проекта**
- Jetix получает **% от прибыли проекта** (5-15%, зависит от deep integration)
- Участник: основная прибыль остаётся у него, Jetix — часть за infrastructure

**Вариант B — Infrastructure usage fee**
- Jetix получает **% за пользование наработками** (общие AI инструменты / методологии / станки / brand)
- Это **более фиксированная модель** — не зависит от прибыли проекта
- Может быть retainer-style («€500-2000/мес за access to Jetix infrastructure») или per-project markup

> **На практике обычно гибрид** — небольшой infrastructure fee + revenue share с проекта. Это **align'ит интересы** Jetix с успехом участника.

#### Главная ценность для участника
- **Не надо строить infrastructure с нуля** (saved 6-12 мес setup time)
- **Доступ к talent pool** для команды (не недели на recruitment)
- **Brand & credibility** через association с Jetix
- **Compound learning** — каждый твой проект делает других участников Jetix умнее (и наоборот)

#### Главная ценность для Jetix
- **Расширение deal flow** через внешние outreach каналы участников
- **Diversification of revenue** — не зависит только от Jetix-driven sales
- **Network growth** — каждый участник приводит свою сеть
- **Methodology validation** — больше реальных кейсов = больше проверки наработок

---

> **Главная фишка:** участники платформы **получают доступ к проектам всех 4 источников** одновременно. Это **существенно больше deal flow** + **больше форматов вовлечения** чем у solo professional.

### Сводная таблица источников

| # | Источник | Кто приводит клиента | Кто платит Jetix | Главная ценность для участника |
|---|----------|---------------------|------------------|-------------------------------|
| 1 | Внутренние Jetix-проекты | Jetix (это сам Jetix) | Jetix (compensation) | Working on system development |
| 2 | TRM-driven (клиенты Jetix) | Jetix через TRM | Клиент → Jetix → участник доля | Steady deal flow |
| 3 | External Owners | Внешний клиент → платформа | Клиент → Jetix take rate | Volume через marketplace |
| 4 | **Самостоятельный участник** ⭐ | **Сам участник** | Участник (revenue share / infra fee) | **Свой бизнес + Jetix leverage** |

---

## 4.4 Какие проекты партнёры могут делать — уровни сложности

> *Логика уровней — от простого (низкий риск, малая команда) до сложного (высокий impact, multi-domain).*

### Level 1 — Single-resource задача
- **Что:** один Operator решает локальную задачу для клиента
- **Пример:** «нужен audit security для SaaS компании»
- **Длительность:** 1-4 недели
- **Размер команды:** 1-2 человека
- **Цена:** €5-30k

### Level 2 — Multi-step проект одного направления
- **Что:** один Operator + 1-2 поддерживающих, сложный workflow
- **Пример:** «полный AI-внедрение в operations Mid-size компании»
- **Длительность:** 2-6 месяцев
- **Размер команды:** 2-5 человек
- **Цена:** €30-150k

### Level 3 — Cross-domain проект
- **Что:** требует одновременно нескольких specializations
- **Пример:** «complete digital transformation Mittelstand клиента — AI + cybersec + legal + change management»
- **Длительность:** 6-18 месяцев
- **Размер команды:** 5-15 человек
- **Цена:** €150-500k

### Level 4 — TRM-full клиент
- **Что:** полное Total Resource Management (см. §3)
- **Пример:** клиент €670k/год по TRM-full модели
- **Длительность:** 2-5+ лет
- **Размер команды:** 10-30 человек (через платформу)
- **Цена:** €500k-3M+

### Level 5 — Mega-проекты Phase 3 community
- **Что:** проекты которые ОДНОЙ мастерской не под силу (см. Workshop §2.3)
- **Пример:** patent + IP creation в нескольких domain'ах / cross-region market entry / civilizational-scale initiative
- **Длительность:** 1-5 лет
- **Размер команды:** 30-100+ через сеть мастеров с мастерскими
- **Цена:** €1M-50M+

> **Каждый партнёр** может работать на нескольких уровнях одновременно — driver одного Level 2 проекта + исполнитель Level 4 в роли своего specialty.

---

## 4.5 Бизнес-модель платформы — Take rate с обеих сторон

### Структура fees (двусторонний marketplace)

| Источник | Размер | Логика |
|----------|--------|--------|
| **С Operator (партнёра)** | **15-20%** от его revenue с проекта | Платит за лиды, vetting, infra, brand, billing, dispute resolution |
| **С Asset Owner (клиента)** | €1-5k/мес или **5%** от mgmt fee | Платит за curation, dispute resolution, AI tools, escrow |
| **С performance fee** | **10-15% override** | Платит за то, что платформа повышает шанс успеха через synergy |
| **С compute markup** | **20-30% наценка** | Своя добавленная стоимость on AI infrastructure |

### Пример экономики платформы (Phase 3 mature scenario)

#### Сценарий 1: 100 Operators × 3 клиента = 300 контрактов
- Средний контракт: **€200k/год** → GMV **€60M/год**
- Take rate ~25% blended → **€15M/год revenue платформы**
- Маржа 50-70% → **€7.5-10.5M EBITDA**

#### Сценарий 2: 1000 Operators × 3 клиента = 3000 контрактов
- GMV: **€600M/год**
- Revenue платформы: **€150M/год**
- Валуация: **€1.5-3 млрд** (10-20× revenue marketplace мультипликатор)

> **Это и есть $1T trajectory point** — Phase 3 платформа генерит revenue экспоненциально с network effects.

---

## 4.6 ⭐ 7 слоёв защиты от disintermediation (главная угроза marketplace)

> *Главная угроза любого marketplace: Operator находит на платформе клиента → отрабатывает 3 месяца → договаривается работать напрямую — мимо платформы. Все довольны кроме Jetix.*

> *Чем выше take rate и чем дороже одна сделка — тем сильнее стимул дисинтермедиироваться. **TRM с €200k+ контрактами — самая уязвимая категория.***

### Layer 1 — Инфраструктурный lock-in
**Jetix HQ / OS как операционная платформа.** Уйдя с платформы, Operator теряет:
- Foundation v1.0 infrastructure
- AI агенты + tools (12 ролей готовых)
- Workflow templates / станки
- Накопленную knowledge базу

> **Ушёл = вернулся к ручной работе.** Это уже сильный barrier.

### Layer 2 — Шаринг clients = шаринг рисков
- **Escrow платежей** — клиент платит на платформу, не Operator'у напрямую
- **Юридический контракт** — платформа гарантирует клиенту качество
- **Страховка ответственности** — покрытие через платформу
- **Dispute resolution** — neutral arbitration через Jetix

> Уход с платформы = клиент теряет защиту = клиент **сам не захочет** уходить с Operator'ом.

### Layer 3 — Performance-based reputation system
- **Рейтинги, отзывы, performance history** — собственность платформы, не Operator'а
- Уход = потеря track record для следующих клиентов
- На платформе Operator стоит дороже потому что **есть видимая история**

### Layer 4 — AI-leverage недоступен вне платформы
- Флот AI агентов даёт **3-5× продуктивности**
- Уйдёшь — будешь пытаться build the same → не получится один (huge cost)
- Это эквивалент того что **вне платформы Operator зарабатывает в 3-5× меньше** даже на тех же клиентах

### Layer 5 — Cross-resource synergy
- **На платформе для того же клиента работают ещё 5 Operators** (другие ресурсы TRM)
- Все обмениваются контекстом через Jetix
- **Уход одного = потеря синергии** для клиента → клиент теряет Operator первым (по ценности)
- **Это уникальное преимущество TRM-структуры** vs Toptal / Catalant

### Layer 6 — Контрактные ограничения
- **No-circumvention clause** — стандартный 24-мес запрет работать напрямую с клиентом, найденным через платформу
- Психологический барьер + реальный legal cost при нарушении

### Layer 7 — Низкий take rate (мета-стратегия)
**Главный insight:** Jetix НЕ берёт 35-50% как Toptal. Берёт 15-25%.

- 25% → **стимул уйти средний**
- 15% → **стимул уйти маленький**
- 10% → **стимул уйти почти нулевой**

**Жертва margin per deal ради volume + retention.** Платформа выживает через **maximum GMV × разумный take rate** — не через **высокую margin × малый GMV**.

> **Главный «секрет» работающих маркетплейсов** (Wharton academic):  
> *«Наиболее эффективная anti-disintermediation стратегия — это не «запрет», а **постоянное добавление ценности**. Если платформа реально полезна — уход с неё становится невыгодным даже без юридических запретов.»*

---

## 4.7 Главный антипринцип платформы — внутренняя cohesion, внешняя конкуренция

> ⭐ **Critical логика которую Ruslan специально выделил.**

### Внутри платформы — все вместе
- **Никаких конкурирующих отделов** внутри Jetix
- **Никаких internal политических игр** между разделами
- Все мастера / Operators / партнёры — **на одной стороне**
- Конфликты интересов разрешаются через **chinese walls / sectoring** (см. §3.9 risk #2)
- Каждый знает: «я и другие участники Jetix — **одна команда**, не competitors»

### Снаружи платформы — конкуренция полная
- **Все кто не внутри / не с Jetix / против Jetix — конкуренты**
- Конкурентам — **полный набор инструментов** (market share / pricing / talent / partnerships)
- Это «**Predator-outside**» framing (D1 Vision Decision 8)
- НО — это **НЕ aggression at people**. Это **competition at market level** (как McKinsey vs BCG, не personal attacks)

### Почему это критично для платформы
**Без этого принципа:**
- Phase 1: Ruslan vs первые партнёры — competing for same clients → платформа разваливается
- Phase 2: Internal teams грызутся за resources → coordination cost > leverage
- Phase 3: Operators grызутся за наиболее прибыльные deals → клиенты разбегаются

**С этим принципом:**
- Phase 1-2: Cohesion enables fast scaling
- Phase 3: Operators **referят друг другу** клиентов под другие domains → network effect усиливается
- **Внешний враг (other consulting firms / other platforms) объединяет внутри**

> **Это и есть «Mafia inside / Predator outside»** организационная грамматика.

---

## 4.8 Phase transition к платформенной фазе — chicken-and-egg solution

### Проблема Phase 3
**Operators не приходят без клиентов; клиенты не приходят без Operators.** Все известные решения (Uber, Airbnb, Toptal, Catalant) проходили через **одну схему**:

1. **Phase 1** — сервисная компания, набирает первых клиентов руками
2. **Phase 2** — масштабируется через свою команду + Operators + first systematic processes
3. **Phase 3** — открывается как платформа

### Хорошая новость для Jetix
**Именно это Jetix делает в Phase 1-2** (см. §3.11) — путь к платформе **уже встроен** в текущую стратегию TRM.

### Critical timing — НЕ раньше 2028-2029
> *«Все эти marketplace компании потратили **5-10 лет** в Phase 1+2 прежде, чем перейти в Phase 3. Прыгнуть сразу в платформу не получалось ни у кого.»*

| Компания | Phase 1 (сервис) | Phase 2 (масштаб) | Phase 3 (платформа) | Текущий статус |
|----------|----------------|-------------------|---------------------|----------------|
| **Toptal** | Ручной скаутинг 100 разработчиков | $200M+ ARR through own team | Открытая платформа 3% acceptance rate | $200M+ ARR, $1B+ |
| **Catalant** | Ручной матчинг ex-MBA | Команда менеджеров | Marketplace 35k+ экспертов, 30% commission | ~$50M ARR |
| **Andela** | Bootcamp + staff aug | Сами растили инженеров | Open marketplace 175k+ | $200M+ ARR, $1.5B |

> **Урок:** не пытаться открыть платформу преждевременно. Накопить track record в Phase 1-2, потом открывать.

---

## 4.9 Уникальная конкурентная позиция Jetix vs Toptal/Catalant/Andela

### 3 структурных преимущества (повторение из §3.12, в контексте платформы)

#### 1. Resource multidimensionality (TRM-структура)
**Все остальные marketplace'ы матчат один тип отношений** (заказчик ⇄ фрилансер; investor ⇄ deal). **Jetix матчит 6 типов ресурсов одновременно** — уникальный сетевой эффект, которого нет ни у кого.

#### 2. AI-native infrastructure с Day 1
- Toptal / Catalant / Andela спроектированы для **2010-х (pre-LLM era)**
- Jetix HQ изначально **AI-native** — на одно поколение технологий впереди
- Operators получают **3-5× leverage** через AI агентов — ни у кого нет такого

#### 3. Cross-resource synergy для одного клиента
- На платформе для одного клиента работают **до 6 Operators одновременно** (по 6 ресурсам)
- Все обмениваются контекстом
- **Network effects per client** — отсутствуют у single-resource marketplace

### Дополнительные преимущества

#### 4. Foundation v1.0 fork-portable architecture
- Каждый Operator может **взять fork Foundation** — иметь свою специализированную мастерскую
- Не централизованная платформа диктующая workflow — а **distributed** где платформа = grammar + protocol
- Это решает scalability problem Phase 3

#### 5. Methodology compound across Operators
- Каждая успешная methodology одного Operator → попадает в общую library
- **Все Operators становятся умнее** с каждым проектом
- Compound learning эффект на уровне network, не одного человека

---

## 4.X Сводка платформы

| Аспект | Кратко |
|--------|--------|
| **Зачем нужна** | Освободить время партнёров на важное; курировать доступ к крутым людям; общий язык |
| **5 функций** | Управление проектами / Управление ресурсами / Roles / Гипотезы / Общий язык |
| **3 источника проектов** | Внутренние Jetix / TRM-driven / External owners |
| **5 levels проектов** | Single-resource → TRM-full → Mega-проекты community |
| **Take rate** | 15-25% blended (vs Toptal 35-50%) — anti-disintermediation strategy |
| **GMV scenario Phase 3 mature** | 100 Operators = €60M GMV / €15M revenue; 1000 Operators = €600M / €150M |
| **7 layers anti-disintermediation** | Infra lock-in / Escrow / Reputation / AI-leverage / Cross-resource synergy / Contracts / Low take rate |
| **Главный антипринцип** | Внутри cohesion / Снаружи конкуренция (Mafia inside / Predator outside) |
| **Phase 3 timing** | НЕ раньше 2028-2029 (precedent: Toptal/Catalant 5-10 лет в Phase 1+2) |
| **5 структурных advantages** | Resource multidim / AI-native Day 1 / Cross-resource synergy / Fork-portable / Methodology compound |

> **Главный вывод:** платформа — это **фракция Phase 3 vision**, но её механика **уже встроена в Phase 1-2 операционную модель**. Каждый клиент и каждый партнёр Phase 1-2 — это уже **proto-platform participant**.

---

# 5. 🤝 Управляющая компания — Jetix берёт ответственность за результат

> **Цель раздела:** объяснить что Jetix не просто консультирует / советует, а **реально управляет** частью ресурсов клиента и **берёт ответственность за результат**. Это центральное отличие от классического консалтинга — и центральная причина почему клиенту имеет смысл работать с Jetix даже за бóльшие fees.
>
> **Связь с §3 TRM:** этот раздел и §3 пересекаются. **§3 описывает offering структурно** (6 ресурсов / fees / лестница / архитектура). **§5 описывает philosophy** того, **почему** мы можем брать ответственность и **как** это меняет risk profile для клиента.

---

## 5.1 Что значит «управляющая компания» — ключевое отличие

### Классический консалтинг
- Делает **рекомендации** (отчёт / презентация / advisory)
- **Клиент потом** сам решает что внедрять, как, когда, кем
- **Клиент несёт всю ответственность** за результат
- Если рекомендация не сработала — консалтинг говорит «вы её неправильно внедрили / условия изменились» и **уходит**
- Pricing: fixed fee / hourly — independent of результат

### Jetix как управляющая компания
- **Реально управляет** частью ресурсов клиента (с его согласия / по контракту)
- **Сам внедряет** + сам поддерживает + сам оптимизирует
- **Берёт ответственность за результат** — performance fee только если есть рост
- Если что-то не сработало — **Jetix остаётся**, разбирается, исправляет
- Pricing: management fee + **performance fee** (% от incremental профита)

### Главная фраза
> **«Мы не какие-то там просто консультанты. Мы берём ответственность за результат.»**
>
> *Это и есть центральная позиционная разница, которую клиент должен понять с первой встречи.*

---

## 5.2 ⭐ Почему Jetix может брать на себя такую ответственность

> **Это критический раздел.** Объясняет **why now** для клиента — почему именно Jetix может сделать то что обычная консалтинг-фирма не может.

### Причина 1 — Лучшие наработки / up-to-date инструменты
Jetix **систематически собирает и применяет лучшие** существующие наработки в:
- Искусственном интеллекте (latest models / agents / tools)
- Кибербезопасности (best practices / audit frameworks)
- Юриспруденции (legal templates / regulatory expertise)
- Research methodologies (academic + industry frontline)
- Investment / wealth management
- Operations / talent / process design

**Не «один эксперт со своими старыми методами»** — а **постоянно обновляющаяся библиотека best practices**, доступная **всем мастерам / Operators** на платформе.

### Причина 2 — Дисциплинированная работа с информацией
Базовая Система Управления (Документ 1A) даёт нам:
- **Structured capture** — ничего не теряется
- **Knowledge accumulation** — каждый случай делает нас умнее
- **Provenance Officer (Part 6a)** — знаем откуда что пришло
- **Compound learning (Part 5)** — методологии накапливаются

> **Это означает:** к каждому новому клиенту мы приходим **со всем накопленным опытом** прошлых клиентов. Не начинаем с нуля.

### Причина 3 — Быстрая сборка нужных компетенций
Через **платформу** (см. §4) мы за **дни/недели** собираем команду под конкретный проект из **уже выверенных** мастеров / Operators. Не **месяцы рекрутинга** + не «такие себе» хайры.

### Причина 4 — Лучшие специалисты в сети
Каждая роль (AI / cybersec / legal / research / investment / etc.) представлена **топовым specialist'ом** в Jetix-сети. **Curated через 5 critical filter** (см. §7) + track record validation.

### Причина 5 — AI-leverage умножает возможности
12 натренированных AI-агентов + adaptable станки → один Operator делает работу 3-5 человек. **Это снижает cost при сохранении качества** → можем брать risk который traditional consulting не может позволить.

### Что из этого следует
> *Из-за того что:*
> - Мы используем **самые лучшие наработки**
> - Мы **дисциплинированно** с ними работаем
> - Мы **быстро** собираем нужные компетенции
> - У нас **лучшие специалисты** в сети
> - Мы используем **AI-leverage** для productivity multiplier
>
> **— Мы можем себе позволить реально управлять частью ресурсов клиента и брать за это ответственность.**

> *Это не пустая декларация — это **systemic preparation** which makes responsibility-taking technically possible. Без этой подготовки взять ответственность = blind risk.*

---

## 5.3 Risk-sharing model — Jetix размазывает риски, клиент рискует меньше

> ⭐ **Главный insight model:** Jetix не «убирает» риск — а **distributes его** через portfolio эффект.

### Перспектива клиента (один проект)
**Без Jetix:**
- Клиент один сталкивается с risk проекта
- Если проект не получится — **потеря 100% capital + времени + энергии**
- Это **большой risk** который многие клиенты **не могут себе позволить**

**С Jetix:**
- Клиент платит management fee (предсказуемый) + performance fee (только если есть результат)
- Jetix **берёт на себя operational responsibility**
- Если проект не получился — клиент потерял management fee, **но execution risk был на Jetix**
- **Win rate проекта повышается** (см. §5.2 — почему Jetix может)
- → **Net риск клиента ниже** даже после management fee

### Перспектива Jetix (portfolio)
**Один проект для Jetix = 1/N от total Jetix portfolio.**

- Если проект не получился — **малый удар** на Jetix (потеря 1/N от revenue + reputation hit)
- Если 5 проектов параллельно из 30 не получились — **15-20% downturn**, manageable
- **Risk pool диверсифицируется** между десятками клиентов / партнёров / Operators

### Asymmetric risk profile (выгоден всем)

| Сценарий | Один клиент без Jetix | Один клиент с Jetix | Jetix portfolio |
|----------|----------------------|---------------------|-----------------|
| Проект успех | Полная прибыль | Прибыль − performance fee 20% | Performance fee × N |
| Проект провал | Полная потеря (100%) | Потеря mgmt fee только (~5-10% от total budget) | -1/N hit, manageable |
| **Net effect** | **High volatility, ruin risk** | **Lower volatility, capped downside** | **Diversified, sustainable** |

> **Главная мысль:** Jetix не магически убирает риск (риск всегда есть). **Jetix меняет risk distribution** — клиенту выгодно платить premium за этот transfer.

### Почему это работает математически
- **N клиентов одновременно** → variance ↓ через закон больших чисел
- **Performance fee aligns incentives** — мы зарабатываем больше когда клиент зарабатывает больше
- **Cross-pollination knowledge** — каждый клиент даёт learnings которые помогают остальным
- **Aggregate Jetix learns from N projects** — accumulated expertise becomes compound advantage

---

## 5.4 Типы управления — depth levels (по 6 ресурсам)

> *Связано с §3 (TRM 6 ресурсов) — но здесь делаем акцент на **depth** управления, не на структуре.*

### 💰 Финансы
- **Light** — advisory + planning (regulatory simple)
- **Medium** — cash management + budget execution (с authority + reporting)
- **Deep** — investment portfolio management (требует BaFin license, Phase 3+)

### ⏱️ Время CEO
- **Light** — calendar review + priority advisory
- **Medium** — fractional COO/Integrator (рекомендации становятся executions)
- **Deep** — AI Chief of Staff (доступ к календарю, переписке, decision filtering)

### 📢 Аудитория
- **Light** — content strategy
- **Medium** — execution management (LinkedIn / newsletters / podcast)
- **Deep** — full ownership of audience monetization + growth (revenue share)

### 📚 Информация / знания
- **Light** — knowledge audit + recommendations
- **Medium** — KB construction + ongoing maintenance
- **Deep** — full Knowledge Operations (research delivery / synthesis / methodology development)

### 💻 Compute / AI infrastructure
- **Light** — vendor selection advisory
- **Medium** — broker model (Jetix управляет AI subscriptions клиента)
- **Deep** — full infrastructure ownership (AI agents trained на клиентском контексте, hosted by Jetix)

### 🤝 Команда
- **Light** — talent recruitment advisory
- **Medium** — fractional executive ops (Jetix-provided role play)
- **Deep** — full team ownership (Jetix recruits / manages / fires + curates через сеть)

> **Каждый клиент** может выбрать свой **depth level per resource** — не обязательно одинаковый. Например: Deep на финансы + Medium на время + Light на остальное.

---

## 5.5 Trust building — поэтапный onboarding (не «отдай всё сразу»)

### Главная антипринцип
> **Никто не отдаст управление 6 ресурсами незнакомцу сразу.** Это структурная проблема доверия.

### Решение — Land-and-Expand лестница (см. §3.5)

| Step | Уровень | Что отдаёт клиент | Trust accumulated |
|------|---------|------------------|-------------------|
| 1 | L0 €3k гипотеза | Минимум — задача + €3k | Низкий риск, проверка качества |
| 2 | L1 €5k/мес ретейнер | Information access (KB, methodologies) | «Они знают что делают» |
| 3 | L2 один ресурс | Один ресурс под mgmt | «Они могут управлять» |
| 4 | L3 AI Chief of Staff | Календарь, переписка, decision flow | «Я доверяю им integration deep» |
| 5 | L4 venture operator | Новые ventures + capital | «Они partner level» |
| 6 | L5 TRM-full | Все 6 ресурсов | «Они инфраструктура моего бизнеса» |

### Mechanism trust accumulation
1. **Каждый L доказывает Jetix-компетенцию** через результат
2. **Performance fee** показывает skin-in-the-game (Jetix не зарабатывает без roста)
3. **Reporting + transparency** на каждом этапе (Visual / View principle)
4. **Public-company-style accountability** (см. anti-pyramid mechanism, §6.4 collection)
5. **Network references** — другие клиенты Jetix могут confirmable verify experience

### Anti-pattern (что не работает)
- ❌ «Подпиши TRM-full сразу за €670k/год» — никто не подпишет
- ❌ «Платим по результату только, без management fee» — Jetix не может work без operational coverage
- ❌ «100% performance-based» — слишком рискованно для Jetix без validation period

---

## 5.6 Юридическая структура — boundaries и authority

### Phase 1 — Standard consulting contracts
- Без Asset Management license
- Advisory authority only (рекомендации)
- Light operational delegation (через специальные SOWs)
- **Limit:** не управляет официально investment portfolio
- **Pricing:** mgmt fee + performance fee allowed (НЕ falls under regulated AM в большинстве jurisdictions)

### Phase 2 — Extended multi-resource contracts
- Расширенные SOWs покрывают 3-5 ресурсов
- **Не BaFin-licensed** ещё — но close to that boundary
- **Альтернатива:** партнёрство с лицензированной структурой для финансов

### Phase 3 — BaFin license (KAGB / WpHG)
- **Capital requirement:** €730k+
- **Compliance staff:** dedicated team
- **Reporting:** quarterly to BaFin
- **Audit:** external annual
- **Worth it because:** unlocks full TRM-full финансы management
- **Timeline:** 3-5 лет to acquire (parallel with Phase 2 growth)

### Universal contract elements (любая фаза)
- **Clear KPIs at start** — что считается «success» для каждого ресурса
- **Baseline measurement** — что было ДО Jetix (для performance fee calculation)
- **Authority boundaries** — что Jetix может делать без согласования / что требует ack
- **Reporting cadence** — weekly / monthly / quarterly to client
- **Termination clauses** — exit ramp obligations / hand-over period
- **Confidentiality** — chinese walls между разными клиентами Jetix
- **Dispute resolution** — neutral arbitration (NOT internal Jetix authority)

---

## 5.7 Сравнение «Jetix управляющая» vs другие модели

| Параметр | Jetix Mgmt Co | Classic Consulting (Big 4) | Holding (BlackRock) | Interim Executive |
|----------|---------------|---------------------------|---------------------|-------------------|
| **Что делает** | Управляет 6 ресурсами клиента | Даёт рекомендации | Управляет 1 ресурсом (деньги) | Один человек на одну роль |
| **Скейл управления** | До 30+ клиентов parallel через AI | Linear (people-bound) | Тысячи клиентов через algorithms | 1 клиент в моменте |
| **Risk transfer от клиента** | Высокий (operational responsibility) | Минимальный | Только финансовый | Limited (зависит от контракта) |
| **Performance fee** | 15-25% от incremental | Редко (только результаты) | 10-20% от gains | Возможно через equity |
| **Skin-in-the-game** | Сильный (через performance) | Слабый | Сильный по финансам | Зависит |
| **Cross-resource synergy** | Уникально (6 ресурсов одновременно) | НЕТ | НЕТ (только финансы) | НЕТ |
| **Use of AI / leverage** | Native, по умолчанию | Ad-hoc | Algorithmic для финансов | Personal capability |
| **Best fit для** | Клиент с растущим бизнесом ищущий operator | One-time strategic projects | Wealth preservation / growth | Crisis / specific role gap |

---

## 5.8 Анти-паттерны управляющей компании

### ❌ Промахи которые мы НЕ делаем

#### Не пытаемся быть «classic asset manager»
Jetix **не классическая управляющая компания типа BlackRock**. Они управляют **финансами** для **тысяч клиентов** через algorithms. Мы управляем **6 ресурсами** для **десятков клиентов** через **AI + curated team**.

#### Не работаем без skin-in-the-game
Если клиент хочет «pay us flat fee — мы делаем что-то — без performance fee» — **это не наш формат**. Мы работаем только когда **align'ены интересы** через performance.

#### Не даём управление без вётинга клиента
Не каждый клиент подходит. Мы **отбираем** через 5 critical filter (см. §7) — потому что управление requires ownership / discipline / long-term thinking от обеих сторон. Без этого = неудача гарантирована.

#### Не обещаем guaranteed outcomes
Risk transfer ≠ risk elimination. Мы **снижаем** risk через preparation + diversification, но **гарантий** на конкретный результат не даём. Это honest-pricing вместо overpromising-underdelivering.

#### Не работаем с conflict of interest
Если потенциальный клиент **прямой конкурент** существующего клиента — отказываемся. Chinese walls + sectoring (1 клиент на отрасль).

---

## 5.X Сводка управляющей компании

| Аспект | Кратко |
|--------|--------|
| **Ключевое отличие** | Берём ответственность за результат, не просто советуем |
| **Главная фраза** | «Мы не консультанты — мы управляющая компания» |
| **Почему можем** | Лучшие наработки + дисциплина + быстрая сборка + лучшие специалисты + AI-leverage |
| **Risk model** | Distribute, not eliminate. Asymmetric для клиента (lower volatility) и Jetix (diversified) |
| **Depth levels** | Light / Medium / Deep per resource — клиент выбирает |
| **Trust building** | Land-and-Expand лестница L0-L5 (см. §3.5) |
| **Юр. структура** | Phase 1 — standard consulting contracts; Phase 3 — BaFin license unlocks full TRM |
| **Anti-patterns** | Не classic AM / не без skin-in-the-game / не без вётинга / не guaranteed outcomes / не conflict of interest |

> **Главный вывод:** Jetix как управляющая компания **меняет фундаментально** взаимоотношения клиент-провайдер. Не «купил — получил отчёт — внедрил сам». А **«отдал часть управления → получил результат → разделил прибыль»**. Это **архитектурный сдвиг** в том как может выглядеть бизнес-партнёрство в эпоху AI.

---

# 6. 🧪 Большая авантюра века / Эксперимент

> **Цель раздела:** описать главную ambition Jetix — **собрать всех авантюристов мира под одной крышей** и **запустить их на самую большую авантюру века**. Это не маркетинговая фраза — это **архитектурный принцип self-selection** для участников.
>
> **Преобладающая интонация раздела:** честно признаём что это **эксперимент** + **engineering-faith bet** (не gambling). Мы делаем что никто ещё не делал — и понимаем что не на 100% знаем как именно. Но **подготовлены** через Foundation v1.0 + накопленную methodology + curated team.

---

## 6.1 ⭐ Главная мысль — собрать всех авантюристов на самую большую авантюру века

### One-liner
> **«Объединить всех авантюристов в самую большую авантюру.»**  
> *— Verbatim Ruslan, audio_401, 2026-04. LOCKED как D1 Vision tagline.*

### Расшифровка
- **«Авантюристов»** — не gamblers / mass-public. Конкретные **профессионалы / founders / исследователи** которые и так уже работают над собственными амбициозными проектами (см. §6.2 определение).
- **«Объединить»** — собрать на одной платформе, дать инструменты для коммуникации, создать общий язык и общую инфраструктуру.
- **«Самая большая авантюра»** — главная авантюра века, которая больше любого личного проекта (см. §6.5 что это).

### Почему именно «авантюра»
Слово выбрано **сознательно** — оно работает как **filter / self-selection mechanism**:
- Привлекает: **builders, проактивных, тех кто любит игру в долгую**
- Отталкивает: **passive consumers, gamblers, те кто ждут готового решения**
- **Громкость invitation = узкий target audience** (это feature, не bug)

> Это **predator-outside framing** (D1 LOCKED §4.2) — провокативный tone используется как self-selection. **НЕ aggression at people**, а filter who responds.

---

## 6.2 Кто такой авантюрист — определение + 6+ типов

### Определение
**Авантюрист** в контексте Jetix — это человек, который:
- **Имеет какую-то личную авантюру** — большую цель / проект / гипотезу которую хочет воплотить
- **Готов вкладываться** временем / ресурсами / умом ради воплощения
- **Любит игру в долгую** (long-term mindset, не quick win seeking)
- **Не ждёт готовых ответов** — готов открывать / экспериментировать / адаптироваться
- **Имеет skin-in-the-game** — рискует своим, не ищет «бесплатный билет»

### Авантюра ≠ безответственная игра
**Это критически важное различие:**
- Авантюрист = **calculated risk taker** (skilled player)
- НЕ gambler (random risk taker)
- Авантюра подкреплена **подготовкой / методологией / track record**
- Это ближе к "**explorer**" чем к "**casino player**"

### Типы авантюристов — у каждого своя личная авантюра

> *У каждого профессионала есть своя авантюра — то что он сам считает большим вызовом. Все они потенциальные участники Jetix.*

| Тип | Личная авантюра |
|-----|-----------------|
| 🚀 **Founder / Предприниматель** | Построить компанию которая изменит индустрию / рынок |
| 💼 **Менеджер / Operator** | Собрать **лучшую команду** / построить best-in-class operations |
| 💰 **Инвестор** | Найти / build winning bets через unique thesis |
| 🔬 **Исследователь / Учёный** | Сделать прорыв в понимании / закрыть важный белый пятно |
| 🛠️ **Indie hacker / Builder** | Построить продукт который полюбят / нишевая монетизация |
| 🎓 **Educator / Methodology developer** | Описать методологию которая поможет другим |
| 🎯 **Strategist / Thinker** | Понять / описать новую модель мира |
| 📢 **Creator / Influencer** | Построить аудиторию + влияние через качественный контент |
| 🤝 **Coach / Advisor** | Помочь конкретным людям достичь их максимума |
| 💻 **Engineer / Tech expert** | Построить или improve систему делающую невозможное возможным |
| ⚖️ **Politician / Reformer** | Изменить структуру / правила / систему к лучшему |

> **У каждого — своя personal авантюра.** Jetix хочет **их всех** под одной крышей.

---

## 6.3 База — вера в будущее

### Принципиальное основание
**Авантюра не работает без веры в будущее.**

> *Если ты не веришь что будущее можно сделать лучше — ты не возьмёшься за большое дело. Останешься в comfort zone.*

### Что значит «вера в будущее»
- Понимание что **текущее ≠ предел**
- Уверенность что **agency делает разницу** (наши действия влияют на исход)
- Long-term horizon — действуешь сегодня для результата через 1/3/10 лет
- Доверие к **процессу + дисциплине** (не «всё зависит от удачи»)
- Optimism + realism balance — оба нужны, ни один не достаточен

### Почему это критично для платформы
**Jetix как сообщество работает только когда все участники имеют эту базу.** Если кто-то skeptik / cynic / nihilist — он будет **тормозить** работу остальных. Проектный riск ↑.

**Поэтому:** один из критериев входа в Jetix (см. ICP §7) — это **upward direction** (см. ICP filter D22) = **active belief in better future + готовность работать ради него**.

### Engineering-faith, не blind faith
**Вера ≠ магия.** В контексте Jetix:
- ✅ Вера выражается через **resource allocation** (вкладываешь время / деньги / энергию)
- ✅ Вера подкреплена **engineering preparation** (Foundation / methodology / curated team)
- ✅ Вера протестирована на **incremental milestones** (€50K → €200K → €1M)
- ❌ НЕ вера через affirmations / wishful thinking / hope

> **Engineering-faith** = «строю инфраструктуру для $1T scale, потому что верю что engineering preparation делает разницу» (vs «надеюсь что повезёт»).

---

## 6.4 Что делает Jetix для авантюристов — 4 функции

### Функция 1 — Помогает воплощать ИХ личные авантюры быстрее/качественнее
Каждый участник имеет свою personal авантюру. Jetix даёт ему:
- **Foundation infrastructure** — не строит с нуля
- **Adaptable станки** (D2 / MCP / Plan Mode / Voice / etc.)
- **AI-агенты** (12 ролей готовых)
- **Compound learning** из других participants
- **Curated talent pool** для команды

> Эффект: личная авантюра воплощается в **2-5× быстрее** чем без Jetix.

### Функция 2 — Создаёт инфраструктуру для **коммуникации** между авантюристами
- **Общий язык** (Foundation v1.0 grammar)
- **Стандартные форматы** (proposals / contracts / artifacts)
- **Платформа для связи** (Phase 2-3 marketplace, см. §4)
- **Translation cost ≈ 0** между участниками

> Эффект: авантюристы которые раньше работали изолированно — теперь могут **collaborate** на проектах больше любого одного.

### Функция 3 — Запускает их на **главную авантюру века**
> *Это самое амбициозное.* Jetix не только помогает с личными авантюрами — но **направляет collective force** на главную авантюру (см. §6.5).

- Создание **shared vision** того куда мы все идём
- Координация **collective projects** Phase 3 community
- Накопление **shared methodology** которая выйдет наружу мира

### Функция 4 — Тестирует / экспериментирует / документирует
- Какие процессы работают для авантюристов
- Какие инструменты дают наибольший leverage
- Как авантюристы лучше collaborate в разных конфигурациях
- **Накапливаем methodology** = output для следующих поколений

---

## 6.5 ⭐ Что такое самая большая авантюра века — главная цель

> **Это центральная амбиция Jetix.** Главная авантюра, на которую мы запускаем всех авантюристов мира.

### 4 направления главной авантюры

#### 1. Улучшение общества
- Новые модели коллаборации (vs current LinkedIn-style transactional)
- Новые формы organizations (Korp-Startup vs traditional corp)
- Новые механизмы доверия (Reputation system / engineering-faith vs blind authority)
- Снижение systemic frictions (information overload / coordination cost / talent matching)

#### 2. Создание лучших способов жизни
- Personal sovereignty через AI-leverage (см. JETIX-VISION D1 tagline)
- Liberation от рутины через автоматизацию
- Compound learning как новая базовая практика
- Workshop-as-life-pattern (mastery + tools + project + community)

#### 3. Новые инструменты / методы работы — с чем угодно
- С **информацией** (Wiki + retrieval + synthesis methodologies)
- С **людьми** (curated talent matching + cross-resource collaboration)
- С **временем** (Time tracking + compound + 6-resource management)
- С **деньгами** (TRM-style management vs traditional wealth management)
- С **знаниями** (Knowledge accumulation + sharing protocols)
- С **технологиями** (AI-agent orchestration + adaptable станки)

#### 4. Стать новой культурой / философией следующих поколений
- Engineering-faith как replacement для blind faith / hopeful thinking
- Skin-in-game responsibility как new standard
- Quality > quantity в talent / partnerships / клиентах
- Compound learning > consumption
- Cooperation > extraction
- **«Mafia inside / Predator outside»** — sustainable organizational grammar

> *Итог:* **создать общество удобное / качественное + описать / проработать чтобы потом им можно было пользоваться, кайфовать, быстро применять**. Это **infrastructure для civilizations 2030+** который потом «можно скопипастить».

### Civilizational scale
> **Verbatim Ruslan:** *«Jetix настолько блять будет масштабным, мощным… что это будет, блядь, сопоставимо, сука, с странами какими-то.»*  
> [src: audio_496, decisions/JETIX-VISION.md:§14]

> *Это сопоставимо с **созданием новой цивилизационной инфраструктуры**.* Не «компания заработала много» — а «способ жизни / работы изменился у поколения».

---

## 6.6 ⭐ Что Jetix тестирует — 5 главных гипотез

> *Это конкретные experimental claims которые мы doing test через operational existence Jetix.*

### Гипотеза 1 — AI-native operational company возможна
- **Тест:** один человек + 12 AI ролей делает работу команды 5-10 человек
- **Validation:** Phase 1 €50K → Phase 2 €5-20M ARR с командой 30-50
- **Если работает:** новый класс entity (vs traditional consulting / SaaS / agency)

### Гипотеза 2 — Total Resource Management as service на 6 ресурсах одновременно
- **Тест:** один клиент отдаёт 6 ресурсов в управление, Jetix delivers result
- **Validation:** L0 → L5 ladder progression на реальных клиентах
- **Если работает:** переопределение «консалтинга» в эпоху AI

### Гипотеза 3 — Авантюристы могут работать друг с другом эффективно
- **Тест:** Phase 2-3 platform — несколько авантюристов на общих проектах через общую инфраструктуру
- **Validation:** проекты Level 3-5 (cross-domain mega-проекты) собираются и завершаются успешно
- **Если работает:** model для distributed collaboration smart people (новая категория org)

### Гипотеза 4 — ⭐ Авантюра управления — адекватные люди в управлении
> *Самая амбициозная гипотеза — изменить строй общества.*

**Тест:**
- Сейчас управлением (компаниями / проектами / ресурсами) часто занимаются **рандомные люди** — не за заслуги / компетенции, а потому что **повезло иметь доступ** к ресурсам / связям / ситуации
- Jetix показывает альтернативу: **управление берут на себя действительно адекватные** — те кто разбираются в управлении, имеют track record, готовы нести ответственность
- TRM модель + curated Operators = practical demonstration этого

**Validation:**
- Через 5-10 лет — Jetix Operators управляют ресурсами в десятки раз эффективнее «рандомных назначенцев»
- Compound demonstration → social pressure → systemic change
- Не утопия, а **gradual reframing** через example

**Если работает:** изменение standards того, **кому доверяют управление в обществе**. Это и есть «новая культура / философия» (см. §6.5).

### Гипотеза 5 — USB-C universal connector в AI-business space (Phase 3+)
- **Тест:** Jetix существует на уровне universal protocol (vs vendor lock-in)
- **Validation:** партнёры / клиенты / инструменты coexist через Jetix не теряя независимости
- **Если работает:** standards-level interoperability в новой эре business

---

## 6.7 ⭐ Авантюра управления — изменение строя

> ⭐ **Это одна из самых важных вещей которую Jetix тестирует.** Заслуживает отдельного раздела.

### Текущая проблема управления в обществе
**Кто сейчас управляет** компаниями / ресурсами / большими проектами?
- Часто — **наследники** (повезло родиться)
- Часто — **те у кого есть связи** (повезло встретить нужных людей)
- Часто — **те у кого есть капитал** (повезло начать с ресурсами)
- **Не всегда** — те кто реально **разбираются в управлении** + способны нести ответственность

> *Это не критика конкретных людей — это **structural problem**. Selection mechanism для управленческих позиций часто **не корреллирует с компетенцией**.*

### Авантюра Jetix
**Что если можно изменить эту структуру?**

- Создать **alternative path** в управление: через **track record** + **методологию** + **curated network**
- Демонстрировать что **адекватные люди** управляют **в разы лучше** «рандомных назначенцев»
- Через compound demonstration → создать **social pressure** → systemic change

### Mechanism
1. **Phase 1-2:** Jetix Operators управляют ресурсами клиентов **лучше альтернатив**
   - Performance fee показывает skin-in-game
   - Track record накапливается публично
   - **Existence proof** что это возможно
2. **Phase 3:** Платформа открывается — больше Operators получают доступ к management roles через **competence-based selection**, не connections
3. **Phase 4+ / 200y:** Альтернативная модель selection укореняется в обществе. Управленческие позиции всё чаще **earned through competence**, не **inherited / lucky**

### Это НЕ
- ❌ Революция / overthrow существующих структур
- ❌ Заявление что «текущие управленцы плохие»
- ❌ Идеологическое движение

### Это
- ✅ **Practical demonstration** альтернативы
- ✅ **Gradual reframing** через successful examples
- ✅ Изменение **defaults** в society — что считается «нормальным» для управленческих позиций
- ✅ Создание **infrastructure** для этой альтернативы (Foundation + Jetix)

> *Это и есть «новая культура / философия следующих поколений».*

---

## 6.8 Engineering-faith bet — НЕ pyramid / scam / hype

> **Critical:** это не финансовая авантюра типа crypto-pump или MLM. Это **engineering-grounded ambition**.

### Что значит «engineering-faith»
> **Verbatim Ruslan:** *«Это все должно быть не какая-то там ебаная пирамида или еще что-то, блядь. Нет. А реально адекватные инструменты, наработки, технологий.»*  
> [src: holding-vision-2026-04-21 Note 5]

**Engineering-faith =** вера выраженная через:
- **Реальные инструменты** (D2 / MCP / Plan Mode / 12 AI агентов / станки)
- **Адекватная методология** (Foundation v1.0 LOCKED, 11 Parts + Pillar C, fork-portable)
- **Founder commitment** (skin-in-game, full-time, full investment of life)
- **Track record накапливается** (€50K → €200K → €1M validation milestones)
- **Infrastructure-first** ($1T scale baked into Phase 1 architecture, без редизайна)

### Не: hopeful talk / blind belief / get-rich-quick scheme
- ❌ Нет «инвестируйте сейчас и получите multiple X»
- ❌ Нет MLM / referral structure
- ❌ Нет токенов как primary monetization (Phase 2-3 internal utility, не speculation)
- ❌ Нет hype-driven marketing
- ❌ Нет «секретного метода чтобы быстро заработать»

### Trust mechanism — public-company-style transparency from Day 1
> **Verbatim Ruslan (audio_556):** *«джек должен быть публичной компании — вести себя как публичная компания, чтобы любой аналитик мог проверить, посмотреть, видеть, для все пятна, все как управляется»*  
> [src: voice-extract:§1.9.7]

**Mechanism:**
- Jetix **ведёт себя как public company** даже до листинга
- Метрики / decisions / structure — **видимы для аналитика**
- Это **anti-pyramid signal** — не «закрытая контора с секретами»
- Cross-cuts Visual / View principle (external dashboard для accountability)

> *Любой потенциальный participant может **сам проверить** что Jetix реально делает что говорит. Это invariably anti-scam mechanism.*

---

## 6.9 Cooperation, не extraction — ключевая ценность

> **Verbatim Ruslan (audio_554):** *«пока остальные дурачки целятся на какой-то one-person бизнес, в одиночку какие-то инструменты используют и так далее. Jetix наоборот нацелен на синергию, на сотрудничество, на партнерство»*  
> [src: voice-extract:§1.5.1]

### Implications
- **Не zero-sum game** где Jetix забирает у конкурентов / клиентов / партнёров
- **Positive-sum** — synergy создаёт **новую value** которая распределяется между всеми
- **Open-source philosophy** (см. wiki/concepts) — методологии publish'аются, не скрываются
- **Revenue Share contract** — партнёры сохраняют свои ресурсы и навыки даже если Jetix распадётся (антифрагильность)

### Quote re: Open Source
> «Jetix мог бы забирать до 70% прибыли партнёра за счёт экосистемы. Мы этого не делаем — потому что верим, что устойчивее платформа, в которой каждый участник сохраняет свою силу. Если завтра Jetix исчезнет, ваши ресурсы, контакты и навыки останутся у вас. Это закреплено контрактно.»  
> [src: wiki/ideas/revenue-share-jetix-philosophy.md]

---

## 6.10 Что если не получится — honest fallback

> *Никакой авантюры без реалистичного fallback.* Что мы выносим даже из failed experiment?

### Что **остаётся** даже если Jetix не достигнет $1T scale

#### 1. Накопленный knowledge / methodology
- Foundation v1.0 LOCKED — fork-portable architecture, может быть взята другим founder'ом
- Workshop concept + TRM methodology — published artifacts
- Compound learning library — десятки методологий для конкретных задач
- 12-mes retrospective + tracking baseline — proven discipline

#### 2. Network of skilled people
- Curated network через 5 critical filter — these people remain connected даже без Jetix
- Каждый участник вынес свой compound learning и навыки
- Cross-pollination knowledge между participants → они индивидуально сильнее

#### 3. Foundation v1.0 — fork-portable infrastructure
- Архитектура которую любой другой founder может взять и использовать
- 11 Parts + Pillar C полностью документированы
- Open-source ethos позволяет наследование

#### 4. Compound-engineering practices что показали себя
- Plan Mode + ultrathink for strategic decisions
- Voice pipeline → structured artifacts
- D2 diagrams as live documentation
- Time-tracking discipline through Toggl + AW
- Knowledge management through Karpathy LLM Wiki + HippoRAG

#### 5. Personal transformation founder + early team
- Через Phase 2 (mind-training) + Phase 3 (active build) — фундаментальное upgrade человеческого capital
- Это **personal accumulation** который никуда не девается

> **Failure scenario:** Jetix achieves €5-10M ARR по TRM-lite формату, не доходит до Phase 3. **All above stays valid.** Founder + early participants remain stronger than they would be otherwise.

---

## 6.11 Что если получится — масштаб амбиции

### Trajectory
**€5K (now, 2026-04-21)** → **€50K Q2 2026** → **€200K validation** → **€1M ARR** → **$100M** → **$100B** → **$1T market cap**

### $1T trajectory — engineering-faith bet
> **Verbatim Ruslan:** *«Jetix целится на то, чтобы стать первой… поставить вообще мировой рекорд по достижению капитализации в 1 триллион долларов. Скорость, за которую будет достигнута эта цифра от нуля, от создания компании до триллиона.»*  
> [src: holding-vision-2026-04-21 Note 5]

**Precedent to beat:** XEI → $100B за 2 года.

### Что меняется в мире (200-year vision)
- ✅ **Новая категория organization** признана и копируется (AI-native operational corp)
- ✅ **TRM как mainstream** управления бизнесом (vs traditional consulting / family office)
- ✅ **Workshop-as-life-pattern** распространяется среди профессионалов
- ✅ **Compound learning** становится default expectation для high-performance roles
- ✅ **Engineering-faith** как cultural norm (vs blind faith / wishful thinking)
- ✅ **Curated networks** quality > quantity признаны лучшим способом organize
- ✅ **Адекватные люди в управлении** становится more common (мест авантюры управления — см. §6.7)

### Two leverages в long-term (200y vision)
1. **AI-эффективность** — больше выходных продуктов на единицу ресурса (для всех клиентов / партнёров)
2. **AI-безопасность** — снижение systemic risks (cybersec, supply chain, decision quality)

### Founder constitution принцип
> «Когда система станет большой, контролировать её напрямую невозможно — поэтому ценности и предохранители закладываются ДО роста.»  
> [src: wiki/ideas/founder-responsibility-jetix-constitution.md]

**Это значит:** Foundation v1.0 + Pillar C (Tier 2 11 hard rules) уже **закладывают safeguards** на долгосрочное development. Когда Jetix станет $100B+, эти safeguards будут active без нужды в personal control founder'а.

---

## 6.X Сводка авантюры века

| Аспект | Кратко |
|--------|--------|
| **Главная мысль** | «Объединить всех авантюристов в самую большую авантюру» |
| **Кто авантюрист** | Профессионал с personal авантюрой + готовностью вкладываться + long-term mindset |
| **Типы** | Founder / Менеджер / Инвестор / Researcher / Indie / Educator / Strategist / Creator / Coach / Engineer / Reformer (11 archetypes) |
| **База** | Вера в будущее (engineering-faith, не blind faith) |
| **Что Jetix даёт авантюристам** | Infrastructure / коммуникация / inclusion в главную авантюру / тестирование |
| **Главная авантюра века** | Улучшение общества + лучшие способы жизни + новые инструменты + стать новой культурой |
| **5 главных гипотез** | AI-native company / TRM as service / cooperation авантюристов / **изменение управления в обществе** ⭐ / USB-C universal connector |
| **Авантюра управления** | Адекватные люди в управлении вместо «рандомных хуесосов с доступом» — gradual reframing через examples |
| **Trust mechanism** | Engineering-faith + public company transparency Day 1 + reverse all Anti-pyramid signals |
| **Cooperation philosophy** | Positive-sum / synergy / open source / revenue share / антифрагильность партнёров |
| **Если не получится** | Foundation+methodology+network+practices+personal upgrade — все остаётся valid |
| **Если получится** | $1T trajectory / новая категория org / civilizational infrastructure / 200-year impact |

> **Главный вывод:** Афёра века Jetix — это **engineering-faith bet** на изменение **how smart people work together** + **how society organizes management**. **Не gambling, не pyramid, не hype.** Calculated, prepared, founder-committed bet которая опирается на real tools / methodology / track record. **И именно поэтому** мы зовём авантюристов — потому что они **различают** реальную авантюру от пустой обещалки.

---

# 7. 🎯 ICP — концептуальный portrait участников Jetix

> **Цель раздела:** конкретно кто партнёр / клиент Jetix. **НЕ конкретная индустрия / география** — а **концептуальный portrait** через 2 оси: (1) уровень ресурсов и (2) желание развиваться. Под этот portrait подходит много кто, независимо от индустрии.

## 7.1 Базовый принцип ICP — не география / индустрия, а 2 оси

**Главный портрет участника Jetix:**

### Ось 1: Уровень ресурсов
- Финансы (есть деньги или есть нечего вложить)
- Время / энергия (есть капасити вкладываться или нет)
- Знания / экспертиза (накопленная база)
- Network (с кем связан)
- Команда (один человек или есть люди)
- Compute / инструменты (доступы / подписки / tools)

### Ось 2: Желание развиваться
- Понимание что чего-то не хватает (текущее = не предел)
- Готовность вкладываться в развитие (не просто "хочется чтобы кто-то сделал")
- Long-term mindset (не "быстро и потом забыть")
- Готовность учиться на накопленном чужом опыте + делиться своим

**Если оба условия есть** — потенциальный участник Jetix, **независимо** от:
- Индустрии (manufacturing / SaaS / consulting / coaching / etc.)
- Географии (DACH / Eastern Europe / global remote)
- Стадии бизнеса (idea / early / scale / mature)
- Размера (1 человек / 5 / 50 / 500)

## 7.2 3 типа участников — по уровню вовлечения

> *Не клиенты vs партнёры — это спектр.*

### 🟢 Тип 1 — Solo Entrepreneurs / Indie Hackers (используют систему за процент)

**Кто:** один человек строит свой проект / бизнес / practice. Может быть founder / consultant / coach / creator / advisor.

**Что им даёт Jetix:**
- Полный доступ к Базовой Системе как foundation
- Натренированные AI-агенты (12 ролей)
- Adaptable станки (D2 / MCP / Plan Mode / Voice / Time-tracking)
- Compound learning + общая community knowledge
- Cross-collaboration с другими indie через Jetix infrastructure

**Что Jetix получает:**
- **Процент от их revenue / outcome** (модель similar к revenue share)
- Их contributions back в общую систему (новые методологии / inсайты / станки)
- Network growth (они приводят в систему своих клиентов / коллег)

**Пример:** indie consultant с €5-15K/мес practice → получает Jetix infrastructure → растёт до €30-50K/мес → отдаёт 10-20% revenue share.

---

### 🔵 Тип 2 — Средний бизнес (используют систему, отдают процент)

**Кто:** компании размером от 5 до 100+ человек, владелец активно вовлечён, есть **ресурсы и желание расти**. Любая индустрия. Любая география.

**Что им даёт Jetix:**
- Foundation infrastructure для их operational layer
- Натренированные AI-агенты под их специфику
- Implementations / customizations adaptable станков
- Periodic strategic консультации / planning sessions
- Cross-pollination с другими бизнесами в Jetix network

**Что Jetix получает:**
- **Процент** (mgmt fee + performance fee на growth metrics)
- Их operational data → patterns → улучшение системы для всех
- Case studies / success stories для marketing

**Пример:** small SaaS company €500K ARR → подключается к Jetix → растёт до €2-5M ARR за 2-3 года → платит mgmt fee + % growth.

---

### 🟣 Тип 3 — Те кто отдают часть ресурсов в управление (deepest tier)

**Кто:** люди / компании которые **готовы делегировать управление частью своих ресурсов** (финансами / временем / аудиторией / знаниями / etc.) Jetix — потому что верят что Jetix управляет лучше чем они сами.

**Что им даёт Jetix:**
- Активное управление частью их ресурсов (не просто советы)
- Освобождение их focus на то что они любят / умеют лучше всего
- Compound оптимизация ресурсов через Jetix expertise + AI-augmentation
- Reporting + transparency на всё что делается с их ресурсами

**Что Jetix получает:**
- **Mgmt fee + performance fee** (TRM модель в полную силу)
- Глубокую integration → больше data → больше leverage для них и для системы

**Пример:** founder который заработал €5M exit, не хочет сам управлять wealth + time + знаниями — отдаёт это Jetix. Jetix делает trust-based управление.

## 7.3 Общий критерий — у тебя есть **ресурсы** + **желание развиваться**

**Это и есть весь ICP в одной строке:**
> *Любой человек или организация у которых есть какие-либо ресурсы (даже минимальные) и есть желание / понимание что развитие нужно — потенциальный участник Jetix. Уровень вовлечения (Type 1 / 2 / 3) определяется глубиной их ресурсов и amount готовности делегировать.*

## 7.4 Pains / triggers для входа в Jetix

> *Что заставляет потенциального участника искать что-то типа Jetix.*

- **«Я делаю всё сам и не хватает капасити»** (solo founders → Type 1)
- **«Бизнес растёт, но всё медленнее чем хочется, я не понимаю где затыки»** (mid-size → Type 2)
- **«У меня есть деньги / время / связи но я не знаю как их максимально использовать»** (Type 3)
- **«Я хочу учиться у людей с похожими амбициями но более продвинутых»** (любой Type)
- **«Я устал управлять всем сам, хочу делегировать operationally а не просто tactically»** (Type 3)
- **«AI / новые tools меняют game, я не могу один это все integrate»** (любой Type)

## 7.5 НЕ наш ICP — explicitly

**Кому Jetix не подходит:**
- ❌ Люди которые **не хотят меняться** / "у меня и так всё хорошо"
- ❌ Те кто ждут **готовое решение под ключ без вовлечения** (Jetix = сотрудничество, не assembly line)
- ❌ Покупатели **самой дешёвой опции** (мы не competitor SaaS подписок)
- ❌ Те у кого **нет вообще ресурсов** (для start даже Type 1 нужно минимум €X финансов или Y времени)
- ❌ Краткосрочный mindset (Jetix даёт результаты в горизонте 6-36 мес, не 1-3 мес)
- ❌ Не разделяют ценности из Pillar C (если ценности противоречат — не сработает)

## 7.6 Сравнение 3 типов одной таблицей

| Параметр | Type 1: Solo / Indie | Type 2: Средний бизнес | Type 3: TRM (управление) |
|----------|---------------------|------------------------|--------------------------|
| Размер | 1 человек | 5-100+ чел | Любой (с делегированием) |
| Вовлечённость в систему | Полная (сам использует) | Гибрид (часть команда) | Активная (Jetix manages) |
| Что даёт | Foundation + agents + станки + community | + customizations + strategic | + active management части ресурсов |
| Что получает Jetix | Revenue share % | Mgmt fee + % growth | Mgmt fee + performance fee |
| Глубина integration | Light | Medium | Deep |
| Время до результата | 1-3 мес setup, 6-12 мес leverage | 3-6 мес setup, 12-24 мес leverage | 6-12 мес setup, 24-36 мес transformation |

---

## 7.7 ⭐ Команда / работники Jetix — отдельная категория

> **Important:** ICP в разделах выше — это **участники / клиенты / партнёры** платформы. Это **разные люди** от тех кто работает **внутри Jetix как команда** — те кто изучают наработки, работают с клиентами, строят саму Jetix. Эту команду тоже нужно описать **отдельно**.

### Базовый принцип
**В Jetix нет профанов.** На любом уровне — от entry до core team — есть **минимальный bar**.

Базово (общее для всех уровней команды):
- ✅ **Желание развиваться** (то же что для участников ICP — это база)
- ✅ **Интеллектуальные способности** (выше определённого уровня)
- ✅ **Высокий порог качества** в работе
- ❌ **НЕ берём** просто за «согласие работать» / связи / готовность работать дёшево

### Два уровня команды

#### 🟢 Низкий уровень — entry / promotional / supporting
**Кто:** люди которые продвигают систему, рассказывают о Jetix, supporting роли, начальные tasks.

**Минимальный bar:**
- Желание развиваться (active, не пассивное)
- Базовая дисциплина (умеют делать что обещали в сроки)
- Понимают и разделяют ценности (Pillar C Tier 1)

**Что они делают:**
- Outreach / community management
- Content support
- Administrative tasks
- Initial research / data gathering
- Onboarding / coordination

**Не требуется:** прошлый track record / большие достижения. Это **entry path** для людей с потенциалом.

---

#### 🔴 Высокий уровень — core team / работа с клиентами + партнёрами + строительство Jetix
**Кто:** те кто работают с потенциальными партнёрами, с клиентами, делают TRM management, строят платформу, развивают methodology.

**Дополнительный bar (поверх базового):**

##### ⭐ Достижения за спиной — обязательно
**Только** те у кого есть **реальный track record**:
- Управление большими портфелями (бизнесы / проекты / команды / fonds)
- Значимые накопленные ресурсы — **особенно в виде знаний и навыков**
- Доказанная экспертиза в каком-то domain
- История доведённых до конца значимых проектов

##### ⭐ Knowledge & Skills > Просто финансы
**Это критически важная фильтрация:**
- ✅ **Знания + навыки управления** — основной criterion
- ✅ Если у человека есть **знания и навыки управления финансами** — окей, отлично
- ❌ Просто **наличие финансов** — **недостаточно** для core team
- ❌ «Я инвестирую» / «у меня есть деньги» / «я могу подключить капитал» — **не пропуск**

> **Логика:** мы строим **operational corporation**, не investment fund. Команда должна **уметь делать**, не только **финансировать**. Капитал важен, но он secondary к knowledge + skills.

##### ⭐ В Jetix управляют те кто умеет управлять
Это **manifestation** «Авантюры управления» (см. §6.7) — внутри Jetix мы **сами демонстрируем** принцип: управленческие роли получают только те кто **разбираются в управлении**, имеют **track record** + **competence**, не просто **доступ к ресурсам**.

### Рост от низкого к высокому
**Entry уровень → Core team — это путь, не стенка.**
- Человек на entry уровне может **расти внутри Jetix**
- Через накопление достижений / track record внутри системы
- Через демонстрацию competence и result delivery
- Это **internal mobility** — но не automatic, а **earned**

### Что НЕ работает (anti-criteria для команды)
- ❌ «У меня есть деньги, возьмите в основную команду» — нет
- ❌ «У меня связи / могу привести инвесторов» — нет
- ❌ «Я готов учиться / готов работать дёшево» — для entry maybe; для core нет
- ❌ «Я закончил престижный университет» — sole credential ≠ competence
- ❌ «У меня хороший CV» — нужен реальный track record + проверка через работу
- ❌ Conflict с Pillar C Tier 1 ценностями — нет даже на entry уровне

### Сравнение 2 уровней команды

| Параметр | Low — Entry | High — Core team |
|----------|-------------|------------------|
| **Кто** | Promoters / supporters / coordinators | Operators / партнёр-relations / system builders |
| **Минимум** | Желание развиваться + базовая дисциплина + values alignment | + значимые достижения + knowledge & skills track record |
| **Что делают** | Outreach / content / admin / coordination | TRM management / partner work / platform building |
| **Финансы как пропуск** | Не релевантно | **НЕТ — недостаточно** |
| **Knowledge & skills** | Желательно | **ОБЯЗАТЕЛЬНО** |
| **Path to growth** | Через результаты внутри Jetix | Через demonstrated competence |
| **Vetting** | Базовое | Глубокое (track record + work probation) |

### Почему это важно сказать explicitly
**Если этого правила не сформулировать** — будут попытки войти в core команду через:
- Капитал («дайте мне роль за инвестицию»)
- Связи («я знаю влиятельных людей»)
- Бренд («мой опыт в Big 4 / Stanford / etc.»)

**Все 3 — отвергаются** для core team. Только **track record + knowledge + skills + values alignment**.

> *Это и есть **practical demonstration «авантюры управления»** (§6.7) — изменение того, **кому доверяют управление** в обществе. Начинаем с самого Jetix.*

---

# 8. 📊 Видение 1 / 3 / 10 лет

> **Цель раздела:** конкретные numerical milestones куда Jetix движется. **3 horizon'а** — 1 год / 3 года / 10 лет. С честным признанием что **10 лет — это уже за пределами current planning** (см. §8.3).

> **Контекст:** текущая точка (2026-05) — €5K на счету, Foundation v1.0 LOCKED, Workshop concept LOCKED, TRM model LOCKED, Phase 1 €50K Q2 2026 в процессе.

---

## 8.1 Через 1 год — середина 2027

### Ключевые числа
- **50+ клиентов** (по разным уровням TRM ladder + AI Brain on Demand transactions)
- **10+ партнёров** в платформе (Source 4 — приводят своих клиентов; см. §4.3)
- **€500K+ ARR** — это **минимум**

### Что это значит
**€500K ARR — это уже доказанная operational компания.** Не «начинающий founder», а **functioning business с repeating revenue**.

### Mix revenue для €500K ARR (примерный breakdown)
- **30-50 клиентов на L0-L1** (€3-10k за гипотезу или ретейнер) → **€150-200K ARR**
- **5-10 клиентов на L2** (€5-15k/мес — один ресурс под управлением) → **€150-250K ARR**
- **1-3 клиента на L3-L4** (€15-30k/мес — Chief of Staff / Venture Operator) → **€100-150K ARR**
- **0-1 клиент на L5 TRM-full** (€30-60k/мес) — **bonus**, если успели поднять

### Состав команды на 1 год
- Ruslan (founder)
- 3-7 человек core team (см. §7.7 — track record required)
- 5-10 supporting roles / entry уровень
- 10+ партнёров приходят со своими клиентами
- 12-15 AI агентов в активной работе

### Foundation status 1 год
- **Foundation v2.0** опубликована (improvement over v1.0 based on real usage)
- **First methodology publish** — открытая публикация одной key methodology (book / framework / workshop)
- **Track record** на 50+ клиентах = strong validation для следующих
- Public-company-style transparency — first quarterly report публично

### Главная цель Year 1
**Validation что operational model работает** — TRM ladder проходится клиентами, retention высокий, performance fees материализуются. **Это **proof point** для Phase 2 transition.**

---

## 8.2 Через 3 года — 2029

### Ключевые числа
- **€100M+ ARR** — переход в категорию **major operational corporation**
- **500+ клиентов** (по разным TRM levels)
- **20+ партнёров** в core network (deep integration через платформу)
- **Community 1000+ человек** (extended network — не все active каждый день, но curated participants)

### Что это значит
**€100M ARR — это уже категория признаваемая глобально.** Это:
- **Уровень Toptal** в их prime ($200M+ ARR)
- **Уровень premier consulting boutique** (топовые niche firms)
- **Достаточный масштаб для serious institutional credibility**

### Mix revenue для €100M ARR
- **300-400 клиентов на L1-L3** retainer + один-два ресурса под mgmt → **€60-80M ARR**
- **50-80 клиентов на L4-L5** (TRM-full / Venture Operator) → **€20-30M ARR**
- **Performance fees** на existing клиентов growth → **€10-20M ARR**
- **Платформа take rate** (early Phase 3) — Source 4 + external owners → начинает материализоваться → **€5-10M ARR**

### Состав команды на 3 года
- Founding + early team (ядро 5-10 человек)
- **30-50 человек core team** (operations / partner relations / Operators)
- **100-200 partners + extended Operators** в network
- **1000+ community members** (curated network для exchange + future Operators)
- **30+ AI агентов** активные + специализированные под domains

### Foundation status 3 года
- Foundation v3.0+ — production-grade на 1000+ users
- Multiple methodologies опубликованы — Jetix признан **methodology-leader** в AI-leverage space
- Patents (EU + select international) на ключевые processes
- **Phase 3 платформа** — early launch, take rate 15-25% начинает работать

### Главная цель Year 3
**Категориальное признание.** Jetix известен как **«AI-native operational corporation»** — новая категория business, понятная investors / journalists / клиентам / talent. **Translation cost описывать что мы делаем → почти ноль.**

### Признание в индустрии
- Покрытие в Tier 1 business media (Bloomberg / FT / Handelsblatt / etc.)
- Speaker invitations на major industry events
- Academic case studies в business schools
- Other companies copying / adapting Foundation architecture

---

## 8.3 ⭐ Через 10 лет — 2036

### Honest acknowledgement
> **Через 10 лет — мы в душе не ебём что это и как будет.**

И **это feature, не bug.**

### Почему мы НЕ описываем 10 лет конкретно
1. **Мир изменится непредсказуемо** — AI / society / business landscape transformations невозможно предвидеть
2. **Jetix будет настолько огромной**, что **текущее планирование** её **ограничивает** vs liberates
3. **Любые конкретные numbers сейчас** — это **lower bound** того что может быть, не цель
4. **Engineering-faith principle** — закладываем infrastructure для $1T scale + 200-year horizon в Phase 1, но **не пытаемся predict** конкретный путь

### Что мы знаем о 10-летнем horizon
- ✅ Будет **просто огромное и масштабное**
- ✅ Разрастётся настолько сильно, что **вообще все будут в шоке**
- ✅ Будет **сопоставимо со странами какими-то** (verbatim Ruslan, audio_496)
- ✅ Может быть **первой компанией достигшей $1T** (см. ambition § 6.11 + JETIX-VISION D19)
- ✅ Будет **новая культура / философия** для следующих поколений (см. §6.5)
- ✅ Будут **patents / IP** в нескольких domains
- ✅ Будет **multi-region presence** (не привязан к Берлину / DACH)
- ✅ Будет **trust ecosystem** где Jetix participants automatically доверяют друг другу

### Что НЕ пытаемся pin down
- ❌ Конкретное revenue number ($1B / $10B / $100B / $1T — diapason слишком широкий)
- ❌ Точное количество клиентов / партнёров (от десятков тысяч до миллионов)
- ❌ Точная корпоративная structure (может быть holding / multi-corp / DAO / unprecedented)
- ❌ География (от Europe-centered до global)
- ❌ Выход (IPO / private / token economy / hybrid)

### Стыдно даже думать
> **Verbatim Ruslan:** *«Через десять лет — настолько большое будет, что даже стыдно как-то думать, что там через 10 лет будет. Потому что настолько будет большое, что не хочется даже его текущим планированием ограничивать.»*

> **Это правильное отношение к 10y horizon.** Lock'нуть конкретный 10y plan = **artificially capping** возможности.

### Принцип: infrastructure first, scale follows
**Что мы делаем:**
- Закладываем **infrastructure для $1T scale** в Phase 1 architecture (Foundation v1.0)
- Накапливаем **methodology + knowledge + network** которые compound экспоненциально
- Поддерживаем **engineering-faith** + **public-company-style transparency**
- Растём **incrementally** через validated milestones (€50K → €500K → €100M → ...)

**Что не делаем:**
- НЕ обещаем конкретные 10y outcomes
- НЕ ограничиваем upside рамками текущего понимания
- НЕ продаём 10y vision — продаём near-term value (€3K AI Brain → L5 TRM)

---

## 8.4 Phase milestones — visible roadmap

> *Между 1y, 3y, 10y horizons — есть **promеточные milestones**.*

| Milestone | Что |
|-----------|-----|
| **Q2 2026 (now)** | €50K committed revenue (единственная **committed absolute date**) |
| **Q4 2026** | €200K validation — proof что repeating revenue работает |
| **Mid 2027 (1y)** | €500K+ ARR / 50+ клиентов / 10+ партнёров |
| **End 2028** | €5-10M ARR / Phase 2 platform начинает прорастать |
| **2029 (3y)** | €100M ARR / category recognition / Phase 3 platform launch |
| **~2030-2032** | $100M-$1B revenue / multiple regions / first patents EU |
| **~2033-2035** | $1B+ ARR / global presence / category dominance |
| **2036+ (10y)** | TBD — but huge by any measure. **Будут в шоке.** |

### Key transitions (когда фазы переключаются)
- **Phase 0 → Phase 1:** $20-30K self-funded (Q1 2026) — **прошли ✓**
- **Phase 1 → Phase 2:** €50K achieved + first 1-3 partners (Q2 2026) — **в процессе**
- **Phase 2 → Phase 3:** €5-20M ARR + 30+ established клиентов (~2028-2029)
- **Phase 3 → Phase 4 (civilizational):** TBD ambient — likely $1B+ revenue + 1000+ network

---

## 8.5 200-year horizon — civilizational legacy

> *За пределами 10 лет — есть **200-year vision** который informs current decisions, не как target, а как **direction setter**.*

### Что ставим в long horizon
> *«Долгосрочная цель Jetix — вклад в создание будущего, где базовые проблемы (голод, болезни, неравенство) решены. Микро-задача: каждый бизнес, который Jetix делает безопаснее и эффективнее через AI, — кирпичик.»*  
> [src: wiki/ideas/200-year-vision-jetix-humanity.md]

### 2 leverages в long-term
1. **AI-эффективность** — больше выходных продуктов на единицу ресурса (кумулятивно через всех клиентов / партнёров)
2. **AI-безопасность** — снижение systemic risks (cybersec, supply chain, decision quality, governance)

### Founder constitution принцип
> *«Когда система станет большой, контролировать её напрямую невозможно — поэтому ценности и предохранители закладываются ДО роста.»*  
> [src: wiki/ideas/founder-responsibility-jetix-constitution.md]

**Это значит:** Foundation v1.0 + Pillar C (Tier 2 11 hard rules) уже **закладывают safeguards** на долгосрочное development. Когда Jetix станет $100B+, эти safeguards будут active **без нужды в personal control founder'а**.

---

## 8.X Сводка видения

| Horizon | Состояние Jetix | Признание |
|---------|----------------|-----------|
| **Q2 2026 (now)** | Phase 1 finishing, €50K committed | Building, not yet recognized |
| **1 год (mid 2027)** | €500K+ ARR / 50 clients / 10 partners — **functioning business** | Industry-aware (early adopters) |
| **3 года (2029)** | **€100M+ ARR** / 500+ clients / 20+ partners / 1000+ community — **major operational corp** | **Category recognition** в Tier 1 media |
| **10 лет (2036)** | **TBD — стыдно думать** | TBD — будут в шоке |
| **200 лет** | Contributing infrastructure для civilizations 2200+ | Possibly civilizational legacy |

> **Главный вывод:** **1y и 3y — конкретные операционные цели**. **10y — engineering-faith bet** на огромную долгосрочную ценность которую не пытаемся predict, но **закладываем инфраструктуру для**. **200y — direction setter**, не target.

---

# 9. 🤝 Предложение — 3 уровня вовлечения (Партнёры / Клиенты / Работники)

> **Цель раздела:** базовое разделение трёх категорий людей которых Jetix принимает + что каждой стороне даёт + что просит. Это **первый набросок каркаса** — детали работают итеративно по мере real-world feedback.

> **Принципиально:** между этими тремя категориями граница не жёсткая. Один человек может быть **одновременно** клиентом + работником, или партнёром + клиентом. Главное — **разные роли = разные взаимоотношения** с Jetix, и каждая роль имеет свою structure.

---

## 9.1 ⭐ Уровень 1 — Партнёр (top tier — мощные наработки)

### Кто это
**Партнёр** — это **самый верхний уровень** вовлечения. Это люди у которых **уже есть очень мощные наработки**, и они приходят в Jetix не «чтобы научиться», а **с собственным капиталом ценности**.

#### Что значит «мощные наработки» (любое из перечисленного):
- 🎯 **Большая аудитория** — десятки/сотни тысяч подписчиков, собственный bandwidth для распространения
- 🛠️ **Свои инструменты / методологии** — работающие наработки которые они уже применяют
- 💰 **Реально большие ресурсы** — финансовые / материальные / связи
- 🤝 **Влияние / связи / репутация** в индустрии или сообществе
- 📚 **Track record значимых проектов** — exits / built companies / leadership roles

> **Это не «у меня есть деньги».** Это **построенный capital** в одной или нескольких категориях. Причём финансы — **не главное** (см. §7.7 — knowledge & skills > просто финансы).

### Что Jetix даёт Партнёру
- 🔑 **Доступ к управлению частью ресурсов Jetix** — financial / time / knowledge resources
- 👥 **Доступ к команде Jetix** — все 12 ролей AI-агентов + core team
- 🚀 **Все самые последние наработки** Jetix — Foundation v2.0+ / methodology library / станки
- 🤝 **Связь с другими партнёрами** уровня 1 — closed network top participants
- 🎯 **Стратегическая роль в Jetix evolution** — голос в направлении компании

### ⭐ Главное value proposition для Партнёра — Jetix как инструмент-помощник для ЕГО наработок
**Это критически важно:** Jetix **НЕ заменяет** партнёра / **НЕ забирает** его наработки. Jetix **усиливает** уже имеющиеся.

#### Конкретно — что Jetix делает с ИХ существующими наработками:
- 💸 **Помогает в монетизации их аудитории** (TRM Audience layer + new revenue streams)
- 📡 **Помогает в распространении их хороших идей** (через Jetix network + AI augmentation)
- ✨ **Помогает в улучшении их идей** (через 12 агентов + методологии + cross-pollination с другими партнёрами)
- ⚡ **Помогает в ускорении производства их идей** (Foundation infrastructure + станки + 3-5× productivity multiplier)

> **Метафора:** партнёр приходит со своим «бизнесом» — Jetix даёт ему «турбонаддув», но **его бизнес остаётся его**.

### Что Jetix просит у Партнёра

#### 1. Контрибуция в развитие Jetix
- Сваий **опыт / знания / станки / ресурсы** обратно в общую систему
- Каждый партнёр делает Jetix умнее → каждый партнёр получает выгоду от вклада остальных (compound)

#### 2. Распространение Jetix
- Партнёр распространяет факт сотрудничества с Jetix через свои каналы
- Это NOT classic referral marketing — это **organic mention** через track record / cases

#### 3. Финансовая participation (один или несколько вариантов — TBD case-by-case)
> *Варианты — пока в разработке. Ниже черновик логичных options:*

##### Вариант A — Initial investment / contribution
- Single или периодический **финансовый contribution** при входе
- Размер depending on access / leverage получаемого
- Range: €50k-500k+ initial investment / year (для top-tier партнёров)

##### Вариант B — Equity / Membership stake
- Партнёр получает **долю в Jetix** corresponding to contribution
- Вторая сторона: **долгосрочный alignment** через ownership
- Tier: «founding partner» / «founding investor» / «member»

##### Вариант C — Revenue share с проектов где Jetix участвует
- На проектах где Jetix actively contributes — Jetix берёт **% от revenue**
- Partner основной получатель, Jetix — co-receiver
- Range: 5-15% Jetix take

##### Вариант D — Performance fee on partner growth
- Если партнёр **growth'ит после** входа в Jetix — Jetix берёт **% от incremental growth**
- Аналогично TRM модели для клиентов
- Range: 10-20% от incremental

##### Вариант E — Membership fee
- Регулярная **fixed fee** за membership на платформе
- Tier-based (Light / Medium / Deep partnership)
- Range: €1k-10k/мес depending on tier

#### Гибридная модель (на практике)
**Реалистично — комбинация нескольких variants** под конкретного партнёра. Например:
- Initial investment €100k + equity 1-3% + revenue share 10% на co-projects
- Membership €5k/мес + performance fee 15% на growth
- 100% equity model для founding partners (без cash investment, но deep contribution)

> ⚠️ **Honest:** деталей финансовой модели для партнёров пока **не finalized**. Будет работать **итеративно** по мере того как первые партнёры реально подключаются и видим что работает / что нет. **Это нормально** для Phase 1-2 — структуру partnership финализируем по living examples, не upfront.

### Подтипы партнёров (preliminary)
- 🌟 **Founding Partner** — ранний партнёр большого scale, deeply integrated, equity-significant
- 🤝 **Strategic Partner** — fokусированный на one-domain (audience / capital / talent / etc.)
- 💼 **Operating Partner** — активно делает работу через Jetix infrastructure (близок к core team)
- 🏛️ **Network Partner** — основной leverage = его network / influence / reputation
- 💰 **Investor Partner** — основной leverage = capital + advisory (тогда дополнительно к knowledge & skills)

> *Эти подтипы — **black box на сейчас**. Они эволюционируют как первые партнёры подключаются и формируют real patterns.*

---

## 9.2 ⭐ Уровень 2 — Клиент

### Кто это
**Клиент** — **те кто имеют ресурсы и хотят развиваться**, но не имеют (или не интересно) построение собственного capital уровня партнёра. Они хотят **использовать наработки Jetix** для своего бизнеса / проекта / жизни.

#### Quality bar для клиента (см. §7 ICP)
- ✅ Достаточно **ресурсов** для входа (минимум для Type 1: €X финансов или Y времени)
- ✅ **Желание развиваться** + active belief in better future
- ✅ Соответствует **5 critical filter** (Startupper / Azart / Stable / Adequate / Upward)
- ✅ Готов **играть в долгую** (6-36 мес horizon)

### Что Jetix даёт Клиенту
**Прогрессивно (через Land-and-Expand ladder L0-L5):**

#### Stage 1 — Доступ к лучшим наработкам Jetix
- Foundation v2.0+ infrastructure
- 12 натренированных AI агентов
- Adaptable станки
- Knowledge base + methodology library

#### Stage 2 — Консультирование
- Strategic advisory от Jetix experts
- Plan Mode sessions для key decisions
- Methodology guidance per нужду

#### Stage 3 — Управление частью ресурсов
- Начинает с **одного ресурса** (например, время CEO или audience)
- Performance-based contracts
- AI-leverage operationally

#### Stage 4 — Расширение управления (TRM growth)
- Постепенно больше ресурсов под Jetix mgmt
- Larger leverage, deeper integration
- Eventually: TRM-full (все 6 ресурсов)

### Что Jetix просит у Клиента

#### 1. Стабильная ставка (mgmt fee)
- **Recurring monthly** — независимо от результата
- Покрывает operational cost Jetix
- Range: €3k-60k/мес (по уровню L0-L5)

#### 2. Процент от успеха (performance fee)
- **% от incremental** прибыли / роста / outcomes
- Range: 15-25% от growth attributable to Jetix
- Считается через baseline measurement

> *Подробно эта структура расписана в §3 (TRM) и §3.5 (Land-and-Expand ladder).*

### Главное отличие Клиент vs Партнёр
| Аспект | Партнёр | Клиент |
|--------|---------|--------|
| **Что приходит с собой** | Уже мощные наработки | Ресурсы + желание развиваться |
| **Зачем приходит** | Усилить свой существующий capital | Использовать Jetix для своего развития |
| **Доля в Jetix** | Возможна (equity / membership) | Нет |
| **Голос в стратегии Jetix** | Есть | Нет |
| **Платежи** | Initial / equity / membership / revenue share / performance | Mgmt fee + performance fee |
| **Cross-pollination внутри Jetix** | Активная | Indirect (через используемые tools) |
| **Минимум для входа** | Существующий capital + alignment | Ресурсы + желание + 5 critical filter |

---

## 9.3 ⭐ Уровень 3 — Работник

### Кто это
**Работник Jetix** — те кто **работают внутри Jetix**, делают платформу + работают с клиентами + развивают methodology. Это разделено на **2 уровня** (см. §7.7):

#### Низкий уровень — entry / supporting
- Желание развиваться + базовая дисциплина + values alignment
- Promo / community / content / admin / coordination

#### Высокий уровень — core team
- + значимые достижения за спиной (track record)
- + knowledge & skills (особенно НЕ просто финансы)
- TRM management / partner relations / system building

### Что Jetix даёт Работнику

#### 1. Зарплата
- **Стабильное вознаграждение** на уровне market+ для соответствующих ролей
- Может быть retainer / salary / hybrid
- Performance bonuses на key milestones

#### 2. Место для созидания (НЕ просто job)
- Работа с **реально интересными задачами**
- Доступ к **последним наработкам** + AI-leverage
- Среда где можно **глубоко расти** в своей экспертизе
- **Crewmates с track record** — работа с крутыми людьми (см. §7.7 vetting)

#### 3. Опыт + знания + connections
- Каждый проект делает работника лучше
- Network внутри Jetix + extended (партнёры / клиенты)
- Reputation в индустрии через association с Jetix

### Что Jetix просит у Работника

#### 1. Стабильная работа + execution
- Reliable delivery на assigned tasks
- Quality bar высокий (см. §7.7 — нет профанов)
- Communication через стандартные channels

#### 2. ⭐ Процент от ИХ выручки (несильно большой)
**Важная особенность:** Jetix берёт **некоторый процент** от выручки которую работник генерирует через Jetix (на проектах с клиентами / партнёрами). Но **не сильно большой** — чтобы:
- Работник мог **спокойно существовать** на остатке
- Был **stable income** база (от Jetix зарплаты)
- Сохранялся **incentive расти** (бóльшая выручка → бóльшая абсолютная сумма работнику)

**Range:** 10-25% от Jetix-attributable revenue работника (точные numbers — TBD по living examples).

### ⭐ Главный принцип — accumulation остаётся с работником

**Это критически важно — антипаттерн «корпоративного рабства»:**

> **Если работник захочет уйти / поменять деятельность — всё что он накопил остаётся с ним.**

#### Что значит «остаётся с ним» (accumulation portable):
- ✅ Полученные **навыки / экспертиза** — остаются (не «proprietary knowledge of Jetix»)
- ✅ Накопленные **personal connections** — остаются
- ✅ Личные **methodologies / frameworks** разработанные — остаются
- ✅ **Reputation built** через Jetix association — остаётся
- ✅ **Personal portfolio** of cases / examples — остаётся

#### Что НЕ остаётся (только Jetix-собственность):
- ❌ Конкретные client confidential data
- ❌ Jetix proprietary IP / patents (если где-то есть)
- ❌ Active client contracts (Jetix continues servicing them)

#### Контраст с traditional corporate
**Traditional corporate:** уходишь → теряешь доступ к knowledge / network / reputation built within. **Накопление испаряется** при exit.

**Jetix:** уходишь → **накопление остаётся**. Это и есть **антифрагильность для работника** — analogically partner Revenue Share principle (см. §6.9).

> *Это **fundamental shift** в employment relationship.* Это делает Jetix **lower risk** option для skilled people — даже если не понравится через год, **они выходят сильнее** чем входили.

### Подтипы работников (preliminary)
- 🟢 **Entry-level** — promotion / community / admin (стартовый путь, нет track required)
- 🟡 **Specialist** — узкая экспертиза в одном domain (AI / cybersec / legal / etc.)
- 🔴 **Core team / Operator** — высокий track + работа с клиентами и партнёрами
- 🔴 **Founding team** — earliest core team, deep equity / participation

---

## 9.4 Сводное сравнение 3 уровней вовлечения

| Параметр | 🌟 Партнёр | 💼 Клиент | 👷 Работник |
|----------|-----------|----------|-------------|
| **Что приходит с собой** | Существующий capital (audience / tools / resources / influence) | Ресурсы + желание развиваться | Желание развиваться + (для core) track record |
| **Зачем приходит** | Усилить existing capital через Jetix | Развиваться через Jetix infrastructure | Работать в meaningful environment |
| **Что Jetix даёт** | Доступ к Jetix resources + tools + network + усиление их идей | Access к tools → консультирование → resource management | Зарплата + место созидания + accumulation |
| **Что Jetix просит** | Contribution + распространение + finansoval participation (Initial / equity / membership / revenue share / performance) | Mgmt fee + performance fee | Execution + small % от Jetix-attributable revenue |
| **Глубина integration** | Strategic (голос в направлении) | Operational (используют сервис) | Internal (часть команды) |
| **Ownership / equity** | Может быть (equity / membership) | Нет | Может быть для founding / core team |
| **Exit пользу** | Партнёр сохраняет свои наработки + Jetix-built network | Клиент — получил value за период работы | **Работник — accumulation portable** ⭐ |
| **Размер группы Phase 2-3** | 10-50 partners | 100-1000+ clients | 30-100+ team members |

---

## 9.5 Cross-roles — один человек = несколько ролей

> *Реалистично — границы между категориями плавающие.*

### Возможные комбинации
- **Партнёр + Клиент** — у партнёра есть свой бизнес который тоже использует Jetix services
- **Партнёр + Работник** — Operating Partner / Founding Partner может одновременно работать в core team
- **Клиент + Работник** — клиент так понравилось что захотел стать частью команды (после vetting на core team criteria)
- **Работник → Партнёр** — long-term core team member может evolve в Founding Partner status через accumulated contribution

### Каждая роль — своя структура отношений
**Ключевое:** даже если человек в нескольких ролях, **каждая роль имеет свою clear structure**:
- Как Партнёр — equity / contribution / strategic voice
- Как Клиент — mgmt fee + performance
- Как Работник — salary + small % + accumulation portable

> *Это позволяет **clarity** в отношениях даже при сложных multi-role configurations.*

---

## 9.6 Process присоединения (preliminary)

> *Детали будут finalize по мере реальных examples. Сейчас — общий principle.*

### Для Партнёров
1. Initial conversation — взаимный fit assessment
2. Deep dive — capability + intentions + alignment
3. Contract structuring — выбор финансовой модели (один из вариантов A-E из §9.1)
4. Onboarding — integration в Jetix infrastructure + introduction в network
5. **Trial period 3-6 мес** — обе стороны могут exit без consequences
6. Long-term partnership — formalized через chosen structure

### Для Клиентов
1. **L0 €3k гипотеза** — initial paid engagement (минимальный risk обе стороны)
2. Если успех → **L1 retainer** (€3-10k/мес)
3. Прогрессия по TRM ladder L0-L5 (см. §3.5)

### Для Работников (Entry уровень)
1. Initial application + interview
2. Small starter task (paid) — demonstrate capability
3. 3-month probation — accumulating real work
4. Permanent role assignment

### Для Работников (Core team)
1. Track record verification
2. Deep interview по domain + values + approach
3. Reference checks через network
4. Trial project (paid, defined scope) — demonstrated competence
5. Core team integration

---

## 9.X Сводка предложения — 3 уровня

| # | Уровень | Минимум для входа | Что получает | Что даёт Jetix |
|---|---------|------------------|--------------|----------------|
| 1 | 🌟 **Партнёр** | Существующий capital (любой формы) + alignment | Доступ к Jetix resources + network + усиление их идей | Contribution + распространение + financial participation |
| 2 | 💼 **Клиент** | Ресурсы + желание развиваться + 5 critical filter | Прогрессивный access → консультирование → resource mgmt | Mgmt fee + performance fee |
| 3 | 👷 **Работник** | Желание развиваться + (core: track record + skills>finance) | Зарплата + место созидания + **portable accumulation** | Execution + small % revenue |

> **Honest disclaimer:** структура — **первый набросок**. Финансовые details (особенно для Партнёров) — будут finalize **итеративно** через первые real-world examples. Это нормально для Phase 1-2 — system эволюционирует через living patterns, не upfront design.

---

# 10. 🚀 Roadmap к $100K к концу лета 2026 (Phase 1 detailed plan)

> **Цель раздела:** конкретный operational план Ruslan'а на ближайшие месяцы — от текущей точки (созвон с Tseren) до **$100K** к концу лета 2026. Этот раздел **более personal** чем остальные (содержит конкретные имена и задачи), потому что это **operational roadmap THIS Jetix instance**, не generic concept.

> **Главный gating point:** партнёрство с мастерской инженеров-менеджеров (Левенчук / ШСМ) + обсуждение условий с Tseren или Левенчуком. **Всё остальное в roadmap — после этого partnership lock**.

---

## 10.1 ⭐ Главный stopper / question — synergy с мастерской инженеров-менеджеров

### Что нужно сделать сейчас (даже до plan execution)

**Ruslan нужно провести синергию** между:
- **Своей стороны:** амбиции / vision / Jetix concept / Foundation v1.0 LOCKED / energy
- **Стороны Tseren / Левенчук / ШСМ:** реально работающая системa / методология системного мышления / накопленные наработки

**Это НЕ "проект"** — это **fundamental enabling step**. Без него остальной roadmap не запустится с правильной energy.

### Конкретно — что сейчас на повестке
1. **Созвон с Tseren** (Tserenov) — обсуждение партнёрства / сотрудничества / совместной работы
2. **Discussion с Левенчуком** (Анатолий Левенчук, ШСМ) — обсуждение условий synergy
3. **Главный запрос Ruslan'а:** освободить личное время для:
   - Глубокого разбора в системном мышлении ШСМ
   - Внедрения всех самых последних наработок мастерской инженеров-менеджеров
   - Допиливания Jetix concept до production-grade

### Открытый вопрос условий
**Несколько возможных форматов synergy** (TBD по итогам discussion):
- Tseren / Левенчук **что-то должны** Ruslan'у (existing obligations / commitments)
- Они **инвестируют небольшие деньги** в Ruslan'а (€X на освобождение времени)
- Они дают **доступ к наработкам** в обмен на что-то от Ruslan'а
- Гибрид нескольких variants

### Ruslan position (verbatim spirit)
> *«Готов на любые условия — просто пожалуйста, увидите эту идею, дайте мне поговорить с вами, немного обучиться, немного эту систему допилить. Я быстро обучусь, а дальше приду с бабками. Соответственно продвинем эту систему далее.»*

**Промiс:** освобождение времени now → быстрая обучаемость → revenue generation в ближайшие месяцы → возврат + продвижение.

> **Это reasoning behind whole roadmap.** Без enabling synergy step — следующие фазы либо медленнее, либо менее качественно.

---

## 10.2 Step-by-step roadmap (current → конец лета 2026)

### 📅 Step 1 — Сейчас (первые дни)
**Действие:** Ruslan созванивается с Tseren / переговоры с Левенчук.

**Результат:** обсудили варианты партнёрства / сотрудничества / совместной работы / условия.

**Длительность:** 1-2 недели (depending on availability counterparts).

---

### 📅 Step 2 — Глубокий разбор + внедрение (2-3 weeks after Step 1)

**Действие:** Ruslan погружается в:
- Системное мышление ШСМ — глубокий разбор методологии Левенчука
- Внутренности самой системы мастерской инженеров-менеджеров
- **Внедрение всех последних наработок** в Jetix instance

**Параллельно:** synergy effect наработок:
- Ruslan's existing Foundation v1.0 + Workshop concept + TRM
- Левенчук's накопленные методологии + системное мышление framework
- Cross-pollination → **новый уровень обоих систем**

**Длительность:** 2-3 недели intensive.

**Результат:** Jetix instance upgraded с интеграцией ШСМ методологий; Ruslan deeply understands системное мышление; готовая база для следующих steps.

---

### 📅 Step 3 — Strategic document (1 неделя after Step 2)

**Действие:** **Совместное составление strategic документа** — Ruslan + Tseren + Левенчук.

**Что в документе:**
- Обсуждение всех scenarios партнёрства / dynamics
- Фиксация **одного "документа правды"** — clear shared understanding
- Roles + responsibilities + decision rights
- Финансовая структура synergy
- Long-term vision alignment

**Длительность:** 1 неделя focused work.

**Результат:** **Document of Truth** — single source с которого все стороны действуют.

---

### 📅 К концу первого месяца (4-6 weeks from now)

**State после Steps 1-3:**
- ✅ Обсуждено партнёрство с Tseren / Левенчук
- ✅ Latest наработки ШСМ + systemic thinking — внедрены в Jetix
- ✅ Система **уже работает** на upgraded level
- ✅ Strategic document зафиксирован
- ✅ **Ruslan имеет доступ к команде 3-5 человек** (инженеры мастерской менеджеров + энтузиасты)

> **Critical:** к этой точке у Ruslan'a **полный operational toolkit + people + clarity** для следующей фазы.

---

### 📅 Step 4 — Месяц 2-3 (work over продажи системы)

**Действие:** Ruslan + команда (3-5 человек) работают над **продажами Jetix системы / экзокортекса** другим людям.

**Target audience продажи:**
- Предприниматели (особенно большие)
- Стартапёры с амбицией
- Smart entrepreneurs с ресурсами + желанием развиваться (см. ICP §7)

**Базовые опции offering (Phase 1 product-market fit):**
1. **Решение конкретных гипотез** (€3-5k AI Brain on Demand format — см. §3.7)
2. **Установка и внедрение системы** клиенту
3. **Работа с системой** — ongoing setup / onboarding / training

**Цель:** Заработать **первые $50,000** за 1-2 месяца.

---

### 📅 Step 5 — Reinvestment (после первых $50K)

**Действие:** Полученные $50K **обратно в систему**:
- Расширение команды (наём / contracts с performing людьми)
- Улучшение infrastructure / tools
- Развитие methodology / станков

**Параллельно** — определение **what продукты делать дальше** (на основе real customer feedback, не предположений).

---

### 📅 Распределение ролей в Step 4-5

**Ruslan ответственность:**
- 📡 Distribution / распространение
- 🎯 Поиск партнёров и клиентов
- 💰 Sales motion
- 🤝 Relationship building

**Tseren / Левенчук + команда ответственность:**
- 🔧 Система / stability / infrastructure
- ⚡ Новые наработки / methodology development
- 🔬 Глубокая проработка / quality
- 🛠️ Internal R&D

> **Это complementary специализация** — Ruslan = front-office (sales / partnerships / scaling) + Tseren / Левенчук = back-office (system / quality / depth).

---

### 📅 Step 6 — К концу лета 2026 (август-сентябрь)

**Цель: $100,000 заработано.**

**Mix этих $100K (примерно):**
- $30-50K — клиенты на L0-L1 (гипотезы + аналитические retainers)
- $30-50K — клиенты на L2 (один ресурс под management)
- $10-30K — performance fees / consulting deeper

**State to end-of-summer:**
- ✅ $100K cumulative revenue
- ✅ **5-10 paying clients** (различных уровней)
- ✅ Команда 5-10 человек active
- ✅ System работает в production
- ✅ Track record — proof of concept achieved

---

### 📅 Step 7 — Strategic session после $100K

**Действие:** Снова **strategic session** — Ruslan + Tseren + Левенчук + команда:
- Анализ что работает / что нет (real data из месяца Step 4-6)
- Определение что делать дальше — какие продукты / какие markets / какая структура
- **Сборка более лучшей команды** — поиск / онбординг topа specialists
- Planning Q4 2026 / 2027

---

### 📅 Step 8 — Q4 2026+ — Ruslan all-in

**Действие:** Ruslan **все амбиции / энергию / силу** vкидывает в:
- 🔍 Поиск инвесторов
- 🎯 Поиск клиентов
- 💰 Переговоры
- 📡 Pushing distribution / partnerships
- 🚀 Подталкивание команды + всех participants

**Вся organization** mobilized для acceleration.

---

### 📅 2027-2028 — TBD

**Что будет:** **в душе не ебу пока не поговорим с Tseren / Левенчуком** + не увидим real data из 2026.

**Reasoning:** planning слишком далеко — **artificially capping** возможности. Vision §8.2 (€100M ARR через 3 года) направляет **direction**, но конкретный path Q1 2027+ — **emergent** на основе real Q4 2026 state.

---

## 10.3 Sequencing summary table

| Период | Step | Ключевое действие | Результат |
|--------|------|-------------------|-----------|
| **Now** | 1 | Созвон с Tseren / Левенчук | Обсуждены условия synergy |
| **Weeks 2-4** | 2 | Глубокий разбор + внедрение наработок ШСМ | Jetix instance upgraded |
| **Week 5** | 3 | Strategic document с Tseren + Левенчук | Document of Truth зафиксирован |
| **End of Month 1** | — | Snapshot | Система внедрена, доступ к команде 3-5 чел |
| **Months 2-3** | 4 | Продажи Jetix системы предпринимателям | **$50K заработано** |
| **After $50K** | 5 | Reinvestment в систему + команду | Стабильная operational база |
| **End summer 2026** | 6 | $100K cumulative achieved | **$100K achieved + 5-10 clients** |
| **Sep-Oct 2026** | 7 | Strategic session + сборка лучшей команды | Q4 plan + improved team |
| **Q4 2026+** | 8 | Ruslan all-in distribution / sales / fundraising | Acceleration phase |
| **2027-2028** | TBD | TBD после strategic session с Tseren / Левенчуком | TBD |

---

## 10.4 Главный gating dependency — partnership lock

> **Это критично понять:** весь roadmap **зависит от Step 1-3** (synergy с Tseren / Левенчуком).

### Если synergy запускается gracefully
- Step 4-6 идут с **boost** от ШСМ методологии + access к команде
- $100K к концу лета — **realistic**
- Foundation upgrades faster
- **Network effects starting** уже в Q3-Q4 2026

### Если synergy не запускается
- Roadmap не отменяется, но **более slow + менее resonant**
- Ruslan делает Phase 1 в основном sam + AI agents
- Возможно $100K к концу года (не лету), но достижимо
- Отсутствие методологии ШСМ = более длительный путь к категориальной clarity

> **Поэтому Step 1-3 = top priority.** Всё после — execution на уже unlocked enabling infrastructure.

---

## 10.5 Ruslan personal commitment (the asks)

> *Это secciya для honest ask потенциальным синергии-counterparts (Tseren / Левенчук / ШСМ).*

**Что Ruslan просит:**
- ⏰ Освободить **немного личного времени** (через discussion обязательств / небольшую инвестицию / подключение наработок)
- 📚 **Доступ к ШСМ методологиям** + системному мышлению фреймворку
- 🤝 **Access к команде** инженеров-менеджеров (3-5 человек на совместную работу первые месяцы)
- 💬 **Время на discussion** condition + scenarios + strategic alignment

**Что Ruslan обещает:**
- ⚡ **Быстрая обучаемость** — погружение интенсивное, не лениво
- 💰 **Возврат через revenue** — первые $50K-100K в течение 2-4 месяцев
- 📡 **Распространение** ШСМ + методологии Левенчука через Jetix network
- 🎯 **Long-term partnership** — не one-time consultation, а ongoing collaborative evolution

> *«Готов на любые условия — просто пожалуйста, увидите эту идею.»*

---

## 10.X Сводка roadmap

| Аспект | Кратко |
|--------|--------|
| **Главный stopper** | Synergy с мастерской инженеров-менеджеров (Tseren / Левенчук / ШСМ) |
| **Цель Phase 1** | $100K к концу лета 2026 (revised up от €50K) |
| **Path** | 8 steps — synergy → strategic document → команда → продажи → reinvest → $100K → strategic session → all-in Q4 |
| **Распределение ролей** | Ruslan = distribution / sales / partnerships; Tseren-Левенчук + команда = система / quality / depth |
| **2027-2028** | TBD после strategic session |
| **Long-horizon** | Не ограничивает (см. §8.3) |

> **Главный вывод:** roadmap критически зависит от **первых 4-6 weeks** (synergy unlock). После — **execution на мощной enabling base**. До — **гораздо медленнее без leverage**.

---

# 11. 💎 Синергия между участниками — почему 1+1 = 5

> **Цель раздела:** показать как **партнёры + клиенты + работники + сама Jetix** создают exponential value вместе. Это **не просто маркетинговая фраза** — это **architectural feature** Jetix, которая отличает её от любого классического консалтинга / SaaS / agency.
>
> **Главный тезис:** добавление каждого нового участника **усиливает ценность для всех остальных**. Это и есть **network effects**, но с дополнительными layer'ами cross-resource synergy уникальными для Jetix.

---

## 11.1 ⭐ Знание накапливается у всех — compound learning на network уровне

### Главный механизм
**Каждый успешный workflow одного участника → попадает в общую methodology library Jetix → доступен всем остальным участникам.**

Это **не одностороннее** «Jetix даёт knowledge клиентам». Это **двустороннее**:
- Каждый **client** (через работу с ним) генерирует insights → попадают в общую базу
- Каждый **partner** делится своими наработками → доступны remaining партнёрам
- Каждый **работник** Jetix **прокачивается** на проектах → его opыt становится template для следующих

### Конкретные mechanisms накопления

#### 1. После каждого проекта — writeback
- Что сработало → **methodology в Foundation Part 5** (Compound Learning)
- Что не сработало → **anti-pattern documented**
- Какие люди / навыки нужны → **role taxonomy update**
- Какие tools работают → **adaptable станки library update**

#### 2. После каждой стратегической сессии — synthesis
- Insights от Plan Mode sessions → **wiki/concepts**
- Новые decisions → **decisions/ log**
- Pattern recognition → **strategic insights memory**

#### 3. После каждого client engagement — case methodology
- Specific solution для client X → **abstracted methodology** для similar cases
- Через 6 months — library из 50+ methodologies для разных типов задач

### Эффект для каждой категории

#### Для Партнёра
**Twice the leverage every year.** Через 12 months network of partners — **накопленные методологии** из десятков проектов остальных. Партнёр приходит к новому challenge и **уже имеет playbook** (созданный кем-то в network ранее).

#### Для Клиента
**Receives accumulated wisdom of all предыдущих клиентов.** Когда Jetix engaged с клиентом X — он автоматически получает выгоду от learnings что Jetix вынесла из работы с клиентами 1-N до него. **Без compound** — каждый клиент платил бы за «изобретение колеса».

#### Для Работника
**Каждый проект = career acceleration.** В обычной consulting firm — работаешь над одним проектом, узнаёшь что-то узкое. В Jetix — работаешь + получаешь access к методологиям всех остальных проектов сети. **3 года в Jetix ≈ 10 лет обычного опыта**.

#### Для Jetix как системы
**Compound advantage растёт нелинейно.** Через 1 год — 2× advantage. Через 3 года — 5-10× advantage. Через 10 лет — **uncopyable moat** (никакой competitor не может за 1 год догнать 10 лет накопления реальных кейсов).

### Антифрагильность через distributed knowledge
**Если Jetix как entity исчезает** → накопленные knowledge **не пропадают** (распределены через всех participants + open methodology publishing). Это и есть **cooperation, not extraction** principle (см. §6.9).

---

## 11.2 Cross-resource synergy — для одного клиента

### Уникальная особенность TRM-структуры
**На Jetix платформе для одного клиента** работают **до 6 операторов одновременно** (по 6 ресурсам TRM):
- 💰 Финансовый operator
- ⏱️ Time / COO operator
- 📢 Audience operator
- 📚 Knowledge operator
- 💻 Compute operator
- 🤝 Talent operator

### Что они делают между собой
**Все 6 обмениваются контекстом** через единую Jetix infrastructure:
- Финансовый видит сколько Time operator потратил → лучшая cost allocation
- Audience видит какие knowledge insights publishable → новый content
- Knowledge видит patterns из Compute usage → optimisation recommendations
- Talent видит кого-кто будет нужен на основе financial trajectory
- Time operator знает приоритеты CEO → координирует загрузку остальных
- ALL 6 видят одну картину → **decisions made с full contextom**

### Что это даёт клиенту (vs single-resource управление)
| Single-resource (e.g. wealth manager только) | Cross-resource (Jetix TRM) |
|----------------------------------------------|---------------------------|
| Видит только финансы | Видит финансы + время + audience + knowledge + compute + team |
| Decision на одном измерении | Decision учитывает все 6 dimensions |
| Не знает opportunity costs other resources | Знает trade-offs между всеми ресурсами |
| Optimisation одной стороны (сomeitimes за счёт других) | **Holistic optimisation** всех 6 одновременно |
| Result: incremental improvement на 5-15% | Result: **transformational** improvement 30-100%+ |

### Главное преимущество vs Toptal / Catalant / classic firms
**Они матчат один тип отношений** (заказчик ⇄ фрилансер). Jetix матчит **6 типов ресурсов одновременно** = уникальный сетевой эффект **per client**, который **отсутствует** у single-resource marketplace.

### Anti-disintermediation эффект (из §4.6 Layer 5)
**Уход одного operator** = потеря синергии для клиента. Клиент **сам потеряет** этого operator первым (по relative value). Это **structural retention** для всей сети.

---

## 11.3 Clients ↔ Partners interactions — экосистема взаимной помощи

### Главный принцип
**Все компании-клиенты + партнёры Jetix образуют единую экосистему** — помогают друг другу, сотрудничают, объединяют отрасли.

> **Verbatim вспомогательная цитата (wiki/ideas):** *«Все компании-клиенты образуют экосистему Jetix — помогают друг другу (matchmaking, lead-share), сотрудничают (joint-products), объединяют отрасли (cross-vertical insights). Jetix владеет методологией, не отдельными контрактами.»*

### 4 типа cross-interactions

#### 1. 🔗 Matchmaking
- Клиент Jetix А **нужен** product / service который делает клиент Jetix B → Jetix matches их
- Партнёр X **ищет** investor — клиент Y готов вложить → connection через Jetix
- Operator P **ищет** новый specialist для команды — Operator Q **знает** правильного человека → handoff
- **Без Jetix** — эти connections не произошли бы (или произошли бы с low quality / random matching)

#### 2. 🤝 Lead-share
- Клиент Jetix Z **получает запросы** которые не его core business → передаёт другим клиентам Jetix через платформу
- Партнёры **получают доступ** к pool of qualified leads через сеть
- Это **превращает** «Jetix-relationship» в **источник deal flow** для каждого

#### 3. 🚀 Joint-products
- 2-3 клиента / партнёра **объединяют экспертизу** для нового offering
- Например: AI specialist + cybersec specialist + legal expert делают **«AI Compliance Bundle»** который ни один из них в одиночку не сделал бы
- Jetix berет **% от joint product** revenue (как платформа)

#### 4. 📊 Cross-vertical insights
- Клиент в **manufacturing** делится insights — клиент в **fintech** видит pattern применимый к нему
- Через Jetix wiki + community channels — **systematic cross-pollination**
- Это buy advantage больше чем sum of parts — каждый получает insights от **отраслей которые сам не покрывает**

### Quality control через trust system
**Это работает только потому что:**
- Clients / partners **vetted** через 5 critical filter (см. §7)
- Reputation system отслеживает quality каждого
- **No randoms** — закрытая curated network
- **Pillar C values alignment** обязательно для всех

> *Это и есть «**Mafia inside / Predator outside**» (см. §4.7) — внутри trust высокий, разрешает intensive collaboration.*

---

## 11.4 Network effects — почему ценность растёт нелинейно

### Базовая логика network effects
**Стандартная формула:**
- **Linear systems** (most businesses): value добавления пользователя N = constant
- **Network effects systems**: value добавления пользователя N = **функция от существующих пользователей**

### Метcalfe's Law (классический)
В networks ценность растёт **квадратично от количества пользователей** (N²) — каждый новый user может connect с N existing users.

### Jetix усиление формулы (Reed's Law)
В Jetix **ценность растёт быстрее N²** — потому что:
- **Не просто 1-to-1 connections** — **groups можно формировать** (joint projects, multi-resource clients, multi-operator engagements)
- Reed's Law формула: **2^N** для networks с group formation
- Это **экспоненциальный** growth в ценности

### Почему именно Jetix имеет этот property

#### 1. Multiple value flows одновременно
Не один тип benefit (как social network — only social), а:
- 📚 Knowledge sharing
- 🤝 Matchmaking
- 💼 Lead-share
- 🚀 Joint products
- 💎 Cross-resource synergy
- 🛠️ Methodology accumulation
- 📡 Distribution / amplification

**Каждый дополнительный participant** add'ит value **во ВСЕХ 7 потоках**, не только в одном.

#### 2. Quality gate prevents dilution
В обычных networks (LinkedIn / Facebook) — добавление **низкокачественного** user может **снижать** value для остальных (noise / spam / time-waste). В Jetix — **curated через 5 critical filter** (§7) — каждый new participant **гарантированно add'ит quality**, не отнимает.

#### 3. Compound через time
Network effects + compound learning = **многократное умножение**:
- N participants → N² connections
- N² connections × T years → **N²·T accumulated knowledge depth**
- Add quality compound on top → **uncopyable moat в 5-10 годы**

### Threshold для активации network effects
**До какого-то размера network effects не работают.** Jetix Phase 1 (10-50 participants) — value в основном **direct** (Jetix → каждый participant). **Phase 2 (100-500 participants)** — network effects начинают доминировать. **Phase 3 (1000+ participants)** — network effects становятся **главным value driver**.

### Конкретные numerical эффекты

#### Phase 1 (Year 1, ~50 clients + 10 partners + 10 workers = ~70 participants)
- N = 70
- Possible 1-to-1 connections: N² = 4,900
- Group formations: 2^N (theoretical), realistic Active groups = ~50-100
- **Value per participant** ≈ 2-3× single-resource alternative

#### Phase 2 (Year 3, ~500 clients + 20 partners + 30 workers = ~550 participants)
- N = 550
- Possible 1-to-1 connections: N² = 302,500
- Active groups (estimated) = ~500-1000
- **Value per participant** ≈ 5-10× single-resource alternative

#### Phase 3 (Year 5+, 1000+ participants)
- N = 1000+
- Connections: 1M+
- Groups: 10,000+
- **Value per participant** ≈ 10-30× single-resource alternative
- **Jetix как infrastructure** — value так высокая что становится **necessary cost of being competitive in industry**

---

## 11.5 Synergy формула — coalitionary thinking как foundation

### Verbatim Ruslan
> *«Объединить всех авантюристов в самую большую авантюру»*  
> [src: D1 Vision tagline]

> *«Капитализм → коммунизм на высоких уровнях»*  
> [src: audio_495]

> *«Jetix должна быть самой пиздатой корпорацией, но при этом за счет того, что она работает с другими самыми пиздатыми компаниями, людьми, корпорациями. Они свою пиздатость, уникальность подчеркивают, и Jetix за счет этого свою тоже уникальность.»*  
> [src: audio_488]

### Что это значит
**Jetix НЕ конкурирует** с participants — Jetix **усиливает их**. И это back-loop:
- Усиленные participants → лучшие results → лучше для Jetix reputation
- Лучшая Jetix reputation → больше top participants хотят join
- Больше top participants → ещё больше синергии
- ⮌ **Self-reinforcing loop**

### 6-component synergy формула (audio_537)
> *«эффект синергии — ответственность блять и разграничение того в чем силен в чем не силен — адекватное управление ресурсами и тогда поиск рычагов и так далее — автоматизация всего что только можно — занятия стратегическими делами видением»*

**Распакованная formula:**
1. **Ответственность** (skin-in-game всех participants)
2. **Разграничение compete'нций** (каждый делает что лучше всего умеет)
3. **Адекватное управление ресурсами** (TRM principle на network уровне)
4. **Поиск рычагов** (continuous identification leverage points)
5. **Автоматизация рутины** (free up time for important)
6. **Strategic + visionary work** (что делается с освобождённым temps)

> **Это и есть Workshop-as-engine model** на уровне сети, не одного владельца.

---

## 11.6 Сравнение synergy levels через time

| Год | Participants | Connections (N²) | Groups (Reed) | Value per participant | Jetix moat |
|-----|--------------|------------------|---------------|----------------------|------------|
| **Now (Y0)** | ~5 (Ruslan + early team) | 25 | ~5-10 | 1.5-2× single | None yet |
| **Y1** | ~70 (50 cl + 10 pt + 10 wk) | 4,900 | 50-100 | 2-3× single | Early advantage |
| **Y3** | ~550 (500 cl + 20 pt + 30 wk) | 302,500 | 500-1,000 | 5-10× single | **Category leader** |
| **Y5** | ~1,500 | 2,250,000 | 5,000-10,000 | 10-20× single | Strong moat |
| **Y10** | ~10,000+ | 100,000,000+ | 100,000+ | **20-50× single** | **Uncopyable moat** |

> **Y10 — value per participant 20-50× single-resource alternative.** Это означает что **не быть в Jetix через 10 лет** = **competitive disadvantage 20-50×** vs быть в Jetix.

---

## 11.7 Anti-paterns synergy (что разрушает её)

### Что мы НЕ позволяем

#### ❌ Внутренние competitors
**Один participant конкурирует с другим за тот же ресурс / клиента / market.** Это убивает trust + создаёт internal political games.

**Решение:** non-compete sectoring (1 participant per industry для conflicting cases) + chinese walls для информации.

#### ❌ Free-riding
**Кто-то получает knowledge / leads / value от network — не contributes back.** Через 6-12 months это становится visible (нет contributions в methodology library / нет участия в group projects / низкий reputation score).

**Решение:** quality monitoring + потенциальный exit для chronic free-riders. Quality > quantity.

#### ❌ Dilution через mass entry
**Открытие платформы для всех желающих** = noise + low quality entries dragging value down.

**Решение:** **Curated access** через 5 critical filter. **Closed network до Phase 3**, потом **gradual opening** с входным фильтром.

#### ❌ Information hoarding
**Participant скрывает свои insights чтобы сохранить advantage.** Это short-term win, long-term lose (network effect breaks).

**Решение:** Open source / Linux philosophy embedded в Pillar C values (sharing > hoarding).

#### ❌ Disintermediation от платформы
**Operator находит клиента через Jetix → договаривается напрямую мимо платформы.** (Описано подробно §4.6)

**Решение:** 7 layer защита (см. §4.6) — особенно low take rate (15-25% vs Toptal 35-50%).

---

## 11.X Сводка синергии

| Источник синергии | Mechanism | Кому benefit | Эффект |
|-------------------|-----------|--------------|--------|
| **Knowledge accumulation** | Каждый проект → methodology → доступна всем | Все participants | Through time: 5-10× advantage |
| **Cross-resource synergy** (per client) | До 6 operators обмениваются контекстом для одного клиента | Клиенты | Holistic optimisation 30-100%+ |
| **Clients ↔ Partners interactions** | Matchmaking / lead-share / joint products / cross-vertical insights | Все participants | Deal flow + new product opportunities |
| **Network effects** (Reed's Law) | Group formations растут как 2^N | Все participants | Exponential value growth |
| **Coalitionary thinking** | Jetix усиливает participants, не конкурирует | Все participants + Jetix | Self-reinforcing loop |
| **6-component synergy formula** | Responsibility / specialization / TRM / leverage / automation / strategy | Все participants | Workshop-as-engine на network уровне |

> **Главный вывод:** synergy в Jetix — **не маркетинговое заявление, а structural feature**. Mathematics network effects + curated quality + cross-resource architecture делают её **inevitable** через достаточное время. Это и есть **главный moat** который **не может быть скопирован** competitor'ами «за счёт денег / scale» — он **накапливается** через **years of curated participation + compound learning**.

---

# 12. ⚠️ Anti-patterns Jetix Corp (что мы НЕ есть)

> **Цель раздела:** explicit отграничение от похожих но не тех концепций.

## 12.1 НЕ classic consulting firm
*[Pricing / structure / value delivery — отличия.]*

## 12.2 НЕ AI стартап с продуктом
*[Мы не продаём software / API / SaaS как main offering.]*

## 12.3 НЕ holding company
*[Мы не покупаем компании. Мы помогаем владельцу управлять.]*

## 12.4 НЕ accelerator / incubator
*[Не тренинг для founders. Мы реальный operational partner.]*

## 12.5 НЕ управляющая компания типа BlackRock
*[Не управляем investment portfolio. Управляем operational resources Mittelstand.]*

---

# 📎 Appendix

## A. 📚 Источники этого документа
*[Будет заполнено по мере написания.]*

## B. 🔗 Связанные документы
- **Документ 1A** — `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` — universal foundation
- **Workshop concept LOCKED** — `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`
- **TRM model LOCKED** — `decisions/JETIX-TRM-MODEL-2026-04-30.md`
- **Vision Fundamental** — `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`

## C. 📖 Глоссарий
*[Будет заполнено в конце. Термины Jetix-specific: TRM / L0-L5 / Mittelstand / fork Foundation / etc. Generic термины — см. Документ 1A Appendix C.]*

## D. 📅 Changelog документа

| Дата | Версия | Что |
|------|--------|-----|
| 2026-05-05 | v0.1 | Skeleton создан — 12 разделов, frontmatter, audience guide, links на parent (Документ 1A) |
| TBD | v0.2 | Раздел 1 (Что такое Jetix) — Ruslan диктует |
| TBD | ... | Дальше по разделам по такой же логике как 1A |
| TBD | v1.0 | TL;DR + final review → **LOCK** |

---

**Status:** SKELETON v0.1, ожидает наполнения content по диктовке Ruslan'a.

**Workflow:** идём по разделам в логике Ruslan'a, я записываю + структурирую + предлагаю улучшения. AI = scribe для strategic docs (per memory `feedback_ai_is_scribe_not_author_for_strategic_docs.md`).

**Estimated length when complete:** ~1500-2500 строк.

**Parent reference:** Документ 1A — `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` (LOCKED v1.0 2026-05-05).
