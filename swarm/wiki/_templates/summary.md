---
id: summary-<kebab-slug>
title: <summary title>
type: summary
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
pipeline: compiled
state: drafted
confidence: medium
tier: core
produced_by: /build-graph
cycle_id: cyc-<kebab-slug>
sources: []
related: []
topics: []
tags: []
summary_window: <daily|weekly|topic|cluster>
community_id:
covers: []
---

# <Title>

## TL;DR
<3–5 bullet summary>

## Ключевые выводы
- <key takeaway 1> [src:`[[<page>]]`]
- <key takeaway 2>

## Что изменилось/появилось
<delta vs prior summary in same window>

## Что ещё открыто
<open questions surfaced during aggregation>

## Входные страницы
<verbatim from `covers:` frontmatter>

## Provenance
<§5.5.5 — sources[] = the union of `covers[]` pages' sources>

## Edges
- `[[<covered-page>]]` (part_of-inverse — summary aggregates these)
