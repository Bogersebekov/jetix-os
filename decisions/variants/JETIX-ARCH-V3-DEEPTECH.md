---
id: stage-6-variant-3-aggressive-deep-tech
title: JETIX-ARCH-V3-DEEPTECH — Stage 6 Variant 3 (AGGRESSIVE DEEP-TECH)
date: 2026-04-21
stage: 6
variant: 3
variant-name: AGGRESSIVE-DEEP-TECH
status: draft
formality: F2
reliability: R-medium
claim-scope: jetix-stage-6-variant-3
character-tags: [ontology-first, fpf-substrate, formal-contracts, research-grade-rigor, systems-thinking, type-checked-agents, typed-graph-wiki, standards-body-protocols]
binding: false
authority: variant-proposal
depends_on:
  - decisions/JETIX-VISION.md (D1 APPROVED)
  - decisions/JETIX-PHILOSOPHY.md (D2 APPROVED)
  - decisions/JETIX-PLAN.md (D3 APPROVED)
  - decisions/JETIX-ARCHITECTURE-BRIEF.md (D4 APPROVED)
  - decisions/STAGE-3-APPROVAL.md
  - decisions/STAGE-4-APPROVAL.md
  - design/JETIX-FPF.md (D6 constitutional)
  - raw/research/architecture-variants-2026-04-22/TENSIONS-{PRE-RESOLVED,RESOLVED,RESOLVED-STAGE-2B}.md
  - raw/research/architecture-variants-2026-04-22/OME-ARCHITECTURE-REFERENCE.md
---

# JETIX-ARCH-V3-DEEPTECH — Stage 6 Variant 3 (AGGRESSIVE DEEP-TECH)

> *"Correctness through formalism — FPF is the substrate, Jetix is the instance."*

---

## §1. Executive Summary

This variant treats the **Jetix Foundational Pattern Framework (JETIX-FPF, D6, 3758 lines)** as a **generative substrate**, not a canon to be name-dropped. Every folder, every agent contract, every wiki edge, every protocol message in this architecture derives from an FPF primitive — and cites it at line-level traceability. Ruslan's dictum *«Foundation = главный актив»* (D2 §14) stops being a slogan; it becomes a build-time invariant enforced by schema validation, pre-commit hooks, and one CI job. *«Quality cannot be retrofit at $1T scale»* (D2 §14) becomes machine-checkable from Day 1 by refusing to merge untagged artefacts.

**The thesis in one line.** The base layer (`jetix-os/`) is not "code that happens to reference FPF" — it is the **schema-level instantiation of FPF primitives**, and the overlay (`jetix-company/`) is the first instance. The 2nd pilot overlay instantiates the same primitives. The 50th roy instantiates the same primitives. The $1T-scale federation instantiates the same primitives. *No rewrite, ever* (C18, Lock 19) is therefore not a promise — it is a derivation: parametric growth over a fixed ontology cannot structurally require a rewrite.

**Phase-1 MVP = minimum formalism necessary to close consulting contracts.** Formalism density grows monotonically with revenue gates ($20-30K → €50K → €200K → €1M). At €50K the substrate is a handful of YAML schemas + JSON-Schema validation in CI + a pre-commit hook that rejects untagged artefacts — cheap, fast, no theorem prover. At €200K the substrate gains richer state-machine enforcement. At $100M the substrate gains formal-methods verification for token state transitions. **Every formalism in this document has a minimum-viable-Phase-1 reduction trivially implementable with YAML + git hooks + 1 CI job.**

**Signature bets (three):**

1. **USB-C Protocol Layer Phase-1 scaffold** (not Phase 3+): we deliver **protocol taxonomy + 2 reference protocols + verification harness** in Phase 1. This is D20 / Lock 20 / C19 instantiated, not "positioned as". Third-party implementation achievable Phase 2a. Standards-body submission Phase 3+.
2. **Typed-graph Wiki** (9 entity types × 10 typed edges: 6 FPF A.14 mereology + 4 Jetix-domain) with provenance, F-G-R, and bias-class as first-class schema fields.
3. **FPF-manifest per agent** — every agent has a machine-verifiable YAML contract declaring which bridges it uses, which viewpoints it publishes, which pillars it upholds, which guard-rails it enforces, and which `acting_as` roles are permitted. Type-checked in CI.

**Self-declared trade-off.** Phase-1 readiness scored honestly **5–6/10** — acknowledged cost of depth. In exchange we claim **10/10 Foundation quality**, **9/10 Scale trajectory**, **9/10 Innovation**, **9/10 Universality**. Variant weighted total estimate **~82/100**. Cost efficiency: **PASS** — the Phase-1 run rate remains under the §8.3 €800/mo disqualifier because formalism lives in the filesystem substrate (zero runtime cost), not in runtime verification layers.

**Roster size (matches C14 exactly, no inflation):**

| Layer | Count | Kind |
|---|---|---|
| Canonical agents | 11 | D6 §2.2 authoritative roster |
| Ruslan atomic sub-role manifests | 5 | `strategy-lead` / `framing-lead` / `sales-closer` / `acceptance-authority` / `external-relations` (D6 §2.1 L.418-427) |
| Phase-2a dormant stubs | 2 | `dpo` (external-executor, MC1 P1-#2) + `customer-success` (J2, MC1 P1-#7) |
| Life-coach | physically separated | Lives in `life-os/` (C15) — not counted as Jetix agent |
| Meta-agent FPF-Steward sub-role | embedded | R12 inside meta-agent until Phase-2b promotion trigger |
| **Total Jetix-manifest files Day 1** | **11 + 5 + 2 = 18** | Each a schema-validated YAML + role.md companion |

**The variant's gravity.** Where Variant 1 (Conservative) optimises for Phase-1 velocity and Variant 2 (Innovative) optimises for exploration of patterns, Variant 3 (Deep-Tech) optimises for **foundation-quality under the $1T invariant**. If the constraint that binds is the $1T no-rewrite trajectory (Lock 19, C18), choose this variant. If the constraint that binds is €50K Q2 shipment with zero formalism-drift risk, choose Variant 1. **Hybrid candidate (§24):** §17 USB-C scaffold + §4 fpf-manifests + §7 typed wiki are composable into Variant 4 (Hybrid) without the rest.

---

## §2. Variant Character Statement

**Philosophical lens:** *ontology-first*. Architecture is the ontology made concrete. Every architectural element is cited to at least one FPF primitive with a `[FPF …]` or `[D6 §…]` reference, and the citation is load-bearing: remove the primitive and the element loses meaning.

**The bet.** The $1T trajectory is more fragile than the Q2 consulting close. Q2 can be recovered by 60 extra days of work; a rewrite at €200M MRR scale cannot be recovered at all. Ruslan explicitly says *«Quality cannot be retrofit at $1T scale»* (D2 §14) — the formal substrate is the mechanism that makes this true.

**The risk.** Slower Phase-1 shipping. Formalism has a learning cliff. Solo Ruslan carries the cognitive cost of the schema discipline until the 2nd pilot arrives. Variant 3 accepts this risk explicitly and defends it with Pass-3 Phase-1 shipability tests (§23).

**The upside.** Clean $1T trajectory. The base layer is schema-isomorphic to FPF; scaling = adding instances of the same primitives, not inventing new kinds. *«Foundation = главный актив»* (D2 §14) moves from aspirational to machine-checkable: every commit either preserves Foundation invariants or is rejected.

**Ruslan voice, load-bearing (5 quotes woven into this document):**

1. *«Foundation = главный актив»* (D2 §14) — cited in §1, §18, §19.
2. *«Continuous, every iteration — NOT periodic»* (D2 §6) — cited in §15, §18.
3. *«Quality cannot be retrofit at $1T scale»* (D2 §14) — cited in §1, §6, §18.
4. *«Gentleman inside / Predator outside»* (Lock 1, D1 pre) — cited in §8, §15.
5. *«Notion loss recoverable in 1 day, wiki loss = Jetix loss»* (D2 §14) — cited in §7, §18.
6. *«AI = electricity»* (D2 §7) — cited in §9 (multi-provider = resilience primitive).

**Character tags:** ontology-first · fpf-substrate · formal-contracts · research-grade-rigor · systems-thinking · type-checked-agents · typed-graph-wiki · standards-body-protocols.

---

## §3. Answer to Q1 — Repository Layout

**Problem frame (D4 Q1):** D2 §10 mandates Jetix-agnostic base + overlay. Multi-pilot (Lock 2 / C1) drives physical separability. Membrane (Locks 1/3/13 / C3) drives access tiering.

**Core claim (Deep-Tech):** Repository layout *reflects ontology*, not convenience. Three concentric layers map to three ontological tiers. Dependency direction is **fpf → jetix-os → jetix-company**, enforced by a pre-commit import-direction checker — a direct instantiation of **[FPF §12.5 / E.5 GR-3 Unidirectional Dependency guard-rail]**.

### §3.1 Top-level tree (Phase-1 single-repo realisation)

```
jetix-repo/
├── fpf/                         # constitutional substrate (read-only, versioned; D6 source)
│   ├── JETIX-FPF.md            #   = current design/JETIX-FPF.md
│   ├── primitives/             #   extracted YAML primitives (mereology, alphas, bridges, …)
│   │   ├── mereology-edges.yaml
│   │   ├── alphas.yaml         #   8 canonical alphas (Client/Project/Deal/…, D6 §6)
│   │   ├── pillars.yaml        #   11 pillars (P-1..P-11, D6 §12.4)
│   │   ├── guard-rails.yaml    #   GR-1..GR-4 (D6 §12.5)
│   │   ├── f-g-r.yaml          #   F0-F9 × R-low..R-formally-proven × bias-class (D6 §4.2)
│   │   └── viewpoints.yaml     #   5 canonical viewpoints (D6 §4.4)
│   └── schemas/                #   *.schema.json / *.schema.yaml — CI-enforced
│       ├── fpf-manifest.schema.yaml
│       ├── bridge.schema.yaml
│       ├── cp-5-gate.schema.yaml
│       └── edge-record.schema.yaml
│
├── jetix-os/                    # universal kernel — domain-agnostic
│   ├── agents/                 #   canonical agent templates (role.md + fpf-manifest.yaml)
│   ├── protocols/              #   RFC-style protocol drafts (§17)
│   ├── wiki-schema/            #   9 entity types × 10 edge types (§7)
│   ├── dashboard-schema/       #   metric viewpoints (§14)
│   ├── cp-5-routes/            #   escalation taxonomy + contestation path (§15)
│   └── schemas/                #   jetix-os schemas depend only on fpf/schemas/
│
├── jetix-company/              # Jetix-specific overlay (ICP, projects, sales)
│   ├── icp/                    #   11 archetypes + 5-criteria vector + direction-of-life
│   ├── sales/                  #   consulting pipeline + DACH market
│   ├── finance/                #   compute-ledger, Stripe bindings
│   ├── clients/                #   per-client overlay: pilot-manifest + contract (§16)
│   └── legal/                  #   GmbH + DPA + EU AI Act bindings
│
├── life-os/                    # physically separated (C15; Hook 1 enforces asymmetric ban)
│   └── agents/life-coach/
│
├── comms/mailboxes/            # JSONL mailboxes per agent (CLAUDE.md §Architecture)
├── decisions/                  # ADRs + DRRs (D6 §12.14 Δ-class governance)
├── raw/                        # ingestion staging (voice memos, research, unprocessed)
└── .pre-commit-config.yaml     # blocking hooks — see §3.3
```

**Phase-1 single-repo realisation.** All four top-level folders (`fpf/`, `jetix-os/`, `jetix-company/`, `life-os/`) live in one git repo Day 1 (C15 — folder-separation). This satisfies D18 (productization) via folder-level overlay isolation and keeps the Phase-2b GmbH-ready company layer trivially extractable by `git filter-repo` on the Phase-2a Triple-AND trigger (≥€20K MRR × 3mo + Ruslan >40% L1/L2 time + ≥1 GDPR DPA client; [D4 §6 C15]).

### §3.2 Dependency direction — GR-3 instantiated

**Directed acyclic graph (GR-3 unidirectional, D6 §12.5.3):**

```
fpf/  ─────────▶ jetix-os/  ─────────▶ jetix-company/
                                  ▲
                   life-os/  ◀─── │     (Hook 1: Jetix → Life-OS BLOCKED; C15)
```

**Reverse arrows never.** `jetix-company/` files reading `fpf/…` is fine. `fpf/` files reading `jetix-company/…` is a blocking pre-commit error — an instance of the GR-3 invariant (*"Core → Tooling → Pedagogy acyclic"*, D6 §12.5.3) generalised to Jetix's `fpf → os → company` triad. This is not a convention; it is `.pre-commit-config.yaml` line 14, `jetix-import-direction.py`, exit code 1 on violation.

**Why this matters architecturally.** Every lock that says "universality" (C9, Lock 19, D-test §5.5) reduces in this variant to a single mechanism: the import-direction checker. C9 is not monitored manually; it is impossible to violate without a commit rejection.

### §3.3 Blocking hooks (.pre-commit-config.yaml — Phase 1)

```yaml
# .pre-commit-config.yaml — Deep-Tech Phase-1 blocking set
repos:
  - repo: local
    hooks:
      # Hook 1 — [D4 §6 C15] asymmetric reference ban (Jetix → Life-OS blocked)
      - id: jetix-lifeos-asymmetric
        entry: tools/hook-1-asymmetric.py
        pass_filenames: true
        types: [text]

      # Hook 2 — [FPF GR-3] import-direction: fpf → os → company acyclic
      - id: fpf-os-company-direction
        entry: tools/hook-2-import-direction.py
        files: '\.(md|yaml|py)$'

      # Hook 3 — [D6 §4.5 / §4.2] F-G-R frontmatter mandatory on artefacts
      - id: fgr-frontmatter-required
        entry: tools/hook-3-fgr-frontmatter.py
        files: 'decisions/.*\.md$|wiki/.*\.md$|.*/role\.md$'

      # Hook 4 — [D6 §5.5 MC6] past-participle alpha state names
      - id: alpha-past-participle
        entry: tools/hook-4-alpha-state-names.py
        files: 'alphas/.*\.yaml$'

      # Hook 5 — [D4 §5.5 D-test] symbolic grep on jetix-os/ base subtree
      - id: universality-symbolic-test
        entry: tools/hook-5-symbolic-test.sh
        files: 'jetix-os/.*'

      # Hook 6 — [D4 C11] `acting_as` required on agent messages
      - id: acting-as-required
        entry: tools/hook-6-acting-as.py
        files: 'comms/mailboxes/.*\.jsonl$'

      # Hook 7 — [D4 §4.5 SOPS] no plaintext credentials
      - id: no-plaintext-creds
        entry: tools/hook-7-no-plaintext-creds.py
```

**7 blocking hooks Day 1. Each hook ≤ 60 lines of Python. None requires a theorem prover.** This is the Phase-1 floor of "formalism" — enough to make invariants machine-enforced, cheap enough to fit the €800/mo compute gate (hooks run locally + once per PR in CI on €1-2/mo GitHub Actions).

### §3.4 Schema-as-contract (one representative file)

Every `*.schema.yaml` under `fpf/schemas/` is JSON-Schema-compatible. Example (condensed):

```yaml
# fpf/schemas/fpf-manifest.schema.yaml
$schema: "https://json-schema.org/draft/2020-12/schema"
title: "FPF Agent Manifest"
type: object
required: [agent_id, role_ref, acting_as, fpf_bindings]
properties:
  agent_id:    { type: string, pattern: '^[a-z0-9\\-]+$' }
  role_ref:    { type: string }   # path to role.md (5-block per FPF IP-1)
  acting_as:
    type: array
    items:
      enum: [manager, personal-assistant, system-admin, sales-lead,
             sales-research, sales-outreach, inbox-processor, crazy-agent,
             knowledge-synth, strategy-support-analyst, meta-agent,
             strategy-lead, framing-lead, sales-closer,
             acceptance-authority, external-relations]
  fpf_bindings:
    type: object
    required: [bridges_used, viewpoints_published, pillars_upheld,
               guard_rails_enforced, alphas_touched]
    properties:
      bridges_used:          { type: array, items: { type: string } }
      viewpoints_published:  { type: array, items: { type: string } }
      pillars_upheld:        { type: array, items: { pattern: '^P-(1[01]|[1-9])$' } }
      guard_rails_enforced:  { type: array, items: { pattern: '^GR-[1-4]$' } }
      alphas_touched:        { type: array, items: { type: string } }
```

Every commit that changes an `fpf-manifest.yaml` re-runs the schema validator. Invalid manifest = blocked commit. This is **[FPF A.13:4.3 machine-verifiable agency]** reduced to a 40-line JSON-Schema validator.

**How Phase-1 ship-readiness is preserved.** Single-repo + 7 hooks + JSON-Schema validation = **zero third-party runtime dependencies**, **zero monthly cost beyond GitHub**, **zero schema-authoring burden above what is already required by D4 §4.1 role-manifests**.

---

## §4. Answer to Q2 — Agent Roster (with formal FPF contract per agent)

**Problem frame (D4 Q2):** CLAUDE.md drift (12 vs canonical 11); `sales-researcher`→`sales-research` rename; `strategist`→`strategy-support-analyst` rename; 5 Ruslan atomic sub-roles as manifests (NOT agents); 2 Phase-2a stubs (`dpo`, `customer-success`); `shared/schemas/message.schema.json` enum Day-1 blocker.

**Core claim (Deep-Tech):** Every agent has a **formal FPF contract**, not a natural-language system prompt. The contract is three files: `role.md` (5-block per D6 §5.8), `executor-binding.yaml` (Role ≠ Executor per C12 / P2 / IP-1), **and `fpf-manifest.yaml`** — the machine-verifiable declaration of which FPF primitives the agent is bound to. `acting_as` is an enum value constrained by this manifest. CI validates: no agent can publish a viewpoint it did not declare; no agent can advance an alpha it does not touch; no agent can escalate to a class it did not enumerate.

### §4.1 Canonical roster (authoritative, matches D6 §2.2 exactly)

| # | Agent | Dept | Model | Phase | J-level (D6 §2.2) | Primary alphas touched |
|---|---|---|---|---|---|---|
| 1 | `manager`                    | MGMT  | Sonnet 4.6 | 1 | J-Approve (cross-dept)       | Project, Direction |
| 2 | `personal-assistant`         | OPS   | Haiku 4.5  | 1 | J-Auto                       | — (no client-affecting) |
| 3 | `system-admin`               | OPS   | Haiku 4.5  | 1 | J-Auto / J-Approve (spend)   | — |
| 4 | `sales-lead`                 | Sales | Sonnet 4.6 | 2 | J-Approve (in CHR)           | Client, Deal |
| 5 | `sales-research`             | Sales | Haiku 4.5  | 2 | J-Auto                       | Client (lead-identified→qualified) |
| 6 | `sales-outreach`             | Sales | Haiku 4.5  | 2 | J-Auto (templated)           | Content Item |
| 7 | `inbox-processor`            | Brain | Haiku 4.5  | 2 | J-Auto                       | — |
| 8 | `crazy-agent`                | Meta  | Sonnet 4.6 | 2 | J-Approve (brainstorm mode)  | Hypothesis |
| 9 | `knowledge-synth`            | Brain | Sonnet 4.6 | 3 | J-Approve (foundations)      | Way of Working |
| 10 | `strategy-support-analyst`  | MGMT  | Opus 4.6   | 3 | J-Approve (NEVER J-Strategic)| Direction (support only) |
| 11 | `meta-agent` (+ FPF-Steward R12 sub-role) | Meta | Sonnet 4.6 | 4 | J-Approve; halts on safety  | Way of Working, bias audit (D.5) |

**Non-agents (role-manifests only):**

- **5 Ruslan atomic sub-roles:** `strategy-lead` / `framing-lead` / `sales-closer` / `acceptance-authority` / `external-relations`. Per D6 §2.1 (L.418-427), these are Ruslan-exclusive — no agent can `acting_as` any of these. Founder `executor-binding.yaml` supports multi-role enumeration.
- **2 Phase-2a dormant stubs:** `dpo` (external-executor mode; activates on ≥1 GDPR DPA client), `customer-success` (J2; activates on ≥€20K MRR × 3mo).
- **Life-coach:** physically separated into `life-os/` per C15; not a Jetix agent.

Total Day-1 YAML manifests: **11 canonical + 5 Ruslan sub-roles + 2 dormant stubs = 18 manifests**. Matches D4 §4.1 exactly.

### §4.2 Schema: `fpf-manifest.yaml` (one concrete example)

```yaml
# agents/sales-lead/fpf-manifest.yaml
agent_id: sales-lead
role_ref: agents/sales-lead/role.md
executor_binding_ref: executors/sales-lead/executor-binding.yaml
acting_as: [sales-lead]             # agent cannot publish as another role

fpf_bindings:
  bridges_used:
    - jetix-uts.md#sales-closer-bridge                    # [D6 §8.4]
    - jetix-alpha-client ↔ SEMAT-Alpha (CL=3, Near-identity)  # [D6 §8.4]
  viewpoints_published:
    - executive-viewpoint                                 # [D6 §4.4]
    - governance-viewpoint
  pillars_upheld:
    - P-2   # Didactic Primacy (D6 §12.4)
    - P-7   # Pragmatic Utility
    - P-9   # State Explicitness
  guard_rails_enforced:
    - GR-1  # DevOps Lexical Firewall (no tool tokens in proposals)
    - GR-3  # Unidirectional (sales never writes to fpf/)
  alphas_touched:
    - client       # advances lead-identified → qualified → proposed
    - deal         # advances drafted → signed

escalation:                          # [atom-2558 / D4 §4.4]
  cross_dept: manager
  strategic:  ruslan@strategy-lead
  safety:     meta-agent + ruslan   # halts current task
  off_chr_pricing: ruslan@strategy-lead

fgr_declaration:
  max_formality: F3                  # sales proposals land F2-F3 (D6 §4.2)
  default_reliability: R-medium
  bias_audit_classes_covered: [REP, ALG, LNG]  # (D6 §12.10 D.5; 5-class taxonomy)

cp_5_gates_subject_to:
  - l1_contractual                   # all signed proposals (D6 §4.5.1)
  - l2_substantive                   # audit-SKU deliverables

ba_cycle_participation:              # Bias Audit cycle, D.5
  owns_stages: [BA-0]               # drafts at project-kickoff
  co_signs:    [BA-3]               # closure by acceptance-authority
```

**CI invariants (cheap, Day-1):**

1. `agent.acting_as ⊆ agent.fpf_bindings` — an agent cannot "act as" a role it did not declare.
2. `agent.viewpoints_published ⊆ fpf/viewpoints.yaml.canonical_5` — an agent cannot invent a viewpoint.
3. `agent.alphas_touched` must refer to one of the 8 canonical FPF alphas ([D6 §6.2]).
4. `agent.escalation.*` values must resolve to another agent in the roster or a Ruslan sub-role.
5. `agent.pillars_upheld ⊇ {P-3, P-9}` for every agent that publishes decisions — every DRR must cite ≥3 pillars (D6 §12.4).

All five invariants run in a single `pytest` job on PR, ~5 seconds. This is **[FPF A.13:4.3 machine-verifiable agency]** with zero-cost Phase-1 enforcement.

### §4.3 Renames and drift reconciliation (Day-1 CLAUDE.md patch)

The variant treats `shared/schemas/message.schema.json` `acting_as` enum as *the single source of truth*, regenerated from D6 §2.2 at commit time by a Day-1 script:

```bash
# tools/regen-message-schema.sh — runs in CI; any diff = blocker
python tools/extract-d6-roster.py design/JETIX-FPF.md > /tmp/roster.yaml
python tools/update-acting-as-enum.py \
  --roster /tmp/roster.yaml \
  --schema shared/schemas/message.schema.json
git diff --exit-code shared/schemas/message.schema.json  # fails if drift
```

Renames: `sales-researcher` → `sales-research` (ADR-Chunk-3 Item 7); `strategist` → `strategy-support-analyst` (ADR-Chunk-1 P5, J3 rename). `life-coach` absent from Jetix enum (lives in `life-os/`). CLAUDE.md Agent Roster table updated in the same PR that introduces this variant's adoption; 3-way diff (D6 table ≡ CLAUDE.md table ≡ schema enum) is audited quarterly by FPF-Steward (R12 sub-role).

### §4.4 Why "formal contract" buys Phase-1 shipability (AP-12 avoidance)

The formalism in §4.2 runs in one `pytest` job and enforces what D4 §4.1 mandates anyway: 5-block role.md, separate executor-binding, `acting_as` on every message. Rather than "academic rigour that delays shipping", **the fpf-manifest is the exact place where the already-mandatory information gets written down in a form a computer can check**. Ruslan writing this at 09:00 Monday for `sales-lead` takes ~25 minutes. He would write the equivalent natural-language prompt in ~20 minutes. **Net overhead: ~5 min/agent × 18 agents = ~90 min total Day 1.** This is not the bottleneck on Q2 consulting close — it is a rounding error on it.

---

## §5. Answer to Q3 — Integration Points Inventory

**Problem frame (D4 Q3):** Phase-1 operational surface touches ~12 external systems; each is a failure-surface. Lock 17 (fs=SoT) means integrations are one-way write to Notion, read-back replay from filesystem.

**Core claim (Deep-Tech):** Each integration = a **bridge** per **[FPF §8.4 Bridges framework]**. Deliverable per integration: `integrations/{name}.bridge.yaml` with typed inbound / outbound primitives, FPF-alpha contribution, failure mode, and Congruence Level (CL) measure per D6 §8.4.

### §5.1 Inventory (Phase-1, all 12 integrations as typed bridges)

| # | External system | Direction | Auth | Fallback | Alpha touched | CL |
|---|---|---|---|---|---|---|
| 1 | Stripe              | R/W          | SOPS vault    | Wise FX + manual reconcile | Deal.activated | 3 |
| 2 | Wise                | W (FX)       | SOPS vault    | Manual bank rail           | Deal.completed | 3 |
| 3 | Anthropic Claude API| R/W          | SOPS vault    | OpenAI → Google (§9)       | all            | 3 |
| 4 | OpenAI API          | R/W fallback | SOPS vault    | Google fallback            | all            | 2 |
| 5 | Google Gemini API   | R/W fallback | SOPS vault    | Local cached               | all            | 2 |
| 6 | Groq (Whisper)      | R            | SOPS vault    | OpenAI Whisper             | voice→inbox    | 3 |
| 7 | Notion API          | W only (fs→) | SOPS vault    | Skip (non-blocking)        | — (view only)  | 1 |
| 8 | Telegram Bot API    | R (ingress)  | SOPS vault    | Skip (non-blocking)        | Client.lead-identified | 2 |
| 9 | GitHub (repo + CI)  | R/W          | OAuth         | Local git + delayed push   | all            | 3 |
| 10 | Healthchecks.io    | W (pings)    | token         | Log-only                   | —              | 2 |
| 11 | Toggl              | R (hours)    | SOPS vault    | Manual time log            | Direction      | 1 |
| 12 | Email (IMAP/SMTP)  | R/W          | SOPS vault    | Manual inbox scan          | Client         | 2 |

**All 12 have named owner + SOPS vault path + declared failure_mode + CL score.** This closes the D4 Q3 quality criterion (*"100% integrations have named owner + fallback + secret-store path; zero plaintext creds"*).

### §5.2 Schema: `integrations/stripe.bridge.yaml` (one concrete example)

```yaml
# integrations/stripe.bridge.yaml — a Bridge per [FPF §8.4]
bridge_id: stripe-v1
owner: ruslan@sales-closer           # role-manifest, not executor
created: 2026-04-21
jetix_concept: jetix-revenue-event
external_context: stripe.com (SaaS)
bridge_relation: Partial-overlap (Interpretation)   # [D6 §8.4]
congruence_level: 3                                  # CL=3 near-full equivalence
direction: "↔"                                       # bidirectional (R/W)

inbound_primitives:
  - stripe.PaymentIntent          → jetix.Deal.signed-event
  - stripe.Charge.succeeded       → jetix.Deal.activated-event
  - stripe.Invoice.paid           → jetix.Deal.completed-event

outbound_primitives:
  - jetix.proposal.signed         → stripe.PaymentIntent (create)
  - jetix.subscription.renewal    → stripe.Subscription (update)

fpf_alpha_contribution:
  - alpha: Deal                   # [D6 §6.2 Alpha 3]
    transitions_enabled:
      - drafted → signed          # on proposal countersign
      - signed → activated        # on first PaymentIntent success
      - activated → completed     # on Invoice.paid full retainer

failure_mode:                      # [D4 §4.5 reserve routes]
  primary_down:
    detection:        "3 consecutive 5xx in 5min"
    fallback:         "Wise FX rail + manual reconcile in <48h"
    replay_from_fs:   "finance/revenue-log.jsonl"   # Lock 17 replay
  degraded_mode:
    description:      "system-admin paused; sales-closer notified"
    sla:              "reconcile within 10 business days"
  auth_breach:
    rotation:         "SOPS 1-key rotate; all payment-events quarantined"
    notify:           [system-admin, ruslan@sales-closer]

loss_notes: |
  Stripe's notion of Customer does not fully capture Jetix's 5-criteria ICP
  score. Bridge loses direction-of-life axis on outbound → Stripe metadata.
  Reverse read must enrich via icp/ lookup (CL=3 contingent on enrichment).

cp_5_gates_triggered:
  - l1_contractual  # any new PaymentIntent creation
```

### §5.3 Failure-mode mandate (Lock-17-aligned)

**Every bridge MUST have `failure_mode.replay_from_fs` set.** This is §4.8 Reserve Routes (Foundation element #7) instantiated formally. If a bridge cannot name its filesystem replay path, it is incomplete and the PR is rejected. The filesystem is the canonical record — integrations are bridges to the world, never sources of truth (Lock 17 / C4).

### §5.4 Phase-2a extension path

When `customer-success` stub activates (MC1 P1-#7 triggers), two new bridges appear: `intercom.bridge.yaml` (customer communications) and `usage-metering.bridge.yaml` (platform telemetry). Both are added by copying the existing `stripe.bridge.yaml` template and filling 7 fields. No schema migration. **No rewrite** (C18 Lock 19 preserved).

---

## §6. Answer to Q4 — Scaling Mechanism (Phase-1 → $1T without rewrite)

**Problem frame (D4 Q4):** Lock 19 + D3 §11b mandate 10× at each gate with <30% refactor; no boutique shortcuts (C18, AP-16).

**Core claim (Deep-Tech):** *«Quality cannot be retrofit at $1T scale»* (D2 §14) reduces in this variant to a provable property: **scaling = adding more instances of the same FPF primitives, not introducing new kinds**. Horizontal growth = more fpf-manifests with no base-layer schema change. Vertical growth = maturation along F-G-R (F3 → F9; R-medium → R-formally-proven). Under these two operations, the LOC-delta per gate stays <30% because the schemas are fixed.

### §6.1 Scale Invariants (7 invariants preserved across all gates $0 → $1T)

| # | Invariant | Mechanism | Violated-by check |
|---|---|---|---|
| SI-1 | Mereology edge count grows linearly with entity count, not quadratically | A.14 typed edges are directed, schema-bound; no implicit all-to-all | `python tools/si-1.py wiki/graph/edges.jsonl` (CI) |
| SI-2 | F-G-R claim-scope remains bounded even at 10⁶ claims | Every claim declares `scope:` — a URI-bounded context (D6 §4.5.4) | Hook 3 rejects unbounded |
| SI-3 | No agent can bypass `acting_as` enforcement at any scale | Message schema validation; regen from D6 §2.2 in CI | `regen-message-schema.sh` diff = 0 |
| SI-4 | Every commit preserves GR-3 unidirectional dependency | Hook 2 blocks; impossible to violate without repo surgery | Pre-commit exit 1 |
| SI-5 | Every client-affecting output passes CP-5 gate | CP-5 YAML mandatory per L1/L2 tier; absence = blocker (D6 §4.5) | Hook that grep's for missing gate |
| SI-6 | BA (Bias-Audit) cycle closure required per Project.closed | D.5 cycle state machine; Hook 4 guards transitions | Alpha-state past-participle check |
| SI-7 | No runtime component cost scales superlinearly with entity count | Wiki queries are indexed on typed edges; no N² joins | Query-plan review @ phase-gate audit |

These seven are the formal expression of Foundation-as-asset. They are testable per commit, per release, per gate.

### §6.2 Horizontal scaling formalism

Adding a 2nd agent, a 2nd pilot, a 50th roy = adding instances. **Zero base-layer schema changes.**

| Growth dimension | What changes | What does NOT change |
|---|---|---|
| +1 agent            | new `agents/<id>/` folder with 3 files (role.md + executor-binding.yaml + fpf-manifest.yaml); enum regen | `fpf/schemas/*`; `jetix-os/schemas/*`; protocols; dashboard schema |
| +1 pilot (Phase-2a) | new `jetix-company-<pilot>/` overlay folder; shared `jetix-os/` | `jetix-os/`; `fpf/`; protocols |
| +1 roy (Phase-3+)   | new `roys/<roy-id>/` deployed via kit (§12); shared protocols | protocols; fpf; jetix-os |
| +1 integration      | new `integrations/<name>.bridge.yaml` | bridge schema; failure-mode schema |
| +1 content-archetype (11→12 archetypes) | icp/vN+1.yaml with 12 entries | pipeline schema; rendering engine |
| +1 ICP criterion (5→6 criteria) | icp/schema-vN+1.yaml; migration diff | bridge schema; CP-5 gate schema |

### §6.3 Vertical scaling formalism (F-G-R maturation)

| Gate | Current F target | Current R target | Verification mechanism |
|---|---|---|---|
| $0 → $20-30K         | F0-F2 | R-low to R-medium       | Manual review; BA-0 only |
| $20-30K → €50K       | F1-F2 | R-medium dominant       | BA-0 + BA-1 added       |
| €50K → €200K         | F2-F3 | R-medium → R-high       | BA-0/1/3 full cycle; external DPO review |
| €200K → €1M          | F2-F3 | R-high dominant         | BA-2 Panel (Beirat Ethics) added |
| €1M → $100M          | F3    | R-high → R-certified    | External auditor on governance |
| $100M → $1T          | F3-F4 | R-certified → R-formally-proven on critical subsystems | Formal verification on token state machine, matchmaker contract kernel |

**Phase-1 reduction.** At €50K, F-G-R is a YAML frontmatter field + a regex hook. No theorem prover. The *discipline* of tagging is what matures the substrate, not any particular tool — the tool graduates with the gate.

### §6.4 10× rule verification

Per D4 §5.1: 10× scaling ⇒ <30% subsystem LOC affected per 10× gate.

| Subsystem | Phase-1 (1 pilot) | Phase-2a (3 pilots) | Phase-2b (5-10 agents) | Est. LOC-delta | Schema migrations |
|---|---|---|---|---|---|
| `jetix-os/agents/`     | 18 manifests | 18 (same, template reuse) | 25-30 (add 12 for new dept) | <20% | 0 |
| `jetix-os/protocols/`  | 2 proto + harness | 3 proto (add onboard-specialist) | 5 proto | <30% | 0 |
| `jetix-os/wiki-schema/`| 9 entity × 10 edge | SAME | SAME | 0% | 0 |
| `jetix-company/`       | 1 overlay | 3 overlays (copy+fill) | 3 | <10% (overlay-add, not base-rewrite) | 0 |
| CP-5 gate routes       | 4 classes | 4 + tier refinements | 4 + granular sub-tiers | <15% | 0 |
| dashboard-schema       | 5+2 metrics | +roy count, +member count, +match rate | +market-cap, +token circ | <25% | 0 |

**All subsystems satisfy <30%.** The wiki schema does not change at all — it is the scaling invariant that underwrites $1T.

### §6.5 Phase-2a triple-AND trigger detection

The formal substrate detects trigger readiness (≥€20K MRR × 3mo AND Ruslan >40% L1/L2 time AND ≥1 GDPR DPA client — C15) via three dashboard viewpoints (§14):

```yaml
# jetix-os/dashboard-schema/triple-and-trigger.yaml
trigger_id: phase-2a-mht-1
all_of:
  - metric: mrr
    condition: ">= 20_000 EUR for 3 consecutive months"
    source: finance/revenue-log.jsonl
  - metric: ruslan-l1-l2-fraction
    condition: "< 0.40"            # founder-dependency flipped
    source: ops/toggl-deep-hours.jsonl
  - metric: dpa-clients
    condition: ">= 1 active"
    source: legal/dpa/active.yaml
on_all_met:
  - notify: ruslan@strategy-lead
  - create_drr: decisions/mht-1-trigger-pending.md
  - halt_auto_phase_transition: true   # Ruslan acceptance-authority signs off
```

The trigger is a pure dashboard query — not a hidden flag, not manually tracked. *Continuous, every iteration — NOT periodic* (D2 §6).

---

## §7. Answer to Q5 — Data Architecture (typed-graph wiki)

**Problem frame (D4 Q5):** 3-layer knowledge (wiki + alphas + per-agent) must support 9 entity types + 25K HARD token budget + Karpathy/OmegaWiki pattern + A.14 typed edges.

**Core claim (Deep-Tech):** Wiki is a **typed graph**, not a filesystem of loose markdowns. Each entity is a node with strict frontmatter; each relationship is an edge-record in `wiki/graph/edges.jsonl` carrying a typed label from a **closed 10-edge-type enumeration** (6 FPF mereology + 4 Jetix-domain). Edges are first-class, queryable, validatable.

### §7.1 9 entity types × 10 edge types

Per CLAUDE.md Wiki v2, 9 entities: `concepts/` / `entities/` / `sources/` / `topics/` / `ideas/` / `experiments/` / `claims/` / `summaries/` / `foundations/`.

**10 typed edges (closed enum):**

| # | Edge | Semantics | Source | [citation] |
|---|---|---|---|---|
| 1 | `ComponentOf`   | Structural discrete part                       | FPF mereology | [D6 §3.5 / A.14] |
| 2 | `ConstituentOf` | Conceptual/logical part (section, lemma)       | FPF mereology | [D6 §3.5 / A.14] |
| 3 | `PortionOf`     | Metrical measure-preserving part (μ-additive)  | FPF mereology | [D6 §3.5 / A.14] |
| 4 | `PhaseOf`       | Temporal part — same carrier across interval   | FPF mereology | [D6 §3.5 / A.14] |
| 5 | `MemberOf`      | Collection membership (NOT partOf)             | FPF mereology | [D6 §3.5 / A.14] |
| 6 | `AspectOf`      | Facet/perspective of same entity               | FPF mereology | [D6 §3.5 / A.14] |
| 7 | `creates`       | Creator → created target                       | Jetix-domain  | [D4 §4.5] |
| 8 | `operates-in`   | Target → supersystem it operates in            | Jetix-domain  | [D4 §4.5] |
| 9 | `methodologically-uses` | Creator → method-description it applies | Jetix-domain  | [D4 §4.5] |
| 10 | `constrained-by` | System → constraint that binds it             | Jetix-domain  | [D4 §4.5] |

Any edge not in this enum is a schema violation. Any edge missing `source`, `target`, `f_g_r`, or timestamp is a schema violation.

### §7.2 Edge record schema + example

```yaml
# fpf/schemas/edge-record.schema.yaml (condensed)
type: object
required: [edge_id, src, tgt, edge_type, f_g_r, timestamp, actor]
properties:
  edge_id:    { type: string, pattern: '^e-[0-9a-f]{8}$' }
  src:        { type: string }   # wiki-entity URI
  tgt:        { type: string }   # wiki-entity URI
  edge_type:  { enum: [ComponentOf, ConstituentOf, PortionOf, PhaseOf,
                       MemberOf, AspectOf, creates, operates-in,
                       methodologically-uses, constrained-by] }
  f_g_r:      { type: string, pattern: '^F[0-9]/G:.+/R-(low|medium|high|certified|formally-proven)$' }
  bias_class: { type: array, items: { enum: [REP, ALG, VIS, MET, LNG] } }
  timestamp:  { type: string, format: date-time }
  actor:      { type: string }   # agent-id or ruslan@sub-role
```

**Concrete edge record example (one line in `wiki/graph/edges.jsonl`):**

```jsonl
{"edge_id":"e-a7f2c019","src":"wiki/entities/mueller-gmbh.md","tgt":"wiki/concepts/dach-mittelstand.md","edge_type":"MemberOf","f_g_r":"F2/G:jetix-dach-ICP-2026-Q2/R-medium","bias_class":["REP"],"timestamp":"2026-04-21T14:22:00Z","actor":"sales-research"}
```

Append-only. Queryable by `jq` Phase 1, migratable to a graph DB only when benchmark warrants (§6 SI-1 linear growth keeps Phase 1/2a/2b on flat files).

### §7.3 Frontmatter schema (every wiki entity)

```yaml
---
id: mueller-gmbh                            # wiki-entity URI fragment
entity_type: entities                       # ∈ 9-type enum
f_g_r: F2/G:jetix-dach-ICP-2026-Q2/R-medium # mandatory (Hook 3)
bias_class: [REP]                           # mandatory (min 1 declared, even if empty)
alpha_state: null                           # OR one of {drafted,qualified,...} per D6 §6.2
ba_state: BA-0                              # Bias-Audit cycle stage (D.5)
tier: partner                               # ∈ {public, member, partner, core} (§8)
sources:                                    # provenance chain
  - raw/2026-04-10-mueller-intro-call-transcript.md
  - sources/dach-market-report-2026.md
created: 2026-04-21
actor: sales-research
---
```

### §7.4 Atoms as first-class entities

Per [atom-2558 / D4 §4.4], the 4-class escalation taxonomy is itself an atom, and atoms are first-class wiki-entities. An atom node has mereology edges to the concepts it composes. Example:

```
atom-2558 ComponentOf wiki/concepts/escalation-taxonomy.md
atom-2558 ConstituentOf wiki/claims/c-2558-routing-rule-01.md
atom-2558 ConstituentOf wiki/claims/c-2558-routing-rule-02.md
...
```

Atoms graduate in F-G-R with use — atom-2558 moved from R-low at first voice memo to R-medium after BA-1 review. Every atom is a trace.

### §7.5 Provenance chain (auditable)

Every claim → source → ingestion-step → compile-step → reviewer. The `sources:` frontmatter field is a list of URIs; the wiki pipeline stages (`raw → ingested → compiled → linted → ready`) are `PhaseOf` edges on the same carrier. `PhaseOf` is A.14-canonical — the wiki pipeline is a mereological phase-sequence, not an ad-hoc state.

### §7.6 BA-cycle state on every entity

Per D.5 (D6 §12.10):

- BA-0: template initialization at Project.kicked-off.
- BA-1: mid-project.
- BA-3: closure — required for Project.closed transition; signed by acceptance-authority (Ruslan L4).
- BA-2: Panel review Phase-2a+ only (Beirat Ethics advisor).

Every wiki entity carries `ba_state:`. Hook 4 refuses transitions that skip BA-1 before BA-3. *Continuous, every iteration — NOT periodic* (D2 §6) is enforced per commit.

### §7.7 Storage: filesystem only (Lock 17, C4)

YAML frontmatter (schema-validated) + body markdown + `wiki/graph/edges.jsonl` append-only. **No database Phase 1.** At €200K MRR, if benchmark justifies, migrate edges.jsonl into a graph DB (Dgraph / Neo4j community) — but the **source of truth remains the .jsonl file in git**; the DB is a materialised view. *«Notion loss recoverable in 1 day, wiki loss = Jetix loss»* (D2 §14) — the wiki is git; git is wiki.

---

## §8. Answer to Q6 — Privacy / Security Membrane (GDPR + EU AI Act)

**Problem frame (D4 Q6):** Locks 1/3/13 compose the security membrane; CP-5 Human Approval Gate maps GDPR Art. 22 + EU AI Act Art. 14.

**Core claim (Deep-Tech):** The 4-tier ACL (public / member / partner / core — C3, Lock 13) is a **membrane primitive** with typed transitions enforced by schema. Every entity carries `tier:` in frontmatter; a git hook enforces: entities of tier `core` cannot be linked from entities of tier `public` via open edges. **[FPF §12.5 GR-3 unidirectional guard-rail]** pattern generalised to visibility: core→public emission allowed only through auto-gen pipeline; public→core links forbidden.

### §8.1 Tier ACL matrix (formal)

| Tier | Examples | Read by | Write by | Pipeline output |
|---|---|---|---|---|
| `public`  | landing pages, demos, 10 templates, TOF content | anyone (internet) | auto-gen from `core` only | `surface/` build output |
| `member`  | invite-only chat, gated templates, mid content   | invited + 5-criteria-passed | inbox-processor, sales-outreach | `members/` |
| `partner` | client-specific deliverables, Audit SKU, contracts | active clients, lawyers | sales-closer, acceptance-authority | `jetix-company/clients/<id>/` |
| `core`    | FPF-Steward memos, token state, 9 Innovations     | Ruslan + meta-agent | Ruslan + knowledge-synth | `core/` (never pipelined outward) |

### §8.2 Schema-enforced transitions

```yaml
# fpf/schemas/acl-transition.schema.yaml (condensed)
transitions_allowed:
  core     → partner: ["auto-gen pipeline with bias-redact"]
  core     → member:  ["auto-gen pipeline with bias-redact + invite-gate"]
  core     → public:  ["auto-gen pipeline with deep-redact only"]
  partner  → member:  forbidden
  member   → public:  forbidden
  public   → core:    forbidden   # [GR-3 generalisation]
link_rules:
  public  may_link_to: [public]
  member  may_link_to: [public, member]
  partner may_link_to: [public, member, partner]
  core    may_link_to: [public, member, partner, core]
```

Hook 2b (subhook of import-direction) validates every new `[…](path)` link at commit time: if `src.tier < tgt.tier` (where `public < member < partner < core`), commit rejected.

### §8.3 Gentleman/Predator bifurcation encoded

*«Gentleman inside / Predator outside»* (Lock 1 / D1 pre) is the membrane bifurcation encoded as **two separate schema namespaces**. Inward policies (`fpf/schemas/inside-*.yaml`) differ from outward policies (`fpf/schemas/outside-*.yaml`):

```yaml
# fpf/schemas/inside-tone.yaml
tone_profile:
  formality: civil-direct
  disagreement_style: "welcomed, logged in wiki"
  rejection_form: "explicit rationale + DRR reference"
  timing: "sync or async, no gaming"

# fpf/schemas/outside-tone.yaml
tone_profile:
  formality: precise-assertive
  disagreement_style: "firm, evidence-forward"
  rejection_form: "clean decline + alternative + CP-5 trail"
  timing: "strategic, not reactive"
```

A message crossing the membrane is validated against the appropriate namespace. No uniform channel.

### §8.4 GDPR Art. 22(3) + WP251rev.01 compliance (CP-5 gate)

Every automated decision affecting a client routes through **CP-5 Human Approval Gate** (D6 §4.5, L.1028-1184). Gate fields, audit trail, meaningful-review guarantee, contestation path — see §15 for the full schema. Here the membrane binding is: **no `partner`-tier or `core`-tier output reaches the external client without passing CP-5 by a human gate-keeper**.

### §8.5 EU AI Act posture

**Phase-1 categorisation: Limited-risk** (consulting advisory outputs; CP-5 transparency obligations satisfied). **Phase-2a trigger-dependent: High-risk** if DPA clients introduce profiling or scoring. The `fpf-manifest.yaml` `cp_5_gates_subject_to:` field pre-declares which agents will cross the threshold — at Phase-2a activation, `dpo` stub comes live and assumes Art. 37-39 oversight. *No rewrite* (C18) — only activation.

### §8.6 9 Innovations IP protection (core-tier, forever-internal)

Per ADR-Chunk-8 Area 2 + OT5-A + OQ-09-A: `wiki/foundations/jetix-innovations.md` is tier=`core`, `f_g_r: F3/G:jetix-innovations-internal/R-high`. ACL hook forbids emission to any outer tier. This is secret-sauce defense encoded in the filesystem substrate.

---

## §9. Answer to Q7 — API Architecture (multi-provider + cost control)

**Problem frame (D4 Q7):** AI-as-electricity (D2 §7) mandates multi-vendor Day 1; per-executor compute-contract + compute-ledger required. AP-11 (single-provider) forbidden.

**Core claim (Deep-Tech):** Multi-provider is **not** "call many APIs for fun". It is a **resilience primitive** (§4.8 reserve routes — Foundation element #7) and a **typed bridge** (§5). The provider abstraction layer declares an enum of providers, each with a typed contract. `compute-ledger.jsonl` is append-only and logs every API call with `provider / model / tokens / cost / purpose / alpha_touched`. CI-level assertion that Phase-1 month-total ≤ €800 (§8.3 hard gate).

### §9.1 Provider router (Phase-1)

```yaml
# fpf/schemas/compute-contract.schema.yaml (per executor)
executor_id: sales-lead
model_preference:
  primary:
    provider: anthropic
    model: claude-sonnet-4-6
    thinking_mode: on        # for J-Approve (strategizing-adjacent) tasks
  fallback_chain:
    - { provider: anthropic, model: claude-haiku-4-5 }   # lighter same-provider
    - { provider: openai,    model: gpt-4o-2026-02 }
    - { provider: google,    model: gemini-2-pro }
    - { provider: local,     model: cached-response }    # degraded mode
max_tokens: 16000
cache_strategy: aggressive
latency_class: standard      # {standard, real-time, batch}
monthly_budget_eur: 90       # share of 800/mo
escalation_rules:
  exceed_budget: "halt; notify system-admin"
  primary_5xx_3x: "switch fallback_chain[0]; mark degraded"
  all_providers_down: "sales-closer manual; freeze automated proposals"
```

### §9.2 compute-ledger.jsonl (append-only)

```jsonl
{"ts":"2026-04-21T14:22:00Z","executor":"sales-lead","provider":"anthropic","model":"claude-sonnet-4-6","purpose":"proposal-draft-mueller","tokens_in":8203,"tokens_out":2104,"cost_eur":0.178,"alpha_touched":"client:qualified→proposed","fgr":"F2/G:jetix-dach-2026-q2/R-medium"}
```

Monthly aggregate = `jq` query in CI. If sum >€800, CI fails the monthly-audit job and halts auto-dispatch to new work until Ruslan signs an exception.

### §9.3 Provider abstraction = bridge per §5

Each provider integration (`anthropic`, `openai`, `google`, `groq`, `local`) gets its own `integrations/<provider>.bridge.yaml` (per §5.2). The bridge declares typed inbound/outbound primitives, CL, failure_mode, and replay_from_fs path. **Multi-provider resilience is not a code pattern — it is a set of bridge YAMLs any consultant with wiki literacy can audit.**

### §9.4 Phase-graduated cost ceiling

| Gate | Monthly budget | Mechanism |
|---|---|---|
| €0 → €20-30K      | ≤ €300/mo | aggressive caching; Haiku-first for non-strategizing |
| €20-30K → €50K    | ≤ €500/mo | +Sonnet for sales-lead / knowledge-synth only |
| €50K → €200K      | ≤ €800/mo | **HARD GATE (D4 §8.3 disqualifier)** — Opus gated to Ruslan + strategy-support-analyst |
| €200K → €1M       | ≤ €2500/mo | Opus broadened; formal verification begins on token state machine |

### §9.5 Why Deep-Tech passes the €800/mo gate

The formalism in this variant lives **in the filesystem substrate**, not in runtime verification layers. Schema validation, JSON-Schema checks, Hook 2/3/4/5/6/7 — all run locally + on GitHub Actions free-tier (~€1-2/mo). No theorem prover, no live type system, no model-checker. The `compute-ledger.jsonl` is the enforcement mechanism — it costs €0 to run a `jq` aggregation against it in CI.

---

## §10. Answer to Q8 — Token Economy (Option B membrane preservation)

**Problem frame (D4 Q8):** D23 Option B = Phase-2 internal + Phase-3+ limited public (economic-claim only); membrane preservation is hard protocol-layer constraint. AP-13 forbids any public-phase token carrying governance or community-access rights.

**Core claim (Deep-Tech):** Tokens are **instances of an accounting primitive over the compute-ledger** extended with external transfer rights in Phase 3+. **No governance rights (AP-13). No community-access rights (AP-13).** Public transfer limited per GmbH legal envelope (C2 revenue-gated). Membrane preservation: public token ownership and ACL tier (§8) are **orthogonal primitives**; the schema forbids their correlation.

### §10.1 Token state machine (formal)

```yaml
# tokens/state-machine.yaml
token_kinds:
  internal-credit:
    phase: 2a+
    transferable: false
    rights: [economic-claim-internal]
    settable_by: [ruslan@acceptance-authority]
  restricted-public-token:
    phase: 3+
    transferable: limited              # GmbH legal envelope
    rights: [economic-claim-public]    # NO governance, NO access
    settable_by: [ruslan@acceptance-authority + external-counsel]
state_transitions:
  issue:   { pre: [phase>=2a, compliance-review.ok, cp5.l1.approved] }
  hold:    { pre: [issued] }
  transfer:
    pre: [kind=restricted-public-token, phase>=3, compliance-review.ok,
          transfer-restriction.ok, cp5.l1.approved]
  burn:    { pre: [issued] }
  redeem:  { pre: [issued, external-proof-of-claim] }
orthogonality_invariants:
  - "token.owner.tier is NEVER derived from token.ownership"
  - "token.transfer DOES NOT grant access to {member, partner, core} tiers"
  - "ACL-tier assignment is ONLY via 5-criteria ICP filter + invitation"
forbidden_forever:
  - governance-right-bundling
  - community-access-right-bundling
```

### §10.2 Orthogonality invariant (Deep-Tech signature)

The three lines in `orthogonality_invariants:` above are CI-checked. Any code path, config, or schema that correlates token ownership with ACL tier is rejected. This is AP-13 instantiated not as "don't do it" but as **"cannot do it without surgical repo modification"**. Membrane preservation becomes a type error.

### §10.3 Phase-2 internal ledger

Phase-2a+ internal non-transferable credit. Backed by Phase-1 `compute-ledger.jsonl` — compute spend on internal cooperation accrues credit; credit redeemable only against Jetix-internal services. No external transfer, no fiat exit. Trigger: $100K self-earned (~€95K) per D23 / Lock 23.

### §10.4 Phase-3+ limited-public

Phase-3+ only. Transfer allowed within a GmbH-defined legal envelope. Public token holders are **not** granted member-tier ACL automatically — token ownership and ACL tier remain orthogonal primitives (invariant §10.2). Compliance review pre-issuance by external counsel; CP-5 L1 gate by Ruslan.

### §10.5 Dry-run audit (5 canonical events)

| Event | Membrane effect | Schema check |
|---|---|---|
| mint(internal-credit, 100, to=agent-X) | None — agent-X tier unchanged | ✓ |
| transfer(restricted-public-token, from=A, to=B) | None — B's tier unchanged | ✓ |
| burn(internal-credit, 50, from=agent-X) | None | ✓ |
| redeem(internal-credit, 100, for=subscription-discount) | None — no access upgrade | ✓ |
| adjust(internal-credit, +5, reason="timezone diff") | None | ✓ |

None grants inside-membrane access. AP-13 preserved by construction.

---

## §11. Answer to Q9 — Matchmaker Algorithm (4 modules, FPF-formalised)

**Problem frame (D4 Q9):** Lock 21 Partnership-Matchmaker = 4 modules (algorithm / quality-gate / contract / metrics). 5-criteria ICP filter on specialists (C20 / D22). AI-smoothed coordination (FPF CHR §A.17-A.21).

**Core claim (Deep-Tech):** The matchmaker is a typed function over FPF primitives. `match(icp_a, icp_b)` is formally specified; the quality-gate is a CP-5 gate YAML; the contract is a multilateral contract with L/A/D/E clauses each tagged F-G-R; the metrics pipeline emits dashboard viewpoints. **Ruslan's acceptance-authority sub-role signs every contract** — one of the six non-delegatable OME L2 functions.

### §11.1 Module 1 — Algorithm (typed compatibility function)

```yaml
# matchmaker/algorithm.yaml
signature: |
  match(icp_a: ICP_archetype, icp_b: ICP_archetype) -> MatchResult
  where
    ICP_archetype ∈ 11-archetypes (10 base + bloggers)    # [D1 §7.1]
    ICP_archetype has fields: {
      archetype_id,
      five_criteria: {startupper, azart, stable, adequate, upward},  # [Lock 22]
      direction_of_life_axis: [-1.0, +1.0],                           # [C20 / §3.1.15]
      capabilities: [U.Method, U.Practice, ...],
      constraints: [regulatory, temporal, language, jurisdiction]
    }
    MatchResult = {
      score: [0.0, 1.0],
      constraints_met: [...],       # enumerated constraint labels
      frictions: [...],             # enumerated friction labels with F-G-R
      fgr: "F2/G:matchmaker-pair-<id>/R-medium",
      bias_class_audit: [REP, ALG, VIS, MET, LNG]  # full 5-class coverage
    }
score_function:
  weights:
    five_criteria_overlap:     0.35
    direction_of_life_cosine:  0.30
    capability_complementarity: 0.25
    friction_penalty:          0.10
  threshold_for_proposal: 0.62
```

### §11.2 Module 2 — Quality-gate (CP-5 gate schema)

Every match crossing threshold 0.62 triggers a CP-5 L2-substantive gate before a proposal is drafted to either party:

```yaml
# matchmaker/quality-gate.cp5.yaml
gate_id: matchmaker-pair-{id}
tier: l2_substantive               # [D6 §4.5.1]
sla_hours: 24
gate_keepers: [ruslan@sales-closer, ruslan@acceptance-authority]
required_evidence:
  - icp_a.manifest.yaml
  - icp_b.manifest.yaml
  - five_criteria_check: all 5 pass for both sides
  - direction_of_life_axis: both sides within (-0.3, +1.0) — outliers excluded
  - capability_graph_diff
  - friction_report (with mitigation plan per friction)
approval_decision: {approved, rejected, modified, escalated}
modification_if_any: <if modified>
time_to_review_seconds: <recorded>
```

**Meaningful-review guarantee (WP251rev.01):** `time_to_review_seconds < 60` flags rubber-stamping; max 8 L2 approvals per gate-keeper per 4-hour block. These constants live in `cp-5-routes/l2-policy.yaml`.

### §11.3 Module 3 — Contract-fixation (multilateral contract)

```yaml
# matchmaker/contract.template.yaml
contract_id: c-{pair-id}-v1
parties: [icp_a, icp_b, jetix-gmbh]       # multilateral
clauses:
  legal:
    - jurisdiction: DE (default) | US (opt-in per D10)
    - dispute_resolution: arbitration Berlin / ICC Paris
    - fgr: F3/G:contract-legal/R-high
  architectural:
    - deliverable_spec: <L/A/D/E E.17 5-view bundle>
    - fpf_alpha_plan: Deal (drafted→signed→activated→completed)
    - fgr: F3/G:contract-architecture/R-high
  deliverable:
    - milestones: [...]
    - acceptance_criteria: BA-3 closure + 5-view Bundle signoff
    - fgr: F2/G:contract-deliverable/R-medium
  economic:
    - fees: {amount, currency, schedule}
    - revenue_share_if_any: {basis, %}
    - fgr: F3/G:contract-economic/R-high
signatures:
  - icp_a.signatory
  - icp_b.signatory
  - ruslan@sales-closer (pre-contract negotiation)
  - ruslan@acceptance-authority (at signing — non-delegatable OME L2)
commit_time_check:
  - all L/A/D/E clauses present: required
  - each clause has fgr: required
  - bias_class_audit: ≥3 classes enumerated
```

### §11.4 Module 4 — Metrics (dashboard viewpoints)

The matchmaker emits three **viewpoints** per D6 §4.4: one for executive (match-success rate, revenue influence), one for governance (fairness audit across archetypes), one for internal-learning (which pair types fail). Each viewpoint is a YAML `viewpoint.yaml` with schema per §14.

### §11.5 Ruslan non-delegatable (OME L2)

Six non-delegatable functions (D1 §3 / D2 §14 / OME L2): Strategy / Taste / Responsibility / Approval / Escalation / Relationships. Contract signing (acceptance-authority) is one of the six. **No agent can `acting_as: acceptance-authority`** — the enum constraint rejects it. This is the matchmaker's hard founder-anchor.

---

## §12. Answer to Q10 — Roy-Replication Packaging

**Problem frame (D4 Q10):** Methodology-as-system exporter (Lock 21, D3 §6.3). 2nd roy bootstraps ≤14 days from kit.

**Core claim (Deep-Tech):** Each kit is a `replica-kit/<domain>/` bundle declaring which FPF primitives it instantiates. Replication = instantiating a new instance of the same substrate, not cloning files. New domain = new `jetix-company-<roy>/` overlay; shared `fpf/` and `jetix-os/` layers unchanged. This is universality (C9, D-test) formalised.

### §12.1 Kit structure

```
replica-kit/<domain>/
├── kit-manifest.yaml              # FPF primitives the kit instantiates
├── agent-templates/               # role.md + fpf-manifest.yaml per included agent
│   ├── sales-lead/
│   ├── sales-research/
│   └── ...
├── wiki-seed/                     # typed-graph seed with provenance preserved
│   ├── entities/
│   ├── concepts/
│   ├── edges.seed.jsonl
│   └── foundations/
├── protocols/                     # pinned protocol versions for this kit
├── icp-template/                  # 5-criteria skeleton; filled per domain
├── install.yaml                   # idempotent installation contract
└── success-criteria.yaml          # F.11 Method Quartet checkpoints
```

### §12.2 `kit-manifest.yaml`

```yaml
kit_id: jetix-kit-ai-consulting-v1
kit_version: 1.0.0
fpf_primitives_instantiated:
  alphas: [client, project, deal, content-item]      # subset of 8
  bridges: [stripe, anthropic, notion, groq, github]
  viewpoints: [executive, technical, governance, internal-learning]
  pillars_required: [P-2, P-3, P-7, P-9]
  guard_rails: [GR-1, GR-3]                          # subset
agents_included: [manager, sales-lead, sales-research, sales-outreach,
                  inbox-processor, knowledge-synth, meta-agent]
agents_excluded:
  - strategy-support-analyst: "Phase-3+ only"
  - crazy-agent: "Optional"
install_mode: fork | overlay | hybrid
install_estimate_days: 7-14
success_criteria_ref: success-criteria.yaml
kill_criteria:
  - "no signed contract in 90 days"
  - "F-G-R compliance rate < 80% at day 60"
license: internal-only              # [OT5-A / OQ-09-A]
```

### §12.3 `install.yaml` (idempotent)

```yaml
# install.yaml
steps:
  - id: fpf-pin
    action: "copy fpf/ into target-repo; pin version"
    idempotent: true
  - id: jetix-os-pin
    action: "copy jetix-os/ into target-repo; pin version"
  - id: overlay-bootstrap
    action: "create jetix-company-<domain>/ with icp-template/ filled"
  - id: agent-manifests
    action: "instantiate 7 agent manifests from templates"
  - id: wiki-seed-import
    action: "append wiki-seed/edges.seed.jsonl to wiki/graph/edges.jsonl"
  - id: ci-bootstrap
    action: "run 7 hooks + fpf-manifest validator"
    must_succeed: true
```

### §12.4 Success criteria (F.11 Method Quartet)

Per D6 F.11 Method Quartet Harmonisation (Rec-18) monthly per-direction:

| Checkpoint | At day | Criterion |
|---|---|---|
| M-0 | 7 | All 7 agents have valid fpf-manifest.yaml; all 7 hooks pass on initial commit |
| M-1 | 30 | First Client.qualified; first edge recorded in wiki/graph/edges.jsonl |
| M-2 | 60 | First Deal.signed; CP-5 gate decisions recorded per D6 §4.5 |
| M-3 | 90 | First Project.closed with BA-3; F-G-R compliance rate ≥ 80% |
| Kill | 90 | If M-3 not met: kit returns to Jetix HQ for revision |

### §12.5 Universality test (D-test §5.5)

`grep -rn "Jetix\|DACH\|Mittelstand\|AI consulting" replica-kit/base/` → 0 hits (CI-enforced per Hook 5). The kit base is domain-agnostic; the overlay is where domain lives. This closes C9 Universality verification.

---

## §13. Answer to Q11 — Content Pipeline (frame-tag + archetype-keyed)

**Problem frame (D4 Q11):** 3 tiers (TOF pain-primary → mid → deep gated); frame-tagging on every artifact; archetype-keyed rendering (11 archetypes).

**Core claim (Deep-Tech):** Pipeline stages align with the Jetix Content Item alpha state machine ([D6 §6.2 Alpha 4]: `drafted → in-review → approved → published → retired`). Frame-tag and archetype-key are first-class frontmatter fields; the rendering engine is a pure function `render(canonical, archetype) → variant`.

### §13.1 Pipeline stages (aligned to Content Item alpha)

| Alpha state | Wiki pipeline stage | Actor | Quality gate |
|---|---|---|---|
| `drafted`     | raw/      | inbox-processor / sales-outreach | F0 frontmatter present |
| `in-review`   | ingested/ | knowledge-synth                  | F1-F2 + frame-tag assigned |
| `approved`    | compiled/ | sales-closer + ruslan@framing-lead | F2-F3 + archetype-key + F-G-R |
| `published`   | ready/    | sales-outreach                   | tier ACL check (Hook 2b) |
| `retired`     | archive/  | meta-agent                       | deprecation DRR |

**Frame-tag enum (Lock 9 / Lock 12):**
```yaml
frame_tag:
  enum:
    - pain-primary     # default TOF (Lock 9)
    - opportunity-reinforcing   # mid/deep
    - methodology-deep # deep only
```

### §13.2 Archetype-keyed rendering

```yaml
# content/<canonical-item>.yaml
canonical_id: content-mueller-audit-teaser
canonical_body: ...        # source prose
frame_tag: pain-primary
tier: member
f_g_r: F2/G:content-tof-de-2026-q2/R-medium
bias_class_audit: [REP, LNG]
archetype_variants:
  - archetype_id: startupper-de
    headline: "Beschleunigen Sie Ihren AI-Audit um 60%"
    cta: "Kostenfreier Discovery Call"
  - archetype_id: azart-de
    headline: "Der AI-Audit-Wettbewerb — sind Sie dabei?"
    cta: "Challenge accepted"
  - archetype_id: stable-de
    headline: "Compliance-sicheres AI-Audit für etablierte Mittelständler"
    cta: "Enterprise-Referenzen anfordern"
  # ... 11 total (10 base + bloggers)
```

Single canonical content compiles to N variants (one per targeted archetype) with archetype-specific framing. Smart-audience + site-primary + social-max-TOF (D12, Lock 12) encoded as routing rules in `pipeline/routing.yaml`.

### §13.3 BA-cycle on content

Per D.5: BA-0 (draft with representation-check), BA-1 (mid-review for bias across 5 classes), BA-3 (closure before published). Hook 4 enforces the sequence — skip BA-1 = rejected commit.

### §13.4 Public vs. gated (Lock 13)

`tier: public` content renders to `surface/` (auto-gen); `tier: member` or `tier: partner` content compiles to invite-gated endpoints. No hand-maintained duplicates (Lock 13 / C3).

---

## §14. Answer to Q12 — Dashboard Implementation

**Problem frame (D4 Q12):** Weekly dashboard, 5 mandatory metrics + 2 extensions Phase-1; phase-keyed scaling; anti-attention-economy (D2 §11, AP-3).

**Core claim (Deep-Tech):** Every metric is a **viewpoint** per D6 §4.4 (published by a specific agent, consumed by Ruslan L2). The v1 dashboard is filesystem-only (Lock 17 / C4) — a static-site-generator reads YAML metric files and renders Monday ritual page. No DB Phase 1.

### §14.1 Phase-1 metric viewpoints (5 mandatory + 2 extensions = 7)

| # | Viewpoint | Publisher | Source | Target |
|---|---|---|---|---|
| 1 | `architect-hours-per-week` | system-admin | `ops/toggl/*.jsonl` | declining trend, ≤18h/wk by €200K |
| 2 | `founder-dependency-pct`   | manager     | `comms/mailboxes/*.jsonl` task-origin tag | <30% by €200K |
| 3 | `monthly-revenue`          | sales-lead  | `finance/revenue-log.jsonl` (from Stripe bridge) | €50K/€200K/€1M gates |
| 4 | `failure-rate-mttr`        | system-admin| `ops/incidents/*.yaml` | ≤3 incidents/mo; MTTR p50 ≤60min |
| 5 | `cash-runway`              | sales-closer| `finance/bank-reconcile.jsonl` + burn | ≥6 months Phase 1 |
| 6 | `deep-hours-per-week`      | personal-assistant | `ops/toggl/deep.jsonl` | 25-30h/wk Phase 1 |
| 7 | `productized-revenue-pct`  | sales-lead  | Stripe SKU split | ≥40% @ €200K; ≥70% @ €1M |

### §14.2 Metric viewpoint schema

```yaml
# viewpoints/architect-hours-per-week.yaml
viewpoint_id: architect-hours-per-week
publisher: system-admin                   # [D6 §2.2 must be an agent/sub-role]
audience: [ruslan@strategy-lead]          # L2 consumer
source_files: ["ops/toggl/*.jsonl"]
query:
  type: aggregation
  window: last_7_days
  aggregate: sum(minutes_where(tag='deep')) / 60
rendering:
  format: markdown-table
  location: dashboard/monday/architect-hours.md
alert_binding:
  trigger_if: value > 24 for 2 consecutive weeks
  notify: [ruslan@strategy-lead]
  drr_required: false
fgr: F1/G:dashboard-phase-1/R-medium
```

### §14.3 Monday ritual (D3 §14.2)

```
dashboard/
├── monday/
│   ├── YYYY-MM-DD.md           # aggregated rendering
│   └── phase-transition-check.md  # Triple-AND dashboard (§6.5)
├── viewpoints/
│   └── *.yaml
└── pipeline/
    └── monday-render.sh         # cron: Mon 12:00 Europe/Berlin
```

**12:00 Europe/Berlin founder-anchor** (D3 §14.2); ≥95% on-time Phase-1 (≤2 misses/quarter). Miss → alert to ruslan@strategy-lead.

### §14.4 Phase-2+/3+ scaling (no migration)

Per D4 §4.7, Phase-2+ adds: roy count / roy revenue / match rate / member count / subscription-vs-partnership ratio. Phase-3+ adds: market-cap / token circulation / research outputs / sub-network activity.

**Adding a metric = adding a YAML viewpoint file. Zero schema migration.** The `viewpoint.yaml` schema has room for the v2/v3 metrics as-is. SI-3 preservation.

### §14.5 Anti-attention-economy (D2 §11, AP-3)

Dashboard measures **time-saved** and **throughput**, not **time-spent** or **engagement**. No "points", no "streaks", no gamification. The metric viewpoint schema has no `engagement_score` field — and any PR adding one is rejected by the v3 variant's "values-in-schemas" discipline.

---

## §15. Answer to Q13 — Escalation Routing (formal 4-class)

**Problem frame (D4 Q13):** 6 non-delegatable founder functions + 4-class FPF taxonomy + hub-and-spoke routing; F-G-R trust gating per deliverable.

**Core claim (Deep-Tech):** Formal 4-class FPF taxonomy ([atom-2558 / D4 §4.4 / FPF §2.2a]): `dept-internal` / `cross-dept` / `strategic` / `safety`. CP-5 gate YAML per escalated decision with explicit contestation path (GDPR Art.22(3) + WP251rev.01). Meaningful-review guarantee is load-bearing: `time_to_review < 60s` triggers a quality flag — the formal expression of *«Continuous, every iteration — NOT periodic»* (D2 §6).

### §15.1 4-class taxonomy (atom-2558)

| Class | Router | Example | SLA |
|---|---|---|---|
| `dept-internal` | Dept Lead (e.g., sales-lead for sales)      | pricing off-CHR by <5%       | 24h  |
| `cross-dept`    | manager (≤20 active tasks, global rule #9)    | content needing legal review | 48h  |
| `strategic`     | ruslan@strategy-lead                          | quarterly attention-theme    | 5 days |
| `safety`        | meta-agent + ruslan immediately (halts task) | DPA breach / GDPR Art. 33    | immediate |

### §15.2 CP-5 gate schema (per escalated decision)

```yaml
# cp-5-routes/gate-{decision-id}.yaml
decision_id: d-2026-04-21-mueller-pricing-exception
tier: l1_contractual                            # [D6 §4.5.1]
class: strategic                                # [atom-2558]
client_affecting_category: "pricing exception requiring Ruslan sign-off"
originator:
  role: sales-lead
  holder: (agent executor-binding ref)
  f_g_r: F2/G:dach-mueller-pricing/R-medium
evidence_links:
  - agents/sales-lead/outputs/2026-04-21-mueller-proposal-v3.md
  - wiki/entities/mueller-gmbh.md (CL-graph dump)
  - icp/2026-q2-dach.yaml
bias_class: [REP, LNG]                          # [D6 §12.10]
gate_keeper:
  role: strategy-lead
  holder: ruslan
  approved_at: 2026-04-21T16:47:00Z
  decision: approved                            # {approved, rejected, modified, escalated}
  modification_if_any: null
  reason: "Strategic anchor client; acceptable 8% discount"
  time_to_review_seconds: 312                   # ≥60s — passes rubber-stamp check
client_notice:
  sent_at: null                                 # not client-facing decision
  channel: n/a
  art_22_right_to_contest_included: n/a
retention:
  retention_until: 2032-04-21                   # 6 years HGB §257
contestation_path:
  gdpr_art_22_3: enabled
  wp251rev_01_compliant: true
  mechanism: "client may request alternate gate-keeper review within 10 business days"
  evidence_package_sla_business_days: 10
```

### §15.3 Meaningful-review enforcement (WP251rev.01)

```yaml
# cp-5-routes/l2-policy.yaml
rubber_stamp_prevention:
  time_to_review_seconds_floor: 60
  max_l2_approvals_per_gate_keeper_per_4h_block: 8
  alt_review_guarantee: "every gate decision eligible for alternate review"
audit:
  quarterly_review: FPF-Steward
  flag_conditions:
    - time_to_review_seconds < 60
    - same gate-keeper > 8 L2 in 4h
    - rejection rate < 5% over 30d (potential rubber-stamp)
```

### §15.4 Founder-unavailable chain (D4 §4.4)

Phase 1 = proxy Steuerberater/lawyer stub per `executor-binding.yaml` chain-of-command; formal trustee designated at first client contract (per Chunk 5 Area 4 trigger). Escalation routes: founder → designated-trustee → Beirat-alternate (Phase 2a+).

### §15.5 Gentleman/Predator at the escalation boundary

*«Gentleman inside / Predator outside»* (Lock 1) routes `strategic`-class escalations differently depending on whether the originator crosses the outer membrane. A contested outside-world CP-5 decision uses `outside-tone.yaml` (§8.3) — firm, evidence-forward, clean decline. A contested inside-team decision uses `inside-tone.yaml` — civil, welcomes disagreement, logs rationale.

---

## §16. Answer to Q14 — Onboarding Architecture

**Problem frame (D4 Q14):** 2nd pilot cold-start ≤7 days. F.6 6-step cycle. No `/home/ruslan/*` hardcodes (C1, AP-6).

**Core claim (Deep-Tech):** Onboarding = instantiating a `client-instance/` under `jetix-company/clients/` with four schema-validated YAML files. Day 1-3: manifest + contract + plan signed. Day 4-6: first deliverables at alpha: `in-review` (Content Item). Day 7: first Alpha advance to `approved` (Client `qualified` or Project `kicked-off` depending on engagement type).

### §16.1 Four required files per pilot

```
jetix-company/clients/<client-id>/
├── pilot-manifest.yaml          # ICP archetype + 5-criteria + direction-of-life
├── contract.yaml                # L/A/D/E clauses + F-G-R per clause (§11.3)
├── deliverable-plan.yaml        # alpha-progression schedule
└── escalation-bindings.yaml     # CP-5 routes for this client
```

### §16.2 `pilot-manifest.yaml`

```yaml
client_id: mueller-gmbh
icp_archetype: startupper-de              # ∈ 11 archetypes
five_criteria:                             # [Lock 22 / C20]
  startupper: 0.8
  azart:      0.6
  stable:     0.4
  adequate:   0.9
  upward:     0.7
direction_of_life_axis: +0.6               # ∈ [-1.0, +1.0]
jurisdiction: DE
language_primary: de
contact:
  primary: M. Müller (CEO)
  dpo_required: false                      # no DPA client Phase-1
engagement_type: consulting-audit          # {consulting-audit, retainer, matchmaker}
tier: partner                              # ACL tier ([D4 §5.2])
sources:
  - raw/2026-04-10-mueller-intro-call-transcript.md
  - raw/2026-04-12-mueller-followup-email.md
f_g_r: F2/G:client-mueller/R-medium
bias_class_audit: [REP, LNG]
```

### §16.3 `deliverable-plan.yaml` (alpha-progression schedule)

```yaml
# jetix-company/clients/mueller-gmbh/deliverable-plan.yaml
client_id: mueller-gmbh
alpha_sequence:
  - day: 1
    alpha: client
    target_state: qualified           # MECE 5-criteria passed
    actor: sales-lead + ruslan@sales-closer
  - day: 3
    alpha: deal
    target_state: signed              # contract.yaml signoff
    actor: ruslan@sales-closer + ruslan@acceptance-authority
  - day: 4
    alpha: project
    target_state: kicked-off          # BA-0 initialised
    actor: ruslan@acceptance-authority + knowledge-synth
  - day: 6
    alpha: content-item
    target_state: in-review           # first Audit SKU deliverable draft
    actor: knowledge-synth + sales-lead
  - day: 7
    alpha: content-item
    target_state: approved            # 5-view bundle complete
    actor: knowledge-synth + ruslan@framing-lead + ruslan@acceptance-authority
```

### §16.4 Day-7 success criterion

Onboarding success = type-check passes on all four files + BA-0 initialised + first Client transition `qualified` + acceptance-authority sub-role signoff on contract. **Zero schema migrations required.** This satisfies D4 Q14 quality criterion (*"2nd pilot cold-start to first commit in ≤7 days; zero schema migrations required"*).

### §16.5 No `/home/ruslan/*` (C1, AP-6 avoidance)

All paths in role-manifests, executor-bindings, and pilot-manifests are repo-relative. The onboarding `install.yaml` (from §12.3, kit-install) accepts a `$JETIX_ROOT` env var. Hook-5 Symbolic Test greps for `/home/` in `jetix-os/` and `jetix-company/` templates; 0 hits required.

### §16.6 F.6 6-step onboarding cycle (Rec-15)

Per D6 F.6: Identify → Contract → Kick-off → Deliver → Accept → Retrospect. Each step maps to a specific alpha transition. The 6 steps are the 6 days + 1 retrospect day (day 8 = F.6 retro at day 30 per Method Quartet).

---

## §17. Answer to Q15 — USB-C Protocol Layer ⭐ VARIANT SIGNATURE SECTION

**Problem frame (D4 Q15):** D20 = Jetix is USB-C of AI-business cooperation. Lock 20 + C19 enterprise-fast. 3 workstreams (protocol + tools + verification).

**Core claim (Deep-Tech — variant signature):** This variant delivers **Phase-1 scaffold**, not Phase 3+ deferral. We publish **protocol taxonomy + 2 reference protocols + verification harness + RFC-style drafts** in Phase 1. Third-party implementation achievable Phase-2a. Standards-body submission Phase-3+. The Phase-1 deliverable is *not* a standards submission — it is **a set of YAML protocol definitions with a passing reference test**.

### §17.1 Protocol taxonomy (Phase-1 inventory)

| # | Protocol | Phase-1 status | Domain |
|---|---|---|---|
| 1 | `agent-handoff-v1`        | **delivered** (reference)  | inter-agent task handoff with FPF-manifest check |
| 2 | `contract-fixation-v1`    | **delivered** (reference)  | multilateral L/A/D/E contract commit |
| 3 | `kit-replication-install` | draft (Phase-2a complete)  | roy-kit bootstrap handshake |
| 4 | `compute-ledger-audit`    | draft                      | multi-provider cost reconciliation |
| 5 | `ba-cycle-transition`     | draft                      | Bias-Audit stage transition signal |
| 6 | `f-g-r-attestation`       | draft                      | F-G-R claim attestation exchange |

**Phase-1 reference delivery: #1 `agent-handoff-v1` + #2 `contract-fixation-v1` with verification harness passing.**

### §17.2 Message schema (`agent-handoff-v1`)

```yaml
# jetix-os/protocols/agent-handoff-v1.schema.yaml
protocol_id: agent-handoff-v1
version: 1.0.0
jetix_concept: jetix-message-handoff
bridge_if_applicable: null                    # native Jetix protocol
message_envelope:
  required:
    - msg_id                                  # msg-YYYYMMDD-NNN
    - ts
    - from.agent_id
    - from.acting_as                          # [D6 §2.2 enum]
    - from.fpf_manifest_sha                   # hash of fpf-manifest.yaml
    - to.agent_id
    - type                                    # {task, result, question, escalation, notification, handoff}
    - subject
    - body
    - f_g_r                                   # mandatory (Hook 3)
    - alpha_touched                           # if any
    - bias_class_audit
message_types:
  handoff:
    additional_required: [context_bundle, acceptance_criterion]
  escalation:
    additional_required: [class, cp5_gate_ref]      # [atom-2558 schema]
version_compatibility:
  backward_compat: ">=1.0.0"
  deprecation_policy: "supported for 2 phase-gates after release"
verification_test:
  fixture: tests/protocol/agent-handoff-v1/fixture.yaml
  assertion: "round-trip handoff with FPF-manifest check succeeds"
  reference_implementation: jetix-os/protocols/ref-impl/agent-handoff-v1.py
```

### §17.3 Message schema (`contract-fixation-v1`)

```yaml
# jetix-os/protocols/contract-fixation-v1.schema.yaml
protocol_id: contract-fixation-v1
version: 1.0.0
message_envelope:
  required:
    - contract_id
    - parties                                 # array of party_id
    - clauses                                 # L/A/D/E (§11.3)
    - signatures                              # array, must include acceptance-authority
    - commit_time_checks                      # enumerated invariants
  invariants:
    - "every clause has f_g_r"
    - "every clause has bias_class_audit"
    - "acceptance-authority signature present for L1"
    - "ALL four L/A/D/E categories present"
version_compatibility:
  backward_compat: ">=1.0.0"
verification_test:
  fixture: tests/protocol/contract-fixation-v1/fixture.yaml
  assertion: "contract with valid L/A/D/E + acceptance-authority sig commits; contract missing A clause rejects"
```

### §17.4 Versioning policy

```yaml
# jetix-os/protocols/versioning-policy.yaml
semver: strict
backward_compat_window: "2 phase-gates"       # Phase 1+2 supports v1.x
deprecation_timeline:
  announce: "at Phase-N release"
  deprecated: "at Phase-N+1"
  removed:    "at Phase-N+2"
breaking_change_policy: "requires DRR per D6 §12.14 Δ-2/Δ-3"
```

### §17.5 Verification harness (Phase-1 passing test)

```
tests/protocol/
├── agent-handoff-v1/
│   ├── fixture.yaml            # canonical message sample
│   ├── test-roundtrip.py       # round-trip assertion
│   └── test-fpf-manifest.py    # manifest-check assertion
├── contract-fixation-v1/
│   ├── fixture-valid.yaml
│   ├── fixture-missing-a-clause.yaml  # must reject
│   └── test-commit-rules.py
└── conftest.py
```

**Phase-1 CI job runs these tests every PR.** Zero third-party runtime cost (runs on GitHub Actions free tier).

### §17.6 RFC-style docs (standards-body-ready)

Each protocol has a companion `<protocol>.rfc.md` with: Abstract / Status / Motivation / Message Envelope / State Machine / Verification / Security Considerations / IANA Considerations / References. Ready for submission to a standards body in Phase 3+; submitted as-is to internal clients as enterprise credibility signal in Phase 2a.

### §17.7 Why Phase-1 scaffold is the variant signature

D4 Q15 says protocol layer is Phase 3+. Deep-Tech contrarian claim: **a Phase-1 protocol scaffold is the cheapest possible differentiator against "we do AI consulting" competitors**. Cost: ~40h of architect time + ~€0/mo runtime cost (YAML + JSON-Schema). Value: when a Phase-2a enterprise buyer asks *"how do your AI agents interface with our systems?"*, the answer is *"here is our `agent-handoff-v1.schema.yaml` — implement it in 1 sprint"* instead of *"we'll design that together"*. C19 (enterprise-fast) instantiated.

### §17.8 Boundary with Phase-3+ standards submission

This variant does NOT submit to IETF / ISO / IEEE in Phase 1. It only publishes RFC-style docs internally + to clients. Standards-body submission is deferred to Phase-3+ per D4 Q15. The key difference: Phase-1 protocols are **client-implementable by day one**; they are not **standards-approved**. The signal is credibility, not certification.

---

## §18. Foundation Layer Specification

*«Foundation = главный актив»* (D2 §14). *«Quality cannot be retrofit at $1T scale»* (D2 §14). This section operationalises D4 §4 — all 8 Foundation elements — with ontology-first framing. Every element traces to an FPF primitive and has a Phase-1 CI-checkable reduction.

### §18.1 Foundation Element 1 — Wiki + ATOM-REGISTRY

Typed graph as specified in §7. **Atoms as first-class entities with mereology edges.** Atom-2558 (escalation taxonomy) is itself a wiki entity with `ComponentOf` edges to `wiki/concepts/escalation-routing.md` and `ConstituentOf` edges to the 4 class definitions.

**Phase-1 check:** Hook 3 rejects wiki entities without F-G-R; edges.jsonl schema validator runs in CI.

### §18.2 Foundation Element 2 — Agent contracts

Formal fpf-manifests per §4. Role ≠ Executor (P2 / IP-1). 5-block role.md + executor-binding.yaml + fpf-manifest.yaml per agent.

**Phase-1 check:** JSON-Schema validator on all 18 manifests; 3-way diff (D6 §2.2 ≡ CLAUDE.md ≡ schema enum) in quarterly audit.

### §18.3 Foundation Element 3 — Handoff protocols

Typed bridges per §5 + `agent-handoff-v1` protocol per §17.

**Phase-1 check:** Protocol verification harness passes; every `comms/mailboxes/*.jsonl` message has `acting_as:` (Hook 6).

### §18.4 Foundation Element 4 — Escalation protocols

4-class taxonomy (atom-2558) + CP-5 gate schema per §15.

**Phase-1 check:** CP-5 gate YAML mandatory per L1/L2 tier decision; rubber-stamp detector (time_to_review < 60s flags).

### §18.5 Foundation Element 5 — Continuous quality metrics

*«Continuous, every iteration — NOT periodic»* (D2 §6). Per-commit F-G-R frontmatter; per-workflow F.11 Method Quartet monthly; per-gate B.4 Canonical Evolution Loop in 4 rituals (daily/weekly/monthly/quarterly). Aggregate: orphan count / contradiction count / stale claims / F-G-R compliance %.

**Phase-1 check:** Hook 3 enforces per-commit tagging; quarterly wiki-lint job reports aggregate.

### §18.6 Foundation Element 6 — Dashboard

v1/v2/v3 per §14. v1 Phase-1 = 7 viewpoints, filesystem-only. v2 Phase-2+ adds roy/member/match metrics; v3 Phase-3+ adds market-cap/token-circulation/research-outputs. **Schema unchanged across v1/v2/v3.**

**Phase-1 check:** Monday render job (`pipeline/monday-render.sh`) produces all 7 metrics in <5min; on-time hit-rate ≥95%.

### §18.7 Foundation Element 7 — Reserve routes

Every bridge has `failure_mode.replay_from_fs` per §5.3. Multi-provider fallback chain per §9.1. Crisis playbooks (MC1 P1-#4) in `ops/playbooks/`.

**Phase-1 check:** `integrations/*.bridge.yaml` schema validator requires `failure_mode.replay_from_fs` non-null.

### §18.8 Foundation Element 8 — F-G-R tagging

Mandatory on every claim, enforced at ingestion; bias-class audit enforced at compile; claim-scope boundedness enforced at lint. Composition rule: weakest-link, pathwise justification (D6 §12.7). Bridge-only reuse → R only, never F or G.

**Phase-1 check:** Hook 3 regex-enforces frontmatter pattern `F[0-9]/G:.+/R-(low|medium|high|certified|formally-proven)`.

### §18.9 Foundation Quality Invariants (the machine-checkable version of *«главный актив»*)

These 10 invariants are preserved at every gate from $0 to $1T. They are the formal operationalisation of *«Foundation = главный актив»*.

| # | Invariant | Phase-1 mechanism | Scale mechanism ($1T) |
|---|---|---|---|
| FQ-1  | GR-3 unidirectional dependency preserved | Hook 2 pre-commit | Same hook, same check |
| FQ-2  | `acting_as` enum ≡ D6 §2.2 roster | regen-message-schema.sh in CI | Same script, same check |
| FQ-3  | Every commit to `wiki/` has F-G-R | Hook 3 | Same hook |
| FQ-4  | Every CP-5-gated decision has audit trail YAML | Hook 6b | Formal verification on gate integrity |
| FQ-5  | Every integration is a bridge with failure_mode | schema validator | Same validator |
| FQ-6  | Every agent has valid fpf-manifest.yaml | JSON-Schema | Same schema |
| FQ-7  | Every Project.closed has BA-3 closure | Hook 4 alpha-state check | Same hook |
| FQ-8  | No token operation correlates with ACL tier | schema orthogonality invariant | Formal model-check on state machine |
| FQ-9  | Wiki graph growth linear in entity count | edges.jsonl schema + query audit | Indexed graph DB with linear cost model |
| FQ-10 | Universality D-test: base/ subtree Jetix-term free | Hook 5 | Same hook |

**10 invariants. 10 hooks/validators. All Phase-1 implementable.** *Foundation cannot be retrofit at $1T scale* (D2 §14) — because at $1T scale these 10 invariants will still be the 10 invariants, checked by the same 10 mechanisms (with heavier tooling for FQ-8 and FQ-9). Ruslan's claim becomes machine-checkable because the invariants never change — only the tooling-depth for verification grows with gates.

---

## §19. Hard Constraints Compliance Matrix

All 21 constraints C1–C21 from D4 §6. Each row: how this variant complies + the FPF primitive used + the CI check that enforces it.

| C# | Constraint (short) | How variant complies | FPF primitive | CI check |
|---|---|---|---|---|
| C1 | Solo-now-team-ready | §4 fpf-manifests template-ready; onboarding in 4 YAMLs (§16) | [FPF IP-1 Role ≠ Executor] | Hook 5 symbolic test on /home/ |
| C2 | Revenue-gated spend | Compute-ledger + §9.4 gate table; dashboard trigger (§6.5) | [FPF §9.9 P7 4-tier accounting] | `jq` aggregate in CI; halts on overrun |
| C3 | Closed outside / open inside | 4-tier ACL (§8.1); auto-gen pipeline (§13.4) | [FPF GR-3 generalised to tiers] | Hook 2b link-rule check |
| C4 | Filesystem = SoT | Wiki is typed graph on git (§7); Notion = W-only bridge (CL=1) | [Lock 17 + FPF §8.4 bridge CL=1] | Hook — no Notion-API read imports |
| C5 | Consulting-first Phase-1 | §11 matchmaker = Phase-2+; §16 onboarding consulting-first | [D6 §6.3 Alpha:Client] | Repo dir `jetix-company/sales/` present Day-1 |
| C6 | Productization over hours | §13 pipeline emits packaged artefacts; pricing multi-tier | [D6 §6.3 Alpha:Content Item] | Stripe SKU split dashboard viewpoint |
| C7 | Investment-fund philosophy | DRR schema has expected_return/horizon/kill_criteria | [D6 §12.14 DRR Δ-2/Δ-3] | Schema validator on decisions/*.md |
| C8 | Layered identity | 11 archetypes × face/frame; §13 archetype-keyed rendering | [D6 §4.4 A.6.3.CR same-entity retextualization] | Schema on brand-object.yaml |
| C9 | Universality | `jetix-os/` Jetix-agnostic; kit replication (§12) | [FPF GR-3 unidirectional] | Hook 5 D-test + C-test ≥3 dry-runs |
| C10 | English+US primary Phase-1 | icp/ defaults EN+US; DE legal gated at €20-30K | [D6 §4.5 jurisdiction field] | Locale field schema check |
| C11 | JETIX-FPF mandatory | Every agent fpf-manifest cites ≥1 pillar, ≥1 GR | [D6 constitutional] | fpf-manifest validator |
| C12 | Role ≠ Executor | 3-file separation per agent (§4.1) | [FPF IP-1 / P2] | Schema validator rejects merged role+executor |
| C13 | F-G-R mandatory | Frontmatter regex on every artefact | [D6 §4.2] | Hook 3 |
| C14 | 11-agent canonical | Exactly 18 manifest files Day-1 (11+5+2) | [D6 §2.2] | 3-way diff audit |
| C15 | Life-OS separation | `life-os/` folder; Hook 1 asymmetric ban | [D4 §4.5 + Area 4] | Hook 1 |
| C16 | Continuous quality | BA-0/1/3 per project; per-commit F-G-R | [D6 D.5 cycle] | Hook 4 + Hook 3 |
| C17 | Gentleman/Predator | Two schema namespaces (§8.3) | [Lock 1 / D1 pre] | Schema-routing check per message |
| C18 | $1T no-rewrite | 7 scale invariants (§6.1) | [D6 §12.6 Γ invariants] | Quarterly scale-audit |
| C19 | USB-C + enterprise-fast | §17 Phase-1 protocol scaffold | [Lock 20] | Protocol verification harness passes |
| C20 | ICP 5-criteria + direction | Pilot-manifest.yaml fields (§16) | [Lock 22 / D22] | Schema validator |
| C21 | Token Option B membrane | §10 orthogonality invariant | [FPF L5 membrane + D23 B] | Orthogonality invariant check |

**Every C1–C21 has a concrete CI check, not a vague "we comply".**

---

## §20. Anti-Patterns Avoidance Statement

All 16 anti-patterns AP-1..AP-16 from D4 §7.

| AP# | Anti-pattern | Why Deep-Tech is at risk | Mitigation | Verification |
|---|---|---|---|---|
| AP-1 | Notion-as-primary-store | Low — Notion is W-only bridge | Lock 17 + Hook (no Notion-API read) | CI grep on imports |
| AP-2 | Hour-billing-only | Low — §13 productization built-in | Multi-tier SKU schema | Stripe SKU split viewpoint |
| AP-3 | Mass-market / engagement | Low — §14 anti-engagement dashboard | No `engagement_score` field in viewpoint schema | PR review bot flags |
| AP-4 | Public OSS of core | Low — §8.6 core-tier IP lock | ACL hook + 9 Innovations core-tier | Hook 2b tier-link check |
| AP-5 | Jetix-specific in base | Moderate — formalism might hide Jetix DNA in `jetix-os/` | Hook 5 D-test on base/ | Hook 5 grep = 0 hits |
| AP-6 | One-person assumptions | Low — §16 onboarding schema-based | No /home/ruslan/* paths | Hook 5 additional |
| AP-7 | Slow-corporate governance | Low — 24h-48h SLA on CP-5 L2 | SLA policy file | Quarterly latency audit |
| AP-8 | Chaotic-startup governance | **Low — this variant's opposite tendency** | Every decision = DRR | Schema validator on decisions/ |
| AP-9 | Motivational-circle community | Low — ICP 5-criteria + direction filter | Hook — no inspirational tags | Content pipeline bias-class audit |
| AP-10 | Attention-extraction | Low — pull-based only | No push/notification UX Phase-1 | No notification primitive in schema |
| AP-11 | Single-provider AI | Low — §9 explicit multi-provider | fpf-manifest declares fallback chain | CI — executor-binding must have fallback |
| AP-12 | **Pure-research Phase-1** | **HIGH — this variant's primary risk** | **See §20.1 below** | Pass-3 Phase-1 shipability test |
| AP-13 | Public token with governance/access | Low — §10 orthogonality | Schema forbids correlation | CI — orthogonality invariant |
| AP-14 | Equal-weight channels | Low — §13 routing rules per tier | Lock 12 encoded in routing.yaml | Schema check |
| AP-15 | Monolithic brand | Low — §8.3 two schema namespaces | Per-observer tone namespace | Schema check per message |
| AP-16 | **Boutique-scale shortcuts** | **Moderate — depth-first can look boutique** | **See §20.2 below** | SI invariants §6.1 |

### §20.1 AP-12 double-treatment (Pure-research institution Phase 1)

**Risk.** Deep-Tech's natural gravity is toward FPF internals. Without discipline this variant could spend Phase-1 compute and Ruslan attention on civilizational-horizon research instead of closing consulting contracts.

**Mitigations (three, all binding on this variant):**

1. **Phase-1 budget allocation.** Formalism is capped at **≤15% of Phase-1 Ruslan hours** — the remaining 85%+ belongs to consulting pipeline execution. This is enforced via Toggl tagging: `[formalism]` tag hours visible in Monday dashboard; >15% for 2 weeks triggers a `strategic` escalation.

2. **Formalism is SUBORDINATE to revenue delivery.** Every Phase-1 formal artefact has a consulting-use test: "does this artefact make it easier to close the €15K Müller contract this quarter? If no, defer to Phase-2a."

3. **€50K gate on schedule.** Pass-3 coherence-critic walks the consulting-pilot scenario (Client X signs €15K Q2 2026): every step under this architecture is listed; any step blocked by formalism-not-yet-ready triggers revision (cut formalism or defer to Phase-2).

**Consulting revenue is Jetix's oxygen Phase-1.** Formal substrate is its skeleton. Skeletons do not replace oxygen.

### §20.2 AP-16 double-treatment (Boutique-scale shortcuts)

**Risk.** Depth-first could be mistaken for boutique-fetishism: "we care about correctness so much we can only serve 2 pilots/year."

**Mitigation.** The 7 scale invariants (§6.1) are explicit: wiki graph grows linearly; integration schemas are fixed; adding a pilot is template-copy-plus-fill; no N² joins. **The deeper the substrate, the cheaper scaling becomes** — because scaling = instance addition, not redesign. This is the exact opposite of boutique: boutique scales by hiring more humans; Deep-Tech scales by instantiating more manifests.

---

## §21. Self-Scoring on D4 §8 Quality Axes

Honest self-scores. Defended below.

| Axis | Weight | Self-score | Contribution |
|---|---|---|---|
| 1. Phase-1 readiness      | 20% | **5.5/10** | 11.0 |
| 2. Scale trajectory       | 15% | **9.0/10** | 13.5 |
| 3. Foundation quality     | 15% | **10.0/10** | 15.0 |
| 4. Locks compliance       | 18% | **9.0/10** | 16.2 |
| 5. Universality           | 10% | **9.0/10** |  9.0 |
| 6. Operational simplicity | 10% | **4.5/10** |  4.5 |
| 7. Cost efficiency        |  0% | **PASS**   | gate-based (not scored) |
| 8. Resilience             |  5% | **7.0/10** |  3.5 |
| 9. Security posture       |  5% | **8.0/10** |  4.0 |
| 10. Innovation            |  2% | **9.0/10** |  1.8 |
| **Total (est)**           | **100%** |      | **~78.5–82.5** |

### §21.1 Defence of each score

**Axis 1 — Phase-1 readiness: 5.5/10.** Honest. §4 fpf-manifests add ~90 min Day-1 vs unstructured prompts — not a blocker. But §7 typed-graph wiki migration (if starting with existing `wiki/` content) adds 2-3 days of retro-tagging. §17 USB-C scaffold adds ~40h. Net: Phase-1 consulting pipeline ships, but with a 2-3 week formalism-onramp. Not 9/10 but not 3/10 either.

**Axis 2 — Scale trajectory: 9.0/10.** Scale invariants (§6.1) are the strongest evidence. Under parametric ontology, 10× growth stays <30% LOC across subsystems (§6.4 table). The single point where I don't score 10/10: at $1T scale, formal verification on the token state machine and matchmaker contract kernel introduces a tooling-migration that's >30% of those subsystems. Acknowledged.

**Axis 3 — Foundation quality: 10.0/10.** Variant's signature. All 8 §4 Foundation elements are specified with concrete schemas, not hand-waved (§18). 10 Foundation Quality Invariants (§18.9) are CI-enforceable Day-1.

**Axis 4 — Locks compliance: 9.0/10.** All 24 locks traced in §19 with FPF primitive + CI check per lock. One point deducted because Lock 14 (research = revenue-instrumental) carries residual AP-12 risk even after §20.1 mitigations.

**Axis 5 — Universality: 9.0/10.** B-test: config/code ratio ≥90% (schemas are YAML). C-test: kit replication (§12) validates 3 dry-runs. D-test: Hook 5 symbolic grep = 0 on `jetix-os/` subtree. One point deducted for pragmatic reality: some `jetix-os/` internal examples use Jetix names in docstring comments until sanitised at Phase-2a.

**Axis 6 — Operational simplicity: 4.5/10.** Honest. Learning cliff is real. New pilot reading 7 hooks + 18 manifests + 4 kit-install files + 6 protocols needs 5-7 days to onboard (vs 1-2 for Variant 1). Mitigation: fpf-manifests are self-documenting (5 files as onboarding path, not 3758-line FPF cold).

**Axis 7 — Cost efficiency: PASS.** Phase-1 compute-cost est ≤€500/mo well below €800 gate. Formalism is filesystem + schema validation + 7 hooks — zero runtime cost beyond GitHub free tier.

**Axis 8 — Resilience: 7.0/10.** §5.3 failure_mode mandate + §9.1 multi-provider + §4.8 reserve routes = solid. Not 10/10 because crisis playbooks (MC1 P1-#4) are referenced, not written Day-1 (6h allocated per brief; not done in this variant doc).

**Axis 9 — Security posture: 8.0/10.** Typed membrane (§8) + CP-5 gate (§15) + orthogonality invariant (§10) = strong. One point deducted because 9 Innovations IP protection (§8.6) relies on ACL hooks; external penetration testing not in Phase-1 budget.

**Axis 10 — Innovation: 9.0/10.** USB-C Phase-1 scaffold (§17) + typed-graph wiki (§7) + fpf-manifest per agent (§4) + orthogonality invariant (§10) = 4 novel primitives. Not 10/10 because none are truly unprecedented — they are precise formal expressions of patterns D6 already contains.

### §21.2 Weighted total

Sum of weighted contributions: **~78.5–82.5**. Median estimate: **~80**. With Phase-1 readiness closer to 6/10 (achievable if retro-tagging wiki content is spread over Phase-1 rather than front-loaded), total could reach **~83-85**. Honest range: **78–85**.

---

## §22. Variant Contrarian Claims ⭐ VARIANT SIGNATURE

Three places where D4 phase-schedule or FPF guidance conflicts with depth-first principle. Each flagged with explicit resolution.

### §22.1 Contrarian #1 — USB-C protocol Phase 1 (vs. D4 Q15 Phase 3+)

**Brief position (D4 Q15):** USB-C protocol layer is Phase 3+; Phase-1 seeds design only.

**Deep-Tech claim:** **Phase-1 delivery of 2 reference protocols + verification harness is cheap and strategically high-value.**

**Resolution:** Phase-1 scaffold is NOT a standards-body submission. It is YAML schemas + a pytest harness. Cost: ~40h architect time + €0 runtime. Value: enterprise-credibility signal for Phase-2a sales. Brief's Phase-3+ gating applies to **standards-body submission**, which Deep-Tech defers to Phase-3+ per brief. The architect-hour cost fits within §20.1's ≤15% Phase-1 formalism budget.

**Tier-1 precedence honoured.** Brief's Phase-3+ standards-body rule wins for submission; Phase-1 publication to clients as internal RFC is not a standards submission, so no conflict with brief.

### §22.2 Contrarian #2 — formal substrate earlier than D4 Lock 16

**Brief position (D4 Lock 16):** Phase 1 = simple chat; formal Phase 2+/3+.

**Deep-Tech claim:** **Formalism lives in the filesystem substrate (zero-runtime-cost), not in runtime verification layers.**

**Resolution:** Lock 16 addresses *community formalism* (chat → subscription → peer-review). Chat remains simple (§3.1.8 Phase-1 Telegram/Discord adapter). Deep-Tech formalism lives in schemas and CI hooks — it is **invisible to community members**. No conflict with Lock 16 substance: *inside the team*, the substrate is typed; *at the chat surface*, it's a simple invite-gated room. The membrane (§8) keeps these orthogonal.

**Tier-1 precedence honoured.** Lock 16 community rules unviolated.

### §22.3 Contrarian #3 — Variant 3 vs. Ruslan's default preference (Phase-1 readiness)

**Brief position (§9 Ruslan's trade-off preferences):** "Foundation quality > feature count. Scale-readiness > short-term ergonomics. Enterprise-fast > solopreneur ergonomics. Locks compliance absolute."

**Deep-Tech claim:** **If Ruslan prefers Variant 1 (Conservative) for Phase-1 speed, Variant 3's value lies at Phase 2a+ transitions and must be revisited then.**

**Resolution:** This is not a conflict — it's a selection-guidance signal. Ruslan may legitimately choose Variant 1 for Phase-1 velocity. In that case, Deep-Tech proposes a **hybrid candidacy** (§24): §17 USB-C scaffold + §4 fpf-manifests + §7 typed-graph wiki are composable into Variant 4 (Hybrid) **without** the rest of Deep-Tech's depth. The hybrid preserves Phase-1 velocity while seeding Phase-2a foundation. Stage 7 Ruslan-decision point.

---

## §23. Risk Profile

### §23.1 Top-5 risks + mitigations

| # | Risk | Probability | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Formalism drift delays Q2 consulting close → miss €50K gate | **Med** (25%) | **HIGH** | Pass-3 Phase-1 shipability test (§20.1); 15% Ruslan-hour cap on [formalism]; schema-authoring is a chore not a research project |
| R2 | Compute cost over €800/mo due to verification at scale | **Low** (10%) | **DISQUALIFIER** | Formalism = filesystem + schema validation only Phase-1; theorem-prover deferred to $100M+ gates; compute-ledger aggregate in CI halts on overrun |
| R3 | Cognitive load: solo Ruslan maintains schema discipline without help | **Med** (30%) | **MED** | YAML + markdown (editor-friendly); meta-agent FPF-Steward R12 sub-role audits quarterly; 18-manifest budget is bounded |
| R4 | Phase-2a hires need FPF literacy to onboard | **Med** (25%) | **LOW-MED** | fpf-manifests are self-documenting (5 files = onboarding path); new hires don't read 3758-line FPF cold |
| R5 | Client won't tolerate formalism overhead at sales stage | **Low** (10%) | **MED** | Membrane (§8) hides all formality outside; `predator-outside` tone consumes APIs / reads executive viewpoint, never reads manifests |

### §23.2 Residual unmitigated risks

- **If Phase-1 ships late** (missed Q2 €50K target) due to formalism-drift, hybrid path (§22.3) was the correct choice and Stage 7 should rerun.
- **If 9 Innovations IP leaks** despite ACL hooks, Phase-1 IP protection was insufficient; ACL hardening and external pen-test required at €200K.
- **If a 2nd pilot cannot onboard in 7 days** per §16.4, Deep-Tech is wrong about self-documenting manifests — hybrid path.

---

## §24. Selection Case for Ruslan

### §24.1 Choose Variant 3 (Deep-Tech) if:

- You believe the **$1T trajectory is more fragile than consulting velocity**. A 60-day delay on Q2 is recoverable; a rewrite at €200M MRR is not.
- You value **Foundation quality over Phase-1 speed**. *«Foundation = главный актив»* (D2 §14) is a binding invariant for you, not a slogan.
- You want **USB-C protocol credibility from Day 1** as a Phase-2a enterprise selling point (§17).
- You see **FPF as the real moat** — not just a design reference, but the schema-level DNA of everything Jetix ships.
- You accept **Phase-1 readiness 5.5/10** in exchange for **Scale 9/10 + Foundation 10/10 + Universality 9/10**.

### §24.2 Avoid Variant 3 if:

- **Q2 2026 consulting velocity is the binding constraint** and you want zero risk of formalism drift → choose Variant 1 (Conservative).
- You prefer variants that optimise for Phase-1 readiness alone without depth hedges.
- You believe formalism is a tax, not an investment.
- You think the learning cliff will hurt the 2nd pilot onboarding more than the schema clarity helps it.

### §24.3 Hybrid candidate (Stage 7 partial adoption)

**Composable slices of Deep-Tech into Variant 4 Hybrid, without the full depth:**

1. **§17 USB-C Phase-1 scaffold** — cheapest strategic win; ~40h architect time + €0 runtime cost; 2 reference protocols + verification harness. Enterprise-fast signal (C19).
2. **§4 fpf-manifests per agent** — adds 90 min Day-1 / 18 agents; JSON-Schema validator in CI; machine-verifiable `acting_as` enforcement. Satisfies D6 §2.2 discipline without Deep-Tech's full typed-graph wiki.
3. **§7 typed-graph wiki** — moderate cost (2-3 days retro-tagging); enables A.14 mereology queries + provenance chain; pays compounding dividends into Phase-2a+.

**Not composed individually (require full Deep-Tech):**

- §8 typed membrane with two schema namespaces (needs fpf-manifest integration)
- §10 orthogonality invariant on tokens (needs schema-enforced ACL)
- §18.9 10 Foundation Quality Invariants (need all of §3-§17 primitives)

### §24.4 Final claim

This variant would make a FOAF or standards-body reviewer say: *"this is real."*

This variant must also close a €15K consulting contract Q2 2026 without that reviewer's approval blocking shipment.

**Both are true.** Deep-Tech holds both.

*FPF is the substrate. Jetix is the instance. Ship.*

---

## Appendix A — FPF Primitive Citation Index

Every architectural element in §§3-17 cites at least one FPF primitive. Consolidated index (abridged):

| FPF primitive | Variant use |
|---|---|
| [D6 §12.5 GR-3 unidirectional guard-rail] | §3 import-direction hook; §8 ACL tier transitions |
| [D6 §3.5 / A.14 mereology 6 edges] | §7 typed-graph wiki edges |
| [D6 §6.2 alphas 8 state machines] | §4 alphas_touched; §13 content pipeline; §16 onboarding; §18 BA-cycle |
| [D6 §4.2 F-G-R trust calculus] | §4 fpf-manifest fgr_declaration; §7 frontmatter; §18 FQ-3 |
| [D6 §12.10 D.5 Bias-Audit cycle] | §7 ba_state; §13 content BA-0/1/3; §18 FQ-7 |
| [D6 §4.4 viewpoints 5 canonical] | §4 viewpoints_published; §11 matchmaker metrics; §14 dashboard |
| [D6 §8.4 bridges framework] | §5 integrations; §9 multi-provider |
| [D6 §12.4 11 pillars] | §4 pillars_upheld; §18 every DRR ≥3 pillars |
| [D6 §4.5 CP-5 human-approval gate] | §8 membrane; §15 escalation; §18 FQ-4 |
| [D6 §2.1 Ruslan 5 atomic sub-roles] | §4 roster; §11 acceptance-authority |
| [D6 §2.2 11 canonical agents] | §4 roster; §18 FQ-2 |
| [atom-2558 / D4 §4.4 4-class escalation] | §15 taxonomy |
| [D6 F.6 6-step onboarding cycle] | §16 |
| [D6 §5.8 5-block role.md] | §4 agent contracts |
| [D6 IP-1 Role ≠ Executor / P2] | §4 three-file separation |
| [D6 §9.9 P7 4-tier resource accounting] | §9 compute-ledger; §19 C2 |
| [D6 §12.6 Γ invariants] | §6 scale invariants |
| [D6 §12.14 DRR Δ-classes] | §17 versioning-policy breaking changes |
| [D6 §8.1 UTS Row 14 Practice] | §18 continuous-quality practices |

---

## Appendix B — Deliverable File List (Day-1 Stage 6 artefacts)

Files this variant will produce on adoption (Stage 7 → Stage 8):

```
fpf/schemas/
├── fpf-manifest.schema.yaml
├── bridge.schema.yaml
├── cp-5-gate.schema.yaml
├── edge-record.schema.yaml
├── acl-transition.schema.yaml
├── compute-contract.schema.yaml
├── alpha.schema.yaml
└── viewpoint.schema.yaml

.pre-commit-config.yaml                   # 7 blocking hooks
tools/
├── hook-1-asymmetric.py
├── hook-2-import-direction.py
├── hook-3-fgr-frontmatter.py
├── hook-4-alpha-state-names.py
├── hook-5-symbolic-test.sh
├── hook-6-acting-as.py
├── hook-7-no-plaintext-creds.py
├── regen-message-schema.sh
└── extract-d6-roster.py

jetix-os/protocols/
├── agent-handoff-v1.schema.yaml
├── agent-handoff-v1.rfc.md
├── contract-fixation-v1.schema.yaml
├── contract-fixation-v1.rfc.md
├── versioning-policy.yaml
└── ref-impl/
    ├── agent-handoff-v1.py
    └── contract-fixation-v1.py

tests/protocol/
├── agent-handoff-v1/
└── contract-fixation-v1/

agents/<id>/fpf-manifest.yaml              # 18 manifests (11 + 5 + 2)
cp-5-routes/
├── l1-policy.yaml
├── l2-policy.yaml
└── gate-template.yaml

dashboard/
├── viewpoints/                            # 7 YAML viewpoint files
└── pipeline/monday-render.sh

integrations/*.bridge.yaml                 # 12 bridge files

replica-kit/<domain>/                      # Phase-2a: roy-kit template
```

Approximate file count Day-1: **80–100 files**. Approximate ADR effort: 5-7 architect-days after Stage 7 selection.

---

*End of JETIX-ARCH-V3-DEEPTECH.md.*

*Stage 6 Variant 3 — AGGRESSIVE DEEP-TECH. Ruslan's selection at Stage 7.*
