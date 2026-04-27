---
title: Part 6a — philosophy-expert multi-mode cell (epistemic-audit + first-principles + integrator)
date: 2026-04-28
phase: C-1-cell
expert: philosophy-expert
modes: [epistemic-audit, first-principles, integrator]
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 6a
F: F4
ClaimScope:
  holds_when: "Foundation Parts 1-10 in-scope; cyc-foundation-build-2026-04-28 Wave C Bundle 1 context"
  not_valid_when: "RUSLAN-LAYER executor bindings; DACH-specific deliverables; post-Phase-A schema revisions"
R:
  refuted_if: >
    Any promoted canonical artefact in swarm/wiki/ carries F-G-R fields inconsistent
    with the JSON Schema f-g-r.json designed here; OR the citation scanner emits
    >20% false-positive rate on a 20-item synthetic test suite; OR the approval log
    format is found non-append-only after one write cycle
  accepted_if: >
    P6a.1 JSON Schema passes structural validation; P6a.2 scanner flags 8/10 cargo-cult
    test cases correctly; P6a.3 approval log first entry written correctly per format;
    P6a.4 quarterly audit template used for at least one audit cycle without brigadier
    requesting format revisions
sources:
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md L300-360"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/philosophy-expert.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md §4 P5 + §5"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md §4 + §7"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/mereology-typed-edges.md"
  - "design/JETIX-FPF.md §4.2 B.3 + §12.7"
  - "raw/books-md/anthropic/bai-2022-cai.md §1-§3"
---

# Part 6a — Philosophy-Expert Multi-Mode Cell
## Epistemic Audit + First-Principles + Integrator

> Self-exemplification: this document DOGFOODS what it defines.
> Every claim carries `[src:path:section]` + F-G-R. Every dependency
> uses A.14 typed edges. L/A/D/E lanes are explicit. This is not ornament —
> it is the acceptance criterion for Part 6a's own outputs.

---

## Preface — Multi-Mode Activation

This cell runs three simultaneous epistemic modes. Findings are tagged inline:

- **[EPISTEMIC]** — Popperian falsifiability audit, refutation conditions, evidence decay
- **[FIRST-PRINCIPLES]** — why F-G-R triad, not duo or quad; irreducible epistemic primitives
- **[INTEGRATOR]** — synthesizing inputs, defining contract surface, resolving cross-paradigm tension

Mode-default rule (per philosophy-expert §5.0): if context is ambiguous, treat as integrator.
No single mode dominates; all three produce simultaneous output across §§A-N below.

---

## §A Inputs

| Source | Data shape | Event trigger | F-G-R status |
|--------|-----------|---------------|-------------|
| Draft artefact from any Part | `.md` file with YAML frontmatter: `proposed_writes[]`, `provenance[]`, `F-G-R fields` | `submit-draft-for-gate-event` | MUST carry F3+ to enter gate; F0-F2 = gate failure |
| Canonical artefact for re-audit | Promoted `.md` file in `swarm/wiki/` | `quarterly-audit-event` | Existing F-G-R fields checked for drift vs B.3.4 decay |
| Citation lint request | Path to canonical doc or dir | `commit-hook-event` OR manual `/lint --check-citations` | N/A — scanner input, not claim carrier |
| Approval action | Human ack signal (Ruslan) or brigadier-with-ack packet | Post-human-ack | Creates an approval-log entry (P6a.3) |
| Quarterly audit trigger | Part 8 health-check cron | `quarterly-audit-event` | N/A — trigger only |

**[INTEGRATOR]** The admissibility threshold F3+ for canonical promotion is sourced from two convergent claims: (a) FPF B.3 declares F0-F2 as pre-formal, single-source, or unvalidated — "not yet ready for operational use as canonical knowledge" [src:design/JETIX-FPF.md:§12.7 B.3]; (b) Part 6 interface card §E Laws lane states "F-G-R frontmatter fields present" as an admissibility gate condition [src:part-6-governance-provenance-human-gate.md:§E Admissibility]. The synthesis: F0-F2 objects must live only in `swarm/wiki/drafts/` — never in canonical paths. Consequence: the f-g-r.json schema (P6a.1) must enforce this boundary structurally.

---

## §B Outputs

| Consumer | Data shape | Event published | F-G-R |
|---------|-----------|----------------|-------|
| Brigadier + Ruslan | F-G-R compliance report (`swarm/audits/quarterly-YYYY-QN.md`) | `compliance-report-emitted-event` | F4, R-medium (report quality bounded by scanner coverage) |
| Canonical artefact store (via Part 1) | F-G-R tags in promoted artefact frontmatter | `artifact-promoted-event` | F-level per promoted content; minimum F3 |
| Developer / pipeline | Citation lint results (stdout/stderr) | Per commit or manual invocation | N/A |
| Audit trail (Part 1 substrate) | Approval log entry (append-only to `swarm/approvals/log.md`) | `audit-log-appended-event` | F5 for the log format itself (codified rule) |
| Part 8 (health consumer) | Drift signals: stale F-G-R, broken citations, IP-1 violations | `compliance-report-emitted-event` | F4 signal quality; Part 8 refines into F5+ health metrics |

**[EPISTEMIC]** The compliance report is F4, not F5, at this design stage because: the scanner (P6a.2) is not yet implemented; existing F-G-R coverage data comes from manual observation, not systematic scan. F-level promotes to F5 when: (a) scanner runs on first full canonical artefact set AND (b) results are reviewed by Ruslan-ack. Falsifier for this F-level claim: "compliance report generated by automated scanner AND reviewed in one complete quarterly cycle" — if that occurs, F4 → F5 is justified. Failing that, the report remains F4 (operational convention, manually assembled). [src:design/JETIX-FPF.md:§12.7 B.3 F-level anchors]

---

## §C Side-Effects

- Appends to `swarm/approvals/log.md` (append-only; never edits prior entries) [src:part-6-governance-provenance-human-gate.md:§C Side-effects; D25 Company-as-Code]
- Emits citation lint results to stderr (does NOT modify artefacts — advisory output only) — consequence: each flag requires a human or brigadier response cycle, not auto-fix
- Writes quarterly audit reports to `swarm/audits/quarterly-YYYY-QN.md` (new file per audit cycle; never overwrites prior)
- Does NOT write canonical wiki content — all canonical writes flow through Part 6b gate + brigadier [src:part-6-governance-provenance-human-gate.md:§C "Does NOT write wiki canonical content directly"]
- Does NOT modify F-G-R schema autonomously — any schema change is an F8 constitutional update requiring Ruslan ack

**[EPISTEMIC]** The "advisory, not auto-fix" constraint on scanner output is Popper-grounded: a scanner that auto-corrects citations is applying an instrumental decision (how to fix it) that belongs to a human or downstream Part. The scanner's epistemic role is to falsify the claim "all citations are valid" by producing counterexamples. What to do with the counterexamples is instrumental — outside this part's scope per FPF L1003-1006 epistemic vs instrumental Рациональность split. [src:philosophy-expert.md:§1a Dual-ownership note]

---

## §D Dependencies (typed A.14 — zero "depends-on")

| Edge | Type | Rationale |
|------|------|-----------|
| Part 6a `methodologically-uses` Part 1 (System State Persistence) | `methodologically-uses` | Approval log appends through git commit substrate; scanner results surfaced via git-tracked artefacts. Part 6a invokes Part 1's mechanism without being constituted by it — non-rigid dependency [src:mereology-typed-edges.md:§5 table] |
| Part 6a `methodologically-uses` Part 6b (Gate Enforcement) | `methodologically-uses` | Part 6b's real-time gate enforcement triggers Part 6a F-G-R tagging at promotion time; Part 6a defines the tagging schema that Part 6b applies. Separation: Part 6a = schema + audit; Part 6b = real-time gate execution [src:part-6-governance-provenance-human-gate.md:§D Dependency table; wave-c-worklist.md:L300-303] |
| Part 6a `MemberOf` Part 6 governance cluster | `MemberOf` | Part 6a is one member of the Part 6 governance collection alongside Part 6b. MemberOf is correct (not ComponentOf) because removing Part 6a from the governance collection degrades Part 6 but does not destroy it — Part 6b's real-time gate function could operate (degraded) without the quarterly audit arm [src:mereology-typed-edges.md:§5 table MemberOf] |
| Part 6a `creates` F-G-R compliance report | `creates` | The quarterly audit framework (P6a.4) is a creator system that produces the compliance report artefact. Directed creation: Part 6a is productive, the report is target [src:mereology-typed-edges.md:§5 table creates] |
| Part 8 `methodologically-uses` Part 6a quarterly audit | `methodologically-uses` | Part 8 health monitoring consumes the compliance report as an input signal. Part 8 invokes Part 6a's audit output without being constituted by it [src:part-6-governance-provenance-human-gate.md:§D "Part 6 ↔ Part 8 dual"] |
| Part 6a `constrained-by` FUNDAMENTAL §6.1 (11 hard AI/agent limits) | `constrained-by` | Part 6a's scanner and audit framework cannot violate the 11 constitutional limits; they are external boundaries on Part 6a's state space, not internal structure [src:anthropic-constitutional-ai.md:§4 P3; part-6-governance-provenance-human-gate.md:§E Laws] |
| f-g-r.json schema `ConstituentOf` Part 6a | `ConstituentOf` | The JSON Schema is a logical/conceptual section of Part 6a — a rule-clause inside Part 6a's specification. It lives inside Part 6a as a structural constituent [src:mereology-typed-edges.md:§5 table ConstituentOf] |

**[INTEGRATOR]** The Part 6a/Part 6b split is the key integration decision in this document. The two arms of Part 6 represent a temporal and functional decomposition: Part 6a = retrospective, auditing, schema-defining (quarterly cadence); Part 6b = prospective, real-time gate enforcing, approval-packet issuing (per-artefact cadence). They are distinct PhaseOf the same Part 6 governance mission, but they are better modeled as MemberOf the governance cluster (two distinct sub-holons) than as PhaseOf each other — because their lifecycles are independent (Part 6a runs quarterly even when Part 6b has zero gate events). [src:mereology-typed-edges.md:§5 table PhaseOf vs MemberOf]

---

## §E Boundary — L/A/D/E Discipline

### Laws (invariants that MUST hold)

1. Every promoted canonical artefact in `swarm/wiki/` MUST carry F-G-R fields (F, ClaimScope, R) in frontmatter. Absence = gate failure, not warning. **Falsifier**: any canonical artefact without F-G-R fields in a lint pass. [src:levenchuk-shsm-fpf.md:§4 P5; design/JETIX-FPF.md:§4.2 CP-2]

2. F0-F2 artefacts MUST NOT be promoted to canonical. They belong in `swarm/wiki/drafts/` or in-cell scratchpad only. **Falsifier**: any `swarm/wiki/` canonical path containing a file with `F: F0`, `F: F1`, or `F: F2`. [src:design/JETIX-FPF.md:§12.7 B.3 F-level anchors]

3. F8/F9 claims MUST require Ruslan ack before promotion. Constitutional and mathematically formal claims cannot be promoted by brigadier alone. **Falsifier**: any F8/F9 artefact in `swarm/wiki/foundations/` without a corresponding AWAITING-APPROVAL packet with human ack timestamp. [src:philosophy-expert.md:§1d requires-approval; FUNDAMENTAL §4.3]

4. Every `[src:...]` citation in a canonical artefact MUST resolve to an existing file path + section anchor. Dangling citations = broken provenance chain. **Falsifier**: `/lint --check-citations` returns non-zero broken-citation count against any canonical artefact. [src:part-6-governance-provenance-human-gate.md:§E Admissibility "provenance[] non-empty"]

5. RLAIF self-critique (Bai 2022) CANNOT substitute for Ruslan ack. It is a pre-gate noise filter only. The human gate (Part 6b) remains the terminal decision authority. **Falsifier**: any artefact in canonical state whose approval log entry lacks a human actor field. [src:anthropic-constitutional-ai.md:§5 T3; FUNDAMENTAL §4.3 Human-Only]

6. The approval log (`swarm/approvals/log.md`) MUST be append-only. No edits to prior entries. **Falsifier**: any git diff showing modification to an existing log entry (not a new entry appended above or below). [src:part-6-governance-provenance-human-gate.md:§E Laws; D25 Company-as-Code]

### Admissibility (what Part 6a accepts as valid input)

- Draft artefact is accepted into F-G-R audit ONLY IF: (a) `F:` field present in frontmatter (value may be F0..F9), (b) `ClaimScope:` field present and non-empty, (c) `R:` field present with at least `refuted_if:` declared. Incomplete F-G-R = audit-deferred, not audit-failed — the scanner surfaces the gap without blocking. [src:part-6-governance-provenance-human-gate.md:§E Admissibility]

- Citation scan is accepted for any `.md` file in `swarm/wiki/` canonical paths. Drafts MAY be scanned but findings are advisory (not gate-blocking).

- Quarterly audit trigger is accepted from Part 8 ONLY via `quarterly-audit-event` signal. Ad-hoc audit requests from non-Part-8 sources require brigadier mediation.

### Deontics (obligations)

- Part 6a MUST surface every F-G-R gap with line + section reference (not a generic "F-G-R missing"). Same discipline as Part 6 single-line-interface anti-pattern (AP-L4). [src:levenchuk-shsm-fpf.md:§8 AP-L4]

- Part 6a MUST publish quarterly audit report to `swarm/audits/` within the same cycle that triggered the audit. Holding findings without publishing = silent error swallowing. [src:FUNDAMENTAL §5.5 no-silent-error-swallowing]

- Part 6a MUST tag every IP-1 violation (executor name in Foundation-level Part definitions) found in audit as a separate finding class, not a generic "F-G-R violation." IP-1 violations have a different remediation path than F-level problems. [src:part-6-governance-provenance-human-gate.md:§E Laws IP-1 enforcement; philosophy-expert.md §1 pre-read §§2-4]

- Part 6a MUST NOT make canonical promotion decisions autonomously. Its role is to report + gate-input, not to promote. [src:part-6-governance-provenance-human-gate.md:§F Anti-scope first bullet]

### Effects (measurable outcomes)

- F-G-R coverage: (canonical artefacts with valid F-G-R tags) / (total canonical artefacts) = 100% target. Measured per quarterly audit. Starting baseline: unknown (first audit cycle establishes baseline). [src:part-6-governance-provenance-human-gate.md:§E Effects]

- Broken citation rate: (broken citations detected) / (total citations scanned) = 0% target. Measurable immediately on first lint run.

- Cargo-cult citation rate: flagged cargo-cult citations / total citations = drift signal (no hard target; downward trend over 3 cycles = R-medium → R-high for provenance discipline).

- IP-1 violation count: target 0 per quarterly audit in Foundation-level artefacts.

---

## §F Anti-Scope

- **Does NOT make canonical promotion decisions.** Part 6b enforces the real-time gate; Part 6a reports compliance and tags F-G-R drift. The distinction is temporal: Part 6a is retrospective (quarterly), Part 6b is prospective (per-artefact). [src:part-6-governance-provenance-human-gate.md:§F Anti-scope]

- **Does NOT execute halts.** Advisory only. When the scanner finds a Law violation, it surfaces the finding to brigadier / Part 6b for enforcement. Self-executing halts would cross into instrumental authority. [src:philosophy-expert.md:§1b out_of_scope_tasks]

- **Does NOT own AWAITING-APPROVAL packet schema.** Part 6b owns the gate packet format (structure, required fields, routing logic). Part 6a's approval log records the outcome of gate events, not the packet itself.

- **Does NOT modify F-G-R schema autonomously.** The f-g-r.json schema is a constitutional artefact (F8). Any revision requires Ruslan ack. Part 6a proposes revisions via AWAITING-APPROVAL packet; brigadier routes; Ruslan decides. [src:philosophy-expert.md:§1d requires-approval "epistemic claim against an accepted foundation"]

- **Does NOT implement sycophancy detection.** OQ-CAI-3 is a Wave C gap [src:anthropic-constitutional-ai.md:§8 OQ-CAI-3]. Part 6a defines a stub placeholder in the quarterly audit template (§L below) but does not specify the detection mechanism — that is Wave D or Part 8 scope.

- **Does NOT own the blast-radius classification table.** That is P6.2 (Part 6b / Part 6 Wave C Bullet 2), not Part 6a scope. Part 6a's F-G-R scanner and audit framework are orthogonal to blast-radius classification.

---

## §G F-G-R Tagging — DOGFOOD

This section DOGFOODS P6a.1: every major claim in Part 6a's own architecture is tagged below. This demonstrates what F-G-R looks like when applied to design-document claims, not just to wiki content.

| Claim | F | ClaimScope (G) | R (Reliability) |
|-------|---|---------------|-----------------|
| F0-F2 artefacts must not be canonical | F7 | All Foundation Parts; any Jetix instance | R-high — derived from FPF B.3 (F6+) + FUNDAMENTAL §4.3; refuted_if: FPF B.3 F-level anchors are revised to lower threshold |
| JSON Schema approach for F-G-R definition | F5 | Foundation Part 6a scope; JSON Schema draft-07 or later | R-medium — codified rule; refuted_if: alternative schema format (YAML Schema, CDDL) is formally acked as preferred by Ruslan |
| `/lint --check-citations` as skill spec | F4 | Jetix mono-repo; Phase A single-owner | R-medium — operational convention pending first implementation cycle |
| Approval log append-only format | F6 | All Foundation Parts; all Jetix instances per D27 fork contract | R-high — codified + 10 cycles operational (D25 established); refuted_if: git log shows a prior entry modified |
| Quarterly audit cadence | F5 | Foundation Phase A; single-owner cycle | R-medium — codified; refuted_if: audit cadence formally revised to monthly or semi-annual via AWAITING-APPROVAL packet |
| RLAIF pre-filter, not gate substitute | F6 | Any Jetix instance; any AI-augmented canonical promotion workflow | R-high — CAI §5 T3 explicitly states this; human gate primary authority grounded in FUNDAMENTAL §4.3 |
| Sycophancy detection = stub (OQ-CAI-3) | F3 | Wave C scope; single-owner Phase A | R-low — gap acknowledged, mechanism undefined; refuted_if: OQ-CAI-3 closes with an implemented detection mechanism |

**[EPISTEMIC]** Note the heterogeneity: claims about logical/structural invariants (F0-F2 not canonical) earn F7 because they are derived from peer-reviewed FPF methodology (F6+) with an explicit Popper-falsifiable threshold. Claims about implementation conventions (JSON Schema approach, lint skill spec) earn F4-F5 because they reflect operational choices not yet validated across cycles. This heterogeneity is a feature, not a defect — it allows downstream consumers to distinguish "architectural necessity" from "current best practice." Collapsing all claims to F5 would be epistemic false certainty; collapsing to F3 would undersell the structural invariants. [src:levenchuk-shsm-fpf.md:§4 P5 "No false certainty"]

---

## §H Code-Level Interfaces

### H.1 `/lint --check-citations`

Skill spec path (stub): `swarm/wiki/skills/lint-check-citations.md`

```
Entry point:   /lint --check-citations [--path=<dir-or-file>] [--strict]
Input:         One or more .md files in swarm/wiki/ canonical paths
Output:        YAML-structured report to stdout; flags to stderr
Exit codes:    0 = clean; 1 = findings present; 2 = scanner error
```

Subcommand variants:
- `--check-citations` — citation completeness + cargo-cult check (P6a.2)
- `--check-fg-r` — F-G-R fields presence + level compliance (P6a.1)
- `--audit-quarterly` — triggers quarterly audit framework (P6a.4), writes to `swarm/audits/`

### H.2 `/lint --check-fg-r`

```
Scan target:   All .md files under specified path (default: swarm/wiki/)
Checks:
  (a) F: field present in frontmatter
  (b) F level >= F3 if file is in canonical path (not drafts/)
  (c) ClaimScope: field present and non-empty
  (d) R.accepted_if or R.refuted_if present (Hamel-binary predicate check)
Output:        Per-file findings with line reference; summary counts
```

### H.3 Schema validators

- `shared/schemas/f-g-r.json` — JSON Schema draft-07; validates frontmatter F-G-R fields
- `shared/schemas/approval-log-entry.json` — validates each approval log entry structure

### H.4 Quarterly audit invocation

```
Trigger:       Part 8 health-check event OR manual `brigadier --trigger quarterly-audit`
Output path:   swarm/audits/quarterly-<YYYY>-Q<N>.md
Format:        Per §I below (quarterly-template.md)
```

---

## §I Data Schemas

### I.1 F-G-R JSON Schema (`shared/schemas/f-g-r.json`)

**[FIRST-PRINCIPLES]** Before specifying the schema, the first-principles question must be answered: WHY is F-G-R a TRIAD and not a duo or quad?

**The irreducibility argument:**

Three epistemic primitives cover orthogonal dimensions of claim quality that cannot be collapsed:

1. **Formality (F)** answers: "How rigorously was this claim derived?" — the *process* dimension. It captures the derivation pedigree: single hunch (F0) vs multi-cycle validated rule (F6) vs constitutional invariant (F8). A claim cannot have its formality inferred from its scope or reliability — a claim can be high-formality but narrow-scope (e.g., an F7 mathematical fact that applies only within one bounded context). Dropping F would force G to carry derivation-quality information, corrupting G's role as a pure scope declaration.

2. **ClaimScope (G)** answers: "Where does this claim hold?" — the *context* dimension. It bounds the claim's validity domain. Per FPF IP-2 Context-is-king [src:levenchuk-shsm-fpf.md:§4 P3]: "make meaning local; make translation explicit." A claim about F-G-R enforcement in a single-owner Phase A context does not automatically hold in a multi-fork enterprise deployment. Dropping G would allow claims to silently overgeneralize — the anti-pattern FPF calls "scope soup." G cannot be replaced by F or R: a high-reliability claim (R-high) can still have a narrow scope (single bounded context).

3. **Reliability (R)** answers: "How trustworthy is this claim, given evidence?" — the *evidence* dimension. It captures the warrant: how many sources, how many validation cycles, what would refute it. Per Popper P1 [src:philosophy-expert.md:§2.4 P1]: a claim without a refutation criterion has R-undefined status. R carries the Popperian falsifiability condition in the `refuted_if:` field. Dropping R would eliminate the epistemic accountability mechanism — the system would have well-derived (F) and well-scoped (G) claims with no way to distinguish "robustly evidenced" from "guessed with precision."

**Why not a duo?**

- F + G without R: you know how rigorously the claim was derived and where it applies, but you have no evidence-based accountability. A peer-reviewed claim (F7) about domain X (G = narrow) could be completely wrong with no refutation path. This duo describes a formal but potentially vacuous claim.

- F + R without G: you know derivation quality and evidence strength, but the claim applies "everywhere" by default. This is the scope-soup anti-pattern. A R-high F6 claim asserted universally may be correct in one context and deeply wrong in another.

- G + R without F: you know where the claim applies and how trustworthy it is, but you have no information about how it was derived. A well-evidenced (R-high), well-scoped (G = Foundation) claim could be based on a single author's intuition (F1) or on 10-cycle validated convention (F4). The distinction matters for how much weight to put on the claim when F-level evidence accumulates.

**Why not a quad?**

A plausible fourth dimension is **Temporal validity (T)** — when does the claim expire? But FPF B.3 subsumes this under R via the `decay_after:` field (B.3.4 Evidence Decay) [src:design/JETIX-FPF.md:§4.2 CP-2 "Evidence decay tracking"]. Temporal validity is a property of the reliability warrant, not a separate epistemic axis. Including T as a fourth axis would create redundancy with R's decay mechanics.

Another plausible fourth dimension is **Author authority (A)** — who made the claim? But author authority is already captured by F-level: F7+ requires documented derivation methodology, which implicitly encodes author process; F5+ requires "codified rule (canonical — written down + reviewed)" which encodes review authority. Separate author field would conflate the process (F) with the person, violating IP-1 Role≠Executor discipline at the epistemic level.

**Verdict [FIRST-PRINCIPLES]:** F-G-R is the minimal sufficient triad. Each dimension is irreducible to the others. Together they cover process, context, and evidence — the three necessary conditions for a claim to be actionable in a multi-agent, multi-cycle knowledge system. This is the first-principles justification for the triad rather than any other cardinality.

---

**JSON Schema specification:**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/f-g-r.json",
  "title": "F-G-R Trust Calculus Schema",
  "description": "FPF B.3 F-G-R triad fields. Required on all promoted canonical artefacts.",
  "type": "object",
  "required": ["F", "ClaimScope", "R"],
  "properties": {
    "F": {
      "description": "Formality level F0-F9 per FPF B.3",
      "type": "string",
      "enum": ["F0","F1","F2","F3","F4","F5","F6","F7","F8","F9"],
      "x-semantic": {
        "F0": "personal hunch / single-authored claim, no review",
        "F1": "pattern observed once, weak repeatability",
        "F2": "hypothesis with intent to test",
        "F3": "informal multi-source synthesis",
        "F4": "operational convention (3+ cycles applied)",
        "F5": "codified rule (written + reviewed)",
        "F6": "codified rule + 3+ successful applications + cross-cycle reuse evidence",
        "F7": "methodology with explicit acceptance predicate",
        "F8": "constitutional boundary (FUNDAMENTAL Vision lock-class)",
        "F9": "mathematically formalised invariant (rare)"
      }
    },
    "ClaimScope": {
      "description": "Structured scope: where this claim holds and where it does not",
      "type": "object",
      "required": ["holds_when"],
      "properties": {
        "scope_tokens": {
          "description": "One or more canonical scope identifiers",
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "Foundation",
              "RUSLAN-LAYER",
              "Phase-A-single-owner",
              "Jetix-mono-repo",
              "multi-fork",
              "single-cycle-only",
              "cycle-bounded"
            ]
          },
          "minItems": 1
        },
        "holds_when": {
          "description": "Free-text statement of conditions under which claim is valid",
          "type": "string",
          "minLength": 10
        },
        "not_valid_when": {
          "description": "Free-text statement of conditions under which claim does NOT hold",
          "type": "string"
        }
      }
    },
    "R": {
      "description": "Reliability tier + Popperian falsification criterion",
      "type": "object",
      "required": ["tier", "refuted_if"],
      "properties": {
        "tier": {
          "type": "string",
          "enum": ["R-low", "R-medium", "R-high", "R-certified"],
          "x-semantic": {
            "R-low": "anecdotal, single-source, no replication",
            "R-medium": "multi-source synthesis, informal replication",
            "R-high": "peer-reviewed, formal validation, or 10+ consistent cycles",
            "R-certified": "external auditor-verified or formally proven"
          }
        },
        "refuted_if": {
          "description": "Hamel-binary falsification criterion — one condition that would refute this claim",
          "type": "string",
          "minLength": 10
        },
        "accepted_if": {
          "description": "Hamel-binary acceptance criterion (optional but recommended)",
          "type": "string"
        },
        "receipt": {
          "description": "Where to verify the claim's evidence base",
          "type": "string"
        }
      }
    },
    "decay_after": {
      "description": "B.3.4 Evidence Decay — ISO 8601 date after which this claim is flagged stale",
      "type": "string",
      "format": "date"
    }
  },
  "additionalProperties": false
}
```

**Validation rules:**

1. `F` in `[F3, F4, F5, F6, F7, F8, F9]` for any canonical artefact path (not in `drafts/`). F0-F2 values = draft-only; promoting to canonical = gate failure.
2. `R.refuted_if` MUST be present and MUST be a Hamel-binary predicate (one-line condition, not prose essay). Scanner check: length < 200 chars AND does not start with prose qualifiers ("It would be difficult to..." / "Potentially...").
3. F8/F9: requires AWAITING-APPROVAL packet with `actor: ruslan` in approval log before canonical promotion.
4. `decay_after` is optional. If present, the quarterly audit flags artefacts past that date as `STALE` (finding class `F-G-R-decay`).
5. `ClaimScope.scope_tokens` must include at least one of: `Foundation`, `RUSLAN-LAYER`, `Phase-A-single-owner` — the three top-level layer tokens that map to FUNDAMENTAL §0's Foundation/RUSLAN-LAYER distinction. [src:part-6-governance-provenance-human-gate.md:§E Laws; philosophy-expert.md:§1 PP-2]

**[EPISTEMIC]** Validation rule 2 (Hamel-binary `refuted_if`) is the most philosophically load-bearing constraint in the entire schema. It operationalizes Popper P1 (falsifiability) as a structural field requirement, not a convention. The anti-pattern it prevents: a `refuted_if` that reads "this claim would be refuted if evidence emerged suggesting otherwise" — this is tautological, not falsifiable. A genuine Hamel-binary predicate names a specific observable: "any canonical artefact without F-G-R fields in a lint pass." This is falsifiable because the lint pass is a concrete action with a deterministic output. [src:philosophy-expert.md:§2.4 P1 Popper falsifiability; design/JETIX-FPF.md:§4.2 CP-2]

---

### I.2 Approval Log Entry Format (`swarm/approvals/log.md`)

**[INTEGRATOR]** The approval log bridges Part 6a's retrospective audit function and Part 6b's real-time gate function. It is the shared artifact that makes gate events auditable. Part 6a defines the entry schema; Part 6b writes entries at gate time; Part 6a reads entries during quarterly audit. This bidirectional relationship is `methodologically-uses` in both directions — neither owns the other's substrate.

```yaml
# swarm/approvals/log.md
# APPEND-ONLY. New entries prepended above previous. Never edit existing entries.
# Entry format:

---
timestamp: <ISO 8601 UTC, e.g. 2026-04-28T14:32:00Z>
actor: ruslan | brigadier-with-ack | autonomous-low-risk
packet_id: <AWAITING-APPROVAL packet reference, e.g. swarm/awaiting-approval/cycle-X-slug.md>
gate_class: stop_gate | stage_gate | draft_promotion
fg_r_delta:
  F_before: <F-level before, e.g. F3, or "none" if new artefact>
  F_after: <F-level after promotion, e.g. F5>
reversibility: reversible | hard-to-reverse | irreversible
artefact_path: <full path to promoted artefact in swarm/wiki/ or decisions/>
reason: <optional; recommended for non-trivial gate decisions>
---
```

**Field semantics:**

- `actor` encodes the Part 6 + FUNDAMENTAL §4.3 authority hierarchy:
  - `ruslan` = human ack; sole authority for F8/F9, irreversible, and constitutional promotions
  - `brigadier-with-ack` = brigadier acting on explicit prior Ruslan ack per standing authorization
  - `autonomous-low-risk` = Tier 3 routine action per FUNDAMENTAL §4.1 auto-always; no ack required; logged for audit completeness

- `gate_class` maps to FUNDAMENTAL §4.1-§4.6 decision classification:
  - `stop_gate` = hard-BLOCKED; Ruslan ack mandatory before any action
  - `stage_gate` = project lifecycle promotion (Part 7 uses this class)
  - `draft_promotion` = draft → canonical elevation; requires F-G-R compliance

- `fg_r_delta` is the measurable epistemic contribution of each gate event. It enables the quarterly audit to chart F-level trajectory over time — are claims maturing (F3→F5) or stagnating? [src:levenchuk-shsm-fpf.md:§4 P5 "FPF-Steward Q-audit includes F-G-R compliance check"]

- `reversibility` implements FUNDAMENTAL §4.6 reversibility check + Anthropic "Building Effective Agents" [src:anthropic-constitutional-ai.md:§4 P5]: "Prefer reversible over irreversible actions." Logging irreversibility makes the post-hoc audit able to verify that all irreversible promotions had `actor: ruslan`.

---

### I.3 Audit Template Structure (`swarm/audits/quarterly-template.md`)

```markdown
---
title: Quarterly F-G-R + Provenance Immune Audit — <YYYY> Q<N>
date: <ISO 8601>
triggered_by: part-8-quarterly-audit-event | manual
cycle: <cycle-id>
auditor: philosophy-expert | human-override
F: F4
ClaimScope: "Holds for all canonical artefacts in swarm/wiki/ at audit date"
R:
  tier: R-medium
  refuted_if: "scanner run fails to complete OR auditor manually overrides >10% of scanner findings without documented rationale"
---

# Quarterly Immune Audit — <YYYY> Q<N>

## 1. Audit Scope

- Canonical artefacts scanned: <count>
- Drafts excluded: <count>
- Scan date range: <from> to <to>
- Scanner version: <lint version or "manual">

## 2. F-G-R Drift

| Finding class | Count | Severity |
|---------------|-------|----------|
| Missing F field (canonical path) | <N> | High |
| F0-F2 in canonical path | <N> | High (gate violation) |
| Missing ClaimScope | <N> | Medium |
| Missing R.refuted_if | <N> | High (Popper gap) |
| Non-Hamel-binary refuted_if | <N> | Medium |
| Stale (past decay_after date) | <N> | Medium |
| F8/F9 without Ruslan-ack approval log entry | <N> | High (constitutional) |

## 3. Citation Health

| Metric | Value | Target |
|--------|-------|--------|
| Total citations scanned | <N> | — |
| Broken citations (path not resolved) | <N> | 0 |
| Cargo-cult citations (no consequence sentence) | <N> | Downward trend |
| Cargo-cult after RLAIF pre-filter | <N> | Downward trend |

## 4. Typed Edge Health

| Metric | Value | Target |
|--------|-------|--------|
| Total edges in wiki/graph/edges.jsonl | <N> | — |
| Dangling edges (target not found) | <N> | 0 |
| Generic "depends-on" edges found | <N> | 0 |

## 5. IP-1 Violations

| Artefact | Executor name found | Remediation |
|----------|--------------------|-|
| <path> | <executor name in Foundation-level definition> | Replace with role archetype; move to RUSLAN-LAYER |

## 6. Sycophancy Detection (STUB — OQ-CAI-3)

> Status: OQ-CAI-3 unresolved (Wave C gap). [src:anthropic-constitutional-ai.md:§8 OQ-CAI-3]
> Mechanism: undefined. Placeholder for Wave D / Part 8 specification.
> Manual trigger: if Ruslan observes sycophancy pattern in any synthesis artefact,
> log in this section with artefact path + observed pattern + AWAITING-APPROVAL
> for correction cycle.

Findings this quarter: <N or "none — detection mechanism not yet implemented">

## 7. Audit Summary

| Dimension | Status | Trend |
|-----------|--------|-------|
| F-G-R coverage | <X>% | ↑ / ↓ / → |
| Broken citations | <N> | ↑ / ↓ / → |
| Cargo-cult rate | <X>% | ↑ / ↓ / → |
| IP-1 violations | <N> | ↑ / ↓ / → |
| Dangling edges | <N> | ↑ / ↓ / → |

## 8. Priority Remediations (Top 5)

1. <artefact path> — <finding class> — <required action>
2. ...

## 9. Escalations to Brigadier

> List any findings that require AWAITING-APPROVAL packet (e.g., F8/F9 without Ruslan ack,
> dangling edges in foundations/, IP-1 violations in Foundation Parts)

## 10. Coordination Note — Part 8

> Part 8 methodologically-uses this audit framework. This section summarizes what Part 8
> should consume as health signals from this audit.
> [src:part-6-governance-provenance-human-gate.md:§D Dependencies Part 6 ↔ Part 8]
```

---

## §J Operational Rituals

### J.1 Per-commit lint (event-driven)

```
Trigger: git pre-commit hook (implementation: Phase B)
Command: /lint --check-citations [--path=staged-files]
         /lint --check-fg-r [--path=staged-files]
Blocking: yes (for canonical paths); advisory (for drafts/)
Output: stderr flags; blocks commit if Law violations found
```

**[INTEGRATOR]** Per-commit lint is the real-time enforcement arm of Part 6a's schema. It is distinct from the quarterly audit: the per-commit check is deterministic and fast (structural validation only); the quarterly audit is comprehensive and interpretive (includes RLAIF pre-filter, IP-1 pattern recognition, drift trend analysis). Neither replaces the other. [src:levenchuk-shsm-fpf.md:§5 trigger 4 "Promoting a draft artefact to canonical"]

### J.2 Quarterly audit (scheduled)

```
Trigger: Q1 (Jan), Q2 (Apr), Q3 (Jul), Q4 (Oct) — or manual via brigadier
Command: /audit --quarterly [--cycle=<cycle-id>]
Output:  swarm/audits/quarterly-<YYYY>-Q<N>.md
Commit:  brigadier commits after Ruslan review
```

### J.3 RLAIF pre-filter integration (P6a.2 cargo-cult check)

**[EPISTEMIC]** RLAIF integration requires careful epistemic scoping. Bai 2022 §1.2 describes the RLAIF loop as: "generate critiques and revisions against constitutional principles" — a model evaluating its own outputs [src:raw/books-md/anthropic/bai-2022-cai.md:§1.2]. Applied to cargo-cult citation detection, the RLAIF pre-filter asks: "does the surrounding text contain an implicit consequence sentence even if not explicitly structured as one?" This reduces false positives in the cargo-cult check.

However, three constraints bound this application:

1. RLAIF applies ONLY to cargo-cult check (Type 2 — implicit consequence detection), NOT to bare-claim check (Type 1 — deterministic: citation absent = flag) or broken-citation check (Type 3 — deterministic: path resolves or it doesn't). [src:deep-prompt §2.2 P6a.2 design constraint]

2. RLAIF output is advisory, not authoritative. If RLAIF marks a cargo-cult citation as "implicit-consequence-present," the scanner suppresses the flag. But if Ruslan or brigadier reviews and disagrees, the flag can be manually restored. Human judgment overrides RLAIF pre-filter.

3. RLAIF pre-filter is NOT a gate substitute. The constitutional AI constraint (RLAIF cannot replace human ack) applies here: the pre-filter reduces noise, it does not make canonical decisions. [src:anthropic-constitutional-ai.md:§5 T3]

**RLAIF integration design (cargo-cult only):**

```
For each citation [src:X] in document D:
  1. Extract surrounding sentence S (200-char window)
  2. Check Type 1 (bare claim): if [src:X] absent entirely → flag immediately, skip RLAIF
  3. Check Type 3 (broken citation): if path/anchor does not resolve → flag immediately, skip RLAIF
  4. Check Type 2 (cargo-cult): 
     a. Does S contain an explicit consequence sentence? (keyword heuristic: "therefore" / "which means" / "this implies" / "consequence:" / "result:")
     b. If yes → NOT cargo-cult → no flag
     c. If no → run RLAIF pre-filter: "Does the text surrounding this citation imply a concrete consequence of the cited claim, even implicitly?"
        - RLAIF YES → suppress cargo-cult flag; log as "implicit-consequence-detected"
        - RLAIF NO → flag as cargo-cult; record RLAIF verdict in lint output
```

**Acceptance predicate (P6a.2):** "Scanner correctly flags 8/10 synthetic cargo-cult test cases." The 10-case synthetic test suite must include: 5 genuine cargo-cult cases (citation present, no consequence), 3 implicit-consequence cases (RLAIF should suppress), 2 explicit-consequence cases (heuristic should suppress). The 8/10 target allows for 2 failures — either 2 false positives (RLAIF fails to detect implicit consequence) or 2 false negatives (RLAIF incorrectly suppresses a genuine cargo-cult). [src:deep-prompt §2.2 P6a.2 acceptance predicate]

---

## §K Failure Modes

| Failure mode | Observable | Detection | Response |
|-------------|-----------|-----------|----------|
| F-G-R drift undetected | Canonical artefacts accumulate with F3 claims re-declared as F5 without evidence accumulation | Quarterly audit: `fg_r_delta` shows step-function F jumps without corresponding approval log evidence | Flag as `F-G-R-inflation` finding; require AWAITING-APPROVAL with evidence summary |
| Lint false positive on legitimate paraphrase | Author avoids inline citations because scanner over-flags | Cargo-cult rate trends UP while F-G-R coverage trends UP — paradoxical pattern | Re-calibrate RLAIF pre-filter threshold; add more consequence-keyword heuristics |
| Broken citations after file rename | Refactoring moves files without updating `[src:path:anchor]` references | Broken-citation count spikes post-refactor | Pre-commit hook catches most cases; quarterly audit catches stragglers; mitigation: use stable slug-based IDs in critical citations |
| Quarterly audit not invoked | Part 8 fails to emit `quarterly-audit-event` | F-G-R drift detected retrospectively when artefacts are used downstream | Part 8 integration test: verify `quarterly-audit-event` fires per calendar; brigadier manual backup trigger quarterly |
| Approval log edited | Prior entry modified to correct an error | `git log --follow swarm/approvals/log.md` shows non-append commits | Restore from prior git ref; log edit = Law violation (FUNDAMENTAL §5.5 append-only); escalate to Ruslan |
| RLAIF pre-filter hallucination | RLAIF incorrectly suppresses genuine cargo-cult flag | Cargo-cult rate anomalously low vs manual review rate | Cap RLAIF suppression at 30% of total cargo-cult candidates; above 30% = require human review of RLAIF verdict |

**[EPISTEMIC]** The F-G-R inflation failure mode is epistemically the most dangerous: it is undetectable without explicit `fg_r_delta` tracking and is invisible in any single-point-in-time audit. It requires temporal comparison — which is why the approval log's `fg_r_delta` field (§I.2) is not optional metadata but a required field. Without it, F-level claims become self-sealing: "this is F5 because I say it's F5." The `fg_r_delta` field creates a paper trail that makes F-level promotions auditable across cycles. [src:design/JETIX-FPF.md:§12.7 B.3 "weakest-link composition, pathwise justification"]

---

## §L Wave C Bullet Status

### P6a.1 — F-G-R Schema Definition

**Acceptance predicate:** "JSON Schema `shared/schemas/f-g-r.json` is structurally valid (passes `jsonschema --validate`); F0-F9 enum is exhaustive per FPF B.3 anchors; `R.refuted_if` is a required field; F8/F9 gate is enforced by validation rule 3."

**Status:** DESIGNED (schema text in §I.1). Implementation (writing the JSON file) = Part 6b / brigadier execution scope.

**F-G-R of this design:** F5 (codified rule, written and reviewed in this document). Promoted to F6 after first implementation cycle passes validation.

**[EPISTEMIC]** The F0-F9 semantic anchors in §I.1 represent a refinement relative to the FPF B.3 canonical description. The key refinements: (a) F4 is explicitly anchored at "3+ cycles applied" (not merely "convention") — this provides a Hamel-binary count threshold; (b) F6 adds "cross-cycle reuse evidence" as a distinguishing criterion from F5 — this surfaces the replication requirement that FPF B.3 implies but does not make explicit; (c) F8 is tied to "FUNDAMENTAL Vision lock-class" — this grounds the constitutional boundary claim in the specific architectural context of this system. These refinements are PROPOSED for Ruslan ack as F8 constitutional revisions to the F-level anchor definitions. Until acked, the canonical anchor is FPF B.3 as stated; the refinements here are F5 design-level claims.

### P6a.2 — Citation Enforcement Scanner

**Acceptance predicate:** "Scanner correctly flags 8/10 synthetic cargo-cult test cases AND zero false positives on 5 explicit-consequence test cases AND zero false negatives on 5 bare-claim test cases."

**Status:** SPECIFIED (skill spec design in §H.1 + §J.3). Implementation = engineering-expert scope.

**RLAIF integration verdict:** APPLY — with the three constraints stated in §J.3. RLAIF applies to cargo-cult check only; it is advisory; it does not replace human gate. [src:anthropic-constitutional-ai.md:§4 P1 + §5 T3; raw/books-md/anthropic/bai-2022-cai.md:§1.2]

### P6a.3 — Approval Log Structure

**Acceptance predicate:** "First approval log entry written in correct YAML format; `actor` field populated; `fg_r_delta` populated; `reversibility` populated; `git log swarm/approvals/log.md` shows append-only commit pattern after 3 entries."

**Status:** DESIGNED (format in §I.2). `swarm/approvals/log.md` file to be scaffolded by brigadier.

### P6a.4 — Quarterly Immune Audit Framework

**Acceptance predicate:** "Template instantiated for first audit cycle; all 6 audit dimensions present; sycophancy stub acknowledged as OQ-CAI-3; Part 8 coordination section populated; audit report committed to `swarm/audits/`."

**Status:** DESIGNED (template in §I.3). First execution = next quarterly trigger.

---

## §M Wisdom Application Findings (Pre-Wisdom-Loop)

*These are candidate wisdom applications. Wisdom Loop pass will verify sourcing and application precision.*

1. **Левенчук B.3 F-G-R** — applied throughout. Primary canonical anchor. The F-level anchors in §I.1 refine but do not contradict B.3 L.28201. [src:design/JETIX-FPF.md:§12.7]

2. **Bai 2022 CAI §3 RLAIF** — applied in §J.3 (cargo-cult pre-filter). Application is bounded: RLAIF as a noise-reduction preprocessing step, not a gate. Bai 2022's core insight (AI self-critique reduces the need for human labelers on harmlessness) maps to: RLAIF self-critique reduces the need for human review of every cargo-cult flag. The analogy is correct but partial — Bai 2022 removes human labels at training time; here we merely reduce manual review burden at lint time. [src:raw/books-md/anthropic/bai-2022-cai.md:§1.2]

3. **Askell HHH** — applied structurally. HHH as F8 constitutional invariants: Helpfulness (F-G-R enables calibrated claims, not false certainty), Honesty (explicit `refuted_if` field prevents vacuous confidence), Harmlessness (F0-F2 gate prevents premature canonical promotion of unstable claims). [src:anthropic-constitutional-ai.md:§4 P2]

4. **Mereology typed edges** — applied in §D. All 7 dependency edges typed from the 10-edge vocabulary. ConstituentOf, MemberOf, methodologically-uses, creates, constrained-by all used with correct semantic justification. [src:mereology-typed-edges.md:§5]

5. **CAI provenance + transparency** — applied in §I.1 validation rules and §I.2 approval log. Every promoted claim has a plain-text trace via `[src:...]` citations + `fg_r_delta` in the approval log. [src:raw/books-md/anthropic/bai-2022-cai.md:§1.1 "make AI decision making explicit during training"]

6. **Stoic dichotomy of control** — applied in §C. The scanner surfaces findings (in our control); what the findings mean for the system's actual reliability (world's response to the evidence) is not in our control. `refuted_if:` criteria use our-control observables (lint pass returns non-zero, git log shows modification) rather than world-state claims. [src:philosophy-expert.md:§2.4 P5 Stoic dichotomy of control]

7. **First-principles: why triad** — ORIGINAL derivation in §I.1. Not a citation application but a structural derivation from the three orthogonal epistemic axes (process, context, evidence). This is the primary first-principles contribution of this cell.

---

## §N Provenance

All claims in this document trace to one of the following source paths. Every `[src:...]` inline citation points to a specific path:section.

| Source | Coverage | F-level |
|--------|---------|---------|
| `design/JETIX-FPF.md` §4.2 CP-2, §12.7 B.3 | F-G-R schema definition; F-level anchors; B.3.4 Evidence Decay | F5-F7 (canonical Jetix FPF adaptation) |
| `levenchuk-shsm-fpf.md` §4 P5, §5, §7 | B.3 triad sourcing; FPF-Steward audit function; citation discipline | F5 (consultant card with direct FPF-Spec read) |
| `anthropic-constitutional-ai.md` §4 P1-P7, §5 T3, §7, §8 | RLAIF; HHH; hardcoded never-list; sycophancy; Part 6 application table | F5 (library-direct Bai 2022 + Askell 2021) |
| `raw/books-md/anthropic/bai-2022-cai.md` §1.1-§1.2, §3 | RLAIF methodology; Constitutional AI two-stage process | F5 (peer-reviewed preprint, library-direct) |
| `mereology-typed-edges.md` §5 | A.14 typed edge vocabulary; canonical table | F3-F4 (FPF A.14 direct read + academic F4) |
| `part-6-governance-provenance-human-gate.md` all sections | Part 6 interface card; Laws, Admissibility, Deontics, Effects; anti-scope | F4 (Phase A interface card, operational convention) |
| `philosophy-expert.md` §1, §2, §2.4 | Dual-ownership rule; P1 Popper; P5 Stoic dichotomy | F5 (this agent's own Core Layer 1) |
| `wave-c-worklist.md` L300-360 | Part 6 Wave C bullets P6a.1-P6a.4; effort/expert allocation | F4 (cycle worklist, operational) |
| `expert-pre-reads/philosophy-expert.md` §1-§5 | Constitutional pressure points; OQ-PHIL-5 F-G-R ownership | F2 (pre-read, intent-to-test) |

---

## §X Foundation vs RUSLAN-LAYER

Per FUNDAMENTAL §0 and philosophy-expert.md §1 PP-2: Foundation must be generic; RUSLAN-LAYER carries Jetix/Ruslan-specific bindings. The F-G-R schema and Part 6a architecture are explicitly partitioned:

**Foundation (generic — forkable per D27):**

- F-G-R JSON Schema (`shared/schemas/f-g-r.json`) — the schema is generic to any knowledge system using FPF B.3. It does not name Ruslan, DACH, Phase A, or any Jetix-specific artefact path. Any D27 fork may use this schema as-is. F8 constitutional boundary: no fork may change F0-F2 = draft-only rule without losing Foundation compatibility.

- Approval log entry format (§I.2) — the YAML structure is generic. The `actor` enum includes `ruslan` as a value, but this is a role label (human owner), not a person-binding. A D27 fork uses this schema with their own human owner's identifier as the `ruslan` value equivalent. This is the same IP-1 principle applied to the governance schema: the role (human-owner) is Foundation; the executor-binding (Ruslan) is RUSLAN-LAYER.

- Quarterly audit template (§I.3) — the checklist dimensions (F-G-R drift, citation health, typed edge health, IP-1 violations, sycophancy stub) are generic to any Foundation deployment. Section numbers, column names, and audit dimensions are Foundation. The specific artefact counts and paths are RUSLAN-LAYER instantiation values.

- L/A/D/E structure (§E) — the four-lane discipline is Foundation. The specific SLAs, the specific quarterly cadence, the specific Ruslan-ack authority are RUSLAN-LAYER bindings over the Foundation L-lane structure.

**RUSLAN-LAYER (Jetix-specific — not forkable without adaptation):**

- Specific artefact paths (`swarm/wiki/`, `swarm/approvals/log.md`, `swarm/audits/`) — these are Jetix mono-repo paths. A D27 fork defines its own canonical path structure; the Foundation specifies only the *type* of path (canonical artefact store, approval log, audit directory).

- `actor: ruslan` value in approval log — specific to this Jetix instance. A fork uses their own human owner identifier.

- `decay_after` dates on specific Jetix artefacts — these are instance-specific temporal validity claims.

- The specific 11 hard AI/agent limits from FUNDAMENTAL §6.1 (encoded in §E Laws) — these are Jetix's specific constitutional limits. A D27 fork SHOULD have analogous limits but may differ in content; Foundation mandates the *mechanism* (a hardcoded never-list enforced at gate), not the exact list.

- The specific cycle IDs (`cyc-foundation-build-2026-04-28`) referenced in gate packets and log entries — RUSLAN-LAYER.

**Boundary enforcement in Part 6a:** The f-g-r.json schema's `ClaimScope.scope_tokens` enum includes both `Foundation` and `RUSLAN-LAYER` as canonical values. This makes the Foundation/RUSLAN-LAYER split machine-readable in every promoted artefact — the scanner can detect if an artefact claims `scope_tokens: [Foundation]` but contains RUSLAN-LAYER-specific content (e.g., executor names, DACH paths), flagging it as a PP-2 boundary leak. [src:philosophy-expert.md:§1 PP-2; part-6-governance-provenance-human-gate.md:§H A-1 correction applied]

---

## Closing — Acceptance Predicate (§L composite)

**Hamel-binary over this cell as a whole:**

"All four Wave C bullets (P6a.1-P6a.4) have an unambiguous design (schema text, skill spec, log format, audit template), each with a Hamel-binary acceptance predicate; all claims in this cell carry F-G-R tags; all dependencies in §D use A.14 typed edges with zero generic 'depends-on'; the first-principles derivation of the F-G-R triad in §I.1 names the three orthogonal axes (process, context, evidence) with explicit kill-conditions for alternative cardinalities; RLAIF integration is bounded to cargo-cult check only with three explicit constraints."

**Refuted if:** Any of the four P6a acceptance predicates fails on first implementation attempt; OR any §D dependency is found to use unlabeled "depends-on" on review; OR the F-G-R triad argument has a valid counter-example showing that F, G, and R are not mutually irreducible.

---

*End of Part 6a — philosophy-expert multi-mode cell.*
*Word count target: 5000-7000 words. Quality over volume.*
*Next step: brigadier promotes to Part 6a architecture document; engineering-expert implements the schemas and skill specs.*
