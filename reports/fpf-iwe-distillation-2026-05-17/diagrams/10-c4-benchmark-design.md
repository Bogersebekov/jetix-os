---
title: Diagram 10 — C4 benchmark design (vanilla / FPF-loaded / IWE / Jetix-stack)
date: 2026-05-17
type: mermaid
parent: 02-u-episteme-and-iwe.md §3.2 + inbox/levenchuk-tg-2026-05-17.md C4
F: F4
G: distillation-diagrams
R: refuted_if_arms_misdesigned
note: |
  Phase B execution artifact. Phase A surface only the design.
  NOT to execute now per prompt §11 explicit halt.
---

# Diagram 10 — C4 Benchmark Design (Левенчуковский test)

> Per Левенчуковский C4 (TG 2026-05-17):
> «грузите FPF AI-агенту и спрашиваете про ваш проект, или спрашиваете про ваш проект
> прямо у AI-агента без FPF. Разница видна за пять минут сравнений.»

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'13px'}}}%%
flowchart TB
    QUESTION["<b>Test question</b><br><small>About Jetix project — chosen from:<br>1. 'Should Jetix focus 2026 on AI consulting OR community building?'<br>2. 'How to organize 12-agent swarm avoiding role drift?'<br>3. 'How to validate monetization bank 166 H signals?'<br>4. 'How to design partnership с МИМ ethically?'<br>5. 'What's the right scope для FPF integration в Jetix?'</small>"]:::input

    subgraph ARM_A["<b>Arm A — Vanilla Claude / GPT</b><br><small>(control: no FPF, no Jetix context)</small>"]
        A_IN["Input: question only<br>(blank chat session)"]:::vanilla
        A_OUT["Output A:<br><small>'best practices' generic answer</small>"]:::vanilla
    end

    subgraph ARM_B["<b>Arm B — FPF-loaded AI</b><br><small>(Левенчуковский recommendation)</small>"]
        B_IN["Input: question +<br>FPF-Spec.md (62K lines)<br>+ Левенчуковский Starter Prompt (Readme L304)"]:::fpf
        B_OUT["Output B:<br><small>bounded contexts + decision criteria +<br>alternatives portfolio + evidence gaps +<br>starter DRR + UTS</small>"]:::fpf
    end

    subgraph ARM_C["<b>Arm C — IWE itself</b><br><small>(Цэрэновский applied FPF)</small>"]
        C_IN["Input: question reframed<br>в IWE guide format<br>(aisystant.system-school.ru)"]:::iwe
        C_OUT["Output C:<br><small>МИМ residency-style guidance<br>+ recommended route through 16 trans-discs<br>+ relevant книги/practices к study</small>"]:::iwe
    end

    subgraph ARM_D["<b>Arm D — Jetix stack</b><br><small>(claude -p через Foundation + wiki + skills)</small>"]
        D_IN["Input: question + Jetix context<br>(Foundation v1.0 LOCKED + Wiki v2 +<br>strategic insights + Pillar C)"]:::jetix
        D_OUT["Output D:<br><small>Jetix-style — Strategic Insight cards +<br>D-Lock entries + Foundation Part refs +<br>F-G-R-tagged claims</small>"]:::jetix
    end

    subgraph COMPARE["<b>Comparison rubric (≥5 criteria)</b>"]
        CR1["1. Bounded context clarity<br><small>does answer respect explicit context?</small>"]:::criterion
        CR2["2. Alternatives portfolio<br><small>does answer surface ≥3 alternatives?</small>"]:::criterion
        CR3["3. F-G-R trust trail<br><small>do claims declare formality/scope/reliability?</small>"]:::criterion
        CR4["4. Audit-ability<br><small>can next reader trace why this conclusion?</small>"]:::criterion
        CR5["5. Multi-audience views<br><small>different audiences get aligned outputs?</small>"]:::criterion
        CR6["6. Generative breadth<br><small>does answer escape first-plausible loop?</small>"]:::criterion
        CR7["7. Domain accuracy<br><small>specifically applies к Jetix vs generic?</small>"]:::criterion
    end

    QUESTION --> A_IN
    QUESTION --> B_IN
    QUESTION --> C_IN
    QUESTION --> D_IN

    A_IN --> A_OUT
    B_IN --> B_OUT
    C_IN --> C_OUT
    D_IN --> D_OUT

    A_OUT --> COMPARE
    B_OUT --> COMPARE
    C_OUT --> COMPARE
    D_OUT --> COMPARE

    JUDGE["<b>Judges</b><br><small>Ruslan (primary) +<br>blind reviewer (e.g. Tseren or Levenchuk if amenable)</small>"]:::judge
    COMPARE --> JUDGE

    RESULT["<b>Output artifact (Phase B)</b><br><small>reports/c4-benchmark-2026-MM-DD.md<br>tables: per-question per-arm per-criterion scores<br>+ qualitative narrative diff</small>"]:::result
    JUDGE --> RESULT

    HALT["<b>HALT for Phase A — execution is Phase B</b>"]:::halt
    QUESTION -.- HALT

    classDef input fill:#fff8e1,stroke:#f57c00,stroke-width:4px
    classDef vanilla fill:#ffebee,stroke:#c62828,stroke-width:2px
    classDef fpf fill:#e3f2fd,stroke:#1565c0,stroke-width:3px
    classDef iwe fill:#e8eaf6,stroke:#283593,stroke-width:3px
    classDef jetix fill:#fce4ec,stroke:#ad1457,stroke-width:3px
    classDef criterion fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef judge fill:#e0f2f1,stroke:#00695c,stroke-width:3px
    classDef result fill:#fff3e0,stroke:#e65100,stroke-width:3px
    classDef halt fill:#ffebee,stroke:#c62828,stroke-width:4px
```

**Phase A note.** Diagram designs the Phase B benchmark; per prompt §11 + §8 «НЕ
начинать Phase B в этой сессии». Phase B prerequisites: (1) Ruslan ack of Phase A
summary; (2) aisystant access for Arm C; (3) chosen test questions list; (4) blind
reviewer arrangement if external.
