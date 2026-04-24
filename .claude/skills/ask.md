---
name: ask
description: "Ответить на вопрос по `${WIKI_ROOT}/` (default v3): подобрать 5-15 страниц, синтезировать с цитатами, сохранить ценный ответ в `${WIKI_ROOT}/comparisons/`. Поддерживает OFFLINE_MODE=1 (structured-excerpt без LLM)."
allowed-tools: Read, Write, Edit, Glob, Grep
created: 2026-04-24
last_modified: 2026-04-24
pipeline: active
state: active
confidence: high
confidence_method: engineering-canonical-patterns-matched
tier: core
produced_by: engineering-expert
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.A A.5"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md", range: "§4.2 + UC-10"}
---

> **`$WIKI_ROOT` resolution (D7).** This skill reads
> `.claude/config/wiki-roots.yaml` at startup and resolves the wiki
> root via the algorithm in D7 §7.4. All `wiki/`-prefixed paths in
> the algorithm below MUST be read as `${WIKI_ROOT}/...`. Default
> `swarm/wiki/` (v3); set `WIKI_ROOT=wiki` for v2. Cross-tree edges
> (v3->v2 only) → `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.
>
> **OFFLINE_MODE=1 (UC-10 Phase-A).** When env-var `OFFLINE_MODE=1` is set,
> Step 2.5 activates: skip LLM synthesis; return structured-excerpt packet
> only. Zero Task() dispatches. Zero outbound network connections.

# Skill: /ask

## Описание

Ответить на содержательный вопрос пользователя по накопленной `${WIKI_ROOT}/`. Не просто поиск —
синтез: связывание идей, выявление противоречий, неочевидные связи.
Когда `OFFLINE_MODE=1` — retrieval-only structured-excerpt (UC-10 Phase-A architectural proof).

## Триггер

`/ask <вопрос>` — вопрос на русском или английском.

## Алгоритм

### 0. Resolve ${WIKI_ROOT} + check OFFLINE_MODE

Прочитать `.claude/config/wiki-roots.yaml`. Применить D7 §7.4 resolution algorithm.
Проверить: если `OFFLINE_MODE=1` (env-var) — активировать Step 2.5 режим.

### 1. Прочитать `${WIKI_ROOT}/index.md`

Это главный навигатор. Не гадай — читай целиком.

### 2. Отобрать 5-15 релевантных страниц (Tier-A/B/C retrieval)

- **Tier-A Direct path.** Если вопрос называет конкретную страницу — читать её напрямую.
- **Tier-B Index+grep.** По заголовку и summary из index.md; grep по ключевым словам в `${WIKI_ROOT}/**/*.md`; нiche-приоритет.
- **Tier-C Typed-BFS depth-2.** Читать `${WIKI_ROOT}/graph/edges.jsonl`; начать с seed-страниц из Tier-B; раскрыть по `extends`, `supports`, `derived_from` до глубины 2.
- Если есть community summaries (`${WIKI_ROOT}/graph/communities.jsonl`) — использовать `top_k_concepts` из релевантных community для быстрого контекста.

### 2.5 — Offline-first gate (UC-10)

**Активируется ТОЛЬКО при `OFFLINE_MODE=1`.**

1. Использовать candidate pages из Tier-A/B/C (шаги выше).
2. Посчитать edge-degree для каждой candidate страницы:
   - `degree = count(edges in edges.jsonl where from == page OR to == page)`.
3. Отсортировать по degree descending; взять top-10.
4. Для каждой из top-10 составить excerpt запись:
   ```
   | rank | slug | title | niche | excerpt (2 sentences from body) | confidence | sources |
   ```
5. Render markdown table + citation list:
   ```markdown
   ## OFFLINE_MODE=1 — Structured Excerpt

   Query: "<запрос>"

   | # | Page | Niche | Excerpt | Confidence |
   |---|------|-------|---------|------------|
   | 1 | [src:concepts/foo.md] | tech | "..." | high |
   ...

   ### Citations
   - [src:concepts/foo.md] — <title>
   - [src:sources/bar.md] — <title>
   ...
   ```
6. Добавить в `${WIKI_ROOT}/log.md` (сверху):
   ```
   ## [YYYY-MM-DD HH:MM] ask | OFFLINE_MODE=1 | <slug-of-query>
   OFFLINE_MODE=1 query: '<запрос>' → 10 excerpts returned; zero LLM calls.
   ```
7. **НЕ писать в `${WIKI_ROOT}/comparisons/`** — filing loop только при LLM synthesis.
8. **НЕ вызывать Task()** с любым intent на генерацию. Zero LLM dispatches.
9. Вернуть markdown response ≤2KB с ≥3 `[src:...]` citations. **STOP — не идти дальше.**

**Network verification (operational note):**
Для аудита можно запустить рядом с сессией:
```bash
tcpdump -n 'tcp port 443 and host not 127.0.0.1'
# OR (socket-level, no root required):
ss -tnp 'dport = :443'
```
Ожидаемый результат при `OFFLINE_MODE=1`: zero connections на :443 к внешним хостам.
Проверочный скрипт: `swarm/tests/uc-ask-offline.sh`.

### 3. Прочитать отобранные страницы (только если OFFLINE_MODE не активен)

Полностью. Следи за wikilinks — при необходимости иди глубже (но не более 2 уровней).

### 4. Синтезировать ответ (только если OFFLINE_MODE не активен)

```
## Короткий ответ
<1-3 предложения>

## Детали
<3-10 предложений с цитатами в формате [src:file.md]>

## Что противоречиво / открыто
<если есть>

## Откуда это
- [src:sources/...] — что оттуда
- [src:concepts/...]
```

- Цитируй точными wikilink'ами в формате `[src:path.md]`.
- Разделяй: что из wiki vs. что ты добавляешь от себя.
- Если данных мало — честно сказать.

### 5. Оценить ценность ответа

**Сохранить в `${WIKI_ROOT}/comparisons/`** если ответ:
- даёт новую связь между 2+ страницами, которой раньше не было;
- выявляет противоречие между источниками;
- обобщает по 5+ страницам;
- даёт практический вывод, который стоит запомнить.

**Не сохранять** если ответ — простой lookup. **Не сохранять при OFFLINE_MODE=1.**

### 6. Сохранение (если нужно и OFFLINE_MODE не активен)

`${WIKI_ROOT}/comparisons/YYYY-MM-DD-question-slug.md`:

```yaml
---
title: "<сокращённый вопрос>"
type: comparison
question: "<полный вопрос>"
niche: ...
sources: [...]
related: [...]
tags: [#type/comparison]
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: medium
pipeline: ready
---
```

Добавить edges в `${WIKI_ROOT}/graph/edges.jsonl` per D3 12-enum.

### 7. Обновить index.md и log.md

Если сохранили:
- В `index.md` — секция `## Comparisons`: `- [title](comparisons/...) — 1 line [niche]`.
- В `log.md` (сверху): `## [YYYY-MM-DD] ask | <slug>` + какие страницы затронуты.

### 8. Вывести ответ пользователю

Сначала ответ. В конце — "(сохранено в `comparisons/...`)" если сохранили, иначе ничего.

## Правила

- Не выдумывать факты. Если в wiki нет — сказать "в wiki пока нет".
- Не пересказывать содержимое страниц — отвечай на вопрос.
- Один `/ask` = один синтез.
- При `OFFLINE_MODE=1` — НИКАКИХ LLM calls, НИКАКИХ Task() dispatches, НИКАКИХ записей в comparisons/.
