---
title: Philosophy × Critic — Epistemic Hygiene Audit
type: critique
layer: drafts
niche: meta
task_id: T-km-architecture-research-2026-04-24
cycle_id: cyc-km-architecture-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
last_reviewed: 2026-04-24
pipeline: ingested
state: drafted
confidence: high
confidence_method: expert-judgment-from-tier1-citations
tier: tier-1
produced_by: philosophy-critic
sources:
  - prompts/km-architecture-research-2026-04-24.md
  - decisions/JETIX-PHILOSOPHY.md
  - decisions/JETIX-ARCHITECTURE-BRIEF.md
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - .claude/agents/philosophy-expert.md
related: []
binding_scope: km-architecture-philosophy-lens
mode: critic
---

# Philosophy × Critic — Epistemic Hygiene Audit

**Artefact under consideration.** The *epistemic substrate* on which the
6 forthcoming KM+PM architecture variants will make their claims — specifically
the claim-families UC support ("this variant supports UC-9"), scale-survival
("scales without re-architecture to $1T"), anti-fragility ("gets better with
scale"), and moat-preservation ("offline-first inference preserves Jetix's
competitive moat"). No variant text exists yet; this critic audits the
substrate those claims will be required to sit on.

**Predicate for this return.** "Returns ≥5 binary Conformance Checks for
epistemic hygiene (falsifiability + multiple-alternatives-considered +
Anti-scope-explicit + supersession-chain-invariant + F-G-R-discipline) AND
≥2 alternatives per check AND Anti-scope AND flags every 'works at scale'
assertion as candidate falsification target AND each row F/ClaimScope/R triple."

---

## §1 Conformance Checklist (5 binary checks)

| # | Check | Verdict | F | ClaimScope | R |
|---|---|---|---|---|---|
| H-1 | Does the F-G-R triple framework (JETIX-ARCHITECTURE-BRIEF §4 + FPF E-5) make every forthcoming "scales to $1T" claim falsifiable **in advance** — i.e., each claim carries an explicit `R.refuted_if` field naming the observable that would constitute refutation, not merely an `R: high` label? | **NO** | F3 | km-variants-generation-phase | medium |
| H-2 | Does the existing supersession chain (D3 §3.2 `supersedes` edge + α-2 artefact state machine: `drafted → reviewed → accepted → superseded`) preserve a coherent audit trail when a client-isolated claim (per UC-9 client's private KB) conflicts with a Jetix-central claim — i.e., is the supersession edge type unambiguous across the Jetix-central / client-local boundary? | **NO** | F2 | wiki-v3-spec-boundary | medium |
| H-3 | Does the Lakatos hard-core/protective-belt discipline have a concrete counterpart in the wiki v3 spec, such that forthcoming variants cannot accidentally propose changes that re-open the 24 Locks (hardcore) under the framing of "variant design"? | **NO** | F3 | wiki-v3-foundations-layer | low |
| H-4 | Can the contradiction-detection mechanism (UC-7, `/lint` Q5 signal #4, `contradicts` edge) operate across clients in a federated multi-client deployment without leaking client-private content across the UC-9 isolation boundary? | **NO** | F2 | federated-client-deployment-boundary | low |
| H-5 | Does the universality test (JETIX-PHILOSOPHY §10 B/C/D) pass on the proposed local-LLM offline-first KM stack — i.e., is the architecture universalisable across Jetix's 8 active projects AND Mittelstand client deployments AND Phase-B Roy-clone instantiations — such that the `base/` symbolic test (grep for "Jetix|DACH|AI consulting|Mittelstand" → 0 hits) can still pass after the UC-9/UC-10 mechanics are embedded? | **CONDITIONAL** | F3 | universality-criterion-base-layer | low |

**Summary.** Four of five checks return NO; one is CONDITIONAL. This is not
a failure state for the KM research cycle — the variants have not been drafted
yet. It is an advance warning: these four gaps must be explicitly addressed in
the variant design, not discovered post-hoc when brigadier runs its gate-check.

---

## §2 Acceptance Predicates (per "no")

### H-1 — F-G-R falsifiability deficit

**Acceptance predicate for the forthcoming variants:**

> "Every claim in every variant of the form 'this architecture supports UC-N'
> or 'this architecture survives gate G at scale S' carries a triple with
> populated `R.refuted_if` field naming an observable measurement — not merely
> `R: high`. A claim is accepted only when `R.refuted_if` is non-empty and
> specifies a concrete observable (e.g., 'p95 retrieval latency exceeds 3s at
> 5,000 pages', or 'client-B data returned in ≥1 of 10 pen-test runs')."

Predicate is Hamel-binary: either `R.refuted_if` is populated with a named
observable on every major claim, or the variant fails H-1.

**Provenance.** JETIX-ARCHITECTURE-BRIEF §4.6 (continuous quality metrics,
F-G-R per-agent mandatory): "F-G-R frontmatter (formality F0-F9 / scope /
reliability R-low|medium|high|certified|formally-proven)"; FPF E-5 (integrator
adds `F:` + `ClaimScope:` + `R:` per claim, declares not computes).
JETIX-PHILOSOPHY §6: "Fractal quality — паттерн повторяется на всех масштабах."

---

### H-2 — Supersession chain integrity across client boundary

**Acceptance predicate:**

> "Every variant that introduces client-isolated KBs specifies — in its UC-9
> proof section — the edge-type policy for cross-boundary `supersedes`
> relationships: either (a) cross-client `supersedes` edges are FORBIDDEN by
> the `graph/edges.jsonl` schema (simplest; each client's graph is a closed
> holon), or (b) Jetix-methodology `supersedes` edges point FROM Jetix-central
> TO client-local wikis (methodology push, per STRATEGIC-INSIGHT §3) but NEVER
> the reverse, and the `/lint` check enforces the directionality."

Predicate is Hamel-binary: either the cross-boundary edge policy is explicitly
stated in the variant's UC-9 proof section, or the variant fails H-2.

**Provenance.** prompts/km-architecture-research-2026-04-24.md §3.9 (UC-9):
"cross-client edges in `graph/edges.jsonl` are FORBIDDEN; the only edges from
Client-A KB point to Jetix methodology repo, not to other clients";
STRATEGIC-INSIGHT §3: "Methodology push, data no pull."

---

### H-3 — Lakatos hard-core enforcement (variant proposals cannot re-open Locks)

**Acceptance predicate:**

> "The variant design phase is gatekept by a pre-check: brigadier's intake
> (Phase 1) runs a symbolic scan — any variant section that modifies or
> contradicts a 24-Lock item is flagged `lock-violation` before work-phase
> dispatch, not discovered at gate-check. The scan is expressed as a
> named check in brigadier's critic rubric or as a pre-commit hook equivalent,
> not as a verbal reminder."

Hamel-binary: either a machine-checkable lock-violation scan fires before
variant drafts are accepted into work-phase, or H-3 fails.

**Provenance.** JETIX-ARCHITECTURE-BRIEF §6 (hard constraints): "Any variant
violating any of these is disqualified without review of the rest."
Philosophy-expert §2.3 (P3 Lakatos): "refutations hit the belt first, then
the core." The 24 Locks ARE the hard core; variant-design heuristics are
the protective belt.

---

### H-4 — Federated contradiction detection without cross-client data leakage

**Acceptance predicate:**

> "Every variant that claims UC-7 contradiction detection capability in a
> multi-client federated deployment must show — in the UC-7 failure-mode
> trace — that `/lint` operates per-client on an isolated filesystem tree,
> and that no inter-client contradiction can be detected *directly* (i.e.,
> the system cannot compare Client-A's claim about X with Client-B's claim
> about X without first anonymizing or redacting both, or operating only
> within per-client graphs). UC-7 at the Jetix-central level operates only
> over the Jetix-methodology repo, never over client KBs."

Hamel-binary: either the federated `/lint` boundary is explicitly stated in
the variant's UC-7 section with the client-isolation constraint honoured, or
H-4 fails.

**Provenance.** prompts/km-architecture-research-2026-04-24.md §3.7 (UC-7):
"variant specifies how `/consolidate` discovers the semantic equivalence";
§3.9 (UC-9): "architecture must make [cross-client data access] impossible
by construction." These two UCs are in tension; the variant must resolve
that tension explicitly.

---

### H-5 (conditional) — Universality criterion under UC-9/UC-10 constraints

**Acceptance predicate:**

> "The base/ symbolic test (grep `Jetix|DACH|AI consulting|Mittelstand` → 0
> hits) passes even after UC-9 client-isolation mechanics and UC-10
> offline-first inference mechanics are embedded. Concretely: client-isolation
> is implemented as configurable parameters (client-id, filesystem-root,
> agent-scope-key), not as Jetix-specific hardcodes in base/. The local-LLM
> model family is declared as a config field, not as a specific model name
> baked into base/. A third hypothetical use case (not Jetix, not DACH,
> e.g., astronomer per JETIX-PHILOSOPHY §10 C-test) can instantiate UC-9
> and UC-10 without modifying base/."

Hamel-binary: either the universality test passes post-UC-9/UC-10 mechanics,
or H-5 fails.

**Provenance.** JETIX-PHILOSOPHY §10: "B: ≥90% design choices configurable.
C: base works for Jetix-company + astronomer + animal-husbandry without
modification. D: `grep base/ -r 'Jetix|DACH|AI consulting|Mittelstand'` → 0."
JETIX-ARCHITECTURE-BRIEF §5.5 (portability): "Symbolic test applies to
`base/` repo subtree (source code / config)."

---

## §3 Alternatives (≥2 per "no")

### H-1 alternatives — how to enforce falsifiability on scale claims

**Status quo kill-condition:** "Works at scale" phrases remain prose; reviewer
catches them at gate. Kill condition: "reviewers miss > 30% of bare assertions
under time pressure" (documented in brigadier anti-pattern AP-25, missing
acceptance predicate).

**Alternative A — Schema enforcement (preferred).** Variant template (§5.1
of execution prompt) includes a mandatory `claims[]` frontmatter section; each
claim entry requires `F:`, `ClaimScope:`, `R.refuted_if:`. Brigadier's gate-check
(Phase 5) runs a structural lint: any variant with empty `R.refuted_if` on a
UC-support or scale-survival claim is returned to the emitting expert.
Kill-condition for A: "the template adds friction and variants are returned
repeatedly, slowing the cycle beyond the 4-8 hour budget."

**Alternative B — Post-draft critic pass (current approach, enhanced).** After
variant drafts land, philosophy × critic runs a second pass explicitly checking
`R.refuted_if` population per claim. Kill-condition for B: "second pass
discovers falsifiability gaps at gate-check, not during drafting — this makes
fixing expensive (return to work-phase, redraft relevant sections)."

**Alternative C — Fluency heuristic only (weakest).** Instruct variants via
the execution prompt's disqualifying anti-patterns list to avoid specific
phrases (§5 of this document). Kill-condition for C: "phrase-level prohibition
cannot catch semantically equivalent non-falsifiable claims phrased differently."

Verdict: Alternative A is strongest (structural prevention beats detection).
Alternative B is the fallback. Alternative C is the minimum floor — it is
adopted unconditionally as §5 of this document regardless of which alternative
Ruslan picks for the schema decision.

---

### H-2 alternatives — supersession edge policy across client boundary

**Status quo kill-condition:** Edge policy is left implicit; each variant
defines its own edge semantics. Kill-condition: "two variants disagree on
whether cross-client `supersedes` edges are allowed, producing contradictory
UC-9 proofs that brigadier cannot reconcile at integration."

**Alternative A — Closed-holon policy (strict).** Each client's `graph/edges.jsonl`
is a sealed graph. No inter-graph edge types involving two different clients.
Methodology updates propagate by git-pull of the Jetix-methodology remote,
which adds new files and new within-methodology edges — never cross-client
edges. Kill-condition: "client cannot reference Jetix-methodology concepts
by typed edge, only by path import — reduces graph expressiveness."

**Alternative B — Directed push-only edges.** A narrow set of edge types
(`methodology-update-supersedes`, `methodology-push-delivers`) are permitted
FROM Jetix-central TO client-local, but by construction carry zero client-
private data in their payloads (they point to methodology versioned commit
SHA, not to client content). The `/lint` enforcer checks directionality:
any edge FROM client-local TO Jetix-central is flagged `isolation-violation`.
Kill-condition: "directionality enforcement requires a custom `/lint` signal
that adds implementation complexity at UC-9 proof level."

Verdict: Alternative A is architecturally simpler and more conservative
(closed-holon aligns with the STRATEGIC-INSIGHT §3 "methodology push, data
no pull" principle). Alternative B is more expressive but requires additional
lint signal. Recommend A for Phase-A materialization, B for Phase-B if
Mittelstand Alliance coordination requires richer edge semantics.

---

### H-3 alternatives — Lakatos hard-core enforcement

**Status quo kill-condition:** Brigadier's verbal reminder "respect 24 Locks"
in the execution prompt. Kill-condition: "a variant section inadvertently
proposes a mechanism that changes how the wiki write-protocol works (Q2
single-writer), which is a de-facto Lock revision, but this is not caught
until a HITL gate review."

**Alternative A — Pre-flight lock-scan in brigadier intake.** Brigadier's
Phase 1 (intake) includes a named step: grep variant-proposal text for
keywords corresponding to each of the 24 Locks (D17, Q2, D13, etc.) and
flag any section that proposes to change the locked behaviour. Kill-condition:
"keyword scan misses structural lock violations (e.g., proposing 'Notion
as primary KB' without using the word 'authoritative')."

**Alternative B — Lock-compliance checklist as a mandatory section in every
variant template.** Each of the 6 variant drafts contains a `§ Lock compliance`
section that enumerates all 24 Locks and states pass/fail/na per lock.
Philosophy × critic reviews this section explicitly. Kill-condition: "adds
≥24-row compliance table to every variant, inflating word count and adding
mechanical work."

Verdict: Alternative B is more complete (explicit coverage of all 24 Locks)
and is aligned with how JETIX-ARCHITECTURE-BRIEF §6 already operates
(it lists hard constraints). Recommend Alternative B as the variant template
format; brigadier's lock-scan (Alternative A) supplements as a pre-flight
check.

---

### H-4 alternatives — Federated contradiction detection without leakage

**Status quo kill-condition:** UC-7 and UC-9 are specified as separate
acceptance criteria without explicit mutual constraint. Kill-condition:
"a variant proposes a global contradiction-detection sweep that reads all
client KBs simultaneously, satisfying UC-7 while violating UC-9 — the
tension is not caught until integration."

**Alternative A — Per-client-only lint with Jetix-central lint over
methodology-only.** `/lint` is instantiated per-client as a separate
process with access only to that client's filesystem tree. Jetix-central
runs its own `/lint` over the Jetix-methodology repo only. Cross-client
contradictions are by definition undiscoverable by the system — the human
(Ruslan) who notices a cross-client pattern must manually flag it as a
methodology update (anonymized), which then propagates to all clients
via methodology push. Kill-condition: "genuinely cross-domain insights that
would benefit all clients are lost because the system cannot surface them
without violating UC-9."

**Alternative B — Federated lint with client-side summarization.** Each
client's `/lint` produces a contradiction summary (claim slugs + stance, no
content). These slugs — not content — are aggregated by Jetix-central to
detect when multiple clients have contradictions on the same methodology-
concept. Client-specific content is never transmitted; only the slug (which
is derived from Jetix-methodology vocabulary, not client-private data).
Kill-condition: "slug matching can inadvertently reveal which clients have
which conceptual conflicts — potentially commercial intelligence about client
problems."

Verdict: Alternative A is safest and simplest for Phase-A. Alternative B
is richer but requires a slug-normalisation standard to avoid inferential
leakage. Recommend A for Phase-A; B as a Phase-B research item once
Mittelstand Alliance formalization (STRATEGIC-INSIGHT §9 Q3) is settled
legally.

---

## §4 Anti-scope

This critic is explicitly NOT doing the following:

- **NOT evaluating specific variant mechanics** — no variant text exists yet;
  this audit operates on the epistemic substrate, not on variant-specific
  design choices (which methodology files to read, which retrieval tier to
  use, which local LLM family to support).

- **NOT arbitrating instrumental Рациональность** — the question "should
  Jetix pursue Path A vs Path B vs Path C for client hosting" (STRATEGIC-INSIGHT
  §5) is an investment-decision that belongs to investor-expert. This critic
  audits only whether each path's epistemic claims are falsifiable.

- **NOT reopening the 24 Locks** — this critic flags when variant claims
  risk violating Locks (H-3 above), but does not adjudicate whether a Lock
  should be revised. Lock revision requires HITL ack (JETIX-ARCHITECTURE-BRIEF
  §6 binding).

- **NOT producing the corrected variants** — that is the responsibility of the
  work-phase cell that drafts each variant. This document produces the
  acceptance predicates and the falsifiability flag list; the variants must
  satisfy those predicates.

- **NOT assessing local-LLM model capability** (which model is better, which
  quantization suffices) — that is engineering-expert territory (domain code
  and performance review).

- **NOT assessing capital impact of Path A/B/C or Mittelstand Alliance
  formation** — that is investor-expert territory (FPF L1003-1006 epistemic
  vs instrumental boundary).

---

## §5 Falsifiability flag list (forbidden phrases for downstream cells)

Every phrase below, if used in a variant draft WITHOUT an accompanying
`R.refuted_if` field, constitutes an anti-pattern (AP-PHIL-1:
claim-without-falsifiability). The integrator-mode and scalability-mode cells
MUST treat these phrases as candidate falsification targets and either (a)
replace them with a claim carrying a named observable falsifier, or (b)
explicitly demote them to F0 (rumour/aspiration) with `R: low`.

| # | Forbidden phrase (pattern) | Epistemic anti-pattern | Required replacement form |
|---|---|---|---|
| F-1 | "trivially scales" / "scales naturally" / "scales without issue" | Non-falsifiable scale claim (AP-PHIL-1) | "Scales until [named physical threshold]; refuted if [observable] exceeds [metric]." |
| F-2 | "obviously preserves the moat" / "moat is preserved" | Non-falsifiable competitive claim | "Moat claim is falsified if a competitor deploys equivalent local-first architecture with equivalent client-isolation proof within [timeframe]." |
| F-3 | "naturally federates" / "federation is straightforward" | Non-falsifiable architecture claim | "Federates under conditions [X]; fails to federate when [Y] — e.g., when cross-client edge policy is not enforced at filesystem permission level." |
| F-4 | "supports UC-N" (bare, without trace) | Missing acceptance trace (AP-25) | Full UC-N trace: "input → wiki paths touched → agent invoked → write-back fires → citation chain emitted." |
| F-5 | "works offline" / "offline-first" (bare) | Non-falsifiable infrastructure claim | "Inference path requires zero external API calls for [named query type]; falsified if [any network call observed during pen-test scenario with client-private query]." |
| F-6 | "client data is isolated" (bare, without construction proof) | Policy-claim disguised as architecture claim (UC-9 disqualifying anti-pattern) | Named proof: "proof by filesystem isolation / cryptographic scoping / federated holon boundaries" — each with a concrete mechanism, not a policy statement. |
| F-7 | "F: high" or "R: high" or "R: certified" (bare label without criterion) | F-G-R label without criterion (violates FPF E-5 declaration discipline) | `R: high` must be accompanied by `R.refuted_if: [observable]` and `R.accepted_if: [observable]`. Label alone is not a triple. |
| F-8 | "this architecture passes the universality test" (bare) | Universality claim without test evidence | "Passes D-test: grep `base/` → 0 hits confirmed [date]. Passes C-test: [third use case name] can instantiate without base/ modification [confirmed / TBD by [date]]." |
| F-9 | "antifragile" (bare, without mechanism) | Bare antifragility claim | "Antifragile via [named mechanism]: [specific component] gets stronger when [specific stress] because [causal chain]. Falsified if that component degrades (not merely survives) under [named stress at named scale gate]." |
| F-10 | "no re-architecture required" / "no fundamental refactor" (bare) | Non-falsifiable scalability claim (violates D19 trajectory requirement for concrete gate-by-gate failure modes) | "No re-architecture at [gate G], defined as: no change to [specific schema / protocol / edge-type enum]. Refuted if [named component] requires structural change at [gate G] as shown by [measurement]." |

**For scalability-mode cells specifically:** every horizon-gate projection (€50K / €200K / €1M / $100M / $1T) MUST name (a) what physically breaks, (b) the named BOSC-A-T-X trigger, (c) the MHT event. The phrase "scales fine to $1T" is per se disqualifying (execution prompt §1.2 anti-pattern 6).

---

## §6 Universality Criterion check (B/C/D per JETIX-PHILOSOPHY §10)

**Source.** JETIX-PHILOSOPHY §10 (Section 10, "Universality Criterion"):
"B: ≥90% design choices configurable. C: base works for Jetix-company +
astronomer + animal-husbandry. D: symbolic grep → 0 hits on base/."
JETIX-ARCHITECTURE-BRIEF §5.5 (portability tests).

### Test B — Configurability (≥90% design choices configurable)

**Verdict: CONDITIONAL PASS with UC-9/UC-10 risks.**

The existing wiki v3 base architecture (9 entity types, 12 edge types, 5
alphas, Q1 4-tier retrieval) is substantially configurable by design.
The risk introduced by UC-9 and UC-10 is that:

- Client-isolation mechanics (filesystem root, permission scope, per-client
  agent-key) could be hardcoded to a Jetix-specific path structure if
  variants do not explicitly parameterise `CLIENT_ID` and `WIKI_ROOT`.
- Local-LLM selection (which model family, which quantization) could be
  hardcoded to a specific model checkpoint if variants name "Llama 3.1 8B Q4"
  as the only path rather than a configurable `LOCAL_LLM_FAMILY` parameter.

B-test passes when: every UC-9 isolation mechanism is expressed via a
configurable `{client_id, wiki_root, permission_scope}` triple, and every
UC-10 inference path is expressed via a configurable `{local_llm_family,
quantization_level, hardware_profile}` triple — none hardcoded in base/.

F-G-R on this verdict:
```
F: F3  # grounded in §10 text + §5.5 text; not yet empirically tested
ClaimScope:
  holds_when: "UC-9 and UC-10 mechanics are implemented via config params not hardcodes"
  not_valid_when: "a variant implementation hardcodes a specific client path or model name in base/"
R:
  refuted_if: "symbolic grep on base/ returns hits for specific client names or model checkpoint names after variant materialization"
  accepted_if: "grep clean after materialization; C-test also passes"
```

### Test C — Multi-use-case (Jetix + astronomer + animal-husbandry)

**Verdict: NOT YET TESTED; risk of failure if client-isolation vocabulary
is Mittelstand-specific.**

The UC-9 acceptance criteria use explicitly DACH Mittelstand examples
("DACH Mittelstand manufacturing", "GDPR / EU AI Act"). If the client-isolation
vocabulary (permission scope names, audit-trail labels, compliance-calendar
fields) bakes in "GDPR" or "EU AI Act" as hardcoded field names in base/,
the astronomer use case cannot instantiate UC-9 without modifying base/.

C-test passes when: the client-isolation and offline-inference mechanics are
expressed using domain-neutral vocabulary in base/ (e.g., `data_sovereignty_scope`,
`regulatory_framework: configurable`, `inference_privacy_level: local|hybrid|cloud`)
and Jetix/DACH-specific values are overlay-only.

F-G-R:
```
F: F2  # inferred risk; not yet tested
ClaimScope:
  holds_when: "client-isolation is domain-neutral config; regulatory labels are overlay"
  not_valid_when: "GDPR / EU AI Act are hardcoded field names in base/ client-isolation spec"
R:
  refuted_if: "astronomer instantiation requires modification of base/ to implement UC-9"
  accepted_if: "astronomer instantiation passes UC-9 proof section without touching base/"
```

### Test D — Symbolic grep (0 hits in base/ for Jetix|DACH|AI consulting|Mittelstand)

**Verdict: RISK FLAGGED; not yet run but must be run at materialization.**

The current execution prompt (§1.2 item 7, local-first mandate) references
"DACH Mittelstand manufacturing" and "Mittelstand AI Alliance" in the UC-9
and UC-10 sections. If a variant author copies this language into base/
config files, the D-test fails.

D-test passes when: a pre-commit Hook equivalent (analogous to the Hook 1
asymmetric-reference ban) fires on any commit to base/ that introduces
the flagged strings. This hook should be declared as part of the UC-9
architectural proof section in every variant (it is a concrete enforcement
mechanism, not a policy).

F-G-R:
```
F: F2  # risk-level claim; symbolic test not yet run
ClaimScope: "applies to base/ subtree only; overlay/ is unconstrained"
R:
  refuted_if: "grep base/ -r 'Jetix|DACH|AI consulting|Mittelstand' → ≥1 hit after variant materialization"
  accepted_if: "grep returns 0 hits; Hook equivalent prevents future leakage"
```

### Summary verdict — Universality Criterion

The proposed local-first / client-private architecture passes B/C/D
**conditionally**: it is architecturally feasible to maintain universality
while implementing UC-9 and UC-10, but only if variants explicitly
parameterise client-isolation and inference-path mechanics, and avoid baking
DACH/Mittelstand/EU-specific vocabulary into base/. The condition is not
automatically satisfied by the BIOS-strategic framing; it requires explicit
engineering discipline in how the variant authors write their config
specifications.

This is a defensible position — the BIOS analogy itself supports it:
IBM's BIOS specification was domain-neutral (any PC could implement it);
the DACH-specific compliance and Mittelstand-specific terminology were
application-layer (Phoenix BIOS for specific vendors). The parallel instructs
that Jetix's `base/` must be the specification layer, not the instantiation.

---

## §7 Provenance

| Source | Section | Load-bearing quote |
|---|---|---|
| decisions/JETIX-PHILOSOPHY.md | §6 Quality Fundamentals | "Если approach sucks в одном месте — будет suck везде" (fractal quality; falsifiability is non-optional at all scales) |
| decisions/JETIX-PHILOSOPHY.md | §10 Universality Criterion | "B: ≥90% design choices configurable. C: base works for Jetix + astronomer + animal-husbandry without modification. D: grep → 0 hits." |
| decisions/JETIX-PHILOSOPHY.md | §14 Foundation as Main Asset | "Потеряем wiki — потеряем Jetix." (Foundation-first; supersession chain integrity is a Foundation element) |
| decisions/JETIX-ARCHITECTURE-BRIEF.md | §4.6 Continuous quality metrics | "F-G-R frontmatter (formality F0-F9 / scope / reliability R-low|medium|high|certified|formally-proven)" — F-G-R is mandatory per-agent |
| decisions/JETIX-ARCHITECTURE-BRIEF.md | §4 Foundation Layer | "Foundation = главный актив (D2 §14, OME L6). 8 elements: wiki+ATOM-REGISTRY / agent contracts / handoff protocols / escalation / continuous quality / dashboard / reserve routes / F-G-R tagging." |
| decisions/JETIX-ARCHITECTURE-BRIEF.md | §6 Hard Constraints | "Any variant violating any of these is disqualified without review of the rest." (Locks = Lakatos hard core) |
| decisions/JETIX-ARCHITECTURE-BRIEF.md | §5.5 Portability | "Symbolic test applies to base/ repo subtree (source code / config), NOT to brief docs or overlay code." |
| decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md | E-3 (§2.3) | "Critic rubric: AP must be Hamel-binary, not prose. Alternatives enumerated ≥2 + status quo with kill-conditions. Anti-scope stated." |
| decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md | E-5 (§2.5) | "Integrator output schema adds three frontmatter fields per claim: F: formality level, ClaimScope:, R: reliability (pathwise). Dissent-record typing: each dissenting claim tagged with (F, ClaimScope, R)." |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §3 | "Methodology push, data no pull. Client's KB never sends content back to Jetix-central." |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §6 | "Missing для client-facing production: Client-isolation mechanics — how exactly we spawn per-client wiki/agents without cross-contamination." |
| prompts/km-architecture-research-2026-04-24.md | §1.4 depth measure #2 | "≥8 Tier-1 citations per variant, each citing path + section. Bare assertions without source are disqualified. Each major claim carries F-G-R." |
| prompts/km-architecture-research-2026-04-24.md | §1.4 depth measure #5 | "Explicit preserved dissents, minimum three. Do NOT average dissenting conclusions. When two experts disagree, both positions land in the final with F-G-R tagging." |
| prompts/km-architecture-research-2026-04-24.md | §3.7 UC-7 | "Resolution options: edit claim (state: revised), supersede (new page with `supersedes` edge), tombstone (state: tombstoned), or preserve both as conditional claims with bounded ClaimScope (per FPF E-5 F-G-R discipline)." |
| prompts/km-architecture-research-2026-04-24.md | §3.9 UC-9 | "Architecture must make [cross-client data access] impossible by construction — not by policy, not by careful admin, not by 'trusted Jetix employees' — by the physical / directory / cryptographic structure of the variant." |
| .claude/agents/philosophy-expert.md | §3.1 Conformance Checklist | "Falsifier-named (Popper): for every assertion in the artefact body, the artefact states what observation would refute it." |
| .claude/agents/philosophy-expert.md | §2.4 (P3 Lakatos) | "A research programme has a hard core + protective belt; refutations hit the belt first, then the core." |

---

*End of philosophy × critic epistemic hygiene audit. Draft status: authored
by philosophy-expert, mode: critic. Awaiting brigadier integration into cycle
cyc-km-architecture-2026-04-24.*
