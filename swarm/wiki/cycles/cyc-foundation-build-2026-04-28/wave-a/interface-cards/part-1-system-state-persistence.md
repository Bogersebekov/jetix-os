---
title: Part 1 Interface Card — System State Persistence
date: 2026-04-27
phase: A-2
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
part: 1
part_title: System State Persistence
u_classification: U.System
fpf_anchor: "D25 Company-as-Code; FPF IP-3; FPF A.1 WF-A1-1"
F: F4
ClaimScope: "Holds for all Foundation Parts 1-10 in the Jetix Phase-A swarm. Does not govern RUSLAN-LAYER executor bindings or Notion-side display layer."
R: "Refuted if any Foundation part is shown to achieve durable canonical state WITHOUT routing through this part's git interface; accepted when all accepted artefacts carry git-commit provenance linking to this part."
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/engineering-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
---

# Part 1 Interface Card — System State Persistence

**Scope sentence.** The append-only, version-controlled ground-truth substrate on which every other Foundation part stores its committed state: git repository discipline, declarative YAML configuration, atomic commit format (`[area] verb what (why)`), reversibility primitives, and schema validation. [src:candidate-parts-merged.md:§2 Part 1]

---

## A. Inputs

What this part consumes. Each entry: `<source> :: <data-shape> :: <event-trigger>`.

- **All other Foundation parts (Parts 2-10):** committed file writes :: `git commit [area] verb what (why)` :: state-change event in any part
- **Part 6 (Governance, Provenance & Human Gate):** promotion instructions :: human-acked AWAITING-APPROVAL gate packet :: HITL ack received
- **CLAUDE.md / `.claude/config/*.yaml`:** declarative YAML configuration :: config-read :: system boot or skill invocation
- **`shared/schemas/*.json`:** JSON schema definitions :: schema-validation request :: pre-commit hook or lint pass [src:AUDIT §1.1; AUDIT §4.5]

---

## B. Outputs

What this part exposes. Each entry: `<consumer> :: <data-shape> :: <event-published>`.

- **All other Foundation parts:** durable committed artefact at a stable path :: `git log --oneline` queryable :: commit-completed event
- **Part 6 (Governance):** git history as audit trail :: append-only log :: provenance-query event
- **Part 8 (Health Monitoring):** repo integrity metrics (commit cadence, branch status, backup SLI) :: health signal :: periodic health-poll event
- **Part 9 (Owner Interaction Scaffold):** `/company-status` and `/knowledge-diff` snapshots :: markdown report :: owner-review event [src:engineering-expert.md:§2 Part 1; AUDIT §5.1]

---

## C. Side-effects

Per FPF IP-3 [FPF §5.3] and D25 [D25 Company-as-Code]: every state change produced by this part IS a git commit. There are no side-channel writes. Specific side-effects:

- **Append to git history:** every accepted write from any part becomes an immutable commit with `[area] verb what (why)` message format — never in-place mutation [FUNDAMENTAL §2.1 Three cross-cutting substrates]
- **Config resolution:** `.claude/config/*.yaml` is read at skill invocation; any change to config MUST be committed through this part before taking effect
- **Schema validation artefact:** pre-commit or lint pass writes no new file — validation is a gate check, not a file write; failures produce stderr only [src:engineering-expert.md:§3 D25]

---

## D. Dependencies (typed per FPF A.14)

Each edge: `<edge-type> <part-name>` — with rationale. [FPF §3.5 A.14; levenchuk-shsm-fpf.md:§4 P4]

- **No upstream part dependencies.** Part 1 is the substrate. Every other part calls its interface; it calls nothing back. This is the Unix-philosophy one-way data-flow property [engineering-expert.md:§1 "Clear contract boundaries"].

Downstream (other parts depend on Part 1):

- Parts 2-10 all carry an implicit `operates-in Part 1` edge — they operate within the git substrate. This is the `operates-in` A.14 edge type (not `ComponentOf` — the wiki content, methodology entries, etc. are separate entities that reside on Part 1's substrate; destroying the git repo would destroy their persistence but they are not constitutive parts of git). [levenchuk-shsm-fpf.md:§4 P4 "Part 3 operates-in Part 1"]
- Part 6 carries an additional `methodologically-uses Part 1` edge — governance artefacts (AWAITING-APPROVAL packets, LOCKED tags) are written through Part 1's commit interface as its primary enforcement mechanism. [candidate-parts-merged.md:§2 Part 6 D-Lock anchor]

---

## E. Boundary (per FPF A.6.B L/A/D/E)

[FPF §4.3 CP-3; levenchuk-shsm-fpf.md:§4 P6]

**Laws** (invariants MUST hold — violations are constitutional defects):
- Every canonical state change is a committed file in the git repository; no canonical state exists outside git [D25; FUNDAMENTAL §2.1]
- Commit messages MUST follow `[area] verb what (why)` format — legibility is a structural invariant, not a style preference [CLAUDE.md Global Rule 7; D25]
- Notion is a read-display layer only; it NEVER appears in this part's write path [D17; engineering-expert.md:§3 D17]
- No `--amend`, no `--no-verify`, no force-push on canonical branch — append-only is constitutional [FUNDAMENTAL §2.1; D25]

**Admissibility** (acceptance criteria for inputs to be committed):
- Input must carry a valid path under the repo root (no writes to `~/.ssh/`, `/etc/`, `.env*`, `private/`) [CLAUDE.md Global Rule 6]
- Input must pass schema validation where applicable (`shared/schemas/*.json`) before commit
- Input from Part 6 (promotion events) must carry a human-ack receipt in the AWAITING-APPROVAL packet frontmatter [FPF A.13 Agency-CHR; FUNDAMENTAL §4.2]

**Deontics** (obligations of this part toward consumers):
- This part MUST preserve every committed state indefinitely (append-only; no deletion without explicit HITL ack)
- This part MUST expose a queryable log (`git log`, `/knowledge-diff`) for any consumer requesting provenance reconstruction
- This part MUST provide reversibility via `git revert` (not `git reset`) so any canonical state can be undone safely [FUNDAMENTAL UC-H.3; D25]

**Effects** (measurable outcomes):
- After a successful commit: artefact is durable, path-addressable, and appears in `git log` within 1 second
- `/company-status` run: produces a ≤80-line snapshot with zero network calls [AUDIT §5.1 `/company-status`]
- Backup SLI: git repo integrity verifiable via `git fsck` — target: 0 object errors [FUNDAMENTAL §3 starter SLI values]

---

## F. Anti-scope (per FUNDAMENTAL §6)

Generic (applies to all Foundation parts):
- This part does NOT make strategic decisions [FUNDAMENTAL §6.1]
- This part does NOT substitute for founder agency [FUNDAMENTAL §6.2]
- This part does NOT use engagement-economy patterns, dark UX, or persuasion mechanics [FUNDAMENTAL §6.3]

Part-specific:
- This part does NOT enforce commit message content correctness (e.g., whether the commit message accurately describes the change) — that is Part 6 (Governance) responsibility via lint
- This part does NOT own the AWAITING-APPROVAL gate logic — it only executes the physical commit when Part 6 acks the promotion
- This part does NOT own Notion sync or any external-service write path — Notion is read-only display [D17]
- This part does NOT own schema authorship — schemas live in `shared/schemas/` and are authored through the normal Part 6 governance flow; Part 1 only validates against them

---

## G. F-G-R Tagging (per FPF B.3)

[FPF §4.2 CP-2; levenchuk-shsm-fpf.md:§4 P5]

| Artefact emitted | Formality (F0-F9) | ClaimScope (G) | Reliability (R) |
|---|---|---|---|
| Git commit + commit message | F5 — codified rule; `[area] verb what (why)` format enforced by convention + hook layer (cycle 2 log-only, moving to block in Phase B) | Holds for the Jetix mono-repo; unknown for multi-repo or distributed fork architecture | R-high — git commit is cryptographically checksummed; hash is the proof-of-existence |
| YAML config read result | F4 — operational convention; `.claude/config/*.yaml` is the declared source | Holds for skills invoked within the repo root; not applicable to external tool invocations | R-medium — config can drift if edited outside git (violation of Law invariant); mitigated by D25 enforcement |
| `/company-status` snapshot | F3 — multi-source informal; derives from `git log` + `ls` counts | Holds for the snapshot timestamp; may be stale within ≤1 hour in active sessions | R-medium — git-derived; accurate at invocation time |
| `git log` provenance chain | F6 — codified rule + ≥3 successful applications across 571 commits in 30 days [AUDIT §0 git-activity] | Holds for the entire repo history; fork audit trails are separate per D27 | R-high — immutable once committed; refuted only by repo corruption (git fsck detects) |

---

## H. Originating + critic-flagged

**Originating experts:**
- engineering-expert (Part 1: System Substrate) — primary proposal [engineering-expert.md:§2 Part 1]
- investor-expert — independently flagged D25 as "Lindy substrate" (most durable Foundation asset) [candidate-parts-merged.md:§2 Part 1 "Originating expert"]

**Critic flags applied from A-1 critic gate:**
- **NONE.** Part 1 was CLEAN on all IP-1/IP-2/IP-3/A.1/A.14/A.13/B.3/§6 checks. [A-1-critic-gate.md:§2 Part 1 "Verdict: CLEAN"]

**Note for A-2 interface card (from critic gate §2 Part 1 A.14 annotation):** The dependency edge from any other part to Part 1 is `operates-in` (content entities reside on the git substrate) or `methodologically-uses` (governance artefacts are written through Part 1's commit interface). The naive `creates` edge is incorrect here — Parts 2-10 create their own artefacts; Part 1 provides the substrate in which those artefacts persist. This distinction is applied above in §D. [A-1-critic-gate.md:§2 Part 1 A.14 note]
