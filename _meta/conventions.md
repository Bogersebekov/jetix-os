---
type: meta
created: 2026-04-13
updated: 2026-04-13
---

# Конвенции Jetix OS

## Именование файлов
- Формат: `kebab-case.md` (строчные, дефис как разделитель)
- Даты в именах: `YYYY-MM-DD` (префикс для хронологических файлов)
- Примеры: `pricing-models.md`, `2026-04-13.md`, `2026-04-08-pivot-quick-money.md`
- Папки проектов: `kebab-case` без дат

## Даты
- Формат: `YYYY-MM-DD` везде (frontmatter, имена файлов, логи)
- Недели: `YYYY-WNN` (ISO 8601), пример: `2026-W16`

## YAML Frontmatter — обязателен для ВСЕХ .md файлов

### Общие поля (все типы)
```yaml
type: [тип]         # обязательно
created: YYYY-MM-DD # обязательно
updated: YYYY-MM-DD # обязательно
tags: []            # рекомендуется
```

### По типу файла

**project** (overview.md):
```yaml
type: project
status: active | paused | completed | archived
priority: p1 | p2 | p3 | p4
next_action: "Описание следующего шага"
owner: ruslan
```

**daily-log**:
```yaml
type: daily-log
date: YYYY-MM-DD
weekday: Monday | Tuesday | ...
energy: null | 1-10
projects_touched: []
```

**knowledge** (KB-статьи):
```yaml
type: knowledge
pipeline: raw | ingested | compiled | linted | ready
topic: cluster/subtopic
confidence: low | medium | high
sources:
  - id: path/to/raw-file.md
    facts: [fact-1, fact-2]
```

**raw** (источники):
```yaml
type: raw
pipeline: raw | ingested
source_type: perplexity | article | transcript | voice-memo | import
source_url: ""
source_date: YYYY-MM-DD
processed: true | false
extracted_to: []
```

**contact** (CRM):
```yaml
type: contact
name: "Имя Фамилия"
company: ""
role: ""
stage: lead | prospect | client | partner | mentor
language: ru | en | de
last_contact: YYYY-MM-DD
next_action: ""
```

**decision**:
```yaml
type: decision
date: YYYY-MM-DD
status: active | superseded | reversed
impact: high | medium | low
projects: []
```

**meta**:
```yaml
type: meta
```

## Система тегов
Префиксы:
- `#type/` — тип файла (knowledge, raw, project, contact)
- `#status/` — статус (active, paused, completed)
- `#priority/` — приоритет (p1, p2, p3, p4)
- `#topic/` — тема (pricing, consulting, security, market)
- `#team/` — будущее (research, sales, content)

## Логи
- Append-only: новые записи СВЕРХУ
- Формат записи: `### YYYY-MM-DD — Заголовок`
- Максимум 30 записей в файле, потом ротация в `archive/`
- Ротация: `log.md` → `log-archive/YYYY-MM.md`

## Wikilinks и ссылки
- Внутренние ссылки: относительные пути `[текст](../path/to/file.md)`
- Inline provenance: `[src:filename]` (без расширения .md)
- Пример: `Средняя ставка €150-250/час [src:pricing-dach-perplexity]`

## Специальные файлы
- `_index.md` — автогенерируемый навигационный файл (не редактировать вручную)
- `_moc.md` — Map of Content кластера KB (ручной на старте, авто при >30 файлах)
- `_template/` — папка с шаблонами проекта (копировать для нового проекта)

## Git
- Commit в конце каждой рабочей сессии
- Формат коммита: `[area] краткое описание` (пример: `[daily] close day 2026-04-13`)
- Push минимум 1 раз в день (в /close-day)
- Trunk-based development (одна ветка main)

## CRM Conventions

CRM (`crm/`) — multi-purpose contact network. Single source of truth =
filesystem (per Global Rule 4). Notion = view-only mirror. Lives рядом с
`wiki/`, не внутри.

**Filenames:**
- `crm/people/<slug>.md` — one file per person
- `crm/orgs/<slug>.md` — one file per org
- Slug pattern: `^[a-z0-9]+(-[a-z0-9]+)*$` (kebab-case, ASCII only,
  no leading underscore — schema validator enforces)
- Slug == filename without `.md`

**Frontmatter:**
- Required: `name`, `slug`, `type` (`person`|`org`), `roles` (≥1), `created`, `updated`
- Authoritative spec: `crm/_schema/frontmatter.yaml`
- Auto-fix rules: `icp.total = sum(azart+stable+adequate+upward)`, `updated >= created`

**Sections (14 standard, in template `_templates/person.md`):**
- §1 Кто, §2 Связи existing, §3 Потенциальные связи, §4 Аудитория,
  §5 Инструменты, §6 Цели его, §7 Что предлагаем, §8 Что получаем,
  §9 Гипотезы, §10 Связь с Jetix, §11 История (newest top, append-only),
  §12 Статус + next, §13 Observations / red flags, §14 Источники

**Operations only via `/crm-*` skills** (or direct `python3 -m crm._scripts.crm`).
Никогда не редактируй frontmatter вручную для status/last_touch — только через
`/crm-update` / `/crm-touch` (они обновляют `updated` field correctly).

**§11 history append-only:** newest entries at top. Format: `### YYYY-MM-DD — title`.
Never edit or delete old entries; only append new.

**Edges between contacts** (X co-founder-with Y, A founder-of B) → store в
`wiki/graph/edges.jsonl`, не в frontmatter. Edge types defined в
`wiki/graph/edge-types.md`. Auto-pulled into §2 via tooling (Phase 2 work).

**Voice items → DRAFT only:** voice_router creates `<slug>-DRAFT.md` files
with status `draft_from_voice`. Promoted manually after Ruslan review.
See `agents/inbox-processor/system.md § CRM Voice-Routing Protocol`.

**Activity log:** `crm/log.md` — append-only chronology of CRM ops (newest
top), bumped automatically by `crm.py` for add/touch/update/voice-route.

**PII discipline:**
- Real personal data only в `crm/people/` and `crm/orgs/`
- Test fixtures в `crm/_tests/fixtures/` use anonymized samples
- Reference example `crm/people/example-person.md` uses `example.invalid` domain
- Voice memos / transcripts (raw/) may contain PII — never share externally raw

**Phase 2 readiness:** schema is JSON-Schema-compatible → trivial DuckDB / SQLite
mapping when 5K+ records (current: ≤10K via grep + python is fine).
