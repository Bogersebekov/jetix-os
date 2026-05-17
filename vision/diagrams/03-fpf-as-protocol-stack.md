---
title: Diagram 03 — FPF as Protocol Stack (FPF + open-data + role-based trust)
date: 2026-05-17
type: vision-diagram
parents:
  - vision/01-fpf-as-universal-language.md
  - vision/02-internet-layer-for-engineers.md
  - decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md
  - raw/voice-memos-2026-05-17-batch/text_001@17-05-2026_22-00.md
  - raw/voice-memos-2026-05-17-batch/text_002@17-05-2026_22-30.md
F: F3
G: vision-diagram-protocol-stack
constitutional_posture: R1 + R2 + R6 + EP-5
---

# Diagram 03 — FPF as Protocol Stack

> Visual encoding: FPF + open data + role-based attestation = composed trust + cooperation protocol stack. Inspired by OSI layering metaphor; semantic-only (NOT literal network stack spec).

```mermaid
flowchart BT
    subgraph App ["L5 — Application layer<br/>(Jetix Workshop / Clan / first projects)"]
        AppA["Cooperation events"]
        AppB["First-clan workflows"]
        AppC["Workshop deliverables"]
    end

    subgraph Trust ["L4 — Trust composition layer (H8)"]
        TrustA["Role attestation<br/>(actor.role + scope)"]
        TrustB["Open data<br/>(past commitments)"]
        TrustC["FPF context<br/>(domain framing)"]
    end

    subgraph Translate ["L3 — Translation layer (H2F2H workflow)"]
        TransA["Human → FPF<br/>(formalization)"]
        TransB["FPF → Human_i<br/>(per-participant translation)"]
    end

    subgraph FPF ["L2 — FPF formalization layer"]
        FPFA["U.System / U.Role / U.Commitment"]
        FPFB["A.16 U.Episteme single SoT"]
        FPFC["F-G-R typed claims"]
    end

    subgraph Substrate ["L1 — Substrate layer"]
        SubA["Filesystem<br/>(SoT — Tier 2)"]
        SubB["Git append-only<br/>(history)"]
        SubC["Internet transport<br/>(HTTP, git+ssh, etc)"]
    end

    Substrate --> FPF
    FPF --> Translate
    Translate --> Trust
    Trust --> App

    Money["Legacy: Money as trust signal<br/>(low-fidelity, person→person)"]
    Money -.->|H8 supplants| Trust

    classDef substrate fill:#cfd8dc,stroke:#37474f,color:#000
    classDef fpf fill:#bbdefb,stroke:#1976d2,color:#000
    classDef translate fill:#c8e6c9,stroke:#2e7d32,color:#000
    classDef trust fill:#fff9c4,stroke:#f57f17,color:#000
    classDef app fill:#ffe082,stroke:#ef6c00,color:#000
    classDef legacy fill:#ffcdd2,stroke:#c62828,color:#000

    class Substrate substrate
    class FPF fpf
    class Translate translate
    class Trust trust
    class App app
    class Money legacy
```

**Legend:**
- L1 Substrate (grey) = filesystem + git + internet — already exists
- L2 FPF (blue) = formalization — exists as spec; usage = aspirational
- L3 Translation (green) = H2F2H workflow — manual today; tooling = MVPK Component 2 (vision/07)
- L4 Trust (yellow) = H8 composition — text + vapor mechanism
- L5 Application (orange) = Jetix Workshop / Clan — vapor today
- Money (red dashed) = legacy trust signal; H8 supplants (not replaces — supplement)

**Layer dependencies:** higher layers presuppose lower. App layer (L5) collapses if Trust (L4) mechanism absent. Trust (L4) requires Translation (L3) for human accessibility. Translation requires FPF (L2) formalism. FPF requires Substrate (L1) persistence.

**Constitutional note:** H8 LOCK does not claim money replacement — claims fidelity upgrade. Diagram explicit: Money → Trust = «supplants OR supplements» (text_001 ambiguous; vision/00 §7 Q-7).

[src: vision/01 §4 H2F2H + vision/02 §4 properties + H8 LOCK + text_001 ¶3-5 + text_002 ¶1-2]
