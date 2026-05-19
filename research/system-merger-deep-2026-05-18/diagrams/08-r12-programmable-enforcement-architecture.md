---
type: diagram
phase: 8
diagram_id: 08
title: R12 programmable enforcement architecture across merger boundary
parent_doc: 07-r12-programmable-enforcement-merger.md §3
---

# Diagram 08 — R12 Programmable Enforcement Architecture

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TB
    subgraph On_Chain["On-chain layer (Ethereum L2)"]
        WAGE[MergerWageRatioCap<br/>K_cap=15→K_target=6<br/>quarterly review]
        QF[MergerQFDistribution<br/>matching pool<br/>contribution attestation]
        EXIT[ForkAndLeaveExit<br/>soulbound NFT tokens<br/>non-revocable]
    end
    
    subgraph Off_Chain["Off-chain layer (audit complement)"]
        PAYROLL[Independent payroll audit<br/>quarterly]
        WORK[FPF-Steward work-audit<br/>per claim attestation]
        SYBIL[Proof-of-personhood<br/>World ID / Gitcoin Passport]
        CULTURE[Annual culture audit<br/>anonymous whistleblower]
        SEC[Smart contract security<br/>multi-firm audit + bug bounty]
    end
    
    subgraph Provenance["Provenance chain (F-G-R per claim)"]
        EVENT[Append-only event log]
        MERKLE[Merkle-root]
    end
    
    subgraph Governance["Governance layer"]
        MSIG[Multi-sig 4-of-5<br/>host + incoming + Jetix<br/>+ FPF-Steward + neutral]
    end
    
    PAYROLL -->|attest| WAGE
    WORK -->|attest contribution| QF
    SYBIL -->|verify person| QF
    
    WAGE -.->|emit event| EVENT
    QF -.->|emit event| EVENT
    EXIT -.->|emit event| EVENT
    
    EVENT --> MERKLE
    MERKLE -->|periodic anchor| On_Chain
    
    MSIG -->|control params| WAGE
    MSIG -->|control params| QF
    MSIG -->|control params| EXIT
    
    CULTURE -->|inform| MSIG
    SEC -->|inform| MSIG
    
    style WAGE fill:#fcc,stroke:#333,stroke-width:2px
    style QF fill:#cf9,stroke:#333,stroke-width:2px
    style EXIT fill:#ff9,stroke:#333,stroke-width:2px
    style MSIG fill:#9cf,stroke:#333,stroke-width:2px
```

## 3 R12 mechanisms (Phase 6 §2)

| Mechanism | On-chain enforcement | Off-chain complement | Failure mode mitigation |
|---|---|---|---|
| Mondragón wage ratio cap | K_cap monitor; tightening schedule | Quarterly payroll audit | Whistleblower bounty |
| QF revenue distribution | √(per-contribution) matching | Sybil verification + work audit | Cap-per-claimed-person |
| Fork-and-leave exit tokens | Soulbound NFT; unconditional invocation | Anonymous channel + multi-jurisdiction escrow | Arbitration clause |

## 8 failure modes (Phase 6 §5)

| FM | Failure mode | Mitigation |
|---|---|---|
| FM-R1 | Smart contract bug | Audit + bug bounty + pause+patch |
| FM-R2 | Off-chain extraction undetected | Independent audit cadence |
| FM-R3 | Governance capture | k-of-n multi-sig + key rotation |
| FM-R4 | Mass fork-and-leave (collapse) | Crisis comms + FPF-Steward emergency |
| FM-R5 | Sybil-inflated QF | Personhood verification + per-person cap |
| FM-R6 | Wage attestation lies | Random independent audit |
| FM-R7 | Exit token blocked off-chain | Anonymous channel + multi-jurisdiction |
| FM-R8 | Smart contract unenforceability | Off-chain agreement с on-chain reference |
