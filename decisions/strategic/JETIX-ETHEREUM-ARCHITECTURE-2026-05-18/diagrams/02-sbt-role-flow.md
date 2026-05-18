---
title: "Diagram 02 — SBT role-attestation lifecycle flow"
date: 2026-05-18
type: architecture-diagram
F: F3
G: jetix-sbt-role-flow-diagram
parent: ../00-MASTER-ARCHITECTURE.md
---

# Diagram 02 — SBT role-attestation lifecycle flow

## §1 Full lifecycle sequence

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
sequenceDiagram
  participant Soul as Member Soul<br/>(non-custodial wallet)
  participant Issuer as Issuer Soul<br/>(Workshop / Clan / DAO)
  participant Chain as Ethereum L2<br/>(Base default)
  participant IPFS as IPFS metadata
  participant Verifier as External Verifier<br/>(employer / partner / Clan)
  participant FoundationDocs as Foundation Spec<br/>(Layer 1 canonical)
  
  Note over Soul, Issuer: PHASE 1 — Evidence accumulation (off-chain)
  
  Soul->>Issuer: Demonstrate role competence<br/>(Workshop session / project delivery / mentorship)
  Issuer->>Issuer: Internal review<br/>(F-G-R provenance trace<br/>peer attestation)
  Issuer->>IPFS: Upload role-attestation metadata<br/>(JSON-LD; per A.16 U.Episteme schema)
  IPFS-->>Issuer: Return CID hash
  
  Note over Issuer, Chain: PHASE 2 — On-chain attestation
  
  Issuer->>Chain: mint SBT(<br/>  recipient: Soul,<br/>  roleType: bytes32,<br/>  fgrTriple: bytes32,<br/>  ipfsCID: string,<br/>  issuedAt: timestamp)
  Chain->>Chain: Verify Issuer authorized<br/>(Pillar C R7 — no autonomous arbitration)
  Chain->>Chain: Mint non-transferable token<br/>bound to Soul address
  Chain-->>Soul: SBT_id event emitted<br/>(Soul can prove ownership)
  Chain-->>Issuer: TransactionReceipt
  
  Note over FoundationDocs, Chain: Constitutional check (continuous lint)
  
  FoundationDocs->>Chain: Verify SBT contract address<br/>= RUSLAN-LAYER overlay<br/>(NOT named in Foundation Parts — IP-1 preserved)
  FoundationDocs->>Chain: Verify F-G-R schema<br/>= Pillar A.B.3 compliant
  
  Note over Soul, Verifier: PHASE 3 — Verification (any time)
  
  Verifier->>Chain: Query Soul's SBT registry<br/>(getSBTs(soulAddress))
  Chain-->>Verifier: Return SBT attestations array
  Verifier->>IPFS: Fetch metadata for each SBT CID
  IPFS-->>Verifier: Return JSON-LD metadata
  
  alt Privacy required (ZK-SBT)
    Verifier->>Soul: Request ZK-proof<br/>(prove "I have ≥3 master-level SBTs"<br/>without revealing identity)
    Soul->>Soul: Generate ZK-proof<br/>(Semaphore / Polygon ID)
    Soul-->>Verifier: ZK-proof response
    Verifier->>Chain: Verify ZK-proof<br/>(verifyProof(proof, publicInputs))
    Chain-->>Verifier: Boolean valid/invalid
  end
  
  Note over Issuer, Chain: PHASE 4 — Revocation (rare; governance-gated)
  
  Issuer->>Issuer: Revocation governance<br/>(DAO vote OR Issuer-Soul ack)
  Issuer->>Chain: revoke(SBT_id, reasonCID)
  Chain->>Chain: Mark SBT as revoked<br/>(NOT burned — audit trail preserved per A.10)
  Chain-->>Soul: SBT revoked event
  
  Note over Soul, Verifier: PHASE 5 — Fork-and-leave (R12 preserved)
  
  Soul->>Soul: Decide to leave Clan
  Soul->>Chain: Clan-membership SBT remains in soul wallet<br/>OR explicitly revoked by Clan governance
  Chain->>Soul: Workshop-graduate SBT remains permanent<br/>(role-attestation portable)
  Soul->>Verifier: New context (different Clan / external)<br/>presents SBT credentials
  Verifier-->>Soul: Recognize Workshop-graduate role<br/>(cross-Clan SBT recognition per Federation governance)
```

## §2 Reading guide

**5 phases:**

1. **Evidence accumulation (off-chain)** — Workshop session / project / mentorship demonstrates role competence. F-G-R provenance + peer attestation reviewed off-chain. Metadata uploaded к IPFS.

2. **On-chain attestation** — Issuer mints SBT to Soul address. Non-transferable + bound to Soul. Constitutional checks ensure Foundation Parts intact (no IP-1 violation; F-G-R schema valid).

3. **Verification (any time)** — External Verifier queries Soul's SBT registry; fetches IPFS metadata. **ZK-SBT path** for privacy-required verifications (Buterin d/acc-aligned).

4. **Revocation (rare)** — Issuer revokes via governance (DAO vote or Issuer-Soul ack). SBT marked revoked but NOT burned (audit trail preserved per A.10 Evidence Graph).

5. **Fork-and-leave (R12 preserved)** — Soul can leave Clan; Clan-membership SBT removed but Workshop-graduate SBT remains permanent. Role-attestation portable to new Clan or external verification.

## §3 Critical constitutional checks

- **IP-1 Role≠Executor:** SBT contract address = RUSLAN-LAYER overlay; Foundation Parts unchanged
- **Pillar C R7:** Revocation requires governance (no autonomous arbitration)
- **Pillar C R12:** Fork-and-leave preserved (Workshop-graduate SBT portable)
- **A.10 Evidence Graph:** Revocation = «mark» not «delete» — audit trail preserved
- **B.3 F-G-R:** Each SBT carries F-G-R triple in metadata

## §4 Source

`../04-sbt-role-attestation.md` §6 + `../00-MASTER-ARCHITECTURE.md` §4 constitutional preservation
