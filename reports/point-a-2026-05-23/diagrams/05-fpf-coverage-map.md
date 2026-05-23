---
title: D5 — FPF Coverage Map (Primitives × Substrate Areas)
date: 2026-05-23
type: mermaid-diagram
diagram_id: D5
---

# D5 — FPF Coverage Map

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
flowchart LR
    subgraph PRIM[FPF Primitives 8 + R12]
        P1[IP-1 Role≠Executor STRICT]
        P2[IP-2 Substrate-as-Foundation]
        P3[IP-3 Halt-Log-Alert]
        P5[IP-5 Past-participle whitelist]
        P7[IP-7 F-G-R provenance dogfood]
        P_A[A.6.B Append-only history]
        P_B[A.14 Hub-and-spoke]
        P_C[B.3 R6 provenance per claim]
        R12[R12 Anti-Extraction Tier 2 LOCKED]
    end

    subgraph AREAS[Substrate Areas]
        F[Foundation v1.0<br/>11 Parts + Pillar A/C<br/>377 primitive refs]
        D[decisions/strategic/<br/>78 files / 197 primitive refs]
        W[wiki/concepts/<br/>26 files cite FPF]
        PR[principles/<br/>14 files cite FPF]
        SC[shared/schemas/<br/>9 schemas]
        LINT[tools/lints/<br/>8 stubs ⚠️]
        CHARTER[Charter v0 + Pitch Doc<br/>R12 explicit]
    end

    P1 ===> F
    P1 ==> D
    P1 ==> W
    P1 ==> PR
    P1 ==> SC

    P2 ==> F
    P2 ==> D

    P3 ===> F
    P3 ==> D
    P3 ==> SC
    P3 -.> LINT

    P5 ==> F
    P5 ==> SC

    P7 ===> F
    P7 ===> D
    P7 ==> W
    P7 ==> PR
    P7 ==> SC

    P_A ===> F
    P_A ==> D
    P_A ==> W
    P_A ==> PR

    P_B ===> F
    P_B ==> D
    P_B ==> W
    P_B ==> PR

    P_C ===> F
    P_C ===> D
    P_C ==> W
    P_C ==> PR
    P_C ==> SC

    R12 ==> F
    R12 ==> D
    R12 ==> W
    R12 ===> PR
    R12 ==> SC
    R12 ==> CHARTER

    style PRIM fill:#ffe0a0
    style AREAS fill:#d6e8f0
    style R12 fill:#ffd6d6
    style F fill:#d6f0d6
    style CHARTER fill:#fff8d5
    style LINT fill:#f0d6e8
```

**Legend:** `===>` = primary substrate; `==>` = strong application; `-.>` = pending/stub.

---

*D5 2026-05-23. Source: Bucket 2.*
