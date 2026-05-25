---
title: Phase 7 — Reference corporations doc-sets
date: 2026-05-25
type: phase-report
phase: 7
parent_prompt: prompts/jetix-full-map-and-docs-skeleton-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F3
G: jetix-full-map-and-docs-skeleton-phase-7
constitutional_posture: R1 surface only + R6 + R11; F3 reference general knowledge (NO new external research)
language: russian primary
---

# 🏛️ Phase 7 — Какие документы у нормальных корпораций

> **Что это.** Семь референсных организаций — какой минимальный набор документов у каждой,
> и какие паттерны универсальны, а какие специфичны для кооперативов. Это **общие знания**
> (F3), не новое внешнее исследование. Цель — baseline для скелета документов Jetix
> (Phase 8-9).

---

## §0 TL;DR

- **7 референсов:** Apple / Tesla / Mondragón / Berkshire / Equal Exchange + John Lewis (кооперативы) / OpenAI + Anthropic (deep tech).
- **Универсальный минимум** (есть у всех): vision/mission, product/service docs, financials, brand, legal/governance, operational/HR.
- **Кооперативная надстройка** (Mondragón/Equal Exchange/John Lewis): Charter/Statutes, member docs, wage-ratio policy, social fund rules, democratic governance records, exit/membership terms.
- **Deep-tech надстройка** (OpenAI/Anthropic): research papers, safety/governance frameworks, responsible-scaling policy, model cards, charter с миссией.
- **Вывод для Jetix:** мы = кооператив + deep-tech + методология одновременно (D-08 layered identity) → берём обе надстройки + методологический IP-слой.

---

## §1 Apple — продукт + бренд + операционка

Что характерно для Apple-типа (продуктовая корпорация premium):
- **Vision/Strategic:** годовой 10-K (annual report), proxy statement, environmental/supplier responsibility reports.
- **Product:** product roadmap (internal), Human Interface Guidelines (публичный design-стандарт), API docs (developer.apple.com), Tech specs per product, release notes/changelog.
- **Brand:** brand book / identity guidelines (строжайшие), marketing playbook, Keynote/launch scripts.
- **Operational:** supply chain SOPs, retail playbook, support knowledge base.
- **Legal:** patents portfolio, EULA/terms, privacy policy, App Store guidelines.

**Урок для Jetix:** строгий **brand book** + публичный **design/method guideline** (аналог HIG → наш «method canonical для людей») + чёткие **API/template docs** (наши Notion-шаблоны).

---

## §2 Tesla — миссия + платформа + R&D

Tesla-тип (mission-driven tech-платформа):
- **Mission/Strategic:** «Master Plan» (публичный стратегический манифест, part 1/2/3) — редкий жанр: публичная долгосрочная стратегия. Годовые отчёты, shareholder deck.
- **Platform:** vehicle/software specs, OTA changelog, energy products docs, Supercharger network specs.
- **Community:** referral program docs, owner's manual, community forums guidelines.
- **Financial:** quarterly shareholder letter + earnings deck, production/delivery numbers.
- **R&D:** patents (Tesla открыла часть патентов — «all our patent are belong to you» 2014), AI Day technical presentations.

**Урок для Jetix:** **публичный «Master Plan»** (мы это уже частично имеем — STRATEGIC-PLAN + EXECUTION-PLAN, но не для широкой публики) + **открытость части IP** (резонирует с D-13 open-surface/closed-core + jetix-ai-bios-moment open-standard).

---

## §3 Mondragón — кооперативное governance ⭐ (наш главный референс)

Mondragón (68 лет, 80K работников, €11B выручки, 5:1 wage cap, ~85-90% retention) —
**прямой прецедент R12 + Economic V10**:
- **Charter / Statutes:** Corporate Values + Basic Principles (10 cooperative principles), General Assembly bylaws.
- **Member docs:** membership agreement (вступительный взнос ~€15K исторически), capital account statements, member rights & obligations.
- **Wage policy:** wage solidarity ratio document (исторический 3:1 → 6:1, среднее ~5:1) — **прямой источник нашего Mondragón 5:1 cap**.
- **Governance records:** General Assembly minutes (1 member = 1 vote), Social Council records, Governing Council decisions.
- **Financial transparency:** inter-cooperative solidarity fund rules (10% прибыли в общий фонд — **источник нашего QF 10% skim**), reinvestment policy.
- **Education:** Mondragón University docs (кооператив включает свой университет — резонирует с нашим Education layer).

**Урок для Jetix (главный):** Charter с правами/обязанностями/выходом + **wage-ratio policy** (5:1) + **social fund rules** (10%) + **democratic governance records** (1-член-1-голос) + **education arm**. Почти всё это у нас уже спроектировано в Economic V10 / R12 / Education.

---

## §4 Berkshire Hathaway — capital allocation + governance

Berkshire-тип (holding/capital allocator):
- **Annual letter:** Buffett's Shareholder Letter (легендарный жанр — plain-language объяснение философии и результатов; **прямой стилистический референс для нашего PARTNER-OFFERING-HUMAN-LANG**).
- **Portfolio:** subsidiary list, capital allocation framework, acquisition criteria (публичные «what we look for»).
- **Governance:** owner's manual (Buffett's «Owner-Related Business Principles» — 15 принципов, как владелец думает о бизнесе — **прямой референс для нашего Charter + Pillar C Tier 1**).
- **Financial:** annual report, intrinsic value methodology.

**Урок для Jetix:** **plain-language annual letter** (наш будущий «годовой отчёт для партнёров») + **owner's manual / принципы** (у нас = Pillar C + Charter) + **acquisition/partnership criteria** (наши ICP 5 критериев из D-22 + 4 типа партнёров).

---

## §5 Кооперативы — Equal Exchange + John Lewis

**Equal Exchange** (worker-owned, fair trade):
- worker-owner handbook, patronage dividend policy, mission-lock (нельзя продать компанию — «poison pill» защита миссии — **резонирует с fork-and-leave + anti-extraction**).

**John Lewis Partnership** (employee-owned, UK):
- **Constitution** (публичная конституция партнёрства — 7 принципов, «happiness of all members»), Partnership Council records, bonus distribution policy, registrar/governance docs.

**Урок для Jetix:** **публичная Constitution** (наш Charter может быть публичным как у John Lewis) + **mission-lock** (защита от продажи/захвата — наш fork_prevention + R12) + **patronage/bonus distribution policy** (наш 75/25 + promoter bonus).

---

## §6 Deep-tech — OpenAI + Anthropic

**OpenAI:**
- Charter (публичный, про миссию AGI + «merge and assist» clause), research papers, model cards / system cards, usage policies, API docs.

**Anthropic:**
- **Responsible Scaling Policy (RSP)** — публичный governance-framework по уровням риска (ASL), **Constitutional AI** методология, research papers, model cards, **Core Views on AI Safety**, usage policy, Trust & Safety docs.

**Урок для Jetix:** **публичный Charter с миссией** (есть) + **safety/governance framework по уровням** (наш Halt-Log-Alert F2/F4/F8 + Stage Gates — структурно похоже на ASL уровни) + **research papers** (наши 5 research-deep'ов = аналог, но internal — можно curated subset наружу) + **«core views» документ** (наш FUNDAMENTAL / VISION).

---

## §7 Универсальные паттерны (есть у всех 7)

| Паттерн | Везде | Jetix-эквивалент |
|---|---|---|
| Vision/Mission/Strategy doc | ✅ | FUNDAMENTAL + STRATEGIC-PLAN + EXECUTION-PLAN |
| Product/Service docs | ✅ | Method V2 + Notion templates + Platform Lifecycle |
| Financials | ✅ | Economic V10 (но нет реальных statements — нет юрлица) |
| Brand/Marketing | ✅ | PARTNER-OFFERING (но нет brand book / лендинга) |
| Legal/Governance | ✅ | Foundation + FPF (но нет legal entity docs) |
| Operational/HR | ✅ | CRM + ROY roster (но нет HR/hiring docs) |

---

## §8 Кооперативно-специфичные паттерны (Mondragón/EE/JL)

| Паттерн | Источник | Jetix-эквивалент |
|---|---|---|
| Charter / Constitution (публичная) | Mondragón / John Lewis | Charter (текст не написан) |
| Member agreement + rights/obligations | все коопы | per-tier Charter (L4-L7) |
| Wage-ratio policy | Mondragón 5:1 | R12 Mondragón 5:1 cap ✅ |
| Social/solidarity fund rules (10%) | Mondragón | QF 10% skim ✅ |
| Democratic governance records | все коопы | DAO 1-член-1-голос (Phase 2+) |
| Exit / membership terms | EE mission-lock | fork-and-leave + RageQuit ✅ |
| Education arm | Mondragón University | Education layer + Workshop ✅ |

---

## §9 Deep-tech-специфичные паттерны (OpenAI/Anthropic)

| Паттерн | Источник | Jetix-эквивалент |
|---|---|---|
| Публичный Charter с миссией | оба | FUNDAMENTAL / VISION ✅ |
| Safety/governance framework по уровням | Anthropic RSP/ASL | Halt-Log-Alert F2/F4/F8 + Stage Gates ✅ |
| Research papers (публичные) | оба | 5 research-deep'ов (internal, curated subset наружу?) |
| Model/System cards | оба | (нет прямого эквивалента; ROY agent cards?) |
| Usage / Trust & Safety policy | оба | R12 + anti-cult discipline ✅ |
| «Core views» документ | Anthropic | FUNDAMENTAL + Method V2 ✅ |

---

## §10 Вывод для Jetix doc-skeleton

Jetix по D-08 — **три типа сразу**: кооператив (Mondragón) + deep-tech (Anthropic) +
методологический IP (уникально наш). Значит skeleton документов Jetix = **универсальный
минимум + кооперативная надстройка + deep-tech надстройка + методологический IP-слой**.

**Ключевое наблюдение:** бóльшая часть «правильных» документов у Jetix **уже спроектирована
в substrate** (Charter, 5:1, 10% fund, safety framework, education arm) — но не оформлена
в виде самостоятельных документов нужного жанра/аудитории. Task B's job — выписать эти
жанры как skeleton и показать, где substrate есть, а где дыра.

---

*Phase 7 closure. 7 референсов (Apple/Tesla/Mondragon/Berkshire/EE+JL/OpenAI+Anthropic) +
универсальные паттерны (6) + кооперативная надстройка (7) + deep-tech надстройка (6) +
вывод для Jetix. F3 general knowledge, NO new external research. R1 surface.*
