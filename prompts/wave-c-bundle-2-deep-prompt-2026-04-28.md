---
title: ROY Brigadier Deep Prompt — Wave C Bundle 2 (Parts 2 + 3 + 4 — Information Lifecycle + Agent Coordination)
date: 2026-04-28
type: deep-prompt
target: ROY brigadier (.claude/agents/brigadier.md)
parent_brief: prompts/cloud-code-wave-c-bundle-2-prompt-writing-brief-2026-04-28.md
predecessor_deep_prompt: prompts/wave-c-bundle-1-deep-prompt-2026-04-28.md
predecessor_ack: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 2
bundle_scope:
  - "Part 2 — Signal Ingestion & Triage"
  - "Part 3 — Knowledge Base & Methodology Library"
  - "Part 4 — Role Taxonomy & Coordination Protocol"
estimated_walltime: 14-20h
status: ready-for-brigadier-dispatch
constitutional_baseline: 2026-04-28 Ruslan ack of Bundle 1 (RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md) — F-G-R F8 / Default-Deny F8 / Blast-radius F8 / AWAITING-APPROVAL packet schema F8 / Halt-Log-Alert F8 / Corrigibility F8
mantra: "QUALITY > SPEED. PROVENANCE > VOLUME. WISDOM-APPLIED > WISDOM-CITED. OPERATIONAL > PHILOSOPHICAL. RUSLAN-ACK > BRIGADIER-CONFIDENCE. C1 BLOCKING — Part 3 + Part 4 must agree."
---

# Wave C Bundle 2 — ROY Brigadier Deep Prompt

## §0 Mission Statement (READ FIRST, INTERNALIZE)

**Bundle 2 builds the information lifecycle and agent coordination layers atop the Bundle 1 substrate.**

Bundle 1 produced the load-bearing foundation: Part 1 (System State Persistence), Part 6a (Provenance Officer), Part 6b (Human Gate). Those documents are LOCKED-canonical at F8 constitutional. Bundle 2 now consumes those LOCKED schemas and wires three new Foundation parts into them: how raw signals enter the system (Part 2), how knowledge accumulates and compounds (Part 3), how agents coordinate and route work (Part 4). Together these three parts form the **Information Lifecycle + Agent Coordination** layer.

**Treat with 1 trillion percent responsibility.**

The constitutional contract from Bundle 1 is permanent. You do NOT re-litigate F-G-R schema, Default-Deny framework, blast-radius tier structure, AWAITING-APPROVAL packet schema, Halt-Log-Alert, or Corrigibility. You CONSUME them. Every Bundle 2 part calls Part 1 §H operations, every emitted artefact carries F-G-R per Part 6a §I.1 schema, every promotion event logs to `swarm/approvals/log.jsonl`, every novel action class is Default-Deny classified per Part 6b §I.3, every gate packet conforms to Part 6b `awaiting-approval-packet.json` with `gate_class` enum.

Read this prompt three times before dispatching. Read every linked constitutional artefact in §3 before composing your first dispatch. When in doubt, ask Ruslan via HITL escalation.

> *Ruslan emphasis (verbatim, original Russian, do NOT paraphrase before applying):*
> *«Чтобы вся вот эта мудрость, наработки из книг — они были применены в системе,*
> *если это возможно, если нужно, целесообразно — на 1000% насколько это*
> *целесообразно. Ещё чтобы задавались вопросы как мы можем конкретно добавить,*
> *нахуй, эту штуку, чтобы было ещё отдельный прогон где вся эта залупа даёт*
> *обратную связь — а как мы можем это улучшить с точки зрения такой-то книжки*
> *или с книжки такой-то.»*

The Wisdom Application Loop (§5) operationalizes Ruslan's central directive. Bundle 2 refines it with an explicit OPERATIONAL vs PHILOSOPHICAL discriminator (per Ruslan feedback after Bundle 1 walkthrough). Operational adoptions ≥60% target. Philosophical adoptions allowed only if scope-creep-prevention or Phase B/C concrete-need justified.

**Bundle 2 introduces a novel structural phase: the Joint Design Phase between Part 3 and Part 4.** The C1 BLOCKING contradiction (accessor pipeline ownership: where do `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` live?) was acked by Ruslan as **Variant A: shared infra `swarm/lib/` with named owner**. Bundle 2 materializes this answer as a single coherent canonical decision spanning Parts 3 and 4. Parts 3 and 4 cannot be designed sequentially-in-isolation; they must be designed jointly with a single canonical answer documented in `swarm/lib/README.md` referenced from both.

---

## §1 Constitutional Inputs (Bundle 1 LOCKED — DO NOT re-litigate)

These are F8 constitutional invariants from `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md`. Bundle 2 CONSUMES these as canonical contracts.

### §1.1 F8 LOCKED schemas (from Bundle 1)

| Constitutional artefact | F-level | Bundle 2 consumption rule |
|---|---|---|
| `f-g-r.json` (Part 6a §I.1) | F8 | Every Bundle 2 architecture document, every emitted artefact, every wiki entry — F-G-R tag mandatory per OQ-B1-1 anchor wording (F4="≥3 cycles applied"; F6="cross-cycle reuse evidence"; F8="FUNDAMENTAL Vision lock-class") |
| `awaiting-approval-packet.json` with `gate_class` enum (Part 6b §I.1) | F8 | Every Bundle 2 STOP gate packet, stage gate packet, draft promotion packet conforms — `gate_class: stop_gate \| stage_gate \| draft_promotion` mandatory |
| `default-deny-table.yaml:foundation_generic:` + `constitutional_never_list:` (Part 6b §I.3) | F8 | Every novel action class introduced by Bundle 2 must be classified — silently new action classes = constitutional violation |
| `blast-radius-table.yaml:foundation_generic:` 4-tier 0/1/2/3 (Part 6b §I.4) | F8 | Every Bundle 2 action tiered for HITL escalation: Tier 0 integrity (auto-halt) / Tier 1 strategic (Ruslan ack) / Tier 2 tactical (batch ack) / Tier 3 routine (auto-log) |
| Halt-Log-Alert primitive (Part 6b §E Law L9) | F8 | ≤1s halt / ≤5s log / ≤60s alert ordering invariant — every Bundle 2 failure mode in §K conforms |
| Corrigibility (Part 6b §E Law L9, Askell HHH Appendix E.2) | F8 | NO mechanism in Bundle 2 may lock human owner out — verbatim Askell quote constraint |

### §1.2 Bundle 1 interface contracts that Bundle 2 calls

- **Part 1 §H commit interface** — every Bundle 2 part calls Part 1 operations for canonical writes; commit-format-tokens.json schema enforced
- **Part 1 §I.5 task-return-packet stub (frozen field set)** — `git_commit_hash`, `actor_role_archetype`, `cycle_id`, `gate_class`. Part 4 §B Outputs (Bullet P4.3) FULLY SPECIFIES this schema (UND-1 binding); Part 5 (Bundle 3) consumes the raw packet and does its own DRR extraction
- **Part 6a §C `[src:filename]` enforcement** — every Bundle 2 architecture document follows citation discipline within 200 chars (anti-cargo-cult)
- **Part 6a §C approval log structure** — `swarm/approvals/log.jsonl` append-only schema; every Bundle 2 promotion event emits a log entry
- **Part 6b stage-gate predicates registry** (Part 6b §I.2 `stage-gates.yaml`) — Bundle 2 promotion classes (draft → reviewed → accepted → canonical) gate-checked

### §1.3 Open Questions resolved at Ruslan ack time (do NOT reopen)

| OQ | Status | Implication for Bundle 2 |
|---|---|---|
| OQ-B1-1 | F4/F6/F8 anchor wording ACCEPTED | Use new wording in all Bundle 2 §G F-G-R tables |
| OQ-B1-2 | citation scanner — proceed within 2 cycles | NOT Bundle 2 work; Bundle 4 / Phase B engineering backlog |
| OQ-B1-3 | Tier 2 batch sub-grouping | DEFER Wave D + Phase B operational data |
| OQ-B1-4 | jsonschema validator | DEFER Phase B engineering backlog |
| OQ-B1-5 | D27 `approvals_reconciliation_strategy` field | DEFER Bundle 4 Part 10 |
| OQ-B1-6 | Rules 4 + 7 real-time encoding | DEFER Wave D capability gap |
| OQ-B1-7 | `unshare -n` → strace fallback | RESOLVED in Part 1 frontmatter; not Bundle 2 work |
| OQ-B1-8 | cross-fork-audit-deferred-phase-b.md stub | CREATED in Bundle 1 ack commit |

### §1.4 Bundle 2-specific Open Questions (UND-1, UND-4, UND-5, C1 — IN SCOPE)

These are the structural questions Bundle 2 owns answers for:

- **UND-1 (Part 4 → Part 5 DRR boundary)** — Ruslan acked: **Part 5 receives raw task-return packets**, does own DRR extraction. Part 4 §B Outputs FULLY SPECIFIES `task-return-packet.json` schema. Bullet P4.3.
- **UND-4 (`gate_class` field)** — F8 LOCKED in Bundle 1 Part 6b §I.1. Bullet P2.1 emits packets conforming.
- **UND-5 (CRM edge validation)** — IN SCOPE Part 3 Bullet P3.3. Part 3 §D + §E Laws declare Part 10 as content creator writing typed CRM edges into `wiki/graph/edges.jsonl`; Part 3 `/lint` validates CRM-origin edges.
- **C1 BLOCKING (accessor pipeline ownership)** — Ruslan acked: **Variant A — shared infra `swarm/lib/` with named owner**. Bundle 2 materializes this in Joint Design Phase (§4.2 below). Part 3 lead with Part 4 advisory PROPOSED; brigadier may refine in Joint Design if better answer surfaces.

### §1.5 Cross-cuts within Bundle 2 (apply throughout)

| Cross-cut | Rule | Where applied |
|---|---|---|
| **IP-1 Role≠Executor (CRITICAL Part 4)** | Role manifests = U.Episteme; executor bindings = RUSLAN-LAYER `executor-binding.yaml`. NO executor name appears in Foundation Part 4 artefacts. | §A Inputs source-ownership; §X fork-separation; §I.routing-table |
| **A.14 typed edges** | Bundle 1 canonical 10-edge table MUST be referenced; no new edge types invented without explicit FPF A.14 anchor. | §D Dependencies (every entry) |
| **F-G-R DOGFOOD per F8 schema** | Every promoted claim carries F-G-R per Bundle 1 Part 6a §I.1 schema. | §G F-G-R Tagging table; inline tags |
| **Append-only** | wiki/ entries / methodology library / role manifests / mailboxes — append-only. | §C Side-effects; §I Data schemas |
| **L/A/D/E** | Every interface section structured per FPF A.6.B Boundary Norm Square. | §E Boundary lanes |
| **Foundation vs RUSLAN-LAYER** | Explicit §X per part per OQ-MERGED-3 fork-separation declared up-front. | §X (mandatory) |
| **C1 Joint Design** | Parts 3 + 4 produce single coherent answer; brigadier runs Joint Design Phase between A-3 and A-4 (NEW). | Joint design artefact + both §I |

---

## §2 Bundle 2 Scope — Three Parts, Ten Bullets

### §2.1 Part 2 — Signal Ingestion & Triage (3 bullets, ~M total)

**Source**: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` §2 Part 2.
**Interface card**: `.../interface-cards/part-2-signal-ingestion-triage.md` (153 lines).

**Bullet P2.1 — STOP gate packet emission spec (UND-4 binding)**
- Output: Part 2 §H Code interfaces declaring how Part 2 emits packets conforming to Bundle 1 Part 6b §I.1 `awaiting-approval-packet.json` with `gate_class: stop_gate`.
- Acceptance predicate: every Part 2 STOP gate submission validates against Part 6b's frozen schema; `gate_class: stop_gate` field non-null; provenance chain (raw source → triage draft → human-ack timestamp) traceable.
- F-G-R: F4 operational convention (consumer of F8 schema), G holds-within-Foundation-scope, R-medium.
- Bundle 1 dependency: consumes Part 6b §I.1 schema as F8 frozen contract.

**Bullet P2.2 — PARA-tier enforcement at /ingest level**
- Output: `para_tier: Project | Area | Resource | Archive` declared as MANDATORY frontmatter field in draft-candidate schema; `/ingest` rejects drafts without `para_tier`; `/lint` Bundle 1 P6a.2 citation enforcer extended (or new `/lint --check-para-tier` signal added — choose one path in architecture).
- Acceptance predicate: synthetic test fixture of 10 drafts (5 with para_tier, 5 without) — pipeline accepts 5, rejects 5; `/lint` flags any orphan canonical entry lacking `para_tier`.
- F-G-R: F4 operational convention, G holds-within-Foundation-scope, R-high (testable).
- Source: KM consultant card P4 (Forte PARA organise by actionability) + interface card §E Deontics.

**Bullet P2.3 — Multi-owner STOP gate stub (Phase B declaration)**
- Output: Part 2 §H + §X declaring the gate authority delegation mechanism for multi-owner Phase B/C scale: per-owner gate instance with scoped authority; F.9 Bridge fields required for multi-owner activation; trigger predicate (`owner_count > 1`).
- Acceptance predicate: Phase B partner reading Part 2 §X can identify exactly which fields and which authority delegation pattern they must supply to instantiate a second-owner gate without re-architecting.
- Spec-ONLY: NO implementation; declaration committed as Foundation artefact so Phase B doesn't rediscover design intent.
- F-G-R: F2 (proposed; not validated) → F3 on architecture document acceptance, G holds-within-Foundation-scope, R-low (no operational data yet).
- Source: dependency-graph §6.2 "structural change estimate ~35% — ABOVE 30% threshold"; OQ-6.

### §2.2 Part 3 — Knowledge Base & Methodology Library (4 bullets, ~M-L total — C1 Joint Design required)

**Source**: wave-c-worklist §2 Part 3.
**Interface card**: `.../interface-cards/part-3-knowledge-base-methodology-library.md` (167 lines).

**Bullet P3.1 — C1 ACCESSOR PIPELINE OWNERSHIP RESOLUTION (BLOCKING — Joint Design with Part 4)**
- Canonical answer (Ruslan-acked 2026-04-27): **`swarm/lib/` shared infra with named owner**. Skills `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` live in `swarm/lib/` as infrastructure layer (U.System); Part 3 owns wiki content (U.Episteme); Part 4 owns role-manifest content (U.Episteme); neither owns the accessor scripts directly.
- Output: `swarm/lib/README.md` (single canonical document) declaring (a) what scripts live there, (b) who owns each, (c) the named-owner role (proposed: Part 3 lead with Part 4 advisory; brigadier may refine in Joint Design Phase if better answer surfaces), (d) modification governance (changes require AWAITING-APPROVAL stage_gate per Part 6b).
- Output: Part 3 §I + Part 4 §I both REFERENCE `swarm/lib/README.md` (DRY violation prohibited — single canonical answer in `swarm/lib/README.md` with cross-references; do not duplicate the content in two §I sections).
- Acceptance predicate: every accessor skill is path-addressable in `swarm/lib/`; routing-table.yaml (Part 4 P4.1) lists which roles invoke which accessor skills; Part 3 §F Anti-scope explicitly disowns the scripts.
- F-G-R: F4 (operational; canonical post-ack) → F5 if reused across ≥3 cycles, G holds-within-Foundation-scope, R-medium.
- BLOCKING for Wave C task assignment per dependency-graph §3.1.

**Bullet P3.2 — Methodology library sub-layer materialisation**
- Output: `wiki/methodology/` consistently populated as canonical entity-type (or chosen path per architecture decision: `wiki/foundations/` extension OR `wiki/methodology/` new entity-type — pick one explicitly). Promotion pipeline from Part 5 → Part 3 declared in Part 3 §A Inputs + §E Admissibility.
- §E Admissibility: methodology pattern from Part 5 accepted only if (a) carries ≥1 DRR 'Result: validated' marker from ≥2 distinct cycles, (b) carries `rule_slug` for deduplication, (c) F-level rises to F5 post-promotion (per Bundle 1 OQ-B1-1 anchor wording: F5 = "peer-validated methodology" — applicable here on owner ack as peer-equivalent in single-owner Phase A scope).
- Edge density target ≥2.0 edges/entity (current 1.05) — Wave C target via mandatory cross-reference at every methodology entry write.
- Acceptance predicate: at least one methodology entry promoted from Bundle 3 stub (Part 5 work) lands cleanly in `wiki/methodology/<pattern>.md`; passes `/lint`; carries F5 + ClaimScope + `refuted_if`.
- F-G-R: F4 (architecture); the methodology entries themselves carry F5 post-promotion.
- Source: KM consultant card §4 Principle 1 + Compounding-Engineering §5 + UND-3 (partially resolved Part 3 side; Part 5 side in Bundle 3).

**Bullet P3.3 — CRM edge validation schema (UND-5 binding)**
- Output: Part 3 §D + §E Laws explicitly declare Part 10 as a content creator writing typed CRM edges into `wiki/graph/edges.jsonl`. The 8 CRM edge types enumerated. Validation rules: malformed CRM edges flagged by Part 3 `/lint` (operating on Part 3-managed file even though origin is Part 10); the validation surface is Part 3 territory; the edge content origin is Part 10 territory.
- Acceptance predicate: synthetic fixture of 10 CRM edges (5 well-formed, 5 malformed in distinct ways) — Part 3 `/lint` flags 5 malformed edges with specific reasons; cross-references Part 10 (Bundle 4) for content authoring rules.
- F-G-R: F4 operational convention, G holds-within-Foundation-scope (CRM edge type taxonomy is Foundation generic; specific edge instances RUSLAN-LAYER), R-medium.
- Source: dependency-graph §4.5 UND-5; CLAUDE.md CRM System §8 CRM edge types.

**Bullet P3.4 — `/ask --save` default enforcement (per OQ from Wave A)**
- Output: `/ask` skill spec updated to file synthesis responses to `wiki/comparisons/` by default; `--no-save` flag required for ephemeral discard. `/lint` health signal added to flag `wiki/comparisons/` emptiness when `/ask` usage is confirmed in session history.
- Acceptance predicate: `/ask "X"` invocation produces a committed file at `wiki/comparisons/<query-slug>.md` with citations; `/ask --no-save "X"` produces ephemeral output only; `/lint` detects empty `comparisons/` after N>0 `/ask` invocations and flags as health defect.
- F-G-R: F4 operational convention, G holds-within-Foundation-scope, R-high (testable).
- Source: interface card §E Deontics + KM consultant card §6 Part 3 item 3.

### §2.3 Part 4 — Role Taxonomy & Coordination Protocol (3 bullets, ~M-L total — IP-1 CRITICAL + UND-1 binding)

**Source**: wave-c-worklist §2 Part 4.
**Interface card**: `.../interface-cards/part-4-role-taxonomy-coordination-protocol.md` (111 lines).

**Bullet P4.1 — Routing table as declarative YAML (PRIMARY Wave C gap)**
- Output: `swarm/lib/routing-table.yaml` — extract routing logic currently embedded in `brigadier.md` + 5 expert system prompts. YAML declares per role: `slug`, `j_level_authority` (per A.13 Agency-CHR), `allowed_modes`, `write_scope_glob`, `escalation_taxonomy_per_trigger`, `hub_and_spoke_dispatch_chain`, `accessor_skills_invocable` (cross-ref to Bullet P4.2 / P3.1).
- Variety target: **≥20 distinct routing rules** per Ashby requisite variety (TRADEOFF-02 resolution per Manifest §4: brigadier routing variety must match task-type variety in the dispatch space). Below 20 = under-variety; flag and expand.
- Acceptance predicate: `routing-table.yaml` exists, parses without errors, contains an entry for every role in `comms/mailboxes/` (currently 13 channels); `/lint` validates structural completeness; routing variety count ≥20 declared rules.
- F-G-R: F5 SCHEMA target (currently F2 — embedded in system prompts), G holds-within-Foundation-scope, R-low until materialised then R-medium.
- IP-1 enforcement: routing table contains role slugs (U.Episteme), NEVER executor names (no model identifiers, no agent file paths, no instance IDs). Executor bindings live in RUSLAN-LAYER `executor-binding.yaml` referenced from routing-table.yaml by role slug only.
- Highest-leverage single Wave C investment per dependency-graph §6.4 ~40% structural change risk at 10× scale.

**Bullet P4.2 — C1 ownership decision materialized in Part 4 (joint with Part 3 P3.1)**
- Output: Part 4 §I REFERENCES `swarm/lib/README.md` (single canonical answer per P3.1) declaring routing table includes accessor-skill invocations; Part 4 §B Outputs lists "wiki accessor pipeline skills :: invocable by any consumer :: on-demand" with rationale that Part 4 routes invocations but does NOT own the scripts (the named owner per P3.1 is Part 3 lead with Part 4 advisory).
- Output: routing-table.yaml field `accessor_skills_invocable` per role declares which `swarm/lib/<skill>` scripts each role may invoke.
- Acceptance predicate: routing-table.yaml lints clean against `swarm/lib/README.md` declared inventory; no accessor skill is invokable from a role not declared in routing-table.yaml.
- F-G-R: F4 operational convention (post-Joint-Design ack), G holds-within-Foundation-scope, R-medium.
- BLOCKING dependency on P3.1 — Joint Design Phase resolves both bullets simultaneously.

**Bullet P4.3 — UND-1 DRR message schema at Part 4 → Part 5 boundary**
- Output: `task-return-packet.json` FULL schema definition (Bundle 1 stubbed in Part 1 §I.5 with frozen fields `git_commit_hash`, `actor_role_archetype`, `cycle_id`, `gate_class` — Bundle 2 Part 4 fully specifies). Per Ruslan ack OQ-3: **Part 5 receives raw task-return packets, does own DRR extraction.**
- Schema fields (proposed; Joint Design may refine): `packet_id`, `task_id`, `dispatched_at`, `returned_at`, `actor_role_archetype` (U.Episteme — IP-1 enforced), `cycle_id`, `mode` (per L/A/D/E A.6.B), `inputs[]`, `outputs[]`, `provenance_chain[]`, `f_g_r` (per Part 6a §I.1 F8 schema), `gate_class` (per Part 6b §I.1 F8 schema enum), `git_commit_hash` (per Part 1 §I commit-format), `dissent_preserved` (boolean + path if true per AP-6).
- §I declaration: schema VALIDATABLE against `shared/schemas/task-return-packet.json` (file declared inline; physical file generation Phase B per pattern of OQ-B1-2 + OQ-B1-4).
- §B Output declaration: "Structured task-return packets from all dispatched roles :: `compound-phase-start-event`" — Part 5 (Bundle 3) consumes raw packets at compound phase boundary.
- Acceptance predicate: schema structurally complete (every field typed, every required field marked); fixture of 3 synthetic task-return packets validates; Part 1 §I.5 stub fields are SUPERSET-compatible (frozen fields appear unchanged in full schema).
- F-G-R: F4 (architecture-time) → F5 on Bundle 3 Part 5 consumption validation, G holds-within-Foundation-scope, R-medium.
- Source: dependency-graph §4.1 UND-1; OQ-3 ack 2026-04-27; Compounding-Engineering §3 DRR extraction logic.

### §2.4 Cross-cuts within Bundle 2 (re-stated for emphasis)

- **IP-1 Role≠Executor** is CRITICAL for Part 4 — every routing-table.yaml entry, every role-manifest, every dispatch packet uses role archetype names. NO model names, NO agent file paths, NO instance IDs in Foundation artefacts. Executor bindings live exclusively in RUSLAN-LAYER `executor-binding.yaml`. Critic gate AUTO-REJECTS any Part 4 artefact violating this.
- **A.14 typed edges** — Bundle 1's canonical 10-edge reference table is the lookup. Generic `depends-on` is FORBIDDEN.
- **F-G-R DOGFOOD per F8 schema** — every architecture claim tagged with F-level, ClaimScope, Reliability per Bundle 1 Part 6a §I.1.
- **Append-only** — wiki entries, methodology library entries, role manifests, mailbox writes — all append-only.
- **L/A/D/E** — every §E Boundary section structured per FPF A.6.B Norm Square.
- **Foundation vs RUSLAN-LAYER** — explicit §X per part:
  - Part 2: anchor-mandatory pattern + STOP gate structure GENERIC. Voice-pipeline tools / specific PARA tier definitions for Ruslan's projects = RUSLAN-LAYER.
  - Part 3: wiki accessor pipeline + KB structure GENERIC. Specific wiki content / niche slices / methodology library entries Ruslan-authored = RUSLAN-LAYER.
  - Part 4: role-manifest schema + routing table SCHEMA generic. Specific role-manifests + `routing-table.yaml` entries + `executor-binding.yaml` = RUSLAN-LAYER.
- **C1 Joint Design** — Parts 3 + 4 produce single coherent answer; brigadier MUST run Joint Design Phase between them, not just sequential dispatch.

---

## §3 Required Reading — MANDATORY before first dispatch

Brigadier MUST read these BEFORE any subagent dispatch. Each pre-read MUST be cited in output. Subagent dispatches MUST instruct experts to read RELEVANT subsets only.

### §3.1 Constitutional baseline (full-read mandatory)

1. `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0) — esp. **§6.1 hard rules** (Default-Deny anchor — Bundle 2 wires emitters to it)
2. `design/JETIX-FPF.md` — IP-1..IP-8 (esp. **IP-1 CRITICAL for Part 4**), 14 invariants A.1-A.14, A.6.B L/A/D/E, A.13 Agency-CHR (J-level matrix), A.14 typed mereological edges
3. `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` (esp. §4 agents/, comms/mailboxes, swarm/lib/shared-protocols.md; §6 voice pipeline; §8 wiki — 552 entities / 577 edges)
4. `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` — esp. **§4.5 deep-study constraint** (15-25K words per part doc; same as Bundle 1)
5. **Bundle 1 LOCKED Foundation outputs (CONSTITUTIONAL FOR BUNDLE 2):**
   - `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` (esp. §B Outputs / §H Code interfaces / §I.5 task-return-packet stub fields)
   - `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` (esp. §I.1 F-G-R schema F8 / §C approval log discipline)
   - `swarm/wiki/foundations/part-6b-human-gate/architecture.md` (esp. §I.1 awaiting-approval-packet schema F8 with `gate_class` UND-4 / §I.2 stage-gates / §I.3 default-deny-table `constitutional_never_list:` / §I.4 blast-radius-table 4-tier / §E Laws L1-L10 esp. **L9 Halt-Log-Alert + Corrigibility**)
6. `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` (Ruslan's specific ack decisions on F8 promotions; F-promotions table; OQ-B1-1..OQ-B1-8 statuses)
7. `decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-28.md` (Bundle 1 packet — format reference for Bundle 2 packet)
8. Locks D1-D29 + 4 LOCKS-ADDENDUM (focus on **D17 FPF anchor**, **D26 offline-first** (Part 2 voice pipeline), **D27 cross-fork** (Bundle 2 §X), **D28 anchor-mandatory** (Part 2 + Part 3), most recent `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md`)

### §3.2 Wave A artefacts (full-read mandatory)

1. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md`
2. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md`
3. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md` (esp. §3.1 C1 BLOCKING; §4.1 UND-1; §4.4 UND-4; §4.5 UND-5; §6.4 ~40% routing structural change risk)
4. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` (esp. **§2 Part 2** lines 99-138, **§2 Part 3** lines 142-198, **§2 Part 4** lines 202-246, **§3 Bundle 2 composition** lines 592-598, §4 cross-bundle dependencies, §6 OQs)
5. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md`
6. **M1/M2/M3 verification reference patterns** (Bundle 1 used these; Bundle 2 follows the same pattern with Bundle 2 scenario specifics — see §6 below)
7. **Wave A interface cards for Bundle 2 parts:**
   - `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md` (153 lines — Part 2 §A-§H baseline)
   - `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md` (167 lines — Part 3 §A-§H baseline; A-1 critic FLAG-MINOR resolved on accessor pipeline U.System/U.Episteme)
   - `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-4-role-taxonomy-coordination-protocol.md` (111 lines — Part 4 §A-§H baseline)
8. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/` (5 files: engineering, investor, mgmt, philosophy, systems)

### §3.3 Wave B consultant cards (per Manifest §2 matrix)

**For Part 2 dispatches** (engineering + philosophy + mgmt):
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md` — D28 anchor-mandatory, PARA tier (Forte Principle 4)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/unix-philosophy.md` — do-one-thing-well per pipeline stage
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/event-sourcing-cqrs.md` — append-only write, STOP gate as command handler
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` — IP-3, permeable filtered boundary A.1

**For Part 3 dispatches** (engineering + philosophy + systems + investor):
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md` — Karpathy LLM wiki, Luhmann atomicity, Matuschak stranger test, typed graph, P5 query-driven, P6 typed edges
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` — IP-2 bounded context, A.14 typed edges, F-G-R B.3
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md` — CE populates methodology library; DRR → methodology promotion (P3.2)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/clean-code.md` — Ousterhout deep-modules; each wiki concept = atomic unit
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/mereology-typed-edges.md` — typed edges = Part 3's graph schema canonical

**For Part 4 dispatches** (mgmt + philosophy + engineering + systems):
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` — **IP-1 CRITICAL Role≠Executor**, IP-8 F.6 6-step onboarding (M1-M6), L/A/D/E A.6.B
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/multi-agent-architecture.md` — hub-and-spoke P-2, verification architecture P-5, MAST coverage
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md` — hard-rule anti-scope §6.1, simplicity-transparency-trust
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/mereology-typed-edges.md` — typed edges for role dependencies
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md` — **Ashby requisite variety: brigadier routing variety ≥ task-type variety** (P4.1 ≥20 routing rules target)

### §3.4 Wave B Supplement library-direct sources (relevant subset)

- `raw/books-md/event-sourcing/young-cqrs-2010.md` — for **Part 2** (STOP gate as command handler, Reversal Transactions append-only) and **Part 4** (DRR / task-return-packet as event log)
- `raw/books-md/anthropic/bai-2022-cai.md` — for **Part 4** (multi-agent constitutional discipline; hardcoded never-list pattern dogfooded from Bundle 1)
- `raw/books-md/anthropic/askell-2021-hhh.md` — for **Part 4** (HHH framing for agent role manifests; Corrigibility Appendix E.2 already F8 Bundle 1)

(SRE Book + SRE Workbook from Bundle 1 are not first-class Bundle 2 sources; if they become relevant, target specific chapters via `pages` parameter.)

### §3.5 Existing operational artefacts (audit reference, do not duplicate)

- `tools/transcribe.py` / `tools/extract.py` / `tools/filter.py` / `tools/run_pipeline.sh` — current voice pipeline; Part 2 references as RUSLAN-LAYER specifics (Foundation declares STOP gate; specifics are RUSLAN-LAYER)
- `wiki/` (552 entities, 577 edges, 9 entity types) — current Part 3 state; Bundle 2 architecture extends, does not regenerate
- `.claude/agents/brigadier.md` + 5 expert agents (engineering / investor / mgmt / philosophy / systems) — current routing baseline; **Bundle 2 P4.1 EXTRACTS routing logic from these into `swarm/lib/routing-table.yaml`** but does not modify the agent files in this bundle
- `swarm/lib/shared-protocols.md` (current shared infra layer — destination per C1) — Bundle 2 P3.1 extends this with `swarm/lib/README.md` + accessor skill inventory
- `comms/mailboxes/*.jsonl` (13 channels) — Part 4 messaging baseline; routing-table.yaml MUST entry per channel per Bullet P4.1 acceptance predicate
- `shared/schemas/message.schema.json` — current message contract; Part 4 §I extends with `acting_as:` mandatory + task-return-packet schema (P4.3)

---

## §4 Phase Architecture (matrix dispatch + Joint Design + Wisdom Loop + critic gate)

Standard ROY cycle = **integrator → critic → finalize**. **For Bundle 2, brigadier MUST insert TWO structural phases beyond Bundle 1 pattern: a Joint Design Phase between Part 3 and Part 4 integrators (§4.2), and the Wisdom Application Loop with OPERATIONAL/PHILOSOPHICAL discriminator (§5).**

### §4.1 Phase sequence per part (sequential by default)

For each Part (2, 3, 4) execute in this order. Note: Parts 3 + 4 share a Joint Design Phase (§4.2); Part 2 runs independently first.

1. **Phase A — Pre-read confirmation** — brigadier reads §3 mandatory; dispatch instructs each expert to read RELEVANT subset only (per §3.3 mapping).
2. **Phase B — Matrix dispatch (5 experts × 4 modes = up to 20 cells)** — per ROY-ALIGNMENT §3 row mapping. Not every cell fires; brigadier picks cells that genuinely add signal. Minimum 8 cells per part.
3. **Phase C — Integrator** — brigadier (or delegated integrator-mode expert) merges cell outputs into draft architecture per §6 quality bar.
4. **Phase C+ — Joint Design Phase (Parts 3 + 4 ONLY)** — see §4.2. Resolves C1 BLOCKING; produces single canonical answer documented in `swarm/lib/README.md`.
5. **Phase D — Wisdom Application Loop** — see §5. **Bundle 2 refinement: OPERATIONAL/PHILOSOPHICAL column mandatory; ≥60% operational target.**
6. **Phase E — Critic gate** — ≥2 experts in critic-mode review draft + Joint-Design + Wisdom edits. Stricter cargo-cult check + IP-1 enforcement check (Part 4) + C1 coherence check (Part 3 + Part 4).
7. **Phase F — Finalize** — brigadier promotes draft → canonical at `swarm/wiki/foundations/<part-slug>/architecture.md`.
8. **Phase G — M-gates per part** — M1 smoke, M2 cross-ref. (M3 + M4 run at bundle level in §7.)

### §4.2 Joint Design Phase (NEW — Parts 3 + 4)

**Trigger**: After Phase C integrator drafts for Part 3 AND Part 4 are produced (both sequentially or in parallel within HD-02 N=2).

**Procedure**:
1. Brigadier convenes a **C1 resolution session** dispatching engineering-expert (integrator-mode) + systems-expert (critic-mode VSM S3 lens) + philosophy-expert (boundary-clarity lens) jointly on the question: "Where do `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` live? Who owns them? Who can modify them? How does Part 3 invoke them? How does Part 4 invoke them?"
2. The session reads Part 3 §I draft + Part 4 §I draft + the Ruslan-acked answer (`swarm/lib/` shared infra with named owner, Part 3 lead with Part 4 advisory PROPOSED).
3. Output: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` — single coherent answer. Required sections:
   - **Canonical answer**: `swarm/lib/` shared infra; named owner = <role>; modification governance = AWAITING-APPROVAL stage_gate per Part 6b
   - **Skill inventory**: `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` — file paths, brief description, current implementation status (which are operational, which are stubs)
   - **Invocation contract**: which roles invoke which skills (cross-ref to routing-table.yaml P4.1)
   - **Modification governance**: who proposes changes, who acks, where the audit log lives
   - **Cross-references**: Part 3 §I + Part 4 §I both reference this document; do NOT duplicate content
4. Output: `swarm/lib/README.md` — canonical infra-layer documentation. References `C1-joint-design.md` for design rationale; provides operational reference for future cycles.
5. Both Part 3 §I and Part 4 §I REFERENCE these two documents (DRY violation prohibited — single canonical answer; cross-references not duplications).
6. If Joint Design produces conflicting answers from Part 3 + Part 4 integrators (i.e., two different coherent answers): **escalate to brigadier-mode arbitration**; if answer materially differs from "shared infra `swarm/lib/` with Part 3 lead" → Ruslan ack required (write `swarm/wiki/foundations/<part-slug>/oq-bundle-2-N.md` and HALT for HITL).

**Why this matters**: Bundle 1 had no equivalent — Parts 1, 6a, 6b were independently designable. C1 spans Parts 3 + 4 structurally. Sequential design produces incoherent answers; Joint Design forces coherence at design-time, not at integration-time when re-architecture is expensive.

### §4.3 Cell selection guidance per part

**Part 2**: engineering (critic + scalability + integrator), systems (cybernetics + emergence — pipeline as feedback loop), mgmt (boundary + ethics-surface), philosophy (epistemic audit on STOP gate as J-Approve), investor (long-term-compounding — voice-memo flow as source of compound knowledge). Minimum 8 cells.

**Part 3**: engineering (critic + scalability + integrator + clean-code on KB atomicity), philosophy (epistemic audit on F-G-R promotion path; first-principles on `/ask` semantics), systems (Meadows leverage — `/lint` as L7 info-flow leverage), investor (capital-allocation — methodology library as compound asset), mgmt (boundary on accessor pipeline ownership). Minimum 8 cells.

**Part 4**: mgmt (prioritization + integrator + ethics-surface — IP-1 boundary), philosophy (Stoic dichotomy on agent agency + critic on IP-1 strict + first-principles on routing variety), engineering (scalability — federated coordinator substitution risk; critic — IP-1 violations), investor (capital-allocation — routing table as F5 codified investment), systems (requisite-variety — Ashby ≥20 routing rules; cybernetics on hub-and-spoke). Minimum 10 cells (this is the heaviest part — IP-1 critical + UND-1 binding + C1 joint).

### §4.4 Dissent preservation (AP-6)

If any expert in critic-mode produces dissent that integrator could not resolve: preserve in `swarm/wiki/foundations/<part-slug>/dissent.md`. Do NOT silently override expert domain judgment (E-15).

---

## §5 THE WISDOM APPLICATION LOOP (Phase D — central directive)

**This phase is constitutional. Skipping it is a violation.**

After integrator produces draft architecture for Part X (and after Joint Design Phase completes for Parts 3 + 4), brigadier dispatches a dedicated **Wisdom Loop pass**.

### §5.1 Procedure (UNCHANGED from Bundle 1 — preserve discipline)

For each consultant card relevant to this part (per §3.3 mapping) AND each library-direct supplement source (§3.4):

Ask FIVE questions, in order, in writing, with traceable answers:

1. **Question 1 — Application Gap**: "What does this consultant card say that the current draft DOES NOT yet apply, but would benefit from?"
2. **Question 2 — Cargo-Cult Audit**: "Are there principles from this card we cited but did not actually apply (cargo-cult risk per Manifest §5)?"
3. **Question 3 — Concrete Improvement**: "Is there a concrete improvement to the architecture if we apply principle X from this card?"
4. **Question 4 — Section Impact**: "If we DO apply this improvement — what changes in §A Inputs / §B Outputs / §C Side-effects / §D Dependencies / §E Boundary / §F Anti-scope / §H Code interfaces / §I Data schemas?"
5. **Question 5 — Phase A Justification**: "Is the application JUSTIFIED for current Phase A scope (single-owner, Phase 1 €50K horizon)? Or is it premature optimization for Phase B/C/D scale?"

### §5.2 Bundle 2 refinement — OPERATIONAL/PHILOSOPHICAL column (NEW per Ruslan feedback)

After Bundle 1 walkthrough, Ruslan flagged that some adoptions were "academic boundary text" rather than operational changes (e.g., Stoic Dichotomy of Control as §F.3 prose, Lindy verdict box). These were KEPT in Bundle 1 but represent **lower priority adoption category**.

**For Bundle 2, apply the following bias:**

- **PRIORITIZE operational adoptions** — adoptions that change schema fields, add new failure modes, define new SLO targets, add new lint checks, change algorithm, add new edge type, or modify code-level interface. Concrete code-level deltas.
- **MINIMIZE philosophical/marketing text** — adoptions that add only "framing prose" (e.g., "this is Lindy-grade", "in our control vs not", "Beer-clean S3 placement") without operational consequence.
- **REJECT** any adoption whose "concrete consequence sentence" is purely about how the document reads (e.g., "this makes the architecture more legible") rather than about what the system DOES differently.

**Wisdom Findings table format (UPDATED — new column):**

```markdown
### Wisdom Application Findings — Part X

| Card / Source | Principle | Current state | Improvement | Adopted? | Operational vs Philosophical | Justification | Section edited |
|---------------|-----------|---------------|-------------|----------|------------------------------|---------------|----------------|
| #1 Levenchuk SHSM-FPF | IP-1 Role≠Executor | partial in §F | Add IP-1 enforcement to routing-table.yaml header comment + critic-gate auto-reject any executor name | YES | OPERATIONAL | Phase A — IP-1 violations break fork import | §I + §H critic-gate |
| #5 Event Sourcing (Young 2010) | Reversal Transactions | applied in §C | — | n/a (already applied) | OPERATIONAL | already in §C | n/a |
| #7 Stoic | Dichotomy-of-Control | not applied | Add §F.3 "in our control" framing prose | NO | PHILOSOPHICAL | No scope-creep risk; no Phase B/C concrete need; pure framing prose; DEFER to Wave D documentation pass | n/a |
| ... | ... | ... | ... | ... | ... | ... | ... |
```

**New column "Operational vs Philosophical" — definitions:**
- **OPERATIONAL** = changes schema field / adds failure mode / defines SLO target / adds new lint check / changes algorithm / adds edge type / modifies code-level interface / adds new admissibility rule
- **PHILOSOPHICAL** = framing prose / boundary text / marketing positioning / academic context / paragraph in §0 explaining a school of thought

**Adoption thresholds:**
- OPERATIONAL adoption — adopt if Phase A justified (proceed as in Bundle 1)
- PHILOSOPHICAL adoption — adopt ONLY if it prevents a specific scope creep risk OR enables a Phase B/C concrete need; otherwise DEFER to Wave D documentation pass

**Aggregate target:**
> Bundle 2 should have YES Adopted ratio of Operational ≥60% (Bundle 1 was ~50/50; Ruslan asked to bias operational).

If Operational ratio < 60% across the 3 parts: investigate. Is brigadier reverting to philosophical text? Apply refinement bias more strictly. Re-dispatch integrator to convert PHILOSOPHICAL adoptions into OPERATIONAL ones (e.g., a Stoic Dichotomy adoption that was prose becomes a §F Anti-scope rule with a `/lint` check).

### §5.3 Discipline (HARD RULES — same as Bundle 1)

**Brigadier MUST**:
- Run Wisdom Loop AFTER integrator (and after Joint Design for Parts 3 + 4), BEFORE critic gate
- Produce findings table (§M) per part with the new OPERATIONAL/PHILOSOPHICAL column
- Apply every "YES Adopted" edit to draft BEFORE critic gate runs
- Critic gate then verifies: did Wisdom edits hold? Anti-cargo-cult check stricter than usual.
- For each YES Adopted entry, the edit MUST be visible in §A-§L diff (not just claimed in table).
- For each NO entry, the justification MUST be one of the legitimate categories: `Phase B work` / `Phase C+ scale` / `premature optimization` / `requires RUSLAN-LAYER decision Ruslan hasn't made` / `domain-orthogonal to this part` / `pure framing prose without operational consequence` (NEW — Bundle 2 PHILOSOPHICAL deferral category). Vague "not applicable" is INSUFFICIENT.

**Brigadier MUST NOT**:
- Skip Wisdom Loop because "draft seems fine"
- Reject improvement opportunities without explicit justification from the legitimate categories
- Adopt every improvement without Phase A justification (Phase B+ ideas DEFER)
- Treat the loop as paperwork — every YES is a real edit, every NO is a real reasoned defer
- Adopt PHILOSOPHICAL improvements without scope-creep-prevention or Phase B/C concrete-need justification (Bundle 2 refinement)

### §5.4 Failure mode (UNCHANGED from Bundle 1)

If Wisdom Application Loop produces 0 "YES Adopted" across all relevant cards for a part: HALT, write `swarm/wiki/foundations/<part-slug>/wisdom-loop-zero-adoption-flag.md` with reasoning, escalate to Ruslan via tmux output before proceeding to critic gate.

DO NOT fabricate YES entries to satisfy the loop. False positives in Wisdom Loop are worse than zero adoption — they corrupt the audit trail.

### §5.5 Why this matters (UNCHANGED — re-emphasize)

This loop prevents:
- Cargo-cult citation (citing without applying)
- Knowledge sitting unused in `raw/books-md/` despite Wave B Supplement processing
- ROY producing "good enough" architecture that ignores hard-won wisdom from 14 consultant cards + 5 library-direct sources
- Bundle 2 reverting to philosophical text after Ruslan's explicit operational bias feedback

---

## §6 Quality bar (per Master Plan Brief §4.5 deep-study constraint)

### §6.1 Document size

Each Part architecture document MUST be **15-25K words minimum** (~150-250KB markdown). Same as Bundle 1 quality bar.

If draft comes in under 15K words: brigadier returns to integrator with explicit feedback "you delivered N words; quality bar is 15-25K — re-dispatch with §A-§N expansion mandate."
If draft comes in over 25K words: review for redundancy + cargo-cult padding. Tighten before Wisdom Loop.

### §6.2 Section structure (every part doc has §A through §N + §X)

Same as Bundle 1 — see Bundle 1 deep prompt §6.2 table for full reference. Sections: §A Inputs / §B Outputs / §C Side-effects / §D Dependencies / §E Boundary L/A/D/E / §F Anti-scope / §G F-G-R Tagging / §H Code-level interfaces / §I Data schemas / §J Operational rituals / §K Failure modes / §L Wave C work-list bullet status / §M Wisdom Application Findings / §N Provenance / §X Foundation vs RUSLAN-LAYER.

Bundle 2 specifics:
- §I Data schemas: Part 3 §I + Part 4 §I both REFERENCE `swarm/lib/README.md` (single canonical answer per C1 Joint Design); Part 4 §I FULLY SPECIFIES `task-return-packet.json` (UND-1 binding); Part 2 §I emits packets conforming to Part 6b §I.1 (UND-4 satisfied)
- §H Code interfaces: Part 4 §H references `swarm/lib/routing-table.yaml` as PRIMARY artefact (P4.1); Part 3 §H + Part 4 §H reference `swarm/lib/README.md` (DRY)
- §X Foundation vs RUSLAN-LAYER per part — see §2.4 above for explicit declarations

### §6.3 Anti-cargo-cult enforcement (CRITICAL — same as Bundle 1)

Per Bundle 1 Part 6a §C citation discipline:
- Every `[src:...]` citation MUST be followed within 200 chars by a concrete consequence sentence. Example: "...therefore Part 4 §E Laws state: 'No executor name in Foundation routing-table.yaml' [src:design/JETIX-FPF.md §5.1 IP-1]". The consequence sentence is the operational change driven by the source.
- `/lint --check-citations` (Bundle 1 P6a.2 — specified, not yet implemented per OQ-B1-2) is the canonical enforcer; until it ships, manual discipline + critic gate.
- Critic gate MUST reject any §A-§N section with cargo-cult violations and return to integrator with line-number-specific feedback.

### §6.4 Typed A.14 edges everywhere (HARD RULE — Bundle 1 canonical 10-edge table)

Every §D Dependencies entry MUST be one of the canonical edge types per Bundle 1 Part 1 §D 10-edge reference table:

`ComponentOf` / `ConstituentOf` / `PortionOf` / `PhaseOf` / `MemberOf` / `AspectOf` / `creates` / `operates-in` / `methodologically-uses` / `constrained-by` / `derives-from`

**NO `depends-on`. NO `uses` generic. Critic gate auto-rejects.**

Bundle 2 specific edge usage examples:
- Part 2 `PhaseOf information-lifecycle` → Part 3 (triage draft is pre-KB phase)
- Part 2 `methodologically-uses` Part 6b (STOP gate as instance of HITL escalation discipline)
- Part 3 `operates-in` Part 1 (wiki entities persisted in git substrate)
- Part 3 `methodologically-uses` Part 6a (every promotion uses approval log + F-G-R service)
- Part 3 `methodologically-uses` Part 6b (every promotion gate-checked)
- Part 4 `creates` Part 5 (task-return packets feed compound phase) — UND-1 binding
- Part 4 `methodologically-uses` Part 6b (escalation routes through human gate)
- Part 4 `operates-in` `swarm/lib/` (routing-table.yaml + accessor skills live there per C1)

### §6.5 F-G-R on every promoted claim (DOGFOOD — same as Bundle 1)

Every architecture claim MUST have F-G-R tag per Bundle 1 Part 6a §I.1 F8 schema. Inline: `[F4|G:holds-within-Foundation-scope|R-medium]` OR table entry in §G.

Use Bundle 1 OQ-B1-1 anchor wording:
- F4 = "≥3 cycles applied"
- F6 = "cross-cycle reuse evidence"
- F8 = "FUNDAMENTAL Vision lock-class"

### §6.6 Provenance trail (same as Bundle 1)

Every claim → `[src:path]` inline citation → resolves to existing file + section. M2 cross-reference gate (§7.2) verifies 100% citation resolution. No broken citations allowed.

### §6.7 Foundation vs RUSLAN-LAYER fork-separation discipline (per OQ-MERGED-3)

Each Part architecture MUST have explicit **§X Foundation vs RUSLAN-LAYER fork-separation** section. See §2.4 above for Bundle 2 explicit declarations:

- **Part 2**: anchor-mandatory pattern + STOP gate structure GENERIC. Voice-pipeline tools (`tools/transcribe.py`, `tools/extract.py`, etc.) + specific PARA tier definitions = RUSLAN-LAYER.
- **Part 3**: wiki accessor pipeline + KB structure + 9-entity-type taxonomy GENERIC. Specific wiki content (552 entities Ruslan-authored) + niche slices + methodology library entries Ruslan-authored = RUSLAN-LAYER.
- **Part 4**: role-manifest schema + routing-table SCHEMA + message schema + task-return-packet schema GENERIC. Specific role-manifests (5 ROY experts + brigadier + 7 legacy agents) + `routing-table.yaml` entries + `executor-binding.yaml` (model names, agent file paths, instance IDs) = RUSLAN-LAYER.

---

## §7 Verification Gates (M1 / M2 / M3 / M4)

### §7.1 M1 Smoke Test (per part, threshold ≥90%)

Same checklist as Bundle 1:
- [ ] All §A-§N + §X sections populated (no "TBD" placeholders)
- [ ] Word count ≥15K
- [ ] Dependencies (§D) all typed per §6.4
- [ ] F-G-R tags (§G) present on every promoted claim
- [ ] Wave C bullets from §2 all mapped in §L with acceptance predicate ✅/❌
- [ ] §X Fork-separation section explicit
- [ ] No cargo-cult signals (citation without consequence sentence within 200 chars)

Bundle 2 additional checks per part:
- [ ] **(Part 4)** No executor names in §A-§N — IP-1 enforcement check
- [ ] **(Part 4)** routing-table.yaml referenced; ≥20 distinct routing rules variety target documented
- [ ] **(Part 4)** task-return-packet.json schema FULLY SPECIFIED in §I (UND-1 binding)
- [ ] **(Part 3)** §I REFERENCES `swarm/lib/README.md` (does NOT duplicate)
- [ ] **(Part 4)** §I REFERENCES `swarm/lib/README.md` (does NOT duplicate)
- [ ] **(Part 2)** STOP gate packet schema conforms to Part 6b §I.1 F8 schema (UND-4 binding)
- [ ] **(Part 2)** PARA-tier mandatory frontmatter declared
- [ ] **(Part 3)** CRM edge validation declared with Part 10 cross-ref (UND-5 binding)
- [ ] **(Part 3)** `/ask --save` default declared

Pass threshold: ≥90% bullets ticked. Per part. Failure: re-dispatch integrator.

### §7.2 M2 Cross-reference (per part, threshold 100%)

Same as Bundle 1:
- [ ] Every `[src:...]` resolves to an existing file
- [ ] Every cited section anchor resolves to an actual section heading
- [ ] No broken inline citations
- [ ] No dangling typed-edge targets in §D

Bundle 2 additional:
- [ ] Cross-references between Part 3 §I + Part 4 §I + `swarm/lib/README.md` + `C1-joint-design.md` all resolve
- [ ] Bundle 1 Part 1 §I.5 task-return-packet stub fields appear UNCHANGED in Part 4 §I full schema (frozen-fields invariant)
- [ ] Part 6a §I.1 F-G-R schema F8 cited from every Bundle 2 §G F-G-R table
- [ ] Part 6b §I.1 awaiting-approval-packet.json F8 cited from Part 2 P2.1

Pass threshold: 100%. Failure: integrator fixes citations OR escalates if cited file missing.

### §7.3 M3 Scenario Walkthroughs (bundle-level, 4 scenarios MUST pass)

Run each scenario end-to-end against Bundle 2 + Bundle 1 interfaces. Document trace in `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/M3-walkthroughs.md`.

**Scenario 1 — Voice memo full lifecycle (multi-bundle: Parts 2/3/6a/6b/1):**
voice file → `/ingest --anchor=<topic>` → `tools/transcribe.py` → `tools/extract.py` → `tools/filter.py` → `tools/review_report.py` → STOP gate (Part 6b — Bundle 1) → AWAITING-APPROVAL packet with `gate_class: stop_gate` (Part 6b §I.1 F8 schema) → human ack → Part 3 promotion → wiki entry written with F-G-R (Part 6a §I.1 F8) + `para_tier:` (Bullet P2.2) + provenance (Part 6a §C) → Part 1 commit with [area] format (Part 1 §H) → `swarm/approvals/log.jsonl` entry (Part 6a §C) → `/lint --check-citations` (Part 6a P6a.2 — declared, Bundle 4 implementation) passes.
Tests: Parts 2 + 3 + 6a + 6b + 1; UND-4 binding (gate_class); F8 schema consumption discipline.

**Scenario 2 — Multi-agent dispatch (Parts 4 + 5(stub) + 6b):**
brigadier reads task → Part 4 `swarm/lib/routing-table.yaml` selects expert agents (≥20 routing rules variety) → mailbox dispatch via `swarm/lib/` (per C1 Joint Design) → expert returns task-return-packet conforming to Part 4 §I full schema (UND-1 binding) → Part 5 stub receives raw → DRR extraction (Bundle 3 stub level — placeholder for full Part 5 work).
Tests: Parts 4 + 5(stub) + 6b; IP-1 (no executor names in routing-table.yaml); UND-1 binding; Ashby variety target.

**Scenario 3 — Methodology promotion (Parts 5(stub) + 3 + 6a + 1):**
pattern emerges in 3 cycles (Bundle 3 stub level — F4 "≥3 cycles applied" anchor satisfied per OQ-B1-1) → Part 5 (Bundle 3) stages it → Part 3 promotes to `wiki/methodology/<pattern>.md` per Bullet P3.2 admissibility (≥1 DRR validated marker from ≥2 cycles + rule_slug + F-level rises to F5 post-promotion) → `/lint --check-citations` (or per Bundle 4 implementation) passes → committed via Part 1 §H.
Tests: Parts 5(stub) + 3 + 6a + 1; methodology promotion pipeline; F5 rise on promotion.

**Scenario 4 — C1 invocation (Joint Design coherence test):**
Part 3 query "what is X?" calls `swarm/lib/ask.py` (per `swarm/lib/README.md` C1 ownership) → ask.py reads `wiki/index.md` (Part 3 content, U.Episteme) + `swarm/wiki/comparisons/` (per `--save` default) → returns synthesis with citations → response carries F-G-R per Part 6a §I.1 F8 schema → if `--save`, writes to `wiki/comparisons/<query-slug>.md` (Bullet P3.4).
Tests: C1 ownership boundary holds (Part 3 invokes a `swarm/lib/` script; the script accesses Part 3-managed content; Part 3 does NOT own the script); Part 6a F-G-R DOGFOOD.

Pass threshold: 4/4 scenarios trace cleanly with no missing schemas or undefined handoffs. Failure: re-architect specific gaps; do NOT paper over with TODO stubs.

### §7.4 M4 Wisdom Application Loop verification

Per part:
- [ ] §M Wisdom Findings table populated with NEW Operational/Philosophical column (not empty, not 0 adoption — see §5.4)
- [ ] Every "YES Adopted" entry has corresponding visible edit in §A-§L (verify by line-number diff trace)
- [ ] Every "NO" entry has explicit justification from legitimate categories (§5.3 — including new "pure framing prose without operational consequence" Bundle 2 category)
- [ ] No fabricated YES entries (cross-check: edit actually exists in target section)
- [ ] All relevant Wave B consultants per §3.3 mapping covered for each part (no card silently skipped)
- [ ] **Operational adoption ratio ≥60% per part** (Bundle 2 NEW threshold per Ruslan feedback)
- [ ] No PHILOSOPHICAL adoptions without scope-creep-prevention or Phase B/C concrete-need justification

Pass threshold: all bullets ticked per part + aggregate ≥60% operational across Bundle 2. Failure: re-run Wisdom Loop with specific gap list; if persistent under-60%, investigate brigadier reverting to philosophical text.

### §7.5 M5 NEW — C1 Joint Design coherence verification (Bundle 2-specific)

- [ ] `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` exists
- [ ] `swarm/lib/README.md` exists with skill inventory + named owner + modification governance
- [ ] Part 3 §I + Part 4 §I both reference these documents (DRY enforced)
- [ ] No conflicting accessor-pipeline ownership statements between Part 3 §I and Part 4 §I (semantic check by integrator)
- [ ] Named owner declared (proposed Part 3 lead with Part 4 advisory; brigadier-refined acceptable if rationale documented)

Pass threshold: 5/5. Failure: re-dispatch Joint Design Phase.

---

## §8 Output Expected (exact paths, structures)

### §8.1 Per-part architecture documents

- `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md` (~15-25K words)
- `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` (~15-25K words)
- `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` (~15-25K words)

Each with §A-§N + §X sections per §6.2.
Each with YAML frontmatter (per Global Rule 1).

### §8.2 Schemas / configs (PRIMARY GAPS per Wave A)

**Part 2:**
- STOP gate packet emission spec (declarative; conforms to Part 6b `awaiting-approval-packet.json` F8 with `gate_class: stop_gate` per UND-4 binding) — declared inline in Part 2 §H

**Part 3:**
- `swarm/lib/README.md` (C1 ownership + invocation contract — single canonical answer per Joint Design; Part 3 lead owner)
- (Optional, brigadier may decide via architecture lens) wiki entity-type tag spec for `wiki/methodology/` — declared in Part 3 §I

**Part 4:**
- **`swarm/lib/routing-table.yaml`** (PRIMARY GAP from Wave A — declarative routing rules; ≥20 variety target; IP-1 enforced — role slugs only, no executor names)
- `task-return-packet.json` schema (UND-1 binding — FULLY SPECIFIED; superset-compatible with Part 1 §I.5 frozen stub fields) — declared in Part 4 §I
- `executor-binding.yaml` template (RUSLAN-LAYER artefact template; F.6 M1-M6 onboarding block mandatory) — declared in Part 4 §I

### §8.3 Joint Design artefact (NEW for Bundle 2)

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` — single coherent answer to C1 ownership question; required sections per §4.2 step 3

### §8.4 Updated cross-references

- Wave A interface cards updated where outdated (Part 2 §A-§H drift; Part 3 §A-§H drift; Part 4 §A-§H drift) — reflect Bundle 2 final architecture
- Master Plan Draft Bundle 2 status table updated (mark Bundle 2 complete; reflect P3.1 + P4.2 C1 resolution)
- Manifest §2 matrix Bundle 2 rows updated (Parts 2, 3, 4 — adopted cards + Wisdom Loop counts)

### §8.5 Walkthroughs trace

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/M3-walkthroughs.md` — all 4 scenarios traced

### §8.6 Bundle-level dissent (if any)

- `swarm/wiki/foundations/<part-slug>/dissent.md` per part with unresolved critic dissent (AP-6 preservation)

### §8.7 AWAITING-APPROVAL packet (FINAL deliverable)

- `decisions/AWAITING-APPROVAL-wave-c-bundle-2-2026-04-XX.md` (XX = day of completion)

Structure mirrors Bundle 1 packet (`decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-28.md`):

```markdown
---
title: AWAITING-APPROVAL — Wave C Bundle 2 (Parts 2 + 3 + 4)
date: 2026-04-XX
type: awaiting-approval
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 2
parent_packet: decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-28.md
predecessor_ack: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
deep_prompt: prompts/wave-c-bundle-2-deep-prompt-2026-04-28.md
status: awaiting-ruslan-ack
F: F4
ClaimScope: "Holds for the 3 Bundle 2 architecture documents and their declared schemas. Does NOT pre-judge Bundle 3/4 work."
R:
  refuted_if: "Ruslan walkthrough surfaces a constitutional violation, IP-1 violation, C1 incoherence, UND-1 schema gap, UND-4 packet drift, or unresolved boundary leak in any of the 3 architecture documents"
  accepted_if: "Ruslan acks the 3 architecture documents AND the schema set AND the §X Foundation vs RUSLAN-LAYER separations AND the C1 Joint Design canonical answer AND the routing-table.yaml + task-return-packet.json + swarm/lib/README.md"
next_action: "Ruslan ack of this packet → brigadier dispatches Wave C Bundle 3 (Parts 5 + 8)"
---

## §1 Executive Summary
[3-5 paragraphs: what was built, key decisions (C1 Joint Design canonical answer; UND-1 task-return-packet specification; routing-table.yaml extracted); headline numbers (word counts, schemas defined, edges typed, F-G-R tags applied, routing variety count, Wisdom Loop adoption count, Operational vs Philosophical ratio).]

## §2 Outcomes — F-level changes
[Table: Artefact / F-before / F-after / Drift rationale — including routing-table.yaml F2→F5, task-return-packet.json F2→F4 (full schema), swarm/lib/README.md F0→F4]

## §3 Wisdom Findings Rollup (with Operational/Philosophical breakdown)
[Aggregate table across Parts 2 + 3 + 4: Total YES Adopted with Operational/Philosophical split / Total NO with reason categories / Per-card coverage matrix / Operational ratio achieved]

## §4 Verification Gate Results
- M1 Smoke: Part 2 X% / Part 3 X% / Part 4 X%
- M2 Cross-ref: 100% (or list broken citations)
- M3 Scenarios: 4/4 PASS (or list failures)
- M4 Wisdom: PASS with operational ratio ≥60% (or gap list)
- M5 C1 Joint Design coherence: PASS (or list incoherence findings)

## §5 Open Questions Surfaced By Bundle 2
[Any new OQs beyond UND-1/UND-4/UND-5/C1 — with proposed resolution / defer rationale]

## §6 Provenance
[List of every source consulted, with F-G-R tags, with consequence sentences cross-ref; commits on claude/jolly-margulis-915d34]

## §7 Ruslan Ack Request
[Specific decisions Ruslan must ack before Bundle 3 dispatches:
 - 3 Bundle 2 architecture documents canonical-promoted (status: ruslan-acked-canonical)?
 - C1 Joint Design canonical answer accepted (named owner = Part 3 lead with Part 4 advisory OR brigadier-refined alternative)?
 - routing-table.yaml structure + variety target ≥20 accepted?
 - task-return-packet.json schema accepted (UND-1 fully bound; Bundle 3 Part 5 will consume)?
 - PARA-tier mandatory frontmatter discipline accepted?
 - CRM edge validation cross-ref to Part 10 (Bundle 4) accepted?
 - swarm/lib/README.md becomes canonical infra-layer documentation?
 - Any per-part dissent items: Ruslan resolves]

## §8 STOP — Do not auto-launch Bundle 3
Per §11 STOP rule.
```

### §8.8 STOP

After AWAITING-APPROVAL packet — STOP. NO auto-launch Bundle 3.

---

## §9 Branch + Commit Discipline

- **Branch**: `claude/jolly-margulis-915d34` (current, same as Bundle 1). Do NOT create new branches.
- **Commit cadence**: small + frequent. After each major phase per part.
- **Commit message format**: `[architecture] Bundle 2 — <part> — <phase>` examples:
  - `[architecture] Bundle 2 — Part 2 — Phase B + C cells + integrator draft`
  - `[architecture] Bundle 2 — Part 2 — Phase D Wisdom Loop applied (X YES Op / Y YES Phi / Z NO)`
  - `[architecture] Bundle 2 — Parts 3 + 4 — Phase C+ Joint Design (C1 resolution canonical)`
  - `[architecture] Bundle 2 — Part 3 — Phase E critic gate PASS`
  - `[architecture] Bundle 2 — Part 4 — Phase F finalized + M1/M2 PASS (IP-1 verified)`
  - `[architecture] Bundle 2 — M3 walkthroughs 4/4 PASS + M5 Joint Design coherence PASS`
  - `[architecture] Bundle 2 AWAITING-APPROVAL — Parts 2 + 3 + 4 architecture, Wisdom Loop applied (operational ≥60%), C1 resolved, M-gates PASS`
- **Push cadence**: after each commit. No force-push. No `--amend`. No `--no-verify`.
- **API-key audit**: before each commit run `grep -rEn 'ANTHROPIC_API_KEY|GROQ_API_KEY|OPENAI_API_KEY|sk-ant-' <staged-files>` → 0 hits required.

---

## §10 Operational Constraints

1. `unset ANTHROPIC_API_KEY` before any provider invocation. Brigadier MUST NOT reference any provider API-key env var in any code path.
2. `ulimit -n 65535` if not already set.
3. **HD-02 rate limiter N=2 normal mode**. Maximum 2 concurrent Task() dispatches.
4. **Read tool 32MB limit**: for large PDFs use `pages` parameter; do NOT auto-read full books.
5. **NO auto-execution of Bundle 3 after Bundle 2** — explicit STOP per §11.
6. **No `--amend`, no `--no-verify`, no force-push** — git-native rollback via `git revert` only.
7. **Frontmatter compliance**: every `.md` artefact carries YAML frontmatter per the relevant `swarm/wiki/_templates/<type>.md` template.
8. **Untouchable trees in Phase A**: 14 legacy `.claude/agents/*.md` files and the v2 `wiki/` tree. Bundle 2 P4.1 EXTRACTS routing logic from `brigadier.md` + 5 ROY expert system prompts — but does NOT modify the agent files themselves; routing-table.yaml is a NEW artefact that mirrors what's currently embedded.
9. **Security — never touch**: `~/.ssh/`, `/etc/`, any `.env*`, anything under `private/`, Tier-4 closed-core book corpus.
10. **Working directory**: `/home/ruslan/jetix-os/`. Do not `cd` outside.

---

## §11 STOP Rule + Ack Mantra

### §11.1 STOP rule

After AWAITING-APPROVAL packet (`§8.7`) is committed and pushed:

**STOP. DO NOT auto-launch Bundle 3.**

Bundle 3 (Parts 5 + 8) will only dispatch AFTER Ruslan reviews and acks Bundle 2 AWAITING-APPROVAL packet. Brigadier waits for HITL signal.

Final action: notify Ruslan via tmux output (or stdout if no tmux):

> «Wave C Bundle 2 complete. AWAITING-APPROVAL packet at `decisions/AWAITING-APPROVAL-wave-c-bundle-2-2026-04-XX.md`.
> Word count summary: Part 2 = N, Part 3 = N, Part 4 = N. Wisdom Loop adoption: N YES (Operational X / Philosophical Y) / N NO. Operational ratio: ZZ%.
> C1 Joint Design canonical answer documented at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` + `swarm/lib/README.md`.
> routing-table.yaml at `swarm/lib/routing-table.yaml` with N distinct routing rules (target ≥20).
> task-return-packet.json schema fully specified in Part 4 §I (UND-1 binding).
> M1/M2/M3/M4/M5 gates: PASS / PASS / 4/4 PASS / PASS / PASS.
> Awaiting Ruslan ack before Bundle 3 dispatch.»

### §11.2 Autocheck — when to halt early

- **Walltime exceeds 28h**: STOP, report status to Ruslan, ask how to proceed. Do NOT push past 28h without ack.
- **Subagent first attempt produces low-quality output** (cargo-cult signals, missing sections, under word count, IP-1 violations in Part 4): re-dispatch ONCE with explicit feedback citing this prompt's quality bar. Second attempt also fails: escalate.
- **Wisdom Application Loop produces 0 "YES Adopted" for a part**: per §5.4, halt + flag + escalate.
- **Operational adoption ratio < 60% across Bundle 2 after Wisdom Loop**: investigate; re-dispatch integrator to convert PHILOSOPHICAL adoptions into OPERATIONAL ones. If persistent: escalate to Ruslan.
- **C1 Joint Design produces conflicting answers from Part 3 + Part 4 integrators**: escalate to brigadier-mode arbitration; if answer materially differs from "shared infra `swarm/lib/` with Part 3 lead" → Ruslan ack required.
- **Critic gate produces irreconcilable dissent across ≥2 experts**: preserve dissent (AP-6) + escalate to Ruslan via dissent.md.
- **Schema design produces ambiguity that requires RUSLAN-LAYER decision**: pause, write `swarm/wiki/foundations/<part-slug>/oq-bundle-2-N.md`, escalate.
- **IP-1 violation detected in Part 4 routing-table.yaml or any Part 4 artefact** (executor name, model name, agent file path appearing in Foundation): immediate re-dispatch with explicit IP-1 enforcement reminder; if recurring: escalate.

### §11.3 Budget

~30-40 subagent dispatches across phases (5×4 matrix × 3 parts × dispatched cells + integrators + Joint Design Phase + Wisdom Loop pass + critic gates + M-gates). Budget guard: if dispatch count exceeds 50, audit for redundant cells; if exceeds 60, halt and ask Ruslan.

### §11.4 Mantra (recite before each phase transition)

> **QUALITY > SPEED.**
> **PROVENANCE > VOLUME.**
> **WISDOM-APPLIED > WISDOM-CITED.**
> **OPERATIONAL > PHILOSOPHICAL.**
> **RUSLAN-ACK > BRIGADIER-CONFIDENCE.**
> **C1 BLOCKING — Part 3 + Part 4 must agree.**
>
> *Bundle 2 wires the information lifecycle and agent coordination layers atop the Bundle 1 substrate. Every decision compounds for Phase B/C/D. Treat with 1 trillion percent responsibility.*

---

## §12 Pre-flight Checklist (brigadier runs before first dispatch)

- [ ] Read this prompt three times
- [ ] Read all of §3.1 Constitutional baseline (Bundle 1 LOCKED — DO NOT re-litigate F-G-R, Default-Deny, AWAITING-APPROVAL packet schema, blast-radius, Halt-Log-Alert, Corrigibility)
- [ ] Read all of §3.2 Wave A artefacts (esp. wave-c-worklist §2 Parts 2/3/4)
- [ ] Read relevant subsets of §3.3 (per part — see §3.3 mapping)
- [ ] Read §3.4 Wave B Supplement library-direct sources (Young 2010 CQRS for Part 2 + Part 4; Bai 2022 + Askell 2021 for Part 4)
- [ ] Skim §3.5 existing operational artefacts (esp. `tools/transcribe.py` etc. for Part 2; `wiki/` baseline for Part 3; `.claude/agents/brigadier.md` + 5 expert agents for Part 4 routing extraction)
- [ ] Verify branch `claude/jolly-margulis-915d34` is current and clean
- [ ] Verify `unset ANTHROPIC_API_KEY` (operator should have done this)
- [ ] Verify `swarm/lib/shared-protocols.md` consulted
- [ ] Acknowledge §0 Mission Statement and §11.4 Mantra internally before first dispatch
- [ ] Confirm dispatch sequence: Part 2 → Part 3 → Part 4 (with Joint Design Phase between Part 3 + Part 4 integrators per §4.2)
  - Alternative: Parts 3 + 4 in parallel within HD-02 N=2 (both integrator phases can run in parallel; Joint Design Phase synchronizes them)
- [ ] Confirm output paths in §8 are mkdir-ready (parent dirs exist or will be created)

When all bullets ticked: dispatch Phase A pre-read confirmation. Then proceed.

---

## §13 Reference — what NOT to do

1. **DO NOT re-litigate Bundle 1 LOCKED schemas** (F-G-R, Default-Deny, blast-radius, AWAITING-APPROVAL packet schema, Halt-Log-Alert, Corrigibility). Bundle 2 CONSUMES these as F8 constitutional contracts.
2. **DO NOT skip the Joint Design Phase.** Parts 3 + 4 cannot be designed sequentially-in-isolation on C1.
3. **DO NOT skip the Wisdom Application Loop.** It is the central directive.
4. **DO NOT auto-launch Bundle 3.** Always STOP after Bundle 2 AWAITING-APPROVAL.
5. **DO NOT fabricate Wisdom YES entries** to satisfy the loop. Zero adoption with reasoning > fake adoption.
6. **DO NOT use generic `depends-on` edges.** A.14 typed edges only.
7. **DO NOT cite without consequence sentence within 200 chars.** Cargo-cult is the failure mode.
8. **DO NOT exceed 25K words per part doc with redundancy padding.** Tighten before critic.
9. **DO NOT come in under 15K words per part doc.** Re-dispatch integrator.
10. **DO NOT silently override expert dissent.** Preserve in dissent.md.
11. **DO NOT touch the Untouchable trees** (§10.8) or Security paths (§10.9). Bundle 2 P4.1 EXTRACTS routing logic from agent system prompts — does NOT modify those files.
12. **DO NOT push to `main`.** Branch `claude/jolly-margulis-915d34` only.
13. **DO NOT use `--amend` / `--no-verify` / force-push.**
14. **DO NOT reference any provider API-key env var** in code paths brigadier produces.
15. **DO NOT confuse Foundation with RUSLAN-LAYER.** §X section is mandatory.
16. **DO NOT include executor names in Part 4 Foundation artefacts.** IP-1 strict — model names, agent file paths, instance IDs are RUSLAN-LAYER `executor-binding.yaml` only. Critic gate AUTO-REJECTS violations.
17. **DO NOT duplicate the C1 canonical answer in Part 3 §I and Part 4 §I.** Single canonical answer in `swarm/lib/README.md` + `C1-joint-design.md`; both §I sections REFERENCE.
18. **DO NOT drift the Part 1 §I.5 task-return-packet stub fields** when Part 4 §I fully specifies the schema. Frozen-fields invariant: stub fields appear UNCHANGED in full schema.
19. **DO NOT propose bullets outside §2 scope.** Bundle 2 = Parts 2 + 3 + 4 with the 10 bullets enumerated. Other parts (5, 7, 8, 9, 10) are NOT in Bundle 2.
20. **DO NOT bias toward PHILOSOPHICAL adoptions** in Wisdom Loop. Bundle 2 explicit operational bias per Ruslan feedback.
21. **DO NOT confuse Bundle 2 scope with the brigadier's Bundle 1 §7 error.** Bundle 1 AWAITING-APPROVAL §7 wrote "Bundle 2 = Parts 2 + 7" — this was an ERROR. Correct scope is **Parts 2 + 3 + 4** per Master Plan + wave-c-worklist §3.

---

## §14 Final note from Ruslan (paraphrased intent, brigadier internalize)

Bundle 2 is the second compounding step. Bundle 1 froze the constitutional contracts; Bundle 2 wires the productive layers atop them. From here on:
- Every information signal entering the system flows through Part 2 → Part 6b STOP gate → Part 6a F-G-R tag → Part 3 promotion → Part 1 commit. The pipeline is closed-loop.
- Every agent dispatch flows through Part 4 routing-table.yaml → mailbox dispatch → task-return-packet → Part 5 (Bundle 3) compound extraction. The coordination is closed-loop.
- Every fork (Phase B partner, Phase C product, Phase D org) imports the Bundle 2 schemas (routing-table.yaml STRUCTURE, task-return-packet.json schema, PARA-tier discipline) as Foundation generics; Ruslan-specific bindings (executor-binding.yaml, specific routing entries, voice-pipeline tools) overlay as RUSLAN-LAYER.

If Bundle 2 is half-baked, Bundle 3 (Part 5 compound + Part 8 health) inherits weak signals. If Bundle 2 over-engineers Phase B/C/D scenarios, Phase A delivery drags.

The right level: **single-owner Phase A €50K horizon, but FORK-READY to scale**. routing-table.yaml extracted now (≥20 variety rules) prevents federated-coordinator surgery later. task-return-packet.json fully specified now means Part 5 (Bundle 3) consumes a frozen contract, not a moving target. C1 Joint Design canonical answer means Phase B forks know exactly which scripts to fork and which to leave shared.

This is the architecture document a Phase B partner can read in 60 minutes (vs. 90 for Bundle 1 — Bundle 2 is "everyday operations") and import in half a day. Make it the document where the WISDOM IS APPLIED OPERATIONALLY (not philosophically) — Ruslan asked for ≥60% operational because Bundle 1 was 50/50 and the philosophical half was "academic boundary text" rather than concrete code-level deltas. Bias toward changing schema fields, lint checks, edge types, algorithms — not toward adding paragraphs of framing prose.

**C1 BLOCKING — Part 3 + Part 4 must agree, jointly, in a single canonical artefact. Not two §I sections that almost line up. One answer.**

---

*End of deep prompt. Brigadier dispatch begins after §12 pre-flight checklist passes.*

*Mantra (final): QUALITY > SPEED. PROVENANCE > VOLUME. WISDOM-APPLIED > WISDOM-CITED. OPERATIONAL > PHILOSOPHICAL. RUSLAN-ACK > BRIGADIER-CONFIDENCE. C1 BLOCKING — Part 3 + Part 4 must agree.*
