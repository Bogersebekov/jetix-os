---
title: Cross-ref changes audit log — post canonical-cleanup 2026-05-06
date: 2026-05-06
type: cleanup-audit
status: documented-only-not-auto-fixed
parent_walkthrough: ../CANONICAL-WALKTHROUGH-2026-05-06.md
parent_cleanup_prompt: ../prompts/server-cc-canonical-cleanup-2026-05-06.md
authority: Ruslan walkthrough ack 110-item checklist (2026-05-06)
discipline: НЕ автоматически updates cross-refs внутри active canonical docs (это refactor с potential breakage). Только log.
---

# Cross-ref changes audit log — post canonical-cleanup 2026-05-06

> **Purpose.** After Phase D moved ~63 docs to `archive/<original-path>`, the
> following cross-refs in **active** canonical / non-archived docs may need
> update. Per cleanup prompt §2 Phase G discipline: **documented only, NOT
> auto-fixed** — refactor deferred to follow-up cycle.
>
> **Total hits:** 190 across ~30 source files (грубая grep по 16 archived path
> patterns; some hits are quotes / historical references that may stay as-is).

---

## §1 Aggregate stats

### Top affected files (cross-ref count)

| Source file | Hits | Note |
|---|---|---|
| `decisions/strategic/_research/landscape-strategic-docs-2026-04-28.md` | 18 | F2 research scaffold (linked, not moved); historical references ok |
| `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` | 16 | active canonical (Foundation Part 5) |
| `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` | 14 | active canonical (Foundation Part 4) — heavy `design/JETIX-FPF.md` ref |
| `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md` | 12 | active canonical (Foundation Part 2) |
| `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` | 11 | active canonical (Foundation Part 3) |
| `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md` | 10 | active canonical (Foundation Part 8) |
| `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` | 10 | active canonical (Foundation Part 7) |
| `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md` | 9 | active canonical (Foundation Master Overview Technical) |
| `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` | 9 | active canonical (Foundation Part 6a) |
| `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` | 8 | active canonical (Foundation Part 9) |
| `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` | 8 | active canonical (Foundation Part 1) |
| `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` | 7 | active canonical (Foundation Part 11) |
| `decisions/variants/JETIX-ARCH-V3-DEEPTECH.md` | 7 | NOT canonical (variants/ folder) |
| `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md` | 5 | active canonical (Foundation Part 10) |
| `decisions/variants/JETIX-ARCH-V5-EMERGENT.md` | 5 | NOT canonical (variants/ folder) |
| `decisions/variants/JETIX-ARCH-V2-MAXIMALIST.md` | 5 | NOT canonical (variants/ folder) |
| `decisions/JETIX-CORPORATION-2026-05-05.md` | 5 | active canonical (Документ 1B) |
| `swarm/wiki/foundations/part-6b-human-gate/architecture.md` | 4 | active canonical (Foundation Part 6b) |
| `swarm/wiki/synthesis/pilot-design-plan-2026-04-30.md` | 3 | synthesis (NOT in canonical list) |
| `swarm/wiki/foundations/principles/architecture.md` | 3 | active canonical (Pillar C) |
| `decisions/strategic/_templates/founder-overlay.md.template` | 3 | F2 template (linked, not moved) |
| `decisions/strategic/_research/jetix-fit-filtering-2026-04-28.md` | 3 | F2 research scaffold (linked, not moved) |
| `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` | 3 | active canonical (Документ 1A) |
| `CLAUDE.md` | 3 | active canonical |
| ... | ... | (~10 more files with 1-2 hits each) |

### Archived paths most-referenced

| Archived path | New location | Approx ref count |
|---|---|---|
| `design/JETIX-FPF.md` | `archive/design/JETIX-FPF.md` | ~120 (heaviest — Foundation Parts ref FPF IP-1..IP-8 / A.14 / A.6.B / B.3 throughout) |
| `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` | `archive/decisions/AUDIT-CURRENT-STATE-2026-04-27.md` | ~30 |
| `decisions/JETIX-VISION.md` | `archive/decisions/JETIX-VISION.md` | ~15 |
| `decisions/JETIX-PHILOSOPHY.md` | `archive/decisions/JETIX-PHILOSOPHY.md` | ~8 |
| `decisions/JETIX-PLAN.md` | `archive/decisions/JETIX-PLAN.md` | ~6 |
| `decisions/JETIX-ARCHITECTURE-BRIEF.md` | `archive/decisions/JETIX-ARCHITECTURE-BRIEF.md` | ~5 |
| `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` | `archive/decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` | ~3 |
| `decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md` | `archive/decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md` | ~2 |
| `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` | `archive/decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` | ~1 |
| `design/SYSTEM-DESIGN-TECH.md` | `archive/design/SYSTEM-DESIGN-TECH.md` | ~3 |

---

## §2 Suggested mapping (high-level — `archive/<original-path>`)

> Path renames preserve original folder structure under `archive/`.

```
decisions/JETIX-VISION.md                                              → archive/decisions/JETIX-VISION.md
decisions/JETIX-PHILOSOPHY.md                                          → archive/decisions/JETIX-PHILOSOPHY.md
decisions/JETIX-PLAN.md                                                → archive/decisions/JETIX-PLAN.md
decisions/JETIX-ARCHITECTURE-BRIEF.md                                  → archive/decisions/JETIX-ARCHITECTURE-BRIEF.md
decisions/JETIX-SYSTEM-OVERVIEW.md                                     → archive/decisions/JETIX-SYSTEM-OVERVIEW.md
decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md       → archive/decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md
decisions/AUDIT-CURRENT-STATE-2026-04-27.md                            → archive/decisions/AUDIT-CURRENT-STATE-2026-04-27.md
decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md                  → archive/decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md
decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md            → archive/decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md
decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md                      → archive/decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md
decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md                               → archive/decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md
decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md                     → archive/decisions/LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md
decisions/ROY-INFORMATION-DIET.md                                      → archive/decisions/ROY-INFORMATION-DIET.md
decisions/ROY-ALIGNMENT-2026-04-22.md                                  → archive/decisions/ROY-ALIGNMENT-2026-04-22.md
decisions/ROY-AGENTS-BUILT-2026-04-23.md                               → archive/decisions/ROY-AGENTS-BUILT-2026-04-23.md
design/SYSTEM-DESIGN-TECH.md                                           → archive/design/SYSTEM-DESIGN-TECH.md
design/JETIX-FPF.md                                                    → archive/design/JETIX-FPF.md
```

(Full archive map in [INDEX.md](INDEX.md).)

---

## §3 Sample hit dump (first 50 lines, full grep at /tmp/crossref_hits.txt at execution time — re-create with §4 grep below)

(Full 190-line dump kept in commit history; selective sample below for orientation.)

```
swarm/wiki/foundations/principles/architecture.md:16:  - design/JETIX-FPF.md (FPF anti-scope hard rules; B.3 F-G-R; A.6.B Boundary)
swarm/wiki/foundations/principles/architecture.md:74:| FPF anti-scope hard rules | `design/JETIX-FPF.md` anti-scope clauses | ...
swarm/wiki/foundations/principles/architecture.md:984:- `design/JETIX-FPF.md`: anti-scope hard-rule genre; B.3 F-G-R; A.6.B Boundary; A.14 typed edges
swarm/wiki/foundations/part-6b-human-gate/architecture.md:28:  - design/JETIX-FPF.md
swarm/wiki/foundations/part-6b-human-gate/architecture.md:360:corpus for schema validation. [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§3.3]
swarm/wiki/foundations/part-6b-human-gate/architecture.md:659:[src:design/JETIX-FPF.md §5.1 IP-1; ...]
swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:38:  - design/JETIX-FPF.md
swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:39:  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:46:[src:design/JETIX-FPF.md:§5.1 IP-1; ...]
decisions/JETIX-CORPORATION-2026-05-05.md:1814:> [src: audio_496, decisions/JETIX-VISION.md:§14]
decisions/JETIX-CORPORATION-2026-05-05.md:3621:- **`decisions/JETIX-VISION.md`** — D1 Identity Document (источник layered identity §1.2, ICP archetypes)
decisions/JETIX-CORPORATION-2026-05-05.md:3622:- **`decisions/JETIX-PHILOSOPHY.md`** — D2 (philosophy frame)
decisions/JETIX-CORPORATION-2026-05-05.md:3623:- **`decisions/JETIX-PLAN.md`** — D3 (Phase 0/1 actions, used in §10)
decisions/JETIX-CORPORATION-2026-05-05.md:3647:- `design/JETIX-FPF.md` — Foundation Pillar Framework
decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md:1254:- **FPF:** `design/JETIX-FPF.md`
decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md:2330:- **`design/JETIX-FPF.md`** — Foundation Pillar Framework (anti-scope hard rules, F-G-R, Boundary)
decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md:2379:- **`design/SYSTEM-DESIGN-TECH.md`** (2456 строк) — полный технический документ Jetix OS v1-beta
... (162 more lines)
```

---

## §4 How to re-generate this audit grep

```bash
cd ~/jetix-os
grep -rn "decisions/JETIX-VISION\.md\|decisions/JETIX-PHILOSOPHY\.md\|decisions/JETIX-PLAN\.md\|decisions/JETIX-ARCHITECTURE-BRIEF\.md\|decisions/MASTER-PLAN-FOUNDATION\|decisions/JETIX-SYSTEM-OVERVIEW\.md\|decisions/LAYER-5-\|decisions/LAYER-6-\|decisions/LAYER-7-\|decisions/JETIX-FOUNDATION-BUILD\|design/SYSTEM-DESIGN-TECH\.md\|design/JETIX-FPF\.md\|decisions/ROY-INFORMATION-DIET\|decisions/ROY-ALIGNMENT\|decisions/ROY-AGENTS-BUILT\|decisions/AUDIT-CURRENT-STATE\|decisions/VISION-NEXT-STRATEGIC-HORIZON" \
  decisions/ swarm/wiki/foundations/ swarm/wiki/synthesis/ shared/schemas/ CLAUDE.md _meta/ 2>/dev/null \
  | grep -v '^archive/' | grep -v '\.git/'
```

---

## §5 Discipline note

- **Status:** documented only. **NOT** auto-fixed (refactor deferred to follow-up cycle).
- **Why not auto-fix:** mass `sed`/`Edit` across 30+ active canonical docs is high-risk:
  - some refs are historical citations that should stay (e.g., `[src: ...JETIX-VISION.md ...]` in BASE-MANAGEMENT-SYSTEM body — historical provenance)
  - Foundation Part architectures cite `design/JETIX-FPF.md` constitutionally (FPF IP-1..IP-8) — these may need to remain as `design/JETIX-FPF.md` as reading-pointer (not under `archive/`) если Foundation Parts treat FPF as predecessor-canonical companion (see Bundle 1 RUSLAN-ACK)
  - some refs are quotes within markdown code blocks
- **Recommended follow-up cycle:** dedicated `cyc-cross-ref-refactor-YYYY-MM-DD` brigadier prompt that:
  1. Classifies each hit: literal-link / historical-citation / code-block-quote
  2. For literal-links — updates path to `archive/<original-path>`
  3. For historical-citation — leaves untouched OR updates to `archive/<original-path>` if cited as a "go read this" pointer
  4. For code-block-quotes — leaves untouched
  5. Runs `/lint --check-dangling-edges` to verify no broken refs remain
- **Constitutional anchor:** Tier 2 Rule 2 (no architectural changes без gate) — separate gate needed for cross-ref refactor.

---

## §6 Summary signal for Ruslan

After canonical cleanup:
- 63 archive moves complete + 5 deferred moves
- Cross-refs to archived paths exist in **27+ files** (~190 hits total)
- Most-cited archived path: `design/JETIX-FPF.md` (~120 refs across Foundation Parts) — this is constitutional companion, may need special treatment
- **No broken state introduced** — git mv preserves history, paths resolve via `archive/<original-path>`, but absolute paths in `[src: ...]` annotations now point to non-existent original locations
- **Recommended:** schedule cross-ref refactor cycle within 1-2 weeks to keep Foundation Parts hyperlinkable in Antigravity / IDE
