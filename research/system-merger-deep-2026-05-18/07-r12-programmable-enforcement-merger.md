---
type: research-phase-6
phase: 6
date: 2026-05-18 evening
session: system-merger-deep-research-2026-05-18
cells: eng × scalability + investor × roi-frame
constitutional_posture: R1 + R6 + R11 + EP-5
word_budget: 2500
F: F3
G: r12-programmable-enforcement-across-merger-boundary
R: refuted_if_3_components_not_mapped_OR_smart_contract_sketch_uncited_OR_failure_modes_<5
acked_parent_overlay: decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/03-r12-programmable.md (Option D Hybrid acked 2026-05-18)
---

# Phase 6 — R12 Programmable Enforcement Across Merger Boundary

> **Parent overlay (acked):** R12 programmable Option D Hybrid per `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md` ack commit `8a3d800`. Three mechanisms: Mondragón wage ratio cap + Quadratic Funding revenue distribution + Fork-and-leave exit tokens. This Phase 6 doc extends those mechanisms to merger boundary.

---

## §1 R12 reminder

**FUNDAMENTAL §6.1 candidate rule 12 (additive 2026-05-12):** "No extraction beyond agreed share —
AI / substrate cannot extract value from members beyond agreed share; members can fork-and-leave
without penalty." [src: decisions/RUSLAN-ACK-... LOCKED 2026-05-12; commit `93b796d`; cf. CLAUDE.md §4.1].

**Acked enforcement (Option D Hybrid):** programmable via Ethereum substrate; per-Clan opt-in via Charter; 4 RUSLAN-LAYER action classes added to `.claude/config/default-deny-table.yaml`: `extraction_beyond_share` / `wage_ratio_violation` / `non_consensual_distribution` / `fork_prevention_attempt`.

**Application to merger:** merger creates a **new bounded context** where R12 must be preserved across the boundary. Without programmable enforcement, merger = high-risk vector for R12 violation (incoming system imports extractive patterns; host system bends R12 to close deal).

---

## §2 Three R12 mechanisms × merger boundary

### §2.1 Mondragón wage ratio cap × merger

**Mondragón principle:** highest-paid member earns ≤ K × lowest-paid member (historically K=6:1 within cooperative; up to 9:1 federation-wide) [src: Mondragón Corporation governance docs:retrieved 2026; cross-ref research/deepening-2026-05-18/06-success-mondragon-68yr-mechanism.md].

**Merger-boundary application:**
- **Pre-merger:** each system has its own wage distribution (likely incompatible with K=6 — most enterprises K=20-100+).
- **Post-merger:** if K=6 is imposed system-wide → impossible without massive redistribution.
- **Compromise:** apply K-cap to **merger-affected roles only** (new joint roles, executive committee, project leads). Existing roles preserved at legacy ratios.
- **Trajectory:** declared K-cap goal (e.g., K=12 → K=10 → K=8 across 5y), monitored on-chain.

**Smart contract sketch:**

```solidity
// Solidity-like pseudocode — NOT production
contract MergerWageRatioCap {
    address public host;
    address public incoming;
    uint256 public K_cap;           // e.g., K_cap = 12 (initial)
    uint256 public K_target;        // e.g., K_target = 6 (long-term)
    uint256 public review_period;   // e.g., 365 days

    mapping(address => uint256) public mergerRoleCompensation;
    address public lowestPaidMergerRole;
    address public highestPaidMergerRole;

    function attestCompensation(address role, uint256 annualComp) external onlyAuthorized {
        require(annualComp <= mergerRoleCompensation[lowestPaidMergerRole] * K_cap,
                "WAGE_RATIO_VIOLATION");
        mergerRoleCompensation[role] = annualComp;
        emit CompensationAttested(role, annualComp);
    }

    function reviewAndAdjustKCap() external onlyGovernance {
        require(block.timestamp >= lastReview + review_period);
        if (K_cap > K_target) {
            K_cap = K_cap - 1; // gradual tightening
            emit KCapAdjusted(K_cap);
        }
        lastReview = block.timestamp;
    }

    function forkAndLeave() external {
        // delegated to ForkAndLeaveExit contract
    }
}
```

**Acceptance criteria:** quarterly attestation of merger-role compensation; on-chain monitor confirms K_cap; tightening on schedule.

**Failure mode:** wage data attestation lies (off-chain reality differs from on-chain claim) → audit hook + whistleblower protection essential.

### §2.2 Quadratic Funding (QF) revenue distribution × merger

**QF principle:** matching pool distributes proportional to √(sum of individual contributions), not raw contribution; small contributors disproportionately benefit [src: Buterin/Hitzig/Weyl 2018 "A Flexible Design for Funding Public Goods":retrieved 2026; Gitcoin Grants operational since 2019].

**Merger-boundary application:**
- **Synergy revenue** (revenue jointly generated post-merger that wouldn't exist without merger) distributed via QF logic among contributing parties / roles.
- **Matching pool:** funded by merger founders, external grants, or platform fee (Option B).
- **Contributors:** measured by audit trail of artefact contributions (commits, decisions, work-products attested under FPF F-G-R).

**Smart contract sketch:**

```solidity
contract MergerQFDistribution {
    address public mergerBoundary;
    uint256 public matchingPool;
    mapping(address => uint256) public contributorShares;
    mapping(address => uint256) public attestedContributions;

    function attestContribution(address contributor, uint256 amount, bytes32 evidence) external onlyFPFAuditor {
        // evidence = hash of provenance chain (F-G-R attested artefact)
        attestedContributions[contributor] += amount;
        emit ContributionAttested(contributor, amount, evidence);
    }

    function computeQFShares() external view returns (mapping(address => uint256)) {
        // sum_contributors sqrt(per_contribution_sum)^2 = QF formula
        // distribute matching pool proportionally to QF score
    }

    function distributeRevenue(uint256 revenue) external onlyAuthorized {
        // distribute per QF shares; emit DistributedQF(addresses, amounts)
    }
}
```

**Acceptance criteria:** every merger-affecting contribution attested with provenance evidence; QF distribution executed quarterly; audit trail public.

**Failure mode:** gaming via sybil contributions (one person creates many addresses each claiming small contribution → inflates QF score). Mitigation: proof-of-personhood layer (e.g., World ID / Idena / Gitcoin Passport).

### §2.3 Fork-and-leave exit tokens × merger

**Fork-and-leave principle (acked):** any party can exit substrate without penalty within agreed window; exit token issued at entry; non-revocable [src: H7 People-NS LOCKED 2026-05-12 commit `93b796d`].

**Merger-boundary application:**
- **Day-0 of merger:** both parties issued cryptographic exit tokens (e.g., soulbound NFT with `mergerId` + `partyId`).
- **Exit invocation:** holder presents token; smart contract executes pre-defined exit procedure (data extraction, artefact archive, mutual release).
- **Exit window:** initially indefinite (always exitable); later versions may include "lock-up" for committed periods, but only with affirmative consent.

**Smart contract sketch:**

```solidity
contract ForkAndLeaveExit {
    struct ExitToken {
        bytes32 mergerId;
        address party;
        uint256 issuedAt;
        bool exited;
    }
    mapping(bytes32 => ExitToken) public exitTokens;

    function issueExitToken(bytes32 mergerId, address party) external onlyMergerInitiator {
        bytes32 tokenId = keccak256(abi.encode(mergerId, party));
        exitTokens[tokenId] = ExitToken(mergerId, party, block.timestamp, false);
        emit ExitTokenIssued(mergerId, party, tokenId);
    }

    function invokeFork(bytes32 mergerId) external {
        bytes32 tokenId = keccak256(abi.encode(mergerId, msg.sender));
        ExitToken storage token = exitTokens[tokenId];
        require(!token.exited, "ALREADY_EXITED");
        token.exited = true;
        emit ForkInvoked(mergerId, msg.sender);
        // trigger off-chain exit ceremony (data archive, mutual release, etc.)
    }
}
```

**Acceptance criteria:** every merger party holds valid exit token; invocation = unconditional within agreed scope; no penalty clauses honored by smart contract.

**Failure mode:** off-chain coercion (party afraid to invoke for retaliation reasons even though on-chain enforceable). Mitigation: anonymous / pseudonymous invocation channel; whistleblower protection in agreement.

---

## §3 Cross-boundary enforcement architecture

```
                          ┌─────────────────────────┐
                          │  Merger Smart Contracts │
                          │  (Ethereum / L2)        │
                          │                         │
                          │  ┌───────────────────┐  │
                          │  │ Wage Ratio Cap    │  │
                          │  ├───────────────────┤  │
                          │  │ QF Distribution   │  │
                          │  ├───────────────────┤  │
                          │  │ Exit Tokens       │  │
                          │  └───────────────────┘  │
                          └───────────────┬─────────┘
                                          │
                ┌─────────────────────────┼─────────────────────────┐
                │                         │                         │
        ┌───────▼───────┐         ┌───────▼───────┐         ┌───────▼───────┐
        │ Audit Hooks   │         │ Provenance    │         │ Governance    │
        │ (event log,   │         │ Chain         │         │ Multi-sig     │
        │ Merkle-anchor)│         │ (F-G-R per    │         │ (host +       │
        │               │         │ claim)        │         │ incoming +    │
        │               │         │               │         │ FPF-Steward)  │
        └───────────────┘         └───────────────┘         └───────────────┘
```

**Data flow:**
1. **Operational events** (compensation attestations, contribution attestations, exit invocations) emitted on-chain.
2. **Audit hooks** record off-chain events; Merkle-roots anchored on-chain periodically.
3. **Provenance chain** records F-G-R per claim feeding into QF contribution attestation.
4. **Governance multi-sig** (host + incoming + FPF-Steward) controls parameter updates (K_cap target, matching pool top-up).

---

## §4 Off-chain audit complement

Smart contracts cannot enforce off-chain reality. Required complement:

| Off-chain audit area | Mechanism | Cadence |
|---|---|---|
| Compensation reality vs. on-chain attestation | Independent payroll review | Quarterly |
| Contribution reality (work delivered vs. claimed) | FPF-Steward + ROY swarm review | Per claim attestation |
| Sybil detection (QF distribution integrity) | Proof-of-personhood verification | Per contributor onboarding |
| Cultural / governance compliance (no coercion to not exit) | Anonymous whistleblower channel + annual culture audit | Annual |
| Smart contract security | Multi-firm audit pre-deployment + ongoing bug-bounty | Per release |

**Critical insight:** off-chain audit is **necessary** because smart contracts enforce **what they can observe** — but extraction often happens in domains smart contracts cannot observe (informal authority, social pressure, opportunity-cost manipulation).

---

## §5 Failure mode catalog

| FM-# | Failure mode | Cause | Detection | Mitigation |
|---|---|---|---|---|
| **FM-R1** | Smart contract bug enables silent extraction | Code defect | Independent audit + bug bounty; on-chain anomaly detection | Pause contract; patch; retroactive correction; insurance fund |
| **FM-R2** | Off-chain extraction undetected | Constraint applies on-chain only | Off-chain reality audit (§4) | Independent audit cadence; whistleblower bounty |
| **FM-R3** | Governance capture (multi-sig compromised) | Single point of failure in audit governance | Distributed multi-sig (k-of-n); rotating signers | k-of-n threshold; key rotation; transparency log |
| **FM-R4** | Mass fork-and-leave (system collapse) | Crisis of confidence; coordinated exit | Audit + early warning indicators | Crisis communication; FPF-Steward emergency review |
| **FM-R5** | Sybil-inflated QF distribution | Adversarial actor creates many addresses | Proof-of-personhood layer | Personhood verification; QF cap per claimed-person |
| **FM-R6** | Wage ratio attestation lies | Self-reported compensation inaccurate | Independent payroll audit | Random audit; legal disclosure obligations in merger contract |
| **FM-R7** | Exit token blocked off-chain | Social/legal coercion | Anonymous invocation; legal jurisdiction selection | Multi-jurisdiction escrow; arbitration in non-host court |
| **FM-R8** | Smart contract jurisdiction unenforceability | Crypto-legal mismatch | Pre-merger legal review | Off-chain agreement with on-chain reference; co-jurisdictional escrow |

---

## §6 Phase application (per first merger test case Phase 5)

| First merger phase | R12 enforcement activity |
|---|---|
| Phase 1 Discovery | Declare K_cap target; identify QF contributor classes; commit to exit-token issuance |
| Phase 2 Constraint negotiation | Deploy contracts to testnet; sign R12-acceptance ceremony; issue exit tokens |
| Phase 3 Bridge setup | Wire audit hooks to provenance chain; integrate F-G-R attestation with contribution recording |
| Phase 4 Pilot | Quarterly: compensation attestation; contribution attestation; audit review; QF distribution if synergy revenue generated |
| Phase 5 Decision | If SCALE: contracts migrate to mainnet; K_cap tightening schedule activated; if DE-MERGE: exit tokens invoked; final QF distribution; clean release |

---

## §7 Strategic Q × R12 enforcement

| | Option A (Outsource) | Option B (Platform) | Option C (Hybrid) |
|---|---|---|---|
| **Contract deployment** | Per-engagement; possibly off-chain audit only | Standardized; mandatory mainnet | Phase 1 testnet + audit; Phase 2 mainnet |
| **K_cap negotiation** | Per-merger custom | Standardized tiers (e.g., K=20 starter, K=10 advanced, K=6 cooperative) | Custom Phase 1; tiered Phase 2 |
| **QF matching pool size** | Per-engagement; small | Platform-funded; substantial | Phased |
| **Exit token enforceability** | Legal-jurisdiction-dependent | Standardized across platform | Phase 1 legal; Phase 2 cryptographic primary |
| **Audit cost burden** | Client | Platform / pooled | Split |
| **Sybil resistance** | Per-engagement; less critical | Platform-wide; high investment | Phase-gated investment |

---

## §8 Open questions for Ruslan ack

1. **Chain selection** — Ethereum mainnet, Polygon, Arbitrum, Base, or other L2 for first merger?
2. **K_cap initial value** — what ratio for first merger? (Recommend K=15 starter с trajectory to K=10 in 3 years.)
3. **QF matching pool source** — Jetix-funded, merger-parties-co-funded, or external grant (Optimism Retroactive Public Goods, Gitcoin)?
4. **Proof-of-personhood provider** — World ID, Gitcoin Passport, Idena, BrightID?
5. **Multi-sig signers** — host + incoming + Jetix-FPF-Steward + neutral 3rd party = 4-of-5?
6. **Off-chain audit firm** — preferred independent auditor? Big 4? Specialized crypto-audit firm (OpenZeppelin / Trail of Bits / Consensys Diligence)?
7. **Legal jurisdiction** — for off-chain agreements, recommend neutral common-law jurisdiction (e.g., Switzerland or Liechtenstein given EU+crypto-friendly)?

---

## §9 Cross-stream integration

- **Acked overlay parent:** `decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/03-r12-programmable.md` Option D Hybrid.
- **AWAITING-APPROVAL packet:** `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md` (acked 2026-05-18 commit `8a3d800`).
- **Mondragón 68y precedent:** `research/deepening-2026-05-18/06-success-mondragon-68yr-mechanism.md`.
- **Substrate matrix:** `research/deepening-2026-05-18/07-substrate-matrix-vc-sbt-pgp-coordinape.md` — exit tokens via SBT (Soulbound Tokens) per Buterin/Weyl 2022.
- **Phase 3 namordnik C1** = R12 anti-extraction constraint — this Phase 6 doc operationalises C1 enforcement.
- **Phase 4 §7 anti-pattern warning:** R12 dilution under cash flow pressure — Phase 6 contract enforcement makes dilution provably visible (on-chain).

---

## §10 Refutation conditions (Phase 6)

This Phase 6 doc = refuted_if:
- 3 R12 mechanisms (Mondragón wage ratio + QF + fork-and-leave) cannot all be implemented in merger context.
- Smart contract sketches contain provable logic errors (independent review).
- Off-chain audit complement (§4) is insufficient (auditor critique).
- Failure mode catalog (§5) missing critical class (e.g., MEV-related exploits not enumerated).

---

*Phase 6 brigadier-scribe. R6 provenance per claim. EP-5 F3 (acked overlay + Mondragón + QF + SBT triangulation). Next: Phase 7 hypothesis bank.*
