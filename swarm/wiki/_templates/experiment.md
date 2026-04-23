---
id: experiment-<kebab-slug>
title: <experiment title>
type: experiment
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
pipeline: ingested
state: drafted
confidence: medium
tier: core
produced_by: <agent>-<mode>
cycle_id: cyc-<kebab-slug>
sources: []
related: []
topics: []
tags: []
hypothesis: <falsifiable claim, ≤500 chars>
start_date: <YYYY-MM-DD>
end_date:
outcome: open
---

# <Title>

## Гипотеза
<verbatim from `hypothesis:` frontmatter>

## Дизайн
- IV (independent variable):
- DV (dependent variable):
- Control:
- Duration:

## Что делаем
<procedure>

## Результат
<observed; populated when outcome ≠ open>

## Выводы
<interpretation; cites supporting evidence>

## Связи
- Tests claim: `[[claims/<slug>]]` (tested_by inverse)
- Invalidates / supports: <as outcome warrants>

## Provenance
<§5.5.5; experiments are themselves source-class artefacts after closure>

## Edges
- `[[claims/<slug>]]` (tests; inverse of tested_by)
- `[[claims/<slug>]]` (invalidates) — when outcome=lost
