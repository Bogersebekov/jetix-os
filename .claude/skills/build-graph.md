---
name: build-graph
description: "Пройти по wiki/, добить недостающие edges в edges.jsonl, пересчитать communities + summaries."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Skill: /build-graph

## Описание

Обновить граф знаний поверх wiki/. Идемпотентно.

## Триггер

- `/build-graph` — полный пересчёт.
- `/build-graph --edges-only` — только добрать edges, не трогать communities.

## Алгоритм

### 1. Собрать все страницы

Glob `wiki/**/*.md`, исключить `index.md`, `log.md`, `overview.md`, `_templates/*`,
`niches/*/README.md`, `graph/*`, `_archive/*`, `_lint-report-*`.

### 2. Построить карту упоминаний

Для каждой страницы P:
- Grep по `[[slug]]` и `[text](relative-path)` в её теле.
- Собрать `mentioned_by[P] = [...]`.

### 3. Добить edges

Прочитать `wiki/graph/edges.jsonl` в память (set по `(from, to, type)`).

Для каждой пары (A → B) с перекрёстным упоминанием:

1. Определить тип edge:
   - Если в тексте A секция "## Расширяет" / "## Extends" и ссылка на B → `extends`.
   - Секция "Противоречит" / "Contradicts" → `contradicts`.
   - "Поддерживает" / "Supports" → `supports`.
   - "Вдохновлён" / "Inspired by" → `inspired_by`.
   - "Проверяется" / "Tested by" / experiment → `tested_by`.
   - "Опровергает" / "Invalidates" → `invalidates`.
   - "Заменяет" / "Supersedes" → `supersedes`.
   - "Закрывает пробел" / "Addresses gap" → `addresses_gap`.
   - Иначе (просто упоминание) → `derived_from`.

2. Если `(A, B, type)` ещё нет — append в `edges.jsonl`:

   ```json
   {"from": "concepts/a.md", "to": "entities/b.md", "type": "derived_from", "created": "YYYY-MM-DD", "confidence": "medium"}
   ```

### 4. Community detection (простая)

- Построить неориентированный граф: ноды = страницы, рёбра = все edges.
- Найти связные компоненты.
- Если компонента > 15 нод — разбить по niche (как fallback); если всё равно > 15 —
  по topic/tag.
- Имя кластера: центральная нода с макс. degree, + niche.

### 5. Обновить `wiki/graph/communities.md`

Перезаписать секцию `## Кластеры`:

```
## C1: <Имя центральной ноды> [<niche>]
- Страницы: [[...]], [[...]], ...
- Центральные ноды: [[...]], [[...]]
- Summary: → см. summaries.md
```

### 6. Обновить `wiki/graph/summaries.md`

Для каждого кластера — 3-5 предложений:

- О чём этот кластер.
- Ключевые идеи (из concepts).
- Противоречия (из edges type=contradicts).
- Главные источники.

Это и есть HippoRAG/GraphRAG layer для быстрого context в `/ask`.

### 7. Залогировать

В `wiki/log.md` (сверху):

```
## [YYYY-MM-DD] build-graph | edges: +N / total M | communities: K
```

## Правила

- Append-only для edges.jsonl. Никогда не удаляй вручную.
- Для удаления edge — перегенерируй с нуля (это делает полный `/build-graph`).
- Confidence edge-а по умолчанию `medium`. `high` — если в обеих страницах явная секция.
- Не создавать edges к `_templates/*` и системным файлам.
