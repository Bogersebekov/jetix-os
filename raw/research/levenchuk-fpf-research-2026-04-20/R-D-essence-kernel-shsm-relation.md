# Essence Kernel × ШСМ: A Comparative Research Report

*Prepared for Jetix OS Foundational Philosophy Framework (FPF)*
*Focus: OMG Essence (SEMAT) and Anatoly Levenchuk's School of Systems Management adaptations*

---

## Executive Summary

**Essence** is an OMG-standardized meta-framework for describing software engineering methods. Proposed by SEMAT (Software Engineering Method and Theory) and published as [OMG Essence v1.0 in November 2014](https://www.omg.org/spec/Essence/1.0), then revised as [v1.1 (2015)](https://www.omg.org/spec/Essence/1.1), [v1.2 (2018)](https://www.omg.org/spec/Essence/1.2), and an [alpha draft v2.0 (February 2024)](https://www.omg.org/spec/Essence/2.0/Alpha1/About-Essence), it provides two interrelated components: a **Kernel** (seven universal alphas in three areas of concern) and a **Language** (the type system for authoring new kernels and practices). Its central insight is that every software engineering endeavor, regardless of the specific methodology employed, works with the same seven fundamental things — called **alphas** (Abstract-Level Progress Health Attributes) — each of which moves through a sequence of past-participle-named states verified by checklists. Alphas are not documents or processes but role-based functional objects: the things you *track* rather than the things you *produce*.

**Анатолий Левенчук (Anatoly Levenchuk)**, scientific director of ШСМ (Школа системного менеджмента / School of Systems Management), has engaged with Essence since [at least 2010](https://ailev.livejournal.com/1051048.html) and has adopted its architecture as the ontological spine of the ШСМ curriculum. His adaptation is neither a translation nor a critique: it is a deliberate **generalization** — taking Essence's *language* (the type system) while replacing its software-specific *kernel* with a domain-independent kernel applicable to any engineered system, from buildings to organizations to AI agents. Key moves include:

1. **Replacing** the "Requirements / Software System" engineering alpha pair with "System Definition / System Embodiment" (Определение системы / Воплощение системы), aligning with ISO 42010 and systems engineering standards.
2. **Replacing** "Way of Working" (as alpha) with "Technology" (Технология) in the middle-period kernel, then in the most recent editions keeping "Way of Working / Method" (Метод) as a core alpha alongside "System Embodiment / System Description / Works."
3. **Extending** the endeavor area with technology management concerns (CTO/CIO responsibilities), originally absent from Essence.
4. **Embedding** Essence's alpha/checklist mechanism inside a broader **intellect-stack** (интеллект-стек), a layered architecture of trans-disciplines (трансдисциплины) where methodology is one layer.
5. **Foregrounding** the creation graph (граф создания) — three-level mereological structure: super-system / target system / enabling system — as the spatial context within which all alphas are located.
6. **Treating AI agents** as first-class role executors: agents (human, AI, organizational) hold roles and run methods; alpha states become machine-readable progress protocols.

The critical verdict for FPF design: **Essence's Language is the ontological primitive; Levenchuk's kernel is the domain-neutral instantiation of that Language for any engineering endeavor; the original Essence kernel applies only to software.** For Jetix OS, the ШСМ generalization is more appropriate as a foundational layer, but the alpha state-machine mechanism (past-participle states + checklists) must be preserved verbatim — it is the sharpest tool in the framework.

---

## Section 1 — Essence Kernel (Original SEMAT)

### 1.1 History and Authorship

SEMAT (Software Engineering Method and Theory) was [founded in September 2009](https://queue.acm.org/detail.cfm?id=2389616) by **Ivar Jacobson**, **Bertrand Meyer**, and **Richard Soley**, who argued that the field of software engineering suffered from three fundamental pathologies: fads driven by fashion rather than evidence; methods designed for methodologists rather than practitioners; and standards too complex to apply without extensive training. Their manifesto called for a kernel of universally agreed-upon elements that could serve as common ground for all software-engineering endeavors and as a foundation for composing situational methods.

The SEMAT community developed the kernel through submissions to the Object Management Group. The specification received 73% approval at the OMG meeting of [November 12, 2012](https://ailev.livejournal.com/1051048.html) — just two percentage points short of immediate adoption. It was formally adopted as **Essence v1.0 in November 2014**, followed by [v1.1 in December 2015](https://www.omg.org/spec/Essence/1.1), and [v1.2 in July 2018](https://www.omg.org/spec/Essence/1.2). A draft v2.0 was published [in February 2024](https://www.omg.org/spec/Essence/2.0/Alpha1/About-Essence). Jacobson's book [*The Essence of Software Engineering: Applying the SEMAT Kernel*](https://ptgmedia.pearsoncmg.com/images/9780321885951/samplepages/0321885953.pdf) (Addison-Wesley, 2013, co-authored with Pan-Wei Ng, Paul McMahon, Ian Spence, and Michael Goedicke) remains the primary practitioner reference.

The specification distinguishes two parts: the **Language** (a type system for describing methods using constructs such as alpha, activity space, competency, work product, and practice) and the **Kernel** (a specific instantiation of the language for software engineering — the seven alphas and their associated elements). This two-layer design is crucial: the kernel is an *example* of what the language can express, not the language itself.

### 1.2 Core Structure

The Essence Kernel is organized around **three areas of concern** ([OMG Essence spec](https://www.omg.org/spec/Essence/1.2); [SEMAT Quick Reference Guide](https://semat.org/quick-reference-guide.html)):

| Area of Concern | Color Code | Focus | Alphas |
|-----------------|------------|-------|--------|
| **Customer** | Green | Why the system exists; stakeholder value | Stakeholders, Opportunity |
| **Solution** | Yellow | What the system must be and do | Requirements, Software System |
| **Endeavor** | Blue | How the team does the work | Work, Way of Working, Team |

The kernel contains four kinds of essential elements ([SEMAT uniroma2 seminar](https://lists.uniroma2.it/index.html/arc/isssr/2019-03/msg00029/Essence_seminar_to_SW_Eng_Students_Uniroma2.pdf)):
1. **Alphas** — the essential things to work with
2. **Activity Spaces** — the essential things to do
3. **Competencies** — the essential capabilities needed
4. **Patterns** — named bundles of synchronized alpha states

The standard also defines **Work Products** as physical artifacts (documents, databases, meetings) that *manifest* alpha states in the real world. One alpha is typically manifested by 10–15 different work products depending on the practice; one work product can manifest multiple alphas. This separation — functional alpha vs. physical work product — is the philosophical heart of Essence.

### 1.3 Full Alpha Treatment

The seven alphas, their definitions, state sequences, and representative checklist items are as follows ([SEMAT Quick Reference Guide](https://semat.org/quick-reference-guide.html), [ACM CACM](https://cacm.acm.org/practice/the-essence-of-software-engineering/)):

#### Stakeholders (Customer area)
*"The people, groups, or organizations who affect or are affected by a software system."*

**States (6):** Recognized → Represented → Involved → In Agreement → Satisfied for Deployment → Satisfied in Use

Key checklist items: *Recognized* requires stakeholder groups identified and responsibilities defined. *In Agreement* requires priorities clear and perspectives balanced. *Satisfied in Use* requires the system meets expectations.

#### Opportunity (Customer area)
*"The set of circumstances that makes it appropriate to develop or change a software system."*

**States (6):** Identified → Solution Needed → Value Established → Viable → Addressed → Benefit Accrued

Key checklist items: *Value Established* requires opportunity value quantified, success criteria clear, outcomes quantified. *Benefit Accrued* requires ROI profile at least as good as anticipated.

#### Requirements (Solution area)
*"What the software system must do to address the opportunity and satisfy the stakeholders."*

**States (6):** Conceived → Bounded → Coherent → Acceptable → Addressed → Fulfilled

Key checklist items: *Coherent* requires requirements shared, rationale clear, conflicts addressed, team knows what to deliver. *Fulfilled* requires no outstanding items preventing full satisfaction.

#### Software System (Solution area)
*"A system made up of software, hardware, and data that provides its primary value by the execution of the software."*

**States (6):** Architecture Selected → Demonstrable → Usable → Ready → Operational → Retired

Key checklist items: *Architecture Selected* requires HW platforms identified, technologies selected, buy/build/reuse decisions made. *Operational* requires system live, SLAs supported. *Retired* requires no authorized users.

#### Work (Endeavor area)
*"Activity involving mental or physical effort done in order to achieve a result."*

**States (6):** Initiated → Prepared → Started → Under Control → Concluded → Closed

Key checklist items: *Under Control* requires risks under control, estimates revised, commitments consistently met. *Closed* requires lessons learned recorded, budget reconciled, team released.

#### Way of Working (Endeavor area)
*"The tailored set of practices and tools used by a team to guide and support their work."*

**States (6):** Principles Established → Foundation Established → In Use → In Place → Working Well → Retired

Key checklist items: *In Use* requires key practices and tools in use, inspected and adapted. *Working Well* requires the way-of-working is tuned to the team's needs.

#### Team (Endeavor area)
*"A group of people actively engaged in the development, maintenance, delivery or support of a specific software system."*

**States (5):** Seeded → Formed → Collaborating → Performing → Adjourned

Key checklist items: *Seeded* requires mission defined, required competencies identified, governance rules defined. *Performing* requires consistently meeting commitments, continuously adapting, waste continuously eliminated. *Adjourned* requires responsibilities fulfilled, team released.

### 1.4 Activity Spaces

Essence defines **15 activity spaces** grouped by area of concern ([Ivar Jacobson International, Essence Activity Spaces](https://www.ivarjacobson.com/publications/articles/essence-activity-spaces)):

**Customer (4):** Explore Possibilities → Understand Stakeholder Needs → Ensure Stakeholder Satisfaction → Use the System

**Solution (6):** Understand the Requirements → Shape the System → Implement the System → Test the System → Deploy the System → Operate the System

**Endeavor (5):** Prepare to do the Work → Coordinate Activity → Support the Team → Track Progress → Stop the Work

Activity spaces are *generic placeholders* for specific activities; they are method-independent and therefore standardizable. Each activity space has Entry Criteria (expressed as alpha states that must be achieved before entry) and Completion Criteria (target states). For example, *Prepare to do the Work* completes when `Team::Seeded`, `Way of Working::Foundation Established`, and `Work::Prepared`.

### 1.5 Practices, Competencies, and Adoption

A **practice** in Essence is a composable unit containing: activities (things to do), work products (things to produce or use), and competencies (things to be capable of). Practices can be composed into methods by stacking them — provided they do not introduce contradictory alpha-state requirements. The standard defines **six core competencies** ([Essence: Reference Architecture for SE](https://www.scitepress.org/papers/2018/67936/67936.pdf)): Stakeholder Representation, Analysis, Development, Testing, Leadership, Management — each with five levels (Assists, Applies, Masters, Adapts, Innovates).

Essence has been adopted in university curricula, agile coaching, and enterprise transformation programs. Tooling includes the Semat Accelerator, various card-based workshop kits, and integrations with project management platforms. **Limitations** acknowledged by the community include: the kernel is specific to software engineering (not general systems engineering); activity spaces are presented only in overview form in most practitioner guides; the competency model is sparse compared to professional frameworks such as SFIA; and the method composition mechanism, while theoretically sound, requires considerable expertise to use correctly.

---

## Section 2 — Levenchuk's ШСМ Adaptation Overview

### 2.1 Borrowed Unchanged

Levenchuk treats the **Essence Language** — the type system — as essentially correct and preserves it verbatim ([ailev.livejournal.com, 2013](https://ailev.livejournal.com/1082662.html); [Методология 2025](https://flibusta.su/book/358645-metodologia-2025/read/)):

- **The alpha construct** (functional object that tracks method-subject state in a project)
- **Past-participle state naming convention** (states named as completed transformations: "замыслено", "воплощено", "эксплуатируется")
- **State-checklist structure** (each state verified by a list of yes/no control questions, "AND" logic — all must pass)
- **Alpha-state graph** (states form a graph, not necessarily a linear chain; cycles, returns, and loops are all valid)
- **Work products as manifestation** (физические артефакты / physical artifacts that evidence alpha states in the real world)
- **The "things to care about" framing** (alphas as collective attention-management objects)
- **Alpha containment and association** (sub-alpha relationships driving parent alpha progression)

His 2013 post on [alphas and work products](https://ailev.livejournal.com/1082662.html) is the most thorough Russian-language theoretical treatment of Essence's alpha construct, and it is fundamentally expository rather than critical.

### 2.2 Modified

**Alpha set:** In the 2015 paper ["Towards a Systems Engineering Essence"](https://arxiv.org/abs/1502.00121), Levenchuk kept the Customer and Endeavor areas intact but modified the Solution area, replacing "Requirements / Software System" with **"System Definition / System Embodiment"** (Определение системы / Воплощение системы). His rationale: for systems engineering (as opposed to software-only project management), the source code is a *description* of the system, not the system itself; architecture properly belongs in System Definition; and the replacement pair aligns perfectly with ISO 42010 ([ailev.livejournal.com, 2016](https://ailev.livejournal.com/1318973.html)).

**Endeavor alpha — Technology substitution:** In the intermediate period (approximately 2014–2020), Levenchuk replaced "Way of Working" with **"Technology"** (Технология) in the Endeavor area ([wikireading excerpt from his textbook](https://fil.wikireading.ru/h6xqzgWEOR)). His argument: for systems engineering, the CTO/CIO's technology management concerns (selecting, deploying, and governing engineering technologies) are a first-class project concern not covered by Essence's Way-of-Working alpha, which tracks only team practice adoption. The seven ШСМ project-schema alphas in this period were: Возможности, Стейкхолдеры, Определение системы, Воплощение системы, Работы, Технология, Команда.

**Most recent editions (2023–2024):** In "Системное мышление 2024" and "Методология 2025," the alpha set stabilizes around four universal alphas plus practice-specific extensions ([ailev.livejournal.com, April 2024](https://ailev.livejournal.com/1718836.html)): **воплощение системы, описание системы, функция/метод работ (way of working), работы системы**. External project roles (стейкхолдеры, возможности) and team (команда) appear as sub-alphas or as alphas of specific method-level kernels. The systemsworld.club list (2020) documents a ШСМ kernel of: **внешние проектные роли, возможности, воплощение системы, описание системы, работы, команда, метод** — still seven alphas but with "method" (метод) replacing "technology" and "external project roles" (внешние проектные роли) replacing plain "stakeholders."

**Alpha definitions:** Levenchuk explicitly reinterprets "alpha" not as "ALPHA" backronym but as "the subject of a method" (предмет метода) — any important object whose state changes must be tracked throughout a project ([Методология 2025](https://flibusta.su/book/358645-metodologia-2025/read/)). This broadens scope from software project tracking to universal method modeling.

### 2.3 Added

**Creation graph (граф создания):** Levenchuk introduces the three-level mereological structure — super-system (надсистема / using system) / target system (целевая система) / enabling system (обеспечивающая система / creation system) — as the spatial container for all project thinking. Each alpha in the kernel is assigned to one of these levels. The super-system hosts Opportunity and Stakeholders (customer area). The target system is modeled via System Definition and System Embodiment. The enabling system (the team, tools, technology, way-of-working) hosts the Endeavor alphas. This is not in original Essence. Levenchuk derives it from his systems engineering ontology, drawing on ISO 15288 and his own work (["Мой доклад на АПСПИ-2015"](https://ailev.livejournal.com/1188876.html)). In "Методология 2025," he notes that **the creation graph modeling is given following the motifs of OMG Essence 2.0:2024**, indicating that Essence v2.0 itself has partially adopted this multi-level view.

**Strategizing (стратегирование):** Defined as the "method of choosing a method" (метод выбора метода) — the practice of selecting or designing the way-of-working when the appropriate approach is unclear ([Методология 2025](https://flibusta.su/book/358645-metodologia-2025/read/)). This is a meta-practice absent from Essence, which assumes the team's way-of-working is discovered iteratively but does not describe *how* to choose practices.

**Intellect-stack (интеллект-стек):** A layered hierarchy of trans-disciplines in which Methodology (the theory of methods) occupies a specific level, preceded by foundational layers (physics, mathematics, ontology, semantics) and succeeded by applied layers (systems engineering, management). The intellect-stack frames Essence not as a standalone standard but as one formalization within a larger cognitive architecture ([Интеллект-стек 2023](https://ridero.ru/books/intellekt-stek_2023/)).

**Trans-disciplines (трансдисциплины):** Levenchuk identifies a set of domain-independent thinking disciplines that constitute the "firmware" of a competent intellect. The 2023 intellect-stack includes: понятизация (concept formation), собранность (collectedness/focus), семантика (semantics), математика (mathematics), физика (physics), теория понятий (theory of concepts), онтология (ontology), алгоритмика (algorithmics), логика (logic), рациональность (rationality), познание/исследования (cognition/research), эстетика (aesthetics), этика (ethics), риторика (rhetoric), методология (methodology), системная инженерия (systems engineering) — approximately 16–17 items depending on edition ([Интеллект-стек 2023 on Ridero](https://ridero.ru/books/intellekt-stek_2023/)). ⚠ Unverified: The exact count varies between editions; the 2023 edition lists approximately 16; "17" is a commonly cited approximation that should be verified against the specific edition in use.

**Writing-as-thinking (мышление письмом):** Explicit modeling through structured text and tables is elevated to a practice primitive — not merely a documentation technique but the primary vehicle for externalized cognition in ШСМ. This has no equivalent in Essence.

**AI agents as role executors:** See Section 7.

### 2.4 Rejected or Sidelined

**Activity spaces as a compositional layer:** Levenchuk does not explicitly reject activity spaces but effectively sidelines them. The ШСМ curriculum treats alpha-state tracking as primary and does not organize practices around activity-space templates. ⚠ Unverified: Whether Levenchuk has explicitly commented on activity spaces versus silently omitting them is unclear from available primary sources. His 2012–2013 posts translate "activity space" as "деятельность" or "пространство дел" and discuss them, but subsequent ШСМ course structures do not foreground them.

**Practice-as-composition formalism:** Essence's formal practice composition (stacking practices that share kernel alphas, with OCL constraints to verify consistency) does not appear in ШСМ materials. Levenchuk uses "practice" and "method" interchangeably as synonyms; the formal compositional algebra of Essence is replaced by informal method modeling in tables and checklists.

**The software-specific kernel:** Explicitly rejected. The ШСМ 2024 position is to use Essence's *language* (types) only, not the standard software-dev kernel, and to develop a domain-specific kernel for each new application area ([ailev.livejournal.com, April 2024](https://ailev.livejournal.com/1718836.html)).

### 2.5 Levenchuk's Rationale and Self-Explanation

Levenchuk's most explicit rationale is given in [his 2016 post on original Essence alphas](https://ailev.livejournal.com/1318973.html):

> «Напомню, что главное отличие — там инженерные альфы "Requirements" и "System" против доработанного для системной инженерии варианта с "System definition" и "System realization" на их местах.»
> ("Recall that the main difference — there are the engineering alphas 'Requirements' and 'System' against the reworked for systems engineering variant with 'System definition' and 'System realization' in their places.")

His alignment with ISO 42010 is the technical argument: both standards use System Definition / System Realization, creating a coherent view of requirements, architecture, and non-architectural project parts. He contrasts this with the original Essence alphas, which serve project managers (who need only to know a system-result exists and requirements must be met) but not systems engineers (who must develop requirements, reason about architecture, and choose description methods).

In his 2024 post on [alphas and artifacts](https://ailev.livejournal.com/1718836.html), he explains the Language/Kernel separation clearly:

> «В нашем курсе мы рекомендуем использовать OMG Essence, но берём из него только language, а не описанный в нём пример kernel — ровно как этого и требует стандарт, ибо для каждой новой предметной области разработки надо бы разрабатывать свой kernel.»
> ("In our course we recommend using OMG Essence, but we take from it only the language, not the kernel example described in it — exactly as the standard requires, because for each new development domain one should develop one's own kernel.")

This is a principled adoption position rather than a critique: Essence is praised for its language architecture and checklist mechanism; the software-specific kernel is simply not applicable to systems engineering or general organizational work.

---

## Section 3 — Alpha Mapping Table

### 3.1 Seven-Alpha Side-by-Side Comparison

The table maps the original Essence kernel to Levenchuk's ШСМ adaptation across three periods: the 2015 Systems Engineering Essence paper, the intermediate textbook period (2014–2020), and the current ШСМ framework (2020–2024).

| # | Original Essence Alpha | Russian Term (Levenchuk) | ШСМ Counterpart (SE Essence 2015) | ШСМ Counterpart (Textbook 2015–2020) | ШСМ Counterpart (Current 2020–2024) | Key Difference |
|---|------------------------|--------------------------|----------------------------------|--------------------------------------|--------------------------------------|----------------|
| 1 | **Stakeholders** | Стейкхолдеры | Стейкхолдеры (unchanged) | Стейкхолдеры (unchanged) | **Внешние проектные роли** (external project roles) | Later: emphasizes role-based framing over stakeholder-list framing; sub-alpha: enterprise owners |
| 2 | **Opportunity** | Возможности | Возможности (unchanged) | Возможности (unchanged) | Возможности (unchanged) | No structural change; scope widened to include super-system analysis |
| 3 | **Requirements** | Требования | **Определение системы** (System Definition) | Определение системы | Описание системы (System Description) | Major change: source code becomes part of system *description*, not embodiment; architecture explicitly included |
| 4 | **Software System** | Программная система | **Воплощение системы** (System Embodiment / Realization) | Воплощение системы | Воплощение системы | Name change + scope generalization: applies to any engineered system (buildings, organizations, etc.) |
| 5 | **Work** | Работа | Работы (unchanged, plural) | Работы | Работы системы / Работы | Levenchuk distinguishes "works of the target system" (during operation) from "works of the creation system" (during development) — two separate alphas in principle |
| 6 | **Way of Working** | Способ работы / Метод | **Preserved in SE Essence** | **Технология** (replaces Way of Working) | **Метод / Way of Working** (restored) | Middle period: technology management (CTO/CIO concerns) elevated to alpha status, replacing way-of-working; recent editions: method restored, technology demoted to sub-alpha |
| 7 | **Team** | Команда | Команда (unchanged) | Команда (unchanged) | Команда (unchanged) | Unchanged structurally; semantics broadened to include AI agents as team members |

**Commentary on Row 3 (Requirements → System Definition / Description):**
This is Levenchuk's most significant structural change. In original Essence, "Requirements" covers what the system must do. Levenchuk argues that for systems engineering, this alpha must include architecture (how the system will be structured) and all models/descriptions — not just a requirements document. He aligns this with ISO 42010, where architectural description is the central artifact. In his 2015 paper, he writes that "source code is a work product of System Definition, not System Embodiment" — inverting the standard Essence assumption. This reframing makes "System Definition" (Определение системы) a broader concept: the complete specification/design of the target system, including requirements, architecture, and models.

**Commentary on Row 4 (Software System → System Embodiment):**
The word "Embodiment" (воплощение) rather than "Realization" is deliberate: it foregrounds the *physical* nature of the system object. Levenchuk's definition: "воплощение системы привязывает все рассуждения по схеме к физической реальности (воплощение системы — 4D индивид)" — "system embodiment anchors all reasoning in the schema to physical reality (system embodiment is a 4D individual)." ([wikireading excerpt](https://fil.wikireading.ru/h6xqzgWEOR)) This reflects his commitment to ontological grounding: systems must exist in physical spacetime, not just as information constructs.

**States for System Embodiment (ШСМ):**
Explicitly documented in Levenchuk's course materials ([inexsu blog, 2020](https://inexsu.wordpress.com/2020/05/23/%D0%BB%D0%B5%D0%B2%D0%B5%D0%BD%D1%87%D1%83%D0%BA-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D0%BE%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5/)):

| State (Russian) | State (English) | Checklist Sample |
|-----------------|-----------------|-----------------|
| в виде сырья | as raw material | Material resources allocated to project |
| в виде частей | as components/parts | Individual components available |
| демонстрируемо | demonstrable | Architecture demonstrated, key characteristics verified |
| готово | ready | Tested, defect levels acceptable, stakeholders accept |
| эксплуатируется | operational | System in live use, SLAs maintained |
| выведено из эксплуатации | retired | No authorized users, support ceased |

⚠ Note: These states parallel the Essence "Software System" states closely (Architecture Selected → Demonstrable → Usable → Ready → Operational → Retired), with "as raw material / as components" replacing the Essence "Architecture Selected" — reflecting Levenchuk's systems engineering perspective where physical assembly begins before architectural decisions are complete in some domains.

### 3.2 Additional Alphas Levenchuk Added

Beyond modifying the base seven, Levenchuk introduces several additional alphas or sub-alpha classes in various ШСМ materials:

- **Технология (Technology):** In the intermediate period, a full kernel alpha tracking the lifecycle of the engineering platform/toolchain used by the creation system. States include: выбирается (being selected) → используется (in use). ⚠ Unverified: full state list not confirmed in available primary sources.
- **Внешние проектные роли (External project roles):** Replaces or specializes "Stakeholders" in recent editions, with sub-alphas for specific roles: финансист заказчика (customer financier), архитектор (architect), etc. Each role-alpha tracks the state of that role being filled by a specific agent.
- **Enterprise-level alphas:** In [his 2017 enterprise schema post](https://ailev.livejournal.com/1331004.html), Levenchuk sketches governance-level alphas for investor discussions and Goldratt's "global maximum" operational management — additions appropriate for enterprise architects but absent from project-level Essence.

### 3.3 Essence Alphas Levenchuk Dropped

No Essence alpha is entirely dropped; all seven have ШСМ counterparts. However:
- "Way of Working" was *temporarily* demoted to sub-alpha status (replaced by "Technology") in the 2015–2020 textbook period.
- "Stakeholders" is reframed as "External Project Roles" in the most recent editions, which some practitioners may experience as a dropped alpha.

---

## Section 4 — Activity Spaces vs. Creation Graph

### 4.1 Essence Activity Spaces: Full Treatment

Essence defines 15 activity spaces ([Ivar Jacobson International](https://www.ivarjacobson.com/publications/articles/essence-activity-spaces)) that serve as *generic placeholders* for specific activities. They are organized by area of concern and connected to the alphas through Entry and Completion Criteria:

**Customer Area (4 spaces):**
- *Explore Possibilities* — entry: none; completion: `Stakeholders::Recognized`, `Opportunity::Value Established`
- *Understand Stakeholder Needs* — completion: `Stakeholders::In Agreement`, `Opportunity::Viable`
- *Ensure Stakeholder Satisfaction* — completion: `Stakeholders::Satisfied for Deployment`, `Opportunity::Addressed`
- *Use the System* — completion: `Stakeholders::Satisfied in Use`, `Opportunity::Benefit Accrued`

**Solution Area (6 spaces):**
- *Understand the Requirements* — completion: `Requirements::Coherent`
- *Shape the System* — completion: `Requirements::Acceptable`, `Software System::Architecture Selected`
- *Implement the System* — completion: `Software System::Ready`
- *Test the System* — completion: `Software System::Usable`
- *Deploy the System* — completion: `Software System::Operational`
- *Operate the System* — completion: `Software System::Retired`

**Endeavor Area (5 spaces):**
- *Prepare to do the Work* — completion: `Team::Seeded`, `Way of Working::Foundation Established`, `Work::Prepared`
- *Coordinate Activity* — completion: `Team::Formed`, `Work::Under Control`
- *Support the Team* — completion: `Team::Collaborating`, `Way of Working::In Place`
- *Track Progress* — completion: `Team::Performing`, `Way of Working::Working Well`, `Work::Concluded`
- *Stop the Work* — completion: `Team::Adjourned`, `Way of Working::Retired`, `Work::Closed`

Activity spaces are intentionally practice-independent: any practice's specific activities can be *placed* within activity spaces to indicate what kind of thing those activities accomplish, without changing the kernel's structure.

### 4.2 ШСМ Creation Graph: Three-Level Mereology

Levenchuk's creation graph is a three-level systems hierarchy that contextualizes all project alphas spatially and causally ([wikireading excerpt](https://fil.wikireading.ru/h6xqzgWEOR); ["Мой доклад на АПСПИ-2015"](https://ailev.livejournal.com/1188876.html)):

```
Super-system (надсистема / Using System)
    ↕ [contains / uses]
Target System (целевая система / System of Interest)
    ↕ [created by]
Enabling System (обеспечивающая система / Creation System)
```

Each level corresponds to an area of concern:
- **Super-system** ← Customer area: Stakeholders and Opportunity are properties of the super-system relationship; the *using* system needs the target system and creates the opportunity.
- **Target System** ← Solution area: System Definition and System Embodiment are the two aspects of the target system (description + physical instantiation).
- **Enabling System** ← Endeavor area: Work, Technology, Team, and Method/Way-of-Working are properties of the enabling/creation system (the project team and its tools).

This spatial assignment is more explicit than Essence's areas of concern, which are categories without a systemic hierarchy. The creation graph enables recursive application: any node in the creation graph can itself be treated as a project with its own three-level structure.

### 4.3 Equivalence, Replacement, or Complement?

The creation graph is a **complement and partial replacement** for activity spaces:

| Dimension | Essence Activity Spaces | ШСМ Creation Graph |
|-----------|------------------------|-------------------|
| **Primary function** | Sequence work into generic phases | Locate alphas in a systemic hierarchy |
| **Relation to alphas** | Alphas progress *through* activity spaces | Alphas are *assigned to* creation graph levels |
| **Sequencing** | Explicit entry/completion criteria create partial order | Systemic dependencies (super-system before target system analysis) provide implicit order |
| **Scope** | Single project lifecycle | Recursive: any level can be a project |
| **Practice-independence** | Yes — activity spaces are method-independent | Yes — creation graph is method-independent |
| **Ontological depth** | Shallow (procedural placeholder) | Deep (mereological, physically grounded) |

The creation graph does not replace the *alpha-state-progression* mechanism that activity spaces use (entry/completion criteria); it replaces the *organizational metaphor* from a process-flow view to a systems-hierarchy view. For FPF purposes: the creation graph is the superior organizational framework; activity spaces can be mapped onto it for projects that need explicit phase gating.

---

## Section 5 — Practices Composition

### 5.1 Essence Practice Composition

In Essence, a **practice** is a composable unit defined by ([SEMAT Quick Reference Guide](https://semat.org/quick-reference-guide.html); [Ivar Jacobson International, Essence Explained](https://www.ivarjacobson.com/essence-explained-agile-tools)):
- **Alphas** introduced or referenced (sub-alphas that drive kernel alpha progression)
- **Activities** (specific things to do, placed within activity spaces)
- **Work Products** (artifacts produced or consumed)
- **Competencies** required (type + level)

Practices compose by sharing kernel alphas: a User Story practice and a Use-Case Slice practice can both contribute to the progression of the Requirements alpha, and their composition is consistent if their alpha-state requirements do not contradict each other. A **method** is a composed set of practices applied to a specific context. The OMG specification originally included OCL (Object Constraint Language) for formal consistency checking of practice composition.

Essence supports approximately 250 practices for software engineering, composable into thousands of situational methods. This library-based approach to method assembly was a key innovation over prior methodology engineering standards (SPEM 2.0, ISO 24744).

### 5.2 ШСМ Method Terminology

Levenchuk uses **метод** (method) as the primary term, treating "practice," "process," "workflow," "engineering process," "development process," "methodology," "strategy," and "culture" as synonyms or specializations ([Методология 2025](https://flibusta.su/book/358645-metodologia-2025/read/)). The hierarchy:
- **Метод разработки** (development method) — top-level whole
- **Практика** (practice) — finer subdivision
- **Стиль** (style) — stylistic variant of a practice

The ШСМ formalization of a method focuses on the **signature** (сигнатура): the typed set of method subjects (предметы метода = alphas) and roles (роли) that define what a method operates on and who executes it. Stating the signature is the first step in method modeling. This is more precise than Essence's practice definition, which does not require formal typing of inputs.

**Key difference:** Essence treats practice composition as library assembly (pre-defined practices composed into methods). ШСМ treats method composition as signature decomposition (any method can be decomposed into sub-methods with their own signatures, recursively). The ШСМ approach is more general but requires more modeling work per application. ⚠ Conjecture based on Levenchuk's "Methodology" texts: a formal practice library equivalent to Essence's ~250 practices does not appear to exist in the ШСМ ecosystem; composition relies on practitioner modeling skill.

---

## Section 6 — AI Agents and Essence

### 6.1 Essence × AI Adaptations

The original Essence specification (v1.2) does not address AI agents. Essence v2.0 (alpha draft, 2024) begins to formalize the relationship between Essence and software engineering for AI systems, but details are not yet publicly available in normative form. In the practitioner community, there are experiments using Essence alpha states as project-tracking protocols in AI-assisted development tools, treating checklist items as machine-readable objectives.

### 6.2 Levenchuk's AI Angle

Levenchuk has engaged deeply with AI agents as a design consideration in ШСМ since approximately 2020, with acceleration after 2022. His framework is internally consistent and sophisticated:

**Agents as role executors:** The fundamental move is that *any* intelligent agent — human, AI, robotic, collective — can play a role in a project's creation graph. A role is a functional object; an agent (оргзвено / organizational unit) is the construct that enacts the role. This means Essence's "Team" alpha tracks not just human teams but human+AI hybrid formations ([Методология 2025](https://flibusta.su/book/358645-metodologia-2025/read/)):

> «Создатели – это **агенты**, всё что из методов умеет делать агент (совокупность мастерства агента) – это **личность** агента.»
> ("Creators are **agents**, everything that an agent can do from methods (the totality of the agent's mastery) is the agent's **personality**.")

**Exocortex (экзокортекс):** Levenchuk uses this term for the computational extension of an agent's cognition (tools, AI assistants, structured note systems). ШСМ's writing-as-thinking practice is explicitly designed to work with exocortex tools — modeling alpha states in structured tables that an AI assistant can read and update ([Системное мышление 2024](https://books.yandex.ru/books/oTQZfRrv/read-online)).

**Past-participle states as machine-readable protocol:** The naming convention for alpha states (completed transformations named by past-participle verbs) is not merely convenient for humans — it is naturally parseable. Levenchuk notes that when onboarding an AI agent to a project, describing the current state of each alpha (what has been completed) is the most compact possible briefing. The alpha checklist thus becomes an **agent onboarding protocol** ([ailev.livejournal.com, April 2024](https://ailev.livejournal.com/1718836.html)).

**AI agent limitations (Moravec's paradox angle):** Levenchuk explicitly notes that current AI agents excel at tasks humans find cognitively demanding (strategy advice, text generation) but struggle with tasks animals find trivial (adapting method chains to unexpected situations, physical manipulation). The ШСМ framework accommodates this by assigning AI to strategy and planning roles (where they are strong) while keeping human or robotic agents for physical implementation roles ([Методология в интеллект-стеке, 2024](https://ailev.livejournal.com/1725757.html)).

**Scale-free application:** Levenchuk's systems thinking is explicitly "безмасштабное" (scale-free) — applicable from molecular systems to planetary-scale human systems. An AI agent managing a subroutine and a human managing a civilization use the same alpha-state framework at appropriate granularity. This is an extension beyond anything in the original Essence specification.

**Creation graph for AI pipelines:** The three-level creation graph maps cleanly onto multi-agent AI systems: a super-system (the business/user need), a target system (the AI-produced output), and an enabling system (the agent pipeline / scaffolding / infrastructure). ШСМ alpha tracking can therefore serve as the control layer for agentic AI orchestration.

---

## Section 7 — Practitioner Guidance

### 7.1 Recommended Study Sequence

For practitioners approaching Essence and ШСМ for the first time, particularly in the context of FPF design:

1. **Start with Essence Language, not the kernel.** Read [SEMAT Quick Reference Guide](https://semat.org/quick-reference-guide.html) to understand alpha, alpha state, checklist, work product, activity space, and competency as constructs. This takes approximately two hours and provides the vocabulary for everything else.

2. **Then study Levenchuk's 2013 post on alphas and work products** ([ailev.livejournal.com/1082662.html](https://ailev.livejournal.com/1082662.html)) — the clearest Russian-language explanation of why alphas differ from work products and why the distinction matters. Essential for ontological precision.

3. **Then the Essence kernel** (the seven software-specific alphas with full state checklists from the [SEMAT Quick Reference Guide](https://semat.org/quick-reference-guide.html)). Study the checklist items carefully — they encode practitioner wisdom about what must be true before a state is genuinely achieved.

4. **Then Levenchuk's 2015 SE Essence paper** ([arxiv.org/abs/1502.00121](https://arxiv.org/abs/1502.00121)) to understand the SE kernel modifications and why they were made.

5. **Then the "Методология 2025" / "Системное мышление 2024"** materials to see the full ШСМ integration of alpha thinking with the creation graph, intellect-stack, AI agents, and strategizing.

### 7.2 Common Confusion Points

| Confusion | Resolution |
|-----------|------------|
| Alpha = document | No. Alpha = functional object whose state changes. Work products are the physical documents that *evidence* alpha states. |
| States must be linear | No. States form a graph; regression and cycles are valid and important (e.g., system goes back to "under development" from "operational" during major upgrade). |
| Essence kernel = Essence | No. Essence = Language + Kernel. The kernel is a software-specific *example*. The language is the reusable part. |
| ШСМ uses Essence unchanged | No. ШСМ uses Essence's language while replacing the software-specific kernel with a systems-engineering and then domain-universal kernel. |
| "Requirements" and "System Definition" are the same | No. System Definition includes architecture, all models, and descriptions (code is description in SE perspective). Requirements in Essence is narrower. |
| Activity spaces define a lifecycle | No. Activity spaces are generic phase-placeholders; they do not define a specific process flow. The lifecycle is defined by practice choices. |
| Levenchuk rejects Essence | No. He is among Russia's most thorough promoters of Essence. His modifications are principled generalizations following Essence's own recommendation to develop domain-specific kernels. |

### 7.3 Authority for Specific Design Questions

| Design Question | Authoritative Source |
|-----------------|---------------------|
| Alpha state names and checklists for software projects | OMG Essence specification v1.2, SEMAT Quick Reference |
| Alpha state names for systems engineering | Levenchuk, SE Essence 2015 paper; ШСМ textbooks 2015–2020 |
| Designing new alphas for a novel domain | Levenchuk's methodology (signature decomposition, state graph design, checklist construction) — he has the most developed practical method |
| Activity space design | OMG Essence specification; Ivar Jacobson International materials |
| Creation graph / three-level mereology | Levenchuk exclusively — not in original Essence |
| AI agent role assignment in projects | Levenchuk's ШСМ materials (2022–2024) |
| Practice library assembly | Ivar Jacobson International; the standard ~250 Essence practices |
| Trans-discipline structure (intellect-stack) | Levenchuk's Интеллект-стек 2023 |

---

## Section 8 — Resources

### Essence (Original SEMAT)
- [OMG Essence Specification v1.2 (July 2018)](https://www.omg.org/spec/Essence/1.2) — normative
- [OMG Essence 2.0 Alpha draft (February 2024)](https://www.omg.org/spec/Essence/2.0/Alpha1/About-Essence)
- [SEMAT Quick Reference Guide](https://semat.org/quick-reference-guide.html) — best practitioner introduction
- [The Essence of Software Engineering: The SEMAT Kernel (CACM, 2012)](https://cacm.acm.org/practice/the-essence-of-software-engineering/) — Jacobson et al., readable overview
- [The Essence of Software Engineering: The SEMAT Kernel (ACM Queue, 2012)](https://queue.acm.org/detail.cfm?id=2389616) — founding article
- [Ivar Jacobson International: Essence Explained](https://www.ivarjacobson.com/essence-explained-agile-tools)
- [Ivar Jacobson International: Essence Activity Spaces](https://www.ivarjacobson.com/publications/articles/essence-activity-spaces)
- Jacobson, Meyer, Ng et al., *The Essence of Software Engineering: Applying the SEMAT Kernel* (Addison-Wesley, 2013; ISBN 0321885953)

### Levenchuk / ШСМ on Essence
- [ailev.livejournal.com/1051048.html](https://ailev.livejournal.com/1051048.html) — first major Russian exposition of Essence (2012)
- [ailev.livejournal.com/1082662.html](https://ailev.livejournal.com/1082662.html) — alphas vs. work products, theoretical depth (2013)
- [ailev.livejournal.com/1067999.html](https://ailev.livejournal.com/1067999.html) — ISO 15288 and OMG Essence mapping (2013)
- [arxiv.org/abs/1502.00121](https://arxiv.org/abs/1502.00121) — "Towards a Systems Engineering Essence" (2015) — English-language SE kernel paper
- [ailev.livejournal.com/1188876.html](https://ailev.livejournal.com/1188876.html) — АПСПИ-2015 conference paper: Essence for technology management
- [ailev.livejournal.com/1318973.html](https://ailev.livejournal.com/1318973.html) — on original Essence alphas vs. SE modifications (2016)
- [ailev.livejournal.com/1331004.html](https://ailev.livejournal.com/1331004.html) — enterprise system schema (2017)
- [ailev.livejournal.com/1718836.html](https://ailev.livejournal.com/1718836.html) — alphas and artifacts, current ШСМ alpha framework (April 2024)
- [ailev.livejournal.com/1725757.html](https://ailev.livejournal.com/1725757.html) — Methodology in the intellect-stack (2024)
- [techinvestlab.ru/files/systems_engineering_thinking/systems_engineering_thinking_2015.pdf](https://techinvestlab.ru/files/systems_engineering_thinking/systems_engineering_thinking_2015.pdf) — "Системноинженерное мышление" 2015 textbook
- [fil.wikireading.ru/h6xqzgWEOR](https://fil.wikireading.ru/h6xqzgWEOR) — chapter excerpt: project system schema with 7 ШСМ alphas
- [flibusta.su/book/358645-metodologia-2025/read/](https://flibusta.su/book/358645-metodologia-2025/read/) — "Методология 2025" — current ШСМ methodology textbook
- Левенчук, Анатолий. *Системное мышление 2024* (Ridero, 2024; 2 vols.) — primary ШСМ textbook
- Левенчук, Анатолий. *Методология 2025* (Ridero, 2024)
- Левенчук, Анатолий. *Интеллект-стек 2023* (Ridero, 2023; ISBN 978-5-0060-4990-1)

---

## Bibliography

### OMG / SEMAT Standards and Papers
1. OMG Essence Specification v1.0 (November 2014). https://www.omg.org/spec/Essence/1.0
2. OMG Essence Specification v1.1 (December 2015). https://www.omg.org/spec/Essence/1.1
3. OMG Essence Specification v1.2 (July 2018). https://www.omg.org/spec/Essence/1.2
4. OMG Essence Specification v2.0 Alpha draft (February 2024). https://www.omg.org/spec/Essence/2.0/Alpha1/About-Essence
5. Jacobson, I., Ng, P-W., McMahon, P., Spence, I., Goedicke, M. (2013). *The Essence of Software Engineering: Applying the SEMAT Kernel.* Addison-Wesley Professional. ISBN 0321885953.
6. Jacobson, I. (2012). The Essence of Software Engineering: The SEMAT Kernel. *Communications of the ACM.* https://cacm.acm.org/practice/the-essence-of-software-engineering/
7. Jacobson, I. (2012). The Essence of Software Engineering: The SEMAT Kernel. *ACM Queue.* https://queue.acm.org/detail.cfm?id=2389616
8. SEMAT Quick Reference Guide. https://semat.org/quick-reference-guide.html
9. Ivar Jacobson International. Essence Explained. https://www.ivarjacobson.com/essence-explained-agile-tools
10. Ivar Jacobson International. Essence Activity Spaces. https://www.ivarjacobson.com/publications/articles/essence-activity-spaces
11. Ionita, D., Wieringa, R., Bullee, J-W., Vasenev, A. (2018). Essence: Reference Architecture for Software Engineering. *ICSOFT 2018*. https://www.scitepress.org/papers/2018/67936/67936.pdf
12. Levenchuk, A. (2015). Towards a Systems Engineering Essence. *arxiv.org.* https://arxiv.org/abs/1502.00121

### Levenchuk Primary Sources
13. Levenchuk, A. (2012). Основа — сущности и язык для методов программной инженерии (OMG Essence). *ailev.livejournal.com.* https://ailev.livejournal.com/1051048.html
14. Levenchuk, A. (2013). ISO 15288 и OMG Essence. *ailev.livejournal.com.* https://ailev.livejournal.com/1067999.html
15. Levenchuk, A. (2013). Яблоки из задачи и яблоки из жизни: альфы и рабочие продукты. *ailev.livejournal.com.* https://ailev.livejournal.com/1082662.html
16. Levenchuk, A. (2015). Мой доклад на АПСПИ-2015 в секции "SEMAT методология." *ailev.livejournal.com.* https://ailev.livejournal.com/1188876.html
17. Levenchuk, A. (2016). Об оригинальные альфы Essence. *ailev.livejournal.com.* https://ailev.livejournal.com/1318973.html
18. Levenchuk, A. (2017). Системная схема предприятия. *ailev.livejournal.com.* https://ailev.livejournal.com/1331004.html
19. Levenchuk, A. (2021). Системная схема и подальфы учебного курса. *ailev.livejournal.com.* https://ailev.livejournal.com/1575106.html
20. Levenchuk, A. (2024). Альфы и артефакты/«рабочие продукты.» *ailev.livejournal.com.* https://ailev.livejournal.com/1718836.html
21. Levenchuk, A. (2024). Методология в интеллект-стеке. *ailev.livejournal.com.* https://ailev.livejournal.com/1725757.html
22. Levenchuk, A. (2015). Системноинженерное мышление (2nd ed.). *TechInvestLab.* https://techinvestlab.ru/files/systems_engineering_thinking/systems_engineering_thinking_2015.pdf
23. Levenchuk, A. (2024). Методология 2025. Ridero. https://flibusta.su/book/358645-metodologia-2025/read/
24. Levenchuk, A. (2024). Системное мышление 2024. Ridero. https://books.yandex.ru/books/oTQZfRrv/read-online
25. Levenchuk, A. (2023). Интеллект-стек 2023. Ridero. ISBN 978-5-0060-4990-1. https://ridero.ru/books/intellekt-stek_2023/
26. Project system schema chapter. *WikiReading.* https://fil.wikireading.ru/h6xqzgWEOR
27. Tsepkov, M. (2014). Курс системной инженерии от Левенчука. *mtsepkov.org.* https://mtsepkov.org/Блог:Максима_Цепкова/2014-05-27:_Курс_системной_инженерии_от_Левенчука
28. Baguzin, S. (2021). Анатолий Левенчук. Системное мышление. *baguzin.ru.* https://baguzin.ru/wp/anatolij-levenchuk-sistemnoe-myshlenie/

---

## Glossary

### Bilingual Term Table

| Russian (ШСМ/Levenchuk) | English (OMG Essence) | Notes |
|-------------------------|----------------------|-------|
| Альфа | Alpha | Universal in both systems; ШСМ redefines as "предмет метода" (method subject) |
| Предмет метода | Method subject / Alpha | ШСМ's generalized definition of alpha |
| Состояние альфы | Alpha state | Identical semantics in both systems |
| Контрольные вопросы / Чеклист | Checklist items | Same structure; ШСМ sometimes says "контрольный список" |
| Рабочий продукт / Артефакт | Work product / Artifact | Same concept; ШСМ uses "артефакт" more in recent editions |
| Воплощение системы | System Embodiment / System Realization | ШСМ replaces "Software System"; emphasizes physicality |
| Определение системы / Описание системы | System Definition | ШСМ replaces "Requirements"; includes architecture and all models |
| Технология | — (no direct Essence alpha) | ШСМ Endeavor alpha (middle period); replaces Way of Working |
| Метод / Способ работы | Way of Working | ШСМ uses "метод" broadly; Way of Working is one synonym |
| Стейкхолдеры | Stakeholders | Preserved; also "внешние проектные роли" (external project roles) |
| Возможности | Opportunity | Preserved; plural form used |
| Работы | Work | Preserved; ШСМ may distinguish project-level works from system-operation works |
| Команда | Team | Preserved; ШСМ includes AI agents explicitly |
| Область интересов | Area of concern | Three areas: Customer, Solution, Endeavor |
| Клиентская область | Customer area | Concern area for Opportunity and Stakeholders |
| Инженерная / область решения | Solution area | Concern area for System Definition and Embodiment |
| Менеджерская область / Предпринятие | Endeavor area | Concern area for Work, Team, Way of Working/Technology |
| Граф создания | Creation graph | ШСМ addition; three-level mereological structure |
| Целевая система | Target system / System of Interest | System being created; hosts Solution area alphas |
| Использующая система / Надсистема | Super-system / Using system | System using the target; hosts Customer area alphas |
| Обеспечивающая система | Enabling system / Creation system | System creating the target; hosts Endeavor area alphas |
| Трансдисциплины | Trans-disciplines | ШСМ addition; domain-independent thinking practices |
| Интеллект-стек | Intellect stack | ШСМ addition; layered architecture of trans-disciplines |
| Стратегирование | Strategizing / Method selection | ШСМ addition; meta-practice of choosing how to work |
| Мышление письмом | Writing-as-thinking | ШСМ addition; modeling through structured text |
| Деятельность / Пространство дел | Activity space | Levenchuk's 2012 translation; later sidelined |
| Подальфа | Sub-alpha | Alpha whose progression drives a parent alpha; used in both systems |
| Мета-мета-модель | Meta-meta-model | The type system (Essence Language level); ШСМ frames it as a "machine of types" |
| Агент | Agent (intellectual) | Person, AI agent, or organization executing a role |
| Роль | Role | Functional object; an agent plays a role in a method |
| Конструктив / Оргзвено | Construct / Organizational unit | Physical object enacting a role (person, team, AI system) |
| Экзокортекс | Exocortex | Computational extension of agent cognition (tools, AI assistants) |
| Ядро | Kernel | The domain-specific set of alphas and elements (can be software kernel or SE kernel) |
| Язык | Language | The type system for authoring kernels and practices — the reusable part of Essence |
| Практика | Practice | Composable unit of activities + work products + competencies; synonym of метод in ШСМ |
| ШСМ | School of Systems Management / Школа системного менеджмента | Levenchuk's educational institution; site: system-school.ru |
| SEMAT | Software Engineering Method and Theory | Founding community; site: semat.org |
| OMG | Object Management Group | Standards body; published Essence; site: omg.org |

---

*Research compiled from primary sources: OMG specification documents, SEMAT materials, Levenchuk's blog posts on ailev.livejournal.com (2010–2024), ШСМ course textbooks, and the "Методология 2025" and "Системное мышление 2024" books. Where specific claims could not be confirmed from primary sources, ⚠ Unverified: or [Conjecture] flags are used.*
