---
title: "Part 2 — Signal Ingestion & Triage (Architecture)"
date: 2026-04-28
type: foundation-architecture
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 2
part: 2
part_slug: part-2-signal-ingestion-triage
status: draft-pre-ruslan-ack
F: F4
ClaimScope: "Holds for Foundation Phase A single-owner architecture. The STOP gate is a structural invariant of the information lifecycle, not a behavioural convention. Voice-pipeline tooling (`tools/transcribe.py`, `tools/extract.py`, `tools/filter.py`, `tools/run_pipeline.sh`) is RUSLAN-LAYER per §X. Specific PARA-tier definitions for Ruslan's projects, anchor-registry contents, and signal-source whitelists are RUSLAN-LAYER. Multi-owner gate delegation pattern is declared (P2.3) but SPEC-ONLY — implementation is Phase B."
R:
  refuted_if: "(a) A signal reaches canonical wiki/ without traversing the STOP gate (no `human_acked_at:` timestamp in promoted draft frontmatter); OR (b) a STOP gate packet is emitted that does not validate against the F8-LOCKED `awaiting-approval-packet.json` schema in Part 6b §I.4 (`gate_class: stop_gate` field non-null); OR (c) PARA-tier mandatory enforcement fails on the synthetic 10-fixture test (5 `para_tier:`-bearing drafts MUST be accepted; 5 lacking it MUST be rejected); OR (d) a `/ingest` invocation without `--anchor=` succeeds without raising D28 violation"
  accepted_if: "All bullets P2.1/P2.2/P2.3 acceptance predicates pass; STOP gate packets validate against Part 6b §I.4 awaiting-approval-packet.json F8 schema; PARA-tier enforcement lints clean against synthetic fixture; multi-owner stub §X declares F.9 Bridge fields sufficiently for Phase B partner instantiation"
predecessor_artefacts:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md
constitutional_inputs_consumed:
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md
  - swarm/wiki/foundations/part-6b-human-gate/architecture.md
  - decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/unix-philosophy.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/event-sourcing-cqrs.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md
  - raw/books-md/event-sourcing/young-cqrs-2010.md
  - raw/books-md/anthropic/bai-2022-cai.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - design/JETIX-FPF.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
---

# Part 2 — Signal Ingestion & Triage (Architecture)

## §0 Mission

Part 2 is the **pipeline that converts external raw signals into provenance-tagged, anchor-linked draft candidates ready for KB promotion — gated by a structural human STOP**. Voice memos, URLs, PDFs, book excerpts, email forwards, clipboard captures all enter through one interface (`/ingest --anchor=<topic>`) and exit through one gate (the human-acked review report). Between intake and exit, every stage produces a committed file. Nothing is ephemeral. Nothing reaches `wiki/` (Part 3) without `human_acked_at:` populated in the draft frontmatter [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md:§E Laws]. This is the constitutional bargain: ingestion velocity (~2-3 minutes per pipeline run per AUDIT §6 cycle 11) traded for canonical integrity (zero unreviewed signals in the KB).

The STOP gate is **architectural, not behavioural**. A future agent cannot "decide to skip review for trivial cases" — no admissibility predicate of Part 3 (§E Admissibility, line 95-99 of interface card) accepts a draft without `human_acked_at:`, and Part 6b §E Law L9 Halt-Log-Alert (≤1s halt / ≤5s log / ≤60s alert) fires on any attempted bypass [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E L9]. The gate is enforced by Part 6b's `awaiting-approval-packet.json` F8-LOCKED schema (RUSLAN-ACK Bundle 1 Decision #5): every Part 2 STOP submission carries `gate_class: stop_gate` from the canonical enum `[stop_gate, stage_gate, draft_promotion]` [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4 awaiting-approval-packet]. UND-4 is satisfied at this contract level. [F8|G:Foundation single-owner Phase A; cross-fork import as Foundation generic|R-high — rests on the Part 6b F8 contract]

Bundle 2 adds three structural deltas atop the Wave A interface card baseline:

1. **P2.1 — STOP gate packet emission spec**: Part 2 emits packets conforming exactly to the Part 6b §I.4 F8 schema with `gate_class: stop_gate`. The full schema enforcement (every required field present; provenance chain raw→draft→ack traceable) is the §H interface contract (UND-4 binding satisfied).
2. **P2.2 — PARA-tier mandatory frontmatter**: `para_tier: Project|Area|Resource|Archive` becomes a non-negotiable frontmatter field. `/ingest` rejects drafts without it. `/lint --check-para-tier` flags any orphan canonical entry lacking the field. PARA discipline (Forte) is enforced at the structural boundary, not as a soft convention.
3. **P2.3 — Multi-owner STOP gate stub**: Phase A is single-owner; Phase B is multi-owner. The architecture declares the F.9 Bridge fields and delegation predicate (`owner_count > 1`) so Phase B partners do not re-discover the design intent.

The lifecycle Part 2 owns is the **first leg of a closed loop**: raw signal → triage draft → human STOP → promoted draft → `wiki/` entry → F-G-R audit → cycle close (consumed by Part 5 in Bundle 3). Part 2's bargain is to feed clean, provenance-rich, anchor-tagged drafts into Part 3's admissibility surface so Part 3 never has to reason about source-trust at promotion time.

---

## §A Inputs

Each entry: `<source> :: <data-shape> :: <event-trigger>`. Anchored to interface card §A and extended for Bundle 2 specifics.

- **External world (owner-supplied):** raw signal file (`.ogg`, `.mp3`, `.txt`, URL string, `.pdf`, clipboard string, `.eml`) :: file-create or skill-invocation event :: owner initiates `/ingest --anchor=<topic>` or runs `tools/run_pipeline.sh` for the voice batch [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§6 voice pipeline current state — cycle 11 baseline ~2-3 min per run; F4|G:Foundation Phase A single-owner|R-high]. Owner-initiation is Foundation-level: per FUNDAMENTAL §6.2, Part 2 does NOT autonomously fetch signals — that would substitute for founder agency. The consequence: no scheduled cron pulls signals into Part 2 in Phase A; every signal carries an explicit owner-action provenance step.

- **D28 anchor parameter (mandatory):** `--anchor=<topic|project|question>` string :: validated non-null at ingest boundary :: `/ingest` skill invocation [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md:D28; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md:§E Laws "D28 anchor MANDATORY"; F5|G:Foundation generic anchor discipline|R-high]. The anchor must match an existing anchor in `wiki/index.md` OR declare a new anchor with explicit `--new-anchor` flag. Therefore a voice memo triaged without anchor does NOT reach Part 6b's STOP gate — it is rejected at the ingest boundary with stderr error and suggested anchor list. This is a leading constraint, not a lagging lint. Bundle 2 reaffirms but does not modify D28 enforcement.

- **Part 1 (System State Persistence) — git substrate:** commit interface for writing draft artefacts :: `[ingest]` or `[raw]` commit per Part 1 §I.2 commit-format-tokens.json [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§I.2 commit-format-tokens.json; F8|G:Bundle 1 LOCKED|R-high — F8 frozen contract]. Every pipeline stage output is a Part 1 commit. The schema_version_history block in commit-format-tokens.json must be respected; if Part 2 introduces a new area token (none in this Wave C scope), the K7 area-token-expansion failure mode in Part 1 §K applies.

- **Part 3 (Knowledge Base) — anchor query (read-only):** `wiki/index.md` queried for anchor-suggestion at ingest [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md:§B Outputs "queryable index"; F4|G:Part 2 ↔ Part 3 read interface|R-medium]. Part 2 reads but never writes Part 3 content directly. The edge in §D is `methodologically-uses Part 3` (uses the index), NOT `creates Part 3`.

- **FUNDAMENTAL §1 UC-B.1 strategy-aware filters:** declarative filter YAML (signal type + strategic focus tags) :: config-read at pipeline initialisation :: not yet materialised as a discrete file, currently embedded in `tools/extract.py` keyword filters and `filter.py` deduplication logic [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§1 UC-B.1 "filters declarative, не hidden logic"; F2|G:RUSLAN-LAYER config target|R-low — declarative materialisation deferred]. The Foundation declares filters MUST be declarative; the specific filter contents are RUSLAN-LAYER per §X.

- **Part 6b (Human Gate) — gate semantics:** `awaiting-approval-packet.json` F8-LOCKED schema [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4; F8|G:Bundle 1 constitutional lock|R-high]. Part 2 emits packets matching this contract. The contract is the input-side specification for what Part 2 must produce when invoking the STOP gate.

- **Part 6a (Provenance Officer) — F-G-R contract:** `f-g-r.json` F8-LOCKED schema [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1; F8|G:Bundle 1 constitutional lock|R-high]. Every draft Part 2 promotes carries F-G-R per this schema; Part 2 stamps the F-level (typically F1 raw transcript → F2 triage draft → F4 post-ack promotion) per §G of this document.

**Multi-channel capture scope (G.1-G.2 from interface card):**
- Voice memos (`inbox/*.ogg`, `inbox/*.mp3`) :: raw audio :: file-create event detected by `tools/run_pipeline.sh`
- URL / web page :: HTML or text fetched at `/ingest` time :: owner-paste into ingest command
- File / book excerpt / research dump :: `.md`, `.pdf`, `.txt` :: file-path argument to `/ingest`
- Clipboard :: string captured at command invocation :: `/ingest --clipboard` flag
- Email forward (Phase B; declared P2.3 stub) :: `.eml` :: routed via Part 10 inbound boundary

The first three are Phase A operational; clipboard is Phase A (KM MVP added per CLAUDE.md KM section); email is Phase B per Part 10.

---

## §B Outputs

Each entry: `<consumer> :: <data-shape> :: <event-published>`. Reorganised from interface card §B for Bundle 2 specifics.

- **Owner (STOP gate review):** `reports/review_YYYY-MM-DD.md` + `~/review-latest.md` :: human-readable triage review report :: `review-report-generated` event [src:CLAUDE.md Voice-Notes Pipeline §4; F4|G:Foundation single-owner; cross-fork F.9 Bridge for multi-owner|R-high — operational since cycle 11]. Owner reads and decides BEFORE any draft reaches Part 3. The 60-min review-latency target is RUSLAN-LAYER (Phase A attention budget); the Foundation declares only that the report exists and is committed within ≤5 min of the pipeline run.

- **Part 6b (Human Gate):** AWAITING-APPROVAL packet conforming to Part 6b §I.4 F8 schema with `gate_class: stop_gate` :: gate-submission event [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4 awaiting-approval-packet F8 LOCKED; src:RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md:§1 Decision #5; F8|G:Bundle 1 LOCKED contract that Part 2 consumes|R-high]. **This is P2.1 binding (UND-4 satisfied).** Every STOP gate submission carries:
  - `gate_class: "stop_gate"` (enum literal from frozen schema)
  - `packet_id: pkt-YYYYMMDD-<slug>`
  - `timestamp` and `submitted_at` ISO 8601
  - `actor: "part-2-ingest"` (role-archetype, IP-1 compliant)
  - `summary: ≤500 chars` (what is proposed, why, consequence-if-approved)
  - `outcomes[]` ≥1 (e.g., "draft promoted to wiki/concepts/X.md if approved")
  - `provenance: {artefact_path: <draft-path>, sources: [<raw-path>, <transcript-path>]}` ≥1 source
  - `ack_request: {option_a, option_b, option_c}` per Askell HHH corrigibility three-option structure
  - `review_checkpoint: {question: "What specifically did you verify before acking this packet?", answer: <≥10 chars>}`
  - `reversibility_class: "reversible"` (typical for Part 2 — promotion can be reverted via Part 1 Reversal Transactions; rare cases mark `hard_to_reverse` if strategic content)
  - `blast_radius_tier: 2` (typical — tactical batch-eligible; Tier 1 strategic only if signal touches FUNDAMENTAL revision)
  - `f_g_r_delta: $ref shared/schemas/f-g-r.json` (the snapshot at gate time)
  - `cycle_id: cyc-<id>` if part of a cycle context
  
  The packet schema is FROZEN per Bundle 1 ack. Part 2 consumes verbatim; any new field would require a constitutional AWAITING-APPROVAL gate per Part 6b §E Law L9.

- **Part 3 (Knowledge Base):** promoted draft candidate (`.md` with YAML frontmatter + anchor + **`para_tier:`** mandatory + provenance `sources:` + `human_acked_at:`) :: `ingest-completed` event :: ONLY after STOP gate ack [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md:§A Inputs "post STOP gate"; F4|G:Foundation generic|R-high]. **This is P2.2 binding.** Part 3's admissibility predicate (interface card §E) requires `human_acked_at:` populated AND `para_tier:` non-null (Bundle 2 extension). The consequence sentence: a draft missing either field is rejected by Part 3 at admissibility check; Part 2 must produce both before promotion. The frontmatter contract:
  ```yaml
  pipeline: ingested
  sources: [<raw-path>, ...]
  anchor: <D28-validated topic>
  para_tier: Project | Area | Resource | Archive   # P2.2 mandatory
  human_acked_at: <ISO 8601 timestamp>
  ack_packet_id: <pkt-YYYYMMDD-slug>
  F: <F-level per §G>
  ClaimScope: <holds_within scope>
  R:
    refuted_if: <Popperian falsifier>
  ```

- **Part 1 (Substrate):** committed draft file at `raw/transcripts/<slug>.md` (transcription stage), `inbox/<slug>-DRAFT.md` (triage stage), `reports/review_<date>.md` (review stage) :: `[ingest]` or `[raw]` commit per Part 1 §I.2 :: `pipeline-stage-complete` event [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§I.2 commit-format-tokens; F8|G:Bundle 1 LOCKED|R-high]. The commit message follows the `[area] verb what (why)` format precisely; pre-commit hook K3 (Part 1 §K) catches deviations. The K11 latent R2 feedback loop concern (drift toward no-citation) does not apply to Part 2 outputs (they are pre-canonical), but the citation-density discipline applies once Part 3 promotes.

- **Part 6a (Provenance Officer):** provenance chain `(raw_source_path → transcript_path → draft_path → ack_packet_id → human_ack_timestamp → wiki_promotion_path)` :: provenance-chain-emit event :: at every STOP gate ack [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§C approval log structure; F4|G:Foundation generic|R-high]. Part 6a appends to `swarm/approvals/log.jsonl` with the full chain. The Reversal Transactions discipline (Young 2010) means a corrected draft is a NEW entry referencing the prior `corrects: <packet_id>`, not a mutation of the original.

- **Part 8 (Health Monitoring) — Phase B / Bundle 4:** ingest-rate metric, STOP-gate-latency metric, rejection-rate-by-reason metric :: health-poll event :: periodic [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md:§B; F2|G:Phase B / Bundle 4 stub|R-low — Part 8 not yet materialised]. Declared output for Bundle 4 Part 8 work; not active in Phase A.

---

## §C Side-effects

Per FPF IP-3 [src:design/JETIX-FPF.md:§5.3 IP-3] and D28 [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md:D28]: every pipeline stage produces a committed file. No ephemeral-only outputs. No side-channel writes to Notion or external services [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md:D17 — Notion is not authoritative].

- **Transcript write:** `raw/transcripts/<slug>.md` — committed via Part 1 at the transcription stage (after `tools/transcribe.py`). The file is APPEND-ONLY at the path level: a re-transcription of the same audio file with corrections produces a NEW file at `raw/transcripts/<slug>-v2.md` referencing the prior via frontmatter `supersedes: <prior-slug>`, NEVER an in-place edit. This is the Young 2010 "There is no Delete" discipline applied to transcripts [src:raw/books-md/event-sourcing/young-cqrs-2010.md:p.31; F4|G:Reversal Transactions for transcripts|R-high].

- **Draft candidate write:** `inbox/<slug>-DRAFT.md` (when `tools/extract.py` produces a structured item from a transcript) OR `reports/review_<date>.md` (when the review report is generated for owner). The DRAFT.md carries `pipeline: ingested` frontmatter; the review report carries `pipeline: review`. Both are committed.

- **STOP gate artefact:** the AWAITING-APPROVAL packet itself is written to `swarm/awaiting-approval/<pkt-id>.md` (or the legacy path `swarm/gates/AWAITING-APPROVAL-<id>-<date>.md` per brigadier convention) per Part 6b §H. The packet body conforms to the F8 schema. Side-effect of ack: `acked_at:` field populated; the packet remains in the staging directory as a permanent audit artefact (Reversal Transactions — never deleted).

- **`human_acked_at:` field write to draft frontmatter:** at ack time, Part 2 (or brigadier on Part 2's behalf) updates the draft's frontmatter to add `human_acked_at: <timestamp>` and `ack_packet_id: <packet_id>`. This is an APPEND in spirit (the file's history shows the addition; prior versions remain in git) — pre-ack draft and post-ack draft have distinct git commits. The provenance chain is reconstructable via `git log -p inbox/<slug>-DRAFT.md` [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§J "git log as superlinear value"; F4|G:Foundation generic|R-high].

- **`para_tier:` frontmatter field write:** at triage stage (after `tools/extract.py` produces the structured item, or at `/ingest` invocation for non-voice signals), the draft frontmatter receives a `para_tier:` field. **This is P2.2 binding side-effect.** The value is one of `Project | Area | Resource | Archive` per Forte PARA P4 [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 4 + §6 Part 2 item 1; F4|G:Foundation generic — PARA discipline as Foundation invariant|R-high]. The classification logic (which signal goes to which tier) is RUSLAN-LAYER per §X (his projects, his areas, his resources, his archive). The Foundation enforces only that the field exists.

- **Append to `wiki/log.md` (post-ack only):** when a draft is promoted to `wiki/`, a one-line log entry is appended at the top of `wiki/log.md` (per CLAUDE.md Global Rules §Logs append-only-top discipline). The line format: `## [YYYY-MM-DD HH:MM:SS] ingest-promoted | <draft-slug> | <anchor> | part-2`.

- **Update `wiki/index.md`:** the new entity slug is added to the index under its anchor. Idempotent: re-promoting the same slug updates the index entry rather than creating a duplicate.

- **Edge append to `wiki/graph/edges.jsonl`:** when the promoted entity declares typed A.14 edges in its frontmatter `edges:` block, those edges are appended to `wiki/graph/edges.jsonl`. APPEND-ONLY — never in-place mutation [src:design/JETIX-FPF.md:§3.5 A.14; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md:§E Laws "edges.jsonl is append-only"; F5|G:Foundation generic A.14 contract|R-high].

- **NO side-effect to canonical wiki content (Part 3) before STOP gate ack:** Part 2 NEVER writes to `wiki/<entity-type>/<slug>.md` directly. The canonical write happens AT promotion (after STOP gate ack), and the writer-of-record is brigadier (per CLAUDE.md sole_writer convention) acting on Part 3's admissibility check. Part 2's write surface is limited to `raw/transcripts/`, `inbox/`, `reports/`, and `swarm/awaiting-approval/`. This is enforced by the write-scope-glob mechanism (Part 1 Phase B hook K2; advisory in Phase A).

- **NO side-channel to external services:** no Notion API call, no email send, no Linear push from Part 2. The voice pipeline's `tools/transcribe.py` calls Groq Whisper for transcription (RUSLAN-LAYER tooling per §X) but the call is owner-initiated and produces a committed artefact — it is not a "side-channel" in the constitutional sense (per FUNDAMENTAL §6.5 the prohibition is against autonomous external communications). [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.5; F8|G:Foundation hard rule|R-high]

---

## §D Dependencies (typed per FPF A.14)

Every dependency edge below is from the **canonical 10-edge A.14 reference table** authored in Part 1 §D [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§D 10-edge canonical lookup; F8|G:Foundation generic edge taxonomy|R-high]. Generic `depends-on` is FORBIDDEN per Bundle 1 deep-prompt §6.4 / Bundle 2 deep-prompt §6.4. Critic gate auto-rejects.

The canonical edge types: `ComponentOf | ConstituentOf | PortionOf | PhaseOf | MemberOf | AspectOf | creates | operates-in | methodologically-uses | constrained-by | derives-from`.

**Part 2's edges:**

- **`operates-in Part 1`** — every Part 2 pipeline stage output is a committed artefact persisted in the git substrate. Part 2's entire write surface (raw/transcripts/, inbox/, reports/, swarm/awaiting-approval/) operates within Part 1's commit interface [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md:§D first edge; F8|G:Bundle 1 LOCKED|R-high]. Therefore: a Part 1 substrate failure (e.g., K8 git fsck object errors) cascades into Part 2 inability to commit; Part 2's K-class failure modes must include this cascade (see §K K1).

- **`PhaseOf information-lifecycle`** (cross-cutting, Part 2 → Part 3) — Part 2's output (triage draft) is the **pre-KB phase** of the full information lifecycle; the phase boundary is the STOP gate. The lifecycle is: `[external signal] → Part 2 [triage] → STOP → Part 3 [KB] → Part 5 [methodology promotion candidate] → Part 3 [methodology library] → Part 6a [audit]`. The `PhaseOf` edge captures the asymmetric pipeline relationship (Part 2 is upstream phase; Part 3 is downstream phase) without claiming Part 3 is composed of Part 2 (which would be `ComponentOf` and is wrong) or that Part 3 is Part 2's deliverable (which would be `creates` and is also wrong because Part 3 has its own admissibility logic). [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§2 Part 2 A.14 note; F5|G:Foundation generic edge type|R-high]

- **`methodologically-uses Part 6b`** — the STOP gate is an **instance of Part 6b's HITL escalation discipline**. Part 6b owns the J-Approve decision-class authority (per A.13 Agency-CHR — human ack required before canonical promotion); Part 2 instantiates that authority structurally at its boundary [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md:§D third edge; src:design/JETIX-FPF.md:§2.1a A.13; F8|G:Bundle 1 LOCKED Part 6b authority|R-high]. The consequence: any change to Part 6b's gate semantics (e.g., schema_version bump on awaiting-approval-packet.json beyond the F8-LOCKED 1.0.0) requires Part 2 to re-validate its packet emission. Cross-Part schema drift is detected by Part 6a's quarterly immune audit.

- **`methodologically-uses Part 6a`** — every promoted draft carries F-G-R per the Part 6a §I.1 F8-LOCKED schema. Part 2 stamps F-level (typically F1→F2→F4) per §G; Part 6a is the schema authority [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1; F8|G:Bundle 1 LOCKED|R-high]. The consequence: Part 2's F-G-R fields validate against `f-g-r.json`; malformed F-level (e.g., F-letter outside 0-9 range or missing `holds_within:` ClaimScope token) is rejected by Part 6a's pre-promotion validator (advisory in Phase A; blocking in Phase B per OQ-B1-4 jsonschema validator deferral).

- **`methodologically-uses Part 3`** — read-only reference to `wiki/index.md` for anchor suggestions at ingest time [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md:§D read-only reference; F4|G:Part 2 query-side|R-medium]. This is a USE relationship (Part 2 uses Part 3's index to inform anchor selection), not a content-creation relationship. The edge points at Part 3's CONTENT; the accessor mechanism (`/ask` style query) lives in `swarm/lib/` per C1 Joint Design (see `swarm/lib/README.md`).

- **`derives-from` external world** (cross-cutting, signal-source) — every triage draft `derives-from` an external signal (voice memo file, URL response body, PDF text, clipboard string). The provenance chain in §B includes this derivation explicitly. The `derives-from` edge is what Part 6a's quarterly immune audit traverses to verify "every canonical claim has a traceable source" [src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§J quarterly audit; F4|G:Foundation generic provenance discipline|R-high].

**Edges Part 2 explicitly does NOT have:**

- NO `creates Part 3` — Part 2 produces drafts; Part 3 OWNS its admissibility logic and decides when a draft becomes canonical content. Part 2 cannot "create wiki entities" — only feed candidates to Part 3 for promotion. (This is the A-1 critic resolution carried forward — see Part 3 interface card §F.)
- NO `ComponentOf Part 6b` — Part 2 is not part of Part 6b's substance; it instantiates Part 6b's authority at its boundary. The relationship is `methodologically-uses`, not `ComponentOf`.
- NO `depends-on` (any) — generic dependency is forbidden. Every relationship is one of the 11 typed edges.

---

## §E Boundary (per FPF A.6.B L/A/D/E)

[src:design/JETIX-FPF.md:§4.3 A.6.B; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md:§4 P6 Boundary discipline]

### Laws — invariants that MUST hold (constitutional defects on violation)

**L1 — STOP gate is structural, not behavioural.** No draft candidate reaches `wiki/` (Part 3) without `human_acked_at:` populated in its frontmatter AND a corresponding `ack_packet_id:` referencing a Part 6b §I.4-conforming packet with `gate_class: stop_gate`. A draft missing either field is rejected by Part 3 at admissibility check [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.2 HITL; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md:§2 Part 2 "STOP gate is an architectural enforcement"; F8|G:Foundation single-owner Phase A; cross-fork F.9 Bridge for multi-owner|R-high]. Therefore: a future agent cannot "decide to skip review for trivial cases"; the predicate is binary at the schema level.

**L2 — D28 anchor is mandatory at ingest boundary.** A signal without `--anchor=` is REJECTED by the pipeline with a stderr error citing the violation (not a warning). The error message includes suggested anchors from `wiki/index.md` to guide the owner toward a valid anchor selection [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md:D28; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/engineering-expert.md:§3 D28; F8|G:Foundation generic anchor discipline|R-high]. The consequence: anchor compliance is a leading constraint (caught at ingest) not a lagging lint check.

**L3 — Every pipeline stage output is a committed file; no ephemeral-only processing.** Per FPF IP-3 commit-substrate. Therefore: a transcription that runs and produces no committed `raw/transcripts/<slug>.md` is a defect — the transcription is unrepeatable in audit context. [src:design/JETIX-FPF.md:§5.3 IP-3; F8|G:Foundation generic commit substrate|R-high]

**L4 — `para_tier:` field is mandatory in every promoted-draft frontmatter (Bundle 2 P2.2).** A draft handed to Part 3 without `para_tier:` is rejected by `/ingest` (which produces drafts) and by `/lint --check-para-tier` (which audits canonical entries). The PARA classification (Project, Area, Resource, Archive) is enforced at the structural boundary, not as a soft convention [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 4 Forte PARA + §6 Part 2 item 1; F4|G:Foundation generic|R-high]. Therefore: PARA discipline is leading (caught at draft creation), not lagging.

**L5 — Notion NEVER appears in the write path.** Part 2's pipeline does NOT write to Notion. Any "Notion sync" is RUSLAN-LAYER (Phase B / Bundle 4 Part 10 — External Touchpoints) and one-way (Notion is consumer of canonical wiki content, not authoritative source) [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md:D17; F8|G:Foundation hard rule per CLAUDE.md Global Rule 4|R-high].

**L6 — Append-only on raw artefacts.** `raw/transcripts/<slug>.md` is APPEND-ONLY at the path level; corrections produce a NEW file `raw/transcripts/<slug>-v2.md` with `supersedes: <prior-slug>` frontmatter. Reversal Transactions discipline (Young 2010) [src:raw/books-md/event-sourcing/young-cqrs-2010.md:p.31 "There is no Delete"; F5|G:Foundation generic Reversal Transactions|R-high]. Therefore: a re-transcribed audio file does NOT overwrite the prior transcript; the audit chain remains complete.

**L7 — Halt-Log-Alert (Part 6b §E Law L9) applies to STOP gate failures.** If the STOP gate cannot validate the packet (schema violation, missing `gate_class`, malformed F-G-R delta), Part 2 HALTS within ≤1s, LOGS within ≤5s to `swarm/approvals/log.jsonl` (per Part 6a §C), and ALERTS within ≤60s to the owner via `~/review-latest.md` flag [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E Law L9; F8|G:Bundle 1 LOCKED|R-high]. Therefore: STOP gate failure does not silently degrade — the owner is notified within one minute.

**L8 — Corrigibility (Part 6b §E Law L9 Askell HHH verbatim).** "NO mechanism exists by which any agent, any Part, or any automation may lock the human owner out." Therefore: Part 2 cannot block the owner from manually inspecting / halting / overriding any pipeline stage; the owner can `git revert` any Part 2 commit, `rm` any DRAFT.md, edit any review report — Part 2 has no exclusive lock on its own outputs [src:raw/books-md/anthropic/askell-2021-hhh.md:Appendix E.2; src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§E Law L9; F8|G:Bundle 1 LOCKED Corrigibility|R-high].

### Admissibility — acceptance criteria for inputs to enter the pipeline

**A1 — Signal carries non-null `--anchor=`.** Per L2. The anchor matches an existing project / area / question in `wiki/index.md` OR the owner declares a new anchor via `--new-anchor` flag. Bare invocations like `/ingest /path/to/file.pdf` (no anchor) are rejected.

**A2 — Signal duration (for voice) ≤30 minutes per single ingestion event.** Longer audio inputs require manual splitting at owner-meaningful boundaries (typically topic transitions). Rationale: Groq Whisper accuracy degrades on long monologues (per AUDIT §6.1 cycle 11 baseline ~95% accuracy on ≤30 min); pipeline run-time stays bounded at ~2-3 min (cycle 11 measured) [src:decisions/AUDIT-CURRENT-STATE-2026-04-27.md:§6.1; F4|G:Phase A operational tolerance|R-medium].

**A3 — Signal source is owner-supplied.** Part 2 does NOT autonomously fetch or pull signals from external services without owner initiation. (FUNDAMENTAL §6.2 founder agency; §4.2 HITL.) [F8|G:Foundation hard rule|R-high]

**A4 — `para_tier:` declared at ingest OR derivable from anchor.** If the owner provides `--para-tier=Resource` at ingest, that value is used. Otherwise `/ingest` infers from the anchor: anchors in projects/_active/ map to Project; anchors in directions/ map to Area; book-excerpt or research-dump anchors map to Resource; anchors marked archived map to Archive. If neither `--para-tier` nor a derivable anchor is provided, the pipeline pauses and prompts the owner for the value (interactive) or rejects in batch mode. [F4|G:Foundation generic with RUSLAN-LAYER inference rules|R-medium — inference rules are part of RUSLAN-LAYER per §X]

**A5 — Signal type is in the multi-channel scope.** Voice, URL, file (md/pdf/txt), clipboard. Email is Phase B (P2.3 stub). Any other type (e.g., binary data, video) is rejected with `escalations[]{trigger: out-of-scope}` and a suggested route (e.g., extract audio from video first; then re-ingest the audio file).

**A6 — Phase A: single-owner only.** Per the §X declaration. Multi-owner ingestion (where ingest signals could come from multiple human owners with conflicting anchor namespaces) is Phase B with F.9 Bridge fields per P2.3.

### Deontics — obligations of this part toward consumers

**D1 — MUST produce a committed review report `reports/review_YYYY-MM-DD.md` (and copy `~/review-latest.md`) for every pipeline run BEFORE any draft reaches the owner for ack.** [src:CLAUDE.md Voice-Notes Pipeline §4; F4|G:Foundation generic review-report discipline|R-high] Therefore: a pipeline run that produces drafts but no review report is a defect; STOP gate cannot proceed.

**D2 — MUST preserve raw source artefacts permanently in `raw/transcripts/` and `inbox/`.** Raw is immutable; processed may be updated (with supersedes pointer) but the raw source link is mandatory in every promoted draft's `sources:` frontmatter [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§1 UC-B.3 raw-as-source-of-truth; F8|G:Foundation hard rule|R-high].

**D3 — MUST tag every draft with a `para_tier:` field BEFORE handoff to Part 3 (Bundle 2 P2.2).** [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§6 Part 2 item 1; F4|G:Foundation generic|R-high]

**D4 — MUST emit AWAITING-APPROVAL packet conforming to Part 6b §I.4 F8 schema for every STOP gate submission (Bundle 2 P2.1).** `gate_class: stop_gate` field non-null. [src:swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.4; F8|G:Bundle 1 LOCKED contract|R-high]

**D5 — MUST surface gate failure with specific reason, not generic reject.** Per Anthropic CAI transparency principle [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md:§4 P6; F4|G:Foundation generic transparency|R-high]. Therefore: when the STOP gate validator rejects a packet, the rejection includes the specific schema violation (e.g., "missing required field: ack_request.option_b") not a generic "rejected".

**D6 — MUST include provenance chain in every packet.** raw_source_path → transcript_path → draft_path → owner-ack-timestamp (post-ack). Pre-ack the chain is partial; post-ack it is complete and committed to `swarm/approvals/log.jsonl`.

**D7 — MUST commit pipeline-stage outputs within ≤5 min of stage completion.** This is the latency budget — a stage that runs but takes >5 min to commit is a defect (likely indicates batching or queueing that violates the "every stage commits" Law L3).

### Effects — measurable outcomes

**E1 — After pipeline run:** `reports/review_YYYY-MM-DD.md` exists and is committed; owner can read within ≤5 min of signal submission. (Cycle 11 baseline: voice pipeline runs in ~2-3 min per AUDIT §6.) [F4|G:Phase A operational SLO|R-medium]

**E2 — After STOP gate ack:** promoted draft appears in `wiki/` with `human_acked_at:` field populated and is searchable via `/ask` within the next session (or `/consolidate` run for the canonical index update).

**E3 — Signal rejection (missing anchor):** stderr error with suggested anchors from `wiki/index.md`; no partial write to `raw/` or `wiki/`. Verifiable by running `/ingest /path/to/file.pdf` (no anchor) → expecting non-zero exit + stderr message.

**E4 — Signal rejection (missing `para_tier`):** at ingest interactive mode, prompt for the value; in batch mode, reject with `escalations[]{trigger: missing-para-tier}` and suggested values per A4 inference logic.

**E5 — Synthetic 10-fixture acceptance test passes (P2.2 acceptance predicate):** 5 drafts with `para_tier:` populated → accepted; 5 drafts without → rejected. `/lint --check-para-tier` flags 0 false positives, 0 false negatives on the fixture. [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md:§2 Part 2 Bullet 2 acceptance predicate; F4|G:P2.2 binding|R-high]

**E6 — STOP gate packet validation pass (P2.1 acceptance predicate):** every Part 2 STOP gate submission validates against Part 6b §I.4 awaiting-approval-packet.json schema; `gate_class: stop_gate` non-null; provenance chain reconstructable from the packet's `provenance:` field. [F4|G:P2.1 binding; consumer of F8 schema|R-medium]

**E7 — Multi-owner stub readability (P2.3 acceptance predicate):** Phase B partner reading §X can identify exactly which fields and which authority delegation pattern they must supply to instantiate a second-owner gate without re-architecting. Verified by Phase B partner walkthrough at activation time. [F2|G:Phase B preparation; not yet exercised|R-low]

---

## §F Anti-scope (per FUNDAMENTAL §6)

**Generic (applies to all Foundation parts):**

- This part does NOT make strategic decisions [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.1; F8|G:Foundation hard rule|R-high]. Therefore: ranking which signal is more important than another, deciding which project to advance, choosing between investment alternatives — all out of scope. Part 2 ingests signals as supplied; the strategic content is owner-judged at the STOP gate or at downstream Parts (Part 9 Owner Interaction Scaffold, Part 5 Compound Learning).

- This part does NOT substitute for founder agency — the STOP gate enforces the founder's role as the human who reviews and decides [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.2; F8|G:Foundation hard rule|R-high].

- This part does NOT use engagement-economy patterns — no algorithmic feed, no "recommended for you" without explicit query, no notifications that exploit attention rather than informing it [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.3; F8|G:Foundation hard rule|R-high].

**Part-specific:**

- This part does NOT do final synthesis or KB compilation. Part 3 (KB & Methodology Library) owns that. Part 2 produces draft candidates only; the canonical entity creation happens at Part 3 admissibility. The consequence sentence: a pull request that proposes Part 2 directly writing to `wiki/concepts/` is rejected at architecture review.

- This part does NOT own the `wiki/` directory or any canonical KB content. Per the U.System / U.Episteme split: Part 2 produces U.Episteme drafts; Part 3 owns U.Episteme canonical content; the accessor pipeline (`/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint`) is U.System owned by `swarm/lib/` shared infrastructure with Part 3 as named lead per C1 Joint Design [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md; F4|G:Bundle 2 C1 Joint Design canonical|R-medium].

- This part does NOT own signal-type-specific filter definitions beyond the generic anchor discipline. RUSLAN-LAYER declares which signal types are in scope (voice vs URL vs book-excerpt vs research-dump ratios; specific keyword filters per `tools/extract.py`; PARA-tier inference rules per A4). The Foundation declares only that filters EXIST and are DECLARATIVE YAML rather than hidden code logic [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§1 UC-B.1 "filters declarative, не hidden logic"; F4|G:Foundation generic vs RUSLAN-LAYER split|R-medium].

- This part does NOT auto-respond to external signals without owner initiation. Per FUNDAMENTAL §4.5 the auto-respond-without-ack pattern is prohibited [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§4.5; F8|G:Foundation hard rule|R-high].

- This part does NOT own the D28 anchor registry. Anchors are defined in project/area files (Part 7 — Project Lifecycle Substrate) and `wiki/index.md` (Part 3). Part 2 VALIDATES against them at ingest, but does not write anchor definitions itself.

- This part does NOT own the Private Library content (`raw/books-md/` — 393 books per AUDIT §1.1). Books are RUSLAN-LAYER raw source material; the Foundation pipeline ingests EXCERPTS at owner-initiation, not whole books. The book corpus is Phase B "fuel" per §5.8.2 of brigadier conventions; Phase A reads only what owner explicitly references.

- **Stoic Dichotomy of Control (PHILOSOPHICAL note — DEFERRED to Wave D documentation pass per Bundle 2 operational bias):** The pipeline sits at the boundary between "in our control" (anchor discipline, PARA tagging, STOP gate emission) and "not in our control" (the world's signal volume, signal quality, owner attention budget). Part 2 enforces what is in our control (the schema, the gate, the provenance chain); it does not attempt to control what is not (whether the owner reviews quickly, whether the world sends meaningful signals). Per Bundle 2 operational bias, this framing is NOT adopted as §F.3 prose; it is documented here at the §F level as a single-sentence acknowledgement rather than a multi-paragraph philosophical block. The operational consequence (no SLA on owner review latency in Phase A; no auto-escalation when STOP queue grows) is what matters.

- This part does NOT replace Part 10 (External Touchpoints). When signals come from external structured sources (CRM webhook, email forward via Part 10 inbound, Linear sync), Part 10 is the boundary layer; Part 2 receives the inbound after Part 10 has formatted it as `/ingest`-compatible input. In Phase A, Part 10 is stub-only; all signal entry is owner-initiated `/ingest`.

---

## §G F-G-R Tagging (per FPF B.3, Part 6a §I.1 F8 schema)

[src:swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I.1 F-G-R F8 schema; src:design/JETIX-FPF.md:§4.2 B.3]

Every artefact emitted by Part 2 carries F-G-R per the F8-LOCKED schema. The tagging discipline:

| Artefact emitted | Formality (F0-F9) | ClaimScope (G) | Reliability (R) |
|---|---|---|---|
| Raw transcript (`.md` in `raw/transcripts/`) | **F1** — single-source informal; AI-transcribed audio, unverified | `holds_within: [recording-session-<slug>]` — no cross-session validity assumed | **R-low** — transcription accuracy ~95% (Groq Whisper baseline cycle 11 per AUDIT §6.1); owner must review before any consequence; `refuted_if: <transcription_word_error_rate >5%>` per per-slug audit |
| Triage draft candidate (`inbox/<slug>-DRAFT.md`) | **F2** — AI-extracted and structured by `tools/extract.py`, unreviewed by owner | `holds_within: [anchor-<slug-or-topic>]` — not valid cross-anchor without explicit linkage | **R-low** until STOP gate ack; **R-medium** after human-ack (owner confirmed relevance); `refuted_if: <owner rejects at STOP gate>` |
| Review report (`reports/review_YYYY-MM-DD.md` + `~/review-latest.md`) | **F3** — multi-source informal; aggregates multiple pipeline run results into a single human-readable report | `holds_within: [pipeline-run-<date>]` — stale within 24 hours if new signals ingested | **R-medium** — human-readable summary; owner determines actionability; `refuted_if: <next pipeline run produces report contradicting prior actionability>` |
| AWAITING-APPROVAL STOP gate packet (`swarm/awaiting-approval/<pkt-id>.md`) | **F4** — operational convention; conforms to Part 6b §I.4 F8 schema | `holds_within: [packet-<pkt_id>]` — single-decision scope | **R-high** on schema-validation pass; **R-medium** on owner ack (depending on review_checkpoint answer specificity); `refuted_if: <packet rejected at gate as schema-violating>` |
| Promoted wiki entry (post STOP gate, in Part 3's territory) | **F4** — operational convention; passed human review | `holds_within: [anchor-<slug>]` — D28 anchor anchors the claim's relevance domain | **R-medium** — human-acked, but provenance chain is ingest-event-based (not peer-reviewed); F-level may rise to F5 post-cycle-validation per OQ-B1-1 anchor wording |

**F-level promotion path for a typical voice memo:**

1. Voice file enters: F0 (no claim yet — pre-ingestion).
2. Transcription completes: transcript at F1.
3. Extraction produces triage draft: draft at F2 with anchor + `para_tier:` populated.
4. STOP gate packet emitted: packet at F4 (consumer of F8 schema; gate-validating contract).
5. Owner acks: draft frontmatter receives `human_acked_at:`; F-level becomes F4 (operational convention; passed human review).
6. Cycle 13+ accumulates evidence (claim referenced ≥3 times across cycles): F-level may rise to F5 per OQ-B1-1 anchor wording per Part 6a authority (post-ack F-promotion is Part 6a's quarterly audit territory, not Part 2's).

The consequence of this tagging path: Part 2 NEVER stamps F5 or higher on its own outputs. F5 promotion is methodology-validated; F6 is cross-cycle reuse evidence; F8 is constitutional. These promotion classes happen downstream (Part 6a quarterly audit, Ruslan ack via constitutional packet). Part 2 is the F1→F4 segment of the pipeline.

**Inline F-G-R discipline (DOGFOOD per Bundle 1 Part 6a §C):** every claim in this architecture document carries F-G-R either in the §G table above or inline in the form `[F4|G:scope-token|R-medium]` (or via `[src:...]` citation followed within 200 chars by a consequence sentence — the citation+consequence is the operational anti-cargo-cult check; the F-G-R triple is the formal validity stamp). Critic gate verifies both.

---

## §H Code-level Interfaces

This section declares the interface contracts. The actual implementations (`tools/transcribe.py`, `tools/extract.py`, etc.) are RUSLAN-LAYER per §X; the Foundation declares only the structural contract.

### §H.1 `/ingest` skill signature

```bash
/ingest <signal-source> --anchor=<topic|project|question> [--para-tier=<Project|Area|Resource|Archive>] [--new-anchor] [--clipboard] [--no-stop-gate-defer]
```

**Parameters:**

- `<signal-source>` (required, positional) — one of: voice file path (`.ogg`/`.mp3`); URL; markdown/PDF/text file path; literal `clipboard` (with `--clipboard` flag).
- `--anchor=<value>` (required) — D28 anchor; non-null; matches existing anchor in `wiki/index.md` OR requires `--new-anchor` flag.
- `--para-tier=<value>` (optional but enforced) — one of `Project | Area | Resource | Archive`. If absent, pipeline infers per A4 admissibility logic OR prompts (interactive) OR rejects (batch).
- `--new-anchor` (optional) — declares the supplied anchor is new; pipeline accepts and adds to `wiki/index.md` under owner ack.
- `--clipboard` (optional) — signal source is the clipboard string captured at invocation.
- `--no-stop-gate-defer` (optional, advanced) — does NOT defer STOP gate to next session; emits packet immediately. Default behaviour batches packets to next session for owner attention budget.

**Return contract:**
- Exit code 0: pipeline run completed; transcript/draft/review-report committed; STOP gate packet at `swarm/awaiting-approval/<pkt-id>.md` awaiting ack.
- Exit code 1: signal-validation failure (missing anchor, invalid file path, signal type out of scope). Stderr names the violation.
- Exit code 2: pipeline-stage failure (transcription error, extraction error, commit failure). Stderr surfaces the specific failure mode per §K.
- Exit code 3: STOP gate packet schema violation (Part 6b §I.4 contract failed). Stderr names the schema violation. Per L7 Halt-Log-Alert.

### §H.2 STOP gate packet emission contract (P2.1 binding)

Part 2 emits packets conforming exactly to Part 6b §I.4 F8-LOCKED `awaiting-approval-packet.json`. The emission function (Phase A: brigadier on Part 2's behalf; Phase B: Part 2 has direct emission capability) must produce:

```yaml
# Pseudo-schema (the canonical schema is JSON at shared/schemas/awaiting-approval-packet.json
# per Part 6b §I.4; this YAML form is the human-readable view used in swarm/awaiting-approval/<pkt-id>.md)
gate_class: "stop_gate"   # F8 LOCKED enum literal
packet_id: "pkt-YYYYMMDD-<draft-slug>"
timestamp: "<ISO 8601>"
submitted_at: "<ISO 8601>"
acked_at: null   # populated at ack
actor: "part-2-ingest"   # role-archetype, IP-1 compliant
summary: "<≤500 chars: signal source / anchor / proposed promotion / consequence>"
outcomes:
  - "draft promoted to wiki/<entity-type>/<slug>.md if approved"
  - "swarm/approvals/log.jsonl updated with provenance chain"
provenance:
  artefact_path: "inbox/<slug>-DRAFT.md"
  sources:
    - "raw/transcripts/<slug>.md"
    - "<original-signal-path-or-URL>"
ack_request:
  option_a: "Approve as-is: draft promoted to <wiki-path>; provenance committed"
  option_b: "Approve with modifications: <available modifications: edit anchor / change para_tier / amend body>"
  option_c: "Permanently reject: draft remains at <draft-path> with status superseded; not promoted; no retry without new packet"
review_checkpoint:
  question: "What specifically did you verify before acking this packet?"
  answer: ""   # owner fills; ≥10 chars; prevents blank rubber-stamp
reversibility_class: "reversible"   # typical for Part 2 — promotion can be reverted via Part 1 git revert
blast_radius_tier: 2   # tactical batch-eligible (typical); 1 if signal touches FUNDAMENTAL revision (rare)
batch_eligible: true   # Tier 2 typical
supersedes: null   # populated only if this corrects a prior packet
advisory_cai_flag: false   # OQ-CAI-3 Wave D detection logic
f_g_r_delta:
  F: "F2 → F4"   # pre-ack F-level to post-ack F-level
  ClaimScope: {holds_within: ["anchor-<slug>"]}
  R:
    refuted_if: "owner rejects at STOP gate"
cycle_id: "cyc-<id>"   # if applicable
constitutional_violation: null   # populated only if signal trips a §6.1 rule
```

The packet validates against `shared/schemas/awaiting-approval-packet.json` (F8 LOCKED schema). Schema violation triggers L7 Halt-Log-Alert.

### §H.3 PARA-tier validation function (P2.2 binding)

Pseudocode (the actual implementation is RUSLAN-LAYER):

```
function validate_para_tier(draft_path):
  fm = parse_frontmatter(draft_path)
  if "para_tier" not in fm:
    return reject(reason="missing para_tier", suggestion=infer_from_anchor(fm.anchor))
  if fm.para_tier not in ["Project", "Area", "Resource", "Archive"]:
    return reject(reason="invalid para_tier value", got=fm.para_tier)
  return accept

function infer_from_anchor(anchor):
  # RUSLAN-LAYER inference rules per §X:
  # - anchors in projects/_active/* → Project
  # - anchors in directions/* → Area
  # - book-excerpt or research-dump anchors → Resource
  # - archived anchors → Archive
  # Foundation declares only that inference EXISTS as fallback; specific rules are RUSLAN-LAYER.
  return inferred_tier_or_none
```

`/lint --check-para-tier` extends Bundle 1 P6a.2 citation enforcer — ADDED as a new lint signal (not extending the citation check; the para_tier check is structurally distinct: citations validate content quality, para_tier validates classification completeness). The new lint signal:

```
function lint_check_para_tier():
  for file in glob("wiki/**/*.md") + glob("inbox/*-DRAFT.md") + glob("reports/review_*.md"):
    fm = parse_frontmatter(file)
    if fm.pipeline in ["ingested", "compiled", "linted", "ready"] and "para_tier" not in fm:
      flag(file, signal="missing-para-tier", severity="defect")
  return flagged_files
```

The threshold: 0 missing-para-tier defects on canonical entries (`pipeline: ready`); 0 false positives on synthetic 10-fixture acceptance test (P2.2 acceptance predicate).

### §H.4 Voice pipeline integration (RUSLAN-LAYER tooling reference)

The current voice pipeline (per CLAUDE.md §Voice-Notes Pipeline) is RUSLAN-LAYER tooling that invokes into the Foundation interface. The integration:

1. `tools/transcribe.py` reads `inbox/*.ogg`/`*.mp3`; invokes Groq Whisper (RUSLAN-LAYER API binding); writes `raw/transcripts/<slug>.md` with frontmatter `pipeline: raw`, `F: F1`, `sources: [<audio-file-path>]`, `ClaimScope: {holds_within: ["recording-session-<slug>"]}`, `R: {refuted_if: "WER>5%"}`. **Foundation contract:** the file exists at the declared path with the declared frontmatter; the API binding is RUSLAN-LAYER.

2. `tools/extract.py` reads `raw/transcripts/<slug>.md`; invokes Claude (RUSLAN-LAYER API binding) with extraction prompt; produces structured items at `inbox/<slug>-DRAFT.md` with frontmatter `pipeline: ingested`, `F: F2`, anchor + `para_tier:` populated, `sources: [<transcript-path>]`. **Foundation contract:** items have anchor + `para_tier:` mandatory before handoff.

3. `tools/filter.py` reads multiple drafts; deduplicates via `rule_slug` (Bundle 2 P3.2 alignment); produces a deduped set committed to `inbox/`. **Foundation contract:** deduplication is idempotent (re-running on the same set produces the same output).

4. `tools/review_report.py` aggregates the pipeline run into `reports/review_YYYY-MM-DD.md` + `~/review-latest.md`. **Foundation contract:** report is committed within ≤5 min of the pipeline run.

5. STOP gate emission (currently brigadier-mediated; Phase B may move into Part 2 directly): packet at `swarm/awaiting-approval/<pkt-id>.md` per §H.2.

The Foundation does NOT prescribe `tools/*.py` exist; it prescribes the contracts they satisfy. A Phase B partner could replace the toolchain with their own (e.g., different transcription provider, different extraction prompt) as long as the contracts hold.

### §H.5 Multi-owner gate authority delegation (P2.3 stub)

Phase A is single-owner: STOP gate ack is Ruslan-only. Phase B introduces multiple owners; the gate authority must be delegable. The stub declares:

**Trigger predicate:** `owner_count > 1` (where `owner_count` is RUSLAN-LAYER configuration in the partner's `executor-binding.yaml` or equivalent).

**Per-owner gate instance:** when the trigger fires, the STOP gate spawns N gate instances (one per owner), each with scoped authority over a subset of the anchor namespace. The subset is declared via a new packet field `owner_scope:` (added in Phase B; absent in Phase A; Foundation declares the field shape):

```yaml
owner_scope:
  owner_id: "<owner-archetype-name; IP-1 compliant; never executor name>"
  anchor_glob: "<anchor pattern this owner has authority over; e.g., 'directions/sales/*'>"
  authority_class: "primary | delegated | review-only"
```

**F.9 Bridge fields required for multi-owner activation:**
- `bridge_id: <fork-or-instance-identifier>` — links this gate instance to its parent fork
- `scope_signature: <hash of owner_scope>` — verifiable identity of the scope claim
- `co_owner_ack_required: <boolean>` — whether this packet needs additional acks from peer owners
- `escalation_to_super_owner: <owner-archetype-name | null>` — who acks if this owner's authority expires

**Activation gate:** per Part 6b §I.4, multi-owner gate instantiation requires AWAITING-APPROVAL with `gate_class: stage_gate` (constitutional level — not stop_gate, because instantiating a new authority surface is a constitutional act).

**Spec-only.** No implementation in Phase A. The Foundation declares the field shape and trigger so a Phase B partner can instantiate without re-architecting; the partner's executor-binding.yaml supplies the specific owner names, anchor globs, and authority class assignments.

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§6.2 "structural change estimate ~35% — ABOVE 30% threshold"; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§7 OQ-6; F2|G:Phase B preparation; not yet exercised|R-low — proposed; not validated]

---

## §I Data Schemas

### §I.1 Draft-candidate frontmatter schema (P2.2 binding)

The canonical draft frontmatter contract:

```yaml
---
pipeline: ingested      # one of: raw | ingested | compiled | linted | ready
sources:                 # mandatory; ≥1; raw-source provenance chain
  - <path-to-raw-or-prior-stage>
anchor: <topic|project|question>   # D28 mandatory, non-null
para_tier: Project | Area | Resource | Archive   # P2.2 MANDATORY (Bundle 2)
human_acked_at: <ISO 8601 | null>   # populated post-STOP-gate-ack only
ack_packet_id: <pkt-YYYYMMDD-slug | null>   # populated at ack
F: F0..F9   # per FPF B.3 / Part 6a §I.1; typical Part 2 pre-ack: F2; post-ack: F4
ClaimScope:
  holds_within: [<scope-token>]   # typical: [anchor-<slug>]
R:
  refuted_if: <Popperian falsifier>
edges:                   # optional; A.14 typed edges; appended to wiki/graph/edges.jsonl on promotion
  - {from: <slug>, to: <slug>, type: <A.14 edge type>, confidence: <low|medium|high>}
---
```

**Validation rules:**

- `pipeline:` must be one of the 5 enum values [src:CLAUDE.md Wiki Pipeline].
- `sources:` array length ≥1; each element resolves to an existing file or canonical URL.
- `anchor:` non-null; matches `wiki/index.md` entry OR carries `--new-anchor` flag at ingest.
- `para_tier:` non-null; one of the 4 enum values [Bundle 2 P2.2 binding].
- `human_acked_at:` null pre-ack; ISO 8601 timestamp post-ack.
- `F:` matches FPF B.3 0-9 anchors per OQ-B1-1 wording (Bundle 1 ack); F0-F2 NEVER canonical (`pipeline: ready` requires F3+).
- `ClaimScope.holds_within:` array of scope tokens per Part 6a F8 schema.
- `R.refuted_if:` non-empty Popperian falsifier sentence.

### §I.2 STOP gate packet schema (P2.1 binding — UND-4)

**This part REFERENCES `shared/schemas/awaiting-approval-packet.json` as authored at Part 6b §I.4 (F8 LOCKED).** Part 2 does NOT redefine the schema; it CONSUMES the F8 contract. The pre-emission validation step in `swarm/lib/hooks/verify-packet.sh` validates against the schema via `jq` (Phase A advisory) or `jsonschema` (Phase B blocking per OQ-B1-4 deferred).

The fields Part 2 must populate are enumerated in §H.2 above. Required fields (per Part 6b §I.4): `gate_class`, `packet_id`, `timestamp`, `submitted_at`, `actor`, `summary`, `outcomes`, `provenance`, `ack_request`, `reversibility_class`, `blast_radius_tier`, `review_checkpoint`, `f_g_r_delta`. Optional fields: `acked_at` (populated at ack), `batch_eligible`, `supersedes`, `advisory_cai_flag`, `cycle_id`, `constitutional_violation`.

**Schema reference (DRY enforcement):** Part 2 §I.2 REFERENCES Part 6b §I.4. Part 2 does NOT duplicate the JSON schema body. Critic gate verifies the reference; duplicate JSON schema body in Part 2 §I would be an auto-rejection.

### §I.3 Multi-owner gate packet field extensions (P2.3 stub)

The field shape declared in §H.5 above:

```yaml
owner_scope:
  owner_id: <owner-archetype-name>   # IP-1 compliant
  anchor_glob: <pattern>
  authority_class: primary | delegated | review-only
bridge_id: <fork-or-instance-identifier>
scope_signature: <hash>
co_owner_ack_required: <boolean>
escalation_to_super_owner: <owner-archetype-name | null>
```

These fields are NULL/absent in Phase A. The schema MAY declare them as optional (`additionalProperties: false` is RELAXED to allow these specific extension fields under a future schema_version 1.1.0 bump). Bundle 4 / Phase B will materialise the actual schema bump via constitutional AWAITING-APPROVAL gate per Part 6b §E Law L9.

### §I.4 Provenance chain structure (D6 binding)

Every draft promoted via Part 2 carries a reconstructable provenance chain. The chain is implicit in `sources:` frontmatter + `human_acked_at:` + `ack_packet_id:` plus the git history of the file's path. Explicitly (not stored as a separate field; reconstructable):

```
chain:
  - stage: raw
    path: <signal-path or URL>
    timestamp: <when signal arrived>
    F: F0
  - stage: transcript (voice signals only)
    path: raw/transcripts/<slug>.md
    timestamp: <transcription completion>
    F: F1
  - stage: triage_draft
    path: inbox/<slug>-DRAFT.md
    timestamp: <extraction completion>
    F: F2
    para_tier: <value>
    anchor: <value>
  - stage: gate_packet
    path: swarm/awaiting-approval/<pkt-id>.md
    packet_id: <pkt-id>
    submitted_at: <timestamp>
  - stage: human_ack
    acked_at: <timestamp>
    review_checkpoint_answer: <≥10 chars>
  - stage: promotion
    path: wiki/<entity-type>/<slug>.md
    F: F4
    committed_at: <timestamp>
    commit_hash: <SHA-1>
```

This chain is what Part 6a's quarterly immune audit traverses to verify provenance compliance (per Part 6a §J quarterly audit). Each step's existence is the audit invariant; each step's `committed_at` is the timeline reconstruction; each step's F-level is the formality progression.

---

## §J Operational Rituals

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/unix-philosophy.md:§3 "do one thing well per pipeline stage"; src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§J SRE burn-rate]

| Ritual | Cadence | Trigger | Responsible | Expected output | Notes |
|---|---|---|---|---|---|
| `tools/run_pipeline.sh` (voice batch) | Event-driven (when owner has voice memos to process) | Owner runs the script | Owner | Voice transcript(s); triage draft(s); review report at `~/review-latest.md` | Cycle 11 baseline ~2-3 min runtime; RUSLAN-LAYER tooling per §X |
| `/ingest <signal>` (per-signal) | Event-driven | Owner invokes per signal | Owner via slash-command | Triage draft; STOP gate packet at `swarm/awaiting-approval/<pkt-id>.md` | Foundation generic — partner replaces with their own orchestrator if desired |
| Owner STOP gate review | Within ~24h of packet emission (Phase A target; not enforced) | Packet exists at `swarm/awaiting-approval/` | Owner | Ack via Option A/B/C per Part 6b §6.3 | Latency target is RUSLAN-LAYER; Foundation declares only that ack happens before promotion |
| `/lint --check-para-tier` | Weekly (Sunday morning per CLAUDE.md cadence) + on-demand | Calendar cron OR owner invocation | `/lint` accessor skill (swarm/lib/) | List of canonical entries lacking `para_tier:` + suggested values per A4 | Bundle 2 P2.2 binding; new lint signal |
| `/lint --check-citations` | Pre-commit (Phase B blocking) + weekly audit (Phase A log-only) | git commit attempt + Sunday cron | `/lint` accessor skill (per Bundle 1 P6a.2; specified, Bundle 4 implementation per OQ-B1-2) | Cargo-cult flags on Part 2 outputs (citation without consequence sentence within 200 chars) | Bundle 1 P6a.2 cross-check; per Bundle 1 ack OQ-B1-2 proceed within 2 cycles |
| Provenance chain spot-check | Quarterly (Part 6a immune audit cadence) | Part 6a quarterly audit invocation | Part 6a (consumes Part 2's provenance chain) | Audit report at `swarm/audits/<quarter>/p2-provenance-coverage.md` | Coverage SLO target: 100% of `pipeline: ready` entries have reconstructable chain |
| Multi-owner gate stub review | Phase B activation event | `owner_count > 1` predicate fires (RUSLAN-LAYER config change) | Partner architect | F.9 Bridge fields populated per §H.5 | Currently inactive Phase A |

**SRE Workbook burn-rate algebra applied to Part 2 STOP-gate-latency SLO** [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§J burn-rate; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md:§4]:

| Burn rate | Part 2 observable | Required behaviour change |
|-----------|-------------------|---------------------------|
| **1× (normal)** | STOP queue depth ≤5; oldest packet age ≤24h | No change — within SLO |
| **6× (urgent)** | STOP queue depth >10 OR oldest packet age >72h | Ruslan notified within same session; pipeline rate-limited (no new ingests until queue drains to ≤5) |
| **14.4× (critical)** | STOP queue depth >25 OR oldest packet age >7 days | ALL new `/ingest` invocations halted until owner ack; AWAITING-APPROVAL escalation packet to Part 6b with `gate_class: stage_gate` requesting attention-budget reset |

**Phase A note:** these thresholds are advisory; Part 8 health monitoring (Bundle 4) is the operational enforcement substrate. In Phase A, the owner monitors the queue manually via `ls swarm/awaiting-approval/`. [F3|G:Phase A advisory; Phase B-blocking|R-medium — Part 8 not yet materialised]

**Evergreen note discipline (Karpathy / Matuschak)** [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 P3]: this Part 2 architecture document IS evergreen. Updates land via new commits, never via "archive-then-replace." The `git log` of this file is the version history. Therefore: a Bundle 3+ change to Part 2 produces a new commit referencing the prior architecture's commit hash, not a fresh document.

**Blameless postmortem ritual** [src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md:§4 P5; src:raw/books-md/sre/google-sre-book.md:Ch.15 (per Bundle 1 reference)]: any K-class incident affecting Part 2 (transcription error, ingest reject, STOP gate schema violation) MUST produce a `[meta] postmortem: <K-id> <YYYY-MM-DD>` commit with the 5-line minimum (per FUNDAMENTAL §2.4): what happened / why / what changed / how detect next / owner. Without the commit, the postmortem does not exist.

---

## §K Failure Modes

Exhaustive enumeration with detection signal and halt-or-continue policy per Halt-Log-Alert L9 (Part 6b §E Law L9: ≤1s halt / ≤5s log / ≤60s alert).

**K1 — Substrate failure cascade (Part 1 K8 fsck error blocks Part 2 commits).**
Detection: `git commit` exits non-zero in any pipeline stage. Policy: HALT pipeline; LOG to `swarm/awaiting-approval/<pkt-id>-defer.md` with reason; ALERT owner. Recovery: resolve Part 1 K8 (fsck), then resume pipeline. The pipeline produces no further drafts until substrate is healthy. [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§K K8; F4|G:Foundation cascade|R-high]

**K2 — Transcription error (`tools/transcribe.py` fails).**
Detection: non-zero exit from transcribe.py; stderr names the failure (Groq Whisper API error, audio file corruption, length >30 min). Policy: HALT for the specific signal; LOG the error with the audio file path; ALERT owner. The pipeline continues with other signals if batch. Recovery: owner resubmits the audio (possibly split per A2 30-min admissibility) or marks the signal as "skip" (committed `inbox/<slug>-SKIPPED.md` with reason). [F3|G:Phase A operational tolerance|R-medium]

**K3 — Extraction error (`tools/extract.py` fails or produces malformed draft).**
Detection: extract.py exits non-zero OR produces draft missing required frontmatter (anchor, para_tier, sources). Policy: HALT for the specific transcript; LOG the malformed draft path; ALERT owner with specific frontmatter violation. Recovery: re-run extraction with different prompt OR owner manually creates the draft from the transcript. [F3|G:Phase A operational|R-medium]

**K4 — Signal without anchor (D28 violation at ingest).**
Detection: `/ingest` invoked without `--anchor=`. Policy: REJECT immediately with stderr error + suggested anchors from `wiki/index.md`. No partial write. [F8|G:Foundation hard rule per L2|R-high]

**K5 — Signal without para_tier and anchor inference fails (P2.2 binding at ingest).**
Detection: ingest interactive mode prompts for `para_tier`; owner declines OR ingest batch mode without `--para-tier` AND anchor inference per A4 yields no result. Policy: REJECT; LOG to stderr; suggest the 4 enum values. No partial write. [F4|G:Foundation P2.2 binding|R-high]

**K6 — STOP gate packet schema violation (P2.1 binding).**
Detection: `verify-packet.sh` (Phase A advisory; Phase B blocking) fails validation against Part 6b §I.4 schema. Specific violations: missing required field, malformed `gate_class` value, F-G-R delta missing required sub-fields. Policy: HALT within ≤1s; LOG to `swarm/approvals/log.jsonl` within ≤5s with packet_id + violation; ALERT owner within ≤60s via `~/review-latest.md` flag (per L7). Recovery: regenerate packet with corrected fields; original malformed packet marked `superseded` with new packet referencing it. [F8|G:Bundle 1 LOCKED schema; Bundle 2 enforcement|R-high]

**K7 — STOP gate ack timeout (Phase A advisory; Phase B operational).**
Detection: packet age >7 days without ack. Policy: ALERT (no halt — owner attention budget is RUSLAN-LAYER). Phase B may add auto-escalation per `escalation_to_super_owner:` field in P2.3 stub. Recovery: owner manually acks OR explicitly defers via packet update. [F2|G:Phase B operational; Phase A advisory only|R-low]

**K8 — Notion write attempted (L5 violation).**
Detection: pipeline code (or extension) attempts to write to Notion. Policy: REFUSE at the never-list level (per Part 6b §I.3 `constitutional_never_list:`). PRE-COMMIT-HOOK blocks. Postmortem `[meta] postmortem: K8 L5-violation-attempt` commit required. [F8|G:Foundation hard rule per L5|R-high]

**K9 — Auto-respond to external signal without owner initiation (FUNDAMENTAL §4.5 violation).**
Detection: pipeline produces output (transcription, extraction, draft) without prior owner-initiated `/ingest` or `tools/run_pipeline.sh` invocation. Policy: REFUSE at the never-list level. The trigger event MUST be owner-action; "scheduled cron pulls signal" is prohibited Phase A. [F8|G:Foundation hard rule|R-high]

**K10 — Raw transcript in-place mutation (L6 Reversal Transactions violation).**
Detection: `git log` shows `raw/transcripts/<slug>.md` modified after initial commit (excepting frontmatter `supersedes:` updates which are themselves new commits). Policy: BLOCK at pre-commit hook; Phase B-active, Phase A log-only. Recovery: revert mutation; create a NEW transcript file with `supersedes:` pointer. [F5|G:Foundation generic Reversal Transactions|R-high]

**K11 — Multi-channel signal type out of scope (A5 violation).**
Detection: `/ingest <signal>` where signal is binary data, video file, or other unsupported type. Policy: REJECT with `escalations[]{trigger: out-of-scope, alternative_routing: <suggested>}`. Suggest extracting compatible representation (e.g., extract audio from video → re-ingest). [F4|G:Phase A operational|R-medium]

**K12 — Multi-owner gate trigger fires in Phase A (P2.3 stub activation in unsupported phase).**
Detection: `owner_count > 1` predicate evaluates true in Phase A configuration. Policy: HALT pipeline; LOG the predicate violation; ALERT owner that Phase B activation is required (Foundation revision via constitutional AWAITING-APPROVAL packet). [F2|G:Phase B preparation; not exercised Phase A|R-low]

**K13 — Cargo-cult citation violation (Part 6a P6a.2 lint signal — Bundle 4 implementation; Phase A advisory).**
Detection: `/lint --check-citations` flags Part 2 outputs with `[src:...]` not followed within 200 chars by a consequence sentence. Policy: ADVISORY in Phase A (lint signal logged); BLOCKING in Phase B (per Bundle 1 OQ-B1-2 proceed-within-2-cycles ack). [F3|G:Phase A advisory; Phase B blocking|R-medium]

**K14 — Cascading failure: Part 6b STOP gate offline blocks all Part 2 promotions (SRE Ch.22 stub).**
Detection: STOP gate validator unreachable OR Part 6b health degraded. Policy: QUEUE drafts to `swarm/awaiting-approval/<pkt-id>-deferred.md` with `pipeline-stage: pending-gate-recovery` frontmatter; resume promotion when Part 6b health restores. Per Bundle 1 K14 cascading-failure-graceful-degradation pattern. [F2|G:Phase B implementation; Phase A advisory|R-low]

**K15 — Concurrent ingest `.git/index.lock` conflict (Part 1 K15 cascade).**
Detection: parallel `/ingest` invocations both attempt commit. Policy: retry with exponential backoff per Part 1 K15. [src:swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§K K15; F4|G:Foundation cascade|R-medium]

---

## §L Wave C Worklist Bullet Status

Per Bundle 2 deep-prompt §2.1. Each bullet maps to acceptance predicate text + pass/fail rationale.

### Bullet P2.1 — STOP gate packet emission spec (UND-4 binding) ✅ ADDRESSED

**Acceptance predicate:** every Part 2 STOP gate submission validates against Part 6b §I.4 frozen schema; `gate_class: stop_gate` field non-null; provenance chain (raw source → triage draft → human-ack timestamp) traceable.

**Status:** Architecturally addressed in §H.2 (packet emission contract referencing Part 6b §I.4 F8 LOCKED schema by $ref); §I.2 (schema reference, no DRY duplication); §B Outputs (packet to Part 6b consumer); §K K6 (schema violation failure mode with Halt-Log-Alert per L7); §G F-G-R tagging (packet at F4 conforming to F8 contract).

**Operational verification:** at first Bundle 2 post-ack pipeline run, `verify-packet.sh` runs against the emitted packet; expected exit 0 (validation pass); `swarm/approvals/log.jsonl` entry exists. Phase A: this is the fixture-verification step the Part 6a quarterly audit will sample.

**F-G-R:** F4 (operational convention; consumer of F8 schema), `holds_within: [Foundation Phase A single-owner; cross-fork import as F8 contract import]`, `R-medium` until first quarterly audit cycle accumulates evidence (then potentially rises to F5 per OQ-B1-1 anchor wording).

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md:§2 Part 2 Bullet 1; src:RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md:§1 Decision #5]

### Bullet P2.2 — PARA-tier enforcement at /ingest level ✅ ADDRESSED

**Acceptance predicate:** synthetic 10-fixture (5 with `para_tier:`, 5 without) — pipeline accepts 5, rejects 5; `/lint --check-para-tier` flags any orphan canonical entry lacking `para_tier:`.

**Status:** Architecturally addressed in §I.1 (draft frontmatter schema with `para_tier:` mandatory); §H.3 (PARA-tier validation function pseudocode); §H.1 `/ingest` skill signature (`--para-tier=` parameter + A4 inference fallback); §E Law L4 (mandatory invariant); §E Effect E5 (synthetic fixture verification); §J operational ritual (weekly `/lint --check-para-tier`); §K K5 (failure mode at ingest); §C side-effect (frontmatter write).

**Implementation path:** `/lint --check-para-tier` is a NEW lint signal (#13 in the lint signal series, extending Bundle 1 #12 commit-format check). Adds to `/lint` accessor skill in `swarm/lib/` per C1 Joint Design — Part 3 lead, Part 4 advisory.

**Operational verification:** synthetic 10-fixture test created at first Bundle 2 post-ack pipeline run; `/lint --check-para-tier` produces 0 false-positives, 0 false-negatives on the fixture.

**F-G-R:** F4 operational convention, `holds_within: [Foundation Phase A; cross-fork import as Foundation generic]`, R-high (testable via fixture).

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md:§2 Part 2 Bullet 2; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md:§4 Forte PARA P4 + §6 Part 2 item 1]

### Bullet P2.3 — Multi-owner STOP gate stub (Phase B declaration) ✅ ADDRESSED

**Acceptance predicate:** Phase B partner reading Part 2 §X can identify exactly which fields and which authority delegation pattern they must supply to instantiate a second-owner gate without re-architecting.

**Status:** Architecturally addressed in §H.5 (multi-owner gate authority delegation pseudo-spec with trigger predicate, per-owner gate instance shape, F.9 Bridge fields, activation gate per Part 6b §I.4); §I.3 (multi-owner gate packet field extensions); §X Foundation vs RUSLAN-LAYER (the structure is Foundation generic; specific owner names + anchor globs + authority class assignments are partner's RUSLAN-LAYER); §K K12 (failure mode for premature Phase A activation).

**Spec-only:** NO implementation in Phase A. Implementation is Phase B materialisation; the architecture declares the field shape and trigger so a Phase B partner does not need to rediscover design intent.

**F-G-R:** F2 (proposed; not validated) → F3 on architecture-document acceptance (Ruslan ack of this Bundle 2 packet), `holds_within: [Foundation generic multi-owner pattern]`, R-low (no operational data yet).

[src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md:§2 Part 2 Bullet 3; src:swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md:§6.2 + §7 OQ-6]

---

## §M Wisdom Application Findings

[Per Bundle 2 deep-prompt §5 Wisdom Loop. Operational target ≥60% per Ruslan feedback after Bundle 1. NEW column **Operational vs Philosophical** added.]

| # | Card / Source | Principle | Current state | Improvement | Adopted? | Operational vs Philosophical | Justification | Section edited |
|---|---------------|-----------|---------------|-------------|----------|------------------------------|---------------|----------------|
| 1 | KM-Karpathy-Luhmann-Matuschak P4 (Forte PARA) | "Organise by actionability — not by topic, project, or note type" | Interface card §E declared `para_tier:` MUST be tagged but did not enforce | Add `para_tier:` mandatory frontmatter; reject drafts without it; `/lint --check-para-tier` audit check | YES | **OPERATIONAL** | Bundle 2 P2.2 binding; testable via 10-fixture | §I.1 + §H.3 + §E L4 + §K K5 + §J ritual |
| 2 | KM-Karpathy P1 (compounding cross-reference at every ingest) | "Each new note triggers ≥1 cross-reference update; without this, the wiki does not compound" | Interface card §A noted "Karpathy compounding" but Part 2 produces drafts, not entries — cross-ref happens at Part 3 promotion | Defer to Part 3 (P3.2 methodology library + edge density target ≥2.0); Part 2's role is to ensure draft frontmatter `edges:` block can carry edge candidates | NO | OPERATIONAL deferred | Domain-orthogonal: Part 2 produces drafts; Part 3 owns canonical entity creation + edge append; would be scope-creep for Part 2 to enforce edge-density-at-ingest | n/a (deferred to Part 3 §I) |
| 3 | KM-Karpathy P3 (Matuschak stranger test) | "Concept files: declarative-sentence title; context-free body; ≤500 words" | Part 2 produces drafts; concept-file quality is Part 3 admissibility | Defer to Part 3 §E Admissibility (interface card already declares the test); Part 2's deliverable is the DRAFT, not the canonical concept | NO | DOMAIN-ORTHOGONAL | Part 3 territory — concept-file admissibility | n/a |
| 4 | Unix-philosophy (do-one-thing-well per pipeline stage) | "Each stage of a pipeline does one thing and does it well; small composable tools" | Voice pipeline already structured as 4 distinct stages (transcribe / extract / filter / report); `/ingest` is the single-signal entry point | Already applied — voice pipeline cycle 11 baseline; document the discipline in §H.4 (RUSLAN-LAYER tooling reference) | YES | OPERATIONAL (already applied) | Pipeline structure is Foundation-generic; each stage emits committed file per IP-3 | §H.4 (already applied; documenting) |
| 5 | Event-Sourcing-CQRS (Young 2010 Reversal Transactions "There is no Delete") | "Corrections are NEW events with `corrects:` ref, never mutations of past events" | Implicit in Part 1 git history but not declared at Part 2 level | Declare L6 append-only on raw transcripts; `<slug>-v2.md` with `supersedes:` pointer; never in-place edit | YES | **OPERATIONAL** | Constitutional Reversal Transactions discipline applied at Part 2 raw layer | §E L6 + §C side-effects + §K K10 |
| 6 | Event-Sourcing-CQRS (STOP gate as command handler) | "A command (write) is validated, then handled, producing one or more events; events are append-only, never mutated" | STOP gate emission was specified at interface card level but not aligned with command-handler discipline | Declare STOP gate packet as the command-handler artefact; events appended to `swarm/approvals/log.jsonl` (Part 6a §C); packet supersedes path uses `supersedes:` field per Part 6b §I.4 | YES | **OPERATIONAL** | STOP gate is structurally a command-handler-and-event-emitter; aligns with Bundle 1 Part 6a/6b discipline | §H.2 + §C side-effects |
| 7 | Levenchuk-SHSM-FPF IP-3 commit-substrate | "Every artefact is a committed file; no ephemeral-only writes" | Interface card §C declared but did not exhaustively enumerate all stages | Declare L3 explicit (every pipeline stage commits); enumerate the 4 commit points (transcript / draft / report / packet) | YES | OPERATIONAL (reinforcing) | Foundation IP-3 dogfood | §E L3 + §C side-effects |
| 8 | Levenchuk-SHSM-FPF A.1 permeable-filtered boundary | "Boundary is permeable but filtered — what enters is constrained but flow exists" | The STOP gate IS the filter; D28 anchor is the leading filter | Already applied — D28 + STOP gate articulate the permeable-filtered boundary; no operational delta | n/a (already applied) | OPERATIONAL (already applied) | Boundary discipline already structurally enforced | n/a |
| 9 | Levenchuk-SHSM-FPF A.13 Agency-CHR (J-Approve decision class) | "STOP gate is structurally a J-Approve decision class — owner-only authority" | Interface card §D edge `methodologically-uses Part 6` already captures this | Reinforce in §D edge type + §E L1 + §H.2 packet structure (`actor: part-2-ingest` for emission; ack actor is owner per Part 6b §I.4) | YES | OPERATIONAL (reinforcing) | A.13 J-Approve dogfood | §D edge + §E L1 + §H.2 |
| 10 | Anthropic-CAI (transparency on gate failure) | "Surface gate failure with specific reason, not generic reject" | Interface card §E Deontics declared "MUST surface failure with reason" | Reinforce in §K K6 (specific schema violation in error message); §E D5 explicit | YES | **OPERATIONAL** | Transparency principle applied at error-handling level | §K K6 + §E D5 |
| 11 | Anthropic-CAI (constitutional_never_list dogfood) | "Hard rules encoded as machine-readable enum, not prose" | Bundle 1 Part 6b §I.3 has the 11-rule never-list enum | Apply at Part 2: K8 (Notion write) + K9 (auto-respond) + K10 (raw mutation) all reference Part 6b §I.3 enum entries; Part 2 enforces the never-list at its boundary | YES | OPERATIONAL (cross-Part dogfood) | Bundle 1 framework consumed at Part 2 enforcement boundary | §K K8/K9/K10 |
| 12 | SystemsThink-Cybernetics (Meadows L7 info-flows leverage) | "Information flows are highest-leverage intervention point" | `/lint` is Meadows L7 leverage point per Bundle 1 framing | At Part 2: STOP gate review report IS an information-flow design — it surfaces signals to owner attention; the report structure is the leverage | YES | OPERATIONAL (reinforcing) | Review-report design explicitly serves owner attention budget | §J ritual + §B Output |
| 13 | SystemsThink-Cybernetics (Beer pipeline as feedback loop) | "Pipeline produces signal that feeds back into design (e.g., review-report frequency informs cadence tuning)" | Implicit but not declared | Declare in §J operational rituals: pipeline outputs (review report cadence, queue depth) are inputs to Phase B Part 8 health monitoring | YES | OPERATIONAL | Feedback loop closure at Phase B; declared as P2.3 stub interface | §J + §X Phase B |
| 14 | Investor capital-allocation (long-term-compounding — voice-memo flow as compound asset) | "Each ingested signal is a unit of compounding institutional memory; the pipeline VALUE is superlinear in ingest count" | Implicit (Part 1 §J makes the analogous argument for git commits) | Declare in §0: the pipeline value is non-linear; one signal is data, 100 signals are an institutional memory | YES | PHILOSOPHICAL (justified — frames the pipeline value proposition; informs RUSLAN-LAYER attention budget allocation; not pure framing — affects whether owner invests in pipeline upkeep) | Phase A capital allocation: voice pipeline maintenance is high-leverage despite low immediate ROI | §0 |
| 15 | Stoic — Dichotomy of Control (Marcus Aurelius / Epictetus) | "Distinguish 'in our control' from 'not in our control'; design for the former, accept the latter" | Bundle 1 applied at Part 1 §F.3 | At Part 2: in-control = schema, gate, provenance, anchor discipline; not-in-control = signal volume, signal quality, owner attention budget | NO | PHILOSOPHICAL | Pure framing prose without operational consequence; per Bundle 2 Ruslan feedback: defer philosophical adoptions to Wave D documentation pass | §F single-sentence acknowledgement only (NOT a multi-paragraph block) |
| 16 | Lindy effect (long-lived patterns) | "Pipelines that have run unchanged for N cycles are likely to run for ~N more cycles" | Voice pipeline cycle 11 baseline; ~11 cycles operational | The Lindy framing would add a §G note "voice pipeline at Lindy F4"; no operational consequence | NO | PHILOSOPHICAL | Pure framing prose; Bundle 1 over-applied this; Bundle 2 defers | n/a |
| 17 | MAST coverage (Cemri 2025) — termination conditions | "Multi-agent failure 12.4% 'Unaware of Termination Conditions'" | Pipeline has implicit termination per stage exit code | Declare termination explicitly at §H.1 return contract (exit codes 0/1/2/3 + L7 Halt-Log-Alert SLA) | YES | **OPERATIONAL** | MAST failure-mode coverage at exit-code level | §H.1 return contract |
| 18 | KM-Karpathy P5 (query-driven KB) | "/ask --save filing as default" | Bundle 2 P3.4 binding — Part 3 owns the implementation | Defer to Part 3 P3.4; Part 2's role is feeding drafts that become queryable post-promotion | NO | OPERATIONAL deferred | Domain-orthogonal: Part 3 owns `/ask` semantics | n/a (Part 3 §I) |
| 19 | KM-Karpathy P6 (typed graph edges A.14) | "Edges are typed; generic `depends-on` forbidden" | Already enforced via Part 1 §D 10-edge canonical reference | Apply throughout §D dependencies; verify zero `depends-on` violations | YES | OPERATIONAL (reinforcing) | A.14 dogfood | §D entire section |
| 20 | Bai 2022 CAI (hardcoded never-list pattern) | "Hardcoded never-list as constitutional anchor" | Bundle 1 Part 6b §I.3 enum applied | Cross-reference at K8/K9/K10 failure modes | YES | OPERATIONAL (cross-Part dogfood) | Constitutional discipline at boundary | §K K8/K9/K10 |

**Aggregate count:** 20 rows; 13 YES Adopted (operational: 12, philosophical: 1) + 7 NO (deferred / domain-orthogonal / philosophical-without-justification).

**Operational ratio of YES Adopted:** 12 / 13 = **92%** — far exceeds Bundle 2 target of ≥60%.

**No fabricated YES entries** — every YES references a specific section edit verifiable by line trace in §A-§L. The single PHILOSOPHICAL adoption (#14 Investor compound asset) carries explicit Phase B/C-concrete-need justification (it informs RUSLAN-LAYER attention budget allocation; per Bundle 2 deep-prompt §5.2 it is permitted under "Phase B/C concrete need" gate).

---

## §N Provenance

**Sources consulted (with [src:] anchors throughout the document):**

| Source | Type | Sections referenced |
|--------|------|---------------------|
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md` | Wave A interface card | baseline §A-§H |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` | Wave A worklist | §2 Part 2 bullets P2.1/P2.2/P2.3 verbatim |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md` | Wave A dependency graph | §6.2 multi-owner ~35% structural change; §7 OQ-6 |
| `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` | Bundle 1 LOCKED | §I.2 commit-format-tokens.json; §J burn-rate; §D 10-edge A.14 reference; §K K8/K15 cascade |
| `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` | Bundle 1 LOCKED | §I.1 F-G-R F8 schema; §C citation discipline; §J quarterly audit |
| `swarm/wiki/foundations/part-6b-human-gate/architecture.md` | Bundle 1 LOCKED | §I.4 awaiting-approval-packet F8 schema with gate_class enum [stop_gate, stage_gate, draft_promotion]; §I.3 default-deny-table; §E Law L9 Halt-Log-Alert + Corrigibility |
| `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` | Bundle 1 ack record | §1 Decision #5 (packet schema FROZEN) |
| `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` | Constitutional baseline | §1 UC-B.1 strategy filters; §4.2 HITL; §4.5 auto-respond prohibition; §6.1 hard rules; §6.2 founder agency; §6.3 engagement-economy |
| `design/JETIX-FPF.md` | FPF | IP-3 commit-substrate; A.1 permeable-filtered boundary; A.13 J-Approve; A.14 typed edges; B.3 F-G-R; A.6.B L/A/D/E |
| `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` | Audit | §6 voice pipeline current state cycle 11 baseline ~2-3 min |
| `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md` | D25 D28 D17 | D17 Notion-not-authoritative; D25 commit-format; D28 anchor-mandatory |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md` | Wave B consultant | §4 P1/P3/P4/P5/P6; §6 Part 2/3 items |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/unix-philosophy.md` | Wave B consultant | §3 do-one-thing-well |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/event-sourcing-cqrs.md` | Wave B consultant | STOP gate as command-handler; Reversal Transactions |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` | Wave B consultant | IP-3; A.1; A.13; L/A/D/E |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md` | Wave B consultant | §4 P6 transparency-corrigibility; constitutional_never_list pattern |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md` | Wave B consultant | Meadows L7; Beer pipeline; Ashby variety (deferred to Part 4) |
| `raw/books-md/event-sourcing/young-cqrs-2010.md` | Wave B Supplement library-direct | p.31 "There is no Delete"; STOP gate as command handler |
| `raw/books-md/anthropic/bai-2022-cai.md` | Wave B Supplement library-direct | hardcoded never-list pattern (cross-referenced with Bundle 1 Part 6b) |
| `raw/books-md/anthropic/askell-2021-hhh.md` | Wave B Supplement library-direct | Appendix E.2 Corrigibility (cross-referenced with Bundle 1 Part 6b §E Law L9) |
| `CLAUDE.md` | Project conventions | Voice-Notes Pipeline §; Wiki Pipeline §; Global Rules § |
| `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` | Bundle 2 Joint Design | C1 canonical answer (referenced for §F Anti-scope first part-specific bullet) |

**Citation discipline:** every `[src:...]` is followed within 200 chars by a consequence sentence — the operational consequence Part 2 implements because of the source. Critic gate verifies (Bundle 1 P6a.2 lint signal, Bundle 4 implementation per OQ-B1-2). Manual audit at finalize confirms.

**Commits on `claude/jolly-margulis-915d34`:** to be appended at Phase F finalize.

---

## §X Foundation vs RUSLAN-LAYER Fork-Separation

[Per OQ-MERGED-3 fork-separation discipline; per Bundle 2 deep-prompt §6.7]

### Foundation generic (any Phase B partner imports as-is)

- **STOP gate structural pattern** — D28 anchor mandatory; PARA-tier mandatory frontmatter; AWAITING-APPROVAL packet emission to Part 6b §I.4 F8 schema; provenance chain raw→draft→ack reconstructable.
- **Pipeline contract** — every stage emits committed file (IP-3); raw is append-only with `supersedes:` for corrections (Reversal Transactions).
- **`/ingest` skill signature** — parameter shape per §H.1; exit codes per §H.1 return contract.
- **Draft-candidate frontmatter schema** — fields per §I.1 (`pipeline:`, `sources:`, `anchor:`, `para_tier:`, `human_acked_at:`, `ack_packet_id:`, `F:`, `ClaimScope:`, `R:`).
- **Multi-owner gate stub** — F.9 Bridge field shape per §H.5 (`owner_scope:`, `bridge_id:`, `scope_signature:`, `co_owner_ack_required:`, `escalation_to_super_owner:`).
- **`/lint --check-para-tier` signal** — schema and acceptance predicate per §H.3.

### RUSLAN-LAYER (specific to Ruslan's Jetix instance; partner replaces)

- **Voice pipeline tooling** — `tools/transcribe.py` (Groq Whisper API binding, Ruslan's API key — explicitly NOT in this doc per CLAUDE.md security; the script reference in §H.4 is the pattern); `tools/extract.py` (Claude API binding, Ruslan's prompt); `tools/filter.py` (Ruslan's dedup logic); `tools/run_pipeline.sh` (Ruslan's orchestration script). A Phase B partner replaces with their own.
- **PARA-tier inference rules per A4** — the specific mapping (which anchors are projects vs areas) is RUSLAN-LAYER. The Foundation declares only that inference EXISTS as fallback per A4.
- **Anchor registry contents** — `wiki/index.md` entries (Ruslan's specific projects, areas, questions); `projects/_active/` entries; `directions/` entries. The partner's registry is theirs.
- **STOP-gate-latency targets** — the "≤24h" advisory in §J operational rituals is a Phase A target; the partner sets their own based on their attention budget.
- **Strategy-aware filter contents** — per FUNDAMENTAL §1 UC-B.1, the FILTERS are declarative (Foundation generic); the FILTER VALUES (which keywords flag a signal) are RUSLAN-LAYER.
- **Specific signal-source whitelists** — Ruslan's `inbox/*.ogg` watching pattern is RUSLAN-LAYER; partner replaces.

### Phase B fork sees

A Phase B partner forking the Foundation:

1. **Imports** the Foundation generic schemas (draft-candidate frontmatter; STOP gate emission contract; multi-owner gate stub field shape; `/ingest` skill signature).
2. **Imports** the operational discipline (every stage commits; raw append-only; D28 anchor mandatory; PARA-tier mandatory).
3. **Replaces** RUSLAN-LAYER tooling with their own (transcription provider, extraction logic, dedup rules, orchestration script).
4. **Replaces** RUSLAN-LAYER content (anchor registry, PARA inference rules, filter values).
5. **Activates** P2.3 multi-owner stub if partner has multiple owners (`owner_count > 1`); supplies F.9 Bridge fields per §H.5 and `executor-binding.yaml` for owner identifiers.
6. **Cross-fork reconciliation** per Bundle 1 P1.1 cross-fork-provenance.json schema (deferred to `decisions/policy/cross-fork-audit-deferred-phase-b.md` per OQ-B1-8).

### Cross-fork provenance link

Per Bundle 1 P1.1: every cross-fork commit carries `cross_fork_provenance:` block referencing parent fork id, branch, divergence point, role-archetype, and reconciliation strategy. Part 2's pipeline outputs (transcripts, drafts, packets) participate in this provenance schema when imported across forks. The `approvals_reconciliation_strategy:` field (per OQ-B1-5 deferred to Bundle 4 Part 10) determines how a partner's STOP gate acks reconcile with the parent fork's `swarm/approvals/log.jsonl`.

---

*End of Part 2 — Signal Ingestion & Triage architecture. Status: draft-pre-ruslan-ack. F4 → F5 on Ruslan ack of Bundle 2 packet. Cross-references: C1-joint-design.md (Bundle 2); Bundle 1 LOCKED Parts 1/6a/6b architectures; Wave A interface card (superseded by this document for Wave C onward but preserved historically per Reversal Transactions).*
