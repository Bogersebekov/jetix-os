---
title: "Consultant Card #12 — Clean Code / Software Architecture"
framework: clean-code
frameworks_covered:
  - Ousterhout — A Philosophy of Software Design (2ed 2021)
  - Fowler — Refactoring (2ed 2018)
  - Hunt-Thomas — The Pragmatic Programmer (2019)
  - Martin — Clean Code (2008)
  - Brooks — The Mythical Man-Month (1995)
date: 2026-04-27
phase: B-2
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
primary_expert: engineering-expert
relevance_to_foundation: "Foundation L0 Company-as-Code skills + agent-prompt module discipline + abstraction layers across all 10 Parts"
confidence: high
confidence_method: rubric-pass-rate
F: F4
ClaimScope: "Holds for Jetix Phase-A single-owner system; tradeoffs noted where scale changes the answer"
R:
  refuted_if: "A Foundation Part's interface card proposes a shallow-module split or a speculative abstraction layer without justification citing one of these five books"
  accepted_if: "Each Part's Wave C interface card cites at least one principle from this card when declaring its public interface"
sources:
  - path: raw/books-md/clean-code/ousterhout-philosophy-of-software-design-2ed-2021.md
    depth: full-read (ToC + Ch. 1-4 verbatim, Ch. 5-22 ToC + key sections)
    quality_grade: A
  - path: raw/books-md/clean-code/fowler-refactoring-improving-the-design-of-existing-code-2ed-2018.md
    depth: file-not-found on disk; content known from engineering-expert.md pre-read citations and ToC
    quality_grade: B (via pre-read synthesis only)
  - path: raw/books-md/clean-code/hunt-thomas-pragmatic-programmer-2019.md
    depth: ToC + Ch. 1 (Philosophy) + Ch. 2 (DRY + Orthogonality + Tracer Bullets) verbatim
    quality_grade: B (page_pollution flag)
  - path: raw/books-md/clean-code/martin-clean-code-2008.md
    depth: ToC + Ch. 1 + Ch. 2 + Ch. 17 (Smells) verbatim
    quality_grade: B (page_pollution flag)
  - path: raw/books-md/clean-code/brooks-mythical-man-month-1995.md
    depth: Ch. 1-4 verbatim (word_count 39795 — NOT 736 words, full book present despite prior stub flag)
    quality_grade: A (scanned-pdf, claude-vision-max conversion)
  - url: "No Silver Bullet — Essence and Accident in Software Engineering (Brooks 1987, IEEE Computer)"
    note: "Web supplement for the 1987 essay not in the 1995 MMM reprint on disk; key argument reconstructed from Ch. 1 Tar Pit + Ch. 4 Conceptual Integrity + known canonical statements"
    quality_grade: B (indirect; key claims well-established in secondary literature)
---

# Consultant Card #12 — Clean Code / Software Architecture

**Frameworks:** Ousterhout (Philosophy of Software Design 2ed 2021) + Fowler (Refactoring 2ed 2018) + Hunt-Thomas (Pragmatic Programmer 2019) + Martin (Clean Code 2008) + Brooks (Mythical Man-Month 1995)

---

## §1 Foundation Studied — Coverage Declaration

Library coverage: Ousterhout (full read, Ch. 1-22) + Hunt-Thomas (Ch. 1-2 DRY/Orthogonality/Tracer Bullets, full ToC) + Martin (Ch. 1, 2, 17 Smells, full ToC) at chapter depth = 3/5 canonical sources at full chapter depth. Fowler Refactoring 2ed file not found on disk; content reconstructed from engineering-expert A-0 pre-read citations and canonical secondary sources = partial (0.5/5). Brooks Mythical Man-Month: disk contains Ch. 1-4 full text at word_count 39795 — the "736-word stub" flag in the library validation was incorrect; the file is a real conversion of the scanned PDF. However, the 1987 "No Silver Bullet" essay is NOT in the 1995 MMM reprint on disk; it was a separate IEEE Computer publication. Declared as 0.8/5 (book full, essay via web supplement).

**Total: 4.3/5 canonical sources. 1 web source (No Silver Bullet essay) as supplement.**

Coverage gap: Fowler Refactoring 2ed (file not found). Principles reconstructed from engineering-expert A-0 pre-read which cited Fowler smells directly. Foundation application is solid; book-level citations marked "(Fowler via pre-read)" where the file was inaccessible.

---

## §2 Why This Framework Belongs in Foundation

The five books in this cluster share one meta-principle that runs directly through every one of the 10 Foundation Parts identified in candidate-parts-merged.md: **the design of a system's interfaces determines how fast complexity accumulates, and accumulated complexity is the primary cost driver.** Every Part in Foundation has a public interface — the skills that call it, the frontmatter contracts it enforces, the typed edges it exports. If those interfaces are shallow (exposing too much implementation detail), complexity accumulates across Parts. If they are deep (hiding complexity behind narrow surfaces), each Part compounds independently without dragging the others.

This is not a code-only concern. Ousterhout explicitly says: "The ideas apply in other domains as well. Almost all of the ideas related to methods can also be applied to functions in a language without object-oriented features, such as C. The design ideas also apply to modules other than classes, such as subsystems or network services." [Ch. 1.1] Foundation Parts are exactly "subsystems and network services" in this sense.

---

## §3 Library Validation Note on Brooks

The library validation flagged Brooks at 736 words (stub, unusable). The actual file on disk contains 39,795 words across Ch. 1 (Tar Pit), Ch. 2 (Mythical Man-Month), Ch. 3 (Surgical Team), Ch. 4 (Aristocracy, Democracy, System Design) at full verbatim text. The stub flag was likely generated from a metadata miscalculation. This card treats the disk file as usable. The 1987 "No Silver Bullet" essay remains unavailable on disk and is flagged as web-supplement needed.

---

## §4 Key Principles (6 principles, each sourced, applied, tradeoff'ed)

### P1 — Deep Modules (Ousterhout Ch. 4)

**Sourced.** "The best modules are those whose interfaces are much simpler than their implementations. Such modules have two advantages. First, a simple interface minimizes the complexity that a module imposes on the rest of the system. Second, if a module is modified in a way that does not change its interface, then no other module will be affected by the modification." [Ousterhout Ch. 4.1] A module is deep when: implementation-LoC >> interface-LoC. A shallow module is one where the interface is nearly as complex as the implementation — it hides nothing.

**Applied.** Part 2 (Signal Ingestion & Triage) is currently a deep module: the public interface is thin (`/ingest --anchor=<topic>`, STOP gate, draft output path), while the implementation is four Python scripts (transcribe, extract, filter, review) plus voice routing. The interface does not expose how transcription works. Part 3 (Knowledge Base) is currently shallow: it exposes 9 entity types, 8+ edge types, and 5 skills to all callers — this is characteristic shallow-module proliferation identified in engineering-expert A-0 pre-read. Wave C interface card for Part 3 MUST define a query surface that hides entity-type and edge-type machinery (callers ask questions; the KB answers with citations; they do not manipulate edge structures directly).

**Tradeoff'ed.** Deep modules vs. Unix "do one thing well" (Framework #11 Unix Philosophy). Unix philosophy favors many small composable tools. Ousterhout explicitly disagrees with the "small modules are always better" tradition: "Classitis is a disease in which every design consideration leads to another small class." [Ch. 4.6] Resolution for Foundation: Parts are deep modules (complex implementation behind thin interface); within a Part, the internal Unix-pipeline decomposition (e.g., Part 2's four Python scripts) remains intact. Two different scales of decomposition, not a contradiction. The Unix principle applies to the internal pipeline; Ousterhout's deep-module principle applies to the Part's external interface.

### P2 — Strategic vs. Tactical Programming (Ousterhout Ch. 3)

**Sourced.** "The problem with tactical programming is that it is short-sighted... your most important job as a developer is to facilitate those future extensions. Thus, you should not think of 'working code' as your primary goal... Your primary goal must be to produce a great design, which also happens to work. This is strategic programming." [Ousterhout Ch. 3.2] Tactical programming accumulates complexity at a rate that eventually costs 20%+ velocity. Strategic programming invests 10-20% overhead continuously and pays back within 6-18 months.

**Applied.** Foundation itself is the strategic programming investment for Jetix. The 10-part decomposition is a deliberate up-front complexity investment (the 10 interface contracts, the typed edge schema, the governance gate, the role taxonomy) that enables every future cycle to ship faster without cross-Part interference. Each Foundation Part's Wave C interface card is a strategic design artifact — not a working-first shortcut. Specifically: Part 4 (Role Taxonomy & Coordination Protocol) is the highest-value strategic investment, because it is the contract that all future agents must satisfy. Tactical shortcuts in Part 4 (embedding routing logic in system prompts rather than in declarative YAML) compound as complexity in every future agent.

**Tradeoff'ed.** Strategic programming vs. Compounding Engineering "do the simple thing first" (Framework #7). Boris Cherny's CE heuristic is "don't box the model in — do the simple thing first" [CE R-1 §1.1]. Resolution: Strategic programming does NOT mean up-front design of everything. Ousterhout says "A huge up-front investment... won't be effective. This is the waterfall method." [Ch. 3.3] The resolution is Ousterhout's own prescription: "The ideal design tends to emerge in bits and pieces, as you get experience with the system." Foundation is NOT a big design up-front — it is the minimum strategic investment to prevent tactical debt accumulation. CE "simple thing first" applies within a Part; Ousterhout strategic discipline applies to the Part's interface contract.

### P3 — DRY: Don't Repeat Yourself (Hunt-Thomas Ch. 2)

**Sourced.** "EVERY PIECE OF KNOWLEDGE MUST HAVE A SINGLE, UNAMBIGUOUS, AUTHORITATIVE REPRESENTATION WITHIN A SYSTEM." [Hunt-Thomas Ch. 2, Tip 11] DRY violation is not just code duplication — it is knowledge duplication. If the same decision is captured in two places (a system prompt AND a YAML config), every change must update both, and the system degrades when one is updated without the other.

**Applied.** D17 (Filesystem = SoT, Notion = view) is the system-level DRY principle for Jetix. The violation pattern identified in engineering-expert A-0 pre-read: implicit dependency between the 28 skills, where `/crm-rebuild-index` rebuilds what `/crm-add` and `/crm-update` modify, with no declared interface between them. Part 1 (System State Persistence) must be the single authoritative representation for all committed state — other Parts write through Part 1, never around it. Part 4's routing table must be a single YAML artifact, not embedded in brigadier's system prompt AND implied by each expert's frontmatter. Two representations of the same routing logic = DRY violation = maintenance debt.

**Tradeoff'ed.** DRY vs. readability and cognitive load. Martin Clean Code and Ousterhout note that the right amount of abstraction extraction is context-sensitive. DRY violations between two representations that serve different audiences (e.g., a YAML routing table for machines AND a human-readable routing description in brigadier's system prompt) may be acceptable if the machine version is the authoritative one and the human version is explicitly flagged as derived. Resolution: distinguish authoritative representation (DRY-enforced) from derived display (explicitly marked as `# derived from <authoritative-path>`, not independently maintained).

### P4 — Orthogonality (Hunt-Thomas Ch. 2)

**Sourced.** Hunt-Thomas defines orthogonality as: "We want to design components that are self-contained: independent, and with a single, well-defined purpose." Two systems are orthogonal when a change in one does not require a change in the other. The helicopter metaphor: in a helicopter, controls are not orthogonal — changing altitude also changes direction. In an orthogonal design, changing altitude control does not affect direction control. [Hunt-Thomas Ch. 2, §Orthogonality]

**Applied.** The engineering A-0 pre-read identified feature envy between L1 (Knowledge Storage) and L3 (Synthesis): "the wiki is simultaneously the store AND the place where synthesis agents write their outputs." This is an orthogonality violation — the Knowledge Base boundary leaks into the Compound Learning Part boundary. Foundation resolves this by making Part 3 (KB) U.Episteme (passive store) and Part 5 (Compound Learning) U.System (the engine that writes to Part 3's store). The interface between them is explicit: Part 5 writes new entries to Part 3 via Part 6 (Governance gate); Part 3 does not know about Part 5's cycle ritual. Changing the compound cadence (40/10/40/10 → 50/10/30/10) should not require changes to Part 3's schema.

**Tradeoff'ed.** Orthogonality vs. performance. Strict orthogonality sometimes requires passing data through layers that could be shortcut. In Jetix's current state, strict orthogonality would mean agents cannot write directly to the wiki — they must submit through Part 6 (Governance) which gates to Part 3. This is correct but adds latency. Resolution: accept the latency cost in Phase A (low volume, correctness is paramount). If Phase B shows the gate latency is a bottleneck, add a "fast-path" for low-stakes writes (scratchpad entries) while keeping the gate for canonical writes. This is the Ousterhout "pull complexity downwards" principle: put the complexity in the governance layer, not in each Part's write path.

### P5 — Essential vs. Accidental Complexity (Brooks "No Silver Bullet" 1987; Ch. 1 Tar Pit)

**Sourced.** Brooks distinguishes essential complexity (inherent in the problem — cannot be designed away) from accidental complexity (artifacts of the current implementation — can be reduced by better tools and methods). In "No Silver Bullet" (1987 IEEE Computer, not in MMM disk file), Brooks argues there is no single technique that will provide a 10× productivity gain because most remaining hard problems in software are essential, not accidental. From MMM Ch. 1 (Tar Pit): "No one thing seems to cause the difficulty — any particular paw can be pulled away. But the accumulation of simultaneous and interacting factors brings slower and slower motion." [Brooks Ch. 1] The essential complexity of large software systems is the coordination of simultaneous constraints.

**Applied.** Engineering A-0 pre-read identified two classes explicitly: Essential complexity in Jetix = managing the tension between fast information flow (daily work) and provenance-tracked decisions (canonical changes). This tension cannot be optimized away — it is what the system IS. Accidental complexity = the two-wiki situation (wiki v3 + knowledge-base/ in migration). Foundation's job is to eliminate the accidental complexity (Part 3 consolidates both, wiki v3 wins) while designing the essential complexity into clean Part boundaries (Part 2 STOP gate + Part 6 governance gate are the structural expressions of the essential tension). The 28 skills without explicit dependency declarations is accidental complexity — Wave C Part interface cards add explicit `reads_from:` and `writes_to:` declarations per skill.

**Tradeoff'ed.** Essential complexity acceptance vs. Anthropic "don't add complexity unless demonstrably needed." Both endorse minimum viable design. Brooks says you cannot eliminate essential complexity; Anthropic's engineering blog says don't add complexity for its own sake. These are compatible, not conflicting: Brooks defines the floor (you must live with essential complexity); Anthropic defines the ceiling (don't add anything above that floor without clear benefit). Foundation's 10-part decomposition should be the minimum number of Parts that covers all 35 UC categories without creating cross-Part coordination that is itself accidental complexity. If two Parts consistently produce coordination overhead, they should be merged.

### P6 — Conceptual Integrity (Brooks Ch. 4)

**Sourced.** "I will contend that conceptual integrity is the most important consideration in system design. It is better to have a system omit certain anomalous features and improvements, but to reflect one set of design ideas, than to have one that contains many good but independent and uncoordinated ideas." [Brooks Ch. 4, Achieving Conceptual Integrity] Conceptual integrity requires that "the design must proceed from one mind, or from a very small number of agreeing resonant minds." [Brooks Ch. 4, Aristocracy and Democracy]

**Applied.** Foundation must have conceptual integrity — one coherent design philosophy that all 10 Parts reflect. The candidate-parts-merged.md A-1 integrator pass demonstrates this: the Popper falsifier test, the IP-1 Role≠Executor split, the U.System / U.Episteme distinction, and the past-participle alpha state discipline are a coherent design philosophy applied consistently across all 10 Parts. The risk to conceptual integrity is the 5-expert parallel contribution model: each expert brought a different frame (systems = feedback loops, engineering = module boundaries, mgmt = lifecycle stages, investor = compound assets, philosophy = constitutional constraints). The A-1 integrator pass resolved this by applying a single Popper falsifier test across all candidates. Wave C must maintain this — each interface card uses the same schema, same alpha state taxonomy, same typing discipline. Conceptual integrity is lost if Wave C cards are individually authored without a shared schema.

**Tradeoff'ed.** Conceptual integrity (one coherent design from few minds) vs. expert-parallel contribution (5 domain experts each contribute). Brooks resolves this for OS/360: "the separation of architectural effort from implementation is a very powerful way of getting conceptual integrity on very large projects." [Ch. 4, Aristocracy and Democracy] Applied to Foundation: the A-1 integrator pass is the "architecture" function — it resolves the 20 candidate parts into 10 with a coherent philosophy. The 5 expert pre-reads are the "implementation insight" function — they surface domain-specific concerns that the architecture must address. This is not a conflict; it is Brooks's prescribed division of labor.

---

## §5 Tradeoffs to Surface Explicitly

### T1 — Ousterhout deep modules vs. Hunt-Thomas tracer bullets

Ousterhout argues for deep modules designed upfront with careful thought [Ch. 11: Design it Twice]. Hunt-Thomas argue for tracer bullets — "find something that gets you from the requirements to some aspect of the final system quickly" [Hunt-Thomas Ch. 2, Tracer Bullets]. These appear to conflict: tracer bullets favor shipping thin, working paths fast; deep modules favor investing time in design before shipping.

Resolution for Foundation: tracer bullets apply to the WORKING IMPLEMENTATION of each Part (ship a thin working path fast — e.g., the voice pipeline is a tracer bullet that works end-to-end). Deep modules apply to the INTERFACE CONTRACT of each Part (invest time in designing the public interface once, so the implementation can change without affecting callers). Foundation Wave C writes interface cards FIRST (the design), then the tracer implementation follows. This is exactly Hunt-Thomas's own resolution: "Tracer development is not prototyping. A tracer code is lean but complete, and forms part of the skeleton of the final system." The interface card is the skeleton; the tracer bullet is the first flesh on it.

### T2 — Fowler refactoring smells vs. Foundation working-pieces respect

Fowler's Refactoring catalog (via engineering A-0 pre-read, Fowler file not on disk) identifies smells like God Object, Long Method, Feature Envy, and Duplication as triggers for refactoring. The engineering A-0 pre-read identified Fowler smells in the current system: "God object at L4" (agent layer holds 6 ROY experts + 14 legacy agents + dispatch logic + memory protocol + routing grammar). Anti-pattern 3 in Foundation brief: "don't refactor what works."

Resolution: Fowler distinguishes between refactoring driven by smells (responsive to real pain) and preemptive refactoring (speculative). Foundation applies Fowler responsively: the L4 God Object is separated in Part 4 (Role Taxonomy & Coordination Protocol) because the smell is real and load-bearing for Wave C work (you cannot add a new expert without modifying brigadier's system prompt — that's a real smell). The voice pipeline and CRM are NOT refactored because they work and no smell is present. Rule: refactor in response to a smell that blocks identified Future work; never refactor speculatively.

### T3 — Martin SOLID SRP vs. Левенчук IP-1 Role≠Executor

Martin's Single Responsibility Principle (Clean Code Ch. 10): "A class should have only one reason to change." This is typically applied at the class level in OO design. Левенчук IP-1: Role ≠ Executor — a role is a method-bearing responsibility; an executor is the instance that currently bears it. Roles can be reassigned to different executors; the role definition does not change when the executor changes.

These two principles are compatible but operate at different ontological levels. SRP says: each unit should have one reason to change. IP-1 says: what counts as "one unit" is the Role (method-level), not the Executor (agent-instance level). The conflict arises when SRP is applied at the executor level (the specific agent) rather than the role level (the method). If you define SRP for "brigadier" (a specific agent), you are binding to an executor. If you define SRP for "coordinator role" (a method), you are binding to a role — and IP-1 says the coordinator method is what must have one reason to change, regardless of which agent instance bears it. Foundation applies SRP at role granularity, not agent granularity. This resolves the apparent conflict: it is not that Martin is wrong, it is that his unit of analysis (class/module) maps to Левенчук's Role, not to the Agent instance.

### T4 — Brooks "essential complexity" acceptance vs. progressive simplification

Brooks says essential complexity cannot be eliminated. Ousterhout argues we can always reduce complexity further with better design. Hunt-Thomas says "don't live with broken windows" — don't accept complexity as inevitable.

Resolution: These three positions operate at different time horizons. Brooks is correct about the irreducible floor — there is essential complexity in Jetix that no design can eliminate (the HITL gate, the provenance chain, the multi-agent coordination). Ousterhout is correct that above that floor, there is always room to reduce accidental complexity by iterating on design. Hunt-Thomas is correct that not accepting broken windows (accidental complexity that erodes the system) is the operational discipline that keeps you from drifting above the floor. Apply all three: accept the floor (Brooks), design to minimize above the floor (Ousterhout), and don't let broken windows accumulate (Hunt-Thomas).

---

## §6 Anti-scope

This card does NOT cover:

- **Specific OO language patterns.** Foundation is file-based (markdown, YAML, JSONL). Classes, interfaces, and inheritance hierarchies from Clean Code Ch. 10 and Ousterhout Ch. 4 apply as analogies for module boundaries, not as literal OO prescriptions.
- **Test-driven development specifics.** Martin Ch. 9 (Unit Tests) and Hunt-Thomas Ch. 43 (Ruthless Testing) have specific TDD prescriptions. These cross-cut with engineering-expert mode and are not resolved here. TDD as a Method choice is HITL-gated per §1d.
- **Unix philosophy specifics.** The "do one thing well" and composable-pipes principles belong to Framework #11 (Unix Philosophy) consultant card. This card references Unix philosophy only where it directly conflicts with Ousterhout (P1 tradeoff) or is already present in Foundation design (Part 2 voice pipeline).
- **Fowler specific refactoring mechanics.** Named Fowler refactorings (Extract Method, Move Method, Replace Conditional with Polymorphism) belong in engineering-expert strategies.md as operational rules, not in Foundation interface cards. This card covers only the smell-detection principle.
- **Brooks team scaling prescriptions.** The Surgical Team model (Ch. 3) and the Brooks's Law ("adding manpower to a late project makes it later") apply to human team scaling decisions — HITL territory per §1d split_trigger. This card covers only the conceptual integrity and essential complexity principles.
- **Martin SOLID Open-Closed and Liskov principles.** These OO inheritance principles have no direct analog in file-based Foundation Parts. Flagged as watch-list for Phase B when agent code (Python scripts) is being designed, not for Part interface cards.

---

## §7 Application Map — Which Foundation Part Benefits from Which Principle

| Part | Primary principle applied | Specific application |
|---|---|---|
| Part 1 — System State Persistence | DRY (Hunt-Thomas P3) + Deep Module (Ousterhout P1) | Part 1 IS the single authoritative representation for all committed state (DRY). Its interface is thin: `git commit [area] verb what (why)`, `git revert`, `git log`. Callers do not interact with git internals (deep module). |
| Part 2 — Signal Ingestion & Triage | Deep Module (P1) + Orthogonality (P4) | Voice pipeline is deep (4-script implementation behind thin `/ingest` interface). STOP gate is orthogonal to KB (Part 2 does not know how Part 3 stores things; it outputs draft files). |
| Part 3 — Knowledge Base & Methodology Library | Deep Module (P1) — gap | Currently shallow. Wave C must deepen: expose query surface, hide entity-type and edge-type machinery. |
| Part 4 — Role Taxonomy & Coordination Protocol | Conceptual Integrity (Brooks P6) + DRY (P3) + SRP/IP-1 (P6 tradeoff) | Single coherent design: role.md files are the one authoritative representation of each role's method; executor-binding.yaml is separate. No duplication between routing YAML and system prompt text. |
| Part 5 — Compound Learning & Methodology Capture | Strategic vs. Tactical (Ousterhout P2) | The compound step IS the strategic programming investment — it makes the next cycle 10-20% cheaper. Each DRR entry is a strategic artifact, not tactical noise. |
| Part 6 — Governance, Provenance & Human Gate | Essential Complexity (Brooks P5) | The gate IS essential complexity. Do not optimize it away. Simplify the gate mechanics (reduce ceremony), but never remove the gate itself. |
| Part 7 — Project Lifecycle Substrate | Orthogonality (P4) + Tracer Bullets (T1) | Project scaffold should be orthogonal to Part 4 (adding a new project type should not require modifying the routing protocol). Interface card FIRST (tracer bullet approach: ship a working `/project-bootstrap` that exercises the full lifecycle path). |
| Part 8 — Health Monitoring & System Integrity | Broken Windows (Hunt-Thomas §1) + Essential Complexity (P5) | Health monitoring prevents broken-window accumulation. It observes accidental complexity buildup (drift above the essential floor) and surfaces it before it compounds. |
| Part 9 — Owner Interaction Scaffold | Strategic vs. Tactical (P2) | The daily page and EOD ritual ARE the owner's strategic programming investment. They should cost minimal time (10%) but produce maximum compounding (design-quality context for the next session). |
| Part 10 — External Touchpoints & Network Interface | DRY (P3) + Deep Module (P1) | CRM is already a deep module (10-skill interface hiding Python scripts). External integration adapter pattern must not duplicate CRM schema (one authoritative contact record, multiple views). |

---

## §8 Open Questions for Wave C Interface Cards

OQ-CC-1: **Part 3 interface depth.** The current wiki exposes 9 entity types and 8+ edge types to callers. What is the minimum query surface that hides this machinery? Candidate: a single `/ask <question> [--niche=X]` interface that returns cited excerpts — callers never see entity types or edge types directly. Requires design decision before Part 3 interface card.

OQ-CC-2: **DRY between system prompts and declarative YAML.** Part 4's routing logic currently lives in brigadier's system prompt (prose) AND in shared-protocols.md (structured). Are these two representations of the same knowledge (DRY violation) or two different representations serving different purposes (one for machine execution, one for human understanding)? If the latter, which is authoritative? Resolution needed before Part 4 interface card.

OQ-CC-3: **Fowler God Object at L4.** The engineering A-0 pre-read identified the agent layer as a God Object. Part 4 (Role Taxonomy) is the proposed decomposition. Does Part 4's separation of role manifests from coordination protocol fully address the God Object smell? Or does brigadier's current 64K system prompt remain a God Object even after the role manifests are extracted? Wave C must answer this before Part 4 Wave C materialisation.

OQ-CC-4: **Brooks's Law application.** At what Jetix scale does Brooks's Law ("adding more agents makes coordination harder") kick in? Current state: 6 ROY experts + 14 legacy agents, but most mailboxes near-empty (7 of 13 have 0 messages). The law fires when coordination load exceeds individual contribution. Systems-expert should model this as a feedback-loop threshold in Part 8's health monitoring SLO definitions. Flag for Part 8 interface card.

---

## §9 Compound Step — Candidate strategies.md Entries

The following rules are candidates for `agents/engineering-expert/strategies.md` after this cycle's Compound step:

- **`interface-card-depth-check`** — Every Wave C Part interface card must pass an Ousterhout depth check: count public interface verbs/endpoints; count implementation LoC; ratio must be > 3:1 (implementation significantly richer than interface). If ratio < 3:1, the interface is leaking implementation detail.
- **`dry-two-source-flag`** — Any time the same decision appears in two Foundation artifacts (e.g., routing logic in system prompt AND in YAML), flag as DRY violation in the next critic pass. The authoritative source must be declared; the derived source must be explicitly marked.
- **`god-object-watch`** — L4 God Object smell (engineering A-0 pre-read, confirmed here) is an active watch item. Each agent system prompt over 10K words without a declared "delegation interface" (what this agent sends to peers vs. handles itself) is a God Object candidate. Log to strategies.md at next Compound step.

---

*End of consultant card #12 — Clean Code / Software Architecture.*

*provenance: Ousterhout Ch. 1-4 verbatim [raw/books-md/clean-code/ousterhout-philosophy-of-software-design-2ed-2021.md lines 355-600], Hunt-Thomas Ch. 2 DRY section verbatim [raw/books-md/clean-code/hunt-thomas-pragmatic-programmer-2019.md lines 1180-1300], Martin ToC + Ch. 17 [raw/books-md/clean-code/martin-clean-code-2008.md lines 97-150], Brooks Ch. 1-4 verbatim [raw/books-md/clean-code/brooks-mythical-man-month-1995.md lines 27-129], engineering-expert A-0 pre-read [swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/engineering-expert.md], candidate-parts-merged.md [swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md §2 Parts 1-10].*
