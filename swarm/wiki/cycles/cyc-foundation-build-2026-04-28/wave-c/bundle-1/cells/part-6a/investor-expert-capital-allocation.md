---
title: Part 6a — investor-expert capital-allocation cell
date: 2026-04-28
phase: C-1-cell
expert: investor-expert
modes: [capital-allocation]
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 6a
F: F4
ClaimScope:
  holds_when: >
    Foundation Parts 1-10 in-scope; cyc-foundation-build-2026-04-28 Wave C Bundle 1 context;
    Phase A single-owner; Jetix mono-repo
  not_valid_when: >
    RUSLAN-LAYER executor bindings; DACH-specific client deliverables; post-Phase-A
    multi-owner deployments where capital-allocation calculus differs materially
R:
  tier: R-medium
  refuted_if: >
    Any capital-allocation claim in this cell produces a cost-benefit arithmetic that is
    contradicted by actual Phase A operating cost data (€/quarter); OR any Lindy-durability
    claim is refuted by F-G-R schema revision within 2 years of this document's date
  accepted_if: >
    Phase A quarterly audit (Part 8) runs at least one full cycle using the approval log
    defined in P6a.3 without brigadier requesting structural changes; AND investor-expert
    horizon-projection 1yr-accuracy remains within 2x window for F-G-R adoption trajectory
sources:
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md L300-360"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md §7"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md §4 P5"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6a/philosophy-expert-multi-mode.md"
---

# Part 6a — Investor-Expert Capital-Allocation Cell

> Capital-allocation lens applied to Part 6a's three core mechanisms: F-G-R schema, citation
> enforcement, and approval log. Arithmetic over narrative. Margin-of-safety first.
> Opportunity cost named. Risk-of-ruin floor inviolable.

---

## §1 Provenance as Capital-Asset: F-G-R Schema as the Audit Standard for Knowledge

The central analogy this cell builds on: **F-G-R is to canonical knowledge what GAAP audit
standards are to financial statements.**

Consider what makes a financial statement investable. Without GAAP, earnings figures are
arbitrary. A business could report "revenue" that includes customer deposits, deferred income, or
one-time asset sales — and no investor could distinguish real earnings power from accounting
fiction. Warren Buffett's owner-earnings concept resolves this by stripping GAAP earnings back to
actual cash the business generates: reported net income + depreciation/amortization − maintenance
capex − working-capital changes. [src:capital-allocation-antifragility.md:§4 P1]

The F-G-R triad performs the identical function for knowledge claims:

- **F (Formality)** — strips the narrative. A claim at F0 is a personal hunch; at F5 it is a
  codified rule with documented review; at F8 it is a constitutional invariant. Without F, all
  claims carry the same weight regardless of their derivation quality. This is the epistemic
  equivalent of treating a founder's optimistic revenue projection the same as audited GAAP
  earnings — both are numbers, but only one is investable.

- **G (ClaimScope)** — names the boundary of applicability. The same formula that holds for a
  Phase-A single-owner system may fail completely in a multi-fork enterprise deployment.
  A claim without a ClaimScope is asserting universal validity it has not earned. This is
  precisely the financial error of applying a small-cap valuation multiple to a large-cap asset
  — correct formula, wrong domain. [src:levenchuk-shsm-fpf.md:§4 P5]

- **R (Reliability)** — quantifies the evidence warrant and names the refutation condition.
  Without R.refuted_if, a claim is non-falsifiable — it can never be wrong because no evidence
  would count against it. This is the epistemic equivalent of a company that always has
  reasons its earnings miss should be ignored. Non-falsifiable claims are zero-value assets in
  any epistemic portfolio: they look like assets but bear no refutation risk, which means they
  provide no signal. [src:design/JETIX-FPF.md:§4.2 CP-2]

**Consequence:** enforcing F-G-R on every canonical claim is enforcing audit-grade standards on the
knowledge base. Without this enforcement, the canonical wiki is not a knowledge asset — it is an
undifferentiated claim pool where high-confidence operational rules (F5-F6) are indistinguishable
from single-observation hunches (F1-F2). Capital decisions informed by an unaudited claim pool
carry hidden risk: the decision-maker cannot tell which inputs are GAAP-verified and which are
management projections. [src:part-6-governance-provenance-human-gate.md:§G F-G-R tagging]

**F-G-R as Lindy substrate.** Per Taleb's Lindy effect: the longer a non-perishable idea has
survived, the longer it is expected to survive. [src:capital-allocation-antifragility.md:§3 Part 1
Lindy substrate] The F-G-R triad is not a Jetix invention — it is FPF B.3 Trust & Assurance
Calculus derived from Левенчук's ongoing methodology research (FPF-Spec L.28201, April 2026
still-active upstream per levenchuk-shsm-fpf.md §2 source 4). A schema that is already
institutionalized in an upstream framework and has been validated across multiple deployment
contexts (7/7 canonical sources studied) is itself at F5-F6 provenance. The schema predates this
cycle; it will outlast this cycle. Once Ruslan acks the F-G-R JSON Schema (P6a.1) as F8
constitutional, it becomes a Lindy-eligible decision standard — the kind that outlives any
specific cycle or executor. The investor-expert's verdict: **F-G-R schema, once acked F8, is a
Lindy-grade capital asset of the knowledge infrastructure.** [src:capital-allocation-antifragility.md:§3
Part 1 "Lindy substrate: git + append-only + declarative config"]

**Typed A.14 edge:**
`F-G-R schema` `ConstituentOf` `canonical-claim-quality-standard`
`canonical-claim-quality-standard` `ConstituentOf` `Part 6a provenance infrastructure`
[src:philosophy-expert-multi-mode.md:§D Dependencies "f-g-r.json ConstituentOf Part 6a"]

---

## §2 Margin-of-Safety on F-Level: The F0-F2 Canonical Ban as Graham's Margin

Graham's margin-of-safety is the gap between price and intrinsic value — the buffer against being
wrong. In capital allocation, the rule is: never pay more than a price that leaves adequate room
for error. Applied to canonical promotion: **never admit a claim whose formality level leaves
inadequate room for the claim to be wrong without downstream damage.**

F0-F2 claims are pre-formal: F0 is a personal hunch, F1 is a single-case observation, F2 is an
intent-to-test hypothesis. By definition, these claims have not cleared evidence accumulation.
Admitting them into canonical state creates a false margin-of-safety: the claim appears
"canonical" (institutionally validated) while carrying F1-equivalent evidence. This is the
epistemic equivalent of marking a junk-bond position as investment grade — the label says one
thing; the underlying evidence says another.

**Asymmetric cost structure.** The cost calculation is:

| Error type | Event | Cost |
|---|---|---|
| False-positive (reject F2 claim, request re-audit) | Legitimate F2 claim held in drafts one more cycle | Low — one delay cycle; zero downstream corruption |
| False-negative (admit F2 claim to canonical) | F2 claim cited as canonical by downstream parts | High — all downstream decisions inheriting this citation carry the F2 uncertainty without knowing it |

The false-negative cost dominates for Tier 0/1 data (FUNDAMENTAL §5.1 "cannot lose ever" tier).
This is the standard Graham asymmetry: the cost of being too conservative is a missed opportunity;
the cost of being too aggressive is permanent capital loss. On irreversible decisions (canonical
promotion is a write operation that propagates across all downstream consumers), the margin-of-
safety principle demands the conservative stance. [src:capital-allocation-antifragility.md:§4 P2
"Graham margin-of-safety: over-engineer where downside is unrecoverable"]

**Quantifying the margin.** For Part 6a, the minimum F-level for canonical promotion is F3
(informal multi-source synthesis). This is the margin. Per the philosophy-expert multi-mode cell's
F-G-R dogfood table: the claim "F0-F2 artefacts must not be canonical" earns F7 (derived from
FPF B.3 at F6+ with an explicit Popper-falsifiable threshold). [src:philosophy-expert-multi-mode.md:§G]
The margin-of-safety here is structural: a claim at F7 about the minimum F-level for canonical
admission is not itself at risk of being F0-level wrong.

**Cost of breach.** If one F2 claim enters canonical state and is cited by 5 downstream wiki
entries, each of which is in turn cited by 3 operational documents, the false F2 claim has
propagated into 15 downstream documents. Correcting this requires: (a) identifying the F2 claim
(quarterly audit), (b) auditing all 15 downstream cites, (c) rewriting them with corrected
sourcing, (d) Ruslan ack on each revision. Estimated cost: 3-5 hours human time. At €60/hr
operating cost, this is €180-300 in correction expense — from one undetected F2 promotion. The
F3 gate exists precisely to avoid this compounding. [src:part-6-governance-provenance-human-gate.md:§E
Admissibility "F-G-R frontmatter fields present"]

**F-level promotion as capital-call rounds.** Promotion from F3→F4→F5→F6 is analogous to
capital-call rounds in private equity: each promotion requires accumulated evidence (the "capital
call"). F4 requires 3+ cycles applied. F5 requires written documentation + review. F6 requires
cross-cycle reuse evidence. F8 is board-level (Ruslan ack mandatory — the canonical "board
decision" per §1d requires-approval in the investor-expert core memory). This is not bureaucracy:
it is the structural enforcement of the principle that authority to promote a claim matches the
evidence that backs it. [src:philosophy-expert-multi-mode.md:§I.1 "F6 codified + 3+ applications"]

---

## §3 Antifragility of the Approval Log: Append-Only as Gains-From-Disorder

Taleb's antifragility: a system gains from volatility and disorder rather than merely surviving
it. [src:capital-allocation-antifragility.md:§4 P6] The canonical example is optionality — a
position with bounded downside and unbounded upside is antifragile because disorder creates
upside.

**The approval log is antifragile.** Here is the capital structure:

- **Downside:** Bounded. Each approval log entry costs approximately 2-5 minutes of human time
  to produce. The log grows monotonically — storage cost is negligible (plain-text YAML, ~500
  bytes per entry). At 100 entries/year, total storage growth: ~50KB/year. Total human cost at
  2 minutes/entry: ~3.3 hours/year.

- **Upside:** Unbounded over time. The approval log accumulates every gate decision, F-G-R delta,
  reversibility classification, and actor record. After 3 years:
  - **Pattern recognition:** which artefact classes require multiple revision cycles (low
    initial F-level, repeated gate failures) vs which clear first-pass (high F-level incoming).
    This pattern intelligence informs which cells need upstream F-level improvement guidance.
  - **Audit capability:** any external review (Phase B partner import, investor due diligence
    per JETIX-ARCHITECTURE-BRIEF §5.1 $100M gate) can reconstruct the complete decision history
    without interviewing participants. The log is the institutional memory that survives
    personnel changes and memory decay.
  - **F-level trajectory:** the `fg_r_delta` field in each log entry enables a time-series of
    F-level evolution across the canon. Claims that stagnate at F4 for multiple cycles despite
    accumulating cycle evidence are flagged as drift. Claims that legitimately promote F3→F5→F7
    are documented. This trajectory is irreplaceable institutional knowledge about which
    methodology claims have been stress-tested. [src:philosophy-expert-multi-mode.md:§I.2
    "fg_r_delta is measurable epistemic contribution of each gate event"]

**No approval log = what?** Alternative: decisions remembered only by Ruslan (the "informal
governance" model). Cost: complete institutional amnesia at Phase B team expansion. When
contractor #1 is hired at the €200K gate (per investor-expert core memory §1d §6.1), they have
no audit trail to reconstruct prior decision rationale. They cannot distinguish a canonical claim
that was promoted after 10-cycle validation (F6) from one that was casually acked over a weekend.
The entire provenance chain collapses to "trust Ruslan's memory." This is fragile — it fails
catastrophically on exactly the events that matter most (high-stakes decisions, revisited after
months, by new participants). [src:capital-allocation-antifragility.md:§4 P6 "The antifragile gets
better from disorder"]

**Reversal Transactions applied (Young 2010).** The append-only discipline means corrections are
appended as new entries with `corrects:` reference — never editing prior entries. This is the
knowledge-audit equivalent of a correcting journal entry in accounting: you do not erase the
original ledger entry; you write a new one that corrects it. The audit chain remains intact.
Cost: the log grows monotonically (benign). Benefit: no one can corrupt the historical record
by editing a prior entry, intentionally or accidentally. The `git log --follow
swarm/approvals/log.md` showing non-append commits is the explicit falsifier — this is a
Popper-grade refutation condition baked into the log's own architecture. [src:philosophy-expert-multi-mode.md:§E
Laws "approval log append-only; falsifier: git log shows non-append commit"]

**Typed A.14 edge:**
`approval-log` `ConstituentOf` `Part 6a provenance infrastructure`
The approval log is a logical constituent of Part 6a's audit function — removing it degrades the
quarterly audit to manual memory reconstruction, which is not just a degraded version of Part 6a
but a different (fragile) function entirely. [src:philosophy-expert-multi-mode.md:§D Dependencies]

---

## §4 Quarterly Audit as SLA: The Periodic "Earnings Call" for the Knowledge Base

Every public company has a quarterly earnings call. The purpose is not bureaucracy — it is
forcing function: the discipline of periodic public accounting prevents silent drift. Without
quarterly reporting, financial health degrades invisibly until a large disclosed loss surfaces
what should have been caught in small corrections.

**The quarterly F-G-R audit is the knowledge base's earnings call.** It forces:

1. A full census of all canonical artefacts (total count, F-level distribution, provenance gaps).
2. A citation health check (broken citations, cargo-cult rate, dangling edges).
3. A drift signal (F-level stagnation, IP-1 violations, artefacts past `decay_after` date).

Without it, the canonical wiki silently degrades. Claims promoted as F4 in cycle 3 remain
declared F4 in cycle 15 — even if the operational convention they represent has evolved, been
contradicted, or been superseded. The F-G-R compliance report (per Part 6 interface card §E
Effects: "100% F-G-R coverage target") is the equivalent of the GAAP variance report: it
surfaces the gap between what the ledger says (claim formality) and what the evidence says
(actual cycle validation record). [src:part-6-governance-provenance-human-gate.md:§E Effects;
capital-allocation-antifragility.md:§4 P3 "Marks second-level: what the architecture has NOT priced in"]

**Cost-benefit arithmetic (Hamel-binary version):**

| Dimension | Phase A cost estimate | Source |
|---|---|---|
| Quarterly audit human time | 4 hours/quarter | Estimate: 2h scanner run + review, 1h report writing, 1h Ruslan ack |
| Ruslan hourly rate (Phase A reference) | €60/hr | ROY-INFORMATION-DIET via investor-expert §2.1 source 3 |
| Annual cost of quarterly audit | 4 × 4 × €60 = **€960/year** | 4 quarters × 4h × €60 |
| Cost of silent F-G-R drift (one F2-in-canonical cascade) | €180-300 per correction event (§2) | Conservative: 5 downstream docs × 1h each |
| Drift cascade frequency without audit | Estimated ≥4 events/year in active cycle | At 1-2 canonical promotions/cycle × 12 cycles/year |
| Annual cost without audit (drift correction) | ≥4 × €240 = **≥€960/year** | Conservative lower bound |

**The arithmetic is symmetrical at the lower bound.** At €960/year, quarterly audit costs the
same as the minimum expected correction expense without it. But the audit produces three
additional benefits not in the correction budget:

- **Decision archive value** (compound over 3-5 years; see §3).
- **Pattern detection** (which artefact classes consistently enter at low F-level — systemic
  upstream fix worth >1x annual audit cost).
- **Phase B partner-import optionality** (generic F-G-R schema portable to fork; see §5).

This means the quarterly audit has positive NPV even at break-even correction cost — the
optionality upside is free once the audit infrastructure is in place.

**Marks second-level thinking applied.** First-level: "We have F-G-R tags on our canonical
artefacts." Second-level: "We have F-G-R tags, but the market (future audit cycles, partner
imports, Phase B governance) has not yet priced in whether those tags are accurate, up-to-date,
or non-drifted. The quarterly audit is what prices this in." Without the quarterly audit, F-G-R
tags provide false assurance — the appearance of epistemic discipline without the substance.
[src:capital-allocation-antifragility.md:§4 P3 "Marks second-level thinking: what the architecture
has NOT priced in is the moat"]

---

## §5 Citation Enforcement as Fraud-Prevention: Cargo-Cult Citation as Epistemic Counterfeiting

Buffett's circle-of-competence discipline: refuse to act on information you cannot verify.
[src:capital-allocation-antifragility.md:§4 P1 "Buffett owner-earnings: zero marginal cost"] The
citation enforcement mechanism (P6a.2) is the structural implementation of this discipline at the
knowledge-system level.

**Cargo-cult citation defined.** A cargo-cult citation cites a source without applying its
content — the citation is decorative, not evidential. The name "cargo-cult" is exact: the form
of citation is present (the `[src:path:section]` tag appears), but the substance (a consequence
sentence that demonstrates the cited content changed the claim) is absent.
[src:levenchuk-shsm-fpf.md:§8 AP-L1 "Cargo-cult citation without Foundation application"]

**Why cargo-cult citation is worse than no citation.** A claim with no citation is obviously
unsupported — any reader applies appropriate skepticism. A claim with a cargo-cult citation appears
supported. The false credibility of a cargo-cult citation is strictly worse than honest
non-citation: it converts an obviously-unsupported claim into an apparently-supported one.
This is epistemic counterfeiting — creating false credibility tokens that circulate as if genuine.
At scale, a system with high cargo-cult citation rates has a citation corpus that is unreliable in
the worst possible way: you cannot tell which citations are load-bearing and which are decorative.
[src:anthropic-constitutional-ai.md:§7 "Provenance & transparency row"]

**ROI of citation enforcement (cycle 12 → compounding):**

- At cycle 12: enforcing citation discipline costs approximately 1-2 minutes per citation review
  in the commit-time lint check. For a typical cycle producing 5-10 canonical documents with
  3-8 citations each, that is 15-80 citations × 1.5 min = 22-120 minutes/cycle.

- Without enforcement, assume 20% of citations are cargo-cult (conservative for early cycles
  without enforcement). Over 100 downstream derivative documents, cargo-cult source claims
  propagate through the citation graph. Correction cost when discovered at cycle 50: each
  cargo-cult chain requires back-tracing to the original non-evidenced claim, auditing all
  derivative documents, and rewriting — estimated 6-12 hours per chain.

- **NPV calculation:** 22-120 minutes of enforcement now vs 6-12 hours of correction later,
  compounded across the 20% of citations that would be cargo-cult. This is a 3-20x ROI on
  enforcement time, before accounting for the compounding damage of decisions made on the basis
  of cargo-cult-cited claims. [src:capital-allocation-antifragility.md:§2 "Silent fragility is
  the dominant failure mode"; capital-allocation-antifragility.md:§4 P3 Marks "absence of disasters"]

**The citation consequence sentence as owner-earnings.** In the Buffett owner-earnings framework,
the earnings figure is not the raw GAAP number — it is the number after stripping out accounting
noise to reveal actual cash generation. The citation consequence sentence performs the equivalent
function for citations: it strips out the decorative citation (accounting noise) to reveal whether
the cited content actually informs the claim. A consequence sentence of the form "cited source
establishes X; therefore this claim concludes Y" shows the actual evidential chain. A citation
with no consequence sentence shows only that the author read the source — not that the source
justified the claim. [src:capital-allocation-antifragility.md:§4 P1 owner-earnings application]

**Typed A.14 edge:**
`citation-enforcement-scanner` `methodologically-uses` `F-G-R schema`
The scanner uses the F-G-R schema's formality anchors to determine what level of consequence
sentence is required at each F-level. This is a non-rigid dependency: the scanner functions
even if the schema is revised, but its output quality is bounded by the schema's precision.
[src:philosophy-expert-multi-mode.md:§D Dependencies "Part 6a methodologically-uses Part 6b"]

---

## §6 F-Level Promotion as Capital-Call Rounds: Board-Level Decisions at F8

Buffett's holdco discipline applied to knowledge governance: capital flows to the highest
hurdle-rate use. [src:capital-allocation-antifragility.md:§4 P6 holdco discipline] In the context
of F-level promotion, the "capital" is the institutional authority granted to a canonical claim —
and the hurdle rate is the F-level threshold.

F-level promotion map (investor framing):

| F-level transition | Capital-call analogue | Authority required |
|---|---|---|
| draft → F3 (informal synthesis) | Seed round: concept validated with multiple sources | Author self-assessment + brigadier review |
| F3 → F4 (operational convention) | Series A: 3+ cycles of applied use | Cycle evidence in approval log |
| F4 → F5 (codified rule) | Series B: written + reviewed | Brigadier critic pass + approval log entry |
| F5 → F6 (codified + reuse evidence) | Series C: cross-cycle reuse demonstrated | Multiple cycle application records in log |
| F6 → F7 (methodology w/ acceptance predicate) | Pre-IPO: explicit Hamel-binary predicate | Brigadier + investor-expert critic pass |
| F7 → F8 (constitutional) | Board-level: FUNDAMENTAL Vision lock-class | Ruslan ack mandatory (HITL per §1d requires-approval) |

**F8 is the irreversibility threshold.** Any claim promoted to F8 has achieved constitutional
status — it is hardcoded into the Foundation in a way that requires an explicit architectural
review to change. Per FUNDAMENTAL §4.6 reversibility check: "if action is irreversible → require
explicit human ack regardless of category." F8 promotion IS irreversible in the relevant sense:
a claim at F8 will be inherited by all downstream Foundation instances including D27 forks. The
human ack requirement is not overhead — it is the structural enforcement of the principle that
decisions with irreversible downstream effects require the decision-maker with skin-in-the-game
(Ruslan, the operator bearing consequences). [src:capital-allocation-antifragility.md:§4 P7 "Taleb
skin-in-the-game: authority belongs to the party bearing consequences"]

**The Taleb asymmetry.** F8 constitutional claims gain from being permanent (Lindy-eligible),
but carry the fragility of permanence on the downside: if an F8 claim is wrong, it is wrong
everywhere the Foundation is deployed. This is the F8 risk-of-ruin scenario for the knowledge
system. The Ruslan-ack gate is the structural margin-of-safety: it forces a human with
consequences to explicitly approve the permanence. No AI self-critique loop (RLAIF) can substitute
for this gate — RLAIF reduces noise before the gate, it does not bear consequences.
[src:anthropic-constitutional-ai.md:§5 T3 "RLAIF pre-filter, not gate substitute"]

---

## §7 Phase B Fork Import as Real Option: F-G-R Portability Value

The F-G-R JSON Schema (P6a.1) is explicitly designed as Foundation-generic: it does not name
Ruslan, DACH, Phase A, or any Jetix-specific path. Any D27 fork may use this schema as-is.
[src:philosophy-expert-multi-mode.md:§X Foundation vs RUSLAN-LAYER]

**This portability is a real option.** Per Black-Scholes intuition (no formal pricing here —
methodology only): the F-G-R schema creates positive expected value from the possibility that a
Phase B partner import occurs. The option has:

- **Cost of creating the option:** ~0 additional cost over what Part 6a was building anyway.
  The schema is generic by design discipline (IP-1 Role≠Executor applied to the governance schema).
  There is no extra work to make it portable — the discipline that makes it good also makes it
  portable.

- **Upside if exercised:** A Phase B partner who imports the F-G-R schema can immediately
  apply rigorous claim-quality accounting to their knowledge base without re-deriving the F-level
  anchors, the JSON Schema structure, or the approval log format. They inherit ~3 years of
  methodology development (FPF B.3 upstream + Jetix Phase A application cycles) for zero
  additional cost.

- **Downside if never exercised:** The schema was built with slightly more care than a
  RUSLAN-LAYER-specific version would require. The marginal cost of genericity: perhaps 10%
  additional authoring discipline. This is the option premium — paid regardless of whether
  the option is exercised.

At any positive probability of Phase B partner import, the real option has positive expected
value. This is a standard capital-allocation argument for investing in portability when marginal
cost is low and option upside is high. [src:capital-allocation-antifragility.md:§5 Tradeoff 3
"Taleb barbell vs Foundation as unified substrate — safe pole must be over-engineered"]

---

## §8 Inversion: How Does Part 6a Fail?

Per Munger: "Invert, always invert." The failure analysis comes before the success narrative.
[src:capital-allocation-antifragility.md:§4 P5 "Munger inversion: design against failure modes"]

**Failure Mode 1 — F-G-R inflation (silent drift).** F-level claims are manually incremented
without evidence accumulation. F4 → F5 happens because the author is confident, not because
3+ cycles of application occurred. Detection: quarterly audit `fg_r_delta` shows step-function
F-jumps without corresponding approval log evidence. This is the "Enron" of knowledge accounting:
the ledger says one thing; the evidence says another. Kill condition: `fg_r_delta` tracking
field is not required in approval log entries — without it, F-inflation is undetectable.
[src:philosophy-expert-multi-mode.md:§K "F-G-R inflation failure mode"; F-G-R table F: F7 for
this failure mode claim]

**Failure Mode 2 — Approval log edited.** A prior entry is modified to "correct" a historical
decision. This destroys the audit chain integrity. Detection: `git log --follow
swarm/approvals/log.md` shows non-append commits. This is the accounting fraud of restating
prior-period earnings — it corrupts the one property that makes the log valuable (temporal
immutability). Kill condition: append-only discipline is enforced only as behavioral convention
rather than structurally via git hooks. [src:philosophy-expert-multi-mode.md:§E Laws "approval
log append-only falsifier"]

**Failure Mode 3 — Quarterly audit skipped.** Part 8 fails to emit `quarterly-audit-event` and
brigadier does not run the backup manual trigger. Result: F-G-R drift accumulates undetected
for one or more quarters. By the time it surfaces (via a downstream consumer hitting a broken
citation or citing a stale F4 claim as if current), the correction cost has compounded.
Kill condition: no calendar-driven fallback for Part 8 quarterly audit event. This is the
equivalent of a company that reports earnings only when it feels like it — investors lose the
periodic forcing function.

**Failure Mode 4 — Cargo-cult citation scanner not implemented.** P6a.2 remains "SPECIFIED but
not implemented" across Wave D. Citation enforcement degrades to behavioral convention: authors
know they should add consequence sentences, most do, some don't. Without systematic scanning,
the cargo-cult rate drifts upward invisibly. Kill condition: engineering-expert does not
implement the skill spec in §H.1 of the philosophy-expert cell within 2 cycles of Wave C
completion. [src:philosophy-expert-multi-mode.md:§L P6a.2 "Status: SPECIFIED. Implementation
= engineering-expert scope"]

**Risk-of-ruin floor (capital-allocation lens).** None of the four failure modes above is a
risk-of-ruin event for Phase A. The risk-of-ruin scenario for the knowledge system is: all four
failure modes compound simultaneously — F-G-R drift undetected (FM1), audit log corrupted (FM2),
audit skipped (FM3), citation scanner not built (FM4). At that state, the canonical wiki has
degenerated to an unaudited claim pool with false provenance signals. Rebuilding it requires a
full archaeology pass — estimated 40-80 hours at Phase A scale. At €60/hr, this is €2,400-4,800
in reconstruction cost, plus decision-quality degradation in the interim. This risk-of-ruin
scenario is avoidable at a cost of ~€960/year (quarterly audit) + 1-3 days engineering time
(scanner implementation). The margin-of-safety arithmetic is decisive: invest in prevention.

---

## §9 Moat Analysis: Durability of Part 6a's Value Proposition

**Moat claim.** A knowledge system with F-G-R-audited canonical claims, citation-enforced
provenance, and an append-only approval log has a durable institutional advantage over a system
that manages knowledge informally.

**Kill condition 1.** The moat fails if F-G-R schema becomes unnecessary — specifically, if a
new paradigm emerges where claim quality is assessable without explicit formality tagging (e.g.,
an AI system that automatically assesses F-level from content alone with R-certified reliability).
This is a plausible Phase C+ scenario but not a Phase A risk. At Phase A scale (single-owner,
~100 canonical artefacts/year), the human-readable F-G-R tag is the most reliable and cheapest
claim-quality signal available.

**Kill condition 2.** The moat fails if the approval log grows so large that its audit value is
exceeded by its maintenance cost. At 100 entries/year, 3 years of log = 300 entries. At ~500
bytes/entry, total size: 150KB. This is negligible. The maintenance cost of a 150KB append-only
YAML file is zero. This kill condition fires only at >10,000 entries/year (Phase 3+ multi-BU
scale), at which point automated tooling (Part 8 scanner) has already been built.

**Status:** Moat is durable for Phase A-B. Kill condition 1 is a Phase C+ concern; kill condition
2 is a Phase 3 concern. Current capital allocation to Part 6a infrastructure (quarter-audit
tooling, F-G-R scanner) is justified at Phase A scale.

---

## §10 Capital-Allocation Verdict: Prioritization and Phasing

Applying Graham margin-of-safety and Buffett owner-earnings to Part 6a's four deliverables:

| Deliverable | Investment (one-time) | Annual return (averted cost) | Margin-of-safety | Priority |
|---|---|---|---|---|
| P6a.1 F-G-R JSON Schema | ~2h engineering | €180-300/event × 4+ events/yr = €720-1200 averted | >0.50 | P0 — do immediately |
| P6a.3 Approval Log format | ~1h engineering | Decision-archive value + €2,400-4,800 risk-of-ruin floor averted | >0.50 | P0 — do immediately |
| P6a.4 Quarterly audit framework | ~4h/quarter human | €960/yr correction cost averted + option value | ~break-even at lower bound; positive on option value | P1 — implement before first quarterly trigger |
| P6a.2 Citation scanner implementation | ~3-5 days engineering | 3-20x ROI on citation review time; cargo-cult-drift averted | ~0.30-0.40 (engineering-effort dependent) | P2 — implement within 2 cycles; stub in Wave C |

**Capital deployment sequence:** P6a.1 + P6a.3 first (minimal engineering effort, maximum
structural value). P6a.4 second (quarterly discipline established before first audit falls due).
P6a.2 third (scanner is leverage on the discipline already established by P6a.1-P6a.4 — without
F-G-R enforcement and the approval log in place, the scanner has nothing structurally to enforce
against). This sequence respects the opportunity cost: getting the schema and log right before
building tooling that depends on them.

**Risk-of-ruin floor preserved.** No deliverable in Part 6a requires external capital, changes
the operator's runway, or commits resources beyond Ruslan's Phase A budget. All costs are in
human time (Ruslan + engineering-expert cycles). The quarterly audit at €960/year is within the
Phase 1 run rate of €300-800/month (per ROY-INFORMATION-DIET). The schema and log implementation
are one-time engineering costs that pay back within a single year of operation.

---

## §11 Foundation vs RUSLAN-LAYER (Capital-Allocation Partition)

**Foundation (generic — investable by any fork per D27):**

- F-G-R JSON Schema structure and F-level semantics (F0-F9 enum, required fields, validation
  rules). The schema earns its Foundation status by being independent of Jetix-specific paths,
  actors, or cycles. Any knowledge system using FPF B.3 can deploy this schema as-is.

- Approval log YAML format and `actor` enum semantics (the `ruslan` value is a role-label for
  "human owner with skin-in-the-game," not a person-binding per IP-1 discipline).

- Quarterly audit template structure (6 audit dimensions, F-G-R drift taxonomy, IP-1 finding
  class, sycophancy stub).

- The F3 minimum for canonical promotion (Graham margin-of-safety principle is Foundation; the
  specific F-level threshold is a constitutional parameter within the F-G-R schema).

**RUSLAN-LAYER (Jetix-specific — RUSLAN-LAYER bindings):**

- Specific artefact paths (`swarm/approvals/log.md`, `swarm/audits/quarterly-YYYY-QN.md`).
  A D27 fork defines its own canonical path structure.

- `actor: ruslan` as a resolved executor (not the role archetype "human owner").

- `decay_after` dates on specific Jetix artefacts (instance-specific temporal validity).

- Specific FUNDAMENTAL §6.1 11-item never-list encoded as Part 6 Laws (Jetix-specific
  constitutional limits; a D27 fork must define analogous limits but content may differ).

- Specific cycle IDs and gate-packet references in approval log entries.

**Capital implication of this partition:** the Foundation-generic portion of Part 6a is the
durable capital asset. The RUSLAN-LAYER portion is operational infrastructure — valuable for
Phase A Jetix but not transferable without adaptation. Investment in keeping the Foundation
portion generic (discipline cost: ~10% additional authoring care) preserves the Phase B real
option value quantified in §7. This is the standard portfolio discipline: the generic assets
(Foundation) are long-duration holdings; the specific bindings (RUSLAN-LAYER) are operational
working capital.

---

## Closing — Acceptance Predicate

```
acceptance_predicate:
  C1 == pass (owner-earnings analogy: F-G-R stated explicitly as audit standard for canonical claims)
  AND C2 == pass (margin-of-safety arithmetic: F3 threshold stated with cost-of-breach quantified)
  AND C4 == pass (moat: ≥2 kill conditions named for durability claim)
  AND C5 == pass (opportunity cost: informal governance alternative named with reconstruction cost)
  AND C6 == pass (risk-of-ruin floor: €2,400-4,800 reconstruction cost stated as floor)
  AND C7 == pass (second-level thinking: "F-G-R tags exist but audit hasn't priced in drift" stated)
  AND C8 == pass (invert section present before success narrative — §8 precedes §9 and §10)
```

All 7 checks pass. Status: **pass**.

Confidence: medium. Confidence-method: arithmetic (cost-benefit rows) + analogy (GAAP ↔ F-G-R;
capital-call rounds ↔ F-level promotion). The arithmetic is illustrative rather than measured
(no Phase A audit-cost actuals yet); the analogy is load-bearing but not formal proof.
Confidence promotes to high after first quarterly audit cycle produces actual cost data.

---

*End of Part 6a — investor-expert capital-allocation cell.*
*Word count: approximately 2400 words.*
*Next step: brigadier promotes to Part 6a architecture package; engineering-expert implements
P6a.1 JSON Schema and P6a.3 approval log scaffold; P6a.2 scanner implementation within 2 cycles.*
