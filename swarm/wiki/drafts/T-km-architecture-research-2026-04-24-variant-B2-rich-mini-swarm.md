---
title: Variant B2 — "Rich-scaffold per-client per-project mini-swarm (Cagan-problem-over-solution)"
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
confidence_method: brigadier-integration-from-mgmt-integrator-and-systems-integrator-B2
tier: tier-1
produced_by: brigadier
sources:
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-scalability-pm-horizon.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-optimizer-scaffold-deltas.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-integrator-moat-synthesis.md"}
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D1, D11"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md"}
  - {path: "raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md"}
  - {path: "decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md"}
related: []
binding_scope: km-architecture-variant-B2
---

# Variant B2 — "Rich-scaffold per-client per-project mini-swarm"

## §1 Name + One-line Pitch

**B2 — Rich Mini-Swarm : each Jetix project (internal or per-client) carries a 5-9-file rich scaffold (5 baseline + 4 conditional consulting/research/product additions) + lifecycle frontmatter state machine + per-active-P1/P2-project mini-swarm-of-3 (project-brigadier + 2 default experts) + per-client directory namespace + per-client agent instances; Cagan problem-over-solution discipline mandatory in `_moc.md`; PMBOK Work-lifecycle alphas tracked; antifragile through G4 by construction.** [F: F4 / ClaimScope: PM-architecture-Phase-B-production / R: high]

## §2 Axis of Differentiation (~110w)

This variant occupies the **rich-scaffold / federated-per-client-per-project / mini-swarm-per-active-project** quadrant. Variant B1 occupies *thin-scaffold / single-brigadier / Phase-A-default*. Variant B3 occupies *adaptive-scaffold / phase-gated-autonomy / morphogenetic*. Choice between them governed by: (1) **client+project count** — B2 supports 50+ projects across 50+ clients via per-client mini-swarm federation; (2) **isolation rigor** — B2 + A2 substrate IS the by-construction UC-9 STACK; (3) **operational team** — B2 needs ≥2 ops engineers at G2+ for per-client provisioning automation; (4) **horizon trajectory** — B2 antifragile through G4 (per systems-scalability §4); (5) **investor barbell** — B2 is aggressive-tail (30%) at Phase-A; conservative-tail at Phase-B+ (becomes default). [F: F4 / ClaimScope: B-axis / R: high]

## §3 Architecture Diagram

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    Ruslan -->|/project-bootstrap <slug> <p-level> --client=<client> --type=<consulting|research|product>| Bootstrap[/project-bootstrap rich]

    Bootstrap --> RichScaffold[5+4 file scaffold per project]

    subgraph "Baseline (5 files; all project types)"
      Moc[_moc.md: problem_statement Cagan + state + p_level]
      Ctx[context.md: ICP + offers + leads + pricing]
      Hist[history.md: append-only events new-on-top]
      Decs[decisions.md: 4-part DRR per FPF E-9]
      OpQ[open-questions.md]
    end

    subgraph "Consulting-type additions (4 files)"
      Icp[icp.md: Ideal Customer Profile detail]
      Pipe[pipeline.md: lead → prospect → qualified → closed]
      Leads[leads/<lead-slug>.md per active lead]
      OffSpec[offline-inference-spec.md: model + hardware + acceptance test]
    end

    subgraph "Research-type additions (3 files)"
      Hyp[hypotheses.md: Popperian falsifiable claims]
      Refs[references.md: cited sources by tier]
      Drafts[drafts/<artefact-slug>.md]
    end

    subgraph "Product-type additions (4 files)"
      Roadmap[roadmap.md: milestones + dependencies]
      Bugs[bugs.md: open issues]
      Releases[releases/<version>.md]
      Metrics[metrics.md: KPI dashboard rollup]
    end

    Bootstrap --> MiniSwarm[Mini-swarm-of-3 for P1/P2]

    subgraph "Mini-swarm-of-3 (P1/P2 only)"
      ProjBrig[project-brigadier instance]
      Exp1[default expert 1 per project type]
      Exp2[default expert 2 per project type]
      ProjBrig -.->|dispatches| Exp1
      ProjBrig -.->|dispatches| Exp2
    end

    subgraph "Per-client isolation (B2 inherits A2 STACK)"
      ClientNS[clients/<client-slug>/swarm/wiki/operations/<project>/]
      EnvVar[WIKI_ROOT_CLIENT_ID env var]
      OSPerm[OS UNIX permissions]
      Holon[13th holon-ref edge + /lint]
    end

    Bootstrap -.->|--client=<slug>| ClientNS

    subgraph "Cadence + governance"
      WeeklyDigest[/project-status weekly Monday 8:00 CET]
      MonthlyReview[/project-overview monthly Ruslan + project-brigadier co-author]
      AttBudget[meta/health.md attention-budget ratchet]
      WeeklyDigest --> AttBudget
    end
```

## §4 Mechanics (~1500w)

### §4.1 B.1 Project Onboarding (UC-5 ≤30min hard cap)

**Skill: `/project-bootstrap <slug> <p-level> --client=<client> --type=<consulting|research|product>`** (mgmt-integrator candidate; new skill per Q6).

Operator invokes (multi-client example): `/project-bootstrap q3-partnerships P1 --client=client-a --type=consulting`. Skill:

1. Validates `<slug>` kebab-case + unique under `clients/<client>/swarm/wiki/operations/`; `<p-level>` ∈ {P1-P4}; `<client>` exists in `wiki-roots.yaml clients:` stanza; `<type>` ∈ enum.
2. Creates `clients/<client>/swarm/wiki/operations/<slug>/` directory (via `WIKI_ROOT_CLIENT_ID` resolution).
3. Generates 5 baseline scaffold files + 4 consulting-type files (or 3 research / 4 product per `--type`):
   - `_moc.md` (Map of Content): rich frontmatter `type: topic, layer: 6, niche: <auto>, project_type: consulting, p_level: P1, state: active, problem_statement: <Cagan: Hamel-binary REQUIRED>, kill_criteria: <binary>, granularity: client:client-a, compliance_classification: <gdpr-classification>, inference_stack: ollama-mistral-7b-q4, default_inference_tier: T-Offline, related: [theme links], part_of: [client_a_holon]`. Body: ICP / offers / pricing summary; current cycle status; key open questions.
   - `context.md`, `history.md`, `decisions.md`, `open-questions.md`: as B1 + per-client granularity field.
   - **Consulting** adds: `icp.md` (detailed Ideal Customer Profile per criteria), `pipeline.md` (lead-pipeline state with stages), `leads/` directory (per-lead pages), `offline-inference-spec.md` (model + hardware + acceptance test per UC-10).
   - **Research** adds: `hypotheses.md` (Popperian falsifiable claims per philosophy-optimizer Δ1 R.refuted_if discipline), `references.md` (cited sources with tier), `drafts/` directory.
   - **Product** adds: `roadmap.md`, `bugs.md`, `releases/`, `metrics.md`.
4. Pulls topic-wiki context: reads `wiki/themes/<theme>/` per project type (consulting → business+sales themes; research → systems+philosophy; product → engineering+systems); appends `related[]` entries.
5. **For P1/P2 projects: spawns mini-swarm-of-3.** Creates project-brigadier instance manifest at `clients/<client>/swarm/wiki/operations/<slug>/project-brigadier/manifest.md`. Allocates 2 default experts per `<type>` (consulting → mgmt+sales-researcher; research → systems+philosophy; product → engineering+systems). Project-brigadier scope limited to project's `operations/<slug>/` subtree (Q2 single-writer adapted: project-brigadier writes within scope; canonical brigadier writes wiki/global/).
6. Increments `clients/<client>/swarm/wiki/meta/health.md` `project_count` + `active_tasks_per_brigadier` (project-brigadier has separate budget from canonical brigadier).
7. Append to `clients/<client>/swarm/wiki/log.md` + `clients/<client>/swarm/wiki/index.md` + Jetix-central methodology-only log.

**Wall-clock target: ≤30 min.** Limited by Ruslan's `problem_statement:` Cagan-required field + `kill_criteria:` Hamel-binary. Skill itself runs in <90s (more files than B1 but parallel writes). [F: F4 / ClaimScope: B2-onboarding / R: high]

### §4.2 B.2 State Tracking (rich frontmatter + per-project KPIs)

**Frontmatter state machine per B1 §4.2** + B2 additions: per-project `kpi_targets:` field (e.g., consulting: leads/quarter, contracts/quarter, MRR; research: hypotheses/cycle, papers/quarter; product: features/release, MAU). KPI targets visible in weekly digest + per-client `meta/health.md` rollup.

**PMBOK Work-lifecycle alphas** (mgmt-critic gap closure): per-project `lifecycle_state:` field tracks PMBOK alphas (Initiated / Planned / Executing / Monitoring-Controlling / Closed). Distinct from `state:` (which tracks active/paused/etc.). Weekly digest reports both states. [F: F4 / ClaimScope: B2-state-tracking / R: high]

### §4.3 B.3 Mini-Swarm Per Active P1/P2 Project

**Mini-swarm-of-3** (mgmt-integrator candidate; Cagan team-topology). Components:
- **Project-brigadier instance** (`clients/<client>/swarm/wiki/operations/<slug>/project-brigadier/manifest.md`): scoped brigadier with §1d autonomous/requires-approval matrix limited to project subtree. Reads project's `_moc.md` + `decisions.md` + `open-questions.md` + relevant Layer-A topic-wikis.
- **Default expert 1**: per project_type (consulting → mgmt-expert; research → systems-expert; product → engineering-expert).
- **Default expert 2**: per project_type (consulting → sales-researcher (legacy reactivation Phase-B; or skill-based stub); research → philosophy-expert; product → systems-expert).

**On-demand experts:** other 3-4 experts dispatched via canonical brigadier; project-brigadier requests via `peer-input-needed` escalation per shared-protocols §6.

**Capacity per project-brigadier**: ≤7 active tasks (lower than canonical 20 because narrower scope). At 30 P1/P2 projects × 7 tasks = 210 active tasks across the project-brigadier swarm; ≤20 active tasks rule for canonical brigadier still preserved (canonical brigadier handles only cross-project + global tasks; per-project tasks live in project-brigadier scope).

**Mini-swarm activates only at P1/P2.** P3 projects: single on-demand expert dispatch via canonical brigadier. P4 projects: dormant; reactivate per `state: active` transition. [F: F4 / ClaimScope: B2-mini-swarm / R: high]

### §4.4 B.4 Cross-project Leverage

**Per-client cross-project sweep** (B1 §4.4 mechanism): meta-agent weekly sweep within client-holon scope. Detects within-client patterns; promotes to `clients/<client>/swarm/wiki/global/compound-rules/`.

**Cross-CLIENT pattern transfer** (B2 specific): per UC-9 STACK, FORBIDDEN by default. Opt-in case-study mode: project-brigadier proposes anonymized abstraction → HITL ack → submitted to Jetix-methodology-holon's `case-studies/<anon-id>.md` → Jetix brigadier reviews → may promote to methodology v(n+1) for all clients to pull via methodology-push.

**Edge types**: `derived_from` for within-client cross-project; methodology-push for cross-client (one-way). 13th `holon-ref` for client-holon-root anchoring (per A2). [F: F4 / ClaimScope: B2-cross-project / R: high]

### §4.5 B.5 Cadence (weekly Monday digest + monthly co-author + quarterly Ruslan letter)

**Weekly Monday digest** per B1 §4.5 — but B2 adds per-client tier:
- Per-client digest: project-brigadier writes `clients/<client>/swarm/wiki/operations/_weekly-<YYYY-Www>.md` summarizing client's projects since last Monday.
- Jetix-central digest: canonical brigadier aggregates portfolio rollup across clients (methodology-only metrics; no client content).
- Ruslan's view: portfolio rollup first; per-client drill-down on demand.

**Monthly co-author** (Cagan + GTD): project-brigadier + Ruslan co-author `clients/<client>/swarm/wiki/operations/<project>/monthly-<YYYY-MM>.md`. Per FPF E-10 writing-support clause: project-brigadier extracts; Ruslan composes prose.

**Quarterly Ruslan letter** (per FPF E-10 + Strategic Insight §4): Ruslan composes; brigadier dispatches `mode: writing-support` cells for structured extractions across all clients/projects (anonymized for cross-client portfolio summary).

**Latency targets.** Weekly per-client digest: ≤5 min Ruslan review per client (so 50 clients = 4h aggregate quarterly — sustainable with portfolio-rollup-first pattern). Monthly co-author: ≤30 min Ruslan time per high-priority project. [F: F4 / ClaimScope: B2-cadence / R: high]

### §4.6 B.6 Ruslan's Strategic Overview

**`/project-overview --portfolio` skill** aggregates traffic-light table across clients + portfolios (consulting / research / product). Drill-down via `/project-overview --client=<slug>` or `/project-overview --portfolio=consulting`.

**Scheduled Monday 8:00 CET digest** per B1 §4.6.

**Sub-roy split at G3 (Lock 21)**: at 30+ projects, brigadier proposes sub-roy split (consulting / infra / research per `decisions/JETIX-PHILOSOPHY.md §10` Universality Criterion). Each sub-roy has its own `meta/health.md` rollup; canonical brigadier sees sub-roy summaries only. Ruslan attention budget restored. [F: F4 / ClaimScope: B2-overview / R: high]

### §4.7 B.7 Lifecycle (per B1 §4.2 + B2 additions)

**B2 additions**:
- **Per-client lifecycle**: client-holon has its own state machine (`client_state:` ∈ {active | onboarding | paused | offboarded | terminated}). Distinct from project-state. Onboarding state: 30-day initial period; bootstrap automation runs.
- **Per-project lifecycle PMBOK alpha tracking**: `lifecycle_state:` ∈ {Initiated | Planned | Executing | Monitoring-Controlling | Closed}.
- **Mini-swarm dormancy**: when project `state: paused`, mini-swarm dormant; expert allocation freed for other projects.

**Knowledge extraction on termination**: `/consolidate --extract-on-termination <slug>` runs before tombstoning; extracts patterns to `wiki/global/compound-rules/` (within-client) OR opt-in to Jetix-methodology-holon (cross-client). [F: F4 / ClaimScope: B2-lifecycle / R: high]

### §4.8 B.8 Linkage to Layer A

**Read from Layer-A** per B1 §4.8 — but per-client scope. Project-wiki reads `clients/<client>/swarm/wiki/themes/<theme>/` (client-specific theme content) + `jetix-methodology-holon/themes/<theme>/` (Jetix-shared theme content) via methodology-push read-only access.

**Write to Layer-A**: within-client to `clients/<client>/swarm/wiki/claims/`; cross-client to Jetix-methodology-holon ONLY via opt-in case-study (HITL ack + anonymization).

**Cross-layer edges**: `part_of` (project _moc → client_holon_root); `derived_from` (claim → project history); 13th `holon-ref` (any client-scoped page → client_holon_root). [F: F4 / ClaimScope: B2-A-linkage / R: high]

## §5 Use-case Walkthrough (UC-1..UC-10)

### UC-1 — Video Ingest (per-client)

Per-client `/ingest`. Concept pages land in `clients/<client>/swarm/wiki/concepts/`; project's `_moc.md` related[] expands. Mini-swarm of relevant project consumes new concepts via Q1 Tier-A. [F: F3 / ClaimScope: UC-1-B2 / R: high]

### UC-2 — Weekly Digest (per-client + portfolio)

Per-client per-project digest aggregated by client portfolio aggregated by Jetix-central portfolio. Latency ≤5 min Ruslan review per portfolio. [F: F4 / ClaimScope: UC-2-B2 / R: high]

### UC-3 — Solve-with-Wiki (per-project mini-swarm dispatched)

Project-brigadier dispatches `/ask --project=<slug>` scoped to project + client themes + Jetix-methodology themes. Mini-swarm experts contribute. Synthesis writes back to `clients/<client>/swarm/wiki/comparisons/` AND `clients/<client>/swarm/wiki/operations/<project>/decisions.md`. [F: F4 / ClaimScope: UC-3-B2 / R: high]

### UC-4 — Skill Accumulation (per-project + per-client + cross-client opt-in)

Project-brigadier learns project-decomposition patterns. Appends to `clients/<client>/swarm/wiki/operations/<project>/project-brigadier/strategies.md` (project-specific). After ≥10 uses + ≥3:1 ✓/✗, promotion to client's `wiki/global/compound-rules/`. Cross-client opt-in case-study to Jetix-methodology-holon. [F: F4 / ClaimScope: UC-4-B2 / R: high]

### UC-5 — Project Onboarding (≤30 min mini-swarm spawned)

Per §4.1: `/project-bootstrap` rich variant runs in <90s skill execution + Ruslan completes `problem_statement:` in 25 min wall-clock. Total ≤30 min. Mini-swarm spawned for P1/P2 (project-brigadier instance + 2 experts allocated). [F: F4 / ClaimScope: UC-5-B2 / R: high]

### UC-6 — Cross-project Insight Transfer (within-client default; cross-client opt-in)

Per §4.4. Within-client weekly sweep promotes patterns. Cross-CLIENT promotion via opt-in case-study mode (HITL ack + anonymization mandatory). [F: F4 / ClaimScope: UC-6-B2 / R: high]

### UC-7 — Contradiction Detection (per-client + per-project)

`/lint` scoped per-client per philosophy-integrator §4 protocol. Per-project `/lint --project=<slug>` for finer granularity. Cross-client contradictions surface only in opt-in case-study (HITL ack). [F: F4 / ClaimScope: UC-7-B2 / R: high]

### UC-8 — Scale Test (B2 zone of value G2-G4)

B2 antifragile through G4 by construction. At G1 over-engineering (mini-swarm overkill for 8 internal projects); at G2 onset of first paying client → B2 mandatory; at G3-G4 B2 is default. G5 requires Alliance federation. [F: F4 / ClaimScope: UC-8-B2 / R: high]

### UC-9 — Client Isolation (B2 inherits A2 STACK + per-project; ≥200w)

B2 inherits A2 defense-in-depth STACK + adds per-project layer:

**Layer 1-4 (inherited from A2)**: filesystem-namespaced (clients/<slug>/) + per-client git repo + 13th `holon-ref` edge + frontmatter granularity:client:<slug>.

**Layer 5 (B2-specific): per-project granularity within client.** Each project's artefacts carry `granularity: client:<slug>:project:<slug>`. `/lint` extends L-CROSS-CLIENT-GLOBAL signal with cross-PROJECT-within-client check (optional; default off — cross-project within client is allowed).

**Layer 6 (B2-specific): per-project mini-swarm scope.** Project-brigadier instance has read-write scope limited to `operations/<slug>/` subtree (Q2 single-writer adaptation). Cross-project read-only via Q1 Tier-A. Project-brigadier CANNOT write to cross-project paths.

**Per-client agent instantiation per A2.** Multiple project-brigadier instances per client (one per active P1/P2). Independent processes; no shared mutable state. Methodology-push delivers project-brigadier prompt updates to all clients.

**Pen-test scenario.** Hostile actor compromises Client-A's project-X mini-swarm (e.g., prompt-injection in `decisions.md`). Result: project-brigadier scope limits damage to project-X subtree. Client-A's other projects unaffected (separate mini-swarms). Client-B fully unaffected (separate client-holon, OS UNIX permissions deny). Audit trail shows attack pattern; methodology v(n+1) hardens against this prompt-injection class.

**Acceptance predicate.** Pen-test confirms: (a) cross-CLIENT read denied at OS level; (b) cross-PROJECT-within-client read works (intentional) but cross-project WRITE denied at project-brigadier scope; (c) /lint signals fire on attempted L-CROSS-CLIENT-GLOBAL violations. [F: F4 / ClaimScope: UC-9-B2 / R: high / refuted_if: pen-test reveals cross-project write OR cross-client read]

### UC-10 — Offline-First Inference (B2 inherits A2 + per-project tier-config; ≥200w)

B2 inherits A2's local-LLM stack + per-project `inference_stack:` + `default_inference_tier:` fields:
- Consulting projects: `inference_stack: ollama-mistral-7b-q4`; `default_inference_tier: T-Offline`.
- Research projects: `inference_stack: ollama-mistral-7b-q4`; `default_inference_tier: T-Hybrid` (Ruslan-internal Jetix research).
- Product projects: `inference_stack: ollama-mistral-7b-q4`; `default_inference_tier: T-Offline` (client-private products).

Per-project `offline-inference-spec.md` (consulting projects only) declares: model_choice, hardware_requirements, acceptance_test (e.g., "20-query golden set ≥80% pass on Mistral 7B Q4 at 5s p95"). Phase-B engineering validates spec at provisioning.

**Network-disconnect test per A2 §5.** B2 inherits.

**Acceptance predicate.** Per-project offline-inference-spec.md acceptance test passes on first client deployment. Subsequent clients pass within <2h provisioning (per engineering-scalability §8). [F: F4 / ClaimScope: UC-10-B2 / R: high]

## §6 UC-9 + UC-10 Co-located Proof Section (≥400w)

B2 + A2 substrate IS the canonical UC-9 + UC-10 by-construction architecture. The defense-in-depth STACK has 6 layers when B2 is operative on A2 substrate:

**Layer 1 — Filesystem-namespaced (A2).** Each client-holon under `clients/<slug>/`; OS-level UNIX user `jetix-client-<slug>` owns the tree. Cross-client read denied at filesystem level.

**Layer 2 — Per-client git repository (A2 Phase-B).** Separate repos with separate signing keys; cross-client commit-merge impossible.

**Layer 3 — 13th `holon-ref` edge + `/lint` L-CROSS-HOLON-REF (A2).** Graph-level rejection of cross-client edges.

**Layer 4 — Frontmatter granularity `client:<slug>` + `/lint` L-CROSS-CLIENT-GLOBAL (A2).** Artefact-metadata-level rejection of cross-client global writes.

**Layer 5 (B2 addition) — Per-project granularity `client:<slug>:project:<slug>` + optional cross-project `/lint`.** Finer-grained scoping; supports per-project access controls if Mittelstand client requires (e.g., separate teams per project within client).

**Layer 6 (B2 addition) — Per-project mini-swarm scope.** Project-brigadier instance has write-scope limited to project subtree. Cross-project writes require canonical brigadier (HITL-mediated for any cross-project promotion). Multiple project-brigadier processes per client; no shared mutable state.

**Local-LLM family supported (inherited).** ollama + Mistral 7B Q4_K_M default. Per-project `offline-inference-spec.md` declares stack + acceptance test. Mittelstand-finance clients may require larger models (Llama 3.1-70B Q4 = 48GB GPU; €15K capex per A100 amortized).

**Hosting model alignment.** All 3 paths supported:
- **Path B (Client-hosted; default Phase-A first 1-3 clients per investor §6):** client owns hardware + KB; Jetix ships methodology + project-brigadier prompt updates. 70.7% GM at €3K + €15K/yr per investor Δ-H3.
- **Path A (Jetix-hosted EU VPS):** Jetix operates per-client VM + per-client mini-swarm processes; client KB on Jetix VM. ~70% GM at €15K/yr (knife-edge; viable for low-touch SMB).
- **Path C (Hybrid):** Jetix operates per-client mini-swarm processes; client owns KB filesystem; secure mTLS tunnel between. 54% Phase-A GM (fails floor); 82% at €50K enterprise tier post-G2 contractor-#1.

**Tier split per project type per project.** Consulting: T-Offline default; T-Hybrid HITL for novel synthesis. Research: T-Hybrid default. Product: T-Offline default. Per-project override via `default_inference_tier:` field.

**EU compliance alignment.** Inherited from A2 + B2-specific per-project compliance_classification frontmatter field. Per-project DPIA (GDPR Art. 35) for any project where `compliance_classification: gdpr-art-9-special-category`. BSI C5 / ISO 27001 audit trail per-project per-client.

**Pen-test + network-disconnect tests.** Per UC-9 + UC-10 §5 + B2-specific cross-project scope test. [F: F4 / ClaimScope: UC-9+UC-10-B2-co-located / R: high]

## §7 Pros / Cons / Tradeoffs

**Pros.** (a) **Antifragile through G4 by construction** — only PM variant scaling cleanly to 50→500 clients without architectural change. (b) **PMBOK + GTD + Cagan integrated** — per-project Work-lifecycle alphas + weekly review + problem-over-solution. (c) **Mini-swarm-of-3 fits Cagan empowered teams** — project-brigadier + 2 experts = mission-team per Cagan. (d) **Per-project rich-scaffold supports compliance** — per-project DPIA, KPIs, PMBOK lifecycle audit trail; BSI C5 / ISO 27001 ready. (e) **Mittelstand AI Alliance EISA-moment alignment** — federation pattern IS the Alliance template per Strategic Insight §4 + investor-integrator §4.

**Cons.** (a) **Highest setup cost at G1** — over-engineering for 8 Jetix-internal projects; mini-swarm overhead. (b) **Per-client provisioning automation = G2-G3 critical engineering investment** — manual per-client onboarding ~2 days first; ~2h subsequent (per engineering-scalability §8). (c) **Methodology-version coordination at G3+** — when methodology v1.5 changes project-brigadier prompt, all 50 clients pull at different times; version skew tracker required. (d) **Ruslan attention budget at G3** — even with sub-roy split, 30+ active P1 projects across 50 clients = high coordination load.

**Tradeoffs.** (1) Setup overhead vs antifragility: B2 chooses 2-day first-client setup for permanent G2-G4 antifragility. (2) Operational complexity vs by-construction-isolation: B2 + A2 is the defense-in-depth STACK gold standard; cost is per-client ops automation. (3) Per-project mini-swarm vs single-brigadier-on-demand: mini-swarm = better per-project context accumulation; cost = more processes/agents. (4) PMBOK rigor vs Phase-A speed: B2 PMBOK alpha tracking is overkill at G1; pays off at G2-G3 for compliance-strict Mittelstand clients.

## §8 Effort Estimate

- **Bootstrap (Day 1):** 2-3 weeks (after A2 substrate operational). Limited by: rich `/project-bootstrap` skill + 9 scaffold templates per project_type + project-brigadier instance template + mini-swarm allocation logic + `meta/health.md` extension for project-brigadier ratchet.
- **UC-1..UC-4 live (per-client per-project):** 3-4 weeks. Limited by: first per-client mini-swarm provisioning + first weekly digest cycle + first cross-project pattern detection.
- **UC-5..UC-8 stable:** 6-8 weeks. Limited by: ≥3 client-holons operational with mini-swarms + first methodology-update cycle for project-brigadier prompts + portfolio-rollup digest authoring.
- **UC-9 + UC-10 live (Phase-B by-construction):** 3-4 weeks. Limited by: A2 STACK Phase-B activation + per-project DPIA templates + cross-project pen-test + per-project offline-inference-spec validation.

## §9 Migration Path from Current State

B2 builds on B1 (which builds on existing D1 Layer-6 substrate). B2 activates per client at G2 first paying client. Migration steps:

1. **Author** rich scaffold templates per project_type (`swarm/wiki/_templates/project-scaffold-{consulting,research,product}/`).
2. **Extend** `/project-bootstrap` skill with `--client=<slug>` + `--type=<consulting|research|product>` + mini-swarm spawn logic.
3. **Author** project-brigadier instance template (`agents/project-brigadier/manifest.template.md`).
4. **Extend** `meta/health.md` schema with per-client + per-portfolio aggregation; per-project KPI rollup.
5. **Extend** `/project-status` skill with per-client + portfolio drill-down + traffic-light table.
6. **Author** `/project-overview --portfolio` skill aggregating sub-roy splits.
7. **Author** per-project DPIA templates per project_type (consulting requires GDPR Art. 22 + 32 stub; research may add Art. 9 if special-category data; product may add EU AI Act Art. 14).
8. **Author** `/lint` L-CROSS-CLIENT-PROJECT signal (cross-project within client; default off, opt-in).
9. **Test** mini-swarm provisioning + tear-down + per-project pen-test on first client.

**Staging order.** Steps 1-4 in parallel. Step 5 after step 4. Steps 6-7 in parallel. Step 8 in parallel. Step 9 sequential.

**Rollback.** Per-client per-project; rolling back one mini-swarm doesn't affect others. Client opt-out: revert to B1 thin-scaffold (keeps `_moc.md` + `decisions.md` + `history.md`; archives the rest).

## §10 Horizon Projection (≥600w; 5 gates)

| Gate | Projects | Mini-swarms | Clients | Physical failure | Upgrade path | MHT event | BOSC-A-T-X | Janus risk | Per-project ops |
|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | 8 | 0 (no client; B2 not active) | 0-1 | over-engineering at Jetix-internal scale | B2 deactivated; B1 sufficient | — | — | — | minimal |
| **G2 €200K** | 15 (incl 7-10 client) | 5-7 (P1/P2 client projects) | 10 | first per-client mini-swarm provisioning manual ~2 days; CI automation absent | CI methodology-push to project-brigadier prompts; per-client provisioning script (≤2h after first); B2 mandatory for client work | Phase Promotion (per-client mini-swarm; project-brigadier-as-Layer-3-agent); Role-Lift (some experts become project-default vs on-demand) | Operation + Composition + Agency | medium INT excess (per-client coordination overhead); medium S-A excess (Jetix-central monopoly on project-brigadier prompt updates) | per-client GPU rental ~€100-150/mo; per-mini-swarm context budget within Opus 1M |
| **G3 €1M** | 30 (~20 client) | 15-20 mini-swarms | 50 | mini-swarm count exceeds canonical brigadier coordination capacity; methodology-version skew (some clients on v1.4, others v1.5); per-portfolio digest aggregation latency | Sub-roy split (consulting / infra / research per Lock 21); per-portfolio brigadier; methodology-version-skew tracker; GPU procurement gate (≥3 paying clients per portfolio) | Fission (canonical brigadier into per-portfolio sub-brigadiers; meta-agent into per-cluster); Context Reframe (each portfolio peer-roy of Jetix-central) | Composition + Agency + Operation | high INT excess (per-portfolio autonomy creates coordination overhead) — mitigated by per-portfolio sub-roy + Alliance methodology parliament; high S-A excess (sub-roy autonomy needs methodology checks) | per-Alliance-member self-coordinates; Mittelstand-LLM 13B+ default emerging |
| **G4 $100M** | 100 (~80 client) | 50+ mini-swarms | 500 | per-portfolio coordination strains Ruslan attention budget at scale; Mittelstand AI Alliance governance not yet structured; methodology coherence breaks (>3 active versions) | Mittelstand AI Alliance formal entity; methodology-license revenue replaces deployment revenue per investor-scalability §4; Alliance methodology parliament (philosophy-scalability §7); per-Alliance-member sub-roys; per-region governance | Role-Lift (Alliance governance committee); Context Reframe (Jetix-central as standards-body, Strategic Insight §3-§4 EISA); Fusion (Alliance methodology versions canonical) | eXternal + Composition + Agency + Operation | pervasive (mitigated by quarterly Alliance methodology parliament + outcome-level telemetry) | Mittelstand-LLM (Phoenix-BIOS-equivalent per Strategic Insight §8 rec 7) emerges as Alliance-blessed model |
| **G5 $1T** | 500+ (Alliance) | 200+ across federation | 5000+ | distributed coordination; per-roy methodology drift on PM scaffold conventions; Alliance bureaucracy risk | federated PM scaffold conventions; per-region committees; Token economy Option B (D23) tie-in for Alliance member voting | Continuous Fusion (Alliance-shared scaffold conventions); Re-Phase-Promotion at every Alliance methodology release | eXternal + Composition + Agency + Time | pervasive (mitigated by Alliance parliament + outcome-level telemetry per philosophy-scalability §6) | per-Alliance-member sovereign PM; Jetix-central provides scaffold + methodology + brand + standards |

**Antifragility verdict.** B2 is the **only Layer-B variant antifragile through G4 by construction.** G5 conditional on Alliance governance Phase-B+ work. [F: F4 / ClaimScope: B2-horizon / R: high]

## §11 Anti-Fragility Assessment (≥400w)

**Verdict: TRUE ANTIFRAGILE through G4 by construction; CONDITIONAL ANTIFRAGILE at G5 (requires Alliance governance Phase-B+ work).**

**Mechanism for true antifragility G2-G4.** Per Kauffman adjacent-possible: each new client-holon adds an independent variation source. Per-client mini-swarms run independent project decompositions; methodology-push consolidates patterns; opt-in case-studies feed cross-client insights anonymized. With 50 clients × 5 projects each = 250 mini-swarms (G3), Jetix sees 250 independent stress tests of project-mgmt methodology weekly. The methodology gets BETTER with each client because variation in challenges (Mittelstand vendor compliance vs healthcare regulatory vs financial-services audit) exercises corner cases B1 single-tenant could never surface. **B2 IS the EISA-moment compounding mechanism per Strategic Insight §4 + investor-integrator §4 at the project-mgmt layer.**

**Mechanism for conditional antifragility G5.** At 5000+ clients × 500+ projects per Alliance member, variation overwhelm: methodology-version skew + per-roy ontology drift + governance bureaucracy risks INT-excess. The conditional safeguard: Alliance methodology parliament (philosophy-scalability §7) with adversarial mandate (Lakatos protective belt). If parliament structured well (rotating sub-roy leadership; outcome-telemetry-driven decisions), G5 antifragile. If parliament ossifies into bureaucracy, G5 fragile.

**Pressure tests.**

(1) **Methodology v1.4 → v1.5 changes project-brigadier prompt; BREAKS 3 mini-swarms.** Per A2 pressure test 1, broken mini-swarms SIGNAL bug; rollback protects other mini-swarms. **Antifragile because:** the 3 broken mini-swarms surface the bug before propagation. B1 single-brigadier would have shipped the bug to its sole instance.

(2) **Project pivot mid-cycle (e.g., consulting client pivots from "DACH outreach" to "DACH partnerships").** Mini-swarm `state: pivoted`; new project + new mini-swarm spawned; old project archived; `derived_from` edge preserves continuity. **Antifragile because:** lifecycle state machine is built-in; pivots add information (client learning) rather than disrupting.

(3) **Domain expert prompt rewritten Phase-B (engineering-expert v2 with new mode).** Methodology-push delivers new prompt to all 50 client-holons. Each client opts in. Per-project mini-swarm reads new prompt at next dispatch. **Antifragile because:** capability propagates without per-project retraining.

(4) **Project forked into parallel directions across CLIENTS (3 clients independently build "DACH outreach playbooks").** Each client's playbook stays in client-holon. Anonymized opt-in case-study to Jetix-methodology-holon; methodology v1.6 includes "DACH-outreach-playbook" template for all clients to pull. **Antifragile because:** decentralized exploration → centralized methodology consolidation. [F: F4 / ClaimScope: B2-anti-fragility / R: high]

## §12 Open Questions for Ruslan

1. **B2 activation per client:** automatic at first paying client onboarding (Phase-B onset)? Or staged (B1 first 30 days; B2 after onboarding period)?
2. **Mini-swarm-of-3 default expert allocation per project_type:** confirm consulting → mgmt+sales-researcher; research → systems+philosophy; product → engineering+systems? Or per-client custom?
3. **Project-brigadier active-tasks budget:** ≤7 per project-brigadier (B2 default) OR ≤5 (more conservative; supports more mini-swarms in parallel)?
4. **Per-project DPIA template authority:** Jetix-central provides template; client lawyer signs OR Jetix-affiliated legal counsel co-signs?
5. **Cross-CLIENT case-study opt-in mechanism:** project-brigadier proposes; canonical brigadier reviews + Ruslan acks (default) OR client legal counsel co-signs anonymization?
6. **Mittelstand AI Alliance formal entity timing:** G3 (50 clients; investor §3 timing) OR G4 ($100M revenue; Alliance scale)?

— brigadier (Phase-5 variant draft), 2026-04-24
