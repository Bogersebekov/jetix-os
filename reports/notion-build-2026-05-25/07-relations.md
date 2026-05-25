---
title: Notion Build — Phase 7 Cross-layer relations
date: 2026-05-25
type: build-phase-log
phase: 7
status: DONE
---

# Phase 7 — Cross-layer relations (opt-in) ✅

Build script: `tools/notion_builder/builds/phase7_relations.py`. Resolves data-source
ids from the idempotency ledger (Phases 3-5).

## Built (idempotent — verified)

4 cross-layer **dual** relations (all OK):

| Source | Relation | Target |
|---|---|---|
| 🎯 L1 Goals | ↔ L3 Strategy & Goals | 🎯 L3 Strategy & Goals |
| ❓ L1 Hypotheses | ↔ L3 Hypotheses | 🧪 L3 Hypotheses |
| 📋 L2 Project Catalog | ↔ L1 Personal Project | 🚀 L1 Projects |
| 📅 L1 Daily Log | ↔ L3 Executive Briefing | 📊 L3 Executive Briefing |

Plus a 🔗 "Cross-layer connect (opt-in)" doc page on Layer 3 explaining the
opt-in posture + permissions recommendation.

## STANDALONE / privacy posture

- Relations are **additive opt-in links, never auto-merge**. One layer alone is unaffected.
- **Privacy invariant**: Life Pulse / Habits / Финансы (Layer 1) never propagate upward —
  red line, documented in the connect page and Permissions matrix.
- Founder sees both layers; other participants see only L3 / their L2 project. Actual
  per-page sharing is a UI step (Phase 12) — API can't set permissions/linked views.

## Verification

- All 4 relations report OK; idempotent re-run (relation_exists guard) → exit 0, no dupes.

## Mirror

`reports/notion-build-2026-05-25/notion-mirror/_cross-layer-relations.md`.
