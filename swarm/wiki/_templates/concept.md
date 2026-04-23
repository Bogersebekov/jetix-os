---
id: concept-<kebab-slug>
title: <concept name>
type: concept
layer: spine
niche: <personal|business|sales|life|tech|meta>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
last_reviewed:
pipeline: ingested
state: drafted
confidence: medium
confidence_method:
tier: core
produced_by: <agent>-<mode>
derived_from:
sources: []
related: []
topics: []
tags: []
provenance_inline: true
definition: <one-line definition, ≤200 chars>
examples: []
extends:
---

# <Title>

## Суть в одной строке
<concise gist, ≤120 chars>

## Определение
<formal definition, with [src:path#section] inline citations>

## Ключевые свойства
- <property 1>
- <property 2>

## Применимость
<contexts where this concept holds>

## Связи
- Расширяет: <`[[concepts/parent-concept]]`>
- Поддерживает: <`[[claims/relevant-claim]]`>
- Противоречит: <`[[claims/opposing-claim]]`>

## Provenance
<inline-citation map per §5.5.5; one [src:path] per non-trivial paragraph>

## Edges
- `[[concepts/<other-concept>]]` (extends) → `edges.jsonl`
- `[[sources/<source-slug>]]` (derived_from) → `edges.jsonl`

## Источники
<explicit list mirroring sources[] frontmatter>
