---
title: Wave D Phase D-2 — Inter-Part Contract Verification Matrix
date: 2026-04-28
type: contracts-matrix
cycle: cyc-foundation-build-2026-04-28
wave: D
phase: D-2
F: F4
G: wave-d-contracts-matrix
R: refuted_if_silent_❌_edge_or_producer_consumer_disagree
gate: M-D-2
---

# Phase D-2 — Inter-Part Contract Verification Matrix

**Mandate.** For each typed A.14 edge declared in any §D Dependencies section
across the 10 Foundation parts, verify producer side emits what consumer side
expects. NO new edge types invented. Per-edge: ✅ verified / 🟡 stub-Phase-B /
❌ gap. **Pass threshold:** ≥95% verified; 0 silent ❌ gaps.

## §1 Inter-Part edge enumeration (Part-to-Part only; FPF/FUNDAMENTAL constraints
out-of-scope here)

Wave A `dependency-graph.md` + 10 §D Dependencies tables enumerated. Filtering for
inter-Part edges (Part X → Part Y where X,Y ∈ {1,2,3,4,5,6a,6b,7,8,9,10}).
Constraint edges to FPF / FUNDAMENTAL / external book sources (Singer 2019 / Young 2010
/ Anthropic CAI / Askell HHH / Meadows / Beer VSM / Ashby / SRE) are
constitutional-input edges, not inter-Part contracts; verified at Bundle 1-4 ack
time. Wave D verifies the inter-Part contract surface only.

## §2 Inter-Part contracts table (35 declared edges)

| # | Producer | Consumer | Edge type | Contract field(s) | Producer side | Consumer side | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Parts 2-10 | Part 1 | `operates-in` | git substrate; commit-format-tokens.json (4 tokens + [swarm-lib]+[health]+[methodology]) | All Parts 2-10 emit through §H commit interface | Part 1 §H provides interface; §I.2 declares tokens; K15+K18 failure modes preserve | ✅ |
| 2 | Part 2 | Part 3 | `PhaseOf information-lifecycle` | Triage draft → KB admit; STOP-gate boundary | Part 2 §B emits triage draft post-STOP | Part 3 §A admits; admissibility predicate gates; declared reciprocal in Part 3 §D | ✅ |
| 3 | Part 2 | Part 6b | `methodologically-uses` | STOP-gate as Part 6b instance; awaiting-approval-packet.json F8 conformance | Part 2 §I emits packets per F8 schema | Part 6b §I.1 owns enum + schema; gate_class accepted | ✅ |
| 4 | Part 2 | Part 6a | `methodologically-uses` | F-G-R per F8 schema on every promoted draft | Part 2 §G stamps F-level F1→F2→F4 | Part 6a §I.1 F8 schema validates; pre-promotion validator | ✅ |
| 5 | Part 2 | Part 3 | `methodologically-uses` (read-only) | wiki/index.md anchor lookup at ingest | Part 2 §H reads index | Part 3 §I.2 maintains index; accessor skills via swarm/lib/ | ✅ |
| 6 | Part 3 | Part 6a | `methodologically-uses` | F-G-R stamping at promotion; approval-log appends | Part 3 §C emits log entries on promotion | Part 6a §I.1 F8 schema + §C log schema | ✅ |
| 7 | Part 3 | Part 6b | `methodologically-uses` | gate_class: draft_promotion (entity); gate_class: stage_gate (swarm/lib/ pipeline mods) | Part 3 §H + §I emit packets | Part 6b §I.4 owns enum | ✅ |
| 8 | Part 5 | Part 3 | `creates` (methodology entries) | UND-2 — wiki/methodology/ entity-type; methodology-promotion-event.json | Part 5 §B emits promotion event + content | Part 3 §I.2 wiki/methodology/ entity-type owns; admits per predicate | ✅ |
| 9 | Part 4 | Part 5 | `creates` (task-return-packet) | UND-1 — task-return-packet.json F4 schema (Part 4 §I.1) | Part 4 §I.1 declares full schema; emits at cycle close | Part 5 §A.5 admits raw packets; DRR extraction parses outcome/decisions/unresolved fields | ✅ |
| 10 | Part 4 | Part 1 | `creates` | role-manifest, routing-table.yaml, message-schema, executor-binding.yaml committed via §H | Part 4 §I emits artefacts | Part 1 §H accepts via [swarm-lib] token | ✅ |
| 11 | Part 4 | Part 6b | `methodologically-uses` | Routing-table.yaml escalation_taxonomy → gate_class; routing modifications → AWAITING-APPROVAL | Part 4 §I.1 escalation field references | Part 6b §I.4 owns enum | ✅ |
| 12 | Part 4 | Part 6a | `methodologically-uses` | F-G-R per F8 schema; task-return-packet f_g_r field $refs | Part 4 §I.1 emits packet with f_g_r $ref | Part 6a §I.1 F8 schema | ✅ |
| 13 | Part 4 | Part 7 | `methodologically-uses` | project-lifecycle stage_gate semantics (cycle-close packets) | Part 4 §I.1 packet aggregation triggers | Part 7 §A consumes aggregation; activated → under-review event | ✅ |
| 14 | Part 5 | Part 1 | `creates` | DRR + methodology + dissolve-test evidence committed via §H + [methodology] token | Part 5 §B emits artefacts | Part 1 §H + §I.2 commit-format-tokens [methodology] | ✅ |
| 15 | Part 5 | Part 4 | `methodologically-uses` (cadence) | 40/10/40/10 ritual at Part 4 dispatch level; cycle-close → compound phase trigger | Part 5 §J ritual definition | Part 4 §J cadence; cycle-close event aligned | ✅ |
| 16 | Part 5 | Part 4 | `methodologically-uses` (schema as method) | Part 4 §I.1 task-return-packet.json read for DRR extraction | Part 5 §A.5 inputs; DRR parser code-path | Part 4 §I.1 schema F4 declared | ✅ |
| 17 | Part 5 | Part 6a | `methodologically-uses` (F-G-R + log) | F-G-R DOGFOOD; methodology-promotion-event log entries | Part 5 §C emits log entries | Part 6a §I.1 + §C | ✅ |
| 18 | Part 5 | Part 6b | `methodologically-uses` (gate) | gate_class: draft_promotion (methodology promotion gate) | Part 5 §B emits packet | Part 6b §I.4 owns enum | ✅ |
| 19 | Part 7 | Part 5 | `creates` (project-retrospective-packet) | UND-3 finalised — project-retrospective-packet.json (Part 7 §I.2 superset of task-return-packet) | Part 7 §B emits packet on closure | Part 5 §A.5 admits per stub contract; UND-3 finalisation Bundle 4 ack | ✅ |
| 20 | Part 7 | Part 6b | `methodologically-uses` | Stage-gate transitions invoke stage-gates.yaml predicates; gate_class: stage_gate packets | Part 7 §I emits | Part 6b §I.1 + §I.4 | ✅ |
| 21 | Part 7 | Part 4 | `methodologically-uses` | Cycle-close task-return-packet aggregation → activated→under-review event | Part 7 §A consumes aggregation | Part 4 §I.1 emits | ✅ |
| 22 | Part 7 | Part 1 | `derives-from` | All project artefacts via §H commit interface | Part 7 §C emits commits | Part 1 §H | ✅ |
| 23 | Part 7 | Part 6a | `methodologically-uses` | Stage-gate ack → approval-log; F-G-R per F8 | Part 7 §C emits log; §G F-G-R | Part 6a §I.1 + §C | ✅ |
| 24 | Part 7 | Part 8 | `derives-from` | Health emissions conform to canonical health-signal schema F5 (C2) | Part 7 §B emits SLI signals | Part 8 §I.1 schema F5 | ✅ |
| 25 | Part 8 | All 10 Parts | `operates-in` (VSM S3) | Beer VSM S3 audit context | Part 8 §C reads health from all parts | All Parts emit conformant signals; Part 8 §I.1 canonical schema | ✅ |
| 26 | Part 8 | Part 1 | `methodologically-uses` + `derives-from` (§J burn-rate; §B Four Golden Signals) | SLI/SLO schema CONSUMES Part 1 burn-rate algebra; Four Golden Signals | Part 8 §I.2 SLI/SLO references | Part 1 §J burn-rate; §B Four Golden Signals declared | ✅ |
| 27 | Part 8 | Part 6a | `methodologically-uses` (TRADEOFF-01 service invocation) | F-G-R compliance check primitive at quarterly cadence | Part 8 §C invokes; §J quarterly audit | Part 6a §J quarterly audit framework provides primitive | ✅ |
| 28 | Part 8 | Part 6b | `methodologically-uses` (alert routing) | Tier 0/1/2/3 blast-radius routing + Halt-Log-Alert L9 ordering | Part 8 §C emits alerts | Part 6b §I.2 blast-radius F8 + §E L9 F8 | ✅ |
| 29 | Part 8 | Part 5 | `derives-from` (health emissions) | compound-application-rate; methodology-promotion-rate; drr-write-rate; dissolve-test-evidence-count | Part 8 §I.1 SLI definitions | Part 5 §B emits SLI signals | ✅ |
| 30 | Part 8 | Parts 2/3/4 | `derives-from` (health emissions) | Bundle 2 emissions: triage-rate / KB-promotion-rate / coordination-latency | Part 8 §I.1 SLI definitions | Parts 2 §I.6 / 3 §I.6 / 4 §I.4 declare emissions | ✅ |
| 31 | Part 9 | Part 1 | `creates` | daily/weekly/monthly artefacts via §H | Part 9 §B emits artefacts | Part 1 §H | ✅ |
| 32 | Part 9 | Part 6b | `methodologically-uses` | accept-dispositioned drafts → draft_promotion gate | Part 9 §C + §I.4 emit | Part 6b §I.4 enum | ✅ |
| 33 | Part 9 | Part 6a | `methodologically-uses` | F-G-R per F8; approval-log per §C | Part 9 §G emits | Part 6a §I.1 + §C | ✅ |
| 34 | Part 9 | Part 5 | `methodologically-uses` | Weekly review surfaces methodology candidates from agents/<id>/strategies.md; monthly reflection feeds Part 5 input | Part 9 §B emits surface | Part 5 §A admits surface | ✅ |
| 35 | Part 9 | Part 8 | `operates-in` (owner reflection data as health signals) | attention-budget utilisation; daily-log creation rate; weekly review completion rate | Part 9 §B emits signals | Part 8 §I.1 SLI definitions consume | ✅ |
| 36 | Part 9 | Part 7 | `methodologically-uses` | Weekly review consumes project-status updates + project-retrospective-packets | Part 9 §A admits | Part 7 §B emits status + retrospective per UND-3 | ✅ |
| 37 | Part 9 | Part 4 | `methodologically-uses` | Cycle dispatch context surfaces in afternoon execution section of daily-log | Part 9 §I.1 daily-log schema | Part 4 §I.1 dispatch context | ✅ |
| 38 | Part 9 | Part 8 | `derives-from` (Bundle 4 binding) | Part 9 weekly review CONSUMES Part 8 weekly health dashboard | Part 9 §A admits | Part 8 §B emits dashboard | ✅ |
| 39 | Part 10 | Part 3 | `methodologically-uses` (UND-5 binding) | CRM 8 edge types per crm/_schema/edges.yaml conform to wiki/graph/edges.jsonl typed-edge taxonomy | Part 10 §I declares CRM subset | Part 3 §I.2 wiki/graph/edges.jsonl owns canonical | ✅ |
| 40 | Part 10 | Part 6b | `methodologically-uses` | RT-2 write-ack stage_gate; Default-Deny for novel external action classes | Part 10 §I.4 emits | Part 6b §I.3 Default-Deny F8 + §I.4 enum | ✅ |
| 41 | Part 10 | Part 2 | `methodologically-uses` (C3) | Phase A inbound = owner-initiated /ingest only; Phase B inbound external = Part 10 territory | Part 10 §F declares Phase A boundary | Part 2 §A admits /ingest signals | ✅ |
| 42 | Part 10 | Part 1 | `methodologically-uses` + `creates` | Cross-fork-provenance entries; CRM events committed | Part 10 §C emits | Part 1 §H + §I.1 cross-fork-provenance.json v1.1.0 | ✅ |
| 43 | Part 10 | Part 6a | `methodologically-uses` | F-G-R per F8; approval-log per §C on each RT-2 ack | Part 10 §G emits | Part 6a §I.1 + §C | ✅ |
| 44 | Part 10 | Part 8 | `derives-from` (health emissions) | Health emissions per F5 canonical schema | Part 10 §I emits health signals | Part 8 §I.1 schema F5 | ✅ |
| 45 | Part 10 | Part 9 | `methodologically-uses` | Weekly review surfaces stuck contacts via /crm-stuck (per AUDIT §7.6) | Part 10 §J.2 emits | Part 9 §B weekly-review.json admits | ✅ |
| 46 | Part 6a | Part 6 cluster | `MemberOf` | Sub-Part composition | Part 6a self-declaration | Part 6 cluster context | ✅ |
| 47 | Part 6a | Part 1 | `methodologically-uses` | Approval log appends through git commit; scanner results surfaced via git-tracked artefacts | Part 6a §C emits | Part 1 §H | ✅ |
| 48 | Part 6a | Part 6b | `methodologically-uses` (real-time gate triggers tagging) | Part 6a defines schema; Part 6b applies at promotion time | Part 6a §I.1 schema | Part 6b §H invokes tagging | ✅ |
| 49 | Part 6b | Part 6a | `methodologically-uses` (consume F-G-R compliance signals) | Part 6b consumes Part 6a's f-g-r.json $ref for f_g_r_delta field | Part 6a §I.1 owns | Part 6b §I.1 awaiting-approval-packet $refs | ✅ |
| 50 | Part 6a | Part 6b | (edge 10 in Part 6a §D) — gate-class taxonomy reference | Part 6a approval-log records gate_class string value from Part 6b enum | Part 6a §C records value | Part 6b §I.4 owns enum | 🟡 EDGE-TYPE-WATCH (uses non-canonical "references"; engineering FINDING-2 watch item) |
| 51 | Part 6b | Part 6 cluster | `MemberOf` | Sub-Part composition | Part 6b self-declaration | Part 6 cluster context | ✅ |
| 52 | Part 6b | Part 1 | `methodologically-uses` | Canonical promotions via git commit; LOCKED tag application; audit log appends | Part 6b §C emits | Part 1 §H | ✅ |
| 53 | Part 7 | Part 6b | `methodologically-uses` (per-project stage gates) | Already counted as #20 | — | — | (dup-of-20) |
| 54 | Part 8 | Part 6b | `methodologically-uses` | Already counted as #28 | — | — | (dup-of-28) |
| 55 | Part 8 | Part 6a | `methodologically-uses` | Already counted as #27 | — | — | (dup-of-27) |

**Deduplication.** Edges 53/54/55 above are reciprocal references to edges already
counted from the producer side. Total unique inter-Part edges: **52** (entries 1-52
in the table; 50 edges with verdict ✅ + 1 edge ✅ DOGFOOD-cluster + 1 edge 🟡
EDGE-TYPE-WATCH).

## §3 Verdict counts

- ✅ verified: **51 / 52** = 98.1%
- 🟡 stub / watch-item: **1 / 52** (edge 50: Part 6a edge 10 uses non-canonical "references")
- ❌ silent gap: **0**

**Pass M-D-2:** ≥95% verified (actual 98.1%); 0 silent gaps. **PASS.**

## §4 The 1 🟡 watch item — edge 50 detail

**Issue.** Part 6a §D edge 10 declares `Part 6a approval-log references Part 6b
gate-class taxonomy` using edge type `references` (lightweight value-coupling).
This edge type is NOT in the canonical 10-edge A.14 taxonomy (`ComponentOf` /
`ConstituentOf` / `PortionOf` / `PhaseOf` / `MemberOf` / `AspectOf` / `creates` /
`operates-in` / `methodologically-uses` / `constrained-by` / `derives-from`).

**Origin.** Engineering-expert FINDING-2 (Bundle 1) identified the gate-class
coupling as implicit in the design and recommended explicit declaration.
Mgmt-expert §J.1 confirmed the watch item.

**Why not promote to canonical edge type.** The coupling IS lightweight
value-coupling (one-directional string-value reference; consumer doesn't break
when producer adds a new enum value). The closest canonical type would be
`methodologically-uses` (Part 6a uses Part 6b's enum as a method for value-
recording), but the semantics differ: standard `methodologically-uses` implies
the consumer is invoking the producer's METHOD; here Part 6a only stores a
string value Part 6b emitted, not invoking Part 6b's gate logic.

**Honest gap declaration.** The edge type "references" is informal and not
F8-LOCKED. **Routing options:**
- (a) Phase B operational — formalise "references" as a recognised lightweight
  edge type in mereology-typed-edges.md (extension of A.14 canon).
- (b) Wave D-8 retroactive supplement — promote `references` to canonical or
  re-classify as `methodologically-uses` with caveat.
- (c) Wave E ack-time decision — Ruslan decides whether to extend A.14
  taxonomy or retain informal usage.

**Recommended routing:** (c) Wave E ack-time decision — surface in AWAITING-APPROVAL
packet §4. The integration coherence is NOT blocked by this watch item: the
coupling works; the edge type label is the only formality at issue.

**Flag as `OQ-WAVE-D-EDGE-TYPE-50`** in D-5 OQ catalogue.

## §5 Inter-Part contract integrity findings

### §5.1 UND-1 BINDING (Part 4 → Part 5 task-return-packet)

**Verified.** Part 4 §I.1 declares full task-return-packet.json schema F4
(LOCKED at Bundle 2 ack). Part 5 §A.5 admits raw packets; DRR extraction parses
`outcome` / `decisions[]` / `unresolved` fields. Producer side schema =
Consumer side parser. **PASS.**

### §5.2 UND-3 FINALISED (Part 7 → Part 5 project-retrospective-packet)

**Verified.** Part 7 §I.2 declares project-retrospective-packet.json (UND-3
finalised at Bundle 4 ack as superset of task-return-packet — Bundle 4 ack
§5.1). Part 5 §A.5 admits per stub contract; M5 lite coherence PASS at
Bundle 4 ack. Producer side schema = Consumer side parser.
**PASS.** (Bundle 4 M5 PASS confirmed previously; Wave D inherits.)

### §5.3 UND-5 BINDING (Part 10 → Part 3 CRM 8 edge types ↔ wiki/graph/edges.jsonl)

**Verified.** Part 10 §I declares CRM 8 edge types per `crm/_schema/edges.yaml`.
Part 3 §I.2 declares wiki/graph/edges.jsonl typed-edge taxonomy as canonical
mechanism. CRM 8 edge types subset conforms to A.14 canonical taxonomy.
**PASS.**

### §5.4 C1 Joint Design Variant A (swarm/lib/ accessor pipeline)

**Verified.** Part 3 §D declares `operates-in swarm/lib/`; Part 4 §D declares
`operates-in swarm/lib/`. C1 Joint Design at Bundle 2 ack: Part 3 LEAD; Part 4
ADVISORY; shared infra under `swarm/lib/`. Both Parts §D entries align.
**PASS.**

### §5.5 C2 canonical health-signal schema F5 (Part 8 owns; Parts 2/3/4/5/7/9/10 emit)

**Verified.** Part 8 §I.1 declares canonical health-signal schema F5. Parts 2
§I.6 / Part 3 §I.6 / Part 4 §I.4 / Part 5 §B / Part 7 §B / Part 9 §B / Part 10 §I
emit conformant. **PASS** (Bundle 3 ack §5.2; Bundle 4 ack §5.6).

### §5.6 F-G-R F8 (Part 6a owns; ALL parts emit)

**Verified across all 10 parts.** Per D-1 CC-1 row. **PASS.**

### §5.7 AWAITING-APPROVAL packet F8 (Part 6b owns; ALL parts emit)

**Verified across all 10 parts.** Per D-1 CC-2 row + edges 3/7/11/18/20/32/40/48/49.
**PASS.**

### §5.8 cross-fork-provenance.json v1.1.0 (Part 1 owns; Part 10 references)

**Verified.** Part 1 §I.1 v1.1.0 with `approvals_reconciliation_strategy`
top-level field + 5 strategies enum (LOCKED at Bundle 1 supplement-2 ack).
Part 10 §I.1 declares 5 reconciliation strategies aligned. **PASS** (Bundle 4
M5 lite coherence + Bundle 1 supplement-2 ack §6.4 OQ-B1-5 D27).

### §5.9 message schema v2.0.0 with `acting_as:` (Part 4 owns; Bundle 4 messages conform)

**Verified.** Part 4 §H declares message schema v2.0.0. Bundle 4 Parts 7/9/10
emit messages with `acting_as:` field. **PASS** (Bundle 2 ack §5.4).

### §5.10 methodology-promotion-event.json (Part 5 §I.1; Part 9 weekly-review surfaces)

**Verified.** Part 5 §I.1 declares schema F5. Part 9 §B weekly-review surfaces
methodology promotion candidates from `agents/<id>/strategies.md`. Edge 34.
**PASS.**

### §5.11 PARA-tier mandatory (Part 2 origin; Parts 9/10 inherit; Bundle 2 P2.2)

**Verified.** Part 2 §I declares PARA-tier as mandatory frontmatter field.
Part 9 §C declares PARA-tier on every artefact (daily-log = Area; weekly-review
= Area; monthly-reflection = Resource). Part 10 CRM canonicalisation respects
PARA-tier per crm/_schema/. **PASS.**

### §5.12 Halt-Log-Alert L9 F8 (Part 6b owns; Part 8 alerts cannot bypass)

**Verified.** Part 6b §E L9 F8 LOCKED. Part 8 §D `constrained-by Part 6b §E
L9` — alert ordering ≤1s halt / ≤5s log / ≤60s alert. **PASS.**

## §6 M-D-2 Gate verdict

- [x] All 52 inter-Part edges enumerated from §D Dependencies tables
- [x] For each edge: producer Part identified; consumer Part identified
- [x] For each edge: contract fields documented
- [x] 51/52 ✅ verified; 1/52 🟡 watch-item (edge 50, edge-type label informal)
- [x] 0 silent ❌ gaps

**Pass threshold:** ≥95% verified (actual 98.1%); 0 silent gaps. **PASS.**

## §7 Routing of 🟡 watch-item

| Edge | Watch | Routing |
|---|---|---|
| 50 (Part 6a → Part 6b gate-class taxonomy) | Edge type `references` not in canonical 10-edge A.14 taxonomy | Wave E ack-time decision: extend A.14 OR re-label `methodologically-uses` (with caveat) OR formalise `references` as recognised lightweight edge type. Surfaced as OQ-WAVE-D-EDGE-TYPE-50 in D-5 catalogue. |
