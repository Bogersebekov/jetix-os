---
title: Mgmt × Scalability — Layer-B 5-Gate Horizon Projection
type: horizon-projection
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
confidence_method: expert-judgment-from-integrator-drafts-and-tier1
tier: tier-1
produced_by: mgmt-scalability
sources:
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-optimizer-scaffold-deltas.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md
  - prompts/km-architecture-research-2026-04-24.md
  - .claude/agents/mgmt-expert.md
  - CLAUDE.md
related: []
binding_scope: km-architecture-mgmt-scalability-horizon
mode: scalability
---

# Mgmt × Scalability — Layer-B 5-Gate Horizon Projection

> **Cell acceptance predicate status (binary):**
> ≥3 Layer-B variants through 5 gates with project-count + agent-count + client-count + Ruslan-attention-budget per gate → YES (§§1–3).
> Named MHT events per gate → YES (§§1–3 MHT column).
> Janus INT-excess risk per gate → YES (§§1–3 Janus column).
> Federation operational complexity per gate → YES (§4).
> Sub-roy / portfolio split trigger → YES (§5).
> Cadence scaling → YES (§6).
> Lifecycle automation milestones → YES (§7).
> F-G-R per claim → YES (§8 and inline throughout).

---

## §1 Variant B1 — Layer-6 Namespaces (Jetix-Central, Single-Repo)

**Governing metaphor.** Projects as leaves of one tree. `swarm/wiki/operations/<slug>/`
is the atomic project node. All projects — internal and client-facing — coexist
inside one git repository with directory-level separation as the primary isolation
primitive. The Δ1-Δ7 deltas (mgmt-optimizer) are the upgrade stack.
[src: systems-integrator §2.1; mgmt-optimizer §1 Δ1..Δ7]

### §1.1 B1 Gate Table

| Gate | G1 | G2 | G3 | G4 | G5 |
|---|---|---|---|---|---|
| **Label** | €50K | €200K | €1M | $100M | $1T |
| **Project count** | 8 active | 15 active | 30 active | 100 active | 500+ active |
| **Agent count** | 6 (Phase A) | 10 | 25 | 100 | 200+ |
| **Client count** | 0–1 (internal + first pilot) | 3–5 | 10–15 | 50–100 | 500–5000+ |
| **Ruslan active-tasks** | ≤20 (green ratchet at 8 projects) | 15–20 (amber ratchet onset) | **>20 — Agency trigger fires** (AP-MGMT-5 escalation mandatory) | n/a — delegation model required | n/a — federated roys |
| **Physical failure** | Shared `edges.jsonl` grows to ~10K entries; grep latency p95 ~1.5s; manageable | `meta/health.md` attention-budget ratchet at amber continuously; `/project-status` sweep across 15 projects adds ~3 min latency per cycle | Single brigadier cannot route 30 concurrent project-brigadiers without context-window overflow; Q2 write bottleneck on `edges.jsonl` | Single-repo merge-conflicts at 100 simultaneous projects; UCR (unified change record) latency breaks Monday ritual | Monolithic git repo with 500+ project-subtrees becomes unmergeable; BFS over single `edges.jsonl` (>500K entries) exceeds in-memory ceiling |
| **Upgrade path** | Δ3 ratchet (meta/health.md) + Δ5 `/project-status` sweep; no new infrastructure | Project-brigadier delegation (P1-only active brigadiers; P3-P4 dormant auto-protocol via Δ3) | **Sub-roy split per §5** (consulting + infra + research sub-portfolios); delegated portfolio-brigadier per sub-roy | Fission: B1 architecture is END-OF-LIFE at this scale; migrate to B2 federated per-client holons | B2/A2 is the canonical G4-G5 model; B1 exits |
| **MHT event** | Phase Promotion (ops substrate activated) | Role-Lift (brigadier adds attention-pre-filter; auto-approves P4 dormancy) | **Fission** (single-tree splits into sub-roy portfolios) | Context Reframe (B1 → B2 migration complete) | Federated Roys (each sub-roy operates independent B2 instance) |
| **BOSC-A-T-X trigger** | C = Composition (enforcement + schema fields close; OPP-04 predicate) | A = Agency (Ruslan attention budget approaching limit; ratchet amber sustained ≥2 cycles) | **A = Agency (primary) + S = Scale** (30 projects × project-brigadier overhead breaks single-instance capacity) | B = Boundary + A = Agency (B1 boundaries insufficient; role-model broken) | X = eXternal + B = Boundary (regulatory AI-ops frameworks; multi-roy federation governance) |
| **Janus INT-excess** | LOW — single tree ensures automatic cross-project leverage (Δ7 sweep fires naturally) | MEDIUM — attention-budget amber means brigadier over-integrates (absorbs P3-P4 status without real agency) | **HIGH INT-excess risk** — single-brigadier model collapses into INT paralysis: 30 project-status rows per digest → brigadier defers everything to HITL, nothing ships. Counter: sub-roy split (§5) restores S-A assertiveness | n/a at this scale | n/a |
| **Janus S-A-excess** | LOW | LOW | MEDIUM — per §6.3 of mgmt-expert: brigadier may start prioritising own meta-work over project delivery when 30 projects compete for attention | HIGH — role proliferation without governance collapses into every-team-self-directs chaos | HIGH (multi-roy without Alliance governance) |

```
F: F3
ClaimScope: B1 holds for Phase-A solo-founder, single git repo;
  fails by construction at G3 (30 projects, Agency trigger);
  NOT valid for multi-client simultaneous deployment (UC-9 FAIL at G2+)
R: refuted if a single-brigadier instance demonstrably handles 30
   concurrent project-brigadiers at G3 with <20 Ruslan active-tasks;
   accepted if priority-reversal-rate remains <20% and Monday digest
   completes in ≤15 min through G1 and G2
```

[src: mgmt-integrator §4 B.3; mgmt-optimizer Δ3; CLAUDE.md L66 ≤20 active tasks; systems-integrator §2.1 Janus B1]

---

## §2 Variant B2 — Per-Client Per-Project Federated Holons

**Governing metaphor.** Each client engagement is an autonomous project-wiki
living inside that client's sealed holon. Clients are not siblings of Jetix-internal
projects — they live in separate filesystem trees, separate git repositories (Phase B),
with separate brigadier instantiation. Jetix-methodology scaffolds are pushed as
versioned updates via git submodule.
[src: systems-integrator §2.2; mgmt-integrator §6 UC-9 Level 1–3]

### §2.1 B2 Gate Table

| Gate | G1 | G2 | G3 | G4 | G5 |
|---|---|---|---|---|---|
| **Label** | €50K | €200K | €1M | $100M | $1T |
| **Project count** | 8 (Jetix-internal, B1-style) | 5–8 per client × 3–5 clients = 15–40 projects total | 10–15 per client × 10 clients = 100–150 total | 30 per client × 50 clients = 1500 total | 100+ per client × 5000+ clients (Alliance) |
| **Agent count** | 6 (shared; B2 not yet active) | 8–10 per client instance × 5 clients = 40–50 instances | 25 per client × 10 clients | 100 per client × 50 clients | 200+ per Alliance member |
| **Client count** | 0 (internal only; Phase A) | 3–5 (first paying clients; B2 bootstraps here) | 10–15 | 50–100 | 500–5000+ (Alliance network) |
| **Ruslan active-tasks** | ≤20 Ruslan-level (green; Jetix-internal only) | **≤20 Ruslan-level across clients** (each client has a delegated project-brigadier; Ruslan reviews cross-client summaries only; amber risk if Ruslan receives raw per-client digests instead of aggregated) | ≤20 Ruslan-level **only if** a client-lead PM handles per-client digests (Phase B PM hire trigger per §1d split_trigger); Agency trigger deferred by delegation | Portfolio PM (multi-client manager) handles sub-roys; Ruslan sees Alliance-level digest only | Ruslan → board-level governance; operational attention fully delegated |
| **Physical failure** | B2 infra not yet active; B1 operates; no failure at G1 | Per-client repo bootstrap overhead: each client requires ~1 brigadier cycle + 10–15 swarm turns; at 5 clients this is 50–75 swarm turns of onboarding per cycle if clients churn; overhead manageable | Cross-client methodology sync (git submodule updates) to 10 clients requires a scheduled push cycle; if methodology diverges >2 minor versions per client, merge conflicts appear in submodule | 50 client repos require automated CI/CD for methodology pushes; manual brigadier-mediated push breaks at ~20 clients | Alliance-level methodology versioning: 5000+ client repo subscribers; git submodule model breaks (pull latency, fork divergence, version skew) |
| **Upgrade path** | B1 remains canonical; B2 infra spec drafted (this cycle) | Per-client repo bootstrap automation (Δ1 `/project-bootstrap` extended to `--mode federated`); `holon-root.md` creation automated | Methodology push automation (scheduled git submodule update cron; brigadier dispatches push-notification to active client brigadiers) | Package registry model: Jetix-methodology as versioned npm/pypi-analog package; client holons pin a version and upgrade on schedule | Alliance federation platform: open-standard methodology spec with Alliance-member distributed hosting; EISA-model governance |
| **MHT event** | Phase Promotion (B2 spec completed; no deployment) | **Phase Promotion** (first client on B2: directory-level isolation becomes repo-level isolation; UC-9 PASS by construction) | Role-Lift (Ruslan gains per-client summary-only digest; project-brigadier handles per-client detail) | Fission (Jetix splits into Jetix-Methodology-Holon + N client deployment operations) | Context Reframe (Alliance governance replaces Jetix-central control; federated standard replaces proprietary methodology push) |
| **BOSC-A-T-X trigger** | C = Composition (spec + scaffold templates drafted) | C = Composition + A = Agency (first client deployment; federated architecture activated) | A = Agency (Ruslan cannot review 10 client digests individually; PM-hire trigger) | B = Boundary (client-holon boundaries formalised legally; GDPR compliance layer; Alliance governance structure) | X = eXternal (EU AI Act regulatory framework; Alliance legal structure; cross-national Mittelstand compliance) |
| **Janus INT-excess** | LOW (B2 not active) | **MEDIUM** — risk that per-client isolation creates knowledge silos; Ruslan may not see cross-client patterns that improve methodology. Counter: quarterly human-mediated promotion loop (mgmt-expert §6.3 R2 loop) | MEDIUM-HIGH — 10 isolated client holons each accumulating learnings without cross-client synthesis degrades methodology quality over time. Counter: quarterly Ruslan review + `local-patterns/` → `global/` HITL promotion | Resolved via Alliance methodology-pool; quarterly Alliance ceremony | Resolved via EISA-model: Alliance-member contributions anonymised and promoted to Alliance methodology base |
| **Janus S-A-excess** | LOW | LOW — per-client isolation is the design intent, not excess | LOW — each client-holon is self-assertive by design; Jetix-methodology is the shared integrative layer | LOW at client level; MEDIUM at Alliance level if Jetix-methodology team over-asserts control over Alliance members | LOW (Alliance governance prevents Jetix monopoly per EISA analogy) |

```
F: F3
ClaimScope: B2 operational at G2+ (first client); not active at G1;
  UC-9 PASS by construction at G2 (separate-repo);
  NOT valid for B1 single-repo Phase A
R: refuted if per-client repo bootstrap at G2 takes >2 brigadier cycles
   per client (then onboarding cost degrades UC-5 ≤30min);
   accepted if G2 pen-test (10 adversarial queries) returns 0 cross-client
   leakage AND methodology push delivers to all clients in <24h
```

[src: systems-integrator §2.2 B2 structure; mgmt-integrator §6 UC-9 4-layer proof; BIOS-insight §3 "client's KB = client's BIOS"; prompts §3.9 UC-9 construction requirement]

---

## §3 Variant B3 — Adaptive Scaffold (Thin-Base + Milestone-Triggered Enrichment)

**Selection rationale.** The brief names B3 as "adaptive scaffold OR PMBOK-rich;
pick one." This cell selects **Adaptive Scaffold** because PMBOK-rich is a
strict superset of B1 (PMBOK processes applied to Layer-6 namespaces), which
is already covered by B1's upgrade path. Adaptive scaffold occupies a genuinely
distinct design-space position: the scaffold starts thin (3 base files only) and
grows on observable milestone triggers, rather than pre-loading the full 5-file
(or 7-10 file) scaffold at bootstrap. This makes G1 ultra-low-cost and
differentiates from both B1 (pre-loaded 5 files) and B2 (per-client federated
full scaffold from day one).
[src: mgmt-integrator §2 axis-of-differentiation table "Adaptive alternative"]

**Governing metaphor.** Project scaffold as living cell: born minimal
(`_moc.md` + `open-questions.md` only), differentiates on signals. No wasted
structure for projects that die at `hypothesized`; full richness only for
projects that reach `active` and accumulate evidence.

### §3.1 B3 Gate Table

| Gate | G1 | G2 | G3 | G4 | G5 |
|---|---|---|---|---|---|
| **Label** | €50K | €200K | €1M | $100M | $1T |
| **Project count** | 8 (mixed: 2 active, 4 paused, 2 hypothesized) | 15 (B3's thin spawn means more hypothesized projects are created cheaply; 6 active, 9 paused/hypothesized) | 30 (10 active, 20 in various thin states) | 100+ (25 active, 75 thin/dormant) | 500+ |
| **Agent count** | 6 (Phase A) | 10 | 25 | 100 | 200+ |
| **Client count** | 0–1 | 3–5 | 10–15 | 50–100 | 500+ |
| **Ruslan active-tasks** | ≤20 green (thin spawn is cheap; hypothesized projects do NOT count toward active-tasks ratchet; only `state: active` projects count per Δ3) | ≤20 green (ratchet counts only active; thin projects buffer zone) | ≤20 Ruslan-level **maintained longer** than B1 because thin scaffold means fewer projects tip to `active` without evidence (natural backlog pressure valve) | Agency trigger deferred by adaptive model; delegation required as in B2 | Delegation model required |
| **Physical failure** | Trigger-logic for adaptive enrichment must be codified (which milestone fires which file addition); risk of inconsistent scaffold state if trigger fires partially | Trigger-logic complexity grows as project-types diversify; at 15 projects with mixed triggers, `/lint` must understand partial scaffold states | At 30 projects with 5 different trigger-points each, the trigger-state machine becomes opaque; debugging which files were created by which trigger at which milestone is non-trivial without a scaffold-manifest | At 100 projects, adaptive scaffold without a manifest-registry produces orphaned stub files and missed triggers; operational entropy accumulates | Adaptive model without a formal scaffold grammar collapses at 500+ projects; requires migration to B1 or B2 full-scaffold model |
| **Upgrade path** | Codify trigger-points in `_moc.md` as a `scaffold_triggers:` YAML field listing which milestone fires which file additions; `/project-bootstrap` creates only `_moc.md + open-questions.md`; trigger manifest embedded in frontmatter | Introduce a `scaffold-manifest.md` per project (created at first trigger fire); records which files were created by which trigger with timestamps; `/lint` validates manifest vs actual files | Introduce a scaffold-linter mode that validates trigger-state consistency across 30 projects; brigadier runs `/lint --mode scaffold` at cycle-close | Migrate active (evidence-rich) projects to B1 or B2 full scaffold; retain adaptive model only for hypothesized pipeline | Adaptive model is a Phase-A / early Phase-B pattern only; G4+ operates B1 or B2 exclusively |
| **MHT event** | Phase Promotion (adaptive scaffold spec drafted; no deployment difference from B1 at G1) | Role-Lift (trigger-logic codified in frontmatter; scaffold-manifest introduced) | **Fission** (active projects migrate to B1 or B2 based on UC-9 need; adaptive model retained for hypothesized pipeline only) | Context Reframe (adaptive model retired; canonical B1/B2 handles all) | n/a |
| **BOSC-A-T-X trigger** | C = Composition (spec drafted; minimal new schema fields) | C = Composition (scaffold-manifest added) | S = Scale + B = Boundary (trigger-state complexity exceeds debugging capacity; boundary of adaptive model reached) | B = Boundary (end of adaptive model; full-scaffold canonical) | n/a |
| **Janus INT-excess** | LOW — minimal scaffold means less to integrate; fewer premature cross-project edges; cleaner knowledge state | LOW-MEDIUM — trigger fires on milestone; risk that triggers are too conservative (INT excess: project never gets rich scaffold because milestones are not reached) | MEDIUM — projects stuck at thin scaffold create a false sense of "many active projects" when they are actually hypothesized with no evidence | HIGH INT-excess: at 30 projects, many thin-scaffold hypothesized projects are effectively zombie projects consuming Ruslan-attention-budget space | n/a (model retired) |
| **Janus S-A-excess** | LOW | LOW | LOW-MEDIUM — trigger-based enrichment can be over-asserted (fire too many triggers too early → degrades to B1 with extra complexity) | HIGH S-A-excess: each trigger fires its own scaffold additions independently, producing fragmented project structures | n/a |

```
F: F3
ClaimScope: B3 provides genuine value at G1 (ultra-cheap project creation);
  degrades at G3 due to trigger-state complexity;
  NOT valid beyond G3 as a primary model; hybrid role (hypothesized-pipeline
  feeder) valid through G4
R: refuted if trigger-logic complexity at G2 exceeds the maintenance
   overhead of the B1 full-scaffold model (then B3 cost-advantage disappears);
   accepted if ≥50% of hypothesized projects are tombstoned before
   ever receiving full scaffold (validates thin-base value proposition)
```

[src: mgmt-integrator §2 axis-of-differentiation "Adaptive alternative"; mgmt-optimizer Δ1 (B3 is the minimal-delta version); prompts §3.8 UC-8 G1-G3 physical failure rows]

---

## §4 Mittelstand AI Alliance Federation Operational Complexity Per Gate

Per BIOS-insight §3 and systems-integrator §8: the Mittelstand AI Alliance is the
EISA-consortium analog — open methodology standard, per-member private implementation,
no cross-member data flow. This section traces the per-gate PM operational complexity
of running the federated model.

[src: BIOS-insight §3 "Jetix methodology = EISA consortium"; systems-integrator §8 BIOS/EISA parallel; prompts §3.8 UC-8 client-count scale]

### §4.1 Federation PM complexity per gate

**G1 (€50K — 0–1 clients, pre-Alliance).**

Operational complexity: **LOW**. No federation exists. Jetix-internal only.
PM actions: maintain Δ3 ratchet; run `/project-status` weekly; close G1
cycle deliverables. Federation overhead: zero. BIOS parallel: IBM 1981
— no clone makers yet; product exists but ecosystem is pre-formation.

```
F: F3 | ClaimScope: G1 Phase-A solo-founder | R: low
```

**G2 (€200K — 3–5 clients, Alliance embryonic).**

Operational complexity: **MEDIUM**. Each client gets a separate git repo
bootstrap (B2 model activates). PM actions per client: `/project-bootstrap --mode federated`
for each client; `holon-root.md` creation; methodology submodule pin;
`granularity: client:<slug>` enforcement in `edges.jsonl`. Cross-client
PM overhead: Ruslan reviews quarterly cross-client pattern promotions.
Methodology-push cadence: monthly methodology update pushed to 3–5 client
repos (git submodule update; manual per-client ack). BIOS parallel: Compaq
1982 — first clone; IBM's architecture now has external implementors; Phoenix
prepares licensable BIOS (pre-Alliance phase).

Per-client PM artefacts created at G2:
- `client-A/swarm/wiki/foundations/holon-root.md` (holon identity)
- `client-A/swarm/wiki/meta/health.md` (per-client attention budget)
- Methodology submodule pinned to Jetix-methodology v1.x
- `offline-inference-spec.md` per consulting project (UC-10 PM artefact)
- Quarterly review ceremony: Ruslan reviews `client-A/swarm/wiki/local-patterns/` → promotes to `global/` via HITL

```
F: F3 | ClaimScope: G2 3–5 client federated deployment | R: medium
```
[src: mgmt-integrator §4 B.1 onboarding; BIOS-insight §6 "missing: client-isolation mechanics"; systems-integrator §4.2 Layer 1 isolation]

**G3 (€1M — 10–15 clients, Alliance forming).**

Operational complexity: **HIGH**. PM must coordinate:
- 10–15 client repos × monthly methodology push = 10–15 pushes/month
- Per-client health digest aggregation (Ruslan cannot read 10 raw digests; requires a PM lead)
- Cross-client pattern promotion ceremonies: quarterly × 10 clients = 40 reviews/year
- Agency trigger: **Ruslan ≤20 active tasks cap fires** (CLAUDE.md L66) if Ruslan receives raw per-client updates instead of aggregated portfolio digest
- PM hire trigger: per §1d split_trigger row 1, this is the gate where a human PM lead is required (Phase-B PM hire)
- Alliance legal structure initiated (Mittelstand AI Alliance legal entity; Linux Foundation / ARM Holdings analog per BIOS-insight §9 Q3)

Counter-mechanism: per-client brigadier instances produce a `client-portfolio-summary.md`
aggregated by a portfolio-brigadier. Ruslan reads one summary per 10 clients per week
(≤3 minutes per summary per Monday ritual). PM lead manages per-client brigadiers directly.

BIOS parallel: Phoenix Technologies 1984 — first licensable BIOS; multiple
licensees now; Phoenix's PM must coordinate per-client implementations while
maintaining the shared standard.

```
F: F3 | ClaimScope: G3 10–15 clients; PM hire mandatory | R: medium
```
[src: mgmt-expert §6.1 horizon gate €1M; BIOS-insight §3 "Phoenix BIOS → Mittelstand LLM path"; systems-integrator §5.2 R2 feedback loop]

**G4 ($100M — 50–100 clients, Alliance operational).**

Operational complexity: **VERY HIGH → systematized via Alliance platform**.
Individual PM management of 50+ client repos is impossible without Alliance
tooling. Required PM infrastructure:

- Methodology push automation: CI/CD pipeline for methodology updates (not manual git submodule)
- Alliance-level health dashboard: aggregate per-client health signals into an Alliance-wide anonymised dashboard
- Sub-roy PM structure: Jetix splits into methodology-team + deployment-teams per industry vertical (DACH manufacturing / DACH professional services / DACH logistics)
- Compliance layer PM: GDPR, EU AI Act, BSI C5 audit-trail management per client (per BIOS-insight §7 "compliance certification path")
- Alliance governance: standardised Alliance methodology version numbering (semver); member-voting on standard updates; analogous to EISA consortium governance per systems-integrator §8

Ruslan PM role at G4: board-level governance only. Per-client PM delegated to industry-vertical PM leads.

```
F: F3 | ClaimScope: G4 50–100 clients; requires Alliance legal entity and
  CI/CD methodology push automation; PMO-level function | R: low
  (highly speculative; no G4 comparable deployed)
```

**G5 ($1T — 500+ clients, Alliance mature).**

Operational complexity: **SYSTEMATIZED** (complexity absorbed by Alliance platform and governance).
PM actions at G5 are governance-level only: Alliance methodology standard update cycles (quarterly);
member dispute resolution; sub-standard versioning for industry verticals; open-source methodology
components per D24 Lock 24. Jetix-central PM function: Jetix-Methodology-Holon stewardship.
BIOS parallel: ARM Holdings — ARM doesn't manufacture chips; it maintains the architecture
specification and licenses it; 750+ licensees manage their own implementations.

```
F: F2 | ClaimScope: G5 extremely speculative; structural analogy only | R: low
```
[src: BIOS-insight §8 "7 конкретных recommendations"; systems-integrator §8 EISA federation; prompts §3.8 UC-8 G5 multi-roy distributed wiki]

---

## §5 Sub-Roy / Per-Portfolio Split Trigger

### §5.1 When does the split occur?

**Primary trigger (Agency): G3 (30 projects / ≥10 clients).**

The CLAUDE.md L66 ≤20 active-tasks cap is the hardcoded Ruslan-attention-budget
rule. At G3 with 30 projects total across 10 clients, even with B2 per-client
brigadiers aggregating per-client digests, Ruslan's attention budget as the
single decision-maker on ALL priority changes, ALL state transitions, and ALL
cross-client pattern promotions exceeds 20 active tasks. This is the Agency
trigger (A = Agency, BOSC-A-T-X) that mandates structural delegation.
[src: CLAUDE.md L66; mgmt-expert §6.1 horizon gate €1M; mgmt-optimizer §5 ratchet check logic]

**Secondary trigger (Scale): consistent priority-reversal-rate ≥20% sustained ≥2 months.**

If the priority-reversal-rate KPI (per AP-MGMT-5 + mgmt-expert §1d escalation-trigger row 1)
breaches 20% for 2 consecutive months across the portfolio, this signals that a single
orchestrator cannot maintain coherent prioritization across 30 projects. This is both
an Agency and Scale trigger (A + S in BOSC-A-T-X). [src: mgmt-expert §1d escalation-trigger]

### §5.2 Split structure

At G3, the recommended sub-roy split is:

**Sub-roy A: Consulting (Quick-Money motion — P1 projects, client-facing)**
- Scope: all client-facing consulting projects under B2 federated holons
- PM lead: first PM hire (Phase-B PM hire per §1d split_trigger)
- Brigadier: consulting-portfolio-brigadier (per-client brigadier instances + aggregator)
- Cadence: weekly per-client digest → Monday consulting-portfolio summary for Ruslan

**Sub-roy B: Infra + Methodology (Jetix-Methodology-Holon stewardship)**
- Scope: Jetix-internal infrastructure, wiki architecture, swarm operations, methodology update cycles
- PM lead: Ruslan-direct (retained at G3; smaller scope post-split)
- Brigadier: canonical brigadier (unchanged role)
- Cadence: bi-weekly methodology update cycle; quarterly methodology push to all clients

**Sub-roy C: Research + Community (P2-P3 projects, brand + community + engineering-thinking)**
- Scope: internal research directions, brand, community (per CLAUDE.md 8-project roster P2-P3 projects)
- PM lead: Phase-B community-PM hire (optional at G3; mandatory at G4)
- Brigadier: research-portfolio-brigadier
- Cadence: monthly review sufficient; no client-facing deliverables

**Lock-21 check.** Per D21 Matchmaker + Roy-Replication, this sub-roy split mirrors
the "Roy-replication" concept: each sub-roy is a scaled-down version of the full
Jetix swarm operating on a bounded portfolio. This is the intended Phase-B scaling
pattern.

```
F: F3
ClaimScope: G3 split is well-motivated by Agency trigger; sub-roy structure
  is a design proposal, not an observed pattern (no G3 analogue exists yet)
R: refuted if Agency trigger at G3 can be resolved by attention-budget
   tooling (e.g., a portfolio-brigadier aggregator at G2 is sufficient
   through G3 without formal sub-roy split);
   accepted if ≥3 consecutive months at G3 see ratchet: amber sustained
   AND Ruslan explicitly requests delegation
```

[src: mgmt-expert §6.1 horizon gate €1M MHT event "Fission"; CLAUDE.md L66; BIOS-insight §8 recommendation 3 "Mittelstand AI Alliance = EISA moment"]

---

## §6 Cadence Scaling — Weekly Digest Mechanics Per Gate

The weekly Monday digest (JETIX-ARCHITECTURE-BRIEF §4.7 Monday ritual) is the
PM's primary signal-to-Ruslan mechanism. Mechanics differ materially across gates.
[src: mgmt-integrator §4 B.5 cadence; mgmt-optimizer Δ5; systems-integrator §5.4 B2 attention-budget loop]

### §6.1 G1 (8 projects) — Direct Monday sweep

**Mechanics:** `/project-status` skill reads all 8 `_moc.md` files; aggregates
traffic-light rows into `meta/health.md`; produces per-project
`{state, p_level, last_commit_date, open_questions_count, ratchet_status}`.
Ruslan reads in ≤3 minutes Monday morning. No intermediate layer.

**Format:** single `meta/health.md` with 8 traffic-light rows + 1 attention_budget stanza.

**Ruslan load:** ≤3 min read + ≤15 min HITL acks (state transitions, open AWAITING-APPROVALs).

**Risk:** none at this scale. The digest is trivially readable.

```
F: F3 | ClaimScope: G1 8-project set | R: medium
```

### §6.2 G2 (15 Jetix projects + 3–5 client projects = 18–20 total) — Aggregated with client separation

**Mechanics:** Two `/project-status` sweeps: one over `operations/` (Jetix-internal),
one per client over `client-<slug>/swarm/wiki/operations/`. Results aggregated into:
- `meta/health.md` (Jetix-internal section — unchanged format)
- `meta/client-health-summary.md` (NEW at G2: one row per client with aggregate status)

Ruslan reads `meta/health.md` + `meta/client-health-summary.md` combined = ≤5 min.

**Format change from G1:** addition of `meta/client-health-summary.md`; Jetix-internal
unchanged. This is additive (LOC invariant preserved).

**Ruslan load:** ≤5 min read + ≤20 min HITL acks (more clients = more state transitions per week).

```
F: F3 | ClaimScope: G2 18–20 total projects; 3–5 clients | R: medium
```

### §6.3 G3 (30 Jetix+client projects, Agency trigger) — Portfolio-brigadier aggregation layer

**CRITICAL CHANGE: Ruslan cannot read 30 raw traffic-light rows.**

**Mechanics:** Sub-roy portfolio-brigadiers (§5) produce per-sub-roy digests:
- Consulting-portfolio-brigadier → `meta/consulting-portfolio-digest.md` (≤3 key items, colour-coded)
- Research-portfolio-brigadier → `meta/research-portfolio-digest.md` (≤3 key items)
- Infra-portfolio-brigadier → `meta/infra-portfolio-digest.md` (≤3 key items)

A "portfolio-overview-brigadier" (or canonical brigadier in aggregator mode) reads
all 3 sub-digests and produces `meta/weekly-overview.md` — a single ≤10-row summary
for Ruslan. Each row: `sub-roy | red/amber/green | top-1 action-needed | 1 open gate`.

Ruslan reads `meta/weekly-overview.md` in ≤3 minutes. Drills into sub-digests only
when a sub-roy is red. Decision latency target: ≤15 minutes Monday total.

**Format change from G2:** two-tier digest structure. Per-sub-roy detailed digest +
aggregated overview. Raw per-project traffic-light rows are NOT surfaced to Ruslan
at G3 except on drill-down. This is the Grove leverage principle: Ruslan operates
at the highest-leverage layer (sub-roy red/amber/green), not at the
per-project-commit-date layer.
[src: mgmt-expert §2.3 "Grove leverage / output (HOM)"; mgmt-expert §9.3 HITL responsibilities]

```
F: F3 | ClaimScope: G3 30 projects, sub-roy structure activated | R: medium
```

### §6.4 G4–G5 ($100M–$1T) — Alliance dashboard

At G4–G5, per-project digests are entirely delegated. Ruslan (or CEO-equivalent)
sees only:
- Alliance-level health: red/amber/green aggregate across 50–500 clients
- Regulatory flags: any compliance events surfaced immediately
- Strategic pattern promotions: cross-client anonymised methodology improvements pending Alliance vote

The Monday ritual becomes a board-level governance cadence (quarterly rather than
weekly for Ruslan-equivalent; weekly for PM leads). This is the expected evolution
per mgmt-expert §9.4 `cycle_200` expectation.

```
F: F2 | ClaimScope: G4-G5 highly speculative | R: low
```

---

## §7 Lifecycle Automation Milestones

The current state (G1 baseline) has a manual project-pause/kill workflow: Ruslan
identifies a dormant project, acks the state transition, project-brigadier writes
the `decisions-log.md` entry. At G3+ this manual workflow becomes intractable.

[src: mgmt-integrator §4 B.7 lifecycle; mgmt-optimizer Δ2 BASB CODE + state machine; systems-integrator §5.4 B2 attention-budget balancing loop]

### §7.1 G1 — Fully manual (acceptable at 8 projects)

All state transitions require Ruslan HITL ack. No automation. The Δ3 ratchet
(`meta/health.md` `ratchet_status`) surfaces candidates; Ruslan decides.
**Lifecycle automation milestone: NONE.** Status quo is sufficient.

Acceptance predicate: "Every project-state transition in `decisions-log.md` has
a `HITL-acked: yes` entry with Ruslan's ack date."

### §7.2 G2 — Auto-proposal for P3-P4 dormant projects

At G2 (15–20 projects), the `/project-status` sweep automatically identifies
P3-P4 projects with `state: active` AND `last_commit_date > 30 days`. For these,
brigadier automatically:
1. Drafts a `AWAITING-APPROVAL-<slug>-dormancy-<date>.md` gate file
2. Proposes `state: active → paused` with tombstone-candidate flag if >60 days
3. Includes one-sentence rationale (from `open_questions_count` trend + commit history)

Ruslan acks within Monday digest review. Auto-proposal reduces Ruslan's effort from
"manually identifying dormant projects" to "reviewing pre-staged ack packets."

**Lifecycle automation milestone G2: Auto-proposal for P3-P4 dormancy.**

Acceptance predicate: "Any project with P3-P4 priority AND `last_commit_date > 30 days`
automatically receives a AWAITING-APPROVAL dormancy packet within the next `/project-status`
cycle; zero such projects remain in `state: active` without a pending dormancy gate."

```
F: F3 | ClaimScope: G2 15–20 projects, P-level taxonomy in place | R: medium
```

### §7.3 G3 — Auto-tombstone proposal + pattern extraction automation

At G3 (30 projects), manual tombstone protocol (4-step: consolidate sweep → state set →
edge tagging → lint suppression) is intractable across 30 concurrent projects.

**Automation required:**
1. **Auto-tombstone proposal trigger:** project with `state: paused` AND `last_commit_date > 90 days`
   AND `open_questions_count = 0` (all questions resolved or closed) automatically receives
   a tombstone proposal packet. Brigadier drafts; Ruslan acks (HITL mandatory per §1d).

2. **Auto-pattern extraction at tombstone:** on Ruslan's tombstone ack, the project-brigadier
   automatically runs `/consolidate --scope operations/<slug>/open-questions.md` and produces
   a pattern-extraction report. Any pattern appearing in ≥3 projects is auto-promoted to
   `global/compound-rules/` (Δ7 mechanism), removing the manual meta-agent sweep requirement.

3. **Scheduled sweep:** meta-agent runs weekly `/consolidate --scope operations/` at G3+ (not
   ad-hoc). The sweep is a cron-analog (Compound step of canonical brigadier's weekly cycle).

**Lifecycle automation milestone G3: Auto-tombstone proposal + scheduled pattern extraction.**

Acceptance predicate: "At G3, no project remains in `state: paused` for >90 days without a
pending tombstone gate; meta-agent weekly sweep fires every cycle; ≥1 pattern promoted to
`global/compound-rules/` per 10 tombstoned projects."

```
F: F3 | ClaimScope: G3 30 projects; requires meta-agent sweep operational | R: medium
```

### §7.4 G4-G5 — Full lifecycle automation with compliance audit trail

At G4 ($100M / 50+ clients), lifecycle automation includes:
- Per-client lifecycle automation instances (each client's brigadier runs its own lifecycle
  automation per the Jetix methodology standard)
- Compliance audit trail per lifecycle event (GDPR-compatible; every state transition logged
  with timestamp, actor, ack reference; BSI C5 alignment)
- Alliance-level dormancy governance: Alliance methodology specifies the standard dormancy
  thresholds; each member implementation may tune within ±20%

**Lifecycle automation milestone G4: Alliance-compliant automated lifecycle with full
audit trail per client.**

```
F: F2 | ClaimScope: G4-G5 speculative; analogy from enterprise PM systems | R: low
```

---

## §8 Provenance + F-G-R

### §8.1 Cross-claim F-G-R summary

| Claim | F | ClaimScope | R |
|---|---|---|---|
| B1 Agency trigger fires at G3 (30 projects) | F3 | Phase-A → G3 B1 single-repo model | medium; refuted if portfolio-brigadier aggregator extends B1 beyond G3 |
| B2 UC-9 PASS by construction at G2 (separate-repo) | F4 | G2+ per-client separate-repo Phase B | medium; refuted by pen-test showing cross-client leakage |
| B3 degrades at G3 due to trigger-state complexity | F3 | B3 adaptive model; G3 scale | medium; refuted if trigger-manifest adequately tracks scaffold state |
| Ruslan ≤20 active-tasks cap is the Agency trigger parameter | F5 | CLAUDE.md L66 — hardcoded rule, not heuristic | high; refuted only if CLAUDE.md L66 is revised |
| Sub-roy split (consulting + infra + research) at G3 | F3 | G3 design proposal; not observed | medium; refuted if portfolio-brigadier aggregation satisfies G3 without formal split |
| Weekly digest two-tier structure required at G3 | F3 | G3 30 projects; Grove leverage principle | medium; refuted if Ruslan can process 30 rows in ≤5 min (observational test) |
| Auto-tombstone proposal reduces Ruslan load at G3 | F3 | G3 automation proposal; operational | medium; refuted if tombstone-ack latency with auto-proposal is longer than manual identification |
| Alliance federation PM complexity requires PM-hire at G3 | F3 | G3 10 clients, federated model | medium; refuted if per-client brigadier aggregation keeps Ruslan load under cap without hire |
| BIOS-Mittelstand AI Alliance EISA analogy at G4 | F3 | Structural analogy; no Jetix-G4 precedent | low; historical parallel is strong but application to G4 is extrapolation |
| G4-G5 cadence becomes quarterly board-level | F2 | G4-G5 extremely speculative | low |

### §8.2 Tier-1 source citations (≥3×)

**Citation 1** [src: decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §3]:
"Client's KB = client's BIOS — у каждого свой, несравним, не копируется."
Used in: §2 B2 governing metaphor; §4 G2 federation mechanics; §8.1 B2 claim.

**Citation 2** [src: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md §2.2]:
B2 per-client per-project holon structure with `local-patterns/` replacing
`global/` in client holons, and methodology submodule as read-only pull.
Used in: §2 B2 gate table; §4 G2-G3 federation mechanics; §5.2 sub-roy structure.

**Citation 3** [src: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-optimizer-scaffold-deltas.md §5]:
Attention budget ratchet logic: green ≤16 / amber 17–20 / red >20; `/project-status`
sweep computes counter from `state: active` count.
Used in: §1.1 B1 Ruslan active-tasks column; §3.1 B3 Ruslan active-tasks; §5.1 Agency trigger; §6.3 G3 digest.

**Citation 4** [src: swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md §4 B.3]:
Mini-swarm allocation: named project-brigadier + ≤2 allocated experts per active project;
P3-P4 projects share canonical brigadier or go dormant.
Used in: §1.1 B1 agent count; §2.1 B2 agent count; §6.3 G3 portfolio-brigadier.

**Citation 5** [src: CLAUDE.md L66]:
"Manager attention budget: max 20 active tasks." Hardcoded rule.
Used in: §1.1 B1 Ruslan active-tasks (Agency trigger flag); §5.1 primary split trigger; §6.3 G3 mechanics.

**Citation 6** [src: prompts/km-architecture-research-2026-04-24.md §3.8 UC-8 gate table]:
G1-G5 gate parameters (revenue / wiki-page floor / project count / agent count / failure type).
Used in: §1-§3 gate tables (project count + agent count columns calibrated against prompts §3.8).

**Citation 7** [src: decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md Part 6 §6.2.3]:
BOSC-A-T-X trigger taxonomy and split_trigger conditions for brigadier
(sustained intake >10/week; 2+ concurrent cycles; accountability items >7).
Used in: §1.1-§3.1 BOSC-A-T-X trigger column.

### §8.3 Tier-4 procurement gaps

No Tier-4 books were read in this Phase-A pass. The following framework authors are
operated from Phase-A canonical source summaries only (mgmt-expert §2.0):

- **Grove HOM** — leverage principle applied in §6.3 cadence scaling (G3); operated from RESULT-07 + MS §5.2.3 summary.
- **PMBOK 7th Edition** — lifecycle state machine (hypothesized/active/paused/pivoted/tombstoned) per §7.1-§7.4; operated from mgmt-integrator process-group summaries.
- **Drucker Effective Executive** — contribution-not-effort framing in §6.3 digest design; gap flagged per mgmt-expert §2.1.
- **Cagan Empowered** — problem-over-solution enforcement (`problem_statement:` in `_moc.md`); operated from mgmt-integrator B.1 section.

### §8.4 Antifragility check (per mgmt-expert §6.5)

**B1 antifragility at 10× scale (G1 → G3):** B1 templates at 10× backlog (8 → 80 active projects)
require structural refactor beyond 30% — specifically: the single-repo model and single-brigadier
model break. B1 is **robust but not antifragile**; it survives G1-G2, degrades at G3.
Required refactor: sub-roy split = new portfolio-brigadier roles (>30% structural change). **FRAGILE at 10× beyond G2.**

**B2 antifragility at 10× scale (G2 → G4):** B2 templates at 10× client count (5 → 50 clients)
require ≤30% refactor — the per-client repo structure, `holon-root.md`, and methodology
submodule model are stable across the range. The primary change is methodology-push
automation (CI/CD), which is an infrastructure addition, not a structural schema change.
B2 is **antifragile within its design domain**: each new client adds a holon instance
that follows the same template with zero template modification. **ANTIFRAGILE up to G4.**

**B3 antifragility at 10× scale:** B3 at 10× degrades — trigger-state complexity does not
simplify at scale. **FRAGILE beyond G2.** Recommended role: hypothesized-pipeline feeder
only; hand off active projects to B1 or B2.

```
F: F3
ClaimScope: antifragility assessment based on structural analysis of template
  schema change requirements; no empirical G2-G4 data exists for Jetix
R: refuted if B1 sub-roy split requires <30% template changes (then B1
   is antifragile at 10×, contradicting this assessment);
   accepted if B2 10× client increase requires only methodology-push
   CI/CD addition with ≤2 schema fields changed
```

---

*End of mgmt × scalability draft. Produced by mgmt-expert, mode: scalability.
Task: T-km-architecture-research-2026-04-24. Cycle: cyc-km-architecture-2026-04-24.
Awaiting brigadier integration and Stage-Gated HITL review.*
