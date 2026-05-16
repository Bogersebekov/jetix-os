---
title: Methodology lineage — на ком Левенчук опирается, что заимствует, что добавил своего
date: 2026-05-17
type: distillation
parent_prompt: prompts/fpf-iwe-levenchuk-deep-study-2026-05-17.md §3.1 item 11
F: F4
G: distillation-4
R: refuted_if_attribution_incorrect
prose_authored_by: claude (scribe)
language: russian + english
---

# Methodology lineage по Левенчуку

> **Constitutional posture.** Surface'инг attribution + cited innovations. No evaluation
> «больше/меньше credit due». Verbatim where possible.

---

## §1 Three-generation framing (Левенчуковский собственный)

**Verbatim R-A §1.2 (transcribed from Левенчуковский framing):**

### Gen 1 (absorbed wholesale)
- **Ludwig von Bertalanffy** — General Systems Theory (GST)
- **Norbert Wiener** — Cybernetics (1948)
- **Arthur Koestler** — Holons (part-whole nesting)

**Levenchuk's contribution:** recognition + integration as historical base; some critique on second-generation reductionism.

### Gen 2 (absorbed + critiqued)
- **Peter Checkland** — Soft Systems Methodology (SSM)
- **ISO/IEC/IEEE 15288** — system lifecycle
- **ISO/IEC/IEEE 42010** — architecture descriptions
- **ISO 15926** — 4D extensionalism (engineering ontology)
- **Ivar Jacobson + SEMAT** — Essence Kernel (alpha state machines, situational method engineering)

**Levenchuk's contribution:** adapted Essence Kernel for systems engineering (2015 arXiv paper); generalized Essence Language (kept) + replaced software-specific kernel (rejected); developed ISO 15926 methodology + .15926 Editor tool; produced Russian ArchiMate 2.0 terminology.

### Gen 3 (his synthesis, 2020s)
**Source ideas:**
- **Karl Friston** — Active Inference / Free Energy Principle
- Open-ended evolution (techno-evolution lineage)
- Continuous delivery / continuous everything (DevOps scaled к SE)
- **Category theory + mereotopology** — foundation ontology
- NQD OEE (Novelty-Quality-Diversity in Open-Ended Evolution)

**Levenchuk's contribution:** original synthesis + 2023 arXiv paper «Toward an Ontology for Third Generation Systems Thinking»; FPF as 2026 synthesis.

`[R-A §1.2 L52-66]`

---

## §2 Specific direct influences (named individuals)

### §2.1 SEMAT lineage

- **Ivar Jacobson** (along with Bertrand Meyer + Richard Soley) — SEMAT founding 2009
- Essence v1.0 OMG 2014; v1.2 2018; v2.0 alpha draft Feb 2024
- Левенчук = SEMAT supporter; INCOSE × SEMAT 2013-2014 joint project

**Levenchuk's specific borrowing (R-D Section 2.1):**
> «Levenchuk treats the **Essence Language** — the type system — as essentially correct and preserves it verbatim: alpha construct + past-participle state naming + state-checklist structure + alpha-state graph + work products as manifestation + "things to care about" framing + alpha containment.»

**Levenchuk's specific modifications (R-D §2.2):**
- 2015 SE Essence paper: replaced «Requirements / Software System» с «System Definition / System Embodiment» (per ISO 42010)
- Intermediate (2014-2020): replaced «Way of Working» с «Технология»
- 2023-2024: stabilized at 4 universal alphas (воплощение, описание, метод, работы)

**Levenchuk's additions (R-D §2.3):** граф создания (3-level mereology), стратегирование (meta-method), интеллект-стек (transdisciplines), мышление письмом, AI agents as role executors.

### §2.2 Philosophical sources (R-A §1.2)

- **Charles Sanders Peirce** — pragmatism + semiotics → actively formalizing in FPF semio-architecture workstream (active 2025-2026 per LJ Feb 2026 + 10th MIM conf «E.10.SEMIO campaign» upstream)
- **John Searle** — speech acts + institutional ontology
- **Karl Popper** — epistemology as conjectures + refutations (vs SMD Hegelian dialectics)
- **Daniel Dennett** — «hold your definition» anti-essentialism → «Definition as Coffin for a Dead Think» per psybertron capture

### §2.3 Russian methodological context

- **Georgy Shchedrovitsky (Щедровицкий)** — СМД-методология (Systems-Thought-Activity)
- **Pyotr Shchedrovitsky** (son) — engaged + acknowledged Левенчуковский school positively per `mtsepkov.org 2020-08-16` notes

**Levenchuk's position (R-A §6.1):**
> «He engages with SMD concepts (thought-activity methodology, organizational activity games) but rejects the dialectical-Marxist epistemology in favor of Popperian falsificationism and engineering pragmatism.»

### §2.4 Austrian School / praxeology

- **Ludwig von Mises** — praxeology (theory of human action)
- Per R-A §3.1: «libertarian-Austrian-school influence on his emerging methodology framework, emphasizing purposeful human action and market coordination over planning-based approaches»

**Bio context.** Левенчук founded «Московский Либертариум» in 1994; consistent libertarian thread through securities-market work + INCOSE work.

### §2.5 Active Inference Institute / Friston

- **Karl Friston** — Free Energy Principle + Active Inference
- **Ivan Metelkin** — Active Inference Institute co-founder + МИМ mentor — interface к Fristonian international community
- 2023 arXiv paper formally cites Active Inference as physics-based foundation

---

## §3 What Левенчук ADDED (not borrowed) — innovation provenance

Per R-A §4.2 attribution table:

| Framework | Originated by | Левенчук's contribution |
|-----------|--------------|------------------------|
| Alpha state machines | SEMAT (Jacobson) | Adapted for SE; expanded beyond software |
| ISO 15288/42010/15926 | ISO/IEC/IEEE committees | Synthesized в Russian SE pedagogy; contributed RDL methodology |
| Active Inference / Free Energy | Karl Friston | Incorporated as physics-based foundation |
| Writing-as-thinking | Tradition (various) | Systematized + positioned as primary intellect-stack practice |
| Transdiscipline stack concept | Building on SMD + GST + Austrian school | Original synthesis + operationalization |
| Third-generation ST ontology | Building on Bertalanffy / Checkland / SEMAT | Original formalization + arXiv 2023 publication |
| **FPF** | **Original** | **Entirely new pattern language — no direct precursor** |
| Exocortex framing | Term from transhumanism literature | Original application to LLM-augmented intellect-stack в engineering contexts |
| Граф создания (creation graph) | Building on SEMAT + ISO 15288 + mereology | Original 3-level structural formalization |
| Стратегирование | Building on Goldratt + Austrian school + abductive reasoning | Original «infinite strategizing» framing as continuous practice |

`[R-A §4.2 L273-284]`

---

## §4 Detailed lineage of selected primitives

### §4.1 Альфа (Alpha) → from SEMAT, generalized

**Per R-B §2.1:**
> «Alpha definition borrowed verbatim from SEMAT Essence kernel (Ivar Jacobson 2012). Левенчуковский extension: from software-only к any project situation.»

> «An alpha is an essential element of the software-engineering endeavor… relevant to an assessment of its progress and health.»
> — Jacobson 2012 [via R-B §2.1 L170]

> «Alphas are what we progress. Alphas exist whether there are tangible work products or not.»
> — Jacobson 2012 [via R-B §2.1 L172-174]

Левенчук reinterprets «alpha» NOT as backronym but as «предмет метода» (subject of method).

### §4.2 Граф создания → from Essence 2.0 + holonic mereology

**Per R-B §3.1:**
> «Моделировать граф создания […] по мотивам OMG Essence 2.0:2024.»

**Per R-D §2.3:** Levenchuk introduces 3-level mereology (super / target / enabling system) NOT in original Essence; aligns with Левенчуковский 2015 arXiv paper + ISO 15288 system-of-interest framing.

### §4.3 Стратегирование → from praxeology + abductive reasoning + Goldratt

**Per R-B §4.1 + Левенчуковский:**
- Praxeology (Mises) — purposeful action under uncertainty
- Abductive reasoning (Peirce) — «what could be true?» hypothesis generation
- Theory of Constraints (Goldratt) — WIP-limited bottleneck thinking
- Левенчуковский innovation: «infinite strategizing» = continuous practice (not document)

### §4.4 Мышление письмом → tradition systematized

Various sources (Linn / Joyce in writing studies; Naur's «theory» from programming as theory building; Zettelkasten from Luhmann) but **systematized + positioned as primary intellect-stack practice по Левенчуку** = original contribution.

**FPF dedicated section per Spec L515-533:** «Thinking Through Writing: The FPF Discipline of Conceptual Work».

### §4.5 FPF — entirely original

Per R-A §4.2: «**FPF — Original — no direct precursor**».

This is the strongest attribution claim в R-A: FPF as «entirely new pattern language». Anchored in 4-layer architectural pattern language tradition (Christopher Alexander «A Pattern Language» 1977; software design patterns Gamma 1994; pedagogical patterns; pliant patterns) — но as «operating system for thought for mixed human/AI teams» = новое.

---

## §5 Western SE positioning

Per R-A §1.2 closing:
> «Levenchuk is aware of and engages with INCOSE-mainstream systems engineering; he served as INCOSE Russian Chapter President. But he consistently critiques "systems engineering standards" as insufficient when used alone — they address second-generation concerns and miss the evolutionary, continuous-delivery, and multi-agent coordination challenges of the current era.»

**International contributors / collaborators per R-A §7.2:**
- **Victor Agroskin** — INCOSE member, Ontology Summit (POSC Caesar, FIATECH, ISO)
- **Vyacheslav Mizgulin** — Candidate of Technical Sciences, INCOSE member
- **Vyacheslav Kunev** — IT Association President (Moldova)

**Key English-language engagement:**
- Ian Glendinning (Psybertron.org) — described Левенчука + Агроскина as «the smartest people I ever met anywhere in any context»
- Active Inference Institute (Ivan Metelkin link)
- FPF GitHub: 320 stars + 52 forks as of April 2026

---

## §6 What we don't yet have

- Full bibliographic-style lineage tree for every Левенчуковский concept (would need «Методология 2025» book deep read — paid blocker B1)
- Specific page-cites from Levenchuk's books для each named influence
- Левенчуковский собственный treatment of «debt» (acknowledgments — what he explicitly cites in each book)

---

*Distillation §4 complete.*
