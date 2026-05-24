---
title: D12 — 5-clause Empirical + R12 Filter Funnel
date: 2026-05-24
type: diagram
phase: 8
---

# D12 — Operational Empirical + R12 Filter Funnel (5-clause test)

```mermaid
flowchart TD
    START[NLP technique under consideration<br/>for Jetix import]
    C1{1. Independent peer-reviewed<br/>non-NLP-affiliated source<br/>for functional effect?}
    C2{2. Better-validated equivalent<br/>in adjacent literature?<br/>Bolton/CBT/ACT/Atomic/Gollwitzer}
    C3{3. Falsified by independent research?<br/>Sharpley/Heap/NRC/Wiseman/Sturt}
    C4{4. R12-compatible in transparent<br/>voluntary fork-and-leave-preserving deployment?}
    C5{5. Technique defining feature = covertness?<br/>OR built-for-covert deployment?}
    SKIP_NO_SRC[SKIP — R6 violation if cited as authority]
    USE_ALT[IMPORT FROM VALIDATED SOURCE not NLP framing]
    SKIP_FALSIFIED[HARD SKIP — falsified claim cannot be soft-promoted]
    SKIP_R12[SKIP — R12 violation]
    SKIP_COVERT[SKIP — built-for-covert]
    IMPORT[IMPORT with empirical-source citation<br/>per Phase 6 binding sec 6.18]
    START --> C1
    C1 -->|N| SKIP_NO_SRC
    C1 -->|Y| C2
    C2 -->|Y| USE_ALT
    C2 -->|N| C3
    C3 -->|Y| SKIP_FALSIFIED
    C3 -->|N| C4
    C4 -->|N| SKIP_R12
    C4 -->|Y| C5
    C5 -->|Y| SKIP_COVERT
    C5 -->|N| IMPORT
    style SKIP_NO_SRC fill:#ffcccc
    style SKIP_FALSIFIED fill:#ffcccc
    style SKIP_R12 fill:#ffcccc
    style SKIP_COVERT fill:#ffcccc
    style USE_ALT fill:#ffe0cc
    style IMPORT fill:#c8e6c9
```

## Reading

5-clause filter executes Phase 6 + Phase 7 disciplines as operational decision flow. **Any FAIL = SKIP / 5-of-5 PASS = IMPORT.**

This is the daily operational gate when considering NLP-derived material for Workshop curriculum / Welcome-frame enhancement / Cohort building protocol.
