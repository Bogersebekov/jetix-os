---
title: "FMT-exocortex-template — Engineering Structural Integration (IWE Phase B)"
type: integration-synthesis
expert: engineering-expert
mode: integrator
task_id: task-fpf-iwe-phase-b-2026-05-17
cycle_id: cyc-iwe-phase-b-2026-05-17
artefact_source: raw/external/tseren-github-2026-05-17/FMT-exocortex-template/
created: 2026-05-17
status: draft
confidence: high
confidence_method: artefact-direct-read
provenance_count: 24
edges_to_add: []
---

# FMT-exocortex-template — Engineering Structural Integration

> **Контекст:** Engineering × integrator pass. Brigadier integrates this with peer cells (knowledge-synth, philosophy-critic) into `02-iwe-deep-v2.md`. R1 scribe posture — factual structural mapping, not strategic recommendation.

---

## §1 Repo-as-Template Architecture (FMT/Instance split, 3-layer boundary)

### §1.1 Repository taxonomy (3-tier)

FMT-exocortex-template is typed as `Base/Formats` in `REPO-TYPE.md` L1-4: it is the **platform distribution layer** (L1). After a user forks it, the fork becomes their personal DS-exocortex (L3 = user-space). An intermediate Pack layer (L2 = domain knowledge) is maintained separately per user domain.

```
L1 Platform-space  ←  FMT-exocortex-template (this repo; updated via update.sh)
L2 Pack            ←  user's PACK-{domain}/ repos (source-of-truth for domain knowledge)
L3 User-space      ←  user's forked DS-exocortex + DS-strategy (personal data; never overwritten)
```

Source: `ONTOLOGY.md` §2 rows "Platform-space" (DP.D.011), "User-space" (DP.D.011); `README.en.md` L159-179.

### §1.2 Three-layer update boundary

`CLAUDE.md` §7 declares three explicit layers:

| Layer | Content | Update policy |
|---|---|---|
| L1 | §1-§7 of CLAUDE.md + memory/protocol-*.md + .claude/skills/ + .claude/hooks/ | Updated by `update.sh` (platform) |
| L2 | §8 (Staging) of CLAUDE.md | Testing channel — validated rules promoted to L1 |
| L3 | §9 (Author) + extensions/*.md + params.yaml | User-space; `update.sh` explicitly excludes |

Source: `CLAUDE.md` §7 L1-L3 block; `generate-manifest.sh` EXCLUDE_EXACT array lines 41-49 (params.yaml, extensions/*, README.md, LICENSE explicitly excluded from manifest).

### §1.3 Fork instantiation flow

```
gh repo fork TserenTserenov/FMT-exocortex-template --clone
cd FMT-exocortex-template
bash setup.sh
```

`setup.sh` reads `roles/*/role.yaml` (ROLE-CONTRACT.md L84-89), substitutes `{{PLACEHOLDER}}` variables (CLAUDE.md §3 "Placeholder-переменная"), installs launchd/cron entries, and materialises `.iwe-runtime/` (referenced in parity-contract.yaml "build-runtime.sh" pattern). After setup, the instance is independent of git history with the upstream — update flow uses HTTP manifest fetch, not git remote.

Source: `README.en.md` L137-150; `parity-contract.yaml` "build-runtime-invoke" pattern L28-32; `update.sh` L14-18 (no shared git history required).

---

## §2 Composition Map (extensions + params + memory + .claude/skills)

### §2.1 Extension surface

`extensions/` is the designated user-customisation layer. A user writes Markdown files named by hook convention:

| Hook | Filename pattern | Invocation point |
|---|---|---|
| day-open before | extensions/day-open.before*.md | Before step 1 of day-open protocol |
| day-open after | extensions/day-open.after*.md | After "Requires attention" step |
| day-open checks | extensions/day-open.checks*.md | Pre-commit gate (blocking) |
| day-close after | extensions/day-close.after*.md | After day summary, before verification |
| day-close checks | extensions/day-close.checks*.md | Pre-archive gate |
| week-close before | extensions/week-close.before*.md | Before lesson rotation |
| week-close after | extensions/week-close.after*.md | After memory audit |
| protocol-close checks | extensions/protocol-close.checks*.md | Pre-commit gate (R4.3) |
| protocol-close after | extensions/protocol-close.after*.md | After checklist, before verification |
| protocol-open after | extensions/protocol-open.after*.md | After WP-Gate ritual |

Multiple files per hook are loaded alphabetically. Loading is orchestrated by `.claude/scripts/load-extensions.sh` called from each SKILL.md's algorithm.

Source: `.claude/skills/extend/SKILL.md` §3 "Extension points" table; `.claude/skills/day-open/SKILL.md` steps 0, 6c, 7b.

### §2.2 params.yaml gate logic

`params.yaml` is the feature-flag surface. It gates protocol steps at runtime (read by skills, not by hooks). Key flags:

- `video_check`, `multiplier_enabled`, `reflection_enabled`, `lesson_rotation` — step-level on/off per protocol
- `capture_autonomy: propose|manual|auto` — controls Capture-to-Pack initiative level
- `telegram_notifications` — Synchronizer dispatch
- `author_mode: false` — when `true`, unlocks direct L1 editing (author-only; CLAUDE.md §9 Extensions Gate)

`params.yaml` is excluded from `update-manifest.json` (generate-manifest.sh L46), so user flags survive all upstream updates.

Source: `params.yaml` full file; `generate-manifest.sh` EXCLUDE_EXACT L46.

### §2.3 Memory as hot-context surface

`memory/` is the slim knowledge layer. Per `CLAUDE.md` §4:
- **Hot** (≤150 total lines, loaded every session): CLAUDE.md, MEMORY.md, distinctions.md, formatting.md
- **Warm** (lazy, by trigger): protocol-*.md, feedback_*, reference_*
- **Cold/Archive**: ≥30d / ≥90d without access

The declared policy is ≤11 files total in memory/. New files must carry mandatory frontmatter (S-35 spec, `CLAUDE.md` §9 "Memory Lifecycle" block). Files not present in the tracked repo (memory/ returns no Glob hits) appear to be user-space only — the platform ships the schema, not the content.

Source: `CLAUDE.md` §4 "Memory" table; `CLAUDE.md` §9 S-35 frontmatter block.

### §2.4 .claude/skills/ composition

Skills are invocable as `/<name>` inside Claude Code. Each skill is a `.claude/skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`, `version`, `user_invocable`). Observed skills in this repo:

```
apply-captures, archgate, audit-installation, day-close, day-open,
extend, fpf, iwe-bug-report, iwe-rules-review, iwe-update, ke,
month-close, pack-new, personal-guide-render, personal-guide-start,
run-protocol, setup-wakatime, strategy-session, think, verify,
week-close, wp-new
```

Skills are L1 files (protected by extensions-gate.sh from user edits). Users add custom skills to `.claude/skills/<name>/SKILL.md` — update.sh does not touch user-created skills (not in manifest).

Source: Glob output `.claude/skills/**`; `.claude/skills/extend/SKILL.md` §3 "Custom skills" row; `extensions-gate.sh` L15-29.

---

## §3 Hooks and Scripts Substrate

### §3.1 Hook matrix (.claude/settings.json)

Five hook event types are wired:

| Event | Hook(s) | Effect |
|---|---|---|
| UserPromptSubmit | wp-gate-reminder.sh, close-gate-reminder.sh | Injects WP Gate context + real date on day-open trigger (additionalContext, non-blocking read-only) |
| PreToolUse (Edit/Write) | extensions-gate.sh | Blocks direct L1 edits unless author_mode=true or path is FMT itself |
| PreToolUse (Edit/Write/MultiEdit) | capture-bus.sh | Dispatches enabled capture-detectors; never blocks (exit 0 always) |
| PreToolUse (Bash) | protocol-artifact-validate.sh | Validates git-committed DayPlan structure before commit |
| PreToolUse (all write + mcp) | dry-run-gate.sh | Blocks writes when dry-run sentinel active (fail-CLOSED on missing jq) |
| PostToolUse (Read/Skill) | protocol-completion-reminder.sh | Reminds to complete protocol after skill invocation |
| Stop | protocol-stop-gate.sh, capture-bus.sh | Gate: if protocol skill ran, require TodoWrite ≥3 items (warn mode); capture-bus final sweep |
| PreCompact | precompact-checkpoint.sh | Checkpoint before context compaction |

Source: `.claude/settings.json` full file (lines 1-116).

### §3.2 Hooks bypass rule (S-33)

`CLAUDE.md` §2 rule 6 (S-33) is a blocking rule: without explicit user permission, DO NOT modify `.claude/hooks/`, `.claude/scripts/`, `.iwe-runtime/`, `FMT-exocortex-template/` paths, and DO NOT bypass hooks via `--no-verify` or equivalent. When a hook blocks: (1) do not bypass, (2) write bug to governance-repo inbox, (3) report to user, (4) wait. Only bypassed when user explicitly says so.

Source: `CLAUDE.md` §2 rule 6 (S-33) verbatim.

### §3.3 Capture-bus architecture

`capture-bus.sh` is a dispatcher pattern: it sources `.claude/config/capture-detectors.sh`, iterates `DETECTORS[]` array, passes harness JSON to each enabled detector, and pipes detector stdout to `capture_writer.sh`. Detectors are isolated — one failing detector does not stop the cycle (no `set -e` in capture-bus, `set -uo pipefail` only). Three example detectors are present: `detector_decision.sh`, `detector_incident.sh`, `detector_pattern_awareness.sh`.

Source: `.claude/hooks/capture-bus.sh` lines 1-50; `.claude/detectors/` Glob output.

### §3.4 Dry-run gate (fail-CLOSED contract)

`dry-run-gate.sh` operates on a session-scoped sentinel file `/tmp/iwe-dry-run-${SESSION_ID}.flag`. If sentinel exists and is <600s old: blocks all write tools. If jq missing: fail-CLOSED (blocks by default). Sentinel cleaned on Stop event by `protocol-stop-gate.sh` line 15-17. This is an engineering-grade fail-safe: missing dependency causes safe failure, not permissive bypass.

Source: `.claude/hooks/dry-run-gate.sh` lines 1-40; `protocol-stop-gate.sh` lines 15-17.

---

## §4 Roles Taxonomy

### §4.1 Five roles observed in `roles/`

| Role | ID | Type | Automation | Scenarios |
|---|---|---|---|---|
| Стратег (Strategist) | R1 | agential (Claude, Grade 3-4) | launchd: 3 daily triggers | day-plan, session-prep, week-review, strategy-session, evening, add-wp, check-plan, day-close, note-review |
| Экстрактор (Extractor) | R2 | agential (Claude) | launchd: every 3h inbox-check | session-close, on-demand, inbox-check, knowledge-audit |
| Синхронизатор (Synchronizer) | R8 | functional (bash) | launchd: 10+ points/day | scheduler, code-scan, daily-report, sync-files, notify |
| Верификатор (Verifier) | R23 | agential (Haiku, context isolation) | on-demand + auto on Close | verify-pack-entity, verify-content, verify-wp-acceptance |
| Аудитор (Auditor) | R24 | agential (Claude) | auto Day Open step 2 + strategy | audit-plan-consistency, audit-coverage |

Source: `roles/README.md` overview table; `roles/auditor/README.md`; `roles/verifier/README.md`; `roles/strategist/README.md`; `roles/extractor/README.md`; `roles/synchronizer/README.md`.

### §4.2 Role-Contract schema

Each role directory must contain: `role.yaml` (machine-readable manifest with `name`, `id`, `type`, `display_name`, `runner`, `install.auto`, `install.priority`), `README.md`, `install.sh`. Optional: `prompts/*.md` (for agential roles), `scripts/*.sh`, `config/`. `setup.sh` scans `roles/*/role.yaml` and installs `install.auto: true` roles in priority order.

Source: `roles/ROLE-CONTRACT.md` "Required files" + "role.yaml schema" sections.

### §4.3 Comparison with Jetix brigadier + 5 experts

| Dimension | IWE roles (5) | Jetix swarm (brigadier + 5 experts) |
|---|---|---|
| Dispatch model | Synchronizer (R8, bash scheduler) orchestrates; roles are invoked by scheduler or directly by user | Brigadier (sole dispatcher; Task() tool) orchestrates 5 domain experts |
| Role type split | 3 agential (LLM) + 2 functional (bash or Haiku sub-agent) | 5 domain experts (all LLM, claude-sonnet-4-6); brigadier also LLM |
| Memory per role | Shared memory/ layer; roles read from same CLAUDE.md context | 5-layer per-agent memory (system.md, strategies.md, scratchpad, niche, mailbox) |
| Authority model | User = sole authority; agent proposes, user approves (extractor: HITL on all writes) | Ruslan = sole strategist; brigadier dispatches; experts draft + escalate |
| Scheduling | OS-level (launchd/cron) via synchronizer | No scheduled automation in Phase A; brigadier dispatches on each HITL session |
| Separation of concerns | Role ≠ Executor (DP.D.033; IP-1 equivalent) | IP-1 Role≠Executor (FPF IP-1 + Bundle 1 D-1 anti-conflation) — structural parallel |
| Verification | R23 Verifier with context isolation (loads artefact + standard, NOT creator's context) | Brigadier provenance gate (§5.5.5); engineering × critic mode |

Structural parallel: both systems apply the Role≠Executor principle (IWE: DP.D.033; Jetix: IP-1). Both use a functional dispatcher (IWE: Synchronizer R8 bash; Jetix: brigadier LLM). Key difference: IWE roles are temporally triggered (scheduler fires at 04:00, 23:00, etc.); Jetix experts are event-triggered (brigadier dispatches per cycle task).

---

## §5 Memory Lifecycle (S-35)

### §5.1 Frontmatter schema

All new `memory/*.md` files carry mandatory frontmatter (S-35 spec, CLAUDE.md §9):

```yaml
name: "..."
description: "одна строка для MEMORY.md"
type: user | feedback | project | reference | lesson | protocol
horizon: hot | warm | cold | archive
domains: [tag1, tag2]
status: active | dormant | superseded | archived
valid_from: YYYY-MM-DD
owner: user | platform
schema_version: 1
```

Source: `CLAUDE.md` §9 "Memory Lifecycle — S-35" block (verbatim frontmatter).

### §5.2 HOT/WARM/COLD/ARCHIVE policy

- `hot`: loaded every session; sum of all HOT file lines ≤150 (excluding frontmatter). HOT limit exceeded → agent proposes downgrading one HOT file to WARM before adding new one.
- `warm`: default for `project`, `reference`, `lesson`, `protocol` types; loaded on trigger.
- HOT→WARM: 14 days without access.
- WARM→COLD: 30 days.
- COLD→archive: 90 days.
- Archival is **proposed by agent** at Week/Month Close — never executed autonomously.

Source: `CLAUDE.md` §9 S-35 "Rules of horizon" block.

### §5.3 Comparison with Jetix 5-layer agent memory (Karpathy++)

| Layer | IWE | Jetix |
|---|---|---|
| L1 Core (always loaded) | CLAUDE.md (platform instructions; updated by update.sh) | agents/{id}/system.md (Core; read-only per agent body) |
| L2 Strategies / Learnings | MEMORY.md (user-facing summary; agent-maintained) | agents/{id}/strategies.md (Layer-2 self-write; DRR entries) |
| L3 Working memory | memory/*.md (protocol specs, feedback, reference; lazy/hot) | agents/{id}/scratchpad.md (ephemeral per session) |
| L4 Domain slice | Pack repos (domain knowledge; separate repos) | agents/{id}/niche/ (symlinks into wiki/niches/{niche}/) |
| L5 Comms / Mailbox | governance-repo/inbox/ + Telegram notifications | comms/mailboxes/{id}.jsonl |

Key structural difference: IWE memory/ is a single shared layer across all roles (no per-role isolation); Jetix has per-agent isolated memory files. IWE compensates via the hot/warm/cold tiering (only relevant files load). Jetix compensates via per-agent niche symlinks.

IWE `memory/` ≤11 file constraint is structurally equivalent to Jetix's "read this file (Layer 1) + shared-protocols (runtime contract) + strategies.md (Layer 2)" read-order discipline — both enforce slim hot-context surfaces.

---

## §6 MCP Integration

### §6.1 Declared MCP servers

`.mcp.json` declares one server:

```json
{
  "mcpServers": {
    "iwe-knowledge": {
      "type": "http",
      "url": "https://mcp.aisystant.com/mcp"
    }
  }
}
```

`iwe-knowledge` is the IWE Knowledge Gateway — described in `ONTOLOGY.md` §2 as "Navigation знаний / Knowledge Navigation / DP.NAV.001": hybrid search across Pack and guides. It is the primary retrieval surface for the `/fpf` skill's `iwe-knowledge search()` calls.

Source: `.mcp.json` full file; `ONTOLOGY.md` §2 "iwe-knowledge (mcp.aisystant.com/mcp)" row; `.claude/skills/fpf/SKILL.md` step 3 "iwe-knowledge search" calls.

### §6.2 Additional MCPs (from settings.json permissions)

`.claude/settings.json` `allow` array names additional MCP tool permissions:

- `mcp__google-drive__*` (search_files, list_files, create_folder, get_drive_info, list_shared_drives)
- `mcp__railway__*` (list-projects, list-services, list-variables)
- `mcp__ext-linear__search_issues`

These are permitted but not declared in `.mcp.json` — they are configured separately via `claude.ai/settings/connectors` per the CI check in `validate-template.yml` line 164-168. They represent optional integrations (Google Drive, Railway platform, Linear project management) that users may or may not enable.

Source: `.claude/settings.json` permissions.allow array lines 4-15; `.github/workflows/validate-template.yml` "Check MCP documentation" step lines 162-168.

### §6.3 User MCP configuration

`extensions/mcp-user.json` is explicitly excluded from update-manifest (generate-manifest.sh EXCLUDE_EXACT line 48). Users add personal MCP servers via this file without it being overwritten. This is the L3 / user-space MCP surface.

Source: `generate-manifest.sh` EXCLUDE_EXACT array line 48; `.claude/skills/extend/SKILL.md` §3 extensions table row "mcp-user.json".

---

## §7 Update Mechanism

### §7.1 Mechanism overview

`update.sh` v2.1.0 operates on HTTP manifest fetch (no shared git history required). Protocol:

1. Self-update: fetches `update.sh` from upstream; if hash differs, replaces self and re-executes.
2. Fetch `update-manifest.json` from `raw.githubusercontent.com/TserenTserenov/FMT-exocortex-template/main/`.
3. Compare each file in manifest against local hash.
4. Present preview: new files, updated files (with line-diff count), deprecated files.
5. User confirmation (or `--yes` flag) before applying.
6. Apply: copy new/updated files; delete deprecated.
7. Preserve: extensions/, params.yaml, README.md, LICENSE — explicitly never touched.

For CLAUDE.md specifically: a 3-way merge is used (`.claude.md.base` stores upstream base). User edits in §8 / §9 (L2/L3) survive the merge; L1 (§1-§7) is replaced by upstream.

Source: `update.sh` lines 1-200; `README.en.md` L173-178 "Updates" section; `.claude/skills/iwe-update/SKILL.md` steps 3a-3c.

### §7.2 Manifest-based update vs Jetix no-distribution model

| Dimension | IWE update.sh | Jetix |
|---|---|---|
| Distribution model | Template distribution: upstream pushes manifest; users pull via bash update.sh | No distribution model in Phase A — single repo, single operator (Ruslan) |
| Version tracking | `update-manifest.json` version field; CHANGELOG.md; CI validates sync (validate-template.yml) | Agents updated in-place via git; no manifest |
| User customisation preservation | Explicit exclude list in manifest; 3-way merge for CLAUDE.md | Not applicable (single-user; no downstream forks) |
| Upgrade regression testing | CI: fresh-install smoke + upgrade-flow simulation (prev version → HEAD) | Not present Phase A |
| Platform vs user layer enforcement | Extensions gate hook (L1 protect) + author_mode flag | Q2 single-writer rule (brigadier-only canonical writes) + write_scope_glob in frontmatter |

Structural note: IWE's L1/L2/L3 boundary enforcement (extensions-gate.sh blocking direct L1 edits) is architecturally parallel to Jetix's Q2 single-writer rule + `write_scope_glob: swarm/wiki/drafts/**` per agent. Both systems protect a platform layer from user/agent direct mutation and route mutations through a controlled path (extensions/ vs drafts/).

---

## §8 F-G-R Production Readiness Audit

Each subsystem rated on Formality (F), Group-scope (G), Reliability (R) per CLAUDE.md §4.1 rule "F-G-R DOGFOOD".

| Subsystem | F | G | R | Evidence |
|---|---|---|---|---|
| OWC Protocol (CLAUDE.md §2 rules 1-5) | F8 | Всех пользователей IWE | R-high | Blocking rules, pre-commit gate enforced by CI smoke-test; protocol-artifact-validate.sh runs in CI matrix (ubuntu + macOS, 2 gov_repo variants) |
| Extensions mechanism (extensions/*.md + load-extensions.sh) | F6 | Всех пользователей IWE | R-high | Design explicit in extend/SKILL.md; naming convention documented; update.sh exclusion guaranteed by manifest EXCLUDE_EXACT |
| Roles (R1 Strategist + R2 Extractor + R8 Synchronizer) | F6 | Пользователей с launchd/cron | R-medium | ROLE-CONTRACT.md formal spec; role.yaml schema; install.sh pattern; scheduler catch-up logic documented. Dependency: OS scheduler (launchd/cron) availability |
| R23 Verifier (context isolation) | F5 | Advanced users | R-medium | Defined in PACK-verification VR.R.001; prompts present; context isolation principle stated; no automated invocation test visible in CI |
| R24 Auditor | F4 | Advanced users | R-medium | Defined in VR.R.002; prompts present; triggered at Day Open step 2 but mechanism is agent-level (not hook-enforced) |
| MCP iwe-knowledge (mcp.aisystant.com/mcp) | F4 | All users | R-low | Single external HTTP endpoint; no local fallback in .mcp.json; `/fpf` skill has local file fallback (step 4 "if iwe-knowledge unavailable") |
| Capture-bus + detectors | F5 | Users with captures enabled | R-medium | capture-bus.sh never blocks; detector isolation confirmed (no set -e in dispatch loop); three detectors present |
| Dry-run gate (fail-CLOSED) | F6 | All users | R-high | fail-CLOSED contract explicit (lines 19-22); sentinel TTL 600s; Stop hook cleanup; CI: protocol-artifact-validate.sh smoke |
| Parity contract (setup ↔ update) | F5 | Template maintainer | R-medium | parity-contract.yaml documents 10 patterns with grep-regex; CI: validate-template.yml runs setup/integration-contract-validator.sh but script not visible in this read |
| 3-way CLAUDE.md merge | F4 | All users on update | R-medium | Described in iwe-update/SKILL.md step 3c and 5a; implementation in update.sh uses `.claude.md.base` but full merge logic not visible in read window |
| Sync-manifest drift detection (.claude/sync-manifest.yaml) | F4 | Advanced users / template author | R-low | Detection only (not execution); pairs reference placeholder paths `<Pack-репо>`, `<Governance-репо>` requiring user configuration |

**F-grade legend (local convention mapping to FPF F-G-R):**
- F8: production-stable, formally specified, CI-verified, in use by pilots
- F6: codified rule + ≥1 successful real deployment
- F5: codified in spec + partially tested
- F4: under iteration (design stable, operational coverage partial)
- F2: staging / unstable

---

## §9 Cross-Synthesis Claims

### §9.1 Template architecture is an Orchestrator-Workers pattern with OS scheduling

**Claim:** The IWE system implements an Orchestrator-Workers architecture (Anthropic Building Effective Agents pattern) where Synchronizer R8 (bash scheduler, 11 trigger points/day) is the orchestrator and R1 Strategist / R2 Extractor are the workers. The Claude Code session itself is a separate interactive layer outside this automation loop.

- F: F5 (codified in synchronizer/README.md + role taxonomy; single-source; operational per pilot testimony implied by changelog)
- ClaimScope: holds for users with launchd/cron available (macOS primary, Linux secondary). Does not hold for `--core` minimal install (no automation, manual only).
- R: {refuted_if: "roles/synchronizer/README.md or ROLE-CONTRACT.md shows direct-call pattern without dispatcher", accepted_if: "scheduler.sh dispatches strategist.sh and extractor.sh as documented in synchronizer/README.md table"}

### §9.2 L1/L3 boundary enforcement is architecturally equivalent to Jetix Q2 single-writer

**Claim:** IWE's extensions-gate.sh (blocking direct L1 file edits) + extensions/ user-space pattern is structurally equivalent to Jetix's Q2 single-writer (brigadier-only canonical writes) + `write_scope_glob: swarm/wiki/drafts/**` per agent. Both systems protect a platform layer from mutation by enforcing a controlled write path.

- F: F4 (cross-system structural analogy; not formally proven — observable from implementation patterns in both repos)
- ClaimScope: architectural analogy only; implementation differs (bash hook vs agent frontmatter scope). Analogy breaks if Jetix adds per-agent write expansion or if IWE adds role-level L1 write permissions.
- R: {refuted_if: "extensions-gate.sh allows direct L1 edits in normal user mode OR Jetix experts can write to swarm/wiki/canonical/ without brigadier", accepted_if: "extensions-gate.sh blocks .claude/skills/ and memory/protocol-* for non-author users (confirmed line 15-29) AND Jetix expert write_scope_glob excludes canonical/ (confirmed in agent frontmatter)"}

### §9.3 Memory hot-context discipline is convergently similar to Jetix read-order

**Claim:** IWE's ≤11 file / ≤150 hot-line memory constraint and Jetix's "read this file (Layer 1) + shared-protocols + strategies.md" read-order discipline represent convergent solutions to the same problem: preventing context-window pollution by uncontrolled memory growth.

- F: F4 (design-level convergence; no formal cross-study)
- ClaimScope: both systems target single-user, single-session AI-assisted knowledge work. Unknown whether the 150-line constraint would hold for team-level or multi-domain use.
- R: {refuted_if: "IWE memory accumulates to >300 total hot lines across all users without ill effect, invalidating the 150-line theory", accepted_if: "SOTA.002 context pollution research (cited in day-open/SKILL.md) supports the constraint"}

---

## §10 Dissents

**Dissent D-1: author-only dt-collect.sh code present in public template**

- source_cell: engineering × integrator (this cell, self-dissent)
- claim: `roles/synchronizer/README.md` section "Author-only scripts" documents that `dt-collect.sh` and `dt-collect-neon.py` (requiring `NEON_URL` + `DT_USER_ID` secrets) are distributed in the public template but guarded by environment variable presence check. The comment "код при этом остаётся как маркер будущей фичи" (code remains as a future feature marker) is an engineering smell: shipping credential-dependent code as a "marker" in a public template can confuse users and creates a maintenance obligation.
- F: F4 (one-source engineering observation; not a user-facing bug but a design-quality concern)
- ClaimScope: affects template users who inspect synchronizer scripts; not a security risk (guards in scheduler.sh prevent execution without secrets)
- R: {refuted_if: "dt-collect.sh is removed from FMT in a subsequent version OR clearly documented as author-internal with remove-from-template note", accepted_if: "dt-collect.sh remains in template without removal plan (current state per synchronizer/README.md lines 41-61)"}

**Dissent D-2: iwe-knowledge is a single external HTTP dependency with no local fallback in .mcp.json**

- source_cell: engineering × integrator (self-dissent)
- claim: `.mcp.json` declares only one MCP server (`https://mcp.aisystant.com/mcp`). If this endpoint is unavailable, the `/fpf` skill degrades to local file grep (SKILL.md step 4 fallback exists), but no other skill explicitly documents a fallback. This is a single point of failure for the knowledge navigation layer.
- F: F4 (structural observation from .mcp.json and /fpf SKILL.md; no failure-mode test evidence)
- ClaimScope: affects users who depend on iwe-knowledge for Pack search in non-trivial sessions
- R: {refuted_if: "other skills also have documented local fallbacks OR mcp.aisystant.com has SLA documentation", accepted_if: "only /fpf has explicit fallback in SKILL.md step 4 (confirmed) AND no SLA doc found in repo (confirmed by absence in README.en.md FAQ)"}

---

## §11 Residual Open Questions

1. **`memory/` actual file list**: Glob on `memory/**/*` returned no results — this directory may be user-space only (not tracked in template). What files does `setup.sh` populate there? (Relevant for §5 memory lifecycle comparison accuracy.)
2. **`seed/` directory**: Glob on `seed/**/*` returned no results. README.en.md L137 mentions `bash setup.sh` — does setup.sh materalise memory/ from seed/? (`generate-manifest.sh` excludes `seed/` from manifest, line 26.)
3. **`extensions/` actual content**: No files found via Glob. This is expected (user-space; only the gate hook and README are platform-tracked). Confirms L3 separation is working as designed.
4. **Integration contract validator**: `setup/integration-contract-validator.sh` referenced in CI but not read — 8 specific detectors are run. Content not examined.
5. **`roles/` runtime entry**: Glob on `roles/**/*` found no `role.yaml` files despite ROLE-CONTRACT.md documenting them as required. Either they are generated by setup.sh or exist only in the author's instance. Affects §4 role-contract analysis confidence.

---

## Structured Output Packet

```yaml
mode: integrator
context:
  task_id: task-fpf-iwe-phase-b-2026-05-17
  cycle_id: cyc-iwe-phase-b-2026-05-17

summary: "FMT-exocortex-template is a bash+Markdown platform distribution (L1/L2/L3 three-layer) implementing OWC protocol, 5 agent roles (R1 Strategist / R2 Extractor / R8 Synchronizer / R23 Verifier / R24 Auditor), extensions-gate L1 protection, OS-scheduler orchestration, HTTP manifest update (no shared git history), one MCP server (iwe-knowledge), and a memory hot-context discipline (≤11 files, ≤150 hot lines). Architecture converges with Jetix on Role≠Executor, Q2-equivalent layer enforcement, and slim hot-context discipline. Key F-G-R: OWC protocol is F8/R-high; extensions mechanism F6/R-high; MCP iwe-knowledge F4/R-low (single external HTTP, partial fallback). 2 dissents: dt-collect.sh author-only code in public template; single MCP endpoint with no declared SLA."

inputs:
  - {cell: "engineering × integrator (this)", draft_path: "swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-engineering-integrator-fmt-structure.md", summary: "structural analysis of FMT-exocortex-template as software artefact"}

synthesis:
  - claim: "FMT is a Base/Formats repo implementing a 3-tier (L1 platform / L2 pack / L3 user) architecture with bash-enforced layer boundaries, OS-scheduled role automation, and HTTP-manifest distribution"
    F: F6
    ClaimScope: "holds for FMT-exocortex-template v0.22.0 as observed; unknown for Pack or DS-type repos"
    R: {refuted_if: "REPO-TYPE.md or update.sh contradicts the 3-tier model", accepted_if: "REPO-TYPE.md L1-4 + ONTOLOGY.md §2 + CLAUDE.md §7 all confirm the model (confirmed)"}

  - claim: "The extensions gate hook (extensions-gate.sh) + extensions/ user-space pattern is architecturally equivalent to Jetix Q2 single-writer + write_scope_glob enforcement"
    F: F4
    ClaimScope: "architectural analogy; implementation differs (bash vs agent frontmatter); analogy breaks on permission expansion"
    R: {refuted_if: "either system allows uncontrolled writes to protected layer", accepted_if: "both systems block protected-layer writes except through controlled path (confirmed for both)"}

  - claim: "IWE memory lifecycle (≤11 files, ≤150 hot lines, HOT/WARM/COLD/ARCHIVE) is a convergent solution to the same context-pollution problem Jetix addresses with read-order discipline"
    F: F4
    ClaimScope: "single-user, single-session; unknown at team scale"
    R: {refuted_if: "IWE accumulates >300 hot lines without ill effect", accepted_if: "SOTA.002 citation in day-open/SKILL.md supports the constraint"}

dissents:
  - source_cell: "engineering × integrator (self-dissent D-1)"
    claim: "dt-collect.sh author-only credential-dependent code distributed in public template is an engineering smell"
    F: F4
    ClaimScope: "not a security risk (guards present); design-quality concern for template clarity"
    R: {refuted_if: "dt-collect.sh removed or clearly marked author-internal in subsequent version", accepted_if: "dt-collect.sh present with 'marker' rationale (current state confirmed)"}

  - source_cell: "engineering × integrator (self-dissent D-2)"
    claim: "iwe-knowledge single external HTTP MCP endpoint with no declared SLA is a single-point-of-failure for knowledge navigation"
    F: F4
    ClaimScope: "affects non-trivial sessions; /fpf has local fallback; other skills may not"
    R: {refuted_if: "SLA documentation found OR all skills have local fallbacks", accepted_if: "only /fpf has explicit fallback (confirmed); no SLA doc (confirmed by absence)"}

residual_open_questions:
  - "memory/ actual tracked files (Glob returned empty — user-space only?)"
  - "seed/ directory content (excluded from manifest; may be setup.sh source)"
  - "role.yaml files not found in roles/ — generated by setup.sh or author-only?"
  - "integration-contract-validator.sh 8 detectors — content not read"

recommended_next_step:
  - {action: "brigadier integrates this + knowledge-synth + philosophy-critic returns into 02-iwe-deep-v2.md", dispatch_target: "brigadier-promote", rationale: "all three peer cells cover structural / semantic / epistemic dimensions of IWE"}

proposed_writes:
  - path: swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-engineering-integrator-fmt-structure.md
    frontmatter: {title: "FMT-exocortex-template — Engineering Structural Integration (IWE Phase B)", type: integration-synthesis, expert: engineering-expert, mode: integrator, task_id: task-fpf-iwe-phase-b-2026-05-17}
    body: "<this file>"
    edges_to_add: []

provenance:
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/REPO-TYPE.md", range: "1-8", quote: "Тип: Base/Форматы ... Source-of-truth: yes (для формата экзокортекса)"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/README.en.md", range: "1-12", quote: "Repository type: Base/Formats (FMT) — template distribution. After forking, it becomes your personal environment"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/README.en.md", range: "155-179", quote: "Updates — bash update.sh updates the platform while preserving your extensions/, params.yaml, and CLAUDE.md edits (3-way merge)"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md", range: "§7 L1/L2/L3 block", quote: "3 слоя: L1 (§1-§7) = платформа (update.sh). L2 (§8) = staging. L3 (§9) = авторское"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md", range: "§2 rule 6 S-33", quote: "Без явного разрешения пользователя НЕ менять скрипты шаблона (.claude/hooks/, .claude/scripts/, .iwe-runtime/, FMT-exocortex-template/)"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md", range: "§9 S-35", quote: "Обязательный frontmatter для всех новых файлов memory/*.md: name, description, type, horizon, domains, status, valid_from, owner, schema_version"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md", range: "§4 Memory table", quote: "Политика: ≤11 файлов. Горячие (читаются каждую сессию): ≤100 строк. Протоколы (lazy, по триггеру): ≤150."}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/.claude/settings.json", range: "1-116", quote: "UserPromptSubmit: wp-gate-reminder.sh, close-gate-reminder.sh; PreToolUse Edit|Write: extensions-gate.sh; Stop: protocol-stop-gate.sh, capture-bus.sh"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/.claude/hooks/extensions-gate.sh", range: "1-36", quote: "if echo $FILE_PATH | grep -qE '.claude/skills/|memory/protocol-' ... echo decision:block ... Extensions Gate: платформенные (L1) и пользовательские (L3) файлы — разные слои"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/.mcp.json", range: "1-10", quote: "iwe-knowledge: type: http, url: https://mcp.aisystant.com/mcp"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/ONTOLOGY.md", range: "30-32", quote: "Навигация знаний | Knowledge Navigation | DP.NAV.001 | Gateway iwe-knowledge (mcp.aisystant.com/mcp) — hybrid search по Pack и guides"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/roles/README.md", range: "9-15", quote: "Стратег R1 ИИ-агент (Claude) 9 launchd; Экстрактор R2 ИИ-агент (Claude) 4 launchd; Синхронизатор R8 Bash-инструмент 5 скриптов launchd"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/roles/ROLE-CONTRACT.md", range: "8-20", quote: "Обязательные файлы: role.yaml — Машиночитаемый манифест: идентичность, тип, установка; README.md; install.sh"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/roles/synchronizer/README.md", range: "41-61", quote: "dt-collect.sh ... требуют прямого доступа к production-БД Neon ... код при этом остаётся как маркер будущей фичи"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/roles/verifier/README.md", range: "28-34", quote: "Верификатор загружает: Артефакт (результат), Эталон (Pack/SPF) ... НЕ загружает: Задание создателя, Промежуточные рассуждения — context isolation"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/params.yaml", range: "1-70", quote: "params.yaml — пользовательские настройки ... update.sh НЕ перезаписывает этот файл ... author_mode: false"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/.claude/parity-contract.yaml", range: "1-88", quote: "pairs: setup ↔ update patterns: iwe-paths, memory-files, build-runtime-invoke, cross-platform-sed, workspace-dir, script-dir, help-flag, version-flag"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/update.sh", range: "1-80", quote: "REPO=TserenTserenov/FMT-exocortex-template ... RAW_BASE=raw.githubusercontent.com ... Step 0: Self-update ... Step 1: Fetch manifest"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/generate-manifest.sh", range: "23-49", quote: "EXCLUDE_EXACT: README.md, README.en.md, CONTRIBUTING.md, LICENSE, params.yaml, extensions/day-close.after.md, extensions/mcp-user.json"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/.claude/skills/extend/SKILL.md", range: "34-50", quote: "Extension points: protocol-close checks, day-open before/after/checks, day-close checks/after, week-close before/after, protocol-open after"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/.claude/skills/day-open/SKILL.md", range: "1-30", quote: "БЛОКИРУЮЩЕЕ: пошаговое исполнение ... Каждый шаг алгоритма → отдельная задача (pending → in_progress → completed)"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/.claude/hooks/dry-run-gate.sh", range: "1-40", quote: "fail-CLOSED: jq missing, blocking by default ... SENTINEL=/tmp/iwe-dry-run-${SID}.flag ... TTL 600 seconds"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/.github/workflows/validate-template.yml", range: "48-75", quote: "matrix os: [ubuntu-latest, macos-latest] × gov_repo: [DS-strategy, DS-pilot-strategy] ... Run integration-contract-validator.sh ... Run smoke-test-fresh-install.sh"}
  - {path: "raw/external/tseren-github-2026-05-17/FMT-exocortex-template/ONTOLOGY.md", range: "44-58", quote: "Harness (упряжь) | Harness | DP.D.025 | IWE как harness для интеллектуальной работы ... ИИ-система | AI System | DP.ROLE.001 | Claude Code — исполнитель ролей"}

confidence: high
confidence_method: artefact-direct-read
escalations: []
```
