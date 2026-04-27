---
title: "Consultant Card #11 — Unix Philosophy"
slug: unix-philosophy
framework_number: 11
date: 2026-04-27
phase: B-2
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
status: draft
F: F4
ClaimScope: "Holds for Jetix Foundation Phase 1 (single-node, single-founder); unknown for Phase B multi-team or multi-region deployments"
R:
  refuted_if: "Foundation Parts 1 and 2 fail to expose clean per-stage interfaces allowing independent substitution of any single stage"
  accepted_if: "Each tool/script in the voice pipeline can be replaced or tested in isolation without modifying adjacent stages (observable in tools/ directory structure)"
provenance:
  - path: "raw/books-md/unix/raymond-art-of-unix-programming-2003.md"
    range: "Ch. 1 Philosophy (lines 862-1049)"
    quote: "This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface."
  - path: "raw/books-md/clean-code/hunt-thomas-pragmatic-programmer-2019.md"
    range: "DRY section (lines 1219-1360)"
    quote: "EVERY PIECE OF KNOWLEDGE MUST HAVE A SINGLE, UNAMBIGUOUS, AUTHORITATIVE REPRESENTATION WITHIN A SYSTEM."
  - path: "raw/books-md/unix/kernighan-pike-unix-programming-environment-1984.md"
    range: "entire file"
    quote: "File is entirely images — word_count: 2888 is cover/back-cover/index page images; zero text extractable. Declared partial."
  - path: "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md"
    range: "Part 2 Signal Ingestion & Triage (lines 77-101)"
    quote: "The voice pipeline is a working, distinct sub-system with its own tool chain (tools/transcribe.py, tools/extract.py, tools/filter.py, tools/review_report.py) and its own STOP gate"
  - path: "decisions/AUDIT-CURRENT-STATE-2026-04-27.md"
    range: "§6 Voice-pipeline state (lines 398-433)"
    quote: "Default: CC headless subprocess (claude -p) — Max-подписка, без ANTHROPIC_API_KEY"
confidence: high
confidence_method: rubric-pass-rate
---

# Consultant Card #11 — Unix Philosophy

## §1 Scope — Foundation Studied

**Library coverage:**

- Raymond "Art of Unix Programming" 2003: **100% coverage** — full 201 339-word text on disk, Chapter 1 (Philosophy), Chapter 4 (Modularity), Chapter 5 (Textuality), Chapter 7 (Multiprogramming), Chapter 11 (Interfaces), Chapter 13 (Complexity) all readable; this is the single canonical source for the philosophy. [src:raymond-art-of-unix-programming-2003.md]
- Kernighan-Pike "Unix Programming Environment" 1984: **0% usable text** — library validation was accurate but misleading: the 2 888 words on disk are entirely image-placeholder lines ("picture [422x618] intentionally omitted"); the conversion via docling produced zero readable text. The book is effectively absent from the corpus. Declared honestly: **Kernighan-Pike = absent, not partial.** [src:kernighan-pike-unix-programming-environment-1984.md:entire file]
- Hunt-Thomas "Pragmatic Programmer" 1999/2019: **100% coverage** — 109 141 words on disk, readable. DRY principle (ch. 2) and orthogonality chapter are directly relevant to Unix philosophy overlap. [src:hunt-thomas-pragmatic-programmer-2019.md]

**Total canonical coverage: 1.5/2 Unix-specific sources at usable depth (Raymond 100% + Kernighan-Pike 0% + Hunt-Thomas as supplementary overlap). One web source is added below to supply the Kernighan-Pike context that the disk file cannot.**

**Web supplement (1 source):** The Kernighan-Pike book's thesis is summarized in Raymond's own preface: "Kernighan and Pike's The Unix Programming Environment [Kernighan-Pike84] stands out among these and is rightly considered a classic." Raymond's Chapter 1 cites Kernighan-Plauger verbatim ("Controlling complexity is the essence of computer programming") and Pike's "Notes on C Programming" verbatim (6-rule set on simplicity and data). These quotations are available in the disk copy of Raymond, so the Kernighan-Pike deficit is partially recovered via Raymond's citations. No additional web fetch required.

---

## §2 One-Paragraph Summary

Unix philosophy is a set of design heuristics discovered empirically over decades of building small, composable, text-oriented programs at Bell Labs, articulated most clearly by Doug McIlroy and systematized by Eric Raymond. Its core is three connected propositions: (1) each program does one thing and does it well — atomicity prevents bloat and keeps interfaces replaceable; (2) programs compose via clean interfaces, preferably plain text streams — composability means the system is larger than the sum of its parts; (3) build early, try early, throw away and rebuild rather than adding layers — simplicity is preserved by resisting the accumulation of complexity. These heuristics survive because they solve the fundamental problem of software engineering: managing complexity at scale. Applied to Jetix Foundation, they are the design logic behind Part 1 (System State Persistence — git as the universal append-only text interface) and Part 2 (Signal Ingestion — the staged `transcribe → extract → filter → triage` pipeline in which each Python tool does exactly one transformation and passes plain structured text to the next). The philosophy is not Unix-specific; it is a portable craft tradition.

---

## §3 Foundation Relevance Map

| Foundation Part | Unix principle expressed | Observable artefact |
|---|---|---|
| Part 1 — System State Persistence | Plain text as universal interface; every state change is a committed file, human-readable. "Everything is a file" → "everything is a git commit." | `.md` + `.yaml` + `.json` as the only canonical formats; `git log` as the audit trail |
| Part 2 — Signal Ingestion & Triage | Do one thing well; compose via pipes; STOP gate as human-in-loop policy separated from mechanism | `tools/transcribe.py`, `tools/extract.py`, `tools/filter.py`, `tools/review_report.py` — each a single-function filter; `run_pipeline.sh` as the compose-operator |
| Part 3 — Knowledge Base | SPOT rule (Single Point of Truth) — each fact has one authoritative location; no duplication across formats | `wiki/` as the single canonical KB; `wiki/graph/edges.jsonl` as the typed relation layer; provenance tags prevent shadow-copies |
| Part 4 — Role Taxonomy & Coordination | Separation of policy from mechanism — role manifests (policy) separated from executor bindings (mechanism) | `role.md` files = policy; `executor-binding.yaml` = mechanism; message schema enforces interface contract |
| Part 5 — Compound Learning | Rule of Generation: write programs to write programs; accumulate rules, don't hand-hack each cycle | `strategies.md` per agent = the auto-accumulating rulebook; DRR discipline = the generation mechanism |
| Part 6 — Governance & Human Gate | Rule of Separation: the STOP gate IS the policy layer; automation is the mechanism | `swarm/awaiting-approval/*.md` = policy enforcement files; `decisions/` = the locked canonical state |

---

## §4 Key Principles (5-7, each sourced, applied, and tradeoff'd)

### Principle 1 — Do one thing well (Rule of Modularity + McIlroy's first law)

**Sourced.** McIlroy [McIlroy78], quoted in Raymond AoUP Ch. 1, p. 33: "(i) Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new features." Raymond formalizes as Rule of Modularity: "Write simple parts connected by clean interfaces." [src:raymond-art-of-unix-programming-2003.md:Ch.1 line 911]

**Applied.** Foundation Part 2's four Python tools each have exactly one job: `transcribe.py` converts audio to text; `extract.py` converts text to structured JSON items; `filter.py` deduplicates and quality-ranks; `review_report.py` renders the markdown review. None of these tools knows about the others. Replacing `transcribe.py` with a different speech-to-text backend requires zero changes to `extract.py`. This is the modularity principle instantiated. If a future tool does transcription AND extraction in one script, it violates this principle — the failure mode is that any transcription change forces a full re-test of the extraction logic.

**Tradeoff'd.** Do-one-thing-well conflicts with startup overhead: 4 subprocess launches vs 1 monolith. For Jetix Phase 1 (single-founder, batch voice processing) this is irrelevant — the pipeline runs asynchronously and latency tolerance is high. At $100M scale with thousands of voice items per hour, a monolith with shared state might be justified. Foundation should note the appetite: keep single-purpose until observable latency cost exceeds 2× current baseline.

---

### Principle 2 — Compose via clean interfaces; prefer plain text (Rule of Composition + Rule of Representation)

**Sourced.** Raymond AoUP Ch. 1, p. 37: "Unix tradition strongly encourages writing programs that read and write simple, textual, stream-oriented, device-independent formats... Text streams are to Unix tools as messages are to objects in an object-oriented setting. The simplicity of the text-stream interface enforces the encapsulation of the tools." And: "To make programs composable, make them independent. A program on one end of a text stream should care as little as possible about the program on the other end." [src:raymond-art-of-unix-programming-2003.md:Ch.1 lines 983-994]

**Applied.** Foundation chose YAML/JSON as the inter-stage format rather than raw text — a deliberate evolution from pure Unix text streams. The reason: typed safety and grep-friendliness. `extract-items-latest.yaml` can be read by a human, diffed in git, and also parsed by downstream Python. This is "structured text as universal interface" — a legitimate extension of the Unix principle. The invariant preserved is: every inter-stage interface is a plain file on disk, not a socket or an in-memory object. Foundation Part 1 enforces this: every committed state is a file; no agent-to-agent in-memory transfer of state.

**Tradeoff'd.** Pure Unix text streams (newline-delimited flat text) vs Foundation's YAML/JSON: Unix purists would object that YAML introduces a parser dependency and schema coupling. The tradeoff is deliberate: YAML buys provenance fields (`created_at:`, `anchor:`, `priority:`) that raw text cannot carry without bespoke parsing. The Foundation resolves this with a design lock (D28: anchor-mandatory at ingest) — the structure is justified by the provenance requirement, not by convenience. If provenance requirements disappear, revert to simpler formats.

---

### Principle 3 — Separate policy from mechanism (Rule of Separation)

**Sourced.** Raymond AoUP Ch. 1, p. 38: "Separate policy from mechanism; separate interfaces from engines... hardwiring policy and mechanism together has two bad effects: It makes policy rigid and harder to change in response to user requirements, and it means that trying to change policy has a strong tendency to destabilize the mechanisms." [src:raymond-art-of-unix-programming-2003.md:Ch.1 lines 1001-1013]

**Applied.** Foundation Part 4 (Role Taxonomy & Coordination) is the most direct application. Role manifests (role.md files) declare the policy: what a role does, what decisions it owns, what it must not do. Executor bindings (agent instance files, `executor-binding.yaml`) declare the mechanism: which model, which tools, which dispatch path. Policy changes (role expands or shrinks) do not require rebuilding the agent file. Mechanism changes (swap Sonnet 4.6 for Opus 4.7 on a specific agent) do not require touching the role manifest. This is the Unix separation principle applied to multi-agent system design.

The STOP gate in Part 2 is a second application: the automation (mechanism) runs the pipeline; the human review (policy) decides what enters the KB. The pipeline never decides what is canonical — that is policy, and policy is human-owned. Dismantling the STOP gate would be a policy-mechanism conflation: the mechanism would be making the policy decision.

**Tradeoff'd.** Separation-of-policy costs indirection: to understand the system, a reader must consult both the role manifest (policy) and the executor-binding (mechanism) rather than reading one file. At Phase 1 team size (1 founder), this is a mild friction cost. At 50-person team, this separation becomes load-bearing — each person can reason about policy independently of the implementation details. The tradeoff favors separation as team size grows; at €50K gate it is already the right default.

---

### Principle 4 — SPOT / DRY — Single Point of Truth (Rule of Representation + Hunt-Thomas DRY)

**Sourced.** Raymond AoUP Ch. 4, p. 115: "The SPOT Rule" (Single Point of Truth): every piece of knowledge should have a single representation. Hunt-Thomas Pragmatic Programmer Ch. 2, p. 27: "EVERY PIECE OF KNOWLEDGE MUST HAVE A SINGLE, UNAMBIGUOUS, AUTHORITATIVE REPRESENTATION WITHIN A SYSTEM. DRY — Don't Repeat Yourself." [src:hunt-thomas-pragmatic-programmer-2019.md:lines 1220-1233]

**Applied.** Foundation Part 3 (Knowledge Base) enforces SPOT structurally: the wiki is the single authoritative KB; `raw/` is the archive of originals; `decisions/` is the locked policy record. The same fact does not live in the wiki AND in a strategies.md AND in CLAUDE.md — it lives in one place and is referenced from others. The 393-book library is `raw/books-md/` — not duplicated into `wiki/` entries until the `/ingest` skill transforms and attributes them. The provenance chain (`sources:` frontmatter + `[src:]` inline citations) is the mechanism that lets the same underlying source feed multiple wiki entries without creating duplicate authoritative representations.

DRY violation detection in Foundation context: if the same architectural decision appears in `decisions/D-N.md` AND verbatim in `CLAUDE.md` AND in a `strategies.md` entry, that is a DRY violation — one of them is stale. The `decisions/` lock is the authoritative copy; the others should reference it.

**Tradeoff'd.** Strict SPOT creates a lookup tax: to understand a claim, you must follow the reference chain. Foundation accepts this tax because the alternative (repeated copies drifting apart) is worse at scale. The tradeoff point: when reference chains exceed 3 hops, readability suffers. Foundation's current design is 2-hop max (wiki entry → decisions/ lock → FUNDAMENTAL §N). If chains grow to 4+ hops, consider a summary layer.

---

### Principle 5 — Simplicity first; prototype before polishing; worse-is-better (Rule of Simplicity + Rule of Optimization)

**Sourced.** Raymond AoUP Ch. 1, p. 39: "Design for simplicity; add complexity only where you must... The notion of 'intricate and beautiful complexities' is almost an oxymoron. Unix programmers vie with each other for 'simple and beautiful' honors." And Rule of Optimization, p. 46: "Prototype before polishing. Get it working before you optimize it." The "worse-is-better" argument (Richard Gabriel, cited in Raymond Ch. 2): an 80% solution that ships beats a 100% solution that is always six months away. [src:raymond-art-of-unix-programming-2003.md:Ch.1 lines 1019-1041]

**Applied.** Foundation's Phase 1 posture is explicitly simplicity-first: voice pipeline uses Python subprocesses rather than a proper job-queue system (no Redis, no Celery); wiki KB is Markdown + YAML rather than a proper graph database (no Neo4j, no Postgres); agent coordination is file-based mailboxes rather than a proper message broker. Each of these is a deliberate "worse-is-better" choice: the simple solution works today and can be replaced cleanly (because interfaces are plain text) when the appetite justifies the upgrade. The STOP gate is a prototype-before-polishing decision: human review is the simplest correct implementation of "human in the loop," cheaper to build and more reliable than any AI-automated equivalent at Phase 1 scale.

**Tradeoff'd.** Simplicity-first creates a refactor-at-scale risk. When voice items grow from 151 (current) to 15 000, the Python subprocess pipeline without job queuing will saturate. The antifragility check: Foundation's staged-pipeline design means the transition from subprocess to job-queue is a swap of one component (`run_pipeline.sh`) without touching the data format or the per-stage scripts. Simplicity-first is safe here because the interfaces are clean. If the inter-stage interfaces were not plain files, the refactor at scale would be expensive. This is why the Unix principle of text-as-interface is a prerequisite for responsibly applying worse-is-better.

---

### Principle 6 — Transparency and silence (Rule of Transparency + Rule of Silence)

**Sourced.** Raymond AoUP Ch. 1, p. 40-43: "Rule of Transparency: Design for visibility to make inspection and debugging easier... Rule of Silence: When a program has nothing surprising to say, it should say nothing." And Ch. 6 (Transparency, pp. 159-186): "A program that produces output only when something interesting happens is one you can wire into pipelines without worrying about what it will say." [src:raymond-art-of-unix-programming-2003.md:Ch.1 lines 923-937]

**Applied.** Foundation's git commit discipline is a transparency artifact: `[area] verb what (why)` — every state change is visible, human-readable, queryable. `/company-status` produces a ≤80-line snapshot, not a 3000-line dump — silence for the uninteresting, signal for the important. The `review_report.py` script produces a markdown report only when there are items worth reviewing; when `filter.py` finds nothing to surface, the report is minimal. Claude Code hooks log warnings (log-only mode, cycle 2) without blocking operation — silent when correct, noisy when failing. This is the Rule of Silence applied to a multi-agent OS.

**Tradeoff'd.** Transparency (verbose git history, detailed cycle logs) conflicts with cognitive load: a founder reading 406 commits per week cannot absorb all of them. Foundation resolves this with `/company-status` and `/knowledge-diff` — compressed views that surface signal over noise. The tradeoff is that compressed views can obscure anomalies. Mitigation: `/lint` runs health checks that surface structural anomalies, restoring transparency on demand.

---

## §5 Tradeoffs to Surface Explicitly

### T1 — Unix plain text vs Foundation structured YAML/JSON

Unix purists: data should be newline-delimited text; any parser is a dependency. Foundation chose YAML/JSON for typed safety and provenance fields. **Resolution:** Foundation's choice is justified by D28 (anchor-mandatory ingestion) and provenance requirements. The Unix principle is honored at the level of "everything is a file on disk" — the format evolution from raw text to structured text is a legitimate extension, not a violation. Observable test: can you `grep` and `diff` all Foundation data files? Yes. That is the Unix transparency invariant, and it holds.

### T2 — "Everything is a file" vs "Everything is a git commit"

Unix: the filesystem is the universal namespace. Foundation: git history is the universal audit trail. **Resolution:** not a conflict — git IS a filesystem discipline with version history added. Foundation extends the Unix "file as universal interface" with the dimension of time (commit = file state at moment T). The invariant is the same: no ephemeral state, no in-memory-only state, no state that cannot be inspected by a human reading a file. Foundation's git discipline is "Unix philosophy + provenance."

### T3 — Unix "do one thing well" vs Cognition "Don't Build Multi-Agents"

Both endorse single-purpose components. Unix applies this at the program/tool level; Cognition applies this at the orchestrator level (don't build a multi-agent system when a single prompt works). **Resolution:** same principle, different scope. Foundation's answer: each tool in the pipeline does one thing (Unix); the orchestrator (brigadier) does one thing (coordinate); the swarm exists only where the task genuinely exceeds single-agent scope. The principle is consistent — do not add agents for the sake of adding agents any more than you add scripts for the sake of adding scripts.

### T4 — Simplicity (worse-is-better) vs Левенчук's "100% framework foundation studied"

Unix endorses shipping an 80% solution that works over a 100% solution that is always six months away. Левенчук's constitutional rigor demands that the foundation be studied at full depth before the system is designed on top of it. **Resolution:** these operate at different layers. Foundation is being studied at full depth (this card is part of that process) before materializing into Wave C parts. The simplicity principle governs the materialised implementation, not the design rigor. "Study the foundation rigorously; implement it simply" — no conflict when scoped correctly. The dissent is: if the 100%-studied foundation turns out to demand architectural complexity, simplicity-first may produce a wrong implementation. Mitigation: the AWAITING-APPROVAL gate (Part 6) exists precisely to catch this — the foundation informs the gate, not the other way around.

### T5 — Separation-of-policy vs single-file readability

Unix separation of policy from mechanism creates indirection (two files to understand one behavior). For a founder working alone at 2am, reading two files is slower than reading one. **Resolution:** this is a real cost at Phase 1 scale, manageable because: (a) role manifests are short (<200 lines each), (b) `/company-status` gives the operational view without requiring the role files. The cost grows if role manifests proliferate without /lint checking for orphan or contradictory definitions. `/lint` is the mechanism that keeps the indirection manageable.

---

## §6 Anti-scope

- **Specific Unix tooling** — sed, awk, grep, make. Foundation uses Python tools, not Unix shell scripts. The philosophy is portable; the specific tools are not.
- **Distributed systems / network stack** — Unix's network programming (TCP/IP, socket programming, IPC across machines). Foundation is single-node Phase 1.
- **Linux kernel internals** — process scheduling, filesystem internals, device drivers.
- **Binary format design** — Foundation does not produce binary artifacts; this chapter of AoUP is irrelevant.
- **GUI design under Unix** — X11 architecture, toolkit choices. Foundation has no GUI layer.

---

## §7 Open Questions

1. **Kernighan-Pike gap.** The KP book is fully absent from the library (images only). Raymond's citations cover the KP philosophy adequately, but the KP book's practical examples (shell pipelines as composition tools, the `who | sort | uniq -c` style of tool chaining) are not recoverable from disk. If Wave C materialisation needs to cite KP directly (e.g. for a Foundation Part 2 shell composition example), a web source will be needed. Flagged for brigadier.

2. **Orthogonality formal definition.** Hunt-Thomas orthogonality chapter (p. 34, referenced but not read in this session — the read offset reached DRY at line 1395 but orthogonality starts at line 1395 which is the next section). The orthogonality principle states that components should be independent: a change in one should not require changes in another. This is the formal statement of the Unix composability principle. Needs a dedicated read to cite the exact definition. Flagged for brigadier as a low-priority supplement.

3. **Voice pipeline 10× antifragility.** At 15 000 voice items/day (10× current ~151 items over the observed period), will the Python subprocess pipeline remain viable? Unix principle says: if the interfaces are clean, the substitution is cheap. But the STOP gate — requiring human review of each batch — becomes a bottleneck at 10× scale regardless of pipeline speed. This is not a Unix-philosophy design failure; it is a policy decision (human review is mandatory). Foundation should document the gate-volume tolerance explicitly as a part of Part 2's scalability spec.

---

## §8 Compound Step — Candidate strategies.md Entries

Three candidate rules surfaced in this card for `agents/engineering-expert/strategies.md`:

1. `unix-text-interface-as-antifragility-prerequisite` — "Simplicity-first (worse-is-better) is only safe when inter-stage interfaces are plain files. If interfaces are not plain files, simplicity-first creates a refactor trap. Check interface format before approving a 'we'll fix it later' architectural decision."

2. `policy-mechanism-separation-test` — "For any proposed Foundation component, apply the separation test: can I change the policy without touching the mechanism, and vice versa? If not, the component is conflating policy and mechanism. Refuse the design until they separate."

3. `dry-violation-detection-in-knowledge-base` — "If the same architectural decision appears verbatim in ≥2 of {decisions/, CLAUDE.md, strategies.md, wiki/foundations/}, that is a DRY violation. The decisions/ lock is authoritative; the others should reference it. Flag in /lint output."
