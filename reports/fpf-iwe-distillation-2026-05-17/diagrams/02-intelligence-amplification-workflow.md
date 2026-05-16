---
title: Diagram 02 — FPF intelligence amplification workflow
date: 2026-05-17
type: mermaid
parent: 01-fpf-on-human-language.md §6 (the C4-key answer)
F: F4
G: distillation-diagrams
R: refuted_if_mechanism_steps_misordered
---

# Diagram 02 — FPF Intelligence Amplification Workflow

> «От raw input до improved decision, по шагам» — ответ на Левенчуковский C4 challenge.
> Контрастируем vanilla AI loop vs FPF-loaded AI loop.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, system-ui, sans-serif','fontSize':'13px'}}}%%
flowchart LR
    INPUT["<b>Raw input</b><br><small>vague project question:<br>'Should we buy / fine-tune / build agent stack?'</small>"]:::input

    subgraph VANILLA["<b>Vanilla AI loop (no FPF)</b>"]
        direction TB
        V1["context window drift"]:::vanilla
        V2["mixed vocab<br><small>product+safety+ops smeared</small>"]:::vanilla
        V3["premature convergence<br><small>first plausible answer</small>"]:::vanilla
        V4["one document output<br><small>same text for all audiences</small>"]:::vanilla
        V5["no audit trail<br><small>'why?' lost</small>"]:::vanilla
        V1 --> V2 --> V3 --> V4 --> V5
    end

    subgraph FPF["<b>FPF-loaded AI loop</b>"]
        direction TB
        F1["1. Declare U.BoundedContext (A.1.1)<br><small>product / safety / infra / evaluation contexts</small>"]:::fpf
        F2["2. Map U.Roles + method-signatures (A.2/A.3)<br><small>not 'team' — typed responsibilities</small>"]:::fpf
        F3["3. Define U.Alpha-state-graphs (A.2.5)<br><small>past-participle states + checklists per alpha</small>"]:::fpf
        F4["4. Abductive Loop B.5.2<br><small>generate alternatives portfolio<br>NOT pick first</small>"]:::fpf
        F5["5. Explore-Exploit governor C.17-C.19<br><small>declare scale, sample wide before focusing</small>"]:::fpf
        F6["6. F-G-R per claim B.3<br><small>tag formality/scope/reliability<br>auditor can triage</small>"]:::fpf
        F7["7. F.17 UTS<br><small>stabilize vocabulary for risky terms</small>"]:::fpf
        F8["8. E.9 DRR<br><small>decision rationale durable<br>survives team rotation</small>"]:::fpf
        F9["9. E.17 MVPK<br><small>one underlying work<br>→ Plain / Tech / Interop / Assurance views</small>"]:::fpf
        F10["10. F.9 Bridges<br><small>explicit cross-context translation<br>when scope change</small>"]:::fpf

        F1 --> F2 --> F3 --> F4 --> F5 --> F6 --> F7 --> F8 --> F9
        F8 -.->|loops back| F4
        F10 -.->|when scope shifts| F1
    end

    VANILLA_OUT["<b>Vanilla output</b><br><small>structured but ungrounded;<br>indistinguishable from 'confident nonsense'<br>(Spec L187)</small>"]:::vanilla_out
    FPF_OUT["<b>FPF-loaded output</b><br><small>bounded-context map +<br>decision criteria +<br>portfolio of alternatives +<br>evidence/test gap list +<br>starter DRR + UTS +<br>aligned outputs per audience</small>"]:::fpf_out

    INPUT --> VANILLA
    INPUT --> FPF
    VANILLA --> VANILLA_OUT
    FPF --> FPF_OUT

    LEVENCHUK_TEST["<b>Левенчуковский C4 test (2026-05-17)</b><br><small>«Разница видна за пять минут сравнений»</small>"]:::test
    VANILLA_OUT -.->|compare| LEVENCHUK_TEST
    FPF_OUT -.->|compare| LEVENCHUK_TEST

    classDef input fill:#fff8e1,stroke:#f57c00,stroke-width:3px
    classDef vanilla fill:#ffebee,stroke:#c62828,stroke-width:2px
    classDef vanilla_out fill:#ffebee,stroke:#c62828,stroke-width:3px
    classDef fpf fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef fpf_out fill:#e0f2f1,stroke:#00695c,stroke-width:3px
    classDef test fill:#fce4ec,stroke:#ad1457,stroke-width:3px
```

**Note.** Steps F1-F10 not strict order — they are concurrent disciplines applied к
the SAME work. Diagram shows them sequentially for didactic clarity per FPF Pillar P-2.
Provenance: synthesized from FPF-Spec Readme one-minute-example (L97-114) + Part A/B/C
patterns referenced + Левенчуковский TG C4 quote.
