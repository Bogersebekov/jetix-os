---
title: Phase 5 — ⭐ Layer 4 Universal Business Foundation Template (fork-able generic + Jetix optional overlay)
date: 2026-05-25
type: phase-report-layer-4-spec
parent_prompt: prompts/notion-templates-4-layers-architecture-2026-05-25.md
parent_main: decisions/strategic/NOTION-TEMPLATES-4-LAYERS-ARCHITECTURE-2026-05-25.md
phase: 5
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-notion-templates-4-layers-architecture-2026-05-25
R: low
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only + no-sample-data
language: russian primary
layer: 4
roy_dispatch: [mgmt-expert, investor-expert, engineering-expert, systems-expert, sota-tracker]
roy_auto_fire: [influence-ethics, recruitment-dynamics]
---

# Phase 5 — ⭐ Layer 4: Universal Business Foundation Template

> **🚨 КРИТИЧНО — scope.** Layer 4 = **универсальный fork-able foundation для управления ЛЮБЫМ
> бизнесом** (консалтинг / SaaS / продукт / агентство / кооператив / любой). Это **базовый
> skeleton**, который любой founder/executive копирует → адаптирует под свой бизнес. Generic,
> НЕ Jetix-specific. У каждой базы — **extension points** (что добавить под конкретный кейс).
>
> Jetix-специфика (R12 / Mondragón 5:1 / 4 LOCKED / Charter / 10 ролей / 4 монетизации /
> Stage Gates / Ethereum) = **СЕПАРАТНЫЙ OPTIONAL OVERLAY** (§5.X в конце). Не часть base. Один
> пример из многих возможных overlay'ев.
>
> **Per Ruslan voice 25.05:** «шаблон-фундамент, на который люди могут наслаивать… fork-able…
> на базовом уровне описано, но с конкретными дописями, что можно добавить».
>
> **Тон base — универсальный business template**, а не «вот наша корпорация Jetix».
> Generic base §5.1-§5.12 ≥5-6K + Jetix overlay §5.X ≥2-3K. NO sample data.

---

## §5.0 Обзор Layer 4: 12 групп баз + дашборд

Layer 4 — это **executive operating system**: founder видит весь бизнес с одной страницы и
управляет им. 12 функциональных групп баз, объединённых в Executive Command Center.

| # | Группа | Назначение (one-liner) | Ядро/опц |
|---|---|---|---|
| §5.1 | 🎯 **Strategy & Goals** | куда идём + по какой метрике мерим | ядро |
| §5.2 | 💰 **Financial Overview** | сколько денег / сколько горим / сколько осталось | ядро |
| §5.3 | 👥 **Team / People** | кто в команде + кто за что отвечает | ядро |
| §5.4 | 🚀 **Projects Portfolio** | что делается + на какой стадии | ядро |
| §5.5 | 🤝 **Stakeholders / CRM lite** | клиенты / партнёры / инвесторы | ядро |
| §5.6 | ⚖️ **Decisions Log** | что решили + почему + чем кончилось | ядро |
| §5.7 | 🛡️ **Risks Register** | что может пойти не так + что делаем | опц |
| §5.8 | 📜 **Compliance & Legal** | юр / договоры / комплаенс | опц |
| §5.9 | 🧰 **Tools / Resources** | чем работаем + сколько стоит | опц |
| §5.10 | 📚 **Documents / Knowledge Hub** | где что лежит | опц |
| §5.11 | 📊 **Executive Briefing** | ежедневный/недельный обзор для founder | ядро |
| §5.12 | 🚨 **Crisis Mode Playbook** | что делать, когда всё горит | опц |

**Минимум для старта (founder за 2-3 часа):** §5.1 + §5.2 + §5.4 + §5.11 (стратегия + деньги +
проекты + брифинг). Остальное наслаивается по мере роста бизнеса.

**Принцип extension points:** каждая база описана как **generic скелет** + список «если у тебя
X-бизнес → добавь поля Y». Base без extension'ов работает; extension'ы — под конкретику.

---

## §5.1 🎯 Strategy & Goals (generic)

**Назначение.** Куда идёт бизнес и по какой метрике мерим. **Framework-agnostic** — база не
навязывает OKR; каждый бизнес выбирает свой фреймворк (OKR / V2MOM / Hoshin Kanri / EOS Rocks /
любой). База даёт универсальный слот «цель → метрика → owner → горизонт».

**База Vision/Mission:**

| Поле | Тип | Назначение |
|---|---|---|
| Statement | Title | формулировка vision/mission |
| Kind | Select | vision / mission / value |
| Last revised | Date | дата ревизии |
| Owner | Relation → People | кто отвечает |
| Review cadence | Select | quarterly / annual |

**База Goals (universal):**

| Поле | Тип | Формула/дефолт |
|---|---|---|
| Title | Title | — |
| Type | Select | annual / quarterly / monthly |
| Target metric | Text/Number | целевое значение |
| Current state | Number | текущее |
| Progress % | Formula | `prop("Current")/prop("Target")*100` |
| Owner | Relation → People | — |
| Horizon | Date | срок |
| Status | Select | on-track / at-risk / off-track / done |
| Health | Formula | `if(prop("Progress")>=expected,"🟢", if(...,"🟡","🔴"))` |
| Linked projects | Relation → Projects | — |

**Views:** Current quarter, By owner, At-risk (`Status=at-risk/off-track`), Annual roadmap (timeline).

**Extension points:**
- *Если OKR* → добавь поля Objectives + Key Results (KR1-KR3, числовые, confidence 0-1).
- *Если V2MOM* → добавь Values / Methods / Obstacles / Measures.
- *Если EOS/Traction* → добавь Rocks (квартальные) + scorecard метрик.
- *Если industry-specific* → добавь категории целей (продуктовые / sales / operational / people).

---

## §5.2 💰 Financial Overview (generic)

**Назначение.** Денежная картина бизнеса: доход / расход / runway / прайсинг / счета.

**База Revenue (per income stream):**

| Поле | Тип | Дефолт |
|---|---|---|
| Stream name | Title | — |
| Category | Select | services / product / subscription / other (generic) |
| Amount | Number (currency) | — |
| Period | Date | — |
| Status | Select | invoiced / received / projected |
| Customer | Relation → Stakeholders | — |

**База Expenses (per category):**

| Поле | Тип |
|---|---|
| Name | Title |
| Category | Select (operating / hr / tools / marketing / other) |
| Amount | Number |
| Period | Date |
| Recurring? | Checkbox |
| Vendor | Relation → Stakeholders |

**Cash flow + runway (dashboard formulas):**
- Current cash (manual или rollup) / Monthly burn (rollup recurring expenses) / **Runway months**
  = `prop("Current cash") / prop("Monthly burn")` → подсветка 🔴 если < 3.
- Budget vs Actuals view — group by Category, rollup planned vs actual.

**База Pricing tiers (если applicable):** Tier name / Price / Billing period / Features / Target
segment — generic структура tiered pricing.

**База Invoices (universal):** Number / Customer / Amount / Issue date / Due date / Status
(draft/sent/paid/overdue) / Overdue? (formula `Due<now & Status!=paid`). Структура SEPA-ready /
US-invoice — generic.

**Views:** This month P&L, Runway dashboard, Outstanding invoices, Revenue by stream.

**Extension points:**
- *Cooperative бизнес* → добавь Mondragón ratio check formula (highest/lowest comp ratio).
- *VC-funded* → добавь cap table tracking (round / investor / equity % / valuation).
- *Multi-currency* → добавь currency + conversion rate.
- *Crypto/tokenized* → добавь wallet tracking + on-chain tx.

**(investor-expert lens):** runway < 6 мес = критический сигнал в §5.11 брифинг; unit-econ
паттерн (revenue per customer / CAC / LTV) — добавляется как extension под sales-heavy бизнес.

---

## §5.3 👥 Team / People (generic)

**Назначение.** Кто в команде + кто за что отвечает. **Governance-agnostic** — структура
(иерархия / плоская / матрица) выбирается бизнесом.

**База Members (universal):**

| Поле | Тип | Дефолт |
|---|---|---|
| Name | Title | — |
| Role | Relation → Roles | — |
| Start date | Date | — |
| Status | Select | active / onboarding / paused / past |
| Contact | Text | — |
| Responsibilities | Text | — |
| Reports to | Relation → Members | — |

**База Roles (universal role library — НЕ привязан к 10 Jetix ролям):**

| Поле | Тип |
|---|---|
| Role title | Title |
| Responsibilities | Text |
| KPIs | Text |
| Decision rights | Text |
| Reports to | Relation → Roles |
| Comp band | Text (опц.) |

**Org structure visualization:** hierarchical (reports-to chains) ИЛИ flat ИЛИ matrix — user
picks через relation Members.Reports-to.

**Views:** Active team, By role, Org chart (через reports-to), Onboarding pipeline.

**Extension points:**
- *Cooperative governance* → добавь ratio enforcement + Steward role + ротация.
- *Traditional hierarchy* → добавь reporting chains + spans of control.
- *Multi-hat (IP-1 separation)* → добавь role-vs-person matrix (один человек = несколько ролей;
  разделение роли-контейнера и исполнителя).

**(IP-1 generic применение):** даже в generic base полезно различать Roles (контейнеры) и Members
(исполнители) — это снимает «незаменимость человека X» и облегчает передачу обязанностей.

---

## §5.4 🚀 Projects Portfolio (generic)

**Назначение.** Что делается + на какой стадии. Высокоуровневый портфельный взгляд (отделён от
детального проектного трекинга команды Layer 3).

**База Projects (universal):**

| Поле | Тип | Дефолт |
|---|---|---|
| Name | Title | — |
| Type | Relation → Project Types | — |
| Status | Select | proposed / active / paused / done / killed |
| Stage | Select (generic) | early / mid / late / wrap |
| Owner | Relation → People | — |
| Team | Relation → People (multi) | — |
| Start | Date | — |
| Target end | Date | — |
| Actual end | Date | — |
| Health | Formula | по срокам/бюджету → 🟢🟡🔴 |
| Linked goals | Relation → Goals | — |

**База Project Types (user defines):** consulting / product / research / internal / etc.

**Views:** Portfolio timeline, Board by stage, By owner, At-risk projects, Active vs done.

**Extension points:**
- *Если Stage Gates* → добавь SG-1/SG-2/SG-3/SG-4 fields + predicate fields.
- *Если Agile/Scrum* → добавь sprint / velocity / backlog relation.
- *Project-based revenue* → добавь project value / margin / billed amount → rollup в §5.2.

---

## §5.5 🤝 Stakeholders / Customers / Partners (generic CRM lite)

**Назначение.** Универсальный CRM lite (отделён от deep CRM в Layer 1+2): клиенты / партнёры /
инвесторы / советники / вендоры.

**База Contacts (people + orgs, universal):**

| Поле | Тип | Дефолт |
|---|---|---|
| Name | Title | — |
| Kind | Select | person / org |
| Type | Select | customer / partner / investor / advisor / vendor / other |
| Status | Select | lead / active / paused / past |
| Engagement health | Select | strong / ok / weak |
| Last touch | Date | — |
| Days since touch | Formula | `dateBetween(now(),Last touch,"days")` |
| Next action | Text | — |
| Owner | Relation → People | — |
| Linked projects | Relation → Projects | — |

**Pipeline view (universal):** group by stage — discovery / qualification / proposal / closed.

**Relationship map:** через relations contact↔contact (org → its people).

**Views:** Pipeline (board), Needs follow-up (`Days since touch > N`), By type, Key accounts.

**Extension points:**
- *Если Jetix-style partner types* → добавь T1/T2/T3/T4 classification.
- *Если sales-heavy* → добавь deal stage + amount + probability + expected close → forecast rollup.
- *Если cooperative cohort* → добавь Charter signed flag + Mondragón role.

---

## §5.6 ⚖️ Decisions Log (generic)

**Назначение.** Что решили / почему / чем кончилось. Институциональная память бизнеса.

**База Decisions (universal):**

| Поле | Тип | Дефолт |
|---|---|---|
| Title | Title | — |
| Date | Date | — |
| Category | Select | strategic / financial / hiring / product / legal / other |
| Owner | Relation → People | — |
| Status | Select | proposed / approved / executed / rejected / reversed |
| Rationale | Text | почему |
| Linked stakeholders | Relation → Stakeholders | — |
| Linked projects | Relation → Projects | — |
| Impact assessment | Text | — |
| Outcome | Text | чем кончилось (заполняется позже) |
| Review date | Date | когда оценить результат |

**Views:** Recent decisions, By category, Awaiting review (`Review date ≤ today, Outcome empty`),
Reversed (учимся на откатах).

**Extension points:**
- *Если AWAITING-APPROVAL Jetix-style* → добавь packet linking + Ack records + F-G-R triple.
- *Если RACI* → добавь Responsible / Accountable / Consulted / Informed relations.
- *Если board-governed* → добавь board vote tracking (votes for/against/abstain).

**(philosophy-expert lens):** поле Outcome + Review date = встроенный epistemic feedback loop —
бизнес учится на своих решениях, а не повторяет ошибки (анти-amnesia).

---

## §5.7 🛡️ Risks Register (generic)

**Назначение.** Что может пойти не так + что делаем.

**База Risks (universal):**

| Поле | Тип | Формула |
|---|---|---|
| Title | Title | — |
| Category | Select | financial / operational / legal / market / reputational / technical / people |
| Severity (1-5) | Number | — |
| Likelihood (1-5) | Number | — |
| Score | Formula | `prop("Severity")*prop("Likelihood")` |
| Priority | Formula | `if(Score>=15,"🔴 high",if(Score>=8,"🟡 mid","🟢 low"))` |
| Mitigation | Text | — |
| Owner | Relation → People | — |
| Status | Select | open / mitigating / accepted / closed |
| Review date | Date | — |

**Views:** Top risks (sort Score desc), By category, Due for review, Open high-priority.

**Extension points:**
- *Если R12-aware* → добавь R12 category + 8 paired-frame questions check.
- *Если ISO compliance* → добавь ISO category mapping.
- *Если industry risks (healthcare/finance)* → добавь sub-categories + regulator mapping.

---

## §5.8 📜 Compliance & Legal (generic)

**Назначение.** Юр-статус / договоры / комплаенс.

**База Legal Entity:** Entity type / Jurisdiction / Registration date / Tax ID / Status.

**База Contracts (universal):**

| Поле | Тип |
|---|---|
| Title | Title |
| Party | Relation → Stakeholders |
| Type | Select (client / vendor / employment / nda / partnership) |
| Start / End | Date |
| Value | Number |
| Status | Select (draft / active / expired / terminated) |
| Renewal date | Date |
| Expiring soon? | Formula (`Renewal ≤ now+30d`) |

**База Compliance checklist:** Item / Category (privacy/GDPR / tax filings / insurance / licenses) /
Due date / Status / Owner / Overdue? (formula).

**Views:** Active contracts, Expiring soon, Compliance due, By jurisdiction.

**Extension points:**
- *Berlin/DE specific* → добавь Steuerberater contact + Einzel/GmbH/UG decision tracking.
- *Cooperative* → добавь Charter compliance + Mondragón ratio audit.
- *Public company* → добавь SOX / SEC filings tracking.

---

## §5.9 🧰 Tools / Resources Inventory (generic)

**Назначение.** Чем работаем + сколько стоит.

**База Tools:**

| Поле | Тип |
|---|---|
| Name | Title |
| Purpose | Text |
| Category | Select (dev / design / ops / marketing / ai / finance) |
| Status | Select (active / trial / deprecated) |
| Cost / period | Number |
| Owner | Relation → People |
| Usage frequency | Select (daily / weekly / rare) |
| Renewal date | Date |

**Views:** Active tools, By category, Cost rollup (sum → feeds §5.2 expenses), Underused
(`Usage=rare & Cost>0` — кандидаты на отмену).

**Extension points:**
- *Если AI-heavy ops* → добавь AI tools sub-category + agent inventory + model/version.
- *Если remote-first* → добавь collaboration tool stack + seat count.

---

## §5.10 📚 Documents / Knowledge Hub (generic)

**Назначение.** Где что лежит — индекс документов бизнеса.

**База Document Index:**

| Поле | Тип |
|---|---|
| Title | Title |
| Category | Select (executive / methodology / financial / legal / brand / operational) |
| Status | Select (draft / active / archived) |
| Owner | Relation → People |
| Last updated | Date |
| Link | URL |
| Access | Select (public / internal / restricted) |

**Views:** By category, Recently updated, Restricted docs, Stale (`Last updated > 180d`).

**Extension points:**
- *Если wiki-based knowledge* → добавь wiki concepts / sources / claims linking.
- *Если SOPs-heavy* → добавь SOP version control + version number.
- *Если client-facing docs* → добавь public/private flag + sharing tracking.

---

## §5.11 📊 Executive Daily/Weekly Briefing (generic)

**Назначение.** Ежедневный/недельный обзор для founder — «весь бизнес на одной странице».
**DRAFT-only** — ассистент/CC предлагает, founder reviews.

**База Briefing (per period):**

| Поле | Тип |
|---|---|
| Period | Title (date) |
| Cadence | Select (daily / weekly / monthly) |
| Critical attention | Text (≤5 items) |
| Health snapshot | Text (метрики delta) |
| Progress | Text (closed / starting / blocked) |
| People movement | Text |
| Strategic threads | Text (new ideas / decisions awaiting) |
| Reviewed? | Checkbox |

**5 generic секций:**
- 🚨 **Critical attention** (≤5 items, требующие решения founder).
- 📊 **Health snapshot** (key metrics delta — runway / revenue / project health / risk score;
  настраиваемые под бизнес).
- 🎯 **Progress** (что закрыто / стартует / заблокировано).
- 🤝 **People/Stakeholders movement** (новые / ушли / нужен follow-up).
- 💡 **Strategic threads** (новые идеи / решения awaiting).

**DRAFT-only механика:** ассистент собирает цифры из §5.1-§5.10 (rollups) → черновик брифинга;
founder читает → правит → решает. Каденс: daily / weekly / monthly (user picks).

**Extension points:**
- *Если AI-assistant (Claude/etc.)* → добавь auto-generated briefing pipeline (rollup → draft).
- *Если team-based briefing* → добавь distribution rules (кому рассылается).

**(mgmt-expert lens):** брифинг = главный артефакт Layer 4; он превращает 10 баз в один
управляемый поток внимания founder (≤5 critical items = anti-overload, наследие «attention budget»).

---

## §5.12 🚨 Crisis Mode Playbook (generic)

**Назначение.** Что делать, когда всё горит. Заранее прописанные процедуры.

**База Crisis Playbooks:**

| Поле | Тип |
|---|---|
| Crisis type | Title |
| Category | Select (financial-shock / key-person-departure / public-incident / legal-trigger / operational-outage) |
| Trigger conditions | Text |
| Immediate actions | Text (чек-лист) |
| Escalation chain | Relation → People |
| Communication template | Text |
| Debrief checklist | Text |

**5 generic категорий:** Financial shock (revenue drop / unexpected expense / runway shortening) /
Key person departure / Public incident (reputation) / Legal trigger / Operational outage.

**Views:** All playbooks, By category, Active crisis (если триггернулся).

**Extension points:**
- *Если R12-governed* → добавь R12 violation procedure + Steward escalation.
- *Если regulated industry* → добавь regulator notification procedure + timelines.

---

## §5.13 Executive Command Center (хаб Layer 4)

Одна страница-дашборд со встроенными linked views всех 12 групп: Goals health / Runway / Active
projects / Pipeline / Decisions awaiting / Top risks / Expiring contracts / Today's briefing. Это
«точка входа» founder (аналог Command Center Layer 1, но для бизнеса).

**Standalone-capable:** founder может развернуть только §5.1+§5.2+§5.4+§5.11 + этот хаб за 2-3
часа и получить рабочий executive view — без Layer 1-3.

---

# §5.X 🟧 Jetix-specific OPTIONAL OVERLAY

> Это **OPTIONAL overlay** — если кто-то форкает Layer 4 base **именно для Jetix-стиля
> кооперативного бизнеса** (anti-extraction + Mondragón + R12 + cohort + Charter). **Не часть
> base.** Это пример конкретного бизнеса — один из многих возможных overlay'ев. Любой бизнес может
> написать свой (VC-overlay, agency-overlay, SaaS-overlay).
>
> Каждый элемент ниже — «это добавляешь поверх generic §5.X DB, если хочешь Jetix-style».

## §5.X.1 Что Jetix добавляет к каждой generic базе

| Generic база | Jetix-overlay добавляет |
|---|---|
| §5.1 Strategy | POINT A → POINT B + Build/Run/Scale stage field + 4 LOCKED reference |
| §5.2 Finance | Mondragón 5:1 ratio check formula + 75/25 split + 3-layer recursive 25% (V10) + treasury pool |
| §5.3 People | 10 Jetix ролей overlay (PM / Inv-Cap×3 / Contributor / Advisor / Facilitator / Mentor / Observer / Steward) + ротация + IP-1 binding table |
| §5.4 Projects | Stage Gates SG-1..SG-4 + predicate fields + R12 audit status |
| §5.5 Stakeholders | T1-T4 partner classification + Charter signed flag |
| §5.6 Decisions | AWAITING-APPROVAL packet + Ack records + F-G-R triple + Default-Deny категоризация |
| §5.7 Risks | R12 category + 8 paired-frame questions + 4 action classes |
| §5.8 Legal | Charter compliance + Mondragón ratio audit + Berlin Steuerberater + Einzel/GmbH/UG |
| §5.11 Briefing | Jetix-specific 5 секций Daily CC pass + DRAFT-only enforcement |
| §5.12 Crisis | R12 violation procedure + Steward escalation + анти-секта kit |

## §5.X.2 R12 8 paired-frame questions (интеграция)

В Jetix-overlay каждая монетизация / партнёрское касание проходит 8 вопросов (поля-чеклист):
цена ≤ польза? · конкретно? · соразмерно отношениям? · по стадии? · канал уместен? · не доим /
не запираем? · нет манипуляции? · стоп-сигнал готов? — хоть один FAIL → не отправляется / HALT.

## §5.X.3 Mondragón 5:1 ratio enforcement (formulas)

Поверх §5.2: `if(max(comp)/min(comp) > 5, "🛑 HALT F4 ≤5с", "✅ pass")` — проверка перед каждым
распределением. Нарушение → Steward + R12 Audit Log + лог в `swarm/approvals/log.jsonl`.

## §5.X.4 Charter slot + 4 RUSLAN-LAYER action classes

Charter (6 секций, Layer 3 §6) подключается к Layer 4 как governance-документ всего бизнеса.
4 action classes мониторятся в §5.7 Risks (R12 category) + §5.12 Crisis:
`extraction_beyond_share` / `wage_ratio_violation` / `non_consensual_distribution` /
`fork_prevention_attempt` — каждый → HALT.

## §5.X.5 10 Jetix ролей overlay (поверх generic Roles §5.3)

Generic Roles library → заполняется конкретными 10 ролями из Layer 3 §2: PM / Inv-Cap / Inv-Time /
Inv-Net / Contributor / Advisor / Facilitator / Mentor / Observer / Steward. IP-1: роли —
контейнеры, executor binding (Ruslan founder / Maxim PM / Прапион Steward / Цэрэн Inv-Net) =
RUSLAN-LAYER, в отдельной binding-table, не в роль.

## §5.X.6 4 monetization templates linking (поверх §5.2)

T1 стандарт / T2 капитал / T3 когорта €1500/мес / T4 знание-IP (Layer 3 §5) подключаются к
§5.2 Revenue как типы income stream с R12-чеком.

## §5.X.7 Stage Gates SG-1..SG-4 + 4 LOCKED reference

§5.4 Projects получает SG-поля (Layer 3 §3 path). 4 LOCKED canonical (Метод V2 / Strategic Plan /
Economic V10 / AI Market) + Foundation = reference в §5.10 Documents (Access=locked, read-only).

## §5.X.8 Programmable Ethereum Phase 2+ overlay flag

Поле-флаг в Charter: `ethereum_overlay` (Phase 2+, per-Clan opt-in) — Mondragón cap on-chain +
QF distribution + RageQuit exit-token. Phase 1 текстовая версия (Steward надзор) = baseline;
on-chain = опциональное усиление.

## §5.X.9 Daily CC pass — Jetix 5 секций (поверх §5.11)

Generic Executive Briefing → Jetix-specific: 🤝 знакомства / 🎯 пробелы навыков / 🔄 биржа /
🚀 проекты / 📖 интернет (Layer 3 §7). DRAFT-only enforcement: CC предлагает, founder/Ruslan
reviews; никогда не действует сам.

## §5.X.10 Build/Run/Scale alignment (поверх §5.1)

Strategy получает stage-field Build/Run/Scale (Platform Lifecycle Plan): R12-защита растёт с
этапом; Layer 4 наполняется по этапам (Build: minimum exec view; Scale: full + multi-clan agg).

---

## §6 Worked examples — разные типы бизнеса форкают Layer 4 (generic, без Jetix)

> Иллюстративные one-line примеры применения generic base (НЕ sample records — это описания, как
> бизнес X адаптирует скелет).

- **Маленький консалтинг (1-3 чел):** §5.1 (квартальные цели) + §5.2 (invoices + runway) + §5.4
  (проекты-клиенты с project value) + §5.5 (pipeline сделок) + §5.11 (weekly briefing). Extension:
  project-based revenue в §5.4. Никакого Jetix-overlay.
- **Mid SaaS (10-30 чел):** + §5.1 OKR extension + §5.2 subscription revenue + cap table (VC) +
  §5.3 hierarchy + §5.7 risks + §5.9 tools (seat tracking). VC-overlay вместо Jetix.
- **Кооператив:** generic base + Jetix-overlay §5.X (Mondragón + R12 + Charter) — это и есть
  ближайший к Jetix кейс, но это **выбор бизнеса**, не часть base.
- **Агентство:** §5.4 проекты + §5.5 клиенты + §5.2 project margin + §5.3 matrix org + §5.10 docs.

**Это и есть fork-able:** один generic skeleton обслуживает 4 очень разных бизнеса; различие —
только в том, какие extension points каждый включил, и какой (если вообще) overlay наслоил.

---

## §7 Constitutional posture Phase 5

- **R1 surface only** — какие из 12 групп ядро vs опц, какие extension включить, Jetix-overlay
  on/off = решения Ruslan (см. main §11).
- **R2 STRICT** — 4 LOCKED + Foundation = reference only (§5.X.7).
- **R12 paired-frame STRICT** — Layer 4 = high R12-risk (концентрация контроля у top-executive →
  риск authoritarian drift). Defensive: generic base **не enforce'ит** R12 (это нейтральный
  business tool); R12 включается только через Jetix-overlay opt-in. AUTO-FIRE influence-ethics +
  recruitment-dynamics annotated в §5.X.
- **IP-1 STRICT** — generic Roles абстрактны; 10 Jetix ролей + имена = overlay/RUSLAN-LAYER.
- **R6** — generic = enterprise-OS general knowledge (sota-tracker Phase 0 §4) + Mondragón;
  overlay = Economic V10 + Team OS + Execution Plan + Platform Lifecycle.
- **No sample data** — все поля/формулы = паттерны; worked examples = описания применения, не записи.

---

*Phase 5 closure. Layer 4 = universal fork-able business foundation: 12 групп баз (§5.1-§5.12) с
generic схемами + extension points + Executive Command Center, standalone-capable за 2-3 часа.
Jetix-overlay §5.X = отдельная optional под-секция (R12 / Mondragón / Charter / 10 ролей / Stage
Gates / Ethereum). Тон base — универсальный, Jetix = один пример. NO sample data. Дальше Phase 6 —
cross-layer data flows.*
