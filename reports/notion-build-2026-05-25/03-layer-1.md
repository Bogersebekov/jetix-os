---
title: Notion Build — Phase 3 Layer 1 Personal Core
date: 2026-05-25
type: build-phase-log
phase: 3
status: DONE
---

# Phase 3 — 🟢 Layer 1 Personal Core ✅

Build script: `tools/notion_builder/builds/phase3_layer1.py`. Provenance: v2 spec
`reports/notion-templates-3-layers-architecture-v2-2026-05-25/03-layer-1-personal-core-revised.md`.

## ⚠️ Major discovery mid-phase: Notion API 2025-09-03 "data sources" model

The installed `notion-client` defaults to API version **2025-09-03**, in which a
**database is a container** and its schema lives on a separate **data source**.
Consequences (all now handled in the module):

- `databases.create(properties=…)` and `databases.update(properties=…)` **silently
  drop** the schema (no error). Properties MUST be written via
  `initial_data_source={"properties": …}` on create and `data_sources.update(…)` after.
- **Relations target a `data_source_id`**, not a database id.
- Caught only because Phase 3 verification read the data source back and found only
  the title property — a reminder that fail-loud verification matters.

Module refactor (committed): `client.create_database` uses `initial_data_source`;
new `update_data_source` / `data_source_id` / `ds_id_of`; `db_create.relation`
targets data sources; `idempotency.find_or_create_database` returns
`(db_id, ds_id, created)` + a **smart reconcile** that renames the title property
and merges non-title props (stripping select option colors, since Notion forbids
changing an existing option's color). 21 unit tests pass.

## Built (idempotent — verified)

**11 databases** (full schemas on data sources):

| DB | Title prop | Notable |
|---|---|---|
| 📅 Daily Log | Date | Цель дня, Реально сделано, Energy, Deep work minutes, Day type(4) + 5 relations |
| 🚀 Projects | Name | Type/Status/Checkpoint/Priority/Last touched/Notes + **Stuck? formula** + Linked goals |
| ✅ Tasks | Name | Status/Priority/Due + Project relation |
| 💡 Ideas | Name | Maturity/Domain/Promote to/Note |
| 🤝 Contacts | Name | Type/Status/Last touch/offer/ask + **Reconnect? formula** |
| 📚 Knowledge | Name | Kind/Status/**Saved-for-later**/Key takeaway/Domain |
| ❓ Hypotheses | Statement | Confirm/Refute/Status/Confidence + Linked projects |
| ❤️ Life Pulse | Date | Energy/Sleep hours/Mood/Movement (private) |
| 🔁 Habits | Name | Cadence/Target/Area/Active/Notes + Daily Log & Goals relations |
| 💰 Финансы | Name | Type/Amount(euro)/Date/Category (opt-in, private) |
| 🎯 Goals | Name | Horizon/Metric/Target/Due/Status/Why (under Strategy page) |

**9 intra-layer relations** (all OK): Daily Log → Projects/Contacts/Hypotheses/Ideas/Habits
(dual — reverse props auto-created); Projects → Goals; Tasks → Projects; Hypotheses →
Projects; Habits → Goals.

**2 formulas** (both OK): Projects `Stuck?` (active + >14d untouched → "⚠️ застрял"),
Contacts `Reconnect?` (active + >30d → "📵 пора связаться").

**Pages:** 🧭 Стратегия (Vision / Точка А→Б / Философский лист / 🎯 Цели doc + Goals DB),
🔄 Шаблоны ревью (Day template / Weekly / Monthly), 🔧 Что можно ещё добавить (sidebar).

**Views:** 28 recommended views captured as in-page **instruction toggles** (11) + mirror
(API cannot create views — platform limitation, see Phase 10 GAP).

## Verification

- Data sources read back with full correct schemas + renamed titles (Date/Statement/…).
- Idempotency: re-ran build → exit 0, no errors, child_database count stable at 10 (+Goals).

## Mirror

`reports/notion-build-2026-05-25/notion-mirror/layer-1/*.md` (per-DB) + `_overview.md`.
