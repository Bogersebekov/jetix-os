---
id: T-layer-7-business-trajectory-deep-dive-2026-04-25-§4-gate-triggers
title: "§4 5-Gate Migration Triggers Detailed"
type: cell-draft
cell: C-03
expert: systems-expert
mode: scalability
cycle_id: cyc-layer-7-business-trajectory-deep-dive-2026-04-25
created: 2026-04-25
word_floor: 2500-3500
antifragility_check: pass
sources:
  - decisions/JETIX-SYSTEM-OVERVIEW.md#§5
  - decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§13
  - decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11
  - decisions/JETIX-PLAN.md#§1-§6
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
  - decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md#§1
  - swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md
acceptance_predicate: "5 gate transitions detailed AND each gate carries all 7 dimensions AND master table 5×14 rows present AND BOSC-A-T-X per gate declared AND VSM level shift per gate named AND Ashby variety-budget break named AND M&A optionality mentioned at G2-G3 AND F-G-R per primary claim present."
---

# §4 5-Gate Migration Triggers — Детальная спецификация

> **Что этот раздел даёт.** §4 является state-transition спецификацией: описывает критерии перехода между 5 capital-deployment gates, что unlocks/sunsets на каждом переходе, куда сдвигается капитал, как меняется команда, при каком уровне риска gate НЕ активируется, и когда это происходит в реальном времени. §4 НЕ содержит per-direction тактику (та живёт в §13 evolution master) и НЕ является заменой §11 risk register — он питает оба этих раздела.
>
> **BOSC-A-T-X framework** применяется к каждому gate: какая из семи сил (Boundary / Operations / Scale / Composition / Agency / Time / eXternal) является первичным триггером. Источник: L5 §13.5 [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md].
>
> **Beer VSM level shift** применяется к каждому gate: на каком уровне VSM (L1 ops / L2 coord / L3 audit / L4 intel / L5 identity) происходит структурное изменение. Источник: L6 §11.3 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.3].
>
> **Антисфера:** NO M&A deep-dive (brief mention only at G2-G3 per Ruslan 25.04 directive). NO финансовых инструментов. NO реоткрытия 28 Locks.

---

## §4.0 Framing — Что именно gate-triggers специфицируют

Gate-trigger — это не бизнес-план и не список задач. Это **state-transition predicate**: набор бинарно проверяемых условий, выполнение которых означает, что система достигла нового равновесия и готова к следующему уровню сложности. В терминах Meadows: gate — это точка, где до-сих-пор-балансирующий цикл (e.g., «нет выручки → нет найма → нет scale → нет выручки») разрушается под давлением reinforcing-петли следующего уровня.

**Архитектурный принцип** (per JETIX-SYSTEM-OVERVIEW §5): ни один вариант системы не выживает все 5 gates в неизменном виде. Каждый upgrade — планированная migration с measurable trigger. Форсированный pivot под стрессом (e.g., нанять людей без €200K validation) стоит дороже, чем спокойный дождаться gate.

**7 измерений на каждом gate** (требование acceptance predicate):
1. Trigger condition — revenue cumulative + secondary signals
2. What unlocks — per direction + per layer (L1-L9 из SYSTEM-OVERVIEW §5)
3. What sunsets / decommissions — что Phase-1 паттерны уходят на покой
4. Capital allocation shift — reinvest / hire / build
5. Team changes — D26 trajectory
6. Risk threshold — rejection criteria (когда gate НЕ активируется)
7. Estimated calendar timing — месяцы от старта

**F-G-R на meta-claim этого раздела:**

Claim: «Gate-trigger как бинарный state-predicate (revenue cumulative + ≥2 leading indicators) значительно надёжнее pure-date-based milestone как инструмент управления transition, особенно в Phase A solo-operation где Ruslan — единственный контроллер всей системы.»

- F: F4 (operational convention; Meadows leverage-point framework + Beer VSM sequencing book-as-frame)
- ClaimScope: holds для solo-to-10-person trajectory (G0→G3); at G4 ($100M) институциональные инвесторы и Alliance governance добавляют внешние date-anchored обязательства
- R: Refuted если G1 (€50K) пропущен более чем на 60 дней без изменения exit-criteria (означает: predicates неверны, нужна revision); accepted если все 5 gates проходятся с revenue-predicate как первичным триггером без date-driven forced pivots

---

## §4.1 G0 → G1: €0 → €50K (Q2 2026)

### Trigger condition

**Primary (revenue):** Cumulative confirmed revenue €50K. Это единственная committed absolute date в всём плане — Q2 2026 [src:decisions/JETIX-PLAN.md#§1]. Revenue decomposition per CC-1: ~€30K из 2 productized contracts × 2 quarters (Path-B default, €7.5K/contract-quarter) + ~€35K из 233 hourly consulting hours @ €150/hr [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3].

**Secondary signals (2 минимум):**
- ≥2 productized contracts подписаны и выполняются (не только оплачены разово)
- ≥233 часов hourly consulting оказано (или эквивалентная revenue-комбинация)
- Продюсерский центр: ≥2 paying pilot clients с recurring retainer

### What unlocks

**Infrastructure / Legal:**
- GmbH open + Stripe live (€1 000–€1 500 GmbH setup per D15)
- Basic legal: NDA templates + consulting contracts + agent contracts formalized
- $1 000 публичный experiment запущен и задокументирован [src:decisions/JETIX-PLAN.md#§3.1 audio_483]

**По направлениям L5:**
- Продюсерский центр pilot → scaling investment (переходит из «первый клиент» в «2-3 клиента + content pipeline операционален»)
- USB-C Integration Services: architecture-design phase начинается как G2-precondition (не spend — дизайн)
- Patent landscape research budget €500–€1 500: IP-lawyer консультация (Phase-A preparation — precondition для EU patent application на G2)
- Matchmaker: первые 3–10 cumulative matches задокументированы; scoreboard начат

**По слоям SYSTEM-OVERVIEW §5:**
- L0 Foundation: GmbH + Stripe commit в git с провенансом; D25 company-as-code полностью в силе
- L1 Knowledge: A1 Karpathy++ substrate operational; wiki v3 spine built
- L2 Ingest: voice pipeline + manual /ingest с --anchor mandatory (D28)
- L3 Synthesis: 3+ swarm cycles compound завершены
- L4 Agent: 6 ROY + 14 legacy active; brigadier single committer
- L5 Product: AI Consulting + Продюсерский центр = primary revenue (оба active)
- L6 Business: ICP manual outreach active; Telegram chat 5–20 invite-based
- L7 Research: D14 revenue-instrumental only; patent landscape консультация начата
- L8 People: Solo Ruslan + Cloud Cowork; 0 hires
- L9 Governance: 28 Locks в силе; все gates Ruslan-HITL
- L-R Resource: manual budget; compute €200–€400/mo
- L-C Compute: 1 personal workstation
- L-B Brand: 1 landing + USB-C framing + document-compass
- L-P Life OS: manual journal + voice notes

### What sunsets

- Phase-0 «$0 heavy-spend solo earn» mode: per D15 после G1 выручка рейнвестируется (infra + legal + маленькие experiments allowed)
- Запрет на Продюсерский центр-спринты без первых paying clients снят — теперь есть social proof
- Чистый hourly-only mode (€150/hr unbundled) активно productize-ируется после G1: per D18, consulting evolves away from pure hours

### Capital allocation shift

- €2 000–€4 000 единовременно: GmbH setup + legal templates + patent консультация
- €200–€400/mo baseline compute (Phase-1 steady-state)
- On-demand contractors: дизайнер (~€500–€1 500/engagement), видеоредактор (~€300–€800/engagement), IP-lawyer консультация (~€500–€1 500)
- Zero payroll: 0 hires Phase-G0→G1

### Team changes

- Состав: solo Ruslan + Cloud Cowork (рабочий партнёр, не employee)
- On-demand contractors только: дизайнер / видео / legal
- D26: solo-with-team-ready scaffolding в силе; нет hires до G2
- Founder-dependency metric: 100% (норма Phase-1, target <30% к G4)

### Risk threshold — когда gate НЕ активируется

**REJECT G1 IF:**
- €50K revenue НЕ достигнута к Q3 2026 (60-дневный buffer после Q2): означает product-market signal не подтверждён → revision ICP или offer required перед G2-investment
- Продюсерский центр имеет 0 paying clients к Q2 2026 (single-direction dependency — риск R-1 из §11): gate активируется с CAVEAT — без Продюсерский центр validation G2 investments в Alliance и Secure Network преждевременны
- Только один клиент обеспечил весь revenue (>60% concentration): high dependency risk; G1 активируется но G2 triggers ужесточаются
- GmbH НЕ открыт и Stripe НЕ live: infrastructure не готова к Scale; pause G1 до legal close

**F-G-R на reject-condition:**
- F: F3 (multi-case pattern из solo-consulting failures: single-client concentration = systemic fragility)
- ClaimScope: holds в EU solo-consulting context; US can have higher single-client tolerance due to larger market
- R: Refuted если Ruslan закрывает €50K с 1 клиентом AND демонстрирует 2+ в pipeline (leading indicator компенсирует concentration)

### Calendar timing

- **Месяцы 1–6 от старта системы (Q1–Q2 2026, текущий цикл)**
- Committed absolute date: Q2 2026 — единственная в плане [src:decisions/JETIX-PLAN.md#§1]

### BOSC-A-T-X первичный триггер

**C+S (Composition + Scale)**

Swarm устанавливает measurement substrate (OPP-01 eval harness), закрывая Meadows L6 sensor void. Система переходит от open-loop к closed-loop: впервые появляются количественно измеримые KPI (часы Ruslan-архитектора / revenue / cash reserve). Composition меняется потому что GmbH + Stripe добавляют два новых компонента в юридическую структуру системы.

MHT event: **Phase Promotion** — swarm из spec-only переходит в operational; health.md counters начинают производить signal.

### VSM level shift

**L1 only: Ruslan одновременно L1 + L2 + L3 + L4 + L5.** Это функционально, но не масштабируется: один человек = operations (L1) + coordination (L2) + audit (L3) + futures (L4) + identity (L5). G1 не меняет VSM-уровни — это подтверждение что solo-mode выдержал первую scale-test.

### Ashby requisite variety

**Variety budget на G1:** Ruslan-individual variety (ICP judgments, matching, quality curation) достаточна для 0–20 членов community + 2–5 clients. Нет variety-break на G1 — solo controller covers the system. Break придёт на G1→G2 (50+ members).

---

## §4.2 G1 → G2: €50K → €200K (Validation Gate)

### Trigger condition

**Primary (revenue):** Cumulative revenue €200K confirmed. Это «validation gate» per JETIX-PLAN §4.1: подтверждение что операционная модель scales beyond solo [src:decisions/JETIX-PLAN.md#§4.1].

**Secondary signals (≥2 из 3):**
- GmbH operational ≥6 месяцев (legal entity зрелая, не только открытая)
- ≥2 productized contracts retained beyond Phase-1 (не разовые; recurring relationship)
- ≥5 Alliance warm contacts с ≥5h/week commitment (leading indicator Alliance readiness)

### What unlocks

**Legal / IP:**
- EU patent application initiated (€2 000–€3 500 IP lawyer per OT4 / D15 unlock)
- Alliance governance decision: Option C Hybrid (Foundation non-profit + Jetix-Corp GmbH) per L6 ack [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§5]
- Alliance legal incorporation начата (€0–€2 000 DE eingetragener Verein consultation — CF-02 D15 tension, Ruslan ack required per §12 Q-12 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§12])

**По направлениям L5:**
- USB-C Integration Services: architecture-design phase → first productized client engagement
- Matchmaker: AI-smoothed coordination design begins (≥30 match scoreboard records + ≥15 portraits = precondition per L6 §6.4 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§6.4])
- Secure Network: architecture-design phase (Telegram sub-channels structure, D22 formal protocol, digital portrait template)
- Token economy exploration: D23 Option B Phase-2 internal utility design (not launch — design only)
- Path A/B/C empirical validation begins: first 3–5 contracts give data to resolve D-USB-C-1 dissent
- Educational: methodology repo V1 discussion begins; D27 fork-and-merge governance discussion starts

**M&A direction Phase-2+ optionality (brief mention per Ruslan 25.04 directive):** Если к моменту G2 (a) co-founder с M&A background secured AND (b) €200–500K capital available через co-founder или партнёров AND (c) Mittelstand succession window 2026–2028 оценивается как open: → выносим отдельный M&A deep-dive cycle на рассмотрение. НЕ активируем автоматически — HITL decision. Dedicated cycle scheduled when Ruslan re-prioritizes post-€200K [src:decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md#§0 + status_note].

**По слоям SYSTEM-OVERVIEW §5:**
- L0: + CI pipeline + multi-dev commit discipline (first 2–3 hires onboarded)
- L1: + A2 mini-swarm substrate; topic-wikis per domain expert начинаются
- L2: + crawlers V1 (systematic ingest расширяется)
- L3: + skills codified (первые pattern-libraries из Phase-1 compound cycles)
- L4: + first 2–3 hires onboarded в agent-contract protocols (OME Foundation)
- L5: + Matchmaker AI-smoothed design; USB-C first client; Secure Network design
- L6: + DACH Mittelstand outbound initiated; systematic content cadence; Alliance formal discussion
- L7: + EU patent process initiated; first patent landscape research published
- L8: + first 2–3 hires; Secure Network design team; D15 ≥€50K confirmed
- L9: + first gate-delegation (Ruslan delegates first L1 tasks)
- L-R: + per-agent dashboard prototype; first payroll line
- L-C: + 1 dedicated server + GPU (EU-sovereign hosting Hetzner / OVH)
- L-B: + 3 landings (Авантюристы / Инвесторы / Работники мечты per L6 §7.5)
- L-P: + auto-logging prototype

### What sunsets

- Pure-hours consulting (€150/hr unbundled) активно productize-ируется out per D18: становится minority revenue, не primary
- Solo-delivery-only clients депriорitize-ируются (в пользу clients открытых к productized engagement)
- Cloud Cowork как единственный «partner» mode: первые hires берут часть delivery
- Phase-1 D22 qualification «только в голове Ruslan» заменяется written D22 protocol + structured interview

### Capital allocation shift

- **Payroll: €60–90K/yr × 2 hires = €120–180K/yr** (sales-focused English-speaking + operations/PM)
- **Legal + patents: €5–8K** (EU patent application + Alliance incorporation)
- **Office/infra: €3–5K/mo** (EU-sovereign server + GPU + office if needed; compute scale-up)
- **Matchmaker agent development: €5–15K** capex (per L6 §6.6 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§6.6])
- **Continuing compute: €400–800/mo** (scaled from Phase-1 baseline)

### Team changes

- **+2–3 hires:** hire #1 Sales-focused (English-speaking market close); hire #2 Operations/PM (OME agent-contract protocols)
- Optional hire #3: part-time assistant (admin / scheduling) если time-pressure
- D26 trajectory: solo → 2–3 (G2) → 5–10 (G3) → 20–50 (G4) → 50–100 steady-state (G5) [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]
- Founder-dependency metric: target trending down от 100% → 70–80% к концу G2

### Risk threshold — когда gate НЕ активируется

**REJECT G2 IF:**
- Alliance governance (Option A/B/C) unresolved ≥4 weeks до закрытия €200K (filing lag 4–12 weeks DE — означает formal Alliance не откроется 1–3 месяца post-gate, momentum gap per L6 §11 D-S11-1 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.2])
- First hire candidate не прошёл D22 5-criteria filter (hiring someone who fails own filter = identity-grammar violation)
- EU patent application невозможна без prior art search (который ещё не сделан): pause patent spend, не gate
- Single-client revenue concentration >50% на момент €200K: gate активируется с CAVEAT — G3 investments в platform требуют revenue diversification plan

### Calendar timing

- **Месяцы 7–15 от старта (~Q3 2026 — Q1 2027)**
- Range широкий из-за зависимости от рыночных условий; leading indicators могут ускорить или замедлить

### BOSC-A-T-X первичный триггер

**A (Agency)**

Solo → team: первая смена Agency в системе. До G2 единственный агент принятия решений — Ruslan. На G2 появляются hires с delegated authority. Это structural shift: больше нельзя оптимизировать систему как single-agent. Beer VSM L2 (coordination) впервые требует formal existence.

MHT event: **Role-Lift** — founder поднимается от L1 (execution) к L2/L3 (coordination/audit); первые hires берут L1 execution.

### VSM level shift

**L1 → L1+L2: первое разделение execution от coordination.** Ruslan делегирует L1 (execution) к hires; сам поднимается к L2 coordination (orchestration first hires) + сохраняет L3/L4/L5. Critical transition: без formal L2 coordination mechanism (briefing protocols, OME agent-contracts, weekly sync) delegation деградирует обратно в micro-management.

### Ashby requisite variety

**G1→G2 variety-break:** Ruslan individual variety достаточна для ≤20 members. При 50–200 members + 2–3 hires controller variety must expand. Compensating mechanism: D22 written protocol + digital portrait template + OME agent-contract protocols — encoding judgment в replicable filter. Без этой amplification Ruslan = bottleneck; система не может масштабироваться [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.3 Ashby].

---

## §4.3 G2 → G3: €200K → €1M (Phase 2 Core)

### Trigger condition

**Primary (revenue):** Revenue run-rate €1M **sustained 3-month run-rate** (НЕ только snapshot). Run-rate критичен: снимок €1M может быть аномалией; 3-month sustained = pattern.

**Secondary signals (≥2 из 4):**
- ≥5 formal Alliance members с documented ≥5h/week commitment
- Matchmaker: ≥10 successful matches с documented outcomes
- Secure Network: ≥50 total members actively posting + thematic sub-channels live
- Digital portrait template deployed + ≥5 portraits filled (matchmaker precondition)

### What unlocks

**Platform / Product:**
- Secure Network platform launch (post-design phase: Telegram sub-channels per 11 archetypes + складчина + subscription tiers live)
- Matchmaker Platform MVP: structured task-posting, reputation scoring, bid mechanics, escrow (capex €50–100K per L6 §6.6 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§6.6])
- USB-C Integration Services fully productized (all 3 Paths A/B/C supported, 5–20 client deployments)
- Educational methodology repo V1 published (per D27; fork-and-merge governance model decided — BDFL Phase-1 Ruslan)
- D27 fork-community opens for first Alliance members
- Token economy Phase-2 internal utility: D23 Option B — specialist compensation + складчина — NOT public [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3]
- Revenue-share partnerships ($10K/mo × 3–5 partners per D15)
- Mittelstand AI Alliance public EISA-moment positioning: Alliance is public, not just internal concept

**По слоям SYSTEM-OVERVIEW §5:**
- L0: + federation forks (первые clients/partners получают fork Jetix upstream)
- L1: + A3 GraphRAG substrate; client-private namespaces (Path A/B/C)
- L2: + full crawler suite; systematic signal-net
- L3: + cross-project compound (methodology patterns кристаллизуются)
- L4: + team 5–10; sub-brigadiers emerging; first roy-leaders inside Jetix
- L5: + Secure Network launch + USB-C services + methodology repo V1
- L6: + €1M/mo pipeline; thought leadership DACH conferences; first external publication partnerships
- L7: + first Alliance methodology contributions; patent filed (EU)
- L8: + team 5–10 hires; D19 holding-structure кристаллизуется
- L9: + fork-and-merge governance active; Alliance incorporated (Option C)
- L-R: + per-roy P&L (holding-style resource accounting begins)
- L-C: + data-center start (partnership EU-sovereign: Hetzner / OVH / Deutsche Telekom)
- L-B: + USB-C public narrative; DACH-language content
- L-P: + systematic wellness protocol (life-OS не только журнал)

### What sunsets

- Paid-ads campaigns без ROAS ≥3× retired (per Meadows L12 — constants/parameters interventions дорогие и малоэффективные относительно structural leverage)
- Manual Ruslan-only matchmaker ceiling officially replaced: протокол + AI-smoothed agent + platform design
- Consulting direction как pure-solo-Ruslan-delivery model: delivery теперь через team
- Hourly consulting (<€150/hr unbundled) активно выводится — minority channel only (< 20% revenue)

### Capital allocation shift

- **Team payroll: €600K–€1M/yr** (5–10 specialists × €60–100K/yr blended)
- **Platform engineering: €200–500K** (Matchmaker MVP + Secure Network platform + USB-C deployment scripts)
- **Alliance dues + memberships + events: €20–50K/yr**
- **EU-sovereign compute partnership: €30–80K/yr** (Phase-3 start toward own data-center)
- **Educational content production: €30–60K** (methodology repo V1 + first cohort infrastructure)

### Team changes

- **+3–7 specialists:** content / tech-engineer (USB-C deployments) / dedicated operations lead / first PM/project lead / роль Alliance coordinator
- First roy-leaders inside Jetix emerging (D21: specialists who demonstrated D22 alignment in Phase-1 get elevated)
- D26: team 5–10 (G3); holding-structure начинает появляться как organizational container
- Founder-dependency metric: target 60–70% (still high; L3 audit/optimization emerging)

### Risk threshold — когда gate НЕ активируется

**REJECT G3 IF:**
- Senge «Limits to Growth» balancing constraint fires: portrait-completion < 50% among active members (matchmaker value entirely depends on portrait graph density; if only 50 of 200 members have filled portraits → AI-agent match quality poor → network effects не materialise per L6 §11.2 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.2 G3 bottleneck])
- Single-client concentration > 30% revenue (structural fragility before platform spend)
- USB-C Path A/B/C dissent D-USB-C-1 still unresolved после 3–5 contracts (means pricing model unclear → platform build premature)
- EU data-center partnership contract not signed (Secure Network launch requires EU-sovereign compute commitment)

### Calendar timing

- **Месяцы 16–36 от старта (~Q2 2027 — Q4 2028)**
- Range 20 месяцев широкий: зависит от Alliance momentum + hiring speed + platform development cycles

### BOSC-A-T-X первичный триггер

**C+S (Composition + Scale)**

4 направления (USB-C + Matchmaker + Secure Network + Educational) переходят от «preparing» к «active» одновременно. Composition системы меняется кардинально: добавляются компоненты с network effects (Secure Network, Matchmaker Platform) — система quality-changes, не just grows. Это не просто больше того же.

MHT event: **Phase Promotion** — система переходит от «продажа услуг Ruslan'а» к «platform-enabled value creation»; VSM Level-3 впервые становится explicit, budgeted, load-bearing.

### VSM level shift

**+L3: audit/optimization function explicit.** Matchmaker KPI tracking (match rate, NPS, portfolio-completion %) + portrait quality review + Secure Network subscription churn analysis = первый L3 (System 3 Beer) как отдельная функция с own budget и own metrics. До G3 L3 жил в голове Ruslan ad hoc. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.3 Beer VSM table]

### Ashby requisite variety

**G3 variety-break:** при 200–1 000 members + platform + multiple directions, никакой единственный человек-контроллер не имеет достаточного variety. Compensating: L4 agent layer (6 ROY + 14 legacy) functioning as distributed controller с far higher variety. L4 agents становятся load-bearing, а не optional. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.3 Ashby G3 break]

---

## §4.4 G3 → G4: €1M → $100M (Phase 3 Maturation)

### Trigger condition

**Primary (revenue или market cap):** Revenue или market cap $100M sustained 4 quarters (не снимок — sustained trend).

**Secondary signals (≥2 из 3):**
- Ruslan founder-dependency metric < 30% (per JETIX-PLAN §1 dashboard [src:decisions/JETIX-PLAN.md#§1])
- ≥1 external roy independently achieving ≥$10M revenue с Jetix methodology
- Alliance methodology-parliament processed ≥3 upstream merge-back contributions

### What unlocks

**Platform / Product scale:**
- YouTube-analyzer SaaS launch (Phase-3+ per L5 §2.1; deferred to G4 per ack Q-02 [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3])
- Token economy Phase-2 internal utility active: specialist compensation + складчина token pools (D23 Option B internal; NOT public — public requires separate Ruslan ack)
- Secure Network international sub-networks (multi-language + Phase-3+ beyond DACH)
- USB-C Integration Services: 50–200 client deployments (standard-layer positioning)
- Distilled Mittelstand LLM proof-of-concept (BIOS-equivalent per STRATEGIC-INSIGHT §8 rec 7 [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md])
- D24 open-source research direction activates
- Holding structure formally crystallizes (D19 + D21)
- First replicated roy ($10M–$100M revenue per D21)
- Educational: self-serve G3→G4 (cohort-first validated per ack Q-04 [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3])

**По слоям SYSTEM-OVERVIEW §5:**
- L0: + legal audit-trail (SOC2/GDPR + git-provenance as formal compliance layer)
- L1: + federated wikis (each roy maintains own wiki; edges.jsonl cross-federated)
- L2: + industry-standard signal-net (automated crawlers per vertical)
- L3: + meta-compound (cross-roy pattern distillation)
- L4: + Phase-B brigadier-split (if VSM/recursion artefact volume > 60% — split-trigger evaluation)
- L5: + YouTube-SaaS + educational scale + token internal
- L6: + roy-replication external; Alliance methodology-parliament governance active; own conference/summit feasible
- L7: + D24 open-source research active; distilled Mittelstand LLM PoC
- L8: + 20–50 people; Alliance formalized + first external roys operational
- L9: + Alliance methodology-parliament; Kelly portfolio multi-roy
- L-R: + Kelly portfolio multi-roy P&L
- L-C: + multi-region + redundant; EU sovereign data-center start; decision partner Hetzner/OVH vs own-build per L5 §14.3 Dissent D-TOOLS-2
- L-B: + civilizational narrative draft; Alliance brand weight
- L-P: + life-OS-for-millionaires as Phase-3 product concept (if Ruslan acks)

### What sunsets

- Business units below 30% Constellation-style hurdle rate sustained 4 quarters actively wind down
- Solo-founder-dependent service delivery активно wound down: D26 + D21 absorb delivery capacity
- Consulting как standalone revenue entry point: becomes minority (<10% revenue) + sales-motion entry, NOT primary line
- Phase-3 Anthropic Solution Partner status → formal partnership с contracts (Phase-2 status upgraded)

### Capital allocation shift

- **Team payroll: $5–10M/yr** (20–50 people blended, including first external roy-leaders)
- **Alliance + roy seed capital: $2–5M** (first roys в new niches)
- **Data-center investment decision: partnership Hetzner/OVH ($200K–1M capex) vs own-build ($5–20M) — G3→G4 trigger per L5 §14.3**
- **YouTube-analyzer engineering: $500K–2M** (data pipeline + API layer + SaaS infra)
- **Educational scale: $300K–1M** (cohort infrastructure → self-serve platform)

### Team changes

- **+10–30 specialists** (20–50 total): first external roy-leaders operational; Alliance coordinator team; YouTube-analyzer engineering pod; educational content scale
- First external roys: команды по 3–7 человек в других нишах/verticals используют Jetix methodology
- D26: 20–50 людей в core; holding-structure with roys = enterprise-fast architecture
- Founder-dependency metric: target <30% (критерий для gate migration to G4)

### Risk threshold — когда gate НЕ активируется

**REJECT G4 IF:**
- Ashby variety-budget exceeds single-brigadier swarm capacity without split (если brigadier-split не выполнен — coordination collapses under 20–50-person + Alliance complexity)
- Founder-dependency metric ≥30% (per JETIX-PLAN §8.2 dashboard [src:decisions/JETIX-PLAN.md#§1]): означает масштаб создаётся без реального delegation — структурно fragile
- Alliance methodology-parliament не сформирован перед G4 arrival: при первых 100–500 Alliance members без parliament governance → canonical methodology drift от N diverging roys (Senge «Accidental Adversaries») [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.2 G4 bottleneck]
- Token economy Phase-2 internal без legal review (D23 + EU MiCA + US Howey pre-review required перед любым activation)

### Calendar timing

- **Месяцы 37–72 от старта (~2029–2031)**
- Wide range: зависит от market environment + Alliance growth rate + roy-replication speed

### BOSC-A-T-X первичный триггер

**T (Time)**

Time-horizon сдвигается от quarterly к multi-year planning. Alliance methodology-parliament (L4 Beer VSM) function требует multi-year roadmap: что methodology will look like in 3–5 years? Сдвиг: reinforcing loops с longer time constants (roy-replication: 2–3 года на roy, не 2–3 месяца) начинают доминировать над short-cycle consulting loops.

MHT event: **Context Reframe** — planning artefacts re-anchored к multi-year horizon; swarm itself audited/split (VSM L3 audit function as distinct sub-system); brigadier-split evaluation fires.

### VSM level shift

**+L4: intelligence/futures explicitly instantiated.** Alliance methodology-parliament = new agent с explicit goal: process future-facing methodology updates from downstream roys + propose upstream changes. L4 function до G4 была в голове Ruslan (futures = «что-то подумаю»). После G4 = distinct sub-system с own operating cadence (quarterly parliament sessions + annual methodology review). Ruslan lifts от L3 к pure L4/L5. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.3 Beer VSM table G4]

### Ashby requisite variety

**G4 (multi-language + multi-niche + multi-roy + Alliance 100–500) exceeds любой single-human controller и любой single-brigadier swarm.** Compensating: Alliance methodology-parliament (distributed governance с variety proportional к ecosystem variety) + sub-brigadiers per roy. Brigadier-split evaluation fires (per systems-expert §1d split-trigger: VSM/recursion artefact volume > 60% последних 50 returns).

---

## §4.5 G4 → G5: $100M → $100B → $1T (Civilizational Scale)

### Trigger condition

**Primary (market cap trajectory):** Market cap $100B → $1T world-record attempt (XEI precedent: $100B in 2 years). Это не discrete trigger с единственной датой — это trajectory endpoint.

**Secondary signals (≥2 из 3):**
- ≥1 external roy independently achieving ≥$100M revenue
- Alliance ≥500 formal members с regulatory presence (EU AI Act conversations или USB-C standard-body forums)
- Ruslan founder-dependency metric < 10% (civilizational infrastructure не может зависеть от одного человека)

### What unlocks

**Civilizational scale:**
- Token Phase-3+ public layer (D23 Option B/C, ТОЛЬКО если Ruslan ack — NOT automatic; retirement clause applies if MiCA/Howey prohibitive OR $100M ARR achieved without specialist-friction [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3])
- Mittelstand AI Alliance civilizational positioning: 1 000–5 000+ formal members; ISO + EU AI Act regulatory standards-body conversations
- USB-C public launch (D20 protocol = de facto standard): multiple organizations implement
- Multi-roy federation (D21): dozens of active forks; D27 best mutations return upstream
- Jetix own data-center + electricity sources (Phase-3+ per JETIX-PLAN §6; L-C layer)
- Constitutional-amendment process для Alliance governance (VSM Level-5 distributed)

**По слоям SYSTEM-OVERVIEW §5:**
- L0: + constitutional-amendment process (git-provenance as legal-grade audit-trail)
- L1: + Mittelstand AI Alliance federated wiki (каждый roy contributes)
- L2: + sovereign data network
- L3: + federated compound (cross-roy pattern distillation at civilizational scale)
- L4: + 50–100 humans + sub-brigadiers; multi-roy ecosystem; meta-coordinator role
- L5: + tokens Phase-3+ public (if acked); civilizational revenue
- L6: + global regulatory engagement; USB-C narrative international press; Alliance 1 000–5 000+
- L7: + published research (D24); standards contribution; Mittelstand LLM as standard
- L8: + civilization co-governance (Alliance as co-stakeholder)
- L9: + civilization co-govern (constitutional governance)
- L-R: + civilizational resource-accounting
- L-C: + Jetix own data-center + power sources (электростанции)
- L-B: + global USB-C narrative; civilizational brand
- L-P: + externalized life-OS product-line

### What sunsets

- Solo-founder-dependent services entirely: consulting direction как foundational revenue → sunset (replaced by USB-C standard-layer + Alliance methodology licensing per D26 + D27)
- Consulting direction: devient minority (<5% revenue) → potentially sunset as own direction (absorbed by USB-C standard licensing)
- Ruslan as operational decision-maker on routine matters (L5 identity/policy distributed to constitutional governance)

### Capital allocation shift

- **Holding-level consolidation:** Kelly portfolio logic across multi-roy ecosystem
- **Sovereign data-center:** $50–200M capex (own infrastructure + power)
- **Alliance infrastructure:** civilizational spend; regulatory engagement budget
- **Team:** 50–100 steady-state core per D26 + multi-roy ecosystem (hundreds total)

### Team changes

- **50–100 steady-state per D26** в Jetix core [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]
- Multi-roy ecosystem: dozens of external roys с own teams (не в headcount Jetix core)
- Meta-coordinator role: Ruslan (или successor) as System-5 (identity/policy) в Alliance governance
- Constitutional governance: Alliance methodology-parliament + amendment process = replaces founder-HITL для routine methodological decisions

### Risk threshold — когда gate НЕ активируется

**REJECT G5 IF:**
- Identity-grammar (D1, D3, D8, D9, D12, D13, D22) drift > 30% в Alliance founding documents (означает: civilizational scale erodes core identity — это failure mode, не growth)
- Constitutional-amendment process не embedded в Alliance governance до G4 completion (пытаться установить retro-actively при 1 000+ members = structural change > 30% threshold = fragile per antifragility check)
- Founder-dependency metric > 10% (единственный человек как bottleneck для цивилизационного стандарта = single-point-of-failure, unacceptable)

### Calendar timing

- **Месяцы 73+ (2032+); D19 $1T trajectory endpoint** [src:decisions/JETIX-VISION.md]
- По XEI precedent: $100B за 2 года возможно; $1T = trajectory, не deadline

### BOSC-A-T-X первичный триггер

**X+B (eXternal + Boundary)**

Regulatory bodies входят в system boundary: EU AI Act standards bodies, ISO, national regulators начинают рассматривать Alliance как institutional stakeholder (а не просто частную компанию). Граница системы расширяется: регуляторы становятся constituents, а не externalities.

MHT event: **Fusion** — regulators/standards bodies merging into the holon as co-participants (не adversaries). Alliance говорит от имени консорциума с institutional gravity.

### VSM level shift

**+L5: identity/policy distributed к constitutional governance.** Ни один человек не держит L5 (identity). L5 embedded в founding documents + amendment process. Alliance constitution + Jetix canonical upstream + roy-replication methodology template = distributed L5. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.3 Beer VSM table G5]

### Ashby requisite variety

**G5 variety-break (10 000+ members + dozens of roys + multi-jurisdictional holding):** Variety exceeds any agent layer или core team. Compensating: constitutional-amendment process (Beer VSM Level-5) + Alliance methodology-parliament (Level-4) + sub-brigadiers per roy — distributed governance с variety proportional to ecosystem variety. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.3 Ashby G5 break]

---

## §4.6 Master Table — 5 Gates × 14 Layers

> Структура строк = 14 layers из JETIX-SYSTEM-OVERVIEW §5 [src:decisions/JETIX-SYSTEM-OVERVIEW.md#§5]. L7-specific expansion: финансовое измерение каждого слоя на каждом gate. Verbatim structure из SYSTEM-OVERVIEW §5 preserved; расширено для L7 financial + operational detail.

| Layer | G1 €50K Q2 2026 | G2 €200K | G3 €1M run-rate | G4 $100M sustained | G5 $100B → $1T |
|---|---|---|---|---|---|
| **L0 Foundation (Company-as-Code)** | GmbH + Stripe live; D25 full in force; single-dev commits; atomic provenance; 3+ cycles в git log | + CI pipeline; multi-dev discipline; branch protection; pre-commit hooks | + federation: first client forks; D27 upstream curated by Ruslan (BDFL) | + legal audit-trail (SOC2/GDPR grade); federated git network emerging | + constitutional-amendment process в git-provenance; каждый amendment = commit |
| **L1 Knowledge** | wiki v3 spine (53 dirs, 9 types); D28 query-driven ingest; Private Library; A1 Karpathy++ substrate | + A2 mini-swarm substrate; topic-wikis per domain expert начинаются; first client-private namespaces | + A3 GraphRAG; cross-project compound; methodology patterns кристаллизованы | + federated wikis per roy; industry-signal integration | + Mittelstand AI Alliance federated KB; sovereign data network |
| **L2 Ingest & Signal** | voice pipeline + manual /ingest + --anchor mandatory; 3–5 sources/week | + crawlers V1; systematic content cadence; bloggers + podcast ingest | + full crawler suite; DACH-language signal-net; USB-C deployment signal | + industry-standard signal-net (automated per vertical per roy) | + sovereign data network; own-infrastructure ingest |
| **L3 Synthesis & Compound** | 40/10/40/10 CE cadence active; 3+ cycles completed; pattern-capture начато | + skills codified; first pattern-libraries from compound cycles | + cross-project compound; methodology repo V1 = distilled compound output | + meta-compound: cross-roy pattern distillation; Alliance parliament as L3 mechanism | + federated compound; civilizational pattern distillation |
| **L4 Agent Layer** | 6 ROY + 14 legacy; brigadier sole committer; 5×4 mode matrix; 5-layer memory | + first 2–3 human hires onboarded в agent-contract protocols (OME); agent + human layer formalized | + team 5–10; sub-brigadiers emerging; first roy-leaders inside Jetix | + Phase-B brigadier-split evaluation; 20–50 people; first external roys operational | + 50–100 humans steady-state (D26); sub-brigadiers per roy; meta-coordinator |
| **L5 Product & Services** | Consulting (P1A core) + Продюсерский центр (P1A core); Matchmaker informal; 0 platform | + USB-C first client; Matchmaker AI-smoothed design; Secure Network design; Path A/B/C validation | + Secure Network launch; Matchmaker MVP; USB-C productized (3 paths); Educational repo V1; token internal D23 | + YouTube-SaaS launch; token internal active; Educational self-serve; roy-replication 50–200 USB-C deployments | + token public (if acked); civilizational USB-C standard; roy-replication federation |
| **L6 Business & Trajectory** | Manual outreach (LinkedIn + warm); ICP expanded spectrum; €65K blended target vs €50K gate | + DACH outbound initiated; content cadence systematic; Alliance formal discussion; first 5–10 formal members | + €1M pipeline; DACH primary; Alliance EISA-moment; thought leadership; matchmaker fees emerging | + roy-replication external revenue; Alliance dues + methodology licensing = distinct revenue line; consulting <10% | + civilizational revenue; USB-C standard licensing; token public layer (if acked) |
| **L7 Research** | D14 revenue-instrumental only; patent landscape консультация (€500–€1 500) | + EU patent application initiated (€2 000–€3 500); IP lawyer engaged | + first Alliance methodology contributions; D13 Closed core/Open surface operationalized | + D24 open-source research active; distilled Mittelstand LLM PoC; published research | + published research; standards contribution; Mittelstand LLM as industry standard |
| **L8 People & Alliance** | Solo + Cloud Cowork; 0 hires; 5–20 Telegram chat; Alliance = concept | + first 2–3 hires; Alliance Option C legal starts; first 5–10 formal members ≥5h/week | + team 5–10; Alliance ≥50 formal members; Foundation incorporated (Option C); fork-community open | + team 20–50; Alliance 100–500 formal members; first external roys operational | + team 50–100 steady-state (D26); Alliance 1 000–5 000+; multi-roy ecosystem |
| **L9 Governance & Evolution** | 28 Locks in force; all gates Ruslan-HITL; no delegation | + first gate-delegation (Ruslan delegates L1 tasks); Alliance governance decision acked | + fork-and-merge governance active; Alliance incorporated; D27 BDFL Phase-1; first merge-backs designed | + Alliance methodology-parliament active; holding structure formalized; Kelly portfolio logic | + constitutional-amendment process; VSM L5 distributed; multi-jurisdiction holding |
| **L-R Resource Management** | Manual budget; Ruslan-only P&L; compute €200–400/mo; 0 payroll | + per-agent dashboard prototype; payroll line (2–3 hires); per-direction P&L | + per-roy P&L (holding-style); revenue-share partnerships ($10K/mo × 3–5); compute ~€3–5K/mo | + Kelly portfolio multi-roy P&L; Alliance dues revenue; data-center investment decision | + civilizational resource-accounting; Kelly portfolio at scale; token liquidity (if acked) |
| **L-C Compute & Infrastructure** | 1 personal workstation; Max-subscription Claude; Groq API; ~€200–400/mo | + 1 dedicated EU-sovereign server + GPU (Hetzner / OVH); ~€500–1 500/mo | + EU-sovereign data-center partnership; Path A/B/C client-hosted compute; ~€3–8K/mo | + multi-region redundant; data-center start (partnership vs own decision); $200K–1M capex | + Jetix own data-center + power sources (электростанции); sovereign infrastructure |
| **L-B Brand & Narrative** | 1 landing + USB-C framing (D20) + document-compass; Ruslan personal voice | + 3 landings (Авантюристы / Инвесторы / Работники мечты); DACH-language content begins | + USB-C public narrative; DACH-language thought leadership; Alliance brand umbrella | + civilizational narrative draft; Alliance as institutional brand; own conference/summit | + global USB-C narrative; Alliance as civilizational infrastructure brand |
| **L-P Life OS** | Manual journal + voice notes; personal tracking ad hoc | + auto-logging prototype; personal dashboard | + systematic wellness protocol; life-OS integrated с business OS | + life-OS-for-millionaires product concept (if Ruslan acks); wellness institutionalized | + externalized life-OS product-line; founder transition planning |

---

## §4.7 Cross-Section Reconciliation Note

### Reconciliation с L6 §11 Evolution

§4 gate triggers **совместимы** с L6 §11.1 Master Evolution Table [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.1] без противоречий:

- Membership cardinality: 5–20 (G1) → 50–200 (G2) → 200–1 000 (G3) → 1 000–5 000 (G4) → 10 000+ (G5) — идентично §11.1
- Team (D26): solo → 2–3 → 5–10 → 20–50 → 50–100 — идентично §11.1
- Alliance state per gate — идентично §11.1, детализировано в §4.2–§4.5

**Одно уточнение:** §4.3 добавляет "sustained 3-month run-rate €1M" вместо snapshot €1M. Это более строгий trigger чем §11.2 G3 migration trigger (который говорит просто «€1M cumulative»). §4 более conservative — снижает риск false-positive gate activation. Рекомендация: brigadier reconciles формулировку в canonical document в пользу "3-month sustained run-rate" как более robust.

### Reconciliation с L5 §13 Evolution Master

§4 gate triggers совместимы с L5 §13 (Phase activation per direction):

- USB-C: first client G1→G2 (§4.2 ✓ + L5 §13)
- Matchmaker: manual G0→G1 → AI-smoothed G1→G2 → platform G2→G3 (§4.2/4.3 ✓ + L5 §3.4)
- Secure Network: design G1→G2 → launch G2→G3 (§4.2/4.3 ✓ + L6 §10)
- YouTube-analyzer: G3→G4 (§4.4 ✓ + ack Q-02)
- Educational: methodology repo G2→G3 → self-serve G3→G4 (§4.3/4.4 ✓ + ack Q-04)
- Tokens: internal G2→G3 design → internal active G3→G4 → public G4→G5 (if acked) (§4.3/4.4/4.5 ✓ + ack Q-05)

**Нет конфликтов.** §4 добавляет финансовые dimension и secondary signals; §13 добавляет per-direction тактику. Оба совместимы.

### Feed into §11 Risk Register

Следующие rejection criteria из §4 питают kill-criteria §11 risk register:

- G1 reject: €50K miss beyond Q3 2026 → R-1 (Phase-1 revenue miss)
- G2 reject: Alliance governance unresolved → R-7 (Alliance filing lag)
- G3 reject: portrait-completion < 50% → R-3 (matchmaker quality degradation)
- G4 reject: founder-dependency ≥30% → R-6 (scale without delegation)
- G5 reject: identity-grammar drift → R-12 (civilizational identity erosion)

### Feed into §10 Compensation + Team Trajectory

D26 Team 50–100 trajectory (§4 §4.1–§4.5) directly feeds §10 compensation model:

- G1: 0 payroll (solo)
- G2: €120–180K/yr (2–3 hires × €60–90K)
- G3: €600K–1M/yr (5–10 specialists)
- G4: $5–10M/yr (20–50 people + external roy-leaders)
- G5: $10–25M/yr steady-state (50–100 core + sub-brigadiers)

### Feed into §13 Evolution Master

§4 BOSC-A-T-X per gate является input для §13 Evolution Master Table (per L5 §13.5 framework). Каждый gate trigger указывает какой из 7 forces является primary driver, что позволяет §13 правильно последовательность direction-activation.

---

## §X Cell C-03 Self-Improvement Notes

**Pattern 1 — Gate trigger = revenue cumulative + minimum 2 secondary signals.**
Единственный revenue trigger (€50K / €200K / €1M etc.) создаёт false-positive риск: можно иметь revenue но быть структурно не готовым. G2 с €200K revenue но без Alliance governance decision = momentum gap. G3 с €1M revenue но без portrait-completion = matchmaker failure. Secondary signals — это Ashby requisite-variety check: controller variety (pipeline quality indicators) must grow proportionally с controlled system size.

**Pattern 2 — Reject conditions важнее trigger conditions для системной устойчивости.**
Большинство project managers фокусируются на «когда активировать gate». Системное мышление требует аналогичного фокуса на «когда НЕ активировать». Каждый преждевременно активированный gate создаёт structural debt (нанятые люди без revenue support, построенный platform без network liquidity, opened Alliance без governance). Reject conditions — это балансирующие петли против reinforcing-петли «давай масштабируем».

**Pattern 3 — BOSC-A-T-X помогает называть качественный тип изменения, а не только количественный.**
G1→G2 (Agency shift) и G2→G3 (Composition + Scale) — качественно разные transitions несмотря на похожую revenue increment ratio (4×). Agency shift требует coordination mechanisms (OME protocols, briefing templates, clear handoff points). Composition shift требует platform infrastructure. Путать эти types = строить не то. Framework BOSC-A-T-X заставляет называть тип transition explicitly до начала spend.

---

*Provenance (key sources consulted):*
- `decisions/JETIX-SYSTEM-OVERVIEW.md` §5 trajectory table (master layer structure)
- `decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md` §11.1 master evolution + §11.2 per-gate narratives + §11.3 cross-gate scalability (Meadows/Ashby/Beer)
- `decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md` §2.1 portfolio table + §3.1–§3.5 directions + §3.4 matchmaker gate evolution
- `decisions/JETIX-PLAN.md` §1 overview + §3 Phase 1 + §4 transition + §3.1.1 CC-1 revenue-mix
- `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md` D26 team trajectory
- `decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md` §0 TL;DR + §1 structural insights + status_note
- `swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md` §3 L6+L5 acked inputs
