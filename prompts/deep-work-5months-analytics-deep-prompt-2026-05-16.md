---
title: Deep prompt — реальная аналитика Deep Work за последние 5 месяцев + темы + 2 mermaid
date: 2026-05-16
type: server-cc-trigger-prompt
status: ready-to-fire
target_executor: server CC (Plan Mode, autonomous 1-2h)
target_output: _DEEP-WORK-ANALYTICS-5MONTHS-2026-05-16.md (в корне репо, Antigravity-friendly)
language: russian
purpose: |
  Реальный честный отчёт за последние 5 месяцев (декабрь 2025 → май 2026): сколько Deep Work
  было в каждом месяце, какие основные темы засечены, breakdown по тегам (Tseren / Jetix-*
  domains / SOZD / OBR / PODG), сравнение с общим tracked временем. БЕЗ ПИЗДЕЖА — реальные
  числа из Toggl API + existing reports. Если данных нет за период — явно сказать «нет данных»,
  не extrapolate. 2 mermaid: monthly bar + themes breakdown.
F: F2
G: deep-work-analytics-applied-now
R: refuted_if_numbers_diverge_from_toggl_truth_OR_themes_misclassified
---

# 🎯 Deep prompt: Реальная аналитика Deep Work за 5 месяцев + темы + 2 mermaid

> **Как использовать.** Открой Claude Code на сервере с `--dangerously-skip-permissions`, paste этот файл как первый prompt. Autonomous 1-2h.

---

## §0 Контекст

**Руслан**, founder Jetix OS, Berlin. **Sole strategist** (Tier 2 R1).

Сегодня — **2026-05-16**. Нужен **честный отчёт** для:
- Self-orientation (где я реально тратил время)
- Discussion в L1 звонках (объективные числа, не "ощущения")
- Self-OS spec input (что система должна tracking'ать лучше)

**Принцип:** **БЕЗ ПИЗДЕЖА.** Если данных нет за период — явно сказать «нет данных за месяц X», не extrapolate / не make up. Если tracking density низкая — surface этот факт.

---

## §1 ЗАДАЧА

Создать **`_DEEP-WORK-ANALYTICS-5MONTHS-2026-05-16.md`** в корне репо с реальной аналитикой за **декабрь 2025 → май 2026** (5+ месяцев). Содержит:

1. **Honest monthly DW hours** — сколько часов Deep Work в каждом месяце
2. **Themes / domains breakdown** — какие темы в DW (по Toggl tags)
3. **DW vs other categories** — какая доля DW от total tracked
4. **Tracking density** — насколько честные данные (% дня logged)
5. **Notable patterns** — peak / dropoff / shifts (объективно)
6. **2 mermaid схемы:**
   - Mermaid 1 — monthly DW bar chart (5 месяцев)
   - Mermaid 2 — themes / domains breakdown (pie или sankey)

---

## §2 SOURCES — что подтянуть

### §2.1 Existing reports (прочитать первым)
- [reports/toggl_last6months_2025-11_to_2026-05.md](reports/toggl_last6months_2025-11_to_2026-05.md) — 6-month summary, 869.2h tracked, monthly breakdown есть
- [reports/toggl_historical_baseline_2024-04_to_2026-05.md](reports/toggl_historical_baseline_2024-04_to_2026-05.md) — 2-year baseline
- [reports/toggl_2026-05-03.md](reports/toggl_2026-05-03.md) — snapshot 03.05
- [reports/anton-call-report-2026-05-11.md](reports/anton-call-report-2026-05-11.md) — narrative context

### §2.2 Raw JSON в repo
- [reports/toggl_full_history_v2_2026-05-03.json](reports/toggl_full_history_v2_2026-05-03.json) — full history до 03.05
- `tools/toggl-entries-2026-05-*.json` — recent entries (06-07, 07-08, 08-10, 10-11, 12-13, 13-14, 14-15, 15-16)

### §2.3 Live Toggl API (если нужны свежие данные)
- `tools/fetch_toggl_v2_history.py` — fetch history
- `tools/toggl_history_analysis.py` — analytics tool
- Token: `~/.config/jetix/toggl_token` (mode 600)
- Window: **2025-12-01 → 2026-05-16** (5.5 месяцев)

**Если API limit / cache lag** — используй существующий full_history JSON + дополни свежими `tools/toggl-entries-*.json` через append.

### §2.4 Cross-reference: что строилось в каждом месяце
- Git log за каждый месяц для context («что было LOCKED / commit themes»)
- [reports/timeline-narrative-2025-07_to_2026-05.md](reports/timeline-narrative-2025-07_to_2026-05.md) — narrative context

---

## §3 OUTPUT FORMAT — `_DEEP-WORK-ANALYTICS-5MONTHS-2026-05-16.md`

### §3.1 Frontmatter

```yaml
---
title: Real Deep Work analytics — 5 месяцев (декабрь 2025 → май 2026)
date: 2026-05-16
type: time-analytics-report
status: ACTIVE
purpose: |
  Честный отчёт без приукрашивания. Реальные числа Deep Work / темы / tracking density / patterns.
F: F2
G: dw-analytics-applied-now
R: refuted_if_numbers_diverge_from_toggl_truth
prose_authored_by: ai-draft
sources:
  - reports/toggl_last6months_2025-11_to_2026-05.md
  - reports/toggl_full_history_v2_2026-05-03.json
  - tools/toggl-entries-2026-05-*.json
  - Toggl Reports API v3 (live fetch)
language: russian
window: 2025-12-01 → 2026-05-16
---
```

### §3.2 Структура контента

1. **§1 TL;DR** — 3-5 строк honest summary (peak / nadir / средний месяц / total DW / DW vs total)
2. **§2 Monthly breakdown table** (5+ months):
   - Month / DW hours / Total tracked / DW% / Tracking density / Notes
3. **§3 Themes / domains** — DW по tags:
   - Top tags (Jetix-foundation / Jetix-workshop / Tseren / SOZD / OBR / PODG / etc.)
   - Hours per tag (декабрь → май)
   - Какие domains появились / исчезли по месяцам
4. **§4 DW vs other categories** — table:
   - Сон / Рутина / Ебланил / DW / Спорт-Гулял-Зарядка / Отдых
   - Per month + 5-month total
5. **§5 Tracking density honesty**:
   - Сколько % дня logged в каждом месяце (24h baseline)
   - Где dropoff (March 2026 et al)
6. **§6 Notable patterns** — объективные:
   - Peak month + почему (cross-ref с repo commits / narrative)
   - Crash / dropoff months — surface факт, не диагноз
   - Sustained vs sporadic DW (consecutive days >Xh)
   - Долговременные шифты (Q1 → Q2)
7. **§7 Mermaid 1 — Monthly DW bar chart**:
   ```mermaid
   xychart-beta
       title "Deep Work hours per month (Dec 2025 → May 2026)"
       x-axis [Dec, Jan, Feb, Mar, Apr, May]
       y-axis "Hours" 0 --> ?
       bar [?, ?, ?, ?, ?, ?]
   ```
   (CC заполнит реальными числами)
8. **§8 Mermaid 2 — Themes breakdown** (pie или sankey по top 6-8 themes):
   ```mermaid
   pie title "DW themes — last 5 months total"
       "Jetix-foundation" : ?
       "Jetix-workshop" : ?
       "Tseren outreach" : ?
       ... etc
   ```
9. **§9 Honest commentary** — what numbers tell:
   - Где tracking честный, где нет
   - Что значит «March 53.9h» — disclaim что это может быть cache artifact
   - Не «должен был больше» — просто что было

### §3.3 Tier 2 R6 Provenance per claim
- Каждая цифра — со ссылкой на source: «toggl_last6months_2025-11_to_2026-05.md§Monthly breakdown» или «toggl_entries-2026-05-15-16.json:item-N»
- Если число вычислено — формула + intermediate values

---

## §4 CLASSIFICATION LOGIC — какие tags = Deep Work themes

**Deep Work project** в Toggl содержит entries с tags типа:
- **Action prefix:** SOZD (создание) / OBR (обработка) / PODG (подготовка) / RES (research) / ANL (analysis)
- **Domain:** Tseren / Jetix-foundation / Jetix-workshop / Jetix-corp / Jetix-FPF / video / outreach / monetization
- **Output:** doc / understand / decide / data
- **Energy:** обычный / flow / dim / усталый

Themes / domains — это **второй tag** (Tseren / Jetix-*). Group hours by это.

**Boundary case:** если entry имеет несколько domain tags — split hours между ними или attribute к dominant.

---

## §5 CONSTITUTIONAL DISCIPLINE

- **prose_authored_by:** ai-draft (это аналитика, не strategy)
- **Tier 2 R1** — surface numbers, не recommend / not «должен был X»
- **Tier 2 R6** — provenance per item (cite source)
- **R12 anti-extraction** — не extrapolate / не делать sample-based claims без disclaim
- **НЕ §РЕКОМЕНДАЦИИ** / **НЕ §ЧТО ДЕЛАТЬ** / **НЕ §МОИ ВЫВОДЫ**
- Только descriptive факты + observations + objective patterns

---

## §6 VERIFICATION ПЕРЕД COMMIT

1. **Все 5 месяцев** имеют ряд в monthly breakdown (даже если «нет данных»)
2. **Sum of monthly DW** = total DW (внутренняя consistency check)
3. **DW + other categories** ≈ total tracked (не overflow)
4. **Cross-ref:** number в §3.2 §2 (monthly table) matches §3.2 §7 (mermaid 1)
5. **Mermaid valid** — render через `/validate-mermaid` skill если доступен
6. **No API keys** в content (`grep -rE 'ANTHROPIC|sk-'`)
7. **All paths resolve** в file links

---

## §7 COMMIT + PUSH

```bash
git add _DEEP-WORK-ANALYTICS-5MONTHS-2026-05-16.md
git commit -m "[analytics] Real DW analytics 5 months (Dec 2025 → May 2026) — honest numbers + 2 mermaid

- Monthly DW breakdown (декабрь / январь / февраль / март / апрель / май)
- Themes breakdown по tags (Tseren / Jetix-foundation / Jetix-workshop / SOZD / OBR / PODG)
- DW vs other categories per month
- Tracking density honest disclosure (где dropoff)
- Notable patterns (peak / crash / sustained vs sporadic)
- Mermaid 1: monthly DW bar
- Mermaid 2: themes breakdown pie

Sources: toggl_last6months + full_history_v2 + recent toggl-entries-*.json + Toggl API v3 live"
git push origin main
```

---

## §8 SCOPE / TIME

- Ожидаемое время: **1-2 ч autonomous**
- Plan Mode подходит (data fetch + analysis + visualization)
- Если API недоступен → используй existing reports + recent JSON entries

---

## §9 ESCAPE HATCHES

- Если **нет данных за месяц X** → явно «нет данных. Возможные причины: cache lag / нет tracking / API window». Не extrapolate.
- Если **counts diverge** между sources → surface обе цифры + disclaim несоответствие
- Если **API rate limit** → fallback на static reports + дополнить recent JSON entries
- Если **classification unclear** для какого-то tag → list в §«Open classification questions»

---

## §10 ОЖИДАЕМЫЙ РЕЗУЛЬТАТ

После `git pull` Руслан получает:
- `_DEEP-WORK-ANALYTICS-5MONTHS-2026-05-16.md` (~300-500 строк + 2 mermaid)
- Открывает в Antigravity → читает honest numbers за 5 мес
- Используется в звонках с L1 (Дмитрий + следующие) как objective base
- Surface'ит patterns для Self-OS spec обогащения

---

*Создано 2026-05-16. Trigger для server CC autonomous Plan Mode execution. Constitutional anchor: AI = scribe / structurer / analyst, Ruslan = sole strategist. БЕЗ ПИЗДЕЖА — реальные числа из Toggl truth.*
