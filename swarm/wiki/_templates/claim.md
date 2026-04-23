---
id: claim-<kebab-slug>
title: <claim assertion>
type: claim
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
last_reviewed:
pipeline: ingested
state: drafted
confidence: medium
confidence_method:
tier: core
produced_by: <agent>-<mode>
sources: []
related: []
topics: []
tags: []
stance: asserted
support_count: 0
contradiction_count: 0
support_edges: []
contradiction_edges: []
falsifier: <one-sentence falsifier — what evidence would refute this claim>
---

# <Title>

## Точная формулировка
<the claim, single sentence, falsifiable>

## Контекст
<scope, conditions, who is making it>

## Аргументы за
- <evidence 1> [src:path#section] — `[[sources/<slug>]]` supports
- <evidence 2>

## Аргументы против
- <counter-evidence 1> — `[[claims/<slug>]]` contradicts

## Что опровергнуло бы это утверждение
<verbatim from `falsifier:` frontmatter; mirrors v2 explicit-falsifier discipline>

## Связи
- Поддерживается: <`[[sources/<slug>]]`> (supports edge in `edges.jsonl`)
- Противоречит: <`[[claims/<slug>]]`> (bidirectional contradicts)
- Тестируется: <`[[experiments/<slug>]]`> (tested_by)

## Provenance
<§5.5.5 inline citation map; pipeline ≠ raw → sources[] required>

## Edges
- `[[sources/<slug>]]` (supports) → `edges.jsonl`
- `[[claims/<slug>]]` (contradicts) → `edges.jsonl` (BOTH directions written)
- `[[experiments/<slug>]]` (tested_by) → `edges.jsonl`
