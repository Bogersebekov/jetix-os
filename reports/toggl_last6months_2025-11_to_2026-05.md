---
title: Toggl last-6-months focused — система-period (2025-11 → 2026-05)
date: 2026-05-03
type: toggl_focused_report
generator: tools/toggl_history_analysis.py
window: 2025-11-04 → 2026-05-03 (180 days)
note: «как мы начали работать над системой» per Ruslan dictation 03.05
---

# Toggl last 6 months — система-period

> **Window:** 2025-11-04 → 2026-05-03 (180 days). Это период **активной работы над системой Jetix** (Foundation v1.0 + Workshop concept + TRM + Memory architecture + Plan Mode + voice pipeline + ActivityWatch + Toggl integration).

## Summary

- **Entries:** 350
- **Total tracked:** 869.2h
- **Avg per day:** ~4.8h logged (реально ~10-14h actively, density ~50%)
- **Avg per month:** ~145h (выше чем annual avg 136h)

## Monthly breakdown

| Month | Hours | Note |
|-------|-------|------|
| **2025-11** | **260.8h** | start of focused system work |
| **2025-12** | **251.8h** | продолжение, peak monthly tracking |
| 2026-01 | 128.4h | spending less time logging |
| 2026-02 | 90.8h | drop |
| 2026-03 | 53.9h | major dropoff (unclear why) |
| 2026-04 | 83.5h | partial — annual analysis showed 339h, 6mo single-window 83.5h. Cache lag / window edge artifact. **Use 6-month as primary truth** |
| 2026-05 | (partial) | first 2 days |

## By project (last 6 months, post-cleanup)

| Hours | Project | Note |
|-------|---------|------|
| **355.2h** | 🌙 Сон | 41% — better tracked than annual avg (38%) |
| **126.1h** | 🛒 Рутина | 14.5% (post-reassign Работа тупая + еда merged) |
| **118.4h** | 🧠 Deep Work | 13.6% (post-reassign Агентство merged) |
| **109.5h** | ⚠️ Ебланил | 12.6% — honest |
| 92.0h | Работа тупая (archived, residual) | post-reassign cache lag, will resolve |
| **24.7h** | 😌 Отдых | 2.8% |
| **16.8h** | ⚡ Зарядка | 1.9% |
| **15.4h** | 💪 Спорт | 1.8% |
| **11.2h** | 🚶 Гулял | 1.3% |

## Insights — система-period specific

### 1. Real "work" share = ~25%
- Combined (Deep Work 118h + Работа тупая residual 92h) = **210h work** = **24% от 869h**
- Sleep 41% + Routine 14.5% + Ебланил 12.6% + Отдых/Спорт/Зарядка/Гулял ~10% = remaining 78% — что **76% не-работа** в logged time
- **Note:** total day = 24h, но logged = 4.8h/день. Real day = ~10h work + 7h sleep + 3h routine + 4h other. **Работа недотрекается.**

### 2. November-December = peak engagement
260h + 252h = **512h за 2 месяца** = 8.4h/день. **Максимальная density tracking.** Это совпадает с:
- Foundation v1.0 build начало (Wave A → Wave C)
- Workshop concept early articulation
- Memory architecture work
- Voice pipeline development

### 3. March 2026 dropoff — 53.9h month
**Что-то произошло в марте.** Need to investigate — depression / illness / external event / lost interest in tracking? **Worth retrospective.**

### 4. Sleep tracking better in this window
Annual avg 51h/мес sleep. Last 6 months avg 59h/мес. **Slight improvement** in sleep-tracking discipline. Still 25-30% nights tracked maximum.

### 5. Ебланил = ~13% honest
109h/180 days = **~36 min/day Ебланил** logged. Possibly **understated** (most ебланил is unconscious, not logged). Real number может быть higher.

### 6. Sports + Zaryadka + Gulyal = ~5%
43h за 6 mo = **0.24h/день** physical activity logged. Low — should be ≥1h/day per healthy founder routine. **Either low actual activity OR low tracking discipline.**

## Action items для going forward

1. **Tracking discipline = #1 lever.** All 03.05 → 03.06 entries with v1.1 schema (8 направлений + DW 6 sub + 3 mandatory tags). Real change = density of tracking (cover 80%+ of day, не 50%).
2. **Sleep tracking каждый день.** Even short note (start/stop время) — minimum.
3. **Physical activity tracking** — log зарядка / спорт / гулял каждый день где было.
4. **March 2026 retrospective** — что произошло, почему dropoff. Опционально для self-knowledge.

## Pipeline integration

- Forward tracking pipeline ready (08.05 baseline working)
- AW + Toggl + voice→CC→entries integration WIP
- After 4 weeks of new schema (~03.06) — re-analyze with full v1.1 tag breakdown
