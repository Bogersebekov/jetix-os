---
title: Variant B1 — "Layer-6 namespaces (thin-scaffold, high-autonomy single-brigadier)"
type: variant-draft
layer: drafts
niche: meta
task_id: T-km-architecture-research-2026-04-24
cycle_id: cyc-km-architecture-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
last_reviewed: 2026-04-24
pipeline: ingested
state: drafted
confidence: high
confidence_method: brigadier-integration-from-systems-integrator-and-mgmt-optimizer
tier: tier-1
produced_by: brigadier
sources:
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-optimizer-scaffold-deltas.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-scalability-pm-horizon.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md"}
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D1 Layer-6 operations/, D11"}
  - {path: "decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md", range: "Pillar 3, C-2"}
  - {path: "CLAUDE.md", range: "L66 ≤20 active tasks; L88 8-project roster"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md"}
related: []
binding_scope: km-architecture-variant-B1
---

# Variant B1 — "Layer-6 Namespaces (thin-scaffold, high-autonomy single-brigadier)"

## §1 Name + One-line Pitch

**B1 — Layer-6 Namespaces : extends the existing D1 Layer-6 `swarm/wiki/operations/<slug>/` namespace pattern with a 5-file minimal scaffold (`_moc.md` + `context.md` + `history.md` + `decisions.md` + `open-questions.md`) and lifecycle frontmatter state machine; one Jetix brigadier serves all 8 active projects via on-demand expert dispatch; ≤20 active tasks ratchet via `meta/health.md` `active_tasks_per_brigadier` counter; weekly Monday digest cadence — operational at G1, fragile at G3 (forces migration to B2).** [F: F4 / ClaimScope: PM-architecture-Phase-A / R: high]

## §2 Axis of Differentiation (~110w)

This variant occupies the **thin-scaffold / high-autonomy / single-brigadier** quadrant. Variant B2 occupies *rich-scaffold / federated-per-client-per-project / mini-swarm-per-active-project*. Variant B3 occupies *adaptive-scaffold / phase-gated-autonomy / morphogenetic*. Choice between them governed by: (1) **project count** — B1 supports 8-15 projects under ≤20 active tasks rule; B2 supports 50+ via per-client federation; B3 grows with project complexity; (2) **client count** — B1 single-tenant default (Phase-A); B2 multi-client (Phase-B); B3 either; (3) **scaffold cost** — B1 lowest (5 files per project); B2 highest (5+ files + per-client tree + mini-swarm); B3 starts thin, grows on triggers; (4) **operational team** — B1 fits solo-now; B2 needs ≥2 ops at G2+; B3 needs predicate-rigor discipline. **B1 is conservative-tail (70%) in mgmt barbell; B2 is aggressive-tail.** [F: F4 / ClaimScope: B-axis / R: high]

## §3 Architecture Diagram

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    Ruslan -->|/project-bootstrap <slug> <p-level>| Bootstrap[/project-bootstrap skill]
    Bootstrap --> Scaffold[5-file scaffold]
    Scaffold --> Moc[swarm/wiki/operations/<slug>/_moc.md]
    Scaffold --> Ctx[swarm/wiki/operations/<slug>/context.md]
    Scaffold --> Hist[swarm/wiki/operations/<slug>/history.md]
    Scaffold --> Decs[swarm/wiki/operations/<slug>/decisions.md]
    Scaffold --> OpQ[swarm/wiki/operations/<slug>/open-questions.md]

    Brigadier[Single Jetix brigadier] -->|on-demand| Experts[5 domain experts × 4 modes]

    subgraph "Lifecycle frontmatter state machine"
      States[active | paused | pivoted | tombstoned | killed]
      Moc -.->|state:| States
    end

    subgraph "Weekly cadence"
      Digest[/project-status weekly Monday 8:00 CET]
      Digest --> AllProj[walks operations/* for last-7d entries]
      Digest --> Health[meta/health.md project rollup]
    end

    subgraph "Attention-budget ratchet (CLAUDE.md L66)"
      Counter[meta/health.md active_tasks_per_brigadier]
      Counter -->|≥20| Alert[HITL escalation; ratchet check]
    end

    subgraph "UC-9 phase-A primitive (B1 contribution)"
      Granularity[granularity: client:<slug> frontmatter]
      ClientNS[swarm/wiki/operations/clients/<slug>/<project>/]
      Granularity -.->|Phase-A directory + frontmatter only| ClientNS
    end
```

## §4 Mechanics (~1500w)

### §4.1 B.1 Project Onboarding (UC-5 ≤30 min)

**Skill: `/project-bootstrap <slug> <p-level>`** (mgmt-optimizer Δ1; new skill per Q6 candidate → learning → active activation rubric per D11).

Operator invokes: `/project-bootstrap dach-outreach-q3 P2`. Skill:

1. Validates `<slug>` is kebab-case, unique under `swarm/wiki/operations/`, and `<p-level>` ∈ {P1, P2, P3, P4} per CLAUDE.md project-roster.
2. Creates `swarm/wiki/operations/<slug>/` directory.
3. Generates 5 scaffold files from `swarm/wiki/_templates/project-scaffold/`:
   - `_moc.md` (Map of Content): frontmatter `type: topic, layer: 6, niche: <auto|manual>, project_type: <consulting|research|product>, p_level: <P1-P4>, state: active, problem_statement: <Cagan: required field>, kill_criteria: <Hamel-binary>, related: [theme links]`. Body: ICP / offers / pricing summary; current cycle status; key open questions.
   - `context.md`: current state — ICP definition; active leads; live contracts; pricing.
   - `history.md`: append-only events log (new-on-top per CLAUDE.md convention).
   - `decisions.md`: 4-part DRR entries per FPF E-9 (Context / Decision / Alternatives-considered / Review-checkpoint per philosophy-optimizer canonical template at 80w/part floor).
   - `open-questions.md`: pending Ruslan decisions.
4. Pulls topic-wiki context: reads `wiki/themes/<auto-routed-theme>/README.md` per project_type; appends `related[]` entries.
5. Increments `meta/health.md` `project_count` + `active_tasks_per_brigadier += 1` (assuming 1 task at bootstrap).
6. Append to `swarm/wiki/log.md`: `## [YYYY-MM-DD] project-bootstrapped | <slug> | <one-line summary>`.

**Wall-clock target: ≤30 min** (UC-5 acceptance predicate). Limited by Ruslan's manual completion of `_moc.md`'s `problem_statement:` (Cagan-required) — bootstrapping fields auto-populated, but problem-statement requires human voice. Skill itself runs in <30s. [F: F4 / ClaimScope: B1-onboarding / R: high]

### §4.2 B.2 State Tracking

**Frontmatter state machine** (mgmt-optimizer Δ2). Each project's `_moc.md` carries `state:` ∈ {active | paused | pivoted | tombstoned | killed}. Transitions:

- `active → paused`: Ruslan via `/project-pause <slug> --reason="<text>"`. Sets `state: paused`; appends `history.md`: "paused <date> reason: <reason>"; mini-swarm dormant (no scheduled invocation; on-demand experts unaffected).
- `paused → active`: Ruslan via `/project-resume <slug>`. Sets `state: active`; appends history.
- `* → pivoted`: Ruslan via `/project-pivot <slug-old> --to=<slug-new>`. Sets `state: pivoted`; spawns new project with `supersedes` edge; old project archived.
- `* → tombstoned`: Ruslan via `/project-kill <slug> --tombstone-reason="<text>"`. Sets `state: tombstoned`; `/consolidate` scans for knowledge extraction; project lessons appended to `wiki/global/compound-rules/` before archive.
- `* → killed`: hard delete (Phase-B+ rare; requires HITL).

Per CLAUDE.md project-state vocabulary (Active / Planned / Paused). B1 extends with `pivoted` + `tombstoned` for completeness. [F: F4 / ClaimScope: B1-lifecycle / R: high]

### §4.3 B.3 Agent-per-project Model (single Jetix brigadier; on-demand experts)

**B1 model: single Jetix brigadier serves all projects.** No project-specific brigadiers; no mini-swarms. Brigadier dispatches 5 experts × 4 modes on demand per project task. Total agent count Phase-A: 6 (brigadier + 5 experts).

**Capacity.** Per CLAUDE.md L66 ≤20 active tasks rule + brigadier §1d auto/approval matrix. At 8 projects × 2-3 tasks each = 16-24 tasks; B1 fits within budget for the current project portfolio. At 15 projects × 2 tasks = 30 tasks → exceeds cap; **B1 forces migration trigger to B2** at G3.

**Trade-off.** Single-brigadier means context per task is brigadier-only — no per-project brigadier accumulating per-project strategies. Project context is in `operations/<slug>/`; brigadier reads it on each task intake (Q1 Tier-A direct path). [F: F3 / ClaimScope: B1-agent-model / R: high]

### §4.4 B.4 Cross-project Leverage

**Mechanism: meta-agent weekly sweep** (mgmt-optimizer Δ7 alternative; chosen over `learned-in` 13th edge per philosophy-arbitration — 13th edge is for cross-CLIENT, not cross-project).

Weekly cron (Sunday 21:00 CET) runs `/consolidate --cross-project`:
1. Walks `swarm/wiki/operations/*/history.md` for last-7d entries.
2. Extracts entity-level patterns (e.g., "DACH responds 3× to German opening" appears in `quick-money-DACH/history.md`).
3. Runs LLM (Mistral-7B) entity-overlap detection across project histories.
4. For each match (entity in ≥2 projects), proposes promotion to `wiki/claims/<pattern-slug>.md` with `derived_from` edges to source projects.
5. Surfaces in next Monday digest as "cross-project pattern candidates: N proposed".
6. Ruslan reviews; HITL ack promotes to canonical `wiki/global/compound-rules/<slug>.md`.

Edge type: `derived_from` (existing 12-enum suffices; no 13th edge). [F: F4 / ClaimScope: B1-cross-project / R: high]

### §4.5 B.5 Cadence (weekly Monday digest)

**Skill: `/project-status`** (mgmt-optimizer Δ5). Runs Monday 8:00 CET:

1. Walks `meta/health.md` for project rollup.
2. For each project, computes: tasks active, tasks completed-last-week, decisions made, open-questions count, `state:` change events.
3. Emits traffic-light table: 🟢 healthy / 🟡 attention-needed / 🔴 blocked. Drill-down links per project.
4. Cross-project pattern candidates from `/consolidate --cross-project` (§4.4).
5. Output: `swarm/wiki/operations/_weekly-<YYYY-Www>.md` (canonical) + Notion mirror (per CLAUDE.md filesystem=SoT + Notion=collaboration).

**Latency target: ≤5 min Ruslan review** (per JETIX-ARCHITECTURE-BRIEF §4.7 dashboard spec). [F: F4 / ClaimScope: B1-cadence / R: high]

### §4.6 B.6 Ruslan's Strategic Overview

`/project-overview` skill aggregates `meta/health.md` per-project rollup + traffic-light + drill-down. On-demand via Ruslan command OR scheduled Monday 8:00 CET. Per JETIX-ARCHITECTURE-BRIEF §4.7 dashboard spec extension. [F: F3 / ClaimScope: B1-overview / R: high]

### §4.7 B.7 Lifecycle (per §4.2 state machine + §8.2 archive protocol)

**Pause:** `state: paused`; mini-swarm dormant; agent task budget freed; project knowledge preserved.
**Resume:** `state: active`; tasks queueable.
**Pivot:** old `state: pivoted`; new project spawned with `supersedes` edge from new._moc.md → old._moc.md.
**Kill (tombstone):** `state: tombstoned`; `/consolidate` extracts lessons → `wiki/global/compound-rules/` before archive; `_archive/operations-tombstoned/<slug>/` move; edges marked `archived: true` per D5.

### §4.8 B.8 Linkage to Layer A

**Read from Layer-A:** project-wiki reads `wiki/themes/<auto-theme>/README.md` at bootstrap (§4.1 step 4); reads `wiki/foundations/<expert-domain>/` on-demand during expert dispatch.

**Write to Layer-A:** when project pattern validates (≥3 repetitions in `history.md`), project-brigadier proposes promotion to `wiki/claims/<pattern-slug>.md` (HITL-ack required per §5.5.5 provenance gate). Pattern carries `derived_from` edges back to project's `_moc.md`.

**Edge types crossing layers.** Existing 12-enum: `part_of` (project _moc → theme); `derived_from` (claim → project history); `supports` (project decision → theme foundation); `extends` (project methodology → theme). No 13th edge needed for B1. [F: F4 / ClaimScope: B1-A-linkage / R: high]

## §5 Use-case Walkthrough (UC-1..UC-10)

### UC-1 — Video Ingest

Layer-A handles. B1 contributes: project-wiki may include `inbox/videos/` → `/ingest` → concept pages tagged with `niche:` per project's domain. Cross-references to project's `_moc.md` via `related[]`. [F: F3 / ClaimScope: UC-1-B1 / R: medium]

### UC-2 — Weekly Digest

`/project-status` runs at 8:00 CET (§4.5). Aggregates Layer-A wiki additions (per niche) WITH project-level state changes. Latency ≤5 min for Ruslan review. [F: F4 / ClaimScope: UC-2-B1 / R: high]

### UC-3 — Solve-with-Wiki

When solving a project-scoped query (e.g., "How to apply systems-thinking to DACH outreach for `quick-money-DACH`?"), `/ask --project=quick-money-DACH` scopes Q1 retrieval to: `operations/quick-money-DACH/*` + `themes/systems/` + `themes/sales/` + `niches/sales/` + Tier-D fallback. Synthesis writes back to `comparisons/2026-XX-apply-X-to-quick-money-dach.md` AND `operations/quick-money-DACH/decisions.md` (4-part DRR if novel). [F: F4 / ClaimScope: UC-3-B1 / R: high]

### UC-4 — Skill Accumulation

Brigadier learns project-decomposition patterns. Appends to `agents/brigadier/strategies.md` (general) AND `swarm/wiki/brigadier/how-to-decompose-project-tasks/<slug>.md` (project-mgmt-specific). Promotion per W-5 Level-2. [F: F4 / ClaimScope: UC-4-B1 / R: high]

### UC-5 — Project Onboarding

Per §4.1: `/project-bootstrap <slug> <p-level>` ≤30 min wall-clock. 5 scaffold files; topic-wiki linked; `meta/health.md` updated. [F: F4 / ClaimScope: UC-5-B1 / R: high]

### UC-6 — Cross-project Insight Transfer

Per §4.4 meta-agent weekly sweep. Pattern in `quick-money-DACH/history.md` ("DACH 3× to German opening") detected by `/consolidate --cross-project` → proposes `wiki/claims/dach-german-opening.md` with `derived_from` edges to `quick-money-DACH` + (after a future cycle) `research-thesis-validation`. Ruslan acks promotion to `wiki/global/compound-rules/dach-german-opening.md`. Future projects see the rule via Q1 Tier-A niche=meta filter at bootstrap. [F: F4 / ClaimScope: UC-6-B1 / R: high]

### UC-7 — Contradiction Detection (per-project + cross-project HITL-ack)

`/lint` per-project scope (per philosophy-integrator §4 protocol): contradictions surface in project's `meta/health.md` row + project's `open-questions.md`. Cross-project contradiction (e.g., `quick-money-DACH/decisions.md` says "high volume wins DACH"; `research/decisions.md` says "hyper-targeting wins DACH") surfaces in next weekly digest as a HITL prompt; Ruslan acks: edit / supersede / preserve-both with bounded ClaimScope. [F: F4 / ClaimScope: UC-7-B1 / R: high]

### UC-8 — Scale Test (preview; full §10)

B1 scales to 8-15 projects (G1-G2). At G3 (30 projects), Agency trigger fires hard (≤20 active-tasks rule + Ruslan attention budget). **B1 forces migration to B2 at G3** OR portfolio-brigadier aggregation per mgmt-scalability dissent (preserved as D-4). [F: F4 / ClaimScope: UC-8-B1 / R: high]

### UC-9 — Client Isolation (B1 contribution to STACK; ≥200w)

B1 in Phase-A is **single-tenant** by default (no per-client). When first paying client arrives at G2 (Phase-B onset), B1 contributes the **directory namespace + frontmatter granularity layer** to the defense-in-depth UC-9 STACK:

**Directory namespace.** Per-client projects live under `swarm/wiki/operations/clients/<client-slug>/<project-slug>/` (mgmt-optimizer Δ4). Existing `/project-bootstrap` skill extended: `--client=<client-slug>` flag routes scaffold to client-namespaced path.

**Frontmatter granularity field.** Every per-client artefact carries `granularity: client:<client-slug>` per FPF E-16 extension (systems-optimizer Δ-extras). `/lint` enforces L-CROSS-CLIENT-GLOBAL signal: any artefact under `wiki/global/` with `granularity: client:*` triggers ERROR (cross-client global-write FORBIDDEN).

**WIKI_ROOT_CLIENT_ID env-var resolution** (engineering Δ1 inherited): per-client brigadier instance resolves `$WIKI_ROOT` to `clients/<client-slug>/swarm/wiki/`; existing `/project-bootstrap` routes scaffolds within resolved root.

**Phase-A operational reality.** B1 supports first 1-3 clients via per-client directory namespace + frontmatter discipline. **NOT by-construction at OS level until Phase-B** (when separate-repo per client + 13th `holon-ref` edge ship per A2 substrate). Engineering-critic dissent D-1 preserved: Phase-A is policy+config layer; Phase-B is by-construction.

**Pen-test scenario.** Hostile actor in Client-A's brigadier attempts to read Client-B's `_moc.md`. Phase-A: directory-namespace boundary + frontmatter-filtered `/ask` resolves only client-A pages; even if attacker bypasses with absolute path, brigadier's process scope (env-var + skill `$WIKI_ROOT` resolution) prevents skill from accessing client-B. Phase-B: OS UNIX permissions deny.

**Acceptance predicate.** Phase-A: zero cross-client read in `/ask` audit log over rolling 100 multi-client sessions. Phase-B: pen-test verifies OS-level denial. [F: F4 / ClaimScope: UC-9-B1-Phase-A-policy + Phase-B-construction / R: medium / refuted_if: cross-client read detected]

### UC-10 — Offline-First Inference (B1 inherits Layer-A; ≥200w)

B1 inherits Layer-A's offline-first inference path entirely. The project-wiki layer is filesystem-native (per D17 SoT lock); `/ask --project=<slug> --offline` invokes A1's `OFFLINE_MODE=1` structured-excerpt path OR A2/A3's local-LLM synthesis (per Layer-A variant chosen).

**B1-specific contribution:** the project-scaffold ensures every project has the local-LLM stack reference in its `context.md` (via `inference_stack: ollama-mistral-7b-q4` field if `project_type: consulting`). `/project-bootstrap --type=consulting` skill auto-populates this field. Ruslan can per-project override (e.g., research projects may not need offline-first; `inference_stack: cloud-llm`).

**Tier split per project query type.** B1 carries no per-project tier-split logic — inherits Layer-A's T-Offline / T-Hybrid / T-Cloud-only routing. Per-project `context.md` may specify default tier (e.g., `default_inference_tier: T-Offline` for consulting; `T-Hybrid` for research).

**Network-disconnect test.** Per Layer-A; B1 ensures project context is filesystem-readable so brigadier dispatches don't fail on disconnect.

**Acceptance predicate.** Per-project `/ask` against client-private project data with OFFLINE_MODE=1 returns synthesis with citations to project-wiki pages; tcpdump confirms zero outbound. [F: F4 / ClaimScope: UC-10-B1-inheritance / R: high]

## §6 UC-9 + UC-10 Co-located Proof Section (≥400w)

B1 is the Phase-A entry-point for project-mgmt; UC-9 + UC-10 proofs at B1 layer are necessarily LIGHTER than at A2 substrate, because B1 operates within whichever Layer-A substrate is active. The B1-specific proofs are:

**Isolation model: directory-namespace + frontmatter granularity (Phase-A); per-client brigadier instance (Phase-B onset; carried via A2 STACK).**

Phase-A B1 contributes two namespacing primitives:
- **`swarm/wiki/operations/clients/<client-slug>/<project-slug>/` directory naming.** Per-client projects physically live under client-scoped path. Existing `/project-bootstrap --client=<slug>` extension creates scaffolds at correct path. Existing `/project-status` aggregates per-client by walking `operations/clients/<client-slug>/*`.
- **`granularity: client:<slug>` frontmatter field.** Every per-client artefact carries this field. `/lint` L-CROSS-CLIENT-GLOBAL ERROR signal forbids writing client-tagged artefacts to `wiki/global/`. Forces explicit anonymization + HITL ack before cross-client promotion.

Phase-B onset (G2 first paying client) inherits A2's defense-in-depth STACK: OS-level UNIX permissions (separate UNIX user per client); per-client git repository (separate signing keys); 13th `holon-ref` edge with `/lint` L-CROSS-HOLON-REF signal; per-client agent instances (separate `WIKI_ROOT_CLIENT_ID` brigadier processes). B1's per-client `/project-bootstrap` extension fits cleanly into A2 substrate at this point.

**Local-LLM family supported (inherited).** Per Layer-A: ollama + Mistral 7B Q4_K_M (default) or Llama 3.1-8B Q4_K_M (alt). B1 ensures every project's `context.md` declares the inference-stack reference.

**Hosting model alignment.** B1 supports all 3 paths (A/B/C) via Layer-A inheritance. B1 contributes per-project `inference_stack:` + `default_inference_tier:` fields that adapt to hosting model:
- Path A (Jetix-hosted VPS): per-project `default_inference_tier: T-Offline`; uses Jetix-EU GPU pool.
- Path B (Client-hosted): per-project `default_inference_tier: T-Offline`; uses client GPU.
- Path C (Hybrid): per-project `default_inference_tier: T-Hybrid` allowed (cloud opt-in with redacted PII per UC-10 protocol).

**Tier split per project type.**
- Consulting projects: T-Offline default; T-Hybrid HITL opt-in for novel multi-doc synthesis.
- Research projects: T-Hybrid default (Ruslan-internal; less PII risk).
- Product projects: T-Offline default (client-private; no cloud).

**EU compliance alignment.** B1 inherits A2 compliance posture. B1-specific contribution: per-project `compliance_classification: <gdpr-art-9-special-category | gdpr-art-22 | en-AI-Act-limited-risk | etc.>` frontmatter field on `_moc.md`. `/lint` enforces compliance-classified projects use only T-Offline or T-Hybrid (never T-Cloud-only) for client-private queries.

**Pen-test + network-disconnect tests.** Per UC-9 + UC-10 §5. B1-specific pen-test: hostile prompt-injection on `/project-bootstrap --client=client-a` attempting to inject `--client=client-b` flag → skill validates flag against `WIKI_ROOT_CLIENT_ID` env-var; mismatch rejects with permission-denied. [F: F4 / ClaimScope: UC-9+UC-10-B1-co-located / R: high]

## §7 Pros / Cons / Tradeoffs

**Pros.** (a) **Lowest setup overhead** — 5-file scaffold; existing wiki v3 substrate supports today; `/project-bootstrap` skill is the only new skill required. (b) **Fits Phase-A operating reality** — 8 active projects + ≤20 active tasks rule + solo-founder team; B1 is the conservative-tail correct choice. (c) **Filesystem-native** — debuggability high; rollback trivial (git revert). (d) **Smooth migration to B2** — directory-namespace + frontmatter granularity primitives are forward-compatible; B2 adds OS-level + per-client-brigadier on top.

**Cons.** (a) **Fragile at G3** — Agency trigger (≤20 active tasks) fires hard at 30 projects; brigadier attention budget blown; forces migration to B2. (b) **Single-tenant default in Phase-A** — UC-9 isolation is policy+config layer until Phase-B; engineering-critic dissent D-1 (preserved). (c) **No per-project memory accumulation** — single brigadier means no project-specific strategies.md (only general); cross-cycle project memory lives in `operations/<slug>/decisions.md` only.

**Tradeoffs.** (1) Speed-to-ship vs by-construction-isolation: B1 ships in 1-2 weeks; A2 substrate Phase-B by-construction takes 4-6 weeks. (2) Solo-founder fit vs team-fit: B1 fits solo+team-ready; B2 needs ≥2 ops at G2+. (3) Operational simplicity vs per-client autonomy: B1 simple (one brigadier); B2 per-client autonomy. (4) Phase-A vs Phase-B trajectory: B1 is the Phase-A bridge; B2 is the steady-state production model.

## §8 Effort Estimate

- **Bootstrap (Day 1):** 4-8 hours. `/project-bootstrap` skill authoring + 5-file scaffold templates + `meta/health.md` extension.
- **UC-1..UC-4 live:** 1-2 weeks. Limited by: scaffold template iteration on first 2 project bootstraps + Layer-A integration validation.
- **UC-5..UC-8 stable:** 2-3 weeks. Limited by: cross-project meta-agent sweep + traffic-light digest skill + lifecycle state-machine plumbing.
- **UC-9 + UC-10 live (Phase-A):** 2 weeks. Limited by: `--client=<slug>` flag extension + frontmatter granularity validation + L-CROSS-CLIENT-GLOBAL `/lint` signal.

## §9 Migration Path from Current State

Current `swarm/wiki/operations/` exists as empty Layer-6 directory. B1 changes:

1. **Create** `swarm/wiki/_templates/project-scaffold/` with 5 template files.
2. **Author** `.claude/skills/project-bootstrap.md` skill manifest.
3. **Extend** `meta/health.md` 8-section schema with `project_count` + `active_tasks_per_brigadier` fields.
4. **Extend** D2 frontmatter schema with project-specific fields (`project_type`, `p_level`, `state`, `problem_statement`, `kill_criteria`, `compliance_classification`, `inference_stack`, `default_inference_tier`).
5. **Author** `.claude/skills/project-status.md` skill manifest (weekly digest).
6. **Extend** `.claude/skills/consolidate.md` with `--cross-project` mode flag.
7. **Author** lifecycle skills (`/project-pause`, `/project-resume`, `/project-pivot`, `/project-kill`).
8. (Phase-B) **Extend** `/project-bootstrap` with `--client=<slug>` flag.

**Staging order (parallelizable).** Steps 1-4 in parallel. Steps 5-6 after step 1 (templates). Step 7 in parallel. Step 8 Phase-B.

**Rollback.** Each project's scaffold is filesystem-native; revert by `git rm -rf swarm/wiki/operations/<slug>/`. Skill manifests revert by git. No active code path break.

## §10 Horizon Projection (≥600w; 5 gates)

| Gate | Projects | Active tasks | Clients | Physical failure | Upgrade path | MHT event | BOSC-A-T-X | Janus risk | Per-project ops |
|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | 8 (CLAUDE.md roster) | 16-24 | 0-1 | none — within ≤20 ratchet (8 P1-P4 × 2-3 tasks ≈ 24, exceeds slightly; mitigated by P3-P4 dormancy) | none | — | Time | low (S-A: solo-founder context monopoly mitigated by mailbox logging) | manual ; brigadier reads `operations/<slug>/` on each task |
| **G2 €200K** | 15 | ~30 | 10 | active-tasks budget exceeded; Monday digest takes >10min Ruslan review | portfolio-brigadier aggregation (mgmt-scalability dissent D-4 alternative); P3-P4 projects fully dormant; Phase-B B2 substrate prep | Phase Promotion (`/project-status` from manual to scheduled cron); first per-client `--client=<slug>` flag emergence | Operation + Composition + Agency | medium INT excess (Ruslan attention drowns); medium S-A excess (single-brigadier becomes context-monopoly across many projects) | client-onboarding requires Phase-B B2 substrate; B1 still adequate for Jetix-internal projects |
| **G3 €1M** | 30 | ~60 | 50 | **HARD AGENCY TRIGGER** — CLAUDE.md L66 ≤20 rule blown; brigadier attention budget impossible; Ruslan drowns in cross-project decisions | Sub-roy split (consulting / infra / research per Lock 21); per-portfolio brigadier; **B1 INSUFFICIENT — forced migration to B2 federated mini-swarm** | Fission (single Jetix brigadier into per-portfolio sub-brigadiers); Role-Lift (portfolio-brigadier rises to Layer-3 agent role) | Composition + Agency + Operation | high INT excess (Ruslan as bottleneck) — mitigated by sub-roy + portfolio-brigadier pattern; dissent preserved on whether portfolio-aggregation suffices vs full B2 | per-portfolio P1 tasks cap at ~10 per brigadier; B2 transition starts at G2 prep |
| **G4 $100M** | 100 | ~200 | 500 | sub-roy + portfolio-brigadier insufficient; per-client mini-swarms required | full B2 federation (one project-brigadier per active P1 client-project) + Mittelstand AI Alliance per-portfolio governance | Role-Lift (portfolio-brigadier becomes Alliance-member-coordinator); Context Reframe (each Alliance-member is a peer-roy) | Boundary + Agency + Composition + Operation | pervasive (mitigated by Alliance methodology parliament + per-roy autonomy) | per-Alliance-member self-coordinates; Jetix-central focuses on methodology + standards |
| **G5 $1T** | 500+ | ~1000+ | 5000+ | distributed coordination; per-roy methodology drift on PM scaffold conventions | federated PM scaffold conventions (per Alliance methodology version); per-region governance committees; Token economy Option B (D23) tie-in for Alliance-member voting | Continuous Fusion (Alliance-shared scaffold conventions); Re-Phase-Promotion at every Alliance methodology release | eXternal + Composition + Agency + Time | pervasive (mitigated by Alliance parliament + outcome-level telemetry per philosophy-scalability §6) | per-Alliance-member sovereign PM; Jetix-central provides scaffold templates + methodology versions |

**Antifragility verdict.** B1 standalone is **operational at G1, robust at G2, fragile at G3 (forces B2).** The migration B1→B2 between G2 and G3 is the critical PM-architecture transition; pre-investment in B2 substrate at G2 is Kelly-positive per investor-optimizer §3 barbell. [F: F4 / ClaimScope: B1-horizon / R: high]

## §11 Anti-Fragility Assessment (≥400w)

**Verdict: ROBUST G1-G2; FRAGILE at G3; requires migration to B2 substrate (similar pattern to A1→A2).**

**Mechanism for robustness G1-G2.** B1's thin-scaffold + single-brigadier model survives 8-15 projects because: (a) Layer-6 namespace pattern is filesystem-native (CLAUDE.md SoT lock; sub-second access); (b) brigadier's task-decomposition rubric (`.claude/agents/brigadier.md §3`) handles per-project intake without per-project specialization; (c) `/project-status` weekly digest amortizes cross-project visibility cost into one Monday review session (≤5min Ruslan time per JETIX-ARCHITECTURE-BRIEF §4.7).

**Mechanism for fragility G3.** Above 30 projects, Agency-trigger fires hard: ≤20 active tasks rule from CLAUDE.md L66 is HARDCODED (Ruslan's own constraint, not Jetix-default). 30 projects × 2 active tasks each = 60 tasks > 20. Either: (a) ratchet active tasks DOWN per project (means projects stall — fragility); (b) split single brigadier into sub-roy brigadiers (B2 substrate); (c) sub-roy autonomy with periodic sync (preserves attention budget). Options (b)-(c) are antifragile if pre-investment at G2 — under-stress, system EXECUTES known migration to B2 + portfolio-brigadier pattern. Option (a) is fragile.

**Pressure tests.**

(1) **3 projects pivot in same week (`bets` activates with 2 sub-bets; `quick-money` splits DACH/NL).** B1 absorbs at G1-G2 (5 → 8 projects); each pivot triggers `state: pivoted` + new project bootstrap; meta-agent sweep flags pivots for Ruslan in next Monday digest. **Robust because:** lifecycle state-machine is built-in; pivots don't break invariants.

(2) **Domain expert replaced (engineering-expert v2 prompt).** B1 unaffected — agent prompts orthogonal to project-mgmt scaffold. Single-brigadier reads new prompt at next intake. **Robust because:** B1 is brigadier-driven not expert-driven.

(3) **Project forked into parallel directions (e.g., `quick-money` → `quick-money-dach` + `quick-money-nl`).** B1 spawns two project-wikis under separate slugs with `derived_from` edges to original. Both run in parallel under single brigadier. Active-tasks count doubles for the project; meta-agent weekly sweep detects pattern overlap. **Robust at G1-G2; fragile at G3** because forks compound the active-task count toward the ≤20 ratchet.

(4) **First paying client onboards at G2 (Phase-B onset).** B1 extends `/project-bootstrap --client=client-a` flag; client-A's projects land under `operations/clients/client-a/`. Per-client granularity field on every artefact. `/lint` L-CROSS-CLIENT-GLOBAL signal active. **Robust because:** B1 forward-compatible to B2 substrate via directory-namespace primitive; migration is incremental, not a big-bang. [F: F4 / ClaimScope: B1-anti-fragility / R: high]

## §12 Open Questions for Ruslan

1. **B1 → B2 migration trigger:** auto at G3 (30 projects threshold in `meta/health.md`)? OR manual at first paying client onboarding (Phase-B onset)? Preserved dissent D-4 (mgmt-scalability vs mgmt-integrator on portfolio-brigadier-aggregation-vs-full-B2).
2. **CLAUDE.md L66 ≤20 active-tasks rule:** firmly hardcoded OR negotiable upward (e.g., 30 with portfolio-brigadier delegation)? B1 horizon depends on this.
3. **`/project-pause` vs `/project-kill` distinction:** preserve both as distinct (paused = recoverable; killed = tombstoned with knowledge extracted)? Or simplify to single state?
4. **Project-type templates** (`consulting | research | product`): authorized as Phase-A activations? Each adds project-type-specific scaffold sections (e.g., consulting adds `offline-inference-spec.md`).
5. **Cross-project pattern promotion to `wiki/global/compound-rules/`:** HITL ack required (default) OR auto-promote after ≥3 repetitions across ≥2 projects (lower friction)?

— brigadier (Phase-5 variant draft), 2026-04-24
