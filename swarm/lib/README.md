---
title: "swarm/lib/ — Shared Infrastructure Layer (Foundation generic)"
date: 2026-04-28
type: infrastructure-readme
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 2
status: canonical-pre-ruslan-ack
F: F4
ClaimScope: "Holds for swarm/lib/ shared-infrastructure layer in Foundation Phase A. Canonical inventory of accessor pipeline scripts, routing artefacts, and shared protocols. Phase B forks import this README pattern + replace the named lead/advisory owner roles per executor-binding.yaml."
R:
  refuted_if: "An accessor skill is added to swarm/lib/ without an entry here; OR a skill listed here is renamed/removed from swarm/lib/ without a corresponding update; OR Part 3 §I or Part 4 §I duplicates the content here instead of REFERENCING it"
  accepted_if: "Every script in swarm/lib/ is documented in §3 inventory; routing-table.yaml lints clean against the inventory (no role permits an undocumented skill); modification governance per §4 produces audit log entries"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md (the joint design decision this README operationalizes)
  - swarm/lib/shared-protocols.md (current shared infra layer being extended)
  - swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md (cross-reference; named lead owner)
  - swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md (cross-reference; advisory owner; routing-table.yaml location)
  - swarm/wiki/foundations/part-6b-human-gate/architecture.md (§I.4 awaiting-approval-packet F8 — modification governance)
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md (§H commit interface; commit-format-tokens.json)
related_artefacts:
  - swarm/lib/routing-table.yaml (Part 4 P4.1 deliverable; per-role accessor_skills_invocable:)
  - swarm/lib/shared-protocols.md (§3 structured-output schema; §4 escalations)
  - swarm/lib/hooks/ (pre-session-check.sh; pre-commit lint hooks)
---

# swarm/lib/ — Shared Infrastructure Layer

> **Foundation generic. Canonical infra-layer documentation.** Companion to
> `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` (the
> design decision this README operationalizes). Per Bundle 2 C1 Joint Design (Variant A
> Ruslan-acked 2026-04-27): `swarm/lib/` houses shared accessor-pipeline scripts and routing
> artefacts; **Part 3 (Knowledge Base & Methodology Library) is the named LEAD owner**; Part 4
> (Role Taxonomy & Coordination Protocol) holds **ADVISORY** ownership; modifications gate
> through AWAITING-APPROVAL `gate_class: stage_gate` per Part 6b §I.4 F8 schema.

## §1 Purpose

`swarm/lib/` is the U.System layer that bridges Foundation parts. It exists because:

- The accessor pipeline scripts (`/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint`) are
  too cross-cutting to live inside any single Foundation Part (they touch Part 3 content + Part 4
  routing + Part 6a F-G-R + Part 6b gate semantics + Part 1 commit substrate).
- A "shared infra" location with explicit ownership prevents architectural orphaning (the C1
  BLOCKING contradiction from dependency-graph §3.1).
- Phase B forks need a stable home to import scripts from while replacing executor bindings.

## §2 Boundary — what lives here vs what does not

**LIVES IN swarm/lib/:**

- Accessor pipeline scripts (`/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint`) and
  future skills at the same level (e.g. `/search-kb`, `/comparison`).
- Routing artefacts: `routing-table.yaml` (per-role permission matrix; Part 4 P4.1 deliverable).
- Shared protocol contracts: `shared-protocols.md` (structured-output schema; escalations
  taxonomy; provenance gate steps).
- Hook layer: `hooks/pre-session-check.sh`, `hooks/pre-commit-lint.sh`,
  `hooks/mode-prefix.sh` (pre-dispatch validation), `hooks/role-matrix.sh`,
  `hooks/verify-packet.sh`.
- Future shared utility scripts that operate cross-Part (e.g. citation scanner from
  Bundle 1 P6a.2 / OQ-B1-2 deferred to Phase B engineering backlog).

**DOES NOT LIVE HERE:**

- Foundation architecture documents (those live under `swarm/wiki/foundations/<part-slug>/`).
- Part-specific content (wiki entities live in `wiki/`; role manifests live per IP-1 in
  RUSLAN-LAYER `executor-binding.yaml` not in `swarm/lib/`).
- Voice-pipeline tools (`tools/transcribe.py`, `tools/extract.py`, etc.) — those are
  RUSLAN-LAYER per Part 2 §X; they invoke into `swarm/lib/` but are not housed there.
- Provider API-key environment-variable references (per global rule; `swarm/lib/` scripts MUST
  NOT read or write any provider-API-key env var; literal env-var names are deliberately omitted
  from this file so they do not leak into traced output).

## §3 Skill inventory (canonical)

| Skill | Path | Owner-of-record | Status (cycle 11 baseline) | Brief |
|-------|------|-----------------|----------------------------|-------|
| `/ingest` | `.claude/commands/ingest.md` (skill spec) → invokes `tools/run_pipeline.sh` for voice; reads URL/PDF for non-voice | Part 3 lead, Part 4 advisory | Operational; Bundle 2 P2.2 EXTENSION pending Ruslan ack: enforce `para_tier:` mandatory frontmatter | Ingests external signal (voice/URL/PDF/clipboard) into draft candidate at `inbox/<slug>-DRAFT.md` or `raw/transcripts/<slug>.md` with frontmatter; D28 `--anchor=` mandatory; STOP gate ack required before promotion to `wiki/` |
| `/ask` | `.claude/commands/ask.md` (skill spec) | Part 3 lead, Part 4 advisory | Operational; Bundle 2 P3.4 EXTENSION pending: `--save` is DEFAULT (writes to `wiki/comparisons/`), `--no-save` for ephemeral; OFFLINE_MODE=1 supported per KM MVP | Receives `<question>`; reads `wiki/index.md` + relevant entity files; produces synthesis with inline `[src:...]` citations |
| `/consolidate` | `.claude/commands/consolidate.md` | Part 3 lead, Part 4 advisory | Operational; `--weekly` flag from KM MVP cycle | Detects + merges duplicate entities (e.g. two `wiki/concepts/<slug>.md` representing the same idea); `--weekly` runs auto-merge on items added in last 7 days |
| `/build-graph` | `.claude/commands/build-graph.md` | Part 3 lead, Part 4 advisory | Operational + community detection (KM MVP cycle Louvain-equivalent) | Rebuilds `wiki/graph/edges.jsonl` typed-edge graph from per-entity frontmatter; writes `wiki/graph/communities.jsonl` |
| `/lint` | `.claude/commands/lint.md` | Part 3 lead, Part 4 advisory | Operational; 11 KB health checks + Bundle 1 P1.2 `--check-commit-format` (#12) + Bundle 1 P6a.2 `--check-citations` (specified, Phase B implementation per OQ-B1-2) | Validates `wiki/` frontmatter, edges integrity, orphan entities, stale claims, contradicts/supports edge density, anchor compliance. Bundle 2 extensions: P2.2 PARA-tier check, P3.3 CRM edge validation, P3.4 comparisons emptiness signal |
| **`shared-protocols.md`** | `swarm/lib/shared-protocols.md` | Part 4 lead | Operational | §3 structured-output schema (cell return packet); §4 escalations taxonomy (peer-input-needed, out-of-domain, etc.); §2 provenance gate (six checks) |
| **`routing-table.yaml`** | `swarm/lib/routing-table.yaml` | Part 4 lead | Wave C Bundle 2 P4.1 NEW (extracted from `brigadier.md` + 5 expert system prompts) | Per-role declarative routing rules: J-level authority, allowed modes, write-scope-glob, escalation taxonomy per trigger, hub-and-spoke dispatch chain, `accessor_skills_invocable:` |
| **`hooks/`** | `swarm/lib/hooks/*.sh` | Part 4 lead | Operational (pre-session-check.sh, mode-prefix.sh, role-matrix.sh, verify-packet.sh) | Pre-dispatch validation; pre-commit lint enforcement |

**Naming convention:** every accessor skill is invocable as `/<name>` from the slash-command
interface; the skill spec lives at `.claude/commands/<name>.md`; the implementation (when needed
beyond a thin spec) lives at `swarm/lib/<name>.{sh,py}`. Phase A: most skills are spec-driven
(executed by Claude reading the skill spec); Phase B: implementation may move into `.sh`/`.py` for
deterministic execution.

## §4 Modification governance

Any change to a script under `swarm/lib/` (or addition of a new script) requires:

1. **Proposal commit on a feature branch** (do not commit directly to
   `claude/jolly-margulis-915d34`).
2. **AWAITING-APPROVAL packet** with `gate_class: stage_gate` per Part 6b §I.4 F8 schema. Required
   fields per the F8 contract: `packet_id`, `timestamp`, `actor`, `summary`, `outcomes`,
   `provenance`, `ack_request` (three options per Askell HHH corrigibility), `reversibility_class`,
   `blast_radius_tier` (typically tier 1 or 2 for `swarm/lib/` modifications), `review_checkpoint`,
   `f_g_r_delta`.
3. **Lead owner ack** (Part 3 lead — Ruslan in Phase A; Phase B successor named in
   `executor-binding.yaml`). Ack mechanism per Part 6b §6.3 four-response handling.
4. **Advisory pass** (Part 4 advisory) IF the change touches routing semantics (which roles can
   invoke the skill, which modes activate, escalation taxonomy). If routing-table.yaml needs a
   corresponding update, the same packet bundles both files.
5. **Promotion** = ack triggers merge to `claude/jolly-margulis-915d34` (or Phase B equivalent).
6. **Audit trail** = `swarm/approvals/log.jsonl` (Part 6a §C) entry with `packet_id` + outcome.
7. **Commit format** = `[swarm-lib] <verb> <what> (<why>)` per Part 1 commit-format-tokens.json
   schema (Bundle 1 §I.2). The token `[swarm-lib]` MUST be added to the accepted area enum at
   first use; pre-commit hook K7 (Part 1 §K) handles the area-token-expansion-without-schema-update
   failure mode.

**Reversibility class.** Modifications to `swarm/lib/` are typically `hard_to_reverse` (per
Part 6b §I.4 reversibility_class enum) because cell dispatches in flight may rely on the prior
behavior; revert requires careful rollout. `git revert` is the canonical revert mechanism (no
`--amend`, no force-push) per Part 1 §E Laws.

**Blast-radius tier.** Most `swarm/lib/` modifications are **Tier 1 strategic** (per Part 6b
§I.4 blast-radius-table — affects coordination semantics + propagates to all cells via routing).
Some are **Tier 2 tactical** (e.g., adding a new lint signal that doesn't change existing
behavior). NEVER Tier 0 (which is auto-halt) or Tier 3 (which is auto-log) — Tier 0/3 do not
match the strategic-but-not-emergency profile of `swarm/lib/` work.

## §5 Invocation contract — who calls what

Authoritative source: `swarm/lib/routing-table.yaml` (per-role `accessor_skills_invocable:` field).

Default permit sets (until routing-table.yaml lints clean):

| Caller class | Default permits | Rationale |
|--------------|-----------------|-----------|
| Brigadier (Part 4 orchestrator) | All five accessor skills + routing-table reads + hook invocations | Brigadier is the dispatcher; needs full access to coordinate cells |
| Owner (Ruslan) | All five accessor skills directly via slash-command | Founder agency per FUNDAMENTAL §6.2 |
| Cells (5 ROY experts in critic/optimizer/integrator/scalability) | `/ask` (read-only synthesis); `/lint` only in critic-mode pre-pass; otherwise none | Cells produce drafts; brigadier handles canonical writes; cells consume KB via `/ask` only |
| Legacy 13 agents (manager, sales-lead, sales-researcher, sales-outreach, inbox-processor, knowledge-synth, personal-assistant, system-admin, life-coach, meta-agent, crazy-agent, strategist) | Per `executor-binding.yaml` RUSLAN-LAYER | RUSLAN-LAYER bindings; not Foundation-generic |
| Phase B partner roles | Per partner's fork of routing-table.yaml | F.9 Bridge mechanism |

## §6 Cross-references (DRY enforcement)

- **Part 3 §I REFERENCES** this document and `C1-joint-design.md`. Part 3 §I MUST NOT duplicate
  the content here. The brigadier critic gate verifies (M5 Joint Design coherence check).
- **Part 4 §I REFERENCES** this document and `C1-joint-design.md`. Same DRY enforcement.
- **`routing-table.yaml`** lints clean against §3 skill inventory: every skill listed in any
  role's `accessor_skills_invocable:` array MUST exist in §3 above; every skill in §3 MUST be
  listed in at least one role's `accessor_skills_invocable:` array (orphan skills surface as
  `/lint --check-routing-table-coverage` defects).
- **Part 1 §H commit interface** referenced for `[swarm-lib]` area token.
- **Part 6a §C approval log** referenced for modification audit trail.
- **Part 6b §I.4 awaiting-approval-packet schema F8** referenced for proposal packet format.

## §7 Phase B fork pattern

A Phase B partner forking the Foundation:

1. **Imports** this `swarm/lib/` tree as-is (Foundation generic).
2. **Imports** `routing-table.yaml` as a structural template.
3. **Replaces** the named lead/advisory owner roles per their fork's `executor-binding.yaml`.
4. **Replaces** specific role entries in `routing-table.yaml` with their fork's roles.
5. **Optionally extends** `swarm/lib/<skill>.md` specs with fork-specific behavior, gated by
   their fork's AWAITING-APPROVAL.

The pattern persists: shared-infra location + named lead-with-advisory ownership + AWAITING-APPROVAL
modification gate. The names rotate per fork. This is the F.9 Bridge for accessor pipeline ownership
across forks.

## §8 Open Questions

Bundle 2 surfaced (proposed for Bundle 4 / Phase B):

- **OQ-B2-A — `swarm/lib/` security-domain split for external integrations.** If a future
  accessor skill bridges to external API (Notion sync, Linear push, GitHub PR), should it live in
  `swarm/lib/external/` with stricter gate semantics? Current answer: defer to Bundle 4 Part 10
  (External Touchpoints & Network Interface) — Part 10 territory by definition.
- **OQ-B2-B — `swarm/lib/` test harness.** Should accessor scripts have unit tests under
  `swarm/lib/_tests/`? Current answer: defer to Phase B engineering backlog (alongside OQ-B1-4
  jsonschema validator).

---

*End of swarm/lib/ README. See `C1-joint-design.md` for design rationale.*
