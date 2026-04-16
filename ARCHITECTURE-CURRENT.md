---
type: architecture-snapshot
date: 2026-04-16
status: living-doc
scope: as-is, не to-be
author: claude-code
miro_board: https://miro.com/app/board/uXjVG2-05Ns=/
---
# Jetix OS — Architecture Snapshot (2026-04-16)

Документ описывает **то что есть** на 2026-04-16. Без планов, без "хорошо бы".
Источники правды: файловая система `~/jetix-os`, `git log`, `CLAUDE.md`,
`MIGRATION.md`, `reports/`, `wiki/`.

Соответствующие фреймы в Miro: см. ссылку выше. Один уровень = один фрейм + одна
секция здесь. Термины в Miro и в md — совпадают.

Цветовая схема (одинаковая на всех уровнях):

| Цвет | Значение |
|------|----------|
| `#fff6b6` (жёлтый) | agents, app-процессы |
| `#c6dcff` (синий)  | knowledge / data stores |
| `#adf0c7` (зелёный)| pipelines, skills, scripts, tools |
| `#e7e7e7` (серый)  | external systems |

---

## 1. Birds-Eye View

**Miro diagram:** [`1. Birds-Eye View — Jetix OS (snapshot 2026-04-16)`](https://miro.com/app/board/uXjVG2-05Ns=/?moveToWidget=3458764668117439526)
(координаты `x=-60000, y=-50000`).

### Корень

`~/jetix-os` — git-репозиторий (`Bogersebekov/jetix-os`). Текущая ветка:
`claude/xenodochial-jennings`. Главная ветка: `main`. Последний коммит:
`34a0e95 [wiki] report: ideas-import-batch2-2026-04-16`.

### Высокоуровневые блоки (что есть прямо сейчас)

#### Agents & orchestration (жёлтый + зелёный)

- **12 Agents · 6 departments** — определения в `.claude/agents/*.md` (12 файлов)
  и расширенная per-agent memory в `agents/{id}/` (system.md, strategies.md,
  scratchpad.md, niche/ symlinks).
- **`.claude/skills/`** — slash-commands. Реализованы: `/ingest`, `/ask`,
  `/lint`, `/consolidate`, `/build-graph`, `/compile`, `/search-kb`,
  `/plan-day`, `/close-day`, `/focus`.
- **`comms/mailboxes/`** — JSONL-шина. 12 файлов на агентов + `human.jsonl`.
  Активные (с трафиком на 2026-04-16): manager, sales-lead, strategist,
  system-admin, crazy-agent, life-coach. Пустые: остальные 7.
- **`shared/state/`** — JSON-файлы:
  active-projects, contacts, daily-briefing, focus, kanban, priorities,
  system-config, system-health + `metrics/`. Схемы в `shared/schemas/`
  (briefing, message, task).

#### Knowledge layer (синий)

- **`wiki/`** — KB v2 по архитектуре «Karpathy LLM Wiki + OmegaWiki».
  9 entity types (concepts/, entities/, sources/, topics/, ideas/, experiments/,
  claims/, summaries/, foundations/), 6 niches (personal, business, sales, life,
  tech, meta), `graph/edges.jsonl` (137 edges), `index.md` (165 строк),
  `log.md` (81 строка). Импортировано 60 идей из Notion, ~135 страниц всего,
  4 communities. Lint-репорты: `_lint-report-2026-04-16.md`,
  `_lint-report-2026-04-16-v2.md`.
- **`raw/`** — источники: `transcripts/`, `voice-memos/`, `articles/`, `books/`,
  `meetings/`, `web/`, `notion-ideas/`, `imports/`, `research/`.
- **`knowledge-base/`** — **legacy**, в миграции (см. `MIGRATION.md`). Кластеры:
  `ai-consulting/`, `market/`, `sales/`, `_health/`. Ни один не перенесён в wiki/
  (галочки `[ ] не начато`).

#### Apps & pipelines (зелёный + жёлтый)

- **`tools/`** — voice-notes pipeline (Python). Шаги: `transcribe.py`
  (Groq Whisper) → `extract.py` (Claude) → `filter.py` (дедуп) →
  `review_report.py` (markdown в `reports/review_YYYY-MM-DD.md` +
  `~/review-latest.md`). Раннер: `run_pipeline.sh`.
  Также: `summarize.py`, `sync_context.py`. `distribute.py.bak` — отключён
  (ручное ревью обязательно).
- **`scripts/`** — bash: `morning-pipeline.sh`, `evening-pipeline.sh`,
  `read-mailbox.sh`, `run-agent.sh`, `send-message.sh`, `rollback.sh`.
- **`dashboard/`** — отдельное приложение. Frontend: TanStack React (`src/`),
  Express server (`server/index.js`). Server routes: `agents`, `chat`,
  `coordination`, `decisions`, `focus`, `kanban`, `observability`,
  `projects`, `state`. Build: `dist/`. На API path `/api/v1/`
  (см. коммит `c4acbf0`).

#### Operational data (синий, не KB)

- `projects/` — 8 активных проектов + старые номерные дубли (`01-research/` …
  `08-bets/`) + `_template/`.
- `crm/contacts/`, `inbox/` (archive, articles, chats, processed, text, voice),
  `ideas/`, `daily-log/`, `chat-journal/`, `command-center/`,
  `private/` (finance, journal, strategy).

#### External sinks (серый)

- **Notion** — external truth (Command Center `3322496333bf8161b6d3ea789d039356`,
  DBs: Daily Log, Projects, Journal, Банк идей, ICP, Research Hub, Life OS).
- **GitHub** — `Bogersebekov/jetix-os`, ветки `main` + `claude/xenodochial-jennings`.
- **Obsidian** — vault, открытый на `wiki/` (Руслан вручную).
- **Miro** — board `uXjVG2-05Ns=` (этот документ описывает фреймы там).
- **VPS Ubuntu 24** (`100.99.156.28`) — где живёт server-side Claude Code
  и фоновые pipeline'ы.

### Что упомянуто, но НЕ построено (planned / not yet built)

- Миграция `knowledge-base/ → wiki/` через `/ingest` — план есть, выполнено 0%.
- `automations/` — папка пустая.
- `voice-memos/ → wiki/` — ждёт transcribe + ingest.
- Канонизация `baseline.md` vs `system.md` для агентов — обе файла лежат с
  одинаковым содержимым, выбор не сделан.
- Конфликт `.claude/skills/ingest.md` vs `ingest.md.new` — в отчёте
  `arch-migration-2026-04-16.md` помечен как требующий ручного решения
  (на момент 2026-04-16 — старая версия в `ingest.md`, новой `.new` нет
  в дереве; миграция уже выполнена и `.new` слит).
- Niche `global` — нет папки, только enum.
- Phase-3 фичи: hook `/close-day → wiki/summaries/`, intake `inbox-processor →
  /ingest`, миграция стратегий из `baseline.md → strategies.md`.

### Ключевые потоки на этом уровне

1. Agents читают/пишут `comms/mailboxes/*.jsonl` и `shared/state/*.json`.
2. Agents вызывают `/skills` (особенно `/ingest`, `/ask`).
3. `tools/` (voice pipeline) кладёт транскрипты в `raw/transcripts/`,
   откуда потом `/ingest` тянет их в `wiki/`.
4. `dashboard/` читает `shared/state/` и `agents/` для отображения.
5. Всё пушится в GitHub. Notion живёт параллельно (sync через ID, не file-level).
6. Obsidian читает `wiki/` локально (vault).

---

## 2. Mid-Level Detail

_Заполняется на следующем уровне._

---

## 3. Component-Level Detail

_Заполняется на следующем уровне._
