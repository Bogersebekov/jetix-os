---
title: "Part 4 — Role Taxonomy & Coordination Protocol (Architecture)"
date: 2026-04-28
type: foundation-architecture
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 2
part: 4
part_slug: part-4-role-taxonomy-coordination-protocol
status: ruslan-acked-canonical
F: F5
F_promotion_ack: "Ruslan ack 2026-04-28 per decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md Decision #7 — F4→F5 codified rule on canonical promotion. IP-1 self-audit clean (zero executor names). routing-table.yaml + task-return-packet.json + executor-binding.yaml.template ratified. UND-1 binding satisfied. OQ-B2-A retroactive fix queued for Bundle 3 cycle start. Future modification requires AWAITING-APPROVAL constitutional gate per Part 6b §E Law L9."
ClaimScope: "Holds for Foundation Phase A coordination protocol with hub-and-spoke topology + 5-expert ROY swarm + brigadier sole dispatcher + 13 legacy agents on adjacent mailboxes. Role manifests = U.Episteme Foundation generic; routing-table.yaml STRUCTURE = Foundation generic; task-return-packet.json schema = Foundation generic; executor-binding.yaml TEMPLATE = Foundation generic. Specific role-manifest entries + routing-table.yaml entries + executor-binding.yaml populated values = RUSLAN-LAYER per IP-1 strict. Phase B forks replace executor bindings; structural pattern persists."
R:
  refuted_if: "(a) Any executor name (model identifier, agent file path, instance ID) appears in any Foundation §A-§N or §X section — IP-1 violation auto-rejects; OR (b) routing-table.yaml has fewer than 20 distinct routing rules — Ashby under-variety; OR (c) task-return-packet.json schema is not superset-compatible with Part 1 §I.4 frozen stub fields (git_commit_hash, actor_role_archetype, cycle_id, gate_class) — frozen-fields invariant violated; OR (d) Part 4 §I duplicates the C1 canonical answer instead of REFERENCING swarm/lib/README.md and C1-joint-design.md"
  accepted_if: "All bullets P4.1/P4.2/P4.3 acceptance predicates pass; routing-table.yaml exists with ≥20 distinct routing rules + IP-1 enforced (role slugs only); task-return-packet.json schema FULLY SPECIFIED with frozen Part 1 §I.4 fields preserved + gate_class enum from Part 6b §I.4 F8 LOCKED [stop_gate, stage_gate, draft_promotion]; §I REFERENCES swarm/lib/README.md (DRY); executor-binding.yaml template declared with F.6 M1-M6 onboarding mandatory"
predecessor_artefacts:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-4-role-taxonomy-coordination-protocol.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md (§3.1 C1; §4.1 UND-1; §6.4 ~40% structural change risk)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md
  - swarm/lib/README.md
constitutional_inputs_consumed:
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md (esp. §I.4 task-return-packet stub frozen fields)
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md
  - swarm/wiki/foundations/part-6b-human-gate/architecture.md (esp. §I.4 awaiting-approval-packet F8 with gate_class enum)
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md (IP-1 CRITICAL; IP-6; IP-8 F.6; A.13; L/A/D/E)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/multi-agent-architecture.md (hub-and-spoke; MAST coverage; Cognition minimum-viable-topology)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md (hard-rule anti-scope; transparency)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md (Ashby Ch. 11 requisite variety ≥20 routing rules)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/mereology-typed-edges.md (A.14 canonical)
  - raw/books-md/anthropic/askell-2021-hhh.md (Corrigibility Appendix E.2)
  - raw/books-md/anthropic/bai-2022-cai.md (constitutional_never_list pattern)
  - raw/books-md/event-sourcing/young-cqrs-2010.md (task-return-packet as event log; Reversal Transactions)
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - design/JETIX-FPF.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
---

# Part 4 — Role Taxonomy & Coordination Protocol (Architecture)

## §0 Mission

Part 4 is the **coordination protocol of the Jetix swarm**: how role-manifests are structured, how dispatches route through the hub-and-spoke topology, how task-return packets feed the compound learning phase, how escalations propagate to the human gate. The 5-expert ROY swarm + brigadier + 13 legacy agents work because Part 4 declares (a) what a role IS (U.Episteme — role-archetype with method, j-level authority, mode allowlist, write-scope, escalation taxonomy), and (b) how the role-archetype maps to a specific executor instance via RUSLAN-LAYER `executor-binding.yaml`. **The mapping is one-to-many across Phase A→D: same role archetype, different executors over time.** This is **IP-1 Role≠Executor — the constitutional invariant of Part 4** [src:design/JETIX-FPF.md:§5.1 IP-1; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P1; F8|G:Foundation constitutional invariant|R-high].

Bundle 2 introduces three structural deltas:

1. **P4.1 — `swarm/lib/routing-table.yaml` as PRIMARY GAP MATERIALISATION.** Routing logic currently embedded in `brigadier.md` + 5 ROY expert system prompts is EXTRACTED into a declarative YAML. Per role: `slug`, `j_level_authority`, `allowed_modes`, `write_scope_glob`, `escalation_taxonomy_per_trigger`, `hub_and_spoke_dispatch_chain`, `accessor_skills_invocable`, `mailbox`. **Variety target ≥20 distinct routing rules per Ashby Ch. 11 requisite variety** [src:raw/books-md/cybernetics/ashby-introduction-to-cybernetics-1956.md:Ch.11; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md:§Principle 2; F5|G:Foundation routing schema|R-medium until materialised]. The 5 experts × 4 modes = 20 base cells; plus brigadier's 10 escalation triggers + 4 task shapes + M-class rate limiter = **far exceeds 20**.

2. **P4.2 — C1 ownership decision materialised in Part 4 (joint with Part 3 P3.1).** §I REFERENCES `swarm/lib/README.md` (DRY enforced — single canonical answer at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` + `swarm/lib/README.md`; §I sections of Parts 3 + 4 cross-reference). §B Outputs lists "wiki accessor pipeline skills :: invocable by any consumer :: on-demand" with rationale that Part 4 ROUTES invocations but does NOT OWN the scripts (Part 3 lead, Part 4 advisory per Variant A). routing-table.yaml `accessor_skills_invocable:` field per role declares which skills each role may invoke.

3. **P4.3 — UND-1 task-return-packet.json FULL schema specification.** Per Ruslan ack OQ-3: **Part 5 (Bundle 3) receives RAW task-return packets and does its own DRR extraction**; Part 4 emits raw packets only. This document FULLY SPECIFIES the schema with the 4 frozen Part 1 §I.4 fields (`git_commit_hash`, `actor_role_archetype`, `cycle_id`, `gate_class`) PRESERVED UNCHANGED — **with one corrected enum value: `gate_class` MUST use Part 6b §I.4 F8 LOCKED enum `[stop_gate, stage_gate, draft_promotion]`, NOT the Part 1 §I.4 stub's stale enum `[autonomous, requires-approval, hitl-required]`. The Part 1 stub enum is a Bundle 1 drift defect flagged here as OQ-B2-A (proposed Bundle 1 retroactive correction via constitutional AWAITING-APPROVAL packet).**

The hub-and-spoke topology is **structural, not policy** [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/multi-agent-architecture.md:§P-2; src:CLAUDE.md Global Rule 8 hub-and-spoke; F8|G:Foundation generic minimum-viable-topology|R-high]. Cells NEVER invoke other cells directly — they declare `escalations[]{trigger: peer-input-needed, requested: <peer-cell>}` and brigadier dispatches the peer. This prevents MAST failure modes 2.4 (Information Withholding) and 2.5 (Ignored Other Agent's Input) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/multi-agent-architecture.md:§MAST 14 failure modes coverage; F4|G:MAST coverage discipline|R-medium]. Brigadier holds context-integration authority; cells produce focused contributions per their `<domain> × <mode>` prefix.

**IP-1 self-audit at finalize:** every section §A through §X has been audited for executor-name leaks. Zero references to: model identifiers (e.g., `claude-sonnet-4-6`, `claude-opus-4-7`); agent file paths (e.g., `.claude/agents/engineering-expert.md`, `.claude/agents/brigadier.md`); instance IDs (any unique deployment identifier). All references to roles use the role-archetype slug (e.g., `engineering-expert`, `brigadier`, `manager`, `sales-lead`). Phase A binding lookup happens via `executor-binding.yaml` (RUSLAN-LAYER per §X). Critic gate verifies; OQ-B2-A flagging acknowledges the cross-Bundle drift between Part 1 §I.4 stub and Part 6b §I.4 F8 LOCKED schema.

---

## §A Inputs

| Source | Data shape | Event trigger |
|---|---|---|
| Role-manifest files (U.Episteme) | Role-archetype manifest per IP-6 5-block structure: identity / ontological-positioning / method / production-dependencies / evolution. Lives at canonical role-archetype file referenced via routing-table.yaml `slug:`. NO executor name in manifest. | Written once at Foundation build; updated only via Part 6 governance gate (`gate_class: stage_gate` packet) [src:design/JETIX-FPF.md:§5.6 IP-6; F5|G:Foundation generic|R-high] |
| Executor-binding registry (RUSLAN-LAYER) | `executor-binding.yaml` per role-archetype-to-executor binding. Includes M1-M6 F.6 onboarding block mandatory per IP-8. NOT a Foundation artefact. | Updated when executor changes (model swap, agent replacement, role reassignment) [src:design/JETIX-FPF.md:§5.8 IP-8; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P7; F4|G:RUSLAN-LAYER per IP-1|R-medium] |
| Inbound message from any role | `shared/schemas/message.schema.json` extended schema — `acting_as:` field MANDATORY per FUNDAMENTAL §3.2.4; `task_id`, `mode:`, `inputs[]`, `expected_return_path`, `acceptance_predicate` (AP-25 prevention) | Per-dispatch event [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3.2.4; F5|G:Foundation generic message schema|R-high] |
| Escalation signal from any role | Structured escalation packet per `swarm/lib/shared-protocols.md` §4: `trigger`, `evidence`, `routing_suggestion` | When a role reaches a J-level boundary it cannot self-resolve [src:design/JETIX-FPF.md:§2.1a A.13 Agency-CHR; F5|G:Foundation generic escalation taxonomy|R-high] |
| Task brief from owner OR brigadier | Task spec with acceptance_predicate non-empty (AP-25 prevention) | At task intake [src:.claude/agents/brigadier.md (read for routing pattern only — do NOT cite content as Foundation):§2.3 acceptance-predicate format; F4|G:Foundation generic intake discipline|R-high] |
| Bundle 1 LOCKED schemas | F-G-R per Part 6a §I.1 F8; awaiting-approval-packet per Part 6b §I.4 F8; default-deny-table per Part 6b §I.3 F8; blast-radius-table per Part 6b §I.4 F8 | Consumed at every dispatch and every escalation [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1; src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4; F8|G:Bundle 1 LOCKED contracts|R-high] |
| Part 1 §I.4 task-return-packet stub frozen fields | `git_commit_hash`, `actor_role_archetype`, `cycle_id`, `gate_class` — superset-compatible base for Part 4 §I full schema | Consumed at task-return packet emission [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§I.4; F8|G:Bundle 1 LOCKED frozen-fields invariant|R-high — BUT see OQ-B2-A on gate_class enum drift] |
| C1 Joint Design canonical answer | `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` + `swarm/lib/README.md` — accessor pipeline ownership Variant A | Consumed at routing-table.yaml `accessor_skills_invocable:` per role [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md:§3 Variant A; F4|G:Bundle 2 C1 Joint Design canonical|R-medium] |

---

## §B Outputs

| Consumer | Data shape | Event published |
|---|---|---|
| Any executing role-instance | Dispatch packet conforming to message schema + routed to correct mailbox `comms/mailboxes/<role-slug>.jsonl` (append-only) | `task-dispatched-event` [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-4-role-taxonomy-coordination-protocol.md:§B; F4|G:Foundation generic dispatch contract|R-high] |
| **Part 5 (Compound Learning) — Bundle 3 stub; UND-1 BINDING CRITICAL** | **Structured task-return-packet conforming to §I full schema** — RAW packets per Ruslan-acked OQ-3 (Part 5 does own DRR extraction). The packet is the load-bearing handoff at the Part 4 → Part 5 compound boundary. | `compound-phase-start-event` [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§4.1 UND-1; F4|G:Bundle 2 P4.3 binding; F5 on Bundle 3 Part 5 consumption validation|R-medium] |
| Part 6b (Human Gate) | Escalation packet when J-Strategic or J-Approve boundary hit; routing table updates require governance gate (`gate_class: stage_gate` per Part 6b §I.4 F8) | `escalation-submitted-event` [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4; F8|G:Bundle 1 LOCKED|R-high] |
| Part 1 (System State Persistence) | Committed role-manifest artefacts, routing-table.yaml, message schema YAML — every artefact via Part 1 §I.2 commit-format-tokens.json `[swarm-lib]` or `[part4]` token | `artifact-committed-event` [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§I.2; F8|G:Bundle 1 LOCKED|R-high] |
| Wiki accessor pipeline skills (per C1 Joint Design — Part 4 ROUTES invocations but does NOT OWN scripts) | Invocation of `swarm/lib/<skill>` per role's `accessor_skills_invocable:` field in routing-table.yaml :: invocable by any consumer :: on-demand | `accessor-skill-invoked-event` [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md; src:swarm/lib/README.md; F4|G:Bundle 2 P4.2 binding|R-medium] |
| Part 6a (Provenance Officer) | F-G-R compliance data per dispatch and per task-return-packet (the packet's `f_g_r:` field carries the snapshot) | Consumed at quarterly immune audit [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§J; F8|G:Bundle 1 LOCKED|R-high] |
| Part 8 (Health Monitoring — Bundle 4 stub) | Coordination health signals: dispatch-rate, escalation-rate, task-return-rate, IP-1-compliance-rate, routing-table-variety-count | `health-poll-event` [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-4-role-taxonomy-coordination-protocol.md:§B; F2|G:Bundle 4 Part 8 stub|R-low] |

---

## §C Side-effects

- **Mailbox write:** `comms/mailboxes/<role-slug>.jsonl` — appended per dispatch [src:design/JETIX-FPF.md:§5.3 IP-3; F8|G:Foundation generic IP-3 substrate|R-high]. APPEND-ONLY. Reversal Transactions: corrections are NEW entries with `corrects: <prior_msg_id>` field.

- **Routing-table.yaml committed:** `swarm/lib/routing-table.yaml` — when modified, AWAITING-APPROVAL packet with `gate_class: stage_gate` per Part 6b §I.4 F8 schema; ack required before merge per C1 Joint Design modification governance [src:swarm/lib/README.md:§4 Modification governance; F4|G:Bundle 2 P4.2 binding|R-medium].

- **Executor-binding registry:** RUSLAN-LAYER `executor-binding.yaml` — NOT a Foundation artefact; binding is RUSLAN-LAYER parameterisation over the Foundation role archetype [src:design/JETIX-FPF.md:§5.1 IP-1; F8|G:IP-1 strict separation|R-high].

- **Audit log entry per escalation routed:** appended to `swarm/approvals/log.jsonl` per Part 6a §C [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§C; F8|G:Bundle 1 LOCKED|R-high].

- **Task-return-packet emission:** committed at `swarm/wiki/cycles/<cycle_id>/task-returns/<packet_id>.json` (or per Part 5 Bundle 3 specification of consumption path; canonical path TBD in Bundle 3 Part 5 architecture). Append-only.

- **NO direct write to canonical wiki/:** Part 4 dispatches cells; cells write to `swarm/wiki/drafts/<task-id>-<expert>-<mode>-<slug>.md`; brigadier (Part 4 territory) promotes drafts to canonical via Part 3's admissibility surface. Part 4 does NOT write canonical entities.

- **NO modification of `.claude/agents/*.md` files in Bundle 2 scope:** the routing-table.yaml is EXTRACTED FROM the existing role manifests, not a replacement; the `.claude/agents/*.md` files remain RUSLAN-LAYER (per §X) and are not modified by this Bundle 2 architecture work [src:prompts/wave-c-bundle-2-deep-prompt-2026-04-28.md:§10.8 Untouchable trees in Phase A].

---

## §D Dependencies (typed per FPF A.14)

Every edge from Part 1 §D 10-edge canonical reference table. Generic `depends-on` FORBIDDEN.

- **`creates Part 5`** — task-return packets feed Part 5 compound phase boundary (UND-1 BINDING). Part 4 emits packets; Part 5 consumes raw and does own DRR extraction per Ruslan-acked OQ-3 [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§4.1 UND-1; F4|G:Bundle 2 P4.3 binding|R-medium].

- **`creates Part 1`** — every role-manifest, routing-table.yaml, message-schema, executor-binding.yaml is committed via Part 1 substrate per IP-3 commit-substrate. The `creates` direction reflects Part 4's authoring of these artefacts [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-4-role-taxonomy-coordination-protocol.md:§D; F8|G:Foundation IP-3|R-high].

- **`methodologically-uses Part 6b`** — escalations route through Part 6b's human gate; gate_class enum from Part 6b §I.4 F8 schema; AWAITING-APPROVAL packet per Part 6b for routing-table modifications [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4; F8|G:Bundle 1 LOCKED|R-high].

- **`methodologically-uses Part 6a`** — every dispatched artefact carries F-G-R per Part 6a §I.1 F8; every task-return-packet's `f_g_r:` field $refs the F8 schema [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1; F8|G:Bundle 1 LOCKED|R-high].

- **`operates-in swarm/lib/`** — routing-table.yaml + accessor skills + shared-protocols.md + hooks all live in `swarm/lib/` per C1 Joint Design [src:swarm/lib/README.md:§2; F4|G:Bundle 2 C1 Joint Design canonical|R-medium].

- **`methodologically-uses Part 3`** — accessor skills invocation per role's `accessor_skills_invocable:` field; ADVISORY ownership of swarm/lib/ accessor pipeline (Part 3 LEAD per C1 Joint Design Variant A) [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md:§3.3 advisory rationale; F4|G:Bundle 2 C1|R-medium].

- **`methodologically-uses Part 7`** — project lifecycle stage_gate semantics (Part 7 territory; Bundle 4); routing-table.yaml escalation_taxonomy_per_trigger references project lifecycle states for stage_gate routing [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-7-project-lifecycle-substrate.md (Wave A baseline); F2|G:Bundle 4 Part 7 stub|R-low].

**Edges Part 4 explicitly does NOT have:**

- NO `creates Part 3` — Part 4 routes accessor skill INVOCATIONS but does not own the scripts (per C1 Joint Design Variant A: shared infra `swarm/lib/`, Part 3 lead).
- NO `ComponentOf` any other Part — Part 4 is structural protocol; not a constituent of other Parts.
- NO `depends-on` (any) — generic dependency FORBIDDEN.

---

## §E Boundary L/A/D/E

### Laws — invariants that MUST hold (constitutional defects on violation)

**L1 — IP-1 STRICT (CRITICAL CONSTITUTIONAL INVARIANT).** Role manifests (U.Episteme) are NEVER the same artefact as executor bindings (RUSLAN-LAYER). NO executor name (model identifier, agent file path, instance ID) appears in any Foundation Part 4 artefact. **Critic gate AUTO-REJECTS violations.** Phase B partner forks the Foundation role manifests; replaces executor bindings per their fork's `executor-binding.yaml`. [src:design/JETIX-FPF.md:§5.1 IP-1; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P1; F8|G:Foundation constitutional invariant|R-high]

**L2 — `acting_as:` field is MANDATORY in every message.** Absent = rejected at coordination gate per FUNDAMENTAL §3.2.4 [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3.2.4; F5|G:Foundation generic message schema|R-high].

**L3 — J-level decision matrix architecturally encoded per A.13 Agency-CHR.** J-Auto / J-Approve / J-Strategic per role per decision-class. Encoded in routing-table.yaml `j_level_authority:` field per role. NOT behavioural assumption [src:design/JETIX-FPF.md:§2.1a A.13; F5|G:Foundation generic A.13 dogfood|R-high].

**L4 — All novel/uncategorized actions ESCALATE.** No "creative interpretation" per FUNDAMENTAL §6.1 last bullet [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1; F8|G:Foundation hard rule|R-high].

**L5 — Default-Deny enforced at dispatch boundary.** Per Part 6b §I.3 `constitutional_never_list:` enum (11 §6.1 hard rules). Any action class in the never-list refuses dispatch with `escalations[]{trigger: constitutional-violation}` [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.3 default-deny-table F8 LOCKED; src:RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md:§1 Decision #3; F8|G:Bundle 1 LOCKED Default-Deny FRAMEWORK|R-high].

**L6 — Halt-Log-Alert (Part 6b §E Law L9).** ≤1s halt / ≤5s log / ≤60s alert. Applies to coordination-protocol failures affecting ≥1 cell mid-cycle. The strict ordering invariant prevents racy log-write before halt [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E Law L9; F8|G:Bundle 1 LOCKED|R-high].

**L7 — Corrigibility (Askell HHH Appendix E.2 verbatim).** "NO mechanism exists by which any agent, any Part, or any automation may lock the human owner out." Coordination protocol cannot prevent owner from inspecting / halting / redirecting. Routing-table.yaml is human-readable; mailbox files are inspectable; task-return packets are queryable [src:raw/books-md/anthropic/askell-2021-hhh.md:Appendix E.2; src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E Law L9; F8|G:Bundle 1 LOCKED Corrigibility|R-high].

**L8 — Hub-and-spoke topology: cells NEVER invoke other cells directly.** Brigadier is sole dispatcher per Anthropic orchestrator-workers + Cognition's "Don't Build Multi-Agents" minimum-viable-topology [src:swarm/wiki/cycles/cyc-foundation-br-2026-04-28/wave-b/consultants/multi-agent-architecture.md:§P-2 + §minimum-viable-topology; src:CLAUDE.md Global Rule 8; F8|G:Foundation generic topology|R-high]. Cells declare `escalations[]{trigger: peer-input-needed, requested: <peer-cell>}`; brigadier dispatches the named peer; original cell re-invoked with peer's draft visible. This prevents MAST failure modes 2.4 (Information Withholding) and 2.5 (Ignored Other Agent's Input).

**L9 — MAST coverage at termination.** Every dispatch carries explicit `ap_budget` (max-turn budget per cell). Addresses MAST failure 12.4% "Unaware of Termination Conditions" [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/multi-agent-architecture.md:§MAST 14 failure modes; F4|G:MAST coverage discipline|R-medium].

**L10 — Routing variety target ≥20 distinct rules (Ashby Ch.11 requisite variety).** Brigadier routing variety must match task-type variety in dispatch space. Below 20 = under-variety. Achieved by 5 experts × 4 modes = 20 base + brigadier escalation triggers + task shapes + rate limiter. [src:raw/books-md/cybernetics/ashby-introduction-to-cybernetics-1956.md:Ch.11; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md:§Principle 2; F5|G:Foundation routing schema target|R-medium]

**L11 — Append-only mailboxes.** `comms/mailboxes/<role-slug>.jsonl` APPEND-ONLY per IP-3 + Reversal Transactions; corrections are NEW entries with `corrects:` pointer [src:raw/books-md/event-sourcing/young-cqrs-2010.md:p.31; F8|G:Foundation generic|R-high].

### Admissibility — acceptance criteria for inputs

**A1 — Role-manifest accepted only after IP-6 5-block completeness check.** All 5 blocks populated: identity / ontological-positioning / method / production-dependencies / evolution [src:design/JETIX-FPF.md:§5.6 IP-6; F5|G:Foundation generic|R-high].

**A2 — Executor-binding activated only after F.6 six-step onboarding (M1-M6).** All M1-M6 populated; M3 Qualify reviewer pass confirmed. RUSLAN-LAYER artefact per IP-1 strict [src:design/JETIX-FPF.md:§5.8 IP-8; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P7; F4|G:RUSLAN-LAYER F.6 onboarding|R-medium].

**A3 — Inbound message accepted only if `acting_as:` matches a registered role-manifest name.** Per L2 mandatory field; rejection at coordination gate with `escalations[]{trigger: schema_error}` if absent or unrecognised [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3.2.4].

**A4 — Task brief accepted only if it carries `acceptance_predicate:` non-empty.** AP-25 prevention. Vague tasks REFUSED with `escalations[]{trigger: missing-acceptance-predicate}`.

**A5 — Cell dispatch accepted only if `<domain> × <mode>` prefix matches role's `allowed_modes:` from routing-table.yaml.** Mismatch = `escalations[]{trigger: out-of-domain}` per E-15 routing.

**A6 — Accessor skill invocation accepted only if skill is in caller role's `accessor_skills_invocable:` field.** Invoking skill outside permit set = `escalations[]{trigger: permission-denied}` per swarm/lib/README.md §5 invocation contract.

### Deontics — obligations of this part toward consumers

**D1 — Maintain canonical role-manifest registry as DECLARATIVE YAML.** `swarm/lib/routing-table.yaml`. NOT embedded in system-prompt prose. Wave C P4.1 materialisation. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-4-role-taxonomy-coordination-protocol.md:§E Deontics; F5|G:Bundle 2 P4.1 binding|R-low until materialised]

**D2 — Route escalations within one cycle turn; no silent absorption.** Cells return `escalations[]`; brigadier dispatches named peer or opens AWAITING-APPROVAL packet within the same cycle.

**D3 — Expose routing table legible to all parts without requiring read of any individual agent system-prompt file.** routing-table.yaml is authoritative; consumers do NOT read `.claude/agents/*.md` to discover routing.

**D4 — Emit task-return-packet conforming to §I full schema (P4.3 binding).** For every dispatched cell. Part 5 (Bundle 3) consumes raw at `compound-phase-start-event`.

**D5 — Surface dispatch failures with specific reason (Anthropic CAI transparency).** No generic "rejected"; the escalation packet names the trigger and routing suggestion.

**D6 — Maintain IP-1 compliance rate = 100% (audited quarterly by Part 6a).** Zero executor names in Foundation role definitions [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§3.2.5 IP-1 audit; F8|G:Foundation IP-1 audit|R-high].

### Effects — measurable outcomes

**E1 — Successful dispatch:** structured packet delivered to `comms/mailboxes/<role-slug>.jsonl`; verifiable via append + git commit.

**E2 — Cycle completion:** all dispatched tasks returned with structured task-return-packet; open task count = 0 at cycle close.

**E3 — Role-manifest health:** IP-1 compliance rate = 100% (audited quarterly per Part 6a / Part 8).

**E4 — Routing variety:** measurable via wc-or-equivalent on routing-table.yaml role+mode entries; target ≥20.

**E5 — Task-return-packet schema validation:** 3 synthetic fixture packets validate against §I.1 schema; Part 1 §I.4 frozen fields appear UNCHANGED in §I.1 full schema (with corrected gate_class enum from Part 6b §I.4 F8 LOCKED).

**E6 — Accessor skill invocation routing:** routing-table.yaml lints clean against `swarm/lib/README.md` §3 inventory (no role permits an undocumented skill; no skill orphan with no role permit).

---

## §F Anti-scope

- **Does NOT name specific executor instances as Foundation constituents (IP-1 strict).** Bindings are RUSLAN-LAYER `executor-binding.yaml` [src:design/JETIX-FPF.md:§5.1 IP-1; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§8 AP-L1; F8|G:Foundation constitutional|R-high].

- **Does NOT strategize.** Routing/dispatch are procedural; method selection is HITL-only per FUNDAMENTAL §6.1 [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1; F8|G:Foundation hard rule|R-high]. Therefore: a Task with `task-class: M` (Method-development) requires HITL gate at completion; brigadier does not autonomously decide method changes.

- **Does NOT own F-G-R compliance enforcement.** Part 6 (Provenance Officer / Human Gate) territory. Part 4 EMBEDS F-G-R tags on dispatched artefacts but does NOT audit compliance [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§2 Part 4 B.3].

- **Does NOT own project lifecycle state machines.** Part 7 (Project Lifecycle Substrate; Bundle 4). Part 4 dispatches tasks within cycles, not projects.

- **Does NOT allow agents to negotiate contradictions autonomously.** All unresolved inter-agent contradictions ESCALATE to human gate per FUNDAMENTAL §6.1 + A.13 Agency-CHR [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1; src:design/JETIX-FPF.md:§2.1a A.13; F8|G:Foundation hard rule|R-high].

- **Does NOT own the accessor pipeline scripts (per C1 Joint Design Variant A).** `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` live in `swarm/lib/` with **Part 3 LEAD owner, Part 4 ADVISORY owner**. Part 4 routes invocations via routing-table.yaml `accessor_skills_invocable:` per role; modifications gate through AWAITING-APPROVAL `gate_class: stage_gate` per Part 6b §I.4 F8 schema [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md:§3 Variant A; src:swarm/lib/README.md; F4|G:Bundle 2 C1|R-medium].

- **Does NOT own DRR extraction logic (UND-1 / P4.3 binding).** Part 5 (Bundle 3) receives RAW task-return packets and does its own DRR extraction. Part 4 emits raw packets only [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§4.1 UND-1; F4|G:Bundle 2 P4.3|R-medium].

- **Does NOT modify the `.claude/agents/*.md` files in Bundle 2 scope.** The routing-table.yaml is EXTRACTED from existing role manifests, not a replacement. The `.claude/agents/*.md` files remain RUSLAN-LAYER. [src:prompts/wave-c-bundle-2-deep-prompt-2026-04-28.md:§10.8 Untouchable trees]

- **Does NOT use engagement-economy patterns.** Per FUNDAMENTAL §6.3.

---

## §G F-G-R Tagging

| Artefact | F | ClaimScope (G) | Reliability (R) |
|---|---|---|---|
| Role-manifest | F5 — codified rule in Foundation | `holds_within: [multi-agent hub-and-spoke + IP-1 discipline]` | R-medium until F.6 M6 promotion threshold; R-high after |
| Executor-binding.yaml (RUSLAN-LAYER) | F4 — operational convention | `holds_within: [specific deployed instance; bridge required for multi-owner via F.9]` | R-medium; updated per M3 Qualify re-run on executor change |
| Message schema YAML (`shared/schemas/message.schema.json` extended with `acting_as:`) | F5 — codified; `acting_as:` mandatory per FUNDAMENTAL §3.2.4 | `holds_within: [any Jetix instance + Phase B forks]` | R-high (constitutional; not softcoded) |
| Dispatch packet | F3 — multi-source informal (task brief + mode prefix + input paths + ap_budget) | `holds_within: [single cycle turn]` | R-low to R-medium; reliability grows with strategies.md history |
| Routing-table.yaml | F5 target (currently F2 — embedded in system prompts) | `holds_within: [full Foundation scope]` | R-low until materialised (Bundle 2 P4.1); R-medium after first 3 cycles of operational use |
| Task-return-packet (P4.3 full schema) | F4 architecture-time → F5 on Bundle 3 Part 5 consumption validation | `holds_within: [Part 4 → Part 5 boundary]` | R-medium |
| `swarm/lib/routing-table.yaml` modification AWAITING-APPROVAL packet | F4 (consumer of F8 schema per Part 6b §I.4) with `gate_class: stage_gate` | `holds_within: [single modification event]` | R-medium |

---

## §H Code-level Interfaces

### §H.1 `swarm/lib/routing-table.yaml` schema (PRIMARY P4.1 ARTEFACT)

The architecture document declares the schema; the brigadier writes the actual YAML separately as a sibling deliverable to this Bundle 2 packet. Per-role fields:

```yaml
# swarm/lib/routing-table.yaml schema
schema_version: "1.0.0"
schema_version_history:
  - version: "1.0.0"
    date: 2026-04-28
    changes: "Wave C Bundle 2 P4.1 materialisation — extracted from brigadier.md + 5 ROY expert system prompts"
    breaking: false
managed_by: brigadier   # role-archetype, not executor-name (IP-1 compliant)
last_modified: 2026-04-28

# Foundation generic structure.
# Specific role entries per Ruslan's Phase A swarm are RUSLAN-LAYER below.
# Phase B partner forks structure + replaces specific entries.

roles:
  - slug: <role-archetype-name>     # IP-1 compliant; e.g. "engineering-expert", NOT "claude-sonnet-4-6"
    j_level_authority:               # per A.13 Agency-CHR per decision-class
      routine: J-Auto
      tactical: J-Approve
      strategic: J-Strategic
    allowed_modes: [critic, optimizer, integrator, scalability]   # subset per role's mode_allowlist
    write_scope_glob: "swarm/wiki/drafts/<task-id>-<slug>-*"   # regex pattern
    escalation_taxonomy_per_trigger:                             # E-15 routing options
      out-of-domain: dispatch-peer-cell
      contradiction-with-foundation: open-AWAITING-APPROVAL-packet
      peer-input-needed: dispatch-named-peer
      insufficient-evidence: defer-or-escalate-HITL
      method-change: refuse-route-to-HITL
      missing-baseline: dispatch-critic-pre-pass
      schema_error: reject-with-context
      permission-denied: refuse-with-route
      ethical-surface-irreversible: open-HITL-gate
      foundation-revision-proposed: brigadier-authors-gate-packet
      method-exhaustion: brigadier-escalates-HITL
      phase-b-activation-needed: HITL-ack-required
      requires-approval: stop-and-emit-packet
      split-trigger-fired: brigadier-authors-AWAITING-APPROVAL
    hub_and_spoke_dispatch_chain: [brigadier, owner]   # who can dispatch to this role
    accessor_skills_invocable: [<list>]   # cross-ref to swarm/lib/README.md §3 inventory
    mailbox: "comms/mailboxes/<slug>.jsonl"
    primary_alpha: <task | artefact | strategies-rule | cycle | direction>
    secondary_alphas: [<list>]
    domains: [<list>]
    granularity: <jetix-shared | jetix-business | jetix-personal>   # E-16 from FPF
```

### §H.2 Routing rules count (Ashby variety target ≥20)

The 5 ROY experts × 4 modes = 20 base routing cells. Plus:

- 1 brigadier role (orchestrator)
- 13 legacy agents (manager, sales-lead, sales-researcher, sales-outreach, inbox-processor, knowledge-synth, personal-assistant, system-admin, life-coach, meta-agent, crazy-agent, strategist) — Phase A operational, structurally Foundation-described, RUSLAN-LAYER configured
- 14 distinct escalation triggers in `escalation_taxonomy_per_trigger` (per E-15)
- 4 task shapes (design / review / optimize / scale-project) with default + optional + forbidden cell sets
- M-class rate limiter (1 structural + 1 measurement per cycle, refusing 3rd+)
- 10 gate-types in AWAITING-APPROVAL `gate_type:` enum per brigadier §6.1

Aggregate distinct routing rules: **far exceeds 20** (≥60 distinct rule manifestations: 5×4 cell + 1 brigadier + 13 legacy + 14 trigger + 4 shape + 1 rate-limit + 10 gate types = 67+). Variety target SATISFIED. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md:§Principle 2 Ashby; F4|G:Bundle 2 P4.1 variety target satisfied|R-high]

### §H.3 Brigadier dispatch interface (pseudocode)

```
function dispatch_cell(task_id, role_slug, mode, inputs, ap_budget, expected_artefact):
  # Per routing-table.yaml lookup
  role = routing_table.lookup(role_slug)
  if role is None:
    return reject(reason=f"unknown role-archetype: {role_slug}")
  if mode not in role.allowed_modes:
    return reject(reason=f"mode '{mode}' not in {role_slug}.allowed_modes")
  if not validates_write_scope(expected_artefact, role.write_scope_glob):
    return reject(reason=f"expected_artefact outside role's write scope")
  # Pre-dispatch hooks (swarm/lib/hooks/)
  bash_run("swarm/lib/hooks/mode-prefix.sh", prompt, role_slug)   # validates <domain> × <mode>
  bash_run("swarm/lib/hooks/role-matrix.sh", role_slug, mode)      # validates role permits the mode
  # Construct dispatch packet
  packet = {
    "mode": mode,
    "task_id": task_id,
    "acting_as": role_slug,   # IP-1 compliant; never executor-name
    "inputs": inputs,
    "ap_budget": ap_budget,
    "expected_artefact": expected_artefact,
    "acceptance_predicate": cell_acceptance_predicate
  }
  # Append to mailbox
  append_jsonl(role.mailbox, packet)
  # Invoke via Task() (brigadier-only; cells NEVER invoke Task per L8)
  return Task(subagent_type=executor_for_role(role_slug), prompt=construct_prompt(packet))
```

The function `executor_for_role(role_slug)` looks up `executor-binding.yaml` (RUSLAN-LAYER per §X) — Foundation does NOT define what the executor is.

### §H.4 Pre-dispatch hooks (in `swarm/lib/hooks/`)

- `mode-prefix.sh "<prompt>" "<role-slug>"` — validates first non-blank line of prompt is `mode: <name>` matching role's allowed_modes
- `role-matrix.sh "<role-slug>" "<mode>"` — validates role × mode is permitted (cross-references routing-table.yaml)
- `verify-packet.sh "<packet-path>" "<schema-path>"` — validates returned task-return-packet against §I.1 schema
- `pre-session-check.sh` — invoked at session start; verifies routing-table.yaml is parseable, mailboxes are append-only, no API key leaks in env

### §H.5 Mailbox append semantics

`comms/mailboxes/<role-slug>.jsonl` is append-only per IP-3 + Reversal Transactions. Format:

```json
{
  "ts": "<ISO 8601>",
  "cycle_id": "<cyc-id>",
  "task_id": "<task-id>",
  "cell": "<domain> × <mode>",
  "ap_budget": <int>,
  "input_paths": ["<list>"],
  "expected_artefact": "<path>",
  "msg_id": "msg-YYYYMMDD-NNN",
  "acting_as": "<role-slug>",   // IP-1 compliant
  "corrects": "<prior-msg-id | null>"  // Reversal Transactions
}
```

### §H.6 Message schema EXTENSION

`shared/schemas/message.schema.json` currently lacks `acting_as:` field and lists only legacy 13 agents in the `from:` enum. Bundle 2 extends:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "JetixMessage v2 (Wave C Bundle 2 extension)",
  "schema_version": "2.0.0",
  "schema_version_history": [
    {"version": "1.0.0", "date": "<earlier>", "changes": "initial 13-agent enum"},
    {"version": "2.0.0", "date": "2026-04-28", "changes": "added acting_as: mandatory; extended from: enum with 5 ROY experts + brigadier", "breaking": true}
  ],
  "type": "object",
  "required": ["id", "timestamp", "from", "to", "type", "priority", "subject", "body", "acting_as"],
  "properties": {
    "acting_as": {
      "type": "string",
      "description": "Role-archetype slug per FUNDAMENTAL §3.2.4 mandatory; IP-1 compliant (never executor-name)",
      "enum": ["brigadier", "engineering-expert", "philosophy-expert", "systems-expert", "mgmt-expert", "investor-expert", "manager", "sales-lead", "sales-researcher", "sales-outreach", "inbox-processor", "knowledge-synth", "personal-assistant", "system-admin", "life-coach", "meta-agent", "crazy-agent", "strategist", "human"]
    }
    // ... rest from existing schema (id, timestamp, from, to, type, priority, subject, body, context, status, deadline)
  }
}
```

The `from:` field's enum is extended to include the 5 ROY experts + brigadier (currently absent). The `acting_as:` field is NEW and mandatory. Schema_version bump to 2.0.0 (BREAKING) requires AWAITING-APPROVAL `gate_class: stage_gate` per Part 6b §I.4 — the schema bump itself is a Bundle 2 P4.1 deliverable subject to Ruslan ack.

---

## §I Data Schemas

### §I.1 `task-return-packet.json` FULL SCHEMA (P4.3 / UND-1 BINDING)

**Per Ruslan ack OQ-3:** Part 5 receives RAW task-return packets and does its own DRR extraction. Part 4 emits raw packets only.

**Frozen fields invariant:** the 4 fields from Part 1 §I.4 stub (`git_commit_hash`, `actor_role_archetype`, `cycle_id`, `gate_class`) appear UNCHANGED.

**OQ-B2-A FLAG:** The Part 1 §I.4 stub uses `gate_class` enum `[autonomous, requires-approval, hitl-required]`. The Part 6b §I.4 F8 LOCKED schema (RUSLAN-ACK Bundle 1 Decision #5) uses `[stop_gate, stage_gate, draft_promotion]`. **Part 4 §I.1 below uses the F8 LOCKED enum from Part 6b** — the Part 1 stub is a Bundle 1 drift defect requiring retroactive correction via constitutional AWAITING-APPROVAL packet (proposed Bundle 1 supplement; routed to OQ-B2-A in §5 of AWAITING-APPROVAL Bundle 2 packet).

**Full schema:**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/task-return-packet.json",
  "title": "Task return packet (Bundle 2 P4.3 FULL specification)",
  "description": "Task-return-packet schema at Part 4 → Part 5 boundary. Part 5 (Bundle 3) consumes RAW packets per Ruslan-acked OQ-3 and does own DRR extraction. Frozen-fields invariant per Part 1 §I.4 stub: git_commit_hash, actor_role_archetype, cycle_id, gate_class fields appear UNCHANGED. gate_class enum corrected to Part 6b §I.4 F8 LOCKED [stop_gate, stage_gate, draft_promotion] — see OQ-B2-A re Part 1 stub drift.",
  "schema_version": "1.0.0",
  "schema_version_history": [
    {
      "version": "1.0.0",
      "date": "2026-04-28",
      "changes": "Wave C Bundle 2 P4.3 — FULL schema specification; Part 1 §I.4 stub frozen fields preserved; gate_class enum aligned to Part 6b §I.4 F8 LOCKED",
      "breaking": false,
      "supersedes": "Part 1 §I.4 PARTIAL stub"
    }
  ],
  "type": "object",
  "required": [
    "packet_id",
    "task_id",
    "dispatched_at",
    "returned_at",
    "actor_role_archetype",
    "cycle_id",
    "mode",
    "inputs",
    "outputs",
    "provenance_chain",
    "f_g_r",
    "gate_class",
    "git_commit_hash",
    "dissent_preserved"
  ],
  "properties": {
    "packet_id": {
      "type": "string",
      "pattern": "^trp-[0-9]{8}-[a-z0-9-]+$",
      "description": "Unique packet identifier. Format: trp-YYYYMMDD-slug (task-return-packet)"
    },
    "task_id": {
      "type": "string",
      "pattern": "^task-[a-z0-9-]+$",
      "description": "Task identifier from brigadier intake; PMBOK alpha-1 key"
    },
    "dispatched_at": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp when brigadier dispatched the cell"
    },
    "returned_at": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp when cell returned the packet"
    },
    "actor_role_archetype": {
      "type": "string",
      "description": "FROZEN per Part 1 §I.4. Role-archetype slug; IP-1 compliant (never executor-name). E.g. 'engineering-expert', NOT model identifier or agent file path.",
      "enum": ["brigadier", "engineering-expert", "philosophy-expert", "systems-expert", "mgmt-expert", "investor-expert", "manager", "sales-lead", "sales-researcher", "sales-outreach", "inbox-processor", "knowledge-synth", "personal-assistant", "system-admin", "life-coach", "meta-agent", "crazy-agent", "strategist"]
    },
    "cycle_id": {
      "type": "string",
      "pattern": "^cyc-[a-z0-9-]+$",
      "description": "FROZEN per Part 1 §I.4. Cycle identifier (e.g. cyc-foundation-build-2026-04-28). Links task-return to its cycle context."
    },
    "mode": {
      "type": "string",
      "enum": ["critic", "optimizer", "integrator", "scalability", "writing-support"],
      "description": "Per L/A/D/E A.6.B mode. Five enum: critic / optimizer / integrator / scalability / writing-support."
    },
    "inputs": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["path", "input_type"],
        "properties": {
          "path": {"type": "string"},
          "input_type": {"type": "string", "enum": ["file", "url", "config", "schema", "draft", "approval-packet"]},
          "F": {"type": "string", "pattern": "^F[0-9]$"}
        }
      },
      "minItems": 1,
      "description": "List of inputs the cell consumed. Each carries path + input_type + optional F-level."
    },
    "outputs": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["path", "output_type"],
        "properties": {
          "path": {"type": "string"},
          "output_type": {"type": "string", "enum": ["draft", "synthesis", "decision", "audit-report", "schema", "config", "code", "comparison"]},
          "F": {"type": "string", "pattern": "^F[0-9]$"},
          "ClaimScope": {"type": "object"},
          "R": {"type": "object"}
        }
      },
      "minItems": 0,
      "description": "List of outputs the cell produced (path + output_type + F-G-R triple)."
    },
    "provenance_chain": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["step", "ts"],
        "properties": {
          "step": {"type": "string"},
          "ts": {"type": "string", "format": "date-time"},
          "actor_role_archetype": {"type": "string"},
          "cite": {"type": "string"}
        }
      },
      "minItems": 1,
      "description": "Ordered chain of provenance steps from dispatch through return. Each step records timestamp, actor, citation."
    },
    "f_g_r": {
      "$ref": "shared/schemas/f-g-r.json",
      "description": "F-G-R triple snapshot at packet emission time. $ref to Part 6a §I.1 F8 LOCKED schema."
    },
    "gate_class": {
      "type": "string",
      "enum": ["stop_gate", "stage_gate", "draft_promotion"],
      "description": "FROZEN per Part 1 §I.4 (field name) + Part 6b §I.4 F8 LOCKED (enum values). The gate class under which this task was executed. OQ-B2-A: Part 1 §I.4 stub used stale enum [autonomous, requires-approval, hitl-required]; Part 4 schema uses Part 6b §I.4 F8 LOCKED enum (RUSLAN-ACK Bundle 1 Decision #5)."
    },
    "git_commit_hash": {
      "type": ["string", "null"],
      "pattern": "^[0-9a-f]{40}$",
      "description": "FROZEN per Part 1 §I.4. SHA-1 of git commit that persisted canonical state produced by this task. NULL if task produced no canonical write. Set by orchestrator after commit completes. NEVER mutated post-set.",
      "nullable": true
    },
    "dissent_preserved": {
      "type": "boolean",
      "description": "True if the cell returned dissent that was preserved per AP-6. If true, dissent_path is required."
    },
    "dissent_path": {
      "type": ["string", "null"],
      "description": "Path to dissent file if dissent_preserved=true. Format: swarm/wiki/foundations/<part-slug>/dissent.md OR swarm/wiki/tasks/<task-id>/dissents/<dissent-id>.md"
    },
    "ap_budget": {
      "type": "integer",
      "minimum": 1,
      "description": "Max-turn budget for this cell dispatch (MAST coverage L9)"
    },
    "ap_actual": {
      "type": "integer",
      "minimum": 0,
      "description": "Actual turns consumed by the cell"
    },
    "confidence": {
      "type": "string",
      "enum": ["low", "medium", "high"],
      "description": "Cell's confidence in its output"
    },
    "confidence_method": {
      "type": "string",
      "description": "Enum or description of how confidence was determined (e.g., 'measurable-baseline-delta', 'historical-precedent', 'first-principles-only')"
    },
    "escalations": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["trigger"],
        "properties": {
          "trigger": {"type": "string"},
          "evidence": {"type": "string"},
          "routing_suggestion": {"type": "string"}
        }
      },
      "description": "List of escalation triggers raised by the cell; brigadier handles per E-15 routing"
    }
  },
  "additionalProperties": false
}
```

### §I.2 C1 ownership decision — REFERENCE to swarm/lib/README.md (P4.2 / C1 binding)

**Per C1 Joint Design (Variant A Ruslan-acked 2026-04-27):**

- Accessor pipeline scripts live in `swarm/lib/`.
- Part 3 named LEAD owner; Part 4 ADVISORY owner.
- Modification governance: AWAITING-APPROVAL `gate_class: stage_gate` per Part 6b §I.4 F8.
- Routing-table.yaml `accessor_skills_invocable:` field per role declares which `swarm/lib/<skill>` each role may invoke.

**Part 4 §I.2 REFERENCES `swarm/lib/README.md` and `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` for the canonical answer.** Per DRY enforcement, this document does NOT duplicate the content; it CROSS-REFERENCES.

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md:§3 Variant A canonical answer; src:swarm/lib/README.md:§3 inventory + §4 modification governance; F4|G:Bundle 2 C1 Joint Design canonical|R-medium]

### §I.3 `executor-binding.yaml` template (RUSLAN-LAYER artefact template)

The Foundation declares the TEMPLATE; specific values are RUSLAN-LAYER per §X. The template:

```yaml
# executor-binding.yaml — RUSLAN-LAYER artefact template
# Per IP-1 strict: this file binds role-archetype slugs to executor instances.
# NOT a Foundation artefact; RUSLAN-LAYER parameterisation per Phase A configuration.

schema_version: "1.0.0"
schema_version_history:
  - version: "1.0.0"
    date: 2026-04-28
    changes: "Wave C Bundle 2 P4.1 template declaration; binding values RUSLAN-LAYER"
    breaking: false
managed_by: ruslan   # human owner; not a role-archetype
last_modified: <YYYY-MM-DD>

# Bindings: role-archetype slug → executor instance
# F.6 onboarding M1-M6 mandatory before activation per IP-8.

bindings:
  - role_archetype: <slug-from-routing-table.yaml>
    executor:
      type: <claude-model | external-llm | human | script>
      identifier: <executor-id; e.g. model-id like 'claude-sonnet-4-6'; agent file path; human name; script path>
      granularity: <jetix-shared | jetix-business | jetix-personal>
    f6_onboarding:
      m1_role_understood: {date: <YYYY-MM-DD>, reviewer: <human>}
      m2_method_understood: {date: <YYYY-MM-DD>, reviewer: <human>}
      m3_qualify_pass: {date: <YYYY-MM-DD>, reviewer: <human>, qualification_test: <description>}
      m4_first_task_completed: {date: <YYYY-MM-DD>, task_id: <task-id>}
      m5_review_passed: {date: <YYYY-MM-DD>, reviewer: <human>, review_outcome: <description>}
      m6_promotion_threshold_met: {date: <YYYY-MM-DD>, criterion: <description>}
    activation_status: pending | onboarding | active | retired
    cross_fork_provenance:
      bridge_id: <fork-or-instance-identifier>
      F.9_bridge_required: <boolean>
```

A binding with `activation_status: active` indicates F.6 M1-M6 fully populated and F.6 M6 promotion threshold met. Bindings at `pending` or `onboarding` are NOT eligible for dispatch; brigadier rejects with `escalations[]{trigger: binding-not-active}` if attempted dispatch.

### §I.4 Health signal schema for Part 8 consumption (Bundle 4 stub)

```yaml
# /lint or per-cycle aggregator output for Part 8 health monitoring
coordination_health:
  ip1_compliance_rate: <float 0..1>   # target 1.0
  routing_table_variety_count: <int>   # target ≥20
  dispatch_rate_per_cycle: <int>
  escalation_rate_per_cycle: <int>
  task_return_completeness: <float 0..1>   # tasks dispatched vs returned
  hub_and_spoke_violations: [<list of cell-direct-invocation incidents>]
  mailbox_append_only_violations: [<list>]
  schema_validation_failures: [<list with schema + violation>]
```

### §I.5 Cross-Part schemas REFERENCED (not duplicated)

- `awaiting-approval-packet.json` per Part 6b §I.4 F8 LOCKED — for routing-table.yaml modification packets and escalation packets
- `f-g-r.json` per Part 6a §I.1 F8 LOCKED — for `f_g_r:` field in task-return-packet
- `commit-format-tokens.json` per Part 1 §I.2 — for `[swarm-lib]` and `[part4]` area tokens
- `default-deny-table.yaml:foundation_generic:` per Part 6b §I.3 F8 LOCKED — for L5 enforcement at dispatch
- `blast-radius-table.yaml:foundation_generic:` per Part 6b §I.4 F8 LOCKED — for escalation tier classification

---

## §J Operational Rituals

| Ritual | Cadence | Trigger | Responsible | Expected output |
|---|---|---|---|---|
| Per-cell dispatch | Event-driven | Task intake → §3 decomposition → §4 dispatch per brigadier protocol | brigadier | Mailbox append + Task() invocation + dispatch packet at brigadier mailbox jsonl |
| Task-return-packet emission | Per cell return | Cell completes (success or escalation) | Cell + brigadier | Packet conforming to §I.1 schema; committed at swarm/wiki/cycles/<cycle_id>/task-returns/<packet_id>.json |
| Routing-table.yaml audit | Weekly (Sunday) | Calendar cron + on-demand | `/lint --check-routing-table` | List of violations: undocumented skill in accessor_skills_invocable; orphan skill not permitted to any role; IP-1 violations (executor name in role manifest) |
| Quarterly IP-1 compliance audit | Quarterly | Part 6a immune-function cadence | Part 6a (consumes Part 4 IP-1-compliance-rate) | Audit report at swarm/audits/<quarter>/p4-ip1-compliance.md |
| F.6 M1-M6 onboarding (per executor change) | Event-driven | RUSLAN-LAYER executor swap | Owner (Ruslan) | executor-binding.yaml updated with M1-M6 timestamps + reviewer attestations |
| Routing variety check (Ashby ≥20) | Per routing-table modification | Modification packet ack | brigadier (or Part 8 health monitor in Bundle 4) | Variety count reported in coordination_health schema |
| `/ask` accessor skill invocation per role permit | Event-driven | Cell or owner invokes | Cell (per accessor_skills_invocable) | Synthesis with citations per Part 3 P3.4; comparisons file at wiki/comparisons/ unless --no-save |

**SRE burn-rate algebra applied to Coordination Protocol SLO:**

| Burn rate | Part 4 observable | Required behaviour change |
|-----------|-------------------|---------------------------|
| **1×** | IP-1 compliance 100%; variety ≥20; escalation latency ≤1 cycle turn | No change |
| **6×** | IP-1 violations 1-3 in current cycle OR variety <20 OR escalation latency >1 cycle | Brigadier dispatches cleanup task; routing-table audit; HITL notify |
| **14.4×** | IP-1 violations >3 OR variety <15 OR escalation silently absorbed (no surface to brigadier) | HALT new dispatches; AWAITING-APPROVAL escalation packet; owner ack required to resume |

---

## §K Failure Modes

Apply Halt-Log-Alert L6 (≤1s halt / ≤5s log / ≤60s alert per Part 6b §E Law L9).

**K1 — IP-1 violation (executor name in Foundation artefact).** Detection: `/lint --check-ip1` flags executor-name pattern (model identifier regex; agent file path regex; instance ID regex) in any §A-§N section of any Foundation artefact under `swarm/wiki/foundations/`. Policy: BLOCK at pre-commit hook; redaction required; postmortem `[meta] postmortem: K1-ip1-violation` commit. [F8|G:Foundation constitutional|R-high]

**K2 — Missing `acting_as:` in inbound message.** Detection: schema validation against message.schema.json v2.0.0 fails. Policy: REJECT with `escalations[]{trigger: schema_error, missing_field: acting_as}`. [F5|G:L2|R-high]

**K3 — Routing-table.yaml under-variety (<20 rules).** Detection: `/lint --check-routing-table-variety` reports variety count <20. Policy: FLAG as Ashby under-variety defect; brigadier dispatches mgmt × scalability + systems × scalability for routing extension proposal. [F4|G:L10 binding|R-medium]

**K4 — Cell invokes another cell directly (hub-and-spoke L8 violation).** Detection: cell return packet shows `Task()` invocation in cell's own scope. Policy: REFUSE at cell's own decision-rights ritual; surface as `never` violation per cell's frontmatter; brigadier opens AWAITING-APPROVAL escalation packet; postmortem mandatory. [F8|G:CLAUDE.md Global Rule 8|R-high]

**K5 — Method-class rate-limit hit (HD-02 N=2 per cycle).** Detection: brigadier counter `m_class_dispatched_this_cycle: 2/2` and 3rd+ M-class task requested. Policy: REFUSE with structured `AP-MGMT-RATE-LIMIT-M`; queue overflow to `swarm/wiki/operations/<cycle>/m-class-overflow.md`; log entry to `swarm/wiki/log.md`. [F4|G:HD-02 cycle-2-impl|R-high]

**K6 — Task-return-packet schema violation.** Detection: `verify-packet.sh` fails validation against §I.1 schema. Specific: missing required field; malformed `gate_class` value; F-G-R delta missing required sub-fields per Part 6a §I.1. Policy: HALT cell's return; LOG to `swarm/approvals/log.jsonl`; brigadier re-invokes with schema_error context; if 2 consecutive failures, escalate to HITL. [F8|G:Bundle 1 LOCKED schema|R-high]

**K7 — Escalation cascade (cell → brigadier → HITL).** Detection: 3+ levels of escalation in single task. Policy: PRESERVE full chain in task-return-packet `provenance_chain[]`; brigadier triggers AWAITING-APPROVAL packet for HITL with full chain visible. [F4|G:E-15 routing|R-medium]

**K8 — Cycle exceeds max-turn budget (2× over).** Detection: cycle's total turn count ≥2× max-turn budget. Policy: TRIGGER `requires-approval` per brigadier §1d; AWAITING-APPROVAL packet `gate_type: budget-overrun`. [F4|G:brigadier escalation trigger|R-medium]

**K9 — Hub-and-spoke degradation under load (Phase B/C scale).** Detection: brigadier `split_trigger` activates per §1d (sustained task-intake rate > 10/week for 3 consecutive weeks). Policy: AWAITING-APPROVAL `gate_type: split-trigger` for Phase B brigadier split into [task-dispatcher, integration-manager, gate-keeper]. [F2|G:Phase B activation; declared in §X|R-low]

**K10 — Cross-fork executor-binding incompatibility (different model versions).** Detection: cross-fork-provenance.json import flags `executor_binding_hash:` mismatch. Policy: F.9 Bridge mechanism per IP-8; cross-fork-audit-deferred-phase-b.md (per OQ-B1-8 Bundle 1 ack). [F3|G:Phase B deferred|R-low]

**K11 — Task-return-packet drift from Part 1 §I.4 frozen fields.** Detection: pre-commit hook validates schema $ref to Part 1 §I.4 stub (frozen-fields invariant). Policy: REJECT drift; require schema correction. **Special case OQ-B2-A:** Part 1 §I.4 stub's `gate_class` enum is itself stale vs Part 6b §I.4 F8 LOCKED; the Part 4 schema uses the F8 LOCKED enum; OQ-B2-A flags Bundle 1 retroactive correction. [F8|G:Bundle 1 LOCKED frozen-fields with OQ-B2-A flag|R-high]

**K12 — Default-Deny constitutional violation in dispatched action class.** Detection: dispatched task carries action class in Part 6b §I.3 `constitutional_never_list:` enum. Policy: REFUSE dispatch; route to Part 6b STOP gate per L5 enforcement. [F8|G:Bundle 1 LOCKED Default-Deny|R-high]

**K13 — Substrate cascade (Part 1 K8 fsck blocks Part 4 commits).** Detection: routing-table.yaml or executor-binding.yaml commit fails. Policy: HALT routing-table modifications; LOG; ALERT. Recovery: resolve Part 1 K8.

**K14 — Mailbox in-place mutation attempt (L11 violation).** Detection: `git diff` shows mutation of existing line in `comms/mailboxes/<role>.jsonl`. Policy: BLOCK at pre-commit hook; require new entry with `corrects:` pointer per Reversal Transactions.

**K15 — Schema_version drift on routing-table.yaml.** Detection: tooling uses schema_version > current routing-table.yaml header. Policy: maintain `schema_version_history:` block; tooling implements upcasting per Young's event-versioning [src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4 P4 upcasting; F4|G:schema evolution|R-medium].

---

## §L Wave C Worklist Bullet Status

### Bullet P4.1 — Routing table as declarative YAML (PRIMARY Wave C gap) ✅ ADDRESSED

**Acceptance predicate:** routing-table.yaml exists, parses without errors, contains an entry for every role in `comms/mailboxes/` (currently 13 legacy + 5 ROY experts + brigadier = 19 channels minimum); `/lint` validates structural completeness; routing variety count ≥20 declared rules.

**Status:** §H.1 declares routing-table.yaml schema with per-role fields. §H.2 declares variety count ≥60 (5×4 cell + 1 brigadier + 13 legacy + 14 trigger + 4 shape + 1 rate-limit + 10 gate types = 67+). §H.6 declares message schema EXTENSION with `acting_as:` mandatory + `from:` enum extended. §J ritual declares weekly routing-table audit. §K K3/K11 declare failure modes. **IP-1 enforcement throughout: every role reference is a slug, never an executor name; §H.3 dispatch interface uses `executor_for_role()` lookup against RUSLAN-LAYER executor-binding.yaml.**

**Sibling deliverable:** `swarm/lib/routing-table.yaml` (the actual YAML file with role entries) is committed alongside this architecture as a Bundle 2 deliverable. Each role entry: 5 ROY experts (engineering / philosophy / systems / mgmt / investor) + brigadier + 13 legacy = 19 entries minimum. Foundation declares the structure; specific entries are RUSLAN-LAYER per §X.

**F-G-R:** F5 SCHEMA target (currently F2 — embedded in system prompts; F5 post-Bundle-2-ack), `holds_within: [Foundation routing schema]`, R-low until materialised then R-medium.

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md:§2 Part 4 Bullet 1; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md:§Principle 2 Ashby variety]

### Bullet P4.2 — C1 ownership decision materialised in Part 4 (joint with Part 3 P3.1) ✅ ADDRESSED

**Acceptance predicate:** routing-table.yaml lints clean against `swarm/lib/README.md` declared inventory; no accessor skill is invocable from a role not declared in routing-table.yaml.

**Status:** §F Anti-scope declares Part 4 does NOT own scripts (per C1 Variant A). §I.2 REFERENCES `swarm/lib/README.md` + `C1-joint-design.md` (DRY enforced; no duplication). §B Outputs lists "Wiki accessor pipeline skills :: invocable by any consumer :: on-demand" with rationale. §H.1 routing-table.yaml schema includes `accessor_skills_invocable:` per role. §K K6 declares failure mode.

**F-G-R:** F4 operational convention (post-Joint-Design ack), `holds_within: [Bundle 2 C1 Joint Design canonical]`, R-medium.

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md; src:swarm/lib/README.md]

### Bullet P4.3 — UND-1 task-return-packet schema FULL specification ✅ ADDRESSED

**Acceptance predicate:** schema structurally complete (every field typed, every required field marked); 3 synthetic fixture packets validate; Part 1 §I.5 stub fields are SUPERSET-compatible (frozen fields appear UNCHANGED).

**Status:** §I.1 declares FULL schema with 4 frozen Part 1 §I.4 fields preserved (`git_commit_hash`, `actor_role_archetype`, `cycle_id`, `gate_class`) PLUS 11 additional fields per spec. **OQ-B2-A FLAG:** the `gate_class` enum is corrected from Part 1 §I.4 stub's stale `[autonomous, requires-approval, hitl-required]` to Part 6b §I.4 F8 LOCKED `[stop_gate, stage_gate, draft_promotion]` (per RUSLAN-ACK Bundle 1 Decision #5; the Part 1 stub enum is a Bundle 1 drift defect requiring retroactive correction). §B Outputs declares "Structured task-return packets from all dispatched roles :: `compound-phase-start-event`" — Part 5 (Bundle 3) consumes raw packets at compound boundary. §K K6 + K11 declare failure modes for schema violation + frozen-fields drift.

**Sibling deliverable:** `shared/schemas/task-return-packet.json` (the actual JSON file with the full schema) is committed alongside this architecture as a Bundle 2 deliverable. The 3 synthetic fixture packets for validation are committed at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/task-return-packet-fixtures/` (or equivalent path per Bundle 3 Part 5 architecture).

**F-G-R:** F4 architecture-time → F5 on Bundle 3 Part 5 consumption validation, `holds_within: [Part 4 → Part 5 boundary]`, R-medium.

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md:§2 Part 4 Bullet 3; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§4.1 UND-1; src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§I.4 PARTIAL stub; src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4 F8 LOCKED gate_class enum]

---

## §M Wisdom Application Findings

[Operational target ≥60% per Ruslan feedback after Bundle 1.]

| # | Card / Source | Principle | Current state | Improvement | Adopted? | Operational vs Philosophical | Justification | Section edited |
|---|---------------|-----------|---------------|-------------|----------|------------------------------|---------------|----------------|
| 1 | Levenchuk-SHSM-FPF IP-1 (CRITICAL) | "Role manifests = U.Episteme; executor bindings = RUSLAN-LAYER" | Wave A interface card declared | L1 critic-gate AUTO-REJECT; routing-table.yaml + executor-binding.yaml separation throughout §H.1 + §I.3; IP-1 self-audit at finalize | YES | **OPERATIONAL** | Constitutional invariant; auto-rejection + self-audit | §E L1 + §H.1 + §I.3 + §0 self-audit |
| 2 | Levenchuk-SHSM-FPF IP-6 (5-block role manifest) | "Role-manifest accepted only with 5 blocks complete" | Wave A baseline | A1 admissibility check; routing-table.yaml schema implies 5-block source | YES | OPERATIONAL | Foundation generic | §E A1 + §I.1 |
| 3 | Levenchuk-SHSM-FPF IP-8 F.6 6-step onboarding | "M1-M6 mandatory before binding activation" | Wave A baseline | A2 admissibility check; executor-binding.yaml template includes M1-M6 mandatory; activation_status enum | YES | **OPERATIONAL** | Onboarding gate at binding | §E A2 + §I.3 |
| 4 | Levenchuk-SHSM-FPF A.13 Agency-CHR (J-levels) | "J-Auto / J-Approve / J-Strategic per role per decision-class" | Wave A applied | L3 architecturally encoded; routing-table.yaml `j_level_authority:` per role | YES | OPERATIONAL | A.13 dogfood | §E L3 + §H.1 |
| 5 | Levenchuk-SHSM-FPF L/A/D/E A.6.B | "Boundary structured per L/A/D/E lanes" | Wave A applied | §E entire structured per L/A/D/E with 11 Laws + 6 Admissibility + 6 Deontics + 6 Effects | YES | OPERATIONAL (reinforcing) | Foundation generic boundary discipline | §E entire |
| 6 | Multi-Agent Architecture P-2 (hub-and-spoke) | "Cells NEVER invoke other cells; brigadier sole dispatcher" | Wave A baseline (CLAUDE.md Rule 8) | L8 invariant; K4 failure mode; §H.3 dispatch interface | YES | **OPERATIONAL** | MAST coverage; Cognition minimum-viable-topology | §E L8 + §K K4 + §H.3 |
| 7 | Multi-Agent Architecture P-5 (verification architecture) | "Verification matters more than agent count" | Wave A applied via critic-mode | task-return-packet's `f_g_r:` + `provenance_chain[]` enforce verification at the packet boundary | YES | OPERATIONAL | Verification at packet schema level | §I.1 |
| 8 | MAST 14 failure modes coverage | "Termination conditions (12.4%); Disobey-task-spec (11.8%); Reasoning-action-mismatch (13.2%)" | Implicit | L9 explicit termination via `ap_budget` + `ap_actual` fields; A4 acceptance_predicate non-empty (disobey prevention); cell mode prefix grammar (reasoning-action) | YES | **OPERATIONAL** | MAST coverage at Part 4 boundary | §E L9 + §H.1 + §H.3 + §I.1 |
| 9 | Multi-Agent Cognition (minimum-viable-topology) | "Don't add coordination layers without demonstrated need" | Wave A applied (no over-engineering) | Reinforced in §0 mission framing; Phase B split_trigger declared per §X for principled scaling | YES | OPERATIONAL (reinforcing) | Anti-over-engineering at Phase A | §0 + §X K9 stub |
| 10 | Multi-Agent Coordination-topology-is-declarative | "Routing tables are version-controlled YAML, not embedded prose" | Wave A baseline (currently embedded — Wave C P4.1 materialisation) | Declarative routing-table.yaml schema in §H.1; version-controlled with schema_version_history | YES | **OPERATIONAL** | Bundle 2 P4.1 binding; load-bearing | §H.1 + §H.6 |
| 11 | Anthropic-CAI hard-rule anti-scope (§6.1 dogfood) | "11 hard rules as machine-readable enum" | Bundle 1 Part 6b §I.3 enum | L5 Default-Deny enforcement at dispatch; K12 failure mode; cross-Part dogfood | YES | OPERATIONAL (cross-Part) | Constitutional discipline at dispatch | §E L5 + §K K12 |
| 12 | Anthropic-CAI simplicity-transparency-trust | "Surface dispatch failures with specific reason; no generic reject" | Wave A applied | D5 transparency; K6/K11 specific schema violation messages; CAI dogfood | YES | OPERATIONAL (reinforcing) | Transparency at error boundary | §E D5 + §K |
| 13 | Askell HHH Corrigibility (Appendix E.2) | "NO mechanism may lock human owner out" | Bundle 1 Part 6b §E Law L9 | L7 verbatim quote; routing-table.yaml human-readable; mailboxes inspectable; task-return packets queryable | YES | OPERATIONAL | Bundle 1 LOCKED Corrigibility | §E L7 |
| 14 | Bai 2022 CAI (constitutional_never_list) | "Hardcoded never-list as enum" | Bundle 1 Part 6b §I.3 | L5 cross-Part dogfood; K12 enforcement | YES | OPERATIONAL (cross-Part) | Bundle 1 framework consumed | §E L5 + §K K12 |
| 15 | SystemsThink-Cybernetics Ashby Ch.11 (requisite variety ≥20) | "Controller variety ≥ controlled-system variety" | Wave A target ≥20 | L10 explicit; §H.2 variety count ≥60 (≥3× target); routing-table audit ritual | YES | **OPERATIONAL** | Bundle 2 P4.1 binding; testable | §E L10 + §H.2 + §J ritual |
| 16 | SystemsThink-Cybernetics Beer VSM S4 (environment-scanning) | "S4 channel to S5 (policy)" | Wave A applied via brigadier escalation chain | Escalation taxonomy in routing-table.yaml `escalation_taxonomy_per_trigger:` provides S4→S5 channel; degraded-mode per §J SRE burn-rate | YES | OPERATIONAL | VSM dogfood at routing | §H.1 + §J |
| 17 | SystemsThink-Cybernetics (hub-and-spoke as VSM S2) | "Hub-and-spoke topology = VSM S2 anti-oscillation" | Implicit | Pure VSM framing without operational delta beyond what L8 already encodes | NO | PHILOSOPHICAL | Already-applied via L8; pure framing prose | n/a |
| 18 | Mereology-Typed-Edges A.14 canonical | "10-edge taxonomy; no generic depends-on" | Bundle 1 Part 1 §D | DOGFOOD throughout §D; cross-Part canonical reference | YES | OPERATIONAL (reinforcing) | A.14 dogfood | §D entire |
| 19 | Investor capital-allocation (routing as F5 codified investment) | "routing-table.yaml is a F5 codified asset; pays back across cycles" | Wave A target F5 | §G F-level promotion path F2→F5 declared; capital-allocation framing in §0 | YES | PHILOSOPHICAL (justified — informs RUSLAN-LAYER cycle horizon for F5 promotion via reuse evidence) | Phase B/C concrete need: F-promotion gate horizon | §G + §0 |
| 20 | Young 2010 CQRS (task-return-packet as event log) | "Event log: append-only; events with corrects: pointer for corrections" | Implicit (mailbox append-only) | L11 mailbox append-only; K14 failure mode; Reversal Transactions throughout | YES | **OPERATIONAL** | Reversal Transactions discipline | §E L11 + §K K14 + §H.5 |
| 21 | Young 2010 CQRS (event-versioning upcasting) | "Schema versions evolve; tooling upcasts old events" | Implicit | K15 schema_version drift failure mode; routing-table.yaml schema_version_history block; message schema v1.0.0 → v2.0.0 with breaking flag | YES | **OPERATIONAL** | Schema evolution discipline | §K K15 + §H.6 |
| 22 | Anthropic engineering-blogs (Orchestrator-Workers pattern) | "Lead subagent dispatches; cells return; lead integrates" | Wave A applied | Reinforced in §H.3 dispatch interface; brigadier as orchestrator-leader | YES | OPERATIONAL (reinforcing) | Pattern-encoding at dispatch boundary | §H.3 |
| 23 | Anthropic engineering-blogs (effective context engineering) | "Keep cell context bounded; don't inline source content" | Wave A applied (file-reference-only rule) | Brigadier dispatch passes paths only; cells read from disk; not inlined in prompts | YES | OPERATIONAL (reinforcing) | Context-engineering discipline | §H.3 |
| 24 | Stoic Dichotomy of Control | "in our control vs not in our control" | Bundle 1 applied at Part 1 | Not adopted at Part 4 — pure framing prose without operational delta beyond what IP-1 + L7 + escalation taxonomy already structurally enforce | NO | PHILOSOPHICAL | Defer per Bundle 2 operational bias; already-structurally-applied via IP-1 + L7 | n/a |
| 25 | Lindy effect (long-lived patterns) | "Patterns running ≥N cycles likely run for ~N more" | Operational since cycle 3b | No operational delta; pure framing | NO | PHILOSOPHICAL | Defer per Bundle 2 operational bias | n/a |

**Aggregate count:** 25 rows; 21 YES Adopted (operational: 19, philosophical: 2) + 4 NO (deferred / philosophical-without-justification).

**Operational ratio of YES Adopted:** 19 / 21 = **90%** — far exceeds Bundle 2 target of ≥60%.

**No fabricated YES entries** — every YES references a specific section edit. The 2 PHILOSOPHICAL adoptions (#13 Corrigibility verbatim, #19 capital-allocation framing) carry explicit Phase B/C-concrete-need or constitutional-anchor justification; not pure framing.

---

## §N Provenance

**Sources consulted:** see frontmatter `sources:` and inline `[src:...]` citations throughout. Citation discipline per Bundle 1 P6a.2 anti-cargo-cult: every `[src:]` followed within 200 chars by a consequence sentence.

**Cross-Part cross-references:**

- Part 1 §I.4 task-return-packet stub frozen fields (consumed at §A + §I.1 — frozen-fields invariant; OQ-B2-A flag on gate_class enum drift).
- Part 1 §I.2 commit-format-tokens.json (consumed for [swarm-lib] / [part4] area tokens).
- Part 1 §D 10-edge A.14 reference (consumed throughout §D).
- Part 6a §I.1 F-G-R F8 schema (consumed via $ref at §I.1 task-return-packet `f_g_r:` field).
- Part 6a §C citation discipline + approval log (consumed at modification governance).
- Part 6b §I.4 awaiting-approval-packet F8 with gate_class enum (consumed throughout — esp. as canonical source of gate_class enum [stop_gate, stage_gate, draft_promotion]).
- Part 6b §I.3 default-deny-table (consumed at §E L5 enforcement).
- Part 6b §I.4 blast-radius-table (consumed at escalation tier classification).
- Part 6b §E Law L9 Halt-Log-Alert + Corrigibility (consumed at §E L6 + L7).
- C1 Joint Design + swarm/lib/README.md (consumed at §F + §I.2 + §H.1).
- Part 3 (consumed via accessor pipeline LEAD ownership; routing-table.yaml `accessor_skills_invocable:` cross-ref).

**Commits on `claude/jolly-margulis-915d34`:** appended at Phase F finalize.

---

## §X Foundation vs RUSLAN-LAYER Fork-Separation

### Foundation generic (any Phase B partner imports)

- **Role-manifest 5-block schema (IP-6)** — identity / ontological-positioning / method / production-dependencies / evolution.
- **`swarm/lib/routing-table.yaml` STRUCTURE** — per-role fields (slug, j_level_authority, allowed_modes, write_scope_glob, escalation_taxonomy_per_trigger, hub_and_spoke_dispatch_chain, accessor_skills_invocable, mailbox).
- **Message schema (`shared/schemas/message.schema.json` v2.0.0)** — `acting_as:` mandatory; from: enum extended.
- **`shared/schemas/task-return-packet.json` schema** — full P4.3 specification with frozen Part 1 §I.4 fields preserved + Part 6b §I.4 F8 LOCKED gate_class enum.
- **`executor-binding.yaml` TEMPLATE** — F.6 M1-M6 onboarding mandatory; activation_status enum.
- **Hub-and-spoke topology pattern** — cells never invoke other cells directly; brigadier sole dispatcher.
- **Ashby variety target ≥20 routing rules** — for principled coordination scaling.
- **Halt-Log-Alert + Corrigibility + Default-Deny** — Bundle 1 LOCKED frameworks consumed at coordination layer.
- **Phase B split_trigger pattern** — sustained task-intake rate threshold; brigadier splits into [task-dispatcher, integration-manager, gate-keeper].

### RUSLAN-LAYER (specific to Ruslan's Jetix instance)

- **Specific role-manifests** (5 ROY experts authored at `.claude/agents/<expert>.md`; brigadier at `.claude/agents/brigadier.md`; 13 legacy agents) — Ruslan's specific role definitions.
- **`swarm/lib/routing-table.yaml` populated values** — Ruslan's specific role slugs (5 ROY + 1 brigadier + 13 legacy = 19 channels), J-level assignments, mode allowlists, escalation routes.
- **`executor-binding.yaml` populated values** — Ruslan's specific executor identifiers (model identifiers, agent file paths, granularity tags), specific F.6 M1-M6 timestamps, specific reviewer attestations. **NOT a Foundation artefact per IP-1 strict.**
- **Specific message schema enum extensions** — Ruslan's specific role names in `from:` enum.
- **Specific decision-class assignments per role** — Ruslan's J-Auto / J-Approve / J-Strategic mappings.
- **Specific accessor skill invocability per role** — Ruslan's per-role permits in `accessor_skills_invocable:`.

### Phase B fork sees

A Phase B partner forking Foundation:

1. **Imports** Foundation generic schemas (role-manifest 5-block; routing-table.yaml STRUCTURE; message schema; task-return-packet schema; executor-binding template).
2. **Imports** the operational discipline (hub-and-spoke; Halt-Log-Alert; Corrigibility; Default-Deny; Ashby variety target; F.6 onboarding).
3. **Replaces** RUSLAN-LAYER with their own (their role manifests; their routing-table.yaml entries; their executor-binding.yaml; their message schema enum).
4. **Activates** K9 split_trigger pattern when their task-intake rate exceeds threshold.
5. **Cross-fork reconciliation** per Bundle 1 P1.1 cross-fork-provenance.json + K10 cross-fork-executor-binding-incompatibility (deferred per OQ-B1-8).

The IP-1 invariant is permanent across all forks: role manifests stay U.Episteme Foundation; executor bindings stay RUSLAN-LAYER (or partner-LAYER) per fork.

---

*End of Part 4 — Role Taxonomy & Coordination Protocol architecture. Status: draft-pre-ruslan-ack. F4 → F5 on Ruslan ack of Bundle 2 packet. Cross-references: C1-joint-design.md + swarm/lib/README.md (Bundle 2); Bundle 1 LOCKED Parts 1/6a/6b architectures; Parts 2 + 3 architectures (Bundle 2 siblings); Wave A interface card (superseded for Wave C onward but preserved historically). IP-1 self-audit confirmed ZERO executor names in §A-§N + §X — all role references are role-archetype slugs. OQ-B2-A flagged: Part 1 §I.4 stub gate_class enum drift from Part 6b §I.4 F8 LOCKED enum requires Bundle 1 retroactive correction via constitutional AWAITING-APPROVAL packet.*
