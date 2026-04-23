---
id: source-<kebab-slug>
title: <source title>
type: source
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
pipeline: raw
state: drafted
confidence: high
tier: core
produced_by: /ingest
captured_by: /ingest
captured_date: <YYYY-MM-DD>
sources: []
related: []
topics: []
tags: []
source_type: <article|book|podcast|video|meeting|voice-memo|transcript|web|paper>
url:
local_path:
author:
ingested_date: <YYYY-MM-DD>
coverage: []
---

# <Title>

## TL;DR
<3–5 bullet summary>

## Summary
<longer prose summary, with [src:path#section] back to local_path or url>

## Ключевые цитаты
> "<verbatim quote>" — [src:local_path#L42-L48]

## Что извлекли
- <distilled insight 1, paired with `[[concepts/<slug>]]`>
- <distilled insight 2, paired with `[[claims/<slug>]]`>

## Provenance
<§5.5.5 — sources[] non-empty (this page IS a source); pipeline begins at `raw`>

## Edges
- `[[concepts/<slug>]]` (derived_from inverse — sources are pointed to BY concepts via derived_from)

## Сырое
<location of raw file under raw/; pointer only, not body content>
