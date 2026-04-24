---
name: build-graph
description: "Читать edges.jsonl → in-memory adjacency → Louvain-equivalent greedy modularity community detection → communities.jsonl → health.md rollup. Modes: default (full rebuild), --since=<ISO-date> (incremental), --dry-run."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
created: 2026-04-24
last_modified: 2026-04-24
pipeline: active
state: active
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.A A.8"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md", range: "§4.2 Tier-C"}
---

> **`$WIKI_ROOT` resolution (D7).** Reads `.claude/config/wiki-roots.yaml`
> at startup; resolves wiki root via D7 §7.4. All `wiki/`-prefixed
> paths below MUST be read as `${WIKI_ROOT}/...`. Default `swarm/wiki/`
> (v3); set `WIKI_ROOT=wiki` for v2. Cross-tree edges (v3->v2 only)
> in `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.

# Skill: /build-graph

## Описание

Обновить граф знаний поверх `${WIKI_ROOT}/`. Идемпотентно.
Community detection via Louvain-equivalent greedy modularity (pure Python dict-of-lists; no networkx).
Target performance: <5s on Phase-A wiki (~50 edges, ~20 pages).

## Триггер

- `/build-graph` — полный пересчёт.
- `/build-graph --since=<ISO-date>` — инкрементальный (только edges с `ts >= <ISO-date>`).
- `/build-graph --dry-run` — вывести community count без записи файлов.
- `/build-graph --edges-only` — только добрать edges, не трогать communities.
- `/build-graph --tree {v2|v3|both}` — выбор tree per T1.

## Алгоритм

### 1. Resolve ${WIKI_ROOT} + parse arguments

Прочитать wiki-roots.yaml. Определить режим: full / incremental / dry-run / edges-only.
Для `--since=<ISO-date>`: фильтровать edges с `ts >= <ISO-date>`.

### 2. Загрузить edges.jsonl

Прочитать `${WIKI_ROOT}/graph/edges.jsonl` (и `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` при `--tree=both`).
Пропустить строки-комментарии (начинающиеся с `#`). Парсить JSONL.
Для incremental — отфильтровать по `ts`.

### 3. Собрать все страницы

Glob `${WIKI_ROOT}/**/*.md`, исключить: `index.md`, `log.md`, `overview.md`,
`_templates/*`, `niches/*/README.md`, `graph/*`, `_archive/*`.

### 4. Построить карту упоминаний (для --edges-only или full)

Для каждой страницы P:
- Grep по `[[slug]]` и `[text](relative-path)` в её теле.
- Собрать `mentioned_by[P] = [...]`.

### 5. Добить edges (если не --dry-run)

Для каждой пары (A → B) с перекрёстным упоминанием, не представленной в edges.jsonl:
- Определить тип per D3 12-enum.
- Append в `${WIKI_ROOT}/graph/edges.jsonl`.

### 6. Community detection

Запустить `python3 tools/community-detect.py <edges_jsonl_path> <output_communities_jsonl_path>`.

Алгоритм в `tools/community-detect.py` (≤80 LoC):
- Читать edges → in-memory undirected adjacency dict-of-lists.
- **Greedy modularity (Louvain-equivalent):** начать с каждого нода в своей community.
  Итерировать: для каждого нода попробовать переместить в community соседа, если
  модулярность Q растёт. Повторять до сходимости (delta_Q < 1e-6 OR max_iter=100).
  Формула Q: `(e_c / m) - (k_c / (2m))^2` где e_c = internal edges, k_c = sum of degrees, m = total edges.
- Для каждой community определить `dominant_niche` (mode of niche frontmatter values nodes).
- `top_k_concepts`: top-3 nodes by degree в community.
- Записать `${WIKI_ROOT}/graph/communities.jsonl`:
  ```jsonl
  {"community_id": "C1", "node_count": 5, "nodes": ["concepts/foo.md", ...], "dominant_niche": "tech", "top_k_concepts": ["concepts/foo.md", "concepts/bar.md", "concepts/baz.md"]}
  ```

При `--dry-run`: вывести community count в stdout; не записывать communities.jsonl.

### 7. Обновить `${WIKI_ROOT}/meta/health.md`

Прочитать health.md. Обновить секцию community stats:
```
community_count: N
largest_community_size: M
last_build_graph: YYYY-MM-DD HH:MM
```

### 8. Залогировать

В `${WIKI_ROOT}/log.md` (сверху):
```
## [YYYY-MM-DD] build-graph | edges: +N / total M | communities: K | mode: full|incremental|dry-run
```

## Правила

- Append-only для edges.jsonl. Никогда не удалять вручную.
- Confidence edge-а по умолчанию `medium`. `high` — если в обеих страницах явная секция.
- Не создавать edges к `_templates/*` и системным файлам.
- При `--dry-run` — нулевых записей в любой файл.

## Acceptance

На Phase-A wiki (~50 edges, ~20 pages): `/build-graph` завершается в <5s
и производит непустой communities.jsonl (≥1 community record).
Проверка: `grep -c '^\{' ${WIKI_ROOT}/graph/communities.jsonl`.
