---
title: Phase 3 — Полная схема каждой базы (поля + виды + связи + зеркало в файлах)
date: 2026-05-24
type: design-plan-phase-output
parent_prompt: prompts/personal-os-notion-template-plan-2026-05-24.md
phase: 3
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F3
G: personal-os-notion-template-plan
R: refuted_if_any_db_lt_10_props_OR_lt_3_views_OR_no_frontmatter_mirror
constitutional_posture: R1 surface + R6 + R11 + append-only
language: russian primary + plain conversational
---

# Phase 3 — Что в каждой базе (полная схема)

> **Главная мысль фазы.** Это «техзадание» каждой базы: какие поля (с типом,
> значением по умолчанию, обязательностью), какие виды (фильтры/сортировки), какие
> связи и как база зеркалится в файл на диске. Любой, кто будет строить шаблон в
> Notion (Руслан, Claude Code или форкнувший человек), берёт эту фазу и собирает базу
> один-в-один.
>
> **Дисциплина для всех баз:** каждая строка базы ↔ один `.md` файл на диске.
> Свойства Notion = поля в YAML-шапке (frontmatter). При конфликте — **прав файл**
> (Global Rule 4). Скрипт синхронизации — Phase 6.

---

## §0 Условные обозначения

- **Тип** — тип свойства Notion: Text / Title / Select / Multi-select / Date / Number /
  Checkbox / Person / Relation / Formula / Rollup / Files / URL.
- **По умолч.** — что подставляется при создании записи.
- **Обяз.** — Y (обязательно) / N (нет).
- **Зеркало** — имя поля в YAML-шапке файла на диске.

---

## §1 📅 Daily Log DB (ядро — основной ввод)

**Из кирпичей:** Part 1 (state) + Part 2 (ingestion). Append-only, кормится голосом.

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало (frontmatter) | Заметки |
|---|---|---|---|---|---|
| Title | Title | — | Y | `title` | формат YYYY-MM-DD |
| Date | Date | сегодня | Y | `date` | сортируемое |
| Energy | Select 1-10 | 5 | N | `energy` | утренний само-замер |
| Mood | Select (😞😐🙂😄) | — | N | `mood` | настроение |
| Focus area | Multi-select | — | N | `focus` | активные проекты дня |
| Voice draft? | Checkbox | N | N | `_voice_draft` | маркер DRAFT (Phase 4) |
| Morning intent | Text | — | N | `morning_intent` | намерение на день |
| Entries | Rich text | — | N | `entries` | дневные записи (дописываются) |
| Reflections | Rich text | — | N | `reflections` | вечерняя рефлексия |
| Gratitude | Text | — | N | `gratitude` | за что благодарен |
| Friction | Text | — | N | `friction` | что мешало |
| Tomorrow trigger | Text | — | N | `tomorrow` | зерно плана на завтра |
| Linked Projects | Relation → Projects | — | N | `projects` | упомянуты сегодня |
| Linked People | Relation → CRM People | — | N | `people` | с кем общался (касание) |
| Linked Hypotheses | Relation → Hypotheses | — | N | `hypotheses` | что проверял |
| Pulse score | Number 1-10 | — | N | `pulse` | общая оценка дня |

### Виды
- **Сегодня** (filter: Date = today) — главный рабочий вид.
- **Эта неделя** (filter: Date в последние 7 дней; sort: Date desc).
- **Черновики на разбор** (filter: Voice draft = Y) — очередь промоушена.
- **Недельный дайджест** (group by week) — для ревью.

### Связи
Projects (N:N) / People (N:N) / Hypotheses (N:N) / Life Pulse (1:1 за день).

### Зеркало в файлах
`personal-os/daily/2026-05-24.md` — один файл = один день. Append-only: новые записи
дописываются в `entries`, старые не стираются.

---

## §2 🚀 Projects DB

**Из кирпича:** Part 7. 4 типа + 3 чекпоинта (упрощённые Stage Gates).

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало | Заметки |
|---|---|---|---|---|---|
| Title | Title | — | Y | `title` | человекочитаемое имя |
| Slug | Text | — | Y | `slug` | kebab-case (имя файла) |
| Type | Select (consulting/research/product/bets) | — | Y | `type` | таксономия KM MVP |
| Subtype | Select | — | N | `subtype` | Layer 2 (под нишу) |
| Priority | Select (P1-P4) | P3 | Y | `priority` | |
| Status | Select (active/planned/paused/archived) | planned | Y | `status` | |
| Checkpoint | Select (старт/в-работе/готово-или-архив) | старт | N | `checkpoint` | 3 уровня вместо SG-1..4 |
| Owner | Person | self | Y | `owner` | |
| Collaborators | Relation → CRM People | — | N | `collaborators` | |
| Start date | Date | — | N | `start_date` | |
| Target date | Date | — | N | `target_date` | |
| Last touched | Date | авто | — | `last_touched` | для stuck-детекта |
| Stuck? | Formula | — | — | `stuck` | active AND last_touched > 14д |
| Linked Hypotheses | Relation → Hypotheses | — | N | `hypotheses` | |
| Linked Sources | Relation → Sources | — | N | `sources` | |
| Strategic link | Relation → Strategic | — | N | `serves` | какой цели служит (POINT B) |
| Description | Rich text | — | N | `description` | один абзац |
| Checkpoint notes | Rich text | — | N | `checkpoint_notes` | что нужно для перехода |
| Next 3 actions | Text | — | N | `next_actions` | |

### Виды
- **Активные P1-P2** (filter: status=active, priority в [P1,P2]; kanban by Checkpoint).
- **По типу** (group by Type — 4 колонки).
- **Застрявшие** (filter: Stuck = true) — красный флаг.
- **Архив** (filter: status=archived — отдельно, не мешает).

### Связи
Tasks (1:N) / CRM People (N:N) / Hypotheses (N:N) / Sources (N:N) / Daily Log (N:N) /
Strategic (N:N).

### Зеркало
`personal-os/projects/<slug>.md`.

---

## §3 ✅ Tasks DB (опционально — Variant FULL/STANDARD)

**Из кирпича:** Part 7. Конкретные действия под проекты.

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало | Заметки |
|---|---|---|---|---|---|
| Title | Title | — | Y | `title` | что сделать |
| Status | Select (todo/doing/done/dropped) | todo | Y | `status` | |
| Priority | Select (P1-P4) | P3 | N | `priority` | |
| Project | Relation → Projects | — | N | `project` | к какому проекту |
| Due date | Date | — | N | `due` | |
| Estimate | Select (15м/1ч/полдня/день+) | — | N | `estimate` | |
| Energy needed | Select (низкая/средняя/высокая) | — | N | `energy_needed` | подбор под состояние |
| Voice draft? | Checkbox | N | N | `_voice_draft` | DRAFT-маркер |
| Done date | Date | авто при done | — | `done_date` | |
| Notes | Text | — | N | `notes` | |
| Blocked by | Relation → Tasks | — | N | `blocked_by` | зависимости |

### Виды
- **Сегодня** (filter: due ≤ today, status ≠ done).
- **По проекту** (group by Project).
- **Быстрые победы** (filter: estimate=15м, status=todo).
- **Под энергию** (group by Energy needed — что делать при низкой/высокой энергии).

### Связи
Projects (N:1) / Tasks (self, blocked_by).

### Зеркало
`personal-os/tasks/<slug>.md` (или встроены в проект-файл при варианте LITE).

---

## §4 📖 Sources DB (книги / статьи / видео / подкасты)

**Из кирпича:** Part 3. Кормится голосом («читаю/смотрел X»).

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало | Заметки |
|---|---|---|---|---|---|
| Title | Title | — | Y | `title` | название |
| Author | Text | — | N | `author` | |
| Kind | Select (book/article/video/podcast/talk) | — | Y | `kind` | |
| Status | Select (mentioned/queued/reading/done/abandoned) | mentioned | Y | `status` | |
| URL | URL | — | N | `url` | |
| Rating | Select (1-5⭐) | — | N | `rating` | |
| Started | Date | — | N | `started` | |
| Finished | Date | — | N | `finished` | |
| Key takeaways | Rich text | — | N | `takeaways` | главное |
| Linked Concepts | Relation → Concepts | — | N | `concepts` | |
| Linked Claims | Relation → Claims | — | N | `claims` | что из источника подтвердилось |
| Linked Hypotheses | Relation → Hypotheses | — | N | `hypotheses` | какие гипотезы кормит |
| Domain | Multi-select | — | N | `domain` | тема/область |
| Voice draft? | Checkbox | N | N | `_voice_draft` | |

### Виды
- **Сейчас читаю** (filter: status=reading).
- **Очередь** (filter: status в [mentioned, queued]; sort: rating desc).
- **Прочитано** (filter: status=done; group by domain).
- **По теме** (group by Domain).

### Связи
Concepts (N:N) / Claims (N:N) / Hypotheses (N:N).

### Зеркало
`personal-os/knowledge/sources/<slug>.md`.

---

## §5 🔬 Claims DB (проверенные утверждения)

**Из кирпичей:** Part 3 + 6a (provenance облегчён).

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало | Заметки |
|---|---|---|---|---|---|
| Title | Title | — | Y | `title` | утверждение одной строкой |
| Statement | Rich text | — | Y | `statement` | полная формулировка |
| Confidence | Select (низкая/средняя/высокая) | средняя | Y | `confidence` | F-G-R облегчён до 1 поля |
| Source | Relation → Sources | — | N | `source` | откуда (provenance) |
| Source quote | Text | — | N | `source_quote` | цитата-обоснование |
| Status | Select (draft/verified/disputed/refuted) | draft | Y | `status` | |
| Linked Hypotheses | Relation → Hypotheses | — | N | `hypotheses` | какую гипотезу закрывает |
| Linked Concepts | Relation → Concepts | — | N | `concepts` | |
| Domain | Multi-select | — | N | `domain` | |
| Date added | Date | сегодня | N | `date` | |
| Voice draft? | Checkbox | N | N | `_voice_draft` | |

### Виды
- **Проверенные с высокой уверенностью** (filter: status=verified, confidence=высокая).
- **На проверку** (filter: status=draft) — очередь верификации.
- **Спорные/опровергнутые** (filter: status в [disputed, refuted]).
- **По теме** (group by Domain).

### Связи
Sources (N:1) / Hypotheses (N:N) / Concepts (N:N).

### Зеркало
`personal-os/knowledge/claims/<slug>.md`.

---

## §6 ❓ Hypotheses DB («что хочу узнать» — сердце познания)

**Из кирпича:** Part 3. Прямой запрос Руслана. Кормится голосом («а что если»).

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало | Заметки |
|---|---|---|---|---|---|
| Title | Title | — | Y | `title` | вопрос/гипотеза одной строкой |
| Statement | Rich text | — | Y | `statement` | фальсифицируемая формулировка |
| Status | Select (open/testing/confirmed/refuted/parked) | open | Y | `status` | |
| Acceptance predicate | Text | — | N | `acceptance` | как пойму, что подтвердилась |
| Falsification | Text | — | N | `falsification` | что докажет, что неверна |
| Test method | Text | — | N | `test_method` | эксперимент/наблюдение |
| Time budget | Select (час/день/неделя/месяц) | — | N | `time_budget` | |
| Confidence | Select (низкая/средняя/высокая) | низкая | N | `confidence` | текущая вера |
| Linked Projects | Relation → Projects | — | N | `projects` | где проверяю |
| Linked Sources | Relation → Sources | — | N | `sources` | доказательства |
| Linked Claims | Relation → Claims | — | N | `claims` | что подтвердилось |
| Opened | Date | сегодня | N | `opened` | |
| Closed | Date | — | N | `closed` | |
| Domain | Multi-select | — | N | `domain` | |
| Voice draft? | Checkbox | N | N | `_voice_draft` | |

### Виды
- **Открытые** (filter: status=open; sort: opened desc) — что хочу узнать сейчас.
- **В проверке** (filter: status=testing).
- **Закрытые** (filter: status в [confirmed, refuted]; group by status).
- **По теме** (group by Domain).

### Связи
Projects (N:N) / Sources (N:N) / Claims (N:N).

### Зеркало
`personal-os/knowledge/hypotheses/<slug>.md`.

---

## §7 💡 Ideas Bank DB

**Из кирпича:** Part 3. Кормится голосом («идея:»). Tier A/B/C.

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало | Заметки |
|---|---|---|---|---|---|
| Title | Title | — | Y | `title` | идея одной строкой |
| Body | Rich text | — | N | `body` | развёрнуто |
| Tier | Select (A/B/C) | C | Y | `tier` | C=сырая, A=зрелая |
| Status | Select (raw/developing/promoted/dropped) | raw | Y | `status` | |
| Promoted to | Relation → Projects/Hypotheses | — | N | `promoted_to` | во что выросла |
| Domain | Multi-select | — | N | `domain` | |
| Voice ref | Text | — | N | `voice_ref` | ссылка на голос-источник |
| Added | Date | сегодня | N | `date` | |
| Voice draft? | Checkbox | N | N | `_voice_draft` | |
| Spark | Text | — | N | `spark` | что натолкнуло |

### Виды
- **Tier A — зрелые** (filter: tier=A) — кандидаты на промоушен.
- **Свежие** (filter: status=raw; sort: date desc).
- **По теме** (group by Domain).
- **Промоутнутые** (filter: status=promoted) — история, что выросло.

### Связи
Projects (N:N) / Hypotheses (N:N).

### Зеркало
`personal-os/ideas/<slug>.md`.

---

## §8 🤝 CRM People DB

**Из кирпича:** Part 10. Наследует `crm/` структуру (24 роли, 13 статусов).

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало | Заметки |
|---|---|---|---|---|---|
| Name | Title | — | Y | `name` | |
| Slug | Text | — | Y | `slug` | kebab-case |
| Roles | Multi-select (24 роли в 6 группах) | — | N | `roles` | sales/capital/partnership/advisory/team/network |
| Status | Select (13 статусов) | cold | Y | `status` | cold→warm→...→closed |
| Org | Relation → CRM Orgs | — | N | `org` | |
| Last touch | Date | — | N | `last_touch` | |
| Stuck? | Formula | — | — | `stuck` | active AND last_touch>14д |
| Next action | Text | — | N | `next_action` | |
| What I offer | Text | — | N | `offer` | §7 strategy-hook |
| What I ask | Text | — | N | `ask` | §8 strategy-hook |
| Trust level | Select (1-5) | — | N | `trust` | глубина отношений |
| Linked Projects | Relation → Projects | — | N | `projects` | коллаборации |
| Contact info | Text | — | N | `contact` | tg/email (НЕ секреты) |
| History | Rich text | — | N | `history` | append-only касания (§11) |
| Voice draft? | Checkbox | N | N | `_voice_draft` | |
| Source/met via | Text | — | N | `met_via` | как познакомились |

### Виды
- **Тёплые активные** (filter: status в [warm, active]; sort: last_touch asc).
- **Застрявшие** (filter: Stuck = true) — пора коснуться.
- **По роли** (group by Roles).
- **Pipeline** (kanban by Status).
- **Черновики из голоса** (filter: voice draft=Y).

### Связи
CRM Orgs (N:N) / Projects (N:N) / Daily Log (N:N).

### Зеркало
`crm/people/<slug>.md` (уже существует — наследуем 1:1).

---

## §9 🏢 CRM Orgs DB

**Из кирпича:** Part 10.

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало | Заметки |
|---|---|---|---|---|---|
| Name | Title | — | Y | `name` | |
| Slug | Text | — | Y | `slug` | |
| Kind | Select (company/community/fund/edu/media/other) | — | N | `kind` | |
| Status | Select (13 статусов) | cold | Y | `status` | |
| People | Relation → CRM People | — | N | `people` | кто там работает |
| Relationship | Select (client/partner/investor/vendor/competitor/network) | — | N | `relationship` | |
| Last touch | Date | — | N | `last_touch` | |
| Notes | Rich text | — | N | `notes` | append-only |
| URL | URL | — | N | `url` | |
| Linked Projects | Relation → Projects | — | N | `projects` | |
| Voice draft? | Checkbox | N | N | `_voice_draft` | |

### Виды
- **Активные** (filter: status=active).
- **По типу отношений** (group by Relationship).
- **Застрявшие** (stuck filter).

### Связи
CRM People (N:N) / Projects (N:N).

### Зеркало
`crm/orgs/<slug>.md`.

---

## §10 🔄 Reviews DB (неделя/месяц/квартал/год — одна база)

**Из кирпича:** Part 5. Поле type разделяет периоды.

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало | Заметки |
|---|---|---|---|---|---|
| Title | Title | — | Y | `title` | напр. «Неделя 2026-W21» |
| Type | Select (week/month/quarter/year/project) | week | Y | `type` | |
| Period start | Date | — | Y | `period_start` | |
| Period end | Date | — | Y | `period_end` | |
| Status | Select (draft/done) | draft | Y | `status` | |
| Wins | Rich text | — | N | `wins` | топ побед |
| Friction | Rich text | — | N | `friction` | блокеры |
| Hypotheses closed | Relation → Hypotheses | — | N | `hyp_closed` | что закрыл |
| Projects touched | Relation → Projects | — | N | `projects` | |
| Pulse trend | Text | — | N | `pulse_trend` | динамика Life Pulse |
| Strategic check | Text | — | N | `strategic_check` | на траектории POINT B? |
| Carry forward | Rich text | — | N | `carry` | что переносим |
| Next period top 3 | Text | — | N | `next_top3` | |
| Lessons | Rich text | — | N | `lessons` | compound learning |

### Виды
- **По типу** (group by Type — недели/месяцы/кварталы отдельно).
- **Последнее** (sort: period_end desc).
- **Черновики** (filter: status=draft) — недозаполненные ревью.
- **Годовая лента** (filter: type=year).

### Связи
Hypotheses (1:N) / Projects (1:N) / Life Pulse (через период).

### Зеркало
`personal-os/reviews/<type>/<period>.md`.

---

## §11 🧭 Strategic DB (POINT A → POINT B + решения)

**Из кирпича:** Part 11. Стратегию/цели пишет человек (R1).

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало | Заметки |
|---|---|---|---|---|---|
| Title | Title | — | Y | `title` | |
| Type | Select (point-a/point-b/plan/decision) | — | Y | `type` | 4 типа вместо 6 |
| Horizon | Select (year/quarter/month/now) | — | N | `horizon` | |
| Body | Rich text | — | Y | `body` | проза — пишет человек |
| Authored by | Select (me/hybrid) | me | Y | `authored_by` | трейл авторства облегчён |
| Status | Select (active/superseded/considering) | active | Y | `status` | |
| Linked Projects | Relation → Projects | — | N | `projects` | что служит цели |
| Decision rationale | Text | — | N | `rationale` | для type=decision |
| Decided on | Date | — | N | `decided_on` | |
| Revisit date | Date | — | N | `revisit` | когда пересмотреть |
| Supersedes | Relation → Strategic | — | N | `supersedes` | предыдущая версия |

### Виды
- **Текущий курс** (filter: status=active; group by Type) — POINT A/B/планы.
- **Очередь решений** (filter: type=decision, status=considering) — Human Gate.
- **Архив курса** (filter: status=superseded) — история POINT B.
- **Пора пересмотреть** (filter: revisit ≤ today).

### Связи
Projects (N:N) / Strategic (self, supersedes).

### Зеркало
`personal-os/strategic/<slug>.md`.

---

## §12 ❤️ Life Pulse DB (здоровье человека)

**Из кирпича:** Part 8 (мониторинг системы → мониторинг человека).

### Поля

| Свойство | Тип | По умолч. | Обяз. | Зеркало | Заметки |
|---|---|---|---|---|---|
| Date | Title/Date | сегодня | Y | `date` | YYYY-MM-DD |
| Energy | Number 1-10 | — | Y | `energy` | |
| Sleep hours | Number | — | N | `sleep` | |
| Sleep quality | Select 1-5 | — | N | `sleep_quality` | |
| Mood | Select (😞😐🙂😄) | — | N | `mood` | |
| Health note | Text | — | N | `health` | самочувствие/симптомы |
| Relationships | Select 1-5 | — | N | `relationships` | связь с близкими |
| Finance pulse | Select (🔴🟡🟢) | — | N | `finance` | спокойствие по деньгам |
| Movement | Checkbox | N | N | `movement` | была ли активность |
| Linked Daily Log | Relation → Daily Log | — | N | `daily` | 1:1 за день |
| Note | Text | — | N | `note` | свободно |

### Виды
- **Эта неделя** (last 7 days; sort: date desc).
- **Тренд месяца** (chart-friendly: Energy/Sleep over month).
- **Красные зоны** (filter: energy ≤ 3 OR finance=🔴) — ранние сигналы burnout.

### Связи
Daily Log (1:1 за день).

### Зеркало
`personal-os/pulse/<date>.md`.

---

## §13 🧩 Concepts DB + 📂 Reference (компактно)

**Concepts** (Part 3 — заводить опционально, на старте сливать в Sources):

| Свойство | Тип | Обяз. | Зеркало |
|---|---|---|---|
| Title | Title | Y | `title` |
| Definition | Rich text | Y | `definition` |
| Domain | Multi-select | N | `domain` |
| Linked Sources | Relation → Sources | N | `sources` |
| Linked Claims | Relation → Claims | N | `claims` |
| Related Concepts | Relation → Concepts (self) | N | `related` |
| Maturity | Select (stub/developing/mature) | Y | `maturity` |

Виды: По теме / Зрелые / Заготовки. Зеркало: `personal-os/knowledge/concepts/<slug>.md`.

**Reference** — обычно не база, а страница-контейнер: шаблоны ревью, скрипты синка,
личный канон (правила, ценности), памятка «5 правил Personal OS». Зеркало:
`personal-os/reference/`.

---

## §14 📐 Дисциплина зеркала «файл = правда»

**Главное правило (Global Rule 4):**
- Каждая строка базы ↔ один `.md` файл: `personal-os/<db>/<slug>.md`.
- Свойства Notion = поля в YAML-шапке файла (колонка «Зеркало» в каждой таблице выше).
- **При конфликте — прав файл.** Notion получает поправку при синке.
- Скрипт двусторонней синхронизации — Phase 6.

**Пример файла** (Daily Log за день):
```yaml
---
title: 2026-05-24
date: 2026-05-24
energy: 7
mood: 🙂
focus: [personal-os-template, exec-plan]
_voice_draft: false
projects: [personal-os-template]
people: [dmitry]
hypotheses: [notion-template-transmits-substrate]
pulse: 8
---
# Записи
- утром: спроектировал Phase 3 схемы баз
- ...
# Рефлексия
- ...
```

---

## §15 Конвенции именования

- **Имена баз:** PascalCase в Notion (Daily Log, CRM People).
- **Имена свойств:** короткие, человекочитаемые (Energy, Last touch).
- **Slug:** kebab-case (`my-cool-project`).
- **Даты:** YYYY-MM-DD (ISO).
- **DRAFT-маркер:** поле `Voice draft?` (frontmatter `_voice_draft: true`) во всех
  базах, куда пишет голос.
- **Поля-системные** (Last touched, Stuck?, Done date) — авто, человек не трогает.

---

## §16 Сводка фазы

| База | Полей | Видов | Кормится голосом | Зеркало-путь |
|---|---|---|---|---|
| Daily Log | 16 | 4 | ✅ | `daily/` |
| Projects | 19 | 4 | ✅ | `projects/` |
| Tasks | 11 | 4 | ✅ | `tasks/` |
| Sources | 14 | 4 | ✅ | `knowledge/sources/` |
| Claims | 11 | 4 | ⚠️ | `knowledge/claims/` |
| Hypotheses | 14 | 4 | ✅ | `knowledge/hypotheses/` |
| Ideas Bank | 10 | 4 | ✅ | `ideas/` |
| CRM People | 16 | 5 | ✅ | `crm/people/` |
| CRM Orgs | 11 | 3 | ✅ | `crm/orgs/` |
| Reviews | 14 | 4 | ⚠️ | `reviews/` |
| Strategic | 11 | 4 | ✅ | `strategic/` |
| Life Pulse | 11 | 3 | ✅ | `pulse/` |
| Concepts | 7 | 3 | ⚠️ | `knowledge/concepts/` |

Каждая база ≥10 полей (кроме Concepts — опциональна), ≥3 видов, явные связи, путь
зеркала. Готово для сборки.

*Phase 3 closure 2026-05-24. 13 баз с полной схемой: поля (тип/по-умолч/обяз/зеркало),
≥3 видов, связи, frontmatter-зеркало + пример файла + конвенции. Дальше Phase 4:
матрица голосового ввода.*
