---
title: "Voice Batch 15 — Phase 5: status researches + pending decisions (Situation Report Part 2)"
date: 2026-05-27
type: voice-batch-phase-report
batch: voice-batch-15
phase: 5
F: F3 (synthesis)
language: russian
status: complete
constitutional_posture: R1 surface only — решает Ruslan
---

# Phase 5 — Status research + pending decisions (что обсудить)

## A. Status parallel researches

### ✅ Founder-Role Research — ЗАВЕРШЁН (Phase 0→9)

- Commits `bb21296` (Ph0) → `8a752a8` (Ph9 final push). 9 phase-reports + 7
  mermaid + main `FOUNDER-ROLE-RESEARCH-2026-05-27.md` (46K).
- **Прямо отвечает на voice-batch-15.** Запись спрашивает «чем заниматься / кого
  брать / куда деньги» — research уже ответил:
  - чем: 5-6 из 13 функций (vision/метод/ценности/R&D/discovery/crisis), 7
    делегировать;
  - кого: #1 PM/Ops/CoS → #2 Communicator/EA → #3 Dev; advisor сейчас (~0 cost);
  - деньги: **не нанимать до cashflow+PMF** (premature scaling = #1 убийца) →
    base case бутстрап;
  - AI: берёт Preparation ~80%, человек держит Action+Transition.
- **R1 queue: 15 решений** (см. ниже B).

### ✅ Info-Security + Own-Infra Research — ЗАВЕРШЁН (Phase 0→7)

- Commits `2305a37` (Ph0) → `3719934` (Ph7 final push). 7 phase-reports + 6
  mermaid (SEC-1..6) + main `INFO-SECURITY-OWN-INFRA-RESEARCH-2026-05-27.md` (51K).
- Главное: угрозы скучные (нет offsite-бэкапа / ключи / голос в Groq); Build-
  спринт ~€20-30/мес 3-5 дней; «самая безопасная» = траектория не superlative;
  O-197 militant = reject; doctrine O-193 в Charter сейчас (дёшево).
- **R1 queue: 11 решений** (см. ниже B).

> **Вывод A:** ни один research не «not launched» — оба DONE. Handoff-doc 27.05
> не мог это verify; теперь подтверждено. Substrate для нового плана = полный.

## B. Pending R1 decisions — консолидация + приоритизация

Источники: founder §10 (15) + info-sec §10 (11) + batch-15 D15-1..4 + batch-14
4 held-back (resolved) + V4 §14 (~20-30) + workshop §11 (~10-15) + supplements.
**Всего в системе 80+** (handoff §9 tension #8). Ниже — НЕ все, а **gating для
28.05+**, по приоритету.

### 🔴 P1 — блокирует ближайшие 2-3 дня (решить первыми)

| # | Решение | Источник | Почему P1 |
|---|---|---|---|
| P1-1 | **Подтвердить переход O-160 операционно: ≤20% на substrate-build с этой недели** | founder §10.1 + D15-3 | ядро всего; без него план не сдвинется. Voice-batch-15 эмоционально это подтвердил |
| P1-2 | **Видео А: записать (грубо, не идеально)** | handoff §9.3 + founder §9 + BUILD-ARTEFACTS-SPECS | главный Build-блокер; спеки ✅, запись ❌ |
| P1-3 | **€34k — назначение** (найм vs подряд на фундамент vs runway-подушка) | D15-1 + founder §10.8 | voice: «завтра-послезавтра решаю»; tension с «не нанимать до cashflow» |
| P1-4 | **Tseren letter — polish + send** | handoff §5.1 | единственный external-ready артефакт; готов, не отправлен |
| P1-5 | **Doctrine O-193 в Charter** («не продаём базы / fork-and-leave») | info-sec §10.6 | дёшево, сейчас; это и есть «добавить в документы» из batch-14 voice |

### 🟡 P2 — эта неделя (важно, не блокирует завтра)

| # | Решение | Источник |
|---|---|---|
| P2-1 | Approve Build-P0 security-спринт (~€20-30/мес, 3-5 дней) | info-sec §10.3 |
| P2-2 | Day-job exit — trigger/runway-порог | D15-2 + O-200 + founder §10.8 |
| P2-3 | Express-метрика «≥1 артефакт наружу/неделя» как KPI | founder §10.12 |
| P2-4 | V4 #17 Security-pillar: α новое #17 / β sub-pillar #2+#8 / γ концепт | info-sec §10.1 + V4 |
| P2-5 | Команда #1 (PM/CoS) — триггер «пора»? | founder §10.2 |
| P2-6 | whisper.cpp local (голос из Groq → локально) | info-sec §10.4 |
| P2-7 | «Митя»/Kaiser disambig + созвон по юр+тех фундаменту | Q15-3 + O-204 + A15-1 |

### 🟢 P3 — backlog (после Build-фазы)

founder §10: co-founder (5), компенсация-дефолт (7), revenue-стрим выбор (9),
«Китай»-сканер (10), founder-skills (11), Build-exit чеклист (13), месячная
рефлексия (15). info-sec §10: O-194 Scale-горизонт (7), on-chain R12 timing (8),
infra-steward role (9), B2G-Germany (11). + Strategic Reflection prose D14-1/D14-4.

### Held-back batch-14 (статус)

4 held-back items (security pillar / strategic prose / O-197 reframe / Kaiser
disambig) — per handoff «resolved в 27.05 plan», КРОМЕ Kaiser disambig (всё ещё
open → P2-7) и O-197 reframe (подтверждено info-sec §10.10 reject).

## C. Что обсудить (variants + trade-offs + вопросы для ack)

### Главная напряжённость: €34k сейчас vs «не нанимать до cashflow»

- **Voice-batch-15:** «€34k обязан закидывать → команду брать завтра».
- **Founder-research:** premature scaling (найм до cashflow+PMF) = #1 убийца
  ресурсов; пока solo+AI burn≈0, runway растёт.
- **Варианты разрешения (surface, не выбор):**
  - **(a)** €34k → НЕ штатный найм, а **точечный подряд** на юр+тех фундамент
    (O-204) — закрывает «делегирование bottleneck» без premature scaling;
  - **(b)** €34k → **runway-подушка** для day-job exit (O-200) → больше времени
    на promotion (что и есть bottleneck);
  - **(c)** €34k → **инструменты/инфра/Build-спринт** (info-sec ~€20-30/мес = год
    за <€400);
  - **(d)** комбо a+b+c с распределением.
  - ⚠️ Чистый «нанять штат сейчас» = прямой конфликт с research. Surface, решаешь ты.

### Вторая: скорость инвесторов vs foundation-first

- Voice: «инвесторов вызывать максимально быстро». Но сам же: «перед этим
  фундамент жёстко проработать». Research + O-203 согласны: **foundation-readiness
  = gate**. Конфликта по сути нет — это sequencing, не выбор.

### Конкретные вопросы для ack

1. P1-1: подтверждаешь ≤20% substrate-build с этой недели? (да/нет/%)
2. P1-3: €34k — вариант (a)/(b)/(c)/(d) или свой?
3. P2-2: day-job exit trigger — какой runway-порог (мес расходов)?
4. Q15-3: «Митя» = Дмитрий Кайзер или другой человек?
5. P2-4: Security-pillar — α/β/γ?

→ Phase 6: SITUATION REPORT main + plan substrate (28.05+).
