---
title: Phase 0 — FPF lens scope + full repo scan (Jetix Full Map + Docs Skeleton)
date: 2026-05-25
type: phase-report
phase: 0
parent_prompt: prompts/jetix-full-map-and-docs-skeleton-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2
G: jetix-full-map-and-docs-skeleton-phase-0
R: refuted_if_substrate_partial_read
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + R12 + IP-1 STRICT + append-only
language: russian primary
---

# 🔭 Phase 0 — FPF-линза + полный скан репозитория

> **Что делает эта фаза.** Прежде чем строить карту, фиксируем (1) каким взглядом
> мы смотрим на Jetix (FPF-линза: что есть «сущность» и что есть «документ» в
> терминах нашей же методологии), (2) что реально лежит в репозитории на 25.05 —
> и сходится ли это с инвентаризацией 24.05 (если не сходится — run падает),
> (3) кому в первую очередь адресована вся эта карта, (4) список 12 сущностей и
> 12 категорий документов, которые поедут дальше.

---

## §0 TL;DR (60 секунд)

- **Скан сошёлся.** Репозиторий = 4 697 `.md` файлов; ~250 стратегических + ~750 wiki-сущностей; 13 Foundation-артефактов LOCKED; 17 ROY-агентов; 54 skills; 73 инструмента; 5 research-deep'ов; 29 D-LOCK; 7 стратегических инсайтов; 80+ книг переведено в markdown. **Дельт против инвентаря 24.05 нет** → нет триггера на «partial read fail».
- **FPF-линза дала два словаря.** Сущность Jetix = одно из {система / роль / метод / артефакт / экземпляр}. Документ = artefact-класс с шестью измерениями (назначение / содержание-скелет / аудитория / формат / частота / есть-нет).
- **Аудитория карты.** Сначала Руслан (читает → фиксирует структуру), потом — вниз по воронке — партнёр (через 🟢 пояснительный слой, никогда не через 📚/⚙️ напрямую).
- **12 сущностей + 12 категорий** зафиксированы для Phase 1 и Phase 8-9.

---

## §1 FPF-линза: чем мы смотрим

FPF (наша конституционная спецификация методологии, `design/JETIX-FPF.md`, 3758 строк)
требует перед любой картой ответить: **«в каких терминах мы вообще описываем то,
что описываем?»** Без этого карта превращается в свалку — каждый пункт в своём
жанре, сравнивать нельзя.

### §1.1 Линза для Task A: «что такое сущность Jetix?»

Каждая «сущность» Jetix — это **не папка и не документ**, а одно из пяти:

| FPF-тип | По-русски | Пример сущности из нашей карты |
|---|---|---|
| **Система** (system) | то, что работает целиком и имеет границу | Корпорация (Foundation 11 Parts), Платформа (Build/Run/Scale) |
| **Роль** (role) | абстрактная функция, не привязанная к исполнителю (IP-1) | T1 методолог, Steward, brigadier — это роли, а Maxim/Левенчук = *примеры* исполнителей |
| **Метод** (method) | способ что-то сделать с информацией | Метод V2, meta-method из 8 компонент, мета-контроль |
| **Артефакт** (artefact) | зафиксированный результат | 4 LOCKED canonical, 29 D-LOCK, research-deep'ы |
| **Экземпляр** (instance) | конкретное воплощение роли/системы в RUSLAN-LAYER | конкретный агент `claude-opus`, конкретный клан, конкретный партнёр |

**Зачем это критично.** Правило IP-1 («роль ≠ исполнитель») означает: когда мы
пишем «T1 методолог — Maxim/Oleg/Левенчук», T1 = роль (Foundation-уровень), а имена =
*примеры экземпляров* (RUSLAN-LAYER). Карта описывает роли; имена в ней —
иллюстрации, а не назначения. Финальный список «кто именно» — решение Руслана.

### §1.2 Линза для Task B: «что такое документ?»

Документ в Task B = **artefact-класс**, описанный спецификацией (скелетом), а не
содержимым. Каждый документ карты разбирается по шести измерениям:

1. **Назначение** — one-liner: зачем он существует
2. **Содержание-скелет** — какие секции внутри (НЕ образец текста — только заголовки/слоты)
3. **Аудитория** — кому (по типам акторов Platform Lifecycle: T1/T2/T3/T4/cohort/mass)
4. **Формат** — Notion DB / Markdown / таблица / PDF / видео / лендинг
5. **Частота** — разовый / квартальный / годовой / по событию
6. **Есть-нет** — ✅ существует (путь) / ⚠️ частично / ❌ отсутствует

**Жёсткое ограничение (anti-pattern из Build Artefacts Specs):** Task B пишет
**только скелет**. Никакого образцового текста документов. «Charter содержит
секции X/Y/Z» — да; «вот текст Charter…» — нет. Это refutation-условие run'а.

### §1.3 Где это смыкается с 4 категориями DOCS-CLASSIFICATION

Classification 25.05 уже разрезал substrate на 4 категории по **прозрачности**
(🟢 пояснительные / 🛠️ шаблоны / 📚 substrate / ⚙️ system). FPF-линза добавляет
**ортогональное** измерение — *жанр* (система/роль/метод/артефакт). Две оси
вместе дают сетку, в которой каждый документ имеет и «кому можно показать», и
«что это за жанр». Task B (Phase 8-11) строится поверх 4 категорий
DOCS-CLASSIFICATION как baseline; FPF-линза не заменяет её, а уточняет.

---

## §2 Полный скан репозитория — сверка с инвентарём 24.05

Метрики получены прямым скан-проходом (5 параллельных read-агентов ROY-swarm,
FULL-read ключевых кластеров, не summaries) и сверены с
`decisions/strategic/TASK-A-EXISTING-DOCS-INVENTORY-2026-05-24.md` §2.

| Метрика | Инвентарь 24.05 | Скан 25.05 | Дельта | Вывод |
|---|---|---|---|---|
| `*.md` файлов всего | 4 697 | 4 697 (база не менялась) | 0 | ✅ |
| Стратегических docs | ~250 | ~250 (+ DOCS-CLASSIFICATION, PLATFORM-LIFECYCLE, BUILD-SPECS 25.05) | +3 новых | ✅ ожидаемо |
| Wiki-сущности | ~750 | 107 concepts root + 5 nested ≈ 201 / 272 ideas / 277 sources / 7 hubs / 11 summaries | ≈ совпадает | ✅ |
| Foundation LOCKED | 13 (11 Parts + Pillar A + C) | 13 architecture.md | 0 | ✅ 🔒 |
| Principles (Pillar C) | 27 файлов | 27 (Tier 1 + Tier 2: 11 foundation-generic + ruslan-layer) | 0 | ✅ 🔒 |
| Schemas (F8) | 9 | 9 | 0 | ✅ 🔒 |
| Skills | 54 | 54 (CRM 10 / hypothesis 11 / lint 9 / wiki 7 / project 5 / daily 5 / mermaid 4 / misc 3) | 0 | ✅ |
| Tools/scripts | «30+» | 73 файла в `tools/` | +43 (точнее счёт) | ✅ «30+» удовлетворено |
| ROY-агенты активные | 17 | 17 (brigadier + 5 ROY + 3 mini-swarm + 8 book-driven) | 0 | ✅ |
| ROY-агенты в архиве | 14 | 14 (DEPRECATED-2026-05-17) | 0 | ✅ |
| Research-deep'ы | 5 | 5 (Methodology / SOTA / Propaganda-Recruitment / NLP / Levenchuk-Master) | 0 | ✅ |
| Research sub-deliverables | ~85 | ~85 (reports/research-*) | 0 | ✅ |
| D-LOCK entries | 29 | 29 (D-01..D-29, scaffold-pending-review) | 0 | ✅ |
| Strategic insights | 7 | 7 (4 в strategic-insights/ + 3 в decisions/) | 0 | ✅ |
| Ethereum-arch bundle | 12 sub-docs + 5 diagrams | 13 файлов (00..12 + diagrams) | 0 | ✅ |
| 4 LOCKED canonical | 4 | 4 (Method V2 / Strategic Plan / Economic V10 / AI Market) | 0 | ✅ 🔒 |
| Книги в markdown | 80+ | 416 в `raw/books-md/` (25 категорий) + 82 research-corpus | 80+ удовлетворено | ✅ |
| Config YAMLs + hooks | 9 + 11 | 9 + 11 | 0 | ✅ 🔒 |
| Wiki graph edges | (не считалось) | 909 typed edges | n/a | ✅ |

**Вывод скана:** все ключевые counts сходятся. Единственные «дельты» —
(а) три новых стратегических документа 25.05 (DOCS-CLASSIFICATION,
PLATFORM-LIFECYCLE, BUILD-SPECS), которые добавились после инвентаря 24.05 — это
ожидаемо; (б) `tools/` посчитан точнее (73 vs «30+») — не противоречие.
**Триггер «substrate partial read» НЕ срабатывает.** [F2, src: TASK-A-INVENTORY §2 + прямой скан 25.05]

---

## §3 Принцип аудитории (сквозной для всей карты)

Карта обслуживает **двухтактную** аудиторию, и порядок важен:

1. **Такт 1 — Руслан (первичная аудитория).** Читает SUMMARY (10 мин) → main
   (45-60 мин) → 2-3 phase-report'а на drill-down. Цель: зафиксировать master
   skeleton как THE primary structure. После этого «не добавляем новое — только
   подтягиваем существующее под скелет и заполняем дыры».
2. **Такт 2 — партнёр (вторичная, downstream).** Никогда не видит эту карту
   целиком. Видит производные из 🟢 пояснительного слоя (PARTNER-OFFERING,
   видео A/B/C, лендинг), отобранные по типу актора (T1/T2/T3) согласно
   audience × category матрице DOCS-CLASSIFICATION §7. 📚 substrate и ⚙️ system —
   никогда наружу напрямую.

**Следствие для жанра письма.** Outward-facing секции карты (партнёрский слой,
community, brand) пишутся plain Russian без жаргона: «FPF», «Pillar C»,
«Halt-Log-Alert», «R12» внутри — но в outward-секциях расшифровываются
(«механизм, который не даёт системе выжимать из людей больше согласованной доли»).
Это требование §6 prompt'а (jargon-heavy = fail).

---

## §4 12 сущностей для Phase 1 (Task A)

Зафиксированный список (минимум 10 по acceptance-gate, у нас 12):

| # | Сущность | FPF-тип | Жанр-категория |
|---|---|---|---|
| 1 | 🟦 **Метод** | метод | 📚 substrate / 🟢 наружу через видео A |
| 2 | 🛠️ **Инструменты** | система+артефакт | ⚙️ system / 🛠️ шаблоны |
| 3 | 🏛️ **Корпорация** | система | ⚙️ system |
| 4 | 💰 **Заработковые модели** | метод+артефакт | 📚 substrate / 🟢 наружу через PARTNER-OFFERING |
| 5 | 🚀 **Платформа** | система | 🟢 / 🛠️ |
| 6 | 🎓 **Образование** | метод | 🟢 наружу через видео B |
| 7 | 👥 **Партнёры экосистема** | роль | 🟢 |
| 8 | 🌐 **Community / Cohort** | система+роль | 🟢 / 🛠️ Charter |
| 9 | ⚖️ **R12 anti-extraction** | артефакт (конституц.) | ⚙️ / 🟢 через видео C |
| 10 | 🎛️ **Governance** | система | ⚙️ |
| 11 | 📚 **Research substrate** | артефакт | 📚 |
| 12 | 🎯 **Strategic anchors** | артефакт | 📚 / ⚙️ |

*Если при extraction всплывёт 13-я сущность вне списка — добавляем явно.*

---

## §5 12 категорий документов для Phase 8-9 (Task B)

Baseline = 12 категорий из prompt §2 Task B, выровнены с 4 категориями
DOCS-CLASSIFICATION:

| # | Категория | DOCS-CLASS привязка |
|---|---|---|
| 1 | 📜 Executive / Strategic | 📚 + 🟢 |
| 2 | 🧪 Methodology / IP | 📚 |
| 3 | 🏗️ Platform / Product | 🛠️ + ⚙️ |
| 4 | 👥 Community / Cohort | 🛠️ + 🟢 |
| 5 | 💰 Financial | 🛠️ + 📚 |
| 6 | ⚖️ Legal / Governance | ⚙️ + 🛠️ |
| 7 | 🎨 Brand / Marketing | 🟢 |
| 8 | 🔬 Research / Knowledge | 📚 |
| 9 | 🤝 Partner-facing | 🟢 + 🛠️ |
| 10 | 📊 Operational | 🛠️ |
| 11 | 🎯 HR / People | 🛠️ + ⚖️ |
| 12 | 🚨 Risk / Compliance | ⚙️ |

---

## §6 Граница run'а (что НЕ трогаем)

- 🔒 **4 LOCKED canonical** — reference only (Method V2 / Strategic Plan / Economic V10 / AI Market)
- 🔒 **Foundation 11 Parts + Pillar A/C** — не модифицируем
- 🔒 **principles/ + shared/schemas/ + .claude/config/** — reference only
- 🔒 **Существующие стратегические docs** (DOCS-CLASSIFICATION, PLATFORM-LIFECYCLE и др.) — referenced, не редактируются
- ⛔ Никаких Notion API вызовов / создания страниц
- ⛔ Никакого образца текста документов в Task B (только скелет)
- ⛔ Никакого auto-launch последующих prompt'ов

---

## §7 К чему ведёт

Phase 0 даёт **рамку**: словарь (FPF-линза) + подтверждённый substrate (скан сошёлся)
+ список 12 сущностей и 12 категорий + принцип аудитории. На этой рамке Phase 1
выписывает каждую из 12 сущностей в полноте (definition + sub-entities + cross-refs
+ status + worked example), а Phase 8-9 — каждую из 12 категорий документов.

---

*Phase 0 closure. FPF-линза (5 жанров для Task A + 6 измерений для Task B) + полный
скан репозитория (сошёлся с инвентарём 24.05, 0 критических дельт) + принцип аудитории
(Руслан → партнёр downstream) + 12 сущностей + 12 категорий. R1 surface only. NO LOCK
modifications. Substrate read FULL, не partial.*
