---
task_id: phase-0-fpf-scope-2026-05-17-task-2
produced_by: philosophy-expert × critic
mode: critic
status: draft
F: F4
G: phase-0-cell-draft
R: refuted_if_falsifiers_missing_per_claim_OR_anti_scope_absent_OR_use_mention_not_distinguished
date: 2026-05-17
sources:
  - path: "reports/phase-0-fpf-scope/01-jetix-objects-inventory.md"
    range: "§1–§8 (primary input)"
  - path: "swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-philosophy-critic-inventory-boundaries.md"
    range: "full (Task 1 phil cell; CE-1..CE-5 extended here)"
  - path: "reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md"
    range: "§1–§14"
  - path: "JETIX-WORKING-FILE-v0-2026-05-17.md"
    range: "§0–§12, Appendix A/B"
  - path: "raw/external/ailev-FPF/FPF-Spec.md"
    range: "A.1, A.1.1, A.2, A.2.1, A.3, A.4, A.7, A.10, A.13, A.14, A.16, B.3, B.5.2, E.5, E.9, E.17"
  - path: "CLAUDE.md"
    range: "§4 Pillar C, §Agent Roster, §Foundation Architecture v1.0"
provenance_inline: true
---

# Philosophy-Expert × Critic — Per-Object Epistemic Deep-Dive

> **Mode:** critic. Task 2, Phase 0 FPF scope definition.
> **Constitutional posture:** R1 (surfacing only; Ruslan decides) + R2 (Foundation read-only)
> + R6 (provenance per claim) + Append-only. Critic mode = find problems, ambiguities,
> conflations. Do NOT recommend fixes. Do NOT evaluate «Levenchuk right/wrong».
> **Predecessor:** Task 1 inventory (`reports/phase-0-fpf-scope/01-jetix-objects-inventory.md`).
> **This artefact:** extends CE-1..CE-5 (Task 1) into per-object falsifier + use-mention +
> anti-scope + conflation trap + hidden assumption + cross-object boundary analysis.

---

## §0 Summary — Epistemic Posture Surfaced Through Deep-Dive (≤300 words)

Fourteen objects across 4 reference-frame stability classes. The deep-dive surfaces five
aggregate epistemic patterns not visible at inventory level:

**EP-1 (Artefact-system gap, ubiquitous).** Ten of fourteen objects carry a LOCKED
artefact status (document language-state per A.16) while their corresponding operational
system status is F2-F4 or vapor. This is not dishonesty — it is a systematic conflation
of two different formality measurements applied to two different subjects (document vs
system). Nearly every top claim about these objects requires the split: Claim-as-document
vs Claim-as-operational-system. Falsifier discipline is missing for the operational face.

**EP-2 (Use-mention drift in definitional prose).** Objects with named metaphors (Workshop,
Clan, Meta-workshop) exhibit use-mention drift: the metaphor name is first mentioned as
a frame, then used as a structural claim predicate, without declaring the promotion.
Workshop is the clearest case; the same pattern recurs in Clan («community of masters»)
and Meta-workshop («мета-мастерская»).

**EP-3 (Role/executor conflation persists cross-object).** CE-2 from Task 1 extends
beyond O-06a/b. The same role-type vs executor-token confusion propagates into O-01
(«12 specialized agents» in the one-liner), O-04 (product claims), O-07 (Foundation
Part 4), and O-12 (brand mermaid «12 Specialized Agents × 6 Departments»). The
IP-1 split has been declared but not yet applied uniformly to prose descriptions.

**EP-4 (Promise without commitment machinery).** O-02, O-10, O-11, O-13 all contain
promise-shaped language (TRM ladder, R12 guarantee, Clan constitutional protections)
without unpacked U.Commitment objects per A.2.8: no adjudication path, no holder-of-
obligation named, no receipt mechanism. The promises exist as U.Episteme text, not as
operational U.Commitments.

**EP-5 (F-G-R level applied to wrong subject).** Several objects have an F-level label
(F5, F8) that actually applies to the document's LOCK status, not to the truth-grade of
the claim itself. F8 for Foundation = «document formally approved via 8 RUSLAN-ACK»,
not «claim verified by 8 independent tests». The F-G-R schema (shared/schemas/f-g-r.json)
is applied, but the subject of the F-level is inconsistently declared.

---

## §1 — O-01: Jetix как оперативный субстрат (information management system)

**Reference-frame stability:** Evolving · reason: voice pipeline, ROY swarm, wiki 551
records all actively changing; state JSON stale 2026-04-14 = mixed evidence.
[src: CLAUDE.md §System Overview; reports/review_2026-05-14.md]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «Jetix = U.System operating on information as single-owner AI OS» | F4 · jetix-operational · R-medium | F4: accurate formality; scope claim is bounded enough | Refuted if: owner scope expands to multi-owner OR if filesystem-SoT rule is violated without AWAITING-APPROVAL packet. [src: CLAUDE.md §4.2] |
| «Filesystem = SoT; Notion = view» | F5 · jetix-canonical | F5: LOCKED rule with enforcement evidence (CLAUDE.md §4.2 RUSLAN-LAYER) | Refuted if: any state change is canonical in Notion without corresponding filesystem copy. Observable: grep for «Notion-authoritative» commits with no filesystem counterpart. |
| «12 specialized agents × 6 departments» | F5 (implicit from CLAUDE.md roster) | F3: conflates role-types (O-06a) with executor-tokens (O-06b); IP-1 split NOT applied to this claim | Refuted as «12 running processes» by Phase column in CLAUDE.md (Phase 3-4 agents not operational). Confirmed as «12 role-type declarations» — a different, weaker claim. [src: CLAUDE.md §Agent Roster] |

**Use-mention concerns:**
- «Jetix как оперативный субстрат» USES «substrate» as a technical term (FPF A.1 / holonic substrate concept) while simultaneously MENTIONING it as a category label. If «substrate» is being used in the FPF-technical sense, it requires A.1 holon-type declaration; if mentioned as colloquial description, no formal requirement. The distinction is never declared.
- «Information management system» — used as type-designation, implying this is the correct FPF primitive. But per Task 1 D-2, this is disputed (U.System vs U.MethodDescription). The USE of the designation pre-empts the dispute.

**Anti-scope (rigorous):**
- O-01 does NOT include the filesystem-repo itself (carrier, not the system; A.7 Strict Distinction per phil × critic Task 1 O1 entry)
- O-01 does NOT include the corporate entity (O-02 = vapor; different object-type)
- O-01 does NOT include the vision/intended-state (O-03 = future system descriptor)
- O-01 does NOT include Notion as co-equal SoT; Notion is explicitly a view-layer only

**Conflation traps:**
- Trap 1 (type-token): «12 agents» cited as evidence of system complexity, but 8 of 12 are Phase-2..4 role-type declarations without executor bindings. Evidence of «12 running processes» is not what is claimed; evidence of «12 declared roles» is. [src: CLAUDE.md §Agent Roster Phase column]
- Trap 2 (language-state / operational-state): Describing O-01 as «working system» while shared/state/active-projects.json is stale 2026-04-14. The language-state of the state file has not been updated. Working system ≠ state-files-up-to-date.
- Trap 3 (carrier/content): «The repo IS Jetix» vs «the repo CARRIES Jetix artefacts». A.10 Evidence carrier ≠ U.System itself. [src: FPF-Spec.md A.10]

**Hidden assumptions:**
- Assumes «single owner» is a stable, unchanging property. If ownership changes (Ruslan brings in partner), the BoundedContext (A.1.1) scope declaration would need revision, but no such revision trigger is specified.
- Assumes filesystem monotonicity: files are added but not destructively deleted. If large-scale cleanup occurs (как Генеральная чистка 2026-04-28), O-01's operational continuity is non-trivial to assert.
- Assumes «operating on information» is the correct description. The system operates on LLM calls, filesystem I/O, and HITL inputs — information processing is one face, not the whole activity.

**Cross-object epistemic boundary disputes:**
- vs O-04: O-01 (substrate) is the architectural frame; O-04 (working product) is what actually ships as outputs. Conflation: citing O-01 substrate maturity (Foundation LOCKED) as evidence of O-04 product maturity. These are different objects with different falsifier conditions.
- vs O-07: Foundation v1.0 LOCKED is claimed to constitute O-01. But if Foundation Parts 1/3/5/9/11 are memory-dominant (06-honest-self-audit §2), does O-07 actually constitute O-01 or merely describe the intended architecture of O-01?

---

## §2 — O-02: Jetix как юр.лицо / корпорация (in-progress)

**Reference-frame stability:** Vapor · reason: no legal entity registered; Doc 1B
purpose = «концептуальный документ» (narrative, not operational record).
[src: decisions/JETIX-CORPORATION-2026-05-05.md frontmatter status]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «Jetix Corp = applied use case базовой системы управления» | F4 · jetix-brand | F3: logical relationship claim grounded in a single document (Doc 1B); no operational evidence | Refuted if: Doc 1B is revised to drop this framing OR if Base-Mgmt-System is applied to a different entity first |
| «TRM 6-resource model: controls capital / founder-time / audience / knowledge / compute / talent» | F4 · jetix-corp-concept | F4 for the taxonomy claim; but «controls» is F2 — no evidence of systematic resource tracking | Refuted if: resource tracking logs show only 1-2 of 6 actually tracked. Observable: only capital (€10/day cap) and attention (≤20 tasks) appear in CLAUDE.md §3.2; others informal. |
| «Doc 1B purpose = conceptual document for partners/investors» | F5 · explicit frontmatter | F5: stated in frontmatter; no ambiguity about status | Refuted if: Doc 1B is cited as evidence of operational legal entity |

**Use-mention concerns:**
- «Корпорация» in the object name uses the word as if referring to an existing entity, while actually mentioning it as a future-state concept. Every time O-02 appears in prose as «Jetix корпорация», readers unfamiliar with the vapor status may interpret it as existing. This is an audience-relative use-mention ambiguity — the same token does different semantic work depending on reader context.
- Doc 1B §0 «TL;DR» is written in present tense («Jetix is a meta-workshop...») but the entity does not exist. Present-tense USE of description language in a concept-only document = use-mention slip.

**Anti-scope (rigorous):**
- O-02 does NOT include a registered GmbH, UG, Ltd, or any other legal entity (none exist per repo evidence)
- O-02 does NOT include active partner agreements or client contracts (no executed contract in repo)
- O-02 does NOT include the OS/software system (O-01 is distinct)
- O-02 does NOT include the role-type taxonomy (O-06a) — the corporation concept may reference roles, but the taxonomy object is separate

**Conflation traps:**
- Trap 1 (concept-as-instance): Treating Doc 1B as evidence that «Jetix Corp exists» because the document describes a corporation. Document existence ≠ corporation existence. A.4 Temporal Duality: design-time description vs run-time instantiation.
- Trap 2 (promise-as-commitment): TRM ladder (€3K→€40-60K/мес) described as business model. As of 2026-05-17, revenue = 0 and ICP has been revised (Mittelstand → Online-first per ACTION-PLAN). The TRM ladder = U.PromiseContent (A.2.3) at best; no U.Commitment (A.2.8) with adjudication path exists.

**Hidden assumptions:**
- Assumes GmbH/UG incorporation will happen on an unspecified timeline. No falsifier for «incorporation within N months» is stated.
- Assumes that Doc 1B's «partner/investor» framing is appropriate for L1 audience (Levenchuk, Tseren). Neither Levenchuk nor Tseren has reviewed Doc 1B for this purpose.
- Assumes TRM as described in LOCKED v1.0 is still current ICP. Contradicted by ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md which changes ICP. [src: 01-jetix-objects-inventory.md §2 O-10 notes]

**Cross-object epistemic boundary disputes:**
- vs O-10: O-02 (corporation concept) and O-10 (business model TRM) are listed as separate objects, but their boundaries blur: TRM is the commercial implementation of the corporation concept. If TRM changes (ICP updated), does O-02 require revision? The dependency direction is unstated.
- vs O-14: O-02 (current corp concept) and O-14 (meta-workshop Phase B+) are different horizon objects. O-02 describes «Jetix Corp today/near»; O-14 describes the platform-for-others version. They are sometimes cited interchangeably under «Jetix Corporation».

---

## §3 — O-03: Jetix как задумка / vision (future state target)

**Reference-frame stability:** Stable-as-artefact; vapor-as-system · reason: FUNDAMENTAL
v1.0 LOCKED 2026-04-27 (artefact F8); described future system has zero operational
realisation.
[src: decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md; 06-honest-self-audit §12]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «35 UC × 12 categories = complete vision encoding» | F4 · jetix-vision-fundamental | F4: the document is well-structured but «complete» is unverified; UC-coverage is asserted, not independently validated | Refuted if: a domain-expert review finds missing use cases OR if Ruslan adds UC-36+ without AWAITING-APPROVAL |
| «100-200 year ambition» (Clan Charter §1.7) | F2 · future-pattern-experimental | F2: timeframe this long has no falsifiability structure; unfalsifiable as stated | Unfalsifiable over 100-year horizon. Per Popper: such claims are not scientific claims about future states — they are normative commitments. Different epistemic category. |
| «Part 11 Strategic Direction Substrate hosts vision correctly» | F5 (Part 11 LOCKED) | F4 for the hosting claim: Part 11 is a substrate (memory-dominant per §2.1 audit); whether it «correctly hosts» depends on whether Part 11's MVPK requirements are met | Refuted if: Part 11 operational audit shows no multi-view publication enforced; per 06-honest-self-audit §2: Part 11 = «memory + structural» — MVPK not enforced |

**Use-mention concerns:**
- «We have a LOCKED vision» — LOCK is mentioned as a property of the document. But «LOCKED vision» is used to imply operational commitment («we are committed to this vision»). The document being LOCKED (A.16 language-state) does not entail the system being built toward it. Two different propositions.
- «35 UC × 12 categories» — mentioned as a coverage metric. But USED implicitly to argue «the vision covers everything Jetix does». Coverage of UC-categories by UC-items does not entail completeness.

**Anti-scope (rigorous):**
- O-03 does NOT include current operational capability (that is O-04)
- O-03 does NOT include revenue or commercial activity (revenue = 0 as of 2026-05-17)
- O-03 does NOT include FPF-grade claims (F2-F4 max for forward-looking vision claims; not independently verified)
- O-03 does NOT include the corporation as an entity (O-02 is separate)

**Conflation traps:**
- Trap 1 (lock = realised): «Foundation LOCKED» repeatedly cited near O-03 vision language, creating proximity-based association that vision = realized. A.16 language-state LOCK on the document ≠ A.4 operational enactment of the described system.
- Trap 2 (normative-as-predictive): The 100-200 year framing presents normative commitments (what we aspire to) as if they were predictive claims (what will happen). Normative and predictive claims have different falsifiability structures.

**Hidden assumptions:**
- Assumes Ruslan's ownership and commitment remain stable over multi-decade horizon. No succession, pivot, or exit clause articulated.
- Assumes that FUNDAMENTAL Layer 1 (sector-agnostic) maps cleanly onto Jetix actual domain. But Jetix = single-owner AI consulting business — the generality claim of Layer 1 adds abstraction debt that has not been paid with any concrete instantiation beyond the vision document itself.

**Cross-object epistemic boundary disputes:**
- vs O-04: O-03 (vision) describes the intended final state; O-04 (working product) describes current state. The gap between them is the truthful statement of O-03's realization status. Gap is large (revenue=0, Parts 1/3/5/9/11 memory-dominant). Claims that «we are building toward O-03» are valid; claims that «O-03 is being realized» require evidence.
- vs O-09: Strategic Insights (O-09) are claimed to «refine» the vision (O-03). But the Hexagon H1-H7 insights were generated 2026-05-10..12; FUNDAMENTAL was LOCKED 2026-04-27. The temporal relationship is inverted: the vision predates the insights. Whether insights «refine» the vision or constitute evidence for a vision revision is unstated.

---

## §4 — O-04: Jetix как работающий продукт (what REALLY works NOW)

**Reference-frame stability:** Stable · reason: grounded in observable artefacts — git
commits, cycle logs, voice pipeline outputs (11 active reviews), CRM records, wiki 551
records. Most rigorous stability anchor of all 14 objects.
[src: 06-honest-self-audit §2; git log; reports/review_2026-05-14.md]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «Foundation v1.0 LOCKED + ROY swarm + voice pipeline = the working product» | F4 · jetix-operational-honest | F4: Foundation-as-document F8 is correct; ROY swarm evidenced (15 Phase-B dispatches); voice pipeline evidenced (11 reviews). But all three are claimed under one F4 label with no disaggregation | Refuted if: ROY swarm stops dispatching OR voice pipeline produces no outputs in next 2 review cycles. [src: 00-SUMMARY-PHASE-B §1] |
| «~27 components = memory+automation; ~12 = intelligence/FPF-derivative» | F4 · distillation-self-audit | F4: sourced from 06-honest-self-audit §11; honest self-assessment | Refuted if: independent FPF-grade audit classifies MORE components as intelligence (raises the 12 count) or FEWER (lowers it). The ~27/~12 split is Ruslan-assessed, not independently validated. |
| «Revenue = 0» | F5 · jetix-operational-honest | F5: verifiable observable; no closed_won in CRM; no client deliverable in git | Refuted immediately when first paying client appears in CRM as closed_won with invoice evidence. |

**Use-mention concerns:**
- «Работающий продукт» — the word «продукт» is used in the commercial sense (something delivered to clients) while the actual product evidence is all internal (Foundation docs, cell drafts, outreach files). The INTERNAL product works; the EXTERNAL product (client deliverable) has zero evidence. This use-mention distinction between «product-for-self» and «product-for-client» is not drawn.
- «Foundation v1.0 is the working product» — this conflates the organisational substrate (Foundation) with the deliverable output (what clients receive). Foundation = infrastructure for delivering; it is not itself what clients buy.

**Anti-scope (rigorous):**
- O-04 does NOT include Phase B managed team capability (no team member besides Ruslan)
- O-04 does NOT include enterprise clients or enterprise-grade deliverables
- O-04 does NOT include TRM at scale — TRM is a model (O-10), not operational at any scale yet
- O-04 does NOT include FPF-grade intelligence amplification — per honest-self-audit §12, Jetix = «memory + automation + ~25% structural-intelligence + ~10% FPF-derivative». Not FPF-grade.

**Conflation traps:**
- Trap 1 (internal-external conflation): The working product exists internally (Foundation docs, ROY swarm cycle outputs) but has zero external commercial evidence. Claiming «Jetix works» without the internal/external distinction is audience-sensitive and epistemically sloppy.
- Trap 2 (substrate=product): Foundation v1.0 = organisational substrate; this is correctly stated in the Foundation's own self-description. But in O-04 framing, Foundation is cited as part of «the product». Substrate is prerequisite for product, not the product itself.

**Hidden assumptions:**
- Assumes that ROY swarm cycles producing cell drafts = «product delivery». This may be accurate for an internal intelligence system but is not a deliverable to external clients. The assumption that internal process maturity = product maturity is not argued.
- Assumes that 06-honest-self-audit §2 classification (~27/~12 split) is stable. It was produced by claude-in-context, not by independent external review. Self-assessment of one's own intelligence amplification level is epistemically suspect.

**Cross-object epistemic boundary disputes:**
- vs O-07: Foundation (O-07) is cited as constituting O-04. But O-04 = what works NOW, while O-07 Parts 1/3/5/9/11 are memory-dominant per audit. The claim «Foundation v1.0 constitutes the working product» needs per-Part qualification: which Parts contribute to working-product claims and which contribute only to architectural-substrate claims?
- vs O-01: O-01 (substrate) and O-04 (working product) are related but distinct. O-01 = the system architecture; O-04 = the actual outputs. A working system does not entail working outputs, and vice versa. The distinction is collapsed in some Phase B prose.

---

## §5 — O-05: Jetix как методология / pattern language (forkable)

**Reference-frame stability:** Vapor-as-distributable · reason: no distributable format
exists; Fork guide v0 = 6-step outline in working file §11 (F2); zero external instances.
[src: JETIX-WORKING-FILE-v0 §11; 01-jetix-objects-inventory.md §2 O-05]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «FUNDAMENTAL Layer 1 = sector-agnostic pattern» | F2 · future-pattern-experimental | F2: «sector-agnostic» is an unfalsified design claim. The pattern has only one instance (Jetix itself), making sector-agnosticism non-testable | Refuted if: first external fork of the pattern requires significant domain-specific modifications that break the sector-agnostic claim. Observable only when first fork exists. |
| «Fork guide v0 (6 steps) enables pattern instantiation» | F2 · future-pattern-experimental | F2: a 6-step outline in a narrative file does not constitute a «guide» in the engineering sense (Koen heuristic: needs sotam + known failure modes). It is a U.WorkPlan, not a U.Method | Refuted if: a person with no Jetix context attempts the 6 steps and cannot produce a working instance without additional guidance |
| «Phase C remit for distribution» | F2 · jetix-phase-B-framing | F2: Phase C is not defined beyond this label; no timeline, no activation conditions beyond «Cooperation Plan Tier 3 activates» | Unfalsifiable as stated: «Phase C» has no defined start condition. |

**Use-mention concerns:**
- «Методология» — used in the title as if this is a declared U.MethodDescription (A.3.2). But the methodology object has never been formally declared per A.3.1 (abstract method with known failure modes). The word «методология» is mentioned as an aspiration, not used to denote an existing formal method object.
- «Forkable» — mentioned as a property but never tested. The property «forkable» requires at least one successful fork. Until then, «forkable» is a design claim about intended modularity, not an evidenced property.

**Anti-scope (rigorous):**
- O-05 does NOT include a distributed template format (nothing has been packaged for distribution)
- O-05 does NOT include any external instance or fork (zero external forkers confirmed)
- O-05 does NOT include the formal IWE-Pack analogue — Phase B research explicitly scoped this as future (Phase C remit)
- O-05 does NOT operate in the same ontological register as O-01 (running system); O-05 is U.Episteme describing a future U.Method

**Conflation traps:**
- Trap 1 (existence-by-description): Describing a methodology in detail does not make it exist as a tested method. A.4 Temporal Duality: the description (O-05) ≠ the enactment (which has zero instances).
- Trap 2 (unique-because-described): O-05 is implicitly positioned as unique because it is described as forkable and sector-agnostic. These are design intentions, not verified properties. The uniqueness claim requires comparative evidence.

**Hidden assumptions:**
- Assumes there is a market for «fork-and-instantiate» pattern adoption among future partners. Zero market validation exists.
- Assumes FUNDAMENTAL Layer 1 achieves «sector-agnostic» status by design intent. No architectural stress-test of the claim (what sector would break the pattern?) has been attempted.
- Assumes Phase C will activate in time for the methodology to be distributed before obsolescence. Phase C activation depends on Phase B commercial outcomes (revenue = 0 today).

**Cross-object epistemic boundary disputes:**
- vs O-03: O-03 (vision) includes the pattern-language aspiration as part of its 35 UC. O-05 is effectively a sub-claim of O-03. The separation into two objects may be justified operationally (the methodology can be extracted from the vision), but the epistemic dependence is not declared.
- vs O-14: O-14 (meta-workshop) is the activation context for O-05 (methodology). Without O-14 being operational, O-05 cannot be forkable in practice. This dependency creates a cascade vapor: O-14 vapor → O-05 forkable vapor.

---

## §6 — O-06a: Jetix-as-12-role-types (type-level — IP-1 split A)

**Reference-frame stability:** Stable · reason: CLAUDE.md §Agent Roster is a LOCKED
declaration with Phase column; type-level declarations are stable as long as roster
is not revised.
[src: CLAUDE.md §Agent Roster; swarm/wiki/foundations/part-4-role-taxonomy/architecture.md]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «12 role-types declared in roster» | F5 · jetix-role-taxonomy | F5: count is verifiable from CLAUDE.md §Agent Roster table (12 rows present) | Refuted if: CLAUDE.md §Agent Roster row count changes to ≠ 12 without AWAITING-APPROVAL packet |
| «Phase 1: 4 active roles; Phase 2-4: 8 planned» | F5 · jetix-role-taxonomy | F5: Phase column in CLAUDE.md is explicit and verifiable | Refuted if: a Phase 2-4 role is operationally dispatched without Phase promotion documented |
| «12 U.Role declarations satisfy A.2 Role Taxonomy» | F4 · jetix-role-taxonomy | F3: satisfying A.2 requires method-signature per role, not just name + model + department. Part 4 LOCKED contains the taxonomy but method-signature enforcement = STUB Phase-B per mgmt-expert.md §3.0 | Refuted if: any role declaration is missing its A.2.7 RoleAlgebra position or A.13 Agential Role autonomy budget |

**Use-mention concerns:**
- «12 agents» in CLAUDE.md and working file mermaid §4 — the word «agents» is used (claiming these are running-process-style agents) while the roster actually MENTIONS abstract role-type slots. An «agent» in AI discourse implies a running process; a «role-type» implies a typed declaration. The two uses are not equivalent.
- «4 Phase-1 active» — USED as evidence of operational scale («Jetix has 4 active AI agents»). But this means 4 role-types have confirmed executor bindings in Phase 1. The claim about scale depends on which face of the IP-1 split you're measuring.

**Anti-scope (rigorous):**
- O-06a does NOT include executor instances (Sonnet 4.6, Haiku 4.5) — those are O-06b
- O-06a does NOT include running processes or conversation threads
- O-06a does NOT include the ROY swarm (brigadier + 5 experts) — ROY swarm = a separate set of executor bindings distinct from the legacy 12-role roster
- O-06a does NOT constitute evidence of operational capability; type-declarations without executor bindings have no operational evidence

**Conflation traps:**
- Trap 1 (IP-1 core): The persistent conflation of «12 role-types» with «12 agents running» is CE-2 from Task 1. Quantitatively: ROY swarm = 6 dispatching roles; legacy 12 mailboxes stale as of 2026-04-15. Neither count equals 12 running processes.
- Trap 2 (type-completeness): Declaring 12 role-types does not mean the 12 roles cover all needed functions. The «completeness» of the role taxonomy is asserted but no coverage criterion is specified.
- Trap 3 (Phase-implies-active): Phase 1 agents being «active» does not mean they run continuously. Manager, personal-assistant, system-admin, sales-lead are Phase 1 — but evidence of manager mailbox activity since 2026-04-15 = absent.

**Hidden assumptions:**
- Assumes that CLAUDE.md §Agent Roster remains the authoritative roster (not the ROY swarm agents in .claude/agents/). These are currently different sets with partial overlap; the canonical roster is ambiguous.
- Assumes that «4 Phase-1 active» is a meaningful operational claim. But if Phase 1 agents' mailboxes are stale, «active» = «declared as Phase 1» not «receiving dispatches».

**Cross-object epistemic boundary disputes:**
- vs O-06b: The IP-1 split between type (O-06a) and token (O-06b) is the correct resolution of CE-2. However, the boundary condition for «which claims about agents belong in which object» is not consistently applied. Prose about «12 agents» should always specify which face.
- vs O-07: Foundation Part 4 governs O-06a (Role Taxonomy). But if Part 4's method-signature enforcement = STUB, then the governance relationship is declared but not enforced. O-07→O-06a edge has asymmetric strength: architectural declaration F5, operational enforcement F2.

---

## §7 — O-06b: Jetix-as-executor-bindings (token-level — IP-1 split B)

**Reference-frame stability:** Evolving · reason: ROY swarm = actively dispatching
(15 Phase-B invocations evidenced); legacy 12 mailboxes = stale 2026-04-15; two
different populations with different stability profiles.
[src: 00-SUMMARY-PHASE-B §1; comms/mailboxes/manager.jsonl]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «ROY swarm (brigadier + 5 experts) = actively dispatching» | F4 · jetix-executor-bindings | F4: 15 dispatches evidenced in Phase B summary. But «actively» implies ongoing cadence; the evidence is Phase-B-specific | Refuted if: no new ROY dispatch occurs in the next 2 Jetix work sessions. Observable via git commits from brigadier. |
| «Legacy 12-agent mailboxes = stale» | F4 · mgmt-integrator assessment | F3: stale mailboxes = necessary evidence of inactivity but not sufficient (direct dispatch without mailbox trace possible per D-mgmt-2) | Refuted if: any session transcript shows legacy agent invoked via direct dispatch without mailbox record. This is the D-mgmt-2 dissent — unresolved. |
| «RUSLAN-LAYER executor-binding.yaml.template governs bindings» | F5 (template LOCKED) | F4: template exists and is LOCKED; but whether it is APPLIED to all current bindings is unverified. ROY swarm .claude/agents/ files may not all conform to the template schema | Refuted if: any .claude/agents/*.md file binds executor without declaring the executor-binding fields specified in the template |

**Use-mention concerns:**
- «Executor binding» — used throughout as if these are persistent, persistent processes. But bindings are contextual (per FPF A.2.1: Holder#Role:Context = session-scoped). The USE of «binding» implies permanence; the ontological reality is session-scoped enactment.
- «The agents are running» — MENTIONED occasionally in Phase B prose to describe what brigadier dispatches. But RUN ≠ RUNNING-CONTINUOUSLY. Each dispatch is a new context instantiation. The use of present-progressive «running» maps badly to the reality of context-window-scoped enactment.

**Anti-scope (rigorous):**
- O-06b does NOT include the role-type declarations (O-06a) — token-level binding is a separate object from the type declaration
- O-06b does NOT include the chat history or session memory (those are in scratchpad per 5-layer memory architecture, if scaffolded)
- O-06b does NOT guarantee persistence across sessions; each binding is context-scoped
- O-06b does NOT include «the 12 legacy agents» as actively operational (stale mailbox evidence plus D-mgmt-2 dissent)

**Conflation traps:**
- Trap 1 (persistence assumption): Executor bindings described as if they constitute «the agents of Jetix» as persistent actors. They are contextual role-enactments. A.2.1 Holder#Role:Context is the correct formulation.
- Trap 2 (ROY swarm = «the agents»): Since legacy 12 are stale and ROY swarm is active, there is an implicit migration: «the agents of Jetix» now refers to ROY swarm, not the declared 12. This migration has NOT been explicitly documented in CLAUDE.md.

**Hidden assumptions:**
- Assumes ROY swarm (brigadier + 5 experts) covers the functional responsibilities of the legacy 12-role roster. This is not verified: knowledge-synth, life-coach, meta-agent roles (Phase 3-4) have no ROY equivalent.
- Assumes that «stale mailbox = inactive» (with the D-mgmt-2 dissent noted): the absence-of-trace assumption may not hold for direct-dispatch sessions.

**Cross-object epistemic boundary disputes:**
- vs O-06a: The IP-1 boundary is declared but not consistently applied in CLAUDE.md prose. The mermaid in §4 of the working file shows «12 Specialized Agents × 6 Departments» as a unified block, not split by IP-1.
- vs O-01: O-06b executor bindings ARE the operational face of O-01 (the system). But if O-06b's ROY swarm covers only partial O-06a role-type roster, then O-01's «12 role-types × 6 departments» claim overstates operational coverage.

---

## §8 — O-07: Foundation Architecture v1.0 (F8-LOCKED)

**Reference-frame stability:** Stable-as-artefact; mixed-as-system · reason: 11
architecture.md files + 8 RUSLAN-ACK records + git-tag provide stable artefact anchor.
4 of 11 Parts FPF-derivative operational; 7 substrate/memory-dominant.
[src: CLAUDE.md §Foundation Architecture v1.0; 06-honest-self-audit §2]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «Foundation v1.0 LOCKED = F8 grade» | F8 (artefact lock) | F8 for the document-formality claim ONLY. «F8» here means «locked via formal approval process (8 RUSLAN-ACK records)» — NOT «independently tested 8 times» per standard F8 scientific usage | Refuted (as artefact-lock claim) if: a Foundation Part is modified without an AWAITING-APPROVAL packet. Observable via git history. |
| «11 Parts + Pillar A + Pillar C constitute the organisational substrate» | F5 · jetix-foundation-canonical | F3 for «constitute» (operational claim): 7 Parts are memory/automation substrate; only 4 Parts are FPF-derivative operational. «Constitute» implies operational contribution, not just architectural description | Refuted if: operational audit shows zero enforcement evidence for Parts 1/3/5/9/11 beyond static file storage (per 06-honest-self-audit §2 findings) |
| «Halt-Log-Alert response time: F8 ≤1s / F4 ≤5s / F2 ≤60s» | F5 (Part 6b LOCKED) | F2 for the operational claim: Halt-Log-Alert = STUB Phase-B per agent files. The specification is F5; the operational implementation is F2 at best | Refuted as operational claim if: any F8-grade violation is committed and no halt/log/alert fires within 1s. |

**Use-mention concerns:**
- «Foundation v1.0 LOCKED» — MENTIONED as a label that implies full operational system. USED throughout Phase B output as shorthand for «Jetix works». The mention (document status) is being used to make claims about operational reality. CE-3 from Task 1 is the definitive statement; the use-mention slip persists across all Phase B prose despite the disclaimer.
- «Organisational substrate» — Foundation describes itself as such in its own architecture.md files. This is an internally self-referential USE: Foundation claims to be the substrate for the system it specifies. Per A.4: the claim is a design-time description; the operational substrate status requires independent U.Work evidence.

**Anti-scope (rigorous):**
- O-07 does NOT include proof that all 11 Parts are operational (Parts 1/3/5/9/11 = memory-dominant per honest-self-audit)
- O-07 does NOT include FPF-compliance certification — Jetix Foundation is acknowledged as «tactical FPF adoption, not full FPF-grade» per working file §6.1
- O-07 does NOT include Halt-Log-Alert as operational enforcement (STUB Phase-B)
- O-07 does NOT include the ROY swarm agent files (.claude/agents/) — those are implementation artefacts separate from the Foundation architecture specification

**Conflation traps:**
- Trap 1 (artefact-F8 vs claim-F8): F8 in Jetix = «formally approved via RUSLAN-ACK process». F8 in standard F-G-R (B.3) = «formal proof / highest assurance». These are not the same. The Jetix F8 is approval-grade, not proof-grade. Calling Foundation «F8» without this disambiguation misleads external audiences.
- Trap 2 (D-2 unresolved): Foundation = U.System + U.Mechanism (eng) vs U.Episteme / U.MethodDescription (phil) — this typing dispute is preserved as D-2 in Task 1 but not resolved. Every FPF primitive assignment downstream of O-07 carries this ambiguity.
- Trap 3 (all-Parts-equal): «11 Parts LOCKED» implies equal status. But Parts differ radically in operational evidence: Part 6b (enforcement mechanism, F5 operational) vs Part 9 (owner interaction scaffold, memory-dominant, no daily-log/ directory exists). [src: 06-honest-self-audit §2]

**Hidden assumptions:**
- Assumes that 8 RUSLAN-ACK records = «extensive review». But all ACKs are from one reviewer (Ruslan) reviewing their own system. No external reviewer has validated the Foundation architecture. The «F8 LOCKED» process is formally correct by Jetix rules but is a single-author approval trail.
- Assumes Foundation v1.0 is the current authoritative spec. Phase B outputs (working file, cell drafts) have added context and framing that may implicitly extend or revise Foundation without formal Part update processes.

**Cross-object epistemic boundary disputes:**
- vs O-08: Foundation (O-07) and Pillar C (O-08) are specified as separate objects but Pillar C is part of Foundation v1.0 LOCKED. The «Foundation → Pillar C constrains» edge creates a circular reference: Pillar C is part of Foundation, which Pillar C governs. This recursion is unproblematic in practice but muddies the ontological separation.
- vs O-04: If Foundation (O-07) = «organisational substrate» and O-04 = «working product», then O-07 should be a prerequisite of O-04. But O-04's operational outputs (cycle outputs, voice pipeline) did not wait for Foundation to be complete. Foundation was LOCKED after O-04 operations were running. Temporal order is inverted relative to the «Foundation constitutes product» narrative.

---

## §9 — O-08: Pillar C конституциональная система (12 Tier-2 rules)

**Reference-frame stability:** Stable-as-text; partial-as-enforcement · reason: 12 rules
LOCKED in CLAUDE.md §4.1 and in principles/ Foundation sub-system. Machine-enforcement
confirmed only for Rule 11 (Default-Deny table). Remaining 11 rules = human-review or no
mechanism.
[src: CLAUDE.md §4.1; .claude/config/default-deny-table.yaml; 06-honest-self-audit §2 Pillar C row]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «12 hard rules = Tier 2 Constitutional» | F8 (text) / F4 (enforcement) per Task 1 inventory | F8 for text-lock: confirmed. F2 for «constitutional» = uniformly enforced: machine enforcement only for Rule 11; human-convention for Rules 1/3/8/9; no mechanism for R12 | Refuted as «12 uniformly enforced constitutional rules» if: any Rule 1/3/8/9/12 violation is committed and no halt/alert fires. |
| «Default-Deny table (11 entries) = machine-enforced» | F5 · Part-6b-LOCKED | F5: .claude/config/default-deny-table.yaml exists with 11 entries; Halt-Log-Alert response described | Refuted if: a novel action class is NOT in the table and the system proceeds without deny-and-escalate behavior. Observable: test an unlisted action class. |
| «R12 additive rule 12 = constitutional Tier 2» | F5 (text per CLAUDE.md §4.1 additive 2026-05-12) | F3 for full constitutional status: text LOCKED but AWAITING-APPROVAL packet not yet ack'd; enforcement mechanism = none | Refuted as «ack'd constitutional rule» if AWAITING-APPROVAL packet (r12-anti-extraction-2026-05-12.md) remains unacked beyond the current cycle. |

**Use-mention concerns:**
- «Constitutional» — used as a property of all 12 rules (the heading in CLAUDE.md §4.1 = «Tier 2 Constitutional»). In political theory and FPF (E.5 Guard-Rails), «constitutional» means enforced constraints on system actors. This USE implies uniform enforcement. The MENTION of «constitutional» applies only to the declared intent of the rule set.
- «12 LOCKED» — mentioned as a security property. Used to imply «12 rules are in effect». Effect ≠ text-lock. CE-4 from Task 1 is the definitive statement.

**Anti-scope (rigorous):**
- O-08 does NOT include Tier 1 owner principles (self-discipline only; agents do not enforce)
- O-08 does NOT include machine-enforcement for Rules 1/3/8/9/12 (human-review only)
- O-08 does NOT include formal U.Commitment objects per A.2.8 for all 12 rules (only Rule 11 has adjudication-path evidence: the default-deny-table.yaml)
- O-08 does NOT include R12 as ack'd (AWAITING-APPROVAL pending)

**Conflation traps:**
- Trap 1 (text=enforcement): CE-4 from Task 1. The three sub-categories — machine-enforced / human-review / no-mechanism — have been identified but are not visibly separated in CLAUDE.md §4.1. The uniform «constitutional» heading masks the enforcement stratification.
- Trap 2 (rule-count as capability signal): «12 constitutional rules» cited as evidence of governance maturity. Rule count without enforcement evidence is a count of MENTIONED obligations, not EFFECTIVE constraints. Levenchuk's C3 critique applies here: governance substrate ≠ intelligence amplification.
- Trap 3 (R12 four-source trail = ack'd): R12 has a 4-source attribution trail (CLAUDE.md §4.1 additive). But a 4-source trail ≠ ack'd constitutional rule. The packet is AWAITING-APPROVAL. Citing R12 as «LOCKED» in the same breath as Rules 1-11 conflates pending-ack with ack'd.

**Hidden assumptions:**
- Assumes Ruslan's human review of Rules 1/3/8/9 is reliably performed in every session. No audit trail for human-review-enforced rules exists. The governance substrate depends on Ruslan's consistent attention — an unchecked single-point-of-failure.
- Assumes that the Default-Deny table's 11 entries are exhaustive for current novel-action classes. As Jetix's operations expand (new agent types, new tool permissions), new action classes will emerge that are not in the table. No table-maintenance process is specified.

**Cross-object epistemic boundary disputes:**
- vs O-11: R12 (O-11) is declared to be part of O-08 (Pillar C Tier 2 Rule 12). But O-11 is also given a separate object entry in the inventory. The boundary between «R12 as rule-in-O-08» and «R12 as separate-architectural-meta-property-O-11» is the EP-4 pattern applied specifically here.
- vs O-07: Pillar C (O-08) is claimed to «constrain» Foundation (O-07). This is the correct direction per CLAUDE.md §Critical Tier-2 Principles. But if Pillar C enforcement is partial (only Rule 11 machine-enforced), then «constrains Foundation» means «partially constrains Foundation». The constraint claim requires per-rule qualification.

---

## §10 — O-09: Strategic Insights Hexagon (synthesis cadence 6+1)

**Reference-frame stability:** Stable-as-artefacts; process-informal · reason: 6 STRATEGIC-
INSIGHT files exist, are LOCKED, and have 4-source attribution trails. But cadence = informal
(no weekly schedule documented); «synthesis» process is Ruslan-directed in each cycle.
[src: decisions/STRATEGIC-INSIGHT-*-2026-05-10..12.md; 06-honest-self-audit §7]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «Strategic Insights Hexagon = closest to FPF intelligence amplification in Jetix» | F5 · jetix-canonical | F4: «closest to» is a comparative claim within the Jetix system (internal comparison). Not a claim against the FPF bar itself. The self-audit §7 provides the most honest framing | Refuted if: an independent FPF reviewer classifies another Jetix component (e.g., F-G-R schema + Provenance Officer combination) as closer to B.5.2 Abductive Loop. |
| «6 STRATEGIC-INSIGHT files = Hexagon synthesis output» | F5 · jetix-canonical | F5: 6 files exist, are LOCKED, have F-G-R tagging. But «Hexagon» as a name implies a structured 6-cell synthesis process with defined positions. The process that produced these 6 insights is not formally documented as a Hexagon protocol | Refuted if: the 6 insights were NOT produced by a structured abductive process but by sequential single-perspective analysis. Observable: review the generation process for alternatives-portfolio evidence. |
| «B.5.2 Abductive Loop partial implementation» | F4 (per 06-honest-self-audit §7) | F3: «partial» is honest but imprecise. Abductive Loop (B.5.2) requires explicit alternatives-portfolio generation, NOT first-answer. Strategic Insights show conclusions; the alternatives-generation process is not documented | Refuted if: Hexagon generation logs show alternatives explicitly generated and discarded before LOCKED insight was chosen. |

**Use-mention concerns:**
- «Hexagon» — MENTIONED as a name for the synthesis cadence. USED as evidence of a structured process. The name «Hexagon» implies 6 structured positions/perspectives. But the 6 insights cover different strategic topics (Balaji / Foundation-Model / Gamification / People-NS / Partnership / Tyson) — not 6 systematic perspectives on the same topic. The hexagonal structure is a naming metaphor, not a guaranteed analytical structure.
- «Weekly cadence» — cited in working file §5.1 as a mechanism description, but the 6 insights were all generated in a 3-day window (2026-05-10..12), not over 6 weeks. Use of «cadence» implies regularity that the evidence does not support.

**Anti-scope (rigorous):**
- O-09 does NOT include a formal NQD-CAL alternatives portfolio (explicit alternatives not documented per gap in Task 1 §2)
- O-09 does NOT include a full E.17 MVPK bundle (1A+1B multi-view = informal; no ViewpointBundle definition)
- O-09 does NOT include systematized weekly cadence (3-day generation window for 6 insights ≠ sustained weekly process)
- O-09 does NOT include B.5.2 full Abductive Loop implementation (partial adoption only)

**Conflation traps:**
- Trap 1 (output=process): Having 6 LOCKED strategic insight outputs does not demonstrate that the process that generated them was a formal Abductive Loop. Process quality ≠ output quality. The outputs may be high-quality without the process being formally implemented.
- Trap 2 (proximity-implies-equivalence): «Closest to FPF intelligence amplification» does not mean «equivalent to FPF intelligence amplification». The comparison is relative within Jetix, not absolute against the FPF bar.
- Trap 3 (Hexagon-as-system): «Hexagon synthesis cadence» treated as an O-09 system object, but it is more accurately a collection of 6 artefacts produced by informal-abductive-adjacent process. Calling it a «cadence» (which implies ongoing repetition) based on one 3-day generation event is premature.

**Hidden assumptions:**
- Assumes that the 6 insights generated in 2026-05-10..12 represent a reproducible synthesis pattern. One data point is insufficient to claim a «cadence».
- Assumes F-G-R tagging on insights = intelligence amplification. F-G-R tagging is a provenance discipline (memory + structural); it does not itself constitute abductive intelligence work.

**Cross-object epistemic boundary disputes:**
- vs O-03: O-09 insights «refine» O-03 vision per §4 cross-ref table. But H1-H7 were generated after FUNDAMENTAL was LOCKED. «Refinement» is the correct framing only if the insights are incorporated into a FUNDAMENTAL revision via AWAITING-APPROVAL. If not, they coexist as parallel claims without formal reconciliation.
- vs O-11: H7 People-NS (one of O-09 insights) is the «origin of R12» per §4 cross-ref table. This makes O-09 causally upstream of O-11 (R12). But the causal attribution «R12 originated from H7» is itself an F4 claim — the 4-source attribution trail does not formally prove origination, it documents provenance.

---

## §11 — O-10: Бизнес-модель Phase 1 (TRM / quick-money consulting)

**Reference-frame stability:** Aspirational · reason: TRM model LOCKED (artefact stable)
but revenue = 0; ICP has been revised without updating Doc 1B; critical path
(Tseren/Levenchuk partnership) = unresolved.
[src: decisions/JETIX-TRM-MODEL-2026-04-30.md; decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md;
shared/state/active-projects.json revenue_current:0]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «TRM 6-resource model = business model» | F4 · jetix-business-model | F3: TRM is a U.PromiseContent framing (A.2.3) — what Jetix promises to manage. A business model requires also: revenue logic, client acquisition path, delivery mechanism. TRM describes one face only | Refuted if: TRM is replaced by a different resource taxonomy in a revised locked business-model document |
| «ICP = Online-first entrepreneurs and consultants» | F4 (ACTION-PLAN-PHASE-1) | F2: ICP was Mittelstand DACH in Doc 1B (LOCKED); ACTION-PLAN-PHASE-1 revised it to Online-first. Doc 1B §7 not updated. Two documents carry contradicting ICP definitions. This is a live inconsistency. | Refuted as «consistent ICP» by the existence of Doc 1B §7 (Mittelstand) coexisting with ACTION-PLAN §0 (Online-first). Observable today. |
| «L0-L5 ladder = activation path from €0 to €40-60K/мес» | F4 · TRM-LOCKED | F2 for the activation claim: L0 = «first client at any fee»; as of 2026-05-17, revenue = 0. The ladder is a U.WorkPlan (intended progression), not a U.Work record of progression | Refuted as «activation path» if L0 is not achieved within N months (undefined). Without a falsifier deadline, the ladder claim is unfalsifiable as an activation claim. |

**Use-mention concerns:**
- «TRM works» vs «TRM is the current operating model» — TRM MENTIONED as a LOCKED model, but USED as if it describes current operating reality. As of 2026-05-17, TRM operates only as a documented aspiration, not as a tracked resource management system.
- «6 resource classes» — USED as if these 6 are currently being tracked and managed. Only 2 of 6 have tracking mechanisms in CLAUDE.md: attention (≤20 active tasks) and capital (€10/day cap). Knowledge, network, reputation, and founder-time = informal at best.

**Anti-scope (rigorous):**
- O-10 does NOT include active contracts (revenue = 0; no closed_won in CRM)
- O-10 does NOT include a consistent ICP (Doc 1B vs ACTION-PLAN inconsistency = live flag)
- O-10 does NOT include TRM at any scale beyond theoretical (L0 not achieved)
- O-10 does NOT include the 6 resource tracking systems as operational (only 2 of 6 mechanized)

**Conflation traps:**
- Trap 1 (model=implementation): TRM is a model (description of how resource management works). That TRM is LOCKED ≠ TRM is being implemented. A.4 Temporal Duality applies: model ≠ enacted method.
- Trap 2 (ICP inconsistency invisible): Two LOCKed documents contain contradicting ICP definitions. Each document internally appears consistent; the inconsistency is only visible cross-document. This is a silent conflation that will surface when pitching to prospects.
- Trap 3 (ladder-as-roadmap): L0-L5 ladder presented as a clear activation path. But the conditions for each level are not fully falsifiable: «L0 = first client at any fee» — what counts as a «fee»? When is this level achieved? The ladder is more of a narrative ordering than a formal stage-gate predicate system.

**Hidden assumptions:**
- Assumes ACTION-PLAN-PHASE-1 ICP revision (Online-first) is correct and that Mittelstand DACH target in Doc 1B is now deprecated. Neither document explicitly states this.
- Assumes the Tseren/Levenchuk partnership «unlock» is the critical path. But if the partnership does not materialize, the business model's activation path is unspecified.
- Assumes that «management fee + performance fee» structure is viable for Online-first entrepreneurs. No validation of fee structure against this ICP segment exists.

**Cross-object epistemic boundary disputes:**
- vs O-02: TRM (O-10) is claimed to «implement» the corporation concept (O-02). But if ICP has changed in ACTION-PLAN without Doc 1B update, the TRM that O-10 describes may no longer implement the corporation-as-designed in O-02. The gap between O-02 (LOCKED 2026-05-05) and O-10 (ICP revised 2026-05-10) is not formally tracked.
- vs O-12: O-10 (business model) and O-12 (brand/public layer) are both oriented toward external audiences. Doc 1B (O-12) contains both the corporation narrative AND the ICP definition. Revising the ICP without updating Doc 1B = inconsistency propagating from O-10 into O-12.

---

## §12 — O-11: R12 Anti-extraction (конституциональный принцип)

**Reference-frame stability:** Stable-as-text; vapor-as-enforcement · reason: text LOCKED
in CLAUDE.md §4.1 (additive 2026-05-12); 4-source attribution trail documented;
AWAITING-APPROVAL packet written but not yet acked; enforcement mechanism = none evidenced.
[src: swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md; CLAUDE.md §4.1 rule 12]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «R12 = constitutional Tier 2 rule, F5 LOCKED» | F5 (text) | F5 for text-LOCKED: CLAUDE.md §4.1 additive confirmed. But «constitutional» requires enforceable constraint; AWAITING-APPROVAL not ack'd = not yet formally ack'd as O-08 Pillar C member | Refuted as «ack'd constitutional» if AWAITING-APPROVAL packet remains in swarm/awaiting-approval/ without RUSLAN-ACK for >3 cycles |
| «Substrate cannot extract value from members beyond agreed share» | F5 (text) | F2 for operational claim: no «agreed share» is defined per member; no enforcement path; «fork-and-leave» = technically non-trivial (no infrastructure for data portability evidenced) | Refuted as operational guarantee if: any substrate-member relationship is established without explicit agreed-share definition AND R12 text is invoked as protection. Observable: check CRM for any partner agreement with R12 scope declared. |
| «NONE in public IWE template = unique» | F4 · jetix-position-vs-IWE | F2: «unique» as a claim requires: (a) complete search of IWE template, (b) complete search of FPF Spec, (c) confirming no equivalent in paid aisystant guide (B2 blocker per D-1). Only (a) and (b) done | Refuted if paid aisystant IWE guide contains R12-equivalent mechanism |

**Use-mention concerns:**
- «Constitutional guarantee» — R12 is MENTIONED as a rule (text). Used implicitly as if it PROVIDES a guarantee to future members/partners. A constitutional text is not itself a guarantee; it is a commitment that requires enforcement for the guarantee to be real. Three faces of R12 (EP-4 pattern): text / applied commitment / architectural meta-property — all three are mentioned together without distinguishing which USE is operative.
- «Fork-and-leave without penalty» — text states this as a right. USED as if the right is currently exercisable. No «fork-and-leave» infrastructure (data export, state handoff, transition protocol) is evidenced. Declaring a right without the mechanism to exercise it is a use-mention conflation: MENTIONING the right vs USING a functioning right-exercising mechanism.

**Anti-scope (rigorous):**
- O-11 does NOT include bilateral written agreements with any partner (none executed)
- O-11 does NOT include technical fork-and-leave infrastructure (no data-portability mechanism documented)
- O-11 does NOT include formal Game Theory proof of the M-C mechanism claim (Game Theory M-C §11 is cited as backing but the proof is not in the repository)
- O-11 does NOT include IWE/FPF community agreement or endorsement
- O-11 does NOT include enforcement mechanism for determining what «beyond agreed share» means in any specific relationship

**Conflation traps:**
- Trap 1 (three-object conflation as EP-4): (a) rule text, (b) applied commitment in specific relationship, (c) architectural meta-property — these three faces of R12 have different F-G-R levels, different evidence requirements, and different scopes. Treating R12 as a single object with one F-G-R label (F5) masks the internal stratification.
- Trap 2 (attribution-trail = proof): The 4-source attribution trail documents provenance, not validity. Having 4 sources for an idea does not prove the idea is correctly formulated or enforceable.
- Trap 3 (unique = superior): «NONE in IWE template» is a comparative-negative claim. It does not establish that R12 is a better mechanism, only that no equivalent was found in one specific (public template) version of IWE. D-1 dissent from Task 1 applies: comparison is scoped to public template, not to paid guide.

**Hidden assumptions:**
- Assumes that «agreed share» can be operationally defined for future partner relationships. No definition template or negotiation protocol exists.
- Assumes R12 is self-executing in practice: that partners would actually be able to fork and leave without penalty even if the rule exists only as text. The gap between normative declaration and practical exercisability is not addressed.
- Assumes that R12 being in Pillar C Tier 2 (text) = R12 being ack'd at the same level as Rules 1-11. The AWAITING-APPROVAL packet is explicitly not acked. There is a pending uncertainty about whether this assumption holds.

**Cross-object epistemic boundary disputes:**
- vs O-08: R12 is part of O-08 (Pillar C) AND a separate object O-11. The separation is useful for analysis but creates a claim-scope problem: statements about O-08 («12 constitutional rules LOCKED») must either include R12 as ack'd (which it isn't yet) or exclude it from the 12-count. Current prose includes it without this qualification.
- vs O-13: Clan members are «governed by R12» per §4 cross-ref table. But if O-13 (Clan) = 0 signatories and R12 enforcement = vapor, then «governed by R12» = two vapor objects referencing each other. The governance relationship is a future-conditional claim, not a present operational claim.

---

## §13 — O-12: Бренд / публичный слой (Jetix public-facing)

**Reference-frame stability:** Stable-as-frame; vapor-as-structure · reason: Doc 1A/1B
LOCKED; Workshop metaphor LOCKED; but no public website, no public pitch deck, no formal
ViewpointBundle definition.
[src: decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md; decisions/JETIX-CORPORATION-2026-05-05.md;
decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «Workshop metaphor = LOCKED canonical anchor» | F5 · jetix-canonical-workshop | F5 for document-LOCK. F3 for «architectural anchor»: per D-PHIL-SCOPE-2 (Task 1), Workshop CONCEPT doc lacks A.1.1 BoundedContext fields (local glossary, invariants, scope declaration). Document LOCKED ≠ formal BoundedContext declared | Refuted as «formal architectural anchor» if: JETIX-WORKSHOP-CONCEPT-2026-04-30 does not contain explicit A.1.1 fields. Verify by checking the document for glossary + invariants + scope. [src: decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md — needs direct check] |
| «Doc 1A/1B = two-view MVPK shape» | F4 · jetix-brand | F3: E.17 MVPK requires ViewpointBundle definition, audience-specification, and formal linking. Doc 1A/1B are two documents with different scopes — «two-view» is a structural observation, not a demonstrated MVPK implementation | Refuted as formal MVPK if: Doc 1A and Doc 1B do not formally declare their ViewpointBundle membership and audience-link per E.17 |
| «Brand = Jetix = Workshop metaphor» | F5 · LOCKED | F3 for the identity claim: brand identity is claimed based on a LOCKED concept document. But brand identity requires external audience recognition. No public-facing brand touchpoint exists yet (no website) | Refuted if: external audience (Levenchuk, Tseren) does not associate «Jetix» with «Workshop» framing upon hearing it |

**Use-mention concerns:**
- «Workshop» — UM-1 from Task 1 applies here: the metaphor name is simultaneously MENTIONED (as the LOCKED canonical frame name) and USED (as if it describes the structural reality of the system). When «owner = мастер» and «agents = instrumental specialists» are applied as functional role-names in prose, the metaphor has been promoted from mention to use without explicit declaration.
- «Brand» — mentioned as an object of O-12; used in Phase B outreach materials as the public-facing signal. But brand = external audience perception. Until external audiences consistently perceive Jetix-as-Workshop, «brand» = aspirational label, not operational reality.

**Anti-scope (rigorous):**
- O-12 does NOT include a public website (none exists)
- O-12 does NOT include an enterprise pitch deck (none evidenced)
- O-12 does NOT include formal E.17 MVPK bundle with ViewpointBundle declarations
- O-12 does NOT include Workshop as a formal U.BoundedContext with A.1.1 fields (per D-PHIL-SCOPE-2)
- O-12 does NOT include external audience validation of brand identity (zero external feedback captured)

**Conflation traps:**
- Trap 1 (document-LOCK = brand-established): Having a LOCKED concept document (Workshop) does not constitute an established brand. Brand establishment requires consistent external perception across interactions. Pre-brand documentation ≠ established brand.
- Trap 2 (frame=structure): Workshop metaphor provides a navigational frame for understanding Jetix. This does not mean Jetix IS structurally a workshop. A.7 Strict Distinction: the map is not the territory. Using workshop terms as structural role names (instrumental specialists) promotes the metaphor to structural claim without declaring the promotion.
- Trap 3 (MVPK-by-analogy): Doc 1A/1B are analogous to MVPK multi-view in shape; they are not implementations of E.17. «MVPK shape» ≠ «MVPK implemented».

**Hidden assumptions:**
- Assumes that the Workshop metaphor resonates with L1 audience (Levenchuk, Tseren) without having tested this. The outreach materials in outreach/pack-for-l1-2026-05-17/ use Workshop framing, but no feedback has been received.
- Assumes Doc 1A and Doc 1B are consistently maintained. The ICP inconsistency between Doc 1B §7 and ACTION-PLAN (flagged in O-10) also affects O-12 since Doc 1B is the primary brand narrative document.

**Cross-object epistemic boundary disputes:**
- vs O-05: O-12 (brand/public layer) and O-05 (methodology/pattern language) both have «external audience» claims. Brand (O-12) = how external audiences perceive Jetix NOW. Methodology (O-05) = what external adopters can do with Jetix in the future. They share audience but differ in temporal frame. Phase B prose sometimes conflates them.
- vs O-14: Meta-workshop (O-14) is partially about the external-facing architecture of Jetix-as-platform-for-others. O-12 (brand) should be consistent with the meta-workshop framing of O-14. But O-14 is vapor; if O-12's brand is built around Workshop metaphor (single-owner workshop), and O-14's vision is meta-workshop (platform for multiple masters), the brand claim may need revision when O-14 becomes operational.

---

## §14 — O-13: People-Network-State / Clan vision (сетевой паттерн)

**Reference-frame stability:** Stable-as-charter; vapor-as-instantiation · reason: Clan
Charter v0 LOCKED 2026-05-12 (artefact stable); 0 signatories confirmed; community object
does not exist operationally.
[src: decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md; decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «H7 People-Network-State LOCKED = stable strategic insight» | F5 · jetix-canonical | F5 for the document-LOCK. F3 for the insight-validity: «People-Network-State» as a strategic direction has no external validation (0 signatories; stealth; no market test) | Refuted as validated strategic direction if: first signatory acquisition fails to materialize within 60 days (per Task 1 inventory falsifier) |
| «6 archetypes × RoleAlgebra = Clan composition» | F4 · charter-applied-now | F3: the 6 archetypes are declared in the charter; RoleAlgebra (A.2.7) is cited as applicable. But RoleAlgebra requires that the ⊗ operator has defined semantics for this specific set of roles. No such semantics are declared in the charter | Refuted if: Clan first signatory is not classifiable into one of the 6 archetypes |
| «R12 = constitutional guarantee for Clan members» | F5 (text reference) | F2 for operational guarantee: as per O-11 analysis — R12 text exists; enforcement = vapor; AWAITING-APPROVAL not acked; no bilateral agreement exists with any Clan member (0 members). The guarantee is a future-conditional claim | Refuted as present guarantee if: any Clan membership interaction occurs without R12 scope being explicitly declared to the new member |

**Use-mention concerns:**
- «Clan» — used as the name of an existing organizational entity. But 0 signatories = no entity exists. The charter MENTIONS a Clan; it does not USE a name for an existing group. Present-tense descriptions of Clan properties («members can fork-and-leave», «6 archetypes govern composition») use language appropriate for an existing entity applied to a vapor concept.
- «Stealth launch» — MENTIONED as a strategy (for when the launch occurs). USED implicitly to explain the current absence of public evidence. But «stealth» presupposes something exists to be stealthy about. Without any members, «stealth launch» is a label applied to pre-existence.

**Anti-scope (rigorous):**
- O-13 does NOT include 5 or more signatories (confirmed 0)
- O-13 does NOT include public-phase activity
- O-13 does NOT include cooperative formation (no legal entity)
- O-13 does NOT include operational R12 enforcement for Clan members (enforcement vapor as per O-11)
- O-13 does NOT include people who have reviewed or responded to the Clan Charter

**Conflation traps:**
- Trap 1 (charter=community): Having a LOCKED charter does not make a community. The charter is a U.WorkPlan for community formation; it is not U.Work evidence of a formed community.
- Trap 2 (Balaji-reference conflation): Clan is conceptually adjacent to Balaji's Network State thesis (per H5 = BALAJI-NETWORK-STATE insight). But conceptual adjacency ≠ implementation path. The Balaji reference provides intellectual pedigree, not operational guidance.
- Trap 3 (R12-as-active-protection): R12 cited as «constitutional guarantee for Clan members» when there are no Clan members. The protection is declared for a population that does not yet exist. This is logically valid (conditional declaration) but may mislead if read as present-active protection.

**Hidden assumptions:**
- Assumes «professional masters with their own workshops» are a discoverable, reachable audience for Clan membership. No market-research evidence for this ICP exists.
- Assumes the 6 archetypes are exhaustive and non-overlapping. No stress-test of the taxonomy against potential signatories has been attempted.
- Assumes stealth launch is operationally superior to public launch for early signatory acquisition. No comparative evidence.

**Cross-object epistemic boundary disputes:**
- vs O-14: O-13 (Clan = members) and O-14 (meta-workshop = platform) are distinct but interdependent. Clan members are the target participants for the meta-workshop. Without Clan activation, O-14 has no participants. Both are vapor; the cascade from one vapor to another is not addressed.
- vs O-05: Clan (O-13) and methodology (O-05) both depend on Phase C activation. If Phase C does not activate, neither O-05 nor O-13 progresses. Their shared dependency is not explicitly stated.

---

## §15 (was §14) — O-14: Meta-workshop для профессиональных мастеров (Phase B target)

**Reference-frame stability:** Vapor · reason: concept-only framing from Doc 1B §0;
no implemented partner instances; no formal partner-Jetix interoperability protocol;
far Phase B+ target.
[src: decisions/JETIX-CORPORATION-2026-05-05.md §0; JETIX-WORKING-FILE-v0 §3.3]

**Top claims with epistemic calibration:**

| Claim | Stated F-G-R | Phil-assessed F-G-R | Falsifier (Popperian) |
|---|---|---|---|
| «Jetix = мета-мастерская для профессиональных мастеров со своими мастерскими» | F4 (Doc 1B §0 concept) | F2: this is a marketing/vision statement in a conceptual document. «Мета-мастерская» is a metaphor, not a specification. No A.1 holon-type declaration, no A.1.1 BoundedContext, no partner-instance specifications | Refuted as «implemented meta-workshop» by the absence of any partner instance. Observable: count partner-instances in repo. Current count = 0. |
| «Each partner-instance = fork + specialise (A.5 Kernel Modularity)» | F4 (conceptual) | F2: A.5 Kernel Modularity is cited as applicable, but no partner-instance has been forked or specialised. The modularity claim has zero operational evidence | Refuted if: no partner attempts to fork Jetix pattern for their own domain within Phase B timeline |
| «R12 becomes canonical guarantee binding partner-instances when Meta-workshop activates» | F4 · jetix-phase-B-framing | F2: future-conditional claim («when this activates»). R12 itself has enforcement vapor (O-11 analysis). A future-conditional with a vapor antecedent is doubly uncertain | Refuted as «canonical guarantee at activation» if: activation occurs without bilateral R12 agreement with each partner |

**Use-mention concerns:**
- «Meta-workshop» — Doc 1B §0 uses this term in TL;DR summary, present tense («Jetix is a meta-workshop»). But as a U.System object, meta-workshop does not exist operationally. The present-tense USE is writing fiction about a future state — a narrative device, not an ontological claim.
- «Professional masters with their own workshops» — MENTIONED as the target partner archetype. USED in subsequent analysis as if such partners exist and are identifiable. The population is a conceptual target, not an enumerated set.

**Anti-scope (rigorous):**
- O-14 does NOT include implemented partner instances (zero)
- O-14 does NOT include formal protocol for partner-Jetix interoperability
- O-14 does NOT include Phase C IWE cooperation realized
- O-14 does NOT include any binding with FPF community (Levenchuk has only been contacted; no agreement exists)
- O-14 is NOT operational at any scale, micro or otherwise

**Conflation traps:**
- Trap 1 (description=instantiation): Describing a meta-workshop architecture in Doc 1B does not instantiate it. This is the same A.4 Temporal Duality trap as O-03 and O-07, applied to the most vapor object in the inventory.
- Trap 2 (B.2 MHT-as-endorsement): B.2 Meta-Holon Transition is cited as applicable. Citing an FPF pattern as applicable to a future object does not make the object more real. FPF patterns are analytical tools for describing transitions; using them in advance of the transition is speculative application.
- Trap 3 (Phase-B-target-as-Phase-B-deliverable): «Phase B target» in the object name implies this will be delivered in Phase B. But Phase B = FPF scope definition (this cycle). O-14 is a Phase B+ aspiration, not a Phase B deliverable. The naming creates scope-creep pressure.

**Hidden assumptions:**
- Assumes that the meta-workshop framing is stable enough to use as an L1 audience anchor (Levenchuk, Tseren). If L1 audience finds the framing confusing or inaccurate, the entire Phase B outreach may need reframing.
- Assumes that «professional masters with their own workshops» would want to join a meta-workshop governed by a single-owner's principles (Ruslan's). The governance structure (R12, Pillar C) is designed for Ruslan as primary owner. How it extends to partner-owners is unspecified.
- Assumes O-14 and O-13 (Clan) are compatible or identical in their member populations. They may not be: Clan = loose collective of independent professionals; meta-workshop = structured platform with Jetix as substrate host. These are different value propositions.

**Cross-object epistemic boundary disputes:**
- vs O-05: O-14 (meta-workshop as activation context) and O-05 (methodology as forkable pattern) are mutually dependent: meta-workshop needs a methodology to host; methodology needs a meta-workshop to demonstrate. Both are vapor; their mutual dependency is the central cascade risk for Phase C.
- vs O-12: O-14's framing («мета-мастерская») and O-12's brand framing («мастерская для работы с информацией») are in tension: O-12 = single workshop (Ruslan's); O-14 = platform for multiple workshops. If brand (O-12) is built on single-workshop framing, the meta-workshop rebrand (O-14) will require brand revision. This dependency is not flagged anywhere in current Phase B outputs.

---

## §16 Aggregate Epistemic Concerns — Categories of Conflation Across All 14 Objects

This section extends CE-1..CE-5 from Task 1 inventory to 14 objects with categorized
patterns.

### AEC-1 (Extension of CE-3): Artefact-lock vs operational-system gap

**Scope:** O-03 (vision), O-07 (Foundation), O-08 (Pillar C), O-09 (Hexagon), O-11 (R12),
O-12 (brand), O-13 (Clan) — at minimum.

**Pattern:** F-G-R applied to document-lock status (A.16 language-state) is being used
as if it applies to operational-system maturity. The two subjects of the F-level claim
(the document vs the system) are conflated throughout Phase B output.

**Aggregate falsifier:** For each LOCKED object, two distinct F-G-R triples are needed:
(a) for the document as document, (b) for the system described by the document. Currently
only (a) is consistently assigned; (b) is either absent or carried as an informal
«working-partially» qualifier.

### AEC-2 (Extension of CE-2): IP-1 type/token conflation propagates beyond O-06

**Scope:** O-01 («12 agents» in one-liner), O-04 (product description cites «12 agents»),
O-06a (type-declarations), O-06b (executor-bindings), O-07 (Foundation Part 4 «role taxonomy»),
O-12 (mermaid «12 Specialized Agents × 6 Departments»).

**Pattern:** The 12-role-types declaration is used as evidence of 12 operational agents
wherever a system-complexity claim is made. IP-1 split is correctly declared in
Foundation (Part 4 + RUSLAN-LAYER) but NOT consistently applied to prose descriptions
across Phase B artefacts.

**Aggregate falsifier:** «12 agents» claim refuted as «12 running processes» by any
enumeration of sessions-with-dispatched-agents in the last 30 days (expected result:
ROY swarm 6 + occasional others, not 12 simultaneous).

### AEC-3 (Extension of CE-4): Promise-without-commitment-machinery

**Scope:** O-02 (TRM promises), O-10 (TRM activation path), O-11 (R12 guarantee),
O-13 (Clan R12 protection), O-14 (partner binding at activation).

**Pattern:** Promise-shaped language («substrate will not extract», «fork-and-leave
without penalty», «L0-L5 ladder = activation path») appears without U.Commitment (A.2.8)
machinery: no holder-of-obligation named, no adjudication path, no receipt mechanism,
no bilateral execution evidence.

**Aggregate falsifier:** For each promise-shaped claim, the U.Commitment test: Does a
specific holder, a specific obligee, a specific adjudication path, and a specific receipt
mechanism exist? If any element is missing, the claim is a promise-text (U.Episteme),
not an operational commitment (U.Commitment). Currently all such claims fail the test.

### AEC-4 (New): Use-mention-drift in framing objects

**Scope:** O-08 (Workshop), O-12 (Workshop as brand anchor), O-13 (Clan metaphor),
O-14 (Meta-workshop as description).

**Pattern:** Named metaphors (Workshop, Clan, Meta-workshop) are first MENTIONED as
conceptual frames (clearly valid), then USED as structural predicates (implying structural
properties they haven't been certified to have). The promotion from mention to use is
never declared explicitly, creating a progressive accumulation of unverified structural
claims that look like design decisions.

**Aggregate falsifier:** Per metaphor object: does the document containing the metaphor
also contain formal structure declarations (A.1.1 glossary + invariants + scope)? If not,
the metaphor is properly mention-level; all structural USE of the metaphor terms requires
separate declaration.

### AEC-5 (Extension of CE-1): Language-state collapse across temporal registers

**Scope:** O-02 (present-tense description of vapor corporation), O-04 (internal-product
labeled as commercial product), O-05 (forkable claimed without forks), O-10 (ICP
inconsistency across time), O-13 (charter described in present tense for 0-member Clan),
O-14 (meta-workshop described in present tense for uninstantiated platform).

**Pattern:** Documents written in present tense make claims about objects that exist
only in future-conditional or aspirational form. A.16 language-state transduction is
not applied: the language-state of each claim (design-time / in-progress / operational)
is not declared. CE-1 from Task 1 applies specifically to project-count; AEC-5 extends
it to all objects with vapor or aspirational status.

**Aggregate falsifier:** For each present-tense claim about an aspirational/vapor object,
the falsifier test: can the claim be verified by an independent observer today without
reference to future plans? If not, the claim should be in future-tense or conditional
form, with A.16 language-state declared.

---

## §17 Dissents Preserved + Open Questions

### Preserved dissents (carried forward from Task 1, now grounded per-object)

**D-2 (O-07 typing dispute):** Foundation = U.System + U.Mechanism (eng) vs
U.Episteme / U.MethodDescription (phil). Per §8 analysis: both faces are simultaneously
true of different parts of Foundation (some Parts operational = U.Work evidence; most
Parts spec-only = U.Episteme describing intended system). The dispute is resolved as
«both faces are present; different Parts correspond to different faces». Not a binary.

```yaml
held_by: [engineering-expert cell (D-2), philosophy-expert × critic (this cell)]
F: F4
ClaimScope:
  holds_when: "typing question = which face of Foundation is operative for FPF scope claim"
  not_valid_when: "typing question = whether Foundation documents are well-written"
R:
  refuted_if: "FPF Part A authors clarify U.System vs U.MethodDescription boundary for design-locked artefacts"
  accepted_if: "both-faces framing is adopted in Phase 0 output (separate F-G-R per face)"
reconciliation: "Not resolved. Ruslan decides which face is primary for FPF scope (OQ-3 from Task 1)"
```

**D-PHIL-SCOPE-2 (Workshop metaphor status):** LOCKED canonical anchor vs narrative-only
frame without A.1.1 fields. Per §13 analysis: the document LOCK is valid (F5); the
architectural-anchor claim requires A.1.1 fields that have not been verified to exist
in JETIX-WORKSHOP-CONCEPT-2026-04-30.

```yaml
held_by: philosophy-expert × critic (this cell)
F: F4
ClaimScope:
  holds_when: "FPF formal BoundedContext discipline is claimed for the Workshop frame"
  not_valid_when: "Workshop functions as narrative-only orientation frame (per Ruslan's original use)"
R:
  refuted_if: "JETIX-WORKSHOP-CONCEPT-2026-04-30 contains explicit A.1.1 fields"
  accepted_if: "document is narrative without formal A.1.1 structure (requires direct file check)"
reconciliation: "Preserved per AP-6. Ruslan decides per OQ-4 (Task 1)."
```

### New open questions surfaced by per-object deep-dive

**OQ-A (AEC-1 aggregate).** Should Phase 0 output require TWO F-G-R triples per object
where artefact-lock ≠ operational status: one for document and one for system? Or is
single F-G-R per object adequate if the subject is explicitly declared?

**OQ-B (AEC-3 aggregate).** Which of the promise-shaped claims (TRM ladder activation,
R12 guarantee, Clan protection) are intended to be U.Commitments (A.2.8) requiring
adjudication-path specification? Or are they U.Episteme texts (design intentions without
enforcement path for now)?

**OQ-C (AEC-4 per-object).** For each metaphor-named object (Workshop, Clan,
Meta-workshop): is the metaphor operating as mention (navigational frame) or use
(structural claim)? If use is intended, when and how will A.1.1 formalisation occur?

**OQ-D (O-10 ICP inconsistency).** Doc 1B §7 (Mittelstand DACH ICP) vs ACTION-PLAN
§0 (Online-first ICP) — which is current? This is not a philosophy question: it is
a factual inconsistency between two LOCKED documents that affects O-10 and O-12.

**OQ-E (O-14 brand tension).** O-12 brand = single-workshop (Ruslan as solo master).
O-14 meta-workshop = platform for multiple masters. These are different value propositions.
When and how is the brand (O-12) intended to evolve to accommodate O-14 framing?

---

## Conformance Checklist (§3.1 critic self-check)

| Check | Result | Evidence |
|---|---|---|
| 1. Falsifier-named (Popper) | pass | Every object §1-§15 (O-01 through O-14) carries ≥3 claims with explicit Popperian falsifier conditions |
| 2. Paradigm-named on shift (Kuhn) | pass | AEC-1 names the artefact-lock vs operational-system paradigm distinction; CE-3/D-2 cite A.4 Temporal Duality as the applicable paradigm frame |
| 3. Mental-model + conditions cited (Munger) | pass | A.4 / A.7 / A.16 / A.2.8 / B.5.2 cited with applicable conditions per object |
| 4. Method declares what it is NOT (via-negativa) | pass | Every object has Anti-scope block with ≥3 items; §17 anti-scope inherited |
| 5. Dichotomy-of-control for meta-decisions | pass | Reference-frame stability column per object separates in-control (O-04, O-06a, stable artefacts) from not-in-control (O-13, O-14, O-02 = vapor) |
| 6. Fallacy-named-when-named | pass | No fallacy accusations; categorical errors named with FPF-pattern citation (A.4 / A.7 / A.16 / IP-1) |
| 7. Meta-claim grounded in object-level | pass | Every aggregate claim (AEC-1..AEC-5, EP-1..EP-5) grounded in ≥2 specific object-level instances with source citations |

**BA-Cycle-lite:** BA-0 = NO (epistemic inventory; not capital memo or life-affecting decision). Not required.

---

## Acceptance Predicate (§3.2 Hamel-binary)

```
acceptance_predicate: "All 14 objects (O-01..O-14) covered, each with ≥3 claims
carrying Popperian falsifiers AND ≥1 use-mention concern with object-level example
AND ≥3 anti-scope items AND ≥1 conflation trap AND ≥1 hidden assumption AND ≥1
cross-object boundary dispute; AND 5 aggregate epistemic patterns (AEC-1..AEC-5)
named with aggregate falsifiers; AND all dissents preserved (AP-6) without resolution;
AND zero recommendations emitted (R1 compliant)."
```

This predicate holds over this artefact as written: 14 objects covered; each with
≥3 falsified claims, ≥1 use-mention analysis, ≥3 anti-scope items, ≥1 conflation trap,
≥1 hidden assumption, ≥1 cross-object dispute; 5 aggregate patterns; 2 preserved
dissents + 5 new OQs; 0 recommendations.

---

## Anti-scope (What This Critic Did NOT Do)

- Did NOT recommend which object should be primary for Phase 0 FPF scope — Ruslan decides (R1).
- Did NOT assess whether ICP revision from Mittelstand to Online-first is strategically correct — strategic decision per Tier 2 Rule 1.
- Did NOT evaluate whether Levenchuk's C3 critique is «right» — surface facts only.
- Did NOT produce a corrected inventory — next cycle's optimizer or integrator pass.
- Did NOT run engineering critique on code, schemas, or infrastructure — engineering-expert scope.
- Did NOT arbitrate instrumental Рациональность — what to DO with these findings — investor-expert scope.
- Did NOT assess whether Phase B outputs are «good» or «bad» — surfaced categorical distinctions only.
- Did NOT attempt to resolve D-2 or D-PHIL-SCOPE-2 dissents — preserved per AP-6.

---

*Draft produced by philosophy-expert × critic. Mode: critic per §3. Task 2, Phase 0 FPF scope definition.
Read order: this file → agents/philosophy-expert/system.md → swarm/lib/shared-protocols.md →
agents/philosophy-expert/strategies.md → 01-jetix-objects-inventory.md → cited source paths.
Brigadier promotes; this cell does not. §5.5.5 gate: provenance inline ✓ tier coherence ✓
dissents preserved per AP-6 ✓ non-recommendation R1 ✓ 14 objects covered ✓ acceptance predicate holds ✓.*
