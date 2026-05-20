---
title: План дня — YYYY-MM-DD <day-of-week>
date: YYYY-MM-DD
day_of_week: <Monday/Tuesday/...>
type: plan-of-day
authored_by: ruslan / brigadier-scribe
trigger: <voice ack | reflection | etc>
constitutional_posture: R1 surface only + R6 + R11 + append-only
related: []
F: F2
G: plan-of-day
R: low
---

# 🎯 План дня — YYYY-MM-DD

## §0 Главная цель

> **<One-sentence primary objective for the day.>**

---

## §1 Контекст входа (start-of-day state)

**Substrate state:**
- <key relevant items from substrate>

**Pending inputs:**
- <items expected during day>

**SKIP:**
- <items explicitly out-of-scope today>

---

## §2 Шаги дня

### Шаг 1 — <name> ⭐ (P1)
- Action: <one-line>
- Output: <expected deliverable>
- Time: <estimate>

### Шаг 2 — <name> (P2)
...

---

## §3 Active Hypotheses (Layer 4 inline tracking)

> Per `hypotheses/active/` + `testing/` current focus (top 3-5).
> Updated via `/hypothesis-dash` integration.
> Layer 4 of 7-layer hypothesis architecture.

### Top 3-5 in-focus today
- **H-NNN** [<category>]: <one-line summary> — status: <status> — next: <next action>
- **H-NNN** [<category>]: <one-line summary> — status: <status> — next: <next action>
- ...

### Hypothesis ops planned today
- [ ] `/hypothesis-add <slug>` — surfacing «<idea>»
- [ ] `/hypothesis-update H-NNN --status testing` — initiate test of «<title>»
- [ ] `/hypothesis-close H-NNN --outcome ...` — close pending

### Closed last 7 days
- **H-NNN**: <outcome> — learning: <key insight>
- ...

### Attention budget
- Active + Testing: N / 20 (Pillar C §4.2 RUSLAN-LAYER cap)
- Status: ✅ healthy / ⚠️ approaching / 🛑 over

---

## §4 Risks / blockers

- <risk> → mitigation: <plan>

---

## §5 Wrap (end-of-day inline)

> Updated by Ruslan at EOD before `/close-day`.

- ✅ Completed: <what>
- ⏸️ Carried: <what for tomorrow>
- 🌱 Surfaced: <ideas / questions added к pool>
- 🧪 Hypothesis ops executed:
  - H-NNN created / updated / closed
- 📝 Compound learning extracted: <1-line>

---

## §6 Cross-refs

- Hypotheses inline (Layer 4): `hypotheses/docs/inline-daily-log-integration.md`
- Dashboard skill: `.claude/skills/hypothesis-dash.md`
- Build views: `.claude/skills/hypothesis-build-views.md`
- Plan-day skill: `.claude/skills/plan-day`
- Close-day skill: `.claude/skills/close-day`
