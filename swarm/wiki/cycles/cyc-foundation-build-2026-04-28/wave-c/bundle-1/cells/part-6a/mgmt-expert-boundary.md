---
title: Part 6a — mgmt-expert boundary cell
date: 2026-04-28
phase: C-1-cell
expert: mgmt-expert
modes: [boundary]
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 6a
F: F4
ClaimScope:
  holds_when: "Foundation Parts 6a / 6b split analysis within cyc-foundation-build-2026-04-28 Wave C Bundle 1; Phase A single-owner Jetix context"
  not_valid_when: "RUSLAN-LAYER executor bindings; post-Phase-A schema revisions; multi-fork Part 6 deployments where Part 6b gate-class taxonomy diverges"
R:
  tier: R-medium
  refuted_if: >
    Any canonical artefact reaches swarm/wiki/foundations/ via Part 6a alone (without traversing
    Part 6b gate); OR Part 6a is found to own or re-define AWAITING-APPROVAL packet internal
    schema; OR Part 6b is found to execute quarterly F-G-R audits or run /lint --check-fg-r
    scans autonomously without consuming Part 6a outputs
  accepted_if: >
    Three successive Part 6a deliverable promotions (P6a.1-P6a.4) route exclusively through Part
    6b stop-gate packets with human ack; AND quarterly audit reports write to swarm/audits/ without
    touching Part 6b packet contents; AND gate_class field in log.jsonl remains a reference-only
    coupling, not an embedded schema duplication
sources:
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md L300-360"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md §4 P6 A.6.B"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6a/philosophy-expert-multi-mode.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6a/engineering-expert-multi-mode.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md §3-§4"
---

# Part 6a — mgmt-Expert Boundary Cell
## Delivery-Boundary Analysis: Split Rationale, Seam Verification, Phase B Fork Readiness

> **Self-exemplification.** This document applies the same provenance discipline it analyses. Every
> claim carries `[src:path:section]` + F-G-R inline. L/A/D/E lanes are named. All dependency
> references use A.14 typed edges. Anti-scope is explicit.

---

## §A Scope Declaration

This cell operates from the **mgmt-expert delivery-boundary lens**: the question of whether the
Part 6a / Part 6b split is *organisationally clean* — meaning each part can change cadence
independently, each part can be owned by a distinct delivery agent in Phase B/C/D, and the seam
between them does not leak in either direction.

The management question is not "what does Part 6a contain?" (philosophy-expert resolved that
fully in §I.1–§I.3 of its multi-mode cell) nor "how is the scanner implemented?" (engineering-
expert resolved that in §2.1–§2.3). The management question is: **does the boundary hold under
pressure from future change?** — change in cadence, change in scope, change in fork operators.

**F4 | ClaimScope: mgmt-boundary lens is delivery-discipline, not code review or epistemic
audit | R: refuted_if this cell's boundary findings are superseded by a direct contradiction
in Part 6b design documents (not yet produced at time of writing)**

---

## §B Split Rationale: Cadence Independence Verification

The primary management criterion for a clean split is **cadence independence**: two parts must
be able to evolve their operating rhythms without forcing each other to change.

### §B.1 Part 6a Cadence: Quarterly

Part 6a operates on a **quarterly cadence**. Its four Wave C deliverables map to a single
quarterly rhythm:

- P6a.1 (F-G-R JSON Schema): define once; evolve only on F8 constitutional revision with
  AWAITING-APPROVAL gate. Change frequency: rare (constitutional boundary). [src:philosophy-
  expert-multi-mode.md:§L P6a.1 "F8 constitutional update requiring Ruslan ack"]
- P6a.2 (Citation Enforcement Scanner): run per-commit (fast path, deterministic) AND per-
  quarterly immune audit (slow path with RLAIF). Change frequency: moderate (scanner
  calibration) but the *schema* does not change with each calibration. [src:engineering-
  expert-multi-mode.md:§2.4 "RLAIF must be disabled on pre-commit hooks"]
- P6a.3 (Approval Log Format): append on every gate event, but the *format* evolves only
  on schema version bump. Change frequency: rare. [src:engineering-expert-multi-mode.md:
  §3.2 schema_version + event-sourcing upcasting]
- P6a.4 (Quarterly Immune Audit Framework): fires quarterly. Not per-artefact, not per-
  commit. The cadence is calendar-driven (Q1/Q2/Q3/Q4). [src:philosophy-expert-multi-
  mode.md:§J.2 "Quarterly audit (scheduled)"]

**Delivery assessment:** Part 6a's operational cadence is long-interval. The schema artefacts
(f-g-r.json, approval-log-entry.json) are effectively stable once promoted. The scanner runs
frequently but its *interface contract* (exit codes, stderr format) changes rarely. The quarterly
audit fires four times per year. This is fundamentally different from Part 6b's expected cadence.

**F4 | ClaimScope: Phase A, Jetix single-owner | R: refuted_if quarterly audit fires more
than once per month in practice (indicating it is not quarterly but per-event)**

### §B.2 Part 6b Cadence: Real-Time Per-Artefact

Part 6b owns: AWAITING-APPROVAL packet schema, blast-radius classifier, Default-Deny rule for
uncategorized actions, and the stop-gate enforcement path. These operate at **real-time per-
artefact cadence**. Every time an agent submits a draft for canonical promotion, Part 6b fires.
Every time an action lacks a blast-radius tag, Part 6b fires Default-Deny immediately. [src:
part-6-governance-provenance-human-gate.md:§B "Any agent action before execution"]

Part 6b's blast-radius classification table (wave-c-worklist Bullet 2) must be a *living*
artefact: as Jetix encounters novel action categories (Phase B multi-client operations, external
API integrations, financial disbursements), the table requires additions. The change frequency
for Part 6b is therefore moderate-to-high in Phase B, compared to Part 6a's rare-to-moderate.

**Cadence independence verdict:**

| Dimension | Part 6a | Part 6b | Independent? |
|---|---|---|---|
| Primary trigger | Quarterly calendar / per-commit (fast) | Per-agent-action / per-artefact-submission | YES — non-overlapping triggers |
| Schema change frequency | Rare (constitutional) | Moderate (blast-radius additions, gate-class evolution) | YES — different change drivers |
| Who decides runtime behaviour | Philosophy-expert + engineering-expert (scanner calibration) | Investor-expert + systems-expert (blast-radius policy) | YES — different decision authorities |
| Phase B driver | F-G-R coverage maturity, citation discipline | New action categories, multi-fork gate customisation | YES — different Phase B pressures |

**F4 | ClaimScope: cadence-independence claim holds for Phase A + Phase B pressures as reasoned
above; NOT validated against actual Phase B operational data (does not yet exist) | R: refuted_if
Part 6b schema changes require synchronised changes to Part 6a f-g-r.json in >30% of cases over
10 consecutive change events**

---

## §C Seam Analysis: Where Does 6a End and 6b Begin?

The seam is the boundary line. A clean seam means: anything on the 6a side can be changed
without triggering a change on the 6b side, and vice versa — except at the explicitly declared
coupling points.

### §C.1 The Three Declared Coupling Points

From combined reading of philosophy-expert and engineering-expert cells:

**Coupling Point 1: `gate_class` field in the approval log.**

The `gate_class` field in `swarm/approvals/log.jsonl` is a Part 6a artefact that references
Part 6b's gate-class taxonomy (`stop_gate | approval_gate | foundation_revision |
phase_b_activation`). [src:engineering-expert-multi-mode.md:§3.5 "gate_class field in the
approval log schema couples Part 6a to Part 6b's gate-class taxonomy. This coupling is
necessary but must be documented as an A.14 typed edge: Part 6a approval-log `references`
Part 6b gate-class taxonomy."]

**Management assessment of this coupling:** This is a *reference coupling*, not a *schema-
embedding coupling*. The approval log stores the gate class label as a string value. If Part
6b adds a new gate class (`external_write_gate` for Phase B), Part 6a's log schema does NOT
change — it simply records a new enum value. The enum lives in Part 6b; the log records it.
One-directional coupling. **Acceptable at this seam.**

The required mitigation (per engineering-expert FINDING-2) is that this A.14 typed edge must be
declared: `Part 6a approval-log MemberOf Part 6b gate-class taxonomy` is WRONG; the correct
edge is `Part 6a approval-log references Part 6b gate-class taxonomy` — noting that "references"
is a lightweight coupling edge, not ConstituentOf or ComponentOf. [src:levenchuk-shsm-fpf.md:
§4 P4 A.14 "every dependency must be typed; generic depends-on is forbidden"]

**Coupling Point 2: Part 6a's `gate_packet_path` is a read-only reference to Part 6b artefact.**

The approval log entry schema contains `gate_packet_path: <swarm/awaiting-approval/filename>`.
This is a disk path to a Part 6b artefact. Part 6a records the reference; it does NOT read
the packet's internal structure and does NOT re-define the packet schema. [src:engineering-
expert-multi-mode.md:§3.5 "The approval log records that a gate occurred and where the gate
packet lives; Part 6b owns the gate packet schema and authoring."]

**Management assessment:** Clean. A path reference is the lightest possible coupling. If Part 6b
changes the gate packet's internal structure (adds a `decision_rationale:` field, changes
`blast_radius` sub-fields), the approval log is unaffected. The `gate_packet_path` still resolves.
This coupling does NOT constrain Part 6b's evolution. **Clean at this seam.**

**Coupling Point 3: F-G-R tags at promotion time — Part 6a defines schema; Part 6b applies it.**

When Part 6b issues a stop-gate packet and Ruslan acks it, Part 6b writes the canonical
promotion and records the F-G-R snapshot in the approval log. The schema for *what* to record
is Part 6a's `f-g-r.json`. Part 6b is a *consumer* of Part 6a's schema, not an owner of it.
[src:philosophy-expert-multi-mode.md:§D "Part 6a `methodologically-uses` Part 6b (Gate
Enforcement). Part 6b's real-time gate enforcement triggers Part 6a F-G-R tagging at promotion
time; Part 6a defines the tagging schema that Part 6b applies."]

**Management assessment:** This is the *intended* dependency direction. Foundation layer
(6a schema) is stable; RUSLAN-LAYER enforcement arm (6b gate execution) consumes the stable
schema. This maps cleanly to the constitutional principle that Foundation layer = generic and
stable; RUSLAN-LAYER = specific and adaptive. [src:levenchuk-shsm-fpf.md:§4 P1 IP-1 Role≠
Executor: "the schema is the role; the enforcement arm is the executor-binding"]

**F4 | ClaimScope: three coupling points above are the COMPLETE set at Wave C design stage;
additional couplings may emerge in Phase B (e.g., if blast-radius classification adds an F-G-R-
level sub-classification) | R: refuted_if a fourth undeclared coupling point is found during
Part 6b design work that requires synchronised changes to Part 6a artefacts**

### §C.2 Cargo-Cult Detection → Escalation Decision: The Key Seam Test

The mission brief identifies a critical seam test: "Part 6a detects cargo-cult; Part 6b decides
whether to escalate to human." This is the detection vs decision split.

Philosophy-expert's cell is explicit: "Does NOT execute halts. Advisory only. When the scanner
finds a Law violation, it surfaces the finding to brigadier / Part 6b for enforcement.
Self-executing halts would cross into instrumental authority." [src:philosophy-expert-multi-
mode.md:§F "Does NOT execute halts. Advisory only."]

Engineering-expert's scanner design confirms: the scanner outputs structured stderr (exit code
+ flag report); it does NOT issue AWAITING-APPROVAL packets; it does NOT invoke halt sequences.
[src:engineering-expert-multi-mode.md:§2.1 "/lint --check-citations interface: exit N — N
citation flags found; stderr — structured report"]

**Management assessment of this seam:** CLEAN. The signal flow is:

```
Part 6a scanner → structured findings (exit code + stderr report)
    → brigadier reads report
    → if Law violation: brigadier constructs AWAITING-APPROVAL packet (Part 6b mechanism)
    → Ruslan acks → Part 6b records gate outcome
    → Part 6a approval log appends entry
```

No step in this flow requires Part 6a to make a gate decision. No step requires Part 6b to run
the scanner. The seam is at the handoff of the structured report from Part 6a to brigadier.
Brigadier is the integration agent between the two parts — it is not a part of either.

**Risk flagged:** IF a future cycle adds a "Part 6a auto-escalates high-severity cargo-cult
findings directly to AWAITING-APPROVAL" mechanism, this seam breaks. Part 6a would be
writing gate packets (Part 6b territory). The correct pattern is: Part 6a raises the finding
with severity tag; Part 6b (via brigadier) decides whether the severity warrants a gate packet.
Detection never escalates autonomously — that is the AP-MGMT-4 scope-creep anti-pattern
applied to governance architecture.

### §C.3 Quarterly Audit Findings → Remediation Decision: The Second Seam Test

Part 6a produces the quarterly audit report to `swarm/audits/quarterly-YYYY-QN.md`. The report
lists findings across five dimensions (F-G-R drift, citation health, cargo-cult, dangling edges,
IP-1 violations). [src:engineering-expert-multi-mode.md:§4.2 D1-D5 audit dimensions]

Who decides which findings become AWAITING-APPROVAL packets? Part 6b, via brigadier. Part 6a
categorizes finding severity; it does NOT author the gate packet. The audit report's §9
"Escalations to Brigadier" section (philosophy-expert §I.3) names the findings that *require*
gate escalation — but naming the requirement is different from authoring the packet.

**Management assessment:** This seam is clean at design stage. The risk is structural: if the
quarterly audit template starts embedding gate-packet templates inline (e.g., "Escalation for
Finding X: paste this into swarm/awaiting-approval/..."), Part 6a has crossed into Part 6b
territory. The template MUST stop at "this finding class requires an AWAITING-APPROVAL packet;
brigadier authors it per Part 6b schema."

**F4 | ClaimScope: seam cleanliness is structural (design-level); operational leakage may
emerge once the first quarterly audit fires in Q2-2026 | R: refuted_if first quarterly audit
report contains any embedded gate-packet YAML structure**

---

## §D Decision Authority: Distinct Per Part

A clean organisational boundary requires **distinct decision authorities** — different actors
decide what happens in each part.

| Decision type | Authority | Part | Basis |
|---|---|---|---|
| F-level assignment to a promoted artefact | Author + audit verifier | 6a | Philosophy-expert owns epistemic-audit function; F-level is an epistemic claim [src:philosophy-expert-multi-mode.md:§G] |
| `refuted_if` Hamel-binary predicate quality | Philosophy-expert critic gate | 6a | "Validation rule 2 (Hamel-binary refuted_if) is the most philosophically load-bearing constraint" [src:philosophy-expert-multi-mode.md:§I.1] |
| Gate outcome (approve / reject) | Ruslan (HITL) | 6b | FUNDAMENTAL §4.3 Human-Only; not delegatable [src:part-6-governance-provenance-human-gate.md:§E Laws] |
| Blast-radius category assignment | Part 6b classifier (investor-expert critic) | 6b | wave-c-worklist Bullet 2: "investor-expert critic (blast-radius has capital implications)" [src:wave-c-worklist.md:L329] |
| Scanner calibration (cargo-cult threshold) | Engineering-expert (RLAIF tuning) | 6a | RLAIF pre-filter is Part 6a scope [src:engineering-expert-multi-mode.md:§2.2 Algorithm D] |
| AWAITING-APPROVAL packet schema | Part 6b designer | 6b | Engineering-expert explicitly anti-scoped: "Does NOT author the AWAITING-APPROVAL gate packet schema. That is Part 6b territory." [src:engineering-expert-multi-mode.md:§6.3] |
| F8/F9 schema revision | Ruslan HITL with brigadier gate | 6a → 6b gate | F8 constitutional boundary; Part 6a proposes via AWAITING-APPROVAL; Part 6b routes [src:philosophy-expert-multi-mode.md:§C "Does NOT modify F-G-R schema autonomously"] |

**Management conclusion on authority separation:** The authorities are distinct. The two parts do
not share a decision type at any current design stage. The only potential overlap is the
F8/F9 schema revision, which correctly flows *from* Part 6a (the schema owner proposes) *through*
Part 6b (the gate mechanism routes) *to* Ruslan HITL (the sole F8 decision authority). This is a
clean serial chain, not a shared authority.

**F4 | ClaimScope: decision-authority mapping is complete at Wave C design stage | R: refuted_if
a Part 6b design document assigns the F-level assignment decision to Part 6b rather than Part 6a**

---

## §E Phase B Fork Importability Verdict

Per the mission brief, a Phase B partner should be able to import Part 6a's generic artefacts
while substituting their own Part 6b RUSLAN-LAYER bindings.

### §E.1 What a Phase B Fork IMPORTS as-is (Foundation layer)

| Part 6a artefact | Importable? | Basis |
|---|---|---|
| `shared/schemas/f-g-r.json` (F-G-R JSON Schema) | YES, generic | "Any D27 fork may use this schema as-is" [src:philosophy-expert-multi-mode.md:§X Foundation partition]. Schema does not name Ruslan, DACH, or cycle IDs. |
| Approval log entry format (YAML/JSONL structure) | YES, role-label | `actor: ruslan` is a role label (human-owner), not a person-binding. Fork substitutes their own human owner. [src:philosophy-expert-multi-mode.md:§X "`actor: ruslan` is a role label, not a person-binding"] |
| Quarterly audit template dimensions (D1-D5) | YES, generic | Dimensions (F-G-R drift, citation health, dangling edges, IP-1 violations) are generic to any FPF Foundation deployment. [src:engineering-expert-multi-mode.md:§4.2 D1-D5] |
| `/lint --check-citations` interface contract | YES, generic | Interface is 5 lines (exit code + stderr). Does not reference Jetix paths in its *contract*. RUSLAN-LAYER: the specific canonical paths scanned. [src:engineering-expert-multi-mode.md:§2.1] |
| L/A/D/E structure (§E lanes) | YES, Foundation | L/A/D/E is FPF A.6.B constitutional. "L/A/D/E structure is Foundation." [src:philosophy-expert-multi-mode.md:§X] |
| RLAIF integration contract | YES with caveat | Contract (what input/output the RLAIF call produces) is generic. The provider, model name, and cost per call are RUSLAN-LAYER. A fork substitutes their own RLAIF endpoint. [src:engineering-expert-multi-mode.md:§6.3 "RUSLAN-LAYER: model endpoint"] |

### §E.2 What a Phase B Fork REPLACES (RUSLAN-LAYER equivalents)

| Element | Reason for replacement | Basis |
|---|---|---|
| `gate_class` enum values | Fork defines their own gate taxonomy (different action categories, different organisational risk topology) | wave-c-worklist Bullet 2 blast-radius table is explicitly Jetix-specific; "J-level authority mapping per category" is RUSLAN-LAYER [src:wave-c-worklist.md:L321] |
| Blast-radius category assignments | Capital implications differ by business context (a DACH consulting fork vs a US product fork have different financial action thresholds) | [src:wave-c-worklist.md:L329 "investor-expert critic (blast-radius has capital implications at J-Strategic tier)"] |
| Escalation taxonomy | Who receives escalations, what constitutes "strategic" vs "operational" — these are org-specific | Part 6b scope |
| Specific canonical wiki paths (`swarm/wiki/`, `swarm/approvals/`) | Fork defines their own mono-repo path structure | [src:philosophy-expert-multi-mode.md:§X "Specific artefact paths are Jetix mono-repo paths"] |
| Executor-name registry for IP-1 audits (D5) | Fork has different executor names | [src:engineering-expert-multi-mode.md:§4.2 D5 "requires RUSLAN-LAYER executor name list"] |

### §E.3 Importability Verdict

**Part 6a is a GENERIC provenance layer.** Its schemas, its scanner contract, its audit
template, and its log format are portable across any FPF Foundation deployment. The RUSLAN-LAYER
bindings (paths, executor names, specific gate-class values) are cleanly segregated in Part 6b.

This matches the Cagan Principle 2 (Shape Up appetite discipline) applied to architecture: Part
6a's scope is *shaped and bounded* — it does not expand into blast-radius policy, it does not
absorb AWAITING-APPROVAL packet definitions, it does not own the escalation chain. The appetite
boundary ("provenance officer: scanner + audit + log schema") is respected.
[src:product-management-cagan-shape-up.md:§4 Principle 2 "Fixed time, variable scope —
appetite set first; scope is what fits inside it"]

**F4 | ClaimScope: importability claim holds for Phase B fork with FPF Foundation baseline;
NOT validated for a fork with a different constitutional layer (non-FPF) | R: refuted_if a
Phase B fork operator adopts Part 6a schemas and finds they require Jetix-specific modifications
to >30% of fields to function in their context**

---

## §F Risk Register: Boundary-Violation Risks

Four boundary-violation risks, each with detection trigger and prevention rule.

### §F.1 Risk: F-G-R-Driven Gate Decision Bleeds into Part 6a

**Pattern:** A future ROY cycle proposes "Part 6a should recommend a gate decision based on
the F-level of the submitted artefact — e.g., auto-approve F6+ artefacts, auto-deny F0-F2
artefacts." This would give Part 6a *decision authority* in addition to *detection authority*.

**Why it is a boundary violation:** Gate decisions (approve/deny) are Part 6b territory per
FUNDAMENTAL §4.3. Human ack is "architecturally mandatory, not behaviourally expected."
[src:part-6-governance-provenance-human-gate.md:§E Laws "Human ack is the TERMINAL decision
point for every canonical promotion."] If Part 6a starts making gate recommendations that
function as pre-decisions, the human gate's authority is eroded by a technically-non-binding
but practically-influential upstream filter.

**Detection trigger:** Any proposed design document that includes a `recommended_gate_action:`
field in Part 6a scanner output or audit findings. The *existence* of the field creates the
bleed, even if it is labelled "advisory."

**Prevention rule:** Part 6a outputs are FINDINGS, not RECOMMENDATIONS with gate implications.
The finding format is `{type, file, line, severity, evidence}`. No `gate_action:` field.
Brigadier translates findings into gate packets via Part 6b; Part 6a does not participate
in the translation.

**F4 | ClaimScope: this risk is real but not yet materialized; flagged for Watch during Part
6b design | R: refuted_if Part 6b design document explicitly forbids Part 6a recommended-action
fields in its own anti-scope**

### §F.2 Risk: AWAITING-APPROVAL Packet Embeds F-G-R Audit Findings Inline

**Pattern:** Part 6b's gate packet template starts including a section "F-G-R compliance
findings from Part 6a scanner" inline in the packet body. What begins as a convenience
(Ruslan sees everything in one packet) becomes a schema coupling: Part 6b's packet now has
a structural dependency on Part 6a's finding format.

**Acceptable variant:** Part 6b packet includes `lint_report_path: <swarm/logs/lint-events-
YYYY-MM-DD.jsonl>` — a read-only path reference. This is the same pattern as `gate_packet_path`
in the approval log: a reference, not an embedding.

**Reject variant:** Part 6b packet embeds the scanner output as a nested YAML block. This
creates schema coupling: if Part 6a changes its finding format (e.g., adds a `false_positive_
suppressed_by_rlaif: bool` field), Part 6b packet schema must update in lockstep.

**Prevention rule:** Part 6b gate packet schema MUST NOT embed Part 6a finding content. It
MAY include a path reference to the associated lint report. The distinction is REFERENCE vs
EMBEDDING. [src:engineering-expert-multi-mode.md:§3.5 AP-3 acceptance predicate:
"swarm/approvals/log.jsonl entries contain zero embedded copies of AWAITING-APPROVAL
packet body content (only gate_packet_path reference)"] — the inverse of this check applies
to Part 6b packets referencing Part 6a outputs.

### §F.3 Risk: Approval Log Becomes a Substitute for AWAITING-APPROVAL Packet

**Pattern:** As the approval log matures and gains rich structured fields (`gate_class`,
`artefact_f_level`, `reversibility`, `acked_by`), a well-intentioned engineer proposes
"we can skip the separate gate packet — just log the approval event directly in
swarm/approvals/log.jsonl." This substitutes the log for the packet.

**Why it is a boundary violation:** The AWAITING-APPROVAL packet is Part 6b's *blocking
mechanism* — it exists at state `BLOCKED` until Ruslan acks it. The approval log is Part 6a's
*recording mechanism* — it records gate events that have already been resolved. Skipping
the packet eliminates the blocking state: there would be no enforced pause before promotion.
[src:part-6-governance-provenance-human-gate.md:§C Side-effects "Writes swarm/awaiting-
approval/<cycle>-<slug>.md — gate packet (BLOCKED state, awaiting human ack)"]

**Detection trigger:** Any artefact in `swarm/wiki/foundations/` whose promotion is traceable
in the approval log but has no corresponding AWAITING-APPROVAL packet in `swarm/awaiting-
approval/` or `swarm/gates/`.

**Prevention rule:** The quarterly audit (Part 6a D-dimension check, beyond the current D1-D5
declared by engineering-expert) should include: `count(canonical promotions in approval log
without corresponding gate packet) = 0`. This is a sixth audit dimension the mgmt lens
recommends adding: **D6 — Gate-packet completeness ratio**.

**F4 | ClaimScope: Phase A single-owner; Ruslan's personal discipline currently prevents this
risk; Phase B with additional contributors raises risk materially | R: refuted_if all 11 D-series
lock-indexed canonical decisions (D1-D29) have corresponding gate packets verifiable in the
audit**

### §F.4 Risk (Priority Boundary Risk): IP-1 Violation in Part 6b Spec Leaks into Part 6a Audit Scope

**Pattern:** Part 6b design document names specific executor agents ("brigadier will issue the
AWAITING-APPROVAL packet") as Foundation-level constituents of Part 6b. Part 6a's quarterly
audit (D5 IP-1 check) runs over Foundation artefacts and finds these executor names. Suddenly
Part 6a's audit is reporting on Part 6b's IP-1 compliance.

**This is NOT a boundary violation** — Part 6a's D5 IP-1 check applies to all Foundation-
tagged artefacts, which includes any Part 6b documents that declare themselves as Foundation
layer. Part 6a auditing Part 6b's IP-1 compliance is correct governance. This is the "Part 6
`operates-in` all other parts" structural edge from the interface card. [src:part-6-
governance-provenance-human-gate.md:§D "Part 6 `operates-in` all other Parts. Governance
is the supersystem context every other part operates within."]

**Management note:** This is NOT a risk to prevent — it is a feature to preserve. Part 6a's
audit authority over IP-1 violations applies universally. The risk would be if Part 6b
*exempted itself* from Part 6a's audit scope, claiming it is "internal governance and
therefore not subject to governance audit." That exemption would break the constitutional
self-referentiality. Part 6 must audit itself.

---

## §G Cagan / Shape Up Appetite Assessment

### §G.1 Part 6a Appetite: 2-Day Wave C Build

Per mission brief: Part 6a appetite is 2-day within Bundle 1 (scaled as 1/3 of total Part 6
budget). The philosophy-expert cell produced a full 5000-7000 word multi-mode analysis
(§A-§N plus schemas and templates). The engineering-expert cell produced ~4200 words with
detailed algorithm specifications, JSONL schema, and acceptance predicates. Together these
two cells represent the full P6a.1-P6a.4 design scope. [src:philosophy-expert-multi-mode.md:
closing "Word count target: 5000-7000 words"] + [src:engineering-expert-multi-mode.md:
closing "Word count: approximately 4,200 words"]

**Shape Up verdict on Part 6a:** The scope was *shaped* correctly. The design outputs (JSON
Schema, skill spec design, log format, audit template) are bounded artefacts with Hamel-binary
acceptance predicates. No scope creep into Part 6b territory was detected. The appetite of
2 days is justified by the four well-scoped deliverables. [src:product-management-cagan-
shape-up.md:§4 Principle 2 "Fixed time, variable scope — appetite set first; scope is what
fits inside it"]

### §G.2 Part 6b Appetite: 3-Day Wave C Build

Part 6b carries the heavier scope: Default-Deny classifier, blast-radius table, AWAITING-APPROVAL
packet schema, stop-gate enforcement mechanism. The constitutional weight of Default-Deny (it is
a Foundation invariant per FUNDAMENTAL §6.1 "якщо action не categorized — default deny + escalate,
не creative interpretation" [src:part-6-governance-provenance-human-gate.md:§E Laws]) justifies
the higher appetite. A 3-day appetite for a constitutional mechanism is proportionate.

**Hill-chart milestone for Part 6b (Shape Up discipline):** The "figuring-it-out" phase for
Part 6b centres on the blast-radius category taxonomy. Once the categories are enumerated and
the Default-Deny rule is stated as a Hamel-binary predicate, Part 6b moves to execution.
The hill-chart top is "blast-radius table canonical artefact produced." Post-hill: acceptance
predicate validation, dependency edge declarations, AWAITING-APPROVAL packet schema finalised.

**Sum appetite:** 5 days for Part 6a + Part 6b combined. Within Bundle 1's 12-18h walltime
estimate. The 5-day estimate assumes the design cells (philosophy + engineering for 6a;
equivalent cells for 6b) are the primary cost centres. [src:wave-c-worklist.md:L302
"Effort M" for each Part 6 bullet]

### §G.3 Scope-Hammering Rule for Part 6a (if under time pressure)

If the 2-day Part 6a appetite runs short, the scope-hammering priority order (per Shape Up
circuit-breaker rule) is:

1. **MUST ship:** P6a.1 (f-g-r.json schema) — constitutional; without it, F-G-R compliance
   has no formal definition
2. **MUST ship:** P6a.3 (approval log format) — the gate mechanism cannot produce auditable
   records without it
3. **SHOULD ship:** P6a.4 (quarterly audit template) — the first audit cycle provides
   cadence discipline; deferral one quarter is survivable
4. **MAY defer to Part 6b Wave C or Wave D:** P6a.2 (citation scanner implementation) —
   the scanner specification is complete; implementation can be deferred without breaking
   the system (manual cargo-cult checks are survivable in Phase A)

**F4 | ClaimScope: scope-hammering priority reflects Phase A single-owner survival order;
Phase B mandates all four | R: refuted_if Ruslan determines a different item is the survival
priority during Wave C materialisation**

---

## §H L/A/D/E Lane Declarations (boundary-cell specific)

Per FPF A.6.B [src:levenchuk-shsm-fpf.md:§4 P6]: this section applies L/A/D/E to the
Part 6a / Part 6b *interface* itself, not to the parts individually (which have their own
L/A/D/E in philosophy-expert and engineering-expert cells).

### Laws (invariants governing the 6a / 6b interface):

1. Part 6a MUST NOT write AWAITING-APPROVAL packets. Detection-layer outputs are findings
   only. The seam is findings-in → packets-out at brigadier. Violation = scope-leak.
2. Part 6b MUST NOT run citation scans or F-G-R field presence checks. Enforcement-layer
   inputs are structured findings from Part 6a. Violation = inverted dependency.
3. The `gate_class` field in Part 6a's approval log MUST remain a reference coupling only
   (string value from Part 6b taxonomy). Violation = embedding coupling.
4. Part 6a's F-G-R schema revisions MUST route through Part 6b's gate mechanism (AWAITING-
   APPROVAL packet) before promotion. Violation = Part 6a unilaterally modifying its own
   constitutional schema.

### Admissibility (what the 6a/6b interface accepts):

- Part 6a → brigadier: structured lint report (exit code + YAML findings per file per check).
  Accepted: findings with severity + evidence. Rejected: findings with `gate_action:` field.
- Part 6b → Part 6a (via approval log): gate outcome (acked / rejected). Accepted: JSONL
  entry per schema v1.0.0 with all required fields. Rejected: inline packet body embedding.

### Deontics (obligations at the seam):

- Brigadier MUST translate Part 6a findings into gate packets (Part 6b) when Law violations
  are found — not buffer or batch across cycles.
- Part 6a MUST surface every finding with severity + evidence to brigadier within the same
  cycle that produced the finding. Silent buffering = AP-MGMT-12 (provenance empty on non-
  trivial output).

### Effects (measurable outcomes at the seam):

- Seam health metric: `count(canonical promotions with Part 6a approval log entry) /
  count(canonical promotions)` = 100%. Measures whether Part 6b's gate is connected to
  Part 6a's recording. Measured at quarterly audit.
- Seam violation metric: `count(canonical promotions without corresponding AWAITING-APPROVAL
  packet)` = 0 (D6 proposed dimension from §F.3 above).

---

## §I Anti-Scope

This boundary analysis does NOT:

- **Define the blast-radius classification table or Default-Deny rule.** That is Part 6b
  scope (wave-c-worklist Bullet 2). This cell analyses the boundary from Part 6a's side.
- **Specify the AWAITING-APPROVAL packet schema.** That is Part 6b. This cell only
  describes what Part 6a must NOT embed from that schema.
- **Evaluate the F-G-R triad epistemically.** Philosophy-expert resolved the first-principles
  justification in §I.1 of its cell. This cell accepts F-G-R as the given schema and analyses
  its organisational boundary placement.
- **Code-review the citation scanner implementation.** Engineering-expert owns that critique
  (§2 of its cell). This cell analyses delivery-boundary cleanliness.
- **Project capital implications of the blast-radius threshold settings.** That is investor-
  expert × critic territory (wave-c-worklist Bullet 2 "investor-expert critic").
- **Strategize whether to split Part 6 further.** The 6a/6b split is established by OQ-
  MERGED-1 override from brigadier. This cell verifies the split is clean; it does not
  propose alternative splits. Method-choice = HITL per §1d.

---

## §J Synthesis: Split Verdict

### J.1 Is the Split Clean?

**Verdict: YES, with one watch item.**

The three declared coupling points (§C.1) are all one-directional references, not bidirectional
schema embeddings. The two cadence rhythms (quarterly vs real-time per-artefact) are genuinely
independent. The decision authorities (F-level assignment vs gate outcome) are distinct.
The Phase B importability partition (Foundation generic vs RUSLAN-LAYER specific) is clean
and machine-readable via `ClaimScope.scope_tokens` in the f-g-r.json schema.

**Watch item:** The `gate_class` coupling (§C.1 Coupling Point 1) must be formally documented
as an A.14 typed edge in both Part 6a and Part 6b dependency sections. At the time of this
analysis, engineering-expert's cell identifies this as FINDING-2 — the edge is not yet
declared in Part 6's canonical dependency graph. Until it is declared, the coupling is
structurally implicit, which means it could be duplicated or modified without detection.

**Proposed action:** brigadier should add to Part 6a's `§D Dependencies` table (interface card)
a new row: `Part 6a approval-log references Part 6b gate-class taxonomy | references-value-from
(proposed A.14 extension: lightweight value-reference coupling) | rationale: log records gate
class string from Part 6b taxonomy; one-directional; no schema embedding`. If "references-
value-from" is not in the current A.14 edge vocabulary, the nearest valid edge is `methodologically-
uses` with a note clarifying the constraint is read-only value coupling.

### J.2 Can Each Part Change Cadence Independently?

**Verdict: YES.**

Part 6b can add a new gate class (`multi_fork_promotion`) without triggering changes to Part
6a's f-g-r.json schema, scanner algorithm, or audit template. Part 6a can evolve its scanner
calibration thresholds (RLAIF suppression rate cap, 200-char window for cargo-cult) without
triggering changes to Part 6b's blast-radius table or AWAITING-APPROVAL packet schema.

The one exception is an F-G-R schema revision (P6a.1 constitutional update). This requires a
Part 6b gate event (AWAITING-APPROVAL packet). But this is by design: constitutional schema
changes *should* require a gate. The gate mechanism enforcing the schema change is not a
cadence coupling — it is the constitutional authority pathway. The change is rare (F8 level)
and the gate is correct procedure.

### J.3 Where Is the Seam?

The seam lives at **brigadier's translation layer**. Part 6a produces findings; brigadier
reads findings; brigadier authors gate packets (Part 6b mechanism) when Law violations warrant
them; Part 6b executes the gate; Part 6a records the outcome. Brigadier is the integration
agent — it holds both sides of the seam in its context without merging them into a single
Part.

This is the correct architectural placement: brigadier is the orchestration authority (per
mgmt-expert §1a "brigadier owns routing, decomposition, gating, integration"); neither Part
6a nor Part 6b should absorb the orchestration function.

**F4 | ClaimScope: seam placement at brigadier holds for Phase A; Phase B may require a
dedicated "governance coordination" role if the volume of findings-to-packets translation
exceeds brigadier's decision budget | R: refuted_if brigadier's gate packet volume exceeds
10 per cycle sustained for 3 cycles — signals the seam needs a delegated governance-coordination
layer between 6a and 6b**

---

## §K Provenance

| Source | Sections used | F-level |
|---|---|---|
| `part-6-governance-provenance-human-gate.md` | §A-§H; Laws; Anti-scope; Dependencies | F4 (Phase A interface card, operational) |
| `wave-c-worklist.md` L300-360 | Bullets 1-4; effort/expert allocation; OQ-MERGED-6 | F4 (cycle worklist, operational) |
| `levenchuk-shsm-fpf.md` §4 P4/P5/P6 | A.14 typed edges; F-G-R B.3; L/A/D/E A.6.B | F5 (consultant card, library-direct FPF read) |
| `philosophy-expert-multi-mode.md` | §D dependencies; §F anti-scope; §I.1-§I.3 schemas; §X Foundation/RUSLAN-LAYER partition | F4 (Wave C cell, operational convention) |
| `engineering-expert-multi-mode.md` | §2.1-§2.3 scanner; §3.1-§3.5 approval log; §4.2 audit dimensions; §6.2 FINDING-2; §6.3 anti-scope; §7 acceptance predicates | F4 (Wave C cell, operational convention) |
| `product-management-cagan-shape-up.md` §3-§4 | Principle 2 Shape Up appetite; anti-scope §3; boundary discipline | F4 (consultant card; library-direct Shape Up read) |

---

*End of Part 6a — mgmt-expert boundary cell.*
*Word count: approximately 2100 words in analysis body + provenance sections.*
*Next step: brigadier reviews; if boundary verdict is confirmed, Part 6b design begins with explicit dependency on this cell's §C.1 coupling-point declarations and §F.3 proposed D6 audit dimension.*
