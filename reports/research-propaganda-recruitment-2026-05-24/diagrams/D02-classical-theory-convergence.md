---
title: D02 — Classical Theory Convergence (Phase 2)
diagram_id: D02
phase: 2
F: F2
---

# D02 — Classical Theory Convergence

```mermaid
flowchart LR
    L[Lippmann 1922<br/>Pseudo-environment<br/>Stereotypes<br/>Manufacture of consent]:::cog
    LB[Le Bon 1895<br/>Mental unity<br/>Anonymity+Contagion+Suggestibility<br/>Prestige-Assertion-Repetition]:::soc
    F[Freud 1921<br/>Libidinal binding<br/>Leader as common ego-ideal<br/>Identification]:::psy
    E[Ellul 1965<br/>Sociological propaganda<br/>Pre-propaganda<br/>Integration vs Agitation<br/>Propagandee wants propaganda]:::struct
    CH[Chomsky-Herman 1988<br/>5 Filters propaganda model<br/>Ownership/Ads/Sourcing/Flak/Enemy]:::pe

    L --> CONV((CONVERGENCE<br/>Mass-democracy opinion<br/>is structurally mediated<br/>NOT direct))
    LB --> CONV
    F --> CONV
    E --> CONV
    CH --> CONV

    CONV --> R12{R12 implication}
    R12 -->|Cannot eliminate<br/>intermediation| CHOICE[Choose: TRANSPARENT<br/>or OPAQUE intermediation]
    CHOICE -->|TRANSPARENT| OK[Jetix R12-compatible<br/>substrate]:::ok
    CHOICE -->|OPAQUE| BAD[R12 VIOLATION<br/>invisible government<br/>+ extraction]:::bad

    classDef cog fill:#cef
    classDef soc fill:#fec
    classDef psy fill:#fcf
    classDef struct fill:#cfe
    classDef pe fill:#cff
    classDef ok fill:#9f9
    classDef bad fill:#f99
```

**Source:** Phase 2 §2.6 cross-author convergence.

**Insight:** 5 different lenses converge on one structural claim — opinion
formation in mass democracy is mediated by intermediaries. R12 doesn't
eliminate intermediation; it determines whether intermediation is
transparent (compatible) or opaque (violation).
