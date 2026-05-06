---
id: ADR-2026-04-19-architecture-v2-approval
title: Architecture Synthesis v2 — Ruslan Approval Record
date: 2026-04-19
date-closed: 2026-04-20 (Chunk 7) + 2026-04-20 (Chunk 8 — same day)
status: APPROVED
phase: Stage 3 + 3.6 COMPLETE — Gap Analysis review finished 2026-04-20
chunks-complete: [1, 2, 3, 4, 5, 6, 7, 8]
chunks-pending: []
unblocks: Stage 4 (D1-D8 writing) + D6 JETIX-FPF writing
type: architecture-decision
author: ruslan
scribe: claude-opus-4-7
source: raw/research/architecture-synthesis-v2-final.md
status: archived
archived_at: 2026-05-06
archived_reason: Stage-3 chunk tracker — historical decision journal
moved_by: canonical-cleanup-2026-05-06 (Ruslan walkthrough ack via CANONICAL-WALKTHROUGH-2026-05-06.md)
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

## Chunk 5 — Part 2 Areas 1-5 (D1-D5 details)

## Chunk 7 — Final Sign-off ✅ APPROVED 2026-04-20

**Status:** Stage 3 review COMPLETE. ADR closed. Ready for Stage 3.5 (D9 draft) и Stage 4 (D1-D8 writing).

**Ruslan final directive:** "в целом okey, я всё подтверждаю на данный момент. Можем этот этап проверки закрывать, менять статус".

**Part 5 Implementation Roadmap Preview:** accepted implicit через Chunks 1-6.

**Part 6 Final Sign-Off Checklist:** all pending items resolved через Chunks 1-6.

**ADR status change:** `in-progress` → `APPROVED`.

**Next steps (Stage 3.5+):**
- Stage 3.5: write `decisions/2026-04-20-jetix-architecture-final-DRAFT.md` (clean D9 v0.5 consolidation)
- Stage 4: write D1-D8 using D9 draft as source of truth
- Stage 4.5: finalize D9 (draft→committed)

Дальнейший roadmap + план work будет обсуждён отдельным разговором.

---

## Chunk 6 — Part 2 Areas 6-9 (D6-D9 details)

### Area 9 → D9 Final Decision Record ✅ APPROVED 2026-04-20 — **3-stage process**

**Ruslan decision: Option C — 3-stage evolution.**

**Stage 3.5 (next action after Chunk 7):**
- **Action:** Claude Code writes `decisions/2026-04-20-jetix-architecture-final-DRAFT.md`
- **Purpose:** clean consolidation всех decisions из messy approval ADR + 11 overrides
- **Size:** 10-15 pages
- **Format:** T-02 Oxide RFD template
- **State tag:** `draft`
- **Content:** 8 principles + Reference/Operational split + 15 folders + 8 alphas + 18 role-manifests list + 7+7 rollout + cost model + overrides table (v1 → v2 → v2-Ruslan-approved)
- **Purpose:** single source of truth для Stage 4 writers (не весь 30+ page messy ADR)

**Stage 4 (D1-D8 writing):**
- Claude Code пишет D1-D8 используя D9 draft как authoritative input
- Каждый D references D9 draft как source
- 8 documents total (D1-D8)

**Stage 4.5 (after D1-D8):**
- Review D9 draft
- Update если actual writing diverged от draft
- State change: `draft` → `committed`
- Rename: `DRAFT` removed → `decisions/2026-04-20-jetix-architecture-final.md`
- Final approved architecture

**Rationale:**
- Clean reference для Stage 4 writers (avoid forcing writers через messy 30+ page history)
- Incremental refinement — draft evolves to final based on реальный writing experience
- Matches Ruslan's stated flow "consolidate → write → finalize"

**Accept all formatting defaults:**
- Size 10-15 pages ✓
- State tag draft→committed ✓
- 3-column diff table (v1/v2/v2-Ruslan) ✓
- Write post-D1-D8 for final ✓

---

### Area 8 → D8 docs/INSTRUCTIONS ✅ APPROVED 2026-04-20

**Ruslan directive:** "Главное план фиксировать, чтобы потом по нему адекватно идти и трекать что сделано. Всё остальное добавим по ходу."

**7+7 day rollout accepted + realistic tolerance:**

**Days 1-7 Sales Infrastructure:**
- Day 1: jetix.de domain + git init + directions/_active/ai-consulting-dach/ init
- Day 2: First SKU + 4 pre-commit hooks (asymmetric ref / Rechnungsnummer / role-manifest / past-participle)
- Day 3: Cold outreach list 50 Mittelstand (IHK directory + Perplexity research)
- Day 4: Discovery call template (DE+EN) + Cal.com booking
- Day 5: Proposal template + Audit SKU pricing
- Day 6: Contract + invoice template + Stripe account setup
- Day 7: Steuerberater intake + first hypothesis direction stub

**Days 8-14+ Foundation (realistic 7+10-12 timeline):**
- Day 8: SOPS+age + Life-OS ≠ Jetix folder separation
- Day 9 (may extend to 9a+9b): 18 role.md migration full depth + 18 executor-bindings
- Day 10: First golden dataset sales-lead + 5-й auto-translation hook
- Day 11: Diátaxis 2-form docs + D6 FPF first-pass (parallel track может extend)
- Day 12: First RFD + Constitution §11 с TBD trustee placeholder
- Day 13: ops/ artifacts text (hit-by-bus + continuity + incident-playbook + disaster-recovery + gdpr-art-33) с TBD trustee
- Day 14: Backup restic → Backblaze B2 + Healthchecks.io

**Parallel tracks:**
- D6 FPF full writing (30-50 pages, 3 passes) — parallel к Foundation Days 10-14+
- Migration script existing 568 wiki files (Life-OS vs Jetix classification) — post-Day 14
- First attention-theme setup — Day 14
- Per-agent compute contract activation — Day 9

**Tool stack Phase 1 (5 tools + Claude Code + git):**
- git + GitHub
- Claude Code
- SOPS + age (1 key)
- restic → Backblaze B2
- Healthchecks.io free tier
- + Stripe (payment)
- + Toggl (Deep Hours tracking per P7)
- + Perplexity (research)

**Cost model Phase 1 Run Rate:**
- Total monthly: €275-737
- 12-month run rate: €3,300-8,850
- Break-even: 1st Audit SKU €5K = 7-18 months covered
- Per-direction compute breakdown (per Item 9 Variant B): ai-consulting ~70-80%, hypotheses ~15-20%, meta ~10-15%

**4 rituals cadence:**
- Daily morning (30 min): inbox + pipeline + intent
- Weekly Friday (60 min): Shape Up + commits + close-week
- Monthly last Friday (2h): P&L + OKR + founder note + meta-review
- Quarterly (1 day): letter + OKR-next + role-manifest delta + strategy

**Strategizing:** trigger-driven event, НЕ ceremony.

**Ruslan's stance:** plan-as-tracker primary purpose. Additional items can be added по ходу rollout без formal review.

---

### Area 7 → D7 JETIX-CAREER-LEVELS ✅ APPROVED 2026-04-20

**Preserved decisions** (уже fixed через Chunks 1-4):
- Dual system J0-JX reference + Phase 1 3 operational (J-Auto / J-Approve / J-Strategic) — Item 7
- 5 Ruslan atomic sub-roles — Chunk 1 P5
- strategy-support-analyst rename + J3 mapping — Chunk 1 P5
- Customer Success J2 stub (Phase 2a trigger) — MC1
- DPO role external-mode — MC1
- Compensation matrix — MC1
- EU AI Act calendar — OT3
- Triple-AND Phase 2a trigger — Area 4

**New decisions:**

1. **AI promotion mechanism:** external review (meta-agent compiles evidence) + Ruslan sign-off.
   - ❌ 90-day self-graded (v1 original) — rejected
   - ✅ Monthly external audit + human ratification — accepted
   - `decisions/promotions/YYYY-MM-DD-<agent>-J<X>-to-J<Y>.md` format

2. **Strategic client definition:** Phase 1 — "any client likely = strategic" (informal, Phase 1 все clients treated как strategic because each = >5% ARR). Formal criteria (ARR >5% OR ≥3 stakeholders OR referrer) applies Phase 2a+.

3. **C-suite timing:** accept v2 corrections (CFO fractional €1M, FTE €10M; Head of Finance €100-140K; all in €).

4. **Phase transitions timeline:** accept (Phase 2a 2027, 2b 2027-2028, 2c 2028-2030, 3 2030+).

5. **crazy-agent placement — Variant B (Claude decision):** J2 operational (J-Approve) + special "brainstorming mode outside normal ladder" documentation. Evaluation criteria: novelty + cross-domain connection quality (не accuracy). Different promotion signals than other J2 agents.

6. **life-coach placement:** **Life-OS only** — migrates to `life-os/agents/life-coach/`. НЕ part of Jetix career ladder. Consistent с Item 6 physical separation.

7. **Ecosystem Resources governance roles:** DEFERRED discussion. Add при Phase 3 activation trigger.

8. **FPF-Steward as separate role:** APPROVED evolution — currently sub-role в meta-agent (R12). Trigger to separate role: **30+ agents OR 1+ human hire in meta-function OR quarterly audit burden >4h** (whichever fires first — Phase 2b likely).

**Ruslan quote:** "основное всё уже зафиксировали, мы оставляем, не трогаем."

---

### Area 6 → D6 JETIX-FPF ✅ APPROVED 2026-04-20 — **RENAMED from FPF-Lite к FULL FPF, MAXIMUM DEPTH**

**CRITICAL RENAME:** `FPF-Lite` → `FPF` (drop "Lite" качество — документ становится full constitutional).

**Ruslan directive:**
> "Мы к этому документу подходим глубоко. Он не должен быть light — он должен быть constitutional, адекватный, глубокий. Максимально глубоко всё что можно, прописываем по Левенчуку, добавляем, внедряем, делаем, потом ещё один дополнительный прогон. Этот документ очень критически важен. Делаем прям full, мега full, как только возможно, по всем данным которые только есть от Левенчука. Вообще никакого компромисса."

**Implications:**
- **Document rename:** D6 JETIX-FPF-LITE.md → **D6 JETIX-FPF.md** (full framework)
- **Size:** 30-50 pages (vs v2 3-5 pages) — constitutional depth
- **NO EXCLUSIONS** что касается Левенчук — всё что is reasonable applicable → included:
  - ✅ Full 17 trans-disciplines (reference + selected application) — было v2 excluded
  - ✅ Advanced mereology (Kit Fine acknowledgment, holon hierarchy fully documented) — было v2 excluded
  - ✅ Holons recursive (Ruslan-as-executor → role → Jetix → Life-OS) — materialize в spec syntax
  - ✅ Category theory considerations (где applicable — objects, morphisms, functors if useful)
  - ✅ Constructor theory (если reasonable fit — для Creation Graph depth)
  - ✅ Full FPF architectural invariants — applied

**Writing process:**
- **First pass:** all 10 sections + creation graph + exclusions-turned-inclusions
- **Second pass (дополнительный прогон):** deepen each section, verify Левенчук fidelity
- **Third pass validation:** FPF-Steward audit (meta-agent) review against Левенчук source material

**Full 10 sections preserved + expanded:**
1. Target System (full L0-L7 + Model D)
2. Stakeholders (all 11 Ecosystem categories per P7)
3. **Creation Graph** — full 3-level mereological (per MC3)
4. Client Principles
5. **Internal Principles** — 8 (включая agents-as-master-class)
6. **8 True Alphas** (Client/Project/Deal/Content/Hypothesis/Member/WayOfWorking/**Direction**) с states past-participle
7. Ritual Cadence (4 rituals/quarter + strategizing event-not-ceremony)
8. **U-Types Full** — expand от 6 (Lite) до full set (Левенчук max: System/Role/Method/Stakeholder/Objective/Decision/Practice/Case/Knowledge/Artifact/... всё что применимо)
9. What ШСМ is NOT (expanded protection section)
10. **Mereology** — full (не "lightweight" — holons recursive fully documented)
11. **NEW: 17 trans-disciplines reference** (which apply, which referenced)
12. **NEW: Full FPF architectural invariants**
13. **NEW: Constructor/Category theory applications** (где relevant)

Plus separate artifacts:
- `wiki/foundations/jetix-creation-graph.md` (full 3-level mereological graph, 4-8 pages)
- `wiki/foundations/shsm-primitives.md` (5 primitives deep reference)
- `wiki/foundations/holon-hierarchy.md` (Jetix holon structure full)

**Loading:** full text в каждый agent system.md (OT5 Scenario A — full everywhere). Context budget 25K exocortex hard reservation handles.

**Publishing:** internal only Phase 1+ (OT5 — secret sauce protected).

**Evolution rules:**
- Major changes (ontological shifts) → RFD approved by Ruslan
- Minor clarifications → FPF-Steward quarterly audit + Ruslan approve
- Breaking changes → Constitution-level amendment with wide reflection

**Cost Phase 1:**
- D6 FPF writing: ~15-25h (3 passes)
- Creation graph artifact: 4-8h
- Supplementary artifacts (holon hierarchy, ШСМ primitives): 3-6h
- Total: ~25-40h foundational work

**Consistency с previously-decided principles:**
- Full 3-level mereological (MC3 override)
- Full text loading во всех agents (OT5)
- Direction as 8th alpha (Item 6)
- FPF-Steward quarterly audit (R12)
- Past-participle strict (MC6)
- Forbidden dynamic role + founder exception (Chunk 1 P5)

---

### Area 5 → D5 JETIX-KNOWLEDGE-ARCHITECTURE ✅ APPROVED 2026-04-20

**3-layer model:**
- Layer 1 wiki/ (Karpathy LLM Wiki pattern)
- Layer 2 alphas/ (8 true alphas с past-participle state machines)
- Layer 3 per-agent memory (3 layers: system.md + scratchpad + mailbox)

**All previously-decided components confirmed:**
- 9 entity types preserved (concepts/entities/sources/topics/ideas/experiments/claims/summaries/foundations)
- 1 общая wiki/ Phase 1 (не 6 niches — Item 6)
- 6 edges (3 baseline + 3 portfolio: belongs-to-direction / applies-to / sames-as-crm)
- 2 skills /ingest /ask (Item 6)
- 8 true alphas с Direction added (Item 6)
- Past-participle strict (MC6)
- Per-agent memory 3 layers (Item 5)
- 25K exocortex HARD reservation (MC3)
- Single event log Phase 1 (Item 4)

**8 alpha state machines past-participle:**

| # | Alpha | States |
|---|-------|--------|
| 1 | Client | lead-identified → qualified → proposed → in-negotiation → won / lost → churned |
| 2 | Project | scoped → kicked-off → started → delivered → closed → in-follow-up |
| 3 | Deal | drafted → signed → activated → completed / cancelled |
| 4 | Content Item | drafted → in-review → approved → published → retired |
| 5 | Hypothesis | formulated → under-validation → validated / invalidated → implemented |
| 6 | Member | applied → invited → activated → flagged-at-risk → churned |
| 7 | Way of Working | drafted → implemented → refined → deprecated |
| 8 | Direction (NEW) | hypothesized → under-validation → validated → activated → scaled → plateaued / invalidated / dropped → archived |

**Reclassified as NOT alphas:**
- Invoice → work product (clients/invoices/YYYY/)
- SKU → entity (entities/skus/)
- Postmortem → work product (decisions/postmortem/)
- Research Note → work product (wiki/sources/)

**Context loading budget (per call):**
- 25K HARD reservation exocortex (Full FPF 7-10K + role.md 2-3K + alpha states 3-5K + FPF-Steward context 3-5K)
- 25K SOFT (current task + scratchpad + recent decisions + mailbox)
- Total fixed: 50K + 950K flexible (Opus 4.7 1M window)

**German legal compliance:**
- Invoice YAML schema preserved (11 Pflichtangaben § 14 UStG)
- Rechnungsnummer monotonicity hook (Item 8 Hook 2)
- Steuerberater backup contact в ops/hit-by-bus.md
- ZUGFeRD 2.x — **proactive Q3 2026** (Q3 Variant A — before 2027-01 mandatory)

**Decisions:**
- **Q1 Writeback в comparisons/:** Manual (Variant B) — Ruslan approves writeback selectively
- **Q2 GraphRAG trigger:** Latency-based (Variant B) — migrate при >3s p95 retrieval latency, не firm page count
- **Q3 ZUGFeRD timing:** Proactive Q3 2026 (Variant A)

---

### Area 4 → D4 JETIX-VS-LIFE-OS ✅ APPROVED 2026-04-20

**Folder-level separation Day 1:**
- Parallel structure `~/jetix-os/life-os/` + `~/jetix-os/jetix/`
- Разные wiki, разные decisions, разные everything
- Ruslan quote: "разные папки, чтобы мы не запутались и чтобы наш Claude Code тоже не запутался"

**Asymmetric reference rule:** accepted — Jetix files НЕ МОГУТ reference Life-OS paths. Hook 1 (Item 8) enforces Day 1.

**SOPS:** 1 key Phase 1 (no business/personal split). All private, no public sharing. Accept v2 default.

**Phase 2a trigger Triple-AND:** accepted — extraction в отдельный repo когда все 3 условия:
1. ≥€20K MRR × 3 consecutive months
2. Ruslan >40% time на L1/L2 ops (Toggl-tracked)
3. ≥1 active client requesting GDPR DPA

**Phase 3 trigger:** different servers / different clouds (Ruslan explicit).

**Grey zone / Insight sanitization:**
- Dual tracking accepted в principle (Anton pattern: life-os/relationships/ + jetix/governance/advisory-board/)
- Insight sanitization rule accepted (Life-OS → Jetix insights generalized, personal identifiers removed)
- **BUT Phase 1 execution:** informal, manual mode. No strict enforcement. Ruslan quote: "пока тоже будет всё, буду там ручным режимом ещё дописывать, дофиксировать".

**Geschäftskonto:** deferred — не Phase 1 week 1-2 priority. Add когда реально понадобится (Stripe integration активируется или first invoice готовится).

**`shared/` Phase 2 evolution:** accept my recommendation C (move into Jetix, Life-OS references externally).

**3 evolution phases formalized:**
- **Phase 1 (Day 1):** folder-level separation, parallel structure, hook enforcement
- **Phase 2a (Triple-AND trigger):** git filter-repo extraction → life-os и jetix-os separate repos
- **Phase 3+:** different servers / clouds

---

### Area 3 → D3 JETIX-ROLE-MANIFESTS ✅ APPROVED 2026-04-19

**Template:** 5-block role.md (identity / ontological / method / production_dependencies / evolution) + separate `executor-binding.yaml`.

**All additions accepted:**
- Direction authority в Block 5 seniority-lite (per Item 7 + Portfolio model)
- Compute contract в executor-binding.yaml (per P7 override)
- FPF-Steward sub-role в meta-agent (per R12 override)
- EN-primary body в roles/ (per OT2)
- english-summary mandatory в frontmatter
- agent_onboarding (initial_context_pack + warm_up_tasks + calibration_checkpoint)
- reasoning_examples optional field (per Левенчук Part 3)

**Role list Phase 1: 18 full-depth manifests:**

- **5 Ruslan atomic sub-roles:** strategy-lead / framing-lead / sales-closer / acceptance-authority / external-relations (+ `executors/ruslan.yaml` with multi-role-binding flag)
- **11 agent roles:** manager / personal-assistant / system-admin / sales-lead / sales-research / sales-outreach / inbox-processor / crazy-agent / knowledge-synth / strategy-support-analyst (renamed от strategist, J3) / meta-agent (+FPF-Steward sub-role)
- **2 Phase 2a stubs:** dpo (external-mode) / customer-success (J2)

**Decisions:**

- **Q1 Family field:** **Functional** (sales, knowledge, meta, admin, research, etc.) — more practical than L-layer
- **Q2 All 18 manifests Phase 1 full depth:** APPROVED (Ruslan override my recommendation core+skeleton)
  - Ruslan quote: "всё, сука, писать сразу, глубоко, качественно, насколько это возможно"
  - Cost: ~35-45h writing работы (up from 25-30h)
  - Rationale: foundational contracts, no compression
- **Q3 Strategic-management decomposition:** already resolved Chunk 1 P5 — 5 atomic now + multi-binding
- **Q4 Compute contract в executor-binding:** YES (per P7)
- **Q5 D3 size accepted:** no compression, full depth

**Block 5 Lite list (per Item 7):**

```yaml
seniority-lite:
  current_level: J-Approve  # J-Auto | J-Approve | J-Strategic
  autonomous: [...]
  approve-required: [...]
  never: [...]
  direction_authority:
    - "Open hypothesis direction: J-Auto"
    - "Activate direction: J-Strategic"
    - "Archive direction: J-Strategic"
```

**Compute contract в executor-binding:**

```yaml
compute_contract:
  model_preference: claude-opus-4-7
  fallback_models: [claude-sonnet-4-6]
  thinking_mode: auto
  max_tokens_per_session: 50000
  cache_strategy: high
  latency_class: batch-ok | real-time
  escalation_rules: [...]
```

---

### Area 2 → D2 JETIX-FOLDER-STRUCTURE ✅ APPROVED 2026-04-19

**All 6 additions to v2 structure ACCEPTED:**

1. **`directions/`** top-level folder (Item 6 Portfolio model) — _active / _hypotheses / _archived
2. **8-я alpha `direction/`** в alphas/ — state machine + instances
3. **`inbox/`** top-level folder (Critic Weakness 2.4) — voice-notes pipeline outputs land here
4. **`outreach/`** с split model (Q5 Вариант C accepted):
   - Top-level `jetix/outreach/_shared/` — cross-direction templates
   - Per-direction `jetix/directions/*/outreach/{de,en,ru}/` — personalized content per language per direction
5. **Physical separation Life-OS ≠ Jetix** — Parallel structure (Q4 Вариант B):
   - `~/jetix-os/life-os/` — personal namespace
   - `~/jetix-os/jetix/` — business namespace
   - Asymmetric reference rule enforced (Jetix → Life-OS blocked via pre-commit hook)
   - Phase 2+ trigger: git filter-repo extraction
6. **Compute + Resource tracking files** (Chunk 1 P7 override):
   - `jetix/finance/compute-ledger.yaml`
   - `jetix/finance/resource-ledger.yaml` (Capital + Deep Hours)
   - `jetix/decisions/quarterly/YYYY-QN-attention-theme.md`

**Other Open Questions resolved:**

- **Q1 wiki separation:** SEPARATE fully confirmed (already decided Item 6; not shared)
- **Q2 `shared/` location:** top-level (accept Ruslan via "все остальное по рекомендациям")
- **Q3 entities/jetix-gmbh/ stub:** yes, write now (already decided MC1)
- **Q6 15 folders:** accept (no premature compression)

**Final Phase 1 folder count в `jetix/`: 15 folders:**

1. agents/<id>/ (combined role+executor+system+scratchpad)
2. alphas/ (8 subfolders including NEW direction/)
3. alpha-log/
4. clients/ (markdown CRM)
5. **directions/** (NEW — portfolio model)
6. wiki/ (cross-cutting knowledge, scope: jetix)
7. decisions/ (adr + postmortem + letter + strategy + weekly + okr + policy + quarterly + promotions + fpf-stewardship + backlog + templates)
8. evals/<role>/
9. docs/ (Diátaxis how-to + reference)
10. finance/ (invoices + ledger + compute-ledger + resource-ledger)
11. **inbox/** (NEW — voice-notes pipeline output)
12. **outreach/** (NEW — _shared templates)
13. entities/jetix-gmbh/ (federation stub)
14. governance/ (advisory-board, trustee-designations, beirat/, aufsichtsrat/)
15. ops/ (hit-by-bus, business-continuity, incident-playbook, regulatory-incidents)

Plus files: CONSTITUTION.md, CLAUDE.md, README.md.

**Life-OS structure (`~/jetix-os/life-os/`):**
- wiki/ (personal knowledge, NOT shared)
- daily-log/{YYYY}/, reflection/, health/, relationships/, personal-goals/
- decisions/ (personal ADRs), okrs/, letters/

**Top-level shared (`~/jetix-os/shared/`):**
- role-framework/ (meta methodology — used by both life-os and jetix)
- levenchuk-ontology/ (ШСМ reference)
- writing-templates/

**Deferred Phase 1 (Simplifier triggers):**
- `comms/mailboxes/` — при inter-agent dependency
- `state/` — при DuckDB real usage
- `sales/` — при 2+ продавцах
- `templates/` — при 2+ авторе (currently в docs/reference/)
- `processes/` — при formal procedures
- `products/` — при 1-м SaaS commit
- `roles/` separate — при 30+ agents OR 1-й human

---

### Area 1 → D1 JETIX-ARCHITECTURE-FINAL ✅ APPROVED 2026-04-19

**4 decisions:**

- **Q1 Exit strategy:** **не упоминаем вообще** в D1. Focus на Phase 1 + mega-corp target, no exit path specifics.
- **Q2 Length:** **15-20 pages accepted** — инженерный структурный документ без воды; sufficient space для all overrides reflected.
- **Q3 Structure 8 sections:** accept as-is (Context / Reference Architecture / Operational Architecture (Phase 1 MVA) / Decision / Consequences / Alternatives / Migration / Review triggers).
- **Q4 Portfolio of Directions как 8-й first-class principle:** ✅ APPROVED.

**IMPORTANT — 7 principles → 8 principles:**

После Chunk 1 было 7 core principles. Теперь добавляется 8-й:

**P8 — Jetix operates as Portfolio of Directions (holding-style pattern).**

- Directions = business verticals / research tracks / portfolio bets
- Каждое direction: hypothesis → research → experiment → activated / dropped
- Cross-functional observation через wiki/concepts/ + edges.jsonl
- CRM ↔ Wiki ↔ Direction graph
- Jetix = research engine + operational infrastructure для multiple bets
- 8-я true alpha (Direction) materializes this principle operationally

**Ruslan quote:** "портфолио модель как first-class принцип, это фундаментальная архитектурная парадигма."

**D1 final structure:**

1. Context (vision, DACH + US + RU markets, portfolio thinking intro)
2. Reference Architecture (full 7-layer + 8 principles + 8 alphas)
3. Operational Architecture Phase 1 MVA (4 layers materialized, 11 folders, 8 alphas, directions/)
4. Decision (key architectural commitments)
5. Consequences (what enables / costs)
6. Alternatives (considered + rejected)
7. Migration (Phase 1 Min → Phase 2 Add → Phase 3 Add; 7+7 rollout)
8. Review triggers

**Link-backs к D2-D9 (folder/roles/life-os-sep/knowledge/fpf-lite/career/instructions/decision-record).**

---

## Chunk 4 — Outstanding Tensions (4 items — OT1 resolved early в Chunk 1)

### OT5 — FPF-Lite Token-budget + Publishing ✅ APPROVED 2026-04-19

**Sub-question 1 — Token-budget loading: Вариант A (full text везде)**

Ruslan quote: "Мы оставляем эти FPF контексты полностью на всех. Мы можем себе это позволить. Главное чтобы это глубоко и качественно использовалось и работало."

**Decision:** full FPF-Lite text (7-10K tokens) loaded в каждый agent system.md.

- Глубина > efficiency
- Quality over token savings
- Monthly cost estimate: $5-10/month (negligible при €150-350 total API spend)
- Context window pressure: minimal (10K = 1% of Opus 4.7 1M context, 5% of Sonnet/Haiku 200K)
- Consistent с Левенчук #11 exocortex reservation (25K hard-pinned) — full FPF fits comfortably

**Все 11 agents (+meta-agent) получают full FPF-Lite в system prompt.** No differentiation.

**Sub-question 2 — Publishing: Вариант A (internal forever — initially)**

Ruslan quote: "Мы оставляем это в GitHub пока как секретный соус. Нигде не публикуем, это должно быть в секрете. Потом по мере роста будем смотреть."

**Decision:** FPF-Lite — **internal only** Phase 1+. No public release without explicit decision.

- Protect methodology during iteration
- Secret sauce defense
- Phase 2c-3+ trigger: revisit publishing decision когда methodology proven + case studies accumulated
- Backlog entry: `decisions/backlog/fpf-lite-publishing-review.md` — review trigger at €1M+ ARR

**Outcome:** Maximum ontology depth Day 1 + competitive moat protected.

---

### OT4 — Trademark Jetix vs Disney: DEFER (Perplexity research + backlog) ✅ RESOLVED 2026-04-19

**Ruslan decision:**
> "Мы просто сейчас сделаем research c Perplexity глубокий, нам этого на данный момент будет достаточно. Будем в неофициальном режиме двигаться. Потом, как только получим финансы, с этим вопросом разберемся более подробно."

**Plan:**

1. **Phase 1 (immediate):** Ruslan runs Perplexity deep research — DPMA/EUIPO trademark status для "Jetix", Disney brand history post-2009, preliminary risk assessment. Cost: ~30 min, €0.
2. **Phase 1 (ongoing):** Unofficial / informal brand usage — continue using "Jetix" без formal trademark registration.
3. **Trigger for formal resolution:** first meaningful revenue (€20-50K range, когда brand equity starts forming).
4. **Phase 2a action:** IP lawyer consultation + full trademark search + defensive registration OR rename decision (~€2000-3500 budget allocated).
5. **Backlog entry:** создать в `decisions/backlog/trademark-jetix-formal-resolution.md` с trigger conditions + budget estimate + action checklist.

**Risk accepted Phase 1:** Disney может send cease-and-desist — probability low при €0-50K revenue + unofficial usage. Defense: rename burden lower сейчас чем Phase 2b+.

**Outcome:** Zero cost Phase 1. Formal resolution triggered by revenue. Backlog tracked.

---

### OT3 — EU AI Act Tier: Scenario C (Risk-proportional) ✅ APPROVED 2026-04-19

**Status:** accept Scenario C + compliance calendar + DPA template Phase 1.

**4 risk categories с different human gates:**

| Category | Risk | Gate | Examples |
|----------|------|------|----------|
| **Internal-only** | Minimal | None (J-Auto) | Research, wiki ingestion, internal notes, summaries |
| **External reversible** | Low-medium | Batch approval (J-Approve batch) | Outreach drafts (batch 20/week), social media scheduling |
| **External non-reversible / client-affecting** | High | Per-action approval (J-Approve per) | Send specific email, publish content, commit to client deliverable |
| **Strategic / regulatory** | Critical | Ruslan explicit (J-Strategic) | Sign contract, offer discount, compliance claim, legal liability |

**Policy document:** `decisions/policy/ai-agent-decision-authority.md` — defines categories + examples.

**Art. 22 GDPR compliance:** all client-affecting AI decisions have human approval gate — automated Art. 22 protection.

**Complementary (applied defaults per recommendation):**

- ✅ **Compliance calendar Phase 1:** `decisions/policy/eu-ai-act.md` с quarterly review triggers (2h cost). Timeline: 2025 GPAI monitor → 2026 Q2 internal AI inventory → 2026 Q3 tier classification → Aug 2026 High-risk obligations go live.

- ✅ **DPA template Phase 1:** `decisions/templates/client-dpa-template.md` (3-4h, may need IP lawyer consult). Critical для ai-consulting-dach direction — client engagement часто requires DPA ДО data sharing. Having template ready accelerates first enterprise close.

**Consistent с:**
- Item 7 Career Ladder (J-Auto / J-Approve / J-Strategic already maps decisions)
- R12 FPF-Steward (max Левенчук discipline — compliance thinking integrated)
- P6 DACH +US +RU (GDPR territorial scope covered)

**Outcome:** Ruslan не bottleneck для internal work; batch approvals scale; high-risk protected; DPA-ready Day 1.

---

### OT2 — Bilingual Frontmatter: Scenario E (Hybrid) ✅ APPROVED 2026-04-19

**Status:** accept Hybrid scenario — best discipline + minimum burden.

**Implementation:**

**Namespace language conventions:**
- `policy/`, `decisions/` — **bilingual** (`lang: [ru, en]`): EN summary mandatory (~150-300 words) + RU body allowed
- `roles/` — **EN primary** (`lang: en`): agents + hires + Mittelstand Geschäftsführer read; DE добавляется Phase 2a closer to hire
- `ops/` — **EN primary** (emergency accessibility для trustee)
- `wiki/concepts/`, `wiki/summaries/`, `directions/*/direction.md` — RU primary + **auto-translation hook** (`auto_en: true` → pre-commit hook translates via Claude Opus 4.7, saves sibling `.en.md`)
- `wiki/sources/`, `wiki/ideas/`, `alphas/` — RU default
- `finance/` — DE mandatory (HGB compliance)
- `clients/<id>.md` — internal notes RU; `client_language: de|en|ru` for client-facing
- `outreach/` — **separate folders per language** (`outreach/de/`, `outreach/en/`, `outreach/ru/`): different copy, not translations; cultural tuning

**Auto-translation hook (5-й pre-commit hook на top of 4 принятых в Item 8):**
- Detects `auto_en: true` в frontmatter
- Extracts content, runs Opus 4.7 translation
- Saves sibling `.en.md`
- Cost: 2-3h setup + ongoing €1-5/mo API

**Cost breakdown:**
- Phase 1 setup: 5-10h existing EN summaries (30-50 docs) + 2-3h hook setup = ~8-13h total
- Ongoing: ~5 min per new critical doc + auto-translation for auto_en docs
- Phase 2a (first non-RU hire): ~4-6h targeted just-in-time translation (no mass burst)

**Consistent с:**
- Левенчук max discipline (structural conventions)
- P6 DACH +US +RU (client folders per language)
- Item 8 pre-commit hooks (5-й hook integrates naturally)
- Mega-corp scalability (EN-ready foundation)
- MC3 Left мереологический override (concepts auto-translate quality-preserving)

---

### Steps 3+4 — Rejections + Flag scan ✅ RESOLVED 2026-04-19

**R11 IPO readiness placeholder:** ✅ **REJECT confirmed** (Variant A — no placeholder Phase 1; add при Series A contemplation 2029-2031).

**R12 FPF-Steward sub-role:** ⚠️ **OVERRIDE — Variant B** (add FPF-Steward sub-role в meta-agent Phase 1).

Ruslan quote: "Здесь мне нужен Левенчук на максимум. Всё что его техника предлагает, мы используем на 100% на максимум. Берем вариант B и внедряем глубоко."

**Implementation:**
- Sub-role section в `agents/meta-agent/system.md`
- Scope: FPF-Lite consistency, Alpha/WP/Entity classification, past-participle (automated via Hook 4 + manual audit cross-check), concept duplication detection, role-manifest structural integrity, Direction-concept boundary clarity, frontmatter schema
- Cycle: Quarterly audit (Q1/Q2/Q3/Q4 within 2 weeks of quarter close) + ad-hoc при major ontology changes
- Output: `decisions/fpf-stewardship/YYYY-QN-ontology-audit.md`
- Critical для portfolio model (8 directions increases drift risk)

**Other 9 rejections (R1-R9):** confirmed implicit через Chunks 1-2 — nothing to revise.

**R10 Multi-currency:** resolved via Stripe/Wise pattern (Step 2 above).

**Flag scan 38 accepted:** no flags — все 38 items integrated через Chunks 1-2 + Chunk 3 Items 1-10.

---

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

## ✅ All 7 Chunks COMPLETE 2026-04-20

- [x] Chunk 1 — High-level frame (7→8 principles + P7 evolution)
- [x] Chunk 2 — 6 Meta-conflicts resolved (MC1-MC6)
- [x] Chunk 3 — 38 Accepted + 12 Rejected + R10 multi-currency revisit
- [x] Chunk 4 — 5 Outstanding Tensions resolved (OT1-OT5)
- [x] Chunk 5 — Areas 1-5 (D1-D5 detailization)
- [x] Chunk 6 — Areas 6-9 (D6-D9 detailization)
- [x] Chunk 7 — Final sign-off (Stage 3 APPROVED)

Stage 3 ADR финализован. Stage 3.5 (D9 draft v0.5) выпущена 2026-04-20.
Затем Stage 3.6 review добавил Post-FPF-Discovery layer — см. **Chunk 8** ниже.

---

## Chunk 8 — Post-FPF-Discovery Additions ✅ APPROVED 2026-04-20

### 8.1 Discovery context

После closure Chunk 7 (Stage 3 ADR finalized 2026-04-20 morning), Ruslan
прислал ссылку на `github.com/ailev/FPF` — **First Principles Framework**
Анатолия Левенчука. Это тот самый источник, к которому Jetix Левенчук-
ориентированная онтология уже апеллировала imlicitly через предыдущие
waves research'а (9 architectural research waves R1-R9 + 4 reviewer-reports),
но теперь доступна **первоисточник в полном виде — 62,202 строки spec'а
(FPF-Spec.md, 5.7 MB) + Readme.md**.

**Vendor**: FPF-Spec + Readme вендорнуты в `raw/external/ailev-FPF/`
(commit 0a22129), **ATTRIBUTION.md** оформлен (usage scope **internal-only**,
**no formal license stated в upstream repo** — GitHub default "all rights
reserved"; **citation explicitly requested** upstream в Readme:
`Levenchuk, Anatoly. First Principles Framework (FPF). GitHub repository:
https://github.com/ailev/FPF`; **conservative interpretation**: internal
reference + adaptation OK с citation; public redistribution requires
explicit permission).

**5 Perplexity researches выполнены** параллельно (R-A through R-E,
`raw/research/levenchuk-fpf-research-2026-04-20/`):
- R-A: 5 primitives + 16 trans-disciplines
- R-B: holonic architecture + mereology
- R-C: trust calculus + language-state transduction
- R-D: characteristic spaces + CSLC
- R-E: multi-view publication + method harmonization

**KB compilation**: `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md`
(~60 pages, commit 3cb5f81) — compiled digest FPF primitives / patterns /
instruments / guard-rails structured for Jetix application.

**Gap Analysis**: `raw/research/fpf-gap-analysis-2026-04-20.md` (2486 строк,
commit 74cf858) — systematic сравнение current Jetix architecture (post-
Chunk 7) vs FPF-Spec patterns. Output: **65/100 alignment** + 5 critical
gaps + 22 recommendations + 11 open questions + 9 Jetix innovations
identified.

**Ruslan directive Stage 3.6 opening:**
> "Я хочу всё что там ещё не дотягивается улучшить. Максимально глубоко.
> Все критические gaps — качественно разбирать по одному."

**Stage 3.6 review executed 2026-04-20** через tracking file
`decisions/gap-analysis-review-decisions-2026-04-20.md`. Все 60+
decisions locked тот же день:
- 5 Gaps — full depth adoption
- 22 Recommendations — all accepted
- 11 Open Questions — resolved
- 9 Innovations — confirmed internal-only

Chunk 8 consolidates эти решения в ADR; D9 draft v0.6 (separate file)
regenerates full architecture record с учётом Chunk 8 material.

### 8.2 Overall alignment + Ruslan stance

Gap analysis output: **65/100 alignment** score Jetix (post-Chunk 7) vs
FPF-Spec. Strongest alignment: 5 primitives absorbed (Role ≠ Executor =
U.Role split; past-participle = state-machine discipline; holonic 3-
level mereology). Critical gaps: boundary unpacking A.6.*, trust
calculus B.3 F-G-R, characteristic spaces A.17-21, unified term sheet
F.17, multi-view publication E.17.

**Post-adoption expected alignment: 85-90/100** (все 5 critical gaps +
22 recs adopted).

**Stance**: consistent с previous pattern 11 Ruslan overrides — все в
+Левенчук direction (Chunk 1 P7 Compute, MC3 full 3-level mereology, R12
FPF-Steward sub-role, OT5 full-text FPF loading и т.д.). Здесь тот же
course: **maximum depth, no compromises, all applicable FPF patterns
adopted**. Ни одна P1 рекомендация не reject'нута; ни один P2 не
deferred; P3 все accepted full depth; 2 P2 elevated к P1-equivalent
(Rec-09 E.17 Multi-View, Rec-11 A.18 CSLC) через Gap-adoption.

### 8.3 5 Critical Gaps adopted full depth

#### Gap 1 — Boundary Unpacking (A.6.*) ✅ FULL ADOPT

- **FPF basis:** A.6.B Boundary Norm Square (L/A/D/E — Laws /
  Admissibility / Deontics / Work-Effects), plus A.6.C Contract
  Unpacking, A.6.0 U.Signature, A.6.P Relational Precision, A.6.Q
  Quality Term, A.6.H Wholeness
- **Ruslan decision:** "подтверждаем полностью, внедряем глубоко,
  качественно" (Option A full)
- **Cost:** 4-6h Phase 1 + ~5 min per new clause ongoing
- **Rationale:** DACH enterprise compliance signal; audit-readiness;
  reusable L sections между contracts
- **Implementation:**
  - Day 5 (proposal template) + Day 6 (contract + DPA template) —
    full L/A/D/E structure applied
  - `decisions/policy/boundary-discipline.md` — routing convention
    + A.6 cluster usage guide
  - A.6.C Contract Unpacking applied к contract/DPA templates
  - A.6.0 U.Signature для formal kind-explicit role-manifest headers
  - A.6.P RPR-qualified relations в concept cross-references
  - A.6.Q Q-TERM precision restoration в SKU/quality descriptions
  - A.6.H Wholeness language unpacking в complex concepts
- **Ties to:** Rec-01 P1 (same scope — fully subsumed)

#### Gap 2 — Trust & Assurance Calculus (B.3 F-G-R) ✅ FULL + DEEP ADOPT

- **FPF basis:** B.3 Trust & Assurance Calculus — Formality scale
  (F0-F9), Ground-scale (G evidence types), Reliability scale (R-low
  через R-formally-proven), plus B.3.3 Assurance Subtypes, B.3.4
  Evidence Decay, B.3.5 Working-Model Relations (CT2R-LOG), Pathwise
  Justification, Weakest-Link analysis, CL (Congruence Level)
- **Ruslan decision:** "подтверждаем полностью + deep adoption"
  (Option A full) — **ADRs + client deliverables + agent outputs**
  (broader scope than Claude rec B)
- **Cost:** 3-5h Phase 1 (policy + retrofit 10-15 existing ADRs +
  template updates) + ~1 min per new ADR/deliverable ongoing
- **Rationale:** Art. 22 GDPR defence strengthened; AI-agent output
  discipline; audit trail quality; EU AI Act high-risk readiness
- **Implementation:**
  - `decisions/policy/trust-tagging.md` — policy document для F/G/R
    conventions
  - F-scale F0-F9 defined, Jetix expected range F0-F3
  - ClaimScope naming convention (bounded-context paths,
    `sales/dach-mittelstand/...`)
  - R-levels: R-low / R-medium / R-high / R-certified / R-formally-proven
  - **Frontmatter schema addition** (ADR + client deliverables):
    ```yaml
    formality: F0-F9
    reliability: R-low | R-medium | R-high | R-certified | R-formally-proven
    claim-scope: bounded-context-path
    ```
  - Retrofit existing 10-15 ADRs с F-G-R tags (mostly F1-F2 R-medium)
  - Meta-agent prompt update: enforce F-G-R tagging
  - FPF-Steward quarterly audit scope includes F-G-R compliance check
- **Ties to:** Rec-04 P1 (same scope — fully subsumed)

#### Gap 3 — Characteristic Space (A.17-A.21) ✅ FULL + DEEP ADOPT

- **FPF basis:** A.17 CHR-NORM (Canonical Characteristic), A.18 Minimal
  CSLC (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) Kernel, A.19
  CharacteristicSpace + mechanisms (UNM / UINDM / USCM / ULSAM / CPM /
  SelectorMechanism), A.20 Flow Constraint Validity, A.21 GateFit
- **Ruslan decision:** "максимально подтверждаю" (Option A full) —
  все 5 patterns + 3 concrete Phase 1 applications
- **Cost:** 8-15h Phase 1 + 30-60 min per new SKU/direction/promotion
  ongoing
- **Rationale:** измеримые decisions > subjective; defensible pricing;
  objective agent promotion; consistent comparison framework
- **Implementation 3 concrete Phase 1 CHR spaces:**
  1. **SKU pricing CHR** — `decisions/policy/sku-pricing-chr.yaml`
     (3-5h). Scales: hours-invested, deliverable-complexity, client-
     risk-tier, DACH-premium-factor. Gate profiles via A.21 для
     acceptance criteria.
  2. **Direction kill criteria CHR** —
     `directions/_templates/kill-chr-template.yaml` + applied к
     existing `ai-consulting-dach/` (3-5h). Scales: 90-day revenue-
     generated, pipeline-health, unit-economics, strategic-fit.
  3. **Agent promotion CHR** —
     `decisions/policy/agent-promotion-chr.yaml` (2-5h). Scales:
     task-success-rate, evidence-quality, autonomy-demonstrated,
     critical-decisions-ratified. A.18 CSLC formal (OQ-11 resolution).
- **Plus conventions doc:**
  `decisions/policy/characteristic-space-conventions.md` — общие
  правила для Jetix CSLC usage (when to formalize vs informal).
- **Plus deep:** NQD-CAL (C.18), E/E-LOG (C.19), MM-CHR (A.21),
  Pareto dominance — adopted где applicable в decisions.
- **Ties to:** Rec-11 P2 elevated к P1-equivalent, OQ-11 resolved,
  partial tie к Rec-07 (portfolio C.18/C.19 usage)

#### Gap 4 — Unified Term Sheet (F.17 UTS) + LEX-BUNDLE (E.10) ✅ FULL + DEEP ADOPT

- **FPF basis:** F.17 Unified Term Sheet (Kernel-first Layout A, 30-50
  rows × 6-8 context columns), E.10 LEX-BUNDLE (4-register naming:
  tech / plain / legacy / mnemonic), SenseCells per non-trivial cell,
  explicit Bridges mappings
- **Ruslan decision:** "полное и глубокое внедрение" (Option A full) +
  **timing concurrent с D6 writing** (OQ-08 Variant B)
- **Cost:** 6-10h Phase 1 setup + ~2h per quarter FPF-Steward audit
- **Rationale:** critical для 18 agents + future hires + clients;
  prevents ontological drift; onboarding hire-friendly; single source
  of truth для Jetix terminology
- **Implementation:**
  - **`wiki/foundations/jetix-uts.md`** — central UTS table (Layout A
    Kernel-first, 30-50 core rows)
  - **Context columns** (6-8):
    1. FPF U.Type (canonical)
    2. Jetix tech (engineering-grade term)
    3. Jetix plain (client-facing / plain English)
    4. ШСМ-Russian (Левенчук legacy)
    5. Essence-legacy (SEMAT / v1 mapping — historical)
    6. DACH-legal (HGB / AktG / BGB / GDPR terms)
    7. AI-industry (industry-standard vocabulary)
    8. Bridges (explicit equivalence mappings between contexts)
    + Rationale column per row
  - **LEX-BUNDLE 4-register** naming per row (tech/plain/legacy/
    mnemonic identifiers)
  - **SenseCells** per non-trivial cell (clarify domain-specific sense)
  - **Bridges** explicit equivalence mappings + CL (Congruence Level)
    measurement for semantic drift between contexts
- **Timing (OQ-08 B):** concurrent с D6 JETIX-FPF writing — UTS rows =
  U.Types = D6 Section 8 ontology. Ensures consistency; avoids
  dual-maintenance burden.
- **Maintenance:** FPF-Steward quarterly audit scope includes UTS
  review (row additions, Bridges updates, CL re-measurement).
- **Ties to:** Rec-02 P1 (fully subsumed), Rec-12 P2 (LEX-BUNDLE fully
  subsumed), Rec-10 P2 (Bridges/CL fully subsumed), OQ-08 resolved

#### Gap 5 — Multi-View Publication (E.17) ✅ FULL + DEEP ADOPT (modified stronger)

- **FPF basis:** E.17 Multi-View Publication Kit (Viewpoints / Views /
  Correspondences), E.17.0 U.MultiViewDescribing, E.17.1
  U.ViewpointBundleLibrary, E.17.2 TEVB Typical Engineering
  Viewpoints Bundle, plus E.18 TGA Transduction Graph (simpler form
  via A.6.3.CR ConservativeRetextualization for safe cross-view
  translation)
- **Ruslan decision:** "подтверждаю все глубоко, максимально фиксируем"
  (Option A **modified stronger**) — **mandatory multi-view для ALL
  Audit SKU deliveries from first delivery onward** (не pilot-only per
  Claude rec; stronger than OQ-04 default)
- **Cost:** 3-5h setup (Viewpoint Bundle + canonical template + first
  view templates) + 8-12h first pilot delivery + marginal ongoing
  after templates mature
- **Rationale:** Mittelstand deal acceleration (5 audiences served in
  parallel); audit-readiness; scale-prep для Phase 2a+; ISO/IEC/IEEE
  42010 alignment (professionalism signal к Aufsichtsrat-grade clients)
- **Jetix Viewpoint Bundle — 5 viewpoints Phase 1:**
  1. **Executive** (CEO, Aufsichtsrat; 2-3 pages; plain + finance)
  2. **Technical** (CTO, engineers; 20-40 pages; technical + specs)
  3. **Governance** (board, risk committee; 3-7 pages; governance +
     legal)
  4. **Regulatory** (BfDI, EU AI Act auditors; 3-5 pages; regulatory +
     legal — pre-mapped против EU AI Act / GDPR Art. 22 / EU DORA
     obligations)
  5. **Internal-learning** (Jetix team; 5-10 pages; internal + FPF
     patterns referenced)
- **Implementation:**
  - `decisions/templates/jetix-viewpoint-bundle.yaml` — Viewpoint
    definitions (name / audience / depth / language / canonical-
    sections-mapping)
  - `decisions/templates/audit-canonical-template.md` — underlying
    canonical artifact structure (single source of truth per audit)
  - `decisions/templates/views/` — 5 view templates (one per viewpoint)
  - **Correspondences table** — canonical section → view section
    mapping (automated rendering check)
  - **Update protocol:** canonical changes → views regenerated
    (A.6.3.CR Same-Entity Retextualization discipline prevents
    semantic drift)
  - First pilot: Müller GmbH audit (or first actual Audit SKU client)
- **Ties to:** Rec-09 P2 elevated к P1-equivalent, OQ-04 resolved
  (override to mandatory, stronger than pilot-only)

**Total 5 Gaps work estimate Phase 1: ~30-45h** + ongoing discipline.

### 8.4 22 Recommendations all accepted

Summary table (все 22 accepted; P2/P3 conditionally elevated):

| # | Rec | FPF basis | Status | Ties to Gap/OQ |
|---|-----|-----------|--------|----------------|
| 01 | Boundary Norm Square lanes в contract/DPA | A.6.B + A.6.C | ✅ Full | Gap 1 |
| 02 | UTS skeleton для Jetix concepts | F.17 | ✅ Full | Gap 4 |
| 03 | D.5 Bias-Audit Cycle для EU AI Act | D.5 | ✅ Full (standalone) | — |
| 04 | F + R tags в ADR/deliverable frontmatter | B.3 | ✅ Full | Gap 2 |
| 05 | A.14 typed mereology edges | A.14 + A.6.H | ✅ Full (standalone) | — |
| 06 | B.2 MHT Jetix phase transitions | B.2 + B.2.1/2.2/2.5 | ✅ Full (standalone) | — |
| 07 | Portfolio через C.18 NQD-CAL + C.19 E/E-LOG | C.18 + C.19 | ✅ Full | Gap 3 partial |
| 08 | A.13:4.3 Agency-CHR fallback | A.13 | ✅ Full | — |
| 09 | E.17 Multi-View Publication | E.17 + E.18 | ✅ Full (elevated) | Gap 5 |
| 10 | F.9 Bridge + CL convention | F.9 / E.10 | ✅ Full | Gap 4 |
| 11 | A.18 CSLC Characteristic Space | A.18 / A.19 | ✅ Full (elevated) | Gap 3 / OQ-11 |
| 12 | E.10 LEX-BUNDLE | E.10 | ✅ Full | Gap 4 |
| 13 | E.5.1 DevOps Lexical Firewall (D6 Core/Tooling split) | E.5.1 + E.5.3 | ✅ Full (Option C) | OQ-07 |
| 14 | B.4 Canonical Evolution Loop в 4 rituals | B.4 + B.4.1 | ✅ Full | — |
| 15 | F.6 Role Assignment cycle (agent onboarding) | F.6 | ✅ Full | — |
| 16 | C.22 Problem-CHR TaskSignature | C.22 + C.22.1 | ✅ Full | — |
| 17 | A.16 PreArticulationCuePack (voice-notes) | A.16 / A.16.1 | ✅ Full | — |
| 18 | F.11 Method Quartet Harmonisation | F.11 | ✅ Full | — |
| 19 | A.6.S Signature Engineering Pair (SKU evolution) | A.6.S | ✅ Full | — |
| 20 | E.20 Mechanism Introduction Protocol | E.20 | ✅ Full | — |
| 21 | G.5 Multi-Method Dispatcher | G.5 | ✅ Full | — |
| 22 | First quarterly FPF-Steward audit Q2 2026 | — (Jetix-specific) | ✅ Full | — |

#### P1 standalone recs (not covered в Gaps) — narrative

**Rec-03 D.5 Bias-Audit Cycle ✅ FULL**

- **FPF basis:** D.5 Bias-Audit & Ethical Assurance
- **Cost:** 3-5h setup + 1h per deliverable + 2h quarterly
- **Implementation:**
  - `decisions/policy/bias-audit-cycle.md` — policy + 4-stage cycle
    (BA-0 kickoff / BA-1 scan / BA-2 panel / BA-3 closure)
  - Templates: BA-0 kickoff / BA-1 scan / BA-3 closure в
    `decisions/templates/bias-audit/`
  - `bias-register.yaml` schema per deliverable
  - Per-deliverable structure:
    `clients/<client>/audits/<audit>/bias-audit/`
  - **Bias Taxonomy (5-class):** REP (representation) / ALG (algorithmic)
    / VIS (visual) / MET (measurement) / LNG (linguistic)
  - Quarterly aggregation:
    `decisions/bias-audit/YYYY-QN-bias-audit.md`
  - **Phase 1 simplified cycle:** BA-0 + BA-1 + BA-3 (solo Ruslan, no
    BA-2 Panel Review until Phase 2a Beirat Ethics advisor)
  - Integration: `decisions/policy/eu-ai-act.md` (OT3 compliance
    calendar) + FPF-Steward quarterly audit scope (R12)
- **Rationale:** EU AI Act compliance Aug 2026; Art. 22 GDPR defence;
  enterprise client readiness (DACH Mittelstand Compliance VP expects
  formal bias-audit trail)

**Rec-05 A.14 typed mereology edges ✅ FULL**

- **FPF basis:** A.14 Advanced Mereology (Components / Portions /
  Aspects / Phases / Members) + A.6.H Wholeness
- **Cost:** 2-4h Phase 1 + 5 min per new edge ongoing
- **Implementation:**
  - Retag existing 5 generic edges в `wiki/foundations/jetix-creation-
    graph.md` с A.14 typed edges
  - **`decisions/policy/mereology-edge-types.md`** documents 10 edge
    types:
    - **A.14 core 6:** ComponentOf / ConstituentOf / PortionOf /
      PhaseOf / MemberOf / AspectOf
    - **Jetix-introduced 4:** creates / operates-in /
      methodologically-uses / constrained-by / fills
    - When-to-use-which guide + anti-patterns
  - A.6.H Wholeness patterns applied где relevant (client-relationship
    wholeness, deal wholeness, direction wholeness)
  - FPF-Steward quarterly audit scope: edge type verification
- **Rationale:** reasoning accuracy; semantic clarity; FPF-Steward
  auditability; cheap finishing touch для MC3 full-depth mereological
  graph (повышает quality tractably)

**Rec-06 B.2 MHT phase transitions ✅ FULL**

- **FPF basis:** B.2 Meta-Holon Transition + B.2.1 Emergence + B.2.2
  Re-identification + B.2.5 Supervisor-Subholon Feedback Loop
- **Cost:** 2-4h Phase 1 + 2h per transition when happens
- **Implementation:**
  - **`decisions/policy/phase-transitions-mht.md`** — 4 MHTs documented:
    - **MHT-1:** Phase 1 → 2a (solo + hire)
    - **MHT-2:** Phase 2a → 2b (team 5-20)
    - **MHT-3:** Phase 2b → 2c (€10-50M, multi-entity, first
      acquisition)
    - **MHT-4:** Phase 2c → 3 (€50M+, multi-entity federation)
  - **Each MHT template:** from-holon / to-holon / trigger-conditions /
    emergence-signals (early indicators) / re-identification
    (invariants + mutables) / transition-process (pre/during/post
    actions) / supervisor-subholon-feedback loop
  - **`decisions/templates/mht-template.yaml`** — reusable template
  - Integration: D8 rollout timeline + D7 career levels phase-column +
    D4 Life-OS separation Phase 2a/3 triggers aligned
- **Rationale:** systematic transition management; invariant preservation;
  audit-readiness; bridge к scale. Предотвращает архитектурный хаос
  при 1st hire, 5-20 team growth, 1st acquisition, multi-entity.

#### P2 (10 recs) accepted narrative

**Ruslan directive:** "All full + Deep Adoption. Подтверждаю."

- **Rec-07 Portfolio C.18 NQD-CAL + C.19 E/E-LOG** (3-5h): per-direction
  `ee-log.yaml` + `nqd-distinctions.yaml`; strengthens Portfolio
  model's exploration/exploitation discipline.
- **Rec-08 A.13:4.3 Agency-CHR fallback** (1-2h): `executor-binding.yaml`
  получает `agency-profile` section + fallback rule; formal agency-
  scale 0.0-1.0 dimension adds к 3-tier J-Auto/Approve/Strategic.
- **Rec-09 E.17 Multi-View** → via Gap 5 (elevated).
- **Rec-10 F.9 Bridge + CL convention** (2-3h): Bridges между contexts
  + Congruence Level measurement для semantic drift; applied в
  cross-direction wiki + UTS bridge section.
- **Rec-11 A.18 CSLC** → via Gap 3 (elevated).
- **Rec-12 E.10 LEX-BUNDLE** → via Gap 4 UTS (4-register naming).
- **Rec-13 E.5.1 DevOps Lexical Firewall (D6 Core/Tooling split)**
  (3-5h, OQ-07 Option C): D6 JETIX-FPF Core-focused (20-30 pages);
  `wiki/foundations/fpf-tooling.md` companion (10-20 pages). E.5.3
  Unidirectional Dependency preserved (Core → Tooling, not reverse).
- **Rec-14 B.4 Canonical Evolution Loop в 4 rituals** (1-2h):
  Observe/Reflect/Decide/Act mapped к daily/weekly/monthly/quarterly.
  D8 4-rituals section updated с explicit evolution loop framing.
- **Rec-15 F.6 Role Assignment cycle (agent onboarding)** (1-2h):
  extends already-accepted `agent_onboarding` (Левенчук Part 3 #2) с
  full cycle (6-step F.6 pattern: identify/request/propose/negotiate/
  enact/retrospect) + retrospective step + template.
- **Rec-16 C.22 Problem-CHR TaskSignature** (2-3h): structured client
  problem intake (Problem-CHR coordinate + TaskSignature: inputs /
  outputs / constraints / acceptance-criteria); template в
  `decisions/templates/client-intake-problem-chr.yaml`.

**Total P2 new work: ~13-22h Phase 1.**

#### P3 (6 recs) accepted narrative

**Ruslan directive:** "all подтверждаю, deep adoption".

- **Rec-17 A.16 PreArticulationCuePack** (1-2h): template
  `inbox/cues/<slug>.md` с maturity layer pre-articulation → claim →
  hypothesis → direction progression. Voice-notes pipeline получает
  PACK wrapping.
- **Rec-18 F.11 Method Quartet Harmonisation** (1-2h): monthly check
  per direction — method-design / method-work / method-plan / method-
  evidence alignment. Ties с Rec-14 B.4 Evolution Loop.
- **Rec-19 A.6.S Signature Engineering Pair (SKU evolution)** (1-2h):
  versioned SKU signatures (v1 active для old clients + v2 для new).
- **Rec-20 E.20 Mechanism Introduction Protocol** (1h): protocol doc
  для introducing new mechanisms — trial period, success criteria,
  rollback plan; applies perk mechanism additions к Jetix OS.
- **Rec-21 G.5 Multi-Method Dispatcher** (2-3h): MethodFamily Registry
  + dispatcher rules для multi-method decisions; integrates с F.11
  Method Quartet.
- **Rec-22 First quarterly FPF-Steward audit Q2 2026** (2-4h Q2 close):
  first `decisions/fpf-stewardship/2026-Q2-ontology-audit.md` validates
  Phase 1 FPF adoptions (all Gaps + 22 Recs sanity-checked against
  FPF-Spec).

**Total P3 new work: ~8-14h Phase 1.**

### 8.5 11 Open Questions resolved

| OQ | Topic | Decision | Rationale |
|----|-------|----------|-----------|
| 01 | FPF rename | ✅ **B — JETIX-FPF** | "переименуем в Jetix FPF, чтобы ничего не запуталось" — attribution clarity |
| 02 | P1 adoption scope | ✅ All 6 P1 + 3 P2 elevated | Steps 2-3 full depth |
| 03 | Portfolio NQD+E/E-LOG timing | ✅ Phase 1 (wiki artifact) | Consistent с Rec-07 |
| 04 | E.17 Multi-View threshold | ✅ **Modified A — Mandatory от first delivery** | Stronger than Claude pilot rec |
| 05 | F-G-R scope | ✅ ADRs + client deliverables + agent outputs | Broader than Claude rec B |
| 06 | Model D terminology | ✅ **B — Anglicize (Nested Holonic Structure)** | "похуй на историю, делай по FPF как правильно" |
| 07 | D6 Core/Tooling split | ✅ Soft split (Option C) + wiki companion | Rec-13 |
| 08 | UTS timing | ✅ Concurrent с D6 (Variant B) | Single source consistency |
| 09 | Contribute-back | ✅ **A — No contribution (hard)** | "всё держим, ничего никуда не отправляем, нигде не публикуем" |
| 10 | Upstream FPF sync | ✅ **Modified C — Semi-annual reminder, Ruslan manual** | "не автоматом, будут напоминания, semi-annual, держим под контролем" |
| 11 | Agent promotion CSLC | ✅ A.18 CSLC full (mandatory) | Gap 3 adoption |

**4 explicitly resolved (OQ-01, 06, 09, 10); 7 implicitly resolved через
Gaps/Recs adoption (OQ-02, 03, 04, 05, 07, 08, 11).**

#### Narrative — 4 explicit resolutions

**OQ-01 JETIX-FPF rename:**
- "FPF" → **"JETIX-FPF"** везде (D6 rename, D1/D2/D4/D5 refs updated).
- Attribution phrase explicit: "JETIX-FPF — Jetix-specific adaptation
  of First Principles Framework (FPF) by Anatoly Levenchuk
  (https://github.com/ailev/FPF) — internal Jetix use с citation;
  upstream repo has no formal license, citation requested."
- Cross-references в Chunk 1-7 retroactively read как "JETIX-FPF"
  (historical writing preserved, но ADR frontmatter + D9 v0.6 use new
  name).

**OQ-06 Model D → Nested Holonic Structure:**
- "Model D Nested Hierarchy" retired as primary term.
- Replaced by **"Nested Holonic Structure"** (FPF A.1 Holonic
  Foundation + A.14 Advanced Mereology canonical).
- D6 introduces using FPF canonical: *"Jetix uses Nested Holonic
  Structure (A.1 + A.14)"*.
- "Model D" может appear как legacy alias only (footnote где
  исторически referenced в v1/v2).
- D1, D2, D4, D5 references updated к Nested Holonic Structure primary.
- Russian lineage retired as primary terminology (consistent с OT2
  Scenario E trajectory toward EN-primary ontological layer).

**OQ-09 No contribute-back (hard internal-only):**
- Все 9 Jetix innovations (см. 8.6) remain **internal-only**.
- **No formal pull-requests, proposals, or public sharing** с ailev/FPF
  community.
- Ruslan может attend курсы Левенчука sam для own learning — no
  obligation to share back.
- Full secret sauce preservation.
- Review trigger: **none Phase 1-2** (consistent с OT5 internal-only,
  strengthened). Phase 3+ — только если publishing decision explicitly
  revisited (unlikely per current stance).

**OQ-10 Semi-annual FPF sync reminder:**
- Every 6 months (Q2 close + Q4 close) — FPF-Steward audit **flags**
  "upstream FPF sync review due".
- **Reminder only — не автоматический** fetch/apply.
- Ruslan decides когда actually sync (может быть same quarter, может
  be defer).
- Sync involves: check `github.com/ailev/FPF` main branch для delta
  since last vendor; if substantive update → re-vendor FPF-Spec.md +
  Readme.md; update ATTRIBUTION.md version; propagate changes в
  JETIX-FPF adaptation as needed.
- Not every reminder becomes actual sync (trigger-based selective).
- Added к Review Triggers (Section 10).

### 8.6 9 Innovations — internal-only preservation

Gap analysis identified **9 Jetix-originated innovations** beyond FPF
canonical patterns. Per OQ-09 A — **no public sharing, no publishing,
no community contribution.** Documented internally только для own
methodology evolution.

| # | Innovation | Category | Phase 1 Status |
|---|-----------|----------|----------------|
| 1 | Portfolio of Directions (P8 + 8-я alpha) | Strategic | ✅ Phase 1 implemented |
| 2 | 4-tier Resource Accounting (Capital + Compute + Deep Hours + Attention + Phase 3 Ecosystem) | Operational | ✅ Phase 1 ledgers live |
| 3 | 18-manifest AI-native architecture (Day 9) | Organizational | ✅ Phase 1 Day 9 implementation |
| 4 | FPF-Steward sub-role в meta-agent | Methodological | ✅ via R12 |
| 5 | Physical Life-OS ≠ Jetix separation | Architectural | ✅ Day 8 |
| 6 | DACH + US + RU unified funnel | Market | ✅ P6 adopted |
| 7 | 7+7 day rollout (sales-first) | Operational | ✅ Phase 1 plan |
| 8 | Company-as-Code + Git = SoT | Foundational | ✅ P1 core |
| 9 | Full-FPF-Permeation pattern (full text loading) | Methodological | ✅ OT5 Scenario A |

**Single internal reference artifact:**
**`wiki/foundations/jetix-innovations.md`** — живой document listing
all 9 + rationale + current implementation status + future evolution
notes. Reference-only (не active sharing). Preservation, not
publishing — innovations retained с context для own methodology
evolution.

**No review trigger Phase 1-2.** Phase 3+ publishing decision — только
если OT5 publishing revisit происходит explicitly (highly unlikely per
current stance).

### 8.7 Architectural changes summary

Key structural changes after Chunk 8 adoption.

#### Terminology

- **"FPF"** → **"JETIX-FPF"** везде (D6 rename primary; D1/D2/D4/D5
  cross-references updated)
- **"Model D Nested Hierarchy"** → **"Nested Holonic Structure"**
  (FPF A.1 + A.14 canonical); Russian lineage retired as primary
- **"FPF-Lite"** — retained as historical-alias only (legacy footnote);
  never active term
- **"Left мереологический"** legacy term — replaced в technical docs
  by A.14 typed mereology (ComponentOf / ConstituentOf / etc.)

#### New artifacts list (~20 new files/folders)

**Policy documents (9):**
- `decisions/policy/boundary-discipline.md` (Gap 1 L/A/D/E routing)
- `decisions/policy/trust-tagging.md` (Gap 2 F-G-R conventions)
- `decisions/policy/sku-pricing-chr.yaml` (Gap 3 SKU CHR)
- `decisions/policy/agent-promotion-chr.yaml` (Gap 3 promotion CHR)
- `decisions/policy/characteristic-space-conventions.md` (Gap 3
  general CSLC conventions)
- `decisions/policy/mereology-edge-types.md` (Rec-05 A.14 10 edge
  types)
- `decisions/policy/phase-transitions-mht.md` (Rec-06 4 MHTs)
- `decisions/policy/bias-audit-cycle.md` (Rec-03 D.5 cycle)
- `decisions/policy/mechanism-introduction.md` (Rec-20 E.20 protocol)

**Wiki foundations (4):**
- `wiki/foundations/jetix-uts.md` (Gap 4 UTS, 30-50 rows target)
- `wiki/foundations/fpf-tooling.md` (Rec-13 D6 companion, 10-20 pages)
- `wiki/foundations/jetix-innovations.md` (8.6 reference doc, 9
  innovations catalog)
- `wiki/foundations/jetix-creation-graph.md` (retagged A.14 typed
  edges)

**Templates (5):**
- `decisions/templates/jetix-viewpoint-bundle.yaml` (Gap 5 Viewpoint
  definitions)
- `decisions/templates/audit-canonical-template.md` + 5 views
  (`decisions/templates/views/` — executive / technical / governance /
  regulatory / internal-learning)
- `decisions/templates/client-intake-problem-chr.yaml` (Rec-16 C.22)
- `decisions/templates/kill-chr-template.yaml` (Gap 3 direction kill)
- `decisions/templates/mht-template.yaml` (Rec-06 B.2 transition)

**Directions updates (per-direction):**
- `directions/<slug>/ee-log.yaml` (Rec-07 C.19 exploration-exploitation)
- `directions/<slug>/nqd-distinctions.yaml` (Rec-07 C.18)

**Retrofits:**
- 10-15 existing ADRs get F-G-R frontmatter tags retrofit (mostly
  F1-F2 R-medium)
- `wiki/foundations/jetix-creation-graph.md` retagged с A.14 typed
  edges (5 generic → 10 typed)

#### Structural additions к frontmatter conventions

**role.md Block 5:**
- `seniority-lite` with J-Auto/Approve/Strategic — preserved (Item 7)
- `direction_authority` mapping — preserved (Item 7)

**`executor-binding.yaml` new sections:**
- `agency-profile` (Rec-08 A.13:4.3) — formal agency-scale 0.0-1.0
- `agent_onboarding` (Левенчук Part 3 — already approved Chunk 5) +
  F.6 6-step cycle (Rec-15)
- `compute-contract` (P7 override — already approved Chunk 1)

**ADR + client deliverable frontmatter (Gap 2):**
```yaml
formality: F0-F9
reliability: R-low | R-medium | R-high | R-certified | R-formally-proven
claim-scope: bounded-context-path
```

**Per-direction frontmatter (Rec-07):**
```yaml
ee-log-ref: directions/<slug>/ee-log.yaml
nqd-distinctions-ref: directions/<slug>/nqd-distinctions.yaml
```

**Wiki + clients frontmatter (Rec-10 + Gap 4):**
- `bridges-to: [context-a, context-b]` (where applicable)
- `cl-level: 1-5` (Congruence Level)

### 8.8 Updated Phase 1 work estimate

| Category | Hours |
|----------|-------|
| Previous Stage 4 writing commitment (D1-D8, Chunks 1-7) | 80-120 |
| **Post-FPF-Discovery additions (Chunk 8):** | |
| — 5 Gaps full depth | 30-45 |
| — P1 standalone recs (Rec-03 + Rec-05 + Rec-06) | 7-13 |
| — P2 recs (excluding Gap-subsumed) | 13-22 |
| — P3 recs | 8-14 |
| — First FPF-Steward Q2 audit | 2-4 |
| **Post-FPF-Discovery subtotal** | **60-98** |
| **Total Phase 1** | **140-220** |
| Realistic calendar | **3.5-5.5 weeks intensive** |

**Timeline impact:**

- **7+7 rollout** (Chunk 6 Area 8) — still valid strategic frame; Days
  1-7 sales-first execution not impacted (Gap 2/4 adoption happens Day
  5-6 в proposal/contract templates).
- **Realistic tolerance:** 7+10-14 days (slightly extended from 7+10-12
  per Chunk 6 — additional 2 days для UTS concurrent writing + CHR
  space setup + MHT documentation).
- **Parallel tracks heavier:** D6 JETIX-FPF writing (30-50 pages) +
  UTS (Gap 4, concurrent per OQ-08 B) + CHR space artifacts Gap 3 +
  Viewpoint Bundle Gap 5 + Bias-Audit Rec-03 — значительно больше
  Phase 1 cognitive load чем Chunks 1-7 alone.
- **Critical path:** D6 JETIX-FPF (Core 20-30 pages) — unblocks UTS
  concurrent write; Gap 1/2 artifacts parallel к Day 5-6 sales
  infrastructure; Gap 3 CHR spaces parallel к SKU pricing work Day 5.

### 8.9 References

**Decision artifacts:**
- Stage 3 ADR (Chunks 1-7): `decisions/2026-04-19-architecture-v2-
  approval.md` (APPROVED 2026-04-20)
- Stage 3.6 tracking file: `decisions/gap-analysis-review-decisions-
  2026-04-20.md`
- Notion mirror: <https://www.notion.so/3482496333bf8174a7ffd6f30c02f0bf>
- D9 draft v0.5: `decisions/2026-04-20-jetix-architecture-final-DRAFT.md`
  (regenerated к v0.6 same commit as Chunk 8)

**FPF source materials:**
- FPF-Spec: `raw/external/ailev-FPF/FPF-Spec.md` (62K строк, commit
  0a22129)
- Attribution: `raw/external/ailev-FPF/ATTRIBUTION.md`
- KB compilation: `raw/research/levenchuk-fpf-knowledge-base-
  2026-04-20.md` (commit 3cb5f81)
- Gap analysis: `raw/research/fpf-gap-analysis-2026-04-20.md` (2486
  строк, commit 74cf858)
- 5 Perplexity researches: `raw/research/levenchuk-fpf-research-
  2026-04-20/R-{A,B,C,D,E}.md`

**FPF patterns cited в Chunk 8 (verified against FPF-Spec.md):**
- A.1 (L.1017), A.6.0 (L.8062), A.6.B (L.7097), A.6.C (L.7741), A.6.H
  (L.15851), A.6.P (L.10601), A.6.Q (L.11326), A.6.S (L.15419),
  A.6.3.CR (L.9521), A.13 (L.17328), A.14 (L.17478), A.16 (L.18954),
  A.16.1 (L.19549), A.17 (L.20064), A.18 (L.20202), A.19 (L.20359),
  A.20 (L.24927), A.21 (L.25224), B.2 (L.27444), B.2.5 (L.28100),
  B.3 (L.28201), B.4 (L.29094), C.18 (L.37808), C.19 (L.38008), C.22
  (L.38734), D.5 (L.39964), E.5.1 (L.40589), E.5.3 (L.40743), E.10
  (L.41604), E.17 (L.45107), E.17.0 (L.43945), E.17.1 (L.44325),
  E.17.2 (L.44696), E.18 (L.47502), E.20 (L.48322), F.6 (L.50641),
  F.11 (L.52604), F.17 (L.54586), G.5 (L.58316).

---

## ✅ Chunk 8 COMPLETE 2026-04-20 — ADR FINAL CLOSED

Stage 3.6 Gap Analysis review layer absorbed. 60+ Ruslan decisions
locked (5 Gaps + 22 Recs + 11 OQs + 9 Innovations). Total Phase 1
estimate: **~140-220h (3.5-5.5 weeks intensive)**.

**Ruslan opening directive:** *"Максимальная глубина + качество, на 100%.
Никаких compromises. Всё что применимо из FPF — внедряем. Стратегический
курс как с 11 overrides — +Левенчук direction."*

**Unblocks Stage 4 with enriched single source of truth:**
- D9 Draft v0.6 (regenerated same commit) = primary input для Stage 4
  writers
- D6 JETIX-FPF (renamed) first up — Core (20-30 pages) + `wiki/
  foundations/fpf-tooling.md` companion + concurrent UTS writing

**All pending state:** NONE. ADR полностью finalized через Chunk 8.
