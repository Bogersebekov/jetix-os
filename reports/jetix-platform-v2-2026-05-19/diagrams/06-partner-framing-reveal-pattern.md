---
type: mermaid-diagram
date: 2026-05-19
session: jetix-platform-v2-description-2026-05-19
phase: 9
diagram_subject: Phase 6 — Partner framing reveal pattern + 8-step structure
---

# Diagram 6 — Partner-Framing Reveal Pattern (text_011 thesis operationalised)

## 8-step reveal sequence

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    START[Outreach start]
    START --> S1[1. ANCHOR<br/>«Ты работаешь над их project»]
    S1 --> S2[2. REVEAL Jetix<br/>«Я работаю над Jetix»]
    S2 --> S3[3. ZOOM OUT<br/>«Мы оба работаем над humanity-development»]
    S3 --> S4[4. PARTNER DECLARATION<br/>«Мы уже партнёры — просто не были знакомы»]
    S4 --> S5[5. RECIPROCAL VALUE OFFER<br/>«Вижу могу помочь твоему: X, Y, Z»]
    S5 --> S6[6. RECIPROCAL VALUE ASK<br/>«Прошу help в моём: A, B, C»]
    S6 --> S7[7. CONVERGE<br/>«Together → конкретный positive outcome»]
    S7 --> S8[8. GOAL-ALIGNMENT CHECK<br/>«Verifiable through FPF protocol»]
    S8 --> END[Response window opens]

    classDef framing fill:#FFD700,stroke:#B8860B
    classDef reciprocal fill:#90EE90,stroke:#006400
    classDef alignment fill:#87CEEB,stroke:#1E3A5F

    class S1,S2,S3,S4 framing
    class S5,S6,S7 reciprocal
    class S8 alignment
```

## Pre-meeting profiling required (FPF discipline)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    PROFILE[Pre-outreach profiling<br/>per template]
    PROFILE --> P1[Their project<br/>1-2 paragraphs]
    PROFILE --> P2[Their resources offered<br/>R1-R32 subset]
    PROFILE --> P3[Their likely asks]
    PROFILE --> P4[X/Y/Z Jetix can offer]
    PROFILE --> P5[A/B/C Jetix needs]
    PROFILE --> P6[Goal-alignment expected]
    PROFILE --> P7[Divergent-values risk]

    P7 --> HANDLE{R12 + FPF<br/>compatible?}
    HANDLE -->|Yes| GO[Proceed]
    HANDLE -->|Partial| SCOPE[Scope-limited]
    HANDLE -->|No| DECLINE[Decline]
    HANDLE -->|Unclear| TEST[Small-test]
```

## Saturation discipline (3-tier)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    SAT[Saturation strategy<br/>«каждому запихаю» tempered by quality]

    SAT --> T1[T1 high-leverage 1-on-1<br/>1-2 active cultivations<br/>Templates 13/15/17/19<br/>Cat 12/16/17/19]
    SAT --> T2[T2 medium-batch personalised<br/>5-10 outreaches/week<br/>Templates 8-11/14/16/18/20<br/>Cat 7/8/9/14/16/18/20]
    SAT --> T3[T3 template-batch with touches<br/>20-50 outreaches/week<br/>Templates 1-7/12<br/>Cat 1-7/11]

    T1 --> Q1[Quality floor: 100h engagement before claim]
    T2 --> Q2[Quality floor: 100h engagement before claim]
    T3 --> Q3[Quality floor: 100h engagement before claim]

    Q1 -.-> COMP[F-G-R verifiable claims]
    Q2 -.-> COMP
    Q3 -.-> COMP

    classDef hightier fill:#FFB6C1,stroke:#8B0000
    classDef midtier fill:#FFD700,stroke:#B8860B
    classDef lowtier fill:#90EE90,stroke:#006400

    class T1 hightier
    class T2 midtier
    class T3 lowtier
```

## 10 values × 22 categories × R12 alignment

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    VALUES[10 Values<br/>Phase 6 §0]

    VALUES --> V1[1. Humanity development]
    VALUES --> V2[2. All people partners]
    VALUES --> V3[3. R12 anti-extraction]
    VALUES --> V4[4. Honest transparent]
    VALUES --> V5[5. Reciprocal value]
    VALUES --> V6[6. No hierarchy of worth]
    VALUES --> V7[7. Responsibility-era]
    VALUES --> V8[8. Anti-Sisyphus]
    VALUES --> V9[9. Open-source default]
    VALUES --> V10[10. Long-term thinking]

    V1 --> ENFORCE[Operationalisation:<br/>Phase 4 L8 R12 enforcement<br/>4 mechanisms]
    V2 --> ENFORCE
    V3 --> ENFORCE

    ENFORCE --> E1[Mondragón ratio cap]
    ENFORCE --> E2[QF revenue distribution]
    ENFORCE --> E3[Fork-and-leave exit tokens]
    ENFORCE --> E4[Default-Deny constitutional_never_list]
```

**Cross-link:** Phase 6 §11 reveal pattern + §12 10 base templates + §14 saturation; Phase 8 20 operationalised templates; Phase 4 R12 enforcement.

---

*Mermaid Diagram 6 of 7. Phase 6 visualisation. 8-step reveal + pre-meeting profiling + saturation discipline + values × enforcement.*
