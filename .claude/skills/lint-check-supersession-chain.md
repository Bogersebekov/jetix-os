---
name: lint-check-supersession-chain
description: "Lint: Pillar A supersession chains are consistent (no orphan supersedes refs)"
status: stub-phase-b-materialization
created_date: 2026-04-28
brigadier_phase: wave-1-scaffolding-stub
allowed-tools: Read, Glob, Grep
---

# Skill stub: /lint-check-supersession-chain

> **STUB.** Wave 1 scaffolding placeholder. Логика lint check'а НЕ реализована.
> Phase B materialization (post-Wave-1.4 ack) implements grep-based + hash-match
> verification per Pillar C / Part 11 architecture.

## Описание

Per Part 11 §H.1: verifies supersession chains в strategic-direction-doc artefacts — if A supersedes B, then B has superseded_by: A; chain reachable; no orphan refs; no cycles.

## Wave 1 status

`stub-phase-b-materialization` — skill file exists для archival reference; не
выполняется до Phase B materialization. До активации этого lint check'а
sync invariants enforce'ятся manually на ack-time review.

## Provenance

- Pillar C architecture: `swarm/wiki/foundations/principles/architecture.md` §H.1 + §J.5 (для Pillar C-related lints)
- Part 11 architecture: `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` §H.1 (для Pillar A-related lints)
- Part 7 Bundle 5 supplement: `swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md` §K.X (для Pillar B-related lints)
- Wave 1 scaffolding brief: `prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md` §3.12
