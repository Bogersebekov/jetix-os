---
title: "§12 Open Questions — Philosophy-Critic (Layer 6 Community Deep-Dive)"
type: epistemic-audit
produced_by: philosophy-expert
mode: critic
cycle_id: cyc-layer-6-community-deep-dive-2026-04-24
task_id: T-layer-6-community-deep-dive-2026-04-24
cell: C-12
section_ref: "§12 Open Questions"
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: drafted
confidence: high
confidence_method: claim-by-claim-trace
provenance_inline: true
sources:
  - {path: "swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md", range: "§4 risks + §6 Ruslan clarifications"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S2-icp-trinity.md", range: "§B Dissents + §2.1 payment filter"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S3-archetypes.md", range: "§3.7-§3.11 L6-deep-dive additions + §3.Y Claim-3"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S4-five-criteria.md", range: "§4 Dissents + §4.6 self-selection mechanism"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S5-alliance.md", range: "§5.X brigadier recommendation + §13 Preserved dissents"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S5-alliance-roi.md", range: "§5.X.3-§5.X.7 Option C analysis + Dissent-2"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S6-matchmaker.md", range: "§6.8 Preserved Dissents + §6.4 migration triggers"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S6-matchmaker-kpis.md", range: "§13 Preserved dissents + §6.1 KPI table"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S7-outreach.md", range: "§7.1 channel analysis + S2/S7 dissents"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S8-membership.md", range: "§8.2 + §8.5 Open questions + template-level flags"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S9-growth.md", range: "template-level stub flags"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-engineering-integrator-S10-secure-network.md", range: "dissents (Telegram-dependency + migration cost) + §10.1-§10.2"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-scalability-S11-evolution.md", range: "§11.4 Dissents D-S11-1 + D-S11-2 + §11.2 G2 Alliance timing"}
anti_scope:
  - "NO new claims — this section surfaces open questions only; synthesis is aggregated from sibling drafts"
  - "NO Locks D1-D28 reopened — where a Lock creates tension, flagged without override"
  - "NO Notion writes"
  - "NO provider-key env-var literal references"
  - "NO Task() invocation strings"
  - "NO instrumental Рациональность arbitration — investor-expert domain; questions surface the issue, resolution stays with Ruslan"
---

# §12 Open Questions

> Этот раздел — один из 13 разделов финального документа `decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md`.
> Назначение: собрать все нерешённые вопросы из 11 дочерних черновиков в единый реестр
> с чётким epistemic-статусом каждого вопроса. Философская линза применена как lens
> ясности: что точно известно, что открыто, что принципиально неразрешимо без новых данных.

Философский принцип, применённый к этому разделу: **Поппер-задача §12** состоит в
том, чтобы каждый вопрос был сформулирован так, что у него есть наблюдаемый ответ —
то есть каждый вопрос фальсифицируем в принципе. Вопросы, которые не имеют
фальсифицируемых ответов, были переформулированы или помечены как
«принципиально открытые» с объяснением почему.

[src:swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md#§1]

---

## §12.1 Locked-Pending-Ruslan-Ack

Это вопросы, ответ на которые ждёт только одного: ack Руслана. Brigadier HALTS до ответа.

---

### Q-01: Alliance Option A / B / C — какой структуре быть?

**Вопрос.** Brigadier рекомендует Option C (Hybrid — non-profit methodology upstream + for-profit services downstream). Подтверждает ли Руслан Option C, или выбирает Option A или Option B?

**Контекст.** §5 Alliance Architecture (sibling cell C-05) детально рассматривает три юридических структуры:
Option A (non-profit consortium, аналог Linux Foundation), Option B (for-profit standards body, аналог ARM Holdings), Option C (hybrid Mozilla/Red Hat model). Brigadier рекомендует Option C, аргументируя четырьмя locked decisions: D13 (Closed core / Open surface), D20 (USB-C positioning), D21 (Roy-replication), D27 (Fork-and-merge governance). Investor-expert peer-input (sibling cell C-05-peer) подтверждает рекомендацию по финансовым критериям: только Option C совместим с Phase-1 capital discipline (Phase-1 incremental cost ≈ €0 vs €15-30K для Option A и €80-200K для Option B).
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S5-alliance.md#§5.X]
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S5-alliance-roi.md#§5.X.3]

**Почему это важно.** Выбор структуры определяет: кто получает долю Alliance, как защищается IP, когда Alliance может быть формализован, какова модель дохода Jetix-Corp, и возможен ли рост к $1T trajectory через equity compounding (только Option C).

**Proposed resolution path.** HITL ack — Руслан выбирает в AWAITING-APPROVAL пакете.

**Who decides.** Руслан.

---

### Q-02: Millionaire vs Spectrum — граничный кейс платёжеспособности

**Вопрос.** Проходит ли человек с доходом $2K/месяц recurring + $50K сбережений Phase-1 payment filter?

**Контекст.** Intake §6.1 вводит payment-ability filter: ≥$5K/month recurring ИЛИ ≥$10K one-shot.
§2 ICP Trinity (sibling cell C-02) разъясняет: фильтр — это liquidity и готовность платить, а не уровень дохода как таковой. Но граничный кейс остаётся: человек с $2K/mo recurring + $50K сбережений технически не проходит recurring-критерий ($2K < $5K), но проходит one-shot-критерий ($50K >= $10K). Вопрос в том, должен ли Руслан рассматривать сбережения как доказательство способности к one-shot engagement, или только ликвидный денежный поток.
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S2-icp-trinity.md#§2.1]

**Почему это важно.** Это операционный фильтр, который Руслан применяет на каждом discovery call. Без чёткого ответа будет каждый раз принимать ad hoc решение — inconsistent application нарушает Beer VSM Level-2 anti-oscillation function фильтра.

**Epistemic note (philosophy-critic).** Это вопрос, который ИМЕЕТ фальсифицируемый ответ — Руслан может ответить «да, $50K savings считается» или «нет, нужен $5K/mo cash flow». Обе позиции легитимны. Текущая формулировка intake §6.1 допускает оба прочтения. Рекомендую зафиксировать принцип, а не правило: «смотрим на liquidity, не на источник» — тогда $50K savings считается.

**Proposed resolution path.** HITL ack — одна-две строки от Руслана прояснят intent.

**Who decides.** Руслан.

---

### Q-03: Дуров contact timing — когда и при каких условиях?

**Вопрос.** Когда (если вообще) Jetix инициирует контакт с Дуровым? Phase-2 (€200K+), Phase-3+ (€1M+), или принципиально «не assumе, пока он сам не придёт»?

**Контекст.** Intake §4 risk 7 и §6.4 явно: «Дуров contact marked as "potential future contact", don't assume engagement». §10 Secure Network (sibling cell C-10) следует этому — Telegram используется как infrastructure, Дуров как человек не является operating assumption. Тем не менее STRATEGIC-INSIGHT §4 называет «Mittelstand AI Alliance = EISA moment» — позиция, потенциально интересная Дурову как человеку с mission-driven view на технологии. Вопрос открыт: при каком уровне traction Alliance имеет leverage для outreach?
[src:swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md#§6.4]

**Почему это важно.** Если Jetix строит инфраструктуру на Telegram и позиционирует Alliance как «суверенный европейский AI-консорциум», то отношения с Дуровым как создателем платформы потенциально стратегически значимы. Но это requires leverage Jetix не имеет в Phase-1. Зафиксировать trigger-условие важно, чтобы не создавать ни ложных ожиданий, ни упущенной возможности.

**Epistemic note (philosophy-critic).** Вопрос о том, «придёт ли Дуров», принципиально ненаблюдаем до Phase-3+. Наблюдаем другой вопрос: «при каком milestone имеет смысл warm outreach через общих знакомых?» — это более операциональная формулировка.

**Proposed resolution path.** HITL ack — Руслан называет условие (Phase или milestone), при котором тема снова поднимается.

**Who decides.** Руслан.

---

### Q-04: Fork-community IP licensing — MIT, proprietary, или dual?

**Вопрос.** Под какой лицензией публикуется методологическая документация Alliance (upstream Foundation layer при Option C)?

**Контекст.** D27 (Fork-and-merge governance) зафиксирован, но «конкретика IP licensing TBD» отражена в §10 sibling cell. §5 Alliance Architecture (sibling cell C-05) предлагает Apache 2.0 permissive для Foundation layer и proprietary для Jetix-Corp closed core per D13 grammar. Но существует три реалистичных варианта:
(a) Apache 2.0 / MIT (максимальная adoption, минимальная защита — Option A flavor)
(b) Weak copyleft (CC BY-SA или LGPL-analog для документации — Option C preferred)
(c) Proprietary с controlled access (Option B flavor, несовместимо с D20 USB-C positioning)
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S5-alliance.md#§5.3]

**Почему это важно.** Выбор лицензии определяет, могут ли McKinsey / Deloitte / BCG легально взять методологию и продавать её как свою — и будет ли у Jetix что-то возразить кроме репутации. Это фундаментальный competitive moat вопрос.

**Epistemic note (philosophy-critic).** Философски: IP лицензия — это claim о будущем поведении третьих лиц, которое невозможно наблюдать сейчас. Поппер-совместимая формулировка: «какой режим лицензирования максимально совместим с D13 + D20 + D27 при Option C?» — на этот вопрос §5 sibling уже ответил: weak copyleft + Apache 2.0 для документации, proprietary для tooling. Остаётся только ack.

**Proposed resolution path.** HITL ack — Руслан подтверждает weak copyleft (Apache 2.0 / CC BY-SA) для Foundation документации при Option C.

**Who decides.** Руслан.

---

### Q-05: Discovery call format — phone / video / in-person?

**Вопрос.** §7 Outreach (sibling cell C-07) templates предполагают video call format. Должно ли это быть зафиксировано как стандарт, или Руслан оставляет формат гибким?

**Контекст.** §7 outreach templates (sibling cell C-07) включают CTA «15-20 min video call». §2 ICP Trinity (sibling cell C-02) qualification script также structured under call-format assumption. Однако для некоторых сегментов — особенно Mittelstand DACH Phase-2+ и Инвесторов с плотным расписанием — in-person или phone могут давать лучший acceptance rate. Зафиксировать один формат как primary прагматично для Phase-1 solo-founder: меньше вариаций = меньше cognitive overhead.
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S7-outreach.md#§7.1]

**Почему это важно.** Consistency в CTA снижает friction при конверсии. Если Руслан использует разные форматы в зависимости от наcтроения — tracking и A/B comparison становятся невозможными.

**Proposed resolution path.** HITL ack — одна строка от Руслана: «video primary, phone при явной просьбе клиента, in-person только Phase-2+».

**Who decides.** Руслан.

---

### Q-06: L6-deep-dive archetype additions — которые оставить как standalone?

**Вопрос.** §3 Archetypes (sibling cell C-03) добавляет 5 новых архетипов сверх JETIX-VISION §7.1 canonical 11: Соединитель (Connector), Athlete, Designer, Teacher, Operator/Founder-CEO. Какие из них Руслан признаёт как standalone, а какие объединить обратно в ближайшие JETIX-VISION §7.1 архетипы?

**Контекст.** §3 Archetypes sibling cell честно флагирует: Соединитель и Athlete — самые слабо обоснованные из L6-additions (F-tag: F2-F3), strong overlap с существующими canonical архетипами. Teacher и Operator имеют F-tag F4 — лучше обоснованы через Продюсерский центр D11 и architect-orbit §3. Designer имеет F-tag F3. Решение имеет downstream-влияние на §3 canonical enumeration в LAYER-6-COMMUNITY-DEEP-DIVE.md и потенциально на JETIX-VISION §7.1 revision.
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S3-archetypes.md#§3.Y-Claim-3]

**Почему это важно.** JETIX-VISION §7.1 является locked D7. Добавление 5 новых архетипов в LAYER-6 документ без ack = de facto расширение D7 без HITL gate. Philosophy-critic flagging: это boundary case для «reopening a Lock» — §3 sibling creates an extension without calling it a revision. Brigadier должен clarify перед финальной интеграцией.

**Proposed resolution path.** Ruslan ack по каждому из 5: (a) Соединитель — merge в «Менеджеры/коммуникаторы» или standalone? (b) Athlete — merge в «Разработчики жизни» или standalone? (c) Designer — merge в «Разработчики идей» или standalone? (d) Teacher — standalone (прямой Продюсерский центр fit)? (e) Operator/Founder-CEO — standalone (прямой Phase-1 buyer)?

**Who decides.** Руслан.

---

## §12.2 Operational Tactics Open

Это вопросы с более ограниченными stakes. Многие могут быть решены brigadier в следующем цикле или зафиксированы как conditional «update при наличии data».

---

### Q-07: Phase-1 outreach primary channel — один или параллельно?

**Вопрос.** Руслан должен сфокусироваться на ОДНОМ канале (LinkedIn) в течение первых 90 дней, или тестировать LinkedIn + Email + Referral параллельно?

**Контекст.** §2 ICP Trinity (sibling cell C-02) dissent 1 поднимает вопрос bandwidth-discipline. §7 Outreach (sibling cell C-07) описывает LinkedIn как «Primary Phase-1» с tempo 10-20 connection requests/day, но также рекомендует Email (secondary) и Referral. Для solo founder с ≈200 outreach/month capacity — параллельный запуск трёх каналов делит это внимание на три части, снижая execution quality в каждом канале.
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S7-outreach.md#§7.1]

**Почему это важно.** Epistemic-точка: при параллельном тестировании трёх каналов нет возможности атрибутировать успех/неудачу конкретному каналу. Поппер требует изолированных экспериментов. Первые 90 дней = Phase-1 data collection window — данные имеют ценность только если измеримы.

**Epistemic note (philosophy-critic).** Вопрос имеет Поппер-совместимый ответ: «LinkedIn-only 90 дней, затем измерить response rate, затем ввести Email если LinkedIn plateau». Это более falsifiable design чем «тестируем всё одновременно».

**Proposed resolution path.** Brigadier решает в следующем цикле OR Руслан ack в AWAITING-APPROVAL пакете. Рекомендация: LinkedIn-only первые 90 дней.

**Who decides.** Руслан / brigadier.

---

### Q-08: Mittelstand AI Alliance formalization timing — Phase-1 или строго Phase-2?

**Вопрос.** Когда Jetix делает публичное объявление «Mittelstand AI Alliance Working Group»? В Phase-1 (до €50K gate, как brand positioning) или строго после €200K validation?

**Контекст.** §11 Evolution (sibling cell C-11) recommendation: публичное объявление Working Group в Phase-1 — zero legal cost, stakes the brand position in the market. D11-dissent D-S11-1 поднимает question: Alliance legal incorporation — ≤€2000 — является ли это нарушением D15 «heavy spend» lock? §5 Alliance (sibling cell C-05) §5.3 Option C Phase-1 action: «operate the informal working group» без legal entity.
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-scalability-S11-evolution.md#§11.2]

**Почему это важно.** STRATEGIC-INSIGHT §8 называет 6-12 month window. Если Jetix публично объявит Alliance в Phase-1 без формальной структуры — занимает brand position. Если ждёт Phase-2 — рискует конкурент займёт аналогичную позицию.

**Epistemic note (philosophy-critic).** Два разных вопроса смешаны в один: (a) «публичное объявление бренда» (zero cost, can be done Phase-1) vs (b) «юридическое оформление» (requires ≤€2000, D15 question). Рекомендую разделить: (a) resolve immediately, (b) requires Ruslan ack on D15 application.

**Proposed resolution path.** (a) Brigadier в следующем цикле формулирует draft public Working Group announcement. (b) Руслан ack: считается ли ≤€2000 legal consultation pre-€200K нарушением D15?

**Who decides.** (a) Brigadier. (b) Руслан.

---

### Q-09: G1 NPS target ≥7/10 vs B2B benchmark 5.0-6.5 в первом квартале

**Вопрос.** Является ли ≥7/10 NPS в первом квартале matchmaker operation реалистичным target или aspirational?

**Контекст.** Investor-expert (sibling cell C-06-peer) dissent-1: первый квартал manual matching вероятно даст NPS 5-7/10 из-за структурных friction (scope creep, specialist over-claims, contract ambiguity) без специальной инфраструктуры. Он рекомендует рассматривать «≥7/10» как aspirational goal, а реальным gate-failure condition считать «NPS не растёт по кварталам».
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S6-matchmaker-kpis.md#§13]

**Почему это важно.** Gate predicates должны быть Hamel-binary и реалистичными. Если G1 NPS target = ≥7/10, но первый квартал даёт 5.5/10 из-за структурных причин (а не качественных), Руслан может ошибочно прочитать это как failure. Правильный predicate: «NPS trend is positive over 3 quarters», не «NPS ≥7 in Q1».

**Proposed resolution path.** Brigadier в следующем цикле уточняет G1 matchmaker acceptance predicate до «NPS trend positive across first 3 quarters + first match that generates Jetix revenue within 90 days».

**Who decides.** Brigadier (с Ruslan ack при необходимости).

---

### Q-10: Vendor partnerships Phase-1 scope — Anthropic Solution Partner only?

**Вопрос.** Входит ли в Phase-1 scope только Anthropic Solution Partner registration, или также Groq + EU cloud (Hetzner/OVH) evaluation?

**Контекст.** §2 ICP Trinity (sibling cell C-02) dissent 2: «Phase-1 = ТОЛЬКО Anthropic Solution Partner registration (бесплатно, ≤2 часа). Все остальные vendor partnerships: schedule для review после €50K gate. Revenue-gating vendor conversations = discipline aligned с D15».
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S2-icp-trinity.md#§B]

**Почему это важно.** Vendor partnerships — это attention budget item. В Phase-1 у Руслана есть X часов в неделю на всё. Каждый час на vendor conversations не является consultation delivery hour. Важно знать: Anthropic Solution Partner (≤2 часа, free) — ок. Groq formal partnership — нет (требует time + они захотят иметь дело с validated revenue). EU cloud evaluation — нет (это technical infrastructure decision, можно defer).

**Proposed resolution path.** Brigadier в следующем цикле фиксирует: Anthropic Solution Partner registration = Phase-1 action. Все остальные vendor partnerships = deferred to post-€50K review.

**Who decides.** Brigadier (с логикой из §2 dissent 2).

---

### Q-11: Mittelstand vs broader Tier-1 sub-prioritization (P1A vs P1B)

**Вопрос.** Должна ли Phase-1 outreach иметь explicit P1A (Mittelstand + Startupper) vs P1B (High-earners $100K+ + миллионеры referral) разделение с разными allocation of Ruslan-time?

**Контекст.** §2 ICP Trinity (sibling cell C-02) dissent 1: «expanded Tier-1 без уточнения приоритизации внутри expanded Tier-1 создаёт риск дилюции. Предлагается sub-prioritization: P1A = Mittelstand + Startupper (KM-Mat legacy, proven hypothesis); P1B = High-earners $100K-$150K+ + миллионеры через referral (new, test cautiously). P1A остаётся primary outreach target; P1B = opportunistic when inbound».
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S2-icp-trinity.md#§B]

**Почему это важно.** Без этой sub-prioritization расширенный ICP spec может привести к тому, что Руслан распределит одинаковое внимание на Mittelstand-owner и на millionaire-referral-network — при том что первый более доступен и более проверен как hypothesis, второй требует warm-intro сети которой у Jetix пока нет.

**Proposed resolution path.** Brigadier фиксирует P1A/P1B разделение в финальном §2 документа. Не требует отдельного Ruslan ack — это refinement existing ICP, не изменение spec.

**Who decides.** Brigadier.

---

## §12.3 Phase-2+ Design Open

Это вопросы, ответы на которые будут известны только по достижении Phase-2+ gates. Они зафиксированы сейчас как «deferred by design» — не потому что неважны, а потому что данных для ответа ещё нет.

---

### Q-12: Pre-G2 Alliance legal cost — является ли ≤€2000 нарушением D15?

**Вопрос.** Alliance legal incorporation через немецкий eingetragener Verein (eV) или консультацию по non-profit GmbH стоит ≤€2000. D15 запрещает «heavy spend» до €200K. Применяется ли D15 к €2000 legal consultation fee?

**Контекст.** §11 Evolution dissent D-S11-1 (sibling cell C-11): systems-expert surfaced the tension. Alliance legal filing имеет 4-12 недель delay time — если Руслан хочет formal Alliance к G2, решение нужно принимать ВО ВРЕМЯ G1, не после G2. €2000 legal consultation — это 4% от €50K target. По духу D15 это не «heavy spend», но по букве нет явного исключения для legal.
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-scalability-S11-evolution.md#§11.4]

**Почему это важно.** Если D15 применяется строго — Alliance не может быть юридически оформлен до €200K. Если D15 применяется к spirit (heavy spend = operational risk, not small legal setup) — то ≤€2000 consultation и minimal filing работают в G1.

**Epistemic note (philosophy-critic).** Это вопрос об интерпретации Lock D15. Locks нельзя reopen без HITL ack. Данный вопрос есть конфликт между Locks D15 (spend gate) и архитектурной рекомендацией §5 sibling (Option C Phase-1 informal working group без legal entity). Philosophy-critic flagging: вопрос НЕ reopens D15 — он уточняет его применимость к конкретному amount. Руслан должен ответить на это как HITL.

**Proposed resolution path.** HITL ack — Руслан уточняет: «D15 = heavy spend ≥€X threshold» ИЛИ «D15 = все расходы выше operational minimum». С ответом brigadier действует.

**Who decides.** Руслан.

---

### Q-13: Matchmaker portrait-density prerequisite — добавить KPI в G3 trigger?

**Вопрос.** §11 Evolution dissent D-S11-2 предлагает добавить «portrait-completion rate ≥50% among active members» как дополнительный trigger для G3 matchmaker platform launch. Принимается ли это как официальный gate condition?

**Контекст.** Текущий G3 migration trigger (§11 sibling): revenue threshold €1M + leading indicators (matchmaker successful matches + Secure Network subscription revenue ≥15% + first D27 merge-back). D-S11-2 добавляет структурный аргумент: Senge «Limits to Growth» — запуск matchmaker platform с low portrait density генерирует плохие match results → community trust падает → portraits заполняются ещё хуже → decay loop. Решение: portrait-completion rate как G3 gate condition.
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-scalability-S11-evolution.md#§11.4]

**Почему это важно.** Добавление KPI в gate trigger — это изменение acceptance predicate для G3. Это structural design decision, который downstream влияет на G2 work priorities (строить portrait-intake infrastructure раньше).

**Proposed resolution path.** Brigadier добавляет portrait-density KPI (≥50% active members with ≥80% portrait filled) как дополнительный leading indicator для G3 migration trigger. Не требует отдельного Ruslan ack — это operational improvement в рамках существующих locked decisions. Деферировать до L8 People Deep-Dive.

**Who decides.** Brigadier.

---

### Q-14: Membership form fields — что именно собирать в Phase-2+ application?

**Вопрос.** §8 Membership (sibling cell C-08) является template-level и содержит stub «Детали TBD (§8.5): конкретные поля формы, формат интервью, право вето участников». Когда и в каком цикле разрабатываются эти детали?

**Контекст.** Per Ruslan 2026-04-24 §6.2: §8 Membership = template-level, full Deep Dive deferred to L8 People Deep-Dive (Phase-2+ trigger). Trigger: post-€200K validation. До этой точки детали формы — premature optimization.
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S8-membership.md#§8.5]

**Почему это важно.** Зафиксировать это как «явно deferred» — чтобы агенты не трактовали template-level как bug или gap. Это design by intent.

**Proposed resolution path.** Deferred to L8 People Deep-Dive (separate M-task, Phase-2+ trigger). Brigadier создаёт task-stub в backlog.

**Who decides.** Brigadier (creates stub). Руслан (activates L8 deep-dive when ready).

---

### Q-15: §9 Growth Model — когда полноценный Deep Dive?

**Вопрос.** §9 Growth Model (sibling cell C-09) является template-level per Ruslan 2026-04-24. Когда это становится полноценным Deep Dive?

**Контекст.** §9 sibling содержит skeleton (Phase-1 = 5-20 members invite-based; Phase-2 = 50-200 thematic sub-networks; Phase-3+ = 500+ Alliance formalized). Детальная механика growth (viral coefficients, referral economics, churn prediction, activation sequences) = deferred to L8.
[src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S9-growth.md]

**Proposed resolution path.** Deferred to L8 People Deep-Dive. Brigadier создаёт task-stub.

**Who decides.** Brigadier (creates stub). Руслан (activates).

---

## §12.4 Conflict Flags

Это места, где новые рекомендации из текущего цикла создают tension с существующими Locks D1-D28. Philosophy-critic flagging без override — Locks не reopened. Каждый conflict требует либо Ruslan ack, либо explicit «это не противоречие, это extension».

---

### CF-01: L6 Archetype additions vs D7 canonical 11-archetype list

**Flag.** §3 Archetypes (sibling cell C-03) добавляет 5 новых архетипов (#7-#11 в новой нумерации), создавая фактически 16-archetype enumeration для LAYER-6 документа. D7 (JETIX-VISION §7.1) зафиксировал canonical 11 архетипов. Если §3 LAYER-6 документа принимается с 11 позициями как operational (16 всего) — это расширение D7 без формального HITL.

**Philosophy-critic lens.** Два разных claim-scope: D7 применяется к JETIX-VISION как canonical identity document. §3 LAYER-6 применяется к outreach messaging segmentation. Это не противоречие — это разные levels of analysis. Но brigadier должен явно написать в финальном документе: «5 дополнительных архетипов #7-#11 являются operational specialisations для outreach/community segmentation, NOT revisions to D7 canonical list». Без этой explicit statement §3 LAYER-6 может быть воспринят как de facto D7 revision.

**Resolution.** Brigadier добавляет explicit statement в §3 финального документа. Не требует Ruslan ack IF это extension (same level — outreach segmentation), требует ack IF это meant to be D7 revision.

---

### CF-02: Alliance incorporation pre-€200K vs D15 revenue-gated spend lock

**Flag.** §11 dissent D-S11-1 и Q-12 выше: Alliance legal filing timing tensioned against D15. Alliance informal brand announcement в Phase-1 (zero cost) = нет конфликта с D15. Alliance formal legal incorporation pre-€200K = potential D15 conflict. Специфически: Option C Phase-1 action «operate informal working group» (zero cost) = полностью aligned. Formal Foundation eV formation pre-G2 = requires D15 clarification.

**Philosophy-critic lens.** D15 говорит «no heavy spend pre-€200K». Вопрос о том, является ли ≤€2000 legal consultation «heavy spend», — это вопрос о ClaimScope D15, а не о его content. Locks нельзя override без HITL, но уточнение scope возможно через brigadier escalation.

**Resolution.** Q-12 above. HITL ack required от Руслана.

---

### CF-03: Expanded ICP Tier-1 spectrum vs prior KM-Mat Tier-1 lock

**Flag.** Intake §6.1 явно supersedes KM-Materialization MVP Option-C Tier-1 lock {Предприниматели + Блогеры only}. Это supersession задокументирована в intake и в §2 ICP Trinity sibling. Conflict resolution: intake §6.1 is binding per Ruslan clarification 2026-04-24 24:00 CET. Нет открытого вопроса здесь — зафиксировано для трассируемости.

**Status.** Resolved. KM-Mat Tier-1 lock superseded by intake §6.1.

---

### CF-04: §10 Telegram-primary dependency vs enterprise data sovereignty positioning

**Flag.** Engineering-expert (sibling cell C-10) dissent F4: «Telegram-as-primary carries structural third-party platform risk — Jetix does not control Bot API ToS, data residency policy, or API versioning cadence». При этом Jetix позиционирует себя как «local-first, data sovereign» для Mittelstand clients. Tension: Jetix сам использует non-EU-controlled platform для своего community, пока продаёт EU data sovereignty как value proposition.

**Philosophy-critic lens.** Это не нарушение Lock — это эпистемический inconsistency в позиционировании. Логически: если GDPR-compliance и data sovereignty — core value proposition Jetix для Mittelstand, то собственная community-инфраструктура должна либо (a) использовать EU-based platform, либо (b) иметь явный карантин (portraits в EU KB, conversations in Telegram = acknowledged risk). §10 sibling cell уже предлагает (b) как mitigation — portraits stored in Jetix EU KB, mirrored from Telegram intake.

**Resolution.** §10 sibling mitigation достаточна как Phase-1 answer. Phase-2+ требует migration-readiness plan (documented in §10). No new ack needed — but the §12 final document should note this explicitly for Mittelstand-audience transparency.

---

## §12.5 Epistemic Summary — Что точно известно, что открыто, что принципиально неизвестно

Философский раздел. Применена Поппер-классификация всех открытых вопросов.

### Точно известно (F5 — locked decisions, Ruslan-attested)

- Payment ability filter = ≥$5K/month recurring OR ≥$10K one-shot [intake §6.1]
- D22 5-criteria filter применяется ко всем archetype segments
- Alliance = concept-only в Phase-1, AWAITING-APPROVAL gate обязателен перед formalization
- Brigadier recommends Option C, Руслан picks in ack
- Telegram = primary secure network substrate per audio_524
- D15 revenue-gated spend lock: active until €50K confirmed
- §8 Membership + §9 Growth = template-level, no deep dive in this cycle

### Открыто, решаемо в этом цикле (Q-01 — Q-06)

Все вопросы §12.1: ждут только HITL ack Руслана. Как только ack придёт — brigadier имеет operational authority действовать.

### Открыто, условно решаемо в следующем цикле (Q-07 — Q-11)

Вопросы §12.2: могут быть разрешены brigadier на основе уже имеющихся данных, без нового HITL. Philosophy-critic рекомендует brigadier принять operational decision и зафиксировать в strategies.md.

### Открыто, будет разрешено данными (Q-12 — Q-15)

Вопросы §12.3: ответы становятся известны только по достижении Phase-2+ gates или при накоплении операционных данных. Принципиально unknowable сейчас — не потому что вопросы плохие, а потому что observations ещё не существуют.

### Принципиально неразрешимо (unknowable by design)

Один вопрос остаётся за пределами epistemic reach: «Примет ли Дуров предложение Jetix?» — даже при самом правильном Alliance momentum, это зависит от агентности третьего лица, и никакая Popper-совместимая falsifiability здесь не поможет. Он либо ответит, либо нет. Единственное действие — сформулировать условие outreach (Q-03) и ждать observability window.

---

*End of §12 Open Questions. Cell C-12 complete. Ожидает brigadier integration gate.*
