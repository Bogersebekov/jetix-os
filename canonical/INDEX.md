---
title: Canonical Docs INDEX — single source of truth navigation
date: 2026-05-06
type: index
status: active
git_tag_planned: canonical-organized-2026-05-06
parent_walkthrough: ../CANONICAL-WALKTHROUGH-2026-05-06.md
parent_inventory: ../reports/canonical-docs-inventory-2026-05-06.md
parent_cleanup_prompt: ../prompts/server-cc-canonical-cleanup-2026-05-06.md
authority: Ruslan walkthrough ack 110-item checklist (2026-05-06)
---

# Canonical Docs — Source of Truth (2026-05-06)

> **See first:** [JETIX-DOCUMENT-MAP-2026-05-15.md](../decisions/JETIX-DOCUMENT-MAP-2026-05-15.md) — карта местности всех актуальных documents + 3 mermaid + 4 reading tracks per audience. Используется как primary orientation для video screen-share, L1 onboarding, и self-orientation.

> Это **single page** со ссылками на все active canonical документы Jetix OS.
> Каждый doc ниже — LOCKED canonical (production source-of-truth) или active living
> infrastructure. Пройти структурированный walkthrough всего что было — см.
> [CANONICAL-WALKTHROUGH-2026-05-06.md](../CANONICAL-WALKTHROUGH-2026-05-06.md)
> (root) или [reports/canonical-docs-inventory-2026-05-06.md](../reports/canonical-docs-inventory-2026-05-06.md).
>
> Что-то в архиве — см. [archive/INDEX.md](../archive/INDEX.md).
> Deferred — [deferred/INDEX.md](../deferred/INDEX.md).

---

## 1. Конституция (Tier 1)

- [JETIX-VISION-FUNDAMENTAL-2026-04-27](../decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md) — 2624 строки — constitutional anchor (35 use cases × 12 categories, 11 hard rules); Layer 1 of 2

---

## 2. Концепция системы

- [JETIX-WORKSHOP-CONCEPT-2026-04-30](../decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md) — Workshop metaphor (мастерская); LOCKED v1.0
- [JETIX-TRM-MODEL-2026-04-30](../decisions/JETIX-TRM-MODEL-2026-04-30.md) — Total Resource Management (TRM); LOCKED v1.0 (companion canonical to Workshop)
- [BASE-MANAGEMENT-SYSTEM-2026-05-04](../decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md) — Документ 1A — universal базовая система управления
- [JETIX-CORPORATION-2026-05-05](../decisions/JETIX-CORPORATION-2026-05-05.md) — Документ 1B — applied use case Документа 1A

---

## 3. Foundation Architecture v1.0 (LOCKED 2026-04-28)

> Tag: `foundation-architecture-locked-2026-04-28`. Cycle: `cyc-foundation-build-2026-04-28`.

### 3a. 11 Foundation Parts + Pillar C

| # | Part | Architecture |
|---|------|--------------|
| 1 | System State Persistence | [architecture.md](../swarm/wiki/foundations/part-1-system-state-persistence/architecture.md) |
| 2 | Signal Ingestion & Triage | [architecture.md](../swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md) |
| 3 | Knowledge Base & Methodology Library | [architecture.md](../swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md) |
| 4 | Role Taxonomy & Coordination Protocol | [architecture.md](../swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md) |
| 5 | Compound Learning & Methodology Capture | [architecture.md](../swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md) |
| 6a | Provenance Officer | [architecture.md](../swarm/wiki/foundations/part-6a-provenance-officer/architecture.md) |
| 6b | Human Gate | [architecture.md](../swarm/wiki/foundations/part-6b-human-gate/architecture.md) |
| 7 | Project Lifecycle Substrate | [architecture.md](../swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md) + [Bundle 5 Pillar B supplement](../swarm/wiki/foundations/part-7-project-lifecycle-substrate/bundle-5-supplement-pillar-b.md) |
| 8 | Health Monitoring & System Integrity | [architecture.md](../swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md) |
| 9 | Owner Interaction Scaffold | [architecture.md](../swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md) |
| 10 | External Touchpoints & Network Interface | [architecture.md](../swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md) |
| 11 | Strategic Direction Substrate (Pillar A) | [architecture.md](../swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md) |
| Pillar C | Principles Foundation sub-system | [architecture.md](../swarm/wiki/foundations/principles/architecture.md) |

### 3b. Foundation Master Overviews

- [Technical overview (engineering audience)](../swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md)
- [Workshop / Human overview (founder / partner / investor)](../swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md)

### 3c. F8 Constitutional Schemas

| Schema | Path |
|--------|------|
| Message v2.0.0 | [shared/schemas/message.schema.json](../shared/schemas/message.schema.json) |
| Task contract | [shared/schemas/task.schema.json](../shared/schemas/task.schema.json) |
| Task return packet (Part 4 §I.1) | [shared/schemas/task-return-packet.json](../shared/schemas/task-return-packet.json) |
| Briefing | [shared/schemas/briefing.schema.json](../shared/schemas/briefing.schema.json) |
| Executor binding template (IP-1 Role≠Executor) | [shared/schemas/executor-binding.yaml.template](../shared/schemas/executor-binding.yaml.template) |
| Default-Deny table (Part 6b §I.2) | [.claude/config/default-deny-table.yaml](../.claude/config/default-deny-table.yaml) |
| Principle doc | [shared/schemas/principle-doc.json](../shared/schemas/principle-doc.json) |
| Project strategy | [shared/schemas/project-strategy.json](../shared/schemas/project-strategy.json) |
| Strategic direction doc | [shared/schemas/strategic-direction-doc.json](../shared/schemas/strategic-direction-doc.json) |
| Decisions DB | [shared/schemas/decisions-db.json](../shared/schemas/decisions-db.json) |

---

## 4. Top-level Living Configuration

- [CLAUDE.md](../CLAUDE.md) — master configuration (Tier 2 Pillar C inlined; Source of Truth section points here)
- [HOME.md](../HOME.md) — entry point overview
- [README.md](../README.md) — repo README
- [MIGRATION.md](../MIGRATION.md) — wiki v1 → v2 migration tracker
- [_meta/conventions.md](../_meta/conventions.md) — file/naming/log conventions

---

## 5. Operational Pipelines

- [reports/retrospective_2025-05_to_2026-04.md](../reports/retrospective_2025-05_to_2026-04.md) — annual retrospective
- [swarm/wiki/operations/quick-log-template.md](../swarm/wiki/operations/quick-log-template.md) — time-tracking quick log template
- [swarm/wiki/operations/](../swarm/wiki/operations/) — time-tracking pipeline folder
- [tools/](../tools/) — voice pipeline scripts (transcribe / extract / filter / review_report)

---

## Что НЕ canonical (но preserved)

- **Archive** — [archive/INDEX.md](../archive/INDEX.md) (~63 docs — pre-Foundation work, superseded; append-only via git mv)
- **Deferred** — [deferred/INDEX.md](../deferred/INDEX.md) (5 strategic insights + 1 active WIP companion)
- **Strategic Layer F2 scaffolds** — [decisions/strategic/](../decisions/strategic/) (29 D-Lock entries + 4 insights + 7 templates — F2 promotion queue для Wave 1.4; NOT moved, mentioned in deferred/INDEX.md as "linked, not moved")
- **Reports** — [reports/](../reports/) (33 historical research deliverables + inventory + 2026-05-06 audit reports — kept where they are)
- **Prompts** — [prompts/](../prompts/) (149 brigadier prompts + handoff chats — kept where they are)
- **Active Wave 1.4 packet** — [decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-28.md](../decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-28.md) (KEPT active per EXCEPTION — pending Wave 1.4 ack)

---

## Provenance

- Authority: Ruslan walkthrough ack via 110-item checklist
- Walkthrough: [CANONICAL-WALKTHROUGH-2026-05-06.md](../CANONICAL-WALKTHROUGH-2026-05-06.md)
- Companion inventory: [reports/canonical-docs-inventory-2026-05-06.md](../reports/canonical-docs-inventory-2026-05-06.md)
- Cleanup execution: [prompts/server-cc-canonical-cleanup-2026-05-06.md](../prompts/server-cc-canonical-cleanup-2026-05-06.md)
- Constitutional anchor: Tier 2 Rule 2 (gate = walkthrough ack); Default-Deny → draft branch; append-only via git mv
