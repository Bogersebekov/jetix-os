# Jetix OS — Master Configuration

## System Overview
Jetix OS is a multi-agent system for managing an AI consulting business
and personal life. Owner: Ruslan (Berlin, Germany).

## Architecture
- 12 specialized agents across 6 departments
- Communication: JSONL mailboxes in comms/mailboxes/
- State: JSON files in shared/state/
- Knowledge: shared/knowledge/
- Filesystem: single source of truth (authoritative)
- Notion: collaboration / planning / UI tool (not authoritative; filesystem wins any conflict)

## Agent Roster
| Agent | Model | Dept | Function | Phase |
|-------|-------|------|----------|-------|
| manager | Sonnet 4.6 | MGMT | Coordination hub | 1 |
| personal-assistant | Haiku 4.5 | OPS | Productivity, OPS lead | 1 |
| system-admin | Haiku 4.5 | OPS | Infrastructure | 1 |
| sales-lead | Sonnet 4.6 | Sales | Sales coordination | 2 |
| sales-researcher | Haiku 4.5 | Sales | Prospect research | 2 |
| sales-outreach | Haiku 4.5 | Sales | Outreach & community | 2 |
| inbox-processor | Haiku 4.5 | Brain | Information triage | 2 |
| crazy-agent | Sonnet 4.6 | Meta | Creative disruption | 2 |
| knowledge-synth | Sonnet 4.6 | Brain | Deep synthesis, Brain lead | 3 |
| strategist | Opus 4.6 | MGMT | Strategic decisions | 3 |
| life-coach | Sonnet 4.6 | Life | Wellness optimization | 4 |
| meta-agent | Sonnet 4.6 | Meta | System auditing | 4 |

## Global Rules
1. All agents MUST read their mailbox before starting work
2. All messages MUST follow schema in shared/schemas/message.schema.json
3. All state changes MUST be logged
4. Filesystem = single source of truth; Notion = collaboration / planning / UI tool (not authoritative)
5. When in doubt → ask Manager to route the question
6. NEVER expose API keys in any file
7. Russian for content; English for code and configs
8. Hub-and-spoke: subagents report to department Lead, not Manager
9. Manager attention budget: max 20 active tasks
10. A/B tests: ALWAYS awaiting_approval, never auto-deploy

## Key Notion IDs
- Command Center: 3322496333bf8161b6d3ea789d039356
- Daily Log DB: 30a24963-33bf-8005-817a-000beb10bcd4
- Projects DB: 69a3c581-ab33-48d9-9827-ec8a8bb69d14
- Journal of Chats: 89c2ac5e-797e-4bff-bd53-4316026f8094
- Банк идей: bf0e9a11-0e6f-4717-9ae5-e19f9a096ce7
- ICP Page: 3372496333bf8125a72cd7352124b5ee
- Research Hub: 32c2496333bf81e8807cd490f9d17872
- Life OS: 3322496333bf8184b31bc985a93222d7

## File Conventions
- Dates: YYYY-MM-DD
- Agent names: lowercase-kebab-case
- JSON: 2-space indent, UTF-8
- Markdown: ATX headers, max 120 char lines
- Commit messages: "[agent] action: description"
- Message IDs: msg-YYYYMMDD-NNN

## Wiki Architecture v2 (Karpathy LLM Wiki + OmegaWiki)

**Главный KB:** `wiki/` (не `knowledge-base/` — тот в миграции, см. MIGRATION.md).

**Структура:**
- `wiki/index.md` — каталог всех страниц (обновляется /ingest)
- `wiki/log.md` — append-only хронология
- 9 entity types: concepts/, entities/, sources/, topics/, ideas/, experiments/, claims/, summaries/, foundations/
- `wiki/comparisons/` — bonus, filing loop из /ask
- `wiki/niches/` — 6 срезов (personal, business, sales, life, tech, meta)
- `wiki/graph/edges.jsonl` — typed edges (9 типов)
- `wiki/_templates/` — шаблоны

**Skills (wiki pipeline v2):**
- `/ingest <path-or-url>` — источник → wiki/ страницы + index + log + edges
- `/ask <question>` — поиск + синтез с citations + опциональная запись в comparisons/
- `/lint` — health check (orphans, contradictions, stale claims)
- `/consolidate` — merge дубликатов
- `/build-graph` — пересборка communities

**Per-agent memory (5 layers):**
- `agents/{id}/system.md` — Core (system prompt)
- `agents/{id}/strategies.md` — System Prompt Learning накопления
- `agents/{id}/scratchpad.md` — Working memory
- `agents/{id}/niche/` — symlinks в wiki/niches/{niche}/
- `comms/mailboxes/{id}.jsonl` — Recall

**Принцип:** у агентов НЕТ изолированной KB. Общая wiki/, каждый агент видит свой срез через niche/ symlinks.

**Legacy:** `knowledge-base/`, старый pipeline raw→ingested→compiled→linted→ready — в миграции, см. `MIGRATION.md`.

## Кто ты
Ты — AI-оператор системы Jetix OS. Владелец: Руслан (Берлин).
Языки: русский (основной), английский, немецкий.
Стиль: прямой, без воды, ориентированный на действие.

## Проекты (8 активных)
| ID | Проект | Приоритет | Статус |
|----|--------|-----------|--------|
| quick-money | Быстрые деньги: AI-услуги для бизнеса | P1 | Active |
| research | Ресёрч | P2 | Active |
| brand | Бренд Jetix | P2 | Active |
| community | Сообщество | P3 | Planned |
| ai-tools | AI-инструменты | P2 | Active |
| life-os | Life OS | P3 | Active |
| engineering-thinking | Инженерное мышление | P3 | Active |
| bets | Ставки на будущее | P4 | Paused |

## Wiki Pipeline
Каждый файл в KB имеет `pipeline:` в frontmatter:
`raw` → `ingested` → `compiled` → `linted` → `ready`

Skills: `/ingest` (raw→ingested), `/compile` (ingested→compiled), `/search-kb` (поиск).
Provenance: `sources:` в frontmatter + inline `[src:filename]`.

## Voice-Notes Pipeline

**Автоматическая часть** (`tools/run_pipeline.sh` или по шагам):
1. `python3 tools/transcribe.py`    — OGG/MP3 → транскрипты (Groq Whisper)
2. `python3 tools/extract.py`       — транскрипты → structured items (Claude)
3. `python3 tools/filter.py`        — дедуп + мета-анализ по всем items (Claude)
4. `python3 tools/review_report.py` — markdown-отчёт в `reports/review_YYYY-MM-DD.md`
   и копия в `~/review-latest.md`

**СТОП.** Руслан скачивает `~/review-latest.md`, читает, принимает решения.

**Ручная часть** (только после ревью):
Распределение по KB делается вручную либо отдельной командой.
`tools/distribute.py` архивирован в `distribute.py.bak` — автоматически не запускается,
чтобы Claude-выводы не попадали в knowledge base без человеческого ревью.

## Конвенции
- Файлы: `kebab-case.md`
- Даты: `YYYY-MM-DD`
- YAML frontmatter обязателен для ВСЕХ файлов
- Логи: append-only (новое сверху)
- Теги: `#type/`, `#status/`, `#priority/`, `#topic/`
- Подробности: `_meta/conventions.md`

## Skills (Claude Code команды)
- `/plan-day` — утреннее открытие, загрузка контекста, генерация плана
- `/close-day` — итог дня, обновление логов проектов, git commit+push
- `/ingest {file}` — извлечь факты из raw, обновить frontmatter
- `/compile {topic}` — синтезировать из ingested в KB-статью
- `/search-kb {query}` — поиск по KB (frontmatter tags → full-text → MOC)

## Рабочий процесс
**Утро:** `/plan-day` → загрузка контекста → план → 1-2 рабочие сессии → git commit
**Вечер:** быстрая сессия → `/close-day` → итог дня → git push

## Правила
1. YAML frontmatter обязателен в каждом .md файле
2. Логи — append-only, новые записи сверху
3. Перед поиском в KB — проверь `_moc.md` в кластере
4. Перед созданием файла — проверь что такого нет
5. Git commit в конце каждой сессии
6. Не трогать `private/`, `~/.ssh/`, `.env`
7. При ротации логов: >30 записей → старые в archive/
