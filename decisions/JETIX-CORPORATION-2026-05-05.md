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

#### 🤝 Mentor Search Pipeline
Отдельный workstream для unlock'а Phase 0 isolation as stopper class (`swarm/wiki/operations/quick-money/personal-mentor-search/`).

#### 📚 Methodology Publishing Pipeline
Pipeline для конвертации накопленной internal methodology → publishable artifacts (Phase 2+).

#### 🪙 Token Economy Layer
Phase 2 internal / Phase 3+ public — alternative-to-IPO liquidity path. Trigger: $100K self-earned.

#### 📅 Tseren Tserenov Outreach Track
Specific dedicated workflow (Phase 1 → 2 first transition partnership).

#### 🌐 Cross-Workshop Communication Protocol
Phase 3+ станок — стандарт communication между мастерскими в community (TRM Network platform layer).

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

> **Цель раздела:** описать центральный business offering Jetix — TRM модель.

## 3.1 Что такое TRM
*[Total Resource Management — Jetix управляет 6 категориями ресурсов клиента: 💰 Финансы / ⏱️ Время CEO / 📢 Аудитория / 📚 Знания / 💻 Compute / 🤝 Команда. Mgmt fee + performance fee.]*

## 3.2 6 ресурсов в деталях
*[Для каждого: что именно делается, какие deliverables, какой outcome.]*

## 3.3 Бизнес-модель — fees
*[Mgmt fee (recurring monthly) + performance fee (% от результата). Уровни L0-L5 от €3K/мес до €40-60K/мес.]*

## 3.4 Unit economics
*[На какие numbers смотрим: customer acquisition cost / lifetime value / margin / capacity per Ruslan-equivalent.]*

## 3.5 Сравнение с альтернативами
*[Vs traditional consulting / vs SaaS / vs management consulting / vs interim CEO.]*

---

# 4. 🌐 Платформа для проектов — partners ecosystem

> **Цель раздела:** описать Phase 2-3 видение — Jetix как платформа на которой партнёры запускают свои проекты.

## 4.1 Зачем нужна платформа партнёрам
*[Почему партнёр должен присоединиться к Jetix vs строить своё. Compound learning / shared infrastructure / synergy.]*

## 4.2 Кто потенциальные партнёры
*[Профили: solo founder с своей экспертизой / advisor / coach / consultant с маленьким practice / etc.]*

## 4.3 Как технически работает (fork Foundation)
*[Партнёр получает fork Foundation v1.0 (canonical 11 Parts + Pillar C). Накладывает свою RUSLAN-LAYER специфику. Подключается к shared Jetix infrastructure.]*

## 4.4 Какие проекты партнёры могут делать
*[Свои consulting practices / свои клиенты / свои specializations / cross-collaboration с другими партнёрами.]*

---

# 5. 🤝 Управляющая компания

> **Цель раздела:** объяснить что Jetix не только консультирует, но и реально управляет частью ресурсов клиента.

## 5.1 Что значит «управляющая»
*[Не просто советы — реальное управление частью ресурсов клиента (с его согласия). Like Berkshire Hathaway но для Mittelstand operations.]*

## 5.2 Типы управления
*[Финансами / временем CEO / аудиторией / etc. Разные depth levels.]*

## 5.3 Юридическая структура
*[Как оформляется управление. Контракты / authority / boundaries.]*

## 5.4 Trust building
*[Как мы строим trust с клиентом чтобы он отдал управление частью ресурсов.]*

---

# 6. 🧪 Большая афёра века / Эксперимент

> **Цель раздела:** честно описать что Jetix — это в значительной степени эксперимент / афёра века. Без претензии что мы 100% знаем что делаем.

## 6.1 Что значит «афёра века»
*[Не negative connotation — это честное признание масштаба амбиции. Мы пытаемся построить что-то чего никто ещё не делал.]*

## 6.2 Что именно тестируется
*[Гипотезы: AI-native operational company / Total Resource Management as service / partner ecosystem / etc.]*

## 6.3 Что если не получится
*[Честный fallback: что мы выносим даже из failed experiment. Накопленный knowledge / methodology / network.]*

## 6.4 Что если получится
*[Trajectory €50K → €500K → €5M → €50M+ revenue / Mittelstand transformation / новая категория бизнеса в DACH.]*

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

# 8. 📊 Видение 1 / 3 / 10 лет

> **Цель раздела:** где Jetix через год / 3 года / 10 лет.

## 8.1 Через 1 год (середина 2027)
*[€50K achieved → €100-300K ARR / 3-5 клиентов / 1-2 партнёра / Foundation v2.0 / first methodology publish.]*

## 8.2 Через 3 года (2029)
*[€1-5M ARR / 15-30 клиентов / 5-10 партнёров / community 50-200 people / признание в DACH consulting space.]*

## 8.3 Через 10 лет (2036)
*[€50M+ ARR / категория «AI-native operational corp» признана / multi-region / patents / Trust ecosystem.]*

## 8.4 Через 10 лет — экспериментальный сценарий
*[Что если получится действительно big — €1T trajectory. Как может выглядеть Jetix как infrastructure для нового способа делать business в Европе.]*

---

# 9. 🤝 Предложение партнёрам

> **Цель раздела:** для тех кто рассматривает партнёрство — что мы даём, что просим.

## 9.1 Что Jetix даёт партнёру
*[Foundation infrastructure / shared knowledge / cross-collaboration / leads / tools / community.]*

## 9.2 Что Jetix просит у партнёра
*[Commitment level / contribution / values alignment / etc.]*

## 9.3 Типы партнёрств
*[Light / medium / deep partnership tiers. Что входит в каждый.]*

## 9.4 Как присоединиться
*[Process / criteria / next steps.]*

---

# 10. 🚀 Roadmap к €50K → €1T trajectory

> **Цель раздела:** конкретные шаги.

## 10.1 Q2 2026 — €50K первые
*[Конкретный план до 30.06.2026.]*

## 10.2 H2 2026 — продуктизация
*[Что делаем после первой выручки.]*

## 10.3 2027 — масштабирование
*[Партнёры / больше клиентов / first methodology publish.]*

## 10.4 2028+ — категория
*[Превращение в признанную категорию.]*

---

# 11. 💎 Синергия между участниками

> **Цель раздела:** как партнёры + клиенты + Jetix создают exponential value вместе.

## 11.1 Знание накапливается у всех
*[Compound learning effect не только у Jetix, но у всей сети.]*

## 11.2 Clients ↔ Partners interactions
*[Как клиенты могут получать ценность от других партнёров.]*

## 11.3 Network effects
*[Почему ценность растёт нелинейно с ростом сети.]*

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
