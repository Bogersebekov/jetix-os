---
title: "Wave 1 — Strategic Layer Mechanical Scaffolding Brief"
date: 2026-04-28
type: cloud-code-brief
target: ROY brigadier on server (claude/jolly-margulis-915d34)
parent_cycle: cyc-foundation-build-2026-04-28
phase: layer-2-rollout-wave-1
estimated_walltime: 30-90min
F: F4
G: brigadier Wave 1 scaffolding dispatch
R: R-medium — pending Ruslan ack on output AWAITING-APPROVAL packet
---

# §0 Mission

Wave 1 первой итерации Layer 2 RUSLAN-LAYER content authoring rollout. **Mechanical scaffolding** Strategic Layer canonical structure **БЕЗ content migration**. Per Ruslan 2026-04-28 evening directive: «пусть залупа создаётся; информацию переноса каждую обрабатываем после, по штуке».

Wave 1 расчищает поле — после неё Ruslan делает per-artefact review (Wave 1.4) каждого Lock / Insight / scattered principle, и каждый migration является ack-driven write. Foundation generic structure is locked-in immediately; RUSLAN-LAYER content stays scaffold-pending-review до Ruslan-driven per-file review.

Strategic Layer Foundation v1.0 LOCKED 2026-04-28; this Wave 1 starts content rollout at structural level.

# §1 Scope

## §1.1 ВКЛЮЧЕНО

- **Pillar C `principles/` directory tree** creation per `swarm/wiki/foundations/principles/architecture.md` §I structure
- **11 Tier-2 foundation-generic principle files** — mechanical mirror of FUNDAMENTAL §6.1 (`decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`); rule statements + rationale extracted, not authored
- **7 Tier-2 ruslan_layer_overrides SCAFFOLDS** — frontmatter + structure stubs + candidate-content from CLAUDE.md as commented HTML reference (NO actual content migration; Ruslan reviews per-file in Wave 1.4)
- **Tier 1 manager directory** — `_template.md` + `_index.md` (empty for content; Wave 2 ответственность)
- `principles/_governance.md` per Pillar C §I.4 (Foundation generic, copy-as-is from architecture)
- **CLAUDE.md §4 placeholder section** per `claude-md-reframing-decision.md` §3.1 — додаётся в конец (NOT delete or modify existing scattered principles; Wave 1.4 decides per-line)
- **Lock Entry scaffolds D-1..D-29** в `decisions/strategic/lock-entries/D-NN-<slug>.md` — frontmatter + section headers + candidate content extracted from source files as commented reference
- **Strategic Insight scaffolds — 4 existing** в `decisions/strategic/strategic-insights/<slug>.md`:
  - `ai-psy-led-design.md` ← `decisions/STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md`
  - `arbitrage-traffic-direction.md` ← `decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md`
  - `jetix-ai-bios-moment.md` ← `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md`
  - `ma-direction.md` ← `decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md`
- **Schemas physical files** (4) в `shared/schemas/`:
  - `strategic-direction-doc.json` per Part 11 §I.1
  - `project-strategy.json` per Part 7 Bundle 5 supplement §I.X.1
  - `decisions-db.json` per Part 11 §I.3
  - `principle-doc.json` per Pillar C §I.1
- **Configs physical files** (4) в `.claude/config/`:
  - `default-deny-table.yaml` constitutional_never_list (11 entries derived from B.2 above)
  - `strategic-doc-types.yaml` per Part 11 §I.4 foundation_generic stanza only
  - `principles-tier-1-manager.yaml` per Pillar C §I.6 foundation_generic stanza
  - `principles-tier-2-system.yaml` per Pillar C §I.5 foundation_generic stanza
- **Decisions DB index bootstrap** — file `decisions/strategic/_decisions-db-index.jsonl`, 33 stub entries (29 Locks + 4 Insights), all `status: pending-review`, recall metadata to be populated during Wave 1.4
- **Lint skill stubs** (placeholder files only; do not implement logic) for: `--check-pillar-c-part-6b-sync`, `--check-claude-md-sync`, `--check-principle-citations`, `--check-tier-2-foundation-count`, `--check-lock-to-principle-trail`, `--check-supersession-chain`, `--check-pillar-a-anchors`, `--check-strategic-staleness` (Phase B materialization later)

## §1.2 ИСКЛЮЧЕНО (НЕ Wave 1)

- Content migration of CLAUDE.md scattered principles → ruslan_layer_overrides actual content (scaffolds only; Wave 1.4 per-file review)
- Content migration of Lock Entry text into Foundation 7-section structure (scaffolds only; per-Lock review)
- Content migration of Strategic Insight text (scaffolds only; per-Insight review)
- Authoring Tier 1 manager principle CONTENT (Wave 2 — Ruslan-driven writing-as-thinking)
- Authoring Tier 2 ruslan_layer_overrides NEW content beyond CLAUDE.md candidates (Wave 2)
- Removal / supersession of legacy files (`LOCKS-D25-D28-ADDENDUM-*`, `STRATEGIC-INSIGHT-*` at root) — preserve as-is; Wave 1.4 decides per-artefact
- Activation of sync lints (skill files exist as stubs; lint logic Phase B)
- Wave 2 documents (Founder Overlay, Phase Plan v1.0, North Star, Direction Cards, project strategies)
- Multi-chat methodology (это Wave 3 North Star concern)
- Any owner-acked write (no F4/F5 promotion; everything stays at F2 scaffold-pending-review)

# §2 Phase A — Reconnaissance (мандатно перед Phase B)

Бригадир сначала находит existing artefacts. Output → `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-1-scaffolding/recon.md`.

## §2.1 Existing Locks D-1..D-29 inventory

D-25..D-29 already known:
- D-25..D-28: `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md`
- D-29: `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md`

D-1..D-24: search в:
- `decisions/JETIX-PHILOSOPHY.md`
- `decisions/JETIX-VISION.md`
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`
- `decisions/JETIX-PLAN.md`
- `decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md`
- recursive grep `D-[0-9]+` over `decisions/` (excluding `_research/`, `_templates/`, `policy/`)

Для каждого Lock output:
- `lock_id`: D-NN
- `slug`: kebab-case (брать существующий if visible или derive from rationale text)
- `source_path`: где сейчас живёт
- `source_section`: § ref если nested
- `candidate_statement_text`: 1-3 sentences extract
- `candidate_rationale_text`: paragraph-level extract
- `current_status_signal`: active / superseded if visible
- `mentioned_in_other_files`: list of cross-refs

Если total < 29 — flag missing IDs и попытаться найти через `LOCKED_DECISIONS` keyword grep / decision-ID references in architecture parts (Part 6a, 6b, 7, 11).

## §2.2 Existing Strategic Insights inventory

4 confirmed at `decisions/STRATEGIC-INSIGHT-*.md`. Confirm exhaustive (grep `STRATEGIC-INSIGHT` recursively over `decisions/`).

Если найдётся 5-й — добавить.

Для каждого output:
- `slug`: kebab-case derivative
- `source_path`
- `current_structure_summary`: какие секции есть now
- `lifecycle_state_signal`: draft / accepted / promoted / deferred (visible in current text)
- `contains_lock_promotion_candidates`: yes/no
- `contains_direction_promotion_candidates`: yes/no

## §2.3 CLAUDE.md scattered principles audit

Source: `CLAUDE.md` (26.8 KB). Per `claude-md-reframing-decision.md` §3.2 candidates:

| Candidate slug | CLAUDE.md location signal |
|---|---|
| `no-api-key-exposure` | Global Rules item 6 |
| `filesystem-source-of-truth` | Global Rules item 4 |
| `language-discipline` | Global Rules item 7 |
| `ab-test-gating` | Global Rules item 10 |
| `path-protection` | Правила item 6 |
| `voice-pipeline-draft-only` | CRM voice-pipeline section |
| `voice-pipeline-manual-review` | Voice-Notes Pipeline СТОП gate |

Бригадир locates exact line ranges + extracts verbatim text. Output:
- `candidate_slug`
- `claude_md_line_range`
- `verbatim_text`
- `surrounding_context_1_paragraph`
- `apparent_intent`
- `migration_complexity_estimate`: trivial / requires-rephrasing / needs-Ruslan-clarification

Если в CLAUDE.md находятся **другие** principle-кандидаты (не в списке выше) — flag separately в recon под heading `additional-candidates-flagged`.

## §2.4 FUNDAMENTAL §6.1 11 hard rules text extraction

Source: `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` §6.1.

Output: 11 entries:
- `rule_number`: 1..11
- `rule_statement`: verbatim from §6.1
- `rule_rationale`: verbatim from §6.1
- `pillar_c_target_slug`: per mapping in `swarm/wiki/foundations/principles/architecture.md` §A.1 (already canonical):
  - rule 1 → `ai-does-not-strategize`
  - rule 2 → `ai-does-not-execute-architectural-decision`
  - rule 3 → `ai-does-not-set-skill-direction`
  - rule 4 → `ai-does-not-claim-persistent-identity`
  - rule 5 → `ai-does-not-claim-skin-in-the-game`
  - rule 6 → `ai-does-not-aggregate-unstructured-long-term-memory`
  - rule 7 → `agents-do-not-negotiate-contradictions-autonomously`
  - rule 8 → `agent-does-not-evaluate-peer-agent`
  - rule 9 → `ai-does-not-self-modify-at-runtime`
  - rule 10 → `ai-does-not-impersonate-human-externally`
  - rule 11 → `bypass-blast-radius-categorization-forbidden`
- `part_6b_action_class`: enforcement identifier per Part 6b §I.2 constitutional_never_list

Phase A complete when recon.md committed.

# §3 Phase B — Scaffolding

После Phase A recon committed, Phase B создаёт структуры. Каждый файл carries complete frontmatter per relevant schema. Filenames kebab-case. Dates ISO YYYY-MM-DD.

## §3.1 Pillar C directory tree

```
principles/
├── _index.md                        # MOC for both tiers
├── _governance.md                   # Foundation generic governance per Pillar C §I.4
├── tier-1-manager/
│   ├── _index.md                    # Tier 1 catalogue stub
│   └── _template.md                 # Per Pillar C §I.3 8-section structure
└── tier-2-system/
    ├── _index.md
    ├── _template.md
    ├── foundation-generic/
    │   ├── _index.md
    │   └── (11 files — see §3.2)
    └── ruslan-layer-overrides/
        ├── _index.md
        └── (7 scaffold files — see §3.3)
```

`_index.md` files contain catalogue listing (auto-generatable; for Wave 1 manual-write listing is fine).

## §3.2 11 Tier-2 foundation-generic files (MECHANICAL MIRROR)

For each rule (1..11) per §2.4 mapping:

```yaml
---
title: "Principle: <verbatim §1 statement>"
principle_id: P-C-<NN>
tier: tier_2_system
category: foundation_generic
slug: <mapped-slug>
date: 2026-04-28
F: F8
G: "Foundation generic — mirror of FUNDAMENTAL §6.1 rule <N>"
R: R-high
fundamental_anchor: "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md §6.1 rule <N>"
fpf_anchor: <as applicable>
owner_ack:
  acked_by: ruslan
  acked_date: 2026-04-28  # via RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28
review_cadence: annual
last_reviewed_date: 2026-04-28
enforcement:
  part_6b_action_class: <action_class_id>
  part_6b_enforcement_mode: halt_log_alert
  grade: F8
audit:
  - {date: 2026-04-28, event: "created (Wave 1 mechanical mirror)", note: "constitutional baseline"}
---
```

Body per Pillar C §I.3 8-section structure. **Это mechanical extraction, не authoring.** Бригадир copy-paste'ит rule statement + rationale из FUNDAMENTAL §6.1 verbatim в §1 и §2; §3-§8 заполняет structurally per template.

§5 Enforcement section fields populated from §2.4 recon (`part_6b_action_class`, mode `halt_log_alert`, grade `F8`).

## §3.3 7 Tier-2 ruslan_layer_overrides SCAFFOLDS

Каждый файл — frontmatter complete + 8 section headers + extracted candidate as HTML comment **БЕЗ автоматической migration в §1 statement / §2 rationale**.

Frontmatter pattern:
```yaml
---
title: "Principle: <slug-readable> (SCAFFOLD-PENDING-REVIEW)"
principle_id: P-S-<NN>  # NN = sequential 01..07 для overrides
tier: tier_2_system
category: ruslan_layer_overrides
slug: <kebab-slug>
date: 2026-04-28
status: scaffold-pending-review
F: F2  # NOT promoted; pending Wave 1.4 review
G: "scaffold awaiting Ruslan-driven migration review"
R: R-low
candidate_source:
  path: "CLAUDE.md"
  line_range: "<from-recon>"
  extracted_2026-04-28: "<extracted-verbatim-as-yaml-string-or-empty>"
review_status: pending-wave-1.4
created_date: 2026-04-28
---
```

Body:
```markdown
<!-- WAVE-1-SCAFFOLD: Ruslan reviews this artefact in Wave 1.4 migration step.
DO NOT auto-promote to F4. DO NOT activate referenced enforcement until Ruslan ack.
Candidate source: CLAUDE.md line <N>-<M>.

CANDIDATE TEXT (verbatim from CLAUDE.md, awaiting review):
<verbatim-extracted-text>

Review actions available in Wave 1.4:
- PROMOTE-AS-IS: minor frontmatter cleanup, content unchanged → F4
- REFACTOR: rewrite §1 statement to fit principle-doc style; preserve intent → F4
- SPLIT: candidate covers multiple principles; split into N files → drafts F2
- MERGE: candidate duplicates another principle → archive this; supersede the other
- ARCHIVE-WITHOUT-MIGRATION: not principle-grade; remove from Pillar C target
- ESCALATE: needs Ruslan clarification before action
-->

# Principle: <slug-readable>

## §1 Statement
<!-- empty pending Wave 1.4 review; do not author here -->

## §2 Rationale
<!-- empty pending Wave 1.4 review -->

## §3 Scope
applies_to: system_wide  # default; review at Wave 1.4
specific_part_consumers: []  # populate at review

## §4 Anchors
- Constitutional: <as applicable>
- Lock Entry origin: <as applicable>
- Wave B framework: <as applicable>

## §5 Enforcement (Tier 2 only)
<!-- empty pending Wave 1.4; mode/grade depend on principle severity classification -->

## §6 Anti-scope
<!-- empty pending Wave 1.4 -->

## §7 Audit history
| Date | Event | Note |
|---|---|---|
| 2026-04-28 | scaffolded | Wave 1 mechanical scaffold; pending Ruslan migration review |

## §8 Provenance
- Bundle 5 Pillar C architecture: `swarm/wiki/foundations/principles/architecture.md`
- Wave 1 scaffolding brief: `prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md`
- CLAUDE.md re-framing decision: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/claude-md-reframing-decision.md`
- Original location: CLAUDE.md line <N>-<M>
```

## §3.4 Tier 1 manager directory (EMPTY for content)

`principles/tier-1-manager/_template.md`: per Pillar C §I.3 8-section structure (template for future Tier 1 authoring; structure-only).

`principles/tier-1-manager/_index.md`: catalogue header («Manager principles — owner values authored Wave 2») + empty list section.

**НЕ create RUSLAN content files в Tier 1.** Ruslan authors в Wave 2 manually (writing-as-thinking, не делегируется бригадиру).

## §3.5 `principles/_governance.md`

Copy verbatim Foundation generic per Pillar C architecture §I.4 — authoring authority, supersession discipline, audit cadence, sync invariants, Lock-to-principle promotion.

## §3.6 CLAUDE.md §4 placeholder section

Per `claude-md-reframing-decision.md` §3.1. **APPEND at end of CLAUDE.md** (после current operational sections). DO NOT delete / modify existing scattered principles (those go through Wave 1.4 per-file review).

```markdown
## §4 Pillar C Principles — Boot Context

> **Authority note.** Canonical principles live in `principles/` (Foundation
> sub-system). This section inlines critical Tier-2 hard rules for Claude Code
> boot context. Sync invariant enforced via `/lint --check-claude-md-sync` (Phase B).
> If divergent → canonical wins; CLAUDE.md is derived.
> 
> **PHASE A NOTE (Wave 1):** This section is PLACEHOLDER. Tier 2 inline content 
> populated when Wave 1.4 migration review completes per-file. Until then, 
> existing scattered Global Rules / Правила remain authoritative.

### §4.1 Tier 2 Constitutional (11 hard rules — Foundation generic)

> [DERIVED FROM `principles/tier-2-system/foundation-generic/*.md` — Wave 1 scaffolded; 
> inline content populates at Wave 1.4 ack.]

### §4.2 Tier 2 Instance-specific (RUSLAN-LAYER overrides)

> [DERIVED FROM `principles/tier-2-system/ruslan-layer-overrides/*.md` — Wave 1 
> scaffolded as pending-review; content migrates at Wave 1.4 per-file ack.]

### §4.3 Tier 1 reference

Tier 1 (manager/owner principles) canonical at `principles/tier-1-manager/_index.md`.
Wave 2 ответственность для content authoring. Not inlined — agents do not 
enforce Tier 1; owner discipline.

### §4.4 Sync discipline

Lint check `/lint --check-claude-md-sync` (Phase B materialization):
- Counts Tier-2 entries in §4.1 (target == 11) and §4.2 (instance-specific count)
- Hash-compares each entry to canonical `principles/tier-2-system/.../<rule>.md`
- Fail-loud if drift detected
```

## §3.7 Lock Entry scaffolds (29 files)

Path: `decisions/strategic/lock-entries/D-NN-<slug>.md`.

Each per `decisions/strategic/_templates/lock-entry.md.template` 7-section structure.

Frontmatter:
```yaml
---
title: "Lock D-<NN> — <human-readable-summary> (SCAFFOLD-PENDING-REVIEW)"
type: lock-entry
version: 1.0
status: scaffold-pending-review  # NOT draft, NOT active — explicit Wave 1 state
cadence: append-only
owner: ruslan-plus-agent
audience: internal
F: F2  # NOT F4/F5 until Wave 1.4 ack
G: "scaffold awaiting Ruslan-driven migration review"
R: R-low
last_updated: 2026-04-28
lock_id: D-<NN>
slug: <kebab-slug-from-recon>
candidate_source:
  path: "<source-path-from-recon>"
  section: "<section-ref-if-nested>"
review_status: pending-wave-1.4
created_date: 2026-04-28
references:
  foundation_parts: [Part 6 governance gate, Part 1 system state persistence, Part 8 health monitor, Part 11 strategic direction substrate]
  fpf_anchors: [B.3 trust calculus, IP-3 artifacts-over-conversations]
  parent_strategic_docs:
    - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
related_locks: []  # populate at Wave 1.4
---
```

Body: 7-section template skeleton + HTML comment block at top:
```markdown
<!-- WAVE-1-SCAFFOLD: Ruslan reviews this Lock in Wave 1.4 migration step.
DO NOT promote to F4 until ack.

Source: <source-path> §<section>
Extracted candidate (verbatim from source):

<verbatim candidate text from recon>

Migration actions available in Wave 1.4:
- PROMOTE-AS-IS: copy candidate to §1-§7; minor cleanup → F4
- REFACTOR: reorganize candidate to fit 7-section discipline → F4
- SPLIT: candidate is multi-Lock; split into D-NN-a, D-NN-b → scaffold
- ARCHIVE: not actually a Lock (might be Direction, Insight, or operational note)
- SUPERSEDE-WITH-NEW: write new Lock; mark this superseded
- ESCALATE: needs clarification
-->

# Lock D-<NN> — <title>

## §1 What is locked
<!-- empty pending Wave 1.4 review -->

## §2 Why this is irreversible
<!-- empty pending Wave 1.4 -->

## §3 Scope of what this Lock covers
<!-- empty pending -->

## §4 Downstream artifacts depending on this Lock
<!-- empty pending -->

## §5 Reversal predicate
<!-- empty pending -->

## §6 Anti-scope
<!-- empty pending -->

## §7 Provenance + sources
- Bundle 5 Pillar A architecture: `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md`
- Wave 1 scaffolding brief: `prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md`
- Original location: <source-path>
- Scaffolded: 2026-04-28
```

## §3.8 Strategic Insight scaffolds (4 files)

Path: `decisions/strategic/strategic-insights/<slug>.md`.

Each per `decisions/strategic/_templates/strategic-insight.md.template` 9-section structure (§0-§9).

Frontmatter pattern (`lifecycle_state: scaffold-pending-review`, `F: F2`, status reflects Wave 1 state). Body: section headers + HTML comment + extracted candidate text from source as commented reference. Same migration-action options as Lock scaffolds.

## §3.9 Schemas physical files

Create в `shared/schemas/`:

- `strategic-direction-doc.json` — copy from Part 11 §I.1 schema literal
- `project-strategy.json` — copy from Part 7 Bundle 5 supplement §I.X.1 schema literal
- `decisions-db.json` — copy from Part 11 §I.3 schema literal
- `principle-doc.json` — copy from Pillar C §I.1 schema literal

Files validate as JSON Schema draft-07 conformant.

## §3.10 Configs physical files

Create в `.claude/config/`:

- `default-deny-table.yaml` constitutional_never_list — 11 entries derived from §3.2 11 Tier-2 foundation-generic principle files. Format per Part 6b §I.2 schema. Each entry: `action_class`, `trigger`, `enforcement: halt_log_alert`, `grade: F8`, `fundamental_anchor: "§6.1 rule N"`, `pillar_c_canonical: "principles/tier-2-system/foundation-generic/<slug>.md"`
- `strategic-doc-types.yaml` — copy Part 11 §I.4 foundation_generic stanza literal
- `principles-tier-1-manager.yaml` — copy Pillar C §I.6 foundation_generic stanza literal
- `principles-tier-2-system.yaml` — copy Pillar C §I.5 foundation_generic stanza literal (11 rules listed; no ruslan_layer_overrides yet)

## §3.11 Decisions DB index bootstrap

File: `decisions/strategic/_decisions-db-index.jsonl` (JSON Lines format, one record per line per `shared/schemas/decisions-db.json` schema).

33 entries:
- 29 Lock entries: `decision_id: D-NN`, `what: <1-line summary from recon>`, `when: <if dateable from source else null>`, `by_whom: ruslan`, `based_on.context: ""`, `status: pending-review`, `scope.level: constitutional`, `connection.anchored_strategic_docs: []`, `lock_candidate: true`
- 4 Strategic Insight entries: `decision_id: I-<slug>`, `what: <1-line summary>`, `when: <date from source>`, `by_whom: ruslan`, `status: pending-review`, `scope.level: strategic`, `lock_candidate: false`

All recall metadata минимальное; full population happens at Wave 1.4 per-artefact review.

## §3.12 Lint skill stubs

Create в `.claude/commands/` (or `skills/` per repo convention) — placeholder files:

- `lint-check-pillar-c-part-6b-sync.md` — skill description + STUB note (Phase B implementation)
- `lint-check-claude-md-sync.md`
- `lint-check-principle-citations.md`
- `lint-check-tier-2-foundation-count.md`
- `lint-check-lock-to-principle-trail.md`
- `lint-check-supersession-chain.md`
- `lint-check-pillar-a-anchors.md`
- `lint-check-strategic-staleness.md`

Each stub: frontmatter (`status: stub-phase-b-materialization`) + 1-paragraph description per relevant Pillar architecture §H.1 / §J.5.

# §4 Phase C — Review Queue Generation

Output: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-1-scaffolding/review-queue.md`.

Tabular queue с одной строкой на каждый scaffolded artefact requiring Ruslan content review:

| Item | Type | File path | Source path | 1-line summary | Priority | Migration action options |
|---|---|---|---|---|---|---|

Priority guidance:
- **HIGH**: critical Locks D-13, D-21, D-22, D-26, D-27, D-29 (per locked_decisions_referenced в Part 11 frontmatter); STRATEGIC-INSIGHT-AI-BIOS-MOMENT (foundational thesis)
- **MEDIUM**: остальные Locks; остальные 3 Insights
- **LOW**: ruslan_layer_overrides scaffolds (operational, low-strategic)

Migration action options per item — same enum as scaffold HTML comment.

This queue is INPUT для Wave 1.4 (Ruslan-driven per-artefact migration session).

# §5 Phase D — STOP at AWAITING-APPROVAL

Бригадир does NOT:
- Migrate any content (only scaffolds; HTML comments preserve candidate text)
- Activate sync lints (stubs only)
- Modify FUNDAMENTAL §6.1 text (Pillar C is downstream mirror)
- Author Tier 1 content
- Delete legacy files (preserve as-is; Wave 1.4 decides)
- Touch Wave 2+ documents
- Force-promote any scaffold to F4

Бригадир DOES:
- Create AWAITING-APPROVAL packet at `decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-28.md` summarizing:
  - File counts per category (e.g., «11 Tier-2 foundation-generic files created», «29 Lock scaffolds created»)
  - List of pending-review queue
  - Self-check verification: `count(principles/tier-2-system/foundation-generic/*.md) == 11`, all Pillar C dirs created, all 4 schemas present, all 4 configs present
  - Review queue location ref
  - Recon report ref
  - Что Ruslan'у проверить перед per-artefact review (Wave 1.4 entry)
- Push all commits

# §6 Constraints

- Foundation generic only — RUSLAN-LAYER content authoring deferred (per memory `feedback_strategic_layer_is_foundation_level` + `feedback_ai_is_scribe_not_author_for_strategic_docs`)
- Beta-first НО enterprise + $1T baseline preserved (per memory `feedback_no_solo_founder_downgrade`)
- Russian primary in any human-readable text (per memory `feedback_orientation_day_flow`)
- Filesystem = source of truth (D17/D25)
- Push после commit (always)
- Structured commit pattern: `[wave-1] <area> <verb>: <slug-or-summary>` (areas: pillar-c, lock-scaffold, insight-scaffold, schemas, configs, claude-md, decisions-db, lint-stubs, recon, awaiting-approval)
- НЕ run multi-chat methodology (Wave 3 concern)
- НЕ trigger any cascade (cascade discipline activates Wave 4+)
- НЕ self-modify Wave 1 brief (this file)
- При неоднозначности — flag в recon.md `unclear_<area>` section, do NOT decide; Ruslan reviews

# §7 Output

- Working branch: `claude/jolly-margulis-915d34` (server side main work branch)
- All commits per structured pattern, push to origin per commit batch (small batches OK)
- AWAITING-APPROVAL packet at `decisions/AWAITING-APPROVAL-wave-1-scaffolding-2026-04-28.md`
- Review queue at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-1-scaffolding/review-queue.md`
- Recon report at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-1-scaffolding/recon.md`
- Summary report at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-1-scaffolding/SUMMARY.md`

# §8 Branch + commit pattern + sync from CC

## §8.1 Server pulls this brief

CC side delivered this brief on branch `claude/clever-ramanujan-bd4845` (current Cloud Cowork session worktree). Server pulls:

```bash
cd ~/jetix-os
git fetch origin claude/clever-ramanujan-bd4845
git show origin/claude/clever-ramanujan-bd4845:prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md > prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md
git add prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md
git commit -m "[wave-1] sync brief from CC: Wave 1 scaffolding"
git push origin claude/jolly-margulis-915d34
```

(Or alternative: cherry-pick from clever-ramanujan-bd4845 onto jolly-margulis. Server picks workflow.)

## §8.2 Server work branch

Work branch: `claude/jolly-margulis-915d34`. All Wave 1 commits land here. Push to origin per commit batch.

## §8.3 CC notification on completion

Бригадир signals completion via tmux session log + notes в AWAITING-APPROVAL packet. Cloud Cowork next session pulls AWAITING-APPROVAL + walks Ruslan through review queue (Wave 1.4 entry).

# §9 Estimated walltime

30-90 minutes:
- Phase A recon: 10-20 min (recursive grep + extract)
- Phase B scaffolding: 15-50 min (mostly file creation, mechanical mirror, HTML comment construction; 33 scaffold files + 11 mirror files + Pillar C tree + schemas + configs + CLAUDE.md amendment)
- Phase C review queue: 5-10 min (tabular generation)
- Phase D AWAITING-APPROVAL packet: 5-10 min (summary + self-check)

No heavy synthesis (это не Wave C bundle); mostly mechanical work. Compound velocity 5-9× from estimates is unlikely here — work is bounded mechanical, not synthesis.

---

*End of Wave 1 brief. Foundation v1.0 LOCKED → Layer 2 rollout starts. Mechanical scaffolding only; per-artefact content review (Wave 1.4) is Ruslan-driven per-file ack-driven write. Mantra: SCAFFOLDS-NOT-MIGRATIONS. RUSLAN-IS-SOLE-AUTHOR. AI-IS-SCRIBE-AND-EXTRACTOR.*
