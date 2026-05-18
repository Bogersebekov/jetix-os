---
title: "R12 programmable enforcement (RUSLAN-LAYER overlay Option D Hybrid)"
type: concept
niche: tech
sources:
  - swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md
  - swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md
  - decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/03-r12-programmable-enforcement.md
  - decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/diagrams/05-smart-contract-r12-enforcement.md
  - research/deepening-2026-05-18/06-success-mondragon-68yr-mechanism.md
  - research/deepening-2026-05-18/11-people-tang-weyl-plurality-2024.md
related:
  - concepts/jetix-on-ethereum.md
  - concepts/trust-infrastructure-positive-signaling.md
  - concepts/man-as-army-jetix.md
  - concepts/pitch-pattern-power-rangers.md
tags: [#type/concept, #topic/r12, #topic/anti-extraction, #topic/programmable-enforcement, #topic/smart-contract, #status/acked]
topics: [system-design, octagon-h8, pillar-c, ruslan-layer]
created: 2026-05-18
updated: 2026-05-18
confidence: medium (F3 acked; Option D Hybrid acked but не yet deployed)
pipeline: ingested
status: ruslan-acked-option-d-hybrid-2026-05-18 (commit 8a3d800)
F: F3
G: r12-programmable-enforcement-ruslan-layer-overlay
R: refuted_if_Tier_2_R12_text_modified_OR_substrate_agnostic_principle_violated_OR_new_extraction_vector_unmitigated_in_deployment
parent_packet: swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md
ack_trail:
  - timestamp: 2026-05-18 evening Berlin
  - decision: Option D Hybrid (Mondragón ratios + QF revenue + fork-and-leave smart contracts)
  - commit: 8a3d800
---

# R12 programmable enforcement (RUSLAN-LAYER overlay Option D Hybrid)

## Суть в одной строке

R12 anti-extraction principle (Pillar C Tier 2 rule 12 LOCKED 2026-05-12) implemented via Ethereum smart contracts с Mondragón ratio cap + Quadratic Funding revenue distribution + fork-and-leave exit tokens; RUSLAN-LAYER overlay preserving substrate-agnostic foundation_generic principle.

## Определение

R12 (Pillar C Tier 2 rule 12):
> «AI / substrate cannot extract value from members beyond agreed share; members can fork-and-leave without penalty.»

**Programmable enforcement (acked 2026-05-18 Option D Hybrid)** = smart-contract implementation of R12 на Ethereum L2 substrate, combining 3 mechanisms:

1. **Mondragón ratio cap** — revenue distribution smart contract enforces max-share/min-share ≤ configured ratio (5:1 default per direction 06 empirical 68yr precedent)
2. **Quadratic Funding** — Workshop revenue distributed по QF formula (Buterin/Hitzig/Weyl 2018; Tang+Weyl Plurality 2024) с anti-concentration property
3. **Fork-and-leave smart contract** — RageQuit-style member exit с proportional treasury share preserved; Workshop-graduate SBT remains portable

## Ключевые свойства

### Constitutional preservation (critical)

- **Tier 2 R12 text** = LOCKED 2026-05-12 = **UNCHANGED** (no amendment proposed)
- **foundation_generic count** = **12 UNCHANGED** (sync_invariant_count preserved)
- **Substrate-agnostic foundation_generic principle** = **PRESERVED** (programmable enforcement = specific RUSLAN-LAYER overlay; rule remains substrate-agnostic)
- **IP-1 Role≠Executor** = preserved (Ethereum smart-contract addresses live в RUSLAN-LAYER overlay; Foundation Parts unchanged)
- **Per-Clan opt-in** = each Clan decides per Charter whether to adopt overlay (not forced)

### Programmable enforcement properties

- **Verifiable execution** > human-trust-based enforcement
- **Auditable on-chain** (transparent + immutable post-deployment)
- **Anti-concentration mathematical property** (QF sqrt formula)
- **Bounded distribution** (Mondragón ratio cap; redistribute excess if violated)
- **Fork-and-leave preserved** (exit transfers proportional treasury share; SBT portability)

### Anti-Sybil layer (within QF)

- SBT-gated participation (only Clan-membership SBT holders can signal)
- Peer attestation required (signals require ≥1 co-sign from established Soul)
- F-G-R reliability weight (new Souls weight × 0.5; established × 1.0)
- Stake bond (signaler posts small SBT-bond; lost if peer-reviewed as Sybil)

## Применимость

**Когда применимо:**
- Phase 2+ Clan opt-in (after audit + deployment)
- Workshop revenue events with multi-contributor distribution
- Multi-Clan Federation governance treasury distribution
- Fork-and-leave events (member exit с proportional share)

**Когда НЕ применимо:**
- Phase 1 (off-chain text-only baseline still primary)
- Clans choosing NOT to opt-in (per Charter)
- Russian-jurisdiction-only members (off-chain alternative preserved)
- Substrate-agnostic principle abandonment (foundation_generic intact)

## Falsifier conditions

- If Tier 2 R12 text modified (substrate change required) → concept refuted
- If substrate-agnostic foundation_generic principle violated → concept refuted
- If new extraction vector materializes in deployment (smart-contract bug / oracle manipulation / etc.) → mitigation cycle invoked
- If fork-and-leave clause exercised + retaliation observed → concept failed; revert к text-only
- If per-Clan opt-in becomes effectively-required (de facto lock-in) → R12 violation; revert

## Cross-domain precedents

| Precedent | Period | Pattern match |
|---|---|---|
| **Mondragón** (direction 06) | 68 years | 5:1 wage ratio cap; cooperative resilience; voluntary participation |
| **Tang+Weyl Plurality** (direction 11) | 2024+ | Quadratic Voting / Funding production-proven (Gitcoin Grants 15+ rounds, ~$50M distributed) |
| **Coordinape** (direction 07 §2.5) | 2021+ | Epoch peer-reward pattern (referenced, not directly used) |
| **MolochDAO RageQuit** | 2019+ | RageQuit fork-and-leave pattern; proportional share preservation |

## 4 RUSLAN-LAYER action classes (Default-Deny table additions)

Per `.claude/config/default-deny-table.yaml` ruslan_layer_action_classes section (added 2026-05-18):

1. **extraction_beyond_share** — Agent / DAO / smart contract attempts extraction beyond Charter-agreed share OR ratio cap → halt_log_alert
2. **wage_ratio_violation** — Distribution produces ratio > configured cap → redistribute proportionally OR halt
3. **non_consensual_distribution** — Distribution executed без DAO quorum + Charter authorization + contributor signaling → halt
4. **fork_prevention_attempt** — Smart contract / DAO / actor attempts to penalize OR prevent member exit → halt_log_alert

All map к parent Tier 2 rule `ai_extract_value_beyond_agreed_share` (preserved substrate-agnostic).

## Implementation roadmap

Per `decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/11-phase-2-implementation-checklist.md`:

- **M2P-2 smart contract development:** `JetixRevenueDistribution.sol` (QF + Mondragón cap) + `JetixForkAndLeave.sol` (RageQuit-style)
- **External audit required** ($50-200K budget; Trail of Bits / ConsenSys Diligence / OpenZeppelin Audits)
- **M2P-3 pilot deployment** single Clan с €500-1000 test event
- **M2P-4 mainnet deployment** first real Workshop revenue event
- **Per-Clan opt-in** via Charter v0+1 addendum

## Связи

- **Parent constitutional:** Pillar C Tier 2 rule 12 (R12 anti-extraction LOCKED 2026-05-12)
- **Bridge:** [[concepts/jetix-on-ethereum.md]] — execution substrate enabling programmable enforcement
- **Связано:** [[concepts/trust-infrastructure-positive-signaling.md]] — H8 trust mechanism complementary positive face к R12 negative face
- **Связано:** [[concepts/man-as-army-jetix.md]] — distributed resilience requires R12 (anti-extraction is composition glue)
- **Cross-domain precedents:** Mondragón direction 06 + Tang+Weyl Plurality direction 11 + MolochDAO RageQuit
- **Контрастирует с:** Text-only enforcement (human trust-based; weaker); Friend.tech financialization (NO native fungible token here; SBT-only attestation); Traditional corporate equity structures (R12 caps maximum extraction)

## Provenance

[src: Pillar C Tier 2 rule 12 LOCKED 2026-05-12 via `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` Q2 ack commit `93b796d`]
[src: Programmable enforcement Option D Hybrid acked 2026-05-18 evening via `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md` commit 8a3d800]
[src: Phase 3 architecture detail `decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/03-r12-programmable-enforcement.md`]
[src: Mermaid state diagram `decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/diagrams/05-smart-contract-r12-enforcement.md`]
[src: Mondragón 5:1 ratio empirical precedent `research/deepening-2026-05-18/06-success-mondragon-68yr-mechanism.md`]
[src: QF Buterin/Hitzig/Weyl 2018 + Tang+Weyl Plurality 2024 `research/deepening-2026-05-18/11-people-tang-weyl-plurality-2024.md`]

## Open questions

| OQ | Question |
|---|---|
| OQ-R12-PE-1 | Mondragón ratio cap parameter — 3:1 / 5:1 / 9:1 / DAO-configurable? |
| OQ-R12-PE-2 | Per-Clan opt-in mechanism — Charter addendum format? |
| OQ-R12-PE-3 | Exit notice period — 30 days / 90 days / Charter-configurable? |
| OQ-R12-PE-4 | QF matching pool funding source — % of revenue / external grants / DAO mint? |
| OQ-R12-PE-5 | Immutable revenue contracts vs upgradeable governance contracts — trade-off resolution? |
| OQ-R12-PE-6 | Per-Clan deployment vs shared infrastructure — independence vs reuse? |

## Key implication: distinctive feature vs competitors

Per Ruslan ack rationale (packet ack_trail):
> «Distinctive feature vs competitors (no other crypto project does programmable R12).»

This positions Jetix Phase 2+ as **unique substrate** в crypto ecosystem — most DAOs implement governance + revenue distribution **without** programmatic anti-extraction enforcement. Jetix R12 programmable = **competitive moat** + **attractor для Tang+Weyl camp + d/acc community**.

---

*Brigadier-promoted Tier A 2026-05-18 post-ack (commit 8a3d800). R1 surface (Ruslan acked Option D Hybrid; brigadier transcribes) + R6 provenance + EP-5 + append-only. Wiki concept page для R12 programmable enforcement RUSLAN-LAYER overlay.*
