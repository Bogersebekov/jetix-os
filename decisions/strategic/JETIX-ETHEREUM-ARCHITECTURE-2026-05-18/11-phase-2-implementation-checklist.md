---
title: "11 — Phase 2+ Implementation Checklist (post-ack concrete steps)"
date: 2026-05-18
type: implementation-checklist-post-ack
F: F3
G: jetix-ethereum-phase-2-implementation-checklist
R: refuted_if_sequencing_violates_constitutional_posture_OR_R12_enforcement_breaks_in_pilot
constitutional_posture: R1 surface (Ruslan ack reasserted per step) + R6 + EP-5
parent: 00-MASTER-ARCHITECTURE.md
ack_trail:
  - timestamp: 2026-05-18 evening Berlin
  - decisions_referenced: H8 Option A + R12 Option D Hybrid
  - commit: 8a3d800
language: russian + english
---

# 11 — Phase 2+ Implementation Checklist (post-ack concrete steps)

> **Post-ack baseline.** H8 Option A + R12 Option D Hybrid acked 2026-05-18. This checklist concretizes implementation roadmap §09 §3-§5 Phase 2+ deployment.

> **R1 reminder:** each step requires Ruslan re-ack at execution time (this checklist = surface; ack = per-step at execution).

---

## §0 TL;DR

Phase 2+ Ethereum overlay implementation = unblocked at decision-checkpoint level. 6 sequenced milestones (M2P-1 → M2P-6), each with concrete deliverables + dependencies + Ruslan-ack-required actions + risk gates. Timeline aspirational Q2 2027 → Q4 2027.

---

## §1 Sequenced milestones

### M2P-1 — L2 + DAO framework commit (gate: Ruslan ack)

**Pre-conditions:**
- ✅ H8 Option A acked
- ✅ R12 Option D Hybrid acked
- ⏳ Phase 2 milestones stable ≥6 months (per `09-implementation-roadmap.md` §3 gating)
- ⏳ Crypto-tribe perception study acceptable (Phase 2 deliverable P2-D4)
- ⏳ Legal advisor consult complete

**Deliverables:**
- L2 selection commit (default surface: Base; alternatives: Optimism / multi-L2)
- DAO framework commit (default surface: Aragon OSx; alternative: Moloch v3)
- Per-Clan opt-in mechanism specified в Charter v0+1 (`decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md` addendum)

**Ruslan-ack actions:**
- L2 selection ack (commit ETH-overlay surface as production substrate)
- DAO framework ack
- Charter v0+1 update with «Phase 2+ overlay opt-in» clause

**Risk gate:**
- Crypto-tribe perception negative? → defer M2P-2; revisit Phase 3
- Legal blocker (jurisdiction)? → switch jurisdiction OR defer

### M2P-2 — Smart contract development + audit (gate: budget + audit)

**Pre-conditions:**
- M2P-1 acked
- Audit budget secured ($50-200K per `10-risks-mitigations.md` §7)
- Audit firm engaged (Trail of Bits / ConsenSys Diligence / OpenZeppelin Audits)

**Deliverables (smart contracts):**
- `JetixClanMembershipSBT.sol` — Clan-membership SBT (revokable on exit)
- `JetixWorkshopGraduateSBT.sol` — Workshop-graduate SBT (permanent + portable)
- `JetixRoleAttestationRegistry.sol` — F-G-R-provenance role attestations
- `JetixRevenueDistribution.sol` — QF formula + Mondragón 5:1 cap (R12 Option D Hybrid)
- `JetixForkAndLeave.sol` — RageQuit-style exit (R12 Option D Hybrid)
- `JetixDAOFactory.sol` — Aragon OSx wrapper + Clan-specific deployment

**Off-chain integrations:**
- IPFS pinning service для metadata (Pinata / Infura / self-hosted)
- The Graph subgraph indexer для Evidence Graph A.10 query
- Account Abstraction (ERC-4337) bundler для gas sponsorship (optional Phase 2+ pilot)

**Ruslan-ack actions:**
- Audit firm selection ack
- Audit budget release ack
- Final smart contract specs ack (per-contract per-spec line review)

**Risk gate:**
- Audit reveals critical bugs? → fix → re-audit (cost overrun risk)
- Spec ambiguity unresolved (e.g., Mondragón ratio param)? → DAO-configurable parameter with bounds

### M2P-3 — Pilot deployment (single Clan, limited treasury)

**Pre-conditions:**
- M2P-2 audit complete + passed
- Single Clan opted-in via Charter addendum
- Bug bounty program live (Immunefi / similar)

**Deliverables:**
- Deploy contracts on Base testnet (Sepolia)
- Workshop graduate SBT pilot (first 1-3 graduates)
- DAO governance pilot (first Clan-internal vote on minor decision)
- Revenue distribution pilot (€500-1000 test event с 3-5 contributors)
- Fork-and-leave exit pilot (1 simulated exit; verify treasury share transfer)

**Ruslan-ack actions:**
- Each pilot event ack-gated (limited blast radius initially)
- Move-to-mainnet ack post-testnet stable

**Risk gate:**
- Pilot exposes unfixable bug → revert; redesign
- Gas costs Higher than expected → ERC-4337 sponsorship OR L2 reconsider
- Member experience friction → UX iteration

### M2P-4 — Mainnet deployment + first real Workshop revenue event

**Pre-conditions:**
- M2P-3 testnet stable ≥4 weeks
- Mainnet bug bounty active
- Legal-DAO bridge operational (per `08-legal-entity-dao-interaction.md` Pattern C hybrid)

**Deliverables:**
- Deploy contracts on Base mainnet
- First real Workshop revenue event executed via smart contracts
- First SBT issuances post-mainnet
- First DAO vote post-mainnet

**Ruslan-ack actions:**
- Mainnet deployment ack (multi-sig 3-of-5)
- First revenue event ack
- Public announcement ack (timing + framing per crypto-tribe perception mitigation)

**Risk gate:**
- Mainnet exploit → Halt-Log-Alert; pause; investigation
- Treasury extraction attempt → R12 enforcement contract halts

### M2P-5 — Multi-Clan Federation introduction (Phase 3 transition)

**Pre-conditions:**
- M2P-4 stable ≥6 months
- ≥3 Clans onboarded
- Cross-L2 bridge tests successful (DRA-T4 from CONCEPT-MAN-AS-ARMY §6.3)

**Deliverables:**
- Federation DAO deployed (per `05-dao-governance-multi-clan.md` §2.2)
- Cross-Clan SBT recognition policy ack'd via Federation vote
- Federation treasury (shared infrastructure costs)

**Ruslan-ack actions:**
- Federation DAO contract deployment ack
- Federation governance scope ack (cross-Clan disputes + shared infra; NOT internal Clan affairs)

### M2P-6 — Constitutional preservation continuous audit

**Continuous (parallel к all milestones):**

| Audit dimension | Frequency | Trigger |
|---|---|---|
| Foundation principle preservation | Continuous (lint) | Foundation Part change attempt |
| R12 enforcement integrity | Per distribution event | Smart contract execution |
| IP-1 Role≠Executor | Continuous | Any address-naming attempt в Foundation Parts |
| Halt-Log-Alert correctness | Per emit event | Constitutional violation detection |
| Default-Deny table sync | Daily lint | constitutional_never_list / RUSLAN-LAYER changes |
| Pillar C Tier 2 text preservation | Quarterly review | Pillar C evolution loop B.4 |

**Ruslan-ack actions:**
- Quarterly Pillar C review ack
- Any HALT-Log-Alert escalation review

---

## §2 Resource estimate

| Phase | Cost estimate | Note |
|---|---|---|
| M2P-1 | €5-10K | L2 + DAO framework legal/technical review |
| M2P-2 | €50-200K | Smart contract development + external audit |
| M2P-3 | €5-20K | Pilot deployment + testnet gas + UX iteration |
| M2P-4 | €5-15K | Mainnet deployment + initial gas sponsorship |
| M2P-5 | €20-50K | Federation DAO + Phase 3 transition |
| M2P-6 | Continuous | Audit + lint + review |

**Total Phase 2+ aspirational budget:** ~€85-295K over 2-3 quarters.

**Funding assumption:** Phase 2 Workshop revenue established (~€50K+) + external grants (Optimism RetroPGF / Gitcoin Grants / Ethereum Foundation Public Goods).

---

## §3 Constitutional checkpoints (per milestone)

Each milestone passes through:

1. **AWAITING-APPROVAL packet** (if Foundation / Pillar C touches)
2. **Ruslan ack** (recorded в commit message + packet frontmatter)
3. **Default-Deny table check** (RUSLAN-LAYER action class permits action)
4. **F-G-R provenance trace** (claim provenance recorded)
5. **Halt-Log-Alert monitoring** (constitutional violations detection live)

---

## §4 Cross-refs

- `00-MASTER-ARCHITECTURE.md` §12 ack-trail
- `09-implementation-roadmap.md` (high-level Phase 1/2/2+/3 sequencing)
- `12-buterin-outreach-materials-draft.md` (companion outreach doc)
- AWAITING-APPROVAL packets (both acked):
  - `swarm/awaiting-approval/h8-ethereum-substrate-extension-2026-05-18.md`
  - `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md`
- Default-Deny table: `.claude/config/default-deny-table.yaml`
- CONCEPT-MAN-AS-ARMY §7.1 progression model

---

## §5 Open questions (per-milestone open)

| OQ | Question | Milestone |
|---|---|---|
| OQ-11-1 | L2 selection final commit — Base / Optimism / multi-L2? | M2P-1 |
| OQ-11-2 | DAO framework commit — Aragon OSx / Moloch v3 / hybrid? | M2P-1 |
| OQ-11-3 | Mondragón ratio cap parameter — 3:1 / 5:1 / 9:1 / DAO-configurable? | M2P-2 |
| OQ-11-4 | Audit firm selection — Trail of Bits / ConsenSys / OpenZeppelin? | M2P-2 |
| OQ-11-5 | First-Clan pilot Charter — same v0 or v0+1 addendum? | M2P-3 |
| OQ-11-6 | Gas sponsorship policy (ERC-4337) — onboarding-only / continuous? | M2P-3 |
| OQ-11-7 | Public announcement timing — pre-mainnet / post-stable / Phase 3? | M2P-4 |
| OQ-11-8 | Federation governance scope final — disputes-only / shared-infra / both? | M2P-5 |

---

**Word count:** ~1500.

*Brigadier-scribed post-ack 2026-05-18 per Ruslan ack commit 8a3d800. R1 surface (per-step Ruslan ack required at execution) + R6 + EP-5 + append-only.*
