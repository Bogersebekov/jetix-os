---
title: "Tier 2 ruslan_layer_overrides — instance-specific MOC"
date: 2026-04-28
type: tier-2-ruslan-layer-overrides-moc
F: F2
G: "RUSLAN-LAYER overrides scaffold catalogue — pending Wave 1.4 review"
R: R-low
status: scaffold-pending-review
created_date: 2026-04-28
---

# Tier 2 ruslan_layer_overrides — instance-specific Tier-2 rules

Per-fork-instance Tier-2 system rules (Ruslan's Jetix instance specifics).
Wave 1 scaffolded as `scaffold-pending-review`; Wave 1.4 owner-driven per-file
migration determines final form (PROMOTE-AS-IS / REFACTOR / SPLIT / MERGE /
ARCHIVE / ESCALATE).

| # | Slug | Source (CLAUDE.md or other) | Wave 1 status |
|---|---|---|---|
| 1 | [no-api-key-exposure](no-api-key-exposure.md) | CLAUDE.md line 160 (Global Rule 6 origin) | scaffold-pending-review |
| 2 | [filesystem-source-of-truth](filesystem-source-of-truth.md) | CLAUDE.md line 159 (Global Rule 4 origin); D-17 derived | scaffold-pending-review |
| 3 | [language-discipline](language-discipline.md) | CLAUDE.md line 161 (Global Rule 7 origin) | scaffold-pending-review |
| 4 | [ab-test-gating](ab-test-gating.md) | CLAUDE.md line 162 (Global Rule 10 origin) | scaffold-pending-review |
| 5 | [path-protection](path-protection.md) | CLAUDE.md line 163 + line 358 (Правила item 6 origin) | scaffold-pending-review |
| 6 | [voice-pipeline-draft-only](voice-pipeline-draft-only.md) | CLAUDE.md line 164 + line 253 (CRM voice-integration discipline) | scaffold-pending-review |
| 7 | [voice-pipeline-manual-review](voice-pipeline-manual-review.md) | CLAUDE.md line 326 (Voice-Notes Pipeline СТОП-gate) | scaffold-pending-review |

## Sync invariant

Per Pillar C §B.2: scaffold count is fork-specific (instance-specific Tier-2
count varies per fork). Sync invariant lint-enforces match between this
catalogue + CLAUDE.md §4.2 inline + count-of-files in this directory.
