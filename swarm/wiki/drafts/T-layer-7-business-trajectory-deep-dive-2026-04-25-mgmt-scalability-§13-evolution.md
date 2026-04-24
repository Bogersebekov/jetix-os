---
id: T-layer-7-business-trajectory-deep-dive-2026-04-25-§13-evolution
title: "§13 Evolution per Gate Master Table"
type: cell-draft
cell: C-05
expert: mgmt-expert
mode: scalability
cycle_id: cyc-layer-7-business-trajectory-deep-dive-2026-04-25
created: 2026-04-25
word_floor: 1000-1500
sources:
  - {path: "decisions/JETIX-SYSTEM-OVERVIEW.md", range: "§5 trajectory table 5 gates × 14 layers"}
  - {path: "decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md", range: "§13.2 master evolution table 9 directions × 5 gates + §13.3 per-gate narratives"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§11.1 master evolution table + §11.2 per-gate narrative"}
  - {path: "decisions/JETIX-PLAN.md", range: "§1 revenue-gated unlocks + §3-§6 Phase 1-3"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D26 team 50-100 + D27 fork-and-merge + D25 company-as-code"}
  - {path: "swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md", range: "§1-§4 full intake"}
provenance_inline: true
confidence: high
confidence_method: structured-rubric | cross-source-reconciliation
escalations: []
dissents: []
---

# §13 Evolution per Gate — Master Table (L7 Financial Expansion)

## §13.0 Framing — чем владеет L7 §13

**Что этот раздел делает.** L7 §13 — это **финансово-операционное измерение** эволюции Jetix по 5 gates. Он отвечает на вопрос: как конкретно выглядят revenue, team size, direction priority, cash burn, cash reserve, KPIs и активные sub-systems на каждом из пяти ценовых/масштабных порогов. Это финансовая проекция на скелете системной архитектуры.

**Что этот раздел НЕ делает:**
- Не описывает per-gate trigger conditions (triggering mechanics — зона §4 этого документа)
- Не углубляется в per-direction unit-econ (это §3)
- Не детализирует M&A стратегию (Phase-2+ deferred per Ruslan 25.04 directive; brief mention only при G2-G3 narrative)
- Не пересматривает 28 Locks

**Иерархия источников:**
- `JETIX-SYSTEM-OVERVIEW.md §5` [src:decisions/JETIX-SYSTEM-OVERVIEW.md#§5] — базовый скелет 5 gates × 14 layers — **verbatim структура**
- `LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md §13` [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§13] — 9 directions × 5 gates — per-direction portfolio evolution
- `LAYER-6-COMMUNITY-DEEP-DIVE.md §11` [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11] — L6 community dimensions × 5 gates
- `JETIX-PLAN.md §1` [src:decisions/JETIX-PLAN.md#§1] — revenue-gated unlocks at-a-glance

L7 §13 **расширяет** эти три источника, добавляя финансовое измерение (cash burn / cash reserve / KPIs) как cross-section, которого в L5/L6 нет.

---

## §13.1 Master Table — 5 Gates × 7 Financial Dimensions

> **Pricing disclaimer:** все €/$ цифры по cash burn и revenue, не помеченные как «locked», являются оценочными ориентирами для планирования. Точная unit-econ арифметика — зона §3 этого документа. KPIs — ориентиры; L7 §7 (если есть) является авторитетным источником для dashboard metrics.

| Dimension | G1 — €50K (Q2 2026) | G2 — €200K | G3 — €1M | G4 — $100M | G5 — $100B → $1T |
|---|---|---|---|---|---|
| **Revenue (cumulative/run-rate)** | €50K cumulative (€65K target ~30% buffer per CC-1); revenue-mix: ~€30K productized contracts + ~€35K hourly (233h × €150/hr) | €200K cumulative validation gate; productized retainers dominant (D18); hourly consulting declining share | €1M run-rate; 5+ revenue streams active (consulting + producer + USB-C + Secure Network subscription + matchmaker fees) | $100M revenue or market cap; consulting <10% share; licensing + SaaS + Alliance dues + token economy dominant | $100B → $1T civilizational run-rate; methodology licensing + token public layer (conditional) + Alliance standard-layer fees primary |
| **Team size** | Solo Ruslan + Cloud Cowork; 0 hires; contractors on-demand only (D2 solo-now/team-ready-scaffolding) | +2-3 first hires: Sales (English-speaking market close) + Ops/PM; D26 trajectory begins [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26] | 5-10 specialists; sub-brigadiers emerging; first roy-leaders inside Jetix; D19 holding structure begins crystallizing | 20-50 people; first external roys ($10M-$100M per D21); D26 holding structure crystallized; Alliance formally exceeds core team numerically | 50-100 steady-state per D26; multi-roy ecosystem; Ruslan lifts to meta-coordinator only [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26] |
| **Direction priority** | AI Consulting (P1A core) + Продюсерский центр (P1A co-primary); all other directions deferred or informal | + USB-C Path B/C first productized client; Secure Network architecture design; Matchmaker protocol documented | + Secure Network platform launch + Matchmaker MVP + Educational methodology repo V1 + USB-C all 3 Paths (5 active directions simultaneously) | + YouTube-analyzer SaaS launch + Token Phase-2 internal + USB-C 50-200 deployments + first replicated roy ($10M+); consulting = sales-motion entry point only | USB-C standard-layer + Alliance methodology licensing + multi-roy federation + Token public layer (if Ruslan acks D23 Option B); Consulting sunset |
| **Cash burn** | €200-400/mo compute (Claude Max + tools); €1-2K one-shot legal (GmbH prep); total Phase-1 ~€0 heavy spend per D15; Ruslan draw = personal expenses only | €120-180K/yr payroll (2-3 hires); €2-3.5K IP lawyer (EU patent prep); €5-10K GmbH legal/Alliance legal; €3-5K/mo office or Cloud Cowork upgrades; total ~€150-200K/yr operational | €600K-€1M/yr team payroll (5-10 specialists); €200-500K platform engineering (Secure Network + Matchmaker + USB-C productization); €30-80K ISO 27001 / BSI C5 certification; Alliance Foundation incorporation €30-50K | $5-10M/yr team (20-50); data-center partnership capex (Hetzner/OVH EU-sovereign ~$500K-$1M/yr); first roy seed capital ($1-3M per roy); YouTube-analyzer SaaS engineering sprint; legal multi-jurisdictional | Enterprise-scale; own data-center ($10M+ capex Phase 3+); regulatory engagement; Token public layer legal €100-500K; multi-roy ecosystem operating costs |
| **Cash reserve target** | ≥€2K runway minimum (Phase-1 low-spend; personal expenses covered); target: 3-month runway from earned revenue | 6-month runway in bank (≥€75-100K liquid) before triggering G2 heavy-spend unlocks; D15 discipline: patent + hires only AFTER €200K gate confirmed | 9-month runway (≥€750K liquid at €1M/yr burn rate); allows buffer for platform build delays + parallel direction activation | 12-month runway ($5-12M liquid given $5-10M/yr burn); Kelly portfolio cash allocation for cross-roy capital decisions | Civilizational cash reserve; sovereign wealth-fund discipline; runway measured in years not months |
| **KPIs** | MRR €5K by Q2 2026; 4-pack offer validation (≥2 of 4 components used by paying clients); 5+ active clients (or 3 contracted); founder-dependency = 100% (expected); 0 churn (too early) | First 3 productized contracts retained (not one-off); GM ≥70% per contract (per CC-1 Path B economics); NPS ≥40 from first 5 clients; team ramp <60 days to productive; priority-reversal-rate <20%/month | Subscription revenue ≥15% of total Jetix revenue; ≥10 successful matchmaker matches with documented outcomes; methodology repo V1 published; founder-dependency <50% (toward <30% target D19); Alliance ≥50 formal members | Founder-dependency <30% (D19 explicit target); ≥1 external roy achieving $10M+ revenue using Jetix methodology; ≥3 Alliance methodology-parliament merge-backs; YouTube-analyzer SaaS churn <5%/month | Global Alliance 1000-5000+ formal members; multi-roy ecosystem dozens of forks; identity-grammar drift <30% (D1/D13/D22 preservation); token public layer KPIs (if launched): accredited-holder count + JCU redemption rate |
| **Sub-systems active** | AI Consulting (active) + Продюсерский центр (active) + Matchmaker (manual/informal) + Smart AI narrative (internal) + Company-as-Code L0 (D25) | + Matchmaker (protocol documented) + Secure Network (architecture design) + USB-C (first productized engagement) + Alliance Foundation (legal process starts) + 2-3 human team-members | + Secure Network platform (live) + Matchmaker MVP (platform) + USB-C all 3 Paths (active) + Educational Products V1 (live) + Alliance Foundation (incorporated, Option C) + Token economy (design phase per D23 $100K trigger) | + YouTube-analyzer SaaS (live) + Token Phase-2 internal (active) + Holding structure (crystallized per D19) + First external roy + Alliance methodology-parliament | + Token public layer (conditional on D23 B/C ack) + Multi-roy federation + Civilizational infrastructure + Own data-center + Regulatory engagement sub-system |

[src:decisions/JETIX-SYSTEM-OVERVIEW.md#§5 verbatim gate structure]
[src:decisions/JETIX-PLAN.md#§1 revenue-gated unlocks]
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§13.2 master evolution table]
[src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.1 master evolution table]
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]

---

## §13.2 G1 Narrative — €50K (Q2 2026)

**F: F5** (KPI-tracked с explicit gate; операционный контракт D15 + CC-1 revenue decomposition; единственная committed absolute date в плане)
**ClaimScope:** holds Phase-A solo-founder Q1-Q2 2026; NOT valid Phase-B managed team; unknown if macro-disruption occurs Q1 2026
**R:** refuted if €50K gate not cleared by Q2 2026 end; accepted if MRR €5K reached + 4-pack validated + ≥3 paying clients documented

G1 — это gate выживания и валидации базовой гипотезы: **может ли Ruslan генерировать выручку через AI-consulting + Продюсерский центр как solo-operator с агентной поддержкой**.

**Capital allocation decision rule:** на G1 каждый расход >€500 требует explicit ROI-to-€50K-gate justification по D15 [src:decisions/JETIX-PLAN.md#§1]. Никаких heavy-spend. Компания живёт на bootstrap cashflow. Единственные легитимные категории spend: Claude Max subscription (~€200/mo), базовые инструменты, и откладывание на GmbH setup (который тригерится при $20-30K self-earned, не €50K). Foundation-building расходы (лендинги, шаблоны, контент) — нулевые или минимальные, делаются руками Ruslan + агентами.

**Team trajectory:** Solo + Cloud Cowork. Contractors on-demand только если прямой billable проект оправдывает. Никаких hires до G1 gate. D2 "Solo-now / Team-ready-scaffolding" — архитектура scaffolding строится D25 Company-as-Code способом (декларативные конфиги, wiki, agents file), чтобы first hire onboarding был механическим, а не героическим [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25].

**Direction portfolio:** Consulting + Producer = 100% revenue. Matchmaker = informal lever (0% direct revenue; creates goodwill + specialist network). Secure Network = Telegram чат «попутно» (5-20 лично знакомых; zero mechanics). Все остальные directions — deferred. D11 диктует этот порядок [src:decisions/JETIX-PLAN.md#§3.1].

**Revenue architecture (CC-1):** ~€30K из 4 productized contract-quarters (2 contracts × 2Q × €7.5K/contract-Q) + ~€35K из 233 hourly consulting hours (×€150/hr) = ~€65K target против €50K gate (~30% buffer). Без hourly capacity ≥20h/week — gate не проходится даже при выполнении contract targets [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.1.1].

**KPIs monitored:** MRR €5K (Q2 target); 4-pack offer validation; ≥3-5 active client relationships; priority-reversal-rate <20% (AP-MGMT-5 threshold).

---

## §13.3 G2 Narrative — €200K (Phase 2 Entry)

**F: F4** (operational convention; rests on D15 + JETIX-PLAN §4 + L6 ack + L5 ack; no formal proof — operational projection)
**ClaimScope:** holds Phase-B entry post-€50K; NOT valid if macro-recession causes sales-cycle collapse; unknown for first-hire hiring speed in DE labour market
**R:** refuted if €200K gate takes >18 months from €50K (suggests operating model не scales); accepted if first hires ramp productive <60 days + GM ≥70% sustained

G2 — это gate, на котором **solo-operator превращается в минимальную команду**. Выручка €200K в JETIX-PLAN называется "Validation Gate" — это проверка что операционная модель выживает за пределами одного основателя.

**Capital allocation decision rule:** D15 unlock при €200K opens heavy-spend categories: patents EU (€2-3.5K IP lawyer), first 1-2 hires, Secure Network build start, Alliance Foundation legal incorporation. Каждая из этих линий требует runway-impact projection перед commitment. Правило: никакая тяжёлая статья не активируется пока не подтверждена liquidity с 6-month runway buffer. Порядок приоритетов spend: (1) payroll first hires; (2) GmbH legal finalization; (3) Foundation eV incorporation (если Alliance Option C acked); (4) patent EU prep; (5) Secure Network architecture build (не launch — design).

**Team trajectory:** G1 solo → G2 +2-3 hires. Профили первых hires: (a) Sales/BD — English-speaking market closure, prospecting, outreach execution (разгружает Ruslan от pipeline); (b) Operations/PM — OME agent scaffolding → human counterpart, deliverable coordination. D26 trajectory начинается здесь; при этом D26 target 50-100 остаётся горизонтом, не Phase-2 задачей [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]. Hiring discipline: D22 5-criteria filter применяется к каждому hire-у — нельзя нанимать «просто ресурс»; нужен адекватный, стабильный, с азартом.

**Direction portfolio:** Consulting remains primary (declining % от total revenue как другие directions включаются). USB-C Path B/C productization starts (first client engagement; Path-B default per L5 ack). Secure Network architecture design begins (не launch — paper+design pre-work). Matchmaker protocol documented + digital portrait template designed. Educational Products skeleton drafted. **M&A direction Phase-2+ optionality decision deferred per Ruslan 25.04 directive:** если к G2 появился co-founder + €200-500K capital available + Mittelstand 2026-2028 window assessed open → spawn dedicated M&A cycle (separate brigadier dispatch); иначе M&A остаётся deferred в backlog [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3-M&A].

**Alliance Foundation:** Option C (Foundation eV + Jetix-Corp GmbH) рекомендован L6. Идеально — governance decision принимается в конце G1 (параллельно G1→G2 revenue build), потому что EU/DE legal filing = 4-12 недели. Если ждать G2 arrival — Alliance не может onboard первых формальных членов 1-3 месяца после gate. «Wrong option fast > right option 2 years late» [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§8].

---

## §13.4 G3 Narrative — €1M (Phase 2 Core)

**F: F4** (operational convention; rests on D15 + D26 + L5 §13.3 + L6 §11.2 G3; cross-validated across 3 source documents)
**ClaimScope:** holds Phase-2 core (€200K-€1M) с team 5-10; NOT valid если direction activation sequence отклоняется существенно от L5 §13.2 column G2→G3; unknown in Phase-B managed-team context with >5 specialist hires
**R:** refuted if subscription revenue <15% total Jetix revenue by €1M gate (suggests Secure Network + USB-C productization не working); accepted if ≥10 matchmaker matches with documented outcomes + methodology repo V1 published

G3 — самый **структурно плотный** gate в эволюции Jetix. Четыре direction одновременно переходят из "preparing" в "active" [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§13.3-G2→G3]. Это требует синхронизированного capital allocation.

**Capital allocation decision rule:** team payroll — доминирующая статья (~€600K-€1M/yr). Каждое новое direction при G3 проходит hurdle-rate gate: **GM ≥70% в течение 2 кварталов после activation**. Ниже — de-morph back per `/project-de-morph` mechanic. Этот hurdle применяется индивидуально к каждому direction: Secure Network subscription, USB-C Path B client, Matchmaker platform fee. Alliance Foundation operational dues (~€10-30K/yr) — отдельная статья; не subject to GM hurdle (это governance infrastructure, не revenue direction). ISO 27001 / BSI C5 certification (€30-80K + 6-9 months) активируется в G3 как prerequisite для full Mittelstand enterprise pipeline [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.1-OQ-3.1-B].

**Team trajectory:** 2-3 → 5-10 specialists. Структура: Consulting BU (3-4 специалиста под Sales + Delivery); Producer BU (1-2 продюсера); USB-C/Platform engineering (1-2 инженера); Operations (1 PM). Первые roy-leaders могут появиться внутри Jetix на этом gate — это люди достаточно глубоко погружённые в методологию, чтобы возглавить отдельный roy-cluster [src:decisions/JETIX-PLAN.md#§5]. D19 holding structure начинает кристаллизоваться: GmbH + Foundation eV + первые контракты с механикой revenue-share.

**Direction portfolio:** 5 направлений активны одновременно (Consulting + Producer + USB-C + Matchmaker MVP + Secure Network launch + Educational V1). Добавляется Alliance Foundation как operational unit. Token economy — design-phase: если $100K self-earned trigger достигнут внутри G2→G3 span — первая legal consultation по D23 MiCA structure [src:decisions/JETIX-PLAN.md#§5 D23 trigger]. Revenue диверсифицирована по 5+ streams; consulting снижается в доле revenue total но остаётся strongest per-client GM direction.

**Feedback structure shift:** от single reinforcing loop (Ruslan консультирует → зарабатывает → реинвестирует) к **multi-loop architecture**: R1 (consulting revenue → team → capacity → revenue) + R2 (Secure Network members → portraits → matchmaker → more value → more members) + balancing B1 (portrait quality degrades при слишком быстром onboarding). Leverage point B1: portrait-completion как structural hard gate к premium Secure Network features (Meadows L4) [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.2-G3].

---

## §13.5 G4 Narrative — $100M (Phase 3 Core)

**F: F3** (pattern observed across comparable consulting-to-platform trajectories; no Jetix-specific evidence; horizon projection, not operational convention)
**ClaimScope:** holds Phase-3 scaling context ($1M-$100M); NOT valid if USB-C productization fails to get market traction (fundamental assumption); unknown in regulatory-disruption scenarios (EU AI Act expansion, GDPR interpretation shift)
**R:** refuted if founder-dependency remains >30% at $100M gate (D19 non-negotiable target); accepted if ≥1 external roy achieves $10M+ revenue AND Alliance methodology-parliament processes ≥3 merge-backs

G4 — gate, на котором **Jetix перестаёт быть consulting-centric** и становится **infrastructure-layer play**. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§13.3-G3→G4]

**Capital allocation decision rule:** Kelly portfolio approach для cross-roy capital allocation — каждый active roy оценивается против hurdle rate. Любой roy ниже 30% Constellation-style hurdle rate, sustained 4 quarters → retirement. Data-center decision: Phase-2 EU-sovereign partnership (Hetzner / OVH / Deutsche Telekom cloud) vs Phase-3 own data-center. При G4 **own data-center capex** начинает быть оправданным при >$50M/yr infrastructure spend threshold. До этого — партнёрство с EU-sovereign provider достаточно [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.3-OQ-3.3-Q4]. First replicated roy требует seed capital: ориентир $1-3M per roy при первом external roy (D21). Этот seed — не grant, не equity dilution — это operating advance из Jetix holding pool, возвращаемый из roy revenue-share.

**Team trajectory:** 5-10 → 20-50. Holding structure по D19 кристаллизована: separate BU-entities под Jetix-Corp umbrella для Consulting, Platform (USB-C + Matchmaker), Alliance, Producer. Ruslan lifts от operational delivery к meta-coordinator role: Alliance methodology-parliament oversight + roy-replication program management + investor/regulatory relations. Founder-dependency target <30% (D19) — это hard constraint на G4 для перехода к G5. YouTube-analyzer SaaS требует engineering sprint: отдельная sub-team 3-5 engineers [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.6].

**Direction portfolio:** YouTube-analyzer SaaS launch (seat/channel/query pricing); Token Phase-2 internal utility active (specialist compensation + складчина; NOT public); USB-C Integration Services 50-200 client deployments (potential distilled Mittelstand LLM proof-of-concept per STRATEGIC-INSIGHT §8 rec 7); D24 open-source research direction activates; first external roys operational. Consulting = minority share, primary function = sales-motion entry point к ecosystem (не standalone revenue line).

**Dominant BOSC trigger: T (Time).** Planning horizon shifts от quarter-cycle к multi-year. Beer VSM Level-4 (intelligence/futures) и Level-5 (identity/policy) должны быть **явно инстанциированы как distinct sub-systems** — иначе variety coordination needs превышает single-brigadier-swarm capacity [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.2-G4]. MHT event: Context Reframe.

---

## §13.6 G5 Narrative — $100B → $1T

**F: F2** (pattern inference from USB-C/Windows/Linux Foundation analogs; no direct evidence from Jetix trajectory; civilizational-horizon projection)
**ClaimScope:** holds IF USB-C standard-layer positioning succeeded at G3-G4; NOT valid if competitor achieves standards-body adoption first; entirely unknown in AI-regulatory-disruption scenarios
**R:** refuted if Alliance formal membership <1000 at G5 gate (insufficient regulatory weight для standards-body conversations); accepted if multi-roy ecosystem includes dozens of active forks AND Jetix methodology referenced by EU AI Act standards process

G5 — это **цивилизационная инфраструктурная позиция**, не просто масштаб revenue [src:decisions/JETIX-VISION.md#§14]. Аналог не McKinsey, не SAP — аналог Windows firmware как de-facto standard или Linux Foundation как ecosystem governance infrastructure.

**Capital allocation decision rule:** D11 Investment-fund philosophy fully operationalized [src:decisions/JETIX-PLAN.md#§1-D11]. Identity-grammar preservation (D1 / D13 / D22 / D27 cluster) > capital-allocation efficiency. Это означает: даже если конкретный roy или direction генерирует меньше GM чем alternative deployment, если он несёт identity-critical функцию (например — Alliance Foundation как epistemic authority в EU AI Act discussions) — он финансируется.

**Capital allocation:** civilizational infrastructure — own data-center + power infrastructure (Phase-3+ per JETIX-PLAN §6); regulatory engagement sub-system (EU AI Act, BaFin, ISO/IEC standards); Token public layer legal infrastructure (€100-500K per regulatory structure per D23 — IF Ruslan acks D23 Option B/C; this is NOT automatic; explicit ack required) [src:decisions/JETIX-VISION.md#D23]. Sovereign cash reserve measured in years.

**Team trajectory:** 20-50 → 50-100 steady-state per D26 [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]. Multi-roy ecosystem. Meta-coordinator role (Ruslan или successor) = VSM Level-5 identity/policy function. Sub-brigadiers per BU. Alliance numerically dominates: 1000-5000+ formal members exceed core team by 10-50×.

**Direction portfolio:** Consulting sunset (replaced by USB-C standard-layer + methodology licensing). USB-C standard-layer + Alliance methodology licensing = dominant revenue model (Wintel precedent: value migrated from hardware BIOS к Intel patents + Microsoft licensing [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§1]). Token public layer ТОЛЬКО если D23 Option B/C явно acked Ruslan — conditional sub-system. Fork-and-merge (D27) mature: dozens of active Jetix-methodology forks; best mutations return upstream; Jetix = canonical upstream с quality bar.

**Civilizational KPIs:** Alliance 1000-5000+ formal members с regulatory weight; multi-roy ecosystem dozens of forks; identity-grammar drift <30% (D1/D13/D22 preservation measured via methodology audit); Token public layer: accredited-holder count + JCU redemption rate (if launched). Global USB-C narrative в international press + EU standards-body conversations.

---

## §13.7 Cross-Section Reconciliation Note

**Как §13 соотносится с другими разделами этого документа:**

- **§4 (5-gate triggers):** §13 описывает финансовое состояние на каждом gate; §4 описывает конкретные observables и conditions, которые сигнализируют переход к следующему gate. §13 и §4 взаимодополняют, не дублируют.
- **§10 (Compensation + Team trajectory):** team size rows в §13.1 master table являются skeleton; §10 детализирует compensation structure, equity mechanics, Roy-replication compensation модель.
- **§11 (Risk Register):** cash reserve targets и burn rates из §13.1 напрямую фидят в risk register. **Mittelstand 2026-2028 window closing** (per M&A direction research) — риск идентифицированный в §11, не в §13. M&A direction при G2-G3 упомянута только как optionality: если к G2 появился co-founder + capital + window assessed open → spawn dedicated M&A cycle; иначе deferred [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§3-M&A].
- **§3 (Unit-econ per direction):** pricing и GM% в §13 — placeholders; §3 owns final arithmetic.
- **L5 §13 + L6 §11:** L7 §13 добавляет financial dimensions (cash burn / cash reserve / KPIs) которых в L5/L6 нет; не пересматривает direction status или community cardinality (те остаются per L5 §13.2 и L6 §11.1 verbatim).

**F-G-R на master claim этого раздела:**

Claim: «Переход €50K → €200K → €1M → $100M → $1T описывается единой sequence capital allocation decisions + team growth + direction activation, где каждый gate является Phase Promotion в системном смысле, а не просто revenue milestone».

- **F:** F4 (operational convention; cross-validated per SYSTEM-OVERVIEW §5 + PLAN §1-6 + L5 §13 + L6 §11; consistent framework applied across sources)
- **ClaimScope:** holds для Jetix при current trajectory assumptions (consulting + producer revenue-primary G1, USB-C productization G2, platform launch G3); NOT valid если fundamental pivot происходит (e.g., pivot away from Mittelstand, token-first go-to-market); unknown в regulatory-disruption scenarios (EU AI Act hard prohibition on private AI deployments)
- **R:** refuted if G1 gate fails entirely (€50K not reached Q2 2026) — все downstream projections становятся invalid; accepted if G1 cleared + G2 team ramp proceeds по D26 trajectory + GM ≥70% maintained через первые 3 productized contracts

[src:decisions/JETIX-SYSTEM-OVERVIEW.md#§5]
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§13.4]
[src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§11.3]

---

## §X Cell C-05 Self-Improvement Notes

1. **Evolution master table = financial-dimension cross-section.** L5 §13 владеет direction-status cross-section; L6 §11 владеет community-cardinality cross-section; L7 §13 добавляет специфически финансовое измерение (burn / reserve / KPIs) как третью ортогональную ось. Эта роль «третьей оси» должна быть explicit в §13.0 framing с первых строк — иначе интегратор не поймёт зачем §13 существует рядом с L5 §13 и L6 §11.

2. **Per-gate narrative = 200w decision-rule paragraph.** Оптимальный формат для per-gate narrative: (1) capital allocation decision rule (что и в каком порядке тратится), (2) team trajectory (конкретные роли/числа), (3) direction portfolio (active/preparing/deferred + M&A optionality mention где уместно). Это «помещается» между master table и §4 trigger detail без дублирования обоих.

3. **M&A optionality mention pattern.** Per Ruslan 25.04 directive — brief mention only at G2-G3, не deep-dive. Правильный паттерн: одно-два предложения в G2 narrative с conditional trigger («если co-founder + capital + window → spawn dedicated M&A cycle»), nil mention в остальных gates кроме §13.7 reconciliation note. Этот паттерн реюзаем для других «deferred optionality» items (e.g., Token public layer при G5).
