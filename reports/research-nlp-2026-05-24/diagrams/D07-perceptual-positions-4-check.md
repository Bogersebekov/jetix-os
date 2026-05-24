---
title: D07 — Perceptual Positions 4-check
date: 2026-05-24
type: diagram
phase: 8
---

# D07 — Perceptual Positions 4-position Audit Before Action

```mermaid
flowchart TD
    ACTION[Action under consideration<br/>e.g. Welcome-frame invite / Promotion offer / Workshop pitch]
    P1[FIRST POSITION self<br/>What am I asking?<br/>What am I offering?]
    P2[SECOND POSITION partner<br/>If I were receiving this<br/>how would it land?]
    P3[THIRD POSITION observer<br/>From outside does this look<br/>honest? Coercive? Manipulative?]
    P4[FOURTH POSITION Jetix system<br/>Does this preserve fork-and-leave?<br/>Does this honor R12?]
    Q1{Concern raised?}
    Q2{Concern raised?}
    Q3{Concern raised?}
    Q4{Concern raised?}
    GO[Proceed with action]
    HALT[Halt + revise]
    ACTION --> P1 --> Q1
    Q1 -->|No| P2 --> Q2
    Q1 -->|Yes| HALT
    Q2 -->|No| P3 --> Q3
    Q2 -->|Yes| HALT
    Q3 -->|No| P4 --> Q4
    Q3 -->|Yes| HALT
    Q4 -->|No| GO
    Q4 -->|Yes| HALT
    style P1 fill:#cce5ff
    style P2 fill:#cce5ff
    style P3 fill:#cce5ff
    style P4 fill:#c8e6c9
    style GO fill:#c8e6c9
    style HALT fill:#ffcccc
```

## Reading

Perceptual Positions discipline applied as **mandatory 4-position check** before any R12-sensitive action. Any single concern = halt + revise.

This is the **identity-binding-free** version of Dilts Logical Levels — adopts perspective-taking discipline without committing to neurological-levels causal claim.
