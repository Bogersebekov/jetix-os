---
id: foundation-<kebab-slug>
title: <foundation principle>
type: foundation
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
last_reviewed: <YYYY-MM-DD>     # required per Q5 365-day re-review
pipeline: linted
state: accepted                 # foundations enter at `accepted`
confidence: high
confidence_method: ruslan-attested
tier: core
produced_by: brigadier
sources: []
related: []
topics: []
tags: [#type/foundation]
binding_scope: swarm-wide      # or theme:<theme> | expert:<expert>
supersedes_versions: []
---

# <Title>

## Принцип
<the foundation, single decisive statement>

## Почему принимается
<rationale; 1–3 paragraphs with [src:path#section] citations>

## Что из этого следует
- <consequence 1>
- <consequence 2>

## Когда сомневаться
<conditions under which this foundation should be revisited>

## Связи
- Supersedes: <`[[foundations/<v2-slug>@v1]]`> (supersedes edge)
- Tested by: <`[[experiments/<slug>]]`>
- Тестируется: list of experiments referencing this

## Provenance
<§5.5.5 — foundations require ≥1 source AND ruslan-attested confidence_method,
OR brigadier-attested with ≥3 supports>

## Edges
- `[[foundations/<slug>@v<N-1>]]` (supersedes) → `edges.jsonl`
