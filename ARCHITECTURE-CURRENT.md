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

## 2. Component Deep-Dive — Layered + Data Flow

**Miro header doc:** [`2. Component Deep-Dive`](https://miro.com/app/board/uXjVG2-05Ns=/?moveToWidget=3458764668118323824).
Шесть диаграмм расположены вертикально по `x≈-100000`, `y` от `-20000` до `5000`.

Цвета те же: жёлтый = agent/app процессы, синий = data, зелёный = pipeline/skill,
серый = external.

### 2.1 IO Layer

[`2A. IO Layer`](https://miro.com/app/board/uXjVG2-05Ns=/?moveToWidget=3458764668118140988)

- **Drop zones:** `inbox/voice`, `inbox/text`, `inbox/articles`, `inbox/chats`.
- **Voice pipeline (Python):** `tools/transcribe.py` (Groq Whisper) →
  `tools/extract.py` (Claude → items) → `tools/filter.py` (dedup + meta) →
  `tools/review_report.py`. Оркестратор: `tools/run_pipeline.sh`.
- **Raw archive:** `raw/voice-memos`, `raw/transcripts`, `raw/articles`,
  `raw/books`, `raw/meetings`, `raw/web`, `raw/imports`, `raw/research`,
  `raw/notion-ideas`.
- **Human gate:** `~/review-latest.md` + `reports/review_YYYY-MM-DD.md` —
  обязательный STOP перед распределением.
- **Processed/triage:** `inbox/processed/`, `inbox/archive/`. Triage пока
  делается вручную/частично (`tools/distribute.py.bak` отключён); шаг
  «inbox-processor → triage report» помечен **planned**.

### 2.2 Knowledge Layer

[`2B. Knowledge Layer`](https://miro.com/app/board/uXjVG2-05Ns=/?moveToWidget=3458764668118513490)

- **`wiki/` (active):** `index.md` (165 строк), `log.md` (append-only),
  `overview.md`, 9 entity-папок (concepts, entities, sources, topics, ideas,
  experiments, claims, summaries, foundations), `comparisons/`, `niches/` (6),
  `_templates/` (9), `_lint-report-2026-04-16.md` (+v2).
- **`wiki/graph/` (HippoRAG):** `edges.jsonl` (137 typed edges, 9 типов),
  `communities.md` (4 кластера), `summaries.md`.
- **`knowledge-base/` (legacy):** `ai-consulting/`, `market/`, `sales/`,
  `_health/`. Все четыре — в миграции (`MIGRATION.md`), 0% выполнено.
- **`shared/knowledge/` (agent outputs):** `research-summaries/` (читают
  sales-lead, knowledge-synth), `client-insights/` (пишут sales-агенты),
  `life/` (пишет life-coach), `crazy-ideas/` (пишет crazy-agent),
  `decisions-log.jsonl` (пишет strategist).

### 2.3 Agents + Skills Layer

[`2C. Agents + Skills Layer`](https://miro.com/app/board/uXjVG2-05Ns=/?moveToWidget=3458764668118676020)

- **Agent definitions:** `.claude/agents/*.md` (12 system prompts).
- **Per-agent memory (5 layers):** `agents/{id}/system.md` (рабочая копия),
  `baseline.md` (immutable v1.0), `strategies.md` (System Prompt Learning),
  `scratchpad.md` (working memory), `niche/` (24 symlinks на `wiki/niches/*`).
- **Skills:** активные — `/ingest`, `/ask`, `/lint`, `/consolidate`,
  `/build-graph`, `/plan-day`, `/close-day`, `/focus`. Legacy — `/compile`,
  `/search-kb` (от старого raw → ingested → compiled пайплайна).
- **Mailboxes:** `comms/mailboxes/*.jsonl` (12 + `human.jsonl`). Все сообщения
  conform `shared/schemas/message.schema.json` (regex `msg-YYYYMMDD-NNN`,
  enum from + 8 types + 4 priorities + 5 statuses).
- **Shared state:** `active-projects.json`, `daily-briefing.json`,
  `focus.json`, `kanban.json`, `priorities.json`, `system-config.json`,
  `system-health.json`, `contacts.json`, `metrics/` (agent-performance,
  ab-tests, feedback).
- **Schemas + rules:** `briefing.schema.json`, `message.schema.json`,
  `task.schema.json`, `.claude/rules/global.md`.

### 2.4 Apps Layer

[`2D. Apps Layer`](https://miro.com/app/board/uXjVG2-05Ns=/?moveToWidget=3458764668118676161)

- **Frontend (TanStack):** `dashboard/src/` (components, features, routes,
  stores, lib). Build → `dashboard/dist/`. Fetches `/api/v1/*`.
- **Backend (Express):** `dashboard/server/index.js` монтирует 9 routes:
  `agents`, `chat`, `coordination`, `decisions`, `focus`, `kanban`,
  `observability`, `projects`, `state`. Routes читают `agents/{id}/*`,
  `comms/mailboxes/*.jsonl`, `shared/state/*.json`.
- **Bash scripts:** `morning-pipeline.sh`, `evening-pipeline.sh` (запускают
  `run-agent.sh`, который дёргает manager); `read-mailbox.sh`,
  `send-message.sh` (cat/append на `comms/mailboxes/*`); `rollback.sh`.
- **Voice-notes pipeline (Python):** `run_pipeline.sh` цепочкой запускает
  `transcribe.py · extract.py · filter.py · summarize.py · review_report.py`.
  Также `sync_context.py`. `distribute.py.bak` — disabled, distribute по KB
  не запускается автоматически (ручное ревью обязательно).

### 2.5 External Layer

[`2E. External Layer`](https://miro.com/app/board/uXjVG2-05Ns=/?moveToWidget=3458764668118676501)

- **Notion (external truth):** Command Center, Daily Log DB, Projects DB,
  Journal of Chats, Банк идей, ICP Page, Research Hub, Life OS — все 8
  IDs зашиты в CLAUDE.md и в системных промптах manager/inbox-processor/
  knowledge-synth/life-coach/sales-lead.
- **Code & vault:** GitHub `Bogersebekov/jetix-os`, локальный `~/jetix-os`,
  Obsidian vault на `wiki/`.
- **Boards:** Miro `uXjVG2-05Ns=` (содержит фреймы из этого документа +
  старые planning-фреймы Руслана).
- **Infra:** VPS Ubuntu 24 (`100.99.156.28`), Anthropic API
  (Opus 4.6 / Sonnet 4.6 / Haiku 4.5 — по `model:` в каждом agent definition),
  Groq Whisper API (для `transcribe.py`).
- **MCP bridges:** `notion` и `miro` — оба активны. Использование Notion MCP
  падает, если сервер MCP отключается (наблюдали на этой сессии).

### 2.6 Data Flow Overlay

[`2F. Data Flow Overlay`](https://miro.com/app/board/uXjVG2-05Ns=/?moveToWidget=3458764668118323633)

Поверх layered-разреза — основной writeback-цикл знаний:

1. **Ingestion:** `raw/` файл (или URL → `raw/web/`) → `/ingest <path|url>` →
   создаёт/обновляет `wiki/{type}/*.md`, `wiki/sources/YYYY-MM-DD-*.md`,
   обновляет `wiki/index.md`, append в `wiki/log.md` и `wiki/graph/edges.jsonl`,
   линкует в `wiki/niches/{niche}/README.md`. Сюда же приходят
   `raw/transcripts/` (через voice pipeline), `raw/notion-ideas/` (export),
   `knowledge-base/*` (legacy migration).
2. **Graph build:** `/build-graph` сканирует все wiki-страницы, добивает edges
   по типам секций ("## Расширяет/Extends" → `extends`, "Противоречит" →
   `contradicts` и т.д., 9 типов), ищет связные компоненты, перезаписывает
   `wiki/graph/communities.md` и `wiki/graph/summaries.md` (HippoRAG layer
   для `/ask`).
3. **Query (writeback loop):** пользователь задаёт `/ask <вопрос>`. Skill
   читает `index.md`, `summaries.md`, отбирает 5-15 страниц, синтезирует
   ответ с цитатами `[[file.md]]`. Если ответ ценный (новая связь между
   2+ страницами / противоречие / synthesis по 5+ / практический вывод) —
   сохраняет `wiki/comparisons/YYYY-MM-DD-slug.md`, обновляет index/log,
   **append-ит новые edges** обратно в `edges.jsonl` (writeback).
4. **Maintenance:** `/lint` (orphans, contradictions, stale claims) → отчёт
   в `wiki/_lint-report-YYYY-MM-DD.md`. `/consolidate` (merge dupes по
   similarity) — переписывает страницы с merge-notice.

---

## 3. Component-Level Detail

_Заполняется на следующем уровне._
