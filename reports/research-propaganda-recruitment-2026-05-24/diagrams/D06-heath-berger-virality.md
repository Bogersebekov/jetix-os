---
title: D06 — Heath SUCCESs + Berger STEPPS Combined
diagram_id: D06
phase: 5
F: F2
---

# D06 — Heath + Berger Virality Frameworks (R12-disciplined)

```mermaid
flowchart LR
    subgraph H[Heath 2007 — SUCCESs<br/>Sticky idea properties]
        S1[Simple]
        S2[Unexpected]
        S3[Concrete]
        S4[Credible]
        S5[Emotional]
        S6[Stories]
    end

    subgraph B[Berger 2013 — STEPPS<br/>Sharing drivers]
        T1[Social Currency]
        T2[Triggers]
        T3[Emotion]
        T4[Public]
        T5[Practical Value]
        T6[Stories]
    end

    S1 --> J1[Commander's intent<br/>Welcome-frame one line]:::j
    S2 --> J2[Honest unexpected<br/>this-is-not framing]:::j
    S3 --> J3[F-G-R schema<br/>specific artifacts]:::j
    S4 --> J4[Verifiable work<br/>member-portable proof]:::j
    S5 -->|substrate-real| J5[Real builder identity]:::j
    S5 -.manufactured.-> SKIP[SKIP]:::bad
    S6 -->|factual| J6[Member case studies<br/>with consent]:::j
    S6 -.fabricated.-> SKIP

    T1 -->|substrate-real| J1
    T1 -.vanity.-> SKIP
    T2 --> J7[Cycle cadence<br/>natural recall]:::j
    T3 -->|substrate-justified| J5
    T3 -.high-arousal manufactured.-> SKIP
    T4 --> J8[Public demos<br/>wikis code]:::j
    T5 --> J9[Methodology shared<br/>practical value]:::j
    T6 -->|factual| J6

    classDef j fill:#9f9
    classDef bad fill:#f99
```

**Source:** Phase 5 §5.2-5.3 + §5.7 imports.

**R12 line:** Both frameworks are R12-compatible **when substrate-grounded**;
SKIP when manufactured. Sticky/viral mechanisms are neutral — what matters
is whether the substrate they ride on is real or fabricated.
