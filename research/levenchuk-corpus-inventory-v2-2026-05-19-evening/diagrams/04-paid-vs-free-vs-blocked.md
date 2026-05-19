---
title: Diagram 4 — Paid vs Free vs Blocked
phase: 6
parent: research/levenchuk-corpus-inventory-v2-2026-05-19-evening/
---

# Diagram 4 — Volume distribution: Paid vs Free vs Blocked

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
pie title Levenchuk Corpus Access Distribution (source count by access type)
    "FREE web/repo (LJ + МИМ + arXiv + GitHub + 3rd-party)" : 25
    "PAID Ruslan-handles (Aisystant 8 + Ridero 9 + LitRes 12 + R1-R10)" : 38
    "BLOCKED / 404 / rejected (LJ tags + Ozon + YT transcripts + IWE chat)" : 7
```

---

## Summary table — volume estimates by access type

| Access type | Source count | Volume estimate | Examples |
|---|---|---|---|
| **FREE (web/repo accessible)** | ~25 | unlimited (web) + 8 MB PDF + 73K FPF lines + 2 arXiv papers | LJ ailev / system-school.ru pages / arXiv abstracts / Psybertron / Habr/vc.ru samples / GitHub FPF / TechInvestLab PDF / in.wiki / inexsu / Tseren systemsworld / TG @ailev_blog |
| **PAID (Ruslan handles)** | ~38 items | ~4080 pp Ridero + 12 LitRes + 8 Aisystant courses + 10 residencies | Ridero 9 / LitRes 12 / Aisystant 8 courses / R1-R10 residencies |
| **BLOCKED** | 7 | n/a | LJ tag pages (4 × 404) / Ozon catalog (geo-redirect) / YT transcripts (infrastructure) / IWE chat interface (REJECTED per memory) |

---

## Cost projection (€ approximate)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    R[Ruslan acquisition decision] --> A[Tier-A €0-50<br/>2-3 Ridero books<br/>+ free corpus]
    R --> B[Tier-B €50-200<br/>9 books + Aisystant 1mo<br/>+ test material]
    R --> C[Tier-C €600-1000<br/>+ R1 residency cohort<br/>practical validation]
    R --> D[Tier-D €5K-7K<br/>+ Full R1-R10 14mo<br/>complete pathway]
    R --> E[Tier-E €20K+<br/>+ Project-based mentor sup<br/>premium investment]

    style A fill:#d6f0d6,color:#000
    style B fill:#fff8d5,color:#000
    style C fill:#fff8d5,color:#000
    style D fill:#fff4e6,color:#000
    style E fill:#ffd6d6,color:#000
```

**Each tier additive, не replacement.** Ruslan picks; Phase 5 §G surfaces overlap-strength ordering (NOT judgment).
