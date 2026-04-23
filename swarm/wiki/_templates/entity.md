---
id: entity-<kebab-slug>
title: <entity name>
type: entity
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
tags: []
provenance_inline: true
entity_type: <person|company|product|team|event|place>
external_ids:
  notion:
  linkedin:
  github:
  hubspot:
---

# <Title>

## Кто/что это
<one-paragraph identification>

## Контекст
<who/what/where/when>

## Факты
- <fact 1> [src:path#section]
- <fact 2>

## Связи
- Tracked by alpha: <`[[tasks/<task-id>]]`> via `alpha-ref`
- Related concept: <`[[concepts/<slug>]]`>

## История взаимодействий
<chronological log of interactions; rotates at 30 entries to _archive/>

## Provenance
<§5.5.5 inline citation map>

## Edges
- `[[<task-or-operation-id>]]` (alpha-ref) → `edges.jsonl`

## Источники
