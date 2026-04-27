---
title: Part 1 — engineering-expert multi-mode cell (critic + scalability + integrator)
date: 2026-04-28
phase: C-1-cell
expert: engineering-expert
modes: [critic, scalability, integrator]
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 1
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-1-system-state-persistence.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/engineering-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/event-sourcing-cqrs.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/unix-philosophy.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/clean-code.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
  - decisions/LOCKS-D29-ADDENDUM-2026-04-26.md
confidence: high
confidence_method: rubric-pass-rate
F: F4
ClaimScope: "Holds for Part 1 (System State Persistence) in Jetix Phase-A single-node single-founder configuration. Does not govern RUSLAN-LAYER repo names, branch names, or executor bindings."
R:
  refuted_if: "Cross-fork provenance schema (P1.1) cannot roundtrip through synthetic Phase B partner test fixture while preserving audit chain"
  accepted_if: "All three Wave C bullets P1.1/P1.2/P1.3 have Hamel-binary acceptance predicates satisfied and no IP-1 violations found by critic mode pass"
---

# Part 1 — Engineering-Expert Multi-Mode Cell (Critic + Scalability + Integrator)

**Dispatch mode:** MULTI-MODE (critic + scalability + integrator run in parallel)
**Tag convention:** [CRITIC] / [SCALABILITY] / [INTEGRATOR] mark mode-of-origin for each finding

---

## §A Inputs — Full Enumeration

**[INTEGRATOR]** Part 1 is the substrate — it has no upstream Part dependency. Its inputs are heterogeneous write requests arriving from all other Parts, not structured data from a single upstream. Enumerating precisely:

| Source | Data shape | Event trigger |
|---|---|---|
| All Parts 2-10 | Committed file write :: YAML/JSON/Markdown at a repo-rooted path | State-change event in any downstream Part |
| Part 6 (Governance) | AWAITING-APPROVAL gate packet :: frontmatter `status: acked` + `acked_by: ruslan` + `acked_at: <ISO>` | HITL ack received — human promotes draft to canonical |
| `CLAUDE.md` + `.claude/config/*.yaml` | Declarative YAML config :: parsed key-value namespace | Skill invocation boot OR `git pull` config refresh |
| `shared/schemas/*.json` | JSON Schema draft-07 :: validation schema | Pre-commit hook fire OR `/lint` run |
| `tools/git-hooks/pre-commit-format.sh` (P1.2 stub) | Commit message string :: stdin from `git commit` hook | git commit attempt |
| Cross-fork import (D27, Phase B) | Cross-fork provenance record :: `shared/schemas/cross-fork-provenance.json` (P1.1 stub) | Phase B partner fork export event |

**[CRITIC]** The Wave A interface card lists "schema validation request" as a trigger but does not name the specific schemas. This is a cargo-cult risk: citing schema validation without naming the schema paths leaves the input underspecified. Consequence: the canonical architecture.md MUST enumerate `shared/schemas/message.schema.json`, `shared/schemas/cross-fork-provenance.json` (new, P1.1), and any other JSON Schema files by path. Generic "schema validation" without path reference fails Conformance Check 5 (external-dep without failure-mode declaration). [src:part-1-system-state-persistence.md:§A; src:AUDIT:§4.5]

**[INTEGRATOR]** The `CLAUDE.md` config input is interesting because it is also an OUTPUT of Part 1 (it is committed through git). This apparent circularity resolves cleanly: CLAUDE.md is read at boot as config-input; it is written through git as committed-state. The write path is serialized (you cannot change CLAUDE.md and immediately benefit from its new value within the same git transaction). This is correct and non-circular. [F4|G:Part 1 Jetix Phase-A|R-high]

---

## §B Outputs — Including raw-task-return-packet slot

**[INTEGRATOR]** Part 1 produces three classes of output, which the Wave A card lists correctly. The critical gap identified here concerns the **raw-task-return-packet slot** (UND-1 / OQ-3):

| Output | Consumer | Data shape | Event published |
|---|---|---|---|
| Durable committed artefact | All Parts 2-10 | Stable path in `git log --oneline` | commit-completed event |
| `/company-status` snapshot | Part 9 (Owner Interaction Scaffold) | Markdown ≤80 lines, zero network calls [src:AUDIT:§5.1] | owner-review trigger |
| `/knowledge-diff` delta | Part 9 | Markdown delta report between two git log dates | periodic or on-demand owner trigger |
| Audit trail (`git log` chain) | Part 6 (Governance) | Append-only ordered immutable events per Greg Young [src:event-sourcing-cqrs.md:§4 Source 2] | provenance-query |
| Repo integrity signal | Part 8 (Health Monitoring) | `git fsck` exit code + object error count | periodic health-poll |
| **raw-task-return-packet frozen field** | Part 5 (Compound Learning / Task return) | `git_commit_hash: <sha>` frozen after commit | task-completion event |

**[CRITIC]** The raw-task-return-packet frozen field is currently undeclared in Part 1's interface card. Every task-return packet from any agent that produces a canonical write must include `git_commit_hash` as a frozen (post-commit) field. Without this, Part 5 cannot verify that the compounded state it references in a strategies.md DRR entry corresponds to an actual commit. This is an AP-ENG-10 trigger (external-dep without failure-mode declaration at the interface level). Consequence: the canonical architecture.md must declare `git_commit_hash` as a mandatory frozen output field in the task-return-packet schema. [F4|G:Part 1 + Part 5 interface|R-medium]

---

## §C Side-effects — Append-only, no in-place mutation

**[INTEGRATOR]** Every Part 1 side-effect is a git commit. There are no side-channel writes. Three specific side-effects, each with its append-only guarantee sourced from Greg Young's Reversal Transactions pattern:

**C.1 Git history append.** Every accepted write is a new commit appended to the history. `git revert` produces a compensating commit (a new event that describes the undo) — it does NOT rewrite history. Per Greg Young [src:event-sourcing-cqrs.md:§3 Source 2, p.31]: "There is no Delete in event sourcing... a compensating event is the correct mechanism." Applied to Jetix D25: `git revert <hash>` is the canonical undo; `git reset --hard` or `--amend` are constitutional violations. Consequence: any skill or hook that calls `git reset` or `git commit --amend` on the canonical branch is a D25 violation and must be blocked by the pre-commit hook layer. [src:part-1-system-state-persistence.md:§E Laws; src:AUDIT:§0 git-activity]

**C.2 Schema validation gate (pre-commit).** The pre-commit hook validates schema but produces no file write. Validation failure produces stderr output only and blocks the commit. This is correct: validation is a gate, not a state change. The hook must be idempotent — running it twice on the same commit produces the same result. [F5|G:Part 1 git hook discipline|R-high]

**C.3 Commit-format lint (P1.2 new).** The `tools/git-hooks/pre-commit-format.sh` hook will validate commit message format as a pre-commit side-effect. Fail = block commit with human-readable error to stderr. No file mutation. Idempotent.

**[CRITIC]** The Wave A card states "Schema validation artefact: validation is a gate check, not a file write; failures produce stderr only." This is correct but incomplete. The card does not specify what happens to false-positive lint failures (AP-ENG-5 analog: tool-eval without acceptance predicate). Consequence: the canonical architecture.md must declare the lint false-positive rate budget (target: 0 false positives on valid commits per the P1.2 acceptance predicate) and the bypass mechanism (human operator may `git commit --no-verify` only with explicit HITL ack, itself committed as a subsequent record). [F4|G:Part 1 commit-format discipline|R-medium]

---

## §D Dependencies — Typed A.14 Edges

**[INTEGRATOR]** Part 1 has NO upstream Part dependencies. This is its defining structural property. Citing the FPF A.14 typing requirement: [src:levenchuk-shsm-fpf.md:§4 P4]

```
Upstream: NONE — Part 1 is the substrate root; all Parts operate-in it
```

Downstream (other Parts depend on Part 1):

| Edge | Edge type (A.14) | Rationale | Source |
|---|---|---|---|
| Parts 2-10 → Part 1 | `operates-in` | Content entities (wiki entries, agent files, CRM records) reside on the git substrate; destroying Part 1 destroys their persistence, but they are not constitutive parts of git itself. `ComponentOf` would be wrong — KB content is a separate entity that happens to persist on Part 1's filesystem. [FPF §3.5 A.14] | [src:part-1-system-state-persistence.md:§D A.14 note] |
| Part 6 → Part 1 | `methodologically-uses` | Governance artefacts (AWAITING-APPROVAL packets, LOCKED tags, `decisions/*.md` files) are authored through Part 1's commit interface as their enforcement mechanism. Part 6's method requires Part 1's git discipline. | [src:part-1-system-state-persistence.md:§D] |
| Part 8 → Part 1 | `operates-in` + `AspectOf` | Health monitoring reads Part 1's git history and fsck status; repo health is an observable aspect of Part 1. The monitoring function (Part 8) is an aspect of the substrate's observable state. | [FPF-Spec A.14 L.17478; src:clean-code.md:§4 P1 deep-modules] |

**[CRITIC]** The `AspectOf` edge for Part 8 is a new claim not present in the Wave A card. It is defensible: `git fsck` output and commit cadence ARE aspects of Part 1 — they describe properties of the substrate, not separate entities. But this edge should be validated by the philosophy-expert in critic mode against FPF-Spec A.14 L.17478 before being promoted to canonical. Flagging as [F3|G:Part 1 → Part 8 dependency|R-medium — pending philosophy-expert critic pass].

**[INTEGRATOR]** The `cross-fork-provenance.json` schema (P1.1) introduces a new dependency class: **Phase B partner fork → Part 1**. The correct A.14 edge for an imported cross-fork record is `operates-in` (the imported record resides in Part 1's substrate after import) with a `constrained-by` edge to the cross-fork schema (the import is constrained by the validation rules in `shared/schemas/cross-fork-provenance.json`). The fork itself is external; its imported provenance record is internal. This A.14 analysis must appear in the canonical architecture.md §D section. [F3|G:Phase B cross-fork dependency|R-low — Phase B not yet materialised]

---

## §E Boundary — L/A/D/E Lanes

Per FPF A.6.B [src:levenchuk-shsm-fpf.md:§4 P6]. Full lane enumeration for Part 1:

### Laws (invariants — violations are constitutional defects)

1. **Append-only commit discipline.** No `--amend`, no `--no-verify`, no force-push on canonical branch. Reversal is exclusively via `git revert` (compensating event). Sourced from D25 [src:part-1-system-state-persistence.md:§E Laws] AND Greg Young's no-delete pattern [src:event-sourcing-cqrs.md:§3 Source 2 p.31]. Concrete consequence: any CI pipeline step, hook, or agent action that calls `git reset --hard` on `main` is a constitutional defect requiring HITL review and a corrective `git revert` commit.

2. **`[area] verb what (why)` commit format.** Every canonical commit message MUST match `^\[(area)\] (verb) (subject)( \(why\))?$`. Sourced from D25 [src:CLAUDE.md Global Rule 7; src:part-1-system-state-persistence.md:§E Laws]. Concrete consequence: the `pre-commit-format.sh` hook (P1.2) enforces this as a blocking gate — a commit that fails format validation is rejected at the client side before it reaches the repo.

3. **Offline-first guarantee for `/company-status` and `/knowledge-diff`.** Every invocation of either skill makes ZERO network calls. `curl`, `wget`, any HTTP client library call, any API call is a constitutional violation. Sourced from D26 alignment [src:wave-c-worklist.md:Bullet 3] and FUNDAMENTAL §6.1 (AI tools do not call external services autonomously). Concrete consequence: if the test stub (`tools/tests/test-offline-guarantee.sh`) intercepts a network syscall, the skill MUST halt with a non-zero exit code and surface the specific syscall attempted — not continue with degraded output.

4. **Filesystem = SoT; Notion is not in any write path.** Sourced from D17 [src:engineering-expert.md:§3 D17; src:part-1-system-state-persistence.md:§E Laws]. Concrete consequence: any skill modification that proposes writing state to Notion before committing to git is a D17 violation; the AWAITING-APPROVAL gate blocks it.

5. **No canonical state outside git.** State written only to an in-memory structure, a `.env` file, or a tool-specific cache that is not git-committed does not exist as canonical Jetix state. Sourced from FUNDAMENTAL §2.1 [src:part-1-system-state-persistence.md:§E Laws; src:event-sourcing-cqrs.md:§4 Principle 1].

### Admissibility (acceptance criteria for inputs)

- Path is under repo root; not `~/.ssh/`, `/etc/`, `.env*`, `private/` [src:CLAUDE.md Global Rule 6]
- JSON/YAML files pass schema validation against the relevant `shared/schemas/*.json` definition before commit
- Part 6 promotion inputs carry `status: acked`, `acked_by: ruslan`, `acked_at: <ISO>` in frontmatter [src:part-1-system-state-persistence.md:§E Admissibility]
- **New (P1.1):** Cross-fork import inputs must validate against `shared/schemas/cross-fork-provenance.json` and carry `F-G-R-on-imported-claims` non-null before integration into the native audit log

### Deontics (obligations toward consumers)

- Part 1 MUST preserve every committed state indefinitely (append-only; no deletion without HITL ack)
- Part 1 MUST expose a queryable log (`git log --oneline`, `/knowledge-diff`) for provenance reconstruction
- Part 1 MUST provide reversibility via `git revert` — not `git reset` [src:event-sourcing-cqrs.md:§4 Principle 1; src:unix-philosophy.md:§4 P2]
- **New (P1.2):** Part 1's pre-commit hook MUST block malformed commit messages AND produce a human-readable error to stderr naming the specific format violation
- **New (P1.3):** Part 1's `/company-status` and `/knowledge-diff` skills MUST exit non-zero if any network call is detected during execution; the offline guarantee is not optional

### Effects (measurable outcomes)

- After successful commit: artefact durable, path-addressable, in `git log` within 1 second [src:part-1-system-state-persistence.md:§E Effects]
- `/company-status`: ≤80-line markdown snapshot, zero network calls, exit 0 [src:AUDIT:§5.1]
- `git fsck`: 0 object errors (target SLI) [src:part-1-system-state-persistence.md:§E Effects]
- Pre-commit hook (P1.2): blocks malformed commit with exit non-zero + stderr message within 50ms
- Offline test (P1.3): exit 0 if zero network calls detected; exit non-zero with syscall name if any network call detected

---

## §F Anti-scope

Generic (all Foundation parts per FUNDAMENTAL §6):
- Does NOT make strategic decisions [FUNDAMENTAL §6.1]
- Does NOT substitute for founder agency [FUNDAMENTAL §6.2]
- Does NOT use engagement-economy patterns [FUNDAMENTAL §6.3]

Part-specific:
- Does NOT enforce commit message **content** correctness (whether the message accurately describes the change). [CRITIC] This is the most important anti-scope to preserve. Content correctness is a human judgment call — it belongs to Part 6 (Governance) via lint check at a later quality gate. Part 1's P1.2 hook enforces ONLY format. Conflating format enforcement with content enforcement would give the pre-commit hook more authority than it should have, and would risk false-positive blocks on valid commits with unusual but accurate descriptions.
- Does NOT own AWAITING-APPROVAL gate logic — Part 1 executes the physical commit when Part 6 acks; it does not decide whether an ack is warranted
- Does NOT own Notion sync or any external-service write path [D17]
- Does NOT own schema authorship — schemas in `shared/schemas/` are authored via normal Part 6 governance flow; Part 1 validates against them, does not define them
- Does NOT own the cross-fork reconciliation architecture (Phase B work, declared-deferred) — Part 1's P1.1 contribution is the STUB schema with deferred-phase label; the reconciliation algorithm is Phase B

**[CRITIC]** [SCALABILITY] The current Wave A anti-scope entry "does NOT enforce commit message content correctness" is correct but must be made more precise in the canonical architecture.md. The boundary sentence: "Part 1 enforces `^\[(area)\] (verb) (subject)( \(why\))?$` regex structure; it does not evaluate whether `verb` accurately describes what the commit does." This precision prevents scope creep where a future developer argues the hook should check that "add" is not used when files are deleted. That check is a content concern; the hook does not own it.

---

## §G F-G-R Tagging — Full Table

Per FPF B.3 [src:levenchuk-shsm-fpf.md:§4 P5]:

| Artefact | F (Formality) | G (ClaimScope) | R (Reliability) | Rationale |
|---|---|---|---|---|
| Git commit + commit message | F5 — codified rule; hook layer enforcing (P1.2 new; log-only cycle 2, blocking Phase B per §6.1 BOSC table) | Holds for Jetix mono-repo; unknown for multi-repo or distributed fork | R-high — cryptographic SHA checksum is the proof-of-existence; refuted only by repo corruption | [src:part-1-system-state-persistence.md:§G] |
| YAML config read result | F4 — operational convention; `.claude/config/*.yaml` is declared source | Holds for skills invoked within repo root; not applicable to external tool invocations | R-medium — config can drift if edited outside git (D25 violation); mitigated by hook enforcement | [src:AUDIT:§1.1] |
| `/company-status` snapshot | F3 — multi-source informal; derives from `git log` + `ls` counts + no network | Holds at snapshot timestamp; may be stale within ≤1 hour in active sessions | R-medium — git-derived, accurate at invocation time | [src:part-1-system-state-persistence.md:§G] |
| `git log` provenance chain | F6 — codified + ≥3 successful applications (571 commits / 30 days [src:AUDIT:§0]) | Holds for entire repo history; fork audit trails separate per D27 | R-high — immutable once committed; detected by `git fsck` | [src:part-1-system-state-persistence.md:§G] |
| `shared/schemas/cross-fork-provenance.json` (P1.1 new) | F2 — single-source stub; not yet validated against Phase B test fixture | Holds only for schema stub phase; ClaimScope extends to Phase B when test fixture passes | R-low — stub, not validated; acceptance predicate not yet satisfied | [src:wave-c-worklist.md:Bullet 1] |
| `pre-commit-format.sh` hook (P1.2 new) | F4 — operational convention when implemented; currently stub only | Holds for all commits on canonical branch once hook is active; unknown for emergency bypasses | R-medium — depends on `--no-verify` bypass policy being enforced via HITL ack | [src:wave-c-worklist.md:Bullet 2] |
| `/knowledge-diff` delta output | F4 — operational convention; skill already working [src:AUDIT:§5.1] | Holds for time-bounded git log queries within repo history | R-medium — accurate at invocation time; does not project future state | [src:engineering-expert.md:§3 D25] |
| Offline guarantee test stub (P1.3 new) | F2 — stub; requires `unshare -n` or strace infrastructure to be verified as callable | Holds once test infrastructure confirmed compatible with server OS | R-low — test-infrastructure availability unverified; flag as HARD GAP (see §K) | [src:wave-c-worklist.md:Bullet 3] |

**[CRITIC]** The two new F2-level items (cross-fork schema stub, offline test stub) are correctly low-formality. [INTEGRATOR] They must not be promoted to canonical artefacts until their acceptance predicates are satisfied. The canonical architecture.md must include this F-G-R table and annotate which items are currently at stub-level.

---

## §H Code-level Interfaces

**[INTEGRATOR]** Part 1 is a deep module (Ousterhout P1 [src:clean-code.md:§4 P1]). Its public interface is intentionally narrow:

```
NARROW PUBLIC INTERFACE                       WIDE INTERNAL COMPLEXITY
─────────────────────────────────────────────────────────────────────
git commit [area] verb what (why)             git plumbing (SHA, tree, blob, ref)
git revert <hash>                             schema validation engine
git log [--oneline] [--since] [--until]       config resolution (YAML parse)
/company-status                               snapshot assembly (git log + ls)
/knowledge-diff [--since] [--until]           delta computation (git diff + log)
/lint --check-commit-format                   regex parse + area-token lookup
```

This is Ousterhout's deep-module test applied: implementation-LoC >> interface-LoC. [src:clean-code.md:§4 P1] Concrete consequence: consumers (other Parts) never call git plumbing directly — they call the declared CLI interface. This is the Unix "everything is a commit" extension of Raymond's "everything is a file" principle. [src:unix-philosophy.md:§4 P2]

**CLI signatures (canonical for architecture.md):**

```bash
# /company-status
# Owner: swarm/lib/ shared infra (per C1 shared-protocols ownership)
# Zero network calls guaranteed (P1.3 Law)
# Output: ≤80-line markdown snapshot to stdout
/company-status [--days=N]

# /knowledge-diff
# Owner: swarm/lib/ shared infra (per C1)
# Zero network calls guaranteed (P1.3 Law)
# Output: markdown delta report to stdout
/knowledge-diff [--since=YYYY-MM-DD] [--until=YYYY-MM-DD]

# /lint --check-commit-format
# Owner: swarm/lib/ shared infra
# Trigger: standalone invocation OR as part of full /lint run
# Input: last N commits OR --all
# Output: PASS/FAIL per commit with format violation description
/lint --check-commit-format [--count=N] [--all]

# pre-commit-format.sh (git hook stub P1.2)
# Location: tools/git-hooks/pre-commit-format.sh
# Install via: git config core.hooksPath tools/git-hooks OR symlink
# Input: commit message via $1 (file path of commit message, git hook convention)
# Output: exit 0 (pass) or exit 1 + stderr message (fail)
tools/git-hooks/pre-commit-format.sh

# test-offline-guarantee.sh (test stub P1.3)
# Location: tools/tests/test-offline-guarantee.sh
# Requires: unshare -n (Linux network namespacing) OR strace-based syscall filter
# Output: exit 0 (zero network calls) or exit 1 + intercepted syscall description
tools/tests/test-offline-guarantee.sh [/company-status|/knowledge-diff]
```

**[CRITIC]** The `/lint --check-commit-format` flag extends the existing `/lint` skill (18K, current) rather than creating a new skill. This is the correct anti-duplication discipline per Hunt-Thomas DRY [src:unix-philosophy.md:§4 P4]. The canonical architecture.md must reference that `/lint` is the owner and that `--check-commit-format` is lint signal #12 (extending current 11 KB health checks, per wave-c-worklist.md Bullet 2 spec). Creating a standalone `check-commit-format` skill would be a DRY violation.

**[INTEGRATOR]** The `swarm/lib/` shared infra ownership annotation is per C1 shared-protocols.md ownership. `/company-status` and `/knowledge-diff` are already operational; the P1.3 work adds the offline guarantee test and the Law declaration, not new implementations. The Wave C work for these skills is constitutional declaration + test stub, not reimplementation.

---

## §I Data Schemas

### I.1 Cross-fork provenance schema (P1.1) — `shared/schemas/cross-fork-provenance.json`

**Foundation-vs-RUSLAN-LAYER separation:** The schema below is GENERIC (Foundation layer). Specific repo names, branch names, and executor bindings are RUSLAN-LAYER and must NOT appear in this schema. [src:wave-c-worklist.md:Bullet 1 "Fork-separation"; src:levenchuk-shsm-fpf.md:§4 P1 Foundation vs RUSLAN-LAYER]

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/cross-fork-provenance.json",
  "title": "Cross-fork provenance record",
  "description": "Schema for tracking provenance of state imported from a fork of this repository into the parent repo's canonical audit log. Phase B stub — reconciliation algorithm deferred.",
  "type": "object",
  "required": [
    "parent_repo_id",
    "parent_commit_hash",
    "fork_id",
    "fork_branch",
    "divergence_point",
    "reconciliation_strategy",
    "audit_trail_continuation",
    "f_g_r_on_imported_claims",
    "ip1_role_binding_overrides"
  ],
  "properties": {
    "parent_repo_id": {
      "type": "string",
      "description": "Stable identifier for the parent repository. GENERIC: do not embed repo URL (RUSLAN-LAYER). Use a logical ID agreed between parties.",
      "pattern": "^[a-z0-9-]+$"
    },
    "parent_commit_hash": {
      "type": "string",
      "description": "Full 40-char SHA-1 hash of the parent repo commit at divergence point.",
      "pattern": "^[0-9a-f]{40}$"
    },
    "fork_id": {
      "type": "string",
      "description": "Stable identifier for the fork. GENERIC: logical ID, not URL or branch name. RUSLAN-LAYER binds this to actual fork repo.",
      "pattern": "^[a-z0-9-]+$"
    },
    "fork_branch": {
      "type": "string",
      "description": "Branch name in the fork at the time of export. Mapped to imported-state-token in parent audit log — does NOT contaminate parent branch namespace.",
      "pattern": "^[a-zA-Z0-9/_-]+$"
    },
    "divergence_point": {
      "type": "object",
      "description": "The commit in the parent repo from which this fork diverged.",
      "required": ["commit_hash", "timestamp_utc", "description"],
      "properties": {
        "commit_hash": { "type": "string", "pattern": "^[0-9a-f]{40}$" },
        "timestamp_utc": { "type": "string", "format": "date-time" },
        "description": { "type": "string", "maxLength": 200 }
      }
    },
    "reconciliation_strategy": {
      "type": "string",
      "description": "How conflicts between fork and parent are resolved. Phase B stub: 'deferred-phase-b' is the only valid value in Phase A.",
      "enum": ["deferred-phase-b", "cherry-pick-manual", "merge-with-review", "fork-read-only"]
    },
    "audit_trail_continuation": {
      "type": "object",
      "description": "How the parent audit log references the fork's commit history without contaminating its native log.",
      "required": ["strategy", "imported_state_token"],
      "properties": {
        "strategy": {
          "type": "string",
          "enum": ["imported-state-token", "shadow-log", "annotation-only"],
          "description": "imported-state-token: fork commits mapped to a token in parent log, not copied as commits"
        },
        "imported_state_token": {
          "type": "string",
          "description": "Opaque token representing the fork's state as imported into the parent audit log. Foreign branch/commit refs map to this token; parent branch namespace is not modified.",
          "pattern": "^import-[a-z0-9-]+-[0-9a-f]{8}$"
        }
      }
    },
    "f_g_r_on_imported_claims": {
      "type": "object",
      "description": "F-G-R trust tags for claims imported from the fork, per FPF B.3. Imported claims carry their own trust level, not inherited from parent.",
      "required": ["formality_level", "claim_scope", "reliability_level"],
      "properties": {
        "formality_level": {
          "type": "integer",
          "minimum": 0,
          "maximum": 9,
          "description": "FPF B.3 F-level (0=rumor, 9=formal proof). Imported claims default to F2 unless elevated by explicit verification."
        },
        "claim_scope": {
          "type": "string",
          "description": "Bounded context where imported claims hold. Required to declare where they do NOT hold."
        },
        "reliability_level": {
          "type": "string",
          "enum": ["R-low", "R-medium", "R-high", "R-certified"],
          "description": "FPF B.3 reliability. Imported claims default R-low until verified by parent ack."
        }
      }
    },
    "ip1_role_binding_overrides": {
      "type": "array",
      "description": "List of role binding differences between fork and parent. IP-1 (Role!=Executor): if the fork uses different executor names for the same roles, declare here. GENERIC field — specific executors are RUSLAN-LAYER.",
      "items": {
        "type": "object",
        "required": ["role_archetype", "fork_executor_id", "parent_executor_id"],
        "properties": {
          "role_archetype": { "type": "string", "description": "Generic role name (e.g. orchestration-coordinator, not brigadier)" },
          "fork_executor_id": { "type": "string", "description": "RUSLAN-LAYER: actual executor in fork" },
          "parent_executor_id": { "type": "string", "description": "RUSLAN-LAYER: actual executor in parent" }
        }
      }
    }
  },
  "additionalProperties": false
}
```

**Acceptance predicate (Hamel-binary):** "Schema validates against synthetic Phase B partner test fixture; fork export+import roundtrip preserves audit chain (imported_state_token present and non-null); foreign branch/commit refs mapped to imported-state-token without contaminating native audit log (parent git log contains zero refs to fork branch names)." [F2|G:Phase B stub, not validated|R-low — pending test fixture]

**[CRITIC]** The `ip1_role_binding_overrides` array correctly uses `role_archetype` (generic) rather than executor-specific names for the Foundation-layer field. The executor IDs (`fork_executor_id`, `parent_executor_id`) are explicitly labeled as RUSLAN-LAYER. This correctly applies IP-1 (Role≠Executor) [src:levenchuk-shsm-fpf.md:§4 P1]. However: the schema must declare a `$comment` at the top level noting "GENERIC — repo/branch names are RUSLAN-LAYER per OQ-MERGED-3." This prevents future authors from embedding Jetix-specific values in a Foundation-layer schema file.

### I.2 Commit-format regex spec (P1.2)

```
CANONICAL REGEX: ^\[(area)\] (verb) (subject)( \(why\))?$

Where:
  area   = one of the accepted area tokens (see token list below)
  verb   = imperative present tense (add, remove, update, fix, refactor, move, rename, ...)
  subject = description of what changed (≥3 chars, ≤72 chars excluding area prefix)
  (why)  = optional parenthetical clause explaining motivation

Accepted area tokens (enumerated):
  kb | daily | project | raw | crm | meta | skills | infra |
  prompts | architecture | ingest | decisions | swarm | 
  engineering | agents | wiki | cycles | design | strategy |
  tools | reports | comms | hooks | schemas | lint |
  voice | clients | templates | review | foundation

Examples of VALID commits:
  [kb] add wiki entry for event-sourcing pattern
  [swarm] update brigadier routing table for Part 6 dispatch (align with D25)
  [architecture] refactor Part 4 role manifest to extract executor binding
  [hooks] add pre-commit-format.sh stub (P1.2 Wave C)

Examples of INVALID commits (would be blocked by hook):
  kb: add wiki entry          <- missing brackets around area
  [KB] update wiki            <- uppercase area token not in allowlist
  update wiki entry           <- no area token prefix
  [kb] added wiki entry       <- past tense verb (violation of convention)
  [unknown-area] add thing    <- unknown area token
```

**[CRITIC]** The token list above is longer than the CLAUDE.md list (which names: kb, daily, project, raw, crm, meta, skills, infra). This is intentional: the repo has grown beyond the original 8 areas. The canonical architecture.md MUST declare an authoritative token list and note that new tokens require a HITL ack (addition to this list is a schema-level change, not a mechanics-level change). The DRY concern: the token list must live in ONE authoritative location — the recommendation is `shared/schemas/commit-format-tokens.json` (a new lightweight file), referenced by both the hook and the `/lint --check-commit-format` check. Two copies of the token list would be a DRY violation. [src:clean-code.md:§4 P3 DRY; src:unix-philosophy.md:§4 P4 SPOT]

### I.3 raw-task-return-packet frozen field stub

```yaml
# Addition to shared/schemas/task-return-packet schema (not yet created)
# This field is FROZEN — set post-commit, not pre-commit
git_commit_hash:
  type: string
  pattern: "^[0-9a-f]{40}$"
  description: >
    The SHA-1 hash of the git commit that persisted the canonical state
    produced by this task. Set by brigadier after the commit completes.
    NULL if the task produced no canonical write. FROZEN — not mutable after set.
  nullable: true
```

---

## §J Operational Rituals

**[INTEGRATOR]** Part 1 has four operational rituals, each with a cadence and trigger:

| Ritual | Cadence | Trigger | Responsible | Expected output |
|---|---|---|---|---|
| Commit with `[area] verb what (why)` | Every canonical write | Any Part producing a new file or mutation | All Parts via brigadier | Valid `git log` entry; hook exit 0 |
| `git fsck` integrity check | Weekly (Monday pre-Plan) | Calendar + brigadier cycle-start | Part 8 health monitor (triggers) | 0 object errors |
| `/company-status` snapshot | Session-start + post-ack | Owner session open + after HITL gate ack | Owner + Part 9 | ≤80-line markdown report |
| `/lint --check-commit-format` | Pre-commit (hook) + `/lint` run | git commit attempt + weekly `/lint` run | Pre-commit hook (automatic) + Part 8 | 0 format violations on last 50 commits |

**[INTEGRATOR]** The `git fsck` ritual is currently undeclared in any operational schedule. It is mentioned as a target SLI in the Wave A card [src:part-1-system-state-persistence.md:§E Effects] but has no declared trigger or responsible party. The canonical architecture.md must assign it to Part 8 (Health Monitoring) as a periodic trigger and to brigadier's weekly cycle-start as a manual reminder. [F4|G:Part 1 + Part 8 operational coordination|R-medium]

---

## §K Failure Modes

**[CRITIC]** Twelve failure modes identified, each with detection signal and halt-or-continue policy:

| # | Failure mode | Detection signal | Policy |
|---|---|---|---|
| K1 | Partial commit (file written, git commit failed) | `git status` shows uncommitted files post-attempt; `git log` does not reflect the write | Halt. Operator must decide: `git add + git commit` to complete, or `git checkout -- <file>` to revert. NEVER auto-retry silently. |
| K2 | Schema validation failure on pre-commit | Pre-commit hook exits non-zero; commit blocked | Halt. Human must fix schema violation or seek HITL ack to bypass with `--no-verify` (bypass itself must be a subsequent `git revert`-targetable commit). |
| K3 | Lint false-positive on valid commit message | `/lint --check-commit-format` flags a valid message | HARD GAP: the acceptance predicate for P1.2 requires 0 false positives on last 50 commits. If false-positive rate > 0, the hook must be blocked from production until fixed. Do not ship a false-positive-prone hook — it will erode trust and lead to `--no-verify` bypasses. |
| K4 | Offline guarantee bypass (`/company-status` makes a network call) | `tools/tests/test-offline-guarantee.sh` exit non-zero | Halt. Surface the specific syscall (e.g., `curl: https://api.notion.com`) and halt the skill. NEVER continue with potentially polluted output. |
| K5 | Fork import collision (same path written in fork and parent since divergence) | Cross-fork provenance schema validation failure on `divergence_point.commit_hash` mismatch | Halt. Phase B reconciliation architecture required. In Phase A, all cross-fork imports are `reconciliation_strategy: deferred-phase-b` — reject any import that is not marked deferred. |
| K6 | Hook bypass attempt (`git commit --no-verify`) | `git log` shows commit with message not matching format regex | Log. Cannot prevent retroactively. Mitigation: `/lint --check-commit-format --all` run by Part 8 health monitor detects historical bypasses; surfaces as lint signal. |
| K7 | Commit message area token expansion (new area added without schema update) | `/lint --check-commit-format` flags valid commits as using "unknown area" | Fix: update `shared/schemas/commit-format-tokens.json` as an authoritative token list; both hook and lint consume from this file. Area token expansion is a schema change requiring HITL ack. |
| K8 | `git fsck` object errors | `git fsck` exits non-zero with object error count > 0 | Halt all canonical writes. Escalate to HITL immediately. Repo integrity is prerequisite for all other Parts. |
| K9 | Stale `/company-status` (run during active write session) | Snapshot timestamp >1 hour old while git log shows commits since snapshot | Surface staleness note in output. Never block. Re-run to refresh. |
| K10 | Test infrastructure unavailable for offline guarantee test | `unshare -n` or `strace` not available on server OS | HARD GAP (see §L). Cannot verify offline guarantee without OS-level network isolation. Must be resolved before P1.3 acceptance predicate can be satisfied. |
| K11 | imported-state-token collision (two fork imports generate same token) | Duplicate `imported_state_token` values in audit trail | Hash the token from `fork_id + divergence_point.commit_hash + timestamp` — collision probability negligible. Declare in schema `$comment`. |
| K12 | DRY violation: token list duplicated | `commit-format-tokens.json` differs from hook's embedded list | Deploy-time check in CI: run `diff <(jq .tokens commit-format-tokens.json) <(grep TOKENS hook.sh)` — fail build on divergence. |

---

## §L Wave C Bullet Status

### P1.1 — Cross-fork provenance schema stub

**Design:** `shared/schemas/cross-fork-provenance.json` with all 9 required fields declared (see §I.1). Foundation-layer generic; RUSLAN-LAYER separation enforced via `$comment` and `ip1_role_binding_overrides` pattern.

**Acceptance predicate status:** ❌ NOT YET SATISFIED

"Schema validates against synthetic Phase B partner test fixture; fork export+import roundtrip preserves audit chain; foreign branches/commits mapped to imported-state-token without contaminating native audit log."

**Reason not satisfied:** The synthetic Phase B partner test fixture does not yet exist. The schema is designed and the acceptance predicate is declared; the test fixture is Wave C→D transition work. The canonical architecture.md must declare: "P1.1 schema is a Foundation stub at F2/R-low; promoted to F4/R-medium when Phase B test fixture passes."

**Decisions/policy entry needed:** A `decisions/policy/cross-fork-audit-deferred-phase-b.md` entry must declare explicitly: "Cross-fork audit trail reconciliation is Phase B architecture work. In Phase A, all cross-fork imports use `reconciliation_strategy: deferred-phase-b` and carry F2/R-low imported claims." This prevents Wave C from inheriting the ambiguity silently per wave-c-worklist.md Bullet 1 spec.

### P1.2 — D25 commit-format lint as Foundation artefact

**Design:** `swarm/wiki/skills/lint-check-commit-format.md` skill spec + `tools/git-hooks/pre-commit-format.sh` stub. Extends `/lint` as signal #12. Area token list in `shared/schemas/commit-format-tokens.json` (authoritative single-point-of-truth per DRY). Anti-scope: format only, not content.

**Acceptance predicate status:** ❌ NOT YET SATISFIED (design complete; implementation stub pending)

"Lint run on last 50 commits produces 0 false positives + flags any malformed commit."

**Reason not satisfied:** `pre-commit-format.sh` and `lint-check-commit-format.md` are designed but not yet written as implemented files. Wave C materialisation step must produce both. The design is complete (see §I.2 for regex spec and §H for CLI signatures).

### P1.3 — /company-status + /knowledge-diff offline-first guarantee

**Law declared:** See §E Laws item 3. "Every invocation of /company-status or /knowledge-diff makes ZERO network calls; halt on attempted curl/wget/http/api call."

**Test stub design:** `tools/tests/test-offline-guarantee.sh` using `unshare -n` (Linux network namespace isolation) to assert-fail on any network syscall. Failure mode: if test intercepts a network call → exit non-zero, surface specific call.

**Acceptance predicate status:** ❌ NOT YET SATISFIED — HARD GAP

**Reason not satisfied:** K10 (see §K) — `unshare -n` availability on the server OS is unverified. `unshare` requires Linux kernel ≥ 3.8 and either root privileges or `CAP_SYS_ADMIN`. On the current Ubuntu 22.04 / kernel 6.8.0-90 [env], `unshare -n` should be available but unprivileged network namespace creation may require `sysctl kernel.unprivileged_userns_clone=1`. This must be verified before the test stub can be declared functional.

**Alternative approach (if `unshare -n` unavailable):** `LD_PRELOAD`-based network call interception (preload a shared library that overrides `connect()`, `socket()` with exit-non-zero). This requires a compiled `.so` file, not just a shell script. A simpler fallback: `strace -e trace=network /company-status 2>&1 | grep -E 'connect|socket' && exit 1 || exit 0`. `strace` availability must also be verified.

**HARD GAP requiring Ruslan ack:** Ruslan must confirm which of {`unshare -n`, `LD_PRELOAD`, `strace`} is available on the server before the test stub can be finalised.

---

## §X Foundation vs RUSLAN-LAYER — Part 1 Boundary Table

Per OQ-MERGED-3 (Foundation generic, fork-portable vs RUSLAN-LAYER Jetix-specific):

| Artefact | Layer | Rationale |
|---|---|---|
| `shared/schemas/cross-fork-provenance.json` schema structure | **FOUNDATION** | Generic JSON Schema; no Jetix-specific values. Any fork-aware repo can adopt it. |
| `parent_repo_id`, `fork_id` field VALUES | **RUSLAN-LAYER** | Actual repo identifiers are Jetix-specific. Declared in `executor-binding.yaml` or equivalent config, not in the schema file. |
| Accepted area tokens list (commit format) | **FOUNDATION** (enumerated list) | The token vocabulary is part of the language of the commit protocol. Any fork adopting D25 discipline adopts the same vocabulary. Extensions for a specific fork are declared in a fork-local override. |
| Specific branch names (e.g. `claude/jolly-margulis-915d34`) | **RUSLAN-LAYER** | Branch names are Jetix git-session specifics. Never appear in Foundation schema or skill spec. |
| `^\[(area)\] (verb) (subject)( \(why\))?$` commit regex | **FOUNDATION** | The format rule is generic; any D25-disciplined repo uses it. |
| `/company-status` skill logic (reads git log, produces markdown) | **FOUNDATION** | The skill's logic is generic; the output content is Jetix-specific at runtime. |
| `tools/git-hooks/pre-commit-format.sh` hook script | **FOUNDATION** | The hook script is generic (validates against the regex + token list); no Jetix-specific values embedded. |
| `tools/tests/test-offline-guarantee.sh` | **FOUNDATION** | The test mechanism (network isolation + exit-code check) is generic. |
| `decisions/policy/cross-fork-audit-deferred-phase-b.md` CONTENT | **RUSLAN-LAYER** | The decision to defer cross-fork reconciliation to Phase B is Jetix's specific architectural choice, even though the deferral pattern is generic. |

**[INTEGRATOR]** The Foundation/RUSLAN-LAYER distinction is the clearest in Part 1 because git discipline is already a well-established general pattern. The RUSLAN-LAYER additions are thin: specific repo IDs, specific branch names, specific timeline decisions. The Foundation layer is thick: the schema structure, the commit format regex, the hook script, the test mechanism. This is the correct ratio for a Foundation part — generic is structural, specific is configurable.

---

## §Y Scalability Projections (§6.1 horizon gates applied to Part 1)

**[SCALABILITY]**

| Gate | First-fire signal | Part 1 specific observable | Refactor-at-10× estimate | Risk |
|---|---|---|---|---|
| **€50K (current)** | Composition + Scale: hook layer activates (log-only → blocking per OPP-02 cycle-2-impl) | Pre-commit-format.sh moves from stub to active; `/lint --check-commit-format` added as signal #12; cross-fork schema stub committed | 0% refactor — additive only; no existing interface changes | LOW |
| **€200K** | Agency: 1 contractor added to git workflow | Commit format hook must handle two authors without false positives; area token list may need extensions for contractor-specific work areas | 5-10% refactor — token list extension; hook author-awareness optional | LOW |
| **€1M** | Operation + Composition: multi-developer review queue; 10K+ commits/year | `/knowledge-diff` query latency grows with history depth (10K commits over `git log --since` is still fast; no snapshot strategy needed yet per Greg Young rolling snapshot threshold) | 10-15% refactor — snapshot strategy for `/knowledge-diff` if history exceeds 50K commits; otherwise git remains sufficient [src:event-sourcing-cqrs.md:§5 Tradeoff A] | MEDIUM |
| **$100M** | Composition + External: multi-team monorepo or polyrepo; SRE owns deploy | Cross-fork provenance schema becomes load-bearing (multiple partner forks active); Phase B reconciliation architecture required; `deferred-phase-b` strategy invalid at this gate | 25-30% refactor — reconciliation algorithm implementation; possible migration from git-as-sole-event-log to git + lightweight event bus for high-frequency ops [src:event-sourcing-cqrs.md:§5 Tradeoff A scale flag] | HIGH — this is the fragile-at-10× threshold |
| **$1T** | External + Time: platform-level git infra; compliance requirements | Git history may require retention policy; `git fsck` alone insufficient for enterprise repo integrity | 30%+ refactor at $1T — but this is the "context reframe" horizon per §6.1 of engineering-expert.md; infrastructure choice may change entirely | HIGH at this horizon — Part 1 as currently designed is fragile at $1T scale |

**[SCALABILITY]** The antifragility check for Part 1:

- **Build system 10×:** git commit throughput scales to hundreds of commits/hour on a single repo without architectural changes. NOT fragile at 10× current rate (571/month → 5710/month). [F4|G:Part 1 commit throughput|R-medium]
- **Architecture pattern 10×:** git-as-event-log pattern holds at 10× volume. The cross-fork schema is the only component that becomes fragile at scale (Phase B). [F4|G:Phase A + Phase B transition|R-medium]
- **Test suite 10×:** Not applicable (Part 1 test = `tools/tests/test-offline-guarantee.sh`, a single test). Single test scales trivially.
- **Dependency graph 10×:** The commit-format token list may need extension as new work areas emerge. A `shared/schemas/commit-format-tokens.json` single-source-of-truth (§I.2 recommendation) prevents the DRY violation from compounding at 10× area token count.

**[SCALABILITY]** The $100M gate is the critical fragility point for Part 1. The cross-fork provenance schema (P1.1) is the architectural investment that buys headroom between €50K and $100M. If Phase B reconciliation architecture is not designed before the $100M gate fires, Part 1 becomes a bottleneck for multi-partner deployment.

---

## §Z Critic-Mode Summary (all passes)

**[CRITIC]** Findings from the concurrent critic pass, each with AP code:

| Finding | AP code | Severity | Location | Recommended change |
|---|---|---|---|---|
| `raw-task-return-packet frozen field` undeclared in Part 1 output | AP-ENG-10 (external-dep without failure-mode declaration) | Medium | §B Outputs | Add `git_commit_hash` frozen field to task-return-packet schema (see §I.3) |
| Schema validation mentions no path names | AP-ENG-10 | Low | Wave A card §A Inputs | Enumerate `shared/schemas/*.json` paths in canonical architecture.md §A |
| Lint false-positive budget undeclared | AP-ENG-5 (tool-eval without eval-dataset) analog | High | P1.2 design | Declare false-positive rate = 0 as acceptance predicate; block hook production until achieved |
| DRY risk: area token list in hook + lint separately | AP-ENG-11 (DRY violation) | Medium | §I.2 | Single `shared/schemas/commit-format-tokens.json`; hook + lint both consume it |
| `AspectOf` edge for Part 8 dependency needs philosophy-expert validation | Dependency typing hygiene | Low | §D | Flag for philosophy-expert critic pass before promoting to canonical |
| Offline test infrastructure unverified (`unshare -n` availability) | K10 hard gap | Critical | §L P1.3, §K | HITL ack required from Ruslan on test infrastructure availability |
| `decisions/policy/cross-fork-audit-deferred-phase-b.md` not yet written | AP-ENG-9 (premature abstraction without deferred tag) | Medium | §L P1.1 | Write the policy entry as part of P1.1 materialisation |

**[CRITIC]** Part 1 was noted as "CLEAN" in the Wave A critic gate [src:part-1-system-state-persistence.md:§H critic flags]. The Wave C critic pass surfaces new items arising from the three new bullets, not from defects in the Wave A card itself. The Wave A card is sound. The three new bullets introduce new design surface that must be critic-verified before promotion.

---

*End of engineering-expert multi-mode cell. Word count: ~5200 words. Sections §A-§X + §Y (scalability) + §Z (critic summary). Proposed write: this file.*
