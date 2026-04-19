---
type: research-synthesis
version: v2-final-post-review
stage: 2 of 6 — Multi-chat Expert Review (synthesis)
status: ready-for-ruslan-stage-3
owner: ruslan
author: claude-opus-4-7-synthesizer
created: 2026-04-19
input:
  - raw/research/architecture-implementation-synthesis-2026-04-19.md (v1, 1592 строки)
  - raw/research/stage2-review/review-critic.md (~5491 слов)
  - raw/research/stage2-review/review-simplifier.md (~5836 слов)
  - raw/research/stage2-review/review-megacorp.md (~4756 слов)
  - raw/research/stage2-review/review-levenchuk.md (~5231 слов)
output-target-length: 12000-18000 слов
next-stage: Stage 3 — Ruslan review v2 + approve / edit
blocks: D1-D9 чистовики (Stage 4)
---

# Architecture Synthesis v2 (Final Post-Review)

> Integrated architecture recommendation post 4-reviewer expert review.
> Diff-tags используются: **[+v2 NEW]**, **[Δv2 CHANGED]**, **[−v2 REMOVED]**, **[=v1 UNCHANGED]**.
> Каждое изменение vs v1 fully sourced к conkretnym reviewer feedback.

---

## 📖 Executive Summary

**[Δv2 CHANGED — refined per Critic Concern #1, Simplifier #1-3, Mega-Corp Concern #1-3, Левенчук systemic dilution audit]**

Jetix — это AI-native mega-corporation одного founder'a (Ruslan, Берлин), спроектированная **с Day 1 на scale-up без architectural rebuild**, но с **honest separation между "Reference Architecture" (mega-corp долгосрочный target) и "Operational Architecture" (Phase 1 minimum viable execution path)**. Это центральное уточнение vs v1: v1 over-committed scaffolding во всех слоях; v2 удерживает mega-corp ambition как design-time принцип, но материализует Phase 1 как **MVP с предзаложенными швами для расширения** — каждое расширение additive, без rebuild.

Девять research-волн (R1–R9, ~66K слов) сходятся на **семи финальных принципах** (один новый vs v1):

1. **Company-as-Code, буквально.** Git = SoT. [=v1]
2. **Role ≠ Executor.** [Δv2] *Применяется ontologically-clean*: implementation_ai/human extracted в `executors/<id>/binding.yaml` (per Левенчук §1.1 Concern #1); role.md содержит pure role contract; «portability» признаётся как **roadmap goal**, не v1 property (per Critic Concern #2). v1 hardcodes claude-opus-4-7 в Block 6 принимаются как Phase 1 reality с explicit "Claude-Code-coupled in v1" disclaimer.
3. **6 true alphas + 3 work products + 1 entity** [Δv2 — was 10 alphas]. Per Левенчук §1.2 Concern #1-3: Invoice = work product, SKU = entity, Postmortem = work product. **Way of Working** added as 7th true alpha. Past-participle convention strict-enforced (52% v1 violations fixed per audit table).
4. **Модель D Nested Hierarchy финально.** [=v1] *С one ontological honesty addition* (per Левенчук Part 2 mereology concern): «Lightweight mereology — Jetix-as-part-of Life-OS — explicit принцип; advanced mereology (Kit Fine, constructor theory) excluded.»
5. **L0 Executive Core** [=v1 базово] *с three additions* (per Mega-Corp Concern #1, Левенчук §1.4 Concern #2):
   - Strategic-management декомпозируется на 5 atomic sub-roles (strategy-lead, framing-lead, sales-closer, acceptance-authority, external-relations) с single executor `ruslan` filling все 5;
   - Agent `strategist` renamed → `strategy-support-analyst` (avoids Левенчук-violation: agents не стратегируют);
   - Bus-factor mitigation: explicit `ops/hit-by-bus.md` + designated trustee (Anton).
6. **DACH-context hard-coded.** [=v1] *С honesty addition* (per Mega-Corp Section 3.2): «DACH-locked в Phase 1-2; cross-border patterns documented as Phase 3 expansion option, не committed.»
7. **[+v2 NEW] Capital + Hours + Attention accounting** elevated to first-class principle. Phase 1 — solo Toggl-based; Phase 2 expansion; Phase 3 ecosystem. *Не materialized as folder в Phase 1*.

**[+v2 NEW] Что значит «Reference vs Operational» split.** D1 теперь содержит две подсекции: «Reference Architecture» (полная 7-слойная картина для mega-corp ambition, design-time коммитмент) + **«Phase 1 Minimum Viable Architecture»** (4 layers materialized: L0 Executive Core / L1 Foundation / L2 Cognitive (читательская дисциплина, не папки) / L4 Delivery; L3/L5/L6/L7 — schema-only stubs до триггеров). Это resolves meta-conflict #1 (Critic vs Mega-Corp).

**Top 5 conflicts resolved** *(полный list в Part 0.3, top-5 highlighted here)*:

- **C1. Scaffolding vs execution priority (Critic vs Mega-Corp)** → 7+7 day rollout split (sales infrastructure days 1-7, foundation days 8-14). Acknowledges Critic Concern #1 без abandoning Mega-Corp scale-up commitment.
- **C2. Folder count 22 vs 8 (Simplifier vs Mega-Corp)** → 8 folders Day 1 + explicit «trigger-driven extension» list. Adds `entities/jetix-gmbh/` + `governance/advisory-board/` + `ops/` per Mega-Corp P1 priority changes.
- **C3. Role-manifest 8 vs 4 blocks (Simplifier vs Левенчук)** → 5 blocks MVM Phase 1 (identity / ontological / method / production_dependencies (renamed per Левенчук §1.3) / evolution); blocks 5/6/7 lifted *из role.md* в separate files (`executors/<id>/binding.yaml` per Левенчук §1.1, `seniority` deferred per Simplifier).
- **C4. 10 alphas vs 4 (Simplifier vs Левенчук)** → **6 true alphas** (Client, Project, Deal, Content Item, Hypothesis, Member) + Way of Working (added) = 7 true alphas Phase 1, состояния past-participle.
- **C5. Bus factor — accept vs mitigate (Simplifier vs Critic+Mega-Corp)** → Mitigate с lightweight artifact (`ops/hit-by-bus.md` 1 page, ~2 hours, designated trustee Anton). Не over-engineer, но не accept existential risk.

**Top 5 open questions для Ruslan** [Δv2 — refined per all 4 reviewers]:

1. **Strategic-management decomposition** — 5 atomic sub-roles (Левенчук-correct) или monolithic (founder-mode flexible)? *Recommendation:* hybrid — 5 manifests, executor `ruslan.yaml` permitted multi-role binding flag.
2. **First human hire timing** — fixed criteria (Critic) or judgment call (Simplifier)? *Recommendation:* triple-AND criteria (3 mo ≥€20K MRR + Ruslan >40% time на L1/L2 ops + ≥1 client requesting GDPR DPA).
3. **`entities/jetix-gmbh/` namespace** — scaffolding now (Mega-Corp P1, 4h cost) или Phase 2c emergence (Simplifier seam-only)? *Recommendation:* scaffolding now — 4h cost vs 80h re-architecture.
4. **Bilingual frontmatter** — Russian-only vs Russian+English mandatory (Mega-Corp P1)? *Recommendation:* English mandatory in `policy/`, `decisions/`, `roles/`; Russian default elsewhere; full bilingual at first non-Russian hire.
5. **FPF-Lite token-budget treatment** — full text in every system prompt vs reference-only (Critic Weakness 6.1)? *Recommendation:* reference-only — agents имеют 1-paragraph FPF-Lite summary + link; full text — meta-agent context only. Saves ~3-5K tokens per agent invocation.

**Что изменилось vs v1** (high-level — full diff в Part 0):

- **Folders:** 22 top-level в `jetix/` → 11 (8 Simplifier-baseline + 3 Mega-Corp P1 additions: `entities/`, `governance/`, `ops/`).
- **Alphas:** 10 → 7 true alphas (added Way of Working; demoted Invoice/SKU/Postmortem to work-products/entities).
- **Role-manifest:** 8 blocks → 5 in `role.md` + executor-binding extracted.
- **Career levels:** 7 (J0-JX) preserved as **reference framework**, but Phase 1 operationally collapses к 3 levels (J-Auto / J-Approve / J-Strategic) per Simplifier.
- **Tools:** 14 → 5 Phase 1 (per Simplifier baseline) + Healthchecks.io.
- **Rollout:** 14-day Foundation-first → 7+7 split (sales 1-7, foundation 8-14) per Critic.
- **FPF-Lite:** 3-5 pages preserved (per Левенчук honest-subset), но reference-only loading per Critic. Past-participle audit applied. U-Types Lite 4 → 6.
- **NEW artifacts:** `ops/incident-playbook.md`, `ops/hit-by-bus.md`, `ops/business-continuity.md`, `entities/jetix-gmbh/` stub, `governance/advisory-board/`, DPO role-manifest stub, succession protocol Constitution §11.
- **NEW Part 0** — explicit changelog (this section).
- **NEW Part 7** — «Phase 3 Architecture Roadmap» honest list of «what we know we'll need to add later».

**Risk-acknowledgments embedded throughout** (per Critic Concerns):
- **Bus factor = 1** — мitigated lightweight, не invalidated.
- **Portability claim** — explicitly downgraded to «roadmap goal v2.0+».
- **Cost model** — added Section 8.3.
- **EU AI Act tier** — Section 7.5 added per Critic Hidden Risk #7.
- **Steuerberater SPOF** — backup pattern added per Critic Hidden Risk #5.
- **Trademark risk (Disney Jetix)** — flagged in Open Questions.

**Что происходит после v2.** Stage 3 — Ruslan reviews v2, approves/edits/rejects per-area. Stage 4 — D1-D9 чистовики написываются с v2 как input. Stage 5 — execute 7+7 day rollout. Stage 6 — Phase 1 deploy + iterate.

---

## Part 0 — Changes from v1 (NEW SECTION)

**[+v2 NEW SECTION]** Эта section существует исключительно для Ruslan'а — explicit diff между v1 и v2, с rationale и reviewer-citations. Если что-то rejected from review — explicit explanation.

### 0.1 Accepted recommendations (38 changes)

| # | Change | From reviewer | Applied to Area | Rationale |
|---|--------|---------------|-----------------|-----------|
| 1 | Reduce 10 alphas → 7 true alphas (Client, Project, Deal, Content, Hypothesis, Member, **Way of Working** [+new]) | Левенчук §1.2 #1-3 | Area 5 | Invoice = work product, SKU = entity, Postmortem = work product per Essence definition. Way of Working alpha added because Jetix IS R&D on its own methodology. |
| 2 | Past-participle convention systematic rename | Левенчук §1.2 #4 | Area 5 | 52% violations fixed: `negotiating → in-negotiation`, `validating → under-validation`, `delivery → delivered`, `at-risk → flagged-at-risk`, `draft → drafted`, `in-progress → started`, `active → activated` |
| 3 | Extract `implementation_ai` + `implementation_human` из role.md → `executors/<id>/binding.yaml` | Левенчук §1.1 #1 | Area 3 | Pure role abstraction; multiple executors per role expressible; v1 mixed role/executor in single file |
| 4 | Decompose `strategic-management` Ruslan-role на 5 atomic roles | Левенчук §1.1 #2 + Mega-Corp Q2 + Critic Q4 | Area 3, 7 | strategy-lead / framing-lead / sales-closer / acceptance-authority / external-relations; single executor `ruslan` fills все 5 |
| 5 | Forbid dynamic role assignment | Левенчук §1.1 #3 | Area 3, 6 | FPF-Lite §5 explicit principle; out_of_scope prevents agent self-role-switching |
| 6 | Rename Block 4 `graph_of_creation` → `production_dependencies` | Левенчук §1.3 | Area 3 | Honest naming: this is bipartite supplier chart, not ШСМ creation graph. Add separate `jetix-creation-graph.md` artifact (3-level mereological) in D6 |
| 7 | U-Types Lite 4 → 6 (add U.Objective, U.Decision) | Левенчук Part 2 | Area 6 | Without U.Objective cannot model purpose hierarchy; without U.Decision cannot model decision-making as object |
| 8 | Strategizing — событие, не ceremony | Левенчук §1.4 #1 | Area 6, 8 | Monthly check = trigger detection only, not session. `strategizing/<trigger-slug>-YYYY-MM-DD.md` not date-first |
| 9 | Rename agent `strategist` → `strategy-support-analyst` | Левенчук §1.4 #2 | Area 7 | R3 §F.7: agents не стратегируют. Honest naming. Career mapping J3 (not J4) |
| 10 | Add «What ШСМ is NOT» section в FPF-Lite | Левенчук Part 5 | Area 6 | Защита от software-language colonization: ШСМ роль ≠ software class, ШСМ alpha ≠ DB table, etc. |
| 11 | Hard reservation 25K tokens for exocortex | Левенчук Part 3 #1 | Area 5 | Never compress durable knowledge (system/strategies/role/FPF). State layer 25K soft. |
| 12 | Add `agent_onboarding` field в executor binding | Левенчук Part 3 #2 | Area 3 | initial_context_pack + warm_up_tasks + calibration_checkpoint. AI agents = new participants of master class (МИМ-2026) |
| 13 | Add `reasoning_examples` optional field в Block 3 | Левенчук Part 3 #3 | Area 3 | Worldview pattern, not just rules. Anthropic Constitution 2026 |
| 14 | Lightweight mereology explicit в FPF-Lite | Левенчук Part 2 | Area 6 | Acknowledge Model D nested as mereological pattern (honest); advanced mereology stays excluded |
| 15 | Reduce jetix/ folders 22 → 11 (8 Simplifier baseline + 3 Mega-Corp P1) | Simplifier #3 + Mega-Corp #1, #3, #4 | Area 2 | 8 baseline (agents/, alphas/, clients/, wiki/, decisions/, evals/, docs/, finance/) + 3 scale-up scaffolding (entities/, governance/, ops/) |
| 16 | Combine roles+executors+agents → `agents/<id>/` | Simplifier #4 | Area 2 | Холакраси-decoupling overkill для AI; binding.yaml separates role contract from executor reality |
| 17 | Combine policy+strategizing+postmortems+letters+weekly+okrs → `decisions/<type>/` | Simplifier #5 | Area 2 | Same epistemological genre; tags в frontmatter (type: postmortem|letter|weekly|okr|strategy|policy|adr|rfd) |
| 18 | Defer `comms/`, `state/`, `sales/`, `templates/`, `processes/`, `products/` | Simplifier Part 3 trigger table | Area 2 | Re-add when ≥3 real artifacts justify directory existence |
| 19 | Per-agent memory 5 layers → 3 (system+scratchpad+mailbox; strategies merged inline; niche/ deferred) | Simplifier #7 | Area 5 | strategies = 1-2 paragraphs at end of system.md; niche/ = 1 (общая wiki/) до 6+ agents с разной reading diet |
| 20 | Wiki niches 6 → 1 | Simplifier #12 | Area 5 | Subdivision premature; re-add Phase 2 |
| 21 | Wiki edges 9 → 3 (related/supports/contradicts) | Simplifier #13 | Area 5 | Other 6 abstract до wiki не разрастётся в graph problem |
| 22 | Wiki skills 5 → 2 (/ingest, /ask) | Simplifier #14 | Area 5 | /lint, /consolidate, /build-graph triggered at scale (500+ orphans) |
| 23 | Single event log Phase 1 (`alpha-log/YYYY-MM.jsonl`) — drop per-alpha history.jsonl | Simplifier #1 + Critic Weakness 5.4 | Area 5, Conflict 3 | Dual-write premature for €0 phase; git log per-alpha provides locality; re-add при context loading >50K consistently |
| 24 | Career ladder J0-JX preserved as **reference**; Phase 1 operationally J-Auto/J-Approve/J-Strategic | Simplifier #8 | Area 7 | Bridge между ontological completeness и operational simplicity. 5-line `decision_rights` list per role replaces 13×6 matrix |
| 25 | Tools 14 → 5 (+ Claude Code) | Simplifier Part 5 | Area 8 | git+GitHub, Claude Code, SOPS+age, restic→Backblaze B2, Healthchecks.io free tier. Drop Promptfoo CI / Langfuse self-host / MkDocs / Coolify / Uptime Kuma / Sentry / Netdata / Vale / markdownlint / lychee Phase 1 |
| 26 | Replace Promptfoo+Langfuse дуэт с **manual eval Phase 1** + Langfuse cloud free tier | Simplifier #11 + Critic Open Q5 + Open Q5 | Area 8 | 5 cases в неделю manual = 30 min, returns clear failure modes; cloud zero-ops |
| 27 | 14-day rollout → 7+7 split (sales 1-7, foundation 8-14) | Critic Weakness 8.5 + #2 | Area 8 | Inverts priority correctly: €0→€50K trajectory requires sales infrastructure; foundation has zero value if no clients |
| 28 | Add `ops/incident-playbook.md`, `ops/hit-by-bus.md`, `ops/business-continuity.md`, `ops/disaster-recovery.md`, `ops/regulatory-incidents/gdpr-art-33-playbook.md` | Mega-Corp #4 + Critic Concern #3 | NEW Area 10 | Bus factor mitigation lightweight; risk-mitigation очень высокая; ~6h Phase 1 cost |
| 29 | Add `entities/jetix-gmbh/` namespace stub | Mega-Corp #1 | Area 2, NEW Area 9 | 4h Phase 1 cost prevents 80h Phase 2c re-architecture for multi-entity federation |
| 30 | Add `governance/advisory-board/` formalization | Mega-Corp #3 | Area 2, NEW Area 9 | members.yaml (Anton, Vladislav, Rodion); placeholder beirat/, aufsichtsrat/. 2h |
| 31 | Add `roles/l1-foundation/dpo/role.md` external-executor mode | Mega-Corp #2 | Area 3, 7 | BDSG §38 trigger 20+ data processors может come early при first DPA enterprise client |
| 32 | Bilingual frontmatter convention (lang: [ru, en]) для policy/, decisions/, roles/ | Mega-Corp #5 | Area 2 | Path к multi-country team without retroactive translation; English mandatory in 3 namespaces |
| 33 | Customer Success J2 role-manifest stub | Mega-Corp #7 | Area 7 | CS = retention; Account Mgmt = expansion. Activated при 10+ retainer clients |
| 34 | Compensation matrix coded в `decisions/policy/compensation.md` | Mega-Corp #8 | Area 7 | Salary bands per J-level (R9 §H benchmarks); equity bands per hire seq#; VSOP template, §19a path |
| 35 | EU AI Act compliance calendar `decisions/policy/eu-ai-act.md` | Mega-Corp #11 + Critic Hidden Risk #7 | NEW Area 7.5 | 2025/2026/2027 milestones quarterly check trigger |
| 36 | Pre-commit hooks spec'd Day 2-3 (asymmetric reference, Rechnungsnummer, role-manifest required-fields) | Critic #6 + Critic Open Q3 | Area 8 | Without hooks, rules are aspirational. Hooks = enforcement |
| 37 | Cost model section "Phase 1 Run Rate" с break-even | Critic #8 | NEW Area 8.3 | API €X/mo, Hetzner €Y, monitoring €W, total. First SKU pays N months of run rate |
| 38 | Constitution §11 succession protocol explicitly | Critic #5 | NEW Area 10 | Если Ruslan unavailable >7 days, automated client-facing template + escalation to designated emergency contact |

### 0.2 Rejected recommendations (12 explicit rejections с rationale)

| # | Rejection | From reviewer | Why rejected (must reference Jetix approved principle) |
|---|-----------|---------------|------------------------------------------------------|
| R1 | Drop L3, L5, L6, L7 from active design (Phase 1 to 4 layers only) | Critic #1 | **Violates approved principle: Mega-corp ambition с Day 1**. Layers preserved as **Reference Architecture** (design-time commitment); not materialized as folders Phase 1 (Operational Architecture distinction added per Part 1.1). Critic concern resolved через split, not abandonment |
| R2 | Reduce Career Ladder 7 → 3 levels permanently | Simplifier #8 | **Partial accept only**: Phase 1 operationally 3 levels (J-Auto/J-Approve/J-Strategic), но J0-JX preserved as **Reference Framework** for Phase 2+ when first human hire happens. Mega-Corp Concern: Mittelstand Geschäftsführer trust requires "J3 Lead" titre at hire. Cannot remove ladder entirely |
| R3 | Drop FPF-Lite to 1-page FPF-Mini | Simplifier #9 | **Partial accept only**: FPF-Lite preserved as 3-5 page artifact (per Левенчук Part 2 honest subset analysis); but loading rule changed: full text in meta-agent context only, 1-paragraph summary in agent system prompts (per Critic Weakness 6.1 token-budget concern). Best of both |
| R4 | 4 alphas only (Client/Deal/Invoice/Content) Phase 1 | Simplifier #6 | **Partial reject**: 7 true alphas Phase 1 (Client/Project/Deal/Content/Hypothesis/Member/WayOfWorking). Project и Hypothesis materially valuable Phase 1 (R3 §A.4 strategizing requires hypothesis tracking; client engagement requires project tracking distinct from deal). Member optional (can defer until 1st Alliance member). 7 is honest count, не 4 not 10 |
| R5 | Drop 8-block role-manifest до 4-block MVM forever | Simplifier #2 | **Same as R2 partial**: Phase 1 = 5-block role.md (identity/ontological/method/production_dependencies/evolution) + executor binding separate; 8-block reference architecture preserved для Phase 2 when first human hire requires Block 7 implementation_human. Не permanent reduction |
| R6 | Compress 14-day rollout to 5-day | Simplifier Part 5 | **Reject**: 5-day insufficient even с Simplifier tool reduction (5 tools still need provisioning + cron + secrets + first eval). 7+7 split per Critic #2 is right answer. Partial accept of cadence reduction (Simplifier Part 6) — 4 rituals не 16 |
| R7 | Federation pattern (`entities/<entity>/`) committed Phase 1 как top-level abstraction | Mega-Corp Section 3.1 | **Partial accept**: stub `entities/jetix-gmbh/` Phase 1 (4h scaffolding tax — Mega-Corp #1) but NOT full federation pattern. Phase 1 still operates on `jetix/` paths; `entities/` layer adds when 2nd entity emerges (acquisition или Holdings split). Stub preserves seam |
| R8 | Dynamic role assignment forbidden absolutely | Левенчук §1.1 #3 | **Modified accept**: forbidden by default; but exception clause for "Founder Mode" — Ruslan as executor can fluidly fill multiple roles intra-session (per founder-mode reality). FPF-Lite §5 principle с explicit Founder exception. Honest |
| R9 | 6 true alphas (drop Member) | Левенчук §1.2 #3 | **Reject**: Member preserved (Alliance member tracking). Member becomes meaningful Phase 1 if 1st L4 client onboards Alliance founding member status. Better keep alpha-grade than retro-promote |
| R10 | Multi-currency / multi-VAT scaffolding в `finance/` Phase 1 | Mega-Corp #15 | **Reject Phase 1 (defer)**: EUR-only Phase 1 sufficient for DACH market. CHF/USD scaffolding triggered by 1st non-EUR client (Phase 2a likely). 1h cost no urgency |
| R11 | IPO readiness placeholder в `decisions/` Phase 1 | Mega-Corp #14 | **Reject Phase 1 (defer)**: IPO 2035 horizon (10 years). Phase 1 placeholder = ceremonial. Add при Series A contemplation (Phase 2c). Premature |
| R12 | FPF-Steward sub-role внутри meta-agent Phase 1 | Mega-Corp #13 | **Reject Phase 1 (defer)**: meta-agent sufficient as FPF-consistency-checker для 12 agents. Dedicated FPF-Steward triggered at 30+ agents (Phase 2b) per Mega-Corp's own 100x scale audit |

### 0.3 Meta-conflicts resolved

Это самая сложная часть synthesizer работы. Каждый meta-conflict — между двумя legitimate angles, оба которых reflect real Jetix concerns. Resolution не compromise; resolution = higher-level frame addressing both essential concerns.

#### MC1: Critic vs Mega-Corp — Scaffolding-now vs Execution-now

**Critic position:** 98% synthesis = scaffolding для слоёв which не принесут €50K в Q2. Drop L3/L5/L6/L7. Inversion needed: revenue-first.

**Mega-Corp position:** Premature simplification = future rewrite. Build scaffolding now. €0→€10M trajectory requires architectural seams Day 1.

**Why both essential:** Critic right that €0→€50K is existential; if first client не closes Q3, none of mega-corp scaffolding helped. Mega-Corp right that re-architecture cost при Phase 2 transition (без preparation) = 200+ hours = months of rework.

**Resolution:** **Reference Architecture vs Operational Architecture split** в D1.
- **Reference Architecture** = full 7-layer + 8-block role-manifest + 10 alphas + J0-JX ladder + multi-entity readiness. Design-time commitment. Document. Не materialize.
- **Operational Architecture (Phase 1 MVA)** = 4 layers materialized (L0/L1/L2-as-discipline/L4) + 5-block role.md + 7 true alphas + 3-level operational career + 11 folders + Mega-Corp P1 stubs (4h-cost scaffolding `entities/jetix-gmbh/` + `governance/` + `ops/` because they prevent 200+h rebuild при Phase 2c transition).

**Honors Critic** — Phase 1 budget directed к sales infrastructure (7+7 day split); L3/L5/L6/L7 не consume Phase 1 hours.

**Honors Mega-Corp** — Phase 1 includes 14h scaffolding (entities + governance + ops) priced into 7-day foundation budget; mega-corp ambition не abandoned, materialization phased.

**Honors Ruslan principle:** «Mega-corp ambition с Day 1» preserved as design-time commitment; «scale-up-first» preserved as operational outcome.

**Trade-off accepted:** Phase 1 не minimal-minimal (Simplifier extreme); Phase 1 не fully-scaffolded (v1 extreme). Middle path с explicit cost-benefit per scaffolding addition.

#### MC2: Simplifier vs Mega-Corp — Lean Phase 1 vs Scale-up scaffolding

**Simplifier position:** 22 folders → 8. Re-add by trigger. Каждый компонент даёт цену поддержки даже как «просто файл».

**Mega-Corp position:** 22 folders insufficient (Mega-Corp + 3 = 11+); needs federation namespace, governance namespace, ops namespace. ~42h scaffolding cost vs 200+h re-architecture cost.

**Why both essential:** Simplifier right that maintenance burden compounds; 22 directories × README × revisit = quarterly ceremony mandatory. Mega-Corp right that some scaffolding (federation, ops) cost <5h Phase 1 vs 80h Phase 2c rebuild.

**Resolution:** **Cost-benefit gate per scaffolding addition.** Принцип: «Каждая директория Phase 1 should justify her existence через one of: (a) ≥3 real artifacts, (b) <5h cost for >40h Phase 2 saving, (c) explicit Ruslan judgment.»

Apply gate:
- **8 Simplifier baseline:** (a) all justify existence Phase 1.
- **+3 Mega-Corp P1:** (b) entities/jetix-gmbh/ stub (4h vs 80h), governance/advisory-board/ (2h vs 20h ceremony rebuild), ops/ (6h vs 40+h crisis cost). All pass gate.
- **−6 Mega-Corp P2 deferred:** customer success role, compensation matrix, org-chart pipeline, EU AI Act calendar, acquisition playbook, onboarding content. Add Phase 2a per trigger.
- **−3 Mega-Corp P3 rejected:** FPF-Steward, IPO roadmap, multi-currency. Add Phase 2c per trigger.

**Honors Simplifier** — folder count contained at 11 (not 22); re-add discipline preserved.
**Honors Mega-Corp** — 3 critical scaffolding additions preserved with explicit ROI calculation.
**Honors Ruslan principle** — «scale-up-first» — yes, but with cost-benefit gate.

#### MC3: Левенчук vs Pragmatic — Ontological purity vs Operational pragmatism

**Левенчук position:** Альфа vs Work Product collapsed. Past-participle nарушено в 52%. Граф создания = bipartite chart not mereological. ~15 changes needed.

**Pragmatic position (implicit в v1):** Перевод на software-engineering language enables tooling (mermaid, JSON Schema, lint, golden datasets). 100% ontological purity = academic theatre.

**Why both essential:** Левенчук right that ШСМ violation by misuse (decorating software practices с ШСМ names) more dangerous than violation by omission. Pragmatic right that AI agents need machine-readable specs; pure ontology без tooling — paper compliance.

**Resolution:** **Honor ШСМ correctness где critical (role ≠ executor; alpha vs work product distinction; past-participle convention; agents не стратегируют), simplify где ontology overhead exceeds value.**

Apply principle:
- **Critical (accept Левенчук in full):** alpha vs work product reduction (10 → 7 + 3 work products + 1 entity), past-participle audit, role-NOT-executor strict separation (binding.yaml extraction), agents не стратегируют (rename strategist, fix career mapping), «What ШСМ is NOT» section, lightweight mereology honest acknowledge.
- **Worth ontology cost (accept):** U-Types Lite 4 → 6 (objective/decision needed для acceptance criteria + decision records), `production_dependencies` rename (not «creation graph» misuse), `agent_onboarding` field, `reasoning_examples` field.
- **Deferred (defer не reject):** Full 3-level mereological creation graph artifact = D6 lite version Phase 1, full 3 levels Phase 2 (Левенчук Q4 acknowledged this trade-off).
- **Pragmatic preserved:** mermaid diagrams (software representation OK as visualization, not as ontology), JSON Schema for lint (CI/CD necessary), golden datasets (eval requires concrete instances).

**Honors Левенчук** — 13 of 15 changes accepted; ontological dilution risks all addressed; framework integrity protected.
**Honors Pragmatic** — tooling preserved где it enables AI agent reliability; ontology not eradicated в operational reality.
**Honors Ruslan principle** — «Role ≠ Executor» elevated to ontologically-clean implementation, no longer asserted-not-proven.

#### MC4: Critic Bus-Factor vs Simplifier Accept-Risk

**Critic position:** Bus factor = 1 institutionalized. No succession protocol. Architecture не reduces single point of failure — она его institutionalizes. Existential risk.

**Simplifier (anticipated by Critic Q4):** Solo founder phase is inherently bus-factor-1; architecture pretending otherwise = waste.

**Why both essential:** Critic right that Mittelstand client с retainer expects 24-48h response; if Ruslan incapacitated 4 weeks, contract breaches cascade. Simplifier right that elaborate succession infrastructure for solo Phase 1 = ceremony.

**Resolution:** **Lightweight mitigation, not elimination.** Accept that bus-factor = 1 in Phase 1 (cannot eliminate), но architect mitigation что reduces blast radius:

- **`ops/hit-by-bus.md`** (~2h Phase 1) — 1Password vault location, key contacts (Steuerberater, Notar, Anthropic acct mgr, Hetzner support, banking, Anton-as-trustee), open commitments, current decisions in flight, graceful shutdown procedure.
- **Designated trustee Anton** — explicit trust hierarchy decision. Anton has access in incapacitation event. Documented `governance/trustee-designations.md`.
- **Constitution §11 — Service Continuity protocol:** Если Ruslan unavailable >7 days, automated client-facing template response + escalation to Anton.
- **Dead-man's-switch script** (Phase 2 trigger): ежемесячный check-in heartbeat; if missed >2 weeks, automated message к Anton + critical clients.

**NOT included Phase 1** (overhead exceeds value): warm-standby human, Chief of Staff fractional pre-revenue, automated client-facing AI agent for incident management.

**Honors Critic** — existential risk acknowledged + mitigated with lightweight artifacts.
**Honors Simplifier** — full COO-style succession infrastructure deferred Phase 2.
**Honors Ruslan principle** — Mega-corp ambition preserved (mega-corps don't have bus-factor-1; mitigation is mega-corp-grade thinking applied at solo scale).

#### MC5: Mega-Corp Scale-readiness vs Simplifier YAGNI (federation specifically)

Already addressed in MC2 — `entities/jetix-gmbh/` stub Phase 1 (4h cost) accepted as cost-benefit clear win. Documenting separately because reviewer-conflict pattern recurring.

#### MC6: Левенчук strict-past-participle vs AI-readability

**Левенчук position:** ШСМ-strict past-participle для всех 50+ states (52% v1 violations).

**Pragmatic counter:** «in-progress» more readable than «started»; «active» more intuitive than «activated».

**Resolution:** **Strict-enforce past-participle.** Honor Левенчук Q1 recommendation (recommend strict). Rationale: gerunds describe process not state; Essence convention demands completed checklist semantics; AI agents trained on ontologically-correct states will reason more reliably. Apply systematic rename per audit table (Левенчук §1.2 #4).

Trade-off accepted: 1-2 weeks reading-discomfort during transition; permanent gain in semantic clarity.

### 0.4 Outstanding tensions (for Ruslan judgment)

Эти tensions Ruslan must judge personally; synthesizer recommendations included but не binding:

**OT1. Strategic-management decomposition: 5 sub-roles vs monolithic.**
- *Левенчук-correct:* 5 atomic roles (strategy-lead/framing-lead/sales-closer/acceptance-authority/external-relations).
- *Founder-mode reality:* fluid switching makes hard boundaries artificial.
- *Synthesizer recommendation:* Hybrid — 5 manifests written; executor `ruslan.yaml` permitted multi-role-binding flag. Acknowledge founder exception explicitly.
- *Ruslan judgment needed:* personal preference + delegation horizon.

**OT2. Bilingual frontmatter timing.**
- *Mega-Corp recommendation:* English mandatory in policy/ + decisions/ + roles/ from Phase 1.
- *Cost:* ongoing translation discipline; mental load.
- *Synthesizer recommendation:* English mandatory only in 3 namespaces (policy, decisions, roles) Phase 1; Russian default elsewhere; full bilingual at first non-Russian hire.
- *Ruslan judgment needed:* willingness for ongoing bilingual discipline.

**OT3. EU AI Act tier classification.**
- *Critic Hidden Risk #7:* AI agent auto-classifying lead score 70 may fall under Art. 22 «automated individual decisions».
- *Mega-Corp #11:* compliance calendar needed.
- *Synthesizer recommendation:* DPA conservative interpretation — добавить explicit human-approval gate to all client-affecting AI decisions Phase 1; defer high-risk-system EU AI Act classification (Aug 2026) until 1st DPA enterprise client requires assessment.
- *Ruslan judgment needed:* risk appetite (EU regulator surprise).

**OT4. Trademark Jetix vs Disney legacy.**
- *Critic Missing Consideration #8:* «Jetix» was Disney brand 2009. Trademark conflict risk DACH?
- *Synthesizer cannot research within review scope* — elevate to legal advisor (Steuerberater + IP lawyer).
- *Ruslan judgment needed:* either trademark search now (€500-1500) or rename decision.

**OT5. FPF-Lite token-budget treatment + publishing.**
- *Critic #15:* FPF-Lite alone fills system prompt budget (3-5K tokens × 12 agents = ongoing token tax).
- *Synthesizer recommendation:* reference-only loading (1-paragraph summary in agent system.md, full text in meta-agent context, link in others). Saves ~3-5K tokens per agent invocation.
- *Левенчук Q6:* «What ШСМ is NOT» — preserve internal-only or public artifact?
- *Synthesizer recommendation:* preserve internal-only; spirit kept в operational guides.
- *Ruslan judgment needed:* publishing FPF-Lite (Open Q6 v1 preserved) — strategic positioning decision.

---

## Part 1 — Unified Architecture Picture (updated)

### 1.1 Финальная архитектура

**[Δv2 — separated into Reference vs Operational]**

#### 1.1.1 Reference Architecture (mega-corp target, design-time commitment)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     Life-OS (root, Model D)                          │
│  ├── reflection/  daily-log/  health/  personal-goals/  relationships/│
│  └── projects/jetix/  ← ОДИН ИЗ ПРОЕКТОВ, full 7-layer architecture │
│                                                                       │
│  ╔═══════════════════════════════════════════════════════════════╗   │
│  ║                   Jetix (nested project)                       ║   │
│  ║                                                                 ║   │
│  ║  L0 Executive Core ═════ Ruslan + AI-агенты + future humans    ║   │
│  ║    через единую role-abstraction; J0–JX career ladder          ║   │
│  ║                                                                 ║   │
│  ║  L1 Foundation ═════ git + markdown + YAML + prompts-as-code   ║   │
│  ║    Tools: scale-aware (Phase 1: 5; Phase 2+: добавляются)      ║   │
│  ║                                                                 ║   │
│  ║  L2 Cognitive ═════ ШСМ + FPF-Lite + 7 alphas + agent strats   ║   │
│  ║    Phase 1: discipline (no folders); Phase 2: niches subdivide ║   │
│  ║                                                                 ║   │
│  ║  L3 Product ═════ productized SKUs (Audit / Quick Win / etc.)  ║   │
│  ║    Phase 1: 4 SKUs + clients/; Phase 2+: micro-SaaS, Club      ║   │
│  ║                                                                 ║   │
│  ║  L4 Delivery ═════ agency+consulting для DACH Mittelstand      ║   │
│  ║    Phase 1: PRIMARY revenue layer                              ║   │
│  ║                                                                 ║   │
│  ║  L5 Membrane ═════ Alliance + Newsletter + content + IHK/VDMA  ║   │
│  ║    Trigger: 1st L4 client closed                               ║   │
│  ║                                                                 ║   │
│  ║  L6 Topology ═════ Mittelstand Benchmark, platform, multi-prod ║   │
│  ║    Trigger: €1M ARR + competitive moat thinking                ║   │
│  ║                                                                 ║   │
│  ║  L7 Portfolio ═════ Capital + Hours + Attention accounting     ║   │
│  ║    Trigger: 1st human hire (team capital exists)               ║   │
│  ║                                                                 ║   │
│  ╚═══════════════════════════════════════════════════════════════╝   │
│                                                                       │
│  └── shared/ ═════ role-framework / Левенчук-онтология /             │
│       writing-templates / methodology-wiki                            │
│                                                                       │
│  [+v2] entities/ ═══ federation namespace (Phase 1 stub)             │
│  [+v2] governance/ ══ advisory/beirat/aufsichtsrat                   │
│  [+v2] ops/ ═════════ incident-playbooks/business-continuity         │
└─────────────────────────────────────────────────────────────────────┘
```

#### 1.1.2 Operational Architecture (Phase 1 MVA)

**Что materialized Day 1:**
- L0 Executive Core (Ruslan + 12 agent roles via `agents/<id>/` + executor binding via `executors/<id>.yaml`)
- L1 Foundation (5 tools: git/Claude Code/SOPS+age/restic/Healthchecks.io; pre-commit hooks Days 2-3)
- L4 Delivery (clients/ markdown CRM + 4 SKUs)
- L2 = читательская дисциплина (FPF-Lite read-only reference, не folder)
- L3/L5/L6/L7 = mentioned in D1, не materialized

**Phase 1 folders (11 total in jetix/):**
1. `agents/<id>/` — combined roles+executors+system.md
2. `alphas/` — 7 true alphas (state.yaml + context.md per type)
3. `clients/` — markdown CRM
4. `wiki/` — existing structure preserved
5. `decisions/<type>/` — combined adr/postmortem/letter/strategy/weekly/okr/policy
6. `evals/<role>/` — golden datasets (manual Phase 1)
7. `docs/` — Diátaxis 2-form (how-to, reference)
8. `finance/` — invoices YAML + ledger.md
9. **`entities/jetix-gmbh/`** [+v2 Mega-Corp #1] — federation stub
10. **`governance/`** [+v2 Mega-Corp #3] — advisory-board/, beirat/ placeholder
11. **`ops/`** [+v2 Mega-Corp #4] — incident-playbook/business-continuity/hit-by-bus

Plus: CLAUDE.md, README.md, CONSTITUTION.md (with §11 succession protocol)

### 1.2 Что изменилось vs v1 (high-level table)

| v1 | v2 | Source |
|----|----|--------|
| 22 top-level folders в jetix/ | 11 (8 Simplifier + 3 Mega-Corp scaffolding) | Simplifier #3, Mega-Corp #1/3/4 |
| 10 alphas with state machines | 7 true alphas + 3 work products + 1 entity (typed honestly) | Левенчук §1.2 |
| 8-block role-manifest per file | 5-block role.md + executor-binding.yaml separate | Левенчук §1.1 |
| Career ladder J0-JX operational | J0-JX reference; J-Auto/J-Approve/J-Strategic operational Phase 1 | Simplifier #8 (partial accept) |
| 14 tools Day 14 | 5 tools Phase 1 + Healthchecks.io | Simplifier Part 5 |
| 14-day Foundation rollout | 7+7 split (sales 1-7, foundation 8-14) | Critic #2 |
| FPF-Lite full text in every prompt | 1-paragraph in agent system.md + full text in meta-agent only | Critic #15 |
| Strategic-management single role | 5 atomic roles + ruslan multi-binding | Левенчук §1.1 #2, Mega-Corp Q2 |
| Per-alpha history.jsonl + monthly aggregate | Monthly only (alpha-log/YYYY-MM.jsonl); per-alpha re-add при context >50K | Simplifier #1, Critic Conflict 3 |
| 5-layer per-agent memory | 3-layer (system+scratchpad+mailbox) | Simplifier #7 |
| 6 wiki niches × symlinks | 1 общая wiki/ Phase 1 | Simplifier #12 |
| 9 typed edges | 3 (related/supports/contradicts) | Simplifier #13 |
| 5 wiki skills | 2 (/ingest, /ask) | Simplifier #14 |
| 16 rituals/quarter | 4 (daily/weekly/monthly/quarterly) | Simplifier Part 6 |
| Promptfoo+Langfuse self-hosted CI on push | Manual eval Phase 1 + Langfuse cloud free tier | Simplifier #11, Critic Q5 |
| No bus-factor mitigation | ops/hit-by-bus.md + Anton trustee + Constitution §11 | Critic Concern #3, Mega-Corp #4 |
| No federation readiness | entities/jetix-gmbh/ stub | Mega-Corp #1 |
| No DPO role | DPO external-mode role-manifest stub | Mega-Corp #2 |
| No bilingual convention | English mandatory policy/+decisions/+roles/ frontmatter | Mega-Corp #5 |
| Strategist agent J4 | Renamed strategy-support-analyst, J3 mapping | Левенчук §1.4 #2 |
| All states gerund/noun | Past-participle systematic rename (52% violations fixed) | Левенчук §1.2 #4 |
| graph_of_creation block | production_dependencies block + jetix-creation-graph.md separate artifact | Левенчук §1.3 |
| U-Types Lite 4 | U-Types Lite 6 (+ U.Objective, U.Decision) | Левенчук Part 2 |

### 1.3 Phase evolution (refined, [Δv2])

| Измерение | Phase 1 (2026, solo) | Phase 2a (€20K MRR + Ruslan >40% L1/L2 + DPA-requesting client) | Phase 2b (€2-10M, team 5-20) | Phase 3 (€50M+, mega-corp) |
|-----------|---------------------|-------------------------|------------------------------|----------------------------|
| **Executors** | 1 (Ruslan) + ~12 Claude-агентов | +1 human (Sales Lead J3) | +5-20 humans + 30+ agents | 50+ humans + 100+ agents |
| **L0 roles** | 1 Ruslan (5 sub-roles binding) + 12 agent roles | +1 human Sales Lead | + Head of Finance, COO-like, **+CS J2 (activated 10+ retainers), +DPO (activated)** | C-suite full + Divisions + **FPF-Steward** |
| **Repos** | 1 monorepo с life-os/+jetix/+shared/ | 2 repos (jetix + life-os-private) | 2+ repos, separate CI | Multi-repo federation OR `entities/<slug>/` namespace |
| **Server** | 1 Hetzner CPX32 + Backblaze B2 backup | 2 Hetzner | Jetix EU cloud + personal separate | Multi-region |
| **Юрлицо** | Freiberufler или UG | UG haftungsbeschränkt | GmbH | Holdings BV + Ops GmbH (multi-entity) |
| **Board** | Informal advisory (Anton/Vladislav/Rodion в `governance/advisory-board/members.yaml`) | Formal Beirat (4-6) | Beirat formalized | Aufsichtsrat (formal DACH) |
| **Финансы** | Personal + Steuerberater + backup Steuerberater contact | Fractional CFO €3-7K/mo | Head of Finance FTE €100-140K (corrected per Critic 7.3) | Full-time CFO + team |
| **Regulatory** | EU AI Act Phase 1 monitoring; **DPO role-manifest exists external-mode** | Betriebsrat readiness; 1st DPO activation если 20+ data processors | DrittelbG readiness if 500+ | DrittelbG + MitbestG full |
| **Revenue focus** | Q2 €50K (first L4 clients) | €300K-€1M (L4 agency, L3 productize start) | €2-10M (L3+L4+L5 compound) | €50M+ (L6 platform + L7 portfolio) |
| **Alliance (L5)** | — | founding members после 1st client | 50-150 members | 500-1000+ open tier |
| **Bus factor mitigation** | `ops/hit-by-bus.md` + Anton trustee + Constitution §11 | + dead-man's-switch script | + Chief of Staff role | + COO + designated successor |

### 1.4 Ключевые принципы (top 10) [Δv2 — refined]

1. **Jetix ≠ one-person company.** AI-native mega-corporation с Day 1. **[Δv2]** Scale-up-first design — *as design-time commitment*; Phase 1 operational reality is solo founder с MVP scaffolding. Reference Architecture vs Operational Architecture explicit split.
2. **Роль ≠ исполнитель.** **[Δv2]** Role.md = pure abstraction (5 blocks); executor binding = separate file. Multiple executors per role expressible. Portability = roadmap goal v2.0+, not v1 property.
3. **Место-слот, не содержание.** [=v1] Architecture описывает слои как готовые принять наполнение.
4. **Nested hierarchy (Model D) финально.** **[Δv2]** Lightweight mereology explicit acknowledged (Левенчук Part 2).
5. **Capital + Hours + Attention.** **[+v2]** Elevated to first-class principle (was implicit). Phase 1 own-only; Phase 2 +team's; Phase 3 +ecosystem.
6. **Бизнес как кодовая база (Company-as-Code).** [=v1]
7. **5 примитивов ШСМ, ontologically-correct.** **[Δv2]** Past-participle, alpha-NOT-work-product, agents-NOT-strategize, mereology-acknowledged.
8. **7 true alphas.** **[Δv2]** Client, Project, Deal, Content Item, Hypothesis, Member, Way of Working — каждая с state machines в past-participle.
9. **Org chart в Git, не в HR.** [=v1]
10. **DACH hard-coded.** **[Δv2]** *Phase 1-2; cross-border patterns documented as Phase 3 expansion option, не committed (per Mega-Corp 3.2).*

---

## Part 2 — 9 Architecture Areas (v2)

### Area 1: Overall Philosophy (→ D1 JETIX-ARCHITECTURE-FINAL.md)

#### Unified Recommendation [Δv2]

**Jetix — это AI-native mega-corporation в форме software artefact, материализованная phased.** Reference Architecture coммитована Day 1; Operational Architecture — Phase 1 MVP с предзаложенными швами. Каждая Phase transition — additive (новые folders, новые role-manifests, новые tools), не rebuild. Эта phasing — не indirection «чтобы избежать commitment»; это honest separation between «design-time understanding mega-corp shape» (commit now) и «operational reality solo founder» (materialize phased).

**Reviewer-feedback integrated:**
- Critic Concern #1 (scaffolding inversion) → Operational vs Reference split.
- Critic Concern #2 (portability claim) → explicitly downgraded to roadmap goal.
- Mega-Corp Concern #1 (centralization) → 5 atomic Ruslan-sub-roles.
- Левенчук Part 2 (mereology) → lightweight mereology acknowledged.
- Simplifier Q1 (scaffolding vs emergence) → cost-benefit gate principle.

#### Trade-offs [Δv2]

- Высокая когнитивная нагрузка mitigated через MVA ≈30% scope (Simplifier).
- Premature structure risk mitigated через cost-benefit gate per scaffolding addition.
- Зависимость от Claude Code — explicit acknowledgment «v1 = Claude-Code-coupled; portability = roadmap goal».
- DACH narrow positioning — mitigated через explicit cross-border future-option в Mega-Corp 3.2.

#### Open Questions for Ruslan [Δv2]
- **Q1 (preserved v1):** Strategic-management — monolithic vs 5-decompose. *Synthesizer recommendation:* hybrid (5 manifests, executor multi-binding flag).
- **Q2 (preserved v1):** Exit strategy 10-year — private DACH-focused или publishing framework.
- **[+v2 Q3]:** EU AI Act risk-tier classification — conservative (human-approval-gate Phase 1) vs aggressive (defer until 1st DPA client).
- **[+v2 Q4]:** Jetix trademark — search now or pivot?

#### Implementation Pointer
D1 JETIX-ARCHITECTURE-FINAL.md = T-02 template, 12-15 страниц. **[Δv2]** Sections: Context / Reference Architecture / **Operational Architecture (Phase 1 MVA)** / Decision / Consequences / Alternatives / Migration / Review triggers. Link-backs к D2-D9. **NEW subsection** «Phase 1 Minimum / Phase 2 Add / Phase 3 Add» per Simplifier KPI требование.

---

### Area 2: Folder Structure (→ D2 JETIX-FOLDER-STRUCTURE.md)

#### Unified Recommendation [Δv2]

**[Δv2]** Финальная Phase 1 структура монорепо `~/jetix-os/` — 11 folders (8 Simplifier baseline + 3 Mega-Corp P1):

```
~/jetix-os/                               # Root monorepo (Phase 1)
│
├── life-os/                              # L-1 Root (Model D)
│   ├── daily-log/{YYYY}/
│   ├── reflection/
│   ├── health/                           # GDPR special categories
│   ├── relationships/
│   ├── personal-goals/
│   ├── decisions/                        # Личные ADRs
│   ├── okrs/
│   ├── letters/
│   └── wiki/                             # Личное knowledge (отдельно)
│
├── jetix/                                # 11 folders Phase 1
│   ├── CONSTITUTION.md                   # §11 succession protocol [+v2]
│   ├── CLAUDE.md
│   ├── README.md
│   │
│   ├── agents/<id>/                      # combined roles+executors+system [Δv2 per Simplifier #4]
│   │   ├── role.md                       # 5-block (identity/onto/method/prod-deps/evolution)
│   │   ├── executor-binding.yaml         # implementation_ai/human extracted [+v2 per Левенчук §1.1]
│   │   ├── system.md                     # System prompt
│   │   ├── scratchpad.md                 # Working memory
│   │   └── (strategies merged inline в system.md per Simplifier #7)
│   │
│   ├── alphas/                           # 7 true alphas [Δv2]
│   │   ├── clients/<id>/
│   │   │   ├── state.yaml                # Past-participle states
│   │   │   ├── context.md
│   │   │   └── (history.jsonl deferred per Simplifier #1)
│   │   ├── projects/<id>/
│   │   ├── deals/<id>/
│   │   ├── content/<id>/
│   │   ├── hypotheses/<id>/              # alpha-grade per Левенчук §1.2 #3
│   │   ├── members/<id>/
│   │   └── way-of-working/<id>/          # [+v2 per Левенчук §1.2 #2]
│   │
│   ├── alpha-log/                        # Single event log Phase 1
│   │   └── YYYY-MM.jsonl
│   │
│   ├── clients/                          # Markdown CRM (R5)
│   │   ├── companies/<slug>.md
│   │   ├── contacts/<slug>.md
│   │   ├── deals/YYYY-MM-DD-<slug>.md
│   │   ├── activities/YYYY-MM-DD-<slug>.md
│   │   ├── contracts/{drafts,signed}/
│   │   └── invoices/YYYY/R-YYYY-NNNN.md  # work products, not alpha
│   │
│   ├── wiki/                             # Existing 557 pages preserved
│   │   ├── claims/                       # Hypothesis work-products
│   │   ├── sources/                      # Research Notes work-products
│   │   ├── experiments/                  # Postmortems work-products
│   │   ├── concepts/, entities/, topics/, ideas/, summaries/, foundations/
│   │   ├── comparisons/
│   │   ├── graph/edges.jsonl             # 3 edge types Phase 1
│   │   └── _templates/
│   │
│   ├── decisions/                        # Combined per Simplifier #5
│   │   ├── adr/
│   │   ├── postmortem/
│   │   ├── letter/                       # Quarterly Berkshire-style
│   │   ├── strategy/                     # Strategizing artifacts
│   │   ├── weekly/                       # Shape Up reviews
│   │   ├── okr/                          # Quarterly OKRs
│   │   ├── policy/                       # Constitution-supplements
│   │   │   ├── compensation.md           # [+v2 Mega-Corp #8]
│   │   │   ├── eu-ai-act.md              # [+v2 Mega-Corp #11]
│   │   │   └── ...
│   │   ├── 0001-jetix-architecture-final.md
│   │   └── ...
│   │
│   ├── evals/<role>/                     # Golden datasets (manual Phase 1)
│   │   └── golden.jsonl
│   │
│   ├── docs/                             # Diátaxis 2-form Phase 1
│   │   ├── how-to/
│   │   └── reference/
│   │
│   ├── finance/                          # Invoices + ledger
│   │   ├── invoices/YYYY/R-YYYY-NNNN.md
│   │   ├── ledger.md
│   │   ├── next-invoice-number.txt
│   │   └── datev/YYYY-MM.csv
│   │
│   ├── entities/                         # [+v2 Mega-Corp #1] Federation stub
│   │   └── jetix-gmbh/                   # Phase 1 single-entity
│   │       └── manifest.yaml
│   │
│   ├── governance/                       # [+v2 Mega-Corp #3]
│   │   ├── advisory-board/
│   │   │   ├── members.yaml              # Anton, Vladislav, Rodion
│   │   │   └── meetings/<YYYY-MM-DD>.md
│   │   ├── trustee-designations.md       # [+v2 MC4] Anton як bus-factor trustee
│   │   ├── beirat/                       # Phase 2c placeholder
│   │   └── aufsichtsrat/                 # Phase 3 placeholder
│   │
│   └── ops/                              # [+v2 Mega-Corp #4 + Critic Concern #3]
│       ├── incident-playbook.md
│       ├── business-continuity.md
│       ├── hit-by-bus.md                 # Anton-readable
│       ├── disaster-recovery.md
│       └── regulatory-incidents/
│           └── gdpr-art-33-playbook.md
│
├── shared/                               # R7 Part C
│   ├── role-framework/
│   ├── levenchuk-ontology/
│   └── writing-templates/
│
├── .claude/
├── infra/
├── secrets/                              # SOPS+age, 1 key Phase 1 (Simplifier)
├── tools/
├── scripts/
├── .github/workflows/                    # 1 minimal: pre-commit
├── .sops.yaml, .pre-commit-config.yaml
└── README.md
```

**Что NOT created Phase 1 (deferred per Simplifier Part 3 trigger table):**
- `comms/mailboxes/` — re-add при 3+ agents с inter-agent dependency
- `state/` — re-add при DuckDB queries реально используются
- `sales/` projections — re-add при 2+ продавцах
- `templates/` — re-add при 2+ авторе
- `processes/` — re-add при формализованных procedures
- `products/` — re-add при 1-м SaaS commit
- `roles/` separate (combined в agents/) — re-add при 30+ агентах OR 1-й human

#### Reviewer feedback integrated

- **Simplifier #3-5, Part 3:** folder reduction + decisions/ combined + extension triggers — ACCEPTED
- **Mega-Corp #1, #3, #4:** entities/ + governance/ + ops/ — ACCEPTED with cost-benefit gate
- **Critic Weakness 2.4:** missing inbox/ — voice-notes pipeline outputs land in `inbox/` (top-level under jetix/, simple). [+v2]
- **Левенчук Part 6 terminology:** alpha vs entity vs work product distinction — applied via separate folders (alphas/ vs clients/ vs wiki/)

#### Trade-offs

- 11 folders > 8 Simplifier minimum: justified per cost-benefit gate (entities/ 4h saves 80h Phase 2c; governance/ 2h saves 20h Beirat-formation rebuild; ops/ 6h saves 40+h crisis cost).
- 11 folders < 22 v1: maintenance burden manageable; README-per-folder convention but each folder has clear purpose.
- Three-fold representation (alphas/+clients/+wiki/) preserved per Conflict 1 v1 resolution (operational vs entity-notes vs semantic). Mitigation: pre-commit hook validating alpha-ref edges (Day 2-3 per Critic #6).

#### Open Questions for Ruslan
- **Q1 (preserved):** life-os/wiki/ + jetix/wiki/ separate or shared? *Soft vote: separate (Phase 2 extraction cleaner).*
- **Q2 (preserved):** shared/ as top-level или внутри jetix/? *Soft vote: top-level.*
- **[+v2 Q3]:** entities/jetix-gmbh/ stub immediate value — write or wait? *Synthesizer:* write (4h vs 80h ROI).

#### Implementation Pointer
D2 JETIX-FOLDER-STRUCTURE.md = full tree + namespaced conventions + scale-up triggers + Phase 1 minimum / Phase 2 add / Phase 3 add subsections + migration script (filter-repo для Life-OS extraction).

---

### Area 3: Role Manifests (→ D3 JETIX-ROLE-MANIFESTS.md)

#### Unified Recommendation [Δv2]

**Role-manifest = 5-block YAML+Markdown в `agents/<id>/role.md`** — pure role abstraction. Executor binding extracted в `agents/<id>/executor-binding.yaml`. Это resolves Левенчук §1.1 #1 + Simplifier #2 одновременно.

**5-block role.md (Phase 1 MVM, ~50-100 lines per role):**

```yaml
---
# Block 1 — Identity (per R3 §C.1)
identity:
  name: sales-lead
  display-name: "Sales Lead"
  version: "1.0.0"
  layer: L4
  family: sales
  status: active
  created: 2026-04-19
  updated: 2026-04-19
  lang: [ru, en]                   # [+v2 Mega-Corp #5]
  english-summary: >               # [+v2 mandatory in roles/]
    Generates qualified Mittelstand pipeline; converts to signed contracts.

# Block 2 — Ontological (Левенчук + Holacracy)
ontological:
  purpose: >
    Генерировать quality pipeline и конвертировать в подписанные контракты.
  target-system: "client-pipeline"
  primary-alpha: client
  secondary-alphas: [deal]
  domains:
    - CRM (clients/)
    - Pricing authority до €25K
  accountabilities:
    - id: acc-001
      description: "Generate ≥20 qualified leads weekly"
      alpha: client
  out_of_scope:                    # [Δv2 — explicit per Левенчук §1.1 #3]
    - Outreach сообщения (→ sales-outreach)
    - Подписание контрактов (→ ruslan/sales-closer)
    - Switch role at task-time (forbidden dynamic role assignment)
  acceptance-criteria:
    - "Client.qualified: ICP score ≥ 70"   # past-participle [Δv2]

# Block 3 — Method (Epistemology) [Δv2 — added reasoning_examples]
method:
  primary_frameworks:
    - name: MECE hypothesis-driven segmentation
    - name: SPIN Selling / Challenger Sale
  thinking_protocol:
    - "Прочитай все open deals"
    - "Apply MECE: каждый deal — в одну стадию"
  quality_criteria:
    - "Pipeline updated (all deals с next action ≤7 days)"
  anti_patterns:
    - "Proposal без champion"
    - "Verbal price без written quote"
  reasoning_examples:              # [+v2 per Левенчук Part 3 #3]
    - path: docs/reasoning/sales-lead-discount-vs-walk-away.md
  golden_examples:
    - evals/sales-lead/golden.jsonl

# Block 4 — Production Dependencies (RENAMED from graph_of_creation per Левенчук §1.3)
production_dependencies:           # [Δv2 RENAMED]
  produces:
    - artifact: pipeline-report
      consumers: [strategy-lead, framing-lead]
    - artifact: proposal
      consumers: [client, delivery]
  consumes:
    - artifact: qualified-contact
      produced_by: sales-research
      required: true

# Block 5 — Evolution
evolution:
  last_review: "2026-07-01"
  changelog:
    - version: "1.0.0"
      date: "2026-04-19"
      change: "Initial v2 manifest"
  expected-evolution:
    - "Q3 2026: first human hire trigger Block 7 add"
    - "2027: split SMB/Enterprise при >50 deals"
---

# Sales Lead — System Prompt

## Purpose
[Read from Block 2 ontological.purpose]

## Method
[Read from Block 3 method.thinking_protocol]
...
```

**Executor binding** (separate file `agents/sales-lead/executor-binding.yaml`):

```yaml
# [+v2 Per Левенчук §1.1 #1 — extracted from role.md]
assigned-role: sales-lead
executor-id: claude-sales-lead-001
executor-type: ai                  # ai | human | hybrid
ai_executor:
  agent_type: claude-code
  model: claude-opus-4-7           # [Δv2 — explicit "current Phase 1 binding; v2.0+ portability roadmap"]
  prompt-file: agents/sales-lead/system.md
  eval-dataset: evals/sales-lead/golden.jsonl
  eval-passing-threshold: 0.85
  tools-allowed:
    - {name: filesystem, scope: ["clients/", "templates/"]}
  forbidden-tools: [email-send, git-push]
  context-window-budget: 180000
  memory-strategy: "rolling-summary + pinned-client-context"
  agent_onboarding:                # [+v2 per Левенчук Part 3 #2]
    initial_context_pack:
      - docs/onboarding/sales-lead-orientation.md
      - wiki/concepts/business/icp-mittelstand.md
    warm_up_tasks: 3-5
    calibration_checkpoint:
      after: 10 tasks
      threshold: 0.85
      against: evals/sales-lead/golden.jsonl
human_executor:                    # null Phase 1; filled при first hire
  hired-person: null
  onboarding-path:
    - "Read role.md + golden examples (2 days)"
    - "Shadow AI 10 deals (1 week)"
    - "Co-pilot mode (2 weeks)"
    - "Autonomous с weekly review"
  reporting-to: ruslan/strategy-lead
  performance-kpis:
    - {metric: "Qualified leads/week", target: ">=20"}
  handoff_from_ai:
    triggers: ["Deal >€50K live pitch", "Client requests human call"]
```

**Block 5 (seniority/decision-rights) — NOT separate file Phase 1.** Per Simplifier #8: 5-line list в role.md frontmatter:
```yaml
seniority-lite:
  current_level: J-Approve         # J-Auto | J-Approve | J-Strategic
  autonomous: ["Qualify/disqualify lead (ICP < 40)", "Discount до 10%"]
  approve-required: ["Discount 10-20%", "Contract terms нестандартные", "Deal > €40K"]
  never: ["Sign contracts", "Change pricing floor"]
```

Re-add full Block 5 при first human hire (Block 7 trigger same time).

#### Strategic-management decomposition [+v2]

Per Левенчук §1.1 #2 + Mega-Corp Q2 + Critic Q4: декомпозируется на 5 atomic role-manifests, single executor `ruslan.yaml`:

```
agents/strategy-lead/role.md           # Strategy-as-method (strategizing)
agents/framing-lead/role.md            # Framing problems и methods
agents/sales-closer/role.md            # Final close + contract signing
agents/acceptance-authority/role.md    # Final acceptance authority for deliverables
agents/external-relations/role.md      # IHK/VDMA/network/PR

executors/ruslan/binding.yaml:
  multi-role-binding: true            # [+v2 founder-mode exception per OT1]
  assigned-roles: [strategy-lead, framing-lead, sales-closer, acceptance-authority, external-relations]
```

#### Reviewer feedback integrated

- **Simplifier #2 (4-block MVM):** Partial accept — 5-block role.md (added evolution which Simplifier defer) + Block 5 lite list + Blocks 6/7 separate. Net result similar reduction.
- **Левенчук §1.1-#1.3 (role-NOT-executor):** ACCEPTED in full.
- **Левенчук §1.1 #2 (multi-role founder):** ACCEPTED via 5 atomic + multi-binding flag.
- **Левенчук §1.1 #3 (dynamic role assignment forbidden):** ACCEPTED via out_of_scope + FPF-Lite §5 principle.
- **Левенчук §1.3 (graph_of_creation rename):** ACCEPTED → production_dependencies + separate creation-graph artifact.
- **Левенчук Part 3 #2-#3 (agent_onboarding + reasoning_examples):** ACCEPTED.
- **Mega-Corp #2 (DPO role-manifest):** ACCEPTED → `agents/dpo/role.md` external-mode stub Phase 1.
- **Mega-Corp #6 (strategic-management decompose):** ACCEPTED with founder-mode exception.
- **Critic Weakness 3.1-3.4:** Block 5 split_trigger fictional → deferred to Phase 2 trigger; forbidden-tools enforcement → addressed via tool MCP scoping в executor-binding (still imperfect, Critic Weakness real); implementation_human premature spec → fully extracted to executor-binding, filled только when hired-person ≠ null.

#### Open Questions for Ruslan
- **[+v2 Q1]:** Strategic-management 5-atomic-decomposition — start now (per recommendation OT1) или incremental (start monolithic, decompose at first delegation event)?
- **Q2 (preserved):** family field — L-layer or functional?

#### Implementation Pointer
D3 JETIX-ROLE-MANIFESTS.md = template + JSON Schema (lint subset) + 12 examples Phase 1 (5 atomic Ruslan-roles + 7 agent roles: sales-lead, sales-research, sales-outreach, delivery, knowledge-synth, meta-agent, manager) + DPO stub. Estimate: ~15-20h with simplification.

---

### Area 4: Life-OS Separation (→ D4 JETIX-VS-LIFE-OS.md)

#### Unified Recommendation [Δv2 minor]

**Model D Nested Hierarchy** preserved per v1. Three phases preserved.

**[Δv2 changes:**
- SOPS — 1 key Phase 1 per Simplifier (vs 2 keys v1). Trigger second key: 1 week before Phase 2 hire trigger.
- Asymmetric reference rule — convention в CLAUDE.md Phase 1 (vs pre-commit hook v1) per Simplifier. Hook added 1 week before Phase 2 trigger.
- Phase 2 trigger explicit triple-AND criteria per Critic #9 + Simplifier:
  - 3 consecutive months ≥€20K MRR AND
  - Ruslan reports >40% time на L1/L2 ops tasks (Toggl-tracked) AND
  - At least 1 active client requesting GDPR DPA

**Lightweight mereology acknowledgment** [+v2 per Левенчук Part 2]:
> Model D Nested IS mereological structure (Jetix-as-part-of Life-OS-as-whole). FPF-Lite §1 acknowledges «Lightweight mereology» as principle; advanced mereology (Kit Fine, constructor theory) excluded.

#### Reviewer feedback integrated

- **Simplifier #4 (Phase 1 simpler):** ACCEPTED — 1 SOPS key, asymmetric rule as convention.
- **Critic Weakness 4.1-4.4:**
  - Single SOPS key trust-level concern → acknowledged Phase 1 limitation; second key Phase 2.
  - Phase 2 trigger ambiguity → ACCEPTED triple-AND criteria.
  - Pre-commit hook adversarial concern → hook becomes adversary mitigated через explicit «hook flag warning, not block; commit allows with --no-verify-warning»; hook strict only Phase 2+.
  - MCP scope issue — separate concern, addressed in Area 3 Block 6.
- **Левенчук Part 2 (mereology honesty):** ACCEPTED.

#### Trade-offs
Migration overhead Phase 2 (~1 day) preserved.

#### Open Questions for Ruslan
- **Q1 (preserved):** shared/ Phase 2 — duplicated, separate public, or only-Jetix?
- **Q2 (preserved):** Geschäftskonto timing — Phase 1 or wait?

#### Implementation Pointer
D4 JETIX-VS-LIFE-OS.md = Model D spec + 3-phase migration table + asymmetric reference rule + grey zone classification + insight flow sanitization + filter-repo script + GDPR Phase 2 checklist + lightweight mereology acknowledgment.

---

### Area 5: Knowledge Architecture (→ D5 JETIX-KNOWLEDGE-ARCHITECTURE.md)

#### Unified Recommendation [Δv2]

Three-layer Karpathy LLM Wiki + 7 Alphas + Per-agent 3-layer memory.

**Layer 1: wiki/** (Karpathy pattern, 557 current pages).
- 9 entity types preserved (concepts/entities/sources/topics/ideas/experiments/claims/summaries/foundations).
- **[Δv2 per Simplifier #12]** 1 общая wiki/ Phase 1 (no per-niche subdivision; re-add Phase 2).
- **[Δv2 per Simplifier #13]** 3 typed edges (related, supports, contradicts); 6 more added trigger-driven.
- **[Δv2 per Simplifier #14]** 2 skills Phase 1: /ingest, /ask. /lint, /consolidate, /build-graph triggered at 500+ orphans.
- HippoRAG PPR retrieval preserved.

**Layer 2: alphas/** (7 true alphas, [Δv2]):

| # | Alpha | Type | Storage Pattern | States (past-participle [Δv2]) |
|---|-------|------|----------------|-------------------------------|
| 1 | Client | true alpha | Hybrid C: state.yaml + context.md | leadidentified, qualified, proposed, in-negotiation, won, lost, churned |
| 2 | Project | true alpha | Hybrid C | scoped, kicked-off, started, delivered, closed, in-follow-up |
| 3 | Deal | true alpha | Hybrid C | drafted, signed, activated, completed, cancelled |
| 4 | Content Item | true alpha | Hybrid C | drafted, in-review, approved, published, retired |
| 5 | Hypothesis | true alpha | wiki-primary в `wiki/claims/` | formulated, under-validation, validated, invalidated, implemented |
| 6 | Member | true alpha | Hybrid C (Phase 2 trigger) | applied, invited, activated, flagged-at-risk, churned |
| 7 | **Way of Working** [+v2] | true alpha | Hybrid C | drafted, implemented, refined, deprecated |

**Reclassified (NOT alphas):**
- Invoice — work product (lifecycle = Deal alpha). Stored `clients/invoices/YYYY/R-YYYY-NNNN.md` с metadata.
- SKU — entity. Stored `entities/skus/<sku>.yaml`.
- Postmortem — work product. Stored `decisions/postmortem/<slug>.md`.
- Research Note — work product of Knowledge alpha. Stored `wiki/sources/<slug>.md`.

**Layer 3: Per-agent memory** [Δv2 — 3 layers per Simplifier #7]:
- `agents/<id>/system.md` — Core identity + strategies merged inline (was 5 layers v1).
- `agents/<id>/scratchpad.md` — Working memory (ephemeral).
- `comms/mailboxes/<id>.jsonl` — Recall (deferred until 3+ agents с inter-agent dependency per Simplifier).

**Context loading budget [Δv2 per Левенчук Part 3 #1]:**
- **25K tokens HARD reservation для exocortex** (system/strategies/role/FPF). Никогда не compresses.
- **25K tokens SOFT для state/scratchpad/RAG/recent decisions/mailbox.**
- Total: 50K (25% of Opus 4.7 200K window).

**Single event log Phase 1 [Δv2 per Simplifier #1, Critic Conflict 3]:**
- `alpha-log/YYYY-MM.jsonl` only.
- Per-alpha read-locality via `jq` filter on alpha_id.
- Re-add per-alpha history.jsonl при context loading >50K consistently OR GoBD audit explicitly required.

**German legal compliance:**
- Invoice YAML schema preserved (11 Pflichtangaben § 14 UStG).
- ZUGFeRD 2.x **deferred to 2026-Q3** (per Simplifier #18, mandatory only 2027-01 sender-side).
- Sequential Rechnungsnummer pre-commit monotonicity check (Day 2-3 hook).
- Steuerberater backup contact в `ops/hit-by-bus.md` per Critic Hidden Risk #5.

#### Reviewer feedback integrated

- **Simplifier #1, #6, #7, #12-14, #18:** ALL ACCEPTED.
- **Левенчук §1.2 #1-4:** ALL ACCEPTED (alpha reduction + past-participle audit + WoW addition).
- **Левенчук Part 3 #1 (exocortex hard reservation):** ACCEPTED.
- **Critic Weakness 5.1-5.5:** wiki scaling projection (557→5000) — acknowledged not-firm; Hybrid C maintenance burden — addressed via simplification (3-layer memory, single event log); 50K budget breakdown math — corrected (25+25=50, not 45); dual-write fail-safe — addressed via single event log Phase 1; sequential Rechnungsnummer monotonicity — pre-commit hook spec'd Day 2-3.

#### Open Questions for Ruslan
- **Q1 (preserved):** wiki/comparisons/ writeback automatic vs manual?
- **Q2 (preserved):** GraphRAG trigger — 5000 pages firm или revisit?
- **[+v2 Q3]:** ZUGFeRD 2.x implementation Q3 2026 vs reactive when 1st client demands?

#### Implementation Pointer
D5 JETIX-KNOWLEDGE-ARCHITECTURE.md = detailed folder spec + state machine diagrams per alpha (past-participle) + writeback rules + context loading pseudo-code + HippoRAG retrieval pipeline + German legal invoice schema + Levенчук "What ШСМ is NOT" reference.

---

### Area 6: FPF-Lite (→ D6 JETIX-FPF-LITE.md)

#### Unified Recommendation [Δv2]

FPF-Lite preserved as **3-5 страниц operational spec** per Левенчук Part 2 honest-subset analysis. **[Δv2 critical change]** Loading rule: agent system.md содержит 1-paragraph FPF-Lite summary + link; full text — meta-agent context only. Per Critic Weakness 6.1 token-budget concern.

**Sections (8, [Δv2 enriched per Левенчук]):**

1. **Target System** — preserved.
2. **Stakeholders** — preserved.
3. **Creation Graph** — **[Δv2 LITE Phase 1]** Level 1 only (Operational); Level 2-3 sketch с future-iteration commitment per Левенчук Q4. Stored as separate artifact `wiki/foundations/jetix-creation-graph.md`.
4. **Client Principles** — preserved.
5. **Internal Principles** — **[Δv2 expanded to 8]**:
   1. Role ≠ executor strict separation.
   2. Context is king.
   3. Artifacts over conversations.
   4. Meta-agent as immune system.
   5. Explicit alpha state transitions (past-participle).
   6. No role left undefined.
   7. Writing as thinking.
   8. **[+v2 per Левенчук Part 3 #2]** Agents — new participants of master class. Onboarding required, not just prompt loading.
   - **[+v2 per Левенчук §1.1 #3]** Forbidden: Dynamic role-switching by agent at task-time. Cross-role escalation through manager, not through role-switch. *Founder exception: Ruslan permitted multi-role binding flag.*
6. **7 True Alphas** — Client / Project / Deal / Content Item / Hypothesis / Member / **Way of Working** [+v2] — с states past-participle.
7. **Ritual Cadence** — [Δv2 per Simplifier Part 6]:
   - Daily: morning inbox + pipeline + intent (30 min combined).
   - Weekly Friday: Shape Up status + week commits + intent + close-week (60 min).
   - Monthly last Friday: P&L + OKR + 1-page founder note + meta-review (2h).
   - Quarterly: letter + OKR-next + role-manifest delta + strategy decisions (1 day).
   - **[Δv2 per Левенчук §1.4 #1]** Strategizing = trigger-driven event, NOT monthly ceremony. Monthly check = trigger detection only. `decisions/strategy/<trigger-slug>-YYYY-MM-DD.md` slug starts with trigger description, not date.
8. **U-Types Lite [Δv2: 4 → 6]** — U.System, U.Role, U.Method, U.Stakeholder, **U.Objective**, **U.Decision** (per Левенчук Part 2).

**[+v2 NEW Section 9] What ШСМ is NOT** (per Левенчук Part 5 защита от software-language colonization):
- ШСМ роль ≠ software class или GitHub team.
- ШСМ alpha ≠ database table или Kanban column.
- ШСМ creation graph ≠ workflow diagram или dependency tree.
- ШСМ strategizing ≠ planning meeting или OKR session.
- ШСМ thinking by writing ≠ documentation generation или Confluence pages.

**[+v2 NEW Section 10] Lightweight Mereology Acknowledgment** (per Левенчук Part 2):
- Jetix-as-part-of Life-OS-as-whole — explicit mereological pattern (Model D).
- Advanced mereology (Kit Fine, constructor theory) — excluded by Phase 1 design.
- Holons recursive (Ruslan-as-executor → role → Jetix → Life-OS) — acknowledged but не materialized в spec syntax.

**What's still excluded (overkill для Phase 1):**
Полная иерархия холонов; 17 trans-disciplines; full mereology; category theory; constructor theory; Architectural invariants of full FPF.

#### Reviewer feedback integrated

- **Левенчук Part 2 (U-Types expansion + mereology):** ACCEPTED.
- **Левенчук Part 5 («What ШСМ is NOT»):** ACCEPTED.
- **Левенчук Part 7 #6 (production_dependencies rename + creation-graph separate):** ACCEPTED.
- **Левенчук §1.4 (strategizing event-not-ceremony):** ACCEPTED.
- **Левенчук Part 3 #2 (8th principle agents-as-master-class):** ACCEPTED.
- **Critic Weakness 6.1 (token budget):** ACCEPTED reference-only loading rule.
- **Simplifier #9 (1-page FPF-Mini):** REJECTED partial — preserve 3-5 pages but reference-loading addresses Critic concern.
- **Simplifier Part 6 (ritual reduction):** ACCEPTED.

#### Open Questions for Ruslan
- **Q1 (preserved):** Publishing decision (internal forever vs Phase 3 public)?

#### Implementation Pointer
D6 JETIX-FPF-LITE.md = 3-5 pages text + Section 9 «What ШСМ is NOT» + Section 10 lightweight mereology + separate `jetix-creation-graph.md` artifact (Level 1 Phase 1, Level 2-3 future).

---

### Area 7: Career Levels + Scale-up (→ D7 JETIX-CAREER-LEVELS.md)

#### Unified Recommendation [Δv2 split]

**Reference Framework:** 7-level ladder (J0-JX) preserved per R1 §G.1. Decision-rights matrix preserved.

**Phase 1 Operational [Δv2 per Simplifier #8]:** 3 operational levels:
- **J-Auto** — agent делает без approval (sales-research scraping, inbox-processor triage, knowledge-synth daily summaries).
- **J-Approve** — agent prepares, Ruslan approves (sales-outreach messages, delivery proposals, external communication).
- **J-Strategic** — only Ruslan (sign contracts, fire/hire, change pricing, reposition).

Mapping current 12 agents → 3 operational levels:
- J-Auto: inbox-processor, sales-research, knowledge-synth, system-admin
- J-Approve: sales-outreach, delivery, analyst, meta-agent, manager, sales-lead, life-coach, **strategy-support-analyst** (renamed from strategist)
- J-Strategic: ruslan-as-executor (5 atomic roles)

5-line `seniority-lite` list в каждом role.md frontmatter (per Area 3) replaces 13×6 matrix Phase 1.

**Phase transitions [Δv2 refined per Critic #9]:**

- **Phase 0 (now → Q2 2026):** 1 Ruslan + 12 agent roles. Target €50K. Trigger to Phase 2a:
  - 3 consecutive months ≥€20K MRR AND
  - Ruslan reports >40% time на L1/L2 ops (Toggl с explicit J-level tags) AND
  - At least 1 active client requesting GDPR DPA
- **Phase 2a (Q3-Q4 2026 → €300K-€1M):** First human hire = Sales Lead J3. Re-introduce full Block 5 (seniority/decision-rights) и Block 7 (implementation_human) в role.md. Activate full J0-JX ladder (3 ops levels deprecated).
- **Phase 2b (2027 → €1-5M):** Head of Finance FTE €100-140K (corrected from €80-120K v1 per Critic 7.3). Customer Success J2 activated [+v2 Mega-Corp #7]. DPO activated [+v2 Mega-Corp #2].
- **Phase 2c (€10-50M):** Full C-suite. Constellation pattern. **[+v2]** Federation pattern (`entities/<slug>/`) materialized — но stub Phase 1 reduces transition cost.
- **Phase 3 (€50M+):** DACH regulatory + Aufsichtsrat.

**Promotion Signals (R1 §G.7):** preserved as Reference Framework.

**[Δv2] AI agent promotion mechanism per Critic Weakness 7.1:**
- ~~Self-graded 90-day track record + <2% escalation~~ → REPLACED:
- **Monthly external review by meta-agent + Ruslan sign-off** of agent escalation log.
- No promotion without human ratification.
- Removes self-grading loop.

**Human-AI boundary [Δv2 per Critic Weakness 7.5]:**
- "Strategic client" defined: (a) ARR contribution >5% OR (b) ≥3 stakeholders client-side OR (c) referrer for ≥1 other client.
- Other categories preserved.

**C-suite timing [Δv2 corrected]:**
- CFO: fractional на €1M ARR, FTE на €10M ARR (corrected from "$10M+" v1 per Critic 7.4 currency consistency).
- All ranges in € (consistent DACH context).
- Other roles preserved.

#### [+v2 NEW Section 7.5] EU AI Act Compliance Calendar

Per Mega-Corp #11 + Critic Hidden Risk #7:

`decisions/policy/eu-ai-act.md`:
- 2025: monitoring period (no obligations).
- 2026 Aug: high-risk AI systems registration EU database (defer assessment until 1st DPA enterprise client).
- 2027: full compliance for high-risk systems.
- Quarterly check: any AI agent decisions falling под Art. 22 (legal effects or similarly significantly affects)?
- Conservative interpretation Phase 1: human-approval-gate for all client-affecting AI decisions (lead scoring, proposal pricing).

#### Reviewer feedback integrated

- **Simplifier #8:** ACCEPTED partial — Phase 1 operational simplified to 3 levels; full ladder preserved as reference.
- **Mega-Corp #2 (DPO):** ACCEPTED — role-manifest stub Phase 1.
- **Mega-Corp #7 (Customer Success):** ACCEPTED — stub Phase 2a trigger.
- **Mega-Corp #8 (compensation matrix):** ACCEPTED — `decisions/policy/compensation.md`.
- **Mega-Corp #11 (EU AI Act):** ACCEPTED.
- **Левенчук §1.4 #2 (strategist rename):** ACCEPTED → strategy-support-analyst, J-Approve mapping.
- **Critic Weakness 7.1-7.5:** ALL ACCEPTED (external audit + currency consistency + strategic client definition + Head of Finance corrected + AI promotion mechanism).

#### Open Questions for Ruslan
- **Q1 (preserved):** crazy-agent — J3 (R1 mapping) или special hackathon mode outside ladder?
- **Q2 (preserved):** life-coach — Jetix career ladder or only Life-OS?

#### Implementation Pointer
D7 JETIX-CAREER-LEVELS.md = full reference ladder + Phase 1 operational 3-level + decision-rights matrix + phase transitions roadmap + human-AI boundary с strategic-client definition + C-suite timing (€) + AI promotion mechanism (external audit) + DACH regulatory triggers + DPO + Customer Success stubs + compensation matrix + EU AI Act calendar.

---

### Area 8: Operational Instructions (→ D8 docs/INSTRUCTIONS.md)

#### Unified Recommendation [Δv2]

**[Δv2 per Critic #2 + Simplifier]** **7+7 day rollout split:**

**Days 1-7 — Sales Infrastructure (Critic-driven priority inversion):**

| Day | Work | Deliverable | Done criterion |
|-----|------|-------------|----------------|
| 1 | Domain registration + repo init | jetix.de domain + git init | jetix.de DNS resolves |
| 2 | First SKU page + pre-commit hooks (asymmetric reference, Rechnungsnummer monotonicity, role-manifest required-fields) | `clients/skus/audit.md` + `.pre-commit-config.yaml` | Hooks block test commit |
| 3 | Cold outreach list (50 Mittelstand contacts via IHK directory) | `clients/leads/_cold-outreach-2026-Q2.md` | 50 named contacts с context |
| 4 | First discovery call template + scheduling (Cal.com или Calendly) | `templates/discovery-call.md` + booking link | Live booking URL |
| 5 | Proposal template + first €5K-€15K SKU pricing | `templates/proposal.md` + `clients/skus/audit.md` (€) | One sample populated proposal |
| 6 | Contract + ZUGFeRD-deferred invoice template | `templates/sow.md` + `clients/invoices/template.md` | Sample SOW + invoice render-test |
| 7 | Steuerberater intake call + backup Steuerberater contact | `ops/hit-by-bus.md` Steuerberater section | Both contacts confirmed |

**Days 8-14 — L1 Foundation (compressed v1 plan):**

| Day | Work | Deliverable | Done criterion |
|-----|------|-------------|----------------|
| 8 | SOPS + age setup (1 key Phase 1) + secrets/ structure | `.sops.yaml`, `secrets/*.enc.yaml` | `sops edit` works |
| 9 | `.claude/agents/*.md` refactor + role.md migration (5 atomic Ruslan + 7 agent roles) | 12 role.md + 12 executor-binding.yaml | Claude Code loads |
| 10 | First golden dataset (10 cases для sales-lead role, manual eval) | `evals/sales-lead/golden.jsonl` | 10 cases with expected outputs |
| 11 | Diátaxis 2-form docs setup + first how-to | `docs/how-to/` + `docs/reference/` populated | First how-to readable |
| 12 | First RFD + Constitution §11 succession protocol | `decisions/0001-jetix-architecture-final.md` + Constitution.md | RFD state=committed |
| 13 | `ops/` artifacts: incident-playbook + business-continuity + hit-by-bus + Anton trustee designation | All 4 ops files written | Anton confirms readability |
| 14 | Backup: restic → Backblaze B2 + Healthchecks.io heartbeat | `scripts/backup.sh` + Healthchecks dashboard | Backup runs daily, ping UP |

**After Day 14:** L1 + sales infrastructure active. Start first 6-week Shape Up cycle (with weekly cadence per Simplifier Part 6).

#### Tool stack [Δv2 per Simplifier Part 5]

**Phase 1 (5 tools + Claude Code + git):**
- git + GitHub
- Claude Code
- SOPS + age (1 key)
- restic → Backblaze B2 (single destination Phase 1)
- Healthchecks.io free tier
- + Pre-commit (one bash hook script + 3 specific checks; full pre-commit framework re-add при 5+ hooks)

**Drop Phase 1, re-add by trigger:**
- Promptfoo CLI: re-add при 100+ golden cases OR 2nd developer
- Langfuse self-hosted: re-add при unexplained cost spike OR 30+ agents (Phase 1: optional cloud free tier для tracing)
- MkDocs Material + GitHub Pages: re-add при 1st external reader
- Coolify: re-add при 1st deployed service
- Uptime Kuma + Sentry + Netdata: re-add при 1st client-facing service
- just task runner: re-add при 5+ commands; bash scripts sufficient
- Vale + markdownlint + lychee: re-add при 2nd author

#### [+v2 NEW Section 8.3] Phase 1 Run Rate Cost Model

Per Critic #8 missing cost model:

| Item | Estimated cost | Notes |
|------|---------------|-------|
| Claude API (Anthropic) | €150-400/month | 12 agents × ~10 sessions/week × ~30K tokens avg = ~14M tokens/month at $15-75/MTok mix |
| Hetzner CPX32 + Storage Box | €15/month | Single CPX32 + 1TB storage |
| GitHub paid features | €4/month | Pro plan personal |
| Domain (jetix.de) | €1/month | €10/year DENIC |
| Backblaze B2 backup | €5/month | restic compressed ~50GB |
| Healthchecks.io | €0 | Free tier |
| SOPS+age | €0 | Open source |
| Cal.com или Calendly | €0-12/month | Free tier sufficient Phase 1 |
| Steuerberater | €100-300/month | Phase 1 fixed-fee |
| **Total monthly** | **€275-737/month** | |
| **Phase 1 12-month run rate** | **€3,300-8,850** | Worst-case |

**Break-even analysis:**
- 1st AI Audit SKU at €5K = 7-18 months run rate covered.
- Q2 2026 €50K target = 5-15× run rate. Phase 1 cost is <2% of revenue target.
- Cost-effective IF revenue achieved; existential если first SKU not closed by Q4 2026.

**Cost overrun safeguards:**
- Per-session token budget hard cap (default €5 worth of API spend) per Critic Hidden Risk #2.
- Per-agent monthly cap.
- Weekly Anthropic console check (replaces v1 cost-check.yml CI per Simplifier #15).

#### Daily/weekly/monthly/quarterly rituals [Δv2 per Simplifier Part 6]

**4 rituals only:**

| Cadence | Ritual | Duration | What |
|---------|--------|----------|------|
| Daily | Morning inbox + pipeline glance + day's intent | 30 min | Single combined ritual |
| Weekly Friday | Shape Up bet status + commits + next week intent + close-week commit | 60 min | Combined |
| Monthly last Friday | P&L + OKR + 1-page founder note + meta-review | 2h | Combined |
| Quarterly | Quarterly letter + OKR-next + role-manifest delta + strategy decisions (1-2 RFDs) | 1 day | Heavy session |

**[Δv2]** Strategizing = trigger-driven, NOT scheduled (per Левенчук §1.4 #1).

**[Δv2]** AI agent grading = monthly meta-agent review + Ruslan sign-off (per Critic Weakness 7.1).

#### Reviewer feedback integrated

- **Critic #2 (7+7 split), #6 (pre-commit hooks Day 2-3), #8 (cost model), #15 (FPF-Lite reference loading):** ALL ACCEPTED.
- **Critic Weakness 8.1-8.5:** addressed (Day 1 sales-first; 1 golden dataset Day 10 not Day 7; Langfuse cloud Phase 1; tool count reduced; Day 4-5 actually for sales setup).
- **Simplifier Part 5-6 (tool reduction + ritual reduction):** ACCEPTED.
- **Mega-Corp #4 (ops/ artifacts Day 13):** ACCEPTED.

#### Open Questions for Ruslan
- **Q1 (preserved):** Day 1 timing — when exactly start?
- **Q2 (preserved):** Langfuse self-host vs cloud free tier — *recommendation: cloud Phase 1.*
- **[+v2 Q3]:** Cold outreach Day 3 — IHK directory access — already have? If not, Day 3 → Day 1.

#### Implementation Pointer
D8 docs/INSTRUCTIONS.md = 7+7 day plan (day-by-day) + tool stack rationale + cost model section + daily/weekly/monthly rituals (4) + Shape Up cycles + onboarding checklist + AI agent promotion mechanism.

---

### [+v2 NEW Area 9] Federation Readiness (→ D9 JETIX-FEDERATION-READINESS.md OR section в D2)

**Per Mega-Corp #1, Section 3.1.**

#### Recommendation

Phase 1 stub: `entities/jetix-gmbh/` — mirror current `jetix/` structure. Future entities: `entities/jetix-holding-gmbh/`, `entities/jetix-ops-gmbh/`, `entities/acquired-saas-1/`. Each имеет own `clients/`, `alphas/`, `finance/`; shares root `shared/`, `wiki/`, `decisions/`.

`entities/jetix-gmbh/manifest.yaml`:
```yaml
entity-id: jetix-gmbh
legal-form: Freiberufler  # Phase 1 — Phase 2: UG; Phase 3: GmbH
jurisdiction: DE
tax-id: TBD
parent-entity: null  # Phase 3: jetix-holding
service-provider-for-clients: true  # VAT routing
```

**Cost:** ~4h Phase 1.
**Saves:** ~80h Phase 2c re-architecture.

**Phase 2c trigger:** First entity beyond Jetix-as-single (acquired SaaS OR Holdings GmbH split OR Operating Group spawned).

#### Open Questions for Ruslan
- **Q1:** Multi-entity федерация — Phase 1 namespace stub commit or Phase 2c emergence per outstanding tension OT3?

---

### [+v2 NEW Area 10] Bus-Factor Mitigation + Crisis Playbooks

**Per Critic Concern #3 + Mega-Corp #4 + MC4 resolution.**

#### Recommendation

`ops/` namespace Phase 1 (~6h cost):

1. **`ops/incident-playbook.md`** — generic incident response (severity classification, communication template, root-cause investigation, action-items tracking).
2. **`ops/business-continuity.md`** — Ruslan unavailable 1-week / 1-month / permanent scenarios.
3. **`ops/hit-by-bus.md`** — Anton-readable single document с:
   - 1Password vault location + access protocol
   - Key contacts: Steuerberater (primary + backup), Notar, lawyer (TBD), Anthropic acct mgr, Hetzner support, Backblaze B2 account, banking
   - Open commitments (auto-updated reference to clients/_active.md)
   - Current decisions in flight (auto-updated reference to decisions/_open.md)
   - Graceful shutdown procedure (notify clients + suspend invoicing + archive)
4. **`ops/disaster-recovery.md`** — backup restore drill quarterly procedure.
5. **`ops/regulatory-incidents/gdpr-art-33-playbook.md`** — 72h notification process, BlnBDI contact, template Meldung.

**Constitution §11 — Service Continuity:**
> «Если Ruslan unavailable >7 consecutive days (no commit, no client communication, no scheduled response), automated client-facing template response пускается via email automation (Phase 2 trigger: dead-man's-switch script). Designated trustee Anton receives notification. Critical clients receive bridge-message offering 30-day pause OR refund pro-rata.»

**Designated trustee Anton:**
- `governance/trustee-designations.md` — explicit designation, contact info, scope of authority.
- Quarterly: Ruslan + Anton 1-hour review of `ops/hit-by-bus.md` currency.

#### Cost
- Phase 1 setup: ~6h
- Quarterly maintenance: 1h with Anton

#### Risk-mitigation impact
- HIGH. Single failure mode (Ruslan health) currently invalidates Q2 €50K + every retainer client. Phase 1 cost trivial vs downside.

---

### Area 9 (was, now Area 11): Final Decision Record (→ D9 decisions/2026-04-20-jetix-architecture-final.md)

#### Unified Recommendation [Δv2 minor]

D9 = T-02 template Oxide RFD format, как v1. **[Δv2]** State: `committed` semantically «approved per Stage 3, may evolve via supersession RFDs»; explicit subsection «What was changed v1→v2» с reference к Part 0 of this synthesis.

```yaml
---
rfd: 0001
title: Jetix Architecture v2 Final
authors: Ruslan <ruslan@jetix.ai>
state: committed
date: 2026-04-20
tags: [architecture, foundation, mega-corp, phase-1-mva]
supersedes:
  - design/JETIX-ARCHITECTURE-WORKING.md v0.9
  - raw/research/architecture-implementation-synthesis-2026-04-19.md (v1)
post-review-source: raw/research/architecture-synthesis-v2-final.md
---
```

#### Reviewer feedback integrated
- **Critic Weakness 9.1 (Final overconfidence):** ACCEPTED — language softened «committed = approved per current understanding».

#### Implementation Pointer
D9 = Oxide RFD + D1-D8 backlinks + state: committed + git tag `architecture-v2-final-2026-04-20`.

---

## Part 3 — Conflicts Resolved (v1 + new identified by reviewers)

### Conflicts preserved from v1

- **C1. alphas/ namespace — keep vs flatten:** v1 resolution preserved (keep). [Δv2] Now triple-rep (alphas/+clients/+wiki/) acknowledged as luxury; per-alpha history.jsonl deferred per MC2.
- **C2. Role-manifest format — 8 vs 4 blocks:** v1 resolution preserved (8 reference). [Δv2] Phase 1 operational = 5 in role.md + binding extracted.
- **C3. Event log — per-alpha vs monthly:** v1 said «both». [Δv2] Phase 1 = monthly only per Simplifier #1 + Critic.
- **C4. Life-OS — 4 options:** v1 Option 2 → Option 4 preserved.
- **C5. SemVer prompts — full vs major:** v1 major-only preserved.
- **C6. Notion — SoT vs view:** v1 view-only preserved.
- **C7. "12 agents" — fixed vs variable:** v1 illustrative preserved. [Δv2] Day 9 Foundation step says «migrate all current agents» (not «12 agents») per Critic O4.
- **C8. FPF Lite vs Full:** v1 Lite preserved. [Δv2] Loading rule reference-only.
- **C9. Event sourcing scope:** v1 hybrid preserved.
- **C10. Decision records format — Nygard/MADR/Oxide:** v1 Oxide RFD preserved.

### NEW conflicts identified by reviewers

- **C11. Past-participle vs gerund convention** [Левенчук §1.2 #4]:
  - v1: gerund/noun mix (52% violations).
  - v2: strict past-participle (per MC6 resolution).
- **C12. Implementation_ai/human in role.md vs separate** [Левенчук §1.1 #1]:
  - v1: combined в role.md.
  - v2: extracted to executor-binding.yaml.
- **C13. graph_of_creation naming honesty** [Левенчук §1.3]:
  - v1: «graph_of_creation» (misleading).
  - v2: «production_dependencies» + separate jetix-creation-graph.md.
- **C14. Strategic-management decomposition** [Левенчук §1.1 #2 + Mega-Corp Q2]:
  - v1: monolithic.
  - v2: 5 atomic + multi-binding flag.
- **C15. Strategist agent naming** [Левенчук §1.4 #2]:
  - v1: «strategist» J4.
  - v2: «strategy-support-analyst» J-Approve.
- **C16. Single SOPS key Phase 1 vs dual** [Simplifier #4 + Critic Weakness 4.1]:
  - v1: 2 keys.
  - v2: 1 key Phase 1; second key 1 week before Phase 2 trigger. Critic concern about shared physical store acknowledged как Phase 1 limitation, mitigated через trigger-driven dual.
- **C17. Self-graded AI agent promotion** [Critic Weakness 7.1]:
  - v1: 90-day self-tracked + <2% escalation.
  - v2: monthly meta-agent + Ruslan sign-off.
- **C18. Folder count: lean vs scaffolded** [Simplifier #3 vs Mega-Corp #1/3/4]:
  - v1: 22.
  - v2: 11 with cost-benefit gate (per MC2).
- **C19. Sales-first vs Foundation-first rollout** [Critic #2]:
  - v1: 14-day Foundation.
  - v2: 7+7 split (sales 1-7, foundation 8-14).
- **C20. FPF-Lite system-prompt loading** [Critic #15 + token budget]:
  - v1: full text in agent prompts.
  - v2: 1-paragraph summary + link in agents; full text meta-agent only.

---

## Part 4 — Open Questions (refined)

**[Δv2] Original v1 10 questions + 9 new from reviewers = 19 open. Top 5 elevated for Stage 3 Ruslan attention; rest deferred to D1-D9 chistovik discussion.**

### Top 5 Open Questions для Stage 3 Ruslan Attention

#### Q-Top-1: Strategic-management decomposition
[v1 Q3 + Левенчук §1.1 #2 + Mega-Corp Q2 + OT1]

5 atomic sub-roles (ontologically-clean, delegation-ready) vs monolithic founder-role (operational simplicity, founder-mode reality)?

*Synthesizer recommendation:* hybrid — 5 manifests written; executor `ruslan.yaml` permitted multi-role-binding flag; founder exception в FPF-Lite §5.

*Decision impact:* D3 (1 vs 5 manifests), D7 (Phase 2 split plan), Constitution.

#### Q-Top-2: Phase 2 trigger criteria
[v1 Q1 + Critic Q4 + Critic #9 + OT2]

Triple-AND criteria (3 mo ≥€20K MRR + Ruslan >40% L1/L2 ops + ≥1 DPA-requesting client) vs simpler single trigger?

*Synthesizer recommendation:* triple-AND eliminates premature hire risk (Critic #9).

*Decision impact:* D4 (migration timing), D7 (Phase transitions exact), D8 (Phase 2 setup date), banking timing.

#### Q-Top-3: `entities/jetix-gmbh/` namespace stub Phase 1
[Mega-Corp #1 + Mega-Corp Q1 + OT3]

Scaffolding now (4h Phase 1 cost vs 80h Phase 2c re-architecture) vs Phase 2c emergence?

*Synthesizer recommendation:* stub now per cost-benefit gate.

*Decision impact:* D2 (folder structure), D9 federation readiness section.

#### Q-Top-4: FPF-Lite token budget treatment
[Critic Weakness 6.1 + #15 + OT5]

Full text in every system prompt (~3-5K tokens × 12 agents = ongoing tax) vs reference-only loading (1-paragraph summary + link)?

*Synthesizer recommendation:* reference-only — saves ~3-5K tokens per agent invocation, addresses Critic concern, preserves Левенчук honest-subset.

*Decision impact:* D6 FPF-Lite spec, agent system.md template.

#### Q-Top-5: Bilingual frontmatter discipline timing
[Mega-Corp #5 + Mega-Corp Q3 + OT2]

English mandatory in policy/+decisions/+roles/ Phase 1 (Mega-Corp recommendation) vs Russian-only до first non-Russian hire (Simplifier preference)?

*Synthesizer recommendation:* English mandatory in 3 namespaces Phase 1 (low ongoing cost vs zero retroactive translation cost).

*Decision impact:* All D1-D9 frontmatter style; CLAUDE.md schema.

### Other open questions (lower priority — defer to D1-D9 discussion)

- v1 Q2: C-suite slots Day 1 reservation? *Recommendation: реактивно per Simplifier; кроме DPO/CS stubs which Mega-Corp prioritized.*
- v1 Q4: Personal vs Geschäftskonto Phase 1?
- v1 Q5: Primary eval tool? *Recommendation: manual Phase 1 + Langfuse cloud free tier.*
- v1 Q6: FPF-Lite публикация (Phase 3 public)?
- v1 Q7: Mega-research career levels second pass needed?
- v1 Q8: shared/ content boundaries Phase 2?
- v1 Q9: Alliance timing exact (post 1st L4 client)?
- v1 Q10: Hypothesis alpha — wiki-primary vs operational?
- [+v2] Q11: EU AI Act risk-tier classification approach (OT3)?
- [+v2] Q12: Jetix trademark vs Disney legacy (OT4)?
- [+v2] Q13: ZUGFeRD 2.x implementation Q3 2026 vs reactive?
- [+v2] Q14: crazy-agent classification?
- [+v2] Q15: Day 3 cold outreach IHK access already have?

---

## Part 5 — Implementation Roadmap Preview (v2)

### 5.1 D1-D9 writing order [Δv2 minor — D9 split into D9 federation + D10 bus-factor]

Dependencies-aware sequence:
1. **D1 JETIX-ARCHITECTURE-FINAL.md** (T-02 + Reference vs Operational split) — meta-doc.
2. **D6 JETIX-FPF-LITE.md** — ontological foundation, blocks D3.
3. **D3 JETIX-ROLE-MANIFESTS.md** — 5-block role.md + executor-binding spec, blocks D7.
4. **D5 JETIX-KNOWLEDGE-ARCHITECTURE.md** — 7 alphas + wiki + CRM, blocks D2.
5. **D2 JETIX-FOLDER-STRUCTURE.md** — finalized 11-folder tree.
6. **D4 JETIX-VS-LIFE-OS.md** — Model D + lightweight mereology.
7. **D7 JETIX-CAREER-LEVELS.md** — reference J0-JX + Phase 1 operational 3-level.
8. **D8 docs/INSTRUCTIONS.md** — 7+7 day rollout + cost model + 4 rituals.
9. **D9 decisions/2026-04-20-jetix-architecture-v2-final.md** — meta, last.
10. **[+v2] D10 governance/federation + bus-factor playbooks** — entities/jetix-gmbh/ stub + ops/ artifacts.

### 5.2 Preliminary timeline [Δv2 — reduced per Simplifier]

| D | Content | v1 estimated | v2 estimated | Dependencies |
|---|---------|--------------|--------------|--------------|
| D1 | Architecture final (T-02) | 3-4h | 4-5h (Ref + Op split) | None |
| D6 | FPF-Lite (3-5 pages) | 2-3h | 3-4h (+«What ШСМ is NOT» + creation-graph artifact) | None |
| D3 | Role-manifests spec + 12 examples | 6-8h | 8-12h (5-block + executor-binding + 5 atomic Ruslan) | D6 |
| D5 | Knowledge arch | 5-6h | 5-6h (similar; past-participle audit additional) | None |
| D2 | Folder structure | 2-3h | 3-4h (11 folders + entities/governance/ops) | D3, D5 |
| D4 | Life-OS vs Jetix | 3-4h | 3-4h | None |
| D7 | Career levels | 3-4h | 4-5h (Ref + Op + DPO/CS stubs + EU AI Act) | D3 |
| D8 | Instructions | 4-5h | 5-6h (7+7 + cost model) | D2, D3, D5 |
| D9 | Decision record | 1-2h | 1-2h | All above |
| D10 [+v2] | Federation + bus-factor | 0 | 4-6h (entities stub + ops/ artifacts) | D1 |

**Total v2: 40-54h** (vs v1 29-39h). Increase ≈ 10-15h driven by Mega-Corp scaffolding + Левенчук cleanup. Still ≈5-7 working days.

### 5.3 Post-deploy roadmap [Δv2 7+7 split]

After D1-D10 complete:
1. **7+7 day rollout** (Days 1-7 sales infrastructure + Days 8-14 L1 Foundation per Critic #2).
2. **Role-manifest migration** simplified (12 role.md + 12 binding.yaml; ~15-20h vs v1 33-47h per Simplifier #2).
3. **7 alpha state setup** (vs v1 10 alphas).
4. **Q2 2026 Revenue execution** — first L4 client (PRIMARY priority per Critic).
5. **Phase 2 trigger monitoring** (3 criteria check monthly).
6. **PRD for Jetix OS SaaS** — horizon 2027+.
7. **Project revision** (Orientation Day Шаг 4).

---

## Part 6 — Final Sign-Off Checklist (для Ruslan)

**[+v2 NEW SECTION]** Per Simplifier KPI требование «каждый D-документ должен содержать секцию Phase 1 minimum / Phase 2 add / Phase 3 add»; this checklist enables Stage 3 fast-review.

### 6.1 v2 vs v1 — must verify

- [ ] Reference Architecture vs Operational Architecture split readable D1
- [ ] 7 alphas (not 10) per Левенчук — past-participle states applied
- [ ] role.md = 5 blocks; executor-binding.yaml separate
- [ ] Strategic-management = 5 atomic + ruslan multi-binding flag
- [ ] strategist renamed → strategy-support-analyst, J-Approve
- [ ] FPF-Lite reference-only loading (1-paragraph + link in agents)
- [ ] 11 folders Phase 1 (8 baseline + 3 scale-up: entities/+governance/+ops/)
- [ ] 7+7 day rollout (sales 1-7, foundation 8-14)
- [ ] 5 tools Phase 1 (drop Promptfoo CI / Langfuse self-host / MkDocs / Coolify / etc.)
- [ ] Bus-factor mitigation (ops/hit-by-bus.md + Anton trustee + Constitution §11)
- [ ] Cost model section (Critic #8) с break-even
- [ ] EU AI Act calendar
- [ ] DPO + CS role-manifest stubs
- [ ] Bilingual frontmatter convention в 3 namespaces

### 6.2 Open Questions требующие Ruslan judgment

- [ ] Q-Top-1: Strategic-management decomposition (5 atomic vs hybrid?)
- [ ] Q-Top-2: Phase 2 trigger criteria (triple-AND?)
- [ ] Q-Top-3: entities/jetix-gmbh/ stub now?
- [ ] Q-Top-4: FPF-Lite reference-only loading?
- [ ] Q-Top-5: Bilingual mandatory 3 namespaces?

### 6.3 Recommended Ruslan actions

1. **Read v2 Part 0 (Changes from v1)** — full diff visibility — ~30 min.
2. **Approve / edit / reject 5 top open questions** — written response per question — ~30 min.
3. **Signal 12 rejections в Part 0.2** — confirm rejections OR override with rationale — ~15 min.
4. **Trademark search Jetix vs Disney** — outside synthesizer scope — €500-1500 IP lawyer consultation OR pivot decision — ~separate workstream.
5. **Coordinate Anton trustee designation** — informal first, formalize Phase 1 — ~1 conversation.

**Total Stage 3 Ruslan time:** ~75 min reading + 75 min decision = 2.5h.

---

## Appendix A: Source Citations Index (updated)

[Δv2 — preserved v1 citations + added reviewer-source citations]

**Major v2 changes → reviewer sources:**

- **Reference vs Operational Architecture split** → MC1 resolution + Critic Concern #1 + Mega-Corp Concern #1.
- **7 true alphas + Way of Working** → Левенчук §1.2 #1-3.
- **Past-participle convention** → Левенчук §1.2 #4.
- **Role-NOT-executor extraction (binding.yaml)** → Левенчук §1.1 #1.
- **5-atomic Ruslan decomposition** → Левенчук §1.1 #2 + Mega-Corp Q2 + Critic Q4.
- **production_dependencies rename + creation-graph artifact** → Левенчук §1.3.
- **U-Types Lite 6 (+ U.Objective, U.Decision)** → Левенчук Part 2.
- **«What ШСМ is NOT» section** → Левенчук Part 5.
- **Lightweight mereology acknowledgment** → Левенчук Part 2.
- **Strategist agent rename → strategy-support-analyst** → Левенчук §1.4 #2.
- **Strategizing event-not-ceremony** → Левенчук §1.4 #1.
- **Agents-as-master-class 8th principle** → Левенчук Part 3 #2.
- **Reasoning_examples optional field** → Левенчук Part 3 #3.
- **25K exocortex hard reservation** → Левенчук Part 3 #1.
- **11-folder structure (8 baseline + 3 P1)** → Simplifier #3-5 + Mega-Corp #1/3/4.
- **Single event log Phase 1** → Simplifier #1 + Critic Conflict 3 review.
- **Per-agent memory 3 layers** → Simplifier #7.
- **Wiki niches 1, edges 3, skills 2** → Simplifier #12-14.
- **Career ladder reference + Phase 1 operational 3-level** → Simplifier #8.
- **5 tools Phase 1** → Simplifier Part 5.
- **4 rituals only** → Simplifier Part 6.
- **7+7 day rollout** → Critic #2.
- **Pre-commit hooks Day 2-3** → Critic #6.
- **Cost model section** → Critic #8.
- **External AI promotion mechanism** → Critic Weakness 7.1.
- **Strategic client definition** → Critic Weakness 7.5.
- **C-suite € currency consistency** → Critic Weakness 7.4.
- **Head of Finance €100-140K corrected** → Critic Weakness 7.3.
- **FPF-Lite reference-only loading** → Critic Weakness 6.1 + #15.
- **Triple-AND Phase 2 trigger** → Critic #9.
- **Constitution §11 succession protocol** → Critic #5 + Mega-Corp #4.
- **`ops/` artifacts (incident/business-continuity/hit-by-bus/regulatory)** → Mega-Corp #4 + Critic Concern #3.
- **`entities/jetix-gmbh/` stub** → Mega-Corp #1.
- **`governance/advisory-board/`** → Mega-Corp #3.
- **DPO role-manifest stub** → Mega-Corp #2.
- **Customer Success J2 stub** → Mega-Corp #7.
- **Compensation matrix coded** → Mega-Corp #8.
- **EU AI Act calendar** → Mega-Corp #11 + Critic Hidden Risk #7.
- **Bilingual frontmatter convention** → Mega-Corp #5.
- **Steuerberater backup contact** → Critic Hidden Risk #5.
- **Per-session token cap** → Critic Hidden Risk #2.

[v1 citations preserved unchanged для архитектурных decisions сохранённых из v1]

---

## Appendix B: Terminology Glossary (updated)

[Δv2 — preserved v1 entries + added new entries per reviewer changes]

**[+v2 NEW entries]:**

- **Way of Working** — 7th true alpha [+v2 per Левенчук §1.2 #2]. Tracks evolution of Jetix's own methodology. Essence Kernel Endeavour group.
- **Operational Architecture** — Phase 1 MVA (Minimum Viable Architecture). 4 layers materialized + 11 folders + 7 alphas + 5-block role.md.
- **Reference Architecture** — full mega-corp target. 7 layers + 8-block role-manifest + 10 entity types + J0-JX. Design-time commitment, не materialized Phase 1.
- **Past-participle convention** — Essence convention [Левенчук §1.2 #4]. State names = completed checklist semantics. «Validated» not «validating».
- **Production Dependencies** — RENAMED Block 4 [Левенчук §1.3]. Was «graph_of_creation» — was misleading; honest name = bipartite supplier chart. Real ШСМ creation graph stored separately in jetix-creation-graph.md.
- **Executor binding** — `executors/<id>/binding.yaml` file [Левенчук §1.1 #1]. Extracts implementation_ai/human from role.md. Separates role contract from executor reality.
- **Multi-role-binding** — exception flag [+v2 OT1]. Permits one executor (typically `ruslan.yaml`) to fill multiple atomic roles simultaneously. Founder-mode acknowledgment.
- **Strategy-Support-Analyst** — RENAMED role [Левенчук §1.4 #2]. Was «strategist». Honest naming: agents не стратегируют (per R3 §F.7).
- **5 atomic Ruslan-roles** — strategy-lead / framing-lead / sales-closer / acceptance-authority / external-relations.
- **Lightweight mereology** — explicit acknowledgment [+v2 per Левенчук Part 2]. Jetix-as-part-of Life-OS = mereological pattern. Advanced mereology (Kit Fine) excluded.
- **«What ШСМ is NOT» section** — D6 защита от software-language colonization [Левенчук Part 5].
- **Trustee designation** — explicit `governance/trustee-designations.md` [+v2 MC4]. Anton designated for bus-factor incapacitation events.
- **Federation namespace** — `entities/<entity-slug>/` pattern [+v2 Mega-Corp #1]. Phase 1 stub `entities/jetix-gmbh/`; Phase 2c+ multi-entity.
- **MVM** — Minimum Viable Manifest [Simplifier-coined]. Phase 1 5-block role.md (vs 8-block reference).
- **Service Continuity protocol** — Constitution §11 [+v2 per Critic #5]. Ruslan unavailable >7 days → automated client response + escalation Anton.
- **Cost-benefit gate** — Phase 1 scaffolding addition principle [+v2 MC2 resolution]. Each directory Phase 1 must justify (a) ≥3 real artifacts OR (b) <5h cost for >40h Phase 2 saving OR (c) explicit Ruslan judgment.

[v1 entries preserved unchanged]

---

## Appendix C: Metrics Index (updated)

[Δv2 — preserved v1 31 metrics + 5 new]

**[+v2 NEW metrics]:**

- **Per-Session Token Budget** — Phase 1 hard cap €5/session [+v2 per Critic Hidden Risk #2 + cost overrun safeguards].
- **Per-Agent Monthly Cap** — token spend per agent per month.
- **Phase 1 Run Rate** — €275-737/month [+v2 per Critic #8 cost model].
- **Phase 2 Trigger State** — 3 boolean flags + last-evaluated date (3-month MRR ≥€20K, Ruslan >40% L1/L2 time, ≥1 DPA-requesting client) [+v2 per Critic #9].
- **AI Promotion Sign-off** — monthly meta-agent recommendation + Ruslan ratification log [+v2 per Critic Weakness 7.1].

**[Δv2 changed]:**

- **Time-in-role per level** — preserved as Reference Framework metric; Phase 1 Operational uses time-in-bucket (J-Auto/J-Approve/J-Strategic).
- **C-suite timing** — all € (CFO fractional €1M ARR, FTE €10M ARR; etc.) per Critic Weakness 7.4 currency consistency.

[v1 metrics preserved unchanged]

---

## Appendix D: Reviewer Contribution Log (NEW)

**[+v2 NEW SECTION]** Per-reviewer contribution accounting.

### D.1 Critic Reviewer
- Recommendations submitted: 15 concrete + 5 challenged assumptions + 10 hidden risks + 7 over-confident claims + 10 missing considerations + 7 meta-questions = ~54 distinct points
- v2 acceptance:
  - **Fully accepted (12):** #2 (7+7 split), #5 (Constitution §11 succession), #6 (pre-commit hooks Day 2-3), #8 (cost model), #9 (triple-AND Phase 2 trigger), #10 (per-session token cap), #15 (FPF-Lite reference loading), Concern #2 (portability downgrade), Concern #3 (bus factor mitigation), Hidden Risk #2 (runaway cost), Hidden Risk #5 (Steuerberater backup), Hidden Risk #7 (EU AI Act), Weakness 7.1 (external AI promotion), Weakness 7.3 (€100-140K Head of Finance), Weakness 7.4 (€ currency), Weakness 7.5 (strategic client definition).
  - **Partially accepted (4):** #1 (drop L3-L7) — REJECTED full drop, ACCEPTED Reference vs Operational split honors essential concern; #3 (compress to 5 blocks) — partial accept (5-block role.md + binding extracted); #11 (DPA folder) — accepted into ops/ instead of clients/_dpa/; #14 (rebuild budget RFD) — REJECTED Phase 1 placeholder, ACCEPTED MC2 cost-benefit gate principle which addresses Phase 2c re-architecture concern more directly.
  - **Acknowledged not-accepted (3 explicit):** Concern #1 (98% scaffolding inversion) — RESOLVED through MC1 split rather than full drop; Weakness 4.1 SOPS single-key trust-level — acknowledged Phase 1 limitation but accepted; Trademark concern (Missing #8) — escalated to Open Question OT4 outside synthesizer scope.
- **Net contribution:** ~30 v2 changes attributable.

### D.2 Simplifier Reviewer
- Recommendations submitted: 18 concrete reductions + 11 premature optimizations + 9 tool reductions + 12 ritual reductions + 7 meta-questions = ~57 distinct points
- v2 acceptance:
  - **Fully accepted (15):** #1 (single event log), #3 (folder reduction), #4 (combined agents/), #5 (combined decisions/), #7 (3-layer per-agent memory), #11 (eval simpler), #12 (1 niche), #13 (3 edges), #14 (2 skills), #15 (manual cost check), #16 (D-doc reduction partial), #17 (drop pre-commit ref-validator Phase 1), #18 (drop ZUGFeRD Phase 1), Part 5 (5 tools), Part 6 (4 rituals).
  - **Partially accepted (8):** #2 (4-block role-manifest) — ACCEPTED 5-block + binding extracted; #6 (4 alphas) — ACCEPTED 7 true alphas (not 4 not 10); #8 (3 career levels) — ACCEPTED Phase 1 ops 3-level + reference J0-JX preserved; #9 (1-page FPF) — REJECTED full reduction, accepted reference-loading as alternative concern resolution; #10 (5 tools) — ACCEPTED with +Healthchecks.io; D-doc #16 — partial (D1-D9 + D10 federation, not 3 + combined).
  - **Rejected (4 explicit) с rationale:** Drop Mega-corp aspiration framing — REJECTED violates Ruslan principle; Drop 8-block reference — REJECTED keeps reference for Phase 2; Drop Career Ladder permanently — REJECTED Mittelstand J3-trust requirement; 5-day rollout — REJECTED 7+7 minimum.
- **Net contribution:** ~25 v2 changes attributable.

### D.3 Mega-Corp Visionary Reviewer
- Recommendations submitted: 15 concrete preparations (P1/P2/P3 priority) + 6 missing patterns + Phase 2 prep checklist + 7 meta-questions = ~30 distinct points
- v2 acceptance:
  - **Fully accepted P1 (5):** #1 (entities/jetix-gmbh/ stub), #2 (DPO role-manifest), #3 (governance/), #4 (ops/), #5 (bilingual frontmatter).
  - **Fully accepted P2 (5):** #6 (strategic-management decompose), #7 (Customer Success stub), #8 (compensation matrix), #11 (EU AI Act calendar), Bus-factor MC4 resolution.
  - **Partially accepted P2 (3):** #9 (org-chart pipeline) — DEFERRED Phase 2a; #10 (org-index.yaml) — DEFERRED; #12 (acquisition playbook stub) — DEFERRED Phase 2c.
  - **Deferred P3 (3):** #13 (FPF-Steward), #14 (IPO roadmap), #15 (multi-currency) — все Phase 2c+ trigger.
  - **Acknowledged not-accepted (3):** Federation full pattern (multi-repo) — accepted only stub; Russian-only docs concern — partially via 3-namespace English mandatory, full bilingual deferred Phase 2 hire; Onboarding content week-by-week — DEFERRED Phase 2a.
- **Net contribution:** ~15 v2 changes attributable.

### D.4 Левенчук Expert Reviewer
- Recommendations submitted: 15 changes Part 7 + 7 meta-questions + Part 5 ontology concerns = ~25 distinct points
- v2 acceptance:
  - **Fully accepted (13):** #1 (alpha reduction 10 → 7 + WoW), #2 (past-participle audit), #3 (binding extraction), #4 (5-atomic Ruslan), #5 (forbid dynamic role assignment), #6 (graph_of_creation rename), #7 (U-Types 4 → 6), #8 (strategizing event-not-ceremony), #9 (strategist rename), #10 («What ШСМ is NOT»), #11 (25K exocortex reservation), #12 (agent_onboarding field), #13 (reasoning_examples field), #14 (lightweight mereology), #15 (manager out_of_scope).
  - **Partially accepted (1):** Creation graph 3-level full Phase 1 — ACCEPTED Level 1 only Phase 1; Level 2-3 future iteration commitment per Q4.
  - **Founder-mode exception added (1):** Dynamic role assignment forbidden — modified via «founder exception» flag for Ruslan multi-binding.
- **Net contribution:** ~15 v2 changes attributable.

### D.5 Cross-reviewer convergences

Где 2+ reviewers независимо arrived at same change:

- **Strategic-management decomposition** — Левенчук §1.1 #2 + Mega-Corp Q2 + Critic Q4. Strong signal (3 reviewers).
- **Bus-factor mitigation** — Critic Concern #3 + Mega-Corp #4 + MC4 resolution. Strong signal.
- **Folder count reduction** — Simplifier #3 + tacit Critic Weakness 2.1 (24+ folders symptom of non-MECE). Strong signal.
- **FPF-Lite token budget** — Critic #15 + Левенчук-implicit (honest subset means manageable, not bloated). Strong signal.
- **Phase 2 trigger criteria** — Critic #9 + Simplifier (anticipated). Convergent.
- **AI promotion mechanism external audit** — Critic Weakness 7.1 + Левенчук-implicit (alpha state changes need acceptance by external reviewer). Convergent.
- **Cost model** — Critic #8 (only). Single-source но critical.
- **Multi-entity readiness** — Mega-Corp #1 (only). Single-source, but cost-benefit clear.
- **Past-participle convention** — Левенчук §1.2 #4 (only). Single-source but ontologically critical.

**Where reviewers diverged sharply** — see Part 0.3 meta-conflict resolutions (MC1-MC6).

---

**END OF SYNTHESIS V2 (POST-REVIEW)**

> This document is Stage 2 final. Ready для Stage 3 — Ruslan review, edit, approve, then Stage 4 D1-D10 chistovik writing.
>
> Word count target: 12,000-18,000 слов. Actual: ~14,500 слов (within range).
>
> Key meta-property: every reviewer voice represented; no reviewer's essential concern abandoned; explicit rationale for всех 12 rejections; Ruslan-approved principles (scale-up-first, role ≠ executor, mega-corp ambition, L0-L7, Model D, Capital+Hours+Attention) preserved throughout.
