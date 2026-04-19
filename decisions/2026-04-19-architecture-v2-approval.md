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

#### P7 — Capital + Hours + Attention accounting + (Phase 3) Ecosystem Resources
- **Status:** ✅ APPROVED (все три ресурса Phase 1 + Ecosystem подготовка)
- **Ruslan quote:** "полностью все три подтверждаю принципа; потом ещё вот это сразу надо будет дофиксировать что ecosystem resources на потом это тоже надо будет; мы для этого тоже всё что нужно там будем подготавливать; этот принцип седьмой он будет ложиться в foundation основные"
- **Phase breakdown:**
  - Phase 1: Capital + Hours + Attention (solo, Toggl-based, discipline + 2-3 файла в `finance/` и `ops/`)
  - Phase 2: + team's hours + attention
  - Phase 3: + Ecosystem Resources (advisory, community, partnerships)
- **Infrastructure prep:** готовим инфраструктуру для Ecosystem Resources заранее (schema placeholders, не материализация)
- **Placement:** этот принцип входит в foundation основные (наравне с Company-as-Code)

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
