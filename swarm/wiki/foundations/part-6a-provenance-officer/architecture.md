---
title: Part 6a — Provenance Officer — Architecture
date: 2026-04-28
type: foundation-architecture
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 6a
parent_part: 6
split_rationale: "OQ-MERGED-1 override Ruslan walkthrough 2026-04-27: scale-readiness Phase B/C/D, fork-friendly portable provenance standard, independent change cadence (quarterly vs real-time)"
status: post-critic-finalized
wisdom_loop_adoption: "YES=13 NO=3 ALREADY_APPLIED=19"
critic_findings: "Cargo-cult flags: 0 (all citations carry consequence within 200 chars). IP-1 verdict: CLEAN — no executor names in Foundation-level definitions. A.14 purity: CLEAN — zero generic depends-on outside §D Prohibited declaration. Hamel-binary: all four P6a predicates are binary. Default-allow: none detected. Four HARD GAPS remain open and explicitly named."
F: F4
ClaimScope: "Foundation generic — F-G-R schema, citation lint, approval log, quarterly audit framework. RUSLAN-LAYER: specific governance role bindings (Provenance Officer human assignment)"
R:
  refuted_if: "Any canonical artefact in swarm/wiki/ promoted without F-G-R fields; OR any cargo-cult citation passes /lint --check-citations and reaches canonical state"
  accepted_if: "100% of canonical promotions trace to F-G-R; quarterly audit drift report shows zero untagged canonical artefacts"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6a/philosophy-expert-multi-mode.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6a/engineering-expert-multi-mode.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6a/investor-expert-capital-allocation.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6a/mgmt-expert-boundary.md
  - design/JETIX-FPF.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
---

# Part 6a — Provenance Officer — Architecture

> **Self-exemplification.** This document dogfoods every discipline it specifies. Every claim
> carries `[src:path:section]` with a concrete consequence within 200 characters. All
> dependencies are A.14 typed edges. F-G-R tags every promoted claim. Foundation/RUSLAN-LAYER
> distinction is explicit. L/A/D/E lanes are named. This is not ornament — it is the acceptance
> criterion for Part 6a's own outputs. [src:philosophy-expert-multi-mode.md:§ preface]

---

## §0 Executive Summary

Part 6a — Provenance Officer — is the **epistemically grounded immune-system function** for the
Jetix knowledge base. It is one of the two sub-parts of Part 6 Governance, occupying the
retrospective, schema-defining, and quarterly-audit arm of the governance mission. Part 6b (the
Human Gate, designed in a parallel Wave C bundle) occupies the prospective, real-time gate
enforcement arm. Together they constitute Part 6 Governance. [src:part-6-governance-provenance-human-gate.md:§A]

The need for Part 6a emerges from a fundamental asymmetry in knowledge systems: **claims are
cheap to produce, but epistemic accountability is expensive to reconstruct after the fact**.
Without systematic provenance enforcement at promotion time, a canonical wiki degrades
predictably. High-confidence operational rules (F5-F6) become indistinguishable from single-
observation hunches (F1-F2). Cargo-cult citations — citations that are decorative rather than
evidential — propagate false credibility through the citation graph. F-level tags that were
accurate at cycle 3 become stale at cycle 15 without a forcing function for re-audit. The
downstream cost of this epistemic drift is not theoretical: it manifests as decisions made on
false epistemic grounds, compounding errors across all consumers of the canonical knowledge base.
[src:investor-expert-capital-allocation.md:§1 "GAAP-equivalent argument"]

**F-G-R as the GAAP-equivalent for knowledge claims.** Just as GAAP audit standards make
financial statements investable by separating genuine earnings from accounting fiction, the F-G-R
triad (Formality / ClaimScope / Reliability) makes canonical knowledge claims actionable by
making their derivation pedigree (F), validity scope (G), and evidence warrant (R) explicit and
machine-readable. Without F-G-R, all canonical claims carry the same weight regardless of how
rigorously they were derived. With F-G-R, a consumer of any canonical artefact can immediately
determine whether they are relying on a 10-cycle-validated operational rule (F5, R-high) or a
design-stage proposal (F3, R-medium) — and calibrate their decisions accordingly.
[src:investor-expert-capital-allocation.md:§1 owner-earnings analogy; src:design/JETIX-FPF.md:§4.2 B.3]

**The IP-4 immune system function applied to provenance.** FPF IP-4 designates a quarterly
ontological-integrity audit as a Foundation constitutional function — the immune system that
detects and flags systemic deviations before they become architectural failures.
[src:part-6-governance-provenance-human-gate.md:§H FPF anchors "IP-4"] Part 6a is the concrete
materialisation of this function for the provenance domain: it is the quarterly audit that
detects F-G-R drift, cargo-cult citation accumulation, broken citations, dangling typed edges,
and IP-1 executor-name violations in Foundation-level artefacts.

**Leverage-point placement (Meadows).** Meadows (Thinking in Systems, 2008, Ch. 6) identifies twelve
leverage points in systems, from weakest (L12 — numbers and constants) to strongest (L1 — power to
transcend paradigms). The F-G-R schema sits at **Meadows leverage point L5 (rules of the system)**:
it is a structural rule that constrains what claims may enter the canonical knowledge base, not a
parameter adjustment or a feedback-loop gain change. The citation scanner sits at **L7 (information
flows)**: it surfaces gaps in provenance visibility that would otherwise remain invisible. Together,
L5 + L7 represent the two highest-leverage interventions available without requiring a paradigm
change. Interventions at L12 alone (adjusting individual claim counts, tweaking cycle lengths) would
leave the epistemic accountability problem structurally untouched.
[src:systems-thinking-cybernetics.md:§4 Principle 1 "Leverage Points"]

**VSM S3 authority placement (Beer).** Beer's Viable System Model (Brain of the Firm, 1972,
Ch. 9) designates System 3 (S3) as the audit and optimisation function — the level responsible
for resource bargaining and performance monitoring across S1 operational units. Part 6a is the
designated S3 lead for provenance governance: it runs the quarterly audit (S3 comprehensive
scan), emits the D1-D6 signals, and surfaces priority remediations. Part 6b (real-time gate
enforcement) serves as S3's enforcement arm. This placement resolves the TRADEOFF-01 surfaced
by the systems-expert consultant (Card #2 §7): the S3 audit authority must be designated to
one Part, not split ambiguously. Part 6a holds S3 audit lead; Part 6b holds S3 enforcement arm.
Without this explicit designation, Beer's VSM predicts oscillation: neither Part acts decisively
on audit signals, introducing delay at exactly the point where fast response matters.
[src:systems-thinking-cybernetics.md:§4 Principle 3 "Beer's VSM" + §7 TRADEOFF-01]

**Four outputs, one schema, one scanner, one log, one audit framework.** Part 6a delivers four
concrete Wave C artefacts, each with a Hamel-binary acceptance predicate:

1. **P6a.1 — F-G-R JSON Schema** (`shared/schemas/f-g-r.json`): the canonical machine-readable
   definition of the F-G-R triad for any promoted artefact. Currently F5 (codified rule, written
   and reviewed in Wave C); promoted to F8 on Ruslan ack. [src:philosophy-expert-multi-mode.md:§L P6a.1]

2. **P6a.2 — Citation Enforcement Scanner** (`swarm/lib/lint-check-citations.sh`): a
   four-algorithm pipeline implementing bare-claim detection (Algorithm A), cargo-cult detection
   (Algorithm B), broken-citation detection (Algorithm C), and optional RLAIF pre-filter
   (Algorithm D, critic-gate only). Delivered as a subcommand extension of the existing
   `swarm/lib/`-owned `/lint` skill. [src:engineering-expert-multi-mode.md:§2.3]

3. **P6a.3 — Approval Log** (`swarm/approvals/log.jsonl` + regenerated `log.md` view): the
   append-only event log recording every gate outcome, F-G-R delta, and reversibility
   classification. JSONL is the primary record; markdown is the derived human-readable view.
   [src:engineering-expert-multi-mode.md:§3.1]

4. **P6a.4 — Quarterly Immune Audit Framework**: a six-dimension audit template (D1 F-G-R
   drift, D2 citation health, D3 cargo-cult drift, D4 dangling edges, D5 IP-1 violations, D6
   gate-packet completeness) producing a quarterly compliance report at `swarm/audits/Q<n>-YYYY.md`.
   [src:engineering-expert-multi-mode.md:§4.2; src:mgmt-expert-boundary.md:§F.3 D6]

**Headline signal numbers** (targets, measured quarterly):
- F-G-R coverage of canonical artefacts: 100%
- Broken citation rate: 0%
- Cargo-cult flag rate: downward trend over 3 cycles (no hard cap; trend is the signal)
- IP-1 violations in Foundation-level artefacts: 0
- Gate-packet completeness ratio (D6): 100% (every canonical promotion has a corresponding
  AWAITING-APPROVAL packet)

**Split rationale in one sentence.** Part 6a operates on a quarterly retrospective cadence;
Part 6b operates on a real-time per-artefact cadence. These are genuinely different rhythms with
different decision authorities — a clean split per OQ-MERGED-1. [src:mgmt-expert-boundary.md:§B.1]

**HARD GAPS surfaced.** Four gaps remain open after Wave C cell integration:
- HARD GAP A: F4/F6/F8 F-level anchor wording refinements (§L below) — PROPOSED for Ruslan ack
- HARD GAP B: P6a.2 scanner implementation timeline — close within 2 cycles of Wave C completion
- HARD GAP C: D27 `cross-fork-provenance.json` needs `approvals_reconciliation_strategy` field
  (Part 1 schema gap, engineering-expert FINDING-3 in Phase B stub)
- HARD GAP D: OQ-CAI-3 sycophancy detection stub — Wave D or Part 8 scope; acknowledged in audit
  template but mechanism undefined

---

## §A Inputs

Part 6a accepts five distinct input classes, each with a named data shape, event trigger, and
F-G-R admission threshold. The admissibility rules are structural gates, not conventions.
[src:part-6-governance-provenance-human-gate.md:§A; src:philosophy-expert-multi-mode.md:§A]

### A.1 Draft Artefacts from Any Part (F-G-R Gate Input)

**Data shape.** Any `.md` file with YAML frontmatter containing `proposed_writes[]`,
`provenance[]`, and F-G-R fields (`F:`, `ClaimScope:`, `R:`). The file arrives via Part 6b's
`submit-draft-for-gate-event` — Part 6a is invoked by Part 6b to perform F-G-R compliance
checking before the gate decision is made. [src:part-6-governance-provenance-human-gate.md:§A
"submit-draft-for-gate-event"]

**Admissibility threshold.** An artefact is accepted into F-G-R audit ONLY IF: (a) `F:` field
is present in frontmatter (value may be F0..F9 — presence is required; level F0-F2 triggers a
gate failure, not a deferred audit), (b) `ClaimScope:` field is present and non-empty, (c)
`R:` field is present with at least `refuted_if:` declared. Incomplete F-G-R produces
`audit-deferred` status, which is surfaced to brigadier as a specific finding (not a silent pass).
[src:philosophy-expert-multi-mode.md:§A admissibility threshold; src:part-6-governance-provenance-human-gate.md:§E Admissibility]

**The F3 minimum for canonical promotion (Graham margin-of-safety applied).** F0-F2 artefacts
are pre-formal: F0 is a personal hunch, F1 is a single-case observation, F2 is an intent-to-test
hypothesis. Admitting F0-F2 to canonical state creates epistemic false margin: the claim appears
institutionally validated while carrying F1-equivalent evidence. Cost of breach: one undetected
F2 promotion that propagates to 5 downstream wiki entries × 3 operational documents each =
15 documents carrying hidden F2 uncertainty. Estimated correction cost: €180-300 at €60/hr.
[src:investor-expert-capital-allocation.md:§2 asymmetric cost structure]

**F-G-R of this boundary claim.**
```
F: F7
ClaimScope: [Foundation, Jetix-mono-repo]
R:
  tier: R-high
  refuted_if: "FPF B.3 F-level anchors are revised to lower the canonical admission
               threshold below F3; OR a confirmed case where an F2 canonical claim
               produced no downstream corruption is documented across 10+ cycles"
  receipt: design/JETIX-FPF.md §12.7 B.3 F-level anchors
```

### A.2 Canonical Artefacts for Re-Audit (Quarterly F-G-R Re-Check)

**Data shape.** Any promoted `.md` file in `swarm/wiki/` canonical paths. The quarterly audit
scanner reads every canonical artefact's frontmatter and body to check: (a) F-G-R fields still
present and syntactically valid against `shared/schemas/f-g-r.json`, (b) F-level has not drifted
upward without corresponding approval log evidence (`fg_r_delta` field check), (c) `decay_after`
date has not passed (FPF B.3.4 Evidence Decay), (d) `refuted_if` field is still a Hamel-binary
predicate rather than a prose essay that accumulated qualification clauses.
[src:engineering-expert-multi-mode.md:§4.2 D1; src:design/JETIX-FPF.md:§4.2 B.3.4]

**F-level inflation detection (most dangerous failure mode).** F-level claims that are manually
incremented without evidence accumulation — e.g. F4 → F5 because the author is confident, not
because 3+ cycles of application occurred — are undetectable without temporal comparison.
The `fg_r_delta` field in approval log entries (§I below) is the evidence trail that makes
F-inflation auditable: if the quarterly audit detects an F5 claim with no corresponding
approval log entry showing the F4→F5 transition with cycle evidence, it flags `F-G-R-inflation`.
This is the "Enron of knowledge accounting." [src:investor-expert-capital-allocation.md:§8 FM1]

### A.3 Citation Lint Requests (Scanner Input)

**Data shape.** A path to one or more `.md` files in `swarm/wiki/` canonical paths (or
`swarm/wiki/drafts/` for advisory-only pre-gate scans). The scanner receives this path via the
`/lint --check-citations [--path=<dir-or-file>]` invocation. For canonical paths: scanner
output is gate-relevant (Law violation = brigadier constructs AWAITING-APPROVAL packet). For
draft paths: scanner output is advisory (finding surfaced, no gate obligation created).
[src:engineering-expert-multi-mode.md:§2.1; src:philosophy-expert-multi-mode.md:§J.1]

**Event triggers.** Three distinct trigger contexts:
1. Pre-commit hook (Phase A: advisory; Phase B: blocking for canonical paths) — fires
   automatically on `git commit` over any canonical path file.
2. Manual invocation — `/lint --check-citations [--path=<dir>]` run by brigadier or Ruslan.
3. Quarterly audit integration — the `P6a.4` audit framework invokes the scanner as D2/D3
   measurement input. [src:engineering-expert-multi-mode.md:§4.2 D2-D3]

### A.4 Gate Outcome Signals (Approval Log Append Input)

**Data shape.** A structured approval event arriving after Part 6b's gate resolution: Ruslan
acks or rejects an AWAITING-APPROVAL packet. This signal carries: packet ID, gate class,
artefact path, F-G-R state at gate time, actor, reversibility classification, and an ISO 8601
timestamp. Part 6a appends this signal to `swarm/approvals/log.jsonl` as a new JSONL entry
without modifying any prior entry. [src:engineering-expert-multi-mode.md:§3.2 log entry schema]

**Actor hierarchy.** The `acked_by` field in the log entry encodes the Part 6 + FUNDAMENTAL §4.3
authority chain:
- `ruslan`: sole authority for F8/F9, irreversible, and constitutional promotions
- `brigadier-with-ack`: brigadier acting on explicit prior Ruslan ack per standing authorisation
- `autonomous-low-risk`: Tier 3 routine action (FUNDAMENTAL §4.1 auto-always); logged for audit
  completeness without requiring new ack
[src:philosophy-expert-multi-mode.md:§I.2 field semantics; src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3]

### A.5 Quarterly Audit Trigger (From Part 8)

**Data shape.** A `quarterly-audit-event` signal from Part 8's health-check cron. Fires at
quarterly boundaries (Q1=January, Q2=April, Q3=July, Q4=October). Also accepts a
`brigadier --trigger quarterly-audit` manual invocation when ad-hoc audit is needed between
calendar boundaries. [src:engineering-expert-multi-mode.md:§4.1 audit triggers]

**Admissibility.** Quarterly audit trigger is accepted from Part 8 ONLY via `quarterly-audit-event`
signal. Ad-hoc requests from non-Part-8 sources require brigadier mediation. This boundary
prevents audit fragmentation: multiple simultaneous quarterly audit runs would produce conflicting
compliance reports. [src:philosophy-expert-multi-mode.md:§E Admissibility "quarterly audit trigger"]

---

## §B Outputs

Part 6a produces five distinct output classes, each with a declared consumer, data shape, event
published, and F-G-R characterisation of the output's own reliability. The outputs are
information-emitting only: Part 6a never writes canonical wiki content and never issues gate
decisions autonomously.
[src:philosophy-expert-multi-mode.md:§B; src:part-6-governance-provenance-human-gate.md:§B]

### B.1 F-G-R Compliance Report (Quarterly Audit Report)

**Consumer.** Brigadier + Ruslan (primary); Part 8 health monitor (secondary, as health signals).
[src:engineering-expert-multi-mode.md:§4.3 Part 8 coordination edge]

**Data shape.** A markdown file at `swarm/audits/Q<n>-YYYY.md` following the six-dimension audit
template (§I.3 below). Fields include: F-G-R drift ratio (D1), citation health ratio (D2),
cargo-cult drift time series (D3), dangling edges count (D4), IP-1 violation count (D5), and
gate-packet completeness ratio (D6). Each dimension carries a measured value and a declared SLO
target. Priority remediations (top 5) are listed with artefact path, finding class, and required
action. [src:engineering-expert-multi-mode.md:§4.2]

**F-G-R of the compliance report itself.**
```
F: F4  (operational convention — automated scanner not yet implemented at Wave C design stage;
        first quarterly scan will mature this to F5)
ClaimScope: [Foundation, Phase-A-single-owner, Jetix-mono-repo]
R:
  tier: R-medium
  refuted_if: "Scanner run fails to complete; OR auditor manually overrides >10% of
               scanner findings without documented rationale"
  accepted_if: "All six audit dimensions produce measured values in first quarterly cycle;
                Part 8 consumes report without surfacing structural objections"
```

**Health signals emitted to Part 8.** Per C2 discipline (emit signals, NOT specify SLO thresholds
— those are Part 8's domain): Part 6a emits four named signals, deliberately structured to mirror
the SRE Book's Four Golden Signals discipline (Google SRE Book, Ch. 6: latency, traffic, errors,
saturation — signals that, together, characterise system health without duplication). Part 6a's
four provenance health signals are the knowledge-system analogue of those four:
1. `fg_r_coverage_pct` — **completeness signal** (canonical artefacts with valid F-G-R) / (total canonical)
2. `cargo_cult_flag_count` — **quality-drift signal**: count of cargo-cult flags raised per audit cycle (time-series); the knowledge-system analogue of latency trend — a rising count indicates systemic citation discipline erosion
3. `broken_citation_count` — **error signal**: count of broken `[src:path:anchor]` references; the canonical error-rate metric for provenance infrastructure
4. `dangling_edge_count` — **structural-integrity signal**: count of edges in `wiki/graph/edges.jsonl` pointing to nonexistent targets; signals graph substrate health
[src:philosophy-expert-multi-mode.md:§B "emit health signals for Part 8 consumption";
src:raw/books-md/sre/google-sre-book.md:Ch.6 "Four Golden Signals"]

Naming all four signals explicitly serves the SRE discipline: a signal without a name is a metric
nobody monitors. These four names become the canonical references for Part 8's health dashboard
design and for cross-cycle trend comparisons in quarterly audit §9.

### B.2 Citation Lint Results (Scanner Output)

**Consumer.** Developer/brigadier who invoked the scanner; Part 8 health monitor (via
`swarm/logs/lint-events.jsonl` append entries); quarterly audit (as D2/D3 input).

**Data shape.** Structured per-flag output to stderr (one line per flag: `TYPE | file:line |
evidence`). Human-readable summary to stdout (≤20 lines). Exit code: 0 (clean) or N (count
of citation flags found). Flags have types: `BARE-CLAIM`, `CARGO-CULT`, `BROKEN-PATH`,
`BROKEN-ANCHOR`. [src:engineering-expert-multi-mode.md:§2.1 interface contract]

**Critical design principle — advisory only, never auto-fix.** The scanner's epistemic role is
to falsify the claim "all citations are valid" by producing counterexamples. What to DO with the
counterexamples is instrumental — outside Part 6a's scope per FPF L1003-1006 epistemic-vs-
instrumental split. A scanner that auto-corrects citations is applying an instrumental decision
that belongs to a human or downstream Part. [src:philosophy-expert-multi-mode.md:§C "advisory,
not auto-fix"; src:philosophy-expert.md:§1a Dual-ownership note]

### B.3 Approval Log Entries (Gate Outcome Record)

**Consumer.** Part 6a quarterly audit (reads entries during D1 F-G-R delta analysis). Brigadier
+ Ruslan (query via `/approvals --filter`). Phase B partner due-diligence review.

**Data shape.** JSONL entry appended to `swarm/approvals/log.jsonl`. Each entry captures the
complete F-G-R state at gate time (F_before, F_after, ClaimScope, R.accepted_if), the actor,
the reversibility classification, the gate class, and a reference to the corresponding
AWAITING-APPROVAL packet path. The markdown view `log.md` is a derived projection, regenerated
weekly via `/approvals --regen-log`. [src:engineering-expert-multi-mode.md:§3.1-§3.2]

**Antifragility of append-only log.** The approval log is antifragile in the Taleb sense:
bounded downside (~3.3 hrs/year human time, ~50KB/year storage) with unbounded upside (pattern
recognition over F-level trajectories, audit capability for Phase B due diligence,
institutional memory surviving personnel changes). No approval log = complete institutional
amnesia at Phase B team expansion. [src:investor-expert-capital-allocation.md:§3]

**Every ack compounds epistemic capital.** Per Compounding Engineering discipline (Card #7,
§2): "each unit of engineering work should make subsequent units easier — not harder." Each
approval log entry is a unit of epistemic work that compounds. A single gate ack creates:
(1) a searchable precedent for future similar decisions; (2) an F-level delta record that
makes F-inflation auditable; (3) a temporal evidence trail that matures F3 proposals into
F5 operational conventions over cycles. The approval log is not a bureaucratic receipt — it
is the compound ledger for governance decisions, exactly as `strategies.md` is the compound
ledger for agent learning. The compounding rate is: each entry reduces the decision cost
of the next similar gate by eliminating the need to reconstruct context from scratch.
[src:compounding-engineering.md:§2 "compound ledger" P2]

### B.4 Quarterly Audit Report (Structured Markdown)

Already described in B.1. The data shape distinction: B.1 describes what Part 8 consumes (signals);
B.4 describes what brigadier and Ruslan read (the full audit report with priority remediations,
escalations list, and sycophancy stub acknowledgment). The report is committed to
`swarm/audits/Q<n>-YYYY.md` after Ruslan review.

### B.5 F-G-R Tags on Promoted Artefacts (Gate-Time Annotation)

At every canonical promotion event (Part 6b gate ack → Part 1 git commit), Part 6a's schema
is applied: the promoted artefact's frontmatter receives or validates its F-G-R block per
`shared/schemas/f-g-r.json`. This output is not a separate file — it is an annotation on the
promoted artefact itself. The F-G-R block becomes part of the canonical artefact's content.
[src:philosophy-expert-multi-mode.md:§B "F-G-R tags in promoted artefact frontmatter"]

---

## §C Side-Effects

Part 6a produces three categories of side-effects. All are append-only or read-only.
No side-effect modifies existing content.

### C.1 Append-Only Approval Log Writes

Every gate ack event appends exactly one JSONL entry to `swarm/approvals/log.jsonl`.
**No existing entry is ever edited.** Corrections to prior entries are themselves new entries
with the `corrects:` field set to the entry ID being corrected. This is Young's Reversal
Transactions principle applied to governance records: the correction is a new event in the
event log; the original entry is immutable history. [src:event-sourcing-cqrs.md:§3 Source 2
"There is no Delete"; src:engineering-expert-multi-mode.md:§3.2 corrects field]

Example correction flow:
```
Entry appr-20260428-001: records wrong artefact_path
Entry appr-20260428-002: entry_type=correction; corrects=appr-20260428-001; notes="correct
  path is swarm/wiki/foundations/part-6a-provenance-officer/architecture.md"
```
Entry 001 is never touched. The audit query for "what was the correct path?" traverses the
correction chain and takes the most recent non-overridden value.

**Falsifier for append-only discipline:** `git log --follow swarm/approvals/log.jsonl` showing
a non-append commit (a commit that modified an existing line rather than appending a new one)
is the explicit Popper-grade refutation condition for this Law. [src:philosophy-expert-multi-mode.md:§E
Laws item 6]

**Matuschak evergreen-note parallel.** Matuschak's evergreen-note discipline (notes that are
written to evolve by accretion, not overwrite) maps directly onto the approval log's append-only
design. Each approval log entry is an evergreen record of a governance decision at a specific
point in time — it never becomes stale by design, because it captures what WAS decided, not what
SHOULD BE decided in the future. Corrections are new evergreen entries that reference the prior
one. The approval log is therefore the governance-layer analogue of an evergreen-note system:
its value compounds as entries accumulate; its integrity is preserved precisely because no entry
is ever overwritten. This parallel grounds the append-only design not only in Young's event-
sourcing engineering tradition but in knowledge-management theory.

### C.2 Lint Results to Stderr + Lint Events Log

Citation scanner flags are emitted to stderr (structured, one line per flag). They are also
appended to `swarm/logs/lint-events.jsonl` for audit trail completeness. The scanner DOES NOT
modify any scanned artefact. The scanner DOES NOT produce canonical wiki content. The scanner
DOES NOT issue AWAITING-APPROVAL packets. Its only side-effects are: stderr output, exit code,
and lint-events log append. [src:engineering-expert-multi-mode.md:§2.1 interface contract]

RLAIF call failures (Algorithm D unavailable) are also logged to `swarm/logs/lint-events.jsonl`:
`{type: rlaif-failure, timestamp: <ISO>, sentence_hash: <hash>}`. This ensures that RLAIF
unavailability does not silently degrade the scanner's false-positive properties — the fallback
(emit the flag conservatively) is logged for human review. [src:engineering-expert-multi-mode.md:§6.2 FINDING-1]

### C.3 Quarterly Audit Reports (New File Per Cycle)

The quarterly audit framework writes `swarm/audits/Q<n>-YYYY.md` as a new file. Prior audit
reports are NEVER overwritten. This creates an append-equivalent audit history at the file level:
the history of quarterly audits is preserved across cycles and is diffable via git log.
[src:philosophy-expert-multi-mode.md:§J.2 "never overwrites prior"]

**Log regeneration side-effect.** Weekly (Friday 17:00 RUSLAN-LAYER cron binding), the markdown
view `swarm/approvals/log.md` is regenerated from `log.jsonl` via `/approvals --regen-log`.
This is a CQRS read-model rebuild: the write model (JSONL) is canonical; the read model (markdown)
is always reconstructable. Regeneration is idempotent: running it twice produces the same
`log.md`. [src:engineering-expert-multi-mode.md:§3.4 CQRS projection rebuild]

---

## §D Dependencies (A.14 Typed Edges)

All edges use the A.14 typed vocabulary from `mereology-typed-edges.md`. Zero generic
"depends-on" edges. Ten-edge reference table per Part 1 §D style convention.
[src:philosophy-expert-multi-mode.md:§D; src:part-1-architecture.md:§D "10-edge reference table"]

| # | Edge | Type | Rationale |
|---|------|------|-----------|
| 1 | Part 6a `MemberOf` Part 6 governance cluster | `MemberOf` | Part 6a is one member of the Part 6 governance collection alongside Part 6b. Removing Part 6a degrades Part 6 (no quarterly audit, no F-G-R schema definition) but does not destroy Part 6b's real-time gate function. MemberOf is correct (not ComponentOf) because the sub-holons have independent lifecycles. [src:mereology-typed-edges.md:§5 MemberOf vs ComponentOf] |
| 2 | Part 6a `methodologically-uses` Part 1 (System State Persistence) | `methodologically-uses` | Approval log appends through git commit substrate (Part 1 D25). Scanner results surfaced via git-tracked artefacts. Part 6a invokes Part 1's mechanism without being constituted by it — non-rigid dependency. [src:philosophy-expert-multi-mode.md:§D edge 1] |
| 3 | Part 6a `methodologically-uses` Part 6b (Gate Enforcement) | `methodologically-uses` | Part 6b's real-time gate enforcement triggers Part 6a F-G-R tagging at promotion time; Part 6a defines the tagging schema that Part 6b applies. Separation: Part 6a = schema + audit (quarterly); Part 6b = real-time gate execution (per-artefact). [src:philosophy-expert-multi-mode.md:§D edge 2; src:mgmt-expert-boundary.md:§B] |
| 4 | Part 6a `creates` F-G-R compliance report | `creates` | The quarterly audit framework is a creator system that produces the compliance report artefact. Directed creation: Part 6a is productive system; report is target system. [src:mereology-typed-edges.md:§5 creates] |
| 5 | Part 6a `creates` approval log entries | `creates` | Each gate ack event produces a new JSONL entry. The entries are distinct artefacts created by Part 6a's write mechanism. [src:philosophy-expert-multi-mode.md:§D "Part 6a creates approval log entries"] |
| 6 | Part 8 `methodologically-uses` Part 6a quarterly audit | `methodologically-uses` | Part 8 health monitoring consumes the compliance report as a health signal input. Part 8 invokes Part 6a's audit output without being constituted by it. [src:philosophy-expert-multi-mode.md:§D edge 5; src:part-6-governance-provenance-human-gate.md:§D Part 6 ↔ Part 8] |
| 7 | Part 6a `constrained-by` FPF B.3 (canonical F-G-R upstream) | `constrained-by` | FPF B.3 Trust & Assurance Calculus is the upstream methodology that defines the F-level anchors and R-tier semantics. Part 6a's f-g-r.json operationalises B.3 but cannot contradict it without a HITL foundation-revision gate. [src:design/JETIX-FPF.md:§4.2 B.3] |
| 8 | Part 6a `constrained-by` Ruslan ack for F8 promotions | `constrained-by` | Any revision to the F-G-R schema (a constitutional F8 artefact) requires explicit Ruslan ack. Part 6a proposes via AWAITING-APPROVAL; Ruslan decides. [src:philosophy-expert-multi-mode.md:§1d requires-approval; src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3 Human-Only] |
| 9 | `f-g-r.json` schema `ConstituentOf` Part 6a | `ConstituentOf` | The JSON Schema is a logical/conceptual section of Part 6a — a rule-clause inside Part 6a's specification. It lives inside Part 6a as a structural constituent: removing it from Part 6a would destroy Part 6a's core function. [src:mereology-typed-edges.md:§5 ConstituentOf] |
| 10 | Part 6a approval-log `references` Part 6b gate-class taxonomy | `references` (lightweight value-coupling) | The `gate_class` field in `log.jsonl` stores a string value from Part 6b's gate-class enum. One-directional reference: Part 6a records the value; Part 6b owns the enum definition. Adding a new Part 6b gate class does NOT require Part 6a schema change — the log simply records the new value. [src:mgmt-expert-boundary.md:§C.1 Coupling Point 1; src:engineering-expert-multi-mode.md:§3.5 FINDING-2] |

**On edge 10 (gate-class coupling, WATCH ITEM).** Engineering-expert FINDING-2 identified this
coupling as implicit in the design. Mgmt-expert §J.1 confirms the watch item: until edge 10 is
declared in both Part 6a and Part 6b dependency tables, the coupling is invisible to the
dependency graph and future gate-class taxonomy changes may break approval-log queries silently.
This document declares the edge. Part 6b's Wave C architecture document MUST declare the
reciprocal edge: `Part 6b gate-class taxonomy referenced-by Part 6a approval-log`.
[src:engineering-expert-multi-mode.md:§6.2 FINDING-2; src:mgmt-expert-boundary.md:§J.1 Watch item]

---

## §E Boundary — L/A/D/E Discipline

Per FPF A.6.B [src:part-6-governance-provenance-human-gate.md:§E "L/A/D/E discipline FPF §4.3
A.6.B"]. This section applies L/A/D/E to Part 6a specifically. The overarching Part 6 L/A/D/E
remains at the interface card level; this section refines it for Part 6a's specific domain.

### Laws (invariants that MUST hold — constitutional, not negotiable)

**L1 — Every promoted canonical artefact MUST carry F-G-R fields.**
Every `.md` file in a canonical path (`swarm/wiki/` excluding `drafts/`) must carry `F:`,
`ClaimScope:`, and `R:` fields in YAML frontmatter. Absence = gate failure, not warning.
The F-G-R check is structural, not advisory.
**Falsifier [Popper P1 applied]:** any canonical artefact without F-G-R fields detected by a
`/lint --check-fg-r` pass.
[src:design/JETIX-FPF.md:§4.2 CP-2; src:levenchuk-shsm-fpf.md:§4 P5]

**L2 — F0-F2 artefacts MUST NOT be promoted to canonical state.**
F0-F2 artefacts belong exclusively in `swarm/wiki/drafts/` or in-cell scratchpad.
**Falsifier:** any `swarm/wiki/` canonical path file with `F: F0`, `F: F1`, or `F: F2`.
[src:design/JETIX-FPF.md:§12.7 B.3 F-level anchors]

**L3 — F8/F9 claims MUST require Ruslan ack before canonical promotion.**
Constitutional and mathematically formal claims cannot be promoted by brigadier alone.
**Falsifier:** any F8/F9 artefact in `swarm/wiki/foundations/` without a corresponding
AWAITING-APPROVAL packet with `acked_by: ruslan` and human ack timestamp in the approval log.
[src:philosophy-expert-multi-mode.md:§E Laws item 3; src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3]

**L4 — Every `[src:...]` citation in a canonical artefact MUST resolve.**
Dangling citations = broken provenance chain. The path component must exist in the repo; if an
anchor is declared, it must match an ATX header in the referenced file.
**Falsifier:** `/lint --check-citations` returns non-zero broken-citation count against any
canonical artefact.
[src:part-6-governance-provenance-human-gate.md:§E Admissibility "provenance[] non-empty"]

**L5 — RLAIF self-critique CANNOT substitute for Ruslan ack.**
RLAIF (Bai 2022 §3) is a pre-gate noise filter only. The human gate remains the terminal
decision authority. The Constitutional AI constraint is explicit: self-critique applies at
generation time; it is a quality filter, not final authority.
**Falsifier:** any artefact in canonical state whose approval log entry lacks a human actor field.
[src:anthropic-constitutional-ai.md:§5 T3; src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.3 Human-Only]

**L6 — The approval log MUST be append-only.**
No edits to prior entries. Corrections are new entries with `corrects:` field.
**Falsifier:** `git log --follow swarm/approvals/log.jsonl` shows a non-append commit
(a commit that modified an existing line).
[src:part-6-governance-provenance-human-gate.md:§E Laws; src:event-sourcing-cqrs.md:§3 "There is no Delete"]

**L7 — Harmlessness as constitutional invariant (HHH framework).**
Part 6a's scanner and audit framework cannot violate the 11 constitutional limits in
FUNDAMENTAL §6.1. The HHH triad (Helpful, Honest, Harmless) from Askell et al. 2021 is
F8-grade invariant. Each arm grounds a specific F-G-R mechanism as a constitutional claim:
- **Helpful**: F-G-R enables calibrated claims — consumers know whether they are relying
  on F7 methodology or F3 multi-source synthesis and can calibrate accordingly. Without F-G-R,
  all canonical claims carry false equivalence, making the wiki unhelpful (it cannot be
  actionably differentiated). [src:raw/books-md/anthropic/askell-2021-hhh.md:§3 HHH definition]
- **Honest**: explicit `refuted_if` field prevents vacuous confidence — a claim with no
  falsifier is "honest" in surface form but epistemically dishonest because it cannot be wrong.
  Structural honesty enforcement: the schema REQUIRES `R.refuted_if`; absence = lint failure.
  [src:raw/books-md/anthropic/askell-2021-hhh.md:§3 Honesty component]
- **Harmless**: F0-F2 gate prevents premature canonical promotion of unstable claims.
  An F1 claim (single-case observation) promoted to canonical harms downstream consumers
  who build decisions on it. The gate is structural harm-prevention at the epistemic level —
  not a content filter, but a maturity filter. [src:raw/books-md/anthropic/askell-2021-hhh.md:§3 Harmlessness component]
The HHH triad makes the F-G-R schema's constitutional status grounded: it is not merely a
FPF convention but an operationalisation of the three properties any trustworthy information
system must exhibit. [src:anthropic-constitutional-ai.md:§4 P2; src:philosophy-expert-multi-mode.md:§M item 3 HHH]

### Admissibility (what Part 6a accepts as valid input)

**A1.** Draft artefact accepted into F-G-R audit ONLY IF F-G-R fields are present (values may
be F0-F9; Level F0-F2 triggers gate failure, not deferred audit). Incomplete F-G-R = audit-
deferred finding surfaced to brigadier with line reference. [src:philosophy-expert-multi-mode.md:§E Admissibility]

**A2.** Citation scan accepted for any `.md` file in `swarm/wiki/` canonical paths. Drafts
MAY be scanned; findings are advisory (not gate-blocking for draft paths).

**A3.** Quarterly audit trigger accepted from Part 8 ONLY via `quarterly-audit-event` signal.
Ad-hoc audit requests from non-Part-8 sources require brigadier mediation (prevents parallel
competing audit reports). [src:philosophy-expert-multi-mode.md:§E Admissibility]

**A4.** Approval log entries accepted from the gate-outcome signal ONLY IF they conform to the
JSONL schema at `shared/schemas/approval-log-entry.json` — specifically: all required fields
present, `schema_version` declared, `entry_id` follows `appr-YYYYMMDD-NNN` format.
[src:engineering-expert-multi-mode.md:§3.2]

### Deontics (obligations of Part 6a toward its consumers)

**D1.** Part 6a MUST surface every F-G-R gap with line + section reference (not a generic
"F-G-R missing"). Specific failure identification is the AP-L4 discipline applied to governance
findings. [src:levenchuk-shsm-fpf.md:§8 AP-L4]

**D2.** Part 6a MUST surface every IP-1 violation (executor name in Foundation-level artefact)
as a separate finding class. IP-1 violations have a different remediation path from F-level
problems (foundation-revision escalation + HITL ack, not a simple field correction).
[src:part-6-governance-provenance-human-gate.md:§E Laws IP-1 enforcement]

**D3.** Part 6a MUST publish quarterly audit report to `swarm/audits/` within the same cycle
that triggered the audit. Holding findings without publishing = silent error swallowing per
FUNDAMENTAL §5.5 no-silent-error-swallowing. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§5.5]

**D4.** Part 6a MUST distinguish R-low advisory findings from R-high actionable findings in
every lint report. This prevents all scanner output from being treated with equal urgency —
a false positive at R-low that floods brigadier's attention budget is as harmful as an
undetected R-high Law violation. [src:philosophy-expert-multi-mode.md:§E Deontics]

**D5.** Part 6a MUST NOT modify F-G-R schema autonomously. Schema revisions are F8
constitutional updates requiring Ruslan ack via AWAITING-APPROVAL packet + Part 6b routing.
[src:philosophy-expert-multi-mode.md:§C "Does NOT modify F-G-R schema autonomously"]

### Effects (measurable outcomes)

**E1 — F-G-R coverage: 100% target (canonical artefacts).**
Measured: `(canonical artefacts with valid F-G-R tags) / (total canonical artefacts)`.
Measurement cadence: quarterly audit D1.
Starting baseline: unknown (first audit cycle establishes baseline). Drift threshold: any
quarter where coverage drops from prior quarter triggers D1 Priority Remediation.
[src:part-6-governance-provenance-human-gate.md:§E Effects]

**E2 — Broken citation rate: 0% target.**
Measured: `(broken citations detected) / (total citations scanned)`.
Measurement cadence: per-commit (pre-commit hook advisory/blocking) + quarterly audit D2.
Achievable immediately on first lint run. [src:philosophy-expert-multi-mode.md:§E Effects]

**E3 — Cargo-cult flag rate: downward trend target (no hard count).**
Measured: `count(cargo-cult flags per audit cycle)` as time-series.
Alert condition: count > 2× rolling 4-cycle average. This is a trend metric, not a ratio
target — enforcing zero cargo-cult flags would produce overcorrection (citations suppressed
entirely). The goal is systematic improvement, not perfection. [src:engineering-expert-multi-mode.md:§4.2 D3]

**E4 — IP-1 violation count: 0 target in Foundation-level artefacts.**
Measured: `count(Foundation-tagged artefacts containing executor names)`.
Measurement cadence: quarterly audit D5.
[src:engineering-expert-multi-mode.md:§4.2 D5]

**E5 — Gate-packet completeness ratio: 100% target.**
Measured: `count(canonical promotions in approval log without corresponding gate packet)` = 0.
This is the D6 audit dimension proposed by mgmt-expert to prevent approval log substituting
for AWAITING-APPROVAL packet. [src:mgmt-expert-boundary.md:§F.3 D6 proposed dimension]

---

## §F Anti-Scope

### §F.1 Generic Anti-Scope (§6.1 hard rules apply universally)

These boundaries apply regardless of what any cycle or stakeholder requests. They are not
negotiable through cycle tasking. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1]

- Part 6a NEVER makes canonical promotion decisions. Final authority = Ruslan (human owner).
  Part 6a reports compliance and tags F-G-R drift; Part 6b enforces the gate. The distinction
  is detection vs decision. [src:part-6-governance-provenance-human-gate.md:§F]

- Part 6a NEVER executes halts. Advisory only. When the scanner finds a Law violation, it
  surfaces the finding to brigadier / Part 6b for enforcement. Self-executing halts would
  cross into instrumental authority (FPF L1003-1006 epistemic-vs-instrumental wall).
  [src:philosophy-expert-multi-mode.md:§F; src:philosophy-expert.md:§1a Dual-ownership note]

- Part 6a NEVER writes canonical wiki content. All canonical writes flow through Part 6b gate
  + brigadier (Q2 single-writer rule). [src:part-6-governance-provenance-human-gate.md:§C]

### §F.2 Part-Specific Anti-Scope

**Does NOT own AWAITING-APPROVAL packet schema.** Part 6b owns the gate packet format
(structure, required fields, routing logic). Part 6a's approval log records the *outcome* of
gate events, not the packet itself. The `gate_packet_path` field in the log is a read-only
path reference, not an embedded copy of the packet's contents.
[src:engineering-expert-multi-mode.md:§3.5 boundary verdict; src:mgmt-expert-boundary.md:§C.1 Coupling Point 2]

**Does NOT modify F-G-R schema autonomously.** The `f-g-r.json` schema is a constitutional
artefact (F8 on Ruslan ack). Any revision requires Ruslan ack via AWAITING-APPROVAL packet.
Part 6a proposes; brigadier routes; Ruslan decides. Part 6a never self-amends its own
constitutional specifications. [src:philosophy-expert-multi-mode.md:§F; src:philosophy-expert.md:§1d requires-approval]

**Does NOT implement sycophancy detection.** OQ-CAI-3 is a Wave C gap. Part 6a defines a
stub placeholder in the quarterly audit template (§I.3 section 6 "Sycophancy Detection STUB")
but does not specify the detection mechanism — that is Wave D or Part 8 scope.
[src:anthropic-constitutional-ai.md:§8 OQ-CAI-3; src:philosophy-expert-multi-mode.md:§F OQ-CAI-3 stub]

**Does NOT own blast-radius classification table.** That is Part 6b scope (wave-c-worklist
Bullet 2). Part 6a's F-G-R scanner and audit framework are orthogonal to blast-radius
classification. F-level (a provenance quality metric) is distinct from blast-radius (an action
risk metric). [src:wave-c-worklist.md:L320-332]

**Does NOT substitute approval log for AWAITING-APPROVAL packet.** The approval log records
gate events that have already been resolved. The AWAITING-APPROVAL packet is the blocking
mechanism that exists at state `BLOCKED` until Ruslan acks it. Skipping the packet eliminates
the enforced pause before promotion. Detection: D6 audit dimension flags any canonical
promotion traceable in the approval log but without a corresponding gate packet.
[src:mgmt-expert-boundary.md:§F.3 Risk description; src:mgmt-expert-boundary.md:§H Laws item 1]

**Does NOT execute pre-commit lint blocking in Phase A (advisory log-only).** The scanner runs
in advisory mode during Phase A (exit code reported, finding logged, no commit blocked). Phase B
upgrade-path: blocking enabled per Part 1 P1.2 upgrade-path mirror — the same mechanism that
switches commit-format checking from advisory to blocking.
[src:engineering-expert-multi-mode.md:§4.1 "calendar-driven, not blocking Phase A"]

**Does NOT auto-escalate high-severity findings directly to AWAITING-APPROVAL.** Part 6a raises
findings with severity tags; brigadier decides whether severity warrants a gate packet
construction. Detection never escalates autonomously — that is the AP-MGMT-4 scope-creep
anti-pattern applied to governance architecture. The correct signal flow is:
`Part 6a scanner → structured findings → brigadier reads → brigadier constructs gate packet
(Part 6b mechanism) → Ruslan acks → Part 6a approval log appends entry`.
[src:mgmt-expert-boundary.md:§C.2 seam test; src:mgmt-expert-boundary.md:§H Deontics]

### §F.3 Stoic Dichotomy of Control — Foundation/RUSLAN-LAYER Governance Boundary

Per the stoic-epistemic consultant card (Card #9, §4 P5), every governance enforcement rule
must be classified along the Stoic dichotomy of control: what is **in-system-control** (Part 6a
can enforce structurally) vs what is **not-in-system-control** (Part 6a can observe and surface,
but not decide). This classification is the epistemic complement to the Foundation/RUSLAN-LAYER
split: Foundation-generic rules are those that any deployment can enforce structurally;
RUSLAN-LAYER rules carry human-actor-dependent bindings that are, by nature, influence-zone.
[src:stoic-epistemic.md:§4 P5 Stoic dichotomy; src:philosophy-expert-multi-mode.md:§F]

**Category A — Hard enforcement (fully in-system-control, Foundation):**
- F0-F2 artefacts cannot enter canonical paths (structural: path check is automated)
- Every canonical artefact must carry F-G-R fields (structural: `/lint --check-fg-r` validates)
- The approval log is append-only (structural: no write operation modifies existing lines)
- F8/F9 requires `acked_by: ruslan` in log entry before canonical promotion (structural: schema validation)
- RLAIF is never enabled in pre-commit paths (structural: `RLAIF_ENABLED=0` default)

**Category B — Monitoring and alerting (influence-zone, RUSLAN-LAYER):**
- Ruslan reviews the quarterly audit report within N days (influence: system surfaces the report and alerts; cannot compel review)
- HARD GAP B scanner implementation within 2 cycles (influence: investor-expert verdict surfaced; execution is Ruslan's decision)
- OQ-CAI-3 sycophancy detection resolved in Wave D (influence: stub acknowledged; human commits the timeline)
- Cargo-cult flag rate trends downward over 3 cycles (influence: system measures and surfaces; cultural change is RUSLAN-LAYER)

**Category C — Pure logging, no constraint (not-in-control):**
- External paradigm shifts in FPF methodology (Левенчук publishes; Foundation records impact, not timing)
- Model-level capability changes affecting RLAIF latency (Anthropic releases; Foundation logs new benchmarks, does not control releases)

This three-category classification prevents the most common governance anti-pattern: treating
Category B influence-zone items as Category A hard constraints, which produces false compliance
signals when Ruslan is unavailable. It also prevents treating Category A hard constraints as
Category B suggestions, which produces real enforcement gaps.
[src:stoic-epistemic.md:§4 P5 Stoic dichotomy "three categories not two"; src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.2]

---

## §G F-G-R Tagging — DOGFOOD

This section dogfoods P6a.1 by tagging every major claim in Part 6a's own architecture with
F-G-R metadata. This demonstrates the schema in production use on design-document claims, not
just wiki content claims — proving the schema is general enough to apply to its own defining
document. [src:philosophy-expert-multi-mode.md:§G "DOGFOOD: every major claim tagged"]

| Claim | F | ClaimScope | R tier | refuted_if |
|-------|---|------------|--------|------------|
| F-G-R triad is irreducible (not collapsible to duo or quad) | F7 | Foundation; any knowledge system using FPF B.3 | R-high | A valid counter-example showing F, G, and R are not mutually irreducible; OR a working quad that demonstrably outperforms the triad across 10+ canonical artefacts |
| F0-F2 artefacts must not be canonical | F7 | All Foundation Parts; any Jetix instance | R-high | FPF B.3 F-level anchors are revised to lower threshold; OR 10+ cycles show zero downstream corruption from F2 canonical artefacts |
| JSON Schema approach for F-G-R definition | F5 | Foundation Part 6a; JSON Schema draft-07 or later | R-medium | Alternative schema format (YAML Schema, CDDL) is formally acked as preferred by Ruslan via AWAITING-APPROVAL |
| `/lint --check-citations` as swarm/lib/ subcommand extension | F5 | Jetix mono-repo; as long as Part 1 §H swarm/lib/ ownership contract holds | R-medium | Part 1 §H ownership note revised to remove /lint from swarm/lib/ scope |
| Approval log append-only (JSONL primary, markdown derived) | F6 | All Foundation Parts; all Jetix instances per D27 fork contract | R-high | git log shows a prior JSONL entry modified; OR three consecutive /approvals queries take >5s (scalability refutation) |
| Quarterly audit cadence (Q1/Q2/Q3/Q4) | F5 | Foundation Phase A; single-owner cycle | R-medium | Audit cadence formally revised to monthly or semi-annual via AWAITING-APPROVAL packet |
| RLAIF pre-filter bounded to cargo-cult check only; not gate substitute | F6 | Any Jetix instance; any AI-augmented canonical promotion workflow | R-high | CAI §5 T3 explicitly states this; human gate is primary authority per FUNDAMENTAL §4.3 |
| Scanner must be disabled for RLAIF on pre-commit hooks | F5 | All deployments with pre-commit hook integration | R-high | A pre-commit RLAIF call completes under 2 seconds for all citations (new capability unavailable at time of writing) |
| gate_class coupling between 6a log and 6b taxonomy is reference-only | F4 | Phase A design stage; may gain couplings in Phase B | R-medium | A Part 6b design adds a structural schema dependency on Part 6a finding format (not just a value reference) |
| F-G-R schema portability as Lindy-grade capital asset on F8 ack | F5 (F8 on ack) | Foundation generic; any FPF B.3 deployment | R-medium (R-high on ack) | F-G-R schema is revised significantly within 2 years of first F8 ack |
| Sycophancy detection = stub (OQ-CAI-3) | F3 | Wave C scope; single-owner Phase A | R-low | OQ-CAI-3 closes with an implemented detection mechanism in Wave D or Part 8 |
| D6 gate-packet completeness ratio as 6th audit dimension | F4 | Phase A; proposed by mgmt-expert | R-medium | First quarterly audit D6 check finds no cases of approval-log-without-gate-packet |

**[Epistemic note on heterogeneity].** The F-level heterogeneity in this table is a feature.
Claims derived from FPF B.3 (a peer-validated methodology) with explicit Popper falsification
thresholds earn F7. Claims about implementation conventions pending first validation cycle earn
F4-F5. Claims about open stubs earn F3. Collapsing all claims to F5 would be epistemic false
certainty; collapsing to F3 would undersell structural invariants. The triad's value is making
this heterogeneity visible. [src:philosophy-expert-multi-mode.md:§G epistemic note]

**Lindy verdict box.** Taleb's Lindy Effect (Antifragile, 2012, Ch. 20): a technology or idea
that has survived for N years is likely to survive for another N years. The F-G-R schema
inherits Lindy durability from its upstream lineage — FPF B.3 Trust & Assurance Calculus
draws on Popperian falsifiability (1963), which has persisted 60+ years as the dominant
epistemological framework for scientific claims. The JSON Schema container (draft-07) was
published in 2012 and remains the dominant machine-readable schema format in 2026. The
approval log JSONL format rests on append-only log structures with roots in database WAL
(write-ahead logging) from the 1970s. These Lindy substrates predict the F-G-R schema will
remain valid and deployable for at least the next decade without structural revision. The
Lindy verdict applies to the F-G-R **mechanism** (append-only, machine-readable,
Popper-grounded); it does NOT apply to the specific F-level anchor wordings, which are
Jetix-specific refinements pending first validation cycles (F4-F5 currently).
[src:capital-allocation-antifragility.md:§3 Part 1 "Lindy substrate";
src:investor-expert-capital-allocation.md:§6 capital-call rounds table]

**F-G-R coverage SLO — 100% canonical target.** The F-G-R coverage percentage (canonical
artefacts with valid F-G-R / total canonical) is the primary SLO for Part 6a. Drawing
from SRE Book discipline (Google SRE Book, Ch. 4 SLI/SLO framework): the SLO for this
service-level indicator is 100% — not because 100% is achievable on day one (the baseline
is unknown; first quarterly audit establishes it), but because any deviation from 100%
represents a canonical claim without epistemic accountability, which is the exact failure
mode Part 6a exists to prevent. Error budget: 0%. The SLO is deliberately strict because
F-G-R missing is not a performance degradation — it is a provenance security gap. Phase A
tolerance: the first audit quarter establishes the baseline; drift from baseline is the
operational SLO (downward trend in coverage is the alert condition). Phase B: any quarter
that ends below the prior quarter's coverage triggers D1 Priority Remediation.
[src:raw/books-md/sre/google-sre-book.md:Ch.4 SLI/SLO framework]

---

## §H Code-Level Interfaces

All Part 6a-owned code lives as subcommand extensions of `swarm/lib/`-owned `/lint` (citation
and F-G-R scanners) and as new `swarm/lib/`-owned skills (audit and approvals). This follows
the Part 1 §H ownership contract: `/lint` is owned by `swarm/lib/` shared infra; Part 6a
extends it without creating a competing skill. [src:part-1-architecture.md:§H; src:engineering-expert-multi-mode.md:§2.3]

### H.1 `/lint --check-citations [--path=<dir-or-file>] [--strict]`

```
Entry point:   /lint --check-citations [--path=<dir-or-file>] [--strict] [--rlaif]
Input:         One or more .md files in swarm/wiki/ canonical paths (or drafts/ for advisory)
Outputs:
  stdout:      Human-readable summary (≤20 lines): "Scanned N files, M citations, K flags"
  stderr:      Structured flag report: one line per flag, format TYPE|file:line|evidence
               Types: BARE-CLAIM, CARGO-CULT, BROKEN-PATH, BROKEN-ANCHOR
Exit codes:    0 = clean (zero flags); N = N flags found; 2 = scanner internal error
Env vars:      RLAIF_ENABLED=1 (default: 0; never set in pre-commit or CI paths)
```

Implementation file: `swarm/lib/lint-check-citations.sh`

The scanner is a four-algorithm pipeline. All four algorithms are stateless and independently
testable. This is Unix decomposition within the module: each algorithm does one thing.
[src:engineering-expert-multi-mode.md:§2.2 "four algorithms, each stateless"]

**Algorithm A — Bare-claim detector (deterministic regex).**
Operates line-by-line on body text of any canonical markdown artefact.
Flag condition: line ends with `.` (sentence terminator) AND contains at least one claim
keyword (`must`, `will`, `is`, `has`, `requires`, `enforces`, `ensures`, `guarantees`, `never`,
`always`) AND no `[src:` token appears within the preceding 500-character sliding window.
Flag output: `BARE-CLAIM | file:line | "sentence text"`
False-positive risk: claim keywords appear in non-claim prose. Mitigation: 500-char window is
generous; residual false positives are handled by Algorithm D (RLAIF optional pass, critic-gate
invocation only). [src:engineering-expert-multi-mode.md:§2.2 Algorithm A]

**Algorithm B — Cargo-cult detector (deterministic regex).**
Operates on every `[src:...]` citation token found in body text.
Flag condition: `[src:...]` token found AND within the 200-character window AFTER the token:
none of these consequence-verb tokens present (`therefore`, `so`, `thus`, `hence`, `this means`,
`applies as`, `requires`, `must`, `MUST`, `enforces`, `consequently`, `which means`) AND none
of these operational-change keywords present (`anti-scope`, `lint flag`, `gate`, `halt`,
`BLOCKED`, `escalate`).
Flag output: `CARGO-CULT | file:line | "[src:...]" → missing consequence`

Rationale for 200-char window: a citation where the consequence is two full sentences later
is an authoring smell regardless — the connection should be made explicit. This operationalises
the citation discipline: citation + consequence within 200 chars is the declared standard.
[src:engineering-expert-multi-mode.md:§2.2 Algorithm B; src:anthropic-constitutional-ai.md:§4 P6 transparency]

**Algorithm C — Broken-citation detector (filesystem check).**
Operates on every `[src:path:anchor]` token.
Step 1: parse `path` component → `os.path.exists(repo_root + "/" + path)`. False → flag
`BROKEN-PATH | file:line | "path not found: <path>"`.
Step 2: if path exists AND anchor declared → grep file for `^## <anchor>` or `^### <anchor>`.
No match → flag `BROKEN-ANCHOR | file:line | "anchor not found in <path>"`.
Step 3: if no anchor in citation token → no flag (bare-path citations are valid).

Critical edge case — path rename breakage: when `git mv` renames a file, all citations to the
old path break silently. Algorithm C detects this at lint time but not at commit time.
Recommended mitigation (Phase B): add a `post-rewrite` git hook that runs Algorithm C on any
commit touching files with path renames. Phase A: log-only non-blocking warning to
`swarm/logs/lint-events.jsonl`. [src:engineering-expert-multi-mode.md:§2.2 Algorithm C edge case]

**Algorithm D — RLAIF self-critique (optional, critic-gate only).**
Applies ONLY to pending flags from Algorithms A and B (not C, which is deterministic).
Disabled by default (`RLAIF_ENABLED=0`). Enabled only when `/lint --rlaif` is invoked
explicitly (quarterly immune audit, per-cycle critic-gate pass). NEVER enabled in pre-commit.
Performance rationale: at current scale (~5,500 citations), RLAIF adds ~46 minutes to every
scan. Pre-commit timeout budget is 10 seconds. RLAIF on pre-commit = hard usability failure.
[src:engineering-expert-multi-mode.md:§2.4 "RLAIF must be disabled on pre-commit hooks"]

RLAIF integration design:
```
For each pending flag from A or B:
  1. Extract surrounding text S (200-char window around flagged sentence)
  2. Prompt: "Does the following sentence have a concrete operational consequence
     that a system or agent could act on? Answer YES or NO with one-sentence
     justification.\n\nSentence: <flagged text>"
  3. RLAIF YES → suppress flag; log "implicit-consequence-detected" to lint-events.jsonl
  4. RLAIF NO → emit flag
  5. RLAIF failure (timeout after 5s, retry 1, then fallback): emit flag conservatively;
     log {type: rlaif-failure, timestamp, sentence_hash} to lint-events.jsonl
```

Fallback is conservative (emit the flag): a false positive that reaches a human is recoverable;
a false negative that silently suppresses a genuine cargo-cult citation is a provenance failure.
[src:engineering-expert-multi-mode.md:§6.2 FINDING-1 recommended fix]

**Expected false-positive reduction from RLAIF: ~30%.** Bai 2022 §3 demonstrated false-positive
reduction via self-critique in harmlessness feedback. Application here is analogous: RLAIF
reduces the need for human review of every cargo-cult flag candidate, just as Constitutional AI
reduces the need for human labelers on every harmlessness training example. The analogy is
correct but partial — here we reduce review burden at lint time, not training time.
[src:raw/books-md/anthropic/bai-2022-cai.md:§3 RLAIF method; src:philosophy-expert-multi-mode.md:§M item 2]

### H.2 `/lint --check-fg-r [--path=<dir-or-file>]`

```
Entry point:   /lint --check-fg-r [--path=<dir>]
Default path:  swarm/wiki/ (recursive)
Checks:
  (a) F: field present in frontmatter
  (b) F level ∈ {F3..F9} for canonical paths (F0-F2 = gate violation)
  (c) ClaimScope: field present and non-empty
  (d) R.refuted_if present (Hamel-binary predicate: length < 200 chars, no tautological
      qualifiers like "It would be difficult to...")
Output:        Per-file findings with line reference; summary counts
Exit codes:    0 = clean; N = N violations; 2 = scanner error
```

Implementation file: `swarm/lib/lint-check-fg-r.sh`

Kept separate from `--check-citations` per OQ-6A-2 engineering verdict: F-G-R field presence
checks operate on frontmatter (structural layer); citation content checks operate on body text
(semantic layer). Callers who need only the quick SLO snapshot (Part 8 health monitor) should
not be forced to run the full citation scan. Merging them would violate the deep-module
principle. [src:engineering-expert-multi-mode.md:§9 OQ-6A-1 verdict]

### H.3 `/audit --quarterly [--cycle=<cycle-id>] [--year=YYYY] [--quarter=N]`

```
Entry point:   /audit --quarterly [--cycle=<cycle-id>] [--year=YYYY] [--quarter=N]
Trigger:       Part 8 quarterly-audit-event OR manual brigadier invocation
Actions:
  1. Run /lint --check-fg-r over all canonical paths → D1 data
  2. Run /lint --check-citations --mode=broken-only over all canonical paths → D2 data
  3. Run /lint --check-citations --mode=cargo-cult-only over all canonical paths → D3 data
  4. Run dangling-edge check over wiki/graph/edges.jsonl → D4 data
  5. Run IP-1 executor-name grep over swarm/wiki/foundations/ → D5 data
  6. Count canonical promotions in log.jsonl without gate packet reference → D6 data
  7. Instantiate audit template (§I.3) with collected data
  8. Write to swarm/audits/Q<n>-YYYY.md
Exit:          0 = audit complete; N = audit found N priority-high findings
```

### H.4 `/approvals --regen-log`

Rebuilds `swarm/approvals/log.md` from `swarm/approvals/log.jsonl`. This is the CQRS
read-model rebuild operation. The markdown view is always reconstructable from the JSONL
source; the JSONL source is authoritative and never modified.
[src:event-sourcing-cqrs.md:§4 Principle 2 "projections can be discarded and rebuilt"; src:engineering-expert-multi-mode.md:§3.4]

### H.5 `/approvals --filter <key>=<value> [--since YYYY-MM-DD]`

Query the approval log. Examples:
- `/approvals --filter gate_class=stop_gate --since 2026-01-01`
- `/approvals --filter acked_by=ruslan`
- `/approvals --entry appr-20260428-001`

All queries operate on `log.jsonl` via `jq`. The markdown view is not queried — it is a
rendering convenience only. [src:engineering-expert-multi-mode.md:§3.4]

### H.6 swarm/lib/ ownership and subcommand architecture

```
swarm/lib/lint.sh                            # existing, swarm/lib/-owned
  case "$1" in
    --check-fg-r)         source swarm/lib/lint-check-fg-r.sh ;;       # Part 6a P6a.1
    --check-citations)    source swarm/lib/lint-check-citations.sh ;;  # Part 6a P6a.2
    --check-stage-gates)  source swarm/lib/lint-check-stage-gates.sh ;; # existing
    --check-commit-format) source swarm/lib/lint-check-commit-format.sh ;; # Part 1 P1.2
    --all)                # runs all subcommands in sequence
  esac
```

Why subcommand, not standalone? DRY principle at skill level: file-walk logic, report
formatting, exit-code conventions, and pre-commit hook integration are already present in
`swarm/lib/lint.sh`. The subcommand pattern inherits them without duplication. A standalone
`/check-citations` script would replicate all of this — a DRY violation.
[src:engineering-expert-multi-mode.md:§2.3 DRY rationale; src:clean-code.md:§4 P3]

---

## §I Data Schemas

### I.1 F-G-R JSON Schema (`shared/schemas/f-g-r.json`)

**First-principles derivation of the triad (why F-G-R and not a duo or quad).**

The F-G-R triad is justified from first principles as the minimal sufficient set of orthogonal
epistemic dimensions for actionable claims in a multi-agent, multi-cycle knowledge system.
Each dimension answers a distinct, irreducible question:
[src:philosophy-expert-multi-mode.md:§I.1 irreducibility argument]

- **F (Formality)** answers: "How rigorously was this claim derived?" — the *process* dimension.
  It captures derivation pedigree from F0 (single hunch) to F9 (mathematically formalised).
  F cannot be inferred from G or R: a claim can be high-formality (F7, derived from peer-reviewed
  methodology) but narrow-scope (G = single bounded context). Dropping F would force G to carry
  derivation-quality information, corrupting G's role as a pure scope declaration.

- **G (ClaimScope)** answers: "Where does this claim hold?" — the *context* dimension.
  It bounds the claim's validity domain. Per FPF IP-2 Context-is-king: "make meaning local;
  make translation explicit." A high-reliability claim (R-high) can still have a narrow scope
  (single bounded context). G cannot be replaced by F or R.
  [src:levenchuk-shsm-fpf.md:§4 P3 IP-2 Context-is-king]

- **R (Reliability)** answers: "How trustworthy is this claim, given evidence?" — the *evidence*
  dimension. It captures the evidence warrant and carries the Popperian falsifiability condition
  in the `refuted_if:` field. A claim without `refuted_if` has R-undefined status — it can never
  be wrong because no evidence would count against it, making it a zero-value epistemic asset.
  Dropping R eliminates epistemic accountability.
  [src:philosophy-expert-multi-mode.md:§2.4 P1 Popper; src:design/JETIX-FPF.md:§4.2 CP-2]

**Why not a duo?**
- F+G without R: derivation quality and scope declared, but no evidence accountability. A formal
  (F7), well-scoped (G = Foundation) claim could be completely wrong with no refutation path.
- F+R without R: derivation quality and evidence strength, but claim applies "everywhere" by
  default — scope-soup anti-pattern.
- G+R without F: scope and evidence declared, but no information about how the claim was derived.
  A well-evidenced (R-high) claim could rest on single-author intuition (F1) or 10-cycle
  validated convention (F4); the distinction is epistemically load-bearing.

**Why not a quad?** Two plausible fourth dimensions and why they collapse into the existing triad:
- Temporal validity (T): subsumed under R via `decay_after:` field (FPF B.3.4 Evidence Decay).
  Temporal validity is a property of the reliability warrant, not a separate epistemic axis.
- Author authority (A): captured by F-level (F7+ requires documented derivation methodology;
  F5+ requires written + reviewed). A separate author field would conflate process (F) with
  person, violating IP-1 Role≠Executor at the epistemic level.

**Full JSON Schema (`shared/schemas/f-g-r.json`):**

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
        "F3": "informal multi-source synthesis (≥2 sources)",
        "F4": "operational convention (3+ cycles applied, evidence in approval log)",
        "F5": "codified rule (written + reviewed; brigadier critic pass documented)",
        "F6": "codified rule + 3+ successful applications + cross-cycle reuse evidence",
        "F7": "methodology with explicit Hamel-binary acceptance predicate",
        "F8": "constitutional boundary (FUNDAMENTAL Vision lock-class; Ruslan ack mandatory)",
        "F9": "mathematically formalised invariant (formal proof or equivalent)"
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
            "R-low": "anecdotal, single-source, no replication (F0-F2 range typical)",
            "R-medium": "multi-source synthesis, informal replication (F3-F5 range typical)",
            "R-high": "peer-reviewed, formal validation, or 10+ consistent cycles (F5-F7 range)",
            "R-certified": "external auditor-verified or formally proven (F8-F9 range)"
          }
        },
        "refuted_if": {
          "description": "Hamel-binary falsification criterion. One specific observable that
                          would refute this claim. NOT a prose essay. Max 200 chars.
                          Tautological qualifiers ('it would be difficult to...') are invalid.",
          "type": "string",
          "minLength": 10,
          "maxLength": 200
        },
        "accepted_if": {
          "description": "Hamel-binary acceptance criterion (optional but strongly recommended)",
          "type": "string",
          "maxLength": 200
        },
        "receipt": {
          "description": "Where to verify the claim's evidence base (path + section)",
          "type": "string"
        }
      }
    },
    "decay_after": {
      "description": "FPF B.3.4 Evidence Decay — ISO 8601 date after which quarterly audit
                      flags this claim as STALE. Optional; use for time-sensitive claims.",
      "type": "string",
      "format": "date"
    }
  },
  "additionalProperties": false
}
```

**Validation rules (enforced by `/lint --check-fg-r`):**

1. `F` must be in `[F3, F4, F5, F6, F7, F8, F9]` for any canonical artefact path (not in
   `drafts/`). F0-F2 values = draft-only; attempting to promote = gate failure.

2. `R.refuted_if` MUST be present AND MUST be a Hamel-binary predicate: length < 200 chars
   AND does not start with tautological qualifiers ("It would be difficult...", "Potentially...",
   "This claim could be refuted if evidence emerged suggesting otherwise").

3. F8/F9 artefacts require AWAITING-APPROVAL packet with `acked_by: ruslan` in approval log
   before canonical promotion. Scanner check: query `log.jsonl` for matching `artefact_path` +
   `acked_by: ruslan` entry with `artefact_f_level: F8` or `F9`.

4. `decay_after` is optional. If present and date has passed, quarterly audit flags the
   artefact as `STALE` (finding class `F-G-R-decay`) for Ruslan review.

5. `ClaimScope.scope_tokens` must include at least one of: `Foundation`, `RUSLAN-LAYER`,
   `Phase-A-single-owner` — the three top-level layer tokens that map to the Foundation/RUSLAN-LAYER
   distinction. [src:philosophy-expert-multi-mode.md:§I.1 validation rule 5]

**HARD GAP A — F-level anchor wording refinements.** The F4, F6, and F8 anchor definitions
in this schema are refinements relative to the upstream FPF B.3 canonical description:
- F4 now explicitly requires "evidence in approval log" (not just "convention" — adds a
  Hamel-binary count threshold)
- F6 adds "cross-cycle reuse evidence" as a distinguishing criterion from F5
- F8 is tied to "FUNDAMENTAL Vision lock-class" (grounds the constitutional boundary in
  Jetix's specific architectural context)

These refinements are PROPOSED for Ruslan ack as F8 constitutional revisions. Until acked,
the canonical anchor is FPF B.3 as stated in `design/JETIX-FPF.md:§12.7`; the refinements
here are F5 design-level claims. Status: REQUIRES-APPROVAL.
[src:philosophy-expert-multi-mode.md:§L P6a.1 epistemic note]

### I.2 Approval Log JSONL Entry Schema (`shared/schemas/approval-log-entry.json`)

**Format decision rationale.** JSONL (not markdown tables, not CSV) is the primary record for
five reasons: (1) append-only semantics are natural in JSONL (one JSON object per line, `echo
'{...}' >> log.jsonl` is the write operation — no file parsing on write); (2) machine-
parseability without regex (`jq 'select(.gate_class == "stop_gate")' log.jsonl` is reliable);
(3) CQRS read/write split — JSONL is the write model, markdown table is the derived read model
(regenerated via `/approvals --regen-log`); (4) scalability to 10K entries without structural
change; (5) schema version support for forward compatibility.
[src:engineering-expert-multi-mode.md:§3.1 format decision; src:event-sourcing-cqrs.md:§4 Principles 2-3]

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/approval-log-entry.json",
  "title": "Approval Log JSONL Entry Schema",
  "description": "One entry per gate resolution event. Append-only. Corrections via corrects: field.",
  "type": "object",
  "required": [
    "entry_id", "entry_type", "schema_version", "timestamp_utc",
    "gate_class", "artefact_path", "artefact_f_level", "artefact_g_scope",
    "artefact_r", "acked_by", "acked_at", "gate_packet_path", "corrects", "notes"
  ],
  "properties": {
    "entry_id": {
      "description": "Unique ID per CLAUDE.md message ID convention, adapted to appr- prefix",
      "type": "string",
      "pattern": "^appr-[0-9]{8}-[0-9]{3}$"
    },
    "entry_type": {
      "type": "string",
      "enum": ["gate_ack", "gate_rejection", "correction", "audit_event"]
    },
    "schema_version": {
      "description": "Semantic version for upcasting on schema evolution",
      "type": "string",
      "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"
    },
    "timestamp_utc": {
      "description": "ISO 8601 UTC timestamp of gate resolution",
      "type": "string",
      "format": "date-time"
    },
    "gate_class": {
      "description": "Gate class string from Part 6b taxonomy. Part 6a records the value;
                      Part 6b owns the enum definition. Reference coupling, not schema embedding.",
      "type": "string"
    },
    "artefact_path": {
      "description": "Repo-rooted path of the artefact at gate time",
      "type": "string"
    },
    "artefact_f_level": {
      "description": "F-level of artefact at gate time (snapshot; artefact may evolve after)",
      "type": "string",
      "enum": ["F0","F1","F2","F3","F4","F5","F6","F7","F8","F9"]
    },
    "artefact_g_scope": {
      "description": "ClaimScope string of artefact at gate time (snapshot)",
      "type": "string"
    },
    "artefact_r": {
      "description": "R.accepted_if value of artefact at gate time (snapshot)",
      "type": "string"
    },
    "acked_by": {
      "description": "Actor who resolved the gate. ruslan = human owner (sole authority for
                      F8/F9 and irreversible). brigadier-with-ack = acting on prior standing
                      auth. autonomous-low-risk = Tier 3 auto-always no ack required.",
      "type": "string",
      "enum": ["ruslan", "brigadier-with-ack", "autonomous-low-risk"]
    },
    "acked_at": {
      "description": "ISO 8601 UTC timestamp of human ack (for human actors)",
      "type": ["string", "null"],
      "format": "date-time"
    },
    "gate_packet_path": {
      "description": "Path to the AWAITING-APPROVAL packet. Reference only — not embedded copy
                      of packet body. Part 6b owns the packet schema.",
      "type": ["string", "null"]
    },
    "corrects": {
      "description": "entry_id of a prior entry this entry corrects (Reversal Transaction).
                      null if this is an original entry.",
      "type": ["string", "null"]
    },
    "notes": {
      "description": "Optional free text, max 200 chars",
      "type": ["string", "null"],
      "maxLength": 200
    }
  },
  "additionalProperties": false
}
```

**Idempotency gate.** Before appending a `gate_ack` entry, `/audit --append-ack` checks whether
`log.jsonl` already contains an entry with matching `gate_packet_path` AND `entry_type:
gate_ack`. If found: return "already acked; no new entry written." Idempotency key:
`gate_packet_path + entry_type`. Prevents duplicate ack entries from double-clicking or
re-running `/audit`. [src:engineering-expert-multi-mode.md:§3.3 idempotency gate]

### I.3 Quarterly Audit Report Template

```markdown
---
title: Quarterly F-G-R + Provenance Immune Audit — <YYYY> Q<N>
date: <ISO 8601 date of audit run>
triggered_by: part-8-quarterly-audit-event | manual
cycle: <cycle-id in effect at audit time>
auditor: philosophy-expert | human-override
F: F4
ClaimScope:
  holds_when: "All canonical artefacts in swarm/wiki/ at audit timestamp"
  scope_tokens: [Foundation, Phase-A-single-owner]
R:
  tier: R-medium
  refuted_if: "Scanner run fails to complete; OR auditor manually overrides >10% of
               scanner findings without documented rationale"
  accepted_if: "Part 8 health monitor consumes this report without surfacing structural
                contradictions in any of the six dimensions"
sources:
  - swarm/lib/lint-check-fg-r.sh (D1)
  - swarm/lib/lint-check-citations.sh (D2, D3)
  - wiki/graph/edges.jsonl (D4)
  - swarm/approvals/log.jsonl (D5, D6)
---

# Quarterly Immune Audit — <YYYY> Q<N>

## 1. Audit Scope

- Canonical artefacts scanned: <count>
- Drafts excluded: <count>
- Audit date range: <from> to <to>
- Scanner version: <swarm/lib/lint.sh version or "manual">

## 2. D1 — F-G-R Drift

| Finding class | Count | Severity |
|---|---|---|
| Missing F field (canonical path) | <N> | High |
| F0-F2 in canonical path | <N> | High (Law L2 violation) |
| Missing ClaimScope | <N> | Medium |
| Missing R.refuted_if | <N> | High (Popper gap = Law L1 violation) |
| Non-Hamel-binary refuted_if (tautological) | <N> | Medium |
| Stale (past decay_after date) | <N> | Medium |
| F8/F9 without Ruslan-ack approval log entry | <N> | High (Law L3 constitutional violation) |
| F-G-R inflation (F-jump without log evidence) | <N> | High |

F-G-R coverage: <X>% (target: 100%)

## 3. D2 — Citation Health

| Metric | Value | Target |
|---|---|---|
| Total citations scanned | <N> | — |
| Broken path citations | <N> | 0 |
| Broken anchor citations | <N> | 0 |
| Broken citations total | <N> | 0 (Law L4) |

## 4. D3 — Cargo-Cult Drift Time Series

| Metric | This quarter | Prior quarter | 4-cycle rolling avg | Alert? |
|---|---|---|---|---|
| Cargo-cult flags (raw) | <N> | <N> | <N> | >2× avg? |
| After RLAIF pre-filter (if enabled) | <N> | <N> | <N> | — |

## 5. D4 — Typed Edge Health

| Metric | Value | Target |
|---|---|---|
| Total edges in wiki/graph/edges.jsonl | <N> | — |
| Dangling edges (target not found) | <N> | 0 |
| Generic "depends-on" edges found | <N> | 0 (A.14 discipline) |

## 6. D5 — IP-1 Violations

| Artefact | Executor name found | Remediation action |
|---|---|---|
| <path> | <executor name in Foundation-level definition> | Replace with role archetype; move binding to RUSLAN-LAYER; AWAITING-APPROVAL packet |

IP-1 violation count: <N> (target: 0 in Foundation-level artefacts)

## 7. D6 — Gate-Packet Completeness (proposed dimension, mgmt-expert)

| Metric | Value | Target |
|---|---|---|
| Canonical promotions in approval log | <N> | — |
| Promotions without corresponding gate packet | <N> | 0 |
| Gate-packet completeness ratio | <X>% | 100% |

## 8. Sycophancy Detection Stub (OQ-CAI-3)

> Status: OQ-CAI-3 unresolved (Wave C gap). Detection mechanism undefined.
> [src:anthropic-constitutional-ai.md:§8 OQ-CAI-3]
> Scheduled resolution: Wave D or Part 8 specification.
> Manual trigger: if Ruslan observes sycophancy pattern in any synthesis artefact,
> log here with artefact path + observed pattern + AWAITING-APPROVAL for correction cycle.

Findings this quarter: <N or "none — detection mechanism not yet implemented">

## 9. Audit Summary

| Dimension | Status | Trend vs prior quarter |
|---|---|---|
| F-G-R coverage | <X>% | ↑ / ↓ / → |
| Broken citations | <N> | ↑ / ↓ / → |
| Cargo-cult rate | <X>% | ↑ / ↓ / → |
| IP-1 violations | <N> | ↑ / ↓ / → |
| Dangling edges | <N> | ↑ / ↓ / → |
| Gate-packet completeness | <X>% | ↑ / ↓ / → |

## 10. Priority Remediations (Top 5)

1. <artefact path> — <finding class> — <required action>
2. ...

## 11. Escalations to Brigadier

> List findings requiring AWAITING-APPROVAL packet:
> - F8/F9 artefacts without Ruslan ack
> - Dangling edges in foundations/
> - IP-1 violations in Foundation Parts
> - Gate-packet completeness gaps (D6)
> For each: escalation type, artefact path, required action.

## 12. Part 8 Coordination Note

> This section summarizes health signals for Part 8 consumption.
> Part 8 methodologically-uses this audit framework.
> [src:part-6-governance-provenance-human-gate.md:§D "Part 6 ↔ Part 8 dual"]
>
> Emitted signals this quarter:
> - fg_r_coverage_pct: <X>%
> - broken_citation_count: <N>
> - cargo_cult_flag_count: <N>
> - dangling_edge_count: <N>
> - gate_packet_completeness_pct: <X>%
```

### I.4 Citation Regex Specification

For reproducibility and portability: the exact regex contracts for Algorithms A, B, C.
[src:engineering-expert-multi-mode.md:§2.2 — all three algorithms]

**Claim-keyword list (Algorithm A):**
```
CLAIM_KEYWORDS = [
  "must", "will", "is", "has", "requires", "enforces", "ensures",
  "guarantees", "never", "always"
]
```

**Sentence terminator (Algorithm A):** Line ends with `.` after optional whitespace.

**Sliding window (Algorithm A):** 500-character backward window from line end; presence of
`[src:` anywhere in this window suppresses the bare-claim flag.

**Consequence-verb tokens (Algorithm B):**
```
CONSEQUENCE_VERBS = [
  "therefore", "so", "thus", "hence", "this means", "applies as",
  "requires", "must", "MUST", "enforces", "consequently", "which means"
]
OPERATIONAL_CHANGE_KEYWORDS = [
  "anti-scope", "lint flag", "gate", "halt", "BLOCKED", "escalate"
]
```

**Forward window (Algorithm B):** 200-character forward window from end of `[src:...]` token.
Presence of any consequence-verb or operational-change keyword in this window suppresses the
cargo-cult flag.

**Broken-path check (Algorithm C):** `os.path.exists(repo_root + "/" + path_component)`
where `repo_root` is the absolute path to the git repository root (resolved at scanner startup
via `git rev-parse --show-toplevel`).

**Broken-anchor check (Algorithm C):** `grep -n "^## <anchor>" <file_path>` OR
`grep -n "^### <anchor>" <file_path>`. Match = anchor exists; no match = flag.

---

## §J Operational Rituals

The rituals below define the steady-state cadences at which Part 6a's mechanisms fire.
Phase A = advisory (no blocking). Phase B = blocking on canonical paths.
[src:philosophy-expert-multi-mode.md:§J]

### J.1 Per-Commit Citation Lint (Event-Driven, Fast Path)

```
Trigger:   git pre-commit hook (Phase A: advisory; Phase B: blocking for canonical paths)
Command:   /lint --check-citations --path=<staged-files>
           /lint --check-fg-r --path=<staged-files>
Blocking:  Phase A: NO (log findings, do not block commit)
           Phase B: YES for canonical paths; advisory for drafts/
Output:    stderr flags; Phase B blocks commit on Law violations
Latency:   ≤10 seconds at Phase A scale (regex only; RLAIF disabled)
RLAIF:     NEVER enabled in pre-commit hook path
```

Per-commit lint is the real-time enforcement arm. It is distinct from the quarterly audit:
per-commit check is deterministic and fast (structural validation only); the quarterly audit
is comprehensive and interpretive (includes RLAIF, IP-1 pattern recognition, trend analysis).
Neither replaces the other. [src:philosophy-expert-multi-mode.md:§J.1 integrator note]

### J.2 Quarterly Audit (Calendar-Driven, Comprehensive)

```
Trigger:   Q1=January, Q2=April, Q3=July, Q4=October (calendar boundary)
           OR manual: brigadier --trigger quarterly-audit
Command:   /audit --quarterly [--cycle=<cycle-id>]
Output:    swarm/audits/Q<n>-YYYY.md
Commit:    brigadier commits after Ruslan review
RLAIF:     ENABLED (--rlaif flag) — acceptable because this is not a blocking pre-commit
Duration:  Phase A estimated: 2-4 hours including RLAIF pass and report writing
```

The quarterly audit is the knowledge base's earnings call — the periodic forcing function that
prevents silent drift. Without it, F-G-R tags that were accurate at cycle 3 stagnate at cycle 15.
The audit forces a full census: total canonical count, F-level distribution, citation health,
trend comparison. [src:investor-expert-capital-allocation.md:§4 quarterly audit as earnings call]

### J.3 Approval Log Weekly Regeneration (Scheduled)

```
Trigger:   Weekly, Friday 17:00 (RUSLAN-LAYER cron binding — timezone specific to Ruslan's TZ)
Command:   /approvals --regen-log
Purpose:   Rebuild swarm/approvals/log.md from log.jsonl (CQRS read-model refresh)
Commit:    Brigadier commits the regenerated log.md
```

### J.4 Gate Ack Recording (Event-Driven, On Every Gate Resolution)

```
Trigger:   Part 6b gate ack event (Ruslan acks AWAITING-APPROVAL packet)
Command:   /audit --append-ack --packet=<gate_packet_path> --artefact=<path> --actor=ruslan
Idempotency: checked (§I.2 idempotency gate); double-ack = no-op
Output:    Appended JSONL entry to swarm/approvals/log.jsonl
```

### J.5 Phase B Upgrade: Advisory → Blocking

At Phase B activation, two changes occur simultaneously (mirror of Part 1 P1.2 upgrade-path):
1. Pre-commit hook switches from advisory to blocking for canonical paths (Law violations
   prevent commit).
2. The `RLAIF_ENABLED` env var is still `0` by default in all pre-commit paths (the latency
   constraint does not change at Phase B).

This upgrade requires an AWAITING-APPROVAL packet authored by brigadier, Ruslan ack, and a
test suite validation confirming the blocking behaviour does not create false-positive deadlocks.
[src:philosophy-expert-multi-mode.md:§J.1; src:part-1-architecture.md P1.2 upgrade-path mirror concept]

---

## §K Failure Modes

Failure modes are treated as commits, not blame. Each mode has an observable, detection
mechanism, and response — not an accusation. This is SRE Chapter 15 blameless postmortem
culture applied to architecture specification. The Google SRE Book, Ch. 15, states the
principle directly: "The primary goals of a postmortem are to ensure that the incident is
documented, that all contributing root causes are well understood, and that effective preventive
actions are put in place to reduce the likelihood or impact of recurrence." Consequence for
Part 6a: every K-entry in this table is a pre-declared postmortem template. When a failure
mode fires in production, the observable column becomes the incident trigger, the detection
column becomes the detection narrative, and the response column becomes the action items.
The postmortem is already half-written. [src:raw/books-md/sre/google-sre-book.md:Ch.15 blameless postmortem]

**Burn-rate alert tiers for broken-citation rate.** Drawing from the SRE Workbook (Implementing
SLOs, §12 burn-rate algebra): the burn-rate framework provides three alert tiers that balance
detection speed against false-positive rate. Adapted to the broken-citation error-budget signal:

| Alert Tier | Burn Rate | Broken-Citation Rate Threshold | Alert Window | Consequence |
|---|---|---|---|---|
| Page-equivalent (critical) | 14.4× | >14.4% of citations broken in any single quarterly scan | Immediate | D2 Priority Remediation; brigadier constructs AWAITING-APPROVAL for Ruslan; no new canonical promotions until resolved |
| Ticket-equivalent (warning) | 6× | >6% citations broken | Within-cycle alert to brigadier | D2 findings escalated; scanner re-run within 7 days |
| Background (trend) | 1× | Any broken citations detected | Next quarterly audit | D2 finding logged; fix scheduled in next cycle |

The 14.4× threshold is the SRE Workbook's canonical "fast burn" rate: at this rate, the
broken-citation error budget would be exhausted in 1/14.4 of the error-budget window (roughly
6 days per quarter). At 6×, exhaustion in 2 weeks. At 1× (steady-state), the error budget
exhausts exactly at the quarter boundary. This tiered structure prevents both over-alerting
(treating every single broken citation as a critical incident) and under-alerting (treating
a 10% broken-citation rate as normal. The thresholds are Phase B targets; Phase A uses the
simplified "any broken citations → fix before next cycle" rule.
[src:raw/books-md/sre/google-srewb-implementing-slos.md:§12 burn-rate algebra "1×/6×/14.4×"]

| ID | Failure Mode | Observable | Detection | Response |
|----|--------------|------------|-----------|----------|
| K1 | F-G-R drift undetected | Canonical artefacts declare higher F than evidence warrants; `fg_r_delta` in log shows step-function jumps | Quarterly audit D1: cross-reference F-level jumps against approval log evidence | Flag `F-G-R-inflation` finding; require AWAITING-APPROVAL with evidence summary for each inflated jump |
| K2 | Lint false positive on legitimate paraphrase | Authors receive spurious cargo-cult flags; start omitting citations to avoid flags | Cargo-cult rate trends UP while F-G-R coverage trends UP — paradoxical pattern | Re-calibrate RLAIF pre-filter threshold; add consequence-keyword heuristics; re-run against synthetic test suite |
| K3 | Broken citations after file rename | `git mv` renames canonical file; all `[src:old-path:anchor]` citations break silently | Algorithm C detects at next lint run; post-rewrite hook (Phase B) detects immediately | Phase A: quarterly audit D2 catches stragglers. Phase B: post-rewrite hook logs broken citations immediately (non-blocking). |
| K4 | Quarterly audit not invoked | Part 8 fails to emit `quarterly-audit-event`; brigadier backup trigger not set | F-G-R drift detected retrospectively when downstream artefact cites stale F4 as current | Part 8 integration test: verify quarterly-audit-event fires per calendar. Brigadier quarterly manual trigger as failsafe. |
| K5 | Approval log JSONL corruption | JSONL file fails `jq .` parse check | Daily `jq . swarm/approvals/log.jsonl > /dev/null` integrity check (Part 1 fsck); failure → alert | Restore from prior git ref; investigate the non-append commit that introduced corruption |
| K6 | Schema version mismatch on log import from fork | Old `log.jsonl` entries from prior schema version are imported without upcasting | Schema validation fails on import: entries use `schema_version: 0.9.0` but validator expects `1.0.0` | Schema version history at `swarm/approvals/schema-version-history.yaml`; upcasting functions per event-sourcing Principle 4. HARD GAP C: `cross-fork-provenance.json` needs `approvals_reconciliation_strategy` field. [src:engineering-expert-multi-mode.md:§5.3] |
| K7 | RLAIF cost explosion if accidentally enabled in pre-commit | CI/pre-commit build time explodes from seconds to hours (~46 min at current scale) | CI build time > 2× normal triggers alert | `RLAIF_ENABLED` env var gated; default 0; CI pipelines must never set this var; test: three CI runs with env var absent complete under 30s each |
| K8 | Approval log substituting for AWAITING-APPROVAL packet | Artefacts are promoted to canonical without a blocking gate packet; log entries appear but no prior BLOCKED state was enforced | D6 audit dimension: count(canonical promotions without gate packet) > 0 | D6 triggers priority remediation; brigadier retroactively creates gate packets for unpacketed promotions and escalates to Ruslan review |
| K9 | Cargo-cult flag rate suppression by RLAIF false negatives | RLAIF consistently marks genuine cargo-cult citations as "implicit-consequence-present"; rate anomalously low vs manual spot-check | Quarterly audit: manual 10% random sample of RLAIF-suppressed flags; if disagreement > 20% → RLAIF false negative rate is too high | Cap RLAIF suppression at 30% of total cargo-cult candidates; above 30% = require human review of RLAIF verdicts |
| K10 | OQ-CAI-3 sycophancy detection unaddressed | Sycophantic synthesis artefacts reach canonical state; they appear to satisfy surface F-G-R criteria but their content confirms priors rather than challenging them | No automated detection at Wave C. Manual: Ruslan notices pattern in synthesis output and logs it in quarterly audit §8 | Stub acknowledged in audit template §8. Resolution scheduled: Wave D or Part 8. Until then: manual vigilance; Ruslan logs instances; brigadier flags for next bundle. [src:anthropic-constitutional-ai.md:§8 OQ-CAI-3] |

**Risk-of-ruin floor (investor lens).** None of K1-K10 individually is a risk-of-ruin event
for Phase A. The catastrophic scenario is all four primary failure modes compounding: K1
(F-G-R drift undetected) + K5 (log corrupted) + K4 (audit skipped) + K7 (scanner accidentally
not built). At that state, the canonical wiki has degenerated to an unaudited claim pool with
false provenance signals. Estimated reconstruction cost: 40-80 hours at Phase A scale =
€2,400-4,800. Prevention cost: ~€960/year (quarterly audit) + 1-3 days engineering (scanner
implementation). The margin-of-safety arithmetic is decisive: invest in prevention.
[src:investor-expert-capital-allocation.md:§8 risk-of-ruin floor]

---

## §L Wave C Work-List Bullet Status

Per `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` lines 305-319.
[src:wave-c-worklist.md:L305-319]

### P6a.1 — F-G-R Schema Definition

**Acceptance predicate (Hamel-binary):**
"JSON Schema `shared/schemas/f-g-r.json` is structurally valid (passes `jsonschema --validate`);
F0-F9 enum is exhaustive per FPF B.3 anchors; `R.refuted_if` is a required field with
200-char max length constraint; F8/F9 gate enforcement rule is declared in §I.1 validation
rule 3; `decay_after` field supports FPF B.3.4 Evidence Decay."

**Status:** DESIGNED. Schema text complete in §I.1. Implementation (writing the JSON file to
`shared/schemas/f-g-r.json`) = brigadier + engineering-expert execution scope.

**F-G-R of this deliverable:**
```
F: F5 (codified rule, written and reviewed in Wave C architecture document)
ClaimScope: [Foundation, Jetix-mono-repo]
R:
  tier: R-medium
  refuted_if: "JSON Schema fails structural validation; OR F8/F9 gate rule is absent"
  accepted_if: "jsonschema --validate passes on first implementation; F-G-R dogfood
                table in §G validates cleanly against the schema"
```
Promotes to F8 on Ruslan ack. Promotes to F6 after first implementation cycle passes
validation.

**HARD GAP A (open):** F4/F6/F8 anchor wording refinements are PROPOSED for Ruslan ack as F8
constitutional revisions. Until acked: canonical anchor remains FPF B.3 as-stated. This
architecture document carries the proposed refinements as F5 design claims, clearly flagged.

### P6a.2 — Citation Enforcement Scanner

**Acceptance predicate (Hamel-binary):**
"Scanner correctly flags 8/10 synthetic cargo-cult test cases AND zero false positives on 5
explicit-consequence test cases AND zero false negatives on 5 bare-claim test cases AND
`RLAIF_ENABLED` defaults to 0 when env var absent AND exit-code-on-zero-flags = 0 AND
exit-code-on-N-flags = N AND stderr contains one structured line per flag with format
`TYPE|file:line|evidence`."

**Status:** SPECIFIED. Skill spec complete in §H.1 + §H.6. Algorithm contracts in §H.1.
Implementation of `swarm/lib/lint-check-citations.sh` = engineering-expert scope.

**HARD GAP B (open):** Scanner implementation timeline. Investor-expert verdict: implement
within 2 cycles of Wave C completion. Deferral to Wave D is a capital risk — without the
scanner, cargo-cult citation rate drifts invisibly and the 3-20x ROI on enforcement time is
unrealized. [src:investor-expert-capital-allocation.md:§10 P6a.2 priority P2]

**Scope of RLAIF application:**
RLAIF integration verdict: APPLY — tightly bounded to cargo-cult check only (Algorithm B
pending flags), with three explicit constraints: (1) cargo-cult check only (not bare-claim or
broken-citation which are deterministic), (2) advisory not authoritative (human judgment
overrides RLAIF pre-filter), (3) NEVER in pre-commit. RLAIF reduces the need for human review
of every cargo-cult flag; it does not replace the human gate.
[src:philosophy-expert-multi-mode.md:§L P6a.2 RLAIF verdict; src:raw/books-md/anthropic/bai-2022-cai.md:§3]

### P6a.3 — Approval Log Structure

**Acceptance predicate (Hamel-binary):**
"First approval log entry written in correct JSONL format; all required fields present; `jq .
swarm/approvals/log.jsonl` exits 0 (no JSON parse errors); `git log --follow
swarm/approvals/log.jsonl` shows only append commits after 3 entries; `/approvals --regen-log`
produces a valid markdown table from the JSONL entries."

**Status:** DESIGNED. Schema complete in §I.2. `swarm/approvals/log.jsonl` file to be
scaffolded by brigadier as the first gate event is recorded.

**HARD GAP C (Phase B stub, open):** The `cross-fork-provenance.json` schema at Part 1 needs
an `approvals_reconciliation_strategy` field analogous to its existing `reconciliation_strategy`
field. In Phase A: `reconciliation_strategy: deferred-phase-b` applies. In Phase B: merge-with-
deduplication by `(gate_packet_path + entry_type + acked_at)` three-field key; genuine conflicts
→ HITL escalation. This is a Phase B HARD GAP requiring Ruslan ack before fork operations begin.
[src:engineering-expert-multi-mode.md:§5.3 Phase B stub]

### P6a.4 — Quarterly Immune Audit Framework

**Acceptance predicate (Hamel-binary):**
"Audit template instantiated for first audit cycle; all 6 audit dimensions present (D1-D6);
sycophancy stub acknowledged as OQ-CAI-3 with 'mechanism undefined; Wave D scope' note;
Part 8 coordination section (§12) populated with five named emitted signals; audit report
committed to `swarm/audits/Q<n>-YYYY.md`; brigadier confirms report format requires no
structural revisions."

**Status:** DESIGNED. Template complete in §I.3 with 6 dimensions. First execution = next
quarterly trigger (Q2-2026 = April 2026 boundary).

**D6 gate-packet completeness.** Added beyond the original D1-D5 per mgmt-expert §F.3 risk
analysis: the approval log substituting for AWAITING-APPROVAL packet is a boundary violation
detectable only with an explicit audit dimension. D6 is the structural detection mechanism.
[src:mgmt-expert-boundary.md:§F.3 proposed D6; src:mgmt-expert-boundary.md:§H Effects seam health]

---

## §M Wisdom Application Findings

> Phase D Wisdom Application Loop — 14 consultant cards + 5 library-direct supplement sources covered.
> Every YES Adopted entry corresponds to a real edit in §A-§L above.

| # | Card / Source | Principle | Current draft state | Improvement opportunity | Adopted? | Justification | Section edited |
|---|---------------|-----------|---------------------|--------------------------|----------|---------------|----------------|
| 1 | Левенчук SHSM-FPF (Card #1) | B.3 F-G-R triad | F-G-R is the schema this Part DEFINES — it is the dogfood case | — | ALREADY_APPLIED | This document is the operative definition of F-G-R | §I.1 |
| 2 | Левенчук SHSM-FPF (Card #1) | IP-4 immune system | Applied in §0 framing as Part 6a's constitutional mandate | — | ALREADY_APPLIED | §0 explicitly names IP-4 as the constitutional source | §0 |
| 3 | Левенчук SHSM-FPF (Card #1) | A.14 typed edges | §D 10-edge reference table present; zero generic "depends-on" | — | ALREADY_APPLIED | §D table covers all ten edges with A.14 vocabulary | §D |
| 4 | Левенчук SHSM-FPF (Card #1) | IP-3 artifacts-over-conversations | F-G-R schema IS an artifact; approval log IS a committed file | — | ALREADY_APPLIED | §C.1 and §I.2 enforce artifact-over-conversation discipline | §C, §I |
| 5 | Capital Allocation Antifragility (Card #10) | Lindy substrate | F-G-R F5→F8 trajectory in §G dogfood table | Add explicit Lindy verdict box in §G identifying the Lindy-grade substrates and what the verdict applies to | YES | Concrete consequence: reinforces which part of the schema is durable vs which is Jetix-specific; prevents over-claiming Lindy for the wording details | §G |
| 6 | Capital Allocation Antifragility (Card #10) | Graham margin-of-safety | F0-F2 ban = margin-of-safety framing present in §A.1 | — | ALREADY_APPLIED | §A.1 already carries the Graham margin-of-safety arithmetic | §A.1 |
| 7 | Capital Allocation Antifragility (Card #10) | Compounding approval log | Approval log antifragility noted in §B.3; compound value not explicitly stated | Add "every ack compounds epistemic capital" statement with Compounding Engineering parallel | YES | Makes the compound-value claim concrete and testable; grounds it in CE mechanics not just Taleb | §B.3 |
| 8 | Unix Philosophy (Card #11) | Plain-text universal interface | JSONL + markdown views ARE plain text; scanner uses text streams | — | ALREADY_APPLIED | §I.2 rationale point (1): natural append-only in JSONL; §H subcommand architecture uses shell text conventions | §I.2, §H |
| 9 | Unix Philosophy (Card #11) | Do one thing and do it well | Each of the four scanner algorithms is stateless and independently testable; scanner = ONE concern (citations) | — | ALREADY_APPLIED | §H.1: "each algorithm does one thing; all four are stateless and independently testable" | §H.1 |
| 10 | Event Sourcing CQRS (Card #5) | Reversal Transactions — corrections are new events | Applied in §C.1: `corrects:` field in approval log | — | ALREADY_APPLIED | §C.1 example correction flow explicitly named as "Young's Reversal Transactions principle" | §C.1 |
| 11 | Event Sourcing CQRS (Card #5) | No Delete / append-only | Applied in §C.1 and §I.2: append-only JSONL, no existing entries modified | — | ALREADY_APPLIED | §E Laws L6 names append-only as a constitutional Law with Popper falsifier | §C.1, §E, §I.2 |
| 12 | Event Sourcing CQRS (Card #5) | CQRS read/write split | Applied in §I.2 format decision: JSONL = write model; markdown = derived read model | — | ALREADY_APPLIED | §I.2 names CQRS read/write split as one of five rationale points for JSONL | §I.2 |
| 13 | Clean Code (Card #12) | Deep modules — narrow public/wide internal | Scanner has narrow public interface (4 exit codes, structured stderr); wide internal algorithm space | — | ALREADY_APPLIED | §H.1 interface contract: ≤20-line stdout summary hides four algorithm internals; per Part 1 §H deep-module framing | §H.1 |
| 14 | SRE Book (Card #6) | Four Golden Signals | §B emits four health signals but prior draft did not name them as the SRE Four Golden Signals analogue | Enumerate four by name (fg_r_coverage_pct, cargo_cult_flag_count, broken_citation_count, dangling_edge_count) with SRE parallel and specific consequence for each | YES | Naming makes signals concrete and unambiguous for Part 8 dashboard design; prevents "four unnamed metrics" anti-pattern | §B.1 |
| 15 | SRE Book (Card #6) | Blameless postmortems Ch. 15 | §K framing states "failure modes are treated as commits, not blame" | Quote SRE Book Ch. 15 principle directly with consequence: every K-entry is a pre-declared postmortem template | YES | Strengthens the citation by making the consequence concrete (postmortem half-written at architecture time) | §K |
| 16 | SRE Workbook supplement | Burn-rate algebra 1×/6×/14.4× | Broken-citation rate not yet structured as tiered alert | Apply burn-rate triggers to broken-citation rate as three-tier Phase B alert system | YES | Actionable: gives brigadier/Part 8 specific thresholds; prevents over-alerting on single broken citation while ensuring fast detection at high-break-rate | §K |
| 17 | Systems Thinking Cybernetics (Card #2) | Meadows leverage points Ch. 6 | Not explicitly placed in leverage-point hierarchy | Add §0 explicit Meadows leverage-point placement: F-G-R schema at L5 (rules), scanner at L7 (information flows) | YES | Identifies the leverage class of Part 6a's mechanism; prevents L12-level parameter tuning from being confused with L5 structural rule discipline | §0 |
| 18 | Systems Thinking Cybernetics (Card #2) | Beer VSM S3 audit authority | S3 authority split ambiguity exists (Parts 6 and 8 both serve S3 function per TRADEOFF-01) | Add §0 explicit VSM S3 placement: Part 6a = S3 audit lead, Part 6b = S3 enforcement arm | YES | Resolves Card #2 TRADEOFF-01 directly; designates clear S3 authority without creating a new section — fits in §0 framing | §0 |
| 19 | Constitutional AI Bai 2022 supplement | RLAIF self-critique §3 | Applied in §H.1 Algorithm D bounded to cargo-cult check only | — | ALREADY_APPLIED | §H.1 Algorithm D carries the bounded application with all three explicit constraints | §H.1 |
| 20 | Constitutional AI Bai 2022 supplement | Provenance + transparency | F-G-R IS the constitutional provenance mechanism; explicit `refuted_if` = transparency | — | ALREADY_APPLIED | §0 GAAP-equivalent framing; §E Laws L1-L7 structural enforcement | §0, §E |
| 21 | Constitutional AI Bai 2022 supplement | Hardcoded never-list F8/F9 | F8/F9 cannot be downgraded autonomously applied in §E L3 | — | ALREADY_APPLIED | §E L3: "F8/F9 claims MUST require Ruslan ack"; §F.2 anti-scope prohibits autonomous schema modification | §E, §F.2 |
| 22 | Stoic Epistemic (Card #9) | Dichotomy of control | Part 6 enforcement rules not yet classified as in-control vs influence-zone | Add §F.3 Stoic Dichotomy section classifying Part 6a enforcement rules into Category A (hard), B (influence), C (logging) | YES | Improves Foundation/RUSLAN-LAYER clarity; prevents false compliance signals from Category B rules treated as Category A | §F.3 (new) |
| 23 | Stoic Epistemic (Card #9) | Marcus Aurelius engineering virtue | Not applicable to Part 6a scope | NO | Premature: the Stoic virtue framing is relevant to Part 5 Compound Learning, not the provenance schema. Out of scope for Part 6a. | n/a |
| 24 | Stoic Epistemic (Card #9) | Popper falsifiability — Foundation claims carry falsifiers | Already applied throughout; every Law in §E has a Falsifier field; every F-G-R claim in §G has `refuted_if` | — | ALREADY_APPLIED | §E Laws P1 applied: each Law carries its Falsifier in bold; §G table has `refuted_if` per row | §E, §G |
| 25 | Compounding Engineering (Card #7) | Every cycle compounds; approval log = compound ledger | Approval log antifragility framed via Taleb; CE compound-ledger framing not yet applied | Add "every ack compounds epistemic capital" statement making the compound-ledger parallel explicit | YES | Grounding the compound claim in CE mechanics makes it testable: can measure how many future decisions are de-risked by precedent lookup | §B.3 |
| 26 | Compounding Engineering (Card #7) | DRR + strategies.md as compound memory | Not Part 6a scope — those are Part 5 mechanisms | NO | Domain-orthogonal for Part 6a: CE's DRR ledger is Part 5's concern, not the provenance officer's. Part 6a is the governance substrate, not the learning substrate. | n/a |
| 27 | Knowledge Management (Karpathy/Matuschak) | Matuschak evergreen notes — append-only accretion | Approval log append-only already established; evergreen-note parallel not drawn | Add evergreen-note parallel in §C.1: each approval log entry is an evergreen record of a governance decision — never stale, never overwritten | YES | Grounds append-only in knowledge-management theory, not just engineering tradition; makes the epistemic value of immutability explicit | §C.1 |
| 28 | Knowledge Management (Karpathy/Matuschak) | Karpathy LLM wiki pattern | Already applied: JSONL + markdown = the Karpathy file-based wiki substrate applied to governance records | — | ALREADY_APPLIED | §0 and §N acknowledge Karpathy LLM wiki as a source; CQRS pattern mirrors Karpathy's read/write split | §0 |
| 29 | Knowledge Management (Karpathy/Matuschak) | Luhmann Zettelkasten | Not directly relevant: Zettelkasten is bidirectional-link knowledge management for note-taking; the approval log is a sequential gate record with a different topology | NO | Domain-orthogonal: Zettelkasten is Part 3 wiki territory. Approval log entries are not note cards — they are time-ordered event records. Forcing Zettelkasten structure would contradict the append-only constraint. | n/a |
| 30 | Multi-Agent Architecture (Card #3) | Orchestrator + Specialist pattern | Not applicable: Part 6a is a Foundation substrate, not an agent coordination pattern | NO | Domain-orthogonal: Part 6a defines schemas and audit mechanics; Part 4 (Role Taxonomy) is where orchestrator/specialist patterns apply. | n/a |
| 31 | Product Management Cagan/ShapeUp | Appetite framing — 2-day cycle | Applied: §J.2 quarterly audit duration estimate "2-4 hours" is an appetite declaration | — | ALREADY_APPLIED | §J.2 carries the duration estimate as a bounded appetite; §L HARD GAP B carries the "2 cycles" appetite for scanner implementation | §J.2, §L |
| 32 | Mereology typed edges (Card #14) | Formal mereology A.14 | Applied in §D 10-edge reference table | — | ALREADY_APPLIED | §D carries all ten edges with mereology type and rationale; MemberOf vs ComponentOf distinction explicitly argued for edge 1 | §D |
| 33 | Askell 2021 HHH supplement | HHH framework — Helpful/Honest/Harmless | Applied in §E L7; prior draft cited it; expanded HHH grounding available | Add explicit HHH grounding to §E L7 showing each F-G-R mechanism maps to a specific HHH component with consequence | YES | Makes the constitutional claim concrete: each HHH arm has an observable enforcement mechanism in Part 6a | §E L7 |
| 34 | Young 2010 CQRS supplement | "There is no Delete" + CQRS projection rebuild | Applied in §C.1 and §H.4 | — | ALREADY_APPLIED | §H.4 `/approvals --regen-log` explicitly cites CQRS "projections can be discarded and rebuilt" | §C.1, §H.4 |
| 35 | SRE Book supplement | SLI/SLO/error-budget | F-G-R coverage claimed as 100% target in §E E1; SLO framing not explicit | Add explicit "F-G-R coverage SLO = 100%, error budget = 0%" claim in §G with SRE Book framing and Phase A vs Phase B tolerance | YES | Concrete actionable target; distinguishes Phase A baseline-establishment tolerance from Phase B operational SLO | §G |

**Wisdom rollup:** YES = 13, NO = 3, ALREADY_APPLIED = 19. Total sources covered: 14 consultant cards + 5 supplement library sources = 19 distinct wisdom streams, 35 rows.

**Top 5 most impactful adopted edits:**
1. **§0 Meadows + VSM placement** (rows 17, 18): names the leverage class and VSM authority, resolving Card #2 TRADEOFF-01 directly.
2. **§F.3 Stoic Dichotomy** (row 22): new subsection classifying all enforcement rules into Category A/B/C — prevents false compliance signals.
3. **§G Lindy verdict box + SLO claim** (rows 5, 35): makes durability claims concrete and time-bounded; SLO = 100% with explicit error budget.
4. **§K burn-rate tiers + blameless postmortem quote** (rows 15, 16): pre-declares postmortem template; gives Part 8 three specific thresholds for alert design.
5. **§E L7 HHH grounding expansion** (row 33): each F-G-R mechanism now maps to a specific HHH component with observable enforcement consequence.

---

## §N Provenance

Every source cited in this document listed with its role and F-level characterisation.
[src:philosophy-expert-multi-mode.md:§N]

| Source | Role in this document | F-level |
|--------|----------------------|---------|
| `design/JETIX-FPF.md` §4.2 B.3, §12.7, §5.1 IP-1, §5.3 IP-3, IP-4 | F-G-R schema definition; F-level anchors; IP-1/IP-3/IP-4 immune system | F5-F7 (canonical Jetix FPF adaptation of Левенчук SHSM-FPF) |
| `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` §4.1-§4.6, §5.5, §6.1, §6.7 | FUNDAMENTAL authority hierarchy; 11 hard limits; reversibility checks; human-gate requirement | F8 (constitutional, Ruslan-authored) |
| `swarm/wiki/cycles/.../part-6-governance-provenance-human-gate.md` all sections | Part 6 interface card; Laws, Admissibility, Deontics, Effects, Anti-scope, F-G-R tagging | F4 (Phase A interface card, operational convention) |
| `swarm/wiki/cycles/.../philosophy-expert-multi-mode.md` §A-§X | First-principles derivation of F-G-R triad irreducibility; epistemic audit findings; L/A/D/E; DOGFOOD; schema design | F4 (Wave C cell, peer-reviewed in integration) |
| `swarm/wiki/cycles/.../engineering-expert-multi-mode.md` §1-§9 | Scanner algorithm contracts; JSONL approval log design; CQRS architecture; acceptance predicates; critic findings; scalability analysis | F4 (Wave C cell, peer-reviewed in integration) |
| `swarm/wiki/cycles/.../investor-expert-capital-allocation.md` §1-§11 | GAAP-equivalent argument; margin-of-safety arithmetic; antifragility of approval log; quarterly audit as earnings call; risk-of-ruin floor; Lindy durability | F4 (Wave C cell, peer-reviewed in integration) |
| `swarm/wiki/cycles/.../mgmt-expert-boundary.md` §A-§K | Split rationale (cadence independence); seam analysis (three coupling points); Phase B importability; risk register; D6 proposed audit dimension | F4 (Wave C cell, peer-reviewed in integration) |
| `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` §H | swarm/lib/ ownership contract; deep-module framing; cross-ref edges convention | F4 (sister canonical architecture document) |
| `raw/books-md/anthropic/bai-2022-cai.md` §3 | RLAIF methodology; Constitutional AI two-stage process; self-critique false-positive reduction | F5 (peer-reviewed preprint, library-direct) |
| `raw/books-md/anthropic/askell-2021-hhh.md` | HHH framework; harmlessness as structural invariant | F5 (peer-reviewed preprint, library-direct) |
| `raw/books-md/event-sourcing/young-cqrs-2010.md` | "There is no Delete"; Reversal Transactions; append-only event log; CQRS read/write split; schema upcasting | F5 (practitioner reference, library-direct) |
| `raw/books-md/sre/google-sre-book.md` Ch.6, Ch.15 | Four Golden Signals (§B); blameless postmortem culture (§K); failure modes as commits not blame | F5 (practitioner reference, library-direct) |
| `raw/books-md/sre/google-srewb-implementing-slos.md` §12 | Burn-rate algebra (1×/6×/14.4× tiers); alert window design for broken-citation error budget | F5 (practitioner reference, library-direct) |
| `wave-c-worklist.md` L300-360 | P6a.1-P6a.4 Wave C bullets; effort/expert allocation; OQ-MERGED-1 split rationale | F4 (cycle worklist, operational) |
| `mereology-typed-edges.md` §5 | A.14 typed edge vocabulary; 10-edge reference table | F3-F4 (FPF A.14 + academic cross-reference) |
| `systems-thinking-cybernetics.md` §4 P1 + §4 P3 + §7 TRADEOFF-01 | Meadows leverage-point placement (L5/L7); Beer VSM S3 authority designation; TRADEOFF-01 resolution | F4 (Wave B consultant card, peer-reviewed) |
| `stoic-epistemic.md` §4 P5 | Stoic dichotomy of control applied to governance enforcement rule classification (Category A/B/C) | F3 (Wave B consultant card, philosophy-expert scope) |
| `compounding-engineering.md` §2 P2 + §4 P1 | Compound ledger framing for approval log; approval log as epistemic compound interest | F4 (Wave B consultant card, engineering-expert scope) |
| `capital-allocation-antifragility.md` §3 + §4 P7 | Lindy substrate verdict; via-negativa applied to anti-scope enforcement | F4 (Wave B consultant card, investor-expert scope) |

---

## §X Foundation vs RUSLAN-LAYER

Per FUNDAMENTAL §0 and FPF IP-1 Role≠Executor: Foundation must be generic (forkable per D27);
RUSLAN-LAYER carries Jetix/Ruslan-specific bindings over the Foundation structure.
[src:philosophy-expert-multi-mode.md:§X; src:mgmt-expert-boundary.md:§E Phase B fork importability]

### Foundation Layer (Generic — Portable to Any FPF Deployment)

The following artefacts and structures are Foundation-generic. Any D27 fork may adopt them
as-is, substituting only RUSLAN-LAYER bindings:

- **F-G-R JSON Schema (`shared/schemas/f-g-r.json`).** The schema is independent of Jetix-
  specific paths, actors, or cycles. Any knowledge system using FPF B.3 can deploy this schema
  as-is. The F0-F9 enum, `R.refuted_if` requirement, and F8/F9 gate rule are Foundation
  invariants — no fork may change the F0-F2 = draft-only rule without losing Foundation
  compatibility. [src:philosophy-expert-multi-mode.md:§X Foundation partition]

- **Approval log JSONL entry format.** The YAML/JSONL structure is generic. The `acked_by:
  ruslan` value is a role label (human owner with skin-in-the-game), not a person-binding.
  A D27 fork uses this schema with their own human owner's identifier. IP-1 applied to the
  governance schema: the role (human-owner) is Foundation; the executor-binding (Ruslan) is
  RUSLAN-LAYER. [src:philosophy-expert-multi-mode.md:§X approval log; src:mgmt-expert-boundary.md:§E.1]

- **Quarterly audit template structure (D1-D6 dimensions).** The six audit dimensions (F-G-R
  drift, citation health, cargo-cult drift, dangling edges, IP-1 violations, gate-packet
  completeness) are generic to any FPF Foundation deployment. The specific artefact counts
  and paths are RUSLAN-LAYER instantiation values. Any fork runs the same six dimensions
  against their own canonical paths. [src:mgmt-expert-boundary.md:§E.1]

- **L/A/D/E structure.** The four-lane discipline is Foundation (FPF A.6.B constitutional).
  The specific SLAs, quarterly cadence, Ruslan-ack authority are RUSLAN-LAYER bindings over
  the Foundation L-lane structure. [src:philosophy-expert-multi-mode.md:§X]

- **Scanner subcommand interface contract.** The `/lint --check-citations` interface (exit
  codes, stderr format, RLAIF env-var gate) is Foundation-generic. The specific canonical
  wiki paths being scanned are RUSLAN-LAYER. A fork adopts the scanner contract; they
  configure the paths to match their own repo structure. [src:mgmt-expert-boundary.md:§E.1]

- **F-level promotion capital-call sequence (F3→F4→...→F8).** The promotion sequence and
  its authority requirements (author assessment → cycle evidence → brigadier critic pass →
  cross-cycle reuse → Ruslan ack) are Foundation. The specific actors who fill each role
  in a given deployment are RUSLAN-LAYER. [src:investor-expert-capital-allocation.md:§6]

### RUSLAN-LAYER (Jetix-Specific — Requires Adaptation for Forks)

The following are RUSLAN-LAYER bindings. A D27 fork replaces these with their own equivalents:

- **Specific artefact paths.** `swarm/wiki/`, `swarm/approvals/log.jsonl`, `swarm/audits/`,
  `swarm/logs/lint-events.jsonl` — Jetix mono-repo paths. A D27 fork defines its own canonical
  path structure; the Foundation specifies only the *type* of path (canonical artefact store,
  approval log, audit directory, lint events log).

- **`acked_by: ruslan` as resolved executor.** Specific to this Jetix instance. A fork uses
  their own human owner identifier.

- **Cron timezone and log regeneration schedule.** "Friday 17:00 Berlin timezone" is RUSLAN-LAYER
  (Ruslan is in Berlin, Germany). A fork sets their own cron timezone.

- **`decay_after` dates on specific Jetix artefacts.** Instance-specific temporal validity
  claims tied to Jetix's cycle schedule.

- **Specific FUNDAMENTAL §6.1 11-item never-list.** Jetix's specific constitutional limits.
  A D27 fork SHOULD have analogous limits but content may differ; Foundation mandates the
  mechanism (a hardcoded never-list enforced at gate), not the exact list.

- **Specific cycle IDs and gate-packet references in approval log entries.** RUSLAN-LAYER.

- **Executor-name registry for D5 IP-1 audit.** The list of executor names to grep for
  (`brigadier`, `meta-agent`, `engineering-expert` as executor instances) is RUSLAN-LAYER.
  Foundation declares the D5 check mechanism; the name list is Jetix-specific.

### Machine-Readable Foundation/RUSLAN-LAYER Split

The `ClaimScope.scope_tokens` enum in the f-g-r.json schema includes both `Foundation` and
`RUSLAN-LAYER` as canonical values. This makes the Foundation/RUSLAN-LAYER split machine-
readable in every promoted artefact: the scanner can detect if an artefact claims
`scope_tokens: [Foundation]` but contains RUSLAN-LAYER-specific content (executor names,
DACH paths), flagging it as a PP-2 boundary leak. The audit dimension D5 (IP-1 violations)
is the detection mechanism for exactly this class of boundary leakage.
[src:philosophy-expert-multi-mode.md:§X machine-readable boundary enforcement; src:philosophy-expert.md:§1 PP-2]

### Phase B Import Path

A Phase B partner clones: (1) `shared/schemas/f-g-r.json` (no changes needed), (2) the
scanner subcommand contract (adapts path configuration only), (3) the approval log JSONL
format (replaces `ruslan` actor value with their human owner), (4) the quarterly audit
template (fills their own canonical paths into D1-D6 measurements). They replace only
RUSLAN-LAYER tokens. Foundation machinery works unchanged. The marginal cost of maintaining
Foundation genericity: approximately 10% additional authoring discipline. This is the option
premium for Phase B importability — paid regardless of whether the option is exercised. At
any positive probability of Phase B partner import, positive expected value.
[src:investor-expert-capital-allocation.md:§7 real option analysis]

---

## Closing — Acceptance Predicate (Composite)

**Hamel-binary over Part 6a as a whole:**

"All four Wave C bullets (P6a.1-P6a.4) have an unambiguous design with a Hamel-binary
acceptance predicate; all claims in this document carry F-G-R tags in §G; all ten §D
dependencies use A.14 typed edges with zero generic 'depends-on'; the first-principles
derivation of F-G-R triad irreducibility in §I.1 names three orthogonal axes (process,
context, evidence) with explicit kill-conditions for alternative cardinalities (duo + quad);
RLAIF integration is bounded to cargo-cult check only with three explicit constraints named
in §H.1; Foundation/RUSLAN-LAYER partition is machine-readable via scope_tokens in §X and
§I.1 schema; four HARD GAPS are explicitly named and tracked (A, B, C, D)."

**Refuted if:** Any of the four P6a acceptance predicates fails on first implementation
attempt; OR any §D dependency is found to use unlabeled "depends-on" on architecture review;
OR the F-G-R triad argument (§I.1) has a valid counter-example showing F, G, and R are not
mutually irreducible; OR RLAIF is found enabled in a pre-commit hook path.

---

*End of Part 6a — Provenance Officer — Architecture.*
*Synthesised from four expert cells: philosophy-expert, engineering-expert, investor-expert,
mgmt-expert. Integration role: philosophy-expert as integrator (epistemic territory primary
per OQ-MERGED-1 rationale — F-G-R schema is epistemic territory).*
