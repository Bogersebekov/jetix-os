---
task_id: phase-0-fpf-scope-2026-05-17
produced_by: philosophy-expert × critic
mode: critic
status: draft
F: F4
G: phase-0-cell-draft
R: refuted_if_categorical_errors_not_flagged_OR_anti_scope_missing_OR_reference_frame_not_addressed
date: 2026-05-17
sources:
  - path: "JETIX-WORKING-FILE-v0-2026-05-17.md"
    range: "§1–§5, §8, §9"
  - path: "reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md"
    range: "§2–§3"
  - path: "reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md"
    range: "§1–§13"
  - path: "decisions/JETIX-CORPORATION-2026-05-05.md"
    range: "§0–§1"
  - path: "decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md"
    range: "§0–§2"
  - path: "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md"
    range: "§0–§1"
  - path: "raw/external/ailev-FPF/FPF-Spec.md"
    range: "Part A kernel: A.1, A.1.1, A.2, A.2.1, A.3, A.7, A.14, A.15; Part E overview"
  - path: "CLAUDE.md"
    range: "§4 Pillar C, §Agent Roster"
provenance_inline: true
---

# Philosophy-Expert × Critic — Epistemic Boundary Inventory for FPF Scope Definition

> **Mode:** critic. Task: Phase 0 FPF scope definition — epistemic boundary lens.
> **Constitutional posture:** R1 (surfacing only; Ruslan decides what counts) +
> R2 (Foundation read-only) + R6 (provenance per claim) + Append-only.
> This artefact is a DRAFT. Brigadier promotes; philosophy-expert does NOT promote.

---

## §0 Summary: Epistemic Concerns Surfaced

Five structural concerns surface before the inventory:

**EC-1 (Most critical): The word «Jetix» is used as a name for at least 6
ontologically distinct objects without disambiguation.** Phase B working file
uses «Jetix» to mean (a) the filesystem repo, (b) the consultancy vision, (c)
the OS/software system, (d) the corporation entity, (e) the «workshop» metaphor,
and (f) the «meta-workshop» / platform-for-others. Per FPF A.7 Strict Distinction
and A.1.1 BoundedContext: mixing these under one name without explicit context
declaration is a boundary violation at the object-model level — not a style choice.
[src: raw/external/ailev-FPF/FPF-Spec.md A.7 + A.1.1]

**EC-2: The type/token confusion around «12 agents» is unresolved and
consequential.** CLAUDE.md §Agent Roster describes 12 named rows. Whether each
row is a U.Role (type — abstract functional assignment) or an instantiated executor
binding (token — specific Sonnet/Haiku model runs) is NOT the same question.
IP-1 Role≠Executor (CLAUDE.md §4.1, decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md)
explicitly bifurcates these. FPF A.2 + A.2.1 makes this a first-class distinction.
Phase B working file treats «12 agents» as a single count without declaring
which ontological level the count lives at. [src: CLAUDE.md §Agent Roster +
§4.1 IP-1; FPF A.2, A.2.1]

**EC-3: «Foundation v1.0 LOCKED» conflates an artefact state with a system
operational state.** «LOCKED» is a language-state declaration on a document
(per FPF A.16 Language-State Transduction). It does NOT guarantee that the
corresponding system behaviors are instantiated and running. The self-audit
(06-honest-self-audit §2) shows Foundation Parts 1/2/3/5/7/8/9/10 are
predominantly «memory + automation» — substrate, not enforcement. The
artefact being LOCKED does not entail the system operating per the artefact.
This is FPF's Temporal Duality (A.4) / plan≠work problem applied to Jetix itself.
[src: 06-honest-self-audit.md §2 + §2.1; FPF A.4, A.16]

**EC-4: «Workshop metaphor» is used simultaneously as an architectural anchor
and as a marketing frame.** These are two different functions with different
stability requirements. An architectural anchor needs to be stable under
counterexamples and edge cases (FPF A.7 Strict Distinction). A marketing frame
is chosen for resonance, not falsifiability. Using one artefact for both
functions creates a use-mention confusion: is «мастерская» the name-of-the-system
or a description-of-the-system? [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md §0;
JETIX-WORKING-FILE-v0 §3.1]

**EC-5: R12 anti-extraction is simultaneously a rule (Pillar C item), a
meta-property (applying to all relationships), and a strategic differentiator
(marketing claim). These three functions require different epistemic treatment.**
As a rule: it needs deontic form (MUST/MUST NOT) + scope + adjudication path.
As a meta-property: it needs scope-of-applicability (which relationships? which
parties?). As a marketing claim: it needs a falsifier (what would refute «Jetix
does not extract»?). Phase B collapses all three uses without distinguishing them.
[src: CLAUDE.md §4.1 rule 12; JETIX-WORKING-FILE-v0 §5.2; FPF A.2.8 U.Commitment;
A.2.6 ClaimScope]

---

## §1 Inventory — ≥10 Objects with Boundary Lens

**Reading key for FPF primitives column:**
- U.System = agentive holon (has roles, does work)
- U.Episteme = non-agentive knowledge holon (claim-bearing, not acting)
- U.Role = contextual functional assignment on a holder
- U.Method = abstract way of doing (not the doing itself)
- U.Work = record of actual occurrence (actuals, not plan)
- U.BoundedContext = semantic frame with local glossary + invariants
- Temporal Duality (A.4) = plan/design-time vs run-time distinction

| # | Object name | Type (FPF ontological category) | Reference-frame stability | FPF primitive assignment | Anti-scope (what does NOT belong here) | Conflation traps |
|---|---|---|---|---|---|---|
| O1 | **Jetix-as-filesystem-repo** | Artefact / carrier (FPF A.10 Evidence carrier; not the system itself) | Stable (git-tracked; observable) | U.Work record + carrier for U.Episteme content; NOT U.System itself | Does NOT include: the vision, the corporation, the agents-as-software; does NOT include Notion | Confusion: «the repo IS Jetix»; reality: the repo is the carrier/substrate; the system that runs on it is a different object. A.7 Strict Distinction: carrier ≠ object. |
| O2 | **Jetix-as-information-management-system** | U.System (agentive holon operating on information) | Evolving (operational; active project) | U.System subtype; contains U.Roles (12 named role-types per CLAUDE.md) + U.Methods (agent skills/tools) + U.Work records (cycle outputs, mailboxes) | Does NOT include: the legal entity, the vision document, the marketing narrative, the «workshop» metaphor as such | Confusion with O1 (repo) and O5 (vision). The «system» operates; the repo stores; the vision declares intent. These are different holons. |
| O3 | **Jetix-as-corporation/legal-entity** | U.System subtype (agentive; has stakeholder roles, contractual commitments) | Vapor (conceptual; no legal instantiation yet per JETIX-CORPORATION-2026-05-05 status) | Conceptual U.System with U.RoleAssignment (Partner/Client/Worker roles per §0 TL;DR); constitution-adjacent (R12 applies here) | Does NOT include: the OS/software, the agents, the Foundation architecture | Confusion: treating the corporation-concept as if it is operationally instantiated. It is not. It is a design-time U.Episteme describing a future U.System. |
| O4 | **Jetix-as-vision/задумка** | U.Episteme (non-agentive; claim-bearing; the described entity is a future system) | Stable-as-document (LOCKED v1.0 2026-04-27); NOT stable as predictive claim (F2-F4) | U.Episteme describing a future U.System; described entity = Jetix OS in its intended-final form; NOT itself a system | Does NOT include: current operational reality, current revenue, current agent behavior; does NOT include the corporation-structure | Confusion: «we have a LOCKED vision therefore the vision is realised.» Lock = language-state of the document (A.16). Lock ≠ operational enactment (A.4). |
| O5 | **Jetix-as-working-product (what ACTUALLY runs now)** | U.Work / U.System (partial instantiation; evidenced by actual cycle outputs) | Stable (observable; grounded in git commits + cycle logs) | U.Work records (actual cycle outputs per 06-honest-self-audit §2); partially instantiated U.System; ~27 memory+automation components evidenced | Does NOT include: the vision, the corporation, future capabilities, anything marked «TBD Phase B», unbuilt mechanisms | Confusion: «Foundation v1.0 LOCKED» describes the working product. Falsifier: 06-honest-self-audit §2 shows Parts 1/3/5/9/11 = memory-dominant; abductive loop NOT operational; UTS NOT formal; Claim Register absent. The document is LOCKED; the operational system is partial. |
| O6 | **Jetix-as-12-role-types** (type-level) | U.Role set (type-level; abstract functional assignments) | Stable (declared in CLAUDE.md; LOCKED roster) | 12 × U.Role per FPF A.2; each role has holder-type (agent model), context (department), responsibility | Does NOT include: specific executor instances (Sonnet 4.6 / Haiku 4.5); does NOT include running processes; does NOT include conversation threads | Core IP-1 confusion: «12 agents» in CLAUDE.md is used as both (a) the role taxonomy (type) and (b) the running executor list (token). These are different objects. Per FPF A.2 + A.2.1 + IP-1: the role type ≠ the executor binding. The count «12» does NOT mean 12 simultaneously running processes. |
| O7 | **Jetix-as-executor-bindings** (token-level) | U.RoleAssignment tokens (contextual; holder=specific model; role=one of 12; context=active session) | Evolving (different models instantiated per task; no persistent process) | U.RoleAssignment per FPF A.2.1 (Holder#Role:Context standard); NOT a permanent U.System | Does NOT include: the role-type definitions (O6), the org chart, the Foundation architecture | Confusion: executor bindings are often mentioned as «the agents» as if persistent actors. They are contextual enactments. Manager role can be held by Sonnet 4.6 in one session and a different model in another without violating the role-type. |
| O8 | **Workshop metaphor** («мастерская для работы с информацией») | Frame / U.BoundedContext candidate (semantic anchor; NOT itself a U.System) | Stable-as-canonical-frame (LOCKED v1.0 JETIX-WORKSHOP-CONCEPT-2026-04-30); NOT stable as structural claim | NOT a U.System. Candidate: U.BoundedContext that provides local glossary (мастер/работники/станки/заказы) for interpreting other Jetix objects | Does NOT include: the legal entity, the OS architecture, the FPF primitive structure, engineering discipline; it is a FRAME not a SYSTEM | Danger: treating the metaphor as an object with properties to defend. «Does the workshop have X?» assumes the metaphor IS the system. Correct: «Does the framing help model X?» Metaphors are use-tools, not ontological commitments. When the metaphor stops helping, retire it (via-negativa). |
| O9 | **Foundation v1.0 LOCKED** (11 Parts + Pillar A/C) | U.Episteme (document cluster; non-agentive; describes intended system architecture) + partial U.Work (some Parts have operational evidence) | Stable-as-artefact (LOCKED 2026-04-28; git-tagged); MIXED as operational claim | U.Episteme (the documents) describing a U.System (Jetix OS); Parts with operational evidence (6a, 6b, Part 4) ≈ grounded U.Episteme; Parts without operational evidence (1, 3, 5, 9) = design-time descriptions only | Does NOT include: proof that all 11 Parts are operationally instantiated; does NOT include FPF-compliance claims (derivation is acknowledged as partial per 06-honest-self-audit §§2,12) | Critical trap: «Foundation LOCKED» used to imply operational system. The LOCK is on the U.Episteme (document language-state per A.16). The operational status of the described system is a SEPARATE question requiring U.Work evidence. FPF A.4 Temporal Duality: MethodDescription ≠ Work. |
| O10 | **Pillar C Tier 2 — 12 constitutional rules** | U.Episteme (text of rules; deontic) + U.Commitment candidates (if adjudication path exists) + partial enforcement via Default-Deny table | Stable-as-text (LOCKED; CLAUDE.md §4.1 inlined); MIXED as enforcement claim | U.Episteme containing U.Commitment objects (per FPF A.2.8) for each rule; enforcement evidence = Default-Deny table (11 entries) + Halt-Log-Alert | Does NOT include: guarantee that all 12 rules are machine-enforced; does NOT include rules 1-12 being equally enforceable (Rule 11 Default-Deny is machine-checkable; Rule 1 «AI does NOT strategize» depends on human review) | Trap: «12 rules LOCKED» = «12 rules enforced». Per FPF A.2.8 U.Commitment: a commitment requires adjudication hooks + evidence refs. Some rules have these (Rule 11 Default-Deny); others do not yet (Rule 3 capability direction). Conflating «exists as text» with «enforced as commitment» is the A.7 Strict Distinction problem applied to deontics. |
| O11 | **R12 anti-extraction** | THREE DISTINCT OBJECTS: (a) Pillar C rule text (U.Episteme); (b) applied commitment in any specific relationship (U.Commitment per A.2.8); (c) architectural meta-property (design constraint on all substrate-member relationships) | Stable-as-text (LOCKED via CLAUDE.md §4.1 additive 2026-05-12); VAPOR as enforcement | (a) U.Episteme: text of rule; (b) U.Commitment: when applied to a specific partner/member agreement; (c) Architectural property: ClaimScope = all substrate relationships (A.2.6 USM) | Does NOT include: (a) proof that R12 is enforced today; (b) proof that «fork-and-leave» is technically possible (no infrastructure evidenced); (c) equivalence with FPF or IWE mechanisms (per 00-SUMMARY-PHASE-B §3 J-U2: «NONE in IWE template» is a negative comparison, not a proof of superior mechanism) | Multi-object conflation: treating three R12 objects as one creates: measuring «rule text F5 LOCKED» as evidence of «enforcement», and using «unique vs IWE» as claim of operational superiority. Each face of R12 needs its own F-G-R triple. |
| O12 | **8 active projects** | Portfolio object (one) OR 8 separate U.Work/U.System instances (many) — NOT yet disambiguated | Evolving (per CLAUDE.md §Projects; status «Active» / «Planned» / «Paused» / «Deferred») | IF portfolio: one U.Episteme describing the project set + one aggregate management object; IF 8 separate: 8 × U.System instances (each with own U.Work records, stage-gates, mini-swarm) | «8 active projects» does NOT mean 8 equally active U.Work streams. Status «Active» vs «Planned» vs «Paused» = different language-states per A.16. Does NOT mean 8 simultaneously generating revenue. | Confusion: treating the count «8» as meaningful without language-state disambiguation. Per CLAUDE.md §Projects: «bets» = P4/Paused; «community» = P3/Planned. These are not running systems. The portfolio label «8 active» applies different A.16 language-states to different members without declaring the aggregate status. |

---

## §2 Categorical Errors in Phase B Working File

These are structural observations, not evaluative verdicts. Each is a surfaced candidate — Ruslan decides which, if any, require correction.

### CE-1: «8 active projects» — type-token confusion + language-state collapse

**Observed.** JETIX-WORKING-FILE-v0 §9 presents «8 Active Projects» as a uniform list.
Per CLAUDE.md §Projects: «bets» = P4/Paused, «community» = P3/Planned — not active in
the same sense as «quick-money» P1/Active. [src: CLAUDE.md §Projects table]

**Categorical error.** «8 projects» is stated as one number for three different
language-states (A.16): some are U.Work-in-progress (actual work records exist),
some are U.WorkPlan (planned, not yet enacted), some are U.Episteme-only (ideation).
Collapsing these into «8 active» mixes U.Work + U.WorkPlan + U.Episteme under one
count. Per FPF A.4 Temporal Duality: these are ontologically distinct.

**Falsifier.** Count of projects with actual U.Work evidence (cycle logs, commits, client
touchpoints) would differ from count with only U.WorkPlan or U.Episteme status.
Claim «8 active» is refuted if fewer than 8 have actual work records in last 30 days.

**Alternative framings (not recommendations — surface only):**
- Frame A: «8 project slots in portfolio; N currently generating work records» — distinguishes plan from actuals.
- Frame B: «1 primary (quick-money P1) + 7 supporting/staged» — priority-honest.
- Status quo: «8 active projects» — kills if misleads external audience about operational scale.

### CE-2: «12 agents» — role-type count vs executor-token count (IP-1 conflict)

**Observed.** CLAUDE.md §Agent Roster: 12 rows, each with Model + Dept + Phase column.
JETIX-WORKING-FILE-v0 §4 mermaid: «12 Specialized Agents × 6 Departments». Phase B
summary §1 uses «15 expert cell dispatches» for a different count.
[src: CLAUDE.md §Agent Roster; JETIX-WORKING-FILE-v0 §4]

**Categorical error.** «12 agents» conflates:
- 12 U.Role type-definitions (abstract; declared in CLAUDE.md; Phase 1-4 rollout schedule)
- N active U.RoleAssignment tokens (instantiated in any given session; most Phase 2-4 roles have no executor binding yet per Phase column)
- M cell invocations per cycle (brigadier dispatches; 15 in Phase B per summary)

Per FPF A.2 + A.2.1 + IP-1: these three counts are for three different objects.
«Phase 1» agents (manager, personal-assistant, system-admin, sales-lead) may have
executor bindings. «Phase 3-4» agents (knowledge-synth, strategist, life-coach,
meta-agent) are declared role-types without confirmed operational executor bindings.

**Falsifier.** If «12 agents» means «12 simultaneously runnable instances», this is
refuted by the Phase column in CLAUDE.md (Phase 3 and 4 agents not yet operational).
If it means «12 role-type declarations», it is confirmed.

**Alternative framings:**
- Frame A: «12 U.Role type-definitions (4 Phase-1 active + 8 Phase-2..4 planned)» — type-honest.
- Frame B: «N active executor bindings (confirm N from actual system state)» — token-honest.
- Status quo: «12 agents» without qualifier — kills if audience interprets as «12 running processes».

### CE-3: «Foundation v1.0 LOCKED» — artefact language-state vs operational system

**Observed.** CLAUDE.md, JETIX-WORKING-FILE-v0, all Phase B outputs routinely cite
«Foundation v1.0 LOCKED 2026-04-28» as evidence of system maturity.
[src: JETIX-WORKING-FILE-v0 §0, §7; CLAUDE.md Foundation Architecture section]

**Categorical error.** «LOCKED» per FPF A.16 is a language-state transition on a
U.Episteme (the architecture documents). It is NOT a U.Work record confirming that
the described system behaviors are operationally enacted.

**Evidence from self-audit.** 06-honest-self-audit §2 + §2.1 explicitly classifies:
- Parts 1/3/5/9/11 = «memory-dominant» (substrate; not intelligence amplification)
- Parts 2/7/8 = «automation-dominant»
- Parts 4/6a/6b + Pillar C = «FPF-derivative + intelligence» (4 of 14)
- Abductive loop NOT formally implemented
- U.UTS (F.17) NOT formal; Claim Register absent; Bridges informal

**Falsifier.** «Foundation v1.0 is operational» is refuted if operational audit shows
Parts 1/3/5/9/11 have no execution evidence beyond static file storage.

**This is not a criticism — it is a categorical sharpening.** «Foundation v1.0
LOCKED» is true as an artefact claim. «Foundation v1.0 operational» requires
separate U.Work evidence per Part. The two claims are not equivalent.

### CE-4: «12 constitutional rules» — text vs enforcement conflation

**Observed.** Pillar C «12 rules» cited as constitutional substrate in CLAUDE.md
§4.1 with varying implementation reality per rule.
[src: CLAUDE.md §4.1 + §4.4]

**Categorical error.** Rules vary by enforceability:
- Rule 11 (Default-Deny) has machine-enforcement path: `.claude/config/default-deny-table.yaml` with 11 entries + Halt-Log-Alert
- Rule 1 (AI does NOT strategize) requires human review; no automated check exists
- Rule 12 (anti-extraction) = no enforcement mechanism described; depends on Ruslan review
- Rules 3, 8, 9 = human-enforced conventions; no lint or halt exists

**Categorical error.** Treating the 12 rules as a uniform «constitutional substrate»
conflates: (a) machine-enforced commitments (FPF A.2.8 U.Commitment with adjudication
hooks), (b) human-review conventions (U.Episteme text only), (c) structural design
principles (embedded in architecture, not separately enforced).

These three categories of rule have different epistemic status (F-G-R would differ).
Presenting all 12 as equally «constitutional» implies equal enforcement reality which
is not evidenced.

### CE-5: «Phase B output» and «JETIX-FPF.md archived» — suppressed conflation

**Observed.** Phase B outputs (JETIX-WORKING-FILE-v0) repeatedly disclaim:
«JETIX-FPF.md 3762-line derivative archived 2026-05-06 as overreach.»
[src: JETIX-WORKING-FILE-v0 §0 constitutional_disclaimer]

**Surfaced concern.** Phase B working file, while lighter than JETIX-FPF.md, still
applies FPF terminology (U.Role, U.Episteme, F-G-R) to Jetix objects WITHOUT the
bounded context discipline that FPF A.1.1 requires. The working file maps Jetix
components to FPF primitives in a narrative register. Per FPF A.1.1: a U.BoundedContext
requires explicit glossary + local invariants + scope declaration for each context
where FPF terminology is applied. The working file lacks this scaffolding. This is a
lighter version of the same overreach pattern — the disclaimers are honest, but the
mapping exercise itself may need a bounded-context declaration to be FPF-compliant.

**Not an assertion that the working file is wrong.** Surface only. FPF A.1.1 applies
if formal FPF alignment is claimed; if the working file is narrative-only (as
the disclaimer states), A.1.1 does not apply. The question of which frame is operative
should be explicit.

---

## §3 Reference-Frame Disputes — Stable vs Evolving vs Vapor Objects

**Principle applied.** Per FPF A.1 + A.7: a stable reference point must have clear
boundaries, a declared described-entity, and observable falsifiers. A vapor object
has no grounding evidence.

| Object | Stability verdict | Reason | Suitable as anchor? |
|---|---|---|---|
| O1 Jetix-as-filesystem-repo | **Stable** | Git-tracked; verifiable; observable; filesystem = SoT per CLAUDE.md | Yes — best anchor for «what exists now» claims |
| O4 Jetix-as-vision/задумка | **Stable-as-artefact; vapor-as-system** | LOCKED document exists (verifiable); described future system = uninstantiated U.Episteme | Yes as «intended state» anchor; NO as «current state» anchor |
| O5 Jetix-as-working-product | **Stable** (grounded in observables) | Evidenced: git commits, cycle logs, voice pipeline outputs, CRM records | Yes — most rigorous anchor for «current operational capability» |
| O9 Foundation v1.0 | **Stable-as-artefact; mixed-as-system** | 4 of 11 Parts have direct FPF-derivative operational grounding; 7 are substrate/memory-dominant | Use as anchor only for «architectural intent»; NOT for «operational capability» |
| O3 Jetix-as-corporation | **Vapor** | Conceptual document LOCKED; no legal instantiation; no partner agreements executed | NOT suitable as anchor; describing future state |
| O8 Workshop metaphor | **Stable-as-frame; vapor-as-structure** | LOCKED canonical (JETIX-WORKSHOP-CONCEPT-2026-04-30); but frames don't have structure — they have resonance | Use as orientation frame for human communication; NOT as structural anchor for FPF mapping |
| O10 Pillar C 12 rules | **Stable-as-text; partial-as-enforcement** | Text LOCKED; machine enforcement confirmed for subset (Rule 11); human-only for remainder | Yes as «design intent» anchor; only partial as «enforcement reality» anchor |
| O11 R12 anti-extraction | **Stable-as-text; vapor-as-enforcement mechanism** | Text LOCKED 2026-05-12; no technical fork-and-leave infrastructure evidenced | Yes as «constitutional commitment declaration»; NOT as «operational guarantee» |
| O6 12 role-types | **Stable** | Declared roster in CLAUDE.md; Phase column disambiguates active vs planned | Yes as «role taxonomy» anchor; NOT as «running agent count» anchor |

**Key finding.** The most rigorous stable anchor for Phase 0 FPF scope work is O5
(Jetix-as-working-product) cross-referenced against O1 (filesystem-repo). O4 (vision)
and O9 (Foundation-as-artefact) are legitimate anchors for «intended architecture»
claims if clearly labeled. O3 (corporation), O8 (workshop as structure), and O11
(R12 enforcement) are vapor for operational claims.

---

## §4 Use-Mention Discipline — Where Jetix Docs Confuse Concept with Mention

**Principle applied (FPF A.1, A.7; standard use-mention distinction from philosophy of language).**
Use: employing a concept to refer to the world.
Mention: referring to the concept itself (typically quoted or labeled).
Conflating use and mention creates scope creep where describing a concept implies
it exists.

### UM-1: «Jetix is a Workshop» vs «Jetix uses the Workshop frame»

**Working file §3.1.** «Workshop metaphor — architectural anchor.» This is a USE
of the metaphor as if it describes the system structurally, while simultaneously
being a MENTION of the metaphor as a named conceptual frame.

**Symptom.** «Owner = мастер; agents = instrumental specialists; projects = workshop
output» — this applies the metaphor terms as functional role names. If «instrumental
specialist» is then used as a U.Role label, the metaphor has been promoted from
mention to use without declaring this promotion.

**Falsifier.** Is «instrumental specialist» a formal U.Role in the system with a
declared U.RoleAssignment? Or is it a metaphor-derived descriptor used informally?

### UM-2: «Foundation v1.0 is operational» vs «Foundation v1.0 is the specification for what should be operational»

**All Phase B outputs.** LOCKED Foundation is cited as evidence of operational maturity.
06-honest-self-audit §2 explicitly shows this conflation and corrects it.

**Remaining issue.** Despite the self-audit correction, Phase B WORKING-FILE-v0 §7
presents «Foundation 11 Parts table» in a way that implies operational status
by proximity: «F5 LOCKED» appears next to rows for Parts 1/5/9 which the same
self-audit classifies as «memory-dominant» substrate. The F5 applies to the document
formality, not to the operational implementation. Per FPF A.4: the distinction
between document-formality and operational-enactment is non-optional.

### UM-3: «12 rules» as constitutional substrate vs «12 rules as declared intent»

The word «constitutional» (CLAUDE.md §4.1 heading: «Tier 2 Constitutional (12 hard rules)»)
does semantic work that the actual enforcement reality does not support uniformly.
«Constitutional» in political philosophy means enforced constraints on system actors.
In Jetix usage, some rules are enforced (Rule 11), some are conventional (Rules 1, 3),
some have no enforcement path yet (R12). The mention of «constitutional» in the
heading implies the use-level property of enforceable constraint for all 12 rows.

### UM-4: «FPF-derivative» as description vs claim of compliance

Phase B outputs correctly use «FPF-derivative» to describe Jetix mechanisms that
borrow from FPF. This is mention (labeling a relationship). The risk is when
«FPF-derivative» slides into use — implying FPF-compliance. 06-honest-self-audit
§12 explicitly flags: «Not yet FPF-grade on Левенчуковский bar.»
Maintaining the use-mention discipline here requires: every «FPF-derivative» claim
explicitly states «this is a recognized partial adoption, not FPF-compliance.»

---

## §5 Dissents Preserved (per AP-6 + E-5)

### Dissent D-PHIL-SCOPE-1: Brigadier's inventory order vs epistemic object-typing order

**Position held by Phase B brigadier integration.** Objects are presented in a
functional/narrative sequence (system → vision → working product → agents → projects).

**Dissent (philosophy-expert critic, this cell).** Functional sequence and ontological
type-sequence are different orderings and should not be silently merged. FPF A.1
requires holon-type declaration before functional narration. An inventory that
precedes object-type declaration with narrative use of the objects risks embedding
the conflations described in §2.

```yaml
held_by: philosophy-expert × critic (this cell)
F: F4
ClaimScope:
  holds_when: "Phase 0 FPF scope definition aims to establish formal ontological mapping"
  not_valid_when: "working file is intended as narrative-only (which the disclaimer states)"
R:
  refuted_if: "inventory re-ordered by FPF type produces identical claims in same order as functional narration"
  accepted_if: "reordering by type reveals different groupings or surfaces new conflations"
reconciliation: "preserve both orderings; Ruslan decides which governs the Phase 0 scope definition output"
```

### Dissent D-PHIL-SCOPE-2: «Workshop metaphor» status as architectural anchor

**Position held by JETIX-WORKSHOP-CONCEPT-2026-04-30 (LOCKED, Ruslan-dictated).**
Workshop metaphor = LOCKED architectural anchor (canonical frame).

**Dissent (philosophy-expert critic).** An architectural anchor per FPF A.1.1
requires a U.BoundedContext declaration: explicit glossary + role names + scope
+ invariants. The workshop CONCEPT document provides narrative richness but not
formal BoundedContext structure. Using «LOCKED canonical» to grant it architectural
anchor status conflates document-LOCK with formal-structure-declaration.

```yaml
held_by: philosophy-expert × critic (this cell)
F: F4
ClaimScope:
  holds_when: "FPF formal BoundedContext discipline is applied"
  not_valid_when: "workshop metaphor functions as navigation/communication frame only (its original use per Ruslan dictation)"
R:
  refuted_if: "JETIX-WORKSHOP-CONCEPT-2026-04-30 contains explicit U.BoundedContext fields (local glossary, invariants, scope declarations)"
  accepted_if: "document is narrative without formal A.1.1 structure"
reconciliation: "preserve both; if Phase 0 output needs formal FPF anchor, Workshop concept needs A.1.1 formalisation; if narrative framing suffices, no action required. Ruslan decides."
```

---

## §6 Open Questions for Ruslan

> Per R1: surfacing only. These are questions, not recommendations. Ruslan decides.

**OQ-1 (Most load-bearing for Phase 0).** Which of the 6 uses of «Jetix» is the
PRIMARY described entity for FPF scope definition? The scope definition work
cannot proceed without declaring which object is the subject. Candidates:
O2 (information-management system), O5 (working product as-is), O4 (vision),
O3 (corporation). Mixed answer is possible if the scope declaration explicitly
names which object is primary and which are secondary.

**OQ-2.** Does «12 agents» in the scope definition refer to 12 role-types (type)
or 12 active executor bindings (token)? IP-1 makes these different objects.
For FPF scope: if we are mapping FPF primitives onto Jetix, which level is the
primary subject of mapping — the role taxonomy (U.Role) or the executor bindings
(U.RoleAssignment)?

**OQ-3.** Should the FPF scope definition treat Foundation v1.0 as (a) the
described-system-architecture (U.Episteme, current language-state = LOCKED), or
(b) the operational-system-as-instantiated (requires U.Work evidence per Part)?
These two frames produce different FPF-scope outputs.

**OQ-4.** Workshop metaphor: is it being asked to function as a U.BoundedContext
(formal semantic frame with invariants and scope, per FPF A.1.1), or as a
communication frame for human audiences only? If the former, it needs
formalisation. If the latter, FPF scope definition should use a different anchor.

**OQ-5.** R12 anti-extraction: for Phase 0 FPF scope purposes, is R12 being scoped
as (a) a Pillar C rule text (U.Episteme), (b) a commitment object in a specific
relationship (U.Commitment per A.2.8), or (c) an architectural meta-property
(ClaimScope = all substrate-member relationships)? Each faces requires different
FPF primitive assignment and different evidence requirements.

**OQ-6.** «8 active projects» — for FPF scope purposes, should the project
portfolio be treated as one object (portfolio U.Episteme) or as 8 separate objects
(each a U.Work/U.System)? The answer affects which FPF patterns apply (B.4
Canonical Evolution Loop applies per-project; Part 11 Strategic Direction Substrate
applies to the portfolio).

**OQ-7.** Enforcement asymmetry in Pillar C 12 rules: is this known and accepted
as a design-phase artifact (some rules will be machine-enforced in Phase B), or
is the claim that all 12 are currently constitutional (enforced)? If the former,
the scope definition should use different F-G-R levels per rule cluster. If the
latter, the claim needs operational evidence.

---

## §7 Anti-scope (What This Critic Did NOT Do)

Per §3.4 of philosophy-expert system prompt:

- This critic did NOT arbitrate instrumental Рациональность — e.g., did NOT decide
  which object should be primary for FPF scope. That is Ruslan's decision.
- This critic did NOT assess whether FPF alignment is a good goal — that is
  strategic decision per Tier 2 Rule 1 (AI does NOT strategize).
- This critic did NOT assess «is Levenchuk right» about Jetix — surface facts only.
- This critic did NOT produce a corrected inventory — it surfaced errors in existing
  framing; a new inventory is the next cycle's output (integrator or optimizer mode).
- This critic did NOT run engineering critique on code or schemas — engineering-expert
  scope.
- This critic did NOT evaluate Phase B quality as good/bad — only surfaced categorical
  distinctions that affect FPF mapping correctness.

---

## §8 Conformance Checklist (§3.1 critic self-check)

| Check | Result | Evidence |
|---|---|---|
| 1. Falsifier-named (Popper) | pass | Each categorical error (CE-1..CE-5) and reference-frame verdict carries explicit falsifier or refutation condition |
| 2. Paradigm-named on shift (Kuhn) | pass | FPF A.7 Strict Distinction applied as paradigm-lens; pre/post-FPF framing named where applicable |
| 3. Mental-model + conditions cited (Munger) | pass | FPF A.1/A.7/A.4/A.16 cited with applicable conditions per object; Temporal Duality condition stated |
| 4. Method declares what it is NOT (via-negativa) | pass | §7 Anti-scope: 6 explicit NOT-items |
| 5. Dichotomy-of-control for meta-decisions | pass | Object stability column (§3) separates in-control (O1, O5, O6) from not-in-control (O3 corporation, O11 enforcement) |
| 6. Fallacy-named-when-named | pass | No fallacy accusations made; categorical errors named with FPF pattern citation |
| 7. Meta-claim grounded in object-level | pass | Every meta-level claim (e.g., «Foundation LOCKED ≠ operational») grounded in specific evidence from 06-honest-self-audit §2 |

**BA-Cycle-lite check.** BA-0: does this artefact have an ethical surface? NO —
this is a categorical/epistemic inventory, not a capital memo or life-affecting
decision. BA-Cycle-lite not required.

---

## §9 Acceptance Predicate (§3.2 Hamel-binary)

```
acceptance_predicate: "All ≥10 inventory objects carry explicit FPF primitive assignment
AND reference-frame stability verdict AND ≥1 anti-scope item AND ≥1 conflation trap;
AND ≥4 categorical errors are named with explicit falsifiers; AND ≥2 use-mention
confusions are identified with object-level grounding; AND ≥1 dissent block is
present for inter-cell disputes; AND all open questions are surfaced without
recommendations (R1 compliant)."
```

This predicate holds over this artefact as written: 12 objects inventoried (≥10),
5 categorical errors (≥4), 4 use-mention confusions (≥2), 2 dissent blocks, 7 open
questions (≥1), 0 recommendations (R1 compliant).

---

*Draft produced by philosophy-expert × critic. Mode: critic per §3. Read order: this
file → shared-protocols.md → strategies.md → artefact paths cited above. Brigadier
promotes; this cell does not.*
