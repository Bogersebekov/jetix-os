---
title: Part 2 Interface Card — Signal Ingestion & Triage
date: 2026-04-27
phase: A-2
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
part: 2
part_title: Signal Ingestion & Triage
u_classification: U.System
fpf_anchor: "FPF IP-3; D28 anchor-mandatory; FPF A.1 permeable-filtered boundary; FPF A.13 Agency-CHR STOP gate"
F: F4
ClaimScope: "Holds for all Foundation Parts 1-10 in Jetix Phase-A. The STOP gate is a structural invariant, not a behavioral convention. Does not cover RUSLAN-LAYER signal-type-specific filters or voice-pipeline toolchain choices."
R: "Refuted if a signal is shown to reach canonical KB (Part 3) without passing through a human-review STOP gate; accepted when all wiki entries carry a provenance link to a triage draft that has a human-ack timestamp."
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/engineering-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
---

# Part 2 Interface Card — Signal Ingestion & Triage

**Scope sentence.** The pipeline that converts external raw signals (voice memo, URL, file, book excerpt, email, clipboard item) into provenance-tagged, anchor-linked draft candidates ready for Knowledge Base promotion — with a mandatory STOP gate requiring human review before any entry becomes canonical. [src:candidate-parts-merged.md:§2 Part 2]

---

## A. Inputs

What this part consumes. Each entry: `<source> :: <data-shape> :: <event-trigger>`.

- **External world (owner-supplied):** raw signal file (`.ogg`, `.mp3`, `.txt`, URL, `.pdf`, clipboard string) :: file-create or skill-invocation event :: owner initiates `/ingest --anchor=<topic>` or voice-pipeline run
- **D28 anchor parameter (mandatory):** `--anchor=<topic|project|question>` string :: validated non-null at ingest boundary :: ingest-skill invocation [D28; engineering-expert.md:§3 D28]
- **Part 1 (System State Persistence):** git substrate for writing draft artefacts :: commit interface :: draft-write event
- **Part 3 (Knowledge Base & Methodology Library):** `wiki/index.md` for suggested anchor matching :: read-only query :: anchor-suggestion step during triage
- **FUNDAMENTAL §1 UC-B.1 strategy-aware filters:** declarative filter YAML (signal type + strategic focus tags) :: config-read :: pipeline initialization [FUNDAMENTAL §1 UC-B.1]

Multi-channel capture scope (G.1-G.2 addressed here per candidate-parts-merged.md §2 Part 2):
- Voice memos (`inbox/*.ogg`) :: raw audio :: file-create event
- URL / web page :: HTML or text :: owner-paste into ingest command
- File / book excerpt / research dump :: `.md`, `.pdf`, `.txt` :: file-path argument to `/ingest`

---

## B. Outputs

What this part exposes. Each entry: `<consumer> :: <data-shape> :: <event-published>`.

- **Owner (STOP gate):** `reports/review_YYYY-MM-DD.md` + `~/review-latest.md` :: human-readable triage review report :: review-report-generated event — **owner reads and decides before any part receives further output** [FUNDAMENTAL §4.2 HITL; FUNDAMENTAL §6.2]
- **Part 3 (Knowledge Base & Methodology Library):** promoted draft candidate (`.md` with YAML frontmatter + anchor + PARA-tier tag + provenance `sources:` block) :: ingest-completed event :: only after human ack at STOP gate
- **Part 1 (System State Persistence):** committed draft file at `raw/transcripts/` or `inbox/` :: `[ingest] verb what (why)` commit :: pipeline-stage-complete event
- **Part 6 (Governance, Provenance & Human Gate):** provenance chain (raw source path → draft path → human-ack timestamp) :: audit trail :: STOP gate ack event [FPF IP-3; D28]

---

## C. Side-effects

Per FPF IP-3 [FPF §5.3] and D28 [D28 anchor-mandatory]: every pipeline stage produces a committed file. No ephemeral-only outputs. No side-channel writes to Notion or external services.

- **Transcript write:** `raw/transcripts/<slug>.md` — committed via Part 1 at transcription stage
- **Draft candidate write:** `inbox/<slug>-DRAFT.md` or `reports/review_<date>.md` — committed via Part 1 at triage stage
- **STOP gate artefact:** human-ack timestamp written to draft frontmatter field `human_acked_at:` before promotion — this field is the provenance proof
- **PARA-tier tag:** frontmatter field `para_tier: Project|Area|Resource|Archive` written at triage stage per KM consultant P4 (Forte PARA organise by actionability) [knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 4; §6 Part 2 item 1]
- **NO side-effect to canonical wiki (Part 3):** Part 2 NEVER writes directly to `wiki/`; it queues a reviewed draft for Part 3 to promote

---

## D. Dependencies (typed per FPF A.14)

Each edge: `<edge-type> <part-name>` — with rationale. [FPF §3.5 A.14; levenchuk-shsm-fpf.md:§4 P4]

- `operates-in Part 1` — all pipeline stage outputs are committed files persisted in the git substrate; Part 2 operates within Part 1's write surface [candidate-parts-merged.md:§2 Part 2 FPF anchor: D25]
- `PhaseOf information-lifecycle` (cross-cutting) — Part 2's output (triage draft) is the pre-KB phase of the full information lifecycle; the phase boundary is the STOP gate [A-1-critic-gate.md:§2 Part 2 A.14 note: "Part 2 → Part 3 is PhaseOf"]
- `methodologically-uses Part 6` — the STOP gate is an instance of Part 6's HITL escalation discipline; the J-Approve decision-class authority (human ack required before canonical promotion) is owned by Part 6 but instantiated structurally in Part 2 [candidate-parts-merged.md:§2 Part 6 D-Lock anchor; FPF A.13 Agency-CHR]

Read-only reference (not a dependency edge):
- Part 2 reads `wiki/index.md` (Part 3 content) for anchor suggestions at ingest — this is a read, not a write dependency. The edge is `methodologically-uses Part 3` (Part 2 uses the KB's index to inform anchor selection) but does NOT create content in Part 3 directly.

---

## E. Boundary (per FPF A.6.B L/A/D/E)

[FPF §4.3 CP-3; levenchuk-shsm-fpf.md:§4 P6]

**Laws** (invariants MUST hold — violations are constitutional defects):
- The STOP gate is STRUCTURAL, not behavioral. No draft candidate reaches `wiki/` (Part 3) without a human-ack timestamp in its frontmatter [FUNDAMENTAL §4.2; FUNDAMENTAL §6.2; A-1-critic-gate.md:§2 Part 2 "STOP gate is an architectural enforcement"]
- D28 anchor is MANDATORY at ingest boundary. A signal without `--anchor=` is REJECTED by the pipeline with an error (not a warning) — this is a leading constraint, not a lagging lint check [D28; engineering-expert.md:§3 D28]
- Every pipeline stage output is a committed file; no ephemeral-only processing [FPF IP-3; D25]
- Notion NEVER appears in the write path of this part [D17]

**Admissibility** (acceptance criteria for inputs to enter the pipeline):
- Signal must carry a non-null `--anchor=` parameter matching an existing project, area, or question in `wiki/index.md` OR a newly declared anchor [D28]
- Signal duration (for voice): ≤30 min per single ingestion event — longer inputs require manual splitting [FUNDAMENTAL §1 UC-B.1 filter discipline]
- Signal source: owner-supplied only — Part 2 does NOT autonomously fetch or pull signals from external services without owner initiation [FUNDAMENTAL §6.2; §4.2]

**Deontics** (obligations of this part toward consumers):
- This part MUST produce a human-readable triage review report (`reports/review_YYYY-MM-DD.md`) for every pipeline run before any draft reaches the owner for ack [CLAUDE.md Voice-Notes Pipeline §4]
- This part MUST preserve raw source artefacts permanently in `raw/transcripts/` and `inbox/` — raw is immutable; processed may be updated but provenance link to raw is mandatory [FUNDAMENTAL §1 UC-B.3]
- This part MUST tag every draft with a PARA-tier field (`para_tier:`) before handoff to Part 3 [knowledge-management-karpathy-luhmann-matuschak.md:§6 Part 2 item 1]

**Effects** (measurable outcomes):
- After pipeline run: `reports/review_YYYY-MM-DD.md` exists and is committed; owner can read within ≤5 min of signal submission (voice pipeline runs in ~2-3 min per cycle 11 baseline) [AUDIT §6 voice-pipeline]
- After STOP gate ack: promoted draft appears in `wiki/` with `human_acked_at:` field populated and is searchable via `/ask` within the next `/consolidate` run
- Signal rejection (missing anchor): stderr error with suggested anchors from `wiki/index.md`; no partial write to `raw/` or `wiki/`

---

## F. Anti-scope (per FUNDAMENTAL §6)

Generic (applies to all Foundation parts):
- This part does NOT make strategic decisions [FUNDAMENTAL §6.1]
- This part does NOT substitute for founder agency — the STOP gate enforces the founder's role as the human who reviews and decides [FUNDAMENTAL §6.2]
- This part does NOT use engagement-economy patterns [FUNDAMENTAL §6.3]

Part-specific:
- This part does NOT do final synthesis or KB compilation — that is Part 3 (Knowledge Base & Methodology Library); Part 2 produces draft candidates only
- This part does NOT own the `wiki/` directory or any canonical KB content — it feeds drafts to Part 3 after STOP gate ack
- This part does NOT own signal-type-specific filter definitions beyond the generic anchor discipline — RUSLAN-LAYER declares what types of signals are in scope (voice vs URL vs book excerpt ratios, strategic focus tags); Foundation declares that filters exist and are declarative YAML [FUNDAMENTAL §1 UC-B.1 "filters declarative, не hidden logic"]
- This part does NOT auto-respond to external signals without owner initiation [FUNDAMENTAL §4.5 "auto-respond external без ack" — prohibited]
- This part does NOT own the D28 anchor registry — anchors are defined in project/area files (Part 7) and `wiki/index.md` (Part 3); Part 2 validates against them

---

## G. F-G-R Tagging (per FPF B.3)

[FPF §4.2 CP-2; levenchuk-shsm-fpf.md:§4 P5]

| Artefact emitted | Formality (F0-F9) | ClaimScope (G) | Reliability (R) |
|---|---|---|---|
| Raw transcript (`.md` in `raw/transcripts/`) | F1 — single-source informal; AI-transcribed audio, unverified | Holds only for the specific recording session; no cross-session validity assumed | R-low — transcription accuracy ~95% (Groq Whisper baseline per AUDIT §6.1); owner must review |
| Triage draft candidate (DRAFT.md with PARA-tier + anchor) | F2 — AI-extracted and structured, unreviewed by owner | Holds for the anchor context declared at ingest; not valid cross-anchor without explicit linkage | R-low until STOP gate ack; R-medium after human-ack (owner confirmed relevance) |
| Review report (`reports/review_YYYY-MM-DD.md`) | F3 — multi-source informal; aggregates multiple pipeline run results | Holds for the specific pipeline run date; stale within 24 hours if new signals ingested | R-medium — human-readable summary; owner determines actionability |
| Promoted wiki entry (post STOP gate, in Part 3) | F4 — operational convention; passed human review | Holds within the declared anchor scope; D28 anchor anchors the claim's relevance domain | R-medium — human-acked, but provenance chain is ingest-event-based (not peer-reviewed) |

---

## H. Originating + critic-flagged

**Originating experts:**
- engineering-expert (Part 3: Information Lifecycle) — primary proposal, Unix pipeline decomposition framing [engineering-expert.md:§2 Part 3]
- systems-expert (Part 1 partial: Information Lifecycle Substrate) — contributed the STOP gate as a structural leverage point
- G.1-G.2 UC gap addressed here: no expert proposed a standalone for multi-channel capture; voice pipeline already implements it [candidate-parts-merged.md:§2 Part 2 "Originating expert"]

**Critic flags applied from A-1 critic gate:**
- **NONE.** Part 2 was CLEAN on all IP-1/IP-2/IP-3/A.1/A.13/A.14/B.3/§6 checks. [A-1-critic-gate.md:§2 Part 2 "Verdict: CLEAN"]

**Key critic observations to carry forward to A-2 (non-flag):**
- STOP gate is structural (A.13 J-Approve decision class), not behavioral — this distinction is applied explicitly in §E Laws and §C Side-effects above [A-1-critic-gate.md:§2 Part 2 A.13 note]
- D28 anchor-mandatory cited as architectural constraint (leading, not lagging) — applied in §E Laws and §A Inputs above [A-1-critic-gate.md:§2 Part 2 B.3 note]
- G.1-G.2 multi-channel capture confirmed in scope of this part [candidate-parts-merged.md:§2 Part 2 UC mapping]
