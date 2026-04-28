---
title: "Wave 1 — Review Queue (Wave 1.4 input)"
date: 2026-04-28
type: cycle-review-queue
parent_cycle: cyc-foundation-build-2026-04-28
phase: wave-1-scaffolding-phase-c
F: F2
G: "Wave 1.4 per-artefact review queue — Ruslan-driven migration"
R: R-low
brief: prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md
---

# §0 Mission

40 scaffolded artefacts requiring per-file Ruslan-driven review (Wave 1.4).
29 Lock scaffolds + 4 Insight scaffolds + 7 ruslan_layer_overrides scaffolds.

Migration action enum (per scaffold HTML comment):

- **PROMOTE-AS-IS** — copy candidate to body sections; minor frontmatter cleanup → F4
- **REFACTOR** — rewrite to fit doc-type discipline; preserve intent → F4
- **SPLIT** — multi-artefact; split into N files → drafts F2
- **MERGE / SUPERSEDE-WITH-NEW** — duplicates / new authoring overrides
- **ARCHIVE** — not actually a Lock/Insight/principle; remove from scaffold target
- **PROMOTE-TO-LOCK** (insights only) — Insight stable enough → author Lock Entry
- **PROMOTE-TO-DIRECTION-CARD** (insights only) — Insight stable enough → author Direction Card
- **ESCALATE** — needs Ruslan clarification before action

Priority guidance (per brief §4):

- **HIGH** — critical Locks per `locked_decisions_referenced` в Part 11 frontmatter (D-2, D-12, D-13, D-21, D-22, D-26, D-27, D-29) + foundational thesis Insight (jetix-ai-bios-moment)
- **MEDIUM** — остальные Locks; остальные 3 Insights
- **LOW** — ruslan_layer_overrides scaffolds (operational, low-strategic)

# §1 Lock Entry scaffolds (29)

| Item | File path | Source path | 1-line summary | Priority | Migration options |
|---|---|---|---|---|---|
| D-1 | decisions/strategic/lock-entries/D-01-gentleman-inside-predator-outside.md | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md §Decision 1 | Gentleman inside (member↔member: civility) / Predator outside (network↔world: max-defence). Membrane = quality-gate + subscription. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-2 | decisions/strategic/lock-entries/D-02-solo-with-team-ready-scaffolding.md | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md §Decision 2 | Solo-now-with-team-ready scaffolding architecture discipline. | **HIGH** (referenced in Part 11 frontmatter D-2 architect-orbit) | PROMOTE-AS-IS / REFACTOR |
| D-3 | decisions/strategic/lock-entries/D-03-closed-outside-open-inside.md | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md §Decision 3 | Closed для внешнего мира; open для команды/community (privileged access; не public open-source). | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-4 | decisions/strategic/lock-entries/D-04-name-jetix-locked.md | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md §Decision 4 | Jetix — name LOCKED (не Jackson). | MEDIUM | PROMOTE-AS-IS |
| D-5 | decisions/strategic/lock-entries/D-05-consulting-first-phase-1.md | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md §Decision 5 | Phase 1 = Consulting-first; Secure Network = Phase 2+ natural evolution. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-6 | decisions/strategic/lock-entries/D-06-anton-vladislav-rodion-not-key.md | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md §Decision 6 | Anton/Vladislav/Rodion — not key, removed. Advisory parked. | LOW | ARCHIVE / PROMOTE-AS-IS |
| D-7 | decisions/strategic/lock-entries/D-07-community-cast-11-archetypes.md | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md §Decision 7 | Union 11 archetypes (10 base + Блогеры Stage 3). | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-8 | decisions/strategic/lock-entries/D-08-layered-identity-multiplicity-frames.md | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md §Decision 8 | Layered identity per observer/phase grammar. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-9 | decisions/strategic/lock-entries/D-09-pain-primary-opportunity-secondary.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md §Decision 9 (T1) | Pain primary + Opportunity secondary outbound messaging. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-10 | decisions/strategic/lock-entries/D-10-english-us-first-germany-later.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md §Decision 10 (T2) | Phase 1 English+US first; Germany Phase 2+. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-11 | decisions/strategic/lock-entries/D-11-producer-center-investment-fund-philosophy.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md §Decision 11 (T3) | Phase 1 Consulting + Продюсерский центр + Investment-fund Day 1. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-12 | decisions/strategic/lock-entries/D-12-content-strategy-smart-audience-site-primary.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md §Decision 12 (T4) | Smart audience + site primary + соцсети max TOF. | **HIGH** (per brief §4 priority guidance) | PROMOTE-AS-IS / REFACTOR |
| D-13 | decisions/strategic/lock-entries/D-13-open-surface-closed-core.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md §Decision 13 (T5) | Open surface (results/frames/demos) / Closed core (промпты/wiki/workflows). | **HIGH** (Pillar A frontmatter referenced) | PROMOTE-AS-IS / REFACTOR |
| D-14 | decisions/strategic/lock-entries/D-14-research-revenue-instrumental-phase-1.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md §Decision 14 (T6) | Phase 1 research = revenue-instrumental only. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-15 | decisions/strategic/lock-entries/D-15-revenue-gated-spend.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md §Decision 15 (T7) | Revenue-gated spend (phased unlocks). | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-16 | decisions/strategic/lock-entries/D-16-community-phase-1-simple-chat.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md §Decision 16 (T8) | Phase 1 community = simple chat; formal mechanics Phase 2+/3+. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-17 | decisions/strategic/lock-entries/D-17-filesystem-source-of-truth.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md §Decision 17 (T9) | Filesystem = single source of truth; Notion = view. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-18 | decisions/strategic/lock-entries/D-18-productization-not-hours.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md §Decision 18 (T10) | Productization (templates/frameworks/subscription); not hours-billing. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-19 | decisions/strategic/lock-entries/D-19-holding-scale-1t-ambition.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md §Decision 19 | World-record speed для $1T market cap trajectory. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-20 | decisions/strategic/lock-entries/D-20-usb-c-positioning-enterprise-fast.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md §Decision 20 | USB-C positioning + enterprise-fast structure. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-21 | decisions/strategic/lock-entries/D-21-partnership-matchmaker-roy-replication.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md §Decision 21 | Partnership-matchmaker + roy-replication. | **HIGH** (Pillar A frontmatter D-21 Roy-Replication) | PROMOTE-AS-IS / REFACTOR / SPLIT |
| D-22 | decisions/strategic/lock-entries/D-22-icp-5-criteria-direction-of-life.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md §Decision 22 | ICP 5-criteria + direction-of-life axis. | **HIGH** (Pillar A frontmatter D-22 Korp-Startup) | PROMOTE-AS-IS / REFACTOR |
| D-23 | decisions/strategic/lock-entries/D-23-token-economy-phase-2-plus.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md §Decision 23 | Token economy Phase 2+; default Option B. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-24 | decisions/strategic/lock-entries/D-24-open-source-research-direction-phase-2-plus.md | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md §Decision 24 | Phase 2+ open-source research direction. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-25 | decisions/strategic/lock-entries/D-25-company-as-code.md | decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D25 | Company-as-Code Day 1. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-26 | decisions/strategic/lock-entries/D-26-team-50-100-enterprise.md | decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D26 | Team 50-100 Enterprise. | **HIGH** (Pillar A frontmatter D-26 single-accountable + Pillar C D-26) | PROMOTE-AS-IS / REFACTOR |
| D-27 | decisions/strategic/lock-entries/D-27-fork-and-merge-evolution.md | decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D27 | Fork-and-merge upstream-controller architecture. | **HIGH** (Pillar A frontmatter D-27 Fork-and-merge) | PROMOTE-AS-IS / REFACTOR |
| D-28 | decisions/strategic/lock-entries/D-28-query-driven-kb-filtering.md | decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28 | Pool-filling driven by anticipated queries. | MEDIUM | PROMOTE-AS-IS / REFACTOR |
| D-29 | decisions/strategic/lock-entries/D-29-korp-startup-self-narrative.md | decisions/LOCKS-D29-ADDENDUM-2026-04-26.md §D29 | Корпорация-стартап Day 1 — founder ответственен за сотни тысяч / миллионы. | **HIGH** (Pillar A frontmatter D-29 hybrid-framework) | PROMOTE-AS-IS / REFACTOR |

# §2 Strategic Insight scaffolds (4)

| Item | File path | Source path | 1-line summary | Priority | Migration options |
|---|---|---|---|---|---|
| I-jetix-ai-bios-moment | decisions/strategic/strategic-insights/jetix-ai-bios-moment.md | decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | Jetix as AI-era BIOS moment — рынок AI 2026 = рынок PC 1982; foundational thesis. | **HIGH** (per brief §4 — foundational thesis) | PROMOTE-AS-IS / REFACTOR / PROMOTE-TO-LOCK / PROMOTE-TO-DIRECTION-CARD |
| I-ai-psy-led-design | decisions/strategic/strategic-insights/ai-psy-led-design.md | decisions/STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md | AI Psy-Led Design Principle (DEFERRED Phase-2+; potential D-30 Lock candidate). | MEDIUM | PROMOTE-AS-IS / REFACTOR / DEFER |
| I-arbitrage-traffic-direction | decisions/strategic/strategic-insights/arbitrage-traffic-direction.md | decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md | Arbitrage Traffic как future Phase-2+ direction (DEFERRED). | MEDIUM | PROMOTE-AS-IS / DEFER |
| I-ma-direction | decisions/strategic/strategic-insights/ma-direction.md | decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md | M&A Advisory + ETA как Phase-2+ direction (DEFERRED). | MEDIUM | PROMOTE-AS-IS / DEFER |

# §3 Tier 2 ruslan_layer_overrides scaffolds (7)

| Item | File path | Source | Apparent intent | Priority | Migration options |
|---|---|---|---|---|---|
| P-S-01 | principles/tier-2-system/ruslan-layer-overrides/no-api-key-exposure.md | CLAUDE.md line 160 + line 187 (Global Rule 6) | NEVER expose API keys | LOW | PROMOTE-AS-IS |
| P-S-02 | principles/tier-2-system/ruslan-layer-overrides/filesystem-source-of-truth.md | CLAUDE.md line 159 + 185 + 249 + 107-108 (Global Rule 4 + D-17 derived) | Filesystem = source of truth; Notion = view | LOW | PROMOTE-AS-IS / MERGE-WITH-D-17 |
| P-S-03 | principles/tier-2-system/ruslan-layer-overrides/language-discipline.md | CLAUDE.md line 161 + 188 (Global Rule 7) | Russian for content; English for code/configs | LOW | PROMOTE-AS-IS |
| P-S-04 | principles/tier-2-system/ruslan-layer-overrides/ab-test-gating.md | CLAUDE.md line 162 + 191 (Global Rule 10) | A/B tests always awaiting_approval, never auto-deploy | LOW | PROMOTE-AS-IS |
| P-S-05 | principles/tier-2-system/ruslan-layer-overrides/path-protection.md | CLAUDE.md line 163 + 358 (Правила item 6) | Don't touch private/, ~/.ssh/, .env | LOW | PROMOTE-AS-IS |
| P-S-06 | principles/tier-2-system/ruslan-layer-overrides/voice-pipeline-draft-only.md | CLAUDE.md line 164 + 253 (CRM voice-integration) | Voice-pipeline DRAFT-only: never auto-overwrite prod records | LOW | PROMOTE-AS-IS / REFACTOR |
| P-S-07 | principles/tier-2-system/ruslan-layer-overrides/voice-pipeline-manual-review.md | CLAUDE.md line 326 (Voice-Notes Pipeline СТОП-gate) | Manual review gate before KB distribution | LOW | REFACTOR (not yet bullet-formatted in §4.2) |

# §4 Open question for Wave 1.4 entry

Ruslan disposition required on:

- **CLAUDE.md §4 status note** (`claude-md-section-4-status.md`) — Option A (replace populated §4 with placeholder per brief §3.6) или Option B (keep as-is, since Bundle 5 ack already populated). Default proposed B. See note for rationale.

# §5 Wave 1.4 entry checklist

For Ruslan-driven per-artefact review:

1. Open queue file (this document)
2. For each item, open the scaffold file + the source file side-by-side
3. Pick migration action (PROMOTE-AS-IS / REFACTOR / SPLIT / MERGE / ARCHIVE / etc)
4. For PROMOTE-AS-IS / REFACTOR: write final §1-§7 (Locks) / §0-§9 (Insights) / §1-§8 (overrides) content; update F:F4; ack via Part 6b stage_gate
5. For SPLIT: create N daughter scaffolds; delete or archive original
6. For ARCHIVE: mark scaffold archived; remove from Pillar A / Pillar C scope
7. Update `_decisions-db-index.jsonl` entry status from `pending-review` → `active` (or other terminal state)
8. Address §4 Open question (CLAUDE.md §4 disposition)

# §6 Provenance

- Wave 1 brief: `prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md` §4
- Wave 1 recon: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-1-scaffolding/recon.md`
- Pillar A architecture: `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` §H.3 + §I.5 + locked_decisions_referenced
