---
id: topic-<kebab-slug>
title: <topic name>
type: topic
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
pipeline: ingested
state: drafted
confidence: medium
tier: core
produced_by: <agent>-<mode>
sources: []
related: []
topics: []
tags: [#type/topic]
MOC_for: []
---

# <Title>

## Зачем эта тема
<motivation; ≤200 chars>

## Основные концепции
- `[[concepts/<slug>]]`
- `[[concepts/<slug>]]`

## Ключевые сущности
- `[[entities/<slug>]]`

## Открытые вопросы
- <Q1>
- <Q2>

## Смежные темы
- `[[topics/<slug>]]` (related_to / part_of)

## Provenance
<§5.5.5; topics often aggregate without primary sources — `sources[]` may
list canonical references>

## Edges
- `[[concepts/<slug>]]` (part_of) — children via reciprocal edge
- `[[topics/<slug>]]` (layer-ref or related_to)
