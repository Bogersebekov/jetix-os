---
title: CLAUDE.md Re-framing Decision (Bundle 5 — Pillar C)
date: 2026-04-28
type: decision-artefact
status: AWAITING-APPROVAL
parent_cycle: cyc-foundation-build-2026-04-28
bundle: 5-strategic-layer
phase: A-3 Joint Design synthesis
F: F4
G: brigadier Bundle 5 Pillar C re-framing decision; gates Pillar C architecture drafting
R: R-medium — pending Ruslan ack
---

# §0 Mission

Per Ruslan 28.04 evening: «принципы это такой как бы мега CLAUDE.md для всей
системы». Pillar C Principles substrate structurally re-frames CLAUDE.md.

CLAUDE.md current state (273 lines):
- ~95% operational config (paths, agent roster, project list, file conventions, Wiki/CRM/Voice pipelines, KM-MVP skills)
- ~5% scattered principles (Global Rules 4/6/7; «не трогать private/ssh/.env»; «AI учит, не выполняет»)

This document analyzes 3 re-framing options + adopts hybrid.

# §1 Options

| Option | Description | Verdict |
|---|---|---|
| 1 | Keep CLAUDE.md as-is + Pillar C lives separately + CLAUDE.md references Pillar C | Reject — splits boot-context principles |
| 2 | HYBRID: CLAUDE.md operational config + Pillar C principles canonical, with critical Tier-2 inlined in CLAUDE.md for boot context | **ADOPT** |
| 3 | Pillar C IS CLAUDE.md (re-frame entirely) — operational config moves elsewhere | Reject — breaks Claude Code session boot expectation |

# §2 Adopted rationale (Option 2 HYBRID)

## §2.1 Boot-context constraint

Claude Code reads `CLAUDE.md` at every session start. Principles that constrain
agent behavior MUST be in startup context — not just "by reference". Otherwise
agents load operational config without principle constraints, then operate
without principle awareness.

**Implication:** critical Tier-2 principles MUST be physically present in
CLAUDE.md text (inlined), not only by reference. This rules out Option 1
(reference-only) and Option 3 (move principles out).

## §2.2 Operational config has its own discipline

CLAUDE.md operational config (paths, agent roster, project list, skills) has
discipline around:
- KM-MVP changes (new skill = new CLAUDE.md table row)
- Project-list updates (new project = new row)
- Agent roster changes (new agent = new row)

This discipline is operational-config-update discipline. Mixing it with principle
authoring (which has owner-only authority + supersession discipline + audit cadence)
creates governance confusion. Principle authoring is high-discipline; operational
config update is medium-discipline. Different cadence + authority.

**Implication:** principles canonical authority must live in Pillar C `principles/`
where it has its own governance. CLAUDE.md inlines for boot context but is NOT
canonical. Inline copy is **derived** from Pillar C; lint check ensures sync.

## §2.3 Sync discipline (lint-enforceable)

Hybrid creates a sync invariant:
- Pillar C `tier-2-system/foundation-generic/<rule>.md` files are canonical
- CLAUDE.md "Pillar C Principles (boot-context)" section contains inline derived copy
- A lint rule (added to `/lint`) verifies count + hash match: every foundation-generic Tier-2 rule has corresponding CLAUDE.md inline entry; if mismatch → lint fail

This is **machine-enforceable hybrid** — not "we'll keep them in sync by hand". 
Discipline is mechanized.

## §2.4 Tier 1 not inlined in CLAUDE.md

Tier 1 (manager / owner principles) is **not** inlined in CLAUDE.md because:
- Tier 1 principles are owner-self-discipline (e.g., «long-term thinking») — not enforceable on agents
- Agents reading CLAUDE.md don't need Tier 1 in boot context
- Tier 1 lives in `principles/tier-1-manager/` accessed at owner-reflection cadences (Part 9 weekly/monthly review)

CLAUDE.md "Pillar C Principles (boot-context)" section ONLY contains Tier-2 critical
hard rules (Default-Deny, no API keys, filesystem source-of-truth, no agent strategize,
etc.) — agent-relevant principles only.

# §3 Re-framed CLAUDE.md structure (proposed)

```
# Jetix OS — Master Configuration

## §1 System Overview                          [operational]
## §2 Architecture                             [operational]
## §3 Agent Roster                             [operational]

## §4 Pillar C Principles — Boot Context       [PRINCIPLES — NEW SECTION]
   ## §4.1 Tier 2 Constitutional (11 hard rules — derived from principles/tier-2-system/foundation-generic/)
   ## §4.2 Tier 2 Instance-specific (RUSLAN-LAYER overrides — derived from principles/tier-2-system/ruslan-layer-overrides/)
   ## §4.3 Tier 1 reference link (canonical at principles/tier-1-manager/_index.md)
   ## §4.4 Lint sync discipline (hash check vs canonical)

## §5 Global Rules                             [operational + transitional]
   (Items 4/6/7 etc move to §4 Pillar C; remainder stays operational)

## §6 Key Notion IDs                           [operational]
## §7 File Conventions                         [operational]
## §8 Wiki Architecture v2                     [operational]
## §9 CRM System                               [operational]
## §10 Кто ты                                  [identity → may move to §4 Tier 2]
## §11 Проекты (8 активных)                    [operational]
## §12 Wiki Pipeline                           [operational]
## §13 Voice-Notes Pipeline                    [operational + 1 principle inlined]
## §14 Конвенции                               [operational]
## §15 Skills                                  [operational]
## §16 Рабочий процесс                         [operational]
## §17 Правила                                 [transitional — items consolidate to §4 or §14]
## §18 KM MVP                                  [operational]
## §19 KM MVP quick ops                        [operational]
```

## §3.1 New §4 content (Pillar C boot-context inline section)

```markdown
## §4 Pillar C Principles — Boot Context

> **Authority note.** Canonical principles live in `principles/` (Foundation
> sub-system). This section inlines critical Tier-2 hard rules for Claude Code
> boot context. Sync invariant enforced via `/lint --check-principles-sync`.
> If divergent → canonical wins; CLAUDE.md is derived.

### §4.1 Tier 2 Constitutional (11 hard rules — Foundation generic)

Mirror of `.claude/config/default-deny-table.yaml` constitutional_never_list +
canonical at `principles/tier-2-system/foundation-generic/`.

1. AI does NOT make strategic decisions (FUNDAMENTAL §6.1 rule 1)
2. AI does NOT execute architectural changes without gate (§6.1 rule 2)
3. AI does NOT set capability/skill direction (§6.1 rule 3)
4. AI does NOT claim persistent identity beyond `acting_as` (§6.1 rule 4)
5. AI does NOT claim skin-in-the-game / ownership (§6.1 rule 5)
6. AI does NOT aggregate unstructured long-term memory (§6.1 rule 6)
7. Agents do NOT negotiate contradictions autonomously without human gate (§6.1 rule 7)
8. Agent does NOT evaluate peer agent without human review (§6.1 rule 8)
9. AI does NOT self-modify at runtime (§6.1 rule 9)
10. AI does NOT impersonate human externally without disclosure (§6.1 rule 10)
11. No action without blast-radius categorization + Default-Deny (§6.1 rule 11)

### §4.2 Tier 2 Instance-specific (RUSLAN-LAYER)

Specific to Ruslan's Jetix instance; canonical at `principles/tier-2-system/ruslan-layer-overrides/`:

- NEVER expose API keys (was Global Rule 6)
- Filesystem = source of truth; Notion = view (was Global Rule 4)
- Russian for content; English for code/configs (was Global Rule 7)
- Don't touch `private/`, `~/.ssh/`, `.env` (was Правила item 6)
- Voice-pipeline DRAFT-only — NEVER auto-overwrite prod records
- A/B tests: ALWAYS awaiting_approval, never auto-deploy (was Global Rule 10)

### §4.3 Tier 1 reference

Tier 1 (manager/owner principles) canonical at `principles/tier-1-manager/_index.md`.
Not inlined — agents do not enforce Tier 1; owner discipline.

### §4.4 Sync discipline

Lint check `/lint --check-principles-sync` runs on commit:
- Counts Tier-2 entries in §4.1 (must == 11) and §4.2
- Hash-compares each entry to canonical `principles/tier-2-system/.../<rule>.md`
- Fail-loud if drift detected
```

## §3.2 Items moving FROM CLAUDE.md TO Pillar C principles

| CLAUDE.md current location | Item | Pillar C destination |
|---|---|---|
| Global Rules item 4 | Filesystem = source of truth | tier-2-system/ruslan-layer-overrides/filesystem-source-of-truth.md |
| Global Rules item 6 | NEVER expose API keys | tier-2-system/ruslan-layer-overrides/no-api-key-exposure.md |
| Global Rules item 7 | Russian for content; English for code | tier-2-system/ruslan-layer-overrides/language-discipline.md |
| Global Rules item 10 | A/B tests awaiting_approval | tier-2-system/ruslan-layer-overrides/ab-test-gating.md |
| Правила item 6 | Don't touch private/.ssh/.env | tier-2-system/ruslan-layer-overrides/path-protection.md |
| CRM System «Voice-pipeline DRAFT-only» | NEVER auto-overwrite prod records | tier-2-system/ruslan-layer-overrides/voice-pipeline-draft-only.md |
| Voice-Notes Pipeline «СТОП. Руслан скачивает...» | Manual review gate before distribute | tier-2-system/ruslan-layer-overrides/voice-pipeline-manual-review.md |
| «Кто ты» / persona | Direct, action-oriented, no fluff | tier-2-system/foundation-generic OR ruslan-layer-overrides depending on Foundation-vs-RUSLAN-LAYER analysis at Pillar C draft |
| (FUNDAMENTAL §6.1 11 rules — already canonical at Part 6b) | 11 hard rules | tier-2-system/foundation-generic/<11 files> (Pillar C canonical; Part 6b lints derived) |

## §3.3 Items STAYING in CLAUDE.md (operational)

- Architecture (paths, mailboxes, state)
- Agent Roster (table)
- Key Notion IDs (UI tool refs)
- File Conventions (kebab-case, dates, JSON indent)
- Wiki Architecture v2 (paths, skills)
- CRM System (paths, schemas, skills)
- Проекты 8 активных (operational list)
- Wiki Pipeline (operational)
- Voice-Notes Pipeline operational steps
- Конвенции (file naming)
- Skills (table)
- Рабочий процесс (utro/vecher)
- KM MVP details
- KM MVP quick ops table

# §4 Migration plan

**Phase A (Bundle 5 architecture, this cycle):**
- Pillar C architecture defines structure + governance + sync discipline
- `principles/` directory scaffold created with Foundation-generic Tier-2 11 files derived from Part 6b §I.2
- CLAUDE.md `§4 Pillar C Principles` section template added (placeholder; content authoring in Phase B/Layer 2)
- Lint rule `/lint --check-principles-sync` skill stub created

**Phase B (Layer 2 next sprint):**
- Authoring Tier 2 RUSLAN-LAYER overrides (concrete content)
- Authoring Tier 1 manager principles (concrete content)
- Migrating CLAUDE.md inline content to canonical principles/ files
- Activating sync lint

**Phase C (post-Layer-2):**
- CLAUDE.md fully reflects Pillar C; sync lint enforces invariant
- Items moved out of Global Rules / Правила; transitional sections retired
- Documentation refresh

# §5 Risks + mitigations

| Risk | Mitigation |
|---|---|
| CLAUDE.md drift from canonical principles | `/lint --check-principles-sync` + commit-time hash verification |
| Boot-context principle gap (agent loads CLAUDE.md before reading principles/) | Critical Tier-2 inlined in §4 of CLAUDE.md; agents see at boot |
| RUSLAN-LAYER content authoring deferred (Layer 2) — interim CLAUDE.md still mixed | Acceptable: Phase A leaves CLAUDE.md as-is structurally; Phase B migrates content. Bundle 5 architecture defines target state, not migration timing |
| FUNDAMENTAL §6.1 source vs Part 6b derived vs Pillar C canonical = 3 places for same rules | Single-source-of-truth enforced: FUNDAMENTAL §6.1 = constitutional; Pillar C = canonical principle docs; Part 6b = derived enforcement; CLAUDE.md = derived boot copy. Audit chain: FUNDAMENTAL → Pillar C → {Part 6b config, CLAUDE.md inline} |

# §6 Provenance

- Ruslan 28.04 evening: «принципы это такой как бы мега CLAUDE.md для всей системы»
- CLAUDE.md current state analysis (273 lines, 95% operational + 5% principles)
- FUNDAMENTAL §6.1 (11 constitutional hard rules) — upstream source
- Part 6b §I.2 constitutional_never_list (11-entry enum) — derived enforcement
- Anthropic Constitutional AI [src:raw/books-md/anthropic/bai-2022-cai.md] — constitutional structure pattern
- Anthropic HHH [src:raw/books-md/anthropic/askell-2021-hhh.md] — Tier 2 framework example

---

*End of CLAUDE.md re-framing decision. Pillar C architecture consumes this as input.*
