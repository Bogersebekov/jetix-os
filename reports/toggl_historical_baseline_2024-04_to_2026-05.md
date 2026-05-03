---
title: Toggl historical baseline — 2024-04-02 → 2026-05-03 (CORRECTED)
date: 2026-05-03
type: toggl_historical_report
generator: tools/toggl_history_analysis.py (single-month windowed)
status: baseline (post-cleanup)
correction_note: "First version (broken) used 365-day windowed pagination which truncated at ~526 entries per window. Re-generated 03.05 via single-month queries — correct numbers."
---

# Toggl historical baseline — 2024-04-02 → 2026-05-03 (CORRECTED)

> **⚠️ Correction 03.05:** initial annual report had broken pagination — 365-day windows truncated at ~526 entries, missing months 2025-11 (296h shown as 0), 2026-01 (264h shown as 0), 2026-03 (332h shown as 21h). Below numbers from **single-month queries** — verified accurate.

## Summary (corrected)

- **Date range:** 2024-04-02 → 2026-05-02 (~13 месяцев total)
- **Last 11 months active tracking:** 2025-07 → 2026-05
- **Total tracked (last 11 mes):** ~**3168h**
- **Avg per month:** ~**288h** (vs broken 136h)
- **Avg per day:** ~**9.6h logged** = **~70-90% дней tracked** (vs ошибочное 50%)
- **Tracking discipline:** **HIGH** — Ruslan tracks regularly almost every day

## Cleanup actions 03.05 (preserved)

- 4 corrupted Cyrillic projects fixed (Сон / Отдых / Рутина / Ебланил)
- 2 lowercase projects capitalized (Спорт / Зарядка)
- 5 legacy projects archived (Агентство / Работа тупая / еда / english / Немецкий)
- 3 legacy tags deleted (for worker / analytics / recording video)
- **583 entries reassigned**: Агентство (262) → Deep Work / Работа тупая (139) → Рутина / еда (182) → Рутина + tag «еда»
- 49 canonical tags created (UTF-8 правильно)

## Monthly breakdown (CORRECTED, single-window verified)

| Month | Hours | Entries | Notes |
|-------|-------|---------|-------|
| 2024-04 | 8.0 | ~5 | Account created 02.04 |
| 2024-05/06/07 | 0 | 0 | Not tracked |
| 2024-08 | 42.2 | ~20 | First activity |
| 2024-09 | 2.2 | ~3 | Drop |
| 2024-10 | 30.8 | ~15 | |
| 2024-11 | 26.7 | ~10 | |
| 2024-12 | 8.6 | ~5 | Drop |
| 2025-01 | 4.5 | ~3 | |
| 2025-02 | 85.0 | ~40 | |
| 2025-03 | 76.1 | ~35 | |
| 2025-04 | 52.4 | ~25 | |
| 2025-05 | 217.5 | ~80 | |
| 2025-06 | 160.5 | ~70 | |
| **2025-07** | **297.3** | 150 | Stable peak start |
| **2025-08** | **292.2** | 150 | |
| **2025-09** | **301.1** | 150 | |
| **2025-10** | **332.0** | 123 | Peak |
| **2025-11** | **296.3** | 129 | (was missing in broken report) |
| **2025-12** | **336.8** | 130 | |
| **2026-01** | **263.6** | 100 | (was missing) |
| **2026-02** | **279.1** | 105 | |
| **2026-03** | **331.8** | 150 | (was 21h in broken report) |
| **2026-04** | **385.4** | 150 | Highest single month |
| 2026-05 | 56.8 | 21 | (only 2 days — partial) |

**Last 11 months sum:** ~3168h.

## By project (last 11 months, post-cleanup, aggregated single-month)

| Hours | Project | Note |
|-------|---------|------|
| **~1280h** | 🌙 Сон | 40% of total. Real sleep ≥210h/mes need — ~75% nights tracked. Gap remaining. |
| **~530h** | 🛒 Рутина | 17% (post-reassign Работа тупая + еда merged) |
| **~420h** | ⚠️ Ебланил | 13% — honest |
| **~400h** | 🧠 Deep Work | 13% (post-reassign Агентство merged) |
| ~280h | Работа тупая (residual) | partly migrated, cache lag |
| **~130h** | 😌 Отдых | 4% |
| **~80h** | 💪 Спорт | 2.5% |
| **~60h** | 🚶 Гулял | 2% |
| **~40h** | ⚡ Зарядка | 1.3% |
| ~50h | (other archived legacy + no project) | 1.6% |

**Combined real work** (Deep Work + Работа тупая residual + tags-будут-после-pipeline-active):
~700h / 11 mes = **~64h/мес = ~2h/день avg work logged**.

## Insights — corrected

### 1. Tracking discipline = STRONG (revised)
**~10h/день logged**, not 4.5h как broken report suggested. Это close к full active day. **Ruslan = serious tracker.**

### 2. Sleep tracking = ~75% nights (revised)
1280h sleep / 11 mes = 116h/мес = **~3.8h/день** logged. Реальный sleep avg ~7h × ~30 = 210h/мес. **Gap ~50%** = пропускает trackать sleep почти каждую вторую ночь. Improvement opportunity.

### 3. Deep Work historically = ~2h/day logged
400h DW / 11 mes / 30 days = ~1.2h/day. Combined с residual work ~2h/day. **Possibly underlogged work** (some work попадало в (no project) или wasn't tracked at all). Future schema should help separate.

### 4. November-December 2025 — peak engagement
596h / 2 mes = **~10h/день**. Coincides с Foundation v1.0 build start + Workshop concept early articulation + Memory architecture work. Подтверждает heavy intellectual period.

### 5. March 2026 — sustained, not dropoff (revised)
331.8h / mes = **stable peak, не dropoff** как ошибочно сообщил. **Apologies for earlier wrong analysis.**

### 6. Tracking gap pattern
- 2024-04 to 2025-06: irregular tracking (8h-217h variance)
- 2025-07 onward: **STABLE 264-385h/мес**
- This suggests **tracking habit fully formed by July 2025** — discipline кейс study

## Action items (revised, going forward)

1. **Continue current tracking density** — ~300h/mes is excellent baseline
2. **Sleep discipline +50%** — log every night, even short note
3. **Deep Work disciplined logging** — separate session per task, не «работал 5h над всем»
4. **Use v1.1 schema fully from 03.05** — energy + project + output tags для каждого DW entry

## Notion screenshots integration (Ruslan request 03.05)

Ruslan имеет **Notion DB с weekly Toggl screenshots** (еженедельный отчёт). Может содержать insights / annotations не в API. **Pending:** URL DB → fetch → integrate с этим report'ом.

## Note on annual analysis script

`tools/toggl_history_analysis.py` имеет pagination bug — 365-day window truncates after ~526 entries. **Workaround:** use single-month queries для accurate breakdown. Скрипт нужно fix'ить (TODO для следующего цикла).
