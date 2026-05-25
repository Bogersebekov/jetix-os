---
title: Docs Classification — что есть / что нужно / кому что показываем (Plan-of-Day Шаг 1 closure)
date: 2026-05-25
type: docs-classification-matrix
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2
G: docs-classification-2026-05-25
R: low
constitutional_posture: R1 surface only + R2 + R6 + R11 + R12 + append-only
language: russian primary
status: pool — Ruslan reads + picks final categorization / priorities; NO auto-promotion
trigger: daily-logs/_PLAN-OF-DAY-2026-05-25.md §A Шаг 1
substrate:
  - decisions/strategic/TASK-A-EXISTING-DOCS-INVENTORY-2026-05-24.md
  - decisions/strategic/PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md §6
  - reports/build-artefacts-specs-2026-05-25/02-overview-cross-map.md
  - daily-logs/_PLAN-OF-DAY-2026-05-25.md §A (pre-classification draft)
---

# 🗂️ Docs Classification — что у нас есть, что нужно ещё сделать, кому что показываем

> **Цель:** разрезать накопленный substrate по 4 категориям, чтобы каждый документ имел чёткое назначение, аудиторию и место в потоке. Каши быть не должно. Это база для Шагов 2-4 Plan-of-Day 25.05 (readiness audit / foundational needs / integrated plan).

---

## 📍 §0 TL;DR (90 секунд)

- **4 категории:** 🟢 Пояснительные (для людей наружу) / 🛠️ Шаблоны (для работы) / 📚 Substrate (глубина внутри) / ⚙️ System (инфраструктура).
- **Что есть сейчас (счёт):** ~250 strategic docs + ~750 wiki entities + 130+ tools/templates + 11 Foundation Parts + 17 ROY агентов + 80+ книг MD'd. **Хватает по объёму, не хватает по полировке per артефакт partner-facing.**
- **Главная gap'а:** партнёр-ready набор (🟢 категория) — **частично готов** (PARTNER-OFFERING + JETIX-NAVIGATION + CONSOLIDATED-HL + EXECUTION-PLAN), не хватает **видео A/B/C + лендинга + Charter v1 текста + discovery call script** (это Build артефакты 25.05 — спеки готовы Phases 0-12, теперь создавать сами).
- **Шаблоны (🛠️):** Personal OS + Team OS = **дизайн готов, реальные Notion базы не построены**. CRM + voice pipeline + Mistral OCR + Toggl = работают.
- **Substrate (📚):** 4 LOCKED canonical + 5 research deeps + 60+ книг = saturated. **Не добавляем больше.**
- **System (⚙️):** 11 Foundation Parts + Pillar A/C + 17 ROY + 9 schemas — работает. Не трогаем.
- **Кому что показываем:** только 🟢 пояснительные + relevant 🛠️ шаблоны идут наружу. 📚 substrate = depth refs для curious. ⚙️ system = internal only.
- **5-7 R1 решений** ждут тебя в §10.

---

## 🎯 §1 Цель и контекст

После Sprint 23-24.05 у нас накопилось много документов из разных слоёв. **Sustrate saturation подтверждён** (О-163 hypothesis closed). Теперь не add — теперь **organize + classify + decision**.

Без классификации каждый разговор с потенциальным партнёром = «какой документ ему дать?» + «что из него релевантно?» + «это для внутреннего пользования или нет?». Эта каша **сжигает контакты** (per Platform Lifecycle Plan §1 — «дорогие контакты сгорят на недоделанной системе»).

Классификация решает: на любой вопрос «что показать партнёру/тестеру/инвестору» — берём из категории 🟢 (+ при необходимости релевантные шаблоны 🛠️), не из 📚 substrate, никогда из ⚙️ system.

---

## 🏷️ §2 4 категории — определения

| Категория | Что это | Кому показываем | Прозрачность | Объём |
|---|---|---|---|---|
| 🟢 **Пояснительные** (explanation layer) | Plain-language тексты которые объясняют что-то конкретное человеку наружу. Без жаргона. Style anchor = PARTNER-OFFERING-HUMAN-LANG. | Партнёрам / cohort кандидатам / publicly shareable | Полная — публично можно | **~15-20 docs** |
| 🛠️ **Шаблоны работы** (operational templates) | Готовые structures чтобы человек начал работать. Notion-базы / Charter draft / discovery script / FAQ. | Internal + cohort onboarding / partner fork | Полная для fork; внутри клана = co-create | **~30-40 templates** |
| 📚 **Substrate** (depth) | Глубокий research / Foundation / методология / wiki entities. Не для чтения — для refs. | Internal только; refs для curious deep-divers (1-2 per разговор max) | Closed-by-default; selective public via curated subset | **~200+ docs + 750 wiki entities** |
| ⚙️ **System infrastructure** | Foundation Parts / Pillars / schemas / scripts / configs / agent definitions. То что заставляет систему работать. | Internal только; не показываем партнёрам | Closed | **~50 files + 130+ tools** |

**Главный принцип:** перед тем как послать партнёру/тестеру документ — **проверь категорию**. Если 📚 или ⚙️ → НЕ посылай напрямую. Возьми соответствующий 🟢 пояснительный + опционально 🛠️ шаблон.

---

## 🟢 §3 Пояснительные (explanation layer) — что есть + что нужно

### §3.1 Что есть готового

| # | Документ | Что объясняет | Audience target | Status |
|---|---|---|---|---|
| 1 | `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md` | Что мы предлагаем партнёрам (ступени L1-L7 + 75/25 + Mondragón 5:1) | T1+T3 | ✅ ready |
| 2 | `JETIX-NAVIGATION-GUIDE-2026-05-22-DRAFT.md` | Sanitized public overview (что Jetix вообще) | T1+T3+T2 | ⚠️ DRAFT — нужен polish |
| 3 | `CONSOLIDATED-HUMAN-LANGUAGE-PLAN-2026-05-24.md` | План обучения на пальцах (7 ступеней + что даём) | T3 cohort target | ✅ ready |
| 4 | `EXECUTION-PLAN-FIXATION-2026-05-24.md` | Что мы делаем + кто партнёры + sequencing | T1+T2 | ✅ ready |
| 5 | `PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md` | 3 этапа (Build/Run/Scale) + per-stage actors + R12 | T1+R12-мост (продвинутый) | ✅ ready |
| 6 | `CALL-PLAN-DMITRIY-KAISER-2026-05-25.md` | Скрипт звонка (internal — но пример формата) | Self + future call planners | ✅ ready |
| 7 | `BUILD-ARTEFACTS-SPECS-2026-05-25` (phases) | Спеки артефактов | Self | 🔄 13 phase reports, main pending |

**Итого 7 ready (5 sharable + 2 internal-ish).** Не хватает много для completeness наружу — см. gap list §3.2.

### §3.2 GAP — что нужно создать (Build блокеры)

| # | Артефакт | Spec в | Status |
|---|---|---|---|
| 1 | 🎬 **Видео A** — методология / прошивка / база | `reports/build-artefacts-specs-2026-05-25/03-video-A-spec.md` | ❌ не записано (БЛОКЕР всего Wave 1) |
| 2 | 🎬 **Видео B** — видение обучения / 7 ступеней | `.../04-video-B-spec.md` | ❌ не записано |
| 3 | 🎬 **Видео C** — экосистема / Charter / R12 / 4 партнёров | `.../05-video-C-spec.md` | ❌ не записано |
| 4 | 📜 **Charter v1 текст** | `.../08-charter-spec.md` | ❌ текст не написан (структура + R12 чек spec'нуты) |
| 5 | 🌐 **Лендинг + FAQ 10 вопросов** | `.../09-landing-faq-spec.md` | ❌ не написано (sections готовы) |
| 6 | 🗣️ **Discovery call script** | `.../10-discovery-call-spec.md` | ⚠️ есть spec — пока для Dmitriy Kaiser ad-hoc; универсальный не финал |
| 7 | 📚 **Course skeleton** (только sections, не курс end-to-end) | `.../12-supporting-materials-spec.md` §11.1 | ❌ skeleton не написан |
| 8 | 📊 **One-pager + pitch deck-light 5-7 slides** | `.../12-supporting-materials-spec.md` §11.3 | ❌ не сделано |
| 9 | 📱 **Telegram positioning + первые 5-7 постов outline** | `.../12-supporting-materials-spec.md` §11.2 | ❌ не сделано |
| 10 | 📊 **Brand-minimum** (logo / typography / 2-3 colors) | `.../12-supporting-materials-spec.md` §11.4 | ❌ не сделано |

**10 GAP'ов.** Из них **Видео A = блокер всего Wave 1**. Charter / Лендинг / Discovery call = critical параллельные. Остальное (course skeleton / one-pager / Telegram / brand) = nice-to-have для Build exit, не блокеры.

---

## 🛠️ §4 Шаблоны работы (operational templates) — что есть + что нужно

### §4.1 Что есть готового

| # | Шаблон | Назначение | Используем | Status |
|---|---|---|---|---|
| 1 | `PERSONAL-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md` | Layer 1+2 дизайн (5+ баз) | Дмитрий-trial → Сева → cohort | ⚠️ ДИЗАЙН — не implemented в Notion |
| 2 | `TEAM-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md` | Layer 3 multi-tenant + 10 ролей + marketplace | T1 partner co-design | ⚠️ ДИЗАЙН — не implemented |
| 3 | `OUTREACH-CONTENT-OUTCOMES-CTAS-2026-05-24.md` | 13 CTAs + 18 артефактов P0-P6 + 5+1 архетипов | Outreach planning + Wave 1 prep | ✅ substrate ready |
| 4 | `WAVE-1-OUTREACH-PACKAGE-2026-05-22-evening.md` | Substrate для Wave 1 рассылки | Wave 1 first send | ✅ ready |
| 5 | `CRM` система (crm/) | 180 контактов + 24 роли + 13 статусов + 10 skills | Daily contact management | ✅ работает |
| 6 | `swarm/wiki/_templates/project-*` (4 типа) | Bootstrap новых проектов | `/project-bootstrap` skill | ✅ работает |
| 7 | `crm/_templates/person.md + org.md` | CRM entry templates | `/crm-add` skill | ✅ работает |
| 8 | `decisions/strategic/_templates/` (7 templates) | Strategic Layer templates (Lock / North Star / Insight / Direction / Phase Plan / Reflection) | Strategic doc creation | ✅ работает |
| 9 | `tools/run_pipeline.sh` (voice → extract → review) | Voice notes processing pipeline | Voice batch processing | ✅ работает |
| 10 | `tools/aggregate.py` (ActivityWatch export) | Daily timeline generation | Daily logs / Toggl substrate | ✅ работает |
| 11 | Mistral OCR pipeline | Book scan → MD | 14 education books + 11 raw books processed | ✅ работает |
| 12 | Toggl push pipeline | Time entries → API | Daily logging | ✅ работает |

**12 рабочих шаблонов.** + ~130+ tools/templates (mini-shaped) из Task A inventory.

### §4.2 GAP — что нужно создать

| # | Шаблон | Status |
|---|---|---|
| 1 | **Notion Personal OS — 5 баз implementation** (реально построенные базы, не дизайн) | ❌ Week 1-2 per Platform Lifecycle |
| 2 | **Notion Team OS demo overlay** (для 1 партнёра — Maxim или Oleg) | ❌ Week 2-3 |
| 3 | **Charter v1 text** (после spec + после R12 Прапион ревью) | ❌ Week 2-3 |
| 4 | **Discovery call script универсальный** (текущий = для Dmitriy Kaiser ad-hoc) | ❌ Week 2 |
| 5 | **Контракт template** (partner agreement minimum — fork-and-leave + 30-day + asset retrieval) | ❌ Week 3 |
| 6 | **Invoice template SEPA-ready + bookkeeping минимум** | ❌ Week 2 (после Steuerberater) |
| 7 | **Steuerberater email template** | ❌ Week 1 |
| 8 | **Course skeleton** (table of contents с Bloom 1-7 mapping) | ❌ Week 2-3 |
| 9 | **FAQ 10 вопросов** (placeholder заполняется после Discovery звонков) | ⚠️ structure готова, content fills after Дмитрий + Maxim + Oleg калиброваны |

---

## 📚 §5 Substrate (depth) — что есть (НЕ добавляем, только classify)

### §5.1 Главные substrate группы

| Группа | Где | Объём | Используется как |
|---|---|---|---|
| **4 LOCKED canonical** | `decisions/strategic/METHOD-LIFE-DEVELOPMENT-V2 + STRATEGIC-PLAN-NEAR-FUTURE + ECONOMIC-MODEL-TOKENOMICS + AI-MARKET-ELECTRICITY-ANALOGY-PLAN` | ~120K combined | Reference для 🟢 пояснительных + Foundation |
| **5 Research deeps May 2026** | `decisions/strategic/RESEARCH-{METHODOLOGY,SOTA,PROPAGANDA-RECRUITMENT,NLP,EDUCATION} + LEVENCHUK-MASTER-QUALIFICATION-RESEARCH` | ~150K combined + 85 sub-deliverables | Substrate для R12 + методологии + ed |
| **Sprint 21-24.05 strategic** | DEVELOPMENT-PLAN / EXPERTS-PACK / QUESTIONS-PACK / TASKS-PACK / DISTRIBUTION-PLAN / RECURSIVE-PARTNERSHIP-MECHANICS / TRIPLE-ROLE-PARTNER / TOKENOMICS-VARIANTS / DR-38 / DR-40 / META-METHOD-8-COMPONENT-DEEP / EXTERNAL-SYSTEM-PRINCIPLE-DEEP / META-METHOD / ONE-PAGER-FPF | ~30 docs | Подложка к 4 LOCKED |
| **JETIX-ETHEREUM architecture** | `decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/` (12 sub-docs + 5 diagrams) | ~80K | Phase 2+ R12 programmable substrate |
| **POINT-A / POINT-B** | `POINT-A-CURRENT-STATE-2026-05-23 + POINT-B-NEAR-TARGET-2026-05-23 + POINT-B-FOCUSED-WEEK-1` | ~50K | Где мы / куда идём |
| **JETIX-AS-X conceptual hubs** | JETIX-AS-HACKATHON-PLATFORM / EDUCATION-LAYER / OUTREACH-SYSTEM / RECURSIVE-SELF-DEVELOPMENT / SYSTEM-MERGER-PROTOCOL-FPF (6 docs from 18.05) | ~60K | Insight library |
| **29 D-LOCK entries** | `decisions/strategic/lock-entries/D-01..D-29.md` | ~50K | Fundamental decisions log |
| **7 Strategic Insights** | `decisions/strategic/strategic-insights/` (4) + `decisions/STRATEGIC-INSIGHT-*` (3) | ~30K | Concept anchors |
| **Wiki concepts Tier A/B-Plus** | `wiki/concepts/` (62+ Tier A/B-Plus from sprint 23-24) | 200+ entities | Lookup library |
| **Wiki ideas / sources / topic-hubs** | `wiki/ideas/` (272) + `wiki/sources/` (276) + 7 topic hubs | 555+ entities | Append-only knowledge net |
| **80+ books MD'd** | `inbox/` + `inbox-reocr/` + `raw/external/research-corpus-2026-05-23/` + `raw/external/levenchuk-books-2026-05-20/` + `raw/external/research-corpus-2026-05-23/education/` | Multi-GB | Raw substrate for further research |
| **Voice notes verbatim** | `decisions/strategic/RUSLAN-NOTES-EDUCATION-PARADIGM-2026-05-24.md` + audio_* transcripts | ~50 voice batches | Substrate anchor (F2) |
| **AWAITING-APPROVAL packets** | `swarm/awaiting-approval/` (14 packets) | ~40K | Acked decisions traceability |

**Итого:** ~200+ substrate docs + 750+ wiki entities + 80+ books.

**Правило substrate:** не показываем партнёрам сразу. Если разговор уходит в глубину — даём **1-2 specific cross-refs** в footnote стиле («если хочешь глубже — посмотри Method V2 §J»), не вываливаем кучу.

### §5.2 Substrate анти-паттерны

- ❌ Отправить новому партнёру 4 LOCKED canonical «вот почитай» — он закроется через 5 минут
- ❌ Дать ссылку на JETIX-ETHEREUM-ARCHITECTURE до Build exit — это Scale-материал, для Build = noise
- ❌ Делиться raw voice notes / 80+ книгами / wiki concepts — это depth для нас, не для них
- ❌ Линковать на D-LOCK entries в первом разговоре — appears как «у нас закрытый клуб с своими правилами»

---

## ⚙️ §6 System infrastructure — что есть (НЕ трогаем)

| # | Слой | Где | Status |
|---|---|---|---|
| 1 | **11 Foundation Parts F5 LOCKED** | `swarm/wiki/foundations/part-1..10 + part-11-strategic-direction-substrate/` | 🔒 LOCKED 2026-04-28, untouched |
| 2 | **Pillar C principles** | `principles/tier-1-manager/ + tier-2-system/ + foundation-generic/ + ruslan-layer-overrides/` (27 files) | 🔒 LOCKED |
| 3 | **9 F8 schemas** | `shared/schemas/` (f-g-r / default-deny / blast-radius / AWAITING-APPROVAL / Halt-Log-Alert / Corrigibility / message v2 / task / briefing) | 🔒 LOCKED |
| 4 | **17 ROY agents** | `.claude/agents/` (brigadier + 5 ROY + 3 mini-swarm + 8 book-driven) | ✅ Active per CLAUDE.md |
| 5 | **routing-table.yaml** | `swarm/lib/routing-table.yaml` (29 role entries + 4 R12 auto-pair rules) | ✅ Active |
| 6 | **shared-protocols + hooks** | `swarm/lib/shared-protocols.md + swarm/lib/hooks/` (pre-commit + cycle) | ✅ Active |
| 7 | **54 Skills** | `.claude/skills/` (12 wiki / 4 day / 6 KM / 10 CRM / 11 hypothesis / 4 mermaid / 3 misc / 8 lint sub) | ✅ Active |
| 8 | **30+ tools/scripts** | `tools/` (Python + shell — transcribe / extract / filter / aggregate / run_pipeline / etc.) | ✅ Active |
| 9 | **`.claude/config/*.yaml`** | project-types / wiki-roots / sg-banned-phrases / default-deny-table | 🔒 Foundation reference |
| 10 | **CLAUDE.md** | Корень — Master Configuration | 🔒 LOCKED structure |

**Анти-паттерн:** показывать партнёру что у нас FPF / Pillar C / Halt-Log-Alert / R12 4 RUSLAN-LAYER action classes / Default-Deny-Table — это значит сразу выглядеть как **закрытый секта-tier клуб с своим жаргоном**. Внутренний слой не уходит наружу.

---

## 👥 §7 Кому что показываем (matrix по этапам и партнёр-типам)

> Cross-reference per Platform Lifecycle Plan §4 actor matrix.

### §7.1 Audience × Category матрица

| | 🟢 Пояснительные | 🛠️ Шаблоны | 📚 Substrate | ⚙️ System |
|---|---|---|---|---|
| **T1 Методолог (Maxim/Oleg/Левенчук)** ⭐⭐⭐ | ✅ PARTNER-OFFERING + EXECUTION-PLAN + PLATFORM-LIFECYCLE + видео A/C | ✅ Charter draft + course skeleton + discovery script | ⚠️ Selective (Method V2 §J + lev-master Phase 7) | ❌ Никогда |
| **T1 R12-мост (Прапион)** ⭐⭐ | ✅ EXECUTION-PLAN §4 R12 + видео C + PARTNER-OFFERING | ✅ Charter draft (primary ревью target) | ⚠️ Selective (R12 packets + Economic V10 §11) | ❌ Никогда |
| **T3 Smart тестер (Дмитрий, Сева)** ⭐⭐⭐ | ✅ CONSOLIDATED-HL + PARTNER-OFFERING + видео B + лендинг | ✅ Personal OS template (Дмитрий-trial) | ⚠️ Selective (RUSLAN-NOTES-ED + Method V2 §J) | ❌ Никогда |
| **T1 Engineer-tier (Karpathy, Vitalik)** | ✅ ONE-PAGER-FPF + JETIX-NAVIGATION-GUIDE + видео A | ⚠️ Только если они спросят (Charter + tech architecture) | ⚠️ Selective (Method V2 + Ethereum architecture для Vitalik) | ❌ Никогда |
| **T2 Ресурсы (capital / audience)** | ✅ JETIX-NAVIGATION + EXECUTION-PLAN | ❌ Шаблоны не нужны (не co-create) | ❌ Не нужно | ❌ Никогда |
| **T3 Когорта members (Run stage)** | ✅ CONSOLIDATED-HL + видео A/B + Charter подписанный | ✅ Personal OS template + course materials | ⚠️ Selective on request | ❌ Никогда |
| **Mass audience (Scale stage)** | ✅ JETIX-NAVIGATION + видео B (paradigm shift) + лендинг | ⚠️ Public-fork only Personal OS | ❌ Не нужно | ❌ Никогда |

### §7.2 Канал × что отправляем

| Канал | Default отправка | Cap |
|---|---|---|
| **Cold email Wave 1** | Видео A link + PARTNER-OFFERING-HL + 1-paragraph intro | ≤500w письмо |
| **Discovery call follow-up** | EXECUTION-PLAN + Charter draft + PLATFORM-LIFECYCLE link | ≤3 ссылки |
| **Telegram канал** | JETIX-NAVIGATION + видео B (когда готово) | Без overwhelm |
| **Лендинг** | Embed видео A + ссылки на PARTNER-OFFERING + 1 CTA | Single page primary |
| **Прапион ревью** | Charter draft + Economic V10 §11 R12 + packet R12-12th-rule | Polished package |

---

## 🚨 §8 GAP list (приоритезированно) — что нужно ещё создать

### §8.1 P1 critical (без них Build exit не пройдём)

1. ❌ **Видео A** — methodology / прошивка (БЛОКЕР всего Wave 1)
2. ❌ **Notion Personal OS implementation** — 5 баз real, для Дмитрий-trial
3. ❌ **Charter v1 текст** — Прапион не сможет ревьюить spec, нужен реальный текст
4. ❌ **Discovery call script универсальный** (Dmitriy Kaiser = ad-hoc, нужен общий)
5. ❌ **Лендинг + FAQ 10 вопросов** (FAQ структура готова, content fills after first calls)
6. ❌ **Steuerberater email** + Einzel/GmbH/UG матрица — без юр Build exit неполный
7. ❌ **Бизнес-счёт** открыт + invoice template

### §8.2 P2 important (нужны для Run readiness)

8. ❌ **Видео B** — видение обучения / 7 ступеней
9. ❌ **Видео C** — экосистема / Charter / R12
10. ❌ **Notion Team OS demo overlay** (для T1 партнёр co-design)
11. ❌ **Контракт template** (partner agreement)
12. ❌ **Course skeleton** (table of contents)
13. ❌ **JETIX-NAVIGATION-GUIDE polish** (статус DRAFT → ready)

### §8.3 P3 nice-to-have (Build exit ОК без, до Run желательно)

14. ❌ **One-pager** + pitch deck-light 5-7 slides
15. ❌ **Telegram positioning + первые 5-7 постов outline**
16. ❌ **Brand-minimum** (logo / typography / colors)
17. ❌ **edu-agent execution prompt** (Option A acked но executor не создан)
18. ❌ **ABC execution prompts** (Plan B docs / Plan A video / Plan C Notion — Cloud Cowork side)
19. ❌ **Phase 13 Build Artefacts Specs main consolidated** (server CC бросил)

### §8.4 Decision-pending (НЕ создаём пока)

- ⏸️ Полный course end-to-end (это Run stage — пишет T1 партнёр когда придёт)
- ⏸️ Multi-tenant Notion implementation (Scale stage)
- ⏸️ Смарт-контракты R12 enforcement (Phase 2+)
- ⏸️ Wave 1 outreach actual sends (Week 2-3 после артефактов)

---

## ⚠️ §9 Анти-паттерны при показе документов

- ❌ Послать новому партнёру 5+ ссылок — overwhelm, закрывается
- ❌ Дать substrate (4 LOCKED / research deeps) до того как партнёр прочитал 🟢 пояснительные — выглядит как «у нас всё сложно, не для тебя»
- ❌ Линковать на 📚 без context («вот наш Method V2, почитай») — substrate работает только с framing из 🟢
- ❌ Показывать ⚙️ system (Foundation Parts / R12 4 action classes / Halt-Log-Alert) первый раз — выглядит как закрытый секта-tier клуб
- ❌ Отправлять DRAFT документы как final (JETIX-NAVIGATION-GUIDE-DRAFT — нужен polish первым)
- ❌ Mixing категорий в одном сообщении («вот наш PARTNER-OFFERING + Foundation Part 6b + voice notes за 24.05») — каша
- ❌ Дать партнёру всё «чтобы выбрал что важно» — это shifting cognitive load на него, F4 R12 violation в смягчённой форме

---

## 📊 §10 Status snapshot — где мы сейчас по Build readiness

| Слой | Готовность Build exit | Что блокирует |
|---|---|---|
| 🟢 Пояснительные | **60%** | Видео A/B/C + лендинг + полированный JETIX-NAVIGATION-GUIDE |
| 🛠️ Шаблоны | **40%** | Notion Personal OS implementation + Charter text + discovery script + контракт + invoice |
| 📚 Substrate | **95%** | Можно остановить накопление (saturation подтверждён) |
| ⚙️ System | **95%** | Phase 13 Build Specs main + Notion Team plan upgrade decision |

**Аггрегат:** ~70% Build readiness. До exit нужно закрыть Видео A + Charter text + Personal OS implementation + Steuerberater email + лендинг.

---

## ✅ §11 R1 решения для тебя (5-7)

1. **Pre-classification из §A Plan-of-Day подтверждаем?** Категории и mapping ОК или есть правки?
2. **Приоритеты GAP'ов** — P1/P2/P3 как surface здесь, или другой order? (Особенно: Видео A first vs Notion Personal OS first?)
3. **JETIX-NAVIGATION-GUIDE polish** — кто пишет polish и когда? (DRAFT → ready)
4. **Phase 13 Build Artefacts Specs main** — server CC бросил, рестартим автономный prompt или Cloud Cowork собирает быстро?
5. **Кому-что-показывать matrix** §7.1 — добавить / изменить partner types?
6. **Каналы дистрибуции** §7.2 — лендинг hosting (Notion public / Webflow / static HTML)?
7. **Course end-to-end** vs **course skeleton** — solidify Build = только skeleton, end-to-end = Run partner-driven?

---

## 🔗 §12 Cross-refs (substrate which fed this)

| Документ | Зачем |
|---|---|
| `decisions/strategic/TASK-A-EXISTING-DOCS-INVENTORY-2026-05-24.md` | Inventory baseline (~250 strategic + 750 wiki + 130+ tools) |
| `decisions/strategic/PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md` §6 | Documents matrix Build/Run/Scale baseline |
| `daily-logs/_PLAN-OF-DAY-2026-05-25.md` §A | Pre-classification draft 4 категории |
| `reports/build-artefacts-specs-2026-05-25/02-overview-cross-map.md` | Build артефакты cross-map |
| `reports/build-artefacts-specs-2026-05-25/13-dependencies-risks.md` | Build артефакт dependencies |
| `decisions/strategic/EXECUTION-PLAN-FIXATION-2026-05-24.md` §4 | 4 типа партнёров (T1-T4) baseline |
| `CLAUDE.md` `## Source of Truth` + Foundation Architecture | System infrastructure canonical |
| `decisions/strategic/PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md` | Style anchor для 🟢 категории |

---

## 🎯 §13 К чему ведёт (что разблокирует после твоего ack)

После того как ты прочитаешь + acked этот документ:

1. **Чёткий понимание что где** — для любого нового разговора с партнёром знаешь категорию каждого документа → не смешиваешь / не отдаёшь internal substrate
2. **GAP list = roadmap Build closing** — 7 P1 артефактов = следующая неделя priority
3. **Кому-что-показывать matrix** — pre-call prep ≤2 минут (по типу партнёра берёшь applicable docs)
4. **Шаг 2 Plan-of-Day разблокирован** — readiness audit может использовать эту classification как baseline
5. **Шаг 3 + 4 Plan-of-Day** — foundational needs + integrated plan строятся поверх этого

---

*Document closure 2026-05-25. Docs Classification — 4 категории mapping (🟢/🛠️/📚/⚙️) + GAP list 19 missing artefacts (7 P1 + 6 P2 + 6 P3) + audience × category matrix + анти-паттерны + Build readiness 70%. R1 surface only — ты picks final priorities + categorization adjustments. Pool result — следующие шаги (readiness audit / foundational needs / integrated plan) после твоего ack.*
