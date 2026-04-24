---
title: Variant B3 — "Adaptive-scaffold phase-gated autonomy (biological morphogenesis)"
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
confidence: medium
confidence_method: brigadier-integration-from-engineering-scalability-B3-axis-and-mgmt-optimizer
tier: tier-1
produced_by: brigadier
sources:
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-scalability-ingest-retrieval-horizon.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-optimizer-scaffold-deltas.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-optimizer-frg-discipline.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md"}
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md"}
  - {path: "decisions/JETIX-PHILOSOPHY.md", range: "§6 Quality Fundamentals (1000% depth, fractal quality)"}
related: []
binding_scope: km-architecture-variant-B3
---

# Variant B3 — "Adaptive-Scaffold Phase-Gated Autonomy (Biological Morphogenesis)"

## §1 Name + One-line Pitch

**B3 — Adaptive-Scaffold Phase-Gated Autonomy : project scaffold starts MINIMAL (1-3 files) at bootstrap; auto-extends sections (icp.md, leads/, contracts/, pipeline.md, hypotheses.md, etc.) when stage-gate predicates fire (e.g., ≥3 leads → leads/ activates; ≥1 signed contract → contracts/ activates; ≥1 falsified hypothesis → hypotheses.md gains supersession entry); each extension carries Hamel-binary activation predicate; mini-swarm spawns conditionally (P1+contract-stage triggers project-brigadier, not P1-on-bootstrap); like biological morphogenesis — complexity emerges from developmental triggers, not pre-specified at birth.** [F: F3 / ClaimScope: PM-architecture-adaptive / R: medium]

## §2 Axis of Differentiation (~110w)

This variant occupies the **adaptive-scaffold / phase-gated-autonomy / morphogenetic** quadrant. Variant B1 occupies *thin-scaffold-static / single-brigadier / Phase-A*. Variant B2 occupies *rich-scaffold-static / per-client mini-swarm / Phase-B-default*. Choice between them governed by: (1) **scaffold cost per project stage** — B3 minimizes upfront cost (3 files at bootstrap) but ratchets up on triggers (could end at 9+ files like B2 if project succeeds); (2) **predicate rigor discipline** — B3 requires Hamel-binary stage-gate predicates (per philosophy-optimizer Δ1 + brigadier OPP-04 cycle-2 schema); risk if predicates loose: B3 collapses to ad-hoc; (3) **horizon trajectory** — B3 promising at G1-G2 with rigorous predicates; antifragility uncertain at G3-G5 (less proven than B2); (4) **investor barbell** — B3 is *exploratory-tail* (10% of barbell); high-variance bet. **B3 represents biological morphogenesis pattern (Kauffman / Kelly out-of-control); requires philosophy-grade epistemic discipline.** [F: F3 / ClaimScope: B-axis-B3 / R: medium]

## §3 Architecture Diagram

```mermaid
graph TD
    Ruslan -->|/project-bootstrap-adaptive <slug> <p-level>| Bootstrap[/project-bootstrap --adaptive]

    Bootstrap --> Minimal[3-file minimal scaffold]
    Minimal --> Moc1[_moc.md: problem_statement Cagan + state + p_level + stage_gates declared]
    Minimal --> Hist1[history.md: append-only events]
    Minimal --> OpQ1[open-questions.md: pending Ruslan decisions]

    subgraph "Stage-Gate Predicates (Hamel-binary; declared in _moc.md)"
      SG1[Trigger: leads_count >= 3]
      SG2[Trigger: contracts_signed >= 1]
      SG3[Trigger: hypothesis_validated >= 1 OR hypothesis_refuted >= 1]
      SG4[Trigger: cycle_count >= 5 AND active_tasks >= 5]
      SG5[Trigger: client_revenue_recurring >= 1000_eur_per_month]
    end

    subgraph "Scaffold Extensions (auto-spawn when SG fires)"
      Ext1[SG1 → leads/ + pipeline.md]
      Ext2[SG2 → contracts/ + decisions.md]
      Ext3[SG3 → hypotheses.md + references.md]
      Ext4[SG4 → mini-swarm spawn (project-brigadier + 2 experts)]
      Ext5[SG5 → kpi_targets + monthly co-author cadence]
    end

    SG1 -.->|when fires, auto-spawn| Ext1
    SG2 -.->|when fires, auto-spawn| Ext2
    SG3 -.->|when fires, auto-spawn| Ext3
    SG4 -.->|when fires, auto-spawn| Ext4
    SG5 -.->|when fires, auto-spawn| Ext5

    subgraph "Predicate evaluation"
      LintCron[/lint --check-stage-gates daily cron]
      LintCron --> EvalSG[Evaluates predicates against scaffold + history]
      EvalSG -->|fires SG → triggers extension| Ext1
      EvalSG -->|surfaces in next digest| Digest[/project-status weekly]
    end

    subgraph "Risk mitigation: predicate rigor"
      PhilCheck[philosophy-expert × critic on every new SG predicate]
      PhilCheck -->|REJECT if not Hamel-binary| Bootstrap
    end

    subgraph "B3 inherits B2 STACK at full-extension"
      FullB2[At full SG firing: B3 = B2 by construction]
    end
    Ext4 -.->|≥4 SGs fired| FullB2
```

## §4 Mechanics (~1500w)

### §4.1 B.1 Project Onboarding (UC-5 ≤30min minimum)

**Skill: `/project-bootstrap-adaptive <slug> <p-level> [--client=<slug>] [--type=<consulting|research|product>]`** (mgmt-integrator candidate; new skill; per Q6 candidate → learning → active).

Operator invokes: `/project-bootstrap-adaptive new-bet-X P1`. Skill:

1. Validates per B1 §4.1 step 1.
2. Creates `swarm/wiki/operations/<slug>/` directory (or `clients/<client>/swarm/wiki/operations/<slug>/` per UC-9).
3. Generates **3-file minimal scaffold** (vs B2's 5+4):
   - `_moc.md`: rich frontmatter with `state: active, p_level: P1, problem_statement: <Cagan>, kill_criteria: <Hamel-binary>, **stage_gates:**` declaring 5 Hamel-binary triggers per §4.2; `granularity: client:<slug>`; `inference_stack:` etc.
   - `history.md`: append-only.
   - `open-questions.md`: pending Ruslan decisions.
4. **No ICP / pipeline / leads / hypotheses / decisions files yet** — those auto-spawn on SG firing per §4.3.
5. **No mini-swarm yet** — single-brigadier handles initial cycles per B1 model. Mini-swarm spawns on SG-4 trigger (cycle_count ≥ 5 AND active_tasks ≥ 5).
6. Pulls topic-wiki context per B1 §4.1 step 4.
7. Increments `meta/health.md project_count`.

**Wall-clock target: ≤15 min** (B3 fastest because least scaffold). Bootstrapped in <30s skill execution + Ruslan completes `problem_statement:` + `kill_criteria:` + `stage_gates:` declarations in 10-15 min. [F: F3 / ClaimScope: B3-onboarding / R: medium]

### §4.2 Stage-Gate Predicates (Hamel-binary discipline; declared in `_moc.md`)

Per philosophy-optimizer Δ1 R.refuted_if discipline: every stage-gate predicate is HAMEL-BINARY. Each project's `_moc.md` declares 5 default stage-gates (per project_type's template):

**Consulting project default SGs:**
- **SG-1 leads:** `count(leads/<slug>.md) >= 3` → spawns `leads/` directory + `pipeline.md`.
- **SG-2 contracts:** `count(contracts/<slug>.md) >= 1` (any signed contract) → spawns `contracts/` + extends `decisions.md` to 4-part DRR per E-9.
- **SG-3 hypotheses:** `count(history.md entries with type:hypothesis) >= 1 AND (validated OR refuted)` → spawns `hypotheses.md` + `references.md`.
- **SG-4 cycle:** `cycle_count >= 5 AND active_tasks_per_brigadier >= 5` → spawns mini-swarm (project-brigadier + 2 default experts per project_type per B2 §4.3).
- **SG-5 revenue:** `client_revenue_recurring_eur_per_month >= 1000` → adds `kpi_targets:` + monthly co-author cadence (Cagan + GTD).

**Research project default SGs:** SG-3a (hypothesis count ≥ 5 → `hypotheses.md` mandatory); SG-3b (refuted hypotheses ≥ 1 → philosophy-expert mode dispatch); SG-4 (per consulting); SG-rd (paper drafted ≥ 1 → `drafts/`).

**Product project default SGs:** SG-roadmap (milestone count ≥ 3 → `roadmap.md`); SG-bugs (open issues ≥ 5 → `bugs.md`); SG-release (release count ≥ 1 → `releases/`); SG-metrics (DAU/MAU tracking active → `metrics.md`).

**Custom SG declaration.** Ruslan or project-brigadier may declare custom SGs in `_moc.md` (must pass philosophy-critic review for Hamel-binary discipline). [F: F4 / ClaimScope: B3-stage-gates / R: medium]

### §4.3 Predicate Evaluation + Auto-Spawn

**Daily cron: `/lint --check-stage-gates`** runs per project. For each project's `_moc.md stage_gates:` declarations:
1. Evaluates predicate against current scaffold + history.
2. If FIRES (predicate evaluates TRUE), checks if SG already fired (idempotent).
3. If first-fire, executes auto-spawn:
   - Creates extension files per template (e.g., `leads/` directory + `pipeline.md` template).
   - Updates `_moc.md` with `stage_gate_fired: SG-1 at <date>` audit trail.
   - Appends `history.md`: "stage-gate SG-1 fired; spawned leads/ + pipeline.md".
   - For SG-4 (mini-swarm trigger): spawns project-brigadier instance per B2 §4.3.
4. Surfaces in next weekly digest as "B3 stage-gate fires this week: N".

**Risk**: predicate misfire (e.g., SG-1 fires on test-data leads). Mitigation: every predicate is Hamel-binary AND validated by philosophy-critic at SG-declaration time; auto-spawn is REVERSIBLE (rollback by deleting extension files + reverting `_moc.md` audit trail). Phase-B engineering work: SG-misfire detection + auto-rollback cron.

### §4.4 B.2 State Tracking (per B1+B2 + adaptive frontmatter fields)

`_moc.md state:` per B1 §4.2 + B3 additions:
- `stage_gates: { SG-1: declared_at, SG-1_fired_at?, SG-1_spawn_paths: [...] ... }`.
- `scaffold_complexity:` automated rollup (`minimal | partial | rich | full-B2-equivalent`).
- `morphogenesis_log: [...]` append-only audit of SG firings.

PMBOK Work-lifecycle alphas tracked per B2 §4.2. [F: F3 / ClaimScope: B3-state-tracking / R: medium]

### §4.5 B.3 Agent-per-project (single-brigadier → mini-swarm on SG-4)

Bootstrap: single Jetix brigadier handles project (per B1 model). When SG-4 fires (cycle_count ≥ 5 AND active_tasks ≥ 5), mini-swarm spawns per B2 §4.3 (project-brigadier instance + 2 default experts per project_type).

**Capacity**: pre-SG-4: project consumes 1-3 active tasks of canonical brigadier's ≤20 budget. Post-SG-4: project-brigadier has its own ≤7 active-tasks budget; canonical brigadier sees only cross-project + global tasks for this project.

**Reversibility**: if project SG-4 fires but project-brigadier subsequently underperforms (e.g., FPAR <80%), mini-swarm tear-down via `/project-pause-mini-swarm <slug>`. Project reverts to single-brigadier model. [F: F3 / ClaimScope: B3-agent-model / R: medium]

### §4.6 B.4 Cross-project Leverage (per B1 + B3-adaptive)

Per B1 §4.4 meta-agent weekly sweep + B3 SG-driven detection: if pattern emerges across ≥3 projects' `history.md`, automatically declares a cross-project SG (`SG-cross: pattern <slug> appears in N projects → propose promotion to wiki/global/`). HITL ack required for promotion.

### §4.7 B.5 Cadence (adaptive)

- **Weekly digest**: per B1 §4.5; reports SG firings + scaffold-complexity changes per project.
- **Monthly co-author**: only for projects where SG-5 fired (recurring revenue ≥ €1K/month). Pre-SG-5 projects skip monthly co-author; weekly digest sufficient.
- **Quarterly Ruslan letter**: per FPF E-10; same as B1+B2.

### §4.8 B.6 Ruslan's Strategic Overview

**`/project-overview --by-stage` skill**: aggregates traffic-light by scaffold-complexity (minimal / partial / rich / full-B2) + SG-fire-rate per project. Reveals which projects are graduating (more SGs firing = more momentum) vs stagnating (no SGs firing in 4+ weeks = candidate for `state: paused`).

### §4.9 B.7 Lifecycle (per B1+B2 + B3-specific reversibility)

Per B1 §4.7 / B2 §4.7 + B3-specific:
- **De-morphing**: if project regresses (e.g., contracts churn → SG-2 conditions no longer satisfied), `/lint --check-stage-gates` flags but does NOT auto-tear-down extensions (asymmetric morphogenesis: easier to grow than shrink). Ruslan or project-brigadier may explicitly de-morph via `/project-de-morph <slug> --remove-sg=SG-N`.
- **Skip-stage**: Ruslan may declare `_moc.md skip_stage_gates: [SG-1, SG-3]` to bypass SGs (e.g., for paid contract projects that should start at full B2 from day 1; B3 effectively becomes B2 via skip).

### §4.10 B.8 Linkage to Layer A (per B1 + B3-adaptive)

Per B1 §4.8. B3 specific: as project grows scaffold (SG-2/3 fire), it pulls more topic-wiki context (more `themes/<theme>/` references in `related[]`). Layer-A reads scale with project complexity.

## §5 Use-case Walkthrough (UC-1..UC-10)

### UC-1 — Video Ingest (Layer-A; B3 same as B1)

[F: F3 / ClaimScope: UC-1-B3 / R: medium]

### UC-2 — Weekly Digest

Per B1 §5; B3-additional: weekly digest reports SG firings per project ("this week: SG-2 fired in `quick-money-DACH`; spawned contracts/ + 4-part DRR template"). Scaffold-complexity rollup. [F: F3 / ClaimScope: UC-2-B3 / R: medium]

### UC-3 — Solve-with-Wiki

Per B1 §5; project's available scaffold (e.g., pre-SG-2 = no contracts/) determines `/ask --project=<slug>` retrieval scope. Pre-SG-2 projects have less per-project content; Tier-D fallback to topic-wiki dominant. [F: F3 / ClaimScope: UC-3-B3 / R: medium]

### UC-4 — Skill Accumulation

Per B1 / B2 §5. B3-specific: SG-firing-pattern itself is a meta-pattern: brigadier learns "SG-2 fires within 2 cycles of bootstrap for consulting projects with high-quality leads" → strategies.md entry → next consulting project bootstrap may auto-elevate to higher initial scaffold. [F: F3 / ClaimScope: UC-4-B3 / R: medium]

### UC-5 — Project Onboarding (≤15min B3 minimum vs ≤30min B2)

Per §4.1: ≤15 min wall-clock (3-file scaffold + Ruslan completes problem_statement + kill_criteria + stage_gates). B3 LOWEST onboarding cost across the 3 B variants. Trade-off: less initial scaffold = less initial structure for project-brigadier to consume; project-brigadier accumulates structure as SGs fire. [F: F4 / ClaimScope: UC-5-B3 / R: medium]

### UC-6 — Cross-project Insight Transfer (per B1 + B3-adaptive cross-SG)

Per §4.6. Cross-project SG (pattern across ≥3 projects) auto-detects + proposes promotion. Lower friction than B1's manual meta-agent sweep. [F: F3 / ClaimScope: UC-6-B3 / R: medium]

### UC-7 — Contradiction Detection (per B1)

Per philosophy-integrator §4 protocol; per-project `/lint`. B3-specific: SG-3 (hypothesis-refuted ≥ 1) is itself a contradiction-driven extension; spawns `hypotheses.md` to track the supersession chain. [F: F3 / ClaimScope: UC-7-B3 / R: medium]

### UC-8 — Scale Test (B3 promising G1-G2; uncertain G3+)

B3's antifragility is morphogenetic — promising at G1-G2 (low overhead; grows as needed). At G3+, B3 effectively converges to B2 for any project with SG-4 fired (mini-swarm spawned). G3-G5 antifragility = B2-equivalent for graduated projects + B3-thin for early-stage. **Risk**: if SG-discipline degrades (predicate misfires; auto-spawn errors), B3 collapses to ad-hoc. [F: F3 / ClaimScope: UC-8-B3 / R: medium]

### UC-9 — Client Isolation (B3 inherits A2 + B2 STACK; ≥200w)

B3 inherits A2's defense-in-depth STACK + B2's per-project-mini-swarm scope (when SG-4 fires). Pre-SG-4: project lives in client-namespaced directory + frontmatter granularity (B1-equivalent isolation). Post-SG-4: full per-project mini-swarm scope (B2-equivalent isolation).

**B3-specific consideration**: stage-gate predicates may themselves leak cross-client information if mis-designed. E.g., SG-1 "leads_count >= 3" — if leads/ files contain identifying data, predicate evaluation must NOT log client-private content to cross-client audit logs. **Mitigation**: SG predicate evaluation runs per-client UNIX user; predicates evaluate against per-client filesystem only; predicate-firing audit logs anonymized at cross-client portfolio rollup.

**Pen-test scenario**: hostile actor crafts a malicious SG predicate in a project's `_moc.md` that attempts to enumerate cross-client filesystem. Result: predicate evaluation runs as `jetix-client-<slug>` UNIX user; cross-client read denied at OS level; predicate evaluates FALSE; no spawn. Audit log shows the attempted predicate; methodology v(n+1) hardens predicate-evaluation sandbox.

**Acceptance predicate**: per-project SG firings produce auto-spawns within client-holon scope only; pen-test verifies cross-client SG predicate misfires denied at OS. [F: F4 / ClaimScope: UC-9-B3 / R: medium / refuted_if: SG predicate enumerates cross-client filesystem successfully]

### UC-10 — Offline-First Inference (per B2; ≥200w)

B3 inherits B2's UC-10 mechanism per §5. B3-specific: SG predicate evaluation cron runs locally (no LLM required for most predicates — counts + filesystem checks); SG predicates that require local-LLM evaluation (e.g., "history.md mentions of 'partnership' >= 5" requires entity extraction) use Mistral-7B local LLM per inference-stack.yaml. Zero outbound network. [F: F4 / ClaimScope: UC-10-B3 / R: medium]

## §6 UC-9 + UC-10 Co-located Proof Section (≥400w)

B3 inherits A2's UC-9 STACK + B2's per-project layer (when SG-4 fires). Pre-SG-4 projects use B1-equivalent isolation (directory namespace + frontmatter granularity). Post-SG-4 projects use full B2 isolation (per-project mini-swarm scope).

**B3-specific UC-9 consideration: stage-gate predicate-evaluation sandbox.** Predicates run per-client UNIX user (jetix-client-<slug>); predicate-firing audit logs anonymized at portfolio rollup. Hostile predicate enumerating cross-client denied at OS level.

**B3-specific UC-10 consideration: predicate evaluation is offline-first by construction.** Most predicates are pure filesystem/counter operations (no LLM); LLM-required predicates (entity-detection in history.md) use Mistral-7B local. Zero outbound network for SG evaluation cron.

**Local-LLM family supported (inherited).** Per A2/B2: ollama + Mistral 7B Q4_K_M default (Apache 2.0). B3-specific note: SG predicate evaluation latency budget is generous (daily cron), so larger models (Llama 3.1-70B Q4) feasible if needed for entity-extraction quality.

**Hosting model alignment.** Per A2/B2.

**Tier split per project type per project per stage.**
- Consulting projects pre-SG-2: T-Offline default (limited scaffold; less retrieval surface).
- Consulting projects post-SG-2: T-Offline default; T-Hybrid HITL for novel synthesis.
- Research projects pre-SG-3: T-Hybrid default (Jetix-internal research; pre-hypothesis-refutation phase has fewer constraints).
- Research projects post-SG-3: T-Offline default (refuted hypotheses must be supersession-chained; cloud LLM may introduce drift).
- Product projects per stage: T-Offline default (client-private throughout).

**EU compliance alignment per A2/B2.** B3-specific: per-project DPIA template auto-spawns when SG-2 fires (contract signed → compliance-classification declared in contracts/ template).

**Pen-test + network-disconnect tests per A2/B2 §5.** B3-specific: SG predicate-evaluation pen-test (hostile predicate enumeration). [F: F3 / ClaimScope: UC-9+UC-10-B3-co-located / R: medium]

## §7 Pros / Cons / Tradeoffs

**Pros.** (a) **Lowest onboarding cost** (≤15min vs B1 ≤30min vs B2 ≤30min full-rich); fits exploratory projects. (b) **Scaffold cost matches project momentum** — fragments resources go to projects that earn them via SG firings. (c) **Reversible morphogenesis** — extensions can be torn down if project regresses. (d) **Meta-pattern detection** — SG-firing patterns themselves yield strategies.md insights. (e) **Forward-compatible to B2** — at full SG firing, B3 = B2 by construction.

**Cons.** (a) **Predicate rigor discipline mandatory** — if SGs are loose, B3 collapses to ad-hoc; risk = high if discipline lapses. (b) **Scaffold-complexity variance across projects** confuses Ruslan oversight (different projects look architecturally different at any moment); B3 needs `/project-overview --by-stage` skill to surface this clearly. (c) **Less-proven antifragility at G3+** vs B2 (which has 4 cells' worth of horizon validation in this cycle). (d) **Auto-spawn errors are public artefacts** — if SG misfires + spawns wrong template, the wrong template lives in the repo until rollback (filesystem-native means audit-trail intact but visible).

**Tradeoffs.** (1) Onboarding speed vs scaffold predictability: B3 = fast onboard, variable scaffold; B2 = standard onboard, predictable scaffold. (2) Resource efficiency vs cognitive overhead: B3 economizes scaffold cost but adds cognitive load (different projects look different). (3) Predicate-driven autonomy vs HITL gates: B3 leans on auto-spawn (speed); B2 leans on Ruslan-driven activation (predictability). (4) Exploratory bet vs proven bet: B3 is the *exploratory-tail* (10%); B2 is the *proven-tail* (default Phase-B).

## §8 Effort Estimate

- **Bootstrap (Day 1):** 2-3 weeks. Limited by: SG predicate evaluation cron + auto-spawn template engine + philosophy-critic gate on SG declarations + reversibility logic.
- **UC-1..UC-4 live:** 2-3 weeks. Limited by: first project bootstrap with B3 + observe SG firings + iterate on predicate rigor.
- **UC-5..UC-8 stable:** 6-8 weeks. Limited by: cross-project SG-pattern detection + auto-rollback on misfire + integration with B2 substrate at SG-4-trigger.
- **UC-9 + UC-10 live (B3 specific):** 3-4 weeks. Limited by: SG predicate sandbox + per-project DPIA auto-spawn + offline-first predicate evaluation cron.

## §9 Migration Path from Current State

B3 builds on B2 (which builds on B1). B3 specific deltas:

1. **Author** `/project-bootstrap-adaptive` skill with `--type` template selector; minimal 3-file scaffold.
2. **Author** `_templates/project-stage-gates-{consulting,research,product}.yaml` declaring 5 default SGs per project_type.
3. **Author** `/lint --check-stage-gates` cron + auto-spawn template engine.
4. **Author** philosophy-critic SG-validation skill (Hamel-binary check on SG declarations at bootstrap + at any custom SG addition).
5. **Author** `/project-de-morph` reversibility skill.
6. **Extend** `/project-overview --by-stage` skill aggregating scaffold-complexity rollup.
7. **Extend** `_moc.md` frontmatter with `stage_gates: {...}` + `morphogenesis_log: [...]` + `scaffold_complexity:` fields.
8. **Test** SG firings + auto-spawn + reversibility on first 2 B3 projects (Jetix-internal first; client only after Phase-B onset).

**Staging order.** Steps 1-4 in parallel. Step 5 in parallel. Step 6 after step 7. Step 7 in parallel. Step 8 sequential.

**Rollback.** Per-project; reverting to B2 means: declare project in `state: paused` per B3; manually populate B2's standard 9-file scaffold from B3's morphogenesis log; resume as B2.

## §10 Horizon Projection (≥600w; 5 gates)

| Gate | Projects | SG-firings/wk | Clients | Physical failure | Upgrade path | MHT event | BOSC-A-T-X | Janus risk | Per-project ops |
|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | 8 | ~5-10 (early-cycle exploration) | 0-1 | predicate misfire risk on first 2-3 projects (B3 less battle-tested); cron orchestration tooling absent | rigorous philosophy-critic SG-validation; manual SG audit weekly; iterate on predicate templates | — | Time | medium INT (Ruslan oversight required for SG misfire detection); low S-A | minimal cron compute; predicate evaluation sub-second per project |
| **G2 €200K** | 15 (mix of mature + exploratory) | ~15-25 | 10 | scaffold variance across projects confuses Ruslan oversight (different projects look architecturally different); cross-client SG predicates may emerge | `/project-overview --by-stage` skill; cross-client SG = HITL ack mandatory; per-project DPIA auto-spawn refinement | Phase Promotion (cron from manual to scheduled; per-project SG audit elevated); first cross-project SG-pattern detected | Operation + Composition | medium INT excess (per-project autonomy creates variance); medium S-A excess (Jetix-central monopoly on SG template) | per-client SG cron on rented compute; ~€20-50/mo per client |
| **G3 €1M** | 30 (~70% post-SG-4 = B2-equivalent; 30% B3-thin exploratory) | ~50+ | 50 | mature projects converge to B2; B3-thin exploratory projects pile up; Ruslan attention budget; SG misfire cumulative risk | sub-roy split per portfolio; per-portfolio SG governance; auto-rollback cron at portfolio level; B3 confined to research / bets portfolios | Fission (SG governance into per-portfolio sub-committees); Role-Lift (philosophy-expert mode dispatch on SG misfire) | Composition + Agency + Operation | high INT excess (cross-portfolio SG variance); medium S-A excess (per-portfolio sub-roy SG drift) | per-client per-portfolio SG cron; aggregate ~€500-1K/mo at G3 |
| **G4 $100M** | 100 (~80% B2-equivalent; 20% B3-exploratory) | ~150+ | 500 | B3 governance bureaucracy at scale; SG predicate library fragmentation across Alliance members | Mittelstand AI Alliance SG-template parliament; per-region SG governance; B3 confined to research/exploration sub-roys; mature projects fully B2 | Role-Lift (SG governance to Alliance committee); Continuous Phase-Promotion of SG templates; Context Reframe (B3 as research-tier, B2 as production-tier) | eXternal + Composition + Agency | pervasive (mitigated by Alliance SG parliament + outcome-telemetry per philosophy-scalability §6) | per-Alliance-member SG infrastructure; aggregate ~€10-30K/mo at G4 |
| **G5 $1T** | 500+ | thousands across federation | 5000+ | per-roy SG drift; predicate-template-coherence breaks across Alliance | federated SG templates; per-Alliance-region predicate libraries; Token economy Option B (D23) for predicate-library voting; statistical convergence on SG quality | Continuous Fusion (Alliance-shared SG templates); Re-Phase-Promotion at every Alliance methodology release | eXternal + Composition + Agency + Time | pervasive (mitigated by Alliance parliament + outcome-telemetry) | per-Alliance-member sovereign SG infrastructure; Jetix-central provides predicate templates + standards |

**Antifragility verdict.** B3 is **promising at G1-G2 (morphogenetic adaptation matches early-stage exploration)**; converges to B2 at G3+ for mature projects; B3-exploratory niche persists at all gates for research/bets portfolios. **Risk**: predicate-rigor discipline lapses → B3 collapses to ad-hoc. Mitigation: philosophy-critic SG-validation gate at every SG declaration. [F: F3 / ClaimScope: B3-horizon / R: medium]

## §11 Anti-Fragility Assessment (≥400w)

**Verdict: PROMISING ANTIFRAGILE at G1-G2 (morphogenetic adaptation matches early-stage exploration); CONVERGES to B2 at G3+ for mature projects; CONDITIONAL on philosophy-critic SG-discipline.**

**Mechanism for promising antifragility G1-G2.** Per Kelly out-of-control + Kauffman adjacent-possible: B3's morphogenetic pattern allows projects to grow scaffold complexity ONLY when SGs fire — i.e., when ACTUAL momentum justifies the cost. Compare to B2's pre-allocated rich-scaffold: B2 over-invests in failing projects (scaffold cost sunk before failure-evidence accumulates). B3 economizes by deferring scaffold investment until evidence accumulates. At G1-G2 (8-15 projects, 70-90% mortality typical for early-stage bets), B3's economy compounds.

**Mechanism for convergence to B2 at G3+.** When project succeeds (multiple SGs fire including SG-4 mini-swarm), B3 becomes structurally B2-equivalent. Mature projects look like B2 projects. B3's distinctive value is in EARLY STAGES where most projects die before achieving SG-4. At G3+ portfolios, mature projects dominate; B2 default; B3 niche.

**Mechanism for conditional risk: philosophy-critic SG-discipline.** B3's antifragility depends ENTIRELY on Hamel-binary SG predicate discipline. If predicates loose or ambiguous: SG misfires; auto-spawn creates wrong scaffolds; auto-spawn churn confuses oversight; B3 collapses to ad-hoc. **Mitigation**: every SG declaration (default + custom) passes philosophy-critic gate at SG-declaration time + at first-fire (post-fire validation).

**Pressure tests.**

(1) **Predicate misfire on first 3 projects (e.g., test-data leads trigger SG-1).** `/lint --check-stage-gates` audit log shows misfire pattern; brigadier dispatches philosophy-critic for predicate refinement; auto-rollback removes mis-spawned `leads/` files; revised predicate added. **Antifragile because:** misfire SURFACES the predicate weakness; predicate library improves. B2 would never surface this signal (no auto-spawn).

(2) **Project regresses (contracts churn → SG-2 conditions no longer satisfied).** B3 does NOT auto-tear-down (asymmetric morphogenesis). Ruslan or project-brigadier explicitly de-morph via `/project-de-morph <slug>`. **Antifragile because:** asymmetry preserves audit trail (we KNOW contracts existed); de-morph is explicit choice with rationale.

(3) **Cross-project SG pattern emerges (e.g., 5 consulting projects all hit SG-3 hypothesis-refutation in first 4 weeks).** Auto-detected; surfaced in weekly digest as "consulting projects show high hypothesis-refutation rate"; methodology v(n+1) may revise consulting project_type template to add hypotheses.md at bootstrap (skipping SG-3 for new consulting projects). **Antifragile because:** cross-project signal updates methodology; B1/B2 would require manual meta-agent sweep.

(4) **Hostile predicate-injection on `_moc.md` (UC-9 attack via SG declaration).** Per UC-9 §5 B3-specific: predicate evaluation runs per-client UNIX user; cross-client read denied at OS level; predicate-injection enumeration fails. Audit log + philosophy-critic SG-validation gate catch the malicious predicate at SG-declaration time. **Antifragile because:** philosophy-critic gate is the primary defense; OS-level isolation is backup. [F: F3 / ClaimScope: B3-anti-fragility / R: medium]

## §12 Open Questions for Ruslan

1. **B3 vs B2 default per project type:** B3 for early-stage exploratory (research, bets); B2 for production (consulting, product)? Or B3 default for all and let SGs determine convergence to B2?
2. **Default SG predicates per project_type:** confirm consulting SG-1..SG-5 set per §4.2? Customize per Ruslan input.
3. **Custom SG declaration discipline:** Ruslan-only declares custom SGs OR project-brigadier may propose subject to philosophy-critic gate?
4. **Auto-spawn vs HITL-gate:** auto-spawn at SG firing (default; speed) OR HITL-gate at every SG firing (slower; predictable)?
5. **De-morph reversibility scope:** asymmetric (default; only Ruslan/brigadier explicit) OR auto-tear-down on prolonged SG-condition-violation?
6. **B3 portfolio confinement at G3+:** confine B3 to research/bets portfolios at scale OR keep B3 as default with SG-driven convergence to B2 for mature projects?

— brigadier (Phase-5 variant draft), 2026-04-24
