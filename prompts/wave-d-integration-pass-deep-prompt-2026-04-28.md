---
title: ROY Brigadier Deep Prompt — Wave D Integration Pass — FINAL GATE before Foundation Architecture LOCKED
date: 2026-04-28
type: deep-prompt
target: ROY brigadier (.claude/agents/brigadier.md)
parent_brief: prompts/cloud-code-wave-d-prompt-writing-brief-2026-04-28.md
predecessor_deep_prompts:
  - prompts/wave-c-bundle-1-deep-prompt-2026-04-28.md
  - prompts/wave-c-bundle-2-deep-prompt-2026-04-28.md
  - prompts/wave-c-bundle-3-deep-prompt-2026-04-28.md
  - prompts/wave-c-bundle-4-deep-prompt-2026-04-28.md
predecessor_ack_records:
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-28.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md
cycle: cyc-foundation-build-2026-04-28
wave: D
phase_count: 8
phases: [D-0 pre-flight, D-1 coverage matrix, D-2 inter-Part contracts, D-3 extended M3, D-4 FUNDAMENTAL coherence, D-5 OQ catalogue, D-6 dissolve-test verdict, D-7 synthesis + AWAITING-APPROVAL, D-8 optional retroactive supplement]
verification_gates: [M-D-1 coverage completeness, M-D-2 contracts verified, M-D-3 scenarios PASS rate, M-D-4 FUNDAMENTAL coherence, M-D-5 OQ catalogue routing, M-D-6 dissolve-test verdict]
estimated_walltime: 4-6h ROY substantive (1-2.5h likely at compound velocity); 12h ceiling
status: ready-for-brigadier-dispatch
output_word_count_target: 5K-8K (NOT 10K-20K; this is integration REPORT not bundle architecture)
substantive_mandate: INTEGRATION VERIFICATION — not creation
no_new_architecture: true
no_new_schemas: true
no_new_configs: true
no_wisdom_loop: true
mantra: "INTEGRATION > CREATION. VERIFICATION > INVENTION. HONEST-GAP-DECLARATION > PAPER-OVER. FOUNDATION-LOCKED-IS-THE-FINISH-LINE. RUSLAN-ACK > BRIGADIER-CONFIDENCE. THIS IS THE LAST GATE."
---

# Wave D Integration Pass — ROY Brigadier Deep Prompt — FINAL GATE before Foundation Architecture LOCKED

## §0 Mission Statement (READ FIRST, INTERNALIZE)

**Wave D is the INTEGRATION PASS. After Wave D → Wave E LOCKED tag → Foundation Architecture COMPLETED.** Ten Foundation parts are F5 LOCKED on `claude/jolly-margulis-915d34`: Part 1 (Bundle 1, supplement-corrected ×2), Part 6a (Bundle 1), Part 6b (Bundle 1), Part 2 (Bundle 2), Part 3 (Bundle 2), Part 4 (Bundle 2), Part 5 (Bundle 3), Part 8 (Bundle 3), Part 7 (Bundle 4), Part 9 (Bundle 4), Part 10 (Bundle 4). Bundle 4 acked 2026-04-28; head commit `236fefc`. **Wave D verifies that the 10 parts INTEGRATE.**

**Wave D is fundamentally different from Bundles 1-4.** Bundles 1-4 each CREATED 2-3 architecture documents (each 10K-20K words) with new schemas, new configs, Wisdom Application Loop, M-gates per part. Wave D produces NO new architecture documents, NO new schemas, NO new configs. Wave D produces:

1. **Cross-cutting concerns coverage matrix** (5 concerns × 10 parts = 50 cells) — verifies that each cross-cut (provenance, gating, append-only, fork-separation, privacy) is implemented coherently across all 10 parts.
2. **Inter-Part contract verification matrix** — for each typed A.14 edge declared in any §D Dependencies section across the 10 parts, verify the producer side emits what the consumer side expects.
3. **Extended M3 scenarios** (8-10 system-wide end-to-end traces) — Bundles 1-4 produced 4 per-bundle scenarios each (16 total); Wave D adds 8-10 SYSTEM-WIDE scenarios that traverse 5+ parts in a single trace.
4. **FUNDAMENTAL Vision §0-§9 coherence check** — verify all ~39 UC items from §1 are mapped to a Foundation part responsibility, and verify all ~77 §6 anti-scope items have at least one structural enforcement mechanism declared in some Foundation part.
5. **Open-questions catalogue** — collect all ~17 OQ-B*-* deferred items from Bundles 1-4 AWAITING-APPROVAL packets + Wave A unresolved items, and route each to (a) Wave E ack-time decision, (b) Phase B operational backlog, (c) Phase C+ deferred, (d) close-as-resolved-already, (e) re-route as Wave D fix.
6. **Dissolve-test Cycle 3 verdict** — OQ-MERGED-2 dissolve-test threshold check (≥3 distinct compound-phase-exclusive operations across full window); declare Part 5 standalone-preserved OR dissolve-into-Part-1+Part-3.
7. **AWAITING-APPROVAL packet** — Wave D summary; surfaces any integration gaps for Ruslan ack.
8. **Optional Phase D-8 retroactive supplement** — IF integration verification surfaces a real gap that requires a schema/config edit, brigadier authors a retroactive supplement (analogous to Bundle 1 supplement 1+2 patterns); IF no gap surfaces, Phase D-8 is skipped.

**Treat with 1 trillion percent responsibility. This is the final gate before Foundation Architecture LOCKED.**

The constitutional contract from Bundles 1+2+3+4 is permanent. Wave D does NOT re-litigate any F5/F8 LOCKED schema. Wave D VERIFIES that the integration is coherent — no missing edges, no contract gaps, no forgotten cross-cuts. **Honest-gap-declaration is mandatory** — if you find a gap, name it; do NOT paper over with prose.

---

## §1 Constitutional Inputs (Bundles 1+2+3+4 LOCKED — DO NOT re-litigate)

### §1.1 F8 LOCKED schemas (consumed verbatim)

Wave D consumes ALL of these as input contracts. NEVER edit. NEVER propose alternatives.

| Constitutional artefact | F-level | Source bundle | Wave D role |
|---|---|---|---|
| `f-g-r.json` (Part 6a §I.1) | F8 | Bundle 1 | Wave D output (integration report) carries F-G-R tag (`F4|G:wave-d-integration|R:integration-gap-surfaces`). |
| `awaiting-approval-packet.json` with `gate_class` enum (Part 6b §I.1) | F8 | Bundle 1 | Wave D AWAITING-APPROVAL packet conforms (`gate_class: stage_gate`). |
| `default-deny-table.yaml` (Part 6b §I.3) | F8 | Bundle 1 | Wave D coverage matrix verifies Default-Deny entries declared across parts (Privacy cross-cut). |
| `blast-radius-table.yaml` 4 tiers (Part 6b §I.4) | F8 | Bundle 1 | Wave D coverage matrix verifies blast-radius classification consistent across parts. |
| Halt-Log-Alert L9 (Part 6b §E) | F8 | Bundle 1 | Wave D scenarios verify ordering preserved end-to-end. |
| Corrigibility (Part 6b §E L9 / Askell HHH) | F8 | Bundle 1 | Wave D autocheck — no Wave D action locks Ruslan out. |
| WORD COUNT TARGET 10K-20K per architecture part | F8 | Bundle 2 | NOT applicable to Wave D output (5K-8K integration report). |
| `task-return-packet.json` (Part 4 §I.1) | F4→F5 | Bundle 2/3 | Wave D verifies Part 7 `project-retrospective-packet.json` is a SUPERSET (UND-3 finalised at Bundle 4). |
| Canonical health-signal schema (Part 8 §I.1) | F5 | Bundle 3 | Wave D verifies Part 7 + 9 + 10 emitter mapping declared. |
| `wiki/methodology/` entity-type + admissibility predicate (Part 3) | F4-F5 | Bundle 2/3 | Wave D verifies Part 5 promotion pipeline emits to this entity-type. |
| Message schema v2.0.0 with `acting_as:` (Part 4 §H) | F4 | Bundle 2 | Wave D verifies Bundle 4 messages (Part 7/9/10 emits) conform. |
| `cross-fork-provenance.json` v1.1.0 (Part 1 §I.1) | F8 | Bundle 1 + supplement 2 | Wave D verifies Part 10 §I.1 5 reconciliation strategies declaration aligned. |
| `wiki/graph/edges.jsonl` 9 typed edges + CRM 8 edge types | F4 | Bundle 2 | Wave D verifies Part 10 UND-5 binding. |
| `methodology-promotion-event.json` (Part 5 §I.1) | F5 | Bundle 3 | Wave D verifies Part 9 weekly-review surfaces these. |
| `sli-slo.json` (Part 8 §I.2) | F5 | Bundle 3 | Wave D verifies Bundle 4 health emissions conform. |
| PARA-tier mandatory (Part 2 P2.2; Part 9 daily-log; Part 10 CRM) | F5 | Bundle 2/4 | Wave D coverage matrix cross-cut. |
| `commit-format-tokens.json` (Part 1 §I.2) with [swarm-lib]+[health]+[methodology] tokens | F5 | Bundle 1 + supplement 1 | Wave D verifies all Bundle 1-4 commit messages used valid tokens. |
| `project-retrospective-packet.json` (Part 7 §I.2 — UND-3 finalised) | F4 | Bundle 4 | Wave D verifies M5 lite coherence still holds (Part 7 §B emit ↔ Part 5 §A.5 input). |
| `daily-log.json` + `weekly-review.json` (Part 9 §I.1/§I.2) | F4 | Bundle 4 | Wave D verifies methodology-candidate forwarding from §I.2 to Part 5. |
| 4 STRUCTURAL privacy invariants (Part 10 §I.5/§H.7/§F) | F8 | Bundle 4 | Wave D Privacy cross-cut row in coverage matrix. |
| 5 reconciliation strategies enum (Part 10 §I.1; Part 1 §I.1 v1.1.0) | F8 | Bundle 4 + Bundle 1 supplement 2 | Wave D Phase B partner-fork import scenario. |

### §1.2 RUSLAN-ACK records (constitutional inputs — full read mandatory)

1. `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` — Bundle 1 ack (Part 1 / 6a / 6b F5/F8; F-G-R F8; Default-Deny F8; blast-radius F8; AWAITING-APPROVAL packet schema F8; Halt-Log-Alert F8; Corrigibility F8; cross-fork-provenance.json schema)
2. `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md` — supplement 1 (Part 1 §I.4 enum + commit-format-tokens [swarm-lib]+[health]+[methodology] + K18 upcasting)
3. `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-28.md` — supplement 2 (cross-fork-provenance.json v1.1.0 approvals_reconciliation_strategy top-level + 5 strategies)
4. `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md` — Bundle 2 ack (Parts 2/3/4 F5; C1 Joint Design Variant A F5; routing-table.yaml F4; task-return-packet.json F4; WORD COUNT TARGET F8; message schema v2.0.0 F4)
5. `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md` — Bundle 3 ack (Parts 5/8 F5; C2 canonical health-signal schema F5; SLI/SLO schema F5; TRADEOFF-01 split F8; UND-2 methodology promotion pipeline F5; UND-3 P5↔P7 stub F2; OQ-MERGED-2 dissolve-test active)
6. `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md` — Bundle 4 ack (Parts 7/9/10 F5; UND-3 finalised F5; C4 nomenclature fix F8; OQ-MERGED-3 fork-separation FINAL CLOSURE F8; OQ-5 cadence event-driven F8; IP-2 single-owner bounded F8; Privacy STRUCTURAL F8; CRM canonicalisation F8; OQ-B1-5 D27 supplement F5)

### §1.3 Cross-cuts within Wave D (the 5 rows of the coverage matrix)

Wave D coverage matrix has 5 cross-cutting concern rows × 10 part columns = 50 cells. Each cell is one of: ✅ FULLY-IMPLEMENTED, 🟡 PARTIAL-WITH-DECLARED-GAP, ❌ MISSING (red flag), N/A (concern doesn't apply to this part — must justify).

| Cross-cut | Description | Per-cell verification |
|---|---|---|
| **CC-1: Provenance F-G-R** | Every promoted claim carries F-G-R tag per Part 6a §I.1 schema. | Grep `[F` tags in Part X §A-§N; verify ≥1 per major section. |
| **CC-2: Gating discipline** | Every external/risky action passes through Part 6b stage-gate (`gate_class: stage_gate` or `stop_gate` or `draft_promotion`). | Grep `gate_class` in Part X §H/§I; verify all blast-radius Tier 0/1 events route to Part 6b. |
| **CC-3: Append-only history** | Every state change is append-only with corrections via NEW entries (Reversal Transactions; Young 2010). | Grep "append-only" + verify §C Side-effects has no DELETE/UPDATE-IN-PLACE. |
| **CC-4: Fork-separation Foundation vs RUSLAN-LAYER** | Every part has explicit §X declaration distinguishing Foundation generic from RUSLAN-LAYER specifics. | Verify §X exists; verify ≥1 example each side; flag if missing. |
| **CC-5: Privacy structural** | Privacy invariants enforced via schema fields + lint signals + Default-Deny entries (NOT behavioral framing prose). | Verify Default-Deny entries cross-ref Part 6b §I.3; verify schema fields declared; verify <10% behavioral prose in privacy-touching sections. |

### §1.4 The 10 Foundation parts (column headers of coverage matrix)

| Part | Slug | F-level | Bundle | Domain |
|---|---|---|---|---|
| 1 | system-state-persistence | F5/F8 | Bundle 1 + supplements | Substrate (commit interface, F-G-R writes, cross-fork-provenance) |
| 2 | signal-ingestion-triage | F5 | Bundle 2 | Inbound signal triage (PARA-tier; STOP-gate) |
| 3 | knowledge-base-methodology-library | F5 | Bundle 2 | KB + methodology library + typed-edge graph |
| 4 | role-taxonomy-coordination-protocol | F5 | Bundle 2 | Routing-table + role manifests + task-return-packet |
| 5 | compound-learning-methodology-capture | F5 | Bundle 3 | Plan/Work/Review/Compound 40/10/40/10; methodology promotion |
| 6a | provenance-officer | F5/F8 | Bundle 1 | F-G-R officer; quarterly immune audit |
| 6b | human-gate | F5/F8 | Bundle 1 | Stage-gate; Default-Deny; blast-radius; Halt-Log-Alert |
| 7 | project-lifecycle-substrate | F5 | Bundle 4 | 5-state project state machine; Shape Up appetite; UND-3 emit |
| 8 | health-monitoring-system-integrity | F5 | Bundle 3 | Canonical health-signal schema; SLI/SLO; alert routing |
| 9 | owner-interaction-scaffold | F5 | Bundle 4 | Daily-log + weekly-review + 3-tier SLA; IP-2 single-owner bounded |
| 10 | external-touchpoints-network-interface | F5 | Bundle 4 | CRM canonicalisation; integration adapters; privacy STRUCTURAL |

---

## §2 Wave D Scope — Eight Phases, Six Verification Gates

### §2.1 What Wave D is NOT (autocheck — re-dispatch with verification-only mandate if scope creeps)

- **NOT** creation of new architecture documents (10 parts already F5 LOCKED).
- **NOT** creation of new schemas (`shared/schemas/*.json` declared inline in Bundles 1-4; Phase B physical generation per OQ-MERGED-5 specify-and-stub).
- **NOT** creation of new configs (`.claude/config/*.yaml` already shipped: project-types / wiki-roots / sg-banned-phrases / sla-taxonomy / ip5-past-participle-whitelist / commit-format-tokens / routing-table).
- **NOT** Wisdom Application Loop (already done per-Bundle; Bundle 4 hit 95% operational ratio; Wave D inherits).
- **NOT** re-dispatch of 5×4 expert matrix (already done per-Bundle; Wave D dispatches verification-mode reviewers only).
- **NOT** 10K-20K word architecture document (Wave D output is a 5K-8K integration report).
- **NOT** new typed A.14 edges (already declared per-part §D in Bundles 1-4).

If during execution brigadier finds itself drafting a new architecture document, declaring a new schema field, or invoking a Wisdom Application Loop pass: **HALT, autocheck §11.2, re-dispatch with verification-only mandate.**

### §2.2 What Wave D IS (the 8 phases)

**Phase D-0 — Pre-flight verification.** Brigadier reads §3 mandatory, verifies branch state (`claude/jolly-margulis-915d34`; clean working tree; head `236fefc` Bundle 4 ack), verifies all 10 parts F5 LOCKED, verifies all 5 ack records committed, verifies no active PR conflict. Output: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-0-pre-flight.md` (≤500 words; 10 verification ticks).

**Phase D-1 — Cross-cutting concerns coverage matrix.** Brigadier (or delegated reviewer-mode expert) builds the 5×10 = 50-cell matrix. For each cell: read the relevant Part X architecture, verify the cross-cut is implemented (per §1.3 verification rule), classify ✅/🟡/❌/N/A. Output: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-1-coverage-matrix.md` (≤2K words; 50-cell table + per-cell justification ≤2 sentences).

**Phase D-2 — Inter-Part contract verification matrix.** For each typed A.14 edge declared in any §D Dependencies section across the 10 parts, verify the producer side emits what the consumer side expects. Edge taxonomy (Bundle 1 canonical 10-edge): `ComponentOf` / `ConstituentOf` / `PortionOf` / `PhaseOf` / `MemberOf` / `AspectOf` / `creates` / `operates-in` / `methodologically-uses` / `constrained-by` / `derives-from`. Output: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-2-contracts-matrix.md` (≤2K words; per-edge row: edge-type, producer Part, consumer Part, contract-field-list, ✅ verified / 🟡 stub / ❌ gap).

**Phase D-3 — Extended M3 system-wide scenarios.** Bundles 1-4 produced 16 per-bundle scenarios (4 each). Wave D adds 8-10 SYSTEM-WIDE end-to-end scenarios that each traverse 5+ parts. Examples (final list at brigadier discretion): (a) full project lifecycle Bundle 4 Scenario 1 EXTENDED to include Part 2 ingest origin + Part 3 methodology promotion target; (b) Tier 0 protected-characteristic inference attempt → Halt-Log-Alert → Corrigibility verified → owner unlock path (Parts 10/6b/6a/8/1); (c) Phase B partner-fork import → 5 reconciliation strategies exercised → CRM canonicalisation imported / declined → privacy invariants inherited (Parts 10/1/3/6a); (d) Methodology promotion full pipeline: voice memo → /ingest → wiki concept → strategies.md → DRR ledger → admissibility predicate satisfied → wiki/methodology/ canonical (Parts 2/3/4/5/6b/1/9); (e) System-health degradation: Tier 1 health alert → owner notified per SLA L1 → blast-radius classify → mitigation path (Parts 8/9/6b/1); (f) external write-ack with consent missing → Default-Deny → AWAITING-APPROVAL stop_gate → Ruslan ack required → no fallthrough (Parts 10/6b/6a/1); (g) Project archive due to appetite exceedance → re-shape OR archive (NEVER extend) → retrospective emit → compound learning (Parts 7/5/4/1); (h) Daily-log → weekly-review → draft-disposition table → 3 drafts marked `accept` → Part 6b draft_promotion gate × 3 (Parts 9/6b/1). Document trace per scenario (which Part fires which schema/event in which order). Output: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-3-extended-scenarios.md` (≤2.5K words; 8-10 scenarios; PASS/FAIL verdict per scenario).

**Phase D-4 — FUNDAMENTAL Vision §0-§9 coherence check.** Verify all FUNDAMENTAL Vision LOCKED v1.0 use-cases and anti-scope items are coherently mapped to Foundation parts. Two sub-checks: (a) **UC mapping** — for each of the ~39 UC items in §1 (UC-A.1 through UC-L.3 across 12 categories A-L), declare which Foundation Part(s) implement(s) the UC; flag any UC with no mapped Part as a coverage gap; (b) **Anti-scope verification** — for each of the ~77 anti-scope items in §6 ("система НЕ делает X"), verify ≥1 Foundation Part has a structural enforcement mechanism (Default-Deny entry / lint signal / schema constraint / §F Anti-scope declaration); flag any anti-scope item with no enforcement as a gap. Output: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-4-fundamental-coherence.md` (≤2K words; UC mapping table + anti-scope enforcement table).

**Phase D-5 — Open-questions catalogue.** Collect all OQ-B*-* items deferred from Bundles 1-4 (estimated ~17 items: OQ-B1-1 through OQ-B1-8; OQ-B2-A/B/C/D/E/F/WC; OQ-B3-P5-1 through P5-5; OQ-B3-P8-1 through P8-6; OQ-B4-1/B4-2/B4-3) plus any unresolved Wave A items (OQ-MERGED-2 dissolve-test threshold check; OQ-MERGED-3 already CLOSED; OQ-MERGED-5 specify-and-stub; OQ-MERGED-7 U.System/U.Episteme; OQ-CONFLICT-4 A2A flag). For each: route to one of (i) **Wave E ack-time decision** (constitutional-tier item Ruslan must ack; surfaces in Wave D AWAITING-APPROVAL packet); (ii) **Phase B operational backlog** (calibration / observation / test-fixture work post-Foundation-LOCKED); (iii) **Phase C+ deferred** (multi-owner / multi-tenant / scale-dependent items); (iv) **close-as-resolved-already** (item already addressed by a Bundle 1-4 decision; document resolution); (v) **re-route as Wave D fix** (item is small enough to fix in Wave D-8 retroactive supplement). Output: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-5-oq-catalogue.md` (≤2K words; per-OQ row: ID, description, source bundle, route, rationale).

**Phase D-6 — Dissolve-test Cycle 3 verdict.** OQ-MERGED-2 dissolve-test: Bundle 3 = Cycle 1 (Bundle 3 evidence count); Bundle 4 = Cycle 2 (2.5 entries); Wave D = Cycle 3 (close decision window). Threshold: ≥3 distinct compound-phase-exclusive operations across full Cycle 1+2+3 window. Read Bundle 3 + Bundle 4 dissolve-test evidence files; tally cumulative count; brigadier accumulates own Wave D Cycle 3 evidence (typically 0-2 entries since Wave D is verification not creation); render verdict: **STANDALONE PRESERVED** (≥3 distinct operations witnessed; Part 5 holds as separate Foundation Part) OR **DISSOLVE INTO PART-1+PART-3** (<3 distinct operations; Part 5 should be merged into Part 1 substrate + Part 3 methodology library; constitutional refactor required). Output: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-6-dissolve-test-verdict.md` (≤1K words; cumulative evidence table + verdict + rationale; if DISSOLVE verdict, escalate to Ruslan via dedicated AWAITING-APPROVAL packet — DO NOT auto-execute the dissolution).

**Phase D-7 — Synthesis + AWAITING-APPROVAL packet.** Brigadier integrates D-1 through D-6 outputs into a single 5K-8K integration report at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md`. Then brigadier drafts AWAITING-APPROVAL packet at `decisions/AWAITING-APPROVAL-wave-d-integration-pass-2026-04-XX.md` (XX = day of completion). Then **STOP** for Ruslan ack.

**Phase D-8 — Optional retroactive supplement.** ONLY IF integration verification surfaces a real schema/config gap (e.g., a typed A.14 edge with no producer or no consumer; a cross-cut cell ❌ with concrete fix; a UC item with no Foundation mapping that's blocking). Brigadier authors a retroactive supplement record analogous to Bundle 1 supplement 1+2 patterns (`decisions/RUSLAN-ACK-WAVE-C-BUNDLE-N-supplement-M-2026-04-XX.md`) and edits the relevant Part architecture in-place. Single commit. Phase D-8 is the ONLY phase where Wave D writes to Foundation architectures. **If no gap surfaces, Phase D-8 is SKIPPED.** If gap surfaces but is too large for a supplement (e.g., requires re-architecture of a Part), brigadier escalates to Ruslan via dissent.md and DOES NOT auto-fix.

### §2.3 Wave D verification gates (M-D-1 through M-D-6)

These are NEW gates specific to Wave D — not the M1/M2/M3/M4/M5/M6 gates of Bundles 1-4.

| Gate | Phase | Check | Pass threshold |
|---|---|---|---|
| **M-D-1 Coverage matrix completeness** | D-1 | All 50 cells classified; ≤5 cells 🟡; 0 cells ❌; N/A cells justified | 50/50 cells classified; 0 ❌ |
| **M-D-2 Contracts verified** | D-2 | All declared typed A.14 edges across 10 parts have producer + consumer verified or 🟡 stub flagged | ≥95% verified; 0 silent gaps |
| **M-D-3 Extended scenarios PASS rate** | D-3 | 8-10 system-wide scenarios; each traverses 5+ parts | ≥8 scenarios PASS; 0 FAIL silent |
| **M-D-4 FUNDAMENTAL coherence** | D-4 | All UC items mapped; all anti-scope items enforced or flagged | ≥95% UC mapped; ≥95% anti-scope enforced; gaps flagged for Ruslan |
| **M-D-5 OQ catalogue routing** | D-5 | All ~17 OQ items routed to one of 5 categories | 100% routed; 0 unrouted |
| **M-D-6 Dissolve-test verdict** | D-6 | Cumulative evidence tallied; verdict rendered with rationale | Verdict declared (STANDALONE or DISSOLVE); evidence tallied |

If any gate fails: brigadier returns to relevant phase with explicit feedback. If repeated failure: escalate to Ruslan via `swarm/wiki/cycles/.../wave-d/escalation-N.md`.

---

## §3 Required Reading — MANDATORY before first dispatch

Brigadier MUST read these BEFORE any subagent dispatch (or before starting brigadier-direct verification work). Each pre-read MUST be cited in the integration report.

### §3.1 Constitutional baseline (full-read mandatory)

1. `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0) — Phase D-4 binding. Esp. **§1 (39 UC items across 12 categories A-L)**, **§2 (потоки)**, **§3 (health indicators)**, **§4.2-§4.3 human-only tasks + 3-tier SLA**, **§6 anti-scope (77 items)**, **§7 roles + agency**, **§8 layered evolution**.
2. `design/JETIX-FPF.md` — IP-1 through IP-9 binding for cross-cut verification. **A.14 typed edges canonical 10-edge taxonomy** for D-2 contracts matrix.
3. `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` — operational baseline reference (CRM cycle 10; daily-log baseline; projects/ baseline; agents/ baseline; swarm/lib/).
4. `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` — overall cycle frame.
5. **All 5 RUSLAN-ACK records** (Bundle 1 + supplement 1 + supplement 2 + Bundle 2 + Bundle 3 + Bundle 4) per §1.2.
6. Locks D17 (Notion read-only), D26 (hub-and-spoke), D27 (forkable + ICP external), D29 (Korp-Startup), `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md`.

### §3.2 All 10 LOCKED Foundation architectures (full read mandatory; brigadier may dispatch parallel reads OK; ALL 10 must be covered)

Each architecture is ~10K words; total ~95K words. Brigadier MAY parallelise via reviewer-mode expert dispatches with explicit `read this Part X architecture and report which §A-§N sections cover which cross-cut from §1.3 + which UC items from FUNDAMENTAL §1` instruction. Brigadier consolidates reports.

1. `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` (esp. §H commit interface; §I.1 cross-fork-provenance.json v1.1.0; §I.2 commit-format-tokens.json with 4 tokens + [swarm-lib]+[health]+[methodology]; §I.4 task-return-packet stub-now-aligned-to-Part-4-full-schema; §K K15+K18+K18-upcasting failure modes)
2. `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md` (esp. PARA-tier discipline; anchor-mandatory; STOP-gate; 6 input types; C3 cross-ref Part 10 inbound external)
3. `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` (esp. `wiki/methodology/` entity-type; `wiki/graph/edges.jsonl` typed-edge taxonomy; UND-5 Part 10 binding; accessor pipeline)
4. `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` (esp. routing-table.yaml; **task-return-packet.json schema F4 — Part 7 SUPERSET binding via UND-3**; executor-binding template; message schema v2.0.0)
5. `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` (esp. compound ritual 40/10/40/10; UND-2 methodology promotion pipeline; **§A.5 Inputs Part 7 finalised — UND-3 closure verified**; dissolve-test condition F3)
6. `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` (esp. F-G-R schema F8; approval log; quarterly immune audit framework)
7. `swarm/wiki/foundations/part-6b-human-gate/architecture.md` (esp. gate_class enum F8; Default-Deny F8; blast-radius 4-tier F8; Halt-Log-Alert L9 F8; Corrigibility F8; AWAITING-APPROVAL packet F8)
8. `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` (esp. 5-state IP-5 past-participle state machine; §B project-retrospective-packet.json schema; §E Laws cadence event-driven OQ-5 4 laws verbatim; appetite-as-CONSTRAINT; §X Foundation vs RUSLAN-LAYER)
9. `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md` (esp. canonical health-signal schema F5 §I.1; SLI/SLO schema §I.2; alert-routing stub §H; specify-and-stub scope discipline)
10. `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` (esp. daily-log §I.1; weekly-review §I.2 with draft-disposition table; SLA taxonomy §I.3; §X IP-2 single-owner bounded with multi-owner stub fields §I.4; §D every Part 6 reference uses `methodologically-uses Part 6` not `PhaseOf Part 6` — C4 fix)
11. `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md` (esp. CRM canonicalisation §A.1+§H.1+§I.2 references existing 24 src / 35 tests / 10 skills / 4 schemas; integration adapter pattern §I.4 RT-1+RT-2+L.1/L.2/L.3; §I.5 privacy STRUCTURAL 4 invariants; §F C3 Phase A inbound boundary; §X FINAL CLOSURE with explicit DACH/GDPR/auth-token/contact-list/r/Berlin examples; §I.1 5 reconciliation strategies)

### §3.3 All 4 Bundle AWAITING-APPROVAL packets (deferred OQ source — ~17 items)

1. `decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-28.md` — esp. §3 (OQ-B1-1 through OQ-B1-8)
2. `decisions/AWAITING-APPROVAL-wave-c-bundle-2-2026-04-28.md` — esp. §3 (OQ-B2-A/B/C/D/E/F/WC)
3. `decisions/AWAITING-APPROVAL-wave-c-bundle-3-2026-04-28.md` — esp. §3 (OQ-B3-P5-1 through P5-5; OQ-B3-P8-1 through P8-6)
4. `decisions/AWAITING-APPROVAL-wave-c-bundle-4-2026-04-28.md` — esp. §5 (OQ-B4-1/B4-2/B4-3)

### §3.4 Wave A artefacts (verification reference)

1. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md`
2. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md`
3. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md` — Phase D-2 contracts matrix uses §3 contradictions catalog + §4 understandings.
4. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md`
5. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md`
6. **All 10 Wave A interface cards** in `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/` — Phase D-2 source-of-truth for declared edges (per Wave A §A-§B card schema).

### §3.5 Wave B 14 consultant cards (verification reference; D-1 cross-cut justifications)

`swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/` — 14 cards. Wave D does NOT re-run Wisdom Loop; Wave D references cards if a coverage cell justification cites a consultant principle.

### §3.6 Wave B Supplement library-direct sources (5 items)

1. `raw/books-md/anthropic/bai-2022-cai.md` (Constitutional AI)
2. `raw/books-md/anthropic/askell-2021-hhh.md` (HHH)
3. `raw/books-md/event-sourcing/young-cqrs-2010.md` (Reversal Transactions)
4. `raw/books-md/sre/google-sre-book.md` (Ch.6 + Ch.15)
5. `raw/books-md/sre/google-srewb-implementing-slos.md` (Ch.2)

### §3.7 Schemas + configs (verification reference)

- `shared/schemas/*` — declared schemas (Phase B physical generation pending)
- `.claude/config/project-types.yaml`
- `.claude/config/wiki-roots.yaml`
- `.claude/config/sg-banned-phrases.yaml`
- `.claude/config/sla-taxonomy.yaml` (Bundle 4)
- `.claude/config/ip5-past-participle-whitelist.yaml` (Bundle 4)
- `.claude/config/commit-format-tokens.json` (Bundle 1 + supplement 1)
- `.claude/config/routing-table.yaml` (Bundle 2)

### §3.8 Operational baselines (verification reference; CC-4 fork-separation cross-cut)

- **CRM tree**: `crm/` (24 source files; 35 tests; 10 skills; 4 schemas) — Part 10 CC-4 reference
- **Agents**: `agents/<id>/strategies.md` — Part 5 methodology promotion source
- **Swarm-lib**: `swarm/lib/` (routing-table.yaml; shared-protocols.md; hooks/) — Part 4 substrate
- **Daily-log**: `daily-log/` directory — Part 9 baseline
- **Projects**: `projects/` directory — Part 7 baseline

---

## §4 Phase Architecture (matrix-light + verification mode)

Standard ROY cycle for Wave D = **Phase D-0 pre-flight → D-1 → D-2 → D-3 → D-4 → D-5 → D-6 → D-7 synthesis + AWAITING-APPROVAL → optional D-8 retroactive supplement → STOP**.

### §4.1 Brigadier dispatch mode (DIFFERENT from Bundles 1-4)

Bundles 1-4 used 5×4 expert matrix (5 experts × 4 modes = up to 20 cells per Part). Wave D uses **REVIEWER-MODE only** dispatches: brigadier may delegate phase-specific reviewer work to up to 2 concurrent (HD-02 N=2) experts with explicit "verify, do not invent" mandate.

**Acceptable dispatch patterns:**
- D-1 coverage matrix: brigadier may dispatch 2 reviewers in parallel — one for cross-cuts CC-1+CC-2+CC-3 (provenance / gating / append-only), one for CC-4+CC-5 (fork-separation / privacy). Brigadier consolidates.
- D-2 contracts matrix: brigadier may dispatch 1 reviewer for typed-edge enumeration, then brigadier verifies producer-consumer pairs.
- D-3 extended scenarios: brigadier authors directly OR dispatches 1 reviewer with explicit scenario list.
- D-4 FUNDAMENTAL coherence: brigadier may dispatch 1 reviewer for UC mapping + 1 reviewer for anti-scope enforcement.
- D-5 OQ catalogue: brigadier authors directly (cross-bundle synthesis is brigadier work).
- D-6 dissolve-test verdict: brigadier authors directly (cumulative evidence judgment).
- D-7 synthesis: brigadier authors directly (the integration report is brigadier's product).
- D-8 retroactive supplement: brigadier authors directly IF triggered.

**Unacceptable dispatch patterns:**
- Spawning expert-mode (critic / optimizer / integrator / scalability) cells for Wave D — verification only.
- Spawning >2 concurrent dispatches — HD-02 N=2 hard cap.
- Dispatching subagents to write new architecture content — verification only.

### §4.2 No Wisdom Application Loop

Wave D does NOT run Wisdom Application Loop. Bundles 1-4 already applied 14 consultant cards + 5 library-direct sources via 4 separate Wisdom Loop passes (Bundle 1 50/50 mix; Bundle 2 89% operational; Bundle 3 100% operational; Bundle 4 95% operational). If during Wave D verification brigadier identifies a consultant principle not yet applied that would close an integration gap, brigadier flags it as `OQ-WAVE-D-N` for Ruslan ack-time decision (Wave E or Phase B retroactive Wisdom Loop) — does NOT auto-apply.

### §4.3 No M5 inter-Part lite coherence as separate phase

Wave D inherits M5 from Bundle 4 (UND-3 finalised; C4 fix applied; OQ-B1-5 D27 supplement F8 LOCKED). Wave D verification reuses M5 results.

### §4.4 Phase D-7 synthesis — the integration report structure

The integration report at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md` follows this skeleton (5K-8K words total):

```markdown
---
title: Wave D Integration Report — Foundation Architecture coherence verification
date: 2026-04-XX
type: integration-report
F: F4
G: wave-d-integration
R: refuted_if_integration_gap_surfaces
cycle: cyc-foundation-build-2026-04-28
wave: D
---

## §0 Executive Summary
[3-5 paragraphs: Wave D verifies 10 LOCKED parts integrate; cross-cut coverage; contracts verified; scenarios PASS; FUNDAMENTAL coherence; OQ catalogue routed; dissolve-test verdict; gaps surfaced (if any).]

## §1 Cross-cutting Concerns Coverage Matrix (D-1)
[5×10 = 50-cell table; per-cell ✅/🟡/❌/N/A; per-row summary; per-column summary; 🟡/❌ cells listed with proposed fix.]

## §2 Inter-Part Contract Verification (D-2)
[Per-edge table: producer Part / consumer Part / edge type / contract fields / ✅ verified / 🟡 stub / ❌ gap; total edge count; gap list.]

## §3 Extended M3 Scenarios (D-3)
[8-10 system-wide scenarios; per-scenario trace summary (≤200 words); PASS/FAIL verdict; failure analysis if any.]

## §4 FUNDAMENTAL Vision §0-§9 Coherence (D-4)
[UC mapping table (~39 rows: UC-A.1..UC-L.3 → Foundation Part(s)); anti-scope enforcement table (~77 rows: anti-scope item → enforcing Part + mechanism); gap summary.]

## §5 Open-Questions Catalogue (D-5)
[Per-OQ table (~17 rows): OQ ID / source bundle / description / Wave D routing decision / rationale; Wave E ack-time decision OQs surfaced for Ruslan.]

## §6 Dissolve-test Cycle 3 Verdict (D-6)
[Cumulative evidence Cycle 1+2+3; verdict STANDALONE or DISSOLVE; rationale; if DISSOLVE, escalation note.]

## §7 Optional Retroactive Supplement (D-8 — if triggered)
[If gap surfaced and supplement authored, link supplement record + describe gap closure. If skipped, "No retroactive supplement required — integration coherent."]

## §8 Foundation Architecture LOCKED Readiness
[Brigadier judgment: is Foundation ready for Wave E LOCKED tag? If YES — recommend Wave E dispatch. If NO — list blocking gaps + proposed resolutions.]

## §9 Provenance + Citations
[Every claim cites a source ($src:path) per Part 6a §C citation discipline.]
```

---

## §5 Quality Bar (HARD RULES)

### §5.1 Word count target: 5K-8K integration report (NOT 10K-20K)

Wave D output is an **integration report** not a bundle architecture. Word count target: **5,000-8,000 words** for `INTEGRATION-REPORT.md`. Auxiliary phase outputs (D-1 through D-6 separate files) are ≤2K each, total auxiliary ≤10K.

If integration report drafts <5K words: review for missing phase coverage. Re-draft with phase-specific expansion.
If integration report drafts >8K words: review for redundancy with auxiliary phase files. Tighten.
**DO NOT scope-creep into 10K-20K bundle-architecture-style document.** That is the autocheck failure.

### §5.2 Anti-cargo-cult enforcement

Per Bundle 1 Part 6a §C citation discipline: every `[src:...]` citation MUST be followed within 200 chars by a concrete consequence sentence. **Wave D specific rule**: citations should primarily reference Bundle architectures + ACK records (verification of declared work), NOT consultant cards (verification ≠ Wisdom application). If a Wave D claim cites a consultant card, ask "is this a verification of an applied principle, OR am I drifting into Wisdom Loop territory?" — drift = re-dispatch with verification-only mandate.

### §5.3 Typed A.14 edges (D-2 contracts matrix discipline)

D-2 verifies edges declared in Bundles 1-4 §D Dependencies sections. **NO new edge types invented in Wave D.** If verification finds an edge that should have been declared but isn't, flag as gap (route to Phase D-8 retroactive supplement OR Wave E ack-time decision); do NOT auto-add.

### §5.4 F-G-R DOGFOOD per F8 schema

Wave D integration report carries F-G-R tag in frontmatter (`F: F4`, `G: wave-d-integration`, `R: refuted_if_integration_gap_surfaces`). Per-section F-G-R inline tags optional but encouraged for major findings.

### §5.5 Honest-gap-declaration

If Wave D verification surfaces a gap, **NAME IT EXPLICITLY**. Do NOT paper over with "looks good overall" prose. Brigadier autocheck §11.2 rejects integration report sections that conclude positively without per-cell/per-edge/per-scenario evidence.

### §5.6 No new architecture content (scope-creep autocheck)

Wave D produces:
- Verification matrices (D-1, D-2)
- Scenario traces (D-3)
- Mapping tables (D-4)
- OQ routing table (D-5)
- Dissolve-test verdict (D-6)
- Integration report synthesis (D-7)
- AWAITING-APPROVAL packet (D-7)
- Optional retroactive supplement (D-8)

Wave D does NOT produce:
- New §A-§N architecture document
- New schema declaration
- New `.claude/config/*.yaml` file
- New `swarm/wiki/foundations/<part-slug>/` content (except D-8 supplement edits)
- New consultant card
- New Wisdom Loop pass

If brigadier finds itself drafting ANY of the second list: **HALT, re-dispatch with verification-only mandate.**

---

## §6 Verification Gates (M-D-1 through M-D-6)

### §6.1 M-D-1 Coverage matrix completeness

- [ ] All 50 cells classified ✅/🟡/❌/N/A
- [ ] N/A cells justified (concern doesn't apply to this part — explain why)
- [ ] 🟡 cells have proposed fix or "Phase B work" reasoning
- [ ] 0 cells ❌ silent (every ❌ has explicit gap declaration + proposed fix)
- [ ] Per-row summary (cross-cut adoption rate across 10 parts)
- [ ] Per-column summary (cross-cut coverage of single Part)

Pass threshold: 50/50 cells classified; 0 silent ❌ cells; ≤5 🟡 cells with proposed fix.

### §6.2 M-D-2 Contracts verified

- [ ] All declared typed A.14 edges in Bundles 1-4 §D Dependencies sections enumerated
- [ ] For each edge: producer Part identified; consumer Part identified
- [ ] For each edge: contract fields (what producer emits / consumer expects) listed
- [ ] For each edge: ✅ verified (producer + consumer agree on schema), 🟡 stub (Phase B materialisation), ❌ gap (producer or consumer missing)
- [ ] 0 silent ❌ gaps

Pass threshold: ≥95% verified; 0 silent gaps.

### §6.3 M-D-3 Extended scenarios PASS rate

- [ ] 8-10 system-wide scenarios authored
- [ ] Each scenario traverses 5+ parts
- [ ] Per-scenario trace documents which Part fires which schema/event in which order
- [ ] Per-scenario PASS/FAIL verdict
- [ ] Failed scenarios have failure analysis + gap routing

Pass threshold: ≥8 scenarios PASS; ≤2 FAIL with explicit gap routing.

### §6.4 M-D-4 FUNDAMENTAL coherence

- [ ] UC mapping table covers all ~39 UC items from FUNDAMENTAL §1
- [ ] Each UC item maps to ≥1 Foundation Part responsibility (or flagged as gap)
- [ ] Anti-scope enforcement table covers all ~77 anti-scope items from FUNDAMENTAL §6
- [ ] Each anti-scope item has ≥1 structural enforcement mechanism (Default-Deny / lint / schema constraint / §F declaration) (or flagged as gap)
- [ ] Gap summary lists UC items + anti-scope items needing Wave E ack-time decision

Pass threshold: ≥95% UC mapped; ≥95% anti-scope enforced; gaps flagged for Ruslan.

### §6.5 M-D-5 OQ catalogue routing

- [ ] All ~17 OQ-B*-* items collected from Bundle 1-4 AWAITING-APPROVAL packets
- [ ] Plus Wave A unresolved items (OQ-MERGED-2 dissolve-test threshold check; OQ-MERGED-5; OQ-MERGED-7; OQ-CONFLICT-4)
- [ ] Each OQ routed to one of 5 categories: Wave E ack-time / Phase B operational / Phase C+ deferred / close-as-resolved / re-route as Wave D fix
- [ ] Per-OQ rationale included
- [ ] OQs routed to Wave E ack-time surface in AWAITING-APPROVAL packet

Pass threshold: 100% routed; 0 unrouted.

### §6.6 M-D-6 Dissolve-test verdict

- [ ] Cumulative evidence count from Bundle 3 Cycle 1 + Bundle 4 Cycle 2 + Wave D Cycle 3 tallied
- [ ] Threshold check: ≥3 distinct compound-phase-exclusive operations across full window
- [ ] Verdict declared: STANDALONE PRESERVED OR DISSOLVE INTO PART-1+PART-3
- [ ] Rationale documented
- [ ] If DISSOLVE: escalation to Ruslan via dedicated AWAITING-APPROVAL packet (DO NOT auto-execute dissolution)

Pass threshold: verdict declared with rationale.

---

## §7 Output Expected (exact paths, structures)

### §7.1 Per-phase auxiliary output files

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-0-pre-flight.md` (≤500 words)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-1-coverage-matrix.md` (≤2K words)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-2-contracts-matrix.md` (≤2K words)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-3-extended-scenarios.md` (≤2.5K words)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-4-fundamental-coherence.md` (≤2K words)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-5-oq-catalogue.md` (≤2K words)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/D-6-dissolve-test-verdict.md` (≤1K words)

### §7.2 Main integration report

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md` (5K-8K words; structure per §4.4)

### §7.3 AWAITING-APPROVAL packet

- `decisions/AWAITING-APPROVAL-wave-d-integration-pass-2026-04-XX.md` (XX = day of completion)

Structure mirrors Bundle 1-4 packets but adapted to Wave D scope:

```markdown
---
title: AWAITING-APPROVAL — Wave D Integration Pass — FINAL GATE before Foundation Architecture LOCKED
date: 2026-04-XX
type: awaiting-approval
cycle: cyc-foundation-build-2026-04-28
wave: D
parent_packet: decisions/AWAITING-APPROVAL-wave-c-bundle-4-2026-04-28.md
predecessor_acks:
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-28.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md
deep_prompt: prompts/wave-d-integration-pass-deep-prompt-2026-04-28.md
status: awaiting-ruslan-ack
F: F4
ClaimScope: "Holds for Wave D integration verification across 10 LOCKED Foundation parts. Output = INTEGRATION-REPORT.md + 7 phase auxiliary files. Does NOT modify Bundle 1-4 architectures (except optional Phase D-8 retroactive supplement if integration gap surfaces). Recommends Wave E LOCKED tag (or blocks with gap list)."
R:
  refuted_if: "Ruslan walkthrough surfaces an unflagged integration gap, an UC item with no Foundation mapping that should map, an anti-scope item with no enforcement that should have enforcement, an OQ routed to wrong category, OR dissolve-test verdict disputed"
  accepted_if: "Ruslan acks the integration report AND the OQ catalogue routing AND the dissolve-test verdict AND any Wave E ack-time decisions surfaced AND any optional D-8 retroactive supplement"
next_action: "Ruslan ack of this packet → Wave E LOCKED tag dispatch → Foundation Architecture COMPLETED"
final_gate_before_foundation_locked: true
---

## §1 Executive Summary
## §2 Outcomes — Coverage / Contracts / Scenarios / FUNDAMENTAL / OQ / Dissolve-test
## §3 M-D-1 through M-D-6 gate results
## §4 Open Questions surfaced for Wave E ack-time decision
## §5 Optional Phase D-8 retroactive supplement (if any)
## §6 Provenance
## §7 Ruslan Ack Request (specific decisions)
## §8 STOP — Wave D COMPLETE; ready for Wave E LOCKED tag
```

### §7.4 Optional retroactive supplement (D-8 — if triggered)

- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-N-supplement-M-2026-04-XX.md` (analogous to Bundle 1 supplement 1+2 patterns)
- Plus the relevant Part architecture edit committed atomically with the supplement record

### §7.5 STOP

After AWAITING-APPROVAL packet committed and pushed AND optional D-8 supplement committed and pushed: **STOP. WAVE D COMPLETE.** Brigadier waits for Ruslan ack → Wave E LOCKED tag = Foundation Architecture COMPLETED.

---

## §8 Branch + Commit Discipline

- **Branch**: `claude/jolly-margulis-915d34` (current). Do NOT create new branches.
- **Commit cadence**: small + frequent. After each phase D-0 through D-7. (Phase D-8 atomic if triggered.)
- **Commit message format** examples:
  - `[wave-d] D-0 pre-flight verification PASS`
  - `[wave-d] D-1 cross-cutting concerns coverage matrix (50 cells; X✅/Y🟡/Z❌)`
  - `[wave-d] D-2 inter-Part contract verification matrix (N edges; X verified)`
  - `[wave-d] D-3 extended M3 system-wide scenarios (8 scenarios; X PASS / Y FAIL)`
  - `[wave-d] D-4 FUNDAMENTAL §0-§9 coherence (UC mapping + anti-scope enforcement)`
  - `[wave-d] D-5 OQ catalogue routing (~17 items)`
  - `[wave-d] D-6 dissolve-test Cycle 3 verdict — STANDALONE PRESERVED (or DISSOLVE)`
  - `[wave-d] D-7 INTEGRATION-REPORT synthesis + AWAITING-APPROVAL packet`
  - `[architecture] Bundle N retroactive supplement M — <gap closure description> (Phase D-8)` (only if triggered)
- **Push cadence**: after each commit. No force-push. No `--amend`. No `--no-verify`.
- **API-key audit**: before each commit run `grep -rEn 'ANTHROPIC_API_KEY|GROQ_API_KEY|OPENAI_API_KEY|sk-ant-' <staged-files>` → 0 hits required.
- **Commit area tokens**: Wave D introduces `[wave-d]` token (per Part 1 §I.2 commit-format-tokens.json — verify token is registered or flag as OQ for Phase D-8 supplement).

---

## §9 Operational Constraints

1. `unset ANTHROPIC_API_KEY` before any provider invocation. NEVER reference provider API-key env vars in code paths.
2. `ulimit -n 65535` if not already set.
3. **HD-02 rate limiter N=2 normal mode**. Maximum 2 concurrent dispatches.
4. **Read tool 32MB limit**: brigadier may parallelise reads of the 10 Part architectures via reviewer-mode dispatches; for large architectures use `offset`/`limit` parameters.
5. **NO auto-execution of Wave E after Wave D** — explicit STOP per §10.
6. **No `--amend`, no `--no-verify`, no force-push** — git-native rollback via `git revert` only.
7. **Frontmatter compliance**: every `.md` artefact carries YAML frontmatter.
8. **Untouchable trees in Phase A**: 14 legacy `.claude/agents/*.md` files; v2 `wiki/` tree; CRM operational baseline (24 src / 35 tests / 10 skills / 4 schemas); 10 LOCKED Foundation architectures (except D-8 supplement edits).
9. **Wave D writes to `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/` for phase auxiliary files + `swarm/wiki/cycles/.../wave-d/INTEGRATION-REPORT.md` for synthesis + `decisions/AWAITING-APPROVAL-wave-d-integration-pass-2026-04-XX.md`.** Wave D does NOT write elsewhere except via Phase D-8 retroactive supplement (if triggered).
10. **Security — never touch**: `~/.ssh/`, `/etc/`, any `.env*`, anything under `private/`, Tier-4 closed-core book corpus.
11. **Working directory**: `/home/ruslan/jetix-os/`. Do not `cd` outside.
12. **NO Wisdom Application Loop** — Wave D is verification, not Wisdom invocation.
13. **NO 5×4 expert matrix** — reviewer-mode dispatches only.
14. **NO new architecture content** — scope-creep autocheck per §5.6.
15. **HONEST-GAP-DECLARATION mandatory** — name gaps explicitly per §5.5.

---

## §10 STOP Rule + Ack Mantra

### §10.1 STOP rule

After AWAITING-APPROVAL packet (`§7.3`) is committed and pushed AND optional D-8 supplement (if triggered) committed and pushed:

**STOP. WAVE D IS COMPLETE.** Brigadier waits for HITL signal (Ruslan ack of Wave D AWAITING-APPROVAL packet → Wave E LOCKED tag).

Final action: notify Ruslan via tmux output (or stdout if no tmux):

> «Wave D Integration Pass complete. **THIS IS THE LAST GATE BEFORE FOUNDATION ARCHITECTURE LOCKED.**
> AWAITING-APPROVAL packet at `decisions/AWAITING-APPROVAL-wave-d-integration-pass-2026-04-XX.md`.
> Integration report at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md`.
> Coverage matrix: 50 cells classified — X ✅ / Y 🟡 / Z ❌ / W N/A.
> Inter-Part contracts: N typed A.14 edges enumerated; X verified / Y stubs / Z gaps.
> Extended M3 scenarios: N system-wide scenarios; X PASS / Y FAIL.
> FUNDAMENTAL coherence: ~39 UC items mapped (X gaps); ~77 anti-scope items enforcement-verified (Y gaps).
> OQ catalogue: ~17 OQ-B*-* items routed (Wave E ack-time / Phase B / Phase C+ / closed / Wave D fix).
> Dissolve-test verdict: STANDALONE PRESERVED / DISSOLVE (rationale: <evidence count and threshold>).
> Phase D-8 retroactive supplement: applied / skipped (rationale).
> M-D-1 through M-D-6 gates: PASS / PASS / PASS / PASS / PASS / PASS.
> Foundation Architecture LOCKED readiness: YES / NO (with blocking gaps listed).
> Awaiting Ruslan ack before Wave E LOCKED tag dispatch.
> **THIS IS THE FINAL GATE BEFORE FOUNDATION ARCHITECTURE LOCKED.**»

### §10.2 Autocheck — when to halt early

- **Walltime exceeds 12h**: STOP, report status to Ruslan, ask how to proceed. (Wave D = verification of 10 LOCKED parts; projected 1-2.5h at compound velocity; 12h ceiling extremely generous.)
- **Brigadier finds itself drafting NEW architecture content**: scope-creep failure per §5.6; HALT, re-dispatch with verification-only mandate; if persistent, escalate to Ruslan.
- **Brigadier finds itself running Wisdom Loop**: scope-creep failure; HALT.
- **Coverage matrix has >5 ❌ cells**: integration is not coherent; HALT, escalate, propose Phase D-8 retroactive supplement OR escalate to Ruslan.
- **Contracts matrix surfaces >3 gaps**: significant inter-Part incoherence; HALT, escalate, propose Phase D-8 supplement OR Wave E ack-time decision routing.
- **Extended scenarios produce <8 PASS**: verify failure analysis is honest; HALT if FAIL has no clear gap routing.
- **FUNDAMENTAL UC mapping surfaces >5 unmapped UC items**: significant Foundation gap; escalate to Ruslan; verify FUNDAMENTAL Vision was correctly read.
- **Dissolve-test verdict = DISSOLVE**: do NOT auto-execute Part 5 dissolution; surface in dedicated AWAITING-APPROVAL packet for Ruslan ack.
- **OQ catalogue surfaces an OQ that requires ack-time decision but Bundle 4 ack already made the decision**: route to close-as-resolved-already with rationale.
- **Brigadier subagents stall on stream watchdog**: switch to direct-write mode acceptable; flag in AWAITING-APPROVAL packet.

### §10.3 Budget

~5-12 reviewer-mode dispatches across phases (≤2 reviewers per Phase D-1, D-2, D-4 = ≤6; brigadier-direct for D-3, D-5, D-6, D-7, D-8). Budget guard: if dispatch count exceeds 20, audit for redundant dispatches; if exceeds 30, halt and ask Ruslan.

### §10.4 Mantra (recite before each phase transition)

> **INTEGRATION > CREATION.**
> **VERIFICATION > INVENTION.**
> **HONEST-GAP-DECLARATION > PAPER-OVER.**
> **FOUNDATION-LOCKED-IS-THE-FINISH-LINE.**
> **RUSLAN-ACK > BRIGADIER-CONFIDENCE.**
> **THIS IS THE LAST GATE.**
>
> *Wave D verifies that 10 LOCKED parts integrate. No new architecture. No new schemas. No new configs. No Wisdom Loop. Output = integration report 5K-8K words + 7 phase auxiliary files + AWAITING-APPROVAL packet + optional retroactive supplement IF and ONLY IF integration gap surfaces. After Wave D ack → Wave E LOCKED tag → Foundation Architecture COMPLETED. Treat with 1 trillion percent responsibility. WAVE D = LAST GATE.*

---

## §11 Pre-flight Checklist (brigadier runs before first Phase D-0 dispatch)

- [ ] Read this prompt three times
- [ ] Read all of §3.1 Constitutional baseline (FUNDAMENTAL Vision §1+§6 binding for D-4; ALL 5 ACK records)
- [ ] Read all 10 LOCKED Foundation architectures per §3.2 (parallel reviewer-mode dispatches OK; brigadier consolidates)
- [ ] Read all 4 Bundle AWAITING-APPROVAL packets per §3.3 (D-5 source-of-truth for OQ catalogue)
- [ ] Skim §3.4 Wave A artefacts (esp. dependency-graph.md §3 contradictions catalog for D-2 contracts gap reference)
- [ ] Skim §3.5 Wave B 14 consultant cards (verification reference; cite if cross-cut justification needs it)
- [ ] Skim §3.6 Wave B Supplement library-direct sources
- [ ] Skim §3.7 schemas + configs (verification reference)
- [ ] Skim §3.8 operational baselines (CC-4 fork-separation cross-cut reference)
- [ ] Verify branch `claude/jolly-margulis-915d34` is current and clean (head `236fefc` Bundle 4 ack)
- [ ] Verify all 10 Foundation parts F5 LOCKED via grep on `swarm/wiki/foundations/part-*/architecture.md` frontmatter
- [ ] Verify `unset ANTHROPIC_API_KEY` (operator should have done this)
- [ ] Acknowledge §0 Mission Statement and §10.4 Mantra internally before first dispatch
- [ ] Confirm phase sequence: D-0 → D-1 → D-2 → D-3 → D-4 → D-5 → D-6 → D-7 (synthesis + AWAITING-APPROVAL) → optional D-8
- [ ] Confirm output paths in §7 are mkdir-ready
- [ ] Confirm verification-only mandate internalised — NO new architecture / schemas / configs / Wisdom Loop

When all bullets ticked: dispatch Phase D-0 pre-flight verification. Then proceed sequentially through D-1 through D-7. Phase D-8 only if triggered.

---

## §12 Reference — what NOT to do

1. **DO NOT re-litigate Bundles 1+2+3+4 LOCKED schemas.** Wave D CONSUMES these as F5/F8 constitutional contracts.
2. **DO NOT re-create 10K-20K bundle architecture documents.** Wave D produces 5K-8K integration report.
3. **DO NOT run Wisdom Application Loop.** Bundles 1-4 already applied 14 cards + 5 library-direct sources.
4. **DO NOT dispatch 5×4 expert matrix.** Reviewer-mode only; HD-02 N=2 cap.
5. **DO NOT auto-launch Wave E.** Always STOP after Wave D AWAITING-APPROVAL.
6. **DO NOT invent new typed A.14 edges in D-2.** Verify declared edges; flag missing as gap.
7. **DO NOT cite consultant cards for verification claims.** Cite Bundle architectures + ACK records.
8. **DO NOT paper over integration gaps.** Honest-gap-declaration mandatory per §5.5.
9. **DO NOT auto-execute Part 5 dissolution if D-6 verdict = DISSOLVE.** Escalate to Ruslan via dedicated AWAITING-APPROVAL packet.
10. **DO NOT touch the Untouchable trees** (§9.8) or Security paths (§9.10).
11. **DO NOT push to `main`.** Branch `claude/jolly-margulis-915d34` only.
12. **DO NOT use `--amend` / `--no-verify` / force-push.**
13. **DO NOT reference any provider API-key env var** in code paths.
14. **DO NOT confuse Foundation with RUSLAN-LAYER in cross-cut CC-4.** Coverage matrix verifies §X declarations exist; does NOT propose new RUSLAN-LAYER bindings.
15. **DO NOT include executor names or model names in Wave D outputs.** IP-1 strict.
16. **DO NOT skip Phase D-0 pre-flight.** Branch state verification + 10 parts F5 LOCKED verification + 5 ACK records committed verification = mandatory.
17. **DO NOT skip Phase D-4 FUNDAMENTAL coherence.** UC mapping + anti-scope enforcement is the final test that Foundation parts satisfy the constitutional mission.
18. **DO NOT route OQs to Wave E ack-time silently.** Each Wave E ack-time OQ surfaces explicitly in AWAITING-APPROVAL packet §4.
19. **DO NOT exceed 8K words in INTEGRATION-REPORT.md.** That's the bundle-architecture scope-creep failure mode.
20. **DO NOT come in under 5K words in INTEGRATION-REPORT.md.** Phase coverage is incomplete.

---

## §13 Final note from Ruslan (paraphrased intent, brigadier internalize)

Wave D is the integration pass — the moment of truth. Bundles 1-4 designed 10 Foundation parts independently (with cross-bundle finalisations: C1 Joint Design, C2 canonical health-signal schema, UND-1 task-return-packet binding, UND-2 methodology promotion pipeline, UND-3 project-retrospective-packet finalisation, UND-5 CRM edges binding, OQ-MERGED-3 fork-separation FINAL CLOSURE, OQ-B1-5 D27 reconciliation strategies, C4 nomenclature fix). Wave D verifies that the 10 parts INTEGRATE — that the cross-cuts are coherent, that the typed edges have producers AND consumers, that the system-wide scenarios trace cleanly, that the FUNDAMENTAL Vision is faithfully implemented, that the OQ debt from Bundles 1-4 is routed honestly, that the dissolve-test for Part 5 has a defensible verdict.

**Honest-gap-declaration is the central discipline.** If integration is coherent, declare it coherent with evidence. If integration has gaps, declare them with proposed routing. Do not paper over. Do not invent. Do not scope-creep into new architecture. The 10 parts are F5 LOCKED — Wave D's job is to verify, not to redesign.

**Foundation Architecture LOCKED is the finish line.** After Wave E LOCKED tag, the Foundation envelope is sealed. Phase B onboarding begins (partner forks; live integration adapter implementation; calibrated SLI/SLO thresholds; F.9 Bridge spec). Phase C product, Phase D org follow.

If Wave D is half-baked, Wave E LOCKED tag is premature — Foundation has invisible integration gaps that Phase B partners will discover the hard way. If Wave D over-engineers — drifts into Wisdom Loop, drafts new architectures, re-litigates LOCKED schemas — Phase B onboarding drags as Foundation churns.

The right level: **verification depth sufficient to trust Foundation; verification scope tight enough to ship.** 50-cell coverage matrix tells truth about cross-cut coherence in one page. Inter-Part contracts matrix tells truth about edge integrity in one page. 8-10 system-wide scenarios tell truth about end-to-end traces in 5 pages. FUNDAMENTAL UC + anti-scope mapping tells truth about constitutional fidelity in 5 pages. OQ catalogue tells truth about debt in 3 pages. Dissolve-test verdict tells truth about Part 5 standalone in 1 page. Integration report synthesises in 8K words. AWAITING-APPROVAL packet surfaces ack-time decisions for Wave E.

**This is the document a Phase B partner can read in 30 minutes to trust the Foundation. Make it the document where the integration is verified, the gaps are honest, and the lock is earned.**

**OQ-MERGED-3 FINAL CLOSURE held — Bundle 4 ack confirmed.**
**OQ-5 cadence event-driven held — Part 7 §E 4 laws verbatim, Bundle 4 ack confirmed.**
**IP-2 single-owner bounded held — Part 9 §X + §I.4 multi-owner stub fields, Bundle 4 ack confirmed.**
**Privacy STRUCTURAL held — Part 10 §I.5 + §H.7 + §F 4 invariants, Bundle 4 ack confirmed.**
**OQ-B1-5 D27 promotion held — Part 1 §I.1 v1.1.0 + 5 reconciliation strategies, Bundle 4 supplement-2 ack confirmed.**
**UND-3 finalised — Part 7 §B emit ↔ Part 5 §A.5 input, Bundle 4 M5 PASS confirmed.**
**C4 nomenclature fix held — Part 9 §D `methodologically-uses Part 6` not `PhaseOf Part 6`, Bundle 4 ack confirmed.**
**OQ-MERGED-2 dissolve-test Cycle 3 — Wave D = decision window close.**

**THIS IS THE LAST GATE BEFORE FOUNDATION ARCHITECTURE LOCKED.** After Ruslan ack of Wave D AWAITING-APPROVAL packet → Wave E LOCKED tag dispatch → Foundation Architecture COMPLETED.

---
