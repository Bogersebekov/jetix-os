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

## 4.3 3 источника проектов на платформе

> *Это критическая особенность — платформа не просто marketplace. У неё 3 источника входящих проектов.*

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

> **Главная фишка:** партнёры на платформе **получают доступ к проектам всех 3 источников**. Это **существенно больше deal flow** чем у solo professional.

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
