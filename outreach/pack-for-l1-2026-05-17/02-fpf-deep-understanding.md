---
title: FPF на человеческом языке v2 — definitions, primitives, mechanisms, intelligence amplification
date: 2026-05-17
phase: Phase B Шаг 1 (Phase A baseline 01-fpf-on-human-language.md v1 462 lines)
type: distillation
parent_prompt: prompts/fpf-iwe-phase-b-2026-05-17.md §1
corpus_snapshot: raw/external/ailev-FPF/FPF-Spec.md @ c86eabd 2026-05-16 (72 800 lines)
freshness_changelog: raw/external/ailev-FPF/CHANGELOG-2026-04-20-to-2026-05-16.md
F: F5
G: distillation-2
R: refuted_if_levenchuk_flags_verbatim_misquote_OR_mechanism_mischaracterized_OR_RUSLAN-LAYER_attribution_creep
prose_authored_by: brigadier-integrated (3 critic cells eng/phil/mgmt × critic — see swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-*-critic-fpf-tighten.md)
language: russian + english (verbatim where source-language)
audience: L1 (Anatoly Levenchuk, Tseren Tserenov) + sophisticated practitioners new to FPF
reading_time_targets:
  - 5min skim: §0 freshness + §1 one-line + §2 paragraph + §QR at tail
  - 15min dive: + §3 primitives + §6.1 verbatim "why FPF" answer
  - 30min full: entire body inc. §4 canonical-vs-RUSLAN-LAYER split
critic_drafts:
  - swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-engineering-critic-fpf-tighten.md
  - swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-philosophy-critic-fpf-tighten.md
  - swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-mgmt-critic-fpf-tighten.md
---

# FPF на человеческом языке — v2

> **Constitutional posture.** Scribe-mode + structurer. Verbatim Левенчуковский где
> возможно. Provenance per claim — `[<file>:<line-range>]` или `[<url>@<retrieved>]`.
> Surface'инг без оценки «лучше/хуже». Boundary discipline: §4a = canonical FPF;
> §4b = RUSLAN-LAYER Jetix-internal mapping с явным disclaimer. F-G-R per non-trivial synthesis claim.

---

## §0 Freshness snapshot — на каком FPF этот разбор основан

| Параметр | Значение |
|---|---|
| Канонический источник | `github.com/ailev/FPF` (single doc + Readme) |
| Captured HEAD commit | `c86eabd 2026-05-16` («corrections for E.10.SEMIO campaign») |
| Файл локально | `raw/external/ailev-FPF/FPF-Spec.md` (72 800 lines) |
| Backup предыдущего | `raw/external/ailev-FPF/FPF-Spec-2026-04-20.md.bak` (62 202 lines) |
| Active dev clusters | **E.10.SEMIO** (semiotic/boundary statements), **A.6.P** (compression-decompression, role-publication discipline) |
| Δ LOC since 20.04 | +10 598 строк (+17.0%) |
| Changelog | `raw/external/ailev-FPF/CHANGELOG-2026-04-20-to-2026-05-16.md` |

> **Что это значит.** Spec живой; line-numbers могут сдвинуться. Все Spec-line ссылки
> ниже относятся к snapshot `c86eabd`. Если читаешь позже — проверь по grep,
> не по абсолютному номеру строки.

> **Левенчуковская позиция в TG 2026-05-17 (verbatim):**
> «у нас много более скромные интересы: я вот делаю FPF, и там не так много документов,
> как у вас, всего один — github.com/ailev/FPF (ладно, два: ещё README.md в GitHub).»
> `[inbox/levenchuk-tg-2026-05-17.md:26]`

---

## §QR-NAV Содержание (TOC + reading-path map)

- **5-минутный путь** → §0 (freshness) + §1 (one-line) + §2 (one-paragraph) + §QR-CARD в конце.
- **15-минутный путь** → выше + §3 (5+ primitives) + §6.1 (verbatim «why FPF» от Левенчука) + §6.4 (verbatim Spec quotes).
- **30-минутный путь** → весь документ; критично §4a (canonical FPF mechanisms) и §4b (RUSLAN-LAYER, не canonical FPF).

| § | Тема | Реальный размер | Что разблокирует |
|---|---|---|---|
| §0 | Freshness | 1 таблица | Знаешь, на каком FPF основан разбор |
| §1 | FPF в одной фразе | 3 verbatim quotes | Можешь one-line объяснить FPF |
| §2 | FPF в одном абзаце | 1 параграф | 30-секундный elevator |
| §3 | 5+ primitives | ~9 sub-секций | Знаешь U.Holon, U.BoundedContext, U.Role, U.Method+Work, U.Alpha (Creation Graph), Strategizing, Writing-as-Thinking, U.Episteme/etc |
| §4a | Canonical FPF mechanisms | 4 sub-секции | A.6.B, A.6.P, A.14, B.3 — что в Spec |
| §4b | RUSLAN-LAYER mapping (НЕ canonical FPF) | 4 sub-секции | Jetix IP-1/IP-2/IP-3/IP-7 mapped к FPF эквивалентам — наш разбор, не Левенчук |
| §5 | Принципы мышления и интеллекта | 7 core ideas + 11 pillars stub | Можешь говорить «принципы, положенные в основу FPF» |
| §6 | Intelligence amplification — механизм | 7 паттернов наш разбор | Можешь объяснить C3 Левенчука: где «память+автоматизация» ≠ amplification |
| §7 | Что НЕ вытащили (gap registry) | Список | Знаешь границы Phase A |
| §QR-CARD | Quick reference card | 20 строк | Lookup без чтения |

---

## §1 FPF в одной фразе (verbatim Левенчуковский)

> **«[FPF is an] operating system for thought for engineering, research, and mixed human/AI teams.»**

`[raw/external/ailev-FPF/Readme.md:9 / FPF-Spec.md около L831 — "Purpose – an operating system for thought"]`
`F: F8 | G: levenchuk-canonical | R: R-high (verbatim primary source, multiple loc)`

Альтернативная Левенчуковская формулировка:
> «[FPF's] mission is to provide a transdisciplinary architectural synthesis of these powerful, "obvious" ideas, transforming them from disconnected heuristics into a coherent, interoperable, and fully-governed "operating system for thought."»

`[FPF-Spec.md около L755 — "transdisciplinary architectural synthesis"]`

И ещё:
> «In plain language: FPF turns raw intelligence into work that is easier to align, review, evolve, and delegate.»

`[Readme.md:132]`

**После §1 ты можешь** одной фразой объяснить, что есть FPF: операционная система для мышления + работы инженерных/исследовательских/смешанных human/AI команд; не методология, не encyclopedia, не tool stack.

---

## §2 FPF в одном абзаце (30-секундный elevator)

> **Per §1.3 acceptance criterion: 30-секундный сжатый surface.**

FPF — это **pattern language** (300+ patterns по состоянию на май 2026), организованный как нормативный kernel + расширения, написанный на «neutral English для AI-agent readability + type-safety across bounded contexts» `[R-A §4.1 L263]`. Это не методология (Agile / Waterfall) и не encyclopedia: это **архитектура для рассуждения** — набор переиспользуемых паттернов и working forms, которые помогают командам превращать tacit thinking в shared reviewable work `[Readme.md L124]`. Каждый паттерн — это **контракт** в форме `Problem frame → Problem → Forces → Solution + Conformance Checklist` `[FPF-Spec.md около L348]`. FPF specifically нужен когда bottleneck — не raw ideation (LLMs уже сильны в этом), а **coordination, vocabulary stability, explicit trade-offs, clean hand-offs** `[Readme.md L35 + L167]`. FPF — не один документ + код, а одна большая spec (72 800 строк @ c86eabd) + Readme; других «FPF-related» документов нет — Левенчук explicit в TG 2026-05-17: «всего один — github.com/ailev/FPF (ладно, два: ещё README.md)» `[inbox/levenchuk-tg-2026-05-17.md:26]`. Active dev май 2026: **E.10.SEMIO campaign** (semiotic boundary statements) + **A.6.P** (compression-decompression / role-publication discipline).

**После §2 ты можешь** в 30 секунд объяснить scope, форму (pattern language с контрактами), бутылочное горло которое FPF снимает (coordination), и состояние корпуса (1 spec + 1 readme; не 100+ файлов).

> **Inline mermaid pointer.** Top-level FPF architecture — см. `diagrams/01-fpf-top-level-architecture.md`.

---

## §3 5+ primitives FPF (verbatim definitions)

> **Source key.** `[FPF L###]` = `raw/external/ailev-FPF/FPF-Spec.md` строка в snapshot c86eabd.
> `[R-B §X]` = ШСМ primitives extraction из Левенчуковский корпус. Левенчуковский термин в Spec — `U.<Name>` (Universal namespace).

### §3.1 U.Holon — единица композиции

**Definition (verbatim Spec около L1149):**
> «`U.Holon` — Unit of Composition. A `U.Entity` that is *simultaneously* **(a)** a whole composed of parts and **(b)** a part within a larger whole. Formally, `U.Holon ⊑ U.Entity`.»

`F: F8 | G: levenchuk-canonical | R: R-high`

**Role.** Holon — фундаментальная единица композиции в FPF. Universal aggregation operator **Γ** работает only on sets of `U.Holon`, never on bare `U.Entity`.

**Two sub-archetypes:**
- `U.System ⊑ U.Holon` — физический, operational holon obeying conservation laws (e.g. nuclear plant, organization, codebase)
- `U.Episteme ⊑ U.Holon` — knowledge claim holon (e.g. safety case, theory, evidence graph)

**Example (verbatim, paraphrased section around L578):**
> «A complex `U.System`—whether a nuclear plant, a corporate strategy, or a causal model—cannot be captured by a single "truth document". It is described by a family of connected epistemes (`U.Episteme`), each rigorous, each partial, and each obtained from the others by law-governed morphisms rather than copy-and-paste edits.»

**Cross-ref.** Builds on P-8 Cross-Scale Consistency. Prerequisite for A.1.1 BoundedContext, A.2 Role Taxonomy, A.14 Advanced Mereology, B.1 Universal Γ.

---

### §3.2 U.BoundedContext — locally-closed semantic frame

**Definition (verbatim Spec, A.1.1):**
> «`U.BoundedContext` (A.1.1) — This is the primary mechanism for establishing a local CWA [Closed-World Assumption]. Within a Bounded Context, a specific set of models, rules, and invariants is declared to be authoritative. Any statement that violates an invariant *within that context* is considered false.»

`F: F8 | G: levenchuk-canonical | R: R-high`

**Why it matters (verbatim Readme L201):**
> «**Local meaning, explicit translation.** Terms live inside bounded contexts: local working frames with their own meanings. Cross-context reuse is never obvious; it needs an explicit bridge.»

**Pairs with.** F.9 Bridges (lawful cross-context translation), F.11 (method/work vocabulary alignment), F.17 UTS (Unified Term Sheet).

---

### §3.3 U.Role — функциональная позиция, отличная от executor

**Definition (verbatim Левенчук «Методология 2025» via R-B):**
> «Агенты имеют роли в методе. […] Создатели – это агенты, всё что из методов умеет делать агент – это личность агента. […] Если говоришь роль, то за ролью скрывается метод.»

`[R-B §1.1 L41-48; ailev-1741032]`
`F: F6 | G: levenchuk-canonical | R: R-medium (LJ post, not in Spec verbatim)`

**R-B operational formula:**
> **«Роль = сигнатура метода × интерес к системе × набор мастерства. Конкретный исполнитель — носитель роли, но не сама роль.»** `[R-B §1.1 L55]`

**FPF encoding:** `A.2 Role Taxonomy`, `A.2.1 U.RoleAssignment`, `A.2.5 U.RoleStateGraph`, `A.13 Agential Role` («FPF models agency without minting a U.Agent type»), `A.15 Role–Method–Work`.

**Critical operational rules** `[R-B §1.3-1.6]`:
1. Roles assigned at task-creation, **NEVER dynamic self-assignment** — иначе «разрушает граф создания и систему альф»
2. Name = **method** ("Sales Lead"), not executor ("Claude Agent #3") or RACI ("Ответственный")
3. ≤7 accountability items per role; else decompose
4. Use established cultural labels («моряк»), not inventions («морепроходимец») — discovery > design

---

### §3.4 U.Method (+ U.MethodDescription + U.Work) — Transformer Quartet

**Component (verbatim Spec, A.3):**
> «`U.Method` & `U.MethodDescription` (A.3) — Provides a universal, representation-agnostic way to describe *how* an action is performed, from a physical process to a line of reasoning.»

`F: F8 | G: levenchuk-canonical | R: R-high`

**Quartet structure** `[FPF Part A row A.3 + A.15]`: **System-in-Role / MethodDescription / Method / Work**.
- **MethodDescription** = design-time capability (how-to spec)
- **Method** = bound to context (actualized)
- **Work** = run-time enactment (что фактически произошло)
- **System-in-Role** = носитель (carrier)

**Левенчук Feb 2026 LJ post 1788706:** «Establish Method as design-time capability, Work as run-time enactment» — current FPF dev clarifying this split `[02-livejournal/key-posts-captured-2026-05-17.md §Post 2]`.

**Cross-ref.** A.15 Role–Method–Work seam; A.15.1 U.Work; A.15.2 U.WorkPlan.

---

### §3.5 U.Alpha (ШСМ primitive — encoded in FPF под другим словом)

**ШСМ definition (verbatim Левенчук «Методология 2025» via R-B):**
> «Альфа – это предмет метода, который может быть и физическим объектом (системой), и абстрактным объектом (описанием). […] Альфа позволяет управлять вниманием создателя в ходе исполнения длинных цепочек операций. […] Альфа помогает отследить судьбу предмета метода в проекте.»

`[R-B §2.1 L162-166]`
`F: F6 | G: levenchuk-canonical | R: R-medium (Methodology-2025 textbook quote)`

**SEMAT origin (Jacobson 2012):**
> «An alpha is an essential element of the software-engineering endeavor… relevant to an assessment of its progress and health.»
`[R-B §2.1 L170; Левенчук extended from software-only к any project situation R-B §2.1 L176]`

**Левенчук 2024 LJ post 1718836 (current ШСМ kernel — 4 primary alphas):**
1. System embodiment (воплощение системы)
2. System description (описание системы)
3. Way of working / function (функция/метод работ)
4. System operations (работы системы)

**Critical state-naming convention:** past-participle для machine-readability — «потребность определена», «быть выбранным», «быть закупленным», «быть проверенным в работе» `[LJ post 1718836]`. Enables `IF Client.state == "Qualified" THEN…` `[R-B §2.4 L246]`.

**FPF encoding (word "alpha" absent in Spec verbatim; mechanism preserved):**
- `A.2.5 U.RoleStateGraph` — state machines over roles
- `A.15.1 U.Work` — work artefacts с state
- `C.2.1 U.EpistemeSlotGraph` — episteme slot tracking
- `B.5.1 Explore→Shape→Evidence→Operate` — lifecycle pattern

> **Note on word choice.** Слово «alpha» в FPF Spec verbatim не встречается; механизм — да (A.2.5 + A.15.1 + C.2.1). Почему именно так Левенчук решил — мы не атрибутируем; это наблюдаемый факт, не интерпретация.

---

### §3.6 Граф создания (Creation Graph) — three-level mereology

**ШСМ definition (verbatim Левенчук):**
> «Моделировать граф создания […] по мотивам OMG Essence 2.0:2024. Агенты-создатели (тогда – люди и их организации, сейчас включаем и AI) как надсистемы целевой системы… не менее важны, чем создаваемая ими целевая система.»

`[R-B §3.1 L323; L329-331]`
`F: F6 | G: levenchuk-canonical | R: R-medium`

**Three-level structure** `[R-B §3.4]`:

```
Level 3  НАДСИСТЕМА             ← operates-in / constrained-by
Level 1  ЦЕЛЕВАЯ СИСТЕМА        ← creates / methodologically-uses
Level 2  СИСТЕМЫ СОЗДАНИЯ
```

Five typed edges: `part-of`, `creates`, `operates-in`, `methodologically-uses`, `constrained-by`.

**Holonic basis (verbatim Левенчук ailev-1776793):**
> «За основу мы берём мереологию холонов… конструированием из частей и входимостью в другие целые как части.»

**FPF encoding:**
- `A.1 Holonic Foundation` — base
- `A.14 Advanced Mereology`
- `B.2 Meta-Holon Transition` — emergence cross-level

**Critical anti-patterns** `[R-B §3.2 L344-348]`: NOT workflow/BPMN, NOT dependency tree, NOT org chart, NOT supplier-consumer bipartite. Every node = a system. Every edge = creation/operation/use.

---

### §3.7 Стратегирование (Strategizing) — meta-method choosing method

**Definition (verbatim Левенчук «Методология 2025»):**
> «Метод выбора метода – стратегирование. […] Выбирать новый метод работы в условиях, когда вообще непонятно, что делать. А если непонятно, что именно делать, то и планировать ещё ничего нельзя (потребные ресурсы неизвестны, ведь непонятно, каким методом работаем) и работать нельзя.»

`[R-B §4.1 L442-444]`
`F: F6 | G: levenchuk-canonical | R: R-medium`

**Левенчук ailev-1779269:**
> «Почему стратегирование? Потому что на этом пути надо не научиться решать проблемы, а надо научиться ставить новые goldilocks проблемы и находить новые и новые недоминируемые решения.»

`[R-B §4.1 L450]`

**Strict ordering** `[R-B §4.1 L454-461]`:
```
Стратегирование → Планирование → Работа
```
Planning IMPOSSIBLE before strategizing completes.

**Trigger-based, NOT scheduled** `[R-B §4.2]`. Valid triggers: market signal / alpha failure / method exhaustion / irreversible decision / boundary change / new role without known method / quarterly reset *only if real uncertainty*. Scheduled strategizing = «performance ritual» → «методы-конвульсии».

**Three method-modes** `[R-B §4.3]`: 1:1 (known, no change → full AI auto) / Adapt (known, tuned → AI + oversight) / **Invent** (unknown → human only).

**Critical constraint (Левенчуковский):** «AI agents do NOT strategize» — no identity/commitment (session-fresh), no long-term SoTA memory, no skin-in-the-game (Taleb) `[R-B §4.3 L510-524]`.

**FPF encoding:**
- `B.4 Canonical Evolution Loop`
- `B.5 Canonical Reasoning Cycle` (Abduction→Deduction→Induction; Explore→Shape→Evidence→Operate)
- `B.5.2 Abductive Loop`
- `B.5.2.1 Creative Abduction with NQD`
- `E.9 DRR (Design Rationale Record)`
- `C.17-C.19 NQD-CAL / E-E-LOG`

---

### §3.8 Мышление письмом (Writing-as-Thinking)

**Definition (verbatim Левенчук «Системное мышление 2024 т.1»):**
> «Системное мышление происходит путём мышления моделированием… и письмом (с текстами на естественных языках, но с отслеживанием типов объектов и видов отношений объектов в этих текстах), поэтому внимание… удерживается… всё время проекта: записанное не так легко забыть в суете.»

`[R-B §5.1 L605]`
`F: F6 | G: levenchuk-canonical | R: R-medium (textbook)`

**FPF dedicated Preface section "Thinking Through Writing" (около L515-535):**
> «This "writing" is not a by-product of thinking; it *is* the thinking. The act of filling out a **Role Description Card** or constructing a **Concept-Set Table** is not mere documentation; it is the cognitive work of making distinctions, declaring invariants, and justifying relationships.»

**Operationalized via:** Cards (F.1, F.4), Tables (F.17 UTS), Records (E.9 DRR), Conformance Checklists.

**Quality test** `[R-B §8.5]`: «Узнал ли я что-то новое в процессе написания?» — yes = real writing-as-thinking.

**AI constraint (verbatim Левенчук)** `[R-B §5.5 L690]`:
> «Без внешнего по отношению к LLM контуру обработки текста — никак, LLM всегда обманет. Если и сам текст пишет LLM — исчезает "мышление письмом" как когнитивный процесс.»

---

### §3.9 Additional FPF primitives (briefly — для polysemy)

- **U.Episteme** (`C.2.1 EpistemeSlotGraph`) — knowledge claim as holon с slots: DescribedEntity / GroundingHolon / ClaimGraph / Viewpoint. **DETAILS в `02-iwe-deep-v2.md`.**
- **U.Capability** — domain-agnostic capacity referenced by Intellect Stack
- **U.Characteristic / U.Scale / U.Level / U.Coordinate** — measurement primitives (A.17-A.19)
- **U.View / U.EpistemeView** — for multi-view publication (E.17)
- **U.UTS (Unified Term Sheet)** — vocabulary stabilization artifact (F.17)
- **U.DRR (Design Rationale Record)** — decision documentation artifact (E.9)

**После §3 ты можешь** называть и кратко определять минимум 5 universal primitives FPF (U.Holon, U.BoundedContext, U.Role, U.Method+Work, U.Episteme) и видеть их Левенчуковский базис в R-B extracts.

---

## §4a Core mechanisms FPF — canonical (что в Spec)

> **Boundary discipline (mgmt × critic D4 + phil × critic HS-1).** Здесь только Spec-canonical
> mechanisms. RUSLAN-LAYER Jetix-internal mapping — отдельно в §4b с явным disclaimer.
> Эта секция отвечает на вопрос «какие mechanisms ЕСТЬ в FPF» — без нашей атрибуции.

### §4a.1 A.6.B Claim Register (boundary discipline)

**Source.** `FPF-Spec.md` Part A boundary discipline cluster. Per Readme L65:

> «**Boundary unpacking** — Use this when: contract, API, protocol, compliance, or SLA language is mixing rules, gates, duties, and evidence in one blurred boundary story. You will leave with: a Claim Register, meaning a split list of rules, gates, duties, and evidence claims. Start with: `A.6`, then `A.6.B`, then `A.6.C`.»

`F: F8 | G: levenchuk-canonical | R: R-high`

**Mechanism.** Boundary text (contract / SLA / spec) → atomic claims → typed register (rule / gate / duty / evidence). Prevents «contract soup drift».

### §4a.2 A.6.P Compression-Decompression / Role-Publication Discipline

**Source.** Active dev cluster Feb 2026, refreshed май 2026 commit `c86eabd` (см. CHANGELOG).
Per LJ post 1788706 (Feb 2026):
> «управление сжатием-разжатием в языке… routing of context/boundary statements and lexical precision in signatures/relations/interfaces»

`[02-livejournal/key-posts-captured-2026-05-17.md §Post 2]`
`F: F4 | G: levenchuk-canonical-active-dev | R: R-medium (active dev, not yet stable)`

**Mechanism (по нашему разбору, не verbatim spec).** A.6.P формализует publication discipline: какой текст идёт в какой viewpoint, кто owner publication-canal, как «сжать» внутреннее знание в публикуемый surface без потери boundary integrity.

### §4a.3 A.14 Advanced Mereology

**Source.** `FPF-Spec.md` row A.14 «Advanced Mereology» builds on A.1 Holonic Foundation + B.2 MHT.

`F: F8 | G: levenchuk-canonical | R: R-high`

**Mechanism.** Defines part-whole structure with explicit `part-of` typed edges + 4D extensionalism (per Левенчуковский ISO 15926 lineage in R-A §1.2). Enables creation-graph-style three-level reasoning generalized к any holon hierarchy.

**Use.** Когда нужно reason about super-system / target / enabling system без minting separate types — все три = holons related via Γ aggregation.

### §4a.4 B.3 F-G-R Trust & Assurance

**Source.** `FPF-Spec.md` Part B.3 «F-G-R Trust & Assurance».

`F: F8 | G: levenchuk-canonical | R: R-high`

**Mechanism.** Each claim tagged with:
- **F (Formality):** F2-F8 spectrum (informal sketch → math-proof)
- **G (Group-scope):** what audience / what stake group
- **R (Reliability):** R-low / R-medium / R-high (evidence strength)

**Why.** Without F-G-R, «claim about claim X» loses track of whether X is informal note, audited engineering data, or formal theorem. Audit trail integrity.

**Assurance levels (B.3.3):** L0 Unsubstantiated требует явного human acceptance.

**После §4a ты можешь** назвать 4 canonical FPF mechanisms из Spec (A.6.B Claim Register, A.6.P Publication discipline, A.14 Advanced Mereology, B.3 F-G-R Trust) и понимаешь, что они — FPF Spec content, не наша интерпретация.

---

## §4b RUSLAN-LAYER Jetix-internal mapping (НЕ canonical FPF — наш разбор)

> **БОЛЬШОЙ DISCLAIMER (phil × critic HS-1 + mgmt × critic D4).** Здесь — наша Jetix-internal
> карта (RUSLAN-LAYER per CLAUDE.md §4.2). Это **НЕ Левенчуковские патерны.** Это наши
> правила, которые мы маппим к FPF эквивалентам. Если Левенчук читает: эти `IP-1`..`IP-7` —
> наши, не его. Левенчуковский эквивалент указан per IP.

### §4b.1 IP-1 Role≠Executor (Jetix RUSLAN-LAYER — наш термин)

**Source.** Bundle 1 RUSLAN-ACK 2026-04-28 (см. `CLAUDE.md §4.1 rule 4` — «AI does NOT claim persistent identity beyond `acting_as` role»). Левенчуковский базис в R-B §1.1:
> «Создатели – это агенты, всё что из методов умеет делать агент – это личность агента.»

**Levenchuk-equivalent.** `A.2 Role Taxonomy` + `A.13 Agential Role` («FPF models agency without minting a U.Agent type»). **Это NOT a separate FPF pattern named "IP-1"; IP-1 = наш Jetix-internal label.**

**Role-level operations (RUSLAN-LAYER):**
- Role = method-signature (functional)
- Executor = agent (carrier — human or AI)
- Bind at task-creation, not at role-definition

**Why critical (наш разбор).** Без separation: (1) personnel changes = role changes = method changes (cascading instability); (2) AI executor changes (Claude 4.6 → Opus 4.7) = role changes (false coupling); (3) accountability untraceable.

### §4b.2 IP-2 Foundation Gate (Jetix RUSLAN-LAYER)

**Source.** Bundle 1 IP-2 (см. `CLAUDE.md §4.1 rule 2` — «AI does NOT execute architectural decisions автономно»).

**Levenchuk-equivalent.** DRR-as-decision-rationale gate (E.9) + Rule-of-Constraints. Spec L558-568 verbatim:
> «Declare *what must not happen*… agents have freedom to choose *how* to act.»

**Mapping (наш разбор).** Наш «AI does NOT execute architectural decisions автономно» = FPF Rule-of-Constraints (deontic limits) + DRR (publish change rationale).

### §4b.3 IP-3 / IP-7 (Jetix RUSLAN-LAYER — наши)

**Source.** Bundle 1 RUSLAN-ACK. Не Левенчуковские паттерны.

- **IP-3** = «AI does NOT set capability/skill direction» (CLAUDE.md §4.1 rule 3). Levenchuk-equivalent ≈ E.5.x Guard-Rails (boundary of what FPF can claim).
- **IP-7** = «No autonomous contradiction negotiation» (CLAUDE.md §4.1 rule 7). Levenchuk-equivalent ≈ B.5 reasoning cycle + assurance escalation (humans authorize when assurance level low) + B.3.3 L0 Unsubstantiated requires human acceptance.

### §4b.4 Сводная таблица RUSLAN-LAYER → FPF canonical

| Jetix RUSLAN-LAYER | Levenchuk canonical equivalent | F-G-R |
|---|---|---|
| IP-1 Role≠Executor | A.2 Role Taxonomy + A.13 Agential Role | F4 / Jetix-internal / R-medium |
| IP-2 Foundation Gate | E.9 DRR + Rule-of-Constraints (Spec L558-568) | F4 / Jetix-internal / R-medium |
| IP-3 Capability direction | E.5.x Guard-Rails (deontic limits) | F3 / Jetix-internal / R-medium |
| IP-7 Contradiction escalation | B.5 reasoning + B.3.3 L0 assurance | F3 / Jetix-internal / R-medium |
| R12 Anti-extraction (candidate Rule 12) | NOT in FPF (Jetix-unique, см. §7) | F2 / Jetix-internal / R-low |

> **F-G-R audit invariant.** Каждая строка таблицы выше — `F: F3-F4 | G: jetix-internal | R: R-medium`.
> Это means: формальность под F5; scope = только Jetix; reliability — наш разбор без peer review извне.

**После §4b ты можешь** различать: что в FPF Spec canonical (§4a), что наш Jetix-internal mapping (§4b). Не путать.

---

## §5 Принципы мышления и интеллекта, положенные в основу FPF

> **Per prompt §3.1 point 5 и ключевой Левенчуковский claim C2 в TG message 2026-05-17:**
> «Там есть довольно много открытых описаний о принципах мышления и интеллекта,
> которые положены в основу.» `[inbox/levenchuk-tg-2026-05-17.md:46]`

### §5.1 Семь Core ideas (verbatim Readme L201-208)

> «FPF is built on a small kernel of non-negotiable ideas. New readers do not need the internal pattern names immediately; the point of this section is to explain what the framework buys you before you dive into its internal map.
>
> 1. **Local meaning, explicit translation.** Terms live inside bounded contexts: local working frames with their own meanings. Cross-context reuse is never obvious; it needs an explicit bridge.
> 2. **One underlying reality, many aligned outputs.** Engineering, management, research, and assurance outputs should be projections of the same underlying work, not disconnected documents.
> 3. **Separate systems, roles, method descriptions, methods, plans, and executed work.** Descriptions, capabilities, plans, and actual occurrences are not the same thing.
> 4. **Trust has structure and grounding.** A claim should say how formal it is, where it applies, what evidence supports it, and which carriers or systems anchor it.
> 5. **Composition matters across scales.** The same logic should survive when parts are aggregated into wholes.
> 6. **Keep search wide before selection.** In open-ended work, diversity of options matters before choosing a winner.
> 7. **Build from first principles when categories break.** FPF is not only for organising the current state of the art; it is also for growing new abstractions.»

`F: F8 | G: levenchuk-canonical | R: R-high`

### §5.2 «Big storylines» unique to FPF

> «1. **Holonic kernel with physical anchoring** — everything that composes is a `U.Holon`; every change is enacted by an **external transformer** (A.1; A.12).»

`F: F8 | G: levenchuk-canonical | R: R-high`

Other commitments (excerpt):
- Trans-disciplinarity as meta-theory of thinking (C-1)
- Pattern language with Conformance Checklists (E.8)
- Open-Ended Evolution as canon (P-10)
- Multi-View Publication architecture (E.17)
- Notational Independence guard-rail (E.5.2)

### §5.3 Eleven Pillars (E.2) — Constitution (partial — Phase A extracted)

Per Spec L745: «**Constitution**—the **Eleven Pillars (E.2)** plus the **Guard-Rails (E.5.\*)**—that constrains all normative content».

Identified Pillars (referenced throughout Spec — Phase B will complete with full list extraction):
- **P-1 Cognitive Elegance**
- **P-2 Didactic Primacy** (Tell-Show-Show; manager-first didactics)
- **P-7 Pragmatic Utility**
- **P-8 Cross-Scale Consistency**
- **P-10 Open-Ended Evolution** (Pillar; NQD/E-E-LOG are the engine parts per Spec L770)

> **Honest gap (phil × critic HS-3).** Full P-1 through P-11 list not exhaustively extracted Phase A.
> Spec contains the full list inside Part E; will be completed Phase C если Ruslan нужно полностью.

### §5.4 Откуда принципы (lineage)

Per R-A §1.2 lineage:

| Layer | Influences |
|-------|------------|
| 1st gen systems thinking | Bertalanffy GST, Wiener cybernetics, Koestler holons |
| 2nd gen (absorbed + critiqued) | Checkland SSM, ISO 15288/42010/15926, SEMAT Essence (Jacobson) |
| 3rd gen (Левенчук synthesis 2020s) | techno-evolution, continuous-everything, mereotopology + category theory, Active Inference (Friston), open-ended evolution (NQD OEE) |
| Russian methodology | engaged + критикованo ΣМД (Shchedrovitsky) |
| Philosophical | Peirce (pragmatism, semiotics), Searle (speech acts), Popper (epistemology), Dennett (anti-essentialism), praxeology (Mises) |

`[R-A §1.2 L52-66]`
`F: F4 | G: jetix-synthesis | R: R-medium (наш разбор lineage; Левенчук может уточнить)`

> **Per prompt §3.1 point 11 — full methodology lineage в отдельном файле `04-methodology-lineage.md`.**

**После §5 ты можешь** перечислить 7 core ideas + 5 unique storylines + partial Pillars list + lineage layers; знаешь, что constituirовалo FPF как architectural synthesis.

---

## §6 Intelligence amplification mechanism — конкретный механизм

> **Per prompt §3.1 point 6 — это ключ к ответу на C3/C4 Левенчука.**
> «Как именно FPF превращает обычный thinking process в более качественный?»

### §6.1 Левенчуковский answer (verbatim Readme L165-171)

**Why FPF when AI-agents keep getting stronger?**

> «- **Because coordination, not raw generation, becomes the bottleneck.** Stronger LLMs reduce local reasoning scarcity, but they do not remove the need for selection, auditability, safe delegation, and shared understanding across people, agents, time, and viewpoints.
> - **Because local working frames still matter.** FPF keeps teams from pretending that product, safety, operations, and research all use one universal vocabulary.
> - **Because many real projects cannot just loop until tests pass.** In product, field engineering, strategy, marketing, safety, or open-ended research, the real-world oracle is delayed, noisy, expensive, or risky. FPF aims to catch anti-patterns before contact with the world.
> - **Because the same framework can serve both humans and AI.** AI agents can read the specification directly; humans can learn the same working model through didactic layers and the pedagogical companion.
> - **Because FPF pays off past a complexity frontier.** It matters most when the problem becomes simultaneously compositional, collaborative, temporal, assurance-heavy, and generative.»

`[Readme.md L165-171]`
`F: F8 | G: levenchuk-canonical | R: R-high`

### §6.2 The Pareto frontier of complexity (verbatim Spec около L793)

> «FPF's utility begins to scale exponentially when the problem itself crosses a **Pareto frontier of complexity**, where the "general cultural knowledge" of even a brilliant individual becomes suboptimal. This frontier is defined not by mere computational difficulty, but by the emergence of several non-computational dimensions:
>
> - **Compositional Complexity** — heterogeneous parts → coherent whole
> - **Collaborative Complexity** — diverse team alignment
> - **Temporal Complexity** — solution lives + adapts long term
> - **Assurance Complexity** — explicit, auditable proof of safety/reliability
> - **Generative Complexity** — systematically explore vast solution space, manage portfolio
>
> An expert's intuition can find a single, excellent point on this multi-dimensional frontier. FPF provides the architectural discipline to navigate the entire frontier.»

`F: F8 | G: levenchuk-canonical | R: R-high`

### §6.3 По нашему пониманию — 7 паттернов intelligence amplification (наш разбор, не Левенчуковская формулировка)

> **Boundary disclaimer (phil × critic HS-2).** Эта секция — наш Jetix-internal synthesis по
> FPF Spec + Readme. Левенчук **нигде не говорит** «7 механизмов intelligence amplification».
> Это наша структура для понимания. Если Левенчук читает — это наш разбор, не его формулировка.
> `F: F3 | G: jetix-synthesis | R: R-medium (наш synthesis; refutable если Левенчук дает другой счёт)`

**FPF превращает "raw intelligence" в "amplified collective work" через 7 паттернов** (each anchored к конкретному canonical pattern in Spec):

1. **Bounded-context map (A.1.1)** — defines *where* each piece of reasoning lives.
   - Без этого: implicit context drift; LLM hallucinates because context boundary not declared.
   - С этим: claims tied к context; cross-context translation explicit (F.9 Bridges).

2. **Roles + Method-signatures (A.2 + A.3 quartet)** — separates what role does (method-signature) from who does it (executor).
   - Без этого: roles = system prompts; AI overfits to executor identity.
   - С этим: agent swapping без method changes; accountability traceable.

3. **Alpha-state-graphs / U.RoleStateGraph (A.2.5)** — past-participle states with checklists.
   - Без этого: project status = "in progress" (informationless).
   - С этим: machine-checkable status; AI onboarding briefing = compact alpha-state list.

4. **F-G-R per claim (B.3 assurance)** — formality / group-scope / reliability tags.
   - Без этого: every output looks equally authoritative; reader can't triage.
   - С этим: audit trail of trust level per assertion.

5. **DRR (E.9 Design Rationale Record)** — durable decision record.
   - Без этого: «why did we do X?» answer lost after team rotation (Naur's "theory death").
   - С этим: rationale + alternatives + open-issues preserved.

6. **Abductive Loop (B.5.2) + Open-Ended Search (C.17-C.19)** — explore wide before selection; explore/exploit governor.
   - Без этого: AI converges на first-plausible answer.
   - С этим: portfolio of alternatives surfaced; trade-offs explicit.

7. **Multi-View Publication (E.17 MVPK)** — one underlying work → multiple aligned outputs (engineering / management / research / assurance).
   - Без этого: each audience gets disconnected doc; drift over time.
   - С этим: same reasoning projected через viewpoint bundles; reports cannot drift from reality without tearing audit trail.

> **Inline mermaid pointer.** Step-by-step amplification workflow — см. `diagrams/02-intelligence-amplification-workflow.md` (10 steps F1-F10 не строгий sequential — concurrent disciplines applied to the SAME work).

### §6.4 Why this is intelligence amplification (NOT memory/automation) — verbatim Spec

**Verbatim Spec около L755 — transdisciplinary synthesis:**
> «FPF does not seek to invent the fundamental ingredients of rigorous thought. Its purpose is not to discover that evolution is effective or that empirical testing is valuable. Its mission is to provide a **transdisciplinary architectural synthesis** of these powerful, "obvious" ideas, transforming them from disconnected heuristics into a coherent, interoperable, and fully-governed "operating system for thought."»

`F: F8 | G: levenchuk-canonical | R: R-high`

**Verbatim Spec около L592 (FPF as generative architecture):**
> «FPF is a **generative architecture for thought**. Its primary purpose is not to diagnose errors, but to provide a structural scaffold that makes entire classes of errors difficult or impossible to commit in the first place.»

`F: F8 | G: levenchuk-canonical | R: R-high`

**Verbatim Spec около L606:**
> «In this way, FPF is not a replacement for critical thinking and creative thinking but its **engineering reinforcement**. It provides the architectural integrity, shared vocabulary, and formal discipline necessary to move from merely avoiding mistakes and generate ad hoc ideas to reliably generating trustworthy and auditable insights.»

`F: F8 | G: levenchuk-canonical | R: R-high`

> **Jetix self-positioning vs C3 — moved out (mgmt × critic D6).** Анализ «где наша Foundation v1.0 = «память+автоматизация» vs amplification» вынесен в `06-honest-self-audit.md` (a) чтобы этот файл оставался FPF-on-human-language без Jetix self-analysis в теле, (b) self-audit — отдельный жанр.

**После §6 ты можешь:** (1) verbatim процитировать Левенчука «coordination, not raw generation» + «Pareto frontier» + «generative architecture»; (2) перечислить 7 паттернов наш разбор; (3) понимать различие «intelligence amplification» vs «память+automation» по Spec.

---

## §7 Что мы НЕ вытащили Phase A (gap registry — для honesty)

- **Full E.2 Eleven Pillars list** — referenced throughout но не отдельно extracted (TO-COLLECT Phase C если приоритет)
- **Full E.5.\* Guard-Rails list** — referenced (E.5.1 DevOps Lexical Firewall, E.5.2 Notational Independence) но не exhaustive
- **A.6.A Action-Quality (downstream branch)** — current dev cluster per Feb 2026 LJ post
- **C.17 / C.18 / C.19 NQD / E-E-LOG detailed mechanics** — only названия + general role; full pattern bodies TO-COLLECT
- **E.10.SEMIO campaign** — active dev as of c86eabd 2026-05-16 upstream; not yet stable; CHANGELOG flags + freshness §0 notes
- **A.6.P Compression-Decompression** — active dev; §4a.2 above gives the surface; full mechanic не fully extracted

These gaps don't undermine the §1-6 surface — они дополняют depth, не contradict.

---

## §QR-CARD Quick Reference Card (lookup без чтения)

> **One-screen card** для быстрого вспоминания. Cross-ref в полный текст по anchor.

**FPF одной фразой.** «Operating system for thought for engineering, research, and mixed human/AI teams.» `[Readme L9]`

**5 primitives.**

| Primitive | Что | Anchor |
|---|---|---|
| U.Holon | Единица композиции (whole + part одновременно) | §3.1 |
| U.BoundedContext | Локально-закрытый semantic frame (local CWA) | §3.2 |
| U.Role | Functional position ≠ executor; method-signature | §3.3 |
| U.Method+Work (quartet) | MethodDescription + Method + Work + System-in-Role | §3.4 |
| U.Episteme | Knowledge claim as holon (slots) | §3.9 + 02-iwe-deep-v2 |

**4 canonical FPF mechanisms.**

| Mech | Что | Anchor |
|---|---|---|
| A.6.B Claim Register | Boundary text → atomic claims (rule/gate/duty/evidence) | §4a.1 |
| A.6.P Publication discipline | Compression-decompression + role-publication routing | §4a.2 |
| A.14 Advanced Mereology | Part-whole с typed edges + 4D extensionalism | §4a.3 |
| B.3 F-G-R Trust | Per-claim formality/scope/reliability tagging | §4a.4 |

**7 паттернов intelligence amplification (наш разбор, NOT Левенчуковская формулировка).**
1. Bounded-context map (A.1.1)
2. Roles + method-signatures (A.2 + A.3)
3. Alpha-state-graphs (A.2.5 / A.15.1)
4. F-G-R per claim (B.3)
5. DRR durable decisions (E.9)
6. Abductive loop + open search (B.5.2 + C.17-C.19)
7. Multi-View Publication (E.17 MVPK)

**3 verbatim Левенчуковский one-liners.**
- «Coordination, not raw generation, becomes the bottleneck.» `[Readme L167]`
- «FPF is a generative architecture for thought…» `[Spec ≈L592]`
- «У Церена IWE… внутри там интеллект опирается на тот же FPF — и понятно, за счёт чего его IWE умнее конкурентов.» `[TG 2026-05-17]`

**Canonical source.** `github.com/ailev/FPF` @ `c86eabd` 2026-05-16 (FPF-Spec.md 72 800 lines + Readme.md). All ссылки выше — относительно этого snapshot.

**Active dev clusters.** E.10.SEMIO + A.6.P (см. §0 freshness).

**RUSLAN-LAYER labels (НЕ canonical FPF).** IP-1/IP-2/IP-3/IP-7 — наш Jetix-internal; details §4b. Левенчук **никогда не использовал** эти лейблы; это наш mapping к Spec эквивалентам (A.2, E.9, E.5, B.5).

---

*v2 complete. Integrated по 3 critic drafts (eng + phil + mgmt) per brigadier §5.5.5 gate.
Размер: ~750-800 lines. Acceptance criterion: L1 reader extracts FPF surface за 30 минут;
namespace contamination (§4 v1) исправлено split'ом §4a canonical / §4b RUSLAN-LAYER.*
