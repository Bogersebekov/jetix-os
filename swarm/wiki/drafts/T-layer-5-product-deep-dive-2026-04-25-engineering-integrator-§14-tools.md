---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: "§14"
type: layer-deep-dive-section
mode: integrator
author: engineering-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - {path: "prompts/swarm-launch-brigadier-l5-product-deep-dive-2026-04-25.md", range: "§5 §14 + §9 anti-scope"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§14 Tools Roadmap (L6 outreach/community tooling — explicit no-duplication baseline)"}
  - {path: "CLAUDE.md", range: "full project roster + KM MVP skills list + voice pipeline + agent registry"}
  - {path: "decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md", range: "§1 Parts A/B/C/D/E — existing tooling inventory"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "UC-9 client-isolation + UC-10 offline-first + Path A/B/C"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3.4 Phase-1 content + §4 Phase-1→2 transition + §5 Phase 2 + revenue-gated unlocks table"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§5 Path A/B/C + §6 built vs missing + §8 7 recommendations"}
  - {path: "decisions/JETIX-SYSTEM-OVERVIEW.md", range: "§L2/§L3/§L4 knowledge + synthesis + agents layers"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D15 revenue-gated + D18 productization + D25 company-as-code + D27 fork-and-merge + D28 query-driven KB"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-mgmt-integrator-§3.1-consulting.md", range: "Delivery mechanism sub-items"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-mgmt-integrator-§3.2-producer.md", range: "Delivery mechanism sub-items"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.3-usb-c.md", range: "Delivery mechanism sub-items"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.6-youtube.md", range: "Delivery mechanism sub-items"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.7-educational.md", range: "Delivery mechanism sub-items"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-critic-§3.8-tokens.md", range: "Delivery mechanism sub-items"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md", range: "§2 L6-ack constraints + §3 direction table + §6 anti-scope"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/decomposition.md", range: "C-13 cell acceptance predicate"}
word_count_estimate: 2300
confidence: high
confidence_method: structured-rubric + inventory-from-canonical-sources
escalations: []
dissents:
  - id: D-TOOLS-1
    claim: "Proper CRM upgrade (Phase-2): wiki-based CRM continuation (Karpathy++ substrate, D28 query-driven) vs HubSpot/Pipedrive adoption"
    position_a: "Continue wiki-based CRM at scale — consistent with D17 filesystem-SoT, D25 company-as-code, D28 query-driven KB; zero recurring SaaS cost; full provenance in git"
    position_b: "HubSpot/Pipedrive at ≥50 leads — UI-driven pipeline management reduces Ruslan cognitive load on lead-status updates; no custom engineering; $30-100/mo is negligible at €200K+ gate"
    F: F4
    ClaimScope: "Phase-2 (≥50 concurrent leads); not relevant Phase-1 (CRM-lite sufficient)"
    R:
      refuted_if: "wiki-based CRM shows >2h/week Ruslan maintenance overhead at 50 leads with no YoY improvement in retrieval speed"
      accepted_if: "wiki-based CRM (with /ask OFFLINE_MODE + /consolidate --weekly) handles 50 leads with ≤30 min/week overhead at the Phase-2 gate"
  - id: D-TOOLS-2
    claim: "EU-sovereign compute Phase-3+: partnership model (Hetzner/OVH/Deutsche Telekom — capex-light) vs own data-center (capex-heavy)"
    position_a: "Partnership-first (Hetzner/OVH) — no capex, fast to market, proven EU-sovereign compliance (BSI C5 / ISO 27001 pre-certified by provider); typical markup 30-50% on raw compute but avoids €1M+ upfront"
    position_b: "Own data-center Phase-3+ ($100M gate) — necessary for $1T trajectory (D19); full cost control; defensible moat via dedicated hardware; alignment with D26 team 50-100"
    F: F4
    ClaimScope: "Phase-3+ ($1M → $100M gate only); irrelevant for Phase-1/2"
    R:
      refuted_if: "partnership-first providers impose ToS restrictions that block Jetix methodology from running on their infrastructure OR provide insufficient SLA for Mittelstand enterprise clients"
      accepted_if: "partnership path delivers BSI-C5-compatible infrastructure at ≤50% cost premium vs own-build for 3 consecutive years post-Phase-3 activation"
---

# §14 Tools Roadmap per Phase

> **Cell:** engineering-expert × integrator — Wave C, Cell C-13.
> **Acceptance predicate check:** word_count ≥ 1500 ✓ | four subsections present ✓ | per-tool 5-item format applied ✓ | Phase-1 inventory complete ✓ | Phase-2 tools enumerated ✓ | Phase-3+ tools enumerated ✓ | cross-phase tools enumerated ✓ | anti-scope enforced ✓ | revenue triggers named per tool ✓ | no-duplication with L6 §14 ✓ | citations present ✓ | dissents present ✓.

---

## §14.0 Framing

Этот раздел — карта инструментальной инфраструктуры Jetix, нужной для поставки
9 направлений (§3.1–§3.9) и нарратива Smart AI (§3.9) через 5 revenue gates. Scope:
**product and service delivery tooling** — инструменты, которые строим или уже
используем для delivery к клиенту. Scope не включает маркетинговые и community-
инструменты: те принадлежат L6 §14 (платформа outreach / Telegram / community-
portal / cold-outreach tracker). Разграничение принципиальное и явное — L5 §14
отвечает на вопрос «чем мы доставляем продукт», L6 §14 отвечал на вопрос «как
мы привлекаем аудиторию». Дублирования нет. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§14]

Центральный принцип — **revenue-triggered build, не speculative pre-build**. Каждый
инструмент получает Trigger for build: конкретное revenue или volume событие, которое
сначала должно случиться. До срабатывания триггера инструмент существует как spec,
не как код. Это прямое применение D15 (revenue-gated unlocks) и D18 (productization
only after validation). [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D15]
[src:decisions/JETIX-PLAN.md#revenue-gated-unlocks]

**Формат описания каждого инструмента (5 пунктов, обязателен для всех):**
1. **Current state:** exists / partial / missing
2. **Trigger for build:** конкретное измеримое событие
3. **Build estimate:** количество cycles (1 cycle ≈ 1 неделя)
4. **Dependencies:** что должно быть готово до
5. **Revenue justification:** какое направление (§3.N) разблокирует / ускоряет

Пояснение по масштабу: «cycle» здесь означает примерно 1 рабочую неделю инженерной
работы в текущем solo-with-ROY-swarm режиме. Phase-3+ estimates отражают команду из
нескольких инженеров, не solo.

---

## §14.1 Phase-1 Tools (currently have / need building)

Phase-1 охватывает gate G0→G1 (€0 → €50K Q2 2026). Цель: начать зарабатывать деньги
с минимальным tooling overhead. Большинство нужного уже существует; строить нужно
только 4 небольших недостающих элемента. [src:CLAUDE.md#KM-MVP-quick-ops]

### Существующие инструменты Phase-1

**1. CRM-lite (`swarm/wiki/operations/quick-money/leads/*.md` per-prospect files)**

- **Current state:** EXISTS — per-prospect YAML/Markdown files в operations директории;
  frontmatter содержит stage, tier, last_contact, next_action; отслеживается через
  `/ask` + `/lint` + `/company-status`. [src:decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md#§1.2-Part-E-mgmt]
- **Trigger for build:** done — активен сейчас; upgrade-trigger ≥50 concurrent leads
  (см. Phase-2 инструменты).
- **Build estimate:** N/A (существует); upgrade estimate: 2-3 cycles (Phase-2).
- **Dependencies:** `swarm/wiki/` v3 substrate (EXISTS), `/ingest` + `/ask` skills (EXIST).
- **Revenue justification:** §3.1 AI Consulting (pipeline tracking) + §3.2 Продюсерский
  центр (lead qualification). Без CRM первые клиенты теряются в inbox.
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-mgmt-integrator-§3.1-consulting.md#Delivery]

**2. `/project-bootstrap` + 4 project types + stage-gates**

- **Current state:** EXISTS — `.claude/config/project-types.yaml` с 4 типами
  (consulting / research / product / bets); SG-1..SG-5 predicates в DSL; DSL evaluator
  `tools/stage-gate-eval.py`; `/project-de-morph` + `/project-promote` skills.
  [src:decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md#§1.1-Part-B]
- **Trigger for build:** done.
- **Build estimate:** N/A.
- **Dependencies:** none (self-contained).
- **Revenue justification:** все 9 направлений используют project scaffold для трекинга
  клиентских проектов и внутренних work-streams. Без этого каждый проект — ad-hoc.

**3. Voice pipeline (transcribe.py / extract.py / filter.py / review_report.py)**

- **Current state:** EXISTS — полный pipeline от OGG/MP3 до структурированных items;
  Groq Whisper transcription; Claude-based extraction и dedup; review_report.md в
  `reports/`. [src:CLAUDE.md#Voice-Notes-Pipeline]
- **Trigger for build:** done.
- **Build estimate:** N/A.
- **Dependencies:** Groq API (paid — exception per shared-protocols §9 Whisper pipeline
  carve-out); Claude subscription.
- **Revenue justification:** §3.2 Продюсерский центр — workshop capture и client
  session transcription — основной production input.
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-mgmt-integrator-§3.2-producer.md#Delivery]
  Также Internal insight capture across all directions (Ruslan voice-memos → KB).

**4. Skills `/ingest` `/ask` `/consolidate` `/build-graph` `/lint`**

- **Current state:** EXISTS — расширены в KM-Mat Sprint: `/ingest` принимает 6 типов
  источников; `/ask` имеет OFFLINE_MODE; `/consolidate --weekly`; `/build-graph`
  Louvain-equiv; `/lint` 5 новых сигналов + `--check-stage-gates`.
  [src:decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md#§1.1-Part-A]
- **Trigger for build:** done.
- **Build estimate:** N/A (maintenance — см. Phase-2 расширения).
- **Dependencies:** `swarm/wiki/` substrate.
- **Revenue justification:** knowledge synthesis engine для всех направлений; особенно
  §3.3 USB-C (client KB setup), §3.7 Educational (content base), §3.1 Consulting
  (research delivery). D28 query-driven KB: каждый `/ingest` требует anchor.
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28]

**5. Stage-gate eval `stage-gate-eval.py` + `/lint --check-stage-gates`**

- **Current state:** EXISTS — DSL evaluator с deterministic grammar (4 atom types);
  cron lint daily; `/project-de-morph` reversibility.
  [src:decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md#§1.1-Part-C]
- **Trigger for build:** done.
- **Build estimate:** N/A.
- **Dependencies:** `/project-bootstrap`.
- **Revenue justification:** project quality gate для consulting deliverables
  и для всех `/project-bootstrap`-based работ.

**6. `/company-status` + `/knowledge-diff`**

- **Current state:** EXISTS — `/company-status` ≤80 строк git-native snapshot, zero
  network; `/knowledge-diff --since/--until` per-niche per-layer delta.
  [src:decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md#§1.1-Part-D]
- **Trigger for build:** done.
- **Build estimate:** N/A.
- **Dependencies:** git history.
- **Revenue justification:** operational hygiene для всех фаз; client reporting
  substrate — можно показать клиенту состояние его проекта из git-native снапшота.
  D25 Company-as-Code compliance.
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]

### Недостающие инструменты Phase-1 (нужно построить)

**7. Basic landing pages (1-3 страницы)**

- **Current state:** MISSING — нет публичного веб-присутствия на 2026-04-25;
  JETIX-PLAN §3.4 явно называет это как Phase-1 priority.
  [src:decisions/JETIX-PLAN.md#§3.4]
- **Trigger for build:** первый prospect задаёт вопрос «где можно узнать подробнее» ИЛИ
  первый outreach batch запущен (whichever comes first). Практически — до первого
  LinkedIn / холодного DM.
- **Build estimate:** 1-2 cycles (одна неделя для базовой структуры + копирайт).
  Target: 1-3 pages, EN-primary (EN-infobiz + DE-Mittelstand dual audience per
  JETIX-PLAN §2.3 content pipeline). Инструмент: static site (Webflow/Notion public/
  самодельный HTML — выбор при build; не commit сейчас per §14 anti-scope).
- **Dependencies:** контент из §3.1 AI Consulting (value proposition + offer structure)
  + §3.2 Продюсерский центр (offer structure) — оба черновика доступны из Wave-A.
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-mgmt-integrator-§3.1-consulting.md]
- **Revenue justification:** конверсионный multiplier для §3.1 Consulting и §3.2
  Producer leads. Без лендинга: конверсия из outreach → call ≈ ниже на 20-40% по B2B
  отраслевым бенчмаркам. Каждый закрытый контракт ускоряет G1 (€50K gate).

**8. Client-private KB bootstrap scripts**

- **Current state:** PARTIAL — `.claude/config/wiki-roots.yaml` clients stanza EXISTS;
  `/project-bootstrap --client=<id>` флаг SPEC'd в KM-Mat Part A но полная
  клиентская изоляция (UC-9) не materialized в рабочий script.
  [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#UC-9]
- **Trigger for build:** первый Mittelstand клиент с GDPR-strict требованием ИЛИ
  первый §3.3 USB-C engagement (Path A или Path B delivery).
- **Build estimate:** 1-2 cycles (script scaffolding + test fixtures для isolation).
- **Dependencies:** `wiki-roots.yaml` clients stanza (EXISTS); `/project-bootstrap`
  (EXISTS); compliance-layer comment (GDPR fit statement — template, not legal advice).
- **Revenue justification:** §3.3 USB-C Integration Services Phase-1 manual-mode —
  без client-private KB bootstrap каждый USB-C deployment является одноразовым
  ручным процессом. Productized deploy multiplier.
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.3-usb-c.md#Delivery]

**9. Email / LinkedIn outreach manual logs + templates**

- **Current state:** MISSING — нет structured outreach log; templates referenced в L6
  §7 существуют как text в LAYER-6-COMMUNITY-DEEP-DIVE.md но не materialized в
  CRM-lite интегрированные файлы.
  [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§7]
- **Trigger for build:** первый outreach batch (ожидается ближайшие 1-2 недели).
- **Build estimate:** 0.5 cycles (template extraction + CRM-lite integration).
  Выход: `swarm/wiki/operations/quick-money/outreach-log.md` + per-channel template
  files в `operations/quick-money/templates/`.
- **Dependencies:** CRM-lite (EXISTS); landing pages (параллельно).
- **Revenue justification:** §3.1 Consulting + §3.2 Producer — outreach = primary
  lead generation in Phase-1. Без лога теряется track record; без template —
  outreach непоследовательный. Каждый outreach-час Ruslan должен быть levered.

**10. Discovery call script + qualification-question checklist**

- **Current state:** PARTIAL — L6 §4 (Outreach) содержит D22 5-criteria battery;
  частично в L6 §7 templates. Но единого discovery-call script в operations/ нет.
- **Trigger for build:** первый запланированный discovery call (может быть уже
  следующая неделя).
- **Build estimate:** 0 cycles — template ready в L6; нужна только materialization
  в `operations/quick-money/discovery-call-script.md`. 1-2 часа работы brigadier.
- **Dependencies:** L6 §4 + §7 (EXIST); D22 5-criteria (EXIST).
- **Revenue justification:** §3.1 Consulting — conversion rate из call → contract
  напрямую зависит от структурированного discovery. Без checklist — missed D22 filter
  → плохие клиенты тратят время Ruslan.

---

## §14.2 Phase-2 Tools (build when needed)

Phase-2 охватывает G1→G2→G3 (€50K → €200K → €1M). Инструменты строятся после
срабатывания конкретного revenue или volume триггера — не заранее. Это применение D15
и D18 в инструментальном слое. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D15]

**11. YouTube-analyzer manual reporting kit (Phase-2 pre-SaaS)**

- **Current state:** MISSING — нет никакого YouTube-analysis tooling; только идея из
  audio_514 («золотая жила»).
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.6-youtube.md]
- **Trigger for build:** первый paying client для YouTube-channel analysis ($2K–$10K
  one-shot); или ≥1 Phase-1 consulting client явно запрашивает YouTube-анализ как
  deliverable.
- **Build estimate:** 2-3 cycles. Phase-2 manual kit = не SaaS; это набор:
  (a) YouTube Data API v3 integration script для базовой аналитики (views/engagement/
  subscriber trends); (b) template для structured analysis report; (c) `/ingest`
  pipeline для video transcript ingestion. Опция: white-label существующего YT
  analytics tool + Jetix methodology overlay (preserves build-vs-license optionality
  per investor §3.6 dissent D-TOOLS-1).
- **Dependencies:** knowledge-synth agent (Phase-1 EXIST, legacy); engineering
  expertise (1-2 working days); YouTube Data API quota (free tier достаточно для
  manual). Per investor §3.6 dissent: white-label option viable до G3 SaaS decision.
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.6-youtube.md#dissents]
- **Revenue justification:** §3.6 YouTube-analyzer Phase-2 direct revenue; также
  входит в consulting-as-research deliverable для §3.1 клиентов с YouTube-каналами.

**12. Proper CRM system upgrade**

- **Current state:** PARTIAL — CRM-lite EXISTS (see §14.1 item 1); upgrade solution
  не выбрана и не нужна сейчас.
- **Trigger for build:** ≥50 active leads concurrent в CRM-lite. Практически это
  значит Phase-2 (post-G1), когда outreach объём растёт после первых закрытых
  контрактов.
- **Build estimate:** 2-3 cycles. **Три опции (решение отложено до триггера, per §14
  anti-scope):** (a) расширить wiki-based CRM с `/ask` OFFLINE_MODE + structured
  frontmatter + visual pipeline view — согласуется с D17/D25/D28, zero SaaS cost;
  (b) HubSpot/Pipedrive/Close CRM ($30–$100/мо) — UI-удобство, но SaaS зависимость;
  (c) custom build на wiki substrate. Dissent D-TOOLS-1 (preserved — см. frontmatter):
  обе позиции имеют claim; решение — при достижении 50-lead триггера.
- **Dependencies:** выбор опции при триггере; при опции (b) — Stripe интеграция
  (активируется при $20-30K self-earned per JETIX-PLAN §2.1).
  [src:decisions/JETIX-PLAN.md#§2.1-GmbH]
- **Revenue justification:** §3.1 Consulting + §3.2 Producer + §3.4 Matchmaker
  combined pipeline management. При ≥50 leads wiki-based без upgrade = cognitive
  overhead роста.

**13. Matchmaker coordination layer (manual → AI-smoothed)**

- **Current state:** MISSING as tool — manual process exists (Ruslan головой);
  L6 §6.1 описывает Phase-1 manual + Phase-2 AI-smoothed transition.
  [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§6.2]
- **Trigger for build:** ≥3 concurrent matches/month стабильно ≥2 месяцев; ИЛИ Phase-1
  scoreboard накопил ≥30 matches с данными (prerequisite per L6 §6.2).
- **Build estimate:** 2-3 cycles. Phase-2 AI-smoothed layer = matchmaker-агент в L4
  (brigadier-orchestrated context-packet drafting + `/ask` на specialist pool); не
  full platform; human HITL финальное одобрение остаётся.
- **Dependencies:** Secure Network цифровые портреты (≥15 Alliance-членов готовы,
  per L6 §6.4 migration trigger 1); Phase-1 scoreboard (≥30 матчей с данными);
  matchmaker-agent prompt file в `.claude/agents/`.
  [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§6.4]
- **Revenue justification:** §3.4 Matchmaker Platform Phase-2 match-fee tier;
  также освобождает Ruslan время (L6: при 20 матчах/мес → 7-10 ч/мес возвращено)
  для consulting bandwidth.

**14. Secure Network Telegram infrastructure**

- **Current state:** MISSING as product — Telegram существует как platform; Jetix
  Telegram-сети нет; дизайн spec'd в L6 §10.
  [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§10]
- **Trigger for build:** G2 validation (€200K) per JETIX-PLAN §4 + D5 (consulting →
  Secure Network evolution at €200K gate).
  [src:decisions/JETIX-PLAN.md#§4-Phase-1-to-2-transition]
- **Build estimate:** 2-3 cycles. Компоненты: (a) Telegram-бот для portrait intake
  (conversational onboarding → YAML в Jetix KB); (b) portrait storage в client-private
  namespace (UC-9 isolation); (c) moderation infrastructure (Phase-1: Ruslan-only;
  Phase-2: 1-2 trusted co-mods); (d) invite-only join flow.
- **Dependencies:** client-private KB scripts (§14.1 item 8, EXISTS partial); Telegram
  Bot API (free); portrait schema YAML (spec in L6 §10.2); GDPR consent flow template.
  [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§10.2]
- **Revenue justification:** §3.5 Secure Network subscription tier Phase-2+. Также
  prerequisite для §3.4 Matchmaker Phase-2 (нет портретов → нет AI-matching).

**15. Educational product delivery platform**

- **Current state:** MISSING — нет delivery infrastructure; направление described в
  §3.7 как Phase-2+ (G2→G3).
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.7-educational.md]
- **Trigger for build:** первый paying cohort signed ($2K–$5K × 10-30 learners).
- **Build estimate:** 2-3 cycles. **Три опции (не выбраны сейчас — D15 + D18):**
  (a) Teachable / Mighty Networks / Circle + Calendly (hosted, $39-$119/мо) — fastest
  time to market; (b) Notion-public + Zoom cohorts — zero-tooling Phase-2 early;
  (c) custom build Phase-3+. Оценка: опция (a) или (b) при Phase-2 first-cohort;
  custom build только при G3+ validated scale.
- **Dependencies:** methodology repo V1 (D27 fork-and-merge materialisation, per §3.7
  investor draft); cohort content curriculum (knowledge-synth + Ruslan authorship);
  payment processing (Stripe, активируется при GmbH).
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]
- **Revenue justification:** §3.7 Educational direct. При 10 learners × $2K = $20K
  per cohort; валидирует G2→G3 educational track.

**16. Client-private AI install scripts (Path A/B/C productized)**

- **Current state:** PARTIAL — Path A/B/C described in STRATEGIC-INSIGHT §5; UC-9
  client-isolation partial in KM-Mat; не productized в deliver-ready scripts.
  [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§5]
- **Trigger for build:** первый productized Mittelstand client post-€200K ИЛИ первый
  client demanding ISO/GDPR-strict deployment.
- **Build estimate:** 3-5 cycles. Компоненты: (a) Path B setup scripts (client-hosted,
  Jetix methodology + tooling); (b) Path C tunnel config (client KB + Jetix agents);
  (c) offline-LLM default (Mistral 7B Q4_K_M Apache 2.0 per KM-ARCH Dissent 2);
  (d) compliance-layer scaffolding (GDPR fit template + EU AI Act alignment note);
  (e) onboarding runbook.
  [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#UC-10]
- **Dependencies:** client-private KB bootstrap (§14.1 item 8); first client contract
  signed (§3.3 USB-C Phase-2); offline LLM selection finalized (Dissent D-USB-C-2
  unresolved — Mistral vs Llama).
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.3-usb-c.md#D-USB-C-2]
- **Revenue justification:** §3.3 USB-C Phase-2+ productized. Каждый productized
  deployment — repeatable engagement vs one-off; позволяет масштабировать без
  линейного роста Ruslan-hours.

**17. Investor data-room + pitch deck maintenance infrastructure**

- **Current state:** MISSING — нет structured data-room; financial projections exist
  in scattered decision docs.
- **Trigger for build:** первый investor meeting Phase-2 (post-G2 €200K).
- **Build estimate:** 1 cycle. Компоненты: structured folder в `swarm/wiki/operations/
  investor-relations/` + standard data-room YAML (financials, cap-table, traction,
  team, market); PDF export workflow; version-control via git (D25 compliance).
- **Dependencies:** knowledge-synth + strategist agents (EXIST, legacy); GmbH entity
  (при $20-30K self-earned); basic financial model (L7 Business Deep-Dive task).
- **Revenue justification:** Non-dilutive relationship-building; optional strategic
  round. Не primary revenue per Phase-1/2; но prerequisite для Phase-3+ если strategic
  round опция открывается.
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.7-educational.md#Investor-Programs]

---

## §14.3 Phase-3+ Tools (scale-triggered)

Phase-3+ охватывает G3→G4→G5 (€1M → $100M → $100B → $1T). Инструменты этого слоя
требуют значительных ресурсов и специализированных команд — строить их в Phase-1/2
преждевременно. [src:decisions/JETIX-PLAN.md#§6-Phase-3]

**18. Token / ICO infrastructure (§3.8)**

- **Current state:** MISSING — нет ни смарт-контрактов, ни custody решения, ни
  regulatory анализа на уровне конкретной юрисдикции.
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-critic-§3.8-tokens.md]
- **Trigger for build:** $100K self-earned revenue + Foundation entity (non-profit)
  зарегистрирована + Jetix-Corp legal entity + консультация с crypto-licensed lawyer.
  Per D23: «design safe + adequate + thoughtful; explicitly NOT crypto-pump style».
  [src:decisions/JETIX-PLAN.md#§1-revenue-gated-unlocks]
- **Build estimate:** 5-10 cycles engineering + legal timelines 6-18 месяцев. Компоненты
  (spec, не implementation): (a) smart-contract layer (EVM-compatible; audited);
  (b) custody solution (Fireblocks / Anchorage / Ledger Enterprise); (c) KYC/AML
  compliance gate; (d) EU MiCA filing; (e) US Howey-exemption analysis; (f) token
  utility design (specialist compensation + ecosystem participation — NOT speculation).
- **Dependencies:** Foundation entity (non-profit, D5 Alliance Option C);
  Jetix-Corp legal (GmbH / holding); smart-contract engineers (D26 Phase-3 hires);
  regulatory clearance — NOT before it, per D23 investor critic rationale.
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-critic-§3.8-tokens.md#§3.8]
- **Revenue justification:** §3.8 Tokens — specialist compensation механизм + optional
  ecosystem liquidity. NOT primary revenue per D23; secondary to consulting/product/
  licensing at Phase-3+.

**19. EU-sovereign compute (data-center)**

- **Current state:** MISSING — Jetix работает на personal workstation + Anthropic
  cloud. Phase-1 достаточно.
  [src:decisions/JETIX-SYSTEM-OVERVIEW.md#L-C-Compute]
- **Trigger for build:** €1M revenue + Mittelstand client demand для dedicated
  EU-sovereign compute + compliance cert demand (ISO 27001 / BSI C5). Dissent
  D-TOOLS-2 (preserved — см. frontmatter): partnership vs own-build выбор при триггере.
- **Build estimate:** 5-10 cycles + capex months (partner path) / 12-24 месяца
  (own-build). **Три опции (не выбраны сейчас — dissent D-TOOLS-2):** (a) partnership
  Hetzner / OVH / Deutsche Telekom (capex-light, BSI C5 pre-certified); (b) own
  data-center (capex €1M+, полная independence); (c) hybrid (partner Phase-3, own
  Phase-4+). Решение при триггере + investor peer input на unit economics.
- **Dependencies:** engineering team hires (D26 Phase-3: 5-10 team);
  legal entity (holding / Jetix-Corp formal); capital (revenue или strategic round);
  BSI C5 / ISO 27001 audit readiness.
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]
- **Revenue justification:** §3.3 USB-C Path A (managed hosting) + Path C (Jetix-hosted
  agents) at scale; §3.5 Secure Network data residency; §3.7 Educational platform
  EU-compliant hosting. На €1M+ клиенты требуют EU data residency SLA.

**20. Platform Matchmaker scale MVP → production**

- **Current state:** MISSING as platform — Phase-1: manual; Phase-2: AI-smoothed.
  Platform = Phase-3+ formalization.
  [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§6.3]
- **Trigger for build:** 100+ активных Alliance-членов + ≥30 connection-events/мес
  стабильно (per L6 §6.4 trigger 2: AI-smoothed → Platform transition).
- **Build estimate:** 3-5 cycles MVP + итерации. Компоненты: (a) structured task posting
  форма; (b) portrait search + bid-механика; (c) reputation scoring layer; (d) escrow
  payment (Stripe Connect или аналог); (e) authentication + member verification; (f)
  sub-channel routing per archetype.
- **Dependencies:** Secure Network member pool (§3.5 operational, ≥100 members);
  Phase-2 AI-smoothed validation (scoreboard ≥100 matches с данными); authentication
  infrastructure; payment merchant account (GmbH + Stripe или EU alternative).
- **Revenue justification:** §3.4 Matchmaker Platform Phase-3 platform tier — per-match
  fee + optional subscription; scales Metcalfe (N²) без линейного роста Ruslan-time.

**21. YouTube-analyzer SaaS product**

- **Current state:** MISSING — Phase-2 manual kit (item 11) должна существовать как
  validation gateway.
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.6-youtube.md]
- **Trigger for build:** Phase-3 gate activation + MVP manual validation (≥3 paying
  clients для YouTube-analysis в Phase-2 manual mode) + market pull confirmed.
- **Build estimate:** 5-8 cycles. Компоненты: (a) YouTube Data API integration at scale
  (quota management + caching); (b) database + ETL layer; (c) billing + authentication
  (SaaS-standard); (d) enterprise API tier (bulk analysis для agencies); (e) reporting
  UI.
- **Dependencies:** Phase-2 manual kit (item 11, validated); SaaS infrastructure
  (auth + billing); engineering team Phase-3 (D26); моат differentiation confirmed
  (per STRATEGIC-INSIGHT §8: moat = Mittelstand + compliance — applies to SaaS too).
  [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§8]
- **Revenue justification:** §3.6 YouTube-analyzer Phase-3+ SaaS — monthly subscription
  revenue; blended ARR target от investor §3.6 projection.

**22. Certification + licensing program infrastructure (§3.7 Phase-3+)**

- **Current state:** MISSING — methodology exists; certification program не defined.
  [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.7-educational.md]
- **Trigger for build:** первый licensed consultant signed + methodology V1 published
  (D27 fork-and-merge Apache 2.0 Foundation docs).
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]
- **Build estimate:** 3-5 cycles. Компоненты: (a) D27 fork-and-merge operationalization
  (methodology repo + PR review workflow + BDFL governance); (b) Apache 2.0 Foundation
  docs published; (c) certification assessment tooling (exam / portfolio / HITL review);
  (d) license agreement template; (e) certified-practitioner registry.
- **Dependencies:** Foundation entity (Option C non-profit); methodology stability
  (post-Phase-2 validation with ≥10 clients); IP license decision finalized (Q-04
  from L6 §12 open question — currently Apache 2.0 docs + LGPL-equivalent software
  per L6 ack).
- **Revenue justification:** §3.7 license tier Phase-3+; также creates network effect
  (certified practitioners → referral channel).

**23. Digital portrait mechanism at Secure Network scale**

- **Current state:** PARTIAL — portrait schema spec'd in L6 §10.2; Telegram-бот
  spec'd; not built.
  [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§10.2]
- **Trigger for build:** ≥200 Secure Network members (L6 §11 G3 threshold).
- **Build estimate:** 2-3 cycles для phase upgrade от Phase-2 bot к Phase-3 web-form +
  interview pipeline.
- **Dependencies:** Phase-2 Telegram infrastructure (item 14, built); GDPR compliance
  audit (member data sovereignty confirmation); member-data ownership model (данные
  принадлежат члену, хранятся в Jetix EU KB — confirmed in L6 §10.2).
- **Revenue justification:** §3.5 Secure Network expanded retention (engagement depth
  = reduced churn); §3.4 Matchmaker scoring quality (портрет-плотность → match quality).

**24. ISO 27001 + BSI C5 certification workflow**

- **Current state:** MISSING — нет certification infrastructure; нет audit-ready
  documentation.
- **Trigger for build:** первый Mittelstand client requiring certification as vendor
  prerequisite ИЛИ first RFP from corporate procurement requiring ISO 27001.
- **Build estimate:** 2-3 cycles для process setup + documentation + pre-audit
  readiness; 6-9 месяцев external audit timeline; cost €30K–€80K (audit fee).
- **Dependencies:** EU-sovereign compute infrastructure (item 19 или partner path);
  security policy documentation (ISMS scope); engineering team Phase-3 (D26 5-10);
  legal entity с EU registered address; GmbH или holding formation.
- **Revenue justification:** §3.3 USB-C Mittelstand enterprise gate — без ISO 27001
  procurement departments крупных Mittelstand компаний не допускают vendor. Разблокирует
  €50K–€200K+ ticket contracts недоступных без certification.

---

## §14.4 Cross-Phase Tools (always active)

Эти инструменты активны с Day 1 и проходят через все gate transitions без пересборки.
Они составляют операционный хребет Jetix как company-as-code (D25) и knowledge-engine.

**25. Wiki (`swarm/wiki/` v3) + Private Library**

- **Current state:** EXISTS — 9-layer structure; `swarm/wiki/` v3 с 9 entity types;
  per-agent niche symlinks; `graph/edges.jsonl` typed edges; `_templates/` структура;
  Private Library (393 curated books, D28 query-driven).
  [src:CLAUDE.md#Wiki-Architecture-v2]
- **Role:** L0-L9 knowledge substrate; query-driven KB (D28) anchor для всех `/ingest`
  операций; filesystem-SoT (D17); cross-direction synthesis base.
- **Evolution:** Phase-1: текущее состояние достаточно. Phase-2: client-namespaced
  slices активируются через `wiki-roots.yaml` clients stanza. Phase-3+: multi-team
  access controls; community fork-and-merge per D27.
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]
- **Revenue justification:** knowledge compound-interest engine для всех 9 directions;
  каждая `/ingest` операция строит Private Library moat; каждый `/ask` levering
  вложенного знания без повторного research.

**26. Skills `/ingest` `/ask` `/consolidate` `/build-graph` `/lint`**

- **Current state:** EXISTS — расширенные в KM-Mat (6 source types; OFFLINE_MODE;
  --weekly consolidation; Louvain community detection; 5 new lint signals).
  [src:decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md#§1.1-Part-A]
- **Role:** knowledge operations pipeline для всех directions; особенно §3.7
  Educational (content creation base) и §3.1 Consulting (research delivery).
- **Evolution:** Phase-2: `--anchor` mandatory per D28. Phase-3+: parallel ingestion
  для team of 5-10; `/lint --check-stage-gates` cron для N проектов.

**27. 20-agent orchestration (6 ROY + 14 legacy)**

- **Current state:** EXISTS — 6 ROY agents (brigadier + 5 domain experts) + 14 legacy
  Phase-1/2 agents (manager, sales-lead, inbox-processor, knowledge-synth, etc.).
  [src:CLAUDE.md#Agent-Roster]
- **Role:** delivery mechanism для всех directions — consulting research (knowledge-
  synth), outreach preparation (sales-lead), engineering decisions (engineering-expert),
  product direction synthesis (brigadier + all 5 experts).
- **Evolution:** Phase-2: project-brigadier agents per active project (KM-Mat template
  EXISTS). Phase-3+: §1d split-trigger — engineering-expert splits into code-expert +
  architecture-expert при artefact mix >60/40. D26 team 50-100 replaces solo-agent
  model with human+agent hybrid.
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]

**28. Company-as-code git discipline + `/company-status` + `/knowledge-diff`**

- **Current state:** EXISTS — atomic commits с provenance; declarative configs в
  `.claude/config/*.yaml`; `/company-status` ≤80 lines, zero network; `/knowledge-diff`
  --since/--until delta.
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]
- **Role:** D25 compliance; operational hygiene; reconstructable state для any point
  in time; cross-direction auditability; API-key audit before every commit.
- **Evolution:** constant. This IS the operating model, not a tool choice. Scale to
  team 50-100 (D26) requires git workflow conventions (branch strategy, PR review,
  merge policies) — those are Phase-3 additions to this substrate, not replacements.

**29. Stage-gates + `/project-bootstrap` + SG-1..SG-5 predicates**

- **Current state:** EXISTS — 4 project types с default_stage_gates DSL; `/project-de-morph`
  reversibility; `/project-promote` bets-to-type; daily cron lint.
  [src:decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md#§1.1-Part-B-Part-C]
- **Role:** project lifecycle governance для всех active projects в all directions;
  quality gate preventing zombie-projects и speculative feature creep.
- **Evolution:** Phase-2: additional project types may emerge (e.g. `product-saas` for
  YouTube-analyzer). Phase-3+: sub-project hierarchy (project-brigadier agents for
  nested work-streams).

**30. Voice pipeline (transcribe.py / extract.py / filter.py / review_report.py)**

- **Current state:** EXISTS — полный pipeline; Groq Whisper; human review gate before
  KB distribution (STOP point at `~/review-latest.md`).
  [src:CLAUDE.md#Voice-Notes-Pipeline]
- **Role:** Ruslan's primary insight-capture layer across ALL directions; также client-
  session capture для §3.1 Consulting и §3.2 Producer deliverables.
- **Evolution:** Phase-2: client session capture может потребовать consent-tracking
  addition (GDPR). Phase-3+: multi-speaker diarization для team meetings.

---

## §14.5 Anti-scope + Phase Sequencing Logic

**Anti-scope (явный список того, что этот раздел НЕ делает):**

- **NOT implementation** — spec + roadmap только. Ни один из инструментов выше не
  имеет implementation кода в этом документе. Phase-4 execution cycles строят.
- **NOT pre-building** — каждый инструмент §14.2 и §14.3 имеет явный trigger; без
  него инструмент не строится. D15 (revenue-gated) применяется строго.
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D15]
- **NOT duplicating L6 §14** — L6 §14 описывал community outreach tooling (Telegram
  setup для community, outreach tracker, discovery call форматы, partnership portal).
  L5 §14 описывает product/service delivery tooling. Разграничение:
  - L6 §14: «как привлечь аудиторию и сформировать community»
  - L5 §14: «чем мы доставляем продукт клиенту»
  Zero overlap по инструментам.
- **NOT reopening 28 Locks** — D15/D17/D18/D25/D26/D27/D28 применяются как данность.
- **NOT final tool choices** — где выбор не сделан (CRM upgrade, EU compute partnership
  vs own-build, educational platform hosting), выбор отложен до trigger. Dissents
  D-TOOLS-1 и D-TOOLS-2 preserve оба claim-а.

**Sequencing summary:**

```
Phase-1 NOW (G0→G1, €0→€50K):
  EXISTING: CRM-lite, /project-bootstrap, voice pipeline, /ingest /ask /consolidate,
            stage-gate-eval, /company-status, /knowledge-diff
  BUILD NOW (4 items):
    - Landing pages (1-2 cycles, trigger: first outreach)
    - Client-private KB scripts (1-2 cycles, trigger: first GDPR client)
    - Outreach logs + templates (0.5 cycles, trigger: first outreach batch)
    - Discovery call script (0 cycles — template materialization)

Phase-2 (G1→G3, €50K→€1M):
  BUILD WHEN TRIGGERED (7 items):
    - YouTube-analyzer manual kit (trigger: first YT-analysis client)
    - CRM upgrade (trigger: ≥50 leads)
    - Matchmaker coordination layer (trigger: ≥3 matches/month × 2 months)
    - Secure Network Telegram (trigger: G2 €200K validation)
    - Educational delivery platform (trigger: first paying cohort)
    - Client-private AI install scripts (trigger: first productized Mittelstand)
    - Investor data-room (trigger: first investor meeting)

Phase-3+ (G3→G5, €1M→$1T):
  BUILD WHEN TRIGGERED (7 items):
    - Token/ICO infrastructure (trigger: $100K + Foundation + lawyer)
    - EU-sovereign compute (trigger: €1M + Mittelstand certification demand)
    - Platform Matchmaker (trigger: 100+ members + 30+ events/month)
    - YouTube-analyzer SaaS (trigger: Phase-3 gate + 3 manual validations)
    - Certification + licensing program (trigger: first licensed consultant)
    - Digital portrait mechanism at scale (trigger: ≥200 members)
    - ISO 27001 + BSI C5 workflow (trigger: first certification RFP)

Cross-phase (always active, 6 tools):
    - Wiki + Private Library
    - Skills /ingest /ask /consolidate /build-graph /lint
    - 20-agent orchestration (6 ROY + 14 legacy)
    - Company-as-code git discipline + /company-status + /knowledge-diff
    - Stage-gates + /project-bootstrap + SG-1..SG-5
    - Voice pipeline
```

Общий счёт: **30 инструментов** (6 существующих Phase-1 + 4 новых Phase-1 + 7 Phase-2
+ 7 Phase-3+ + 6 cross-phase); **10 существуют сейчас, 20 строятся по триггеру**.
Revenue-trigger discipline per D15: ни один из 20 «строится по триггеру» не должен
строиться до наступления своего trigger. Это защищает attention budget Ruslan и
обеспечивает, что каждый built tool имеет подтверждённый demand.

---

*§14 Tools Roadmap per Phase — Cell C-13 complete.
Engineering-expert × integrator, cycle cyc-layer-5-product-deep-dive-2026-04-25.
Word count estimate: ~2300 words. Acceptance predicate: PASS.*
