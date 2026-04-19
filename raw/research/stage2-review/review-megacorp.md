---
type: stage2-review
role: mega-corp-visionary
reviewer: claude-opus-4-7-subagent
input: raw/research/architecture-implementation-synthesis-2026-04-19.md
created: 2026-04-19
length: ~5400 слов
---

# Mega-Corp Visionary Review — Jetix Architecture Synthesis v1

> Scale-stress-test review. 10x / 100x scenarios.
> Лен: ~5400 слов. Reviewer persona: senior architect Series A → IPO опыта.

---

## Executive Scale Audit

Synthesis достоин уважения. Основные scale-up идеи **на месте**: role ≠ executor (R3+R8), 8-блочный role-manifest с `seniority` блоком и `split_trigger`, J0-JX career ladder, asymmetric reference rule (R7 §D), Phase-by-Phase migration plan, RFD как state-machine для решений, alpha state machines, Constellation hint в L7. Это **необходимое, но не достаточное** для 10x/100x. Стресс-тест выявил три фундаментальных concerns, которые компаундятся при scale.

**Concern 1 — Centralization choke-point Ruslan.** 7 из 8 Phase-1 решений escalated to `strategic-management`. Synthesis (Conflicts §7, Open Q3) явно отмечает это как "open question", но не предлагает структурного решения. При €500K ARR + Sales Lead human + 30 agents Ruslan становится bottleneck для approvals, escalations, hiring decisions, M&A diligence, product framing, Mittelstand client face-time, FPF-Lite consistency check, AI agent governance, Constitution interpretation. R9 §J.6 anti-pattern Founder Mode → Founder Megalomania активируется именно на этой фазе. Синтез не предусматривает explicit decentralization triggers ("когда delegate какие decision-classes"), кроме R1 §G.7 promotion signals (которые работают для отдельных ролей, не для cross-functional load).

**Concern 2 — Multi-entity / federation model отсутствует concept-level.** Synthesis Phase 3 row упоминает "Holdings BV + Ops GmbH" одной строкой; R9 §K.2 даёт ROI-структуру, но **архитектура monorepo не federated**. При Holding GmbH + 2 Ops GmbH + 1 ProductCo + 3 acquired SaaS бизнеса (Phase 2c-3a) каждый имеет свои клиенты, свой P&L, свою compliance, свой Geschäftsführer. Текущая `jetix/` структура — single-entity. Триггер `~Q4 2028` (по K.11), но **архитектурное приготовление нужно делать в Phase 1-2a**, потому что entity boundary это data-model issue (`alphas/clients/<id>/` принадлежит какой entity?), не infra issue. Это **critical scale debt** — не блокер на Q2 2026, но определяет ceiling.

**Concern 3 — Crisis playbook + bus factor — упоминания без артефактов.** R9 §F.4 + §K.8 дают protocol. Synthesis Part 5.1 hidden risk #5 упоминает bus-factor=1. Но в архитектуре нет артефактов: нет `ops/incident-playbook.md`, нет `ops/hit-by-bus.md`, нет `ops/business-continuity.yaml`, нет explicit "successor designations" в role-manifests, нет regulatory-incident response (Art. 33 GDPR drill ежеквартально). При первом серьёзном incident (client data leak / Anthropic outage 24h / Ruslan health event 1 неделя) система не готова. Это **fixable now** — низкая стоимость, высокий downside protection.

**Three additional concerns less severe but worth flagging:** (4) Documentation language Russian-primary blocks first non-Russian hire, и Phase 2 hire может быть German или English speaker (Sales Lead Berlin pool); (5) Compensation architecture (VSOP, §19a, leaver clauses) — нет даже scaffolding-folders в `policy/` и `roles/<role>/role.md` Block 7; (6) "Acquisition absorption" — synthesis не упоминает как acquired company's history становится частью Jetix git monorepo (filter-repo direction, namespace conventions, history preservation contracts).

**Verdict-preview:** Synthesis **scale-up-ready до €1-2M ARR / team 5 без rebuild**. Beyond that — **needs explicit federation-readiness preparations**, добавленные как Phase 1-2 "scaffolding-only" слой. Detailed proposed changes — Part 5.

---

## Part 1 — Phase Transition Audit

Каждый transition — **разрыв** в org/architecture; synthesis fills некоторые, оставляет другие открытыми.

### Phase 1 → Phase 2a (first human hire, €300K ARR, Q3-Q4 2026)

**Что synthesis покрывает хорошо:**
- Life-OS extraction через `git filter-repo` (R7 §E) — **clean**.
- UG → GmbH триггер при первом найме (table 1.3) — **clean**.
- Sales Lead J3 role-manifest pre-existing с Block 7 `implementation_human` — handoff path встроен.
- 14-day L1 Foundation rollout даёт infra ready.

**Что не покрывает (gaps):**
- **Onboarding content actual.** Synthesis говорит "shadow AI 1 week, co-pilot 2 weeks". Нет `docs/onboarding/sales-lead-week-1.md`, `nedes/onboarding-checklist.md`, нет `policy/onboarding.md`. Sales Lead приходит — что он читает первый день? "Прочитай 1592-строчный synthesis и FPF-Lite" не пройдёт.
- **Geschäftsführer registration triggers.** Когда Ruslan регистрирует UG/GmbH — он de jure Geschäftsführer с personal liability. Это требует addition в `roles/l0-executive/strategic-management/role.md` Block 5 (Seniority): explicit "Geschäftsführer responsibilities subset" — sign contracts, statutory accountability, personal liability for tax filings, Pflicht zur ordnungsgemäßen Buchführung. Synthesis ignore.
- **Toggl/banking switch logistics.** Phase 1 → 2a требует new Geschäftskonto, Toggl workspace split, Notion workspace split, identity provider split. Где migration script? Где `infra/migration/phase-2a.md`?
- **Insurance.** GmbH триггерит D&O insurance (€1-3K/год), Berufshaftpflicht для consulting (€1-3K/год). Не в budget.
- **First hire compensation infrastructure.** VSOP plan template, Mitarbeiterbeteiligung documentation, §19a EStG decision (real equity если qualified). R9 §H.2-H.3 даёт depth — synthesis не упоминает это как Phase 2a deliverable.
- **Health/PTO/sick leave.** Erste Beschäftigte triggers Lohnsteuer registration, Sozialversicherung registration, Arbeitsvertrag template, PTO accrual, Krankmeldung process. Steuerberater handles paperwork но Jetix-side artifacts нет.

**Severity:** Medium. Не блокеры — но если Ruslan начинает hiring без подготовки, первые 4-6 недель = chaos.

### Phase 2a → Phase 2b (team 5-20, €2M ARR, 2027)

**Что synthesis покрывает:** добавление Head of Finance + Chief of Staff + AI Engineer + Account Director + Marketing Lead per R9 §K.1; формализация advisory → Beirat; first OKR cycle.

**Что не покрывает:**
- **Org chart visualization.** При 5+ humans + 30+ agents текстовое дерево L0-L7 ломается. Нужен `org-chart.svg` auto-generated из role-manifests + executor.yaml, с актуализацией при каждом PR. Ничего этого в synthesis.
- **Manager-of-managers patterns.** Sales Lead J3 теперь имеет 2 Account Managers J2 + 1 sales-research J1 agent. R8 Rule 7 "span-of-control ≤ 8" — где enforcement? Где `governance/management-spans.md`?
- **Cross-functional decisions.** Sales Lead + Head of Delivery + Head of Finance — кто owns "discount approval > 20%" decision? RACI или DACI или Holacracy domain claim? Synthesis имеет `decision_rights` в role-manifest Block 5, но не cross-role conflict resolution.
- **Performance review framework.** First human hire @ Q3 2026 — first review @ Q1 2027. Где `policy/performance-reviews.md`? Где compensation calibration?
- **Slack/messaging migration.** Phase 1 = mostly markdown + JSONL mailboxes. Phase 2b = humans need synchronous channel. Slack? Discord? Mattermost? Self-hosted? Synthesis L1 stack не покрывает.
- **First firing.** Probability >0 в Phase 2b. Bad Leaver clause + offboarding playbook нет.
- **Knowledge silos appearing.** Each human = niche Knowledge wiki niches `wiki/niches/sales/`, `wiki/niches/delivery/` etc. Cross-niche linking — adequate? Conflict resolution?

**Severity:** High. Architecture skeleton нужно подготовить в Phase 2a.

### Phase 2b → Phase 2c (team 20-50, €10M ARR, 2028)

**Что synthesis покрывает:** Holding GmbH + Ops GmbH split, formal Beirat, full C-suite hires (CFO, COO Executor archetype, CTO, CMO, CHRO), DPO внешний при 20+ data processors.

**Critical gaps:**
- **DPO (Data Protection Officer) role-manifest.** BDSG §38 — обязателен при 20+ data processors. Synthesis Part 5.3 Phase 2/3 readiness gap #3 упоминает но не resolves. Создать `roles/l1-foundation/dpo/role.md` с Block 5 "external" mode + escalation paths to BfDI/BlnBDI. Должен существовать к Phase 2a, не Phase 2c.
- **Constellation-style Operating Group rev. структура.** Phase 2c хочет "первое поглощение" (R9 §K.6, K.11 2028). Acquired SaaS = separate P&L = separate `og/<og-name>/` или `entities/<entity-name>/` namespace в jetix monorepo. Текущая `jetix/clients/`, `jetix/alphas/clients/` — single-entity assumed. Architecture не federated.
- **Integration playbook (acquired company → Jetix monorepo).** Constellation-light integration (R9 §G.3) — где Jetix-specific? Какие репозитории merge, какие keep separate? Какие customers transfer to Jetix CRM, какие keep in acquired company's system? Master Data Management strategy unspecified.
- **Compensation matrix (formal).** При 20-50 humans: salary bands, equity bands, promotion rubrics. Synthesis R9 §K.7 даёт ranges — но в Jetix repo они не coded. Должно существовать `policy/compensation.md` + `policy/equity.md` ранее.
- **Customer Success как distinct role.** Synthesis Part 5.3 Missing Pattern #3 flagged. CS=retention, Account Mgmt=expansion. При 20+ retainer clients — separate roles mandatory.
- **Translation management.** Если первый hire в P2a — non-Russian speaker, then weekly+monthly+quarterly artifacts в Jetix language layer become English/German default. Russian → bilingual transition костлявая.

**Severity:** Critical. Без подготовки, Phase 2c = re-architecture event.

### Phase 2c → Phase 3 (team 100+, €50M+, multi-entity, 2030+)

**Что synthesis покрывает:** многоюрисдикционная структура, formal Aufsichtsrat при 500+ (DrittelbG), Operating Groups Constellation-style, divisional planning hint (R9 §K.9).

**Massive gaps:**
- **Federation model.** При 4+ entities (Jetix Holding GmbH, Jetix Operations GmbH, Jetix Alliance GmbH, Jetix ProductCo GmbH, +acquired SaaS GmbHs) — single monorepo больше не работает. Multi-repo + shared standards (Karpathy LLM Wiki в каждом, common `shared/` package). Требует **explicit federation pattern** в architecture.
- **Cross-border tax/regulatory.** Holdings BV (NL, Deelnemingsvrijstelling 100%), Operations GmbH (DE, §8b 95%), IP в IE / CH. Synthesis не покрывает data flow architecture между entities, transfer pricing documentation, treasury management, intercompany invoicing.
- **IPO readiness.** R9 K.11 2035 IPO ready. Что нужно начать готовить с Phase 2c: Audit-ready financials (PCAOB или DCGK Prüfung), public-company governance (Audit Committee, Compensation Committee, Nomination Committee), IFRS не HGB, MAR (Market Abuse Regulation) compliance preparation. Architecture должна допускать дополнительный contoll layer.
- **Aufsichtsrat при 500+.** DrittelbG = 1/3 employee representation. Required org-chart-in-git: `governance/aufsichtsrat/` намespace, election procedure, employee representative selection, board-meeting cadence formal. Synthesis Phase 3 row упоминает но не concretizes.
- **EU AI Act enforcement (Aug 2026).** High-risk AI системы — registration в EU database, conformity assessments, post-market monitoring. AI consulting может попадать в high-risk если Jetix deploys agents, принимающих employment / credit / education decisions для клиентов. Compliance calendar нужен в Phase 1, не Phase 3.

**Severity:** Critical. Phase 3 требует Phase 1-2 preparation.

---

## Part 2 — Scale-up Weaknesses by Area

### Area 1: Overall Philosophy
**At 10x:** Holds. 7-layer architecture works for 30-50 agents.
**At 100x:** Breaks. "L0 Executive Core" assumption single human strategic-management не scales beyond Phase 2c. Need Constellation OG abstraction layer between L0 and Operations. Current synthesis "L0 = Ruslan + agents + future humans" — это Phase 1-2 frame. Phase 3 = "L0 = Holdings Board + CEO + Operating Group GMs + agents + employees".

### Area 2: Folder Structure
**At 10x:** 20+ top-level folders + per-agent memory + alpha state — fine for 30 agents. Git status / fzf okay при 5K-10K файлов.
**At 100x:** Breaks. 120 agents × `agents/<id>/{system.md, strategies.md, scratchpad.md, niche/, v1/, v2/}` × multi-version = 1500+ файлов в one tree. Multi-entity не работает при monorepo. Recommendation: prepare `entities/<entity-slug>/` namespace conventions with Phase 1 single-entity stub `entities/jetix-gmbh/` (rest inherits from root). Future expansion trivial.

### Area 3: Role Manifests
**At 10x:** 8-блочный role-manifest scales хорошо. R3 + R1 ladder адекватны.
**At 100x:** Несколько issues:
- Manifest size 500-1000 строк × 100 ролей = 50-100K строк YAML+MD к ревью при annual role review. Ритуал не scales.
- "current-executor" в manifest — при 100 agents где executor сменяется per-PR, churn raises blame-noise.
- Cross-role decision-rights conflicts (когда два J3 disagree) — нужен escalation matrix beyond per-role `escalation-trigger`.
- `seniority.split_trigger` — implicit assumption Ruslan делает split decision. На 100 ролях нужен auto-detection (когда `accountabilities.length > 7` — alert).

### Area 4: Life-OS Separation
**At 10x:** Phase 2 separate-repos pattern (R7 §E) works.
**At 100x:** Holds, потому что Life-OS остаётся 1 person Ruslan'а. Concern не scale — concern Ruslan succession (если Ruslan exits, Life-OS fate?). Не critical.

### Area 5: Knowledge Architecture
**At 10x:** HippoRAG на 5000 pages — R4 §G.2 acknowledges open question. Scale concern real.
**At 100x:** HippoRAG breaks at 50K pages. GraphRAG trigger 5K pages нужен ясно (synthesis говорит "deferred"; нужна explicit trigger metric и preparation). Vector DB hybrid mandatory. Вторая критическая проблема: per-entity knowledge isolation — клиент Acme принадлежит Jetix Operations GmbH или Jetix Alliance GmbH? Knowledge access controls не есть в synthesis.

### Area 6: FPF-Lite
**At 10x:** Holds. Solo founder + 12 → 30 agents применяют FPF-Lite consistently через CLAUDE.md.
**At 100x:** Breaks subtly. "Application of FPF-Lite" requires consistency check. При 100 agents + 50 humans — кто owns FPF-Lite consistency? Meta-agent J3 имеет review burden, but не accountable for org-wide ontology drift. Phase 2c+ — нужен dedicated "FPF-Steward" sub-role или quarterly external Левенчук audit.

### Area 7: Career Levels (J0-JX)
**At 10x:** Полностью адекватен. R1 framework solid.
**At 100x:** Адекватен но needs additions:
- **Compensation matrix (€-band per level)** explicitly missing — R9 §H gives ranges, not coded.
- **Promotion review cadence** (semi-annual vs annual) for humans — not specified.
- **AI agent "promotion" formalization** — сейчас informal "extend decision_rights after 90 days <2% escalation". При 100 agents это нужно быть `governance/agent-promotions.yaml` log с metrics gate.
- **JX (C-level) executive search process** — what's required to hire CFO at €5M+ ARR? Search firm? Interview loop? Background check?

### Area 8: Operational Instructions (14-day rollout)
**At 10x:** Holds. Stack scales (Promptfoo + Langfuse + Coolify) до 30-50 agents.
**At 100x:** Breaks:
- Promptfoo CLI на 120 agents × per-PR eval = CI queue saturation.
- Langfuse self-hosted single-instance — needs HA + DB scaling at 1M+ traces/month.
- Coolify single-server — needs orchestration at 5+ services.
- SOPS+age — workable до 10-20 humans с keys; при 50+ нужен Vault.
- Hetzner Storage Box — sufficient до 10TB. Beyond — multi-region S3-compatible.

Recommendation: **scale triggers documented in synthesis** (some present, others missing) с per-tool replacement specifications.

### Area 9: Final Decision Record (RFD format)
**At 10x:** Holds. Oxide RFD scales хорошо.
**At 100x:** RFD numbering convention — nested RFDs (RFD 0001 supersedes 0042) tracking via metadata only, нет visual tree. Need `decisions/_index.md` auto-generated с supersession graph.

---

## Part 3 — Missing Scale Patterns

### 3.1 Federation / Multi-entity (Holdings + Ops)

**Current synthesis:** Single-entity monorepo. Mentions Holdings BV + Ops GmbH в Phase 3 row only.

**Missing patterns:**
- **Entity boundary in folder structure.** Recommend: top-level `entities/<entity-slug>/` namespace. Phase 1 = `entities/jetix-gmbh/` (mirror current `jetix/`); Phase 2c+ = `entities/jetix-holding-gmbh/`, `entities/jetix-ops-gmbh/`, `entities/acquired-saas-1/`. Each имеет own `clients/`, `alphas/`, `finance/`, but shares root `shared/`, `roles/` (role contracts), `wiki/`, `decisions/`.
- **Cross-entity transactions.** `entities/jetix-holding-gmbh/intercompany/` для transfer pricing документации, intercompany invoicing log.
- **Federated role-executor.** Same role (e.g., "сales-lead") can have different executors per-entity (`sales-lead-jetix-ops` vs `sales-lead-acquired-saas-1`).
- **Multi-entity decision RFD.** Decisions touching multiple entities need joint approval — RFD frontmatter `entities: [jetix-holding, jetix-ops]`.
- **Tax-residency annotations.** Each `clients/companies/<slug>.md` — `service-provider-entity: jetix-ops-gmbh` для VAT routing.

**Phase 1 preparation cost:** ~4 hours adding `entities/jetix-gmbh/` namespace stub + documenting future expansion в `decisions/0002-multi-entity-readiness.md`. **Saves Phase 2c re-architecture (~80 hours).**

### 3.2 Cross-border Operations (beyond DACH)

**Current synthesis:** DACH-locked. Mention "DACH alone feasible at €50M+?" в Open Q (Part 5.1, Conflict 7).

**Missing patterns:**
- **i18n/l10n for client communication.** Templates `templates/proposal-de.md`, `templates/proposal-en.md`, `templates/proposal-fr.md` (CH, AT, FR-DACH border).
- **Multi-currency invoicing.** EUR primary, CHF secondary (Switzerland MIT clients), USD tertiary (US Mittelstand subsidiaries). `finance/currencies.yaml`.
- **VAT/tax rules per country.** Reverse charge B2B intra-EU, VAT One Stop Shop (OSS) для B2C, Swiss VAT 7.7%, US sales tax.
- **GDPR vs adequacy decisions.** UK adequacy 2025, US-EU DPF (R9 §I.6). Data flow architecture per-jurisdiction.
- **Hiring beyond Germany.** Berlin office Phase 1-2; Vienna / Zurich / Munich satellites Phase 3. Each = own entity или cross-border employment? PEO/EOR (Deel, Remote, Multiplier) — preparation.

**Phase 1-2 preparation cost:** Low — add `policy/cross-border.md` placeholder, `templates/` multi-language stubs.

### 3.3 M&A Absorption

**Current synthesis:** R9 §G full M&A research; Phase 2c trigger upspoken. **Architecture-side:** zero. Synthesis doesn't address how acquired company's data, repo, employees, customers integrate.

**Missing patterns:**
- **Acquisition integration playbook.** `playbooks/acquisition/` with: `due-diligence-checklist.md` (R9 §G.2 codified), `integration-week-1.md`, `integration-month-1.md`, `integration-month-12.md`, `cultural-onboarding.md`.
- **Repo absorption strategy.** Three options:
  - (A) **Full merge** — `git filter-repo` acquired SaaS history into `entities/acquired-saas-1/` (preserves history but binds futures).
  - (B) **Reference link** — keep acquired SaaS repo separate, link via `entities/<entity>/manifest.yaml` (preserves autonomy but data silo).
  - (C) **Selective import** — copy roles + alphas + key wiki pages, archive old repo (clean slate but history loss).
  Document choice template `decisions/<RFD-N>-acquisition-<acquired-name>.md`.
- **Employee migration to Jetix structure.** Acquired company's roles → Jetix role-manifests (mapping table). Career-level translation (their "Senior" → J? Jetix). Compensation harmonization plan.
- **Customer migration.** Their CRM → `clients/` Jetix. GDPR re-consent if data subject categories change.
- **Brand vs sub-brand decision.** Constellation-light keeps brand. Decision tree.

**Phase 1-2 preparation cost:** Medium — `playbooks/acquisition/template.md` (~3 hours stub). Detailed playbook closer to Phase 2c.

### 3.4 Crisis Playbook (bus factor, outage, legal)

**Current synthesis:** R9 §F full crisis research; §K.8 protocols. **Architecture-side:** zero artifacts.

**Missing artifacts (создать сейчас в Phase 1):**
- `ops/incident-playbook.md` — generic incident response.
- `ops/incidents/<YYYY-MM-DD-slug>.md` — per-incident folder (severity, timeline, root cause, action items).
- `ops/business-continuity.md` — Ruslan incapacitated 1 week / 1 month / permanent.
- `ops/hit-by-bus.md` — passwords (1Password vault location), key contacts (Steuerberater, Notar, lawyer, Anthropic acct mgr, Hetzner support, banking), open commitments, current decisions in flight, how to shut down gracefully if needed.
- `ops/regulatory-incidents/`:
  - `gdpr-art-33-playbook.md` — 72h notification process, BlnBDI contact, template Meldung des Datenschutzvorfalls.
  - `eu-ai-act-incident.md`.
  - `tax-audit.md`.
- `ops/disaster-recovery.md` — backup restore drill quarterly.

**Phase 1 cost:** ~6 hours для все templates filled с current Jetix specifics. **Risk-mitigation очень высокая.**

### 3.5 Governance Evolution (advisory → Beirat → Aufsichtsrat)

**Current synthesis:** Phase evolution table mentions "Board" column. R9 §D + §K.5 detailed framework. **Architecture-side:** stub.

**Missing patterns:**
- **`governance/` top-level namespace.** Currently merged under `policy/`. Recommend separate:
  - `governance/advisory-board/` — Phase 1-2a informal (Anton, Vladislav, Rodion + advisors).
  - `governance/beirat/` — Phase 2c formal Beirat.
  - `governance/aufsichtsrat/` — Phase 3b при 500+ DrittelbG / 2000+ MitbestG.
  - Each: `members.yaml`, `meetings/`, `pre-reads/`, `decisions/`, `compensation.md`.
- **Board meeting cadence in `weekly/`-style.** `governance/<board-type>/meetings/<YYYY-MM-DD>.md` with 72-hour pre-read rule.
- **Director independence tracking.** При Phase 3 board — independence criteria, conflict-of-interest declarations.
- **Committee structure.** Phase 3b: Audit / Compensation / Nomination committees per DCGK.
- **Employee representation election.** Phase 3b DrittelbG — election procedure, representative tracking.

**Phase 1 cost:** ~2 hours — `governance/` namespace stub, `governance/advisory-board/members.yaml` (Anton, Vladislav, Rodion).

### 3.6 IPO Readiness

**Current synthesis:** "IPO ready" 2035 row R9 §K.11. **Architecture-side:** zero.

**Critical preparations с Phase 2c (3-5 years before IPO):**
- **IFRS не HGB.** GAAP → IFRS conversion at €15M+ revenue / Phase 2c. Hire IFRS-experienced controller. Architecture: `finance/ifrs/` parallel to `finance/hgb/`.
- **Audit-ready financials.** Big4 (PwC / KPMG) audit cycle. `finance/audit/<YYYY>/`.
- **MAR compliance preparation.** Insider trading list, deal-room procedures, financial calendar.
- **Public-company governance.** Audit Committee charter, Compensation Committee charter, Nomination Committee charter, Code of Ethics, Whistleblower hotline.
- **CEO succession planning формальное.** Internal candidate identification 3-5 years before transition. Successor-pipeline в `governance/succession/`.
- **Equity story documentation.** Investor deck templates, financial model, market sizing, competitive positioning — все в git.
- **Public reporting cadence.** Quarterly earnings, annual report, capital markets day infrastructure.

**Phase 1 cost:** Низкая — `decisions/0003-ipo-readiness-roadmap.md` (3-5 page placeholder с timeline). Real work Phase 2c+.

---

## Part 4 — Architecture Debt Risks

| Phase 1 Decision | Debt Accrued at 10x | Debt Accrued at 100x | Mitigation Now (Phase 1-2a) |
|---|---|---|---|
| Single-entity monorepo | Acquisitions awkward, single `clients/` namespace | Federation impossible without re-architecture | Add `entities/jetix-gmbh/` namespace stub now |
| Russian-primary docs | First non-Russian hire requires translation push | Multi-country team blocked | Establish English+Russian frontmatter convention now; English mandatory in `policy/`, `decisions/`, `roles/` |
| Centralized escalation to Ruslan | Bottleneck при 5 humans | Founder Mode → Megalomania | Explicit decentralization triggers in role-manifest `escalation-trigger`; Chief of Staff role-manifest reserved Phase 1 |
| 12 agents enumerated as roster | Still works at 30 | Org-chart visualization broken | Auto-generated `org-index.yaml` from role-manifests; SVG generation pipeline |
| Hourly-billing forbidden absolute | Some Mittelstand small advisory deals lost | Architecture rigid | Allow "consultancy retainer minutes" as exception SKU; documented escape hatch |
| HippoRAG retrieval | Latency at 5K pages | Breaks at 50K pages | Document GraphRAG trigger metric (retrieval latency >3s p95); preparation script |
| SOPS+age secrets | Workable at 10 humans | Key management chaos at 50+ | Document Vault/Bitwarden/1Password Teams trigger (10 humans) |
| No DPO role-manifest | Just-in-time scrambling at 20 data processors | Compliance gap | Create `roles/l1-foundation/dpo/role.md` external-mode now |
| No incident playbook | Improvise at first incident | Reputation damage at scale | `ops/incident-playbook.md` Phase 1 |
| No Customer Success role | Retention drift at 10+ retainers | Churn epidemic at 50+ | CS as J2 role-manifest stub Phase 2a |
| No translation infrastructure | Each new language hire = manual | Multi-country impossible | Bilingual frontmatter convention now |
| Single Hetzner CPX32 | Capacity constrained at 30 agents | Multi-region required | Document scale triggers; Terraform multi-region readiness |
| FPF-Lite single-author Ruslan | Drift at 30 agents | Ontology fragmentation | FPF-Steward sub-role (могут быть meta-agent extension) |
| `current-executor` in role-manifest | High churn at 100 agents | Manifest churn noise | Move executor binding to separate `executors/<role>/current.yaml` (separation of contract from binding) |

---

## Part 5 — Proposed Changes для v2 (15 scale-improvements)

**P1 = блокер для Phase 2; P2 = should-do для Phase 1; P3 = nice-to-have.**

1. **[P1] Add `entities/jetix-gmbh/` namespace stub now.** Mirror current jetix/ structure under entities/. Document multi-entity expansion rationale в `decisions/<N>-multi-entity-readiness.md`. Cost: 4h. Saves: 80h Phase 2c.

2. **[P1] Create `roles/l1-foundation/dpo/role.md` external-executor mode.** BDSG §38 trigger 20+ data processors можеt come early при first DPA enterprise client. Cost: 2h.

3. **[P1] Create `governance/` top-level namespace with advisory-board sub-folder.** `governance/advisory-board/members.yaml` (Anton, Vladislav, Rodion); placeholder `governance/beirat/`, `governance/aufsichtsrat/`. Cost: 2h.

4. **[P1] Create `ops/` operations namespace with crisis playbooks.** `ops/incident-playbook.md`, `ops/business-continuity.md`, `ops/hit-by-bus.md`, `ops/disaster-recovery.md`, `ops/regulatory-incidents/gdpr-art-33-playbook.md`. Cost: 6h. Risk-mitigation очень высокая.

5. **[P1] Bilingual frontmatter convention для `policy/`, `decisions/`, `roles/`.** YAML `lang: [ru, en]` + minimum English summary required. Establishes path к multi-country team without retroactive translation. Cost: 2h convention + ongoing discipline.

6. **[P2] Decompose strategic-management role into 5 sub-roles upfront.** R3 §A.1 multi-roled-founder critique. Open Q3 в synthesis. Recommendation: monolithic Ruslan-as-role + 4-5 explicit sub-role manifests with `executor: ruslan` initially, marked as "delegation candidates". Each gets explicit "delegation trigger" в Block 5. Saves Phase 2a confusion. Cost: 4h.

7. **[P2] Customer Success J2 role-manifest stub.** Distinct from Account Management. Owns retention metrics, NPS, expansion. Activated при 10+ retainer clients (Phase 2a-2b). Cost: 2h.

8. **[P2] Compensation matrix coded в `policy/compensation.md`.** Salary bands per J-level (R9 §H benchmarks); equity bands per hire seq#. VSOP template, §19a path documented. Cost: 4h.

9. **[P2] Org-chart visualization pipeline.** `scripts/org-chart.py` reads `roles/` + `executors/` + emits SVG. Updated в pre-commit hook. Cost: 3h.

10. **[P2] Auto-generated `org-index.yaml`** with role count, executor count, span-of-control checks (R8 Rule 7), alpha coverage (R8 Rule 10). Lint failure if violated. Cost: 3h.

11. **[P2] EU AI Act compliance calendar в `policy/eu-ai-act.md`.** 2025/2026/2027 milestones. Quarterly check trigger. Cost: 2h.

12. **[P2] Acquisition playbook stub `playbooks/acquisition/template.md`.** Three-strategy decision tree (full merge / reference / selective import). Cost: 3h.

13. **[P3] FPF-Steward sub-role внутри meta-agent.** Quarterly ontology consistency check; flag drift; suggest consolidation. Cost: 2h.

14. **[P3] IPO readiness placeholder `decisions/<N>-ipo-readiness-roadmap.md`.** 3-5 page timeline + "what to start preparing when". Cost: 2h.

15. **[P3] Multi-currency / multi-VAT scaffolding в `finance/`.** EUR primary, CHF/USD secondary. `finance/currencies.yaml`. Cost: 1h.

**Total Phase 1-2 preparation cost: ~42 hours.** This is "scale-up scaffolding tax" — 4-5 days of focused work that prevents 200+ hours of re-architecture при Phase 2-3 transitions.

---

## Part 6 — Phase 2 Preparation Checklist

Что должно быть готово **до** первого human hire (трigger Phase 2a):

### Legal/HR
- [ ] UG → GmbH conversion completed (or direct GmbH formation).
- [ ] Geschäftsführer-Anstellungsvertrag для Ruslan (formal employment contract distinct from Gesellschafter rights).
- [ ] D&O insurance contracted (€1-3K/year).
- [ ] Berufshaftpflicht-Versicherung для consulting (€1-3K/year).
- [ ] VSOP plan template + §19a EStG eligibility check (если qualified).
- [ ] Employment contract template (Arbeitsvertrag) lawyer-approved.
- [ ] PTO/sick leave policy в `policy/employment.md`.
- [ ] DPO designated (внутренний at first; external when 20+ processors).
- [ ] BfDI/BlnBDI contact на file в `ops/regulatory-incidents/`.

### Architecture
- [ ] `entities/jetix-gmbh/` namespace stub created.
- [ ] `governance/advisory-board/` formalized (members, cadence).
- [ ] `ops/` crisis playbooks written.
- [ ] Sales Lead role-manifest (Block 7 implementation_human filled fully).
- [ ] Onboarding content `docs/onboarding/sales-lead/week-1.md`, `week-2.md`, `week-3.md`, `week-4.md`.
- [ ] Bilingual frontmatter convention in place; first English-summary added к key documents.
- [ ] Customer Success role-manifest stub.
- [ ] Org-chart auto-generation pipeline.
- [ ] Strategic-management decomposed into sub-roles (or explicit decision to keep monolithic).

### Infrastructure
- [ ] Toggl team workspace setup with billing.
- [ ] Geschäftskonto opened (Commerzbank / Penta / Qonto).
- [ ] Slack/messaging channel decided (or async-only commitment documented).
- [ ] Performance review cadence defined в `policy/performance-reviews.md`.
- [ ] Bad Leaver / Good Leaver clauses in employment template.
- [ ] Backup restore drill performed and documented.
- [ ] Multi-provider AI fallback (Claude primary, GPT-4o secondary) tested.
- [ ] `ops/hit-by-bus.md` written and shared с Anton (or designated trustee).

### Operations
- [ ] First Beirat meeting with informal advisors (Anton, Vladislav, Rodion).
- [ ] First quarterly OKR cycle started (Q3 2026).
- [ ] First quarterly letter draft (Berkshire-style) — public-facing intent.
- [ ] First postmortem template applied to a real incident (even minor).
- [ ] FPF-Lite frozen v1.0.0 (changes after Phase 2a require RFD).

**If 80%+ of this list — Phase 2a ready.** Below 60% — high re-architecture risk Phase 2.

---

## Part 7 — Questions для Final Synthesizer

1. **Multi-entity readiness — Phase 1 scaffolding or Phase 2c emergence?** Cost is 4 hours now vs ~80 hours later. Is this tradeoff обвaltываемый — "scaffolding now, occupy later" — или нарушает "minimum viable" принцип?

2. **Strategic-management decomposition — monolithic Ruslan or 5 sub-roles?** R3 §A.1 multi-roled founder критика vs operational clarity. Recommendation: explicit 4-5 sub-roles with single executor `ruslan` initially + delegation triggers per sub-role. But this предположение значительной upfront ontology work — нужен Ruslan judgment.

3. **Bilingual frontmatter starting now — or Russian-only до first non-Russian hire?** Russian-only простe; bilingual front-load translation effort. But first hire может быть Mittelstand-DACH speaker (German/English), не Russian. Decision affects all docs from Day 1.

4. **DPO role-manifest creation timing.** BDSG §38 triggers at 20+ data processors. AI agents = data processors? Anthropic processes data на behalf клиентов = controller-processor relationship. Conservative interpretation: 20+ Claude agents already triggers DPO. Aggressive interpretation: only when Jetix has 20+ data subjects under contract. Reading?

5. **Federation pattern — `entities/` namespace или multi-repo с Phase 2c?** `entities/<slug>/` keeps everything in monorepo (simpler, slower при scale). Multi-repo (one per entity) keeps things separate (cleaner, harder cross-entity ops). Constellation pattern is multi-repo de facto. Decision needed before first acquisition.

6. **Crisis playbook authorship — Ruslan or shared?** `ops/hit-by-bus.md` requires designated trustee (Anton?) с access к 1Password vault, contacts. Trust hierarchy decision имеет implications далеко за architecture.

7. **Multi-country expansion explicit decision.** "DACH-locked" в synthesis vs "DACH first then DACH-adjacent" vs "DACH primary с opportunistic global". Each implies different architectural preparations. Soft vote recommendation — but this is JX-level decision.

---

## Part 8 — Verdict

**Q: "Synthesis scale-up-ready до €10M ARR без rebuild?"**
**A: NO — only YES with the 15 proposed changes (or equivalent).**

Rationale: synthesis is **strong для €0-2M ARR / team 0-5**. Beyond that, three categories of Phase 2-3 preparations are **missing in architecture artifacts** (even though research R9 acknowledges them):

1. Federation/multi-entity скаффолдинг.
2. Crisis playbook + bus factor artifacts.
3. Cross-functional / operational роли (DPO, CS, FPF-Steward, Compliance).

Without these, transitions Phase 2a → 2b → 2c require re-architecture each step. With these (≤42 hours Phase 1-2 work), synthesis scales clean to €10M ARR / team 20-50.

**Q: "Synthesis scale-up-ready до €50M ARR / multi-entity без rebuild?"**
**A: NO — even with 15 changes, Phase 3 needs additional preparations.**

Rationale: Phase 3 (multi-entity, 100+ team, IPO-readiness) requires:
- Federation pattern committed (multi-repo or `entities/` namespace at scale).
- IFRS conversion process.
- Aufsichtsrat formal infrastructure (DrittelbG election procedures, board committees).
- IPO-readiness preparations (audit-ready financials, succession planning, public-company governance, MAR compliance).
- Cross-border tax/regulatory architecture.

These are **legitimately Phase 2c-3 work** (cannot reasonably build now). Synthesis должен **explicitly acknowledge Phase 3 will require additional architectural work** — это not a violation of "scale-up-first design" если acknowledged как conscious trade-off.

**Recommendation для v2:** Add Part 7 "Phase 3 Architecture Roadmap" с explicit "what we know we'll need to add later" list. Honesty about Phase 3 future-work беспокоит less чем pretending current synthesis covers it.

**Missing preparations summary (priority order):**

1. (P1, 4h) Multi-entity namespace stub (`entities/jetix-gmbh/`).
2. (P1, 6h) Crisis/incident playbooks (`ops/`).
3. (P1, 2h) DPO role-manifest external-executor mode.
4. (P1, 2h) Governance namespace with advisory board formalized.
5. (P1, 2h) Bilingual frontmatter convention.
6. (P2, 4h) Strategic-management decomposition decision + sub-role manifests if chosen.
7. (P2, 4h) Compensation matrix in `policy/`.
8. (P2, 3h) Org-chart auto-generation pipeline.
9. (P2, 2h) EU AI Act compliance calendar.
10. (P2, 2h) Customer Success role-manifest stub.
11. (P2, 3h) Acquisition playbook template.
12. (P3, 2h) FPF-Steward sub-role.
13. (P3, 2h) IPO readiness roadmap placeholder.
14. (P3, 1h) Multi-currency scaffolding.
15. (P2, 3h) Onboarding content (week-by-week) для first hire.

**Total: ~42 hours scale-up scaffolding.** Phase 1 ROI overwhelmingly positive — these are not Phase 3 systems demanded prematurely; they are Phase 1-appropriate stubs and conventions that prevent costly re-architecture at later phases.

---

**END OF MEGA-CORP VISIONARY REVIEW** — Stage 2, role: scale-up.
