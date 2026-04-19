---
type: research-synthesis
version: v1-draft-for-review
stage: 1 of 6 — Deep Synthesis
status: ready-for-multi-chat-review
owner: ruslan
author: claude-code-opus-4-7 (Stage 1)
created: 2026-04-19
input-research:
  - raw/research/career-levels-deep-research-2026-04-19.md
  - raw/research/company-as-code-impl-deep-research-2026-04-19.md
  - raw/research/levenchuk-for-ai-deep-research-2026-04-19.md
  - raw/research/knowledge-architecture-deep-research-2026-04-19.md
  - raw/research/crm-sales-architecture-deep-research-2026-04-19.md
  - raw/research/folder-structure-deep-research-2026-04-19.md
  - raw/research/jetix-life-separation-deep-research-2026-04-19.md
  - raw/research/org-chart-in-git-deep-research-2026-04-19.md
  - raw/research/mega-corp-governance-deep-research-2026-04-19.md
total-research-words: ~66000
output-target-length: 10000-15000 слов
next-stage: Этап 2 — Multi-chat expert review (5 параллельных chats)
blocks: D1-D9 чистовики
---

# Deep Synthesis — Jetix Architecture v1 Final (pre-review)

> Integrated architecture recommendation на базе 9 research-волн (~66K слов)
> для Jetix OS mega-corporation. Stage 1 output, input для Stage 2 multi-chat review.

---

## 📖 Executive Summary

**Jetix — это AI-native mega-corporation одного founder'а (Ruslan, Берлин), спроектированная с Day 1 так, чтобы scale до 30 / 100 / 200+ ролей без архитектурного rebuild.** Не "solo с AI-помощниками", а корпоративная инфраструктура в миниатюре, где роль — абстрактный контракт, а исполнитель (Claude-агент сегодня, junior-human завтра, C-level executor послезавтра) подключается через единую role-abstraction.

Девять research-волн — R1 Career Levels, R2 Company-as-Code, R3 Левенчук/ШСМ, R4 Knowledge Architecture, R5 CRM+Sales, R6 Folder Structure, R7 Jetix vs Life-OS, R8 Org-in-Git, R9 Mega-corp Governance — сходятся на **шести фундаментальных принципах**, которые переходят из этого synthesis в чистовую архитектуру:

1. **Company-as-Code, буквально.** Git-репозиторий — единственный source of truth для ролей, процессов, решений, клиентов, финансов, org chart. Markdown + YAML + JSONL — primary storage. Notion — view layer, не база. Это наследие GitLab Handbook + Oxide RFD + Holacracy Constitution как public git-артефакт, синтезированное с Karpathy LLM Wiki паттерном для AI-агентского контекста.

2. **Role ≠ Executor (ШСМ-онтология, 1:1 для AI).** Role-manifest — 8-блочная YAML+Markdown спецификация (identity / ontological / method / graph-of-creation / seniority / implementation-ai / implementation-human / evolution) в `roles/<slug>/role.md`. Executor — `executors/<id>.yaml` (привязка к Claude-модели сегодня, к человеку при найме). Это [R3 §C.1–C.9] + [R8 §C.2–C.4]. Смена модели Claude 4.7 → Claude 5 или смена executor с AI на human не требует пересмотра accountabilities.

3. **10 core alphas с explicit state machines.** Client, Project, Deal, Invoice, Content Item, Hypothesis, SKU, Member, Research Note, Postmortem — каждая альфа имеет lifecycle state.yaml + context.md + history.jsonl ([R3 §D, R4 §D.1 Hybrid C]). Для шести "operational" альф (Client, Project, Deal, Invoice, Content, Member) — выделенная директория `alphas/<type>/<id>/`; для трёх "semantic" (Hypothesis, Research Note, Postmortem) — wiki-primary в `wiki/claims/`, `wiki/sources/`, `wiki/experiments/`. Это разрешает ключевой конфликт R4 vs R5 vs R6.

4. **Модель D Nested Hierarchy финальна.** `life-os/` — root (вся жизнь Ruslan'а); `jetix/` — один из проектов Life-OS с полной 7-слойной архитектурой внутри; `shared/` — методологические компоненты (role-framework, Левенчук-онтология, writing-templates). Phase 1 (2026, solo): единый monorepo `~/jetix-os/` с тремя папками. Phase 2 (первый найм ~Q3-Q4 2026): `life-os/` выносится в отдельный private репо через `git filter-repo`. Phase 3 (5+ сотрудников или GDPR DPA): раздельные серверы. Asymmetric reference rule: Life-OS → Jetix разрешено, Jetix → Life-OS запрещено (GDPR-подготовка).

5. **L0 Executive Core = Ruslan (strategic-management) + AI-агенты + future humans через единую role-abstraction.** Сейчас ~12 ролей — иллюстративно, не константа; масштабируется до сотен. Career ladder J0–JX (Executor → Specialist → Senior → Lead/Staff → Principal → Strategic → Executive), decision-rights matrix, promotion signals, phase transitions — из R1 §G1-G7. C-suite триггеры — из R9 §A. Первый human hire — Sales Lead J3 (DACH Mittelstand требует Geschäftsführer-to-Geschäftsführer trust) на €300K ARR. Первый C-level — fractional CFO на €1M ARR или при Series A contemplation.

6. **DACH-context hard-coded.** German Mittelstand (50-500 employees, €10-500M revenue), Konsenskultur, IHK/VDMA networks, Betriebsrat/Mitbestimmung пороги, § 14 UStG Rechnungspflichtangaben, GoBD 2025 e-invoice archiving (10 лет ZUGFeRD 2.x), Art. 33 GDPR (72h breach notification), §19a EStG / Zukunftsfinanzierungsgesetz 2023 для equity. Не "generic AI consulting", а "Meisterklasse AI для серьёзного Mittelstand". Roland Berger + Simon-Kucher style, не McKinsey hype. Hourly billing запрещён — только value-based / fixed-price SKUs.

**Что изменилось vs v0.9 working-draft.** Synthesis существенно углубил L1 Foundation (конкретные tools: Promptfoo CLI + Langfuse self-hosted + SOPS+age + Coolify + Hetzner Storage Box + Uptime Kuma + Netdata — R2 §H2), L2 Cognitive (FPF-Lite полный draft 3-5 страниц — R3 §H.1), L3 Product (SKU-структура, productized consulting, не hourly), L4 Delivery (markdown CRM + event log + DuckDB projections — R5 §F.4), L5 Membrane (Alliance founding members после первого L4 клиента), L6 Topology (Mittelstand Benchmark dataset horizon), L7 Portfolio (Attention + Capital + Hours accounting). Добавил Career Ladder J0-JX (R1), Constitution §11 (R8), 14-day L1 rollout (R2 §H4), Phase 1→2→3 migration plan (R7 §E), 10 lint-правил для org-chart-in-git (R8 §E.1-E.2).

**Пять биggest conflicts resolved:**

- **C1. `alphas/` namespace — keep vs flatten.** R4 (knowledge arch) говорит keep `alphas/` как отдельный слой для operational state; R6 (folder structure) говорит flatten в `clients/`, `projects/`, `deals/`. Resolution: **keep alphas/ с nested structure per type** — `alphas/clients/<id>/{state.yaml, context.md, history.jsonl}`. Rationale: R6-критика ("лишний уровень вложенности") overriden R4-необходимостью separate operational state от semantic knowledge (wiki). Для 7 альф — Hybrid C (alpha + wiki entity ref); для 3 — wiki-primary (A); Invoice — YAML-only (B).

- **C2. Role-manifest format — 8 blocks (R3) vs simpler (R8).** R3 предлагает 8 блоков (identity/ontological/method/graph-of-creation/seniority/implementation-ai/implementation-human/evolution); R8 предлагает простую YAML-схему (id/layer/purpose/accountabilities/decision_rights/kpi). Resolution: **adopt R3 8-block format как canonical; R8 схема — lint-subset.** 8 блоков нужны для mega-corp aspiration; lint проверяет только subset обязательных полей. Это сохраняет R3 ontology (Левенчук 1:1) + R8 CI/CD validation.

- **C3. Event log — per-alpha history.jsonl (R4) vs monthly alpha-log (R5).** R4 предлагает `alphas/<type>/<id>/history.jsonl` (один log на alpha); R5 — `alpha-log/YYYY-MM.jsonl` (одно file на месяц на весь Jetix). Resolution: **both.** Per-alpha history.jsonl для read-локальности (агент работает с конкретным клиентом); monthly aggregate alpha-log через background projection (`scripts/project.py` собирает все события за месяц в один файл для GoBD audit и cross-entity analytics). Redundancy приемлема — hot write к per-alpha, cold aggregate к monthly.

- **C4. Life-OS separation — nested vs parallel vs submodule vs separate.** R7 финально фиксирует Модель D: **Phase 1 parallel folders в одном monorepo; Phase 2 separate repos (life-os-private); Phase 3 separate servers.** R6 подтверждает Phase 1 параллельные. Trigger для Phase 2: первый human hire или GDPR DPA enterprise клиент. Migration через `git filter-repo`, rollback-safe (bare clone + tag).

- **C5. SemVer для промптов — полные folders (R2) vs major-only (R6).** R2 предлагает `prompts/<agent>/vX.Y.Z/system.md` (полный SemVer в папках); R6 критикует folder explosion при 30+ агентах и 100+ версиях (3000+ папок). Resolution: **major-only folders + git tags для minor/patch** из R6 §D.2. `agents/<name>/v1/system.md`, `agents/<name>/v2/system.md`; git tag `agent-sales-lead-v2.1.3` для patch/minor. Сохраняет parallel A/B версии для major и git as version control для micro-изменений.

**Top 5 open questions для Ruslan:**

1. **Первый human hire timing.** Когда именно (какой ARR, какая метрика)? R1 предлагает €300K ARR; R9 — €300K-€1M; R7 — при GDPR DPA. Нужен твой judgment.
2. **C-suite slots в L0 на Day 1.** Резервируем ли сейчас role-manifests для COO/CFO/CSO/CMO/CTO (пустые, с expected-executor: null) или добавляем реактивно?
3. **Strategic-management роль Ruslan'а — декомпозиция.** Сейчас одна роль (strategy + framing + sales + acceptance + external). Описать как 5 sub-ролей с постепенной делегацией или держать монолитной?
4. **Banking + юрлицо timing.** Phase 1 Freiberufler / без Gewerbe или Gewerbeanmeldung + UG haftungsbeschränkt сейчас? Trigger?
5. **Promptfoo vs Langfuse vs DeepEval — какой primary?** R2 предлагает Promptfoo + Langfuse дуэт. Все self-hostable, free. Но нужно выбрать one как primary eval source.

**Что происходит после synthesis.** Stage 2 — multi-chat expert review через 5 параллельных chats (Critic / Simplifier / Mega-Corp Visionary / Левенчук Expert / Final Synthesizer). Каждый получит этот документ + Review Package из Part 5. Результаты сводятся в Stage 3 финальный pass. Stage 4-5 — написание D1-D9 чистовиков (9 decision-документов по T-02 template: JETIX-ARCHITECTURE-FINAL, JETIX-FOLDER-STRUCTURE, JETIX-ROLE-MANIFESTS, JETIX-VS-LIFE-OS, JETIX-KNOWLEDGE-ARCHITECTURE, JETIX-FPF-LITE, JETIX-CAREER-LEVELS, docs/INSTRUCTIONS, decisions/2026-04-20-jetix-architecture-final). Stage 6 — deploy: 14-day L1 Foundation rollout (R2 §H4) + migration existing 12 агентов в new structure.

---

## Part 1 — Unified Architecture Picture

### 1.1 Финальная архитектура в одной странице

```
┌─────────────────────────────────────────────────────────────────────┐
│                     Life-OS (root, Model D)                          │
│  ├── reflection/  daily-log/  health/  personal-goals/  relationships/│
│  └── projects/jetix/  ← ОДИН ИЗ ПРОЕКТОВ, но с полной 7-слойной арх. │
│                                                                       │
│  ╔═══════════════════════════════════════════════════════════════╗   │
│  ║                   Jetix (nested project)                       ║   │
│  ║                                                                 ║   │
│  ║  L0 Executive Core ═════ Ruslan + AI-агенты + future humans    ║   │
│  ║    через единую role-abstraction; J0–JX career ladder          ║   │
│  ║                                                                 ║   │
│  ║  L1 Foundation ═════ git + markdown + YAML + prompts-as-code   ║   │
│  ║    Promptfoo/Langfuse + Oxide RFD + SOPS+age + Coolify         ║   │
│  ║                                                                 ║   │
│  ║  L2 Cognitive ═════ Левенчук ШСМ (роль/альфа/граф/стратег./    ║   │
│  ║    мышление письмом) + FPF-Lite + 10 alphas + agent strategies ║   │
│  ║                                                                 ║   │
│  ║  L3 Product ═════ productized SKUs (Audit / Quick Win / Custom ║   │
│  ║    / Retainer) + future micro-SaaS + Jetix Club (post-L4)      ║   │
│  ║                                                                 ║   │
│  ║  L4 Delivery ═════ agency+consulting для DACH Mittelstand,     ║   │
│  ║    primary Q2 2026 revenue; markdown CRM + event log           ║   │
│  ║                                                                 ║   │
│  ║  L5 Membrane ═════ Alliance (founding members after 1st L4     ║   │
│  ║    client) + Newsletter + authority content + IHK/VDMA         ║   │
│  ║                                                                 ║   │
│  ║  L6 Topology ═════ 18-36мес horizon: Mittelstand Benchmark,    ║   │
│  ║    platform, multi-product                                      ║   │
│  ║                                                                 ║   │
│  ║  L7 Portfolio ═════ Capital + Hours + Attention accounting;    ║   │
│  ║    Phase 1 (own) → Phase 2 (team) → Phase 3 (ecosystem)        ║   │
│  ║                                                                 ║   │
│  ╚═══════════════════════════════════════════════════════════════╝   │
│                                                                       │
│  └── shared/ ═════ role-framework / Левенчук-онтология /             │
│       writing-templates / methodology-wiki (без данных)               │
└─────────────────────────────────────────────────────────────────────┘
```

Каждый слой — не изолированный кластер, а функция системы. L0 — "кто делает работу" (role-executor abstraction). L1 — "инфраструктура истины" (git + evals + observability). L2 — "как думаем" (ШСМ framing + acceptance = узкое место AI-эпохи). L3 — "что продаём" (productized SKUs). L4 — "как доставляем" (DACH Mittelstand delivery). L5 — "как тянется внимание" (community + content). L6 — "куда идём" (18-36 мес horizon). L7 — "как распределяем ресурсы" (capital + hours + attention).

### 1.2 Что изменилось vs v0.9 working-draft

| v0.9 | v1 (после synthesis) | Source |
|------|---------------------|--------|
| L0: "Ruslan + 12 агентов" | L0: "Executive Core" = Ruslan (strategic-management) + AI-агенты + future humans через единую role-abstraction; 12 иллюстративно | [R3 §F.7], [R9 §A.1] |
| L1: общие принципы | L1: конкретный tool stack (Promptfoo+Langfuse+SOPS+age+Coolify+Uptime Kuma+Netdata), 14-day rollout plan | [R2 §H.2, §H.4] |
| L2: Левенчук как руль | L2: FPF-Lite полный draft (3-5 стр.), 10 alphas с state machines, writing rituals (daily/weekly/quarterly), agent scope FPF (кто применяет что) | [R3 §H.1, §D, §E] |
| L3: "productized services" | L3: SKU structure template, 4 стартовых SKU (AI Audit / Quick Win / Custom / Retainer), hourly billing запрещён | [R5 §E.1] |
| L4: delivery | L4: markdown CRM (clients/{companies,contacts,deals,activities}/) + event log (alpha-log/*.jsonl) + DuckDB projections, пре-commit schema validation, ZUGFeRD 2.x для invoices | [R5 §A-F] |
| L7: "attention + capital + hours" | L7: Phase 1 (own) → Phase 2 (team + team's) → Phase 3 (ecosystem: клиенты, партнёры, сообщество) | [R9 §B.1 Berkshire, §B.2 Constellation] |
| 12 ролей как table | Career Ladder J0-JX + mapping текущих 12 на уровни + decision-rights matrix + promotion signals + phase transitions roadmap | [R1 §G.1-G.8] |
| Role-manifest kept abstract | Role-manifest spec: 8 блоков (identity/ontological/method/graph-of-creation/seniority/implementation-ai/implementation-human/evolution); example для sales-lead | [R3 §C.1-C.9] |
| Nested hierarchy конфирм | Model D Nested с 3-фазной миграцией (monorepo → separate repos → separate servers), asymmetric reference rule, shared/ папка | [R7 §A-J] |
| Notion IDs в CLAUDE.md | Notion = view layer; git = SoT; Notion MCP read-only | [R5 §A.3, anti-pattern] |

### 1.3 Phase evolution (Phase 1 → 2 → 3)

| Измерение | Phase 1 (2026, solo) | Phase 2a (€300K-€1M ARR) | Phase 2b (€2-10M, team 5-20) | Phase 3 (€50M+, mega-corp) |
|-----------|---------------------|-------------------------|------------------------------|----------------------------|
| **Executors** | 1 (Ruslan) + ~12 Claude-агентов | +1 human (Sales Lead J3) | +5-20 humans + 30+ agents | 50+ humans + 100+ agents |
| **L0 roles** | 1 Ruslan + 12 agent roles | +1 human Sales Lead | + Head of Finance, COO-like | C-suite full + Divisions |
| **Repos** | 1 monorepo (`~/jetix-os/`) | 2 repos (jetix + life-os-private) | 2+ repos, separate CI | Multi-repo federation |
| **Server** | 1 Hetzner CPX32 | 2 Hetzner (jetix-srv + personal) | Jetix enterprise EU cloud + personal separate | Multi-region, distributed |
| **Юрлицо** | Freiberufler или UG | UG haftungsbeschränkt | GmbH | Holdings BV + Ops GmbH (multi-entity) |
| **Board** | — | неформальный advisory (2-3) | Beirat (4-6) | Aufsichtsrat (formal DACH) |
| **Финансы** | Personal + Steuerberater | Fractional CFO €3-7K/mo | Head of Finance FTE €80-120K | Full-time CFO + team |
| **Regulatory** | — | <5 employees → nothing triggered | Betriebsrat-ready (5+), DPO if 20+ data processors | DrittelbG (500+), MitbestG (2000+) |
| **Revenue focus** | Q2 €50K (first L4 clients) | €300K-€1M (L4 agency) | €2-10M (L3+L4+L5 compound) | €50M+ (L6 platform + L7 portfolio) |
| **Alliance** | — | founding members после 1st client | 50-150 members, founding retainer | 500-1000+, open tier |

### 1.4 Ключевые принципы (top 10)

1. **Jetix ≠ one-person company.** AI-native mega-corporation с Day 1. Scale-up-first design: 10x рост капитала/часов/людей/проектов/ролей → система справляется без rebuild.
2. **Роль ≠ исполнитель.** Role-manifest — абстрактный контракт (целевая система + альфа + метод + acceptance). Executor (AI или human) подключается. Смена модели Claude 4.7 → 5 — меняется executor, не роль.
3. **Место-слот, не содержание.** Архитектура описывает слои как "места готовые принять наполнение". Не придумываем SKU/pricing/Club design заранее — наполняем итерационно.
4. **Nested hierarchy (Model D) финально.** Life-OS = root, Jetix = один из проектов с полной 7-слойной архитектурой. Полное разделение ресурсов (часы/деньги/внимание отдельно). Asymmetric reference rule: Life-OS→Jetix OK, Jetix→Life-OS запрещено.
5. **Capital + Hours + Attention.** L7 Portfolio трекает три ресурса (не только капитал, как Buffett/Leonard). Phase 1 (свои) → Phase 2 (+team's) → Phase 3 (+ecosystem: клиенты, партнёры, сообщество).
6. **Бизнес как кодовая база (Company-as-Code).** Все практики software industry переносим 1:1: Git = source of truth, SemVer для промптов, Oxide RFD для решений, blameless postmortems, error/hallucination budgets, CI/CD для prompts, Diátaxis для docs.
7. **5 примитивов ШСМ, selectively.** Роль (1:1), альфа (adapt), граф создания (adapt), стратегирование (invent = исключительно Ruslan), мышление письмом (adapt). FPF-Lite 3-5 стр., не full FPF. Узкое место AI-эпохи — framing и acceptance, не execution.
8. **10 core alphas.** Client, Project, Deal, Invoice, Content Item, Hypothesis, SKU, Member, Research Note, Postmortem — с state machines, acceptance criteria, event history.
9. **Org chart в Git, не в HR.** Flagship positioning (Thesis 5). Компания = software artefact. 8-блочный role-manifest YAML+Markdown, 10 lint-правил, Constitution §11 инварианты, decision-records как Oxide RFD.
10. **DACH hard-coded.** Немецкий Mittelstand, Konsenskultur, IHK/VDMA, Betriebsrat, § 14 UStG, GoBD 2025, GDPR Art. 33. Roland Berger/Simon-Kucher style > McKinsey. Hourly billing запрещён, value-based/fixed-price SKUs only. Shape Up > Scrum (2-6 недель bets).

---

## Part 2 — 9 Architecture Areas

### Area 1: Overall Philosophy (→ D1 JETIX-ARCHITECTURE-FINAL.md)

#### Unified Recommendation

**Jetix — это AI-native mega-corporation в форме software artefact.** Компания целиком (роли, процессы, решения, клиенты, финансы, org chart, интеллектуальная собственность) живёт в git-монорепо как версионированные markdown+YAML+JSONL файлы. Исполнитель работы — либо Ruslan (strategic-management role), либо AI-агент через Claude Code, либо (с Phase 2) human executor — все через единую role-abstraction. Целевой рынок — немецкий Mittelstand (50-500 employees, €10-500M revenue). Q2 2026 цель — €50K revenue через productized consulting L4 (AI Readiness Audit / Quick Win / Custom / Retainer). 7-слойная архитектура (L0 Executive Core + L1 Foundation + L2 Cognitive + L3 Product + L4 Delivery + L5 Membrane + L6 Topology + L7 Portfolio) спроектирована для 10x рoста без архитектурного rework; nested hierarchy внутри Life-OS (Model D) обеспечивает чистое разделение personal/business ресурсов; company-as-code принцип означает, что вся org introspectable через git (git blame = кто и когда принял decision, git history = institutional memory). Философский якорь — Левенчуковская онтология (роль, альфа, граф создания, стратегирование, мышление письмом) в L2; практический якорь — 10 core alphas с explicit state machines; операционный якорь — 8-блочный role-manifest как контракт между системой и любым executor.

#### Alternatives Considered

- **Alt A: Classic SaaS startup organization.** Notion + Slack + HubSpot + Pipedrive + GitHub для кода только. Rejected: не AI-native, не удерживает institutional memory в мире где knowledge workers уходят, нарушает company-as-code thesis, плохо подходит для Mittelstand Konsenskultur.
- **Alt B: Pure Left-Of-MBB consulting firm.** Классическая up-or-out лестница, hourly billing, partner-track. Rejected: Ruslan явно запретил hourly billing; требует 5-10 consultants для работы, не соответствует AI-native leverage (R9 §A.2 compressed C-suite через AI).
- **Alt C: Full Holacracy adoption.** [R8 §A.4] детально разобрал Holacracy Constitution v5.0. Rejected частично: Holacracy-inspired Role definition (Purpose + Domains + Accountabilities) принят; Governance Meetings + Tactical Meetings ceremonies — отвергнуты (overhead, не подходит для mostly-AI executors). Zappos кейс показал 18% turnover после adoption — Ruslan избегает Big Bang transformation.
- **Alt D: Pure Левенчук FPF full adoption.** Full интеллект-стек + 17 дисциплин + полная мереология холонов + advanced mereology Kit Fine. Rejected как overkill для Phase 1: FPF-Lite (3-5 стр.) достаточен; остальное read-only reference.

#### Rejected Options

- **Opt X (McKinsey hype positioning)** rejected потому что DACH Mittelstand не доверяет McKinsey-style consulting; Roland Berger + Simon-Kucher ближе по духу (operational, specialized, long-term relationships).
- **Opt Y (Speedrun к Series A)** rejected потому что AI-native mega-corp должна сначала доказать unit economics и product-market fit с DACH Mittelstand; инвесторы в Germany требуют Jahresabschluss + stability.

#### Rationale

1. **Leverage AI-native без early dilution** [R9 §A.2]: compressed C-suite через Claude-агентов позволяет оставаться в founder mode дольше (Paul Graham 2024); traditional SaaS требует VP-найма к €5M ARR, Jetix может держать solo-founder mode до €2-5M ARR.
2. **Mittelstand DACH = underserved premium market** [R1 §B.3, R9 Part D]: 215K Mittelstand компаний планируют Nachfolge до 2025 (KfW); конкуренты Big4/MBB игнорируют <€10M revenue сегмент; IHK/VDMA networks дают channel access.
3. **Company-as-Code как USP** [R8 Part J.11]: "организация как код" — продающий narrative для Mittelstand, уставшего от Notion/Confluence хаоса и SAP-сложности.
4. **Model D Nested** [R7 §E]: решает Company vs Life-OS раз и навсегда; готов к найму без архитектурного rework.
5. **10 core alphas** [R3 §D]: переводит Essence Kernel в B2B consulting контекст; даёт universal lifecycle tracking.

#### Trade-offs

- Высокая когнитивная нагрузка на Ruslan для поддержания всех слоёв синхронно (mitigated: meta-agent = immune system; weekly consolidation).
- Риск over-engineering (mitigated: Levenchuk principle "minimum viable spec", FPF-Lite не Full FPF, lint > manual review).
- Зависимость от Claude Code infrastructure (mitigated: role-manifests portable; exit strategy к любой LLM через standardized YAML contracts).
- DACH positioning ограничивает TAM (mitigated: интенциональный trade-off — premium narrow market > global commodity).

#### Open Questions for Ruslan

- **Q1:** Cross-слой governance: L0 strategic-management роль Ruslan'а должна быть описана как 1 monolithic manifest или декомпозирована на 5 sub-roles (strategy / framing / sales / acceptance / external) с разными delegation plans?
- **Q2:** Exit strategy (10-year horizon): остаёмся private DACH-focused или publishing framework (MIT + CC BY-SA из R8 §J.6) после v1.0.0?

#### Implementation Pointer

D1 JETIX-ARCHITECTURE-FINAL.md = T-02 template, 12-15 страниц. Sections: Context / Decision (7-слойная архитектура финализирована, Model D, role-abstraction, company-as-code, 10 alphas) / Consequences / Alternatives / Migration / Review triggers. Link-backs ко всем остальным D2-D9 чистовикам.

---

### Area 2: Folder Structure (→ D2 JETIX-FOLDER-STRUCTURE.md)

#### Unified Recommendation

Финальная структура монорепо `~/jetix-os/` синтезирует R2 §H.1 + R6 §J.1 + R7 §Part J + R4 §H.1 + R8 §J.2:

```
~/jetix-os/                               # Root monorepo (Phase 1)
│
├── life-os/                              # L-1 Root (Model D: вся жизнь Ruslan'а)
│   ├── daily-log/{YYYY}/                 # Year subfolders (D7)
│   ├── reflection/                       # Личные рефлексии
│   ├── health/                           # Медицинские (GDPR special categories)
│   ├── relationships/                    # Личные контакты
│   ├── personal-goals/                   # Не Jetix цели
│   ├── decisions/                        # Личные ADRs
│   ├── okrs/                             # Личные OKRs
│   ├── letters/                          # Личная переписка
│   └── wiki/                             # Личное knowledge (отдельно от business!)
│
├── jetix/                                # Компания Jetix (L0-L7)
│   ├── CONSTITUTION.md                   # §11 инварианты (AI не редактирует)
│   ├── CLAUDE.md                         # Master schema для всех агентов (wiki)
│   ├── README.md
│   │
│   ├── roles/                            # R3 8-block manifests (D1 из R6: combined)
│   │   ├── schema/role-manifest.schema.yaml
│   │   ├── l0-executive/
│   │   │   └── strategic-management/role.md   # Ruslan's role
│   │   ├── l1-foundation/
│   │   │   └── chief-of-staff/role.md
│   │   ├── l2-cognitive/
│   │   │   └── strategist/role.md
│   │   ├── l3-product/
│   │   │   └── sales-lead/role.md
│   │   ├── l4-delivery/
│   │   │   ├── delivery/role.md
│   │   │   └── analyst/role.md
│   │   ├── l5-membrane/
│   │   │   └── community-lead/role.md
│   │   ├── l6-topology/
│   │   │   └── platform-lead/role.md     # Future slot
│   │   ├── l7-portfolio/
│   │   │   └── portfolio-manager/role.md
│   │   └── archive/                      # Deprecated roles (не удаляются)
│   │
│   ├── executors/                        # Holacracy decouple: role ≠ executor
│   │   ├── ruslan.yaml                   # Ruslan как executor strategic-management
│   │   ├── claude-sales-lead.yaml        # Claude Opus как executor sales-lead
│   │   ├── claude-delivery.yaml
│   │   └── ...
│   │
│   ├── agents/                           # Claude Code per-agent memory (R4 5-layer)
│   │   └── <agent-id>/
│   │       ├── system.md                 # Core identity, pointer to role
│   │       ├── strategies.md             # Meta-cognitive (system prompt learning)
│   │       ├── scratchpad.md             # Working memory (ephemeral)
│   │       ├── niche/ → ../../wiki/niches/<niche>/   # Symlinks
│   │       └── v1/system.md, v2/system.md  # Major versions (R6 D2)
│   │
│   ├── alphas/                           # Operational state machines (keep — R4)
│   │   ├── clients/<id>/
│   │   │   ├── state.yaml                # Current state
│   │   │   ├── context.md                # Rich context for agents
│   │   │   ├── history.jsonl             # Append-only events (per-alpha)
│   │   │   └── gdpr-deletion-log.yaml    # GDPR retention dates
│   │   ├── projects/<id>/ (same)
│   │   ├── deals/<id>/ (same)
│   │   ├── invoices/YYYY/R-YYYY-NNNN.yaml  # Sequential Rechnungsnummer
│   │   ├── content/<id>/ (same)
│   │   ├── members/<id>/ (same)
│   │   └── skus/<sku>.yaml               # Stable, YAML-only
│   │
│   ├── alpha-log/                        # Aggregated monthly (R5)
│   │   └── YYYY-MM.jsonl                 # Cross-alpha event projection
│   │
│   ├── clients/                          # Markdown CRM (R5)
│   │   ├── companies/<slug>.md           # Entity notes with frontmatter
│   │   ├── contacts/<slug>.md
│   │   ├── leads/<slug>.md
│   │   ├── deals/YYYY-MM-DD-<slug>.md
│   │   ├── activities/YYYY-MM-DD-<slug>.md
│   │   ├── contracts/{drafts,signed}/
│   │   ├── invoices/YYYY/R-YYYY-NNNN.md  # Rendered for PDF + ZUGFeRD
│   │   └── _archive/YYYY/                # Within-zone archiving
│   │
│   ├── wiki/                             # Karpathy LLM Wiki (R4) — business KB
│   │   ├── CLAUDE.md                     # Wiki schema
│   │   ├── index.md
│   │   ├── log.md                        # Append-only chronology
│   │   ├── graph/edges.jsonl             # Typed edges (9 types)
│   │   ├── concepts/{personal,business,sales,life,tech,meta}/
│   │   ├── entities/                     # Wiki-side entity refs (alpha-ref)
│   │   ├── sources/                      # Research Notes (alpha wiki-primary)
│   │   ├── claims/                       # Hypotheses (alpha wiki-primary)
│   │   ├── experiments/                  # Postmortems (alpha wiki-primary)
│   │   ├── topics/, ideas/, summaries/, foundations/
│   │   ├── comparisons/                  # /ask writeback
│   │   ├── niches/                       # 6 срезов per agent niche
│   │   └── _templates/
│   │
│   ├── decisions/                        # Oxide-style RFDs (D4 flat)
│   │   ├── schema/decision.schema.yaml
│   │   ├── template.md
│   │   ├── 0001-jetix-architecture-final.md
│   │   └── ...
│   │
│   ├── postmortems/                      # Separate жанр
│   │   └── YYYY-MM-DD-<slug>.md
│   │
│   ├── strategizing/                     # Левенчуковские стратегирование-доки
│   │   └── YYYY-MM-DD-<slug>.md
│   │
│   ├── weekly/{YYYY-Wnn}.md              # Shape Up weekly reviews
│   ├── letters/{YYYY-Qn}.md              # Quarterly letters (Berkshire-style)
│   ├── okrs/{YYYY-Qn}.md                 # Quarterly OKRs in Git
│   │
│   ├── policy/                           # Constitution layer
│   │   ├── constitution.md, decision-rights.md, hiring.md,
│   │   ├── ai-governance.md, gdpr.md
│   │
│   ├── processes/                        # Process docs (Diátaxis: tutorials)
│   ├── evals/                            # Promptfoo golden datasets
│   │   └── <agent>/golden.jsonl
│   │
│   ├── docs/                             # Diátaxis 4-forms (Ruslan + public)
│   │   ├── tutorials/, how-to/, reference/, explanation/
│   │
│   ├── templates/                        # Top-level shared (D8)
│   │   └── client-brief.md, proposal.md, sow.md, adr.md, postmortem.md,
│   │       role-manifest.md, ...
│   │
│   ├── products/                         # L3 Product layer (future SaaS)
│   ├── comms/mailboxes/<agent>.jsonl     # Agent mailboxes (recall memory)
│   ├── state/                            # Aggregated JSONL state for DuckDB
│   │   └── clients.jsonl, deals.jsonl, ...
│   │
│   ├── sales/                            # Sales projections (auto-generated)
│   │   ├── pipeline.md, dashboard.md, playbooks/
│   │   └── reports/YYYY-Www.md
│   ├── finance/                          # Finance projections
│   │   ├── ledger.md, reports/, datev/YYYY-MM.csv
│   │   └── next-invoice-number.txt
│   │
│   └── secrets/ → ../secrets/            # Symlink to root secrets/
│
├── shared/                               # R7 Part C: методологический слой
│   ├── role-framework/                   # Role-manifest schema generator
│   ├── levenchuk-ontology/               # ШСМ read-only references
│   ├── writing-templates/                # Generic templates (format only)
│   └── methodology-wiki/                 # Процессы без данных
│
├── .claude/                              # Claude Code config
│   ├── agents/                           # Sub-agent definitions (project-level)
│   ├── commands/                         # /slash-commands
│   ├── skills/                           # Complex multi-file skills
│   └── settings.json
│
├── infra/                                # IaC
│   ├── terraform/main.tf                 # Hetzner provisioning
│   ├── docker-compose.yml                # Langfuse, Coolify
│   ├── systemd/                          # Service units
│   └── coolify/
│
├── secrets/                              # SOPS+age encrypted (2 keys: jetix + life)
│   ├── .sops.yaml
│   └── *.enc.yaml
│
├── tools/                                # Python pipelines
│   ├── transcribe.py, extract.py, filter.py, review_report.py
│
├── scripts/                              # Bash utilities
│   ├── backup.sh, project.py, datev-export.py
│
├── .github/workflows/                    # CI
│   ├── eval.yml                          # Promptfoo on prompt changes
│   ├── docs.yml                          # Vale + markdownlint + lychee
│   ├── structure-check.yml, org-ci.yml   # Lint + schema validation
│   ├── cost-check.yml                    # Weekly token budget
│
├── .sops.yaml, .vale.ini, .pre-commit-config.yaml
├── justfile                              # Task runner (not Make)
├── promptfooconfig.yaml
└── README.md
```

**Phase 2 migration:** `life-os/` → отдельный private репо через `git filter-repo` [R7 §E]; `jetix/` остаётся; `shared/` можно либо в каждом, либо как отдельный public репо.

#### Alternatives Considered
- **Alt A: flatten `alphas/` в `clients/`, `projects/`, `deals/`** (R6 §D3): rejected — R4 argued keeping `alphas/` separate для operational state vs `wiki/` semantic knowledge, и markdown CRM layer в `clients/` уже даёт flatness для daily work.
- **Alt B: combined `roles/<name>/{manifest.md, executor.yaml}`** (R6 §D1 Alt 1): partially adopted — `roles/` содержит role-manifests, `executors/` остаётся separate для Holacracy decoupling и privacy (GDPR).
- **Alt C: full SemVer folders для prompts** (R2 draft): rejected — folder explosion. Adopted: major-only folders + git tags.

#### Rejected Options
- **Opt X: Johnny.Decimal numbering** (R6 §Part B): rejected — ломается на >1000 clients.
- **Opt Y: Git submodule для life-os в Phase 1**: rejected — известный DX tax, Phase 2 trigger.
- **Opt Z: Notion как primary**: rejected — API rate limits, UUID opacity, export fidelity (R5 §A.3).

#### Rationale
1. [R6 §J.1] stress-tested R2 draft и нашла 10 D-решений.
2. [R4 §H.1] требует separate `alphas/` для Hybrid C storage pattern.
3. [R7 §E] требует Model D: 3 folders + migration path.
4. [R8 §C.6] требует `policy/` + `decisions/` + `CONSTITUTION.md` для org-in-git.
5. [R5 §B.1-B.5] требует CRM schema в `clients/{companies,contacts,deals,activities}/`.

#### Trade-offs
- Сложность структуры vs clarity trade-off: 20+ top-level folders в `jetix/` требуют README.md в каждом, но это норма для mega-corp aspiration.
- Redundancy `alphas/` + `clients/` vs single layer: редундантность приемлема, разные concerns (state vs entity-notes).

#### Open Questions for Ruslan
- **Q1:** `life-os/wiki/` + `jetix/wiki/` отдельны или shared root `wiki/` с `area:` tag? R6 §D6 рекомендует separate. Soft vote для separate.
- **Q2:** `shared/` как top-level или внутри `jetix/`? R7 советует top-level.

#### Implementation Pointer
D2 JETIX-FOLDER-STRUCTURE.md = полное дерево + namespaced conventions (kebab-case D10) + scale-up triggers (R6 §J.3, R7 §Part E) + migration script (R7 §E for filter-repo).

---

### Area 3: Role Manifests (→ D3 JETIX-ROLE-MANIFESTS.md)

#### Unified Recommendation

Role-manifest — **8-блочный YAML frontmatter + Markdown body** в `roles/<slug>/role.md`, синтез R3 §C + R8 §C.2 + R1 §G.2:

```yaml
---
# Block 1 — Identity
identity:
  name: sales-lead
  display-name: "Sales Lead"
  version: "1.2.0"        # SemVer для роли
  layer: L3
  family: sales
  status: active           # draft | active | deprecated
  created: 2026-04-19
  updated: 2026-04-19

# Block 2 — Ontological (Левенчук/Holacracy синтез)
ontological:
  purpose: >
    Генерировать квалифицированный pipeline немецких Mittelstand-клиентов
    и конвертировать его в подписанные контракты ≥€50K в Q2 2026.
  target-system: "client-pipeline"
  primary-alpha: client
  secondary-alphas: [deal, invoice]
  domains:                 # Что роль контролирует эксклюзивно
    - CRM (clients/)
    - Pricing authority (до €25K)
  accountabilities:        # Ongoing activities
    - id: acc-001
      description: "Генерировать ≥20 qualified leads в неделю"
      alpha: opportunity
  out_of_scope:            # Явные НЕ-accountabilities
    - Outreach-сообщения (→ sales-outreach)
    - Подписание контрактов (→ strategic-management)
  acceptance-criteria:
    - "Client.qualified: ICP score ≥ 70"

# Block 3 — Method (Epistemology)
method:
  primary_frameworks:
    - name: MECE hypothesis-driven segmentation
    - name: SPIN Selling / Challenger Sale
  thinking_protocol:       # Обязательные шаги
    - "Прочитай все открытые deals"
    - "Применяй MECE: каждый deal — в одну стадию"
  quality_criteria:
    - "Pipeline обновлён (все deals с next action ≤7 дней)"
  anti_patterns:
    - "Proposal без champion"
    - "Verbal price без written quote"
  golden_examples:         # Few-shot refs
    - evals/sales-lead/golden.jsonl

# Block 4 — Graph of Creation
graph_of_creation:
  produces:
    - artifact: pipeline-report
      consumers: [chief-of-staff, strategic-management]
    - artifact: proposal
      consumers: [client, delivery]
  consumes:
    - artifact: qualified-contact
      produced_by: sales-research
      required: true

# Block 5 — Seniority / Scale (R1 Career Ladder)
seniority:
  current_level: J3        # J0 | J1 | J2 | J3 | J4 | J5 | JX
  decision-rights:
    autonomous: [
      "Qualify/disqualify lead (ICP < 40)",
      "Discount до 10%",
      "Standard proposal (list price)",
    ]
    advisory: [
      "Discount 10-20% → chief-of-staff",
      "Contract terms нестандартные",
    ]
    veto: [
      "Commit to delivery timeline без согласования с delivery",
    ]
    never: ["Sign contracts", "Change pricing floor"]
  escalation-trigger:
    - condition: "Deal > €40K"
      escalate-to: strategic-management
    - condition: "Discount > 10%"
      escalate-to: chief-of-staff
  split_trigger:           # Когда роль делится
    conditions: ["active-deals > 30", "2+ FTE needed concurrently"]
    split_into: [sales-strategy, sales-execution, account-management]

# Block 6 — Implementation AI
implementation_ai:
  agent_type: claude-code
  current-executor: "claude-opus-4-7"
  prompt-file: "agents/sales-lead/v1/system.md"
  eval-dataset: "evals/sales-lead/golden.jsonl"
  eval-passing-threshold: 0.85
  tools-allowed:
    mcp-tools: [{name: filesystem, scope: "clients/, templates/"}]
    forbidden-tools: [email-send, git-push]
  context-window-budget: 180000
  memory-strategy: "rolling-summary + pinned-client-context"

# Block 7 — Implementation Human (Future team)
implementation_human:
  hired-person: null       # null = AI only; person-slug при найме
  onboarding-path:
    - "Изучить role.md + golden examples (2 дня)"
    - "Shadow AI на 10 сделках (1 неделя)"
    - "Co-pilot mode: подтверждение решений (2 недели)"
    - "Autonomous mode с weekly review"
  reporting-to: chief-of-staff
  performance-kpis:
    - {metric: "Qualified leads/week", target: ">=20", cadence: weekly}
    - {metric: "Lead->closed-won conversion", target: ">25%", cadence: monthly}
    - {metric: "Avg deal cycle time", target: "<30 days", cadence: monthly}
  handoff_from_ai:
    triggers: ["Deal >€50K live pitch", "Client requests human call"]

# Block 8 — Evolution
evolution:
  last_review: "2026-07-01"
  changelog:
    - version: "1.2.0"
      date: "2026-04-19"
      change: "Added J3 seniority + explicit escalation triggers"
  expected-evolution:
    - "Q3 2026: first human hire, co-pilot mode"
    - "2027: split SMB/Enterprise при >50 deals"
---

# Sales Lead — System Prompt

## Purpose
Максимизировать conversion от qualified lead до closed-won...

## Method
1. Читай открытые deals и обновления
2. Применяй MECE к каждому deal
3. ...
```

#### Alternatives Considered
- **Alt A: Simple 5-field schema (R8 simplified):** rejected — mega-corp readiness требует seniority + decision-rights + implementation human/AI блоков для Phase 2.
- **Alt B: Pure YAML (`manifest.yaml` без prose):** rejected — нет места для system prompt, которым Claude фактически пользуется [R3 §C.0].
- **Alt C: Dual file (`manifest.yaml` + `system.md`):** rejected — sync overhead, синхронизация ломается.

#### Rejected Options
- **Opt X: Holacracy-full constitutional definition per role:** rejected — overkill для Phase 1.
- **Opt Y: Separate `implementation.md` + `contract.md`:** rejected — fragmentation.

#### Rationale
1. [R3 §C.1-C.9] дал academically-grounded 8-block spec.
2. [R8 §C.2-C.4] дал JSON Schema для CI validation.
3. [R1 §G.1-G.2] дал Career Ladder J0-JX для `seniority` блока.
4. Единый файл = minimum friction для solo founder + AI-агенты читают целиком.

#### Trade-offs
- 8 блоков vs minimum viable: adopted full 8 для future-proof, но `minimum viable manifest` = Blocks 1, 2, 4, 6 (остальные optional) для bootstrap.
- Synchronization между Block 1 version и git tags: manual discipline, не automated.

#### Open Questions for Ruslan
- **Q1:** Семейство ролей (`family:` field): L-слой или functional (sales/delivery/intelligence/ops)? Сейчас — functional.
- **Q2:** `current-executor` поле обновляется каждый PR или на SemVer bumps? Рекомендация: PATCH bump при смене executor.

#### Implementation Pointer
D3 JETIX-ROLE-MANIFESTS.md = template + JSON Schema + 14 filled examples (migration plan из R3 §H.5: manager → meta-agent → strategist → sales-lead → delivery → analyst → knowledge-synth → sales-research → sales-outreach → strategic-management → inbox-processor → personal-assistant → crazy-agent → system-admin, 33-47 часов work).

---

### Area 4: Life-OS Separation (→ D4 JETIX-VS-LIFE-OS.md)

#### Unified Recommendation

**Model D Nested Hierarchy финально** [R7 §E]. Life-OS = root (вся жизнь Ruslan'а); Jetix = один из проектов с полной 7-слойной архитектурой; shared/ = методологический слой без данных. Three phases:

**Phase 1 (2026, solo, сейчас → €50K-€300K):** Monorepo `~/jetix-os/` с тремя folders (`life-os/`, `jetix/`, `shared/`). SOPS+age с **двумя ключами** (`age-life.pub`, `age-jetix.pub`) в одном `.sops.yaml`. Toggl один workspace, tags `jetix:*` / `life:*` для time tracking. Личный банковский счёт (DKB/N26) с категоризацией jetix:* / life:*. Asymmetric reference rule enforced: Life-OS markdown может ссылаться на `[[jetix/...]]`, Jetix markdown запрещён ссылаться на `life-os/` (pre-commit hook validation).

**Phase 2 (первый human hire OR GDPR DPA enterprise клиент, ~Q3-Q4 2026):** `git filter-repo` extracts `life-os/` history → `github.com/ruslan/life-os-private` (private). `~/jetix-os/` remains (теперь без `life-os/`). `shared/` либо в каждом, либо как public third repo `github.com/jetix/shared-methodology`. SOPS раздельные ключи в каждом репо. Toggl два workspaces (Personal + Jetix team). Гражданско-правовой переход — UG haftungsbeschränkt регистрация, Gewerbeanmeldung, Geschäftskonto (business account) — e.g., Commerzbank или Penta.

**Phase 3 (5+ сотрудников OR funding OR Series A contemplation, 2028+):** Отдельные серверы. Jetix — enterprise EU cloud (Hetzner с dedicated VPS или AWS Frankfurt); Life-OS — personal server или home NAS или separate cheap VPS. Раздельные DNS, раздельные identity providers, раздельные backup regimes. UG → GmbH conversion (€25K минимальный капитал).

**Rollback protection:** перед каждой миграцией — git tag (`pre-phase2-migration-YYYYMMDD`) + bare clone backup. Migration scripts idempotent.

#### Alternatives Considered
- **Alt A: Option 1 — полностью вложенный `~/jetix-os/life-os/` + `~/jetix-os/jetix/`:** rejected — privacy слабая при найме.
- **Alt B: Option 3 — git submodule с Day 1:** rejected — submodule hell, premature optimization.
- **Alt C: Option 4 — separate repos с Day 1:** rejected — overhead без benefit для solo.

#### Rejected Options
- **Opt X: Notion-based separation (два Notion account):** rejected — не company-as-code.
- **Opt Y: Obsidian vault separation:** accepted для note-taking layer, но не для infrastructure.

#### Rationale
1. [R7 §A] PKM patterns (PARA, PPV, Ultimate Brain) недостаточны для команды + GDPR.
2. [R7 §B.1-B.7] infrastructure patterns: monorepo-with-folders оптимален для solo; separate repos для team.
3. [R7 §D] asymmetric reference rule критичен для role-ontology cleanness (Ruslan-as-founder роль не должна знать Ruslan-as-person детали).
4. Phase 2 trigger == first human hire — точно когда privacy требуется GDPR-wise.

#### Trade-offs
- Migration overhead в Phase 2 (~1 день): mitigated — filter-repo + tags.
- Cross-references Life-OS → Jetix ломаются при extract: mitigated — в Life-OS ссылки становятся external GitHub URLs, не broken.

#### Open Questions for Ruslan
- **Q1:** `shared/` в Phase 2 — в каждом из двух репо duplicated или separate third public репо?
- **Q2:** Personal banking vs Geschäftskonto в Phase 1 — держать personal до Gewerbe или уже сейчас открывать business account?

#### Implementation Pointer
D4 JETIX-VS-LIFE-OS.md = Model D spec + 3-phase migration table + asymmetric reference rule + grey zone classification (learning notes / network / creative ideas / reflection about fatigue из R7 §C) + insight flow sanitization pattern (R7 §D) + filter-repo script + GDPR Phase 2 checklist.

---

### Area 5: Knowledge Architecture (→ D5 JETIX-KNOWLEDGE-ARCHITECTURE.md)

#### Unified Recommendation

Three-layer Karpathy LLM Wiki + 10 Alphas + Per-agent 5-layer memory, синтез R4 + R5:

**Layer 1: wiki/** (Karpathy pattern, 557 current pages → 5000+ projected).
- 9 entity types: concepts / entities / sources / topics / ideas / experiments / claims / summaries / foundations.
- 6 niches per agent: personal / business / sales / life / tech / meta — symlinks в `agents/<id>/niche/`.
- `wiki/graph/edges.jsonl` — 9 typed edges (supports, based-on, consumes, produces, derives-from, contradicts, refines, archived-by, alpha-ref).
- HippoRAG PPR retrieval (current Jetix engine) + alpha-aware filtering.
- Skills: `/ingest`, `/ask` (writeback to `wiki/comparisons/`), `/lint`, `/consolidate`, `/build-graph`.

**Layer 2: alphas/** (operational state, 6 types — Hybrid C из R4).
- `alphas/clients/<id>/{state.yaml, context.md, history.jsonl}`.
- `alphas/projects/<id>/, alphas/deals/<id>/, alphas/content/<id>/, alphas/members/<id>/` — same pattern.
- `alphas/invoices/YYYY/R-YYYY-NNNN.yaml` — YAML-only (no state machine after issuance).
- `alphas/skus/<sku>.yaml` — YAML-only, stable.
- Wiki-primary для 3 alphas: Hypothesis → `wiki/claims/<slug>.md`, Research Note → `wiki/sources/<slug>.md`, Postmortem → `wiki/experiments/<slug>.md`.

**Layer 3: Per-agent memory (5 layers, R4 §C.2):**
- `agents/<id>/system.md` — Core identity (Procedural, 2KB budget).
- `agents/<id>/strategies.md` — Meta-cognitive, System Prompt Learning (1.5KB budget).
- `agents/<id>/scratchpad.md` — Working memory (ephemeral, ~8KB budget).
- `agents/<id>/niche/` → `wiki/niches/<niche>/` symlinks.
- `comms/mailboxes/<id>.jsonl` — Recall (inter-agent, 2KB budget).

**Context loading budget (50K tokens per session, R4 §H.3):**
- Core identity (system.md): 2K
- Strategies: 1.5K
- Task + alpha state: 5K
- HippoRAG retrieval (top-20): 20K
- Recent decisions (30d): 3K
- Mailbox (last 10): 2K
- Scratchpad: 8K
- Overhead: 3.5K
- Total: ~50K (25% of Opus 4.7 200K window at auto-compact threshold).

**Writeback rules (R4 §H.4):** `/ask` novel comparisons → `wiki/comparisons/`; alpha state changes → `history.jsonl`; new patterns detected → `wiki/claims/`; `/consolidate` weekly → `wiki/topics/`; postmortems → `wiki/experiments/`.

**CRM-specific (R5):** markdown CRM в `clients/{companies, contacts, leads, deals, activities, contracts, invoices}/` + `alpha-log/YYYY-MM.jsonl` (projected from per-alpha `history.jsonl` для GoBD audit) + DuckDB projections (`sales/pipeline.md`, `sales/reports/YYYY-Www.md`, `finance/ledger.md`).

**German legal compliance (R5 §E):**
- Invoice YAML schema в `clients/invoices/YYYY/R-YYYY-NNNN.md` (11 Pflichtangaben § 14 UStG).
- ZUGFeRD 2.x (PDF/A-3 с embedded XML) для e-invoicing GoBD 2025.
- Sequential Rechnungsnummer через `finance/next-invoice-number.txt` + pre-commit monotonicity check.
- `_gdpr-deletion-log.yaml` per-client с retention dates (10 years HGB/AO; 6 years commercial correspondence).

#### Alternatives Considered
- **Alt A: Pure GraphRAG (Microsoft 2024):** deferred — overkill для 557 pages; trigger at 5000+ pages.
- **Alt B: Vector DB (Qdrant/Chroma) primary:** rejected — HippoRAG outperforms dense retrieval на multi-hop без embeddings [R4 §A.3].
- **Alt C: Dense + sparse hybrid (BM25 + embeddings):** deferred — BM25 fallback при PPR score < threshold; full hybrid at 10K+ pages.
- **Alt D: Monthly alpha-log (R5) only, no per-alpha history.jsonl:** rejected — hurts read-locality (agent фокусируется на одном клиенте).
- **Alt E: Per-alpha history.jsonl only, no monthly aggregate:** rejected — hurts GoBD audit + cross-entity analytics.

#### Rejected Options
- **Opt X: Notion as primary KB:** rejected — R5 §A.3 anti-pattern.
- **Opt Y: SQL database для alphas:** deferred to Phase 2b (20+ employees), Hybrid C sufficient до этого.

#### Rationale
1. [R4 §A.1] Karpathy pattern доказан на Jetix scale (557 pages).
2. [R4 §D.1-D.2] Hybrid C решает operational vs semantic split.
3. [R5 §C.2] event sourcing + snapshot гибрид даёт GoBD audit trail.
4. [R5 §E.3-E.7] German legal requirements (§ 14 UStG, GoBD 2025) hardcoded в schema.

#### Trade-offs
- Redundancy: per-alpha history.jsonl + monthly alpha-log — дубликация event data, но разные read patterns.
- Per-agent memory 5 layers — когнитивная нагрузка на дизайн system.md/strategies.md split; mitigated via template.

#### Open Questions for Ruslan
- **Q1:** `wiki/comparisons/` automatic writeback — по novelty-threshold (LLM decides) или manual approval? Soft vote: novelty-threshold с weekly human review.
- **Q2:** Scale trigger для GraphRAG — 5000 pages firm или revisit?

#### Implementation Pointer
D5 JETIX-KNOWLEDGE-ARCHITECTURE.md = detailed folder spec + state machine diagrams per alpha + writeback rules table + context loading pseudo-code + HippoRAG retrieval pipeline + German legal invoice schema (full).

---

### Area 6: FPF-Lite (→ D6 JETIX-FPF-LITE.md)

#### Unified Recommendation

FPF-Lite = **3-5 страниц operational spec** синтезирован из R3 §H.1. Не full FPF (17 дисциплин, full mereology). Sections:

1. **Target System** — что Jetix создаёт (AI-native delivery: превращение бизнес-проблемы в actionable решение, scalable без rebuild).
2. **Stakeholders** — Ruslan, клиенты, AI-агенты, future human executors, Alliance members, future investors, регуляторы (EU AI Act, GDPR), tech partners (Anthropic, GitHub).
3. **Creation Graph** (Mermaid diagram) — sales-research → sales-lead → delivery → analyst → knowledge-synth → strategist → client.
4. **Client Principles** — Deliverable определён до начала; MECE structure каждого output; Predictable cadence; One point of contact (Phase 1); Feedback loop structured не NPS; Scope creep = новый контракт.
5. **Internal Principles (Ruslan ↔ agents ↔ executors)** — Role ≠ executor; Context is king; Artifacts over conversations; meta-agent как immune system; Explicit alpha state transitions; No role left undefined; Writing as thinking.
6. **Critical Alphas (10)** — Client / Project / Deal / Invoice / Content Item / Hypothesis / SKU / Member / Research Note / Postmortem — с states.
7. **Ritual Cadence** — Daily (inbox triage, pipeline review, agent grading), Weekly (manager review), Monthly (strategizing, QA audit, founder letter), Quarterly (OKR review, quarterly letter, role-manifest review).
8. **U-Types Lite (4-6)** — U.System, U.Role, U.Method, U.Stakeholder. Минимальный upper ontology.

**What's excluded (overkill для Phase 1):** Полная иерархия холонов; 17 trans-disciplines; advanced mereology (Kit Fine); category theory formalization; constructor theory; Architectural invariants of full FPF.

#### Alternatives Considered
- **Alt A: Full FPF adoption:** rejected — overkill, see Part B.7 из R3.
- **Alt B: No formal FPF, just CLAUDE.md rules:** rejected — mega-corp aspiration требует formal ontology.

#### Rejected Options
- **Opt X: Holacracy Constitution instead:** rejected — слишком ceremonial для AI-executors; ШСМ-based больше подходит AI-native.

#### Rationale
1. [R3 §B.7] explicit включение/исключение per component.
2. [R3 §F.7] 5 примитивов Левенчука: роль 1:1, альфа adapt, граф adapt, стратегирование invent, мышление письмом adapt.
3. FPF-Lite — "big system prompt" для всех агентов (Левенчук, ailev 1769890).

#### Trade-offs
- Overhead maintaining FPF-Lite current vs value of formal ontology: mitigated — quarterly review + meta-agent consistency check.

#### Open Questions for Ruslan
- **Q1:** FPF-Lite публикуется (publicly visible, Phase 3+) или internal forever?

#### Implementation Pointer
D6 JETIX-FPF-LITE.md = 3-5 pages из R3 §H.1 (copy-paste starting point) + tuning к Jetix-specific content.

---

### Area 7: Career Levels + Scale-up (→ D7 JETIX-CAREER-LEVELS.md)

#### Unified Recommendation

**7-level ladder (J0-JX)** из R1 §G.1:

| Level | Jetix | Scope | Decision-rights | Horizon | Current mapping |
|-------|-------|-------|-----------------|---------|-----------------|
| J0 | Executor | Точно определённая задача | Execute only | <1 день | — |
| J1 | Specialist | Компонент, функция | Метод в границах | 1-7 дней | inbox-processor, personal-assistant, sales-research, sales-outreach |
| J2 | Senior Specialist | Feature, workflow | Technical approach | 1-4 недели | system-admin, delivery, analyst |
| J3 | Lead (Staff) | Домен, несколько ролей | Domain architecture | 1-3 месяца | sales-lead, meta-agent, manager, crazy-agent, life-coach |
| J4 | Principal | Business function | Business decisions в функции | 3-12 месяцев | strategist |
| J5 | Strategic | Вся компания | Company-level strategy | 1-3 года | strategic-management (Ruslan) |
| JX | Executive (C-level) | Компания + экосистема | Irreversible decisions | 3-10 лет | strategic-management (Ruslan, dual) |

**Decision-rights matrix** (R1 §G.3) — 13 decision types × 6 levels + escalation thresholds (€-based).

**Phase transitions (R1 §G.4 + R9 §K):**
- **Phase 0 (now → Q2 2026):** 1 Ruslan (J5+JX) + 12 agent roles (J1-J4). Target €50K. Trigger to Phase 1: €30K/mo stable 2 months OR Ruslan >30% time в J2-tasks.
- **Phase 1 (Q3-Q4 2026 → €300K-€1M):** +first human hire = Sales Lead (J3). Mittelstand Geschäftsführer требует human trust. Fractional Steuerberater → first interactions with fractional CFO.
- **Phase 2a (2027 → €1-5M):** Head of Finance (FTE). C-suite slots начинают заполняться. Chief of Staff добавляется.
- **Phase 2b (2028 → €5-15M, 20 employees):** COO (Executor архетип из Sadun & Bennett). Split Ruslan strategic-management.
- **Phase 2c (€10-50M, 100 employees):** Full C-suite; Constellation Software "delegation to abdication" pattern; 6 Operating Groups hint.
- **Phase 3 (€50M+, 500+):** DACH regulatory triggers — DrittelbG (1/3 Aufsichtsrat), MitbestG (2000+). Multi-entity Holdings BV + Operations GmbH.

**Promotion Signals (R1 §G.7):**
- J1 → J2: выполняет без clarification >80%, предлагает альтернативы, self-reviews, 3+ delivery cycles "exceeds".
- J2 → J3: управляет workflow J1-агентов без микроменеджмента, domain-level decisions, 2+ quarters ownership.
- J3 → J4: cross-domain, OKR для функции, revenue contribution attributable, first hiring recommendation принят.
- J4 → J5: irreversible J4 decisions autonomously, year roadmap, peer J4s consult.

**AI agent promotion:** extends `decision_rights` в role-manifest после 90-day track record с <2% escalation rate и zero false-positive critical decisions.

**Human-AI boundary (R1 §G.6):**
- "Точно human": первые встречи Mittelstand GF, контракты (sign), увольнения, IHK events, Type 1 decisions.
- "Точно AI": inbox-processor, sales-research, knowledge-synth, routine monitoring.
- "Зависит": sales-outreach (AI writes, human reviews >€50K), delivery (human reviews for strategic clients), analyst (human validates interpretations for client presentation), meta-agent (human signs legal).

**C-suite timing (R9 §A.1-A.5):**
- CFO: fractional на €1M ARR, FTE на $10M+.
- CMO: boutique на €1M ARR, full-C на €15-20M.
- COO: 50-100 сотрудников / $5-10M ARR, Executor archetype для Jetix.
- CTO: 10-30 engineers или $2M ARR.
- CHRO: 100-200 сотрудников.
- Chief of Staff: 30-50 чел., перед COO.
- CAIO (Chief AI Officer): Phase 2c при 50+ сотрудников; до этого — Ruslan де-факто.

#### Alternatives Considered
- **Alt A: Flat Anthropic-style "Member of Technical Staff":** rejected — needs C-suite differentiation для Mittelstand trust-building.
- **Alt B: Classic MBB (Analyst → Associate → EM → AP → Partner):** partially adopted — Partner-level ≈ JX, но Mittelstand-style (Roland Berger) better fit than McKinsey.

#### Rejected Options
- **Opt X: No career levels (pure self-organization):** rejected — Mittelstand Konsenskultur требует clear hierarchy.

#### Rationale
1. [R1 §G.1-G.8] полный Career Ladder framework.
2. [R9 §A.1-A.6] C-suite DACH specifics.
3. [R1 §F.1-F.3] AI compresses junior skill premium; senior orchestration becomes leveling signal.

#### Trade-offs
- 7 levels vs simpler 4-level: adopted 7 для future-proof, но J0 rarely used в Jetix (most tasks require J1+).

#### Open Questions for Ruslan
- **Q1:** `crazy-agent` — J3 (R1 mapping) или специальный "hackathon mode" outside ladder?
- **Q2:** Life-coach — в Jetix career ladder или только в Life-OS?

#### Implementation Pointer
D7 JETIX-CAREER-LEVELS.md = full ladder table + decision-rights matrix + phase transitions roadmap + human-AI boundary + C-suite timing table + promotion signals + DACH regulatory triggers (BetrVG, BDSG, DrittelbG, MitbestG).

---

### Area 8: Operational Instructions (→ D8 docs/INSTRUCTIONS.md)

#### Unified Recommendation

**14-day L1 Foundation rollout plan (R2 §H.4)** — один operational guide для Ruslan:

| Day | Work | Deliverable | Done criterion |
|-----|------|-------------|----------------|
| 1 | Repo init + folder structure + README | `jetix-os/` structure | `git log` shows initial commit, folders created |
| 2 | SOPS + age setup | `secrets/*.enc.yaml`, `.sops.yaml`, pre-commit hook | `sops edit` works, `git diff` shows keys only |
| 3 | Justfile base commands | `justfile` with `eval`, `backup`, `deploy`, `docs-serve`, `lint`, `cost-check` | `just --list` shows all |
| 4 | `.claude/agents/*.md` refactor | 12 agents с new frontmatter | Claude Code loads without errors |
| 5 | First `roles/<role>/role.md` + `executors/<id>.yaml` | sales-lead role (8 blocks) + claude-sales-lead executor | Reviewer answers "what does role do?" from file alone |
| 6 | First prompt in `agents/<name>/v1/system.md` | Immutable version | Frontmatter reflects version |
| 7 | First golden dataset (10 cases для 1 role) | `evals/<role>/golden.jsonl` | `promptfoo eval` runs without errors |
| 8 | Promptfoo CI + `.github/workflows/eval.yml` | GitHub Actions eval-on-push | Push to `prompts/**` triggers eval |
| 9 | Langfuse self-host (Docker on Hetzner) | `infra/docker-compose.yml` + Claude Code hook | Langfuse UI on `http://hetzner-ip:3000` |
| 10 | MkDocs Material docs (Diátaxis 4 folders) | `docs/` + `mkdocs.yml` + GitHub Pages | `mkdocs gh-deploy` successful |
| 11 | Vale + markdownlint + lychee CI | `.github/workflows/docs.yml` + `.vale.ini` | Push to `docs/**` triggers lint |
| 12 | First Oxide-style RFD | `decisions/0001-jetix-architecture-final.md` | RFD state=`committed` |
| 13 | Postmortem template + example | `postmortems/template.md` + README | `just postmortem` creates new file |
| 14 | Monitoring stack + backup | Uptime Kuma + Healthchecks.io + Sentry + Netdata + restic | `just backup` works, Healthchecks shows UP |

**After Day 14:** L1 Foundation active. Start first 6-week Shape Up cycle.

**Tool stack (R2 §H.2):**
- Eval: **Promptfoo CLI** (GitHub Actions, free) + **Langfuse self-hosted** (OSS, trace + prompt registry + eval).
- Docs: **MkDocs Material** (Python stack, GitHub Pages).
- Secrets: **SOPS + age** (git-native, offline).
- Monitoring: **Uptime Kuma + Healthchecks.io + Sentry (free) + Netdata**.
- Backup: **restic → Hetzner Storage Box + Backblaze B2**.
- Task runner: **`just` (justfile)**.
- Decision records: **Oxide-style RFDs**.
- Git workflow: **Trunk-based solo** (commit to main, eval gate on push).
- Deploy: **Coolify** (push-to-deploy, Claude integration).
- Prompt registry: **git + folders** (Langfuse Tags при >20 agents).

**Daily/weekly/monthly/quarterly rituals (R3 §E.1-E.3):**
- Daily: inbox triage (inbox-processor); pipeline review (sales-lead); agent grading (meta-agent); morning approvals; commit.
- Weekly: Shape Up review (manager); Toggl review; close-week commit.
- Monthly: strategizing trigger check; QA audit; P&L review; OKR update; founder letter draft.
- Quarterly: quarterly letter (Berkshire-style); OKR set; role-manifest review; strategy offsite (post-Phase 1).

**Shape Up cycles (Basecamp):** 6 weeks work + 2 weeks cool-down. Betting Table = Ruslan. Cool-down = postmortems, role-manifest updates, eval golden dataset expansion, wiki consolidation.

#### Alternatives Considered
- **Alt A: Scrum/Agile ceremonies:** rejected — no standups, no story points, no retros with 12 AI agents.
- **Alt B: Kubernetes/Helm deploy:** rejected — overkill, Coolify + systemd covers current needs.
- **Alt C: Vault for secrets:** deferred — SOPS+age sufficient до Phase 2b.

#### Rejected Options
- **Opt X: Copy GitLab Handbook 2000+ pages:** rejected — unmanageable для solo.
- **Opt Y: All-Obsidian authoring:** deferred — Obsidian as reading layer, git as storage contract.

#### Rationale
1. [R2 §H.1-H.10] complete 14-day rollout tested.
2. Minimum viable infrastructure — Kubernetes trigger = +20 executors, not now.

#### Trade-offs
- Self-hosting Langfuse вместо SaaS — maintenance overhead vs data sovereignty.

#### Open Questions for Ruslan
- **Q1:** Day 1 timing — когда конкретно начинать 14-day rollout? Parallel с D1-D9 чистовиками или после?
- **Q2:** Langfuse self-host vs cloud (free tier)?

#### Implementation Pointer
D8 docs/INSTRUCTIONS.md = 14-day plan (day-by-day) + tool stack rationale + daily/weekly/monthly rituals + Shape Up cycles + onboarding checklist.

---

### Area 9: Final Decision Record (→ D9 decisions/2026-04-20-jetix-architecture-final.md)

#### Unified Recommendation

D9 = **T-02 template decision record** фиксирующий всё принятое в D1-D8. Format (Oxide RFD state-machine):

```markdown
---
rfd: 0001
title: Jetix Architecture v1 Final
authors: Ruslan <ruslan@jetix.ai>
state: committed   # prediscussion | ideation | discussion | published | committed | abandoned
date: 2026-04-20
tags: [architecture, foundation, mega-corp]
supersedes: [design/JETIX-ARCHITECTURE-WORKING.md v0.9]
---

# RFD 0001: Jetix Architecture v1 Final

## Problem Statement
Jetix needs formal architecture спецификацию, масштабируемую до mega-corp без rebuild.

## Background
8-layer synthesis v0.9 (design/JETIX-ARCHITECTURE-WORKING.md), 9 research waves, stage 1 deep synthesis (raw/research/architecture-implementation-synthesis-2026-04-19.md).

## Decision
We adopt:
1. 7-слойная архитектура (L0 Executive Core + L1-L7 + shared).
2. Model D Nested Hierarchy (life-os root, jetix project, 3-phase migration).
3. 10 core alphas with state machines (Hybrid C для 6, wiki-primary для 3, YAML-only для 1).
4. 8-block role-manifest (R3 spec).
5. J0-JX career ladder (R1 spec).
6. Company-as-code stack (R2 tools).
7. DACH Mittelstand positioning (не McKinsey).
8. FPF-Lite 3-5 pages (R3 §H.1).
9. 14-day L1 Foundation rollout.

## Alternatives Considered
[→ Part 3 этого synthesis]

## Consequences
Positive: [...]
Negative: [...]

## Rollback Plan
[...]

## Questions / Open Issues
[→ Part 4 этого synthesis]
```

#### Alternatives Considered
- **Alt A: Single monolithic T-02:** rejected — 9 D-documents better для navigability.
- **Alt B: Notion page instead of git:** rejected — git SoT principle.

#### Rejected Options
None.

#### Rationale
Oxide RFD pattern proven [R2 §A.8]; links D1-D8 as supporting artifacts.

#### Trade-offs
Document maintenance overhead vs clarity.

#### Open Questions for Ruslan
None — D9 is meta-document capturing D1-D8.

#### Implementation Pointer
D9 decisions/2026-04-20-jetix-architecture-final.md = Oxide RFD template + D1-D8 backlinks + state: committed + git tag `architecture-v1-final`.

---

## Part 3 — Conflicts Resolved

### Conflict 1: `alphas/` namespace — keep (R4) vs flatten (R6)

**Context:** Где хранить operational state entity types (Client, Project, Deal, etc.) — отдельная `alphas/` директория или прямые folders в `jetix/clients/`, `jetix/projects/` и т.д.?

**R4 position:** [R4 §H.1-H.2] — keep `alphas/` как отдельный слой для operational state. Rationale: "отделяет operational state от semantic knowledge (wiki/), решает dual-write проблему". Hybrid C storage pattern: `alphas/<type>/<id>/{state.yaml, context.md, history.jsonl}`.

**R6 position:** [R6 §J.7 D3] — "Убрать `alphas/` namespace. Прямые папки `clients/`, `projects/`, `deals/`." Rationale: "`alphas/` — хорошее концептуальное слово, плохое имя папки. Вводит лишний уровень вложенности."

**Your resolution:** **Keep `alphas/` with nested structure per type** + ADD `clients/` в R5-стиле как markdown CRM layer (separate concern).

**Rationale:**
1. R4 operational vs semantic split более важен, чем R6 UX критика. Daily work agent работает с `alphas/clients/<id>/state.yaml` (machine-readable) — это explicitly operational layer.
2. R5 CRM pattern `clients/{companies,contacts,deals,activities}/` — это human-facing markdown notes layer, separate from operational alpha state.
3. Обе layer coexist: `alphas/clients/acme-gmbh/state.yaml` (operational) ↔ `clients/companies/acme-gmbh.md` (entity note) ↔ `wiki/entities/clients/acme-gmbh.md` (wiki-side view) linked via `alpha-ref` edge type.

**Trade-off:** Three places referencing same client (alphas/, clients/, wiki/). Mitigated: alpha-ref edges in `edges.jsonl` + pre-commit hook validating links + agent reads via single lookup через index.

**Open:** Documentation of three-layer responsibilities (state vs notes vs wiki) must be explicit in D5.

---

### Conflict 2: Role-manifest format — 8 blocks (R3) vs simpler YAML (R8)

**Context:** Canonical role-manifest format для Jetix.

**R3 position:** [R3 §C.1-C.9] — 8 blocks (identity, ontological, method, graph-of-creation, seniority, implementation-ai, implementation-human, evolution). YAML frontmatter + Markdown body. ~500-1000 lines per manifest при filled.

**R8 position:** [R8 §C.2-C.3] — simpler YAML-only schema: id, layer, purpose, accountabilities, decision_rights, reporting_to, kpi, version. ~50-100 lines per manifest.

**Your resolution:** **Adopt R3 8-block format as canonical. R8 schema = lint subset (required fields).**

**Rationale:**
1. Mega-corp aspiration requires все 8 blocks для Phase 2b+ (implementation_human block критичен).
2. `seniority.decision-rights` (R1 Career Ladder) нужен для AI escalation логики.
3. `evolution.changelog` — audit trail для роли.
4. R8 simpler schema остаётся полезен как **lint check** (`required fields: [id, layer, purpose, accountabilities, decision_rights.autonomous, reporting_to, kpi]`).

**Trade-off:** High-ceremony 8-block manifest может замедлить создание новых ролей. Mitigated: "Minimum Viable Manifest" = Blocks 1, 2, 4, 6 (R3 anti-pattern АП-2). Остальные filled итерационно.

**Open:** Convention for partial manifests (status: draft) — когда lint strict vs relaxed.

---

### Conflict 3: Event log — per-alpha (R4) vs monthly aggregate (R5)

**Context:** Где хранить history of alpha state transitions + activities?

**R4 position:** [R4 §D.2 Hybrid C] — `alphas/<type>/<id>/history.jsonl` (per-alpha, append-only).

**R5 position:** [R5 §C.2] — `alpha-log/YYYY-MM.jsonl` (single file per month, все alphas).

**Your resolution:** **Both — per-alpha as hot write, monthly aggregate as projection.**

**Rationale:**
1. Per-alpha `history.jsonl` = read-locality для agent работающего с конкретным клиентом (load only relevant history into context).
2. Monthly `alpha-log/YYYY-MM.jsonl` = cross-entity analytics, GoBD audit trail, compliance.
3. Redundancy приемлема — events write к per-alpha → `scripts/project.py` daily/weekly rebuilds monthly aggregate.
4. Compensating events (R5 §C.6) write к both places одновременно для consistency.

**Trade-off:** Dual-write complexity. Mitigated: automated projection script, not manual sync.

**Open:** Fail-safe — что если projection script breaks и monthly log out-of-sync?

---

### Conflict 4: Life-OS position — 4 options (R7)

**Context:** Физическое разделение Life-OS и Jetix.

**R7 positions:** 4 options — Option 1 (nested), Option 2 (parallel monorepo), Option 3 (submodule), Option 4 (separate repos).

**Your resolution:** **Option 2 (parallel monorepo) → Option 4 (separate repos) at Phase 2 trigger.**

**Rationale:**
1. [R7 §B-D recommendation matrix] — Option 2 для Phase 1 (single-person simplicity); Option 3 (submodule) explicitly rejected как "submodule hell"; Option 4 direct переход предпочтительнее.
2. Phase 2 trigger: first human hire OR GDPR DPA enterprise client.
3. Model D (nested hierarchy) сохраняется conceptually — Life-OS root через reference layer, не через filesystem nesting.

**Trade-off:** Migration overhead в Phase 2 (~1 day work via `git filter-repo`). Accepted.

**Open:** `shared/` Phase 2 fate — duplicated in both репо, separate public repo, или only-Jetix?

---

### Conflict 5: SemVer для promptов — full (R2) vs major-only (R6)

**Context:** Versioning структура для prompts.

**R2 position:** [R2 §H.1, §B.1] — full SemVer в folders: `prompts/<agent>/v1.0.0/`, `v1.0.1/`, `v1.1.0/`, ...

**R6 position:** [R6 §D2, §J.1] — only major versions in folders + git tags для minor/patch: `agents/<name>/v1/system.md`, `v2/system.md`; git tag `agent-sales-lead-v2.1.3`.

**Your resolution:** **R6 major-only folders + git tags.**

**Rationale:**
1. [R6 §D2] folder explosion: 30 agents × 100 versions = 3000+ folders.
2. Git already IS version control — duplicating через folders redundant.
3. Parallel A/B testing (v1 + v2 simultaneously in working tree) only matters for major changes.
4. SemVer в frontmatter (Block 1 `identity.version`) + git tags give full traceability.

**Trade-off:** Cannot parallel test minor versions in working tree. Accepted — minor changes git branched.

**Open:** При major bump — `v2/` new folder, `v1/` archived in place? Or `v1/` moved to `archive/`?

---

### Conflict 6: Notion integration — SoT vs view

**Context:** Role of Notion в Jetix.

**R5 position:** [R5 §A.3] — Notion = anti-pattern as SoT (API rate limits, UUID opacity, export fidelity).
**R2 position:** [R2 §H.10 anti-pattern 6] — "Git = SoT. Notion = view layer. Никогда не редактировать в Notion то, что есть в Git."

**Your resolution:** **Notion = read-only view via MCP; all edits в git.**

**Rationale:**
1. Company-as-code principle.
2. Notion used for human-friendly dashboard (stakeholder presentations, journal views) but never as source.
3. Bi-directional sync rejected — introduces consistency issues.

**Trade-off:** Ruslan loses Notion editing convenience. Mitigated: Obsidian as editing layer over git markdown.

**Open:** Migration path для 557 wiki pages if any still edited в Notion.

---

### Conflict 7: "12 agents" number — fixed or variable

**Context:** Is "12" canonical or illustrative?

**v0.9 position:** 12 ролей in table.
**R3 position:** [R3 §G.1] — number variable; roles split by Miller's law (accountabilities > 7) or scale triggers.
**R1 position:** [R1 §G.1] — roles 12-200 scale;
**R9 position:** [R9 §A.2-A.5] — C-suite adds roles по phase.

**Your resolution:** **"12" illustrative, not константа.**

**Rationale:**
1. All three research confirm scale-up-first design.
2. L0 Executive Core layer — переменное количество slots.
3. Role-manifest `seniority.split_trigger` — explicit rule for splitting.

**Trade-off:** Documentation harder когда "roles" unbounded. Mitigated: `org-index.yaml` auto-generated.

**Open:** How to communicate "not fixed 12" externally — в marketing, в Mittelstand proposals?

---

### Conflict 8: FPF extent — Lite (R3) vs Full (implicit в academic research)

**Context:** How much Левенчук-ontology to adopt.

**R3 position:** [R3 §B.6-B.7] — FPF-Lite (3-5 pages), explicit exclusions.
**No countervailing position** — R3 decisive.

**Your resolution:** **FPF-Lite accepted. Full FPF = read-only reference.**

**Rationale:** R3 §B.7 explicit cost-benefit analysis.

**Trade-off:** None significant.

**Open:** When trigger full FPF adoption? R3 suggests 50+ agents or Series A — likely not in 2026-2028.

---

### Conflict 9: Event sourcing scope — all fields (pure) vs state+activities only (hybrid)

**Context:** Which events go in event log?

**R5 position:** [R5 §C.7] — "start events.jsonl from day one but only for state-change events and activity events. Do not event-source field edits on Companies or Contacts — those belong to the markdown file and rely on git commits."

**Your resolution:** **Hybrid — state transitions + activities in event log; field edits in markdown + git.**

**Rationale:** Lean event log; git commits as audit trail for slow-changing data.

**Trade-off:** None.

**Open:** Should `contact.consent-updated` (GDPR-relevant) be event-sourced для compliance? Likely yes.

---

### Conflict 10: Decision records format — Nygard ADR vs MADR vs Oxide RFD

**Context:** Canonical format для decisions.

**R2 position:** [R2 §F.3] — Oxide RFD best overall.
**R8 position:** [R8 Part J.5] — RFD-style with state machine.

**Your resolution:** **Oxide RFD format** (prediscussion → ideation → discussion → published → committed → abandoned). Nygard ADR + MADR covered within RFD body.

**Rationale:** RFD covers tech + business + operational decisions; state machine better для pre-decision discussion.

**Trade-off:** Nothing significant.

**Open:** Nested RFDs (e.g., RFD 0042 supersedes 0001) — tracking convention.

---

## Part 4 — Open Questions

### Q1: Первый human hire timing

**Context:** Когда именно первый human executor добавляется?
**Why it matters:** Phase 2 trigger точка; influences Life-OS extraction, юр. структуру, Toggl workspaces.
**What we'd need to answer it:** Revenue velocity data (€/month), Ruslan's opportunity cost data (какой % времени на J2 tasks), Mittelstand pipeline conversion rates.
**Impact on D1-D9:** D4 (migration timing), D7 (Phase transitions exact), D8 (Phase 2 infrastructure setup date).

### Q2: C-suite slots в L0 на Day 1

**Context:** Резервируем role-manifests для COO/CFO/CSO/CMO/CTO now (empty, expected-executor: null) или добавляем реактивно при найме?
**Why it matters:** Architectural scaffolding vs YAGNI.
**What we'd need to answer it:** Vision clarity on 2027-2028 structure.
**Impact on D1-D9:** D3 (roles created now), D7 (Phase 2 plan).

### Q3: Strategic-management роль декомпозиция

**Context:** Сейчас Ruslan — одна роль (strategy + framing + sales + acceptance + external). 5 sub-roles или monolithic?
**Why it matters:** Explicit decomposition clarifies delegation path.
**What we'd need to answer it:** Ruslan self-reflection на текущие time allocation.
**Impact on D1-D9:** D3 (one vs five role-manifests), D7 (Phase 2 split plan).

### Q4: Personal vs Geschäftskonto timing

**Context:** Phase 1 Freiberufler + personal bank OR Gewerbe + Geschäftskonto (UG) сейчас?
**Why it matters:** Legal + tax + migration timing.
**What we'd need to answer it:** Revenue projection Q2 2026, legal advice.
**Impact on D1-D9:** D4 (money accounting Phase 1 structure).

### Q5: Primary eval tool — Promptfoo vs Langfuse vs DeepEval

**Context:** All three self-hostable, free. R2 recommends dual (Promptfoo CI + Langfuse tracing). Pick one as primary?
**Why it matters:** Single tool reduces cognitive overhead; integration depth.
**What we'd need to answer it:** Test run each с sales-lead eval dataset.
**Impact on D1-D9:** D8 (Day 7-9 plan exact tool).

### Q6: FPF-Lite публикация (L5 Membrane public artifact)

**Context:** FPF-Lite internal forever или eventually public (Phase 3)?
**Why it matters:** Community/Alliance positioning; marketing leverage.
**What we'd need to answer it:** Competitive analysis — would публикация help or hurt?
**Impact on D1-D9:** D6 (writing style: internal audience vs external), D1 (strategy narrative).

### Q7: Mega-research по career levels (second pass)

**Context:** v0.9 identified follow-up mega-research (R1 partially addressed). More deep research needed?
**Why it matters:** Role splits, compensation matrices, gradient paths.
**What we'd need to answer it:** Does R1 cover enough? Soft yes.
**Impact on D1-D9:** D7 (could expand Career Ladder content, but no blocker).

### Q8: `shared/` content boundaries

**Context:** Что ровно в `shared/`? Role-framework tools, Левенчук-онтология, writing templates. Что-то ещё?
**Why it matters:** Phase 2 migration (keep in both или move to third public repo).
**What we'd need to answer it:** Experiment — что появляется в `shared/` при actual development.
**Impact on D1-D9:** D2 (folder structure), D4 (migration plan).

### Q9: Alliance timing — founding members после первого L4 клиента

**Context:** R9 principles + CLAUDE.md rules. Ruslan confirmed "после первого клиента", но когда точно?
**Why it matters:** L5 Membrane layer activation.
**What we'd need to answer it:** First L4 client timeline (Q2 2026 target).
**Impact on D1-D9:** D1 (L5 narrative), D7 (Phase 1 → 2 timing).

### Q10: Hypothesis alpha — wiki-primary vs operational

**Context:** R4 §D.2 says wiki-primary (in `wiki/claims/`). Is state.yaml needed for active hypothesis tracking?
**Why it matters:** Solo founder tracks hypothesis = learning engine.
**What we'd need to answer it:** First few hypotheses in production — do they need lifecycle states?
**Impact on D1-D9:** D5 (alpha storage pattern per type).

---

## Part 5 — Review Package (для Этапа 2)

### 5.1 For Critic Chat

**Context для reviewer:** Ты — devil's advocate. Attack this synthesis. Find gaps, weaknesses, risks. Cite specific sections.

**Specific items для критики (10-15):**

1. **Over-engineering risk:** 20+ top-level folders + 8-block role-manifest + 10 alphas + 5-layer per-agent memory + Constitution §11 — не слишком ли много architecture для solo founder с €0 revenue и Q2 €50K target?
2. **Phase 2 migration (Life-OS extraction) risk:** `git filter-repo` cuts historical lines — any case where historical reference from Jetix to Life-OS breaks and rollback painful?
3. **Career ladder (J0-JX) для AI agents:** Анатомически J0-JX имеет смысл для humans, но для AI agents "promotion" означает just expanding `decision_rights` в role-manifest — не manufactured ceremony?
4. **10 alphas overkill:** Hypothesis + Research Note + Postmortem как отдельные alphas — добавляет overhead vs просто wiki pages?
5. **FPF-Lite 3-5 pages vs Cluade system prompt budget (2K tokens):** 3-5 pages = ~2000-3000 words = ~3000-5000 tokens — FPF-Lite alone fills system prompt budget. Room for agent-specific context?
6. **Coolify + Hetzner + systemd — DACH compliance edge cases:** GDPR data residency in Germany OK, но если enterprise client требует ISO 27001 certification — current stack sufficient?
7. **"Company-as-code" narrative для Mittelstand — will they get it?** Mittelstand Geschäftsführer может находить termin "code" слишком technical. Positioning risk.
8. **Event sourcing + per-alpha history.jsonl + monthly alpha-log + git commits = 4 sources of truth для audit.** Which wins if conflicting? R5 §C.6 compensating events handle, but complexity.
9. **`agents/<id>/system.md` vs `roles/<role>/role.md` — what if agent assigned to role becomes mismatched?** Drift detection mechanism?
10. **Phase 1 Ruslan solo: burnout risk.** 12+ роль-менеджментов, 7 слоёв, weekly/monthly/quarterly rituals — realistic для 6 focused hours/day?
11. **Alphas vs clients/ vs wiki/entities/ — triple representation:** What if Ruslan edits one, forgets others? Pre-commit hook sufficient validation?
12. **DACH regulatory triggers (Betriebsrat 5+, DPO 20+, DrittelbG 500+) — does Phase 2 plan address them explicitly?** Current synthesis mentions but доesn't specify response actions.
13. **Promptfoo + Langfuse dual — real need or cognitive overhead?** Single tool simpler.
14. **"Hourly billing запрещено" absolutism:** Edge case — Mittelstand client требует hourly для small advisory engagements. Hard rule приводит к потерянным deals?
15. **Mittelstand focus = narrow TAM:** At €50M+ ARR, DACH alone feasible или expansion required? If expansion, architecture accommodates?

**Assumptions to challenge:**
1. Mittelstand Konsenskultur primary driver для hiring Sales Lead J3 first — is this assumption validated by Ruslan's actual discovery calls or a hypothesis?
2. 12 Claude agents сейчас really covering все 7 layers adequately, или just L1-L4?
3. "AI compresses skill premium" (R1 §F.1) — how much vs specific DACH industries (manufacturing more conservative)?
4. HippoRAG scales to 5000+ pages без performance issues — R4 §G acknowledges "open research question."
5. Constellation Software pattern applicable для micro-SaaS поглощений при ARR €2-10M — or too big jump?

**Hidden risks:**
1. Anthropic pricing changes → 12+ agents monthly cost spike.
2. Claude Opus 4.7 → 5 transition breaks role-manifests (unlikely, but).
3. DACH regulator surprise ruling on AI agents as "data processors."
4. GitHub outage (mono-dependency на git).
5. Ruslan health event: bus factor = 1 (R9 §F.4 mentioned, but doc mitigation?).

---

### 5.2 For Simplifier Chat

**Context:** Ты — anti-complexity. Where over-engineered? What can be removed without loss?

**Specific complexity candidates (10-15):**

1. **5-layer per-agent memory** — can be 3 layers (system.md, scratchpad.md, niche/) with strategies.md merged into system.md, mailbox separate.
2. **10 alphas** — start с 3-4 (Client, Deal, Invoice for Phase 1); rest added реактивно.
3. **Constitution §11** — start с §1-§5; add rest когда real incidents occur.
4. **14 role-manifests immediately** — migrate Top 5 (manager, meta-agent, sales-lead, delivery, strategist) first; rest gradual.
5. **Separate `roles/` + `executors/` + `agents/` directories** — combine into `agents/<id>/{manifest.md, system.md, evals/, v1/, v2/}`. R6 D1 hinted at this.
6. **JSON Schema + lint + CI** — start с simple Python script validating required fields; full JSON Schema only если role-manifests proliferate.
7. **Model D Nested 7 layers** — simplify to 3 layers (Foundation / Operational / Portfolio) for Phase 1?
8. **Promptfoo + Langfuse + SOPS + Coolify + Uptime Kuma + Healthchecks + Sentry + Netdata** — 8 tools for Phase 1 solo. Pick 3-4.
9. **Daily/weekly/monthly/quarterly/annual rituals** — Phase 1 daily + weekly enough; monthly/quarterly forced ceremony.
10. **Per-alpha `history.jsonl` + monthly aggregate** — single monthly file sufficient for Phase 1 audit.
11. **8-block role-manifest** — 4 blocks (identity, ontological, method, implementation-ai) enough for Phase 1.
12. **Full 6 niches symlinks per agent** — один niche per agent в Phase 1.
13. **FPF-Lite 3-5 pages** — 1 page enough для Phase 1.
14. **Diátaxis 4-form docs** — 2 forms (how-to + reference) sufficient.
15. **Career ladder J0-JX** — 3 levels (Junior/Senior/Lead) для Phase 1.

**What can be removed без loss (Phase 1):**
1. `letters/` directory — quarterly letters can be monthly at first.
2. `hypotheses/` as separate alpha — use `wiki/claims/` only.
3. `policy/` directory — merge into `decisions/`.
4. `shared/` directory — keep content within `jetix/` до Phase 2 extraction.
5. `strategizing/` directory — just another decisions/ type.

**Premature optimizations:**
1. GraphRAG community detection — trigger 5000+ pages not 557.
2. OPA/Rego — trigger 50+ roles not 12.
3. CUE/Dhall — trigger 100+ roles не 12.
4. Vector DB — trigger 3000+ pages не 557.
5. Kubernetes — trigger +20 executors, not now.

---

### 5.3 For Mega-Corp Visionary Chat

**Context:** Ты — 10x scale thinker. What breaks at 10x? What's missing?

**Scale-up weaknesses (10x = 120 agents, €500K ARR, team of 5):**

1. **`agents/<id>/` structure с 120 agents — filesystem navigation performance** (ls, git status slow).
2. **`alpha-log/YYYY-MM.jsonl` с 120 agents producing events — file size explodes** (10K-100K events/month).
3. **HippoRAG PPR на 5000+ pages + 5000+ edges — latency grows.** R4 §G.2 acknowledges unknown.
4. **Context loading budget 50K tokens** — с 120 agents, 50 niches, 5000 pages — budget insufficient для some tasks.
5. **Git repository size** — monorepo c histories + 120 agents + 5000 pages + 1000 invoices + event logs likely >10GB. Performance degrades.
6. **CI/CD run time** — 120 agent eval jobs on every push = CI queues backed up.
7. **Single SoT для decisions** — при 5+ humans PR reviews block velocity.
8. **Ruslan as single approver** — 5 humans + 120 agents all escalate to him.
9. **Promptfoo + Langfuse** — UI может не scale для 120 agents dashboards.
10. **Toggl two workspaces** — team collaboration на time tracking потребует enterprise plan.

**Phase 2/3 readiness gaps:**
1. **First hire onboarding**: no explicit "learn the system" путь — R1 mentions "shadow AI 1 week" but no concrete content.
2. **Geschäftsführer regulatory role**: when Ruslan registers UG — он становится Geschäftsführer с юр. accountability. Architecture ignore this in L0 spec.
3. **DPO обязательный** при 20+ data processors — role slot not в current L0 roster.
4. **Betriebsrat** при 5+ employees — interaction model with architecture not defined.
5. **Aufsichtsrat** при 500+ — completely unaddressed.
6. **M&A governance** — R9 Part G covers, но architecture doesn't reflect acquisition absorption.
7. **Multi-entity Holdings BV + Ops GmbH** (Phase 3) — current architecture мonoorepo doesn't easily federate.
8. **Succession planning** — bus factor = 1 mentioned, no документ.
9. **Translation management** (when Ruslan hires non-Russian speakers) — docs mostly Russian.
10. **Compensation architecture** — VSOP vs §19a EStG, ESOP — not in Phase 1 architecture.

**Missing patterns для mega-corp:**
1. **Federation of repos** — Phase 3 multi-entity needs federation model (beyond monorepo).
2. **Service-level operational roles** (site reliability, security, compliance) — not in current roster.
3. **Customer Success function** — L4 includes retainer, but CS as distinct role absent.
4. **Product management function** (L3 expansion) — когда micro-SaaS launches.
5. **Legal function** — GC trigger when?

---

### 5.4 For Левенчук Expert Chat

**Context:** Ты — ШСМ expert. ШСМ correctness?

**ШСМ applications to verify:**

1. **Роль primitive** — 8-block manifest accurately reflects Левенчук-role? Missing elements?
2. **Альфа primitive** — 10 alphas cover Essence Kernel + business extensions correctly?
3. **Граф создания** — R3 §A.3 definition; current synthesis uses `graph_of_creation` block in role-manifest — adequate representation?
4. **Стратегирование** — FPF-Lite Section 7 ritual; Template R3 §E.1; appropriate?
5. **Мышление письмом** — daily/weekly/monthly/quarterly rituals (R3 §E.2); agent participation pattern (R3 §E.3) — does this preserve thinking-as-process, не just artifact?

**Ontology cleanness concerns:**
1. **Role ≠ executor strict separation** — but `roles/<role>/role.md` имеет `implementation_ai` и `implementation_human` blocks. Is this blurring?
2. **Alpha states** — "active_deal" style state (R4 example) vs past-participle "Qualified" (R3 §A.2 Essence convention). Consistent across 10 alphas?
3. **Граф создания для AI-agent context** — R3 §F.7 "agent не строит graph autonomously; explicit в CLAUDE.md." But CLAUDE.md is project-level, not per-role. Adequate?
4. **Стратегирование is human-only** (R3 §A.4) — but some R9 patterns (Constellation hurdle rates) imply AI-assisted strategy. Contradiction?
5. **U-Types Lite (4-6)** — R3 §H.1 "U.System, U.Role, U.Method, U.Stakeholder." Minimal sufficient или violates ontological completeness?

**Где можем нарушать ролевую онтологию:**
1. **Multi-role executor (Ruslan)** — один human может fill strategic-management + parts of sales-lead + chief-of-staff simultaneously. R3 §A.1 mentions "multi-roled founder" as critique of role ontology. How handle?
2. **Agent orchestration** — manager role coordinates other agents. Left pattern strictly ролевой или нарушает (manager acts on behalf of roles)?
3. **Dynamic role assignment** — agent назначает себя role at task-time. R3 §A.1 mentions this as third critique.
4. **Холоны recursive** — Ruslan as executor играет role; role — part of Jetix холон; Jetix — part of Life-OS холон. Proper FPF-Lite treatment?

**FPF-Lite honest?**
1. 3-5 pages — is it truly Левенчук FPF sub-set or approximation?
2. Excludes full mereology, 17 disciplines, category theory — are these excluded cleanly or just postponed?
3. Does FPF-Lite risk "переводить на язык доминирующей области" (R3 §B.4 LLM Fortran critique)?

---

### 5.5 For Final Synthesizer Chat

**Context:** Ты — meta-synthesizer. Identify hard questions requiring deep thinking.

**5-7 hard open questions:**

1. **L0 декомпозиция.** Ruslan strategic-management роль — один manifest monolithic или 5 sub-roles explicit? Trade-off: operational clarity (5 sub-roles) vs human reality (Ruslan fluidly switches). Which wins?

2. **Phase 2 migration timing.** Concrete trigger — "first human hire" sounds clean, but may conflict с "€300K ARR hit" metrics. Dual-criteria OR-logic (either triggers) or AND-logic (both required)?

3. **"Company-as-code" externality.** Will публикация org-in-git artifacts (Phase 3) help positioning или make competitors copy easily? Open-source Jetix framework vs proprietary advantage.

4. **Alpha coverage completeness.** 10 alphas — is this complete MECE coverage of Jetix business operations? What about "Employee/Contractor" as alpha at Phase 2? "Partner" for Alliance members — not in current list.

5. **`shared/` methodology trapping.** If role-framework + Левенчук-онтология + templates in `shared/` — and Jetix publishes framework eventually — что тогда with `shared/` vs `jetix/` vs `life-os/`? Triple-licensing model needed?

6. **DACH positioning stickiness.** At €50M+ ARR, is Mittelstand DACH focus maintained или expansion mandatory? If expansion required, когда triggered and how architected?

7. **Meta-conflict: premature structure vs emergent structure.** R3 §H.6 anti-pattern "онтология ради онтологии" + R6 §J.9 anti-patterns vs R1-R9 prescriptive architecture. Where is the line? If we pre-design 7 layers + 10 alphas + 8 blocks + 12 roles — are we committing "premature structure" anti-pattern, OR building necessary scaffolding?

**Meta-conflicts между reviewers (predicted):**
- Critic will argue over-engineered; Mega-Corp will argue under-engineered. Reconciliation: "scaffolding now for 10x scale" vs "simplify for Phase 1 execution."
- Simplifier will argue fewer layers; Левенчук expert will argue completeness matters for ontology.
- Final synthesizer must weight these — Ruslan's judgment call.

**Critical decision points:**
1. Does architecture commit to full structure now (scaffolding) or iterate (start 3-4 layers)?
2. Does role-manifest commit to 8 blocks now or start 4-block MVP?
3. Does Life-OS extraction happen pre-hire (preemptive) or at-hire (reactive)?

---

## Part 6 — Implementation Roadmap Preview

### 6.1 D1-D9 writing order

Dependencies-aware sequence:
1. **D1 JETIX-ARCHITECTURE-FINAL.md** (T-02) — meta-doc, но можно writing draft параллельно.
2. **D6 JETIX-FPF-LITE.md** — ontological foundation, blocks D3.
3. **D3 JETIX-ROLE-MANIFESTS.md** — role-manifest spec + template, blocks D7.
4. **D5 JETIX-KNOWLEDGE-ARCHITECTURE.md** — alphas + wiki + CRM, blocks D2.
5. **D2 JETIX-FOLDER-STRUCTURE.md** — finalized tree.
6. **D4 JETIX-VS-LIFE-OS.md** — Model D migration; independent.
7. **D7 JETIX-CAREER-LEVELS.md** — after D3.
8. **D8 docs/INSTRUCTIONS.md** — after all above, practical rollout.
9. **D9 decisions/2026-04-20-jetix-architecture-final.md** — meta, last.

### 6.2 Preliminary timeline

| D | Content | Estimated | Dependencies |
|---|---------|-----------|--------------|
| D1 | Architecture final (T-02, 12-15 pages) | 3-4h | None for draft |
| D6 | FPF-Lite (3-5 pages) | 2-3h | None |
| D3 | Role-manifests spec + 14 examples | 6-8h | D6 |
| D5 | Knowledge arch (wiki + alphas + CRM) | 5-6h | None |
| D2 | Folder structure | 2-3h | D3, D5 |
| D4 | Life-OS vs Jetix | 3-4h | None |
| D7 | Career levels | 3-4h | D3 |
| D8 | Instructions (14-day rollout) | 4-5h | D2, D3, D5 |
| D9 | Decision record | 1-2h | All above |

**Total: 29-39 hours** focused work ≈ 4-5 working days at 6-8h/day.

### 6.3 Post-deploy roadmap

After D1-D9 complete:
1. **14-day L1 Foundation rollout** (Days 1-14 из R2 §H.4) — execute.
2. **Role-manifest migration** (R3 §H.5) — 14 роль-manifest files, ~6-9 working days.
3. **Alpha state setup** — 6 Hybrid C alphas + 3 wiki-primary + 1 YAML-only.
4. **Q2 2026 Revenue execution** — first L4 клиент, pipeline generation.
5. **Phase 2 planning** — Sales Lead J3 hire description, filter-repo migration script testing.
6. **PRD for Jetix OS SaaS** (eventual platform product from L3) — horizon 2027+.
7. **Project revision** (Orientation Day Шаг 4) — 8 active projects review through new architecture lens.

---

## Appendix A: Source Citations Index

Major decisions → sources:

- **7-слойная архитектура (L0-L7)** → [v0.9 working-draft approved], [R3 §G Holacracy circles mapping], [R9 §B Berkshire/Constellation references for L7].
- **Model D Nested Hierarchy** → [R7 §E], [R6 §D5], [v0.9 §7].
- **10 alphas** → [R3 §D.1-D.10].
- **8-block role-manifest** → [R3 §C.1-C.9].
- **J0-JX Career Ladder** → [R1 §G.1-G.8].
- **Alpha storage Hybrid C** → [R4 §D.1-D.2, §H.2].
- **Event log hybrid (per-alpha + monthly)** → [R4 §D, R5 §C.1-C.7].
- **Markdown CRM schemas** → [R5 §B.1-B.5, §E.1-E.7].
- **Company-as-Code tool stack** → [R2 §H.1-H.10].
- **FPF-Lite** → [R3 §H.1].
- **Oxide RFD format** → [R2 §A.8, §F.3], [R8 §B.1].
- **Constitution §11** → [R8 §J.8].
- **SemVer major-only folders** → [R6 §D.2].
- **DACH regulatory triggers** → [R9 §A.6, §D.2-D.3], [R1 §B.3].
- **German invoice § 14 UStG** → [R5 §E.3-E.7].
- **Shape Up cycles** → [R2 §A.5].
- **14-day rollout** → [R2 §H.4].
- **Constellation "delegation to abdication"** → [R9 §B.2, §G.1].
- **Founder Mode preservation** → [R1 §C.2], [R9 §A.1].
- **Promptfoo + Langfuse dual** → [R2 §B.3, §D.1, §H.2].
- **Role ≠ executor** → [R3 §A.1, §F.7], [R8 §A.4 Holacracy].
- **Asymmetric reference rule (Life-OS→Jetix only)** → [R7 §D].
- **kebab-case universal** → [R6 §C.1, §D.10].
- **SOPS + age secrets** → [R2 §G.3].
- **Coolify deploy** → [R2 §G.4].
- **HippoRAG retrieval** → [R4 §A.3, §B.2].
- **Per-agent 5-layer memory** → [R4 §C.2].
- **50K context budget** → [R4 §H.3].

---

## Appendix B: Terminology Glossary

- **Alpha** — Essence Kernel concept (R3). Lifecycle entity with states, not data object or process. 10 core для Jetix.
- **Auftragstaktik** — Prussian mission-command doctrine (R1 §E.5). Role-manifest = Auftrag.
- **Betriebsrat** — German works council (R1 §B.3). Trigger: 5+ employees.
- **CAIO** — Chief AI Officer (R9 §A.4). Ruslan de facto до Phase 2c.
- **Claude Code** — Anthropic CLI tool. Primary execution environment для agents.
- **Company-as-Code** — Paradigm: company живёт в git repository as versioned text (R2 §A, R8 §A).
- **Diátaxis** — 4-form documentation framework (R2 §C.1): tutorials / how-to / reference / explanation.
- **DRI** — Directly Responsible Individual. GitLab convention (R8 §B.2).
- **Executor** — Role filler (AI agent, human, or system). Decoupled from role.
- **FPF** — First Principles Framework (Левенчук, R3 §B).
- **FPF-Lite** — Jetix-adapted 3-5 page version (R3 §H.1).
- **FPAR** — First-Pass Acceptance Rate. Quality metric для framing (R3 §H.4).
- **Geschäftsführer** — German Managing Director (R1 §B.3). Legal accountability role.
- **GoBD** — German audit/archiving standards (R5 §E.7). 10-year retention for invoices.
- **Graph of Creation** — ШСМ concept: directed graph with systems as nodes, creation relations as edges (R3 §A.3).
- **Hybrid C** — Alpha storage pattern: state.yaml + context.md + history.jsonl (R4 §D.1).
- **IHK** — Industrie- und Handelskammer (R1 §B.3). B2B access channel.
- **J0-JX** — Jetix Career Ladder levels (R1 §G.1).
- **Karpathy LLM Wiki** — Pattern (R4 §A.1): LLM as compiler/editor для markdown knowledge base.
- **Konsenskultur** — German consensus culture (R1 §B.3, R9 Part D).
- **L0-L7** — Jetix 7 layers + Executive Core.
- **MECE** — Mutually Exclusive, Collectively Exhaustive. Minto Pyramid method.
- **Mitbestimmung** — German co-determination (R9 §D.3). Trigger: 500+/2000+ employees.
- **Model D** — Nested Hierarchy для Life-OS vs Jetix (R7 §E).
- **Oxide RFD** — Request for Discussion format (R2 §A.8, §F.3).
- **Promptfoo** — Eval framework (R2 §D.1).
- **Langfuse** — OSS LLM observability (R2 §B.3, §D.1).
- **Rechnungsnummer** — Sequential invoice number required by § 14 UStG (R5 §E.4).
- **RFD** — Request for Discussion state machine: prediscussion → ideation → discussion → published → committed → abandoned.
- **Role-manifest** — 8-block YAML+Markdown role specification (R3 §C.1-C.9).
- **Shape Up** — Basecamp method, 6-week cycles + 2-week cool-down (R2 §A.5).
- **SKU** — Stock Keeping Unit. Productized service (AI Audit / Quick Win / Custom / Retainer).
- **SOPS + age** — Git-native encrypted secrets (R2 §G.3).
- **Steuerberater** — German tax advisor. Required for Jahresabschluss.
- **UG haftungsbeschränkt** — German limited liability company with €1 min capital (R9 Part H).
- **VSOP** — Virtual Stock Option Plan (R9 §H.2). Dominant German equity model.
- **ZUGFeRD 2.x** — German e-invoice standard (PDF/A-3 + XML). GoBD 2025 compliance.

---

## Appendix C: Metrics Index

Operational metrics defined in synthesis:

- **ARR (Annual Recurring Revenue)** — Phase gating metric (€50K Q2 2026, €300K Phase 2a trigger, €1M Phase 2b trigger, €50M+ Phase 3).
- **FPAR (First-Pass Acceptance Rate)** — % tasks accepted without rework. Target 80% mature (R3 §H.4).
- **Hallucination Rate** — <2%/week (R2 §E.2). SLO.
- **Tool-call Error Rate** — <1% per session (R2 §E.2).
- **Schema-failure Rate** — <0.5% per run (R2 §E.2).
- **Human-escalation Rate** — <5% of tasks (R2 §E.2).
- **Cost-overrun Rate** — <10% over budget (R2 §E.2).
- **Pipeline Velocity** — deals advancing per week.
- **Lead → closed-won Conversion** — >25% target sales-lead J3.
- **Avg Deal Cycle Time** — <30 days target.
- **On-Time Delivery Rate** — ≥90% delivery role.
- **Client NPS** — structured feedback, not questionnaire.
- **Revenue per Client** — €5-50K SKU range.
- **MRR (Monthly Recurring Revenue)** — Retainer €3-5K/mo × N clients.
- **Time in Alpha State** — e.g., lead <2 days target.
- **Agent Cost per Day** — budget per role-manifest.
- **Token Usage per Agent** — input/output tokens tracked via Langfuse OTel.
- **Context Window Utilization** — ~50K of 200K budget (25%).
- **Wiki Pages Growth Rate** — 50-100/month current.
- **Decision Record Count** — Oxide RFD total.
- **Postmortem Count** — blameless incidents per month/quarter.
- **Role Manifest Coverage** — % of 14 agents with role.md written.
- **Alpha Coverage** — all 10 alphas covered by ≥1 role (R8 Rule 10).
- **Lint Pass Rate** — 100% target (Rule from R8).
- **Span of Control** — ≤8 direct reports per role (R8 Rule 7).
- **Span of Control at Mega-corp** — Jensen Huang exception (60 direct reports).
- **Utilization Rate (billable)** — 75-85% consultants target (R1 §B.1).
- **Time-in-role per level** — J1→J2 1-2 years, J2→J3 2-3 years, etc. (R1 §A.1).
- **Retention Rate** — Alliance members.
- **IHK/VDMA Network Touchpoints** — Phase 2 metric.
- **Mittelstand Benchmark Dataset Size** — L6 horizon metric.

---

**END OF DEEP SYNTHESIS** — Stage 1 complete. Ready for Stage 2 multi-chat review.
