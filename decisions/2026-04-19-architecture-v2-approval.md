---
id: ADR-2026-04-19-architecture-v2-approval
title: Architecture Synthesis v2 — Ruslan Approval Record
date: 2026-04-19
status: in-progress
phase: Stage 3 — Review v2 synthesis chunk-by-chunk
chunks-complete: [1]
chunks-pending: [2, 3, 4, 5, 6, 7]
type: architecture-decision
author: ruslan
scribe: claude-opus-4-7
source: raw/research/architecture-synthesis-v2-final.md
blocks: D1-D9 чистовики (Stage 4)
---

# ADR: Architecture Synthesis v2 — Approval Record

Живой ADR фиксирует утверждения Ruslan'а по результатам Stage 3 review
`raw/research/architecture-synthesis-v2-final.md` (1621 строка).

Обновляется по мере прохождения 7 чанков review.

Финальная версия (после Chunk 7) = основа для написания D1-D9 чистовиков
в Stage 4.

---

## Chunk 1 — High-level frame ✅ APPROVED 2026-04-19

### 1.1 Four framing questions — ALL ACCEPTED

| # | Вопрос | Decision | Nuance |
|---|--------|----------|--------|
| Q1 | Reference vs Operational Architecture split | ✅ ACCEPTED | "полностью принимаю, сразу же принимаем" |
| Q2 | L2 Cognitive as discipline (не папка) | ✅ ACCEPTED + усиление | "нам нужно по Левенчуку максимальная дисциплина, максимально вся глубокая онтология; всё правильно как нужно делать; это даже не обсуждается" |
| Q3 | Capital + Hours + Attention elevated в first-class | ✅ ACCEPTED | "заносим в first principles" |
| Q4 | Portability honesty addition ("roadmap goal v2.0+") | ✅ ACCEPTED | Ruslan note: "логика архитектуры позволит довольно быстро это всё переделать, учитывая возможности агентов быстро переписывать"; не врём себе, принимаем честно |

### 1.2 Seven Core Principles — APPROVED (с нюансами по P5 и P6)

#### P1 — Company-as-Code, буквально. Git = SoT
- **Status:** ✅ APPROVED as foundation
- **Ruslan quote:** "отлично мы это всё подтверждаем, фиксируем, это уже база прям база"
- **Implication:** Git = единственный SoT. Commit = акт управленческого решения. Notion decommission планируется в 7+7 rollout Day 8-14.

#### P2 — Role ≠ Executor (5-block role.md + separate binding.yaml)
- **Status:** ✅ APPROVED с усилением
- **Ruslan quote:** "подтверждаем и делаем все папки, ну вот всё что только возможно, глубоко, адекватно, мы это всё делаем"
- **Implication:** D3 (Role Manifests) детально прорабатывается. Разделение role.md / executors/<id>/binding.yaml соблюдается строго. Dynamic role assignment forbidden (с founder exception).

#### P3 — 7 true alphas + past-participle convention strict-enforced
- **Status:** ✅ APPROVED с усилением
- **Ruslan quote:** "всё делаем максимально правильно, то есть всё как там Левенчук говорит, всё как по логике, по красоте мы это делаем"
- **Implication:**
  - 7 true alphas (Client, Project, Deal, Content Item, Hypothesis, Member, Way of Working) materialized в `alphas/`
  - 3 work products (Invoice, Postmortem, ...) живут в `finance/` и `decisions/postmortems/`
  - 1 entity (SKU) — в `catalog/` или `decisions/policy/sku-catalog.md`
  - Past-participle audit применяется строго (52% v1 violations fixed)
  - U-Types Lite 6 (с Objective, Decision)
  - "What ШСМ is NOT" section в FPF-Lite

#### P4 — Model D Nested Hierarchy + lightweight mereology explicit
- **Status:** ✅ APPROVED
- **Ruslan quote:** "да, мы берём эту модель, тоже подтверждаю"
- **Implication:** Life-OS root → projects/jetix/ nested. Lightweight mereology explicit; advanced mereology (Kit Fine, constructor theory) excluded.

#### P5 — L0 Executive Core + 3 additions
- **Status:** ✅ APPROVED с MODIFICATION по trustee
- **Ruslan quote:** "всё подтверждаю, мы манифест пишем, всё что нужно для этого принципа, максимально всё используем"

**Component breakdown:**

| Component | Decision |
|-----------|----------|
| 5 atomic sub-roles (strategy-lead / framing-lead / sales-closer / acceptance-authority / external-relations) | ✅ ACCEPTED — manifests пишем |
| Executor `ruslan.yaml` with multi-role-binding flag (hybrid founder-mode) | ✅ ACCEPTED |
| Agent `strategist` → `strategy-support-analyst` rename (Левенчук §1.4 #2) | ✅ ACCEPTED |
| Bus-factor mitigation (`ops/hit-by-bus.md`, Constitution §11) | ✅ ACCEPTED — но **делаем чуть потом**, не Day 1 приоритет |
| **Designated trustee = Anton** (v2 synthesis default) | ❌ **REJECTED — trustee ≠ Anton** |
| Designated trustee identity | ⏳ **TBD — определим позже** |

**CRITICAL CHANGE vs synthesis:** v2 synthesis MC4 resolution явно назначал Anton designated trustee. Ruslan эксплицитно отверг: "но это будет потом, это будет тоже не Антон".

**Implication для MC4 (Chunk 2):** пересмотреть meta-conflict 4 resolution. Lightweight mitigation accepted в принципе, но trustee identity открыт. Это повлияет на:
- `ops/hit-by-bus.md` content
- `governance/trustee-designations.md`
- Constitution §11 succession protocol

**OT1 (Outstanding Tension #1) — RESOLVED EARLY:** Strategic-management decomposition question (из Chunk 4) resolved утверждением hybrid: 5 manifests + executor ruslan multi-role-binding. Вычеркнуть из Chunk 4 outstanding tensions.

#### P6 — DACH-context — PARTIALLY MODIFIED

- **Status:** ⚠️ PARTIAL / MODIFIED vs v2 synthesis
- **Ruslan quote:** "не совсем подтверждаю; основной упор на DACH, но при этом ещё будет US и русскоязычное тоже; они все у нас будут проходить через одну воронку, или через один вид оплаты, и плюс минус это всё будет лаконично связано с друг с другом"

**Original (v2 synthesis):** "DACH-locked в Phase 1-2; cross-border patterns documented as Phase 3 expansion option, НЕ committed"

**Ruslan modification 2026-04-19:**

| Dimension | Ruslan decision |
|-----------|-----------------|
| Primary market | DACH (confirmed) |
| Secondary market | US clients + Russian-speaking clients |
| Timing | С Day 1, не Phase 3 expansion |
| Infrastructure | Unified funnel / unified payment / лаконично связано |
| Legal entity | Freiberufler → UG → GmbH trajectory (DACH-based) |

**CRITICAL CHANGES vs synthesis:**

1. **Rejection R10 (multi-currency scaffolding Phase 1) — needs revisit.** v2 synthesis отверг multi-currency scaffolding с аргументом "EUR-only Phase 1 достаточно, добавим при 1st non-EUR клиенте". Если Ruslan планирует US-клиентов с Day 1 — trigger срабатывает сразу. Решение: light multi-currency readiness включить в D2 (folder structure) и D8 (instructions).

2. **Unified funnel requirement.** Все клиенты (DACH / US / RU) проходят через **одну** воронку и **один** payment flow. Это архитектурное требование — влияет на:
   - `clients/` CRM structure — уметь различать jurisdiction но в одной системе
   - Payment provider choice — must accommodate EUR + USD (RUB — через альтернативу)
   - Contract templates — EN primary + DE localization; RU — nice-to-have
   - Tax handling — как DACH entity обслуживает US client (Reverse charge VAT / W-8BEN-E implications)
   - Legal advisor — проверить с Steuerberater и IP lawyer

3. **Language strategy.** Уже было предложено bilingual frontmatter (policy/ + decisions/ + roles/ в EN). При RU-секции клиентов — возможно добавить trilingual или RU-секцию в outreach-контенте.

**Action items for downstream documents:**
- D1 (Architecture) — зафиксировать "Primary DACH + Secondary US + RU with unified funnel"
- D2 (Folder Structure) — revisit `finance/` для light multi-currency
- D4 (Life-OS vs Jetix) — подумать про RU-speaking network implications
- D8 (Instructions) — include "first non-EUR client onboarding checklist" в Phase 2 trigger list
- OT2 (bilingual frontmatter) — Chunk 4 judgment должен учесть этот modification

#### P7 — Resource Accounting (FINAL formulation 2026-04-19)

**Статус:** ✅ APPROVED с EVOLUTION через обсуждение Chunk 1 (3 итерации).

**Evolution history:**
1. v2 synthesis proposed: Capital + Hours + Attention (+ Phase 3 Ecosystem)
2. Ruslan raised Compute question → добавлен Compute как 4-й ресурс
3. Ruslan raised Attention-vs-Hours question → Attention collapsed to quarterly-level concept, Hours refined to "Deep Hours"

**Финальная формулировка (accepted Вариант C hybrid):**

> Jetix учитывает ресурсы в двух измерениях:
>
> **Tier 1 — Quantitative ledger (daily/monthly tracking):**
> - **Capital** — деньги, runway, commitments
> - **Compute** — machine cognition (tokens, models, thinking-time, cache)
> - **Deep Hours** — focused human cognition (attention-weighted time)
>
> **Tier 2 — Strategic allocation (quarterly-level decisions):**
> - **Attention Budget** — focus-theme квартала, % распределение внимания по направлениям (не ledger-metric, а decision-concept в `decisions/quarterly/`)
>
> **Phase 3 addition:**
> - **Ecosystem Resources** — relational capital (first-class при триггере mega-corp stage)

**Ruslan quotes 2026-04-19:**
- Compute: "заносим в first principles"
- Deep Hours: "мне понравился вариант C; capital + compute + deep hours; attention budget — квартальный уровень"
- Ecosystem: "фаза 3 ecosystem это тоже очень важно, она будет довольно мощной и массивной и она тоже будет приносить довольно много ресурсов"

### P7.1 Deep Hours definition

| Counts as Deep Hour | Does NOT count (shallow, tracked for awareness only) |
|---------------------|-------------------------------------------------------|
| Session с Claude Code (создание нового) | Email triage (→ inbox-processor agent) |
| Стратегическое мышление / планирование | Data entry / form filling |
| Sales conversations (live) | Routine admin |
| Deep learning (Левенчук, книги, деконструкция) | Meetings без decision-making |
| Deep writing (мышление на бумаге) | Social media scroll "ради идей" |
| Architectural work | Чтение новостей |
| Client deliverable creation | Tool configuration (одноразовое) |

**Tracking:** Toggl tag system (`[deep]` / `[shallow]`). Shallow трекается для self-awareness но НЕ идёт в главный счётчик.

**Target range:** 25-30 deep hours/week founder-mode Phase 1. Recalibrate при Phase 2+.

**Natural incentive:** избыток shallow hours = системная ошибка, сигнал делегировать больше AI-агентам.

### P7.2 Compute tracking

`finance/compute-ledger.yaml` — monthly:
- Tokens per model (Opus/Sonnet/Haiku)
- API spend (EUR)
- Cache hit ratio
- Rate limit incidents
- Thinking mode usage

Per-executor `executors/<id>/binding.yaml` fields:
- `model_preference`, `fallback_models`
- `thinking_mode`, `max_tokens_per_session`
- `cache_strategy`, `latency_class`
- `escalation_rules`

### P7.3 Attention Budget (quarterly)

Lives в `decisions/quarterly/YYYY-QN-attention-theme.md`:

```markdown
---
quarter: 2026-Q2
attention_theme: "First €50K revenue from DACH Mittelstand"
---
## Attention allocation
- 60% Sales (outreach, conversations, closings)
- 25% Delivery (first client audit execution)
- 10% Architecture (Jetix OS evolution Phase 2 prep)
- 5% Learning (Левенчук, domain expertise)
```

НЕ ledger-metric, а decision-record. Review при quarterly ritual.

### P7.4 Ecosystem Resources (Phase 3 first-class — но infrastructure prep Phase 1)

**Что входит в Ecosystem Resources:**

| Категория | Что считается | Когда активируется |
|-----------|---------------|-------------------|
| **Advisory relationships** | Anton (ментор, системное мышление), Vladislav (экономист, pricing), Rodion (YouTuber, AI-темы) + future Beirat | Phase 1 informal; Phase 2a formal Beirat (4-6 members); Phase 3 Aufsichtsrat |
| **Community members** | Alliance members (L5 Membrane), Club subscribers, newsletter list | Phase 2a при первом L4 client closed |
| **Partnerships** | Cross-referral partners, co-marketing deals, JV agreements, technology integrations | Phase 2a expand; Phase 3 multiplicative |
| **Brand equity / reputation** | Testimonials, case studies, media mentions, NPS, Net Promoter Score, inbound-vs-outbound lead ratio | Phase 2a начало; Phase 3 dominant |
| **DACH institutional networks** | IHK (Industrie- und Handelskammer), VDMA (Verband Deutscher Maschinen- und Anlagenbau), Bundesverband der Deutschen Industrie, BITKOM | Phase 2 (first clients дают access); Phase 3 institutional presence |
| **Alumni / reference network** | Former clients giving references, introductions, testimonials | Phase 2a при 5+ clients delivered |
| **Media / content relationships** | Journalists, podcast hosts, YouTubers (Rodion уже есть), LinkedIn influencer network, newsletter cross-promotion | Phase 2+ growth |
| **Talent network** | Fractional experts, future hire candidates, AI agent community, open-source contributor relationships | Phase 2b при scaling team |
| **Capital relationships** | Angels, VCs, banks, Steuerberater network, grant/subsidy programs (KfW, EXIST) | Phase 2b pre-Series-A; Phase 3 institutional |
| **Academic / research** | TU Berlin, TU München, Fraunhofer Institutes, academic advisory | Phase 3 если relevant to Jetix product |
| **Regulatory / government** | BaFin (finance), Bundeskartellamt (competition), EU AI Act regulators, state-level (Berlin Senat) | Phase 3 institutional presence |

**Как измеряется (примеры metrics Phase 3):**
- Advisory: quarterly consult sessions count, decisions influenced by advisors
- Community: active members, engagement rate, user-generated testimonials
- Partnerships: joint pipeline €, cross-referrals count, co-marketing reach
- Brand: inbound lead % vs outbound, NPS, unprompted mentions
- DACH networks: speaking invitations, referral introductions, industry report inclusions
- Alumni: reference calls requested, LinkedIn recommendations, case study participation

**Почему это first-class resource в mega-corp stage:**
- Network effects: 1 strong advisor может открыть 10 клиентов
- Brand equity: снижает CAC (customer acquisition cost) радикально vs cold outbound
- Partnerships: multiplicative, не аддитивные (1+1=10)
- Institutional access: unlocks enterprise deals которые cold outreach не закрывает

**Phase 1 infrastructure prep:**
- `governance/advisory-board/members.yaml` (Anton/Vladislav/Rodion formalized informally)
- `decisions/policy/ecosystem-strategy.md` (placeholder — how we'll invest in ecosystem when triggered)
- Schema ready для Phase 3 activation

### P7.5 Implications

**D2 (Folder Structure):**
- `finance/resource-ledger.yaml` — tri-resource monthly tracking (Capital, Compute, Deep Hours)
- `finance/compute-ledger.yaml` — detailed compute breakdown
- `decisions/quarterly/YYYY-QN-attention-theme.md` — attention budget records
- `governance/advisory-board/` — Ecosystem infrastructure Phase 1 stub
- `decisions/policy/ecosystem-strategy.md` — Phase 3 placeholder

**D3 (Role Manifests):**
- `executors/<id>/binding.yaml` получает compute contract fields

**D8 (Instructions / weekly rituals):**
- Weekly review проходка по 3 ресурсам (Capital, Compute, Deep Hours) + attention-theme check
- Monthly resource ledger commit
- Quarterly attention-theme setting ceremony

**Placement:** этот принцип входит в foundation основные (Ruslan quote: "будет ложиться в foundation основные").

### 1.3 Three additional principles (Part 1.4) — implicit APPROVED

Через общее принятие frame эти три принципа также APPROVED:
- **Место-слот, не содержание** — архитектура описывает слои готовые принять наполнение
- **Org chart в Git, не в HR** — организационная структура reviewable через PR
- **ШСМ 5 примитивов ontologically-correct** — past-participle, alpha-NOT-work-product, agents-NOT-strategize, mereology-acknowledged

---

## 🔄 Open changes to propagate upstream

Эти изменения от Ruslan'а в Chunk 1 влияют на последующие чанки — при прохождении учитывать:

### Change 1: MC4 (bus-factor) — trustee identity open

- **Was (synthesis v2):** "Designated trustee = Anton. Documented в `governance/trustee-designations.md`."
- **Is (Ruslan 2026-04-19):** "Trustee ≠ Anton. Identity TBD. Bus-factor mitigation ACCEPTED but Day 1 priority DEFERRED."
- **Affects:** MC4 (Chunk 2), `ops/hit-by-bus.md` draft, Constitution §11, `governance/` structure (D2)

### Change 2: OT1 (Strategic-management) — RESOLVED EARLY

- **Was (Chunk 4 tension):** "5 sub-roles Левенчук-correct vs monolithic founder-mode"
- **Is (Ruslan 2026-04-19):** "Accept hybrid: 5 manifests + ruslan multi-role-binding. Manifests пишем."
- **Affects:** Chunk 4 outstanding tensions reduced 5 → 4; D3 (Role Manifests) explicitly pre-approved для 5 atomic sub-roles.

### Change 3: P6 (DACH) — PARTIAL MODIFICATION (+ US + RU)

- **Was (synthesis v2):** "DACH-locked Phase 1-2; cross-border = Phase 3"
- **Is (Ruslan 2026-04-19):** "Primary DACH + Secondary US + RU with unified funnel/payment"
- **Affects:**
  - R10 rejection (multi-currency scaffolding) — needs revisit в Chunk 3
  - OT2 (bilingual frontmatter) — Chunk 4 judgment should account for RU
  - D1, D2, D4, D8 content

---

## Chunk 3 — Accepted 38 / Rejected 12

### Step 1 — Accepted items judgment

**Items 1-5 CONFIRMED 2026-04-19:**
- #25 Tools 14 → 5 + Healthchecks.io ✅
- #27 Rollout 14-day → 7+7 split (sales 1-7, foundation 8-14) ✅
- #26 Manual eval Phase 1 + Langfuse cloud free tier ✅
- #23 Single event log Phase 1 (drop per-alpha history.jsonl) ✅
- #19 Per-agent memory 5 → 3 layers ✅

### Step 2 — R10 Multi-currency REVISIT ✅ RESOLVED 2026-04-19

**Context:** v2 synthesis отверг multi-currency scaffolding Phase 1 (Rejection R10). Ruslan P6 modification (+US +RU с Day 1) переворачивает основание rejection — trigger «1st non-EUR client» срабатывает.

**Ruslan decision — Payment-processor pattern (не internal multi-currency):**

| Question | Decision |
|----------|----------|
| **Q1 Currency handling** | **Option C** — currency-agnostic payment processor (Stripe / Wise) handles all conversion externally |
| **Q2 Scaffolding** | Minimum Mega-Corp P3 placeholder: `finance/currencies.yaml` (1h setup) — держим место |
| **Q3 Tax implications** | **Defer** — «это на потом, глубже разбираться» (Steuerberater consultation later) |
| **Q4 Legal entity multi-currency** | **Defer** — «оставим место под это, потом глубже» |

**Ruslan quote:** "Мы пока тут систему для финансов не делаем, всё будет через Stripe."

**Architectural implication:**
- External: Stripe/Wise as single source of truth для currency conversion + invoicing + tax handling
- Internal: минимальный `finance/` Phase 1 — ledger.md (EUR reported) + invoices YAML + placeholder `currencies.yaml`
- No internal multi-currency bookkeeping до Phase 2a
- When Phase 2a triggers (Steuerberater escalation или DPA client requires audit trail) → real multi-currency scaffolding

**Partial R10 reversal:** technically rejection confirmed (no internal multi-currency scaffolding Phase 1), но practical pathway created (Stripe routes around внутреннюю complexity).

**Action items Phase 1:**
- Stripe / Wise account setup (external)
- `finance/currencies.yaml` placeholder (1h)
- Invoice template parameterizable on currency (Stripe handles format)
- **НЕ делаем:** internal ledger.md multi-currency columns, FX rate tracking, tax calculations

---

### Step 1 Items 8-10 ✅ APPROVED 2026-04-19

**Item 8 — Pre-commit hooks — Вариант B (3 + past-participle check):**
- Hook 1: Asymmetric reference check (Jetix → Life-OS blocked)
- Hook 2: Rechnungsnummer sequential monotonicity
- Hook 3: Role-manifest required-fields lint
- **Hook 4: Past-participle state check** (block commit если state.yaml имеет gerunds) — +1h для regex check по state files

**Item 9 — Cost model section — Вариант B (+per-direction breakdown):**
- `docs/INSTRUCTIONS.md` Section 8.3 «Phase 1 Run Rate»
- Компоненты: API spend / Hetzner / Backblaze / domain / Langfuse cloud free = ~€150-350/mo Phase 1
- Break-even: First Audit SKU €2000 = 6-13 мес covered
- **Per-direction compute allocation** breakdown (ai-consulting vs shaurma research vs ...) для portfolio visibility
- Monthly review: actual vs estimate; trigger >€500/mo → Anthropic volume tier

**Item 10 — Constitution §11 Succession protocol — Вариант A (Day 1 с TBD placeholder):**
- §11.1 unavailable >7d → automated client template
- §11.2 unavailable >14d → trustee notification (trustee: TBD, NOT Anton per Chunk 1)
- §11.3 unavailable >30d → trustee formal authority (limited scope)
- §11.4 return: debrief + authority transfer back
- 30 мин Day 1 для написания текста; trustee name filled позже
- Consistent с MC4 deferred (text создаётся, execution artifacts отложены)

---

### Step 1 Item 7 — Career Ladder dual system ✅ APPROVED 2026-04-19

**Accepted полностью без modifications.**

- **J0-JX Reference Framework** в D7 (hiring + compensation + promotion criteria)
- **Phase 1 Operational levels:** J-Auto / J-Approve / J-Strategic
- **5-line decision_rights list** per role (не 13×6 matrix)
- Promotion process: meta-agent compiles evidence → decisions/promotions/ → Ruslan approves
- **Direction authority** (из Item 6 portfolio model):
  - Open hypothesis direction: J-Auto (strategy-support-analyst agent может propose)
  - Activate direction: J-Strategic (Ruslan only)
  - Archive direction: J-Strategic (Ruslan only, с post-mortem)

**Agent `strategy-support-analyst` reference level:** J3 (downgraded от J4 per Левенчук §1.4 — agents не стратегируют).

---

### Step 1 Item 6 — Wiki + Portfolio Directions [MAJOR DECISION] ✅ APPROVED 2026-04-19

**Two intertwined decisions locked:**

#### Decision 6.1 — Physical separation Life-OS ≠ Jetix (Вариант A)

**Status:** ACCEPTED с Day 1 as architectural principle.

**Ruslan directive:**
> "Life-OS и Jetix должны быть принципиально вообще разделены, никак не коим образом не смешиваться. Ничего с Life-OS не должно попадать в Jetix. В Jetix только суть бизнес и всё что важно для процветания компании. Потом физически разделим на разных серверах."

**Implementation:**
- `life-os/wiki/` — PERSONAL (reflections, relationships, book-notes, health, personal-concepts)
- `life-os/projects/jetix/wiki/` — JETIX (business-only cross-cutting knowledge)
- **Asymmetric reference rule** (per R7): Jetix НЕ может ссылаться в Life-OS; Life-OS может ссылаться в Jetix.
- Pre-commit hook enforces separation.
- Phase 2+ trigger: `git filter-repo --path life-os/` → extract Life-OS в отдельный repo.
- Phase 3+ trigger: physical separation на разные servers.

**Migration plan:**
- Structure подготавливается в D1/D2.
- Claude Code task: классифицировать existing 568 wiki files → распихать по life-os/ vs jetix/.
- Outcome: clean separation по всему repo.

#### Decision 6.2 — Jetix as Portfolio of Directions (Hybrid 1+4) 🏢

**Status:** ACCEPTED — maximum depth implementation.

**Ruslan vision:**
> "Jetix = большая корпорация, десятки направлений. Шаурмечные, кибербезопасность, AI-tools, и т.д. Гипотезы, эксперименты, всё должно где-то храниться. Википедия должна работать с людьми, с CRM, cross-functional. Jetix как **холдинг для кросс-функционального наблюдения**."

**Model:** Hybrid Variant 1 (folder per direction) + Variant 4 (Direction как 8-й true alpha).

**Implication:** **7 true alphas → 8 true alphas** (adding Direction).

#### Full Structure — `life-os/projects/jetix/`

```
life-os/projects/jetix/
│
├── directions/                          ⭐ PORTFOLIO LAYER
│   ├── _active/
│   │   └── ai-consulting-dach/          (primary Q2 revenue bet)
│   │       ├── direction.md             (thesis, ICP, economics, conviction)
│   │       ├── hypotheses/              (testable hypotheses within direction)
│   │       │   ├── h-001-<slug>.md
│   │       │   └── ...
│   │       ├── experiments/             (planned + running experiments)
│   │       │   ├── e-001-<slug>.md      (status, design, results)
│   │       │   └── ...
│   │       ├── research/                (direction-specific research)
│   │       │   └── ...
│   │       ├── pipeline.md              (active deals/prospects in this direction)
│   │       └── state.yaml               (past-participle state machine)
│   │
│   ├── _hypotheses/                     (directions under validation)
│   │   ├── shaurma-chains-automation/   (example hypothesis direction)
│   │   ├── cybersecurity-dach-mittelstand/
│   │   └── <others>/
│   │
│   ├── _archived/                       (dropped directions с post-mortem)
│   │
│   └── README.md                        (portfolio dashboard — all directions + status)
│
├── alphas/                              ⭐ OPERATIONAL STATE MACHINES (8 true alphas)
│   ├── client/                          (1) all clients with direction frontmatter
│   ├── project/                         (2) active projects
│   ├── deal/                            (3) active negotiations
│   ├── content-item/                    (4) content pieces
│   ├── hypothesis/                      (5) hypotheses с state machines
│   │   └── instances/                   (symlinks в directions/*/hypotheses/)
│   ├── member/                          (6) Alliance members
│   ├── way-of-working/                  (7) Jetix methodology evolution
│   └── direction/                       (8) ⭐ NEW 8th alpha
│       ├── states.yaml                  (lifecycle past-participle)
│       │   # hypothesized → under-validation → validated → activated →
│       │   # scaled → plateaued | invalidated | dropped | archived
│       └── instances/                   (symlinks в directions/*/state.yaml)
│
├── wiki/                                ⭐ CROSS-CUTTING KNOWLEDGE
│   ├── concepts/                        (reusable across directions)
│   ├── entities/                        (companies, people, tools — cross-direction)
│   ├── sources/                         (research — tagged с directions relevant)
│   ├── topics/
│   ├── claims/
│   ├── experiments/                     (cross-direction experimental insights)
│   ├── summaries/
│   ├── foundations/                     (FPF-Lite, Constitution, creation-graph)
│   ├── graph/
│   │   └── edges.jsonl                  (typed edges: related/supports/contradicts
│   │                                     + belongs-to-direction / sames-as-crm /
│   │                                     applies-to-direction)
│   ├── index.md                         (catalog)
│   └── log.md                           (append-only chronology)
│
├── clients/                             ⭐ CRM (frontmatter references direction)
│   └── companies/
│       └── <slug>.md                    (frontmatter: direction: <slug>; alpha_ref; wiki_ref)
│
├── decisions/                           (cross-direction + per-direction)
├── governance/                          (advisory board, etc.)
├── ops/                                 (deferred — bus factor)
├── entities/jetix-gmbh/                 (federation stub)
├── finance/
├── evals/
├── agents/
└── docs/
```

#### Graph edges (typed)

Phase 1 edges (3 Simplifier baseline + 3 portfolio-specific):

**Cross-cutting (Simplifier Phase 1 baseline):**
- `related` — generic connection
- `supports` — evidence/argument supports claim
- `contradicts` — evidence against claim

**Portfolio-specific (NEW for Hybrid 1+4):**
- `belongs-to-direction` — file belongs to specific direction's scope
- `applies-to-direction` — concept/entity applies to multiple directions
- `sames-as-crm` — wiki entity ↔ CRM entry cross-ref

**Phase 2+ triggered additions:** part-of, instance-of, causes, etc. (при growth wiki content)

#### Frontmatter convention (critical for graph)

Каждый file в `wiki/` или `clients/` имеет:

```yaml
---
type: concept | entity | source | claim | ...
scope: jetix                           # жёстко после separation (no Life-OS here)
direction: ai-consulting-dach          # single direction scope
# OR
directions: [ai-consulting-dach, shaurma-chains]  # applies to multiple
crm_ref: clients/companies/<slug>.md   # if entity has CRM counterpart
alpha_ref: alphas/<alpha>/instances/<slug>.yaml  # if has operational state
---
```

#### Wiki simplifications (Simplifier accept с modification)

- ✅ **Niches 6 → 0 PERSONAL niches** (personal/business/sales/life/tech/meta dropped) — **НО** portfolio replaced через `directions/` top-level (richer abstraction)
- ✅ **Edges 9 → 6** (3 baseline + 3 portfolio-specific, не 3 как Simplifier predложил)
- ✅ **Skills 5 → 2** (`/ingest`, `/ask`) — `/lint`, `/consolidate`, `/build-graph` triggered at 500+ orphans

#### Use case example — CRM ↔ Wiki ↔ Direction graph

Scenario: Müller GmbH prospect в ai-consulting-dach direction.

- `clients/companies/muller-gmbh.md` (CRM: operational state, contacts, deal state)
- `wiki/entities/muller-gmbh.md` (Knowledge: background, research, decision-makers)
- `directions/_active/ai-consulting-dach/pipeline.md` (portfolio context: где в sales cycle)
- `alphas/client/instances/muller-gmbh.yaml` (state machine: qualified → in-negotiation → ...)

Query `/ask "что знаю про Müller"` → agent traverses graph:
CRM → wiki entity → related research → direction context → operational state → synthesis.

#### Phase evolution

- **Phase 1 Day 1:** `directions/_active/ai-consulting-dach/` created (minimum). Other directions added как возникают hypotheses.
- **Phase 1 rolling:** каждая новая idea от Ruslan → new `directions/_hypotheses/<slug>/` folder с direction.md (thesis + kill criteria)
- **Phase 2a:** validated directions → `_active/`, invalidated → `_archived/` с post-mortem
- **Phase 2b+:** multiple active directions одновременно, cross-functional learning через wiki/concepts/

#### Cross-references к другим principles

- **P4 Model D Nested** — this confirms and deepens: Jetix nested portfolio внутри Life-OS
- **P7 Attention Budget (quarterly)** — attention allocation per direction (50% ai-consulting, 25% shaurma research, ...)
- **P7 Capital** — budget allocation per direction
- **MC3 3-level mereological graph** — Direction = Level 3 supersystem containing hypothesis/experiment creation systems
- **Mega-Corp Holdings thinking** — теперь аккуратно моделируется portfolio layer

**Outcome:** wiki/ работает максимально глубоко как portfolio engine + cross-functional observation tool. Ruslan quote: "это тоже очень важно будет".

---

## Chunk 2 — Meta-conflicts resolved

### MC5: Mega-Corp vs Simplifier — Federation pattern ✅ APPROVED 2026-04-19

**Status:** v2 resolution accepted (already implicit через MC1 9 P1 additions).

- Phase 1: `entities/jetix-gmbh/` namespace stub (4h) — empty skeleton mirroring current `jetix/`
- `jetix/` paths активны, stub inactive
- Activation trigger: 2nd entity emergence (Phase 2c acquisition или Holdings split)

### MC6: Левенчук strict past-participle vs AI-readability ✅ APPROVED 2026-04-19

**Status:** Strict-enforce past-participle accepted (already implicit через Chunk 1 P3).

- Systematic rename: 52% v1 violations fixed
- Trade-off accepted: 1-2 weeks reading-discomfort → permanent semantic clarity
- Applied to: all `alphas/` state machines, all role-manifests, all decision records

---

### MC4: Critic vs Simplifier — Bus-factor mitigation ⏳ ACKNOWLEDGED, DEFERRED 2026-04-19

**Status:** v2 structure acknowledged. Phase 1 execution deferred — не priority сейчас.

**Ruslan directive 2026-04-19:**
> "На данный момент это не сильно уж важная штука. Что-то там зафиксируй, что v2 предлагал. На это мы пока время тратить не будем. Просто учитываем в архитектуре, что у нас будет какой-то ответственный человек на внезапные ситуации. Но пока не критично."

**v2 structure acknowledged (будет готов к execution когда time comes):**
- `ops/hit-by-bus.md` (~2h) — 1-page operational guide с 1Password vault, contacts, open commitments
- Constitution §11 Service Continuity protocol (unavailable >7d / >14d / >30d escalations)
- `ops/business-continuity.md` — scenarios 1 week / 1 month / permanent
- `ops/incident-playbook.md` — generic incident response
- `governance/trustee-designations.md` — с placeholder `{trustee: TBD, NOT Anton}`
- Phase 2 trigger: dead-man's-switch script при first retainer client
- Phase 2b trigger: Chief of Staff formal role

**Ruslan overrides из Chunk 1 preserved:**
- Trustee ≠ Anton (identity TBD)
- Timing: Phase 1 но не Day 1 priority — execution «чуть потом»

**Implicit trigger (моя рекомендация):** complete bus-factor artifacts **до first client contract signed** — это hard deadline после которого risk становится non-theoretical.

**Outcome:** v2 structure будет materialized когда Ruslan решит (либо до first contract, либо позже). Сейчас — acknowledged, не executed. Architectural seams preserved для painless future add.

---

### MC3: Левенчук vs Pragmatic — Onto purity vs Tooling ✅ APPROVED + 1 OVERRIDE 2026-04-19

**Status:** v2 accept 13 из 15 Левенчук changes полностью; 1 preservation confirmed; **1 OVERRIDE на full mereological graph**.

**Ruslan decisions:**

1. **Member preserved as alpha** ✅ (v2 rejection of Левенчук drop confirmed)
   - Ruslan quote: "Member — это альфа, да, мы это оставляем. Фиксируем, что member будет у нас альфой."
   - `alphas/member/` Phase 1 schema + empty instances; активация при 1st L4 client → Founding Alliance Member

2. **3-level mereological creation graph — FULL Phase 1** ⚠️ **OVERRIDE v2 partial deferral**
   - Ruslan quote: "Три уровня mereological важно, обязательно мы делаем все три уровня максимально глубоко, как говорит Левенчук. Качественно, удобно, глубоко. Мы это полностью принимаем от него. Никаких упрощений."
   - **CHANGE vs synthesis:** v2 accepted Lite version Phase 1 + Full Phase 2. Ruslan overrides → **Full 3-level Phase 1**.
   - **Cost Phase 1:** +4-8h ontology work (встроено в D6 writing)
   - **Deliverable:** `jetix-creation-graph.md` (separate artifact в D6) с 3-level structure:
     - **Level 1 Target systems:** client-relationship, deal-opportunity, product-SKU, content-item, member-engagement, hypothesis, way-of-working
     - **Level 2 Creation systems:** роли (все 5 Ruslan sub-roles + 12 agent roles), методологии, processes
     - **Level 3 Supersystems:** Jetix-Sales-Function, Jetix-Revenue-Engine, Jetix-Delivery-Function, Jetix-Ecosystem (Phase 3 hooks)
     - **Mereological relationships:** part-of / creates / operates-in / methodologically-uses / constrained-by
   - **Implication:** D6 (JETIX-FPF-LITE) получает expanded section. Meta-agent reference this graph для onboarding новых agents/humans.

3. **Остальные 13 Левенчук changes** — все ACCEPTED:
   - Alpha/WP split (10→7+3+1), past-participle strict, role/executor separation, 5 sub-roles, forbid dynamic assignment, production_dependencies rename, strategist rename, «What ШСМ is NOT», lightweight mereology, 25K exocortex reservation, agent_onboarding field, reasoning_examples field, U-Types 4→6, strategizing as event

**Outcome:** v2 accept + 1 override в strengthening direction (больше Левенчук, не меньше).

---

### MC1: Critic vs Mega-Corp — Scaffolding vs Execution ✅ APPROVED 2026-04-19

**Status:** v2 resolution принято полностью.

**Ruslan quote 2026-04-19:**
> "То что у нас Version 2 предложил, мы в итоге для начала его и примем. То что там надо было, всё что там надо мы построим уже с первого дня адекватно. Остальное просто оставим на потом, все чертежи. Фиксируем версию 2."

**Accepted resolution:**

- **Reference vs Operational Architecture split** — already approved Chunk 1
- **9 Mega-Corp P1 additions** accepted в Phase 1 (~28h scaffolding):
  1. `entities/jetix-gmbh/` namespace stub (4h)
  2. `roles/l1-foundation/dpo/role.md` external-executor mode (2h)
  3. `governance/` + `advisory-board/members.yaml` (Anton/Vladislav/Rodion) (2h)
  4. `ops/` crisis playbooks full stack (incident / hit-by-bus / continuity / disaster-recovery / gdpr-art-33) (6h)
  5. Bilingual frontmatter convention в policy/decisions/roles (2h)
  6. Strategic-management 5 sub-roles decomposition (4h) — already confirmed
  7. Customer Success J2 role-manifest stub (2h)
  8. Compensation matrix `policy/compensation.md` (4h)
  9. EU AI Act compliance calendar `policy/eu-ai-act.md` (2h)

- **5 Mega-Corp P2 items DEFERRED Phase 2a:**
  - Org-chart visualization pipeline
  - Auto-generated org-index.yaml
  - Acquisition playbook stub
  - Onboarding content week-by-week
  - Performance review framework

- **3 Mega-Corp P3 items REJECTED:**
  - FPF-Steward sub-role (meta-agent sufficient Phase 1)
  - IPO readiness placeholder (premature)
  - ⚠️ **Multi-currency scaffolding** — formally rejected by v2 BUT Ruslan P6 modification (+ US + RU с Day 1) triggers revisit в Chunk 3 (R10)

- **Federation pattern:** stub only (`entities/jetix-gmbh/` 4h), NOT full Day 1 pattern

- **3 Strategic concerns addressed:**
  - C1 Centralization choke-point — via 5 sub-roles decomposition + Chief of Staff reserved Phase 2a
  - C2 Federation — via entities/ stub
  - C3 Bus factor — via ops/ stack + Constitution §11 + trustee (**trustee TBD per Ruslan override, not Anton**)

**Ruslan directive:** "по этому вопросу всё понятно, фиксируем версию 2, больше смотреть не буду".

---

## ⏳ Chunks 2-7 — PENDING

- [ ] **Chunk 2** — 6 Meta-conflicts resolved (MC1-MC6) — review resolutions, особенно MC4 с trustee change
- [ ] **Chunk 3** — Accepted 38 / Rejected 12 changes — особенно R10 (multi-currency) revisit
- [ ] **Chunk 4** — Outstanding Tensions (было 5, теперь 4 — OT1 resolved early)
  - OT2 Bilingual frontmatter
  - OT3 EU AI Act tier
  - OT4 Trademark Jetix vs Disney
  - OT5 FPF-Lite token-budget + publishing
- [ ] **Chunk 5** — Part 2 Areas 1-5 (D1-D5 detailization)
- [ ] **Chunk 6** — Part 2 Areas 6-9 (D6-D9 detailization)
- [ ] **Chunk 7** — Part 6 Final sign-off checklist + Part 5 Roadmap

После Chunk 7 → ADR финализуется (status: approved) → Stage 4 unblocks → D1-D9 writing start.
