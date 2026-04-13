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
