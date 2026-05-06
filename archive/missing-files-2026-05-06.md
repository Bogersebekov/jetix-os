---
title: Missing files report — canonical cleanup 2026-05-06
date: 2026-05-06
type: cleanup-audit
status: complete
parent_prompt: prompts/server-cc-canonical-cleanup-2026-05-06.md
parent_walkthrough: CANONICAL-WALKTHROUGH-2026-05-06.md
moved_by: canonical-cleanup-2026-05-06 (Ruslan walkthrough ack via 110-item checklist)
---

# Missing files report — canonical cleanup 2026-05-06

> Per Phase A verification of all paths in §1.1 (canonical), §1.2 (DEFER), §1.3
> (ARCHIVE) of the cleanup prompt. Records files that were listed in the prompt
> but did not exist on disk at execution time, plus name/date substitutions for
> unambiguous matches.

## §1 Truly missing (no close-name match — recorded only, no move)

| Listed in prompt | Category | Investigation result |
|---|---|---|
| `decisions/STRATEGIC-INSIGHT-TOP-LISTS-PARTNER-FACTORY-2026-04-26.md` | DEFER (§1.2 Strategic Insights #5) | Not present on `main` (anticipated per §8 obs O3 in prompt) — never committed; no action taken |
| `decisions/AWAITING-APPROVAL-fpf-enhancement-2026-04-23.md` | ARCHIVE (§1.3 Уровень 8 stale packets) | No file matches `*fpf-enhancement*` in decisions/; closest is `prompts/step-2-2-2-fpf-enhancement-scan-2026-04-23.md` (different intent — prompts/ is not in scope per §1.4) |
| `decisions/AWAITING-APPROVAL-wiki-v3-mechanics-2026-04-23.md` | ARCHIVE (§1.3 Уровень 8 stale packets) | No file matches `*wiki-v3-mechanics*` outside the canonical-archive `decisions/WIKI-V3-MECHANICS-2026-04-23.md` (which IS in §1.3 Уровень 4d ROY layer and was archived); the AWAITING-APPROVAL packet variant was never committed |
| `design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md` | ARCHIVE (§1.3 Уровень 8 stale packets) | Only `*-gate1-*` and `*-gate2-*` variants exist (both already in §1.3 list and were archived); no plain `wiki-v3-architecture` packet without gate suffix |
| `decisions/RUSLAN-ACK-WAVE-B-SUPPLEMENT-2026-04-27.md` | ARCHIVE (§1.3 Уровень 9 RUSLAN-ACK historical) | No file matches in decisions/; Wave-B supplement was likely ack'd via `decisions/AWAITING-APPROVAL-wave-b-supplement-2026-04-27.md` body or via subsequent BUNDLE-1 supplement chain (`RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-28.md` exists). No standalone Wave-B-supplement ack file |

## §2 Substitutions applied (unambiguous date/name typos in prompt → moved actual file)

| Listed in prompt | Actual file moved | Rationale |
|---|---|---|
| `decisions/AWAITING-APPROVAL-strategic-layer-templates-2026-04-30.md` | `decisions/AWAITING-APPROVAL-strategic-layer-templates-2026-04-28.md` | Date typo in prompt (-04-30 vs actual -04-28); only one file matches `strategic-layer-templates` pattern |
| `decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-30.md` | (KEPT in `decisions/`, NOT moved) | Date typo in prompt (-04-30 vs actual -04-28); EXCEPTION clause from §2 Phase D applies — verified state via frontmatter: `status: AWAITING-APPROVAL` + no corresponding RUSLAN-ACK file → KEEP active in decisions/ pending Wave 1.4 |
| `decisions/RUSLAN-ACK-WAVE-D-2026-04-28.md` | `decisions/RUSLAN-ACK-WAVE-D-INTEGRATION-PASS-2026-04-28.md` | Same Wave-D event; only one wave-d ack file exists (with `INTEGRATION-PASS` suffix per CLAUDE.md "Wave D Integration Pass" reference) |
| `decisions/RUSLAN-ACK-STRATEGIC-LAYER-BASELINE-2026-04-28.md` | `decisions/RUSLAN-ACK-STRATEGIC-LAYER-PHASE-1-BASELINE-2026-04-28.md` | Same Strategic Layer baseline event; CLAUDE.md references it as "Phase 1 Strategic Layer Templates ack" pointing to PHASE-1-BASELINE filename |

## §3 Items NOT in prompt list (left in `decisions/` per Tier 2 Rule 2 — no autonomous classification extension)

The following AWAITING-APPROVAL / RUSLAN-ACK files exist on disk but were NOT
classified by Ruslan in the 110-item walkthrough. They are LEFT IN `decisions/`
unchanged. Future cleanup cycle should include them in walkthrough scope.

- `decisions/AWAITING-APPROVAL-swarm-self-improve-gate1-2026-04-23.md`
- `decisions/AWAITING-APPROVAL-swarm-self-improve-gate2-2026-04-23.md`
- `decisions/AWAITING-APPROVAL-wave-d-integration-pass-2026-04-28.md`
- `decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-28.md` (kept active per §2 EXCEPTION)
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md`
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-28.md`
- `decisions/RUSLAN-ACK-STRATEGIC-LAYER-TEMPLATES-2026-04-28.md`

## §4 Discipline note

- Items in §1 are **logged only**, no archive action taken.
- Items in §2 substitutions are pragmatic 1-character/word typo fixes; only
  applied where the closest match was unambiguous (single candidate in repo).
- Items in §3 are explicitly OUT OF SCOPE per Ruslan walkthrough (not in §1.1,
  §1.2, §1.3 lists). Tier 2 Rule 2 forbids autonomous architectural classification
  extension; these stay where they are pending future ack.

## §5 Final move counts

- **DEFER moves:** 5 of 6 listed (TOP-LISTS-PARTNER-FACTORY missing per §1)
- **ARCHIVE moves:** 63 of 67 listed (4 truly missing per §1; 1 KEPT per §2 EXCEPTION; 4 substitutions resolved)
- **Append-only verified:** all moves via `git mv` (history preserved); frontmatter additions only add new fields, no deletions
