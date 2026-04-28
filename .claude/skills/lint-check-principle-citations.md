---
name: lint-check-principle-citations
description: "Lint: Pillar A + Pillar B `principles_compliance:` refs resolve to active principles"
status: stub-phase-b-materialization
created_date: 2026-04-28
brigadier_phase: wave-1-scaffolding-stub
allowed-tools: Read, Glob, Grep
---

# Skill stub: /lint-check-principle-citations

> **STUB.** Wave 1 scaffolding placeholder. Логика lint check'а НЕ реализована.
> Phase B materialization (post-Wave-1.4 ack) implements grep-based + hash-match
> verification per Pillar C / Part 11 architecture.

## Описание

Per Pillar C §K.3: every Pillar A artefact (Part 11) + Pillar B project strategy (Part 7 supplement) carries `principles_compliance:` array. Verifies each ref resolves to existing principle file AND principle status != superseded. Alert if ref points to superseded principle (cascade re-citation needed).

## Wave 1 status

`stub-phase-b-materialization` — skill file exists для archival reference; не
выполняется до Phase B materialization. До активации этого lint check'а
sync invariants enforce'ятся manually на ack-time review.

## Provenance

- Pillar C architecture: `swarm/wiki/foundations/principles/architecture.md` §H.1 + §J.5 (для Pillar C-related lints)
- Part 11 architecture: `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` §H.1 (для Pillar A-related lints)
- Part 7 Bundle 5 supplement: `swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md` §K.X (для Pillar B-related lints)
- Wave 1 scaffolding brief: `prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md` §3.12
