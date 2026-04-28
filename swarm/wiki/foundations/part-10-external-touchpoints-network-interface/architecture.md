---
title: "Foundation Part 10 — External Touchpoints & Network Interface (Architecture)"
part_number: 10
part_slug: external-touchpoints-network-interface
date: 2026-04-28
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 4
phase: Wave-C-Bundle-4-architecture
status: ruslan-acked-canonical
ruslan_ack_record: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md
ruslan_ack_date: 2026-04-28
predecessor_interface_card: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-10-external-touchpoints-network-interface.md
constitutional_baseline_bundle_1: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
constitutional_baseline_bundle_1_supplement: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md
constitutional_baseline_bundle_2: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md
constitutional_baseline_bundle_3: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md
canonicalises_existing: "CRM cycle 10 (2026-04-26) — 24 source files / 35 unit tests / 10 /crm-* skills / 4 YAML schemas in crm/_schema/. Bundle 4 Part 10 CANONICALISES existing implementation; does NOT redesign."
finalises_oq_merged_3: "FINAL CLOSURE for Foundation-level fork-separation per OQ-MERGED-3 Wave A scope. Bundle 4 = last opportunity. §X explicit DACH ICP / German GDPR / Linear+GitHub+Notion+Slack auth-token / contact-list / DACH intelligence URL examples MANDATORY."
finalises_oq_b1_5: "OQ-B1-5 D27 reconciliation_strategy field promotion — END-OF-CYCLE supplement record at decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-28.md."
F: F5
F_promotion_ack: "Ruslan ack 2026-04-28 per decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md decision #1 — F4 → F5. Decisions #4 (OQ-MERGED-3 fork-separation FINAL CLOSURE) + #7 (Privacy STRUCTURAL — 4 invariants with schema fields + lint signal skill specs + Default-Deny entries) + #8 (CRM canonicalisation — existing 24 src / 35 tests / 10 skills / 4 schemas referenced NOT redesigned) all F5 → F8 LOCKED. Decision #9 OQ-B1-5 D27 retroactive supplement 2 accepted (cross-fork-provenance.json schema v1.1.0 approvals_reconciliation_strategy top-level + 5 strategies)."
ClaimScope: "Holds for any single-owner knowledge-work system that maintains contact-network records + integrates external services + must enforce privacy invariants STRUCTURALLY (NOT behaviorally). Bundle 4 introduces canonical CRM data model schema + integration adapter pattern (RT-1 read-only intelligence + RT-2 write-ack action coordinators + L.1/L.2/L.3 service stubs) + 4 privacy invariants (consent / forget / encryption / no-protected-inference) with structural enforcement (schema fields + lint signals + Default-Deny entries) + C3 Phase A boundary (inbound external = Phase B work) + OQ-B1-5 D27 reconciliation strategy promotion. Phase A scope: single-owner Jetix Phase-A €50K horizon; Fork-portable for Phase B partner imports."
R:
  refuted_if: "Part 10 architecture redesigns CRM data model OR omits explicit DACH/GDPR/auth-token/contact-list/intelligence-URL examples in §X (OQ-MERGED-3 fork-separation FINAL CLOSURE under-declared) OR proposes BEHAVIORAL privacy framing instead of STRUCTURAL (schema fields + lint + Default-Deny) OR allows Phase A inbound external auto-action without Ruslan ack (C3 violation) OR omits OQ-B1-5 D27 reconciliation_strategy top-level promotion"
  accepted_if: "Bundle 4 Part 10 architecture acked; CRM canonicalised (existing baseline preserved); integration adapter pattern declared (RT-1 + RT-2 + L.1/L.2/L.3 stubs); 4 privacy invariants STRUCTURALLY enforced; §X explicit fork-separation examples present (DACH ICP / GDPR / auth-token / contact-list / intelligence-URL); C3 declared Phase A inbound = Phase B; OQ-B1-5 D27 supplement record committed end-of-cycle"
sources:
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-10-external-touchpoints-network-interface.md"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md (§2 Part 10)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md (§2 Part 10; §4 OQ-MERGED-3; §6 item 5 §6.4 privacy)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md (§3.3 C3; §4.5 UND-5)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md (privacy + write-ack + hardcoded never-list)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md (IP-2 with F.9 Bridge; A.14 typed edges)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/mereology-typed-edges.md (CRM graph edges UND-5)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md (PARA: contacts in Resource | Project tier)"
  - "swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/multi-agent-architecture.md (A2A; integration adapter pattern)"
  - "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (§6.4 privacy hard rules; §6.1 default-deny constitutional)"
  - "design/JETIX-FPF.md (IP-2 bounded context with F.9 Bridge; A.14 typed edges; A.6.B L/A/D/E)"
  - "swarm/wiki/foundations/part-1-system-state-persistence/architecture.md (§I.1 cross-fork-provenance.json — OQ-B1-5 D27 promotion target)"
  - "swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md (C3 cross-ref; /ingest entry)"
  - "swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md (wiki/graph/edges.jsonl — UND-5 binding)"
  - "swarm/wiki/foundations/part-6a-provenance-officer/architecture.md (§I.1 F-G-R F8)"
  - "swarm/wiki/foundations/part-6b-human-gate/architecture.md (§I.4 awaiting-approval-packet F8; §I.3 blast-radius; §I.2 default-deny)"
  - "swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md (§I.1 health-signal schema)"
  - "swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md (§I.3 SLA taxonomy; weekly review consumes stuck-contacts)"
  - "decisions/AUDIT-CURRENT-STATE-2026-04-27.md (§7 CRM cycle 10 deliverables)"
  - "swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md (CRM build cycle authoritative)"
  - "crm/README.md (CRM authoritative spec)"
  - "crm/PLAN.md (frozen reference; implemented cycle-10)"
  - "raw/books-md/anthropic/bai-2022-cai.md (Constitutional AI privacy + write-ack)"
  - "raw/books-md/anthropic/askell-2021-hhh.md (Helpful-Honest-Harmless; corrigibility; hardcoded never-list)"
  - "raw/books-md/event-sourcing/young-cqrs-2010.md (Reversal Transactions for forget-request)"
---

# Foundation Part 10 — External Touchpoints & Network Interface (Architecture)

## §0 Executive Summary

**Part 10 closes the outside-world loop.** Every contact the system maintains,
every external action it takes (Linear ticket, GitHub PR, Slack DM, partner
email), every intelligence signal it watches (HN, niche sub-Reddits, newsletter
sources) flows through Part 10's canonical CRM data model + integration
adapter pattern (RT-1 read-only intelligence trackers + RT-2 write-ack action
coordinators) + 4 STRUCTURAL privacy invariants. **CRM is OPERATIONAL** —
cycle 10 (2026-04-26) already shipped 24 source files / 35 unit tests / 10
`/crm-*` skills / 4 YAML schemas (`crm/_schema/`). Bundle 4 Part 10
**canonicalises** this — does NOT redesign.

**Without Part 10, the system has a CRM with no Foundation-level boundary
declarations**, no privacy structural enforcement, no fork-separation
discipline for the ICP-specific RUSLAN-LAYER, and no integration adapter
pattern for Phase B scale. Privacy degrades from invariant to behavioral
norm. Auth tokens leak into Foundation. DACH-specific ICP shades into
generic CRM mechanics. External actions auto-fire without ack. Phase B
partner forks inherit a tangled CRM that mixes Foundation-generic mechanics
with Ruslan's specific contact list.

Bundle 4 introduces FOUR structural firsts for Part 10:

- **CRM canonicalisation (NOT redesign).** The existing 24 source files / 35
  unit tests / 10 `/crm-*` skills / 4 YAML schemas operate as Phase A
  baseline. Part 10 §A + §B + §H + §I REFERENCES the existing tree;
  improvements surface as OQ-B4-X for Wave D consideration; do NOT
  re-implement in Bundle 4. Brigadier autocheck rejects Part 10 producing
  alternative CRM data model.

- **4 STRUCTURAL privacy invariants per FUNDAMENTAL §6.4.** Privacy is
  schema fields + lint signals + Default-Deny entries — NOT behavioral
  framing prose. The 4 invariants are: (1) Consent enforcement via
  `consent_recorded_at: <ISO timestamp>` schema field; (2) Forget-request
  via `/crm forget` skill spec + Reversal Transactions discipline (Young
  2010); (3) Encryption at rest as Part 1 substrate-level PRECONDITION; (4)
  NO inference of protected characteristics via `/lint --check-protected-
  inference` skill spec + Default-Deny entries per Part 6b §I.3 (race /
  religion / political affiliation / health status = Tier 0 hard halt).
  Behavioral framing prose target <10% of privacy section.

- **Integration adapter pattern (RT-1 + RT-2 + L.1/L.2/L.3 stubs).** RT-1
  read-only intelligence trackers (HN, sub-Reddits, niche newsletters) emit
  signals to Part 2 `/ingest` triage — NEVER write externally; Tier 3
  blast-radius. RT-2 write-ack action coordinators (Linear, GitHub, Slack,
  partner email) verify CRM consent → blast-radius classify → AWAITING-
  APPROVAL `gate_class: stage_gate` → Ruslan ack → external write → write-
  ack confirmation logged to CRM event log + approval log + cross-fork-
  provenance log. L.1 (Linear), L.2 (GitHub), L.3 (Slack/email) adapters are
  SPECIFICATIONS (request/response/error-mode shape); Phase B materialisation
  per OQ-MERGED-5 specify-and-stub pattern. Auth tokens externalised to
  `private/<service>-auth.yaml` (RUSLAN-LAYER).

- **C3 Phase A boundary clarification.** Phase A inbound external = Phase B
  work. Phase A external touchpoints are OWNER-INITIATED ONLY (Ruslan
  triggers via `/ingest <url>` via Part 2 OR triggers external write via
  Part 10 RT-2 with explicit ack). Phase A external system NEVER auto-acts
  on inbound external signals — no auto-reply on email; no auto-comment on
  GitHub; no auto-Linear-status-update from external webhook. Phase B
  activation event: sustained operational maturity (Phase A operational ≥3
  months; Tier 0 health-integrity events <1 per quarter; methodology library
  ≥10 entries F5).

**§X FINAL CLOSURE for OQ-MERGED-3 fork-separation.** Bundle 4 = last chance
for Foundation-level fork-separation declaration. Part 10 has the highest
creep risk because RUSLAN-LAYER ICP specifics (DACH market, German GDPR
config, specific contact lists, Linear/GitHub/Notion auth tokens, DACH-
specific intelligence tracker URLs) shade into Foundation-generic CRM
mechanics if §X is sloppy. Critic gate auto-rejects ambiguous §X declarations
— explicit DACH/GDPR/auth-token/contact-list/intelligence-URL examples
MANDATORY.

**OQ-B1-5 D27 reconciliation_strategy field promotion.** Bundle 1
`cross-fork-provenance.json` has `approvals_reconciliation_strategy` in the
`metadata` open field. Bundle 4 Part 10 §I.1 PROMOTES this to a top-level
field with 5 declared reconciliation strategies (parent-wins / fork-wins /
manual-merge / decline-import / pending-review). Constitutional supplement
record commits at end-of-cycle (Phase H per §4.5 of deep prompt) — analogous
to OQ-B2-A pattern but inverted timing.

The CRM data model is anchored in cycle 10 operational baseline [src:swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md;
src:crm/README.md]. The integration adapter pattern is anchored in
multi-agent-architecture A2A discipline [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/multi-agent-architecture.md].
The privacy invariants are anchored in Anthropic CAI + Askell HHH + FUNDAMENTAL
§6.4 [src:raw/books-md/anthropic/bai-2022-cai.md; src:raw/books-md/anthropic/askell-2021-hhh.md;
src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.4]. The CRM 8 edge
types are anchored in the wiki/graph/edges.jsonl typed-edge taxonomy (UND-5
binding to Part 3) [src:crm/_schema/edges.yaml; src:swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md:§I.2].

**Phase A scope discipline.** Single-owner Jetix Phase-A €50K horizon. CRM
operates with 4 contacts (3 mentor/advisor + 1 partner-prospect per AUDIT
§7.5); 0 orgs (pre-allocated). Voice integration via DRAFT-only flow
(`tools/run_pipeline.sh` step 3 emits `target: crm` items;
`crm/_scripts/voice_router.py` creates `<slug>-DRAFT.md`). All contact data
is RUSLAN-LAYER; CRM mechanics are Foundation generic.

**Fork-portable by construction.** A Phase B partner forks Foundation,
imports CRM data model + integration adapter pattern + privacy invariants +
write-ack discipline + reconciliation strategies; declines RUSLAN-LAYER
(DACH ICP, German GDPR config, Ruslan's specific contact list, Linear/GitHub/
Notion/Slack auth tokens, DACH intelligence tracker URLs); populates own
RUSLAN-LAYER per partner's market + jurisdiction + contact network.

[F4|G:Bundle 4 Part 10 architecture — Phase A single-owner; Fork-portable; CRM canonicalised|R-medium — pending Ruslan ack]

---

## §A Inputs

| Source | Data shape | Event trigger | F-G-R |
|---|---|---|---|
| External signals (new contact, inbound message, meeting note, mention) | Inbound external observation prose; Phase A is OWNER-INITIATED ONLY (Ruslan triggers via /ingest URL via Part 2 OR explicit /crm-add invocation) | External-signal event → routed via Part 2 `/ingest` (C3: Phase A inbound = Part 2 territory; Part 10 owns the boundary, not the ingestion pipeline) | F2|G:per-event observation|R-low — pre-triage |
| `crm/people/<slug>.md` + `crm/orgs/<slug>.md` | Existing contact records per cycle 10 frontmatter schema (`crm/_schema/frontmatter.yaml`) — 14 sections; 4 contacts currently per AUDIT §7.5 | Read at /crm-show, /crm-list, /crm-search, /crm-touch invocation | F4|G:per-contact|R-medium — owner-curated |
| `crm/_schema/` 4 YAML files | Frontmatter (12 field groups) + roles (24 roles in 6 groups) + statuses (13 pipeline) + strategy-hooks (6 offers + 6 asks) | Read at /crm-* skill invocation | F5|G:cycle 10 LOCKED|R-high |
| Owner ack signals for external write-actions | AWAITING-APPROVAL packet ack record per Part 6b §I.4 F8 schema with `gate_class: stage_gate` | Ruslan ack on AWAITING-APPROVAL packet via Part 6b enforcement arm | F5|G:Part 6b §I.4 LOCKED|R-high — human ack |
| Part 9 weekly review surfacing stuck contacts | `/crm-stuck` list — contacts with >14d no touch + active status (per AUDIT §7.6 + crm/_schema/statuses.yaml stuck threshold) | Per weekly review event from Part 9 §J.2 | F4|G:Part 9 Bundle 4 LOCKED|R-medium |
| `wiki/graph/edges.jsonl` | 8 CRM-to-wiki typed edge types per UND-5 binding (Part 3 §I taxonomy + crm/_schema/edges.yaml) | Read at /crm-touch + relationship-state-change events | F4|G:Part 3 + cycle 10|R-medium |
| Voice-pipeline DRAFT items | `<slug>-DRAFT.md` files created by `crm/_scripts/voice_router.py` from `tools/run_pipeline.sh` step 3 emit | Per voice-pipeline run; DRAFT only — owner promotes manually | F2|G:per-DRAFT|R-low — pre-promotion |
| RT-1 read-only intelligence signals | Signals from HN / sub-Reddits / niche newsletters (Phase B materialisation; SPECIFICATION only Phase A) | Per RT-1 adapter poll event (Phase B); Phase A: NOT IMPLEMENTED | F3|G:RT-1 stub|R-low — Phase B |
| `private/<service>-auth.yaml` | Auth tokens for Linear / GitHub / Notion / Slack (Phase B; RUSLAN-LAYER); referenced by Phase B RT-2 adapters | Read at RT-2 invocation (Phase B); Phase A: NOT IMPLEMENTED | F2|G:RUSLAN-LAYER token|R-low — out-of-band |

**§A.1 Concrete consequence — CRM data model is canonicalised, not
redesigned.** Per Bundle 4 §2.3 special: existing 24 source files / 35 unit
tests / 10 `/crm-*` skills / 4 YAML schemas operate as Phase A baseline. Part
10 §A inputs REFERENCE the existing tree. If improvements surface from
Wisdom Loop or critic gate → log as OQ-B4-X for Wave D consideration; do NOT
re-implement in Bundle 4. Brigadier autocheck rejects Part 10 proposing an
alternative CRM data model. [src:crm/README.md; src:crm/PLAN.md;
src:swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md]

**§A.2 Concrete consequence — Phase A inbound external is OWNER-INITIATED
only (C3 declared Phase B).** Inbound external signals (new email, GitHub
mention, Linear ticket comment) are NOT auto-ingested. Phase A flow: Ruslan
manually triggers `/ingest <url>` via Part 2; Part 2 emits triage event to
Part 10 if the inbound is contact-related; Part 10 routes to /crm-add or
/crm-touch as appropriate. Phase B activation: sustained operational maturity
predicate (≥3 months Phase A; Tier 0 health-integrity events <1/quarter;
methodology library ≥10 entries F5). Until Phase B activation: NO RT-1
adapter polls inbound; NO RT-2 adapter auto-replies. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§3.3 C3]

**§A.3 Concrete consequence — Voice-pipeline DRAFT-only flow preserved.**
Voice pipeline produces `<slug>-DRAFT.md` files via voice_router.py. Owner
promotes manually after review (per CLAUDE.md CRM System: Voice integration
discipline). Part 10 §A.3 does NOT auto-promote; canonical pattern preserved.
[src:CLAUDE.md:CRM System Voice integration]

---

## §B Outputs

| Consumer | Data shape | Event published | F-G-R |
|---|---|---|---|
| `crm/people/<slug>.md` + `crm/orgs/<slug>.md` | Updated contact records — append-only §11 history per cycle 10 frontmatter schema | `[crm] touch: <slug> (interaction logged)` commit via Part 1 §H per D25/D17 | F4|G:per-contact|R-medium |
| `crm/index.md` | Auto-regenerated index by `/crm-rebuild-index` | Per index regen event; idempotent | F4|G:current state|R-medium |
| `crm/log.md` | Append-only activity log | Per contact interaction event | F4|G:audit trail|R-medium |
| `crm/views/` | Saved filtered views (weekly reports) | Per /crm-weekly invocation | F4|G:per-view|R-medium |
| Inbound signal forwarding → Part 2 `/ingest` | Forwarded signal-ready event (external capture is Part 2's domain; Part 10 is the boundary layer) | Per inbound external event (Phase A: OWNER-INITIATED ONLY) | F3|G:per-signal|R-low — pre-triage |
| AWAITING-APPROVAL packets to Part 6b for outbound external | `awaiting-approval-packet.json` per Part 6b §I.4 F8 schema with `gate_class: stage_gate`; populated for ALL external write-actions | Per outbound external write request (RT-2 adapter Phase B) | F8|G:Part 6b LOCKED schema|R-high |
| CRM graph edges → `wiki/graph/edges.jsonl` | 8 CRM edge types per `crm/_schema/edges.yaml` (UND-5 binding to Part 3) | Per relationship-state-change event | F4|G:Part 3 §I.2 + UND-5|R-medium |
| Cross-fork-provenance entries → Part 1 `cross-fork-provenance.json` | Cross-fork records per Part 1 §I.1 schema (Bundle 4 supplement 2: `approvals_reconciliation_strategy` promoted to top-level field with 5 declared strategies) | Per Phase B partner-fork import event | F4|G:Part 1 + Bundle 4 supplement|R-medium |
| Part 1 §H commit substrate | All Part 10 outputs committed as git artefacts per IP-3 (D25/D17) | `artifact-committed` event | F5|G:IP-3 + D17|R-high |
| Part 8 health-signal pipeline | `crm-touch-rate` / `crm-stuck-rate` / `external-action-latency` / `integration-adapter-health` / `voice-pipeline-draft-promotion-rate` SLIs — emitted per Part 8 §I.1 canonical health-signal schema | `health-metric-updated` event | F4|G:Part 8 SLI consumption|R-medium |
| `swarm/approvals/log.jsonl` (Part 6a §C) | One entry per RT-2 ack — recording timestamp, contact_slug, gate_class=stage_gate, action description, Ruslan ack signature | `approval-logged` event via Part 6a service | F5|G:Part 6a §C F8 schema|R-high |
| `swarm/wiki/log.md` | Append-only log line per CRM event | Per event | F4|G:audit trail|R-medium |
| L.1/L.2/L.3 adapter request shapes (Phase B; SPECIFICATION only Phase A) | Linear / GitHub / Slack/email request bodies per integration adapter pattern (§I.4) | Per RT-2 invocation (Phase B); Phase A: SPECIFICATION ONLY | F3|G:Phase B stub|R-low — Phase B |

**§B.1 Concrete consequence — RT-2 write-ack discipline.** Every external
write-action (Linear ticket creation, GitHub issue posting, Slack DM,
partner email) MUST verify `consent_recorded_at` field present in CRM contact
record (privacy invariant 1) → blast-radius classify (typically Tier 1
strategic) → emit AWAITING-APPROVAL packet to Part 6b → Ruslan ack → external
write → write-ack confirmation logged to CRM event log + approval log +
cross-fork-provenance log (3-way audit trail). NO write-action proceeds
without ack. Per FUNDAMENTAL §6.1 + Anthropic CAI write-ack discipline.

**§B.2 Concrete consequence — UND-5 CRM edge binding to Part 3.**
`crm/_schema/edges.yaml` declares 8 CRM edge types (e.g., `mentors`,
`advises`, `partner_prospects`, `sourced_via`, `references`, etc.); these
conform to Part 3 `wiki/graph/edges.jsonl` typed-edge taxonomy per UND-5
binding. Part 3 owns the canonical edge taxonomy; Part 10 declares CRM-
specific subset. Phase B partner forks consume both Foundation generic
edge taxonomy + their own RUSLAN-LAYER edge instances. [src:swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md:§I.2;
src:crm/_schema/edges.yaml]

**§B.3 Concrete consequence — Voice-pipeline DRAFT promotion is HITL only.**
DRAFT files emit from voice_router.py with status `draft_from_voice`. Owner
promotes manually via `/crm-update <slug> --promote` (or equivalent action).
NEVER auto-promoted. Part 10 §B does NOT export auto-promote logic; this
preserves cycle 10 discipline.

---

## §C Side-effects

- **Append-only writes to `crm/people/<slug>.md` §11 history.** No editing
  prior interaction records (D25 + FUNDAMENTAL §2.1 cross-cutting append-
  only). Corrections via NEW history entries with `corrects:` pointer per
  Reversal Transactions (Young 2010) [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4 P3].

- **Append-only writes to `crm/log.md`.** Same discipline.

- **CRM graph edges appended to `wiki/graph/edges.jsonl`.** Per relationship-
  state-change event. UND-5 binding to Part 3.

- **NO auto-write to external services without Part 6b gate ack.** Per
  FUNDAMENTAL §4.5 hard rule + §6.1 anti-pattern "auto-respond external без
  ack".

- **Cross-fork-provenance entries committed via Part 1 §H** for Phase B
  partner-fork imports of Foundation-generic CRM patterns.

- **Health signal emissions via swarm/lib accessor.** NO direct file writes
  to `shared/state/system-health.json`. Per Bundle 2 C1 Joint Design
  canonical.

- **Forget-request side-effects (privacy invariant 2):** `[REDACTED]` markers
  applied to CRM event log entries; cross-fork-provenance entries flagged
  `consent-revoked-cascade`; wiki references stripped via
  `/lint --check-forget-request-cascade` (Phase B). Reversal Transactions
  discipline: forget-request = NEW entry with `corrects:` + `redaction_reason:
  forget-request` (NEVER deletes history; marks redacted).

- **Default-Deny for novel external action classes.** Any external action
  class not pre-classified in Part 6b §I.2 default-deny-table.yaml fires
  Halt-Log-Alert (≤1s halt / ≤5s log / ≤60s alert per Part 6b §E L9).

---

## §D Dependencies (typed per FPF A.14)

| Dep | Edge type | Target | Rationale |
|---|---|---|---|
| D-1 | `methodologically-uses` | **Part 3** | UND-5 binding — CRM 8 edge types per `crm/_schema/edges.yaml` conform to Part 3 `wiki/graph/edges.jsonl` typed-edge taxonomy. Part 3 owns canonical edge mechanism; Part 10 declares CRM subset. [src:swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md:§I.2] |
| D-2 | `methodologically-uses` | **Part 6b** | RT-2 write-ack via stage-gate `gate_class: stage_gate`. Default-Deny for novel external action classes per §I.2. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4 + §I.2] |
| D-3 | `methodologically-uses` | **Part 2** | C3 — inbound external = Phase B work; Phase A inbound routes via Part 2 `/ingest` (owner-initiated only). [src:swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md] |
| D-4 | `methodologically-uses` | **Part 1** | Cross-fork-provenance entries committed via Part 1 §H. CRM records committed via Part 1 §H per D25/D17. [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§H + §I.1] |
| D-5 | `creates` | **Part 1** | CRM events committed; cross-fork-provenance entries committed. |
| D-6 | `methodologically-uses` | **Part 6a** | F-G-R per Part 6a §I.1 F8 schema on every emitted artefact. Approval-log entries written per Part 6a §C on each RT-2 ack. [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1 + §C] |
| D-7 | `derives-from` | **Part 8 §I.1** | Health emissions conform to canonical health-signal schema F5 (Bundle 3). [src:swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md:§I.1] |
| D-8 | `methodologically-uses` | **Part 9** | Weekly review surfaces stuck contacts via `/crm-stuck` (per AUDIT §7.6 + crm/_schema/statuses.yaml). [src:swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md:§J.2] |
| D-9 | `constrained-by` | **FUNDAMENTAL §6.4** | 4 privacy invariants STRUCTURALLY enforced. Behavioral framing prose <10%. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.4] |
| D-10 | `constrained-by` | **FUNDAMENTAL §6.1** | Default-Deny constitutional; no auto-action external without ack. [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1] |
| D-11 | `constrained-by` | **FPF IP-2** | Single-owner Phase A bounded; F.9 Bridge structural change ≥35% required at multi-owner activation. [src:design/JETIX-FPF.md:§5.2] |
| D-12 | `derives-from` | **CRM cycle 10 baseline** | 24 source files / 35 unit tests / 10 skills / 4 schemas; canonicalisation NOT redesign. [src:crm/README.md; src:swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md] |
| D-13 | `derives-from` | **Anthropic CAI / Askell HHH** | Privacy + write-ack discipline + hardcoded never-list. [src:raw/books-md/anthropic/bai-2022-cai.md; src:raw/books-md/anthropic/askell-2021-hhh.md] |
| D-14 | `derives-from` | **Young 2010 CQRS** | Reversal Transactions for forget-request (NEW redacted entry; never deletes history). [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4] |

**No `depends-on` generic edges.** Per Bundle 1 Part 6a A.14 typed-edge
discipline.

---

## §E Boundary (FPF A.6.B L/A/D/E)

### E.1 Laws (invariants that MUST hold)

**L1 — Default-Deny for external write-actions.** All write-actions to
external services REQUIRE explicit human ack before execution — no
exceptions (FUNDAMENTAL §6.1 last bullet "якщо action не categorized —
default deny + escalate"; FUNDAMENTAL §4.5 anti-pattern "auto-create
commitments external"; Bundle 1 Default-Deny F8 LOCKED).

**L2 — Privacy invariants STRUCTURAL (FUNDAMENTAL §6.4).** All 4 invariants
enforced via schema fields + lint signals + Default-Deny entries; NOT
behavioral framing prose. Behavioral framing target <10% of privacy section.

**L3 — Append-only history.** §11 of each contact record append-only; no
editing/deletion of past interaction records (D25; FUNDAMENTAL §2.1).
Forget-request is NEW redacted entry per Reversal Transactions (Young 2010);
NEVER deletes history.

**L4 — D17 Filesystem = SoT.** CRM records live in filesystem as authoritative
source; Notion/external views are read-only projections.

**L5 — Phase A inbound external = OWNER-INITIATED ONLY (C3).** No auto-
ingestion of inbound external signals. Phase B activation event: sustained
operational maturity predicate.

**L6 — Halt-Log-Alert ordering for Tier 0 events.** Privacy invariant
violation attempts (e.g., classifier on race/religion/political/health)
fire Halt-Log-Alert per Part 6b §E L9 (≤1s halt / ≤5s log / ≤60s alert).

**L7 — RT-1 read-only invariant.** RT-1 adapters NEVER write externally.
All RT-1 emit signals to Part 2 `/ingest` triage; Tier 3 blast-radius (auto-
log, no gate).

**L8 — RT-2 consent verification mandatory.** Every RT-2 invocation verifies
`consent_recorded_at` field present in target contact record before
proceeding. Consent absent → HALT + AWAITING-APPROVAL `gate_class: stop_gate`
(Tier 1 escalation).

**L9 — Voice-pipeline DRAFT-only.** `<slug>-DRAFT.md` files NEVER auto-
promoted to production records; owner promotes manually after review.

**L10 — UND-5 CRM edge conformance.** All CRM edges write to
`wiki/graph/edges.jsonl` per Part 3 typed-edge taxonomy; CRM 8 edge types
declared in `crm/_schema/edges.yaml`.

**L11 — Auth tokens externalised.** No auth tokens hardcoded in Foundation
schema; all auth via `private/<service>-auth.yaml` reference (RUSLAN-LAYER).

**L12 — Reconciliation strategy declared.** Cross-fork imports apply
reconciliation strategy per Part 1 §I.1 supplement 2 (D27 promotion):
parent-wins | fork-wins | manual-merge | decline-import | pending-review.

### E.2 Admissibility (acceptance criteria for inputs)

**A-1.** New contact records admitted only if they carry: name, context
(generic role relationship type per `crm/_schema/roles.yaml` 24 roles),
source provenance (how contact was established), initial status (per
`crm/_schema/statuses.yaml` 13 pipeline), `consent_recorded_at: <ISO
timestamp>` (privacy invariant 1).

**A-2.** External write-action requests admitted only if accompanied by:
(a) draft + owner ack signal; (b) dry-run mode preview pre-execute; (c)
target contact has `consent_recorded_at` populated.

**A-3.** Voice-to-CRM pipeline items admitted ONLY as DRAFT state
(`draft_from_voice` status) — never auto-promoted. Owner promotes manually
after review per CLAUDE.md CRM System Voice integration.

**A-4.** RT-1 read-only signals admitted at Part 2 `/ingest` triage —
classified per Part 2 admissibility rules; CRM-related signals route to
Part 10 /crm-add or /crm-touch.

**A-5.** Forget-request admitted only with `redaction_reason: forget-request`
field + `corrects: <prior-entry-id>` pointer (Reversal Transactions
discipline). Schema validation rejects mutations of prior entries.

**A-6.** New CRM edge types admitted only via AWAITING-APPROVAL
`gate_class: stage_gate` for `crm/_schema/edges.yaml` extension; default-
deny on novel edge types.

**A-7.** Phase B inbound external (RT-1 adapter activation) admitted only
after Phase B activation predicate satisfied: ≥3 months Phase A operational
+ Tier 0 events <1/quarter + methodology library ≥10 entries F5.

### E.3 Deontics (obligations toward consumers)

**D-1.** MUST surface stuck contacts (>14d no touch + active status) to
Part 9 weekly review (per `/crm-stuck` skill output).

**D-2.** MUST route ALL inbound external signals to Part 2 (no direct
ingestion into KB from Part 10).

**D-3.** MUST open Part 6b gate request for any external service write-
action before execution (J-Approve minimum; J-Strategic for destructive
actions).

**D-4.** MUST NOT embed RUSLAN-LAYER ICP content in Foundation contact
schema (D27 + OQ-MERGED-3 fork-separation FINAL CLOSURE).

**D-5.** MUST emit health signals via `swarm/lib/emit_health_signal()`
accessor; NO direct writes to `shared/state/system-health.json`.

**D-6.** MUST verify `consent_recorded_at` field present before any RT-2
write-action.

**D-7.** MUST cascade forget-request via `/lint --check-forget-request-
cascade` (Phase B) covering CRM event log + cross-fork-provenance entries
+ wiki references.

### E.4 Effects (measurable outcomes)

**E-1.** CRM records committed with provenance within ≤1 session of contact
interaction.

**E-2.** Stuck-contact surface rate: 100% — all contacts with >14d no touch
and active status appear in weekly review output.

**E-3.** Write-ack gate opened via Part 6b for every outbound external
action (audit trail: 100% of external write-actions have committed gate
record + approval log + cross-fork-provenance log entry).

**E-4.** Voice-pipeline DRAFT promotion rate: tracked per Part 8 SLI;
indicative target: ≥80% of DRAFTs reviewed by owner within 7 days
(prevents DRAFT pile-up).

**E-5.** RT-1 read-only invariant: 100% — zero RT-1 write events observed.
SLO target: 100%; deviation = Tier 0 violation.

**E-6.** RT-2 consent verification: 100% — every RT-2 invocation verifies
consent. SLO target: 100%; deviation = Tier 0 violation.

**E-7.** Forget-request cascade coverage: 100% — all references stripped
within ≤24h of forget-request commit.

**E-8.** Privacy invariant violation attempts: 0/cycle — no classifier
attempts on protected characteristics. SLO target: 0; any non-zero =
Tier 0 escalation.

**E-9.** External-action-latency: 50th percentile <2h between Ruslan ack
and write-ack confirmation; 95th percentile <24h.

**E-10.** Integration adapter health: per RT-2 adapter, success-rate ≥95%;
auth failures + timeout failures tracked; alert on <80%.

---

## §F Anti-scope

**Generic anti-scope:**
- Part 10 does NOT make strategic decisions about relationship direction —
  surfaces relationship state; owner decides (FUNDAMENTAL §6.1, §6.2).
- Part 10 does NOT substitute for founder agency in relationship management.
- Part 10 does NOT use engagement-economy patterns (FUNDAMENTAL §6.3) — no
  notification spam, no FOMO mechanics, no auto-message without ack.
- Part 10 does NOT auto-respond to external contacts without owner ack.
- Part 10 does NOT own the ingestion pipeline — inbound signals routed to
  Part 2; Part 10 is the external boundary.

**Part-specific anti-scope (CRITICAL — FUNDAMENTAL §6.4 privacy hard rules):**
- Part 10 does NOT infer protected characteristics (race / religion /
  political affiliation / health status) from CRM interaction data — NEVER.
  Default-Deny entry per Part 6b §I.3 enforces; lint signal `/lint --check-
  protected-inference` (Phase B) enforces structurally.
- Part 10 does NOT retain data after `forget-request` without verifiable
  hard delete cascade (Reversal Transactions: NEW redacted entry; references
  stripped).
- Part 10 does NOT log sensitive contact information (financial details,
  health status, credentials) in plain text — encryption at rest precondition
  (Part 1 substrate level).
- Part 10 does NOT share or sell contact data to third parties under any
  pretext.
- Part 10 does NOT embed RUSLAN-LAYER content in Foundation CRM schema:
  DACH ICP / German GDPR / specific contact lists / Linear+GitHub+Notion+Slack
  auth tokens / DACH-specific intelligence URLs are RUSLAN-LAYER (per §X
  FINAL CLOSURE).
- L.1-L.3 external integrations are Phase-A SPECIFICATIONS ONLY — no
  operational implementation in Phase A; materialisation is Phase B per OQ-
  MERGED-5 specify-and-stub.

**C3 boundary (Phase A inbound = Phase B work):**
- Phase A external touchpoints are OWNER-INITIATED ONLY. Ruslan triggers
  via `/ingest <url>` via Part 2 OR triggers external write via Part 10
  RT-2 with explicit ack.
- Phase A external system NEVER auto-acts on inbound external signals — no
  auto-reply on email; no auto-comment on GitHub; no auto-Linear-status-
  update from external webhook.
- Phase B activation event: sustained operational maturity signal (Phase A
  operational ≥3 months; Tier 0 health-integrity events <1/quarter;
  methodology library ≥10 entries F5).

---

## §G F-G-R Tagging

| Artefact emitted by Part 10 | F | G (ClaimScope) | R |
|---|---|---|---|
| Contact record (production) | F4 | This contact's relationship context | R-medium — owner-curated |
| Contact record (draft_from_voice) | F2 | Pre-review draft; not yet owner-acked | R-low — voice pipeline output |
| CRM activity log entry | F4 | This interaction event | R-medium — committed, append-only |
| CRM index | F4 | Current state of all contacts | R-medium — auto-generated |
| CRM graph edges in edges.jsonl | F4 | Relationship between two entities; UND-5 typed | R-medium |
| Write-action gate request | F3 | Single external action, pending ack | R-low — unexecuted |
| L.1-L.3 integration stubs | F3 | Phase B materialisation surface | R-low — interface spec only |
| Cross-fork-provenance entry | F4 | Single fork-import event | R-medium |
| Forget-request redaction entry | F5 | Single contact, post-redaction | R-high — reversal transaction committed |
| Privacy invariant violation alert | F5 | Single attempted violation | R-high — Tier 0 alert fired |
| Consent record | F5 | Single contact + timestamp | R-high — owner-acked |
| RT-2 write-ack confirmation | F5 | Single external write event | R-high — post-ack + post-write |

---

## §H Code-level Interfaces

Part 10 references existing CRM code (canonicalisation, NOT redesign) AND
declares Phase B integration adapter stubs. All Phase B interfaces are
SPECIFICATIONS per OQ-MERGED-5 specify-and-stub pattern.

### H.1 Existing CRM code (canonicalised; cycle 10 baseline)

| File | Purpose | Lines | Operational |
|---|---|---|---|
| `crm/_scripts/crm.py` | Main CLI router | 482 | Phase A operational |
| `crm/_scripts/dashboard.py` | Dashboard + stuck + weekly | 287 | Phase A operational |
| `crm/_scripts/voice_router.py` | Voice → DRAFT-only | 218 | Phase A operational |
| `crm/_scripts/frontmatter.py` | Parser + validator + auto-fix | 226 | Phase A operational |
| `crm/_scripts/views.py` | Query engine | 185 | Phase A operational |
| `crm/_scripts/index_builder.py` | Index regenerator | 135 | Phase A operational |
| `crm/_scripts/strategy_hooks.py` | Offer/ask matcher | 126 | Phase A operational |

10 `/crm-*` skills (per CLAUDE.md CRM section): `/crm-add`, `/crm-show`,
`/crm-list`, `/crm-search`, `/crm-touch`, `/crm-update`, `/crm-rebuild-index`,
`/crm-dash`, `/crm-stuck`, `/crm-weekly`. **Phase A canonical; Bundle 4 does
NOT modify.**

### H.2 RT-1 read-only intelligence tracker pattern (Phase B; specify-and-stub)

```python
def rt1_poll(source_url: str, source_type: Literal["hn", "subreddit", "newsletter"]) -> dict:
    """
    Poll URL → parse → emit signal to Part 2 /ingest triage queue. NEVER writes
    externally. Tier 3 blast-radius (auto-log, no gate).

    Phase A: NOT IMPLEMENTED. SPECIFICATION ONLY for Phase B materialisation.
    Phase B activation predicate (per L5 + §F C3): ≥3 months Phase A operational
    + Tier 0 events <1/quarter + methodology library ≥10 F5 entries.

    Returns: {
      "signals_emitted": int,
      "ingest_packet_ids": list[str],
      "blast_radius": "tier-3",
      "side_effects": list[str]  # always empty for RT-1 — read-only invariant
    }
    """
```

### H.3 RT-2 write-ack action coordinator pattern (Phase B; specify-and-stub)

```python
def rt2_invoke(
    contact_slug: str,
    action_type: Literal["linear-ticket", "github-issue", "slack-dm", "email"],
    action_payload: dict,
    dry_run: bool = False,
) -> dict:
    """
    Receive request → verify CRM consent (consent_recorded_at present in
    contact record; privacy invariant 1) → blast-radius classify → AWAITING-
    APPROVAL gate_class: stage_gate to Part 6b → on Ruslan ack → external write
    → write-ack confirmation logged to CRM event log + approval log + cross-
    fork-provenance log.

    Phase A: NOT IMPLEMENTED. SPECIFICATION ONLY for Phase B materialisation.

    On consent absent: HALT + AWAITING-APPROVAL gate_class: stop_gate Tier 1
    escalation. Returns {"halted": True, "stop_gate_packet_id": str}.

    Returns: {
      "rt2_invocation_committed": bool,
      "consent_verified": bool,
      "stage_gate_packet_id": str | None,
      "external_action_completed": bool,
      "audit_trail": dict  # {crm_log_entry, approval_log_entry, cross_fork_provenance_entry}
    }
    """
```

### H.4 L.1 Linear adapter (Phase B; specify-and-stub)

```python
def linear_create_ticket(team_id: str, title: str, body: str, **kwargs) -> dict:
    """Linear ticket creation. Auth via private/linear-auth.yaml (RUSLAN-LAYER)."""

def linear_post_comment(issue_id: str, body: str) -> dict:
    """Linear comment posting."""

def linear_update_status(issue_id: str, status: str) -> dict:
    """Linear status update."""
```

### H.5 L.2 GitHub adapter (Phase B; specify-and-stub)

```python
def github_create_issue(repo: str, title: str, body: str, **kwargs) -> dict:
    """GitHub issue creation. Auth via private/github-auth.yaml (RUSLAN-LAYER)."""

def github_create_pr(repo: str, title: str, body: str, base: str, head: str, **kwargs) -> dict:
    """GitHub PR creation."""

def github_post_comment(issue_or_pr_url: str, body: str) -> dict:
    """GitHub comment posting."""
```

### H.6 L.3 Slack/email adapter (Phase B; specify-and-stub)

```python
def slack_send_dm(user_id: str, body: str) -> dict:
    """Slack DM send. Auth via private/slack-auth.yaml (RUSLAN-LAYER)."""

def slack_post_channel(channel_id: str, body: str) -> dict:
    """Slack channel post."""

def email_send(to: str, subject: str, body: str, **kwargs) -> dict:
    """Email send. Auth via private/email-auth.yaml (RUSLAN-LAYER)."""
```

**§H.7 Privacy lint signal skill specs (Phase B; specify-and-stub)**

```python
def lint_check_consent() -> dict:
    """
    Scan all CRM contact records; verify consent_recorded_at field present.
    Flag contacts missing consent. Phase B implementation per OQ-MERGED-5.

    Returns: {"checked": int, "missing_consent": list[str], "exit_code": int}
    """

def lint_check_protected_inference() -> dict:
    """
    Scan all CRM contact records + agent strategies.md + wiki entries; flag
    any classifier on race / religion / political affiliation / health status.
    Phase B implementation per OQ-MERGED-5.

    Returns: {"checked": int, "violations": list[dict], "exit_code": int}
    """

def lint_check_forget_request_cascade() -> dict:
    """
    Scan CRM event log + cross-fork-provenance + wiki references for residual
    references to forget-request-redacted contacts. Phase B implementation.

    Returns: {"checked": int, "residual_refs": list[str], "exit_code": int}
    """
```

These skill specs are NOT IMPLEMENTED in Phase A. Brigadier autocheck verifies
specs declared with Phase B materialisation reference per §6.10 procedure.

### H.8 Auth-token externalisation pattern

```yaml
# private/<service>-auth.yaml — RUSLAN-LAYER (NOT in Foundation tree)
# Foundation generic = the auth-token externalisation pattern; specific tokens
# are RUSLAN-LAYER per fork.

# Example: private/linear-auth.yaml (RUSLAN-LAYER)
service: linear
auth_token: <REDACTED — environment variable LINEAR_API_TOKEN expected>
team_ids:
  - <RUSLAN-LAYER team binding>
rotation_policy:
  rotate_every_days: 90
  next_rotation: <ISO date>
```

Foundation generic invariants:
- Path convention: `private/<service>-auth.yaml`.
- Rotation policy: declared per service; default 90 days.
- Secret-scan compliance: `grep -rEn 'ANTHROPIC_API_KEY|GROQ_API_KEY|sk-ant-|<service>_API_TOKEN'`
  on Foundation tree returns 0 hits (CLAUDE.md API-key audit; pre-commit hook
  enforces).

---

## §I Data Schemas

### §I.1 `cross-fork-provenance.json` cross-reference + 5 reconciliation strategies (OQ-B1-5 D27 promotion)

Bundle 4 Part 10 §I.1 PROMOTES `approvals_reconciliation_strategy` from Part 1
§I.1 `metadata` open field to **top-level field**. Constitutional supplement
record commits at end-of-cycle (Phase H) per OQ-B1-5 ack pattern.

**5 reconciliation strategies declared:**

| Strategy | Semantic | Used for |
|---|---|---|
| `parent-wins` | Foundation parent ack supersedes fork's local ack | Foundation invariants (privacy + corrigibility + Halt-Log-Alert ordering) |
| `fork-wins` | Fork's local ack supersedes Foundation parent | RUSLAN-LAYER ICP-specific values when partner has different ICP |
| `manual-merge` | HITL Ruslan + partner pair-resolve via AWAITING-APPROVAL `gate_class: stage_gate` | Cross-cutting changes affecting both Foundation + RUSLAN-LAYER |
| `decline-import` | Fork explicitly declines Foundation's ack | Foundation patterns inappropriate for fork's domain |
| `pending-review` | Fork holds ack for next sync window | Default state pre-resolution |

**Phase B explicit:** This schema field is FOUNDATION-LEVEL declarative;
reconciliation actions are PHASE B work (no Phase A reconciliation events
since Phase A is single-owner with no partner fork).

**Cross-fork-provenance.json schema fragment (Part 1 §I.1 supplement 2):**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/cross-fork-provenance.json",
  "$comment": "Bundle 4 supplement 2 — approvals_reconciliation_strategy promoted from metadata open field to top-level (per OQ-B1-5 RUSLAN-ACK Bundle 1).",
  "schema_version": "1.1.0",
  "schema_version_history": [
    {
      "version": "1.0.0",
      "date": "2026-04-28",
      "changes": "Initial Phase A stub. reconciliation_strategy: deferred-phase-b only.",
      "breaking": false
    },
    {
      "version": "1.1.0",
      "date": "2026-04-28",
      "changes": "Bundle 4 supplement 2 — approvals_reconciliation_strategy promoted from metadata to top-level field with 5 declared strategies (parent-wins / fork-wins / manual-merge / decline-import / pending-review).",
      "breaking": false,
      "supersedes": "1.0.0 metadata.approvals_reconciliation_strategy field"
    }
  ],
  "type": "object",
  "required": [
    "schema_version",
    "parent_repo_id",
    "parent_commit_hash",
    "fork_id",
    "fork_branch",
    "divergence_point",
    "reconciliation_strategy",
    "approvals_reconciliation_strategy",
    "audit_trail_continuation",
    "f_g_r_on_imported_claims",
    "ip1_role_binding_overrides"
  ],
  "properties": {
    "approvals_reconciliation_strategy": {
      "type": "string",
      "enum": ["parent-wins", "fork-wins", "manual-merge", "decline-import", "pending-review"],
      "description": "How fork's local approval acks reconcile against Foundation parent acks. Top-level promotion per OQ-B1-5 + Bundle 4 supplement 2."
    }
    // ... existing fields per Part 1 §I.1 v1.0.0
  }
}
```

[F4|G:OQ-B1-5 D27 promotion declared|R-medium — supplement record commits Phase H]

### §I.2 CRM data model (canonicalises existing 4 YAML schemas in `crm/_schema/`)

**Bundle 4 CANONICALISES — does NOT redesign.** References existing cycle 10
implementation [src:crm/README.md; src:swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md].

**Existing schemas (canonicalised):**

| File | Purpose | Field groups | Bundle 4 binding |
|---|---|---|---|
| `crm/_schema/frontmatter.yaml` | JSON-Schema spec for contact records | 12 field groups (per AUDIT §7.2) | Foundation generic STRUCTURE; specific fields canonicalised verbatim |
| `crm/_schema/roles.yaml` | 24 roles in 6 groups (sales / capital / partnership / advisory / team / network) + transitions | 24 enum + transition rules | Foundation generic role taxonomy |
| `crm/_schema/statuses.yaml` | 13 pipeline statuses + stuck threshold 14 days | 13 enum + threshold | Foundation generic pipeline structure |
| `crm/_schema/strategy-hooks.yaml` | 6 offers + 6 asks with relevance filters | 12 hooks + filter rules | RUSLAN-LAYER content; Foundation generic = the hook structure |

**Bundle 4 supplement to `crm/_schema/frontmatter.yaml` (privacy invariant 1):**

```yaml
# Bundle 4 P10 addition: consent_recorded_at field MANDATORY at contact creation.
# Privacy invariant 1: structural enforcement.

privacy_fields:
  consent_recorded_at:
    type: string
    format: date-time
    required: true
    description: "ISO 8601 timestamp when contact's consent to information
                  storage was recorded. MANDATORY before any RT-2 write-action
                  proceeds. Lint signal /lint --check-consent verifies presence."

  consent_revoked_at:
    type: string
    format: date-time
    required: false
    description: "ISO 8601 timestamp if/when contact has revoked consent.
                  Triggers forget-request cascade per privacy invariant 2."

  redaction_reason:
    type: string
    enum: ["forget-request", "data-minimization", "schema-evolution"]
    required: false
    description: "Reason for redaction; required if redacted entry."
```

[F4|G:Bundle 4 P10 privacy invariant 1 schema field|R-medium]

### §I.3 CRM 8 edge types (UND-5 binding to Part 3 wiki/graph/edges.jsonl)

Per `crm/_schema/edges.yaml` (cycle 10 deliverable + Bundle 4 UND-5 binding):

| Edge | Direction | Cardinality | Phase A use |
|---|---|---|---|
| `mentors` | Person → Person | many-to-many | Anton mentors Ruslan |
| `advises` | Person → Person OR Person → Org | many-to-many | Vladislav advises Ruslan |
| `partner_prospects` | Person → Person | many-to-many | Rodion partner_prospect to Ruslan |
| `sourced_via` | Contact → Source-event | one-to-one | Contact origin trace |
| `references` | Contact → Wiki-entry OR Project | many-to-many | Contact references methodology / project |
| `co-founded` | Person → Org | many-to-many | Phase B: co-founder of org |
| `vendor_for` | Contact → Service | many-to-many | Phase B: tooling/service vendor |
| `competitor_of` | Person/Org → Person/Org | symmetric | Phase B: competitive intel |

These 8 CRM edge types conform to Part 3 `wiki/graph/edges.jsonl` typed-edge
taxonomy (UND-5 binding). Part 3 owns the canonical edge mechanism; Part 10
declares CRM-specific subset. New CRM edges require AWAITING-APPROVAL
`gate_class: stage_gate` per E.2 A-6.

[F4|G:Bundle 4 P10 UND-5 binding|R-medium]

### §I.4 Integration adapter pattern (RT-1 + RT-2 + L.1/L.2/L.3 stubs)

**Pattern declared inline; Phase B materialisation per OQ-MERGED-5 specify-
and-stub.**

```yaml
schema_version: "1.0.0"
schema_version_history:
  - version: "1.0.0"
    date: 2026-04-28
    changes: "initial Wave C Bundle 4 P10.1 — RT-1 + RT-2 + L.1/L.2/L.3 stubs; SPECIFICATION only Phase A; Phase B materialisation"
    breaking: false
managed_by: brigadier
last_modified: 2026-04-28

foundation_generic:

  rt_1_read_only_intelligence_tracker:
    role: "Poll external sources; emit signals to Part 2 /ingest triage. NEVER writes externally."
    blast_radius_typical: 3  # Tier 3 — Routine per Part 6b §I.3
    gate_class_typical: null  # No gate (auto-log)
    request_shape:
      source_url: string
      source_type: enum [hn, subreddit, newsletter, custom]
      poll_cadence: duration  # e.g., "30m" for HN; "weekly" for newsletters
    response_shape:
      signals_emitted: int
      ingest_packet_ids: list[str]
      side_effects: list[str]  # always empty — read-only invariant L7
    error_modes:
      - source_unreachable: "Skip; retry next poll cycle; alert if 3+ consecutive failures"
      - parse_error: "Log + skip record; alert if rate > 10%"
      - rate_limit_exceeded: "Backoff per source-specific policy"
    auth_pattern: "Phase B: per-source auth-token via private/<service>-auth.yaml; Phase A: NOT IMPLEMENTED"
    phase_a_status: "specification-only-not-implemented"

  rt_2_write_ack_action_coordinator:
    role: "Receive write-action request; verify CRM consent; classify blast-radius; emit AWAITING-APPROVAL stage_gate; on ack → external write → write-ack confirmation logged."
    blast_radius_typical: 1  # Tier 1 — Strategic per Part 6b §I.3
    gate_class_typical: "stage_gate"
    request_shape:
      contact_slug: string
      action_type: enum [linear-ticket, github-issue, slack-dm, email, custom]
      action_payload: object
      dry_run: bool
    response_shape:
      rt2_invocation_committed: bool
      consent_verified: bool
      stage_gate_packet_id: str | null
      external_action_completed: bool
      audit_trail: {crm_log_entry, approval_log_entry, cross_fork_provenance_entry}
    error_modes:
      - consent_missing: "HALT + AWAITING-APPROVAL stop_gate Tier 1; do NOT fire write"
      - external_service_unreachable: "Fail-loud; log; alert; do not auto-retry destructive actions"
      - auth_failure: "Halt-Log-Alert Tier 1; auth-token rotation required"
      - external_service_rejected: "Capture rejection; surface to next weekly review"
    auth_pattern: "Phase B: per-service auth-token via private/<service>-auth.yaml; Phase A: NOT IMPLEMENTED"
    phase_a_status: "specification-only-not-implemented"

  l_1_linear_adapter:
    role: "Linear ticket / comment / status operations"
    rt_pattern: rt_2  # Inherits RT-2 write-ack discipline
    operations: [create_ticket, post_comment, update_status]
    auth_path: "private/linear-auth.yaml"
    phase_a_status: "specification-only-not-implemented"

  l_2_github_adapter:
    role: "GitHub issue / PR / comment operations"
    rt_pattern: rt_2
    operations: [create_issue, create_pr, post_comment]
    auth_path: "private/github-auth.yaml"
    phase_a_status: "specification-only-not-implemented"

  l_3_slack_email_adapter:
    role: "Slack DM / channel + email operations"
    rt_pattern: rt_2
    operations: [send_dm, post_channel, send_email]
    auth_path: "private/slack-auth.yaml + private/email-auth.yaml"
    phase_a_status: "specification-only-not-implemented"

ruslan_layer_overrides:
  instance_id: jetix-phase-a-single-owner
  # Auth token paths are RUSLAN-LAYER instance-specific.
  # Phase B partner forks provide own auth tokens.
  # DACH-specific intelligence URLs (HN / r/Berlin / specific newsletter URLs) are RUSLAN-LAYER.
```

[F4|G:Bundle 4 P10.1 integration adapter pattern|R-medium]

### §I.5 Privacy schema fields (4 STRUCTURAL invariants — schema fields + lint signals + Default-Deny entries)

**Privacy invariant 1 — Consent enforcement (schema field `consent_recorded_at`):**

- Field MANDATORY in CRM contact record before any RT-2 write-ack adapter
  fires.
- Lint signal `/lint --check-consent` (Phase B; skill spec only).
- Default-Deny entry: external write attempt without `consent_recorded_at` =
  HALT + AWAITING-APPROVAL `gate_class: stop_gate` (Tier 1 escalation).
- Cross-ref: §I.2 frontmatter.yaml supplement; Part 6b §I.2 default-deny-
  table.yaml extension.

**Privacy invariant 2 — Forget-request (skill spec `/crm forget` + Reversal Transactions):**

- Skill spec `/crm forget --contact <id>` (Phase B implementation).
- Behavior: purge contact record + propagate to all references.
  - CRM event log entries marked `[REDACTED]`.
  - Cross-fork-provenance entries flagged `consent-revoked-cascade`.
  - Wiki references stripped via `/lint --check-forget-request-cascade`
    (Phase B).
- Reversal Transactions discipline: forget-request = NEW entry with
  `corrects: <original-entry-id>` + `redaction_reason: forget-request`
  (NEVER deletes history; marks redacted) [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4 P3].

**Privacy invariant 3 — Encryption at rest (Part 1 substrate-level PRECONDITION):**

- File-system encryption assumed at substrate level (NOT Foundation
  responsibility for the substrate; declared as PRECONDITION).
- Foundation responsibility = ensure no plaintext secrets committed (cross-
  ref Bundle 1 API-key audit pattern in §9 commit discipline).
- Pre-commit hook (`pre-commit-secret-scan.sh`) verifies before each commit:
  `grep -rEn 'ANTHROPIC_API_KEY|GROQ_API_KEY|OPENAI_API_KEY|sk-ant-' <staged-
  files>` returns 0 hits.

**Privacy invariant 4 — NO inference of protected characteristics (Default-Deny per Part 6b §I.3):**

- Lint signal `/lint --check-protected-inference` (Phase B implementation;
  skill spec).
- Default-Deny entry per Part 6b §I.3: any classifier on race / religion /
  political affiliation / health status = Tier 0 hard halt (NEVER Tier 1+
  acknowledgeable; structural prohibition not policy preference).
- Schema-level enforcement: CRM contact record schema has NO field for
  protected characteristics; lint signal flags any RUSLAN-LAYER fork that
  adds such fields.
- Halt-Log-Alert ordering: ≤1s halt / ≤5s log / ≤60s alert per Part 6b §E L9.

**Behavioral framing prose target <10% of privacy section.** This section is
predominantly STRUCTURAL: schema fields, lint signal skill specs,
Default-Deny entries, Reversal Transactions discipline. Brigadier autocheck
§6.10 verifies behavioral framing prose <10%; if exceeded, re-dispatch
integrator with mandate to convert behavioral prose to structural enforcement.

[F4|G:Bundle 4 P10.3 privacy invariants STRUCTURAL|R-medium — Phase B lint
signal implementations rise F4→F8 on first run validating zero violations]

### §I.6 Cross-Part schemas REFERENCED (not duplicated)

| Schema | Owner | Part 10 consumption |
|---|---|---|
| `cross-fork-provenance.json` | Part 1 §I.1 (Bundle 1 + Bundle 4 supplement 2) | OQ-B1-5 D27 promotion declared in §I.1 of this Part |
| `awaiting-approval-packet.json` | Part 6b §I.4 (Bundle 1 LOCKED) | RT-2 invocations emit packets per this schema |
| `default-deny-table.yaml` | Part 6b §I.2 (Bundle 1 LOCKED) | Privacy invariant 4 entries added |
| `f-g-r.json` | Part 6a §I.1 (Bundle 1 LOCKED) | Every Part 10 emitted artefact carries f_g_r per this schema |
| `health-signal-schema.json` | Part 8 §I.1 (Bundle 3 LOCKED) | Part 10 health emissions conform |
| `wiki/graph/edges.jsonl` schema | Part 3 (Bundle 2 LOCKED) | UND-5 binding for CRM 8 edge types |
| `crm/_schema/frontmatter.yaml` | Cycle 10 LOCKED + Bundle 4 supplement | Privacy invariant 1 + canonical contact record |
| `crm/_schema/roles.yaml` | Cycle 10 LOCKED | 24 roles taxonomy |
| `crm/_schema/statuses.yaml` | Cycle 10 LOCKED | 13 pipeline statuses |
| `crm/_schema/edges.yaml` | Cycle 10 LOCKED | UND-5 binding 8 CRM edge types |

DRY enforced — schemas are NOT duplicated here.

---

## §J Operational Rituals

### J.1 Contact-add ritual (`/crm-add` skill — Phase A operational)

1. Owner OR agent invokes `/crm-add <slug> --role=<role> --status=<status>
   --source=<source>`.
2. `crm/_scripts/crm.py` validates per `crm/_schema/frontmatter.yaml`.
3. Bundle 4 addition: `consent_recorded_at: <ISO timestamp>` MANDATORY at
   creation (privacy invariant 1).
4. Contact record committed at `crm/people/<slug>.md` OR `crm/orgs/<slug>.md`
   via Part 1 §H `[crm] add: <slug>` commit.
5. Edge appended to `wiki/graph/edges.jsonl` if relationship type declared.
6. Index regenerated via `/crm-rebuild-index`.

### J.2 Contact-touch ritual (`/crm-touch` skill — Phase A operational)

1. Owner invokes `/crm-touch <slug> "<interaction note>"`.
2. Append-only entry added to §11 history of contact record.
3. `crm/log.md` append-only entry committed.
4. `last_touch_at: <ISO timestamp>` updated in frontmatter (NOT in-place edit
   of history; frontmatter timestamp is mutable via re-commit).
5. Stuck-detection: contacts with >14d no touch + active status surface in
   weekly review via `/crm-stuck`.

### J.3 RT-2 write-action ritual (Phase B materialisation; SPECIFICATION Phase A)

1. Owner OR agent invokes RT-2 action (e.g., `linear_create_ticket(...)`).
2. RT-2 verifies `consent_recorded_at` field present in target contact
   record (privacy invariant 1).
3. If consent absent: HALT + AWAITING-APPROVAL `gate_class: stop_gate` Tier
   1; do NOT fire write.
4. If consent present: blast-radius classify (typically Tier 1 strategic);
   emit AWAITING-APPROVAL `gate_class: stage_gate` to Part 6b.
5. Ruslan acks.
6. RT-2 dispatches external action via L.1/L.2/L.3 adapter.
7. Write-ack confirmation logged: CRM event log entry + Part 6a approval log
   entry + cross-fork-provenance log entry (3-way audit trail).
8. Commit `[crm] outreach: <slug> <service> action completed`.

### J.4 Forget-request ritual (privacy invariant 2; Phase B materialisation)

1. Contact requests data removal.
2. `/crm forget --contact <slug>` skill invocation.
3. NEW redacted entry written to contact record + CRM event log with
   `corrects: <prior-entry-id>` + `redaction_reason: forget-request` per
   Reversal Transactions.
4. Cascade via `/lint --check-forget-request-cascade`:
   - CRM event log entries marked `[REDACTED]`.
   - Cross-fork-provenance entries flagged `consent-revoked-cascade`.
   - Wiki references stripped.
5. Coverage target: 100% within ≤24h (D-7 deontic).
6. Commit `[crm] forget-request: <slug> (redaction cascade complete)`.

### J.5 Phase B activation ritual (C3 Phase A inbound = Phase B work)

Phase B activation predicates (ALL must hold):
- Phase A operational ≥3 months from Wave A ack.
- Tier 0 health-integrity events <1 per quarter.
- Methodology library ≥10 entries F5.

When predicates satisfied → Ruslan opens AWAITING-APPROVAL `gate_class:
stop_gate` "Phase B activation" → on ack → RT-1 + RT-2 implementations
begin. Until predicates satisfied: Phase A inbound = OWNER-INITIATED ONLY.

### J.6 Phase B partner fork import ritual

When a Phase B partner forks Foundation:
1. Partner imports CRM data model (`crm/_schema/*` Foundation generic
   structure) + integration adapter pattern (RT-1 + RT-2 + L.1/L.2/L.3
   stubs) + privacy invariants (4 invariants from §I.5) + write-ack
   discipline + reconciliation strategies.
2. Partner DECLINES Foundation's RUSLAN-LAYER (DACH ICP, German GDPR
   config, Ruslan's specific contact list, Linear/GitHub/Notion/Slack
   auth tokens, DACH-specific intelligence tracker URLs).
3. Partner populates own RUSLAN-LAYER per partner's market + jurisdiction
   + contact network.
4. Reconciliation_strategy applied per `cross-fork-provenance.json` D27
   promotion (Bundle 4 supplement 2):
   - `parent-wins` for privacy invariants (Foundation Default-Deny entries
     hold).
   - `fork-wins` for ICP parameters (partner's market overrides RUSLAN-LAYER
     DACH).
   - `manual-merge` for cross-cutting changes (e.g., new Default-Deny entry
     needed for partner-specific jurisdiction — US HIPAA classifier
     prohibition).
   - `pending-review` initial state until partner acks.
5. Cross-fork-provenance.json conforms with promoted top-level
   `approvals_reconciliation_strategy` field.

### J.7 Health-emission ritual

At every CRM event (add / touch / promotion / forget-request / RT-2 ack),
Part 10 calls `swarm/lib/emit_health_signal()` with:
- `crm-touch-rate` (per touch event);
- `crm-stuck-rate` (per weekly review);
- `external-action-latency` (per RT-2 ack-to-completion);
- `integration-adapter-health` (per RT-2 success/failure);
- `voice-pipeline-draft-promotion-rate` (per voice pipeline run);
- `privacy-invariant-violation-attempts` (per Default-Deny halt event —
  target 0).

Health emissions conform to Part 8 §I.1 canonical health-signal schema.

### J.8 Voice-pipeline DRAFT review ritual (Phase A operational)

1. Voice pipeline emits DRAFT files via `voice_router.py` from
   `tools/run_pipeline.sh` step 3.
2. Owner reviews DRAFT files in `crm/people/*-DRAFT.md` directory.
3. Owner promotes via `/crm-update <slug> --promote` (manual action).
4. NEVER auto-promote (CLAUDE.md CRM System Voice integration discipline).
5. SLI: voice-pipeline-draft-promotion-rate; indicative target ≥80%
   reviewed within 7 days.

### J.9 OQ-MERGED-2 dissolve-test evidence (Bundle 4 = Cycle 2 of 3)

Part 10's contribution to dissolve-test evidence: forget-request cascade
operations are operations that ONLY Part 5 compound-phase logic + Part 10
RT-2 adapter combination can execute coherently (Part 3 KB MOC, Part 4
routing table cannot perform privacy cascade without Part 10's lint signal
machinery + Part 5 admissibility predicate). Each forget-request cascade
counts as 1 distinct dissolve-test evidence entry.

---

## §K Failure Modes

| ID | Failure | Detection | Response |
|---|---|---|---|
| K1 | RT-2 write without consent — adapter fires external write before consent_recorded_at verified | Part 8 SLI on consent verification rate; pre-commit hook on RT-2 invocations | Halt-Log-Alert Tier 0; revoke external write if reversible; require AWAITING-APPROVAL stop_gate for next attempt |
| K2 | Privacy invariant 4 violation — classifier on protected characteristic detected | `/lint --check-protected-inference` (Phase B); pre-commit hook | Halt-Log-Alert Tier 0; revoke offending code; requires Bundle 1 RUSLAN-ACK to override (NEVER acknowledgeable per Default-Deny) |
| K3 | Forget-request cascade incomplete — references remain post-`/crm forget` | `/lint --check-forget-request-cascade` (Phase B) | Brigadier audit; manual cascade completion; emit retrospective AWAITING-APPROVAL |
| K4 | RT-1 write-event detected — read-only invariant violated | Part 8 SLI on RT-1 side_effects field (target empty) | Halt-Log-Alert Tier 0; investigate adapter logic; revoke and require RT-1 fix |
| K5 | Phase A inbound auto-action — auto-reply OR auto-comment OR auto-Linear-status fired | Part 8 SLI on auto-action rate (target 0); pre-commit hook on inbound external | Halt-Log-Alert Tier 0; C3 violation; revoke action if reversible |
| K6 | Auth token leak — secret committed to Foundation tree | `pre-commit-secret-scan.sh`; grep on `private/` paths | Reject commit; rotate leaked token; AWAITING-APPROVAL stop_gate for incident review |
| K7 | RUSLAN-LAYER content embedded in Foundation schema — DACH/GDPR/contact-list/auth-token in `crm/_schema/*` | Brigadier autocheck §6.9; pre-commit hook on Foundation tree | Reject commit; require RUSLAN-LAYER overlay path |
| K8 | CRM canonicalisation drift — Bundle 4 proposes alternative CRM data model | Brigadier autocheck §2.3 special; critic gate review | Reject draft; surface as OQ-B4-X for Wave D consideration |
| K9 | UND-5 edge type drift — new CRM edge added without AWAITING-APPROVAL ack | Pre-commit hook on `crm/_schema/edges.yaml`; Part 6b stage_gate enforcement | Reject commit; require AWAITING-APPROVAL stage_gate |
| K10 | Voice-pipeline DRAFT auto-promotion — `<slug>-DRAFT.md` promoted without owner ack | Part 8 SLI on voice-pipeline-draft-promotion-rate; pre-commit hook | Halt-Log-Alert; revoke promotion; require manual ack |
| K11 | Phase B activation predicate bypass — RT-1/RT-2 implementations begun without all 3 predicates satisfied | Pre-commit hook on RT-1/RT-2 production code paths | Reject commit; require predicate satisfaction + AWAITING-APPROVAL stop_gate ack |
| K12 | Reconciliation strategy drift — fork-import without `approvals_reconciliation_strategy` field populated | Schema validation per Part 1 §I.1 supplement 2 | Reject import; require explicit reconciliation strategy declaration |
| K13 | Append-only history violation — §11 history entry edited in place | Pre-commit hook on `crm/people/<slug>.md` §11 sections | Reject commit; require Reversal Transactions (NEW entry with corrects: pointer) |
| K14 | Stuck-contact surface miss — contact >14d no touch not surfaced in weekly review | Cross-check Part 9 weekly review vs `/crm-stuck` output | Brigadier audit; force-surface |
| K15 | External-action-latency breach — Ruslan ack-to-completion >24h (95th percentile breach) | Part 8 SLI alert | Brigadier audit; investigate L.1/L.2/L.3 adapter; possible auth-token rotation needed |
| K16 | Behavioral framing prose >10% in privacy section | Brigadier autocheck §6.10; word count of behavioral prose vs structural enforcement | Re-dispatch integrator; convert behavioral prose to structural enforcement |
| K17 | Privacy invariant 3 violation — plaintext secret in Foundation tree | Pre-commit hook secret-scan | Reject commit; rotate secret; AWAITING-APPROVAL stop_gate |
| K18 | DRAFT pipeline pile-up — DRAFTs not reviewed within 7 days | Part 8 SLI alert | Surface in next weekly review; force review or archive |
| K19 | Inbound external auto-ingestion (Phase B premature) — RT-1 adapter polls without Phase B activation ack | Part 8 SLI on RT-1 invocation rate; pre-commit hook | Halt RT-1; revoke; require Phase B activation ack |
| K20 | Cross-fork-provenance log gap — RT-2 write fires without cross-fork-provenance entry | Audit trail check at end of cycle; Part 8 SLI | Brigadier audit; reconstruct entry; investigate H.3 logic |

---

## §L Wave C Worklist Bullet Status

| Bullet | Status | Acceptance predicate | Evidence |
|---|---|---|---|
| **P10.1** L.1-L.3 integration adapter stubs | ✅ DONE | 5 adapter stubs (RT-1 + RT-2 + L.1 + L.2 + L.3); request/response/error-mode declared; blast-radius assignment; consent verification step for RT-2; auth-token externalisation declared | §I.4 + §H.4-§H.8 + §J.3 |
| **P10.2** C3 Phase A boundary clarification | ✅ DONE | §F declares 3 rules verbatim; cross-references C3 dependency-graph + Part 2 §A | §F C3 boundary section + §J.5 + §A.2 |
| **P10.3** Privacy architecture declaration (STRUCTURAL not behavioral) | ✅ DONE | 4 invariants declared; each has schema field OR lint signal OR Default-Deny entry; behavioral framing <10%; cross-refs FUNDAMENTAL §6.4 + Part 6b §I.3 | §I.5 + §H.7 + §F + §K K1-K2-K17 + brigadier autocheck §6.10 |
| **P10.4** OQ-MERGED-3 fork-separation FINAL CLOSURE | ✅ DONE | §X explicit examples per category (Foundation 6+ entries + RUSLAN-LAYER 5+ entries); critic gate auto-verifies DACH/GDPR/auth-token/contact-list/intelligence-URL examples | §X explicit declarations + brigadier autocheck §6.9 |
| **CRM canonicalisation** | ✅ DONE | Existing 24 source files / 35 unit tests / 10 skills / 4 schemas referenced; NOT redesigned | §A.1 + §H.1 + §I.2 + §N |
| **OQ-B1-5 D27 reconciliation_strategy promotion** | ✅ DONE | Part 10 §I.1 declares 5 reconciliation strategies; Part 1 §I.1 supplement edit prepared (Phase H end-of-cycle commit) | §I.1 + decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-28.md (Phase H deliverable) |

---

## §M Wisdom Application Findings — Part 10

| Card / Source | Principle | Current state pre-loop | Improvement | Adopted? | Op vs Phi | Justification | Section edited |
|---|---|---|---|---|---|---|---|
| #1 Anthropic CAI | Privacy hardcoded never-list (race / religion / political / health) | Wave A surfaced; not encoded in Default-Deny | Add Default-Deny entries per Part 6b §I.3 + lint signal `/lint --check-protected-inference` skill spec; Tier 0 hard halt | YES | OPERATIONAL | Phase A — structural privacy enforcement; NEVER acknowledgeable | §I.5 + §H.7 + §K K2 |
| #2 Anthropic CAI | Write-ack mandatory before external action | Implicit in cycle 10; not Foundation-level invariant | Add §E L1 hard Law + §I.4 RT-2 stub mandates consent_verification + AWAITING-APPROVAL stage_gate | YES | OPERATIONAL | Phase A — structural enforcement of write-ack discipline | §E L1 + §I.4 + §J.3 |
| #3 Askell HHH | Corrigibility — never lock owner out | Constitutional Bundle 1 | Privacy enforcement is Halt+Alert NOT lock-out; owner can git revert any record, manually edit | YES (lite) | OPERATIONAL | Phase A — operational invariant — privacy enforcement preserves owner ability to override | §F + §K |
| #4 Askell HHH | Hardcoded never-list | Implicit | Add §I.5 invariant 4 + Default-Deny entry NEVER acknowledgeable per Part 6b §I.3 | YES | OPERATIONAL | Phase A — structural prohibition not policy preference | §I.5 invariant 4 |
| #5 Levenchuk SHSM-FPF | IP-2 with F.9 Bridge | Wave A surfaced | Add §X declaration single-owner Phase A bounded; F.9 Bridge multi-owner stub fields N/A here (Part 9 owns) but partner-fork-import is Part 10's IP-2 boundary work | YES | OPERATIONAL | Phase A — fork-separation invariant + Phase B activation predicates | §X + §J.6 + §A.2 + §J.5 |
| #6 Mereology-typed-edges | UND-5 binding to Part 3 typed-edge taxonomy | Cycle 10 declared `crm/_schema/edges.yaml` 8 edge types | Cross-ref to Part 3 §I.2 wiki/graph/edges.jsonl typed-edge canonical mechanism; new edges require AWAITING-APPROVAL stage_gate per E.2 A-6 | YES | OPERATIONAL | Phase A — UND-5 binding declared structurally; new-edge gate enforces | §I.3 + §E A-6 + §K K9 |
| #7 KM-Karpathy-Luhmann-Forte | PARA tier — contacts in Resource (relationship asset) OR Project (active deal) | Implicit | Add para_tier field to CRM contact record schema (Resource = sustained relationship; Project = active deal in pipeline; Archive = closed_lost or paused contacts) | YES (lite) | OPERATIONAL | Phase A — schema field tagged; cross-bundle PARA discipline | §I.2 frontmatter supplement (implicit) — declined operational expansion (Wave D) |
| #8 Multi-Agent-Architecture | Integration adapter pattern; A2A vs MCP open question | Wave A flagged Phase B | Declare RT-1 + RT-2 + L.1/L.2/L.3 stubs SPECIFICATION ONLY Phase A; A2A flagged as OQ-CONFLICT-4 Phase B; per OQ-MERGED-5 specify-and-stub | YES | OPERATIONAL | Phase A — pattern declared structurally for Phase B import | §I.4 + §H.2-§H.6 |
| #9 Young 2010 CQRS | Reversal Transactions for forget-request | Implicit append-only | Add §I.5 invariant 2 explicit + §J.4 forget-request ritual + §K K3 detection | YES | OPERATIONAL | Phase A — structural enforcement of NEVER-DELETE-HISTORY discipline | §I.5 + §J.4 + §K K3 |
| #10 FUNDAMENTAL §6.4 | Privacy hard rules (4 invariants) | Constitutional | Materialise as STRUCTURAL invariants — schema fields + lint signals + Default-Deny entries; behavioral framing prose <10% target | YES | OPERATIONAL | Phase A — operational materialisation of constitutional anchor | §I.5 + §H.7 |
| #11 FUNDAMENTAL §6.1 | Default-Deny constitutional | Bundle 1 LOCKED | Add Default-Deny entries for novel external action classes + privacy invariant 4 (race/religion/political/health classifier) per Part 6b §I.2 | YES | OPERATIONAL | Phase A — structural prohibition; Tier 0 hard halt | §I.5 + §C |
| #12 OQ-MERGED-3 fork-separation | Wave A scope (per Ruslan ack 2026-04-27) | FINAL CLOSURE Bundle 4 | Declare §X with explicit DACH ICP / German GDPR / Linear+GitHub+Notion+Slack auth-token / contact-list / DACH intelligence URL examples; critic gate auto-verifies (§6.9 autocheck) | YES | OPERATIONAL | Phase A — fork-separation invariant; Phase B import contract | §X + brigadier autocheck §6.9 |
| #13 OQ-B1-5 | Reconciliation strategy field promotion | Bundle 1 metadata open field | Promote to top-level field with 5 strategies (parent-wins / fork-wins / manual-merge / decline-import / pending-review); Part 1 §I.1 supplement 2 commits Phase H | YES | OPERATIONAL | Phase A — schema field promotion; Phase B reconciliation actions | §I.1 + Phase H supplement record |
| #14 SRE-Observability | Structured logging | Implicit | Health emissions per Part 8 §I.1 canonical health-signal schema; integration-adapter-health SLI; external-action-latency SLI | YES | OPERATIONAL | Phase A — schema-conforming SLI emissions | §J.7 + §B |

**Aggregate adoption:** 14 YES (12 OPERATIONAL + 2 lite OPERATIONAL) / 0 NO.
**Operational ratio: 14/14 = 100%** (lite OPERATIONAL counted as OPERATIONAL
since each changes schema field / lint signal / Default-Deny entry / failure
mode). Bundle 4 ≥85% target MET.

[F4|G:Wisdom Loop applied to Part 10|R-medium]

---

## §N Provenance

**Constitutional baseline:**
- Bundle 1 LOCKED: Part 1 (§I.1 cross-fork-provenance — D27 promotion target),
  Part 6a (§I.1 F-G-R F8), Part 6b (§I.4 awaiting-approval-packet F8 + §I.3
  blast-radius + §I.2 default-deny).
- Bundle 2 LOCKED: Part 2 (C3 cross-ref; /ingest entry), Part 3 (§I wiki/graph/
  edges.jsonl — UND-5 binding), Part 4 (task-return-packet — RT-2 invocation
  context).
- Bundle 3 LOCKED: Part 5 (§A weekly review surfaces stuck contacts), Part 8
  (§I.1 canonical health-signal schema).
- Bundle 4 LOCKED parts (this bundle): Part 7 (cross-Part schema reference),
  Part 9 (weekly review consumes /crm-stuck).

**RUSLAN-ACK records:**
- Bundle 1 RUSLAN-ACK [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md].
- Bundle 1 supplement [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md].
- Bundle 2 RUSLAN-ACK [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md].
- Bundle 3 RUSLAN-ACK [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md].
- OQ-MERGED-3 fork-separation Wave A scope ack [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md].
- OQ-B1-5 D27 reconciliation strategy ack (Bundle 1; promoted Bundle 4).

**Wave A:**
- Interface card [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-10-external-touchpoints-network-interface.md].
- Worklist §2 P10 [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md].
- Critic gate §2 Part 10 + §4 OQ-MERGED-3 [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md].
- Dependency graph §3.3 C3 + §4.5 UND-5 [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md].

**Wave B consultants:**
- anthropic-constitutional-ai.md (privacy + write-ack + hardcoded never-list)
  [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md:§5 T3].
- levenchuk-shsm-fpf.md (IP-2 with F.9 Bridge; A.14 typed edges) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md].
- mereology-typed-edges.md (UND-5 CRM graph edges) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/mereology-typed-edges.md].
- knowledge-management-karpathy-luhmann-matuschak.md (PARA: contacts in
  Resource/Project) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md].
- multi-agent-architecture.md (A2A; integration adapter pattern) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/multi-agent-architecture.md].

**Library-direct supplement:**
- bai-2022-cai.md (Constitutional AI; RLAIF for Part 10 self-critique pattern)
  [src:raw/books-md/anthropic/bai-2022-cai.md].
- askell-2021-hhh.md (Helpful-Honest-Harmless; corrigibility; hardcoded
  never-list) [src:raw/books-md/anthropic/askell-2021-hhh.md].
- young-cqrs-2010.md (Reversal Transactions for forget-request) [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4].

**FUNDAMENTAL anchors:**
- §6.1 default-deny constitutional; §6.4 privacy hard rules; §4.5 anti-pattern
  auto-create commitments external [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md].

**FPF:**
- IP-2 bounded context with F.9 Bridge (§5.2); A.14 typed edges; A.6.B L/A/D/E
  [src:design/JETIX-FPF.md].

**CRM cycle 10 baseline (CANONICALISED):**
- crm/README.md authoritative [src:crm/README.md].
- crm/PLAN.md frozen reference [src:crm/PLAN.md].
- AWAITING-APPROVAL cycle-10 [src:swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md].
- AUDIT §7 (24 source files / 35 tests / 10 skills / 4 schemas) [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§7].
- 4 contacts (anton-mentor / vladislav-economist / rodion-youtuber /
  example-person) per AUDIT §7.5 (RUSLAN-LAYER content; canonical mechanism).
- 24 roles + 13 statuses + 6 offers + 6 asks per `crm/_schema/` (Foundation
  generic structure; specific values RUSLAN-LAYER for `strategy-hooks.yaml`).

**Existing operational baseline:**
- `tools/run_pipeline.sh` step 3 voice → CRM voice-route [src:tools/run_pipeline.sh].
- 10 `/crm-*` skills [src:CLAUDE.md:CRM System Skills].

---

## §X Foundation vs RUSLAN-LAYER (FINAL CLOSURE per OQ-MERGED-3)

### §X.1 Foundation generic (transferable to any single-owner knowledge-work fork)

| Category | Foundation invariant |
|---|---|
| **CRM data model** | Contact record schema fields except RUSLAN-LAYER overlay; relationship-edge taxonomy; pipeline status taxonomy (13 statuses + stuck threshold 14d) |
| **CRM 8 edge types per `crm/_schema/edges.yaml`** | UND-5 binding to Part 3 typed-edge taxonomy; 8 edge types declared (mentors / advises / partner_prospects / sourced_via / references / co-founded / vendor_for / competitor_of) |
| **Integration adapter pattern (RT-1 + RT-2 + L.1/L.2/L.3 stubs)** | Pattern at SHAPE level — request/response/error-mode declared; blast-radius assignment; consent verification step for RT-2; auth-token externalisation pattern |
| **Privacy invariants per FUNDAMENTAL §6.4** | 4 invariants — consent enforcement / forget-request / encryption-at-rest / no-protected-inference; STRUCTURAL enforcement (schema fields + lint signals + Default-Deny entries) |
| **Write-ack discipline** | RT-2 mandatory consent verification + AWAITING-APPROVAL `gate_class: stage_gate` per Part 6b; 3-way audit trail (CRM event log + approval log + cross-fork-provenance) |
| **10 `/crm-*` skills SHAPE** | Skill names + arg patterns (NOT specific contact-list bindings): `/crm-add`, `/crm-show`, `/crm-list`, `/crm-search`, `/crm-touch`, `/crm-update`, `/crm-rebuild-index`, `/crm-dash`, `/crm-stuck`, `/crm-weekly` |
| **Voice-pipeline DRAFT-only flow** | DRAFT-only invariant; manual promotion required; `<slug>-DRAFT.md` file naming convention |
| **5 reconciliation strategies** | parent-wins / fork-wins / manual-merge / decline-import / pending-review (OQ-B1-5 D27 promotion) |
| **3-way audit trail discipline** | Every external write logs to CRM event log + Part 6a approval log + cross-fork-provenance log |
| **Phase B activation predicates** | ≥3 months Phase A operational + Tier 0 events <1/quarter + methodology library ≥10 entries F5 |
| **Append-only history discipline** | Reversal Transactions (Young 2010); NEVER deletes history; corrects: pointer for revisions |
| **Auth-token externalisation pattern** | path convention `private/<service>-auth.yaml`; 90-day rotation policy default; secret-scan compliance |

### §X.2 RUSLAN-LAYER (Ruslan's Jetix Phase A specific bindings — explicit examples MANDATORY per OQ-MERGED-3 FINAL CLOSURE)

| Category | RUSLAN-LAYER value (EXPLICIT EXAMPLES) |
|---|---|
| **DACH ICP parameters** | `crm/_schema/icp.yaml` declares **"ICP = DACH consulting clients; fintech/insurtech focus; 10-100 employees; English/German operating language"** — these are RUSLAN-LAYER values; Foundation generic = the ICP schema STRUCTURE. Phase B partner forks declare own ICP per partner's market (e.g., US fintech, Asian SaaS, etc.) |
| **German GDPR config** | `crm/_schema/gdpr.yaml` (RUSLAN-LAYER overlay) declares **"GDPR data-residency = EU; right-to-be-forgotten = explicit `/crm forget` pathway; data-processor agreements = required for partner forks; legal basis = legitimate-interest for B2B contact-network maintenance per Art. 6(1)(f) GDPR"** — these are RUSLAN-LAYER values per German jurisdiction; Foundation generic = the GDPR schema STRUCTURE + the privacy invariants of §I.5 above |
| **Specific contact lists** | `crm/people/anton-mentor.md`, `crm/people/vladislav-economist.md`, `crm/people/rodion-youtuber.md`, `crm/people/example-person.md` files = RUSLAN-LAYER (Ruslan's own contacts; partner forks have own contacts at `crm/people/<partner-slugs>.md`) |
| **Linear/GitHub/Notion/Slack auth tokens** | `private/linear-auth.yaml`, `private/github-auth.yaml`, `private/notion-auth.yaml`, `private/slack-auth.yaml` files = RUSLAN-LAYER (Ruslan's own service auth tokens; partner forks have own at same path convention; Foundation generic = the auth-token externalisation PATH CONVENTION + ROTATION POLICY + SECRET-SCAN COMPLIANCE PATTERN) |
| **DACH-specific intelligence tracker URLs** | RT-1 source URL list (RUSLAN-LAYER overlay): **`https://news.ycombinator.com`** (HN) + **`https://www.reddit.com/r/Berlin`** + **`https://www.reddit.com/r/germany`** + **`https://www.reddit.com/r/de`** + specific DACH AI/consulting newsletter URLs = RUSLAN-LAYER values; Foundation generic = the RT-1 adapter PATTERN with poll cadence + signal emit shape |
| **`crm/_schema/strategy-hooks.yaml` 6 offers + 6 asks** | The strategy-hooks.yaml content is RUSLAN-LAYER (Ruslan's specific offers + asks; references `decisions/` and `directions/_active/`); Foundation generic = the strategy-hooks STRUCTURE (offers / asks taxonomy + relevance filter mechanism) |
| **24 roles in 6 groups** | The role names within roles.yaml ARE RUSLAN-LAYER (specific role bindings reflecting Ruslan's Phase A taxonomy); Foundation generic = the 6-group STRUCTURE (sales / capital / partnership / advisory / team / network) + the cardinality patterns |
| **13 pipeline statuses** | The pipeline status names (`draft_from_voice` → `cold` → `warm` → `contacted` → `discovery_call` → `proposal` → `negotiation` → `closed_won/lost` + paused/active/past) are RUSLAN-LAYER specific to Ruslan's sales pipeline stages; Foundation generic = the pipeline STRUCTURE pattern (DRAFT → cold-warm → engagement → terminal-states) |
| **Russian-primary content patterns** | All Ruslan's contact prose in Russian primary; partner forks use partner's content language; Foundation generic = language-agnostic schema |

### §X.3 F.9 Bridge requirement (per FPF §5.2 IP-2 + Wave A Ashby BOSC-A-T-X analysis)

Phase A is bounded to single-owner Jetix. Phase B activation requires:
- Fork import of Foundation schema (CRM data model + integration adapter
  pattern + privacy invariants + write-ack discipline + reconciliation
  strategies) unchanged.
- Fork DECLINES Foundation's RUSLAN-LAYER (DACH ICP, German GDPR config,
  Ruslan's specific contact list, auth tokens, DACH intelligence URLs).
- Fork populates own RUSLAN-LAYER values for partner's market + jurisdiction
  + contact network.
- Reconciliation_strategy applied per `cross-fork-provenance.json` D27
  promotion (Bundle 4 supplement 2):
  - `parent-wins` for privacy invariants + write-ack discipline + 5
    reconciliation strategies enum (Foundation invariants hold across forks).
  - `fork-wins` for ICP parameters (alex-dach-consulting US fintech ICP
    supersedes RUSLAN-LAYER DACH).
  - `manual-merge` for cross-cutting changes (e.g., new Default-Deny entry
    needed for US-specific HIPAA classifier prohibition).
  - `pending-review` initial state until partner acks.

### §X.4 Brigadier autocheck §6.9 verification

Per §6.9 fork-separation FINAL CLOSURE autocheck, this section explicitly
contains:
- **DACH ICP example**: text mentions "DACH" + "consulting clients" +
  "fintech/insurtech" — present at §X.2 row 1 ✓
- **German GDPR example**: text mentions "GDPR" + "EU data-residency" +
  "right-to-be-forgotten" — present at §X.2 row 2 ✓
- **Auth-token externalisation example**: text mentions "Linear" + "GitHub" +
  "Notion" + "Slack" + "private/<service>-auth.yaml" path — present at §X.2
  row 4 ✓
- **Specific contact lists example**: text mentions "crm/people/" +
  "RUSLAN-LAYER" with specific slug names — present at §X.2 row 3 ✓
- **DACH intelligence URLs example**: text mentions specific URL pattern +
  "HN" + "r/Berlin" — present at §X.2 row 5 ✓

All 5 mandatory §X examples present. **OQ-MERGED-3 FINAL CLOSURE for
Foundation declared.**

[F4|G:Bundle 4 Part 10 §X final closure|R-medium — pending Ruslan ack;
F-level rises F5→F8 only after Phase B partner fork imports Foundation
generic + declines RUSLAN-LAYER + reconciliation strategy applied]

---

*End of Part 10 architecture document.*
