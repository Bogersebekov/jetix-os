---
title: "Part F prep — 5-Gate Horizon Projection: KM MVP Substrate (post-ack Option B)"
type: systems-scalability-record
task_id: T-km-materialization-mvp-2026-04-24
cycle_id: cyc-km-materialization-mvp-2026-04-24
produced_by: systems-expert
promoted_by: brigadier
promoted_at: 2026-04-24
mode: scalability
wave: 4
part: F-prep
created: 2026-04-24
last_modified: 2026-04-24
pipeline: accepted
state: accepted
confidence: high
confidence_method: gate-decomposition
tier: core
antifragility_check: fail-G3-fragile-conditional-G4-antifragile
promotion_note: |
  Wave-4 gate passed 2026-04-24. 5-horizon projection against post-ack
  Option B parameters (€30K contracts + €35K hourly = €65K Q1+Q2 reality-check;
  two-checkpoint kill; tier_1_phase_1 archetype filter; levenchuk minimum kpi).
  Dominant finding: G3→G4 FRAGILE gate (~40% structural change); G3 pre-investment
  in A2 substrate at G2-first-paying-client onset is mandatory for G4 antifragility.
  Governance-before-infrastructure rule: G5 owned compute requires G4 Alliance
  governance as precondition. 10/10 acceptance greps pass (121 token hits).
sources:
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "§§3-11"}
  - {path: "decisions/JETIX-PLAN.md", range: "§§3.1-3.1.1"}
  - {path: "decisions/JETIX-VISION.md", range: "§§1-4 + §8"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§§3-7"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md", range: "full"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md", range: "full"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partC-stage-gates-merged.md", range: "full"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md", range: "full"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partE-quick-money-levenchuk-bootstrap.md", range: "full"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partE-investor-critic-icp-kpi-realism.md", range: "§§1-3"}
  - {path: "swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md", range: "§§3-5"}
  - {path: "swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24-ack.md", range: "full"}
related: []
binding_scope: task-T-km-materialization-mvp-2026-04-24-partF-scalability
granularity: jetix-internal
acceptance_predicate: |
  count(gates with BOSC-A-T-X) == 5
  AND count(gates with Janus degraded-mode spec) == 5
  AND count(gates with MHT event) == 5
  AND count(gates with migration trigger binary predicate) == 5
  AND body contains "two-checkpoint"
  AND body contains "233"
  AND body contains "tier_1_phase_1"
  AND body contains "A1↔B1" AND body contains "A2↔B2" AND body contains "A3↔B2"
  AND body contains "Self-Assertive" AND body contains "Integrative"
---

# Part F prep — 5-Gate Horizon Projection: KM MVP Substrate

**Mode: scalability.** Post-ack Option B. This artefact projects the KM MVP
substrate (A1↔B1 → A2↔B2 → A3↔B2 migration trajectory per §11 of
KM-ARCHITECTURE-VARIANTS-2026-04-24.md) through 5 horizon gates. Every gate
receives a full BOSC-A-T-X decomposition, MHT event, Janus degraded-mode spec
with binary recovery predicates, migration trigger binary predicate, skip-gate
failure mode, and a revised-parameter reality-check against Option B parameters
(€30K contracts + €35K hourly = €65K Q1+Q2 per CC-1; 2 contracts/quarter; 233
hourly hours; two-checkpoint kill per CC-4; tier_1_phase_1 = [Предприниматели,
Блогеры] per CC-3; A2↔B2 mandatory at first paying client per §12 Dissent-1
resolution).

Anti-scope: no re-arbitration of CC-1/3/4/5; no new SG predicates; no new
project types; no implementation detail; no provider API-key references.

---

## §G1 G1 €50K Q2 2026

**Substrate pairing: A1↔B1** — Karpathy++ filesystem-native KM + Layer-6
thin-namespace project-mgmt. Phase-A committed absolute date (D9/D15). This is
the Phase-1 finish line: Ruslan solo, 2 contracts/quarter, 233 hourly hours at
€150/hr across Q1+Q2, tier_1_phase_1 = [Предприниматели, Блогеры] active, two-checkpoint
kill discipline engaged.

### BOSC-A-T-X triggers

- **B (Boundary shift):** The system's boundary expands from Jetix-internal-only
  (wiki as personal knowledge store for Ruslan) to Jetix-client-external (wiki
  substrate serves as the backend for 1-3 paying client engagements). The boundary
  change is: "client-facing methodology artefacts" cross the boundary for the
  first time. The A1 defense-in-depth STACK (env-var WIKI_ROOT_CLIENT_ID +
  directory namespace + frontmatter granularity:client:<slug>) becomes active at
  this boundary. Without this boundary shift, A1 is Jetix-internal research tool
  only.
- **O (Observable):** `swarm/wiki/operations/quick-money/_moc.md:cumulative_revenue_q2_2026_eur`
  >= 50000 AND `swarm/wiki/operations/quick-money/_moc.md:hourly_consulting_hours_q1_q2_2026`
  >= 150 (ramp signal) by 2026-06-30. Secondary observable: wiki page count
  `count(swarm/wiki/**/*.md)` >= 500 (enough artefact accumulation to demonstrate
  methodology-as-code to first clients).
- **S (Substrate):** A1 operational: `/ingest`, `/ask`, `/lint`, `/build-graph`,
  `/consolidate` skills live; edges.jsonl seeded; wiki-roots.yaml configured;
  OFFLINE_MODE=1 path tested. B1 operational: `/project-bootstrap`, 5-file
  scaffold, meta-agent weekly digest. Stage-gate DSL evaluator (`tools/stage-gate-eval.py`)
  live with 18-banned-phrase validator. company-as-code skills (`/company-status`,
  `/knowledge-diff`) live. All per Parts A/B/C/D design records.
- **C (Constraint removed/imposed):** REMOVED: the "no client isolation" constraint
  (all prior knowledge was Jetix-internal; first client removes this). IMPOSED: the
  ≤20 active tasks ratchet on brigadier (B1 single-brigadier constraint); the
  two-checkpoint kill predicate (week-7: <5 sales calls → pivot outreach; week-13:
  0 contracts + <10 pipeline → kill), which is a hard falsifiability constraint on
  Phase-1 Quick-Money hypothesis.
- **A (Agents):** ACTIVATES: project-brigadier instance for quick-money P1 project
  (consulting type); mini-swarm-of-3 for first paying client engagement (project-brigadier
  + mgmt-expert + domain-expert). DEACTIVATES: none (this is G1 onset). EVOLVES:
  Ruslan shifts from "Ruslan builds the tool" to "Ruslan uses the tool for client
  delivery" — the swarm transitions from meta-construction to operational delivery.
- **T (Trajectory):** From G1, the system points toward G2 (€200K validation gate,
  first paying client steady-state, A2↔B2 substrate prep). The G1→G2 trajectory is
  NOT automatic: it requires ≥1 signed client contract that triggers Phase-B substrate
  preparation within 2 weeks of signing. The trajectory vector is: methodology-proof
  (we proved it internally) → client-proof (we proved it for a paying client).
- **X (External trigger):** The BIOS-moment window: 35,000+ AI consulting shops with
  90%+ year-one mortality (STRATEGIC-INSIGHT §0) constitute the external landscape
  that makes the €50K gate meaningful. The external trigger that FIRES G1 is not a
  specific competitor event — it is Ruslan's own Q2 2026 deadline as the sole committed
  absolute date in the plan (D9/D15). The external signal to WATCH: Mittelstand buyers
  activating ("DACH German-opening" pattern per §9.1 read-trace) — early signal G1→G2
  is viable.

### MHT events at G1

- **Maturity signal:** `swarm/wiki/operations/quick-money/_moc.md:stage_gates.SG-1:fired`
  = true AND contracts_per_quarter >= 2 in Q1 2026 (first milestone) OR cumulative
  revenue >= €50K by 2026-06-30.
- **Hazard signal:** The two-checkpoint kill (CC-4) fires NEGATIVE: week-7 shows <5 sales
  calls made → outreach pivot required immediately. If week-13 shows 0 signed contracts +
  <10 pipeline contacts → kill predicate fires → G1 FAILS. Secondary hazard: `hourly_consulting_hours_q1_q2_2026`
  tracker is NOT being filled in (i.e., Ruslan is not tracking actual hourly hours logged
  against the 233-hour target) → arithmetic gap stays invisible until too late.
- **Transition mechanism:** G1 completes when cumulative_revenue_q2_2026_eur >= 50000 is
  confirmed AND at least 1 signed client contract exists (which triggers the A2↔B2 prep
  cycle). The transition is: brigadier opens a Phase-B substrate preparation task
  (A2 federated peer-holons template authoring + B2 rich mini-swarm per-client provisioning
  automation); this task runs in parallel with ongoing G1 delivery — NOT sequentially.

### Janus degraded-mode spec

**Self-Assertive excess (centralization pathology — brigadier overload):**
- Symptom pattern: brigadier is dispatched for every small artefact (single-page
  `/ingest` calls, individual note classification, trivial project status updates).
  The ≤20 active tasks ratchet is hit by meta-tasks, leaving zero capacity for
  actual client-delivery tasks. Observable: `meta/health.md:active_tasks_brigadier`
  >= 18 sustained for 3 consecutive weeks with zero client-facing artefacts shipped.
- Binary recovery predicate: `count(swarm/wiki/operations/quick-money/history.md:client-delivery)
  >= 2 per 7-day window` => brigadier load rebalanced to client-delivery.
- Escalation trigger: if `active_tasks_brigadier >= 20` for 5 consecutive days → HITL
  via brigadier (load-balancing packet); Ruslan must prune or batch tasks manually.

**Integrative excess (deference pathology — tool-first, no delivery):**
- Symptom pattern: Ruslan spends G1 window perfecting wiki substrate (refining skill
  configs, adding edge types, running lint cycles) instead of closing contracts and
  logging hourly hours. Observable: `hourly_consulting_hours_q1_q2_2026` < 50 by
  week 7 while wiki page count is growing rapidly (> 200 new pages in week 7).
- Binary recovery predicate: `swarm/wiki/operations/quick-money/_moc.md:hourly_consulting_hours_q1_q2_2026
  >= 30 per 4-week window` => delivery mode confirmed.
- Escalation trigger: if week-7 two-checkpoint predicate fires (< 5 sales calls) AND
  hourly hours < 20 in weeks 1-7 → HITL (G1 failure-mode packet).

### Migration trigger binary predicate

```
G1 → G2 migration fires when:
swarm/wiki/operations/quick-money/_moc.md:stage_gates.SG-2:fired == true
AND count(swarm/wiki/operations/*/contracts/*.md) >= 1
AND meta/health.md:cumulative_revenue_eur >= 50000
```

First signed client contract (SG-2 = "≥1 signed contract" predicate) is the Hamel-binary
trigger. On SG-2 fire, brigadier opens A2↔B2 Phase-B substrate prep task within 2 weeks.
This is a hard constraint per §12 Dissent-1 resolution (systems-expert: UC-9 by construction
required at first paying client; Phase-B prep CANNOT wait for G2 completion).

### What breaks if we skip G1

If the system jumps from Phase-0 (pre-€50K) directly to G2 (€200K) without the G1 gate:
- The A1↔B1 substrate was never proven operationally (skills exist in design records but
  have not served a real client workflow). The migration to A2↔B2 has no empirical basis
  for what the substrate must actually do.
- The two-checkpoint kill discipline was never tested. The week-7 pivot signal was never
  observable. The system would arrive at G2 with an untested outreach model.
- The stage-gate DSL (`tools/stage-gate-eval.py`) was never exercised against real
  project data. Predicate misfires at G2 scale (15 projects) are far more costly than
  at G1 scale (2-3 projects).
- The hourly_consulting_hours_q1_q2_2026 accounting discipline was never established.
  At G2, the revenue mix becomes harder to track without this habit.

### Revised-parameter reality-check

Post-ack Option B parameters: 2 contracts/quarter × €7.5K/contract-quarter = €30K
contracts over Q1+Q2 2026. Plus 233 hours × €150/hr = €35K hourly. Total €65K,
clearing the €50K gate with ~30% margin. The margin absorbs: (a) 1 contract failing
to close in Q2 (€7.5K loss → €57.5K, still above gate); (b) hourly hours reaching
only 200 of 233 (€4.5K shortfall → €60.5K, still above gate). The gate is robust
to moderate execution shortfall IF both revenue lines are pursued in parallel.

The tier_1_phase_1 = [Предприниматели, Блогеры] filter (CC-3) is structurally
compatible with G1: these archetypes have the shortest decision cycles (6 weeks per
CC-3 investor analysis) and are reachable via Ruslan's existing English-speaking
infobiz network (D10 primary market). G1 does NOT activate Ресёрчеры / Инженеры /
Инвесторы (tier_2_unlock_trigger: SG-2=fired — these archetypes unlock only on first
signed contract).

**G1 clears under Option B parameters: YES, with ≥30% margin if both revenue lines
are actively pursued.**

---

## §G2 G2 €200K

**Substrate pairing: A2↔B2** — Federated peer-holons KM + Rich mini-swarm per-client
project-mgmt. First paying client steady-state; Phase-B substrate mandatory. Validation
gate: revenue growth from consulting to productized recurring.

### BOSC-A-T-X triggers

- **B (Boundary shift):** The boundary shifts from single-holon (Jetix-central wiki
  with client subdirectories) to multi-holon (Jetix-methodology-holon + per-client-holons
  federated via methodology-push). Each new client is a structurally autonomous peer
  holon. The 13th `holon-ref` edge type activates. The boundary change is: UC-9
  isolation moves from policy+config (A1 Phase-A STACK) to by-construction (A2
  OS+graph+filesystem layers). This boundary shift is triggered by the first signed
  client contract, not by revenue reaching €200K.
- **O (Observable):** count of active client holons: `count(swarm/wiki/clients/*/swarm/wiki/_moc.md)`
  >= 5 (i.e., 5 client-holons operational). Methodology-push protocol demonstrably
  working: `count(jetix-methodology-holon/methodology-versions/*.md)` >= 2 (at least 2
  methodology version pushes completed). Revenue observable: cumulative revenue >= €200K
  (approximately 2 × €7.5K/contract-quarter × 4 quarters = €60K contracts PLUS hourly
  channel continuing).
- **S (Substrate):** A2 operational: per-client JSONL edge-store sharding in place (Ashby
  requisite-variety obligation — NOT optional performance optimization; AP-SYS-10 fires
  without it); per-client agent instances (separate WIKI_ROOT_CLIENT_ID brigadier
  processes); 13th holon-ref edge with /lint L-CROSS-HOLON-REF enforcement; methodology-push
  protocol (one-way Jetix → client). B2 operational: /project-bootstrap rich scaffold
  per client project; mini-swarm-of-3 per active P1/P2 project; per-client KPIs;
  PMBOK lifecycle alpha tracking. CI methodology-push fan-out automation onset (manual
  push at 5 clients; automated at 10+).
- **C (Constraint removed/imposed):** REMOVED: the "single-brigadier serves all" constraint.
  At G2, per-client brigadier instances become the default for client-facing work. IMPOSED:
  the cross-client knowledge-transfer constraint (holon-ref edge + /lint L-CROSS-HOLON-REF
  prohibition = cross-client synthesis FORBIDDEN by default; opt-in case-study only). This
  is the price of UC-9 by-construction: Jetix cannot accidentally learn about client-A from
  client-B's data.
- **A (Agents):** ACTIVATES: per-client project-brigadier instances; per-client mini-swarm-of-3
  per active P1/P2 project; meta-agent weekly sweep expanded to portfolio-level (cross-client
  pattern detection via opt-in case-study protocol). EVOLVES: Ruslan lifts from "operator of
  Jetix-internal swarm" to "coordinator of per-client swarms" — the Role-Lift MHT event.
  Per D21 Alliance 5h/week: early Alliance relationship building begins at G2 (not G4).
- **T (Trajectory):** G2 points toward G3 (€1M, ≥3K pages per client, ≥10 clients active,
  A3 augmentation onset). The trajectory vector: validation (1-3 paying clients, methodology
  works) → replication (10+ clients, methodology is replicable without Ruslan's direct
  involvement in every delivery). The G2→G3 migration requires per-client provisioning
  automation (currently manual at G2); CI automation is the G2 engineering investment.
- **X (External trigger):** The tier_2_phase_2 archetypes activate at SG-2=fired (first
  signed contract), meaning G2 sees broader ICP activation: Ресёрчеры + Инженеры +
  Инвесторы become reachable. Externally, the Mittelstand DACH market is the primary
  growth vector (STRATEGIC-INSIGHT §3 + BIOS-moment positioning). The external signal
  to WATCH: first DACH Mittelstand client onboarded → confirms the EISA-moment positioning
  is functional for the target buyer, not just the English-speaking infobiz ICP.

### MHT events at G2

- **Maturity signal:** `count(swarm/wiki/clients/*/swarm/wiki/_moc.md)` >= 3 (three
  autonomous client holons operational) AND methodology-push v2 has been executed at
  least once (i.e., Jetix has shipped a methodology upgrade to existing clients without
  touching their KB data). This proves the federated architecture is working as designed.
- **Hazard signal:** If Ruslan attempts G2 scale without per-client JSONL sharding, the
  controller variety (BFS over N clients × 125K edges) falls below system variety —
  AP-SYS-10 fires. Observable hazard: `/build-graph` runtime > 5 minutes weekly at 5
  clients (this is the observable from A1 §10 G2 prediction: /build-graph >5min =
  sharding mandatory). Secondary hazard: methodology-push fan-out is still manual at 10+
  clients — each methodology version push requires Ruslan manually running the protocol
  for each client. This caps G2→G3 throughput.
- **Transition mechanism:** G2 → G3 transition executes when the provisioning automation
  is CI-capable (methodology-push automated) AND per-client GPU procurement gate is
  considered (A2 §10 G3 prediction: per-client GPU for offline LLM). The transition is
  NOT revenue-gated alone; it is substrate-capability-gated (CI automation must precede
  the client-count explosion at G3).

### Janus degraded-mode spec

**Self-Assertive excess (per-client isolation over-enforcement):**
- Symptom pattern: the /lint L-CROSS-HOLON-REF rule is enforced so strictly that
  no cross-client learning occurs even via opt-in case-study protocol. Ruslan's
  methodology improves for each client independently but never compounds across
  clients. Observable: `count(jetix-methodology-holon/case-studies/*.md)` = 0 after
  6 months of G2 operation despite having 5+ clients.
- Binary recovery predicate: `count(jetix-methodology-holon/case-studies/*.md) >= 1
  AND count(swarm/wiki/methodology-versions/*.md) >= 2` => cross-client compound
  learning functioning.
- Escalation trigger: if after 3 months of G2 operation there is 0 opt-in case-study
  content in the methodology-holon → HITL (compound-learning-absent packet).

**Integrative excess (methodology-holon rigidity):**
- Symptom pattern: per-client brigadier instances defer every decision to the
  methodology-holon (Ruslan), causing a re-centralization: G2 architecture nominally
  federated but operationally hub-and-spoke with Ruslan as hub. Observable: Ruslan's
  non-delegatable functions (architecture, taste, approval) expanding beyond the 6
  locked functions per D4 Architect-Orbit definition — Ruslan approving per-client
  delivery artefacts that project-brigadier should own autonomously.
- Binary recovery predicate: `count(project-brigadier-autonomous-promotions-per-week) >= 3`
  (project-brigadier autonomously promoting artefacts without HITL, per its decision-rights
  §1d) => federation working as designed.
- Escalation trigger: if `count(ruslan-approvals-per-week)` > 15 sustained for 2 weeks
  (re-centralization observable) → HITL (architect-overload packet).

### Migration trigger binary predicate

```
G2 → G3 migration fires when:
count(swarm/wiki/clients/*/swarm/wiki/_moc.md) >= 10
AND swarm/wiki/clients/<any-client>/swarm/wiki/**/*.md count >= 3000
AND meta/health.md:methodology_push_automation_ci == true
AND meta/health.md:build_graph_runtime_minutes < 5
```

At 10 active client holons AND any single client exceeding 3K wiki pages, A3
augmentation becomes viable and the A3↔B2 substrate migration begins. The
methodology-push CI automation is a prerequisite (manual push collapses at 10+
clients). [F: F4]

### What breaks if we skip G2

If the system jumps from G1 (A1↔B1) directly to G3 (A3↔B2) without the G2 transition:
- A2 federated peer-holons substrate was never built. A3 GraphRAG+HippoRAG is an
  AUGMENTATION layer atop A2 — not standalone. A3 without A2 means the cron
  community-summaries have no per-client isolation (they run against a non-federated
  edge store → UC-9 violation at the compute layer).
- Per-client JSONL sharding was never implemented. At G3 scale (50+ clients × 125K
  edges each = 6.25M edges total), the un-sharded edges.jsonl becomes unmanageable.
  AP-SYS-10 fires at full G3 load.
- The mini-swarm-of-3 per project (B2) was never validated. At G3 scale (15-20
  mini-swarms active simultaneously per B2 §10), an unvalidated mini-swarm pattern
  creates coordinated failure across all active client projects simultaneously.
- The Dissent-1 resolution (UC-9 by-construction at first paying client) was violated.
  Clients onboarded under A1 Phase-A isolation (policy+config only) are now at G3
  scale without by-construction isolation. Retroactive migration of client data to A2
  substrate under live client load is the highest-cost outcome.

### Revised-parameter reality-check

G2 (€200K) is reachable from Option B G1 parameters if the trajectory holds:
assuming 4 contracts/quarter (2/Q × 2 Qs) = €30K from contracts in Phase-1, then G2
requires roughly 4 more quarters of equivalent or growing contract velocity (8 total
contract-quarters = €60K contracts) PLUS hourly channel continuing (233hrs at €150 =
€35K/year at G1 pace → more at G2 as Ruslan's rate and capacity grow). The €200K gate
is not a single-year target — it is a cumulative validation gate. The tier_1_phase_1
filter makes G2 progression cleaner: [Предприниматели, Блогеры] validated at G1 serve
as case studies for tier_2_phase_2 (Митьельштанд, Ресёрчеры) activation at G2. The
two-checkpoint kill at G1 ensures only a validated outreach model carries forward into G2
scale — a failed G1 kill-predicate prevents G2 scale on a broken model.

**G1→G2 trajectory holds under Option B parameters: YES, conditional on CI methodology-push
automation being built during G1-G2 transition (this is the engineering investment that
enables G2 scale).**

---

## §G3 G3 €1M

**Substrate pairing: A3↔B2** — GraphRAG+HippoRAG hybrid (augmenting A2) + Rich
mini-swarm. Phase-2 close; ≥3K wiki-pages per client; ≥10 clients active. A3 activation
mandatory. A2↔B2 → A3↔B2 migration. VSM Level-3 audit/optimisation function emerges as
a distinct sub-system.

### BOSC-A-T-X triggers

- **B (Boundary shift):** The boundary expands from bilateral (Jetix ↔ individual clients)
  to network (Jetix ↔ clients ↔ emerging Alliance). The Mittelstand AI Alliance begins
  formal entity discussions at G3 (per A2 §10 G3: "sub-roy split + per-portfolio brigadier;
  per-client GPU procurement gate"). The boundary change: Alliance-methodology-holon becomes
  a distinct entity from Jetix-methodology-holon — Alliance members can push to the Alliance
  methodology corpus, not just receive from Jetix.
- **O (Observable):** `count(swarm/wiki/clients/*/)` >= 10 active client holons AND
  `count(swarm/wiki/clients/<any-client>/swarm/wiki/**/*.md)` >= 3000 AND A3 cron
  producing `communities.jsonl` per client (nightly cron confirmed running). Revenue
  observable: cumulative revenue >= €1M (approximately 3-4 years from G1 at Option B
  trajectory, assuming contract growth to 4-6 contracts/quarter at higher rates by G3).
- **S (Substrate):** A3 operational: GraphRAG community-summaries (Leiden algorithm nightly
  cron per-client UNIX user); HippoRAG PPR index (parquet per-client); A3-augmented
  `/ask --multidoc-graphrag` skill live; per-client GPU procurement (rental at G3,
  ownership path at G4). B2 with sub-roy split: 3 sub-roys (consulting / infra / research)
  each with their own brigadier instance and domain-expert roster. VSM Level-3 audit function
  materializes as a distinct swarm cell (meta-agent at G3 is no longer a single instance
  but a per-portfolio sub-coordinator pool).
- **C (Constraint removed/imposed):** REMOVED: the grep p95 <2s constraint (A3 pre-computed
  community summaries eliminate retrieval latency; cross-document synthesis no longer
  bottlenecked by real-time BFS). IMPOSED: the nightly cron compute constraint (~50 GPU-hours
  nightly aggregated per A3 §10 G3 prediction; ~€4-7K/month compute per investor §4 note);
  the methodology-version-skew tracker constraint (at 50+ clients, different clients may be
  on different methodology versions — skew tracker is mandatory G3 infrastructure).
- **A (Agents):** ACTIVATES: sub-roy brigade per portfolio (consulting sub-roy, infra sub-roy,
  research sub-roy); per-client GPU procurement governance; methodology-version-skew tracker
  agent. EVOLVES: Ruslan lifts further — from "coordinator of per-client swarms" to "Alliance
  architect" (D21 Alliance 5h/week: this is where the D21 roy-replication pattern begins to
  materialize). The roy-replication: Ruslan trains a roy (replication of Ruslan's methodology
  governance role) for each sub-roy portfolio. This is the G3 organizational inflection.
- **T (Trajectory):** G3 points toward G4 ($100M, holding structure active, Alliance formal
  entity, methodology-license dominant revenue). The trajectory vector: replication (10+
  clients → 500+ clients) requires the Alliance governance structure that G3 begins to build.
  The G3 pre-investment decision (pre-investing in persistent graph + Alliance structure at G3
  rather than at G4) is the single most important scalability decision in the entire trajectory —
  per prior strategies.md rule: `rule: G3-pre-investment-mandatory-for-G4-antifragility`.
- **X (External trigger):** EU regulatory landscape (GDPR Art. 32 + EU AI Act Art. 14 + BSI C5)
  intensifies at G3 scale. Mittelstand clients at G3 are likely to require ISO 27001 / BSI C5
  compliance attestation. This external trigger imposes a compliance-overhead constraint that
  was optional at G1-G2 but becomes mandatory at G3. The external signal: first client
  formally requesting compliance audit → triggers Jetix compliance-layer activation (per
  A2 §6 EU compliance section).

### MHT events at G3

- **Maturity signal:** A3 nightly cron running successfully for ≥30 consecutive days across
  ≥5 client holons AND cross-document synthesis quality demonstrably improved (per UC-3 read
  trace: multi-partnership query answered in <3s vs A1 alone >30s). Sub-roy structure
  operational: 3 sub-roys with autonomous per-portfolio brigadiers.
- **Hazard signal (primary):** VSM Level-3 function (audit/optimisation) attempted implicitly
  (brigadier trying to aggregate state from 50 client holons) rather than explicitly (dedicated
  sub-coordinator pool). Observable: LLM session context budget collapsing under volume of
  state to aggregate — per strategies.md rule: `rule: mht-fission-triggers-on-context-budget-collapse-not-on-client-count`.
  The hazard is: attempting to run Level-3 audit via a single brigadier instance after client
  count exceeds the context budget. Observable: brigadier session summaries becoming truncated
  or missing escalations from client holons.
- **Hazard signal (secondary — FRAGILE gate):** G3→G4 is the antifragility failure gate.
  If G3 does NOT pre-invest in persistent graph DB + Alliance governance structure, the G4
  transition requires ~40% structural change under live load. Per systems-expert strategies.md
  `rule: G3-pre-investment-mandatory-for-G4-antifragility`: this pre-investment CANNOT be
  deferred to G4.
- **Transition mechanism:** MHT Fission event at G3 onset: meta-agent splits into sub-coordinators
  (one per sub-roy portfolio). This is NOT triggered by client count crossing an arbitrary
  threshold — it fires when context-budget collapse is observed (per strategies.md rule). The
  transition: brigadier opens a Fission packet; new sub-coordinator agent files are authored;
  per-portfolio brigadiers take over Level-1/Level-2 coordination; top-level brigadier handles
  only Level-3 (audit) + Level-4 (futures/Alliance) + Level-5 (identity/policy) per Beer VSM.

### Janus degraded-mode spec

**Self-Assertive excess (sub-roy siloing):**
- Symptom pattern: the 3 sub-roys (consulting / infra / research) operate as fully
  independent entities with no methodology sharing between them. The cross-sub-roy compound
  learning (patterns from consulting sub-roy informing research sub-roy) is absent. Observable:
  `count(jetix-methodology-holon/cross-portfolio-claims/*.md)` = 0 after 6 months of
  sub-roy operation despite each sub-roy having rich `strategies.md` entries.
- Binary recovery predicate: `count(jetix-methodology-holon/cross-portfolio-claims/*.md) >= 3`
  => cross-sub-roy learning compounding.
- Escalation trigger: if 6 months post-Fission shows 0 cross-portfolio claims → HITL
  (compound-siloing packet); brigadier may mandate a cross-portfolio synthesis cycle.

**Integrative excess (Ruslan as single G3 bottleneck):**
- Symptom pattern: sub-roy roys are not functioning as independent governance — every
  Alliance methodology update, every cross-client compliance decision, every new sub-roy
  investment still routes to Ruslan for approval. The VSM Level-3 audit function nominally
  exists but functionally = Ruslan reviewing everything. Observable: Ruslan's weekly
  HITL-approval count > 20 (far above the ≤20 active tasks rule that applies even at
  brigadier level).
- Binary recovery predicate: `count(sub-roy-autonomous-decisions-per-week) >= 10`
  (sub-roys making governance decisions without HITL routing) => governance decentralized
  as designed.
- Escalation trigger: if `ruslan_weekly_approvals > 20` sustained for 3 weeks → HITL
  (governance-overload packet); trigger roy-replication review (D21 Alliance 5h/week
  is the intended mechanism for training roys to take this load).

### Migration trigger binary predicate

```
G3 → G4 migration fires when:
count(swarm/wiki/clients/*/) >= 50
AND meta/health.md:alliance_entity_formed == true
AND meta/health.md:methodology_license_revenue_pct >= 0.20
AND meta/health.md:sub_roy_autonomous_decision_rate >= 10_per_week
AND count(jetix-methodology-holon/methodology-versions/*.md) >= 5
```

The Alliance entity formation + methodology-license revenue at 20%+ of total revenue are the
structural signals that G4 infrastructure is activating. Without the Alliance entity, the G4
holding structure has no formal counterpart. [F: F4]

### What breaks if we skip G3

If the system jumps from G2 (A2↔B2, 10 clients) directly to G4 ($100M, 500+ clients):
- A3 pre-computed retrieval atlas was never built. At G4 scale, real-time BFS over 500 clients
  × 125K edges = 62.5M edges is computationally infeasible without A3 pre-compilation. Every
  client query degrades severely.
- The VSM Fission event was never executed. G4 scale requires sub-coordinators by construction;
  attempting G4 with a single-tier brigadier causes the context-budget collapse identified as the
  hazard signal. The Fission event becomes an emergency rather than a planned transition.
- The Alliance governance structure was not built at G3. At G4, the methodology-license revenue
  shift (Wintel precedent: dominant revenue from licensing, not from services) requires an
  Alliance entity to distribute and enforce the license. Without it, G4 scale is purely services-
  revenue (fragile; hits Ruslan capacity ceiling hard).
- The ~40% structural change at G3→G4 becomes unavoidable: it executes under live client load
  rather than as a planned pre-investment. This is the highest-cost restructuring scenario per
  strategies.md `rule: G3-pre-investment-mandatory-for-G4-antifragility`.

### Revised-parameter reality-check

The G3 trajectory is not directly governed by the Option B parameters (which are Phase-1-specific).
However, the two-checkpoint kill (CC-4) applied at G1 ensures only a validated model reaches G3.
The tier_1_phase_1 filter ([Предприниматели, Блогеры]) at G1 builds the early case studies that
unlock tier_2 archetypes (Митьельштанд — the primary G3 buyer). The 233-hour accounting discipline
(`hourly_consulting_hours_q1_q2_2026: 233` in quick-money _moc.md) established at G1 becomes the
habit infrastructure for tracking time-allocation across sub-roys at G3 (the metric scales: it
becomes a per-sub-roy time-allocation tracker). The A1↔B1 → A2↔B2 migration (executed at G2
first paying client per Dissent-1 resolution) is the prerequisite for A3↔B2 at G3 to have any
substrate to augment.

**G3 is reachable if G2 CI automation investment executes on schedule. G3 is the gate where
antifragility is made or broken — pre-investment at G3 determines G4 outcome.**

---

## §G4 G4 $100M

**Substrate pairing: A3↔B2 (Alliance-federated)** — A3 GraphRAG+HippoRAG at Alliance scale;
B2 mini-swarms across 50+ active clients; holding structure active; methodology-license revenue
dominant; D21 Alliance 5h/week formal; roy-replication active.

### BOSC-A-T-X triggers

- **B (Boundary shift):** The system's boundary now includes the Alliance formal entity as an
  internal constituent, not an external partner. The Alliance methodology-holon is no longer
  Jetix-owned exclusively — it is jointly governed by Alliance members under a methodology-license
  structure. The boundary change: Jetix transitions from "single-methodology-provider" to
  "Alliance-committee member with special IP rights" (per STRATEGIC-INSIGHT §1 EISA-committee
  parallel). D21 Alliance 5h/week was the seed; G4 is where D21 becomes a structural governance
  right, not a weekly call.
- **O (Observable):** `meta/health.md:alliance_member_count` >= 50 (Mittelstand AI Alliance
  members deploying Jetix methodology under license) AND `meta/health.md:methodology_license_revenue_pct`
  >= 0.50 (licensing at 50%+ of total revenue, per Wintel precedent where licensing overtook
  services as dominant revenue stream). Revenue observable: cumulative or annual revenue >= $100M
  (requires Alliance-scale licensing fees + services at 50+ clients).
- **S (Substrate):** A3 at Alliance scale: federated cron orchestration across per-Alliance-region
  GPU pools; Mittelstand-LLM 13B+ default for community summaries (per A3 §10 G4 prediction:
  "aggregate ~50 GPU-hours nightly; Alliance governance"). B2 at 50+ mini-swarms: per-Alliance-
  member methodology-push from Alliance-methodology-holon (not from Jetix directly); per-sub-roy
  autonomous governance. Holding structure: GmbH holding entity (DE legal home per JETIX-PLAN §1)
  expanded to holding group with Alliance governance subsidiary.
- **C (Constraint removed/imposed):** REMOVED: the "Ruslan is the sole methodology arbiter"
  constraint. At G4, the Alliance methodology parliament (per philosophy-scalability: the mechanism
  for $1T peer-review) begins to function. Ruslan retains veto rights per Architect-Orbit (D4)
  but day-to-day methodology evolution is Alliance-governed. IMPOSED: the √N network-effect
  constraint (conservative Reed-approximation per investor-scalability Dissent-6; Metcalfe N²
  not yet validated — requires Alliance governance maturity assessment). The Alliance governance
  overhead: standardization lag (different member deployments at different methodology versions;
  skew tracker mandatory).
- **A (Agents):** ACTIVATES: per-Alliance-region sub-coordinator pools; Alliance-methodology-
  parliament agent (a new agent archetype: Alliance-brigadier, responsible for cross-member
  methodology synthesis without leaking member KB). EVOLVES: Ruslan lifts from "Alliance architect"
  to "USB-C connector" identity (D20) — the active role is standards-maintenance and new-member
  onboarding, not per-client delivery. Roy-replication: multiple roys now independently operate
  sub-roy portfolios; Ruslan trains roy-of-roys (second-order replication).
- **T (Trajectory):** G4 points toward G5 ($1T, jetix-owned compute infra, CRDT federation,
  Token economy Option B). The trajectory vector: Alliance becomes self-governing → Jetix
  extracts value from Alliance membership fees + methodology-license + hardware infrastructure
  (audio_526 hardware + электростанции as per brief G5 spec). From G4, the adjacent-possible
  (per Kauffman) is: G5 infrastructure ownership as the next reachable configuration.
- **X (External trigger):** The EU AI Act enforcement timeline accelerates at G4 scale. 50+
  Mittelstand clients means the Alliance is a regulatory touchpoint — BSI C5 + ISO 27001
  alignment is not optional at this scale but contractually required for DACH enterprise sales.
  The external trigger: first regulatory audit of an Alliance member deployment → forces Alliance-
  wide compliance attestation standardization. The BIOS-moment maturation: at G4, the Alliance IS
  the EISA consortium from the historical parallel — it has established the standard that others
  reference.

### MHT events at G4

- **Maturity signal:** Alliance methodology parliament has executed ≥1 collective methodology
  upgrade (all members receive methodology-push v(n) simultaneously via Alliance-brigadier) AND
  `meta/health.md:methodology_license_revenue_pct` >= 0.50 (licensing dominant) AND at least 3
  roys operate independently (roy-replication producing second-generation roys).
- **Hazard signal:** Context-budget collapse at Alliance-level (analogous to the G3 Fission
  event, but at Alliance scale): the Alliance-brigadier attempting to aggregate methodology state
  from 50+ member holons exceeds LLM session context budget. Observable: Alliance-brigadier
  session quality degrades (cross-member synthesis outputs truncated, contradictions undetected).
  This triggers Alliance-level Fission: per-region sub-coordinators for the Alliance, not just
  per-portfolio.
- **Transition mechanism:** Alliance-Fission at G4 onset: Alliance-brigadier splits into
  per-region Alliance-coordinators (EU / US / APAC — per global rollout per JETIX-PLAN §1 Phase 3).
  The mechanism mirrors the G3 Fission but at the Alliance (inter-holon) layer rather than the
  sub-roy (intra-Jetix) layer. Alliance governance constitution is drafted at G4 and ratified by
  members — the document that defines the Alliance methodology parliament procedures.

### Janus degraded-mode spec

**Self-Assertive excess (Alliance over-control):**
- Symptom pattern: Jetix retains de facto control of the Alliance methodology parliament (voting
  rights weighted so Jetix always wins any methodology vote). The Alliance "parliament" is
  nominal — Jetix pushes methodology without genuine Alliance input. Members defect to competing
  standards (Senge L5 — pushing the wrong lever too hard creates equal-and-opposite resistance).
  Observable: Alliance member churn rate > 20% annually (members exiting the Alliance).
- Binary recovery predicate: `meta/health.md:alliance_member_churn_rate_annual < 0.10`
  AND `count(alliance-member-initiated-methodology-proposals/*.md) >= 3` => Alliance functioning
  as genuine parliament, not captured methodology.
- Escalation trigger: if churn > 20% in any 12-month period → HITL (Alliance-governance-crisis
  packet); Ruslan activates Architect-Orbit veto + Alliance constitution revision.

**Integrative excess (Alliance dependency lock-in):**
- Symptom pattern: Jetix's methodology evolution becomes so dependent on Alliance consensus
  that Jetix cannot ship methodology improvements without waiting for Alliance ratification (3-6
  month consensus cycles). The Lakatos hardcore ossification risk (identified by philosophy-scalability):
  Alliance governance becomes so rigid that the methodology cannot adapt to market changes.
  Observable: time-to-methodology-version-ship > 90 days consistently.
- Binary recovery predicate: `meta/health.md:methodology_version_cycle_days < 30` (Jetix can
  ship methodology updates within 30 days via an expedited Alliance fast-track protocol) =>
  governance agile enough.
- Escalation trigger: if version cycle days > 90 for 2 consecutive versions → HITL (methodology-
  velocity-collapse packet); Ruslan activates Architect-Orbit authority to bypass Alliance
  ratification for emergency methodology updates.

### Migration trigger binary predicate

```
G4 → G5 migration fires when:
meta/health.md:alliance_member_count >= 500
AND meta/health.md:jetix_compute_owned_gpu_count >= 1
AND meta/health.md:methodology_license_revenue_pct >= 0.70
AND meta/health.md:token_economy_internal_active == true
AND count(alliance-methodology-parliament-votes/*.md) >= 10
```

G5 requires owned compute infrastructure (audio_526 hardware + электростанции per brief G5 spec)
— this is the first gate where hardware ownership becomes a migration prerequisite. The Alliance
must also have demonstrated genuine parliamentary function (≥10 recorded methodology votes) before
G5 infrastructure investment is justified. [F: F3 — forecast-grade at this horizon]

### What breaks if we skip G4

If the system jumps from G3 (€1M, sub-roy operative) directly to G5 ($1T, federated compute):
- Alliance governance structure was never established at G4. G5 federation (thousands of holons
  across regions) requires an Alliance governance constitution as prerequisite. Without it,
  CRDT edge federation (the G5 technical requirement) has no governance layer to resolve
  conflicts between federated holons.
- Methodology-license revenue never became dominant. G5 assumes licensing >> services as revenue
  structure. Without G4 establishing this structure, G5 revenue is still predominantly services
  (Ruslan + roys consulting at scale) — not infrastructure + licensing. This is a different
  business and not the $1T trajectory.
- Roy-replication never scaled to second-generation. G5 requires multiple waves of roys operating
  independently. Skipping G4 means the roy-training methodology was never validated at G4 scale.
  G5 attempt with first-generation roys only = capacity ceiling re-emerges.
- The owned compute infrastructure decision at G5 has no operational proof of the usage pattern
  it must serve. G4 is where Alliance-scale GPU usage (50 GPU-hours nightly aggregated) creates
  the predictable demand curve that justifies compute ownership at G5.

### Revised-parameter reality-check

G4 is not directly constrained by G1 Option B parameters. The G4 trajectory depends on G3
executing correctly (Alliance entity formed, methodology-license revenue at 20%+, sub-roys
autonomous). The CC-4 two-checkpoint kill discipline from G1 is structurally analogous to G4's
Alliance-member churn rate discipline: both are falsifiability mechanisms that prevent operating
on an assumption without observable signal. The `hourly_consulting_hours_q1_q2_2026: 233`
metric established at G1 scales into a per-sub-roy time-allocation framework at G4 — the habit
of tracking time against a measurable target becomes the Alliance's capacity-planning tool.

**G4 is the antifragility realization gate: if G3 pre-invested correctly, G4 is true-antifragile
(Alliance adds more value per member as methodology compound-learns). If G3 pre-investment was
deferred, G4 is FRAGILE and requires ~40% emergency restructuring under live client load.**

---

## §G5 G5 $1T

**Substrate pairing: Alliance-federated A3↔B2 + owned compute.** Thousands of holons across
multiple continental regions; CRDT edges; federated wikis; jetix-owned compute infrastructure
(audio_526 hardware + электростанции per brief spec); Token economy Option B (D23); civilizational-
level infrastructure.

### BOSC-A-T-X triggers

- **B (Boundary shift):** The boundary expands from "Jetix + Alliance members" to "Jetix + Alliance
  + regulators/standards bodies as internal constituents." The EU AI Act standards bodies, BSI, ISO,
  potentially NIST — these become Alliance governance participants (not external constraints) because
  at $1T scale, Jetix's methodology IS the industry standard that regulators reference. The boundary
  fusion: regulators join the holon (per the systems-expert agent core memory MHT Fusion definition:
  "regulators become part of the holon"). The Jetix Fusion at G5 is analogous to how EISA became
  the regulatory standard body for PC bus architecture — the standard IS the regulator.
- **O (Observable):** `meta/health.md:alliance_member_count` >= 2000 (thousands-scale per A2 §10 G5
  prediction) AND `meta/health.md:jetix_owned_compute_active == true` AND annual methodology-license
  + infrastructure revenue >= $100M (prerequisite for $1T valuation via standard revenue multiples).
  Secondary observable: first government procurement referencing Jetix methodology standard in
  procurement specifications.
- **S (Substrate):** CRDT edges for conflict-free distributed synchronization across per-Alliance-region
  federated wikis (per A1 §10 G5 prediction: "CRDT edges + federated wikis"). Per-Alliance-region GPU
  pools with jetix-owned compute (not rental). Token economy Option B (D23) operational internally:
  Alliance members transact in a token layer for methodology access, compliance attestation, and
  cross-member knowledge transfer. Mittelstand-LLM 70B+ Alliance-blessed (per A3 §10 G5: "Mittelstand-
  LLM 70B+ Alliance-blessed") running on owned hardware.
- **C (Constraint removed/imposed):** REMOVED: the GPU-rental dependency (from G4 rental → G5 owned;
  the predictable demand curve from G4 justifies CapEx). REMOVED: the Ruslan-as-single-veto
  constraint in methodology parliament (at G5, Jetix retains "protocol layer" authority but specific
  methodology votes are Alliance-parliamentary without Ruslan veto on most issues). IMPOSED: the
  civilizational-infrastructure operating discipline — at $1T, failure modes are not business
  failures but societal failures. The reliability, security, and governance standards required
  are categorically different from G1-G4.
- **A (Agents):** ACTIVATES: per-Alliance-region Alliance-coordinators (EU / US / APAC / LATAM at
  minimum); Token-economy-clearing agent; regulatory-liaison agent (interfaces with standards bodies).
  EVOLVES: Ruslan lifts from "USB-C connector" to "founder-of-the-standard" identity — the role
  analogous to IBM's role after EISA: the standard creator who no longer controls the standard but
  whose original design remains in every implementation. Roy-of-roys at second and third generation:
  the methodology is now self-replicating beyond direct Ruslan involvement.
- **T (Trajectory):** G5 is the final stated gate in the KM-ARCHITECTURE-VARIANTS §11 trajectory.
  Beyond G5, the adjacent-possible (Kauffman) includes: civilizational-infrastructure position
  where AI methodology becomes as fundamental as the internet protocol stack (D19 $1T trajectory).
  The trajectory beyond G5 is not architecture-level — it is civilizational.
- **X (External trigger):** The external trigger that realizes $1T is not a single event but a
  convergence: (a) AI regulation globally standardizes around frameworks compatible with Jetix
  methodology (privacy-by-architecture + local-first becomes the regulatory default); (b) the
  Mittelstand AI Alliance has enough members that the methodology IS the de facto standard for
  AI implementation in European Mittelstand (and potentially broader); (c) the Token economy
  Option B (D23) creates a self-reinforcing adoption loop (methodology improves → more members →
  token value rises → methodology investment increases). The external X-event: first major
  government mandate citing Jetix methodology standard in public-sector AI procurement.

### MHT events at G5

- **Maturity signal:** Alliance methodology parliament autonomous (Jetix retains protocol-layer
  rights but daily governance is Alliance-run without Ruslan's operational involvement) AND
  jetix-owned compute infrastructure cashflow-positive (hardware not a cost center — it is a
  revenue center via Alliance compute access fees) AND Token economy Option B (D23) demonstrably
  creating self-reinforcing adoption (new members citing existing member success as primary
  adoption driver rather than Jetix direct sales).
- **Hazard signal:** The network-effect exponent question (Dissent-6: √N vs N²) resolves at G5.
  If the Alliance at 2000+ members shows √N growth pattern (sub-linear marginal value per new
  member), the $1T valuation requires more members than assumed (conservative). If N² Metcalfe
  holds (validated by Alliance governance maturity + HITL bottleneck removal at G4), the $1T
  target is reachable with fewer members (aggressive). The hazard: planning on N² and getting √N
  → Alliance size estimate is wrong by a factor of N. The correct posture is planning on √N
  (per investor-scalability Dissent-6 resolution) with Metcalfe as upside.
- **Transition mechanism:** G5 is an operating state, not a gate to a G6. The transition
  "mechanism" at G5 is the civilizational-infrastructure operating discipline: maintaining
  the standard, evolving it via Alliance parliament, and ensuring no single point of control
  re-emerges (per BIOS-moment Lesson 1: single-point-of-control does not hold in multi-layer
  systems). The Token economy Option B (D23) is the self-sustaining mechanism.

### Janus degraded-mode spec

**Self-Assertive excess (standards monopoly pathology):**
- Symptom pattern: the Alliance methodology becomes so dominant that it begins functioning as a
  proprietary lock-in rather than an open standard. Members cannot migrate away because their
  entire KB is formatted in Jetix-specific edge types and file conventions. The IBM MCA mistake
  (vs EISA open standard — STRATEGIC-INSIGHT §1 lesson 6: standard > proprietary on mature
  market). Observable: Alliance member contract terms preventing methodology migration within 12
  months of signing; no published migration path for members wanting to exit.
- Binary recovery predicate: `meta/health.md:alliance_published_exit_protocol == true`
  AND `count(alliance-methodology-interoperability-specs/*.md) >= 3` => Alliance provably
  open-standard (not proprietary lock-in).
- Escalation trigger: if any Alliance member publicly cites vendor lock-in as a concern →
  HITL (standards-openness packet); Ruslan activates Architect-Orbit + Alliance parliament
  to publish migration path within 30 days.

**Integrative excess (civilizational diffusion — loss of self):**
- Symptom pattern: the methodology becomes so diffuse across Alliance members and regulatory
  frameworks that the Jetix core identity and IP rights dissolve. The closed core (D13) has
  been so thoroughly opened that there is no remaining proprietary layer to protect. Jetix
  becomes a "historical contributor" to a standard it no longer controls or profits from.
  The Kelly out-of-control risk: designed control released too fully, leaving no residual
  value capture.
- Binary recovery predicate: `meta/health.md:jetix_core_ip_licensing_revenue_annual_usd >= 1e8`
  (at least $100M/year from core IP licensing, not just Alliance services) => Jetix retains
  meaningful value capture from the standard it created.
- Escalation trigger: if annual core-IP licensing revenue < $10M for 2 consecutive years at G5
  scale (indicating value-capture failure) → HITL (IP-strategy revision packet); Ruslan activates
  patent + licensing structure review.

### Migration trigger binary predicate

```
G5 ongoing operating predicate (not a migration gate):
meta/health.md:alliance_member_count >= 2000
AND meta/health.md:methodology_license_revenue_pct >= 0.70
AND meta/health.md:jetix_core_ip_licensing_revenue_annual_usd >= 1e8
AND meta/health.md:alliance_published_exit_protocol == true
AND meta/health.md:token_economy_self_sustaining == true
```

G5 is not a migration-from gate (there is no G6 in the stated trajectory). This predicate
is an ongoing health check that confirms G5 is stable rather than sliding back toward G4
configuration. If multiple predicates fail simultaneously → HITL (G5-structural-degradation
packet). [F: F2 — anecdote-grade at this forecast horizon]

### What breaks if we skip G5

G5 is the stated endpoint of the trajectory; there is no skip scenario in the conventional
sense. However: attempting G5 infrastructure investment (owned compute, CRDT, Token economy)
without G4 Alliance governance in place creates the governance-before-infrastructure inversion.
The BIOS-moment parallel: IBM shipped BIOS (infrastructure) before the Alliance standard existed,
which is why IBM lost control. Jetix must ship Alliance governance (G4) before owning compute
infrastructure (G5) — the governance layer must precede the infrastructure ownership or the
infrastructure becomes a control mechanism that member resistance can terminate (Senge L2: the
harder you push the system, the harder it pushes back).

### Revised-parameter reality-check

G5 is not constrained by G1 Option B parameters in any direct arithmetic sense. However, the
foundational habit established at G1 (hourly_consulting_hours_q1_q2_2026: 233 tracked; two-checkpoint
kill falsifiability; tier_1_phase_1 archetype discipline) establishes the operational culture that
scales through every gate: measure, falsify, adapt. The culture of falsifiable predicates (from
CC-4 two-checkpoint kill at G1 to G5's ongoing operating predicate) is the single structural
property that must survive from G1 to G5 — not any specific technical substrate.

**G5 is true-antifragile if G4 pre-invested in Alliance governance and G3 pre-invested in
sub-roy structure. The antifragility chain: G1→G2→G3 each add a layer the next gate depends on.
Remove any layer and the chain breaks.**

---

## §Overview Overall antifragility check (Brief §5.1 ≤30% refactor per 10× scale)

| Gate transition | Structural change estimate at 10× | Verdict | Dominant loops at 10× |
|---|---|---|---|
| G1 → G2 (10× clients: 0→3 avg) | ~15% (A2 substrate authoring; per-client JSONL sharding) | ROBUST | Reinforcing: methodology-replication loop; Balancing: UC-9 isolation constraint |
| G2 → G3 (10× clients: 3→30+) | ~25% (A3 cron layer + sub-roy Fission + per-GPU procurement) | ROBUST | Reinforcing: community-summary quality loop; Balancing: nightly-cron compute constraint |
| G3 → G4 (10× clients: 50→500+) | ~40% (Alliance entity + methodology-license revenue shift + holding structure) | FRAGILE | Reinforcing: Alliance-network-effect (√N); Balancing: Alliance-governance-overhead constraint |
| G4 → G5 (10× members: 50→500+ Alliance) | ~20% (CRDT edges + Token economy + owned compute) | ROBUST if G4 pre-invested | Reinforcing: Token-self-reinforcing loop; Balancing: regulatory-compliance overhead |

**Overall antifragility verdict per trajectory:**
- G1-G2-G3: ROBUST (each transition < 30% structural change if executed as designed)
- G3→G4: FRAGILE (40% change; requires G3 pre-investment to avoid emergency restructuring)
- G4→G5: ROBUST-conditional (< 30% change if G4 Alliance governance in place; FRAGILE if not)

**True antifragility claim:** The system demonstrates TRUE ANTIFRAGILE properties at G4-G5
IF G3 pre-investment executes. Each Alliance member that joins adds an independent variation
source to the methodology (per Kauffman adjacent-possible). The methodology gets BETTER with
each client — per A2 §10 anti-fragility verdict. This is the Jetix moat: methodology quality
is superlinear in Alliance membership, which is the precondition for the $1T trajectory.

---

## §Summary MHT sequence across all 5 gates

| Gate | MHT event type | Trigger | Effect |
|---|---|---|---|
| G1 €50K | Phase Promotion | First paying client (SG-2 fire) | A1↔B1 operational → A2↔B2 prep begins |
| G2 €200K | Role-Lift | per-client holons ≥ 3 + methodology-push v2 executed | Ruslan lifts from operator → coordinator |
| G3 €1M | Phase Promotion + Fission | Context-budget collapse on meta-agent + Alliance entity formation | Sub-roys created; Level-3 audit promoted to explicit |
| G4 $100M | Context Reframe + Fission (Alliance) | Alliance parliament ≥ 10 votes + licensing dominant | Alliance-brigadier splits to per-region; methodology = licensed standard |
| G5 $1T | Fusion | Regulatory bodies join Alliance governance | Jetix = civilizational infrastructure; standard IS the regulator |

---

## §Risks residual

- **R1:** G3 pre-investment deferral is the single highest-risk failure mode. If G2
  CI automation investment is deferred, G3 arrives without the substrate that enables
  pre-investment. Brigadier must flag any deferral of CI automation as a G3 risk amplifier.
- **R2:** The DACH golden-set evaluation for Mistral 7B vs Llama 3.1-8B (Dissent-2 in
  KM-ARCHITECTURE-VARIANTS §12) is unresolved. This becomes load-bearing at G2 when the
  first client's UC-10 offline LLM is deployed. Recommendation: authorize evaluation as a
  separate task before first client onboarding.
- **R3:** The √N vs N² Alliance network-effect resolution (Dissent-6) determines the $1T
  member-count requirement. Planning on √N (conservative) is correct for Phase-B financial
  models; if Metcalfe N² validates at G4, the timeline compresses significantly.
- **R4:** Regulatory acceleration (EU AI Act enforcement timeline) may impose G3-equivalent
  compliance overhead on G1-G2 operations. Observable: first client requesting BSI C5 / ISO
  27001 attestation before G3 — this is an early-trigger signal for compliance-layer
  acceleration.
- **R5:** The two-checkpoint kill at G1 (CC-4) may fire negatively. If week-7 shows <5
  sales calls → outreach pivot immediately. If week-13 shows 0 contracts + <10 pipeline →
  the quick-money P1 project is killed and a new G1 approach must be designed. The kill
  predicate is a feature, not a risk — it prevents investing further in a failed model.
  The risk is: executing the kill cleanly (archiving the project per /project-archive skill)
  and not drifting into zombie status.
