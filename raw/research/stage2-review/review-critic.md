---
type: stage2-review
role: critic
reviewer: claude-opus-4-7-subagent
input: raw/research/architecture-implementation-synthesis-2026-04-19.md
created: 2026-04-19
length: 5400 слов
---

# Critic Review — Jetix Architecture Synthesis v1

> Honest, attacking review. Я не ищу "что хорошо" — я ищу где модель ломается.

## Executive Critique (≈500 слов)

**Concern #1 — Synthesis систематически путает "architectural readiness" с "operational utility" и не имеет ни одного механизма который бы заставил это распутать.** Документ заявляет "scale-up-first design" 47+ раз и оправдывает каждое решение через "Phase 2/3 readiness" (Part 1 §1.4 принцип 1, Part 2 §Area 1 Rationale, Conflict 7). При этом sole revenue-bearing layer — L4 Delivery — занимает в synthesis ~2% объёма (одна таблица в Part 1.3 + 6 строк в Area 1). 98% документа — про слои которые НЕ принесут €50K в Q2 2026. Это не "balanced architecture"; это "premature scaffolding с retrofit оправданием через mega-corp narrative". Синтез нигде не задаёт вопрос: "если первый клиент не закрылся к Q3 2026, какие из этих 7 слоёв нам помогли его закрыть?". Ответ: ни один. L1 Foundation (Promptfoo+Langfuse+SOPS+Coolify+Uptime Kuma+Healthchecks+Sentry+Netdata = 8 tools на solo founder) — не sales infrastructure. L2 FPF-Lite — не proposal generator. L7 Portfolio — для €0 capital pure ceremony. И при этом 14-day rollout (Area 8) тратит ВСЕ 14 дней на L1, а не на L4. Это инверсия приоритетов maskированная под "foundation-first wisdom".

**Concern #2 — Modular swap-out claim ("role ≠ executor, Claude 4.7 → Claude 5 = меняется executor, не роль") не подтверждён ни одним эмпирическим тестом.** Synthesis утверждает в Part 1 §1.4 принцип 2 и в Area 3 что 8-блочный role-manifest даёт "stable contract" между ролью и executor. Это hand-waved. Реальность LLM-эпохи: каждый major model upgrade меняет prompt sensitivity, tool-call behavior, context-window economy, hallucination patterns. Anthropic уже публично deprecated Claude 2.x → 3.x → 4.x с поломкой prompt techniques (XML tag conventions, system prompt budget, tool-use schema). `prompt-file: agents/sales-lead/v1/system.md` + `eval-passing-threshold: 0.85` (Area 3 Block 6) НЕ является "portable contract" — это hardcoded coupling к Claude API quirks. При смене Claude 4.7 → 5 нужно: пересмотреть golden datasets, перерайтить system prompts, перенастроить context budgets (50K из Area 5 — функция Claude Opus 4.7 экономики), перетестировать tool-call patterns. Synthesis это знает (Trade-off в Area 1: "Зависимость от Claude Code infrastructure mitigated: role-manifests portable") но НЕ показывает доказательство portability. Это претензия, а не свойство.

**Concern #3 — Bus factor = 1 упомянут в Hidden Risks (5.1 #5) но не имеет ни одного architectural mitigation в самом synthesis.** Это не deferred technical risk — это existential risk для всего проекта. Если Ruslan на 4 недели вышел из строя (грипп, авария, family emergency, mental health), ВСЕ слои стоят: L0 strategic decisions, L4 client commitments, L5 community presence, L7 portfolio rebalance. AI-агенты не могут autonomy на client commitments (L4 in Area 7: "Точно human: первые встречи Mittelstand GF, контракты sign, увольнения"). Mittelstand клиент с подписанным retainer ожидает ответ в 24-48 часов. Synthesis не имеет: (а) succession protocol, (б) "warm standby human" pattern, (в) client-facing automated incident response, (г) explicit Service Continuity playbook в L1. Это особенно cruel потому что вся Phase 1 архитектура спроектирована **усилить** dependency на Ruslan: он единственный J5+JX, единственный с decision rights на discounts >20%, contracts, hiring, strategic-management. Architecture не reduces single point of failure — она его institutionalizes.

---

## Part 1 — Critical Findings by Architecture Area

### Area 1: Overall Philosophy

- **Weakness 1 (Part 2 Area 1 §Unified Recommendation):** Заявление "AI-native mega-corporation в форме software artefact" — это positioning, а не architectural decision. Документ нигде не показывает _что конкретно_ "mega-corporation" property означает в архитектуре vs "well-organized solo consultant с git". Вся 7-слойная структура работала бы для "solo consultant who likes folders". Mega-corp claim не falsifiable.
- **Weakness 2 (Trade-offs в §Area 1):** "Высокая когнитивная нагрузка mitigated: meta-agent = immune system; weekly consolidation". Это circular — meta-agent сам требует cognitive load (его prompts, его evals, его escalations). Если Ruslan не успевает справиться с 7 слоями, добавление 13-го агента которому надо проверять консистенцию НЕ снимает нагрузку, а перекладывает её на другую кост-структуру (input tokens, time-to-validate meta-agent's output).
- **Weakness 3 (Rationale §1):** "Compressed C-suite через AI permits founder mode дольше" — predicated на claim что AI agents могут replace VP-level decision-making. Это empirical question с ZERO evidence в synthesis. Paul Graham's "Founder Mode" essay (cited) — про human founders делающих detail work, не про AI заменяющих executives.
- **Weakness 4 (Rationale §2 "underserved premium market"):** 215K Mittelstand Nachfolge до 2025 (KfW) — but цифра не означает "underserved AI consulting market". Большинство этих компаний даже не имеют CTO; они нанимают Steuerberater и IT-Dienstleister, не AI-консультантов. Synthesis confuses TAM с addressable demand.

### Area 2: Folder Structure

- **Weakness 1 (Part 2 Area 2):** Дерево содержит 24+ top-level folders в `jetix/` (CONSTITUTION, CLAUDE, README, roles, executors, agents, alphas, alpha-log, clients, wiki, decisions, postmortems, strategizing, weekly, letters, okrs, policy, processes, evals, docs, templates, products, comms, state, sales, finance, secrets). Synthesis Trade-off honest: "20+ top-level folders требуют README.md в каждом, но это норма для mega-corp". Это не норма — это **симптом не-MECE декомпозиции**. Например: `decisions/`, `postmortems/`, `strategizing/`, `policy/` — все четыре содержат "long-form decision artifacts". Зачем 4 папки?
- **Weakness 2 (Conflict 1 resolution):** Triple-representation (`alphas/clients/<id>/state.yaml` + `clients/companies/<slug>.md` + `wiki/entities/clients/<slug>.md`) — это **deliberate three-fold redundancy** который synthesis сам признаёт ("Three places referencing same client. Mitigated: alpha-ref edges + pre-commit hook + agent reads via single lookup через index"). Это не mitigation, это перенос burden на (а) hook который надо написать, (б) index который надо поддерживать, (в) discipline которая ломается под deadline pressure. Стоимость поддержки три-fold consistency для solo founder в Phase 1 — high; benefit — нулевой пока нет 5+ humans.
- **Weakness 3 (Open Q1 §Area 2):** "life-os/wiki/ + jetix/wiki/ отдельны или shared". Это unresolved вопрос про cross-cutting concern в Phase 1. Откладывается до Q&A Ruslan'а. Я бы spec'аnул — split с Day 1, иначе при Phase 2 extraction `git filter-repo` встретит cross-references.
- **Weakness 4 (отсутствует):** Нет explicit `inbox/` или `triage/` папки несмотря на наличие `inbox-processor` агента в L0 (Career table Area 7). Где живут voice-notes, raw transcripts, ingest queue? `tools/transcribe.py + extract.py + filter.py` упомянуты в CLAUDE.md, но output-папка в дереве отсутствует.

### Area 3: Role Manifests

- **Weakness 1 (Block 5 `seniority.split_trigger`):** Условия "active-deals > 30, 2+ FTE needed concurrently" для split sales-lead роли — magical numbers. Откуда 30? В Phase 1 (€50K Q2 2026) у sales-lead будет ~3-10 active deals max. Trigger срабатывает в Phase 2b/2c — то есть 2-3 года с сейчас. Spec на `split_trigger` — это **planning fiction**, не actionable rule.
- **Weakness 2 (Block 6 `tools-allowed`/`forbidden-tools`):** `forbidden-tools: [email-send, git-push]` — но Claude Code MCP architecture не имеет gracefully-enforced tool prohibition. Что произойдёт когда Claude **попытается** git-push потому что user попросил? Tool fails silently? Returns error agent ignores? Synthesis не описывает enforcement mechanism — это policy aspiration без implementation hook.
- **Weakness 3 (Block 7 `implementation_human` в каждом role-manifest):** Все 14 manifests должны иметь filled implementation_human даже когда `hired-person: null`. Это значит Ruslan пишет onboarding-path для гипотетического sales-lead human за 2-3 года до hire. К моменту hire DACH рынок talent изменится, AI tooling изменится, role будет outdated. Это **exemplar premature spec**.
- **Weakness 4 (Block 5 `decision-rights`):** "veto: Commit to delivery timeline без согласования с delivery". Это написано как bullet point в YAML. Real-world deal flow: prospect на Zoom-call просит timeline. Sales-lead AI должен (а) знать что нельзя commit, (б) знать кого спросить, (в) иметь sub-second latency response. YAML-defined veto не decompiles в actionable inhibition при live conversation. Mechanism missing.

### Area 4: Life-OS Separation

- **Weakness 1 (Phase 1 description):** "SOPS+age с двумя ключами в одном `.sops.yaml`". При компрометации single laptop или single GitHub account атакующий получает оба ключа — separation на logical level, не на trust level. Если threat model — "при найме первый human не должен видеть life-os" — то shared physical key store violates это с Day 1.
- **Weakness 2 (Phase 2 trigger ambiguity):** "First human hire OR GDPR DPA enterprise client". OR-logic создаёт race condition — один из двух может triggered earlier чем другой. Migration-day-of stress: "Wait, у нас уже 3 client'а с DPA, а филь-репо ещё не делали потому что hire отложился". Synthesis не quantifies leading indicators (kakие сигналы в pipeline trigger preemptive migration).
- **Weakness 3 (Asymmetric reference rule pre-commit hook):** "Jetix → Life-OS запрещено" enforced pre-commit. Что если Ruslan локально ссылается с Jetix на life-os/health/... (понятно почему — energy-level влияет на client work) и hook блочит commit на дедлайн? Hook становится adversary а не helper.
- **Weakness 4 (отсутствует):** Synthesis говорит про file-level separation но игнорирует Claude Code MCP scope. Claude session открытая в `~/jetix-os/` имеет filesystem access ко всему дереву. Per-agent isolation требует MCP-level scoping (`tools-allowed.scope: clients/, templates/`) — но это не enforced separation, а cooperative agreement. Real GDPR DPA enterprise клиент будет требовать **proof** что AI не имеет access к other client's data. Current architecture не предоставляет.

### Area 5: Knowledge Architecture

- **Weakness 1 (Layer 1 wiki/ scaling):** "557 current pages → 5000+ projected" — projection не grounded. На каком rate? CLAUDE.md упоминает "50-100/month current" — это 5 лет до 5000. Тогда GraphRAG trigger (Open Q2) — после 2030. Зачем design-decision сейчас?
- **Weakness 2 (Layer 2 alphas/ Hybrid C):** Per-alpha `state.yaml + context.md + history.jsonl` × 6 alpha types × N entities. Для 50 active clients это 150 файлов в `alphas/clients/`. Каждый требует maintenance. Stale `state.yaml` из 2026-Q2 — больший risk чем "missing source of truth" — это **deceptive source of truth**. Synthesis не описывает stale-detection или TTL.
- **Weakness 3 (Layer 3 50K context budget):** Budget breakdown (Area 5) выделяет 5K на "Task + alpha state". Real client context (Mittelstand company с 5-летней истории отношений + 20 emails + 5 contracts + ZUGFeRD invoices + 3 SOWs) far exceeds 5K. При load шквала clients context budget насмарку — agent либо truncates (потеряет detail), либо expands (нарушит 50K) → cost spike + latency.
- **Weakness 4 (Conflict 3 dual-write):** Per-alpha + monthly aggregate с "automated projection script". Open Question §C3 explicitly: "что если projection script breaks". Synthesis не отвечает. GoBD audit trail compliance означает ZERO data loss tolerance — projection script breakage = compliance violation.
- **Weakness 5 (Sequential Rechnungsnummer pre-commit monotonicity check):** В git world это race condition. Two branches local with R-2026-0042 and R-2026-0043 — merge conflict тривиальный, но at solo dev это fine; при первом найме (Phase 2) — mid-month merge может dispense duplicate Rechnungsnummer → § 14 UStG violation. Synthesis не описывает atomic counter mechanism.

### Area 6: FPF-Lite

- **Weakness 1 (3-5 страниц = ~3000-5000 tokens, item §5.1.5 pre-flagged):** Critic chat starting point flag: "FPF-Lite alone fills system prompt budget". Synthesis отвечает: "Open Question". Это not Open — это known constraint которое invalidates current design. Если FPF-Lite full text prepended в каждый agent system prompt, то 12+ agents × 3-5K tokens = ongoing token tax. Если FPF-Lite только в meta-agent + reference в других, то agents не имеют ontological frame — defeats the purpose.
- **Weakness 2 (Section 5 Internal Principles "Artifacts over conversations"):** В FPF-Lite это principle, но реальность Claude Code = conversational. Каждая session — диалог Ruslan ↔ agent. Principle violates own implementation.
- **Weakness 3 (Section 6 "Critical Alphas (10) — с states"):** FPF-Lite определяет 10 alphas + states. Это implementation detail, не fundamental ontology. При первом alpha-revision (а они будут — synthesis admits в Conflict 9 Open Question "consent-updated event"), весь FPF-Lite требует pdate. FPF-Lite as living document = constant churn.
- **Weakness 4 (отсутствует):** Левенчук's "стратегирование" — human-only (R3 §A.4 noted in 5.4 Левенчук-chat). FPF-Lite Section 7 ritual cadence привязывает стратегирование к "monthly trigger check". Какой trigger? Synthesis не определяет — это hidden manual ritual masquerading as scheduled cadence.

### Area 7: Career Levels + Scale-up

- **Weakness 1 (J0-JX для AI agents, item 5.1.3 pre-flagged):** AI agent "promotion" = expanding `decision_rights` после 90-day track record + <2% escalation + zero false-positive critical decisions. **Кто измеряет** zero false-positive? Critical-decision detector сам — AI. Self-rating loop. Если detector mis-classifies (say, миссировал false-positive), agent promoted с broken trust. Synthesis не имеет independent audit mechanism.
- **Weakness 2 (Phase 0 trigger "Ruslan >30% time на J2 tasks"):** Time tracking presupposes Toggl discipline + accurate task-J-level mapping. Solo founder не делает этого honestly. Trigger не measurable in practice.
- **Weakness 3 (Phase 2a "Head of Finance FTE €80-120K"):** Это €80-120K/year salary при €1-5M ARR. Mittelstand DACH market reality: Head of Finance с German GAAP + ZUGFeRD + Steuerrecht expertise costs €100-140K + 25-30% Lohnnebenkosten. Synthesis under-quotes by ~30% — fragility в Phase 2 financial planning.
- **Weakness 4 (C-suite timing "CFO fractional на €1M ARR, FTE на $10M+"):** Неконсистентность валюты (€ vs $). При DACH context это должно быть всегда €. Symptomatic of cargo-culting US startup advice.
- **Weakness 5 (Human-AI boundary "delivery: human reviews for strategic clients"):** "Strategic" не определено. Ruslan становится bottleneck определения strategic-ности каждого клиента — что является именно тем что architecture якобы устраняет (через explicit decision-rights в role-manifest).

### Area 8: Operational Instructions (14-day rollout)

- **Weakness 1 (Day 4 "12 agents с new frontmatter"):** Migration of existing 12 agents в new structure. Что происходит с running production state в `comms/mailboxes/<agent>.jsonl` при schema change? Frontmatter migration without state migration = breaks recall memory.
- **Weakness 2 (Day 8 Promptfoo CI на eval-on-push):** Eval requires golden dataset (Day 7 = 10 cases for 1 role). Day 8 CI deployed но 11 других agents без datasets — CI runs but tests one role. False sense of coverage.
- **Weakness 3 (Day 9 Langfuse self-host):** Self-host на Hetzner с Docker + ongoing maintenance. For solo founder в Phase 1 это additional ops burden. Synthesis Open Q2 признаёт: "Langfuse self-host vs cloud (free tier)". Cloud free tier для Phase 1 — обоснованнее.
- **Weakness 4 (Day 14 Monitoring stack: Uptime Kuma + Healthchecks.io + Sentry + Netdata):** 4 monitoring tools для Phase 1 single Hetzner CPX32. Это **больше тулзов чем сервисов которые мониторят**. Symptom of "company-as-code aspirational shopping list".
- **Weakness 5 (отсутствует):** Нет Day для **первый paying client outreach setup**. Все 14 дней — internal infra. Если Q2 2026 €50K target real — first sales activity должна fit в эти же 14 дней или предшествовать им. Architecture inverts priorities.

### Area 9: Final Decision Record

- **Weakness 1:** RFD 0001 "state: committed" с tag `architecture-v1-final`. "Final" в Software v1 — это либо overconfidence, либо misuse Oxide RFD pattern (Oxide RFDs revised continuously — `committed` ≠ frozen). Naming convention misleading.

---

## Part 2 — Challenged Assumptions

**Assumption A1 (Part 1 §1.4 принцип 1):** "10x рост капитала/часов/людей/проектов/ролей → система справляется без rebuild."
- **Why risky:** Rebuild-avoidance — это desire, не свойство архитектуры. Каждая software architecture в истории (LAMP, microservices, event-driven, K8s) обещала 10x scaling без rebuild и каждая в реальности требовала rewrite на specific 10x point.
- **Evidence:** Conflict 1 итог уже создаёт triple-representation который не scales линейно. Conflict 3 dual-write pattern — projection script becomes critical path.
- **What if false:** Phase 2b (€2-10M, 5-20 humans) встретит rewrite. Architecture-v2 в 2028 потребует Q1 2028 dedicated migration sprint. Synthesis должен PRE-allocate Q1 2028 для rebuild, not deny возможность.

**Assumption A2 (Area 3 Block 6 portability claim):** Role-manifest portable между LLM providers / model versions.
- **Why risky:** Already discussed in Concern #2. Empirical fact: prompt-engineering — model-specific.
- **Evidence:** Block 6 hardcodes `agent_type: claude-code`, `current-executor: claude-opus-4-7`, `context-window-budget: 180000`. Это Claude-Opus-specific. "Portable" requires abstraction layer не присутствующий в spec.
- **What if false:** Claude → ChatGPT/Gemini migration в случае Anthropic outage / pricing change / DACH regulator ruling требует full re-implementation, не просто "swap executor".

**Assumption A3 (Area 1 §Rationale §2):** DACH Mittelstand "underserved" premium market.
- **Why risky:** Underservedness — функция (а) demand (есть ли сами клиенты), (б) reachability (есть ли channel), (в) willingness-to-pay. Synthesis cites только (а) и тangentially (б). (в) — ZERO data.
- **Evidence:** R5 deep research упоминает IHK/VDMA networks но не цены. Mittelstand notoriously frugal — €50K за AI Audit это серьёзная категория budget approval (Aufsichtsrat sometimes required). Synthesis не provides comparable transactions.
- **What if false:** Q2 2026 €50K target missed. Phase 0 → Phase 1 trigger never fires. Architecture invalidated by market.

**Assumption A4 (Area 5 Layer 1):** HippoRAG PPR sufficient retrieval до 5000+ pages.
- **Why risky:** R4 §G acknowledges "open research question". Synthesis hand-waves it ("scale trigger 5000 pages firm or revisit").
- **Evidence:** No production deployments of HippoRAG at 5000-page scale в open literature. PPR (Personalized PageRank) latency grows with edge density — current edges/pages ratio not measured.
- **What if false:** Wiki retrieval becomes slow → agents spend более context loading → cost spike → operational pain.

**Assumption A5 (Area 7 Promotion Signals):** AI agent qualified for promotion после 90-day + <2% escalation + zero critical false-positives.
- **Why risky:** Метрики самооценки. Кто audit agent's escalation rate? meta-agent? Same Claude family — shared blind spots.
- **Evidence:** Anthropic published research on Claude self-evaluation showing systematic biases (sycophancy, over-confidence). Self-graded "ready for promotion" suspect.
- **What if false:** Premature promotion → autonomous decisions с insufficient supervision → client incident.

**Assumption A6 (Area 4 Phase 2 trigger):** First human hire = clean cleave point for Life-OS extraction.
- **Why risky:** Сначала pre-screen interviews (2-3 weeks) → trial period (4-8 weeks) → first formal hire date. На каком из этих moments triggers extraction? Synthesis assumes binary moment.
- **Evidence:** GDPR DPA-required clients требуют DPA ДО data sharing — то есть до того как hire даже начнёт работу. Trigger lags requirement.
- **What if false:** First human onboards с access ко всему monorepo (включая life-os). Privacy violation. GDPR breach (Art. 5 data minimization).

**Assumption A7 (Area 8 14-day plan):** 14 consecutive working days available для Foundation rollout.
- **Why risky:** Solo founder с €0 revenue на one-track focus 14 дней — assumes no sales meetings, no client emails, no personal life intrusions. Real Phase 1 looks like 14-day plan stretches к 6-8 недель.
- **Evidence:** CLAUDE.md показывает 8 active projects + voice-notes pipeline + research workload + Project review tasks. Bandwidth не allocated.
- **What if false:** 14-day plan slips → L1 Foundation incomplete → other layers postponed → Q2 €50K target missed.

---

## Part 3 — Hidden Risks (не mentioned в synthesis)

1. **Anthropic API key leak risk через role-manifest exemplification.** Sample role-manifests checked into public git (если Phase 3 publishing happens, R8 §J.6) могут leak prompt-engineering insights ценные для конкурентов И contain inadvertent client-data in golden datasets (Area 8 Day 7). Synthesis не имеет PII-scrubber check на golden dataset publication.

2. **Claude Code agent infinite-loop / runaway cost.** При misconfigured `tools-allowed` + buggy logic — agent делает тысячи tool calls. Synthesis имеет "cost-overrun rate <10%" SLO (Area 8 Tool stack) но не circuit breaker mechanism. Single runaway session может стоить €100-500.

3. **Git repository corruption.** Mono-dependency на git (Hidden Risk 5.1 #4 mentioned only as "GitHub outage"). Local repo corruption (.git/objects damage from disk failure) — не addressed. SOPS+age key loss = encrypted secrets unrecoverable. Backup strategy mentions restic → Hetzner+Backblaze (Day 14) но не mentions key escrow.

4. **DACH labour law trap при first hire — Geschäftsführer regulatory role.** Synthesis Area 7 mentions Geschäftsführer регистрацию при UG. Не mentioned: Sozialversicherung obligations, Arbeitsschutzgesetz, Mutterschutz risk при hire of female applicant. Architecture не имеет HR compliance layer.

5. **Steuerberater dependency single point.** Steuerberater ошибается с GoBD interpretation — implications cascade в `finance/datev/YYYY-MM.csv` (Area 2 dree). Synthesis treats Steuerberater как infrastructure, не как fallible service provider. Backup Steuerberater? Dual review? Missing.

6. **Claude Code prompt-injection vulnerability через scraped content.** Sales-research agent ingests websites of prospects. Modern attacks (prompt injection via HTML comments, hidden text, file-delivered XML) могут hijack agent. `tools-allowed.forbidden-tools: [git-push, email-send]` — defensive **if enforced**, but architecture не describes prompt-injection threat model.

7. **GDPR Art. 22 (automated individual decisions).** AI agent auto-classifying lead as ICP score 70 (Area 3 acceptance-criteria) может попасть под Art. 22 если decision имеет "legal effects or similarly significantly affects". Synthesis не addresses Art. 22 risk explicitly.

8. **First-mover penalty в "company-as-code" narrative.** Если это unique positioning (Area 1), первые 2-3 Mittelstand клиента будут educate-the-market sales = much longer cycle. Synthesis не allocates time для market education в Q2 2026 timeline.

9. **Karpathy LLM Wiki dependency на specific Karpathy approach evolutions.** Если Karpathy abandons / pivots pattern, no fallback. R4 cites blog post; not academic standard.

10. **Mental load of being "AI-native mega-corp" theatre для one person.** Self-fulfilling prophecy risk: писать "L0 Executive Core" с decision-rights matrices для AI agents — это persona maintenance. Cognitive burden of pretending "we are mega-corp" while doing solo work — measurable in burnout.

---

## Part 4 — Over-Confident Claims

**Claim O1 (Conflict 1 resolution):** "Hybrid C решает operational vs semantic split."
- **Reality:** Resolution shifts split от **storage problem** к **maintenance problem**. Three places (alphas/, clients/, wiki/) now require sync mechanism that synthesis doesn't fully specify. "Solved" means "moved".

**Claim O2 (Conflict 5 resolution):** "R6 major-only folders + git tags. SemVer в frontmatter + git tags give full traceability."
- **Reality:** Git tags непривычная developer-convention — easy для CI, hard для humans navigating. Tag `agent-sales-lead-v2.1.3` discoverable только через `git tag --list`. Solo founder в session A не помнит какая version в session B. Frontmatter SemVer + git tags = double bookkeeping not full traceability.

**Claim O3 (Area 1 Trade-offs):** "Зависимость от Claude Code mitigated: role-manifests portable; exit strategy к любой LLM через standardized YAML contracts."
- **Reality:** Already discussed Concern #2. "Standardized YAML" — synthesis own standard, not industry standard. Portability нigde не tested.

**Claim O4 (Conflict 7 resolution):** "12 illustrative, not константа."
- **Reality:** Throughout synthesis "12 agents" referenced как concrete (Area 8 Day 4: "12 agents с new frontmatter"). Если truly variable, Day 4 should say "all current agents". Inconsistency between principle и operational spec.

**Claim O5 (Area 4 Phase 1 description):** "Asymmetric reference rule enforced (pre-commit hook validation)."
- **Reality:** Hook не написан. "Will be enforced" ≠ "is enforced". Multiple synthesis sections reference hooks as solved when они unbuilt.

**Claim O6 (Area 5 Layer 3 "Context loading budget 50K"):** Точная sum (2+1.5+5+20+3+2+8+3.5 = 45K, не 50K). Math error в budget breakdown — small but symptomatic of "looks designed but unverified".

**Claim O7 (Area 8 14-day rollout) "tested":** "[R2 §H.1-H.10] complete 14-day rollout tested." R2 — research document, не deployment record. "Tested" claim не grounded.

---

## Part 5 — Missing Considerations

1. **Cost model.** Synthesis нигде не quantifies monthly run-rate Phase 1: Anthropic API tokens (12 agents × N sessions × M tokens), Hetzner CPX32 + Storage Box, GitHub paid features, domain, SOPS key infrastructure. Estimated €X/month — should be in Area 8 with break-even analysis.

2. **First customer journey map.** L4 Delivery as primary revenue layer должен иметь explicit sales funnel: cold outreach → discovery → audit pitch → SOW → contract → kickoff → delivery → invoice → retention. Synthesis имеет sales-lead role-manifest но not the funnel.

3. **Onboarding for second human (после Sales Lead).** Phase 2a mentions Head of Finance, но synthesis не specifies onboarding asymmetry: Sales Lead onboarding (R3 §H.5 пункт ~30 hours) vs Head of Finance (different domain, different ramp-up).

4. **Failure modes for Coolify deploy.** "Push-to-deploy" — what if push contains broken role-manifest? Production agent breaks. Rollback procedure missing.

5. **Inter-agent coordination protocol.** "Hub-and-spoke: subagents report to department Lead, not Manager" (CLAUDE.md rule 8) but synthesis Area 3 doesn't specify message format / ack/nack / timeout / retry semantics. Mailbox JSONL pattern — too thin.

6. **Versioning of FPF-Lite itself.** FPF-Lite imports concepts from Левенчук evolving. When Левенчук publishes ШСМ v2.0, Jetix FPF-Lite update path?

7. **EU AI Act compliance.** Mentioned briefly (Area 6 §2 stakeholders) но no compliance roadmap. EU AI Act Art. 9-15 (high-risk AI systems) may apply if AI agents make decisions affecting Mittelstand client business operations. Architecture doesn't classify own AI risk-tier.

8. **Trademark / IP for "Jetix" name.** "Jetix" was previously Disney brand (children's TV channel until 2009). Trademark conflict risk in DACH? Synthesis assumes name available.

9. **Pricing data for SKUs.** L3 mentions "AI Audit / Quick Win / Custom / Retainer" but no €-ranges, no anchor prices. Sales-lead role-manifest references "discount до 10%" — discount of what?

10. **Ruslan's Wochen-/Tagesplanung integration.** CLAUDE.md mentions /plan-day, /close-day skills. Synthesis doesn't integrate these into 14-day rollout or daily rituals (Area 8 §Daily mentions inbox triage, pipeline review — но not /plan-day execution).

---

## Part 6 — Proposed Changes (concrete)

1. **Reduce Phase 1 to 4 layers (L0/L1/L2/L4) — drop L3, L5, L6, L7 from active design.** L3 Product (no SaaS yet), L5 Membrane (Alliance после первого клиента — wait), L6 Topology (18-36 month horizon = 2027-2028, not Phase 1 concern), L7 Portfolio (€0 to allocate). Dropping не означает delete — означает "schema only, no implementation". Reduces synthesis scope ~40%.

2. **Replace 14-day rollout с 7+7 split: Days 1-7 = MVP sales infrastructure; Days 8-14 = L1 Foundation.** Day 1: domain registration. Day 2: first SKU page (AI Audit landing). Day 3: cold outreach list (50 Mittelstand contacts via IHK directory). Day 4: First discovery call template + scheduling. Day 5: Proposal template + first €5K-€15K SKU pricing. Day 6: Contract + ZUGFeRD invoice template. Day 7: Steuerberater intake call. Days 8-14 = current plan compressed.

3. **Compress 8-block role-manifest to 5 blocks for Phase 1 MVP:** identity / ontological / method / implementation_ai / evolution. Drop graph_of_creation (over-spec for solo), seniority (J0-JX premature), implementation_human (premature). Re-introduce при Phase 2 trigger.

4. **Replace triple-representation (alphas/ + clients/ + wiki/entities/) с single source `clients/<slug>/` containing state.yaml + notes.md + history.jsonl.** Wiki references via symlink, not duplication. Eliminate `alphas/` намеspace для Phase 1.

5. **Spec succession protocol explicitly в Constitution §11.** "Если Ruslan unavailable >7 days, automated client-facing template response + escalation to designated emergency contact (Ruslan's spouse / advisor / Steuerberater)". Add `BUS-FACTOR.md` к top-level.

6. **Pre-commit hook spec'ы — write them в Day 2-3 of rollout, not "future work".** Asymmetric reference enforcement, Rechnungsnummer monotonicity, role-manifest required-fields. Without hooks, rules are aspirational.

7. **Replace "Promptfoo + Langfuse" dual с single tool primary в Phase 1.** Pick Langfuse cloud free tier (Open Q5). Reason: cloud=zero ops; covers tracing + eval + prompt registry. Self-host trigger: data residency client requirement (Phase 2).

8. **Quantify cost model в new Section "Phase 1 Run Rate":** API €X/mo (with assumed token velocity), Hetzner €Y, domain €Z, monitoring €W, total €V/mo. Break-even: first SKU pays N months of run rate.

9. **Replace "first human hire timing" Open Q1 с decision rule:** "Hire when (а) 3 consecutive months ≥€20K MRR AND (б) Ruslan reports >40% time на L1/L2 ops tasks (measured in Toggl with explicit J-level tags) AND (в) at least 1 active client requesting GDPR DPA". Triple-AND eliminates premature hire.

10. **Spec circuit breaker для Claude Code agents:** Per-session token budget hard cap (default €5 worth of API spend). Per-agent monthly cap. Hook in Coolify deploy that кill агент-runaway.

11. **Add first-class `clients/_dpa/` folder for GDPR Data Processing Agreements.** Each DPA — document + DPA-checklist YAML + risk assessment. Required для Phase 2 trigger. Currently absent.

12. **Define "strategic client" in Area 7 (Human-AI boundary).** Strategic = (а) ARR contribution >5% OR (б) ≥3 stakeholders на client side OR (в) referrer for ≥1 other client. Clear rule eliminates Ruslan as bottleneck.

13. **Replace "AI agent promotion via 90-day track record" с external audit pattern:** monthly review by meta-agent **+ Ruslan sign-off** of agent escalation log. No promotion without human ratification. Removes self-grading loop.

14. **Add `decisions/0000-architecture-rebuild-budget.md`.** Pre-commit to allocate Q1 2028 sprint для architecture rebuild. Reduces "no rebuild ever" overconfidence; makes rebuild a planned event, not surprise.

15. **Move FPF-Lite to reference document NOT prepended to system prompts.** Each agent's system.md имеет 1-paragraph FPF-Lite summary + link. Full FPF-Lite — meta-agent context only. Saves ~3-5K tokens per agent invocation.

---

## Part 7 — Questions for Final Synthesizer (5-7 meta-questions)

**Q1: "Scale-up-first design" vs "Phase 1 execution" — which wins при conflict?**
- Critic position: Phase 1 execution wins. €0 → €50K is existential. €50K → €500K is gravy. Architecture serves immediate need, evolves later.
- Anticipated Simplifier position: Same as Critic but more aggressive (drop more, keep less).
- Anticipated Mega-Corp position: Scale-up-first wins. Premature simplification = future rewrite. Pay scaffolding cost now.
- Anticipated Левенчук position: Ontology consistency matters. Не оба — design Lite version ontologically correct, scale through depth not breadth.
- Synthesizer must pick. My vote: Critic / Simplifier consensus.

**Q2: Is "AI-native mega-corporation" a real architectural property или narrative positioning?**
- Critic position: Narrative. Synthesis can't articulate concrete "mega-corp property" missing in well-organized solo consultancy.
- Anticipated Simplifier position: Narrative — drop the framing, just describe what we're building.
- Anticipated Mega-Corp position: Real property — embodied in 7 layers, role-abstraction, decision-rights matrix.
- Anticipated Левенчук position: It's an aspiration in Левенчуковской terminology — целевая система проекта определяет архитектуру.
- Synthesizer should clarify: are we describing system-now or system-future-target? Different documents.

**Q3: Pre-commit hooks vs. cooperative discipline — what's the trust model?**
- Critic position: Hooks must exist Day 2 or rules are vapourware. Architecture без enforcement = paper compliance.
- Anticipated Simplifier position: Drop most rules; only keep hooks that pay back (e.g., Rechnungsnummer monotonicity = legal requirement).
- Anticipated Mega-Corp position: Hooks essential for team scaling. Build now.
- Anticipated Левенчук position: Discipline ритуальная; hooks — внешняя поддержка. Both needed.
- Synthesizer must answer: "by Day 14, which hooks MUST be enforced (gate to Phase 1 declaration)?".

**Q4: Bus factor — succession plan or accept existential risk?**
- Critic position: Must have succession protocol. Bus factor = 1 invalidates "mega-corp" claim.
- Anticipated Simplifier position: Accept. Solo founder phase is inherently bus-factor-1; architecture pretending otherwise = waste.
- Anticipated Mega-Corp position: Add Chief of Staff fractional на Phase 0 to reduce bus factor proactively.
- Anticipated Левенчук position: Роль strategic-management — это исполнитель, который может быть compromised. Architectural требование — fallback executor.
- Synthesizer should define minimum viable succession: документ, contact, dead-man's-switch script.

**Q5: Triple-representation (alphas + clients + wiki) — keep or collapse?**
- Critic position: Collapse. Triple-rep is luxury Phase 1 cannot afford.
- Anticipated Simplifier position: Same — collapse to single source.
- Anticipated Mega-Corp position: Keep — triple-rep solves different read patterns (state vs context vs semantic). Pre-commit + index handle drift.
- Anticipated Левенчук position: Альфа vs entity vs concept — три разные онтологические сущности. Collapsing загружает ontology.
- Synthesizer must adjudicate operational vs ontological priorities.

**Q6: Phase 2 trigger — fixed criteria or judgment call?**
- Critic position: Fixed criteria (revenue + time + client GDPR signal). Judgment alone slips.
- Anticipated Simplifier position: Judgment + minimal threshold — over-spec creates false precision.
- Anticipated Mega-Corp position: Layered triggers — leading indicators (pipeline GDPR mentions) + lagging (revenue) + capacity (Ruslan's J2 time).
- Anticipated Левенчук position: Trigger — это альфа state transition. Define states + transitions + acceptance criteria explicitly.
- Synthesizer should write trigger spec as alpha state machine, not prose.

**Q7: 14-day rollout — Foundation-first or Revenue-first?**
- Critic position: Revenue-first (7+7 split). Foundation has zero value if no clients.
- Anticipated Simplifier position: Same — start with sales infrastructure.
- Anticipated Mega-Corp position: Foundation-first; sales ops emerge from Foundation. Order matters.
- Anticipated Левенчук position: Foundation = метод; revenue = результат метода. Метод первый, но не 14 дней — итеративно.
- Synthesizer must decide: this changes whether Q2 €50K target realistic.

---

## Part 8 — Verdict

**YES with material changes.**

**Rationale:** Synthesis correctly identifies the major design questions (9 conflicts well-framed, 10 open questions surfaced) и собирает substantive research. As a research synthesis output it succeeds. Однако as architectural commitment for Phase 1 execution, документ over-commits в 4 dimensions:

1. **Scope inflation** — 7 layers + 10 alphas + 8 blocks + 12 roles + 14-day rollout all "active now" → unrealistic для solo founder. Mitigation: reduce to MVP per Proposed Changes #1, #3.

2. **Inversion of priorities** — €0 to €50K trajectory requires sales infrastructure, but document allocates ~98% real estate to non-sales infrastructure. Mitigation: Proposed Change #2 (7+7 rollout split).

3. **Unproven portability claims** — "role ≠ executor" abstraction asserted, not demonstrated. Architecture has Claude Code dependencies hardcoded в multiple blocks. Mitigation: explicit "we are Claude-Code-coupled in v1, portability is roadmap goal not v1 property".

4. **Unaddressed existential risks** — bus factor, runaway agent cost, prompt injection, Anthropic pricing volatility. Mitigation: Proposed Changes #5, #10 + new "Existential Risk" section в D1.

**What is genuinely good** (resist temptation to attack everything): Conflict-resolution structure (Part 3) honest about trade-offs. Open Questions section (Part 4) admits not-yet-decided. Source citation discipline (Appendix A) traceable. Career Ladder + Decision-rights table (Area 7) — best-shaped section. FPF-Lite scoping (Area 6) explicit about what's excluded — good.

**Recommendation to Final Synthesizer:** accept synthesis as v1-input, but require D1 final to have explicit "Phase 1 Minimum Viable Architecture" subsection that strips concept to executable Phase 0→1 path (≤3 months work). Full 7-layer architecture survives as Reference Architecture, not Operational Architecture. Without this split, Stage 6 deployment will either (а) overrun timeline by ~3x, or (б) ship partial implementation labeled "complete" — both outcomes worse than honest Phase 1 / Phase 2+ separation.

---

**END OF CRITIC REVIEW** — devil's advocate complete. Adversarial position registered.
