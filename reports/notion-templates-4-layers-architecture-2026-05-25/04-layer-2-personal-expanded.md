---
title: Phase 3 — Layer 2 Personal Expanded (overlay поверх Layer 1)
date: 2026-05-25
type: phase-report-layer-2-spec
parent_prompt: prompts/notion-templates-4-layers-architecture-2026-05-25.md
parent_main: decisions/strategic/NOTION-TEMPLATES-4-LAYERS-ARCHITECTURE-2026-05-25.md
phase: 3
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-notion-templates-4-layers-architecture-2026-05-25
R: low
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + IP-1 STRICT + append-only + no-sample-data
language: russian primary
layer: 2
baseline: PERSONAL-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md
---

# Phase 3 — 🟡 Layer 2 Personal Expanded: delta-overlay

> **Что в этой фазе.** Layer 2 = **не новая система**, а надстройка наблюдательных контуров
> над Layer 1. Здесь только **delta**: что добавляется поверх базовых баз. Семь добавок:
> (1) аналитика cross-DB, (2) шаблоны ревью каскадом, (3) гипотезы deep, (4) расширение
> личной вики, (5) продвинутые связи, (6) AI-хелперы (готовые промпты), (7) промоушен
> optional-баз Layer 1 в core. NO sample data.

---

## §1 Принцип delta: что меняется при апгрейде L1 → L2

Layer 2 **не трогает схемы Layer 1** (это сохраняет совместимость и форк-апдейты — «грамматика»
неизменна). Он добавляет три типа сущностей поверх:

1. **Производные виды** (rollup/aggregation views) — новые линзы на те же данные.
2. **Базы-агрегаторы** (Reviews, Analytics) — собирают данные Layer 1, не дублируя их.
3. **Углубление существующих** (Hypotheses из add-on → core; Knowledge LITE → разделённая).

| L1 (было) | L2 (стало) | Тип delta |
|---|---|---|
| Hypotheses (add-on, базовая) | core + deep tracking (этапы, evidence chain, confidence trail) | углубление |
| Knowledge (одна база LITE) | Sources + Claims + Concepts раздельно + bi-link | расщепление |
| Daily Log (записи) | + Reviews каскад (день→неделя→месяц→квартал→год) | агрегатор |
| Projects (статусы) | + Analytics views (скорость по типам, throughput) | производный вид |
| ручной ввод | + AI-хелперы (готовые промпты ревью/синтеза) | инструмент |

---

## §2 Аналитика cross-DB (производные виды + база Analytics)

**Назначение.** Превратить разрозненные базы Layer 1 в «живой дашборд» через rollup-формулы и
агрегирующие виды. Без новых данных — только агрегация существующих.

**Опция A — только виды (без новой базы):** добавить в Command Center встроенные виды с
группировками и rollup-колонками:
- Projects: group by Type → rollup `count` + `avg Days since touch` (скорость по типам).
- Daily Log: group by Week → rollup `avg Energy`, `count drafts promoted`.
- Hypotheses: group by Status → `count`, конверсия open→confirmed.
- Contacts: group by Type → `count Reconnect needed`.

**Опция B — база Metrics Snapshot (для тех, кто хочет тренды во времени):**

| Поле | Тип | Формула/источник |
|---|---|---|
| Period | Title (week/month) | `YYYY-Www` |
| Projects active | Number | rollup snapshot |
| Hypotheses closed | Number | rollup |
| Avg energy | Number | rollup avg Life Pulse |
| Drafts promoted | Number | rollup Daily Log |
| Stuck count | Number | rollup Projects |
| Pulse red days | Number | rollup Life Pulse |

**Formula patterns:** period-over-period delta (`current - lookup(previous period)`); trend-arrow
паттерн (↑/↓/→ по знаку delta); burnout-early-warning (rolling 7-day avg energy < threshold).

**R1:** Опция A (виды, проще) или B (база снапшотов, тренды)? — surfaced.

---

## §3 Шаблоны ревью каскадом (8 шаблонов)

**Назначение.** Прямой запрос Ruslan — «шаблон анализа недели + месяца». 8 готовых шаблонов;
AI предзаполняет цифры (что было за период), человек отвечает на «почему» и «что дальше».
Реализуются как **templates в базе Reviews** (одна база, поле `Type`).

**База Reviews:**

| Поле | Тип | Дефолт |
|---|---|---|
| Name | Title | автоген `Тип — период` |
| Type | Select | day / week / month / quarter / year / project / hypothesis / call |
| Period | Date range | — |
| Wins | Text | — |
| Friction | Text | — |
| Closed hypotheses | Relation → Hypotheses | — |
| Pulse delta | Text/rollup | — |
| Strategic check | Text | — |
| Lessons | Text | — |
| Next focus | Text | — |

**8 шаблонов (каждый = Notion template button с предзаполненными вопросами):**

| Шаблон | Каденс | Время | Ядро вопросов |
|---|---|---|---|
| 🗒️ День | ежедневно | ~5 мин | намерение / записи / рефлексия / пульс / триггер |
| 🗓️ Неделя | вс вечером | ~20 мин | топ-5 побед / гипотезы / трение / скорость / топ-3 след |
| 📆 Месяц | конец мес | ~45 мин | скорость по 4 типам / закрытие гипотез / финансы / здоровье / паттерны |
| 🌗 Квартал | раз в 3 мес | ~1.5 ч | сдвиги / прогресс к POINT B / аудит отношений / ревизия плана |
| 🎇 Год | конец года | ~полдня | кем стал / победы-провалы / ценности / новый POINT B (пишет человек) |
| 🚀 Проект | квартально | ~30 мин | чекпоинт / блокеры / гипотезы / продолжать-убить-пивот |
| ❓ Гипотеза | при создании | ~15 мин | фальсифицируемость / как проверю / бюджет / уверенность |
| 📞 Звонок | перед звонком | ~15 мин | 8-пунктовый этический чек + 7 вопросов подготовки |

**Каскад:** день сворачивается в неделю → месяц → квартал → год. Каждый уровень опирается на
rollup предыдущего (week агрегирует 7 day-записей через week-number ключ из Daily Log §1 Phase 2).
Это и есть «система учится на себе» (кирпич 5).

**Шаблон звонка отдельно** — идёт в паре с этическим чеком (8 вопросов R12): иду помочь или
впарить? не присваиваю чужое? можно уйти без штрафа? не давлю на «принадлежность к крутым»? —
это мост к Layer 3 (тот же чек применяется к монетизации).

---

## §4 Hypotheses deep (углубление)

**Назначение.** Для Method V2 practitioners (per Education Paradigm O-179/O-185 hypothesis-driven
learning) — гипотеза становится first-class объектом с полным жизненным циклом.

**Delta-поля поверх Layer 1 Hypotheses:**

| Добавляемое поле | Тип | Назначение |
|---|---|---|
| Stage | Select | formulate → design-test → gather-evidence → conclude |
| Evidence chain | Relation → Knowledge (multi) | связь claim→source цепочкой |
| Confidence trail | Text (append) | история изменения уверенности с датами |
| Falsifiability score | Select | weak / ok / strong (насколько фальсифицируема) |
| Method used | Relation → Concepts | какой метод проверки (Method V2 §J) |
| Parent hypothesis | Relation → self | дерево гипотез (под-гипотезы) |
| Cost so far (h) | Rollup | сумма времени по связанным проектам |

**Views:** Pipeline (board by Stage), Strong vs weak (group Falsifiability), Hypothesis tree
(self-relation), Cost overrun (`Cost so far > Time budget`).

**Formula patterns:** falsifiability-gate (гипотеза без Refute criterion помечается «не
фальсифицируема — переформулируй»); confidence-trajectory (растёт/падает); cost-overrun alert.

---

## §5 Расширение личной вики (Knowledge expansion)

**Назначение.** Из единой Knowledge (LITE) → три связанные базы (FULL-стиль), как в wiki v2.

- **Sources** — книги/статьи/видео/подкасты (status, key takeaways).
- **Claims** — проверенные утверждения (confidence, source ref).
- **Concepts** — понятия/определения (для методологов = first-class база).

**Bi-directional links (продвинутые связи):**
- Concept ↔ Concept (related concepts) — граф понятий.
- Claim → Source (provenance) + Claim → Hypothesis (evidence).
- Concept → Hypotheses (где понятие применялось как метод).

**Formula patterns:** concept-degree (число связей понятия = его центральность); orphan-detection
(концепт без связей подсвечивается — наследие `/lint` из wiki v2); stale-claim re-check.

**Для методолога-ниши (Левенчук-уровень):** Concepts становится центральной базой — точные
определения = ядро профессии (per Personal OS Plan §9 ниша «методолог»).

---

## §6 AI-хелперы (готовые промпты)

**Назначение.** Layer 2 добавляет **библиотеку готовых промптов** для Claude Code — review/synthesis
помощники. Это база `AI Helpers` (или просто страница с prompt-сниппетами). **DRAFT-only** —
AI предлагает черновик ревью/синтеза, человек правит.

**База AI Helpers:**

| Поле | Тип |
|---|---|
| Name | Title |
| Purpose | Select (review-prefill / synthesis / weekly-digest / hypothesis-suggest / connection-find) |
| Prompt text | Text |
| Output target | Select (Reviews / Knowledge / Ideas / Daily Log draft) |
| Last used | Date |

**5 паттернов хелперов (описание функций, не реальные промпты-инструкции):**
1. **Review pre-fill** — собирает цифры периода из баз → черновик в Reviews (человек пишет «почему»).
2. **Synthesis** — несколько Sources → черновик Claim/Concept (человек подтверждает).
3. **Weekly digest** — что закрыто/застряло/новое → черновик в Daily Log.
4. **Hypothesis suggest** — из паттернов Daily Log предлагает кандидаты-гипотезы (Ideas draft).
5. **Connection find** — предлагает недостающие relations между записями.

**Железно:** все хелперы пишут с флагом `Draft? = true`; не перезаписывают боевые записи; человек
промоутит вручную. Это перенос дисциплины голосового ввода Layer 1 на аналитику.

---

## §7 Промоушен optional-баз L1 → core L2

В Layer 1 эти базы были optional add-on; в Layer 2 они становятся core (предполагается, что
пользователь Layer 2 — опытный):

| База | L1 | L2 |
|---|---|---|
| Hypotheses | add-on | **core** (deep, §4) |
| Life Pulse | add-on | **core** + trend analytics |
| Knowledge | одна LITE | **расщеплена** (§5) |
| Tasks | сливалась в Projects | **отдельная база** + throughput analytics |

---

## §8 Продвинутые виды (advanced views каталог)

- **Cross-DB dashboard** — Command Center v2 с 10+ linked views и rollup-колонками.
- **Linked DB rollups** — Projects показывает avg confidence связанных гипотез.
- **Timeline синтез** — все проекты + гипотезы + цели на одной шкале времени.
- **Heatmap** — Life Pulse calendar с цветовой картой энергии (через formula → emoji).
- **Saved filtered views** — «красные зоны», «застрявшее», «на ревью» как сохранённые срезы.

---

## §9 Onboarding L1 → L2 (1-week add-ons sequence)

Апгрейд делается за неделю поверх работающего Layer 1:

1. **День 1-2:** расщепить Knowledge → Sources/Claims/Concepts; перенести записи.
2. **День 3:** создать базу Reviews + 8 template-кнопок.
3. **День 4:** сделать первое недельное ревью (ретро прошлой недели через шаблон).
4. **День 5:** углубить Hypotheses (добавить delta-поля §4).
5. **День 6:** настроить AI Helpers (5 промпт-паттернов) в режиме DRAFT.
6. **День 7:** собрать Command Center v2 с аналитическими видами.

**Анти-паттерн:** не делать L2 до того, как L1 реально работает неделю-две. Аналитика поверх
пустых баз = бесполезна.

---

## §10 Constitutional posture Phase 3

- **R1 surface only** — Analytics опция A/B, глубина Hypotheses = выбор Ruslan.
- **R6** — delta наследует Personal OS Plan §7 (8 шаблонов) + wiki v2 (Sources/Claims/Concepts).
- **R11** — AI Helpers строго DRAFT-only; Notion API не зовётся.
- **No sample data** — все хелперы и формулы = паттерны функций, не реальные промпты/данные.
- **IP-1** — ниши (методолог/практик) = примеры применения, схема абстрактна.

---

*Phase 3 closure. Layer 2 = delta-overlay над Layer 1: аналитика cross-DB, 8 шаблонов ревью
каскадом, гипотезы deep, расщеплённая вики, продвинутые связи, AI-хелперы (DRAFT-only),
промоушен add-on→core. Апгрейд за 1 неделю. Дальше Phase 4 — Layer 3 Team Collaboration (R12 AUTO-FIRE).*
