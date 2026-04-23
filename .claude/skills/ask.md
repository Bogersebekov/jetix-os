---
name: ask
description: "Ответить на вопрос по `${WIKI_ROOT}/` (default v3): подобрать 5-15 страниц, синтезировать с цитатами, сохранить ценный ответ в `${WIKI_ROOT}/comparisons/`."
allowed-tools: Read, Write, Edit, Glob, Grep
---

> **`$WIKI_ROOT` resolution (D7).** This skill reads
> `.claude/config/wiki-roots.yaml` at startup and resolves the wiki
> root via the algorithm in D7 §7.4. All `wiki/`-prefixed paths in
> the algorithm below MUST be read as `${WIKI_ROOT}/...`. Default
> `swarm/wiki/` (v3); set `WIKI_ROOT=wiki` for v2. Cross-tree edges
> (v3→v2 only) → `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.

# Skill: /ask

## Описание

Ответить на содержательный вопрос пользователя по накопленной `${WIKI_ROOT}/`. Не просто поиск —
синтез: связывание идей, выявление противоречий, неочевидные связи.

## Триггер

`/ask <вопрос>` — вопрос на русском или английском.

## Алгоритм

### 1. Прочитать `${WIKI_ROOT}/index.md`

Это главный навигатор. Не гадай — читай целиком.

### 2. Отобрать 5-15 релевантных страниц

- Сначала по заголовку и one-line summary из index.md.
- При необходимости — grep по ключевым словам вопроса в `${WIKI_ROOT}/**/*.md`.
- Смотри niche: если вопрос явно про sales — приоритет `${WIKI_ROOT}/niches/sales/` и страниц с `niche: sales`.
- Если есть community summaries (`${WIKI_ROOT}/graph/summaries.md`) — используй их для быстрого контекста. (Tier 4 long-context fallback per Q1: scope to current niche dir, not full wiki.)

### 3. Прочитать отобранные страницы

Полностью. Следи за wikilinks — при необходимости иди глубже (но не более 2 уровней).

### 4. Синтезировать ответ

Структура ответа:

```
## Короткий ответ
<1-3 предложения>

## Детали
<3-10 предложений с цитатами в формате [[file.md]]>

## Что противоречиво / открыто
<если есть>

## Откуда это
- [[sources/...]] — что оттуда
- [[concepts/...]]
```

- Цитируй точными wikilink'ами.
- Разделяй: что из wiki vs. что ты добавляешь от себя.
- Если данных мало — честно сказать.

### 5. Оценить ценность ответа

**Сохранить в `${WIKI_ROOT}/comparisons/`** если ответ:

- даёт новую связь между 2+ страницами, которой раньше не было;
- выявляет противоречие между источниками;
- обобщает по 5+ страницам (неочевидный synthesis);
- даёт практический вывод, который стоит запомнить.

**Не сохранять** если ответ — простой lookup ("кто такой X", "что такое Y").

### 6. Сохранение (если нужно)

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

# <Вопрос>

## Ответ
<синтез>

## Какие страницы использованы
- [[...]]

## Новые связи
- [[A]] → [[B]] (tип edge, например supports)
```

Добавить edges в `${WIKI_ROOT}/graph/edges.jsonl` per D3 12-enum. Cross-tree refs (v3→v2) → `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per T1.

### 7. Обновить index.md и log.md

Если сохранили:
- В `index.md` — секция `## Comparisons`: `- [title](comparisons/...) — 1 line [niche]`.
- В `log.md` (сверху): `## [YYYY-MM-DD] ask | <slug>` + какие страницы затронуты.

### 8. Вывести ответ пользователю

Сначала ответ. В конце — "(сохранено в `comparisons/...`)" если сохранили, иначе ничего.

## Правила

- Не выдумывать факты. Если в wiki нет — сказать "в wiki пока нет, могу загуглить / спросить".
- Не пересказывать содержимое страниц — отвечай на вопрос.
- Один `/ask` = один синтез. Длинные дискуссии — пусть спрашивают несколько раз.
