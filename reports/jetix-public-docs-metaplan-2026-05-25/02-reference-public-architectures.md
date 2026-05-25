---
title: Phase 1 — Референсные публичные информационные архитектуры (как у других)
date: 2026-05-25
type: phase-report
phase: 1
parent_prompt: prompts/jetix-public-docs-metaplan-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F3
G: prompt-jetix-public-docs-metaplan-phase-1
constitutional_posture: R1 surface only + R6 + R11; F3 reference general knowledge (NO new external research)
language: russian primary
---

# 🏛️ Phase 1 — Как устроены публичные сайты у других (IA-референс)

> **Что это.** Phase 7 substrate (`08-reference-corps.md`) смотрел на **набор документов**
> у корпораций. Здесь другой угол — **информационная архитектура публичного сайта**: сколько
> разделов верхнего уровня, по какой логике разбито, в каком порядке человек читает, что
> открыто, а что за «дверью» (gated). Это F3 — общие знания, без нового внешнего research.
>
> **Зачем.** Чтобы 3 варианта структуры в Phase 2 опирались на проверенные паттерны, а не
> изобретались с нуля. У каждого референса — свой урок для Jetix.

---

## §1 Семь референсов — IA на пальцах

### 🔵 Anthropic — «исследования → продукт → ответственность → компания»
- **Top-level (≈5-6):** Research · Claude (продукт) · API/Developers · Safety/Policy · Company · (Careers).
- **Логика разбиения:** по **зрелости отношений** — сначала «во что мы верим» (Research + Core Views), потом «что можно потрогать» (Claude/API), потом «как мы это держим безопасно» (RSP/ASL), в конце «кто мы» (Company).
- **Narrative flow:** миссия/взгляды → продукт → безопасность → команда. Safety не спрятана — вынесена в топ как часть оффера.
- **Public vs gated:** почти всё public (research papers, RSP, core views); gated — только API-ключи и enterprise-контакт.
- **Урок для Jetix:** **safety/принципы выносим в топ, а не прячем** — резонирует с R12 как публичным обещанием. «Core views» = наш Vision/FUNDAMENTAL-для-людей.

### ⚡ Tesla — «продукт впереди, миссия отдельным манифестом»
- **Top-level (≈4-5):** Vehicles/Models · Energy · Charging · Discover (about/careers) · Shop.
- **Логика:** по **линейкам продукта**, не по аудитории. Миссия живёт отдельным жанром — публичный **«Master Plan»** (part 1/2/3), редкий формат «вот наша долгосрочная стратегия открыто».
- **Narrative flow:** продукт сразу → манифест опционально для тех, кто хочет «зачем».
- **Public vs gated:** всё public; конфигуратор/заказ — мягкий gate (нужен аккаунт).
- **Урок для Jetix:** **публичный «Master Plan»** как отдельный жанр манифеста (у нас есть substrate — STRATEGIC-PLAN + видение, но не в публичном жанре). Открытость части IP (Tesla открыла патенты) ↔ наш open-surface/closed-core.

### 🍎 Apple — «по продуктовым линиям + поддержка отдельно»
- **Top-level (≈6-7):** Mac · iPhone · iPad · Watch · Services · Support · (Store).
- **Логика:** по **продуктовым семействам**; единый brand-язык поверх всего; глубина (tech specs, HIG, developer docs) уходит на под-уровни и в отдельный поддомен (developer.apple.com).
- **Narrative flow:** витрина-эмоция сверху → tech specs по клику → developer/API в отдельной зоне для своих.
- **Public vs gated:** маркетинг public; developer-глубина — отдельный слой (не gated, но «для тех, кто ищет»).
- **Урок для Jetix:** **слой глубины отделён от витрины** — обычный человек видит эмоцию и суть, методолог проваливается в спеки. Прямой аргумент за слой-разделение (Вариант C по аудиториям).

### 🟢 OpenAI — «research / product / safety / company»
- **Top-level (≈4-5):** Research · Products (ChatGPT/API) · Safety · Company · (Pricing).
- **Логика:** почти зеркало Anthropic — по **функциональным блокам**. Charter (про миссию AGI) — отдельный якорный документ.
- **Narrative flow:** research → продукт → safety → кто мы; Charter как «конституция» в Company.
- **Public vs gated:** research/charter public; API/pricing — мягкий gate.
- **Урок для Jetix:** **Charter как отдельный публичный якорь** — у нас Charter рычажный (8/12 сущностей), его можно сделать публичным «конституционным» документом.

### 🤝 Mondragón ⭐ (главный кооп-референс) — «about → опыт → сектора → знание»
- **Top-level (≈4-5):** About us (кто мы / принципы) · Cooperative experience (как устроено членство/governance) · Sectors/Business areas · Knowledge (University/research) · (Contact).
- **Логика:** по **сущностям кооператива** — отдельно «принципы и ценности», отдельно «кооперативный опыт» (10 принципов, 1-член-1-голос, social fund), отдельно бизнес-сектора, отдельно образовательное крыло.
- **Narrative flow:** ценности/принципы **впереди** → как это работает (членство, governance) → что мы делаем (сектора) → как учим (университет).
- **Public vs gated:** принципы и модель — public; членские документы (agreement, capital accounts) — для членов.
- **Урок для Jetix (главный):** **кооперативные принципы и модель денег — публичны и впереди**; членский Charter — за порогом вступления. Прямой каркас для разделения «публичное обещание R12 / членский Charter».

### 🏪 John Lewis Partnership — «about → партнёрство → бренды»
- **Top-level (≈3-4):** About us · Our Partnership (Constitution + как работает employee-ownership) · Our brands · (Careers/News).
- **Логика:** **«Partnership» вынесена в отдельный топ-раздел** — публичная Constitution (7 принципов, «happiness of all members»), records совета, bonus policy.
- **Narrative flow:** кто мы → **как устроено совладение** (это их отличие, поэтому впереди) → что продаём.
- **Public vs gated:** Constitution полностью public — это часть бренда «мы партнёрство».
- **Урок для Jetix:** **публичная Constitution = часть идентичности**, не юридический мелкий шрифт. Наш Charter может быть публичным манифестом отношений, как у John Lewis.

### 💳 Stripe — «по аудитории-задаче + developers + ресурсы»
- **Top-level (≈5-6):** Products · Solutions (по индустрии/задаче) · Developers (docs) · Resources · Pricing · Company.
- **Логика:** двойная — **по продуктам** И **по решениям-под-задачу** (Solutions = «ты кто и что хочешь»); developer-docs — мощный отдельный столп (их главное конкурентное преимущество).
- **Narrative flow:** «что у нас есть» (Products) ИЛИ «реши мою задачу» (Solutions) → developers ныряют в docs → pricing → company.
- **Public vs gated:** docs/pricing полностью public (это стратегия Stripe — открытая дока продаёт); аккаунт — gate на дашборд.
- **Урок для Jetix:** **двойной вход** — можно зайти «по продукту» или «по своей роли/задаче». И **открытая дока/шаблоны как часть оффера** (наши Notion-шаблоны = аналог Stripe docs).

---

## §2 Сводка паттернов IA (что повторяется)

| Паттерн | У кого | Урок для Jetix |
|---|---|---|
| **3-6 разделов верхнего уровня** (не больше) | у всех | публичный набор Jetix = **3-6 главных документов/разделов**, не 94 |
| **Принципы/safety/миссия впереди, не спрятаны** | Anthropic, OpenAI, Mondragón, John Lewis | R12-обещание + Видение = в топе, часть оффера |
| **Витрина отделена от глубины** | Apple, Stripe | слой для любопытного ≠ слой для методолога (аргумент за Вариант C) |
| **Манифест/Master Plan как отдельный жанр** | Tesla, OpenAI Charter | публичный Vision/Master-Plan-док — отдельная страница |
| **Членское/governance — за порогом, публичны только принципы** | Mondragón, John Lewis | публичное R12-обещание ≠ членский Charter (gated за вступлением) |
| **Вход «по продукту» ИЛИ «по роли/задаче»** | Stripe | возможен гибрид: и направления (Вариант A), и воронка (Вариант B) |
| **Открытые docs/шаблоны продают** | Stripe, Apple HIG | Notion-шаблоны и метод-гайд — публичный актив, а не секрет |

---

## §3 Три способа разбить, которые подсказывают референсы

Референсы кластеризуются в **три логики разбиения** — и это ровно три варианта Phase 2:

1. **По сущностям/направлениям** (Apple по продуктам, Mondragón по кооп-сущностям, Tesla по линейкам) → **Вариант A**.
2. **По воронке/пути** (Anthropic/OpenAI: research→продукт→safety→company как путь доверия; John Lewis: кто мы→как устроено→что делаем) → **Вариант B**.
3. **По аудитории/задаче** (Stripe Solutions; Apple витрина-vs-developer; Mondragón публичное-vs-членское) → **Вариант C**.

То есть три варианта в Phase 2 — **не выдуманы**, а сняты с трёх реальных способов, которыми
организуют публичную информацию зрелые компании. Гибрид (Вариант D) — тоже наблюдается живьём
(Stripe = продукты + solutions одновременно).

---

## §4 Что Phase 1 даёт следующим фазам

- **Кап 3-6 разделов** → дисциплина для всех вариантов в Phase 2 (не плодим).
- **3 логики разбиения** → прямые каркасы Вариантов A/B/C.
- **«Принципы впереди» + «публичное ≠ членское»** → как раскладывать R12/Charter/Vision (Phase 3).
- **«Витрина vs глубина»** → entry points для 3 персон (Phase 4).

---

*Phase 1 closure. 7 референсов по углу публичной IA (Anthropic / Tesla / Apple / OpenAI /
Mondragón / John Lewis / Stripe): top-level разделов, логика разбиения, narrative flow,
public vs gated. 7 повторяющихся паттернов. 3 логики разбиения → каркасы Вариантов A/B/C +
гибрид D. F3 general knowledge, NO new external research. R1 surface.*
