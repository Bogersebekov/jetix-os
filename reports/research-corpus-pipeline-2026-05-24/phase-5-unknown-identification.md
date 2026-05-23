---
title: Phase 5 — _unknown PDFs Identification
date: 2026-05-24
phase: 5/7
pipeline: research-corpus-pdf-to-md-pipeline-2026-05-24
constitutional_posture: R1 surface
---

# Phase 5 — _unknown PDFs Identification

## §5.1 Method

Read first ~3-5 pages of each _unknown/*.md (extracted in Phase 2). Identify author, title, year, language via cover/front-matter content.

## §5.2 Identifications

### 5.2.1 `17.pdf` → Г.П. Щедровицкий — собрание сочинений (том 17?)

| Field | Value |
|---|---|
| **Author** | Георгий Петрович Щедровицкий (1929–1994) |
| **Title** | Сборник работ — методология, ОДИ, СМД-подход |
| **Year** | post-1994 publication (likely сборник 2000s) |
| **Language** | Russian |
| **Pages** | 586 |
| **Volume number** | "17" из filename — likely том 17 коллекции |
| **Topics** | Системно-структурная методология, ОДИ (организационно-деятельностные игры), мыследеятельность, "Параллелизм формы и содержания мышления", СМД (схема-моделирующая деятельность) |
| **Filing** | Suggest rename → `shchedrovitsky-collected-works-vol-17.pdf` |
| **Bucket** | **methodology** (primary) + **sota** (philosophy-of-science adjacent via Меthodologische Differenzierung) |

**Note:** Schedrovitsky = Levenchuk's intellectual lineage substrate (MMK — Московский методологический кружок). HIGH relevance.

### 5.2.2 `formal-15-12-02.pdf` → OMG Essence Kernel v1.1 (December 2015)

| Field | Value |
|---|---|
| **Title** | Essence — Kernel and Language for Software Engineering Methods, Version 1.1 |
| **Publisher** | Object Management Group (OMG); document SMSC/15-12-02 |
| **Year** | December 2015 |
| **Authors** | Ivar Jacobson International AB + 11 contributor organizations (Florida Atlantic University, KTH Royal Institute, Fujitsu, Metamaxim, Stiftelsen SINTEF, University of Duisburg-Essen, etc.) |
| **Language** | English |
| **Pages** | 308 |
| **Topics** | Software engineering methods meta-model; кernel + language; method design; standardized practice + activity + work-product representation |
| **Filing** | Suggest rename → `omg-essence-kernel-software-engineering-methods-v1.1-2015.pdf` |
| **Bucket** | **methodology** (primary — formal SE method specification) + **sota** (software engineering) |

**Note:** Essence is widely cited in SE methodology literature (Levenchuk references it). Foundational for understanding "method-as-pattern-library" approach.

### 5.2.3 `visual_toolbox_chapter_1.pdf` → Climate-KIC Visual Toolbox for System Innovation (2016)

| Field | Value |
|---|---|
| **Authors** | Javier de Vicente Lopez (author) + Cristian Matti (editor) |
| **Publisher** | Climate-KIC, Brussels |
| **Year** | 2016 |
| **ISBN** | 978-2-9601874-1-0 |
| **Language** | English |
| **Pages** | 66 (Chapter 1 only — partial book) |
| **Topics** | System innovation tools, stakeholder management, sustainability transitions, facilitation patterns (Pentagonal problem, Actor tree, Empathy map, Credential cards, Stakeholder mapping/universe) |
| **Filing** | Suggest rename → `de-vicente-matti-visual-toolbox-system-innovation-ch1-2016.pdf` |
| **Bucket** | **methodology** (facilitation tools + system-innovation method library) |

**Note:** Practical companion to academic system-innovation literature. Methodology for HOW to facilitate stakeholder workshops on sustainability transitions.

## §5.3 Action items (deferred — append-only discipline)

Renames not executed in this pipeline (would break extracted MD provenance). Documented for future cleanup cycle:

| Current | Suggested rename |
|---|---|
| `_unknown/17.pdf` | `methodology/shchedrovitsky-collected-works-vol-17.pdf` |
| `_unknown/formal-15-12-02.pdf` | `methodology/omg-essence-kernel-v1.1-2015.pdf` |
| `_unknown/visual_toolbox_chapter_1.pdf` | `methodology/de-vicente-matti-visual-toolbox-ch1-2016.pdf` |

Decision authority for renames: Ruslan (per prompt §6 "NOT identify _unknown books через external API beyond first 3-5 pages + Google search" — done; rename action requires owner ack).

## §5.4 Phase 5 conclusion

All 3 _unknown PDFs identified through extracted-text analysis (no external API needed). All belong to **methodology bucket**. Inventory data added to Phase 6 cross-mapping substrate.
