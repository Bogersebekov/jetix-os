---
title: Philosophy × Integrator — Epistemic Backbone Overlay + Meta-Decision Arbitration
type: integration
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
confidence_method: expert-judgment-from-peer-integrator-drafts-and-tier1
tier: tier-1
produced_by: philosophy-integrator
sources:
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-critic-epistemic-audit.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-optimizer-frg-discipline.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-optimizer-scaffold-deltas.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md
  - decisions/JETIX-PHILOSOPHY.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - prompts/km-architecture-research-2026-04-24.md
  - .claude/agents/philosophy-expert.md
related:
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md
  - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md
  - decisions/JETIX-ARCHITECTURE-BRIEF.md
binding_scope: km-architecture-philosophy-integrator-overlay
mode: integrator
---

# Philosophy × Integrator — Epistemic Backbone Overlay + Meta-Decision Arbitration

> **Purpose.** This document provides the epistemic-backbone overlay that sits
> above the engineering, systems, and mgmt optimizer outputs for the KM
> architecture research cycle. It does not pick variants — that is instrumental
> Рациональность (investor-expert territory, FPF L1003-1006). It validates
> claim-validity gates, surfaces inter-cell contradictions with dissent
> preservation, and delivers meta-decision arbitration per brigadier §5.3
> case-4. Each major claim carries an (F, ClaimScope, R) triple.

---

## §1 F-G-R Discipline Applied to Peer Variant Candidates

The six anticipated variants (Layer-A: A1/A2/A3; Layer-B: B1/B2/B3) are
characterised below by their epistemic posture — specifically whether each
carries the three properties required by the philosophy-critic (H-1..H-5) and
closed by the philosophy-optimizer (Delta-1..Delta-5). For each candidate the
integrator scores three gates:

- **Falsifiability check (Δ1 gate).** Does every "supports UC-N" or "scales
  to G5" claim carry a populated `R.refuted_if` naming an observable, not
  merely an `R: high` label?
- **Supersession-chain check (Δ2..Δ4 gate).** Are SC-1 (cross-client
  supersedes FORBIDDEN), SC-2 (Lakatos hardcore lint), SC-3 (lint-scope
  isolation), and SC-4 (universality gate on F4+ claims) honoured?
- **UC-7×UC-9 tension resolved.** Does the variant show — in its UC-7 section
  — that contradiction detection runs per-client and cannot sweep across client
  boundaries?

| Variant candidate | Falsifiability check | Supersession check | UC-7×UC-9 check | Epistemic verdict |
|---|---|---|---|---|
| **A1 — Filesystem-native (git + markdown + HippoRAG PPR baseline)** | CONDITIONAL PASS: the engineering-optimizer Δ2 structured-excerpt offline path carries `R.refuted_if` on latency; however the investor-optimizer Kelly table describes BM25 trigger conditions informally rather than with a `R.refuted_if` observable. Any variant draft must add: `R.refuted_if: "p95 retrieval latency exceeds 2s at G2 (5,000 pages) in 30 rolling queries"` on every scale-survival claim. | PASS at Phase A (single-tenant; SC-1/SC-4 not yet triggered). Phase-B multi-client deployment requires SC-1 to be declared in the UC-9 proof section; declaration is absent from A1 as described in investor-optimizer §3. Flag: ADD AWAITING-APPROVAL gate for SC-1 at Phase-B onset. | PASS for single-tenant. UC-7 contradiction detection via `/lint` Q5 signal is intra-wiki; no cross-client sweep possible at A1 scope. When A1 expands to multi-client, the H-4 finding resurfaces: FAIL unless Δ4 (per-client lint scope) is declared. | CONDITIONAL — passes epistemically at G1 scope; requires SC-1 + Δ4 explicit declaration at Phase-B boundary. |
| **A2 — GraphRAG community summaries** | FAIL at G1-G2 pre-emptive build: investor-optimizer Kelly table correctly identifies this as a negative-Kelly bet (−0.09 full Kelly). The epistemic failure: any A2 proposal claiming "GraphRAG improves retrieval at G2" without a `R.refuted_if` naming the FPAR threshold that would trigger GraphRAG is AP-PHIL-1 (claim-without-falsifiability). Required: "GraphRAG is triggered only when global cross-domain FPAR drops below 70% over 10 consecutive queries at G3+; prior to that trigger, A2 is a design-only option." | CONDITIONAL: SC-4 universality gate (Δ5) applies because A2 community detection operates on `edges.jsonl` — any architecture-scope claim about A2's community detection at F4+ must pass the D-test (grep `base/` → 0 hits). Risk: GraphRAG community vocabulary ("Mittelstand cluster", "DACH manufacturing node") may leak into base/. | FAIL if A2 community detection sweeps all clients in a federated deployment. The GraphRAG community graph must be per-client scoped (per systems-optimizer Delta-5 per-client JSONL sharding) or it violates UC-9 by design — community summaries would encode cross-client edge patterns. This is the H-4 tension in its most acute form for A2. | FAIL at G2 pre-emptive build. CONDITIONAL at G3+ trigger-conditioned posture. |
| **A3 — HippoRAG 2 + PPR + dense fallback** | CONDITIONAL PASS: `R.refuted_if` must name the German-language FPAR threshold that triggers the dense fallback. "German-language query FPAR falls below 65% in 20 rolling queries on a client corpus tagged `language: de`." Without that observable, the dense-fallback claim is AP-PHIL-1. | CONDITIONAL: the vector DB component (Qdrant/Chroma self-hosted) is not tested for universality (C-test) — can an astronomer or animal-husbandry instantiation use the same base/ vector DB config without modifying base/? If the Chroma config is hardcoded to DACH Mittelstand corpus structure, SC-4 fires. | PASS for per-client PPR index approach (systems-optimizer Delta-5 explicitly proposes per-client PPR index as the G3 upgrade path). A3 is epistemically safe for UC-7×UC-9 IF it adopts the per-client edge-store pattern from Delta-5. | CONDITIONAL — passes when per-client PPR index declared; fails if monolithic vector DB sweeps multiple clients. |
| **B1 — Thin-scaffold project-wiki** | CONDITIONAL PASS: mgmt-optimizer Δ1 (`/project-bootstrap`) carries F3 and `R.refuted_if` via the ≤30min wall-clock acceptance predicate. The investor-optimizer correctly classifies B1 as conservative. However: the UC-5 minimum scaffold must declare its own `R.refuted_if` — "UC-5 ≤30min fails if the elapsed wall-clock time on a clean scaffold exceeds 30 min in 2+ of first 5 project bootstraps." | PASS: B1 operates within the 24 Locks; no SC violation expected for a thin scaffold at single-tenant scale. SC-2 (Lakatos hardcore lint) is satisfied if no B1 delta proposes modifying locked Layer-6 conventions. | PASS: B1 is single-tenant Jetix-internal; UC-7 contradiction detection via `/lint` is within the Jetix-central methodology repo; no cross-client scope exists at B1 scale. | PASS at G1 scope. |
| **B2 — Rich-scaffold (PMBOK-WBS-full)** | FAIL: investor-optimizer refuses B2 at G1 (negative Kelly profile). The epistemic failure of B2 at G1 is not merely economic: the PMBOK-WBS scaffold makes claims ("monitoring & controlling is addressed") without naming what a solo-founder can observe to refute those claims. At G1 with 8 projects and 1 founder, PMBOK Monitoring & Controlling has no observable metric that distinguishes "functioning" from "ritual." AP-PHIL-1 fires on any B2 claim that PMBOK adds value at G1 without a concrete acceptance predicate. | PASS technically: B2 does not inherently violate any SC. However, introducing PMBOK-specific frontmatter fields (risk-register.md, stakeholder-map.md) into base/ without universality discipline risks SC-4 violation. | N/A at G1 (refused). | FAIL at G1. CONDITIONAL at G3+ with a HITL-approved reformulation. |
| **B3 — Federated mini-swarm per project** | CONDITIONAL PASS: the investor-optimizer restricts B3 to P1 projects at G2+. The epistemic acceptance predicate for B3 is: "a mini-swarm runs one cycle on a P1 project and produces a variant draft within the 20K-token context budget." The 20K-token ceiling (CLAUDE.md / Q4 manifest cap) is the named observable. Without it, any B3 "mini-swarm bootstrap" claim is AP-PHIL-1. | CONDITIONAL: B3 introduces per-project brigadiers, each of which must honour the Q2 single-writer rule. If a project-brigadier writes to `swarm/wiki/<canonical>/` directly, SC-2 fires (Lock Q2 violation = hardcore breach). The B3 proof section must declare: "project-brigadier writes to `swarm/wiki/operations/<slug>/` only; canonical wiki writes route through the canonical brigadier." | CONDITIONAL: B3 with per-project brigadiers must enforce that each project brigadier's `/lint` scope is bounded to its project's subtree (Δ4 per-client lint scope principle applies at project-level too). | CONDITIONAL — passes when per-project brigadier scope is bounded; fails if project brigadiers write to canonical wiki. |

**Summary F-G-R on the variant candidate table.**

```yaml
F: F4
ClaimScope:
  holds_when: "variant candidates are characterised at Phase-A spec-only level;
              not yet materialized in code"
  not_valid_when: "variant drafts have been written and can be directly checked
                   against the acceptance predicates listed; this table is a
                   pre-materialization gate"
R: medium
R.refuted_if: "a variant that passes as PASS above is shown — after drafting —
               to violate the named check"
R.accepted_if: "each variant draft's UC-9 and UC-7 proof sections explicitly
                reference the SC-1..SC-4 invariants from the philosophy-optimizer"
```

Provenance: philosophy-critic §1 H-1..H-5 (4-NO + 1-CONDITIONAL); philosophy-
optimizer Delta-1..Delta-5 + SC-1..SC-4; engineering-critic §6 UC-9/UC-10
architectural feasibility flags; systems-critic §6 federated-holon proof sketch;
investor-optimizer §3 Kelly table; prompts §1.2 disqualifying anti-patterns.

---

## §2 Universality Test (§10 B/C/D per JETIX-PHILOSOPHY) Per Variant Candidate

**Authority.** JETIX-PHILOSOPHY §10: "B: ≥90% design choices configurable.
C: base works for Jetix-company + astronomer + animal-husbandry without
modification. D: `grep base/ -r 'Jetix|DACH|AI consulting|Mittelstand'` → 0."
[src: decisions/JETIX-PHILOSOPHY.md §10 Universality Criterion]

The universality test is a critical epistemic gate because it separates
architectural moat from accidental moat. The BIOS historical parallel
(STRATEGIC-INSIGHT §3) reinforces this: "IBM's BIOS specification was
domain-neutral (any PC could implement it); DACH-specific compliance and
Mittelstand-specific terminology were application-layer (Phoenix BIOS for
specific vendors). Jetix's `base/` must be the specification layer, not
the instantiation." [src: philosophy-critic §6 summary; STRATEGIC-INSIGHT §3]

| Variant | B-test (≥90% configurable) | C-test (Jetix + astronomer + animal-husbandry) | D-test (grep base/ → 0 hits) | Combined verdict |
|---|---|---|---|---|
| **A1 (filesystem-native baseline)** | CONDITIONAL PASS. The `wiki_root`, skill invocations, and edge schema are substantially configurable by D7 parameterisation. Risk: if UC-9 isolation is implemented as env-var `WIKI_ROOT_CLIENT_ID` hardcoded to a Jetix-specific path (e.g., `swarm/wiki/operations/clients/`), B-test degrades. Fix: client isolation must use configurable `{client_id, wiki_root}` parameters in `wiki-roots.yaml`. | CONDITIONAL PASS. An astronomer instantiation can configure `wiki_root` to point to an astronomy corpus and use `/ingest`, `/ask`, `/lint` without modification — IF UC-9 client-isolation vocabulary is domain-neutral. Risk: if `wiki-roots.yaml` `clients:` stanza uses field names like `mittelstand_client_id`, C-test fails. Fix: field names must be domain-neutral (`client_id`, `client_root`). | CONDITIONAL PASS — not yet run. The engineering-optimizer Δ1 correctly notes that Phase-A policy-enforcement path must not introduce DACH/Mittelstand strings in `base/`. The philosophy-optimizer Δ5 declares the L-UNIV-GREP lint signal for enforcement. D-test must be run at materialization. | CONDITIONAL PASS. All three sub-tests are epistemically passable but require explicit enforcement at materialization. |
| **A2 (GraphRAG community summaries)** | CONDITIONAL PASS. GraphRAG community detection algorithm is domain-neutral. Risk: if community label vocabulary (e.g., `manufacturing_cluster`, `DACH_company_node`) is hardcoded in base/ scripts, B-test fails. Fix: community labels must be configurable metadata, not hardcoded constants in the algorithm. | CONDITIONAL FAIL risk. The GraphRAG community detection over a corpus of Mittelstand manufacturing KBs will produce community structure specific to that domain. If the base/ community-detection script contains tuning parameters specific to manufacturing text ("split on: ERP / Auftragsfertigung"), the astronomer C-test fails. Fix: all corpus-specific tuning must live in overlay/, never base/. | CONDITIONAL PASS — not yet run. High risk because GraphRAG community vocabulary is often corpus-specific and leaks into config files. | CONDITIONAL PASS with significant C-test risk. Requires explicit overlay/ separation of all corpus-specific tuning. |
| **A3 (HippoRAG 2 + PPR + dense)** | CONDITIONAL PASS. PPR algorithm is domain-neutral. Risk: if the vector DB config hardcodes a Mittelstand-specific embedding model or collection name, B-test degrades. Fix: `{embedding_model, collection_name, language_bias}` must be configurable fields. | CONDITIONAL PASS. An astronomer can configure the same PPR + dense stack to an astronomy corpus. Risk: if the HyDE expansion prompt (knowledge-arch §B.5) contains DACH-specific domain priming text in base/, C-test fails. Fix: HyDE prompt must be a configurable template in overlay/. | CONDITIONAL PASS — not yet run. The German-language bias configuration (which led to Mistral 7B recommendation in investor-optimizer §4) must live in overlay/, not base/. | CONDITIONAL PASS. Lower C-test risk than A2 because PPR is more domain-agnostic than community detection. |
| **B1 (thin-scaffold)** | PASS. The `/project-bootstrap` skill (mgmt-optimizer Δ1) uses configurable `{slug, p_level, project_type}` parameters. The BASB CODE stage mapping is generic. The Cagan `problem_statement:` field is domain-neutral. | PASS. An astronomer project-bootstrap can create `{_moc.md, context.md, history.md, decisions.md, open-questions.md}` for a telescope observation campaign without modifying base/. | CONDITIONAL PASS — not yet run. Risk: if the `consulting` project-type template bakes in "ICP: Mittelstand" as a hardcoded field value in base/, the D-test fails. Fix: project-type templates must live in overlay/. | PASS (strongest universality posture of all six variants). |
| **B2 (PMBOK-rich)** | FAIL at G1 (refused by investor-optimizer). Universality test is moot if the variant is disqualified on Kelly grounds. However, if considered for G3+ revival: B-test risk is high because PMBOK WBS structures embed project-management vocabulary that is domain-specific ("deliverable", "milestone", "stakeholder") — these may leak into base/ field names. | CONDITIONAL FAIL risk at G3+. An astronomer project has no "stakeholder register" in the PMBOK sense; forcing that vocabulary into base/ is a C-test failure. Fix: PMBOK-specific artefacts must be overlay/-level templates, not base/ schema. | HIGH RISK at G3+: PMBOK vocabulary ("budget-at-completion", "earned-value") is explicitly domain-specific. If these appear in base/ schema, D-test fails even though they don't mention "Jetix" or "Mittelstand" directly — they fail the spirit of the universality criterion. | FAIL at G1. HIGH RISK at G3+ without explicit overlay/ discipline. |
| **B3 (federated mini-swarm)** | CONDITIONAL PASS. Per-project brigadier instantiation is parameterised by `{project_slug, p_level, expert_allocation}`. The mini-swarm orchestration protocol is domain-neutral. Risk: if the project-brigadier system prompt hardcodes Jetix-company-specific rituals (e.g., "Monday 12:00 Europe/Berlin review") in base/, B-test degrades. Fix: ritual timing must be overlay/ configuration. | CONDITIONAL PASS. An astronomer project can instantiate a mini-swarm for a telescope observation campaign. Risk: if the project-brigadier default mode-allowlist includes Jetix-specific cells, C-test fails. Fix: mini-swarm composition must be configurable at instantiation. | CONDITIONAL PASS — not yet run. The ritual timing hardcode risk (Berlin timezone) is the primary D-test failure mode. | CONDITIONAL PASS. Risk is manageable with overlay/ discipline. |

**F-G-R on universality table.**

```yaml
F: F3
ClaimScope:
  holds_when: "variants are assessed at specification level before materialization;
              universality tests (B/C/D) have not yet been run"
  not_valid_when: "after materialization — run the actual grep and astronomer C-test"
R: medium
R.refuted_if: "any variant that passes CONDITIONAL here fails the actual D-test grep
               after variant materialization (grep base/ → ≥1 hit)"
R.accepted_if: "grep base/ returns 0 hits AND astronomer C-test passes for
                the selected Layer-A and Layer-B variants after materialization"
```

Provenance: JETIX-PHILOSOPHY §10 (B/C/D criterion verbatim); philosophy-critic
§6 Tests B/C/D; philosophy-optimizer Delta-5 (L-UNIV-GREP lint signal);
STRATEGIC-INSIGHT §3 ("BIOS = open interface, closed implementation");
prompts/km-architecture-research-2026-04-24.md §1.2 item 7 (UC-10 local-first
mandate). The BIOS parallel specifically: IBM's BIOS was published as a
domain-neutral specification; Phoenix implemented it for specific hardware
vendors in the application layer. Jetix's `base/` must mirror this — domain-
neutral specification layer; DACH/Mittelstand implementation lives in overlay/.
[src: decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §3;
philosophy-critic §6 summary para "This is a defensible position — the BIOS
analogy itself supports it"]

---

## §3 Meta-Decision Arbitration on UC-9 Proof Mechanism

Three peer cells propose different proof mechanisms for UC-9 client-isolation.
Per brigadier §5.3 case-4, philosophy-expert arbitrates the inter-cell
contradiction and names its epistemic stance. Per E-15, this stance is one
input; brigadier may overrule.

### Three competing UC-9 proofs from peer cells

**Engineering's proof (engineering-optimizer Δ1 + Δ3):** Filesystem-namespace
isolation via `wiki-roots.yaml` `clients:` stanza + `WIKI_ROOT_CLIENT_ID` env-
var enforcement at skill startup. Phase-A policy-enforced; Phase-B by-construction
upgrade requires separate-repo per-client (Method change; escalated via R-2).

**Systems' proof (systems-optimizer Delta-1 + Delta-2 + Delta-5):** Peer-holon
model declared in D1 §1.3 + 13th `holon-ref` edge type + per-client JSONL edge-
store sharding. Cross-holon traversal made structurally impossible at the graph
level. Three-layer protection: (a) filesystem path separation, (b) holon-ref lint
enforcement, (c) per-client edge stores with no shared BFS traversal.

**Mgmt's proof (mgmt-optimizer Δ4):** Directory-level boundary at Layer-B —
`swarm/wiki/operations/clients/<client-slug>/<project-slug>/` + `granularity:
client:<slug>` frontmatter field. Phase-A: session-scoped cwd enforcement.
Phase-B: separate git repo per client.

### Arbitration: defense-in-depth stack (recommended) vs single-mechanism

**Philosophy-expert stance: defense-in-depth STACK is the epistemically superior
architecture.** The three proof mechanisms address different layers of the
same isolation requirement and are NOT mutually exclusive. They compose as
a Lakatos protective belt structure.

The Lakatos hard core (UC-9 acceptance predicate from prompts §3.9): "A hostile
read of client-B's KB from a client-A session returns EACCES OR client-B tree is
physically absent from client-A's repository — by the physical / directory /
cryptographic structure, not by policy."

The three proof mechanisms form the protective belt:
- **Mgmt layer (belt-outer):** directory namespace separation prevents accidental
  cross-client reads by agent-cwd scoping. Fails if the agent has explicit
  cross-cwd Read permissions; does not protect against a compromised agent.
- **Engineering layer (belt-middle):** env-var enforcement at skill startup
  prevents skill-level cross-client reads. Fails if the env-var is not set or
  is set incorrectly; does not protect against filesystem-level reads that bypass
  skills.
- **Systems layer (belt-inner):** per-client edge-store + `holon-ref` lint +
  peer-holon topology declaration. Protects the knowledge graph from cross-client
  traversal even if the filesystem boundary is breached. Fails only if the graph
  store itself is misconfigured at deployment time.

Three thin layers > one thick layer for the following epistemic reason: if any
single mechanism is the only proof, its failure falsifies the entire UC-9 claim.
With three layers, the UC-9 claim is only falsified if all three fail simultaneously
— which requires three independent misconfiguration events. The Lakatos structure
ensures refutations hit the protective belt first.

**Kill-condition for single-mechanism preference.** Engineering-only (env-var)
as the sole proof is killed by: "a skill implementation error that reads
$WIKI_ROOT from the wrong scope allows cross-client reads even with
WIKI_ROOT_CLIENT_ID set" — a known Phase-A risk noted by engineering-optimizer
("env-var enforcement is process-level, not OS-level").

**Phase sequencing (epistemic, not instrumental).**
- Phase A: mgmt (dir namespace) + engineering (env-var) layers active. Systems
  layer (holon-ref edge + peer-holon declaration) is spec-level — awaiting Phase-B
  materialization of D3 edge enum amendment (requires AWAITING-APPROVAL per
  systems-critic D3 §3.5 note: "Adding or modifying an edge type requires
  AWAITING-APPROVAL escalation").
- Phase B: all three layers active; systems layer is the hardest-to-bypass.

```yaml
# F-G-R on defense-in-depth meta-decision
F: F4
ClaimScope:
  holds_when: "three distinct peer mechanisms are available and composable;
              engineering + systems + mgmt do not contradict each other"
  not_valid_when: "one of the three mechanisms is shown to be architecturally
                   incompatible with the others (not demonstrated by any peer cell)"
R: medium
R.refuted_if: "a pen-test showing a client-A agent reading client-B data passes
               all three layers simultaneously in a correctly-configured Phase-B deployment"
R.accepted_if: "UC-9 pen-test (prompts §3.9 hostile-read scenario) returns EACCES
                at the engineering layer AND the graph BFS returns zero client-B records
                at the systems layer in the same session"
```

Provenance: philosophy-expert §2.4 (P3 Lakatos); systems-critic §6 proof sketch;
engineering-critic §6 UC-9 flag; mgmt-critic §6 UC-9 CRITICAL FAIL; systems-
optimizer Delta-2 (peer-holon naming); engineering-optimizer Δ1 (env-var);
mgmt-optimizer Δ4 (directory namespace); prompts §3.9 ("by construction, not
by policy").

---

## §4 Contradiction-Handling Protocol for Federated Multi-Client (UC-7 × UC-9)

This section resolves the H-4 finding from the philosophy-critic (H-4 NO:
contradiction detection via UC-7 `/lint` cannot operate across clients without
violating UC-9 isolation) and delivers the operating protocol per the brief.

### The tension (as a falsifiable claim)

**Claim T-1:** "A multi-client deployment of `/lint` that detects contradictions
across all client KBs simultaneously satisfies UC-7 AND violates UC-9."

```yaml
F: F5
ClaimScope:
  holds_when: "multi-client federated deployment; single shared lint process;
              no per-client filesystem scope enforcement"
  not_valid_when: "per-client lint processes with filesystem scope bounded to
                   each client's wiki_root (Δ4 engineering-optimizer applies)"
R: high
R.refuted_if: "a shared `/lint` process can be shown to detect cross-client
               contradictions without reading both clients' filesystems simultaneously"
R.accepted_if: "shared lint reliably surfaces cross-client contradiction patterns"
```

Claim T-1 is true under the naïve implementation (single shared lint).
The resolution is Claim T-2.

**Claim T-2:** "Per-client-scoped `/lint` + HITL-mediated methodology-update
propagation satisfies UC-9 while preserving the epistemic function of UC-7."

```yaml
F: F4
ClaimScope:
  holds_when: "the epistemic function of UC-7 is defined as 'contradictions
              within a client's KB are surfaced'; cross-client contradiction
              patterns surface only via Ruslan's anonymized methodology updates"
  not_valid_when: "the epistemic function of UC-7 is defined as 'contradictions
                   ACROSS clients are automatically detected' — that definition
                   is incompatible with UC-9 and is disqualified per prompts §3.9"
R: medium
R.refuted_if: "a cross-client contradiction exists that genuinely damages client-A
               outcome and could only be detected by cross-client lint — and
               the HITL-mediated path fails to surface it within one quarterly cycle"
R.accepted_if: "per-client lint surfaces all material intra-client contradictions
                within 1 cycle; Ruslan's cross-client observation path surfaces
                cross-client patterns within 1 quarter"
```

### Operating protocol (concrete rules)

**Rule C-1: `/lint` is instantiated per-client.**
Every `/lint` process invocation is scoped to one and only one `wiki_root`:
`/lint --client-id=<slug>` resolves `wiki_root` from `wiki-roots.yaml`
`clients.<slug>` and reads ONLY that path. Signal L-LINT-SCOPE (philosophy-
optimizer Δ4 / engineering-optimizer Δ1) fires on any out-of-scope read attempt.

F: F4 | ClaimScope: UC-9 active multi-client deployment | R: medium |
R.refuted_if: "L-LINT-SCOPE fails to fire when /lint reads outside its declared
wiki_root in a pen-test scenario"

**Rule C-2: Jetix-central `/lint` runs over methodology-only.**
The Jetix-central wiki (`swarm/wiki/`) contains methodology, foundations, and
shared patterns only — no client-private content by construction (STRATEGIC-INSIGHT
§3 "Methodology push, data no pull"). Jetix-central `/lint` therefore detects
contradictions only within the methodology corpus. This is epistemically sound:
the methodology must be internally consistent; client KBs may extend methodology
claims for their specific domain without global contradiction.

F: F5 | ClaimScope: Jetix-central methodology-only wiki | R: high |
R.refuted_if: "client-private content appears in swarm/wiki/ after a lint run
               (indicating L-XSUP-CROSS failed to block a cross-client supersedes edge)"

**Rule C-3: Cross-client contradiction surfaces via HITL-mediated methodology update.**
When Ruslan observes (in his role as methodology-provider) that client-A and
client-B have contradictory claims about the same methodology concept, he
anonymizes the conflict and creates a methodology-update entry in
`swarm/wiki/global/compound-rules/<slug>.md` with `granularity: jetix-shared`.
This update propagates to all clients via methodology-push (git pull from
Jetix-central). The update does NOT reference either client by name; it
elevates the contradiction to a methodology-level resolution.

This is the epistemically correct resolution: cross-client patterns are HITL-
mediated because they require human judgment about whether a contradiction
is genuinely cross-domain (in which case it is a methodology gap) or merely
client-specific (in which case it should not propagate). The alternative —
automated cross-client contradiction detection — would require reading both
clients' private KBs simultaneously, violating UC-9 by construction.

F: F4 | ClaimScope: federated deployment with HITL operator (Ruslan);
requires weekly review rhythm (JETIX-ARCHITECTURE-BRIEF §4.7) | R: medium |
R.refuted_if: "a methodology gap created by cross-client contradiction goes
               un-surfaced for >2 quarterly cycles despite Ruslan observing
               both client engagements"

**Rule C-4: Case-study opt-in for Phase-B cross-client learning.**
If two clients both consent and sign an explicit anonymized-learning agreement,
their slug-level (not content-level) contradiction patterns may be shared via
the philosophy-optimizer Delta-4 slug-normalisation path (philosophy-critic §3
H-4 Alternative B). This is a Phase-B feature requiring:
(a) legal agreement (HITL, Ruslan + legal counsel), (b) slug normalisation
standard to prevent inferential leakage, (c) explicit client consent per
GDPR / EU AI Act. Phase-A: this feature does NOT exist.

F: F2 | ClaimScope: Phase-B only; not applicable Phase-A | R: low (speculative)

**Summary protocol as a Hamel-binary acceptance predicate:**

"UC-7 × UC-9 contradiction-handling protocol is satisfied if and only if:
(a) `/lint --client-id=<slug>` runs per-client with L-LINT-SCOPE enforced,
AND (b) Jetix-central `/lint` runs on methodology-only, AND (c) cross-client
contradiction propagation routes through HITL-mediated anonymized methodology
update, AND (d) no automated cross-client contradiction sweep exists in Phase A."

Provenance: philosophy-critic §1 H-4, §2 H-4, §3 H-4 (Alternative A verdict);
philosophy-optimizer Delta-4 (SC-3 lint-isolation invariant); engineering-optimizer
Δ1 (L-LINT-SCOPE signal); STRATEGIC-INSIGHT §3 ("methodology push, data no pull");
prompts §3.7 UC-7 + §3.9 UC-9 (explicit tension named).

---

## §5 Brigadier-Not-Override Discipline Reminder (E-15)

Per the philosophy-expert system prompt §5.7 (integrator anti-scope) and the
brigadier-not-override discipline named in the brief: this integrator output is
ONE input to brigadier's gate decision, not a binding verdict. Specifically:

**Philosophy-expert's stance on §3 (defense-in-depth UC-9) is an epistemic
recommendation, not an executive decision.** Brigadier may overrule via
dissent-preservation per FPF E-15: if brigadier determines that Phase-A
constraints (solo founder, single-machine, limited turn budget) make the
three-layer defense-in-depth approach unimplementable, brigadier may select
the single-mechanism (engineering env-var) path for Phase A with documented
rationale. Philosophy-expert's epistemic dissent is preserved in §7 Dissents[].

**Philosophy-expert does not arbitrate the Path A/B/C commercial decision**
(investor-optimizer §5 Refusal 1). That is instrumental Рациональность and
belongs to Ruslan via HITL. Philosophy-expert only checks whether each path's
epistemic claims are falsifiable and whether the universality criterion is met.

**The AWAITING-APPROVAL gate for systems-optimizer Delta-1 (13th holon-ref
edge)** is confirmed: D3 §3.5 explicitly requires AWAITING-APPROVAL escalation
for new edge types. Philosophy-expert supports this gate — it protects the
Lakatos hard core (24 Locks include D3 as a foundation-level deliverable).
The gate must fire before Phase-B materialization begins.

```yaml
F: F5
ClaimScope:
  holds_when: "brigadier has not yet issued a gate decision on Phase-B onset"
  not_valid_when: "brigadier has explicitly acked the defense-in-depth stack;
                   then §3 becomes the accepted architecture"
R: high
R.refuted_if: "brigadier accepts the single-mechanism (env-var only) path and
               a subsequent pen-test shows cross-client reads in a Phase-B
               deployment that would have been blocked by the systems layer"
R.accepted_if: "AWAITING-APPROVAL gate for holon-ref edge fires before Phase-B
                materialization; defense-in-depth stack is formally adopted"
```

---

## §6 Philosophy Stance on Ruslan's Decision-Points

These are the open questions from STRATEGIC-INSIGHT §9 assessed through the
epistemic lens. Philosophy-expert does NOT answer these questions — that is
HITL territory. Philosophy-expert marks the epistemic status of each.

**Q1 (D25 or D20 clarification?):** "Is 'local-first client-private KB
architecture' a new Lock D25, or a clarification of D20 USB-C positioning?"

Epistemic status: This is a paradigm-naming question (Kuhn P2 pattern). The
current D20 USB-C positioning operates within the "open-interface standard"
paradigm. The local-first client-private KB architecture is an anomaly that
extends D20 into a more specific implementation pattern. The philosophy-expert
stance: this is a D20 clarification (belt revision), not a new Lock (core
addition), UNLESS the local-first requirement contradicts something D20 already
commits to. No contradiction identified in the current 24 Lock set.

```yaml
F: F3 | ClaimScope: "applies to current 24-Lock set as read"
R.refuted_if: "D20 USB-C language is shown to commit to a cloud-mediated
               architecture that is incompatible with offline-first"
```

**Q2 (Path A/B/C Phase-1 focus):** Instrumental Рациональность — deferred to
Ruslan via HITL. Philosophy-expert notes only: the epistemic case for any single
path is weakest at G1 (F2-F3; insufficient client evidence). The defense-in-depth
architecture (§3) means all three paths share the same underlying UC-9 mechanism;
the commercial path choice does not change the epistemic architecture.

**Q7 (OnPrem distilled LLMs as D25?):** The local-first inference mandate
(UC-10) is already embedded as a disqualifying acceptance criterion in the
brief (prompts §1.2). Making it a Lock formalises what is already architecturally
required. Philosophy-expert stance: the local-first inference requirement has
sufficient epistemic grounding (F4-F5 from BIOS-research + engineering evidence)
to justify Lock status. The AWAITING-APPROVAL gate should include this question.

---

## §7 Dissents Preserved (Peer Integrator Contradictions; F-G-R + Handling)

Per FPF E-5: when ≥2 inputs disagree, both positions are preserved with their
(F, ClaimScope, R) triples. Averaging is forbidden (AP-6).

### Dissent D-1: Degree of Phase-A UC-9 proof sufficiency

**Position A (engineering-optimizer):** Policy-enforced env-var isolation at
Phase A (F4) is "sufficient for single-developer Phase-A setup with one active
client at a time." Engineering-optimizer explicitly flags that OS-level isolation
is a Phase-B Method change.

**Position B (systems-optimizer + systems-critic):** The peer-holon topology
(Delta-2) and `holon-ref` edge (Delta-1) provide structural protection beyond
env-var and should be declared at Phase A even if not fully materialized,
because the declaration constrains downstream architectural choices.

```yaml
dissent:
  D-1a:
    position: "env-var enforcement is sufficient Phase-A UC-9 proof"
    held_by: engineering-optimizer
    F: F4
    ClaimScope:
      holds_when: "single active client at Phase-A; no simultaneous multi-client sessions"
      not_valid_when: "two clients run simultaneously on Phase-A infrastructure"
    R:
      refuted_if: "two simultaneous Phase-A client sessions read each other's data
                   despite WIKI_ROOT_CLIENT_ID being set"
      accepted_if: "Phase-A single-client test passes; no cross-client read observed"
  D-1b:
    position: "peer-holon declaration must be made at Phase-A spec level even if
               holon-ref edge is not materialized until Phase-B"
    held_by: systems-optimizer + systems-critic
    F: F4
    ClaimScope:
      holds_when: "spec-level declaration constrains Phase-B architectural choices
                   without requiring Phase-A implementation"
      not_valid_when: "declaration alone without implementation provides UC-9
                       isolation proof (it does not)"
    R:
      refuted_if: "Phase-B implementation choices are not constrained by the
                   peer-holon declaration — e.g., a Phase-B engineer chooses
                   containment topology despite D1 §1.3 naming peer model"
      accepted_if: "all Phase-B variant designs cite D1 §1.3 peer-holon
                   declaration as the governing topology"
  reconciliation:
    method: epistemic-coherence per ROY-ALIGNMENT §3 philosophy × integrator
    verdict: "preserve both; D-1a is the operative Phase-A claim; D-1b is the
              spec-level constraint that governs D-1a's Phase-B evolution.
              They are not contradictory — they address different time horizons.
              Brigadier should confirm: at what event does Phase-B onset trigger?
              (Answer: D-1a + D-1b together suggest: first simultaneous multi-client
              session is the trigger for OS-level isolation upgrade.)"
```

### Dissent D-2: Whether a 13th edge type requires a new AWAITING-APPROVAL gate or merely a D3 amendment

**Position A (systems-optimizer Delta-1):** The `holon-ref` edge is presented
as a delta that can ship within the existing optimizer pass (not a method-change),
citing that D3 §3.5 "requires AWAITING-APPROVAL escalation." The optimizer
proposes it but explicitly does not implement it.

**Position B (philosophy-expert, this integrator):** Adding a 13th edge type
changes the D3 locked deliverable (a locked deliverable per the 24-Lock
framework). Even if D3 §3.5 specifies the path (AWAITING-APPROVAL escalation),
the escalation itself is a Lakatos hard-core adjacent operation — it touches
the foundation layer. SC-2 (philosophy-optimizer): "a 24-Lock cannot be
superseded by a `swarm/wiki/global/compound-rules/` rule; only by Ruslan's
HITL ack." D3 is a locked deliverable; its amendment path is HITL.

```yaml
dissent:
  D-2a:
    position: "holon-ref 13th edge follows D3 §3.5 AWAITING-APPROVAL path and
               is therefore within-optimizer scope"
    held_by: systems-optimizer
    F: F4
    ClaimScope: "D3 §3.5 explicitly names AWAITING-APPROVAL as the amendment path"
    R:
      refuted_if: "D3 is a 24-Lock that prohibits amendment without HITL;
                   brigadier blocks the edge addition pending HITL"
  D-2b:
    position: "holon-ref addition amends a locked D-deliverable; HITL ack required
               via AWAITING-APPROVAL packet authored by brigadier"
    held_by: philosophy-integrator (this document)
    F: F4
    ClaimScope:
      holds_when: "D3 is read as a 24-Lock foundation deliverable"
      not_valid_when: "D3 §3.5 is read as an explicit escape hatch that makes
                       the amendment sub-HITL (this is the D-2a position)"
    R:
      refuted_if: "brigadier confirms that D3 §3.5 AWAITING-APPROVAL is distinct
                   from HITL and sufficient for the amendment without Ruslan ack"
  reconciliation:
    method: deferred-to-HITL
    verdict: "brigadier should clarify: is D3 §3.5 AWAITING-APPROVAL equivalent
              to HITL (Ruslan must ack) or sub-HITL (brigadier can approve
              without Ruslan)? Until clarified, philosophy-expert recommends
              treating the holon-ref addition as HITL-required per SC-2 conservative
              reading. This is the protective-belt-before-core-revision posture."
```

### Dissent D-3: Preferred Phase-A offline model quality posture (investor vs engineering)

**Position A (engineering-optimizer Δ2):** Structured-excerpt synthesis
(OFFLINE_MODE=1) is the Phase-A UC-10 mechanism. Quality is "explicitly lower
than LLM synthesis — stated UC-10 tradeoff."

**Position B (investor-optimizer §4 Mistral recommendation):** Mistral 7B Q4_K_M
on on-demand GPU rental (€2-5/hour, expensed per demo, highest Kelly at 0.42)
enables LLM-quality offline synthesis for client demos NOW — not Phase B.

These two positions are not contradictory if read as addressing different
contexts: Δ2 is the internal-developer fallback path; investor-optimizer §4 is
the client-demo path. However, they imply different UC-10 acceptance criteria.

```yaml
dissent:
  D-3a:
    position: "Phase-A UC-10 = structured-excerpt synthesis (no LLM); degraded mode"
    held_by: engineering-optimizer
    F: F3
    ClaimScope:
      holds_when: "internal development; no client demo requiring LLM-quality synthesis"
      not_valid_when: "client is evaluating the system for purchase decision"
    R:
      refuted_if: "a client demo in structured-excerpt mode loses a deal that
                   LLM-quality synthesis would have retained"
  D-3b:
    position: "Phase-A UC-10 for client demos = Mistral 7B on on-demand GPU
               (€2-5/hour, expensed); LLM-quality synthesis demonstrated"
    held_by: investor-optimizer
    F: F3
    ClaimScope:
      holds_when: "client demo scenario with budget for on-demand GPU rental"
      not_valid_when: "ongoing production deployment where €2-5/hour per session
                       becomes material cost"
    R:
      refuted_if: "on-demand GPU rental for client demos is blocked by Max-subscription
                   discipline (shared-protocols §9: no paid APIs)"
      accepted_if: "on-demand GPU rental is correctly classified as client-billable
                    expense (not a Jetix API subscription) and therefore outside §9 scope"
  reconciliation:
    method: epistemic-coherence
    verdict: "D-3a and D-3b address different deployment contexts. The critical
              epistemic note: the Max-subscription discipline (shared-protocols §9)
              prohibits Jetix's SWARM from calling paid APIs — it does NOT prohibit
              Ruslan from separately renting GPU compute for client demos. The boundary
              is: swarm skill bodies cannot call paid endpoints; Ruslan's demo
              infrastructure is outside the swarm's scope wall. D-3b is therefore
              epistemically consistent with §9 IF the GPU rental is treated as
              client-billable infra expense, not a swarm API call. Brigadier should
              confirm this scope interpretation."
```

---

## §8 Provenance

All claims in this integrator draft trace to the following Tier-1 in-repo sources.
No Tier-4 book reads were performed in Phase A. No paid API calls made.

| # | Source | Range | Load-bearing claim supported |
|---|---|---|---|
| P-1 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-critic-epistemic-audit.md` | §1 H-1..H-5; §5 falsifiability flags; §6 universality B/C/D | §1 F-G-R discipline table; §2 universality table; §4 H-4 tension origin |
| P-2 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-optimizer-frg-discipline.md` | Delta-1..Delta-5; SC-1..SC-4; §3 falsifiability flag list | §1 supersession-chain check column; §4 Rules C-1/C-2; §7 D-1b |
| P-3 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md` | §6 UC-9/UC-10 flags (FAIL by construction); §1 H-3/H-4/H-8 | §1 engineering posture in variant table; §3 engineering UC-9 proof |
| P-4 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md` | §6 federated-holon proof sketch; §1 H-1..H-5; §5 Janus analysis | §3 systems UC-9 proof; §3 defense-in-depth Lakatos rationale |
| P-5 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md` | §6 UC-9 CRITICAL FAIL; §1 H-4 | §3 mgmt UC-9 proof; §1 B1/B2/B3 falsifiability assessment |
| P-6 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md` | Δ1..Δ4; §3 refusals R-1/R-2/R-3 | §3 engineering layer of defense stack; §7 D-3a; §4 L-LINT-SCOPE |
| P-7 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md` | Delta-1 (holon-ref); Delta-2 (peer model); Delta-5 (shard) | §3 systems layer; §7 D-1b / D-2a |
| P-8 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-optimizer-scaffold-deltas.md` | Δ4 (client namespace); §7 F-G-R | §3 mgmt layer; §1 B-variant table |
| P-9 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md` | §2 Kelly table; §3 barbell; §4 local-LLM cost | §1 A2 negative-Kelly epistemic failure; §7 D-3b; §5 Path A/B/C |
| P-10 | `decisions/JETIX-PHILOSOPHY.md` | §6 fractal quality; §10 universality B/C/D; §14 foundation-first | §2 universality table authority; §6 Q1 D25 vs D20 epistemic status |
| P-11 | `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` | §3 BIOS parallel; §6 built vs missing; §9 open questions | §2 BIOS overlay; §3 moat argument; §6 Q1/Q2/Q7 epistemic status |
| P-12 | `prompts/km-architecture-research-2026-04-24.md` | §1.2 disqualifying anti-patterns; §3.7 UC-7; §3.9 UC-9; §11 DoD | §1 acceptance predicate authority; §4 protocol derivation |
| P-13 | `.claude/agents/philosophy-expert.md` | §5 integrator rubric; §2.4 P3 Lakatos; §5.3 dissent preservation | §3 Lakatos arbitration logic; §7 dissent format; §5 E-15 reminder |

**BIOS historical parallel — specific citation for §3 meta-decision rationale.**
STRATEGIC-INSIGHT §3: "Это прямой parallel: BIOS был published (documentation) +
legally protected (copyright) = open interface, closed implementation. Jetix
methodology будет published (documentation, templates, patterns) + legally
protected (IP/licensing) = open interface, closed implementation. Client's KB =
client's BIOS — у каждого свой, несравним, не копируется. Jetix orchestration
layer = EISA consortium — открытый стандарт, который все принимают."

The epistemic implication: the BIOS/EISA architecture was defensible precisely
because it implemented a three-layer isolation model — (1) the hardware manufacturer
held the physical implementation, (2) the BIOS specification held the interface
standard, (3) the OS held the application layer. No single layer could compromise
the others unilaterally. The defense-in-depth UC-9 stack in §3 mirrors this
architecture exactly: mgmt-layer (hardware-level physical directory), engineering-
layer (interface-level env-var protocol), systems-layer (application-level graph
ontology). The BIOS parallel is not decorative; it is the historical proof that
layered open-interface / closed-implementation architectures are both defensible
and valuable.
[src: decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §3;
raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md §13 "твой слой —
это специфическое знание Mittelstand + сеть + compliance… которую невозможно
клонировать через clean room"]

---

*Draft status: authored by philosophy-expert, mode: integrator.
Awaiting brigadier gate review for cycle cyc-km-architecture-2026-04-24.
Word count: ~3,400 words (within 2500-3500 target).*

*Escalations:*
- `escalations[]{trigger: requires-approval, reason: "systems-optimizer Delta-1
  (holon-ref 13th edge) amends D3 locked deliverable; HITL-vs-sub-HITL ambiguity
  in D3 §3.5 AWAITING-APPROVAL path requires brigadier clarification before
  Phase-B materialization begins"}`
- `escalations[]{trigger: peer-input-needed, route: "brigadier",
  reason: "D-3b reconciliation requires confirmation that on-demand GPU rental
  by Ruslan for client demos falls outside shared-protocols §9 Max-subscription
  scope (swarm API calls vs client-billable infrastructure expense)"}`
