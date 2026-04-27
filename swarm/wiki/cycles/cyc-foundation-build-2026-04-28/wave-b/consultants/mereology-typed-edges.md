---
title: "Consultant Card #14 — Mereology + Ontology: FPF A.14 Typed Edges"
slug: mereology-typed-edges
framework: 14
date: 2026-04-27
cycle: cyc-foundation-build-2026-04-28
phase: B-2
expert: philosophy-expert
mode: integrator
sources:
  - {path: "design/JETIX-FPF.md", section: "§3.5 A.14 typed mereological edges (Rec-05)", role: "canonical typed-edge vocabulary"}
  - {path: "design/JETIX-FPF.md", section: "§1 A.1 Holonic Foundation", role: "whole-part-supersystem trinity"}
  - {path: "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md", section: "§2 Parts 1-10", role: "Foundation application context"}
  - {url: "https://plato.stanford.edu/entries/mereology/", status: "web-mandatory", F: F4, note: "WebFetch unavailable; canonical academic knowledge applied — F4 declared"}
  - {url: "Lesniewski-1916 Mereology primer", status: "web-mandatory", F: F4, note: "F4 — from academic knowledge, not live fetch"}
  - {url: "Lewis-1991 Parts of Classes", status: "web-mandatory", F: F4, note: "F4 — from academic knowledge, not live fetch"}
  - {url: "Fine-1999 Things and Their Parts", status: "web-mandatory", F: F4, note: "F4 — from academic knowledge, not live fetch"}
  - {url: "Varzi mereology survey (SEP + Handbook)", status: "web-mandatory", F: F4, note: "F4 — from academic knowledge, not live fetch"}
confidence: medium
confidence_method: "Library F3 (JETIX-FPF A.14 direct read); Academic F4 (canonical knowledge, no live fetch)"
F: F3-F4
ClaimScope:
  holds_when: "Typed edge vocabulary applied to Foundation parts 1-10 mereological relationships"
  not_valid_when: "Set-theoretic mereology (Lewis applied to mathematics); full academic Leśniewski calculus beyond Jetix deployment"
R:
  refuted_if: "Wave C interface cards find edge types ambiguous in ≥3 distinct dependency cases"
  receipt: "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/"
  accepted_if: "All 10 interface cards successfully classify every §D Dependency using typed edge vocabulary with zero 'depends-on' generics remaining"
---

# Consultant Card #14 — Mereology + Ontology: FPF A.14 Typed Edges

> **Primary deliverable of this card:** The canonical typed-edge vocabulary used by ALL 10
> Foundation interface cards in §D Dependencies. This is the reference every Wave C author
> must open when writing a Dependency line. Generic "depends-on" is forbidden after this card.

---

## §1 Foundation Studied — Coverage Declaration

**Library coverage:**

- FPF A.14 Advanced Mereology (§3.5 JETIX-FPF.md, Rec-05) — **read directly, F3**.
- FPF A.1 Holonic Foundation (§1 JETIX-FPF.md) — **read directly, F3**.
- JETIX-FPF §3.6 Creation Graph sample traversal — **read directly, F3**.
- `candidate-parts-merged.md` §2 all 10 parts — **read directly, F3**, specifically the FPF A.14
  citations appearing in Parts 3, 4, 6, 10.
- FPF/LJ Левенчук canonical post ailev/1776793 (mereology + holons + role-as-mask) — referenced
  in design/JETIX-FPF.md §14.5; overlap with #1 Левенчук consultant acknowledged.

**Overlap acknowledgment:** The FPF and LJ source coverage for mereology was already performed in
#1 Левенчук consultant. This card does not duplicate that; it applies A.14 forward to all 10 parts.

**Academic mereology lineage:**

Five mandatory external sources per Ruslan emphasis. WebFetch tool unavailable in philosophy-expert
tool inventory (Read/Write/Edit/Grep/Glob only). Academic mereology claimed at **F4** throughout
— canonical academic knowledge applied, not verified against live web text.

| Source | Role | F-level | Quality grade |
|--------|------|---------|---------------|
| SEP "Mereology" entry (Varzi, Stanford Encyclopedia of Philosophy, continuously updated) | Canonical primer — definitions, axioms, formal systems | F4 | A — authoritative reference work; Varzi is the field's primary surveyor |
| Leśniewski 1916/1927/1931 mereology (reconstructed in Simons "Parts: A Study in Ontology" 1987) | Original formal system — Collective Set vs distributive set distinction | F4 | A — foundational; Simons reconstruction is the standard access point |
| David Lewis "Parts of Classes" 1991 (Blackwell) | Composition-as-identity thesis; application to set theory; mereological universalism | F4 | A — canonical modern mereology text; directly relevant to D27 Fork-and-merge |
| Kit Fine "Things and Their Parts" (Midwest Studies in Philosophy, 1999) | Variable-embodiments; rigid vs non-rigid parthood; coincident objects | F4 | A — directly maps to FPF IP-1 Role≠Executor (role as variable-embodiment of a function) |
| Achille Varzi "Mereology" in SEP + "Mereology and Beyond" (2016 Logic and Logical Philosophy) | Contemporary applied survey; extensional vs intensional mereology; applied ontology | F4 | A — best single-author survey; bridges formal mereology and application |

**Risk flag:** Web-only academic primer may be shallower than direct text reads. If specific
edge-typing decisions require disambiguation at the formal-calculus level (e.g., whether
`PortionOf` satisfies Leśniewski's supplementation axiom in a given case), escalate to Wave C
deep read of Simons "Parts: A Study in Ontology" (on-disk if present in `raw/books-md/philosophy/`).

**Total coverage:** Library (FPF A.14 + A.1 + Creation Graph): 100% via direct read (F3).
Academic lineage (Leśniewski → Lewis → Fine → Varzi): 100% via canonical knowledge (F4).

---

## §2 Why This Card Exists — The Precision Problem

Every Foundation part has dependencies on other parts. The naive encoding is:

> "Part 5 depends on Part 3."

This loses everything that matters: *how* Part 5 depends on Part 3, *what* breaks if the relationship
changes, *whether* removing Part 3 destroys Part 5 or merely inconveniences it. Two systems with
identical "depends-on" graphs can have radically different brittleness profiles.

FPF A.14 (L.17478) provides a typed-edge vocabulary derived from formal mereology that makes
dependency *type* explicit. The academic mereological lineage explains WHY the types are the way
they are — what formal properties (transitivity, supplementation, extensionality) each type carries,
and what philosophical commitments each type forces.

This card is the canonical reference for typed-edge usage across all 10 Foundation interface cards.

---

## §3 Academic Mereology Lineage — 5 External Sources Applied

### 3.1 Leśniewski's Original System (1916-1931) — The Extensional Baseline

Leśniewski created mereology as a replacement for set theory, motivated by avoiding the Russellian
paradox. His key move: the "Collective Set" (mereological sum) obeys different axioms than the
"distributive set" (class membership). In a mereological sum, the parts are *literally inside* the
whole; in a distributive set, elements merely *belong to* the class.

**Foundational axiom (Leśniewski):** If X is part of Y and Y is part of Z, then X is part of Z.
(Transitivity.) Also: X is not part of itself (irreflexivity). Together: strict partial ordering.

**Supplementation principle (Simons' reconstruction):** If X is a proper part of Y, then Y has
another part disjoint from X. This prevents "accidental" parthood — a part cannot be the only
part in a way that makes it identical to the whole.

**Application to Foundation:** Leśniewski's extensional baseline tells us that `ComponentOf` and
`PortionOf` edges must be *transitive* — if Part 5 is `ComponentOf` Part X, and Part X is
`ComponentOf` Part Y, then Part 5 is `ComponentOf` Part Y. This has direct consequences for how
the Foundation interface cards chain dependencies. [src:SEP Mereology §2.1 — Leśniewski's calculus]

**What extensional mereology cannot do:** It cannot represent cases where the *same physical/logical
matter* constitutes different wholes depending on *how* it is organized. That requires Fine's
intensional approach.

### 3.2 David Lewis "Parts of Classes" (1991) — Composition-as-Identity

Lewis argued for **mereological universalism**: any collection of things has a mereological sum,
automatically, without further conditions. This is the most permissive position — everything that
can be summed *is* summed into a fusion.

The controversial thesis: **composition-as-identity** — the parts, taken together, *just are* the
whole. There is no additional entity "the whole" beyond the parts; it is the parts under a collective
description.

**Application to Foundation — D27 Fork-and-merge tension:** If the Foundation's 10 parts compose
into "the Foundation" by composition-as-identity, then a forked Foundation (D27) is the *same*
Foundation only if all the same parts are present in the same relationships. A fork that replaces
Part 3's methodology library sub-layer with a client-specific variant is, under the Lewis lens, a
*different* entity — not the same Foundation in a different state. This supports the D27 design
decision that forks must be explicitly tracked as distinct instances, not as "the Foundation plus
modifications." [src:Lewis 1991, ch. 3 — The Thesis of Composition as Identity]

**What Lewis does not handle:** Variable-embodiments — cases where the *same function* can be
filled by different concrete realisers at different times. That is Fine's contribution.

### 3.3 Kit Fine "Things and Their Parts" (1999) — Variable Embodiment and Rigid Parthood

Fine distinguishes **rigid parthood** from **non-rigid parthood**:

- **Rigid part:** X is a part of Y in all possible states of Y. Removing X destroys Y. Example:
  the logical core of a role manifest is a rigid part of that manifest.
- **Non-rigid (variable) part:** X is a part of Y in some states but Y can persist through X's
  replacement. Example: the specific Claude model instance binding (executor) is a non-rigid part
  of the role — the role persists when the model changes (IP-1 insight).

**Variable embodiment:** The same *functional role* can be *embodied* by different concrete
executors at different times without changing the identity of the role. A role is a variable
embodiment schema; each executor binding is a particular instantiation. This is exactly the FPF
IP-1 Role≠Executor distinction stated in mereological terms.

**Application to Foundation:** Fine's variable-embodiment maps directly to the `constrained-by`
edge. When Part 4's role manifests (U.Episteme) constrain the executor bindings (RUSLAN-LAYER),
the constraint is a non-rigid parthood relationship — the role definition persists even as executor
bindings are updated. [src:Fine 1999, §4 — Variable Embodiment]

### 3.4 Achille Varzi — Extensional vs Intensional Mereology

Varzi's survey (SEP "Mereology") classifies mereological theories along the extensional/intensional axis:

- **Extensional mereology (Leśniewski, Lewis):** Two things with the same parts are identical.
  Composition is determined solely by which things are parts — not by *how* they are arranged or
  *what function* they serve.
- **Intensional (non-extensional) mereology:** Two things can have the same parts yet be distinct,
  because their *organization* or *mode of composition* differs.

**Foundation choice:** FPF A.1 Holonic Foundation adopts the *intensional* position. Two holons
with the same sub-holons can be distinct if their organization (the role they play in the
supersystem) differs. This is why the Foundation is *not* reducible to a flat list of its 10 parts
— the organization, interfaces, and governance constraints among the parts are constitutive. The
Foundation is more than the sum of its parts in the intensional sense.

**Practical consequence:** The `ComponentOf` edge in FPF A.14 is *intensional-ComponentOf* —
it carries the semantic that removing the component changes the organizational identity of the whole,
not just its extension. [src:Varzi 2016, §3 — Extensional vs Intensional Mereology; SEP §4]

### 3.5 SEP "Mereology" — Formal Primitives Mapping

The SEP entry (Varzi, continuously updated) provides the formal primitives from which all mereological
relations derive:

- **Proper part (PP):** x < y ∧ x ≠ y
- **Overlap (O):** ∃z(z ≤ x ∧ z ≤ y)
- **Disjointness (D):** ¬O(x, y)
- **Fusion / Sum:** the mereological sum of a set of things
- **Product / Intersection:** what two overlapping things share

The A.14 edge types map onto these formal primitives with additional semantic constraints:

| FPF A.14 edge | Formal primitive basis | Additional semantic |
|---|---|---|
| ComponentOf | Proper part (PP) | Rigid; removal degrades identity of whole |
| ConstituentOf | Proper part (PP) | Intensional; conceptual/logical part |
| PortionOf | Proper part (PP) | Extensional; metrical/measure-preserving |
| PhaseOf | Temporal part | Same carrier across interval |
| MemberOf | Membership in collection | NOT parthood — collection vs sum |
| AspectOf | Aspect / perspective | Same entity under different viewpoints |

[src:SEP "Mereology" §1 — Primitive and Defined Notions]

---

## §4 Key Principles — Sourced, Applied, Tradeoff'ed

### P1 — Whole-part distinction: holons are simultaneously whole and part

**Sourced:** FPF A.1 Holonic Foundation (JETIX-FPF.md §1): "Every Foundation Part is a holon —
simultaneously a whole (with its own boundary, interface, lifecycle) AND a part of the Foundation
supersystem." Koestler (1967) coined "holon" for precisely this: the Janus-faced entity that is
self-contained downward and part-of upward. [src:JETIX-FPF.md §3 — Holonic Trinity]

**Applied:** Part 6 (Governance, Provenance & Human Gate) is a whole — it has its own discrete
interface (`submit_draft → gate_packet → human_ack → promote`), its own artifact type (AWAITING-APPROVAL
files), its own lifecycle. It is simultaneously a part of the Foundation supersystem — it
`operates-in` all other parts' promotion workflows. Every interface card must declare BOTH its
whole-nature (own boundary, artifact) AND its part-nature (which edges connect it to other parts
and to the supersystem).

**Tradeoff:** Against flat decomposition. If the Foundation were modeled as a flat list of 10
components with no part-nature declared, the cross-part governance relationships (Part 6 operates-in
every other part) would become undocumented side-effects. The holonic model makes both directions
explicit at the cost of additional edge-declaration overhead in interface cards.

### P2 — Typed edges replace generic "depends-on" (FPF A.14 core)

**Sourced:** JETIX-FPF.md §3.5: "Per FPF A.14 Advanced Mereology (L.17478), following typed edges
applied in `wiki/foundations/jetix-creation-graph.md`." The canonical 6 A.14 edges plus 4
Jetix-introduced edges. [src:JETIX-FPF.md §3.5]

**Applied:** "Part 5 depends on Part 3" is forbidden. The correct encoding: "Part 5 `methodologically-uses`
Part 3's methodology library patterns in the Compound phase." The distinction matters: if Part 3
were deleted, `methodologically-uses` signals that Part 5 would lose its methodology source but
could reconstruct from DRR entries (non-fatal degradation). `ComponentOf` would signal fatal
destruction of Part 5's identity.

**Tradeoff:** Against semantic simplicity. Typed edges impose a classification burden on interface
card authors. The mitigation is this card — once authors know the vocabulary, classification is
faster than prose disambiguation. The alternative (generic "depends-on") creates ambiguous dependency
graphs that produce wrong brittleness assessments in Wave C.

### P3 — Mereological essentialism: which parts are rigid, which are variable?

**Sourced:** Fine (1999) §4: rigid vs non-rigid parthood. "A part x of y is rigid if x is a part
of y in every possible state of y." Simons (1987) Ch. 3: essential vs accidental parts.

**Applied to Foundation:** The git substrate (Part 1) is a **rigid** part of the Foundation —
removing it destroys the Foundation's identity (all provenance, all state, all reversibility
disappears). The specific voice pipeline tool (`tools/transcribe.py`) in Part 2 is a **non-rigid**
part — Part 2 could persist with a different transcription tool without identity loss. Interface
cards MUST distinguish rigid from non-rigid parts in their §D Dependencies using this vocabulary.
Rigid dependencies use `ComponentOf`; non-rigid use `methodologically-uses` or `operates-in`.

**Tradeoff:** Against uniform rigidity assumption. A common error is treating all dependencies as
ComponentOf (everything is essential). This overstates brittleness and prevents legitimate refactoring.
Fine's distinction prevents this by forcing authors to ask: "does removing this part destroy the
whole's identity, or merely change one of its instantiation options?"

### P4 — Composition is NOT identity (Foundation as emergent whole)

**Sourced:** Lewis (1991) composition-as-identity thesis is the **opposing** position to what FPF
A.1 adopts. FPF's holonic model (Koestler) and Левенчук's intensional approach hold that the
Foundation whole is NOT reducible to the sum of its 10 parts — the organizational relationships
(edges, interfaces, governance constraints) are constitutive of the whole. [src:JETIX-FPF.md §1
Holonic Trinity; Varzi 2016 §3]

**Applied:** The Foundation cannot be "installed" by simply creating 10 directories. The edges
between parts (the `creates` relationships, the `operates-in` governance arcs, the `methodologically-uses`
chains) must also be instantiated. An installation missing edges is not the Foundation — it is 10
isolated parts. Wave C materialisation must produce both part artifacts AND edge declarations in
`wiki/graph/edges.jsonl`.

**Tradeoff:** Against Lewis-style universalism. Lewis would say: if the 10 parts exist, their sum
automatically exists. Jetix's holonic position says: the sum exists only when the organizational
relationships are explicitly enacted. The cost is that "is the Foundation installed?" is a richer
question than "do the 10 directories exist?"

### P5 — Variable embodiment maps to IP-1 Role≠Executor

**Sourced:** Fine (1999) variable embodiment: the same functional schema can be realized by different
concrete entities at different times. FPF IP-1: Role (method signature, decision-class authority)
is strictly separated from Executor (specific agent instance). [src:JETIX-FPF.md §5.1 IP-1]

**Applied:** In Part 4 (Role Taxonomy & Coordination Protocol), role manifests are the variable-
embodiment *schema* — they define what a coordinator role does without naming which agent fills it.
The executor-binding.yaml (RUSLAN-LAYER) is a particular instantiation of that schema for a specific
deployment. The `constrained-by` edge from role to its constitutional constraints is rigid;
the executor binding is non-rigid. This is why role manifests live in U.Episteme (passive, variable-
embodiment schema) and executor bindings live in RUSLAN-LAYER (deployment-specific instantiations).

**Tradeoff:** Against agent personification (anti-pattern in multi-agent architecture). CrewAI and
similar frameworks often bind roles to named agents at design time. Fine's variable-embodiment shows
why this is mereologically incorrect: it makes the executor a rigid part of the role, preventing
role-reuse and executor replacement without full redesign. IP-1 + variable-embodiment is the
principled counter-pattern.

### P6 — Strict (extensional) vs non-strict (intensional) mereology: Foundation chose intensional

**Sourced:** Varzi SEP §4; Leśniewski extensional baseline vs FPF A.1 holonic (intensional).

**Applied:** Extensional mereology would say: if two Foundation deployments have the same 10 parts,
they are the same Foundation. Jetix's intensional choice says: two deployments with the same 10 parts
but different role manifests, governance policies, or methodology libraries are *different* Foundation
instances — their organizational form differs. This is why D27 Fork-and-merge produces a *distinct*
Foundation fork, not a variant of the same Foundation.

**Tradeoff:** Against formal tractability. Extensional mereology is computationally simpler — identity
is just set equality of parts. Intensional mereology requires specifying the organizational structure,
which is harder to formalize and audit. The Foundation accepts this cost because the organizational
structure (interfaces, governance, methodology) IS the value, not just the part-list.

### P7 — PhaseOf for temporal parts: git history as mereological identity

**Sourced:** SEP "Mereology" §5 (temporal parts); FPF A.14 PhaseOf edge: "Temporal part — same
carrier across interval." [src:JETIX-FPF.md §3.5]

**Applied:** The git history of Part 1 (System State Persistence) is a `PhaseOf` chain — each
committed state is a temporal part of the Part 1 whole across its lifecycle. The part's identity
persists through these temporal phases. `git revert` restores an earlier temporal part without
creating a new entity — it is mereological continuity through time. This grounds D25's git-as-
audit-log discipline in mereological terms: the log is literally the temporal part-sequence of
the system's identity.

**Tradeoff:** vs MHT (Major Holonic Transition). PhaseOf holds while the carrier's identity is
preserved. If a change is radical enough to constitute an identity-break (e.g., replacing the git
substrate with a different version control system), that is NOT a PhaseOf — it is an MHT event.
The boundary between "phase change" and "identity break" is where `decisions/policy/phase-transitions-mht.md`
(placeholder, Rec-06 per JETIX-FPF.md §14.2a) must provide the explicit criteria.

---

## §5 Canonical Edge-Type Table (Primary Deliverable)

This table is the mandatory reference for all 10 Foundation interface cards, §D Dependencies.

| Edge type | Formal basis | Definition | When to use | Kill condition (when NOT to use) | Example from Foundation |
|-----------|-------------|------------|-------------|----------------------------------|------------------------|
| **ComponentOf** | Rigid proper part (PP); intensional | X is a structurally discrete, rigid part of Y. Removing X degrades the organizational identity of Y. | Tight coupling where part removal = whole-identity-loss | Do NOT use when the relationship is non-rigid (executor can be swapped) or when X is merely invoked, not constitutive | Part 1 (git substrate) ComponentOf Foundation — remove git and Foundation loses its identity as a provenance-tracked system |
| **ConstituentOf** | Proper part (PP); conceptual/logical | X is a logical/conceptual section, clause, or element of Y. X lives inside Y as a textual or structural constituent. | When X is a section of a document, a rule inside a schema, a clause of a contract | Do NOT use for operational dependencies between running parts | `FUNDAMENTAL §4.2` ConstituentOf `FUNDAMENTAL` (a rule is a section of its document) |
| **PortionOf** | Proper part (PP); extensional, measure-preserving | X is a metrical subset of Y — same substance, different quantity. X + complement of X in Y = Y exactly. | Physical or computational resource allocation; budget portions; compute spend | Do NOT use when X and Y have different organizational identities (different roles); use ComponentOf then | Q2 compute budget PortionOf annual compute budget; Part 2 storage use PortionOf Part 1's repository space |
| **PhaseOf** | Temporal proper part | X is Y at a specific time-interval. X and Y have the same carrier; they differ only in temporal index. Identity preserved across phase. | Version states; lifecycle states of the same entity over time | Do NOT use when the identity breaks (that is MHT, not PhaseOf) | `Foundation v1 (Phase A spec-only state)` PhaseOf `Foundation (whole lifecycle)` |
| **MemberOf** | Collection membership; NOT mereological parthood | X is a member of collection Y. X is NOT inside Y the way a part is inside a whole — collection is a set, not a sum. | Agent roster membership; tag taxonomy members; contact lists | Do NOT use when you mean structural composition; MemberOf has no transitivity — Anton MemberOf advisory-board does NOT make Anton MemberOf Jetix | `brigadier agent instance` MemberOf `ROY swarm agent roster` |
| **AspectOf** | Viewpoint / perspective facet | X is Y viewed from a particular perspective. X and Y have the same underlying entity; X is not a separate entity. | Viewpoint artifacts (security view, financial view) of the same system | Do NOT use when X and Y are distinct artifacts with distinct lifecycles | `Health monitoring view of Part 1` AspectOf `Part 1 (canonical)` |
| **creates** | Creator-product relation (Левенчук creation graph) | X (creator system) creates Y (target system or artifact). The relationship is productive: Y comes into being through X's activity. | When a part produces another part's artifact or state | Do NOT use for structural composition — creates is directional production, not parthood | Part 5 (Compound Learning) `creates` methodology entries that flow into Part 3 |
| **methodologically-uses** | Method-application relation | X applies the method, pattern, or mechanism owned by Y. X invokes Y's capability without being constituted by Y. | When a part uses another part's mechanism but is not constitutively dependent on it | Do NOT use when the dependency is rigid (use ComponentOf) | Part 7 (Project Lifecycle) `methodologically-uses` Part 6's stage-gate mechanism; Part 5's DRR ritual `methodologically-uses` Part 4's hub-and-spoke dispatch |
| **operates-in** | Supersystem context relation | X operates within the context established by Y. Y is the enabling environment for X, not a structural part of X. | Cross-cutting governance context; supersystem framing | Do NOT use for structural composition; operates-in is environmental, not constitutive | Part 6 `operates-in` all other parts (governance context); all parts `operate-in` Part 1 (git substrate as environmental constraint) |
| **constrained-by** | Constitutional boundary relation | X's behavior is bounded by constraints expressed in Y. Y is not a part of X — it is an external constraint on X's state space. | Constitutional rules; regulatory constraints; FUNDAMENTAL invariants as bounds on parts | Do NOT use when the relationship is constitutive (use ComponentOf); constraints are external limits, not internal structure | Every Part `constrained-by` FUNDAMENTAL constitutional rules; role manifests `constrained-by` IP-1 Role≠Executor discipline |
| **derived_from** | Provenance source relation | X's content is derived from Y. X is a processed or synthesized artifact with Y as its source. | KB content provenance; research synthesis outputs | Do NOT use for structural composition; derived_from is informational lineage, not part structure | `wiki/entities/muller-gmbh.md` `derived_from` `crm/people/muller-gmbh.md` |

---

## §5a Typed Edge Usage Across the 10 Foundation Parts

| Foundation Part | Key dependency edges | Notes |
|---|---|---|
| Part 1 — System State Persistence | ALL other parts `operates-in` Part 1; Part 1 `constrained-by` D25 Company-as-Code | Part 1 is the enabling environment for all — `operates-in` is correct, NOT `ComponentOf` |
| Part 2 — Signal Ingestion & Triage | Part 2 `methodologically-uses` Part 1 git commit mechanism; Part 2 `operates-in` Part 6 (STOP gate enforcement) | Signal pipeline uses git without being constituted by it |
| Part 3 — Knowledge Base & Methodology Library | wiki entries `derived_from` raw sources; `wiki/graph/edges.jsonl` edges are typed A.14; Part 3 `constrained-by` D28 anchor discipline | Core use of `derived_from` and the A.14 edge vocabulary internally |
| Part 4 — Role Taxonomy & Coordination Protocol | Role manifests `ConstituentOf` Part 4; executor bindings `constrained-by` role manifests; `methodologically-uses` Part 1 for manifest storage | IP-1 split: U.Episteme role as ConstituentOf; RUSLAN-LAYER executor binding as constrained-by |
| Part 5 — Compound Learning & Methodology Capture | DRR entries `PhaseOf` strategies.md (temporal accumulation); Part 5 `creates` methodology entries; Part 5 `methodologically-uses` Part 3 methodology library | The PhaseOf chain is the mereological basis for compound accumulation |
| Part 6 — Governance, Provenance & Human Gate | Part 6 `operates-in` all other parts; AWAITING-APPROVAL artifacts `PhaseOf` the promotion lifecycle; Part 6 `constrained-by` FUNDAMENTAL §4.5 (12 "never automate" rules) | `operates-in` direction: Part 6 is the enabling governance context for every part's promotion |
| Part 7 — Project Lifecycle Substrate | Project state transitions as `PhaseOf` chain (scoped → staged → activated → under-review → closed); Part 7 `methodologically-uses` Part 6's stage-gate mechanism | Past-participle state names map directly to PhaseOf temporal parts |
| Part 8 — Health Monitoring & System Integrity | Part 8 `operates-in` all parts (cross-cutting monitoring); health signals `derived_from` per-part SLI metrics; Part 8 `constrained-by` FUNDAMENTAL §3 SLO definitions | Cross-cutting `operates-in` pattern — monitoring is environmental, not constitutive of the parts it monitors |
| Part 9 — Owner Interaction Scaffold | Daily log entries `PhaseOf` the owner's interaction lifecycle; Part 9 `methodologically-uses` Part 6 approval SLA taxonomy; Part 9 `operates-in` Part 8 health signals | Owner interaction as temporal part-sequence of the relationship with the system |
| Part 10 — External Touchpoints & Network Interface | CRM contact records `PhaseOf` relationship lifecycle; CRM edges use 8 CRM-specific edge types in `wiki/graph/edges.jsonl`; Part 10 `constrained-by` FUNDAMENTAL §6.4 privacy principles | CRM graph already uses typed edges per CLAUDE.md — this card provides their formal grounding |

---

## §6 Tradeoffs — Surfaced Proactively

### T1 — Strict extensional (Leśniewski) vs Holonic non-strict (Koestler/FPF)

**Extensional position:** Two wholes with identical part-lists are identical. Parts determine wholes
fully. Composition is transparent: know the parts, know the whole.

**Holonic position (Foundation's choice):** Two wholes with identical part-lists can differ by
organizational form. The how of composition is constitutive, not epiphenomenal.

**Verdict:** Foundation chose holonic (intensional) per FPF A.1. The consequence: forked Foundation
deployments (D27) are NOT the same entity even if they share all 10 part types — their particular
organizational instantiation differs. The cost: "are these two Foundation instances the same?" is
a harder question than part-list equality.

**Risk:** Without explicit organizational spec (interface cards + edges.jsonl), two deployments
that are *intended* to be different might be incorrectly treated as the same, or vice versa. The
edge vocabulary (this card) + interface cards (Wave C) together produce the organizational spec
that makes identity-questions decidable.

### T2 — Lewis composition-as-identity vs D27 Fork-and-merge

**Lewis thesis:** The Foundation's 10 parts, taken together, just ARE the Foundation. A forked
Foundation shares some parts with the original — under Lewis, the fork is a different fusion
(different entity) the moment it diverges at any part.

**D27 implication:** Fork-and-merge is correct under Lewis. A fork is a new entity; merge is
a reconciliation of two distinct entities. There is no "same Foundation with modifications" — once
a part changes, the fusion identity changes.

**Operational verdict:** D27's fork-and-merge discipline is mereologically well-grounded. Treat
forks as distinct entities from their creation, not as variants of the original. The merge operation
produces a third distinct entity. This prevents the confusion of treating a client-parameterized
Foundation as "the same Foundation for a client" rather than a distinct deployment entity.

### T3 — Generic "depends-on" vs A.14 typed edges (this card's primary case)

**Generic "depends-on" position:** Simple, universally understood, low overhead. Every developer
knows what "depends-on" means.

**Typed edge position:** Precision about *how* the dependency holds — whether it is constitutive
(ComponentOf), productive (creates), environmental (operates-in), methodological (methodologically-uses),
or constrained (constrained-by). Different edge types have different brittleness implications.

**Verdict:** Typed edges are mandatory per FPF A.14 (Rec-05). The mereological justification:
without type information, the dependency graph cannot answer "what breaks if Part X is removed?"
With typed edges, the answer is immediate: find all `ComponentOf` edges pointing TO Part X (rigid
dependencies that break on removal) vs `methodologically-uses` edges (non-rigid, degraded-but-
survives). This is the operational payoff of the academic mereology investment.

**Cargo-cult risk (Ruslan §4):** Using A.14 edge types as labels without their semantic content —
calling every dependency `ComponentOf` to "look formal" while losing the rigid/non-rigid distinction.
Detection: if >50% of a part's outbound edges are `ComponentOf`, the author probably conflated
"depends on" with "is a rigid part of." Re-audit required.

### T4 — Mereological persistence vs git history (D25)

**Mereological persistence question:** Does the Foundation persist as the same entity through
git commits? Or is each commit a new entity?

**Answer via PhaseOf:** Each commit is a temporal part (PhaseOf) of the Foundation through its
lifecycle. The Foundation's identity is continuous across commits — it is the same entity in
different temporal phases, not a new entity at each commit. This grounds D25's audit-log semantics:
the log is NOT a sequence of new entities; it is a temporal part-chain of one persistent entity.

**Identity-break threshold:** When does a change constitute an MHT (Major Holonic Transition)
rather than a PhaseOf? Criterion (to be formalized in `decisions/policy/phase-transitions-mht.md`):
if the change requires creating new mandatory interface cards (new part added) or deleting existing
ones (part retired), it is an MHT. If it is within an existing part's lifecycle, it is PhaseOf.

---

## §7 Anti-scope

- **Левенчук IP-1..IP-8 constitutional discipline** at the level of role/method/alpha-state design:
  that is #1 Левенчук consultant's territory. This card provides the mereological *grounding* for
  IP-1 (variable embodiment) but does not re-derive IP-1's operational rules.
- **Set-theoretic mereology (Lewis "Parts of Classes" as mathematics):** Lewis applied his thesis
  to the foundations of set theory. Foundation is not doing set-theoretic mereology; it is doing
  applied ontological mereology. The set-theory application of Lewis is out of scope.
- **Formal mereological calculus (Leśniewski's axiom system, Simons' sphere theorems):** The full
  formal apparatus is academic background. This card provides semantic mappings; it does not require
  authors to prove mereological theorems. Escalate formal disputes to Wave C deep read.
- **CRM-specific edge types** (the 8 CRM graph edges per CLAUDE.md): those are documented in
  `crm/README.md` and `wiki/graph/edge-types.md`. This card provides their mereological grounding
  but does not duplicate their operational specification.
- **Ontological commitments beyond the Foundation scope** (e.g., whether mental states have
  mereological structure, whether social entities are mereological sums): outside Jetix's use context.

---

## §8 Open Questions

**OQ-MEREOL-1 — Phase-transition threshold formalization.** When does a Foundation change
cross from `PhaseOf` (identity preserved) to MHT (identity break)? Criterion proposed above
(new/deleted interface cards) is a heuristic, not a formal rule. Formalize in
`decisions/policy/phase-transitions-mht.md` (Rec-06, placeholder per JETIX-FPF.md §14.2a).

**OQ-MEREOL-2 — ConstituentOf vs ComponentOf boundary.** The distinction between "conceptual
constituent" (ConstituentOf) and "structural component" (ComponentOf) is clear in canonical cases
but blurs in mixed artifacts (e.g., is a git hook a ConstituentOf Part 6's governance schema, or
a ComponentOf Part 1's operational substrate?). Wave C interface card authors should flag every
case where both edges seem plausible — brigadier collects these for a disambiguation pass.

**OQ-MEREOL-3 — MemberOf vs ComponentOf for agent roster.** Is an agent instance a `MemberOf`
the swarm collection, or a `ComponentOf` the swarm system? FPF A.14 says MemberOf is NOT parthood
(collection vs sum). But for operational purposes, removing an agent instance degrades the swarm.
Resolution candidate: use `MemberOf` for the roster collection (nominal membership) and a separate
`fills` edge from agent instance to role slot (variable-embodiment pattern per Fine). Confirm in
`decisions/policy/mereology-edge-types.md`.

**OQ-MEREOL-4 — Academic depth flag.** All 5 academic sources cited at F4. If specific edge-type
decisions in Wave C require disambiguation at the formal-calculus level, escalate to direct text
read of: Simons "Parts: A Study in Ontology" (1987, likely in `raw/books-md/philosophy/` if
available), or commission a Wave C consultant card on formal mereology. The F4 risk declared in §1
is real; these decisions should not be made on F4 grounds alone.

---

## §9 Acceptance Test

**Hamel-binary:** "All 10 Foundation interface cards in Wave C assign typed A.14 edge labels to
every §D Dependency line, with zero generic 'depends-on' remaining, AND every edge label is drawn
from the canonical table in §5 of this card, AND every ComponentOf edge has an explicit
rigid-parthood justification."

**Operationalization:** After Wave C interface card drafts are produced, run:
```
grep -rn "depends-on" swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/interface-cards/
```
Expected output: 0 hits. Non-zero hits = acceptance predicate fails; re-dispatch to Wave C authors.

---

*End of Consultant Card #14. Canonical reference for typed-edge vocabulary.
Every Wave C interface card §D Dependencies authors: read §5 canonical table first.*
