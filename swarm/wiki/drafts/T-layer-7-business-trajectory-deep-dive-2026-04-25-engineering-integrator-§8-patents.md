---
id: T-layer-7-business-trajectory-deep-dive-2026-04-25-engineering-integrator-§8-patents
title: "§8 Patents Strategy + IP Licensing — L7 Business Trajectory Deep-Dive"
type: section-draft
layer: L7
section: §8
cell: C-11
expert: engineering-expert
mode: integrator
cycle_id: cyc-layer-7-business-trajectory-deep-dive-2026-04-25
task_id: T-layer-7-business-trajectory-deep-dive-2026-04-25
brigadier_cycle_number: 7
phase: Phase 2 Wave 3
created: 2026-04-25
word_floor: 1500-2000
status: draft
state_transition_target: AWAITING-APPROVAL
provenance_inline: true
locks_referenced: [D13, D14, D15, D17, D19, D20, D21, D24, D25, D27]
sources:
  - {path: "swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md", range: "§4 28 Locks + §8 Anti-scope"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D25 Company-as-Code + D27 Fork-and-merge"}
  - {path: "decisions/JETIX-VISION.md", range: "D13 Closed core/Open surface + D14 research revenue-instrumental + D20 USB-C + D24 open-source research"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3.2 Phase 1 infra + §4 Phase 1→2 legal + §6.2 Phase 3 legal"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§4 IP strategy + §8 rec 4 + §9 Q4 patent budget"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§5 Alliance Option C + §12 Q-04 IP license"}
  - {path: "decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md", range: "§3.7 Educational methodology licensing"}
acceptance_predicate: |
  §8 passes if: Phase-1 = defensive-only (zero patent filing, D14 + D15 enforced); Phase-1→2 = €500-€1500 lawyer consultation only (landscape research, no filing); Phase-2 = EU patent application €2000-€3500 per OT4; Phase-3+ = Foundation Apache 2.0 + LGPL + Jetix-Corp proprietary licensing tiers; IP audit enumerates ≥5 defensible IP categories with per-item protection mechanism; every major claim carries F-G-R triple; anti-scope enforced (no filing Phase-1, no Phase-3 strategic docs, no Notion writes).
anti_scope:
  - "NO patent filing Phase-1 (D14 + D15)"
  - "NO Phase-3 strategic doc prose"
  - "NO Notion writes"
  - "NO API-key refs"
  - "NO reopening 28 Locks"
  - "NO duplication with L6 §12 Q-04 (IP license decision) — L7 §8 implements it"
---

# §8 Patents Strategy + IP Licensing

> Раздел L7 §8 — IP-стратегия Jetix по фазам. Адресует четыре вида IP
> (патенты / авторские права / товарные знаки / коммерческая тайна) × фаза роста.
> Binding constraints: D14 (research revenue-instrumental Phase-1), D15 (revenue-gated spend),
> D13 (Closed core / Open surface), D25 (Company-as-Code provenance), D27 (Fork-and-merge governance).
> L6 §12 Q-04 acked Apache 2.0 + LGPL-equivalent software для Foundation;
> proprietary для Jetix-Corp closed core. L7 §8 имплементирует это решение в
> конкретные фазовые бюджеты, механику защиты и программу лицензирования.

---

## §8.0 Framing — IP-стратегия как (патенты + авторские права + товарные знаки + коммерческая тайна) × фаза

IP-стратегия Jetix не является однородным пространством: разные виды IP доступны в разных фазах при разных бюджетных ограничениях. Для Phase-1 бюджет на IP-подачи = €0 (D14 + D15 — hard constraint). Это не слабость — это рациональное применение D15 revenue-gated spend: IP-стоимость захватывается через комбинацию авторского права (автоматическое), коммерческой тайны (управленческое) и доказательства приоритета через git-провенанс (D25 Company-as-Code).

**Preservation-by-architecture** — ключевой Phase-1 принцип: архитектура системы сама по себе является формой IP-защиты. D13 Closed core / Open surface разделяет то, что защищено закрытостью (ядро методологии), от того, что защищено открытостью (поверхностные фреймворки привлекают сообщество). D17 filesystem-SoT + D25 Company-as-Code создают timestamp-цепочку приоритета для каждого элемента методологии без единого евро расходов на патентное бюро.

**Фазовая логика IP-спенда:**

| Фаза | Бюджет | Механика защиты | Основание |
|---|---|---|---|
| Phase-1 (€0-€50K) | €0 | Авторское право + коммерческая тайна + git-провенанс | D14 + D15 |
| Phase-1→2 (€50K-€200K) | €500-€1500 | Патентный ландшафт-ресёрч (только консультация) | D15 unlock |
| Phase-2 (€200K+) | €2000-€3500/патент | EU EPO подача × 3-5 инноваций | D15 unlock |
| Phase-3+ | портфель | Портфель + лицензионная программа + D27 fork-and-merge | D27 + L6 Q-04 |

**Defensible IP enumeration.** Jetix обладает защищаемым IP в пяти категориях (полный аудит — §8.5). Центральный тезис: наиболее ценный IP Phase-1 — это методология FPF + 9 Jetix Innovations из D6 / ADR-Chunk-8 Area 2. Эти инновации являются кандидатами на патентную защиту Phase-2+; до тех пор они защищаются коммерческой тайной (D13) и доказательством приоритета через git-историю (D25).

---

## §8.1 Phase-1 (€0-€50K) — только защита, нулевой бюджет патентных заявок

### D14 revenue-instrumental: нет расходов на абстрактный IP Phase-1

D14 зафиксирован: research revenue-instrumental Phase-1. Расширение на IP: любой IP-spend, который не конвертируется прямо в Phase-1 revenue, откладывается. Патентная заявка в EPO обрабатывается 18-36 месяцев и не генерирует дохода Phase-1. Следовательно: **нулевой бюджет патентных заявок Phase-1 — не компромисс, а логически выверенное решение.** [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§4-D14]

**F-G-R (Claim Phase-1 IP budget = €0):**
- F: F5 (кодифицировано — D14 + D15 зафиксированы Ruslan'ом; применение к IP-spend прямое)
- ClaimScope: holds Phase-1 €0-€50K; NOT holds при экстренном появлении конкурента с overlapping patent claim — HITL-override per §8.8 D-IP-1
- R: refuted если конкурент подаёт патент на overlapping Jetix innovation во время Phase-1 (trigger: §8.8 D-IP-1 escalation path); accepted если €50K достигнут без IP-filing spend и ни одна из 9 Jetix innovations не оспорена юридически

### Defensive measures (все нулевой стоимости)

**1. Атомарные git-коммиты с провенансом (D25).** Каждое изменение методологии — commit с attribution, timestamp и описанием. Это создаёт audit trail для prior-art disputes: если конкурент подаёт патент на AI×Mittelstand method combination, Jetix демонстрирует earlier creation date через git log. Это Phase-1 эквивалент «предварительной заявки на патент» без стоимости. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]

D25 verbatim: «строить инфраструктуру Company as a Code с самого начала, способную выдержать масштабирование до триллиона капитализации» + «в режиме GitHub работала — компания как код, знания как код». Каждый commit = timestamped IP assertion. Инструкция Phase-1: все `decisions/` + `swarm/wiki/foundations/` + `swarm/wiki/designs/` файлы коммититься атомарно с явным описанием создаваемого методологического элемента.

**2. Авторское право на документы методологии (автоматическое).** Авторское право возникает автоматически при создании оригинального произведения. Все файлы `decisions/JETIX-*.md`, `decisions/LAYER-*.md`, `swarm/wiki/foundations/`, `agents/*/system.md` защищены авторским правом Ruslan (Berlin) с момента создания. Действие Phase-1: добавить явное © notice в header всех `decisions/` + `swarm/wiki/designs/` файлов. Формат: `© 2026 Ruslan [Jetix]. All rights reserved.` Стоимость: ноль. [src:decisions/JETIX-PLAN.md#§3.2]

**3. Коммерческая тайна: закрытое ядро Jetix (D13).** D13 Closed core / Open surface зафиксирован: ядро методологии (специфические prompt-шаблоны, оптимизированные под Mittelstand DACH ICP; клиентские KB-адаптации; конфигурации оркестрации agent-swarm) защищено как коммерческая тайна через управленческую дисциплину. Операционно: NDA-шаблоны во всех клиентских engagement'ах (базовые NDA-шаблоны Phase-1 — часть Phase-1 legal setup per JETIX-PLAN §3.2); явное обозначение `CONFIDENTIAL` на закрытых документах; ограниченный доступ к core-директориям. [src:decisions/JETIX-VISION.md#D13]

**4. Документальная дисциплина как IP-защита.** FPF + VISION + PLAN + ARCHITECTURE-BRIEF написаны с inline-провенансом (`[src:...]` citations per D25 Company-as-Code discipline). Это формирует defensible record: каждое методологическое утверждение отслеживаемо до первоисточника (voice-memo, research, decision). Это уровень документации, который выдерживает IP-ревью при Phase-2+ due diligence. [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§4-D25]

### Anti-pattern: преждевременная патентная заявка

Преждевременная патентная заявка Phase-1 — это нарушение D14 + D15. Конкретные аргументы против:
- EPO processing: 18-36 месяцев prosecuting → ноль дохода за этот период
- Cost: €2000-€3500 per application cash outflow в момент когда runway критичен
- AI-method patents: rejection rate EU > 40% для software-method claims → риск потери и денег, и времени
- Alternative: git-провенанс (D25) создаёт equivalent prior-art protection бесплатно

**F-G-R (Claim: Patent filing Phase-1 rejected per D14 + D15):**
- F: F5 (D14 + D15 = locked decisions; логическое применение прямое)
- ClaimScope: holds Phase-1 €0-€50K unconditionally; single exception: competitor patent-filing on overlapping Jetix innovation triggers §8.8 D-IP-1 override
- R: refuted если Ruslan явно override D14/D15 для конкретного патента с обоснованием «revenue-direct» применимости (HITL-only decision)

---

## §8.2 Phase-1 → Phase-2 transition (€50K-€200K) — патентный ландшафт-ресёрч

### Бюджет: €500-€1500 (только консультация адвоката, без подачи)

После прохождения €50K gate (D15 unlock) открывается первый IP-бюджет: €500-€1500 для **патентного ландшафт-ресёрча только**. Это консультационный бюджет — оплата DACH IP-адвоката за prior-art search + patentability opinion + оценку стоимости EU-подачи per candidate innovation. Никакой подачи заявок в Phase-1→2 transition — только research. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§8-rec4 + §9-Q4]

**F-G-R (Claim: Patent landscape research budget Phase-1→2 = €500-€1500):**
- F: F3 (substantive — STRATEGIC-INSIGHT §8 rec 4 reference; typical DACH IP attorney rates €150-€300/hr → 3-5h = €450-€1500 for initial landscape opinion)
- ClaimScope: EU-only landscape research; excludes international search (Phase-3+); excludes prosecution amendment fees
- R: refuted если first DACH IP attorney quote exceeds €2000 for initial landscape research; accepted при receipt Lehner-or-equivalent quote ≤€1500 (receipt: lawyer engagement letter filed in `decisions/ip-lawyer-engagement-[date].md`)

### Профиль адвоката: DACH IP attorney, Mittelstand-специализация

STRATEGIC-INSIGHT §8 rec 4 + §9 Q4 называет конкретный профиль: **Лехнер (Lehner) в Германии** — IP-адвокат со специализацией на Mittelstand, SME pricing. Ставки: €150-€300/час (vs крупные IP-firms €400-€800/час). Phase-1→2 бюджет €500-€1500 предполагает 2-5 billable hours = первичная консультация + preliminary prior-art landscape + patentability opinion на 3-5 kandidatov. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§9-Q4]

### Кандидаты: 3-5 патентоспособных инноваций Jetix из D6

Landscape research фокусируется на 3-5 кандидатах из D6 inventory (полный список — §8.5 IP audit). На основе current knowledge, наиболее патентоспособные кандидаты для EU research:

1. **Stage-Gated HITL protocol** (D8 + SG-1..SG-5 predicate DSL) — AI orchestration с explicit human-in-the-loop gates; potential AI×process claim
2. **Client-private local-first AI architecture** (Path A/B/C per STRATEGIC-INSIGHT §5) — federated KB isolation pattern; AI×privacy claim
3. **Fork-and-merge methodology evolution** (D27) — version-control applied to business methodology; method claim
4. **Query-driven KB filtering** (D28) — anchor-mandatory ingest pattern; information retrieval claim
5. **Matchmaker 3-cadence progression** (manual → AI-smoothed → platform, D21 + L6 §6) — AI-assisted professional matching with progressive automation; platform method claim

Deliverable landscape research: per each candidate — (a) prior art search summary, (b) patentability opinion (yes/no/conditional), (c) estimated EU filing cost, (d) recommendation filing/abandon/monitor.

### Trademark Jetix vs Disney: парковка P5

Товарный знак «Jetix» паркован как P5 per TENSIONS-RESOLVED-STAGE-2B pending Disney clarification. Disney ранее использовал бренд Jetix для programming block (2003-2009). В 2026 Disney не имеет активного trademark use в AI/consulting domain — но риск trademark opposition существует. [src:raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md P5]

**Действие Phase-2a:** engage trademark counsel для одноразового legal review. Бюджет: €1-2K (trademark attorney, 2-4 hours). Вопросы review: (a) активен ли Disney registration в EU classes 41-42 (education/consulting)? (b) Есть ли риск likelihood of confusion в AI/consulting domain? (c) Стоит ли регистрировать Jetix-отдельный-вариант или защищаться через use-based trademark?

**Timing:** Phase-2 (post-€200K), не Phase-1→2 transition. Причина: risk низкий Phase-1 (нет public commercial use scale достаточного для opposition trigger); Phase-2 — первая коммерчески значимая scale point.

---

## §8.3 Phase-2 (€200K+) — EU patent application

### Бюджет: €2000-€3500 per application

После прохождения €200K gate открывается полный IP-бюджет. EU patent application через EPO: €2000-€3500 per application = EPO official fees (search fee ~€1350 + examination fee ~€1640 + designation fees) + DACH attorney prosecution fees. Total для 3-5 патентов: €6K-€17K Phase-2 patent-filing budget. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§8-rec4]

**F-G-R (Claim: Phase-2 EU patent application budget = €2000-€3500 per application):**
- F: F3 (substantive — EPO official filing fees + DACH patent attorney typical rates 2026; STRATEGIC-INSIGHT §8 rec 4)
- ClaimScope: EU patent application per innovation; excludes international filing (Phase-3+); excludes prosecution amendment fees if complex office actions
- R: refuted если actual quote from Lehner или equivalent DACH IP attorney превышает €5K per application для standard prosecution; receipt at lawyer quote request Phase-1→2 transition

### Jurisdiction: EU primary (EPO), US/international Phase-3+

Jurisdiction selection per D10 geographic rollout: English+US primary sales market Phase-1→2, но Germany = legal home. EPO filing предоставляет coverage EU-27 + UK (через EPC separate) + CH/NO/IS. Priority claim: EPO filing creates Paris Convention priority for subsequent US/PCT filing Phase-3+. Не нужно одновременно подавать US — priority сохраняется 12 месяцев от EPO filing date.

**Filing sequence:**
1. Prior-art search Phase-1→2 (done; €500-€1500 budget)
2. Draft application — DACH attorney + Ruslan (methodology detail)
3. EPO submission → formal examination → search report (12-18 months)
4. Prosecution: respond to office actions → grant or rejection (18-36 months total)
5. Grant probability: EU AI/software-method patents — исторически 40-60% EPO (source: EPO annual report 2024); чем конкретнее method claim, тем выше вероятность

### Patent scope: AI×Mittelstand method combinations

STRATEGIC-INSIGHT §8 rec 4 прямо рекомендует: «Patents on AI×Mittelstand method combinations — licensable assets». Scope claim должен охватывать специфическую комбинацию AI-method + Mittelstand-context, а не общий AI-algorithm (последнее не патентоспособно EU). Конкретика повышает patentability: «Method of client-isolated AI knowledge base construction with query-driven filtering for SME business intelligence» конкретнее и патентоспособнее чем «AI knowledge management method». [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§4]

---

## §8.4 Phase-3+ — patent portfolio + licensing program

### Portfolio structure per D27 + L6 Alliance Option C Hybrid

D27 Fork-and-merge + L6 Option C (Mozilla/Red Hat analog, acked Q-04) создают двухуровневую IP-структуру: [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27 + decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§12-Q04]

**Foundation (некоммерческий, Apache 2.0 + LGPL):**
- Methodology documentation: Apache 2.0 (permissive) — внешние форки разрешены, attribution required
- Open-source software components: LGPL (weak copyleft) — модификации LGPL-компонентов остаются LGPL; proprietary стек может линковаться без LGPL-contamination
- Foundation publishes → ecosystem forks allowed → best mutations merge-back upstream (D27)
- Что публикуется: framework-level patterns (templates, compliance checklists, fork-and-merge protocol spec), но НЕ closed-core Jetix-specific implementations

**Jetix-Corp (коммерческий, proprietary):**
- Closed-core methodology (D13): специфические prompt-шаблоны, client-specific KB adaptations, agent orchestration configs — proprietary advanced patterns
- Licensed selectively per tier (см. ниже)
- Patent portfolio Phase-2+: patents filed per §8.3 → licensable assets

### Licensing tiers (concrete € per L5 §3.7)

[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.7]

| Tier | Target | Price | Mechanic |
|---|---|---|---|
| Practitioner license | Individual consultant using Jetix methodology for client work | €500-€5K/year | Annual renewal; methodology access + templates + update stream |
| Corporate license | Corporation using Jetix methodology internally | €10-€50K/year | Per-entity; tiered by company size (SMB/Mittelstand/Enterprise) |
| Alliance member license | Included in Alliance dues (Option C Hybrid) | Included | Membership dues cover Foundation methodology access |
| Strategic partner license | Large corporations (Porsche/BMW/Apple/Google scale) | Negotiated €50K-€500K/year | Custom terms; methodology + integration support + co-branding |

**F-G-R (Claim: Practitioner license €500-€5K/year):**
- F: F4 (operational convention — L5 §3.7 educational methodology licensing; analogous to professional software licenses e.g. JetBrains €69-€249/year per developer, Figma $45/month per editor)
- ClaimScope: holds for individual practitioners using Jetix methodology commercially; NOT applicable for internal personal use without client work
- R: refuted если Phase-2 market testing shows ≤5% willingness-to-pay at €500/year minimum tier; accepted при Phase-2 Alliance member survey showing ≥20% would pay ≥€500/year for practitioner access

### Revenue-share model (co-consultant network)

[src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§5 + decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.7]

Co-consultant использует Jetix methodology + получает referrals через Matchmaker (L6 §6):
- **Option A (methodology fee):** Jetix получает 15-25% methodology license fee от co-consultant's annual earnings using Jetix methods
- **Option B (referral fee):** Jetix получает 10-20% от стоимости engagement при referral-initiated contract
- **Enforcement:** Alliance membership agreement + methodology-repo fork-and-merge governance (D27) + git-provenance audit trail (D25)

Выбор A vs B per engagement — операционное решение Phase-2+ (Ruslan HITL); оба механизма co-exist в Alliance framework.

---

## §8.5 IP аудит — защищаемый IP Jetix

### Category 1: FPF-grounded methodology (9 Jetix Innovations)

[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27 + decisions/JETIX-VISION.md + decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§4]

| # | Innovation | Protection mechanism Phase-1 | Phase-2+ path |
|---|---|---|---|
| 1 | Stage-Gated HITL protocol (D8 + SG-1..SG-5 predicate DSL) | Git-provenance (D25) + коммерческая тайна (D13) | Patent candidate: AI orchestration with human-gate mechanism |
| 2 | Fork-and-merge methodology evolution (D27) | Git-provenance + авторское право на protocol docs | Patent candidate: methodology version-control method |
| 3 | Query-driven KB filtering (D28) | Git-provenance + коммерческая тайна | Patent candidate: anchor-mandatory ingest pattern |
| 4 | Client-private local-first AI architecture (Path A/B/C) | Git-provenance + NDA в client engagements | Patent candidate: federated AI-KB isolation method |
| 5 | Roy-replication methodology distribution (D21) | Git-provenance + авторское право | Patent candidate: methodology replication protocol |
| 6 | USB-C standards-level AI-ecosystem positioning (D20) | Авторское право на framework docs | Trademark potential; standards publication |
| 7 | Company-as-Code operational discipline (D25) | Git-provenance (self-proving) + авторское право | Reference implementation publication |
| 8 | Matchmaker 3-cadence progression (D21 + L6 §6) | Git-provenance + авторское право | Patent candidate: progressive AI-matching automation |
| 9 | Secure Network folk-community governance (D16 + D27) | Авторское право на governance docs + NDA | Foundation methodology publication (Apache 2.0) |

**F-G-R (Claim: 9 Jetix Innovations = defensible IP portfolio):**
- F: F4 (operational convention — innovations documented in locked decisions + git history; patentability unverified until landscape research)
- ClaimScope: holds as prior-art defense per D25 git-provenance; patentability in EU NOT confirmed until Phase-1→2 lawyer consultation
- R: refuted если ≥5 из 9 innovations имеют prior art published before earliest Jetix git commit on relevant topic; accepted при Phase-1→2 lawyer report showing ≥3 innovations have patentability merit

### Category 2: коммерческие тайны (Closed core per D13)

- Специфические prompt-шаблоны, оптимизированные под Mittelstand DACH ICP
- Клиентские KB-адаптации (per-engagement proprietary)
- Конфигурации agent orchestration (swarm protocols, brigadier dispatch logic)
- Внутренние FPF-применения (конкретные matrix-parameters, mode-dispatch heuristics)

**Protection механика:** NDA в клиентских engagement'ах; internal access controls; D13 discipline (open surface published / closed core never); explicit `CONFIDENTIAL` marking на всех core-documents.

### Category 3: авторские права

- Методология documents: VISION, PLAN, FPF, SYSTEM-OVERVIEW, все LAYER-N deep-dives — protected automatically upon creation
- Training materials Phase-2+ educational direction (per L5 §3.7)
- Marketing content (landing pages per L6 §7.5, sales decks)
- Swarm code: agent system prompts, shared protocols, brigadier logic — software copyright

**Action Phase-1:** добавить `© 2026 Ruslan [Jetix]. All rights reserved.` в header всех `decisions/` files. Cost: zero. Explicit © notice усиливает enforcement позицию.

### Category 4: товарные знаки

- **Jetix**: парковка P5; engage trademark counsel Phase-2a (€1-2K one-shot); pending Disney-clarification (см. §8.7)
- **Smart AI**: internal label только (не D29; Ruslan «не лок блять забей»); A/B test G2 trigger per L5 Q-03 — Δ ≥15% response-rate + ≥20% clarity delta required для external promotion consideration [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md Q-03]
- **Direction names**: Mittelstand AI Alliance, Secure Network — file trademark Phase-2 after first use in commerce documented (first commercial use = trademark priority in EU)
- **USB-C (as metaphor)**: NOT trademarkable in isolation (descriptive/generic); Jetix methodology application documented as reference — используется как positioning narrative, не brand claim

### Category 5: патенты (Phase-2+ подача)

3-5 patentable innovations из Category 1; конкретный selection — на Phase-1→2 landscape research. Preliminary ranking по patentability potential:

1. Stage-Gated HITL protocol — конкретный, technical, novel combination
2. Client-private local-first AI architecture — specific federated pattern
3. Query-driven KB filtering — specific algorithmic approach
4. Matchmaker 3-cadence progression — specific platform method
5. Fork-and-merge methodology evolution — potentially prior art heavy (GitHub mechanics known); lower priority

---

## §8.6 D27 fork-and-merge governance: IP implications

[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]

**Что можно форкать:**
- Foundation methodology (Apache 2.0) — framework-level templates, compliance checklists, protocol specs
- LGPL software components — open-source tooling, reference implementations

**Что нельзя форкать:**
- Jetix-Corp proprietary core (D13 closed core) — closed until explicit license grant
- Patent-protected methods Phase-2+ — без royalty license agreement

**Merge-back IP mechanism:**
- External fork contributor retains authorship attribution на конкретных commits (D25 git-provenance)
- Foundation retains methodology-document copyright на canonical upstream
- Jetix-Corp retains proprietary-core copyright; merge-back contributor grants Jetix irrevocable license на contribution
- **CLA (Contributor License Agreement):** Phase-2+ fork-and-merge требует CLA от contributors — стандартная практика (Apache Software Foundation CLA model)

**Governance Phase-1→Phase-3+:**
- Phase-1: BDFL (Ruslan) — единственный maintainer upstream per D27 verbatim + L6 §10.5
- Phase-2: committee starts forming из Alliance-членов с ≥12 месяцев + ≥3 merged contributions
- Phase-3+: committee/meritocracy; Ruslan BDFL veto time-limited per L6 §5 antitrust mitigation (Bundeskartellamt precedent)

**IP attribution rule (D25 + D27):** merge-back contributor gets `Co-authored-by:` в git commit + named credit в CONTRIBUTORS.md. Foundation retains publication copyright. Jetix-Corp retains core copyright. Нет transfer of ownership — только irrevocable contribution license.

---

## §8.7 Trademark strategy

**Jetix trademark (P5 парковка):**
Phase-2a action: engage trademark counsel (DE, IP specialty) для одноразового review. Бюджет €1-2K. Scope review: (a) активен ли Disney EU registration в classes 41-42? (b) likelihood of confusion analysis в AI/consulting domain? (c) регистрировать через EU EUTM (European Union Trademark) или DE DPMA first? Timing: post-€200K, не раньше. Phase-1: строгая парковка — никаких public-facing использований «Jetix» в коммерческих контекстах beyond current scope (current use = internal + existing client contacts).

**Smart AI (conditional D29):**
[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#Q-03]
A/B test params Phase-2 G2: ≥15% response-rate delta + ≥20% clarity delta в outreach vs Jetix-branded variant. Если delta достигнута → Ruslan evaluates D29 promotion (HITL decision). Trademark Smart AI = action ТОЛЬКО после D29 promotion + evidence of external use. Phase-1: internal marker only.

**Direction names (Secure Network, Mittelstand AI Alliance):**
- EU trademark priority = first use in commerce, не registration date
- Phase-1 action: document all public uses с timestamps (DMs, posts, landing pages) — creates priority evidence
- Phase-2 action: file EU EUTM for Mittelstand AI Alliance + Secure Network после first commercial use documented

**International strategy:**
- DE/EU primary (GmbH domicile + primary market Phase-2)
- US secondary Phase-3+ (per D10 geographic rollout; US trademark filing after EU grant)
- Estimated US trademark cost: $350-500 per class (USPTO filing fee) + attorney; Phase-3+ budget

---

## §8.8 Preserved dissents

**D-IP-1: Patent filing timing — Phase-2 first application vs Phase-1 early filing if competitor emerges.**
Default: Phase-2 (D15 revenue-gated). Override trigger: competitor files patent application on overlapping Jetix innovation during Phase-1. If triggered: Ruslan HITL decision whether to (a) respond with prior-art submission (git-provenance D25 evidence; cost ~€500 attorney review), (b) accelerate own filing despite D14/D15 (requires explicit Lock override), или (c) monitor and challenge during prosecution phase (cheaper). Default retained — HITL override only on trigger.
- F: F4 (operational convention; D15 codified; override trigger is speculative)
- R: refuted если competitor filing occurs AND git-provenance defense insufficient; accepted при €50K without competitor patent conflict

**D-IP-2: Apache 2.0 vs MIT vs dual-license для Foundation methodology.**
L6 §12 Q-04 acked: Apache 2.0 (permissive документация) + LGPL-equivalent software (weak copyleft). Retained default. MIT alternative (более permissive, меньше attribution enforcement) — не выбрано, т.к. Apache 2.0 patent-license-back clause защищает Jetix от contributors, которые потом патентуют contributed methodology. Dual-license (proprietary + open option) — отложено Phase-3+ если market shows value в proprietary-only access tier поверх Foundation. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§12-Q04]
- F: F5 (codified — L6 Q-04 acked by Ruslan)
- R: refuted если legal counsel advises Apache 2.0 incompatible с EU jurisdiction specific requirements; accepted при first Foundation publication under Apache 2.0

**D-IP-3: коммерческая тайна vs open-source publication — case-by-case.**
D13 grammar: Closed core / Open surface. Реализация: которые конкретные prompts/patterns остаются closed, а какие публикуются — case-by-case Phase-2+ decision. Операционный критерий: «публикуем framework (HOW to think about X), не implementation (specific WHAT для Jetix ICP)». Пример: публикуется ICP filter framework (5-criteria D22 structure) — не публикуется конкретный discovery script optimized на Mittelstand psychographics. Граница проходит per D13 grammar per decision, не по глобальному правилу.
- F: F4 (D13 codified; case-by-case boundary not yet drawn for all elements)
- R: refuted если competitor replicates Jetix methodology from published Foundation content alone; accepted если Foundation publications do NOT enable full methodology replication without proprietary core

---

## §8.9 Cross-section reconciliation note

**Feeds §4 gate triggers:**
- Phase-1→2 transition: IP landscape research line item €500-€1500 (lawyer consultation)
- Phase-2 (€200K+): patent applications €2000-€3500/патент × 3-5 = €6K-€17K
- Phase-2 trademark review: Jetix/Disney clarification €1-2K one-shot
- Phase-2 foundation formation legal (L6 §5 Option C): €30K-€50K for dual-entity setup

**Feeds §7 cash flow:**
- Phase-1→2 transition: IP legal line item €500-€1500 (одноразово; post-€50K)
- Phase-2 IP filing: €6K-€17K total patent portfolio; €1-2K trademark; можно распределить 18-24 месяцев prosecution
- Phase-2 Foundation formation: €30K-€50K (одноразово; separate budget item)

**Feeds §9 investor relations (data-room Phase-2+):**
- IP portfolio = data-room material Phase-2+: patent applications pending + copyright registrations + trademark filings = defensible IP narrative
- Investor due diligence checklist: NDA templates, © notices on core docs, git-provenance audit trail, landscape research report, patent application status
- Clean IP audit = prerequisite для serious investor conversations Phase-2+ (L7 §9 investor roadmap)

**Note on §6 overlap (L6 §12 Q-04):** L6 Q-04 принял решение по IP license (Apache 2.0 + LGPL + proprietary). L7 §8 имплементирует это решение в фазовые бюджеты + конкретные licensing tiers + enforcement mechanics. Нет дублирования — есть impl-layer иерархия.

---

## §X Cell C-11 self-improvement notes

**Pattern 1: IP strategy phase decomposition (3-slot template).**
IP стратегия для pre-revenue stage = три слота: (Phase-1 = zero-cost defensive architecture) + (Phase-1→2 = bounded research budget) + (Phase-2+ = revenue-gated filing). Каждый слот имеет hard budget ceiling derived from revenue milestone. Паттерн prevents IP-spend drift: единственный способ обосновать IP-spend Phase-1 — это доказать, что он revenue-direct (D14 criterion). Применение: любой future IP question в swarm cycle проходит эту 3-slot template первым.

**Pattern 2: Preservation-by-architecture как Phase-1 IP moat.**
D25 Company-as-Code + D13 Closed core + atomic git commits = полноценная IP defense без единого €. Это инверсия стандартного consulting thinking («нужен патент для защиты IP»): архитектура системы (git-provenance = timestamped prior-art chain) + управленческая дисциплина (NDA + closed core) + явное © = достаточная Phase-1 protection. Паттерн для strategies.md: `defense-by-architecture-phase1` — когда Phase-1 budget = €0, architectural IP defense = primary moat.

**Pattern 3: License structure follows entity structure.**
D27 fork-and-merge + L6 Option C (Foundation + Corp) → IP license structure mirrors entity structure: Foundation = open license (Apache 2.0 + LGPL), Corp = proprietary. Попытка создать license structure несовместимую с entity structure = governance conflict. Rule: IP license design должен начинаться с entity structure, не с IP preferences. Применение: Phase-3+ token economy (D23) license structure — тоже должна следовать entity structure, не наоборот.

---

*End of §8 Patents Strategy + IP Licensing (Cell C-11, engineering-expert × integrator, cyc-layer-7-business-trajectory-deep-dive-2026-04-25).*
