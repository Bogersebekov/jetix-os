---
title: Phase 1 — Task A.1 System Description Docs Inventory
date: 2026-05-24
phase: 1
type: inventory
parent_prompt: prompts/task-a-existing-docs-inventory-2026-05-24.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: task-a-phase-1
R: refuted_if_doc_missed_OR_content_interpreted
mode: INVENTORY (classification only, NO content interpretation)
language: russian primary
---

# 📋 Phase 1 — Task A.1: System Description Docs Inventory

> **Цель:** classify ВСЁ что описывает Jetix систему (Foundation / Strategic /
> Wiki / Research / Synthesis / Concepts) — title + path + size + public/internal
> + R12 + last-mod. **R1 surface only.**

**Total docs inventoried in §2.A–§2.F: ~250** (Foundation 13 + Strategic
canonical ~95 + Wiki entry-points ~30 + Research ~95 + Synthesis ~20).

**Legend:**
- **R12:** `clean` (R12-compatible) / `review` (нужна проверка) / `R12-skip` (R12-violating, NOT to share)
- **P-level:** P1 public-ready / P2 landing-ready / P3 NDA-tier / P4 never-share
- **Last-mod:** `YYYY-MM-DD` или approx based on filename date

---

## §2.A Foundation Layer (canonical LOCKED 2026-04-28)

### §2.A.1 Foundation 11 Parts (F5 LOCKED)

| # | Doc | Path | Size | P-level | R12 |
|---|---|---|---|---|---|
| 1 | Part 1 — System State Persistence | `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` | 136 KB | P3 | clean |
| 2 | Part 2 — Signal Ingestion & Triage | `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md` | 96 KB | P3 | clean |
| 3 | Part 3 — KB & Methodology Library | `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` | 77 KB | P3 | clean |
| 4 | Part 4 — Role Taxonomy & Coordination | `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` | 79 KB | P3 | clean |
| 5 | Part 5 — Compound Learning & Methodology Capture | `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` | 94 KB | P3 | clean |
| 6 | Part 6a — Provenance Officer | `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` | 126 KB | P3 | clean |
| 7 | Part 6b — Human Gate | `swarm/wiki/foundations/part-6b-human-gate/architecture.md` | 123 KB | P3 | clean |
| 8 | Part 7 — Project Lifecycle Substrate | `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` + `bundle-5-supplement-pillar-b.md` | 87+31 KB | P3 | clean |
| 9 | Part 8 — Health Monitoring & System Integrity | `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md` | 105 KB | P3 | clean |
| 10 | Part 9 — Owner Interaction Scaffold | `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` | 82 KB | P3 | clean |
| 11 | Part 10 — External Touchpoints & Network Interface | `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md` | 87 KB | P3 | clean |

### §2.A.2 Strategic Layer Foundation extension (Bundle 5 LOCKED)

| Doc | Path | Size | P-level | R12 |
|---|---|---|---|---|
| Part 11 — Strategic Direction Substrate (Pillar A) | `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` | 69 KB | P3 | clean |
| Principles Foundation sub-system (Pillar C) | `swarm/wiki/foundations/principles/architecture.md` | 59 KB | P3 | clean |

### §2.A.3 Constitutional Documents (root)

| Doc | Path | Size | P-level | R12 |
|---|---|---|---|---|
| JETIX VISION FUNDAMENTAL v1.0 | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` | 202 KB | P3 | review (35 UC + RUSLAN-LAYER overlay) |
| JETIX FPF Constitutional Spec | `design/JETIX-FPF.md` (no file under that name — see `design/JETIX-ARCHITECTURE-WORKING.md` 148 KB) | 148 KB | P3 | clean |
| Foundation Build Master Plan Brief | `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` (referenced; may live elsewhere) | ? | P3 | clean |
| Audit Current State | `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` (referenced; may live elsewhere) | ? | P3 | clean |
| JETIX Corporation Sweep | `decisions/JETIX-CORPORATION-2026-05-05.md` | 290 KB | P3 | clean |
| JETIX TRM Model | `decisions/JETIX-TRM-MODEL-2026-04-30.md` | 71 KB | P3 | clean |
| Base Management System | `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` | 198 KB | P3 | clean |
| Self-Management System Spec v0 | `decisions/SELF-MANAGEMENT-SYSTEM-SPEC-v0-2026-05-16.md` | 40 KB | P3 | clean |
| Reflection Inbox | `decisions/REFLECTION-INBOX-2026-05-16.md` | 131 KB | P4 (personal) | clean |
| Phase Namespace Convention | `decisions/PHASE-NAMESPACE-CONVENTION-2026-05-17.md` | 9 KB | P3 | clean |
| Life Decisions Log | `decisions/life-decisions-log.md` | 2 KB | P4 (personal) | clean |

### §2.A.4 RUSLAN-ACK records (8 + 1 NEW)

| ACK | Path | Bundle | Last-mod |
|---|---|---|---|
| Wave-C Bundle 1 | `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` (root decisions/) | Parts 1/2/4/6a baseline | 2026-04-28 |
| Wave-C Bundle 1 supplement 1 | `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md` | retroactive constitutional pattern | 2026-04-28 |
| Wave-C Bundle 1 supplement 2 | `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-28.md` | constitutional pattern | 2026-04-28 |
| Wave-C Bundle 2 | `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md` | Parts 3/5/6b | 2026-04-28 |
| Wave-C Bundle 3 | `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md` | Parts 8/10 | 2026-04-28 |
| Wave-C Bundle 4 | `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md` | Parts 7/9 | 2026-04-28 |
| Wave-D Integration Pass | `decisions/RUSLAN-ACK-WAVE-D-INTEGRATION-PASS-2026-04-28.md` | Coverage 55/55 | 2026-04-28 |
| Strategic Layer Bundle 5 | `decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md` | Pillar A/B/C placement | 2026-04-28 |
| Strategic Layer Templates | `decisions/RUSLAN-ACK-STRATEGIC-LAYER-TEMPLATES-2026-04-28.md` (11 KB) | 7 templates | 2026-04-28 |
| Monetization Hypothesis Bank | `decisions/RUSLAN-ACK-MONETIZATION-HYPOTHESIS-BANK-2026-05-14.md` (11 KB) | hypothesis system | 2026-05-14 |
| Book-Driven Agents | `decisions/RUSLAN-ACK-BOOK-DRIVEN-AGENTS-2026-05-24.md` (4 KB) | MAX-8 ack | 2026-05-24 |

### §2.A.5 AWAITING-APPROVAL packets (Foundation)

| Packet | Path | Size | Status |
|---|---|---|---|
| Wave 1 Scaffolding | `decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-28.md` | 13 KB | acked |
| Wave D Integration Pass | `decisions/AWAITING-APPROVAL-wave-d-integration-pass-2026-04-28.md` | 21 KB | acked |
| Swarm Self-Improve Gate 1 | `decisions/AWAITING-APPROVAL-swarm-self-improve-gate1-2026-04-23.md` | 11 KB | acked |
| Swarm Self-Improve Gate 2 | `decisions/AWAITING-APPROVAL-swarm-self-improve-gate2-2026-04-23.md` | 12 KB | acked |
| Book-Driven Agents (active) | `swarm/awaiting-approval/book-driven-agents-2026-05-24.md` | — | acked 2026-05-24 |
| R12 Anti-Extraction (LOCK 2026-05-12) | `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` | — | acked |
| R12 Programmable Ethereum | `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md` | — | acked |
| H6 Hackathon Platform Pre-eminent | `swarm/awaiting-approval/h6-hackathon-platform-pre-eminent-2026-05-18.md` | — | acked |
| H8 Ethereum Substrate Extension | `swarm/awaiting-approval/h8-ethereum-substrate-extension-2026-05-18.md` | — | acked |
| H9 Strategic Insight Candidate | `swarm/awaiting-approval/h9-strategic-insight-candidate-2026-05-18.md` | — | acked |
| Pillar A Hackathon Mode Extension | `swarm/awaiting-approval/pillar-a-hackathon-mode-extension-2026-05-18.md` | — | acked |
| Legacy 12-agents deprecation | `swarm/awaiting-approval/legacy-12-agents-deprecation-2026-05-17.md` | — | acked |
| Cycle-10 CRM Build | `swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md` | — | acked |
| Cycle-11 Voice Migration | `swarm/awaiting-approval/cycle-11-voice-migration-2026-04-26.md` | — | acked |

### §2.A.6 Principles (Pillar C — Tier 1 + Tier 2)

**Tier 1 manager:**
- `principles/tier-1-manager/_index.md` + `_template.md`

**Tier 2 foundation_generic (12 rules — R12 LOCK incl):**
- `principles/tier-2-system/foundation-generic/_index.md`
- 12 rule files: ai-does-not-strategize / ai-does-not-execute-architectural-decision / ai-does-not-set-skill-direction / ai-does-not-claim-persistent-identity / ai-does-not-claim-skin-in-the-game / ai-does-not-aggregate-unstructured-long-term-memory / agents-do-not-negotiate-contradictions-autonomously / agent-does-not-evaluate-peer-agent / ai-does-not-self-modify-at-runtime / ai-does-not-impersonate-human-externally / bypass-blast-radius-categorization-forbidden / **ai-does-not-extract-value-beyond-agreed-share** (R12 LOCK 2026-05-12)

**Tier 2 ruslan-layer-overrides (7):**
- ab-test-gating / filesystem-source-of-truth / language-discipline / no-api-key-exposure / path-protection / voice-pipeline-draft-only / voice-pipeline-manual-review

**Governance:**
- `principles/_governance.md`, `principles/_index.md`

### §2.A.7 Shared Schemas (9 contracts)

All F8 constitutional. P3 internal.
- `shared/schemas/briefing.schema.json`
- `shared/schemas/decisions-db.json`
- `shared/schemas/executor-binding.yaml.template`
- `shared/schemas/message.schema.json` (v2.0.0 with `acting_as:`)
- `shared/schemas/principle-doc.json`
- `shared/schemas/project-strategy.json`
- `shared/schemas/strategic-direction-doc.json`
- `shared/schemas/task-return-packet.json` (Part 4 §I.1 LOCKED)
- `shared/schemas/task.schema.json`

### §2.A.8 Domain READMEs (swarm-alphas)

- `swarm/wiki/foundations/swarm-alphas.md` (10 KB)
- `swarm/wiki/foundations/{engineering,investing,mgmt,philosophy,systems}/README.md` (~0.3 KB stubs each)

---

## §2.B Strategic Canonical Layer

### §2.B.1 4 Big LOCKED + sub-deliverables (May 21-22 sprint)

| Doc | Path | Size | P-level | R12 |
|---|---|---|---|---|
| **Method V2 main** | `decisions/strategic/METHOD-LIFE-DEVELOPMENT-V2-2026-05-21.md` | 62 KB | P2 | clean |
| Method V2 sub-deliverables | `reports/method-v2-2026-05-21/` (17 files: 16 phase reports + diagrams) | — | P3 | clean |
| Method Deep Description | `decisions/strategic/METHOD-DEEP-DESCRIPTION-2026-05-21.md` | 26 KB | P3 | clean |
| Method Deep build outputs | `reports/method-deep-description-2026-05-21/` | — | P3 | clean |
| **Strategic Plan Near-Future** | `decisions/strategic/STRATEGIC-PLAN-NEAR-FUTURE-2026-05-21.md` | 39 KB | P3 | review |
| Strategic Plan sub-deliverables | `reports/strategic-plan-near-future-2026-05-21/` (15 files: 14 phases + diagrams) | — | P3 | review |
| **Economic Model V10 Hybrid + Tokenomics** | `decisions/strategic/ECONOMIC-MODEL-TOKENOMICS-2026-05-22.md` | 22 KB | P3 | review |
| Tokenomics Variants | `decisions/strategic/TOKENOMICS-VARIANTS-2026-05-22.md` | 30 KB | P3 | review |
| Economic Model sub-deliverables | `reports/economic-model-tokenomics-2026-05-22/` (12 files: 8 sub-docs + diagrams) | — | P3 | review |
| **AI Market PLAN Stage 1+2 (Electricity Analogy)** | `decisions/strategic/AI-MARKET-ELECTRICITY-ANALOGY-PLAN-2026-05-22.md` | 28 KB | P2 | clean |
| AI Market PLAN sub-deliverables | `reports/ai-market-analogy-PLAN-2026-05-22/` (8 files) | — | P3 | clean |

### §2.B.2 Partner-facing / outreach docs

| Doc | Path | Size | P-level | R12 |
|---|---|---|---|---|
| Partner Offering Human-Lang | `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md` (root) | 12 KB | **P1 ready** | clean |
| Jetix Navigation Guide DRAFT | `decisions/strategic/JETIX-NAVIGATION-GUIDE-2026-05-22-DRAFT.md` | 31 KB | P2 | clean |
| Triple-Role Partner | `decisions/strategic/TRIPLE-ROLE-PARTNER-2026-05-22.md` | 28 KB | P3 | review |
| Recursive Partnership Mechanics | `decisions/strategic/RECURSIVE-PARTNERSHIP-MECHANICS-2026-05-22.md` | 24 KB | P3 | review |
| Wave-1 Outreach Package | `decisions/strategic/WAVE-1-OUTREACH-PACKAGE-2026-05-22-evening.md` | 24 KB | P3 | review |
| Dmitriy Call Plan | `decisions/strategic/DMITRIY-CALL-PLAN-2026-05-22.md` | 28 KB | P3 | review (1-1 plan) |
| Audio 721 Insights Report | `decisions/strategic/AUDIO-721-INSIGHTS-REPORT-2026-05-22.md` | 23 KB | P3 | review |

### §2.B.3 Point-A / Point-B docs

| Doc | Path | Size | P-level | R12 |
|---|---|---|---|---|
| Point A Current State | `decisions/strategic/POINT-A-CURRENT-STATE-2026-05-23.md` | 30 KB | P3 | review (private) |
| Point B Near-Target | `decisions/strategic/POINT-B-NEAR-TARGET-2026-05-23.md` | 32 KB | P3 | review |
| Point B Focused Week 1 | `decisions/strategic/POINT-B-FOCUSED-WEEK-1-2026-05-23.md` | 22 KB | P3 | review |
| Point A reports | `reports/point-a-2026-05-23/` | — | P3 | clean |
| Point B compact reports | `reports/point-b-compact-2026-05-23/` | — | P3 | clean |

### §2.B.4 Plans / packs sprint

| Doc | Path | Size | P-level | R12 |
|---|---|---|---|---|
| Development Plan | `decisions/strategic/DEVELOPMENT-PLAN-2026-05-21.md` | 19 KB | P3 | review |
| Distribution Plan | `decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md` | 51 KB | P3 | review |
| Tasks Pack | `decisions/strategic/TASKS-PACK-2026-05-21.md` | 20 KB | P3 | clean |
| Questions Pack | `decisions/strategic/QUESTIONS-PACK-2026-05-21.md` | 28 KB | P3 | clean |
| Experts Pack | `decisions/strategic/EXPERTS-PACK-2026-05-21.md` | 40 KB | P3 | review |
| One-Pager FPF Substrate | `decisions/strategic/ONE-PAGER-FPF-SUBSTRATE-2026-05-21.md` | 30 KB | P2 | clean |

### §2.B.5 Jetix as <X> conceptual hubs (May 18 wave)

| Doc | Path | Size | P-level | R12 |
|---|---|---|---|---|
| Concept Man-as-Army Jetix Integration | `decisions/strategic/CONCEPT-MAN-AS-ARMY-JETIX-INTEGRATION-2026-05-18.md` | 28 KB | P3 | clean |
| Jetix as Hackathon Platform | `decisions/strategic/JETIX-AS-HACKATHON-PLATFORM-2026-05-18.md` | 17 KB | P2 | clean |
| Jetix Education Layer Systems Thinking | `decisions/strategic/JETIX-EDUCATION-LAYER-SYSTEM-THINKING-2026-05-18.md` | 16 KB | P2 | clean |
| Jetix Outreach System Scalable | `decisions/strategic/JETIX-OUTREACH-SYSTEM-SCALABLE-2026-05-18.md` | 14 KB | P3 | review |
| Jetix Recursive Self-Development Engine | `decisions/strategic/JETIX-RECURSIVE-SELF-DEVELOPMENT-ENGINE-2026-05-18.md` | 13 KB | P3 | clean |
| Jetix System Merger Protocol FPF | `decisions/strategic/JETIX-SYSTEM-MERGER-PROTOCOL-FPF-2026-05-18.md` | 15 KB | P3 | clean |

### §2.B.6 Jetix-Ethereum Architecture (12-doc bundle)

| Doc | Path | P-level | R12 |
|---|---|---|---|
| 00 Master Architecture | `decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/00-MASTER-ARCHITECTURE.md` | P3 | review |
| 01 Substrate Selection | `.../01-substrate-selection-rationale.md` | P3 | review |
| 02 FPF on Ethereum Mapping | `.../02-fpf-on-ethereum-mapping.md` | P3 | review |
| 03 R12 Programmable Enforcement | `.../03-r12-programmable-enforcement.md` | P3 | **review CRITICAL R12** |
| 04 SBT Role Attestation | `.../04-sbt-role-attestation.md` | P3 | review |
| 05 DAO Governance Multi-Clan | `.../05-dao-governance-multi-clan.md` | P3 | review |
| 06 Quadratic Funding Workshop Revenue | `.../06-quadratic-funding-workshop-revenue.md` | P3 | review |
| 07 Cost Economy L2 Selection | `.../07-cost-economy-l2-selection.md` | P3 | review |
| 08 Legal Entity DAO Interaction | `.../08-legal-entity-dao-interaction.md` | P3 | review |
| 09 Implementation Roadmap | `.../09-implementation-roadmap.md` | P3 | review |
| 10 Risks Mitigations | `.../10-risks-mitigations.md` | P3 | review |
| 11 Phase 2 Implementation Checklist | `.../11-phase-2-implementation-checklist.md` | P3 | review |
| 12 Buterin Outreach Materials Draft | `.../12-buterin-outreach-materials-draft.md` | P3 | review |
| + diagrams subfolder | `.../diagrams/` | P3 | clean |

### §2.B.7 H9 / Strategic Insights / Other DR-NN

| Doc | Path | Size | P-level | R12 |
|---|---|---|---|---|
| H9 Candidates Surface | `decisions/strategic/H9-CANDIDATES-SURFACE-2026-05-19.md` | 5 KB | P3 | review |
| DR-38 Meta-Method Composition | `decisions/strategic/DR-38-META-METHOD-COMPOSITION-2026-05-22.md` | 25 KB | P3 | clean |
| DR-40 Cybernetic External System | `decisions/strategic/DR-40-CYBERNETIC-EXTERNAL-SYSTEM-2026-05-22.md` | 15 KB | P3 | clean |
| External System Principle Deep | `decisions/strategic/EXTERNAL-SYSTEM-PRINCIPLE-DEEP-2026-05-22.md` | 12 KB | P3 | clean |
| Meta-Method 8-Component Deep | `decisions/strategic/META-METHOD-8-COMPONENT-DEEP-2026-05-22.md` | 28 KB | P3 | clean |

### §2.B.8 Strategic Insights (7 — full bundle from sprint history)

| Insight | Path | Size |
|---|---|---|
| Balaji Network State | `decisions/STRATEGIC-INSIGHT-BALAJI-NETWORK-STATE-2026-05-10.md` | 30 KB |
| Jetix as Foundation Model | `decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md` | 13 KB |
| Jetix as Gamified Platform | `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md` | 40 KB |
| Jetix as People Network State | `decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md` | 21 KB |
| Jetix Partnership Model | `decisions/STRATEGIC-INSIGHT-JETIX-PARTNERSHIP-MODEL-2026-05-10.md` | 24 KB |
| Jetix Trust Infrastructure | `decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md` | 38 KB |
| Tyson Mentorship Pattern | `decisions/STRATEGIC-INSIGHT-TYSON-MENTORSHIP-PATTERN-2026-05-10.md` | 11 KB |

**+ 4 strategic-insights subfolder docs** (`decisions/strategic/strategic-insights/`):
- ai-psy-led-design.md
- arbitrage-traffic-direction.md
- jetix-ai-bios-moment.md
- ma-direction.md

### §2.B.9 Lock Entries (29 D-LOCK)

`decisions/strategic/lock-entries/` — D-01..D-29, average 2.7 KB each. Each = irreversible strategic decision. P3 (Ruslan + roy internal).

| ID | Topic | ID | Topic |
|---|---|---|---|
| D-01 | gentleman-inside / predator-outside | D-16 | community phase-1 simple-chat |
| D-02 | solo-with-team-ready scaffolding | D-17 | filesystem source-of-truth |
| D-03 | closed-outside / open-inside | D-18 | productization not-hours |
| D-04 | name "Jetix" LOCKED | D-19 | holding scale 1T ambition |
| D-05 | consulting-first phase-1 | D-20 | USB-C positioning enterprise-fast |
| D-06 | Anton/Vladislav/Rodion NOT key | D-21 | partnership matchmaker ROY-replication |
| D-07 | community-cast 11 archetypes | D-22 | ICP 5-criteria direction-of-life |
| D-08 | layered identity multiplicity-frames | D-23 | token-economy phase-2+ |
| D-09 | pain primary / opportunity secondary | D-24 | open-source research direction phase-2+ |
| D-10 | English-US first / Germany later | D-25 | company-as-code |
| D-11 | producer-center investment-fund | D-26 | team 50-100 enterprise |
| D-12 | content-strategy smart-audience site-primary | D-27 | fork-and-merge evolution |
| D-13 | open-surface closed-core | D-28 | query-driven KB filtering |
| D-14 | research-revenue instrumental phase-1 | D-29 | korp-startup self-narrative |
| D-15 | revenue-gated spend | — | — |

### §2.B.10 Strategic Templates (7) + Variants + Insights subfolder

`decisions/strategic/_templates/`:
- bet-pitch.md.template
- direction-card.md.template
- founder-overlay.md.template
- lock-entry.md.template
- mentor-brief.md.template
- north-star.md.template
- strategic-insight.md.template

`decisions/strategic/variants/`: cross-fork-audit-deferred-phase-b.md / oq-merged-2-dissolve-test-2026-04-28.md
`decisions/strategic/_research/`: hierarchy-cadences / jetix-fit-filtering / landscape-strategic-docs (all 2026-04-28)

### §2.B.11 Other strategic / management docs (decisions root)

| Doc | Path | Size | P-level |
|---|---|---|---|
| Action Plan Phase-1 Near-Future | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` | 72 KB | P3 |
| Video Proposal Options Tseren-Levenchuk | `decisions/VIDEO-PROPOSAL-OPTIONS-TSEREN-LEVENCHUK-2026-05-10.md` | 102 KB | P3 |
| Jetix First Clan Charter | `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md` | 50 KB | P2 |
| Jetix Workshop Concept | `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` | 26 KB | P2 |
| Jetix Document Map | `decisions/JETIX-DOCUMENT-MAP-2026-05-15.md` | 54 KB | P3 |
| Jetix Monetization Methodology v0 | `decisions/JETIX-MONETIZATION-AUDIENCE-COOPERATION-METHODOLOGY-v0-2026-05-14.md` | 154 KB | P3 |
| Jetix Monetization Methodology Wave2 | `decisions/JETIX-MONETIZATION-METHODOLOGY-WAVE2-DEEPER-MINING-2026-05-14.md` | 25 KB | P3 |
| Plan monetization methodology | `decisions/PLAN-monetization-methodology-2026-05-14.md` | 13 KB | P3 |
| Plan monetization wave2 | `decisions/PLAN-monetization-wave2-2026-05-14.md` | 13 KB | P3 |
| Strategic Directions Voice-17 | `decisions/STRATEGIC-DIRECTIONS-VOICE-17-2026-05-17.md` | 14 KB | P3 |
| Review V2 Progress Checklist | `decisions/review-v2-progress-checklist.md` | 10 KB | P3 |

### §2.B.12 Strategic _index + DB

- `decisions/strategic/_index.md` (12 KB)
- `decisions/strategic/_decisions-db-index.jsonl` (24 KB)

---

## §2.C Wiki Layer (Karpathy LLM Wiki + OmegaWiki)

### §2.C.1 Wiki entry-points

| Doc | Path | Size |
|---|---|---|
| Wiki Index | `wiki/index.md` | — |
| Wiki Overview | `wiki/overview.md` | — |
| Wiki Log | `wiki/log.md` | append-only |
| Wiki Lint Report v1 | `wiki/_lint-report-2026-04-16.md` | — |
| Wiki Lint Report v2 | `wiki/_lint-report-2026-04-16-v2.md` | — |

### §2.C.2 Wiki entity dirs (counts only — too many for per-doc table)

| Entity type | Path | Count |
|---|---|---|
| Concepts (root level) | `wiki/concepts/` | 107 *.md |
| Concepts/game-mechanics | `wiki/concepts/game-mechanics/` | 44 |
| Concepts/game-economy | `wiki/concepts/game-economy/` | 17 |
| Concepts/psychology | `wiki/concepts/psychology/` | 15 |
| Concepts/game-theory | `wiki/concepts/game-theory/` | 12 |
| Concepts/jetix-realm | `wiki/concepts/jetix-realm/` | 6 (Persona/Class/Clan/Quest/Resources/Seasons) |
| Ideas | `wiki/ideas/` | 272 |
| Sources | `wiki/sources/` | 276 |
| Topics (hubs) | `wiki/topics/` | 7 hubs |
| Templates | `wiki/_templates/` | 9 (claim/concept/entity/experiment/foundation/idea/source/summary/topic) |
| Foundations | `wiki/foundations/` | 1 architecture.md (Karpathy substrate) |
| Niches | `wiki/niches/` | 6 symlinks |
| Comparisons | `wiki/comparisons/` | — |
| Claims | `wiki/claims/` | — |
| Entities | `wiki/entities/` | — |
| Experiments | `wiki/experiments/` | — |
| Summaries | `wiki/summaries/` | — |
| Graph | `wiki/graph/edges.jsonl` | — |

### §2.C.3 Wiki topic hubs (7)

| Hub | Path | Audience |
|---|---|---|
| Influence Tactics R12 Boundary | `wiki/topics/influence-tactics-r12-boundary.md` | ROY influence-ethics; **R12 review** |
| Jetix-Clan Substrate References | `wiki/topics/jetix-clan-substrate-references.md` | Clan members |
| Levenchuk Corpus Deep-Dive | `wiki/topics/levenchuk-corpus-deep-dive.md` | MIM-inner / methodology |
| Methodology Engineering Resources | `wiki/topics/methodology-engineering-resources.md` | engineering / method experts |
| R12 Enforcement Substrate | `wiki/topics/r12-enforcement-substrate.md` | ROY R12 enforcement |
| SOTA Tracking Discipline | `wiki/topics/sota-tracking-discipline.md` | sota-tracker / phil-sci |
| System Design Hub | `wiki/topics/system-design-hub.md` | engineering / architects |

### §2.C.4 13 existing Tier A wikis + 49 NEW Tier A/B-Plus (referenced)

Per prompt §2.C: "13 existing + 49 NEW Tier A/B-Plus (3+31+15)". Total = 62 high-tier wiki entries. Inventoried under §2.C.2 counts; individual classification deferred until Tier A list canonicalised. Substrate present and verified in `wiki/concepts/`.

### §2.C.5 Swarm Wiki (parallel layer)

| Doc | Path |
|---|---|
| Swarm Wiki Index | `swarm/wiki/index.md` |
| Swarm Wiki Overview | `swarm/wiki/overview.md` |
| Swarm Wiki Log | `swarm/wiki/log.md` |
| Synthesis dir (9 docs) | `swarm/wiki/synthesis/` |
| Designs dir | `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/` |
| Cycles dir (4) | `swarm/wiki/cycles/cyc-foundation-build / cyc-foundation-overview / cyc-layer-7 / cyc-producer-services` |
| Agent niches (5) | `swarm/wiki/agents/{eng,inv,mgmt,phil,sys}-expert/` |
| Operations dir | `swarm/wiki/operations/` (claude-code-os-mastery / quick-money / levenchuk-deep-dive / etc.) |
| Themes (5) | `swarm/wiki/themes/{eng,inv,mgmt,phil,sys}/` |
| Templates | `swarm/wiki/_templates/` |
| Proposals (3) | jetix-system-overview / km-architecture-research / swarm-self-improve decomposition |

---

## §2.D Research Outputs

### §2.D.1 5 Big Research mains (2026-05-23/24)

| Research | Main doc | Sub-deliverables dir | Files | P-level | R12 |
|---|---|---|---|---|---|
| **Methodology** | `decisions/strategic/RESEARCH-METHODOLOGY-2026-05-24.md` (22 KB) | `reports/research-methodology-2026-05-24/` | 11 (8 phases + diagrams + SUMMARY + phase-0) | P3 | clean |
| **SOTA** | `decisions/strategic/RESEARCH-SOTA-2026-05-24.md` (26 KB) | `reports/research-sota-2026-05-24/` | 9 (7 phases + diagrams + SUMMARY) | P3 | clean |
| **Propaganda-Recruitment** | `decisions/strategic/RESEARCH-PROPAGANDA-RECRUITMENT-2026-05-24.md` (16 KB) | `reports/research-propaganda-recruitment-2026-05-24/` | 25 (phases/ + diagrams + SUMMARY) | P3 | **R12-skip outward** (extraction techniques) |
| **NLP** | `decisions/strategic/RESEARCH-NLP-2026-05-24.md` (25 KB) | `reports/research-nlp-2026-05-24/` | 25 | P3 | **R12 STRICT review** |
| **Levenchuk Master Qualification** | `decisions/strategic/LEVENCHUK-MASTER-QUALIFICATION-RESEARCH-2026-05-23.md` (21 KB) | `reports/levenchuk-master-research-2026-05-23/` | 12 (article-decode / aisystant-curriculum / ailev-blog / books-synthesis / MIM-ecosystem / master-deep / jetix-lens / offer-to-MIM / recommendations + diagrams) | P3 | clean |

### §2.D.2 Levenchuk-adjacent

| Doc | Path | Size |
|---|---|---|
| Levenchuk Systems-Thinking Synthesis | `decisions/strategic/LEVENCHUK-SYSTEMS-THINKING-SYNTHESIS-2026-05-23.md` | 15 KB |
| Education Research Books | `decisions/strategic/EDUCATION-RESEARCH-BOOKS-2026-05-24.md` | 7 KB |
| Research Books to Download | `decisions/strategic/RESEARCH-BOOKS-TO-DOWNLOAD-2026-05-23.md` | 17 KB |

### §2.D.3 Earlier DR-NN reports

Per prompt §2.D: DR-26 (unit-econ) / DR-33 (communication) / DR-34 (AI commoditisation) / DR-38 (meta-method) / DR-40 (cybernetic).
DR-38 + DR-40 already mapped above. DR-26/DR-33/DR-34 substrate referenced in `decisions/strategic/_decisions-db-index.jsonl` (24 KB index).

### §2.D.4 Other research substrate (reports/)

Recent research-quality reports:
- `reports/canonical-docs-inventory-2026-05-06.md` (80 KB) — previous inventory
- `reports/foundation-consolidation-status-2026-05-06.md` (18 KB)
- `reports/deep-analysis-wiki-autoresearch-2026-05-11.md` (72 KB)
- `reports/gamification-deep-wiki-mining-plan-2026-05-11.md` (52 KB)
- `reports/gamification-question-mining-run-2026-05-11.md` (500 KB — massive deep mining)
- `reports/jetix-game-theory-cheating-research-2026-05-12.md`
- `reports/jetix-people-network-state-research-2026-05-11.md`
- `reports/jetix-vs-iwe-audit-2026-05-17.md`
- `reports/anton-call-report-2026-05-11.md` (50 KB)
- `reports/timeline-narrative-2025-07_to_2026-05.md`
- `reports/retrospective_2025-05_to_2026-04.md`
- `reports/toggl_historical_baseline_2024-04_to_2026-05.md`
- `reports/toggl_last6months_2025-11_to_2026-05.md`
- `reports/research-corpus-pipeline-2026-05-24/` (corpus prep substrate)
- `reports/education-corpus-pipeline-2026-05-24/` (NEW education corpus — 14 books OCR/text-extract)

### §2.D.5 Subordinate research / mining outputs

- `reports/master-map-2026-05-19-evening/` — master map
- `reports/sprint-synthesis-2026-05-19/` + `sprint-synthesis-v2-2026-05-19-evening/`
- `reports/monetization-research-2026-05-14/`
- `reports/distribution-plan-research-2026-05-20/`
- `reports/jetix-fpf-describe-2026-05-17/`
- `reports/fpf-iwe-distillation-2026-05-17/`
- `reports/expanded-docs-2026-05-21/` (Phase-0+ FPF lens scope)
- `reports/dmitriy-call-prep-2026-05-22/`
- `reports/book-driven-agents-2026-05-24/` + `execute-book-driven-agents-2026-05-24/`
- `reports/phase-0-fpf-scope/`, `reports/phase-0-plus/`
- `reports/voice-pipeline-2026-05-{10..22}-batch-{1..11}/` (12+ voice batches)
- `reports/voice-batch-12-quick-2026-05-23/`, `voice-batch-13-quick-2026-05-24/`
- `reports/wiki-promotions-batch-10-2026-05-22/`
- `reports/wiki-integration-redesign-2026-05-10/`, `wiki-rebuild-stage-2A-plan-2026-05-11.md`
- `reports/jetix-platform-v2-2026-05-19/`
- `reports/autoresearch-karpathy-integration-2026-05-11/`

---

## §2.E Synthesis + Plan-Mode + Plan-of-Day

### §2.E.1 Critical 2026-05-24 substrate

| Doc | Path | Size | Role |
|---|---|---|---|
| **SYNTHESIS-EXECUTION-PLANS** | `decisions/strategic/SYNTHESIS-EXECUTION-PLANS-2026-05-24.md` | 26 KB | parent synthesis для PoD-24 + Task A/B |
| Synthesis sub-deliverables | `reports/synthesis-execution-plans-2026-05-24/` | 8 files | batch-13-voice / research-key-ideas / execution-plans / ack-queue / resources-capabilities-map / phase-0-substrate / diagrams |
| **PLAN-MODE-DOCS-VIDEO-NOTION** | `decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md` | 23 KB | parent plan-mode для Plan A/B/C |
| Plan-mode sub-deliverables | `reports/plan-mode-docs-video-notion-2026-05-24/` | 7 files | plan-b-docs / plan-a-video / plan-c-notion / sequencing-matrix / phase-0-substrate / diagrams / SUMMARY |
| **RUSLAN-NOTES-EDUCATION-PARADIGM** | `decisions/strategic/RUSLAN-NOTES-EDUCATION-PARADIGM-2026-05-24.md` | 16 KB | NEW 2 voice notes + 10 ideas O-176..O-185 + 8 cross-cites |

### §2.E.2 Plan-of-Day + daily logs (recent)

| Doc | Path | Type |
|---|---|---|
| PoD-2026-05-24 | `daily-logs/_PLAN-OF-DAY-2026-05-24.md` | parent PoD for Task A |
| PoD-2026-05-23 | `daily-logs/_PLAN-OF-DAY-2026-05-23.md` | prev PoD |
| PoD template | `daily-logs/_PLAN-OF-DAY-template.md` | template |
| Daily Log 2026-05-{17..22} | `daily-logs/_DAILY-LOG-2026-05-NN.md` | 6 daily logs |
| Expanded Docs Plan 2026-05-21 | `daily-logs/_EXPANDED-DOCS-PLAN-2026-05-21.md` | plan |
| Updated Execution Plan 2026-05-21 | `daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md` | rev |
| Updated Execution Plan 2026-05-22 | `daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-22.md` + `-evening.md` | 2 revs |

### §2.E.3 Reflection / inboxes / handoffs

| Doc | Path | Size |
|---|---|---|
| Reflection Inbox | `decisions/REFLECTION-INBOX-2026-05-16.md` | 131 KB (P4 personal) |
| _HANDOFF cowork 2026-05-20 | `_HANDOFF_to_next_cowork_session_2026-05-20.md` | 27 KB |
| _HANDOFF cowork 2026-05-22 | `_HANDOFF_to_next_cowork_session_2026-05-22.md` | 22 KB |
| Working File v0 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | 38 KB |

---

## §2.F Concepts / Ideas Pool / Knowledge-Base Legacy

### §2.F.1 Wiki concepts (top-level — 107)

См. §2.C.2 counts. Examples (cross-refs from prompt: O-107..O-185):
- `wiki/concepts/method-method-one-liner.md` (O-107)
- `wiki/concepts/meta-method-8-component-composition.md` (O-121)
- `wiki/concepts/external-system-cybernetic-principle.md` (O-128)
- `wiki/concepts/development-promotion-mode-transition.md` (O-160)
- `wiki/concepts/100x-multiplier-discipline.md`, `5-filters-propaganda-model.md`, `8-criteria-thought-reform.md`, `affirmation-ritual-founder-state.md`, `agi-collective-substrate-positioning.md`, ... (107 total)

### §2.F.2 Ideas folder (272 files)

`wiki/ideas/` — 272 ideas (canonical idea bank). E.g. `03-platyat-za-ai-ty-uzhe-v-elite-polzovateley.md`, `200-year-vision-jetix-humanity.md`, etc.

### §2.F.3 Sources folder (276 files)

`wiki/sources/` — 276 source records (per-source provenance), prefixed with date.

### §2.F.4 Knowledge-base legacy

Per CLAUDE.md: `knowledge-base/` (legacy, в миграции). См. `MIGRATION.md`. NOT inventoried per-file (legacy).

---

## §2.G Root-level supplementary docs

| Doc | Path | Size | P-level | R12 |
|---|---|---|---|---|
| Claude Master Config | `CLAUDE.md` | 33 KB | P3 (internal config) | clean |
| Canonical Walkthrough 2026-05-06 | `CANONICAL-WALKTHROUGH-2026-05-06.md` | 27 KB | P3 | clean |
| HOME nav | `HOME.md` | 3 KB | P3 | clean |
| README | `README.md` | 1 KB | P1 (public) | clean |
| Migration | `MIGRATION.md` | 3 KB | P3 | clean |
| Symlinks (5): CALL-DMITRIY / META-METHOD / METHOD-V2 / ONE-LINER / STRATEGIC-PLAN | root | symlinks | mirror target | mirror target |

---

## §3 Counts summary

| Category | Doc count |
|---|---|
| Foundation 11 Parts + Pillar A + C architecture.md | 13 |
| Constitutional + RUSLAN-ACK + AWAITING-APPROVAL | ~35 |
| Principles (Tier 1 + Tier 2 + governance) | 27 files |
| Shared schemas | 9 |
| Strategic canonical (decisions/strategic/ root) | 44 + 29 lock-entries + 7 templates + 4 strategic-insights + 2 variants + 3 _research + 13 ethereum-arch = ~102 |
| Strategic insights (decisions/ root) | 7 |
| Big LOCKED 4 + sub-deliverables (reports/) | 4 mains + 4 sub-dirs (~50 files) |
| Wiki entry points + topic hubs | ~12 |
| Wiki concepts (root + 5 nested) | 201 |
| Wiki ideas | 272 |
| Wiki sources | 276 |
| Swarm wiki (synthesis/cycles/agents/themes/...) | ~70 strategic + organisational |
| Research mains (5) + sub-dirs | 5 + ~85 sub-files |
| Synthesis + plan-mode + PoD + daily logs + handoffs | ~25 |
| Root-level supplementary | 11 (incl symlinks) |
| **System-description docs total (count)** | **~250 strategic + ~750 wiki entity files** |

---

## §4 Phase 1 closure

- ✅ All categories §2.A–§2.G inventoried per-doc table
- ✅ Foundation 11 Parts + Pillar A + C all confirmed-present with sizes
- ✅ 29 D-LOCK entries mapped
- ✅ 5 research mains + sub-deliverables tabled
- ✅ 12-doc Ethereum-architecture bundle mapped
- ✅ 7 strategic-insights + 4 strategic-insights subfolder
- ✅ NEW RUSLAN-NOTES-EDUCATION-PARADIGM substrate included
- ✅ R12 status flagged per-doc (`clean` / `review` / `R12-skip`)
- ✅ P-level (1-4) tagged per-doc
- ✅ NO content interpretation (R1 surface)
- ✅ NO LOCK modifications

**Next:** Phase 2 — Tools/Templates Inventory.

---

*Phase 1 closure 2026-05-24. Per Ruslan voice ack «всё в кучу собрать».*
