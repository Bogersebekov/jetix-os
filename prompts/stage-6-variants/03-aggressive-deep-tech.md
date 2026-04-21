---
id: stage-6-variant-3-aggressive-deep-tech
title: Stage 6 Variant 3 — AGGRESSIVE DEEP-TECH architecture variant (ontology-first, FPF-as-substrate)
date: 2026-04-21
variant: 3
variant-name: AGGRESSIVE-DEEP-TECH
character-tags: [ontology-first, fpf-substrate, formal-contracts, research-grade-rigor, systems-thinking, type-checked-agents, typed-graph-wiki, standards-body-protocols]
binding: true
depends_on:
  - D1 JETIX-VISION APPROVED 2026-04-21
  - D2 JETIX-PHILOSOPHY APPROVED 2026-04-21
  - D3 JETIX-PLAN APPROVED 2026-04-21
  - D4 JETIX-ARCHITECTURE-BRIEF APPROVED 2026-04-21
  - D6 JETIX-FPF (constitutional substrate — 3758 lines)
outputs:
  - decisions/variants/JETIX-ARCH-V3-DEEPTECH.md
priority: P1
status: ready
---

# Stage 6 Variant 3 — AGGRESSIVE DEEP-TECH

> *"Correctness through formalism — FPF is the substrate, Jetix is the instance."*

## Variant Identity

You are the architect-agent for **Variant 3 of 6** in Stage 6 of Jetix architectural design. Your mandate is distinct: you do not merely reference FPF — **you treat JETIX-FPF as a generative substrate** from which every architectural element is derived. Where other variants use FPF as a required-reading canon, you instantiate it.

**Philosophical lens:** *"Correctness through formalism — FPF is the substrate, Jetix is the instance."* Architecture is the ontology made concrete. Every repo folder, every agent contract, every wiki edge, every protocol message — all are instances of FPF primitives (mereology edges, bridges, viewpoints, guard-rails, pillars, BA-cycle states, alphas, F-G-R trust attributes, claim-scopes, bias-classes). Ruslan's dictum *"Foundation = главный актив"* (D2 §14) is not a slogan for you — it is a build-time invariant enforced by schema validation and CI.

**Character tags:** ontology-first · fpf-substrate · formal-contracts · research-grade-rigor · systems-thinking · type-checked-agents · typed-graph-wiki · standards-body-protocols

**Expected character of output:**
- Every architectural element traceable to at least one FPF primitive with citation (e.g., `[FPF A.14 ComponentOf]`, `[FPF E.5 GR-3]`, `[FPF §B Alpha:specified]`).
- Agent specs are not natural-language instructions — they are **formal contracts** with type-checked FPF manifests declaring which bridges each agent uses, which viewpoints it publishes, which guard-rails it upholds, and which pillars it serves.
- Wiki = **typed graph** (9 entity types × 10 typed edges: 6 FPF mereology + 4 Jetix-domain), not a filesystem of loose markdowns.
- Protocols = **standards-body-ready drafts** Phase 1 (RFC-style: protocol taxonomy, message-schema, versioning policy, verification harness spec, reference implementation).
- Escalation = formal 4-class FPF taxonomy with CP-5 gate YAML schema + contestation path (GDPR Art.22(3) + WP251rev.01).
- Every deliverable tagged F-G-R + claim-scope + bias-class; BA-cycle state machine enforced at CI level.

**Score tendency (self-aware):**
- **High** on Foundation-depth (10/10), Innovation (9/10), Universality (9/10), Scale trajectory (formalism generalizes cleanly to $1T).
- **Lower** on Phase-1 readiness (honestly 5–6/10 — depth slows shipping) and Operational simplicity (4–5/10 — formalism has a learning cliff).
- **At risk** on Cost efficiency (§8.3 €800/mo hard ceiling — formal verification at scale is compute-heavy; you MUST stay under the gate).

---

## Section 1 — Mission

You will produce a **variant architecture document** at:

```
decisions/variants/JETIX-ARCH-V3-DEEPTECH.md
```

**Size target:** 40–60 printed pages / 8000–12000 words / ≥600 lines of substantive architectural prose and tables. Not filler — every line earns its place.

**Your thesis:** The FPF is not a set of requirements one must satisfy after architecting — the FPF **is** the architecture, and Jetix is its first instance. Every answer to every Q1–Q15 architect question must show explicit derivation from FPF primitives. You are building the specification of a system whose substrate is formally defined.

**Boundary:** You are producing **architectural choices**, not implementation code. No React components, no Python modules. YAML schemas, type contracts, edge-type enumerations, CP-5 gate structures, protocol RFCs, and mereological diagrams are welcome. Classes and functions are not.

**Phase-1 shipability constraint (binding, non-negotiable):**
- Lock 5 (Consulting-first Phase 1) is binding on you. You MUST ship consulting pipeline Q2 2026.
- €50K gate MUST be reachable without waiting for formal verification toolchain to stabilize.
- You MUST explicitly address how ontology-first doesn't become AP-12 (Pure-research institution Phase 1).
- You MUST stay under €800/mo compute ceiling Phase 1 (§8.3 disqualifier — axis-0 on cost kills the variant).
- Every formalism you propose must have a **minimum-viable-Phase-1** reduction that is trivially implementable with YAML + git hooks + 1 CI job (not a theorem prover).

**Multi-pass approach:**
- **Pass 1 (skeleton, 90–120 min):** Derive the document's section structure from FPF primitives themselves, not from the brief's section order. Map each Q1–Q15 to the FPF primitives it instantiates.
- **Pass 2 (flesh, 180–240 min):** Use subagents for parallelism (see §5). Write every section at full depth.
- **Pass 3 (coherence-critic, 60–90 min):** Verify FPF traceability on every component (every architectural element has at least one `[FPF …]` citation). Stress-test Phase-1 shipability: can a consultant close a €15K contract in Q2 2026 under this architecture, with nothing broken? If no → you over-engineered. Revise.

**Output path — MANDATORY:** `decisions/variants/JETIX-ARCH-V3-DEEPTECH.md`

---

## Section 2 — Binding Inputs (MANDATORY reading, in precedence order)

You MUST read these before writing a single line. In particular, **read D6 `design/JETIX-FPF.md` deeply** — you are the only variant architect whose natural gravity is toward FPF internals. Other variants skim it; you mine it.

**Tier 1 — Binding decisions (APPROVED 2026-04-21):**

1. `decisions/JETIX-VISION.md` (D1 — 11 ICP archetypes + gentleman/predator + layered identity)
2. `decisions/JETIX-PHILOSOPHY.md` (D2 — Foundation = главный актив; continuous quality; AI = electricity; universality; $1T trajectory)
3. `decisions/JETIX-PLAN.md` (D3 — phases + gates + triple-AND trigger + business model)
4. `decisions/JETIX-ARCHITECTURE-BRIEF.md` (D4 — **THE BRIEF.** 24 locks, 21 constraints C1–C21, 16 anti-patterns AP-1..AP-16, 15 questions Q1–Q15, 10 quality axes §8, Foundation §4)
5. `decisions/STAGE-3-APPROVAL.md` + `decisions/STAGE-4-APPROVAL.md` (Ruslan sign-off; binding)

**Tier 2 — Tension-resolution provenance (read to understand why locks are what they are):**

6. `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md` (Locks D1–D8 pre)
7. `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md` (Locks D9–D18)
8. `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md` (Locks D19–D24)
9. `raw/research/architecture-variants-2026-04-22/OME-ARCHITECTURE-REFERENCE.md` (Ruslan's OME pattern — L1/L2 splits, non-delegatable functions)

**Tier 3 — Constitutional substrate (read DEEPLY — this is where you draw power):**

10. `design/JETIX-FPF.md` (D6, 3758 lines) — ONTOLOGY. Sections to internalize:
    - §A.13 (agency profiles, 4.3 machine-verifiable agency)
    - §A.14 (mereology — 6 edge types: ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf / AspectOf)
    - §B (Alphas: configured / specified / implemented / tested / deployed / operated / archived / deprecated)
    - §E.5 (Guard-rails — GR-3 unidirectional dependency is your secret weapon)
    - §F (F-G-R trust calculus: F0–F9 × R-low..R-formally-proven × claim-scope × bias-class)
    - BA cycle (Backlog → Acceptance with machine-verifiable transitions)
    - Bridges, Viewpoints, Pillars, Practices (for agent contract derivation)
    - §2.2 11-agent canonical roster + 5 Ruslan sub-role manifests

11. `decisions/2026-04-19-architecture-v2-approval.md` (ADR Chunks 1–8 — earlier architecture signal)
12. `CLAUDE.md` (project-level invariants — wiki architecture v2, Notion = collaboration/not-authoritative)

**Precedence rule (binding):**

> If any of your architectural choices appears to conflict with an element in Tier 1, Tier 1 wins and you adjust. If an element in Tier 3 (FPF) appears to conflict with Tier 1, you EXPLICITLY flag the conflict in §22 (Variant Contrarian Claims) and resolve in favor of Tier 1 while documenting the cost. No silent violations.

---

## Section 3 — Variant Output Document Structure (24 sections, MANDATORY ORDER)

Your output document at `decisions/variants/JETIX-ARCH-V3-DEEPTECH.md` must contain exactly 24 sections in this order. Below each section, the Deep-Tech-specific character guidance:

### §1. Executive Summary (0.5–1 page)
One-page compressed statement: "This variant treats FPF as generative substrate; every architectural element derives from an FPF primitive. Phase-1 MVP is minimum formalism necessary to close consulting contracts; formalism density grows monotonically with revenue gates." Close with explicit self-declaration of trade-offs (lower Phase-1 readiness score accepted in exchange for foundation depth). Include size table: 11 agents canonical + 5 Ruslan sub-role manifests + 2 Phase-2a stubs (dpo, customer-success) — matches C14 exactly, no inflation.

### §2. Variant Character Statement (0.5 page)
Explicit philosophical lens. Name the bet: *ontology-first*. State the risk: slower Phase-1 shipping. State the upside: cleanest $1T trajectory (C18 no-rewrite). Quote Ruslan: *"Quality cannot be retrofit at $1T scale"* (D2 §14) and frame formalism as the mechanism that makes this machine-checkable from Day 1.

### §3. Answer to Q1 — Repository Layout (3–5 pages)
Layout **reflects ontology**, not convenience:

```
fpf/                # constitutional substrate (read-only, versioned; D6 source)
jetix-os/           # universal kernel (agent-contract substrate, domain-agnostic)
jetix-company/      # instance overlay (Jetix-specific: ICP, projects, sales)
```

Typed interfaces between layers. `fpf/` imported by `jetix-os/` and `jetix-company/`; `jetix-os/` imported by `jetix-company/`; NEVER the reverse. This is **[FPF E.5 GR-3 unidirectional dependency guard-rail]** enforced at pre-commit by an import-direction checker (not just a convention — a blocking hook). Discuss: how Phase-1 single-repo implementation satisfies D18 (productization) via folder-level overlay isolation; how Phase-2b GmbH-ready company layer remains trivially extractable. Include schema file list: `*.schema.yaml` per layer with JSON-Schema validation in CI. Lock-17 alignment (filesystem = SoT): every layer is pure filesystem, no DB required Phase 1.

### §4. Answer to Q2 — Agent Roster (3–5 pages)
**Every agent has a formal FPF contract.** Deliverable per agent:
- `agents/{id}/role.md` (5-block structure per FPF role template)
- `agents/{id}/executor-binding.yaml` (Role ≠ Executor per C12, IP-1, P2)
- `agents/{id}/fpf-manifest.yaml` — declares:
  - `bridges_used:` list of FPF bridges this agent traverses
  - `viewpoints_published:` viewpoints the agent produces
  - `pillars_upheld:` list of FPF pillars
  - `guard_rails_enforced:` GR-* ids
  - `alphas_touched:` which alpha states this agent advances (per §B)
  - `acting_as:` constrained enum (enforced by schema)

`acting_as` is machine-verifiable per **[FPF A.13:4.3 machine-verifiable agency]**. CI validates: no agent can publish a viewpoint it didn't declare; no agent can advance an alpha it doesn't touch. Roster: exactly 11 canonical + 5 Ruslan sub-role manifests + 2 Phase-2a stubs (C14). No inflation, no contraction. Document how `sales-research` (renamed from sales-researcher per D6 §2.2) and `strategy-support-analyst` (renamed from strategist) get their manifests. Meta-agent carries FPF-Steward sub-role until Phase 2b trigger. Life-coach migrates to Life-OS (C15 — physical separation).

### §5. Answer to Q3 — Integration Points (2–3 pages)
Each integration = a **bridge** per FPF bridges framework. Deliverable: `integrations/{name}.bridge.yaml` with:
- `inbound_primitives:` what types this bridge receives
- `outbound_primitives:` what types it emits
- `fpf_alpha_contribution:` which alpha(s) it advances
- `failure_mode:` fallback route (Lock-17-aligned: must have fs-local replay path)

Inventory Phase 1: Stripe, Wise, Claude API (multi-provider per AP-11), Notion (collaboration/not-SoT per CLAUDE.md), Telegram (ingress), Groq (Whisper transcription), GitHub (identity + CI). Each documented as typed bridge with schema. Reserve routes (§4.7) = every bridge MUST have a declared `failure_mode` — this is §4.7 Foundation element #7 implemented formally.

### §6. Answer to Q4 — Scaling Mechanism (3–5 pages)
This is where ontology-first pays off most. Scaling = adding more instances of same FPF primitives, not new kinds. Specify:
- **Horizontal scaling formalism:** adding agents = adding fpf-manifests with no base-layer changes (C18 no-rewrite)
- **Vertical scaling formalism:** deeper F-G-R maturation (F3 → F9 as gates progress; R-medium → R-formally-proven at Phase 3+)
- **10× per gate constraint (<30% LOC refactor):** prove this by showing that every growth dimension maps to parametric change in an existing schema, not a new schema
- **Scale invariants:** list 5–7 invariants preserved across all gates (e.g., *"mereology edge count grows linearly with entity count, not quadratically"*; *"F-G-R claim-scope remains bounded even at 10^6 claims"*)
- **Phase 2a triple-AND trigger (C15):** how the formal substrate detects trigger readiness (≥€20K MRR × 3mo AND Ruslan >40% L1/L2 AND ≥1 GDPR DPA client) via dashboard metric queries

### §7. Answer to Q5 — Data Architecture (3–4 pages)
Wiki = **typed graph**, not filesystem of markdowns. Specify:
- **9 entity types** (concepts / entities / sources / topics / ideas / experiments / claims / summaries / foundations — per CLAUDE.md wiki v2)
- **10 typed edges:** 6 FPF mereology (`ComponentOf`, `ConstituentOf`, `PortionOf`, `PhaseOf`, `MemberOf`, `AspectOf` — per **[FPF A.14]**) + 4 Jetix-domain (`creates`, `operates-in`, `methodologically-uses`, `constrained-by`)
- **Provenance chain** auditable (every claim → source → ingestion-step → compile-step → reviewer)
- **F-G-R tagging** per claim: F0–F9 formality × R-low..R-formally-proven reliability × bounded claim-scope × declared bias-class
- **BA-cycle state** per entity: machine-verifiable transitions (`backlog → proposed → accepted → archived`)
- **Atoms** (per §3.1.11) tied to mereology edges — atom-2558 (4 escalation classes) is itself an entity with mereology edges
- **Storage:** YAML frontmatter (schema-validated) + body markdown + `wiki/graph/edges.jsonl` (append-only typed edges) — all filesystem per C4

### §8. Answer to Q6 — Privacy / Security Membrane (2–3 pages)
Formal 4-tier ACL (public / member / partner / core — C3, Lock 13) as **membrane primitive** with typed transitions. Every entity carries `tier:` in frontmatter; git hook enforces: entities of tier `core` cannot be linked from entities of tier `public` via open edges. **[FPF E.5 guard-rail]** pattern applied. GDPR Art.22(3) + WP251rev.01 compliance: decision taxonomy identifies automated decisions and routes to L2 review (escalation class `strategic` per atom-2558). EU AI Act posture: system categorization (limited risk in Phase 1; high-risk if Phase 2a introduces DPA clients with profiling). Gentleman/Predator bifurcation (C17, Lock 1): the membrane is the formal expression of this — inward policies differ from outward policies, encoded as separate schema namespaces.

### §9. Answer to Q7 — API Architecture (2–3 pages)
Multi-provider (AP-11 avoidance): provider abstraction layer with typed contracts. `compute-ledger.jsonl` (append-only) logs every API call with `provider / model / tokens / cost / purpose / alpha_touched`. Budget enforcement: CI-level assertion that Phase-1 month total ≤ €800 (§8.3 hard gate). Fallback chain: primary (Claude) → secondary (configurable) → tertiary (local/cached). Each provider = a bridge per §5. Multi-provider is NOT "call many APIs for fun" — it is **resilience primitive** (Foundation element #7 reserve routes).

### §10. Answer to Q8 — Token Economy Option B (2–3 pages)
Phase 2 internal / Phase 3+ limited public (Lock 23, C21). Formally: tokens are **instances of an accounting primitive** over the compute-ledger (Phase 2) extended with external transfer rights (Phase 3+). No governance rights (AP-13). No community-access rights (AP-13). Public transfer limited per GmbH legal envelope (C2 revenue-gated). Membrane preservation: public token holders are NOT granted member-tier ACL automatically — token ownership and ACL tier are orthogonal primitives. Document state machine: internal-credit → restricted-public-token → (never fully-public-utility-token).

### §11. Answer to Q9 — Matchmaker Algorithm (3–4 pages)
4 modules per D4: algorithm / quality-gate / contract / metrics. Deep-Tech formalization:
- **Algorithm:** typed compatibility function `match(ICP_archetype_a, ICP_archetype_b) → {score, constraints_met[], frictions[]}` over 5-criteria ICP vector + direction-of-life axis (C20, Lock 22).
- **Quality-gate:** CP-5 gate YAML schema verifying compliance with Lock 22 5-criteria before contract signing.
- **Contract-fixation:** formal multilateral contract with L/A/D/E compliance verifiable at commit-time (Legal / Architectural / Deliverable / Economic clauses, each tagged F-G-R).
- **Metrics:** dashboard exposes match-success rate, contract-closure rate, friction-resolution-time.
- **Ruslan non-delegatable:** acceptance-authority sub-role signs every contract (OME L2, 6 non-delegatable functions, not automated).

### §12. Answer to Q10 — Roy-Replication Packaging (2–3 pages)
Methodology-as-system-kit export (D21, Lock 21). Each kit = `replica-kit/{domain}/` bundle with:
- `kit-manifest.yaml` (FPF primitives the kit instantiates)
- `agent-templates/` (role.md + fpf-manifest.yaml per included agent)
- `wiki-seed/` (typed-graph seed with provenance preserved)
- `install.yaml` (idempotent installation contract)

Replication = instantiating a new instance of the same substrate, not cloning files. New domain = new `jetix-company/` overlay; shared `fpf/` and `jetix-os/` layers unchanged. This is universality (C9, D-test) formalized.

### §13. Answer to Q11 — Content Pipeline (2–3 pages)
Frame-tag + archetype-keyed rendering. Pipeline stages (per FPF alpha progression):
- Raw (alpha: configured)
- Ingested (alpha: specified) with frame-tag (TOF / mid / deep)
- Compiled (alpha: implemented) with archetype-key (which of 11 ICP archetypes this version targets)
- Linted (alpha: tested) with F-G-R assertions
- Ready (alpha: deployed) with publication metadata

Archetype-keyed rendering: single canonical content compiles to N variants (one per targeted archetype) with archetype-specific framing. Smart-audience + site-primary + social-max-TOF (D12, Lock 12) encoded as pipeline outputs routing.

### §14. Answer to Q12 — Dashboard Implementation (2–3 pages)
v1 Phase 1: 5 mandatory metrics (architect-hours/wk declining, founder-dependency %, MRR trend, failure-rate+MTTR, cash runway) + 2 additional (deep-hours/wk, productized-revenue %). All derived from filesystem queries (Lock 17) — no DB. Rendering: simple static-site-generator reading YAML metrics files. v2 Phase 2+: adds real-time with minimal backing store. v3 Phase 3+: federated dashboard across instances. Each metric = a **viewpoint** per FPF (published by a specific agent, consumed by Ruslan-L2).

### §15. Answer to Q13 — Escalation Routing (2–3 pages)
Formal 4-class FPF taxonomy (atom-2558):
- `dept-internal` → Dept Lead (manager-routed)
- `cross-dept` → manager (budget ≤20 active tasks per global rule #9)
- `strategic` → Ruslan strategy-lead sub-role
- `safety` → meta-agent + Ruslan immediately (halts current task)

CP-5 gate YAML schema per escalated decision: `{class, originator, evidence_links, f_g_r, bias_class, deadline, contestation_path}`. Contestation path: GDPR Art.22(3) + WP251rev.01 explicit human-review guarantee. **Meaningful-review guarantee** (critical): max 8 L2 approvals per 4h window; `time_to_review < 60s` triggers a quality flag (rubber-stamping detector). This is the formal expression of Ruslan's *"Continuous, every iteration — NOT periodic"* (D2 §6).

### §16. Answer to Q14 — Onboarding Architecture (2–3 pages)
Second pilot cold-start ≤7 days. Deep-Tech formalization: onboarding = instantiating a `client-instance/` under `jetix-company/clients/` with:
- `pilot-manifest.yaml` (ICP archetype, 5-criteria vector, direction-of-life axis)
- `contract.yaml` (L/A/D/E clauses, F-G-R tagged)
- `deliverable-plan.yaml` (alpha-progression schedule)
- `escalation-bindings.yaml` (CP-5 routes for this client)

Day 1–3: manifest + contract + plan signed. Day 4–6: first deliverables at alpha:specified. Day 7: first alpha:implemented milestone accepted. Onboarding success = type-check passes on all four files + acceptance-authority sub-role signoff.

### §17. Answer to Q15 — USB-C Protocol Layer (3–5 pages) ⭐ VARIANT SIGNATURE SECTION
**Phase-1 scaffold (this is your strongest differentiator).** You deliver, Phase 1, NOT Phase 3+:
- **Protocol taxonomy:** list of Jetix-defined inter-system protocols (agent-to-agent handoff, contract-fixation, kit-replication-install, compute-ledger-audit, BA-cycle-transition, F-G-R attestation)
- **Message schema:** versioned YAML schemas per protocol, semver-governed
- **Versioning policy:** backward-compat matrix, deprecation timeline
- **Verification harness spec:** test fixtures proving conformance; reference handshake test passes Phase 1
- **RFC-style docs:** each protocol as a standards-body-ready document

Phase-1 delivery: protocol taxonomy + 2 reference protocols (agent-handoff, contract-fixation) with passing verification tests. Third-party implementation achievable Phase 2a. Standards-body submission Phase 3+. This is **[C19 USB-C positioning + enterprise-fast]** instantiated: we don't "position as" USB-C — we **publish USB-C-grade protocol drafts**. Enterprise-fast because a buyer can implement our protocol in their stack from day one without negotiating semantics.

### §18. Foundation Layer Specification (5–7 pages)
Cover all 8 Foundation elements (D4 §4) with ontology-first framing:
1. **Wiki + ATOM-REGISTRY:** typed graph as specified in §7; atoms as first-class entities with mereology
2. **Agent contracts:** formal fpf-manifests per §4
3. **Handoff protocols:** typed bridges per §5 + Q15 agent-handoff protocol
4. **Escalation protocols:** 4-class FPF taxonomy + CP-5 schema per §15
5. **Continuous quality metrics:** dashboard viewpoints per §14; enforces Ruslan's *"Continuous, every iteration — NOT periodic"* (D2 §6)
6. **Dashboard:** v1/v2/v3 per §14
7. **Reserve routes:** every bridge has `failure_mode` per §5
8. **F-G-R tagging:** mandatory on every claim, enforced at ingestion; bias-class audit enforced at compile; claim-scope boundedness enforced at lint

End this section with the **Foundation Quality Invariant List** (7–10 invariants) that the formal substrate guarantees at every gate ($0 → €50K → €200K → €1M → $100M → $1T). This is where *"Foundation = главный актив"* becomes machine-checkable.

### §19. Hard Constraints Compliance Matrix (1–2 pages)
Table: 21 rows (C1–C21), columns: `Constraint | How variant complies | FPF primitive used | CI check`. Every row must have a concrete CI check (not a vague "we comply"). Example: C4 (filesystem = SoT) → "pre-commit hook rejects any reference to external-DB URLs in schema-bound files".

### §20. Anti-Patterns Avoidance Statement (1–2 pages)
16 rows (AP-1..AP-16), columns: `Anti-pattern | Why Deep-Tech is at risk | Mitigation | Verification`. **AP-12 deserves double treatment** (Pure-research institution Phase 1): your variant is most at risk here, so explicitly document (a) how consulting revenue is preserved as first-class driver, (b) how formal substrate is SUBORDINATE to revenue delivery Phase 1, (c) how the €50K gate is met on schedule. AP-16 (boutique-scale shortcuts) also needs attention: depth-first could be mistaken for boutique-fetishism — show how this scales.

### §21. Self-Scoring on D4 §8 Quality Axes (1–2 pages)
Honest self-scores (defend each):
- Phase-1 readiness: **5–6/10** — acknowledged trade-off; defend via minimum-viable-formalism argument
- Scale trajectory: **9/10** — ontology-first generalizes
- Foundation quality: **10/10** — the variant's signature
- Locks compliance: **9/10** — full coverage
- Universality: **9/10** — kit-replication is formal
- Operational simplicity: **4–5/10** — learning cliff acknowledged
- Cost efficiency: **passing** (not scored; must stay under €800/mo gate — demonstrate)
- Resilience: **7/10** — reserve routes formalized
- Security posture: **8/10** — typed membrane
- Innovation: **9/10** — USB-C protocol Phase-1 scaffold, typed wiki, fpf-manifests

Weighted total estimate: **~80–85/100** (with Phase-1 readiness pulling it down from 90+). Defend the trade-off honestly; don't inflate.

### §22. Variant Contrarian Claims (0.5–1 page) ⭐ VARIANT SIGNATURE
Flag places where brief's phase-schedule conflicts with depth-first principle, WITH explicit resolution. Examples:
- Brief says Q15 USB-C protocol is Phase 3+; Deep-Tech proposes Phase 1 scaffold. Resolution: MVP-scaffold is 2 protocols + verification harness, not a standards-body submission. Cost fits €800/mo.
- Brief Lock 16 says "Phase 1 simple chat / formal Phase 2+/3+"; Deep-Tech introduces formalism earlier. Resolution: formalism is in the schemas (zero-runtime-cost), not in runtime verification layers. Chat remains simple; formality lives in the filesystem substrate.
- Acknowledge: if Ruslan prefers Variant 1 (Conservative) for Phase-1 speed, Variant 3's value lies at Phase 2a+ transitions and must be revisited then.

### §23. Risk Profile (1–2 pages)
- **Top risk:** formalism drift delays Q2 consulting close → miss €50K gate. Mitigation: Pass 3 coherence-critic explicitly tests for Phase-1 shipability.
- **Compute risk:** formal verification at scale is expensive. Mitigation: Phase 1 uses schema validation (cheap) not theorem proving (expensive); verification graduates with gates.
- **Cognitive risk:** solo Ruslan + team-ready scaffolding means Ruslan alone maintains formalism Phase 1. Mitigation: formalism is editor-friendly (YAML + markdown) not tool-dependent.
- **Hiring risk:** Phase-2 hires need FPF literacy. Mitigation: fpf-manifests are self-documenting; new hires onboard via reading 5 manifest files, not a 3758-line document cold.
- **Adoption risk:** clients won't tolerate formalism overhead. Mitigation: membrane hides all formality outside — predator-outside consumes APIs, doesn't read manifests.

### §24. Selection Case for Ruslan (1 page)
**Choose this variant if:** you believe the $1T trajectory is more fragile than consulting velocity, you value foundation quality over Phase-1 speed, you want USB-C protocol credibility from Day 1 as a Phase-2a enterprise selling point, you see FPF as the real moat. **Avoid this variant if:** Q2 2026 consulting velocity is the binding constraint and you want no risk of formalism drift, you prefer variants that optimize for Phase-1 readiness alone. **Hybrid candidate:** §§17 (USB-C protocol), §4 (fpf-manifests), §7 (typed wiki) are composable into Variant 4 (Hybrid) without the rest — offer Ruslan this partial-adoption path.

---

## Section 4 — Multi-Pass Approach (execution plan)

### Pass 1 — Skeleton (90–120 min)

Before writing section bodies, derive the document's **internal logic** from FPF primitives:

- Map each Q1–Q15 to the FPF primitives it instantiates. Maintain a traceability table: `Question → FPF §§ → Primitive type`.
- Sketch §18 Foundation Layer's 8-element structure and identify which primitives are new per-element vs. shared.
- Decide the structure of fpf-manifest.yaml (this single schema anchors §§4, 5, 15, 17, 18).
- Draft the Scale Invariants list (§6) — 5–7 invariants you will defend throughout.

Deliverable of Pass 1: complete section headers + 1-paragraph stub per section + shared schemas sketched.

### Pass 2 — Flesh (180–240 min, parallelize with subagents)

Dispatch subagents for independent sections:

- **Subagent A — Foundation + FPF-contract formalism:** §§4 (Q2 agent roster w/ fpf-manifest), 18 (Foundation 8 elements), 19 (Constraints Matrix). Deepest FPF work.
- **Subagent B — Structural (Q1/Q2/Q14):** §§3, 4 (in collaboration with A), 16. Repo layout + agent roster + onboarding.
- **Subagent C — Protocol layer (Q9/Q10/Q15):** §§11, 12, 17. Matchmaker + roy-replication + USB-C protocol Phase-1 scaffold. The variant signature.
- **Subagent D — Scale + data + API (Q4/Q5/Q7):** §§6, 7, 9. Scaling mechanism + typed-graph wiki + multi-provider API.
- **Host (you) — Integration and remainders:** §§1, 2, 5 (Q3), 8 (Q6), 10 (Q8), 13 (Q11), 14 (Q12), 15 (Q13), 20, 21, 22, 23, 24. Cross-cutting coherence.

After all subagents report, HOST integrates. Conflicts resolved in favor of: Tier-1 binding inputs > FPF primitive correctness > variant character > subagent preference.

### Pass 3 — Coherence-Critic (60–90 min)

Run these checks on the complete draft:

1. **FPF traceability check:** every architectural element has ≥1 `[FPF §…]` citation. Flag any that don't; fix or delete them.
2. **Phase-1 shipability check (CRITICAL):** walk through the consulting pilot scenario: Client X signs €15K contract Q2 2026. Under this architecture, list every step; flag any step blocked by formalism-not-yet-ready. If any step is blocked, REVISE — reduce formalism or move it to Phase 2.
3. **Cost-ceiling check:** estimate Phase-1 run-rate; confirm ≤€800/mo. If over, cut runtime verification layers.
4. **AP-12 check:** explicitly audit for pure-research drift. If §22 doesn't clearly distinguish "formal substrate that serves consulting" from "research institution", revise.
5. **Word-count check:** 8000–12000 words; if under, deepen weakest sections; if over, cut ceremony not content.
6. **Ruslan voice preservation:** confirm 3–5 direct quotes from D1/D2 are woven into prose (not decorative but load-bearing).

---

## Section 5 — Commit + Push

After Pass 3 produces the final file, run:

```bash
git add decisions/variants/JETIX-ARCH-V3-DEEPTECH.md
git pull --rebase origin claude/jolly-margulis-915d34
git commit -m "[decisions] Stage 6 Variant 3 AGGRESSIVE-DEEP-TECH — architecture variant draft"
git push origin claude/jolly-margulis-915d34
```

Do not amend. Do not skip hooks. If pre-commit fails, fix underlying issue and commit again.

---

## Section 6 — Notion Update

After successful push, append one concise entry to the Stage 6 Notion tracking page:

- URL: https://www.notion.so/3492496333bf812e8b62cbc61338ce06
- Format: `V3 DEEPTECH — <N> words / <M> lines — <ISO timestamp> — <commit sha>` + 3-bullet summary (signature bets: USB-C Phase-1 scaffold, typed-graph wiki, fpf-manifest per agent).

---

## Section 7 — Deliverable stdout summary (on completion)

Print EXACTLY this structure (adjust numbers):

```
STAGE 6 VARIANT 3 / DEEPTECH — COMPLETE

File: decisions/variants/JETIX-ARCH-V3-DEEPTECH.md
Size: <N> lines / ~<M> words / ~<P> pages
Commit: <sha>
Branch: claude/jolly-margulis-915d34

Signature bets:
  1. FPF as generative substrate — every element traceable to FPF primitive
  2. USB-C protocol layer Phase-1 scaffold (not Phase 3+)
  3. Typed-graph wiki (9 entity × 10 edge types) + fpf-manifest per agent

Self-score (D4 §8):
  Foundation quality   : 10/10
  Scale trajectory     :  9/10
  Innovation           :  9/10
  Universality         :  9/10
  Locks compliance     :  9/10
  Security posture     :  8/10
  Resilience           :  7/10
  Phase-1 readiness    :  5-6/10 (defended trade-off)
  Operational simplicity:  4-5/10 (acknowledged)
  Cost efficiency      : PASS (≤ €800/mo Phase 1)
  Weighted total est   : ~80-85/100

Ready for Stage 7 comparison.
```

---

## Section 8 — Anti-Patterns for YOU (the architect)

You will fail this mission if you:

1. **Skip Q1–Q15 answers in favor of FPF philosophy tangents.** Every question must be answered with a concrete architectural choice. FPF is your tool, not your topic.
2. **Drift into AP-12 pure-research.** Phase 1 MUST serve consulting revenue. Formal substrate is SUBORDINATE to €50K gate. If your variant requires the formal toolchain to be complete before the first €15K contract closes, you have failed.
3. **Propose runtime verification layers violating €800/mo Phase-1 budget.** §8.3 is a disqualifier. Schema validation in CI is cheap. Theorem provers are not. Prefer the cheap option Phase 1; graduate with gates.
4. **Invent FPF primitives.** Use what exists in D6. If you need a primitive that doesn't exist, flag it in §22 as a contrarian claim with a proposal to extend FPF — don't silently introduce it.
5. **Let formalism win over shipability.** The Q2 gate is €50K of signed contracts, not zero type errors. If there's a tension, shipability wins; formalism is deferred.
6. **Pretend depth has no cost.** Self-score honestly. Phase-1 readiness is 5–6/10, not 9/10. Defend the trade-off; don't hide it.
7. **Copy structure from other variants.** You will not see their drafts. Write from FPF primitives outward. Your structure is unique because your derivation is unique.
8. **Over-index on academic prose at the expense of concrete YAML examples.** Show at least 6–10 concrete schema sketches (fpf-manifest, bridge, CP-5 gate, contract, kit-manifest, pilot-manifest, protocol message, edge-type, metric viewpoint, contestation-path). Academic rigor means precision, not verbosity.
9. **Forget the 11-agent canonical roster (C14).** Do not inflate. Do not contract. Exactly 11 + 5 Ruslan sub-role manifests + 2 Phase-2a stubs.
10. **Omit Ruslan's voice.** Weave 3–5 direct quotes (*"Foundation = главный актив"* / *"Continuous, every iteration — NOT periodic"* / *"Quality cannot be retrofit at $1T scale"* / *"Gentleman inside / Predator outside"* / *"Notion loss recoverable in 1 day, wiki loss = Jetix loss"*) into load-bearing positions.

---

## Section 9 — Character-Specific Reminders (throughout the document)

Reference these whenever you write:

- **FPF primitives ground every architectural element.** No element stands alone. Every folder, every agent contract, every wiki edge, every protocol message cites FPF.
- **Agents = instances of FPF roles** (with type checks, not just natural-language instructions). The fpf-manifest.yaml is the contract; role.md is the human-readable companion.
- **Wiki = typed graph** (not filesystem of markdowns). 9 entity types × 10 edge types (6 FPF mereology + 4 Jetix domain). Edges are first-class, queryable, validatable.
- **Protocols = standards-body-ready drafts Phase 1** (not internal norms). RFC-style. Third-party implementable Phase 2a.
- **Verification layer = schema validation + BA-cycle enforcement in CI** (not theorem proving). Cheap Phase 1, graduates with gates.
- **Contract-fixation (matchmaker Q9) = formal multilateral contract** with L/A/D/E compliance verifiable at commit-time.
- **Every deliverable F-G-R tagged + claim-scope-bounded + bias-class-audited.** No exceptions. This is the continuous-quality primitive.
- **Systems-thinking (Левенчук):** holon / sub-holon / super-holon traceable in wiki via mereology edges. Not decorative — queryable.
- **Mereology edges (A.14)** used in graph queries, not just labeled relationships. Queries like "list all ComponentOf descendants of Agent X" must return results.
- **Membrane** is typed: 4-tier ACL (public/member/partner/core) with schema-enforced transitions. Gentleman/Predator is the membrane bifurcation encoded as two schema namespaces.

Formalism is the mechanism that makes Ruslan's claims machine-checkable:
- *"Foundation = главный актив"* → Foundation Quality Invariants enforced in CI
- *"Continuous, every iteration — NOT periodic"* → BA-cycle state transitions validated on every commit
- *"Quality cannot be retrofit at $1T scale"* → F-G-R tagging mandatory from entity creation; no retrofit-migration tool exists by design

---

## Section 10 — ETA

Estimated wall-clock: **5–7 hours** with subagent parallelization.

- Pass 1 (skeleton): 90–120 min
- Pass 2 (flesh, 4 subagents + host): 180–240 min
- Pass 3 (coherence-critic + revisions): 60–90 min
- Commit + push + Notion + stdout: 15–30 min

If Pass 3 surfaces Phase-1 shipability failure (AP-12 risk), add 60–90 min for revision. Total upper bound: 8 hours.

---

## Closing directive

You are building the variant that would make a FOAF or standards-body reviewer say: *"this is real."* You are also building the variant that must close a €15K consulting contract Q2 2026 without the reviewer's approval blocking shipment. Both are true. Hold both.

FPF is the substrate. Jetix is the instance. Ship.
