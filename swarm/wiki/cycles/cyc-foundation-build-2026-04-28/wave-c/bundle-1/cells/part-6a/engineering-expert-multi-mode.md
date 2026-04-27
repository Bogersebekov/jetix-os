---
title: Part 6a — engineering-expert multi-mode cell
date: 2026-04-28
phase: C-1-cell
expert: engineering-expert
modes: [critic, clean-code, scalability]
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
part: 6a
F: F4
ClaimScope: "Holds for Part 6a (citation scanner + approval log architecture) within Jetix Foundation Phase A single-owner system. Unknown for Phase B multi-fork or multi-operator deployments."
R:
  refuted_if: "A canonically promoted Part 6a artefact achieves F-G-R compliance without routing scanner output through the /lint subcommand extension architecture declared here; OR the approval log is implemented as an in-place-mutable markdown table rather than JSONL with regenerated view."
  accepted_if: "Wave C materialises /lint --check-citations as a swarm/lib/ subcommand handler; approval log at swarm/approvals/log.jsonl (append-only JSONL) with generated markdown view; RLAIF enabled only on critic-gate runs not pre-commit; all three acceptance predicates below hold simultaneously."
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md lines 300-360
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/engineering-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/clean-code.md §4
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/event-sourcing-cqrs.md §3-§4
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md §4 P3
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md §3-§4
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md §H (swarm/lib/ ownership)
---

# Part 6a — Engineering-Expert Multi-Mode Analysis
## Citation Scanner + Approval Log Architecture

> **Read-order confirmation.** This cell read, in sequence: Part 6 interface card (133 lines, full) → wave-c-worklist lines 300-360 → engineering-expert pre-read §6 → clean-code consultant §4 → event-sourcing-cqrs §3+§4 → anthropic-constitutional-ai §4 P3 → sre-observability §3+§4 → Part 1 architecture §H. All reads completed before output produced. Non-consultation would be a defect per Layer 1 §7 read-order protocol.

---

## §1 Scope Declaration and Part 6a Boundary

Part 6a owns the **Provenance Officer** machinery: the automated citation scanner (`/lint --check-citations`) and the append-only approval log (`swarm/approvals/log.jsonl`). Part 6b owns the Human Gate: AWAITING-APPROVAL packet schema, blast-radius classifier, and stop-gate packet authoring.

The boundary is crisp: Part 6a is the **detection and recording** layer. Part 6b is the **decision and escalation** layer. Part 6a never writes a gate packet; Part 6b never runs citation regex. Any proposed design element that blurs this line is an AP-ENG-12 violation (missing scope declaration) and is flagged in §6 critic findings below.

**Foundation vs RUSLAN-LAYER.** Per Part 1 §X and IP-1 [src:part-1-system-state-persistence/architecture.md §H]:
- Foundation layer: scanner algorithm contracts, JSONL log schema, F-G-R field presence rules, CLI subcommand interface signature.
- RUSLAN-LAYER: specific canonical wiki paths being scanned, RLAIF model endpoint, approval log physical path binding, threshold calibration values.

This separation is load-bearing: a Phase B fork operator must be able to adopt Part 6a's scanner without inheriting Jetix-specific path assumptions.

---

## §2 Citation Scanner Architecture (Critic Mode + Clean-Code Mode)

### §2.1 Ousterhout Deep-Module Test

The scanner's public interface must be narrow. [src:clean-code.md §4 P1 "The best modules are those whose interfaces are much simpler than their implementations"]

**Declared public interface:**

```
/lint --check-citations [<path>]
  Returns:
    exit 0   — zero citation flags
    exit N   — N citation flags found
    stderr   — structured report (one line per flag, machine-parseable)
    stdout   — human-readable summary (≤ 20 lines)
```

This is a one-verb, one-option, two-output interface. Internal complexity — regex matching, RLAIF optional pass, broken-citation resolution, F-G-R field parsing, cargo-cult detection — is fully hidden from callers. Callers (pre-commit hook, Part 8 health monitor, quarterly immune audit) interact only with exit code and structured stderr.

**Implementation-to-interface ratio (Ousterhout P1 check):**
- Interface lines: ~5 (CLI signature + exit code contract)
- Implementation lines: estimated 200-350 (four detection algorithms + RLAIF pass + file walking + report formatter)
- Ratio: ~50:1. Passes deep-module test. [src:clean-code.md §4 P1 deep-module check: "implementation-LoC >> interface-LoC"]

**What must NOT leak into the interface:**
- RLAIF prompt template text (internal implementation detail)
- Regex patterns (callers do not need to know how bare-claim detection works; they need the exit code)
- F-level thresholds (policy, not mechanism; RUSLAN-LAYER calibration)
- File walk order (irrelevant to callers)

### §2.2 Detection Algorithm Specifications

Four algorithms, each stateless and independently testable. This is the Unix "do one thing well" decomposition within the module. [src:clean-code.md §4 T1 resolution: "within a Part, the internal Unix-pipeline decomposition remains intact"]

**Algorithm A — Bare-claim detector.**

Stateless regex. Operates line-by-line on body text of any canonical markdown artefact.

Flag condition:
- Line ends with `.` (sentence terminator)
- Line contains at least one claim keyword: `must`, `will`, `is`, `has`, `requires`, `enforces`, `ensures`, `guarantees`, `never`, `always`
- No `[src:` token appears within the preceding 500-character window (sliding window over the byte stream, not line-count)

Produces flag: `BARE-CLAIM | file:line | "sentence text"`

False-positive risk: English prose naturally uses claim keywords in non-claim sentences ("Regular expressions are powerful"; "This section is an overview"). Mitigation: the 500-char `[src:` window check is generous enough to catch citations that precede a claim by one or two sentences. Residual false positives are surfaced to RLAIF optional pass (Algorithm D) before emission.

**Algorithm B — Cargo-cult detector.**

Stateless regex. Operates on any `[src:...]` citation token found in body text.

Flag condition:
- `[src:...]` token found
- Within the 200-character window AFTER the token: none of the consequence-verb tokens present (`therefore`, `so`, `thus`, `hence`, `this means`, `applies as`, `requires`, `must`, `MUST`, `enforces`, `consequently`, `which means`)
- AND none of the operational-change keywords present (`anti-scope`, `lint flag`, `gate`, `halt`, `BLOCKED`, `escalate`)

Produces flag: `CARGO-CULT | file:line | "[src:...]" → missing consequence`

**Why 200 chars, not a full sentence?** A citation that appears mid-paragraph with its consequence in the same sentence is captured. A citation where the consequence is two full sentences later is an authoring smell regardless — the connection should be made explicit. This is the constitutional discipline: citation + consequence within 200 chars is the declared standard per the mission brief. [src:anthropic-constitutional-ai.md §4 P6 transparency: "only human oversight is provided through principles" — consequence makes the principle operational]

**Algorithm C — Broken-citation detector.**

Operates on every `[src:path:anchor]` token.

Step 1: parse `path` component. Check `os.path.exists(repo_root + "/" + path)`. If false: flag `BROKEN-PATH | file:line | "path not found: <path>"`.

Step 2: if path exists, parse `anchor` component (if present). Grep file at `path` for `^## <anchor>` or `^### <anchor>` regex (ATX header match). If no match: flag `BROKEN-ANCHOR | file:line | "anchor '## <anchor>' not found in <path>"`.

Step 3: if no anchor present in the citation token — no flag. Bare-path citations (`[src:path]`) are valid; broken-anchor detection only fires when an anchor is declared.

**Critical edge case — path rename.** When a canonical file is renamed via `git mv`, all citations to the old path break silently. Algorithm C detects this at lint time but not at commit time. The pre-commit hook for Part 1 (`pre-commit-format.sh`) is commit-format only; it does not resolve citations. This creates a latent fragility: a rename that breaks 50 citations passes all pre-commit checks and is only detected at the next `/lint --check-citations` run.

**Recommended mitigation (engineering position):** Add a git `post-rewrite` hook that runs `Algorithm C` on any commit touching files with path renames. This hook fires after `git mv` + commit. It produces a non-blocking warning listing all citations that now resolve to broken paths. The warning is logged to `swarm/logs/lint-events.jsonl` (append-only, per Part 1 §J operational discipline). Blocking is not recommended — it would prevent legitimate renames when the author intends to update citations in a follow-up commit. Log-only is the Phase A default; blocking is Phase B option.

**Algorithm D — RLAIF self-critique (optional pass).**

Applies only to pending flags from Algorithms A and B (not C, which is deterministic).

For each flagged sentence:
1. Construct prompt: `"Does the following sentence have a concrete operational consequence that a system or agent could act on? Answer YES or NO with a one-sentence justification.\n\nSentence: <flagged text>"`
2. Call internal RLAIF evaluator (details are RUSLAN-LAYER — model endpoint is not named in this Foundation-layer spec per §1a security discipline)
3. If RLAIF returns YES: suppress the flag (it has an operational consequence even without explicit `[src:]` or consequence verb)
4. If RLAIF returns NO: emit the flag

**Expected false-positive reduction: ~30%.** [src:anthropic-constitutional-ai.md §4 P1 "RLAIF self-critique loop enables scalable harmlessness feedback": Bai 2022 §3 demonstrated false-positive reduction via self-critique]

This is an important calibration point: RLAIF does NOT replace human judgment (the Part 6b gate remains the terminal decision authority per E Laws "Human ack is TERMINAL"). RLAIF is a pre-filter that reduces noise before the lint report reaches the author and before the quarterly audit surfaces flags to Part 8. [src:anthropic-constitutional-ai.md §5 T3 "self-critique applies at generation-time; it is a quality filter, not final authority"]

### §2.3 swarm/lib/ Ownership Integration (C1 Contradiction Resolution)

**This is the critical architectural decision for Part 6a.**

Part 1 §H establishes the ownership contract verbatim: `/company-status`, `/knowledge-diff`, and `/lint` are owned by `swarm/lib/` shared infra, NOT by Part 1 directly. [src:part-1-system-state-persistence/architecture.md §H "Ownership note. /lint [...] owned by swarm/lib/ shared infra"]

This ownership contract extends directly to `/lint --check-citations`. The scanner is NOT a new Part 6a-owned skill. It is an EXTENSION of the existing `swarm/lib/`-owned `/lint` skill.

**Architectural realisation:**

```
swarm/lib/lint.sh                         # existing, swarm/lib/ owned
  case "$1" in
    --check-fg-r)      source swarm/lib/lint-check-fg-r.sh ;;        # Part 6a F-G-R scanner
    --check-citations) source swarm/lib/lint-check-citations.sh ;;   # Part 6a citation scanner
    --check-stage-gates) source swarm/lib/lint-check-stage-gates.sh ;; # existing
    --check-commit-format) source swarm/lib/lint-check-commit-format.sh ;; # Part 1 P1.2
    --all)             # runs all subcommands in sequence
  esac
```

`swarm/lib/lint-check-citations.sh` is the Part 6a deliverable. It contains:
- Imports of Algorithms A, B, C (as shell functions or Python module calls)
- RLAIF pass gate (conditional on `RLAIF_ENABLED=1` env var; default off)
- Structured stderr report formatter (one line per flag: `TYPE | file:line | evidence`)
- Exit code computation (`exit $(flag_count)`)
- F-G-R schema reference for reporting which F-level claims triggered cargo-cult flags

**Why subcommand handler, not standalone script?** DRY principle applied at skill level. [src:clean-code.md §4 P3 "EVERY PIECE OF KNOWLEDGE MUST HAVE A SINGLE, UNAMBIGUOUS, AUTHORITATIVE REPRESENTATION"] A standalone `/check-citations` script would duplicate: file-walk logic, report formatting, exit-code conventions, and the pre-commit hook integration. All of these are already present in `swarm/lib/lint.sh`. The subcommand pattern inherits them without duplication.

**Write-scope for this expert.** Per `write_scope_glob` in this expert's frontmatter: writes land in `swarm/wiki/drafts/<task-id>-engineering-<mode>-<slug>.md`. The design above is a PROPOSAL. The implementation of `swarm/lib/lint-check-citations.sh` is the brigadier-promoted canonical artefact — this expert cannot write it directly.

### §2.4 Performance and Scalability

Scan latency analysis at current and projected scale:

| Scale point | Wiki entries | Citations/entry | Total citations | Regex-only latency | RLAIF latency |
|---|---|---|---|---|---|
| Phase A (now) | ~552 entities | ~10 | ~5,500 | ~275ms (50ms/file avg) | Disabled |
| Wave C materialised | ~600 canonical | ~20 | ~12,000 | ~600ms | If enabled: ~100min |
| €200K horizon | ~1,000 canonical | ~25 | ~25,000 | ~1.25s | ~208min — prohibited |
| €1M horizon | ~5,000 canonical | ~30 | ~150,000 | ~7.5s | — |

Key findings:

1. **Regex-only scan is always fast enough for pre-commit.** Even at €1M scale (~150K citations), a 7.5-second pre-commit scan is acceptable. Git pre-commit hooks with a 10-second timeout are standard. This is not a scalability constraint.

2. **RLAIF must be disabled on pre-commit hooks.** At current scale (5,500 citations), RLAIF would add ~46 minutes to every commit. This is a hard usability failure. RLAIF is a critic-gate-only tool: enabled when `/lint --check-citations --rlaif` is invoked explicitly (quarterly immune audit, or per-cycle critic-gate pass), never enabled in the pre-commit path.

3. **F: F4 | ClaimScope: Phase A regex performance claim | R: refuted_if scan latency exceeds 2× projections above under actual file-walk timing on the production server. Accepted_if: three consecutive `/lint --check-citations` runs complete under projected ceiling.**

### §2.5 Failure Modes (Critic Mode)

| Failure mode | Detection | Response |
|---|---|---|
| Regex false-positive on legitimate prose | Human author receives spurious flag; RLAIF (critic-gate only) suppresses ~30% | Log RLAIF suppression rate; if >50% suppression, recalibrate regex claim-keyword list. Fail-loud criterion: zero false-positives in production must be the acceptance predicate, not "acceptable level". [src:sre-observability.md §4 P6 "silent failures = worst category of bug"] |
| Path rename breaks citations silently | Algorithm C catches at next lint run | `post-rewrite` hook (see §2.2) logs broken citations immediately post-rename; non-blocking warning |
| Anchor heading renamed (silent break) | Algorithm C catches at next lint run | Same as path rename. Anchor renames require contributor discipline: rename heading → run `/lint --check-citations` → fix citations before committing |
| RLAIF cost explosion (accidentally enabled in CI) | CI build time explosion from seconds to hours | `RLAIF_ENABLED=1` must be env-var gated; default OFF; CI must never set this var; accepted_if: three CI runs with RLAIF_ENABLED absent complete under 30s each |
| F-G-R schema evolution breaks old citations | Old citations reference F-level values no longer in schema | Schema version field in every canonical artefact's frontmatter (per event-sourcing upcasting principle). [src:event-sourcing-cqrs.md §4 Principle 4 "Events are immutable but schemas evolve"] When F-level enum changes, old artefacts carry their prior F-value; scanner reads schema_version to apply correct validation rules |
| Scanner produces empty report on syntax error | Bug in shell script causes silent pass | Fail-loud requirement: if the scanner exits 0 but produced zero output lines, this is a scanner health failure, not a clean scan. Acceptance predicate: scanner must emit at least one status line on every run (e.g., `STATUS: scanned N files, M citations, K flags`) [src:sre-observability.md §4 P6] |

---

## §3 Approval Log Structure (Critic Mode + Event-Sourcing Lens)

### §3.1 Format Decision: JSONL is the Primary Record

**Decision: `swarm/approvals/log.jsonl` (append-only JSONL) is the source of truth. `swarm/approvals/log.md` is a derived view, regenerated from JSONL.**

**Rationale:**

1. **Append-only semantics are natural in JSONL.** Each approval event is one JSON object per line. `echo '{...}' >> swarm/approvals/log.jsonl` is the write operation. No file parsing required on write — sequential append is the cheapest possible write. This matches Young's event-log property: "append-only architectures distribute more easily than updating architectures because there are far fewer locks to deal with." [src:event-sourcing-cqrs.md §3 Source 2 p.31]

2. **Machine-parseability without regex.** `jq 'select(.gate_class == "stop_gate")' log.jsonl` is reliable. Parsing markdown tables with regex is fragile (column count variation, header encoding, whitespace). For a system that queries approvals programmatically (quarterly audit, `/approvals --filter` CLI, Part 8 health monitor), JSONL is the correct primary format.

3. **Human-readability via derived view.** The `log.md` is generated by `/audit --regen-log` from JSONL. The markdown table is the human-facing view; it is NOT the authoritative record. This is the CQRS read/write split applied at the file level: JSONL is the write model (event log); markdown is the read model (derived projection). [src:event-sourcing-cqrs.md §4 Principle 2 "The write path is normalized for correctness; the read path is denormalized for query performance"]

4. **Scalability.** JSONL scales to millions of lines without structural change. At 10K entries, a grep/jq query over JSONL is sub-second. A markdown table with 10K rows is visually unusable and grep-slow. [This addresses the mission brief §Scalability mode point directly.]

**Alternative rejected: CSV.** CSV is machine-parseable but loses nested structure (F-G-R snapshot at gate time is an object, not a flat row; forcing it flat loses information). CSV also lacks schema self-description. Rejected.

**Alternative rejected: single markdown file (primary record).** Markdown tables are human-readable but not append-only by nature (editing a table row = in-place mutation). Using markdown as the primary record would require file locking, conflict resolution, and per-row parsing — all unnecessary overhead that JSONL eliminates. Rejected per Young 2010 append-only principle and per Hunt-Thomas DRY (the table parser would duplicate logic that `jq` already provides). [src:clean-code.md §4 P3 DRY]

### §3.2 Log Entry Schema

Each JSONL entry is a JSON object on one line. Schema (Foundation-layer; RUSLAN-LAYER values are not hardcoded):

```json
{
  "entry_id": "appr-YYYYMMDD-NNN",
  "entry_type": "gate_ack | gate_rejection | correction | audit_event",
  "schema_version": "1.0.0",
  "timestamp_utc": "<ISO-8601>",
  "gate_class": "stop_gate | approval_gate | foundation_revision | phase_b_activation",
  "artefact_path": "<repo-rooted path of the artefact gated>",
  "artefact_f_level": "<F0-F9 at gate time>",
  "artefact_g_scope": "<ClaimScope at gate time>",
  "artefact_r": "<R.accepted_if value at gate time>",
  "acked_by": "ruslan",
  "acked_at": "<ISO-8601>",
  "gate_packet_path": "<swarm/awaiting-approval/<filename>>",
  "corrects": null,
  "notes": "<optional free text, ≤200 chars>"
}
```

**Key design decisions:**

- `entry_id` follows `msg-YYYYMMDD-NNN` convention from CLAUDE.md, adapted to `appr-` prefix for approval log disambiguation.
- `schema_version` field per event-sourcing upcasting requirement. [src:event-sourcing-cqrs.md §4 Principle 4] When schema evolves, old entries remain parseable by declaring their schema version. Schema changes increment this field and add a changelog entry to `swarm/approvals/schema-version-history.yaml`.
- `corrects` field: when an entry corrects a prior entry (errata), set `corrects: "appr-YYYYMMDD-NNN"`. Prior entry is NEVER edited. This is Young's Reversal Transactions pattern applied directly. [src:event-sourcing-cqrs.md §3 Source 2 p.31 "There is no Delete"; Reversal Transactions]
- `artefact_f_level`, `artefact_g_scope`, `artefact_r` snapshot the F-G-R state AT GATE TIME. This is critical: the F-level may change after promotion (e.g., if the claim receives more citations and matures from F4 to F5). The log records what was acked, not what exists now. This is the audit-trail-as-event-log property: "we can use the event log to determine how we got to the state." [src:event-sourcing-cqrs.md §3 Source 3 Fowler "determine how we got to that state"]
- `gate_class` is from the blast-radius / gate-class taxonomy. The approval log records gate class so that quarterly audits can filter by class (how many stop-gate events per quarter, how many foundation-revision events, etc.)

**Correction entry discipline (Reversal Transaction example):**

If `appr-20260428-001` recorded the wrong `artefact_path`, the correction is:

```json
{"entry_id":"appr-20260428-002","entry_type":"correction","corrects":"appr-20260428-001","notes":"artefact_path was wrong in prior entry; correct path is swarm/wiki/foundations/part-6a/...",...}
```

Entry `appr-20260428-001` is never touched. The audit query for "what was the correct path?" is: find the correction chain and take the most recent non-overridden value. [src:event-sourcing-cqrs.md §4 Principle 1 "git revert creates a compensating event rather than mutating history"]

### §3.3 Idempotency Gate

Per event-sourcing Principle 3: "The stage-gate mechanism MUST be idempotent: if a human acks the same AWAITING-APPROVAL packet twice, the second ack must be a no-op." [src:event-sourcing-cqrs.md §4 Principle 3]

Implementation: before appending a gate_ack entry, `/audit --append-ack` checks whether `log.jsonl` already contains an entry with matching `gate_packet_path` AND `entry_type: gate_ack`. If found: return "already acked; no new entry written." If not found: append new entry.

The idempotency key is `gate_packet_path + entry_type`. This prevents duplicate ack entries from double-clicking, re-running `/audit`, or automated re-invocation.

### §3.4 Query Interface

The `/approvals` CLI (Part 6a deliverable) is a read-model query over `log.jsonl`. It regenerates or filters the markdown view:

```
/approvals --filter gate_class=stop_gate --since 2026-01-01
/approvals --regen-log
/approvals --entry appr-20260428-001
```

The `/approvals --regen-log` command rebuilds `swarm/approvals/log.md` from `log.jsonl`. This is the CQRS "rebuild projection" operation. [src:event-sourcing-cqrs.md §4 Principle 2 "projections can be discarded and rebuilt"] The markdown view is always reconstructable; the JSONL source is never discarded.

### §3.5 Does the Approval Log Accidentally Encode AWAITING-APPROVAL Packet Schema?

Critic finding: this boundary must be examined.

**Verdict: NO, but one field requires explicit boundary marking.**

The approval log records the OUTCOME of a gate event (acked, rejected, gate class, F-G-R snapshot at gate time, gate packet path). It does NOT encode the gate packet's internal structure (what the packet contains, the blast-radius classification algorithm, the decision criteria). The gate packet schema is Part 6b territory.

The `gate_packet_path` field in the log schema is a REFERENCE to the Part 6b artefact — a disk path, not an embedded copy of the packet's contents. This is the correct boundary: Part 6a records that a gate occurred and where the gate packet lives; Part 6b owns the gate packet schema and authoring.

**One exception to document:** The `gate_class` field in the approval log schema references a Part 6b concept (gate classification). This is a minimal necessary coupling: the approval log cannot be queried by gate type without knowing the gate class taxonomy. The coupling is one-directional (6a log references 6b taxonomy; 6b does not reference 6a log schema). This is an acceptable coupling, not a boundary violation. It should be documented as a typed A.14 edge: Part 6a `references` Part 6b blast-radius/gate-class taxonomy. [src:part-6-governance-provenance-human-gate.md §D Dependencies]

---

## §4 Quarterly Immune Audit Framework (Integrator Mode)

### §4.1 Audit Architecture

The quarterly immune audit is the Part 6a-owned periodic scan that consumes outputs of both the citation scanner and the approval log to produce a compliance report for Part 8.

**Audit triggers:**
- Calendar-driven (cron): quarterly boundary (January, April, July, October). Not event-driven. Rationale: deterministic cadence is easier to operationalise for a single-owner system. SRE Workbook recommends 4-week rolling window for SLO monitoring; quarterly is the outer boundary for audit (not continuous monitoring). [src:sre-observability.md §3 Source 5 "four-week rolling window to be a good general-purpose interval"]
- Event-driven exception: HITL can trigger an ad-hoc audit via `/audit --now` at any time. This does NOT replace the quarterly cadence; it supplements it when a drift signal is detected between regular cycles.

**Output:** `swarm/audits/Q<n>-<YYYY>.md` with required frontmatter:

```yaml
---
title: Quarterly Immune Audit Q2-2026
date: 2026-07-01
type: immune-audit
part: 6a
F: F4
ClaimScope: "All canonical artefacts at audit timestamp; Part 6a governance layer"
R:
  refuted_if: "Any canonical artefact promoted after audit date has F-G-R tags that contradict the compliance ratios reported here"
  accepted_if: "Part 8 health monitor consumes this report without surfacing contradictions"
---
```

### §4.2 Audit Dimensions — Concrete Checklists

Five dimensions, each with a measurable ratio and a declared SLO:

**D1 — F-G-R drift ratio.**
- Metric: `count(canonical without F-G-R frontmatter fields) / count(total canonical)`
- SLO: 0% (zero untagged canonical artefacts)
- Measurement: `/lint --check-fg-r` (Part 6a Bullet 1 from wave-c-worklist) run over all canonical paths. Already specified as a parallel Part 6a bullet.
- Behaviour change when SLO failed: halt canonical promotions until F-G-R coverage restored. [src:sre-observability.md §4 P7 "error budget behaviour change — not just fires alert"]

**D2 — Citation health ratio.**
- Metric: `count(broken citations) / count(total citations)`
- SLO: 0% (zero broken citations in canonical artefacts)
- Measurement: `/lint --check-citations --mode=broken-only` (Algorithm C only; fast, deterministic, no RLAIF needed)
- Behaviour change: surface broken citations list to author of each affected artefact via brigadier dispatch

**D3 — Cargo-cult drift time series.**
- Metric: `count(cargo-cult flags per cycle)` tracked as time series
- SLO: not a ratio target; a trend target — alert if count > 2× rolling 4-cycle average
- Measurement: `/lint --check-citations --mode=cargo-cult-only` (Algorithm B) per cycle; results appended to `shared/state/metrics/health-snapshots.jsonl` [src:sre-observability.md §4 P3 "metrics snapshot mechanism"]
- Behaviour change: if trend alert fires, dispatch `engineering × critic` on the artefacts contributing the highest cargo-cult count

**D4 — Dangling edges.**
- Metric: `count(edges in wiki/graph/edges.jsonl pointing to nonexistent canonical targets) / count(total edges)`
- SLO: 0% dangling edges
- Measurement: `/lint` existing dangling-edge check (signal already present per CLAUDE.md `/lint` skill description). The quarterly audit aggregates this signal.

**D5 — IP-1 violations.**
- Metric: `count(Foundation-tagged artefacts containing executor names) / count(Foundation-tagged artefacts)`
- SLO: 0% violations
- Measurement: grep over `swarm/wiki/foundations/` for known executor names (e.g., `brigadier`, `meta-agent`, `engineering-expert` as executor instances, not as role references). This check requires a curated executor-name registry — RUSLAN-LAYER concern. The Foundation-layer spec declares the check; the name list is RUSLAN-LAYER. [src:part-6-governance-provenance-human-gate.md §H "IP-1 enforcement is a Part 6 quarterly audit function"; FPF §5.1 IP-1]
- Behaviour change: surface violations as foundation-revision escalation; HITL ack required per §1d requires-approval

**F4 | ClaimScope: five audit dimensions hold for Jetix Phase A single-owner system; D5 IP-1 check requires RUSLAN-LAYER executor name list | R: refuted_if quarterly audit Q2-2026 cannot complete all five dimensions in under 30 minutes wall-clock time on the production server**

### §4.3 Part 8 Coordination Edge

The quarterly audit produces a compliance signal that Part 8 consumes. The edge type per A.14: `Part 8 methodologically-uses Part 6a audit framework`. [src:part-6-governance-provenance-human-gate.md §D "Part 6 ↔ Part 8 dual: constrained-by + methodologically-uses"]

Practically: the audit report at `swarm/audits/Q<n>-YYYY.md` is read by Part 8's health monitor. Part 8 incorporates the five dimension ratios into its SLI registry. Part 6a does NOT write to Part 8's SLI registry directly — it produces the audit report; Part 8 ingests it. This is the separation of detection (6a) from monitoring (8).

---

## §5 Scalability Mode

### §5.1 Approval Log at 10K Entries

**Question: Is markdown viable at 10K entries?**

**Answer: No for primary record; yes for derived view.**

At 10K entries, `log.md` rendered as a markdown table has 10K rows. This is:
- Visually unusable in any markdown viewer
- Grep-slow for full-text queries
- Unmaintainable as a hand-edited document

The JSONL primary record design (§3.1) resolves this completely. `log.jsonl` at 10K entries is ~10MB (1KB/entry typical). `jq` on a 10MB JSONL file is sub-second on any modern hardware. The markdown view is regenerated on demand via `/approvals --regen-log` and shows only the last N entries (configurable; default last 100) for human readability.

**F4 | ClaimScope: 10K entries on single-node system with jq available | R: refuted_if jq query over 10MB log.jsonl takes > 5 seconds on the production server (Ubuntu 22.04)**

### §5.2 Citation Scanner at 1,000 Wiki Entries × 30 Citations

Covered in §2.4. Headline: regex-only scan at this scale takes ~1.5s. Acceptable for pre-commit. RLAIF disabled = always safe.

At the €1M horizon where a managed team might introduce parallel wiki contributions, the scanner may need to run in parallel processes (one per wiki directory partition). This is a Phase B architecture concern; the Phase A single-threaded scanner is correct at current scale.

### §5.3 Phase B Fork Import and Approval Log Reconciliation

When Phase B activates a fork, the approval log faces a reconciliation problem: two parallel log.jsonl streams diverge at the fork point and must be reconciled when merging. This is the same problem addressed by `cross-fork-provenance.json` in Part 1. [src:part-1-system-state-persistence/architecture.md §I.1]

**Recommended approach (Phase B stub):** The `cross-fork-provenance.json` schema should declare an `approvals_reconciliation_strategy` field analogous to its existing `reconciliation_strategy` field. In Phase A: `reconciliation_strategy: deferred-phase-b` applies. In Phase B: the most conservative strategy is "merge-with-deduplication" — when merging fork approval logs, deduplicate by `gate_packet_path + entry_type + acked_at` (three-field key). Any genuine conflicts (same gate packet acked differently in parent and fork) are surfaced as HITL escalation.

This is registered as a Phase B HARD GAP requiring Ruslan ack before fork operations begin.

### §5.4 BOSC-A-T-X Horizon Analysis (Part 6a Specific)

| Gate | First-fire | MHT event | Engineering observable | Refactor % |
|---|---|---|---|---|
| €50K (current) | C+S = Composition + Scale | Phase Promotion: scanner moves from spec to operational (hooks active, JSONL log first written) | `swarm/approvals/log.jsonl` first entry appears; `/lint --check-citations` first returns structured stderr | ~5% |
| €200K | A = Agency (one reviewer added) | Phase Promotion: approval log gains second acked_by value (Ruslan + contractor) | `acked_by` field must support enum expansion; schema_version bump required | ~10% |
| €1M | O + C = Operation + Composition | Fission risk: citation scanner may need to handle multi-contributor wiki (concurrent writes, branch-based draft review) | Scanner must handle git-branch scoping (`--branch=<name>`) to scan in-progress drafts, not only main | ~25% |
| $100M | C + X = Composition + External | Role-Lift: IP-1 audit function becomes cross-team governance, not single-owner | Executor-name registry (D5) becomes multi-team registry; audit report format changes significantly | ~40% |
| $1T | X + T = External + Time | Context Reframe: approval log is regulatory compliance substrate, not just internal governance | GDPR / SOC2 audit trail requirements may impose external schema constraints on log entries | >30% — fragile |

**Antifragility check (10× gate per §6.4):**

- Scanner at 10×: regex O(n) on file size — 10× wiki entries → 10× scan time. Still under 15 seconds. Not fragile.
- Approval log at 10×: JSONL appends — 10× entries → 10× file size. jq queries scale linearly. Not fragile.
- F-G-R schema at 10×: enum expansion (more F-levels, more gate_class values) → schema_version bump required, tooling must implement upcasting. Potentially fragile if upcasting is not implemented before scale. Register as Phase B preparation item.
- IP-1 check at 10×: executor-name registry grows linearly with team size. At $100M (100+ contributors), maintaining the name list manually is prohibitive. Phase B: executor-name registry must be auto-derived from role manifest files, not hand-curated. This is the fragility trigger at $100M.

---

## §6 Critic Mode Findings

### §6.1 Conformance Checklist

| Check | Result | Evidence |
|---|---|---|
| 1. Deep-module (Ousterhout) | PASS | `/lint --check-citations` interface is narrow (5 lines); implementation is ~300 lines. Ratio ~60:1. |
| 2. Function-purpose | PASS (design) | Each algorithm (A/B/C/D) has a one-sentence purpose declared in §2.2. Implementation must carry purpose comments. |
| 3. Test-integrity | N/A (no diff under review) | — |
| 4. Premature-abstraction | PASS | No abstract "ProvenanceScanner" class proposed. Four concrete algorithms, each directly testable. Abstraction over them (a scanner pipeline object) is deferred until Phase B when needed. |
| 5. External-dep (RLAIF call) | FINDING-1 | RLAIF call site (Algorithm D) lacks explicit failure-mode declaration. See §6.2. |
| 6. DRY | PASS | JSONL is single source of truth; markdown is derived. Token lists in single-source JSON file. Area token DRY from Part 1 §I.2 pattern applied here. |
| 7. Tool-eval acceptance | N/A | This is an architecture proposal, not a tool-eval.md. |
| 8. Architecture pattern declaration | PASS | Orchestration pattern is explicitly named: swarm/lib/ subcommand extension (not a new owned skill). §2.3 declares and justifies. |

### §6.2 Specific Failures Found

**FINDING-1 — AP-ENG-10: RLAIF call site without failure-mode declaration.**

Algorithm D declares an RLAIF call but does not specify: timeout, retry policy, or fallback behaviour when the RLAIF evaluator is unavailable.

Consequence: if the RLAIF evaluator is unreachable (model endpoint down, context window exhausted, rate limit), Algorithm D has no declared behaviour. A silent failure here would mean cargo-cult flags are either all emitted (noise explosion) or all suppressed (silent corruption) depending on the failure mode's effect on the algorithm.

**Recommended fix:** Algorithm D must declare:
```
RLAIF call failure-mode:
  timeout: 5s per sentence
  retry: 1 (total 2 attempts, then fallback)
  fallback: emit the flag (conservative — surface rather than suppress when evaluator unavailable)
  failure_log: append to swarm/logs/lint-events.jsonl entry: {type: rlaif-failure, timestamp, sentence_hash}
```

The fallback "emit the flag" is the correct conservative choice: a false positive that reaches a human is recoverable; a false negative that silently suppresses a real cargo-cult citation is a provenance failure.

**FINDING-2 — Part 6a / Part 6b boundary — one field requires explicit marking.**

The `gate_class` field in the approval log schema couples Part 6a to Part 6b's gate-class taxonomy. This coupling is necessary (§3.5 verdict) but must be documented as an A.14 typed edge: `Part 6a approval-log references Part 6b gate-class taxonomy`. Without this edge declaration, the coupling is invisible to the dependency graph and future changes to the gate-class taxonomy may break approval-log queries silently.

**FINDING-3 — Scope creep risk: /lint --check-citations vs /lint --check-commit-format.**

The citation scanner scans for F-G-R field presence and citation consequence sentences. It does NOT scan for commit message format. These are different concerns: one is about artefact content quality (citations), the other is about process discipline (commit format). The two subcommands must share the file-walk infrastructure but must NOT share detection logic. A merged "check everything" subcommand would violate the deep-module principle by coupling two unrelated concerns behind one interface.

Verdict: scope creep risk is NOT present in the current design (§2.3 explicitly separates them as distinct subcommand handlers). Finding is a confirmation, not a new failure. Record it as a Watch item: any future proposal to merge `--check-citations` and `--check-commit-format` into a single subcommand is an AP-ENG-2 violation (shallow-module proliferation).

### §6.3 Anti-Scope

This engineering analysis does NOT:

- **Author the AWAITING-APPROVAL gate packet schema.** That is Part 6b territory. Part 6a records gate outcomes; Part 6b owns gate authoring.
- **Specify the blast-radius classifier algorithm.** That is Part 6b / OQ-MERGED-6 territory per wave-c-worklist Bullet 2.
- **Specify the RLAIF model endpoint or prompt templates at detail level.** Those are RUSLAN-LAYER. This analysis declares the RLAIF integration contract (what input/output the call produces) but not the provider, model name, or cost per call.
- **Author the Part 8 SLI registry.** Part 8 consumes the quarterly audit output; it owns the SLI schema. This analysis declares what signals Part 6a emits; Part 8 decides how to store and alert on them.
- **Evaluate the F-G-R level schema as a philosophical matter.** F-G-R definition is levenchuk-shsm-fpf territory and was authoritatively declared in prior waves. This analysis applies F-G-R tagging as specified; it does not critique the F-G-R schema.
- **Strategize about whether to adopt RLAIF at all.** That is a Method-level decision (HITL-only per §1d). This analysis names RLAIF as an optional component and declares its integration contract; the decision to activate it is Ruslan's.

---

## §7 Acceptance Predicates (Hamel-binary)

Three predicates, each independently falsifiable:

**AP-1 (Scanner architecture):**
`swarm/lib/lint-check-citations.sh exists AND bash -n clean AND exit-code-on-zero-flags = 0 AND exit-code-on-N-flags = N AND stderr contains one structured line per flag with format TYPE|file:line|evidence AND RLAIF_ENABLED defaults to 0 when env var absent`

**AP-2 (Approval log):**
`swarm/approvals/log.jsonl exists AND first entry is valid JSON with all required fields (entry_id, entry_type, schema_version, timestamp_utc, gate_class, artefact_path, acked_by, acked_at, gate_packet_path, corrects, notes) AND jq . log.jsonl exits 0 (no JSON parse errors) AND no prior entry has been edited (git log --follow log.jsonl shows only append commits)`

**AP-3 (Boundary against Part 6b):**
`swarm/lib/lint-check-citations.sh contains zero references to AWAITING-APPROVAL packet internal schema fields (artefact_under_review, blast_radius, escalation_routing) AND swarm/approvals/log.jsonl entries contain zero embedded copies of AWAITING-APPROVAL packet body content (only gate_packet_path reference)`

---

## §8 F-G-R Promoted Claims

| Claim | F | ClaimScope | R |
|---|---|---|---|
| JSONL is the correct primary format for the approval log | F4 | Single-owner Jetix Phase A; single-node file system | refuted_if: three consecutive `/approvals` queries over log.jsonl take >5s wall-clock; accepted_if: all query benchmarks complete under 1s |
| RLAIF must be disabled on pre-commit hooks | F5 | All deployments of the citation scanner where pre-commit hook latency matters (i.e. all interactive development workflows) | refuted_if: a pre-commit RLAIF call completes under 2 seconds for all citations in a single commit (would require new RLAIF model capability unavailable at time of writing); accepted_if: three pre-commit runs with RLAIF_ENABLED=1 each take >60s |
| The scanner is an extension of swarm/lib/ owned /lint, not a new Part 6a-owned skill | F5 | Holds as long as swarm/lib/ shared infra ownership contract from Part 1 §H remains in force | refuted_if: Part 1 §H ownership note is revised to remove /lint from swarm/lib/ scope; accepted_if: Part 1 architecture.md §H remains unchanged at next canonical review |
| Algorithm C (broken-citation) should have a post-rewrite git hook as mitigation for silent path-rename breakage | F3 | Holds for systems where git mv renames are common; Phase A Jetix has moderate rename frequency | refuted_if: no renames occur in 6 consecutive months of operation; accepted_if: at least one rename event occurs that would have broken a citation undetected without the hook |

---

## §9 Dissents and Open Questions

**Dissent-1 (self-dissent, engineering × critic vs engineering × integrator).**

The RLAIF optional pass (Algorithm D) creates a component dependency on a language model that is not version-controlled, not deterministically reproducible, and not available offline. The citation scanner's offline-first property (which makes it suitable for pre-commit hooks) is degraded by having RLAIF as even an optional component.

Counter-position (integrated): RLAIF is disabled by default and gated behind `RLAIF_ENABLED=1`. The pre-commit path NEVER enables it. The offline guarantee for the scanner's fast path is preserved. The RLAIF slow path (critic-gate only) explicitly accepts a network dependency in exchange for reduced false-positive noise. This is the same tradeoff resolution as Part 1's offline-first law for `/company-status`: the law applies to the default invocation, not to every conceivable invocation with non-default flags.

F3 | ClaimScope: this dissent holds if RLAIF is ever accidentally enabled in a pre-commit hook | R: refuted_if three consecutive CI runs with RLAIF_ENABLED absent complete under 30s each

**OQ-6A-1: `/lint --check-fg-r` vs `/lint --check-citations` — should these be one subcommand?**

Wave-c-worklist Bullet 1 specifies `/lint --check-fg-r` as a separate subcommand from `/lint --check-citations` (which this analysis designs). The F-G-R field presence check (do frontmatter fields F, ClaimScope, R exist?) is technically simpler than the citation content scan (does the body text have properly consequenced citations?). They operate on different layers: frontmatter vs body.

Engineering position: keep them separate. Merging them would violate the deep-module principle by coupling frontmatter structure checks with body content analysis behind one interface. Callers who need only the F-G-R presence check (Part 8 health monitor may only need this for a quick SLO snapshot) should not be forced to run the full citation scan.

**OQ-6A-2: Should the approval log entry include the full F-G-R snapshot or just the F-level?**

Current schema snapshots all three F-G-R fields (artefact_f_level, artefact_g_scope, artefact_r). This is complete but makes entries verbose. Alternative: snapshot only artefact_f_level (the scalar) and include a `artefact_canonical_path` reference where the full G/R are available.

Engineering position: keep all three. The approval log records state at gate time. If the artefact's ClaimScope or R changes after promotion (a legitimate evolution), the gate record should preserve what was acked — not what the artefact says now. Loss of G and R from the gate record loses the ability to audit "what was claimed to hold when this was acked." This matters for the quarterly immune audit. The verbosity cost is 2-3 extra JSON fields per entry; acceptable.

---

*End of Part 6a engineering-expert multi-mode analysis. Word count: approximately 4,200 words. Reads confirmed: 8/8 required sources consumed before output.*
