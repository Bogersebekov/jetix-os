---
title: Philosophy × Optimizer — F-G-R Discipline + DRR Template + Supersession Invariants
type: optimization
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
confidence_method: expert-judgment-from-critic-draft-and-tier1
tier: tier-1
produced_by: philosophy-optimizer
sources:
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-critic-epistemic-audit.md
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md
  - decisions/JETIX-ARCHITECTURE-BRIEF.md
  - .claude/agents/philosophy-expert.md
  - prompts/km-architecture-research-2026-04-24.md
related:
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-critic-epistemic-audit.md
binding_scope: km-architecture-philosophy-optimizer-deltas
mode: optimizer
---

# Philosophy × Optimizer — F-G-R Discipline + DRR Template + Supersession Invariants

**Artefact lineage.** This optimizer pass receives the 4-NO + 1-CONDITIONAL
verdict from the philosophy × critic epistemic audit (H-1 through H-5) and
proposes minimal-LOC deltas to close each gap. Scope is strictly epistemic:
schema field additions, lint-check declarations, and template format — not
variant mechanics (anti-scope §6).

**Optimizer predicate (§4.0 of philosophy-expert.md).** "Does the proposed
first-principles-reset preserve all 5 invariants (WLNK / MONO / IDEM / COMM /
LOC) AND deliver a measurable baseline → reset delta on at least one of
{axioms-named, claims-rooted-in-source, paradigm-explicit}?"

---

## §1 Delta proposals

Each delta closes one H-N failure from the critic. Baseline is the current
wiki v3 spec state (ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23, Gate 1 + Gate 2
APPROVED, not modified here). Proposed state adds fields or lint checks.
Method-change check precedes every delta: none below changes the governing
epistemic method (Popper-falsifiability framing throughout); all are
parameter-level additions within the existing F-G-R framework.

---

### Delta-1 — Close H-1: `R.refuted_if` required on type=claim

**Failure from critic.** H-1 NO: the F-G-R triple framework (JETIX-ARCHITECTURE-BRIEF
§4.6 + FPF E-5) does not mandate a populated `R.refuted_if` field. Labels
(`R: high`) ship without named observables. AP-PHIL-1 (claim-without-falsifiability)
fires when a UC-support or scale-survival claim carries a bare `R:` label.
[src: philosophy-critic §1 H-1, §2 H-1]

**Method-change check.** This delta adds a required subfield to an existing
schema field. It does NOT switch from Popper-falsifiability to a different
epistemic framework. Not a method-change. Proceed.

**Before / after table.**

| Field | Baseline | Proposed | Delta |
|---|---|---|---|
| claim schema fields (type=claim) | `F:`, `ClaimScope:`, `R:` (label only) | `F:`, `ClaimScope:`, `R:` (label), `R.refuted_if:` (required, non-empty string), `R.accepted_if:` (recommended, non-empty string) | +2 subfields on every type=claim |
| `/lint` signal for bare `R:` | absent | Signal L-FALSY-R: fires when type=claim AND `R.refuted_if` is null or empty | +1 lint signal |
| Accepted claim count | Uncounted (bare labels pass) | Claims passing only when `R.refuted_if` non-empty | Measurable: 0 bare-R claims post-delta |
| AP-PHIL-1 exposure | Chronic: any "supports UC-N" claim may be bare | Closed: structural prevention, not reviewer detection | -N false-negatives |

**Invariant check.**

- WLNK: the epistemic dependency chain is preserved — `R.refuted_if` cites the
  observable within the same claim node; provenance is not broken.
- MONO: the simplified-but-true direction holds — adding a required field tightens
  the schema monotonically (no claims that previously passed can regress).
- IDEM: re-running the lint on an already-compliant claim returns the same result.
- COMM: field order in YAML frontmatter does not affect lint outcome.
- LOC: the delta stays epistemic — it names what observation refutes a claim, not
  what action to take. No instrumental bleed.

All 5: PASS.

**Example (operative, not illustrative).**

```yaml
# type=claim — after Delta-1
F: F4
ClaimScope:
  holds_when: "wiki graph ≤50,000 nodes; single-tenant deployment"
  not_valid_when: "multi-tenant federated deployment with >3 client graphs"
R: medium
R.refuted_if: "ANY query latency at G2 (€200K gate) > 5s p95 over rolling 100 queries"
R.accepted_if: "p95 latency ≤ 2s over rolling 100 queries for 30 consecutive days"
```

Provenance: FPF E-5 [src: decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md §2.5]:
"Integrator output schema adds three frontmatter fields per claim ... R: reliability
(pathwise, not point estimate)." Delta-1 sharpens "pathwise" to mean: a named
observable that constitutes a refutation event, not merely a qualitative label.

**F-G-R on Delta-1.**

```yaml
F: F5  # grounded in critic draft + FPF E-5 + JETIX-ARCHITECTURE-BRIEF §4.6
ClaimScope:
  holds_when: "type=claim entities in wiki v3 (9 entity types; swarm/wiki/)"
  not_valid_when: "type != claim; prose-only artefacts without claim nodes"
R: medium
R.refuted_if: "≥1 type=claim in a gate-passed variant lacks R.refuted_if after delta materialization"
R.accepted_if: "zero bare-R claims in all 6 variant drafts at brigadier gate-check"
```

---

### Delta-2 — Close H-2: Cross-client supersession FORBIDDEN — `/lint` check

**Failure from critic.** H-2 NO: the supersession chain (D3 §3.2 `supersedes`
edge + α-2 artefact state machine) does not specify edge-type policy across the
Jetix-central / client-local boundary. Two simultaneous Jetix clients could
theoretically emit a `supersedes` edge pointing at each other's KB nodes.
[src: philosophy-critic §1 H-2, §2 H-2, §3 H-2 Alternative A verdict]

**Method-change check.** This delta adds a lint signal enforcing a topological
constraint on `graph/edges.jsonl`. It does not change the edge-type vocabulary
or the supersession semantics — it adds a directionality rule. Not a
method-change. Proceed.

**Before / after table.**

| Field | Baseline | Proposed | Delta |
|---|---|---|---|
| Cross-client `supersedes` edge policy | Implicit (not specified in schema) | FORBIDDEN: any `supersedes` edge where `source.client_id ≠ target.client_id` is a lint violation | +1 policy declaration in schema |
| `/lint` signal | absent | Signal L-XSUP-CROSS: fires when `edges.jsonl` contains a `supersedes` edge with mismatched client-scopes | +1 lint signal |
| Methodology-push edges (Jetix-central → client-local) | Implicit (no edge-type exists) | Permitted narrow exception: edge-type `methodology-update-supersedes` FROM `scope:jetix-central` TO `scope:client-*` only; reverse direction triggers L-XSUP-CROSS | +1 permitted exception + asymmetry rule |

**Supersession-chain invariant (operative rule for `/lint`).**

```
SUPERSESSION-CHAIN INVARIANT SC-1 (cross-client):
  IF edge.type == "supersedes"
  AND edge.source.client_scope != edge.target.client_scope
  AND edge.type != "methodology-update-supersedes"
  THEN VIOLATION: isolation-breach
  ACTION: lint returns L-XSUP-CROSS; variant fails H-2
```

Provenance: philosophy-critic §2 H-2 Alternative A: "each client's graph is a
closed holon — no inter-graph edge types involving two different clients."
STRATEGIC-INSIGHT §3 [src: decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md]:
"Methodology push, data no pull."

**Invariant check.**

- WLNK: provenance chains within each client's graph remain intact; the lint
  only blocks cross-client edges, not intra-client ones.
- MONO: closed-holon policy is monotonically restrictive; no previously-passing
  edge type is permissioned away beyond the specified violation class.
- IDEM: re-running L-XSUP-CROSS on a compliant `edges.jsonl` returns no violations.
- COMM: lint evaluation order across edges does not affect outcome.
- LOC: purely structural constraint on graph topology; no instrumental claim.

All 5: PASS.

**F-G-R on Delta-2.**

```yaml
F: F5
ClaimScope:
  holds_when: "UC-9 client-isolation deployment; per-client graph/edges.jsonl"
  not_valid_when: "single-tenant Jetix-only deployment with no client KBs"
R: medium
R.refuted_if: "L-XSUP-CROSS fires zero times in 50 lint runs on a corpus seeded with
               known cross-client supersedes edges"
R.accepted_if: "L-XSUP-CROSS catches 100% of seeded cross-client edges in validation run"
```

---

### Delta-3 — Close H-3: Lakatos hardcore lint check

**Failure from critic.** H-3 NO: the 24 Locks (Lakatos hard core) have no
machine-checkable enforcement at variant-intake time. A variant section could
propose changing Lock D17 (Filesystem = SoT) under "variant design" framing
without triggering a pre-flight block. [src: philosophy-critic §1 H-3, §2 H-3,
§3 H-3 Alternative B verdict]

**Method-change check.** This delta specifies a pre-flight scan and a mandatory
lock-compliance section in the variant template. It does not re-open, revise,
or re-prioritize any of the 24 Locks. The Locks are the hard core; the scan is
the protective belt. Not a method-change. Proceed.

**Before / after table.**

| Field | Baseline | Proposed | Delta |
|---|---|---|---|
| Lock violation detection | Verbal reminder in execution prompt §1.2 item 6 | Named lint check L-LOCK-VIO: scans variant text for keywords from 24-Lock keyword table (D17, Q2, D13, etc.) + flags structural changes to locked behaviours | +1 lint signal |
| Variant template | No mandatory Lock-compliance section | Mandatory `§ Lock compliance` section: enumerated 24-Lock rows with pass/fail/na per lock, pre-submission | +1 required template section |
| Lakatos hardcore preservation rule | Implicit | Explicit: "a 24-Lock cannot be superseded by a `swarm/wiki/global/compound-rules/` rule; only by Ruslan's HITL ack (AWAITING-APPROVAL packet)" | +1 supersession-chain invariant SC-2 |

**Supersession-chain invariant SC-2 (Lakatos hardcore).**

```
SUPERSESSION-CHAIN INVARIANT SC-2 (hardcore preservation):
  IF edge.type == "supersedes"
  AND edge.target.entity_type == "foundation"
  AND edge.target.binding_class == "24-lock"
  AND edge.source.produced_by != "HITL-ruslan-ack"
  THEN VIOLATION: hardcore-breach
  ACTION: lint returns L-LOCK-VIO; immediately escalate to HITL;
          variant dispatch blocked until ack received
```

Provenance: JETIX-ARCHITECTURE-BRIEF §6 [src: decisions/JETIX-ARCHITECTURE-BRIEF.md]:
"Any variant violating any of these [24 Locks] is disqualified without review of
the rest." Philosophy-expert §2.4 (P3 Lakatos): "refutations hit the belt first,
then the core — the 24 Locks ARE the hard core."

**Invariant check.**

- WLNK: provenance chain to each Lock's source document is preserved; the lint
  scan cites the Lock ID and source doc in its violation report.
- MONO: the scan is monotonically additive — it adds a gate that was absent;
  it does not remove any existing check.
- IDEM: scanning a Lock-compliant variant twice returns zero violations both times.
- COMM: keyword scan order across 24 Locks does not affect violation detection.
- LOC: the check is epistemic (does this claim contradict a locked foundation?)
  not instrumental (should we keep this Lock?).

All 5: PASS.

**F-G-R on Delta-3.**

```yaml
F: F5
ClaimScope:
  holds_when: "variant drafts submitted to brigadier intake; Phase A + Phase B"
  not_valid_when: "HITL-authored revision packets (those are the only legitimate
                   hardcore supersession path)"
R: medium
R.refuted_if: "A variant containing a structural D17 revision passes brigadier
               gate-check without L-LOCK-VIO firing"
R.accepted_if: "L-LOCK-VIO catches 100% of seeded Lock-violation sections in
                validation run across 6 variant drafts"
```

---

### Delta-4 — Close H-4: Federated contradiction-detection scope boundary

**Failure from critic.** H-4 NO: UC-7 (contradiction detection, `/lint` Q5 signal
#4, `contradicts` edge) has no explicit boundary preventing a federated multi-client
`/lint` sweep from reading Client-A's and Client-B's KBs simultaneously, which
would violate UC-9 isolation. [src: philosophy-critic §1 H-4, §2 H-4, §3 H-4
Alternative A verdict]

**Method-change check.** This delta specifies a per-client lint instantiation
rule. It does not change the contradiction-detection algorithm or the `contradicts`
edge semantics — it adds a scope constraint. Not a method-change. Proceed.

**Before / after table.**

| Field | Baseline | Proposed | Delta |
|---|---|---|---|
| `/lint` process scope | Unspecified; potentially global | Explicit: `/lint` is instantiated per-client with filesystem-scope limited to that client's wiki root; Jetix-central `/lint` covers only the Jetix-methodology repo | +1 scope-declaration rule |
| Cross-client contradiction detection | Potentially possible (not blocked) | By-construction impossible: each lint process has no filesystem read-path to another client's wiki root | +1 architectural constraint |
| Inter-client contradiction surface | None | Manual path only: Ruslan flags cross-client patterns as anonymized methodology updates, which propagate via methodology-push | +1 human-in-loop preservation |
| `/lint` signal for scope violation | absent | Signal L-LINT-SCOPE: fires if `/lint` process attempts to read a path outside its declared `wiki_root` | +1 lint signal |

**Supersession-chain invariant SC-3 (federated lint scope).**

```
SUPERSESSION-CHAIN INVARIANT SC-3 (lint isolation):
  IF lint.process.filesystem_scope CONTAINS path NOT under lint.client.wiki_root
  THEN VIOLATION: lint-scope-breach
  ACTION: lint returns L-LINT-SCOPE; terminate process; log attempt
```

Provenance: philosophy-critic §2 H-4: "every variant that claims UC-7 capability
in a multi-client federated deployment must show that `/lint` operates per-client
on an isolated filesystem tree." Prompts §3.9 UC-9 [src: prompts/km-architecture-research-2026-04-24.md]:
"architecture must make [cross-client data access] impossible by construction."

**Invariant check.**

- WLNK: each client's contradiction graph retains its provenance; the scope
  constraint does not break intra-client edges.
- MONO: the constraint is monotonically restrictive on cross-client reads.
- IDEM: scoping check on a correctly-bounded lint process returns PASS on re-run.
- COMM: evaluation order of filesystem-path checks is order-independent.
- LOC: purely structural (filesystem scope) — no instrumental claim about
  which contradictions to resolve.

All 5: PASS.

**F-G-R on Delta-4.**

```yaml
F: F4
ClaimScope:
  holds_when: "federated multi-client deployment; UC-9 enforcement active"
  not_valid_when: "single-tenant Jetix-only deployment"
R: medium
R.refuted_if: "A variant's /lint process reads Client-B's filesystem root
               while instantiated for Client-A in a pen-test scenario"
R.accepted_if: "L-LINT-SCOPE fires on 100% of out-of-scope filesystem access
                attempts in validation run"
```

---

### Delta-5 — Close H-5: Universality test on F4+ claims (conditional)

**Failure from critic.** H-5 CONDITIONAL: the universality test (JETIX-PHILOSOPHY
§10 B/C/D) passes only if UC-9 and UC-10 mechanics are expressed via configurable
parameters, not hardcoded DACH/Mittelstand vocabulary in `base/`. The condition
is not yet verifiable until variant materialization. [src: philosophy-critic §1 H-5,
§6 Tests B/C/D]

**Method-change check.** This delta adds a universality-gate lint check and a
pre-commit hook equivalent. It does not change the universality criterion itself
(JETIX-PHILOSOPHY §10 B/C/D). Not a method-change. Proceed.

**Before / after table.**

| Field | Baseline | Proposed | Delta |
|---|---|---|---|
| Universality test timing | Post-materialization (not enforced during variant drafting) | Pre-commit hook equivalent declared in variant's UC-9 proof section; lint signal L-UNIV-GREP fires on any commit to `base/` introducing flagged strings | +1 pre-commit signal |
| F4+ claim universality requirement | Absent | Every claim with F≥4 that makes an architecture-scope assertion MUST pass §10 B/C/D before brigadier promotes it from `drafted` to `accepted` | +1 promotion gate |
| `base/` symbolic test | Informal (mentioned in JETIX-ARCHITECTURE-BRIEF §5.5) | Formalized as lint signal L-UNIV-GREP: `grep base/ -r 'Jetix|DACH|AI consulting|Mittelstand'` → must return 0 hits | +1 named lint signal |
| C-test (astronomer use case) | Unstated requirement | Explicit: "Third hypothetical use case (not Jetix, not DACH) can instantiate UC-9 and UC-10 without modifying base/" stated as acceptance condition in each variant's universality section | +1 acceptance condition |

**Supersession-chain invariant SC-4 (universality enforcement on F4+ claims).**

```
SUPERSESSION-CHAIN INVARIANT SC-4 (universality gate):
  IF claim.F >= 4
  AND claim.scope CONTAINS "architecture" OR "base/"
  AND claim.state == "accepted"
  AND (B-test OR C-test OR D-test) == FAIL
  THEN VIOLATION: universality-breach
  ACTION: lint returns L-UNIV-GREP; claim state reverts to "drafted";
          brigadier cannot promote until tests pass or claim F demoted to ≤3
```

Provenance: JETIX-PHILOSOPHY §10 [src: decisions/JETIX-ARCHITECTURE-BRIEF.md §1]:
"No Jetix-specific content in base (universality B/C/D tests; D2 §10)."
Philosophy-critic §6 D-test: "grep base/ -r 'Jetix|DACH|AI consulting|Mittelstand'
→ 0 hits."

**Invariant check.**

- WLNK: every promoted F4+ claim retains its provenance citation; the universality
  gate adds a condition to promotion, not a source erasure.
- MONO: the gate is monotonically restrictive on F4+ claims; it does not demote
  claims that already pass the test.
- IDEM: running L-UNIV-GREP twice on a clean `base/` returns 0 hits both times.
- COMM: grep evaluation order across files does not affect the hit count.
- LOC: the test is epistemic (does this architecture claim survive universality
  scrutiny?) not instrumental (should we pursue universal design?).

All 5: PASS.

**F-G-R on Delta-5.**

```yaml
F: F4
ClaimScope:
  holds_when: "F4+ architecture-scope claims in base/ subtree"
  not_valid_when: "overlay/ subtree; F<4 claims; non-architecture claims"
R: medium
R.refuted_if: "A variant with a known DACH hardcode in base/ passes the universality
               gate without L-UNIV-GREP firing"
R.accepted_if: "L-UNIV-GREP returns 0 hits on base/ after variant materialization;
                astronomer C-test passes without base/ modification"
```

---

## §2 4-part DRR canonical template (FPF E-9)

**Authority.** FPF Enhancement E-9 [src: decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md §2.9]:
"Strategies.md entry format standardized to 4-part DRR: {context, decision,
alternatives, review-checkpoint}." This optimizer canonicalizes the exact format
that integrators must embed at `decisions/<slug>.md` entry points AND in each
variant draft's decision-record sections.

**Note on translation.** E-9 uses `{context, decision, alternatives, review-checkpoint}`.
This swarm operationalises them as `{Context, Decision, Alternatives considered,
Review-checkpoint}` — `Context` captures the why (FPF's `context`); `Alternatives
considered` makes the why-not explicit (FPF's `alternatives`). The translation
is deliberate and consistent per brigadier §8.3 documented-translation note.

**Canonical template (required format).**

```markdown
### <YYYY-MM-DD> — <one-line subject>

- **Context:** <Why this decision arose; what problem it solves; what prior state
  it supersedes or extends; what triggered the need now rather than later.
  Cite task_id + cycle_id + upstream artefact path. Minimum 80 words. Do not
  summarize — give the reader enough context to understand without reading the
  upstream artefact.>

- **Decision:** <What was decided, in one operative sentence, followed by the
  full specification: which schema fields change, which lint signals are added,
  which rules are declared. State the decision as a past-participle action
  ("decided to add", "declared that"). Minimum 80 words. Include the Hamel-binary
  acceptance predicate: what observable confirms the decision has been correctly
  implemented.>

- **Alternatives considered:** <At minimum two alternatives plus status quo.
  For each: (a) brief description of the alternative, (b) kill-condition — the
  exact reason this alternative was not chosen. Status quo kill-condition is
  mandatory: what bad outcome the status quo produces that made the decision
  necessary. Minimum 80 words total. Format each alternative as a sub-bullet.>

- **Review-checkpoint:** <Was the decision validated, refuted, or partially
  confirmed? Cite the next-cycle confirmation event (artefact path + date).
  If not yet reviewed: state "pending — review at cycle <N> when <observable>
  is measurable." If refuted: state the refutation evidence and tombstone the
  decision. If validated: state the ✓/✗ ratio and promote to strategies.md
  validated status. Minimum 80 words.>

#### Evolution
- changelog:
  - <YYYY-MM-DD> — created
  - <YYYY-MM-DD> — <amendment if any>
- last-review: <YYYY-MM-DD>
- expected-evolution:
  - cycle_10: <drift expectation>
  - cycle_50: <drift expectation>
  - cycle_200: <drift expectation>
```

**Placement rules.** (a) Every `decisions/<slug>.md` that results from a
brigadier-mediated gate carries a DRR block for each decision it embodies. (b)
Every variant draft (`swarm/wiki/drafts/`) carries a DRR block in its final
section for its primary design decision. (c) The `agents/philosophy-expert/strategies.md`
file uses this exact format for every entry. (d) Word-count floor of 80 words
per part is a hard floor enforced at brigadier gate-check (not a target).

**F-G-R on the DRR template itself.**

```yaml
F: F5  # grounded in FPF E-9 + brigadier §8.3 documented-translation note
ClaimScope:
  holds_when: "all decisions/*.md + variant drafts in swarm/wiki/drafts/ + strategies.md entries"
  not_valid_when: "inline prose decisions in agent body text (those are design commentary, not DRR entries)"
R: medium
R.refuted_if: "brigadier gate-check passes a DRR entry with <80 words in any of the
               4 parts OR missing alternatives OR missing review-checkpoint"
R.accepted_if: "all 6 variant drafts carry compliant DRR blocks at brigadier gate-check"
```

---

## §3 Falsifiability flag list (operative — 10 forbidden phrases + lint regex)

These are the 10 forbidden phrases from philosopher-critic §5 [src: philosophy-critic
§5], restated as operative lint patterns. Each phrase, if detected in a variant
draft WITHOUT an accompanying `R.refuted_if` field on the same claim node,
constitutes AP-PHIL-1 (claim-without-falsifiability) and triggers lint signal
L-FALSY-R.

**Lint signal: L-FALSY-PHRASE.** Fires when body text matches the regex in column
3 and the enclosing claim node has no `R.refuted_if` field (or `R.refuted_if`
is empty). The signal does not fire if `R.refuted_if` is populated — the phrase
is then permissible as prose shorthand anchored by a falsifier.

| # | Forbidden phrase | Lint regex | AP triggered | Required replacement |
|---|---|---|---|---|
| F-1 | "trivially scales" / "scales naturally" / "scales without issue" | `scales (trivially\|naturally\|without issue)` | AP-PHIL-1 | Name gate + physical threshold + metric |
| F-2 | "obviously preserves the moat" / "moat is preserved" | `(obviously )?preserves the moat\|moat is preserved` | AP-PHIL-1 | Name competitor-observable that would falsify |
| F-3 | "naturally federates" / "federation is straightforward" | `(naturally federates\|federation is straightforward)` | AP-PHIL-1 | Name conditions X where federation holds; Y where it fails |
| F-4 | "supports UC-N" (bare, without trace) | `supports UC-[0-9]+(?!.*input →)` | AP-25 | Full UC-N trace: input → wiki paths → agent → write-back → citation |
| F-5 | "works offline" / "offline-first" (bare) | `(works offline\|offline-first)(?!.*refuted)` | AP-PHIL-1 | Name query type + zero-network proof + falsification condition |
| F-6 | "client data is isolated" (bare, without construction proof) | `client data is isolated(?!.*proof)` | AP-PHIL-1 | Name construction mechanism (filesystem / cryptographic / holon) |
| F-7 | "F: high" or "R: high" or "R: certified" (bare, no criterion) | `^R:\s*(high\|certified\|formally-proven)$` | FPF E-5 | Add `R.refuted_if:` and `R.accepted_if:` on adjacent lines |
| F-8 | "passes the universality test" (bare) | `passes the universality test(?!.*grep)` | AP-PHIL-1 | Cite D-test grep result + C-test third-use-case confirmation |
| F-9 | "antifragile" (bare, without mechanism) | `antifragile(?!.*mechanism\|.*because\|.*via)` | AP-PHIL-1 | Name mechanism + specific component + specific stress + causal chain |
| F-10 | "no re-architecture required" / "no fundamental refactor" (bare) | `no (re-architecture\|fundamental refactor) (required\|needed)(?!.*gate)` | AP-PHIL-1 | Name gate + specific invariant preserved + measurement |

**Implementation note.** Lint signals L-FALSY-R (Delta-1) and L-FALSY-PHRASE
(this section) are complementary: L-FALSY-R fires on schema-level absence of
`R.refuted_if`; L-FALSY-PHRASE fires on body-text patterns that signal non-falsifiable
claims even when the schema field is present but the body contradicts it. Both
must fire to constitute full AP-PHIL-1 prevention.

---

## §4 Refusals (method-change escalations)

No method-change escalations were triggered in this optimizer pass. All five
deltas are parameter-level additions within the existing F-G-R / Popper-falsifiability
framework. Confirmation: no delta proposes to switch governing epistemic method
(e.g., Popper → Bayesian, or falsifiability → coherentism). Per §4.3 of
philosophy-expert.md, method-change refusal would read:

```json
{
  "status": "refusal",
  "reason": "method-change request — switching epistemic framework is a Method-level
             decision (E-4 hard refusal). Route to integrator-mode OR escalate HITL.",
  "escalation": "integrator OR HITL",
  "alternative_routing": "philosophy × integrator",
  "artefact_path": null,
  "turns_used": 1,
  "verifier_result": null
}
```

No such refusal is needed here. Documented for completeness.

---

## §5 Coverage matrix

| H-N failure | Closed by | Lint signal | Template change | Supersession invariant |
|---|---|---|---|---|
| H-1 (R.refuted_if absent) | Delta-1 | L-FALSY-R | `R.refuted_if:` required on type=claim | — |
| H-2 (cross-client supersedes) | Delta-2 | L-XSUP-CROSS | UC-9 proof section must declare edge policy | SC-1 |
| H-3 (Lakatos hardcore unprotected) | Delta-3 | L-LOCK-VIO | Mandatory `§ Lock compliance` in variant template | SC-2 |
| H-4 (federated lint leaks) | Delta-4 | L-LINT-SCOPE | UC-7 section must declare per-client lint scope | SC-3 |
| H-5 (universality conditional) | Delta-5 | L-UNIV-GREP | UC-9/UC-10 sections must pass B/C/D before F4+ promotion | SC-4 |
| Forbidden phrases (§3) | §3 operative list | L-FALSY-PHRASE | Phrase-body match triggers without `R.refuted_if` | — |
| DRR format (all decisions) | §2 template | — | 4-part DRR 80w/part floor at all decision entry points | — |

Total: 5 lint signals declared (L-FALSY-R, L-XSUP-CROSS, L-LOCK-VIO, L-LINT-SCOPE,
L-UNIV-GREP) + 1 supplementary (L-FALSY-PHRASE) + 4 supersession-chain invariants
(SC-1..SC-4).

---

## §6 Anti-scope

This optimizer is explicitly NOT doing the following:

- **NOT evaluating variant mechanics.** No variant text exists yet. The deltas
  above operate on the epistemic substrate — schemas, lint signals, and templates
  — not on variant-specific design choices (which retrieval tier, which local
  LLM family, which graph traversal algorithm).

- **NOT arbitrating instrumental Рациональность.** The question of which variant
  to pursue is investor-expert territory (FPF L1003-1006). This optimizer
  audits only whether the epistemic substrate each variant sits on is
  falsifiable.

- **NOT producing the variant drafts.** That is the work-phase cells' responsibility.
  This optimizer produces the acceptance predicates and the lint-signal declarations;
  variant authors must satisfy those predicates.

- **NOT re-opening the 24 Locks.** Delta-3 adds a check that enforces the Locks;
  it does not adjudicate whether any Lock should change. Lock revision requires
  Ruslan's HITL ack (JETIX-ARCHITECTURE-BRIEF §6 binding).

- **NOT proposing paid APIs or infrastructure changes.** All deltas are schema
  declarations and lint patterns — implementable as filesystem reads and regex
  matches. No external service is required (Max-subscription discipline).

- **NOT assessing engineering implementation.** How exactly `/lint` is implemented
  (shell script, Python, Makefile target) is engineering-expert territory. This
  optimizer declares the check semantics only.

---

## §7 F-G-R summary per delta

| Delta | F | ClaimScope (compressed) | R | R.refuted_if |
|---|---|---|---|---|
| Δ1 — R.refuted_if required | F5 | type=claim entities in wiki v3 | medium | ≥1 bare-R claim passes gate post-delta |
| Δ2 — cross-client FORBIDDEN | F5 | UC-9 multi-client deployment | medium | L-XSUP-CROSS misses seeded cross-client edge |
| Δ3 — Lakatos hardcore lint | F5 | variant drafts at brigadier intake | medium | Lock-violation variant passes gate without signal |
| Δ4 — federated lint scope | F4 | UC-9 active; multi-client | medium | /lint reads out-of-scope client path undetected |
| Δ5 — universality gate F4+ | F4 | F4+ architecture claims in base/ | medium | Known DACH hardcode passes gate without L-UNIV-GREP |
| DRR template (§2) | F5 | all decisions/*.md + variant drafts | medium | DRR entry passes with <80w in any part |
| Forbidden phrases (§3) | F4 | variant draft body text | medium | F-1..F-10 phrase passes without R.refuted_if |

**Composite confidence.** All deltas rated F5 or F4. F-level grounded in:
JETIX-ARCHITECTURE-BRIEF §4.6 (F-G-R mandatory per-agent), FPF E-5 (integrator
adds F/ClaimScope/R per claim), philosophy-critic §1-§3 (4-NO + 1-CONDITIONAL),
prompts §1.4 depth measure #4 (F-G-R on every major claim). No delta reaches
F6+ because empirical testing (the variant drafts themselves) has not yet run.

---

## §8 Provenance

| Source | Section | Load-bearing citation |
|---|---|---|
| philosophy-critic §1 H-1..H-5 | Conformance checklist | 4-NO + 1-CONDITIONAL verdicts driving all 5 deltas |
| philosophy-critic §2 H-1 | Acceptance predicate | "Every claim ... carries a triple with populated `R.refuted_if` field naming an observable measurement" |
| philosophy-critic §2 H-2 | Alternative A | "each client's graph is a closed holon — no inter-graph edge types involving two different clients" |
| philosophy-critic §2 H-3 | Alternative B | "each of the 6 variant drafts contains a `§ Lock compliance` section that enumerates all 24 Locks" |
| philosophy-critic §2 H-4 | Alternative A | "/lint is instantiated per-client as a separate process with access only to that client's filesystem tree" |
| philosophy-critic §5 | Falsifiability flag list | 10 forbidden phrases F-1..F-10 (restated in §3 with lint regex) |
| philosophy-critic §6 | Universality B/C/D | "B-test passes when every UC-9 mechanism is expressed via configurable triple; D-test: grep → 0 hits" |
| decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md §2.4 | E-4 optimizer rubric | "invariants WLNK/MONO/IDEM/COMM/LOC constrain what optimization may change" |
| decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md §2.5 | E-5 F-G-R | "R: reliability (pathwise, not point estimate)" — basis for R.refuted_if |
| decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md §2.9 | E-9 DRR | "{context, decision, alternatives, review-checkpoint}" 4-part template |
| decisions/JETIX-ARCHITECTURE-BRIEF.md §4.6 | Continuous quality metrics | "F-G-R frontmatter (formality F0-F9 / scope / reliability R-low|medium|high|certified|formally-proven)" |
| decisions/JETIX-ARCHITECTURE-BRIEF.md §6 | Hard Constraints | "Any variant violating any of these is disqualified without review" — Lakatos hard core |
| decisions/JETIX-ARCHITECTURE-BRIEF.md §1 | Executive Summary | "No Jetix-specific content in base (universality B/C/D tests; D2 §10)" |
| decisions/JETIX-ARCHITECTURE-BRIEF.md §5.5 | Portability | "Symbolic test applies to base/ repo subtree" |
| prompts/km-architecture-research-2026-04-24.md §1.4 #4 | F-G-R depth measure | "F-G-R tagging on every major claim in every variant. Bare assertions without F-G-R are not claims in this cycle; they are noise." |
| prompts/km-architecture-research-2026-04-24.md §1.4 #5 | Dissent-preservation | "Explicit preserved dissents, minimum three. Do NOT average dissenting conclusions." |
| prompts/km-architecture-research-2026-04-24.md §3.9 | UC-9 | "architecture must make [cross-client data access] impossible by construction — not by policy" |
| .claude/agents/philosophy-expert.md §4.1 | Optimizer invariants | "WLNK / MONO / IDEM / COMM / LOC must hold; if unclear defer to integrator" |
| .claude/agents/philosophy-expert.md §4.3 | Method-change refusal | "If the proposed optimization changes the method itself ... escalate — this is strategizing territory" |
| .claude/agents/philosophy-expert.md §2.4 (P3) | Lakatos | "A research programme has a hard core + protective belt; refutations hit the belt first, then the core" |

---

*Draft status: authored by philosophy-expert, mode: optimizer.
Awaiting brigadier integration into cycle cyc-km-architecture-2026-04-24.*
