---
title: Phase 7 — OMG Essence Kernel + Method Engineering standards (SEMAT + Brinkkemper SME + ISO/IEC 24744)
date: 2026-05-24
phase: 7
parent_prompt: prompts/research-methodology-2026-05-24.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2 (verbatim citations) + F3 (synthesis)
G: research-methodology
R: refuted_if_R1_strategic_prose_authored_OR_LOCK_modified
constitutional_posture: R1 surface only + R2 + R6 + R11 + R12 + IP-1 + EP-5 + AP-6 + append-only + SKIP-list
status: phase-7 surface
language: russian primary
---

# Phase 7 — Method Engineering standards (OMG Essence Kernel + SEMAT + Brinkkemper SME + ISO/IEC 24744)

> **Цель.** Распаковать **standards-discipline side** of method engineering:
> formal standards that codify methodology-as-engineering. OMG Essence 2.0:2024
> = primary modern standard (Левенчук-anchor); ISO/IEC 24744:2014 = parallel
> SE methodology metamodel; SEMAT initiative = industrial backing; Brinkkemper
> SME (Situational Method Engineering) = academic foundation.

---

## §0 TL;DR (≤300w)

**Method Engineering = engineering discipline of constructing, evaluating, and
maintaining methods.** Differentiates from "methodology" in narrower sense by
focusing on **engineerable artefacts** (process descriptions, method fragments,
practices, alphas) rather than philosophical foundations.

**4 standards-discipline anchors:**

1. **Brinkkemper 1996** «Method Engineering: Engineering of information systems
   development methods and tools» — academic founding paper. SME = **situational**
   composition (one-size-fits-all rejected).
2. **ISO/IEC 24744:2014** «Software Engineering — Metamodel for Development
   Methodologies» — formal metamodel for representing development methodologies.
3. **SEMAT initiative 2009-** «Software Engineering Method And Theory» —
   Jacobson + Spence + Bittner industrial effort to put SE on rigorous footing.
4. **OMG Essence Kernel 1.0 (2014) → 2.0 (2024)** — adopted SEMAT work as OMG
   standard. **Левенчук primary anchor** для современной methodology pedagogy.

**Convergent methodology pattern:**
- Methods as composable artefacts
- Alpha-based state-graph tracking
- Practice-fragment library
- Way-of-Working assembly
- Health diagnostics
- Situational tailoring

**Jetix relevance:** Hypothesis Architecture 7-layer = OMG Essence alpha-machinery
applied; Foundation Parts 1-11 = essence-style architectural composition;
Method V2 §J 8-component = SME-style composition. Standards-grounding for Jetix
substrate already implicit; Phase 8 R1 can surface explicit standards-claim.

---

## §1 Brinkkemper 1996 — Situational Method Engineering foundation

### §1.1 Authority + paper

Sjaak Brinkkemper (Universiteit Utrecht) 1996 paper:
> Brinkkemper S. 1996 «Method engineering: engineering of information systems
> development methods and tools» Information and Software Technology 38(4):275-280
> https://doi.org/10.1016/0950-5849(95)01059-9

Defining paper for **Method Engineering as academic discipline**.

### §1.2 Central thesis

**Verbatim definition:**
> «The discipline to construct new methods from parts of existing methods,
> called method fragments.»

**Operations of method engineering:**
1. Decompose existing methods into reusable **method fragments**
2. Maintain **method base** (repository)
3. Assemble situation-specific methods by selecting + connecting fragments
4. Quality-control composed methods

### §1.3 Situational Method Engineering (SME)

**Brinkkemper-Saeki extension (1998):** even within software dev, **one method
does not fit all situations**. Each project carries unique combination of:
- Domain complexity
- Team size + skill
- Stakeholder count
- Technology stack
- Regulatory environment
- Time horizon

Therefore method needs **situational assembly** from method-base.

[src: Brinkkemper S., Saeki M., Harmsen F. 1998 «Assembly Techniques for Method
Engineering» CAiSE 1998 LNCS 1413]

### §1.4 Method fragment types

Brinkkemper-Saeki taxonomy of method fragments:

| Type | Description |
|---|---|
| **Process fragment** | Description of a development activity |
| **Product fragment** | Description of an artefact / deliverable |
| **People fragment** | Role specification |
| **Tool fragment** | Supporting technology |

### §1.5 Method Engineering vs ad-hoc methodology selection

| Approach | Pattern |
|---|---|
| Ad-hoc methodology selection | Pick "Agile" or "Waterfall" wholesale; force-fit project to method |
| Method Engineering | Diagnose project situation; assemble custom method from fragments |
| Situational Method Engineering | Add explicit situation-classification + fragment-selection algorithm |

**Implication:** SME = methodology-engineering elevated to engineering-discipline
(repository + composition rules + quality + validation).

### §1.6 SME literature lineage

- Brinkkemper 1996 (founding)
- Brinkkemper-Saeki 1998 (assembly techniques)
- Henderson-Sellers & Ralyté 2010 «Situational Method Engineering: State-of-
  the-Art Review»
- Henderson-Sellers, Ralyté, Ågerfalk, Rossi 2014 «Situational Method
  Engineering» (book; comprehensive)
- ME conference series (1996-)

### §1.7 Jetix-mapping

| SME concept | Jetix substrate |
|---|---|
| Method fragment | Cycle / phase / skill artefacts |
| Method base | swarm/wiki/ designs + foundations + cycles |
| Situational assembly | `/project-bootstrap --type=<4>` + ROY swarm dispatch |
| Situation classification | KM MVP project-types.yaml + .claude/config/* |
| Quality control | F-G-R triple + lint hooks + Default-Deny gate |

[src: Brinkkemper 1996 + KM-materialization-mvp + CLAUDE.md]

---

## §2 ISO/IEC 24744:2014 — Metamodel for Development Methodologies

### §2.1 Standard description

**Full title:** ISO/IEC 24744:2014 «Software engineering — Metamodel for
development methodologies» https://www.iso.org/standard/62644.html

**Purpose:** provides metamodel that allows different software development
methodologies to be described using common vocabulary and structure.

### §2.2 Architecture

Metamodel includes:
- **Methodology concepts:** process / artefact / role / model
- **Endeavour concepts:** project context (specific use of methodology)
- **Notation conventions:** UML stereotypes + ISO/IEC 24744 specific symbols
- **Conformance levels:** how strictly an implementation adheres to metamodel

### §2.3 Powertype pattern (key innovation)

ISO/IEC 24744 introduces **powertype pattern** для метамодельной representation:
class can be both an instance AND a class. Enables methodology composition:
- "TestCase" can be a class (concept) AND an instance (specific test case)
- Resolves classical metamodel ambiguity

### §2.4 Jetix-relevance

ISO/IEC 24744 less directly used by Jetix; OMG Essence is preferred Левенчук-
anchor. But powertype pattern useful concept: F-G-R triple has
similar "rule + instance" duality (rule applies to specific claim instances).

---

## §3 SEMAT initiative

### §3.1 Origin

**SEMAT = Software Engineering Method And Theory.** Founded 2009 by:
- Ivar Jacobson (UML co-creator, Rational founder)
- Bertrand Meyer (Eiffel)
- Richard Soley (OMG chairman)

**Manifesto:** software engineering lacked theoretical foundation; many
methodologies competing; need universal theory + practice base.

### §3.2 SEMAT call for action

Original manifesto (2009-) призывал к:
1. **Identify common ground** across methodologies
2. **Develop theoretical foundation** for SE
3. **Create kernel** of universal SE elements
4. **Build community** of practice

### §3.3 Initial OMG Essence Kernel 1.0 (2014)

SEMAT work formalised as OMG Essence Kernel 1.0 adopted 2014:
> OMG 2014 «Kernel and Language for Software Engineering Methods» version 1.0
> https://www.omg.org/spec/Essence/

### §3.4 Industrial backing

SEMAT/Essence backed by IBM, BBVA, Munich Re, MIT, et al. Adopted in some
enterprise SE practices. Critique: low adoption rate outside SEMAT-affiliated
companies; "another OMG standard" fatigue.

---

## §4 OMG Essence Kernel 2.0:2024 — Левенчук primary anchor

### §4.1 Standard status

**Latest version:** OMG Essence 2.0 (March 2024). https://www.omg.org/spec/Essence/2.0/

### §4.2 7 default alphas

Essence Kernel 1.0/2.0 defines 7 "Alphas" — fundamental things to manage
throughout software endeavour:

| Alpha | Description |
|---|---|
| **Opportunity** | Why are we doing this? Business case. |
| **Stakeholders** | Whose problem are we solving? |
| **Requirements** | What does it need to do? |
| **Software System** | What are we building? |
| **Work** | How is our endeavour going? |
| **Team** | Who's involved? |
| **Way-of-Working** | How will we work? |

Each Alpha has **state graph** (well-defined progression through states) +
**checklist** (testable conditions for each state).

### §4.3 Way-of-Working alpha as method recursion

**Critical:** Way-of-Working is itself an Alpha! Method evolves through states:
- Principles Established
- Foundation Established
- In Use
- In Place
- Working Well
- Retired

This is **method-engineering applied to itself** — Essence is reflexive.

### §4.4 Practice library

Beyond Kernel: **Practice library** — reusable practices (Scrum, XP, User Stories,
Use Cases, etc.) expressed in Essence vocabulary. Allows mix-and-match.

### §4.5 Alpha state checklists

Each Alpha state has **explicit checklist of verifiable conditions** that must
be satisfied for state to be recognised. Example Requirements/Acceptable state:

- Requirements are clear, consistent, testable
- Stakeholders agree they reflect needs
- Implementation team understands them
- Risks of acceptance understood

[src: OMG Essence 2.0 spec; Jacobson I., Spence I., Bittner K. 2013 «The
Essence of Software Engineering: Applying the SEMAT Kernel»]

### §4.6 Jacobson-Spence-Bittner book 2013

> Jacobson I., Spence I., Bittner K. 2013 «The Essence of Software Engineering:
> Applying the SEMAT Kernel» Addison-Wesley

Canonical practitioner introduction to Essence. Essence as **shared
vocabulary** rather than yet-another-methodology.

### §4.7 Essence-Diff and progress visualisation

Essence provides **alpha state cards** (physical cards in some implementations)
for team workshops. Team moves cards between states; **Essence-Diff** = visual
comparison of current vs target alpha states.

### §4.8 Critique of Essence

- Adoption: low outside SEMAT-affiliated organisations
- Complexity: 7 alphas + many states overwhelming для new teams
- Software-engineering-specific: alphas tilted к SW (Software System alpha
  central) — generalisation к other domains requires substantial effort
- Standards-fatigue: yet another OMG standard

[src: critique literature; SEMAT website https://www.semat.org]

### §4.9 Левенчук's adoption + generalisation

Левенчук M2025 line 56: «Изложение базируется тем самым ... сколько на
методологических международных стандартах ... появившихся уже в 21 веке
(особенно широко мы используем стандарт OMG Essence 2.0:2024, моделирование
графа создания дано по его мотивам).»

**Implication:** Левенчук = **primary modernised methodology educator using
OMG Essence as substrate.** This is the chain through which Russian methodology
tradition + Western standards integrate.

### §4.10 Essence + Jetix mapping (detailed)

| Essence concept | Jetix substrate |
|---|---|
| **Opportunity alpha** | Strategic Layer Foundation Part 11 + JETIX-VISION-FUNDAMENTAL 35 UC |
| **Stakeholders alpha** | CRM system (people + orgs); Pillar B Project Strategy slot |
| **Requirements alpha** | Hypothesis Architecture 7-layer + Default-Deny table + R12 LOCK |
| **Software System alpha** | Foundation Parts 1-11 + ROY swarm + Wiki v2 |
| **Work alpha** | Project Lifecycle Substrate Part 7 + Stage Gates SG-0 → SG-N |
| **Team alpha** | Role Taxonomy Part 4 + ROY Swarm CLAUDE.md table |
| **Way-of-Working alpha** | METHOD-DEEP-DESCRIPTION + METHOD-LIFE-DEVELOPMENT-V2 + Method V2 §J |

[src: cross-reference Jetix Foundation + Method V2 + CLAUDE.md]

---

## §5 Alpha-machinery generalisation outside SE

### §5.1 Essence Universal Kernel (proposed)

OMG has proposed generalising Essence Kernel beyond software engineering к
**any endeavour**. Universal kernel would replace "Software System" с
"Endeavour Outcome" or similar.

[src: OMG Essence 2.0 extension working group]

### §5.2 Левенчук's generalisation move

Левенчук M2025 generalises:
- Software System alpha → Целевая система (target system; any kind)
- Work → Project в общем смысле
- Team → Команда создателей
- Way-of-Working → Метод (universal)

Essence concepts adapted к scale-free agent-systems framework. This is what
Левенчук means by «безмасштабное методологическое мышление».

### §5.3 Jetix universal-alpha application

Jetix Hypothesis Architecture 7-layer maps:

| Hypothesis layer | Essence-style alpha |
|---|---|
| Layer 1: Frame the question | Opportunity alpha (formative) |
| Layer 2: Stakeholders + value | Stakeholders alpha |
| Layer 3: Operational design | Requirements alpha |
| Layer 4: Prediction | Software System alpha (in non-SW: "Endeavour Outcome") |
| Layer 5: Test execution | Work alpha |
| Layer 6: Observation | Work alpha + post-state |
| Layer 7: Reflection + update | Way-of-Working alpha (recursion: method updates) |

[src: Hypothesis Architecture from Method V2 + Essence 2.0 alphas]

---

## §6 Method engineering academic + industrial communities

### §6.1 ME academic community

- ME conference series (1996-)
- CAiSE (Conference on Advanced Information Systems Engineering) hosts ME tracks
- Information and Software Technology journal
- IEEE Transactions on Software Engineering ME papers
- Henderson-Sellers + Ralyté + Brinkkemper + Rossi as central researchers

### §6.2 ME industrial reality

Method engineering rarely deployed at full SME-discipline level в industry.
More common:
- **Light-touch tailoring**: org adopts "Scrum + our adaptations"
- **Compliance-driven methodology**: ISO 9001 / CMMI mandates specific process
- **Vendor methodology**: SAFe / Disciplined Agile / Spotify-Model imitations

True situational composition rare; engineering-grade method-base rarer.

### §6.3 Why low industrial adoption?

Several factors:
1. **Methodology fatigue** — orgs have adopted 5+ methodologies already
2. **Standards complexity** — OMG specs intimidate non-academics
3. **ROI unclear** — investment in method engineering vs investment в product
4. **Cultural resistance** — methodology = "process people" stereotype

---

## §7 Левенчук's relation to standards-discipline

### §7.1 Direct Левенчук statements

Левенчук M2025 line 56-58:
- OMG Essence 2.0:2024 = primary modern standard used
- ISO/IEC 24744:2014 = also referenced
- Brinkkemper SME = footnote-acknowledged

### §7.2 Левенчук's pedagogical innovation

Левенчук doesn't simply teach OMG Essence; he **integrates** Essence vocabulary
с:
- Russian methodology tradition (СМД lineage adaptation)
- Intellect-stack as broader fundamental-methods framework
- Engineering discipline (системная инженерия adjacent)
- AI-era considerations (LLM agents as createurs)

**Result:** OMG Essence-via-Russian-tradition pedagogy unique on world stage.

### §7.3 Critique of Левенчук's standards-grounding (literature)

Some Russian methodology orthodox critics (П.Г.Щедровицкий direction) argue:
- Standards-grounding sacrifices ММК-distinctive reflexive-position depth
- OMG Essence too SE-specific; generalisation work incomplete
- Standards = vendor-driven; concedes methodology politics к industry

These critiques have merit but Левенчук's standards-grounding wins in **practical
pedagogy + interoperability** dimension.

---

## §8 Convergent methodology engineering pattern

Common pattern across 4 traditions (Brinkkemper SME + ISO/IEC 24744 + SEMAT +
OMG Essence + Левенчук modernisation):

```
1. Bound method scope
   (Essence: 7 alphas; SME: method base; ISO: metamodel concepts)
2. Decompose into fragments
   (SME: process/product/people/tool fragments; Essence: practices)
3. Specify alpha state-graphs
   (Essence: explicit; SME: optional checkpoints)
4. Compose situationally
   (SME: explicit composition algorithm; Essence: practice mix)
5. Monitor + audit (alpha cards)
   (Essence: progress visualisation; SME: quality metrics)
6. Reflect + adapt
   (Way-of-Working alpha recursion; Левенчук: SoTA tracking)
```

**Jetix substrate implements all 6 steps:**
1. Foundation Parts 1-11 bound system architecture
2. Wiki v2 9 entity types + cycle artefacts = method-base fragments
3. Hypothesis Architecture 7-layer = alpha state-graph
4. KM MVP `/project-bootstrap --type=<4>` situational composition
5. cycle hooks + lint + Default-Deny + R12 LOCK = audit
6. Cycle end-reflection + ROY meta-agent + SoTA tracking = reflection-adapt

[src: cross-tradition convergence + CLAUDE.md + KM-materialization-mvp]

---

## §9 Sources cited

**Primary standards references:**
- Brinkkemper S. 1996 «Method engineering: engineering of information systems
  development methods and tools» Information and Software Technology 38(4):275-280
  https://doi.org/10.1016/0950-5849(95)01059-9
- Brinkkemper S., Saeki M., Harmsen F. 1998 «Assembly Techniques for Method
  Engineering» CAiSE 1998 LNCS 1413
- ISO/IEC 24744:2014 «Software Engineering — Metamodel for Development
  Methodologies» https://www.iso.org/standard/62644.html
- OMG 2014 «Kernel and Language for Software Engineering Methods» version 1.0
  https://www.omg.org/spec/Essence/
- OMG 2024 «Essence Kernel» version 2.0 https://www.omg.org/spec/Essence/2.0/
- SEMAT Manifesto 2009 https://www.semat.org/

**Practitioner books:**
- Jacobson I., Spence I., Bittner K. 2013 «The Essence of Software Engineering:
  Applying the SEMAT Kernel» Addison-Wesley
- Henderson-Sellers B., Ralyté J. 2010 «Situational Method Engineering: State-
  of-the-Art Review»
- Henderson-Sellers B., Ralyté J., Ågerfalk P.J., Rossi M. 2014 «Situational
  Method Engineering»

**Cross-pulled Russian methodology:**
- Левенчук А. «Методология 2025» lines 56-58, 271
- Phase 1 (Левенчук deep decode)
- Phase 6 (Russian methodology tradition)

**Cross-pulled Jetix substrate:**
- Hypothesis Architecture 7-layer (Method V2 §10)
- Foundation Architecture v1.0 LOCKED 2026-04-28
- KM-materialization-mvp cycle (2026-04-24)
- CLAUDE.md Active ROY Swarm table

**Total: 12+ distinct anchors. Target 4+ met.**

---

## §10 Key takeaways (EP-5 summary)

1. **Method Engineering = engineering discipline** of constructing/evaluating/
   maintaining methods; distinct from "methodology" philosophical sense.
2. **Brinkkemper SME 1996** = academic founding; situational composition from
   method fragments; rejection of one-size-fits-all.
3. **OMG Essence Kernel 2.0:2024** = current primary modern standard; 7 alphas
   + state graphs + checklists + practice library; Way-of-Working alpha reflexive.
4. **ISO/IEC 24744:2014** = parallel SE methodology metamodel; powertype pattern
   innovation.
5. **SEMAT initiative** = industrial backing (Jacobson/Meyer/Soley); low adoption
   rate but theoretical importance.
6. **Левенчук-modernisation** = integration of OMG Essence + Russian methodology
   tradition + intellect-stack + AI-era; unique world-stage pedagogy.
7. **Jetix implements 6-step common ME pattern** (bound / decompose / state-graph /
   compose situationally / audit / reflect-adapt) — explicit standards-grounded
   methodology operationalisation.

---

*Phase 7 closure. ~510 lines. R1 preserved. LOCK preserved. 12+ sources cited.*
