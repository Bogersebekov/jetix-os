---
title: Phase A-2 Dispatch Template — Interface Cards (brigadier prep)
date: 2026-04-27
phase: A-2-prep
status: template-ready (per-part dispatches pending Phase A-1 list)
cycle: cyc-foundation-build-2026-04-28
---

# Phase A-2 Dispatch Template — Interface Cards

> Brigadier-level prep before A-1 list lands. Once Phase A-1 produces the 8-14 main parts list (+ critic gate-pass), brigadier instantiates this template per part and dispatches batches of 3-5 in parallel via `engineering-expert` (integrator mode) per spec §4 Phase A-2.

---

## §1 Per-part interface card structure (per spec §4 Phase A-2)

Each interface card must declare:

### A. Inputs
What the part **consumes** — data sources, events, signals from upstream parts or external world.
- Schema: `<source>: <data-shape> :: <event-trigger>`
- Example: `voice-memos/*.ogg :: file-create-event`

### B. Outputs
What the part **exposes** — deliverables, events, queries it answers.
- Schema: `<consumer>: <data-shape> :: <event-published>`
- Example: `wiki/<niche>/<slug>.md :: ingest-completed-event`

### C. Side-effects
What the part **writes** — state transitions, mailbox postings, edges.jsonl entries, log appends.
- Per FPF IP-3: every state change is an artefact (commit, mailbox, scratchpad).
- Per D25 Company-as-Code: every change = git commit with `[area] verb what (why)` format.

### D. Dependencies (typed per FPF A.14)
Other Foundation parts this part **depends on**, with TYPED edge:
- `ComponentOf <part-name>` — strict whole-part
- `PortionOf <part-name>` — non-strict portion
- `creates <part-name>` — instance creation
- `methodologically-uses <part-name>` — applies method/pattern
- NOT generic `depends-on` (FPF A.14 violation)

### E. Boundary (per FPF A.6.B L/A/D/E discipline)
Every interface card splits:
- **Laws** — invariants that MUST hold (e.g., "every output has provenance link")
- **Admissibility** — acceptance criteria for inputs (e.g., "voice memo accepted only if duration < 30 min")
- **Deontics** — obligations of the part toward consumers (e.g., "ingest completes within 60 sec SLO")
- **Effects** — measurable outcomes (e.g., "wiki word-count increased by N")

### F. Anti-scope (what part does NOT do)
Explicit statements per FUNDAMENTAL §6 hard rules:
- Part does NOT make strategic decisions (§6.1)
- Part does NOT substitute founder agency (§6.2)
- Part does NOT use engagement-economy patterns (§6.3)
- Part-specific anti-scope (e.g., "Information Lifecycle does NOT do final synthesis output — that's Knowledge Compound")

### G. F-G-R tagging (per FPF B.3)
Per artefact emitted by this part:
- **Formality** (F0-F9): structured-ness level
- **claim-Scope** (G): bounded context of validity
- **Reliability** (R-low/medium/high/certified): trust level

### H. Originating-expert + critic-flagged
- Which A-0 expert proposed this part (or "synthesis")
- Critic flags from philosophy-expert if any (e.g., "potential Ruslan-creep risk: must avoid 11-archetype-specific schemas")

---

## §2 Per-part dispatch prompt (brigadier instantiates per part)

Template for engineering-expert (integrator mode) per part — brigadier fills `<<...>>` slots:

```
[ROLE-MODE: integrator]

You are dispatched as Phase A-2 per-part interface card writer for part <<PART-NAME>> of Jetix Foundation.

## Mission
Write the interface card for Foundation Part <<PART-NUM>> "<<PART-TITLE>>" per dispatch template at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-2-dispatch-template.md` §1 (sections A-H).

## Part scope (from Phase A-1 candidate-parts-merged.md)
- Scope sentence: <<SCOPE-SENTENCE>>
- U.System or U.Episteme: <<CLASSIFICATION>>
- FUNDAMENTAL UC mapping: <<UC-LIST>>
- FPF anchor: <<FPF-IP-OR-INVARIANT>>
- D-Lock anchor: <<LOCK-LIST>>
- AUDIT existing artefacts to reuse: <<EXISTING-ARTEFACTS>>

## Critic flags from philosophy-expert (must respect)
<<PHILOSOPHY-CRITIC-FLAGS>>

## Inputs to read
1. Phase A-1 merged list: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md`
2. A-0 originating-expert pre-read: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/<<ORIG-EXPERT>>.md`
3. Relevant FUNDAMENTAL UC: `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` §1.<<UC-CAT>>
4. SYSTEM-OVERVIEW relevant L-section: `decisions/JETIX-SYSTEM-OVERVIEW.md` §L<<X>>
5. AUDIT existing parts: `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` §<<RELEVANT-SECTIONS>>

## Output
Write to: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-<<NUM>>-<<SLUG>>.md`

200-400 words target per spec §11 deliverable checklist. Tight, structured, A-H sections.

## Discipline
- Provenance mandatory — every claim cites FUNDAMENTAL/FPF/SYSTEM-OVERVIEW/AUDIT/D-Lock with section
- A.14 typed edges in §D Dependencies — NO generic "depends-on"
- L/A/D/E split in §E Boundary — all 4 lanes populated
- F-G-R tagging in §G — actual values, not "TBD"
- Anti-scope in §F — generic + part-specific
- Generic-only — flag Ruslan-specific creep

Self-contained brief. Quality > speed. Provenance > volume.
```

---

## §3 Batch composition rule

Per spec §4 Phase A-2: **cap parallelism at 3** per batch. If list = 10 parts, run 4 batches of 2-3.

Bundle related parts into one batch where possible (e.g., Information Lifecycle + Knowledge Substrate + Provenance — all on info-flow path; one engineering-expert reads all 3 in single dispatch).

---

## §4 Post-A-2 review dispatch

After all interface cards written, dispatch:
- `systems-expert` (scalability-architect mode) — review aggregated cards. Identify: (a) cycles in dependency graph, (b) interface contradictions (Part X expects Y but Y exposes Z), (c) underspecified interfaces. Output: dependency graph + cycle/contradiction list.

Per spec §4 Phase A-2 final paragraph.

---

## §5 Output of Phase A-2

- N interface cards in `wave-a/interface-cards/part-<N>-<slug>.md`
- 1 dependency graph + cycle analysis in `wave-a/dependency-graph.md`

These feed Phase A-3 (per-part Wave C work-list bullets) and Phase A-4 (Master Plan compile).
