---
title: Cross-link Heatmap — 5 Левенчук Books × 8 Jetix Sources
date: 2026-05-20
type: mermaid-diagram
F: F2
G: levenchuk-books-distill
---

# Cross-link Heatmap — 5 books × 8 sources (Phase 5 distillation)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    subgraph BOOKS["📚 5 books"]
        B1["СМ Т1"]
        B2["СМ Т2"]
        B3["Методология 2025"]
        B4["Интеллект-стек"]
        B5["Инженерия личности"]
    end

    subgraph SRC8["🎯 8 Jetix sources"]
        S1["K-6 method<br/>3 wikis + deep"]
        S2["K-4 intellect<br/>12-audit"]
        S3["5 concept docs F2"]
        S4["Platform v2 §6/§7/§20"]
        S5["Левенчук inventory v2<br/>189-cell"]
        S6["Sprint-Synthesis v2<br/>Doc 4 Step 6"]
        S7["9 Tier A wikis"]
        S8["3 NEW Tier A batch-7<br/>(partnership/mastery/persistence)"]
    end

    B1 ==> |"deep"| S1
    B1 --> |"medium"| S2
    B1 ==> |"deep"| S5
    B1 ==> |"deep"| S7

    B2 ==> |"deep"| S1
    B2 ==> |"deep"| S3
    B2 ==> |"deep"| S5
    B2 ==> |"deep"| S7

    B3 ==> |"deep"| S1
    B3 ==> |"deep"| S3
    B3 ==> |"deep"| S5
    B3 ==> |"deep"| S6

    B4 ==> |"deep"| S2
    B4 ==> |"deep"| S4
    B4 ==> |"deep"| S5
    B4 ==> |"deep"| S8

    B5 ==> |"deep"| S3
    B5 ==> |"deep"| S7
    B5 ==> |"deep"| S8

    style S3 fill:#fff8d5,color:#000
    style S2 fill:#fff8d5,color:#000
    style B3 fill:#d6f0d6,color:#000
```

**Legend:** Bold (==>) = deep / verbatim structural twin; thin (-->) = medium / adjacent overlap. ⭐⭐⭐ central: Methodology 2025 ↔ 5 concept docs.

[src: research/levenchuk-books-distillation-2026-05-20/06-cross-link-к-jetix-substrate.md §1]
