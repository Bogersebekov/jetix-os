---
title: D11 — R12 Paired-Frame Discipline Test Funnel
diagram_id: D11
phase: 7
F: F2-F3
---

# D11 — 3-Layer R12 Discipline Test Funnel

```mermaid
flowchart TB
    DESIGN[Any Jetix recruitment / Welcome-frame /<br/>cohort design move]:::start

    DESIGN --> T1{LAYER 1<br/>9-clause R12 test<br/>Phase 7 §7.0}:::test

    T1 -.fails.-> REVISE1[Revise to R12-compatible form]:::revise
    T1 -.passes.-> T2{LAYER 2<br/>16-point Clan-vs-Cult test<br/>Phase 4 §4.6}:::test

    T2 -.fails.-> REVISE2[Audit against Lifton+Hassan+Hoffer SKIP-list<br/>Revise structural design]:::revise
    T2 -.passes.-> T3{LAYER 3<br/>8-point Cialdini Discipline test<br/>Phase 3 §3.6}:::test

    T3 -.fails.-> REVISE3[Revise communication]:::revise
    T3 -.passes.-> AUDIT[70-entry SKIP-list audit<br/>Phase 7 §7.3]:::test

    AUDIT -.match SKIP entry.-> REVISE4[Skip technique<br/>or substitute IMPORT]:::revise
    AUDIT -.clean.-> DEPLOY[✅ R12-compatible<br/>Deploy]:::ok

    REVISE1 --> DESIGN
    REVISE2 --> DESIGN
    REVISE3 --> DESIGN
    REVISE4 --> DESIGN

    classDef start fill:#9cf
    classDef test fill:#ff9
    classDef revise fill:#fc9
    classDef ok fill:#9f9
```

**Source:** Phase 7 §7.0 + §7.3 + §7.4 + cumulative test artifacts.

**Operational use:** Every recruitment / Welcome-frame / cohort design
decision passes through 4 layers. Failure at any layer → revise. Only
recommendations passing all 4 → deploy.

**Test composition:**
- **9-clause R12 test** = pull/disclose/substrate-real/reversible/portable/glossaried/falsifiable/impartial/fork-preserved
- **16-point Clan-vs-Cult test** = 16 cult-substrate questions inverted
- **8-point Cialdini Discipline test** = per-principle compliance check
- **70-entry SKIP-list** = full mechanism audit
