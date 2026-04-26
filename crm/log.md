<!--
CRM Activity Log
================
Append-only chronological log of CRM operations. Newest at top.
Auto-appended by `crm._scripts.crm` (add / touch / update / voice-route),
manually appended for major decisions / migrations. Header is in HTML
comment so the auto-prepend doesn't push it down.
-->

## 2026-04-26 02:47 — Smoke test (bootstrap)
  Verified add/show/touch/update/list/dash/rebuild-index pipeline end-to-end
  on `test-person` fixture. All 6 ops succeeded. Test fixture cleaned up
  (`rm crm/people/test-person.md` + `rebuild-index`). Bootstrap complete.

## 2026-04-26 02:38 — CRM bootstrap
  System bootstrap (cycle-10-crm-build). Initial state:
  - schema: roles.yaml (24 roles / 6 groups), statuses.yaml (13 statuses + stuck config),
    frontmatter.yaml (full JSON-Schema spec), strategy-hooks.yaml (6 offers + 6 asks)
  - templates: person.md (14 sections) + org.md
  - scripts: crm.py (CLI router) + frontmatter.py + strategy_hooks.py + views.py
    + index_builder.py + dashboard.py + voice_router.py
  - skills: 10 (/crm-add, /crm-show, /crm-list, /crm-search, /crm-touch, /crm-update,
    /crm-rebuild-index, /crm-dash, /crm-stuck, /crm-weekly)
  - tests: 35 (unittest) — frontmatter (12) + views (11) + index_builder (4) + strategy_hooks (8)
  - reference: people/example-person.md (committed reference template, paused)

  Total contacts in CRM at bootstrap: 1 (people: 1, orgs: 0).

  See `crm/README.md` for usage, `swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md`
  for full build packet.
