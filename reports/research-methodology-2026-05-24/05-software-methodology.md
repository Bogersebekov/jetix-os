---
title: Phase 5 — Software methodology lineage (Dijkstra discipline + Knuth literate + Brooks Mythical Man-Month + Unix philosophy + Martin Clean Code + Karpathy Software 2.0/LLM-OS)
date: 2026-05-24
phase: 5
parent_prompt: prompts/research-methodology-2026-05-24.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2 (verbatim citations) + F3 (synthesis)
G: research-methodology
R: refuted_if_R1_strategic_prose_authored_OR_LOCK_modified
constitutional_posture: R1 surface only + R2 + R6 + R11 + R12 + IP-1 + EP-5 + AP-6 + append-only + SKIP-list
status: phase-5 surface
language: russian primary
---

# Phase 5 — Software methodology lineage

> **Цель.** Распаковать **software-engineering tradition как methodology
> ancestry**: Dijkstra structured-programming discipline + Knuth literate
> programming + Brooks Mythical-Man-Month + Unix philosophy + Martin clean-code
> + Karpathy software 2.0 / LLM-OS. Эта линия особо важна для Jetix потому
> что Jetix substrate = effectively a software-engineering system.

---

## §0 TL;DR (≤300w)

Software engineering — **first discipline where methodology became explicit
1st-class concern** для intellectual workers at scale.

**6 traditions** lineage:

1. **Dijkstra «Notes on Structured Programming» 1968-72** — anti-GOTO discipline,
   step-wise composition, proof-of-correctness, "designing a class of computations"
   not "making a program"
2. **Knuth «Art of Computer Programming» 1968-** + Literate Programming 1984 —
   programs as expositions for humans
3. **Brooks «Mythical Man-Month» 1975** — "adding people to a late project makes
   it later"; conceptual integrity + No Silver Bullet
4. **Unix philosophy (Thompson/Ritchie 1969+ / Raymond 2003)** — small composable
   tools, plain text streams, do one thing well, modularity
5. **Martin «Clean Code» 2008 + «Clean Architecture» 2017** — SOLID principles,
   names matter, refactoring discipline
6. **Karpathy «Software 2.0» 2017 + LLM-OS 2023** — neural networks as
   programming substrate; LLM as new operating-system kernel

**Convergence:** software-methodology = **complexity-control discipline**.
Common thread: humans cannot hold большие systems in head simultaneously;
methodology = discipline for **modularising / abstracting / verifying** код
так чтобы piecewise-tractable.

**Jetix relevance:** Jetix-substrate = (a) software system at code-level
(skills / hooks / configs / wiki MD), (b) LLM-augmented cognition system
(Karpathy LLM-OS realised), (c) methodology system at meta-level. All 6
traditions contribute distinct discipline layers.

---

## §1 Dijkstra — structured programming discipline

### §1.1 EWD 316 «A Short Introduction to the Art of Programming» 1971

Edsger Dijkstra (1930-2002) — Dutch computer scientist; Turing Award 1972.
EWD 316 (cited as "Dijkstra-short-intro-art-of-programming-1969" в Jetix
corpus; actually August 1971 lecture notes published as Technische Hogeschool
Eindhoven dictaat). Available full MD 181 KB / 3044 lines.

**Tradition:** structured programming, methodology of programming as
mathematical discipline.

### §1.2 Central thesis — "designing a class of computations" not "making a program"

**Verbatim** [src: Dijkstra 1971 line 160]:
> «It is not unusual -although a mistake- to consider the programmer's task to
> be the production of programs. ... This mistake may be at the heart of the
> management failure which is so apparent in many large software efforts. It is
> a mistake, because the true subject matter of the programmer's activity is
> not the program he composes, but the class of possible computations that may
> be evoked by it, the "production" of which he delegates to the machine.
> It seems more fruitful to describe the programmer's activity as "designing a
> class of computations", rather than as "making a program".»

**Implication для methodology:** код = artefact; настоящий продукт = behaviour
space (= Левенчук's «alpha state graph»). Resonance с Левенчук's "method as
pattern of behavior".

### §1.3 Action / Process / Algorithm definitions

**Action** [Dijkstra line 162]:
> «An action is a happening, taking place in a finite period of time and
> establishing a well-defined, intended net effect.»

**Process:** «dissect such a happening as a time sequence of (sub)actions, the
cumulative effect of which equals the net effect of the total happening» [line 177].

**Algorithm** [Dijkstra line 220]:
> «An algorithm is the description of a pattern of behaviour, expressed in
> terms of a well-understood, finite repertoire of named (so-called "primitive")
> actions of which it is assumed a priori that they can be done.»

**Connection to Левенчук:** «алгоритм описывает паттерн поведения» = direct
overlap с Левенчук's «метод/практика — это паттерн работ». Levenchuk 2025 takes
this CS lineage and generalises к agent-systems.

### §1.4 Connectives (sequencing / conditional / repetitive)

Dijkstra's structured-programming 3 connectives [line 297-345]:
- Sequence `;` (semicolon)
- Conditional `if X do Y`
- Repetition `while X do Y`

**Methodology gain:** complete behaviour-class can be expressed without GOTO
using only these 3 connectives + composition + abstraction (subroutines).
This is the **structured-programming theorem** (Böhm-Jacopini 1966).

### §1.5 Step-wise program composition

Dijkstra's primary methodology: **decompose problem top-down** through layers
of abstraction; refine each layer until primitives reached. Each level is
**meaningful in own right** (Левенчук parallel: разложение метода по уровням
мета-мета-model / мета-model / model).

[src: Dijkstra 1971 §A first example of step-wise program composition; line 1582]

### §1.6 Loop invariants (correctness discipline)

**Verbatim** [src: Dijkstra 1971 line 849]:
> «While the typical use of variables manifests itself with the program loop,
> the way to understand such a program implies looking for the relations between
> their values which remain invariant during the repetition.»

**Methodology gain:** мастер код требует articulating **invariant relations**
that hold через iteration. Resonance с Polya 4-stage "look back" + Левенчук
«проверка чеклиста состояний альфы».

### §1.7 «GOTO Considered Harmful» (1968)

Dijkstra's famous letter to Communications of ACM. Argues that unrestricted
GOTO destroys ability to reason about program behaviour. Catalysed structured-
programming revolution.

[src: Dijkstra E.W. 1968 «Go To Statement Considered Harmful» CACM 11:3 147-148]

### §1.8 «The Discipline of Programming» 1976

Dijkstra full book on programming methodology. **Predicate calculus + weakest
preconditions** as foundation для formal program design. Established
program-verification-as-construction (vs program-verification-as-after-the-fact).

[src: Dijkstra E.W. 1976 «A Discipline of Programming»]

**Methodology gain:** programs designed **alongside their correctness proofs**.
Verification is not after-thought; it shapes the design.

---

## §2 Knuth — Art of Computer Programming + Literate Programming

### §2.1 TAOCP (1968-) и Knuth methodology

Donald Knuth (1938-) — Stanford computer scientist; Turing Award 1974.
«The Art of Computer Programming» multi-volume series (vol 1 1968 / vol 2 1969
Fundamental Algorithms + Seminumerical Algorithms; available в Jetix corpus
2.2 MB MD / 60153 lines).

**Methodology contribution:** algorithms as mathematical objects of careful
analysis (asymptotic complexity, average-case + worst-case analysis, randomised
analysis).

### §2.2 Literate programming (1984)

**Verbatim** [Knuth «Literate Programming» 1984 paper]:
> «Instead of imagining that our main task is to instruct a computer what to
> do, let us concentrate rather on explaining to human beings what we want a
> computer to do.»

**Methodology move:** code = communication artefact для humans first, machine
second. Program structure follows human-explanatory logic, not compiler-
convenience.

Tools: WEB / CWEB systems weaving code + documentation в single source. Modern
incarnations: Jupyter notebooks, Markdown-driven docs (Jetix wiki = literate-
programming pattern applied to organisational knowledge).

[src: Knuth D. 1984 «Literate Programming» Computer Journal 27(2):97-111]

### §2.3 Premature optimization is the root of all evil

**Verbatim:** *"Premature optimization is the root of all evil (or at least
most of it) in programming."* — Knuth 1974 paper.

**Methodology gain:** profile first, optimize hotspots. Don't optimize until
you have measurement data. Resonance с Polya «Look at the unknown!» — focus
attention on actual bottleneck not assumed bottleneck.

[src: Knuth D. 1974 «Structured Programming with go to Statements» ACM Computing
Surveys 6(4):261-301]

---

## §3 Brooks — Mythical Man-Month + No Silver Bullet

### §3.1 «The Mythical Man-Month» 1975 / 1995

Frederick Brooks (1931-2022) — IBM System/360 chief architect; Turing Award 1999.

**Brooks's Law (canonical):** *"Adding manpower to a late software project
makes it later."* Reason: communication overhead grows N² with team size +
ramp-up time for newcomers.

[src: Brooks F. «The Mythical Man-Month» 1975, anniversary edition 1995]

### §3.2 Conceptual integrity

**Verbatim:** *"Conceptual integrity is the most important consideration in
system design."* — Brooks 1975 ch. 4.

**Implication:** systems designed by single mind have **integrity** that
committee-designed systems lack. Methodology gain: chief-architect role +
"surgical team" structure preserve coherence.

**Jetix relevance:** Pillar A (constitutional documents) + Pillar C (Tier 2
12 hard rules) = explicit conceptual-integrity preservation via owner-only
strategic-prose authorship.

### §3.3 «No Silver Bullet» 1986

**Verbatim:** *"There is no single development, in either technology or
management technique, which by itself promises even one order-of-magnitude
improvement within a decade in productivity, in reliability, in simplicity."*
— Brooks 1986.

**Distinction:** essential complexity (intrinsic к problem) vs accidental
complexity (introduced by tooling/process). Silver bullets attack accidental;
no silver bullet exists for essential.

[src: Brooks F. 1986 «No Silver Bullet» Computer 20(4):10-19]

**Implication для methodology:** **no methodology** can eliminate essential
complexity; methodology can reduce accidental. Realistic methodology = humility
about gain limits.

---

## §4 Unix philosophy

### §4.1 Thompson/Ritchie origins (1969+)

Ken Thompson + Dennis Ritchie at Bell Labs created Unix 1969-1973. Implicit
methodology became explicit через Mike Gancarz «Unix Philosophy» 1995 +
Eric Raymond «Art of Unix Programming» 2003.

### §4.2 Doug McIlroy formulation (1978)

**Verbatim** [McIlroy in Bell System Technical Journal 1978]:
> «(i) Make each program do one thing well. To do a new job, build afresh
> rather than complicate old programs by adding new "features".
> (ii) Expect the output of every program to become the input to another,
> as yet unknown, program.
> (iii) Design and build software, even operating systems, to be tried early,
> ideally within weeks. Don't hesitate to throw away the clumsy parts and
> rebuild them.
> (iv) Use tools in preference to unskilled help to lighten a programming task,
> even if you have to detour to build the tools and expect to throw some of
> them out after you've finished using them.»

[src: McIlroy M.D. 1978 in Bell System Technical Journal]

### §4.3 Raymond's «17 rules of Unix Philosophy» (2003)

| # | Rule |
|---|---|
| 1 | Modularity |
| 2 | Clarity |
| 3 | Composition |
| 4 | Separation |
| 5 | Simplicity |
| 6 | Parsimony |
| 7 | Transparency |
| 8 | Robustness |
| 9 | Representation |
| 10 | Least Surprise |
| 11 | Silence |
| 12 | Repair |
| 13 | Economy |
| 14 | Generation |
| 15 | Optimization (only after profile) |
| 16 | Diversity |
| 17 | Extensibility |

[src: Raymond E.S. 2003 «The Art of Unix Programming» ch. 1]

### §4.4 Jetix Unix-philosophy adoption

| Unix rule | Jetix substrate manifestation |
|---|---|
| Modularity | swarm/wiki/ entities (9 types: concepts/entities/sources/...) |
| Composition | KM MVP `/project-bootstrap --type=<4 types>` composable |
| Simplicity | Markdown + YAML frontmatter (no DB schema lock-in) |
| Transparency | Filesystem source-of-truth (Global Rule 4) — grep-friendly |
| Generation | `.claude/config/*.yaml` config-driven (no hardcoded paths) |
| Extensibility | Per-agent niche/ symlinks + per-project mini-swarms |

---

## §5 Martin — Clean Code + Clean Architecture

### §5.1 Robert Martin «Clean Code» 2008

Robert C. Martin (1952-) — software craftsman; founder Agile Manifesto co-author.
«Clean Code: A Handbook of Agile Software Craftsmanship» (2008) = best-seller
methodology book — primarily for software engineers.

**Central thesis:** code is read far more often than written; therefore readability
trumps cleverness.

### §5.2 SOLID principles

| Principle | Description |
|---|---|
| **S**ingle Responsibility | Module/function should have one reason to change |
| **O**pen/Closed | Open for extension, closed for modification |
| **L**iskov Substitution | Subtypes must be substitutable for base types |
| **I**nterface Segregation | Many specific interfaces > one general |
| **D**ependency Inversion | Depend on abstractions, not concretions |

[src: Martin R.C. 2002 «Agile Software Development»; Martin 2008 «Clean Code»]

### §5.3 Naming + small functions discipline

- Names matter: variables/functions/classes self-documenting
- Functions small: do one thing; one level of abstraction per function
- Comments: prefer code that explains itself; comments compensate for code
  failure

### §5.4 Critique (literature)

- SOLID criticised for OOP-only framing; не applies to FP / data-flow code
- "Clean code" can be over-engineered (premature SOLID); Single Responsibility
  taken to extreme = micro-classes everywhere
- Martin's recent comments на politics → community polarised

**Implication для methodology:** SOLID = useful heuristic catalogue (Polya-
style) for OOP design; not theorems.

---

## §6 Karpathy — Software 2.0 + LLM-OS

### §6.1 «Software 2.0» 2017 essay

Andrej Karpathy (Tesla AI head 2017-2022; OpenAI founding member; now ai.com).

**Verbatim** [Karpathy 2017 «Software 2.0» Medium]:
> «Software 2.0 is written in much more abstract, human unfriendly language,
> such as the weights of a neural network. No human is involved in writing this
> code because there are a lot of weights (typical networks might have millions),
> and coding directly in weights is kind of hard. Instead, our approach is to
> specify some goal on the behavior of a desirable program (e.g., "satisfy a
> dataset of input output pairs of examples"), write a rough skeleton of the
> code (i.e. a neural net architecture) that identifies a subset of program
> space to search, and use the computational resources at our disposal to
> search this space for a program that works.»

**Methodology shift:**

| Software 1.0 | Software 2.0 |
|---|---|
| Human writes explicit rules | Human curates dataset + architecture |
| Program = source code | Program = trained weights |
| Debugging = trace through logic | Debugging = data quality + arch design |
| Testing = unit tests + integration | Testing = held-out data + metrics |

[src: Karpathy A. 2017 «Software 2.0» https://karpathy.medium.com/software-2-0-a64152b37c35]

### §6.2 LLM-OS (2023)

Karpathy 2023 talk «Intro to Large Language Models» introduces **LLM as new
Operating System kernel**:

- **CPU** ≈ LLM (autoregressive transformer)
- **RAM** ≈ context window
- **Disk** ≈ embedding-based retrieval (vector DB)
- **Internet** ≈ tool-use / function-calling
- **Peripherals** ≈ multi-modal I/O
- **User mode / kernel mode** ≈ instruction-following / pre-trained capabilities

[src: Karpathy A. 2023 «Intro to LLMs» https://youtu.be/zjkBMFhNj_g]

### §6.3 Jetix relevance

Jetix substrate = explicit Karpathy LLM-OS realisation:
- **wiki/** ≈ disk + filesystem
- **CLAUDE.md + cycle outputs** ≈ kernel ROM / boot config
- **ROY swarm 5 experts × 4 modes** ≈ process scheduler + IPC
- **mailboxes JSONL** ≈ pipes
- **mcp__ tools** ≈ syscalls
- **brigadier** ≈ init / dispatcher

[src: KM-materialization-mvp + CLAUDE.md ROY Swarm table + Method V2 §10]

### §6.4 «Sortware 2.0» implications для Jetix methodology

| Implication | Manifestation |
|---|---|
| Dataset curation = primary engineering | Jetix wiki curation = primary substrate-engineering activity |
| Architecture = constraint on program space | F-G-R triple + Foundation Parts = architecture |
| Reproducibility = data + model snapshots | Git as substrate + cycle artefacts immutable |
| Continuous improvement = active learning | Hypothesis Architecture 7-layer feedback loops |

---

## §7 Convergent methodology pattern across 6 traditions

| Discipline | Anti-pattern targeted | Mechanism |
|---|---|---|
| Dijkstra structured prog | Spaghetti code | Composition + invariants |
| Knuth literate prog | Cryptic code | Code as human exposition |
| Brooks integrity | Committee-designed mess | Chief architect role |
| Unix small tools | Monolithic complexity | Composable pipes |
| Martin clean code | Hard-to-modify code | SOLID + naming + small functions |
| Karpathy Software 2.0 | Hand-coded fragile heuristics | Data-driven program synthesis |

**5-step convergent software-methodology pattern:**
1. **Bound complexity** (modularity / functions / VSM-like recursion)
2. **Make intent explicit** (invariants / literate / SOLID / dataset)
3. **Verify correctness** (proofs / tests / metrics / observability)
4. **Iterate cheap** (Unix early-throw-away / Brooks build-to-throw-away /
   Karpathy iterate dataset)
5. **Document for humans** (literate / clean names / NSB humility)

---

## §8 Connection to Левенчук methodology

### §8.1 Levenchuk 2025 §M references software methodology

Levenchuk M2025 line 56: «OMG Essence 2.0:2024 моделирование графа создания
дано по его мотивам.» OMG Essence = software-engineering meta-methodology
standard. Implicit acknowledgment of software-methodology lineage as primary
source.

### §8.2 Method-engineering inheritance

Brinkkemper 1996 Situational Method Engineering — born within IS/SE community.
Levenchuk 2025 footnote 13 directly links к SME literature через own livejournal
post.

### §8.3 «Жизненный цикл» → method evolution

Левенчук M2025 line 58: «понятие «жизненный цикл», как оно постепенно
заменилось понятием «метод» ... по мере перехода к agile инженерным процессам.»
This is direct **software-engineering history** — waterfall (life-cycle frame)
displaced by agile (method/practice frame).

### §8.4 OMG Essence Kernel inherits software-eng foundation

OMG Essence Kernel 2.0:2024 alphas (Opportunity / Stakeholders / Requirements /
Software System / Work / Team / Way-of-Working) — explicitly SW-engineering
origin; Левенчук generalises но retains SW-eng substrate.

---

## §9 Sources cited

**Primary corpus:**
- Dijkstra E.W. 1971 «A Short Introduction to the Art of Programming» EWD 316
  — full MD 181 KB / 3044 lines
- Knuth D.E. «Art of Computer Programming vol 2 Seminumerical Algorithms»
  1969 (1981 2nd ed) — full MD 2.2 MB / 60153 lines

**Cross-pulled external:**
- Dijkstra E.W. 1968 «Go To Statement Considered Harmful» CACM 11:3 147-148
- Dijkstra E.W. 1976 «A Discipline of Programming»
- Böhm C., Jacopini G. 1966 «Flow diagrams, Turing machines and languages
  with only two formation rules» CACM 9:5
- Knuth D.E. 1984 «Literate Programming» Computer Journal 27(2):97-111
- Knuth D.E. 1974 «Structured Programming with go to Statements» ACM Computing
  Surveys 6(4):261-301
- Brooks F. 1975/1995 «The Mythical Man-Month»
- Brooks F. 1986 «No Silver Bullet — Essence and Accidents of Software
  Engineering» Computer 20(4):10-19
- McIlroy M.D. 1978 Bell System Technical Journal Unix philosophy
- Gancarz M. 1995 «The Unix Philosophy»
- Raymond E.S. 2003 «The Art of Unix Programming»
- Kernighan B., Pike R. 1999 «The Practice of Programming»
- Martin R.C. 2008 «Clean Code»
- Martin R.C. 2017 «Clean Architecture»
- Martin R.C. 2002 «Agile Software Development»
- Karpathy A. 2017 «Software 2.0» Medium
- Karpathy A. 2023 «Intro to Large Language Models»
- Ousterhout J. 2018 «A Philosophy of Software Design»

**Cross-pulled Jetix:**
- Левенчук Методология 2025 (lines 56, 58, footnote 13, OMG Essence anchor)
- Method V2 §10 (Hypothesis Architecture parallels)
- KM-materialization-mvp (Karpathy LLM-OS realisation)
- CLAUDE.md ROY Swarm table

**Total: 19+ distinct anchors. Target 5+ exceeded.**

---

## §10 Key takeaways (EP-5 summary)

1. **Software engineering = first discipline где methodology became explicit
   1st-class** for intellectual work at scale.
2. **6 traditions convergent on 5-step pattern**: bound complexity / make intent
   explicit / verify correctness / iterate cheap / document for humans.
3. **Dijkstra «designing a class of computations» = Левенчук method-as-pattern**
   direct lineage.
4. **Karpathy LLM-OS realised в Jetix substrate**: wiki=disk, ROY=scheduler,
   mailboxes=pipes, mcp=syscalls, brigadier=init.
5. **Brooks «No Silver Bullet» humility** — methodology can reduce accidental
   complexity, NOT essential complexity. Realistic expectation setting.
6. **Unix small-tools philosophy operationalised в Jetix**: composable skills /
   markdown + YAML / filesystem source-of-truth / config-driven.
7. **OMG Essence Kernel inheritance** — Левенчук generalises software-engineering
   methodology к scale-free agent-systems.

---

*Phase 5 closure. ~590 lines. R1 preserved. LOCK preserved. 19+ sources cited.*
