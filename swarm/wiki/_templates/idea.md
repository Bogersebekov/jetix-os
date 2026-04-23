---
id: idea-<kebab-slug>
title: <idea name>
type: idea
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
pipeline: raw
state: drafted
confidence: low
tier: core
produced_by: <agent>-<mode>
sources: []
related: []
topics: []
tags: []
proposed_by: <agent or human>
routing_target:
idea_status: raw
---

# <Title>

## Одна строка
<the idea, ≤120 chars>

## Обоснование
<why this is worth considering>

## Предполагаемый эффект
<concrete expected impact>

## Что уже известно/проверено
<existing evidence, with [src:path] citations if any>

## Следующий шаг
<routing_target action; e.g. "schedule experiment", "write claim", "skill candidate", "drop">

## Связи
- Inspired by: <`[[ideas/<slug>]]`> (inspired_by)
- Related concept: <`[[concepts/<slug>]]`>

## Provenance
<§5.5.5 — for `state: drafted, pipeline: raw` ideas, sources[] may be empty;
gate enforces non-empty only at `state: accepted` per D6 §2>

## Edges
- `[[ideas/<slug>]]` (inspired_by) → `edges.jsonl`
