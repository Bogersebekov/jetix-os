---
type: mermaid-diagram
date: 2026-05-19
session: jetix-platform-v2-description-2026-05-19
phase: 9
diagram_subject: Phase 4 — FPF interaction protocol 8-layer stack flow
---

# Diagram 4 — FPF Interaction Protocol Flow

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
sequenceDiagram
    autonumber
    actor User as Participant
    participant L1 as L1 Identity (A.1.1)
    participant L2 as L2 Promise (U.PromiseContent)
    participant L3 as L3 Match (A.6.B Bridge)
    participant L4 as L4 Commitment (A.2.8)
    participant L5 as L5 Execution (A.15 Work)
    participant L6 as L6 Audit (B.3 F-G-R)
    participant L7 as L7 Dispute (U.SpeechAct)
    participant L8 as L8 R12 Enforcement (E.5)

    User->>L1: Register + FPF profile + R12 Charter ack
    L1->>L6: Audit-trail entry (registration)
    L1->>L8: R12 Charter verification

    User->>L2: Publish offer / ask
    L2->>L8: R12 quick-check per offer
    L2->>L6: Audit-trail entry (publication)

    L2->>L3: Match algorithm
    L3->>L3: Algorithmic / Curator / Manual
    L3->>User: Surface candidate matches
    User->>L3: Accept match (both parties)

    L3->>L4: Commitment artefact creation
    L4->>L8: R12 verification (Mondragón + fork-and-leave)
    L4->>L6: Audit-trail entry (commitment)

    L4->>L5: Resources flow + Work execution
    L5->>L6: Progress milestones audit
    L5->>L8: Quarterly R12 audit cadence

    L5->>L6: Completion event
    L6->>L6: F-G-R reliability update
    L6->>User: Reputation update

    alt Failure / dispute
        User->>L7: File dispute (T1 informal)
        L7->>L7: T1 mediation → T2 arbitration → T3 governance
        L7->>L6: Audit-trail (resolution)
        L7->>L8: R12 violation grade triage
        L8->>L8: Halt-Log-Alert if R12 violation
    end
```

## Layer flow (linear simplified)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    L1[L1 Identity<br/>Registration + FPF profile]
    L2[L2 Promise<br/>Offers + Asks]
    L3[L3 Match<br/>Algo + Curator + Manual]
    L4[L4 Commitment<br/>Artefact + R12 verify]
    L5[L5 Execution<br/>Resources flow]
    L6[L6 Audit<br/>F-G-R + Reputation]
    L7[L7 Dispute<br/>3-tier resolution]
    L8[L8 R12 Enforcement<br/>4 mechanisms]

    L1 --> L2 --> L3 --> L4 --> L5 --> L6
    L6 -.-> L7
    L7 -.-> L6
    L1 -.->|audit| L6
    L2 -.->|audit| L6
    L4 -.->|R12| L8
    L7 -.->|violations| L8
    L8 -.->|enforcement| L4

    classDef substrate fill:#90EE90,stroke:#006400
    classDef gov fill:#FFB6C1,stroke:#8B0000

    class L1,L2,L3,L4,L5,L6 substrate
    class L7,L8 gov
```

## Mode negotiation (System Merger Protocol cross-ref)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    PARTNER[Partner system<br/>FPF-fluency assessment]
    PARTNER --> Q1{Full FPF<br/>fluent?}
    Q1 -->|Yes| MODE1[Mode 1 Full-FPF<br/>Default within Jetix]
    Q1 -->|Partial| MODE2[Mode 2 Partial-FPF<br/>Cross-cohort bridges]
    Q1 -->|No| MODE3[Mode 3 Opaque-Bridge<br/>Non-FPF partners]

    MODE1 --> EX[F-G-R verifiable<br/>High-trust env]
    MODE2 --> MAP[FPF→partner mapping<br/>Mid-trust env]
    MODE3 --> TRANS[Translation layer<br/>Low-trust assumed]
```

**R12 enforcement constant across all modes:**
- Mondragón wage-ratio cap
- Quadratic Funding revenue distribution
- Fork-and-leave exit tokens
- Default-Deny constitutional_never_list (4 RUSLAN-LAYER entries)

**Cross-link:** Phase 4 §1-§13 detailed; Phase 5 IP-1 28-entry boundary mapping (per layer substrate-auto vs human-decision).

---

*Mermaid Diagram 4 of 7. Phase 4 visualisation. 8-layer protocol sequence + linear flow + mode negotiation.*
