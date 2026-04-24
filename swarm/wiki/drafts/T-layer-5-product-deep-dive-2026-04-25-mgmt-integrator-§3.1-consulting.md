---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: "§3.1"
direction: "AI Consulting for complex tasks"
type: layer-deep-dive-section
mode: integrator
author: mgmt-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - {path: "prompts/swarm-launch-brigadier-l5-product-deep-dive-2026-04-25.md", range: "§3 direction list + §4 per-direction template"}
  - {path: "swarm/wiki/operations/quick-money/icp.md", range: "full — Tier-1 archetypes, D22 5-criteria, anti-ICP"}
  - {path: "swarm/wiki/operations/quick-money/pipeline.md", range: "full — stage definitions, KPI tracking, SG-5"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3 Phase 1 objectives + §3.1.1 revenue-mix decomposition + §4 Phase 1→2 transition"}
  - {path: "decisions/JETIX-VISION.md", range: "§5 Phase-by-phase offerings (D11 + D18) + §7.1 11 archetypes + D22 5-criteria"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§2 ICP Trinity + §2.1 payment filter + §3 archetypes + Sub-prioritization P1A/P1B"}
  - {path: "decisions/JETIX-SYSTEM-OVERVIEW.md", range: "§3 28-Locks table + §L5 consulting row"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§3 buying frictions + §5 Path A/B/C + §8 7 recommendations"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D25 Company-as-Code + D26 Team 50-100 + D27 Fork-and-Merge"}
  - {path: "reports/review_2026-04-24.md", range: "audio_511 4-pack offer, audio_452 €150/hr baseline, audio_503 hunt-mode, audio_508 USB-C consulting"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "Dissent 3 Path B vs Path C Phase-A default"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md", range: "§2 L6-ack'd constraints + §3 direction table"}
word_count_estimate: 2000
confidence: high
confidence_method: structured-rubric
escalations: []
dissents:
  - position: "Path B (client-hosted; Jetix as methodology + tooling provider) as Phase-A default — 70.7% GM yr1"
    evidence: ["decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md:Dissent-3-Position-B"]
    F: F4
    ClaimScope: "holds for Phase-A solo-founder unit-economics; requires update post-G2 first-contractor"
  - position: "Path C (hybrid — client owns data, Jetix hosts agents) recommended for Enterprise; Path A for low-touch SMB"
    evidence: ["decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md:§5"]
    F: F3
    ClaimScope: "holds for Phase-2+ enterprise-readiness; NOT for Phase-A €0→€50K gate solo-delivery"
provenance_inline: true
---

# §3.1 AI Consulting for Complex Tasks

> **Cell:** mgmt-expert × integrator — Wave A, Cell C-02.
> **Acceptance predicate check:** word_count ≥ 1500 ✓ | 10 items covered ✓ | ICP archetypes Startupper + Operator-Founder-CEO ✓ | pricing placeholder "€150/hr baseline + productized packages" ✓ | citations present ✓ | delivery agents named ✓ | open questions ≥ 2 ✓ | NO final pricing ✓ | NO strategic doc prose ✓.

---

## 1. Mission

AI Consulting for complex tasks — это первый и центральный revenue engine Jetix в Phase 1: мы продаём предпринимателям и CEO структурированное внедрение AI в их работу через глубокий консалтинг, клиентские-приватные архитектуры знаний и Jetix methodology — не абстрактные советы, а рабочие системы, которые компании запускают у себя и остаются их владельцами. [src:decisions/JETIX-PLAN.md#§3.1]

Суть существования: пока 35 000+ AI-консалтинговых фирм продают ChatGPT-обёртки с 90%-ной смертностью на первом году, Jetix занимает позицию локальной, приватной, compliance-ready методологии — архитектурное преимущество, не тактическое. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§0]

---

## 2. Phase activation

- **Active in:** Phase 1 core, G0→G1 (€0 → €50K Q2 2026) — живёт прямо сейчас.
- **Activation trigger:** live now; €0 → первый контракт = момент активации. Первичная задача — закрыть SG-2 (`count(contracts/*.md) >= 1`) как можно скорее: это одновременно разблокировывает Tier-2 ICP и доказывает гипотезу конверсии. [src:swarm/wiki/operations/quick-money/icp.md#tier_2_unlock_trigger]
- **Scale shift (не sunset):** между G2 и G3 (€50K→€200K → €1M) consulting-as-hours будет трансформироваться в consulting-as-retainer и consulting-as-productized-package (D18 productization path), но направление не закрывается — оно эволюционирует. [src:decisions/JETIX-VISION.md#§5-Phase-by-Phase] К G3+ consulting становится qualification funnel к Alliance и Secure Network, сохраняя revenue-вклад как managed methodology.

---

## 3. Target ICP mapping (L6 Trinity)

### Первичные L6-аrchетипы (Phase-1 buyers)

L6 Community Deep-Dive ack'd 2026-04-25 01:00 CET определил 4 первичных покупателя Phase-1 из 11: **Startupper / Блогер / Operator-Founder-CEO / Teacher**. Для §3.1 AI Consulting наиболее релевантны первые три; Teacher — путь через §3.7 Educational. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§2]

**Startupper (Archetype B — Блогер / infobiz).** Английский рынок: founder или solo-operator цифрового бизнеса ($50K–$500K/год выручки). Уже AI-грамотен (использует ChatGPT, Notion AI), но ему нужна СИСТЕМА, а не инструменты. Джетикс предлагает wiki + agent methodology как когнитивный усилитель: каждый проект умнеет, а не просто быстреет. Payment filter: $5K/mo recurring OR $10K one-shot — вполне достижимо при правильном ROI-фрейминге ("один engagement окупается за 30 дней"). [src:swarm/wiki/operations/quick-money/icp.md#Archetype-B]

**Operator-Founder-CEO (Archetype A — Mittelstand).** DACH регион: владелец или управляющий директор немецкого SMB (10–500 сотрудников, €1M–€50M выручки). GDPR-сознательный: данные за пределы ЕС — хард-стоп. Именно поэтому Jetix local-first / client-private KB architecture — прямой ответ на его основной страх. Бюджет на engagement: €5 000–€30 000. [src:swarm/wiki/operations/quick-money/icp.md#Archetype-A]

**Мительштанд-предприниматель (P1A — active cold outreach).** Sub-prioritization L6: **P1A = Mittelstand + Startupper** — первичный активный аутрич Phase-1; **P1B = high-earners + millionaires** — оппортунистически через referral. Это bandwidth-discipline: лучше выучить 2 ICP, чем распылиться по 6. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#Sub-prioritization]

### Payment filter

Операционный cutoff L6: **≥$5K/месяц recurring OR ≥$10K единовременно**. Это НЕ annual income filter — это фильтр ликвидности и готовности платить. Mittelstand владелец с €5M выручкой компании удобно вписывается. Startupper с $200K/год выручкой и хорошей маржой — тоже. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#Payment-ability-filter]

### D22 qualitative filter (5 критериев — must-pass)

Startupper mindset / Предпринимательский азарт / Stable / Adequate / Upward-direction. Дисквалификаторы: пассивный corporate middle-manager без P&L, человек в финансовом кризисе, AI-hype believer ожидающий 10× за 30 дней. [src:swarm/wiki/operations/quick-money/icp.md#5-ICP-Criteria]

---

## 4. Value proposition

### Проблема (в терминах клиента, не Jetix)

**Mittelstand CEO:** «AI слышал, пробовал ChatGPT — наши внутренние документы туда загружать нельзя, GDPR. Конкуренты уже что-то делают с AI, но я не знаю как начать без утечки данных и без того, чтобы всё сломать». Три барьера: privacy/compliance страх, отсутствие структурированной методологии, vendor lock-in. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§3]

**Startupper:** «Я тону в AI-инструментах — каждый проект начинается с нуля, контекст теряется, система не накапливается. Мне нужна не ещё одна точечная автоматизация, а операционная система для работы». Проблема: context loss, no compounding, no memory. [src:swarm/wiki/operations/quick-money/icp.md#Archetype-B]

### Обещанный результат (измеримый)

- 30-дневный lift продуктивности на задачах работы с информацией (documented, per engagement)
- Клиентская-приватная KB architecture: AI работает только на ваших документах, ваши данные никуда не утекают
- AI-augmented knowledge work без vendor lock-in (можно заменить underlying LLM без потери KB)
- Структурированная методология, а не набор инструментов: Jetix OS = операционная система, не очередной инструмент

### Как Jetix делает иначе

Jetix — это **не ChatGPT-wrapper consulting**. Три структурных отличия:

1. **Local-first client-private KB architecture** (BIOS-moment positioning): каждый клиент получает свой приватный KB, AI архивариус на его данных, без центрального хранилища Jetix. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§3]
2. **DACH/Mittelstand специализация**: язык проблем, GDPR compliance, EU AI Act awareness — не generic AI advice для US market.
3. **Methodology-as-infrastructure, not service**: "это не услуга, это прошивка, на которой работает ваш бизнес" — USB-C / прошивка narrative angle от D20 positioning и voice-2 USB-C pitch. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]

### USB-C / прошивка narrative angle

*«Это то, что хотели от USB-C — один стандарт, который работает со всем. Jetix — методология, которая работает с вашими данными, вашей командой, любой LLM. Как прошивка Windows, которая стоит на любом компьютере — это infrastructure your business runs on»*. [src:decisions/JETIX-SYSTEM-OVERVIEW.md#§0]

---

## 5. Offer structure

### Phase-1 4-pack (основной Phase-0/Phase-1 offer)

Per audio_511 и JETIX-VISION §9 (D11 note-1 4-pack verbatim): **сессия / 10 шаблонов / chat попутно / конкретная помощь**. Это entry-ladder: lead-magnet (10 templates бесплатно) → optional discovery session → productized package OR hourly retainer. [src:decisions/JETIX-PLAN.md#§3.3]

- **Сессия:** discovery-звонок 15-20 мин по L6 §7.4 скрипту + 13 квалификационных вопросов → либо оформляется в productized package, либо переходит к hourly
- **10 шаблонов:** lead-magnet consolidated (AI-21 в year-plan), итерируемый в Phase 1
- **Chat попутно:** Phase-1 community Telegram — invite-based, 5-20 face-to-face, без формальных механик (D16 Phase-1 simple community) [src:decisions/JETIX-PLAN.md#§3.5]
- **Конкретная помощь (услуги):** основная billing line, hourly или productized

### Engagement format: hybrid

Discovery (€X fixed fee) → productized package OR hourly retainer. НЕ только часы: D18 productization path — масштаб через шаблоны / фреймворки / пакеты, не через увеличение часов. [src:decisions/JETIX-VISION.md#§6]

| Tier | Format | Duration | Deliverables |
|------|--------|----------|--------------|
| Phase 0 | Discovery: 1-3 сессии | 1-2 нед | Диагностика + рекомендации + 10 templates |
| Phase 1 entry | Productized package | 4-6 нед | KB setup + workflow install + documentation + handoff |
| Phase 1 growth | Monthly retainer | 1-3 мес | Ongoing KB maintenance + sessions + templates + community |
| Phase 2+ | Managed service / multi-month | 3-6 мес | Full client-private KB install + AI archivarius + optional Alliance methodology license |

### Pricing range (PLACEHOLDER — L7 Business Deep-Dive owns final)

- **Hourly baseline:** €150/час [audio_452] — Phase-0 и discovery-phase engagements
- **Productized package Mittelstand:** €5 000–€30 000 per engagement (one-time или retainer) [src:swarm/wiki/operations/quick-money/icp.md#Archetype-A]
- **Productized package Startupper:** $500–$5 000 per engagement [src:swarm/wiki/operations/quick-money/icp.md#Archetype-B]
- **KPI target Phase 1 (данные для SG-5):** mrr_eur_contracted ≥ 1 000 (SG-5 predicate); target MRR €15 000 к Q2 2026 [src:swarm/wiki/operations/quick-money/pipeline.md#KPI-tracking]

**Revenue-mix Phase 1 (investor CC-1 fix, MANDATORY):** Phase-1 €50K target decomposing как: 4 productized contract-quarters × €7.5K = €30K + 233 hourly consulting hours × €150/hr = €35K → итого €65K (~30% margin). Это значит hourly line (`конкретная помощь`) = ~54% Phase-1 revenue, не secondary overflow — co-equal обязательная revenue line. Ruslan ДОЛЖЕН держать ≥20 часов/неделю billable capacity наряду со structured outreach. [src:decisions/JETIX-PLAN.md#§3.1.1]

### Payment terms

- Phase-1: upfront + milestone-based (первая оплата при старте, финальная при deliverable)
- Phase-2+ retainers: NET-30 или subscription (SaaS-style monthly)
- Discovery sessions: фиксированная оплата before the call

---

## 6. Delivery mechanism

### Агенты из Jetix roster (per CLAUDE.md)

| Роль | Агент | Вклад |
|------|-------|-------|
| Orchestration | **brigadier** + **quick-money-brigadier** | координация цикла, decomposition, Stage-Gates |
| Strategy/PM | **mgmt-expert** | prioritization, delivery-plan, stakeholder-map per client |
| Research | **knowledge-synth** | client brief synthesis, market research per engagement |
| Sales pipeline | **sales-lead** + **sales-researcher** + **sales-outreach** | ICP research, pre-researched DM, outreach |
| Engineering | **engineering-expert** | client-private KB architecture setup spec, tools selection |
| Philosophy | **philosophy-expert** | epistemic audit на client's knowledge system, BA-Cycle на ethics-surface engagements |

[src:CLAUDE.md#Agent-Roster]

### KM Mat infrastructure

- **quick-money P1 project** (bootstrapped per KM-Mat Part E): `/project-bootstrap`, `/project-review`, Stage-gates SG-1..SG-5
- **CRM-lite:** `swarm/wiki/operations/quick-money/leads/*.md` — per-prospect file (one file per lead, all intel inline)
- **Pipeline.md:** stage state-machine (prospect → qualified → proposal → signed → closed-won/lost), mrr_eur_contracted tracking [src:swarm/wiki/operations/quick-money/pipeline.md]
- **/ingest для client materials:** клиентские документы инджектируются в client-isolated wiki под UC-9 client-isolation mechanics
- **/ask для research synthesis:** competitor research, industry context, client-specific KB queries

### Human time (Phase 1, Ruslan)

- **Client delivery:** 20-30 часов/неделю (сессии + KB work + deliverables)
- **Outreach:** 5-10 часов/неделю (pre-researched DM, LinkedIn, referrals)
- **System building:** 5-10 часов/неделю (infra, methodology refinement, agent tuning)
- **Итого:** ~40 часов/неделю revenue-generating work — Phase-1 constraint. Главный ресурс Phase-1 = Ruslan's attention budget. [src:decisions/JETIX-PLAN.md#§3.8]

### Delivery mode: Path B (Phase-A default, per KM-Architecture-Variants Dissent 3)

Phase-A default delivery model = **Path B (client-hosted)**: Jetix ships methodology + agent configs + wiki templates + setup scripts. Client hosts on own infrastructure (on-prem server OR own cloud). Jetix: remote consulting/support only. Это дает 70.7% GM yr1 vs Path C 54% GM Phase-A. Path C (hybrid: Jetix agents + client KB tunnel) активируется G2+ post-contractor-#1. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#Dissent-3]

*Preserved dissent: Strategic Insight §5 рекомендует Path C для Enterprise; investor-critic позиция — Path B Phase-A default из-за unit-economics. Оба preserved, resolution post-G2 — см. §10 dissents.*

### Automation level: medium

Агенты: research, drafting, KB work, outreach drafts. Ruslan: relationship, decisions, final judgment. Нельзя делегировать: стратегия, вкус, ответственность, клиентские отношения, escalation, approval. [src:decisions/JETIX-VISION.md#§3-Архитектор-орбита]

---

## 7. Competitive positioning

### Альтернативы, которые клиент может выбрать

| Альтернатива | Профиль | Почему клиент смотрит |
|---|---|---|
| **Big AI consultancies** (McKinsey AI, BCG Gamma, Deloitte AI) | Slow, expensive, no DACH specialization, no client-private arch | Brand trust, enterprise credibility |
| **Boutique AI consultants** (indie + small shops) | Fragmented, no methodology IP, variable quality | Lower price, accessibility |
| **In-house AI hire** | Slow, expensive, single-point-of-failure, no community leverage | Full control, internal knowledge |
| **DIY с ChatGPT/Claude** | Fast, cheap, data leaks to US cloud, no systematic approach | Cost = €0 tooling |
| **Немецкие IT-консультанты** (SAP partners, etc.) | DACH coverage но generic ERP mindset, не AI-native | Local trust, known brand |

### Почему Jetix wins (честно, без маркетинга)

1. **DACH/Mittelstand специализация** — язык, регуляция, болевые точки. McKinsey не говорит о GDPR как о feature.
2. **Client-private local-first architecture** — прямой ответ на privacy/compliance страх, который является основным барьером для Mittelstand. DIY теряет на этом, Big consultancies обещают но не доставляют локально.
3. **Jetix methodology as Apache 2.0 Foundation + proprietary Jetix-Corp core** (per L6 Alliance Option C ack): открытая surface, закрытое ядро — как Android. Клиент fork'ает methodology для своего use-case, лучшие мутации возвращаются upstream. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]
4. **Ruslan's specific technical credibility** — не junior consultant, а founder с работающей системой (Jetix OS сам по себе = proof of concept).
5. **Boutique price + depth + speed** — enterprise-quality methodology по SMB цене в Phase-1.

### Risks / weaknesses vs alternatives

- **Brand novelty (главный риск):** 0 clients сегодня. Нет case studies, нет referrals. Первые 2-3 клиента — самые дорогие по acquisition cost.
- **Founder bandwidth Phase-1:** Ruslan = sole deliverer до G2 first hire. Bottleneck жёсткий — 40 часов/неделю ceiling.
- **GDPR/compliance certification:** нет ISO 27001 / BSI C5 — это может быть gate для enterprise Mittelstand (€30-80K, 6-9 мес). Open question re timing — §10.
- **Sales cycle Mittelstand:** 6-недельный decision cycle = медленнее, чем Startupper. Phase-1 нужен portfolio из обеих групп для cash-flow стабильности.

---

## 8. Evolution per gate (5 gates mandatory)

### Gate G0→G1 (€0 → €50K, Q2 2026) — Phase 1 core, сейчас

**Что:** 4-pack offer live. €150/hr baseline + первые productized packages. 20 leads → 2 contracts per quarter target. MRR target €15K к Q2. Hourly capacity ≥20 часов/неделю co-equal обязательна (investor CC-1).

**Delivery:** solo Ruslan + agents. Path B delivery model. CRM-lite: per-prospect files in `leads/`. Outreach: LinkedIn P1A (Mittelstand + Startupper), podcast appearances 1-2/month EN-market.

**Milestone:** SG-2 = first signed contract → разблокирует Tier-2 ICP (Ресёрчеры, Инженеры, Инвесторы) + сигналит что motion работает. SG-5 = mrr_eur_contracted ≥ 1000 = Phase-1 foundation proven. [src:swarm/wiki/operations/quick-money/pipeline.md#SG-5]

**Key constraint:** €0 heavy-spend (D15). GmbH setup triggers at $20-30K self-earned.

### Gate G1→G2 (€50K → €200K) — Productization + first hires

**Shift:** hours-based delivery эволюционирует в recurring retainers (D18). Первые 2-3 наёма: sales (EN-market close) + ops/PM (OME scaffolding → human). Path C delivery (hybrid) активируется при первом contractor-#1. Client-private KB install становится productized add-on, не только consulting deliverable.

**Unlock (D15):** €200K gate открывает patents EU (€2-3.5K IP lawyer) + team growth + Secure Network build start. Alliance "informal" engagement (case-study channel + methodology-license proposals) может начинаться уже на этом gate как Partnership ICP (не Client ICP). [src:decisions/JETIX-PLAN.md#§4.1]

**Consulting BU split:** post-€100K [audio_511] — consulting team + sales team разделяются как первичные sub-units. mgmt-expert scalability-mode активирует deliverability projections под расширенный team.

### Gate G2→G3 (€200K → €1M) — Managed methodology

**Shift:** consulting эволюционирует от per-client billable hours к managed methodology: fewer hourly engagements, больше productized packages, licensing Jetix methodology как standalone. Alliance Foundation methodology публикуется Apache 2.0 (per L6 ack Option C). Team 5-10 человек.

**Consulting позиционирование:** не "AI-консультанты на час" — "методология которую вы лицензируете и используете". Это первое приближение к USB-C standards-level play. Engagements становятся depth-first: меньше клиентов, глубже связь, выше margin. GDPR/compliance certification (ISO 27001 / BSI C5) должна быть live к этому gate — иначе enterprise Mittelstand pipeline не открывается. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§8]

### Gate G3→G4 ($1M → $100M) — Enterprise scale + Constellation hurdle

**Shift:** consulting BU — enterprise-scale с strict Constellation hurdle rate (≥30% margin sustained). Консалтинговые проекты которые не проходят hurdle → рутятся в §3.3 USB-C Integration Services (lower-margin productized). Team 20-50. Alliance AI Mittelstand = established consortium.

**Position:** §3.1 AI Consulting — не primary revenue, но qualification funnel к Alliance / USB-C Services / Secure Network membership. High-value engagements ($100K+) с Fortune-500-adjacent clients (Phase-3+ per D6 hard rule). [src:decisions/JETIX-PLAN.md#§5]

### Gate G4→G5 ($100M → $1T) — Qualification funnel

**Steady state:** consulting not primary revenue — это мощный **qualification funnel** к Alliance / USB-C platform / Secure Network membership. Team 50-100 (D26 target). Ruslan-independent delivery: methodology exported through licensing + roy-replication, не founder-hours. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]

---

## 9. Cross-direction dependencies

### §3.1 зависит от (upstream):

- **§3.9 Smart AI flagship narrative:** framing языка positioning для всех клиентских conversations. Без этой narrative layer консалтинг продаётся как generic AI consulting, не как infrastructure-play.
- **§3.4 Matchmaker Platform (Phase-1 manual Ruslan):** leads flow — specialists которых Jetix матчит ТАКЖЕ могут рутиться в consulting для complex tasks. Matchmaker = lead source для §3.1.
- **§3.7 Educational Products:** upsell path — клиент начинает с consulting engagement, потом переходит на methodology licensing / educational programs. §3.1 → §3.7 graduation track.

### §3.1 питает (downstream):

- **§3.3 USB-C Integration Services:** consulting clients — первые USB-C productization customers. Глубокий engagement выявляет интеграционные нужды (CRM + ERP + AI workflow), которые §3.3 берёт в productized form.
- **§3.5 Secure Network:** consulting clients которые прошли через полный engagement и aligned с Jetix philosophy → естественный graduation path в Secure Network membership post-G2.
- **§3.6 YouTube-analyzer SaaS:** consulting engagements с content-heavy clients (Startupper / блогеры) выявляют niches где YouTube-analyzer продуктово ценен. §3.1 = market intelligence source для §3.6 product discovery.

### Cross-cutting tension:

**§3.4 Matchmaker ↔ §3.1 Consulting:** двунаправленная зависимость. Consulting PRODUCES leads для Matchmaker (specialists которых Jetix matches через consulting relationship). Matchmaker ROUTES leads в Consulting (complex tasks которые выходят за пределы компетенции matched specialist — рутятся обратно к Jetix consulting team). Это бизнес-модельная петля reinforcement: каждый consulting engagement расширяет Matchmaker network; каждый Matchmaker match может стать consulting client. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§1-четыре-главных-вывода]

---

## 10. Open questions (≥2 required)

### OQ-3.1-A: Path A/B/C delivery model — когда переход?

**Tension (inherited Dissent 3):** KM-Architecture-Variants Dissent 3 ack'd Phase-A default = Path B (client-hosted, 70.7% GM). Strategic Insight §5 рекомендует Path C для Enterprise. Открытый вопрос: при каком конкретном trigger Phase-A переходит с Path B на Path C? Текущее operationalization: "G2 post-contractor-#1" — но что если первый enterprise client (Mittelstand €20M company) приходит на G1 и требует Path C? Нужен explicit decision rule: "если client revenue tier > €X AND требует GDPR audit trail → Path C overrides Path B default без ожидания G2". Пока этого правила нет, delivery team (Ruslan alone in Phase-A) может оказаться в position где Path B technically неadequate для конкретного клиента.

**Ownership для resolution:** L7 Business Deep-Dive должен зафиксировать decision tree per client-tier vs hosting model. Нельзя оставить implicit.

### OQ-3.1-B: ISO 27001 / BSI C5 certification — Phase 1 (€30-80K, 6-9 мес) или Phase 2 (post-€200K gate)?

**Tension:** для полноценного Mittelstand P1A pipeline (Archetype A) enterprise-grade data security certification — de-facto gate. Без ISO 27001 или BSI C5 крупный Mittelstand (€10M+ revenue) с compliance officer просто не рассматривает Jetix как поставщика. Стоимость сертификации: €30-80K + 6-9 месяцев активной работы. D15 revenue-gated: €200K checkpoint открывает серьёзные IP/legal расходы, но certification не naming explicitly в D15 unlock list.

**Sub-question:** Можно ли Phase-1 продавать Mittelstand без сертификации, если явно позиционировать "client-private on-prem" (Path B) как solution, а не managed service? Возможно клиент держит данные у себя полностью — тогда Jetix не является data processor по GDPR и сертификация не требуется для Phase-1. Этот аргумент ТРЕБУЕТ legal verification.

**Ownership:** L7 Business Deep-Dive + legal counsel (post-GmbH setup). Флаг на brigadier для escalation к HITL при первом Mittelstand enterprise lead.

### OQ-3.1-C: Timing split "consulting team + sales team" post-€100K

[audio_511] называет €100K как момент split consulting и sales в отдельные команды. Это не lock — это Ruslan voice в review. Нужна clarification: это hard trigger или guideline? Потому что если это hard trigger, то mgmt-expert должен планировать first hire (sales-focused) при €100K runway, а не при €200K gate. Конфликт с JETIX-PLAN §4 который называет first hires как Phase 1→2 transition (€50K → €200K). Разрешение: L7 owns final hire-trigger.

---

*End of §3.1 AI Consulting for complex tasks. Word count estimate: ~2 050 words. Cell C-02 complete.*
