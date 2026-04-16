---
type: raw-index
updated: 2026-04-16
---
# Raw — Jetix OS

Сырые источники до обработки. Ничего отсюда не удаляется — только добавляется.
Все `/ingest` читают именно отсюда.

## Структура

| Папка | Что кладём | Pipeline |
|-------|------------|----------|
| `articles/` | Статьи, блог-посты, PDF-выжимки, заметки из веба | raw → ingested |
| `transcripts/` | Транскрипты голосовых/видео (уже есть, не трогать) | raw → ingested |
| `voice-memos/` | OGG/MP3 голосовые (уже есть, сначала transcribe) | raw → transcript → ingested |
| `meetings/` | Заметки и расшифровки встреч | raw → ingested |
| `books/` | Заметки по книгам, выдержки, highlights | raw → ingested |
| `web/` | Автосохранённые страницы (через /ingest URL) | raw → ingested |
| `imports/` | Импорты из внешних систем (Notion и т.п.) | raw → ingested |
| `research/` | Рабочие ресёрч-заметки | raw → ingested |

## Pipeline

```
raw/{type}/YYYY-MM-DD-slug.{md,txt,ogg}
  ↓ /ingest
wiki/{entity-type}/slug.md + wiki/sources/YYYY-MM-DD-slug.md
  ↓ /lint, /consolidate, /build-graph
wiki/graph/ (edges + communities + summaries)
```

## Конвенции
- Имя файла: `YYYY-MM-DD-slug.ext` (дата — когда получен источник).
- Slug — kebab-case, английский, короткий.
- Если файл — Markdown, YAML frontmatter обязателен:

```yaml
---
title: "..."
source: "URL или название"
author: "..."
captured: 2026-04-16
pipeline: raw
niche: personal | business | sales | life | tech | meta
---
```

## Migration plan

Старые источники постепенно поднимаются в wiki/:

- [ ] `knowledge-base/` → разбор через `/ingest` (добавить в план MIGRATION.md)
- [ ] `raw/transcripts/` существующие → `/ingest`
- [ ] `raw/voice-memos/` → сначала transcribe через `tools/transcribe.py`, потом `/ingest`
- [ ] `raw/imports/`, `raw/research/` — по мере касания

Не удалять старое, пока не перенесено и не подтверждено.
