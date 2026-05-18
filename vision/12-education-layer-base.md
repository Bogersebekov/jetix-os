---
title: Education Layer Base — Базовое системное мышление через Workshop
date: 2026-05-18
type: vision-theme
status: brigadier-structured (R1 surface-only)
authored_by: ruslan-via-voice-dictation+brigadier-structured
prose_authored_by: ruslan-via-voice-dictation+brigadier-structured
parents:
  - raw/voice-memos-2026-05-17-batch/text_009@2026-05-18_evening.md (Thread 6 + 8)
  - decisions/strategic/JETIX-EDUCATION-LAYER-SYSTEM-THINKING-2026-05-18.md (concept doc E)
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md (Workshop LOCKED)
  - research/harari-jetix-lens-2026-05-18/03-21-lessons.md (4 Cs P1#1)
constitutional_posture: R1 surface + R6 + R11 + R12 anti-extraction + EP-5 + paternalism mitigation
F: F2
G: vision-education-layer-base
R: refuted_if_curriculum_lacks_systems-thinking_OR_4Cs_misalignment_OR_paternalism_complaint_unmitigated
language: russian + english
word_budget: 1500
---

# Education Layer Base — Системное мышление

> Companion vision document — plain English + FPF formal. Cross-links concept doc E + Harari 4 Cs corroboration.

---

## §1 Plain English (Russian primary)

text_009 Thread 6: «эта платформа будет обучать этому ну то есть кому-то системному мышлению адекватному подходу к и как-то и и потом стремиться на то чтобы вот у всех людей был вот этот базовый уровень закрыт». Education layer = базовое системное образование через Workshop curriculum + Hackathon как teaching vehicle.

**Workshop curriculum tier structure:**
- **Tier 1 Foundation** — Meadows leverage points / Ashby variety / Senge laws / Kauffman adjacent-possible.
- **Tier 2 Methodology** — NASA SE 15-of-17 / TPS Hansei + Kaizen / Pattern Language / FPF discipline.
- **Tier 3 Specialization** — Hackathon participation = applied learning vehicle; mentor pairing.
- **Tier 4 Master apprenticeship** — Master Workshop of Engineers (Thread 14 «не ступеньки ниже»).

**Harari 4 Cs alignment** (research/harari-jetix-lens P1#1):
- Critical thinking — «×100 multiplier» semantics analysis.
- Communication — FPF discipline + outreach personalization.
- Collaboration — hackathon team formation + mentor pairing.
- Creativity — solution innovation per hackathon.

**NASA framework integration** (Thread 8): «life-as-spaceship» — personal life-design = systems engineering project. NASA SE processes (Stakeholder Expectations / Requirements / Logical Decomposition / Implementation / Integration / Verification / Technical Assessment) applied к persona scale.

**Paternalism risk (phil critic per batch-3 §B.3):** Workshop curriculum = **opt-in voluntary**; не universalist mandate. R12 anti-extraction = fork-and-leave preserved. «Базовое образование» = aspiration, не enforcement.

---

## §2 FPF formal version

```
System: Jetix-education-layer (A.1)
  Method: Системное мышление curriculum + NASA SE + Pattern Language (A.3)
  Roles: Student / Master / Teacher (A.2; apprenticeship roles)
  Work-as-process: curriculum progression (Tier 1 → 4) (A.16)
  Epistemic role-type: U.Episteme (knowledge transmission)
  Method documentation: U.MethodDescription (curriculum canonical)
  Speech-Acts: lecture / dialogue / Socratic (U.SpeechAct)
  
  Tier structure (A.3 method sub-decomposition):
    Tier 1 Foundation:
      - Meadows leverage points
      - Ashby requisite variety
      - Beer VSM basics
      - Senge 11 laws
      - Kauffman adjacent-possible
    Tier 2 Methodology:
      - NASA SE 15-of-17 processes (life-as-spaceship)
      - TPS Hansei + Kaizen
      - Pattern Language method
      - FPF discipline
    Tier 3 Specialization:
      - Hackathon = applied learning vehicle
      - Mentor pairing (TPS pattern)
      - Domain-specific deepening
    Tier 4 Master apprenticeship:
      - Master Workshop of Engineers
      - Cohort multi-year engagement
      - Medieval guild model + ШСМ 30-year precedent
  
  Constitutional posture (A.14):
    - R12 anti-extraction (opt-in voluntary)
    - Paternalism mitigation (phil critic surface preserved)
    - AP-6 dissent preservation in curriculum feedback
```

---

## §3 Mermaid — Education layer flow

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TB
    subgraph "Entry — Hackathon Participation"
        E1[First Hackathon Event]
        E2[Solution Artefact Produced]
        E3[Reflection Cycle TPS Hansei]
    end
    
    subgraph "Tier 1 Foundation — Systems Thinking"
        T1[Meadows Leverage Points]
        T2[Ashby Requisite Variety]
        T3[Senge 11 Laws]
        T4[Kauffman Adjacent-Possible]
    end
    
    subgraph "Tier 2 Methodology"
        M1[NASA SE 15-of-17]
        M2[TPS Hansei + Kaizen]
        M3[Pattern Language]
        M4[FPF Discipline]
    end
    
    subgraph "Tier 3 Specialization"
        S1[Hackathon Applied Learning]
        S2[Mentor Pairing TPS]
        S3[Domain-Specific Mastery]
    end
    
    subgraph "Tier 4 Master Apprenticeship"
        MA1[Master Workshop of Engineers]
        MA2[Multi-year Cohort]
        MA3[Quality Predicate ШСМ-style]
    end
    
    subgraph "Harari 4 Cs Alignment"
        C1[Critical Thinking]
        C2[Communication]
        C3[Collaboration]
        C4[Creativity]
    end
    
    subgraph "Constitutional Guards"
        G1[R12 Opt-in Voluntary]
        G2[Paternalism Mitigation]
        G3[Fork-and-Leave Preserved]
    end
    
    E1 --> E2
    E2 --> E3
    E3 --> T1
    T1 --> T2
    T2 --> T3
    T3 --> T4
    T4 --> M1
    M1 --> M2
    M2 --> M3
    M3 --> M4
    M4 --> S1
    S1 --> S2
    S2 --> S3
    S3 --> MA1
    MA1 --> MA2
    MA2 --> MA3
    
    T1 -.-> C1
    M4 -.-> C2
    S2 -.-> C3
    S3 -.-> C4
    
    G1 -.->|enforces| E1
    G2 -.->|enforces| T1
    G3 -.->|enforces| MA1
    
    style E1 fill:#d6f0d6
    style MA1 fill:#ffd6a6
    style G1 fill:#ffd6d6
    style G2 fill:#ffd6d6
    style G3 fill:#ffd6d6
```

---

## §4 Cross-refs

- `decisions/strategic/JETIX-EDUCATION-LAYER-SYSTEM-THINKING-2026-05-18.md` (concept doc E)
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` (Workshop LOCKED parent)
- `research/harari-jetix-lens-2026-05-18/03-21-lessons.md` P1#1 (4 Cs)
- `research/deepening-2026-05-18/12-nasa-se-15-of-17.md` (NASA SE precedent)
- `research/deepening-2026-05-18/05-pattern-language-lineage.md` (Alexander → Cunningham → Karpathy)
- `wiki/concepts/education-layer-systems-thinking.md` (Tier A)
- `vision/03-jetix-as-masterskaya-platform.md` §APPEND (Workshop = master of info processing + 4 Cs overlay)

[src: text_009 Thread 6+8 verbatim + concept doc E + research streams (Harari + Deepening) + batch-3 analysis]
