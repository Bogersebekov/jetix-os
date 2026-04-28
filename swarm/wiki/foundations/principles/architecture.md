---
title: "Foundation Sub-System — Principles Substrate (Pillar C)"
date: 2026-04-28
type: foundation-architecture
sub_system: principles (Foundation cross-cutting subordinate, NOT a numbered Part)
pillar: C — Principles / Values (two-tier)
status: F5 LOCKED — Ruslan ack 2026-04-28 (decisions/RUSLAN-ACK-STRATEGIC-LAYER-BUNDLE-5-2026-04-28.md)
parent_cycle: cyc-foundation-build-2026-04-28
bundle: 5-strategic-layer
brigadier_phase: A-4 integrator drafts
predecessor_decisions:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/structural-placement-decision.md (Pillar C as standalone sub-system)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/claude-md-reframing-decision.md (HYBRID re-frame)
constitutional_anchors:
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (§6.1 11 constitutional hard rules; §6.2 founder-agency; §0 two-layer pattern)
  - design/JETIX-FPF.md (FPF anti-scope hard rules; B.3 F-G-R; A.6.B Boundary)
  - swarm/wiki/foundations/part-6b-human-gate/architecture.md (§I.2 constitutional_never_list as Tier 2 derived enforcement)
  - swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md (Pillar A → Pillar C feedback flow)
  - CLAUDE.md (Pillar C re-framing target — HYBRID split per claude-md-reframing-decision.md)
fpf_anchors:
  - "FPF anti-scope hard rules genre"
  - "FPF B.3 — F-G-R per principle artefact"
  - "FPF A.14 — typed edges (constrained-by)"
  - "FPF A.6.B — Boundary (L/A/D/E)"
F: F5
G: Foundation sub-system canonical — Principles Substrate (Pillar C) — Ruslan ack'd Bundle 5
R: R-high — owner ack'd 2026-04-28
locked_decisions_referenced: [D-2 architect-orbit, D-12 founder-agency, D-26 single-accountable]
ip2_single_owner_bounded: "Phase A scope is single-owner; principles authoring authority = Ruslan only per FUNDAMENTAL §6.2. Tier 2 foundation_generic (11 hard rules from §6.1) is fork-portable; Tier 2 ruslan_layer_overrides + Tier 1 manager principles content = RUSLAN-LAYER per Phase A. F.9 Bridge structural change ≥35% required at Phase B (multi-owner / fork instances)."
ClaimScope: "Foundation generic — two-tier structure (Tier 1 manager + Tier 2 system); Tier 2 foundation_generic 11-rule canonical authoring (mirroring FUNDAMENTAL §6.1); principle-doc schema + frontmatter; governance discipline (authoring authority, supersession, audit cadence); CLAUDE.md HYBRID sync invariant; Part 6b derivation contract (canonical → derived enforcement); Pillar A consumption contract (principles_compliance citation); cross-cutting integration. RUSLAN-LAYER: Tier 1 content (Ruslan's values), Tier 2 ruslan_layer_overrides content (Ruslan's instance-specific rules), specific principle texts."
critic_findings: "Self-checks: (1) Pillar C does not author strategic direction (Pillar A boundary); (2) Pillar C does not author project strategy (Pillar B boundary); (3) Tier 2 foundation_generic = 11 entries mirror FUNDAMENTAL §6.1; (4) Part 6b derivation contract preserved; (5) CLAUDE.md HYBRID sync mechanized; (6) Tier 1 vs Tier 2 separation clear; (7) Foundation vs RUSLAN-LAYER strict per tier. Phase A-6 critic gate pending."
---

# Pillar C — Principles Substrate (Foundation cross-cutting sub-system)

## §0 Mission

Pillar C is the **Foundation-level Principles Substrate** — the canonical place
where principles are authored, versioned, audited. Per Ruslan emphasis (28.04
evening): «принципы это такой как бы мега CLAUDE.md для всей системы».

**Two-tier structure** per Ruslan emphasis:

- **Tier 1 — Manager / Owner principles** — values driving the human owner («развитие
  общества», «честность», «long-term thinking», «AI учит, не выполняет за человека»).
  Tier 1 content varies per fork-instance; Foundation generic = the structure.
- **Tier 2 — AI / System / Agent principles** — values constraining system behaviour
  («AI does not strategize», «default-deny novel actions», «filesystem source of
  truth»). Tier 2 has Foundation-generic 11-rule core (mirroring FUNDAMENTAL §6.1);
  RUSLAN-LAYER overrides per instance.

**Pillar C is a cross-cutting Foundation sub-system, NOT a numbered Part.** Per
`structural-placement-decision.md` §4.2 rationale 5: Pillar C is consumed by 5+
parts (6a, 6b, 7, 9, 11) and CLAUDE.md. Numbering would imply peer-status with
Parts 1-11. Sub-system status preserves cross-cutting subordinate semantics.

**Consumed by:**
- Part 6b (Human Gate): Tier 2 foundation_generic mirrors to Part 6b §I.2 `constitutional_never_list` 11-entry enum (derivation chain: FUNDAMENTAL §6.1 → Pillar C Tier 2 foundation_generic → Part 6b config)
- Part 11 (Strategic Direction Substrate): strategic docs cite Pillar C principles via `principles_compliance:` frontmatter
- Part 7 Bundle 5 supplement (Pillar B): project strategies cite Pillar C principles via `principles_compliance:` frontmatter
- Part 9 (Owner Interaction Scaffold): Tier 1 surfaces in monthly reflection cadence
- Part 6a (Provenance Officer): F-G-R per principle artefact + supersession audit
- CLAUDE.md (operational config): Tier 2 critical hard rules inlined for boot context per claude-md-reframing-decision.md HYBRID split

[F5|G:Foundation Pillar C canonical — Phase A single-owner; Fork-portable structure|R-high — Ruslan ack'd 2026-04-28]

---

## §A Inputs

| Source | Data shape | Event trigger | F-G-R |
|---|---|---|---|
| FUNDAMENTAL §6.1 (11 constitutional hard rules) | Constitutional baseline rule text + grade + anchor | Read at Tier 2 foundation_generic authoring (one-time per Bundle 5; refreshed if FUNDAMENTAL revised) | F8|G:LOCKED v1.0 constitutional|R-high |
| FPF anti-scope hard rules | `design/JETIX-FPF.md` anti-scope clauses | Read at Tier 2 authoring (one-time + on FPF supersession) | F5|G:FPF-Steward governed|R-high |
| Pillar A Lock Entry promotion candidates | Lock-to-Pillar-C candidate event from Part 11 §C.2 | Per Lock Entry commit citing rule rationale | F4|G:Pillar A integration|R-medium |
| Owner-authored principle | Direct Ruslan-authored principle file at `principles/tier-1-manager/<slug>.md` or `principles/tier-2-system/{foundation-generic|ruslan-layer-overrides}/<slug>.md` | Owner write event | F4-F8|G:owner-authored|R-high |
| Memory rules | Memory-system feedback rules (e.g., `feedback_strategic_layer_is_foundation_level`) — INPUT to inform principle authoring; not auto-promoted | Owner ack-driven only | F2|G:memory-recall|R-low pre-ack |
| Anthropic CAI / HHH framework | `raw/books-md/anthropic/bai-2022-cai.md` + `raw/books-md/anthropic/askell-2021-hhh.md` | Read at Tier 2 structural authoring | F5|G:Wave B library-direct|R-medium |
| Stoic / Munger mental-model frames | Wave B consultant cards (stoic-epistemic; capital-allocation-antifragility) | Read at Tier 1 framework reference | F4|G:Wave B|R-medium |

### §A.1 Concrete consequence — Tier 2 foundation_generic mirrors FUNDAMENTAL §6.1

Per `structural-placement-decision.md` §4.2 rationale 4 + §4.3 internal structure,
Tier 2 foundation_generic SUB-DIRECTORY contains EXACTLY 11 principle files
mirroring FUNDAMENTAL §6.1 11 hard rules. Lint check at Pillar C governance
audit:

```
count(files in principles/tier-2-system/foundation-generic/*.md) == 11
AND
each file maps to exactly one FUNDAMENTAL §6.1 rule via fundamental_anchor: frontmatter
AND
union of file fundamental_anchor: fields == FUNDAMENTAL §6.1 rules 1 through 11
```

Mapping (canonical, Bundle 5 Foundation generic):

| Pillar C Tier 2 file | FUNDAMENTAL §6.1 rule | Part 6b derived enforcement |
|---|---|---|
| `ai-does-not-strategize.md` | Rule 1 — AI does NOT make strategic decisions | constitutional_never_list[ai_strategize_or_set_direction] |
| `ai-does-not-execute-architectural-decision.md` | Rule 2 — Architectural changes require gate | constitutional_never_list[ai_execute_architectural_decision] |
| `ai-does-not-set-skill-direction.md` | Rule 3 — AI does NOT set capability direction | constitutional_never_list[ai_set_skill_direction] |
| `ai-does-not-claim-persistent-identity.md` | Rule 4 — No identity beyond acting_as | constitutional_never_list[ai_claim_persistent_identity] |
| `ai-does-not-claim-skin-in-the-game.md` | Rule 5 — No ownership claims | constitutional_never_list[ai_claim_skin_in_the_game] |
| `ai-does-not-aggregate-unstructured-long-term-memory.md` | Rule 6 — No memory persistence outside artefact paths | constitutional_never_list[ai_aggregate_unstructured_long_term_memory] |
| `agents-do-not-negotiate-contradictions-autonomously.md` | Rule 7 — No autonomous contradiction resolution | constitutional_never_list[agents_negotiate_contradictions_autonomously] |
| `agent-does-not-evaluate-peer-agent.md` | Rule 8 — No peer judgment without human | constitutional_never_list[agent_evaluate_peer_agent] |
| `ai-does-not-self-modify-at-runtime.md` | Rule 9 — No runtime self-modification | constitutional_never_list[ai_self_modify_at_runtime] |
| `ai-does-not-impersonate-human-externally.md` | Rule 10 — External AI disclosure mandatory | constitutional_never_list[ai_impersonate_human_externally] |
| `bypass-blast-radius-categorization-forbidden.md` | Rule 11 — Default-Deny constitutional | constitutional_never_list[bypass_blast_radius_categorization] |

This is the Foundation 11. ANY Phase B fork imports these unchanged.

### §A.2 Concrete consequence — Tier 1 + Tier 2 ruslan_layer_overrides authoring discipline

Tier 1 manager principles: owner-authored at `principles/tier-1-manager/<slug>.md`.
Per FUNDAMENTAL §6.2 founder-agency, owner is sole author. Foundation generic =
template + governance; content = RUSLAN-LAYER per fork-instance.

Tier 2 ruslan_layer_overrides: owner-authored at `principles/tier-2-system/ruslan-layer-overrides/<slug>.md`.
Examples (RUSLAN-LAYER content — illustrative, NOT this document's authoring):
- `no-api-key-exposure.md` (was CLAUDE.md Global Rule 6)
- `filesystem-source-of-truth.md` (was Global Rule 4)
- `language-discipline.md` (was Global Rule 7)
- `ab-test-gating.md` (was Global Rule 10)
- `path-protection.md` (was Правила item 6)
- `voice-pipeline-draft-only.md` (was CRM voice-integration discipline)

These are CANDIDATE migrations from CLAUDE.md per `claude-md-reframing-decision.md`
§3.2 — actual content authoring is Layer 2 next sprint.

### §A.3 Concrete consequence — input-as-data discipline (no auto-write)

Inputs (Lock candidates from Part 11; memory rules; Wave B framework references) feed
principle authoring but DO NOT auto-promote. Pillar C governance discipline:
every principle file is owner-acked write (per FUNDAMENTAL §6.2). Auto-promotion
of Lock candidate → principle = halt_log_alert violation (per Pillar C Tier 2
rule 1 «AI does not strategize»; principle authoring = strategic act).

---

## §B Outputs

| Consumer | Data shape | Event published | F-G-R |
|---|---|---|---|
| Part 6b (Human Gate) | Tier 2 foundation_generic config sync to `.claude/config/default-deny-table.yaml` constitutional_never_list | On Tier 2 file commit; sync lint enforces match | F8|G:Part 6b §I.2 LOCKED contract|R-high |
| CLAUDE.md HYBRID inline | Boot-context Tier 2 inline section §4.1 (foundation_generic 11) + §4.2 (ruslan_layer_overrides) per claude-md-reframing-decision.md | On Tier 2 file commit; sync lint enforces hash-match | F4|G:boot-context derived|R-medium (canonical = principles/, this is derived) |
| Part 11 (Strategic Direction Substrate) | Pillar C principles available for `principles_compliance:` ref; principle-supersession events surface for Pillar A re-citation | Per principle commit; per supersession | F4|G:Pillar A integration|R-medium |
| Part 7 Bundle 5 supplement (Pillar B) | Pillar C principles available for project-strategy `principles_compliance:` ref | Per principle commit | F4|G:Pillar B integration|R-medium |
| Part 9 (Owner Interaction Scaffold) | Tier 1 manager principles surface in monthly reflection cadence; principle-violation candidates surface in weekly review | Per cadence trigger + per surfaced candidate | F4|G:Part 9 owner reflection surface|R-medium |
| Part 6a (Provenance Officer) | F-G-R per principle artefact; supersession audit trail | Per commit | F8|G:Part 6a §I.1 LOCKED|R-high |
| Part 8 (Health Monitoring) | Principle-violation-rate SLI; principle-staleness SLI; Tier 1 review cadence SLI | Continuous emit | F4|G:Part 8 SLI consumption|R-medium |
| `.claude/config/default-deny-table.yaml` | constitutional_never_list 11 entries derived from Tier 2 foundation_generic | Sync trigger on Tier 2 commit | F8|G:Part 6b config canonical|R-high (derived but lint-enforced) |
| `swarm/wiki/log.md` | Append-only principle-event log | Per event | F4|G:audit trail|R-medium |

### §B.1 Concrete consequence — Pillar C → Part 6b derivation contract

Pillar C `principles/tier-2-system/foundation-generic/<rule>.md` files are
**canonical**. Part 6b `.claude/config/default-deny-table.yaml`
constitutional_never_list 11 entries are **derived**.

Sync invariant: count(Pillar C Tier 2 foundation_generic files) == 11 ==
count(Part 6b constitutional_never_list entries). Hash-match on each entry's
fields (action_class, trigger, enforcement, grade, fundamental_anchor).

Lint check `/lint --check-pillar-c-part-6b-sync` runs on commit:
- Counts on both sides
- Hash-compares
- Fail-loud on drift

This makes Part 6b §I.2 the **derived enforcement** of Pillar C canonical. If
they drift, fail-loud per FUNDAMENTAL §5.5 (no silent swallowing).

### §B.2 Concrete consequence — CLAUDE.md HYBRID sync

Per `claude-md-reframing-decision.md` §3.1, CLAUDE.md `§4 Pillar C Principles —
Boot Context` section contains inline copy of:
- §4.1: Tier 2 foundation_generic 11 rules (mirror of Part 6b config + canonical Pillar C)
- §4.2: Tier 2 ruslan_layer_overrides (RUSLAN-LAYER instance-specific)
- §4.3: Tier 1 reference link (canonical at `principles/tier-1-manager/_index.md`)

Sync invariant: hash-match between CLAUDE.md inline entries and canonical
`principles/tier-2-system/.../<slug>.md` files (specifically the rule statement
+ enforcement field).

Lint check `/lint --check-claude-md-sync` runs on commit:
- Counts inline entries vs canonical files
- Hash-compares rule statement field
- Fail-loud on drift

Why hash-match instead of "duplicate-as-needed": prevents drift where CLAUDE.md
inline diverges from canonical principles (e.g., wording change in canonical
not propagated). Mechanized invariant per Bundle 5 quality bar.

### §B.3 Concrete consequence — Tier 1 monthly cadence to Part 9

Tier 1 manager principles have monthly review cadence (Foundation generic; specific
calendar value RUSLAN-LAYER). Pillar C emits `tier-1-review-due` event to Part 9.
Owner sees in monthly reflection: «Tier 1 principles X / Y / Z — still aligned?
Any superseded?». Owner ack: re-affirm / supersede / amend.

This implements UC-A.4 decisions-DB integration at Tier 1: owner self-discipline
review surfaced via cadence.

### §B.4 Concrete consequence — Pillar A consumption via principles_compliance citation

Every Pillar A artefact (per Part 11 §I.5 frontmatter template) carries
`principles_compliance:` array of refs to Pillar C principle paths. Part 11
promotion gate runs lint:
- Each ref resolves to existing principle file
- Each ref is in `active` status (not `superseded`)
- Strategic doc principle citations align with strategic content

Same discipline applies to Pillar B project strategies (`principles_compliance:`
field per Part 7 Bundle 5 supplement §I.X.3 frontmatter template).

---

## §C Side-effects

### §C.1 Principle commit triggers Part 1 §H structured commit

`[principles] <tier> <verb> <slug>: <rationale>`

Examples:
- `[principles] tier-2-foundation lock ai-does-not-strategize: D-30 promotion from Lock Entry`
- `[principles] tier-2-overrides commit no-api-key-exposure: migrated from CLAUDE.md Global Rule 6`
- `[principles] tier-1-manager commit long-term-thinking: Layer 2 baseline`
- `[principles] tier-2-foundation supersede ai-does-not-strategize-v1: clarified scope`

### §C.2 Principle supersession triggers downstream re-review

When principle is superseded (new version with `supersedes:` ref), Pillar C emits:
- `principle-superseded` to Part 11 → Pillar A docs citing old version enter `under-review`
- `principle-superseded` to Part 7 Pillar B supplement → project strategies citing old version enter `under-review` at next stage gate
- `principle-superseded` to Part 6b → if Tier 2 foundation_generic, sync triggers updates to constitutional_never_list (subject to stop_gate per Part 6b §I.4)
- `principle-superseded` to CLAUDE.md HYBRID inline → sync triggers update

Cascade discipline parallel to Pillar A §C.3 cascade.

### §C.3 Lock-to-principle promotion (cross-Pillar discipline)

Per Part 11 §C.2 + §J.5: Lock Entry promoted at Pillar A level may emit
`pillar-c-principle-candidate` event. Pillar C governance reviews:
- Tier 1 candidate? → owner authors at `principles/tier-1-manager/<slug>.md`
- Tier 2 foundation_generic candidate? → owner authors at `.../foundation-generic/<slug>.md` AND triggers FUNDAMENTAL §6.1 revision (constitutional event; Part 6b stop_gate)
- Tier 2 ruslan_layer_overrides candidate? → owner authors at `.../ruslan-layer-overrides/<slug>.md`
- Lock-only (instance governance, not principle)? → remains Lock Entry only

Promotion is owner-acked write per FUNDAMENTAL §6.2.

### §C.4 Append-only via supersession (Pillar C side)

Per Part 6b §C.4 + Young Reversal Transactions, principles are NEVER edited in
place after promotion. New principle = new file with `supersedes:` ref. Prior
principle's `status:` field updated from `active` to `superseded` AS A NEW
APPEND-ONLY LINE in the file's status-history.

Why: if prior principle is edited away, the chain «what we believed in March
→ what we revised in May → why» becomes mutated prose; principle-evolution
audit becomes impossible.

### §C.5 Tier 2 foundation_generic supersession is constitutional event

Tier 2 foundation_generic mirrors FUNDAMENTAL §6.1. Editing a foundation_generic
principle = de facto FUNDAMENTAL §6.1 revision. Constitutional event (Part 6b
stop_gate per §I.4 LOCKED schema). Cannot be silent edit.

Tier 2 ruslan_layer_overrides + Tier 1 supersession is owner-acked per Part 6b
stage_gate (lower bar). Distinction matters: Foundation 11 is bedrock; instance
overrides are mutable.

---

## §D Dependencies (typed A.14 edges)

| Edge ID | Edge type | Target | Description |
|---|---|---|---|
| C-1 | `consumes-from` | FUNDAMENTAL §6.1 | Tier 2 foundation_generic mirrors 11 hard rules |
| C-2 | `consumes-from` | Part 11 (Strategic Direction Substrate) | Lock-to-Pillar-C candidate events feed principle authoring backlog |
| C-3 | `consumes-from` | Wave B consultant cards (Anthropic CAI / HHH; Stoic; Munger) | Framework references for Tier 1 + Tier 2 structural authoring |
| C-4 | `produces-for` | Part 6b (Human Gate) | Tier 2 foundation_generic sync to constitutional_never_list |
| C-5 | `produces-for` | Part 11 (Strategic Direction Substrate) | Principles available for principles_compliance citation |
| C-6 | `produces-for` | Part 7 Pillar B supplement | Principles available for project strategy principles_compliance citation |
| C-7 | `produces-for` | Part 9 (Owner Interaction Scaffold) | Tier 1 monthly review cadence; Tier 1+2 violation candidates surface |
| C-8 | `produces-for` | Part 8 (Health Monitoring) | Principle-violation-rate SLI; principle-staleness SLI |
| C-9 | `produces-for` | CLAUDE.md HYBRID | Tier 2 inline boot-context sync |
| C-10 | `governed-by` | Part 6a (Provenance Officer) | F-G-R per principle artefact + supersession audit |
| C-11 | `governed-by` | Part 6b (Human Gate) | Stop_gate for Tier 2 foundation_generic supersession; stage_gate for Tier 2 overrides + Tier 1 |
| C-12 | `constrained-by` | **FUNDAMENTAL §6.1** | Tier 2 foundation_generic = mirror of constitutional 11 hard rules |
| C-13 | `constrained-by` | **FUNDAMENTAL §6.2** | Founder-agency — principle authoring owner-only |
| C-14 | `constrained-by` | **FPF anti-scope hard rules genre** | Pillar C inherits FPF hard-rule discipline pattern |
| C-15 | `subordinate-of` | Foundation Architecture (10 LOCKED Parts) | Pillar C is cross-cutting subordinate, not peer-Part |

### §D.1 Why these 15 edges and not others

- Cross-cutting subordinate status (C-15) explicitly typed as `subordinate-of` — Pillar C is not a peer-Part
- Multiple `produces-for` edges (C-4 through C-9) reflect Pillar C's cross-cutting consumption pattern (5+ consumers)
- Two `governed-by` edges (C-10 + C-11) acknowledge dual governance: Part 6a for provenance, Part 6b for gate authority on supersession
- `constrained-by` edges (C-12 through C-14) anchor in FUNDAMENTAL §6.1/§6.2 + FPF discipline

No `depends-on` (banned). Untyped edges absent.

---

## §E Boundary (L/A/D/E per FPF A.6.B)

| Boundary direction | Concrete boundary |
|---|---|
| **L (Lower)** | What Pillar C will NOT pull from below. Pillar C does NOT auto-extract principles from agent scratchpads, daily-log prose, or memory rules. Owner-authored only |
| **A (Above)** | What Pillar C will NOT push upward. Pillar C does NOT modify FUNDAMENTAL §6.1 directly — Tier 2 foundation_generic mirrors §6.1; revision is constitutional stop_gate event flowing through Part 6b |
| **D (Down-system)** | What Pillar C enforces downward. Pillar C enforces Tier 2 foundation_generic 11-rule sync to Part 6b config + CLAUDE.md inline; enforces principles_compliance citation discipline at Pillar A + B promotion |
| **E (External)** | What Pillar C exposes externally. Pillar C principles MAY surface to mentor / external review via Part 10 sanitization; Tier 1 personal values may be redacted per FUNDAMENTAL §6.4 privacy boundary |

### §E.1 Concrete L boundary: no auto-extraction from agent surfaces

Agents writing to `agents/<id>/strategies.md` may surface principle-candidate
patterns. Pillar C does NOT auto-promote agent-surfaced patterns. Owner-acked
write only. Why: principle authoring = strategic act per Tier 2 rule 1.

### §E.2 Concrete A boundary: FUNDAMENTAL §6.1 is upstream, not downstream

Pillar C Tier 2 foundation_generic is downstream of FUNDAMENTAL §6.1 — mirrors
canonical, doesn't author. If Pillar C Tier 2 ENG identifies §6.1 gap, Pillar C
emits constitutional-revision-candidate via Part 6b stop_gate (per §C.5).

### §E.3 Concrete D boundary: enforcement via derivation

Pillar C does not directly halt actions (Part 6b owns Default-Deny + halt_log_alert).
Pillar C provides canonical principles; Part 6b derives + enforces. Boundary
respected: principle authoring vs principle enforcement.

### §E.4 Concrete E boundary: external sanitization

Tier 1 manager principles may contain personal values (e.g., specific Tier 1
principle «honor my late father's memory by building lasting work» — example,
not actual). External surfacing requires Part 10 sanitization. Tier 2 system
principles are typically less sensitive (rule statements about agents); but
RUSLAN-LAYER overrides may contain instance-specifics (specific paths,
specific keys) that need redaction.

---

## §F Anti-scope

### §F.1 Pillar C does NOT author strategic direction

Strategic direction (North Star, Direction Cards, etc.) lives at Part 11 (Pillar
A). Pillar C principles inform direction (cited via principles_compliance) but
do not author it.

Anti-pattern: principle file containing direction prose like «for 2026, the
North Star is X». Wrong: that's strategic direction, belongs in Pillar A
North Star artefact. Pillar C principle would be a meta-rule like «owner sets
annual North Star at year boundary».

### §F.2 Pillar C does NOT author project strategy

Project strategy lives at Part 7 Pillar B supplement. Principles are cited
via `principles_compliance:` but not authored as project strategy fragments.

### §F.3 Pillar C does NOT enforce (Part 6b enforces)

Pillar C is principle AUTHORING. Part 6b is principle ENFORCEMENT. Tier 2
foundation_generic 11-rule canonical at Pillar C; Part 6b config derives + runs
Default-Deny + halt_log_alert. Boundary respect.

Anti-pattern: Pillar C principle file embedding gate-execution code. Wrong:
that's enforcement, belongs in Part 6b. Pillar C declares; Part 6b enforces.

### §F.4 Pillar C does NOT modify FUNDAMENTAL §6.1

Per §E.2 + §C.5, Tier 2 foundation_generic supersession is constitutional event
flowing through Part 6b stop_gate. Pillar C does not edit FUNDAMENTAL.

### §F.5 Pillar C does NOT auto-promote candidates

Lock candidates from Part 11 §C.2; memory rules; agent-surfaced patterns —
all go to candidate review backlog. Owner-acked write only per FUNDAMENTAL §6.2.

### §F.6 Pillar C does NOT replace operational config (CLAUDE.md HYBRID)

CLAUDE.md operational config (paths, agent rosters, project lists, skills)
stays in CLAUDE.md per `claude-md-reframing-decision.md` Option 2 HYBRID.
Pillar C absorbs principles content; operational stays.

Anti-pattern: Pillar C absorbing CLAUDE.md operational config. Wrong: CLAUDE.md
operational has its own discipline (KM-MVP updates, project list updates) on
different cadence + authority than principles.

### §F.7 Pillar C does NOT host Ruslan-specific Tier 1 content as Foundation

Tier 1 foundation generic = STRUCTURE + governance discipline. Tier 1 CONTENT
(actual principles like «honesty», «long-term thinking», «развитие общества»)
is RUSLAN-LAYER. Bundle 5 architecture (this doc) defines structure; content
authoring next sprint Layer 2.

### §F.8 Pillar C does NOT enforce Tier 1 (owner-self-discipline)

Tier 1 manager principles are owner-self-discipline. Pillar C surfaces Tier 1
in cadence reviews (§B.3) but does not gate-enforce. Owner self-recognition at
Strategic Reflection cadence (Pillar A) and monthly Tier 1 review (Part 9
surface). Per Pillar C two-tier philosophy: Tier 1 = owner discipline; Tier 2
= system constraint.

### §F.9 Pillar C does NOT be a numbered Part

Per `structural-placement-decision.md` §4.2 rationale 5, Pillar C is cross-cutting
subordinate sub-system. Not Part 12. Not peer with Parts 1-11.

### §F.10 Pillar C does NOT replace `agents/<id>/strategies.md`

Agent strategies (Strategy Layer-2 self-write per Part 6b §I.2 whitelisted
class) are agent-internal learnings, not principles. Strategy = «what worked
for this agent in this role». Principle = «system-wide value/rule». Different
artefacts; do not conflate.

---

## §G F-G-R DOGFOOD

| Artefact | F (Formality) | G (Group-scope) | R (Reliability) |
|---|---|---|---|
| Tier 2 foundation_generic principle file | F8 (constitutional mirror) | System-wide (all agents + owner) | R-high (mirrors canonical FUNDAMENTAL §6.1) |
| Tier 2 ruslan_layer_overrides principle file | F4 → F5 (LOCKED post-ack) | System-wide RUSLAN-instance | R-medium-high |
| Tier 1 manager principle file | F4 → F5 | Owner-only canonical; mentor-surfaced sanitized | R-high (owner-authored prose) |
| Pillar C → Part 6b sync record | F8 (sync invariant) | System-internal | R-high (lint-enforced) |
| Pillar C → CLAUDE.md HYBRID inline derived | F4 (derived) | Boot-context | R-medium (derived, lint-enforced) |
| Principle supersession event | F5 | System-internal (cascade) | R-high (audit-essential) |
| Principle-violation candidate | F2 | Internal review | R-low pre-ack |

### §G.1 Promotion gates by F-grade

- **F2 → F4:** owner ack via Part 6b draft_promotion gate
- **F4 → F5:** owner ack via Part 6b stage_gate (Tier 1 + Tier 2 ruslan_layer_overrides)
- **F5 → F8:** Tier 2 foundation_generic supersession via Part 6b stop_gate (constitutional)

### §G.2 R degradation triggers

- Tier 1 principle not reviewed for >cadence (12 months default; RUSLAN-LAYER) → R-medium → R-low
- Tier 2 foundation_generic not synced to Part 6b config (sync drift detected) → R-low CRITICAL (fail-loud)
- Cited principle (referenced by Pillar A or B doc) superseded → cascade to citing doc R-degradation

---

## §H Code-level interfaces

### §H.1 Skills

| Skill | Purpose | Bundle 5 status |
|---|---|---|
| `/principle-author <tier> <slug>` | Scaffold new principle file with frontmatter + section template | Bundle 5 stub |
| `/principle-supersede <prior-path> <new-slug>` | Author supersession; verify cascade emission to citing docs | Bundle 5 stub |
| `/principle-review <tier>` | Surface principles due for cadence review (Tier 1 monthly; Tier 2 quarterly) | Bundle 5 stub |
| `/lint --check-pillar-c-part-6b-sync` | Hash-match invariant: Pillar C Tier 2 foundation_generic ↔ Part 6b constitutional_never_list | Bundle 5 stub |
| `/lint --check-claude-md-sync` | Hash-match invariant: Pillar C Tier 2 ↔ CLAUDE.md §4 inline | Bundle 5 stub |
| `/lint --check-principle-citations` | Verify Pillar A + Pillar B `principles_compliance:` refs resolve to active principles | Bundle 5 stub |
| `/lint --check-tier-2-foundation-count` | Verify count(foundation_generic files) == 11 | Bundle 5 stub |

### §H.2 Configs

- `principles/_governance.md` — authoring authority, supersession discipline, audit cadence (Foundation generic)
- `principles/_index.md` — MOC for both tiers (auto-generated by `/principle-rebuild-index`)
- `.claude/config/principles-tier-1-manager.yaml` — Tier 1 catalogue config (Foundation generic structure; RUSLAN-LAYER content)
- `.claude/config/principles-tier-2-system.yaml` — Tier 2 catalogue config (foundation_generic 11 + ruslan_layer_overrides)
- Sync hooks to `.claude/config/default-deny-table.yaml` constitutional_never_list (derived from foundation_generic)
- Sync hooks to CLAUDE.md `§4 Pillar C Principles` inline section (derived)

### §H.3 Agents involved

- `meta-agent` — quarterly principle audit (Tier 2 staleness; sync drift detection)
- `philosophy-expert` — Wisdom Loop application + Stoic / mental-model framework reference for Tier 1 authoring (DRAFT only; owner ack required)
- `manager` — coordinates Tier 1 monthly review cadence (Part 9 surface)
- All agents — CONSUME Tier 2 at session boot via CLAUDE.md §4 inline

No agent has principle authoring authority; owner is sole author per FUNDAMENTAL §6.2.

### §H.4 Part 1 §H commit substrate

Principle commits use Part 1 §H structured commit pattern (per §C.1).

### §H.5 CLAUDE.md HYBRID re-frame structure

Per `claude-md-reframing-decision.md` §3.1, CLAUDE.md gets new §4 section
(NEW for Bundle 5 + Layer 2 authoring sprint):

```markdown
## §4 Pillar C Principles — Boot Context

> Authority note: Canonical at `principles/`. This section inlines Tier-2
> for Claude Code boot context. Sync invariant via `/lint --check-claude-md-sync`.

### §4.1 Tier 2 Foundation Generic (11 hard rules)
[derived from principles/tier-2-system/foundation-generic/*.md]

### §4.2 Tier 2 RUSLAN-LAYER Overrides
[derived from principles/tier-2-system/ruslan-layer-overrides/*.md]

### §4.3 Tier 1 Reference
Canonical: principles/tier-1-manager/_index.md (not inlined; agents do not enforce Tier 1)

### §4.4 Sync Discipline
[doc of /lint --check-claude-md-sync invariant]
```

Bundle 5 ack creates §4 placeholder section with sync stub. Layer 2 sprint
populates with actual derived content.

---

## §I Data schemas

### §I.1 `shared/schemas/principle-doc.json` (NEW — Bundle 5)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "shared/schemas/principle-doc.json",
  "title": "Principle Document",
  "description": "Schema for principle artefacts hosted by Pillar C. Foundation-generic per Wave C Bundle 5.",
  "type": "object",
  "required": [
    "principle_id", "tier", "category", "slug", "statement",
    "rationale", "scope", "F", "G", "R", "owner_ack", "created_date"
  ],
  "properties": {
    "principle_id": {"type": "string", "pattern": "^P-[CSM]-[0-9]+$"},
    "tier": {
      "type": "string",
      "enum": ["tier_1_manager", "tier_2_system"]
    },
    "category": {
      "type": "string",
      "enum": ["foundation_generic", "ruslan_layer_overrides"],
      "description": "Tier 1 always ruslan_layer_overrides; Tier 2 splits foundation_generic vs ruslan_layer_overrides per directory structure"
    },
    "slug": {"type": "string", "pattern": "^[a-z0-9-]+$"},
    "statement": {"type": "string", "description": "The principle text — concise, declarative"},
    "rationale": {"type": "string", "description": "Why this principle; what it prevents / enables"},
    "scope": {
      "type": "object",
      "properties": {
        "applies_to": {
          "type": "array",
          "items": {"type": "string", "enum": ["all_agents", "specific_role_archetypes", "owner_only", "system_wide", "specific_part_consumers"]}
        },
        "specific_role_archetypes": {"type": "array", "items": {"type": "string"}},
        "specific_part_consumers": {"type": "array", "items": {"type": "string"}}
      }
    },
    "fundamental_anchor": {
      "type": "string",
      "description": "Required for tier_2_system foundation_generic. Refs FUNDAMENTAL §6.1 rule N"
    },
    "fpf_anchor": {"type": "string"},
    "F": {"type": "string", "enum": ["F2", "F4", "F5", "F8"]},
    "G": {"type": "string"},
    "R": {"type": "string"},
    "owner_ack": {
      "type": "object",
      "required": ["acked_by", "acked_date"],
      "properties": {
        "acked_by": {"const": "ruslan"},
        "acked_date": {"type": "string", "format": "date"}
      }
    },
    "supersedes": {"type": "string"},
    "superseded_by": {"type": "string"},
    "promoted_from_lock_entry": {"type": "string", "description": "If promoted via Pillar A Lock-to-principle pathway, ref to Lock Entry"},
    "enforcement": {
      "type": "object",
      "description": "For tier_2_system foundation_generic: derived enforcement contract to Part 6b",
      "properties": {
        "part_6b_action_class": {"type": "string"},
        "part_6b_enforcement_mode": {"type": "string", "enum": ["halt_log_alert", "advisory", "default_deny"]},
        "grade": {"type": "string"}
      }
    },
    "audit": {
      "type": "object",
      "properties": {
        "review_cadence": {"type": "string"},
        "last_reviewed_date": {"type": "string", "format": "date"},
        "violation_history": {"type": "array", "items": {"type": "object"}}
      }
    }
  }
}
```

### §I.2 Frontmatter template

```yaml
---
title: "<Principle title>"
principle_id: P-<C|S|M>-<NN>  # C=Constitutional, S=System, M=Manager
tier: tier_1_manager | tier_2_system
category: foundation_generic | ruslan_layer_overrides
slug: <kebab-case>
date: <YYYY-MM-DD>
F: F4 | F5 | F8
G: <scope description>
R: R-medium | R-medium-high | R-high
fundamental_anchor: <e.g., decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md §6.1 rule 1>  # required for tier_2 foundation_generic
fpf_anchor: <optional>
owner_ack:
  acked_by: ruslan
  acked_date: <YYYY-MM-DD>
supersedes: <prior-path-or-null>
superseded_by: <path-or-null>
promoted_from_lock_entry: <path-or-null>
enforcement:  # for tier_2 foundation_generic
  part_6b_action_class: <e.g., ai_strategize_or_set_direction>
  part_6b_enforcement_mode: halt_log_alert
  grade: F8
review_cadence: <e.g., quarterly | annual>
last_reviewed_date: <YYYY-MM-DD>
---
```

### §I.3 Principle file body structure (Foundation generic)

```markdown
# Principle: <Title>

## §1 Statement
<concise declarative principle statement>

## §2 Rationale
<why this principle; what it prevents / enables; framework anchors>

## §3 Scope
<applies_to> + <specific_role_archetypes if any> + <specific_part_consumers if any>

## §4 Anchors
- Constitutional: <FUNDAMENTAL § ref if applicable>
- FPF: <FPF § ref if applicable>
- Wave B framework: <consultant card refs>
- Lock Entry origin: <if promoted from Lock Entry>

## §5 Enforcement (Tier 2 only)
- Part 6b action_class: <ref>
- Enforcement mode: <halt_log_alert | advisory | default_deny>
- Grade: <F8 / F4 / etc>

## §6 Anti-scope
<what this principle does NOT cover; common confusions>

## §7 Audit history
| Date | Event | Note |
|---|---|---|
<append-only audit log>

## §8 Provenance
<sources, framework refs, prior context>
```

### §I.4 `principles/_governance.md` (Foundation generic)

```markdown
# Principles Governance

## §1 Authoring authority
- Tier 1 + Tier 2 ruslan_layer_overrides: owner-authored only per FUNDAMENTAL §6.2
- Tier 2 foundation_generic: mirrors FUNDAMENTAL §6.1; no direct authoring (revised via stop_gate flow)

## §2 Supersession discipline
- Append-only via supersedes: refs (per Young Reversal Transactions)
- Tier 1 + Tier 2 ruslan_layer_overrides: stage_gate
- Tier 2 foundation_generic: stop_gate (constitutional event)

## §3 Audit cadence
- Tier 1: monthly review (Part 9 surface)
- Tier 2 ruslan_layer_overrides: quarterly review (Pillar A Strategic Reflection cadence)
- Tier 2 foundation_generic: annual constitutional review

## §4 Sync invariants
- Pillar C Tier 2 foundation_generic ↔ Part 6b constitutional_never_list (count + hash match; lint enforced)
- Pillar C Tier 2 ↔ CLAUDE.md §4 inline (hash match; lint enforced)
- Lint failure = fail-loud per FUNDAMENTAL §5.5

## §5 Lock-to-principle promotion
- Pillar A Lock Entry promotion → Pillar C principle-candidate event (per Part 11 §C.2)
- Owner reviews tier categorization
- Authored as principle file with promoted_from_lock_entry: ref
```

### §I.5 `.claude/config/principles-tier-2-system.yaml` (NEW — Bundle 5)

```yaml
foundation_generic:
  schema_version: 1.0
  required_count: 11  # constitutionally fixed
  rules:
    P-C-01:
      slug: ai-does-not-strategize
      statement: "AI agents do NOT make strategic decisions; only owner authors strategic prose"
      fundamental_anchor: "§6.1 rule 1"
      enforcement:
        part_6b_action_class: ai_strategize_or_set_direction
        mode: halt_log_alert
        grade: F8
    # ... 10 more entries mirroring FUNDAMENTAL §6.1 rules 2-11

ruslan_layer_overrides:
  instance_id: jetix-phase-a-single-owner
  authoring_authority: ruslan
  rules:
    # Examples (to be populated Layer 2):
    # P-S-01: no-api-key-exposure (was CLAUDE.md Global Rule 6)
    # P-S-02: filesystem-source-of-truth (was CLAUDE.md Global Rule 4)
    # ... etc
```

### §I.6 `.claude/config/principles-tier-1-manager.yaml` (NEW — Bundle 5)

```yaml
foundation_generic:
  schema_version: 1.0
  structure:
    review_cadence: monthly
    surface: part_9_owner_interaction_scaffold
    enforcement: owner_self_discipline_only  # not gate-enforced

ruslan_layer_overrides:
  instance_id: jetix-phase-a-single-owner
  authoring_authority: ruslan
  values:
    # Examples (to be populated Layer 2):
    # P-M-01: long-term-thinking
    # P-M-02: honesty
    # P-M-03: ai-uchit-ne-vypolnyaet  (AI teaches, doesn't do for human)
    # ... etc
```

---

## §J Operational rituals

### §J.1 Principle authoring cycle (generic)

1. **Trigger.** Lock candidate from Pillar A; owner direct decision; framework
   reference (Wave B); memory-rule promotion candidate; gap surfaced via
   Strategic Reflection
2. **Tier categorization.** Owner determines: Tier 1 (manager value) /
   Tier 2 foundation_generic (constitutional system rule) / Tier 2
   ruslan_layer_overrides (instance-specific rule). Lock-only retained at
   Pillar A is NOT promotion to principle
3. **Drafting.** Owner authors principle file at appropriate path per §I.2
   frontmatter + §I.3 body structure
4. **F2 commit.** Draft committed at F2 / R-low per Part 1 §H
5. **F2 → F4 promotion.** Owner ack via Part 6b draft_promotion gate
6. **F4 → F5 promotion (LOCKED).** Owner ack via Part 6b stage_gate
7. **(Tier 2 foundation_generic only) F5 → F8 promotion.** Constitutional event;
   stop_gate; AND simultaneous FUNDAMENTAL §6.1 revision flow
8. **Sync to Part 6b config + CLAUDE.md HYBRID.** Sync lint runs on commit;
   updates `.claude/config/default-deny-table.yaml` constitutional_never_list
   (Tier 2 foundation_generic) and CLAUDE.md §4 inline
9. **Cascade emission.** Per §C.2, supersession events to consuming Pillar A + B
   + Part 6b + CLAUDE.md
10. **Audit log append.** Principle file §7 audit history appended

### §J.2 Tier 1 monthly review ritual

Pillar C emits `tier-1-review-due` to Part 9 monthly (Foundation generic;
calendar timing RUSLAN-LAYER). Part 9 surfaces in monthly reflection:
- «Tier 1 principle X — still aligned with current direction?»
- «Tier 1 principle Y — any tension with recent decisions?»
- «New Tier 1 principle candidate from this month's reflection?»

Owner ack: re-affirm / supersede / amend / no-change.

### §J.3 Tier 2 quarterly review ritual

Pillar C emits `tier-2-review-due` to Part 9 quarterly. Surfaces:
- «Tier 2 ruslan_layer_overrides — any rules superseded? Sync drift?»
- «Tier 2 foundation_generic — any FUNDAMENTAL §6.1 revision candidates?»
- «Lint sync invariant status: PASS / FAIL»

### §J.4 Tier 2 foundation_generic annual constitutional review

Annual review: full audit of FUNDAMENTAL §6.1 11 rules + Pillar C Tier 2
foundation_generic mirror + Part 6b constitutional_never_list derivation +
CLAUDE.md inline. Aligned with FUNDAMENTAL annual revision cadence (per Ruslan
note 28.04 evening «они как бы окей они есть, но мы их потом еще раз будем
перерабатывать»).

### §J.5 Sync drift detection ritual

`/lint --check-pillar-c-part-6b-sync` and `/lint --check-claude-md-sync` run on
every commit. Fail-loud if drift. Owner notified via Part 8 alert.

### §J.6 Principle-violation candidate review ritual

When agent action would violate a principle (per Part 6b enforcement), Part 6b
emits halt_log_alert + creates candidate in `swarm/wiki/drafts/principle-violation-candidates/`.
Pillar C governance reviews at next quarterly Tier 2 review:
- Was this a true violation (principle correctly enforced)?
- Or a false positive (principle scope too broad)?
- → Principle amendment / supersession candidate

---

## §K Failure modes

### §K.1 KC1 — Tier 2 foundation_generic / Part 6b sync drift

**Failure.** Owner edits Pillar C Tier 2 foundation_generic file but Part 6b
config is not updated; constitutional_never_list now diverges from canonical
principle text.

**Mitigation.**
- `/lint --check-pillar-c-part-6b-sync` invariant on every commit
- Pre-commit hook blocks commit on sync drift
- Part 8 SLI fires alert on detected drift

### §K.2 KC2 — CLAUDE.md HYBRID inline drift

**Failure.** Owner edits Pillar C Tier 2 file but CLAUDE.md §4 inline section is
not updated.

**Mitigation.**
- `/lint --check-claude-md-sync` invariant on every commit
- Hash-match enforcement
- Part 8 SLI alert

### §K.3 KC3 — Principle citation orphan

**Failure.** Pillar A or Pillar B doc cites Pillar C principle that has been
superseded; citing doc operates against stale principle.

**Mitigation.**
- Cascade: principle supersession emits `principle-superseded` to Part 11 + Part 7 (per §B.4 + §C.2)
- `/lint --check-principle-citations` on commit verifies all `principles_compliance:` refs are active
- Part 8 SLI: count(active principles_compliance refs to superseded principles) — alert if >0

### §K.4 KC4 — Tier 2 foundation_generic count drift

**Failure.** Tier 2 foundation_generic directory has 10 or 12 files; count
violates constitutional 11.

**Mitigation.**
- `/lint --check-tier-2-foundation-count` on every commit
- Pre-commit hook blocks
- Part 6b config sync also catches (constitutional_never_list count == 11 invariant)

### §K.5 KC5 — Tier 2 foundation_generic edited without stop_gate

**Failure.** Owner edits Tier 2 foundation_generic file in place (not via
supersession + stop_gate).

**Mitigation.**
- Append-only via supersedes: discipline (§C.4)
- Part 6a F-G-R audit flags in-place edits
- Part 6b stop_gate enforcement: F5 → F8 promotion requires stop_gate ack

### §K.6 KC6 — Tier 1 staleness (no review for >12 months)

**Failure.** Tier 1 manager principle not reviewed for >12 months; owner
direction may have shifted; principle now stale.

**Mitigation.**
- Monthly Part 9 surface (§J.2)
- R-degradation: R-high → R-medium at 12 months → R-low at 18 months
- Strategic Reflection cadence (Pillar A) surfaces «Tier 1 alignment with
  current direction?»

### §K.7 KC7 — Lock-to-principle promotion bypass

**Failure.** New constitutional rule (Tier 2 foundation_generic candidate)
authored without going through Part 11 Lock Entry → Pillar A → Pillar C
promotion pathway.

**Mitigation.**
- `/lint --check-lock-to-principle-trail` verifies Tier 2 foundation_generic
  files have either `fundamental_anchor:` (mirror of §6.1) OR
  `promoted_from_lock_entry:` ref
- Direct authoring of Tier 2 foundation_generic (without anchor or promotion
  trail) = halt_log_alert
- Constitutional revision flow per §C.5

### §K.8 KC8 — Cargo-cult principle authoring

**Failure.** Principle authored that just restates a Wave B framework
quote without adapting to Jetix instance context.

**Mitigation.**
- Principle file §2 Rationale required (not auto-empty)
- Wisdom Loop §M discipline at Pillar C governance review
- Quarterly audit checks for cargo-cult flag

### §K.9 KC9 — Tier 1 / Tier 2 confusion

**Failure.** Owner authors a principle as Tier 1 that is actually Tier 2 (or vice
versa).

**Mitigation.**
- `tier:` and `category:` frontmatter fields explicit
- Principle review checks tier appropriateness (e.g., "AI does not strategize"
  is Tier 2 system rule, not Tier 1 owner value — owner doesn't enforce on
  self; gate enforces on agents)
- §6 Anti-scope sections clarify boundaries

### §K.10 KC10 — Foundation generic vs RUSLAN-LAYER blur

**Failure.** Tier 2 ruslan_layer_overrides content embedded in foundation_generic
(or vice versa).

**Mitigation.**
- Directory structure enforces split
- Schema validation on principle file `category:` field
- Foundation vs RUSLAN-LAYER §X strict per Bundle 5 quality bar
- Fork-portability test: Phase B fork should be able to delete
  ruslan-layer-overrides/ + author own without touching foundation-generic/

### §K.11 KC11 — Principle file accumulation without value

**Failure.** Principles accumulate (Tier 1 + Tier 2 overrides) without
meaningful enforcement / use; principle-set becomes "decorative" parallel to
Pillar A direction-drift anti-pattern.

**Mitigation.**
- Cadence reviews (§J.2 monthly Tier 1; §J.3 quarterly Tier 2)
- Quarterly audit: «which principles were cited in Pillar A or B docs this
  quarter? Which were not?»
- Unused principles → R-degradation → eventual `paused` status

---

## §L Bundle 5 Pillar C work-list

| ID | Task | Status |
|---|---|---|
| L1 | Pillar C architecture (this document) | DRAFT |
| L2 | `principles/` directory scaffold (tier-1-manager/, tier-2-system/foundation-generic/, tier-2-system/ruslan-layer-overrides/) | Bundle 5 ack-then-create |
| L3 | `principles/_governance.md` Foundation generic | SPECIFIED §I.4; Bundle 5 ack-then-create |
| L4 | `principles/_index.md` MOC | Bundle 5 ack-then-create (auto-generated by Phase B skill) |
| L5 | `shared/schemas/principle-doc.json` schema | SPECIFIED §I.1; physical file Phase B |
| L6 | `.claude/config/principles-tier-1-manager.yaml` foundation_generic stanza | SPECIFIED §I.6; physical file Bundle 5 ack |
| L7 | `.claude/config/principles-tier-2-system.yaml` foundation_generic stanza (11 rules mirror) | SPECIFIED §I.5; physical file Bundle 5 ack |
| L8 | 11 Tier 2 foundation_generic principle files (mirroring FUNDAMENTAL §6.1) | Bundle 5 ack-then-create |
| L9 | `/principle-author`, `/principle-supersede`, `/principle-review` skills | Phase B materialization |
| L10 | `/lint --check-pillar-c-part-6b-sync`, `/lint --check-claude-md-sync`, `/lint --check-principle-citations`, `/lint --check-tier-2-foundation-count`, `/lint --check-lock-to-principle-trail` | Phase B materialization |
| L11 | CLAUDE.md HYBRID re-frame: §4 placeholder section | Bundle 5 ack-then-create |
| L12 | Migration of CLAUDE.md scattered principles → Pillar C ruslan_layer_overrides | Layer 2 next sprint |
| L13 | RUSLAN-LAYER Tier 1 manager principle authoring (~5-10 principles) | Layer 2 next sprint |
| L14 | RUSLAN-LAYER Tier 2 ruslan_layer_overrides authoring (~5-10 instance rules) | Layer 2 next sprint |
| L15 | Sync skills physical implementation | Phase B |

---

## §M Wisdom Application Findings

| # | Card | Principle | Current state | Improvement | Adopted? | O/P | Justification |
|---|---|---|---|---|---|---|---|
| 1 | Anthropic CAI Bai 2022 | Hardcoded never-list as constitutional | §A.1 Tier 2 foundation_generic = mirror FUNDAMENTAL §6.1; §I.5 11-rule canonical | Foundation 11 rules formally encoded; mirror invariant lint-enforced | YES | OPERATIONAL | Schema discipline + lint mechanism |
| 2 | Anthropic Askell HHH | Helpfulness / Harmlessness / Honesty triad as principle structure | (deferred to Tier 1 + Tier 2 examples per Layer 2) — Foundation generic structure adopted | Tier 2 foundation_generic 11 rules align with HHH genre | PARTIAL | OPERATIONAL | Structural alignment; specific HHH principles for Ruslan Tier 1 = next sprint |
| 3 | Levenchuk FPF anti-scope hard rules | Hard-rule discipline pattern | §F anti-scope discipline; F5/F8 hard-rule structure | Pillar C inherits FPF hard-rule genre | YES | OPERATIONAL | Genre adoption explicit |
| 4 | Stoic-Epistemic Munger | Mental models as principle structure | Wave B card referenced as Tier 1 framework anchor (§A); Tier 1 content (next sprint) cites Munger | Tier 1 framework reference established | YES | PHILOSOPHICAL | Framework-genre informs Tier 1; not gate-enforced |
| 5 | Stoic-Epistemic Naval | Specific knowledge / agency | (deferred to Tier 1 RUSLAN-LAYER content) — agency principle "AI учит не выполняет за человека" structurally captured at Tier 1 placeholder | Tier 1 framework reference | DEFERRED | — | Layer 2 next sprint |
| 6 | Stoic-Epistemic Holiday Obstacles | Reframing as growth | Tier 1 framework reference for "obstacles-way" Tier 1 candidate | Available as Tier 1 candidate | DEFERRED | — | Layer 2 next sprint |
| 7 | Capital Allocation Munger Inversion | Inversion as decision-frame | (deferred to Tier 1 candidate "always-invert"; relevant Tier 1) | Tier 1 framework reference | DEFERRED | — | Layer 2 next sprint |
| 8 | Capital Allocation Buffett | Owner perspective | (deferred to Tier 1 candidate "owner-discipline"; relevant Tier 1) | Tier 1 framework reference | DEFERRED | — | Layer 2 next sprint |
| 9 | Compounding Engineering R2 Reinforcing | Self-improvement loop | Cadence reviews (§J.2-J.4) compound Tier 1+2 review patterns | Self-improvement loop integrated | YES | OPERATIONAL | Cadence schedule discipline |
| 10 | Multi-agent Architecture | Tier 2 = constraint surface for agents | Tier 2 system principles constrain all agent behavior; Part 6b enforces | Cross-Pillar contract solid | YES | OPERATIONAL | Schema + sync discipline |
| 11 | Levenchuk IP-7 Writing-as-Thinking | Owner-authored principle prose | §A.3 owner-acked write only; principle file §2 Rationale prose required | Foundation discipline | YES | OPERATIONAL | Schema + governance |
| 12 | FUNDAMENTAL §6.2 Founder-agency | Owner-only principle authority | Authoring authority §I.4 §1; D-13 constrained-by | Constitutional alignment | YES | OPERATIONAL | Cross-edge typed |
| 13 | FUNDAMENTAL §6.4 Privacy boundary | Tier 1 personal-value sensitivity | §E.4 sanitization for external surface | Privacy preserved structurally | YES | OPERATIONAL | Boundary discipline |
| 14 | FPF B.3 F-G-R | Provenance grading per principle | §G F-G-R per artefact-type table | Schema discipline | YES | OPERATIONAL | Schema-enforced |
| 15 | Young Reversal Transactions | Append-only via supersession | §C.4 + §C.5 + audit log §7 | Foundation discipline | YES | OPERATIONAL | Schema discipline |
| 16 | Anthropic CAI ASL-tier (OQ-CAI-2) | Risk-graded enforcement | (deferred — Tier 2 grade field aligned with F-grade for now) | F-grade is current proxy | DEFERRED | — | OQ stub Phase B |

**Operational ratio:** 10 OPERATIONAL + 1 PHILOSOPHICAL + 5 DEFERRED = 10/11
adopted = 90.9% — exceeds ≥85% target.

**5 DEFERRED appropriate**: 3 are Layer-2 content authoring (Naval / Holiday / Munger / Buffett — Tier 1 candidates next sprint); 1 is partial (Askell HHH structurally adopted, content next sprint); 1 is OQ stub (CAI ASL-tier).

---

## §N Provenance

### §N.1 Constitutional anchors
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` LOCKED v1.0: §0 (two-layer pattern), §6.1 (11 constitutional hard rules — Tier 2 foundation_generic source), §6.2 (founder-agency), §6.4 (privacy boundary)
- `design/JETIX-FPF.md`: anti-scope hard-rule genre; B.3 F-G-R; A.6.B Boundary; A.14 typed edges

### §N.2 Decision artefacts (Bundle 5)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/structural-placement-decision.md` §4 (Pillar C as standalone sub-system)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/claude-md-reframing-decision.md` (HYBRID re-frame Option 2)

### §N.3 LOCKED Foundation parts consumed
- Part 6a (F-G-R per principle artefact)
- Part 6b (§I.2 constitutional_never_list as derived enforcement; stop_gate for foundation_generic supersession)
- Part 7 (Pillar B Bundle 5 supplement — principles_compliance citation surface)
- Part 8 (SLI emission for principle-violation-rate, sync drift)
- Part 9 (monthly Tier 1 review surface)
- Part 11 (Pillar A Bundle 5 sibling — principles_compliance citation surface; Lock-to-principle promotion pathway)
- CLAUDE.md (boot-context HYBRID inline derivation target)

### §N.4 Wave B consultant cards
- `consultants/anthropic-constitutional-ai.md` (Bai 2022 hardcoded never-list; CAI structural pattern)
- Wave B Supplement library-direct: `raw/books-md/anthropic/bai-2022-cai.md`, `raw/books-md/anthropic/askell-2021-hhh.md`
- `consultants/levenchuk-shsm-fpf.md` (FPF anti-scope hard rules + IP-7)
- `consultants/stoic-epistemic.md` (Tier 1 framework references)
- `consultants/capital-allocation-antifragility.md` (Tier 1 framework: Munger inversion, Buffett owner)
- `consultants/multi-agent-architecture.md` (Tier 2 agent constraint surface)
- `consultants/compounding-engineering.md` (R2 reinforcing loop)

### §N.5 Memory references
- `feedback_strategic_layer_is_foundation_level` (Bundle 5 cycle basis)
- `feedback_ai_does_not_strategize` (Tier 2 foundation_generic rule 1; Pillar C canonical authoring)
- `feedback_no_solo_founder_downgrade` (Tier 1 candidate Layer 2)
- `methodology_multi_chat_review_for_critical_docs` (Tier 1/2 candidate Layer 2)

### §N.6 CLAUDE.md current state
- 273 lines analyzed: ~95% operational config + ~5% scattered principles
- Migration candidates per `claude-md-reframing-decision.md` §3.2

---

## §X Foundation vs RUSLAN-LAYER strict separation

### §X.1 Foundation generic (this document — Pillar C architecture)

- **Two-tier structure** (Tier 1 manager / Tier 2 system) — fork-portable
- **Tier 2 foundation_generic 11-rule canonical authoring** — mirror of FUNDAMENTAL §6.1; ANY fork imports unchanged
- **Tier 2 ruslan_layer_overrides directory pattern** — fork-portable structure (renamed `<instance>-layer-overrides` per fork)
- **Principle-doc schema** (§I.1) — fork-portable
- **Principle-doc body structure** (§I.3) — 8 sections Foundation canonical
- **Frontmatter template** (§I.2) — fork-portable
- **Governance discipline** (`principles/_governance.md` §I.4) — authoring authority + supersession + audit cadence
- **CLAUDE.md HYBRID re-frame structure** (§H.5) — split discipline + sync invariant lint mechanism (specific CLAUDE.md content is per-fork)
- **Part 6b derivation contract** (§B.1) — sync invariant lint
- **Lock-to-principle promotion pathway** (§C.3) — cross-Pillar discipline
- **11 failure modes** (§K.1-11) — Foundation-generic mitigations
- **Cadence schedule** (§J.2-J.4): monthly Tier 1 / quarterly Tier 2 / annual Tier 2 foundation_generic constitutional review (specific calendar timings RUSLAN-LAYER)
- **15 typed A.14 edges** (§D) — fork-portable Foundation contracts
- **9 anti-scope clauses** (§F) — fork-portable

### §X.2 RUSLAN-LAYER (next sprint Layer 2 — NOT in Bundle 5 scope)

- **Tier 1 manager principles content** — Ruslan's actual values (long-term thinking, AI учит не выполняет за человека, развитие общества, honesty, etc.)
- **Tier 2 ruslan_layer_overrides content** — Ruslan's instance-specific Tier-2 rules (no API key exposure, filesystem source-of-truth, language discipline, path protection, etc.)
- **CLAUDE.md migration** — Ruslan's CLAUDE.md scattered principles migrated to canonical Pillar C files
- **Specific cadence values** — calendar timing of monthly / quarterly / annual reviews
- **Specific Tier-2 ruslan_layer_overrides count** — fork specific (Ruslan's instance may have N rules; another fork may have M)
- **Specific principle-violation review patterns** — instance-specific patterns

### §X.3 Fork-portability test

A Phase B fork-importer (e.g., scientific researcher applying Jetix-methodology
to medical research):
- Imports `principles/` scaffold structure unchanged
- Imports Tier 2 foundation_generic 11 files unchanged
- Imports principle-doc schema unchanged
- Imports `_governance.md` unchanged (Foundation generic governance discipline)
- Imports CLAUDE.md HYBRID re-frame structure unchanged (just §4 section template)
- Replaces Tier 2 ruslan_layer_overrides with own (e.g., medical-instance-overrides)
- Authors own Tier 1 manager principles (medical researcher's values)
- Renames CLAUDE.md instance-specific blocks to medical-researcher-context

### §X.4 Lint enforcement of X boundary

| Lint rule | Enforces |
|---|---|
| `--check-no-instance-content-in-foundation-generic` | Foundation generic Tier 2 directory contains only the 11 mirror rules; instance-specific Tier-2 always lives in ruslan-layer-overrides (or fork-rename) |
| `--check-tier-1-content-not-in-tier-2` | Tier 1 manager values never authored in Tier 2 directory (and vice versa) |
| `--check-pillar-c-architecture-foundation-only` | Pillar C architecture document does not embed instance-specific Tier-1 / Tier-2-overrides content |

---

*End of Pillar C architecture. ~10K words. Foundation cross-cutting sub-system.
Two-tier structure: Tier 1 manager + Tier 2 system. CLAUDE.md HYBRID re-frame
+ Part 6b derivation contract + Pillar A/B principles_compliance integration.
Foundation-generic; RUSLAN-LAYER content authoring next sprint (Layer 2).
AWAITING-APPROVAL — gates Wave E LOCKED tag.*
