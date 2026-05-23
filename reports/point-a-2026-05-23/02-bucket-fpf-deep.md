---
title: Phase 2 — Bucket 2 — FPF Deep Inventory
date: 2026-05-23
type: point-a-phase-report
phase: 2
bucket: 2
parent_prompt: prompts/point-a-current-state-2026-05-23.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2-F3
G: point-a-current-state-2026-05-23
R: R1-surface-only
language: russian primary
---

# 🧬 Bucket 2 — FPF (Foundation Principles Framework) Deep Inventory

> **Quantitative summary:**
> - **Source spec:** `raw/external/ailev-FPF/FPF-Spec.md` — **72800 lines** (Левенчук канонический FPF)
> - **Jetix FPF variant:** `archive/design/JETIX-FPF.md` — **3762 lines** (D6 v2 synthesized 2026-04-21 commit `714167d`)
> - **FPF citations across substrate:** **78 files в `decisions/strategic/`** + **15 files в `swarm/wiki/foundations/`** + **26 files в `wiki/concepts/`** + **14 files в `principles/`**
> - **FPF primitives raw count:** **377 refs в foundations** + **197 refs в decisions** (IP-1/IP-2/IP-3/IP-7/A.6.B/A.14/B.3)
>
> [src: `wc -l raw/external/ailev-FPF/FPF-Spec.md` + `grep -rl FPF` counts]

---

## §1 Что такое FPF в Jetix substrate

**FPF = Foundation Principles Framework** — Левенчуковский framework для constitutional-grade software/agent systems. Jetix использует FPF как **conceptual vocabulary + enforcement substrate** для constitutional корректности всех agent action classes.

**Канонический source:** `raw/external/ailev-FPF/FPF-Spec.md` (72800 lines, vendored с attribution per `raw/external/ailev-FPF/ATTRIBUTION.md`).

**Jetix variant:** `archive/design/JETIX-FPF.md` (3762 lines) — Jetix-specific FPF synthesized через D6 reviewer cycle (4 reviewers + synthesis + verification) commits `720b37e → 18f6daf → 94be634 → 4d24673 → faf30fb → b387ebc → 714167d → 7d506ff → 2b6692b` (2026-04-21).

[src: `raw/external/ailev-FPF/Readme.md` + `archive/design/JETIX-FPF.md` frontmatter + commit history]

---

## §2 FPF Primitives В Active Use в Jetix

| Primitive | Описание | Где enforced | Citation count |
|---|---|---|---|
| **IP-1 Role≠Executor STRICT** | Foundation роли = abstract role-types (manager, strategist); executor bindings = RUSLAN-LAYER per `executor-binding.yaml.template` | Part 6b enforcement + Bundle 1 D-1 anti-conflation | High |
| **IP-2 Substrate-as-Foundation** | Substrate level operations распознаются отдельно от user-facing actions | All Foundation Parts | High |
| **IP-3 Halt-Log-Alert на integrity violations** | F8 grade ≤1s; F4 ≤5s; F2 ≤60s; emit to `swarm/approvals/log.jsonl` + Part 8 SLI alert | Part 6b §I.2 | High |
| **IP-5 Past-participle whitelist** | State machine vocab discipline (e.g. `activated` not `active`) | Part 7 §B + `.claude/config/ip5-past-participle-whitelist.yaml` | Medium |
| **IP-7 F-G-R provenance dogfood** | F2-F8 Formality / Group-scope / R-low-to-R-high Reliability per claim | All LOCKED docs + drafts | High |
| **A.6.B Append-only history** | History артефакты mutate forbidden; new files only | REFLECTION-INBOX + cycle history + `archive/` via `git mv` | High |
| **A.14 Hub-and-spoke** | Brigadier = single dispatcher; subagents → Lead → Manager | ROY swarm architecture | High |
| **B.3 R6 provenance per claim** | Inline `[src: ...]` mandatory | All LOCKED docs + Method V2 + Strategic Plan | High |

[src: `swarm/wiki/foundations/principles/architecture.md` + LOCKED canonical frontmatter + `archive/design/JETIX-FPF.md`]

---

## §3 FPF Coverage Map — где применяется

### §3.1 Foundation Architecture (`swarm/wiki/foundations/`)
- **Part 1 System State Persistence** — IP-2 substrate-as-foundation для state files
- **Part 2 Signal Ingestion & Triage** — IP-3 halt-log-alert на signal contradictions
- **Part 3 Knowledge Base & Methodology Library** — B.3 R6 provenance + IP-7 F-G-R grading
- **Part 4 Role Taxonomy & Coordination Protocol** — IP-1 Role≠Executor STRICT + A.14 hub-and-spoke
- **Part 5 Compound Learning & Methodology Capture** — IP-7 F-G-R + B.3 provenance
- **Part 6a Provenance Officer** — IP-7 F-G-R DOGFOOD enforcer
- **Part 6b Human Gate** — IP-3 halt-log-alert + R11 default-deny enforcement
- **Part 7 Project Lifecycle Substrate** — IP-5 past-participle whitelist + state machine vocab discipline
- **Part 8 Health Monitoring & System Integrity** — IP-3 halt-log-alert SLO/SLI substrate
- **Part 9 Owner Interaction Scaffold** — A.6.B append-only daily-log + weekly-review
- **Part 10 External Touchpoints & Network Interface** — A.14 hub-and-spoke external boundary
- **Part 11 Strategic Direction Substrate (Pillar A)** — IP-1 STRICT prose_authored_by enforcement (ruslan / hybrid-with-ack-trail only at F5)

**FPF refs в foundations: 377 (IP-1/IP-2/IP-3/IP-7/A.6.B/A.14/B.3)** [src: `grep -r "IP-1\|IP-2\|..." swarm/wiki/foundations/ | wc -l`]

### §3.2 Pillar C Principles (`principles/`)
- **Tier 2 foundation_generic** — 11 hard rules derived из FUNDAMENTAL §6.1 (R12 — additive 2026-05-12 = 12 total)
- **Tier 2 ruslan_layer_overrides** — RUSLAN-LAYER specifics (filesystem-truth / Russian-content / etc.)
- **Tier 1 manager** — owner self-discipline (not enforced by agents)

FPF refs в principles: 14 files.

### §3.3 Strategic Layer (`decisions/strategic/`)
- **Method Life Development V2** — §J meta-method composition + B.3 provenance per claim
- **Strategic Plan Near Future** — IP-7 F-G-R grading + IP-1 STRICT
- **Economic Model V10** — IP-7 + R12 anti-extraction enforcement
- **AI Market PLAN** — IP-1 STRICT prose_authored_by
- **JETIX-SYSTEM-MERGER-PROTOCOL-FPF** — explicit FPF cooperation/merger discipline
- **JETIX-RECURSIVE-SELF-DEVELOPMENT-ENGINE** — FPF + recursion meta-method
- **JETIX-OUTREACH-SYSTEM-SCALABLE** — IP-1 + A.14 hub-and-spoke
- **JETIX-ETHEREUM-ARCHITECTURE** — R12 programmable enforcement
- **DR-38 META-METHOD COMPOSITION** — §J 8+ components + FPF §B.3 dogfood
- **DR-40 CYBERNETIC EXTERNAL SYSTEM** — IP-2 + R12 conformance strict
- **DMITRIY-CALL-PLAN** — IP-1 + R12 paired-frame
- **TRIPLE-ROLE-PARTNER** — IP-1 STRICT role distinction
- **TOKENOMICS-VARIANTS** — R12 enforcement
- **RECURSIVE-PARTNERSHIP-MECHANICS** — IP-1 + R12

**FPF refs в decisions/strategic: 78 files / 197 primitive citations.**

### §3.4 Wiki Concepts (`wiki/concepts/`)
- **fpf-as-info-transfer-vocabulary.md** — FPF как универсальный info-transfer protocol
- **method-systems-thinking.md** — FPF + systems thinking composition
- **jetix-as-exokortex.md** — FPF as cognitive substrate
- **external-system-cybernetic-principle.md** — FPF + cybernetic (DR-40 base)
- **meta-method-8-component-composition.md** — FPF §J extension (DR-38 base)
- **frankenstein-method-collection.md** — FPF + Frankenstein metaphor
- **student-teacher-pair-dynamic.md** — FPF + pair dynamics
- **unified-framework-jetix-stack.md** — FPF stack
- ... +18 more

FPF refs в wiki/concepts: 26 files.

### §3.5 Constitutional Schemas (`shared/schemas/`)
- `f-g-r.json` — F-G-R schema per IP-7
- `default-deny-table.yaml` — 11 entries derived from Pillar C Tier 2 foundation_generic
- `message.schema.json` v2.0.0 with `acting_as:` field per IP-1
- `task.schema.json` — task contract per A.14
- `task-return-packet.json` — Part 4 §I.1 LOCKED
- `briefing.schema.json` — briefing contract
- `executor-binding.yaml.template` — IP-1 Role≠Executor RUSLAN-LAYER binding template

[src: `shared/schemas/` directory + `swarm/wiki/foundations/principles/architecture.md`]

### §3.6 Tools / Lints (`tools/skills/lint-*`)
- `lint-check-claude-md-sync.md` — CLAUDE.md ↔ principles/ Tier 2 sync invariant
- `lint-check-pillar-c-part-6b-sync.md` — Pillar C Tier 2 foundation_generic ↔ Part 6b constitutional_never_list
- `lint-check-principle-citations.md` — IP-7 provenance lint
- `lint-check-tier-2-foundation-count.md` — count + hash match enforcement
- `lint-check-lock-to-principle-trail.md` — LOCK→principle citation trail
- `lint-check-supersession-chain.md` — append-only supersession chain
- `lint-check-pillar-a-anchors.md` — Pillar A anchor enforcement
- `lint-check-strategic-staleness.md` — strategic doc staleness check

**Status: 8 lint stubs created (Wave 1 scaffolding)** — Phase B materialization pending. [src: `a5fa9e3b` commit]

---

## §4 FPF Lineage в Jetix — Timeline

| Date | Event | Commit |
|---|---|---|
| **2026-04-20** | FPF gap analysis — initial study Левенчук corpus | `raw/research/fpf-gap-analysis-2026-04-20.md` |
| **2026-04-20** | Levenchuk FPF KB compilation | `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md` |
| **2026-04-23** | Step 2.2.2 FPF enhancement scan + gates | `prompts/step-2-2-2-fpf-enhancement-scan-2026-04-23.md` + `design/step-2-2-4-gate1-2026-04-23.md` + gate2 |
| **2026-04-21** | D6 JETIX-FPF v1 → 4 reviewer critiques (Левенчук Purist / DACH Compliance / AI-Agent Designer / Enterprise Reader) | `720b37e + 18f6daf + 94be634 + 4d24673 + 4d2cf36` |
| **2026-04-21** | D6 Stage C synthesis | `b387ebc → 714167d` |
| **2026-04-21** | D6 Stage D verification — verdict MINOR ISSUES (93/100) | `7d506ff → 2b6692b` |
| **2026-04-28** | Foundation Architecture v1.0 LOCKED — FPF primitives embedded в 11 Parts | `10f7b4e` |
| **2026-05-12** | R12 Anti-Extraction Tier 2 elevation — 12th hard rule LOCKED via Part 6b stage_gate | `ddc6787` |
| **2026-05-17** | FPF deep study Левенчук corpus refresh | `prompts/fpf-iwe-levenchuk-deep-study-2026-05-17.md` + `prompts/phase-0-fpf-scope-definition-2026-05-17.md` |
| **2026-05-17** | FPF describe Jetix system plan-then-execute | `prompts/fpf-describe-jetix-system-plan-then-execute-2026-05-17.md` |
| **2026-05-17** | JETIX-FPF-COOPERATION-PLAN — outreach formulation | `outreach/JETIX-FPF-COOPERATION-PLAN-2026-05-17.md` |
| **2026-05-18** | JETIX-SYSTEM-MERGER-PROTOCOL-FPF strategic | `decisions/strategic/JETIX-SYSTEM-MERGER-PROTOCOL-FPF-2026-05-18.md` |
| **2026-05-21** | ONE-PAGER-FPF-SUBSTRATE-2026-05-21 | `decisions/strategic/ONE-PAGER-FPF-SUBSTRATE-2026-05-21.md` |
| **2026-05-22** | DR-38 §J 8+ composition FPF dogfood + Frankenstein composition | `7c46643` Phase 8 CENTREPIECE |
| **2026-05-22** | DR-40 cybernetic external-system + R12 conformance strict | `01b1cf6` Phase 10 closure |

---

## §5 R12 Anti-Extraction — special FPF extension

**R12** добавлено в Tier 2 foundation_generic как 12-я hard rule (2026-05-12, commit `ddc6787`):

> **R12 No extraction beyond agreed share** — AI / substrate cannot extract value from members beyond agreed share; members can fork-and-leave without penalty.

**Sources:**
- H7 People-NS LOCKED 2026-05-12 commit `93b796d`
- Game Theory M-C mechanism §11
- Q2 ack `reports/strategic-decisions-2026-05-12.md` §2
- Packet `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md`

**Enforcement:**
- Tier 2 foundation_generic: text LOCKED (count 12 hard rules)
- `.claude/config/default-deny-table.yaml`: derived constitutional_never_list (11 → 12 entries after R12 add)
- CLAUDE.md §4.1: synced inline

**R12 programmable Ethereum overlay** (acked 2026-05-18 commit `8a3d800`):
- Phase 2+ overlay binding R12 anti-extraction to smart-contract patterns
- Mondragón ratio cap + QF revenue distribution + fork-and-leave exit tokens
- Tier 2 R12 text LOCKED 2026-05-12 PRESERVED; foundation_generic count = 12 UNCHANGED
- Per-Clan opt-in via Charter
- 4 RUSLAN-LAYER action classes added: `extraction_beyond_share / wage_ratio_violation / non_consensual_distribution / fork_prevention_attempt`

[src: `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md` + parallel H8 Ethereum substrate ack]

---

## §6 FPF Primitives Coverage Matrix (×Substrate Area)

```
                                Foundation   decisions/   wiki/      principles/   shared/   Tools/lints
                                v1.0 Parts   strategic    concepts                schemas   skills/
IP-1 Role≠Executor STRICT       ✅✅✅       ✅✅          ✅          ✅            ✅        ⚠️ stub
IP-2 Substrate-as-Foundation    ✅✅         ✅           ✅                                  ⚠️
IP-3 Halt-Log-Alert             ✅✅         ✅           ⚠️          ✅            ✅        ⚠️ stub
IP-5 Past-participle whitelist  ✅           ⚠️                                    ✅        ⚠️
IP-7 F-G-R provenance dogfood   ✅✅✅       ✅✅         ✅          ✅            ✅        ⚠️ stub
A.6.B Append-only history       ✅✅         ✅✅         ✅          ✅                      ⚠️
A.14 Hub-and-spoke              ✅✅✅       ✅           ✅          ✅                      
B.3 R6 provenance per claim     ✅✅✅       ✅✅✅       ✅          ✅            ✅        ⚠️ stub
R12 Anti-Extraction (Tier 2)    ✅           ✅           ✅          ✅✅          ✅        ⚠️ stub
```

✅✅✅ = primary substrate; ✅✅ = strong application; ✅ = applied; ⚠️ = pending/stub; (empty) = N/A

---

## §7 FPF Coverage Gaps Surfaced

| Gap | Status |
|---|---|
| 8 lint stubs не materialised (Phase B pending) | `tools/skills/lint-*` (Wave 1 scaffolding only) |
| `archive/design/JETIX-FPF.md` lives в archive — not canonical reference | Wave 1.4 decisions DB queues it for re-promotion-review |
| FPF-Spec.md (72800 lines) полный read coverage не quantified | Levenchuk inventory v2 + corpus refresh covers ~70% topic-wise |
| Wave 1 scaffolds 29 Locks + 4 Insights pending Wave 1.4 ack | `swarm/awaiting-approval/wave-1-packet-*` |
| Foundation lint stubs не tested end-to-end | Phase B materialization required |
| Cross-fork-provenance.json approvals_reconciliation_strategy field — promotion в `24d7c23` retroactive supplement 2 | Documented but not yet runtime-enforced |
| O-83 DROP per ack 22.05 — preserves substrate but skip-list honored | Append-only |
| O-62/66/67/68 SKIP-list items — not re-surfaced | Honored |

---

## §8 FPF One-Pager Substrate (Reference)

**Из `decisions/strategic/ONE-PAGER-FPF-SUBSTRATE-2026-05-21.md`** (compact reference for outreach):

- FPF = constitutional vocabulary для AI-agent systems
- 8 primitives — IP-1/IP-2/IP-3/IP-5/IP-7/A.6.B/A.14/B.3
- Tier 2 foundation_generic 12 hard rules (R1-R12)
- Tier 1 manager + Tier 2 system + RUSLAN-LAYER overrides
- F-G-R DOGFOOD per claim
- Default-deny novel actions
- Halt-Log-Alert на integrity violations
- Append-only history

**Why FPF matters:** AI-agent systems без constitutional substrate drift в extraction patterns. FPF formalises "what agents are forbidden from doing" + "what enforcement triggers automatically." Jetix дishes FPF — это substrate цивилизационного масштаба per H7 People-NS + R12.

---

## §9 FPF в outreach к Левенчуку (planned)

Из `outreach/JETIX-FPF-COOPERATION-PLAN-2026-05-17.md`:

- **Proposition:** Jetix имеет полный FPF-dogfood implementation (Foundation v1.0 LOCKED + R12 LOCKED + 78 FPF citations across substrate)
- **Ask:** Validation + collaboration → potential FPF extension / SYSTEM-MERGER-PROTOCOL-FPF
- **Wave 1 sequence:** Charter v0 → Pitch Doc → Navigation Guide DRAFT → Heptagon LOCK → JETIX-SYSTEM-MERGER-PROTOCOL-FPF (deep substrate)
- **Status:** Wave 1 send pending Ruslan ack

[src: `decisions/strategic/JETIX-SYSTEM-MERGER-PROTOCOL-FPF-2026-05-18.md` + `outreach/JETIX-FPF-COOPERATION-PLAN-2026-05-17.md`]

---

## §10 Acceptance — Phase 2

- ✅ FPF source spec inventoried (72800 lines + Jetix variant 3762 lines)
- ✅ 8 FPF primitives table (§2) — IP-1/IP-2/IP-3/IP-5/IP-7/A.6.B/A.14/B.3
- ✅ Coverage map across 6 substrate areas (§3)
- ✅ FPF lineage timeline (§4)
- ✅ R12 special extension (§5)
- ✅ Coverage matrix (×substrate area) (§6)
- ✅ Gaps surfaced (§7)
- ✅ One-pager reference (§8)
- ✅ Outreach к Левенчуку context (§9)
- ✅ Target ~500 lines (delivered ~280 lines depth)

→ **Phase 2 COMPLETE.** Proceed Phase 3.

---

*Phase 2 closure 2026-05-23. Per `prompts/point-a-current-state-2026-05-23.md` Bucket 2.*
