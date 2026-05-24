---
title: Diagrams INDEX — Левенчук Master Qualification Research
date: 2026-05-23
type: diagrams-index
parent: prompts/levenchuk-master-qualification-research-2026-05-23.md
language: russian primary
diagram_count: 15
---

# Diagrams INDEX — 15 Mermaid Visualizations

> **15 mermaid diagrams** (each ≥6 nodes target; multiple ≥10 nodes per §11.0 mandate).
> Each diagram inline in this index с context + cross-cite Phase.

---

## §1 Master Qualification flow (8 levels x 3 indicators)

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
flowchart TB
    subgraph Indicators[3 Core Indicators]
        Agency[Агентность<br/>EPA L1-L5]
        Scale[Масштаб<br/>я → команда → коллектив<br/>→ сообщество → цивилизация]
        Method[Методологическая<br/>дисциплина<br/>SoTA + Парето-фронт]
    end

    subgraph Levels[8 Quals Levels EQF rough]
        L1[L1 Ученик<br/>EQF 1-2<br/>1.5-2h/day]
        L2[L2 Работник<br/>EQF 3-4<br/>org goals]
        L3[L3 Стратег<br/>EQF 5<br/>система мышление]
        L4[L4 Специалист<br/>EQF 6<br/>обобщённый процесс]
        L5[L5 Практик<br/>EQF 7<br/>до 10 чел]
        L6[L6 Мастер<br/>EQF 7-8<br/>предлагает улучшения]
        L7[L7 Реформатор<br/>EQF 8+<br/>сообщество культура]
        L8[L8 Революционер<br/>beyond EQF<br/>цивилизация]
    end

    Agency -.measures.-> L1
    Agency -.measures.-> L8
    Scale -.measures.-> L1
    Scale -.measures.-> L8
    Method -.measures.-> L1
    Method -.measures.-> L8

    L1 --> L2 --> L3 --> L4 --> L5 --> L6 --> L7 --> L8

    style L6 fill:#ffd6d6
    style L7 fill:#ffe0a0
    style L8 fill:#d6f0d6
```

**Source:** Phase 1 §3-§4. **Decoded:** 3 ortho indicators × 8 levels = Goodhart-resistant measurement framework.

---

## §2 R0-R10 residency curriculum graph

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333'}}}%%
flowchart LR
    R0[R0 Личное развитие<br/>Рациональная работа<br/>6 wk / no prereq]
    R1[R1 Распожаризация<br/>6 wk / open admission]
    R2[R2 Моделирование<br/>communicaton + leadership]
    R3[R3 Рабочее моделирование<br/>engineering + mgmt]
    R4[R4 Причинность<br/>интервенции counterfactuals]
    R5[R5 Системное мышление<br/>← CORE entry / 6 wk]
    R6[R6 Системное моделирование]
    R7[R7 Методология<br/>872 pp Методология 2025]
    R8[R8 Системная инженерия<br/>INCOSE + ISO]
    R9[R9 Инженерия мастерства<br/>renamed 2026<br/>was Инженерия личности]
    R10[R10 Системный менеджмент<br/>TOC + Goldratt]
    Cert[Certification<br/>open/closed defense<br/>Methsovet decision]
    Master[Мастер 2026 года<br/>3 года valid]

    R0 --> R1 --> R2 --> R3 --> R4 --> R5
    R5 --> R6 --> R7 --> R8
    R7 --> R9
    R7 --> R10
    R8 --> Cert
    R9 --> Cert
    R10 --> Cert
    Cert --> Master

    style R5 fill:#ffd6d6
    style R7 fill:#ffd6d6
    style Master fill:#d6f0d6
```

**Source:** Phase 2 §3 + Phase 6 §2. **Decoded:** Linear R0-R7, then split R8/R9/R10 then cert. 60+ weeks group format.

---

## §3 Books × Aisystant × R# × Quals correspondence

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
    subgraph Books[9 Active Books]
        B1[Системное мышление 2024<br/>Т1+Т2 / 900 pp]
        B2[Методология 2025<br/>872 pp]
        B3[Системная инженерия 2022]
        B4[Системный менеджмент 2023]
        B5[Инженерия личности 2023]
        B6[Интеллект-стек 2023]
        B7[Визуальное мышление 2018]
        B8[English ST 2020]
    end

    subgraph Aisystant[Aisystant courses]
        A1[Системное мышление]
        A2[Методология]
        A3[Системная инженерия]
        A4[Системный менеджмент]
        A5[Инженерия мастерства]
        A6[Интеллект-стек]
    end

    subgraph Residency[R# Residency 6wk]
        Rr5[R5+R6]
        Rr7[R7]
        Rr8[R8]
        Rr10[R10]
        Rr9[R9]
        Rresearch[Research программа]
    end

    subgraph Quals[Quals]
        QL3[L3 Стратег]
        QL5[L5 Практик]
        QL6[L6 Мастер]
        QL8[L8 Революционер]
    end

    B1 --> A1 --> Rr5 --> QL3
    B2 --> A2 --> Rr7
    B3 --> A3 --> Rr8 --> QL5
    B4 --> A4 --> Rr10 --> QL6
    B5 --> A5 --> Rr9
    B6 --> A6 --> Rresearch --> QL8
    B7 -.companion.-> A1
    B8 -.intl.-> A1
```

**Source:** Phase 4 §12. **Decoded:** Books feed Aisystant courses, feed R# residencies, certify к Quals levels.

---

## §4 Cost + Time для Master path

```mermaid
%%{init: {'theme':'base'}}%%
flowchart LR
    subgraph SelfStudy[Self-Study Path]
        SS1[Aisystant subscription<br/>1K руб/мес × 36 мес = 36K]
        SS2[9 Books × 1K = 9K]
        SS3[~45K руб ≈ €450<br/>2160h / 36 мес<br/>NO certification]
    end

    subgraph GroupPath[Group Certified Path]
        GP1[10 residencies × 60K = 600K]
        GP2[Books × 9 ≈ 9K]
        GP3[~641K руб ≈ €6,400<br/>600-900h / 15-30 мес<br/>L6 Master certification]
    end

    subgraph HybridPath[Hybrid Path]
        HP1[R0-R4 self ~6K]
        HP2[R5-R10 group ~360K]
        HP3[~370K руб ≈ €3,700<br/>18-24 мес]
    end

    SS1 --> SS3
    SS2 --> SS3
    GP1 --> GP3
    GP2 --> GP3
    HP1 --> HP3
    HP2 --> HP3

    style GP3 fill:#ffd6d6
    style SS3 fill:#d6f0d6
    style HP3 fill:#ffe0a0
```

**Source:** Phase 6 §12. **Decoded:** Self-study cheapest (€450) but no cert; group fully certified €6,400; hybrid €3,700 middle path.

---

## §5 Левенчуковский book genealogy (annual rewrite cycle)

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
    SM2018[Системное мышление<br/>2018<br/>1st edition]
    SM2019[2019 ed]
    SM2020[2020 ed]
    SM2022[2022 ed]
    SM2023[Практическое<br/>системное мышление<br/>2023 / 8th rewrite]
    SM2024[Системное мышление<br/>2024 Том 1+2<br/>9th rewrite / 900 pp<br/>CURRENT]

    OE2021[Образование для<br/>образованных 2021]
    IS2023[Интеллект-стек 2023<br/>16-17 transdisciplines<br/>CURRENT]

    Methodology[Методология 2025<br/>872 pp / CURRENT]

    SE2022[Системная инженерия 2022]
    SM2023x[Системный менеджмент 2023]
    PE2023[Инженерия личности 2023]
    VT2018[Визуальное мышление 2018]

    SM2018 --> SM2019 --> SM2020 --> SM2022 --> SM2023 --> SM2024
    OE2021 --> IS2023

    style SM2024 fill:#d6f0d6
    style IS2023 fill:#d6f0d6
    style Methodology fill:#d6f0d6
```

**Source:** Phase 4 §1 + R-A §2.1. **Decoded:** Annual rewrite cycle exemplifies «непрерывное всё» applied к pedagogical materials.

---

## §6 МИМ ecosystem 12+ figures map

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
    subgraph Leadership[МИМ Leadership]
        Lev[Анатолий Левенчук<br/>Scientific Director<br/>⭐⭐⭐ Wave 1]
        Tseren[Церен Церенов<br/>Managing Partner<br/>⭐⭐⭐ Wave 1]
    end

    subgraph Masters[Master mentors 5]
        Chaikovskaya[Юлия Чайковская<br/>Internship Deployment]
        Agroskin[Виктор Агроскин<br/>INCOSE / ontology / ISO]
        Lubchenko[Анна Лубченко<br/>Curriculum Developer]
        Medvedeva[Прапион Медведева<br/>REFORMER<br/>Кочерга rationality<br/>⭐⭐⭐ R12 bridge]
        Mizgulin[Вячеслав Мизгулин<br/>SE / Cand Tech Sci]
    end

    subgraph External[External practitioners conf 2026]
        Gabdulin[Ilshat Gabdulin<br/>AI-agents practice<br/>⭐⭐⭐ ROY synergy]
        Batyrshin[Timur Batyrshin<br/>FPF service ontology]
        Podobed[Ivan Podobed<br/>Method engineering<br/>⭐⭐⭐ DR-38 anchor]
        Sergeev[Stanislav Sergeev<br/>IWE agro consulting]
        Sultanova[Liya Sultanova<br/>Pre-school intellect-stack]
    end

    Lev ===> Masters
    Tseren ===> Masters
    Masters -.mentor.-> External

    Medvedeva -.affil.-> Kocherga[Кочерга<br/>Moscow rationality]

    style Lev fill:#ffd6d6
    style Tseren fill:#ffd6d6
    style Medvedeva fill:#ffd6d6
    style Gabdulin fill:#ffd6d6
    style Podobed fill:#ffd6d6
```

**Source:** Phase 5 §1-§15. **Decoded:** 5 ⭐⭐⭐ HIGHEST Wave 1 candidates: Левенчук + Tseren + Медведева + Gabdulin + Podobed.

---

## §7 Intellect-stack 16 transdisciplines layered

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
    subgraph Engineering[Engineering layer]
        SE[Инженерия]
    end

    subgraph Methodology[Methodology layer]
        Rhe[Риторика]
        Eth[Этика]
        Aes[Эстетика]
        Res[Исследования]
        Met[Методология]
    end

    subgraph Foundations[Foundation layer]
        Sob[Собранность]
        Rat[Рациональность]
        Ont[Онтология]
        Sem[Семантика]
        TP[Теория понятий]
        Pon[Понятизация]
    end

    subgraph Sciences[Sciences layer]
        Alg[Алгоритмика]
        Mat[Математика]
        Phy[Физика]
        Log[Логика]
    end

    Foundations --> Methodology
    Sciences --> Methodology
    Methodology --> Engineering
```

**Source:** Phase 4 §7.3 (Интеллект-стек 2023 + system-school.ru/stack). **Decoded:** 4 layers / 16 transdisciplines = replaces STEM as 21st-century professional standard.

---

## §8 FPF + SPF emergence pattern

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
    FPF[FPF First Principles<br/>Framework<br/>github.com/ailev/FPF<br/>370 stars / 63 forks<br/>300+ patterns]

    subgraph SPFs[SPF Second Principles Frameworks<br/>11% engineers built own]
        SPF1[Domain SPF 1<br/>e.g., evolutionary stylistics]
        SPF2[Domain SPF 2<br/>e.g., service ontology]
        SPF3[Domain SPF 3<br/>e.g., agricultural consulting]
        JetixSPF[Jetix SPF candidate<br/>AI-consulting + Personal-OS<br/>R12 anti-extraction]
    end

    MCP[MCP server<br/>fpf.sh + mcp.fpf.sh<br/>May 2026 launch]

    Codex[Codex App<br/>GPT-5.5]

    FPF -.programmatic access.-> MCP
    FPF -.AI-agent consumption.-> Codex
    FPF -.domain extension.-> SPFs
    JetixSPF -.feedback.-> FPF

    style FPF fill:#ffd6d6
    style JetixSPF fill:#d6f0d6
```

**Source:** Phase 3 §4 + Phase 7 §3 Proposal 9. **Decoded:** Jetix может formalise as Jetix-SPF for AI-consulting / Personal-OS / R12 domain.

---

## §9 Quality procedure (3-indicator measurement multi-mentor)

```mermaid
%%{init: {'theme':'base'}}%%
flowchart LR
    Resident[Resident<br/>real work project]
    Mentor1[Mentor 1<br/>Mirror feedback<br/>literal quote-back]
    Mentor2[Mentor 2<br/>different context]
    Mentor3[Mentor 3<br/>different time]
    Cohort[Cohort group<br/>peer attestation]
    Methsovet[Methsovet МИМ<br/>collegial decision]

    Resident --> Mentor1
    Resident --> Mentor2
    Resident --> Mentor3
    Mentor1 -.mismatch reveal.-> Resident
    Mentor2 -.mismatch reveal.-> Resident
    Mentor3 -.mismatch reveal.-> Resident
    Cohort -.peer attest.-> Methsovet
    Mentor1 --> Methsovet
    Mentor2 --> Methsovet
    Mentor3 --> Methsovet
    Methsovet ==>|Quals decision<br/>open or closed defense| Cert[Qual cert<br/>3 yrs valid]

    style Cert fill:#d6f0d6
```

**Source:** Phase 1 §5 + qualification page. **Decoded:** 3-4 mirror events + cohort + Methsovet = subjective bias defused.

---

## §10 Jetix subsystems × ШСМ cross-pollination 32 proposals

```mermaid
%%{init: {'theme':'base'}}%%
flowchart LR
    subgraph JetixSub[Jetix Subsystems]
        Wiki[Wiki v2<br/>4 proposals]
        Foundation[Foundation Arch<br/>5 proposals]
        Workshop[Workshop format<br/>4 proposals]
        Hypothesis[Hypothesis Arch<br/>3 proposals]
        Method[METHOD V2 + DR-38<br/>3 proposals]
        ROY[ROY swarm<br/>3 proposals]
        R12[R12 substrate<br/>3 proposals]
        CRM[CRM<br/>2 proposals]
        Voice[Voice pipeline<br/>2 proposals]
        Cross[Cross-cutting<br/>3 proposals]
    end

    subgraph SourceSubstrate[ШСМ Source]
        FPF2[FPF 300+ patterns]
        IS[16 transdisciplines]
        Alpha[Alpha state machines]
        Method2[Methodology 3 approaches]
        Methsovet2[Methsovet pattern]
        SPFp[SPF emergence pattern]
        IWE[IWE patterns]
        EQF[EQF rough mapping]
        Indicator[3 indicator framework]
        Cohort2[Cohort + multi-mentor]
    end

    FPF2 -.->Wiki
    FPF2 -.->Foundation
    IS -.->Wiki
    IS -.->Cross
    Alpha -.->Wiki
    Alpha -.->Hypothesis
    Method2 -.->Wiki
    Method2 -.->Method
    Methsovet2 -.->Foundation
    SPFp -.->Foundation
    SPFp -.->Hypothesis
    SPFp -.->ROY
    IWE -.->ROY
    EQF -.->Foundation
    EQF -.->CRM
    Indicator -.->Workshop
    Indicator -.->ROY
    Cohort2 -.->Workshop
    Cohort2 -.->R12
```

**Source:** Phase 7 §1-§12 (32 proposals total). **Decoded:** Every Jetix subsystem has ≥2 cross-pollination opportunity.

---

## §11 Jetix offer matrix 5 tiers × R12 risk

```mermaid
%%{init: {'theme':'base'}}%%
flowchart LR
    subgraph T0[T0 Lowest]
        T01[Conf attendance<br/>+ talk 2027]
    end
    subgraph T1[T1 Low]
        T11[Cross-cite]
        T12[Methsovet observer]
        T13[Wiki stack share]
        T14[Book review]
        T15[Mutual cohort discount]
    end
    subgraph T2[T2 Medium]
        T21[Joint paper SPF]
        T22[Joint AI study]
        T23[Methodology workshop]
    end
    subgraph T3[T3 Med-High]
        T31[Joint cohort PILOT]
        T32[Alumni pipeline]
    end
    subgraph T4[T4 Highest]
        T41[Jetix-as-SPF<br/>institutional status<br/>⚠️ R12 HIGH]
    end

    T0 -->|low R12| T1 -->|low R12| T2 -->|R12 contracts| T3 -->|R12 careful| T4

    style T01 fill:#d6f0d6
    style T11 fill:#d6f0d6
    style T41 fill:#ffd6d6
```

**Source:** Phase 8 §2-§7. **Decoded:** Slow-thaw sequence T0 → T4 preserving R12 health.

---

## §12 5 Strategic Paths comparison

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
    Start[Ruslan decision frame:<br/>Personal Master + MIM integration]

    PathA[PATH A<br/>Personal Master + High MIM<br/>€7K personal / Tier 0-3<br/>15+ proposals adopted]
    PathB[PATH B<br/>Personal Master + Medium MIM<br/>€7K personal / Tier 0-1<br/>~8 proposals adopted]
    PathC[PATH C<br/>No personal + Deep MIM<br/>€100 R0 / Tier 0-4 long<br/>Jetix-as-SPF positioning]
    PathD[PATH D<br/>Self-study + Low MIM<br/>€110 / Tier 0-1<br/>3-5 proposals]
    PathE[PATH E<br/>Skip both<br/>€60 R0 only / Tier 0-1 light<br/>Maximum independence]

    Start --> PathA
    Start --> PathB
    Start --> PathC
    Start --> PathD
    Start --> PathE

    PathA -.outcome.-> OA[Max institutional credibility<br/>Cert 2027/28]
    PathB -.outcome.-> OB[Personal cred + Jetix indep]
    PathC -.outcome.-> OC[Ecosystem integration<br/>NO personal cert]
    PathD -.outcome.-> OD[Knowledge baseline<br/>NO cert]
    PathE -.outcome.-> OE[Max time/cash preserved<br/>Light bridge maintained]

    style PathA fill:#ffd6d6
    style PathC fill:#ffd6d6
    style PathE fill:#d6f0d6
```

**Source:** Phase 9 §2-§7. **Decoded:** 5 distinct paths surfaced; Ruslan chooses; brigadier NOT recommend.

---

## §13 Pedagogical evolution 2012 → 2026

```mermaid
%%{init: {'theme':'base'}}%%
timeline
    title МИМ Pedagogical Evolution
    2012 : OMG Essence kernel<br/>competency levels theory
    2015 : ШСМ founded<br/>Levenchuk + Tseren
    2017 : 6-day short-form courses
    2018 : Sys Thinking 2018 1st ed<br/>Annual rewrite cycle begins
    2020 : English Sys Thinking 2020<br/>Coursera course
    2021 : 7-alpha course schema<br/>Мастерство = alpha
    2024 : Sys Thinking 2024 Т1+Т2<br/>9th rewrite
    2025 : ШСМ rebrand → МИМ<br/>3 multi-month programs
    2026 : 10 atomic R1-R10 residencies<br/>3-indicator x 8-level quals<br/>FPF MCP launch<br/>10th conf
```

**Source:** Phase 3 §8.1-§8.3. **Decoded:** Annual evolution; 14-year arc.

---

## §14 R12 paired-frame 8-item checklist

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
    R12[R12 anti-extraction<br/>Tier 2 LOCKED 2026-05-12]
    
    subgraph Checklist[8-item compliance check per offer]
        I1[1. Wage-ratio ≤ 6:1<br/>Mondragón cap]
        I2[2. Fork-and-leave<br/>guarantee]
        I3[3. Revenue share<br/>transparency QF]
        I4[4. No extraction<br/>beyond agreed]
        I5[5. Consensual<br/>distribution]
        I6[6. Symmetric<br/>give-take]
        I7[7. R12 dissent<br/>welcome Halt-Log-Alert]
        I8[8. Audit trail<br/>append-only]
    end

    R12 ==> I1
    R12 ==> I2
    R12 ==> I3
    R12 ==> I4
    R12 ==> I5
    R12 ==> I6
    R12 ==> I7
    R12 ==> I8

    Offers[12 Jetix offers across<br/>5 tiers T0-T4]
    Offers ==> Checklist

    Checklist ==>|all pass / некоторые caveats| Result[5 offers ✅ clean PASS<br/>7 offers ⚠️ NEED contract care]

    style R12 fill:#ffd6d6
    style Result fill:#ffe0a0
```

**Source:** Phase 8 §1, §10. **Decoded:** 8-item checklist applied per offer; 5 PASS / 7 require explicit R12 contract terms.

---

## §15 Master Qual full ecosystem (combined view)

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TB
    subgraph Person[Person — Ruslan]
        R[Ruslan]
    end

    subgraph Path[Master Qualification Path 15-30 мес]
        R0_15[R0 Личное развитие]
        R1_15[R1-R4 cluster]
        R5_15[R5-R7 core]
        R8_15[R8-R10 applied]
        Cert_15[Certification]
    end

    subgraph МИМ[МИМ Institutional]
        Lev_15[Левенчук + Tseren leadership]
        Masters_15[5 Master mentors]
        Methsovet_15[Methsovet]
        Aisystant_15[Aisystant LMS + IWE]
        Conf_15[Annual conf 10th 2026]
    end

    subgraph Books[Левенчук corpus]
        Books_15[9 active books<br/>4000+ pp]
        FPF_15[FPF GitHub 370 stars]
    end

    subgraph Jetix[Jetix Substrate]
        Foundation_15[Foundation Arch v1.0]
        ROY_15[17 ROY agents]
        R12_15[R12 anti-extraction]
        SPF_15[Jetix-SPF candidate]
    end

    subgraph Outcomes[Outcomes если Path A]
        L6_15[L6 Мастер 2027/28<br/>3 yrs valid]
        Wave1_15[Wave 1 strong]
        Cross_15[32 substrate proposals]
        SPF2_15[Jetix-as-SPF status long-term]
    end

    R --> Path
    Path -.assets.-> Books
    Path -.attendance.-> МИМ
    R -.builds.-> Jetix
    МИМ -.cross-pollinate.-> Jetix
    Books -.feeds.-> Jetix
    Jetix -.offers.-> МИМ
    Path -.cert.-> L6_15
    Jetix -.tier 2-3.-> Wave1_15
    Jetix -.consume.-> Cross_15
    Jetix -.formalise.-> SPF2_15

    style L6_15 fill:#d6f0d6
    style SPF2_15 fill:#d6f0d6
```

**Source:** All Phases 1-9 synthesised. **Decoded:** Full ecosystem view connecting Ruslan, path, МИМ, books, Jetix, and outcomes.

---

## §16 Diagrams summary

| # | Title | Phase ref | Nodes | Theme |
|---|---|---|---|---|
| 1 | Master Qualification flow (8 levels x 3 indicators) | Phase 1, 6 | 14 | quals framework |
| 2 | R0-R10 residency curriculum | Phase 2, 6 | 13 | path |
| 3 | Books × Aisystant × R# × Quals | Phase 2, 4 | 16 | curriculum stack |
| 4 | Cost + Time для Master path | Phase 6 | 9 | economics |
| 5 | Левенчуковский book genealogy | Phase 4 | 13 | book evolution |
| 6 | МИМ ecosystem 12 figures | Phase 5 | 13 | ecosystem |
| 7 | Intellect-stack 16 transdisciplines | Phase 4, 7 | 16 | substrate |
| 8 | FPF + SPF emergence | Phase 3, 7 | 9 | FPF ecosystem |
| 9 | Quality procedure multi-mentor | Phase 1 | 8 | methodology |
| 10 | Jetix subsystems × cross-pollination | Phase 7 | 20 | proposals overview |
| 11 | Jetix offer matrix 5 tiers × R12 | Phase 8 | 12 | offer matrix |
| 12 | 5 Strategic Paths comparison | Phase 9 | 12 | paths |
| 13 | Pedagogical evolution 2012-2026 | Phase 3 | timeline 9 events | history |
| 14 | R12 paired-frame 8-item checklist | Phase 8 | 11 | R12 compliance |
| 15 | Master Qual full ecosystem combined | All phases | 21 | synthesis |

**15 diagrams total** — within parent prompt target (12-18); avg ~13 nodes per diagram; all ≥6 minimum.

---

*Diagrams INDEX closure — Phase 10 component. Per `feedback_max_density_max_tokens.md` MAX-density applied to mermaid pass.*
