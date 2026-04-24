---
title: Philosophy × Scalability — Epistemic Invariants 5-Gate Projection
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
confidence: high
confidence_method: expert-judgment-from-peer-integrator-drafts-and-tier1
tier: tier-1
produced_by: philosophy-scalability
sources:
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-integrator-epistemic-overlay.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - prompts/km-architecture-research-2026-04-24.md
  - .claude/agents/philosophy-expert.md
related:
  - decisions/JETIX-PHILOSOPHY.md
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md
binding_scope: km-architecture-philosophy-scalability-horizon
mode: scalability
---

# Philosophy × Scalability — Epistemic Invariants 5-Gate Projection

> **Purpose.** This document projects the epistemic invariants governing the
> KM architecture (F-G-R discipline; Popperian falsifiability; Lakatos
> hard-core versus protective-belt; supersession-chain consistency; UC-7
> contradiction-detection scope; universality test B/C/D) through five
> horizon gates. It names the $1T-equivalent of peer review, characterises
> the Lakatos hardcore ossification risk at G3–G4, and analyses the epistemic
> integrity of federated multi-client Popperian falsification. Every major
> claim carries an (F, ClaimScope, R) triple. Provenance anchors to Tier-1
> in-repo sources throughout.

---

## §1 Gate G1 (€50K) — Current Phase A: F-G-R / Falsifiability / Lakatos / Supersession / UC-7 / Universality

**BOSC-A-T-X trigger first:** C (Composition) + S (Scale). The swarm
acquires operational governance primitives. The epistemic substrate is
minimal: ~557 Jetix-internal pages, ~572 edges, one Ruslan-operated
instance. [src: prompts §3.8 G1 row; systems-integrator §5.1 Ashby R1 check]

### F-G-R discipline at G1

F-G-R is operable but embryonic. Claims are traceable to source paths
(provenance gate per shared-protocols §2); Ruslan's HITL ack provides the
only reliable F-level attestation above F2. The integrator produced F4-level
claims in this cycle — that ceiling holds because all evidence comes from
specification-level artefacts, not deployed operational data.

```yaml
F: F3
ClaimScope:
  holds_when: "all knowledge claims in swarm/wiki/ are spec-level (G1 Phase-A
              specification artefacts, not materialized operational results)"
  not_valid_when: "first real client session runs and produces empirical data;
                  that data enables F4+ claims on operational behaviour"
R:
  refuted_if: "a Phase-A claim rated F4 is shown to have no traceable source path in
               the provenance table (bare assertion)"
  accepted_if: "every F4+ claim in cycle artefacts carries a non-empty sources[]
                field tracing to a named in-repo file + section"
```

**Falsifiability mechanism at G1.** The primary peer-review mechanism is
HITL (Ruslan) reviewing cycle artefacts before promotion. Epistemic audits
(philosophy × critic) constitute the in-swarm falsifiability mechanism:
claims that fail the §3.1 Conformance Checklist are returned to source cells
with named falsifier requirements. This is one-reviewer peer review at G1 —
structurally equivalent to pre-submission lab internal review, not
journal-grade peer review. F-ceiling is F3–F4; F5+ requires independent
replication. [src: philosophy-expert §2.3 strategies-rule alpha lifecycle;
philosophy-integrator §1 F-G-R discipline table column headers]

**Lakatos hardcore at G1.** The 24 Locks are the hard core. The
protective belt consists of the cycle's proposed deltas (Delta-1 holon-ref
edge, Δ1 wiki-roots.yaml extension, Δ2 offline-mode, etc.). Refutations at
G1 hit the protective belt (parameter choices, skill implementations) before
reaching the hard core. SC-2 (philosophy-optimizer) ensures: a 24-Lock
cannot be superseded without HITL. This is the correct Lakatos posture for
G1: hard core is small, well-named, and defended. [src: philosophy-integrator
§3 defense-in-depth meta-decision — Lakatos protective belt structure;
philosophy-integrator §7 D-2b Lakatos hard-core adjacent operations]

**Supersession-chain coherence at G1.** Single-tenant. Supersession edges
operate within a single `swarm/wiki/` tree. SC-1 (cross-client supersedes
FORBIDDEN) is trivially satisfied: no second client exists. The supersession
chain is coherent by design absence. Risk: undisciplined pre-materialization
claims without `R.refuted_if` create phantom supersession chains that have
no empirical grounding. AP-PHIL-1 fires on any such claim. [src:
philosophy-integrator §1 supersession-chain check column; philosophy-expert
§3.1 check 1 falsifier-named]

**UC-7 contradiction-detection scope at G1.** `/lint` runs over
`swarm/wiki/` globally. UC-7 is unrestricted at G1 because all content is
within a single client (Jetix-internal). Cross-client contradiction detection
is moot (no second client). The operative constraint is that the
contradiction-detection methodology must be per-client-scoped BEFORE the
second client is onboarded — the architecture must enforce this from G1 so
that the scope-narrowing is structural, not a G2 retrofit. [src:
philosophy-integrator §4 Rules C-1/C-2; prompts §3.7 UC-7]

**Universality test at G1.** B-test: `wiki_root` is configurable. C-test
and D-test have not yet been run (`grep base/ → 0 hits` is unverified at
G1). The universality criterion (JETIX-PHILOSOPHY §10) is an aspiration, not
a confirmed property, at G1. The correct epistemic posture: declare the
criterion explicitly, add a D-test lint signal (L-UNIV-GREP per
philosophy-optimizer Delta-5), and run it at first materialization. [src:
philosophy-integrator §2 universality table A1 row]

**Janus risk at G1.** S-A excess: low (single tenant; Jetix-central
monopoly on truth is appropriate at G1 — there are no peer holons to
under-represent). INT excess: low (all knowledge integrates into one graph;
no under-coupling possible). Net Janus verdict: BALANCED at G1.

---

## §2 Gate G2 (€200K) — First External Client: F-G-R / Falsifiability / Lakatos / Supersession / UC-7 / Universality

**BOSC-A-T-X trigger first:** A (Agency). The architecture transitions from
Ruslan-solo to Ruslan + first external client. This is the Phase Promotion
MHT event: Phase A (policy-level client isolation) must upgrade to Phase B
(by-construction isolation via separate git repository per
systems-integrator §4.2 Layer 1). [src: philosophy-expert §6.1 €200K gate;
systems-integrator §7 pairing table "Canonical Phase B"]

### F-G-R discipline at G2

F-level claims can begin to reach F5 at G2: the first client deployment
produces operational data — real ingest runs, real retrieval queries, real
latency measurements. The F-ceiling at G2 is F5 for empirically-grounded
operational claims, F4 for architectural claims about Phase-B isolation
properties (still awaiting pen-test). F3 remains the ceiling for
cross-client pattern-generalization claims (insufficient N).

```yaml
F: F4
ClaimScope:
  holds_when: "first client deployment is operational; at least 3 ingest cycles
              have run; latency measurements are available from UC-2 weekly digest"
  not_valid_when: "first client deployment is still spec-only (no empirical data
                  yet produced)"
R:
  refuted_if: "a G2 claim rated F5 is shown to have no empirical measurement
               source — only an architecture diagram"
  accepted_if: "per-client BFS latency measured at ≤2s p95 on 5,000 pages
               (G2 ceiling per prompts §3.8) across ≥3 weekly digest runs"
```

**Falsifiability mechanism at G2.** Peer review gains a second reviewer:
the first external client's domain feedback (did the wiki answer their
query accurately?) constitutes an external falsification channel. This is
domain-expert peer review — the client's subject-matter expert implicitly
validates or refutes the wiki's synthesis quality. Still below journal-grade
(N=1 client), but structurally better than G1's sole-HITL review. [src:
systems-integrator §5.2 R2 feedback loop — "Client-A's engagement produces
a novel pattern"]

**Lakatos hardcore at G2.** The protective belt expands: Phase-B deltas
(separate-repo per client, ollama + GGUF local-LLM, per-client edge-store
sharding) enter the belt as Phase-B proposals. None touch the 24-Lock hard
core. The AWAITING-APPROVAL gate for holon-ref 13th edge (systems-optimizer
Delta-1) fires at G2 onset — this is the correct Lakatos discipline: a belt
expansion that MIGHT be core-adjacent requires HITL before materializing.
[src: philosophy-integrator §5 AWAITING-APPROVAL gate confirmation;
philosophy-integrator §7 D-2b "treating holon-ref addition as HITL-required
per SC-2 conservative reading"]

**Supersession-chain coherence at G2.** With two active entities (Jetix
methodology and Client-A holon), SC-1 becomes operative: cross-client
supersedes are FORBIDDEN. A methodology update that supersedes a prior
methodology claim propagates to Client-A via git submodule pull — this is
the ONLY permitted cross-holon supersession direction. Client-A's
accumulated claims cannot supersede Jetix-methodology claims without HITL
ack and redaction. The supersession chain coherence predicate: "Every
supersedes edge whose `to` target is in `swarm/wiki/` (Jetix-central) must
have `granularity: jetix-shared` and Ruslan HITL ack." [src:
philosophy-integrator §1 SC-1 supersession check; engineering-integrator §4.3
W-5 Level-2 CE promotion gate]

**UC-7 contradiction-detection scope at G2.** Per-client `/lint` is now
mandatory. Jetix-central `/lint` runs on methodology only. Cross-client
contradiction detection is structurally absent (UC-9 invariant). The
epistemic posture: this absence is a feature, not a gap. Cross-client
contradictions surface only via Ruslan's quarterly cross-engagement review
(Rule C-3 per philosophy-integrator §4). [src: philosophy-integrator §4
Rules C-1/C-2/C-3]

**Universality test at G2.** The D-test must be run before onboarding the
first client: `grep base/ -r 'Jetix|DACH|AI consulting|Mittelstand'` → 0
hits is the acceptance predicate. A failure at G2 means client-specific
vocabulary has leaked into `base/` — a structural embarrassment before the
second client is even onboarded. The lint signal L-UNIV-GREP enforces this
as a by-construction check. [src: philosophy-integrator §2 universality table;
JETIX-PHILOSOPHY §10 D-test verbatim]

**Janus risk at G2.** S-A excess: the Jetix-central brigadier retains
`global/` write access; client data could leak into `global/` if the
`granularity: client:<slug>` gate fails. INT excess: the first client holon
may begin to diverge from Jetix methodology if quarterly promotion rhythm
is too slow. Net Janus: S-A excess is the G2 dominant risk; the
`granularity:` lint gate is the corrective mechanism. [src:
systems-integrator §6 Janus table A1/A2 rows]

---

## §3 Gate G3 (€1M) — Managed Team: F-G-R / Falsifiability / Lakatos / Supersession / UC-7 / Universality

**BOSC-A-T-X trigger first:** T + A simultaneously. Time-horizon shifts
from single-quarter to multi-quarter planning cycles; agency shifts from
solo → delegated → managed. Role-Lift MHT event: Ruslan transitions from
sole operator to managing director of agents. [src: philosophy-expert §6.1
€1M gate; mgmt-integrator §4 B.3 mini-swarm allocation table — P1 projects
get named project-brigadiers]

### F-G-R discipline at G3

With multiple client engagements (N=3–5) and multiple project cycles per
client, statistical patterns become accessible. F-level ceiling rises to F5
for operational claims with ≥10 measurement points across clients. F6
(formal-protocol grounded with replication) becomes achievable for claims
about the methodology's performance characteristics. However: F-levels
above F5 remain dangerous without independent replication (Ruslan is still
the sole reviewer and operator — internal replication only). [src:
philosophy-expert §5.1 F-G-R declaration requirements; philosophy-integrator
§2 worked example ClaimScope "stays in the 1-10 tasks/week range"]

```yaml
F: F5
ClaimScope:
  holds_when: "≥3 client engagements are operational; ≥10 methodology-claims
              have been tested across distinct client contexts"
  not_valid_when: "all evidence comes from a single client; cross-client
                  pattern N is insufficient for generalization"
R:
  refuted_if: "a methodology claim rated F5 produces different outcomes
               across 3 client contexts — indicating ClaimScope was too broad"
  accepted_if: "the claim holds across ≥3 client contexts with independent
                HITL attestation from each engagement"
```

**Falsifiability mechanism at G3.** The team structure provides a new
falsification channel: delegated agents (project-brigadiers, allocated
domain experts) independently test methodology claims when executing
client work. If a delegated agent's output contradicts a methodology claim,
this is an internal falsification event. However: the Kuhnian risk at G3
is that internal falsification is disciplined out ("the methodology says X,
so I'll adjust my report to match X") — this is paradigm-protecting
behaviour. The safeguard is the explicit AP-PHIL-2 detection rule:
paradigm-inconsistency-unflagged. When delegated work silently conforms to
the methodology despite contradictory evidence, this pattern must be flagged
as AP-PHIL-2. [src: philosophy-expert §8 AP-PHIL-2; philosophy-expert §2.4
P2 Kuhn paradigm shift applicable conditions]

**Lakatos hardcore ossification risk at G3 — critical observation.** The
24-Locks become "the way we do things." At G3 with delegated project-
brigadiers operating across multiple client engagements, the hard core
ossification risk emerges: new evidence that genuinely refutes a 24-Lock
claim gets routed around rather than surfaced, because the AWAITING-APPROVAL
gate for Lock amendment is HITL-only (Ruslan must ack) and the cost of
surfacing a hard-core refutation is high. Result: the protective belt
thickens with ad-hoc workarounds rather than the hard core being
legitimately revised. This is the Lakatos degenerate research programme
path. **See §7 for the dedicated ossification safeguard.** [src:
philosophy-expert §2.4 P3 Lakatos applicable conditions; philosophy-expert
§6.1 €1M gate — "axiom to re-derive: all work passes through me"]

**Supersession-chain coherence at G3.** With N=3–5 client holons, the
supersession-chain coherence predicate must be enforced per-client-per-
methodology-version. A methodology update at version v2.3 supersedes
v2.2 claims for ALL client holons — but clients that have not yet pulled
v2.3 operate under a mix of v2.2 methodology + v2.2-era local-patterns.
The coherence risk: a Jetix agent invoked for Client-A operates under
v2.3 methodology; a Jetix agent for Client-B (behind on git pull) operates
under v2.2 methodology; their outputs are incomparable. The supersession-
chain must carry version tags to detect this. Predicate: "every active
client holon declares its current methodology-submodule version in
`foundations/holon-root.md`; `/lint` warns when the declared version is
more than one minor version behind Jetix-methodology HEAD." [src:
systems-integrator §4.2 Layer 1 "separate git repository per client";
engineering-integrator §9 migration path step 7]

**UC-7 contradiction-detection scope at G3.** Per-client lint remains the
operative scope. At G3, however, Ruslan observes cross-client contradictions
more frequently (3–5 client contexts simultaneously). The HITL-mediated
methodology-update path (Rule C-3) becomes a bottleneck: Ruslan must
manually identify, redact, and promote cross-client patterns. The epistemic
risk is that high-frequency cross-client contradiction observations exceed
Ruslan's quarterly review bandwidth, and methodology gaps accumulate
unresolved. The safeguard: a structured cross-client observation log
maintained by Ruslan (not automated lint) that captures anonymized
contradiction patterns for quarterly synthesis. [src: philosophy-integrator
§4 Rule C-3; systems-integrator §11 Dissent D3]

**Universality test at G3.** With N=3–5 clients in different sub-domains
(DACH manufacturing, professional services, research), the C-test becomes
empirically verifiable: "does the same base/ stack serve a Mittelstand
manufacturer and a professional-services firm without modification?" If not,
`base/` has leaked domain-specific assumptions. At G3, the D-test must pass
on the live production `base/` — not just on the spec-level design. [src:
philosophy-integrator §2 universality table — "run the actual D-test grep
after materialization"]

**Janus risk at G3.** S-A excess: methodology ossification — Jetix-central
methodology claim gets protected rather than falsified (described above in
Lakatos section). INT excess: client holons begin to drift from Jetix
methodology if promotion rhythm cannot keep pace with client-specific
learning rate. Net Janus: BOTH risks are elevated at G3. The S-A excess
risk is harder to detect (it manifests as absence of flag, not presence of
error). [src: philosophy-expert §6.2 Janus degraded-mode; systems-integrator
§6 Janus table — "A2: INT excess is the residual risk"]

---

## §4 Gate G4 ($100M) — Multi-Team Organisation: F-G-R / Falsifiability / Lakatos / Supersession / UC-7 / Universality

**BOSC-A-T-X trigger first:** X + C simultaneously. eXternal regulatory
environment activates (EU AI Act enforcement, GDPR supervisory authority
engagement, sectoral compliance for Mittelstand clients); Composition shifts
from single Ruslan-led team to multi-sub-leader organization. Fission MHT
event: sub-org formation and context reframe. [src: philosophy-expert §6.1
$100M gate; strategic-insight §1 "7 structural lessons — infra слой
коммодитизируется; ценность в app layer"]

### F-G-R discipline at G4

At $100M with multiple sub-leaders and clients numbering in the dozens to
hundreds, F-level attestation must itself become formalized. The HITL gate
(Ruslan-acks-all) fails at G4: Ruslan cannot personally attest every
methodology claim across 50+ client engagements. F-level certification must
be delegated — sub-leaders hold F-attestation authority within their domains,
subject to Ruslan's periodic audit. This is the Vincenti taxonomy becoming
operational: "criteria and specifications" (F6) are different from "practical
considerations" (F4); the organization must have specialists for each
knowledge category. [src: philosophy-expert §2.4 P7 Vincenti taxonomy
applicable conditions — "applicable when an integrator-mode synthesis
attempts to merge inputs of different knowledge categories"]

```yaml
F: F5
ClaimScope:
  holds_when: "F5 is the organizational default for methodology claims;
              F6+ requires sub-leader attestation with evidence base ≥20 observations;
              F7+ (formal proof) is rare and requires formal method review"
  not_valid_when: "F6+ claims are asserted without a named sub-leader attestor
                  and an evidence base"
R:
  refuted_if: "a claim rated F6 by a sub-leader is shown — at Ruslan's audit —
               to have been asserted without the ≥20-observation evidence base"
  accepted_if: "F6 claims carry named sub-leader attestor + evidence base ≥20
               in frontmatter's sources[] + Ruslan audit pass rate ≥80%"
```

**Falsifiability mechanism at G4.** External regulatory review becomes a
falsification channel: a BSI C5 or ISO 27001 audit of a client deployment
tests whether the UC-9 architectural claims (client isolation by
construction) hold against adversarial scrutiny. This is institutional
peer-review — the German BSI assessor is not invested in the methodology
being correct. If UC-9 fails a BSI audit, the Lakatos protective belt claim
("per-client separate git repo provides by-construction isolation") is
directly falsified. F-level of UC-9 architectural claim must be raised to
F6 after first successful BSI audit. [src: engineering-integrator §5 UC-10
EU compliance sketch — "a German BSI assessor identifies a data-egress
path... refuted_if"]

**Lakatos hardcore ossification risk at G4 — maximal.** At $100M with
dozens of sub-leaders, the hard core faces the most acute ossification
pressure: the 24-Locks become organizational gospel. A Lock that was correct
at G1 (when Ruslan had all context) may be incorrect at G4 (when the
organizational context has fundamentally changed — Laloux Teal paradigm
applies, per philosophy-expert §6.1 $100M gate "the org's purpose is what
the people inside it act on, regardless of declaration"). Sub-leaders who
identify Lock-refuting evidence face institutional pressure to protect the
hard core. **See §7 for the dedicated ossification safeguard at G3–G4.**
[src: philosophy-expert §6.1 $100M gate paradigm_break; philosophy-expert
§2.4 P3 Lakatos "when assessing whether an epistemic flag requires only belt
revision or genuine core revision"]

**Supersession-chain coherence at G4.** The methodology must now carry
formal versioning (semver or equivalent) because sub-leaders operating
different client clusters may be on different methodology versions. The
supersession-chain coherence predicate must be enforced across the
organization's methodology version matrix: "No client active on methodology
version N-2 or older; sub-leaders are responsible for client upgrades within
one quarter of major version release." The epistemic risk: stale methodology
versions produce claims that have been superseded in HEAD but are still cited
by clients on older versions — creating ghost supersession chains. [src:
systems-integrator §4.2 Layer 1 "client accepts via git pull jetix-central/
methodology"; engineering-integrator §9 Step 7]

**UC-7 contradiction-detection scope at G4.** Automated per-client lint
cannot scale to 100+ client holons with Ruslan-mediated cross-client
synthesis. At G4, slug-normalised cross-client contradiction detection
(philosophy-integrator §4 Rule C-4 / systems-integrator §11 Dissent D3
Alt B) becomes viable if: (a) the Alliance-methodology slug vocabulary
is standardised, (b) a legal framework for anonymized learning is in
place, (c) slug normalisation passes a non-leakage pen-test. This is still
not automated content-level cross-client contradiction detection — it
operates on slug-vocabulary patterns only. The epistemic principle remains:
client-private content is never read cross-client. [src: systems-integrator
§11 Dissent D3 source_2 "At Alliance federation scale, slug-normalised
cross-client contradiction detection becomes viable if..."]

**Universality test at G4.** With 100+ clients across multiple industry
verticals, the universality criterion becomes an organizational quality
standard: a dedicated base/-integrity team runs D-test on every methodology
release. The C-test ("astronomer + Mittelstand + animal-husbandry") must
be run empirically with actual non-DACH instantiations before the Alliance
marketing claims "open standard." [src: JETIX-PHILOSOPHY §10 universality
criterion B/C/D verbatim; philosophy-integrator §2 universality table]

**Janus risk at G4.** S-A excess: Jetix-central methodology team monopolises
truth; sub-leaders cannot legitimately challenge 24-Locks. INT excess:
client holons drift so far from Jetix methodology that Alliance coherence
breaks. Net Janus: the structural challenge of G4 is that BOTH risks are
simultaneously elevated and feed each other — S-A excess (ossified hard
core) causes INT excess (clients find workarounds that don't propagate
back). The corrective mechanism is a formal "methodology parliament" —
see §7. [src: philosophy-expert §6.2 S-A excess and INT excess definitions]

---

## §5 Gate G5 ($1T) — Societal Scale: F-G-R / Falsifiability / Lakatos / Supersession / UC-7 / Universality

**BOSC-A-T-X trigger first:** O + X simultaneously. Operation core verb
shifts — the organization no longer "delivers consulting" but "configures
AI-knowledge systems at societal scale"; eXternal = regulatory + civilizational
+ planetary. Fusion MHT event + Context Reframe: the organization fuses with
civic and regulatory institutions. [src: philosophy-expert §6.1 $1T gate;
strategic-insight §1 "open architecture × 30-40 размер пирога — Standard >
proprietary на зрелом рынке"]

### F-G-R discipline at G5

At $1T, the organization's methodology claims must survive scrutiny from
national regulatory bodies, academic institutions, and peer AI organizations.
The F-level framework undergoes a paradigm shift: F7+ (formally proven) is
the expected standard for foundational methodology claims — similar to how
ISO standards require formal specification before adoption by member nations.
Individual HITL attestation is structurally impossible; a distributed F-
attestation system (analogous to peer review across multiple independent
organizations) is required. [src: philosophy-expert §6.4 antifragility check
— "P5 Stoic dichotomy: Rewrite — control must split into control + influence
+ no influence"; §6.1 $1T gate "Beer-VSM recursion to societal level"]

```yaml
F: F7
ClaimScope:
  holds_when: "foundational methodology claims (analogous to ISO standards);
              operational variant claims remain F5-F6"
  not_valid_when: "F7 is claimed for a methodology element that has not been
                  validated across ≥3 independent organizational implementations"
R:
  refuted_if: "an independent implementation of Jetix methodology at scale
               produces systematically different outcomes than methodology claims predict"
  accepted_if: "≥3 independent implementations (Alliance members) corroborate the
               methodology claim with documented evidence bases reaching F7"
```

**Falsifiability mechanism at G5: statistical convergence across federated
sub-roys (see §6 for dedicated section).** The "peer review" at $1T is not
one reviewer (Ruslan) or one institutional auditor (BSI) — it is statistical
convergence across 5000+ client deployments. A methodology claim is falsified
at G5 when it fails to replicate across a statistically significant sample
of federated sub-roys operating under different conditions. See §6. [src:
prompts §6.1 cell #16 philosophy-scalability — "$1T equivalent of peer review"]

**Lakatos hardcore at G5.** The 24-Locks cannot survive as the hard core at
$1T — the organisation has become an institution (Drucker's institutionalist
lens per philosophy-expert §6.1 $1T gate). The hard core at $1T is the set
of invariants that have survived falsification across 5000+ client
deployments, not the 24 Locks that one person designated correct at G1.
The Lakatos research programme at $1T has a multi-layer hard core: (a)
epistemically-validated claims (cross-institutional replication, F7), (b)
legally-enforced standards (Alliance membership requirements), (c)
cryptographically-enforced provenance (every claim traceable to originating
deployment via signed git commits). The 24-Lock hard core is subsumed into
this larger, empirically-grounded hard core. [src: philosophy-expert §6.4
antifragility check — "P1 Popper: Keep — falsifiability is scale-invariant"]

**Supersession-chain coherence at G5.** With 5000+ client deployments
running methodology versions that span multiple major versions, supersession-
chain coherence requires a versioned methodology registry with formal
deprecation notices. A methodology claim superseded at v3.0 must carry an
explicit expiry: "claims asserting X under v2.x are invalidated from v3.0
onward; operators on v2.x have 2 quarters to migrate." The epistemic risk
at G5 is zombie claims: superseded claims that continue to be cited by stale
client deployments without the operator knowing the supersession has occurred.
The technical solution: methodology version diff notation embedded in
frontmatter (`valid_from: v1.0`, `superseded_in: v3.0`).

**UC-7 contradiction-detection scope at G5.** At societal scale,
contradiction detection is necessarily statistical, not exhaustive. A
distributed methodology observatory — analogous to scientific journal
systems — aggregates anonymized contradiction signals from Alliance-member
deployments. A contradiction that appears in >10% of deployments on a given
methodology claim is escalated to methodology revision. Fully automated
cross-client content access remains architecturally forbidden by the
federated design (UC-9 invariant is permanent). The observable at G5 is slug-
pattern convergence, not content convergence. [src: systems-integrator §11
Dissent D3 reconciliation — "Phase B+ evaluates slug-normalised detection
only after Alliance legal structure is settled"]

**Universality test at G5.** The C-test at G5 has been empirically answered:
5000+ deployments across diverse domains confirm (or refute) the universality
of `base/`. If the C-test has been continuously passed, the methodology has
earned the designation "open standard" (EISA-equivalent). If it has been
consistently refuted in certain domain classes, `base/` must be split into
domain-neutral core + domain-specific overlays — a paradigm shift in the
architecture itself. [src: STRATEGIC-INSIGHT §3 "Jetix orchestration layer =
EISA consortium"; philosophy-integrator §2 BIOS/EISA overlay]

**Janus risk at G5.** S-A excess: the Alliance methodology team becomes an
institution that cannot be falsified internally — monopoly on epistemic
truth at civilizational scale. INT excess: federated sub-roys each develop
incompatible epistemic frames, and the Alliance fractures. Net Janus: the
G5 Janus challenge is the defining challenge of all standards bodies. The
corrective mechanism is the Alliance's governance constitution: a formal
process for core revision (analogous to IETF RFC process) that prevents both
ossification and fragmentation. [src: philosophy-expert §6.2; STRATEGIC-
INSIGHT §3 "EISA consortium — открытый стандарт, который все принимают"]

---

## §6 $1T-Equivalent of Peer Review — Statistical Convergence Across Federated Sub-Roys

At G5 with 5000+ clients, the only viable peer-review mechanism is
**statistical convergence across federated sub-roys operating under
independently-verified conditions**. This is the epistemic equivalent of
multi-centre clinical trial evidence.

**The mechanism in concrete terms:**

1. **Anonymized telemetry aggregation.** Each client deployment emits
   anonymized slug-level telemetry: "methodology claim X was applied in
   this context (described by category tags, not content); the observable
   outcome was Y (measured, not inferred)." No content leaves the client
   deployment. Only tagged-metadata + outcome-measurable signals are
   aggregated. This is analogous to federated learning — the model (here
   the methodology) improves via gradient signals that never expose client
   data. [src: philosophy-integrator §4 Rule C-4 "slug-level contradiction
   patterns may be shared via slug normalisation path"]

2. **Convergence threshold as the falsifiability criterion.** A methodology
   claim at F7 (G5 standard) is considered validated when: (a) ≥1000
   independent deployments have applied the claim in their context; (b)
   ≥85% of those deployments report the predicted outcome; (c) the 15%
   deviation cases are characterised — they cluster in identifiable context
   categories (e.g., "professional services context" vs "manufacturing
   context"). This is Popperian falsifiability at scale: the claim is
   falsified if the 85% convergence threshold is not met, OR if the 15%
   deviation cases are not classifiable (indicating ClaimScope was ill-
   defined). [src: philosophy-expert §2.4 P1 Popper — "A claim earns the
   status scientific only when it specifies what observation would falsify it"]

3. **Structured peer-review circuit.** A rotating methodology review board
   (analogous to a journal editorial board) composed of sub-roy leaders
   from 5+ Alliance members independently reviews proposed methodology
   updates before they are promoted to the next major version. Review
   requires: (a) the telemetry-based evidence base, (b) a Lakatos protective-
   belt analysis (does this refute belt or core?), (c) a Kuhnian anomaly
   statement if a paradigm shift is proposed.

4. **At G5, the sub-roys themselves ARE the peer reviewers.** Each sub-roy
   (a sub-organisation with its own brigadier, its own epistemological
   community, its own client base) constitutes one "reviewer." Statistical
   convergence across sub-roys is peer review at societal scale. The quality
   of the peer review depends on: (a) sub-roy independence (they must not
   share client-specific assumptions), (b) the richness of the telemetry
   vocabulary (slug categories must be fine-grained enough to distinguish
   contextual variants), (c) the review cadence (annual or biannual
   methodology parliament, not ad-hoc).

```yaml
F: F4
ClaimScope:
  holds_when: "5000+ client deployments are operational and emitting anonymized
              slug-level telemetry; the Alliance has a formal methodology
              parliament with rotating membership"
  not_valid_when: "telemetry vocabulary has not been standardised across Alliance
                  members; slug categories are not cross-holon comparable"
R:
  refuted_if: "the 85% convergence threshold is not achievable for any
               methodology claim across ≥1000 independent deployments"
  accepted_if: "the first 10 methodology claims submitted to the Alliance
               peer-review circuit receive independent verification from ≥5
               sub-roys with convergence ≥85%"
```

**Relation to Popperian falsification.** This mechanism IS Popperian
falsification at scale — applied to the Jetix methodology as the object of
scientific inquiry, not just to the claims within each client's KB. The
methodology itself becomes a research programme (Lakatos) with a hard core
(the invariants that have survived 5000+ tests) and a protective belt (the
variant-specific heuristics that apply conditionally). The methodology
parliament is the institutionalised peer-review body. This is epistemically
consistent: "science" is not a property of a single claim but of a self-
correcting community of inquiry. At $1T, Jetix methodology has that community.
[src: philosophy-expert §2.4 P2 Kuhn; P3 Lakatos; P1 Popper; §2 domain §1
philosophy of science]

---

## §7 Lakatos Hardcore Ossification Safeguard at G3–G4

The ossification risk is real and specific: at G3 (€1M, managed team with
delegated project-brigadiers) and G4 ($100M, multi-team organisation), the
24-Locks face the most acute pressure to become sacred rather than scientific.

**The ossification mechanism (described precisely):** When a sub-leader
encounters evidence that contradicts a 24-Lock claim, the path of least
resistance is to: (a) adjust the evidence framing to remove the contradiction
("our client context is unusual"), (b) route the evidence to the protective
belt ("this is a parameter issue, not a core issue"), or (c) suppress the
evidence to avoid the political cost of an AWAITING-APPROVAL escalation.
All three paths produce the same result: the hard core becomes immune to
refutation not because it is correct but because the institutional cost of
challenging it is prohibitive. This is Lakatos degenerate research programme
— the hard core is protected by increasing complexity of the protective belt
rather than by its own empirical merit. [src: philosophy-expert §2.4 P3
Lakatos — "a research programme has a hard core + protective belt; refutations
hit the belt first, then the core"]

**Safeguard 1: Named falsifier per Lock (G3 implementation).** Every 24-Lock
entry must carry an explicit `R.refuted_if` field specifying the observable
that would refute the Lock. Locks without a named falsifier are AP-PHIL-1
violations applied to the hard core itself — non-falsifiable locks are not
science, they are dogma. Implementation: the Lock registry (`decisions/
JETIX-ARCHITECTURE-BRIEF.md`) is amended at G3 onset to add `R.refuted_if`
for each of the 24 Locks. Ruslan acks this amendment at HITL — it is not a
Lock modification, it is a Lock sharpening.

```yaml
F: F4
ClaimScope:
  holds_when: "the Lock registry has been amended to carry R.refuted_if per Lock"
  not_valid_when: "the Lock registry is treated as an immutable document;
                  no amendment process exists"
R:
  refuted_if: "a Lock is shown to lack R.refuted_if AND no amendment process
               exists after G3 onset"
  accepted_if: "all 24 Locks carry named falsifiers within 1 cycle of G3 onset"
```

**Safeguard 2: Mandatory Lock-review ritual at each gate (G3 and G4).** At
each horizon gate, a philosophy × critic pass is run over the entire 24-Lock
set — not just the deltas proposed in that cycle. The pass checks:
(a) is there accumulated evidence from the gate's context that challenges
any Lock? (b) has any Lock's ClaimScope become too broad for the new
organizational scale? (c) has any Lock's `R.refuted_if` observable been
triggered by operational data? This ritual costs one philosophy-expert
invocation per gate — a small cost against the risk of institutional dogma.
The ritual is Stoic premeditatio malorum applied to the hard core: "before
declaring the methodology stable, enumerate its failure modes." [src:
philosophy-expert §4.4 H4 Stoic premeditatio malorum — "enumerate the
failure modes of the reset itself"]

**Safeguard 3: Methodology parliament with adversarial mandate (G4).** At
G4, a formal "methodology parliament" (quarterly meeting of sub-roy leaders)
has a standing agenda item: "Lock challenge proposals." Any sub-roy leader
who has accumulated ≥5 instances of evidence that contradicts a Lock may
formally submit a "Lock challenge brief." The brief is reviewed by the
parliament, which has three decision paths: (a) confirm the Lock with
updated ClaimScope, (b) update the Lock via HITL (Ruslan acks), (c) tombstone
the Lock. The parliament does NOT average dissents — it preserves both
positions (FPF E-5 discipline) and routes to HITL when non-composable.
[src: philosophy-expert §5.3 dissent preservation; philosophy-expert §1d
requires-approval "epistemic claim against an accepted foundation"]

**Safeguard 4: Anti-ossification F-level auditing (continuous).** Philosophy-
expert × critic mode runs an F-level audit of the Lock registry every 5
cycles. Any Lock whose most recent supporting evidence is older than 20
cycles AND has not been challenged in that period is flagged as a
"Stale-Lock" — not tombstoned, but requiring fresh attestation. The Stale-
Lock flag triggers a targeted evidence-gathering task (not a full Lock-
review) to confirm the Lock remains valid in the current organizational
context. This is the Lakatos "active research programme" discipline applied
to the methodology itself: a programme that has produced no new supporting
evidence in 20 cycles is not thriving, it is drifting.

```yaml
F: F3
ClaimScope:
  holds_when: "philosophy-expert × critic cycles are running at G3+ cadence;
              5-cycle audit is operationalized as a brigadier-dispatched task"
  not_valid_when: "the 5-cycle audit is not scheduled or is deferred indefinitely"
R:
  refuted_if: "a Stale-Lock flag is generated but no attestation task is
               dispatched within 2 cycles"
  accepted_if: "every Stale-Lock flag within 10 cycles triggers a dispatched
               attestation task completed within 3 cycles of flag generation"
```

---

## §8 Epistemic Integrity of Federated Multi-Client Falsification (Popperian) + Janus Risk + Provenance + F-G-R

### Popperian falsification across federated isolation

The central tension: Popperian falsification of shared methodology claims
requires that the methodology be tested across multiple independent instances.
But each client's KB is isolated by construction (UC-9). Can a methodology
claim be falsified without violating the isolation guarantee?

**Claim (falsifiability + isolation are composable, not in tension):**
Popperian falsification of methodology claims works WITHOUT requiring client
data to cross holon boundaries. The key distinction is between:

- **Content-level falsification** (does this client's internal document
  confirm or refute the methodology claim about their specific domain?).
  This requires reading client content — UC-9 violation. FORBIDDEN.
- **Outcome-level falsification** (did the methodology, when applied in this
  client's context, produce the predicted outcome?). This requires only the
  outcome signal (success/failure on a defined acceptance predicate) and the
  context category (Mittelstand manufacturing / professional services / etc.).
  No client content is exposed. UC-9 compatible.

The methodology is falsified when outcome-level signals from ≥N independent
deployments fail to converge on the predicted outcome. This is the G5
statistical convergence mechanism (§6), but it applies from G2 onward with
smaller N:

- G2 (N=1 client): falsification requires ≥3 outcome observations from
  that single client across ≥3 distinct methodology applications. Low
  statistical power but early-signal value.
- G3 (N=3–5 clients): falsification requires convergent failure across
  ≥2 distinct client contexts. This provides cross-context evidence.
- G4 (N=50+ clients): falsification requires convergent failure in ≥10%
  of deployments for a given methodology claim — statistical power is
  meaningful.
- G5 (N=5000+): see §6.

```yaml
F: F5
ClaimScope:
  holds_when: "falsification is defined exclusively via outcome-level signals;
              no client content crosses holon boundaries during the falsification
              process"
  not_valid_when: "the falsification process requires reading client-private
                  documents — that definition is incompatible with UC-9"
R:
  refuted_if: "an outcome-level falsification signal is demonstrated to
               inadvertently expose client content (e.g., the outcome
               description is specific enough to identify the client's product)"
  accepted_if: "outcome-level signals from ≥10 client deployments are
               processed without any client identifying information being
               present in the aggregated telemetry"
```

### Shared methodology claims: falsifiable at Jetix-central, non-falsifiable per-client only

The methodology lives in `swarm/wiki/` (Jetix-central). UC-7 contradiction
detection at Jetix-central runs over methodology content only — this is
intra-methodology contradiction detection, not cross-client. When a
methodology claim is internally inconsistent, `/lint` detects it within
Jetix-central without touching any client holon. This means: the
methodology's internal coherence can be maintained via standard Popperian
tools (lint, contradiction detection, supersession) without UC-9 contact.

The methodology's external validity (does it work across client contexts?)
is tested via the outcome-level falsification mechanism described above.
The two falsification channels are orthogonal and composable:

| Falsification channel | Domain | UC-9 contact? | Applicable gate |
|---|---|---|---|
| Intra-methodology lint | Methodology coherence | NONE | G1+ |
| Philosophy × critic | Claim falsifiability | NONE | G1+ |
| Per-client `/lint` | Client-KB coherence | Per-client only | G2+ |
| Outcome-level telemetry | Methodology validity | Slug-metadata only | G2+ |
| Alliance peer-review | Methodology validity | Anonymized | G5 |

[src: philosophy-integrator §4 Rules C-1/C-2; systems-integrator §11 Dissent
D3; prompts §3.7 UC-7; prompts §3.9 UC-9]

### Janus risk per gate (summary table)

| Gate | S-A excess risk | INT excess risk | Dominant risk | Corrective mechanism |
|---|---|---|---|---|
| G1 | LOW (single tenant; monopoly is appropriate) | LOW (fully coupled) | Neither | HITL gate preserves both |
| G2 | MEDIUM (methodology push only; client data siloed) | LOW (first client holon well-coupled to methodology) | S-A (granularity leak) | `granularity: client:<slug>` lint gate |
| G3 | HIGH (Lock ossification; delegated agents protect core) | MEDIUM (client holons begin to drift) | S-A (ossification) | Named-falsifier per Lock (Safeguard 1) + gate-review ritual (Safeguard 2) |
| G4 | HIGH (institutional ossification; methodology parliament is self-interested) | HIGH (100+ holons; quarterly promotion can't keep pace) | BOTH | Methodology parliament with adversarial mandate (Safeguard 3) + F-level auditing (Safeguard 4) |
| G5 | MEDIUM-HIGH (Alliance is an institution; institutional conservatism) | MEDIUM (federated standards prevent extreme drift) | Balance-point | Alliance constitution with RFC-process for core revision; statistical convergence peer review (§6) |

[src: philosophy-expert §6.2 Janus degraded-mode; systems-integrator §6
Janus table; philosophy-expert §6.3 recovery conditions]

### Provenance of this scalability draft

All claims trace to the following Tier-1 in-repo sources. No Tier-4 book
content was read during Phase A. No paid API calls.

| # | Source | Section | Load-bearing claim |
|---|---|---|---|
| P-1 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-integrator-epistemic-overlay.md` | §1 F-G-R table; §3 defense-in-depth; §4 Rules C-1..C-4; §7 dissents D-1/D-2 | §1 F-G-R scales; §2 falsifiability mechanism; §7 Lakatos ossification description |
| P-2 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md` | §4 UC-9 proof 4-layer; §5 feedback loops R1/R2; §6 Janus table; §11 Dissent D3 | §3 UC-7 G3 bandwidth concern; §4 G4 supersession versioning; §6 statistical convergence proof; §8 Janus table |
| P-3 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md` | §5 UC-9 ≥200w; §5 UC-10 ≥200w; §6 co-located proof; §11 Dissent D-1 | §2 G2 per-client BFS latency; §8 outcome-level falsification channel table |
| P-4 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md` | §6 UC-9 proof 3-level; §8 effort estimates; §11 Dissent D-1 engineering vs mgmt | §3 G3 managed team epistemic risk; §7 Safeguard 2 gate-review ritual |
| P-5 | `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` | §1 7 structural lessons; §3 BIOS parallel; §5 Paths A/B/C; §6 built vs missing | §5 G5 societal scale framing; §6 Alliance peer-review societal analogy |
| P-6 | `prompts/km-architecture-research-2026-04-24.md` | §3.7 UC-7; §3.9 UC-9; §3.8 G1-G5 table; §6.1 cell #16 | §1-§5 gate-row BOSC-A-T-X triggers; §6 $1T peer-review mandate |
| P-7 | `.claude/agents/philosophy-expert.md` | §6.1 BOSC-A-T-X per gate; §6.2 Janus degraded; §6.4 antifragility; §2.4 P1-P10 | §7 ossification safeguards (Stoic premeditatio H4; Lakatos P3; Popper P1); §8 Janus table |

**F-G-R per claim (aggregate meta-triple):**

```yaml
F: F4
ClaimScope:
  holds_when: "epistemic projections are produced at specification level from
              peer integrator drafts; no empirical data from deployed client
              instances is available to validate G2+ projections"
  not_valid_when: "projections are interpreted as empirical findings rather
                  than structured anticipations requiring validation at each gate"
R:
  refuted_if: "any gate-level projection fails to match observable outcomes
               when the gate is actually reached (each projection has a named
               observable in its F-G-R triple)"
  accepted_if: "gate projections are reviewed at each horizon gate transition
               and updated with operational evidence; no projection is allowed
               to remain unchallenged beyond its own gate"
```

**Acceptance test (Hamel-binary):** "This document projects epistemic
invariants through all 5 gates WITH named BOSC-A-T-X triggers AND names the
$1T-equivalent of peer review as statistical convergence across federated
sub-roys with anonymized outcome-level telemetry AND identifies Lakatos
hardcore ossification risk at G3-G4 with 4 named safeguards AND demonstrates
that Popperian falsification of shared methodology claims is UC-9-compatible
via outcome-level (not content-level) falsification channels AND carries
(F, ClaimScope, R) triples on every major claim AND names Janus risk per
gate in the summary table."

---

*Draft status: authored by philosophy-expert, mode: scalability.
Awaiting brigadier gate review for cycle cyc-km-architecture-2026-04-24.
Word count: ~2,600 words. All 5 gates projected. §6 peer-review mechanism
at G5 named. §7 ossification safeguards (4 named). §8 epistemic integrity
of federated falsification + Janus table + F-G-R meta-triple.*
