---
title: Phase 9 — Per-category doc list (≥80 документов, skeleton only)
date: 2026-05-25
type: phase-report
phase: 9
parent_prompt: prompts/jetix-full-map-and-docs-skeleton-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F3
G: jetix-full-map-and-docs-skeleton-phase-9
constitutional_posture: R1 surface only + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + NO sample doc content
language: russian primary
---

# 📋 Phase 9 — Полный список документов по категориям (скелет)

> **Что это.** Для каждой из 12 категорий — список документов «нормальной корпорации»
> Jetix. Per-doc: **назначение** (one-liner) / **скелет** (какие секции — НЕ образец
> текста) / **кому** / **формат** / **частота** / **есть-нет**.
>
> ⛔ **NO sample content.** Описываем *что в документе должно быть* (заголовки секций),
> никогда не пишем сам текст документа.
>
> **Обозначения есть-нет:** ✅ существует · ⚠️ частично · ❌ отсутствует.
> **Частота:** разовый / по-событию / квартал / год / непрерывно.

---

## 📜 §1 Executive / Strategic (8 docs)

**1.1 Vision / North Star** — зачем Jetix существует на 10-летнем горизонте.
Скелет: миссия / проблема / решение / 35 use-case'ов / 12 категорий / layered identity.
Кому: Руслан + T1/T2. Формат: MD. Частота: год (ревизия). ✅ `JETIX-VISION-FUNDAMENTAL`.

**1.2 Strategic Plan (near-future)** — план на 3-12 мес.
Скелет: текущее состояние / цели / cascade layers / path to 1M / Wave-последовательность.
Кому: Руслан. Формат: MD. Частота: квартал. ✅ `STRATEGIC-PLAN-NEAR-FUTURE` 🔒.

**1.3 Execution Plan (fixation)** — что делаем + кто + sequencing.
Скелет: 4 типа партнёров / 2 направления / Wave 1 / 8 вопросов R12 / 6 схем.
Кому: Руслан + T1/T2. Формат: MD. Частота: по-событию. ✅ `EXECUTION-PLAN-FIXATION`.

**1.4 Master Plan (public)** — публичный долгосрочный манифест (аналог Tesla).
Скелет: видение / этапы Build-Run-Scale / кому это / приглашение.
Кому: mass + T2. Формат: лендинг-секция + PDF. Частота: год. ❌ (есть internal, нет публичного).

**1.5 OKR / quarterly objectives** — измеримые цели на квартал.
Скелет: 3-5 objectives × key results / owner / дедлайн / статус.
Кому: Руслан + team (Run). Формат: Notion DB. Частота: квартал. ❌.

**1.6 Annual review / letter** — годовой отчёт plain-language (аналог Berkshire).
Скелет: что было / результаты / уроки / куда дальше / благодарности.
Кому: партнёры + cohort. Формат: MD + PDF. Частота: год. ❌ (рано — нет года истории).

**1.7 Point A / Point B docs** — где мы / куда целимся (snapshot).
Скелет: инвентарь текущего / 3 горизонта / cohort funnel / блокеры.
Кому: Руслан. Формат: MD. Частота: по-событию. ✅ `POINT-A` + `POINT-B-*`.

**1.8 Decisions log (strategic)** — журнал фундаментальных решений.
Скелет: D-NN / что зафиксировано / почему необратимо / reversal predicate / provenance.
Кому: internal + Steward. Формат: MD + JSONL index. Частота: непрерывно. ⚠️ 29 D-LOCK scaffold-pending.

---

## 🧪 §2 Methodology / IP (7 docs)

**2.1 Method canonical (V2)** — метод как передаваемый объект.
Скелет: онтология (информация+методы) / 4 уровня / мета-метод / мета-контроль / внешняя система.
Кому: T1 selective + internal. Формат: MD. Частота: по-событию. ✅ `METHOD-LIFE-DEVELOPMENT-V2` 🔒.

**2.2 Meta-method component reference** — 8/16 компонент покомпонентно.
Скелет: компонента / определение / ≥5 примеров / cross-tradition / failure mode.
Кому: T1 + cohort (ступень 5+). Формат: MD. Частота: по-событию. ✅ `META-METHOD-8-COMPONENT-DEEP`.

**2.3 Method canonical (human-language)** — метод «на пальцах» для людей.
Скелет: что такое метод / зачем мета / прошивка / примеры из жизни.
Кому: T3 + cohort (ступень 1-2). Формат: MD + видео A. Частота: по-событию. ⚠️ (CONSOLIDATED-HL частично; видео A ❌).

**2.4 Technical specs / FPF** — конституциональная спецификация методологии.
Скелет: IP-1/IP-2/IP-3/IP-7 / A.6.B / A.14 / B.3 / Steward governance.
Кому: internal + Steward. Формат: MD. Частота: по-событию (gated). ✅ `design/JETIX-FPF.md` 🔒.

**2.5 SOPs (методологические процедуры)** — как применять метод по шагам.
Скелет: 6-шаговая процедура мета-метода / чек-листы / паузы-перед-задачей.
Кому: cohort + internal. Формат: MD + Notion. Частота: по-событию. ⚠️ (в Method V2, не отдельно).

**2.6 IP licensing terms** — условия лицензирования методологии.
Скелет: что лицензируется / тиры / цена / ограничения / attribution.
Кому: T1 sub-licensing + корп.клиенты. Формат: MD + PDF. Частота: по-событию. ❌ (Phase 2+).

**2.7 Hypothesis Architecture spec** — 7-слойная архитектура гипотез.
Скелет: 7 слоёв / hypothesis lifecycle / skills (11 hypothesis) / views.
Кому: internal + advanced cohort. Формат: MD + Notion. Частота: по-событию. ✅ (skills + concept docs).

---

## 🏗️ §3 Platform / Product (8 docs)

**3.1 Product roadmap** — что строим Build→Run→Scale.
Скелет: фичи per stage / critical path / зависимости / даты.
Кому: internal + T1 co-creators. Формат: Notion DB. Частота: квартал. ⚠️ (в Platform Lifecycle, не отдельно).

**3.2 Personal OS spec (Layer 1-2)** — 5 баз Notion для индивида.
Скелет: Life OS / Business Ops / Knowledge / Methodology Practice / Cohort Coordination — структуры баз.
Кому: T3 + cohort. Формат: Notion template + MD spec. Частота: по-событию. ⚠️ дизайн ✅, implement ❌.

**3.3 Team OS spec (Layer 3)** — multi-tenant + 10 ролей.
Скелет: tenancy model / 10 ролей / marketplace / coordination ≤7 задач.
Кому: T1 co-design. Формат: Notion template + MD. Частота: по-событию. ⚠️ дизайн ✅, implement ❌.

**3.4 Workshop format spec** — мастерская как продукт (ступень 5).
Скелет: 7 ступеней / Bloom mapping / расписание / mentor-pairing / fork-and-leave per step.
Кому: cohort + T1. Формат: MD + Notion. Частота: по-событию. ⚠️ (в Education docs).

**3.5 Feature specs (per feature)** — детальные спеки фич.
Скелет: проблема / решение / acceptance / зависимости.
Кому: internal. Формат: MD. Частота: по-событию. ❌ (Build Artefacts Specs частично).

**3.6 Architecture diagrams** — как система устроена.
Скелет: 11 Foundation Parts / ROY swarm / data flow / mermaid.
Кому: internal + engineer-tier. Формат: MD + mermaid. Частота: по-событию. ✅ (Foundation + TASK-A mermaid).

**3.7 API / template docs** — как настроить шаблоны/инструменты.
Скелет: skill reference / Notion setup / Claude Code setup.
Кому: cohort + T3. Формат: MD + Notion. Частота: по-событию. ⚠️ (CLAUDE.md + skills, не для cohort).

**3.8 Changelog / release notes** — что изменилось.
Скелет: версия / дата / изменения / migration notes.
Кому: internal + cohort. Формат: MD (git) + Notion. Частота: непрерывно. ✅ (git log + `wiki/log.md`).

---

## 👥 §4 Community / Cohort (9 docs) — R12 STRICT

**4.1 Charter v1 (текст)** — конституция сообщества.
Скелет: ценности / права / обязанности / split 75/25 / доля treasury / fork-and-leave / 5:1 cap / 30-day opt-out.
Кому: cohort + T1. Формат: MD + PDF (публичная). Частота: по-событию (версии). ❌ структура ✅, текст ❌. **R12 STRICT** (Прапион ревью).

**4.2 Community guidelines / Code of Conduct** — правила поведения.
Скелет: уважение / не-извлечение / anti-cult / разрешение конфликтов / эскалация.
Кому: cohort. Формат: MD + Notion. Частота: год. ❌. **R12 STRICT** (8 cult-паттернов в Anti-CTA).

**4.3 Onboarding guide (cohort)** — как влиться в когорту.
Скелет: первые шаги / ступени 1-4 / Notion setup / первый звонок / fork-and-leave явно.
Кому: новые cohort members. Формат: Notion + MD. Частота: по-событию. ❌. **R12** (voluntary opt-in mandatory).

**4.4 Cohort target ontology** — кому подходит / не подходит.
Скелет: O-161 положительный профиль / O-162 anti-target / 6-мерный self-fit / demographic-agnostic.
Кому: internal + self-selection. Формат: MD + wiki. Частота: по-событию. ✅ `cohort-target-profile-ontology` (O-161/162).

**4.5 Mentor matrix** — кто кого менторит.
Скелет: ментор / менти / тир / cadence / cross-tier правила.
Кому: cohort + mentors (Run). Формат: Notion DB. Частота: непрерывно. ❌ (Run stage).

**4.6 Cohort calendar** — расписание когорты.
Скелет: сессии / дедлайны / разборы / события.
Кому: cohort. Формат: Notion + calendar. Частота: непрерывно. ❌ (Run).

**4.7 Membership terms (per-tier)** — условия членства L4-L7.
Скелет: take rate per tier / commitment / права / exit terms.
Кому: партнёры по тирам. Формат: MD + PDF. Частота: по-событию. ⚠️ (в PARTNER-OFFERING, не как отдельный per-tier doc).

**4.8 Anti-cult / R12 discipline doc** — как НЕ стать сектой.
Скелет: 8 cult-паттернов / paired-frame вопросы / influence-ethics auto-fire / стоп-сигналы.
Кому: internal + Прапион. Формат: MD. Частота: по-событию. ⚠️ (в OUTREACH-CONTENT Anti-CTA). **R12 STRICT**.

**4.9 Community cast / archetypes** — типы участников сообщества.
Скелет: 11 архетипов / роли / как взаимодействуют.
Кому: internal. Формат: MD. Частота: по-событию. ⚠️ D-07 (scaffold-pending).

---

## 💰 §5 Financial (8 docs)

**5.1 Economic model / tokenomics** — как устроены деньги.
Скелет: 8 моделей дохода / рекурсия 25% / 5:1 cap / QF / V10 Hybrid / break-even.
Кому: Руслан + T2. Формат: MD. Частота: по-событию. ✅ `ECONOMIC-MODEL-TOKENOMICS` V10 🔒.

**5.2 Revenue model (human-language)** — доход «на пальцах».
Скелет: 75/25 / тиры L1-L7 / triple-role / что получаешь.
Кому: партнёры. Формат: MD. Частота: по-событию. ✅ `PARTNER-OFFERING-HUMAN-LANG`.

**5.3 Budget / runway** — сколько тратим, сколько хватит.
Скелет: расходы по месяцам / capital bridge / break-even projection / 4 scenarios.
Кому: Руслан + T2 капитал. Формат: spreadsheet. Частота: квартал. ❌ (в Economic V10 projection, не live sheet).

**5.4 Pricing sheet** — цены по программам/ступеням.
Скелет: 7-variant catalog (V1 Free … V7 Charter share) / hardship policy.
Кому: cohort + партнёры. Формат: MD + Notion. Частота: квартал. ⚠️ (в RESEARCH-EDUCATION §5).

**5.5 Invoice template** — счёт SEPA-ready.
Скелет: реквизиты / позиции / НДС / SEPA / срок.
Кому: клиенты. Формат: PDF template. Частота: по-событию. ❌ (после бизнес-счёта).

**5.6 Contract template (client/service)** — договор на услуги.
Скелет: scope / цена / сроки / ответственность / расторжение.
Кому: клиенты quick-money. Формат: PDF. Частота: по-событию. ❌.

**5.7 Distribution policy** — как делится доход (5:1, 60/40, QF).
Скелет: split rules / Mondragón 60/40 routing / QF 10% skim / promoter bonus.
Кому: internal + cohort. Формат: MD. Частота: по-событию. ✅ (в Economic V10 + TRIPLE-ROLE). **R12** (5:1).

**5.8 Bookkeeping minimum** — учётный минимум.
Скелет: счета / категории / Steuerberater requirements.
Кому: Руслан + Steuerberater. Формат: spreadsheet. Частота: непрерывно. ❌.

---

## ⚖️ §6 Legal / Governance (9 docs)

**6.1 Legal entity docs** — юр-оболочка (Einzel/GmbH/UG).
Скелет: форма / регистрация / устав / responsibilities.
Кому: Руслан + юрист. Формат: PDF. Частота: разовый. ❌ (после Steuerberater).

**6.2 Charter (legal version)** — Charter как юр-документ.
Скелет: legal rights / obligations / dispute resolution / jurisdiction.
Кому: партнёры (legal). Формат: PDF. Частота: по-событию. ❌ (текст не написан).

**6.3 Partner agreement template** — соглашение с партнёром.
Скелет: tier / split / fork-and-leave / 30-day / asset retrieval / R12 8-item.
Кому: партнёры L4-L7. Формат: PDF. Частота: по-событию. ❌. **R12 STRICT**.

**6.4 IP licensing agreement** — лицензия на методологию.
Скелет: что лицензируется / scope / royalty / attribution / termination.
Кому: T1 sub-license. Формат: PDF. Частота: по-событию. ❌ (Phase 2+).

**6.5 Stage Gate records** — журнал прохождения гейтов.
Скелет: проект / SG-N / predicate / дата / решение.
Кому: internal + Steward. Формат: MD + JSONL. Частота: непрерывно. ✅ (Part 7 + lint).

**6.6 Steward decisions log** — лог решений хранителя.
Скелет: решение / основание / FPF-ref / дата.
Кому: internal + audit. Формат: MD. Частота: непрерывно. ⚠️ (AWAITING-APPROVAL log частично).

**6.7 AWAITING-APPROVAL packets** — гейт-пакеты на одобрение.
Скелет: что предлагается / blast-radius / action class / risk / ack-trail.
Кому: Руслан (ack). Формат: MD. Частота: по-событию. ✅ `swarm/awaiting-approval/` (14 packets).

**6.8 Privacy / data handling policy** — как обращаемся с данными.
Скелет: какие данные / хранение / доступ / GDPR / удаление.
Кому: cohort + клиенты. Формат: PDF + MD. Частота: год. ❌.

**6.9 DAO governance docs (Phase 2+)** — on-chain управление.
Скелет: proposal threshold / quorum / multi-sig / time-lock / SBT voting.
Кому: cohort (Phase 2+). Формат: on-chain + MD. Частота: по-событию. ⚠️ (JETIX-ETHEREUM bundle, Phase 2+).

---

## 🎨 §7 Brand / Marketing (8 docs) — R12 STRICT

**7.1 Brand book** — визуальная + вербальная идентичность.
Скелет: logo / typography / 2-3 colors / tone of voice / dos-and-donts.
Кому: все каналы. Формат: PDF. Частота: год. ❌ (brand-minimum в Build Specs).

**7.2 Messaging guide** — как говорим о Jetix.
Скелет: core message / pain-primary / opportunity-secondary / per-архетип / запретные формы.
Кому: outreach + контент. Формат: MD. Частота: по-событию. ⚠️ (в OUTREACH-CONTENT). **R12 STRICT**.

**7.3 Landing page** — главная страница наружу.
Скелет: hero / проблема / решение / 7 ступеней / CTA / FAQ embed / видео A embed.
Кому: mass + T2/T3. Формат: лендинг (Notion public / static). Частота: по-событию. ❌ sections ✅, контент ❌.

**7.4 Pitch deck (light, 5-7 slides)** — короткая презентация.
Скелет: проблема / решение / модель / traction / команда / ask / контакт.
Кому: T2 капитал. Формат: PDF/slides. Частота: по-событию. ❌.

**7.5 One-pager** — одностраничник «что такое Jetix».
Скелет: что / кому / как работает / как войти / контакт.
Кому: T1-T3 первый контакт. Формат: PDF/MD. Частота: по-событию. ⚠️ (ONE-PAGER-FPF есть, но technical).

**7.6 FAQ (10 вопросов)** — частые вопросы наружу.
Скелет: 10 вопросов-слотов / ответы (заполняются после первых звонков).
Кому: mass + T3. Формат: MD + лендинг. Частота: квартал. ❌ structure ✅, content ❌.

**7.7 Website content** — тексты сайта.
Скелет: страницы / навигация / about / contact.
Кому: mass. Формат: лендинг. Частота: квартал. ❌.

**7.8 Telegram positioning + posts outline** — канал + первые посты.
Скелет: позиционирование / 5-7 постов outline / cadence.
Кому: mass + T3. Формат: MD + Telegram. Частота: непрерывно. ❌. **R12** (не манипулировать).

---

## 🔬 §8 Research / Knowledge (7 docs)

**8.1 Research deeps (5)** — глубокие исследования.
Скелет: methodology / sota / propaganda-recruitment / nlp / levenchuk-master — каждый 8-11 фаз.
Кому: internal + curious. Формат: MD. Частота: по-событию. ✅ 5 deeps.

**8.2 Wiki (knowledge base)** — живая сеть знаний.
Скелет: 9 типов сущностей / 750+ entities / 909 edges / 6 ниш / communities.
Кому: internal + agents. Формат: MD + JSONL graph. Частота: непрерывно. ✅ `wiki/`.

**8.3 Book corpus index** — каталог 80+ книг.
Скелет: книга / категория / статус OCR / refs.
Кому: internal. Формат: MD + filesystem. Частота: непрерывно. ✅ `raw/books-md/` (25 категорий).

**8.4 Experiments log** — журнал экспериментов.
Скелет: эксперимент / гипотеза / результат / вывод.
Кому: internal. Формат: MD (wiki/experiments). Частота: непрерывно. ⚠️ (wiki entity type существует).

**8.5 Research portfolio** — обзор всего research.
Скелет: deeps / open questions / pending acks / cross-pollination proposals.
Кому: Руслан. Формат: MD. Частота: квартал. ⚠️ (в каждом deep §, не сводно).

**8.6 Decisions / knowledge diff** — что изменилось в знании.
Скелет: delta между датами / новые концепты / supersessions.
Кому: internal. Формат: MD (skill output). Частота: по-событию. ✅ `/knowledge-diff` skill.

**8.7 Canonical INDEX** — каталог всех canonical docs.
Скелет: 110 docs / статус / walkthrough.
Кому: internal. Формат: MD. Частота: непрерывно. ✅ `canonical/INDEX.md`.

---

## 🤝 §9 Partner-facing (9 docs) — R12 STRICT

**9.1 Partner offering** — что предлагаем партнёрам.
Скелет: ступени L1-L7 / 75/25 / Mondragón 5:1 / triple-role / fork-and-leave.
Кому: T1+T3. Формат: MD. Частота: по-событию. ✅ `PARTNER-OFFERING-HUMAN-LANG`. **R12**.

**9.2 Discovery call script (универсальный)** — скрипт первого звонка.
Скелет: открытие / диагностика дыр / не-продажа / next step / R12 8 вопросов.
Кому: self (call planner). Формат: MD. Частота: по-событию. ⚠️ ad-hoc ✅ (Dmitriy), универсальный ❌. **R12 STRICT**.

**9.3 Partner onboarding** — как партнёр входит.
Скелет: первые шаги / доступы / Charter / co-create правила.
Кому: confirmed партнёры. Формат: Notion + MD. Частота: по-событию. ❌. **R12**.

**9.4 Revenue share spec** — как делим доход с партнёром.
Скелет: tier / take rate / promoter bonus / распределение / примеры.
Кому: партнёры. Формат: MD. Частота: по-событию. ✅ (в TRIPLE-ROLE + Economic). **R12** (5:1).

**9.5 Triple-role explainer** — три роли партнёра.
Скелет: worker 75% / investor доля / promoter бонус / closed-loop / beyond-Mondragón.
Кому: партнёры. Формат: MD. Частота: по-событию. ✅ `TRIPLE-ROLE-PARTNER`.

**9.6 Outreach package (Wave 1)** — пакет для первой волны.
Скелет: 13 CTA / 5+1 архетипов / 18 артефактов P0-P6 / per-tier messaging.
Кому: Wave 1 targets. Формат: MD. Частота: по-событию. ✅ `OUTREACH-CONTENT-OUTCOMES-CTAS` + `WAVE-1-PACKAGE`. **R12 STRICT**.

**9.7 Per-tier offer matrix** — что кому предлагаем (T1-T4).
Скелет: тип / что хотим / что даём / CTA / R12-риск / цель цикла.
Кому: self (pre-call prep). Формат: MD. Частота: по-событию. ✅ (в EXECUTION-PLAN §4). **R12**.

**9.8 Call plan (per-person)** — план конкретного звонка.
Скелет: тезисы / структура / R12 sweep / mermaid.
Кому: self. Формат: MD. Частота: по-событию. ✅ `CALL-PLAN-DMITRIY-KAISER` (пример формата).

**9.9 Видео C (экосистема для партнёра)** — видео-оффер.
Скелет: корпорация / Charter / R12 / 4 типа партнёров / приглашение.
Кому: T1 + T2. Формат: видео. Частота: по-событию. ❌ (spec готов). **R12 STRICT**.

---

## 📊 §10 Operational (7 docs)

**10.1 CRM** — управление контактами.
Скелет: 180 контактов / 14 секций / 24 роли / 13 статусов / stuck-detection.
Кому: internal + sales. Формат: MD + Python CLI. Частота: непрерывно. ✅ `crm/`.

**10.2 Outreach materials** — материалы для рассылки.
Скелет: per-channel templates / cadence / personalization.
Кому: outreach. Формат: MD. Частота: по-событию. ⚠️ (в OUTREACH-CONTENT). **R12**.

**10.3 Sales pipeline** — воронка сделок.
Скелет: статусы / переходы / stuck / weekly report.
Кому: sales (Run). Формат: CRM + Notion. Частота: непрерывно. ✅ (CRM pipeline statuses).

**10.4 Contact research templates** — как ресёрчить контакт перед касанием.
Скелет: org / person / хуки / fit / R12-риск.
Кому: sales-researcher. Формат: MD. Частота: по-событию. ⚠️ (skills + crm).

**10.5 Customer success / support docs** — как поддерживаем cohort.
Скелет: support flow / FAQ / эскалация / SLA.
Кому: support (Run). Формат: Notion. Частота: непрерывно. ❌ (Run).

**10.6 Weekly / daily ops cadence** — ритм работы.
Скелет: plan-day / close-day / weekly review / company-status.
Кому: Руслан. Формат: MD (skills). Частота: непрерывно. ✅ (`/plan-day` + `/close-day` + `/company-status`).

**10.7 Time-tracking / activity log** — учёт времени.
Скелет: Toggl categories / ActivityWatch timeline / daily log.
Кому: Руслан. Формат: Toggl + MD. Частота: непрерывно. ✅ (Toggl + `/log-time`).

---

## 🎯 §11 HR / People (7 docs) — R12 STRICT

**11.1 Role definitions** — описания ролей.
Скелет: роль / responsibilities / U.Episteme type / executor binding (RUSLAN-LAYER).
Кому: internal + hires. Формат: MD. Частота: по-событию. ✅ (Part 4 + ROY agent defs). IP-1.

**11.2 Hiring docs** — как нанимаем (5 ассистентов Month 1).
Скелет: что ищем / ICP / процесс / onboarding.
Кому: Руслан (Run). Формат: Notion + MD. Частота: по-событию. ❌ (Run).

**11.3 Performance review framework** — как оцениваем.
Скелет: критерии / cadence / peer-check (с human review per rule 8).
Кому: team (Run). Формат: MD. Частота: квартал. ❌. **R12** (no peer eval без human review).

**11.4 Compensation structure** — как платим (Mondragón overlay).
Скелет: wage bands / 5:1 cap / cooperative routing / equity/stake.
Кому: Руслан + hires. Формат: spreadsheet + MD. Частота: год. ❌. **R12 STRICT** (5:1).

**11.5 Team OS roles (10)** — роли внутри Team OS.
Скелет: Mentor / Advisor / Facilitator + 7 / responsibilities / marketplace.
Кому: T1 co-design (Run). Формат: Notion + MD. Частота: по-событию. ⚠️ (TEAM-OS-NOTION-TEMPLATE-PLAN дизайн).

**11.6 Worker-owner handbook** — справочник участника-владельца (Mondragón аналог).
Скелет: права / обязанности / patronage / governance participation.
Кому: cohort partners. Формат: MD. Частота: год. ❌ (Scale).

**11.7 People principles (Tier 1)** — ценности владельца о людях.
Скелет: ценности / как обращаемся / corrigibility / anti-extraction.
Кому: internal. Формат: MD. Частота: по-событию. ✅ (Pillar C Tier 1, owner-authored).

---

## 🚨 §12 Risk / Compliance (7 docs)

**12.1 Risk register** — реестр рисков.
Скелет: риск / вероятность / impact / mitigation / owner.
Кому: Руслан + Steward. Формат: MD + Notion. Частота: квартал. ⚠️ (в каждом плане §risks, не сводно).

**12.2 R12 compliance log** — журнал R12-нарушений.
Скелет: timestamp / action class / grade (F2/F4/F8) / halt time / resolution.
Кому: internal + Прапион. Формат: JSONL. Частота: непрерывно. ✅ `swarm/approvals/log.jsonl`. **это R12**.

**12.3 Default-deny table** — таблица запрещённых действий.
Скелет: action class / blast-radius / deny/escalate / 11 + 4 RUSLAN-LAYER.
Кому: internal + agents. Формат: YAML. Частота: по-событию (gated). ✅ `.claude/config/default-deny-table.yaml` 🔒.

**12.4 Audit trail** — след для аудита.
Скелет: git history / commit format / provenance / F-G-R.
Кому: audit (Phase 2+). Формат: git + JSONL. Частота: непрерывно. ✅ (git + Part 6a).

**12.5 Safety / governance framework** — уровни риска (аналог Anthropic RSP).
Скелет: Halt-Log-Alert F2/F4/F8 / Stage Gates / corrigibility / fail-loud.
Кому: internal + Steward. Формат: MD. Частота: по-событию. ✅ (Part 6b + Pillar C).

**12.6 Privacy / data policy** — обработка данных (дубль §6.8, compliance-вид).
Скелет: данные / хранение / GDPR / cohort consent.
Кому: cohort + клиенты. Формат: PDF. Частота: год. ❌.

**12.7 R12 paired-frame checklist (8-item)** — чек-лист перед влиянием.
Скелет: 8 вопросов (цена≤польза / конкретно / соразмерно / по ступени / канал / не доим / не манипулируем / стоп-сигнал).
Кому: internal (pre-outreach). Формат: MD template. Частота: по-событию. ⚠️ (в EXECUTION-PLAN, не как template). **R12 STRICT**.

---

## §13 Итоговый счёт

| Категория | Docs | ✅ | ⚠️ | ❌ |
|---|---|---|---|---|
| 📜 Executive | 8 | 4 | 2 | 2 |
| 🧪 Methodology/IP | 7 | 3 | 3 | 1 |
| 🏗️ Platform/Product | 8 | 2 | 4 | 2 |
| 👥 Community/Cohort | 9 | 1 | 4 | 4 |
| 💰 Financial | 8 | 2 | 1 | 5 |
| ⚖️ Legal/Governance | 9 | 2 | 2 | 5 |
| 🎨 Brand/Marketing | 8 | 0 | 2 | 6 |
| 🔬 Research/Knowledge | 7 | 5 | 2 | 0 |
| 🤝 Partner-facing | 9 | 6 | 1 | 2 |
| 📊 Operational | 7 | 4 | 2 | 1 |
| 🎯 HR/People | 7 | 2 | 1 | 4 |
| 🚨 Risk/Compliance | 7 | 5 | 1 | 1 |
| **ИТОГО** | **94** | **36** | **25** | **33** |

**94 документа описано** (≥80 acceptance ✅). **36 ✅ существует · 25 ⚠️ частично · 33 ❌
отсутствует.** Детальный GAP-маппинг — Phase 10. **R12 STRICT** применён к категориям 4 / 7
/ 9 / 11 + 12 (сама R12-инфраструктура).

---

*Phase 9 closure. 94 документа по 12 категориям, каждый — назначение + скелет-секции (НЕ
образец текста) + аудитория + формат + частота + есть-нет. NO sample content. R12 STRICT
на partner-facing/community/brand/HR. IP-1 STRICT. R1 surface.*
