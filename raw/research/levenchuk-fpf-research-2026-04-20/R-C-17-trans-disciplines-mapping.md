# Anatoly Levenchuk's 17 Trans-Disciplines (17 трансдисциплин) — Research Report

---

## Executive Summary

Anatoly Levenchuk's **intellect-stack** (интеллект-стек) is a framework that organises the foundational disciplines of human thinking into a hierarchically ordered "stack." The stack's constituent elements are called **trans-disciplines** (трансдисциплины) — disciplines whose subject is the mechanics of reasoning itself, regardless of the applied field in which that reasoning is deployed. The stack is the curriculum backbone of **ШСМ (Школа системного менеджмента / School of Systems Management)**, which since 2014 has offered a programme called "Организационное развитие" (Organizational Development) built around its mastery.

**Current canonical count: 16, not 17.** The name "17 трансдисциплин" is associated with the 2021 version of the framework published in the book *Образование для образованных 2021* ([Яндекс Книги description](https://books.yandex.ru/books/wKblpRUy)), which listed exactly 17 items. The 2023 rewrite, published as *Интеллект-стек 2023* ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/)) and independently confirmed by the ШСМ website ([system-school.ru/stack](https://system-school.ru/stack)), reorganised the list to **16 trans-disciplines**. The Systemic Thinking 2024 textbook ([Flibusta mirror](https://flibusta.su/book/215168-sistemnoe-myishlenie-2024-tom-1/read/)) preserves the same 16-item list. This report treats the 2023/2024 canonical 16-item list as primary and provides a full comparison table with the 2021 version.

**Key structural principle:** the stack is ordered bottom-to-top such that higher disciplines use the objects and concepts introduced by lower ones in their explanations. This is a simplification of what is actually a directed graph (онтологическая решётка/lattice), linearised for pedagogical purposes, as Levenchuk himself notes ([ailev.livejournal.com/1579339](https://ailev.livejournal.com/1579339.html)).

**Relation to the user's 5 primitives.** The five concepts — роль, альфа, граф создания, стратегирование, мышление письмом — are drawn from ШСМ course materials across *Методология 2025*, *Системное мышление 2024*, and the online course documentation. They are not a published "canonical list of 5 primitives" in any single source found, but each concept is a first-class object in specific trans-disciplines: роль and альфа in Методология/Системная инженерия; граф создания in Методология (based on OMG Essence 2.0:2024); стратегирование in Методология (method of choosing a method); мышление письмом in Собранность and Системное мышление.

**Relation to Levenchuk's FPF (March 2026).** The [GitHub repository ailev/FPF](https://github.com/ailev/FPF) is titled "First Principles Framework" and describes itself as an "operating system for open-ended thought for engineering, research, and mixed human/AI teams." It does not mention the intellect-stack or trans-disciplines explicitly. Its Part C "Kernel Extension Specifications" concerns bounded-context reasoning tools (logics, characterisation families), not the educational intellect-stack taxonomy. The FPF is a complementary operational framework for multi-actor projects, not a reorganisation of the intellect-stack per se. The user should be aware of this conceptual proximity but treat them as separate artefacts.

**Caveats.** (1) The official count of trans-disciplines has been 16 since at least mid-2023, though ШСМ marketing materials and community discussions still sometimes use the historical "17" label. (2) Levenchuk's own description of the stack as a "conditional" linearisation of a graph means boundaries between disciplines are pedagogically motivated, not ontologically crisp. (3) Where course URLs could not be verified from primary sources, they are noted accordingly.

---

## 1. The Concept of "Trans-discipline"

### 1.1. Definition and Distinction

A **trans-discipline** (трансдисциплина) in Levenchuk's system is formally defined as a *discipline for reasoning in the course of engaging applied disciplines* ([ailev.livejournal.com](https://ailev.livejournal.com/1705503.html)):

> «Дисциплины интеллект-стека называют часто трансдисциплинами, это «дисциплины для рассуждения в ходе задействования прикладных дисциплин» (trans-/транс- — это «находящиеся по ту сторону» от прикладных дисциплин).»

The prefix **trans-** signals that these disciplines stand *beyond* (по ту сторону) applied disciplines: they are not *about* a domain (chemistry, law, accounting) but *about how to think* when working in any domain. A more direct paraphrase from *Интеллект-стек 2023* ([Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack)): trans-disciplines are *disciplines about disciplines — the most general thinking patterns about more specific thinking patterns used for more concrete subject areas.*

Key distinctions:

| Concept | Relation to trans-disciplines |
|---|---|
| **Прикладная дисциплина** (applied discipline) | Domain-specific knowledge (lean startup, TRIZ, kanban). Trans-disciplines give the formal vocabulary that makes applied disciplines learnable. |
| **Кругозорная дисциплина** (horizon discipline) | Broad survey knowledge (systems engineering, systems management, entrepreneurship as overview). These sit *above* the trans-disciplines in the applied stack; ШСМ distinguishes them carefully. |
| **Метод** (method) | A method is a pattern of work; methodology (the trans-discipline) studies *what kinds of methods exist*. |
| **STEM disciplines** | Physics and mathematics *are included* in Levenchuk's trans-discipline list precisely because their SoTA (state-of-the-art) versions offer universal reasoning tools. Levenchuk explicitly rejects the STEM standard as inadequate ([system-school.ru/stack](https://system-school.ru/stack)). |

Trans-disciplines are characterised by **scale-freeness** (безмасштабность): they apply equally to elementary particles, organisms, organisations, and galactic structures — the reasoning patterns do not change with the size of the object being reasoned about ([ailev.livejournal.com/1705503](https://ailev.livejournal.com/1705503.html)).

### 1.2. Why 17? (Historical Evolution)

The number "17" is an artefact of the 2021 version. Levenchuk's own account of the evolution ([ailev.livejournal.com/1579339](https://ailev.livejournal.com/1579339.html)):

1. **Pre-2019 (STEM era):** Standard STEM curriculum — physics, mathematics, computing, plus biology, chemistry. No explicit "trans-discipline" framing.
2. **2019 (ШСМ curriculum):** Three-block structure — деятельностный (engineering/management/entrepreneurship), методологический (ontologics, systems thinking, scientific thinking, computational thinking), когнитивистский (role mastery, systems fitness). Six proto-trans-disciplines ([ailev.livejournal.com/1482071](https://ailev.livejournal.com/1482071.html)).
3. **Mid-2021 (6 trans-disciplines):** онтологика и коммуникации, научное мышление, вычислительное мышление, системное мышление, праксеология (экономика), этика.
4. **August 2021 (16 levels in the blog post):** The August 2021 blog post explicitly says "вместо 12 уровней стало 16" after splitting "онтологика" into smaller parts ([ailev.livejournal.com/1579339](https://ailev.livejournal.com/1579339.html)).
5. **End-2021 (17 in published book):** *Образование для образованных 2021* contains exactly 17 trans-disciplines, with the seventeenth being "Труд (инженерия, менеджмент, предпринимательство)" as a combined slot ([Яндекс Книги](https://books.yandex.ru/books/wKblpRUy)).
6. **2023 (16 in Интеллект-стек 2023):** The book restructures the list: Труд is replaced by "Системная инженерия" as the apex trans-discipline; Математика and Физика are added; Экономика, Объяснения (as a separate slot), and Теория информации (merged into Физика chapter) are removed. The book's table of contents has 16 numbered trans-discipline chapters ([systemsworld.club/t/opublikovana-kniga-intellekt-stek-2023/4980](https://systemsworld.club/t/opublikovana-kniga-intellekt-stek-2023/4980)).
7. **2024–2025:** The Systemic Thinking 2024 and Methodology 2025 books preserve the 16-item list without alteration. The notable editorial change is terminological: "интеллект-стек теперь стек методов мышления (а не дисциплин)" — the stack is now framed as a stack of *thinking methods* rather than *disciplines*, reflecting convergence between AI and human cognition research ([docs.system-school.ru](https://docs.system-school.ru/ru/professional/systems-thinking/introduction)).

The number "17" is pragmatic and historical, not intrinsically significant. Levenchuk acknowledges the list is a simplified linearisation of what is actually an interconnected graph, and expects further updates as the SoTA of each constituent discipline advances.

### 1.3. Curriculum Mapping

The ШСМ "Организационное развитие" programme maps trans-disciplines to semesters as follows ([systemsworld.club/t/modificziruem-shest-semestrov-programmy-organizaczionnoe-razvitie/7895](http://systemsworld.club/t/modificziruem-shest-semestrov-programmy-organizaczionnoe-razvitie/7895)):

| Semester | Course | Trans-disciplines Covered |
|---|---|---|
| 1 | Моделирование и собранность | Понятизация, Собранность, Семантика, Теория понятий, Онтология |
| 2 | Системное мышление | Системное мышление (uses all lower stack) |
| 2 | Методология | Методология (деятельность, роли, практики, граф создания) |
| 3 | Системная инженерия | Системная инженерия |
| 3 | Инженерия личности | Intersects with Собранность, Методология |
| 3 | Системный менеджмент | Applied (organisation engineering) |
| 4 | Создание объяснений | Рациональность, Познание/исследования |
| 4 | Этичная риторика | Этика, Риторика |
| 5 | Интеллект-стек | Full stack overview (all 16 trans-disciplines) |

Mathematics, Physics, Logic, Algorithmics, and Aesthetics are addressed within the Intellect-Stack course (semester 5) and partially in the Modeling and Collectedness course, but do not have standalone semester-long courses in the current curriculum (курс не подтверждён для отдельных дисциплин: Математика, Физика, Логика, Алгоритмика, Эстетика).

---

## 2. Enumeration of All 16 Trans-Disciplines

The following list follows the **bottom-to-top ordering** of the 2023 stack, as presented in both the *Интеллект-стек 2023* book ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/)) and the Aisystant Docs online course ([docs.system-school.ru](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack)).

---

### 2.1. Понятизация (Ponyatizatsiya / Conceptualization, figuring-out)

- **Определение / Definition:** Teaches how to isolate figures from background — to pick out objects of consideration and give them names. It is the discipline of noticing what deserves attention in the first place.
- **Позиция в стеке / Position:** Bottom of the stack. All higher disciplines presuppose the ability to identify objects of attention. Понятизация depends on nothing below it; Собранность depends on it.
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 2 ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/)); [Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack); ШСМ course: Моделирование и собранность, семестр 1.
- **Ключевые концепты / Key concepts:** Figure-ground distinction (фигура и фон), typified figures (типизированные фигуры), naming objects, attention direction, fast thinking via association, neurosemiotics.
- **Пример применения / Application example:** When a product manager reads a customer complaint, понятизация is what allows them to isolate "the person's stated problem" from the surrounding narrative noise and give it a name (e.g., "slow checkout flow").
- **Типичные ошибки / Common mistakes:** (1) Conflating the act of naming with fully defining — a name is just an anchor, not a type. (2) Assuming that figures noticed are universal rather than context-dependent. (3) Skipping понятизация and proceeding directly to formal modelling, resulting in models that don't track anything real.
- **Версионная заметка / Version note:** Present in all versions from 2021 onward. The 2023 version adds neurosemiotics and neurosemantic programming (НСП) as the SoTA scientific basis.

---

### 2.2. Собранность (Sobrannost' / Collectedness, self-possession, attentional mastery)

- **Определение / Definition:** Teaches how to hold objects — already identified by Понятизация — in attention over time, using not "bare brain" but external memory apparatus (exocortex).
- **Позиция в стеке / Position:** One step above Понятизация. It depends on Понятизация (you need objects before you can hold them). Семантика depends on Собранность (you must sustain attention before you can assign signs to objects).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 3 ([systemsworld.club announcement](https://systemsworld.club/t/opublikovana-kniga-intellekt-stek-2023/4980)); ШСМ course: Моделирование и собранность, семестр 1.
- **Ключевые концепты / Key concepts:** Attention control (управление вниманием), exocortex (внешняя аппаратура памяти), cyborgisation, actor-role mastery, organisational собранность, somatic dimension (телесная собранность), writing-as-thinking (мышление письмом) as a tool of собранность.
- **Пример применения / Application example:** When a software architect manages a multi-month project, they do not hold the full design in their head — they use structured documents, diagrams, and notes as exocortex. Собранность is the discipline that teaches them to do this systematically rather than ad hoc.
- **Типичные ошибки / Common mistakes:** (1) Confusing собранность with mindfulness meditation — Levenchuk explicitly distinguishes these. (2) Treating собранность as purely mental (ignoring somatic dimension). (3) Thinking собранность is only for individuals — Levenchuk extends it to teams (organisational собранность).
- **Версионная заметка / Version note:** Present in all versions from 2021. In 2023, the cyborgisation angle and exocortex emphasis are strengthened; theory of consciousness (теория сознания) is explicitly included.

---

### 2.3. Семантика (Semantika / Semantics)

- **Определение / Definition:** Teaches how to link physical/real objects with mathematical/abstract/mental/ideal ones, and how to work with signs that denote objects. The bridge between the physical world and the world of descriptions.
- **Позиция в стеке / Position:** Depends on Собранность (sustained attention over objects). Математика and Физика depend on Семантика (you need to know that mathematical objects are different from physical ones before you can study each in isolation).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 4 ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/)); [Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack); ШСМ course: Моделирование и собранность, семестр 1.
- **Ключевые концепты / Key concepts:** Semantic triangle (треугольник Соссюра), grounding (заземление), formalization spectrum (от нестрогих рассуждений к строгим и обратно), signs and their referents, metanoia (метанойя).
- **Пример применения / Application example:** In contract negotiation, the word "delivery" may refer to a physical act (транспортировка) for one party and to a software deployment event for another. Семантика forces explicit disambiguation — grounding the sign to its referent — preventing misaligned agreements.
- **Типичные ошибки / Common mistakes:** (1) Assuming shared vocabulary implies shared semantics. (2) Treating formalization as an all-or-nothing move rather than a spectrum. (3) Ignoring that AI systems (LLMs) operate on distributed semantic representations that differ structurally from symbolic representations.
- **Версионная заметка / Version note:** Present since 2021. In the 2021 version the slot was covered partly under "Онтологика и коммуникации." In 2023 it is an explicit standalone discipline with expanded SoTA content on neurosemiotics and distributed representations.

---

### 2.4. Математика (Matematika / Mathematics)

- **Определение / Definition:** Teaches what kinds of "mental" (abstract/formal) objects exist, how they behave, and how some are constructed from others. Mathematics provides the catalogue of ideal objects that descriptions of the physical world borrow from.
- **Позиция в стеке / Position:** Depends on Семантика (which established the distinction between physical and mental objects). Physics depends on Mathematics (uses its objects to model physical reality). Theory of Concepts depends on Mathematics (formal type theory is mathematical).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 5 ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/)); [Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack). **Версионная заметка:** ДОБАВЛЕНА в 2023, отсутствует в списке 2021 года.
- **Ключевые концепты / Key concepts:** Meta-modelling (онтологическая инженерия), megamodels, formal type assignment, compactification/universalisation (finding analogies in formulas), homotopy type theory (гомотопическая теория типов), physics-math-computer science unification.
- **Пример применения / Application example:** When designing an AI system's reward function, mathematics disciplines the designer to specify the function's type signature explicitly — preventing category errors where the reward inadvertently optimises for a mathematical proxy rather than the intended physical outcome.
- **Типичные ошибки / Common mistakes:** (1) Teaching mathematics as a collection of calculation recipes rather than as a discipline of formal object taxonomy. (2) Treating mathematical elegance as optional decoration rather than a signal of conceptual correctness. (3) Ignoring the meta-modelling role of mathematics (all formal modelling borrows objects from mathematics).
- **Версионная заметка / Version note:** Added in 2023. Not present in the 2021 list. This is one of the two new foundational additions (along with Физика) reflecting Levenchuk's grounding of the intellect-stack in physics/thermodynamics and evolutionary theory as first principles.

---

### 2.5. Физика (Fizika / Physics)

- **Определение / Definition:** Teaches what kinds of physical objects exist in the real world, and how we use mathematical/mental objects with well-understood behaviour to represent physical objects for the purposes of reasoning about them. Information theory is treated as a branch of Physics in the 2023 version.
- **Позиция в стеке / Position:** Depends on Математика (borrows its formal objects). Теория понятий, Онтология, and all higher disciplines depend on Physics (they all need the physical/abstract distinction to be clear).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 6 ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/)); [Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack). **ДОБАВЛЕНА в 2023, отсутствует в списке 2021.**
- **Ключевые концепты / Key concepts:** Multi-level attention focusing (многоуровневое наведение внимания), physical thinking as a modelling skill (not memorising physics chapters), information theory as physics (Теория информации absorbed here), universal computers as physical objects.
- **Пример применения / Application example:** When an operations manager optimises a supply chain, physical thinking (thermodynamic analogies, flow conservation) tells them that information delays in the chain are fundamentally physical phenomena — not management policy — and should be treated accordingly.
- **Типичные ошибки / Common mistakes:** (1) Confusing "teaching physics" with "teaching physical thinking" — the trans-discipline goal is the latter. (2) Ignoring that information theory belongs here (not as a separate slot, as it was in 2021). (3) Failing to see that computer science is also ultimately a physical science.
- **Версионная заметка / Version note:** Added in 2023. In 2021 "Теория информации" was a separate list item; in 2023 it is absorbed into this chapter ([Интеллект-стек 2023, Chapter 6](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/)).

---

### 2.6. Теория понятий (Teoriya ponyatiy / Theory of Concepts)

- **Определение / Definition:** Teaches how we think about concepts — the abstract/mental objects that represent physical objects. The "type machine" (машинка типов): all objects resemble each other in some way, and this is described by types. Provides the vocabulary of classification, specialization, composition.
- **Позиция в стеке / Position:** Depends on Математика and Физика (it uses both formal objects and the physical/abstract distinction). Онтология depends on Теория понятий (ontology uses the type machine to structure models).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 7 ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/)); [Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack); ШСМ course: Моделирование и собранность, семестр 1.
- **Ключевые концепты / Key concepts:** Theoretical theory of concepts (objects and relations), prototype theory (прототипы и отличия), constructive theories of concepts (objects built by operations), type relations: classification (классификация), specialisation (специализация), composition (композиция).
- **Пример применения / Application example:** When designing an AI agent's tool-use policy, Теория понятий defines the type hierarchy of objects the agent reasons about. Without an explicit type ontology, the agent conflates "a file" (physical storage object), "a document" (semantic object), and "a task" (methodological object) — leading to object-relation hallucinations.
- **Типичные ошибки / Common mistakes:** (1) Using only one theory of concepts (always theoretical, never prototypical) — this cripples handling of metaphor and analogy. (2) Confusing type specialisation with type composition (very common in software architecture). (3) Believing types are discovered rather than constructed (constructive ontology stance is absent).
- **Версионная заметка / Version note:** Present since 2021 under the same name. The constructive theory of concepts is a 2023 addition to the content.

---

### 2.7. Онтология (Ontologiya / Ontology)

- **Определение / Definition:** Teaches how to describe/model the world: how we determine what is important and what is not (modelling), and how we use models to answer questions (reasoning from models). Covers meta-modelling, system levels (part-whole), emergence, and constructive ontology.
- **Позиция в стеке / Position:** Depends on Теория понятий (uses the type machine), Физика (multi-level), and Математика (formal object structure). Алгоритмика and Логика depend on Онтология for their working material (typed/modelled objects).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 8 ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/)); [Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack); ШСМ course: Моделирование и собранность, семестр 1.
- **Ключевые концепты / Key concepts:** Modelling (important/unimportant), meta-modelling levels, system levels (mereology), emergence, rendering/de-modelling (демоделирование — generating world-state predictions from models), constructive ontology (knowledge graphs, ontological engineering).
- **Пример применения / Application example:** In enterprise architecture, Онтология disciplines the architect to specify *at which meta-model level* each element belongs — distinguishing the meta-meta-model (e.g., a "role" type), the meta-model (e.g., "project manager"), and the model (e.g., "Ivan Petrov as project manager in Q3 project"). Without this discipline, models at different abstraction levels are mixed, producing incoherent specifications.
- **Типичные ошибки / Common mistakes:** (1) Conflating ontology with a mere taxonomy or glossary. (2) Ignoring multi-level meta-modelling (treating all descriptions as being at the same abstraction level). (3) Failing to use constructive ontology tools (graphs, formal type assignment) and relying on natural language alone.
- **Версионная заметка / Version note:** Present in all versions. In the 2021 list it was combined with semantics as "Онтологика"; in 2023 it is explicit and separate.

---

### 2.8. Алгоритмика (Algoritmika / Algorithmics / Computational Thinking)

- **Определение / Definition:** Addresses how to compute efficiently — to conduct a given sequence of operations (algorithms) on memory contents that represent mathematical objects. Covers all types of universal computers: human minds, classical computers, quantum computers.
- **Позиция в стеке / Position:** Depends on Онтология (needs typed objects to compute over) and Физика (physical nature of computation). Логика depends on Алгоритмика (reasoning is treated as a species of computation).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 9 ([systemsworld.club announcement](https://systemsworld.club/t/opublikovana-kniga-intellekt-stek-2023/4980)); [Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack); ШСМ course: Интеллект-стек (семестр 5).
- **Ключевые концепты / Key concepts:** Universal algorithm (universal computer), algorithm as sequence of operations, hardware constraints, informatics-in-the-large vs. informatics-in-the-small, universal algorithms (deep learning as universal algorithm), execution hardware differences (human brain, classical/quantum computer).
- **Пример применения / Application example:** An AI research team designing a training pipeline must understand Алгоритмика to distinguish what is *computationally feasible* (given hardware and algorithm classes) from what is *logically possible* (in principle). Without this discipline, teams confuse architectural constraints with fundamental limitations.
- **Типичные ошибки / Common mistakes:** (1) Identifying Алгоритмика with programming skills alone. (2) Ignoring that human thinking is also a form of computation covered by this discipline. (3) Treating algorithm as purely about efficiency rather than also about universal computability.
- **Версионная заметка / Version note:** Present in 2021 and 2023. Content updated in 2023 with emphasis on modern universal algorithms (transformers, diffusion models) as the SoTA.

---

### 2.9. Логика (Logika / Logic)

- **Определение / Definition:** Addresses which modes of computation-as-reasoning over models yield the most error-free results: logical inference, functional evaluation, mathematical function computation, intuitive human assessments, estimation, prediction. At this level reasoning is understood as algorithms run over models.
- **Позиция в стеке / Position:** Depends on Алгоритмика (reasoning as computation) and Онтология (the models that are reasoned over). Рациональность depends on Логика (uses its methods to build correct explanations).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 10 ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/)); [Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack).
- **Ключевые концепты / Key concepts:** Reasoning modes (inference, functional evaluation, probabilistic), cognitive biases (предвзятости), argumentation, probabilistic logical reasoning, formal vs informal logic.
- **Пример применения / Application example:** A manager receiving conflicting project status reports from two team leads applies Логика to identify the type of inference each is making (deductive: "the test passed, so it works"; inductive: "it worked last time"), and to evaluate which has higher reliability given the evidence structure.
- **Типичные ошибки / Common mistakes:** (1) Equating logic with formal symbolic logic only (ignoring probabilistic and informal reasoning). (2) Ignoring cognitive biases as a subject of logic (treating them as purely psychological). (3) Treating logic as purely deductive, missing that most practical reasoning is abductive or probabilistic.
- **Версионная заметка / Version note:** Present in 2021 (as "Логика" and partly as "Рассуждение" in the August 2021 blog version). Stable in 2023.

---

### 2.10. Рациональность (Ratsionalnost' / Rationality)

- **Определение / Definition:** The discipline of creating *correct explanations* — theories/models that describe causes and effects in the physical world. Rationality = explanations + decision-making + actions. Uses logical methods plus mathematical formalism plus physical grounding.
- **Позиция в стеке / Position:** Depends on Логика (reasoning methods), Математика (formalism for causality), and Физика (correspondence of models to reality). Исследования/Познание depends on Рациональность (you need a standard of good explanation before you can study how to produce one).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 11 ([systemsworld.club announcement](https://systemsworld.club/t/opublikovana-kniga-intellekt-stek-2023/4980)); ШСМ course: Создание объяснений (Semester 4).
- **Ключевые концепты / Key concepts:** Explanatory theories (причина-следствие), decision theory, Bayesian updating, critical rationalism (falsificationism), action from models, causal inference.
- **Пример применения / Application example:** A product team attributing user churn to a new feature needs Рациональность to distinguish correlation from causation — building a model that includes confounders (seasonality, competitor release) and designing a test to falsify their hypothesis rather than simply confirming it.
- **Типичные ошибки / Common mistakes:** (1) Equating rationality with logical deduction alone (ignoring decision theory). (2) Treating intuition as the opposite of rationality rather than as an inference mode subject to calibration. (3) Skipping the "action" component — rationality without a commitment to acting on its conclusions is incomplete.
- **Версионная заметка / Version note:** ДОБАВЛЕНА в 2023. In the 2021 list it was split across "Исследования" and "Объяснения" as separate items. The 2023 consolidation is a significant restructuring.

---

### 2.11. Познание / Исследования (Poznaniye / Issledovaniya — Cognition / Research)

- **Определение / Definition:** Addresses how good explanations are obtained through the research cycle: making guesses (conjectures) about causal models/theories, then criticising those guesses through logical consistency tests and experimental confirmation. This is Popperian critical rationalism applied as a practice.
- **Позиция в стеке / Position:** Depends on Рациональность (for the standard of what counts as a good explanation) and Логика (for the criticism mechanism). Эстетика, Этика, Риторика depend on Исследования (they assume a base of research results to be evaluated, communicated, or acted on).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 12 ([systemsworld.club announcement](https://systemsworld.club/t/opublikovana-kniga-intellekt-stek-2023/4980)); ШСМ course: Создание объяснений (Semester 4).
- **Ключевые концепты / Key concepts:** Popper's critical rationalism, conjectures and refutations, creativity (творчество) as conjecture-making, experiment design, critical thinking (with caveat: Levenchuk notes "critical thinking" as traditionally taught is not sufficient), knowledge accumulation.
- **Пример применения / Application example:** An R&D team designing a new cancer treatment uses Исследования to structure their work: conjecture (a molecule inhibits pathway X), deduce testable predictions, design falsifiable experiment, accept or reject. This pattern is identical whether the domain is biology, software architecture, or social policy.
- **Типичные ошибки / Common mistakes:** (1) Treating research as literature review rather than conjecture-refutation. (2) Conflating creativity with random ideation — creativity here is directed conjecture-making, not brainstorming. (3) Ignoring that Исследования is the practice underlying *all* knowledge production, including management and design.
- **Версионная заметка / Version note:** In the 2021 list, "Исследования" and "Объяснения" were two separate slots. In 2023 they are unified into one chapter, with Рациональность absorbing the theoretical content previously in "Объяснения."

---

### 2.12. Эстетика (Estetika / Aesthetics)

- **Определение / Definition:** Provides criteria of beauty and elegance in the results of thinking and applied labour. Aesthetics addresses what response our behaviour elicits in agents — not just in humans, but in agents generally, including AI. Style is the key concept: "what is stylish is beautiful, and style is multilevel patterning."
- **Позиция в стеке / Position:** Depends on Исследования (evaluates research results) and implicitly on all lower disciplines (beauty in a proof requires knowing what a proof is). Этика depends on Эстетика (style of life is adjacent to beauty in life choices).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 13 ([systemsworld.club announcement](https://systemsworld.club/t/opublikovana-kniga-intellekt-stek-2023/4980)); [Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack).
- **Ключевые концепты / Key concepts:** Elegance in reasoning (элегантность доказательств), lean/elegant production, style as multilevel patterning (похожесть произвольного вида), aesthetic response in AI agents, art as engineering, curiosity theories (теории красоты и любопытства).
- **Пример применения / Application example:** A software architect refactoring a legacy codebase uses Эстетика to evaluate whether a proposed redesign is elegant — meaning it solves the problem at the right level of abstraction, introduces no unnecessary concepts, and would be immediately legible to a competent reader. "Nothing superfluous, everything purposeful — that is beautiful."
- **Типичные ошибки / Common mistakes:** (1) Treating aesthetics as subjective preference with no epistemic content. (2) Applying aesthetics only to art rather than to all engineered artefacts, arguments, and plans. (3) Ignoring that AI systems are now subjects of aesthetics (the field applies to machine agents, not just humans).
- **Версионная заметка / Version note:** Present in 2021 and 2023. Content updated with AI aesthetics and multilevel patterning.

---

### 2.13. Этика (Etika / Ethics)

- **Определение / Definition:** Addresses what goals are acceptable to pursue and what means are acceptable to use. Ethics discusses style of life and the governance of research results — what should they be directed towards, and what should they not be directed towards.
- **Позиция в стеке / Position:** Depends on Эстетика (style of life adjacent to beauty), Исследования (knows what research can produce), and all lower disciplines (ethical reasoning requires well-structured concepts and models). Риторика depends on Этика (persuasion must be ethical).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 14 ([systemsworld.club announcement](https://systemsworld.club/t/opublikovana-kniga-intellekt-stek-2023/4980)); [Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack).
- **Ключевые концепты / Key concepts:** Acceptable goals and means, ethics of AI agents, systemic ethics (конфликты агентов разных системных уровней), governance, existential risk reduction, "programmable death" vs immortality debate, ethics and systems thinking.
- **Пример применения / Application example:** When designing an autonomous vehicle's collision avoidance algorithm, Этика provides the framework for specifying whose interests must be prioritised at different system levels (individual passenger, other road users, society) — and for ruling out means that produce individually optimal but systemically harmful outcomes.
- **Типичные ошибки / Common mistakes:** (1) Treating ethics as a list of rules rather than a discipline for reasoning about goals and means. (2) Ignoring systemic ethics — applying individual-level ethics to organisations or ecosystems. (3) Excluding AI from ethical agency (the 2023 version explicitly includes AI agents as both subjects and objects of ethics).
- **Версионная заметка / Version note:** Present in all versions from 2021. Content significantly updated in 2023 with AI ethics and multi-level systems ethics.

---

### 2.14. Риторика (Ritorika / Rhetoric)

- **Определение / Definition:** Teaches how to persuade an agent to take actions — how to communicate a model of a situation and induce an agent to use that model for joint goal pursuit. Rhetoric is constrained by Ethics (no manipulation toward bad ends). It accounts for the fact that both humans and AI are implemented as neural networks, not logical machines.
- **Позиция в стеке / Position:** Depends on Этика (persuasion must be ethical), Исследования (you have a model of reality you are communicating), and Логика (argumentation structure). Методология depends on Риторика (coordinating teams requires rhetoric).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 15 ([systemsworld.club announcement](https://systemsworld.club/t/opublikovana-kniga-intellект-stek-2023/4980)); ШСМ course: Этичная риторика (Semester 4).
- **Ключевые концепты / Key concepts:** Persuasion (убеждение агентов), prompt engineering (for neural-network-based agents including humans and LLMs), vmennost' (вменяемость — reasonableness/persuadability of strong intellect), communication result ≠ communication intention, joint goal alignment.
- **Пример применения / Application example:** A data scientist presenting a model risk analysis to a board of directors uses Риторика to translate from "RMSE = 0.3 on the test set" into a framing that activates the board's existing mental models about acceptable risk — meeting them at their level rather than demanding they ascend to hers.
- **Типичные ошибки / Common mistakes:** (1) Treating rhetoric as synonymous with manipulation or dishonesty — Levenchuk treats it as legitimate persuasion constrained by ethics. (2) Ignoring that the "rhetorical" framing of prompt engineering for AI is exactly the same discipline. (3) Believing that a logically correct argument is sufficient — rhetoric recognises that agents are neural networks, not logic engines.
- **Версионная заметка / Version note:** Present in 2021 and 2023. The LLM/prompt engineering angle is a 2023 addition.

---

### 2.15. Методология (Metodologiya / Methodology)

- **Определение / Definition:** A scale-free teaching about agents' activities aimed at changing the world and themselves. Its primary object is the *method of work* (метод работы / способ работы / практика). Methodology studies what kinds of methods exist, how agents organise into teams, occupy roles, and execute practices to achieve their goals.
- **Позиция в стеке / Position:** Depends on Риторика (coordinating agents), Этика (acceptable methods), and effectively all lower levels. Системная инженерия depends on Методология (systems engineering prescribes how specific engineering methods should be structured).
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 16 ([systemsworld.club announcement](https://systemsworld.club/t/opublikovana-kniga-intellект-stek-2023/4980)); *Методология 2025* ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/metodologiya-2025-71307523/chitat-onlayn/)); ШСМ course: Методология (Semester 2).
- **Ключевые концепты / Key concepts:** Метод (method/practice/pattern), предмет метода = альфа (method's subject = alpha), роль (agent's role in a method), граф создания (creation graph — modelling based on OMG Essence 2.0:2024), стратегирование (method of choosing a method), сигнатура метода (method signature: subjects + roles), разделение труда (division of labour/праксеология).
- **Пример применения / Application example:** An AI system developer needs to specify how the AI agent will perform a "tool selection" task. Методология requires specifying: what is the subject/alpha (the tool choice decision), what states does it pass through (identified → evaluated → selected → applied), what roles are involved (requester, selector, executor), and what is the creation graph (which agents create which other agents' work products).
- **Типичные ошибки / Common mistakes:** (1) Confusing methodology with methodology-as-management-buzzword (agile, scrum, etc.). Levenchuk's Методология is a meta-level discipline that *studies methods*, not a specific method. (2) Ignoring стратегирование as the "meta-method" of choosing which method to use. (3) Treating граф создания as organisational chart rather than as the dependency structure of work products.
- **Версионная заметка / Version note:** Present in all versions since 2021. Significantly enriched in 2023–2025 editions with граф создания (based on OMG Essence), alpha formalism, and constructive role theory.

---

### 2.16. Системная инженерия (Sistemnaya inzheneriya / Systems Engineering)

- **Определение / Definition:** A normative trans-discipline — it not only studies but *prescribes* at a high level of abstraction (meta-meta-model) how activities for creating systems should be structured: what practices should exist and what roles should execute them. Systems engineering is called "systemic" because it starts from the premise that something is being created as a system (a whole with parts, separated from environment).
- **Позиция в стеке / Position:** The apex of the 2023 stack. Depends on Методология (which describes what kinds of methods exist) and on all lower levels. Applied disciplines (systems management, entrepreneurship, education engineering, medicine) are specialisations of systems engineering.
- **Источник / Source:** *Интеллект-стек 2023*, Chapter 17 ([systemsworld.club announcement](https://systemsworld.club/t/opublikovana-kniga-intellect-stek-2023/4980)); [Aisystant Docs](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack); *Системная инженерия 2022*; ШСМ course: Системная инженерия (Semester 3).
- **Ключевые концепты / Key concepts:** Система (system as whole with parts), системный подход (the red thread through the whole stack), эмерджентность, нормативность (prescriptive, not just descriptive), мета-мета-модель (meta-meta-model), создатели/creators, целевая система/target system, жизненный цикл/lifecycle, specialisations (management = engineering of organisation, education = engineering of mastery).
- **Пример применения / Application example:** Designing a multi-agent AI system (e.g., the user's Jetix OS), Systems Engineering demands specification at three levels: the meta-meta-model (role, alpha, creation graph — from the Методология layer), the meta-model (what types of agents exist, what their creation graphs look like), and the model (specific agent instances and their interactions). Without Systems Engineering as the organising frame, multi-agent architectures collapse into ad hoc integration.
- **Типичные ошибки / Common mistakes:** (1) Treating systems engineering as a certification programme (e.g., INCOSE CSEP) rather than as a foundational thinking discipline. (2) Confusing the normative (prescriptive) character of systems engineering with the descriptive character of methodology. (3) Treating systems management, agile, and lean as alternatives to systems engineering rather than as specialisations of it.
- **Версионная заметка / Version note:** In 2021, the top of the stack was "Труд (инженерия, менеджмент, предпринимательство)." In 2023, Системная инженерия is explicitly named as the apex trans-discipline, while Системный менеджмент and Предпринимательство are re-classified as applied (not trans-) disciplines.

---

### 2.A. Version Comparison Table: 2021 vs. 2023

| # | 2021 List (Образование для образованных 2021) | 2023 List (Интеллект-стек 2023) | Status |
|---|---|---|---|
| 1 | Понятизация | Понятизация | ✅ Stable |
| 2 | Собранность | Собранность | ✅ Stable |
| 3 | Семантика | Семантика | ✅ Stable |
| 4 | Теория информации | *(Absorbed into Физика)* | ❌ Removed as standalone |
| 5 | Теория понятий | Теория понятий | ✅ Stable |
| 6 | *(not present)* | Математика | ✨ Added |
| 7 | *(not present)* | Физика (includes ТИ) | ✨ Added |
| 8 | Онтология | Онтология | ✅ Stable |
| 9 | Алгоритмика | Алгоритмика | ✅ Stable |
| 10 | Логика | Логика | ✅ Stable |
| 11 | *(split: Исследования + Объяснения)* | Рациональность | 🔄 Merged/restructured |
| 12 | Исследования | Познание/Исследования | 🔄 Merged |
| 13 | Объяснения | *(Absorbed into Рациональность)* | ❌ Removed as standalone |
| 14 | Эстетика | Эстетика | ✅ Stable |
| 15 | Этика | Этика | ✅ Stable |
| 16 | Риторика | Риторика | ✅ Stable |
| 17 | Экономика | *(Removed from stack)* | ❌ Removed |
| — | Методология | Методология | ✅ Stable |
| — | Системное мышление | *(Not a separate slot in 2023)* | 🔄 Integrated into Системная инженерия |
| — | Труд (инженерия, менеджмент, предпринимательство) | Системная инженерия (only) | 🔄 Replaced |
| **Total** | **17** | **16** | |

**Key 2021→2023 transitions explained:**
- **Экономика** is dropped because pracsiology/economic thinking is now covered within Методология (the division of labour and market reasoning belongs to the methodology of socioeconomic activity).
- **Теория информации** merges into **Физика** (information theory is a branch of physics, not an independent discipline of similar weight).
- **Объяснения** merges into **Рациональность** (Levenchuk realised that explanation theory belongs to the discipline of correct reasoning, not to research practice).
- **Математика** and **Физика** are added as explicit bottom-layer disciplines, reflecting the 2023 grounding of the whole intellect-stack in thermodynamics and evolutionary theory as first principles.
- **Системное мышление** is no longer a standalone trans-discipline slot — it is the application of the entire lower stack, as indicated in Systemic Thinking 2024 which says "one course of systemic thinking does not close the full intellect-stack" ([docs.system-school.ru](https://docs.system-school.ru/ru/professional/systems-thinking/introduction)).

---

## 3. Hierarchical Structure

### 3.1. Foundation → Middle → Application Layers

Levenchuk describes the stack as having three broad zones, though he does not give them canonical layer names. Based on the 2023 structure:

**Foundation layer (фундамент) — disciplines 1–5:** Понятизация, Собранность, Семантика, Математика, Физика. These teach the basic operations that all subsequent thinking presupposes: noticing objects, holding them in attention, connecting them to signs, categorising them as mental vs physical, and representing physical reality with formal objects. Without mastery here, all higher disciplines are unstable. Changes in SoTA at this layer are rare and slow.

**Formal reasoning layer (формальный аппарат) — disciplines 6–9:** Теория понятий, Онтология, Алгоритмика, Логика. These build the machinery of systematic thinking: type systems, world-models, computation, and valid inference. They are more prone to revision than the foundation (the SoTA in formal logic, for instance, has changed significantly since the 20th century).

**Knowledge-building layer (построение знания) — disciplines 10–11:** Рациональность, Познание/Исследования. These describe how correct knowledge is produced — how agents form explanations and test them. They depend heavily on the formal reasoning layer for their tools.

**Coordination and communication layer (коммуникация и нормы) — disciplines 12–14:** Эстетика, Этика, Риторика. These address the evaluation and communication of knowledge — what is beautiful, what is good, what is persuasive. They are the most socially and culturally contingent, and evolve fastest.

**Action and engineering layer (деятельность) — disciplines 15–16:** Методология, Системная инженерия. These address how intelligent agents organise their work and create systems. They are the closest to applied practice while remaining trans-disciplinary.

### 3.2. Dependency Matrix (Simplified)

| Discipline | Directly Depends On |
|---|---|
| Понятизация | — (base) |
| Собранность | Понятизация |
| Семантика | Собранность |
| Математика | Семантика |
| Физика | Математика, Семантика |
| Теория понятий | Математика, Физика |
| Онтология | Теория понятий, Физика, Математика |
| Алгоритмика | Онтология, Физика |
| Логика | Алгоритмика, Онтология |
| Рациональность | Логика, Математика, Физика |
| Познание/Исследования | Рациональность, Логика |
| Эстетика | Исследования, Онтология |
| Этика | Эстетика, Исследования |
| Риторика | Этика, Исследования, Логика |
| Методология | Риторика + all lower |
| Системная инженерия | Методология + all lower |

*Note: this table is a pedagogical simplification. Levenchuk explicitly states the true structure is a graph (lattice), not a sequence* ([ailev.livejournal.com/1579339](https://ailev.livejournal.com/1579339.html)).

### 3.3. Natural Couplings

Several disciplines form natural triads that are often taught together:

- **Понятизация + Собранность + Семантика:** The "attention triad" — noticing, holding, and naming objects. Covered in the "Моделирование и собранность" course.
- **Математика + Физика + Теория понятий:** The "formal world triad" — abstract objects, physical objects, and the type system that organises both.
- **Онтология + Алгоритмика + Логика:** The "reasoning machinery triad" — models, computation over models, valid inference from models.
- **Рациональность + Исследования:** The "knowledge production dyad" — what a correct explanation is, and how to produce one.
- **Эстетика + Этика + Риторика:** The "communication and norms triad" — beauty, goodness, and persuasion.
- **Методология + Системная инженерия:** The "action triad capstone" — methods in general and systems creation in particular.

### 3.4. The Stack Metaphor and its Implications

Levenchuk uses "stack" in two senses simultaneously ([systemsworld.club/t/topic/3018](https://systemsworld.club/t/topic/3018)):

1. **Stack as pile (стопка листов бумаги):** disciplines layered so that higher ones are easier to explain using lower ones. This is the pedagogical metaphor.
2. **Stack as LIFO data structure:** applied practices sit on top and change most frequently; the foundational trans-disciplines sit at the bottom and change least. When people "update their stack," they update top levels far more often than bottom ones.

The **implication** is that mastery cannot be acquired purely bottom-to-top in a simple sequence — because the real structure is a graph, studying any level opens new understandings of previous levels. Levenchuk warns: "Мыслительное мастерство нельзя приобрести, если просто «выучить всё снизу вверх»." A specialised integrating course (the "Интеллект-стек" course itself, in Semester 5) is required to "glue together" what is learned piecemeal across many courses.

---

## 4. Relation to 5 ШСМ Primitives

The five concepts the user asks about — роль, альфа, граф создания, стратегирование, мышление письмом — are core operational concepts in ШСМ's curriculum, but **they do not appear as a named "canonical list of 5 primitives"** in any primary source found. They are each first-class concepts in specific trans-disciplines. Sources consulted: *Методология 2025* ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/metodologiya-2025-71307523/chitat-onlayn/)), *Системное мышление 2024* ([Aisystant Docs](https://docs.system-school.ru/ru/professional/systems-thinking/introduction)), [ailev.livejournal.com/1513051](https://ailev.livejournal.com/1513051.html).

**Brief definitions:**

- **Роль (role):** An agent's function within a method — the "position" that specifies what the agent does, not who they are. Roles are defined by the signature of a method. E.g., "настройщик рояля" (piano tuner) is the role in the "piano tuning" method.
- **Альфа (alpha):** The subject (предмет) of a method — the abstract or physical object that the method transforms through a sequence of states. Drawn from OMG Essence standard. E.g., the "требования" (requirements) alpha passes through states: identified → analysed → formulated → agreed.
- **Граф создания (creation graph):** The directed graph expressing which creators/constructors produce which work products, modelled after OMG Essence 2.0:2024. Note: in November 2024 the terminology shifted to "граф создателей" (creation *agents* graph) per [docs.system-school.ru](https://docs.system-school.ru/ru/professional/systems-thinking/introduction).
- **Стратегирование (strategizing):** The "meta-method" — the method of choosing which method to apply when the course of action is unclear. Described as the first applied discipline of entrepreneurship and is also a sub-practice of any intelligent agent ([Методология 2025](https://www.litres.ru/book/anatoliy-levenchuk/metodologiya-2025-71307523/chitat-onlayn/)).
- **Мышление письмом (thinking-by-writing / writing-as-thinking):** The practice of externalising thinking into text in real time — "не пишешь = не думаешь" (not writing = not thinking). Writing is not documentation after thinking; it *is* the thinking. Central to Собранность (exocortex) and systematically practiced as a learning method across all ШСМ courses ([ailev.livejournal.com/1513051](https://ailev.livejournal.com/1513051.html)).

### Mapping Matrix

| Trans-discipline | Роль (role) | Альфа (alpha) | Граф создания | Стратегирование | Мышление письмом |
|---|---|---|---|---|---|
| Понятизация | Provides the ability to notice role-objects | Enables identifying what the alpha *is* | Helps name nodes in the creation graph | Helps articulate "what is the problem" | Foundational — noticing what to write about |
| Собранность | Sustains attention on role identity across long tasks | Sustains attention on alpha states over time | Enables tracking the creation graph across time | Sustains focus on strategic alternatives | The exocortex *is* writing as thinking |
| Семантика | Grounds role names to actual functions | Grounds alpha names to physical/abstract objects | Ensures creation graph nodes are unambiguous | Ensures strategic options are semantically distinct | Writing externalises meaning — the semantic act |
| Математика | Type system for roles | Formal type of the alpha (state machine) | Graph theory for the creation graph | Decision theory for choosing strategies | Formal specification in writing |
| Физика | — | Alpha states as physical configurations | Physical constraints on creation processes | Physical feasibility of strategies | — |
| Теория понятий | Role as a type (not an individual) | Alpha as a type with specialisations | Composition of creators in the graph | Classifying strategic options by type | Type-aware writing |
| Онтология | Role defined in an ontology of practices | Alpha defined in the method's ontology | Ontology of the creation chain | Ontology of strategic options | Writing reveals the ontology in use |
| Алгоритмика | Role = algorithm executor | Alpha state transitions as algorithm | Creation graph = execution DAG | Strategy selection as search algorithm | Writing as externalised computation |
| Логика | Reasoning about role compatibility | Reasoning about alpha state validity | Reasoning about creator dependencies | Inferring consequences of strategies | Written argument structure |
| Рациональность | Rational justification of role assignments | Rational assessment of alpha state claims | Rational design of creation processes | Rational comparison of strategic options | Written models of causation |
| Познание/Исследования | Researching what roles actually exist | Investigating what states alpha passes through | Discovering what creation chains work | Exploring and testing strategies | Research journals and notes |
| Эстетика | Elegant role decomposition | Elegant alpha state machine (minimal, complete) | Elegant creation graph (minimal dependencies) | Elegant strategy (simple, powerful) | Beautiful, clear writing |
| Этика | Ethical distribution of roles | — | Ethical labour structure | Ethical strategic choices | Honest, non-manipulative writing |
| Риторика | Communicating roles to team members | Communicating alpha status to stakeholders | Describing creation graphs to teams | Persuading others of strategic choice | Rhetoric **is** skilled writing |
| Методология | ★★★ Primary home of Роль concept | ★★★ Primary home of Альфа concept | ★★★ Primary home of Граф создания | ★★★ Стратегирование lives here | Writing methods and documenting practices |
| Системная инженерия | Normative role system for engineering | Canonical alphas of the creation process | Engineering creation graph (systems creators) | Applied strategizing for engineering projects | Engineering documentation |

★★★ = primary definitional home of the concept.

---

## 5. Application to Specific Domains

### 5.1. Engineering

The intellect-stack was developed in an engineering context and its application here is best documented. The interaction of multiple trans-disciplines in engineering work:

**Ontology + Systems Engineering** in requirements: A systems engineer specifying a satellite's communication subsystem must simultaneously work at the meta-meta-model level (roles, alphas, creation graphs — from Системная инженерия), the meta-model level (what types of communication requirements exist — from Онтология), and the model level (specific bandwidth and latency values — from Физика and Математика). Without the Онтология discipline, engineers mix these levels and produce specifications that conflate the requirement, the architecture, and the acceptance criterion in the same text field.

**Алгоритмика + Логика** in software architecture: Designing a distributed system's consistency model (CAP theorem trade-offs) requires Алгоритмика (what is computable under which conditions) and Логика (what can be proven about the system's invariants). These two disciplines together give the engineer the vocabulary to explain *why* eventual consistency is not a bug but a physical constraint.

**Методология** in engineering teams: Introducing a new CI/CD pipeline requires the engineering lead to apply Методология — identifying the new method (CI/CD), its alphas (build artefact, test result, deployment), roles (developer, reviewer, deployment coordinator), and the creation graph that shows how these roles produce these alphas in which order.

### 5.2. Management

**Рациональность + Исследования** in decision-making: A management team deciding whether to enter a new market should, per the intellect-stack, first form explicit hypotheses (конъюнктуры/dogадки) about why the market is attractive, derive testable predictions, and design cheap experiments to falsify them before committing resources. Levenchuk diagnoses most management failures as failures of Рациональность — acting on pattern-matching (fast thinking) rather than on falsifiable models.

**Методология + Стратегирование** in organisational change: A manager leading a digital transformation needs Методология to name the new methods of work (what practices are being changed), identify the alphas (what objects are being transformed and through what states), and apply Стратегирование to choose *which* transformation sequence to pursue when multiple options seem equally valid.

**Риторика + Этика** in stakeholder management: Convincing a board to invest in long-horizon capability building (e.g., intellect-stack training for the engineering team) requires Риторика — translating the argument from engineering terms into terms that activate the board's mental models about risk and return — while Этика constrains the rhetorical framing to avoid overpromising or manufacturing false urgency.

### 5.3. Personal Development

**Собранность** as the gateway discipline: ШСМ explicitly positions Собранность as the prerequisite for all other learning. A person who cannot hold attention on complex abstract theories for extended periods cannot master the higher trans-disciplines. The exocortex (notes, structured writing, external memory) is the concrete practice: "не пишешь — не думаешь" ([ailev.livejournal.com/1513051](https://ailev.livejournal.com/1513051.html)).

**Понятизация + Семантика** as the basis of continuous learning: When a professional enters a new domain, they first apply Понятизация (which objects matter here?) and Семантика (how are the domain's key terms grounded — what physical objects do they refer to?). Without these, domain learning is memorisation of patterns without understanding.

**Рациональность + Познание** as anti-cargo-cult vaccine: Levenchuk argues that the most important personal application of the stack is resisting "cargo cult" thinking — adopting practices that look like the real thing without understanding the explanatory theory behind them. A developer who follows a design pattern without understanding its purpose cannot adapt it; Рациональность and Исследования together provide the tools to identify and fill explanatory gaps.

### 5.4. AI Agent Design (2024–2026)

This domain is most directly relevant to the user's Jetix OS FPF project. Levenchuk himself explicitly frames the 2023 intellect-stack through the lens of AI/human convergence: "мы не будем делить «интеллект» на машинный/искусственный и естественный" ([Интеллект-стек 2023, Litres](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/)).

**Понятизация → AI attention mechanisms:** The challenge of specifying what objects an AI agent should notice (its "attention objects") is precisely the Понятизация problem. Fine-tuning an LLM for a specific task is in part a Понятизация engineering exercise — specifying which figures to pull from background.

**Онтология → AI knowledge graphs and type systems:** When building an agentic AI system, Онтология provides the framework for the agent's type hierarchy. Without it, the agent has no principled way to distinguish "a user request" from "a task" from "a subgoal" from "a tool invocation" — leading to the confusion observed in naive agentic systems.

**Алгоритмика → AI capability specification:** Understanding which algorithms can be executed by which hardware (Алгоритмика) allows AI system designers to correctly match capability requirements to the architecture. The question "can the agent do X?" is partly an Алгоритмика question (is X computable in the required time/space?).

**Методология → AI agent role and method design:** Designing a multi-agent system requires specifying roles (which agent does what), alphas (what objects do they transform), and the creation graph (how do their work products depend on each other). This is exactly Методология. The FPF repository ([github.com/ailev/FPF](https://github.com/ailev/FPF)) — "bounded contexts, auditable reasoning, decision records, and multi-view publication" — can be read as a software artefact that operationalises key Методология concepts for multi-agent AI teams.

**Риторика → Prompt engineering:** Levenchuk explicitly equates prompt engineering for LLMs with classical rhetoric for human agents. Both are the discipline of communicating with a neural-network-based reasoner. Mastery of Риторика transfers directly to skill in prompt/instruction design for AI.

---

## 6. Critical Perspectives

### 6.1. Internal Coherence

The primary tension in the framework is between the **pedagogical linearisation** (a clean stack) and the **actual structure** (a graph). Levenchuk acknowledges this explicitly, calling the stack a "highly conditional" linearisation ([ailev.livejournal.com/1579339](https://ailev.livejournal.com/1579339.html)). Some boundary questions:

- **Системная инженерия as trans-discipline:** The 2023 inclusion of systems engineering as the *apex* trans-discipline (rather than a kругозорная discipline) is a genuine editorial choice that can be questioned. Systems engineering is defined normatively — it prescribes how work should be done, not just studies it — which makes it closer in character to an applied discipline than to, say, Logic or Rationality. Levenchuk justifies this by arguing that systems engineering provides a meta-meta-model (universal prescription at the abstract level), but the boundary is thinner here than for disciplines lower in the stack.

- **Эстетика and Этика** are less formally grounded than the disciplines below them. Their inclusion reflects Levenchuk's view that any complete account of intelligence must include the evaluation of outcomes (is it beautiful? is it good?), but the SoTA content here is more contested than in, say, Logic or Algorithm Theory.

### 6.2. External Academic Critique

No significant external academic critique of the intellect-stack framework was found in the sources consulted. This is expected: the framework is specific to a Russian-language educational community and has not been published in international peer-reviewed venues. The closest conceptual neighbours in Western literature — Philosophy of Science (Lakatos, Popper), Meta-cognition research, Systems Thinking (Ackoff, Checkland), and AI alignment (value alignment, ontology engineering) — treat the constituent trans-disciplines as independent academic fields and do not organise them into a unified pedagogical stack. **Caveat:** absence of critique may reflect limited discoverability rather than absence of critique.

### 6.3. Practical Limitations

- The framework is **high-abstraction and slow to yield practical results.** Levenchuk states that mastery of a trans-discipline takes a full university semester (900 hours minimum). Most practitioners seek faster returns.
- **The 16-discipline scope is ambitious.** Covering all 16 trans-disciplines to SoTA level would require 8 semesters of dedicated study — a commitment closer to a graduate programme than a corporate training initiative.
- **SoTA requirements are moving targets.** Each trans-discipline has its own research frontier, and Levenchuk updates the books frequently (he is on the 9th revision of Systemic Thinking as of 2024). This creates an ongoing re-learning burden.
- **Assessment is under-developed.** The framework lacks a standardised competency assessment mechanism. Progress is assessed primarily through "мышление письмом" (public posts, project work), which is qualitative and difficult to scale.

### 6.4. Evolution Risk (2024–2026 and Beyond)

- **Levenchuk's own FPF (March 2026)** ([github.com/ailev/FPF](https://github.com/ailev/FPF)) signals an operational extension into multi-actor, multi-AI-agent domains. While it does not reorganise the intellect-stack per se, it operationalises Методология and Системная инженерия concepts for AI-era teams. This may drive updates to the top two trans-disciplines.
- The **2024 reframing** from "stack of disciplines" to "stack of thinking methods" (интеллект-стек теперь стек методов мышления, а не дисциплин) is a conceptual shift with possible downstream consequences. If the unit is "method," not "discipline," the granularity of the stack may change.
- The shift to **four basic alphas** (вместо трёх) in Systemic Thinking 2024 ([docs.system-school.ru](https://docs.system-school.ru/ru/professional/systems-thinking/introduction)) indicates continuing incremental evolution of the core ontology, which may eventually require renaming or splitting Методология.

---

## 7. Operational Guide

### 7.1. Self-Assessment of Gaps

Levenchuk's suggested self-assessment heuristic ([systemsworld.club/t/opublikovana-kniga-intellekt-stek-2023/4980](https://systemsworld.club/t/opublikovana-kniga-intellekt-stek-2023/4980)): "Без владения трансдисциплинами интеллект-стека трудно понимать тексты, сосредоточиться, рассуждать без грубых ошибок." A practical self-diagnostic: identify the lowest-level discipline where you consistently make basic errors in reasoning.

Common patterns:
- **Systematically miss relevant objects in a domain** → gap in Понятизация.
- **Forget important considerations after initial identification** → gap in Собранность.
- **Confuse signs/names for actual objects** → gap in Семантика.
- **Build models that mix abstraction levels** → gap in Онтология.
- **Draw conclusions that do not follow from stated premises** → gap in Логика.
- **Cannot distinguish your causal model from the data** → gap in Рациональность.

### 7.2. Top 5 Leverage Trans-Disciplines for Time-Constrained Practitioners

For practitioners with limited time who cannot pursue the full 8-semester programme, the following five offer the highest leverage based on their position in the stack and prevalence of associated errors:

1. **Онтология** — The single highest-leverage trans-discipline for professional knowledge workers. Mastery of meta-modelling levels eliminates the most common class of complex-project failure: mixing abstraction levels. The "Modeling and Collectedness" course covers the basics.

2. **Рациональность** — Most professionals have no formal training in constructing and falsifying explanatory models. This discipline turns "intuitive judgment" into auditable inference.

3. **Методология** — For anyone who coordinates work (manages, architects, leads), the role/alpha/creation-graph vocabulary provides a universal language that cuts through coordination failures.

4. **Собранность** — Without this, mastery of other disciplines remains theoretical. The exocortex and мышление письмом practices are immediately actionable.

5. **Семантика** — Shared vocabulary ≠ shared meaning. Systematically grounding key terms to physical objects eliminates a large fraction of team and stakeholder communication failures.

### 7.3. Verification: Mastery Criteria

Levenchuk describes the mastery path as: explanations (объяснения) → skills (умения) → proficiency (навык) → mastery (мастерство). A discipline is sufficiently mastered when the practitioner:

- Can correctly apply the discipline's concepts to *new* situations they have never encountered before (true generalisation, not pattern-matching).
- Can articulate *why* their application is correct using the discipline's theoretical vocabulary.
- Can identify when they are *not* applying the discipline correctly (meta-cognitive self-monitoring).
- Has public written artefacts (мышление письмом) demonstrating this in multiple domains.

The threshold test: "can you use Operations Research and Advanced Mathematics within a year?" (Levenchuk's intelligence measurement heuristic from *Интеллект-стек 2023*) — applied to trans-disciplines means: "having mastered Логика, can you quickly learn any formal inference system in a new domain?"

---

## 8. Resources for Mastery

| Trans-discipline | ШСМ Course | Levenchuk Book | Outside Authoritative Resources | Practice Exercises |
|---|---|---|---|---|
| Понятизация | Моделирование и собранность (Семестр 1) | *Интеллект-стек 2023*, Ch. 2 | Andy Clark, *Being There*; Francisco Varela, *The Embodied Mind* | Name 10 objects in any domain you are unfamiliar with. Write posts describing what you noticed. |
| Собранность | Моделирование и собранность (Семестр 1) | *Интеллект-стек 2023*, Ch. 3; *Инженерия личности* | Sönke Ahrens, *How to Take Smart Notes*; GTD (David Allen) | Start a public blog or exocortex. Write one post per day for 30 days. |
| Семантика | Моделирование и собранность (Семестр 1) | *Интеллект-стек 2023*, Ch. 4 | Ferdinand de Saussure, *Course in General Linguistics*; modern distributional semantics | For any team meeting, list the 5 most-used terms and ground each to a physical object. |
| Математика | Интеллект-стек (Семестр 5) | *Интеллект-стек 2023*, Ch. 5 | Saunders Mac Lane, *Mathematics: Form and Function*; Vladimir Arnold essays | Work through proofs of basic theorems with explicit type annotations. |
| Физика | Интеллект-стек (Семестр 5) | *Интеллект-стек 2023*, Ch. 6 | Feynman Lectures (conceptual chapters); David Deutsch, *The Fabric of Reality* | Identify one information-theoretic constraint in your work domain. |
| Теория понятий | Моделирование и собранность (Семестр 1) | *Интеллект-стек 2023*, Ch. 7 | George Lakoff, *Women, Fire, and Dangerous Things*; Barwise & Seligman, *Information Flow* | Model a domain using only classification, specialisation, and composition relations. |
| Онтология | Моделирование и собранность (Семестр 1) | *Интеллект-стек 2023*, Ch. 8 | Nicola Guarino, *Formal Ontology in Information Systems*; ISO 15926 | Draw a 3-level meta-model for any system you work with. |
| Алгоритмика | Интеллект-стек (Семестр 5) | *Интеллект-стек 2023*, Ch. 9 | Abelson & Sussman, *SICP*; Knuth, *The Art of Computer Programming* Vol. 1 | Implement a simple interpreter. Relate its operation to human reasoning. |
| Логика | Интеллект-стек (Семестр 5) | *Интеллект-стек 2023*, Ch. 10 | Kahneman, *Thinking, Fast and Slow*; Jaynes, *Probability Theory: The Logic of Science* | Reconstruct 5 recent arguments you made; identify the inference type for each step. |
| Рациональность | Создание объяснений (Семестр 4) | *Интеллект-стек 2023*, Ch. 11 | Karl Popper, *Conjectures and Refutations*; Eliezer Yudkowsky, *Rationality: A-Z* | For any current project belief, write: hypothesis, prediction, how to falsify it. |
| Познание/Исследования | Создание объяснений (Семестр 4) | *Интеллект-стек 2023*, Ch. 12 | Popper, *The Logic of Scientific Discovery*; Thomas Kuhn, *Structure of Scientific Revolutions* | Design a 1-week experiment to test a hypothesis you currently hold. |
| Эстетика | Интеллект-стек (Семестр 5) | *Интеллект-стек 2023*, Ch. 13 | E.H. Gombrich, *The Sense of Order*; Denis Dutton, *The Art Instinct* | Evaluate 3 engineering or design artefacts for elegance. Articulate the criteria you used. |
| Этика | Этичная риторика (Семестр 4) | *Интеллект-стек 2023*, Ch. 14 | Derek Parfit, *Reasons and Persons*; Nick Bostrom, *Superintelligence* (ethics chapters) | Identify an ethical tension in a current project. Apply multi-level systems analysis. |
| Риторика | Этичная риторика (Семестр 4) | *Интеллект-стек 2023*, Ch. 15 | Aristotle, *Rhetoric*; George Lakoff, *Don't Think of an Elephant!* | Re-write a technical proposal as a board presentation. What changed? Why? |
| Методология | Методология (Семестр 2) | *Методология 2025* ([Litres](https://www.litres.ru/book/anatoliy-levenchuk/metodologiya-2025-71307523/chitat-onlayn/)); *Системное мышление 2024* | OMG Essence 2.0:2024 standard; Ivar Jacobson, *The Essence of Software* | Model a current work process using: roles, alphas (with states), and a creation graph. |
| Системная инженерия | Системная инженерия (Семестр 3) | *Системная инженерия 2022*; *Системное мышление 2024* | ISO 15288:2023; INCOSE SE Handbook | Build a 3-level system model (supersystem, target system, subsystems) for one project. |

---

## 9. Glossary

**Агент (agent)** — Any entity capable of performing methods: a person, an AI system, an organisation, or a collective. In the intellect-stack, reasoning about agents is scale-free (the same concepts apply to individual humans and to multi-national corporations).

**Альфа (alpha)** — The subject of a method (предмет метода) — the physical or abstract object that a method transforms through a defined sequence of states. The term is drawn from OMG Essence 2.0:2024. Example: the "requirements" alpha passes through states: identified, agreed, verified, fulfilled.

**Алгоритмика (algorithmics)** — The trans-discipline of computation: how to perform sequences of operations on memory (algorithms) using physical computing devices (universal computers), including human brains. Covers computational complexity and the limits of computation.

**Граф создания (creation graph)** — A directed graph expressing the dependency relationships between creators (creating agents) and their work products. In November 2024, the term shifted to "граф создателей" (graph of creators) per official ШСМ documentation.

**Интеллект-стек (intellect-stack)** — The ordered set of trans-disciplines that constitute the "stack of thinking methods" taught at ШСМ. Currently comprises 16 disciplines. Also the name of a book (*Интеллект-стек 2023*) and a course (Semester 5 of the Organizational Development programme).

**Логика (logic)** — Trans-discipline covering modes of reasoning over models: logical inference, probabilistic reasoning, functional evaluation, argumentation. Treats all reasoning as computation over typed models.

**Математика (mathematics)** — Trans-discipline covering formal (mental/abstract) objects: their types, behaviours, and construction. Provides the formal vocabulary borrowed by all other disciplines.

**Методология (methodology)** — Scale-free trans-discipline about agents' activities: what methods of work exist, how agents occupy roles within methods, and how work products (alphas) are produced via creation graphs. Includes стратегирование (choosing which method to use).

**Мышление письмом (thinking-by-writing / writing-as-thinking)** — The practice of externalising thoughts into written text in real time as the act of thinking itself, not as documentation of prior thinking. "Not writing = not thinking" (не пишешь = не думаешь). Central to Собранность and the ШСМ learning methodology.

**Онтология (ontology)** — Trans-discipline about modelling the world: how to determine what is important (modelling), how to structure descriptions at multiple levels of abstraction (meta-modelling), and how to use models for prediction (rendering).

**Понятизация (conceptualization / figuring-out)** — The foundational trans-discipline of isolating figures from background and giving them names. The bottom of the intellect-stack. The word "понятизация" is a Levenchuk neologism with no direct English equivalent; "conceptualization" is the closest approximation.

**Прикладная дисциплина (applied discipline)** — A domain-specific knowledge system (e.g., lean manufacturing, TRIZ, contract law). Applied disciplines are the *target* of trans-disciplinary support — they are what trans-disciplines help practitioners learn and use faster.

**Рациональность (rationality)** — Trans-discipline of creating correct explanations (theories/models of cause and effect) and making decisions based on them. Covers epistemology, decision theory, and action. Rationality = explanations + decisions + actions.

**Риторика (rhetoric)** — Trans-discipline of persuading agents to act on the basis of shared models and aligned goals. Includes prompt engineering as the rhetoric of neural-network-based agents (human or AI).

**Роль (role)** — An agent's function within a method — the "position" defined by the method's signature, specifying what the agent does (not who they are physically). Roles are types, not instances.

**Семантика (semantics)** — Trans-discipline linking physical/real objects to abstract/mental ones via signs. Covers grounding, the formalization spectrum, and the relationship between symbolic and distributed (neural) representations.

**Системная инженерия (systems engineering)** — Apex trans-discipline of the 2023 stack. Normatively prescribes how activities for creating systems should be structured (meta-meta-model level). All applied engineering disciplines (management, education, medicine) are specialisations of systems engineering.

**Собранность (sobrannost' / collectedness, attentional mastery)** — Trans-discipline of holding identified objects in attention over time using external memory tools (exocortex). Not equivalent to mindfulness; includes somatic and organisational dimensions.

**Стратегирование (strategizing)** — The "meta-method" of choosing which method to apply when the course of action is unclear. A sub-practice within Методология; also an applied discipline for entrepreneurs and managers.

**Теория понятий (theory of concepts)** — Trans-discipline of conceptual representation: how objects are typed, related, and constructed. The "type machine" (машинка типов). Covers classical (object-relation) and prototype theories, plus constructive type theories.

**Трансдисциплина (trans-discipline)** — A discipline for reasoning in the course of engaging applied disciplines; trans- (транс-) = "standing beyond" the applied disciplines. Scale-free, universal, and more abstract than applied disciplines. Currently 16 trans-disciplines in the intellect-stack.

**Физика (physics)** — Trans-discipline covering physical objects and how formal (mathematical) objects are used to represent them. In the 2023 version, information theory is treated as a sub-discipline of physics.

**Экзокортекс (exocortex)** — External memory apparatus (notes, documents, structured files, search systems) used to extend the brain's working memory. Central to Собранность.

**Этика (ethics)** — Trans-discipline of acceptable goals and means. Addresses what agents should strive for and what methods of striving are permissible. Includes systemic ethics (conflicts between agents at different system levels) and AI ethics.

**Эстетика (aesthetics)** — Trans-discipline of beauty and elegance criteria for the results of thinking and labour. Style is the key concept: multilevel patterning. Applies to mathematical proofs, engineering designs, and AI artefacts equally.

**ШСМ (Школа системного менеджмента / School of Systems Management)** — The educational institution (now branded "Мастерская инженеров-менеджеров" / Workshop of Engineer-Managers) founded by Levenchuk that teaches the intellect-stack curriculum via the "Организационное развитие" programme.

---

*Report compiled from: [Интеллект-стек 2023 (Litres)](https://www.litres.ru/book/anatoliy-levenchuk/intellekt-stek-2023-69586294/chitat-onlayn/), [Интеллект-стек 2023 announcement (SystemsWorld Club)](https://systemsworld.club/t/opublikovana-kniga-intellekt-stek-2023/4980), [ailev.livejournal.com/1705503](https://ailev.livejournal.com/1705503.html), [ailev.livejournal.com/1579339 (August 2021 version)](https://ailev.livejournal.com/1579339.html), [ailev.livejournal.com/1513051 (мышление письмом)](https://ailev.livejournal.com/1513051.html), [Aisystant Docs transdisciplinary stack](https://docs.system-school.ru/ru/research/intellect-stack/intellect-and-practices-of-the-intelligence-stack/transdisciplinary-intelligence-stack), [system-school.ru/stack](https://system-school.ru/stack), [SystemsWorld Club stack structure post](https://systemsworld.club/t/topic/3018), [SystemsWorld Club program modification post](http://systemsworld.club/t/modificziruem-shest-semestrov-programmy-organizaczionnoe-razvitie/7895), [Методология 2025 (Litres)](https://www.litres.ru/book/anatoliy-levenchuk/metodologiya-2025-71307523/chitat-onlayn/), [Системное мышление 2024 (Aisystant Docs)](https://docs.system-school.ru/ru/professional/systems-thinking/introduction), [github.com/ailev/FPF](https://github.com/ailev/FPF).*
