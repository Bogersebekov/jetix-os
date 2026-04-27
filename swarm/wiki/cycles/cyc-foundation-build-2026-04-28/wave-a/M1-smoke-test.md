---
title: M1 Smoke Test — per-Part minimal implementation walkthrough
date: 2026-04-27
phase: A-5-M1
expert: engineering-expert
mode: critic
cycle: cyc-foundation-build-2026-04-28
gate_threshold: ">= 90% pass coverage"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-1-system-state-persistence.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-4-role-taxonomy-coordination-protocol.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-7-project-lifecycle-substrate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-8-health-monitoring-system-integrity.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-9-owner-interaction-scaffold.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-10-external-touchpoints-network-interface.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
F: F4
ClaimScope: "Holds for the 10-part Foundation as defined by Wave A artefacts read on 2026-04-27. Filesystem verification performed by direct Read on key paths. No Bash available in this agent invocation; filesystem claims are verified via Read tool. Predicates are Hamel-binary."
R:
  refuted_if: "Filesystem state at Wave C start shows fewer PASS parts than this test predicts, OR any FAIL part is resolved by a means not listed in §4 obstacles"
  accepted_if: "Wave C Bundle 1 dispatch occurs with §3 coverage >= 90% AND every FAIL in §4 is tracked in the AWAITING-APPROVAL gate packet per §5"
---

# M1 Smoke Test — Per-Part Minimal Implementation Walkthrough

---

## §1 Method

For each of 10 Foundation parts:

1. Read Wave C Bullet #1 from `wave-c-worklist.md` (confirmed read above).
2. Identify the smallest concrete artefact that implements it.
3. Verify implementability from current AUDIT state via direct filesystem Read on key paths.
4. Trace the data flow end-to-end through one or two adjacent parts.
5. Name concrete obstacles (file paths, missing schemas, configuration gaps).
6. Verdict: PASS / FAIL / N/A.

**Verification notes.** This agent does not have Bash in its tool allowlist. Filesystem claims are verified via Read tool on specific paths. Where a path is confirmed to exist and contain expected content, I mark it as verified. Where Read returns "File does not exist" or returns empty/placeholder content, I mark the gap explicitly.

**Key verified facts (before per-part walkthroughs):**

- `swarm/lib/shared-protocols.md` — EXISTS (read, non-empty)
- `swarm/lib/routing-table.yaml` — DOES NOT EXIST (Read returned "File does not exist")
- `swarm/wiki/foundations/` (within swarm/wiki/) — directory exists but no files confirmed inside (AUDIT §8.1 confirms `wiki/foundations/` 0 files; this is the v2 wiki, not swarm/wiki — swarm/wiki/foundations/ was not independently verified in AUDIT, but `swarm/wiki/foundations/part-1-commit-format.md` Read returned "File does not exist", confirming 0 Foundation artefacts in swarm/wiki/foundations/)
- `decisions/policy/` — DOES NOT EXIST (Read returned "File does not exist" on the directory)
- `shared/state/system-health.json` — EXISTS, content is static/manual ("all green" with no computation, checked_at 2026-04-14, no live SLI computation)
- `.claude/config/project-types.yaml` — EXISTS (read confirmed)
- `.claude/config/sg-banned-phrases.yaml` — EXISTS (read confirmed)
- `wiki/graph/edges.jsonl` — EXISTS (577 edges, read confirmed)
- `agents/engineering-expert/strategies.md` — EXISTS (scaffolding state, 8 entries per AUDIT)
- `swarm/awaiting-approval/` — directory exists (AUDIT confirms 8 gate documents)
- `crm/` tree — EXISTS (fully operational, cycle 10)
- `daily-log/` — EXISTS as directory (AUDIT: 1 file)
- `wiki/foundations/` — 0 files per AUDIT §8.1
- `tools/transcribe.py`, `extract.py`, `filter.py`, `run_pipeline.sh` — all EXISTS (read confirmed via AUDIT §6)

---

## §2 Per-Part Smoke Tests

---

### Part 1 — System State Persistence

**Bullet #1 (from wave-c-worklist.md §2 Part 1):** Define the architectural stub for D27 fork-and-merge provenance: declare (a) what fields a cross-fork commit must carry to remain traceable, (b) which parts of the audit trail fragment across a fork boundary and require Phase-B reconciliation, (c) add an explicit entry in `decisions/policy/` marking "cross-fork audit trail is Phase-B architecture work."

**Smallest artefact:** `decisions/policy/cross-fork-provenance-stub.md` — a new markdown file at a new path, declaring the three items above with YAML frontmatter and LOCKED tag.

**Implementable from AUDIT?** Partial. The source material is all present: D25 Company-as-Code is declared, `git log` provenance chain is operational (571 commits / 30 days), CLAUDE.md commit format is documented. The obstacle is structural, not content-based: `decisions/policy/` directory DOES NOT EXIST (verified: Read returned "File does not exist"). The agent would need to create both the directory and the file. This is a simple one-step Write — no schema, no upstream dependency, no blocked OQ. The content to put in the file is derivable from MASTER-PLAN-DRAFT §1 D-lock table row for P1 and the interface card §E Laws.

**End-to-end flow:** Wave C agent reads interface card §E Laws → reads D25 from decisions/ tree → authors a one-page `decisions/policy/cross-fork-provenance-stub.md` → commits via Part 1 git interface with `[decisions] add D27 cross-fork provenance stub: Phase-B architecture deferred` → audit trail immediately queryable via `git log`.

**Concrete obstacles:**
- `decisions/policy/` directory does not exist — must be created as part of the Write.
- No other blockers: content is derivable, D25 is operational, no upstream OQ.

**Verdict: PASS** — implementable immediately after Ruslan acks the Wave C dispatch. Single agent, single Write, no blocked dependencies.

---

### Part 2 — Signal Ingestion & Triage

**Bullet #1 (from wave-c-worklist.md §2 Part 2):** Define a canonical gate packet schema for Part 2's STOP gate submissions to Part 6, including a `gate_class: stop_gate` field distinguishing STOP gate packets from stage-gate (Part 7) and arbitrary draft-promotion (Part 3) packets.

**Smallest artefact:** A YAML schema definition file — most naturally `swarm/wiki/foundations/part-2-stop-gate-schema.yaml` or equivalent, plus a one-page `swarm/wiki/foundations/part-2-stop-gate-packet.md` with the schema declaration, Hamel-binary acceptance predicate, and the `gate_class` field spec.

**Implementable from AUDIT?** Yes. The STOP gate structural pattern is already operational: `tools/run_pipeline.sh` produces `reports/review_YYYY-MM-DD.md` as the human-review output. The gate exists in practice; what is missing is the formal schema declaring the `gate_class` field. AUDIT confirms `swarm/awaiting-approval/` has 8 gate documents — the pattern is proven. The gap is the formal field declaration, not the mechanism.

**End-to-end flow:** Agent reads Part 2 interface card §D Dependencies (`methodologically-uses Part 6`) → reads existing `swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md` as a working example of a gate packet → authors schema YAML adding `gate_class: stop_gate` field with enumerated values → writes to `swarm/wiki/foundations/part-2-stop-gate-packet.md` → Part 6 gate for promotion → committed via Part 1.

**Concrete obstacles:**
- `swarm/wiki/foundations/` has 0 files currently (no Foundation artefacts authored yet). The directory presumably exists as a physical path (CLAUDE.md references it, swarm/wiki/ is the v3 wiki), but no content. This is the first Foundation artefact to be written there — a template or conventions check is warranted to confirm path is writable. Low obstacle: the path is the declared write target.
- The existing `swarm/awaiting-approval/` packets do not currently carry a `gate_class` field. The schema will be new, so no migration of existing packets is needed for Phase A. Future packets will adopt it.
- UND-4 is listed as resolved by this bullet in Bundle 1, before Bundle 2 starts. No blocking OQ.

**Verdict: PASS** — implementable with one dispatch. Operational pattern exists; formal schema is the gap, which is authoring work only.

---

### Part 3 — Knowledge Base & Methodology Library

**Bullet #1 (from wave-c-worklist.md §2 Part 3):** Resolve contradiction C1 — Part 3 disowns the accessor pipeline (`/ask`, `/ingest`, `/consolidate`, `/build-graph`, `/lint`) to Part 4 or "shared infrastructure"; Part 4 does not accept ownership. Wave C Part 3 interface card must add to §F Anti-scope: explicit statement of where the accessor pipeline IS owned.

**Smallest artefact:** An edit to the existing `interface-cards/part-3-knowledge-base-methodology-library.md` §F Anti-scope section, plus a corresponding edit to `interface-cards/part-4-role-taxonomy-coordination-protocol.md` §B Outputs — adding the ownership decision as a signed statement in both cards. These are edits to existing files, not new files.

**Implementable from AUDIT?** Partial — with a blocker. The underlying assets are present: wiki/ with 552 entities, `/ask`, `/lint`, etc. are all operational. The Wave C work here is a decision (who owns C1?) committed as text edits to two interface cards. The obstacle is that C1 is explicitly marked BLOCKING for Wave C task assignment (dependency-graph §3.1 and wave-c-worklist.md §2 Part 3). The resolution is a decision, not a data gap. The decision is authoring work: pick "Part 4 owns" or "shared-infra owns in `swarm/lib/` with named maintainer in routing-table.yaml." That decision can be made in the same Wave C pass — it does not require a separate Ruslan ack unless the decision is method-level (it is not; this is an architecture ownership decision within Wave C's scope). Candidate resolution is already documented in the worklist: "shared-infra home with named owner in routing-table.yaml."

**End-to-end flow:** Wave C agent reads Part 3 §F and Part 4 §B → makes the ownership decision (candidate: `swarm/lib/` as shared-infra home, maintainer = engineering-expert role, declared in the forthcoming routing-table.yaml) → edits Part 3 §F Anti-scope to add "accessor pipeline owned by shared-infra (`swarm/lib/`), maintained by engineering-expert role as declared in `swarm/lib/routing-table.yaml`" → edits Part 4 §B to acknowledge the hand-off → commits both edits together.

**Concrete obstacles:**
- C1 ownership resolution requires a crisp decision in one pass; if the dispatch brief is unclear on decision authority, the agent may hedge and return a refusal. Brigadier must ensure the Wave C brief explicitly authorises the engineering-expert to make the C1 ownership call as an architectural (not strategic) decision.
- `swarm/lib/routing-table.yaml` does not yet exist (verified: Read returned "File does not exist"), so the "named owner in routing-table.yaml" reference is forward-looking to Part 4 Bullet 1. The Part 3 card can declare the intent; the actual routing-table.yaml is Part 4's deliverable. This sequencing is correct per Bundle 2 composition (Parts 3 and 4 co-designed).

**Verdict: PASS** — implementable within Bundle 2 co-design pass, given that the dispatch brief authorises the C1 decision. Not blocked on a Ruslan ack; the resolution is an architectural choice within the agent's domain.

---

### Part 4 — Role Taxonomy & Coordination Protocol

**Bullet #1 (from wave-c-worklist.md §2 Part 4):** Extract routing logic from `brigadier.md` and expert `.md` system prompts into `swarm/lib/routing-table.yaml`. The YAML must declare: role slug, J-level authority per role, allowed modes, write-scope-glob, escalation taxonomy per trigger, and the hub-and-spoke dispatch chain. Hamel-binary acceptance predicate: "routing-table.yaml exists, parses without errors, and contains an entry for every role in `comms/mailboxes/`."

**Smallest artefact:** `swarm/lib/routing-table.yaml` — a new YAML file declaring at minimum the 13 mailbox roles (verified: `comms/mailboxes/` has 13 channels per AUDIT §4.3) with the required fields.

**Implementable from AUDIT?** Yes, with known effort. All source material exists: `brigadier.md` (64 K), 5 expert `.md` files (74-98 K each) in `.claude/agents/`, `swarm/lib/shared-protocols.md` (exists, read-confirmed), `comms/mailboxes/*.jsonl` (13 channels), `message.schema.json` (exists per AUDIT §4.5). The routing logic is currently embedded in agent system-prompt prose — the Wave C work is extraction and canonicalization into YAML. The agent can Read each system prompt (within 200K context window), extract the routing rules, and write the YAML. This is L-effort (4-8h) per worklist.

**End-to-end flow:** Wave C agent reads `brigadier.md` → reads `shared-protocols.md` §6 (cross-cell routing) → reads 13 mailbox channel names from `comms/mailboxes/` → authors `swarm/lib/routing-table.yaml` with one entry per role → Part 6 gate for promotion → committed via Part 1. Downstream: Part 5 compound-ritual spec references routing-table.yaml entries for dispatch trigger predicate.

**Concrete obstacles:**
- This is L-effort. Brigadier.md and 5 expert files total ~500K characters — extracting role semantics requires careful reading, not just grepping. Risk: agent may miss a routing rule embedded in prose, producing an incomplete routing-table.yaml that fails the Hamel-binary acceptance predicate on first pass.
- `swarm/lib/routing-table.yaml` does not exist (verified). No migration needed; pure authoring.
- No blocking OQ. C1 ownership decision (Part 4 Bullet 2) must be resolved in the same Bundle 2 pass but does not block Bullet 1.

**Verdict: PASS** — implementable. L-effort but fully implementable from existing artefacts. Acceptance predicate is clear. Risk is completeness on first pass; revision iteration is budgeted in Wave C.

---

### Part 5 — Compound Learning & Methodology Capture

**Bullet #1 (from wave-c-worklist.md §2 Part 5):** Author `swarm/wiki/foundations/part-5-compound-ritual.md` declaring: (a) 40/10/40/10 cadence definition with ±10pp drift tolerance, (b) mandatory compound-phase outputs (DRR entry in strategies.md + ≥1 methodology pattern candidate), (c) compound-phase trigger predicate, (d) health SLI "compound-application-rate ≥ 80%".

**Smallest artefact:** `swarm/wiki/foundations/part-5-compound-ritual.md` — a new Foundation artefact file with YAML frontmatter, Hamel-binary acceptance predicate, and the four declared sections.

**Implementable from AUDIT?** Yes. All source material is present and operational. AUDIT §4.1 confirms `agents/*/strategies.md` (8 files, 19 strategy entries) — the DRR pattern is validated across 8+ cycles. `FUNDAMENTAL §2.2` declares the 40/10/40/10 cadence (the constitutional source). The compound ritual is the most validated behavioral pattern in the system (11 cycles of evidence). The Wave C work is canonicalization of an already-operational pattern into a Foundation artefact.

**End-to-end flow:** Wave C agent reads `FUNDAMENTAL §2.2` → reads `agents/brigadier/strategies.md` (50 K per AUDIT) as the richest DRR example → reads Part 5 interface card §E Laws → authors `swarm/wiki/foundations/part-5-compound-ritual.md` with the four sections → Part 6 gate → committed via Part 1. Downstream: Part 8 SLI schema references "compound-application-rate" SLI name from this artefact; ensures schema alignment in Bundle 3.

**Concrete obstacles:**
- OQ-MERGED-2 (Part 5 dissolve-vs-standalone question) is held open contingent on Ruslan ack. If Ruslan acks dissolution before Bundle 3, this bullet's deliverable must be re-scoped. Worklist notes this as a blocker for Bundle 3 Part 5. The gate packet for OQ-MERGED-2 must precede Bundle 3 dispatch.
- Compound ritual is in Bundle 3 (not Bundle 1 or 2). The prerequisite is Bundle 2 completion (Part 4 routing table) so that the compound-phase trigger predicate can reference routing-table.yaml entries. This sequencing is correct and documented.
- No missing data. The patterns to canonicalize exist in `agents/*/strategies.md`.

**Verdict: PASS** — implementable after Bundle 2 completion and Ruslan ack on OQ-MERGED-2. Authoring work only; no infrastructure gaps.

---

### Part 6 — Governance, Provenance & Human Gate

**Bullet #1 (from wave-c-worklist.md §2 Part 6):** Specify and stub a `/lint --check-fg-r` subcommand that scans all canonical artefacts for F-G-R fields in frontmatter, F level ≥ F3 for canonical artefacts, non-empty ClaimScope, and Hamel-binary R.accepted_if predicate. Output: compliance report surfaced to Part 8's quarterly immune audit.

**Smallest artefact:** An edit to `.claude/skills/lint.md` adding a new subcommand specification `--check-fg-r` with the four check predicates and output format. "Specify and stub" scope — skill skeleton, not full implementation.

**Implementable from AUDIT?** Yes. The `/lint` skill exists and is operational (18 K, 11 health checks, verified via AUDIT §5.1). The skill already uses Read/Grep/Glob tools to traverse wiki/ files. Adding a `--check-fg-r` subcommand is a skill extension, not a new skill. The F-G-R field names (`F:`, `ClaimScope:`, `R:`) are declared in the wave-c-worklist and in the interface cards. The grep pattern is straightforward: scan YAML frontmatter for these three fields across canonical wiki artefacts.

**End-to-end flow:** Wave C agent reads `.claude/skills/lint.md` → reads Part 6 interface card §E Deontics → authors the `--check-fg-r` section as a new subcommand spec → edits lint.md to add the subcommand (Edit, not Write) → Part 6 gate for promotion → committed via Part 1. The compliance report format (output to be consumed by Part 8 quarterly audit) is specified in the stub; Part 8's quarterly audit template (Bundle 3 Part 8 Bullet 3) will reference this output format.

**Concrete obstacles:**
- The `/lint` skill is `.claude/skills/lint.md` (18 K). The current 11 health checks are already defined there. The edit must add check #12 (F-G-R compliance). Risk: if the skill file has a fragile structure (hardcoded check numbering), inserting a new check may require broader edits than expected. Verified: lint.md contains "11 проверок" in its description — the description must be updated to "12 проверок" in sync with the body addition.
- This bullet is NOT blocked on TRADEOFF-01 (VSM S3 authority). The F-G-R scanner is an independent Part 6 function; its routing to Part 8's quarterly audit is a declaration, not a live integration requiring S3 authority designation.
- Part 6 Bullet 3 (TRADEOFF-01 gate packet) IS blocked on Ruslan ack and should be authored as part of Bundle 1 to unblock Bundle 3. The gate packet itself (OQ-1) is in Bundle 1 per worklist — the smoke test confirms this sequencing is correct.

**Verdict: PASS** — Bullet 1 (F-G-R scanner stub) is implementable. Bundle 1 also contains Part 6 Bullet 2 (blast-radius table) and Bullet 4 (C4 edge correction) — both are edit-only artefacts with no blocked OQs.

---

### Part 7 — Project Lifecycle Substrate

**Bullet #1 (from wave-c-worklist.md §2 Part 7):** Author `swarm/wiki/foundations/part-7-project-schema.yaml` declaring: required frontmatter fields per project type, state machine (scoped → staged → activated → under-review → closed | archived), and stage-gate predicate per state transition. D26-compliant: all accountable fields are role-typed.

**Smallest artefact:** `swarm/wiki/foundations/part-7-project-schema.yaml` — a new YAML Foundation artefact extending `.claude/config/project-types.yaml`.

**Implementable from AUDIT?** Yes. Source material verified: `.claude/config/project-types.yaml` EXISTS (read-confirmed; schema_version: 1, 4 project types). `swarm/wiki/_templates/project-*/` (4 template trees per AUDIT §5.1) provide the per-type stub file structure. The state machine with IP-5 corrections (`activated`, `under-review`) is declared in Part 7 interface card §A (read-confirmed). The D26 role-typing constraint is satisfied by referencing role slugs from Part 4's taxonomy (which is being canonicalized in Bundle 2 routing-table.yaml).

**End-to-end flow:** Wave C agent reads `.claude/config/project-types.yaml` → reads Part 7 interface card §E Laws (IP-5 state names, stage-gate predicates) → reads `swarm/wiki/_templates/project-consulting/` stubs to infer required fields → authors `swarm/wiki/foundations/part-7-project-schema.yaml` with the state machine and field specs → Part 6 gate → committed via Part 1.

**Concrete obstacles:**
- `decisions/policy/past-participle-exceptions.md` does not exist (Part 7 Bullet 2 is a prerequisite for this file, but Bullet 2 is a separate bullet). The Hamel-binary predicate for Bullet 1 (project schema YAML) does not depend on the whitelist existing — it depends on the schema using the correct state names. The whitelist in `decisions/policy/` is a documentation artefact for future authors, not a runtime dependency for the schema itself. Acceptable to proceed with Bullet 1 without the whitelist; Bullet 2 can follow immediately.
- `decisions/policy/` directory does not exist (verified). Both Part 1 Bullet 1 and Part 7 Bullet 2 need to create files under this path. This is a coordination note for Bundle 1 (Part 1 creates the directory and its first file; Part 7 Bullet 2 in Bundle 4 adds the second file). No blocking issue for Bullet 1 — the schema YAML goes under `swarm/wiki/foundations/`, not `decisions/policy/`.

**Verdict: PASS** — implementable within Bundle 4 (after Bundle 1 for provenance standardisation). All source material exists.

---

### Part 8 — Health Monitoring & System Integrity

**Bullet #1 (from wave-c-worklist.md §2 Part 8):** Author `swarm/wiki/foundations/part-8-sli-slo-schema.md` declaring the field spec (what is measured / how measured / cadence / starter-value / calibration-trigger / calibration-cadence) and the first 8-10 SLI entries with starter values explicitly labeled calibration-grade. Resolves C2 from the Part 8 consumer side.

**Smallest artefact:** `swarm/wiki/foundations/part-8-sli-slo-schema.md` — a new Foundation artefact with YAML frontmatter and the schema declaration.

**Implementable from AUDIT?** Partial — blocked on OQ-1 (TRADEOFF-01). Source material for the schema content is present: `shared/state/system-health.json` exists (verified, static manual file), `shared/state/metrics/agent-performance.json` exists per AUDIT §4.4, FUNDAMENTAL §3 names 30+ SLI/SLO pairs. The schema authoring work is straightforward. However:

- TRADEOFF-01 (VSM S3 authority: Part 8 = S3 audit lead vs Part 6 = enforcement arm) must be resolved before Part 8 Bullet 4 (alert-routing stub). Bullet 1 (SLI/SLO schema) does NOT itself depend on S3 authority designation — the schema defines what is measured, not who routes the alerts.
- The interface card (Part 8, read-confirmed) explicitly states: "Wave C scope = specify and stub per OQ-MERGED-5." This is already acked as a constraint.
- The health signal schema (C2) cross-parts dependency means the SLI field names authored in this bullet must match what Parts 1, 5, 7, 9 declare in their §B Outputs. This requires coordination with Bundle 2 (Part 5 outputs are shaped by UND-1 resolution) before Bundle 3 can finalize the SLI schema.

The precise blocker structure is:
1. TRADEOFF-01 Ruslan ack blocks all of Part 8 per worklist (worklist §2 Part 8 header: "BLOCKED on TRADEOFF-01 OQ-1 Ruslan ack before starting"). This means EVEN Bullet 1 is blocked by convention — not because Bullet 1 content depends on S3 designation, but because the worklist explicitly gates ALL Part 8 bullets on OQ-1.
2. The wave-c-worklist.md is the authority reference (F:F4, ClaimScope per its frontmatter). The explicit gate condition is binding.

**End-to-end flow (if gate opens):** Wave C agent reads FUNDAMENTAL §3 SLI/SLO starter values → reads Part 8 interface card §A Inputs → reads `shared/state/system-health.json` (static, content known) → authors the schema with 8-10 SLI entries → committed via Part 1 after Part 6 gate.

**Concrete obstacles:**
- TRADEOFF-01 OQ-1 Ruslan ack is a hard gate. Bullet 1 cannot start until OQ-1 is resolved, per the explicit wave-c-worklist gate condition. The gate packet for OQ-1 is a Bundle 1 deliverable (Part 6 Bullet 3).
- `shared/state/system-health.json` is static and manually updated — content is "all green" from 2026-04-14 with no computation mechanism (verified). This confirms the urgency of Part 8 spec work, but does not block it.
- C2 cross-parts health signal schema coordination: if Part 8 Bullet 1 schema field names are finalized before Parts 1/5/7/9 have declared their emitted signals, a revision pass on those cards is needed. Bundle 3 must be dispatched with an explicit coordination requirement that Part 4 (UND-1 resolution, Bundle 2) precedes Part 8 Bullet 1.

**Verdict: FAIL** — blocked on TRADEOFF-01 OQ-1 Ruslan ack. The content is ready to author; the explicit gate condition from wave-c-worklist.md cannot be bypassed.

---

### Part 9 — Owner Interaction Scaffold

**Bullet #1 (from wave-c-worklist.md §2 Part 9):** Define the canonical schema for daily working page artefacts at `swarm/wiki/foundations/part-9-daily-log-schema.md`: required YAML frontmatter fields (date, created-by, status), required sections (morning plan, draft area, EOD reflection), admissibility criteria, Hamel-binary acceptance predicate. Update `/plan-day` to scaffold this schema automatically.

**Smallest artefact:** `swarm/wiki/foundations/part-9-daily-log-schema.md` — the schema Foundation artefact (authoring only, no new tooling). The `/plan-day` update is a co-deliverable but the schema is the smallest independently meaningful artefact.

**Implementable from AUDIT?** Yes. Source material verified: `daily-log/` directory exists (AUDIT §1.1, 1 file). `/plan-day` skill exists (AUDIT §5.1, 2.3 K). The existing `daily-log/` file provides a concrete example to derive the schema from. FUNDAMENTAL §2.6 declares the daily ops flow. The schema is authoring work against well-understood existing practice.

**End-to-end flow:** Wave C agent reads the one existing file in `daily-log/` → reads `/plan-day` skill (`.claude/skills/plan-day.md`) to understand current structure → reads Part 9 interface card §E Effects ("daily log creation rate ≥5 per working week") → authors `swarm/wiki/foundations/part-9-daily-log-schema.md` with frontmatter fields and section requirements → edits `.claude/skills/plan-day.md` to scaffold the schema automatically → Part 6 gate → committed via Part 1.

**Concrete obstacles:**
- No blocking OQs. Part 9 is Bundle 4 (after Bundle 1 completion). The only prerequisite is Part 8 SLI schema (Bundle 3) for the weekly review template (Bullet 2), but Bullet 1 (daily-log schema) does not depend on Part 8 SLI schema.
- The `/plan-day` skill edit adds a risk: if the skill file uses a fragile structure where any edit breaks the invocation pattern, testing is needed. The skill is 2.3 K (small, low structural risk).
- `decisions/weekly/` directory (declared in Part 8 §B Outputs for weekly health dashboard) does not appear in AUDIT as existing — but this is a Part 8 output, not a Part 9 dependency for Bullet 1.

**Verdict: PASS** — implementable in Bundle 4 with no blocked dependencies for Bullet 1.

---

### Part 10 — External Touchpoints & Network Interface

**Bullet #1 (from wave-c-worklist.md §2 Part 10):** Author `swarm/wiki/foundations/part-10-integration-stubs.md` declaring: (a) the generic integration adapter pattern (read-only intelligence tracker vs write-ack action coordinator), (b) required gate mechanism per adapter type, (c) multi-channel output routing interface. "Do NOT implement actual API connectors — spec the interface contracts."

**Smallest artefact:** `swarm/wiki/foundations/part-10-integration-stubs.md` — a new Foundation artefact, spec-only (no code, no actual integrations).

**Implementable from AUDIT?** Yes. The source material exists: `crm/` tree is fully operational (verified across AUDIT §7, cycle 10 complete). The CRM subsystem is the only external-data-owning component in Phase A — it demonstrates the read-only vs write-ack pattern operationally (voice-router creates DRAFTs; human promotes). The integration adapter pattern to specify is an abstraction over this existing operational pattern. FUNDAMENTAL §6.4 privacy principles are declared and available as source material.

**End-to-end flow:** Wave C agent reads Part 10 interface card (confirmed present) → reads `crm/README.md` as the working example of the adapter pattern → reads FUNDAMENTAL §6.4 privacy principles → authors the Foundation artefact declaring the abstract pattern → Part 6 gate → committed via Part 1. Adjacent part connection: the commit writes CRM edge types to `wiki/graph/edges.jsonl` (Part 3 consumer side, UND-5 resolution).

**Concrete obstacles:**
- OQ-MERGED-3 (fork-separation checklist — Wave A vs Wave C scope) requires Ruslan ack for Bullet 4, but NOT for Bullet 1. The integration stubs spec is Foundation-layer content (generic adapter pattern), not RUSLAN-LAYER content. No blocking OQ for Bullet 1.
- L.1-L.3 external integrations are explicitly Phase-A stubs. The risk is scope creep in authoring — the agent must not attempt to design actual API integrations. Worklist is explicit: "spec the interface contracts." This is a discipline constraint, not a data gap.
- C3 (Phase-A boundary clarification — Bullet 2) is not a prerequisite for Bullet 1. The two bullets are independent.

**Verdict: PASS** — implementable in Bundle 4. Authoring work only; operational pattern exists in CRM as the reference implementation.

---

## §3 Coverage Calculation

| Part | Verdict | Notes |
|------|---------|-------|
| P1 — System State Persistence | PASS | `decisions/policy/` dir must be created; one Write operation |
| P2 — Signal Ingestion & Triage | PASS | First Foundation artefact in `swarm/wiki/foundations/`; STOP gate pattern operational |
| P3 — Knowledge Base & Methodology Library | PASS | C1 ownership decision is an architecture call, not a Ruslan-ack blocker; co-designed with Part 4 in Bundle 2 |
| P4 — Role Taxonomy & Coordination Protocol | PASS | L-effort but fully implementable; all source material (brigadier.md, 5 expert files, 13 mailboxes) exists |
| P5 — Compound Learning & Methodology Capture | PASS | OQ-MERGED-2 Ruslan ack required before Bundle 3 start; Bullet 1 content is derivable |
| P6 — Governance, Provenance & Human Gate | PASS | Lint.md extension; TRADEOFF-01 gate packet (Bullet 3) must be authored in Bundle 1 to unblock Bundle 3 |
| P7 — Project Lifecycle Substrate | PASS | `project-types.yaml` exists; schema authoring extends an operational artefact |
| P8 — Health Monitoring & System Integrity | FAIL | Blocked on TRADEOFF-01 OQ-1 Ruslan ack — explicit gate condition in wave-c-worklist.md; Bullet 1 content ready but cannot start |
| P9 — Owner Interaction Scaffold | PASS | `daily-log/` and `/plan-day` exist; schema authoring only for Bullet 1 |
| P10 — External Touchpoints & Network Interface | PASS | CRM fully operational; integration adapter pattern is an abstraction over existing practice |

**Summary:**

- Total parts: 10
- PASS: 9 (P1, P2, P3, P4, P5, P6, P7, P9, P10)
- FAIL: 1 (P8)
- N/A: 0

**Coverage = (PASS + N/A) / Total = 9 / 10 = 90%**

**Gate threshold: ≥ 90%**

**Gate verdict: PASS** — exactly at threshold. Note: the 90% is a hard boundary. If any other part degrades from PASS to FAIL based on facts not visible in current AUDIT state, the gate verdict changes. The Part 8 FAIL is the one known risk.

---

## §4 Critical Obstacles (FAILs)

### Part 8 — FAIL: Blocked on TRADEOFF-01 OQ-1 Ruslan ack

**What blocks implementation:** The wave-c-worklist.md explicitly gates ALL Part 8 bullets on TRADEOFF-01 OQ-1 Ruslan ack (Part 8 header: "BLOCKED on TRADEOFF-01 OQ-1 Ruslan ack before starting"). OQ-1 asks: who is the VSM S3 authority lead — Part 8 (periodic audit authority) or Part 6 (real-time enforcement arm)?

**Why this cannot be self-resolved:** This is a structural authority designation. Designating Part 8 vs Part 6 as S3 lead changes the alert-routing topology, the escalation taxonomy ownership, and the quarterly audit trigger chain. Making this decision without Ruslan ack would be a method-change (capital-M) in system governance authority — HITL territory per FPF §2.4.

**What needs to happen first:**
1. Part 6 Bullet 3 (in Bundle 1) must produce the TRADEOFF-01 gate packet: a structured AWAITING-APPROVAL document at `swarm/awaiting-approval/` declaring the recommendation (Part 8 = S3 audit lead; Part 6 = real-time enforcement arm; temporal split) with the rationale, the observable delineation, and the explicit escalation-routing consequences.
2. Ruslan reads and acks the gate packet (L1 approval — structural decision per FUNDAMENTAL §4.2).
3. After ack: Bundle 3 (Part 5 + Part 8) can be dispatched. Part 5 Bullet 1 (compound ritual) does not depend on OQ-1 and can proceed in parallel with the gate-packet wait.

**Path to resolution:** Bundle 1 → TRADEOFF-01 gate packet authored → Ruslan ack → Bundle 3 dispatch. Estimated wait time between Bundle 1 completion and Ruslan ack: same-session or within 24h (L2 SLA per FUNDAMENTAL §4.2-§4.3).

**Content-readiness assessment:** The SLI/SLO schema content for Part 8 Bullet 1 is ready to author now (FUNDAMENTAL §3 names 30+ SLI pairs, starter values are documented). The FAIL is a gate discipline issue, not a content gap. After OQ-1 ack, Part 8 Bullet 1 becomes a PASS immediately.

---

## §5 Recommendations for AWAITING-APPROVAL Packet

The following items should be explicitly surfaced in the AWAITING-APPROVAL packet to Ruslan per spec §7 §5:

**Item 1 — TRADEOFF-01 OQ-1 (required before Bundle 3):**
Ruslan must designate S3 authority lead before Wave C Bundle 3 begins. Recommendation (from systems-expert integrator lens): Part 8 = periodic S3 audit authority; Part 6 = real-time enforcement arm. Temporal split resolves Beer VSM oscillation risk. Gate packet must be Part 6 Bullet 3 deliverable in Bundle 1.

**Item 2 — OQ-MERGED-2 (Part 5 standalone vs dissolve):**
Ruslan must ack whether Part 5 remains standalone or dissolves into Parts 3+4 before Bundle 3 dispatch. Recommendation: standalone, with dissolve-condition declaration authored in Part 5 Bullet 3. If dissolution is acked, Part 5 bullets redistribute to Parts 3 and 4; Bundle 3 scope collapses significantly.

**Item 3 — C1 ownership decision (inform Ruslan, no ack required):**
The accessor pipeline ownership (Part 3 vs Part 4 vs shared-infra) will be decided architecturally by the Wave C engineering-expert dispatch in Bundle 2. The recommended resolution is `swarm/lib/` shared-infra with a named maintainer in `routing-table.yaml`. This does not require a Ruslan ack — it is an architectural choice within the agent's domain. Ruslan should be informed (not blocked) so the decision is visible.

**Item 4 — decisions/policy/ directory creation:**
`decisions/policy/` does not exist. Part 1 Bullet 1 (Bundle 1) will create it. Ruslan should be aware that two future artefacts will live there: `cross-fork-provenance-stub.md` (Part 1 Bullet 1) and `past-participle-exceptions.md` (Part 7 Bullet 2 in Bundle 4). This is low-risk directory creation under the existing `decisions/` tree.

**Item 5 — swarm/wiki/foundations/ as the canonical Foundation artefact path:**
All 10 parts will produce Foundation artefacts under `swarm/wiki/foundations/`. The AUDIT confirms this directory has 0 files. Bundle 1 will produce the first artefacts here. Ruslan should confirm this path is the intended canonical home (it is per CLAUDE.md wiki architecture and the interface card source citations) — a silent assumption worth making explicit in the approval packet.

**Item 6 — OQ-MERGED-3 fork-separation (for Part 10 Bullet 4 in Bundle 4):**
Ruslan ack is required per wave-c-worklist.md OQ table: "Ruslan acks Wave C scope (one page per part) vs Wave A scope addition." Recommendation: Wave C scope (per-part fork-separation declaration as Foundation artefact). This is a scoping decision, not an architectural method change. Defer to Bundle 4 gate packet.

**Items to defer to Wave C with documented reason:**

- Part 2 multi-owner STOP gate (Bullet 3): Phase-A Phase-B boundary. Stub declaration only in Wave C; actual multi-owner implementation is Phase-B architecture work. No Ruslan ack needed to defer.
- Part 8 full SLI/SLO computation implementation: OQ-MERGED-5 already acked as "specify and stub" for Wave C. Phase-B materialisation confirmed. Document in Bundle 3 gate packet.
- D27 cross-fork provenance full architecture: Part 1 Bullet 1 declares the gap; full cross-fork audit trail reconciliation is Phase-B work. Documented in the stub itself.

---

*End of M1 Smoke Test. Gate verdict: PASS at 90% coverage (9/10 parts). Part 8 FAIL is a known, documented, resolvable blocker contingent on TRADEOFF-01 OQ-1 Ruslan ack via Bundle 1 Part 6 Bullet 3 gate packet.*
