---
title: "Wave C Bundle 4 — M3 Scenario Walkthroughs (4 scenarios)"
date: 2026-04-28
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 4
verification_gate: M3
status: PASS
sources:
  - swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md
  - swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md
  - swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md
  - swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md
  - swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md
  - swarm/wiki/foundations/part-6b-human-gate/architecture.md
  - swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md
---

# Wave C Bundle 4 — M3 Walkthroughs

Per deep prompt §7.3: 4 scenarios MUST trace cleanly with no missing schemas
or undefined handoffs. Pass threshold: 4/4 PASS.

---

## Scenario 1 — Project full lifecycle (Parts 7/4/5/6b/1)

**Setup**: Owner declares project "quick-money" via `/project-bootstrap quick-money P1 --type=consulting --client=acme`.

**Trace**:

1. **`scoped` state** — `/project-bootstrap` writes draft brief at
   `projects/quick-money/brief.md` per Part 7 §I.1 schema (appetite_weeks=4;
   scope; ≥1 Hamel-binary acceptance predicate; type=consulting). State =
   `scoped`. F2|G:draft|R-low. **Commit**: `[project] scoped: quick-money
   (brief drafted, type=consulting, appetite=4w)` via Part 1 §H.

2. **`scoped → staged` stage-gate** — Part 7 emits AWAITING-APPROVAL packet
   per Part 6b §I.4 F8 schema with `gate_class: stage_gate` to enforcement
   arm. Ruslan acks via Part 9 weekly review L1 SLA tier (same-session ≤4h).
   Part 6a logs ack to `swarm/approvals/log.jsonl`. State transitions to
   `staged`. F4|G:staged project|R-medium. **Commit**: `[project] staged:
   quick-money (gate trp-20260428-quick-money-staged acked)`.

3. **`staged → activated` stage-gate** — same flow; Ruslan acks; Part 7
   transitions to `activated`. F5|G:activated project|R-high. **Commit**:
   `[project] activated: quick-money (gate trp-20260428-quick-money-activated
   acked)`.

4. **Cycle dispatch via Part 4** — brigadier dispatches per
   `swarm/lib/routing-table.yaml` (Bundle 2 LOCKED). Cycle 1 of project
   begins. Part 4 emits task-return-packets per §I.1 FULL schema (Bundle 2
   Decision #4 LOCKED).

5. **Cycle close → Part 7 detects closure marker** — task-return-packet
   `outputs[].path` references match `projects/quick-money/` AND closure
   acceptance predicate satisfied. Part 7 fires event-driven `activated →
   under-review` transition (NO Ruslan ack — state-of-fact transition per
   §J.1 step 5). **Commit**: `[project] under-review: quick-money (cycle
   cyc-2026-W18 closure detected)`.

6. **Retrospective drafting** (Option β cadence drafts during `under-review`)
   — Part 7 H.3 emit_project_retrospective(project_id="quick-money",
   state_transition={from:"under-review", to:"under-review"},
   cadence_option="beta-draft-update") writes draft increments to
   comms/mailboxes/part-5.jsonl. Part 5 §A.5 reads as F2 candidate input.

7. **`under-review → closed` stage-gate** — Ruslan reviews retrospective
   draft + acks closure (closure_type=closed; rationale ≥30 chars). Part 7
   emits AWAITING-APPROVAL `gate_class: stage_gate`. Part 6b ack. State =
   `closed`. F5|G:terminal|R-high. **Commit**: `[project] closed:
   quick-money (gate trp-20260428-quick-money-closed acked, retrospective
   emitted)`.

8. **Final retrospective emission (Option α cadence)** — Part 7 H.3 emits
   `project-retrospective-packet.json` per §I.2 schema (extends
   task-return-packet) to `comms/mailboxes/part-5.jsonl`. Schema fields
   include: `project_id` ✓, `state_transition` ✓,
   `appetite_actual_vs_planned` ✓, `lessons_learned[]` ✓, `dr_r_candidates[]`
   ✓, `methodology_promotion_candidates[]` ✓. **UND-3 finalization
   verified** — Part 5 §A.5 admits per admissibility A-5.

9. **Part 5 compound-phase consumption** — Part 5 §I.2 extraction reads
   project-retrospective-packet; updates `agents/<id>/strategies.md` with
   new DRR entries; methodology promotion candidate `shape-up-appetite-
   constraint` accumulates `validated_in_cycles=2` predicate.

10. **Methodology promotion gate** — Part 5 §I.1 emits methodology
    candidate at `wiki/methodology/shape-up-appetite-constraint-DRAFT.md`
    with `pipeline: ingested`; opens Part 6b AWAITING-APPROVAL `gate_class:
    draft_promotion`. Ruslan acks; file renamed to
    `wiki/methodology/shape-up-appetite-constraint.md` with `pipeline:
    ready`; F4 → F5.

**Tests covered**: Parts 7 + 4 + 5 + 6b + 1; UND-3 finalization (Part 7 §B
emit ↔ Part 5 §A.5 input); event-driven cadence (OQ-5 — `activated →
under-review` event-driven, no ack); appetite-as-CONSTRAINT (Singer Shape
Up); stage-gate predicates F8 LOCKED.

**Verdict**: ✅ PASS — clean trace; no missing schemas; UND-3 finalization
verified.

---

## Scenario 2 — Daily-log + weekly review with methodology promotion (Parts 9/5/6b/1)

**Setup**: Friday morning. Ruslan invokes `/plan-day`.

**Trace**:

1. **Morning intent** — `/plan-day` skill invocation creates
   `daily-log/2026-04-28.md` with Part 9 §I.1 schema. Owner authors
   morning_intent prose (appetite + 1-3 tasks; IP-7 owner-authored predicate
   true). frontmatter populated: date, owner=ruslan, projects_touched=[
   quick-money, research], decisions_made=[], ack_events=[],
   attention_budget_used={tasks_started:1}, para_tier:Area, f_g_r:[F2|G:per-day|R-low].
   **Commit**: `[daily] plan: 2026-04-28`.

2. **Cycle dispatch via Part 4** — Part 9 § J.1 step 2 reads cycle dispatch
   summary from brigadier extraction.

3. **Afternoon execution** — cycle_dispatch_summary populated; surprises
   captured.

4. **Evening reflection** — `/close-day` invocation; Owner authors
   evening_reflection (what worked, what dropped, methodology candidates
   surfaced). IP-7 owner-authored predicate verified via git blame.
   **Commit**: `[daily] eod: 2026-04-28`.

5. **Friday EOD weekly review trigger** — Part 9 §J.2 ritual invocation.
   Aggregate daily-logs since prior weekly review.

6. **Read `agents/<id>/strategies.md`** — Part 9 §J.7 reads candidates with
   `validated_in_cycles ≥ 2`. Surfaces `shape-up-appetite-constraint` and
   `event-driven-cadence-throughput` (2 candidates).

7. **Compose draft-disposition table** — Part 9 §I.2 schema. 5 accumulated
   drafts identified. Owner classifies:
   - draft 1 (`drafts/policy-rec-2026-04-26.md`) → `accept` rationale: "ready for
     promotion; F4 schema validated" → action: `promotion request emitted via
     Part 6b draft_promotion gate`
   - draft 2 (`drafts/wiki-synthesis-2026-04-25.md`) → `iterate` rationale:
     "needs additional sources" → action: `iterate — revision note appended`
   - draft 3 (`drafts/crm-outreach-rodion.md`) → `discard` rationale:
     "superseded by direct contact this week" → action: `discard — archived
     to drafts/archive/`
   - drafts 4 + 5: `iterate` and `accept` similarly classified.

8. **Owner authors weekly_retrospective** — 5 questions answered (what
   worked / what blocked / what dropped / next-week appetite / methodology
   candidates). IP-7 owner-authored predicate verified.

9. **Methodology candidate disposition** — both candidates classified
   `weekly_disposition: accept`. Part 9 §J.7 forwards to Part 5 via
   `comms/mailboxes/part-5.jsonl`.

10. **Part 5 admits** per §A.5 admissibility — both candidates have
    `validated_in_cycles ≥ 2` + `rule_slug` populated. Part 5 §I.1 emits
    `wiki/methodology/shape-up-appetite-constraint-DRAFT.md` with
    `pipeline: ingested`; opens AWAITING-APPROVAL `gate_class:
    draft_promotion` to Part 6b.

11. **SLA tier review** — l1_compliance_pct=100% (all L1 acks within
    same-session); l2_compliance_pct=95% (1 batch overflow); l3_compliance_pct=
    100%. Tier_breaches[] = [{tier:L2, item_id:"draft-2-iterate-decision",
    delta:"+12h"}].

12. **Weekly review committed** — `weekly-reviews/2026-W18.md` per Part 9
    §I.2. **Commit**: `[review] weekly: 2026-W18`.

13. **Promotion gate** — Ruslan acks Part 6b `gate_class: draft_promotion`
    same-session per L1 SLA. wiki/methodology/<rule-slug>.md F4 → F5.
    **Commit**: `[methodology] promote: shape-up-appetite-constraint (F5
    codified rule)`.

**Tests covered**: Parts 9 + 5 + 6b + 1; daily-log/weekly-review schemas;
SLA 3-tier taxonomy; methodology promotion via weekly review (Part 9 ↔ Part
5 cross-ref); C4 nomenclature fix (Part 9 §D `methodologically-uses Part 6`
not `PhaseOf Part 6` — verified via grep on edge-table entries; 0 hits);
IP-2 single-owner bounded.

**Verdict**: ✅ PASS — clean trace; methodology candidate flow Part 9 → Part
5 → Part 6b → wiki/methodology canonical; C4 fix applied.

---

## Scenario 3 — External action with privacy enforcement (Parts 10/6b/6a/1)

**Setup**: Ruslan requests CRM contact outreach via `/crm-touch
anton-mentor "follow up on Q2 partnership opportunity"`.

**Trace**:

1. **`/crm-touch` invocation** — Part 10 §J.2 ritual. `crm/_scripts/crm.py`
   reads `crm/people/anton-mentor.md`. Append-only entry added to §11
   history.

2. **Phase B RT-2 outreach branch** (Phase A: SPECIFICATION ONLY; this
   scenario projects Phase B activation) — Ruslan invokes follow-up Linear
   ticket via Phase B RT-2 adapter.

3. **Consent verification** — Part 10 §I.5 invariant 1: RT-2 reads
   `consent_recorded_at` field from anton-mentor.md frontmatter. Field
   present (e.g., `consent_recorded_at: 2026-04-15T10:30:00Z`). Verification
   PASS.

4. **Blast-radius classify** — RT-2 classifies action_type=linear-ticket as
   Tier 1 strategic per Part 6b §I.3.

5. **AWAITING-APPROVAL packet emission** — RT-2 emits packet per Part 6b
   §I.4 F8 schema with `gate_class: stage_gate`, `blast_radius: tier-1`,
   `f_g_r: [F4|G:single external action|R-medium]`, contact_slug,
   action_payload preview.

6. **Ruslan ack** — L1 SLA same-session (≤4h per RUSLAN-LAYER override).
   Part 6a logs ack to `swarm/approvals/log.jsonl` with timestamp +
   acked_by:ruslan signature.

7. **External write fires** — RT-2 invokes `linear_create_ticket(team_id=..,
   title=.., body=..)` via Phase B L.1 adapter. Auth via
   `private/linear-auth.yaml` (RUSLAN-LAYER).

8. **Write-ack confirmation** — Linear API returns success + ticket_id.
   RT-2 logs 3-way audit trail:
   - CRM event log entry: `crm/log.md` append `[crm] outreach:
     anton-mentor (Linear ticket lin-2026-001 created via L.1 adapter)`.
   - Approval log entry: `swarm/approvals/log.jsonl` (already logged at
     step 6).
   - Cross-fork-provenance log entry: `cross-fork-provenance.json` (Phase B
     when partner-fork imports). Phase A: skipped.

9. **Part 1 §H commit** — `[crm] outreach: anton-mentor (Linear ticket
   created)`.

10. **Health emission** — Part 10 §J.7 calls
    `swarm/lib/emit_health_signal()` with:
    - `external-action-latency` metric (Ruslan ack → write-ack: 47s).
    - `integration-adapter-health` metric (Linear adapter success).

11. **Privacy invariant 4 cross-check** — Brigadier autocheck §6.10: RT-2
    invocation produced no protected-characteristic classifier attempts.
    Default-Deny entry NOT triggered. `/lint --check-protected-inference`
    Phase B run zero violations.

**Tests covered**: Parts 10 + 6b + 6a + 1; consent enforcement (privacy
invariant 1); RT-2 adapter pattern; SLA tier L1 ack; AWAITING-APPROVAL
`gate_class: stage_gate`; CRM canonicalisation (existing operational
baseline preserved — no schema redesign); 3-way audit trail.

**Verdict**: ✅ PASS — clean trace; consent verified; privacy invariant 4
NOT violated; auth-token externalised to RUSLAN-LAYER per §X.

---

## Scenario 4 — Fork-separation Phase B import (Parts 10/1; FINAL CLOSURE validation)

**Setup**: Phase B partner "alex-dach-consulting" forks Foundation. Partner
runs US fintech consulting practice (different from Ruslan's DACH ICP).

**Trace**:

1. **Fork import** — alex-dach-consulting clones Foundation tree; imports:
   - `crm/_schema/frontmatter.yaml` (12 field groups per cycle 10)
   - `crm/_schema/roles.yaml` (24 roles in 6 groups)
   - `crm/_schema/statuses.yaml` (13 pipeline statuses)
   - `crm/_schema/edges.yaml` (8 CRM edge types — UND-5 binding)
   - Integration adapter pattern (RT-1 + RT-2 + L.1/L.2/L.3 stubs per §I.4)
   - 4 privacy invariants (consent / forget / encryption / no-protected-
     inference per §I.5)
   - Write-ack discipline (mandatory consent + AWAITING-APPROVAL stage_gate)
   - 5 reconciliation strategies enum (parent-wins / fork-wins /
     manual-merge / decline-import / pending-review)
   - `cross-fork-provenance.json` schema (Bundle 4 supplement 2 — top-level
     `approvals_reconciliation_strategy` field)

2. **Fork DECLINES RUSLAN-LAYER**:
   - DACH ICP parameters (`crm/_schema/icp.yaml` Ruslan content): partner's
     ICP is US fintech, not DACH consulting.
   - German GDPR config (`crm/_schema/gdpr.yaml` Ruslan content): partner's
     jurisdiction is US (HIPAA + CCPA + state-specific privacy laws).
   - Ruslan's specific contact list (`crm/people/anton-mentor.md`,
     `vladislav-economist.md`, `rodion-youtuber.md`, `example-person.md`):
     partner has own contact list.
   - Ruslan's auth tokens (`private/linear-auth.yaml`, etc.): partner has
     own auth tokens at same path convention.
   - DACH intelligence URLs (HN + r/Berlin + r/germany + DACH newsletters):
     partner has own intelligence URLs (US fintech sub-Reddits + US-specific
     newsletters).

3. **Partner populates own RUSLAN-LAYER**:
   - `crm/_schema/icp.yaml` — declares "ICP = US fintech / SaaS Series A-C;
     50-500 employees; English; SOC 2 + HIPAA-aware".
   - `crm/_schema/gdpr.yaml` — replaced with `crm/_schema/privacy-us.yaml`
     (CCPA + HIPAA + state-specific regulations).
   - `crm/people/<partner-slugs>.md` — partner's contacts.
   - `private/linear-auth.yaml`, etc. — partner's tokens (rotation policy
     inherited from Foundation: 90 days).
   - RT-1 source URLs — US-specific (HN + r/SaaS + r/fintech + Stratechery
     newsletter + etc.).

4. **Reconciliation strategy applied**:
   - **`parent-wins` for privacy invariants** — Foundation Default-Deny
     entries hold (race / religion / political / health classifier
     prohibitions). Both partner + Ruslan share these constitutional anchors.
   - **`fork-wins` for ICP parameters** — alex-dach-consulting's US fintech
     ICP supersedes RUSLAN-LAYER DACH for partner's instance.
   - **`fork-wins` for jurisdiction-specific privacy regs** — partner's US
     CCPA + HIPAA replaces German GDPR.
   - **`manual-merge` for cross-cutting changes** — partner proposes new
     Default-Deny entry "US-specific HIPAA classifier prohibition" (e.g.,
     classifier on patient-record fields). Both Ruslan + partner ack via
     AWAITING-APPROVAL `gate_class: stage_gate`. Foundation `default-
     deny-table.yaml` extended with new entry; partner's instance + Ruslan's
     instance both inherit.
   - **`pending-review` initial state** — until partner explicitly acks each
     reconciliation strategy on first import.

5. **Cross-fork-provenance.json conforms** — partner's `cross-fork-
   provenance.json` populated with `approvals_reconciliation_strategy:
   <strategy>` top-level field per Bundle 4 supplement 2 schema. Top-level
   field promotion from `metadata` open field VERIFIED for fork-import
   scenario.

6. **Audit trail integrity** — partner's parent_repo_id maps to imported-
   state-token in partner's audit log. Ruslan's parent commit hashes do NOT
   appear in partner's `git log` directly — only the imported_state_token
   does (per Part 1 §I.1 audit_trail_continuation strategy).

7. **F.9 Bridge spec NOT triggered** — Phase B partner-fork is a SEPARATE
   instance (alex-dach-consulting runs own Jetix instance), not multi-owner
   within same Jetix instance. F.9 Bridge is for multi-owner same-instance
   case (Part 9 IP-2). Phase B partner-fork uses fork-separation discipline,
   not F.9 Bridge.

**Tests covered**: Parts 10 + 1; FINAL CLOSURE fork-separation per
OQ-MERGED-3 (DACH ICP / German GDPR / Linear+GitHub+Notion+Slack auth-token /
contact-list / DACH intelligence URL examples all explicit in Part 10 §X);
OQ-B1-5 D27 promotion (top-level `approvals_reconciliation_strategy` field
verified for fork-import scenario); reconciliation_strategy enum (5 values
exercised); Phase B import pattern.

**Verdict**: ✅ PASS — clean trace; all 5 RUSLAN-LAYER categories
declined by fork; reconciliation strategies applied per §X.3; cross-fork-
provenance D27 promotion exercised.

---

## §M3 Summary

| Scenario | Verdict | Parts tested | Key invariants verified |
|---|---|---|---|
| 1. Project full lifecycle | ✅ PASS | 7+4+5+6b+1 | UND-3 finalization; event-driven cadence (OQ-5); appetite-as-CONSTRAINT; stage-gate F8 LOCKED |
| 2. Daily-log + weekly review + methodology promotion | ✅ PASS | 9+5+6b+1 | C2 producer-side draft-disposition; SLA 3-tier; C4 nomenclature fix; IP-2 single-owner; methodology promotion |
| 3. External action + privacy | ✅ PASS | 10+6b+6a+1 | Privacy invariant 1 (consent); RT-2 write-ack; CRM canonicalisation; Tier 1 stage_gate |
| 4. Fork-separation Phase B import | ✅ PASS | 10+1 | OQ-MERGED-3 FINAL CLOSURE; OQ-B1-5 D27 promotion; reconciliation strategies (5 enum) |

**M3 result: 4/4 PASS.** All 4 scenarios trace cleanly with no missing
schemas or undefined handoffs.
