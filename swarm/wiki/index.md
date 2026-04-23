---
title: Swarm Wiki v3 — Index
type: index
updated: 2026-04-23
---

# Swarm Wiki v3 — Index

This file is updated atomically by `/ingest` after every wiki write.
The Phase-A bootstrap state lists only the foundation pages and
templates that exist on disk at Шаг 2.2.4 close.

## Foundation

- `foundations/swarm-alphas.md` — 5 alphas (α-1..α-5)

## Templates

- `_templates/concept.md`
- `_templates/entity.md`
- `_templates/source.md`
- `_templates/claim.md`
- `_templates/idea.md`
- `_templates/topic.md`
- `_templates/experiment.md`
- `_templates/summary.md`
- `_templates/foundation.md`
- `_templates/edge-types.md` — 12-edge enum (D3)

## Meta

- `meta/health.md` — observability dashboard (D10)
- `meta/agent-improvements/` — per-agent + system-level improvements (D12 + R6)

## Layer READMEs

- `themes/<engineering|mgmt|systems|philosophy|investing>/README.md`
- `brigadier/README.md`
- `agents/<expert-id>/README.md` (5)
- `insights/README.md` — Phase-A scaffold-only (Q8)

## Spine entity-types

Bootstrap empty — populated lazily by `/ingest`.

## Niches

`niches/<personal|business|sales|life|tech|meta>/` — Phase-B symlink
population per CLAUDE.md L70 6-niche lock.

## Cross-tree

- `graph/edges.jsonl` (intra-v3, append-only)
- `graph/cross-tree.jsonl` (v3→v2 only, append-only)
