---
type: implementation-plan
status: v1-beta-FINAL
approval-status: pending-ruslan-review
version: v1-beta-FINAL-2026-04-18
owner: ruslan
created: 2026-04-18
finalized: 2026-04-18
covers-steps: [3, 4, 5, 6]
reference-plan: "план от 2026-04-17 (Шаги 1-6)"
primary-goal-anchor: $50K revenue до 30.06.2026
related:
  - design/SYSTEM-DESIGN-TECH.md
  - design/SYSTEM-DESIGN-TECH-SUMMARY.md
  - SYSTEM-DESIGN-HUMAN.md §4.1 (папочная структура v1-beta)
---

# IMPLEMENTATION-PLAN — Шаги 3-6 воплощения архитектуры v1-beta

> **Scope.** Конкретные технические действия по переводу утверждённой
> архитектуры из документов в реальную файловую систему репозитория.
> Шаги 1-2 (документы + синтез) завершены. Цель v1-beta-ready — конец
> недели 2026-04-24.
>
> **Стратегический якорь.** Всё что здесь — инструмент к $50K до 30.06.2026.
> Если шаг не двигает эту цель прямо или косвенно через разблокировку
> работы — урезаем scope, не расширяем.
>
> **Для каждого шага указано:** что делать, где положить, порядок,
> оценка времени, блокеры (требующие решения Ruslan'а), критерий завершения.

---

## Шаг 3 — Шаблоны (templates)

**Цель.** Создать набор канонических templates, которые cover'ят все
создаваемые entity-файлы. Без них v1-beta не стартует чисто — все
новые файлы будут drift'овать.

### 3.1 Что создаём (место: `templates/` в корне + `projects/_template/`)

Текущее состояние: 7 файлов в `templates/` (daily-log, tpl-contact, tpl-daily, tpl-kb-article, tpl-project-overview, tpl-raw-source, weekly-review). `projects/_template/` — 6 файлов (overview, plan, decisions, log, questions, resources). Пробелы и несоответствия закрываем.

Приоритет выставлен от блокирующих ритуалы к nice-to-have.

| # | Template | Путь | Frontmatter schema (ключевые поля) | Пример использования | Приоритет |
|---|----------|------|-------------------------------------|----------------------|-----------|
| T-01 | `tpl-project-overview.md` | `templates/` (обновить существующий) | `type: project-overview`, `status`, `budget-hours`, `budget-weeks`, `kill-criterion`, `next_action`, `owner`, `project-slug`, `created` | `projects/quick-money/overview.md` | P0 (блокирует I-23) |
| T-02 | `tpl-decision.md` | `templates/` (NEW) | `type: decision`, `created`, `context`, `alternatives: []`, `decision`, `evidence`, `replay-check`, `relevant-agents: []` | `decisions/2026-04-decisions.md` entry | P0 (блокирует I-12 + `/propagate-decision`) |
| T-03 | `tpl-hypothesis.md` | `templates/` (NEW) | `type: hypothesis`, `status: backlog/active/validated/rejected`, `tested-with`, `success-criterion`, `owner-project`, `created` | `hypotheses/active.md` entry | P0 |
| T-04 | `tpl-strategy-life.md` | `templates/` (NEW) | `type: strategy-life`, `level: yearly/monthly/weekly`, `period`, `north-star`, `focus-blocks: []`, `budget-resources` | `strategy/life/2026-yearly.md` | P0 (блокирует Шаг 6) |
| T-05 | `tpl-strategy-project.md` | `templates/` (NEW) | `type: strategy-project`, `project-slug`, `point-a`, `point-b`, `horizon`, `metric-50k-contribution`, `resources-allocated` | `strategy/projects/quick-money/strategy.md` | P0 |
| T-06 | `tpl-task.md` | `templates/` (NEW) | `type: task`, `status: backlog/today/in-progress/done/blocked`, `project-slug`, `estimate`, `next_action`, `created` | `tasks/master.md` entry | P1 |
| T-07 | `tpl-tool-card.md` | `templates/` (NEW) | `type: tool`, `category`, `purpose`, `install-ref`, `usage-example`, `status: active/experimental/deprecated` | `tools-catalog/claude-code.md` | P1 |
| T-08 | `tpl-daily.md` | `templates/` (обновить, добавить draft-link раздел) | `type: daily-log`, `date`, `plan`, `work-blocks`, `reflection`, `drafts: []` | `daily-log/2026-04-19.md` | P1 |
| T-09 | `tpl-daily-draft.md` | `templates/` (NEW) | `type: draft`, `topic`, `parent-day`, `promoted-to: null | <path>` | `daily-log/drafts/2026-04-19-pricing-notes.md` | P1 |
| T-10 | `tpl-reflection-entry.md` | `templates/` (NEW) | `type: reflection`, `date`, `trigger: daily/weekly/event`, `insights: []` | `reflection/log.md` entry | P2 |
| T-11 | `tpl-crm-contact.md` | `templates/` (обновить tpl-contact) | `type: contact`, `category: clients/partners/personal`, `name`, `stage`, `last-touch`, `notes-ref` | `crm/clients.md` entry | P2 |
| T-12 | `tpl-adr.md` | `templates/` (NEW, для будущих `docs/adr/`) | `type: adr`, `number`, `title`, `status: proposed/accepted/superseded`, `date`, `context`, `decision`, `consequences` | `docs/adr/0019-permission-matrix.md` (v1-final) | P3 |

### 3.2 Порядок создания

Сначала P0 (T-01 → T-05), затем P1 (T-06 → T-09), потом P2/P3. P0 блокирует Шаги 4-6.

1. **T-01 `tpl-project-overview.md`** — обновить существующий, добавить обязательные `budget-hours`, `budget-weeks`, `kill-criterion`, `next_action` (I-23). Это первый фильтр против zombie-проектов.
2. **T-02 `tpl-decision.md`** — нужен для логирования решений + `/propagate-decision` (I-29). Без него decisions/ не запустить.
3. **T-04 + T-05 Strategy templates** — блокируют Шаг 6 (стратегический план на 2-3 недели).
4. **T-03 Hypothesis** — блокирует `hypotheses/` в Шаге 4.
5. **T-06 — T-09** — ежедневная гигиена.
6. **T-10 — T-12** — по мере надобности.

### 3.3 Критерий завершения Шага 3

- [ ] Все 12 templates существуют в `templates/` с корректным frontmatter.
- [ ] Для каждого template в первом `example usage` комментарии описано, куда кладётся готовый файл.
- [ ] P0 (T-01 — T-05) прошли ручную проверку Ruslan'а.
- [ ] `/lint` validator знает какие обязательные поля проверять для каждого `type:` (v1-beta это может быть хардкод в `tools/lint.py`, не separate schema JSON).
- [ ] Commit: `[templates] add: v1-beta canonical templates (T-01..T-12)`.

### 3.4 Оценка времени и блокеры

- **Время:** P0 (5 templates) — 2-3 часа чистой работы. Остальные — 2 часа.
- **Блокеры (требуют решения Ruslan'а):**
  - B-3.1: Должен ли `kill-criterion` быть строкой или структурированным полем (`if <metric> < <threshold> by <date>`)? **Предложение:** строка свободного формата в v1-beta, formal schema в v1-final.
  - B-3.2: CRM category `personal.md` — в git-tracked или `.gitignore`? **Предложение:** git-tracked (private repo), но `tpl-crm-contact.md` добавляет опциональный `sensitive: true` флаг.
  - B-3.3: Нужен ли отдельный template для `wiki/experiments/*.md` (сейчас tpl-kb-article покрывает)? **Предложение:** нет, experiment = claim+status, шаблон не нужен отдельно.

---

## Шаг 4 — Папочная структура

**Цель.** Привести репо в соответствие с §4.1 SYSTEM-DESIGN-HUMAN (target
structure для v1-beta) без потери существующих данных.

### 4.1 Diff — текущее состояние vs target

**Уже есть** (не трогать): `agents/`, `comms/`, `crm/`, `daily-log/`, `design/`, `inbox/`, `projects/`, `raw/`, `reports/`, `scripts/`, `shared/`, `templates/`, `tools/`, `wiki/`, `.claude/`.

**Создать** (отсутствует в репо):

| Папка | Назначение | Template якорь |
|-------|------------|----------------|
| `strategy/life/` | yearly/monthly/weekly life strategy | T-04 |
| `strategy/projects/` | per-project strategy files | T-05 |
| `decisions/` | life-level decisions log + monthly | T-02 |
| `tasks/` | `master.md` общий пул | T-06 |
| `hypotheses/` | `active.md`, `backlog.md`, `validated-archive.md` | T-03 |
| `tools-catalog/` | карточки инструментов | T-07 |
| `reflection/` | `log.md` + `insights/` mini-wiki | T-10 |
| `health/` | `habits-tracker.md`, `log.md`, `wiki/` | (без template в v1-beta) |
| `ideas-pool/` | `inbox.md` — общий пул идей вне проектов | (используем tpl-kb-article) |
| `daily-log/drafts/` | песочница дня (GitHub-style feature branches) | T-09 |
| `docs/adr/` | placeholder для будущих ADR files | T-12 (v1-final) |

**Рекомендуется удалить / архивировать** (TD из §14.2):

| Путь | Действие | Rationale |
|------|----------|-----------|
| `automations/` | удалить (`rm -rf`) | TD-08 — пустая папка, не нужна при autonomy=0 |
| `agents/content-team/`, `agents/research-team/`, `agents/sales-team/`, `agents/_shared/` | проверить содержимое, archive в `agents/_archive/` если не пусто | TD-03 — orphan folders |
| `projects/01-research/`, `02-business/`, `03-community/`, `04-ai-tools/`, `05-life-os/`, `06-engineering/`, `07-brand/`, `08-bets/` | смёржить с названными аналогами (`research/`, `quick-money/`, ...), архивировать префиксные | Дубликаты structure (numbered + named) |
| `ARCHITECTURE.md` | переместить в `docs/legacy/ARCHITECTURE-2026-04-14.md` | Замещён ARCHITECTURE-CURRENT + ARCHITECTURE-TARGET |
| `test-sync.md` | удалить | 27 байт, тест синхронизации |

**Рекомендуется оставить без изменений до решения Ruslan'а:**

- `knowledge-base/` (legacy, в MIGRATION.md процесс) — **не трогать**, идёт отдельной миграцией.
- `chat-journal/`, `command-center/`, `ideas/` (legacy), `logs/`, `_meta/`, `dashboard/`, `HOME.md`, `MIGRATION.md`, `private/`, `ARCHITECTURE-CURRENT.md`, `prompts/`, `reviews/` — остаются.

### 4.2 Конкретные команды

Выполнять последовательно, после каждого блока — `git status` и ручная проверка.

```bash
# Block A: создание новых директорий v1-beta
cd ~/jetix-os
mkdir -p strategy/life strategy/projects
mkdir -p decisions tasks hypotheses tools-catalog
mkdir -p reflection/insights health/wiki ideas-pool
mkdir -p daily-log/drafts docs/adr

# Block B: инициализация placeholder .md (чтобы git track'ал пустые папки)
# Каждый init-файл использует соответствующий template из Шага 3.
touch strategy/life/README.md decisions/life-decisions-log.md
touch tasks/master.md hypotheses/active.md hypotheses/backlog.md
touch hypotheses/validated-archive.md tools-catalog/README.md
touch reflection/log.md health/log.md ideas-pool/inbox.md
touch docs/adr/README.md

# Block C: удалить пустое/ненужное (ТОЛЬКО после подтверждения Ruslan'а)
rm -rf automations/
rm test-sync.md
git mv ARCHITECTURE.md docs/legacy/ARCHITECTURE-2026-04-14.md  # сначала mkdir -p docs/legacy

# Block D: архивация orphan agents (проверить содержимое сначала)
mkdir -p agents/_archive
# git mv agents/content-team agents/_archive/
# git mv agents/research-team agents/_archive/
# git mv agents/sales-team agents/_archive/
# git mv agents/_shared agents/_archive/

# Block E: слияние projects/ дубликатов — ручная проверка каждой пары
# (не автоматически — высокий риск потери данных)
```

### 4.3 Критерий завершения Шага 4

- [ ] Все 11 новых папок из §4.1 существуют с минимум одним файлом (placeholder или реальный entry).
- [ ] `automations/` и `test-sync.md` удалены.
- [ ] `ARCHITECTURE.md` legacy перемещён.
- [ ] Дубликаты `projects/NN-*/` либо объединены с именованными аналогами, либо решение «оставить как есть» задокументировано.
- [ ] Orphan agent folders разрешены (archive либо integrate).
- [ ] `git status` чистый. Commit: `[meta] v1-beta folder structure: align with SYSTEM-DESIGN-HUMAN §4.1`.

### 4.4 Оценка времени и блокеры

- **Время:** Block A-B — 15 мин. Block C-E — 1-2 часа (ручная проверка каждого move).
- **Блокеры (Ruslan):**
  - B-4.1: projects/ дубликаты — как объединять? Какой из двух (`01-research/CONTEXT.md` или `research/*`) — canonical? **Предложение:** named-версия canonical, numbered archive если содержит unique файлы.
  - B-4.2: orphan agent folders — archive или удалить? **Предложение:** archive в `agents/_archive/` с датой, не удалять.
  - B-4.3: `knowledge-base/` — когда завершать миграцию? Вне scope Шага 4, но нужно решение в ближайшие 2 недели.

---

## Шаг 5 — Обработка заметок (voice-memos + inbox)

**Цель.** Закрыть TD-14 (voice-memos 0% transcribed — по inventory от 16.04). Обработать накопленные source файлы через voice-pipeline и `/ingest`.

### 5.1 Текущее состояние

- `raw/voice-memos/` — **73 .ogg файла** (апрель 2026).
- `raw/transcripts/` — **73 .txt файла** (имена совпадают один-в-один).

**Вывод:** транскрипция выполнена для всех, то есть pipeline шаги 1-2 (`transcribe.py` + `extract.py`) уже прогнаны. Но:

- Неясно, прогнан ли `filter.py` + `review_report.py` → `~/review-latest.md` для всех 73.
- Неясно, сделан ли `/ingest` в wiki для тех, которые прошли ручное ревью.
- TD-14 считает их «не обработанными» значит по крайней мере финальный writeback в wiki не выполнен.

### 5.2 План обработки

**Этап 5.A — аудит.** Перед массовым прогоном — понять cutoff.

```bash
# Проверить когда последний раз запускался filter + review
ls -la ~/jetix-os/reports/review_*.md | tail -5
ls -la ~/review-latest.md
cat ~/jetix-os/reports/review_2026-04-15.md | head -30
```

Цель аудита — отделить (a) уже обработанные батчи (writeback done) от (b) ожидающих review от (c) нетронутых.

**Этап 5.B — дообработка filter + review для непрогнанных.**

Если есть транскрипты без соответствующего `review_YYYY-MM-DD.md` entry или `extracted/` output — прогнать через `tools/filter.py` + `tools/review_report.py`. Это не требует интернета/LLM для работающего кода, но LLM нужен для extract/filter steps.

**Этап 5.C — ручное ревью Ruslan'а.** `review-latest.md` → Ruslan читает, принимает решения. Это — human gate (ADR-004). `distribute.py.bak` остаётся выключенным — агент не пишет в wiki без явного approve.

**Этап 5.D — writeback через `/ingest`.** По approved items Ruslan запускает `/ingest <transcript-path>` для каждой релевантной заметки (или батчом). Писать в `wiki/ideas/`, `wiki/claims/`, `wiki/sources/` в зависимости от типа.

**Этап 5.E — inbox/.** Проверить `inbox/` на остатки (notion-dump'ы, неразобранные источники). Обработать через `/ingest` или переместить в `raw/` если ещё не финализировано.

### 5.3 Критерий завершения Шага 5

- [ ] Аудит voice-memos даёт чёткий список: processed / pending-review / not-started.
- [ ] Все 73 транскрипта имеют статус: либо writeback в wiki/, либо explicit «skip» (некоторые заметки могут оказаться нерелевантными — это ок, документируется).
- [ ] `inbox/` пуст ИЛИ содержит только in-progress файлы (с `status: draft` во frontmatter).
- [ ] Отчёт `reports/voice-memos-batch-closure-2026-04-18.md` фиксирует результат.
- [ ] Commit: `[raw] voice-memos batch closure + wiki writeback`.

### 5.4 Оценка времени и блокеры

- **Время:** 5.A аудит — 30 мин. 5.B дообработка — 30-60 мин машинного времени. 5.C ручное ревью Ruslan'а — 1-2 часа (зависит от количества pending). 5.D writeback — 1-2 часа в режиме `/ingest`.
- **Блокеры (Ruslan):**
  - B-5.1: Есть ли среди 73 заметок чувствительные личные, которые **не надо** в wiki ни в каком виде? **Предложение:** Ruslan на этапе 5.C помечает такие «archive-only» — остаются в `raw/` (immutable), не попадают в wiki.
  - B-5.2: Нужен ли batch-ingest skill или обрабатываем по одной? **Предложение:** v1-beta — по одной через `/ingest`; batch-skill — nice-to-have v1-final.
  - B-5.3: Что делать со старыми `pipeline_test_*.txt`, `debug-git*.md`, `output.txt` и прочими артефактами в `~/` (outside repo)? Часть — мусор от старых прогонов. **Предложение:** отдельная cleanup-сессия после Шага 6, не смешивать.

---

## Шаг 6 — Стратегический план 2-3 недели

**Цель.** Создать первый реальный `strategy/life/2026-04-monthly.md` + `2026-W17-weekly.md`, привязанный к $50K до 30.06.2026. Это первая «боевая» проверка templates Шага 3 + папок Шага 4.

### 6.1 Файлы

| Файл | Template | Scope |
|------|----------|-------|
| `strategy/life/2026-yearly.md` | T-04 (level: yearly) | 2026-12-31: north star + 4 квартальных milestone'а |
| `strategy/life/2026-04-monthly.md` | T-04 (level: monthly) | апрель 2026: focus blocks, trackable metrics |
| `strategy/life/2026-W17-weekly.md` | T-04 (level: weekly) | 20-26.04.2026: daily-level breakdown |
| `strategy/projects/quick-money/strategy.md` | T-05 | quick-money — ближайший к $50K проект |

### 6.2 Секции weekly file (T-04 template применён)

```
frontmatter: type: strategy-life, level: weekly, period: 2026-W17,
             north-star: "$50K до 30.06.2026", focus-blocks: [...],
             budget-resources: {hours: N, money: $N, attention: ...}

# Неделя W17 (2026-04-20 → 2026-04-26)

## Point A
— где я на начало недели (из monthly + W16 reflection)

## Point B — что достигаем к воскресенью 2026-04-26
— 2-3 измеримых результата

## Focus-blocks
1. [quick-money] — N часов
2. [architecture-obkatka] — N часов (v1-beta проверка)
3. [reflection/health] — N часов

## Daily breakdown
пн — {focus + блокеры}
вт — ...
...

## Hypotheses активные (cross-link в hypotheses/active.md)
— H-001: ...
— H-002: ...

## Decisions ожидаются
— ...

## Kill-criteria на конец недели
— если quick-money не сдвигается на метрику X — пересматриваем в W18 ritual
```

### 6.3 Связь с $50K goal

Каждый strategy-файл (weekly/monthly/yearly) во frontmatter имеет поле
`metric-50k-contribution: <short>` — прямо отвечает «как этот период
двигает нас к $50K». Примеры:

- yearly: «$50K revenue = N clients × avg ticket $X; Q2 milestone = первая выручка».
- monthly (апрель): «quick-money: найти первого платящего клиента; контент-канал: 2 публичных поста».
- weekly (W17): «quick-money: 3 outreach meetings; offer spec draft; architecture obkatka чтобы не блокировала продажи».

Если неделя прошла без прогресса по `metric-50k-contribution` — это red flag
на weekly ritual, требует пересмотра scope или kill-criterion (ADR-004 семимануал не мешает — Ruslan сам видит).

### 6.4 Критерий завершения Шага 6

- [ ] 4 файла (yearly, monthly, weekly, quick-money strategy) существуют с заполненным контентом (не placeholder).
- [ ] Каждый имеет frontmatter в соответствии с T-04/T-05.
- [ ] `quick-money/strategy.md` связан с `strategy/projects/quick-money/` через Obsidian transclude или явный `[[link]]`.
- [ ] `metric-50k-contribution` заполнен везде.
- [ ] `/plan-day` на 2026-04-20 успешно подгружает weekly scope (первая боевая проверка).
- [ ] Commit: `[strategy] v1-beta initial strategic plan — W17-W19 + monthly + yearly + quick-money`.

### 6.5 Оценка времени и блокеры

- **Время:** yearly — 30 мин. monthly — 45 мин. weekly — 30 мин. quick-money strategy — 1 час (требует осмысленного reflection). Итого 2-3 часа Ruslan'а (не делегируется агенту — L3 strategy, human gate I-11).
- **Блокеры (Ruslan):**
  - B-6.1: Какой формат `north-star` — одна фраза или набор под-целей? **Предложение:** одна фраза + 3-4 sub-milestones ниже.
  - B-6.2: quick-money — реально ли приоритет P1? Нет ли проекта ближе к первой выручке? **Требует решения Ruslan'а до Шага 6**, не от агента.
  - B-6.3: 4-5h/день vs fixed-hours budget — как распределить between focus-blocks? **Предложение:** 50% quick-money, 30% infrastructure/obkatka, 20% reflection/health/брain-space.

---

## Общая последовательность исполнения

```
День 1 (2026-04-19, суббота)
  └── Шаг 3 P0: T-01 до T-05 (3 часа)
  └── commit + push

День 2 (2026-04-20, воскресенье)
  └── Шаг 4: Block A-B создать папки (30 мин)
  └── Шаг 4: Block C-D удалить/архивировать — requires Ruslan decisions B-4.1, B-4.2 (1-2 часа)
  └── Шаг 3 P1: T-06 до T-09 (1 час)
  └── commit + push

День 3 (2026-04-21, понедельник) — ↩︎ рабочая неделя начинается
  └── Шаг 6: yearly + monthly + weekly + quick-money strategy (2-3 часа) — Ruslan lead
  └── Шаг 3 P2: T-10, T-11 (30 мин)
  └── commit + push

Дни 4-7 (2026-04-22 → 2026-04-25)
  └── Шаг 5: voice-memos audit + batch closure (параллельно с обычной работой)
  └── v1-beta obkatka — каждый агент запускается ≥1 раз на реальной задаче (closes R-02)
  └── commit + push ежедневно

Воскресенье 2026-04-26 — первый полный weekly ritual на новой структуре
  └── /review week + /cross + `reports/metrics-delta-W17.md`
  └── Решение: что работает, что нет, что чинить в W18
```

## Критерии завершения всей фазы воплощения

- [ ] Шаг 3: 12 templates canonical ✓
- [ ] Шаг 4: папочная структура == §4.1 SYSTEM-DESIGN-HUMAN ✓
- [ ] Шаг 5: voice-memos backlog обработан ✓
- [ ] Шаг 6: первый реальный стратегический документ W17-W19 + monthly + yearly + quick-money ✓
- [ ] Первый `/plan-day` на новой структуре прошёл без блокеров
- [ ] `/lint` чистый OR список known debt задокументирован в `reports/v1-beta-go-live-YYYY-MM-DD.md`
- [ ] Git tag `v1-beta-live-2026-04-26` (или другая дата)

---

## Что Plan НЕ покрывает (out of scope)

- Реализация `tools/llm.py` LLM abstraction (ADR-005) — v1-beta architectural ready; operational swap — отдельная задача v1-final backlog.
- Реализация `tools/query.py` DuckDB + `tools/hipporag.py` — nice-to-have v1-beta, блокеров на $50K не создают.
- `./jetix` unified CLI — сначала обкатать ritual flow, затем wrapper.
- Meta-agent weekly audit cycle — v1-final cadence, в v1-beta triggered manually.
- Notion migration γ/δ — отдельный план в `design/NOTION-MIGRATION-PLAN.md`.
- Onboarding partner/deputy (R-09 mitigation) — v1-final scope.

---

## Risk reminder для Ruslan'а

Три риска, которые могут сорвать эту фазу (из TECH §14.1 + honest retrospective):

1. **R-12: 2-week offline сейчас = rollback.** Фаза обкатки требует ежедневного ритма. Если недельный перерыв неизбежен — **explicit pause** с Git tag + note в `decisions/`, возврат через 5-10 мин recap.
2. **R-09 + B-6.2: $50K goal honest recheck.** Если quick-money не двинется за 2 недели на реальную метрику — это сигнал пересмотреть scope v1-beta obkatka VS скорость продаж, не наоборот. Архитектура — enabler, не self-goal.
3. **Analysis paralysis.** Соблазн «ещё один synthesis round» перед воплощением. План — **готов к действию**. Approve → execute → retrospective W17 → iterate. Не iterate до execute.

---

*Implementation plan v1-beta-FINAL-2026-04-18. ~330 строк. Привязан
к утверждённой архитектуре `design/SYSTEM-DESIGN-TECH.md` v1-beta-FINAL.
Каждый шаг — с явными blocker'ами под решение Ruslan'а и criterion
завершения. Правь файл по ходу исполнения (append decisions как
`[plan] update: B-X.Y resolved by ...`), не переписывай.*
