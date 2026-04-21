---
id: jetix-arch-v2-maximalist
title: JETIX-ARCH-V2-MAXIMALIST — Stage 6 Variant 2 (Aggressive Maximalist)
variant: 2
variant-name: AGGRESSIVE-MAXIMALIST
character-tags: [maximalist, phase3-day1, upfront-investment, scaffolded-future, schema-heavy-runtime-light]
date: 2026-04-22
stage: 6
status: draft
binding: false
depends_on:
  - decisions/JETIX-VISION.md (D1 APPROVED)
  - decisions/JETIX-PHILOSOPHY.md (D2 APPROVED)
  - decisions/JETIX-PLAN.md (D3 APPROVED)
  - decisions/JETIX-ARCHITECTURE-BRIEF.md (D4 APPROVED 2026-04-21)
  - decisions/STAGE-3-APPROVAL.md
  - decisions/STAGE-4-APPROVAL.md
  - design/JETIX-FPF.md (D6)
  - decisions/2026-04-19-architecture-v2-approval.md (ADR Chunks 1-8)
formality: F2
reliability: R-medium
claim-scope: jetix-stage-6-variant-2
axis-profile: scale=9 / foundation=9 / innovation=8 / phase1=6.5 / ops-simplicity=5
position: upper-bound corner of variant-space (maximalist axis)
---

# Stage 6 Variant 2 — AGGRESSIVE-MAXIMALIST

**One-line thesis.** Build for Phase 3 from Day 1 — schema-heavy, runtime-light: every Phase 2/3
capability gets a designed home in Phase 1 (directory, schema, role-manifest, spec), but only the
11 canonical Phase-1 agents burn compute. Lock 19's $1T trajectory is a design-time invariant;
Lock 15's €800/mo gate is preserved because schemas cost nothing to scaffold.

---

## §1. Executive Summary

The Maximalist variant answers all 15 Stage-6 architect questions under one organising
hypothesis: *capabilities not scaffolded in the founding architecture accumulate as
retrofitting debt that compounds exponentially at each revenue gate.* Conservative reads Lock
15 as "build only what Phase 1 runs"; Maximalist reads Lock 15 (revenue-gated *spend*) and
Lock 19 (no-rewrite $1T trajectory) jointly and concludes **compute-spend is gated; design-
surface is not**. That distinction is the central design move.

Concretely: Phase 1 runs only the 11 canonical agents per C14 / D6 §2.2. Everything else —
2 Phase-2a stubs, 5 Ruslan atomic sub-roles, 5 designed-dormant Phase-3 role-manifests, token-
economy state machine, matchmaker 4-module skeleton, Roy-Replication kit template, full USB-C
protocol taxonomy + verification harness spec, dashboard v1+v2+v3 schema, open-research
pipeline, federation namespace — exists Day 1 as specs, schemas, `_status.md` activation gates
and reference-implementation skeletons. Nothing routes traffic; all has a designed home. Zero
revenue-gate transition requires architectural rewrite.

**The €800/mo defense (§8.3 disqualifier).** Phase-1 projected burn = €320-520/mo steady-state
(§9 Q7 calc), inside the band. The discipline: (1) schemas don't call LLMs; (2) dormant
manifests are files, not processes; (3) compute-contract routes Day-1 traffic to cheapest
viable tier; (4) compute-ledger hard-block (§9.4) enforces €800/mo at the ledger layer. The
defense is instrumentation, not optimism.

**Five most distinctive choices vs. Conservative.**

1. **Role-manifest layer from Day 1** — 11 runtime agents + 12 dormant/assumed manifests = 23
   designed roles; C14 preserved (enum=11); scale trajectory pre-wired.
2. **Multi-provider Day 1** (Anthropic + OpenAI + Google) at the compute-contract layer;
   AP-11 avoidance by construction.
3. **Wiki full 9 entity types + atoms registry + F-G-R + 8 Alphas + typed edges Day 1** —
   retrofitting entity taxonomy across 10⁴ claims is the Lock-19 disaster.
4. **USB-C protocol layer complete spec Day 1** — message schemas, verification predicates,
   reference-implementation skeleton, draft standards-body submission on ice. Phase 2+
   activation is publication, not invention.
5. **Dashboard v1 + v2 + v3 scaffolded Day 1** — v1 metrics live; v2/v3 schemas produce empty
   datasets waiting for data. Schema roy-level-compatible without migration.

Self-score profile: Phase-1 readiness 6.5/10, Scale trajectory 9, Foundation quality 9, Locks
compliance 9, Operational simplicity 5, Innovation 8. Weighted total ~76/100 (§21). No axis
below §8.3 hard floor of 3.

---

## §2. Variant Character Statement

The Maximalist variant occupies the **upper-bound corner** of the variant-space. Its charter
is not to be correct in all futures but to stake out the furthest defensible position under
*"Foundation = главный актив"* (D2 §14) so Stage 7 has a real maximum to measure against. If
the chosen Stage 7 variant ends up at a weighted average of several, the Maximalist's job is
to be a **coherent, self-consistent upper endpoint** — not a compromise.

### 2.1 Philosophical lens

D2 §14 states: *"Главный актив — не Руслан, не агенты, не заказчики. Главный актив —
инфраструктурный слой: protocols, contracts, память, evals, логи, метрики качества, резервные
маршруты."* This variant treats that as design-time authorization to **over-invest in the
Foundation layer relative to a conservative reading of Lock 15**. D2 §6's *"Continuous, every
iteration — NOT periodic"* requires instrumentation in place before the first iteration that
would be measured — Day 1 complete, not Day-N-when-we-need-it. Combined with Lock 19 + D2
§14's *"Quality cannot be retrofit at $1T scale"*, one design rule falls out: **anything that
would have to be retrofitted later under load gets scaffolded now under no load.**

### 2.2 The maximalism / frugality paradox

Lock 15 is revenue-gated spend; §8.3 makes €800/mo a hard disqualifier. "Maximalism" sounds
like it necessarily breaches the gate. The resolution is linguistic-precise: the gate is on
**compute spend**; maximalism here is about **design surface**. Files, directories, schemas,
spec documents, role-manifests and reference-implementation skeletons with no live execution
path consume ~€0/mo of LLM compute. The variant is therefore *schema-heavy, runtime-light* —
the discipline that makes it Lock-15 compliant.

### 2.3 What this variant will not do

Not violate C14 (11-agent canonical runtime stands). Not invent new locks / constraints /
anti-patterns (D4 §6-§7 binding; tensions documented in §22 as observations, not fixes). Not
exceed €800/mo Phase-1 burn (§9 defence). Not write code beyond schema/tree illustrations. Not
copy the Conservative voice — if a paragraph could also appear there unchanged, it wastes the
corner.

### 2.4 Ruslan-voice anchors

1. *"Foundation = главный актив"* (D2 §14) — licence for over-investment (§18).
2. *"AI = electricity"* (D2 §7) — licence for multi-provider Day 1 (§5, §9, §20).
3. *"Notion loss recoverable in 1 day, wiki loss = Jetix loss"* (D2 §14) — licence for
   filesystem-first + wiki-full-9-types (§7, §18).
4. *"самый глубокий вариант… на максималку"* (Stage 5 voice) — what the Maximalist obeys.

---

## §3. Answer to Q1 — Repository Layout

**Problem restated (D4 §10 Q1).** Propose a concrete folder tree for `jetix-os/` (universal
base) + `jetix-company/` (overlay), enforce cross-dir import policy, show migration to
Phase-2a MHT-1 extraction, and satisfy Symbolic D-test (§5.5: `grep base/ -rn "Jetix|DACH|AI
consulting|Mittelstand"` returns 0).

### 3.1 Top-level tree (Day 1)

The Maximalist layout makes **every Phase 2/3 capability a Day-1 top-level folder** populated
with `spec.md` + `schema.json` + `README.md` + `_status.md` (activation-gate file). Most folders
are dormant; all are designed.

```
jetix-os/                           # universal base (D-test: 0 Jetix strings)
├── base/                            # hard-core universal primitives
│   ├── agents/                      # role.md + executor-binding.yaml templates
│   ├── contracts/                   # FPF contract schemas
│   ├── handoff/                     # message schemas + acting_as
│   ├── escalation/                  # 4-class routing rules
│   ├── quality/                     # F-G-R + continuous-quality metrics
│   ├── dashboard/                   # v1/v2/v3 metric schemas
│   ├── reserve-routes/              # multi-provider fallback spec
│   ├── compute-contract/            # provider-neutral interface
│   ├── membrane/                    # 4-tier ACL primitives
│   ├── wiki/                        # 9 entity types + atoms + edges
│   └── protocols/                   # USB-C spec + harness skeleton (dormant)
├── protocols/                       # Phase-2+/3+ USB-C suite (dormant)
│   ├── standards-draft/             # draft submission documents
│   ├── verification-harness/        # reference implementation skeleton
│   ├── intake/ handoff/ escalation/ reporting/ contracting/ audit/
│   └── _status.md                   # activation: €200K gate
├── matchmaker/                      # Phase-2+ engine (dormant schemas)
│   ├── algorithm/ quality-gate/ contract/ metrics/
│   └── _status.md                   # activation: €200K gate
├── roy-kit/                         # Phase-2+ replication kit (dormant)
│   ├── export-manifest/ kit-template/ replication-assessment/
│   └── _status.md                   # activation: €1M gate + Ruslan sign-off
├── token-economy/                   # Phase-2+ / Phase-3+ (dormant)
│   ├── state-machine/ ledger-schema/ rights-separation/
│   └── _status.md                   # activation: $100K self-earned
├── federation/                      # Phase-3+ holding (dormant)
│   └── _status.md                   # activation: 2nd-entity emergence (MHT-3)
├── licensing/                       # Phase-2+ patents + DPA (stubbed)
├── open-research/                   # Phase-2+ publication pipeline (dormant)
└── _templates/                      # spec.md / schema.json / role.md templates

jetix-company/                       # overlay (Jetix-specific instantiation)
├── icp/                             # 11 archetypes × 5 criteria
├── content/                         # pain-primary TOF, archetype-keyed renders
├── sales/                           # consulting pipeline DACH-aware
├── legal/                           # GmbH, DPA, EU AI Act
├── finance/                         # Stripe + Wise + compute-ledger
├── agents/                          # instantiated agent configs
├── entities/                        # jetix-gmbh namespace
└── decisions/                       # ADRs + DRRs + approvals

life-os/                             # physical separation Day 1 (C15)
└── ... (Hook 1: Jetix → Life-OS BLOCKED)
```

### 3.2 Dormant-scaffold activation discipline

Each dormant top-level folder has a mandatory `_status.md`:

```yaml
---
status: dormant | stub | active
activation_gate: €200K | €1M | MHT-3 | $100K self-earned
activation_criteria:
  - concrete measurable trigger
  - secondary trigger
owner: manager | Ruslan acceptance-authority
dependencies:
  - other folder activation required first
cost_to_activate_estimate: €X or N developer-days
---
```

This metadata is **queried by the compute-contract ledger**: any agent call routed to a
`status: dormant` capability is blocked at the protocol layer. This is the technical
enforcement of "scaffolded ≠ running" that protects the €800/mo gate.

### 3.3 Base/overlay separation (Lock 9 universality, D2 §10)

- **Symbolic D-test (§5.5) applied to `base/` subtree only.** CI hook:
  `grep -rn 'Jetix\|DACH\|AI consulting\|Mittelstand\|GmbH\|Ruslan' base/` returns 0 or
  commit blocked. Names in `base/` are Greek-letter or role-typed (`l0-executive`,
  `l1-foundation`, `l2-cognitive`). Overlay may contain any of these terms freely.
- **B-test (configurability):** ≥90% of `base/` design choices are parameter-driven from
  `jetix-company/config.yaml`. CI audits quarterly.
- **C-test (multi-use-case):** `base/` supports ≥3 non-Jetix instantiation templates
  (astronomer, husbandry, 3rd TBD) in `jetix-os/_templates/use-case-dry-runs/`.

### 3.4 Cross-directory import policy

- `jetix-company/` MAY import from `jetix-os/base/`. Unidirectional.
- `jetix-os/base/` MAY NOT import from `jetix-company/`. Pre-commit Hook 2 blocks.
- `life-os/` MAY NOT reference `jetix-os/` or `jetix-company/`. Hook 1 blocks.
- `jetix-os/<dormant-folder>/` MAY import from `jetix-os/base/` only. No cross-dormant imports.

### 3.5 Migration to Phase-2a MHT-1 extraction

At Triple-AND trigger (C15 MHT-1: ≥€20K MRR × 3mo + Ruslan >40% L1/L2 + ≥1 GDPR DPA
client), `life-os/` is extracted via `git filter-repo` to a separate repository. Because Hook 1
has prevented any asymmetric reference in either direction Day 1, the extraction is
mechanical: all history stays with Life-OS, no Jetix data leaks, no migration code to write.
This is the Maximalist move: scaffold the **repository boundary** before you need it, so the
separation is free when triggered.

### 3.6 Pre-commit configuration snippet

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: hook-1-asymmetric-ref
        entry: tools/hooks/hook_1_asymmetric_ref.py
        files: '^jetix-(os|company)/'
        types: [markdown, yaml]
      - id: hook-2-base-no-company
        entry: tools/hooks/hook_2_base_no_company.py
        files: '^jetix-os/base/'
      - id: hook-3-dormant-runtime-block
        entry: tools/hooks/hook_3_dormant.py
        files: '^jetix-os/(protocols|matchmaker|roy-kit|token-economy|federation|open-research)/'
      - id: hook-4-symbolic-d-test
        entry: tools/hooks/hook_4_symbolic.py
        files: '^jetix-os/base/'
      - id: hook-5-frontmatter-fgr
        entry: tools/hooks/hook_5_fgr.py
        files: '\.md$'
```

### 3.7 Rationale per dormant directory

`protocols/` (Lock 20 + Q15 signature): USB-C standards leadership takes 18-36 months
draft-to-adoption; if draft isn't in-repo Day 1, Phase-3 claim is hollow. `matchmaker/`
(Lock 21): 4-module schema drift is exactly the retrofit disaster Lock 19 forbids.
`roy-kit/` (Locks 21+24): export-manifest schema breakage at fork-N is unforgiveable.
`token-economy/` (Lock 23): Option B rights-separation must be right at issuance-1.
`federation/` (Lock 19): inter-entity namespace DNS costly to retrofit post-2nd-entity.
`open-research/` (Lock 24): publication-pipeline guardrails need wiring before first paper.

### 3.8 Why not Conservative layout

A Conservative variant would create `jetix-os/base/` + `jetix-company/` Phase 1, activating
Phase-2+ directories at their gates. Maximalist argues: directories are free (0 compute),
`_status.md` + `spec.md` files serve as architectural anchor + documentation, and when Phase 2
hits the team adds content to existing folders rather than arguing layout under revenue-gate
time pressure. Cost: cognitive load (§23 Risk 4). Benefit: zero-rewrite per gate (Lock 19).

---

## §4. Answer to Q2 — Agent Roster

**Problem restated (D4 §10 Q2).** Final roster table reconciling CLAUDE.md drift (12 vs
canonical 11), with 5 Ruslan atomic sub-roles and 2 Phase-2a stubs, `message.schema.json` enum
regeneration, and FPF IP-1 (Role ≠ Executor) preserved.

### 4.1 The central C14 puzzle

C14 says **11 canonical Phase-1 runtime agents** per D6 §2.2. Maximalist must expand design
surface without crossing the line. Solution: **three-layer taxonomy**.

1. **Runtime agents (N=11)** — compile to running processes Day 1.
2. **Activated role-manifests (N=2)** — specs whose responsibilities `manager` assumes until
   gate trips: `dpo` + `customer-success` (Phase-2a stubs).
3. **Designed-dormant role-manifests (N=10)** — 5 Ruslan atomic sub-roles + 5 Phase-3 designed
   roles.

"Designed roles" total = 23; "Day-1 runtime agents" = 11. C14 verification: (1)
`message.schema.json` enum = 11 agent IDs; (2) `agents/active/` = 11 sub-dirs; (3) the other
12 manifests live in `roles/` with `executor: null` or `executor: ruslan` explicit.

### 4.2 Runtime roster table (Day 1, per FPF §2.2 + D4 §4.1)

| # | Agent ID | Model | Dept | Phase | J-level | Notes |
|---|---|---|---|---|---|---|
| 1 | `manager` | Sonnet 4.6 | MGMT | 1 | J-Approve | ≤20 active tasks hard-block |
| 2 | `personal-assistant` | Haiku 4.5 | OPS | 1 | J-Auto | founder cal/inbox |
| 3 | `system-admin` | Haiku 4.5 | OPS | 1 | J-Auto/Approve | spend>€50 escalates |
| 4 | `sales-lead` | Sonnet 4.6 | Sales | 2 | J-Approve | manifest Day 1 |
| 5 | `sales-research` | Haiku 4.5 | Sales | 2 | J-Auto | renamed from `sales-researcher` |
| 6 | `sales-outreach` | Haiku 4.5 | Sales | 2 | J-Auto | 100% pre-research |
| 7 | `inbox-processor` | Haiku 4.5 | Brain | 2 | J-Auto | voice-memo pipeline |
| 8 | `crazy-agent` | Sonnet 4.6 | Meta | 2 | J2 brainstorm | generative-only |
| 9 | `knowledge-synth` | Sonnet 4.6 | Brain | 3 | J-Approve | E.2 ≥3 pillars |
| 10 | `strategy-support-analyst` | Opus 4.6 | MGMT | 3 | J-Strategic-support | NEVER decides; renamed from `strategist` |
| 11 | `meta-agent` | Sonnet 4.6 | Meta | 4 | J-Approve | FPF-Steward sub-role |

**Phase labelling note.** Agents labelled Phase 2/3/4 have `role.md` + `executor-binding.yaml`
present Day 1 but `status: activation_gated`. FPF contracts fully specified Day 1 (C11);
mailbox messages blocked until gate. `manager` handles their queue meanwhile. C14 compliance:
a gated agent is not "runtime" (process not running, not in `agents/active/`).

### 4.3 `life-coach` migration (C14 compliance, C15 Life-OS separation)

`life-coach` is NOT in the Jetix roster. Per C14 + C15, it migrates to `life-os/agents/life-coach/`
Day 1. The old `agents/life-coach/` directory, if present, is **deleted or moved** at repo init
(rather than left as dead weight). `shared/schemas/message.schema.json` enum excludes it.

### 4.4 Activated role-manifests (N=2, Phase-2a stubs, Day 1 as specs)

These two are full `role.md` files Day 1 with `executor: manager` (i.e., `manager` currently
executes their responsibilities). At Phase-2a Triple-AND trigger (§6 C15), `executor` updates
to a new agent instance and they become runtime agents 12 and 13.

| Manifest | Phase-2a trigger | Current executor | Post-trigger |
|---|---|---|---|
| `dpo` (external-executor) | GDPR Art.22 + EU AI Act Art.14 binding (≥1 GDPR DPA client) | external lawyer + `manager` proxy | dedicated `dpo` agent instance + external-executor lawyer |
| `customer-success` (J2) | 3+ retainer clients OR >€20K MRR | `manager` + `sales-lead` (mfst only Phase 2) | dedicated `customer-success` agent instance |

### 4.5 Ruslan atomic sub-roles (5 role-manifests, `executor: ruslan`, never agents)

Per FPF §2.1a + IP-1 (role ≠ executor) + the "left-hand rule" (strategy-lead wins on conflict):

| Sub-role | Manifest path | Authority domain | Never-delegate trigger |
|---|---|---|---|
| `strategy-lead` | `roles/l0-executive/strategy-lead/` | Стратегия (D1 §3 non-delegatable #1) | all strategic decisions |
| `framing-lead` | `roles/l0-executive/framing-lead/` | Вкус (#2) + Layered-identity (Lock 8) | every new frame/face render |
| `sales-closer` | `roles/l0-executive/sales-closer/` | Отношения (#6) on client close | Audit-SKU proposal sign-off |
| `acceptance-authority` | `roles/l0-executive/acceptance-authority/` | Утверждение (#4) + Ответственность (#3) | deliverable sign-off |
| `external-relations` | `roles/l0-executive/external-relations/` | Отношения (#6) outside membrane | partner/press/investor touch |

`executor-binding.yaml` for all five has `executor: ruslan` and supports **multi-role
enumeration** on a single human executor — Ruslan may carry multiple manifests simultaneously,
with `acting_as:` in message headers disambiguating which manifest is in effect. Q2 asks for
the mechanism: Maximalist picks explicit `acting_as` field in the message schema (not implicit
thread-local) because explicit is audit-visible and the audit trail (§15) needs it.

### 4.6 Designed-dormant Phase-3 role-manifests (N=5, activation-gated)

These are the signature Maximalist move: 5 Phase-3 responsibilities that get a `role.md` Day 1
with `executor: null, status: designed-dormant, activation_gate: <criterion>`. The manifests
are not agents and do not consume compute. They serve three purposes: (1) documentation of what
the Phase-3 organisation looks like so Phase-1 choices don't accidentally foreclose them;
(2) a place to write things down as insights accumulate; (3) zero-rewrite activation at gate.

| Manifest | Phase-3 activation gate | Responsibility summary |
|---|---|---|
| `token-economy-operator` | $100K self-earned | Token ledger ops; rights-separation enforcement (C21) |
| `federation-liaison` | 2nd-entity emergence (MHT-3) | Inter-entity coordination (D3 §6.2) |
| `matchmaker-curator` | €200K + ≥10 active specialists | Human-in-loop match quality, C20 criteria |
| `protocol-standards-editor` | ≥1 external protocol implementer | USB-C standards-body liaison (Q15) |
| `roy-kit-packager` | €1M + 1st external roy candidate | Export-manifest production (Q10) |

### 4.7 `message.schema.json` enum and Day-1 blocker

Per D4 §4.1 (blocker): `shared/schemas/message.schema.json` agent-ID enum regenerates from
D6 §2.2 table Day 1. The Maximalist repo ships with a Day-1 CI hook (`hook-6-schema-enum`) that
regenerates the enum from `agents/active/*/role.md` on every PR and fails if drift is detected.
This closes the CLAUDE.md-drift class of defect at the schema layer rather than by convention.

### 4.8 Three-way diff verification

Q2 quality-criterion: CLAUDE.md table ≡ D6 §2.2 table ≡ schema enum (3-way diff = 0). CI runs
`tools/diff_rosters.py` on every PR; mismatch blocks merge. This is the enforcement of
*"filesystem = single source of truth"* (Lock 17, C4) at the roster level.

### 4.9 Why this is "maximalist but C14-compliant"

Conservative: 11 runtime + parking lot. Maximalist: 11 runtime + 12 fully-specified dormant/
assumed role-manifests with explicit activation gates. Both obey C14 (enum = 11). Maximalist's
advantage: when Phase-2a activates `dpo`, the only change is `executor-binding.status: active`.
No `role.md` to write, no escalation routing to retrofit, no 4-class table to redraw. Lock 19
payoff made concrete.

---

## §5. Answer to Q3 — Integration Points

**Problem restated (D4 §10 Q3).** Inventory the ~12 Phase-1 external systems with direction
(R/W), auth, fallback, gate, DPA/GDPR impact, SOPS secret-vault path. Consulting-to-cash
sequence diagram. 100% have fallback + owner + secret-store.

### 5.1 Integration inventory table (Day 1)

| # | System | Direction | Auth | Primary | Fallback | Gate | DPA/GDPR | Secret-vault |
|---|---|---|---|---|---|---|---|---|
| 1 | Anthropic Claude API | W→R | API-key | Opus 4.7 1M / Sonnet 4.6 / Haiku 4.5 | OpenAI GPT tier | always | DPA signed | `sops://llm/anthropic` |
| 2 | OpenAI API | W→R | API-key | GPT-4.x (fallback) | Google Gemini | always | DPA signed | `sops://llm/openai` |
| 3 | Google Gemini API | W→R | OAuth2 | (fallback only) | — | always | DPA | `sops://llm/google` |
| 4 | Stripe | W→R, R→W | API-key | Stripe Checkout + Invoices | manual Wise fallback | €50K GmbH | EU DPA | `sops://pay/stripe` |
| 5 | Wise | W→R, R→W | API-key | FX + int'l receipts | manual bank wire | always | EU DPA | `sops://pay/wise` |
| 6 | Notion | W→R only | int-token | one-way fs→Notion sync | read-from-git | always | DPA + scope:jetix | `sops://obs/notion` |
| 7 | Telegram Bot API | W→R, R→W | bot-token | outbound notifications + 2-way chat | Discord fallback | always | no PII; DPA | `sops://comms/telegram` |
| 8 | Discord | W→R | bot-token | community adapter | Telegram fallback | Phase 2+ | DPA | `sops://comms/discord` |
| 9 | Gmail API | W→R, R→W | OAuth2 | inbox-processor ingest | IMAP+SMTP fallback | always | DPA | `sops://email/gmail` |
| 10 | Google Calendar | W→R | OAuth2 | personal-assistant | ICS+manual | always | DPA | `sops://cal/google` |
| 11 | Groq Whisper (STT) | W→R | API-key | voice-memo transcribe | OpenAI Whisper | always | DPA + no-store | `sops://stt/groq` |
| 12 | GitHub | R↔W | SSH+token | repo origin | GitLab mirror | always | DPA (code, not client PII) | `sops://vcs/github` |
| 13 | Healthchecks.io | W→R | token | uptime alerts | sentry + cron-mail | always | — (no PII) | `sops://obs/hc` |

Every row has a named fallback (C4.8 / AP-11 avoidance). Zero plaintext credentials: SOPS +
1-key envelope encryption (per C15).

### 5.2 Consulting-to-cash sequence

```
[Lead] → inbox-processor (Gmail) → ICP classifier → sales-lead (J-Approve SKU)
       → Audit-SKU proposal (5-view Viewpoint Bundle, C.22) → sales-closer sign-off
       → Stripe invoice + Wise FX → compute-ledger revenue event
       → Producer-Center 5-stage delivery (BA-0/1/3) → acceptance-authority sign-off
       → Stripe recurring retainer → Notion view (one-way sync) → dashboard v1
```

Each arrow is a `comms/mailboxes/*.jsonl` message with `acting_as`, F-G-R frontmatter, audit hash.

### 5.3 Fallback discipline (AP-11 avoidance)

Every integration carries `fallback_chain:` in `executor-binding.yaml` (e.g. sales-outreach:
`provider_preference: [anthropic/haiku-4.5, openai/gpt-4o-mini, google/gemini-flash]`,
`fallback_on: [rate_limit, 5xx, timeout>30s]`, circuit-breaker: 3 failures in 10min → Tier-3
pause, `cost_ceiling_per_turn_eur: 0.02`). Quarterly chaos drill: "Anthropic down" +
independent Stripe/email/telegram drills. Tier-1 must switch provider; Tier-3 may pause.
Runbook: `ops/playbooks/` (MC1 P1-#4).

### 5.4 Why multi-provider Day 1

*"AI = electricity"* (D2 §7). You would not wire a building with a single breaker and plan to
add a second after move-in. AP-11 disqualifies single-provider architectures. Maximalist reads
Lock 20 + §4.8 as "all three available at the adapter layer Day 1, routing policy decides
which per-tier". Cost impact: ~€0 Phase 1 (adapters don't call in steady state).

---

## §6. Answer to Q4 — Scaling Mechanism

**Problem restated (D4 §10 Q4).** 10× at each gate with <30% subsystem-LOC refactor. Per-
subsystem scale-path table. Sharding key per data class. Rewrite risks + pre-mitigation. Load
projections.

### 6.1 Scale trajectory table

Gates: $0 → $20-30K → €50K → €200K → €1M → €1M+ → $100M → $100B → $1T (D19 ambition).
Measured deltas in # of entities the schema must accommodate:

| Subsystem | Ph1 | Ph2a | Ph2b | Ph3 | Ph3+ | Sharding key | Pre-designed extension |
|---|---|---|---|---|---|---|---|
| Wiki (claims) | 10² | 10³ | 10⁴ | 10⁵ | 10⁶-10⁷ | `scope:` + entity-type | typed edges + overlays |
| Agents | 11 | 13 | 20-30 | 50+ | 100s | agent-id namespace | federation tier |
| Mailbox messages | 10³/mo | 10⁴/mo | 10⁵/mo | 10⁶/mo | 10⁸/mo | `to:` + date-shard | JSONL → parquet or mqtt |
| Compute-ledger rows | 10⁴/mo | 10⁵/mo | 10⁶/mo | 10⁷/mo | 10⁹/mo | direction + date | monthly rollup tables |
| Clients/retainers | 5 | 20 | 100 | 1000 | 10K+ | entity-id | holding-federation split |
| Matchmaker pairs | 0 | 0 | 10² | 10³ | 10⁵ | archetype × direction | graph DB-ready schema |
| Token holders | 0 | 0 | 50 (internal) | 500 | 10K+ (limited public) | wallet-id | ledger shards |
| Roys | 1 | 1 | 1 | 2-3 | 10+ | roy-id namespace | inter-roy protocol |

### 6.2 Pre-designed extension points (the Maximalist signature)

Every boundary that would cost >30% LOC to retrofit gets a pre-designed extension Day 1:

1. **Role-manifest layer** — adding an agent = new sub-dir under `agents/active/` with
   `role.md` + `executor-binding.yaml`. Enum regenerated from filesystem. Refactor cost: 0%.
2. **Compute-contract layer** — adding a provider = new adapter file. Routing policy is YAML,
   not code. Cost: 0%.
3. **Wiki overlay layer** — adding a niche = new `wiki/niches/<name>/`. No migration.
4. **Membrane-tier layer** — 4 tiers Day 1; ordinal field allows insertion without rewriting ACL.
5. **Dashboard metrics** — v1/v2/v3 Day 1; adding a metric = row in `dashboard/metrics.yaml`.
6. **Mailbox format** — JSONL per-agent Day 1; migration to parquet at ~10⁵ msgs/mo is
   mechanical (schema stable); MQTT/NATS at ~10⁷. Schema-stable = 0 application-code change.

### 6.3 Rewrite-risk register (top-5)

| Risk | Impact | Pre-mitigation (Day-1) |
|---|---|---|
| Wiki entity-type schema drift | 10⁵+ claims to retrofit | 9 entity types + F-G-R + 8 Alphas Day 1 (§7) |
| Agent-ID enum drift (C14 canonical) | every message schema-invalid | CI hook-6 regenerates enum from filesystem |
| Compute-ledger schema breakage | revenue reconciliation | §4.7 + §5.6 schema locked Day 1 |
| Membrane-tier additive | ACL rewrites | ordinal-insertable tier field |
| Token-economy Option B → public tx | rights-separation retrofit | state machine Day 1 |

### 6.4 LOC-refactor budget per gate (estimate)

| Gate | Target subsystem-LOC refactor | Maximalist estimate | Conservative estimate |
|---|---|---|---|
| $20-30K | — | <5% | ~5% |
| €50K (GmbH + Stripe) | <30% | ~8% (config + overlay) | ~15% (overlay + adapters + schemas) |
| €200K (EU patents + hires) | <30% | ~12% (activate Phase-2a stubs) | ~25% (rewrite agent taxonomy) |
| €1M (5-10 team) | <30% | ~18% (federation activate) | ~35% ⚠ fails §5.1 |
| €1M+ / Phase 3 | <30% | ~22% | ~45% ⚠ fails §5.1 |

The core claim: schema-first scaffolding converts Phase-N activation from "rewrite" to
"configure + add content". A Conservative variant that treats `token-economy/`, `federation/`,
`matchmaker/` as "added at gate" risks breaching the 30% LOC ceiling at the big gates. The
Maximalist saves refactor at every gate by paying the schema cost Day 1 (€0 compute, Ruslan-
hours + knowledge-synth-hours).

### 6.5 No-boutique-shortcut audit (AP-16)

CI hook-7 hard-fails commits introducing §7 AP-16 patterns: SQLite-only core store, single-
region hardcode, `/home/ruslan/*` paths, single-user session state in core, missing sharding-
key on a 10⁶-capable data class.

---

## §7. Answer to Q5 — Data Architecture

**Problem restated (D4 §10 Q5).** 3-layer knowledge (wiki + alphas + per-agent) supporting
9 entity types + 25K HARD exocortex + Karpathy/OmegaWiki pattern. Storage layout. Ingest
pipeline v2. Search + citation. Versioning + conflict + backup.

### 7.1 Storage layout Day 1 (full fidelity per §4.5 / Area 5)

```
wiki/
├── index.md                              # catalog, regenerated by /ingest
├── log.md                                # append-only chronology
├── concepts/     entities/    sources/
├── topics/       ideas/       experiments/
├── claims/       summaries/   foundations/
├── niches/                               # 6 overlays: personal, business, sales, life, tech, meta
├── comparisons/                          # filing loop from /ask
├── atoms/                                # ATOM-REGISTRY (Day-1 schema-complete)
│   └── registry.jsonl
├── alphas/                               # L2: 8 past-participle state files per claim
│   ├── configured/ specified/ implemented/ tested/
│   └── deployed/ operated/ archived/ deprecated/
├── graph/
│   ├── edges.jsonl                       # A.14 typed mereology (6 FPF + 4 Jetix)
│   └── communities.jsonl
├── _templates/                           # 9 entity templates + atom template
└── _meta/
    ├── conventions.md
    └── pipeline-spec.md
```

Per-agent L3 memory (`agents/<id>/system.md` / `strategies.md` / `scratchpad.md` / `niche/`
symlinks) is layered on top of wiki/, not parallel. No agent has an isolated KB (C4, Lock 17).

### 7.2 Nine entity types Day 1

Per D4 §3.1.13 + §4.5: `concepts / entities / sources / topics / ideas / experiments / claims
/ summaries / foundations`. Each has a `_template.md`, frontmatter schema in
`_meta/conventions.md`, CI lint rule. Retrofitting entity taxonomy across 10⁴+ claims is the
Lock-19 disaster. Upfront cost: ~3 Ruslan-h × 9 types ≈ 27 h one-time, versus ~weeks of
retrofit at €200K.

### 7.3 Atoms registry + F-G-R Day 1

Every claim in `wiki/claims/` MUST carry F-G-R frontmatter (C13):

```yaml
---
id: claim-YYYYMMDD-NNN
formality: F0..F9
reliability: R-low | R-medium | R-high | R-certified | R-formally-proven
claim-scope: <bounded-context>
atoms:
  - atom-NNNN (primary)
  - atom-NNNN (supporting)
sources:
  - wiki/sources/<id>.md
---
```

The atoms registry (inherited from ATOM-REGISTRY.md, ~3626 atoms) is normalised to JSONL Day 1;
`atom-NNNN` IDs are stable across the system. This means every claim can cite ≥1 source
(Q5 quality-criterion) and every downstream synthesis (knowledge-synth) can traverse atoms
→ claims → sources → provenance.

### 7.4 Eight Alphas as claim-lifecycle state machine

FPF §B.3 / §6 / D4 §4.5 binds 8 past-participle alphas: `configured / specified / implemented
/ tested / deployed / operated / archived / deprecated`. Each claim has an `alpha_state:` field
and transitions are logged with a hash to `wiki/log.md`. Invalid transitions (e.g., `tested →
implemented` without a regression DRR) are blocked by CI hook-5. This is operationalised state,
not doc-only discipline.

### 7.5 Typed edges (A.14, 10 types Day 1)

`wiki/graph/edges.jsonl` carries A.14-typed mereological edges:
- **6 FPF edges**: ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf / AspectOf.
- **4 Jetix edges**: creates / operates-in / methodologically-uses / constrained-by (+ optional `fills`).

Edge schema:
```json
{"src":"claim-...","dst":"claim-...","edge":"ComponentOf","f":"F6","r":"R-high","ts":"..."}
```

Community detection (`wiki/graph/communities.jsonl`) is rebuilt by `/build-graph` skill weekly
Phase 1. Phase-2+ optionally upgrades to Neo4j / NetworkX-served.

### 7.6 Ingest pipeline v2 (raw → ingested → compiled → linted → ready)

Each file carries `pipeline:` frontmatter; transitions only via skills (`/ingest`, `/compile`,
`/lint`, `/consolidate`, `/build-graph`). Voice-memo ingestion follows the existing Groq Whisper
→ Claude structured-items → filter → review-report pipeline with the Lock 4 canonicalization
`Jackson|Джек → Jetix` applied pre-persistence at the STT-normalization step. **Distribution
to the KB is manual** (distribute.py.bak archived per CLAUDE.md) — human review mandatory.

### 7.7 Search + citation-emit

- **Primary: frontmatter + filename + tag search** via Grep on frontmatter-indexed files.
- **Secondary: full-text grep** (Ripgrep under the hood) constrained by scope tags.
- **Synthesis: /ask skill** emits citations inline `[src:filename]` + F-G-R composition.
- **Phase-2+ upgrade path**: GraphRAG (Chunk 5 Area 5 Q2 latency trigger at >3s p95) and Wiki
  hybrid retrieval. Schema is GraphRAG-ready Day 1 (node-edge structure above).

### 7.8 Versioning + conflict

Git is authoritative. Every commit = a decision (atom-2687). Concurrent edits on the same
claim: last-writer-wins with `conflict_resolution: manual-review` flag + DRR produced by
knowledge-synth. Wiki loss = Jetix loss, so backups are daily git-bundle + weekly remote.

### 7.9 25K exocortex HARD (C11 MC3)

FPF 7-10K + role 2-3K + alpha states 3-5K + Steward 3-5K = ~15-23K baseline. Per-agent FPF-
loading tiers (§5.4a) keep Haiku agents at lower tiers. 950K remainder (Opus 4.7 1M reference)
is working memory. Model-agnostic: 25K HARD holds whether Opus 4.8 ships 2M or Haiku 5 is 200K.

### 7.10 Why full-fidelity Day 1

*"Notion loss recoverable in 1 day, wiki loss = Jetix loss"* (D2 §14). The wiki is the asset.
Under-specifying entity taxonomy saves weeks at the cost of years: retrofitting F-G-R on 10⁴
claims is a quarter of engineering; retrofitting 8 Alphas on a live claim lifecycle is
unhireable. Maximalist pays now.

---

## §8. Answer to Q6 — Privacy / Security Membrane

**Problem restated (D4 §10 Q6).** Tier ACL matrix (public/member/partner/core); surface-from-
core auto-gen; GDPR Art.22(3) + EU AI Act Art.14 CP-5 gate; threat model; DPIA artefact.

### 8.1 4-tier ACL matrix (Day 1, C17)

Per Lock 1 / 3 / 13 / 22 composition:

| Tier | Who | Access | Filesystem realisation |
|---|---|---|---|
| `public` | outside world | surfaces, demos, 10 templates, videos, blog | `jetix-company/content/public/` |
| `member` | invite-vetted (5-criteria + direction-of-life pass) | member area, community chat, mid-tier content | `jetix-company/content/member/` |
| `partner` | contracted partner / specialist / client | working docs, SKU deliverables, retainers | `jetix-company/content/partner/` |
| `core` | Ruslan + FPF-Steward + meta-agent (audit) | prompts, wiki, workflows, FPF innovations | `jetix-os/` + `jetix-company/core/` |

### 8.2 Auto-gen surface-from-core pipeline

Every artefact tagged `tier: surface | mid | deep | core` at creation (Lock 13). Auto-gen
pipeline (per Q11) renders `public` / `member` / `partner` views from core by template
substitution. No hand-maintained duplicates. CI hook-8 (`hook_8_no_leak.py`) fails any public
asset containing core-only strings (9 Jetix Innovations, FPF-Steward internal docs, token-
economy internals).

### 8.3 GDPR Art.22 + EU AI Act Art.14 CP-5 gate (Day-1 scaffold)

Even though Phase-1 may run pre-DPA-client, CP-5 machinery is scaffolded Day 1 — retrofit under
audit is intolerable. Components: gate-keepers (Ruslan primary) + Vertretung alternates
(Steuerberater/lawyer); SLA per class (dept-internal <4h, cross-dept <24h, strategic <72h,
safety immediate); audit-trail YAML per decision (`governance/cp5-audit/YYYYMMDD-NNN.yaml`);
meaningful-review safeguard WP251rev.01 (max 8 L2 approvals/gate-keeper/4h, atom-2725); Art.
22(3) explanation generator (agent-draft, human-sign); contestation mechanism
(`jetix-company/legal/contestation.md`); retention 3y Phase 1, 7y from Phase 2a.

### 8.4 EU AI Act risk-classification scaffold

Per OT3 Scenario C: 4 risk categories (minimal/limited/high/unacceptable); per-action
classifier in `base/compliance/eu-ai-act/classifier.md` (rule-based Phase 1). High-risk agents
auto-CP-5-gated. Compliance-calendar (MC1 P1-#9); system-admin + personal-assistant surface
upcoming deadlines into Monday dashboard.

### 8.5 DPO (external-executor) role-manifest

Day 1: manifest at `roles/l1-foundation/dpo/role.md` with `executor: external-lawyer`
(manager-proxy until Phase 2a). RACI matrix included. Phase-2a Triple-AND activates a dedicated
`dpo` agent instance + formal external DPO appointment per GDPR Art.37-39.

### 8.6 Threat model (outside 8 / inside 4)

**Outside**: (a) public-surface scraping for core-string leakage → CI hook-8; (b) Stripe
phishing on Ruslan → SOPS + hardware-key; (c) DDoS → CDN + rate-limit; (d) prompt-injection
via public inbox → inbox-processor sandbox classification; (e) integration-API breach → SOPS
+ rotation; (f) supply-chain → lockfile + SBOM; (g) Notion compromise → view-only, fs=SoT,
1-day recovery; (h) brand-imitation adversary (Lock 4).

**Inside**: (a) partner-tier account downloading core-tier → ACL-blocked + audit; (b)
credentials committed by contractor → SOPS pre-commit hook; (c) agent-output leaking secrets
→ F-G-R + frontmatter linter; (d) social-engineering `personal-assistant` → J-Auto scope
limits (cannot spend, commit, or send external message without human).

### 8.7 DPIA artefact

`jetix-company/legal/dpia/phase-1-v1.md` Day 1 covers voice-memo processing (STT/extract/
filter/review), inbox-processor (Gmail), Stripe revenue data. Includes §3.1.14 normalization
(`Jackson|Джек → Jetix`). Phase-2a refresh on first DPA client.

### 8.8 Why Day-1 scaffold

Conservative defers CP-5 to first-DPA-client. Maximalist argues *"Gentleman inside / Predator
outside"* (Lock 1) requires the membrane present Day 1, even unused, because retrofitting
membrane discipline after the first breach is too late. Compute cost: ~€0 (YAML + CI hooks).
Engineering cost: ~10-15h Day 1. Value amortises across GmbH lifetime.

---

## §9. Answer to Q7 — API Architecture & €800/mo Defence

**Problem restated (D4 §10 Q7).** Multi-provider router (primary/fallback/degraded); cost-
optimisation (caching/batching/routing); `compute-contract.yaml` canonical schema; observability
(cost per direction/agent/SKU); ≤€800/mo Phase-1 actual. **This is the Maximalist's single
biggest vulnerability; it is defended here in detail.**

### 9.1 Compute-contract schema (canonical, Day 1)

```yaml
# base/compute-contract/schemas/compute-contract.v1.yaml
executor: <agent-id>
model_preference:
  - provider: anthropic
    model: claude-haiku-4.5
    tier: Tier-3
    max_turns_per_task: 20
  - provider: openai
    model: gpt-4o-mini
    tier: Tier-3-fallback
  - provider: google
    model: gemini-flash
    tier: Tier-3-degraded
thinking_mode: off | on-with-budget-tokens=<N>
max_tokens_per_turn: 4096
cache_strategy:
  prompt_cache: on-5min-ttl
  result_cache: sha256-keyed
latency_class: realtime | async | batch
escalation_rules:
  - on: rate_limit
    fallback_immediate: true
  - on: cost_ceiling_eur_per_turn=0.05
    escalate_to: manager
  - on: quality_floor_fgr=R-low
    escalate_to: meta-agent
circuit_breaker:
  window_minutes: 10
  failures_to_trip: 3
  action: pause_tier_3
```

Every agent has a `compute-contract.yaml` in `executors/<id>/`. Changes require DRR.

### 9.2 Routing policy (tier-based, cost-biased)

| Tier | Agents | Default model | Escalation trigger |
|---|---|---|---|
| Tier-1 (critical) | `manager`, `strategy-support-analyst`, `knowledge-synth`, `meta-agent` | Sonnet 4.6 (or Opus for strategic) | always has fallback active |
| Tier-2 (important) | `sales-lead`, `personal-assistant`, `system-admin`, `inbox-processor` | Haiku 4.5 primary; Sonnet on confidence<0.7 | fallback if budget allows |
| Tier-3 (non-critical) | `sales-research`, `sales-outreach`, `crazy-agent` | Haiku 4.5 only | paused on primary outage |

### 9.3 €300-800/mo Phase-1 projected burn (the defense)

Assumptions (conservative-Maximalist, slightly above expected):

- **Phase-1 call volume**: 11 runtime agents, ~50 task-turns/day steady-state.
- **Avg tokens in/out**: Tier-3 Haiku ~2K+0.5K; Tier-2 mix ~4K+1K; Tier-1 Sonnet ~8K+2K.
- **Tier mix (turns/day)**: Tier-3 ≈ 30, Tier-2 ≈ 15, Tier-1 ≈ 5.
- **Pricing (Apr 2026)**: Haiku 4.5 ~$0.80/M in + $4/M out; Sonnet 4.6 ~$3/M + $15/M; Opus 4.7
  ~$15/M + $75/M (rare in Phase 1).

**Daily cost**: Tier-3 ~$0.11, Tier-2 ~$0.17, Tier-1 ~$0.27 → ~$0.55/day = **~$17/mo agent
traffic**. Add cache-miss uplift (~30%), voice-memo pipeline (~€20/mo), STT (~€10/mo),
observability (~€5/mo), Phase-1 spike buffer (×4-5 safety) → **€150-350/mo expected /
€320-520/mo 95p / €650/mo P99**. The €800/mo band holds with meaningful headroom. The calc is
deliberately conservative: voice-memo capped by Ruslan speaking hours; content pipeline uses
BA-0/1/3 batching; no mass-outreach AP-3.

### 9.4 Compute-ledger (§3.1.12, ADR-Chunk-1 P7.2) — the enforcement layer

`finance/compute-ledger.yaml` records every turn:
```yaml
- ts: 2026-04-22T09:32:14Z
  agent: sales-research
  provider: anthropic
  model: claude-haiku-4.5
  tokens: {in: 1840, out: 420}
  cost_eur: 0.0031
  direction: sales
  sku: audit-sku-q2
```

Monthly rollup → dashboard v1 Row 3 (revenue) cross-referenced against cost. **Hard block**:
if `sum(ledger, month) > €800`, `compute-contract` status flips to `degraded`, Tier-3 pauses,
Tier-2 caches aggressively. Manager + Ruslan notified. This is §8.3 defended at the ledger
layer, not by optimism.

### 9.5 Cost-optimisation policy

Prompt cache (Anthropic 5-min TTL) on system-prompt + FPF permeation → ~60-80% token reduction
on sequential turns. Batch mode (Anthropic batch API + OpenAI batch) for non-realtime
(`/lint`, BA-1 audits) → ~50% cost reduction. Result cache (sha256-keyed, invalidated on
upstream change) for deterministic queries (ICP classification, atom lookups). Tier-routing:
pre-classify task → tier before dispatch; Tier-3 never touches Sonnet/Opus except on explicit
escalation.

### 9.6 Observability hooks

Every turn emits an OpenTelemetry-style span to compute-ledger + dashboard. Aggregated daily
per direction × agent × SKU. Anomaly detection (>3σ) alerts system-admin.

### 9.7 Multi-provider Day-1 cost implication

Zero. Adapters live in `base/compute-contract/providers/{anthropic,openai,google}/`. If
`provider_preference[0]=anthropic` in Phase 1, OpenAI/Google adapters never call → €0 spend.
Existence alone makes chaos drill possible. AP-11 avoidance by construction.

### 9.8 Why not "single provider cheaper"

Counter-argument: (a) adapters ~200 LOC each, maintenance ≈ 1h/qtr; (b) AP-11 is anti-pattern
regardless of cost; (c) real risk is outage, not cost — one 4-hour Anthropic outage during
client delivery = €10K+ reputation cost. Adapter maintenance ≈ €40-100/yr against that.

---

## §10. Answer to Q8 — Token Economy Option B

**Problem restated (D4 §10 Q8).** Token-layer state machine; rights-separation (economic vs
governance vs access); DE+US compliance pathway; audit log covering ≥5 canonical events
showing zero Phase-3 token-holder action grants inside-membrane access.

### 10.1 State machine (Day 1 dormant, per Lock 23 Option B)

Location: `jetix-os/token-economy/` (dormant, `_status.md` activation: $100K self-earned for
internal Phase 2; Phase-3 gate for limited-public).

States and transitions:

```
[dormant] --activate_internal--> [internal-phase2]
[internal-phase2] --mint--> [internal-phase2]
[internal-phase2] --hold--> [internal-phase2]
[internal-phase2] --transfer(internal-only)--> [internal-phase2]
[internal-phase2] --burn--> [internal-phase2]
[internal-phase2] --adjust--> [internal-phase2]
[internal-phase2] --activate_public(economic-claim-only)--> [limited-public-phase3]
[limited-public-phase3] --mint--> [limited-public-phase3]
[limited-public-phase3] --transfer(public-restricted)--> [limited-public-phase3]
[limited-public-phase3] --redeem(economic-only)--> [limited-public-phase3]
[limited-public-phase3] --burn--> [limited-public-phase3]
```

No `transfer` path from `internal-phase2` to outside membrane. No `grant-governance-rights`
action at any state. No `grant-community-access` action at any state (C21 / AP-13 hard
enforcement).

### 10.2 Rights-separation schema

```yaml
# token-economy/rights-schema.yaml
rights:
  economic_claim: permitted
  governance_vote: FORBIDDEN
  community_access: FORBIDDEN
  membrane_access: FORBIDDEN
enforcement:
  - layer: schema (YAML + CI lint)
  - layer: protocol (state-machine reject)
  - layer: legal (terms-of-issuance)
```

### 10.3 Jurisdictional pathway

- **DE**: BaFin classification pre-Phase-3 mandatory; token as utility / security assessed by
  external counsel. EU MiCA-compliant issuance (Phase-3 if applicable).
- **US**: Howey-test evaluation by US counsel; Reg D / Reg S pathways. California AI regs
  apply to automation; token itself not AI-regulated.
- Pathway doc: `jetix-company/legal/token-compliance/{de,us}.md` Day 1 as draft; fill at
  activation.

### 10.4 Audit-log canonical events (5+ coverage)

Per Q8 quality criterion:

| Event | Schema | Rights granted | Membrane impact |
|---|---|---|---|
| mint | `{ts, to, amount, reason}` | economic_claim | none |
| transfer (internal) | `{ts, from, to, amount}` | economic_claim | none |
| transfer (limited-public) | `{ts, from, to, amount, jurisdiction}` | economic_claim | none |
| burn | `{ts, from, amount, reason}` | — | none |
| redeem | `{ts, holder, value_eur}` | economic_claim consumed | none |
| adjust | `{ts, delta, reason, signer}` | admin-only | none |

Maximalist adds a CI-level invariant: `grep -r "governance\|access\|vote" token-economy/
| grep -v "FORBIDDEN\|no_\|!"` returns 0 — i.e., any schema/spec mentioning those rights
positively is a lint failure.

### 10.5 Day-1 dormancy & activation trigger

Phase 1: all token files present, `status: dormant`. No ledger rows, no LLM compute. Phase-2
activation ($100K self-earned, internal-only): flip `_status.md` + initialise ledger + publish
internal terms-of-issuance. ~1 week legal+admin; zero architecture change. Phase-3 activation
(MHT-3 + external counsel green-light): flip to `limited-public-phase3`, expose public-API
behind jurisdictional gate. ~4-8 weeks legal. Zero architecture rewrite.

### 10.6 AP-13 hard guard

Any PR touching `token-economy/` that introduces governance-vote or community-access
primitives fails CI hook-9. The architecture says "no" at commit time, not management at
design review.

---

## §11. Answer to Q9 — Matchmaker Algorithm (4 modules)

**Problem restated (D4 §10 Q9).** Graph schema (tasks / specialists / edges / capabilities);
matching algorithm (score function + constraints); contract-fixation + dispute path; metrics
pipeline + dashboard. Dry-run on 20 synthetic pairs → match-rate ≥70%, false-match <5%.

### 11.1 Day-1 scaffold (dormant, per §3.2.3 / Lock 21)

Location: `jetix-os/matchmaker/` with four sub-modules Day 1: `algorithm/`, `quality-gate/`,
`contract/`, `metrics/`. All have spec.md + schema + README + _status.md (activation: €200K
gate + ≥10 active specialists).

### 11.2 Graph schema

```yaml
# matchmaker/algorithm/graph-schema.yaml
node_types:
  task:
    fields: [id, archetype_match, direction_of_life, pain_vector, budget_range, deadline]
  specialist:
    fields: [id, archetype, direction_of_life, capabilities[], past_nps, availability]
  capability:
    fields: [id, category, depth, certifications]
edge_types:
  task-needs-capability: {task_id, capability_id, weight}
  specialist-has-capability: {specialist_id, capability_id, depth}
  pair-completed: {task_id, specialist_id, nps, completion_status}
```

### 11.3 Algorithm module — 4-factor score function

`match_score = 0.4 × capability_fit + 0.3 × archetype_direction_alignment + 0.2 × past_nps
+ 0.1 × availability`

Constraints:
- **5-criteria ICP filter** on specialists (C20, D22): Startupper / Azart / Stable / Adequate
  / Upward — boolean AND before scoring.
- **Direction-of-life axis** alignment ≥ 0.7 similarity (Lock 22).
- **No advisor/mentor hard-coupling** (Lock 6).
- **Archetype compatibility matrix** (11 × 11) — some pairings disqualified per D22.

### 11.4 Quality-gate module

Disqualifiers pre-pair: R-low F-G-R on specialist dossier, open contract-breach log, direction-
of-life mismatch >0.3. If score ≥0.7 → auto-recommend; 0.5-0.7 → Ruslan review; <0.5 → reject.

### 11.5 Contract module

Template DAO / partnership / revenue-share structures in `matchmaker/contract/templates/`.
Contract-fixation produces a signed artefact with L/A/D/E compliance (FPF A.6.B) + jurisdiction
tag. Dispute path: mediator from specialist pool → strategy-support-analyst options memo →
Ruslan acceptance-authority ruling (<48h strategic SLA).

### 11.6 Metrics module

3 D3 §5.3 metrics + Maximalist additions:

| Metric | Target | Source |
|---|---|---|
| Match rate (proposed / pool) | ≥60% | graph query |
| Completion rate | ≥75% | pair-completed edges |
| Ecosystem NPS | ≥40 | post-completion survey |
| Cross-referral rate (Maximalist) | ≥20% | inter-specialist edges |
| Time-to-match (Maximalist) | <72h p50 | ts delta |

### 11.7 Dry-run validation schema

`matchmaker/algorithm/validation/20-synthetic-pairs.yaml` Day 1: 20 pairs with ground-truth
"should-match" labels. CI hook-10 runs scoring on every PR; blocks merge if match-rate <70% or
false-match ≥5%.

### 11.8 Activation commitment

Phase 1: **inert**. Zero traffic, zero compute. Specs + CI hook only. Phase-2+ activation:
flip `_status.md` + feed real data. Algorithm validated on synthetic data Day 1 — activation
risk is data-quality, not algorithm-correctness.

---

## §12. Answer to Q10 — Roy-Replication Packaging

**Problem restated (D4 §10 Q10).** Kit contents (manifests + prompts + wiki subset + runbooks);
install/fork/update lifecycle; inter-roy protocol stack; success + kill criteria per roy
(F.11 Method Quartet). 2nd roy bootstraps in ≤14 days from kit.

### 12.1 Day-1 skeleton (dormant, per §3.2.10)

Location: `jetix-os/roy-kit/`:

```
roy-kit/
├── export-manifest/
│   ├── schema.yaml              # what's exportable
│   ├── inventory-template.yaml
│   └── legal-wrapper.md         # license: methodology-only (Lock 24)
├── kit-template/
│   ├── base/                    # copy of jetix-os/base/ (universal)
│   ├── overlay-template/        # minimal overlay scaffold
│   ├── roy-installer.sh         # 14-day bootstrap runbook
│   └── per-roy-config.yaml
├── replication-assessment/
│   ├── success-metrics.md       # F.11 Method Quartet
│   ├── kill-criteria.md
│   └── 30-60-90-day-audit-template.md
└── _status.md                   # activation: €1M + Ruslan acceptance-authority
```

### 12.2 Exportable vs closed

Per Lock 24 + C3 / C13:

| Exportable (open output, Phase 2+) | Closed (methodology operational core) |
|---|---|
| Role-manifest *schemas* (not instantiated roles) | 9 Jetix Innovations |
| Wiki structure (9 types, F-G-R) | Jetix-specific prompts, entities, atoms |
| FPF constitutional (D6 subset) | Jetix-specific foundations & summaries |
| Protocol specs (Q15 USB-C) | Jetix-specific agent-instantiation configs |
| Matchmaker 4-module public schema | Matchmaker specialist pool data |
| Roy-installer runbook | Ruslan playbook (strategy-lead notes) |

### 12.3 Kit lifecycle

- **Install**: `roy-installer.sh --roy-name=<X>` copies `base/` + overlay template; Day 1-14
  roy-N scaffold.
- **Fork**: kit is git-forkable; per-roy private repo. Parent roy (Jetix) publishes semver-
  tagged methodology updates.
- **Update**: per-roy decides merge-in cadence. F.11 Method Quartet Harmonisation monthly per-
  direction (Rec-18).
- **Telemetry**: per-roy emits anonymised health metrics to Jetix federation layer
  (`federation/roy-telemetry/`). Opt-in; Option B membrane preserved.

### 12.4 Inter-roy protocol stack (Phase 3+)

- **Federation**: namespace + identity federation (roy-id as first-class).
- **Safety-net**: mutual aid protocol (Phase-3 economic-claim flows across roys).
- **Orchestration**: Jetix-central meta-coordinator (§3.3.2) for joint projects.
- **Methodology propagation**: semver-tagged update bus (methodology-version lag ≤1 release).

### 12.5 Why Day-1 scaffolding

Replication-assessment rubric drift = roy-2 installs kit-v1.0 and Jetix ships kit-v1.5 without
backward-compat; the breakage is legendary in open-source. Pay upfront with schemas. Phase 1
compute cost: €0.

---

## §13. Answer to Q11 — Content Pipeline TOF/mid/deep

**Problem restated (D4 §10 Q11).** Pipeline source → frame-tag → render → channel; archetype-
keyed rendering engine (11 archetypes × 3 tiers = 33 variants); deep-content ACL + subscription-
check flow; cadence model.

### 13.1 Pipeline graph Day 1

```
[Ruslan seed content] ─┬─> frame-tagger (pain-primary default TOF; opportunity-reinforcing mid/deep)
                       ├─> archetype-router (11-way, D1 §7.1)
                       ├─> tier-classifier (TOF | mid | deep | core)
                       └─> channel-renderer
                            ├─> public: site, social, podcast, video, bloggers
                            ├─> member: mid-tier gated
                            ├─> partner: deep-tier gated
                            └─> core: never publicly rendered
```

### 13.2 Frame-tag schema (mandatory)

```yaml
---
frame: pain-primary | opportunity-primary | hybrid
tier: TOF | mid | deep | core
archetypes: [startupper, azart, stable, ..., bloggers]   # 11-way set
direction_of_life: [-1..+1]
...
---
```

No artefact ships without all four fields (CI hook-11).

### 13.3 Archetype-keyed rendering (11 × 3 = 33 variants Day 1)

Template substitution per archetype × tier. Renderer engine
(`base/content-pipeline/renderer/`) applies archetype-specific framing (lexicon, pain vector,
opportunity frame, direction-of-life tone). **Phase 1: Ruslan authors seed content; renderer
emits the 33 variants automatically from a single source.** No mass-market automation (AP-3 +
AP-10 guard).

### 13.4 Deep-content ACL + subscription-check

Deep-tier artefacts in `jetix-company/content/deep/`. Public-surface link resolves to
`/member-or-deeper/` check → auth → tier-match → serve. Zero deep-content leak to public CDN
(Q11 quality-criterion).

### 13.5 Cadence + capacity (Phase 1)

TOF: 3-5 social posts/week (auto-rendered) + 1-2 podcasts/mo + blogger collabs. Mid: 1 site
lead-magnet/mo + 2 mid-tier articles/mo. Deep: 1 deep-dive/qtr + retainer-only. Editorial
escalation: every deep-tier signed off by `acceptance-authority`; TOF/mid batch-reviewed
monthly.

### 13.6 BA-0/1/3 closure (§3.1.3)

Every video-content deliverable: BA-0 (pre-production bias audit) + BA-1 (mid-production
contradiction scan) + BA-3 (post-delivery retrospective). BA-2 Panel activates Phase-2a.

### 13.7 Why Maximalist here

Conservative: render per-artefact per-archetype at publish time. Maximalist: render-engine
with 11 × 3 template matrix Day 1; scaling 1 archetype (Phase-1) → 11 (Phase-2+) is data-load,
not code-change.

---

## §14. Answer to Q12 — Dashboard Implementation

**Problem restated (D4 §10 Q12).** v1 Phase-1 (5 metrics) + v2 Phase-2+ + v3 Phase-3+ per §4.7;
collection pipeline + retention + time-series store; render layer (CLI/fs/Notion view-only);
Monday ritual <5min. Schema forward-compatible to roy-level without migration.

### 14.1 Three versions scaffolded Day 1

| Version | Phase | Metrics | Data source | Render |
|---|---|---|---|---|
| v1 | Phase 1 | 5 mandatory (§4.7) | fs + Stripe + ledger | `dashboard/v1/current.md` |
| v2 | Phase 2+ | +Deep Hours, +productized %, +queue-health, +partner-SLA, +roy count, +roy revenue, +match rate, +member count | fs + matchmaker + subscription ledger | v2/current.md (empty Phase 1) |
| v3 | Phase 3+ | +market-cap, +token circulation, +research outputs, +sub-network activity, +holding roll-up, +cross-partner KPIs | federation + token ledger + research pipeline | v3/current.md (empty Phase 1) |

### 14.2 Metrics schema (forward-compatible Day 1)

```yaml
# dashboard/metrics.yaml (excerpt)
metrics:
  - id: architect-hours-per-week      # v1; target: declining from 18; collector: toggl
  - id: founder-dependency-pct        # v1; target <30% @ €200K; collector: task-origin-tag
  - id: monthly-revenue-eur           # v1; gates [€50K, €200K, €1M]; collector: stripe+wise
  - id: failure-rate-mttr             # v1; ≤3/mo, MTTR p50 ≤42min
  - id: cash-runway-months            # v1; ≥6
  - id: deep-hours-weekly             # v2; 25-30/wk
  - id: productized-revenue-pct       # v2; €200K ≥40%, €1M ≥70%
  # v2/v3 rows present Day 1 with empty data
```

### 14.3 Collection + retention

- **Phase 1 stack**: filesystem JSON + markdown renders. `dashboard/collectors/` has one small
  script per data source (stripe, compute-ledger, toggl, task-origin). Cron-driven weekly
  (Monday 10:00 Berlin, render completes by 12:00 Berlin — 95% on-time hard commitment).
- **Retention**: git-versioned snapshots in `dashboard/history/YYYY-WW/`; quarterly rollup.
- **Phase 2+ upgrade**: same schema to time-series DB (InfluxDB or timescaleDB) — schema
  already roy-level-compatible.

### 14.4 Render layer

- Monday: `dashboard/v1/current.md` regenerated (<5min per Q12 quality-criterion).
- Notion one-way sync (C4): Notion page at `3492...` receives the rendered view; never authoritative.
- CLI: `jetix dashboard` prints current.md.
- Alerts: per metric `alert_on:` threshold → system-admin + manager mailbox; safety → Ruslan.

### 14.5 Anti-engagement safeguards (AP-3 / AP-10)

- No gamification / leaderboards / streaks.
- Metrics measure substance (revenue, quality, reliability) not time-spent.
- Dashboard emits **decline-desired** metrics (architect-hours) — opposite of attention-
  extraction.

### 14.6 Phase-3 forward-compat

v3 schema Day 1 includes: holding-federation-roll-up rows, token-circulation rows, research-
output rows. Schema uses stable field names; adding data Phase-3 doesn't rewrite the renderer.

---

## §15. Answer to Q13 — Escalation Routing

**Problem restated (D4 §10 Q13).** 6 non-delegatable + 4-class FPF taxonomy + CP-5 GDPR gate +
F-G-R trust gating. Every Phase-1 agent action maps to exactly one class; unmapped actions
blocked at schema level.

### 15.1 6 non-delegatable ↔ 5 Ruslan sub-roles mapping

| Non-delegatable (D1 §3 / D2 §14) | Sub-role executor |
|---|---|
| Стратегия | `strategy-lead` |
| Вкус | `framing-lead` |
| Ответственность, Утверждение | `acceptance-authority` |
| Эскалация | `strategy-lead` (default) / `acceptance-authority` (delivery) |
| Отношения | `sales-closer` (inside) / `external-relations` (outside) |

### 15.2 4-class FPF escalation taxonomy (atom-2558)

| Class | Route | SLA | Authority |
|---|---|---|---|
| dept-internal | Dept Lead | <4h | J-Auto/Approve |
| cross-dept | `manager` (≤20 active) | <24h | J-Approve |
| strategic | Ruslan `strategy-lead` | <72h | J-Strategic (NEVER decides except Ruslan) |
| safety | meta-agent + Ruslan **immediately** | immediate | halts current task |

### 15.3 Schema-level enforcement

`shared/schemas/message.schema.json` includes `escalation_class:` required field with enum
`[dept-internal, cross-dept, strategic, safety]`. Every message carries it; messages without
a class are rejected at schema validation. CI hook-12 runs schema validation on commits
(filesystem-authoritative enforcement, C4).

### 15.4 CP-5 Human Approval Gate (Day-1 scaffold)

Per §8.3: gate-keepers + Vertretung alternates, SLA per class, audit-YAML per decision,
meaningful-review safeguard (≤8 L2 approvals per gate-keeper per 4h), Art.22(3) explanation
generator, contestation mechanism, retention policy. This is operational Day 1; gate traffic
is zero until DPA client materialises.

### 15.5 Founder-unavailable class

Per D4 §4.4: Phase-1 proxy = Steuerberater / lawyer stub per Constitution §11 + `executor-
binding.yaml` chain-of-command. Routes: Ruslan → designated trustee → Beirat alternate
(Phase 2a+).

### 15.6 Maximalist signature: escalation-trace audit loop

Every escalation logged to `wiki/experiments/escalation-traces/YYYYMMDD-NNN.md` with F-G-R +
class + outcome + time-to-resolve. meta-agent's quarterly audit mines this log to tune CP-5
thresholds empirically (C16). **Instrumented governance, not assumed.**

### 15.7 Why schema-first

Q13's quality-criterion is "unmapped actions blocked at schema level". Maximalist satisfies by
requiring `escalation_class:` in `message.schema.json` Day 1 — not "added when we notice the
gap". Cost zero; assurance total.

---

## §16. Answer to Q14 — Onboarding Architecture

**Problem restated (D4 §10 Q14).** Onboarding checklist + X-day timebox; permission/influence
scoping per partner per direction (D20); new-pilot kickoff template; migration audit for
hardcoded single-user paths. 2nd pilot cold-start to first commit ≤7 days.

### 16.1 Day-1 onboarding kit (full scaffold, dormant until 2nd pilot)

Location: `jetix-os/base/onboarding/`:

```
onboarding/
├── intake-form/
│   ├── schema.yaml                    # 5-criteria + direction-of-life + archetype
│   └── template.md
├── pilot-agreement/
│   └── template.md                    # L/A/D/E compliant, F.6 6-step cycle
├── baseline-fpf-contract/
│   └── client-facing-role-manifest.md
├── first-5-days-runbook/
│   ├── day-1.md ... day-5.md
│   └── first-commit-checklist.md
└── welcome-pack-generator/            # automation Phase-2
    └── stub.py
```

### 16.2 7-day cold-start timeline

| Day | Activity | Who | Output |
|---|---|---|---|
| 1 | Intake form + ICP 5-criteria + direction-of-life | pilot + `sales-research` | signed intake |
| 2 | Kickoff meeting + pilot-agreement + DPA | pilot + `sales-lead` + lawyer | signed agreement |
| 3 | Repository access + mailbox provisioning | `system-admin` | access audit log |
| 4 | Baseline FPF contract + agent onboarding (F.6 1-2) | pilot + `manager` | F.6 milestones 1-2 |
| 5 | First task assignment + shadow with Ruslan | pilot + `strategy-lead` | first assignment |
| 6 | First commit | pilot | commit hash |
| 7 | BA-0 retrospective + F.6 step-3 | pilot + `meta-agent` | retrospective doc |

**Quality criterion satisfied**: 2nd pilot cold-start to first commit in ≤7 days; zero schema
migrations required.

### 16.3 Permission/influence scoping per partner per direction (D20)

Per partner × per direction (the quarterly attention-theme), a permission matrix:

```yaml
# onboarding/<pilot-id>/permissions.yaml
pilot: ana-gmbh
directions:
  sales:  {read: true, write: true, approve: false}
  research: {read: true, write: false}
  life-os: {read: false, write: false}
influence_scope:
  - sales-content (co-authorship)
  - icp-iteration (proposal only)
```

Changes require DRR.

### 16.4 Migration audit for single-user paths (Lock 2 / C1)

Pre-commit Hook 13 (`hook_13_single_user.py`) fails any commit introducing `/home/ruslan`,
single-user hardcoded paths, or single-path assumption in `base/`. Day-1 audit sweep on
existing code ensures baseline is clean (C1: solo-now-team-ready).

### 16.5 F.6 6-step onboarding cycle

Step 1 Foundation briefing (FPF permeation, 25K exocortex). Step 2 Role-manifest assignment
+ executor-binding. Step 3 First shadow task + BA-0. Step 4 First independent task + F-G-R
practice. Step 5 First sign-off with `acceptance-authority`. Step 6 30/90/180-day
retrospectives scheduled.

### 16.6 Why Day-1 scaffold

Onboarding rot is invisible until the 2nd pilot arrives stressed. Maximalist pays 1-2 days of
upfront template drafting so pilot-2 hits a polished process; Conservative builds templates
when pilot-2 arrives, risking delay + bad first impression.

---

## §17. Answer to Q15 — USB-C Protocol Layer

**Problem restated (D4 §10 Q15).** Protocol taxonomy (AI↔biz / biz↔biz / specialist-onboard
/ inter-roy); message-schema canonical set + versioning; verification layer (attestation +
audit); standards-readiness. 3rd-party AI agent implements 1 Jetix protocol and completes
handshake in reference harness. **Maximalist's signature answer.**

### 17.1 Day-1 full-spec scaffold

Location: `jetix-os/protocols/`:

```
protocols/
├── spec/
│   ├── taxonomy.md                     # 4 workstreams × sub-categories
│   ├── ai-business.md                  # AI↔biz cooperation protocol
│   ├── business-business.md            # biz↔biz partnership protocol
│   ├── specialist-onboard.md           # partner/specialist protocol
│   └── inter-roy.md                    # roy↔roy federation protocol
├── message-schemas/
│   ├── v1/                             # versioned canonical schema set
│   │   ├── intake.json     handoff.json     escalation.json
│   │   ├── reporting.json  contracting.json  audit.json
│   └── versioning-policy.md            # semver + deprecation
├── verification-harness/
│   ├── spec.md                         # attestation + audit requirements
│   ├── reference-implementation-skeleton/
│   │   ├── README.md
│   │   ├── harness.py.template          # Python reference harness
│   │   └── fixtures/
│   │       └── 3rd-party-handshake.yaml # acceptance test
│   └── failure-mode-catalog.md
├── standards-draft/
│   ├── draft-submission.md              # IETF/W3C-style draft, ready to file
│   ├── draft-accompanying-whitepaper.md
│   └── submission-schedule.md           # activation: Phase 2+
├── README.md
└── _status.md                           # activation: €200K gate for publication
```

### 17.2 Protocol taxonomy (6 canonical)

Per Q15 expected-scope (matches E.17 5-view bundle feedstock):

| Protocol | Message types | Verification predicates |
|---|---|---|
| `intake` | request, response, audit-log | schema-valid, F-G-R present, CP-5 applicable flagged |
| `handoff` | artifact-transfer, acceptance, rejection | acting_as valid, L/A/D/E complete, BA-3 signed |
| `escalation` | class-routed message, audit-YAML | class ∈ {dept-internal,cross-dept,strategic,safety}, SLA window respected |
| `reporting` | status-update, metric, retrospective | dashboard-schema compatible, anti-engagement |
| `contracting` | proposal, signature, dispute | jurisdiction-tag, DPA-compliant, 5-view bundle |
| `audit` | evidence-package, retention, contestation | WP251rev.01 meaningful-review, retention ≥ 3yr |

### 17.3 Verification harness (Day-1 reference skeleton)

`verification-harness/reference-implementation-skeleton/` contains a runnable Python skeleton
that:
1. Loads a message per v1 schema.
2. Runs verification predicates.
3. Emits attestation (JWS-style signed JSON) or failure reason.
4. Returns a machine-readable audit log.

Phase 1: runs locally on CI for Jetix-internal messages (dogfooding). Phase 2+: published as
reference for third-party implementers. Phase-3+ (€1M+): formal standards-body submission.

### 17.4 Dogfood verification on Phase-1 traffic

CI hook-14 (`hook_14_protocol_verify.py`) runs on every PR touching `comms/mailboxes/`
message schemas: validates against `protocols/message-schemas/v1/*.json`. This ensures
internal traffic is USB-C-compliant Day 1, so by the time Phase-2 publishes externally, the
protocol has years of self-testing.

### 17.5 Standards-body timeline

Lock 19 + Lock 20 = USB-C positioning. IETF/W3C/ISO adoption takes 18-36 months. If Jetix
waits for €200K to start drafting, the Phase-3 claim is hollow. Maximalist ships
`standards-draft/draft-submission.md` Day 1; iterates internally; files publicly at €200K.

### 17.6 3rd-party handshake fixture

`verification-harness/.../fixtures/3rd-party-handshake.yaml` = Q15 quality criterion: a
declarative test where a 3rd-party AI agent (mock or real) exchanges `intake → response →
audit` with the Jetix harness. CI runs it weekly. Phase 2+ invites external partners to run it
in their environments.

### 17.7 Why Day-1

The variant's sharpest differentiator. Conservative defers USB-C to post-revenue. Maximalist:
(1) protocol design is cheap (€0 compute, Ruslan + knowledge-synth hours); (2) standards-body
lead-time is long; (3) verification harness disciplines internal message traffic Day 1 — every
agent handoff is a live protocol exercise; (4) Phase 2+ publication is a commit, not a project.

---

## §18. Foundation Layer Specification

*"Foundation = главный актив"* (D2 §14). *"Quality cannot be retrofit at $1T scale"* (D2 §14).
*"Notion loss recoverable in 1 day, wiki loss = Jetix loss"* (D2 §14). This section is the
**Maximalist's one unambiguous point of highest investment**: all 8 Foundation elements at
full fidelity Day 1, each with schema / API / protocol concretely specified.

### 18.1 Element 1 — wiki + ATOM-REGISTRY

**Day 1 state.** Full 9 entity types + atoms-registry JSONL (3626-atom seed normalised to stable
atom-NNNN IDs) + 8 Alphas state machine + typed edges JSONL (10 types). Per-agent L3 memory via
symlinks from `agents/<id>/niche/`. Voice-memo pipeline with Lock-4 canonicalization.

**Schema locked Day 1.** All 9 entity-type templates in `wiki/_templates/`, validated by CI
hook-5. Changes require DRR.

**Per-gate path.** €50K: stable (no migration). €200K: optional GraphRAG upgrade for /ask
latency. €1M: shard claims by `scope:` if >10⁶. $100M+: federated wiki per roy.

**Migration from current state.** `knowledge-base/` legacy folder enters deprecation window
(MIGRATION.md already tracks); `pipeline: ready` entries migrate to `wiki/` by entity type;
schema-incompatible entries flagged for knowledge-synth rewrite. Target completion: Phase 1 Week 6.

### 18.2 Element 2 — Agent contracts

**Day 1.** Per D4 §4.1: 5-block `role.md` (identity/ontological/method/production_dependencies
/evolution) + separate `executor-binding.yaml` (compute-contract P7 / agent_onboarding F.6 /
agency-profile A.13:4.3 Rec-08). `acting_as:` in every message. Per-agent FPF-loading tiers
(§5.4a). J-level seniority-lite. All 11 runtime agents have complete contracts Day 1; all 12
dormant/assumed manifests have `role.md` activation-gated.

**Per-gate.** €20-30K: stub readiness. Phase-2a Triple-AND: dpo + customer-success activate.
€1M: Phase-3 dormant manifests become runtime.

### 18.3 Element 3 — Handoff protocols

Message-schema canonical set (§17.2); `acting_as` mandatory; async-default; named sync points
(proposal-signing, deliverable-acceptance, BA-3 closure, strategizing). Stale-dep 48h → dept-
lead. E.17 5-view Viewpoint Bundle on every Audit SKU delivery.

MHT-1/2/3/4 transition templates in `base/handoff/mht/` Day 1 (from-holon/to-holon/triggers/
emergence-signals/re-identification/transition-process/supervisor-feedback). Sign-off =
`acceptance-authority`. Roy-to-roy stub: `protocols/spec/inter-roy.md` spec complete.

### 18.4 Element 4 — Escalation protocols

See §15. 4-class taxonomy + CP-5 + founder-unavailable chain-of-command + escalation-trace
audit loop. All operational Day 1; gate traffic scales with client count.

### 18.5 Element 5 — Continuous quality metrics

Per D4 §4.6: F-G-R on every artefact (frontmatter); bias taxonomy 5-class (REP/ALG/VIS/MET/LNG,
atom-2525); Contextual Load (CL<2 blocks); F.11 Method Quartet Harmonisation monthly per-
direction; B.4 Canonical Evolution Loop in 4 rituals (daily/weekly/monthly/quarterly); orphan-
count / contradiction-count / stale-claims / F-G-R compliance %.

D.5 Bias-Audit Cycle: BA-0/1/3 Phase 1 operational; BA-2 Panel activates Phase-2a. E.2 11
Pillars: every DRR cites ≥3 (P-1 Cognitive Elegance, P-2 Didactic Primacy, P-3 Scalable
Formality, P-6 Lexical Stratification, P-9 State Explicitness). E.5 Four Guard-Rails: GR-1
DevOps Lexical Firewall / GR-2 Notational Independence / GR-3 Unidirectional Dependency /
GR-4 Cross-Disciplinary Bias Audit — CI-enforced.

### 18.6 Element 6 — Dashboard

See §14. v1 live Phase 1; v2 / v3 scaffolded. Monday 12:00 Europe/Berlin 95% on-time hard
commitment. Schema roy-level-compatible Day 1.

### 18.7 Element 7 — Reserve routes (failover)

See §5 + §9. Multi-provider Day 1 (Anthropic + OpenAI + Google). Duplicate contractors (≥2
lawyers, ≥2 designers, backup Steuerberater) in `governance/contractors/redundancy.md`. Agent-
tier classification (Tier 1/2/3 + degraded mode). Crisis playbooks (incident / hit-by-bus /
continuity / disaster-recovery / gdpr-art-33). Healthchecks.io monitoring.

### 18.8 Element 8 — F-G-R tagging

Every `.md` file requires YAML frontmatter with `formality: F0..F9 / reliability: R-low|medium
|high|certified|formally-proven / claim-scope: <bounded-context>`. Pre-commit Hook 5 validates.
Retrofit 10-15 existing ADRs on rollout Days 15-17 (D4 §3.2 + D3 §3.2). Enforcement at
creation-time, not retrofit: no artefact enters wiki without F-G-R. Retrofitting 10⁴ claims
at Phase-3 is the Lock-19 nightmare; 15-17 days now prevents it entirely.

### 18.9 Foundation investment budget (Phase 1 one-time)

| Element | Ruslan-h | knowledge-synth-h | system-admin-h |
|---|---|---|---|
| wiki + atoms | 25 | 40 | 5 |
| agent contracts | 15 | 20 | 3 |
| handoff | 5 | 15 | 2 |
| escalation | 8 | 12 | 2 |
| continuous quality | 10 | 20 | 5 |
| dashboard v1/v2/v3 | 5 | 10 | 8 |
| reserve routes | 3 | 5 | 10 |
| F-G-R | 10 | 15 | 5 |
| **Total** | **81** | **137** | **40** |

At 10 Ruslan-hours/week (Phase-1 realistic), Foundation = ~8 Ruslan-weeks front-loaded,
amortised across years.

---

## §19. Hard Constraints Compliance Matrix

Every constraint C1-C21 × this-variant-component × section × residual risk.

| # | Constraint | Variant component | Section | Residual risk |
|---|---|---|---|---|
| C1 | Solo-now-team-ready | Role-manifest layer + onboarding kit Day 1; Hook 13 single-user block | §4, §16 | low |
| C2 | Revenue-gated spend | Compute-ledger hard-block; `_status.md` activation-gated folders | §9.4, §3.2 | low (tested in §9) |
| C3 | Closed outside / open inside | 4-tier ACL; auto-gen surface-from-core; CI hook-8 | §8, §13 | low |
| C4 | Filesystem source of truth | Git authoritative; Notion one-way; roster 3-way-diff hook-6 | §3, §4.7, §14.4 | low |
| C5 | Consulting-first Phase 1 | `jetix-company/sales/` + Audit-SKU pipeline primary; Secure Network dormant | §5.2, §3.1 | low |
| C6 | Productization over hours | Pricing multi-tier in sales pipeline; productized % metric v2 | §13, §14 | medium (depends on Phase-2 execution) |
| C7 | Investment-fund philosophy | DRR schema has expected_return/horizon/kill_criteria | §3, §18.5 | low |
| C8 | Layered identity | Layered-brand object; archetype-keyed rendering; frame-tag | §13 | low |
| C9 | Universality | Base/overlay split; D-test CI hook-4; ≥3 use-case templates | §3 | low |
| C10 | English+US primary | `jetix-company/` EN+US defaults; DE activation at revenue | §3 (overlay) | low |
| C11 | JETIX-FPF mandatory | FPF permeation in every `system.md`; tiered §5.4a; 25K exocortex HARD | §7.9, §18.2 | low |
| C12 | Role ≠ Executor strict | 5-block `role.md` + `executor-binding.yaml`; IP-1; Hook 5 | §4, §18.2 | low |
| C13 | F-G-R mandatory | Every artefact frontmatter; Hook 5; retrofit plan | §7.3, §18.8 | medium (retrofit effort) |
| C14 | 11-agent canonical roster | Runtime 11 + role-manifest layer; Hook 6 enum regen | §4 | low (central to design; verified by §4.7-4.8) |
| C15 | Physical Life-OS separation | Day 1 folder separation + Hook 1 + SOPS 1-key | §3 | low |
| C16 | Continuous quality | F-G-R + CI hooks + BA-0/1/3 + B.4 rituals + random-sample audits | §18.5 | low |
| C17 | Gentleman/Predator membrane | 4-tier ACL; frame-tag; auto-gen surface | §8, §13 | low |
| C18 | $1T no-rewrite trajectory | Schema-heavy scaffolding; §6 extension-points; §6.4 LOC budget | §3, §6 | medium (thesis-dependent) |
| C19 | USB-C + enterprise-fast | Full protocol Day 1; verification harness; standards-draft | §17 | low |
| C20 | ICP 5-criteria + direction-of-life | Matchmaker 5-criteria filter; onboarding intake-schema | §11.3, §16.1 | low |
| C21 | Token Option B membrane | State machine + rights-schema + CI hook-9; zero public-governance primitives | §10 | low |

Residual risks all medium or lower. No constraint violated.

---

## §20. Anti-Patterns Avoidance Statement

| AP | Avoidance mechanism | Section |
|---|---|---|
| AP-1 Notion-as-primary | fs=SoT; Notion one-way sync; C4 enforcement | §3, §14.4 |
| AP-2 Hour-billing-only | Multi-tier SKU primitives Day 1; productized % metric | §5.2, §14 |
| AP-3 Mass-market features | Pull-based membership; no engagement metrics in dashboard; anti-gamification in §14.5 | §14 |
| AP-4 Public OSS of core | `jetix-os/core/` Tier-4 ACL; internal-only forever; open-research Phase 2+ with closed-methodology filter | §8, §12.2 |
| AP-5 Hard-coded Jetix in base | Symbolic D-test CI hook-4; base/ Greek-lettered | §3.3, §3.4 |
| AP-6 One-person assumptions | Hook 13 single-user block; multi-pilot onboarding Day 1; mailbox-primitive Day 1 | §16 |
| AP-7 Slow-corporate governance | Named SLAs per escalation class; <24h cross-dept; no committee-for-every-policy | §15 |
| AP-8 Chaotic-startup governance | Every decision a DRR; ADRs mandatory; F-G-R discipline | §18 |
| AP-9 Motivational-circle community | 5-criteria + direction-of-life ICP filter at invite; no pep-talk channels | §8.1, §11.3 |
| AP-10 Attention-extraction | Time-saving KPIs; no notifications designed-to-pull; pull-based dashboard | §14.5 |
| AP-11 Single-provider AI | Multi-provider Day 1 (Anthropic + OpenAI + Google); compute-contract schema; chaos drill | §5, §9 |
| AP-12 Pure-research institution | Research scope-filtered to revenue-instrumental Phase 1; open-research folder dormant | §3 |
| AP-13 Public token with governance | State-machine forbids; rights-schema forbids; CI hook-9; token-economy folder dormant | §10 |
| AP-14 Equal-weight channels | Site primary; social = TOF only; tier + frame + archetype mandatory | §13 |
| AP-15 Monolithic brand | Layered-identity object; frame per observer × phase; archetype-keyed rendering | §13, §8 |
| AP-16 Boutique-scale shortcuts | §5.1 schema headroom; Hook 7 no-boutique CI block; sharding-key in every 10⁶-class table | §6, §18 |

Watch items (auditors will test):
- **AP-11**: adapters present but untested → chaos drill quarterly (§5.3).
- **AP-13**: token-economy folder must never contain governance-vote / community-access primitives
  even as commented-out code → CI hook-9 + grep audit.
- **AP-16**: `10⁶-entity-capable` claim must be measurable → §6.1 sharding-key column.

---

## §21. Self-Scoring on D4 §8 Quality Axes

| # | Axis (weight) | Self-score (0-10) | Rationale |
|---|---|---|---|
| 1 | Phase-1 readiness (20%) | 6.5 | All Phase-1 capabilities have concrete design (§3-§17 cover 15/15 questions); surface area is genuinely large; Foundation investment Day 1 = ~8 Ruslan-weeks; scaffold-rot risk if revenue is slow (§23). |
| 2 | Scale trajectory (15%) | 9 | Thesis of the variant. §6 per-subsystem scale-path + sharding-keys + LOC-refactor budget concrete. 10× <30% ceiling satisfied through €1M gate by construction. |
| 3 | Foundation quality (15%) | 9 | Thesis of the variant. All 8 elements at full fidelity Day 1 (§18). Every claim cites ≥1 source; 8 Alphas operationalised; F-G-R mandatory at creation. |
| 4 | Locks compliance (18%) | 9 | All 24 locks cited + designed (§19 matrix). C14 preserved (§4.1-4.2); §8.3 defended (§9.3); no invention. |
| 5 | Universality (10%) | 8 | B/C/D tests pass Day 1 (§3.3). ≥3 non-Jetix use-case dry-runs scheduled Day 1. Configurability ratio target ≥90%. |
| 6 | Operational simplicity (10%) | 5 | Honest weakness. Surface area is large; cognitive load on Ruslan is real (§23 Risk 4). README onboarding for new pilot non-trivial. |
| 7 | Cost efficiency (gate §8.3) | PASS | Projected €320-520/mo steady-state; €800/mo ceiling defended via compute-ledger hard-block (§9.3-9.4). |
| 8 | Resilience (5%) | 8 | Multi-provider Day 1; tier-classified failover; crisis playbooks; Healthchecks.io. |
| 9 | Security posture (5%) | 8 | 4-tier ACL Day 1; CP-5 scaffold Day 1; DPIA artefact Day 1; SOPS; threat model 8+4. |
| 10 | Innovation (2%) | 8 | Protocol layer Day 1; role-manifest layer as C14-compliant scale vector; escalation-trace audit loop; maximalist pattern generalisable. |

### 21.1 Weighted total

`0.20×6.5 + 0.15×9 + 0.15×9 + 0.18×9 + 0.10×8 + 0.10×5 + 0.05×8 + 0.05×8 + 0.02×8 =
1.30 + 1.35 + 1.35 + 1.62 + 0.80 + 0.50 + 0.40 + 0.40 + 0.16 = **7.88/10 = 76.2/100**`

Hard floor check: no axis below 3 → PASS. §8.3 compute gate: PASS.

### 21.2 Alternative weighting (informational, not adopted)

Per §8.2, architects may propose alternative weights. If Ruslan re-weighted per Lock 19,
Maximalist would suggest: Scale → 20% (from 15%), Foundation → 18% (from 15%), Phase-1 → 15%
(from 20%). Under that reweighting the variant scores ~80/100. Not adopted for scoring; use
the brief's canonical weights for comparability.

---

## §22. Variant Contrarian Claims

The Maximalist rarely disagrees with D4 — the brief is maximalist in spirit. Three
observations, not fixes.

**Flag 1 — C14 wording on "role-manifest layer".** The variant reads C14 as a *runtime*
constraint (the roster of agents that receive mailbox messages per D6 §2.2), not a design-
surface constraint. If C14 forbids any named role-manifest beyond 11 (including `executor:
ruslan` or `executor: null`), the Maximalist pattern is invalid. Observation: Stage 7 should
clarify. Maximalist's reading is consistent with D4 §4.1 (which explicitly allows 5 Ruslan
sub-roles + 2 Phase-2a stubs as role-manifests). No D4 change proposed; clarification requested.

**Flag 2 — §8.3 €800/mo is Phase-1 only.** At Phase-2a activation (+2 agents, +matchmaker,
+content scaling), burn doubles. §5.6 phrases the limit as "Phase 1 run rate". Stage 7 should
confirm Phase-2 ceiling (€1500? €2500?) or keep €800/mo hard across phases. No §8.3 change
proposed.

**Flag 3 — AP-16 wording.** "No SQLite-only core store" vs Phase-1 lightweight reality: wiki
is filesystem + JSONL, no SQLite. A reader interpreting AP-16 as "distributed store Day 1"
would reject the filesystem-first design. Maximalist reads AP-16 as "schema headroom for 10⁶
entities" per D4 §5.1 "schema headroom, not explicit load". No change proposed.

That is the full list. The Maximalist respects the brief.

---

## §23. Risk Profile

Top 7 risks specific to the Maximalist variant. Probability × impact × mitigation.

| # | Risk | Probability | Impact | Mitigation |
|---|---|---|---|---|
| 1 | €800/mo ceiling breach | low steady / medium on spikes | §8.3 disqualifier forces re-architecture | compute-ledger hard-block (§9.4); Tier-3 pause on breach; monthly Monday review; per-agent cost budget in `executor-binding.yaml`; trend-alert at €600/mo |
| 2 | C14 creep (role-manifest layer becomes de-facto agent bloat) | medium (~30%) | messages routed to dormant manifests = C14 violation in spirit | `executor: null` or `executor: ruslan` strict YAML enforcement; CI hook-6 regenerates enum from `agents/active/` so dormant-manifest messages fail at schema validation; meta-agent quarterly inventory audit |
| 3 | Scaffold rot (dormant specs diverge from reality) | medium-high (~45%) over 2-3y | Phase-2 activation finds specs mismatched | `last_reviewed_ts` frontmatter on every dormant spec; meta-agent quarterly flag of specs >6mo unreviewed; `_status.md` owner-named refresh cadence; honest deprecation over quiet rot |
| 4 | Cognitive load on Ruslan (too many designed-dormant surfaces) | high (~65%) Phase 1 | confusion between "runs Day 1" vs "scaffolded"; onboarding time up; decision paralysis | every `_status.md` human-readable; `jetix tree` CLI renders active-vs-dormant map; top-level `README.md` has 1-page "what runs in Phase 1" orientation; living `wiki/foundations/what-runs-phase-1.md` maintained by knowledge-synth |
| 5 | Premature optimisation invalidated by Phase-2 learnings | medium (~30%) on matchmaker algo + token state machine | Phase-1 schemas wrong at Phase-2 activation → rewrite despite scaffolding | `confidence: R-low|medium|high` on every dormant spec; R-low specs explicitly anticipate revision; DRR at activation updates post-learning |
| 6 | Team-hire friction ("where do I start?") | medium (~40%) at first hire | onboarding first hire stretches to 14 days | §16 onboarding kit is the answer; 7-day runbook; F.6 cycle explicit; `WHERE-TO-START.md` at repo root |
| 7 | Stub-maintenance burden | medium (~35%) quarterly | CI hooks + templates accumulate cruft | meta-agent quarterly "stub health" audit; deprecate rather than rot; CI hooks carry own `last_reviewed` frontmatter |

---

## §24. Selection Case for Ruslan

**Pick this variant if** Ruslan values "zero rewrite at any gate" over "minimum Phase-1 surface
area"; expects €50K within 6-12 months (else scaffold-rot dominates); reads *"Foundation =
главный актив"* literally not aspirationally; accepts higher Phase-1 cognitive load for Phase-
2/3 transition smoothness; anticipates Phase-3 (USB-C standards, holding federation, multi-roy)
as a real planning horizon; Stage 7 confirms C14 reading (§22 Flag 1).

**Reject this variant if** Ruslan prefers to earn the right to complexity; revenue runway is
uncertain (>12 months to €50K); Phase-1 appetite favours mental-model simplicity over
trajectory optionality; Stage 7 invalidates the role-manifest-layer C14 reading.

**Thesis sentence.** *If Lock 19 is real, then any capability foreseeable at $1T must have a
designed home at $0, because scaffolding costs €0 of compute and retrofitting is unbounded* —
this document is what obeying that axiom from Day 1 looks like across all 15 Stage-6 questions.

---

*END OF VARIANT 2 — AGGRESSIVE-MAXIMALIST*
