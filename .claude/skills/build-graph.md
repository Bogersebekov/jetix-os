---
name: build-graph
description: "Пройти по `${WIKI_ROOT}/` (default v3), добить недостающие edges в edges.jsonl per D3 12-enum, пересчитать communities + summaries. Поддерживает `--tree {v2|v3|both}` per T1."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

> **`$WIKI_ROOT` resolution (D7).** Reads `.claude/config/wiki-roots.yaml`
> at startup; resolves wiki root via D7 §7.4. All `wiki/`-prefixed
> paths below MUST be read as `${WIKI_ROOT}/...`. Default `swarm/wiki/`
> (v3); set `WIKI_ROOT=wiki` for v2. Cross-tree edges (v3→v2 only)
> in `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.

# Skill: /build-graph

## Описание

Обновить граф знаний поверх `${WIKI_ROOT}/`. Идемпотентно.

## Триггер

- `/build-graph` — полный пересчёт.
- `/build-graph --edges-only` — только добрать edges, не трогать communities.

## Алгоритм

### 1. Собрать все страницы

Glob `${WIKI_ROOT}/**/*.md`, исключить `index.md`, `log.md`, `overview.md`, `_templates/*`,
`niches/*/README.md`, `graph/*`, `_archive/*`, `_lint-report-*`. **При `--tree=both`: повторить glob для v2 `wiki/**/*.md` и v3 `swarm/wiki/**/*.md`; cross-tree-ref edges (D3 §3.2.12) пишутся в `${WIKI_ROOT_V3}/graph/cross-tree.jsonl`.**

### 2. Построить карту упоминаний

Для каждой страницы P:
- Grep по `[[slug]]` и `[text](relative-path)` в её теле.
- Собрать `mentioned_by[P] = [...]`.

### 3. Добить edges

Прочитать `${WIKI_ROOT}/graph/edges.jsonl` в память (set по `(from, to, type)`). При `--tree=both` — также `${WIKI_ROOT_V3}/graph/cross-tree.jsonl`.

Для каждой пары (A → B) с перекрёстным упоминанием:

1. Определить тип edge per D3 12-enum:
   - "Расширяет" / "Extends" → `extends`.
   - "Противоречит" / "Contradicts" → `contradicts` (запись BIDIRECTIONAL — обе стороны).
   - "Поддерживает" / "Supports" → `supports`.
   - "Вдохновлён" / "Inspired by" → `inspired_by`.
   - "Проверяется" / "Tested by" / experiment → `tested_by`.
   - "Опровергает" / "Invalidates" → `invalidates`.
   - "Заменяет" / "Supersedes" → `supersedes`.
   - "Часть" / "Part of" → `part_of` (FORMALIZED per Q3).
   - Иначе (упоминание сущности) → `derived_from`.
   - Cross-layer (5×4 matrix → alpha tracker) → `alpha-ref`.
   - Cross-layer (theme → global pattern) → `layer-ref`.
   - v3→v2 link → `cross-tree-ref` (запись в cross-tree.jsonl, НЕ edges.jsonl).
   - **Снят: `addresses_gap` per critic-gate1 H4 of the wiki-v3 spec.**

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

### 5. Обновить `${WIKI_ROOT}/graph/communities.md`

Перезаписать секцию `## Кластеры`:

```
## C1: <Имя центральной ноды> [<niche>]
- Страницы: [[...]], [[...]], ...
- Центральные ноды: [[...]], [[...]]
- Summary: → см. summaries.md
```

### 6. Обновить `${WIKI_ROOT}/graph/summaries.md`

Для каждого кластера — 3-5 предложений:

- О чём этот кластер.
- Ключевые идеи (из concepts).
- Противоречия (из edges type=contradicts).
- Главные источники.

Это и есть HippoRAG/GraphRAG layer для быстрого context в `/ask`.

### 7. Залогировать

В `${WIKI_ROOT}/log.md` (сверху):

```
## [YYYY-MM-DD] build-graph | edges: +N / total M | communities: K
```

## Правила

- Append-only для edges.jsonl. Никогда не удаляй вручную.
- Для удаления edge — перегенерируй с нуля (это делает полный `/build-graph`).
- Confidence edge-а по умолчанию `medium`. `high` — если в обеих страницах явная секция.
- Не создавать edges к `_templates/*` и системным файлам.
