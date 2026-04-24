---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: §3.5
direction: Secure Network
type: layer-deep-dive-section
mode: integrator
author: systems-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md
  - decisions/JETIX-VISION.md
  - decisions/JETIX-PLAN.md
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
  - decisions/JETIX-SYSTEM-OVERVIEW.md
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md
  - reports/review_2026-04-24.md
  - swarm/wiki/operations/quick-money/icp.md
  - swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md
  - swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/decomposition.md
word_count_estimate: ~2100
confidence: high
confidence_method: synthesis-from-locked-decisions-plus-L6-deep-dive-inheritance
escalations: []
dissents:
  - id: §3.5-D1
    source: systems-expert × integrator (this draft)
    claim: "Telegram-primary lock creates structural dependency on third-party platform policy; portrait data separation (Jetix KB vs Telegram transport) mitigates data-loss risk but does not mitigate API ToS risk or API deprecation risk"
    F: F4
    ClaimScope: "Holds Phase-1 through Phase-2 (≤200 members); NOT resolved at Phase-3+ own-platform transition (that remains a future decision)"
    R: "Refuted if Telegram provides contractual API-stability commitment to Jetix; accepted if Phase-2 architectural gate locks migration-readiness escape hatch (member export format + migration drill) before Secure Network launch"
  - id: §3.5-D2
    source: systems-expert × integrator (this draft)
    claim: "Складчина tool-sharing mechanic generates ToS exposure with tool vendors who prohibit shared credentials; cost-reduction value proposition depends on this mechanic being operationally viable"
    F: F3
    ClaimScope: "Holds for subscription-model tools prohibiting shared access (e.g. typical SaaS ToS); NOT necessarily fatal — team-account or enterprise pricing may offer compliant path"
    R: "Refuted if compliant team-seat or enterprise pricing eliminates cost-reduction advantage; accepted if ≥3 target tools (Perplexity, Claude Pro, research DBs) have compliant multi-seat pricing at Secure Network member-pool scale"
---

# §3.5 Secure Network — Direction Deep Dive

## 1. Mission

Secure Network — это **quality-gated профессиональная сеть + слой совместного пользования дорогостоящими AI-инструментами (складчина)**, работающая поверх Telegram-primary инфраструктуры и структурированная в тематические субсети по архетипам. Антитезис LinkedIn по дизайну: не для «рабов ищущих других рабов» [src:decisions/JETIX-VISION.md §5 D5], а среда для глубокой кооперации adequately-filtered профессионалов, где качество сигнала на порядок выше любого открытого профессионального пространства. Paid-subscription продукт, активирующийся в Phase 2+ после G2 €200K validation gate, и масштабирующийся до multi-roy federation на Phase 5 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §11.1].

## 2. Phase Activation

- **Активен в: Phase 2+** — дизайн-фаза начинается G1→G2; полноценный запуск G2→G3 [src:decisions/JETIX-PLAN.md §4.1 + §5]
- **Activation trigger: €200K validation gate (G2)** — аппаратный unlock по D15; до €200K heavy-spend lock не позволяет инвестировать в platform infrastructure. Phase-1 чат «попутно» (5-20 участников, invite-only, Telegram) существует как precursor, но не является Secure Network в продуктовом смысле [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §9.2]
- **Sunset trigger: NONE** — Secure Network не заходит в закат; масштабируется от Telegram-чата (Phase 1) → subscription platform (Phase 2+) → multi-roy federation (Phase 5); каждый последующий gate добавляет слой, не заменяет предыдущий
- **Phase-1 precursor (активен сейчас):** 5-20 участников, invite-only Telegram-чат, модерируется Ruslan, нет формальных механик, нет subscription — это D16 "простой чат попутно" [src:decisions/JETIX-VISION.md §5 D16], не Secure Network Phase-2+ продукт

## 3. Target ICP Mapping

### Post-G2 invite-only expanded Tier-1: «семена» из graduated consulting clients

Ключевой структурный инсайт: первые Secure Network члены не берутся из холодного outreach — они являются **выпускниками §3.1 консалтинговых engagements**, прошедшими D22 5-критерийный фильтр в процессе консалтинговых отношений с Ruslan [src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md §2]. Консалтинг = pipeline, Secure Network = retention layer.

**Payment ability filter (L6 ack'd per intake §6.1):** ≥$5K/месяц recurring OR ≥$10K one-shot. Три income категории: миллионеры ($1M+/год) / high-earners ($100-150K+/год) / предприниматели-блогеры с revenue-variable. Subscription-able — Phase-2 pricing tier $100-500/мес (placeholder; L7 owns final) попадает в платёжную способность всех трёх категорий [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §2.1].

**Тематические субсети (MANDATORY — 5 наименований per JETIX-VISION D5):**
- **Предприниматели** — hungry founders, Mittelstand owners, Operator/Founder-CEOs: ищут peer network с skin-in-game, без noise
- **Инвесторы** — pattern seekers: $1T trajectory inside view + matchmaking к specialised deal flow (Phase-2+ primary per L6 §3)
- **Инженеры** — system builders: peer-to-peer architecture conversations без marketing noise; USB-C protocol development context
- **Философы** — meaning seekers: operational wisdom infrastructure + adequate philosophical peer group; Phase-2+ primary
- **Политики** — influence operators: strategic communication leverage + institutional weight platform (Phase-3+)

[src:decisions/JETIX-VISION.md §7.1 archetypes 1/3/4/5/8 + audio_510 thematic channels reference]

Аудио-якорь: в audio_510 Ruslan explicit: *«политики общаются между собой, бизнесмены между собой, философы между собой»* — тематические субканалы как структурное требование, не опция [src:reports/review_2026-04-24.md строки аудио_510].

**Phase-1 archetypes (primary buyers per L6 ack):** Startupper + Блогер + Operator/Founder-CEO + Teacher — все четыре имеют статус Phase-1 buyer YES; все четыре являются target seeds для Secure Network Phase-2+ waitlist [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3 Phase-1 активный outreach].

**Anti-ICP (MANDATORY preserve):** «рабы ищущие других рабов» [src:decisions/JETIX-VISION.md §6] — job-seekers, recruiters, MLM-участники, crypto-pump-аудитория, AI-hype passive consumers. Не берём тех, кто ищет сотрудников для найма, не партнёров для кооперации. Self-selection через framing «самая большая авантюра века» [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §7.5 Landing A] отпугивает passives on entry.

**Digital portrait requirement:** каждый участник Secure Network имеет machine-readable цифровой портрет в Jetix KB (YAML; не в Telegram — Telegram = transport layer, KB = data layer). Без заполненного portrait → Observer role only; полный доступ к subchannels + matchmaker + складчина требует ≥80% portrait completeness [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §10.2]. Ruslan в audio_524: *«люди без цифровых портретов фактически не существуют»* в этой системе [src:reports/review_2026-04-24.md audio_524].

## 4. Value Proposition

### Проблема в терминах клиента

«LinkedIn — это шум и рекрутёры. Slack-сообщества хаотичны. Telegram-группы спамятся. Discord-серверы неплохи, но tool-pooling там не нативен. Mastermind-группы за $10K+ в год слишком дорогие и transactional. Я хочу сеть людей, которые реально строят, реально думают глубоко, которым можно доверять как сигналу — и где доступ к дорогостоящим инструментам не означает $500/мес на каждый из пяти инструментов.»

### Outcome promised (измеримый)

- **Signal-to-noise 10x** по сравнению с LinkedIn/Slack: D22 5-критерийный фильтр (startupper mindset + предпринимательский азарт + stable + adequate + upward-direction) работает как membrane до входа, не пост-фактум модерация [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §4]
- **Cost reduction 5-10x на AI-инструменты**: складчина Perplexity Pro / Claude Pro / дорогостоящих research databases — pooled credentials или team-account схема, split proportionally по tier. Для члена $200-400/мес tier вместо $800-1500/мес за отдельные подписки
- **Тематическая глубина в субсетях**: инженеры говорят с инженерами, инвесторы с инвесторами; кросс-архетипный noise отсутствует в субканалах, он изолирован в General Lounge
- **Coordination via §3.4 Matchmaker**: сложные задачи находят специалистов внутри сети; matchmaker Phase-2+ AI-smoothed, Phase-3+ platform-level [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6]
- **Reputation compounding**: contribution-graph в цифровом портрете фиксирует каждый successful match, каждый merge-back, каждую peer-rated contribution — репутационный капитал начисляется провиденциально [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D25 Company-as-Code]

### Чем Jetix Secure Network отличается от конкурентов

| Конкурент | Почему не решает |
|---|---|
| **LinkedIn Groups** | Нет quality-gate; spam нативен; recruiters = dominant users |
| **Slack communities (Indie Hackers, DevCorp)** | Модерация слабая; tool-pooling не предусмотрен; churn высокий |
| **Discord invite-only серверы** | Лучше, но нет нативного складчина-слоя; DACH Mittelstand воспринимает как gaming platform |
| **YC Bookface** | Закрытый, только YC alumni; транзакционный, не compounding |
| **OnDeck / Reforge** | Cohort-based; $3K-$10K/cohort; нет ongoing membership value |
| **Tiger 21 / EO / YPO** | $10K-$30K/год + physical requirement; барьер входа money-gated, не D22-quality-gated |

**Уникальное дифференцирование Jetix:**
1. **Quality-gate через D22** масштабируется лучше money-gate: D22 фильтрует более точно — человек с $500/мес на подписку но failing D22 не попадает; человек с $200/мес на подписку но passing D22 попадает. Качество сети определяет ценность, не тариф
2. **Tool-sharing складчина** уникален — ни один конкурент не предлагает operational tool-sharing infrastructure как нативный layer
3. **Integration с §3.4 Matchmaker + §3.1 Consulting** → compounding relational capital: консалтинг-клиент → Secure Network member → matchmaker-participant → Alliance Foundation member — один arc, не standalone продукты
4. **USB-C framing**: Secure Network — это human-connector layer USB-C позиционирования; как Jetix = standard на уровне technology, так и Secure Network = standard для качественных human connections в AI-эпохе [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §USB-C Reinforcement]
5. **Alliance Foundation membership convergence (Option C)**: Apache 2.0 methodology docs + Secure Network membership soft-bundled перfor Option C downstream [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5]

## 5. Offer Structure

### Invite-only Phase-2+ membership + subscription + складчина

Продукт состоит из трёх неразрывных слоёв: (a) доступ к качественной сети, (b) подписка на тематические субсети, (c) складчина дорогостоящих инструментов. Разделить их означает уничтожить дифференцирование.

**3 tier placeholder (L7 owns final pricing):**

**Observer tier (~$50-100/мес placeholder):**
- Read-only доступ к 1 тематическому субканалу + архивам
- Ограниченное взаимодействие (не пишет в субканале)
- Складчина: нет доступа
- Matchmaker: нет eligibility
- Use case: «хочу понять атмосферу перед full commitment»; entry-point для warm leads

**Member tier (~$200-400/мес placeholder):**
- Full access к 3 субканалам + General Lounge
- Matchmaker eligibility (может быть задачником и исполнителем)
- Складчина: half-share (3-5 инструментов из пула)
- Portrait: обязателен ≥80% completeness
- Use case: основной активный участник, ищущий peer network + tool-efficiency

**Core Member tier (~$500-1000/мес placeholder):**
- All subnetworks (11 тематических) + General Lounge
- Matchmaker priority routing (first to see tasks matching profile)
- Складчина: full-share (весь пул инструментов)
- Co-development rights: может предлагать fork-and-merge methodology contributions (D27)
- Alliance Foundation member perk: Apache 2.0 methodology docs free access; upgraded subnetwork tier bundled с Foundation membership fee [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5 Option C downstream]
- Use case: top-tier participant строящий deep presence в сети + намеренно участвующий в Jetix methodology evolution

**Invite-only mechanic:** phase-2+ waitlist landing page (Landing A «Авантюристы» [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §7.5]) → заявка → D22-screening → invite token → onboarding. Portrait intake завершается до full access. Vouching Phase-2+: один действующий Member ≥3 мес поручается за кандидата.

**Pricing placeholder rationale:** $200-400/мес Member tier попадает в sweet spot: ниже OnDeck/YPO money-barrier, выше threshold где «приходят случайные люди». D22 quality-gate делает price-threshold не главным фильтром — можно держать ниже рынка без деградации качества, если D22 membrane работает. **L7 owns final** — это structural placeholder, не commitment.

## 6. Delivery Mechanism

### Infrastructure: Telegram-primary per LAYER-6 §10

L6 §10 является авторитетным источником для всей инфраструктурной архитектуры Secure Network — этот раздел L5 не переоткрывает §10 LAYER-6, а inherits and builds product layer поверх [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §10.1].

**Telegram-primary rationale (inherited ack):** три фактора per L6 §10.1: (a) audio_524 прямо называет Telegram как основу [src:reports/review_2026-04-24.md audio_524]; (b) Phase-1 (5-20 членов) не оправдывает инвестиций в собственную платформу; (c) Telegram обеспечивает acceptable security model (E2E для secret chats, transport encryption для групп). Phase-3+ transition к собственной платформе — per §10.7 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §10.7].

**Структура каналов Phase-2+ (50-200 членов):**
- Announcements channel (read-only для членов)
- General Lounge (кросс-архетипный; модерируется по тональности D22)
- 5+ тематических субканалов (предприниматели / инвесторы / инженеры / философы / политики — и дополнительно по мере роста к 11 архетипам)
- Private DM matchmaker-bot (structured task requests)
- Onboarding/waitlist channel (Observer роль, ≤2 недели до portrait completion)

**Agents involved:**
- `brigadier` — координация спорных ситуаций + Phase-B обновление methodology
- `manager` — operations coordination
- `personal-assistant` — invite mechanics + scheduling
- `sales-outreach` — invite механика, onboarding flow
- `inbox-processor` — moderation первый AI-pass (flag + route)
- `knowledge-synth` — community digest generation, portrait graph queries

**KM Mat infrastructure:**
- `/project-bootstrap --type=community` (или расширение consulting type) создаёт project-scaffold для каждого субканала
- `edges.jsonl` фиксирует membership + invite provenance (D25 company-as-code: Secure Network membership = commit) [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D25]
- `/ask` + thematic query-driven KB per subnetwork (D28 query-driven KB filtering: каждый субканал = свой anchor для ingest) [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D28]
- Portrait YAML хранится под `community/<member-slug>/portrait.yaml` в Jetix KB — Telegram = transport layer, не data store

**Модель модерации (per L6 §10.3):**
- Phase-2 (≤200): 1-2 trusted Alliance-членов co-модерируют; критерии: ≥3 мес в сообществе, verified D22, активность ≥5h/week
- Phase-3+ (≥200): по одному модератору на каждый архетипный субканал; эскалация к Owner (Ruslan) в 48h SLA

**Складчина mechanic delivery (Phase-2):**
- Простой spreadsheet: инструменты в пуле, участники по tier, usage tracking
- Phase-3+: автоматизация через tool-API integration (где vendor API позволяет)
- Costs split proportionally per tier: Core Member = full share costs, Member = half share
- ToS compliance: team-account или enterprise pricing изучаются прежде credential rotation — shared credentials = риск ban [диссент §3.5-D2]

**Human time requirement:**
- Ruslan: архитектор-орбита (non-delegatable: strategy, taste, accountability, approvals, escalation, relationships [src:decisions/JETIX-VISION.md §3])
- Phase-2: founder ≤10h/неделю на Secure Network (модерация эскалаций, ключевые onboarding decisions, Alliance-вязанные стратегические решения)
- Phase-3+: elected member moderators + agents → Ruslan <2h/неделю operational

## 7. Competitive Positioning

### Competitive map

| Альтернатива | Tier | Модель | Слабость vs Jetix |
|---|---|---|---|
| LinkedIn Groups | Free | Open platform | Spam нативен; no quality-gate; recruiter-dominated |
| Slack communities (paid tier) | $7-15/мес/user | Tool-based | Weak moderation; tool-pooling absent; high churn |
| Discord invite-only servers | Free/Nitro $10/мес | Gaming-adjacent platform | No складчина layer; DACH professional adoption low |
| YC Bookface | YC-membership-only | Alumni network | Narrow (YC alumni only); transactional, not compounding |
| OnDeck / Reforge | $3K-$10K/cohort | Cohort-based | Cohort ends; no ongoing peer network; high price |
| Tiger 21 / EO / YPO | $10K-$30K/год | Mastermind + physical | Extreme cost; physical attendance required; age-biased |
| Generic Telegram/Discord communities | Free | Viral growth | Spam, weak filter, tool-pooling absent |

### Почему Jetix побеждает (честно, без marketing)

**Structural wins:**
1. **Quality-gate scales better than money-gate.** D22 filter catches what price cannot: stable людей с azart, upward-direction, adequacy. Платные сети с слабым фильтром деградируют в «LinkedIn за деньги». D22 — structural advantage, не feature
2. **Складчина unique.** Ни один конкурент не предлагает operational tool-sharing как нативный membership benefit; это addressable market gap прямо сейчас
3. **Vertical integration с §3.1 Consulting → §3.4 Matchmaker → Secure Network → §3.7 Educational.** Конкуренты продают standalone network memberships; Jetix продаёт arc компаундирующего капитала — consulting relationship → network membership → matchmaker participant → methodology contributor

**Structural risks (честно):**
1. **Cold-start liquidity.** Invite-only dramatically slows growth — первые 50 членов Phase-2 = constraint; без liquidity value proposition subnetworks слабее [Senge «Limits to Growth»]
2. **Telegram dependency.** API ToS risk + potential regulatory block в EU [диссент §3.5-D1]; mitigation существует (portrait в Jetix KB, migration drill), но residual risk остаётся
3. **Складчина legal surface.** Tool vendor ToS может prohibit shared credentials; нужна compliant path (team-seat / enterprise pricing) прежде launch [диссент §3.5-D2]
4. **D22 filter bottleneck при масштабе.** При 200+ заявок/год кто интервьюирует? Ruslan personally не bottleneck Phase-1/2, но Phase-3 требует solution [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §8.5]

## 8. Evolution per Gate

**Системный взгляд:** Secure Network является **VSM System-2/3 уровнем Alliance** (Beer, book-as-frame) — coordination layer между участниками. Без работающего System-3 Alliance деградирует в общий чат с хаотичным поиском помощи. С работающим System-3 Alliance = infrastructure для cooperation, самоусиливающаяся с каждым новым участником [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6]. Каждый gate меняет variety (Ashby) System-3, не его VSM-позицию.

### Phase 1 (G0→G1, €0→€50K): НЕ активен как продукт

Secure Network как платный subscription продукт **не запускается** в Phase 1. Phase-1 = D16 «простой чат попутно» — Telegram invite-only, 5-20 лично знакомых, без формальных механик, без subscription, без тематических субканалов. Ценность = trust-building layer + lead-quality filter для consulting pipeline, не revenue line.

**Phase-1 действия (precursor work, zero-cost):**
- Написать D22 qualification protocol как 1-страничный документ (4-2 часа; zero cost; high leverage)
- Черновик digital portrait template (skills / availability / archetype / contributions в markdown)
- Черновик Landing A «Авантюристы» waitlist skeleton [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §7.5]

Цель: к G1 иметь «paper design» Secure Network и first 5-10 potential founding members identified через консалтинговые отношения.

### Phase 2 (G1→G2, €50K→€200K): architecture design begins

G2 €200K validation gate = unlock для Secure Network architecture. Per JETIX-PLAN §4.4 + L6 §11.1: «Secure Network → designed sub-channels per 11 archetypes» [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §11.1].

- **5-20 founding members** (personally known + graduating consulting clients) bootstrap subchannels
- Telegram infrastructure bootstrap: 2-3 тематических субканала seeded (предприниматели + инженеры + один из философы/инвесторы)
- Digital portrait mechanic piloted: первые портреты заполняются manually через bot-flow
- Складчина mechanic: Perplexity + Claude Pro pooled — первый proof-of-concept; ToS compliance check per tool
- Alliance Foundation membership discussion begins (Option C per L6 §5)
- Waitlist landing page live; invite mechanic operational; D22 qualification protocol документирован и applied
- Subscription pricing структура tested (placeholder Member tier)

G2 cardinality target: 50-200 членов к концу Phase-2 активации.

### Phase 3 (G2→G3, €200K→€1M): Secure Network launched

- **Paid subscription active**; membership revenue = measurable revenue line
- Все 5 primary тематических субсетей (предприниматели / инвесторы / инженеры / философы / политики) + начало expansion к полным 11 архетипам
- Складчина mechanic fully operational; cost-reduction KPI measurable
- Alliance Foundation membership bundled (Option C downstream) [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5]
- Matchmaker Phase-2+ AI-smoothed integration: portrait graph → agent-assisted routing
- D22 formal at entry: application form + 15-мин structured interview
- Portrait completion ≥80% required for premium features (structural mechanic, не suggestion)
- 50-200 членов → first network effects visible

Leverage point Phase-3 (Meadows L4 — structure of material flows): portrait-completion gate wired to складчина access — structural rule that prevents matchmaker reinforcing loop being undermined by portrait quality degradation.

### Phase 3+ (G3→G4, $1M→$100M): international + multi-archetype scale

- **200-5000 членов** — multi-language expansion (EN + DE primary; RU + ES/FR optional)
- Все 11 архетипных субсетей активны
- Elected moderator governance per subchannel (11 архетипных модераторов)
- Anti-spam + anti-toxic automation at scale: AI-first-pass flag + moderator review + Owner escalation
- Integration с §3.4 Matchmaker platform MVP: Secure Network member liquidity = precondition для платформенного режима matchmaker [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.3]
- Fork-community opens for Alliance members (D27 timing per L6 §10.5): каждый субканал может fork methodology + preserve best mutations upstream
- Telegram → potential migration to own platform trigger: if >200 active + sharding degradation OR Telegram API ToS change [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §10.7]

### $1T (G4→G5): multi-roy federation

- **10 000+ членов** — mature consortium across geographies и domains
- Fork-community governance (D27 mature): каждый субканал может fork methodology + возвращать mutations canonical upstream; Jetix = canonical upstream поддерживает quality bar
- Multi-roy federation: каждый roy в другой нише = fork + adaptations + потенциальный merge-back [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D27]
- Secure Network не «community product» Phase-1 sense — **sovereign trusted-professional infrastructure**, аналог USB-C для human connections: стандарт, который multiple networks implement, не single product Jetix hosts exclusively
- Regulatory weight: Alliance 1000-5000+ formal members; когда Alliance говорит в EU AI Act conversations, говорит с institutional gravity major consortium [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §11.2 Gate G5]

**BOSC-A-T-X gate decomposition (systems-expert scalability view):**

| Gate | First trigger | Observable | MHT event |
|---|---|---|---|
| €50K (G1, current) | C+S (Composition + Scale) | Phase-1 чат «попутно» переходит из 0 к первым 5-20; zero-mechanics → первые portrait templates drafted | Phase Promotion (precursor → design-ready) |
| €200K (G2) | A (Agency) | Founder coordination ceiling hit; first Alliance members require agency-shift: Ruslan не единственный модератор | Role-Lift (Ruslan lifts от solo-moderator к architect-overseer) |
| €1M (G3) | S+C (Scale + Composition) | Magnitude triggers VSM Level-3 emergence: audit/optimisation function (portrait quality review, match KPIs, churn analysis) becomes distinct sub-system | Phase Promotion (implicit L3 → explicit operational function) |
| $100M (G4) | T (Time) | Time-horizon shifts: quarterly planning → multi-year; multi-language sub-networks require longer-cycle governance decisions | Context Reframe (governance artefacts re-anchored to multi-year horizon) |
| $1T (G5) | X+B (eXternal + Boundary) | Regulatory bodies + standards organisations become constituents, not externalities; Secure Network boundary expands to include them | Fusion (regulators/standards bodies become part of the holon) |

## 9. Cross-Direction Dependencies

### Зависит от:

- **§3.1 AI Consulting (primary pipeline):** первые Secure Network члены = graduated consulting clients passing D22. Без Phase-1 consulting engagements нет quality-seeded founding members. Consulting → Secure Network = principal arc [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md §2 Secure Network row]
- **§3.4 Matchmaker:** AI-smoothed coordination (Phase-2) требует digital portraits существующих; Secure Network membership gate = prerequisite для Phase-3 Matchmaker platform mode (community liquidity required). Взаимозависимость критическая: нет member liquidity → matchmaker platform stalls; нет matchmaker → Secure Network value proposition weaker
- **§3.7 Educational Products:** methodology + digital-portrait training materials создаются в §3.7; Secure Network = distribution channel + beta-test audience для educational products; educational content seeds subnetwork conversations
- **§3.3 USB-C Integration Services:** client-private KB primitives для digital portrait architecture — portrait YAML в Jetix KB использует те же patterns что USB-C client-private KB; infrastructure reuse

### На неё зависят:

- **§3.4 Matchmaker Phase-3+:** platform mode requires Secure Network member liquidity (100+ active + ≥30 connection-events/мес) as precondition [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.3]
- **§3.6 YouTube-analyzer SaaS:** distribution channel — analyst-product outputs distribution to Secure Network engineer/investor subnetworks; research insights seed высококачественные conversations
- **§3.2 Producer (Продюсерский центр):** блогер-члены Secure Network = production-retainer pipeline; они видят Jetix methodology working from inside → natural buyers for §3.2 services

### Cross-cutting:

- **Alliance Foundation (L6 §5 Option C):** Secure Network = operational-community layer; Alliance = governance-structure layer; они interlocked. Option C Hybrid позволяет Secure Network membership soft-bundle с Foundation membership fee [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5]
- **D25 Company-as-Code:** Secure Network membership events = commits в git; invite provenance в `edges.jsonl`; portrait YAML versioned; community state reconstructable from git history [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D25]
- **D27 Fork-and-Merge:** Secure Network subnetworks = potential fork-community participants; каждый субканал может fork methodology и return mutations upstream; canonical Jetix upstream = quality bar [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D27]

## 10. Open Questions (5)

**Q1 — Telegram backup path (operational priority: Phase-2 gate):**
Если Telegram deprecates Bot API / API изменяется / government blocks (возможно в DACH при определённых regulatory сценариях): Discord secondary (weaker privacy, gaming-perception у DACH Mittelstand) vs own-platform (Phase-3+ capex per D15) vs Matrix protocol (open-source ActivityPub-like, less mainstream adoption)? Plan Phase-2 architectural gate: migration-readiness escape hatch (member export format + migration drill) должен быть locked до Phase-2 Secure Network launch. **Рекомендация: закрыть на Phase-2 gate, не defer к Phase-3** [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §10.8 Engineering dissent S10-D1].

**Q2 — Digital portrait ownership + data residency (EU GDPR compliance):**
Член владеет portrait data; где хранится если EU-sovereign required для DACH? Hetzner self-hosted? Client-private KB pattern из §3.3 применённый на person-level? Telegram chat data — технически вне прямого контроля Jetix (GDPR data-deletion caveat документирован в L6 §10.2 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §10.2]). Вопрос требует legal review перед Phase-2 launch.

**Q3 — Складчина pricing structure (L7 owns final):**
Flat subscription vs usage-tiered vs free-for-contributors? Contributors (приносят matched specialists / content / referrals) — revenue-share или tier-upgrade или оба? Structural tension: если складчина value велик, нужна fair-use enforcement; если нет enforcement → heavy users subsidised by light users → light users churn. L7 Business Deep-Dive должен resolve pricing architecture, не L5.

**Q4 — Дуров contact timing (open from L6 §12):**
Telegram partnership aspirational per audio_524 [src:reports/review_2026-04-24.md audio_524]; L6 §10.6 позиционирует как «potential future contact, NOT assumed». Вопрос: является ли это Phase-2 pursuit (до €200K) или Phase-3+ opportunistic (после platform maturity)? Assumption: стандартный Bot API достаточен для Phase-2; Дуров-specific extensions = additive upside, не critical path. **Нет action до explicit Ruslan ack на timing**.

**Q5 — Fork-community governance operationalization для Secure Network subnetworks (D27 downstream):**
D27 locked: каждый participant может fork + лучшие мутации возвращаются upstream [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D27]. Но operational mechanics для Secure Network subnetwork forks unclear: если субканал "Engineers" форкает methodology → создаёт свою версию Jetix methodology для engineering firms → Jetix-Corp proprietary-core + Foundation-upstream boundary как удерживается? Option C resolves governance at Alliance level, но subnetwork-level fork mechanics требуют explicit design на Phase-2 before first forks open.

---

## Integrator synthesis (F/ClaimScope/R block)

**Claim 1 (основной):** Secure Network как paid-subscription продукт активируется на G2 €200K gate и является retention + compounding layer для consulting-клиентов, прошедших D22, с уникальным дифференцирующим элементом — складчина AI-tool-pooling.

- **F:** F4 (operational convention; rests on L6 §10 + JETIX-PLAN §4.4 + D15 spend-lock + JETIX-VISION D5 + D16 explicit phase distinctions)
- **ClaimScope:** Holds at Phase-2 (€50K-€1M scale, 50-200 members, Telegram-primary); NOT validated at Phase-3+ scale (200+ members with multi-archetype subchannels — matchmaker platform dependency unresolved at this stage); unknown at $100M+ (VSM Level-3 explicit instantiation required)
- **R:** Refuted if Phase-2 launch collects <10 paying members within 6 months of G2 gate crossing, suggesting D22 filter + складчина value proposition insufficient; accepted if Secure Network subscription revenue exceeds 15% of total Jetix revenue by G3 gate (per L6 §11.2 migration trigger to G4)

**Claim 2 (системный):** Складчина mechanic + D22 quality-gate + digital portrait system как совокупность формируют antifragile design для Secure Network: система улучшается от добавления членов (network effects), но не деградирует от их роста при условии, что portrait-completion gate wired to premium feature access остаётся structural rule, не suggestion.

- **F:** F4 (rests on Meadows L4 leverage point logic + Beer VSM System-3 + L6 §11.2 G3 leverage analysis)
- **ClaimScope:** Holds at Phase-2/3 transition; requires structural enforcement (portrait-completion ≥80% = hard gate, not soft recommendation); unknown Phase-3+ when own-platform transition adds engineering complexity
- **R:** Refuted if Secure Network member quality degrades despite D22 gate + portrait requirement; accepted if match-rate KPI and member NPS remain ≥ L6 §6.5 targets for ≥3 consecutive quarters post Phase-3 launch

**Preserved dissents** — см. frontmatter `dissents[]` + §7 Competitive Positioning risks:

**§3.5-D1 (Telegram structural dependency):** Telegram-as-primary = third-party platform risk на всём Phase-1/2 горизонте. Mitigation в L6 §10 design (portrait data в Jetix KB, не Telegram), но API ToS risk остаётся. F4. ClaimScope: Phase-1 через Phase-2; NOT resolved at Phase-3+ own-platform transition.

**§3.5-D2 (Складчина ToS exposure):** shared credentials = vendor ToS risk. Compliant path (team-seat / enterprise pricing) должна быть verified per tool before Phase-2 складчина launch. F3. ClaimScope: applies to any subscription SaaS prohibiting credential sharing; does not apply if enterprise pricing available.

---

*Draft produced by systems-expert × integrator, cell C-06. Цитаты из L6 §10 inherited per hard anti-scope (NO reopening L6 §10 architecture). Pricing placeholders per anti-scope (NO final pricing — L7 owns). Word count estimate: ~2100 words.*
