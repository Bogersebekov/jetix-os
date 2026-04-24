---
title: Swarm Wiki v3 — Index
type: index
updated: 2026-04-25T01:30:00Z
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

## Tasks

- `tasks/T-swarm-self-improve-v1-2026-04-23/` — first real swarm cycle (meta niche, Stage-Gated)
- `tasks/T-km-materialization-mvp-2026-04-24/` — KM materialization MVP (cycle-3; A1+B2+B3-merged+company-as-code; HD-02 N=3 one-cycle)
- `tasks/T-jetix-system-overview-2026-04-24/` — 14-layer system overview (cycle-4; description-shape M-task; state=closed-compounded; Ruslan acked a1+b1+c1+d1)
- `tasks/T-layer-6-community-deep-dive-2026-04-24/` — L6 Community Deep-Dive (cycle-5; first Phase-2 layer-deep-dive; 13 sections; state=closed-compounded; Ruslan acked all-per-recommendations — Option C Hybrid + expanded ICP spectrum + 18 outreach templates)

## Designs

- `designs/T-km-materialization-mvp-2026-04-24/` — Wave-1 promoted design records (Part A substrate / Part B mini-swarm / Part C stage-gates + philosophy critic audit)

## Drafts (active reference — authoritative per-layer detail)

- `drafts/T-jetix-system-overview-2026-04-24-*` (14 files) — cell-authored primary-research material (41.6K words) for each layer L0..L9 + L-R/L-C/L-B/L-P. Integration into `decisions/JETIX-SYSTEM-OVERVIEW.md` (accepted 2026-04-24) cites these as authoritative detail sources.
- `drafts/T-layer-6-community-deep-dive-2026-04-24-*` (15 files) — cell-authored primary-research material (62.7K words) across 13 L6 sections + 2 investor peer-input drafts. Integration into `decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md` (accepted 2026-04-25) cites these as authoritative detail sources.

## Proposals

- `proposals/T-swarm-self-improve-v1-2026-04-23-decomposition.md` — WBS, 13 matrix cells
- `proposals/T-jetix-system-overview-2026-04-24-decomposition.md` — WBS, 15 cells M-class, 3-wave parallel
- `tasks/T-layer-6-community-deep-dive-2026-04-24/decomposition.md` — WBS, 13 content cells + 2 investor peer cells + integration cell, 3-wave parallel (Wave-A 5 / Wave-B 7 / Wave-C 3)

## Niches

`niches/<personal|business|sales|life|tech|meta>/` — Phase-B symlink
population per CLAUDE.md L70 6-niche lock.

## Cross-tree

- `graph/edges.jsonl` (intra-v3, append-only)
- `graph/cross-tree.jsonl` (v3→v2 only, append-only)
