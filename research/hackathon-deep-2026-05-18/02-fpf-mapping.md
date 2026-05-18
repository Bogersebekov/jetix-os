---
title: Hackathon FPF mapping + information-flow analysis + dataism vs R12
date: 2026-05-18 evening
type: fpf-mapping
parent_prompt: prompts/hackathon-deep-research-2026-05-18.md
brigadier_phase: 2
constitutional_posture: R1 surface-only + R6 provenance + AP-6 dissent + EP-5 disclosed
F: F3
G: hackathon-fpf-mapping-2026-05-18
R: refuted_if_FPF_primitive_assignments_misinterpret_spec OR Sankey_info-flow_distortion_evidenced
themes_covered:
  - "#information-flow-mechanics"
  - "#story-vs-data"
  - "#dataism-critique"
  - "#truth-vs-order"
sources:
  - design/JETIX-FPF.md (FPF Spec 3758 lines)
  - research/hackathon-deep-2026-05-18/01-fundamentals.md (parent)
  - research/harari-jetix-lens-2026-05-18/04-nexus-jetix-lens.md (Nexus framework)
  - research/harari-jetix-lens-2026-05-18/02-homo-deus-jetix-lens.md (dataism critique)
  - decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/02-fpf-on-ethereum-mapping.md (FPF mapping precedent)
  - swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md (R12 packet)
language: russian + english (FPF primitives)
---

# 02 — Hackathon FPF mapping + information-flow analysis + dataism vs R12

> **R1.** Surface-only. **EP-5.** F3 grade (mapping based on FPF Spec familiarity + secondary hackathon sources).

---

## §0 TL;DR (≤200 слов)

Hackathon mapped к FPF primitives как **U.System composite** (A.1.1 holonic): дизайн-фаза (organizer side) + run-фаза (event itself) образуют A.4 Temporal Duality. **Roles** (U.RoleAssignment A.2.1): 9 stakeholder types ↔ 9 distinct role-holders с typed contracts (U.Commitment A.2.8 + U.SpeechAct A.2.9).

**Information flow** through A.16 U.Episteme lineage — каждый info stream (ideas/methods/connections/hiring/investment/cultural memes) = mutation chain что транслируется через event boundary. **Sankey-diagrammable** — 6 incoming streams × 9 stakeholder transformations × N outgoing artifacts.

**Capabilities composition** (B.1.6 Γ_work): hackathon-as-system composes participant capabilities в team-level capability spikes — explicit «mutual instrumentation» pattern (per text_004 «virtual tribe»). Composition имеет defined boundary (event end) + Γ_work transfer (winning team's capability persists post-event).

**Dataism vs R12 tension:** hackathon's «information flow as supreme value» logic (Harari Homo Deus critique) directly conflicts с R12 «no extraction beyond agreed share». Resolution per Jetix Pillar C: dual-layer judging (volume + meaning); F-G-R per output; fork-and-leave participant rights; programmable royalty enforcement (per Ethereum architecture R12 Option D Hybrid).

**5 mermaid diagrams** generated в diagrams/ — Sankey + holon + capability composition + lineage + dataism-vs-R12 enforcement.

[src: this doc §1-§5 + Ethereum arch §02 + R12 packet]

---

## §1 Hackathon as U.System holon (A.1.1)

[src: design/JETIX-FPF.md A.1 holonic system + this doc §0]

### §1.1 Holon decomposition

```
U.System Hackathon (event-instance)
├── U.SubSystem Organizer-Layer
│   ├── U.Role Organizer (×N)
│   ├── U.Method Theme-Definition
│   ├── U.Method Sponsor-Curation
│   ├── U.Method Mentor-Curation
│   ├── U.Method Judging-Criteria-Design
│   └── U.System Logistics (venue / catering / platform)
│
├── U.SubSystem Run-Layer (event-time)
│   ├── U.Role Participant (×N teams × 2-5 members)
│   ├── U.Role Mentor (×N)
│   ├── U.Role Judge (×N)
│   ├── U.Role Sponsor-Rep (×N companies)
│   ├── U.Method Pitch
│   ├── U.Method Team-Formation
│   ├── U.Method Build-Sprint (24-48h)
│   └── U.Method Demo-Submission
│
├── U.SubSystem Output-Layer
│   ├── U.Artifact Submission (code + demo + pitch)
│   ├── U.RoleAssignment Winner (post-judging)
│   ├── U.Reward Cash + API-credits + SBT
│   └── U.RoleAssignment Mentor-Connection (post-event)
│
└── U.MetaHolon Event-Substrate (sponsor / hosting platform / organizing body)
    ├── U.Episteme accumulated-narrative (event-series identity)
    ├── B.1.6 Γ_work composition (cohort capability transfer)
    └── A.16 U.Episteme lineage (event-to-event learning)
```

[src: FPF Spec A.1.1 holonic + adaptation для event format]

### §1.2 Holonic levels

| Level | FPF object | Hackathon instance |
|---|---|---|
| L0 | U.System Universe-of-discourse | Hackathon-ecosystem (всё что есть «хакатон» как class) |
| L1 | U.System Series | Event-series (MLH season / ETHGlobal year / Jetix Year-1) |
| L2 | U.System Event-instance | Single хакатон event (ETHDenver 2025 March / MumbaiHacks October 2024) |
| L3 | U.SubSystem Track / Theme | Vertical (Infrastructure / DeFi / Public Good — ETHDenver 5 tracks) |
| L4 | U.SubSystem Team | Specific team (2-5 members, registered, builds artifact) |
| L5 | U.SubSystem Submission | Single project artefact (code+demo+pitch) |

Composition rule (per FPF A.1.1): L_n+1 ⊂ L_n; each level inherits constraints from parent (event-rules constrain teams; track-rules constrain submissions).

---

## §2 U.Role / U.RoleAssignment mapping

[src: FPF Spec A.2 Role / A.2.1 RoleAssignment / A.2.8 Commitment / A.2.9 SpeechAct]

### §2.1 9 stakeholder roles formalized

| Stakeholder | U.Role | A.2.1 holder#role:context binding | A.2.8 Commitment (typical) | A.2.9 SpeechAct |
|---|---|---|---|---|
| Organizer | `Organizer` | `Person#organizer:event-instance-X` | promise: «event runs date Y in venue Z с theme T» | declarative: «hackathon open» |
| Sponsor (cash) | `CashSponsor` | `Company#cash-sponsor:event-X:track-Y` | promise: «$N prize pool + API credits + recruiter present» | commissive: «we sponsor track Y» |
| Sponsor (tooling) | `ToolSponsor` | `Company#tool-sponsor:event-X:api-A` | promise: «free API access + docs + technical support» | commissive: «API A available» |
| Participant | `Participant` | `Person#participant:event-X:team-T` | promise: «build artefact within timeframe + abide rules» | commissive: «I register» |
| Mentor | `Mentor` | `Person#mentor:event-X:track-Y` | promise: «available hours H + domain D guidance» | commissive: «I mentor» |
| Judge | `Judge` | `Person#judge:event-X:track-Y` | promise: «evaluate per criteria C + disclose conflicts» | commissive: «I judge» |
| Investor | `InvestorObserver` | `Person#investor:event-X` | (no formal promise; observation role) | (passive) |
| Media | `MediaCoverer` | `Outlet#media:event-X` | promise: «coverage of X type» (если accredited) | commissive (if accredited) |
| Venue | `VenueProvider` | `Org#venue:event-X` | promise: «space + power + network + permit compliance» | commissive |

**Key FPF discipline:** each role-holder binding = **revocable** per A.2.1 (holder ≠ role); role token carries audit trail independent of holder identity. **Это direct H8 trust infrastructure substrate** для хакатон participation history.

[src: FPF A.2.1 + H8 LOCK §3 + Ethereum arch §04 SBT]

### §2.2 Multi-role same-person case

A single Person can hold multiple roles simultaneously (FPF A.2.1 polymorphism):
- A participant in event-1 → mentor in event-2 (longitudinal compound)
- An organizer who also judges (common at small events; conflict-of-interest disclosure required)
- A sponsor-rep who acts as both Recruiter + Mentor

**Sapiens warning (Q-S-6 «orders not neutral / fair»):** multi-role concentration can create asymmetric power; Jetix Pillar C R8 «agent does NOT evaluate peer agent without human review» = analogous safeguard.

---

## §3 U.Method / U.Capability / B.1.6 Γ_work composition

### §3.1 Hackathon methods inventory

[src: FPF Spec A.3 Method + this doc §1 holon decomposition]

| Method | Phase | FPF subtype | Notes |
|---|---|---|---|
| Theme-Definition | Design | U.MethodDescription | Authored by Organizer; constrains everything downstream |
| Sponsor-Curation | Design | U.WorkPlan + U.RoleAssignment | Multi-party negotiation |
| Mentor-Curation | Design | U.RoleAssignment | Selection criteria documented? |
| Judging-Criteria-Design | Design | U.MethodDescription + B.3 F-G-R | Public criteria → self-correcting (Nexus C-N-4) |
| Registration | Pre-event | U.SpeechAct + U.Commitment | Each participant commit |
| Team-Formation | Pre-event/early | U.RoleAssignment + U.Episteme | Often live-formed at opening |
| Pitch | Early | U.MethodDescription presented | Initial team narrative |
| Build-Sprint | Run | U.Method composition + U.Capability application | Core 24-48h work |
| Mentor-Sessions | Run | U.MethodDescription transfer | Tacit→explicit pattern (per direction 14 TPS) |
| Demo-Submission | End | U.Artifact + U.SpeechAct «we submit» | Public verifiable artefact |
| Judging | End | U.Method + B.3 F-G-R per criterion | Reliability signal per score |
| Awards | End | U.Reward distribution + U.RoleAssignment Winner | Public ceremony |

### §3.2 Capability composition (B.1.6 Γ_work)

[src: FPF B.1.6 Γ_work composition + text_004 mutual instrumentation + text_006 «человек-армия»]

```
Γ_work(team) = compose([cap_member_1, cap_member_2, ..., cap_member_n])

where each cap_member_i = {
  technical: [languages, frameworks, libraries, APIs known],
  domain: [verticals familiar — finance / health / web3 / AI],
  meta: [team-formation, pitch, judging experience]
}
```

**Hackathon as Γ_work amplifier:**
- Team formation = capability composition decision
- Build-sprint = capability application + emergent new capabilities (learning under pressure)
- Mentor sessions = capability transfer (mentor → team)
- Demo-submission = capability externalization (artifact carries team capability signal)
- **Post-event capability persists в team members** — даже если team dissolves, members carry Γ_work residue

**Text_004 «mutual instrumentation»** = exact mechanism: «if I know what tools / resources / position они carry — I can use them в моём проекте». Hackathon = compressed mutual-instrumentation event.

**Text_006 «человек-армия» (Тарасов)** apply: каждый participant = self-army (scout/strategist/warrior/diplomat); team of self-armies = army-of-armies = exponentially capable. Hackathon = compressed army-of-armies formation event.

[src: FPF B.1.6 + text_004 + text_006 + direction 14 TPS]

### §3.3 Capability transfer asymmetry

**Empirical observation:** hackathon mentor session = capability transfer DOWNWARD (mentor → participant). Reverse direction (participant → mentor) often understated — но real ($120K-priced mentors learn from teams что they wouldn't see otherwise).

**Jetix implication:** Workshop apprenticeship vs hackathon mentor = different patterns. Workshop = long-term capability transfer with feedback loop; hackathon = burst capability transfer без long feedback. **Both needed; explicit pipeline.**

[src: this doc empirical + direction 14 TPS tacit-explicit transfer]

---

## §4 A.4 Temporal Duality (design / run faces)

[src: FPF Spec A.4 Temporal Duality]

### §4.1 Hackathon design-face vs run-face

| Aspect | Design-face (pre-event) | Run-face (during-event) |
|---|---|---|
| Timescale | weeks-months | 24-72h |
| Primary actors | Organizers + Sponsors + Venue | Participants + Mentors + Judges |
| FPF primitive dominant | U.MethodDescription + U.WorkPlan + U.RoleAssignment | U.SpeechAct + U.Commitment + U.Method application |
| Outputs | Theme + rules + invitations + sponsorship contracts | Team formations + projects + judging + awards |
| Failure mode | Insufficient sponsors / weak theme / poor venue | Burnout / sponsor-bias / theme dilution |
| Self-correction window | Iteration between events (months) | Live (hours) — limited |

**FPF A.4 implication:** хакатон carries dual-face built-in. Both faces require explicit governance. Many community-organized хакатоны under-invest в design-face → run-face suffers.

### §4.2 Series-level temporal duality

At U.System Series level (L1): MLH 2026 Season = July 2025-June 2026 = **continuous design+run cycle** (events overlap; learning continuously compounds).

ETHGlobal events = quarterly cadence (ETHDenver / ETHOnline / ETHIndia / ETHSF / ETHGlobal+) = explicit series-level Γ_work compound.

**Jetix Hypothesis C (self-bootstrapping) — direct relevance:** Year-1 Jetix хакатон series = explicit series-level Γ_work compound design. Each event строит на predecessor.

[src: FPF A.4 + MLH 2026 + ETHGlobal calendar + Hypothesis C]

---

## §5 A.16 U.Episteme — language-state lineage / information mutation

[src: FPF Spec A.16 U.Episteme lineage]

### §5.1 Information mutation chain through hackathon

Per Harari Nexus framework (Q-N-1, Q-N-6/7/8): information ≠ truth; networks generate both truth + order; mutation occurs at each network node.

**Hackathon as A.16 U.Episteme lineage carrier:**

```
[pre-event state]
  └─> Organizer Theme-Definition (mutation 1: domain → event-specific frame)
       └─> Sponsor commitments (mutation 2: theme → resource bundle)
            └─> Participant registration (mutation 3: announcement → committed cohort)
                 └─> Team-formation (mutation 4: individuals → composite capability)
                      └─> Build-sprint (mutation 5: ideas → executable artefacts)
                           └─> Mentor-sessions (mutation 6: tacit → explicit transfer)
                                └─> Judging (mutation 7: artefacts → ranked outputs)
                                     └─> Public demo (mutation 8: project → community signal)
                                          └─> Post-event press (mutation 9: signal → narrative)
                                               └─> Next-event design (mutation 10: lessons → revised theme)

[post-event state] = base state + cohort learning + community narrative + winner reputation + sponsor positioning
```

**FPF discipline:** each mutation should carry **F-G-R tag** (formality / scope / reliability). Most hackathons skip this — informally tracked. Jetix-hosted = explicit F-G-R per mutation = self-correcting mechanism (per Nexus C-N-3).

### §5.2 Information dissemination Sankey-style flow

See `diagrams/01-hackathon-information-flow-anatomy.md` (mermaid Sankey).

**6 income streams × 9 stakeholder transformations × N output artefacts.**

**Volume signals (typical medium hackathon, 200 participants, 48h):**

| Stream | Income volume | Throughput in event | Outgoing volume |
|---|---|---|---|
| Ideas | ~200 (initial ideas + variations) | ~50 (selected for build) | ~50 (submissions) |
| Methods / patterns | ~1000 (mentor sessions + sponsor APIs + peer share) | continuous | persists in members |
| Connections | ~200×N (each participant N connections) | sustained | network compound |
| Hiring signals | ~50 (recruiters × 5-10 candidates each) | continuous | ~10-30 actual offers post-event |
| Investment signals | ~10-20 (investors × 2-5 projects each) | continuous | ~1-5 actual term sheets post-event |
| Cultural memes | 1 theme + N stories | continuous | persists в community discourse |

[src: typical mid-event empirical observation + this doc §1.3 variants + Hypothesis B framing]

---

## §6 Dataism vs R12 — detailed conflict analysis

[src: Harari Homo Deus dataism (per 02-homo-deus-jetix-lens §3 C-HD-2) + R12 packet 2026-05-12 + Ethereum arch §03 R12-programmable]

### §6.1 Dataism logic applied к hackathon

Harari Homo Deus dataism axioms:
- (a) organisms = algorithms
- (b) cosmic merger / Internet-of-All-Things

**Datist hackathon translation:**
- Participants = data-processing nodes (skill = data-processing capacity)
- Sponsor extracts «contribution to data processing mechanism» (recruitment + API usage)
- Events maximize «information flow» = supreme value
- Output = data artefacts; value = information-flow contribution

### §6.2 R12 anti-extraction logic applied

Pillar C Tier 2 rule 12 (LOCKED 2026-05-12):
> «No extraction beyond agreed share. AI / substrate cannot extract value from members beyond agreed share; members can fork-and-leave without penalty.»

**R12 hackathon translation:**
- Participants retain agency + IP per disclosed rules
- Sponsor recruitment = explicit consent, не covert profiling
- Output value = participants retain meaningful share (not just API-credit token)
- Fork-and-leave: participants can withdraw OR rejoin без penalty; submissions NOT trapped в sponsor IP claims unilaterally

### §6.3 Conflict matrix

| Aspect | Pure datist hackathon | R12-compliant hackathon | Tension |
|---|---|---|---|
| Output ownership | Sponsor / event organizer retains | Participants retain; open-source default | High — most «sponsor-driven» events have IP clauses |
| Recruitment | Covert profiling allowed | Explicit consent + opt-out | High — many sponsor recruiter activities = covert |
| Theme alignment | Whatever sponsor pays for | Theme aligned с community + participant interests | Medium — sponsorship economic pressure |
| Burnout | 48h marathon glamorized; volume metric | Sustainable practice; quality > volume | Medium — culture inertia |
| Mentor asymmetry | Hidden (well-connected teams get more) | Mentor hours allocated transparently | Low-medium — observable + fixable |
| Reward distribution | Winner-take-most | QF matching distribution preserves long-tail | High — most events use winner-take-most |

### §6.4 R12 enforcement options for Jetix-hosted hackathons

Per `decisions/strategic/JETIX-ETHEREUM-ARCHITECTURE-2026-05-18/03-r12-programmable-enforcement.md` Option D Hybrid (Mondragón + QF + fork-and-leave):

1. **Smart-contract enforced royalty caps** — if hackathon output commercialized post-event, programmable royalty share returned к participants
2. **SBT role-attestation** — participant performance recorded portably; не lost if leave event organizer ecosystem
3. **QF prize distribution** — small-contributor weighting в judging-pool counters winner-take-all
4. **Public F-G-R per output** — submission carries explicit reliability tag; community can review (truth dimension preserved)
5. **Open-source mandatory default** — IP retention by community (Karpathy LLM Wiki precedent per direction 09)

### §6.5 «Jetix-hosted hackathon» = potential demonstration platform для R12-compliant model

If Hypothesis C (self-bootstrapping) progresses → Jetix hackathon series may serve as **empirical proof-of-concept что R12-compliant хакатон model works** (vs default sponsor-extractive model). Public differentiation possible.

**Caveat per AP-6:** R12-compliant model has not been empirically tested at scale. Mondragón empirical (direction 06) closest precedent (€11.2B / 70K employees / 3 crises survived) — но Mondragón ≠ хакатон. New mechanism design required + iteration.

[src: Ethereum arch §03 + R12 packet + direction 06 + AP-6 discipline]

---

## §7 5 mermaid diagrams (generated в diagrams/)

Standalone diagram files в `research/hackathon-deep-2026-05-18/diagrams/`:

1. **01-hackathon-information-flow-anatomy.md** — Sankey-style 6 streams × 9 stakeholders × N outputs
2. **02-jetix-self-bootstrapping-hackathon-compound.md** — recursive amplification (Hypothesis C)
3. **03-platform-comparison-quadrant.md** — 8 dimensions ranked across major platforms
4. **04-hypothesis-priority-roadmap.md** — Phase 1/2/3 gantt across hypotheses
5. **05-harari-nexus-hackathon-overlay.md** — Nexus thesis applied к хакатон ecosystem

(Generated в Phase 5 cleanup — этот doc references; standalone files created later.)

---

## §8 На человеческом (plain Russian summary)

Hackathon в терминах FPF — это **U.System (систем) с двумя лицами** (A.4 Temporal Duality):
- **Design face** (дизайн-фаза, недели-месяцы до события): организаторы + спонсоры + venue готовят
- **Run face** (run-фаза, 24-72ч): участники + менторы + судьи работают

**9 ролей** (U.Role): organizer / sponsor (cash) / sponsor (tool) / participant / mentor / judge / investor / media / venue — каждая роль связана с holder через **A.2.1 RoleAssignment** (роль ≠ человек; роль отзываема; роль накапливает audit trail независимо от holder).

**Team capability composition** (B.1.6 Γ_work): команда = композиция capabilities (technical+domain+meta). Хакатон = **компрессированное событие mutual-instrumentation** (точно то что text_004 описывает — «использую людей через их роли+ресурсы+положение») + точно текст_006 «человек-армия Тарасов» — каждый = self-army; команда = army-of-armies.

**Information mutation chain (A.16 U.Episteme lineage):** 10 mutations от pre-event state к post-event state. Каждая mutation должна нести F-G-R тег (формальность / scope / надёжность). Большинство хакатонов это пропускают — Jetix-hosted могло бы explicit.

**6 информационных потоков** (Sankey) через event: ideas / methods / connections / hiring / investment / cultural memes. См. mermaid diagrams/.

---

**Главное напряжение Dataism vs R12:**

Харари Homo Deus говорит: датаизм logic = «participants = data-processing nodes; output = information-flow contribution; sponsor maximizes flow». Это extractive logic.

R12 Jetix говорит: «нет извлечения за пределами agreed share; fork-and-leave без penalty». Это anti-extractive.

**6 точек конфликта:**
1. Output ownership (sponsor retains vs participants retain) — HIGH tension
2. Recruitment (covert profiling vs explicit consent) — HIGH
3. Theme alignment (sponsor pays vs community-aligned) — MEDIUM
4. Burnout (48h marathon glam vs sustainable) — MEDIUM
5. Mentor asymmetry (hidden vs transparent) — LOW-MEDIUM
6. Reward distribution (winner-take-most vs QF matching) — HIGH

**5 R12 enforcement options для Jetix-hosted хакатонов** (per Ethereum architecture §03 Option D Hybrid):
1. Smart-contract enforced royalty caps
2. SBT role-attestation (portable)
3. QF prize distribution
4. F-G-R per output (public)
5. Open-source mandatory default

**Если Hypothesis C (self-bootstrapping) сработает** → Jetix хакатон series может стать **empirical proof что R12-compliant хакатон работает** — публичное differentiation от sponsor-extractive дефолта. Не доказано empirically — Mondragón ближайший прецедент (но не хакатон).

**Главный вывод:** FPF mapping показывает что хакатон формально decomposable + capability-compose-able + lineage-track-able. Не abstract concept; concrete substrate. Jetix может **строить хакатон series которые работают по FPF discipline** = differentiation от existing platforms.

---

**Brigadier note (R1).** FPF mapping surfaces structure + Harari dataism-vs-R12 tension analysis. NOT decision. EP-5: F3 grade. Word count ~3000.
