---
title: Phase 10 — GAP mapping (существующее vs missing)
date: 2026-05-25
type: phase-report
phase: 10
parent_prompt: prompts/jetix-full-map-and-docs-skeleton-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F3
G: jetix-full-map-and-docs-skeleton-phase-10
constitutional_posture: R1 surface only + R6 + R11 + append-only
language: russian primary
---

# 📊 Phase 10 — Что есть vs чего нет (GAP-маппинг)

> **Что это.** По всем 94 документам из Phase 9 — явный маппинг: ✅ существует (путь) /
> ⚠️ частично (путь + что не закрыто) / ❌ отсутствует. Плюс суммарный GAP по категориям и
> сверка с DOCS-CLASSIFICATION § GAP (19 missing артефактов).

---

## §0 TL;DR

- **94 документа: 36 ✅ / 25 ⚠️ / 33 ❌.** Полностью или частично закрыто 65% (61 из 94).
- **Главный паттерн:** глубина и инфраструктура закрыты (Research 100% есть/частично,
  Risk/Compliance 86%, Partner-facing 78%); **outward и operational-новое — дыры**
  (Brand 0 ✅, Financial 5 ❌, Community/Cohort 4 ❌, Legal 5 ❌).
- **Сверка с DOCS-CLASSIFICATION:** их 19 GAP'ов = подмножество наших 33 ❌ + 25 ⚠️
  (наша карта шире — добавила HR/People, Risk register, IP licensing, DAO docs).
- **Build-критичные ❌:** видео A/B/C · Charter текст · Notion implement · лендинг/FAQ ·
  discovery script универсальный · Steuerberater/invoice/бизнес-счёт.

---

## §1 ✅ Существует (36 docs — путь подтверждён)

| Doc | Путь |
|---|---|
| Vision/North Star | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` |
| Strategic Plan | `decisions/strategic/STRATEGIC-PLAN-NEAR-FUTURE-2026-05-21.md` 🔒 |
| Execution Plan | `decisions/strategic/EXECUTION-PLAN-FIXATION-2026-05-24.md` |
| Point A/B | `decisions/strategic/POINT-A-CURRENT-STATE` + `POINT-B-*` |
| Method canonical V2 | `decisions/strategic/METHOD-LIFE-DEVELOPMENT-V2-2026-05-21.md` 🔒 |
| Meta-method reference | `decisions/strategic/META-METHOD-8-COMPONENT-DEEP-2026-05-22.md` |
| FPF technical spec | `design/JETIX-FPF.md` 🔒 |
| Hypothesis Architecture | `.claude/skills/hypothesis-*` + wiki concepts |
| Architecture diagrams | Foundation Parts + `TASK-A-*` mermaid |
| Changelog | git log + `wiki/log.md` |
| Cohort target ontology | `wiki/concepts/cohort-target-profile-ontology.md` |
| Economic model V10 | `decisions/strategic/ECONOMIC-MODEL-TOKENOMICS-2026-05-22.md` 🔒 |
| Revenue model (HL) | `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md` |
| Distribution policy | Economic V10 + `TRIPLE-ROLE-PARTNER` |
| Stage Gate records | Part 7 + `/lint --check-stage-gates` |
| AWAITING-APPROVAL packets | `swarm/awaiting-approval/` (14) |
| Research deeps (5) | `decisions/strategic/RESEARCH-*` + `LEVENCHUK-MASTER-*` |
| Wiki KB | `wiki/` (750+ entities, 909 edges) |
| Book corpus | `raw/books-md/` (25 cat) + research-corpus |
| Knowledge diff | `/knowledge-diff` skill |
| Canonical INDEX | `canonical/INDEX.md` |
| Partner offering | `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md` |
| Revenue share spec | `TRIPLE-ROLE-PARTNER` + Economic |
| Triple-role explainer | `decisions/strategic/TRIPLE-ROLE-PARTNER-2026-05-22.md` |
| Outreach package | `OUTREACH-CONTENT-OUTCOMES-CTAS` + `WAVE-1-PACKAGE` |
| Per-tier offer matrix | `EXECUTION-PLAN-FIXATION` §4 |
| Call plan (example) | `CALL-PLAN-DMITRIY-KAISER-2026-05-25.md` |
| CRM | `crm/` |
| Sales pipeline | CRM pipeline statuses |
| Ops cadence | `/plan-day` + `/close-day` + `/company-status` |
| Time-tracking | Toggl + `/log-time` |
| Role definitions | Part 4 + ROY agent defs |
| People principles Tier 1 | Pillar C Tier 1 |
| R12 compliance log | `swarm/approvals/log.jsonl` |
| Default-deny table | `.claude/config/default-deny-table.yaml` 🔒 |
| Safety/governance framework | Part 6b + Pillar C |
| Audit trail | git + Part 6a |

---

## §2 ⚠️ Частично (25 docs — есть, но не закрыто полностью)

| Doc | Где есть | Что не закрыто |
|---|---|---|
| Decisions log (strategic) | 29 D-LOCK | scaffold-pending-review (Wave 1.4 не завершён) |
| Method canonical (HL) | CONSOLIDATED-HL | видео A не записано |
| SOPs методологические | в Method V2 | не выделены как отдельный SOP-doc |
| Product roadmap | Platform Lifecycle | не отдельный roadmap-артефакт |
| Personal OS spec | дизайн готов | Notion базы не построены (implement) |
| Team OS spec | дизайн готов | не implemented |
| Workshop format | в Education docs | не отдельный self-contained spec |
| API/template docs | CLAUDE.md + skills | не адаптировано для cohort |
| Membership terms per-tier | PARTNER-OFFERING | не как отдельный per-tier doc |
| Anti-cult/R12 discipline | OUTREACH Anti-CTA | не отдельный self-contained doc |
| Community cast | D-07 | scaffold-pending |
| Pricing sheet | RESEARCH-EDUCATION §5 | не live Notion/sheet |
| Steward decisions log | AWAITING-APPROVAL log | не выделенный Steward-лог |
| DAO governance docs | JETIX-ETHEREUM bundle | Phase 2+ (не активно) |
| Messaging guide | OUTREACH-CONTENT | не отдельный brand-asset |
| One-pager | ONE-PAGER-FPF | technical, не human-facing |
| Experiments log | wiki entity type | мало записей |
| Research portfolio | в каждом deep § | не сводный обзор |
| Discovery call script | ad-hoc (Dmitriy) | универсальный не сделан |
| Outreach materials | OUTREACH-CONTENT | не per-channel templates |
| Contact research templates | skills + crm | не формализовано |
| Team OS roles (10) | TEAM-OS-PLAN дизайн | не implemented |
| Risk register | в планах §risks | не сводный реестр |
| R12 paired-frame checklist | EXECUTION-PLAN | не reusable template |
| Per-tier offer (detail) | EXECUTION-PLAN §4 | детализация per-tier pending |

---

## §3 ❌ Отсутствует (33 docs — нужно создать)

**Build-критичные (P0/P1):**
- 🎬 Видео A (методология/прошивка) — **блокер #1**
- 🎬 Видео B (видение обучения)
- 🎬 Видео C (экосистема/Charter/R12/партнёры)
- 📜 Charter v1 текст
- 📜 Charter legal version
- 🗂️ Personal OS implementation (5 баз real)
- 🌐 Лендинг (контент)
- 🌐 FAQ 10 вопросов (контент)
- 🗣️ Discovery call script универсальный
- ⚖️ Legal entity docs (Einzel/GmbH/UG)
- 💰 Invoice template
- 💰 Contract template (client)
- 💰 Bookkeeping minimum
- 💰 Budget/runway live sheet
- 🤝 Partner agreement template
- 🤝 Partner onboarding

**Run-важные (P2):**
- 📜 Master Plan public
- 🎯 OKR/quarterly
- 👥 Community guidelines / Code of Conduct
- 👥 Onboarding guide (cohort)
- 👥 Mentor matrix
- 👥 Cohort calendar
- 🎨 Brand book
- 🎨 Pitch deck light
- 🎨 Website content
- 📱 Telegram positioning + posts
- 📊 Customer success/support docs
- 🎯 Hiring docs
- 🎯 Performance review framework
- 🎯 Compensation structure

**Scale / Phase 2+ (P3-P4):**
- 📜 Annual review/letter (рано)
- 🧪 IP licensing terms + agreement
- 🎯 Worker-owner handbook
- 🚨 Privacy/data policy

---

## §4 GAP по категориям

```
📜 Executive       ████████░░ 75% закрыто (6/8)
🧪 Methodology/IP  ██████████ 86% (6/7)
🏗️ Platform        ███████░░░ 75% (6/8)
👥 Community       █████░░░░░ 56% (5/9)  ← дыра
💰 Financial       ████░░░░░░ 38% (3/8)  ← дыра
⚖️ Legal           ████░░░░░░ 44% (4/9)  ← дыра
🎨 Brand           ███░░░░░░░ 25% (2/8)  ← главная дыра
🔬 Research        ██████████ 100% (7/7)
🤝 Partner-facing  ████████░░ 78% (7/9)
📊 Operational     ████████░░ 86% (6/7)
🎯 HR/People       ████░░░░░░ 43% (3/7)  ← дыра
🚨 Risk/Compliance █████████░ 86% (6/7)
```

**5 категорий-дыр:** Brand (25%) · Financial (38%) · HR/People (43%) · Legal (44%) ·
Community (56%). Всё остальное ≥75%.

---

## §5 Сверка с DOCS-CLASSIFICATION § GAP (19 артефактов)

DOCS-CLASSIFICATION §8 surface'нул 19 missing артефактов (7 P1 + 6 P2 + 6 P3). Все они
**входят** в наши 33 ❌ + 25 ⚠️. Соответствие:

| DOCS-CLASS GAP | Наш статус |
|---|---|
| Видео A/B/C | ❌ (3 docs) |
| Notion Personal OS implement | ⚠️→❌ implement |
| Charter v1 текст | ❌ |
| Discovery script универсальный | ⚠️→❌ |
| Лендинг + FAQ | ❌ (2) |
| Steuerberater email + entity | ❌ (legal entity) |
| Бизнес-счёт + invoice | ❌ (invoice) |
| Контракт template | ❌ |
| Course skeleton | ⚠️ (Workshop spec) |
| One-pager + pitch deck | ⚠️ + ❌ |
| Telegram positioning | ❌ |
| Brand-minimum | ❌ (brand book) |
| Team OS demo | ⚠️ |
| JETIX-NAVIGATION polish | ⚠️ (DRAFT) |

**Наша карта шире:** добавили категории, которых не было в 19-GAP DOCS-CLASSIFICATION —
HR/People (hiring/performance/comp/worker-handbook), Legal (entity/IP licensing/DAO/privacy),
Risk (register/privacy), Financial (budget sheet/bookkeeping). Это «вторая волна» дыр,
видимая только при полном corporate-doc skeleton.

---

## §6 Главный вывод GAP

Дыры **не равномерны** — они кластеризуются в **двух зонах**:
1. **Outward Build-слой** (Brand / Partner-facing новое / Community onboarding) — то, что
   блокирует выход к людям СЕЙЧАС. Держится на видео A.
2. **Corporate-infrastructure будущего** (HR / Legal entity / Financial ops) — то, что
   понадобится при найме + легализации (Run). Не блокер Build, но «вторая волна».

Глубина (Research/Methodology) и защита (Risk/R12) — закрыты. **Мы не недоинвестировали в
понимание — мы недоинвестировали в упаковку наружу и в operational-инфраструктуру роста.**

---

*Phase 10 closure. 94 docs: 36 ✅ / 25 ⚠️ / 33 ❌. GAP по 12 категориям (5 дыр: Brand/
Financial/HR/Legal/Community). Сверка с DOCS-CLASSIFICATION 19-GAP (подмножество наших).
Главный вывод: дыры = upward-упаковка + operational-рост, не глубина. R1 surface.*
