---
title: "§8 Membership / Invite Filter — Layer 6 Community Deep Dive"
type: integrated-synthesis
produced_by: mgmt-expert
mode: integrator
cycle_id: cyc-layer-6-community-deep-dive-2026-04-24
task_id: T-layer-6-community-deep-dive-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: proposed
template_level: true
confidence: medium
confidence_method: structured-rubric
provenance_inline: true
sources:
  - {path: "swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md", range: "§6.2 binding template-level directive"}
  - {path: "decisions/JETIX-VISION.md", range: "§7.2 D22 5-criteria filter; §4 Decision 16 Phase-1 simple chat"}
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md", range: "§2.3 Secure Network membership; §2.1 Phase-1 invite-only chat"}
acceptance_test: pass
---

# §8 Membership / Invite Filter

> **TEMPLATE LEVEL per Ruslan 2026-04-24** — structured skeleton ready for future iteration.
> Full Deep Dive deferred to L8 People deep-dive (Phase-2+ trigger per master-plan §4 Tier-2 backlog).

---

## §8.1 Phase 1 — Invite-only

**Механизм.** Руслан + warm-network introductions. Без формальных заявок — только личное знакомство или доверенная рекомендация от уже состоящего участника. Decision 16 закрепил Phase-1 чат как «простой, invite-based, 5-20 знакомых face-to-face». [src:decisions/JETIX-VISION.md#Decision-16]

**Капасити.** 5–20 участников. Разгоняться до десятков без валидированного сообщества — риск размытия качества до Phase-2+ gate.

**Анти-механика.** Нет форм, нет анкет, нет интервью — доверие достаточный фильтр на этом масштабе. Ценность инвайта в том, что он лично от Руслана или от уже принятого участника: reputation-backed, не process-backed.

**F-G-R.** F: F3 (наблюдение: тёплая сеть работает на 5-20 человек; за пределами нет data). ClaimScope: holds for Phase-1 solo Ruslan; NOT sufficient at Phase-2+ (Alliance 50+ members требует систему). R: рефутируется, если качество участников падает несмотря на инвайт-барьер; принимается, если за первые 3 месяца участники активны и вносят взнос.

---

## §8.2 Phase 2+ — Open application

**Механизм.** Форма-заявка + проверка по 5 критериям D22 (startupper mindset, предпринимательский азарт, stable, adequate, upward-direction) + финальное интервью. Критерии D22 — quality-gate, не income-floor: платёжеспособность (≥$5K/mo или ≥$10K one-shot) — фильтр способности платить, не членский ценз. [src:decisions/JETIX-VISION.md#§7.2] [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md#§2.3]

**Капасити.** 50–200 участников. Верхняя граница условная до появления данных о Dunbar-пределах субсетей.

**Триггер активации.** Post-€200K validation gate (D15). До этого Phase-1 инвайт-механика остаётся единственной точкой входа. Открывать раньше — риск overfill без инфраструктуры качество-gate.

**Детали TBD (§8.5).** Конкретные поля формы, формат интервью, право вето участников — см. §8.5 Open questions.

---

## §8.3 Rejection process — humane

**Тон.** Уважительный, краткий, без стыда. Сообщество quality-gated, но не элитарный клуб с унижением на входе — это anti-pattern для бренда Jetix.

**Паттерн.** «Сейчас не fit — вот конкретно почему; дверь остаётся открытой через N месяцев при X». Честная обратная связь лучше расплывчатого отказа: rejected кандидат понимает, что доработать, и возвращается с ростом.

**Stay-warm.** Периодические апдейты (newsletter, public content) — без спама. Rejected ≠ забыт; это потенциальный участник Phase-3+ или клиент consulting-офера.

---

## §8.4 Anti-spam / anti-toxic mechanics

**Спам-барьер.** Phase-1: инвайт-only — спаммеры не проходят по умолчанию. Phase-2+: reputation-based invitation (кандидата рекомендует действующий участник, несущий репутационный риск за рекомендацию).

**Toxic pattern.** 3-страйк правило: предупреждение → ограничение доступа → исключение. Эскалация к модератору на страйк-2. Исключение возможно; реабилитация — через повторное интервью не ранее чем через 6 месяцев. Детали протокола — Phase-2+ design.

**Контроль качества.** Phase-3+: peer-rating система (как именно — TBD; риск: рейтинги создают внутреннюю политику, нужен дизайн).

---

## §8.5 Open questions для Phase-2+ design

**Форма-заявка.** Какие поля? Минимум: архетип (из 11 D22), кейс применения AI, proof-of-skin-in-game. Максимум TBD — риск overengineering формы до первых 50 участников.

**Формат интервью.** Руслан проводит лично или делегирует? Видео или async-формат? Продолжительность (15-30 мин)? На ранних стадиях — вероятно Руслан лично; Phase-3+ delegate.

**Право вето участников.** Может ли действующий участник флагнуть проблемного кандидата до приёма? Механика флага TBD. Риск: злоупотребление флагом как инструментом конкуренции внутри сети.

**Scaling интервью.** При 200+ заявках в год — кто интервьюирует? Структура интервью-бота vs живого человека? Phase-2+ вопрос для отдельного решения.

---

## Примечание

TEMPLATE LEVEL per Ruslan 2026-04-24 — full Deep Dive деferred to L8 People deep-dive. Активируется при Phase-2+ trigger (€200K validation gate, D15) согласно master-plan §4 Tier-2 backlog. Текущий скелет достаточен для Phase-1 операций: инвайт-only, без лишней бюрократии.

[src:swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md#§6.2]
