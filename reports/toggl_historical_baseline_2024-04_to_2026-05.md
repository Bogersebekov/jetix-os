---
title: Toggl historical baseline — 2024-04-02 → 2026-05-03
date: 2026-05-03
type: toggl_historical_report
generator: tools/toggl_history_analysis.py
status: baseline (post-cleanup)
note: Captured AFTER 2026-05-03 cleanup (5 legacy projects archived, 3 legacy tags deleted, 583 entries reassigned to canonical projects)
---

# Toggl historical baseline — 2024-04-02 → 2026-05-03

> **Status:** baseline снимок после cleanup'а 03.05. Pre-cleanup всё было фрагментировано в 13 projects и 3 legacy tags.
>
> **Cleanup действия 03.05:**
> - 4 corrupted Cyrillic projects fixed (Сон / Отдых / Рутина / Ебланил)
> - 2 lowercase projects capitalized (Спорт / Зарядка)
> - 5 legacy projects archived (Агентство / Работа тупая / еда / english / Немецкий)
> - 3 legacy tags deleted (for worker / analytics / recording video)
> - **583 entries reassigned**: Агентство (262) → Deep Work / Работа тупая (139) → Рутина / еда (182) → Рутина + tag «еда»
> - 49 canonical tags created (UTF-8 правильно)

## Summary

- **Date range:** 2024-04-02 → 2026-05-02 (~13 месяцев)
- **Total entries:** 876
- **Total tracked:** 1769.6h
- **Untagged historical:** 98% (Ruslan почти не использовал tags до 03.05)
- **Account created:** 2024-04-02

## Tracking density / sustainability

- 1770h / 13 mes = **~136h/мес avg** (4.5h/день logged)
- Active hours/day типично 10-14h → **~50-65% дней tracking partial / отсутствует**
- Spikes (217h/мес 2025-05; 339h/мес 2026-04) и valleys (4.5h/мес 2025-01; 21h/мес 2026-03) — **paradoxical discipline** (либо много, либо забил)

## Monthly breakdown

| Month | Hours | Note |
|-------|-------|------|
| 2024-04 | 8.0 | Account created 02.04, тестовое использование |
| 2024-05/06/07 | 0 | not tracked |
| 2024-08 | 42.2 | первая активность |
| 2024-09 | 2.2 | спад |
| 2024-10 | 30.8 | |
| 2024-11 | 26.7 | |
| 2024-12 | 8.6 | спад |
| 2025-01 | 4.5 | dropoff |
| 2025-02 | 85.0 | подъём |
| 2025-03 | 76.1 | |
| 2025-04 | 52.4 | |
| **2025-05** | **217.5** | первый full-track month |
| 2025-06 | 160.5 | |
| 2025-07 | 87.5 | |
| 2025-08 | 77.4 | |
| 2025-09 | 97.1 | |
| 2025-10 | 115.5 | |
| 2025-11 | 0 | not tracked |
| **2025-12** | **136.9** | конец 2025 |
| 2026-01 | 0 | not tracked |
| **2026-02** | **136.6** | |
| 2026-03 | 21.0 | dropoff (что-то происходило?) |
| **2026-04** | **339.4** | пик активности (Foundation + Workshop work) |
| 2026-05 | 43.7 | только 2 дня (1.05 + 2.05) |

## By project (post-cleanup, 8 canonical + remaining legacy)

| Hours | Project | Note |
|-------|---------|------|
| **676.8h** | 🌙 Сон | 38% от total. Real sleep tracking ~25% дней. |
| **228.5h** | 🧠 Deep Work | post-reassign (включает Агентство migrated). Эта цифра вырастет когда cache reflects |
| **217.4h** | 🛒 Рутина | post-reassign (Работа тупая + еда merged) |
| **191.2h** | ⚠️ Ебланил | 11% — honest tracking of unproductive |
| 99.1h | Агентство (archived) | reassigned, но cache lag в reports |
| **90.7h** | 😌 Отдых | |
| **77.0h** | 💪 Спорт | |
| 59.7h | Работа тупая (archived) | partly reassigned |
| **36.0h** | 🚶 Гулял | |
| 25.8h | Немецкий (archived) | DW.UCH (учёба, archived per Ruslan 03.05) |
| 17.9h | еда (archived) | partly reassigned to Рутина |
| 17.9h | english (archived) | DW.UCH |
| 16.6h | (no project) | unattributed |
| **15.1h** | ⚡ Зарядка | |

## By tag (top historical)

| Hours | Tag | Note |
|-------|-----|------|
| 35.2h | еда | post-reassign tag added |
| (legacy untagged > 1700h) | | 98% untagged historically — schema not yet adopted |

**Future:** все entries from 03.05 onwards имеют **3 mandatory tags для DW** (energy + project + output) per `swarm/wiki/operations/time-tracking-categories.md` v1.1.

## Combined "real work time" (post-reassign view)

| Source | Hours | % total |
|--------|-------|---------|
| **Deep Work (post-reassign)** | 228.5h | 13% |
| Агентство (legacy work, archived) | 99.1h | 6% |
| Работа тупая (legacy, archived) | 59.7h | 3% |
| Немецкий + english (учёба, archived) | 43.7h | 2.5% |
| **Combined work** | **~431h** | **~24%** |

24% of tracked time = work. **17% sleep**. **Lower than expected** — суть в том что половина дней не tracked совсем (logged time = ~50% of real day).

## Insights

1. **Tracking discipline = key bottleneck.** Pikes-and-valleys pattern говорит — Ruslan tracks **когда вспоминает**. Pipeline 03.05 + voice→CC→Toggl flow должен решить — log entries прямо в moment без friction.
2. **Sleep undertrack catastrophic.** 51h/мес sleep = 1.7h/день avg = ~25% nights logged. Critical для self-knowledge.
3. **Deep Work historically diluted.** Часть DW попадала в Агентство / Работа тупая / Немецкий. Post-cleanup consolidated в Deep Work + DW.UCH (через tag UCH for учёба).
4. **No tag discipline.** 98% untagged → невозможно historical sub-direction analysis. Going forward — все DW entries have RES/OBR/SOZD/UCH/PODG/KOM + energy + project + output.
5. **2026-04 = peak month** (339h). Совпадает с Foundation v1.0 build + Workshop concept LOCKED + TRM model + Plan Mode pilot work. Подтверждает heavy intellectual work period.

## Next steps

- ✅ Cleanup completed 03.05
- ⏸️ AW Categories regex в web UI (manual)
- ⏸️ AW restart (manual)
- ⏸️ First end-to-end pipeline test (today's Tseren video session as test case)
- ⏸️ Track all 03.05 → 03.06 with full v1.1 schema
- ⏸️ После 4 weeks data — re-analyse new schema effectiveness
- 📋 Possible Phase 2: bulk pattern-based retag historical entries (e.g. all "Tseren" descriptions → tag Tseren)
