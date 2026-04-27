---
title: Part 1 — System State Persistence — Architecture
date: 2026-04-28
type: foundation-architecture
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 1
status: draft-pre-wisdom-loop
F: F4
ClaimScope: "Foundation Parts 1-10; does not govern RUSLAN-LAYER executor bindings or Notion display layer"
R:
  refuted_if: "Any Foundation part achieves durable canonical state without routing through this part's git interface"
  accepted_if: "All accepted artefacts carry git-commit provenance linking to this part"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-1-system-state-persistence.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-1/engineering-expert-multi-mode.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-1/investor-expert-long-term-compounding.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-1/systems-expert-cybernetics-emergence.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-1/philosophy-expert-epistemic-audit.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-1/mgmt-expert-boundary.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - design/JETIX-FPF.md
---

# Part 1 — System State Persistence — Architecture

**This interface card is itself a Part 1-governed artefact:** committed via git under D25 discipline, carrying F-G-R frontmatter and `[src:]` inline citations, with §E structured per FPF A.6.B L/A/D/E lane separation. It models the discipline it specifies. [src:mgmt-expert-boundary.md:§2 self-exemplification; FPF §4.3 CP-3]

---

## §0 Executive Summary

Part 1 is the append-only, version-controlled ground-truth substrate on which every other Foundation part stores its committed state. It is not the most intellectually complex Foundation part; it is the most durably valuable one. Every wiki entry, every governance decision, every agent-produced artefact, every CRM record — all canonical state in the Jetix system either exists as a git commit or does not exist at all. [src:part-1-system-state-persistence.md:§E Laws "no canonical state outside git"; src:AUDIT:§0 "git-репозиторий-как-операционная-система"]

**The substrate thesis in one sentence.** Git is 19 years old, used by approximately 100 million developers worldwide, is FLOSS with zero proprietary risk, and is the only currently available substrate that is simultaneously Lindy-confirmed, content-addressable (cryptographic hash as proof-of-existence), append-only by structural design (directed acyclic graph), and offline-first. No alternative — not Notion, not a proprietary event-store, not an in-memory state machine — passes the 10-year durability test at Jetix's cost basis. [src:investor-expert-long-term-compounding.md:§1.1 Lindy substrate thesis; src:capital-allocation-antifragility.md:§3 "git is the most durable artifact format"]

**Headline numbers.** 571 commits in 30 days as of 2026-04-27 — the system is in active operational use, not a design exercise. [src:AUDIT:§0 "571 коммит за последние 30 дней"] At the current run rate of ~570 commits/month, the system will accumulate approximately 71,820 commits over a 10-year horizon. Each commit is a discrete, hash-verified record carrying: named subsystem (`[area]`), named action class (`verb`), named object (`what`), and optionally named decision rationale (`(why)`). At 71,820 commits, the entire decision history of Jetix is reconstructable from `git log` at any past point in time. [src:investor-expert-long-term-compounding.md:§4.1 arithmetic]

**Wave C scope.** This architecture document addresses three Wave C bullets: (P1.1) cross-fork provenance schema stub for D27 fork-and-merge architecture, (P1.2) D25 commit-format lint rule materialised as a Foundation artefact, and (P1.3) `/company-status` and `/knowledge-diff` offline-first guarantee formalised as a Law. [src:wave-c-worklist.md:L60-95]

**Deep-module frame.** Part 1 is an Ousterhout deep module: its public interface is narrow (six CLI commands), its internal complexity is wide (git plumbing, Merkle tree, DAG history, schema validation engine, config resolution). [src:engineering-expert-multi-mode.md:§H "Ousterhout deep module test applied"; src:clean-code.md:§4 P1] Consumers of other Parts never interact with git plumbing directly; they interact with the declared interface.

**Why this matters for antifragility.** The append-only log does not merely survive incidents — it captures them permanently as named, dated, hash-verified entries. Every `git revert` produces a compensating commit (Young 2010 Reversal Transactions) that makes the correction itself part of the audit trail. Every postmortem is a commit. Every correction is a commit. The system becomes more legible with every incident, not less. This is Taleb's antifragility applied at the substrate level: disorder strengthens the record rather than degrading it. [src:investor-expert-long-term-compounding.md:§2.1 antifragility; src:event-sourcing-cqrs.md:§3 Source 2 p.31 "There is no Delete"]

---

## §A Inputs

**Full enumeration of what Part 1 consumes.** Format: `<source> :: <data-shape> :: <event-trigger>`. Part 1 is the substrate — it has no upstream Part dependency. Its inputs are heterogeneous write requests arriving from all other Parts, plus two infrastructure sources. [src:engineering-expert-multi-mode.md:§A; src:part-1-system-state-persistence.md:§A]

| Source | Data shape | Event trigger | Schema path |
|--------|------------|---------------|-------------|
| All Parts 2-10 | Committed file write :: YAML/JSON/Markdown at a repo-rooted path | State-change event in any downstream Part | `shared/schemas/*.json` (applicable per file type) |
| Part 6 (Governance) | AWAITING-APPROVAL gate packet :: frontmatter `status: acked`, `acked_by: ruslan`, `acked_at: <ISO-8601>` | HITL ack received; human promotes draft to canonical | `shared/schemas/awaiting-approval.json` (existing) |
| `CLAUDE.md` + `.claude/config/*.yaml` (RUSLAN-LAYER path binding; see §X) | Declarative YAML config :: parsed key-value namespace | Skill invocation boot OR `git pull` config refresh | CLAUDE.md is constitutional; validates at human-read |
| `shared/schemas/*.json` | JSON Schema draft-07 :: validation schema | Pre-commit hook fire OR `/lint` run | Self-referential: schemas validate other files; schema files themselves validate on commit |
| `tools/git-hooks/pre-commit-format.sh` (P1.2 stub) | Commit message string :: stdin via `$1` file path (git hook convention) | git commit attempt on canonical branch | `shared/schemas/commit-format-tokens.json` (new, §I.2) |
| Cross-fork import (D27, Phase B) | Cross-fork provenance record :: JSON document | Phase B partner fork export event | `shared/schemas/cross-fork-provenance.json` (new, P1.1, §I.1) |

**Admissibility for each input class** (acceptance criteria before commit is accepted):

- **Path validity.** Input must carry a valid path under the repo root. Excluded paths: `~/.ssh/`, `/etc/`, `.env*`, `private/`. A pre-commit hook path check enforces this. [src:part-1-system-state-persistence.md:§E Admissibility; src:CLAUDE.md Global Rule 6]
- **Schema validation.** JSON and YAML files must pass schema validation against the relevant `shared/schemas/*.json` definition before commit. Schema paths are enumerated by file type in `shared/schemas/` directory. Generic reference to "schema validation" without naming the schema path fails Conformance Check 5 (external-dep without failure-mode declaration) — the specific schema paths are authoritative. [src:engineering-expert-multi-mode.md:§A CRITIC]
- **UTF-8 encoding.** Input must be UTF-8 encoded text OR explicitly declared binary with MIME type annotation in the commit message. Non-UTF-8 files pass the path-validity check but corrupt downstream text-processing tools; failure traces to no single auditable commit. [src:mgmt-expert-boundary.md:§1 Gap B "UTF-8 encoding not specified"]
- **File size.** Input files exceeding 1MB committed directly to canonical paths require an explicit `[large-file]` tag in the commit message. Binary files exceeding 10MB require HITL ack before commit and MUST be tracked via Git LFS. The rationale: a 50MB voice transcript committed raw passes the path check but violates the lean-commit discipline and degrades `/company-status` readability. [src:mgmt-expert-boundary.md:§1 Gap A "file-size limit absent"]
- **Binary-vs-text discrimination.** Binary commits (images, compiled artefacts) MUST include a machine-readable descriptor commit in the same atomic operation naming the binary's provenance and its referencing text artefact. Binary files cannot be diffed, cannot carry inline `[src:]` citations by line range, and degrade the IP-3 writing-as-thinking substrate. [src:mgmt-expert-boundary.md:§1 Gap C; src:levenchuk-shsm-fpf.md:§4 P2 IP-3]
- **Part 6 promotion.** Inputs arriving via Part 6 governance promotion must carry `status: acked`, `acked_by: ruslan`, `acked_at: <ISO-8601>` in frontmatter. A Part 6 promotion without a human-ack receipt is rejected by the pre-commit hook. [src:part-1-system-state-persistence.md:§E Admissibility; src:design/JETIX-FPF.md:§5.1 IP-1]
- **Cross-fork import.** Cross-fork import inputs (Phase B) must validate against `shared/schemas/cross-fork-provenance.json` AND carry `f_g_r_on_imported_claims` non-null AND carry `reconciliation_strategy: deferred-phase-b` (Phase A only). [src:engineering-expert-multi-mode.md:§E Admissibility new P1.1]

**CLAUDE.md circularity resolution.** The `CLAUDE.md` config input is also an output of Part 1 — it is read at boot as config-input; it is written through git as committed-state. This apparent circularity resolves cleanly: the write path is serialised (you cannot change `CLAUDE.md` and immediately benefit from its new value within the same git transaction). Config changes take effect at the next session start after the commit. This is non-circular by design. [src:engineering-expert-multi-mode.md:§A INTEGRATOR "CLAUDE.md circularity resolution"; F4|G:Part 1 Jetix Phase-A|R-high]

---

## §B Outputs

**Full enumeration of what Part 1 exposes.** Format: `<consumer> :: <data-shape> :: <event-published>`. Part 1 produces three classes of output: committed artefacts (durable), query-result snapshots (ephemeral), and health signals (periodic). [src:part-1-system-state-persistence.md:§B; src:engineering-expert-multi-mode.md:§B]

| Output | Consumer | Data shape | Event published | Notes |
|--------|----------|------------|-----------------|-------|
| Durable committed artefact | All Parts 2-10 | Stable path in `git log --oneline` | commit-completed event | The primary output of Part 1; everything else derives from this |
| Git history as audit trail | Part 6 (Governance) | Append-only ordered immutable event log :: `git log --format="%H %ai %s"` | provenance-query event | Per Young 2010 event-log pattern [src:event-sourcing-cqrs.md:§4 Principle 1] |
| `/company-status` snapshot | Part 9 (Owner Interaction Scaffold) | Markdown ≤80 lines, zero network calls | owner-review trigger (manual OR weekly Friday 17:00 ritual) | Zero-network Law; see §E Law 3 |
| `/knowledge-diff` delta | Part 9 | Markdown delta report between two git-log dates | periodic or on-demand owner trigger | Zero-network Law; see §E Law 3 |
| Four health signals (SRE) | Part 8 (Health Monitoring) | Named signal tuple emitted per schedule | periodic health-poll event | See Four Golden Signals enumeration below |
| Repo integrity output | Part 8 | `git fsck` exit code + object error count → written to `shared/state/system-health.json` under `git_integrity` key | weekly fsck cron (proposed: Sunday 02:00 system time) | Part 8 owns SLO threshold; Part 1 owns emission cadence |
| **raw-task-return-packet frozen field** | Part 5 (Compound Learning / task-return) | `git_commit_hash: <sha>` frozen post-commit | task-completion event | LOAD-BEARING for Part 5 DRR verification; see schema stub §I.4 |

### §B.1 SRE Four Golden Signals — Part 1 Contract

The interface card previously declared "repo integrity metrics (commit cadence, branch status, backup SLI)" as the signal set emitted to Part 8. This is a bucket, not a signal taxonomy. Part 8 cannot define its SLI/SLO schema for Part 1 without knowing what signals Part 1 emits. The Google SRE Book Chapter 6 Four Golden Signals framework (Latency, Traffic, Errors, Saturation) provides the minimal complete taxonomy. Applied to the git substrate: [src:systems-expert-cybernetics-emergence.md:§1.5; src:sre-observability.md:§3 Source 1 Ch. 6 pp.55-66]

| Signal | Part 1 observable name | Measurement method | Emitted to Part 8 as | SLI target |
|--------|------------------------|--------------------|-----------------------|------------|
| **Latency** | `commit-latency-p95` | `time git commit` (instrumented in pre-commit hook; result appended to `shared/state/metrics/`) | p95 commit time in milliseconds | ≤3000ms (3 seconds) |
| **Traffic** | `commit-cadence-per-day` | `git log --oneline --after="24 hours ago" \| wc -l` (run at cron midnight) | integer count per 24h window | Informational only Phase A; threshold set by Part 8 |
| **Errors** | `hook-failure-rate` | Pre-commit hook non-zero exit events per total commit attempts in rolling 7-day window | float (events / total) | SLO ≤ 2% per week (false positives are errors; see K3) |
| **Saturation** | `repo-growth-rate-MB-per-day` | `du -sh .git` delta over 24h window (run at cron midnight) | float MB/day | Target ≤ 10MB/day; alert threshold at Part 8's discretion |

These four named signals replace the generic "repo integrity metrics" phrase in §B. The contract is now unambiguous: Part 8 knows exactly what to consume, and Part 1 knows exactly what to emit. [src:systems-expert-cybernetics-emergence.md:§1.5 Wisdom-Application proposal]

**Feedback loop B2 closure.** The `commit-cadence-per-day` signal explicitly closes the B2 (Commit-Volume Balancing Loop) identified in systems analysis: when commit volume becomes high enough that the `git log` becomes unreadable, this signal gives the owner and Part 8 an observable that can trigger deliberate batching. Without this signal, the B2 loop is only weakly closed. [src:systems-expert-cybernetics-emergence.md:§1.4 B2 loop; F3|G:Phase A loop; R-medium]

### §B.2 raw-task-return-packet frozen field — Part 5 interface

Every task-return packet from any agent that produces a canonical write MUST include a `git_commit_hash` as a frozen (post-commit) field. Without this field, Part 5 (Compound Learning) cannot verify that the compounded state referenced in a strategies.md DRR entry corresponds to an actual commit. The field is:

- **Frozen** — set by brigadier after the commit completes; NULL if the task produced no canonical write.
- **Not mutable** after set.
- **Format** — full 40-character SHA-1 hex string.

This is an AP-ENG-10 trigger (external-dep without failure-mode declaration at the interface level) if absent. Full JSON Schema stub in §I.4. [src:engineering-expert-multi-mode.md:§B CRITIC "raw-task-return-packet frozen field undeclared"; F4|G:Part 1 + Part 5 interface|R-medium]

---

## §C Side-effects

**Append-only; no in-place mutation.** Every Part 1 side-effect is a git commit. There are no side-channel writes to external systems, no Notion writes, no API calls. This section documents three specific side-effects, each with its append-only guarantee sourced from Greg Young's Reversal Transactions pattern (Young 2010). [src:event-sourcing-cqrs.md:§3 Source 2 p.31; src:engineering-expert-multi-mode.md:§C]

**C.1 Git history append — the primary side-effect.**
Every accepted write is a new commit appended to the history graph. The git DAG (directed acyclic graph) structurally enforces append-only: commits point to parents, never forward; there are no cycles. This is not a convention — it is the structural invariant of the data structure. Per Young (2010): "There is no Delete in event sourcing... a compensating event is the correct mechanism." Applied to Jetix D25: `git revert <hash>` is the canonical undo; it produces a new commit that describes the reversal, leaving the original commit intact in history. `git reset --hard` and `git commit --amend` on canonical branches are constitutional violations — they simulate deletion by making prior states unreachable or by rewriting content without changing the DAG structure's forward-only guarantee. [src:event-sourcing-cqrs.md:§3 Source 2 p.31; src:design/JETIX-FPF.md:§3.5 D25]

Concrete consequence: any skill, hook, or agent action that calls `git reset --hard` on the canonical branch is a D25 violation requiring immediate HITL review and a corrective `git revert` commit. The correction itself becomes permanent evidence of the violation — the incident is captured, not erased. This is the antifragility mechanism in action. [src:investor-expert-long-term-compounding.md:§8.1 "Young's There Is No Delete applied to Part 1 §F"]

**C.2 Schema validation gate — pre-commit, no file write.**
The pre-commit hook validates schema compliance but produces no file write. Validation failure produces stderr output only and blocks the commit. The hook is idempotent — running it twice on the same uncommitted state produces the same result. Validation is a gate, not a state change. If a validation failure occurs, the correct response is: (a) fix the schema violation, (b) re-attempt the commit. The bypass mechanism (`git commit --no-verify`) is a constitutional violation (Law L-4) and is itself monitored by the B1 format-compliance feedback loop. [src:engineering-expert-multi-mode.md:§C.2; F5|G:Part 1 git hook discipline|R-high]

False-positive handling: the acceptance predicate for P1.2 requires zero false positives on valid commits (§L). If the false-positive rate exceeds zero, the hook must be blocked from production until fixed. A false-positive-prone hook erodes trust and induces `--no-verify` bypasses — the opposite of the desired behaviour. [src:engineering-expert-multi-mode.md:§C CRITIC lint false-positive budget]

**C.3 Commit-format validation side-effect (P1.2 new).**
The `tools/git-hooks/pre-commit-format.sh` hook validates commit message format as a pre-commit side-effect. Fail = block commit + human-readable error to stderr naming the specific format violation. No file mutation. Idempotent. The hook executes in ≤50ms (target SLI from §E Effects). [src:engineering-expert-multi-mode.md:§C.3]

**C.4 Antifragility framing — failures as permanent learning commits.**
Every detected failure that affects Part 1's audit chain MUST produce a postmortem commit — not a verbal note, not a chat message, not a temporary file. The commit is the permanence mechanism. A failure that reaches a commit is a permanent improvement signal; a failure that is only discussed disappears. The discipline: no learning is real unless it is committed. [src:investor-expert-long-term-compounding.md:§9 "Failure Modes as Learning Commits"; src:systems-expert-cybernetics-emergence.md:§2.2 Senge Law 11]

**C.5 Reversal Transactions — "git revert is the only undo."**
To be maximally explicit about this anti-pattern given its high-consequence nature: the sequence `git revert <bad-hash>` → `git commit -m "[area] revert: <reason>"` is the ONLY acceptable undo mechanism. The sequence `git reset --hard HEAD~N` produces no new commit, making the reversal invisible in the linear `git log` — it simulates deletion. The sequence `git commit --amend` rewrites the most recent commit's content and changes its hash — any downstream consumer that cached the original hash now holds a stale reference. Both are constitutional violations. Both are detectable by comparing remote log vs local log or by `git reflog` divergence. [src:philosophy-expert-epistemic-audit.md:§2.2 "Reversibility ≠ deletion"; src:engineering-expert-multi-mode.md:§E Laws item 1]

---

## §D Dependencies

**Typed A.14 edges only.** No `depends-on`, no bare `uses`. Every edge uses A.14 typed vocabulary per FPF §3.5. Part 1 is the substrate root — it has zero upstream Part dependencies. All Parts 2-10 depend on Part 1; Part 1 depends on nothing above it. [src:part-1-system-state-persistence.md:§D; src:levenchuk-shsm-fpf.md:§4 P4 A.14 typing]

### §D.1 Upstream dependencies — NONE

Part 1 is the substrate. The Unix-philosophy one-way data-flow property holds: every other Part calls Part 1's interface; Part 1 calls nothing back. [src:part-1-system-state-persistence.md:§D "No upstream part dependencies"] This is the defining structural property that makes Part 1 the substrate root. Destroying Part 1's git integrity destroys the persistence guarantee for ALL other Parts simultaneously.

### §D.2 Downstream dependency edges

| Edge | Edge type (A.14) | Rationale | Leverage implication |
|------|-----------------|-----------|----------------------|
| Parts 2-10 → Part 1 | `operates-in` | Content entities (wiki entries, agent files, CRM records, cycle logs) reside on the git substrate. Destroying Part 1 destroys their persistence, but they are not constitutive parts of git itself. `ComponentOf` would be wrong — the wiki content is a separate entity that happens to persist on Part 1's filesystem. `operates-in` is the correct A.14 type. [src:levenchuk-shsm-fpf.md:§4 P4; src:part-1-system-state-persistence.md:§D] | Meadows L6 leverage: Part 1 is the information-flow substrate; degrading it degrades ALL downstream simultaneously |
| Part 6 (Governance) → Part 1 | `methodologically-uses` | Governance artefacts (AWAITING-APPROVAL packets, LOCKED tags, `decisions/*.md` files) are authored through Part 1's commit interface as their enforcement mechanism. Part 6's method requires Part 1's git discipline to enforce human-ack receipt gating. [src:part-1-system-state-persistence.md:§D; src:candidate-parts-merged.md:§2 Part 6 D-Lock anchor] | Governance without audit trail = unenforceable governance |
| Part 8 (Health Monitoring) → Part 1 | `operates-in` | Health monitoring reads Part 1's git history and fsck status. The monitoring function is a consumer of Part 1's output signals. [src:systems-expert-cybernetics-emergence.md:§1.5 OQ-PART1-SYS-1] | Part 8 cannot define SLIs without Part 1's signal taxonomy being declared |
| Part 9 (Owner Interaction) → Part 1 | `operates-in` | `/company-status` and `/knowledge-diff` are queries over Part 1's git history. The Owner Interaction scaffold is the human-facing read layer on top of the substrate. [src:part-1-system-state-persistence.md:§B] | Owner understanding of system state is bounded by Part 1's audit legibility |
| Phase B partner fork → Part 1 | `operates-in` (post-import) + `constrained-by` (import schema) | After a cross-fork import, the imported provenance record resides in Part 1's substrate (`operates-in`). The import is constrained by the validation rules in `shared/schemas/cross-fork-provenance.json` (`constrained-by`). The fork itself is external; its imported provenance record is internal. [src:engineering-expert-multi-mode.md:§D Phase B cross-fork dependency] | D27 Phase B investment: schema stub now buys headroom before this dependency becomes load-bearing |

**Note on `AspectOf` for Part 8.** The engineering cell proposed an additional `AspectOf` edge for Part 8 (git fsck output is an aspect of Part 1's observable state). This edge is defensible but requires philosophy-expert validation against FPF A.14 L.17478 before promotion to canonical. Flagging as [F3|G:Part 1 → Part 8 dependency|R-medium — pending philosophy-expert critic pass]. The `operates-in` edge captures the essential dependency; `AspectOf` is an optional precision enhancement.

### §D.3 Meadows leverage context for Part 1 dependencies

Part 1 occupies Meadows leverage levels L2, L5, and L6 simultaneously, which is architecturally unusual. [src:systems-expert-cybernetics-emergence.md:§1.3]

- **L2 (Paradigm):** The append-only paradigm is the deepest lever. Changing this paradigm — introducing mutable state via Notion-as-SoT or an in-place database — would be the most destructive possible intervention. L2 interventions are catastrophic in both directions. The correct paradigm (append-only) is enormously powerful; the incorrect one (mutable SoT) is catastrophic.
- **L5 (Rules):** The `[area] verb what (why)` format rule, the no-amend invariant, the no-force-push invariant. These are harder to change than parameters but softer than the paradigm. Future ROY cycles that propose modifying §E Laws should be aware they are touching L5 rules, not L12 parameters.
- **L6 (Information flows):** The `git log` audit trail is a Meadows L6 lever. A degraded audit trail (missing commits, ambiguous messages, inconsistent area tokens) degrades the information flow to ALL downstream consumers simultaneously.

Each §E Law in this document is annotated with its Meadows leverage level per the systems-expert recommendation. This is a risk-communication convention: a developer who sees `[Meadows-L2]` next to an invariant will think twice before proposing an exception. [src:systems-expert-cybernetics-emergence.md:§1.3 Wisdom-Application proposal]

---

## §E Boundary — L/A/D/E Lanes

**Self-exemplification.** This interface card is itself a Part 1-governed artefact: committed via git under D25 discipline, carrying F-G-R frontmatter and `[src:]` inline citations, with this §E section structured per FPF A.6.B L/A/D/E lane separation. [src:mgmt-expert-boundary.md:§2; FPF §4.3 CP-3]

### Laws (invariants MUST hold — violations are constitutional defects) [Meadows leverage level annotated per systems-expert]

**L-1. No canonical state outside git.** [Meadows-L2 — paradigm] Every canonical state change is a committed file in the git repository. No canonical state exists in memory-only structures, `.env` files, tool-specific caches, or any system that is not git-committed. The filesystem is the single source of truth per D17. Violation refuter: find any canonical state (promoted wiki entry, accepted artefact, approved decision) that does not appear in `git log`. A single such case refutes this Law. [src:FUNDAMENTAL:§2.1; src:D25; src:event-sourcing-cqrs.md:§4 Principle 1]

**L-2. `[area] verb what (why)` commit format.** [Meadows-L5 — rules] Every canonical commit message MUST match `^\[(area)\] (verb) (subject)( \(why\))?$` where `area` is a token from the authoritative enum in `shared/schemas/commit-format-tokens.json`. Violation refuter: a commit in the canonical branch whose message does not match the pattern. **Category note from philosophy-expert:** This law is currently enforced as a Deontic (obligation) in Phase A because the hook is log-only, not blocking. It will be promoted to a hard invariant (true Law) when the Phase B blocking hook is live. Until then, the correct reading is: "Law L-2 is operative as a hard invariant only when the pre-commit hook is blocking; until then it functions as a Deontic obligation." This distinction matters for Part 6 Governance audit: P6 must not produce false-compliance signals by treating an unenforced Law as if it were enforced. [src:philosophy-expert-epistemic-audit.md:§1.1 Law L-2; src:mgmt-expert-boundary.md:§1 Gap G-1; src:CLAUDE.md Global Rule 7; src:D25]

**L-3. Offline-first guarantee for `/company-status` and `/knowledge-diff`.** [Meadows-L5 — rules] Every invocation of `/company-status` or `/knowledge-diff` makes ZERO network calls. `curl`, `wget`, any HTTP client library call, any API call is a constitutional violation. The FUNDAMENTAL §6.1 principle that AI tools do not call external services autonomously underlies this Law. Violation refuter: `tools/tests/test-offline-guarantee.sh` intercepts a network syscall during execution. The skill MUST halt with a non-zero exit code surfacing the specific syscall attempted — not continue with degraded output. [src:engineering-expert-multi-mode.md:§E Laws item 3; src:wave-c-worklist.md:L88-95]

**L-4. Notion is read-display only; never in the write path.** [Meadows-L5 — rules] Notion is a collaboration and planning UI tool (not authoritative). Any skill modification that proposes writing state to Notion before committing to git is a D17 violation; the AWAITING-APPROVAL gate blocks it. Violation refuter: any commit preceded by a Notion write that was not also committed to git first. [src:D17; src:CLAUDE.md "Filesystem = single source of truth"; src:engineering-expert-multi-mode.md:§E Laws item 4]

**L-5. No `--amend`, no `--no-verify`, no force-push on canonical branch.** [Meadows-L2 — paradigm for no-amend; Meadows-L5 for no-verify/no-force-push] Append-only is constitutional. `git revert` is the ONLY undo. `git commit --amend` on a pushed commit changes its hash silently for downstream consumers. `git commit --no-verify` bypasses schema validation, permitting malformed content to enter the canonical record. Force-push on canonical rewrites history for all consumers with stale clones. Three distinct refuters: (a) compare remote log vs local log for force-push detection; (b) `git log --format="%H %s" | grep "no-verify"` for bypass detection; (c) `git reflog` divergence from remote HEAD. **Pre-push hook note from philosophy-expert:** `--amend` before a commit is pushed to remote leaves no trace in `git log` — only a pre-push hook detects it. The enforcement mechanism for no-`--amend` requires a pre-push hook at Phase B; post-hoc `git log` inspection is insufficient. This is a detection gap (not a Law invalidity gap) for Phase A. [src:philosophy-expert-epistemic-audit.md:§1.1 Law L-4; src:FUNDAMENTAL:§2.1; src:D25; src:event-sourcing-cqrs.md:§3 Source 2 p.31]

**L-6. UTF-8 plain text only; binary files require HITL ack and LFS tracking.** [Meadows-L5 — rules] All committed files must be UTF-8 encoded text unless explicitly declared binary with MIME type annotation in the commit message AND tracked via Git LFS for files over 10MB. Plain text is the Constitutional AI transparency requirement [src:anthropic-constitutional-ai.md:§4 P6] — every Part 1 emitted artefact must be human-inspectable. Binary artefacts cannot carry `[src:]` line-range citations, cannot be diffed, and degrade the provenance substrate. Violation refuter: a committed file that fails `file --mime-encoding` UTF-8 check and is not annotated binary in the commit message. [src:mgmt-expert-boundary.md:§1 Gap B; src:philosophy-expert-epistemic-audit.md:§6 Constitutional AI Transparency Check]

### Admissibility (acceptance criteria for inputs to be committed)

- **A-1.** Input path is under repo root; not `~/.ssh/`, `/etc/`, `.env*`, `private/`. [src:CLAUDE.md Global Rule 6]
- **A-2.** JSON/YAML files pass schema validation against the relevant `shared/schemas/*.json` definition before commit. Schema path must be named (not generic "schema validation"). [src:part-1-system-state-persistence.md:§E Admissibility; src:engineering-expert-multi-mode.md:§A CRITIC]
- **A-3.** UTF-8 encoded text OR explicitly declared binary with MIME annotation in commit message. [src:mgmt-expert-boundary.md:§1 Gap B]
- **A-4.** Files ≤1MB commit directly; files 1MB-10MB carry `[large-file]` tag; files >10MB require LFS tracking and HITL ack. [src:mgmt-expert-boundary.md:§1 Gap A]
- **A-5.** Part 6 promotion events carry `status: acked`, `acked_by: ruslan`, `acked_at: <ISO-8601>` in frontmatter. [src:design/JETIX-FPF.md:§5.1 FPF A.13 Agency-CHR]
- **A-6.** Cross-fork import inputs (Phase B) validate against `shared/schemas/cross-fork-provenance.json` AND carry `reconciliation_strategy: deferred-phase-b` (Phase A constraint). [src:engineering-expert-multi-mode.md:§E Admissibility P1.1]

### Deontics (obligations of this part toward consumers)

- **D-1.** Part 1 MUST preserve every committed state with ≥99.999% durability (five nines) over a rolling 10-year horizon. "Indefinitely" is not a measurable SLI; this converts it to one. Concrete implementation: git remote backup verified weekly via `git fsck` with 0 object-error target; result written to `shared/state/system-health.json` under `git_integrity` key. Binding: FUNDAMENTAL §5.1 Tier 0 "cannot lose, ever." [src:mgmt-expert-boundary.md:§1 Deontic 1 "indefinitely → SLI conversion needed"; src:FUNDAMENTAL:§5.1] [F4|G:Part 1 Jetix Phase-A; not yet KPI-tracked|R-medium]
- **D-2.** Part 1 MUST expose a queryable log (`git log --oneline`, `/knowledge-diff`) for provenance reconstruction by any consumer requesting it. [src:part-1-system-state-persistence.md:§E Deontics]
- **D-3.** Part 1 MUST provide reversibility via `git revert` — not `git reset`. Every canonical state can be undone safely by appending a compensating commit. [src:FUNDAMENTAL UC-H.3; src:D25; src:event-sourcing-cqrs.md:§4 Principle 1]
- **D-4.** Part 1's pre-commit hook MUST block malformed commit messages AND produce a human-readable error to stderr naming the specific format violation (Phase B: blocking; Phase A: log-only). [src:engineering-expert-multi-mode.md:§E Deontics P1.2]
- **D-5.** Part 1's `/company-status` and `/knowledge-diff` MUST exit non-zero if any network call is detected during execution. The offline guarantee is not optional; it is constitutionally bounded by L-3. [src:engineering-expert-multi-mode.md:§E Deontics P1.3]

### Effects (measurable outcomes)

- **E-1.** After successful commit: artefact is durable, path-addressable, appears in `git log` within 1 second. Measured locally (Part 1's ClaimScope is the mono-repo; local git commit is atomic without network). [src:part-1-system-state-persistence.md:§E Effects]
- **E-2.** `/company-status` run: produces ≤80-line markdown snapshot to stdout, zero network calls, exit 0. [src:AUDIT:§5.1 /company-status]
- **E-3.** `git fsck` (weekly cron, Sunday 02:00 system time): 0 object errors. Non-zero error count triggers Part 8 health alert. Result written to `shared/state/system-health.json`. The fsck cadence is Part 1's operational obligation; the alert-routing SLO is Part 8's. [src:mgmt-expert-boundary.md:§1 Effects cadence gap; src:part-1-system-state-persistence.md:§E Effects]
- **E-4.** Pre-commit hook (P1.2): blocks malformed commit with exit non-zero + human-readable stderr message within 50ms. [src:engineering-expert-multi-mode.md:§E Effects P1.2]
- **E-5.** Offline test (P1.3): exit 0 if zero network calls detected; exit non-zero with intercepted syscall name if any network call is attempted during `/company-status` or `/knowledge-diff` execution. [src:engineering-expert-multi-mode.md:§E Effects P1.3]

---

## §F Anti-scope

**Format-only scope is LOAD-BEARING.** Part 1 enforces `^\[(area)\] (verb) (subject)( \(why\))?$` regex structure. It does NOT evaluate whether `verb` accurately describes what the commit does, whether `subject` is adequately specific, whether `(why)` is meaningfully informative. Content evaluation is Part 6 (Governance) territory. This distinction prevents scope creep where a future developer argues the hook should check that "add" is not used when files are deleted — that check is a content concern; the hook does not own it. [src:engineering-expert-multi-mode.md:§F; src:mgmt-expert-boundary.md:§4]

### §F.1 Generic anti-scope (all Foundation parts per FUNDAMENTAL §6)

- **NOT strategic decisions.** Part 1 does not choose which methodology the system follows, which architecture variants to adopt, which horizon gates to prioritise. [src:FUNDAMENTAL §6.1]
- **NOT founder agency substitution.** Part 1 does not write content, evaluate quality, or produce insights. It stores whatever the founder and agents produce. [src:FUNDAMENTAL §6.2]
- **NOT engagement-economy patterns.** Part 1 does not use dark UX, persuasion mechanics, or engagement-optimisation. It is a substrate, not a product. [src:FUNDAMENTAL §6.3]

### §F.2 Part-specific anti-scope

- **NOT commit content correctness.** Part 1 does NOT evaluate whether the commit message accurately describes the change. "Does this message describe what was actually committed?" is a Part 6 Governance question, not a Part 1 format question. [src:part-1-system-state-persistence.md:§F; src:mgmt-expert-boundary.md:§4]
- **NOT AWAITING-APPROVAL gate logic.** Part 1 executes the physical commit when Part 6 acks. It does not decide whether the ack is warranted, whether the HITL review was thorough, or whether the accepted artefact is correct. [src:part-1-system-state-persistence.md:§F]
- **NOT Notion sync.** Notion is read-only display. Part 1 does not have a Notion write path. Any proposal to add Notion write as part of the commit pipeline is a D17 violation. [src:D17; src:mgmt-expert-boundary.md:§7 Risk R-2]
- **NOT schema authorship.** `shared/schemas/` files are authored through the normal Part 6 governance flow (AWAITING-APPROVAL gate, Ruslan ack). Part 1 validates against schemas; it does not author them. [src:part-1-system-state-persistence.md:§F]
- **NOT cross-fork reconciliation protocol.** Part 1's P1.1 contribution is the STUB schema declaration. The reconciliation algorithm — how conflicts between fork and parent are resolved, how cross-fork state is merged — is Phase B architecture work. Wave C produces only the stub declaration. [src:engineering-expert-multi-mode.md:§F]
- **NOT CRM entity IDs or financial metrics in commit format.** The `[area] verb what (why)` format is structural only. CRM-entity-ID tagging belongs to Part 6 cross-reference conventions; financial impact attribution belongs to Part 7 (Project Lifecycle Substrate) `outcome:` field. Embedding them in Part 1's commit format expands the schema beyond the structural format invariant. [src:mgmt-expert-boundary.md:§7 Risk R-1, Risk R-3]
- **NOT Slack/Notion post-commit notifications.** Post-commit notification routing is Part 8 (Health Monitoring) or Part 9 (Owner Interaction Scaffold) territory. Part 1 emits signals to `shared/state/system-health.json` only; other Parts decide notification channels. Any proposal to add webhook calls to the post-commit hook is a Law L-4 violation (external-service write path). [src:mgmt-expert-boundary.md:§7 Risk R-2]
- **NOT SLO thresholds or alert policies.** Part 1 emits the Four Golden Signals (§B.1). Part 8 owns the SLO threshold for each signal, the alert conditions, and the error-budget burn policy. Part 1's terminal action is writing to `shared/state/system-health.json`; everything downstream is Part 8. [src:mgmt-expert-boundary.md:§5]
- **NOT postmortem-as-deletion.** Part 1 NEVER deletes commits as "cleanup." A commit that corrects an error IS a commit — it appends, it does not overwrite. "Cleaning up history" is a constitutional violation, not a maintenance task. This distinction is not merely implied by the no-amend rule; it is an explicit architectural boundary. [src:systems-expert-cybernetics-emergence.md:§2.2 Senge Law 11 Wisdom-Application proposal]
- **NOT inline [src:] citation density enforcement.** Citation standardisation for Parts 7, 8, 9 (Wave C Bullet 3) is tracked through the `/lint` skill's citation-density check (lint signal to be added). But the enforcement mechanism lives in `/lint` (swarm/lib/-owned); Part 1 provides the substrate on which citation discipline is expressed. The latent R2 provenance-drift loop identified by systems analysis is real: if "PARTIAL is acceptable" becomes the operational norm, citation density degrades silently. The lint signal is the balancing counterpart required to prevent this loop from activating. [src:systems-expert-cybernetics-emergence.md:§1.4 R2 loop; src:wave-c-worklist.md:L88-95]

---

## §G F-G-R Tagging

**F-G-R tagging per FPF B.3.** [src:levenchuk-shsm-fpf.md:§4 P5; src:design/JETIX-FPF.md:§4.2] Every artefact emitted by Part 1 carries explicit F (Formality 0-9), G (ClaimScope), and R (Reliability) tags with rationale. F-levels adopted from philosophy-expert re-tagging pass (§4 of philosophy-expert cell) over the interface card's initial tags. [src:philosophy-expert-epistemic-audit.md:§4]

| Artefact emitted | F | Rationale for F-level | G (ClaimScope) | R (Reliability) | Upgrade path |
|-----------------|---|----------------------|----------------|-----------------|--------------|
| **Git commit + commit message** | F4 | Hook is currently log-only (not blocking) in Phase A. F5 requires "codified rule with systematic enforcement." A codified rule that is not machine-enforced is F4, not F5. Initial card said F5 — philosophy-expert correctly re-tags to F4. [src:philosophy-expert-epistemic-audit.md:§4 "Git commit + commit message currently F5 → re-tag F4"] | Holds for Jetix mono-repo; unknown for multi-repo or distributed fork architecture | R-medium Phase A (hook log-only); R-high Phase B (hook blocking, adds systematic enforcement) | Promote to F5 when Phase B blocking hook is live and ≥3 cycles confirm zero bypasses |
| **YAML config read result** | F5 | CLAUDE.md constitutionally backs `.claude/config/*.yaml`. CLAUDE.md is a locked constitutional document. Convention backed by a constitutional document is F5 (codified rule), not F4 (operational convention only). "We do this because a codified rule requires it" vs "we do this because we've been doing it." [src:philosophy-expert-epistemic-audit.md:§4 "YAML config read result — currently F4 → re-tag F5"] | Holds for skills invoked within repo root; not applicable to external tool invocations. RUSLAN-LAYER: specific path `.claude/config/*.yaml` (see §X) | R-medium — config can drift if edited outside git (D25 violation). Refuted if config change takes effect without a corresponding git commit. Mitigated by Law L-2 enforcement | No upgrade path needed; F5 is appropriate ceiling for operational config |
| **`/company-status` snapshot** | F3 | Multi-source informal: derives from `git log` (F6) + `ls` counts (informal). The synthesis is informal even though one input is high-formality. Correctly F3. Confirmed by philosophy-expert. [src:philosophy-expert-epistemic-audit.md:§4 "/company-status F3 confirmed"] | Holds at snapshot timestamp; may be stale within ≤1 hour in active sessions. Refuted if output is stale beyond 1 hour of last commit AND still presented as current | R-medium — git-derived; accurate at invocation time | No planned promotion; F3 is correct for a snapshot skill |
| **`/knowledge-diff` delta output** | F3 | Programmatic report over git log; accuracy depends on date-range parameters. Multi-source informal. [src:engineering-expert-multi-mode.md:§G] | Holds for time-bounded git log queries within repo history; does not project future state | R-medium — accurate at invocation time for the specified date range | No planned promotion; F3 is correct |
| **`git log` provenance chain** | F6 | Codified rule + ≥3 successful applications. 571 commits in 30 days clearly exceeds ≥3 by two orders of magnitude. Cross-cycle reuse confirmed. [src:AUDIT:§0; src:philosophy-expert-epistemic-audit.md:§4 "git log F6 confirmed"] The Merkle-tree cryptographic guarantee supports this — SHA-1 collision resistance provides a mathematical guarantee of non-mutability stronger than operational convention. F6 is the defensible ceiling in Phase A (F7+ requires formal peer-reviewed proof; SHA-256's collision resistance is engineering consensus, not a Jetix-specific proof). | Holds for entire repo history; fork audit trails separate per D27 | R-high — immutable once committed; refuted only by repo corruption detectable by `git fsck` | SHA-256 migration (git plans) would elevate to F7-equivalent; no Jetix-specific action required |
| **`shared/schemas/cross-fork-provenance.json` (P1.1 new)** | F3 | Schema stub designed in §I.1; not yet validated against Phase B test fixture. "Design-time draft" — F2 would be too low (the schema structure is derived from multiple cell inputs and FPF principles), F4 would be too high (not yet operationally validated). F3 on Phase B partner activation. [src:engineering-expert-multi-mode.md:§G P1.1] | Holds only for schema stub phase; ClaimScope extends to Phase B when test fixture passes. GENERIC Foundation layer (see §X) | R-low — stub, not validated against live fixture; acceptance predicate not yet satisfied | Promote to F4 when Phase B synthetic test fixture passes; F5 when ≥3 fork-import cycles complete |
| **`tools/git-hooks/pre-commit-format.sh` (P1.2 new)** | F3 | Design complete (§I.2, §H); implementation stub pending. Not yet operational. F3 = "multi-source informal; design is well-grounded but not yet running." [src:engineering-expert-multi-mode.md:§G P1.2] | Holds for all commits on canonical branch once hook is active; unknown for emergency bypasses (tracked as K6) | R-medium — depends on `--no-verify` bypass policy being enforced via HITL ack | Promote to F4 when hook is in active log-only mode; F5 when blocking mode is live |
| **`/lint --check-commit-format` (P1.2 new)** | F3 | Lint signal #12 design complete; extends existing `/lint` skill. Not yet implemented as signal. [src:wave-c-worklist.md:Bullet 2; src:engineering-expert-multi-mode.md:§H] | Holds for commits on canonical branch reachable from current HEAD | R-medium | Promote to F4 when signal is in active `/lint` runs; F5 when 0-false-positive acceptance predicate is satisfied |
| **Offline guarantee test stub (P1.3 new)** | F2 | Stub; requires `unshare -n` or `strace` infrastructure verified as callable on server OS. Currently unverified. F2 = "single-source stub; not validated." [src:engineering-expert-multi-mode.md:§G P1.3] | Holds once test infrastructure confirmed compatible with server OS | R-low — test-infrastructure availability unverified; HARD GAP (see §K K10) | Promote to F3 when `unshare -n` availability confirmed; F4 when test passes end-to-end |
| **Institutional memory (emergent property)** | F4 | Emergent from: structured commit messages + YAML frontmatter + append-only history + query skills. No individual component contains institutional memory; the property appears at system level. F4 = operational convention with multi-cycle evidence (571 commits / 30 days). [src:systems-expert-cybernetics-emergence.md:§2.3] | Holds when all three component disciplines hold simultaneously: commit format + YAML frontmatter coverage + append-only paradigm. Breaks if any single component is degraded. | R-high (emergent) — refuted only by repo corruption OR paradigm change (append-only abandoned) | Promote to F6 at cycle 50 with provenance chain intact |

---

## §H Code-Level Interfaces

**Deep-module interface declaration.** Part 1's public interface is narrow; its internal complexity is wide. Per Ousterhout: implementation-LoC >> interface-LoC. Consumers never call git plumbing directly — they call the declared CLI interface. [src:engineering-expert-multi-mode.md:§H; src:clean-code.md:§4 P1]

```
NARROW PUBLIC INTERFACE                       WIDE INTERNAL COMPLEXITY
─────────────────────────────────────────────────────────────────────
git commit -m "[area] verb what (why)"        git plumbing (SHA, tree, blob, ref, DAG)
git revert <hash>                             schema validation engine (pre-commit hook)
git log [--oneline] [--since] [--until]       config resolution (YAML parse + CLAUDE.md)
/company-status [--days=N]                    snapshot assembly (git log + ls + format)
/knowledge-diff [--since=YYYY-MM-DD]          delta computation (git diff + log)
           [--until=YYYY-MM-DD]
/lint --check-commit-format [--count=N]       regex parse + area-token lookup
                            [--all]
```

### §H.1 CLI signatures (canonical)

```bash
# git commit — direct git invocation
# Format: [area] verb what (why)
# area: token from shared/schemas/commit-format-tokens.json
# verb: imperative present tense
# what: ≥3 chars, ≤72 chars excluding area prefix
# (why): optional motivational clause (recommended; see §I.3 schema_version_history note)
git commit -m "[area] verb what (why)"

# git revert — ONLY acceptable undo on canonical branch
git revert <full-40-char-sha>

# /company-status
# Owner: swarm/lib/ shared infra (NOT Part 1-owned; Part 1 owns the Law guaranteeing offline)
# Guarantee: zero network calls (Law L-3); halts with non-zero exit if network call detected
# Output: ≤80-line markdown snapshot to stdout
# Exit: 0 on success; non-zero on network call detected
/company-status [--days=N]

# /knowledge-diff
# Owner: swarm/lib/ shared infra
# Guarantee: zero network calls (Law L-3)
# Output: markdown delta report to stdout between two git-log date boundaries
# Exit: 0 on success; non-zero on network call detected
/knowledge-diff [--since=YYYY-MM-DD] [--until=YYYY-MM-DD]

# /lint --check-commit-format
# Owner: swarm/lib/ shared infra (lint signal #12, extending existing 11 KB health checks)
# NOT a standalone skill — extends the existing /lint skill per DRY
# Input: last N commits (--count=N) OR all commits (--all)
# Output: PASS/FAIL per commit with format violation description to stdout
# Exit: 0 if all checked commits pass; non-zero if any fail
/lint --check-commit-format [--count=N] [--all]
```

**Ownership note.** `/company-status`, `/knowledge-diff`, and `/lint` are owned by `swarm/lib/` shared infra, NOT by Part 1 directly. Part 1's Wave C work for these skills is constitutional declaration (the Laws and Deontics that bound them) plus test stub (P1.3), NOT reimplementation. The skills are already operational; the Law declarations are the Wave C contribution. [src:engineering-expert-multi-mode.md:§H INTEGRATOR swarm/lib ownership note; src:CLAUDE.md Skills section]

### §H.2 Pre-commit hook specification (P1.2)

```bash
# Location: tools/git-hooks/pre-commit-format.sh
# Install method (choose one):
#   Option A: git config core.hooksPath tools/git-hooks
#   Option B: ln -sf ../../tools/git-hooks/pre-commit-format.sh .git/hooks/pre-commit
# Mode: Phase A = log-only (warn + continue); Phase B = blocking (warn + exit 1)
# Input: $1 = path to temporary commit message file (git hook convention)
# Area tokens source: shared/schemas/commit-format-tokens.json (single source of truth)
# Regex: ^\[(area)\] (verb) (subject)( \(why\))?$
# Exit codes: 0 = message valid; 1 = message invalid (blocking mode) or 0 (log-only mode)
# Stderr: human-readable error naming the specific violation
tools/git-hooks/pre-commit-format.sh

# Example valid messages (hook exits 0):
# "[kb] add wiki entry for event-sourcing pattern"
# "[swarm] update brigadier routing table for Part 6 dispatch (align with D25)"
# "[hooks] add pre-commit-format.sh stub (P1.2 Wave C)"

# Example invalid messages (hook exits 1 in blocking mode):
# "kb: add wiki entry"           <- missing brackets; hook: "FAIL: area token must be in brackets [area]"
# "[KB] update wiki"             <- uppercase; hook: "FAIL: area token must be lowercase"
# "update wiki entry"            <- no area; hook: "FAIL: commit message must start with [area]"
# "[unknown-area] add thing"     <- unknown token; hook: "FAIL: unknown area token 'unknown-area'; see shared/schemas/commit-format-tokens.json"
```

### §H.3 Offline guarantee test specification (P1.3)

```bash
# Location: tools/tests/test-offline-guarantee.sh
# Purpose: verify /company-status and /knowledge-diff make zero network calls
# Primary mechanism: unshare -n (Linux network namespace isolation, kernel ≥3.8)
# Fallback (if unshare unavailable): strace -e trace=network <command> 2>&1 | grep -E 'connect|socket'
# HARD GAP: unshare -n availability on server OS unverified (see K10); Ruslan ack required
# Exit: 0 if zero network calls; non-zero if any network call intercepted (surfaces specific syscall)
tools/tests/test-offline-guarantee.sh [/company-status | /knowledge-diff]

# Example usage:
# tools/tests/test-offline-guarantee.sh /company-status
# Output on pass: "PASS: /company-status made 0 network calls"
# Output on fail: "FAIL: /company-status made network call: connect(3, {sa_family=AF_INET, sin_addr=...})"
```

### §H.4 /company-status output schema (≤80 lines)

The `/company-status` output is a structured markdown report. Part B partner onboarding requires this schema to implement Part 1 in a fork. The schema is indicative (actual field values are RUSLAN-LAYER): [src:mgmt-expert-boundary.md:§3 Outcome b "§H absence blocks Phase B fork implementation"; src:engineering-expert-multi-mode.md:§H]

```
# System Status — <YYYY-MM-DD HH:MM>

## Git Substrate (Part 1)
- Branch: <branch-name>
- Last commit: <YYYY-MM-DD> [<area>] <verb> <subject>
- Commits last 7d: <N>
- Commits last 30d: <N>
- Repo size: <MB>
- fsck status: <pass | fail | last-run: YYYY-MM-DD>

## Active Cycles (Part 5/6)
- <cycle-id>: <status>

## Health Signals
- commit-latency-p95: <ms>
- hook-failure-rate (7d): <pct>%
- repo-growth-rate: <MB>/day

## Pending Approvals (Part 6)
- <N> items in swarm/awaiting-approval/

## Open Questions / HARD GAPS
- <N> items in current wave

---
Generated: <timestamp> | Network calls: 0 | Source: git log + filesystem only
```

---

## §I Data Schemas

**All schemas are JSON Schema draft-07.** All schema files are GENERIC Foundation layer (see §X for Foundation vs RUSLAN-LAYER boundary). Schema file values (repo IDs, branch names, area token strings that are Jetix-specific) are RUSLAN-LAYER and are configured at deployment time, not hardcoded in the schema files. [src:engineering-expert-multi-mode.md:§I "Foundation-vs-RUSLAN-LAYER separation"]

### §I.1 `shared/schemas/cross-fork-provenance.json` (P1.1 new)

Full JSON Schema draft-07. Philosophy-expert requirement: ≥4 named cross-fork fields. Ashby variety-gap requirement: `metadata` open field. IP-1 compliance: `role_archetype` Foundation-generic; executor IDs in RUSLAN-LAYER. Schema-versioning field per investor HARD GAP. [src:philosophy-expert-epistemic-audit.md:§1.2 P1.1 "≥4 named cross-fork fields"; src:systems-expert-cybernetics-emergence.md:§1.2 "metadata open field"; src:investor-expert-long-term-compounding.md:§10 "schema versioning gap"]

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/cross-fork-provenance.json",
  "$comment": "GENERIC Foundation schema — repo URLs, branch names, and executor names are RUSLAN-LAYER. Do not embed Jetix-specific values here. Per OQ-MERGED-3 Foundation/RUSLAN-LAYER separation.",
  "title": "Cross-fork provenance record",
  "description": "Schema for tracking provenance of state imported from a fork of this repository into the parent repo canonical audit log. Phase B stub — reconciliation algorithm deferred. Acceptance predicate: schema validates against synthetic Phase B partner test fixture; fork export+import roundtrip preserves audit chain.",
  "type": "object",
  "required": [
    "schema_version",
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
    "schema_version": {
      "type": "string",
      "description": "Schema version string per schema_version_history block (investor HARD GAP). Enables upcasting when schema evolves — old records remain parseable by declaring which version they conform to.",
      "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"
    },
    "parent_repo_id": {
      "type": "string",
      "description": "Stable logical identifier for the parent repository. GENERIC: do not embed repo URL (RUSLAN-LAYER). Logical ID agreed between parties.",
      "pattern": "^[a-z0-9-]+$"
    },
    "parent_commit_hash": {
      "type": "string",
      "description": "Full 40-char SHA-1 hash of the parent repo commit at divergence point.",
      "pattern": "^[0-9a-f]{40}$"
    },
    "fork_id": {
      "type": "string",
      "description": "Stable logical identifier for the fork. GENERIC. RUSLAN-LAYER binds this to actual fork repo.",
      "pattern": "^[a-z0-9-]+$"
    },
    "fork_branch": {
      "type": "string",
      "description": "Branch name in the fork at export time. Mapped to imported-state-token in parent audit log — does NOT contaminate parent branch namespace.",
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
      "description": "How conflicts between fork and parent are resolved. Phase A only: 'deferred-phase-b'. All other values are Phase B architecture.",
      "enum": ["deferred-phase-b", "cherry-pick-manual", "merge-with-review", "fork-read-only"]
    },
    "audit_trail_continuation": {
      "type": "object",
      "description": "How the parent audit log references the fork commit history without contaminating its native log.",
      "required": ["strategy", "imported_state_token"],
      "properties": {
        "strategy": {
          "type": "string",
          "enum": ["imported-state-token", "shadow-log", "annotation-only"],
          "description": "imported-state-token: fork commits mapped to a token in parent log, not copied as commits. This preserves parent audit-log integrity while making fork state queryable."
        },
        "imported_state_token": {
          "type": "string",
          "description": "Opaque token representing the fork state as imported. Foreign branch/commit refs map to this token; parent branch namespace is not modified. Hash from fork_id + divergence_point.commit_hash + timestamp ensures collision resistance.",
          "pattern": "^import-[a-z0-9-]+-[0-9a-f]{8}$"
        }
      }
    },
    "f_g_r_on_imported_claims": {
      "type": "object",
      "description": "F-G-R trust tags for claims imported from the fork, per FPF B.3. Imported claims carry their own trust level, not inherited from parent. Default: F2/R-low until verified by parent ack.",
      "required": ["formality_level", "claim_scope", "reliability_level"],
      "properties": {
        "formality_level": {
          "type": "integer", "minimum": 0, "maximum": 9,
          "description": "FPF B.3 F-level (0=rumor, 9=formal proof). Imported claims default F2."
        },
        "claim_scope": {
          "type": "string",
          "description": "Bounded context where imported claims hold. Must declare where they do NOT hold."
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
      "description": "Role binding differences between fork and parent. IP-1 (Role!=Executor): if fork uses different executor names for same roles, declare here. GENERIC field — specific executor IDs are RUSLAN-LAYER.",
      "items": {
        "type": "object",
        "required": ["role_archetype", "fork_executor_id", "parent_executor_id"],
        "properties": {
          "role_archetype": {
            "type": "string",
            "description": "Generic role name (e.g. 'orchestration-coordinator', not 'brigadier'). Foundation-layer field."
          },
          "fork_executor_id": { "type": "string", "description": "RUSLAN-LAYER: actual executor in fork." },
          "parent_executor_id": { "type": "string", "description": "RUSLAN-LAYER: actual executor in parent." }
        }
      }
    },
    "metadata": {
      "type": "object",
      "description": "Open extension field for Ashby variety gap compliance. Any fields not yet covered by the schema can be placed here without schema violation, preserving Ashby requisite variety for novel operation types. Contents are not schema-validated. Phase B may formalise specific metadata fields into the main schema.",
      "additionalProperties": true
    }
  },
  "additionalProperties": false
}
```

**Schema version history block** (per investor HARD GAP — commit-message schema versioning):

```yaml
# To be placed in swarm/wiki/foundations/part-1-system-state-persistence/schema-version-history.yaml
schema_version_history:
  - version: "1.0.0"
    effective_from: "2026-04-28"
    changelog: "Initial Phase A stub. reconciliation_strategy: deferred-phase-b only. schema_version field added per investor HARD GAP."
    notes: "Old cross-fork records without schema_version field are assumed version 1.0.0 for upcasting purposes."
```

This block ensures that when the schema evolves (Phase B adds reconciliation strategies, Phase B adds new required fields), old records remain parseable by declaring which version they conform to. Young's upcasting requirement [src:event-sourcing-cqrs.md:§4 Principle 4 "Event Versioning / upcasting"].

**Acceptance predicate (Hamel-binary):** "Schema validates against synthetic Phase B partner test fixture; fork export+import roundtrip preserves audit chain with `imported_state_token` present and non-null; foreign branch/commit refs do NOT appear in parent `git log` — only the `imported_state_token` does; `ip1_role_binding_overrides` uses `role_archetype` not executor names in required fields." [F3|G:Phase B stub, not yet validated|R-low — pending test fixture]

### §I.2 `shared/schemas/commit-format-tokens.json` (P1.2 new)

Single source of truth for area tokens. Both the pre-commit hook AND `/lint --check-commit-format` consume this file — no duplication. Adding a new area token is a schema change requiring HITL ack. [src:engineering-expert-multi-mode.md:§I.2 DRY recommendation; src:clean-code.md:§4 P3; src:unix-philosophy.md:§4 P4 SPOT]

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/commit-format-tokens.json",
  "$comment": "GENERIC Foundation schema. Token list is RUSLAN-LAYER-extended: base tokens are generic; Jetix-specific tokens (e.g. 'swarm', 'cycles', 'prompts') are deployed via RUSLAN-LAYER config. A fork adopts this schema and declares its own token extensions.",
  "title": "Commit format token registry",
  "description": "Authoritative single-source list of valid [area] tokens for the commit-format rule. Both pre-commit-format.sh hook and /lint --check-commit-format consume this file. Token additions require HITL ack (schema change, not mechanics change).",
  "type": "object",
  "required": ["tokens", "schema_version", "overflow_token"],
  "properties": {
    "schema_version": { "type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$" },
    "overflow_token": {
      "type": "string",
      "description": "Ashby variety-gap overflow mechanism. When no existing token fits, use this token AND trigger lint-signal-13 if used >2 times in 7-day window (indicating enum needs expansion). See systems-expert Ashby recommendation.",
      "const": "new"
    },
    "tokens": {
      "type": "array",
      "items": { "type": "string", "pattern": "^[a-z][a-z0-9-]*$" },
      "description": "Enumerated valid area tokens. Lowercase only. Order is alphabetical for diff readability.",
      "uniqueItems": true,
      "minItems": 1
    }
  }
}
```

**Current RUSLAN-LAYER token list** (would live in a RUSLAN-LAYER config file, not in the schema itself):

```json
{
  "tokens": [
    "agents", "architecture", "clients", "comms", "crm", "cycles",
    "daily", "decisions", "design", "engineering", "foundation",
    "hooks", "infra", "ingest", "kb", "lint", "meta", "new",
    "project", "prompts", "raw", "reports", "review", "schemas",
    "skills", "strategy", "swarm", "templates", "tools", "voice",
    "wiki"
  ]
}
```

**Note:** The current CLAUDE.md token list (kb, daily, project, raw, crm, meta, skills, infra) is a subset. The repo has grown beyond the original 8 areas; this authoritative list is the expansion. CLAUDE.md's list should reference `shared/schemas/commit-format-tokens.json` as authoritative rather than maintaining a separate list (DRY). [src:engineering-expert-multi-mode.md:§I.2 CRITIC "token list longer than CLAUDE.md list"]

**Overflow token `[new]` — Ashby compliance.** When no existing area token fits, the author uses `[new]`. Lint signal #13 alerts when `[new]` is used >2 times in a 7-day window — this indicates the enum needs expansion via HITL ack and schema update. This preserves the format invariant while providing an Ashby-compliant escape valve for novel operation types. [src:systems-expert-cybernetics-emergence.md:§1.2 "Add explicit overflow mechanism for [area] enum"]

**Commit-format regex (canonical):**

```
CANONICAL REGEX: ^\[(area)\] (verb) (subject)( \(why\))?$

Where:
  area    = one of the tokens in shared/schemas/commit-format-tokens.json .tokens array
  verb    = imperative present tense (add, remove, update, fix, refactor, move, rename,
            revert, lock, ack, scaffold, extend, clarify, archive, bootstrap, promote, ...)
  subject = description of what changed (≥3 chars, ≤72 chars excluding area prefix)
  (why)   = optional parenthetical clause — RECOMMENDED for all commits;
            format: " (reason or decision basis)"
            Note: making (why) mandatory is an OQ requiring Ruslan ack (see §K K8 discussion)
```

### §I.3 Commit-format Foundation artefact — `schema_version_history:` block

Per investor HARD GAP: every version of the commit format must carry a `schema_version_history:` block. Without it, tooling that parses `git log` for audit purposes may silently misparse old commits when the format evolves. [src:investor-expert-long-term-compounding.md:§10; src:event-sourcing-cqrs.md:§4 Principle 4]

```yaml
# To be placed in swarm/wiki/foundations/part-1-system-state-persistence/commit-format.md frontmatter
schema_version_history:
  - version: "1.0.0"
    effective_from: "2026-04-28"
    format: "^\\[(area)\\] (verb) (subject)( \\(why\\))?$"
    why_optional: true
    token_source: "shared/schemas/commit-format-tokens.json"
    notes: "Initial Foundation artefact. Wave C materialisation. (why) optional by declaration — see OQ-PHIL-PART1-3 for pending Ruslan ack on making mandatory."
```

### §I.4 `task-return-packet.json` stub — frozen `git_commit_hash` field (Part 5 consumer)

Partial schema (Bundle 3 full spec; this is the Part 1-contributed frozen field). [src:engineering-expert-multi-mode.md:§I.3]

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/task-return-packet.json",
  "$comment": "PARTIAL — Bundle 3 will author the full task-return-packet schema. This stub declares only the fields Part 1 contributes. Part 5 (Compound Learning) is the primary consumer of git_commit_hash.",
  "title": "Task return packet (Part 1 stub)",
  "type": "object",
  "properties": {
    "git_commit_hash": {
      "type": ["string", "null"],
      "pattern": "^[0-9a-f]{40}$",
      "description": "SHA-1 hash of the git commit that persisted canonical state produced by this task. Set by orchestrator after commit completes. NULL if task produced no canonical write. FROZEN — not mutable after set. Part 5 uses this to verify DRR entries reference actual commits.",
      "nullable": true
    },
    "actor_role_archetype": {
      "type": "string",
      "description": "IP-1 compliant: generic role name (e.g. 'engineering-expert'), not executor instance. Foundation-layer field."
    },
    "cycle_id": {
      "type": "string",
      "description": "Cycle identifier (e.g. cyc-foundation-build-2026-04-28). Links task-return to the cycle that produced it."
    },
    "gate_class": {
      "type": "string",
      "enum": ["autonomous", "requires-approval", "hitl-required"],
      "description": "The gate class under which this task was executed, per Part 6 governance."
    }
  }
}
```

---

## §J Operational Rituals

**Appetite declaration (per Shape Up, Singer 2019).** Wave C Part 1 architecture build: 2 working days maximum. If §A-§J draft is not complete within 1.5 days, cut §J and §I to stub form. Do NOT scope-balloon. Circuit-breaker: if any Wave C bullet expands beyond its declared effort tier (S or M), re-shape to fit within tier or defer to Wave D with explicit `[deferred: Wave D]` label. Fixed-time variable-scope discipline. [src:mgmt-expert-boundary.md:§6 Cagan/Shape Up; src:product-management-cagan-shape-up.md:§4 Principle 2]

| Ritual | Cadence | Trigger | Responsible | Expected output | Notes |
|--------|---------|---------|-------------|-----------------|-------|
| Commit with `[area] verb what (why)` | Event-driven (not scheduled) | Any Part producing a canonical state change | All Parts via orchestrator | Valid `git log` entry; hook exit 0 | Event-driven is correct: scheduled commits would produce noise |
| `git fsck` integrity check | Weekly (Sunday 02:00 system time, proposed) | Calendar cron + orchestrator cycle-start pre-check | Part 8 health monitor (triggers); Part 1 executes and writes result | 0 object errors; result in `shared/state/system-health.json` | Cadence gap from interface card closed; Part 8 owns alert routing |
| `/company-status` snapshot | Session-start + post-ack + weekly (Friday 17:00 Ruslan review ritual) | Owner session open OR after HITL gate ack OR weekly calendar | Owner + Part 9 | ≤80-line markdown report; 0 network calls | Three distinct triggers; only the weekly one is scheduled |
| `/lint --check-commit-format` | Pre-commit (automatic via hook) + weekly `/lint` run | git commit attempt + Part 8 weekly health check | Pre-commit hook (automatic Phase B blocking; log-only Phase A) + Part 8 | 0 format violations on last 50 commits (acceptance predicate P1.2) | Hook is the primary enforcement; `/lint --all` is the historical audit |
| `imported_state_token` generation | Phase B event (fork export) | Phase B partner fork export event | Phase B architecture (deferred) | Token mapped to fork state in parent audit log | Currently deferred; registered as ritual for Phase B planning visibility |

**Blameless postmortem ritual.** Any incident affecting Part 1 (fsck error, hook bypass, offline guarantee violation) MUST produce a postmortem commit. Not a Slack message. Not a verbal note. A commit. This is Senge Law 11 applied at operational level: the history is preserved even when it contains errors, because errors in the record are the learning substrate. [src:systems-expert-cybernetics-emergence.md:§2.2 Senge Law 11; src:sre-observability.md:§4 P5]

---

## §K Failure Modes

**Exhaustive enumeration with detection signal and halt-or-continue policy.** Per engineering critic mode pass. [src:engineering-expert-multi-mode.md:§K; src:investor-expert-long-term-compounding.md:§9]

**K1 — Partial commit (file written; git commit failed).**
Detection: `git status` shows uncommitted files post-attempt; `git log` does not reflect the write. Policy: HALT. Operator must decide: `git add + git commit` to complete, or `git checkout -- <file>` to revert local changes. NEVER auto-retry silently — silent retry may produce a second partial write. Antifragile response: commit the recovery action with a `[meta] revert: partial-commit recovery (K1 incident YYYY-MM-DD)` message. [F4|G:Part 1 git mechanics|R-high]

**K2 — Schema validation failure (pre-commit hook blocks commit).**
Detection: pre-commit hook exits non-zero; stderr names the schema violation; commit is blocked. Policy: HALT + INFORM. Human must fix the schema violation. Bypass via `git commit --no-verify` is a Law L-5 violation and is itself logged by lint signal #12 historical audit. HITL ack required before `--no-verify` bypass is acceptable. [F5|G:Phase B blocking hook; F4 Phase A log-only|R-high]

**K3 — Lint false-positive on valid commit message.**
Detection: `/lint --check-commit-format` flags a commit that is actually valid. Policy: CRITICAL — do NOT ship the hook in production until false-positive rate = 0. A false-positive-prone hook erodes trust and induces `--no-verify` bypasses (K6), which then evade audit detection entirely. The single-source `commit-format-tokens.json` file prevents token-list drift between hook and lint (the most common source of false positives). Pre-production acceptance predicate: run against last 50 commits; 0 false positives. [src:engineering-expert-multi-mode.md:§K K3; F4|G:P1.2 acceptance predicate|R-medium]

**K4 — Offline guarantee bypass (`/company-status` makes network call).**
Detection: `tools/tests/test-offline-guarantee.sh` exit non-zero; surfaces specific syscall (e.g., `connect: https://api.notion.com`). Policy: HALT immediately. Surface the specific syscall in error output. NEVER continue with potentially network-polluted output. Correct: fix the skill to remove the network call; re-run test; re-verify. [F3|G:P1.3 test stub; Law L-3|R-medium until test infrastructure verified]

**K5 — Fork import collision (same path written in fork and parent since divergence).**
Detection: cross-fork provenance schema validation failure on `divergence_point.commit_hash` mismatch OR conflicting paths in parent and fork history since divergence. Policy: HALT. Phase A: all cross-fork imports use `reconciliation_strategy: deferred-phase-b` — reject any import not marked deferred. Phase B: reconciliation algorithm handles this. [F3|G:Phase B deferred; D27|R-low — Phase B not yet materialised]

**K6 — Hook bypass attempt (`git commit --no-verify`).**
Detection: `git log` shows commit with message not matching format regex (detected retroactively by `/lint --check-commit-format --all`). Cannot prevent retroactively. Policy: LOG + AUDIT. `/lint --all` run by Part 8 health monitor detects historical bypasses; surfaces as lint signal incident. Each bypass must produce a follow-up commit documenting the reason for bypass and confirming HITL ack was obtained. [F4|G:Phase B hook blocking; F3 Phase A log-only|R-medium]

**K7 — Commit message area token expansion without schema update.**
Detection: `/lint --check-commit-format` flags valid commits as using "unknown area." This happens when a new area is used before `commit-format-tokens.json` is updated. Policy: FIX via schema update (HITL ack required). The `[new]` overflow token (§I.2) provides a sanctioned temporary bucket while the permanent token is being added. [src:engineering-expert-multi-mode.md:§K K7; Ashby overflow mechanism; F4|G:token DRY prevention|R-high]

**K8 — `git fsck` object errors.**
Detection: `git fsck` exits non-zero; object error count written to `shared/state/system-health.json`. Policy: HALT ALL CANONICAL WRITES. This is a Tier 0 integrity emergency. Part 8 alert fires. Ruslan ack required before any new commits. Recovery: restore from verified off-site backup; confirm 0 errors on restored repo before resuming. [src:investor-expert-long-term-compounding.md:§6.1 Tier 0 floor; F5|G:Part 1 integrity floor|R-high]

**K9 — Git repo loss (complete loss without backup).**
RISK-OF-RUIN event. Dollar floor estimate at Phase B: €40,000–€80,000 recovery cost for Strategic decisions, Methodology library, CRM history, Wiki KB — partial recovery feasibility only. [src:investor-expert-long-term-compounding.md:§6.1 failure cost table] Mitigation: 3-2-1 backup rule (3 copies, 2 different media, 1 off-site); quarterly restore drill (4 hours/year); margin-of-safety ratio of backup cost vs loss cost exceeds 200:1. [src:investor-expert-long-term-compounding.md:§3.2 arithmetic] Tier 0 data classification per FUNDAMENTAL §5.1: cannot lose, ever. RTO < 1 hour from verified backup. [F5|G:Tier 0 absolute|R-high on prevention; R-medium on recovery without backup]

**K10 — `unshare -n` unavailable on prod server (P1.3 HARD GAP).**
Detection: `unshare -n echo test` exits non-zero or produces "Operation not permitted." Policy: HARD GAP — P1.3 acceptance predicate CANNOT be satisfied without this. Fallback approaches in descending preference: (a) `strace -e trace=network <command> 2>&1 | grep -qE 'connect|socket'` (strace-based; requires strace installed); (b) `LD_PRELOAD`-based network call interception (requires compiled `.so` file). Ruslan must confirm which mechanism is available on the server before `test-offline-guarantee.sh` can be finalised. Current Ubuntu 22.04 / kernel 6.8.0-90: `unshare -n` should be available but unprivileged network namespace creation may require `sysctl kernel.unprivileged_userns_clone=1`. Requires explicit Ruslan ack. [src:engineering-expert-multi-mode.md:§L P1.3 HARD GAP]

**K11 — Inline `[src:]` citation drift across Parts 7/8/9 (latent R2 feedback loop).**
Detection: `/lint` citation density check (to be added as lint signal) flags Parts 7/8/9 with citation density below threshold set by Parts 1-3 and 6. Latent risk: the R2 provenance-drift reinforcing loop identified by systems analysis. If "PARTIAL citation density is acceptable" becomes the operational norm, the norm drifts toward no citation, degrading institutional memory silently. The lint signal is the balancing counterpart required to prevent loop activation. Policy: Wave C Bullet 3 (inline [src:] standardisation for Parts 7/8/9) must be treated as a lint-signal addition, not merely a manual cleanup — otherwise the drift loop reactivates. [src:systems-expert-cybernetics-emergence.md:§1.4 R2 loop; F3|G:Phase A lint signal gap|R-medium]

**K12 — Area token DRY violation (token list duplicated in hook and elsewhere).**
Detection: diff between `commit-format-tokens.json .tokens` array and any other location where tokens are listed (CLAUDE.md, hook embedded list) reveals divergence. Policy: FIX immediately — the single-source file is the authority; all other references update to point to it. Deploy-time check: CI step that validates `jq .tokens shared/schemas/commit-format-tokens.json` matches any embedded lists. [src:engineering-expert-multi-mode.md:§K K12; AP-ENG-11 DRY; F4|G:single-source token enforcement|R-high]

**K13 — Schema version drift (`schema_version_history:` block absent or stale).**
Detection: parsing a `git log` artefact with a schema version > 1.0.0 when tooling only knows version 1.0.0 — silent misparse produces incorrect provenance reconstruction. Policy: maintain `schema_version_history:` block in `commit-format.md` Foundation artefact. Every schema change increments version and adds a changelog entry. Tooling must implement upcasting logic per Young's event-versioning requirement. [src:investor-expert-long-term-compounding.md:§10 "Schema version drift"; src:event-sourcing-cqrs.md:§4 Principle 4 "upcasting"; F4|G:schema evolution discipline|R-medium]

---

## §L Wave C Work-List Bullet Status

**Three bullets from wave-c-worklist.md:L60-95.** Each with acceptance predicate and current satisfaction status. [src:wave-c-worklist.md:L66-95; src:engineering-expert-multi-mode.md:§L]

### P1.1 — Cross-fork provenance schema stub (D27)

**Design:** `shared/schemas/cross-fork-provenance.json` with all required fields declared (see §I.1). Foundation-layer generic; RUSLAN-LAYER separation enforced via `$comment` and `ip1_role_binding_overrides` RUSLAN-LAYER field labelling. Philosophy-expert requirement for ≥4 named cross-fork fields is satisfied: `parent_repo_id`, `parent_commit_hash`, `fork_id`, `fork_branch`, `divergence_point`, `reconciliation_strategy`, `audit_trail_continuation`, `f_g_r_on_imported_claims`, `ip1_role_binding_overrides` — 9 distinct named fields. Ashby `metadata` open field included. [src:philosophy-expert-epistemic-audit.md:§1.2 P1.1; src:systems-expert-cybernetics-emergence.md:§1.2]

**Deferred policy entry required:** A `decisions/policy/cross-fork-audit-deferred-phase-b.md` entry must declare: "Cross-fork audit trail reconciliation is Phase B architecture work. In Phase A, all cross-fork imports use `reconciliation_strategy: deferred-phase-b` and carry F2/R-low imported claims. Gap label: `[PHASE-B-DEFERRED: cross-fork-audit-trail]`." This prevents Wave C from inheriting the ambiguity silently. [src:engineering-expert-multi-mode.md:§L P1.1]

**Acceptance predicate status:** PARTIALLY SATISFIED

"Schema validates against synthetic Phase B partner test fixture; fork export+import roundtrip preserves audit chain with `imported_state_token` present and non-null; foreign branch/commit refs do not appear in parent `git log`."

Schema design: COMPLETE (§I.1 in this document). Test fixture: NOT YET EXISTS (Phase B work). The schema stub is at F3/R-low. Promoted to F4/R-medium when Phase B test fixture passes.

**Option value registered (per investor-expert).** Declaring this gap now at M-cost prevents 570+ commits/month of harder-to-extract content accumulating without declared fork-separation. Every month of silence on D27 = ~570 commits of potentially Ruslan-specific content that becomes harder to extract into a generic Foundation. The option cost (one policy file + schema design) is bounded; the option value is the entire Phase B ecosystem-level distribution thesis. [src:investor-expert-long-term-compounding.md:§7 D27 cross-fork option value]

### P1.2 — D25 commit-format lint rule as Foundation artefact

**Design:** `swarm/wiki/foundations/part-1-system-state-persistence/commit-format.md` Foundation artefact with: format rule (§I.2 regex), accepted area tokens (enumerated in `shared/schemas/commit-format-tokens.json`), anti-scope (format only, not content), `schema_version_history:` block (investor HARD GAP), and Hamel-binary acceptance predicate. Extends `/lint` as signal #12. Area token list in single-source-of-truth file (DRY compliance). Hook stub `tools/git-hooks/pre-commit-format.sh` (§H.2). [src:wave-c-worklist.md:L77-86; src:engineering-expert-multi-mode.md:§L P1.2]

**Hamel-binary acceptance predicate (philosophy-expert confirmed PASS):** "Lint run on last 50 commits produces 0 false positives AND flags any malformed commit (tested by running lint against a deliberately malformed test commit message that fails the regex)." Both halves are independently falsifiable. [src:philosophy-expert-epistemic-audit.md:§1.2 P1.2]

**`(why)` optionality OQ registered.** Philosophy-expert raises: should `(why)` be mandatory in the lint rule? First-principles argument (§2.3 of philosophy cell): `(why)` is the ONLY component that enables future re-derivation of decision rationale; making it optional means the system is reconstructable as to what happened but not reliably as to why. At Phase A (single founder, high context), optional is acceptable. At €1M scale with a managed team, the rationale gap becomes acute. Decision requires Ruslan ack — this is a Method-level change for the commit format convention. Registered as OQ-PHIL-PART1-3. [src:philosophy-expert-epistemic-audit.md:§2.3]

**Acceptance predicate status:** DESIGN COMPLETE; IMPLEMENTATION PENDING

`commit-format.md` Foundation artefact is designed; `pre-commit-format.sh` and lint signal #12 are designed but not yet written as implemented files. Wave C materialisation step must produce both. The design is complete.

### P1.3 — `/company-status` + `/knowledge-diff` offline-first guarantee

**Law declared:** §E Law L-3 declares the offline-first guarantee as a constitutional invariant. Every invocation must make ZERO network calls; halt on any attempted network syscall. This is the Wave C constitutional declaration for skills that were already operational. [src:engineering-expert-multi-mode.md:§E Laws item 3]

**Test stub design:** `tools/tests/test-offline-guarantee.sh` using `unshare -n` (primary) or `strace` (fallback). §H.3 specifies the interface.

**Acceptance predicate:** "Test exits 0 when run against both skills; test exits non-zero with specific syscall name if any network call is made during execution of either skill."

**Acceptance predicate status:** LAW DECLARED; TEST IMPLEMENTATION BLOCKED BY HARD GAP (K10)

`unshare -n` availability on the production server must be confirmed by Ruslan before `test-offline-guarantee.sh` can be finalised. The Law declaration is complete; the enforcement verification is blocked. This is a HITL ack item.

---

## §M Wisdom Application Findings

**TODO — to be populated by Wisdom Loop in Phase D.**

This section is reserved for the Wisdom Loop subagent to verify and document which Wave B Supplement library-direct source wisdom was correctly applied in this document vs. cited without application (cargo-cult prevention). The following items have been pre-registered as wisdom-applied in this document:

**Wisdom pre-registration (integrator self-assessment — to be verified by Wisdom Loop):**

| Wisdom source | Application location | Applied claim | Wisdom Loop verification status |
|---------------|---------------------|---------------|----------------------------------|
| Event Sourcing Young 2010 — Reversal Transactions | §C.1, §C.5, §E Laws L-5 | `git revert` as only canonical undo; `git reset --hard` as constitutional violation | PENDING Wisdom Loop |
| SRE Four Golden Signals (Google SRE Ch. 6) | §B.1 | Named 4 signals: commit-latency-p95, commit-cadence-per-day, hook-failure-rate, repo-growth-rate-MB-per-day | PENDING Wisdom Loop |
| Unix philosophy (Raymond) | §H | Plain-text outputs emphasized; §I schemas are JSON+YAML plain text; deep-module interface design | PENDING Wisdom Loop |
| Ousterhout deep-modules | §0 Executive summary; §H | Part 1 framed as deep module; narrow interface / wide internal complexity diagram | PENDING Wisdom Loop |
| Taleb antifragility | §0, §C.4, §K K9 | Append-only as antifragility floor; 200:1 margin-of-safety on backup; disorder-as-strengthening | PENDING Wisdom Loop |
| Ashby requisite variety | §I.2 overflow token; §E Laws L-2 annotation | `[new]` overflow token + lint-signal-13 as variety-gap mechanism | PENDING Wisdom Loop |
| Meadows leverage points | §D.3; §E Laws annotations | L2/L5/L6 annotations on each §E Law; leverage level as risk-communication convention | PENDING Wisdom Loop |
| Senge Law 11 (No blame) | §C.4, §J postmortem ritual, §F anti-scope | Append-only as structural implementation of blameless culture | PENDING Wisdom Loop |
| Graham margin-of-safety | §K K9 | 200:1 ratio backup cost vs loss cost; discipline cost arithmetic | PENDING Wisdom Loop |
| Young event versioning / upcasting | §I.3, §K K13 | `schema_version_history:` block; upcasting requirement for old records | PENDING Wisdom Loop |

---

## §N Provenance

**Every source consulted with consequence sentences.** Per shared-protocols §2 provenance gate. [src:swarm/lib/shared-protocols.md:§2]

| Source path | Section used | Key contribution | Consequence for this document |
|-------------|-------------|------------------|-------------------------------|
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-1-system-state-persistence.md` | §A-§H (all) | Baseline interface card; Laws, Admissibility, Deontics, Effects, F-G-R table | Primary specification source; Wave C architecture extends and completes it |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` | L60-95 (Part 1 bullets) | Three Wave C bullets with acceptance predicates and effort tiers | Defines the three deliverables: P1.1 schema stub, P1.2 lint artefact, P1.3 offline guarantee |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-1/engineering-expert-multi-mode.md` | §A-§Z (all, ~5200 words) | Primary cell; critic + scalability + integrator passes; all schemas designed here | Foundation for §B raw-task-return-packet field, §I schemas, §H CLI signatures, §K failure modes, §L bullet status |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-1/investor-expert-long-term-compounding.md` | §1-§11 (all, ~4000 words) | Lindy thesis, antifragility analysis, margin-of-safety arithmetic, schema versioning HARD GAP, D27 option value | §0 Lindy framing, §G F6+ rationale for git log, §K K9 risk-of-ruin arithmetic, §I.3 schema_version_history block |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-1/systems-expert-cybernetics-emergence.md` | §1.1-§2.3 (all, ~4000 words) | VSM S1 placement, Ashby variety gap, Meadows leverage, Four Golden Signals, feedback loops, institutional memory emergence | §B.1 Four Golden Signals enumeration, §D.3 Meadows annotations, §I.2 overflow token, §F R2 latent loop anti-scope |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-1/philosophy-expert-epistemic-audit.md` | §1-§9 (all, ~3200 words) | Popperian falsifiability pass, F-G-R re-tagging, IP-1 audit, cargo-cult audit, dichotomy of control, OQs | §E Laws category precision (Deontic-until-enforcement), §G F-level re-tagging rationale, §I.1 ≥4 named fields requirement |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/cells/part-1/mgmt-expert-boundary.md` | §1-§10 (all, ~2800 words) | L/A/D/E gap audit, admissibility gaps (size, encoding, binary), Deontics conversion, §H gap, scope-creep risks | §E Admissibility A-3/A-4/A-6 (new rows), §E Deontics D-1 SLI conversion, §F Risk R-1/R-2/R-3 explicit rejections, §H.4 schema |
| `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` | §0 (TL;DR), §5.1 (company-status) | 571 commits/30 days empirical data; `/company-status` description | §0 headline numbers, §G F6 empirical evidence row, §J ritual cadence baseline |
| `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` | §5.1 Tier 0, §2.1, §6.1 | Tier 0 data classification; append-only substrate; FUNDAMENTAL §6 anti-scope rules | §E Laws citations, §F generic anti-scope, §K K9 Tier 0 emergency classification |
| `design/JETIX-FPF.md` | §3.5 D25, §4.2 F-G-R, §5.1 IP-1, §5.3 IP-3 | D25 Company-as-Code Lock; FPF B.3 F-G-R; IP-1 Role≠Executor; IP-3 writing-as-thinking | Throughout; D25 cited in every Law; IP-1 in cross-fork schema; IP-3 in binary/text discrimination |

---

## §X Foundation vs RUSLAN-LAYER Separation

**Explicit fork-separation per OQ-MERGED-3.** The Foundation layer is generic (any fork can adopt it). The RUSLAN-LAYER is Jetix-specific (instance values for a specific deployment). Phase B partner adoption: clone Foundation schemas and Laws, replace RUSLAN-LAYER tokens with their own values. [src:engineering-expert-multi-mode.md:§X; src:philosophy-expert-epistemic-audit.md:§3.3]

### §X.1 GENERIC Foundation (fork-portable)

These artefacts contain NO Jetix-specific values. A Phase B partner adopts them as-is:

| Artefact | Why GENERIC | Phase B action |
|----------|-------------|----------------|
| `shared/schemas/cross-fork-provenance.json` schema structure | JSON Schema; no Jetix-specific values; `$comment` declares GENERIC explicitly | Adopt as-is; bind `parent_repo_id` and `fork_id` in RUSLAN-LAYER config |
| `^\[(area)\] (verb) (subject)( \(why\))?$` commit regex | The format rule is generic; any D25-disciplined repo uses it | Adopt regex; customise area token list in own `commit-format-tokens.json` |
| `shared/schemas/commit-format-tokens.json` schema structure | JSON Schema structure is generic; base token vocabulary is generic | Adopt schema; extend `.tokens` array with own area names in RUSLAN-LAYER config |
| `tools/git-hooks/pre-commit-format.sh` hook script | Hook validates against the regex + token list; no Jetix-specific values embedded | Adopt hook; point it at own `commit-format-tokens.json` |
| `tools/tests/test-offline-guarantee.sh` | Test mechanism (network isolation + exit-code check) is generic | Adopt test; configure for own skill names |
| F-G-R tagging schema (§G table structure) | FPF B.3 F-level taxonomy is generic | Apply same taxonomy to own artefacts |
| SRE Four Golden Signals names | Signal names (commit-latency-p95, hook-failure-rate, etc.) are generic | Adopt names; set own SLO thresholds in RUSLAN-LAYER Part 8 |
| A.14 typed edge vocabulary (`operates-in`, `methodologically-uses`, `constrained-by`) | FPF A.14 is generic | Apply same edge types to own Part dependency graph |
| Law L-1 through L-6 (structure and principle) | Constitutional principles are generic; specific enforcement mechanisms may vary | Adopt Laws; implement enforcement hooks per own infrastructure |
| Reversal Transactions pattern (§C.5) | Young 2010 pattern is generic | Adopt `git revert` as only canonical undo |

### §X.2 RUSLAN-LAYER (Jetix-specific instance values)

These are the specific values that make Part 1 Jetix's Part 1, not the generic Foundation's Part 1:

| Artefact | Why RUSLAN-LAYER | Phase B isolation |
|----------|-----------------|-------------------|
| `parent_repo_id`, `fork_id` field VALUES in provenance records | Actual repo identifiers are Jetix-specific. Declared in RUSLAN-LAYER config, not in schema file | Declare own repo IDs in own config |
| Specific area token strings (`swarm`, `prompts`, `cycles`, `crm`, etc.) | Reflect Jetix's specific directory structure and work domains | Fork declares own area tokens extending the base vocabulary |
| Branch names (`claude/jolly-margulis-915d34`, `main`) | Git session-specific to Jetix | Never appear in Foundation schema or skill spec |
| `.claude/config/*.yaml` specific path | CLAUDE.md path convention is Jetix-specific | Fork uses own config path; Foundation says "declarative config files, path per fork" |
| CLAUDE.md content | Jetix OS operational constitution | Fork writes own CLAUDE.md with same structural role |
| Notion IDs (in CLAUDE.md) | Ruslan's specific Notion workspace | Fork uses own Notion workspace or different display layer |
| Off-site backup target URL | Ruslan's specific backup provider | Fork uses own backup provider |
| `decisions/policy/cross-fork-audit-deferred-phase-b.md` CONTENT | The specific deferral decision is Jetix's architectural choice for this phase | Fork makes own deferral decision; may activate Phase B reconciliation earlier |
| SLO threshold VALUES for Four Golden Signals | Part 8 SLO thresholds are Jetix-specific | Fork sets own thresholds based on own operational norms |
| Weekly fsck cron time (Sunday 02:00) | Ruslan's preferred maintenance window | Fork configures own maintenance window |

### §X.3 Boundary principle

**Schemas + Laws + edge types + signal names are GENERIC.** Instance values (repo IDs, branch names, area token strings that are Jetix-specific, Notion IDs, backup targets) are **RUSLAN-LAYER**. The schemas declare the shape; RUSLAN-LAYER config populates the values. A Phase B partner who clones Foundation Part 1 gets: (a) all schema files with correct structure, (b) all Law principles with correct invariant logic, (c) all CLI interfaces with correct contract signatures. They configure the RUSLAN-LAYER values (repo ID, token list, backup target) in a separate config layer that does not touch Foundation schema files. This is the clean fork-separation that D27 architecture depends on.

The specific config path `.claude/config/*.yaml` named in §A is a RUSLAN-LAYER binding. A generic Foundation Part 1 would declare: "declarative configuration files that are version-controlled and committed before taking effect — specific path per fork instance." [src:philosophy-expert-epistemic-audit.md:§3.3 Foundation/RUSLAN-LAYER audit finding]

---

## Open Questions Registered (pending Ruslan ack or Phase B resolution)

The following open questions are registered in priority order. Each requires explicit resolution before the associated acceptance predicate can be satisfied.

| OQ ID | Question | Source cell | Resolution path | Blocking? |
|-------|----------|-------------|-----------------|-----------|
| OQ-PHIL-PART1-1 | Is commit-format Law L-2 currently a Law or a Deontic? This document has resolved: it is a Deontic until Phase B blocking hook is live. Ruslan should confirm this resolution is acceptable or request a different treatment. | philosophy-expert §7 | Ruslan ack or Wave D Wisdom Loop | Not blocking for Wave C |
| OQ-PHIL-PART1-3 | Should `(why)` in `[area] verb what (why)` be mandatory in the P1.2 lint rule? First-principles argument supports mandatory; Phase A context supports optional. This is a Method-level change requiring Ruslan ack. | philosophy-expert §2.3 | Ruslan ack required (Method-level change) | Blocks P1.2 final lint rule if mandatory is desired |
| OQ-PART1-K10 | Is `unshare -n` available on the production server (Ubuntu 22.04 / kernel 6.8.0-90)? Confirm which of {`unshare -n`, `strace`, `LD_PRELOAD`} is available before `test-offline-guarantee.sh` can be finalised. | engineering-expert §L P1.3 HARD GAP | Ruslan ack on server capability | Blocks P1.3 acceptance predicate satisfaction |
| OQ-PHIL-PART1-2 | Does the Phase A hook layer address `--amend` pre-push invisibility? Pre-push hook required for no-`--amend` enforcement; post-hoc `git log` is insufficient. Engineering-expert should confirm. | philosophy-expert §7 | Wave D engineering pass | Not blocking for Wave C |
| OQ-PHIL-PART1-4 | Several Part 1 Laws cite FUNDAMENTAL sections. FUNDAMENTAL is a RUSLAN-LAYER locked Vision document, not a Foundation artefact. For D27 fork-and-merge, Part 1 should embed the relevant FUNDAMENTAL clauses it depends on as Foundation invariants, rather than citing RUSLAN-LAYER locked docs. | philosophy-expert §7 | Phase B D27 architecture work | Not blocking Phase A; blocking for Phase B fork distribution |
| OQ-PART1-SYS-1 | Does Part 8's interface card author prefer to own SLI signal definitions for Part 1, or does Part 1's §B.1 Four Golden Signals enumeration stand as the contract? Both architectures are valid; integrator must pick one to avoid duplicate-definition anti-pattern. | systems-expert OQ-PART1-SYS-1 | Brigadier + Part 8 architecture.md author | Not blocking Wave C; must resolve before Bundle 3 Part 8 work |

---

*End of Part 1 — System State Persistence — Architecture.md.*
*Produced by: engineering-expert, integrator mode, Wave C Bundle 1.*
*Date: 2026-04-28. All claims carry `[src:]` citations with consequence sentences.*
*Proposed write: `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md`.*
