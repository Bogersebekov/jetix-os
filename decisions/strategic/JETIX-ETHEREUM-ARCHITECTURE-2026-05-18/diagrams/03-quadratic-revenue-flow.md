---
title: "Diagram 03 — Workshop revenue → Quadratic Funding distribution flow"
date: 2026-05-18
type: architecture-diagram
F: F3
G: jetix-qf-revenue-flow-diagram
parent: ../00-MASTER-ARCHITECTURE.md
---

# Diagram 03 — Workshop revenue → Quadratic Funding distribution flow

## §1 Full flow diagram

```mermaid
flowchart TB
  Client[Workshop Client<br/>пays fiat €10K]
  Corp[Jetix UG/GmbH<br/>legal entity O-02<br/>receives fiat]
  
  Corp -->|step 1: withhold| Tax[Tax + VAT + opex<br/>~40% €4400]
  Corp -->|step 2: net €5600| Convert[Fiat → USDC<br/>licensed ramp]
  Convert -->|step 3: USDC| DAO_Treasury[DAO Treasury<br/>Ethereum L2 Base]
  
  DAO_Treasury -->|step 4: trigger distribution| Signal[Signal Phase<br/>SBT-gated]
  
  Signal -->|members signal contribution<br/>SBT + peer attestation| Sig_Members[Member contributions<br/>per project:<br/>Alice: 100u → Bob: 50u → Carol: 30u → Dave: 80u<br/>etc.]
  
  Sig_Members -->|step 5: QF formula| QF_Calc["QF Calculation<br/>matching_i = (Σ_j sqrt(c_j_to_i))²"]
  
  QF_Calc -->|step 6: enforce ratio cap| Ratio[Mondragón 5:1 ratio cap<br/>verify maxShare ≤ minShare × 5<br/>else redistribute proportionally]
  
  Ratio -->|step 7: distribute| Distribute[Distribution Smart Contract<br/>transfer USDC к member wallets]
  
  Distribute --> Member_A[Alice Soul wallet<br/>receives X USDC<br/>Workshop-graduate SBT preserved]
  Distribute --> Member_B[Bob Soul wallet<br/>receives Y USDC]
  Distribute --> Member_C[Carol Soul wallet<br/>receives Z USDC]
  Distribute --> Member_D[Dave Soul wallet<br/>receives W USDC]
  
  Distribute -->|emit event| EventLog[Event Log<br/>Evidence Graph A.10<br/>publicly auditable]
  
  Member_A -->|step 8: optional| OffRamp_A[Off-ramp USDC → fiat<br/>per jurisdiction tax]
  
  EventLog -->|continuous validation| R12_Check[R12 anti-extraction<br/>check passed<br/>F-G-R provenance preserved]
  
  R12_Check -->|validates| Foundation[Foundation Layer 1<br/>Pillar C Tier 2 rule 12<br/>substrate-agnostic principle intact]
  
  style Client fill:#fef3c7,color:#1a202c
  style Corp fill:#dbeafe,color:#1a202c
  style DAO_Treasury fill:#fef3c7,color:#1a202c
  style QF_Calc fill:#bbf7d0,color:#1a202c
  style Ratio fill:#bbf7d0,color:#1a202c
  style Distribute fill:#bbf7d0,color:#1a202c
  style Foundation fill:#fce7f3,color:#1a202c
  style R12_Check fill:#fce7f3,color:#1a202c
```

## §2 Step-by-step

| Step | Action | Constitutional check |
|---|---|---|
| **1** | Client pays €10K fiat to Jetix UG/GmbH | Legal entity O-02 |
| **2** | Corp withholds tax (VAT 19% + corporate ~10-15% + opex); net €5600 | Legal compliance discipline |
| **3** | Corp converts net → USDC via licensed ramp | KYC at Corp boundary (not member boundary) |
| **4** | USDC transferred to DAO Treasury (Ethereum L2 Base) | RUSLAN-LAYER overlay — Corp directors required to transfer per Articles of Association |
| **5** | Distribution trigger: members signal contributions per project (SBT-gated; peer-attested) | SBT-gated = anti-Sybil; peer attestation = F-G-R provenance |
| **6** | QF formula calculates proposed distribution: `matching_i = (Σ sqrt(c_j_to_i))²` | Anti-concentration mathematical property |
| **7** | Mondragón 5:1 ratio cap enforced (max/min ≤ 5:1; else redistribute) | R12 Tier 2 hard cap |
| **8** | Distribution smart contract transfers USDC to member wallets | Immutable contract; auditable |
| **9** | Event log emits → publicly auditable; Evidence Graph A.10 trace | Transparency + audit |
| **10** | Member off-ramps USDC → fiat per jurisdiction (optional) | Per-member jurisdiction tax |
| **continuous** | R12 anti-extraction validation continuous; Foundation Layer 1 intact | Pillar C preservation |

## §3 QF formula worked example

**Scenario:** Workshop project «Open-Source Pattern Language v1» (Phase 2 deliverable).
**Matching pool:** €5600 (from DAO treasury, one Workshop event)
**4 contributors signal contributions** (peer-attested, F-G-R verified):

| Contributor | Contribution magnitude | sqrt(c) |
|---|---|---|
| Alice (founder lineage) | 200 units | 14.14 |
| Bob (Workshop graduate) | 100 units | 10.00 |
| Carol (mentor) | 50 units | 7.07 |
| Dave (newcomer) | 30 units | 5.48 |
| **Σ** | **380** | **36.69** |

**QF matching:** Σ² = 36.69² = **1346**
**Distribute matching pool by sqrt-weighted share:**

| Contributor | sqrt(c) / Σ | Share |
|---|---|---|
| Alice | 14.14 / 36.69 = 38.5% | €2156 |
| Bob | 10.00 / 36.69 = 27.3% | €1529 |
| Carol | 7.07 / 36.69 = 19.3% | €1081 |
| Dave | 5.48 / 36.69 = 14.9% | €834 |

**Mondragón 5:1 cap check:** Max (Alice 2156) / Min (Dave 834) = 2.58:1. **Within 5:1 cap.** ✅

**Distribute** as calculated.

**Alternative scenario:** If Alice contributed 1000 instead of 200 → Alice share = 73% €4088; Dave share = 7% €392. Ratio 10.4:1. **Exceeds 5:1 cap.** Redistribute: Alice capped at Dave×5 = 1960; excess €2128 redistributed proportionally к Bob+Carol+Dave.

## §4 Anti-Sybil layer

Pre-QF gating:
1. **SBT-gated participation** — only Clan-SBT holders can signal
2. **Peer co-sign required** — each signal needs ≥1 attestation from established Soul
3. **F-G-R reliability factor** — new Souls (R-low) signal weight × 0.5; established (R-high) × 1.0
4. **Stake bond** — signaler posts small SBT-bond; lost if peer-reviewed as Sybil

## §5 Source

`../06-quadratic-funding-workshop-revenue.md` §2-§3 + `../03-r12-programmable-enforcement.md` §2.4 hybrid pattern
