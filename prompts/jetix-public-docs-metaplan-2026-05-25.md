---
title: Jetix Public Docs MetaPlan — варианты skeleton основных публичных документов по направлениям
date: 2026-05-25
type: server-cc-autonomous-prompt
prompt_class: strategic-synthesis-metaplan-public-docs
output_main_doc: decisions/strategic/JETIX-PUBLIC-DOCS-METAPLAN-2026-05-25.md
output_reports_dir: reports/jetix-public-docs-metaplan-2026-05-25/
F: F2-F3
G: prompt-jetix-public-docs-metaplan-2026-05-25
R: refuted_if_legal_or_financial_included_OR_research_raw_pushed_to_public_OR_lt_2_variants_OR_lt_3_mermaid_OR_LOCK_modified_OR_sample_doc_content_OR_auto_launch_consequent_OR_over_engineered
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only
roy_dispatch_target: brigadier + mgmt-expert + methodology-engineer + nlp-expert (R12 framing check) + propaganda-expert (R12 audience) + sota-tracker-expert (reference public info architectures)
language: russian primary
style_anchor: PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md + EXECUTION-PLAN-FIXATION-2026-05-24.md + PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md
mode: METAPLAN VARIANTS (skeleton level — НЕ собираем сами документы, только surface 2-3 варианта structure)
mermaid_target: 3-5 schemes META-1..META-5
status: READY-TO-EXECUTE
runtime_target: 2-3h autonomous (light run — метаплан, не deep content)
audience_primary: Ruslan reads → picks вариант → отдельный prompt позже на actual filling
---

# 🗂️ Jetix Public Docs MetaPlan — варианты верхнеуровневого skeleton

## §0 КРИТИЧНО — что делаем и НЕ делаем

### ✅ ЧТО делаем (фокус):

**Surface 2-3 варианта** verхнеуровневой структуры — **как разбить накопленное по направлениям**, чтобы:
1. Партнёр с нуля за 5-15 минут понимал что Jetix
2. Можно было быстро PDF / Notion / лендинг expose
3. Каждое направление = свой главный документ + дополнительные страницы
4. Логично читается «сверху вниз»

**Per variant:**
- Список направлений (3-6 в варианте)
- Per направление — главный документ + поддерживающие
- Откуда substrate тянем (из 94 docs Phase 9 jetix-map)
- Narrative sequence (в каком порядке партнёр читает)
- Pros / Cons

### ⛔ ЧТО НЕ делаем (deferred per Ruslan voice 25.05 evening):

- ❌ **Legal documents** — defer (потом найдём специалистов)
- ❌ **Financial documents** — defer (потом найдём специалистов)
- ❌ **Research raw** — никому наружу не показываем (пусть лежит internal)
- ❌ **Brand book / pitch deck / one-pager** — defer на сегодняшний вечер (отдельная задача)
- ❌ **Сами документы** — НЕ собираем сейчас (только metaплан structure)
- ❌ **Over-engineered Notion-implementation specs** — это параллельный run (`notion-arch-v2`)
- ❌ **Sample content в документах** — только skeleton

### 🎯 Focus directions (per Ruslan):

- 🧪 **Метод / Методология** — главный фокус (включая образование / прошивку)
- 🚀 **Платформа** + продукт + Notion templates + Community
- 💼 **Бизнес** — направление компании + как работает + Operational
- 💰 **Заработок** — модели заработка (но не финансовая отчётность — это другое)
- 👥 **Команда / Партнёры** — кого ищем / как работаем
- 🎯 **Видение / Стратегия** — куда идём + зачем

---

## §17.0 ⭐ MAX-density (FOR VARIANTS QUALITY)

ROY 500% — focus на качество вариантов + alternative analysis. НЕ density per direction page (метаплан — light), но density per **вариант comparison + recommended path rationale**.

1. ROY swarm full dispatch для discussion вариантов
2. MAX tokens для variants + comparisons + sequencing analysis
3. Read FULL jetix-map output (Phase 9 docs list + Phase 10 GAP + Phase 13 master skeleton) + DOCS-CLASSIFICATION + Platform Lifecycle + Execution Plan
4. Concrete examples per variant — какой документ куда попадает + worked example «партнёр читает A → B → C»
5. NOT stopover — surface больше variants если applicable (3 = base, 4-5 OK если value adds)

---

## §1 Контекст и роль

Ты — **brigadier-scribe**. Задача: на основе jetix-map Phase 9 (94 documents в 12 категориях) + DOCS-CLASSIFICATION (4 категории) + jetix-map Phase 13 (master skeleton — 4 super-кластера + 5 cross-cutting) **surface 2-3 варианта verхнеуровневой публичной структуры** документов Jetix.

**Это metaплан, не collection.** На выходе — карта «куда какой документ идёт» + sequencing narrative + recommendation.

После твоего ack — отдельный prompt на actual filling по выбранному варианту (это **next iteration**, не в этом run'е).

**Constitutional posture STRICT** — см. §6.

---

## §2 Phases (8 phases, light)

### Phase 0 — Substrate read + filter principles

**Tasks:**
- Read FULL: jetix-map main + Phase 9 (94 docs) + Phase 10 (GAP) + Phase 13 (master skeleton) + DOCS-CLASSIFICATION + Platform Lifecycle + Execution Plan + Partner Offering HL
- Define **filter principles:** что входит в публичный скоп / что нет
  - ✅ In: Метод / Платформа / Бизнес / Заработок (модели на пальцах) / Команда / Видение / Партнёрство
  - ❌ Out: Legal docs (defer) / Financial reporting (defer) / Research raw (internal) / Brand assets (separate next session) / Foundation infrastructure (internal)
- Define **audience persona:** умный партнёр (T1 / T3 smart / R12-мост) с нуля за 5-15 мин

**Output:** `reports/jetix-public-docs-metaplan-2026-05-25/01-substrate-filter.md` (~1-1.5K)
**Commit:** `[metaplan] Phase 0 substrate + filter principles`

---

### Phase 1 — Reference public information architectures (что у других)

**Tasks:**
- Quick scan 5-7 reference public sites:
  - **Anthropic** (Research / Products / Use cases / Company / Policy)
  - **Tesla** (Master Plan / Models / Energy / Charging)
  - **Apple** (Mac / iPhone / Services / Support / About)
  - **OpenAI** (Research / Products / Safety / Company)
  - **Mondragón** (About / Cooperative experience / Sectors / Knowledge)
  - **John Lewis** (About us / Partnership / Our brands)
  - **Stripe** (Products / Solutions / Developers / Resources / Company)
- Extract: сколько top-level разделов / какая логика разбиения / какой narrative flow / public vs gated split

**Output:** `.../02-reference-public-architectures.md` (~1.5-2K)
**Commit:** `[metaplan] Phase 1 reference public architectures`

---

### Phase 2 — Generate 2-3 variants of public docs structure

**Tasks — surface 3 варианта minimum:**

#### Variant A — «По направлениям бизнеса» (по entities)
Структура по 5-6 direction groups:
- 🧪 Метод
- 🚀 Платформа (+ продукт + Notion templates + Community)
- 💼 Бизнес (как работает компания + Operational)
- 💰 Заработок (модели + ценообразование на пальцах)
- 👥 Партнёры (кого ищем + что предлагаем)
- 🎯 Видение

**Per direction:**
- Главный документ (one-liner назначения)
- Дополнительные страницы (2-4)
- Откуда substrate (cross-refs к 94 docs)
- Narrative entry point

#### Variant B — «По воронке partner experience»
Структура по тому что партнёр видит **в порядке** discovery:
- 🚪 Старт: «Что Jetix вообще» (vision + одна страница)
- 🔍 Глубже: «Как работает метод» (методология explained)
- 🏗️ Что есть: «Платформа + продукт» (Personal/Team OS + Workshop)
- 🤝 Как сотрудничать: «Партнёрство» (4 типа + что просим/даём)
- 💰 Деньги: «Сколько и как» (модели заработка на пальцах)
- 🎯 Куда идём: «Видение + roadmap»

#### Variant C — «По 3 layers целевой аудитории»
Структура для 3 разных типов читателей:
- 👁️ **Просто любопытный** (5 мин read): vision + one-pager + краткое «что мы делаем»
- 🤔 **Серьёзный кандидат** (30-60 мин read): метод + платформа + партнёрство + заработок detail
- 🔬 **Methodology-savvy partner** (deep dive): полная глубина для T1 методолога + R12-моста (с депт refs)

#### Optional Variant D — Hybrid (если applicable)
- Mix logical strengths из A/B/C

**Phase 2 ≥3-4K words.**

**Output:** `.../03-variants-structure.md`
**Commit:** `[metaplan] Phase 2 variants A/B/C structure`

---

### Phase 3 — Per-variant: main docs list per direction

**Tasks — per каждый вариант:**
- Полный список главных документов с one-liner per doc:
  - Что в нём
  - Кому primary
  - Откуда substrate (file paths cross-refs)
  - Формат (Markdown / PDF / лендинг секция / video)
  - Длина target (≤500w / ≤2K / ≤5K)
- Список дополнительных страниц (2-4 per main)
- GAP flag (есть / частично / нужно создать)

**Phase 3 ≥3-4K words.**

**Output:** `.../04-per-variant-main-docs.md`
**Commit:** `[metaplan] Phase 3 per-variant main docs + supporting`

---

### Phase 4 — Per-variant: narrative sequencing (как партнёр читает)

**Tasks — per каждый вариант:**
- Worked example: «партнёр получил ссылку, открывает первый документ — что видит / что читает дальше / куда CTA ведёт»
- Read time estimate per path
- Decision points (где партнёр выбирает «глубже» vs «достаточно»)
- Entry points для разных audiences (T1 vs T3 vs R12-мост)

**Phase 4 ≥2-3K words.**

**Output:** `.../05-narrative-sequencing.md`
**Commit:** `[metaplan] Phase 4 narrative sequencing per variant`

---

### Phase 5 — Per-variant: substrate mapping (откуда что тянем)

**Tasks:**
- Per main doc в каждом варианте — explicit substrate sources (из 94 docs):
  - Какие 2-5 файлов substrate
  - Какие sections тянем
  - Что добавляем / переводим / упрощаем (от substrate → human-language public doc)
- GAP flag: чего substrate'а нет, нужно создать с нуля

**Phase 5 ≥2-3K words.**

**Output:** `.../06-substrate-mapping.md`
**Commit:** `[metaplan] Phase 5 substrate mapping per variant`

---

### Phase 6 — Per-variant pros / cons + comparison

**Tasks:**
- Per вариант: 5 pros + 5 cons + ideal use case (когда A лучше B / C)
- Comparison matrix:
  - Audience clarity (1-5)
  - Substrate reuse efficiency (1-5)
  - Implementation effort (1-5)
  - Public-readiness (1-5)
  - Flexibility (1-5)
- Anti-patterns per variant (где variant ломается)

**Phase 6 ≥2K words.**

**Output:** `.../07-variants-comparison.md`
**Commit:** `[metaplan] Phase 6 variants pros/cons + comparison matrix`

---

### Phase 7 — Recommended path + R1 decisions queue + mermaid + main consolidate

**Tasks:**
- Surface **recommended variant** с rationale (но R1 — Ruslan picks final)
- 5-10 R1 decisions для Ruslan:
  - Какой variant pick (A / B / C / Hybrid)?
  - 5-6 directions ОК или add/drop?
  - Per direction — формат (Markdown / PDF / лендинг)?
  - Sequencing public release (что первым / параллельно)?
  - Quick wins что закрываем prompt'ом сейчас (which 1-2 main docs готовы к filling)?
- 3-5 mermaid META-1..META-5:
  - META-1: 3 variants comparison overview
  - META-2: recommended variant structure
  - META-3: partner narrative flow
  - META-4: substrate mapping (94 docs → main docs)
  - META-5: implementation sequence
- Main consolidated `decisions/strategic/JETIX-PUBLIC-DOCS-METAPLAN-2026-05-25.md` ~8-12K plain Russian:
  - §0 TL;DR 90-sec
  - §1 Filter principles (что вход / что out)
  - §2 3 variants overview + comparison
  - §3 Per variant deep
  - §4 Recommended path
  - §5 R1 decisions queue (5-10)
  - §6 К чему ведёт
- 00-SUMMARY ≤700w

**Output:** main + summary + INDEX
**Commit:** `[metaplan] Phase 7 Main + SUMMARY + INDEX + recommendation (final push)`

---

## §3 Output structure

```
decisions/strategic/
└── JETIX-PUBLIC-DOCS-METAPLAN-2026-05-25.md   # main ~8-12K + 3-5 mermaid

reports/jetix-public-docs-metaplan-2026-05-25/
├── 00-SUMMARY-FOR-RUSLAN.md                    # ≤700w
├── 01-substrate-filter.md                      # Phase 0
├── 02-reference-public-architectures.md        # Phase 1
├── 03-variants-structure.md                    # Phase 2
├── 04-per-variant-main-docs.md                 # Phase 3
├── 05-narrative-sequencing.md                  # Phase 4
├── 06-substrate-mapping.md                     # Phase 5
├── 07-variants-comparison.md                   # Phase 6
└── diagrams/_INDEX.md                          # 3-5 mermaid META-1..META-5
```

---

## §4 Style anchors

- PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md — plain Russian
- EXECUTION-PLAN-FIXATION-2026-05-24.md — 4 partner types
- PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md — Build/Run/Scale
- jetix-map full output — substrate baseline

---

## §5 Constitutional reminder

| Rule | Application |
|---|---|
| R1 surface only | 3 variants = options. Ruslan picks final. R1 queue в §5 main |
| R2 STRICT | Foundation paths untouched |
| R6 | F-G-R triple + cross-cite |
| R11 | NO auto-actions; NO Notion API; NO sample doc content |
| R12 paired-frame STRICT | Public docs structure = partner-facing = R12 STRICT (no manipulation framings) |
| IP-1 | Roles abstract; names = examples |
| Append-only | New files only |
| Pool result | NO auto-launch consequent (после ack — отдельный prompt на filling) |
| F2-F3 derivative | NO new external research |
| **DEFER:** Legal / Financial reporting / Research raw / Brand book — NOT в этом скопе |

---

## §6 К чему ведёт (~2-3h autonomous)

1. Ruslan reads SUMMARY (5 мин) → main (15-20 мин) → variants comparison
2. Ruslan picks 1 variant (A/B/C/Hybrid) + 5-10 R1 decisions
3. После ack → **next iteration prompt** на actual filling одного main doc'а первым (быстрый win)
4. Параллельно — Brand session (отдельно сегодня вечером)
5. Pool result — NO auto

---

*Prompt closure 2026-05-25. Jetix Public Docs MetaPlan — surface 3 variants of high-level public docs structure (по направлениям / по воронке / по аудиториям). Filter: Legal/Financial/Research-raw/Brand DEFERRED. Focus: Метод / Платформа / Бизнес / Заработок / Команда / Видение. F2-F3 derivative. R1 surface only. Pool result. NO sample doc content. Runtime 2-3h.*
