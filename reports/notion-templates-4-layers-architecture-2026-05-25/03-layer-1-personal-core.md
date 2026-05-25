---
title: Phase 2 — Layer 1 Personal Core (полный Notion-implementation-ready spec)
date: 2026-05-25
type: phase-report-layer-1-spec
parent_prompt: prompts/notion-templates-4-layers-architecture-2026-05-25.md
parent_main: decisions/strategic/NOTION-TEMPLATES-4-LAYERS-ARCHITECTURE-2026-05-25.md
phase: 2
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-notion-templates-4-layers-architecture-2026-05-25
R: low
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + IP-1 STRICT + append-only + no-sample-data
language: russian primary
layer: 1
baseline: PERSONAL-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md
---

# Phase 2 — 🟢 Layer 1 Personal Core: полная Notion-схема

> **Что в этой фазе.** Превращаем обзор Personal OS в **готовую к сборке схему** Layer 1.
> Для каждой базы: назначение, полная схема полей (имя / тип / формула / дефолт / обязательность),
> виды (фильтры/сорты/группировки), связи, шаблоны записей, паттерны формул, базовые права,
> путь онбординга. **NO sample data** — описываем схемы и паттерны формул, не реальные записи.
> Baseline: `PERSONAL-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md`.

---

## §0 Состав слоя: 7 core баз + 3 optional add-on

| # | База | Статус | Назначение (one-liner) |
|---|---|---|---|
| 1 | 📅 **Daily Log** | core | дневник дня + главный голосовой вход (append-only) |
| 2 | 🚀 **Projects** | core | личные проекты: тип + чекпоинт + детект застрявших |
| 3 | ✅ **Tasks** | core | действия (в LITE сливается в Projects) |
| 4 | 💡 **Ideas** | core | банк идей / inbox с уровнем зрелости |
| 5 | 🎯 **Goals** | core | личные цели POINT A → POINT B |
| 6 | 🤝 **Contacts** | core | личные люди (упрощённый CRM) |
| 7 | 📚 **Knowledge** | core | источники + проверенные факты + понятия |
| 8 | ❓ **Hypotheses** | add-on→L2 | «что хочу узнать» (для Method V2 practitioners) |
| 9 | ❤️ **Life Pulse** | add-on | энергия/сон/настроение/отношения/деньги |
| 10 | 💰 **Finances** | add-on (opt-in) | личные финансы (приватно, не текут наверх) |

**R1 (для Ruslan):** держать ли Tasks отдельной базой (FULL/STANDARD) или сливать в Projects
(LITE)? Держать ли Hypotheses в core (Method-практик) или add-on (новичок)? — варианты surfaced.

**Сквозная дисциплина (наследуется всеми базами Layer 1):** каждая строка = один `.md` файл на
диске; свойства Notion = поля YAML-шапки; при конфликте прав файл; голос → только черновик с
флагом; AI не перезаписывает боевые записи.

---

## §1 📅 Daily Log

**Назначение.** День = одна запись. Утреннее намерение, записи дня (дописываются, в т.ч.
голосом), вечерняя рефлексия, благодарность, пульс дня, триггер на завтра. Главная точка входа.

**Схема полей:**

| Поле | Тип | Формула/дефолт | Обяз. |
|---|---|---|---|
| Date | Title (date-named) | `YYYY-MM-DD` | ✅ |
| Morning intention | Text | — | — |
| Day entries | Text (long, append) | — | — |
| Evening reflection | Text (long) | — | — |
| Gratitude | Text | — | — |
| Day pulse | Select | low / mid / high | — |
| Tomorrow trigger | Text | — | — |
| Energy | Number (1-5) | — | — |
| Linked projects | Relation → Projects | — | — |
| Linked people | Relation → Contacts | — | — |
| Linked hypotheses | Relation → Hypotheses | — | — |
| Linked ideas | Relation → Ideas | — | — |
| Source mode | Select | manual / voice-draft / cc-draft | manual |
| Draft? | Checkbox | — | false |
| Day-of-week | Formula | `formatDate(prop("Date"),"dddd")` | авто |
| Week number | Formula | `formatDate(prop("Date"),"w")` rollup-ключ | авто |

**Views:** (1) **Today** — filter `Date = today`, layout page; (2) **This week** — filter
`Week number = current`, group by Day-of-week; (3) **Drafts to review** — filter `Draft? = true`,
sort newest; (4) **Digest** — calendar layout по месяцу.

**Relations:** Projects (касался сегодня), Contacts (упоминал), Hypotheses (продвигал), Ideas
(родил). Все 2-сторонние.

**Template записи:** заголовки-секции (Намерение / Записи / Рефлексия / Благодарность / Пульс /
Триггер) предзаполнены пустыми; `Draft? = false`; Date = today.

**Formula patterns (паттерны, не реальные значения):** day-of-week derivation; week-rollup key
для сворачивания в Reviews (Layer 2); streak-counter паттерн (считает подряд идущие дни с
заполненной рефлексией через rollup на предыдущий день).

**Permissions baseline (single user):** full access (owner).

**Onboarding:** **первая запись Layer 1** — создаёшь сегодняшний день, пишешь намерение одной
строкой. Это «hello world» системы.

---

## §2 🚀 Projects

**Назначение.** Проект = тип + приоритет + статус + чекпоинт + владелец + связанные гипотезы.
Детект застрявших: активный проект без касания >14 дней всплывает красным.

**Схема полей:**

| Поле | Тип | Формула/дефолт | Обяз. |
|---|---|---|---|
| Name | Title | — | ✅ |
| Type | Select | consulting / research / product / bets / personal | ✅ |
| Priority | Select | P1 / P2 / P3 / P4 | P3 |
| Status | Select | idea / active / paused / done / archived | active |
| Checkpoint | Select | start → in-progress → done/archive (3 чекпоинта вместо 4 SG) | start |
| Owner | Person/Text | self | self |
| Collaborators | Relation → Contacts | — | — |
| Linked hypotheses | Relation → Hypotheses | — | — |
| Linked goals | Relation → Goals | — | — |
| Last touched | Date (rollup max from Daily Log) | — | авто |
| Days since touch | Formula | `dateBetween(now(), prop("Last touched"),"days")` | авто |
| Stuck? | Formula | `if(and(prop("Status")=="active", prop("Days since touch")>14), "🔴 stuck", "")` | авто |
| Start date | Date | — | — |
| Target end | Date | — | — |
| Progress % | Number / rollup tasks done | — | — |
| Notes | Text | — | — |

**Views:** (1) **Active** — filter `Status = active`, sort Priority; (2) **Stuck** — filter
`Stuck? contains 🔴`; (3) **Board by checkpoint** — kanban по Checkpoint; (4) **By type** —
group Type; (5) **Timeline** — по Start/Target end.

**Relations:** Tasks (если отдельная), Hypotheses, Goals, Contacts, Daily Log.

**Template:** Name пусто; Type required pick; Checkpoint = start; секции в теле — Цель / План /
Блокеры / Связанные гипотезы.

**Formula patterns:** stuck-detection (выше); progress rollup из Tasks (`count done / count all`);
priority-decay паттерн (P-проекта подсвечивается, если P1 застрял).

**Onboarding:** засеять 3 активных проекта первой недели.

---

## §3 ✅ Tasks

**Назначение.** Атомарные действия. В **LITE** не существует как база — задачи живут чек-листом
внутри Projects. В **STANDARD/FULL** — отдельная база.

**Схема полей:**

| Поле | Тип | Дефолт | Обяз. |
|---|---|---|---|
| Name | Title | — | ✅ |
| Project | Relation → Projects | — | — |
| Status | Select | todo / doing / done / dropped | todo |
| Priority | Select | now / next / later | next |
| Due | Date | — | — |
| Estimate (min) | Number | — | — |
| Done date | Date | — | — |
| Overdue? | Formula | `if(and(prop("Due")<now(), prop("Status")!="done"),"⚠️","")` | авто |
| Source mode | Select | manual / voice-draft | manual |

**Views:** Today (`Priority = now OR Due ≤ today`), Next, By project (board), Overdue, Done this week.

**Onboarding:** опционально; новичку достаточно чек-листов в Projects.

---

## §4 💡 Ideas

**Назначение.** Банк идей и inbox-корзина. Идея с уровнем зрелости (Tier C сырая → A зрелая);
промоутится в Projects или Hypotheses. Сюда же падают «непонятные» голосовые заметки.

**Схема полей:**

| Поле | Тип | Дефолт | Обяз. |
|---|---|---|---|
| Name | Title | — | ✅ |
| Maturity | Select | C-raw / B-shaping / A-ready | C-raw |
| Domain | Multi-select | business / tech / life / research / meta | — |
| Captured | Date | created time | авто |
| Promote to | Select | — / project / hypothesis | — |
| Needs classification? | Checkbox | false | — |
| Source mode | Select | manual / voice-draft | manual |
| Note | Text | — | — |

**Views:** Inbox (`Maturity = C-raw`), Ready to promote (`Maturity = A-ready`), Needs
classification (`Needs classification? = true`), By domain.

**Relations:** при промоушене создаётся связь с Projects/Hypotheses.

**Onboarding:** не обязателен на старте; наполняется голосом.

---

## §5 🎯 Goals

**Назначение.** Личные цели + POINT A (где я сейчас) → POINT B (куда хочу). Это упрощённый
Strategic слой. Стратегическую прозу пишет человек; AI только предзаполняет данные.

**Схема полей:**

| Поле | Тип | Дефолт | Обяз. |
|---|---|---|---|
| Name | Title | — | ✅ |
| Type | Select | point-A / point-B / horizon-goal / decision | horizon-goal |
| Horizon | Select | month / quarter / year / multi-year | quarter |
| Target metric | Text | — | — |
| Current state | Text | — | — |
| Status | Select | active / achieved / dropped / revised | active |
| Linked projects | Relation → Projects | — | — |
| Owner | self | self | — |
| Review date | Date | — | — |

**Views:** Active goals, By horizon, POINT A/B (filter Type), Due for review.

**Template:** для point-B — секции «Каким хочу стать / Метрики / Срок»; прозу пишет владелец.

**Onboarding:** POINT A одним абзацем в первую неделю.

---

## §6 🤝 Contacts

**Назначение.** Личные люди — упрощённый CRM. Наследует структуру `crm/` (роли, статусы,
история касаний), но облегчённую для одного человека.

**Схема полей:**

| Поле | Тип | Дефолт | Обяз. |
|---|---|---|---|
| Name | Title | — | ✅ |
| Type | Select | family / friend / colleague / mentor / client / vendor / interesting | — |
| Status | Select | active / warm / cold / paused / past | active |
| Last touch | Date | — | — |
| Days since touch | Formula | `dateBetween(now(),prop("Last touch"),"days")` | авто |
| Reconnect? | Formula | `if(prop("Days since touch")>30,"🔔","")` | авто |
| What I offer | Text | — | — |
| What I ask | Text | — | — |
| Touch history | Text (append) | — | — |
| Linked projects | Relation → Projects | — | — |

**Views:** Active, Reconnect (`Reconnect? = 🔔`), By type, Recently touched.

**Onboarding:** засеять 5 топ-контактов первой недели.

---

## §7 📚 Knowledge

**Назначение.** Личная вики: источники (книги/статьи/видео), проверенные факты (claims) с
полем «уверенность», понятия (concepts). В **LITE** — одна перегруженная база Knowledge; в
**FULL** — три отдельные (Sources / Claims / Concepts).

**Схема полей (объединённая Knowledge / LITE):**

| Поле | Тип | Дефолт | Обяз. |
|---|---|---|---|
| Name | Title | — | ✅ |
| Kind | Select | source / claim / concept | source |
| Status (для source) | Select | mentioned / queued / reading / read | queued |
| Confidence (для claim) | Select | low / mid / high | mid |
| Source ref | Relation → self (claim→source) | — | — |
| Key takeaway | Text | — | — |
| Domain | Multi-select | — | — |
| Linked hypotheses | Relation → Hypotheses | — | — |

**Views:** Reading queue (`Kind=source, Status=queued/reading`), Claims by confidence, Concepts
glossary (A-Z), By domain.

**Formula patterns:** confidence-rollup паттерн (гипотеза показывает среднюю уверенность
связанных claims); stale-claim паттерн (claim без обновления >180 дней помечается на ре-проверку).

**Onboarding:** опционально; для методолога-ниши — первая база.

---

## §8 ❓ Hypotheses (add-on → core в Layer 2)

**Назначение.** «Что хочу узнать». Сердце познания для Method V2 practitioners (per
RUSLAN-NOTES-EDUCATION-PARADIGM: hypothesis-driven learning O-179). Гипотеза одной
фальсифицируемой фразой + «как пойму, что подтвердилась» + «что докажет, что неверна».

**Схема полей:**

| Поле | Тип | Дефолт | Обяз. |
|---|---|---|---|
| Statement | Title (фальсифицируемая фраза) | — | ✅ |
| Confirm criterion | Text | — | ✅ |
| Refute criterion | Text | — | ✅ |
| Test method | Text | — | — |
| Time budget (h) | Number | — | — |
| Status | Select | open / testing / confirmed / refuted / parked | open |
| Linked projects | Relation → Projects | — | — |
| Evidence sources | Relation → Knowledge | — | — |
| Confidence | Select | low / mid / high | low |
| Opened / Closed | Date | — | — |

**Views:** Open hypotheses, Testing now, Closed (confirmed/refuted), By project.

**Template:** обязательные поля Confirm/Refute предзаполнены подсказками «как пойму…».

**Onboarding:** засеять 3 гипотезы первой недели (для Method-практика).

---

## §9 ❤️ Life Pulse (add-on)

**Назначение.** Ежедневный мини-замер: энергия, сон, настроение, здоровье, отношения,
финансовый пульс, движение. Меняет объект мониторинга с «системы» на «человека» (кирпич 8).
Вид «красные зоны» ловит ранние сигналы выгорания.

**Схема полей:**

| Поле | Тип | Дефолт | Обяз. |
|---|---|---|---|
| Date | Title (date) | today | ✅ |
| Energy | Number (1-5) | — | — |
| Sleep hours | Number | — | — |
| Sleep quality | Select | poor / ok / good | — |
| Mood | Select | low / neutral / good | — |
| Health note | Text | — | — |
| Relationships | Select | strained / ok / nourishing | — |
| Financial pulse | Select | tight / ok / comfortable | — |
| Movement | Checkbox | false | — |
| Red zone? | Formula | `if(or(prop("Energy")<=2, prop("Sleep hours")<5),"🔴","")` | авто |

**Views:** This week, Red zones (`Red zone? = 🔴`), Trend (calendar).

**Privacy:** **никогда не синкается наверх** (Layer 3/4) — личная красная линия.

**Onboarding:** add-on недели 2.

---

## §10 💰 Finances (add-on, opt-in)

**Назначение.** Личные финансы — строго приватно. Простой учёт. **Не путать** с Layer 4
Financial Overview (бизнес). Здесь — личный кошелёк.

**Схема полей:** Name / Type (income/expense) / Category / Amount / Date / Account / Recurring?
/ Note. **Views:** This month, By category, Recurring. **Formula patterns:** monthly-burn
rollup; personal-runway паттерн. **Privacy:** никогда наверх.

**Onboarding:** opt-in; по желанию.

---

## §11 🔗 Связи между базами Layer 1 (relation map)

```
Daily Log ──упоминает──> Projects ──проверяет──> Hypotheses ──доказательства──> Knowledge
Daily Log ──1:1 день──> Life Pulse                Projects ──служит──> Goals
Daily Log ──упоминает──> Contacts                 Ideas ──вырастает в──> Projects/Hypotheses
```

Центр — Daily Log (всё касается дня) + Command Center как хаб-страница (не база, а dashboard со
встроенными linked views всех баз).

---

## §12 Command Center (хаб-страница, не база)

Одна страница со встроенными linked-database views: Today (Daily Log) / Active projects / Stuck /
Reconnect contacts / Open hypotheses / Inbox ideas / Red-zone pulse. Это «точка входа» (кирпич 9).
Onboarding: собирается после 5 core баз.

---

## §13 Три варианта сборки Layer 1 (R1 — выбор Ruslan)

| Вариант | Баз | Что сливается | Кому |
|---|---|---|---|
| **LITE** | 8 | Projects+Tasks; Knowledge одна; Contacts одна | новичкам, гуманитариям |
| **STANDARD** | 11 | разделено основное, без Tasks-базы и Concepts на старте | Ruslan, опытным |
| **FULL** | 14 | всё раздельно (Sources/Claims/Concepts отдельно) | инженерам, методологам |

---

## §14 Onboarding-путь Layer 1 (что создаёшь первым)

1. Command Center хаб (пустой) или 5 core баз — **порядок = R1 выбор Ruslan**.
2. Daily Log → первая запись (сегодня + намерение).
3. Projects → 3 активных проекта.
4. Contacts → 5 топ-контактов.
5. Goals → POINT A одним абзацем.
6. (Method-практик) Hypotheses → 3 гипотезы.
7. Неделя 2 → add-ons (Life Pulse, Knowledge, Ideas, Finances).

**Цель: ≤30 минут до первой осмысленной записи** (fork-friendly порог).

---

## §15 Permissions baseline Layer 1

Single user = full access ко всем базам. Нет ролей, нет шеринга. Это упрощает форк: новичок не
думает о правах. Права появляются только на Layer 3 (команда). Внешний шеринг отдельных страниц
(например, показать проект другу) — ручной Notion share, вне схемы.

---

## §16 Constitutional posture Phase 2

- **R1 surface only** — LITE/STANDARD/FULL, Tasks-как-база, Hypotheses core/add-on = выбор Ruslan.
- **R6** — схемы наследуют Personal OS Plan §5 + crm/ структуру + Hypotheses из Education Paradigm.
- **R11** — Notion API не зовётся; это спека.
- **No sample data** — все поля/формулы = паттерны; ни одной реальной записи/суммы/имени-данных.
- **IP-1** — роль владельца абстрактна; «Ruslan/Дмитрий» = примеры применения, не в схеме.

---

*Phase 2 closure. Layer 1 Personal Core = 7 core + 3 add-on баз, готовая Notion-схема: поля,
виды, связи, шаблоны, паттерны формул, права, онбординг ≤30 мин, 3 варианта сборки. NO sample
data. Дальше Phase 3 — Layer 2 Personal Expanded (overlay поверх Layer 1).*
