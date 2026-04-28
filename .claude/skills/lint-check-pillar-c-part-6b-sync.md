---
name: lint-check-pillar-c-part-6b-sync
description: "Lint: Pillar C Tier 2 foundation_generic ↔ Part 6b constitutional_never_list sync invariant"
status: stub-phase-b-materialization
created_date: 2026-04-28
brigadier_phase: wave-1-scaffolding-stub
allowed-tools: Read, Glob, Grep
---

# Skill stub: /lint-check-pillar-c-part-6b-sync

> **STUB.** Wave 1 scaffolding placeholder. Логика lint check'а НЕ реализована.
> Phase B materialization (post-Wave-1.4 ack) implements grep-based + hash-match
> verification per Pillar C / Part 11 architecture.

## Описание

Hash-match invariant per Pillar C §B.1 + §J.5: count(`principles/tier-2-system/foundation-generic/*.md`) == 11 == count(constitutional_never_list entries в `.claude/config/default-deny-table.yaml`); каждая entry hash-matches на canonical principle file (action_class, trigger, enforcement, grade, fundamental_anchor). Fail-loud per FUNDAMENTAL §5.5.

## Wave 1 status

`stub-phase-b-materialization` — skill file exists для archival reference; не
выполняется до Phase B materialization. До активации этого lint check'а
sync invariants enforce'ятся manually на ack-time review.

## Provenance

- Pillar C architecture: `swarm/wiki/foundations/principles/architecture.md` §H.1 + §J.5 (для Pillar C-related lints)
- Part 11 architecture: `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` §H.1 (для Pillar A-related lints)
- Part 7 Bundle 5 supplement: `swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md` §K.X (для Pillar B-related lints)
- Wave 1 scaffolding brief: `prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md` §3.12
