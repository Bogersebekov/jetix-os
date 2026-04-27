---
title: Part 1 — mgmt-expert boundary cell
date: 2026-04-28
phase: C-1-cell
expert: mgmt-expert
modes: [boundary]
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 1
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-1-system-state-persistence.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/mgmt-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md
F: F4
ClaimScope: "Holds for Part 1 interface card as authored in Wave A/B. Does not govern RUSLAN-LAYER executor bindings or cross-fork architecture decisions (those are explicitly Phase-B deferred)."
R: "Refuted if Part 1 architecture.md, once written, introduces L/A/D/E lane bleed, scope encroachment into Part 6 or Part 8 territory, or admissibility gaps identified below. Accepted if Wave C architecture.md closes the three flagged gaps without opening new lane violations."
provenance_inline: true
produced_by: mgmt-expert
mode: boundary
---

# Part 1 — mgmt-expert Boundary Cell
## Wave C Bundle 1 — System State Persistence

---

## §1 L/A/D/E Lane Crispness Audit

[src:part-1-system-state-persistence.md:§E] [FPF §4.3 CP-3; levenchuk-shsm-fpf.md:§4 P6]

### Laws

The interface card declares four Laws in §E. Evaluated against the Hamel-binary test (single-line, holds or does not hold, no prose hedge):

**Law 1 — "Every canonical state change is a committed file."**
[src:part-1-system-state-persistence.md:L80-81]
Binary status: PASSES. The predicate is checkable by `git log --oneline` — if an artefact exists with no commit in history, the Law is violated. Measurable. Consequence sentence: violated Law 1 means the system operates with shadow state; any Part depending on git provenance breaks silently.

**Law 2 — "Commit messages MUST follow `[area] verb what (why)` format."**
[src:part-1-system-state-persistence.md:L81-82]
Binary status: PASSES in intent. BUT: currently convention-only, not machine-enforced in Phase A. The hook layer (OPP-02) is log-only per cycle-2 implementation. The Wave C worklist explicitly names this gap (Bullet 2: D25 commit-format lint rule as Foundation artefact). Until Bullet 2 closes, Law 2 is a declared invariant without an enforcement substrate — it is aspirationally binary but operationally unenforced. Consequence: a single non-compliant commit passes through undetected; Wave C closes this via lint signal #12. **Gap flagged: Law 2 is not yet machine-checkable; Wave C Bullet 2 is the closure vehicle.**
[src:wave-c-worklist.md:L77-86]

**Law 3 — "Notion is a read-display layer only."**
[src:part-1-system-state-persistence.md:L82-83]
Binary status: PASSES. Verifiable by grep-scan for Notion write paths in any committed skill or hook. Consequence: Notion write path would bifurcate state — Part 1's audit trail would diverge from Notion display state within one cycle.

**Law 4 — "No --amend, --no-verify, force-push on canonical branch."**
[src:part-1-system-state-persistence.md:L83-84]
Binary status: PASSES structurally. Git branch protection can be verified via repo config. Consequence: violated Law 4 rewrites history — git fsck would not detect it; commit hashes referenced in downstream artefacts would become orphaned.

**Overall Laws verdict: 3/4 binary-checkable NOW. Law 2 requires Wave C Bullet 2 closure before it is machine-checkable. No Law is prose-only; all carry consequence sentences. CLEAN with one tracked gap.**

---

### Admissibility

The interface card states two Admissibility criteria: (a) valid path under repo root, (b) schema validation where applicable, (c) human-ack receipt from Part 6 for promotion events.
[src:part-1-system-state-persistence.md:L85-88]

**Admissibility gap A — file-size limit absent.**
No maximum file size is declared. A Part 9 daily log that grows unbounded (e.g., a 50MB voice transcript committed raw) passes Admissibility criterion (a) (valid path) but violates the spirit of the ≤80-line `/company-status` snapshot SLI and the lean-commit discipline. Recommended addition: "Input files exceeding 1MB committed directly to canonical paths require explicit `[large-file]` tag in commit message; binary files exceeding 10MB require HITL ack before commit." This is an Admissibility-lane addition, not a new Law.

**Admissibility gap B — encoding not specified.**
UTF-8 is declared in CLAUDE.md as the file encoding standard [src:CLAUDE.md Global Rules] but is not enumerated in Part 1's Admissibility lane. A non-UTF-8 file would pass the path-validity check but corrupt downstream text-processing tools. Consequence: `/lint` passes on a Latin-1 encoded file and later downstream failures trace to no single commit. Recommended addition to Admissibility lane: "Input must be UTF-8 encoded text OR explicitly declared binary with MIME type annotation in commit message."

**Admissibility gap C — binary-vs-text discrimination absent.**
The current criteria do not distinguish binary commits (images, compiled artifacts) from text commits (Markdown, YAML, JSON). Binary files cannot be diffed, cannot be inline-cited via line ranges in `[src:]` citations, and break the IP-3 writing-as-thinking substrate. [FPF §5.3 IP-3; levenchuk-shsm-fpf.md:§4 P2] Recommended addition: "Binary commits MUST include a machine-readable descriptor commit in the same atomic operation naming the binary's provenance and its referencing text artefact."

**Overall Admissibility verdict: 3 gaps identified (file size, encoding, binary/text). None are blocking for current Phase A operations. All 3 are S-effort additions for the architecture.md §A section. Flag for Wave C architecture author.**

---

### Deontics

Three Deontics are declared. Evaluated for testability:

**Deontic 1 — "Preserve every committed state indefinitely."**
[src:part-1-system-state-persistence.md:L91]
Testability issue: "indefinitely" is not time-bounded. This is the most significant Deontics-lane gap in the interface card. "Indefinitely" is not a measurable SLI; it cannot be violated in a testable sense until state is actually lost. Recommended conversion: "MUST preserve every committed state with ≥99.999% durability over a rolling 10-year horizon (5 nines; FUNDAMENTAL §5.1 Tier 0 binding); concrete implementation: git remote backup verified weekly via `git fsck` with 0 object-error target." This converts "indefinitely" to a measurable SLI with a named cadence. [src:part-1-system-state-persistence.md:L98 "0 object errors" — correct target, but cadence absent] F-tag: F4 (operational convention, not yet KPI-tracked).

**Deontic 2 — "Expose a queryable log."**
[src:part-1-system-state-persistence.md:L92]
Binary and testable. `git log` either responds within acceptable latency or it does not. No gap.

**Deontic 3 — "Provide reversibility via `git revert`."**
[src:part-1-system-state-persistence.md:L93]
Binary and testable. The prohibition on `git reset` (destructive) vs `git revert` (constructive inverse commit) is auditable. No gap.

**Overall Deontics verdict: 2/3 testable as-written. Deontic 1 requires "indefinitely" → SLI conversion (99.999% / 10-year / weekly fsck) before the architecture.md can declare it an enforceable obligation. Gap flagged for Wave C architecture author.**

---

### Effects

Three Effects are declared:
[src:part-1-system-state-persistence.md:L95-98]

**Effect 1 — "Artefact durable within 1 second of commit."** Binary. Good.
**Effect 2 — "≤80-line `/company-status` snapshot, zero network calls."** Binary. Good.
**Effect 3 — "0 object errors via `git fsck`."** Binary target. Gap: cadence is not specified. `git fsck` is named but when it runs is not declared. Consequence: 0-error target is only enforceable at point-in-time checks; a repo with gradual corruption would pass every ad-hoc fsck while drifting toward failure.

Recommended addition to Effects: "Weekly `git fsck` cron (suggested: Sunday 02:00 system time); result appended to `shared/state/system-health.json` under `git_integrity` key; non-zero error count triggers Part 8 health alert pipeline." This crosses into Part 8 territory for the alert routing, but the *emission* of the signal (running fsck, writing to system-health.json) is Part 1's obligation. The SLO threshold and alert-routing are Part 8's.

**Overall Effects verdict: 3/3 binary targets. One cadence gap (fsck). Signal emission is Part 1; SLO contract is Part 8. CLEAN with cadence note.**

---

## §2 Self-Exemplification Check

[src:part-1-system-state-persistence.md; FPF §4.3 CP-3]

Does the interface card itself follow Part 1's discipline?

- The interface card is committed via git per D25 [src:part-1-system-state-persistence.md:L11 `fpf_anchor: D25`]. PASS.
- Every claim in the card cites a source with consequence sentence [src:part-1-system-state-persistence.md:L37,48,58,70,88 — inline [src:] citations throughout]. PASS.
- The card is a Foundation artefact (phase: A-2) in the repo. PASS.
- F-G-R frontmatter is present in the card's own header [src:part-1-system-state-persistence.md:L12-14 F:F4, ClaimScope, R fields]. PASS.
- The card's §E L/A/D/E section is structured by lane (Laws / Admissibility / Deontics / Effects), not as a monolithic contract block. [FPF-Spec A.6.B; levenchuk-shsm-fpf.md:§4 P6 AP-L4 check] PASS — AP-L4 does not fire.

**Self-exemplification verdict: CLEAN. The interface card is its own proof-of-concept. A Phase B partner reading it sees the discipline modelled in the artefact that specifies the discipline.**

One note: the card does not contain an explicit sentence stating "this card itself follows the L/A/D/E discipline it enforces." This is a mirror self-exemplification note (analogous to Part 6's self-exemplification per the mission brief). Recommended addition to §E: a one-sentence assertion — "This interface card is itself a Part 1-governed artefact: it is committed via git, carries F-G-R frontmatter, uses [src:] inline citations, and its §E section follows A.6.B L/A/D/E lane separation." The addition is cosmetic but operationally useful for Phase B onboarding.

---

## §3 Phase B Fork Import Readability

[src:wave-c-worklist.md:L62-75; levenchuk-shsm-fpf.md:§4 P6]

Hypothesis: a Phase B partner (a competent engineer unfamiliar with this repo) should be able to read Part 1's architecture.md cold and within 90 minutes achieve three outcomes. Evaluated against the interface card as the architecture.md precursor:

**Outcome (a) — Understand Part 1's contract surface (§A–§F crisp).**
Current status: §A (Inputs), §B (Outputs), §C (Side-effects), §D (Dependencies), §E (Boundary), §F (Anti-scope) are all present and legible. The Inputs and Outputs sections use the `<source> :: <data-shape> :: <event-trigger>` format consistently [src:part-1-system-state-persistence.md:L32-48]. The dependency section explains WHY no upstream dependencies exist (substrate principle) — not just asserts it [src:part-1-system-state-persistence.md:L66]. This is rare and valuable for onboarding.
**Verdict: achievable within 30 minutes for outcome (a). PASS.**

**Outcome (b) — Implement their own Part 1 in a fork.**
Current status: the interface card names the commit format, the path exclusions, and the reversibility mechanism. However, §H (code-level interfaces) is sparse — the card names `/company-status` and `/knowledge-diff` as outputs but does not specify their invocation contracts (parameters, exit codes, output schema). The Wave C architecture.md must add an §H section with: (i) `git commit` hook spec (what the pre-commit hook validates), (ii) `/company-status` output schema (the ≤80-line format, field definitions), (iii) `/knowledge-diff` date-range parameter contract.
Without §H specificity, a fork implementor knows *what* Part 1 does but not *how to implement* the observable surface.
**Verdict: achievable within 90 minutes ONLY IF Wave C architecture.md adds concrete §H code-level interface specs. Gap flagged.**

**Outcome (c) — Integrate with Jetix-side Part 1 via D27 cross-fork provenance.**
Current status: D27 is explicitly Phase-B deferred per Wave C Bullet 1 [src:wave-c-worklist.md:L66-75]. The stub will declare (a) required fields for cross-fork commit traceability, (b) audit-trail fragmentation points, (c) explicit `decisions/policy/` entry marking Phase-B. A partner reading the stub will understand the gap is intentional, not accidental. But they cannot integrate cross-fork in Phase A.
**Verdict: NOT achievable in Phase A by design. Appropriately bounded. CLEAN deferred-scope.**

**Phase B import readability verdict: Two gaps requiring Wave C closure: (1) §H code-level interface specs, (2) the self-exemplification sentence in §E. One intentional gap (D27 cross-fork) correctly deferred. If §H is present in architecture.md, a competent Phase B partner can fork and implement in one day.**

---

## §4 Scope Boundary vs Part 6 (Governance)

[src:part-1-system-state-persistence.md:§F; candidate-parts-merged.md:§2 Part 6]

Part 1 §F Anti-scope explicitly declares: "This part does NOT enforce commit message content correctness — that is Part 6 responsibility via lint." [src:part-1-system-state-persistence.md:L110] This is the correct partition: Part 1 enforces the physical format invariant (`[area] verb what (why)` as a structural pattern); Part 6 evaluates whether the message accurately describes the change (semantic correctness, link to acceptance predicate, Hamel-binary form).

The partition is clean and the anti-scope entry is explicit. No bleed detected. The only risk of bleed is if Wave C Bullet 2 (commit-format lint rule as Foundation artefact) is implemented incorrectly — if the lint rule checks semantic accuracy rather than format compliance, it would cross into Part 6 territory. The Wave C architecture author must constrain Bullet 2 to format-only checks (regex on `[area] verb what (why)` structure; enumerated area tokens; minimum word count for `why` clause). Semantic evaluation of commit content remains Part 6.

**Part 1 / Part 6 boundary verdict: CLEAN. Explicit anti-scope entry. Wave C Bullet 2 implementation must stay format-only to preserve this clean boundary.**

---

## §5 Scope Boundary vs Part 8 (Health Monitoring)

[src:part-1-system-state-persistence.md:§B; FUNDAMENTAL §3]

Part 1 §B Outputs names "repo integrity metrics (commit cadence, branch status, backup SLI)" as a signal emitted to Part 8. [src:part-1-system-state-persistence.md:L47] This correctly positions Part 1 as signal *emitter* and Part 8 as signal *consumer and SLO-contract holder*.

The Effects lane (§E) names "0 object errors" as the target [src:part-1-system-state-persistence.md:L98] but does NOT specify the SLO threshold, alert conditions, or error-budget burn policy. These are correctly absent — they belong to Part 8. No bleed detected.

Boundary clarity check: Part 1 runs `git fsck`, writes the result to `shared/state/system-health.json`, and emits a health-poll event. Part 8 reads `system-health.json`, evaluates against its declared SLO threshold, and triggers alerting if threshold is breached. The handoff point (the `shared/state/system-health.json` write) is Part 1's terminal action. Everything downstream is Part 8.

**Part 1 / Part 8 boundary verdict: CLEAN. The interface card does not specify SLO thresholds. The cadence gap (when fsck runs) is Part 1's own operational obligation — once the cadence is added, the boundary remains clean because Part 1 only emits; Part 8 interprets.**

---

## §6 Cagan / Shape Up — Appetite Framing for Wave C Build

[src:product-management-cagan-shape-up.md:§4 Principle 2; wave-c-worklist.md:L60-62]

The worklist characterises Part 1 as "~S-M total" effort for Wave C. [src:wave-c-worklist.md:L60] The three bullets are: (S) commit-format lint rule Foundation artefact, (S) inline [src:] citation standardisation for Parts 7/8/9, (M) cross-fork provenance schema stub. The architecture.md itself (15-25K word target across the full Foundation) is a substantial document.

Shape Up discipline demands an explicit appetite for every commitment. [src:product-management-cagan-shape-up.md:§4 Principle 2: "Fixed time, variable scope"] Applied to Wave C Part 1:

**Appetite declaration for Wave C Part 1 architecture.md build: 2 working days maximum.** Scope-hammering rule: if the architecture.md prose is not draft-complete within 1.5 days, cut §J (Operational rituals) and §I (Cross-fork schema stub) down to stub form only — do not extend the timeline. The appetite is 2 days because Part 1 is the most operationally mature part (the substrate already exists and runs; this is documentation and gap-closure, not implementation).

**Realistic assessment:** 15-25K words for the architecture.md across all 10 parts averages 1500-2500 words per part. Part 1, being the substrate, may require 2500-3500 words to cover §A-§J with code-level interface specs (§H). That is achievable in 2 days of focused writing. The appetite is not unrealistic IF Wave C does not expand the scope of what Part 1 must address beyond the 3 worklist bullets plus standard §A-§J structure.

**Scope-balloon risk:** The cross-fork provenance stub (Bullet 1) is the highest risk of over-elaboration. The Wave C worklist explicitly says "do NOT implement; declare the gap" [src:wave-c-worklist.md:L71]. Shape Up's scope-hammering rule applies: if the stub begins requiring design decisions (schema field semantics, reconciliation algorithms), cut to a one-page declaration with explicit Phase-B labels and move on.

---

## §7 Risk Register — Boundary-Violation Risks

F-tag all risks per B.3 discipline: [FPF §4.2 CP-2]

**Risk R-1 — Sales motion requests commit tagging with CRM entity IDs.**
Scenario: sales-lead requests Part 1 auto-tag commits referencing CRM records with `[crm-entity:<slug>]` suffix to enable CRM-to-commit traceability.
Lane violation: this would expand Part 1's Admissibility lane to evaluate commit-message semantic content (CRM entity ID validity) — that is Part 6 (Governance) territory.
Response: REJECT. Part 1 enforces structural format only. CRM-to-commit tracing is a Part 6 cross-reference convention, not a Part 1 input acceptance rule.
F: F3. ClaimScope: holds for consulting-motion Phase A. R: refuted if a specific audit requirement (e.g., GDPR Art. 17 deletion tracking) mandates CRM-entity tagging at commit level — then escalate to HITL for Lock modification.

**Risk R-2 — Engineering proposes Part 1 emit Slack/Notion notifications on commit.**
Scenario: engineering-expert optimizer proposes adding Slack webhook calls to the post-commit hook as a "delivery velocity signal" for stakeholders.
Lane violation: Notion and external services are explicitly excluded from Part 1's write path per Law 3 [src:part-1-system-state-persistence.md:L82-83] and anti-scope §F [src:part-1-system-state-persistence.md:L112]. Slack notification is an external-service write.
Response: REJECT. Notification routing is Part 8 (Health Monitoring) or Part 9 (Owner Interaction Scaffold) territory, not Part 1's. Part 1 emits to `shared/state/system-health.json`; other parts decide notification channels.
F: F4. ClaimScope: holds for all Phase A external-service integration proposals. R: refuted only if a Foundation Lock is added specifically permitting post-commit webhook writes (currently no such Lock exists).

**Risk R-3 — Investor requests Part 1 track financial metrics in commit metadata.**
Scenario: investor-expert scalability analysis requests Part 1 add `revenue_impact:` field to commit messages to enable financial tracing of development work.
Lane violation: financial metrics are investor-expert (capital-allocation domain) per mgmt-expert §1b out_of_scope table. Embedding them in Part 1's commit format expands the commit schema beyond the structural format invariant and introduces a cross-domain field with no Part 1-level enforcement mechanism.
Response: REJECT. Financial impact attribution belongs to Part 7 (Project Lifecycle Substrate) `outcome:` field, not in the version-control commit message. Escalate via `escalations[]{trigger: out-of-domain, alternative_routing: "investor-expert × integrator on financial outcome attribution"}`.
F: F3. ClaimScope: holds for Phase A where financial tracking is manual. R: refuted if Phase B introduces automated revenue attribution and a Lock is added for it.

**Risk R-4 — Scope balloon on Wave C Bullet 1 (cross-fork provenance).**
Scenario: the cross-fork provenance schema stub begins accumulating design decisions (field semantics, reconciliation protocol, merge conflict resolution) during Wave C, converting a stub into an architectural specification.
Management response: apply Shape Up scope-hammer. [src:product-management-cagan-shape-up.md:§4 Principle 2] The acceptance predicate for Bullet 1 is: "A `decisions/policy/cross-fork-provenance-phase-b-deferred.md` file exists with ≤3 pages declaring (a) required fields, (b) audit-trail fragmentation points, (c) explicit Phase-B label." If the draft exceeds 3 pages, cut — do not extend.
F: F4. ClaimScope: holds for Wave C 2-day appetite window.

---

## §8 Cagan / Shape Up Additions to architecture.md

Per the mission brief, the following must be added to the Wave C architecture.md:

**§J Operational Rituals — append appetite limits:**
> "Wave C Part 1 build cycle appetite: 2 working days. If §A–§J draft is not complete within 1.5 days, cut §J and §I to stub form only. Do NOT scope-balloon. Circuit-breaker: if any Wave C bullet expands beyond its declared effort tier (S or M), the bullet is re-shaped to fit within tier or deferred to Wave D with explicit `[deferred: Wave D]` label. Per Shape Up fixed-time variable-scope discipline." [src:product-management-cagan-shape-up.md:§4 Principle 2]

**§F Anti-scope — add most-likely scope-creep proposals explicitly rejected:**
The current §F covers generic (strategic decisions, founder agency, engagement-economy patterns) and part-specific (commit content correctness, AWAITING-APPROVAL gate logic, Notion sync, schema authorship) cases. [src:part-1-system-state-persistence.md:§F] Add the following explicit rejections based on the risk register above:
- "This part does NOT embed CRM entity IDs, financial metrics, or domain-specific semantic fields in the commit format — the `[area] verb what (why)` format is structural only; semantic enrichment is Part 6 (Governance) or Part 7 (Project Lifecycle) territory."
- "This part does NOT trigger notifications or webhooks on commit — signal emission goes to `shared/state/system-health.json` only; notification routing is Part 8 (Health Monitoring) or Part 9 (Owner Interaction Scaffold)."
- "This part does NOT specify SLO thresholds or alert policies for the integrity signals it emits — those are Part 8's contract."
- "This part does NOT implement the cross-fork provenance reconciliation protocol — that is Phase-B architecture work; Wave C produces only the stub declaration in `decisions/policy/`."

**§E self-exemplification sentence:**
Add to §E opening: "This interface card is itself a Part 1-governed artefact: committed via git under D25 discipline, carrying F-G-R frontmatter and [src:] inline citations, with §E structured per A.6.B L/A/D/E lane separation." [FPF §4.3 CP-3]

---

## §9 Summary of Flagged Gaps for Wave C Architecture Author

| Gap ID | Lane | Description | Severity | Closure vehicle |
|---|---|---|---|---|
| G-1 | Laws | Law 2 not machine-checkable until Wave C Bullet 2 lint rule ships | Medium | Wave C Bullet 2 — lint signal #12 |
| G-2 | Admissibility | File size limit absent | Low | Add 1MB / 10MB thresholds to §A Admissibility |
| G-3 | Admissibility | UTF-8 encoding not explicitly required | Low | Add to §A Admissibility |
| G-4 | Admissibility | Binary-vs-text discrimination absent | Low | Add binary commit descriptor rule |
| G-5 | Deontics | "Indefinitely" → SLI conversion needed | Medium | Convert to 99.999% / 10yr / weekly fsck |
| G-6 | Effects | fsck cadence not specified | Low | Add weekly cron + `system-health.json` write |
| G-7 | §H | Code-level interface specs absent | High | Add §H to architecture.md: hook spec, /company-status schema, /knowledge-diff contract |
| G-8 | §E | Self-exemplification sentence absent | Low | Add one sentence to §E opening |
| G-9 | §F | Common scope-creep rejections not enumerated | Medium | Add 4 explicit §F rejections per §8 above |

**Severity guide:** High = would block Phase B fork import. Medium = weakens enforceability but Part 1 still operable. Low = cosmetic / completeness.

Only G-7 is blocking for Phase B fork import. All others are completeness improvements.

---

## §10 F-G-R Summary on mgmt-expert Claims in This Cell

| Claim | F | ClaimScope | R |
|---|---|---|---|
| Law 2 is not machine-checkable in Phase A | F4 — operational observation; OPP-02 log-only confirmed | Holds for current cycle; NOT valid post-Bullet 2 | Refuted when Wave C Bullet 2 lint signal #12 passes; accepted until then |
| "Indefinitely" is not a measurable SLI | F4 — definitional; non-time-bounded predicates are not testable by definition | Universal; holds for all SLI declarations | Refuted if a valid operational definition of "indefinitely" is proposed (it cannot be); accepted |
| §H absence blocks Phase B fork implementation within 90 minutes | F3 — reasoned estimate; no empirical data on actual partner onboarding time | Holds for a competent engineer unfamiliar with this repo | Refuted if the architecture.md §A-§F prose is sufficient for implementation without §H (possible for a very experienced git user) |
| 2-day appetite for Part 1 architecture.md is realistic | F3 — scope-based estimate; Part 1 is most mature part | Holds if Wave C scope stays within 3 worklist bullets | Refuted if cross-fork stub (Bullet 1) requires design decisions (then appetite would need to be 3-4 days) |
| Scope-creep risks R-1 through R-4 are the most likely boundary violations | F3 — domain reasoning; based on Part 1 anti-scope and common cross-domain requests | Holds for Phase A consulting-motion context | Refuted if a different scope-creep vector materialises not covered by the risk register |
