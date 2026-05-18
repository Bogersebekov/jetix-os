---
title: H8 substrate decision tree (Phase 1 → 3+)
date: 2026-05-18
type: diagram
parent: research/deepening-2026-05-18/07-substrate-matrix-vc-sbt-pgp-coordinape.md
---

# Diagram 01 — H8 Substrate Decision Tree (Phase 1 → 3+)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
flowchart TD
  Q1{Phase 1: need immediate role-attestation?}
  Q1 -->|Yes| PGP[PGP-signed Foundation Part changes + Karpathy-wiki-sig convention]
  Q1 -->|No| WAIT[Defer until Phase 2]

  PGP --> Q2{Phase 2: need selective disclosure + production-grade?}
  Q2 -->|Yes| VC[W3C VC v2.0 — Recommendation May 15 2025]
  Q2 -->|No| EXT[Extend PGP + wiki-sig substrate]

  VC --> Q3{Phase 2+: need peer-allocated reward mechanism?}
  Q3 -->|Yes| COORD_PATTERN[Coordinape EPOCH+PEER-ALLOC pattern — adopt without Ethereum]
  Q3 -->|No| KEEP[Keep VC v2.0 substrate]

  KEEP --> Q4{Phase 3+: crypto-native partner Clan onboarding?}
  Q4 -->|Yes| SBT_OPT[SBT optional supplementary — NOT Foundation default]
  Q4 -->|No| DONE[H8 substrate stack stable]

  COORD_PATTERN --> Q4
  EXT --> Q3

  style Q1 fill:#fef3c7,color:#1a202c
  style Q2 fill:#fef3c7,color:#1a202c
  style Q3 fill:#fef3c7,color:#1a202c
  style Q4 fill:#fef3c7,color:#1a202c
  style PGP fill:#bbf7d0,color:#1a202c
  style VC fill:#bbf7d0,color:#1a202c
  style COORD_PATTERN fill:#bbf7d0,color:#1a202c
  style KEEP fill:#bbf7d0,color:#1a202c
  style EXT fill:#dbeafe,color:#1a202c
  style WAIT fill:#dbeafe,color:#1a202c
  style SBT_OPT fill:#fef3c7,color:#1a202c
  style DONE fill:#bbf7d0,color:#1a202c
```

**Recommended Jetix path (default branch):** PGP → VC v2.0 → Coordinape pattern adoption → SBT optional. **Substrate-agnostic claim** preserved by never locking to single substrate.
