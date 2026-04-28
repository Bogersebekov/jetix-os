---
title: Wave D Phase D-5 — Open-questions Catalogue (~38 items routed)
date: 2026-04-28
type: oq-catalogue
cycle: cyc-foundation-build-2026-04-28
wave: D
phase: D-5
F: F4
G: wave-d-oq-catalogue
R: refuted_if_OQ_unrouted_or_misrouted
gate: M-D-5
---

# Phase D-5 — Open-Questions Catalogue

**Mandate.** Collect all OQ items deferred from Bundles 1-4 + Wave A merged
+ OQs surfaced during Wave D itself. Route each to one of:
- **(i) Wave E ack-time decision** — constitutional-tier; Ruslan must ack
- **(ii) Phase B operational backlog** — calibration / observation / test fixture
- **(iii) Phase C+ deferred** — multi-owner / multi-tenant / scale-dependent
- **(iv) close-as-resolved-already** — addressed by Bundle 1-4 decision
- **(v) re-route as Wave D fix** — Phase D-8 retroactive supplement

**Pass threshold:** 100% routed; 0 unrouted.

**Brigadier note on count.** Deep prompt estimated ~17 OQs; actual catalogue
is ~38 items (Bundle 1 = 8, Bundle 2 = 7, Bundle 3 = 11, Bundle 4 = 3, Wave A
merged = 5, Wave D-surfaced = 4). The wider count reflects bundle-by-bundle
honest tracking rather than gap drift.

## §1 Bundle 1 OQs (8 items)

| OQ | Description | Route | Rationale |
|---|---|---|---|
| OQ-B1-1 | F4/F6/F8 anchor wording refinements (F4 = "≥3 cycles applied" Hamel-binary; F6 = "cross-cycle reuse evidence"; F8 = FUNDAMENTAL Vision lock-class) | (i) Wave E ack-time | Constitutional schema-wording revision; Ruslan acks F-G-R F8 wording at Wave E LOCKED tag dispatch OR retains FPF B.3 baseline. Surface in AWAITING-APPROVAL §4. |
| OQ-B1-2 | Citation scanner implementation timeline (`swarm/lib/lint-check-citations.sh`) | (ii) Phase B | Within 2 cycles of Wave C completion = Phase B engineering backlog. Anti-cargo-cult enforcement remains advisory until live. |
| OQ-B1-3 | Tier 2 batch sub-grouping algorithm at Phase C | (iii) Phase C+ | At 500 packets/week scale; deferred until Phase C operational data available. |
| OQ-B1-4 | JSON Schema $ref toolchain (`jsonschema` Python lib) | (ii) Phase B | Add to `swarm/lib/` during Phase B implementation; schemas structurally complete by author discipline. |
| OQ-B1-5 | D27 `approvals_reconciliation_strategy` field promotion | (iv) **close-as-resolved-already** | Bundle 1 supplement-2 ack — promoted top-level + 5 strategies enum LOCKED in `cross-fork-provenance.json` v1.1.0. Bundle 4 M5 lite coherence verified. **CLOSED.** |
| OQ-B1-6 | Rules 4 + 7 real-time encoding gap (agents don't store identity / don't negotiate) | (ii) Phase B | Currently F4 quarterly audit cadence; Phase B Part 4 + Part 8 real-time gate-time enforcement upgrade. Foundation has the audit-cadence backstop. |
| OQ-B1-7 | `unshare -n` availability for offline-guarantee test on prod server | (i) Wave E ack-time | Single-question Ruslan confirmation: `unshare -n` available on prod server, OR fall back to LD_PRELOAD/strace path. Surface in AWAITING-APPROVAL §4. |
| OQ-B1-8 | `decisions/policy/cross-fork-audit-deferred-phase-b.md` stub creation | (i) Wave E ack-time | One-line Ruslan ack: create stub on Wave E ack? Trivial. Surface in AWAITING-APPROVAL §4. |

**Bundle 1 routing:** 1 closed-already; 3 Phase B; 0 Phase C+; 3 Wave E; 0 Wave D fix.

## §2 Bundle 2 OQs (7 items)

| OQ | Description | Route | Rationale |
|---|---|---|---|
| OQ-B2-A | Part 1 §I.4 stub `gate_class` enum drift (stale `[autonomous, requires-approval, hitl-required]` vs Bundle 1 F8 `[stop_gate, stage_gate, draft_promotion]`) | (iv) **close-as-resolved-already** | Bundle 1 supplement-1 ack — Part 1 §I.4 enum corrected + commit-format-tokens registered. **CLOSED.** |
| OQ-B2-B | `swarm/lib/` security-domain split for external integrations | (iii) Phase C+ | Multi-tenant Phase C+ work; not blocking Phase A single-owner. |
| OQ-B2-C | `swarm/lib/` test harness | (ii) Phase B | Add pytest harness during Phase B; Foundation Wave C did not require live tests. |
| OQ-B2-D | `[swarm-lib]` and `[part4]` commit area tokens | (iv) **close-as-resolved-already** | Bundle 1 supplement-1 ack — `[swarm-lib]+[health]+[methodology]` tokens registered in `commit-format-tokens.json`. `[part4]` not registered separately; `[architecture]` token covers part-N work. **CLOSED.** |
| OQ-B2-E | Message schema v1.0.0 → v2.0.0 BREAKING change adoption | (ii) Phase B | Schema v2.0.0 LOCKED at Bundle 2; Phase B operational migration of mailbox JSONL files to `acting_as:` v2.0.0. |
| OQ-B2-F | Multi-owner gate F.9 Bridge field activation | (iii) Phase C+ | F.9 Bridge spec authoring required; tied to OQ-B4-3. Phase C+ multi-owner; Foundation has stub fields per Part 9 §I.4. |
| OQ-B2-WC | Architecture document word count under 15K floor (Bundle 2 came in 9-12K) | (iv) **close-as-resolved-already** | Bundle 2 ack §6.x accepted under-floor; structurally complete docs satisfy functional requirements. **CLOSED.** |

**Bundle 2 routing:** 3 closed-already; 2 Phase B; 2 Phase C+; 0 Wave E; 0 Wave D fix.

## §3 Bundle 3 OQs (11 items)

| OQ | Description | Route | Rationale |
|---|---|---|---|
| OQ-B3-P5-1 | UND-3 stub schema reference: task-return-packet superset OR new project-retrospective-packet | (iv) **close-as-resolved-already** | Bundle 4 ack §5.1 — UND-3 finalised as Part 7 §I.2 `project-retrospective-packet.json` SUPERSET of task-return-packet. M5 PASS verified. **CLOSED.** |
| OQ-B3-P5-2 | UND-3 cadence: per project closure event OR per cycle close | (iv) **close-as-resolved-already** | Bundle 4 ack — OQ-5 cadence event-driven F8 LOCKED. Per project closure event (Part 7 §E 4 laws verbatim). **CLOSED.** |
| OQ-B3-P5-3 | Methodology candidate emergence rate calibration ("≥1 entry per 5 cycles" starter) | (ii) Phase B | Phase B 2-3 month observation data collection; calibrate SLI threshold post-baseline. |
| OQ-B3-P5-4 | DRR review cadence-rate SLI threshold (current ≥80%) | (ii) Phase B | Phase B operational calibration per OQ-MERGED-5 specify-and-stub. |
| OQ-B3-P5-5 | Dissolve-test "compound-phase-exclusive operation" judgment criterion | (i) Wave E ack-time | Wave D Cycle 3 closes the dissolve-test window; Ruslan ack-time judgment on criteria meanings. See D-6 verdict. |
| OQ-B3-P8-1 | Variant A retroactive align deferred to Wave D housekeeping cycle | (v) **re-route as Wave D fix optional D-8** | Lightweight Variant B → Variant A canonical-form alignment IF Phase D-8 supplement is triggered for other reasons; otherwise Phase B housekeeping. Variant B is functional; alignment is cosmetic. **Recommend (ii) Phase B** for cleanliness. |
| OQ-B3-P8-2 | FUNDAMENTAL §3 30+ SLI inventory expansion timing (Bundle 3 ships 8) | (ii) Phase B | Phase B operational data dependent. |
| OQ-B3-P8-3 | Alert delivery infrastructure (Slack/email/SMS/page) | (ii) Phase B | Phase B implementation; specific channel choice TBD. |
| OQ-B3-P8-4 | `shared/state/system-health.json` "all green" hardcoded replacement | (ii) Phase B | Live computation per §I.1 schema. |
| OQ-B3-P8-5 | Tier 1+ Default-Deny default for novel alert class | (i) Wave E ack-time | One-line operational policy confirmation: novel alert class defaults to Tier 1 (Ruslan ack) NOT Tier 2 (batch ack) — to err on visibility side. Surface in AWAITING-APPROVAL §4. |
| OQ-B3-P8-6 | Voice pipeline success-rate SLI starter value 0.95 vs current operational baseline | (i) Wave E ack-time | One-line Ruslan ack pre-Phase-B; small-data acceptance. |

**Bundle 3 routing:** 2 closed-already; 6 Phase B; 0 Phase C+; 3 Wave E; 0 Wave D fix
(B3-P8-1 routed to Phase B per recommendation).

## §4 Bundle 4 OQs (3 items)

| OQ | Description | Route | Rationale |
|---|---|---|---|
| OQ-B4-1 | Phase A operational data on appetite-overrun rates per project type | (ii) Phase B | Calibration; collect 3-6 cycles before SLO commitment. Wave D inherits per Bundle 4 ack §6.x. |
| OQ-B4-2 | Phase B partner fork import test fixture for `cross-fork-provenance.json` v1.1.0 | (ii) Phase B | Phase B materialisation; first partner-fork import exercises full schema. Schema-level coherence verified Wave D S-3 scenario. |
| OQ-B4-3 | F.9 Bridge spec authoring (`design/F-9-Bridge-multi-owner-spec.md`) | (iii) Phase C+ | Phase A bounded; multi-owner activation Phase C+. Tied to OQ-B2-F. |

**Bundle 4 routing:** 0 closed; 2 Phase B; 1 Phase C+; 0 Wave E; 0 Wave D fix.

## §5 Wave A merged OQs (5 items)

| OQ | Description | Route | Rationale |
|---|---|---|---|
| OQ-MERGED-2 | Dissolve-test threshold check (Part 5 standalone vs dissolve into Part 1+Part 3) | (closed via D-6) | Wave D Cycle 3 closes the decision window. See D-6 verdict (STANDALONE PRESERVED). **CLOSED via D-6.** |
| OQ-MERGED-3 | Fork-separation Foundation vs RUSLAN-LAYER FINAL CLOSURE | (iv) **close-as-resolved-already** | Bundle 4 ack §6.5 — FINAL CLOSURE F8 LOCKED across Parts 7, 9, 10 §X with explicit DACH/GDPR/auth-token/contact-list/r/Berlin examples. **CLOSED.** |
| OQ-MERGED-5 | Specify-and-stub scope discipline (Part 8 + Part 10 calibration metrics live data Phase B) | (ii) Phase B | Operational discipline; not single-OQ but cross-Part scope; Phase B materialisation per part baselines. |
| OQ-MERGED-7 | U.System / U.Episteme distinction question | (i) Wave E ack-time | Constitutional-tier epistemic distinction; Ruslan judges whether Foundation Architecture treats system-as-tool vs system-as-knower; possibly closed-already by FUNDAMENTAL §0-§9 LOCKED v1.0 framing — Ruslan confirms. Surface in AWAITING-APPROVAL §4 conditionally. |
| OQ-CONFLICT-4 | A2A flag (agent-to-agent communication outside human gate) | (iv) **close-as-resolved-already** | Bundle 1 ack §6.x — Part 6b L8 mandates HITL ack; Part 4 §F anti-scope: no peer-to-peer negotiation; Bundle 4 §6.1 #7 §6.4 invariants. Architectural backstop holds. **CLOSED.** |

**Wave A merged routing:** 2 closed-already + 1 closed-via-D-6; 1 Phase B; 0 Phase C+; 1 Wave E; 0 Wave D fix.

## §6 Wave D-surfaced OQs (4 items)

| OQ | Description | Route | Rationale |
|---|---|---|---|
| OQ-WAVE-D-EDGE-TYPE-50 | Part 6a §D edge 10 uses non-canonical edge type "references" (gate-class taxonomy coupling); see D-2 §4 watch-item | (i) Wave E ack-time | Constitutional-tier edge taxonomy decision: extend A.14 OR re-label `methodologically-uses` (with caveat) OR formalise `references` as recognised lightweight edge type. Surface in AWAITING-APPROVAL §4. Coherence not blocked; the coupling works; only the edge-type label is at issue. |
| OQ-WAVE-D-PRIVACY-P2 | No explicit privacy-tagged-field schema in Part 2 §I; PII-redaction-on-intake policy implicit | (ii) Phase B | Operational; Foundation has Part 6b Default-Deny + Part 10 STRUCTURAL invariants as architectural backstop. |
| OQ-WAVE-D-PRIVACY-P3 | Admissibility predicate in Part 3 does NOT explicitly check `privacy:` frontmatter field | (ii) Phase B | Operational; backstop via Part 6b Default-Deny propagation. |
| OQ-WAVE-D-PRIVACY-P9 | No explicit PII-redaction policy on weekly-review draft-disposition | (ii) Phase B | Operational; backstop via Part 6b Default-Deny on draft_promotion gate. |

**Wave D-surfaced routing:** 1 Wave E; 3 Phase B; 0 Phase C+; 0 closed; 0 Wave D fix.

## §7 Aggregate routing summary

| Route | Count |
|---|---|
| (i) Wave E ack-time decision | 8 (B1-1 wording; B1-7 unshare-n; B1-8 stub file; B3-P5-5 dissolve criteria; B3-P8-5 Tier-1 default; B3-P8-6 voice SLI; OQ-MERGED-7; OQ-WAVE-D-EDGE-TYPE-50) |
| (ii) Phase B operational | 16 (B1-2; B1-4; B1-6; B2-C; B2-E; B3-P5-3; B3-P5-4; B3-P8-1; B3-P8-2; B3-P8-3; B3-P8-4; B4-1; B4-2; OQ-MERGED-5; OQ-WAVE-D-PRIVACY-P2/P3/P9) — actually 17 unique items |
| (iii) Phase C+ deferred | 4 (B1-3; B2-B; B2-F; B4-3) |
| (iv) close-as-resolved-already | 9 (B1-5; B2-A; B2-D; B2-WC; B3-P5-1; B3-P5-2; OQ-MERGED-2 via D-6; OQ-MERGED-3; OQ-CONFLICT-4) |
| (v) re-route as Wave D fix | 0 |

**Total OQs catalogued: 38** (8 + 7 + 11 + 3 + 5 + 4 = 38).
**Total routed: 38 (100%).** **Pass M-D-5.**

(Note: aggregate counts above show 8+17+4+9+0 = 38; matches total.)

## §8 Wave E ack-time decisions surfaced for Ruslan (8 items for AWAITING-APPROVAL §4)

These 8 items surface in the Wave D AWAITING-APPROVAL packet §4 for Ruslan
ack-time decision before Wave E LOCKED tag:

1. **OQ-B1-1** — F4/F6/F8 anchor wording refinements: accept proposed wording
   (F4="≥3 cycles applied"; F6="cross-cycle reuse evidence"; F8="FUNDAMENTAL
   Vision lock-class") OR retain FPF B.3 baseline?
2. **OQ-B1-7** — `unshare -n` availability on prod server: confirm available
   OR fall back to LD_PRELOAD/strace path?
3. **OQ-B1-8** — Create stub `decisions/policy/cross-fork-audit-deferred-phase-b.md`
   on Wave E ack? (Trivial; one-line.)
4. **OQ-B3-P5-5** — Dissolve-test "compound-phase-exclusive operation" judgment
   criterion — Ruslan validates D-6 verdict criteria (see D-6 cumulative
   evidence tally + STANDALONE verdict).
5. **OQ-B3-P8-5** — Tier 1+ Default-Deny default for novel alert class:
   confirm "default to Tier 1" (err on visibility side) for Phase A
   operational behaviour?
6. **OQ-B3-P8-6** — Voice pipeline success-rate SLI starter value 0.95: ack
   pre-Phase-B?
7. **OQ-MERGED-7** — U.System / U.Episteme distinction: Foundation treats
   system-as-tool (U.System) per FUNDAMENTAL Vision §0; ack as already-resolved
   OR re-open epistemic question? (Brigadier reads as already-resolved by
   FUNDAMENTAL LOCKED v1.0; Ruslan confirms.)
8. **OQ-WAVE-D-EDGE-TYPE-50** — Part 6a §D edge 10 "references" non-canonical
   edge type: extend A.14 / re-label `methodologically-uses` / formalise
   `references`? (Coherence not blocked; cosmetic precision question.)

## §9 M-D-5 Gate verdict

- [x] All 38 OQ items collected (Bundle 1-4 + Wave A merged + Wave D surfaced)
- [x] Each OQ routed to one of 5 categories
- [x] Per-OQ rationale included
- [x] Wave E ack-time OQs (8) surfaced explicitly for AWAITING-APPROVAL §4
- [x] OQ-MERGED-2 dissolve-test routed to D-6 verdict (closes via D-6)

**Pass threshold:** 100% routed; 0 unrouted. **Actual:** 38/38 routed (100%).
**PASS.**
