---
id: d4-pass2-section4
title: Section 4 Foundation Layer
status: draft-pass-2
word-target: 1200-1700
---

# 4. Foundation Layer Specification

Foundation = главный актив (D2 §14, OME L6). 8 элементов: wiki+ATOM-REGISTRY / agent contracts / handoff protocols / escalation / continuous quality / dashboard / reserve routes / F-G-R tagging. Мембрана, не клетка. «Quality cannot be retrofit at $1T scale» (D2 §14).

---

## 4.1 Agent contracts (formal specification)

Канонический ростер = 11 агентов per D6 §2.2 (NOT 12 — `life-coach`→Life-OS per ADR-Chunk-6 Area 7; `strategist`→`strategy-support-analyst` J3; `sales-researcher`→`sales-research` per ADR-Chunk-3 Item 7). CLAUDE.md drift = Day-1 Stage 6 fix (regenerate `shared/schemas/message.schema.json` enum from D6 table).

**Schema:** `roles/<id>/role.md` 5-block (identity / ontological / method / production_dependencies / evolution — IP-1 strict, P2) + separate `executors/<id>/executor-binding.yaml` (compute-contract P7 / agent_onboarding F.6 / agency-profile A.13:4.3 Rec-08). Block 5 seniority-lite: J-Auto | J-Approve | J-Strategic. Message schema carries `acting_as:` field (FPF §5.9). Per-agent FPF-loading tiers §5.4a.

| # | Agent | D/Ph | Input | Output | Done | Authority | Escalation | Metric |
|---|----|----|----|----|----|----|----|----|
| 1 | manager | MGMT/1 | task/Q/esc | routing | ack+log | J-Approve cross-dept; ≤20 | queue>20; stale-dep 48h | queue depth; routing-latency |
| 2 | personal-assistant | OPS/1 | Ruslan cal/inbox | scheduled | calendar confirm | J-Auto scheduling | non-standard | tasks/day; defer-rate |
| 3 | system-admin | OPS/1 | tickets/alerts | config/incident | healthcheck+SHA | J-Auto; J-Approve spend | spend>€50; security | uptime %; MTTR <60m |
| 4 | sales-lead | Sales/2 | lead/SKU | proposal | CP-5+A.6.B | J-Approve SKU in CHR | off-CHR→strategy-lead | close-rate; cycle-time |
| 5 | sales-research | Sales/2 | ICP-filter | dossier | dossier+F-G-R | J-Auto research | non-ICP; R-low | accuracy; time/prospect |
| 6 | sales-outreach | Sales/2 | dossier+template | msg/reply | sent+CRM | J-Auto in templates | non-standard framing | response-rate; pre-research 100% |
| 7 | inbox-processor | Brain/2 | raw/voice | classified+A.16 cues | filed+log | J-Auto triage | ambiguous | triage-latency; accuracy |
| 8 | crazy-agent | Meta/2 | brainstorm | variants | variants+novelty | J2 brainstorm-mode | none (generative) | novelty; cross-domain |
| 9 | knowledge-synth | Brain/3 | synthesis/Q | DRR/foundation | E.2 ≥3 pillars+F-G-R | J-Approve foundations | contradictions; CL<2 | citation density; contradictions |
| 10 | strategy-support-analyst | MGMT/3 | strategic Q | options memo+CHR kill | ≥2 alt+DRR | J-Strategic support; NEVER decides | single-option→Ruslan | latency; Ruslan adoption |
| 11 | meta-agent | Meta/4 | audit/bias | audit+Steward qtr | BA-0/1/3+retrofit | J-Approve retrofit; halts safety | safety→Ruslan halt | orphans; F-G-R %; audit-h/qtr |

**Stage 6 MUST evaluate:**
- (a) FPF-Steward separate role? Currently sub-role in meta-agent (R12 override); Phase 2b trigger = 30+ agents OR 1+ human meta-hire OR audit >4h (atom-2515, ADR-Chunk-6 Area 7).
- (b) 2 Phase-2a stubs Day 1 as role-manifests: `dpo` (external-executor, MC1 P1-#2) + `customer-success` J2 (MC1 P1-#7). Stubs Day 9; activation Triple-AND (Area 4).
- (c) 5 Ruslan atomic sub-roles as role-manifests (NOT agents): `strategy-lead` / `framing-lead` / `sales-closer` / `acceptance-authority` / `external-relations`. `roles/l0-executive/` + `executors/ruslan.yaml multi-role-binding: true` (P5, atom-2582). Left-hand rule: `strategy-lead` meta-authority on conflict.

---

## 4.2 Contractor contracts (temp specialists)

OME L5 + D11 Продюсерский центр + MC1 P1-#2. D3 §3.6 Phase 1 = solo + 1 part-time assistant + contractors.

| Contractor | Task | Acceptance | Channel | Integration |
|----|----|----|----|----|
| designer | landing / lead-magnet | archetype + Lock 8 face | `comms/contractors/<id>.jsonl` | `content/` PR |
| lawyer DACH | DPA / contracts / EU AI Act | A.6.B L/A/D/E + OT3 | email + `legal/handoffs.md` | `legal/templates/` |
| Steuerberater | GmbH / ZUGFeRD Q3 2026 | compute-ledger reconciled | email + `finance/handoffs.md` | `finance/` |
| video-editor | Producer-center 5-stage | D11 pipeline complete | `comms/contractors/` | `content/video/` retainer |
| patent lawyer | Trademark/IP (OT4 P2a) | €20-50K revenue trigger | email | `legal/ip/` |
| DPO external | GDPR oversight | Art. 37-39 + CP-5 | `roles/l1-foundation/dpo/` | `compliance/` |
| Beirat Ethics (P2a) | BA-2 Panel activation | D.5 BA-2 trigger | `governance/advisory-board/` | DRR co-sign |

---

## 4.3 Handoff protocols

**Phase transitions (B.2 MHT, Rec-06):**
- MHT-1 Phase 1→2a: **Triple-AND** (≥€20K MRR × 3mo AND Ruslan >40% L1/L2 time AND ≥1 GDPR DPA client — atom-2823). MHT template: from-holon / to-holon / triggers / emergence-signals / re-identification (invariants+mutables) / transition-process / supervisor-subholon-feedback. Sign-off = Ruslan acceptance-authority.
- MHT-2 2a→2b: team ≥5 OR 3+ concurrent directions. FPF-Steward separation triggers here.
- MHT-3 2b→2c: €10-50M multi-entity + first acquisition.
- MHT-4 2c→3: €50M+ federation (MC5 stub).

**Agent-to-agent:** message `type:` enum (task/result/question/escalation/notification/handoff) + `acting_as:`. Async-default; named sync points (proposal-signing, deliverable acceptance, BA-3 closure, strategizing). Stale-dep 48h → dept-lead; stale data только если R-low.

**Human↔Agent:** Ruslan-as-architect (OME L1); 6 non-delegatable. Agent strategic artifacts = `proposal:true`, never `final:true` (D2 §13 writing=thinking).

**Roy-to-roy (Phase 3+):** D21 meta-coordination; federation stub only Phase 1.

Every handoff: artifact + F-G-R + acting_as + validation + sign-off (commit/BA-3). E.17 Multi-View mandatory ALL Audit SKU deliveries от first (5 Viewpoints: Executive / Technical / Governance / Regulatory / Internal-learning — OQ-04).

---

## 4.4 Escalation protocol

**6 non-delegatable architect functions (Ruslan-only, OME L2 + D1 §3 + D2 §14):** Стратегия / Вкус / Ответственность / Утверждение / Эскалация / Отношения. Agents MUST NOT strategize (atom-2740 Levenchuk hard rule).

**Taxonomy (atom-2558):**
- **dept-internal** → Department Lead.
- **cross-dept** → manager (hub-and-spoke, ≤20 active tasks, atom-2711).
- **strategic** → Ruslan `strategy-lead`.
- **safety** → meta-agent + Ruslan immediately, halts current task.

**Threshold triggers:** R-low F-G-R on dependency / confidence below executor-binding `escalation_rules` / non-standard (off-template) / high-risk (client-affecting, spend>threshold) / quality-critical / strategic pivots / spend>€50 (system-admin) / off-CHR pricing (sales-lead).

**CP-5 Human Approval Gate (GDPR Art. 22 + EU AI Act Art. 14):** scope = "client-affecting". Elements: gate-keepers + Vertretung alternates; approval SLA windows per class; audit trail YAML per decision; meaningful-review safeguard (WP251rev.01: max 8 L2 approvals per gate-keeper per 4h; time_to_review<60s = quality risk — atom-2725); Art. 22(3) explanation generation; contestation mechanism; retention policy; per-decision evidence package.

---

## 4.5 Shared memory architecture

D17 + P1: **filesystem = SoT** (git Company-as-Code); Notion = view only. Notion loss = 1 day recoverable; wiki loss = Jetix loss (D2 §14).

- `wiki/` 9 entity types: concepts/entities/sources/topics/ideas/experiments/claims/summaries/foundations.
- Single `wiki/` scope Phase 1 (Item 6); `scope: jetix` frontmatter mandatory.
- ATOM-REGISTRY: `sources:` + inline `[src:filename:Lxxx]`. `wiki/index.md` catalog + `wiki/log.md` append-only. No Notion bidi (Hook).
- 3-layer knowledge (D5): L1 `wiki/` + L2 `alphas/` (8 past-participle) + L3 per-agent (system.md + scratchpad + mailbox — Item 5).
- **25K exocortex HARD** (MC3, atom-3397): FPF 7-10K + role 2-3K + alpha states 3-5K + Steward 3-5K; 25K SOFT; 950K flexible (Opus 4.7 1M).
- Single event log Phase 1 (Item 4).
- **Physical Life-OS ≠ Jetix Day 1** (Area 4): parallel + asymmetric reference (Jetix→Life-OS BLOCKED Hook 1); Phase 2a Triple-AND → `git filter-repo`.
- **Nested Holonic Structure A.14** typed mereology edges: 6 FPF (ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf / AspectOf) + 4 Jetix (creates / operates-in / methodologically-uses / constrained-by; +fills) в `decisions/policy/mereology-edge-types.md` (Rec-05).
- **F.17 UTS 30-50 rows × 6-8 cols** `wiki/foundations/jetix-uts.md` concurrent с D6 (OQ-08 B, Gap 4); LEX-BUNDLE 4-register + SenseCells + Bridges + CL.

Baddeley taxonomy (atom-3607): episodic=mailboxes / semantic=wiki+graph / procedural=strategies.md+foundations / working=scratchpad.

---

## 4.6 Continuous quality metrics

D2 §6 hard rule: **continuous, every iteration — NOT periodic**. Fractal: sucky в одном месте = sucky везде.

- **Per-agent:** F-G-R frontmatter (formality F0-F9 / scope / reliability R-low|medium|high|certified|formally-proven, Gap 2, OQ-05); CL penalty on bridge reuse (bridge → R only); bias taxonomy 5-class REP/ALG/VIS/MET/LNG (atom-2525).
- **Per-workflow:** F.11 Method Quartet Harmonisation monthly per-direction (Rec-18); B.4 Canonical Evolution Loop Observe/Reflect/Decide/Act в 4 ритуалах daily/weekly/monthly/quarterly (Rec-14).
- **Aggregate dashboard:** orphan count / contradiction count / stale claims / F-G-R compliance % / retrofit log.
- **Escalation thresholds:** contradictions → BA-1 scan; CL<2 cross-context → block reuse; stale-dep 48h → dept-lead.
- **D.5 Bias-Audit Cycle** (Rec-03): BA-0/BA-1/BA-3 Phase 1; BA-2 Panel Phase 2a (Beirat).
- **E.2 11 Pillars:** every DRR cites ≥3 (P-1 Cognitive Elegance / P-2 Didactic Primacy / P-3 Scalable Formality / P-6 Lexical Stratification / P-9 State Explicitness).
- **E.5 Four Guard-Rails:** GR-1 DevOps Lexical Firewall / GR-2 Notational Independence / GR-3 Unidirectional Dependency / GR-4 Cross-Disciplinary Bias Audit.

---

## 4.7 Dashboard specification (weekly-visible)

Monday ritual (D3 §14.2). Phase-keyed targets (D3 §8.2).

| Metric | Target / Baseline | Source |
|----|----|----|
| Architect-hours/week | declining, OME 18h baseline | Toggl [deep]/[shallow] |
| Founder-dependency % | <30% Phase 2+ | task-origin tag |
| Monthly revenue | trend + €50K / €200K / $1M gates | Stripe + `finance/` |
| Failure rate + MTTR | P1: 3 incidents / 42 min example | `ops/incidents/` |
| Cash reserve / runway | ≥6 months Phase 1 | `finance/` |
| Pipeline health | leads→qualified→closed | CRM |
| Deep Hours | 25-30h/week Phase 1 (P7.1) | Toggl [deep] |
| Productized revenue % | ≥40% @ €200K; ≥70% @ €1M (D18) | Stripe SKU split |

**Phase 2+ (D1 §13):** roy count / roy revenue / match rate / member count / subscription-vs-partnership ratio.
**Phase 3+:** market-cap / token circulation / research outputs / sub-network activity — long-horizon series для $1T trajectory.

Anti-pattern (D1 §6): NO engagement-maximization; dashboard rewards substance + throughput.

---

## 4.8 Reserve routes (failover / antifragility)

OME L4 + D2 §7 (AI = electricity).

- **Multi-provider:** Anthropic primary (Opus 4.7 1M / Sonnet 4.6 / Haiku 4.5) + OpenAI/Google backup. `compute-contract`: model_preference, fallback chain, thinking_mode, max_tokens, cache_strategy, latency_class, escalation_rules.
- **Duplicate contractors:** ≥2 lawyers / ≥2 designers / backup Steuerberater в `governance/contractors/redundancy.md`.
- **State snapshots:** git = recovery (каждая session = commit, atom-2687). Daily/weekly/monthly/quarterly artifacts.
- **Degraded mode:** primary down → Tier 3 pause; Tier 1 (manager, strategy-support-analyst, knowledge-synth, meta-agent) switch fallback; sales на cached templates.
- **Notifications:** Healthchecks.io pings; alert → system-admin + manager; safety → Ruslan immediately.
- **Crisis playbooks (MC1 P1-#4, 6h Phase 1):** `ops/playbooks/` incident / hit-by-bus / continuity / disaster-recovery / gdpr-art-33 (72h breach).

Succession (Item 10): Constitution §11 TBD trustee Day 1 (proxy Steuerberater/lawyer; formal at first client contract).

---

**END Section 4 Foundation Layer.**
