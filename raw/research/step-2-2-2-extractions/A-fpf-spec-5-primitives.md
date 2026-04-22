---
title: "Sub-agent A extraction — FPF-Spec + 5 ШСМ primitives"
date: 2026-04-23
sources: [FPF-Spec.md, R-A-levenchuk-full-body-of-work.md, R-B-shsm-5-primitives-deep.md]
pipeline: ingested
---

# Sub-agent A — Extraction: FPF-Spec + 5 ШСМ primitives

Pure extraction. Every claim cited `[source §section/line]`. Keys: `[FPF]` = FPF-Spec.md; `[R-A]` = R-A-levenchuk-full-body-of-work.md; `[R-B]` = R-B-shsm-5-primitives-deep.md.

R-B frames the 5 as «минимально полный онтологический инструментарий… они задают онтологию: классы объектов, которые всегда существуют в любом проекте независимо от применяемого метода» `[R-B §Исп.резюме, L13-23]`. Not a process — an ontology.

---

## Part 1 — The 5 ШСМ primitives

### 1.1 Роль (Role)

**Definition (verbatim Levenchuk, «Методология 2025» via R-B):** «Агенты имеют роли в методе. […] Создатели – это агенты, всё что из методов умеет делать агент – это личность агента. […] Агенты имеют роли в методе.» `[R-B §1.1, L41-48]`. ailev-1741032: «Если говоришь роль, то за ролью скрывается метод» `[R-B §1.1, L47]`.

R-B formula: **«Роль = сигнатура метода × интерес к системе × набор мастерства. Конкретный исполнитель — носитель роли, но не сама роль.»** `[R-B §1.1, L55]`.

FPF encoding: `A.2 Role Taxonomy`, `A.2.1 U.RoleAssignment`, `A.2.5 U.RoleStateGraph`, `A.13 Agential Role` ("FPF models agency without minting a U.Agent type"), `A.15 Role–Method–Work` `[FPF L39-91]`.

**Protocol for AI agent:**
1. Role-manifest is a **method signature** `{method, альфа-subjects, transitions, acceptance criteria, out-of-scope}` — NOT a system prompt `[R-B §1.4, L97-117; §1.6, L142-146]`.
2. Roles assigned at task-creation, **never dynamic self-assignment**: dynamic assignment «разрушает граф создания и систему альф» — unpredictability, unattributed transitions, diluted accountability `[R-B §1.3, L79-85]`.
3. Name = **method** ("Sales Lead"), not executor ("Claude Agent #3") or RACI ("Ответственный") `[R-B §1.6, L138-141]`.
4. ≤7 accountability items per role; else decompose `[R-B §1.6, L151]`.
5. Use established cultural labels ("моряк"), not inventions ("морепроходимец") — discovery > design `[R-B §1.5, L125-131]`.

**Interrelationships:** Роль carries a Метод; operates on Альфы; positioned within Граф создания; `A.15` enforces Role-Method-Work alignment.

---

### 1.2 Альфа (Alpha)

**Definition (verbatim Levenchuk, «Методология 2025» via R-B):** «Альфа – это предмет метода, который может быть и физическим объектом (системой), и абстрактным объектом (описанием).» «Альфа позволяет управлять вниманием создателя в ходе исполнения длинных цепочек операций…» «Альфа помогает отследить судьбу предмета метода в проекте» `[R-B §2.1, L162-166]`.

SEMAT origin (Jacobson 2012): «An alpha is an essential element of the software-engineering endeavor… relevant to an assessment of its progress and health»; «Alphas are what we progress. […] Alphas exist whether there are tangible work products or not» `[R-B §2.1, L170-174]`. Levenchuk extends from software-only to any project situation `[R-B §2.1, L176]`. R-A: past-participle convention "makes alpha-state checklists machine-parseable" `[R-A §5.3, L326]`.

FPF encoding: word "alpha" absent; mechanism preserved via `A.2.5 U.RoleStateGraph`, `A.15.1 U.Work`, `C.2.1 U.EpistemeSlotGraph`, `B.5.1 Explore→Shape→Evidence→Operate` `[FPF L44, 89, 140]`.

**Protocol for AI agent:**
1. State names MUST be past-participle: «квалифицирован, активирован, начат, доставлен, закрыт» `[R-B §2.4, L262]`. Enables `IF Client.state == "Qualified" THEN…` machine-actionability `[R-B §2.4, L246]`.
2. Each state has a **verifiable checklist** (e.g. `Client.Qualified` = ICP ≥ 70, BANT ≥ 2/4, champion identified, no blockers, next step agreed) `[R-B §2.3, L217-224]`.
3. State graph may be non-linear: «возможны возвраты… кольца и петли» `[R-B §2.3, L206]`.
4. Each transition attributed to a role `[R-B §2.3, L211]`.
5. Seven OMG Essence kernel alphas: `Opportunity, Stakeholders, Requirements, Software System, Work, Team, Way of Working` `[R-B §2.5]`.
6. Discrimination: only альфа has lifecycle affecting project health. False positives: `Task, Ticket, Meeting, Document, Person, Feature` `[R-B §2.2, 2.6]`.

**Interrelationships:** Альфа = Method-subject of a Роль; transitions attributed to roles; partitioned across Граф создания levels `[R-B §6.2, L736]`.

---

### 1.3 Граф создания (Creation Graph)

**Definition (verbatim Levenchuk via R-B):** «моделировать граф создания […] по мотивам OMG Essence 2.0:2024» `[R-B §3.1, L323]`; «агенты-создатели (тогда – люди и их организации, сейчас включаем и AI) как надсистемы целевой системы… не менее важны, чем создаваемая ими целевая система» `[R-B §3.1, L329-331]`.

R-A: "A directed graph of which systems create which other systems, capturing the multi-level constructor/constructee relationships. Not a simple hierarchical decomposition — it maps the full ecosystem of enabling systems, creating systems, and target systems" `[R-A §4.1, L243]`.

**Three-level mereological structure** `[R-B §3.4]`:
```
Level 3 НАДСИСТЕМА   ← operates-in / constrained-by
Level 1 ЦЕЛЕВАЯ       ← creates / methodologically-uses
Level 2 СИСТЕМЫ СОЗДАНИЯ
```
Five typed edges: `part-of, creates, operates-in, methodologically-uses, constrained-by` `[R-B §3.4]`. Holonic basis (ailev-1776793): «За основу мы берём мереологию холонов… конструированием из частей и входимостью в другие целые как части» `[R-B §3.3, L352-354]`. Recursive: creators are themselves created `[R-B §3.3, L358]`.

FPF encoding: `A.1 Holonic Foundation`, `A.14 Advanced Mereology`, `B.2 Meta-Holon Transition`.

**Protocol for AI agent:**
1. Every node = a system (not activity, not role, not artifact) `[R-B §3.5]`.
2. Every edge = creation/operation/use (not "supplies", not "depends on") `[R-B §3.5]`.
3. Required three levels: target, creators, supra `[R-B §3.5]`.
4. Recursion: for every creator ask "who creates this creator?" until human/base-infrastructure.

**Anti-patterns:** workflow/BPMN, dependency tree, org chart, supplier-consumer bipartite `[R-B §3.2, L344-348]`.

**Interrelationships:** Граф defines structural constraints on required Роли per level; evolves via Стратегирование; Альфы partitioned across its levels `[R-B §6.2, L726-736]`.

---

### 1.4 Стратегирование (Strategizing)

**Definition (verbatim Levenchuk, «Методология 2025» via R-B):** «метод выбора метода – стратегирование»; «…выбирать новый метод работы в условиях, когда вообще непонятно, что делать. А если непонятно, что именно делать, то и планировать ещё ничего нельзя (потребные ресурсы неизвестны, ведь непонятно, каким методом работаем) и работать нельзя» `[R-B §4.1, L442-444]`. ailev-1779269: «Почему стратегирование? Потому что на этом пути надо не научиться решать проблемы, а надо научиться ставить новые goldilocks проблемы и находить новые и новые недоминируемые решения» `[R-B §4.1, L450]`.

R-A: "Strategy not as a one-time plan document but as a continuous, never-ending practice… 'бесконечное стратегирование'. Against 'strategy documents' as endpoint" `[R-A §4.1, L258]`.

**Strict ordering** `[R-B §4.1, L454-461]`: **Стратегирование → Планирование → Работа**. Planning is impossible before strategizing completes.

**Trigger-based, not scheduled** `[R-B §4.2]`. Valid triggers: market signal, alpha failure, method exhaustion, irreversible decision, boundary change, new role without known method, quarterly reset *only if real uncertainty*. Scheduled strategizing = "performance ritual" → "методы-конвульсии" `[R-B §4.2, L480]`.

**Three method-modes** `[R-B §4.3]`: **1:1** (known, no change → full AI auto), **Adapt** (known, tuned → AI + oversight), **Invent** (unknown → human only).

**Protocol for AI agent:**
1. **AI agents do NOT strategize** `[R-B §4.3, L510-524]`: no identity/commitment (session-fresh), no long-term SoTA memory, no "skin in the game" (Taleb).
2. AI CAN: SoTA research, draft alternatives, devil's advocate, anti-scope checklist. AI CANNOT: choose method, accept decision, bear responsibility `[R-B §4.3, L527-537]`.
3. Mandatory artifact components `[R-B §4.5]`: explicit trigger (not scheduled), ≥2 alternatives + status quo, kill-conditions, review checkpoint with criteria.
4. Filename: `strategizing/{trigger-slug}-{YYYY-MM-DD}.md`; slug = event, not process `[R-B §4.2, L484-494]`.

FPF encoding: `B.4 Canonical Evolution Loop`, `B.5 Canonical Reasoning Cycle`, `B.5.2 Abductive Loop`, `B.5.2.1 Creative Abduction with NQD`, `E.9 DRR`, `C.17-C.19` NQD-CAL / E-E-LOG `[FPF L135-144, 471]`. FPF Preface: "FPF integrates assurance and creativity as complementary engines" `[FPF L400-408]`. Rule-of-Constraints vs Instruction-of-Procedure: "declare *what must not happen*… agents have freedom to choose *how* to act" `[FPF L558-568]`.

**Interrelationships:** Стратегирование is **meta-level** over Роли и Альфы `[R-B §6.2, L728]`; outputs (a) roles for new method, (b) alpha-subjects, (c) target state-graph; may revise Граф создания `[R-B §6.2, L731]`; requires Мышление письмом `[R-B §6.2, L730]`.

---

### 1.5 Мышление письмом (Writing-as-Thinking)

**Definition (verbatim Levenchuk, «Системное мышление 2024 т.1» via R-B):** «Системное мышление происходит путём мышления моделированием… и письмом (с текстами на естественных языках, но с отслеживанием типов объектов и видов отношений объектов в этих текстах), поэтому внимание… удерживается… всё время проекта: записанное не так легко забыть в суете» `[R-B §5.1, L605]`.

R-B synthesis: «Мышление письмом — это когнитивный процесс, в котором письменный текст… является **орудием мышления** (не его продуктом). Ключевое требование — отслеживание типов объектов и видов отношений в тексте (онтологизация). Без онтологизации это не мышление письмом, а просто writing» `[R-B §5.1, L615]`. R-A: "Writing externalizes and stabilizes cognitive processes, making them reviewable and refinable" `[R-A §4.1, L253]`.

**FPF-Spec has a dedicated Preface section "Thinking Through Writing"** `[FPF L515-533]`: «This "writing" is not a by-product of thinking; it *is* the thinking. The act of filling out a **Role Description Card** or constructing a **Concept-Set Table** is not mere documentation; it is the cognitive work of making distinctions, declaring invariants, and justifying relationships» `[FPF L519]`. Operationalized via Cards (F.1, F.4), Tables (F.17 UTS), Records (E.9 DRR), Conformance Checklists, under Notational Independence E.5.2.

**Protocol for AI agent:**
1. Human produces: daily log (5-10 min morning + evening alpha reconciliation), weekly review, quarterly letter (Berkshire-style: Alpha States Then vs Now, "what I got wrong", bets) `[R-B §5.4, L648-663]`.
2. **AI agents must NOT produce primary writing rituals** `[R-B §5.5, L681-686]`. Levenchuk: «Без внешнего по отношению к LLM контуру обработки текста — никак, LLM всегда обманет. Если и сам текст пишет LLM — исчезает "мышление письмом" как когнитивный процесс» `[R-B §5.5, L690]`.
3. AI CAN: extract structured data from human-written text, critique structure, suggest variants, ask probing questions `[R-B §5.5, L676-680]`.
4. Quality test: «Узнал ли я что-то новое в процессе написания?» — yes = real writing-as-thinking `[R-B §8.5]`.

**Interrelationships:** externalizes Стратегирование into transferable artifacts; produces the **exocortex** — context input for next AI session, solving Naur's "theory death on team dissolution" `[R-B §5.3, 6.2]`.

---

## Part 2 — Interrelationships

### 2.1 Graph (R-B §6.1, L700-720, verbatim):
```
ГРАФ СОЗДАНИЯ
    │ задаёт контекст для
    ↓
РОЛИ ←────────── СТРАТЕГИРОВАНИЕ
    │                    │ принимает решения о методах
    │ работают с         │ (какие роли, какие альфы,
    ↓                    │  какие transitions целевые)
АЛЬФЫ ───────────────────┘
    │ переходы фиксируются
    ↓
МЫШЛЕНИЕ ПИСЬМОМ — экстернализирует стратегирование
    │ создаёт контекст
    ↓
экзокортекс (вход для следующей сессии агента)
```

### 2.2 Feed-direction `[R-B §6.2, L724-736]`

| Source | → | Target | Nature |
|---|---|---|---|
| Граф создания | → | Роли | Structural constraint on role set |
| Роли | → | Альфы | Roles work on alphas (method subjects) |
| Стратегирование | → | Роли + Альфы + Граф | Chooses method, may revise all three |
| Альфы | → | Мышление письмом | Transitions recorded |
| Мышление письмом | → | Стратегирование | Externalizes into artifacts |
| Мышление письмом | → | Экзокортекс | Context for next AI session |

### 2.3 Root vs apex

R-B names no single root. Two candidates:
- **Граф создания is root by structure**: defines the systemic context `[R-B §6.2, L726]`.
- **Стратегирование is apex by authority**: only meta-level primitive; can rewrite Граф + roles + alphas `[R-B §6.2, L728-731]`.

Diagram reading: "Graph frames, Strategizing rewrites".

### 2.4 Operational ordering

R-B: **Стратегирование → Планирование → Работа** `[R-B §4.1, L454-462]`. For full 5-primitive setup:
1. **Граф создания** (draw three levels)
2. **Роли** (list roles per level, each tied to a method)
3. **Альфы** (identify method-subjects per role + state machine + checklists)
4. **Стратегирование** (trigger-driven; chooses method, may revise 1-3)
5. **Мышление письмом** (continuous externalization of 1-4)

#5 is continuous, #4 trigger-driven, #1-3 static ontology.

---

## Part 3 — FPF-Spec core structure

### 3.1 One-paragraph summary

FPF is "a small, domain-agnostic kernel and a set of extension patterns for publishing, checking, and evolving conceptual work about systems and epistemes" — holons `[FPF L346]`. It is "a pattern language. A pattern is… a **contract**: Problem frame → Problem → Forces → Solution, ending with a Conformance Checklist" `[FPF L348]`. FPF "treats creativity as a governed search and assurance as a repeatable reckoning. Together they form an engine for changing collective's mind responsibly" `[FPF L416]`. Tool-agnostic, notation-agnostic, workflow-agnostic — conceptual content, not team logistics `[FPF L525-527]`. R-A: "operating system for thought for engineering, research, and mixed human/AI teams… 300+ patterns by April 2026… neutral English for AI-agent readability and type-safety across bounded contexts" `[R-A §4.1, L263]`.

### 3.2 Core elements — Parts A-K `[FPF L357-364]`

- **A — Kernel Architecture:** holons, bounded contexts, role/scope, transformers, time/evolution, work-planning, measurement, signature-stack/boundary
- **B — Trans-disciplinary Reasoning:** aggregation, emergence, trust/assurance, evolution + reasoning cycles, abductive prompting, creative search, bridges
- **C — Kernel Extensions:** Sys/KD/Kind/Method/LOG/CHR calculi, measurement, NQD creativity, explore/exploit, discipline health
- **D — Ethics & Conflict-Optimisation:** axiological neutrality, multi-scale ethics, bias/ethical assurance
- **E — Constitution & Authoring:** vision, pillars, guard-rails, authoring, lexical law, MVPK, DRR governance
- **F — Unification Suite:** concept-sets, naming, role descriptions, bridges, UTS
- **G — Discipline SoTA Kit:** CG-Spec, CG-Frame, SoTA harvesting, selectors, telemetry
- **H-K:** glossary, annexes, indexes, lexical debt

**Load-bearing kernel** `[FPF Part A L36-103]`: `A.1 Holonic Foundation (Entity ⊃ Holon ⊃ {System, Episteme})`, `A.1.1 U.BoundedContext`, `A.2 Role Taxonomy` + `A.2.1 U.RoleAssignment`, `A.3 Transformer Quartet (System-in-Role, MethodDescription, Method, Work)`, `A.4 Temporal Duality & OEE`, `A.5 Open-Ended Kernel`, `A.6 Signature Stack & Boundary Discipline`, `A.7 Strict Distinction`, `A.10 Evidence Graph Referring`, `A.12 External Transformer`, `A.13 Agential Role`, `A.14 Advanced Mereology`, `A.15 Role–Method–Work` + `A.15.1 U.Work` + `A.15.2 U.WorkPlan`, `A.16 Language-State Transduction`, `A.17-A.19 Characteristic/Scale/Level/Coordinate`.

**Reasoning architecture** `[FPF Part B L112-146]`: `B.1 Universal Γ (IDEM/COMM/LOC/WLNK/MONO)`, `B.2 MHT (emergence)`, `B.3 F-G-R Trust & Assurance`, `B.4 Canonical Evolution Loop`, `B.5 Canonical Reasoning Cycle (Abduction→Deduction→Induction; Explore→Shape→Evidence→Operate)`.

### 3.3 FPF ↔ 5 ШСМ primitives mapping

| ШСМ | FPF home |
|---|---|
| **Роль** | `A.2, A.2.1, A.2.5, A.13, A.15` `[FPF L39-91]` |
| **Альфа** | Word absent; mechanism via `A.2.5 U.RoleStateGraph`, `A.15.1 U.Work`, `C.2.1 U.EpistemeSlotGraph`, `B.5.1` lifecycle |
| **Граф создания** | `A.1 Holonic Foundation`, `A.14 Advanced Mereology`, `B.1 Universal Γ`, `B.2 MHT`. Target/creator/supra = Holon/Sub/Super |
| **Стратегирование** | `B.4`, `B.5.2 Abductive Loop`, `B.5.2.1 Creative Abduction w/ NQD`, `E.9 DRR`, `C.17-C.19 NQD/E-E-LOG` |
| **Мышление письмом** | Preface "Thinking Through Writing" `[FPF L515-533]`; via `E.8, F.1, F.4, F.17 UTS, E.9 DRR, E.12/E.14, E.5.2` |

R-A: «FPF provides the architecture for AI-readable reasoning — bounded contexts, stable vocabulary (UTS), decision records (DRR) make AI outputs reviewable and non-drifting» `[R-A §5.3]`.

**Re-framing:** FPF universalizes alpha-state-machines into RoleStateGraphs + U.Work. Граф создания splits across holonic mereology + MHT. Стратегирование splits across abductive loop + DRR + NQD/E-E-LOG + Rule-of-Constraints. FPF is the **operational substrate under the ШСМ primitives** — ШСМ conceptual; FPF normative pattern-language contracts with Conformance Checklists `[FPF L348]`.

---

## Part 4 — Levenchuk body-of-work structural map (R-A)

### 4.1 Top-level layers

R-A §1.2 three generations of systems thinking `[R-A L54-66]`:
- **Gen 1 (absorbed):** Bertalanffy GST, Wiener cybernetics, Koestler holons.
- **Gen 2 (absorbed + critiqued):** Checkland SSM, ISO 15288/42010/15926, SEMAT/Essence.
- **Gen 3 (his synthesis, 2020s):** techno-evolution, continuous-everything, mereotopology + category theory, Active Inference (Friston), NQD OEE.

**Intellect Stack = explicit hierarchical layering.** 16 transdisciplines (2025) `[R-A §4.1, L237]`: Инженерия, Риторика, Эстетика, Исследования, Алгоритмика, Теория понятий, Математика, Собранность, Методология, Этика, Рациональность, Онтология, Физика, Семантика, Понятизация, Логика.

FPF's own 5-layer Intellect Stack `[FPF L718-724]`: L1 Structure & Reality (Kind-CAL, Sys-CAL); L2 Knowledge & Reasoning (KD-CAL, Arg-LOG); L3 Action & Execution (Agent-CHR, Method-CAL, Resrc-CAL); L4 Strategy & Rationality (Decsn-CAL); L5 Governance & Purpose (Norm-CAL). ШСМ 16 = discipline-names; FPF 5 = cognitive layers — coexistent.

### 4.2 Layer home of each primitive

| Primitive | ШСМ transdiscipline | FPF layer |
|---|---|---|
| **Роль** | Системное мышление + Методология `[R-A §4.1]` | L3 Action + L1 |
| **Альфа** | Same — SEMAT-adapted `[R-A §4.1, L242]` | L3 Method-CAL |
| **Граф создания** | Системное мышление 2024 т.2 `[R-A §2.1, L91]` | L1 Structure |
| **Стратегирование** | Методология 2025 + Системный менеджмент 2023 `[R-A §4.1, L258]` | L4 + L5 |
| **Мышление письмом** | Cross-cutting intellect-stack practice `[R-A §4.1, L255]` | Cross-layer (E.12/E.14) |

### 4.3 Canonical vs peripheral `[R-A §4.1-4.2, L227-284]`

**Canonical:** Системное мышление (Gen-3); Интеллект-стек ("structural backbone of all ШСМ curricula"); Роль/Альфа/Граф-создания trio; Мышление письмом; Стратегирование; FPF (2026 synthesis — R-A labels it **"Original — no direct precursor"**); Экзокортекс.

**Peripheral / historical:** 17-transdiscipline 2021 (superseded by 16 in 2025); «Визуальное мышление» 2018; «Образование для образованных 2021» (superseded by Интеллект-стек 2023); pre-2024 Системное мышление editions; individual pre-2024 courses (now in residency).

**Innovation provenance** `[R-A §4.2]`: Alpha state machines — SEMAT adapted; ISO 15288/42010/15926 — synthesized; Active Inference — incorporated; Writing-as-thinking — systematized; Transdiscipline stack — original synthesis; Gen-3 ST ontology — original + arXiv 2023; **FPF — Original**; Exocortex — original LLM application.

---

## Part 5 — Applicability notes (6-agent swarm: brigadier + 5 experts, matrix stage-gated workflow)

**5.1 Роль.** Each expert defined by a **method-signature** (subject-альфы + transitions + acceptance criteria + out-of-scope), not a prompt-blurb; brigadier enforces assignment at task-creation (no dynamic self-assignment) per «разрушает граф создания и систему альф» `[R-B §1.3, L79-85]`.

**5.2 Альфа.** Each expert maintains a state machine over its primary альфа with past-participle states + checklists; matrix stage-gate transitions ARE alpha-state transitions (`ArtifactX.Drafted → .Reviewed → .Accepted`), making gate passage machine-verifiable `[R-B §2.4, L226-246]`.

**5.3 Граф создания.** Brigadier owns three-level graph: **target = project deliverable; creators = 6 agents + infrastructure; supra = client/organizational context + constraints**; "who creates creators" satisfied by human-operator + Anthropic + role-manifest authorship `[R-B §3.4, L390-413]`.

**5.4 Стратегирование.** **No agent strategizes — neither brigadier nor experts** `[R-B §4.3, L510-524]`. Trigger-driven escalation to human; agents produce draft alternatives/SoTA/devil's-advocate. Matrix's "invent" cells flagged for human; "adapt" / "1:1" cells delegated to agents.

**5.5 Мышление письмом.** Human produces primary writing artifacts (strategizing docs, weekly reviews, quarterly letters) — **NOT agents** `[R-B §5.5, L681-690]`. Agents extract structure, critique, surface contradictions. Swarm exocortex (wiki + state + FPF `E.9` DRRs) = human-authored artifacts + agent-extracted structure; prevents Naur's "theory death" on session end.

---

## Divergences and fuzziness notes

1. **"Alpha" word absent in FPF-Spec; mechanism preserved** via `A.2.5 U.RoleStateGraph` + `A.15.1 U.Work` + past-participle state names. Encoding shift, not contradiction.
2. **Граф создания ↔ FPF holonic mereology.** R-B: «по мотивам OMG Essence 2.0:2024» `[R-B §3.1, L323]`. FPF generalizes via `A.1 + A.14 + B.2`. Three-level ШСМ = FPF holon/sub-holon/super-holon.
3. **Stack-size mismatch not a contradiction.** ШСМ 16 transdisciplines vs FPF 5 cognitive layers — different granularity/purpose.
4. **Стратегирование: R-B categorical, FPF machinery present but term absent.** FPF: `B.5.2 abductive loop` + `E.9 DRR` + `C.17-C.19 NQD` + Rule-of-Constraints `[FPF L558-568]`. Mapping: strategizing ≈ abductive-loop + DRR + RoC + human decision authority.
5. **Otherwise full consistency across R-A, R-B, FPF.** R-B most precise (verbatim + anti-patterns); R-A historical framing; FPF normative pattern-language layer with Conformance Checklists `[FPF L348]`.

---

*Extraction complete. Cite section headers (§1.3 Граф создания, §3.3 FPF↔ШСМ mapping, §5.4 Стратегирование applicability, etc.) to refer back.*
