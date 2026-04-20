# Mereology & Holon Theory: Foundational Reference for Jetix OS

**Prepared for:** Ruslan (Jetix OS, Berlin)  
**Framework context:** Anatoly Levenchuk's ШСМ (School of Systems Management)  
**Date:** 2026  
**Status:** Foundational reference — read-only for agents, strategic input for Ruslan

---

## How to Read This Report

**TL;DR path (15 min):** Executive Summary → Section 7 (checklist) → Section 8 (over-formalization risks). This gives the full action picture.

**Deep path (90 min):** Full sequential reading. Sections 1–2 are dense philosophy; Sections 3–4 are applied. Section 5 is the Levenchuk bridge. Section 6 contains the genuine cost-benefit analysis of what Levenchuk excludes. Sections 7–9 are prescriptive.

**Agent-context note:** Sections 5–7 are the most operationally relevant for Jetix OS. Sections 1–4 are reference material — agents should be aware they exist but need not load them into working context for routine tasks.

---

## Executive Summary

Mereology — the philosophical theory of part-whole relations — and holon theory — the framework describing entities that are simultaneously whole-and-part — together form the conceptual spine of Jetix OS's architecture. Ruslan models Jetix as nested holons: L1 roles (sales-lead, strategy-lead), L2 functional clusters (Sales Function, Delivery Function), L3 business directions (ai-consulting-dach, shaurma-chains), L4 Jetix as whole (within Life-OS holon), and L5 Life-OS as supersystem. Levenchuk's FPF codifies this as "мереология холонов" (mereology of holons) — a pragmatic, engineering-oriented framework that deliberately excludes heavy philosophical apparatus.

**Key finding on Levenchuk's mereology:** Levenchuk explicitly calls FPF's foundation "advanced mereology" ([ailev.livejournal.com/1776793](https://ailev.livejournal.com/1776793.html)) but this term in his usage means something specific — it is not Classical Extensional Mereology (CEM) from Leonard-Goodman, nor is it Kit Fine's hylomorphic mereology in full. It is an engineering mereology that: (a) treats holons as the basic unit rather than arbitrary sums, (b) emphasizes causally grounded decomposition over logical completeness, (c) incorporates constructor theory's notion of transformations, and (d) uses the partonomy (партономия) as the preferred hierarchical structure rather than flat fusions. Kit Fine's full apparatus (qua-objects, mereological coincidence, location pluralism) and constructor theory beyond transformation-language are explicitly not imported.

**What to apply now (Section 7 preview):**
- Koestlerian holon duality (self-assertive vs integrative) — directly maps to the tension between L1 role autonomy and L4 Jetix coherence. Apply immediately as a design principle when an agent role "overasserts" or when Jetix-level coordination breaks down.
- Three-level creation graph (target/creation/supersystem) — the core operational tool. Already in use; Section 5 gives the full formal grounding.
- AGR model (Agent/Group/Role) from MAS literature — the closest academic parallel to Jetix's role-based agent architecture. Low cost to import the vocabulary.
- PROSA holonic manufacturing pattern (order/product/resource holons) — the best analogy for Jetix's AI agent decomposition. Section 4 develops this mapping explicitly.

**What to skip:**
- Kit Fine's full qua-objects and mereological coincidence theory — philosophically rigorous but operationally moot for Jetix. The "ham sandwich monster" problem is irrelevant when your "parts" are software agents with clear interface contracts.
- Constructor theory as physics — beautiful framework but the useful fragment (possible/impossible transformations for creation graph) is already absorbed in Levenchuk's usage. The rest is quantum foundations irrelevant to business architecture.
- Category theory formalization of org states — premature at current Jetix scale. Revisit at 50+ agents or when formal interface contracts need machine-verifiable proofs.
- Van Inwagen's organicism (composition only for living organisms) — interesting philosophical position but directly contradicts the multi-level Jetix architecture and should be noted only as a critique to be aware of.

**Critical tension to manage:** The Special Composition Question (van Inwagen) — "under what conditions do some things compose a whole?" — has a direct Jetix instantiation: when do sub-agents constitute a functional cluster? Levenchuk's answer is pragmatic (composition tracks stakeholder interest and lifecycle stage), not formal. This is correct for Jetix Phase 1-2. If Jetix scales to federated multi-company structure (Phase 3+), a more formal composition criterion becomes valuable for governance.

---

## Section 1 — Mereology: Foundational Theory

### 1.1 Definition, Etymology, History

Mereology (from Greek μερος, *meros*, "part") is the philosophical and formal theory of part-whole relations — the relations of part to whole and of part to part within a whole. It is not about the content of things but about the structural logic of how things compose and decompose.

The formal discipline begins with Stanisław Leśniewski's *Foundations of the General Theory of Sets* (1916) and *Foundations of Mathematics* (1927–1931). Leśniewski, working in the Polish tradition of nominalist ontology, needed an alternative to Cantorian set theory that avoided commitment to abstract objects. His key insight: wholes are no more abstract than their parts — a heap of bricks is as concrete as a single brick. This nominalist motivation produced the first rigorous axiomatic mereology ([Stanford Encyclopedia of Philosophy, Mereology](https://plato.stanford.edu/entries/mereology/)).

The modern accessible formulation came through Henry Leonard and Nelson Goodman's *The Calculus of Individuals* (1940), influenced by Whitehead's work on events and extensive abstraction. This "calculus" brought Leśniewski's system into analytic philosophy, where it has remained a central tool for metaphysics of material objects, philosophy of science, and formal ontology.

Historical antecedents reach back through Aristotle's *Metaphysics* and *Physics* (part-whole analysis of substances), Husserl's third *Logical Investigation* (1901) on the theory of wholes and parts, and Leibniz's monadology. However, the pre-Leśniewski treatments lacked the axiomatization that makes modern mereology formally tractable ([SEP Mereology](https://plato.stanford.edu/entries/mereology/)).

**Distinction from set theory:** Mereology and set theory are often confused but are fundamentally different. In set theory, a set {A, B} is abstract — it is not A or B, and contains them as *members*, not parts. In mereology, a whole is *nothing over and above* its parts — it is the fusion of them. The whole is concrete, not abstract. A set can have a set as a member ({A, {B, C}}); mereologically, part-of is a transitive relation between things at the same ontological level. Crucially, mereology admits no empty element (there is no "null object" in standard systems), whereas set theory requires the empty set. Tarski (1935) and Grzegorczyk (1955) showed that models of General Extensional Mereology are isomorphic to complete Boolean algebras minus the zero element — this algebraic character makes mereology amenable to formal reasoning while keeping it ontologically parsimonious ([SEP Mereology](https://plato.stanford.edu/entries/mereology/)).

For Jetix: the mereological framing is correct for organizational architecture because Jetix-as-whole is not an abstract entity separate from its parts — it *is* the structured fusion of its agents, roles, and functions. The Life-OS/Jetix separation (Model D) is not set-theoretic containment but mereological part-within-whole with an asymmetric reference rule.

### 1.2 Major Formal Systems

The axiomatic landscape of mereology can be organized by which axioms are added to a base partial-ordering structure:

| System | Full Name | Key Additions | Character |
|---|---|---|---|
| **M** | Core (Minimal) Mereology | Reflexivity (P.1), Transitivity (P.2), Antisymmetry (P.3) | Partial ordering on parthood |
| **MM** | Minimal Mereology | M + Weak Supplementation (P.4) | A proper part implies another disjoint part exists |
| **EM** | Extensional Mereology | MM + Strong Supplementation (P.5) | No two distinct wholes with same proper parts |
| **GEM** | General Extensional Mereology | EM + Unrestricted Composition | The classical system; any non-empty collection has a fusion |
| **CEM** | Classical (Leonard-Goodman) | Equivalent to GEM | Basis of formal ontology engineering |

The three core axioms of M define parthood (Pxy = "x is part of y") as a partial order:
- **Reflexivity (P.1):** Everything is a part of itself: ∀x Pxx
- **Transitivity (P.2):** If x is part of y and y is part of z, then x is part of z: (Pxy ∧ Pyz) → Pxz
- **Antisymmetry (P.3):** If x is part of y and y is part of x, then they are identical: (Pxy ∧ Pyx) → x=y

The critical supplementation axioms:
- **Weak Supplementation (P.4):** Every proper part has a companion — PPxy → ∃z(Pzy ∧ ¬Ozx). A proper part cannot exhaust its whole.
- **Strong Supplementation (P.5):** Stronger version — if x is not part of y, then y has a part disjoint from x: ¬Pyx → ∃z(Pzy ∧ ¬Ozx). This entails extensionality.

**GEM / Unrestricted Composition (P.15):** For any non-empty collection of objects φ, there exists a fusion of all φ-things: ∃w φw → ∃z S³z φw. This is the most powerful and most controversial axiom — it implies that the fusion of Cleopatra's nose and the Eiffel Tower is a genuine object. Philosophically contentious; operationally irrelevant for Jetix where only intentional compositions matter ([SEP Mereology](https://plato.stanford.edu/entries/mereology/)).

**David Lewis's mereology** (*Parts of Classes*, 1991) applied GEM to set theory itself, treating set membership as a special case of parthood. Lewis's key contribution for organizational reasoning: his defense of mereological universalism (unrestricted composition is fine — the question is not *what* composes but *what we care about* among the vast plurality of composed objects). This is the pragmatic stance Levenchuk effectively adopts: Jetix's holons are not the only possible compositions — they are the *relevant* ones given stakeholder interests.

**Kit Fine's hylomorphic mereology** (*Things and Their Parts*, 1999) is the most philosophically sophisticated departure from CEM. Fine argues that standard mereology yields a "flat" conception of objects — ham, cheese, and bread, combined, produce a ham sandwich *before* assembly (since their fusion exists whenever they exist). This is Fine's "Monster Objection": mereological sums are insensitive to *structure*. Fine's alternative introduces hylomorphism — form as constitutive element. A hylomorphic compound is not a mere sum of its material parts plus an attribute as "coequal"; rather the formal element "preserves its predicative role and somehow serves to modify or qualify the components" ([Fine, 1999, *Things and Their Parts*, Midwest Studies in Philosophy](https://www.academia.edu/114589867/Things_and_Their_Parts)). Fine's system adds: (a) different types of parthood for different entity kinds, (b) qua-objects (an object *qua* playing a role), and (c) mereological coincidence (matter ≠ thing constituted by matter). Section 6.1 evaluates whether this apparatus is useful for Jetix.

**Hudson's location mereology** (*The Metaphysics of Hyperspace*, 2005) adds a location relation L(x,r) ("x is exactly located at region r") to standard mereology. Mereological Harmony principles link structural properties of objects to their locations (H5: x is part of y iff x's location is a subregion of y's location). Extended simples (simple objects at complex locations) and multilocation (one object at multiple regions) are the key puzzles ([SEP Location and Mereology](https://plato.stanford.edu/entries/location-mereology/)). The Jetix application: logical holons (e.g., the ai-consulting-dach direction) can be "multilocated" — instantiated on multiple physical servers, repositories, and team members simultaneously.

**Constructor theory** (David Deutsch & Chiara Marletto, 2012–present) reframes physics as a theory of which transformations (tasks) are possible vs impossible, and why. A *task* is an abstract specification of transformations as input-output pairs of attributes. The central concept is the *constructor*: an object that causes transformations and retains the ability to cause them again. Constructor theory is not a mereology per se — it is a meta-theory of physical laws expressed counterfactually ([Wikipedia, Constructor Theory](https://en.wikipedia.org/wiki/Constructor_theory); [Quanta Magazine](https://www.quantamagazine.org/with-constructor-theory-chiara-marletto-invokes-the-impossible-20210429/)). Levenchuk imports its *vocabulary* (transformations, constructors, possible/impossible tasks) into FPF's creation graph without importing its physics foundations.

### 1.3 Key Concepts

**Parthood types** (all definable from primitive Pxy):

| Term | Symbol | Definition |
|---|---|---|
| Proper parthood | PPxy | Pxy ∧ ¬(x=y) |
| Proper extension | PExy | Pyx ∧ ¬(x=y) |
| Overlap | Oxy | ∃z(Pzx ∧ Pzy) |
| Disjointness | Dxy | ¬Oxy |
| Underlap | Uxy | ∃z(Pxz ∧ Pyz) |
| Fusion / Mereological sum | S³zφ | z overlaps exactly those things that overlap some φ |

**Composition and fusion:** Composition is the upward movement from parts to whole. In GEM, any non-empty set of objects has a unique fusion. The fusion of {A, B} is the minimal whole that has both A and B as parts. Note: fusion ≠ set. The fusion of Ruslan and his laptop is a concrete scattered object; the set {Ruslan, laptop} is abstract.

**Decomposition and supplementation:** Moving downward from whole to parts. The Weak Supplementation Principle ensures that if x is a proper part of y, there is at least one other part of y disjoint from x — a whole cannot consist of only one proper part. The Strong Supplementation Principle (in EM and GEM) entails that objects with the same proper parts are identical.

**Extensionality:** The GEM principle that no two distinct composites share all the same proper parts. This is philosophically contested — the statue and the clay seem to have the same parts but different properties. Kit Fine's theory denies extensionality; it is one reason Fine departs from CEM.

**Atomism vs gunk:** An *atom* is a part with no proper parts. An *atomistic* mereology holds that everything eventually decomposes into atoms. *Gunky* mereology (atomless) holds that every part has proper parts — there is no "smallest piece." For organizations: roles (L1) function as near-atoms — the smallest unit with coherent behavior. But roles themselves decompose into capabilities, routines, and methods. Whether Jetix has true atoms depends on the granularity at which role-decomposition stops being useful.

**Restricted vs unrestricted composition:** Unrestricted composition (GEM) says any collection of objects has a fusion. Restricted composition answers the Special Composition Question with conditions: only objects that are spatially contiguous, or causally integrated, or functionally related, compose a whole. For Jetix, composition is restricted by *stakeholder relevance* — the holons that matter are those whose composition tracks a distinct set of interests in the creation graph.

**Partonomy (партономия):** In Levenchuk's usage, this is the preferred term for holarchic structure — an ordered tree of part-whole relations where each node is a holon. Unlike a flat mereological sum (where all fusions are ontologically equal), a partonomy emphasizes the *hierarchical organization* of parts ([ailev.livejournal.com/1776793](https://ailev.livejournal.com/1776793.html)).

### 1.4 Key Critiques

**The Special Composition Question (van Inwagen, *Material Beings*, 1990):** When do some objects compose a whole? Van Inwagen's answer (organicism): composition occurs only when objects are engaged in life-constituting activity — only organisms are genuine composites. Tables, chairs, and corporations do not literally exist. This is philosophically provocative but operationally absurd for organizational design. The practical response (following Lewis and Levenchuk) is to accept that composition is unrestricted but *relevance* is restricted: infinitely many fusions exist, but only those tracking stakeholder interests deserve a named node in the creation graph ([SEP Ordinary Objects](https://plato.stanford.edu/entries/ordinary-objects/)).

**Vagueness:** Composition can be vague — is the boundary between Jetix and Life-OS sharp? The "problem of the many" and sorites-style arguments suggest no sharp boundary exists. Kit Fine's granular mereology and supervaluationist approaches handle this; Levenchuk sidesteps it with a practical rule: if a human employee would see the data, it belongs to Jetix; otherwise, Life-OS.

**Identity over time:** The Ship of Theseus problem — if all parts of a system are gradually replaced, is it the same system? For Jetix, this is the agent-succession question: if all AI agents are replaced (model upgrades, new Claude versions), is it still Jetix OS? The answer requires either four-dimensionalism (Jetix is a temporal worm that includes all its temporal parts) or a conventionalist stance (Jetix is defined by its role structure and creation graph, not its specific agent-instances). The latter is correct and already implicit in Levenchuk's role-abstraction.

---

## Section 2 — Holon Theory (Koestler + Extensions)

### 2.1 Koestler 1967: Ghost in the Machine

Arthur Koestler coined "holon" in *The Ghost in the Machine* (1967) from Greek *holos* (whole) + *-on* (part, as in proton, neutron). The core definition:

> Sub-wholes on any level of the hierarchy are referred to as holons. ([Koestler, 1969, panarchy.org](https://www.panarchy.org/koestler/holon.1969.html))

Key propositions from Koestler's axiomatic treatment:

- **(1.1)** An organism is not an aggregation of elementary parts nor a chain of elementary units of behaviour.
- **(1.2)** It is a multi-levelled hierarchy of semi-autonomous sub-wholes, branching into sub-wholes of lower order. Sub-wholes at any level = holons.
- **(1.3)** Parts and wholes in an absolute sense do not exist in domains of life. The holon reconciles atomistic and holistic approaches.
- **(1.4)** Biological holons are self-regulating open systems displaying both autonomous (whole) and dependent (part) properties. This dichotomy is the **Janus phenomenon** — holons face simultaneously inward (to their parts) and outward (to their containing whole), like the two-faced god Janus.
- **(1.5)** The term holon applies to any stable biological or social sub-whole with rule-governed behaviour. Examples: organelles, organs, fixed action-patterns, phonemes, words, individuals, families, tribes, nations.

The Janus-faced property is the most important concept for Jetix. Every L2 functional cluster (e.g., Sales Function) simultaneously:
- **Looks inward as a whole** — governs its L1 roles, sets their context, resolves intra-cluster coordination.
- **Looks outward as a part** — responds to L3 direction's goals, contributes outputs upward, cannot act contrary to the L4 Jetix charter.

**Self-assertive (S-A) vs Integrative (INT) tendencies** (Proposition 4.1):

> Every holon has the dual tendency to preserve and assert its individuality as a quasi-autonomous whole; and to function as an integrated part of an existing or evolving larger whole. ([Koestler, panarchy.org](https://www.panarchy.org/koestler/holon.1969.html))

The S-A tendency is the dynamic expression of wholeness; the INT tendency is the expression of partness. This polarity is universal across biology and social organization.

**Dynamic equilibrium** (Proposition 9.1): An organism or society is in dynamic equilibrium when the S-A and INT tendencies of its holons counterbalance each other. Disorder has two failure modes: (9.4) an over-excited holon "monopolizes functions, to the detriment of the whole" (S-A excess), and (9.5) "power of the whole over its parts erodes their autonomy" (INT excess leading to groupthink).

**Holarchy:** A hierarchy of holons. Koestler distinguishes holarchies from hierarchies: in a pure hierarchy, nodes are either pure parts or pure wholes. In a holarchy, every node is simultaneously whole-and-part. The term "holarchy" (not present in the 1969 paper excerpts but established in Koestler's broader work) was popularized by Ken Wilber.

### 2.2 Ken Wilber — Four Quadrants and Tetra-Arising

Wilber's *Sex, Ecology, Spirituality* (1995) extends Koestler's holons into an integral theory of all domains. Wilber's key addition: every individual holon has four irreducible dimensions, expressed as quadrants ([Integral Relationship](https://integralrelationship.com/11397-2/)):

| Quadrant | Label | Description |
|---|---|---|
| Upper Left (UL) | "I" (interior-individual) | Subjective experience, consciousness, intentionality |
| Upper Right (UR) | "It" (exterior-individual) | Physical form, observable behavior, brain states |
| Lower Left (LL) | "We" (interior-collective) | Shared culture, values, mutual understanding |
| Lower Right (LR) | "Its" (exterior-collective) | Social systems, institutions, infrastructure |

**Tetra-arising:** Every holon simultaneously enacts all four quadrants — interior and exterior, individual and collective. No quadrant can be reduced to another (contra reductionism) or ignored (contra flatland).

**Jetix application of four quadrants:** An L2 Sales Function holon has: (UL) the agent's "experience" model of sales context and strategy; (UR) the actual tool calls, CRM writes, and output tokens; (LL) the shared ontology between sales-lead role and Ruslan as strategic authority; (LR) the Jetix L4-delivery infrastructure, Toggl workspace, GitHub repos. Wilber's framework is useful as a *completeness check* — have you specified all four dimensions in a role manifest? Most solo-founder systems neglect LL (shared culture) and LR (infrastructure) in role design.

**Criticism:** Wilber's system becomes unwieldy when taken as a universal theory of everything. The quadrant model is a useful heuristic; its metaphysical foundations (Spirit, Absolute, evolutionary teleology) are not relevant for Jetix.

### 2.3 Related Frameworks

**Piero Mella's holonic revolution** describes organizations and societies as holonic hierarchies where each level adds genuine emergent properties. Mella emphasizes that holons are not just structural but *functional* — they enact goals that are not reducible to lower-level goals. This is directly relevant to the question of whether Jetix L4 has genuinely emergent properties beyond what L1 agents produce.

**Jantsch (The Self-Organizing Universe, 1980)** extended holarchy into self-organization theory. Jantsch argued that holarchies evolve through self-organization: new levels emerge when existing levels reach internal coherence thresholds. For Jetix, this suggests L3 business directions (e.g., shaurma-chains) emerge as genuine holons when they achieve internal self-regulation — not when Ruslan draws a box on an org chart.

**Maturana and Varela's autopoiesis:** Living systems are autopoietic — they continuously produce and maintain their own organization. Autopoiesis is a strong version of holonic self-assertion. An autopoietic holon doesn't merely maintain its boundaries — it *produces* them. For AI-native organizations, this maps to the question: can a Jetix L2 cluster self-maintain its own role manifests, update its own alphas, and reproduce its own operational patterns without Ruslan's intervention? This is the capability threshold for genuine organizational autonomy.

### 2.4 Holon vs System vs Whole — Distinctions

These terms are often conflated:

| Concept | Defining property | Part-whole structure |
|---|---|---|
| **Whole** (generic) | Has parts | May not be a part of anything |
| **System** | Emergent behavior from organized parts; lifecycle | Part of a supersystem (creation graph) |
| **Holon** | Simultaneously whole AND part; Janus-faced; semi-autonomous | Necessarily nested in holarchy |
| **Aggregate** | Collection of parts with no emergent property | Not a system; no integration |
| **Network** | Non-hierarchical connections between nodes | Horizontal, not hierarchical |

In Levenchuk's FPF, "system" and "holon" are not strictly synonymous. A system has a lifecycle and emergent properties; a holon emphasizes the dual whole/part nature. Levenchuk treats the mereological dimension (part-whole structure) and the systemic dimension (lifecycle, emergence) as complementary. The three-level creation graph (target system / creating system / supersystem) is specifically a *systemic* frame; the holarchy is specifically a *mereological* frame.

---

## Section 3 — Organizational Application

### 3.1 Sociocracy 3.0, Holacracy, Teal, Beyond Budgeting

**Holacracy** (Brian Robertson, developed at Ternary Software) is the most explicit application of holarchy to organizational governance. Holacracy structures organizations as nested circles (holons), with each circle simultaneously a whole (self-governing, with its own roles, purpose, accountabilities, and domains) and a part (of a broader circle) ([Reinventing Organizations Wiki](https://reinventingorganizationswiki.com/en/cases/holacracy/)). The anchor circle contains the entire organization. Key architectural features:

- Roles, not jobs: people fill multiple roles simultaneously; roles are defined by purpose + domains + accountabilities, not by personal identity.
- Double-link: each sub-circle sends a "rep link" upward and receives a "lead link" downward, creating bidirectional information flow.
- Governance meetings: separate from operational meetings; handle only role creation/amendment/removal.
- No titles: removing person-role fusion reduces the identity capture that causes S-A excess at the individual level.

Holacracy has been adopted by Zappos (famously, and controversially), HolacracyOne, and hundreds of smaller organizations. The Zappos experiment showed that the main failure mode is transition cost — established power-holders resist redistribution, and the constitutional process imposes significant overhead on small teams ([Integral Leadership Review](http://integralleadershipreview.com/5328-feature-article-organization-at-the-leading-edge-introducing-holacracy-evolving-organization/)).

**Sociocracy 3.0 (S3)** is a lighter-weight pattern library derived from Holacracy and sociocracy. Key organizational principle: "domains" as zones of authority, arranged in nested circles. S3 is more modular than Holacracy — organizations can adopt individual patterns without full constitutional implementation ([Sociocracy 3.0 Patterns](https://patterns.sociocracy30.org/organizational-structure.html)).

**Teal organizations** (Laloux, *Reinventing Organizations*, 2014) describe the developmental stage at which organizations exhibit self-management, wholeness, and evolutionary purpose. Teal is not a governance system but a *consciousness model* — it describes organizations that have internalized the holonic principle without necessarily using Holacracy's formal apparatus ([Laloux, reinventingorganizations.com](https://www.reinventingorganizations.com/uploads/2/1/9/8/21988088/140305_laloux_reinventing_organizations.pdf)). Teal practices: fluid granular roles, decentralized decision-making (advice process), peer-based performance, self-set salaries.

**Beyond Budgeting** (Hope & Fraser, 2003) dismantles fixed annual budgets in favor of rolling forecasts and relative performance benchmarks — an organizational application of holonic decentralization to financial control. Relevant for Jetix when L3 business directions achieve P&L autonomy.

### 3.2 Bureaucratic vs Holonic vs Network Structures

| Structure | Basis | Information flow | Composition principle | Failure mode |
|---|---|---|---|---|
| **Bureaucratic hierarchy** | Position authority | Top-down | Role = person | INT excess: rigidity |
| **Holonic / Holacracy** | Role authority | Bidirectional | Role ≠ person; circles nested | Governance overhead |
| **Network / DAO** | Peer authority | Horizontal | Emergent, task-based | S-A excess: coordination failure |
| **Jetix Model D** | Role authority + lifecycle | Bidirectional + asymmetric ref rule | Role = abstract (human or AI filler) | Risk: role manifest drift |

Jetix sits closest to the holonic model, with one critical extension: role-holders can be AI agents. This is not present in any of the organizational frameworks above — they all assume human role-fillers. The implications are explored in Section 4.

### 3.3 Holonic Manufacturing Systems (HMS) and the PROSA Architecture

The Holonic Manufacturing Systems (HMS) consortium (IMS program, 1990s) formalized holon theory for manufacturing control. The PROSA (Product-Resource-Order-Staff Architecture) reference architecture from KU Leuven (Van Brussel et al., 1998) defines three basic holons ([KU Leuven PROSA](https://www.mech.kuleuven.be/en/pma/research/MACC/prosapaper)):

- **Product holon:** Holds process and product knowledge — how to fabricate a product. Information server to other holons.
- **Resource holon:** Capabilities that can perform processes — machines, workstations, factories. Aggregated into resource holarchies (equipment → workstation → shop → factory).
- **Order holon:** Logistical entity — a specific request to produce a product. Negotiates with resource holons; coordinates with product holons for technical execution.
- **Staff holon** (optional): Expert advisor — centralizes knowledge without imposing rigid hierarchy. Provides advice that basic holons can follow or override.

PROSA is architecturally significant for Jetix because it demonstrates a proven pattern of holonic decomposition in a complex production system. The mapping:

| PROSA holon | Jetix analog |
|---|---|
| Product holon | Service/product specification (e.g., AI audit methodology) |
| Resource holon | Agent capabilities (sales-lead with CRM tools, strategy-lead with research tools) |
| Order holon | Client engagement / project instance |
| Staff holon | Strategic-management role (Ruslan) as advisor to execution agents |

PROSA also demonstrates that self-similar holarchy (equipment = resource holon, workstation = aggregated resource holon) reduces integration complexity — a new component slots into the same interface. This is precisely the promise of Jetix's role-manifest approach: a new agent (human or AI) fills an existing role without requiring architectural changes.

**Microservices as holons:** Domain-driven design (DDD) and microservice architectures apply similar principles at the software level. A bounded context in DDD is mereologically analogous to a holon — it has internal coherence, encapsulates its data model, and exposes a defined interface. Amazon's "two-pizza team" rule is a holonic composition criterion. Constellation Software (Mark Leonard) manages 500+ software businesses as near-autonomous holons within a corporate holarchy — each subsidiary retains its identity (S-A) while reporting financial performance upward (INT).

---

## Section 4 — AI Agent Systems

### 4.1 MAS Mereological Treatment

Multi-agent systems (MAS) literature provides the deepest academic treatment of agent-organization structure. Michael Wooldridge and Nicholas Jennings define agents by autonomy, social capability, reactivity, and pro-activeness. The key organizational insight from Wooldridge's Gaia methodology: a MAS can be architected as a computational organization, and the appropriate abstractions are roles, groups, and interaction protocols — not individual agent internals ([Gaia Methodology, Wooldridge](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/tosem2003.pdf)).

The AGR model (Agent/Group/Role, from Ferber, Gutknecht, Michel, AAMAS 2003) provides the most minimal mereological formalization of MAS organization:
- **Agent:** Individual, autonomous entity; provides and consumes services.
- **Group:** Collection of agents sharing a common context; groups can overlap and are the unit of organizational decomposition.
- **Role:** Abstract behavioral specification associated with a position within a group. A role defines constraints on behavior, not cognitive architecture — any agent (human or AI) that satisfies the constraints can fill the role.

AGR's mereological structure: agents compose groups (mereological composition), groups compose organizations (holarchic nesting). Roles are not parts but *functions* or *masks* that parts play — exactly Levenchuk's "role as mask" (маска роли) formulation ([ailev.livejournal.com/1776793](https://ailev.livejournal.com/1776793.html)).

Organization-Centered MAS (OCMAS) vs Agent-Centered MAS (ACMAS): ACMAS assumes agents define their own relationships; OCMAS starts with the organizational structure and treats agents as interchangeable role-fillers. Jetix is unambiguously OCMAS — role manifests define the organizational skeleton; specific Claude models fill roles and are replaceable.

### 4.2 LLM Agent Systems — Mereological Structures in Production

Modern LLM agent frameworks independently rediscovered holonic structure:

| Framework | Organizational metaphor | Mereological structure | Key mechanism |
|---|---|---|---|
| **CrewAI** | Human team (crews, roles) | Role-based hierarchical composition | Manager agent delegates to specialist agents |
| **LangGraph** | State machine / workflow graph | Graph-theoretic: nodes = agents, edges = transitions | Explicit state passed between nodes |
| **AutoGen** | Conversational group | Peer agents in group chat | Turn-taking dialogue, round-robin or LLM-selected |
| **Claude Code sub-agents** | Orchestrator-worker | Nested context windows | `.claude/agents/` definitions as role manifests |

Crucially, each of these frameworks implements a restricted version of holonic structure. LangGraph is the most explicit about boundaries (nodes have clear inputs/outputs). CrewAI's hierarchical process mode implements the PROSA staff-holon pattern: a manager agent "advises" specialist agents rather than commanding them ([Galileo.AI comparison](https://galileo.ai/blog/autogen-vs-crewai-vs-langgraph-vs-openai-agents-framework)).

**Anthropic's multi-agent research system** (published June 2025) describes the canonical production pattern: an orchestrator (lead agent, Claude Opus 4) spawns 3-5 subagents (Claude Sonnet 4) in parallel. Each subagent operates in its own context window with defined objective, output format, tool access, and task boundaries. The orchestrator decomposes the query into subtasks, distributes them, and synthesizes results ([Anthropic engineering blog](https://www.anthropic.com/engineering/built-multi-agent-research-system)). This is the Janus-face in practice: each subagent is a whole (complete context window, autonomous tool use) and a part (constrained by the orchestrator's decomposition, outputs consumed by the parent).

Anthropic's key design principles translate into mereological terms:
- "Teach the orchestrator how to delegate" = define the holonic boundary precisely (what belongs inside vs outside each holon).
- "Separation of concerns: distinct tools, prompts, exploration trajectories" = holonic encapsulation.
- "Subagent output to filesystem to minimize game of telephone" = reduce inter-holon communication overhead by specifying explicit interface contracts.
- "Scale effort to query complexity" = dynamic holarchy — number of nesting levels scales with task complexity.

**Known production costs:** Multi-agent systems use ~15x more tokens than chat ([Anthropic](https://www.anthropic.com/engineering/built-multi-agent-research-system)). This is the INT overhead — the cost of coordinating parts into a whole. Holonic decomposition is only justified when parallelization gain outweighs coordination cost.

### 4.3 Human+AI Ensembles, Role-as-Holon

The most important architectural insight for Jetix: **role is the correct unit of holonic composition, not the agent/person who fills it.** This is true in both Koestler (behavioral holons), Levenchuk (role as mask), AGR (role as abstract behavioral specification), and modern AI frameworks (role definitions as `.md` files independent of which model executes them).

This means:
- A role-holon (e.g., sales-lead) can be filled by Claude Sonnet 4 today, Claude 5 tomorrow, or a human contractor next year — the holonic structure is preserved.
- The mereological whole (Jetix L4) is invariant under role-filler substitution, as long as role manifests remain well-defined.
- Human+AI ensembles are mereologically equivalent to pure-human or pure-AI teams — the composition criterion is role-interface satisfaction, not biological vs silicon substrate.

**Federated AI-augmented business units:** At Jetix L3 scale (multiple business directions), each direction functions as a semi-autonomous holon with its own agent set, budget, and creation graph. The L4 Jetix charter defines the INT constraints (brand, financial reporting, legal); each L3 direction exercises S-A in its operational domain. This pattern mirrors Constellation Software's federated structure — except the "staff" within each holon are AI agents rather than human operators.

---

## Section 5 — Levenchuk's "Lightweight Mereology"

### 5.1 What Levenchuk Includes

Levenchuk's FPF (First Principles Framework) calls its foundational approach "мереология холонов" — mereology of holons. From his September 2025 post "Компактифицируем FPF" ([ailev.livejournal.com/1776793](https://ailev.livejournal.com/1776793.html)):

> За основу мы берём мереологию холонов (эпистем, дисциплин, систем, сообществ и т.д.). Холоны отличаются конструированием их из частей и входимостью в другие целые как части.

("We take as the foundation the mereology of holons — of epistemes, disciplines, systems, communities, etc. Holons are distinguished by being constructed from parts and by entering into other wholes as parts.")

What FPF actively includes:

**1. Holons as the primitive unit:** Not atoms (as in GEM's bottom-up approach) but holons — entities that are simultaneously whole-and-part. The partonomy (партономия) is the preferred structure: ordered multi-level hierarchy, not flat fusion.

**2. Role as mask (маска роли):** Roles are not separate holons but *masks* that holons wear in context. "Холон в некотором контексте играет роль (holon as a holder of a role), которая служит его 'маской'" — the role exposes some features of the holon's behavior in a given time window.

**3. Interface and encapsulation:** Holons expose interfaces that encapsulate internal assembly. The interface acts as an invariant at the holon's boundary — other holons interact only through the interface, not through internal parts. This is directly analogous to object encapsulation in OOP, but with explicit mereological grounding.

**4. Three-level creation graph (граф создания):** Target system / creating system (system-creator) / supersystem. The creation graph is "мереологически ориентирован" — oriented mereologically: creating systems are themselves systems that someone creates. The recursion is explicitly managed through the metaholon transition (метахолонный переход) concept.

**5. Constructor theory vocabulary (transformations, tasks):** Transformations in the creation graph are taken from constructor theory — "Transformations тут берутся из constructor theory." A creating system *transforms* inputs into the target system; the task specification defines possible/impossible transformations. This is the vocabulary only, not the full physical theory.

**6. Advanced mereology as structural apparatus:** Levenchuk calls the full framework "advanced mereology" and specifies that it involves: multi-type parthood (subtypes of part-whole relation), hierarchical kind-representation (partonomy organized by kinds/types), and the renormalization-group-style recursion of the metaholon transition. The CT2R-LOG and Kind-CAL architheories are referenced as providing the kind-typing apparatus.

**What FPF excludes from standard CEM/GEM:**
- Unrestricted composition (arbitrary fusions of any objects) — only intentional, lifecycle-relevant compositions are modeled.
- Extensionality as identity condition — holons can change parts without losing identity (the role-manifest persists through agent-filler changes).
- The flat "no preferred decomposition" stance of GEM — FPF explicitly privileges the hierarchical partonomy over flat fusion.

### 5.2 What Levenchuk Excludes (Kit Fine, Constructor Theory)

From his 2018 post on systems mereology ([ailev.livejournal.com/1451832](https://ailev.livejournal.com/1451832.html)), Levenchuk makes the exclusion explicit through a critique of standard philosophical mereology:

> Теоретическая мереология: красивые логические формулы, никакой связи с жизнью.

("Theoretical mereology: beautiful logical formulas, no connection to life.")

He argues via examples: a cow has a tail; a cow is part of a herd; therefore (by CEM transitivity) a herd has a tail. This is formally correct but "not systemic" (не системно) — it violates the engineer's intuition that composition should track causal-functional relevance, not formal transitivity alone.

**What specifically is excluded from Kit Fine's apparatus:**

1. **Qua-objects:** Fine's "thing qua playing a role" introduces intensional (abstract, formal) elements as genuine parts of hylomorphic compounds. For engineering purposes, the role-as-mask is sufficient — the role does not need to be ontologically added to the holon as a constituent part.

2. **Mereological coincidence as general principle:** Fine's claim that a statue and its clay are numerically distinct objects occupying the same location (because they differ in modal properties — the clay survives crushing; the statue does not) is philosophically sophisticated but creates ontological "clutter" in engineering models. Levenchuk adopts a single object with multiple roles (masks) rather than numerically distinct coincident objects.

3. **Full location pluralism:** Fine's (2006) defense of three-dimensionalism and location pluralism raises genuine puzzles about multi-located objects. These matter for physical objects; for software holons (which are routinely multi-located — same codebase runs on multiple servers), location-mereology harmony breaks down and the formal apparatus becomes misleading rather than helpful.

4. **Constructor theory as physics foundation:** Levenchuk imports constructor theory's vocabulary (tasks, transformations, constructors) but explicitly avoids importing its quantum foundations or its claims about the nature of information as physical. The creation graph uses "transformation" as a high-level organizational concept, not a claim about counterfactual physical possibilities.

**What specifically is excluded from standard academic mereology:**

- BFO (Basic Formal Ontology) — explicitly rejected ([ailev.livejournal.com/1451832](https://ailev.livejournal.com/1451832.html)) as "негодная онтология для инженерных задач" — inadequate ontology for engineering tasks, because it generates mereological monsters (a herd has a tail).
- Van Inwagen's organicism — excluded because it denies the existence of non-biological composites, which would eliminate all organizational holons.
- Pure extensionality — excluded because engineers need to discuss the same system at different lifecycle stages.

### 5.3 Rationale: Practicality vs Rigour

Levenchuk's position is that the full apparatus of philosophical mereology is designed to answer metaphysical questions (does the statue exist distinct from the clay?) that are not the questions engineers ask. Engineers ask: how do we decompose this system so that we can think clearly about its lifecycle, assign responsibilities, and track emergence? These questions require:

1. A *causally grounded* decomposition criterion (not arbitrary fusions).
2. A *lifecycle-aware* parthood relation (parts change; the whole persists).
3. A *multi-stakeholder* view of composition (different observers decompose differently, per their interests).
4. *Encapsulation* — ability to abstract away internal structure behind an interface.

None of these are addressed by CEM or Fine's hylomorphism. Levenchuk's "мереология холонов" is precisely a mereology designed around these engineering needs — hence "advanced" in the sense of going beyond academic mereology, not in the sense of being more formally elaborate.

---

## Section 6 — Beyond Levenchuk: Evaluation

### 6.1 Kit Fine's Mereology with Location

**What it is:** Fine's full mereological program adds three elements to standard mereology: (1) hylomorphism — form as a constitutive element of structured objects (not merely sum of parts); (2) qua-objects — object qua playing a role; (3) mereological coincidence — distinct objects at the same location with different modal profiles. Location mereology (from Hudson and the SEP entry) adds the Mereological Harmony principles linking object structure to spatial location.

**Jetix application — logical vs physical separation:**

The most potentially useful aspect of Fine's framework for Jetix is the distinction between logical and physical containment. In Model D, the Jetix holarchy is logically nested within Life-OS (Jetix is a part of Life-OS) but physically separated (different git repos, different SOPS keys, different Toggl workspaces). Fine's location pluralism — one object at multiple locations — captures this: Jetix-as-logical-entity "lives at" both its own repository and within Life-OS's structural accounting.

However, Hudson's mereological harmony principle (H5: x is part of y iff x's location is a subregion of y's location) is violated by Jetix/Life-OS structure: Jetix is logically part of Life-OS but physically not a subregion of Life-OS's filesystem. Fine's system handles this through multilocation, but the full apparatus is heavy.

**Honest cost-benefit for Jetix:**

| Aspect | Value | Cost |
|---|---|---|
| Logical/physical separation modeling | Medium: useful concept for explaining Model D | Low: just the vocabulary |
| Qua-objects for role modeling | Low: role-as-mask already sufficient | Medium: adds ontological complexity |
| Mereological coincidence for Jetix/Life-OS boundary | Low: asymmetric reference rule is simpler | High: requires tracking two numerically distinct objects per boundary zone |
| Full hylomorphism | Very low: software holons don't need Aristotelian form | High: requires redesigning all object models |

**Verdict:** Extract one concept only — "logical vs physical location" as a plain-language distinction. Skip the formal apparatus. Estimated value: 30 minutes to internalize the concept; no further investment warranted.

### 6.2 Constructor Theory (Deutsch/Marletto)

**What it is:** A meta-theory of physics that expresses laws as statements about which transformations (tasks) are possible vs impossible, and why. A *constructor* is an object that can cause a task and retain that ability. Knowledge is "causal information" that can act as a constructor. The constructor theory of life addresses how self-reproduction is compatible with physical law ([Quanta Magazine](https://www.quantamagazine.org/with-constructor-theory-chiara-marletto-invokes-the-impossible-20210429/)).

**Jetix application — creation graph transformations:**

Levenchuk already extracts the key useful fragment: the creation graph's "systems-creators transform inputs into target systems" is isomorphic to "constructors perform tasks on substrates." The possible/impossible distinction maps onto: what can a given agent cluster (constructor) produce (task) from given inputs (substrate)?

This has genuine operational value for Jetix:
- Defining an agent's *capabilities* as the set of tasks it can perform (possible transformations) vs tasks outside its domain (impossible).
- Modeling service offerings: "ai-consulting-dach can deliver AI audit (possible) but cannot deliver GDPR legal counsel (impossible for that constructor)."
- Creating graph-level constraints: if no current constructor can perform task T, Jetix needs to either build a new constructor (train/hire) or outsource (use an external constructor).

**Honest cost-benefit:**

| Aspect | Value | Cost |
|---|---|---|
| Task = possible/impossible transformation vocabulary | High: direct operational use for capability mapping | Low: one page of vocabulary |
| Constructor = creating system vocabulary | High: Levenchuk already uses this | Zero: already in FPF |
| Full quantum foundations of constructor theory | Zero for Jetix | High: requires physics education |
| Constructor theory of information (exact physical laws) | Zero operational value | Very high: academic physics |
| Constructor theory of life (self-reproduction) | Medium: interesting for autonomous agent systems | Medium: requires reading Marletto 2015 paper |

**Verdict:** Apply the possible/impossible transformation language immediately for capability mapping. Add to each role manifest: "Possible tasks: [list]. Out-of-scope tasks: [list]." Cost: 1 hour to implement across existing manifests. Skip the physics foundations entirely.

### 6.3 Category Theory

**What it is:** Category theory studies mathematical structures through objects (entities) and morphisms (structure-preserving maps between objects). A functor maps entire categories to each other while preserving compositional structure. A natural transformation maps between functors. Category theory abstracts away from the content of structures to study their relational patterns ([SEP Category Theory](https://plato.stanford.edu/archives/sum2000/entries/category-theory/); [Wikipedia](https://en.wikipedia.org/wiki/Category_theory)).

**Jetix application — functorial mappings between org states:**

The category-theoretic framing of organizations treats org states as objects and transitions between states (role changes, restructurings, scaling events) as morphisms. A functor between the "Jetix Phase 1 category" and "Jetix Phase 2 category" would be a structure-preserving map that shows which elements correspond across the two configurations. Natural transformations would describe how two different ways of scaling (e.g., adding human hires vs adding AI agents) relate to each other.

This is intellectually elegant. It is also operationally premature for a solo founder.

**Honest cost-benefit:**

| Aspect | Value | Cost |
|---|---|---|
| Objects/morphisms vocabulary for interface contracts | Low: "input → output" is sufficient | Low: already in role manifests |
| Functors for org-state transitions | Medium: useful at 50+ agents | High: requires category theory literacy |
| Natural transformations for comparing scaling strategies | Medium: useful for architectural decisions | Very high: requires advanced CT |
| Formal verification of interface contracts | High: at AI-native mega-corp scale | Extremely high: requires proof assistants |

**Verdict:** Defer entirely to Phase 3 (50+ agents, multiple companies). The conceptual return is real but the investment is not justified at current Jetix scale. If Ruslan is interested, the OMG's [category theory introduction for systems engineers](https://www.omg.org/maths/September-2024-Mathsig-Presentation-to-the-AI-PTF.pdf) is the entry point.

### 6.4 Granular Mereology and Vagueness

**What it is:** Granular mereology (Bittner & Stell, building on Smith) adds granularity levels to standard mereology — what counts as a part depends on the *granularity* at which you're looking. This handles the "carburetor is not directly part of the car" problem: at the coarse granularity of "car," the engine is a direct part; at fine granularity, the carburetor is a direct part of the engine. Vagueness in composition is handled through supervaluationism or tolerance margins ([SEP Ordinary Objects](https://plato.stanford.edu/entries/ordinary-objects/)).

**Jetix application — grey zones:**

Ruslan's "personal use of shared assets" is a canonical vagueness case. The Hetzner server hosts both `~/jetix-os/jetix/` and `~/jetix-os/life-os/`. Is the server a part of Jetix, a part of Life-OS, or a part of both? Granular mereology says: at the coarse granularity (infrastructure budget), the server is a part of the shared layer. At fine granularity (specific process), `jetix-ai-agent-2` is part of Jetix and `life-os-journal-backup` is part of Life-OS.

Similarly: Ruslan's time spent reading Levenchuk (improving both Jetix cognition and personal development). Granular mereology provides a principled account: at the coarse granularity, this is shared learning; at the fine granularity of work product, outcomes belong to the relevant holon.

**Honest cost-benefit:**

| Aspect | Value | Cost |
|---|---|---|
| Granularity vocabulary for shared asset classification | Medium: adds precision to grey-zone rules | Low: one concept |
| Formal granular mereology axioms | Low: existing heuristic (employee test) is sufficient | High: requires reading Bittner & Stell |
| Supervaluationism for vague composition | Low: practical rules are better than formal vagueness theories | Medium |

**Verdict:** Extract one concept: "granularity level determines part attribution." Apply as a practical rule: when classifying a shared asset, state the granularity at which the classification holds. Estimated implementation: add a "granularity context" field to grey-zone documentation. 30 minutes. Skip the formal apparatus.

---

## Section 7 — Practical Application Checklist

### 7.1 Definitely Apply (High Value, Low Cost)

**A. Koestlerian holon duality as a design principle**

Every role manifest should explicitly state: (a) S-A scope — what this holon governs autonomously, (b) INT obligation — what this holon contributes upward to the containing holon. When an agent "overasserts" (captures scope that belongs to a higher holon) or "overintegrates" (loses its autonomous judgment and defers everything), Koestler's 9.4/9.5 failure modes apply. Use this vocabulary in retrospectives.

**B. Three-level creation graph (target / creating / supersystem)**

Already in use as part of Levenchuk's FPF. This section confirms it is the correct operational mereological tool. Ensure every L3 business direction has an explicit creation graph: what is the target system (client deliverable), what is the creating system (which agents with which tools), what is the supersystem (market context + Jetix L4 charter).

**C. Role-as-mask / role-as-abstract-specification**

Role manifests should be written as if they will be filled by any competent executor — human or AI. This is already the Jetix pattern; the theoretical grounding confirms it is mereologically correct. The role is not a part of the holon; it is the mask the holon wears in a given context.

**D. Constructor theory vocabulary for capability mapping**

Add "possible tasks" and "out-of-scope tasks" to each role manifest. Frame Jetix's service offerings as constructor capabilities (possible transformations given inputs). Use this when onboarding new clients: match client needs against the possible-transformation set of current agent constructors.

**E. PROSA analogy for agent decomposition**

Use the order/product/resource/staff holon mapping when designing new business directions. Staff holons (Ruslan as strategic-management) give advice; they do not command. This is already the correct relationship but making it explicit reduces the risk of micromanagement patterns.

**F. Granularity vocabulary for grey-zone classification**

Add one field to shared-asset documentation: "granularity at which this belongs to Jetix / Life-OS / shared." Takes 30 minutes to retrofit existing grey-zone inventory.

### 7.2 Maybe Apply (Case-by-Case)

**G. Wilber's four-quadrant completeness check**

Use when writing a role manifest that feels incomplete. Check: have you specified (UL) the agent's internal model / reasoning approach, (UR) the observable output format and tools, (LL) the shared vocabulary and values with the stakeholder ecosystem, (LR) the infrastructure and external systems? If any quadrant is missing, the role manifest will produce systematic gaps. Cost: 15 minutes per manifest; only worthwhile for complex roles (strategic-management, product-lead).

**H. Autopoietic threshold as scaling criterion**

When evaluating whether an L2 cluster is ready for genuine autonomy (budget authority, independent hiring), apply the autopoiesis test: can this cluster maintain its own role manifests, update its own alphas, and reproduce its operational patterns without Ruslan's intervention? If yes, it has earned holonic autonomy. If no, it remains an operational cluster supervised by L4.

**I. Near-decomposability (Simon) for cognitive load management**

Herbert Simon's "Architecture of Complexity" (1962) showed that near-decomposable systems — where within-subsystem interactions are stronger than between-subsystem interactions — are cognitively tractable. Use this as a design heuristic: if agents in L2 cluster A are more tightly coupled to agents in L2 cluster B than within their own clusters, the cluster boundary is wrong. Redraw it.

**J. Kit Fine's logical/physical separation vocabulary**

When explaining Model D to a new team member, use Fine's distinction: Jetix and Life-OS are logically nested (Jetix is part of Ruslan's life) but physically separated (different repos, keys, workspaces). This makes the asymmetric reference rule intuitively clear. Cost: 5 minutes to incorporate into onboarding docs.

### 7.3 Probably Skip (High Cost, Low Value)

**K. Kit Fine's full hylomorphic mereology**

Qua-objects, mereological coincidence, and full hylomorphism are designed to solve the statue-clay problem — not organizational design problems. The role-as-mask framework covers everything Jetix needs from Fine's intuitions at a fraction of the cost.

**L. Constructor theory as physics**

The quantum foundations, counterfactual physics, and constructor theory of information are not relevant to business architecture. The vocabulary (tasks, constructors, transformations) is already imported through Levenchuk. Reading Deutsch (2013) or Marletto (2015) in full is a 40-hour investment with zero operational return at current Jetix scale.

**M. Category theory formalization**

Functors, natural transformations, and topos theory for organizations are genuinely powerful at scale (verified interface contracts, compositional system proofs) but require significant mathematical investment with no payoff until Jetix reaches Phase 3 complexity.

**N. Van Inwagen's organicism**

Van Inwagen's position that only organisms are genuine composites directly implies Jetix OS does not exist as an organizational whole. Philosophically interesting; operationally destructive. Acknowledge it exists as a critique; do not engage further.

**O. BFO (Basic Formal Ontology)**

Levenchuk explicitly rejects BFO for engineering use ([ailev.livejournal.com/1451832](https://ailev.livejournal.com/1451832.html)). It generates mereological monsters (a herd has a tail) and is not lifecycle-aware. Avoid despite its prevalence in biomedical informatics.

**P. Supervaluationism and formal vagueness theories**

The philosophical treatment of vague composition (sorites arguments, problem of the many) is interesting but the practical test ("if an employee would see this, it's Jetix") is more robust in daily use than formal vagueness theory.

---

## Section 8 — Risks of Over-Formalization

### The Academic Theatre Trap

The most dangerous misapplication of mereology and holon theory to Jetix is what Levenchuk calls "академический театр" — the use of formal vocabulary as performance rather than instrument. Symptoms: spending three hours designing the "correct" holarchic structure of a new business direction instead of getting the first client call done. Writing a formal Kit Fine-style mereological specification of the Jetix/Life-OS boundary when the practical rule ("would an employee see this?") already works.

Levenchuk's formulation is direct: "Beautiful logical formulas, no connection to life." The organizational mereology literature (BFO, formal upper ontologies, description logics for organizations) largely falls into this category — it is designed for large-scale ontology engineering with multiple teams and machine-readable constraints, not for a solo founder with a 12-agent AI system.

### Communication Breakdown

Introducing mereological vocabulary to collaborators — even AI agents — without contextualizing it creates friction. If a role manifest uses "qua-object" or "holarchic supplementation principle" without definition, an agent working from that manifest will either hallucinate interpretations or waste context window tokens on disambiguation. Levenchuk's vocabulary (холон, маска, граф создания, партономия) is the right level of formalism — precise enough to guide behavior, common enough to be unambiguous to a Claude agent working in systems-thinking context.

### Maintenance Burden

Formal mereological specifications age badly in fast-moving systems. A formally correct holarchic decomposition of Jetix in 2026 may become incorrect after a single pivot in 2027. The more formal the specification, the more expensive the update. Levenchuk's pragmatic answer: use role manifests as living documents; prefer lightweight constraints over formal axioms; update role manifests on a quarterly cycle rather than treating them as immutable formal specifications.

### The Scaling Cliff

Some frameworks become genuinely necessary at scale thresholds that Jetix has not yet reached:
- Category theory interface verification: relevant at 50+ independent agents with complex dependency graphs.
- Formal composition axioms: relevant when Jetix adds subsidiary companies (L3 directions become legal entities) and contract boundaries require machine-verifiable specifications.
- Full constructor theory: relevant if Jetix builds AI systems complex enough to require formal proof of capability bounds.

The risk is importing these frameworks prematurely, paying the adoption cost without accessing the benefit. Levenchuk's formulation: "FPF remains overkill for short-term projects, well-formalized domains, small teams with implicit culture." For Jetix Phase 1-2, FPF-Lite with the additions from Section 7.1 is the correct operating point.

### Levenchuk's Middle Path

Levenchuk's stance is not anti-formal — it is precision-calibrated. He uses "advanced mereology" as a term precisely because he is importing more than standard engineering part-whole thinking, but less than the full philosophical apparatus. The метахолонный переход (metaholon transition) concept, the kind-typing apparatus (CT2R-LOG), and the role-as-mask formalism are genuine theoretical additions that earn their place by solving specific engineering problems (recursion across levels, interface invariants, multi-stakeholder decomposition).

The principle: import exactly as much formalism as is needed to solve a specific problem that informal language cannot solve. No more. The moment a formalism becomes an end in itself — studied for its beauty rather than its operational utility — it has crossed into academic theatre and should be dropped.

---

## Section 9 — Resources

### Mereology

- [SEP Mereology, Achille Varzi](https://plato.stanford.edu/entries/mereology/) — definitive authoritative source; start here
- [SEP Location and Mereology, Gilmore et al.](https://plato.stanford.edu/entries/location-mereology/) — location theory and mereological harmony
- [SEP Ordinary Objects, Korman & Barker](https://plato.stanford.edu/entries/ordinary-objects/) — material constitution, Special Composition Question, vagueness
- Kit Fine, "Things and Their Parts," *Midwest Studies in Philosophy*, 23 (1999): 61–74 — hylomorphism and Monster Objection
- Peter van Inwagen, *Material Beings* (1990, Cornell UP) — Special Composition Question and organicism
- David Lewis, *Parts of Classes* (1991, Blackwell) — mereological universalism and set theory reform
- Nelson Goodman & Henry Leonard, "The Calculus of Individuals and Its Uses," *Journal of Symbolic Logic*, 5 (1940): 45–55 — classical accessible formulation
- Peter Simons, "Parts: A Study in Ontology" (1987, Oxford UP) — comprehensive treatment; includes engineering-relevant discussion

### Holon Theory

- Arthur Koestler, *The Ghost in the Machine* (1967, Hutchinson) — primary source; Part II (holons) is essential
- [Koestler's axiomatic propositions on holons (1969), panarchy.org](https://www.panarchy.org/koestler/holon.1969.html) — condensed axiomatic treatment
- Ken Wilber, *Sex, Ecology, Spirituality* (1995, Shambhala) — four-quadrant extension; Part I (holons)
- Piero Mella, "The Holonic Revolution: Holons, Holarchies and Holonic Networks" (2009, Pavia UP)
- Erich Jantsch, *The Self-Organizing Universe* (1980, Pergamon) — self-organization in holarchic systems
- Maturana & Varela, *Autopoiesis and Cognition* (1980, Reidel) — foundational autopoiesis theory

### Organizational Application

- Brian Robertson, *Holacracy: The New Management System for a Rapidly Changing World* (2015, Henry Holt) — practical constitutional system
- [Holacracy, Reinventing Organizations Wiki](https://reinventingorganizationswiki.com/en/cases/holacracy/) — overview and case studies
- [Sociocracy 3.0 patterns](https://patterns.sociocracy30.org/organizational-structure.html) — modular organizational patterns
- Frederic Laloux, *Reinventing Organizations* (2014, Nelson Parker) — Teal developmental model; [summary PDF](https://www.reinventingorganizations.com/uploads/2/1/9/8/21988088/140305_laloux_reinventing_organizations.pdf)
- Van Brussel et al., "PROSA: A Reference Architecture for Holonic Manufacturing Systems," *Computers in Industry*, 37 (1998) — HMS reference architecture; [KU Leuven](https://www.mech.kuleuven.be/en/pma/research/MACC/prosapaper)

### AI Agent Systems

- [Anthropic: How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/built-multi-agent-research-system) (2025) — production orchestrator-worker pattern
- Michael Wooldridge, *An Introduction to MultiAgent Systems* (2002, Wiley) — comprehensive MAS textbook
- Ferber, Gutknecht, Michel, "From Agents to Organizations: An Organizational View of MAS," *AAMAS 2003* — AGR model; [MaDKit](https://www.madkit.net/madkit/docs/articles/FromAgentstoOrganizations_AAMAS03_FerbGutMich.pdf)
- Wooldridge et al., "Gaia Methodology for Engineering Multi-Agent Systems," *TOSEM* (2003) — organization-centered MAS design; [Oxford CS](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/tosem2003.pdf)
- [ReadySolutions: Four Sub-Agent Orchestration Patterns (Claude)](https://readysolutions.ai/blog/2026-04-18-sub-agent-orchestration-patterns-claude/) — production patterns with Anthropic primitives
- [Galileo.AI: AutoGen vs CrewAI vs LangGraph vs OpenAI comparison](https://galileo.ai/blog/autogen-vs-crewai-vs-langgraph-vs-openai-agents-framework) — framework comparison

### Levenchuk / ШСМ

- [ailev.livejournal.com/1776793](https://ailev.livejournal.com/1776793.html) — "Компактифицируем FPF" (2025): holons, mereology, role as mask, constructor theory
- [ailev.livejournal.com/1451832](https://ailev.livejournal.com/1451832.html) — "Системная мереология" (2018): engineering vs philosophical mereology, critique of BFO
- Anatoly Levenchuk, "Системное мышление 2024" — [system-school.ru](https://system-school.ru)
- Anatoly Levenchuk, "Методология 2025" — [litres.ru](https://www.litres.ru/book/anatoliy-levenchuk/metodologiya-2025-71307523/chitat-onlayn/)
- [FPF problem-solving skill (GitHub)](https://github.com/CodeAlive-AI/fpf-problem-solving-skill) — FPF as agent prompt
- [ailev.livejournal.com/1798285](https://ailev.livejournal.com/1798285.html) — МИМ-2026 conference notes: FPF + AI agents

### Constructor Theory

- David Deutsch, "Constructor Theory," *Synthese*, 190 (2013): 4331–4359 — foundational paper
- Chiara Marletto, [Edge.org interview on constructor theory](https://www.edge.org/conversation/chiara_marletto-formulating-science-in-terms-of-possible-and-impossible-tasks) — accessible overview
- [constructortheory.org](http://constructortheory.org) — papers and overview

---

## Bibliography

- Koestler, Arthur. *The Ghost in the Machine*. Hutchinson, 1967. [Condensed axioms: panarchy.org/koestler/holon.1969.html](https://www.panarchy.org/koestler/holon.1969.html)
- Varzi, Achille. "Mereology." *Stanford Encyclopedia of Philosophy*, 2003, rev. 2019. [plato.stanford.edu/entries/mereology](https://plato.stanford.edu/entries/mereology/)
- Gilmore, Cody, Claudio Calosi, and Damiano Costa. "Location and Mereology." *SEP*, 2013, rev. 2021. [plato.stanford.edu/entries/location-mereology](https://plato.stanford.edu/entries/location-mereology/)
- Korman, Daniel Z. and Jonathan Barker. "Ordinary Objects." *SEP*, 2011, rev. 2023. [plato.stanford.edu/entries/ordinary-objects](https://plato.stanford.edu/entries/ordinary-objects/)
- Fine, Kit. "Things and Their Parts." *Midwest Studies in Philosophy*, 23 (1999): 61–74. [academia.edu/114589867](https://www.academia.edu/114589867/Things_and_Their_Parts)
- Van Inwagen, Peter. *Material Beings*. Cornell University Press, 1990.
- Lewis, David. *Parts of Classes*. Blackwell, 1991.
- Leonard, Henry and Nelson Goodman. "The Calculus of Individuals and Its Uses." *Journal of Symbolic Logic*, 5 (1940): 45–55.
- Wilber, Ken. *Sex, Ecology, Spirituality: The Spirit of Evolution*. Shambhala, 1995.
- Mella, Piero. *The Holonic Revolution*. Pavia University Press, 2009.
- Van Brussel, H., et al. "PROSA: A Reference Architecture for Holonic Manufacturing Systems." *Computers in Industry*, 37 (1998): 255–274. [kuleuven.be/pma/research/MACC/prosapaper](https://www.mech.kuleuven.be/en/pma/research/MACC/prosapaper)
- Wooldridge, Michael. *An Introduction to MultiAgent Systems*. Wiley, 2002.
- Wooldridge, Michael, et al. "Gaia Methodology." *ACM TOSEM*, 12/3 (2003). [cs.ox.ac.uk](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/tosem2003.pdf)
- Ferber, Jacques, Olivier Gutknecht, and Fabien Michel. "From Agents to Organizations." AAMAS 2003. [madkit.net](https://www.madkit.net/madkit/docs/articles/FromAgentstoOrganizations_AAMAS03_FerbGutMich.pdf)
- Robertson, Brian. *Holacracy*. Henry Holt, 2015. [reinventingorganizationswiki.com](https://reinventingorganizationswiki.com/en/cases/holacracy/)
- Laloux, Frederic. *Reinventing Organizations*. Nelson Parker, 2014. [reinventingorganizations.com](https://www.reinventingorganizations.com)
- Deutsch, David. "Constructor Theory." *Synthese*, 190 (2013): 4331–4359. [constructortheory.org](http://constructortheory.org)
- Anthropic. "How We Built Our Multi-Agent Research System." June 2025. [anthropic.com/engineering/built-multi-agent-research-system](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- Levenchuk, Anatoly. "Компактифицируем FPF" (Compactifying FPF). September 2025. [ailev.livejournal.com/1776793](https://ailev.livejournal.com/1776793.html)
- Levenchuk, Anatoly. "Системная мереология" (Systems Mereology). October 2018. [ailev.livejournal.com/1451832](https://ailev.livejournal.com/1451832.html)
- Simon, Herbert. "The Architecture of Complexity." *Proceedings of the American Philosophical Society*, 106/6 (1962): 467–482.

---

## Glossary

**English → Russian / Russian → English** (philosophical and Levenchuk-specific terms)

| English | Russian | Definition |
|---|---|---|
| Mereology | Мереология | Theory of part-whole relations; from Greek μερος (meros, part) |
| Part-whole relation | Отношение часть-целое | The basic relation studied in mereology; Pxy ("x is part of y") |
| Proper part | Собственная часть | A part that is not identical to the whole: PPxy = Pxy ∧ ¬(x=y) |
| Fusion / Mereological sum | Мереологическая сумма | The minimal whole containing given parts |
| Composition | Композиция | Formation of a whole from parts; upward direction |
| Decomposition | Декомпозиция | Analysis of a whole into parts; downward direction |
| Extensionality | Экстенсиональность | Principle: distinct wholes cannot have identical proper parts |
| Atomism | Атомизм | Doctrine that all things ultimately decompose into atoms (partless elements) |
| Gunk (atomless mereology) | Гань / безатомная мереология | Every part has proper parts; no atoms |
| Special Composition Question | Вопрос специальной композиции | "Under what conditions do some things compose a whole?" (van Inwagen) |
| Holon | Холон | Entity that is simultaneously whole and part; coined by Koestler 1967 |
| Holarchy | Холархия | Hierarchy of holons; each node is simultaneously whole and part |
| Partonomy | Партономия | Ordered hierarchical part-whole structure (Levenchuk's preferred term for holarchic structure) |
| Janus-faced property | Янус-эффект / феномен Януса | Holons face inward (as whole) and outward (as part) simultaneously |
| Self-assertive tendency | Самоутверждающая тенденция (С-У) | Holon's drive to preserve its autonomous wholeness |
| Integrative tendency | Интегративная тенденция (ИНТ) | Holon's drive to function as part of the larger whole |
| Hylomorphism | Гиломорфизм | Aristotelian/Finean doctrine: objects = matter + form; form is constitutive |
| Qua-object | Ква-объект | Object qua playing a role (Fine): x qua being-a-statue |
| Mereological coincidence | Мереологическое совпадение | Two distinct objects at the same location (Fine): statue ≠ clay despite same location |
| Role | Роль | Abstract behavioral specification; a "mask" a holon wears in context |
| Role as mask | Маска роли | Levenchuk: роль как маска холона — the role exposes selected features of the holon |
| Creation graph | Граф создания | Three-level graph: целевая система / система-создатель / надсистема |
| Target system | Целевая система | The system being created; the deliverable |
| Creating system | Система-создатель | The system that creates; constructors + their methods |
| Supersystem | Надсистема | The environment/context within which the target system operates |
| Metaholon transition | Метахолонный переход | Levenchuk: recursive cross-level reasoning analogous to renormalization group |
| Advanced mereology | — (Levenchuk's term, used in English in source) | Levenchuk's engineering mereology: causally grounded, lifecycle-aware, kind-typed |
| Meronomy / meronymic relation | Меронимическая связь | Linguistic/ontological term for part-of relation (esp. in natural language processing) |
| Constructor | Конструктор (CT) | An object that causes a transformation task and retains that capability |
| Task | Задача (CT) | Abstract specification of transformation as input-output pair of attributes |
| Possible/impossible transformation | Возможное/невозможное преобразование | Core constructor theory: what can/cannot be caused by a constructor |
| Interface | Интерфейс | Boundary specification of a holon that encapsulates its internal structure |
| Encapsulation | Инкапсуляция | Hiding internal assembly behind interface invariants |
| Near-decomposability | Квазиразложимость | Simon: within-subsystem interactions >> between-subsystem interactions |
| Autopoiesis | Аутопоэзис | Self-producing/self-maintaining system (Maturana/Varela) |
| Teal organization | Бирюзовая организация | Laloux's developmental model: self-management, wholeness, evolutionary purpose |
| Holacracy | Холакратия | Robertson's constitutional holarchic governance system |
| AGR model | АГР-модель | Agent/Group/Role — minimal organizational MAS model (Ferber et al.) |
| PROSA | ПРОСА | Product-Resource-Order-Staff Architecture for Holonic Manufacturing Systems |
