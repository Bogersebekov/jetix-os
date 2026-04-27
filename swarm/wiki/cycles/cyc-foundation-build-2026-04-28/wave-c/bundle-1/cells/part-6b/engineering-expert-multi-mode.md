---
title: Part 6b — engineering-expert multi-mode cell (scalability + clean-code + critic)
date: 2026-04-28
phase: C-1-cell
expert: engineering-expert
modes: [scalability, clean-code, critic]
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 6b
F: F4
ClaimScope:
  holds_when: "Part 6 interface card (wave-a) read; FUNDAMENTAL §6.1 + §4.6 + §6.7 LOCKED v1.0; mgmt-expert and philosophy-expert cells for Part 6b read; clean-code consultant card §4 P1-P3 and event-sourcing-cqrs §3-§4 and sre-observability §3-§4 read; Part 6a architecture §H-§I read; Part 1 architecture read; sg-banned-phrases.yaml current at 2026-04-28"
  not_valid_when: "FUNDAMENTAL §6 revised post-2026-04-27; OR Part 6b schema definitions change after human gate ack; OR sg-banned-phrases.yaml expanded beyond 40 entries in a way that makes the banned-phrase-as-hamel-check verdict change"
R:
  refuted_if: "gate_class enum is defined independently in >1 of the 5 Part 6b schemas with divergent values; OR blast-radius tier definitions are copied (not referenced) in >1 schema; OR at 500 packets/week the single gate execution path saturates Ruslan's ack capacity with no Tier 2/3 routing"
  accepted_if: "gate_class enum is defined once (in awaiting-approval-packet.json) and all other schemas reference it via JSON Schema $ref; blast-radius tiers defined once in blast-radius-table.yaml; Tier 1/2/3 routing table is machine-readable and enforced at packet submission time"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md (lines 300-360)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6b/mgmt-expert-multi-mode.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-6b/philosophy-expert-multi-mode.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/clean-code.md (§4 P1-P3)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/event-sourcing-cqrs.md (§3 Source 2, §4 P1)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md (§3 Source 1/5, §4 P1/P6)
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md (§H-§I)
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md (§0)
  - .claude/config/sg-banned-phrases.yaml
---

# Part 6b — Engineering-Expert Multi-Mode Cell (Scalability + Clean-Code + Critic)

**Mode sequence:** clean-code → critic → scalability
**Scope:** Part 6b Human Gate — schema architecture (5 schemas + f-g-r.json DRY), config architecture (Foundation vs RUSLAN-LAYER pattern), Phase B/C/D scale stress test, and Ousterhout deep-module gate primitive analysis.

> **Self-exemplification.** Every claim in this cell carries a `[src:path:section]` reference with a concrete consequence within 200 characters. Foundation/RUSLAN-LAYER split is explicit throughout. All typed edges are A.14 compliant. F-G-R tags promoted claims.
> [src:part-6-governance-provenance-human-gate.md:§E "l_a_d_e_self_exemplifies"]

---

## §1 Schema Architecture (Clean-Code Mode)

### §1.1 DRY Audit — gate_class Enum Across 5 Schemas

**The problem.** `gate_class` is the central classification field for every Part 6b gate event. Per the mgmt-expert cell, `gate_class` takes enum values `[stop_gate, stage_gate, draft_promotion]` and is the UND-4 binding. [src:mgmt-expert-multi-mode.md:§7 A4 "gate_class field present with value in enum"] This field is consumed by:

1. `awaiting-approval-packet.json` — primary packet schema
2. `stage-gates.yaml` — predicate registry (stage-gate gate_class)
3. `default-deny-table.yaml` — classifier entries reference gate_class for escalation routing
4. Part 6a `swarm/approvals/log.jsonl` — approval log entries carry gate_class per event
5. Part 1 commit provenance — commit messages reference gate events

**DRY verdict.** Hunt-Thomas P3 (Pragmatic Programmer): "EVERY PIECE OF KNOWLEDGE MUST HAVE A SINGLE, UNAMBIGUOUS, AUTHORITATIVE REPRESENTATION WITHIN A SYSTEM." [src:clean-code.md:§4 P3] The `gate_class` enum is a piece of knowledge. If it is defined independently in each of the 5 schemas, every change to the enum requires 5 updates — a DRY violation that grows proportionally with schema count at Phase B/C scale.

**Recommendation: canonical definition in `awaiting-approval-packet.json`, JSON Schema `$ref` elsewhere.**

```
awaiting-approval-packet.json:
  definitions:
    gate_class_enum:
      type: string
      enum: [stop_gate, stage_gate, draft_promotion]
      description: "Canonical enum for gate classification per UND-4"

stage-gates.yaml:
  # $ref: shared/schemas/awaiting-approval-packet.json#/definitions/gate_class_enum
  # DO NOT redefine — consume by reference only

default-deny-table.yaml:
  # blast_radius_tier escalation entries reference gate_class_enum by value only
  # no redefinition of enum values
```

**F-G-R tag:**
- F: F5 — codified in Hunt-Thomas Ch.2 DRY principle; applied across 10+ systems
- ClaimScope: holds for all 5 Part 6b schemas and Part 6a log schema; weakens if the 5 schemas are deployed in separate process boundaries that cannot share a schema registry
- R: refuted_if "a gate_class value appears in stage-gates.yaml with spelling or casing divergent from awaiting-approval-packet.json definition"; accepted_if "grep for 'stage_gate|stop_gate|draft_promotion' across all 5 schema files shows zero independent enum declarations outside awaiting-approval-packet.json"

### §1.2 JSON Schema $ref Discipline — f-g-r.json Coupling

Part 6a's canonical contribution is the F-G-R schema at `shared/schemas/f-g-r.json` (Part 6a architecture §H declares this as Part 6a's primary schema output). [src:part-6a-provenance-officer/architecture.md:§H "F-G-R schema at shared/schemas/f-g-r.json"] Part 6b's `awaiting-approval-packet.json` references F-G-R for the `f_g_r_delta` field (the F-G-R snapshot captured at gate time per Part 6 §B Outputs "F-G-R snapshot at gate time"). [src:part-6-governance-provenance-human-gate.md:§B "F-G-R snapshot"]

**$ref discipline rule:** `awaiting-approval-packet.json` MUST reference `f-g-r.json` via `$ref`, not by copying F-G-R field definitions inline. Copying is the DRY violation that causes the two schemas to drift as F-G-R evolves (e.g., when Phase B adds an `F_decay_date` field to f-g-r.json, inline copies in awaiting-approval-packet.json do not inherit the field automatically).

**One-way dependency is structurally correct.** Part 6b consumes Part 6a's F-G-R schema; it does not own it. The typed edge is `methodologically-uses` (Part 6b → Part 6a), confirmed in mgmt-expert §6 D row 3. [src:mgmt-expert-multi-mode.md:§6 "Part 6b methodologically-uses Part 6a"] This is Ousterhout's orthogonality principle: changing Part 6a's F-G-R schema should not require changes to Part 6b's gate logic, only to the packet capture field. [src:clean-code.md:§4 P4 Orthogonality]

**Acyclicity check — dependency graph among 6 schemas:**

```
f-g-r.json          ← (no dependencies)
blast-radius-table.yaml  ← (no schema dependencies)
default-deny-table.yaml  → blast-radius-table.yaml (references tier values)
awaiting-approval-packet.json → f-g-r.json, blast-radius-table.yaml (references tier enum)
stage-gates.yaml    → awaiting-approval-packet.json (references gate_class enum via $ref)
escalation-taxonomy.yaml → blast-radius-table.yaml (references tier structure)
```

Graph is acyclic — CONFIRMED. No schema references a downstream consumer. This is the correct dependency direction. [src:clean-code.md:§4 P1 Deep Modules — modules depend on abstractions, not on their own consumers]

**CRITIC FINDING ENG-1 (DRY violation risk):** If `blast-radius-table.yaml` tier definitions (Tier-0/1/2/3) are copied into `awaiting-approval-packet.json` and `escalation-taxonomy.yaml` rather than referenced, the system has 3 independent representations of the same tier structure. At Phase B, when a new tier is added (e.g., Tier-4 for multi-party cross-fork decisions), all 3 must be updated in sync. This is the Hunt-Thomas knowledge-duplication failure mode. Mitigation: declare tier enum in `blast-radius-table.yaml` as the canonical tier source; other schemas reference tier values by the declared enum identifiers, not by re-enumerating them.

### §1.3 Schema Versioning — Version History Block on All 5 Schemas

Per the investor-expert finding on Part 1 (cited in Part 1 architecture §0): schema versioning is required for Phase B partner fork compatibility via D27 cross-fork-provenance. [src:part-1-system-state-persistence/architecture.md:§0 "D27 fork-and-merge"]

**Required frontmatter block on every Part 6b schema:**

```yaml
schema_version: "1.0.0"
schema_version_history:
  - version: "1.0.0"
    date: 2026-04-28
    changes: initial Wave C materialisation
    breaking: false
compatibility:
  min_consumer_version: "1.0.0"
  max_backward_compatible_version: "1.0.0"
```

**Phase B fork implication:** When a Phase B partner forks the Foundation, their instance imports the 5 Part 6b schemas. If the canonical schemas advance to v1.1.0 (non-breaking addition of `advisory_cai_flag` field per mgmt-expert BA-2 action 3 [src:mgmt-expert-multi-mode.md:§2 BA-2 "advisory_cai_flag"]), the fork can detect version mismatch and decide whether to adopt the new field. Without the version block, forks cannot detect drift silently. Young 2010 Reversal Transactions analogy: [src:event-sourcing-cqrs.md:§3 Source 2 "There is no Delete"] — you cannot correct drift you cannot detect.

**F-G-R tag:**
- F: F4 — operational convention; applied in AWS CloudFormation, OpenAPI 3.x, and JSON Schema draft specs; not yet validated in Jetix cycles
- ClaimScope: holds for all 5 Part 6b schemas; essential for D27 fork contract per Part 1 §0
- R: refuted_if "Phase B partner fork imports Part 6b schemas without version mismatch and operates correctly without version tracking"; accepted_if "first D27 fork instance reads schema_version field to validate compatibility before import"

### §1.4 Hamel-Binary YAML for stage-gates.yaml

Wave C worklist Bullet 2 (line 328) requires: "Hamel-binary acceptance predicate: every novel action classification query against the table returns a J-level authority assignment or Default-Deny within one lookup — no open-ended interpretation path." [src:wave-c-worklist.md:line 328]

**YAML design requirement.** `stage-gates.yaml` must use boolean flags and enum values, not prose predicate fields. The `sg-banned-phrases.yaml` check (18 entries, all targeting unfalsifiable prose patterns like "when ready", "if meaningful", "good enough") [src:.claude/config/sg-banned-phrases.yaml:banned_phrases] must be runnable against every predicate string in `stage-gates.yaml` at lint time.

**Compliant schema pattern:**

```yaml
# CORRECT — Hamel-binary stage gate entry
- gate_id: SG-P6b-001
  gate_class: stage_gate
  predicate:
    field: "swarm/approvals/log.jsonl"
    condition: "count(entries where cycle_id == current AND gate_class == 'stage_gate') >= 1"
    result_type: boolean
  blast_radius_tier: 1
  reversible: true
  human_ack_required: true

# INCORRECT — prose predicate (sg-banned-phrases.yaml would flag 'when ready')
- gate_id: SG-P6b-002
  predicate: "when ready for promotion"   # FAILS check: 'when\s+ready' banned phrase
```

**CRITIC FINDING ENG-2 (Hamel-binary gap):** The `/lint --validate-predicate` subcommand must run `sg-banned-phrases.yaml` checks against every `predicate:` string in `stage-gates.yaml`. Currently, `sg-banned-phrases.yaml` is applied to AWAITING-APPROVAL packet predicates (per mgmt-expert §7 A2: "acceptance predicate is Hamel-binary — not banned-phrase per sg-banned-phrases.yaml"). [src:mgmt-expert-multi-mode.md:§7 A2] The same check must extend to `stage-gates.yaml` entries. Gap: `/lint --check-stage-gates` does not yet run banned-phrase validation against the stage-gates predicates themselves. This is a lint scope gap, not a constitutional gap.

---

## §2 Config Architecture (Clean-Code Mode, continued)

### §2.1 Foundation vs RUSLAN-LAYER YAML Pattern

**The requirement.** Each of the 3 config files (P6b.2 `default-deny-table.yaml`, P6b.3 `blast-radius-table.yaml`, P6b.5 `escalation-taxonomy.yaml`) must be importable by a Phase B partner fork without importing Jetix-specific instance choices. Philosophy-expert §C.5 declares the framework-level / RUSLAN-LAYER split explicitly. [src:philosophy-expert-multi-mode.md:§C.5 "fork_importability"]

**Recommended two-section structure per config file:**

```yaml
# default-deny-table.yaml

foundation_generic:
  # These entries are structurally invariant across ALL Jetix Foundation instances.
  # A Phase B fork imports this section unchanged.
  default_policy: deny_and_escalate        # enum: deny_and_escalate | allow_with_log
  uncategorized_action_policy: deny        # FUNDAMENTAL §6.1 last bullet — not relaxable
  constitutional_never_list:               # machine-readable encoding of FUNDAMENTAL §6.1
    - action_class: strategize             # rule 1: AI НЕ принимают strategic decisions
      enforcement: halt_log_alert
      grade: F8                            # structural invariant
    - action_class: architectural_decision # rule 2: AI НЕ принимают architectural decisions
      enforcement: halt_log_alert
      grade: F8
    # ... (rules 3-11 encoded analogously)
  whitelisted_classes_foundation:
    - action_class: append_to_drafts_dir
      blast_radius_tier: 3
      reversible: true
      auto_execute: true

ruslan_layer_overrides:
  # These entries are JETIX-INSTANCE-SPECIFIC.
  # A Phase B fork REPLACES this section with its own whitelisted_classes and overrides.
  # DO NOT merge RUSLAN-LAYER entries into foundation_generic without HITL ack + AWAITING-APPROVAL.
  instance_id: jetix-phase-a-single-owner
  decision_authority_principal: ruslan    # RUSLAN-LAYER: specific person name
  whitelisted_classes_instance:
    - action_class: crm_touch_operation
      blast_radius_tier: 3
      reversible: true
      auto_execute: true
      rationale: "DACH-specific CRM update patterns; low-blast; reversible via git revert"
```

**Why this matters for scale.** At Phase C (500 packets/week, multi-fork), the `foundation_generic` block is the shared contract. Fork instances override `ruslan_layer_overrides` with their own authority principal and their own whitelist. Without the two-section split, a fork that differs on one whitelist entry must fork the entire file, losing provenance linkage to the canonical Foundation. With the split, forks carry `foundation_generic` by reference and own their `ruslan_layer_overrides` independently. This is exactly Ousterhout orthogonality applied to config files. [src:clean-code.md:§4 P4]

**Constitutional never-list as machine-readable enum.** Philosophy-expert §C.1 (encoding audit) validates that all 11 FUNDAMENTAL §6.1 rules have structural enforcement mechanisms. [src:philosophy-expert-multi-mode.md:§C.1 "11 rules structural encoding stress test"] The engineering complement: those 11 rules must appear as machine-readable enum entries in `default-deny-table.yaml`'s `constitutional_never_list` section, not as prose comments. A lint check can verify that the never-list has exactly 11 entries. This closes the gap between philosophical validation (philosophy-expert) and operational enforcement (this cell). [src:clean-code.md:§4 P5 "Essential vs Accidental" — the never-list enforcement IS essential complexity; do not optimize it away]

**F-G-R tag for Foundation/RUSLAN-LAYER split pattern:**
- F: F5 — codified; applied in Anthropic Constitutional AI principle separation (hardcoded vs softcoded per §4 P3 of anthropic-constitutional-ai.md) and in philosophy-expert §C.5 fork_importability
- ClaimScope: holds for all 3 Part 6b config files; applies to any Foundation config that has instance-specific values
- R: refuted_if "a Phase B fork imports default-deny-table.yaml without modification and operates correctly despite having a different authority principal"; accepted_if "first D27 fork instance creates a distinct ruslan_layer_overrides section with its own instance_id and authority principal, leaving foundation_generic untouched"

### §2.2 Default-Deny Table Machine-Readability

Every entry in `default-deny-table.yaml` must carry 4 required fields (no prose decision rules):

| Field | Type | Enum values | Required |
|---|---|---|---|
| `action_class` | string (kebab-case) | open — new classes declared here | yes |
| `blast_radius_tier` | integer | 0, 1, 2, 3 | yes |
| `reversible` | boolean | true, false | yes |
| `whitelist_status` | string | `foundation_default`, `ruslan_whitelisted`, `denied`, `halt_log_alert` | yes |

**CRITIC FINDING ENG-3 (machine-readability requirement):** A lint check must verify that every entry in `default-deny-table.yaml`'s whitelisted_classes sections carries all 4 fields. Any entry missing a field is rejected at lint time (not at gate time). This is the Hunt-Thomas "broken windows" principle [src:clean-code.md:§5 T4] applied to config: one incomplete entry is an incomplete contract; incomplete contracts create interpretation paths; interpretation paths are Default-Allow erosion.

**Blast-radius tier determinism.** Default rule: any `action_class` not in the table maps to `blast_radius_tier: 0` (immediate halt) and `whitelist_status: denied`. The tier-0 auto-halt is the machine-readable encoding of Default-Deny. No prose decision rule can substitute for this mapping. [src:part-6-governance-provenance-human-gate.md:§E Laws "Default-Deny on uncategorized actions"]

---

## §3 Deep-Module Analysis (Ousterhout Mode)

### §3.1 Gate as Deep Module

Ousterhout: "The best modules are those whose interfaces are much simpler than their implementations... A module is deep when implementation-LoC >> interface-LoC." [src:clean-code.md:§4 P1]

**The gate primitive's public interface is narrow:**

```
gate_submit(draft_path, gate_class, blast_radius_tier, reversible) → packet_id
gate_status(packet_id) → {pending | acked | rejected | halted}
gate_halt(violation_type, action_description) → halt_event_id
```

Three functions. The implementation hidden behind this interface is: F-G-R validation (Algorithm A-D from Part 6a §H), blast-radius classification lookup (blast-radius-table.yaml query), Default-Deny table lookup (default-deny-table.yaml query), AWAITING-APPROVAL packet serialisation (awaiting-approval-packet.json schema), halt-log-alert state machine (ordered three-step sequence per L3 [src:mgmt-expert-multi-mode.md:§7 L3]), approval log append (Part 6a JSONL write), and escalation taxonomy routing (escalation-taxonomy.yaml lookup).

**That is 7 internal operations behind 3 public functions.** Implementation-to-interface ratio: ~7:3 ≈ 2.3:1. This is acceptable for a gate primitive at Phase A (Ousterhout's threshold: implementation must be "much simpler" than the interface implies; 2:1 is minimal; 5:1 is good deep-module design). At Phase B, when the implementation grows to include sycophancy detection (OQ-CAI-3) and capability-tier classification (OQ-CAI-2), the ratio should grow to ~12:3 = 4:1. That is directionally correct: the interface stays narrow while the implementation deepens.

**swarm/lib/ placement.** Per clean-code.md §7 Part 6 application: "Part 6 IS essential complexity. Do not optimize it away." [src:clean-code.md:§7 Part 6] The gate machinery lives at `swarm/lib/gate.sh` (or equivalent) and is called by skill commands `/gate-submit`, `/gate-status`, `/escalate`. This is the correct modular decomposition: swarm/lib/ owns the deep module; skill commands are thin wrappers. Skill commands that embed gate logic directly are shallow-module proliferation (AP-ENG-2). [src:part-6a-provenance-officer/architecture.md:§H "All Part 6a-owned code lives as subcommand extensions of swarm/lib/-owned /lint"]

**Anti-coupling check.** Part 6b consumes Part 6a F-G-R schema (one-way `methodologically-uses` edge) and does NOT modify it. This is the Ousterhout "deep module with thin interface" pattern applied to the Part boundary: Part 6b's gate can evolve (adding new gate_class values, adding sycophancy advisory flag) without requiring Part 6a to change its F-G-R schema. The dependency arrow goes one way. [src:mgmt-expert-multi-mode.md:§6 D row 3 "Part 6b methodologically-uses Part 6a"]

### §3.2 Escalation Taxonomy SLA Values — RUSLAN-LAYER

`escalation-taxonomy.yaml` P6b.5 declares L1/L2/L3 tier structure. Per mgmt-expert §1.1 rank 5: "SLA values are primarily RUSLAN-LAYER; Foundation provides only the tier structure." [src:mgmt-expert-multi-mode.md:§1.1 rank 5 P6b.5]

**Engineering encoding:**

```yaml
# escalation-taxonomy.yaml

foundation_generic:
  tiers:
    - tier: 1
      name: strategic
      description: "Decisions touching architectural direction, FUNDAMENTAL revision, method choice"
      batch_ack: false                # L5 from mgmt-expert §7 — Tier 1 cannot be batch-acked
      auto_log: false
    - tier: 2
      name: tactical
      description: "Decisions touching cycle-level design choices, whitelist expansions"
      batch_ack: true
      auto_log: false
    - tier: 3
      name: routine
      description: "Decisions where action is categorized, reversible, low-blast"
      batch_ack: false                # no ack needed
      auto_log: true

ruslan_layer_overrides:
  instance_id: jetix-phase-a-single-owner
  sla_minutes:                        # RUSLAN-LAYER: Ruslan can change without Foundation revision
    tier_1_individual_review: 1440    # 24h — Ruslan's own declared SLA
    tier_2_batch_review_cadence: 10080 # 7d — Friday batch window
    tier_3_log_retention_days: 365
  alert_delivery_path: "shared/state/alerts.jsonl"  # RUSLAN-LAYER path
```

This encoding satisfies the philosophy-expert fork_importability contract [src:philosophy-expert-multi-mode.md:§C.5] and the SRE fail-loud principle (tier structure is the constitutional Foundation element; specific SLA values are the operational knobs). [src:sre-observability.md:§4 P1 "SLO values calibrated over 4-8 weeks; not hard-locked"]

---

## §4 Scalability Mode — Phase B/C/D Stress Test

### §4.1 Gate Throughput at Scale

**Current state (Phase A):** ~10 packets/week. Ruslan reviews individually. All are effectively Tier 1 by default (single authority, no batch mechanism). [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§3.3 "8 confirmed gate packets"]

**Phase B (€200K horizon):** ~50 packets/week. One contractor enters the system. Ruslan remains sole decision authority. Key bottleneck: if all 50 packets are Tier 1 (individual ack), Ruslan's review capacity is saturated (~5-10 high-quality reviews per day maximum). **The Tier 1/2/3 routing must be enforced at packet submission time, not at review time.** A packet that arrives without a tier assignment forces Ruslan into a triage decision — that triage is itself a capacity cost. Mitigation: the `gate_submit()` function must reject any packet without `blast_radius_tier` and `reversible` set. These two fields determine tier at submission time.

**Phase C (~500 packets/week):** At this volume, even Tier 2 batch review (Friday 17:00) becomes a bottleneck if the batch contains 100+ packets. Architecture must support sub-batching: Tier 2 batches grouped by `gate_class` (all `stage_gate` packets in one summary; all `draft_promotion` packets in another). Without sub-grouping, Ruslan's batch review becomes an unsorted inbox, not a decision surface. **HARD GAP ENG-A** (see §6).

**Approval log growth.** JSONL append-only, queryable via jq. At 500 packets/week × 52 weeks = 26,000 entries/year. A 26K-entry JSONL file is ~2-5 MB — trivially queryable by `jq`. At 10 years (260K entries), the file is ~25-50 MB — still within jq range; grep-based queries remain <1s on modern hardware. [src:event-sourcing-cqrs.md:§4 P1 "Append-Only Event Log — log compaction not needed at Jetix Phase A scale"] No compaction strategy is needed before $100M horizon. This is consistent with Greg Young's Rolling Snapshot recommendation (applied only when state reconstruction from full event replay exceeds operational tolerance). [src:event-sourcing-cqrs.md:§3 Source 2 "Rolling Snapshot heuristic pp.33-35"]

**F-G-R tag for throughput analysis:**
- F: F4 — operational convention; 500 packets/week is a Phase C projection, not current observation
- ClaimScope: holds for single-owner Jetix Phase A → C horizon; unknown for multi-authority Phase D
- R: refuted_if "at Phase B (50 packets/week), Ruslan's review bottleneck does not materialize even without Tier 1/2/3 enforcement — measured as <5 min average review time per packet"; accepted_if "approval log shows Tier 1/2/3 routing enforced (field present on every packet) within first 3 cycles after Part 6b materialisation"

### §4.2 Default-Deny Table Growth

Phase A: ~20-30 action classes. Phase B: 50-100. Phase C: 200+. A YAML file with 200+ entries is readable but requires discipline: entries must be sorted by `blast_radius_tier` (descending severity) so that the most restrictive entries appear first and are easiest to audit.

**Migration trigger.** At 1000+ entries, YAML as a human-readable format starts to lose its observability value (Julian Practical Monitoring anti-pattern: "monitoring what is easy to maintain, not what is observable"). [src:sre-observability.md:§3 Source 3 Julian "tool-first thinking anti-pattern"] At that point, migrate to an indexed format (SQLite or a JSON Schema registry with machine-generated HTML documentation). This migration is a Phase D concern — declare as a known future migration, not a current gap.

**Lint check for completeness.** Every entry in `default-deny-table.yaml` must carry all 4 required fields (ENG-3 above). The lint check must also verify that the `constitutional_never_list` has exactly 11 entries matching the 11 FUNDAMENTAL §6.1 rules. [src:part-6-governance-provenance-human-gate.md:§E Laws "11 hard AI/agent limits"] A count mismatch is a lint error. This is the machine-readable encoding of the philosophy-expert's §C.1 encoding audit. [src:philosophy-expert-multi-mode.md:§C.1]

### §4.3 Halt-Log-Alert Latency Targets

FUNDAMENTAL §5.2 fail-loud: "Strategic doc modification — halt, alert, не proceed." [src:sre-observability.md:§4 P6 "Fail-Loud: Silent Failures Are the Worst Category of Bug"] The SRE Book error-budget framing applies: each constitutional violation that proceeds without halting is a budget burn event. Target latency:

| Step | Phase A target | Phase C target | Measurement method |
|---|---|---|---|
| Halt (action stops) | ≤1s from detection | ≤1s (same; halt is in-process) | audit log timestamp delta |
| Log (audit entry written) | ≤5s | ≤5s (append to JSONL is fast) | timestamp delta: halt_at → log_at |
| Alert (Ruslan notification) | ≤60s (file write to alerts.jsonl) | ≤60s (same path) | timestamp delta: log_at → alert_at |

**Phase A measurement mechanism.** Halt-log-alert events write to `swarm/logs/lint-events.jsonl` (Part 6a §H Algorithm C edge case precedent for log-only non-blocking warns). [src:part-6a-provenance-officer/architecture.md:§H Algorithm C] For constitutional violations, the entry carries `{timestamp, halt_at, log_at, alert_at, violation_type, action_class}`. The `/company-status` skill reads this file and surfaces any entry where `alert_at - halt_at > 60s`. This is the SRE "symptom-based alerting" principle: alert on the condition that matters (latency breach), not on the mechanism (specific script failure). [src:sre-observability.md:§3 Source 1 Ch.6 "symptoms vs causes monitoring"]

**Antifragility check for halt-log-alert at 10× scale:**
- **10× violation frequency:** Does the halt-log-alert state machine require >30% refactor if violation rate scales 10×? No — the three-step sequence is stateless (each event is processed independently). Append to JSONL is O(1) per event. Status: NOT fragile at 10×.
- **10× log file size:** Does JSONL become unqueryable? No — jq scales linearly; 260K entries is well within range (see §4.1 approval log analysis). Status: NOT fragile at 10×.
- **10× action class count:** Does Default-Deny table lookup slow down? YAML lookup is O(n) on 200+ entries; Python yaml.safe_load + dict lookup is effectively O(1) after parse. Status: NOT fragile at 10×.

**F-G-R tag:**
- F: F4 — these are Phase A design targets; not yet measured
- ClaimScope: holds for single-node, single-owner, file-based Foundation; unknown for distributed multi-node enforcement
- R: refuted_if "first halt-log-alert event shows alert_at - halt_at > 60s (latency target missed)"; accepted_if "3 consecutive halt-log-alert events show all three timestamp deltas within targets"

### §4.4 Schema Fork Divergence — D27 Cross-Fork Strategy

D27 cross-fork-provenance requires a reconciliation strategy for cases where fork instances diverge on config values. [src:part-1-system-state-persistence/architecture.md:§0 "D27 fork-and-merge architecture"] For Part 6b specifically, the divergence vectors are:

1. **Whitelist divergence** — Fork A whitelists `crm_touch_operation`; Fork B does not. This is a `ruslan_layer_overrides` divergence — expected, by design. No reconciliation needed unless the two forks merge.
2. **Blast-radius tier divergence** — Fork A assigns `external_write` to Tier 1; Fork B assigns it to Tier 2. This is a `foundation_generic` tier definition divergence — unexpected, constitutional. A fork that diverges on `foundation_generic` entries is no longer a valid Foundation fork; it is a separate Foundation. This must be declared in D27's reconciliation rules.
3. **gate_class enum divergence** — If Fork B adds a new enum value `pre_release_gate` not in the canonical schema, any cross-fork packet with `gate_class: pre_release_gate` fails validation on the canonical schema. Mitigation: `gate_class` enum is versioned (§1.3); forks must submit a Foundation revision proposal (AWAITING-APPROVAL gate packet) before adding new enum values. This is the event-sourcing "There is no Delete" principle applied to schema evolution: you cannot remove or diverge a `foundation_generic` enum value silently; you can only add via HITL-gated Foundation revision. [src:event-sourcing-cqrs.md:§3 Source 2 "There is no Delete pattern p.31"]

---

## §5 Critic Mode — Hard Findings

### §5.1 Conformance Checklist

| Check | Result | Evidence |
|---|---|---|
| 1 — Deep-module check | PASS | Gate primitive has 3-function public interface over 7+ internal operations; swarm/lib/ placement correct |
| 2 — Function-purpose check | PASS for schema design; N/A for YAML configs | Schema $ref pattern is self-documenting; config YAML requires purpose comments on every section |
| 3 — Test-integrity check | N/A (no code diff under review) | Schema/config artefacts; no test deletion risk |
| 4 — Premature-abstraction check | PASS | No abstraction proposed without concrete use case; all patterns have ≥3 concrete consumers |
| 5 — External-dependency check | PASS | No external dependencies; all schemas are filesystem-local |
| 6 — DRY check | FAIL-RISK (ENG-1, ENG-3) | gate_class enum and blast-radius tier definitions risk duplication across schemas; mitigation specified in §1.1 and §2.2 |
| 7 — Tool-eval acceptance check | N/A (not a tool-eval artefact) | — |
| 8 — Architecture-pattern check | PASS | Deep-module gate primitive declared; swarm/lib/ placement declared; Hub-and-spoke skill wrapper pattern declared |

**Acceptance predicate for this critic pass:** "The 5 Part 6b schemas have no independent gate_class enum definitions (DRY); blast-radius tiers are defined once in blast-radius-table.yaml and referenced elsewhere; foundation_generic / ruslan_layer_overrides split is present in all 3 config files; schema_version_history block is present on all 5 schemas."

### §5.2 Alternatives + Kill-Conditions

| # | Alternative | Kill condition |
|---|---|---|
| A (recommended) | gate_class canonical in awaiting-approval-packet.json; $ref from all other schemas; foundation_generic / ruslan_layer_overrides split in all 3 configs; schema_version_history block on all 5 | Fails if JSON Schema validator cannot resolve cross-file $ref in the Jetix toolchain (no JSON Schema validator with cross-file resolution currently declared) |
| B | Copy enum values into each schema independently; maintain consistency via lint check rather than $ref | Fails when any of the 5 schemas is updated without running the lint check — drift is guaranteed over 50+ cycles |
| C (status-quo) | No formal schema structure; ad-hoc YAML per packet as currently in swarm/gates/ | Fails at first Phase B fork attempt when the fork cannot determine which YAML fields are Foundation-generic vs Jetix-specific |

**Kill-condition note on Alternative A.** The `$ref` resolution tooling concern is real. Currently, Jetix does not declare a JSON Schema validator in its tech stack. Wave C materialisation must either (a) declare a specific validator (e.g., `jsonschema` Python library, already available in the repo's Python environment) or (b) implement the $ref discipline as a lint-enforced naming convention rather than a runtime-validated schema reference. Option (b) is less rigorous but achievable without adding a new dependency. Decision is RUSLAN-LAYER (tool choice) but the constraint is Foundation (the DRY requirement is constitutional).

### §5.3 Anti-scope

- This cell does NOT produce the canonical Part 6b foundation artefact — it produces an engineering cell draft. Brigadier promotes after human gate ack.
- This cell does NOT evaluate VSM S3 authority designation (TRADEOFF-01) — Wave C Bullet 3, systems-expert territory, BLOCKED on Ruslan ack per worklist line 334. [src:wave-c-worklist.md:line 334-342]
- This cell does NOT author the capital implications of blast-radius Tier 1 decisions — investor-expert territory per §1b integrative_obligation.
- This cell does NOT verify the correctness of each of the 18 banned phrases in sg-banned-phrases.yaml against a Popperian falsifiability standard — that is philosophy-expert scope (philosophy-expert §C.4 declared the gap [src:philosophy-expert-multi-mode.md:§C.4]).
- This cell does NOT implement the F-G-R compliance scanner (Wave C Bullet 1) — that is Part 6a territory; Part 6b consumes Part 6a's compliance signals, not the scanner itself.

---

## §6 Open Questions (Hard Gaps)

**HARD GAP ENG-A — Tier 2 batch sub-grouping at Phase C volume (500 packets/week).**
At 500 packets/week, even a well-tiered approval queue requires sub-grouping by `gate_class` within Tier 2 batches. Without sub-grouping, Ruslan's Friday batch review becomes an unsorted inbox of 100+ heterogeneous tactical decisions. The current escalation-taxonomy.yaml design (§3.2 above) declares Tier 2 as batch-able but does not specify the grouping algorithm for batch summaries. This gap is not closable in Wave C — it requires operational data on actual Tier 2 packet composition (what gate_class mix does Phase B actually produce?) before the grouping algorithm can be designed. Route to Wave D / Phase B operational review.

**HARD GAP ENG-B — JSON Schema $ref toolchain not declared.**
Alternative A's $ref discipline (§5.2) requires a JSON Schema validator with cross-file $ref resolution. The Jetix toolchain does not currently declare a schema validator. This gap is closable within Part 6b materialisation (Phase A Wave C): declare `jsonschema` Python library as the validator, add it to the `swarm/lib/` dependency manifest, and add a `/lint --check-schemas` subcommand that runs jsonschema validation against all Part 6b JSON schemas. Effort: ~0.5 day. Priority: HIGH (this is the DRY enforcement mechanism; without it, ENG-1 and ENG-3 drift risks have no automated detection).

---

## §H Conformance Checklist (self-check, §3.1 engineering-expert mode)

| Check | Result | Evidence |
|---|---|---|
| Falsifier present on every major claim | pass | F-G-R R.refuted_if fields on every tagged claim above |
| ≥2 alternatives + status-quo + kill-conditions | pass | §5.2 three alternatives with kill-conditions |
| Anti-scope declared | pass | §5.3 |
| Provenance: every recommendation traces to canonical source | pass | All recommendations cite specific §-locations in source files read |
| DRY finding surfaced and actionable | pass | ENG-1, ENG-3 with specific mitigation recommendations |
| Foundation/RUSLAN-LAYER split explicit | pass | §2.1 explicit two-section config structure with examples |
| Scalability to 500 packets/week addressed | pass | §4.1-§4.3 with antifragility check |
| At least one HARD GAP declared | pass | ENG-A and ENG-B |

**Acceptance predicate for this engineering cell:** "5 Part 6b schemas have no independent gate_class enum definitions; 3 config files carry foundation_generic / ruslan_layer_overrides sections; schema_version_history present on all 5 schemas; lint check for 11-entry constitutional_never_list count is specified; halt-log-alert latency targets are declared with measurement method."

---

## §I Anti-scope (full cell)

See §5.3 above.

---

*Drafted by engineering-expert, modes: scalability + clean-code + critic, Wave C Bundle 1, 2026-04-28.*
*Candidate for brigadier review before canonical promotion.*
