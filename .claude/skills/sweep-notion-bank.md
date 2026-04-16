---
name: sweep-notion-bank
description: |
  Sweep полный Notion Bank of Ideas (650+ идей), классифицировать по релевантности
  к теме system-design, импортировать релевантные в wiki/ параллельно через
  sub-agent sweep-worker. Скипает уже импортированные (dedup по notion_id/slug).
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task
---

# Skill: /sweep-notion-bank

## Назначение

Массовый импорт Notion Bank of Ideas (database `bf0e9a11-0e6f-4717-9ae5-e19f9a096ce7`)
с классификацией на RELEVANT/IRRELEVANT/UNCLEAR под тему system-design. Релевантные
уходят в `wiki/` с тегом `topics: [system-design]`. Все остальные остаются в Notion.

## Триггер

- `/sweep-notion-bank` — запуск всей pipeline (sweep + classify + import)
- `/sweep-notion-bank --dry-run` — только sweep + классификация, без import
- `/sweep-notion-bank --batch-size=N` — размер батча (default 20)
- `/sweep-notion-bank --parallel=N` — количество параллельных worker'ов (default 4)

## Предусловия

- Текущая ветка main, `git status` clean (или только expected untracked).
- `raw/notion-ideas/` существует.
- `wiki/ideas/`, `wiki/sources/` существуют.
- Subagent `sweep-worker` определён в `.claude/agents/sweep-worker.md`.
- Notion MCP доступен (`mcp__notion-query-database-view`, `mcp__notion-fetch`).

## Pipeline

### Этап 1. Full sweep (query всего Bank of Ideas)

1. `mcp__notion-query-database-view` на data-source `collection://bf0e9a11-0e6f-4717-9ae5-e19f9a096ce7`
   — первая страница, limit=100, sort=createdTime DESC.
2. Pagination — запрашивай следующие страницы пока `next_cursor` не null.
3. Для каждой идеи сохраняй в `raw/notion-ideas-sweep-2026-04-16.jsonl` одну JSON-строку:
   ```json
   {"notion_id": "...", "title": "...", "createdTime": "...", "niche": "...",
    "category": "...", "value": "...", "themes": [...], "content_preview": "...",
    "source_url": "https://notion.so/..."}
   ```
4. Если Notion MCP падает между страницами — повтор до 3 раз с backoff 10сек;
   если всё-таки упал — commit raw/ что собрал, push, остановка с ошибкой.

### Этап 2. Dedup против существующих

1. `grep -l "notion_id:" wiki/sources/` → extract всех notion_id уже импортированных.
2. Подели sweep-список на:
   - `already-imported` (N штук) — пометить, не трогать
   - `new` (остальные) — пойдут на classify+import

### Этап 3. Classify + import параллельно (sub-agents)

1. Подели `new` на батчи по `--batch-size` (default 20 идей).
2. Spawn `--parallel` параллельных `sweep-worker` sub-agents через Task tool.
   Каждому воркеру передай:
   - batch number
   - список notion_id батча
   - pointer на `raw/notion-ideas-sweep-2026-04-16.jsonl` (строки с этими ID)
   - pointer на критерии релевантности в `prompts/system-design-sweep-2026-04-16.md`
3. Ждёшь все воркеры (или группу из N если параллельные пулы).
4. При любом 529 от Anthropic API — foreground fallback (как в batch2, см.
   `reports/ideas-import-batch2-2026-04-16.md`).

### Этап 4. Aggregate + commit

1. Собери отчёты от всех воркеров (батчей).
2. Update `wiki/index.md` — добавь новые страницы под соответствующие категории.
3. Append в `wiki/log.md` новую строку (сверху):
   ```
   ## [2026-04-16] sweep-notion-bank | ingested: N | relevant: N | unclear: N | edges: +N
   ```
4. `git add wiki/ raw/notion-ideas/ raw/notion-ideas-sweep-2026-04-16.jsonl`
5. `git commit -m "[inputs] /sweep-notion-bank: N relevant ingested of M scanned"`

### Этап 5. Post-sweep maintenance

1. `/build-graph` — rebuild communities с учётом новых страниц.
2. `/lint` — проверить broken links, orphans, drift.
3. Commit + push результаты lint/build-graph.

## Output

В чат вывести отчёт:
```
# /sweep-notion-bank — done

- Sweep: {total} ideas scanned (pagination через N запросов)
- Already imported: {N}
- New: {N}
  - RELEVANT ingested: {N}
  - IRRELEVANT: {N}
  - UNCLEAR: {N}
- Edges: +{N} (new total {M})
- Communities после /build-graph: {N}
- Lint: {broken-links}, {orphans}
- Commits: {N} (SHAs: ...)
- Time: {HH:MM}
- UNCLEAR list (для ручного ревью): [ids...]
```

## Ограничения

- Не запускать без явного `/sweep-notion-bank`.
- Не запускать повторно в рамках одной сессии без `--force`.
- UNCLEAR pool может содержать до 30% — это нормально, Ruslan ревьюит вручную.
