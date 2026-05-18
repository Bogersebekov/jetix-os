---
title: "Diagram 01 — Jetix-on-Ethereum 3-layer stack"
date: 2026-05-18
type: architecture-diagram
F: F3
G: jetix-ethereum-stack-diagram
parent: ../00-MASTER-ARCHITECTURE.md
---

# Diagram 01 — Jetix-on-Ethereum 3-layer stack

## §1 Full stack diagram

```mermaid
graph TB
  subgraph L1_Methodology ["LAYER 1 — Methodology (FPF + Foundation v1.0 LOCKED 2026-04-28)"]
    direction LR
    FPF[FPF Spec<br/>3758 lines<br/>F8 LOCKED]
    Found[Foundation 11 Parts<br/>+ Pillar A Strategic<br/>+ Pillar C Principles]
    R12[R12 anti-extraction<br/>Tier 2 rule 12<br/>substrate-agnostic]
    Roles[U.Role + U.RoleAssignment<br/>taxonomy abstract<br/>IP-1 preserved]
    FGR[F-G-R provenance<br/>schema]
  end

  subgraph L2_Execution ["LAYER 2 — Execution substrate (Ethereum L2 — Phase 2+ overlay)"]
    direction LR
    SBT[SBT Role-attestation<br/>EAS or EIP-5114<br/>ZK-extensible]
    DAO[DAO governance<br/>Aragon OSx<br/>Quadratic Voting]
    QF[QF Workshop revenue<br/>Buterin/Hitzig/Weyl 2018<br/>+ Mondragón 5:1 cap]
    SC_R12[R12 enforcement<br/>Smart contract<br/>RUSLAN-LAYER overlay]
    L2_Chain[L2 Rollup<br/>Base default<br/>Optimism fallback]
  end

  subgraph L3_Value ["LAYER 3 — Value flow (R12-aligned)"]
    direction LR
    Revenue[Revenue distribution<br/>Workshop client → DAO]
    Reputation[Reputation aggregation<br/>SBT graph per Soul]
    RoleAttest[Role-attestation portability<br/>cross-Clan + cross-L2]
    Fork[Fork-and-leave preserved<br/>RageQuit / SBT portable]
  end

  subgraph OffChain ["Off-chain substrate (Phase 1 baseline; Phase 2+ continues)"]
    PGP[PGP Web of Trust]
    WikiSig[Karpathy-wiki-signatures]
    VC[W3C VC v2.0<br/>Phase 2+]
    IPFS[IPFS for metadata]
  end

  FPF -->|encodes| SBT
  Found -->|encodes| DAO
  R12 -->|encodes| SC_R12
  R12 -->|encodes| QF
  Roles -->|encodes| SBT
  FGR -->|encodes| SBT

  SBT -->|implements| Reputation
  SBT -->|implements| RoleAttest
  DAO -->|implements| Revenue
  QF -->|implements| Revenue
  SC_R12 -->|implements| Revenue
  SC_R12 -->|implements| Fork

  L2_Chain -.runs.-> SBT
  L2_Chain -.runs.-> DAO
  L2_Chain -.runs.-> QF
  L2_Chain -.runs.-> SC_R12

  PGP -.complements.-> SBT
  WikiSig -.complements.-> SBT
  VC -.complements.-> SBT
  IPFS -.stores metadata.-> SBT
  IPFS -.stores metadata.-> DAO

  Revenue -->|validates| R12
  Fork -->|validates| R12
  Reputation -->|validates| FGR

  style L1_Methodology fill:#dbeafe,color:#1a202c
  style L2_Execution fill:#fef3c7,color:#1a202c
  style L3_Value fill:#bbf7d0,color:#1a202c
  style OffChain fill:#fce7f3,color:#1a202c
```

## §2 Reading guide

**3 horizontal layers + off-chain substrate:**

1. **Layer 1 (blue) — Methodology**: FPF + Foundation + Pillar C + Role taxonomy + F-G-R. **Substrate-agnostic principle preserved**. This layer is **canonical source-of-truth**.

2. **Layer 2 (yellow) — Execution**: Ethereum L2 rollup (Base default). SBT for role-attestation, DAO for governance, QF for Workshop revenue, smart contract for R12 enforcement. **RUSLAN-LAYER overlay** — specific bindings (contract addresses, L2 choice) live here.

3. **Layer 3 (green) — Value flow**: Revenue distribution, reputation aggregation, role-attestation portability, fork-and-leave. **All R12-aligned outcomes**.

4. **Off-chain substrate (pink) — Phase 1 baseline + Phase 2+ continuation**: PGP, Karpathy-wiki-sig, W3C VC v2.0, IPFS. **NOT replaced by Ethereum overlay** — complements.

## §3 Constitutional preservation visualization

- **Layer 1 → Layer 2**: «encodes» (arrow) — Foundation principles encoded INTO smart contracts; Foundation principle reigns
- **Layer 2 → Layer 3**: «implements» — Ethereum substrate implements value flow
- **Layer 3 → Layer 1**: «validates» — value flow outcomes validate Foundation principles (R12 satisfied, F-G-R provenance preserved)

If Layer 3 outcomes **violate** Layer 1 principles → Foundation principle wins (Layer 2 implementation revised).

## §4 Source

`../00-MASTER-ARCHITECTURE.md` §1 + §4 constitutional preservation
