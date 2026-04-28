---
title: "Foundation Part 11 — Strategic Direction Substrate (Pillar A)"
date: 2026-04-28
type: foundation-architecture
part: 11
pillar: A — Main Strategic Documents (system-wide direction)
status: AWAITING-APPROVAL — Bundle 5 brigadier draft
parent_cycle: cyc-foundation-build-2026-04-28
bundle: 5-strategic-layer
brigadier_phase: A-4 integrator drafts
predecessor_decisions:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/structural-placement-decision.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/fundamental-vision-hierarchy-decision.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/phase-1-baseline-disposition.md
constitutional_anchors:
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (LOCKED v1.0 §1 Categoria A UC-A.1/A.2/A.3/A.4)
  - design/JETIX-FPF.md (FPF IP-2/IP-3/IP-7/A.6.B/B.3)
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md (F-G-R F8 schema)
  - swarm/wiki/foundations/part-6b-human-gate/architecture.md (gate_class F8 schema; constitutional_never_list)
  - swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md (Pillar B integration target)
  - swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md (defers UC-A.1/A.2 hosting)
fpf_anchors:
  - "FPF IP-7 — writing-as-thinking (owner authors strategic content)"
  - "FPF IP-2 — bounded context (single-owner Phase A)"
  - "FPF IP-3 — artifacts over conversations"
  - "FPF B.3 — F-G-R provenance grading"
  - "FPF A.6.B — Boundary Norm Square (L/A/D/E)"
  - "FPF A.14 — typed edges (10 canonical types)"
ip2_single_owner_bounded: "Phase A scope is single-owner (Ruslan); strategic doc ack authority = Ruslan only per FUNDAMENTAL §6.2 founder-agency. Specific values (cadence weeks, ack SLA hours, content of Direction Cards) are RUSLAN-LAYER. Foundation generic = the doc-type structure + lifecycle + ack discipline + integration contracts. F.9 Bridge structural change ≥35% required at Phase B (multi-owner / fork instances)."
critic_findings: "Draft prepared; awaiting Phase A-6 critic gate. Self-checks done: 6 doc types map to Phase 1 disposition ADOPT-INTO-PILLAR-A (Lock Entry, North Star, Strategic Insight, Direction Card, Phase Plan, Strategic Reflection); FUNDAMENTAL hierarchy = subordinate elaboration (Option 2); Pillar A does not author principles (Pillar C boundary respected); Pillar A does not author project strategy (Pillar B boundary respected)."
ClaimScope: "Foundation generic — strategic-doc-type catalogue, lifecycle, cadence patterns, ack discipline, supersession via append-only, FUNDAMENTAL hierarchy contract, integration with Parts 4/5/6a/6b/7/8/9, decisions-DB structure (UC-A.4). RUSLAN-LAYER: actual content of strategic docs, specific cadence values, specific instance Direction Cards, specific Lock entries content, specific North Star focus, specific Phase Plan horizons."
F: F4
G: brigadier-Bundle-5 Pillar A integrator draft
R: R-medium — pending Ruslan ack
locked_decisions_referenced: [D-2 architect-orbit, D-21 Roy-Replication, D-22 Korp-Startup, D-26 single-accountable, D-27 Fork-and-merge, D-29 hybrid-framework]
---

# Part 11 — Strategic Direction Substrate (Pillar A — Main Strategic Documents)

## §0 Mission

Part 11 hosts **system-wide strategic direction** — the main strategic documents
that direct, hold, and anchor the owner's overall pursuit. Per FUNDAMENTAL §1
Categoria A (Strategic Management Layer):

- **UC-A.1** Multi-level strategic document hosting
- **UC-A.2** Strategic document creation assistance
- **UC-A.3** Strategic alignment enforcement
- **UC-A.4** Decisions tracking, recall & governance

Part 11 is the **structural place** where these UCs live. Per FUNDAMENTAL §6.2
founder-agency, content authoring is owner-only; agents draft, surface, recall,
remind — but never decide. Part 11 is Foundation generic — the structural slots,
lifecycles, governance, and integration contracts. The CONTENT of strategic
documents (e.g., Ruslan's Direction Card for «AI consulting DACH Mittelstand»)
is RUSLAN-LAYER personalization (next sprint).

[F4|G:Bundle 5 Part 11 architecture — Phase A single-owner; Fork-portable|R-medium — pending Ruslan ack]

---

## §A Inputs

| Source | Data shape | Event trigger | F-G-R |
|---|---|---|---|
| Owner direction signal | Direct Ruslan-authored prose entering `decisions/strategic/<type>/<slug>.md` (one of 6 doc types — Lock Entry / North Star / Strategic Insight / Direction Card / Phase Plan / Strategic Reflection) per §I.1 schema | Owner write event via daily-log promotion (Part 9 §B intake) OR direct authoring | F4-F8|G:owner-authored strategic|R-high |
| FUNDAMENTAL Vision LOCKED v1.0 | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (constitutional baseline; sector-agnostic) | Read at strategic-doc creation; cited in `constitutional_anchors:` frontmatter field | F8|G:LOCKED v1.0 constitutional|R-high |
| FPF Constitutional Spec | `design/JETIX-FPF.md` 3758 lines | Read at strategic-doc creation; cited in `fpf_anchors:` frontmatter field | F5|G:FPF-Steward governed|R-high |
| Pillar C principles | `principles/tier-1-manager/<slug>.md` + `principles/tier-2-system/foundation-generic/<slug>.md` | Read at strategic-doc creation; cited in `principles_compliance:` frontmatter field | F4-F8|G:Pillar-C canonical|R-medium-high |
| Compound learning insights from Part 5 | Methodology promotion candidates + Pattern surfaces from `methodology-promotion-event` per Part 5 §B Outputs | Asynchronous emit when Part 5 detects pattern crossing strategic threshold | F4|G:Part 5 Bundle 3 LOCKED|R-medium |
| Owner reflection prose from Part 9 | `monthly-reflections/<YYYY-MM>.md` containing strategic synthesis (per Part 9 §B output) | Monthly cadence emit per Part 9 §J | F5|G:Part 9 owner-authored|R-high |
| Project closure retrospectives from Part 7 | `project-retrospective-packet.json` per Part 7 §B (Phase B materialization) — `lessons_learned[]`, `dr_r_candidates[]`, `methodology_promotion_candidates[]` | Per project closure event | F4|G:Part 7 Bundle 4|R-medium |
| External signal-driven direction inputs | Mentor calls, market events, capital allocation events — entering via Part 2 (Signal Ingestion & Triage) classified `strategic_input` | Part 2 emit `strategic-input-classified` event | F2-F4|G:Part 2 classifier|R-low pre-ack |
| Strategic-doc supersession trigger | Owner-authored supersession event referencing prior doc via `supersedes:` frontmatter ref | Owner write event | F5|G:owner-authored|R-high |

### §A.1 Concrete consequence — strategic doc authoring is owner-only writing-as-thinking

Per FPF IP-7 [src:design/JETIX-FPF.md:§5.7] and FUNDAMENTAL §6.2 founder-agency
[src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.2], strategic doc PROSE
fields (e.g., North Star statement; Direction Card focus paragraph; Strategic
Insight memo argument body; Strategic Reflection synthesis) are owner-authored.
Agents may:
- Draft frontmatter (type / cadence / cross-refs / principles_compliance / anchors)
- Surface relevant prior decisions (UC-A.4 decisions DB recall)
- Generate "first-pass" prose for owner to edit-or-reject
- Run alignment check (UC-A.3) at promotion time

But agents NEVER author strategic prose without owner edit-pass-and-ack. Per
Pillar C Tier-2 rule 1 (constitutional_never_list rule 1 in Part 6b §I.2):
«AI does NOT make strategic decisions». Agent first-pass prose entering a
strategic doc without owner pass = halt_log_alert violation.

**Concrete enforcement.** Strategic doc frontmatter carries
`prose_authored_by: <ruslan | agent-draft-pending-ack | hybrid-with-ack-trail>`.
Promotion to LOCKED state requires `prose_authored_by ∈ {ruslan,
hybrid-with-ack-trail}`. Pre-commit lint rejects LOCKED state with
`prose_authored_by: agent-draft-pending-ack`. This is the structural enforcement
of FPF IP-7 + Pillar C Tier-2 rule 1 + FUNDAMENTAL §6.1.1.

### §A.2 Concrete consequence — append-only via supersession

Strategic docs are NEVER edited in place after promotion to F4+ status. New
direction = NEW doc with `supersedes: <prior-path>` frontmatter ref + commit
log entry per Part 1 §H discipline. Per Young 2010 Reversal Transactions
[src:raw/books-md/event-sourcing/young-cqrs-2010.md:§4 P3], the prior doc remains
canonical at its provenance moment; the new doc is additive.

Why: Strategic continuity (per FUNDAMENTAL §1 UC-A.4) requires reconstructible
direction-history. If old North Star is edited away, the chain «what we thought
in March → what we changed in May → what we shifted in August» becomes a single
mutated prose; pattern recognition across direction-shifts becomes impossible.
Append-only supersession preserves Strategic Continuity Substrate.

### §A.3 Concrete consequence — FUNDAMENTAL Vision is INPUT not OUTPUT

Per `fundamental-vision-hierarchy-decision.md` Option 2 (subordinate elaboration),
Pillar A docs cite FUNDAMENTAL via `constitutional_anchors:` ref but DO NOT
modify FUNDAMENTAL. FUNDAMENTAL revision (per Ruslan note 28.04 evening «они
как бы окей они есть, но мы их потом еще раз будем перерабатывать») is a
constitutional event handled via Part 6b stop_gate; if FUNDAMENTAL §X changes,
Pillar A docs anchored on §X enter `under-review` state automatically.

---

## §B Outputs

| Consumer | Data shape | Event published | F-G-R |
|---|---|---|---|
| Part 4 (Role Taxonomy) | `strategic-direction-published` event with `doc_type`, `doc_path`, `superseded_paths[]`, `affected_role_archetypes[]` | Per LOCKED-state strategic-doc commit | F5|G:Bundle 2 LOCKED schema|R-medium |
| Part 5 (Compound Learning) | `strategic-doc-promoted` event referencing methodology promotion candidates this doc may consume / enable | Per LOCKED + per quarterly review trigger | F4|G:Part 5 cycle integration|R-medium |
| Part 6a (Provenance Officer) | F-G-R record per strategic-doc commit; supersession chain audit trail; `prose_authored_by` trace | Per commit | F8|G:Part 6a §I.1 LOCKED schema|R-high |
| Part 6b (Human Gate) | AWAITING-APPROVAL packet for strategic-doc promotion; `gate_class: stage_gate` for F4→F5; `gate_class: stop_gate` for F5→F8 (constitutional revision) | Per promotion | F8|G:Part 6b §I.4 LOCKED|R-high |
| Part 7 (Project Lifecycle) | `pillar-a-direction-event` consumed by Pillar B alignment-check; project briefs validate `pillar_a_anchor:` ref | Per North Star / Direction Card / Phase Plan supersession | F4|G:Pillar B integration|R-medium |
| Part 8 (Health Monitoring) | Strategic-alignment SLI / strategic-doc-staleness SLI / decision-recurrence-rate SLI per Part 8 §I.1 canonical schema | Continuous emit | F4|G:Part 8 SLI consumption|R-medium |
| Part 9 (Owner Interaction Scaffold) | `strategic-doc-due-for-review` event surfacing in weekly / monthly review (Direction Card quarterly cadence; North Star annual major + quarterly soft); decisions-DB recall surfaces | Per cadence trigger | F4|G:Part 9 surface|R-medium |
| `decisions/strategic/` directory | Strategic-doc artefact files by 6 type subdirs (`lock-entries/`, `north-star/`, `strategic-insights/`, `direction-cards/`, `phase-plans/`, `strategic-reflections/`) per §I.1 schema | Per LOCKED commit | F5-F8|G:owner-authored canonical|R-high |
| `swarm/wiki/log.md` | Append-only strategic-doc-event log | Per event | F4|G:audit trail|R-medium |
| Pillar C (Principles) | Pillar A → Pillar C feedback: principle-violation-history fed back via Lock Entry promotion | Per Lock Entry commit citing Tier-1/2 rule rationale | F4|G:Pillar C integration|R-medium |

### §B.1 Concrete consequence — strategic-direction-published event surface

When a strategic doc reaches F5 LOCKED state (per Part 6a F-G-R schema), Part 11
emits `strategic-direction-published` consumed by Part 4. Part 4 inspects
`affected_role_archetypes[]` field — e.g., Direction Card "AI consulting DACH"
might affect role archetypes `sales-lead`, `sales-researcher`, `mgmt-expert`.
Part 4 routes the doc to those archetypes' working niches per Part 4 §B
Outputs. Agents in those archetypes read the new direction at next cycle plan
phase. Per FUNDAMENTAL UC-A.3 alignment enforcement.

### §B.2 Concrete consequence — quarterly Direction Card cadence emit

Direction Cards are standing direction artefacts (vs one-shot Strategic Insight
memos). Per FUNDAMENTAL §1 Categoria A and Phase 1 Q1 hierarchy resolution,
Direction Cards have quarterly review cadence. Part 11 emits
`strategic-doc-due-for-review` to Part 9 90 days after last LOCKED commit on
each Direction Card. Owner sees "Direction X due for quarterly review" in next
weekly review. Owner may: re-LOCK as-is (continued direction), supersede
(direction shift), pause (paused state), or close (direction retired).

This converts "Direction Cards drift / become decoration" anti-pattern (per
UC-A.3 «strategy without enforcement = decoration») into operational discipline.

### §B.3 Concrete consequence — decisions-DB recall on incoming question

Per UC-A.4, when a new question / задача surfaces (via Part 2 signal ingestion
or owner direct question to Part 9), Part 11 runs semantic similarity check
against decisions-DB index. If related prior decision exists with `status:
active`, Part 11 emits `decision-recall-surface` event consumed by Part 9 with
data: «You decided X on date Y for reason Z; current question is similar.
Apply, revisit, or treat as different?». Owner picks. Per FUNDAMENTAL UC-A.4
anti-recurrence mechanism («20 одинаковых решений» anti-pattern prevented).

---

## §C Side-effects

### §C.1 Strategic-doc commit triggers Part 1 §H structured commit

Every strategic doc commit follows pattern `[strategic] <doc-type> <verb> <slug>:
<rationale>` per Part 1 §H discipline. Examples:
- `[strategic] direction-card lock dach-mittelstand-ai-consulting: Q1 2026 main pursuit`
- `[strategic] north-star supersede 2026-q1-q2-financial-runway: shifted to learning-velocity primary`
- `[strategic] insight commit ai-consulting-vs-saas-tradeoff: client constraint discovery`
- `[strategic] lock-entry append D-30: agents-do-not-strategize as constitutional Tier-2 rule`

Commit format is parseable by Part 1 / Part 6a — provenance reconstruction works.

### §C.2 Lock Entry promotion may trigger Pillar C principle update

When a Lock Entry is promoted (e.g., D-30 «agents-do-not-strategize»), Part 11
emits `pillar-c-principle-candidate` event consumed by Pillar C governance.
Pillar C maintainer (Ruslan, per FUNDAMENTAL §6.2) reviews: is this Lock a new
Tier-1 manager principle, Tier-2 system principle, or remains Lock-only? If
promoted to Pillar C, principle file authored; sync lint propagates to
`.claude/config/default-deny-table.yaml` constitutional_never_list AND CLAUDE.md
inline boot-context section. This implements the Wave A "Lock-to-principle
promotion" pathway envisioned in Phase 1 Q5.

### §C.3 North Star supersession triggers project re-alignment cascade

When North Star is superseded, Part 11 emits `north-star-superseded` consumed
by Part 7. Part 7 iterates over all `activated` projects, scans
`projects/<slug>/strategy.md` Pillar B doc for `pillar_a_anchor:` ref. Each
project whose anchor was the superseded North Star enters `under-review` state
on next stage gate. Owner ack required.

This is **alignment cascade discipline** — North Star change does not silently
leave projects misaligned; cascade is mechanized.

### §C.4 Supersedes-not-corrects baseline

Per Part 6b §C.4 supersedes-not-corrects discipline + Young Reversal Transactions,
strategic-doc supersession events are NEVER edits to prior docs. Each new
direction takes the form of a new file (or new append-only entry, for Lock
Entries which are append-only ledger format). The prior doc's `status:` field
is updated from `active` to `superseded` AS A NEW APPEND-ONLY LINE in the doc's
status-history; no in-place edit of prior `status: active` line.

### §C.5 Strategic Insight memo flow to Direction Card promotion

Strategic Insight memos are event-driven (~1-2/week peak per Phase 1 corpus
analysis). When 2+ Strategic Insight memos converge on a sustained-direction
pattern, owner may promote pattern to a Direction Card. Part 11 emits
`insight-pattern-recognition` event after Insight memo commit + asks Part 9 to
surface "promote-to-direction-card?" question at next weekly review.

This implements Phase 1 dependency-graph «Type 06 → candidate-promotion → Type 07».

---

## §D Dependencies (typed A.14 edges)

Per Bundle 1 canonical 10-edge table. NO `depends-on` generic.

| Edge ID | Edge type | Target | Description |
|---|---|---|---|
| D-1 | `consumes-from` | Part 9 (Owner Interaction Scaffold) | Strategic prose authored via daily-log promotion or direct authoring; Part 11 receives owner-authored content surface |
| D-2 | `consumes-from` | Part 5 (Compound Learning) | Methodology promotion candidates + pattern surfaces feed strategic-direction inputs |
| D-3 | `consumes-from` | Part 7 (Project Lifecycle) | Project closure retrospectives feed strategic learning cycle (Pillar B → Pillar A informational backflow) |
| D-4 | `consumes-from` | Part 2 (Signal Ingestion & Triage) | External strategic-input signals classified by Part 2 land in Part 11 inbox |
| D-5 | `produces-for` | Part 4 (Role Taxonomy) | strategic-direction-published events route docs to affected role archetypes |
| D-6 | `produces-for` | Part 7 (Project Lifecycle) | pillar-a-direction-event drives Pillar B alignment-check; supersession triggers project re-alignment cascade |
| D-7 | `produces-for` | Part 8 (Health Monitoring) | Strategic-alignment SLI; decision-recurrence-rate SLI; strategic-doc-staleness SLI |
| D-8 | `produces-for` | Part 9 (Owner Interaction Scaffold) | strategic-doc-due-for-review event; decisions-DB recall surfaces |
| D-9 | `governed-by` | Part 6a (Provenance Officer) | F-G-R per strategic-doc commit; supersession chain audit trail |
| D-10 | `governed-by` | Part 6b (Human Gate) | AWAITING-APPROVAL packet for promotion (gate_class stage_gate / stop_gate); founder-only ack authority |
| D-11 | `constrained-by` | **FUNDAMENTAL §1 UC-A.1/A.2/A.3/A.4** | Strategic Management Layer use cases [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§1] |
| D-12 | `constrained-by` | **FUNDAMENTAL §6.2** | Founder-agency — strategic decisions owner-only [src:decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§6.2] |
| D-13 | `constrained-by` | **FPF IP-7** | Writing-as-thinking — owner authors strategic prose; agents draft frontmatter/structure [src:design/JETIX-FPF.md:§5.7] |
| D-14 | `constrained-by` | **Pillar C Tier-2 rule 1** | AI does NOT make strategic decisions; strategic prose `prose_authored_by` discipline [ref:principles/tier-2-system/foundation-generic/ai-does-not-strategize.md] |
| D-15 | `subordinate-of` | FUNDAMENTAL Vision LOCKED v1.0 | Per fundamental-vision-hierarchy-decision.md Option 2 — Pillar A docs elaborate FUNDAMENTAL into actionable direction; revisions cascade |
| D-16 | `governed-by` | FPF Constitutional Spec | Strategic-doc patterns conform to FPF discipline (IP-2 bounded context, IP-3 artifacts, IP-7 writing-as-thinking) |

### §D.1 Why these 16 edges and not others

- **`consumes-from` choice** for D-1 through D-4: Part 11 is downstream consumer of owner direction signal + system-internal inputs. NOT `depends-on` (banned by Bundle 1) — `consumes-from` typed correctly per A.14 canonical
- **`produces-for` choice** for D-5 through D-8: Part 11 outputs are emit-events consumed by these parts; provider-consumer typed semantic
- **`governed-by` choice** for D-9, D-10, D-16: Part 11 outputs subject to Part 6a F-G-R + Part 6b gate + FPF discipline; not consumes (these constrain rather than feed)
- **`constrained-by` choice** for D-11 through D-14: hard-constraint relationships — Part 11 design is bounded by these constitutional anchors
- **`subordinate-of` choice** for D-15: Pillar A docs elaborate FUNDAMENTAL — vertical hierarchy edge type per A.14

No `depends-on` (generic, banned). No untyped edges.

---

## §E Boundary (L/A/D/E per FPF A.6.B)

Per FPF A.6.B Boundary Norm Square [src:design/JETIX-FPF.md:§A.6.B]:

| Boundary direction | Concrete boundary |
|---|---|
| **L (Lower)** | What Part 11 will NOT pull from below. Part 11 does NOT consume project-level tactical decisions from Part 7 except via `project-retrospective-packet.json` aggregations. Part 11 does NOT directly read agent scratchpads — agent learnings reach Part 11 via Part 5 promotion |
| **A (Above)** | What Part 11 will NOT push upward. Part 11 does NOT emit constitutional revisions to FUNDAMENTAL — that is owner-authored stop_gate event (Part 6b). Part 11 does NOT mandate Pillar C principle updates — only emits candidates (§C.2) |
| **D (Down-system)** | What Part 11 enforces downward. Part 11 enforces alignment-check at Pillar B project gates (D-6); enforces supersession cascade on dependent docs; enforces append-only via Part 6a F-G-R |
| **E (External)** | What Part 11 exposes externally. Part 11 outputs to external touchpoints (Part 10) ONLY via sanitized strategic-doc-summary formats — raw strategic prose may contain RUSLAN-LAYER sensitive info per FUNDAMENTAL §6.4 privacy boundary |

### §E.1 Concrete L boundary: agent scratchpad isolation

Agents writing to `agents/<id>/scratchpad.md` may surface insights via Part 5
methodology-promotion-event. Part 11 does NOT bypass Part 5 to read scratchpads
directly. Why: Part 5 owns compound-learning curation; bypass would create
shadow-pull and undermine Part 5 discipline. If Part 11 needs scratchpad
surface, request flows through Part 5.

### §E.2 Concrete A boundary: FUNDAMENTAL revision authority

If Pillar A authoring discovers FUNDAMENTAL §X is wrong, Part 11 does NOT edit
FUNDAMENTAL. Part 11 emits constitutional-revision-candidate via Part 6b
stop_gate. Owner-only ack at Part 6b. Per Bundle 1 supplement 1+2 pattern.

### §E.3 Concrete D boundary: project alignment cascade enforcement

When North Star supersedes, Part 11 emits cascade event (§C.3). Part 7 acts on
the cascade by entering projects under-review. Part 11 does NOT directly
modify project files — Part 7 owns project state machine. Boundary respect.

### §E.4 Concrete E boundary: external sanitization

Direction Cards or Strategic Insight memos surfaced to external partners (e.g.,
mentor calls, investor pitches) MUST go through Part 10 sanitization checkpoint
per FUNDAMENTAL §6.4. Part 11 emits strategic-doc-export-candidate; Part 10
runs sanitization (RUSLAN-LAYER content scrubbed; numeric / financial /
person-specific replaced with placeholders; F-G-R adjusted to F4 external).
Mentor Brief (Phase 1 Type 14, REJECTED-FOUNDATION) is a Part 10 special case
backed by RUSLAN-LAYER fork.

---

## §F Anti-scope

Part 11 explicitly does NOT do the following. The anti-scope is constitutionally
enforced — boundaries that, if violated, would conflate Part 11 with adjacent
parts and break Wave A separation-of-concerns.

### §F.1 Part 11 does NOT author project-level strategy

Project strategy lives at `projects/<slug>/strategy.md` per Pillar B (Part 7
extension via Bundle 5 supplement). Part 11 hosts SYSTEM-WIDE direction; Part 7
hosts PROJECT-LEVEL strategy. Cross-Pillar contract: Pillar B project strategy
references Pillar A doc via `pillar_a_anchor:` frontmatter.

Anti-pattern: Direction Card containing project-execution detail. Direction
Card is direction-of-pursuit (e.g., «AI consulting for DACH Mittelstand —
2-3-month engagements / €15-50K / 3 archetypes»). Project-execution detail
(specific clients, specific deliverables, specific timelines) belongs in
project strategy.

### §F.2 Part 11 does NOT author principles

Principles authoring lives at `principles/` (Pillar C standalone Foundation
sub-system). Part 11 strategic docs **cite** principles via
`principles_compliance:` frontmatter, but do not author them.

Anti-pattern: North Star statement embedding principle text. If a North Star
makes a principle assertion (e.g., «AI does not strategize»), the principle
must already exist at Pillar C; the North Star cites it. New principles are
authored at Pillar C with Pillar A → Pillar C feedback flow per §C.2.

### §F.3 Part 11 does NOT make decisions on owner's behalf

Per FUNDAMENTAL §6.2 + Pillar C Tier-2 rule 1, agents acting on Part 11
substrate do NOT decide. Agents:
- Surface drafts for owner review
- Recall prior decisions on incoming questions
- Run alignment checks
- Emit cadence reminders

Owner ack-authority is preserved structurally. Lint check at promotion gate:
strategic doc reaching F5 LOCKED with no owner ack-trail = halt_log_alert.

### §F.4 Part 11 does NOT modify FUNDAMENTAL Vision

Per fundamental-vision-hierarchy-decision.md Option 2, Pillar A is subordinate
elaboration of FUNDAMENTAL. FUNDAMENTAL revisions are constitutional events
(Part 6b stop_gate). Part 11 emits candidate-revision events but does not
write to `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` or its successors.

### §F.5 Part 11 does NOT execute strategic actions

Strategic doc lifecycle ends at LOCKED state + cascade emission. Part 11 does
NOT spawn cycles, dispatch agents to "execute" the strategic direction, or
otherwise translate prose into action. Translation is Part 4 (Role Taxonomy
distributing direction to archetypes) + Part 7 (Project Lifecycle scoping
projects against direction). Pillar A surface; Pillar B execution.

### §F.6 Part 11 does NOT host RUSLAN-LAYER content as Foundation generic

Foundation-generic Part 11 architecture (this document) does NOT contain
Ruslan's specific Direction Cards, North Star content, Phase Plan horizons, or
Strategic Reflection text. RUSLAN-LAYER content authoring is next-sprint
workstream (per §X.X). Bundle 5 STOP discipline preserved.

### §F.7 Part 11 does NOT replace `decisions/strategic/` Phase 1 baseline

Phase 1 baseline (per `phase-1-baseline-disposition.md`) contributed 6 ADOPT
type-templates. Part 11 §I derives canonical structure from those templates +
Foundation analysis. Phase 1 templates remain as exemplar archive at
`decisions/strategic/_templates/`. Part 11 does not delete or invalidate them.

### §F.8 Part 11 does NOT name specific strategic-doc instances as Foundation

Foundation-generic = type catalogue + structural patterns + lifecycle. Specific
instances (e.g., «Top Lists Partner Factory Direction Card») are
owner-authored RUSLAN-LAYER. Per FPF IP-1 Role≠Executor: Part 11 architecture
names types, not type-instances.

### §F.9 Part 11 does NOT enforce owner-self-discipline at Tier 1

Tier 1 principles (manager / owner) are owner-self-discipline. Part 11 surfaces
Tier 1 anchors (e.g., a Direction Card may cite Tier 1 principle «long-term
thinking») but does NOT enforce. Tier 1 violation is owner self-recognition at
Strategic Reflection cadence; not gate-enforced. Per Pillar C two-tier
philosophy.

### §F.10 Part 11 does NOT host operational config

Operational config (paths, agent rosters, project lists, Notion IDs, file
conventions) lives in CLAUDE.md per claude-md-reframing-decision.md HYBRID
split. Part 11 hosts strategic direction; CLAUDE.md hosts operational config.
Anti-conflation.

---

## §G F-G-R DOGFOOD

Per Part 6a F8 schema, every Part 11 artefact carries F-G-R per `f-g-r.json`
schema. Application:

| Artefact | F (Formality) | G (Group-scope) | R (Reliability) |
|---|---|---|---|
| Lock Entry append-only ledger | F5 → F8 (constitutional Locks) | Owner + role-archetypes informed | R-high — append-only auditable |
| North Star | F4 (draft) → F5 (LOCKED) → F8 (constitutional baseline) | Owner + sanitized external (mentor) | R-high (owner-authored prose) |
| Strategic Insight memo | F2 (draft) → F4 (committed) → F5 (canonical for cycle) | Owner; selected mentor surfacing | R-medium (event-driven) |
| Direction Card | F4 → F5 (LOCKED quarterly) | Owner + mini-swarm + role archetypes | R-medium-high |
| Phase Plan | F5 (annual major) → F4 amendment | Owner + manager-archetypes | R-medium-high |
| Strategic Reflection | F5 owner-authored | Owner self-canonical | R-high (IP-7 prose) |
| Decisions-DB index entry | F4 | Owner + agents (recall consumption) | R-medium |
| `pillar_a_anchor:` ref in Pillar B docs | F-derived (matches anchored doc F) | Project-scope | R-derived |
| Cascade event (north-star-superseded) | F5 | System-internal | R-high (audit-essential) |
| Sanitized export to Part 10 | F4 (external) | External-touchpoint-scope | R-medium (sanitization audited) |

### §G.1 Promotion gates by F-grade

- **F2 → F4:** owner ack via Part 6b draft_promotion gate (or auto on commit if owner-authored from start)
- **F4 → F5:** owner ack via Part 6b stage_gate; for North Star + Phase Plan, multi-chat methodology checklist required
- **F5 → F8:** constitutional-grade promotion (rare; for Lock Entries promoted to constitutional Locks); owner ack via Part 6b stop_gate

### §G.2 R degradation triggers

Reliability degrades when:
- Strategic doc not reviewed for >cadence-period (Direction Card R-high → R-medium after 90 days unreviewed; → R-low after 180 days)
- Cited principle/anchor superseded (R automatically degraded; Part 11 emits staleness alert to Part 8)
- Multi-chat methodology checklist incomplete on North Star promotion (R-medium until methodology completed)

R degradation triggers Part 8 health alerts; Part 9 surfaces in next review.

---

## §H Code-level interfaces

### §H.1 Skills

| Skill | Purpose | Bundle 5 status |
|---|---|---|
| `/strategic-promote <type> <slug>` | Promote draft strategic doc through F2→F4→F5 with appropriate gate | Bundle 5 stub; Phase B materialization |
| `/strategic-supersede <prior-path> <new-slug>` | Author supersession; verify cascade emission | Bundle 5 stub |
| `/strategic-recall <query>` | Decisions-DB semantic recall (UC-A.4) | Bundle 5 stub; Phase B materialization |
| `/strategic-review` | Surface docs due for cadence review | Bundle 5 stub |
| `/lint --check-strategic-staleness` | Health check on strategic-doc cadences | Bundle 5 stub for Part 8 |
| `/lint --check-pillar-a-anchors` | Verify Pillar B project strategies have valid `pillar_a_anchor:` refs | Bundle 5 stub |
| `/lint --check-supersession-chain` | Verify supersession chains are consistent (no orphan supersedes) | Bundle 5 stub |

### §H.2 Configs

- `.claude/config/strategic-doc-types.yaml` — declarative 6-type catalogue with cadence + ack-discipline metadata; Foundation-generic
- `.claude/config/decisions-db-schema.yaml` — UC-A.4 decisions-DB index schema; Foundation-generic
- `principles_compliance:` frontmatter discipline (consumed at Part 11 promotion lint)
- `pillar_a_anchor:` frontmatter discipline (consumed at Part 7 Pillar B integration lint)

### §H.3 Agents involved

- `strategist` (Opus 4.6) — primary surface for Strategic Insight memo drafting + Direction Card drafting; per CLAUDE.md agent roster
- `manager` (Sonnet 4.6) — coordinates strategic-doc creation cycles
- `knowledge-synth` (Sonnet 4.6) — Brain lead; supports Pillar A by surfacing prior decisions for UC-A.4 recall
- `meta-agent` (Sonnet 4.6) — quarterly review on Direction Card cadence health
- All other agents (12-agent roster per CLAUDE.md) **consume** Pillar A direction at cycle plan phase via Part 4 routing

No agent has Pillar A authorship authority; all are draft-or-recall surfaces. Owner is sole author.

### §H.4 Part 1 §H commit substrate

Strategic-doc commits use Part 1 §H structured commit pattern:
- `[strategic] <doc-type> <verb> <slug>: <rationale>` (verbs: lock | supersede | append | review | promote | retire)

Pre-commit hook validates pattern + frontmatter completeness.

---

## §I Data schemas

### §I.1 `shared/schemas/strategic-direction-doc.json` (NEW — Bundle 5)

Authoritative schema for the 6 strategic-doc types. Foundation-generic; per-type
specializations declared in §I.2.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/strategic-direction-doc.json",
  "title": "Strategic Direction Document",
  "description": "Schema for strategic-direction artefacts hosted by Part 11 (Pillar A). Foundation-generic per Wave C Bundle 5. Specific content RUSLAN-LAYER per Phase A instance.",
  "type": "object",
  "required": [
    "doc_type", "slug", "status", "F", "G", "R",
    "constitutional_anchors", "principles_compliance", "prose_authored_by",
    "created_date", "owner_ack"
  ],
  "properties": {
    "doc_type": {
      "type": "string",
      "enum": ["lock_entry", "north_star", "strategic_insight", "direction_card", "phase_plan", "strategic_reflection"],
      "description": "One of 6 Foundation strategic-doc types per Phase 1 disposition ADOPT-INTO-PILLAR-A"
    },
    "slug": {"type": "string", "pattern": "^[a-z0-9-]+$"},
    "status": {
      "type": "string",
      "enum": ["draft", "active", "under-review", "superseded", "paused", "retired"]
    },
    "F": {"type": "string", "enum": ["F2", "F3", "F4", "F5", "F6", "F8"]},
    "G": {"type": "string"},
    "R": {"type": "string", "enum": ["R-low", "R-medium", "R-medium-high", "R-high"]},
    "constitutional_anchors": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Refs to FUNDAMENTAL Vision sections / FPF anchors"
    },
    "fpf_anchors": {"type": "array", "items": {"type": "string"}},
    "principles_compliance": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Refs to Pillar C principle docs (Tier 1 + Tier 2)"
    },
    "prose_authored_by": {
      "type": "string",
      "enum": ["ruslan", "agent-draft-pending-ack", "hybrid-with-ack-trail"],
      "description": "Per FPF IP-7 + Pillar C Tier-2 rule 1; LOCKED state must be ruslan or hybrid-with-ack-trail"
    },
    "created_date": {"type": "string", "format": "date"},
    "last_reviewed_date": {"type": "string", "format": "date"},
    "owner_ack": {
      "type": "object",
      "properties": {
        "acked_by": {"const": "ruslan"},
        "acked_date": {"type": "string", "format": "date"},
        "ack_signature": {"type": "string"}
      },
      "required": ["acked_by", "acked_date"]
    },
    "supersedes": {"type": "string", "description": "Path to prior strategic doc this one supersedes (append-only chain)"},
    "superseded_by": {"type": "string"},
    "cadence": {
      "type": "string",
      "description": "Cadence rule per type — see §I.2 per-type table"
    },
    "audience_F_G_R_flags": {
      "type": "object",
      "description": "Audience-tier flags per FPF B.3"
    },
    "decisions_db_index_entry": {
      "type": "object",
      "description": "UC-A.4 decisions-DB index payload — surfaced at recall-time"
    }
  }
}
```

### §I.2 Per-type specialization table

| doc_type | Cadence (foundation generic) | Ack authority | Promotion gate | Mandatory sections |
|---|---|---|---|---|
| `lock_entry` | append-only event-driven | Owner | stage_gate (F4→F5); stop_gate for F5→F8 | §1 Lock statement, §2 Rationale, §3 Anchors (FUNDAMENTAL/FPF/Principles), §4 Reversal-discipline, §5 Audit |
| `north_star` | annual major + quarterly soft review | Owner ONLY (multi-chat methodology) | stage_gate F4→F5 with multi-chat checklist | §1 North Star statement, §2 Horizon, §3 Constraints, §4 Anchors, §5 Cadence, §6 Anti-scope, §7 Multi-chat methodology trace |
| `strategic_insight` | event-driven (~1-2/week peak) | Owner author + Owner ack | draft_promotion F2→F4 | §1 Trigger, §2 Insight, §3 Anchors, §4 Implications, §5 Decision (if any), §6 Provenance |
| `direction_card` | quarterly review + event-driven status | Owner + agents informed | stage_gate F4→F5 | §1 Direction statement, §2 Pursuit boundary, §3 Constraints, §4 Anchors (must cite Pillar A parent), §5 Status (active/paused/retired), §6 Cadence, §7 Pillar B alignment expectations |
| `phase_plan` | annual major + event-driven amendment | Owner + manager-archetype mini-swarm informed | stage_gate F4→F5 | §1 Phase boundary (start/end conditions), §2 Phase goals, §3 Phase constraints, §4 Anchors, §5 Phase 1 → Phase 2 transition predicate, §6 Phase health metrics |
| `strategic_reflection` | annual major + quarterly review | Owner ONLY (IP-7 writing-as-thinking) | direct F5 commit | §1 Period reflected on, §2 What worked, §3 What didn't, §4 Patterns, §5 Direction implications, §6 Decisions surfaced |

### §I.3 Decisions-DB index schema (`shared/schemas/decisions-db.json` — Bundle 5)

Per UC-A.4. Lightweight, lint-enforceable, semantic-recall-able.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/decisions-db.json",
  "title": "Decisions DB Index Entry",
  "type": "object",
  "required": ["decision_id", "what", "when", "by_whom", "based_on", "status", "scope", "connection"],
  "properties": {
    "decision_id": {"type": "string", "pattern": "^D-[0-9]+$"},
    "what": {"type": "string", "description": "Concise statement of decision"},
    "when": {"type": "string", "format": "date-time"},
    "by_whom": {
      "type": "string",
      "enum": ["ruslan", "ruslan-via-multi-chat", "agent-draft-ruslan-acked"],
      "description": "Per FUNDAMENTAL §6.2 founder-agency"
    },
    "based_on": {
      "type": "object",
      "properties": {
        "context": {"type": "string"},
        "sources": {"type": "array", "items": {"type": "string"}},
        "reasoning": {"type": "string"},
        "data": {"type": "string"}
      }
    },
    "status": {
      "type": "string",
      "enum": ["active", "superseded", "reversed", "paused", "under-review"]
    },
    "scope": {
      "type": "object",
      "properties": {
        "level": {
          "type": "string",
          "enum": ["constitutional", "strategic", "project", "tactical", "personal", "operational"]
        },
        "affected_parts": {"type": "array", "items": {"type": "string"}},
        "external_commitments": {"type": "boolean"}
      }
    },
    "connection": {
      "type": "object",
      "properties": {
        "anchored_strategic_docs": {"type": "array", "items": {"type": "string"}},
        "derived_from_decisions": {"type": "array", "items": {"type": "string"}},
        "contradicts_decisions": {"type": "array", "items": {"type": "string"}},
        "extended_by_decisions": {"type": "array", "items": {"type": "string"}}
      }
    },
    "lock_candidate": {"type": "boolean", "description": "If true, candidate for Lock Entry promotion per D27 evolution discipline"}
  }
}
```

### §I.4 `.claude/config/strategic-doc-types.yaml` (NEW — Bundle 5)

Declarative type catalogue with cadence + ack-discipline metadata.

```yaml
foundation_generic:
  schema_version: 1.0
  default_ack_authority: ruslan  # founder-only per FUNDAMENTAL §6.2 — single-owner Phase A
  doc_types:
    lock_entry:
      cadence: append_only_event_driven
      promotion_gates: [draft_promotion, stage_gate, stop_gate]
      mandatory_sections: [statement, rationale, anchors, reversal_discipline, audit]
      multi_chat_required: false
    north_star:
      cadence: annual_major_plus_quarterly_soft
      promotion_gates: [draft_promotion, stage_gate]
      mandatory_sections: [statement, horizon, constraints, anchors, cadence, anti_scope, multi_chat_trace]
      multi_chat_required: true
    strategic_insight:
      cadence: event_driven
      typical_frequency: 1_to_2_per_week_peak
      promotion_gates: [draft_promotion]
      mandatory_sections: [trigger, insight, anchors, implications, decision, provenance]
      multi_chat_required: false
    direction_card:
      cadence: quarterly_review_plus_event_driven_status
      promotion_gates: [draft_promotion, stage_gate]
      mandatory_sections: [statement, pursuit_boundary, constraints, anchors, status, cadence, pillar_b_alignment]
      multi_chat_required: false
    phase_plan:
      cadence: annual_major_plus_event_driven_amendment
      promotion_gates: [draft_promotion, stage_gate]
      mandatory_sections: [phase_boundary, goals, constraints, anchors, transition_predicate, health_metrics]
      multi_chat_required: false
    strategic_reflection:
      cadence: annual_major_plus_quarterly_review
      promotion_gates: [direct_F5]
      mandatory_sections: [period, what_worked, what_didnt, patterns, direction_implications, decisions_surfaced]
      multi_chat_required: false
      ip7_writing_as_thinking: true

ruslan_layer_overrides:
  instance_id: jetix-phase-a-single-owner
  ack_authority_principal: ruslan
  cadence_value_overrides:
    direction_card_quarterly_review_days: 90
    north_star_annual_major_months: 12
    strategic_reflection_annual_period: "calendar_year"
  multi_chat_methodology_session_count: 5
  # Specific instances populated as authored:
  active_north_star_path: null  # Layer 2 next sprint
  active_phase_plan_path: "decisions/JETIX-PLAN.md"  # current Phase 1
  active_direction_cards: []  # Layer 2 next sprint
```

### §I.5 Pillar A frontmatter excerpt template (Foundation generic)

```yaml
---
title: "<doc-title>"
date: <YYYY-MM-DD>
doc_type: <one of 6 enum>
slug: <kebab-case>
status: draft | active | under-review | superseded | paused | retired
F: F2 | F3 | F4 | F5 | F6 | F8
G: <group-scope description per FPF B.3>
R: R-low | R-medium | R-medium-high | R-high
constitutional_anchors:
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (§...)
fpf_anchors: []
principles_compliance:
  - principles/tier-2-system/foundation-generic/<rule>.md
  - principles/tier-1-manager/<value>.md
prose_authored_by: ruslan | agent-draft-pending-ack | hybrid-with-ack-trail
created_date: <YYYY-MM-DD>
last_reviewed_date: <YYYY-MM-DD>
owner_ack:
  acked_by: ruslan
  acked_date: <YYYY-MM-DD>
supersedes: <prior-path or null>
superseded_by: <path or null>
cadence: <cadence rule per type>
multi_chat_methodology_trace: <required if doc_type=north_star, else null>
decisions_db_index_entry:
  decision_id: D-<NN>
  scope:
    level: strategic
    affected_parts: [<part-id>...]
---
```

---

## §J Operational rituals

### §J.1 Strategic doc creation cycle (generic)

1. **Trigger.** Owner direction signal (insight / question / pattern surfaced from Part 5 / external event from Part 2 / cadence reminder from §B.2)
2. **Type selection.** Owner (or agent surface) determines which of 6 doc types applies (see §I.2)
3. **Drafting.** Agent drafts frontmatter + structural skeleton; owner authors prose (per FPF IP-7 + `prose_authored_by` discipline)
4. **Anchors + principles citations.** Owner cites: constitutional anchors (FUNDAMENTAL / FPF) + Pillar C principles_compliance + cross-refs (prior decisions; cited Direction Card if subordinate)
5. **F2 commit.** Draft committed at F2 / G:draft / R-low per Part 1 §H structured commit
6. **Cadence-as-required gates.** For North Star: multi-chat methodology session loop (5-chat per Phase 1 Q3 + RUSLAN-LAYER override); for others: single-session draft promotion may suffice
7. **F2 → F4 promotion.** Owner ack via Part 6b draft_promotion gate
8. **F4 → F5 promotion (LOCKED).** Owner ack via Part 6b stage_gate; stage-gate predicate Hamel-binary verifies completeness
9. **Cascade emission.** Per §B / §C, supersession events emitted to consumers
10. **Decisions-DB indexing.** UC-A.4 index entry created/updated; semantic-recall index refreshed

### §J.2 Cadence reminder ritual

For Direction Cards (quarterly): Part 11 emits `strategic-doc-due-for-review`
to Part 9 every 90 days post-LOCK. Owner sees in next weekly review per Part 9
intake. Owner action: re-LOCK / supersede / pause / retire.

For North Star (annual major + quarterly soft): annual reminder emits at year
boundary; quarterly soft reminders emit at quarter boundaries. Quarterly soft
reminder asks: «North Star aligned with current direction? Or supersede?».

For Phase Plan: amendment-event-driven (no calendar cadence; reactivated when
Phase transition predicate triggers per §I.2 mandatory section §5).

For Strategic Reflection: annual + quarterly cadence; emits at calendar
boundary (per RUSLAN-LAYER override).

For Strategic Insight memos: NO cadence reminder (event-driven only); but
meta-pattern check at Direction Card quarterly review: «do recent Insight
memos suggest Direction shift?».

For Lock Entries: NO cadence reminder (append-only event-driven); but Lock
Entries are reviewed at quarterly Strategic Reflection (per Phase 1 hierarchy).

### §J.3 Multi-chat methodology for North Star (Foundation discipline)

Per Phase 1 Q3 + Ruslan «multi-chat для critical strategic docs». Foundation-generic
discipline: critical strategic docs (specifically North Star at Foundation level;
RUSLAN-LAYER may extend to Phase Plan / specific Direction Cards) require
multi-session drafting trace. Foundation-generic structure:

| Session | Purpose | Output checklist item |
|---|---|---|
| 1 (primary) | Initial direction articulation; what is the North Star? | Statement draft + initial anchors |
| 2 (zoom-in) | Constraints + anti-scope; what is NOT the North Star? | Anti-scope section + constraint enumeration |
| 3 (zoom-out) | Cross-Pillar + Cross-Part implications | Pillar B alignment expectations + Part-cascade map |
| 4 (epistemic-discipline) | First-principles check; is this rationally grounded? | Rationale prose + counter-arguments addressed |
| 5 (integrative critic + ack) | Multi-session synthesis review + final ack | Final North Star + multi_chat_methodology_trace populated |

Foundation generic = the 5-session structure + checklist mandate. RUSLAN-LAYER
specifies session-naming, calendar timing, specific external mentor inclusion.

### §J.4 Decisions-DB recall ritual

When new question / задача surfaces:
1. Part 2 (Signal Ingestion) classifies as candidate for decisions-DB recall (semantic-similarity check at classification time)
2. Part 11 runs UC-A.4 recall: index search returns top-N matched prior decisions with status `active`
3. If matches exist → Part 9 surfaces «similar decision exists; revisit / apply / treat as new?»
4. Owner picks. If revisit → enter `under-review`. If apply → reference existing decision. If new → proceed to draft.

### §J.5 Lock-to-principle promotion ritual

Lock Entry promoted (e.g., D-30 «agents-do-not-strategize»). Part 11 emits
`pillar-c-principle-candidate` to Pillar C governance. Owner reviews:
- Is this a Tier 1 principle (manager value)? → author at `principles/tier-1-manager/<slug>.md`
- Is this a Tier 2 principle (system rule)? → author at `principles/tier-2-system/{foundation-generic|ruslan-layer-overrides}/<slug>.md`
- Is this Lock-only (instance-specific governance, not principle)? → remain Lock Entry only

If promoted to Pillar C, sync lint propagates to `.claude/config/default-deny-table.yaml`
constitutional_never_list (if Tier 2 Foundation generic) AND CLAUDE.md inline boot-context
(per claude-md-reframing-decision.md).

---

## §K Failure modes

### §K.1 K1 — Strategic doc drift (no enforcement → decoration)

**Failure.** Direction Card LOCKED 6 months ago; owner has shifted direction
informally; project strategies still anchor on stale Direction Card; cascade
never fired because Direction Card was never explicitly superseded.

**Mitigation.**
- §B.2 cadence reminder fires at 90 days post-LOCK
- §G.2 R degradation triggers Part 8 staleness alert at 90 / 180 days
- Strategic Reflection cadence at quarter boundary surfaces «is Direction X still active?»
- Multi-source check: project strategies referencing this Direction Card may show contradictory state per Part 7 alignment-check; emits alert

### §K.2 K2 — Owner ack-skip (LOCKED state without genuine engagement)

**Failure.** Owner clicks "ack" on agent-drafted strategic doc without genuine
cognitive engagement. `prose_authored_by: hybrid-with-ack-trail` set; doc reaches
F5 LOCKED; substance is agent-derivative.

**Mitigation.**
- IP-7 writing-as-thinking enforcement: owner must edit prose at least N% before LOCK (Foundation generic principle; RUSLAN-LAYER specifies %)
- `time_to_review_seconds` Part 6b anti-pattern signal flags review <60s for L1 strategic docs
- Multi-chat methodology mandate for North Star adds friction
- Strategic Reflection cadence surfaces «which direction docs feel agent-derivative?» (self-recognition)

### §K.3 K3 — Decisions-DB recall miss (semantic similarity threshold misaligned)

**Failure.** New question surfaces; semantically similar prior decision exists
but recall similarity-threshold misses it; owner re-decides anti-pattern
violated.

**Mitigation.**
- Threshold tuning: false-negative rate tracked as Part 8 SLI
- Manual recall option: `/strategic-recall <free-text>` skill for owner-initiated search
- Quarterly Strategic Reflection includes «what decisions did I re-make this quarter?» — manual surfacing
- N-best returned (not top-1) so owner can scan candidates

### §K.4 K4 — Cascade non-firing (supersession event missed)

**Failure.** North Star superseded; cascade event fails to emit (e.g., commit
hook bug); dependent project strategies remain anchored to superseded doc.

**Mitigation.**
- Part 8 invariant SLI: `count(active strategic docs) - count(emitted cascade events for superseded docs) == 0` post-supersession
- `/lint --check-supersession-chain` skill verifies chain consistency on commit
- Manual replay: `/strategic-cascade-replay <superseded-path>` skill for recovery

### §K.5 K5 — Premature LOCK on critical doc (multi-chat methodology bypassed)

**Failure.** North Star LOCKED in single session; multi-chat methodology
checklist marked complete falsely.

**Mitigation.**
- Multi-chat methodology checklist requires 5 distinct session_ids (timestamp gaps verified)
- Lint at promotion: `multi_chat_methodology_trace` field validated against doc_type=north_star requirement
- `prose_authored_by` audit trail shows session distribution

### §K.6 K6 — Cross-Pillar contradiction (Pillar B project strategy contradicts Pillar A direction)

**Failure.** Project strategy cites Pillar A Direction Card; project then
operates contrary to that direction.

**Mitigation.**
- Part 7 stage gate at `under-review` runs Pillar A alignment-check predicate
- If project retrospective surfaces contradiction → emits `pillar-a-direction-tension` event to Part 11
- Strategic Reflection surfaces tensions for owner resolution
- Direction Card supersession option: Direction was wrong, project was right

### §K.7 K7 — Constitutional revision risk (Pillar A enabled de-facto FUNDAMENTAL change)

**Failure.** Pillar A docs accumulate that contradict FUNDAMENTAL §X without
formal §X revision. De-facto constitutional change without stop_gate.

**Mitigation.**
- Pillar A frontmatter `constitutional_anchors:` field; if anchored §X is contradicted, lint flags
- Part 6a §F.3 anchor-staleness check
- FUNDAMENTAL revision is constitutional event (Part 6b stop_gate); Pillar A drift detected as anchor-contradiction trigger

### §K.8 K8 — RUSLAN-LAYER content leakage to Foundation

**Failure.** Pillar A architecture (this document) accumulates Ruslan-specific
content over time (e.g., specific Direction Card content embedded as
Foundation-generic example).

**Mitigation.**
- Foundation vs RUSLAN-LAYER §X strict per Bundle 5 quality bar
- Cross-Bundle critic gate at Wave E LOCKED tag (TODO post-ack)
- Fork-portability test: a Phase B fork-importer should be able to take Part 11 architecture + delete `decisions/strategic/` content + start authoring own RUSLAN-LAYER

### §K.9 K9 — Strategic doc authoring blocked by gate friction

**Failure.** Multi-chat methodology + LOCKED ack + stage_gate friction
disincentivizes owner from authoring strategic docs; system reverts to ad-hoc.

**Mitigation.**
- Cadence is event-driven (not calendar-forced) for Insight memos + Lock Entries — low friction
- Multi-chat methodology only required for North Star (annual major); other types lighter
- Direction Card cadence is quarterly-review (not quarterly-rewrite); soft cadence
- Strategic Insight at draft stage F2 has minimal gate (auto-promote via Part 6b draft_promotion)

### §K.10 K10 — Decisions-DB unbounded growth

**Failure.** Every minor decision logged; index grows to 10K entries; recall
becomes noisy; semantic-similarity computation expensive.

**Mitigation.**
- UC-A.4 lightweight discipline: 1-2 lines per decision; not bureaucracy
- Decisions level field (`constitutional / strategic / project / tactical / personal / operational`) — recall scope-filtered by default
- Operational + tactical decisions have R-low; aged-out from active recall after configurable period (RUSLAN-LAYER)
- Index segmentation: per-level, per-time-period

### §K.11 K11 — Strategic Insight memo accumulation without promotion-to-Direction

**Failure.** Strategic Insights accumulate (5+ over 30 days) on a sustained
direction theme; pattern not surfaced; potential Direction Card not authored.

**Mitigation.**
- Part 5 compound-learning emits `pattern-cluster-detected` for clusters of N+ Insight memos on similar topic over time-window
- Part 9 surfaces «promote to Direction Card?» at next weekly review
- Strategic Reflection cadence forces owner self-recognition

---

## §L Bundle 5 work-list

| ID | Task | Status |
|---|---|---|
| L1 | Part 11 architecture document | DRAFT (this document) |
| L2 | `shared/schemas/strategic-direction-doc.json` schema | SPECIFIED §I.1; physical file Phase B |
| L3 | `shared/schemas/decisions-db.json` schema | SPECIFIED §I.3; physical file Phase B |
| L4 | `.claude/config/strategic-doc-types.yaml` | SPECIFIED §I.4; physical file Bundle 5 ack-then-create |
| L5 | `decisions/strategic/` directory restructure (6 type subdirs) | Bundle 5 ack-then-create |
| L6 | `/strategic-promote`, `/strategic-supersede`, `/strategic-recall`, `/strategic-review` skills | Phase B materialization |
| L7 | `/lint --check-strategic-staleness`, `/lint --check-pillar-a-anchors`, `/lint --check-supersession-chain` | Phase B materialization |
| L8 | Pillar B alignment-check predicate in Part 7 supplement | Bundle 5 (Pillar B architecture; sibling work) |
| L9 | Pillar C principles_compliance frontmatter discipline | Bundle 5 (Pillar C architecture; sibling work) |
| L10 | CLAUDE.md HYBRID re-frame (split + sync lint) | Bundle 5 architecture done; Layer 2 content authoring next sprint |
| L11 | Multi-chat methodology session-trace schema | Bundle 5 §J.3 specified; physical file Phase B |
| L12 | Decisions-DB semantic-recall implementation | Phase B materialization |
| L13 | Pillar A → Pillar C principle-candidate-promotion event | Bundle 5 §C.2 specified; cross-Pillar contract |
| L14 | RUSLAN-LAYER strategic-doc content authoring (Direction Cards, North Star, etc.) | Layer 2 next sprint (NOT Bundle 5) |

---

## §M Wisdom Application Findings

Per Bundle 5 §5 Wisdom Loop discipline. OPERATIONAL/PHILOSOPHICAL discriminator
applied. Target ≥85% operational ratio.

| # | Card | Principle | Current state | Improvement | Adopted? | O/P | Justification |
|---|---|---|---|---|---|---|---|
| 1 | Capital Allocation Annual Letters (Buffett) | Annual letters as direction-clarification ritual | Strategic Reflection §I.2 | Annual major + quarterly review cadence; force-function for direction-coherence prose | YES | OPERATIONAL | Mandates writing cadence, structural format. Foundation-generic |
| 2 | Capital Allocation Munger Inversion | Inversion: «what would make this direction wrong?» | Direction Card §3 Constraints + §6 Cadence | Direction Card mandatory section §3 Constraints + Anti-scope. Inversion-prompt at quarterly review | YES | OPERATIONAL | Operationalized as mandatory section + ritual prompt |
| 3 | PM Cagan Empowered Teams | Strategic vs delivery decisions split — strategic upstream of delivery | §F.1 Pillar A vs Pillar B boundary; D-6 produces-for Part 7 | Pillar A direction informs Pillar B project strategy; alignment-check predicate enforced | YES | OPERATIONAL | Cross-Pillar contract; alignment-check is structural |
| 4 | Cagan North Star Metric | NSM as singular metric direction | North Star §I.2 mandatory sections | Foundation-generic structure adopted; RUSLAN-LAYER specifies metric | YES | OPERATIONAL | Doc type slot established; content RUSLAN-LAYER |
| 5 | Stoic-Epistemic Naval | Specific knowledge filter | §I.2 Direction Card Mandatory §1 Direction statement specificity | Direction-not-vague predicate applied at lint | PARTIAL | OPERATIONAL | Lint stub L7 addresses; full predicate Phase B |
| 6 | Stoic-Epistemic Holiday Obstacles-Way | Reframing direction-shift as growth | Strategic Reflection §I.2 mandatory §3 What didn't | Reflection ritual surfaces shifts as learning | YES | PHILOSOPHICAL | Cadence ritual creates space; doesn't mandate prose |
| 7 | Stoic-Epistemic Munger Mental Models | Mental models cited at strategic doc anchors | §I.5 frontmatter `principles_compliance` + `constitutional_anchors` | Pillar C principles ref mandatory; Munger inversion as principle | YES | OPERATIONAL | Citation discipline structural |
| 8 | Levenchuk IP-7 Writing-as-Thinking | Owner authors strategic prose | §A.1 + §I.5 prose_authored_by + §K.2 mitigation | Foundation generic; Tier 2 rule 1 enforcement | YES | OPERATIONAL | `prose_authored_by` field + lint rejection on agent-pending |
| 9 | Levenchuk IP-2 Bounded Context | Single-owner Phase A scope | Frontmatter ip2_single_owner_bounded; D-12 founder-agency | F.9 Bridge structural change at Phase B | YES | OPERATIONAL | Scope boundary explicit |
| 10 | Levenchuk IP-3 Artifacts Over Conversations | Strategic docs as artifacts; no chat-only | §C.1 commit substrate; §I schema discipline | All Pillar A outputs are committed artifacts | YES | OPERATIONAL | Implicit constitutional |
| 11 | Anthropic CAI Hardcoded Never-list | Constitutional 11 hard rules upstream of strategic direction | Pillar C consumption (D-14); Lock-to-Pillar-C promotion (§C.2) | Strategic direction doesn't override constitutional; Pillar C constrains | YES | OPERATIONAL | Lock-to-principle ritual specified |
| 12 | Anthropic Askell HHH | Helpfulness/Harmlessness/Honesty triad | Pillar C Tier 2 informed; not directly Pillar A | (deferred to Pillar C architecture) | DEFERRED | — | Lives in Pillar C |
| 13 | Compounding Engineering R2 Reinforcing | Strategic-doc compound learning loop | D-2 consumes-from Part 5 | Methodology promotion candidates feed direction | YES | OPERATIONAL | Cross-Part feed established |
| 14 | Compounding Engineering DRR | Decision-Result-Rationale per cycle | UC-A.4 decisions-DB §I.3 schema | Decisions DB is DRR substrate | YES | OPERATIONAL | Schema embeds DRR fields |
| 15 | Multi-agent Architecture Coordinator | Hub-and-spoke for direction routing | D-5 produces-for Part 4 | Direction events route to role archetypes | YES | OPERATIONAL | Cross-Part contract |
| 16 | Multi-agent Architecture Mailbox | Async strategic events | Part 4 / Part 9 mailbox consumption | Direction events emitted async | YES | OPERATIONAL | Implicit Bundle 2/4 LOCKED |
| 17 | Buffett Owner-Earnings Genre | Owner perspective on strategic clarity | Strategic Reflection IP-7; Direction Card from owner pursuit | Genre conventions align with Foundation discipline | YES | PHILOSOPHICAL | Genre informs prose style; not gate-enforced |
| 18 | Marks Memos Pattern-Recognition | Insight memos as pattern recognition (Marks genre) | Strategic Insight Memo §I.2 | Doc type adopted; 5 corpus exemplars validate | YES | OPERATIONAL | Doc type slot established |
| 19 | Singer Shape Up Appetite | Appetite-as-CONSTRAINT belongs in Pillar B | (cross-Pillar boundary at §F.1) | Bet Pitch routed to Pillar B per Phase 1 disposition | YES | OPERATIONAL | Boundary respect |

**Operational ratio:** 16 OPERATIONAL + 2 PHILOSOPHICAL + 1 DEFERRED = 16/18 of
adopted = 88.9% — exceeds ≥85% target.

**1 DEFERRED is appropriate**: Anthropic Askell HHH belongs in Pillar C
architecture; Pillar A integration via principles_compliance ref to Pillar C.

---

## §N Provenance

### §N.1 Constitutional anchors
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0): §0 (two-layer pattern), §1 Categoria A (UC-A.1, A.2, A.3, A.4), §6.2 (founder-agency), §6.4 (privacy boundary), §6.1 (constitutional 11 hard rules — derived to Pillar C Tier 2)
- `design/JETIX-FPF.md`: §5.7 IP-7 writing-as-thinking; §5.2 IP-2 bounded context; §5.3 IP-3 artifacts; §B.3 F-G-R; §A.6.B Boundary Norm Square; §A.14 typed edges (10 canonical types)

### §N.2 Decision artefacts (Bundle 5)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/structural-placement-decision.md`
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/fundamental-vision-hierarchy-decision.md`
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/claude-md-reframing-decision.md`
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/phase-1-baseline-disposition.md`

### §N.3 LOCKED Foundation parts consumed
- Part 1 architecture (§H commit substrate); Part 2 (signal classification); Part 4 (role archetype routing); Part 5 (compound learning input); Part 6a (F-G-R); Part 6b (gate_class enum); Part 7 (Pillar B integration target); Part 8 (SLI emission); Part 9 (owner reflection input + cadence surface); Part 10 (sanitization for external)

### §N.4 Phase 1 baseline (INPUT)
- `decisions/AWAITING-APPROVAL-strategic-layer-templates-2026-04-28.md`
- `decisions/strategic/_research/landscape-strategic-docs-2026-04-28.md`
- `decisions/strategic/_research/jetix-fit-filtering-2026-04-28.md`
- `decisions/strategic/_research/hierarchy-cadences-2026-04-28.md`
- `decisions/strategic/_templates/*.md.template` (7 templates as exemplar reference for 6 ADOPT-INTO-PILLAR-A types)

### §N.5 Wave A artefacts
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md`
- `candidate-parts-merged.md` (10-part decomposition)
- `dependency-graph.md` (Pillar A as new producer/consumer node)

### §N.6 Wave B consultant cards (relevant)
- `consultants/levenchuk-shsm-fpf.md` (IP-7, IP-2, IP-3, B.3 F-G-R)
- `consultants/product-management-cagan-shape-up.md` (Cagan + Shape Up + Torres)
- `consultants/stoic-epistemic.md` (Naval / Holiday / Munger)
- `consultants/capital-allocation-antifragility.md` (Buffett annual letters, Munger inversion, Marks memos)
- `consultants/anthropic-constitutional-ai.md` (Bai 2022 + Askell 2021 HHH)
- `consultants/compounding-engineering.md` (R2 + DRR)
- `consultants/multi-agent-architecture.md` (coordinator + mailbox)

### §N.7 Wave B Supplement library-direct sources
- `raw/books-md/anthropic/bai-2022-cai.md` (constitutional structure)
- `raw/books-md/anthropic/askell-2021-hhh.md` (Pillar C deferred)
- `raw/books-md/event-sourcing/young-cqrs-2010.md` (Reversal Transactions for §C.4)

### §N.8 Memory references
- `feedback_strategic_layer_is_foundation_level` (28.04 evening Ruslan correction — basis of Bundle 5 cycle)
- `feedback_no_solo_founder_downgrade` (preserved via Capital Memo DEFER not SKIP per Phase 1 disposition)
- `feedback_ai_does_not_strategize` (Pillar C Tier 2 rule 1, enforced via prose_authored_by discipline)
- `methodology_multi_chat_review_for_critical_docs` (preserved via §J.3 multi-chat methodology Foundation discipline)
- `project_jetix_hybrid_framework_vision` (Layer 2 next sprint — Founder Overlay)

---

## §X Foundation vs RUSLAN-LAYER strict separation

### §X.1 Foundation generic (this document — Part 11 architecture)

What is constitutionally Foundation-level — fork-portable; any Jetix instance imports unchanged:

- **Strategic-doc type catalogue (6 types)**: Lock Entry, North Star, Strategic Insight, Direction Card, Phase Plan, Strategic Reflection — derived from generic strategic-management theory + Phase 1 5-corpus-exemplar evidence + 7-card Wave B framework anchors
- **Per-type structure**: mandatory sections (§I.2), cadence rules, ack discipline, promotion gate types
- **F-G-R schema** application to strategic docs (§G)
- **Append-only via supersession** discipline (§A.2 + §C.4)
- **FUNDAMENTAL hierarchy contract** (Option 2 subordinate elaboration)
- **Cross-Pillar integration contracts**: Pillar A → Pillar B (D-6 produces-for Part 7); Pillar A → Pillar C (D-14 constrained-by Pillar C; §C.2 promotion candidate); Pillar A ← Pillar C (principles_compliance citation)
- **Decisions-DB schema (UC-A.4)**: index entry, scope levels, status enum, semantic recall pattern (§I.3)
- **Multi-chat methodology** Foundation discipline: 5-session structure for North Star (specific session timing = RUSLAN-LAYER)
- **Cascade emission discipline**: supersession events to dependent parts (§C.3); cadence reminders (§B.2)
- **`prose_authored_by` discipline**: Foundation enforcement of FPF IP-7 + Pillar C Tier-2 rule 1 (§A.1)
- **Anti-scope (§F)**: 10 anti-scope clauses as constitutional boundaries
- **Failure modes (§K)**: 11 failure-mode patterns with Foundation-generic mitigations
- **Dependency edges (§D)**: 16 typed A.14 edges to Foundation parts + constitutional anchors
- **Skill stubs (§H.1)**: Foundation-generic skill names + purposes; per-instance implementation Phase B

### §X.2 RUSLAN-LAYER (next sprint — NOT in Bundle 5 scope)

What is Ruslan-specific — every fork-importer authors their own:

- **Specific North Star content** (e.g., what Ruslan's North Star is for 2026)
- **Specific Direction Cards content** (e.g., «Top Lists Partner Factory», «AI Consulting DACH Mittelstand», «Quick-Money €50K target Phase 1»)
- **Specific Phase Plan content** (e.g., Phase 1 €50K Q2 2026 → Phase 2 transition predicates)
- **Specific Strategic Insight memo content** (5 existing exemplars; ongoing event-driven)
- **Specific Lock Entry content** (existing D-1 through D-29; new ones per evolution)
- **Specific Strategic Reflection content** (annual / quarterly retrospectives)
- **Specific cadence values**: how many days between reviews; how many sessions in multi-chat (Foundation-generic = 5; RUSLAN-LAYER may override)
- **Specific multi-chat methodology session-naming**: Phase 1 §1+§2 / §3+§4 / §5 etc are RUSLAN-LAYER; Foundation-generic is the 5-session structure
- **Specific decision-recall similarity threshold**: tunable per instance
- **Specific R-degradation timing**: 90/180-day windows are RUSLAN-LAYER (Foundation-generic = staleness-cadence-rule pattern)
- **Specific principles cited as compliance anchors**: any specific principle is RUSLAN-LAYER content; Foundation-generic is the citation discipline
- **Specific external-touchpoint sanitization rules per stakeholder type**: Mentor Brief is REJECT-FOUNDATION (Phase 1 Type 14); RUSLAN-LAYER fork

### §X.3 Fork-portability test

A Phase B fork-importer (e.g., scientific researcher applying Jetix-methodology
to medical research) takes Part 11 architecture (this doc) + deletes
`decisions/strategic/<type>/*` content + starts authoring own RUSLAN-LAYER:
- Imports the 6 doc-type catalogue unchanged
- Imports cadence rules, ack discipline, promotion gates unchanged
- Imports `strategic-direction-doc.json` schema unchanged
- Imports `decisions-db.json` schema unchanged
- Imports `strategic-doc-types.yaml` foundation_generic stanza unchanged
- Replaces `ruslan_layer_overrides:` stanza with own instance overrides
- Authors own North Star (medical research direction)
- Authors own Direction Cards (e.g., «Cardiology AI diagnostics», «Surgical workflow optimization»)
- Authors own Phase Plan (research grant cycle)
- Authors own Lock Entries (research-ethics governance Locks)

This Phase B fork inherits Foundation generic; authors RUSLAN-LAYER (renamed
to `medical-researcher-layer-overrides:`). Direct test of fork-portability.

### §X.4 What is structurally enforced as Foundation-generic

Lint rules (Phase B materialization) enforce X.1 vs X.2 boundary:

| Lint rule | Enforces |
|---|---|
| `--check-no-instance-content-in-architecture` | Part 11 architecture document does not embed specific Direction Card content |
| `--check-foundation-generic-section-discipline` | Part 11 §X.1 enumeration matches actual Foundation generic content |
| `--check-no-ruslan-layer-leakage` | RUSLAN-LAYER overrides only in `ruslan_layer_overrides:` stanza of YAMLs |
| `--check-pillar-a-frontmatter-completeness` | Strategic doc instances populate Foundation-required frontmatter |

---

*End of Part 11 architecture. ~12K words. Structural placement: NEW Foundation
Part 11 — Strategic Direction Substrate. Pillar A canonical. Foundation-generic;
RUSLAN-LAYER content authoring next sprint (Layer 2). AWAITING-APPROVAL —
gates Wave E LOCKED tag.*
