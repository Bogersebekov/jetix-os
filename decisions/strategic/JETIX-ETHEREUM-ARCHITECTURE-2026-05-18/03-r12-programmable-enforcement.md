---
title: "03 — R12 anti-extraction programmable enforcement via smart contracts"
date: 2026-05-18
type: r12-programmable-enforcement
F: F2
G: r12-programmable-enforcement-ethereum
R: refuted_if_programmable_enforcement_violates_Pillar_C_Tier_2_substrate_agnostic_principle_OR_creates_new_extraction_vector
constitutional_posture: R1 + R2 (Pillar C touches → AWAITING-APPROVAL packet required) + R6 + EP-5
parent: 00-MASTER-ARCHITECTURE.md
mandatory_disclosures:
  - R2 LIVE-FLAG: Pillar C Tier 2 R12 substrate-agnostic foundation_generic is constitutional surface; programmable enforcement = RUSLAN-LAYER overlay candidate; AWAITING-APPROVAL packet required перед LOCK
---

# 03 — R12 anti-extraction programmable enforcement via smart contracts

> ⚠️ **R2 LIVE-FLAG.** This doc touches Pillar C Tier 2 R12 surface. **NO autonomous Pillar C amendment.** AWAITING-APPROVAL packet `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md` (Phase 4) — Ruslan ack required.

## §FPF primitives

| Decision | FPF primitive | F-G-R |
|---|---|---|
| R12 textual statement (Pillar C Tier 2 rule 12) | `U.Commitment` (A.2.8) + `E.5 Guard-Rails` | F8 (text, LOCKED 2026-05-12 ack) |
| R12 programmable enforcement | `E.5 Guard-Rails` (mechanism layer) + `A.6.1 U.Mechanism` (execution substrate) + `B.3 F-G-R` (provenance) | F2 · r12-programmable-candidate · surface only |
| Constitutional integrity | `A.7 Strict Distinction` (Foundation principle vs RUSLAN-LAYER overlay per IP-1) | F4 · ip-1-substrate-binding |

## §1 R12 textual rule (preserved)

**Tier 2 rule 12 (additive 2026-05-12):**
> «No extraction beyond agreed share — AI / substrate cannot extract value from members beyond agreed share; members can fork-and-leave without penalty.»

[src: `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` + CLAUDE.md §4.1 rule 12 + H7 People-NS LOCKED 2026-05-12 commit `93b796d`]

**Substrate-agnostic foundation_generic:** rule applies regardless of substrate (off-chain / on-chain / hybrid).

## §2 Programmable enforcement options

### §2.1 Option A — Revenue distribution smart contract (Mondragón 5:1 ratio)

**Mechanism:** Workshop revenue enters smart contract; distribution function enforces max compensation ratio (highest-paid / lowest-paid ≤ 5:1 per Mondragón empirical precedent).

**Pseudocode:**
```solidity
contract RevenueDistribution {
    uint256 constant MAX_RATIO = 5;  // Mondragón 5:1 cap
    mapping(address => uint256) public memberShares;
    address[] public members;
    
    function distribute(uint256 totalRevenue) external onlyDAO {
        uint256 minShare = type(uint256).max;
        uint256 maxShare = 0;
        
        for (uint i = 0; i < members.length; i++) {
            uint256 share = (totalRevenue * memberShares[members[i]]) / totalShares();
            if (share < minShare) minShare = share;
            if (share > maxShare) maxShare = share;
        }
        
        require(maxShare <= minShare * MAX_RATIO, "R12 violation: ratio exceeds 5:1");
        
        // ... transfer shares ...
    }
}
```

**R12 alignment:** **Yes** — programmatically enforces «no extraction beyond agreed share» at distribution time. **Cannot** override at contract level (immutable).

**Risk:** rigid 5:1 ratio may not fit all Clan contexts. **Mitigation:** ratio = DAO-configurable parameter (within bounds); or per-Clan deployment with own ratio.

### §2.2 Option B — Quadratic Funding for Workshop revenue (Tang+Weyl)

**Mechanism:** Workshop revenue split into matched pool + member contribution pool. QF mechanism (Buterin/Hitzig/Weyl 2018) distributes matched pool weighted by sqrt of contributions:
```
distribution_to_project_i = (Σ sqrt(contribution_j_to_i))² × matched_pool / Σ_all_i (Σ sqrt(...))²
```

**Effect:** small contributions weighted disproportionately; mitigates tyranny of large contributors; aligns with R12 (no single member can dominate value capture).

**Detail:** `06-quadratic-funding-workshop-revenue.md`.

**R12 alignment:** **Yes** — anti-concentration mechanism + transparent + auditable on-chain.

**Risk:** QF Sybil-attack surface (fake contributions); requires anti-Sybil via SBT-gated participation.

### §2.3 Option C — Fork-and-leave smart contract

**Mechanism:** Member exit function transfers proportional treasury share to departing member's wallet + revokes Clan-membership SBT but preserves Workshop-graduate SBT (role-attestation portable across Clans).

**Pseudocode:**
```solidity
contract ForkAndLeave {
    function exitClan(address member) external {
        require(msg.sender == member, "Self-exit only");
        
        uint256 proportionalShare = treasury * memberShares[member] / totalShares();
        // ... transfer proportionalShare to member ...
        
        clanMembershipSBT.burn(member);
        // workshopGraduateSBT remains — portable to other Clans
        
        emit MemberExited(member, proportionalShare);
    }
}
```

**R12 alignment:** **Yes** — fork-and-leave preserved + treasury share proportional + role-attestation portable.

**Risk:** «exit cascade» if many members exit simultaneously could drain treasury; **Mitigation:** time-delayed exit (e.g., 30-day notice) + circuit-breaker if exit > 50% in 30 days.

### §2.4 Option D — Hybrid (recommended)

Combine A + B + C with DAO-configurable parameters:
- A: Revenue distribution with Mondragón ratio cap
- B: QF for Workshop project-specific revenue
- C: Fork-and-leave preserved

**Brigadier inference (F2 surface):** Option D = most aligned with R12 full text + flexible per Clan / Phase. Surface only; Ruslan ack via AWAITING-APPROVAL packet.

## §3 Constitutional preservation analysis

### §3.1 Pillar C Tier 2 substrate-agnostic foundation_generic intact

**Critical:** R12 text Tier 2 rule **does not mention** substrate. Rule applies regardless of:
- Off-chain text-only enforcement (Phase 1 baseline)
- W3C VC v2.0 attestations (Phase 2)
- Ethereum smart-contract enforcement (Phase 2+ RUSLAN-LAYER overlay)

Programmable enforcement = **specific RUSLAN-LAYER implementation choice**; Foundation principle = substrate-agnostic. **No Tier 2 amendment required.**

### §3.2 RUSLAN-LAYER overlay candidate (AWAITING-APPROVAL gate)

**What requires Ruslan ack:**
1. Introduction of RUSLAN-LAYER overlay binding R12 enforcement to specific Ethereum smart-contract patterns
2. Phase 2+ Clan opting into programmable enforcement (each Clan decides per Charter)
3. Default-Deny table addition for «R12 smart-contract deployment» action class

**What does NOT require Tier 2 amendment:**
- R12 text itself (already LOCKED 2026-05-12 + ack)
- Substrate-agnostic principle (preserved)
- IP-1 distinction (preserved — overlay separated from Foundation)

**AWAITING-APPROVAL packet contents (Phase 4 deliverable):**
- Surface R12 programmable enforcement Option A/B/C/D as RUSLAN-LAYER overlay candidates
- Confirm no Tier 2 text modification
- Surface Default-Deny table addition needs (novel action classes)
- Surface fork-and-leave preservation tests (DRA-T4 from CONCEPT-MAN-AS-ARMY §6.3)

## §4 New extraction vector risks (paradox check)

**Question:** Does programmable enforcement via Ethereum substrate introduce NEW extraction vectors not present in text-only enforcement?

**Vector 1 — Smart contract bugs/exploits.** Yes — possible code-vector extraction (e.g., reentrancy attack draining treasury).
- **Mitigation:** OpenZeppelin standard libraries + external audit (Trail of Bits, ConsenSys Diligence) + bug bounty program + gradual rollout.

**Vector 2 — Owner/admin keys controlling upgradeable contracts.** Yes — if Diamond Proxy upgrade keys held by single party, that party = extraction risk.
- **Mitigation:** Multi-sig governance for upgrades (≥3-of-5 DAO delegates); time-locked upgrades (7-day delay); immutable contracts for critical R12 enforcement (revenue distribution).

**Vector 3 — Oracle manipulation.** If revenue distribution depends on price oracles, oracle manipulation = extraction vector.
- **Mitigation:** Off-chain price feeds avoided; on-chain Chainlink oracles only for non-revenue-critical functions.

**Vector 4 — Gas-cost extraction.** Workshop participants paying L2 gas (~$0.01-0.10) = small but real cost not present in pure off-chain.
- **Mitigation:** DAO treasury subsidizes gas via account abstraction (ERC-4337) sponsor; or L2 with near-zero gas (zkSync Era / StarkNet).

**Vector 5 — MEV (Maximal Extractable Value) by validators.** L2 sequencer could front-run / sandwich Workshop transactions.
- **Mitigation:** L2 selection considers MEV protection (Optimism + Arbitrum have decentralization roadmaps; Base operated by Coinbase = trust-mediated).

**Conclusion:** Programmable enforcement adds new vectors but **all mitigatable** via standard practices. Net effect = stronger R12 enforcement than text-only (verifiable execution + immutable rules > human-trust-based enforcement).

## §5 Plain English

**Что такое «R12 programmable enforcement»?**

Простыми словами:
- **R12 текстом** (сейчас): «AI и substrate не могут extract value beyond agreed share». Это правило в Foundation, но enforcement = через human review + trust.
- **R12 programmable** (опция Phase 2+): то же правило, но **встроено в smart contract** на Ethereum. Smart contract физически не может распределить revenue нарушая правило.

Аналогия:
- **Текстом** = «правило не превышать скорость 50 км/ч на жилой улице» — рассчитываем на адекватность водителя
- **Programmable** = «электронный ограничитель скорости в машине, который физически не даёт превысить 50 км/ч»

Programmable enforcement **сильнее** чем text-only:
- Меньше зависит от human trust
- Auditable on-chain (transparent execution)
- Immutable (no one can override post-deployment)

Но programmable enforcement **вводит новые риски**:
- Smart contract bugs
- Upgradeability concentration
- Gas costs
- MEV

Всё это **mitigatable** через стандартные практики (audits, multi-sig, gas subsidies, MEV-resistant L2).

**Сохраняется ли substrate-agnostic principle?**

**ДА.** R12 text Foundation = «substrate-agnostic». Programmable enforcement = **выбор Ruslan'а** на Phase 2+ implement R12 через Ethereum smart contracts. Тут нет противоречия — Foundation описывает **что должно произойти**; programmable enforcement = **один из способов реализации**.

Другие способы реализации:
- Phase 1: Off-chain accounting + Ruslan trust + Karpathy-wiki-sig
- Phase 2: + W3C VC v2.0 audit trail
- Phase 2+: + Ethereum smart contracts

Все три approach **enforce R12** в разных способах + могут coexist.

## §6 AWAITING-APPROVAL packet content surface (Phase 4 deliverable)

**Packet:** `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md`

**Packet sections (preview):**
1. Architectural context (this doc summary)
2. R12 Tier 2 text preservation (no amendment)
3. RUSLAN-LAYER overlay introduction proposal
4. Default-Deny table additions (3-5 novel action classes)
5. Constitutional preservation analysis (§3 from this doc)
6. New extraction vector mitigations (§4)
7. Phase 2+ rollout sequencing
8. Fork-and-leave preservation tests (DRA-T4)
9. Ruslan ack matrix (what is requested ack)

## §7 Open questions

| OQ | Question |
|---|---|
| **OQ-03-1** | Mondragón 5:1 ratio — fixed parameter or DAO-configurable? |
| **OQ-03-2** | QF matching pool source — Workshop revenue % / external grants / native token mint? |
| **OQ-03-3** | Exit notice period — 30 days / 90 days / Charter-configurable? |
| **OQ-03-4** | Immutable vs upgradeable revenue contracts — immutable safer but no bug-fix path |
| **OQ-03-5** | Per-Clan deployment vs shared infrastructure — independence vs reuse trade-off |

## §8 Counter-positions

- **Counter 1 (phil critic):** «Programmable enforcement reduces human-judgment role; some R12 violations require context-sensitive evaluation impossible in code.» Mitigation: programmable enforcement ≠ exclusive enforcement; human-review escalation path preserved for context-edge-cases via DAO governance proposal.
- **Counter 2 (sys integrator):** «Adding programmable enforcement layer increases system complexity → more failure modes.» Mitigation: layered approach (text-only Phase 1; VC v2.0 Phase 2; programmable Phase 2+) — complexity introduced incrementally with empirical validation.
- **Counter 3 (investor scalability):** «Smart-contract development + audit cost ~$50-200K — capital not available pre-revenue.» Mitigation: Phase 2+ timing assumes Workshop revenue established; bootstrap can use existing open-source contracts (Aragon OSx + OpenZeppelin) without major audit cost.
- **Counter 4 (eng critic):** «Once deployed, immutable contracts cannot evolve with R12 understanding refinement. Future Pillar C evolution becomes harder.» Mitigation: upgradeable governance contracts (Diamond Proxy with multi-sig delay) for non-financial-critical functions; immutable only for revenue distribution.

## §9 Sources

- Pillar C Tier 2 R12: `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md`
- CLAUDE.md §4.1 rule 12
- Mondragón 5:1 ratio: `research/deepening-2026-05-18/06-success-mondragon-68yr-mechanism.md`
- Quadratic Funding (Buterin/Hitzig/Weyl 2018): arxiv.org/abs/1809.06421
- Coordinape epoch peer-reward: docs.coordinape.com
- OpenZeppelin AccessControl + Pausable: docs.openzeppelin.com
- Diamond Proxy EIP-2535
- Account Abstraction ERC-4337

**Word count:** ~1830.
