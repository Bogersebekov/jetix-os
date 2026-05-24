---
title: Diagrams INDEX — research-methodology-2026-05-24
date: 2026-05-24
type: diagrams-index
phase: 9
prose_authored_by: brigadier-scribe
F: F2 (synthesis-visualisation)
G: research-methodology
constitutional_posture: R1 surface only + R6 + append-only
total_diagrams: 14
---

# Diagrams INDEX — research-methodology-2026-05-24

> **14 mermaid diagrams** structuring methodology research findings.
> Visualise per-phase synthesis + cross-tradition convergence + Jetix
> positioning options. Substantiates main DR document.

---

## D1 — 12 traditions cross-cite landscape

```mermaid
mindmap
  root((Methodology<br/>research<br/>2026-05-24))
    Russian tradition T1+T6
      ММК 1954
      Щедровицкий
      ОДИ format
      СМД-методология
      Левенчук continuator
    Heuristics + tacit T2+T3
      Polya 1945
      Polanyi 1958/66
      Pragmatism Peirce/James/Dewey
    Systems thinking T4+T5
      Senge 5 disciplines
      Beer VSM
      Ashby variety
      Meadows LP12
      Bateson logical type
      Maturana-Varela
    Reflective practice T7+T8+T11
      Schön practicum
      Ericsson 10000h
      Dreyfus 5-stage
      Merleau-Ponty body
    Software T10
      Dijkstra structured
      Knuth literate
      Brooks NSB
      Unix philosophy
      Karpathy LLM-OS
    Method engineering T12
      Brinkkemper SME 1996
      ISO/IEC 24744
      SEMAT 2009
      OMG Essence 2.0:2024
```

---

## D2 — Левенчук Methodology 2025 — 33 concepts mindmap (Phase 1)

```mermaid
mindmap
  root((Левенчук<br/>Методология<br/>2025))
    Метод как 1st-class object
      Sigнатура
      Альфа граф состояний
      Чеклист альфы
    Constructor theory Deutsch
      Universal constructor
      Hybrot vs cyborg
      IPU information-processing
    Стратегирование
      4 шага алгоритм
      Метод выбора метода
      Policy vs Plan
    Безмасштабность
      Молекула - корпорация
      Anti-anthropocentric
      3-е поколение
    SoTA tracking
      Discipline + tooling + subjects
      Всё новое сбоку
      VUCA context
    OMG Essence standard
      ISO/IEC 24744
      SEMAT initiative
      Brinkkemper SME
    Прагматический поворот
      Peirce abductive
      Dewey inquiry
      Polanyi tacit ack
```

---

## D3 — Polya 4-phase + heuristic catalogue (Phase 2)

```mermaid
graph TD
    Start[Problem encountered] --> P1
    P1[Phase 1: Understanding the problem<br/>What is unknown? Data? Condition?] --> P2
    P2[Phase 2: Devising a plan<br/>Related problem? Restate? Auxiliary?] --> Heuristic
    Heuristic[Heuristic catalogue 25 patterns<br/>Analogy / Working backwards / Variation /<br/>Specialisation / Generalisation / Decomposing] --> P3
    P3[Phase 3: Carrying out the plan<br/>Check each step] --> P4
    P4[Phase 4: Looking back<br/>Verify, derive differently, generalise] --> End
    End[Solution + learning]
    P4 -.feedback.-> P1
    style P1 fill:#e1f5ff
    style P2 fill:#fff3e0
    style P3 fill:#e8f5e8
    style P4 fill:#f3e5f5
```

---

## D4 — Polanyi tacit knowing structure (proximal-distal, Phase 2)

```mermaid
graph LR
    subgraph proximal[Proximal term]
        Features[Particulars / subsidiary cues<br/>= what we are unable to specify]
    end
    subgraph distal[Distal term]
        Whole[Comprehensive entity<br/>= what we attend to]
    end
    Features -.attend FROM.-> Whole
    Features ==> Whole
    Whole --semantic displacement--> Out[Meaning located at tip<br/>like blind man's stick]
    style Features fill:#fff3e0
    style Whole fill:#e8f5e8
    style Out fill:#f3e5f5
```

---

## D5 — Beer VSM 5-system architecture (Phase 3)

```mermaid
graph TD
    S5[S5 Policy / Identity<br/>Owner + Pillar A + Constitutional]
    S4[S4 Intelligence<br/>sota-tracker / autoresearch / brain-lead]
    S3[S3 Operations Mgmt<br/>brigadier dispatch / manager / sales-lead]
    S3star[S3* Audit<br/>meta-agent / cycle-end / lint hooks]
    S2[S2 Coordination<br/>mailboxes / CLAUDE.md / voice pipeline]
    S1[S1 Implementation<br/>Owner deep work / projects / workshops]

    S5 --identity + ethos--> S4
    S5 --identity + ethos--> S3
    S4 --strategic intelligence--> S3
    S3 --resource allocation--> S2
    S3 --audit--> S3star
    S2 --coordination--> S1
    S1 --algedonic emergency--> S5

    style S5 fill:#f3e5f5
    style S4 fill:#e1f5ff
    style S3 fill:#fff3e0
    style S2 fill:#e8f5e8
    style S1 fill:#fce4ec
```

---

## D6 — Meadows 12 leverage points hierarchy + Jetix mapping (Phase 3)

```mermaid
graph TD
    LP1[LP1 Transcend paradigms<br/>OWNER-ONLY]
    LP2[LP2 Paradigm<br/>VISION-FUNDAMENTAL + FPF]
    LP3[LP3 Goals<br/>strategic prose owner-only]
    LP4[LP4 Self-organise<br/>Role Taxonomy + IP-1]
    LP5[LP5 Rules<br/>Default-Deny + R12 LOCK + Pillar C 12]
    LP6[LP6 Info flows<br/>State Persistence + Wiki + Mailboxes]
    LP7[LP7 Positive loops]
    LP8[LP8 Negative loops]
    LP9[LP9 Delays]
    LP10[LP10 Stocks & flows structure]
    LP11[LP11 Buffer capacity]
    LP12[LP12 Parameters / constants<br/>operational tuning]

    LP1 ==strongest==> LP2
    LP2 ==> LP3
    LP3 ==> LP4
    LP4 ==> LP5
    LP5 ==> LP6
    LP6 ==> LP7
    LP7 ==> LP8
    LP8 ==> LP9
    LP9 ==> LP10
    LP10 ==> LP11
    LP11 ==weakest==> LP12

    style LP1 fill:#f3e5f5
    style LP2 fill:#e1f5ff
    style LP3 fill:#fff3e0
    style LP12 fill:#fce4ec
```

---

## D7 — Schön reflective practice triple (Phase 4)

```mermaid
graph LR
    K[Knowing-in-action<br/>tacit embedded competence]
    R1[Reflection-in-action<br/>mid-action thinking on action]
    R2[Reflection-on-reflection-in-action<br/>meta-reflection after action]

    K --surprise / failure / breakdown--> R1
    R1 --improvise + restructure--> K
    R1 --after action--> R2
    R2 --updated practice repertoire--> K

    Indet[Indeterminate zones:<br/>uncertainty / uniqueness / value conflict]
    Indet --triggers--> R1

    style K fill:#e8f5e8
    style R1 fill:#fff3e0
    style R2 fill:#f3e5f5
    style Indet fill:#fce4ec
```

---

## D8 — Software methodology lineage timeline (Phase 5)

```mermaid
timeline
    title Software methodology lineage
    1968 : Dijkstra GOTO Considered Harmful
         : Knuth TAOCP vol 1
    1969 : Thompson + Ritchie Unix
         : Dijkstra A Short Intro to Art of Programming
    1971 : EWD 316 published
    1975 : Brooks Mythical Man-Month
    1984 : Knuth Literate Programming
    1986 : Brooks No Silver Bullet
    1996 : Brinkkemper SME founding paper
    1998 : Brinkkemper-Saeki assembly techniques
    2003 : Raymond Art of Unix Programming
    2008 : Martin Clean Code
    2014 : OMG Essence Kernel 1.0
         : ISO/IEC 24744 v2014
    2017 : Karpathy Software 2.0 essay
    2023 : Karpathy LLM-OS intro
    2024 : OMG Essence Kernel 2.0
         : Левенчук Системное Мышление + Методология
```

---

## D9 — Russian methodology tradition lineage (Phase 6)

```mermaid
graph TD
    Vyg[Выготский 1896-1934<br/>cultural-historical psychology]
    Leont[Леонтьев 1903-1979<br/>Activity Theory]
    MMK[ММК Москва 1954<br/>Щедровицкий + Зиновьев<br/>+ Мамардашвили + Грушин]

    Vyg --activity-ontology--> Leont
    Leont --inheritance + critique--> MMK
    MMK --1979+--> ODI[ODI Organisational<br/>Activity Games<br/>73 games by 1989]
    MMK --1970s+--> SMD[СМД Системо-Мысле-<br/>Деятельностная methodology]

    SMD --1994 Щедровицкий death--> P1[П.Г.Щедровицкий<br/>orthodox continuator]
    SMD --pragmatic adapter--> P2[Попов + Reframing Group<br/>strategic consulting]
    SMD --modernised + standards--> P3[ЛЕВЕНЧУК ШСМ<br/>3-е поколение systems]

    P3 --indirect inspiration--> JETIX[JETIX<br/>multi-tradition convergence<br/>+ R12 + AI-substrate + cohort]

    style MMK fill:#e1f5ff
    style SMD fill:#fff3e0
    style P3 fill:#e8f5e8
    style JETIX fill:#f3e5f5
```

---

## D10 — Method Engineering convergent 6-step pattern (Phase 7)

```mermaid
graph LR
    S1[1 Bound method scope<br/>Foundation Parts 1-11]
    S2[2 Decompose into fragments<br/>Wiki 9 entity types + cycles]
    S3[3 Specify alpha state-graphs<br/>Hypothesis Architecture 7-layer]
    S4[4 Compose situationally<br/>KM MVP project-bootstrap --type=4]
    S5[5 Monitor + audit<br/>cycle hooks + lint + Default-Deny + R12]
    S6[6 Reflect + adapt<br/>Cycle end-reflection + meta-agent + SoTA]

    S1 --> S2
    S2 --> S3
    S3 --> S4
    S4 --> S5
    S5 --> S6
    S6 -.iteration.-> S1

    style S1 fill:#e1f5ff
    style S2 fill:#fff3e0
    style S3 fill:#e8f5e8
    style S4 fill:#f3e5f5
    style S5 fill:#fce4ec
    style S6 fill:#fff8e1
```

---

## D11 — Jetix multi-tradition convergence (Phase 8 §2)

```mermaid
graph TD
    JETIX((JETIX<br/>methodology<br/>substrate))

    T1[T1 Russian methodology<br/>HIGH 87% overlap]
    T4[T4 Cybernetics<br/>HIGH]
    T5[T5 Systems thinking<br/>HIGH]
    T9[T9 Pragmatism<br/>HIGH]
    T10[T10 Software methodology<br/>HIGH]
    T12[T12 Method engineering<br/>HIGH]

    T2[T2 Polya heuristics<br/>MEDIUM]
    T3[T3 Polanyi tacit<br/>MEDIUM-HIGH]
    T6[T6 Bateson<br/>MEDIUM]
    T7[T7 Schön<br/>MEDIUM]

    T8[T8 Ericsson<br/>MEDIUM-LOW]
    T11[T11 Phenomenology embodiment<br/>LOW - CRITICAL GAP]

    T1 ==> JETIX
    T4 ==> JETIX
    T5 ==> JETIX
    T9 ==> JETIX
    T10 ==> JETIX
    T12 ==> JETIX
    T2 --> JETIX
    T3 --> JETIX
    T6 --> JETIX
    T7 --> JETIX
    T8 -.weak.-> JETIX
    T11 -.GAP.-> JETIX

    style JETIX fill:#f3e5f5
    style T11 fill:#ffcdd2
    style T1 fill:#c8e6c9
    style T4 fill:#c8e6c9
    style T5 fill:#c8e6c9
    style T9 fill:#c8e6c9
    style T10 fill:#c8e6c9
    style T12 fill:#c8e6c9
```

---

## D12 — Jetix 4 lineage positioning options (Phase 8 §3)

```mermaid
graph TD
    Question[R1 — Owner question:<br/>Where is Jetix in methodology landscape?]

    A[Option A<br/>Левенчук-continuator<br/>+ R12 distinctive]
    B[Option B<br/>Parallel extension<br/>of Russian tradition]
    C[Option C<br/>Fully hybrid<br/>multi-source synthesis]
    D[Option D<br/>Method-engineering<br/>practice not methodology]

    Question --> A
    Question --> B
    Question --> C
    Question --> D

    A --strengths--> A1[Clear lineage / Russian academic credit / reduces yet-another-methodology critique]
    A --weaknesses--> A2[Dependent on Левенчук trajectory / understates Jetix-distinctive / Russian-language constraint]
    B --strengths--> B1[Acknowledges Jetix-distinctive 6 contributions / International addressability / R12 central]
    B --weaknesses--> B2[Requires substantiation history / may appear pretentious / lose Russian-methodology lineage prestige]
    C --strengths--> C1[Most honest / not committed to single politics / cross-cultural easiest]
    C --weaknesses--> C2[Easy to call eclectic / less brand-clarity / less narrative depth]
    D --strengths--> D1[Lower stakes / more defensible / SME-grounded]
    D --weaknesses--> D2[Less brand power / method-engineering obscure terminology]

    style Question fill:#f3e5f5
```

---

## D13 — Jetix 5 strategic positioning paths (Phase 8 §5)

```mermaid
graph LR
    JETIX((Jetix<br/>R1 path<br/>choice))

    P1[Path 1<br/>Continuator<br/>Russian-academic<br/>HIGH Левенчук dep<br/>12-24mo]
    P2[Path 2<br/>International ME<br/>Global English<br/>LOW dep / 6-12mo]
    P3[Path 3<br/>Crypto-native<br/>DAO + R12 central<br/>LOW dep / 6-12mo]
    P4[Path 4<br/>Multi-track<br/>All 3 audiences<br/>MED dep / 12-18mo]
    P5[Path 5<br/>Slow-build<br/>Own school<br/>LOW dep / 5-7yr]

    JETIX --> P1
    JETIX --> P2
    JETIX --> P3
    JETIX --> P4
    JETIX --> P5

    style JETIX fill:#f3e5f5
    style P1 fill:#e1f5ff
    style P2 fill:#fff3e0
    style P3 fill:#e8f5e8
    style P4 fill:#fce4ec
    style P5 fill:#fff8e1
```

---

## D14 — Jetix 5 extension proposals + 5 critical gaps (Phase 8 §6+§7)

```mermaid
graph TD
    JETIX((JETIX<br/>methodology<br/>2-way exchange))

    JETIX --Extensions OUT<br/>to tradition--> EXT
    JETIX --Gaps OWN<br/>to be addressed--> GAP

    EXT[Extension proposals]
    EXT --> E1[E1 R12 anti-extraction<br/>constitutional methodology layer]
    EXT --> E2[E2 Welcome-frame<br/>design discipline]
    EXT --> E3[E3 Notion-MVP-bypass<br/>filesystem-as-source-of-truth]
    EXT --> E4[E4 Cohort-target-ontology<br/>cohort as 1st-class system]
    EXT --> E5[E5 F-G-R triple lint-enforced<br/>grade-tracking per claim]

    GAP[Critical gaps]
    GAP --> G1[G1 Embodied skill dimension<br/>Workshop verbal-only]
    GAP --> G2[G2 Cohort stage-awareness<br/>one-pathway curriculum]
    GAP --> G3[G3 СМД-schematisation<br/>convention not adopted]
    GAP --> G4[G4 Levenchuk direct collaboration<br/>silent-inspiration only]
    GAP --> G5[G5 Praxeology layer<br/>absent foundational]

    style JETIX fill:#f3e5f5
    style EXT fill:#c8e6c9
    style GAP fill:#ffcdd2
```

---

## §0 Diagrams summary table

| # | Title | Phase | Type | Notes |
|---|---|---|---|---|
| D1 | 12 traditions cross-cite | 0 | mindmap | Phase landscape preview |
| D2 | Левенчук 33 concepts | 1 | mindmap | Methodology 2025 distillation |
| D3 | Polya 4-phase + heuristics | 2 | graph | Problem-solving template |
| D4 | Polanyi proximal-distal | 2 | graph | Tacit knowing structure |
| D5 | Beer VSM 5-system + Jetix mapping | 3 | graph | Viable system architecture |
| D6 | Meadows LP12 + Jetix | 3 | graph | Leverage points hierarchy |
| D7 | Schön reflective triple | 4 | graph | Knowing-in-action / reflection-in-action / -on- |
| D8 | Software methodology timeline | 5 | timeline | 1968-2024 lineage |
| D9 | Russian methodology lineage | 6 | graph | ММК → Левенчук → Jetix |
| D10 | Method Engineering 6-step | 7 | graph | Convergent pattern |
| D11 | Jetix multi-tradition convergence | 8 | graph | Convergence levels |
| D12 | 4 lineage positioning options | 8 | graph | Options A-D с strengths/weaknesses |
| D13 | 5 strategic positioning paths | 8 | graph | Paths 1-5 audience/timing |
| D14 | 5 extensions + 5 gaps | 8 | graph | Outbound contributions + inbound gaps |

**Total: 14 diagrams. Target 10-15 met.** Все diagrams Phase 0-8 substantiated.

---

*Diagrams INDEX closure. ~280 lines. 14 mermaid diagrams. R6 provenance per
diagram inherits Phase-attribution.*
