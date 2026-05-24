---
title: "MAST — Multi-Agent System Failure Taxonomy (Cemri 2024)"
type: concept
niche: tech
agents: [ml-ai-foundations-expert, systems-expert]
sources:
  - raw/articles/arxiv-2503.13657-cemri-mast-failure-modes.md
  - raw/articles/arxiv-2406.07155-qian-scaling-laws.md
  - raw/articles/arxiv-2512.08296-kim-multi-agent-scaling.md
related:
  - concepts/mlops-lifecycle.md
  - concepts/dl-curriculum-3-parts.md
tags: [#type/concept, #topic/mas, #topic/failure-modes]
topics: [mas-failure-modes, jetix-swarm-health]
created: 2026-05-24
updated: 2026-05-24
confidence: medium
pipeline: ingested
F: F2
G: jetix-shared
---

# MAST — MAS Failure Taxonomy (Cemri 2024)

## Суть в одной строке

arxiv-2503.13657 Cemri et al. (2024) — Multi-Agent System Failure Taxonomy, applicable к Jetix swarm health monitoring (Part 8).

## Определение

MAST (Multi-Agent System Tasks) failure-mode таксономия (Cemri 2024, arxiv-2503.13657) категоризирует failure modes по dimensions:

- **Coordination failures** — agents miscommunicate / contradict / duplicate work
- **Specification failures** — incomplete / ambiguous task definitions
- **Reasoning failures** — incorrect inference / hallucination
- **Tool-use failures** — incorrect tool invocation / state corruption
- **Resource failures** — token exhaustion / timeout

Cross-ref scaling laws (Qian 2024, arxiv-2406.07155) + multi-agent scaling (Kim 2025, arxiv-2512.08296).

## Применимость к Jetix

- **Part 8 Health Monitoring substrate** — failure mode catalog для swarm health audit
- **Brigadier orchestration audit lens** — MAS failure detection
- **ml-ai-foundations-expert + systems-expert cross-consult** на MAS issues

## Связи

- Pair с: [[concepts/mlops-lifecycle]] (deployment + monitoring layer)
- Cross-ref scaling laws: Qian 2024 + Kim 2025

## Источники

- [src: raw/articles/arxiv-2503.13657-cemri-mast-failure-modes.md]
- [src: raw/articles/arxiv-2406.07155-qian-scaling-laws.md]
- [src: raw/articles/arxiv-2512.08296-kim-multi-agent-scaling.md]
- [src: reports/book-driven-agents-2026-05-24/05-wiki-auto-creation-proposals.md §5.3.A22]
