---
title: Phase 0 — Pre-flight + FPF lens
date: 2026-05-20
type: build-log-entry
phase: 0
parent_prompt: prompts/scaffolding-hypotheses-architecture-2026-05-20.md
prose_authored_by: brigadier-scribe (Cloud Cowork autonomous)
F: F2
G: hypotheses-scaffolding
R: low
---

# Phase 0 — Pre-flight + FPF lens

## §1 Substrate read (ack)

- ✅ EXPLAIN `prompts/explanations/_EXPLAIN-scaffolding-hypotheses-architecture-2026-05-20.md`
- ✅ Prompt `prompts/scaffolding-hypotheses-architecture-2026-05-20.md` (9 phases / 7 layers)
- ✅ CRM analogous pattern: `crm/_schema/{frontmatter,roles,statuses,strategy-hooks}.yaml` + `crm/_templates/{person,org}.md` + 10 `/crm-*` skills present
- ✅ FPF spec source available: `raw/external/ailev-FPF/FPF-Spec.md`
- ✅ Memory rules: `feedback_fpf_lens_first.md`, `feedback_no_unsolicited_alternatives.md`, `feedback_constitutional.md`
- ⚠️ Existing `hypotheses/{active,backlog,validated-archive}.md` — 3 legacy files preserved; new namespace overlay (status dirs scaffolded alongside).

## §2 Tool availability

| Tool | Version |
|---|---|
| openpyxl | 3.1.5 ✅ |
| pandas | 3.0.2 ✅ |
| PyYAML | 6.0.3 ✅ |

No pip install needed.

## §3 FPF lens scope (mandatory declaration)

**Object under scaffolding:** `hypotheses/` substrate = first-class methodology infrastructure для Jetix.

**FPF layer:** Part B.3 F-G-R primitives integrated into hypothesis frontmatter (F-grade / Group-scope / Reliability).

**Acceptance criteria (Phase 8 closure):**
1. 9 phases done with per-phase commit + push
2. 7 layers operational (dir + skills + CRM overlay + daily log + F-G-R + alpha-machinery + Excel)
3. ≥3 sample hypotheses (target 5: H-001..H-005)
4. 2 mermaid diagrams (architecture + lifecycle)
5. 9 skills functional (file scaffolds + descriptors)
6. Build script `_build-table.py` executes на samples

## §4 Constitutional posture

- **R1:** brigadier-scribe scaffolds structure только; strategic prose ≠ generated; sample hypothesis content = derived from substrate refs (not strategy authoring)
- **R2:** Foundation read-only; new namespace `hypotheses/` + `.claude/skills/hypothesis-*` + `tools/build-hypothesis-views.py`
- **R6:** Per-hypothesis provenance via frontmatter `created`/`updated`/`linked_artefacts`
- **R11:** Only canonical skill patterns (CRM-analogous)
- **R12:** Hypothesis substrate ≠ extraction
- **EP-5:** Mandatory F/G/R per hypothesis frontmatter
- **FPF-lens-FIRST:** этот document ✅
- **Append-only:** `hypotheses/_log.md` audit trail per phase
- **Filesystem-authoritative:** Excel = derived view; MD primary

## §5 Trigger ack

Ruslan launched: «ебашь это prompt и пусть уже ебашит всё что только можно» — autonomous execute, no pause.

---

*Phase 0 closed. Next: Phase 1 Layer 1 — dir + schema + templates.*
