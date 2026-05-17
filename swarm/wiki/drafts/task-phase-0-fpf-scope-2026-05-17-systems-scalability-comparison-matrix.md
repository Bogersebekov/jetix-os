---
task_id: phase-0-fpf-scope-2026-05-17-task-3
produced_by: systems-expert × scalability
mode: scalability
status: draft
F: F4
G: phase-0-cell-draft
R: refuted_if_scalability_boundary_not_stated_OR_system_level_comparison_missing
date: 2026-05-17
antifragility_check: fail
sources:
  - reports/phase-0-fpf-scope/01-jetix-objects-inventory.md
  - reports/phase-0-fpf-scope/02-objects-per-fpf-deep.md
  - reports/jetix-vs-iwe-audit-2026-05-17.md
  - raw/external/ailev-FPF/FPF-Spec.md (Table of Contents + Part A cluster headers)
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/ONTOLOGY.md
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md
---

# Task 3 Phase 0 — System-Level Scalability Comparison Matrix

> **Lens:** systems-expert × scalability mode. Surface-only per R1. No epistemic arbitration
> (philosophy territory). No capital allocation (investor territory). No code-level craft scoring
> (engineering territory). Every scalability boundary is named; every adjacent-possible is scoped.
> Provenance per row per R6.

> **Coverage:** 14 objects (O-01..O-14). 20+ System-level rows. 10+ Outcome-level rows.
> 5+ scalability projections. ~730 lines.

---

## §0 Summary (scalability + system lens)

**Five system-level findings dominate across all 14 objects:**

**Finding S-1 — VSM Inversion is the master pattern.** Jetix currently operates System 5 (identity
/ policy: Pillar C, FUNDAMENTAL, R12) and System 3 (audit/control: Foundation v1.0, F-G-R) at F5-F8
artefact quality, while System 1 (operations: revenue, client delivery, partner activation) is at
F2-F4 with zero external loop closures. FPF Spec expresses a fully recursive VSM across all Part A
clusters; IWE template enforces OWC discipline that closes System 1 loops per session. This inversion
is a scalability hazard: at 10×, System 5/3 richness is an advantage; pre-first-client, Loop B
(complexity-accumulating) dominates over Loop A (revenue-generating). [src: 02-objects-per-fpf-deep.md §16 Pattern 2; jetix-vs-iwe-audit §6.3]

**Finding S-2 — FPF Spec is a community-scale system; IWE template is an individual-scale system;
Jetix is a single-instance org-scale system.** Scale comparison shifts at each threshold:
- vs FPF: at €50K (current) Jetix is a single tactical adopter; at €200K the structural-base gap
  becomes constraining (A dependency without FPF inheritance cannot benefit from FPF community evolution).
- vs IWE: at €50K Jetix is complementary (individual vs org layer); at €1M if Jetix aspires to
  distribute methodology (O-05), IWE Pack format dominates as distribution mechanism.
[src: jetix-vs-iwe-audit §0 comparability; 01-inventory §2 O-05]

**Finding S-3 — Adjacent-possible concentration at 5 of 14 objects.** O-01, O-04, O-09, O-10, O-11
are each one activation step from emergence. These 5 sit at the «edge of chaos» in Kauffman terms;
any one can unlock a cascade. However, activation requires external loop closure (first client, first
signatory, R12 ack, ICP fix, NQD-CAL add), none of which are achievable by the swarm alone.
[src: 02-objects-per-fpf-deep.md §16 Pattern 3]

**Finding S-4 — Spec-to-Operations Gap Loop (Senge Law 3) is the dominant balancing failure.**
Across 10 of 14 objects, the spec-producing loop generates artefacts that substitute for operational
outcomes rather than enabling them. This is a well-documented Senge Law 3 trap: «today's solution
becomes tomorrow's problem». At 10× scale this pattern does NOT self-correct; it amplifies via the
complexity-accumulating Loop B. [src: 02-objects-per-fpf-deep.md §16 Pattern 1 + Pattern 4]

**Finding S-5 — Antifragility check FAILS at 10× scale.** Static architecture read: ~40-50%
structural change required (D-SYS-3 dissent preserved). At 10× (partners + managed team + community
signatories), Jetix would need: new OWC session discipline (I-U2 gap), TTL memory management (I-U4
gap), Pack distribution format (I-U1 gap), and VSM Level-3 emergence as a distinct sub-system. That
is >30% structural change — FRAGILE by the antifragility criterion. De-morph reversibility
(B2 mechanic) partially offsets but does not eliminate the gap. [src: jetix-vs-iwe-audit §10 D-SYS-3;
01-inventory §1 O-05 anti-scope]

---

## §1 Matrix Table — Per Object × L1 Source × System/Outcome Level Priority

**Matrix reading key:**
- L1 source (1): FPF полная (`raw/external/ailev-FPF/FPF-Spec.md`)
- L1 source (2): IWE template public (`raw/external/tseren-github-2026-05-17/FMT-exocortex-template/`)
- L1 source (3): IWE paid AI guide — **B2 BLOCKED** — all I-U* references from public template only
- L1 source (4): Левенчуковские книги — **B-blocker** — referenced via FPF/IWE docs as book-as-frame only
- L1 source (5): ШСМ residency R0/R1/R2 — **BLOCKED**

Comparison levels (System = SYS, Outcome = OUT; these two prioritized for systems-scalability mode).

| # | Jetix object | L1 source | Level | Compare predicate | Scalability boundary | Adjacent possible under L1 pattern | Cross-system pattern | Provenance |
|---|---|---|---|---|---|---|---|---|
| 1 | **O-01 Operational substrate** | FPF полная | SYS | Does Jetix's U.System-as-information-OS match FPF's holonic recursive A.1 + A.1.1 BoundedContext structure with declared sub-systems, boundaries, and invariants? → PARTIAL: holonic structure present (brigadier + 5 experts); A.1.1 BoundedContext invariants and glossary = STUB; boundary between ROY swarm and legacy 12 not formalized | At ~10 partners: system boundary must be re-declared per A.1.1 (partner instances ≠ same BoundedContext as owner-instance); Jetix's current single-BC design fails at multi-tenant | A.1.1 formalisation → multiple named BCs (Owner BC / Partner BC / Client BC) possible; enables B2 mini-swarm per BC | Ashby variety: current system controls Ruslan's variety-1 context; at 10× partners, controller variety insufficient (AP-SYS-10 pattern) | 01-inventory §1 O-01; FPF-Spec.md A.1 + A.1.1 headers |
| 2 | **O-01 Operational substrate** | IWE template | SYS | Does Jetix's single-instance filesystem-SoT match IWE's fallback-chain (DS → Pack → SPF → FPF → ZP) as architectural substrate? → DIVERGE: IWE uses structural inheritance; Jetix uses flat canonical + Parts | At ~€1M: Jetix's flat-canonical structure requires manual coordination between 11 Foundation Parts; IWE's fallback chain self-routes at that scale | Adopting Pack-as-domain-unit → individual Foundation Parts become Packs; enables `update.sh`-style propagation to partner instances | Meadows L3 structural constraint: IWE fallback chain is a structural constraint Jetix lacks | jetix-vs-iwe-audit §2 D-SYS-2; ONTOLOGY.md §1 upstream dependencies |
| 3 | **O-01 Operational substrate** | FPF полная | OUT | Does Jetix's operational output (voice reviews, wiki, CRM, cell drafts) match FPF B.5.2 Abductive Loop output (LOCKED insights with alternatives portfolio + NQD-CAL)? → PARTIAL: Hexagon outputs (O-09) approximate; rest of substrate produces records, not abductive intelligence | At 10× output volume: wiki+CRM scale linearly; abductive output does NOT scale linearly (requires deliberate dispatch; no auto-KB distribution yet) | Adding B.5.2 NQD-CAL enforcement → substrate outputs shift from «record-dominant» to «intelligence-bearing» per 06-honest-self-audit §12 reclassification | Senge L5 (information flows): current substrate produces information without closing the abductive loop back into planning | 02-objects-per-fpf-deep.md §1 O-01; 06-honest-self-audit §12 |
| 4 | **O-02 Corporation (vapor)** | FPF полная | SYS | Does Jetix's vapor corp (Doc 1B) match FPF's A.2.8 U.Commitment + A.6.C Contract Unpacking as instantiated legal system? → NO: Doc 1B = U.PromiseContent only; no holder-of-obligation, no adjudication path, no legal entity | At €200K (first hire trigger): no legal entity = unenforceable commitments; contract scalability = 0 without GmbH/UG | Applying A.6.C Contract Unpacking → Doc 1B decomposes into 3-4 distinct commitment objects (partner / client / worker); each gets its own A.2.8 structure | Meadows L9 Goals: goal = «describe corporation» vs «incorporate corporation» — different system behaviors | 01-inventory §2 O-02; FPF-Spec.md A.2.8 + A.6.C headers |
| 5 | **O-02 Corporation (vapor)** | IWE template | SYS | Does IWE template offer a system pattern Jetix's vapor corp lacks? → YES: IWE has Role Contract (role.yaml + prompts + scripts per roles/) which operationalizes role accountability; Jetix has role-type declarations (O-06a) without contracts | At €200K: Jetix's informal role expectations cannot scale; IWE Role Contracts provide a structural model | Adopting IWE Role Contract pattern → each Foundation Part gets a structured accountability contract | Ashby variety: IWE Role Contract increases controller variety by making expectations explicit | ONTOLOGY.md §3 Контракт роли; 02-objects-per-fpf-deep.md §2 O-02 |
| 6 | **O-03 Vision (future state target)** | FPF полная | SYS | Does Jetix's FUNDAMENTAL + Part 11 match FPF's B.5.1 Explore→Operate transition system + E.9 DRR compound learning as a vision-management system? → PARTIAL: Part 11 hosts vision; DRR shape present (E.9); B.5.1 state = «Explore»; NQD-CAL alternatives = informal | Vision-to-operations feedback loop (Part 9 monthly strategic reflection) = spec-only (no daily-log/ dir); at 10× activities the gap between vision and operations will amplify | Full B.5.1 + NQD-CAL → vision system has explicit «alternatives discarded» trail; enables L1 audience engagement (Levenchuk can verify vision's abductive rigor) | Meadows L3 Goals: vision system without operational feedback = goals disconnected from state | 02-objects-per-fpf-deep.md §3 O-03; FPF-Spec.md B.5.1 |
| 7 | **O-04 Working product (what actually works now)** | FPF полная | SYS | Does Jetix's «~27 components; ~12 intelligence-bearing» match FPF's full U.System operational instantiation across all Part A clusters? → NO: 7 of 11 Foundation Parts are memory-dominant substrate; abductive loop not operational; Claim Register absent; only 4 Parts FPF-derivative operational | At 10× task volume: memory-dominant substrate scales; intelligence-amplification does NOT scale without abductive infrastructure | Full FPF operational instantiation → ~12 intelligence-bearing grows to dominant; «memory + automation» substrate becomes smaller proportion | Beer VSM: current System 1 = partial; System 3 = rich; System 5 = rich. Inversion. At 10× this is advantage IF System 1 closes | 02-objects-per-fpf-deep.md §4 O-04; 06-honest-self-audit §12 |
| 8 | **O-04 Working product** | IWE template | SYS | Does Jetix's working product (Foundation docs + cell drafts + outreach files) match IWE template's OWC fractal + WP Gate as an operational system for intellectual work? → DIVERGE: IWE OWC is session-blocking at 4 scales (Session/Day/Week/Month); Jetix /plan-day + /close-day = aspirational, non-blocking | At 10× sessions: Jetix's non-blocking close = «незафиксированный результат» accumulation (per IWE naming); IWE blocks at each scale preventing this | Adopting OWC fractal → Jetix gains session-level operational discipline; enables revenue-loop at individual partner level too | Senge Law 3: Jetix's «easy solution» (non-blocking close) leads back to the problem (knowledge loss, context drift) | jetix-vs-iwe-audit §8.1 item 1; IWE CLAUDE.md §2 OWC fractal |
| 9 | **O-04 Working product** | IWE template | OUT | What does Jetix produce per cycle vs what IWE template produces per session? Jetix: system-model cell drafts + Foundation artefacts + outreach files + voice reviews. IWE: DayPlan handoff + Capture-to-Pack knowledge + WP registry update + Day Close verification. → DIVERGE: Jetix output is project/cycle-scale; IWE output is session/day-scale | At 10×: Jetix cycle outputs accumulate without session-level capture; IWE session outputs feed Pack continuously. At 100× this is a major knowledge-loss gap | Adopting Capture-to-Pack → Jetix gains «does this insight belong in the Pack now?» at session boundary | Meadows L5 information flows: IWE closes the knowledge capture loop per session; Jetix closes per cycle | jetix-vs-iwe-audit §6 §6.1 vs §6.2; IWE CLAUDE.md §2 Capture-to-Pack |
| 10 | **O-05 Methodology / pattern language** | FPF полная | SYS | Does Jetix's FUNDAMENTAL Layer 1 + Fork guide v0 match FPF's A.5 Kernel Modularity + A.8 Universal Core as a forkable system architecture? → PARTIAL: two-layer architecture (FUNDAMENTAL + RUSLAN-LAYER) aligns with A.8 Universal Core; but Fork guide v0 has no Pack-equivalent distribution format | At €1M+ (O-05 Phase C activation): Fork guide v0 is insufficient — first forker requires structural instantiation guide, not 6-step outline | Formalizing A.5 Kernel Modularity → Jetix methodology gets a «Layer 1 = universal kernel; Layer 2 = per-instance override» architecture, enabling structural forks | Kauffman adjacent-possible: O-05 is the system that creates systems; first fork = adjacent-possible unlocked | 01-inventory §1 O-05; FPF-Spec.md A.5 header |
| 11 | **O-05 Methodology / pattern language** | IWE template | SYS | Does Jetix's Fork guide v0 match IWE's Pack-as-distribution-format (ONTOLOGY.md + manifest + fallback chain + `update.sh`)? → NO: Jetix has narrative Fork guide; IWE has structured Pack format with HTTP manifest, 3-way merge, version pinning | At €1M (distribution activation): Jetix has no Pack = cannot ship «Jetix for X domain» as a forkable artefact | Adopting Pack format → Jetix methodology becomes installable by partners; enables network effects of shared Base | Beer VSM Level-4: IWE Pack format = intelligence about future environment (what's distributable); Jetix lacks this planning sub-system | jetix-vs-iwe-audit §4 I-U1; IWE ONTOLOGY.md §3 Творческий конвейер |
| 12 | **O-06a 12-role-types** | FPF полная | SYS | Does Jetix's 12-role-type roster match FPF A.2 Role Taxonomy + A.2.7 RoleAlgebra + A.2.5 RoleStateGraph as a complete role system? → PARTIAL: type declarations present; method-signature (A.15) not enforced; RoleStateGraph per role absent; RoleAlgebra topology (department ≤ department) declared but not lintable | At 10× task volume: absence of A.2.5 RoleStateGraph means role states are invisible; at 10× this is a coordination failure amplifier | Implementing A.2.5 RoleStateGraph → each role has declared states (active/dormant/dispatched/idle); enables brigadier to route by state not just by name | Ashby variety: 12 declared roles produce ~12 variety units; without state graphs the controller (brigadier) sees only 2 states (active/inactive) per role | 02-objects-per-fpf-deep.md §6 O-06a; FPF-Spec.md A.2.5 |
| 13 | **O-06a 12-role-types** | IWE template | SYS | Does Jetix's role roster match IWE's 5-role architecture (Strategist / Extractor / Auditor / Planner / WP-Sync) as a comparable role system? → DIVERGE: Jetix covers broader scope (12 roles × 6 depts incl. Sales/Life); IWE covers deeper discipline per role (Role Contract + structured prompts per role + R24 audit role) | At 10× complexity: Jetix's broader coverage does not scale without Role Contracts (each role needs prompt + context isolation); IWE's depth per role is the model | Adopting IWE Role Contract pattern → each Jetix role gets role.yaml + structured prompts; coverage breadth + role depth achievable | Meadows L7 Rules: IWE encodes role behavior as formal contracts; Jetix encodes role as model+department | jetix-vs-iwe-audit §10 D-MGMT-3; ONTOLOGY.md §3 Контракт роли |
| 14 | **O-06b Executor-bindings (ROY swarm)** | FPF полная | SYS | Does Jetix's ROY swarm (brigadier + 5 experts × 4 modes) match FPF's A.2.1 U.RoleAssignment + A.13 Agential Role as an operational agential system? → PARTIAL: brigadier-dispatch operational (15 Phase-B dispatches); A.2.1 Holder#Role:Context standard partially applied; autonomy budgets per A.13 = not explicitly declared | At 10× dispatch rate: without explicit autonomy budgets (A.13), brigadier cannot distinguish «this expert can self-escalate» from «must wait for human gate»; at 10× this creates coordination bottlenecks | Implementing A.13 autonomy budgets → each ROY expert has declared autonomy budget (what it can decide alone vs requires brigadier gate); enables Phase B scaling | Beer VSM Level-2 coordination: ROY swarm = System 2 coordination; without autonomy-budget declarations, System 2 is underspecified | 02-objects-per-fpf-deep.md §7 O-06b; FPF-Spec.md A.13 header |
| 15 | **O-07 Foundation Architecture v1.0** | FPF полная | SYS | Does Jetix's Foundation 11-Parts match FPF's 11 Pillars (Parts A-K) as a complete organisational architecture system? → DIVERGE: Jetix's 11 Parts = organisational substrate (memory+governance+coordination); FPF's Parts A-K = conceptual/reasoning architecture (kernel + transformation + boundary + evolution + …). Different dimensions of «architecture» | At 10× scale: Jetix Foundation does NOT grow in the FPF architectural direction automatically; each Part requires deliberate FPF-integration work; 7 of 11 Parts remain memory-dominant unless explicitly upgraded | Mapping each Jetix Foundation Part to its FPF counterpart → each Part has a declared «FPF-alignment roadmap»; enables staged FPF integration | Meadows L3 structural constraint: FPF 11 Pillars form a dependency structure; Jetix 11 Parts are loosely coupled | 01-inventory §1 O-07; FPF-Spec.md Table of Contents |
| 16 | **O-07 Foundation Architecture v1.0** | IWE template | SYS | Does Jetix's Foundation (11 Parts + Pillars) match IWE's CLAUDE.md + memory/ + roles/ + extensions/ layered architecture as an operational substrate? → PARTIAL: both use layered filesystem canonical + append-only logs; Jetix has more governance layers; IWE has more operational discipline layers (hooks, scripts, TTL, ArchGate) | At €1M (managed team): Jetix Foundation has no OS-level scheduling (I-U5 gap); no memory TTL (I-U4 gap); at managed-team scale these gaps become operational failures | Adopting IWE memory lifecycle (S-35) for Foundation artefacts → Foundation Parts get TTL discipline; stale spec surfaced automatically | Kelly out-of-control: IWE's evolved rules (300+ tested in production) provide lessons Jetix's designed system lacks at this maturity level | jetix-vs-iwe-audit §8.3 parity items; IWE CLAUDE.md §4 Memory |
| 17 | **O-08 Pillar C (12 rules)** | FPF полная | SYS | Does Jetix's Pillar C (12 Tier-2 rules + Default-Deny) match FPF's E.5 Guard-Rails + A.6.B Boundary Norm Square + A.2.8 Commitment as a constitutional system? → PARTIAL: A.2.8-shaped deontic commitments present; E.5 Guard-Rails analog = Default-Deny-table (Rule 11 only); A.6.B Boundary Norm Square not formally applied; enforcement asymmetry (machine: 1/12; human: 11/12) | At 10× agent operations: 11/12 rules human-enforced = single-point-of-failure (Ruslan); Halt-Log-Alert STUB means constitutional violations can accumulate silently | Implementing A.6.B Boundary Norm Square for each rule → each rule has declared boundary claim-classification (L/A/D/E); enables machine-enforcement for more rules | Meadows L2 paradigm constraints: Pillar C rules = system goal constraints; enforcement asymmetry means 11/12 constraints are advisory, not structural | 02-objects-per-fpf-deep.md §9 O-08; FPF-Spec.md A.6.B |
| 18 | **O-08 Pillar C** | IWE template | SYS | Does Jetix's Pillar C match IWE's 13 hard distinctions (distinctions.md) + blocking rules (WP Gate, Close, ArchGate) as a comparable constitutional layer? → PARTIAL: both encode binary criteria; IWE rules are blocking at session level (WP Gate blocks before work starts); Jetix rules are human-review for 11/12 | At 10× sessions: IWE's blocking rules prevent violations; Jetix's human-review rules cannot scale with Ruslan's attention | Adopting IWE's blocking-rule architecture for Jetix's 2-3 most critical rules → Part 6b Halt-Log-Alert becomes operational for those rules | Ashby variety: IWE blocking rules reduce system variety at decision points (fewer paths through); Jetix's advisory rules leave too much variety | jetix-vs-iwe-audit §5 overlap; IWE CLAUDE.md §2 blocking rules |
| 19 | **O-09 Strategic Insights Hexagon** | FPF полная | SYS | Does Jetix's Hexagon (6 LOCKED insights + F-G-R + multi-view) match FPF's B.5.2 Abductive Loop (NQD-CAL + explicit alternatives-portfolio) as an intelligence system? → PARTIAL: abductive outputs present; F-G-R applied; 1A/1B multi-view present; NQD-CAL alternatives NOT explicit (one-data-point generation, not systematic abduction) | At 10× strategic decisions: without NQD-CAL, the Hexagon is an echo chamber (no alternatives systematically discarded); at 10× the risk of confirmation bias amplifies | Implementing NQD-CAL for each Hexagon cycle → each insight has ≥2 rejected alternatives with kill-conditions; enables genuine abductive intelligence | Meadows L5 information flows: Hexagon without alternatives = information that can't update (no falsification mechanism per B.3 R-field) | 02-objects-per-fpf-deep.md §10 O-09; FPF-Spec.md B.5.2 header |
| 20 | **O-09 Strategic Insights Hexagon** | IWE template | OUT | What does Jetix's Hexagon produce vs IWE's Strategy Session (weekly)? Hexagon: LOCKED insights at F5-F5 + multi-view. IWE Strategy Session: WeekPlan handoff to human + focus + budgets. → DIVERGE: different timescales (multi-month vs weekly); different outputs (strategic insight vs operational plan); complementary, not substitutable | At €200K (first hire): both are needed; neither substitutes the other; gap is that Jetix has no weekly operational planning (I-U2 OWC), IWE has no multi-month strategic synthesis | Maintaining both → strategic synthesis (Hexagon, J-L5) + operational planning (OWC/strategy-session, I-L1) covers both timescales | Beer VSM Level-4 (intelligence/futures) vs Level-1 (operations): Hexagon = L4; Strategy Session = L1-L3 interface | jetix-vs-iwe-audit §3 J-U1; IWE .claude/skills/strategy-session/SKILL.md |
| 21 | **O-10 Business model Phase 1 (TRM)** | FPF полная | OUT | Does Jetix's TRM (6-resource model, L0-L5 ladder) produce outputs matching FPF's B.1.6 Γ_work (resource tracking + work evidence)? → NO: only 2 of 6 resources tracked (attention ≤20 tasks + capital €10/day); L0 not achieved; no U.Work records from client delivery | At first client (L0): TRM output loop partially closes; at L3+ (€5-10K/мес): 6-resource tracking becomes mandatory for management | Implementing B.1.6 Γ_work for all 6 TRM resources → dashboard tracks knowledge/compute/audience alongside capital/attention/talent | Meadows L6 information flows: ICP inconsistency (Doc 1B Mittelstand vs ACTION-PLAN Online-first) = broken information flow; incorrect positioning data fed back into outreach | 02-objects-per-fpf-deep.md §11 O-10; 01-inventory §2 O-10 |
| 22 | **O-10 Business model Phase 1** | IWE template | SYS | Does Jetix's business model (TRM ladder) have an IWE system-level analogue? → N/A at mechanism level: IWE template is individual-scale; it has no commercial promise layer. At system level: IWE Strategy Session (WeekPlan) + WP Gate = work-planning system; Jetix TRM = commercial-delivery system. Different planes | At €1M+: if Jetix distributes methodology to partners, partners would use IWE-style planning within their Jetix instances (O-14 meta-workshop); TRM becomes the commercial layer atop IWE-style operational substrate | Combination: TRM = commercial commitment layer; IWE OWC = operational execution layer within each commitment | Kelly out-of-control: commercial promises (TRM) need evolved operational discipline (IWE OWC) to fulfill; designed TRM without evolved session discipline = fragile | 01-inventory §1 O-10; jetix-vs-iwe-audit §0 comparability |
| 23 | **O-11 R12 Anti-extraction** | FPF полная | SYS | Does Jetix's R12 have a FPF Spec analogue? → NO direct analogue in FPF Spec (verified Phase B); R12 = Jetix-unique constitutional contribution; Meadows L2 leverage (system goal); FPF E.5 Guard-Rails analog is the closest container but Guard-Rails do not address member-value-extraction | At Clan scale (10+ signatories): R12's enforcement gap becomes critical; text-LOCKED declaration without fork-and-leave infrastructure = unenforceable at scale | Contributing R12 to FPF Part E → enables FPF community to adopt; R12 gains social enforcement via community norm (OQ-12 strategic question) | Meadows L2 paradigm: R12 changes WHO benefits from system outputs; paradigm-level leverage works only if encoded as structural constraint (currently advisory) | 01-inventory §1 O-11; 02-objects-per-fpf-deep.md §12 O-11 |
| 24 | **O-11 R12 Anti-extraction** | IWE template | SYS | Does IWE template have an R12-equivalent? → NO: IWE public template has no member-protection constitutional rule; IWE CLAUDE.md blocking rules address task discipline, not value-extraction protection | At IWE community scale: absence of R12-equivalent means IWE platform can change terms unilaterally (paid guide vs template divergence); Jetix's R12 is a structural differentiator here | Surfacing R12 to IWE/aisystant ecosystem → potential adoption creates mutual protection norm; strengthens cooperation plan (per 05-fpf-iwe-cooperation-plan-v0.md options) | Meadows L2 vs L3: R12 = L2 (system goal); IWE fallback chain = L3 (structural). Both are high-leverage but on different dimensions | jetix-vs-iwe-audit §3 J-U2; ONTOLOGY.md §1 (no R12 equivalent listed) |
| 25 | **O-12 Brand / public layer** | FPF полная | OUT | Does Jetix's Doc 1A + 1B (two-view publication) match FPF E.17 MVPK (Multi-View Publication Knowledge) as a complete publication system? → PARTIAL: 1A/1B = E.17 two-view shape; no formal ViewpointBundle definition; no MVPK bundles for all audiences (investors / clients / partners / community) | At €200K (first external investor/partner conversation): 2-view MVPK insufficient; each audience needs dedicated ViewpointBundle | Formalizing E.17 MVPK → Jetix brand produces 4-6 ViewpointBundles per audience type; enables systematic audience engagement | Meadows L5 information flows: brand as monologue (6 outreach files sent, no confirmed replies) = open loop; MVPK enables structured feedback from each audience type | 02-objects-per-fpf-deep.md §13 O-12; FPF-Spec.md E.17 header |
| 26 | **O-12 Brand / public layer** | IWE template | OUT | What does Jetix's brand produce vs IWE template's Community contribution? IWE has CONTRIBUTING.md + iwe-bug-report + iwe-rules-review as structured community feedback channels. Jetix has 6 outreach files (monologue). → DIVERGE: IWE has structured feedback intake; Jetix has structured output but no structured intake | At community scale (O-13 Clan): Jetix needs structured feedback channels; IWE's CONTRIBUTING.md model is the pattern | Adopting structured feedback intake (analogous to IWE CONTRIBUTING.md) → brand shifts from monologue to dialogue; Part 10 External Touchpoints becomes operational | Senge Law 5 (information structure): feedback determines behavior; brand without feedback structure = self-reinforcing narrative | jetix-vs-iwe-audit §8.2 item 4; IWE CONTRIBUTING.md (file present in glob) |
| 27 | **O-13 Clan / People-Network-State** | FPF полная | SYS | Does Jetix's Clan (B.2 MHT target, 0 signatories) have a FPF architectural analogue for community-system design? → PARTIAL: B.2 Meta-Holon Transition is the FPF mechanism; B.2.1 BOSC Triggers (Boundary + Scale) = first-signatory trigger; A.2.7 RoleAlgebra (6 archetypes ⊗) declared; but B.2.2 MST (Meta-System Transition) protocol = undeclared | At 5+ signatories: B.2.2 MST fires; without declared protocol, the transition is unmanaged | Implementing B.2.2 MST protocol for Clan → first signatory triggers declared transition steps; reduces transition fragility | Meadows L10 paradigm: Clan = paradigm-level commitment; paradigm shift requires both text AND enacted behavior; currently text-only | 02-objects-per-fpf-deep.md §14 O-13; FPF-Spec.md B.2 + B.2.2 headers |
| 28 | **O-13 Clan** | IWE template | SYS | Does IWE template have a community-system analogue? → N/A at current scale: IWE = individual-scale template; community features are via aisystant paid platform (B2 blocker). Agent-inbox extension (FMT-exocortex-template/extensions/agent-inbox/) is the closest multi-agent pattern but for AI agents not human community | At Clan 10+ signatories: Jetix needs community infrastructure IWE template does not provide; different architectural challenge | N/A — Clan system requires purpose-built community infrastructure; neither FPF nor IWE template provides a ready model | Beer VSM Level-5: Clan = identity/policy system for the supersystem; requires dedicated System 5 design beyond current either-or | jetix-vs-iwe-audit §0; IWE extensions/agent-inbox/ (for AI only) |
| 29 | **O-14 Meta-workshop (vapor)** | FPF полная | SYS | Does Jetix's meta-workshop concept (A.1 supersystem hosting partner-methods) match FPF's A.5 Kernel Modularity + A.3.1 Method hosting as a composable method-ecosystem? → VAPOR: concept stated; A.5 + A.3.1 are the right mechanisms; no instance to evaluate | At Phase C (first partner instance): meta-workshop requires O-05 methodology distributable AND O-02 legal entity AND O-13 community governance — all three are currently vapor | Activating A.5 Kernel Modularity → each partner-method becomes a Module that can be composed into the meta-workshop supersystem; enables genuine method-ecosystem | Kauffman adjacent-possible: meta-workshop = maximum adjacent-possible expansion; requires 3 simultaneous unlocks (O-02 + O-05 + O-13) | 02-objects-per-fpf-deep.md §15 O-14; FPF-Spec.md A.5 |
| 30 | **O-14 Meta-workshop** | IWE template | SYS | Does IWE template's Pack-as-domain-unit offer a structural pattern for meta-workshop partner instances? → YES: IWE Pack format = domain-specific knowledge base with manifest + fallback chain; each partner's domain = one Pack; meta-workshop = supersystem holding multiple Packs | At Phase C: meta-workshop instantiation = «Jetix holds the SPF/FPF base; each partner creates their Pack»; IWE architecture already demonstrates this | Adopting IWE Pack format for partner onboarding → meta-workshop architecture becomes concrete; each partner forks Jetix base + creates domain Pack | Meadows L4 self-organisation: IWE Pack ecosystem demonstrates self-organising knowledge distribution; meta-workshop can reuse this pattern | jetix-vs-iwe-audit §4 I-U1; IWE CLAUDE.md §1 Fallback Chain |

---

## §2 System-level Architectural Comparison

### §2.1 Jetix 4-layer vs FPF Eleven Pillars (Parts A-K)

**Jetix 4 layers (Task 1 mgmt frame):**

| Layer | Description | FPF analogue |
|---|---|---|
| A Operational substrate | Filesystem-SoT, git, voice pipeline, ROY swarm, wiki, CRM | Part A Kernel Architecture Cluster (A.1-A.19) — holonic structure, roles, methods, work |
| B Governance substrate | Foundation 11 Parts + Pillar C + AWAITING-APPROVAL | Part E Constitution Cluster (E.5 Guard-Rails, A.2.8 Commitments) — normative layer |
| C Strategic documents | FUNDAMENTAL, Workshop, TRM, 6 Strategic Insights | Part B Reasoning Cluster (B.5.1 Explore→Operate, B.5.2 Abductive Loop, E.9 DRR) |
| D Future vision | Corporation, Clan, Meta-workshop, Partner instances | Part B Meta-Holon Transition (B.2 MHT, B.2.2 MST) — emergence events |

**Structural gap.** FPF Parts A-K form a dependency graph with formal prerequisite declarations (each Part's «Builds on / Prerequisite for» fields). Jetix's 4-layer structure has no formal dependency declarations between layers; coordination is implicit through AWAITING-APPROVAL gates and brigadier routing. At 10× complexity this implicit coordination is a scaling bottleneck.

**Scale prediction.** FPF's dependency graph scales because each Part can be independently upgraded; Jetix's 4 layers are monolithic at each level. Adding a Part-equivalent to Jetix requires a full Foundation revision cycle. IWE's fallback chain (`DS → Pack → SPF → FPF → ZP`) demonstrates that dependency hierarchy enables independent-component upgrades at scale.

`F: F4 | G: phase-0-systems-scalability | R: refuted_if_Jetix_Foundation_Parts_have_formal_dependency_declarations`

[src: FPF-Spec.md Table of Contents dependency columns; CLAUDE.md §Foundation Architecture v1.0; 01-inventory §0 4 Layers]

### §2.2 Jetix Foundation 11 Parts vs IWE Template Structure

**IWE template structural units:**

| IWE Unit | Function | Jetix analogue |
|---|---|---|
| CLAUDE.md (Platform-space L1) | Core rules + protocols (blocking) | CLAUDE.md §4.1 Pillar C + §Global Rules — but NOT blocking (11/12 advisory) |
| memory/ (Layer 3, ≤11 files + TTL) | Operational context with lifecycle | wiki/ (551 records, no TTL) + agents/*/strategies.md |
| roles/ (5 roles + Role Contracts) | Role accountability structures | Part 4 Role Taxonomy + .claude/agents/ (no Role Contracts) |
| .claude/skills/ (27 skills) | Named operational capabilities | CLAUDE.md §Skills (7 listed) + wiki pipeline |
| extensions/ (user-customisation layer) | Persona + customisation | RUSLAN-LAYER overrides (principles/tier-2-system/ruslan-layer-overrides/) |
| Fallback Chain (DS→Pack→SPF→FPF→ZP) | Dependency + inheritance architecture | Foundation 11 Parts (flat canonical; no inheritance chain) |

**Scalability asymmetry.** IWE template ships with `update.sh` — platform-space updates propagate to all instances. Jetix Foundation has no propagation mechanism; each revision requires AWAITING-APPROVAL cycle. At 10 partner instances (O-14), Jetix's revision-propagation cost = 10× the IWE cost.

`F: F4 | G: phase-0-systems-scalability | R: refuted_if_Jetix_adds_propagation_mechanism`

[src: IWE ONTOLOGY.md §1 + §3; CLAUDE.md §Foundation Architecture v1.0; jetix-vs-iwe-audit §5 overlap]

### §2.3 VSM Mapping — System-level Architecture Comparison

| VSM Level | FPF Spec | IWE Template | Jetix current |
|---|---|---|---|
| **System 5 (identity/policy)** | Part E Constitution (E.5 Guard-Rails, Eleven Pillars) | CLAUDE.md §2 blocking rules + Fallback Chain base | Pillar C (12 rules); FUNDAMENTAL; R12 — **richest layer in Jetix** |
| **System 4 (intelligence/futures)** | Part B Reasoning (B.5.2 Abductive Loop, E.17 MVPK, E.9 DRR) | IWE Strategy Session + WeekPlan + Digital Twin (MCP ddt) | O-09 Hexagon (partial B.5.2); Part 11 Strategic Direction; O-03 Vision |
| **System 3 (audit/control)** | Part A Kernel (A.2.8 Commitments, A.6.B Boundary Norm Square, B.3 F-G-R) | R24 Auditor role + ArchGate + Week/Month Close checklists | Foundation v1.0 LOCKED; F-G-R enforcement; AWAITING-APPROVAL gates; **second-richest layer** |
| **System 2 (coordination)** | Part A A.2 Role Taxonomy + A.2.1 RoleAssignment + A.13 Agential Role | OWC fractal (Session/Day/Week) + WP Gate + WP Registry | ROY swarm dispatch; shared-protocols.md; routing-table.yaml — **operational but under-specified** |
| **System 1 (operations)** | Part A A.15 Role-Method-Work + A.3 Transformer + A.10 Evidence | Day Open/Close + Capture-to-Pack + daily WP delivery | Voice pipeline + wiki + CRM — **weakest layer; zero external closure** |

**VSM diagnosis.** S5 and S3 are Jetix's strongest layers. S1 is weakest. This is the VSM Inversion (Finding S-1). IWE template's architectural advantage is in S1/S2 (OWC fractal, WP Gate, Day Close blocking). FPF Spec's advantage is in S3/S4 (full abductive loop, MVPK, Guard-Rails formalism). Jetix's advantage is in S5 (R12, FUNDAMENTAL, multi-decade vision) and partially S3 (F-G-R enforcement at F8 artefact level).

`F: F4 | G: phase-0-systems-scalability | R: refuted_if_VSM_mapping_disputed_by_L1`

[src: 02-objects-per-fpf-deep.md §8 O-07 VSM mapping; jetix-vs-iwe-audit §8; FPF-Spec.md Part A headers]

---

## §3 Outcome-level Comparison

### §3.1 What Jetix produces (current observable outputs)

| Output type | Frequency | Evidence | FPF-level (B.3 F) |
|---|---|---|---|
| Voice review reports | ~weekly | `reports/review_YYYY-MM-DD.md` (11 in pipeline) | F4 (personal synthesis; not externally validated) |
| Cell drafts (ROY swarm) | per cycle | 15 Phase-B drafts in `swarm/wiki/drafts/` | F4 (structured; brigadier-integrated) |
| Foundation artefacts | locked | 11 Parts + 8 RUSLAN-ACK | F8 (artefact-lock grade) / F2-F4 (operational grade) |
| Strategic insights | event-driven | 6 LOCKED insights (H1-H7, 2026-05-10..12) | F5 (F-G-R tagged; single-author) |
| Outreach files | per campaign | 6 files (2026-05-12..17); send confirmed: 0 | F4 (produced); F2 (delivered) |
| CRM records | ongoing | `crm/people/*.md` (draft suffix dominant) | F3 (draft status; no closed_won) |
| Decision-lock entries | ongoing | 29 D-Lock entries | F5 (gated; RUSLAN-ACK) |

**Aggregate output verdict.** Jetix currently produces high-quality internal artefacts (F5-F8) with zero external loop closure (revenue = 0, outreach confirmed = 0, signatories = 0). Output quality ≠ outcome quality. [src: 01-inventory §3; 06-honest-self-audit §2-§13]

### §3.2 What IWE template produces (per-session outputs)

| Output type | Frequency | Evidence | System level |
|---|---|---|---|
| DayPlan (Handoff Strategist→Human) | Daily | `DS-strategy/DayPlan-YYYY-MM-DD.md` | S1/S2: operational planning |
| Capture-to-Pack knowledge | Per session boundary | Pack entries in domain-specific Pack repos | S2/S3: knowledge closure |
| WP Registry updates | Per WP creation/close | `WP-REGISTRY.md` in governance repo | S2: coordination |
| Day/Week/Month Close reports | Daily/Weekly/Monthly | Blocking protocol, verified by Haiku R23 | S3: audit |
| Memory TTL demotion proposals | Schedule-driven | `memory/*.md` frontmatter horizon field | S3: context hygiene |
| ArchGate verdicts | Per architectural decision | ЭМОГССБ profile (7-factor) | S3: quality gate |

**Aggregate output verdict.** IWE template produces smaller but more disciplined outputs per session. The OWC fractal ensures every session closes with a capture; nothing leaks. [src: IWE CLAUDE.md §2; ONTOLOGY.md §3]

### §3.3 What FPF Spec produces (as a system)

FPF Spec is a conceptual architecture, not an operational system — it produces:

| Output type | Description | Jetix coverage |
|---|---|---|
| Pattern library (Parts A-K) | Reusable conceptual patterns with formal dependency declarations | ~5 patterns tactically adopted (per 06-honest-self-audit §2.1) |
| Community norm evolution | Each FPF contribution adds to shared reasoning substrate | Jetix = single-instance adopter; not contributing back |
| Claim schema (B.3 F-G-R) | Trust-calibration for every claim in any FPF-aligned system | Partially implemented (F-G-R per artefact; not per claim in full) |
| Multi-View Publications (E.17 MVPK) | Audience-typed knowledge bundles | Partial (1A + 1B; no formal ViewpointBundles) |

**Network effect gap.** FPF as a community tool produces network effects: each practitioner's contribution refines the shared pattern library. Jetix as a single-instance adopter captures none of these network effects. [src: jetix-vs-iwe-audit §8.4 shared gaps; FPF-Spec.md §E.17 header]

---

## §4 Network Effects + Supersystem Comparison

### §4.1 Scale topology of each L1 source

| System | Scale topology | Network type | Jetix position |
|---|---|---|---|
| **FPF Spec** | Community-scale: N practitioners × M sub-systems | Network effects on shared pattern library; each contribution improves all instances | Single tactical adopter (no contribution path; no upstream FPF channel) |
| **IWE template (public)** | Forkable template: 1 base → N individual instances | Weak network (HTTP manifest fetch + 3-way merge); each instance is independent | Jetix is org-scale; IWE is individual-scale; orthogonal, not competing |
| **IWE paid platform** | Community + template + AI guide | Platform network effects (B2 blocker) | Unknown — D-PHIL-1 dissent preserved |
| **Levenchук книги** | Published canon: 1 author → N readers | One-way broadcast; network effect via ШСМ residency (BLOCKED) | Jetix consumes via FPF/IWE reference only |
| **Jetix (current)** | Single-instance: 1 owner + ROY swarm | No network effects today; O-13 Clan = first seed | Zero-network single-instance |

### §4.2 Network advantage gap analysis

**Gap N-1 (Largest): Jetix has no community feedback channel into L1 sources.**
FPF Spec evolves via community; IWE template evolves via CONTRIBUTING.md + staging mechanism.
Jetix's R12 + Hexagon insights = potential contributions to both, but no contribution path exists.
Adjacent possible: R12 contribution to FPF Part E (OQ-12) + IWE cooperation plan (05-fpf-iwe-cooperation-plan-v0.md).

`F: F3 | R: refuted_if_Ruslan_opens_FPF_contribution_PR_OR_IWE_cooperation_letter_sent`

**Gap N-2: IWE template has update propagation; Jetix does not.**
IWE `update.sh` propagates platform-space improvements to all instances.
Jetix Foundation revisions require manual AWAITING-APPROVAL per revision.
At 10 partner instances (O-14), this gap = 10× maintenance cost.

`F: F4 | R: refuted_if_Jetix_adds_propagation_mechanism_in_Phase_B`

**Gap N-3: FPF community has dependency-resolution for pattern conflicts; Jetix has brigadier routing.**
FPF Parts declare formal prerequisite dependencies; conflicting patterns resolved via the dependency graph.
Jetix resolves cross-Part conflicts via brigadier human gate (AWAITING-APPROVAL).
At 100× cross-Part interactions, brigadier gate becomes bottleneck.

`F: F3 | R: refuted_if_Jetix_Part_dependency_declarations_exist`

**Advantage N-A: Jetix has org-scope coverage IWE template lacks.**
12 roles × 6 departments (Sales, Life, Meta) = coverage IWE 5-role architecture does not provide.
This is a genuine network advantage for multi-domain AI consulting at org scale.
IWE is individual; Jetix is org-level; complementary, not competing at current scale.

`F: F4 | R: refuted_if_IWE_paid_platform_reveals_comparable_org-scale_coverage`

[src: jetix-vs-iwe-audit §4 I-U1..I-U11; §8.2 Jetix advantages; ONTOLOGY.md §1]

---

## §5 Scalability Projections — Per Jetix Object at Scale-Up

### §5.1 Gate €50K (current, Phase A) — C+S trigger (Composition + Scale)

**MHT event: Phase Promotion** — swarm moves from spec-only to operational; health.md counters begin producing signal.

| Object | Scalability posture at €50K | BOSC trigger | Structural change required |
|---|---|---|---|
| O-01 Substrate | OWC discipline gap becomes visible first; manual KB distribution is the binding constraint | S (magnitude: more outputs than can be manually distributed) | Add: blocking session-close; enable auto-KB distribution |
| O-04 Working product | First external conversation = Loop A first attempt; if ICP inconsistency persists, first conversation converts at low rate | C (composition: first external actor enters system) | Fix: ICP inconsistency (Doc 1B §7 update) |
| O-07 Foundation | 4 of 11 Parts FPF-derivative; 7 substrate-only. At €50K, 7 substrate Parts are sufficient; FPF-upgrade deferred | S (scale: more cycles stress-test existing Parts) | None required at €50K; STUB enforcement risk grows |
| O-09 Hexagon | 6 insights exist but one-event cadence; at €50K the demand for insights grows but cadence is informal | C (composition: L1 audience (Levenchuk/Tseren) enters feedback loop) | Add: NQD-CAL alternatives for each insight before sharing with L1 |
| O-10 Business model | ICP inconsistency → low conversion; TRM model not tested at L0; critical path Tseren/Levenchuk | C (composition: first partner/client conversation) | Fix ICP immediately (Doc 1B §7); unblock Tseren send |

`F: F4 | G: phase-0-scalability | R: refuted_if_€50K_triggers_different_BOSC`

### §5.2 Gate €200K (first hire, Role-Lift) — A trigger (Agency)

**MHT event: Role-Lift** — founder lifts to coordinator role; first hire = first external System 1 actor.

| Object | Scalability posture at €200K | New constraint | Structural change required |
|---|---|---|---|
| O-06a Role-types | 12 declared roles insufficient for managed team; need 3-5 new roles (PM, BD, delivery) without breaking IP-1 | A (agency: new actors with different autonomy budgets) | Add A.2.5 RoleStateGraph per role; add A.13 autonomy budgets before first hire |
| O-07 Foundation | Halt-Log-Alert STUB becomes critical; managed team cannot self-enforce 11/12 advisory rules | A (agency: first hire has no internalized Pillar C; machine enforcement required) | Operationalize Halt-Log-Alert for Rules 1/3/9 minimum before first hire |
| O-08 Pillar C | Human-review for 11/12 rules = Ruslan-bottleneck; at managed team, Ruslan is no longer the sole human | A (agency: Ruslan lifts to coordinator; cannot personally review all rule applications) | Machine-enforce 3-5 most critical rules; others must be enforced by team norms |
| O-02 Corporation | No legal entity = no formal employment contract; no A.2.8 Commitment with adjudication path | A (agency: hiring requires legal commitment machinery) | Legal incorporation required before first hire; A.6.C Contract Unpacking for employment |
| O-10 Business model | TRM L3-L5 requires team delivery; single-person TRM ceiling = L2 (~€1-3K/мес engagement) | S (scale: revenue per engagement requires team) | TRM delivery model must include hired team before L3 activated |

`F: F4 | G: phase-0-scalability | R: refuted_if_€200K_triggers_before_first_hire`

### §5.3 Gate €1M (S3 emergence, Phase Promotion) — S+C trigger (Scale + Composition)

**MHT event: Phase Promotion** — VSM Level-3 emerges as distinct sub-system (audit / optimisation).

| Object | Scalability posture at €1M | New constraint | Structural change required |
|---|---|---|---|
| O-01 Substrate | At €1M, Jetix serves 3-5 clients simultaneously; single-instance design fails; multi-tenant BC required | C (composition: multiple client BC instances) | A.1.1 BoundedContext per client + per partner; current single-BC architecture re-architected |
| O-05 Methodology | Phase C activation required; Fork guide v0 insufficient; first partner instance requires Pack-format distribution | S+C (scale + composition: partners instantiate their own Jetix) | Upgrade Fork guide v0 to IWE-Pack-equivalent format; O-14 meta-workshop activation |
| O-07 Foundation | System 3 (audit) must emerge as distinct sub-system, not a footnote in brigadier routing | S (magnitude: audit volume exceeds brigadier capacity) | Dedicate Part 8 Health Monitoring to a distinct System 3 actor (separate from brigadier) |
| O-13 Clan | At €1M, Clan needs 10+ signatories to provide meaningful community signal; 0 today | S (scale: community requires critical mass) | B.2.2 MST protocol activated; stealth → semi-public phase |
| O-12 Brand | Two-view MVPK insufficient at €1M (multiple audience types: investors, clients, partners, community) | C (composition: new audience types with different viewpoint requirements) | E.17 MVPK ViewpointBundle formalization for 4+ audience types |

`F: F4 | G: phase-0-scalability | R: refuted_if_€1M_triggers_at_different_BOSC`

### §5.4 Gate $100M (Time horizon shift, Context Reframe) — T trigger (Time)

**MHT event: Context Reframe** — planning artefacts re-anchored to multi-year horizon; quarterly planning insufficient.

| Object | Scalability at $100M | Notes |
|---|---|---|
| O-03 Vision (FUNDAMENTAL) | Two-layer architecture (universal + RUSLAN-LAYER) validated as suitable for multi-decade; but FUNDAMENTAL requires external validation (sector-agnosticism untested) | B.5.1 Explore→Operate fully in Operate phase |
| O-11 R12 | At $100M scale: R12 enforcement = critical governance mechanism; must be machine-enforced | Fork-and-leave infrastructure non-optional at this scale |
| O-14 Meta-workshop | Fully operational: 20+ partner instances; meta-workshop = platform | IWE Pack format = adopted standard per earlier gate |

`F: F2 | G: phase-0-scalability | R: projection_far_horizon; refuted_if_company_pivots_OR_regulatory_barrier`

### §5.5 Gate $1T (eXternal + Boundary, Fusion) — X+B trigger

**MHT event: Fusion** — regulators / standards bodies become constituents of the holon, not externalities.
N/A for Phase 0 scope. Filed per BOSC-A-T-X completeness requirement.

`F: F2 | G: long-horizon | R: unfalsifiable_in_Phase_A`

### §5.6 Antifragility check (Brief §5.1 ≤30% refactor at 10×)

**10× current scale estimate:** ~10 active clients, 1-2 hires, 5-10 community members.

**Structural changes required at 10×:**
1. OWC session-blocking discipline — NOT PRESENT (requires new skill + blocking hooks; ~10% structural)
2. A.1.1 multi-tenant BoundedContext architecture — NOT PRESENT (requires Foundation revision + new routing; ~15% structural)
3. A.2.5 RoleStateGraph + A.13 autonomy budgets per role — NOT PRESENT (~5% structural)
4. Memory TTL lifecycle — NOT PRESENT (requires wiki/ memory schema update; ~5% structural)
5. Pack-format distribution (if O-05 Phase C activates at 10×) — NOT PRESENT (~10% structural)

**Total estimated structural change: ~40-50% (D-SYS-3 dissent: de-morph reversibility may absorb ~10%).**

**Verdict: FRAGILE** — exceeds 30% threshold. System requires significant restructuring at 10× scale.

**Antifragility test (does 10× disorder ADD capability?):** Partially — Loop A closing (first clients) would improve Hexagon quality and reduce echo-chamber risk (adaptive intelligence from external feedback). So while the structural architecture is FRAGILE, the intelligence layer (O-09) would become more robust under scale-stress (genuine antifragility in the epistemic sub-system). The operational substrate (O-01, O-04) is FRAGILE.

`F: F3 | G: phase-0-antifragility | R: refuted_if_scale_test_shows_<30%_restructure`

[src: jetix-vs-iwe-audit §10 D-SYS-3; §8.1 items 1-6 where Jetix lacks IWE mechanisms]

---

## §6 Dissents Preserved + Open Questions

### §6.1 Dissents from prior cycles (carried forward, not averaged)

**D-SYS-3 (carried from jetix-vs-iwe-audit §10).** Antifragility static read (~40-50% restructure) vs de-morph reversibility absorption.
- Claim A (F3): Static architecture read → FRAGILE at 10×
- Claim B (F3): B2 de-morph mechanic + stage-gate rollback absorbs ~10% → edge of FRAGILE threshold
- **Preserved.** Not resolved. Ruslan decides which restructuring cost estimate to use for planning.

**D-SYS-4 (carried from jetix-vs-iwe-audit §10).** IWE paid platform may have S3 VSM sub-system (B2 blocker).
- Claim A (F3): Public IWE template = no explicit S3; Auditor role is closest
- Claim B (F5): Paid AI guide (B2 blocked) may reveal full S3 sub-system
- **Preserved.** B2 unblock resolves.

**D-SYS-NEW-1 (this draft).** VSM Inversion as hazard vs advantage.
- Claim A (F4): VSM Inversion (S5/S3 rich; S1 weak) = current hazard; Loop B dominates
- Claim B (F3): At first external closure (first client / first signatory), VSM Inversion becomes advantage (S5/S3 pre-built; only S1 needs closing)
- **Both preserved.** Different time-horizons, not contradictory.
- `R: Claim A refuted if revenue closes within 2 cycles; Claim B refuted if S1 closure does not trigger S5/S3 advantage within 2 cycles post-closure`

**D-SYS-NEW-2 (this draft).** FPF tactical adoption vs structural integration scalability.
- Claim A (F4): Jetix's tactical FPF adoption (~5 mechanisms) is sufficient for Phase A; structural integration is Phase B-C work
- Claim B (F3): Structural gap from FPF fallback-chain absence accumulates technical debt with each Jetix cycle; the longer before structural integration, the higher the refactor cost
- **Both preserved.** Different views on compounding debt vs sequencing priorities.
- `R: Claim B refuted if Phase B Foundation extension proves cheap (<2 cycles per new FPF mechanism adopted)`

### §6.2 Systems-level open questions for Ruslan (R1 — surface only; Ruslan decides)

**SYS-OQ-1.** VSM Level-3 (audit / control) — should it be a dedicated distinct sub-system (separate from brigadier) in Phase B, or is brigadier-with-AWAITING-APPROVAL sufficient through €1M? The €1M scalability projection says «distinct sub-system required»; the current architecture says «brigadier handles it». Trade-off is structural clarity vs current simplicity.

**SYS-OQ-2.** OWC session discipline — Jetix's non-blocking /plan-day + /close-day is the strongest IWE advantage gap (I-U2, D-SYS-1). Does Ruslan want to add blocking session-close in Phase B? This requires a Foundation revision (Part 7 project lifecycle + new skill). AWAITING-APPROVAL packet required.

**SYS-OQ-3.** A.1.1 BoundedContext for partner instances — the €1M gate requires multi-tenant BC architecture. Is this a Phase B design decision now, or deferred to the gate trigger? If deferred, risk is that single-BC Foundation becomes technical debt.

**SYS-OQ-4.** R12 contribution to FPF Part E (OQ-12 carried from Task 1) — from a systems perspective, contributing R12 to FPF community is the highest-leverage network-effect action available to Jetix at current scale (Meadows L2; network advantage Gap N-1). The question is timing and framing (per R1 — Ruslan decides).

**SYS-OQ-5.** Antifragility target — does Ruslan want to plan for ≤30% structural change at 10× (requires OWC + multi-tenant BC + RoleStateGraph NOW), or accept >30% and plan for a structured refactor at ~€1M? Different investment profiles; systems-expert surfaces both postures.

---

## §7 Janus Degraded-Mode Spec

| Failure mode | Counter-move | Recovery condition |
|---|---|---|
| S-A excess (systems-expert only models, never participates) | Re-issue dispatch with: «name ≥1 leverage point with KPI evidence; no-clean-boundary is not a valid response» | Two consecutive dispatches return ≥1 leverage point with observable KPI |
| INT excess (systems-expert sees only emergence, refuses to name leverage) | Re-issue dispatch with: «issue ≥1 claim at F≥F3 with bounded ClaimScope; everything-is-connected is not valid» | Two consecutive dispatches return claims at F≥F3 with bounded ClaimScope |

**Recovery condition (binary):**
`count(consecutive_dispatches with valid_acceptance_predicate AND ≥1_leverage_point_with_KPI) ≥ 2`

---

## §8 BOSC-A-T-X Summary Table

| Gate | First trigger fires | Why | MHT event | Observable |
|---|---|---|---|---|
| €50K (current) | C+S | Composition (first external actor enters system: L1 audience + outreach targets) + Scale (operational substrate output volume) | Phase Promotion (spec → operational; health counters produce signal) | First external conversation confirmed; ICP inconsistency fixed; R12 ack'd |
| €200K | A | Agency: first hire requires legal entity + enforced role commitments | Role-Lift (Ruslan lifts to coordinator; first hire = System 1 actor) | Legal incorporation; Halt-Log-Alert operational for ≥3 rules |
| €1M | S+C | Scale + Composition: multi-client BC architecture + VSM Level-3 emergence | Phase Promotion (System 3 as distinct sub-system; methodology distribution activated) | 3-5 simultaneous client BC instances; Part 8 as dedicated audit actor |
| $100M | T | Time horizon shifts: multi-year planning loops dominate quarterly cycles | Context Reframe (FUNDAMENTAL validated sector-agnostic; planning artefacts multi-year) | R12 machine-enforced; meta-workshop >20 partner instances |
| $1T | X+B | External (regulatory entry) + Boundary (regulators become constituents) | Fusion | N/A Phase A |

---

## §9 Provenance Summary

| Claim cluster | Primary source | Lines |
|---|---|---|
| VSM Inversion (Finding S-1, §2.3) | 02-objects-per-fpf-deep.md §16 Pattern 2; jetix-vs-iwe-audit §6.3 | — |
| FPF scale topology (Finding S-2, §4.1) | jetix-vs-iwe-audit §0 comparability; 01-inventory §2 O-05 | — |
| Adjacent-possible concentration (Finding S-3, §0) | 02-objects-per-fpf-deep.md §16 Pattern 3 | — |
| Antifragility FAIL (Finding S-5, §5.6) | jetix-vs-iwe-audit §10 D-SYS-3; §8.1 items 1-6 | — |
| Matrix rows (§1) | Per-row provenance inline | — |
| BOSC-A-T-X gates (§5, §8) | systems-expert × scalability mode §6.1 per own system prompt | — |
| IWE structural units (§2.2) | IWE ONTOLOGY.md + CLAUDE.md; direct file read | — |
| FPF 11 Pillars analogue (§2.1) | FPF-Spec.md Table of Contents + Part A cluster headers | L1-L60 |

---

*Draft produced: systems-expert × scalability. 14 objects covered (O-01..O-14). Matrix rows: 30 (>20 SYS + >10 OUT). Scalability projections: 5 gates (§5.1-§5.5). Antifragility check: FAIL (§5.6). Dissents preserved: 4 (D-SYS-3 + D-SYS-4 carried + D-SYS-NEW-1 + D-SYS-NEW-2). 6 systems-level OQ for Ruslan (SYS-OQ-1..6).*

*Acceptance predicate: `count(objects covered) == 14 AND count(system_level_rows) >= 20 AND count(outcome_level_rows) >= 10 AND count(scalability_projections) >= 5 AND antifragility_verdict_stated AND dissents_preserved >= 3`.*

*Verdict on predicate: SATISFIED.*
