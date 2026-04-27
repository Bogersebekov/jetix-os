---
title: Part 1 — System State Persistence — Architecture
date: 2026-04-28
type: foundation-architecture
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 1
status: ruslan-acked-canonical
wisdom_loop_adoption: "YES=18 NO=4 ALREADY_APPLIED=18"
critic_findings_resolved: "philosophy CC-1..CC-4 fixed inline; engineering DRY-1 / FINDING-2 / FINDING-3 / K15/K16/K17 fixed inline"
F: F5
F_promotion_ack: "Ruslan ack 2026-04-28 per decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md — F4→F5 (codified rule, written and reviewed at Wave C architecture level). Promotion to F6 contingent on ≥3 successful applications across cycles 13+ (Lindy substrate evidence accumulating). OQ-B1-7 unshare -n: NOT available (sandbox AppArmor); strace 6.8 fallback path confirmed available — P1.3 acceptance predicate satisfiable via strace."
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
- **Constitutional provenance requirement (CAI Bai 2022 §3).** Every committed file must be human-inspectable plain text. This is not merely an encoding rule — it is the transparency requirement that makes the entire audit trail auditable by Ruslan without tooling intermediaries. A binary blob that only a tool can read is a provenance dead-end: the audit trail points to it, but no human can verify its content at the bit level. Constitutional AI's transparency principle applied to the substrate: "every committed artefact must be legible to the party bearing consequences." Enforcement: Law L-6 in §E. Accepted exceptions: audio files (voice transcripts), images (must be accompanied by a descriptor commit) — both tracked via Git LFS with HITL ack, per A-4. [src:anthropic-constitutional-ai.md:§4 P6 transparency; src:bai-2022-cai.md:§3 "only human oversight is provided through principles"; F4|G:Part 1 Jetix Phase-A|R-high]
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

The interface card previously declared "repo integrity metrics (commit cadence, branch status, backup SLI)" as the signal set emitted to Part 8. This is a bucket, not a signal taxonomy. Part 8 cannot define its SLI/SLO schema for Part 1 without knowing what signals Part 1 emits. The Google SRE Book Chapter 6 Four Golden Signals framework — **Latency, Traffic, Errors, Saturation** — provides the minimal complete taxonomy [Google SRE Book Ch.6 "Monitoring Distributed Systems" p.60: "In our experience, the most relevant metrics for most services are...the four golden signals: latency, traffic, errors, and saturation"]. Applied to the git substrate: [src:systems-expert-cybernetics-emergence.md:§1.5; src:sre-observability.md:§3 Source 1 Ch. 6 pp.55-66; src:google-sre-book.md:Ch.6 p.60]

**Why all four are necessary and sufficient for Part 1.** Latency catches a degrading pre-commit hook (slow schema validation). Traffic surfaces the commit rate signal that closes the B2 balancing loop. Errors catches hook false-positives and schema failures — the highest-risk quality degradation mode for Part 1. Saturation catches repo-size runaway, which at ≥10MB/day sustained would approach git performance thresholds within 12-18 months. Any signal set missing one of these four has a named blind spot. [src:sre-observability.md:§4 P1; F4|G:Part 1 Phase-A Four Golden Signals application|R-high]

**These threshold values are starter calibration parameters offered to Part 8 for adoption; Part 8 owns the canonical SLO contract per C2 contradiction resolution. Part 1 emits the signal; Part 8 sets the threshold.**

| Signal | Part 1 observable name | Measurement method | Emitted to Part 8 as | SLI target |
|--------|------------------------|--------------------|-----------------------|------------|
| **Latency** | `commit-latency-p95` | `time git commit` (instrumented in pre-commit hook; result appended to `shared/state/metrics/`) | p95 commit time in milliseconds | ≤3000ms (3 seconds) (starter) |
| **Traffic** | `commit-cadence-per-day` | `git log --oneline --after="24 hours ago" \| wc -l` (run at cron midnight) | integer count per 24h window | Informational only Phase A; threshold set by Part 8 (starter) |
| **Errors** | `hook-failure-rate` | Pre-commit hook non-zero exit events per total commit attempts in rolling 7-day window | float (events / total) | SLO ≤ 2% per week (false positives are errors; see K3) (starter) |
| **Saturation** | `repo-growth-rate-MB-per-day` | `du -sh .git` delta over 24h window (run at cron midnight) | float MB/day | Target ≤ 10MB/day; alert threshold at Part 8's discretion (starter) |

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

**Typed A.14 edges only.** No `depends-on`, no bare `uses`. Every edge uses A.14 typed vocabulary per FPF §3.5. Part 1 is the substrate root — it has zero upstream Part dependencies. All Parts 2-10 depend on Part 1; Part 1 depends on nothing above it. [src:part-1-system-state-persistence.md:§D; src:levenchuk-shsm-fpf.md:§4 P4 A.14 typing] Therefore each Part 1 dependency edge is one of the 10 named A.14 types — generic `depends-on` would erase mereological semantics that Part 6 governance later relies on for promotion validation.

**The 10 valid A.14 edge types (for dependency audits).** Per FPF A.14 Advanced Mereology [FPF-Spec A.14 L.17478] + JETIX-FPF §3.5 Rec-05 + mereology-typed-edges consultant card §4:

| Edge type | Meaning | When to use |
|-----------|---------|-------------|
| `ComponentOf` | Strict structural part — destroying the whole destroys this component | Machine component, code module that is truly part of a system |
| `ConstituentOf` | Non-strict part — element that makes up a whole but can exist independently | Wiki entry that constitutes the KB (but can survive KB migration) |
| `PortionOf` | Homogeneous mass portion | One agent's strategies.md is a portion of all strategies.md files |
| `PhaseOf` | Temporal phase of an entity | Draft status is a phase of an artefact's lifecycle |
| `MemberOf` | Set membership | An artefact is a member of the wiki entity collection |
| `AspectOf` | Observable facet, not a structural part | Commit-latency is an aspect of Part 1's observable state |
| `creates` | Agent/process that produces an entity | Brigadier creates canonical wiki pages |
| `operates-in` | Entity exists within a substrate, independently of it | Wiki content operates-in the git substrate |
| `methodologically-uses` | Entity uses another as a method/tool | Governance methodologically-uses git commit as enforcement |
| `constrained-by` | Entity is constrained by a rule/schema | Cross-fork imports constrained-by cross-fork provenance schema |

**Prohibited in §D:** `depends-on`, `uses`, `calls`, `reads`, `writes`, `triggers`, `needs` — all generic and non-mereological. If unsure which A.14 edge applies, escalate to the mereology-typed-edges consultant card before declaring. [src:mereology-typed-edges.md:§4; src:levenchuk-shsm-fpf.md:§4 P4 AP-L3; F4|G:Part 1 dependency graph|R-high]

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

### §F.3 Stoic Dichotomy of Control — What Part 1 Laws Govern

**Sourced.** The Stoic dichotomy of control (Epictetus, Enchiridion §1; Holiday *Daily Stoic* Introduction): "Some things are in our control and others not. Things in our control are opinion, pursuit, desire, aversion — in a word, whatever are our own actions. Things not in our control are body, reputation, command, and, in one word, whatever are not our own actions." Applied to engineering: Laws govern only what is within the system's control. Attempting to enforce Laws over external, uncontrollable events wastes design effort and creates false assurance. [src:stoic-epistemic.md:§4 P5 dichotomy-of-control]

**In our control (Laws apply):**
- Commit format (`[area] verb what (why)`) — fully within the committer's control; hook enforces it.
- No-amend, no-`--no-verify`, no-force-push — fully within the committer's control; HITL gate enforces it.
- `git fsck` weekly cadence — scheduled cron; fully within our control to run or skip.
- UTF-8 encoding of committed files — within the author's control; pre-commit check enforces it.
- Schema validation of YAML/JSON before commit — within the author's control; hook enforces it.

**Not in our control (Laws do NOT apply; failure modes documented in §K instead):**
- Hardware disk failure destroying the git object store (K9) — not in our control; mitigation is 3-2-1 backup (preparation, not control).
- Network partition preventing off-site backup sync (K9) — not in our control; mitigation is backup cadence monitoring.
- Git's internal corruption under extreme I/O conditions (K8) — not in our control; mitigation is fsck detection + restore.
- Force-push by a third party on a shared remote (if applicable in Phase B) — not in our control; mitigation is branch protection rules.

**Consequence for Part 1 design.** Laws L-1 through L-6 govern ONLY the "in our control" category. Failure modes in §K are the documentation for "not in our control" — they carry mitigations and response policies, not constitutional Laws. This boundary prevents scope creep where Part 1 attempts to constitutionally mandate outcomes it cannot structurally enforce. [src:stoic-epistemic.md:§4 P5; src:philosophy-expert-epistemic-audit.md:§6; F4|G:Part 1 Law scope boundary|R-high]
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
| **`git log` provenance chain** | F6 | Codified rule + ≥3 successful applications. 571 commits in 30 days clearly exceeds ≥3 by two orders of magnitude. Cross-cycle reuse confirmed. [src:AUDIT:§0; src:philosophy-expert-epistemic-audit.md:§4 "git log F6 confirmed"] The Merkle-tree cryptographic guarantee supports this — SHA-1 collision resistance provides a mathematical guarantee of non-mutability stronger than operational convention. F6 is the defensible ceiling in Phase A (F7+ requires formal peer-reviewed proof; SHA-256's collision resistance is engineering consensus, not a Jetix-specific proof). **Lindy confirmation (Taleb Antifragile Ch.20):** git is 19+ years old with 100M+ developer adoption — it satisfies the Lindy Effect: the longer a technology survives, the longer its expected remaining lifespan. The Lindy substrate thesis [src:capital-allocation-antifragility.md:§3 P6 Taleb; src:investor-expert-long-term-compounding.md:§1.1 Lindy thesis] justifies F6 confidence: this is not a trend-following choice, it is a Lindy-confirmed foundation. [src:taleb-antifragile-2012.md:Ch.20 Lindy Effect via capital-allocation-antifragility.md:§4 P6] | Holds for entire repo history; fork audit trails separate per D27 | R-high — immutable once committed; refuted only by repo corruption detectable by `git fsck` | SHA-256 migration (git plans) would elevate to F7-equivalent; no Jetix-specific action required |
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

**Unix philosophy — each tool does one thing well.** Per McIlroy's first law [src:unix-philosophy.md:§4 P1; src:raymond-art-of-unix-programming-2003.md:Ch.1 line 911]: "Make each program do one thing well." Applied to Part 1's CLI interface:
- `git commit -m "[area] verb what (why)"` — does ONE thing: appends a new, validated, formatted commit to the history.
- `git revert <hash>` — does ONE thing: creates a compensating commit that undoes a prior commit.
- `git log [--oneline] [--since] [--until]` — does ONE thing: queries the append-only event log.
- `/company-status [--days=N]` — does ONE thing: produces a human-readable substrate snapshot to stdout, zero side-effects, zero network calls.
- `/knowledge-diff [--since] [--until]` — does ONE thing: produces a delta report between two git-log dates.
- `/lint --check-commit-format [--count=N] [--all]` — does ONE thing: checks whether commit messages conform to the format rule.

No tool in this interface does two things. The Rule of Composition (Raymond AoUP Ch.1): these six tools compose via `git log | grep | wc -l` pipelines without any tool needing to know about any other. Part 1's deep-module property (Ousterhout) reinforces this: the narrow public interface IS the Unix-philosophy minimal interface. Each tool exposes exactly the function users need; git plumbing, schema validation, and snapshot assembly are the wide internal complexity hidden behind these six. [src:unix-philosophy.md:§4 P1-P2; src:engineering-expert-multi-mode.md:§H INTEGRATOR; src:clean-code.md:§4 P1 Ousterhout]

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
# Regex: ^\[(area)\] (verb) (subject)( \(why\))?$ (canonical definition: §I.2 commit-format-tokens.json)
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
    "health", "hooks", "infra", "ingest", "kb", "lint", "meta",
    "methodology", "new", "project", "prompts", "raw", "reports",
    "review", "schemas", "skills", "strategy", "swarm", "swarm-lib",
    "templates", "tools", "voice", "wiki"
  ]
}
```

**Note:** The current CLAUDE.md token list (kb, daily, project, raw, crm, meta, skills, infra) is a subset. The repo has grown beyond the original 8 areas; this authoritative list is the expansion. CLAUDE.md's list should reference `shared/schemas/commit-format-tokens.json` as authoritative rather than maintaining a separate list (DRY). [src:engineering-expert-multi-mode.md:§I.2 CRITIC "token list longer than CLAUDE.md list"]

**Bundle 3 retroactive supplement (2026-04-28):** Added `swarm-lib` token to canonicalise the Bundle 2 C1 Joint Design accessor pipeline area (`swarm/lib/` — accessor skills + routing-table.yaml + executor-binding.yaml live here per Part 3 LEAD + Part 4 ADVISORY governance). Also added `health` token (Part 8 Bundle 3 health snapshot commits) and `methodology` token (Part 5 Bundle 3 methodology promotion commits). All three additions per OQ-B2-A retroactive Bundle 1 fix + OQ-B2-D Bundle 2 ack canonicalisation of informally-used tokens. [src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§1 Decision #C1 Joint Design canonical; src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§2 OQ-B2-A + OQ-B2-D]

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
    format: "^\\[(area)\\] (verb) (subject)( \\(why\\))?$"  # canonical definition: §I.2 commit-format-tokens.json
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
  "required": ["git_commit_hash", "actor_role_archetype", "cycle_id", "gate_class"],
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
      "enum": ["stop_gate", "stage_gate", "draft_promotion"],
      "description": "The gate class under which this task was executed. Aligned to Part 6b §I.4 F8 LOCKED awaiting-approval-packet.json gate_class enum (canonical authority — single source of truth). stop_gate = Tier 0 integrity halt requiring same-session HITL ack; stage_gate = stage-bound observability/operational change requiring HITL ack; draft_promotion = methodology / canonical entity F4→F5 promotion gate. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4; src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§2 OQ-B2-A retroactive supplement]"
    }
  }
}
```

---

## §J Operational Rituals

**Every commit compounds — the superlinear value of git log.** Per Compounding Engineering (Klaassen / Shipper / Boris Cherny): "Each unit of engineering work should make subsequent units easier — not harder." [src:compounding-engineering.md:§2 core claim; src:MASTER-SYNTHESIS §1.5] Applied to the git substrate: the value of `git log` is NOT linear in commit count — it is superlinear. A single commit is a named action. Ten commits are a narrative thread. 570 commits in 30 days are a reconstructable institutional memory. Aggregation queries over a structured commit history (`git log --grep="^\[kb\]" --since="2026-01-01" --oneline | wc -l`) reveal patterns invisible at single-commit granularity: knowledge accumulation rate, skill area velocity, architectural decision frequency. Without the structured `[area] verb what (why)` format, these queries are impossible — the log is data-rich but information-poor. The commit format is not bureaucratic overhead; it is the mechanism by which each individual commit compounds into institutional memory. [src:compounding-engineering.md:§4 P2 DRR Ledger; src:capital-allocation-antifragility.md:§4 P1 Buffett owner-earnings analogy; F4|G:Part 1 Jetix Phase-A compound-value claim|R-high]

**Shape Up appetite (Singer 2019) + Cagan scope-boundary.** Wave C Part 1 architecture build: 2 working days maximum. The appetite is fixed; scope is variable. If §A-§J draft is not complete within 1.5 days, cut §J and §I to stub form. Do NOT scope-balloon. Circuit-breaker: if any Wave C bullet expands beyond its declared effort tier (S or M), re-shape to fit within tier or defer to Wave D with explicit `[deferred: Wave D]` label. Fixed-time variable-scope discipline. [src:mgmt-expert-boundary.md:§6 Cagan/Shape Up; src:product-management-cagan-shape-up.md:§4 Principle 2] Therefore if Wave C Part 1 build cycle exceeds 2 days, brigadier cuts scope (e.g., defer P1.1 cross-fork test fixture to Bundle 1.5) rather than expanding the cycle — appetite-fixed / scope-variable per Cagan.

| Ritual | Cadence | Trigger | Responsible | Expected output | Notes |
|--------|---------|---------|-------------|-----------------|-------|
| Commit with `[area] verb what (why)` | Event-driven (not scheduled) | Any Part producing a canonical state change | All Parts via orchestrator | Valid `git log` entry; hook exit 0 | Event-driven is correct: scheduled commits would produce noise |
| `git fsck` integrity check | Weekly (Sunday 02:00 system time, proposed) | Calendar cron + orchestrator cycle-start pre-check | Part 8 health monitor (triggers); Part 1 executes and writes result | 0 object errors; result in `shared/state/system-health.json` | Cadence gap from interface card closed; Part 8 owns alert routing |
| `/company-status` snapshot | Session-start + post-ack + weekly (Friday 17:00 Ruslan review ritual) | Owner session open OR after HITL gate ack OR weekly calendar | Owner + Part 9 | ≤80-line markdown report; 0 network calls | Three distinct triggers; only the weekly one is scheduled |
| `/lint --check-commit-format` | Pre-commit (automatic via hook) + weekly `/lint` run | git commit attempt + Part 8 weekly health check | Pre-commit hook (automatic Phase B blocking; log-only Phase A) + Part 8 | 0 format violations on last 50 commits (acceptance predicate P1.2) | Hook is the primary enforcement; `/lint --all` is the historical audit |
| `imported_state_token` generation | Phase B event (fork export) | Phase B partner fork export event | Phase B architecture (deferred) | Token mapped to fork state in parent audit log | Currently deferred; registered as ritual for Phase B planning visibility |

**SRE Workbook burn-rate algebra applied to Part 1 repo health SLO.** Per SRE Workbook Ch.2 [src:google-srewb-implementing-slos.md:§12 "Decision Making Using SLOs and Error Budgets"]: burn rates of 1×, 6×, and 14.4× govern when behaviour changes. Therefore if commit-error-rate burn = 14.4× in 1h window, Part 8 (when live) raises a P0 page; meanwhile Phase A response = `/company-status` shows red and human owner halts new commits until fsck clean. Applied to Part 1's primary SLO (git object errors = 0 per weekly fsck, i.e. 100% SLO):

| Burn rate | Part 1 observable | Required behaviour change |
|-----------|-------------------|--------------------------|
| **1× (normal)** | `git fsck` exits 0 every Sunday; `hook-failure-rate` ≤ 2% rolling 7d | No change — within SLO |
| **6× (urgent)** | `git fsck` exits non-zero OR `hook-failure-rate` reaches 6–12% in a 7d window | Ruslan notified within same session; non-critical canonical writes paused pending investigation |
| **14.4× (critical — page within 1 hour)** | `git fsck` exits non-zero with object errors > 0 OR `hook-failure-rate` ≥ 15% | ALL canonical writes halted (K8 policy); immediate HITL ack required; restore from verified backup if fsck objects corrupted |

The burn-rate model makes the SLO actionable rather than aspirational: the behaviour change is pre-declared per rate tier, not decided reactively. This is the SRE Workbook's core contribution — "alerting without behaviour change is noise." Part 8 owns the SLO threshold and alert routing; Part 1 declares the burn-rate tiers that map to its own failure modes. This stub is for Part 8 consumption. [src:google-srewb-implementing-slos.md; src:sre-observability.md:§4 P7; F3|G:Part 1 → Part 8 interface stub|R-medium — Part 8 must adopt these tiers in its Wave C materialisation]

**Blameless postmortem ritual.** Any incident affecting Part 1 (fsck error, hook bypass, offline guarantee violation) MUST produce a postmortem commit. Not a Slack message. Not a verbal note. A commit. This is Senge Law 11 applied at operational level: the history is preserved even when it contains errors, because errors in the record are the learning substrate. [src:systems-expert-cybernetics-emergence.md:§2.2 Senge Law 11; src:sre-observability.md:§4 P5]

**Evergreen note discipline (Karpathy / Matuschak).** This architecture document IS a Part 1-governed artefact that exemplifies the evergreen note principle. Per Matuschak [src:knowledge-management-karpathy-luhmann-matuschak.md:§4 P3 "evergreen notes"]: notes should be "written for your future self as a stranger; they evolve from fleeting → literature → evergreen concept." Applied to Foundation architecture documents: this document is NOT versioned-aside when updated — it is updated in-place via new commits, each commit extending the audit trail. The "evergreen" property is enforced by Part 1's own append-only substrate: `git log` for this file shows the evolution from initial Wave C draft through Wisdom Loop pass through critic-pass through canonical promotion. Each git commit IS a version — the version history IS the file's evolutionary record. This contrasts with "archive-and-replace" documentation practices where old versions are filed away and the current version loses its lineage. Foundation explicitly rejects archive-and-replace for architecture documents in favour of the evergreen + commit-history pattern. [src:knowledge-management-karpathy-luhmann-matuschak.md:§4 P3; src:karpathy-llm-wiki-gist-2026-04.md; F4|G:Foundation architecture documents evergreen discipline|R-high]

**SRE Ch.15 blameless postmortem culture applied.** Per Google SRE Book Ch.15 [src:google-sre-book.md:Ch.15 pp.169-175]: "The primary goals of writing a postmortem are to ensure that the incident is documented, that all contributing root cause(s) are well understood, and, especially, that effective preventive actions are put in place." The Foundation operationalizes this at the 5-line minimum per FUNDAMENTAL §2.4: what happened / why / what changed / how detect next / owner. Each postmortem is a committed strategies.md entry or a dedicated `[meta] postmortem:` commit. Without the commit, the postmortem does not exist — verbal debriefs vanish from the audit trail. The blameless principle applied to an agent swarm: agents do not experience blame, but they CAN be optimized to suppress failures silently (AP-ENG-1 test-deletion anti-pattern); the blameless culture at Part 1 means the pre-commit hook error is the signal to improve the hook, never to bypass it. [src:sre-observability.md:§4 P5; src:google-sre-book.md:Ch.15; F4|G:Part 1 postmortem discipline|R-high]

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

**Graham margin-of-safety applied to K9 (Capital Allocation card P2).** Graham's margin-of-safety principle: invest at a gap between price and intrinsic value large enough to survive being wrong about your estimates. Applied here: the "price" of backup infrastructure (AWS S3 cold storage + rsync cron = ~€5-10/month) is vastly below the "intrinsic value" protected (€40-80K recovery floor). Over-engineering backup is explicitly CORRECT here — the margin-of-safety calculation justifies what might seem like disproportionate infrastructure investment. The consequence sentence: "A founder who thinks 'backups are over-engineering for a Phase A system' is applying growth-stage thinking to a risk-of-ruin scenario — these are categorically different." Graham's principle precisely forbids this error. Per Munger inversion (capital-allocation-antifragility.md §4 P5): the question is not "how does backup add value?" but "what does K9 look like without backup?" — and the answer is irreversible data loss with no recovery path. Over-engineering backup is structurally correct for Tier-0 data. [src:capital-allocation-antifragility.md:§4 P2 Graham margin-of-safety; src:capital-allocation-antifragility.md:§4 P5 Munger inversion; F4|G:K9 risk-of-ruin mitigation|R-high]

**K10 — `unshare -n` unavailable on prod server (P1.3 HARD GAP).**
Detection: `unshare -n echo test` exits non-zero or produces "Operation not permitted." Policy: HARD GAP — P1.3 acceptance predicate CANNOT be satisfied without this. Fallback approaches in descending preference: (a) `strace -e trace=network <command> 2>&1 | grep -qE 'connect|socket'` (strace-based; requires strace installed); (b) `LD_PRELOAD`-based network call interception (requires compiled `.so` file). Ruslan must confirm which mechanism is available on the server before `test-offline-guarantee.sh` can be finalised. Current Ubuntu 22.04 / kernel 6.8.0-90: `unshare -n` should be available but unprivileged network namespace creation may require `sysctl kernel.unprivileged_userns_clone=1`. Requires explicit Ruslan ack. [src:engineering-expert-multi-mode.md:§L P1.3 HARD GAP]

**K11 — Inline `[src:]` citation drift across Parts 7/8/9 (latent R2 feedback loop).**
Detection: `/lint` citation density check (to be added as lint signal) flags Parts 7/8/9 with citation density below threshold set by Parts 1-3 and 6. Latent risk: the R2 provenance-drift reinforcing loop identified by systems analysis. If "PARTIAL citation density is acceptable" becomes the operational norm, the norm drifts toward no citation, degrading institutional memory silently. The lint signal is the balancing counterpart required to prevent loop activation. Policy: Wave C Bullet 3 (inline [src:] standardisation for Parts 7/8/9) must be treated as a lint-signal addition, not merely a manual cleanup — otherwise the drift loop reactivates. [src:systems-expert-cybernetics-emergence.md:§1.4 R2 loop; F3|G:Phase A lint signal gap|R-medium]

**K12 — Area token DRY violation (token list duplicated in hook and elsewhere).**
Detection: diff between `commit-format-tokens.json .tokens` array and any other location where tokens are listed (CLAUDE.md, hook embedded list) reveals divergence. Policy: FIX immediately — the single-source file is the authority; all other references update to point to it. Deploy-time check: CI step that validates `jq .tokens shared/schemas/commit-format-tokens.json` matches any embedded lists. [src:engineering-expert-multi-mode.md:§K K12; AP-ENG-11 DRY; F4|G:single-source token enforcement|R-high]

**K13 — Schema version drift (`schema_version_history:` block absent or stale).**
Detection: parsing a `git log` artefact with a schema version > 1.0.0 when tooling only knows version 1.0.0 — silent misparse produces incorrect provenance reconstruction. Policy: maintain `schema_version_history:` block in `commit-format.md` Foundation artefact. Every schema change increments version and adds a changelog entry. Tooling must implement upcasting logic per Young's event-versioning requirement. [src:investor-expert-long-term-compounding.md:§10 "Schema version drift"; src:event-sourcing-cqrs.md:§4 Principle 4 "upcasting"; F4|G:schema evolution discipline|R-medium]

**K15 — Concurrent commit `.git/index.lock` conflict.**
Two parallel agents attempting to commit simultaneously. Detection: git commit fails with "fatal: Unable to create '.git/index.lock'". Recovery: retry with exponential backoff (50ms / 200ms / 1s / 5s); if still locked after 5s — surface to human owner. Mitigation Phase B: queue commits via .partials/ shadow log, drain serially. [F4|G:Part 1 concurrency safety|R-medium]

**K16 — Disk-full during commit leaving dangling object.**
Commit halts mid-write. Detection: `git fsck` flags dangling blob/tree. Recovery: `git gc --prune=now` purges; if commit was load-bearing, owner reconstructs from session context. Mitigation: weekly `df -h` + alert at 85% usage. [F4|G:Part 1 storage integrity|R-medium]

**K17 — Cross-fork `commit-format-tokens.json` schema drift.**
Phase B partner forks Part 1, extends area enum to add their own area tokens (e.g., `[partner-ops]`). Their commits cannot import back into Jetix without enum reconciliation. Detection: cross-fork-provenance import flags unknown area token. Recovery: schema_version_history block tracks versions; reconciliation_strategy field in cross-fork-provenance.json declares 'merge-superset' as default. [F3|G:Part 1 fork discipline|R-medium]

**K18 — Legacy v1.0.0 message upcasting (Bundle 3 retroactive supplement per OQ-B2-A).**
The Bundle 2 message schema v1.0.0 → v2.0.0 BREAKING change made `acting_as:` mandatory and extended the `from:` enum [src:swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md:§H message schema v2.0.0; src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§1 Decision #6]. Part 1 commit substrate may receive legacy v1.0.0 messages from pre-Bundle-2 cycles in operational use (e.g., reprocessing archived task-return packets, replaying mailbox contents from before the schema cutover). Detection: on ingest, parser reads `schema_version` field; if `"1.0.0"`, branch to upcasting logic. Policy: detect `acting_as:` field; if missing, attempt upcast by inferring from `from:` field per role-archetype mapping (e.g., `from: engineering-expert` → `acting_as: engineering-expert.integrator` only when context unambiguous; otherwise REJECT with named-field error). Hamel-binary acceptance predicate: every legacy message either upcasts cleanly (with `upcast_provenance: {from_version: "1.0.0", to_version: "2.0.0", inferred_at: <timestamp>, inference_basis: <field-mapping-rule>}` annotation appended) OR rejects with named field error stating which field could not be inferred. NO silent acceptance of malformed v1.0.0 messages. Per Young 2010 §4 P4 event-versioning ("upcasting"): every schema evolution requires explicit version-tracking + upcasting logic — silent acceptance of pre-cutover messages corrupts the audit trail. Cross-ref K13 (schema version drift) — K18 is the K13 family operationalised for the message schema. **Numbering note:** the OQ-B2-A spec (2026-04-28) was authored unaware of pre-existing K15/K16/K17 in this file (concurrent commit lock / disk-full / cross-fork token drift); this failure mode is therefore filed as K18 to preserve numbering uniqueness; substantive content matches OQ-B2-A spec verbatim. [src:event-sourcing-cqrs.md:§4 Principle 4 "upcasting"; src:decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md:§2 OQ-B2-A; F4|G:Bundle 3 retroactive supplement; pre-cutover legacy ingest discipline|R-medium]

**K14 — Cascading failure: Part 1 git failure blocks all downstream Parts. (Phase B stub — SRE Ch.22)**
**[PHASE-B-DEFERRED: cascading-failure-graceful-degradation]**
Detection: `git fsck` exits non-zero AND `git commit` exits non-zero simultaneously — Parts 2-10 are unable to commit new state. This is the cascading failure scenario: a single Part 1 integrity failure blocks all downstream canonical writes. Policy: READ-ONLY MODE. All Parts switch to read-only mode: existing committed state remains accessible; no new commits are attempted until Part 1 integrity is restored. Commits queued to `.partials/<timestamp>-<area>-<subject>.md` (append-only staging area outside the main repo index) for replay once git integrity is confirmed. Alert format: `{timestamp, failure_type: "git-substrate", severity: critical, behaviour_change: "all canonical writes blocked — queuing to .partials/"}`. Per SRE Book Ch.22 "Addressing Cascading Failures": graceful degradation is the design principle — the system continues to function at reduced capacity rather than failing completely. Phase A: this failure mode is acknowledged and the `.partials/` pattern is declared but not implemented. Phase B: implement the queue-and-replay mechanism. [src:sre-observability.md:§3 Source 1 Ch. 22; src:google-sre-book.md:Ch.22; F2|G:Phase B stub only; not yet operational|R-low — deferred]

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

**Hamel-binary acceptance predicate (philosophy-expert confirmed PASS):** "Lint run on last 50 commits produces 0 false positives AND flags any malformed commit (tested by running lint against a deliberately malformed test commit message that fails the regex `^\[(area)\] (verb) (subject)( \(why\))?$` — canonical definition: §I.2 commit-format-tokens.json)." Both halves are independently falsifiable. [src:philosophy-expert-epistemic-audit.md:§1.2 P1.2]

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

> **Phase D Wisdom Application Loop pass — per deep-prompt §5.** For each Wave B consultant card and Wave B Supplement library-direct source: 5 questions asked (Application Gap / Cargo-Cult Audit / Concrete Improvement / Section Impact / Phase A Justification), findings recorded, YES Adopted edits applied to §A-§L above, NO entries justified per legitimate categories. Every pre-registered Wisdom claim verified against actual body text; every new adoption applied as real edit.

| # | Card / Source | Principle | Current draft state (pre-Wisdom-Loop) | Improvement opportunity | Adopted? | Justification | Section edited |
|---|---------------|-----------|----------------------------------------|-------------------------|----------|---------------|----------------|
| 1 | Левенчук SHSM-FPF | IP-3 Artifacts-over-conversations | Applied throughout: every canonical state = committed file; §C.4 "no learning is real unless committed"; §A §E enforcement | — | ALREADY APPLIED | §0, §C.4, §E Laws, §F.2, throughout | n/a — confirmed |
| 2 | Левенчук SHSM-FPF | A.14 Typed edges | §D uses `operates-in`, `methodologically-uses`, `constrained-by` — all valid A.14 edges; no `depends-on` present | Add explicit 10-edge reference table so Wave C authors for other Parts have a canonical lookup | YES | Gap was the lookup table; edges themselves were already correct A.14 | §D — added 10-edge-type table |
| 3 | Левенчук SHSM-FPF | F-G-R trust tagging (B.3) | §G F-G-R table present with rationale per row | — | ALREADY APPLIED | §G (full table) | n/a — confirmed |
| 4 | Левенчук SHSM-FPF | L/A/D/E lanes (A.6.B) | §E structured in Laws / Admissibility / Deontics / Effects — full L/A/D/E compliance | — | ALREADY APPLIED | §E (all 4 lanes) | n/a — confirmed |
| 5 | Capital Allocation Antifragility | Lindy substrate (Taleb Ch.20) | §0 mentions "Lindy-confirmed" + 19 years + 100M developers. §G git-log row references Lindy thesis. Gap: no explicit Taleb citation with consequence sentence in §G | Add explicit Taleb Lindy citation with consequence sentence to §G git-log F6 row | YES | Gap was explicit citation and consequence sentence; claim was partially applied | §G — added Lindy citation to git log row |
| 6 | Capital Allocation Antifragility | Graham margin-of-safety (P2) | §K K9 mentions "margin-of-safety ratio 200:1" but without the Graham reasoning chain | Add Graham margin-of-safety consequence sentence explaining WHY over-engineering backup is correct | YES | Gap was reasoning chain; the number was present without the principle | §K K9 — added Graham margin-of-safety consequence block |
| 7 | Capital Allocation Antifragility | Taleb antifragility — disorder strengthens (P6) | §0, §C.4, §K K9 all apply Taleb antifragility correctly | — | ALREADY APPLIED | §0 "disorder strengthens the record", §C.4 "failures as permanent learning commits", §K K9 | n/a — confirmed |
| 8 | Unix Philosophy | Plain-text as universal interface (P2) | §A Admissibility specifies UTF-8 text; §I schemas are JSON+YAML; §H deep-module diagram. Gap: no explicit McIlroy/Raymond citation linking plain-text choice to Unix philosophy | Add explicit Unix philosophy citation to §H noting each CLI tool does ONE thing and composes | YES | Gap was explicit McIlroy citation and "do one thing well" enumeration per tool | §H — added Unix philosophy tool-per-function enumeration |
| 9 | Unix Philosophy | Everything-is-a-commit (Raymond SPOT) | §E Law L-1 "No canonical state outside git" is SPOT applied | — | ALREADY APPLIED | §E Law L-1 | n/a — confirmed |
| 10 | Event Sourcing CQRS | Young 2010 — "There is no Delete" / Reversal Transactions (p.31) | §C.1 and §C.5 explicitly cite Young 2010 p.31 with full consequence sentences; §E Law L-5 also cites | — | ALREADY APPLIED | §C.1, §C.5, §E Law L-5 | n/a — confirmed |
| 11 | Event Sourcing CQRS | Append-only event log as source of truth (Principle 1) | §E Law L-1 implements this; §B git history row cites event-sourcing-cqrs.md §4 Principle 1 | — | ALREADY APPLIED | §E Law L-1, §B outputs table row | n/a — confirmed |
| 12 | Event Sourcing CQRS | Young event versioning / upcasting (Principle 4) | §I.3 `schema_version_history:` block and §K K13 explicitly address upcasting | — | ALREADY APPLIED | §I.3, §K K13 | n/a — confirmed |
| 13 | Clean Code (Ousterhout deep-modules) | Deep-module test: impl-LoC >> interface-LoC | §0 frames Part 1 as deep module; §H narrow-interface/wide-internal-complexity diagram present | — | ALREADY APPLIED | §0, §H diagram | n/a — confirmed |
| 14 | Clean Code (Brooks) | No-silver-bullet — abstractions earn weight at ≥3 uses | Not directly applicable to Part 1 (no abstract interfaces to audit in a substrate part); Part 1's interface is CLI commands, not software abstractions | No concrete improvement for Part 1; relevant for Part 3/5 software abstractions | NO | Premature-optimization for Phase A — Brooks applies to Parts 3/5 abstraction layers; Part 1 is a thin substrate | n/a |
| 15 | SRE Observability | Four Golden Signals — Latency, Traffic, Errors, Saturation (SRE Ch.6 p.60) | §B.1 had the four signals enumerated but the citation referenced systems-expert and sre-observability.md card, NOT the primary source (google-sre-book.md Ch.6 p.60) | Add primary SRE Book Ch.6 p.60 citation AND explain WHY all four are necessary and sufficient for Part 1 | YES | Gap was primary source citation + necessity/sufficiency explanation | §B.1 — added primary SRE Book citation and explanatory paragraph |
| 16 | SRE Observability | Blameless postmortems (SRE Ch.15) | §J mentions "blameless postmortem ritual" with Senge Law 11 + sre-observability.md citations. Gap: no direct SRE Ch.15 citation with verbatim grounding and consequence sentence | Add explicit SRE Ch.15 citation with verbatim quote and agent-swarm consequence sentence | YES | Gap was primary SRE Book Ch.15 citation; application was partially present | §J — added SRE Ch.15 blameless postmortem culture block |
| 17 | SRE Observability | Cascading failures graceful degradation (SRE Ch.22) | Not present in draft — no cascading failure entry in §K failure modes | Add K14 cascading failure entry: git failure → all downstream Parts blocked → graceful degradation via .partials/ queue (Phase B stub) | YES | Application Gap confirmed; Phase A stub is justified — declares the pattern before it becomes load-bearing | §K — added K14 cascading failure entry |
| 18 | SRE Observability | Error budget behaviour change — not just fire alerts (SRE Ch.6 P7) | §J has "Blameless postmortem ritual" but no burn-rate triggers for repo health SLO | Add burn-rate algebra (1×/6×/14.4×) triggered behaviour changes for Part 1 SLOs | YES | Gap confirmed; Phase A justified — pre-declares the model before Part 8 consumes it | §J — added burn-rate table and behaviour change declarations |
| 19 | Systems Thinking Cybernetics | Meadows leverage points L2/L5/L6 | §D.3 has full Meadows leverage annotation; §E Laws annotated with [Meadows-L2] and [Meadows-L5] | — | ALREADY APPLIED | §D.3, §E Laws annotations | n/a — confirmed |
| 20 | Systems Thinking Cybernetics | Ashby requisite variety — overflow mechanism | §I.2 `[new]` overflow token + lint-signal-13 | — | ALREADY APPLIED | §I.2 overflow token | n/a — confirmed |
| 21 | Systems Thinking Cybernetics | Beer VSM S1 placement | Systems-expert cell confirms Part 1 as VSM System 1 (primary activity). Not further applied in Part 1 itself — this is Part 4/8 territory | No concrete improvement for Part 1 body; Part 1's role as VSM S1 is a dependency graph claim owned by Part 4 | NO | Domain-orthogonal to Part 1's scope; VSM topology is Part 4 architecture | n/a |
| 22 | Anthropic Constitutional AI | Provenance + transparency — every artefact human-inspectable (Bai 2022 §3) | §E Law L-6 has UTF-8/plain-text + constitutional AI cite. Gap: §A inputs did not have explicit CAI-grounded provenance requirement with reasoning chain | Add explicit CAI transparency requirement to §A with reasoning chain: "every committed file must be human-inspectable per the party-bearing-consequences principle" | YES | Gap confirmed in §A inputs; L-6 in §E is the Law but §A lacked the motivating reasoning | §A — added constitutional provenance requirement paragraph |
| 23 | Anthropic Constitutional AI | Hardcoded never-list (Model Spec S4) | §E Law L-5 declares never-list (no-amend, no-no-verify, no-force-push). §F explicitly scopes anti-scope. This is structurally the same as CAI's hardcoded never-list pattern | — | ALREADY APPLIED | §E Law L-5, §F.2 anti-scope | n/a — confirmed |
| 24 | Anthropic Constitutional AI | RLAIF self-critique applied to lint (Bai 2022 §3 method) | Pre-registered as potential adoption: "§H concrete consequence: `/lint --check-commit-format` first runs RLAIF-style self-critique." Assessment: applying RLAIF to commit-format lint is premature optimization for Phase A. The lint check is a regex + token-list lookup — it does not benefit from self-critique. RLAIF applies to subjective harmlessness evaluation, not to deterministic format checking | NO | Premature optimization — RLAIF self-critique adds latency/cost with zero benefit for deterministic format checking. Phase B if lint expands to subjective quality evaluation (e.g., "is the `(why)` clause informative?") | n/a |
| 25 | Stoic Epistemic | Dichotomy of control — Laws govern only what IS in our control | §F anti-scope lists what Part 1 does NOT do, but the deeper principle — that Laws ONLY apply to controllable elements, while §K covers uncontrollable failures — was not explicitly stated | Add §F.3 Stoic Dichotomy of Control section explicitly demarcating "in our control" (Laws apply) vs "not in our control" (§K failure modes) | YES | Application Gap confirmed; Phase A justified — this is the conceptual foundation for why Laws L-1/L-6 exist and why §K exists | §F — added §F.3 Stoic Dichotomy section |
| 26 | Stoic Epistemic | Popper falsifiability on Foundation claims | §L acceptance predicates are Hamel-binary (falsifiable). §G R-tags have refutation conditions. This is Popper applied structurally | — | ALREADY APPLIED | §L acceptance predicates, §G R-tags | n/a — confirmed |
| 27 | Compounding Engineering | Every cycle compounds — git log value is superlinear | §0 mentions compounding via "71,820 commits over 10-year horizon" arithmetic. Gap: no explicit claim that aggregation over structured commit history is superlinear in informational value | Add explicit superlinear claim with worked query example to §J | YES | Application Gap confirmed; deepens §0's commitment-horizon arithmetic with the mechanism explanation | §J — added "Every commit compounds" ritual entry |
| 28 | Compounding Engineering | DRR compound step — postmortem becomes strategies.md entry | §J "Blameless postmortem ritual" already states "each postmortem is a strategies.md entry." | — | ALREADY APPLIED | §J postmortem ritual | n/a — confirmed |
| 29 | Compounding Engineering | Reversibility via git (P7) | §C.5 "git revert is the only undo" is Compounding Engineering P7 exactly — compound mistakes are revertable | — | ALREADY APPLIED | §C.5 Reversal Transactions | n/a — confirmed |
| 30 | Knowledge Management Karpathy-Luhmann-Matuschak | Evergreen notes — updated in-place, never replaced | §J mentions "blameless postmortem ritual" but not the evergreen-note discipline for the architecture document itself. Gap: no statement that this document IS an evergreen note updated via new commits | Add evergreen-note discipline statement to §J | YES | Application Gap confirmed; self-exemplification: this doc models what it specifies | §J — added evergreen note discipline block |
| 31 | Knowledge Management Karpathy-Luhmann-Matuschak | Karpathy LLM wiki — persistent compounding artefact | §0 frames git as compounding audit substrate. The KB/wiki is mentioned. Direct application to Part 1: structured frontmatter on all committed artefacts is the high-cardinality observability substrate | ALREADY APPLIED | §A requires YAML frontmatter on committed artefacts; §B §B.2 git_commit_hash frozen field supports KB provenance | n/a — confirmed |
| 32 | Multi-Agent Architecture | Orchestrator + specialist split (hub-and-spoke) | Part 1 is not an agent coordination document; this framework's primary application is Part 4. No concrete improvement for Part 1 body | NO | Domain-orthogonal to Part 1's substrate scope; orchestrator/specialist topology is Part 4 architecture territory | n/a |
| 33 | Product Management Cagan Shape Up | Appetite framing — fixed-time variable-scope | §J declares "2 working days maximum" appetite. Present but the Shape Up vocabulary ("appetite is fixed; scope is variable") was not explicit | Add explicit Shape Up vocabulary to the appetite declaration | YES | Trivial but justified: makes the Shape Up principle legible vs generic time-boxing | §J — added "appetite is fixed; scope is variable" sentence |
| 34 | Mereology Typed Edges | 10 valid A.14 edge types as a reference table | §D used correct A.14 edges but lacked the lookup table that Wave C authors for other Parts need | Add 10-edge-type reference table to §D for consumption by all Foundation Part authors | YES | Application Gap: edges correct but lookup table absent — downstream authors have no canonical reference | §D — added 10-edge-type table |
| 35 | **Young 2010 library-direct** (raw/books-md/event-sourcing/young-cqrs-2010.md) | "There is no Delete" p.31 verbatim + Reversal Transactions | §C.1, §C.5, §E Law L-5: already cited with page number. Verified against library source — confirmed present | — | ALREADY APPLIED | §C.1, §C.5, §E L-5 — library-verified | n/a — confirmed |
| 36 | **Google SRE Book library-direct** (raw/books-md/sre/google-sre-book.md) | Four Golden Signals Ch.6 p.60 verbatim | §B.1 cited sre-observability.md card but not the primary source. Added primary citation. | Add primary SRE Book Ch.6 p.60 citation | YES | Library-direct verification applied — primary citation added | §B.1 |
| 37 | **Google SRE Book library-direct** | Blameless Postmortems Ch.15 pp.169-175 verbatim | §J had sre-observability.md citation only. Added primary SRE Book Ch.15 citation with verbatim quote. | Add primary SRE Book Ch.15 citation with verbatim quote | YES | Library-direct verification applied | §J |
| 38 | **SRE Workbook library-direct** (raw/books-md/sre/google-srewb-implementing-slos.md) | Burn-rate algebra (1×/6×/14.4×) §12 | Not present in draft at all | Add burn-rate table to §J with Phase A trigger thresholds for Part 1 repo health SLO | YES | Application Gap confirmed; library-direct source verified. Phase A justified as stub for Part 8 consumption | §J — added burn-rate table |
| 39 | **Bai 2022 CAI library-direct** (raw/books-md/anthropic/bai-2022-cai.md) | CAI §3 method: provenance + transparency | §E Law L-6 cited anthropic-constitutional-ai.md card. §A lacked motivating reasoning chain. | Add explicit CAI reasoning chain to §A | YES | Library-direct verification: Bai 2022 abstract confirms "only human oversight is provided through principles" — human-inspectability of every artefact is the structural implementation | §A |
| 40 | **Askell 2021 HHH library-direct** (raw/books-md/anthropic/askell-2021-hhh.md) | Honest limits + non-deception in agent outputs | HHH framework: Helpful/Harmless/Honest. Applied to Part 1: the offline guarantee (Law L-3) is the "Honest" constraint — `/company-status` must not silently include stale network-sourced data and present it as current-state. The halt-on-network-call discipline IS the HHH honest-limits operationalization. | ALREADY APPLIED via §E Law L-3 — halt on network call detected | ALREADY APPLIED | §E Law L-3, §K K4 | n/a — confirmed |

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
