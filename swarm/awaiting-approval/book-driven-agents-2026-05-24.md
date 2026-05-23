---
title: AWAITING-APPROVAL packet — Book-driven Agent Sorting + ROY Swarm Expansion (8 new ROY agents + 31 Tier A wikis + routing-table extension)
date: 2026-05-24
type: awaiting-approval
gate_class: stage_gate
gate_type: irreversible (architectural — Foundation infrastructure: .claude/agents/ + swarm/lib/routing-table.yaml + swarm/wiki/concepts/ + .claude/config/default-deny-table.yaml additive)
blast_radius: F3-F4 (multi-Foundation-touch)
ack_status: AWAITING-RUSLAN-ACK
parent_prompt: prompts/book-driven-agent-sorting-2026-05-24.md
parent_substrate:
  - reports/research-corpus-pipeline-2026-05-24/phase-6-bucket-cross-mapping.md
  - reports/book-driven-agents-2026-05-24/phase-0-substrate.md
  - reports/book-driven-agents-2026-05-24/01-corpus-knowledge-domains.md
  - reports/book-driven-agents-2026-05-24/02-refined-taxonomy.md
  - reports/book-driven-agents-2026-05-24/03-agent-topology-proposal.md
  - reports/book-driven-agents-2026-05-24/04-per-agent-substrate-drafts.md
  - reports/book-driven-agents-2026-05-24/05-wiki-auto-creation-proposals.md
constitutional_posture:
  - R1 — Ruslan = sole strategist; this packet = surface options, R1 picks final
  - R2 STRICT — Foundation infrastructure modification gate (Tier 2 rule 2 + Part 6b §I.4 stage_gate)
  - R6 — provenance per book / per wiki / per agent draft
  - R11 + Part 6b §I.2 — Default-Deny novel actions discipline preserved (4-6 boundaries per candidate)
  - R12 — paired-frame enforcement operationalized via influence-ethics-expert (THE R12 enforcement cell)
  - IP-1 strict — Foundation = abstract role-types; executor binding = RUSLAN-LAYER separate file per shared/schemas/executor-binding.yaml.template
  - AP-6 — dissent-preservation: variants discussed in Phase 3 §3.4 preserve full reasoning trail
  - append-only — packet appended to swarm/awaiting-approval/; not modifying existing entries
F: F4
G: book-driven-agents-roy-expansion-packet
R: refuted_if_partial_ack_OR_executor_binding_inferred_pre_ack_OR_Foundation_paths_modified_pre_ack
related_packets:
  - swarm/awaiting-approval/legacy-12-agents-deprecation-2026-05-17.md (closest format analog)
  - swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md (R12 substrate)
  - swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md (R12 RUSLAN-LAYER extension)
  - swarm/awaiting-approval/h6-hackathon-platform-pre-eminent-2026-05-18.md (cohort recruitment substrate)
---

# AWAITING-APPROVAL — Book-driven Agent Sorting + ROY Swarm Expansion

## §1 Scope summary

**REQUEST:** Add **5-8 NEW ROY swarm agents** (Ruslan picks tier MIN/STANDARD/MAX) + **31 Tier A wikis** + **routing-table.yaml extension** (`agent_role_extensions` section) + **4 additive RUSLAN-LAYER Default-Deny action classes** (already exist в `.claude/config/default-deny-table.yaml` per R12 programmable Ethereum packet 2026-05-18 — no NEW classes added here; existing 4 R12 classes operationalized via auto-pair routing).

**NOT IN SCOPE (this packet does NOT request):**
- ❌ Modifying existing 9 ROY swarm agents
- ❌ Modifying Foundation Parts 1-11
- ❌ Modifying CLAUDE.md (downstream of this packet ack = future session)
- ❌ Modifying executor-binding.yaml (RUSLAN-LAYER scope — separate Ruslan ack flow per IP-1)
- ❌ Auto-creating any wikis в `swarm/wiki/`
- ❌ Acquiring new books (Witkowski critical-reviews + complexity canon = separate acquisition queue noted)

## §2 Tier options (Ruslan picks one)

> **MIN (5 candidates) — conservative baseline:**
> 1. propaganda-expert (SC1+SC3 merged — incorporates persuasion-tactics)
> 2. recruitment-dynamics-expert (SC2+SC4 merged — incorporates community-formation)
> 3. nlp-expert (SC6+SC7+SC8)
> 4. methodology-engineer (SC11+SC12+SC13)
> 5. influence-ethics-expert (cross-cluster R12 enforcement cell) ⭐ MANDATORY pair with #1-3
>
> **Tier A wikis affected:** 23 of 31 (excludes sota-tracker / ml-ai / gamification clusters)
> **Routing-table additions:** 5 entries в `agent_role_extensions:` section
> **Constitutional risk:** LOW (5 agents = cleanest IP-1 split; R12 enforcement immediately operational; gamification-engagement-expert deferred to future cycle)
> **Ruslan attention budget impact:** modest (5 agents added; total roster goes 9 → 14 active per CLAUDE.md `## Active ROY Swarm`)

> **STANDARD (7 candidates) — recommended:**
> All 5 MIN + **sota-tracker-expert** (SC9+SC10) + **ml-ai-foundations-expert** (SC15)
>
> **Tier A wikis affected:** 27 of 31 (excludes 4 gamification cluster)
> **Routing-table additions:** 7 entries
> **Constitutional risk:** LOW-MEDIUM (sota-tracker IP-1 split from philosophy-expert needs explicit formalization in routing-table comments; ml-ai-foundations-expert specialization split from engineering-expert needs explicit boundary card)
> **Ruslan attention budget impact:** higher (7 agents; total roster 9 → 16)

> **MAX (8 candidates) — aggressive:**
> All 7 STANDARD + **gamification-engagement-expert** (SC17)
>
> **Tier A wikis affected:** all 31
> **Routing-table additions:** 8 entries
> **Constitutional risk:** MEDIUM (gamification has highest R12-extraction risk surface; requires tight influence-ethics-expert pairing; Eyal Hook model = explicitly persuasion engineering)
> **Ruslan attention budget impact:** highest (8 agents; total roster 9 → 17 — still within CLAUDE.md §4.2 max-20 cap per Manager attention budget)

**recommended:** **STANDARD (7 candidates)** per Phase 3 §3.5 rationale. Conservative MIN deferred sota-tracker SOTA-tracking project ROI; MAX gamification-engagement adds R12 surface area без clear current Jetix project demand (Network-State / Jetix-Clan gamification = bets-tier project per CLAUDE.md priority table).

## §3 Actions (sequence per Ruslan ack — staged)

### Stage 1: ACK + executor-binding fill (RUSLAN-LAYER decision)
1. Ruslan picks tier (MIN / STANDARD / MAX) — circles below in `Ruslan ack` section
2. Ruslan fills `shared/schemas/executor-binding.yaml.template` per IP-1: which executor (model + agent file path) binds to each role-archetype slug
3. Ruslan confirms which auto_pair rules apply (suggested: ALL R12 paired-frame mandates from §4 below)

### Stage 2: Agent file creation (future session, post-ack)
4. Create `.claude/agents/<slug>.md` per Phase 4 drafts — 5/7/8 files depending on tier
5. Create `agents/<slug>/strategies.md` initial bootstrap content per Phase 4 strategies.md scaffolds
6. Create `agents/<slug>/scratchpad.md` (empty initial per Karpathy++ substrate convention)
7. Create `agents/<slug>/niche/` directory + symlinks per Phase 4 manifest:
   - `agents/<slug>/niche/books/<book-slug>.md` → relative symlink to required book paths
   - `agents/<slug>/niche/wiki/<wiki-slug>.md` → relative symlink to Tier A wiki paths (post Stage 3 wiki creation)
   - `agents/<slug>/niche/pairings/<pair-slug>` → reference to auto-pair agent

### Stage 3: Wiki creation (future session)
8. Create `swarm/wiki/concepts/<wiki-slug>.md` for selected Tier A wikis per Phase 5 §5.3 drafts (23 / 27 / 31 depending on tier) — each: frontmatter (Phase 5 templates) + 1-3 paragraph content + R6 `derived_from:` list

### Stage 4: Routing-table extension (future session)
9. Update `swarm/lib/routing-table.yaml` — add `agent_role_extensions:` section per Phase 3 §3.6 pseudo-diff:
   - 5/7/8 entries with: modes / sub_clusters / auto_pair / granularity
   - Header comment update to reference this packet ack
   - schema_version bump (1.0.0 → 1.1.0 additive)

### Stage 5: CLAUDE.md update (future session)
10. Update CLAUDE.md `## Active ROY Swarm` section — add 5/7/8 new rows with status `active` (or `provisional` if Ruslan prefers staged activation)
11. Add CLAUDE.md `## §4.5 Book-driven Agent Expansion 2026-05-24` summary section pointing to this packet ack

### Stage 6: Cycle hook (future session — optional)
12. Add `swarm/lib/hooks/post-agent-creation.sh` — verifies symlink integrity per Phase 4 niche/ manifest

## §4 R12 paired-frame discipline operational binding

**MANDATORY R12 auto-pair rules** (Ruslan ack required for these specifically — applies to ALL tier selections):

| Trigger agent | Auto-pair (receiver) | Rationale | Pre-flight check |
|---|---|---|---|
| propaganda-expert dispatch | influence-ethics-expert | every propaganda technique surfacing without R12 paired-frame = Tier 2 R12 violation | brigadier verifies `auto_pair` rule fires in routing-table |
| recruitment-dynamics-expert dispatch | influence-ethics-expert | every recruitment surface MUST include exit-rights + fork-and-leave + non-extraction guarantee per Tier 2 R12 + RUSLAN-LAYER 4 extraction classes | brigadier verifies BITE/Lifton diagnosis paired with R12 audit |
| nlp-expert dispatch | influence-ethics-expert | every NLP pattern surface MUST include critical-review + abuse-mode flag + ethical-use precondition | brigadier verifies Milton-model/Sleight-of-Mouth pattern carries Hassan defensive-use cross-ref |
| gamification-engagement-expert dispatch (MAX tier) | influence-ethics-expert | Hook model = explicit persuasion engineering; dark-patterns gamification = Tier 2 R12 violation | brigadier verifies optimizer-mode allowed ONLY under paired-frame |

**Halt-Log-Alert F4 ≤5s** on any auto-pair-rule violation. Emit to `swarm/approvals/log.jsonl` per Part 6b §I.2 (already operational per legacy-12-agents-deprecation packet 2026-05-17 ack).

**No NEW Default-Deny action classes added.** Existing 4 RUSLAN-LAYER R12 classes (extraction_beyond_share / wage_ratio_violation / non_consensual_distribution / fork_prevention_attempt) per `.claude/config/default-deny-table.yaml` (per r12-programmable-ethereum packet 2026-05-18 ack) — operationalized via auto-pair routing, NOT modified.

## §5 IP-1 strict verification

**ALL drafts comply:** Phase 4 §4.10 IP-1 verification checklist:
- ✅ Zero candidate slugs reference executor models (no "claude-opus-4-7", "sonnet-4-6", "haiku-4-5" in any candidate frontmatter)
- ✅ All `model:` fields = `<RUSLAN-LAYER placeholder>`
- ✅ Executor binding deferred to RUSLAN-LAYER per `shared/schemas/executor-binding.yaml.template`

**RUSLAN-LAYER fill template** (Ruslan completes post-ack):
```yaml
# shared/executor-binding.yaml additions
executor_bindings:
  propaganda-expert:
    executor: <ruslan picks: claude-opus-4-7 OR sonnet-4-6 OR haiku-4-5 OR other>
    agent_file_path: .claude/agents/propaganda-expert.md
  recruitment-dynamics-expert:
    executor: <ruslan picks>
    agent_file_path: .claude/agents/recruitment-dynamics-expert.md
  # ... etc for selected tier
```

## §6 Risks & mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| R12 paired-frame discipline drifts in practice | MEDIUM | HIGH (Tier 2 violation) | brigadier verifies `auto_pair` rule at dispatch time; Halt-Log-Alert F4 on miss; influence-ethics-expert REJECTS unpaired requests |
| sota-tracker-expert vs philosophy-expert role confusion | MEDIUM | MEDIUM (routing ambiguity) | IP-1 explicit split formalized in routing-table.yaml comment: philosophy-expert = evaluative; sota-tracker = instrumental tracking. Different cells, different modes |
| methodology-engineer overlaps systems-expert + engineering-expert | LOW | LOW (Phase 3 §3.4 V4 NOT promoted; methodology-engineer = orthogonal cell) | Boundary cards in system.md §5 Dispatch Routing Notes for each |
| Witkowski et al. critical NLP review NOT in 80-corpus | KNOWN | LOW (acquisition queue noted) | nlp-expert strategies.md initial flags Witkowski as acquisition priority — separate Ruslan decision |
| Ruslan attention budget exceeded (>20 active agents per CLAUDE.md §4.2) | LOW (9+8=17 still <20) | LOW | Budget headroom preserved; future agents would consolidate via deprecation cycle (analog to legacy-12 deprecation 2026-05-17) |
| Tier A wiki count (31) overwhelms operator attention at creation time | LOW | LOW | Wikis are deferred-creation per Stage 3; creation cadence = ~3-5 wikis per cycle post-ack; not 31-in-one-cycle |
| Agent overlap with existing legacy-archived agents (e.g., crazy-agent = adjacent-thinking-expert variant) | LOW (variant DROPPED per Phase 3 §3.4 V6) | LOW | Phase 3 explicit rejection of adjacent-thinking-expert; future cycle can revisit |

## §7 Acceptance criteria for packet ack (Ruslan completes)

```yaml
# Ruslan ack section — circle one tier + provide executor-binding decisions
ruslan_ack:
  date: ____________
  tier_selected: [ MIN | STANDARD | MAX ]  # circle one
  executor_bindings_filled: [ Y | N ]  # if Y, fill RUSLAN-LAYER file
  r12_auto_pair_rules_acked: [ Y | N ]  # §4 above
  staged_activation_preference: [ all-at-once | provisional-then-active | other ]
  additional_notes: ____________
```

**Halt conditions (packet rejected / partial):**
- Ack tier = NONE → no agents created; report archived
- Executor-bindings NOT filled within 7 days of tier ack → Stage 2 blocked; brigadier escalates per Part 9 owner-reflection cadence
- R12 auto-pair rules NOT acked → tier MIN forced (only sota-tracker + methodology-engineer + ml-ai have NO R12 dependency); propaganda/recruitment/nlp/gamification creation blocked

## §8 Provenance & verification trail

**Phase reports (all 7 committed to main):**
- a45c6d2 Phase 0 substrate
- 46d513b Phase 1 corpus knowledge-domain extraction (80 books × structured profile)
- 2a59657 Phase 2 refined taxonomy (17 sub-clusters × 5 mega-clusters)
- 9fc5896 Phase 3 agent topology proposal (8 candidates rubric-scored)
- d0371a6 Phase 4 per-agent substrate drafts
- 0dc715f Phase 5 wiki auto-creation proposals (31 Tier A + 15 Tier B-Plus)
- <this packet's commit hash post-Phase-6> Phase 6 AWAITING-APPROVAL packet

**Foundation references consulted (read-only):**
- swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md (Part 4 LOCKED)
- swarm/wiki/foundations/part-6b-human-gate/architecture.md (Part 6b LOCKED — stage_gate authoritative)
- shared/schemas/task-return-packet.json (Part 4 §I.1 LOCKED)
- shared/schemas/executor-binding.yaml.template (IP-1 strict separation pattern)
- .claude/config/default-deny-table.yaml (Part 6b §I.2 constitutional_never_list + RUSLAN-LAYER 4 R12 classes from r12-programmable-ethereum packet 2026-05-18)
- swarm/lib/routing-table.yaml (schema 1.0.0 — current state)
- CLAUDE.md (`## Active ROY Swarm` + §4 Pillar C Principles)

**Existing AWAITING-APPROVAL precedent (format reference):**
- swarm/awaiting-approval/legacy-12-agents-deprecation-2026-05-17.md (closest format analog — agent infrastructure modification)
- swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md (R12 substrate)
- swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md (R12 RUSLAN-LAYER extension; ack establishes 4 extraction action classes)

## §9 Constitutional posture summary

| Posture | Status | Verification |
|---|---|---|
| R1 surface only — Ruslan = sole strategist | ✅ | All Phase 3 + 4 + 5 outputs framed as options for Ruslan ack; rubric-scoring transparent; recommendations technical not strategic |
| R2 STRICT — Foundation infrastructure via packet | ✅ | NO writes to `.claude/agents/`, `swarm/lib/routing-table.yaml`, `swarm/wiki/concepts/`, `.claude/config/default-deny-table.yaml` pre-ack |
| R6 — provenance per book / wiki / agent | ✅ | Phase 1 [src:] per book; Phase 4 `required_books_path_refs` per agent; Phase 5 `derived_from:` per wiki |
| R11 + Part 6b §I.2 — Default-Deny | ✅ | 4-6 explicit out-of-scope action classes per candidate Phase 4 |
| R12 — paired-frame enforcement | ✅ | influence-ethics-expert designed as enforcement cell + auto-pair rules §4 above + Phase 4 §4.10 R12 discipline table |
| IP-1 strict — abstract role-types only | ✅ | Phase 4 §4.10 IP-1 verification + RUSLAN-LAYER executor-binding template §5 above |
| AP-6 — dissent preservation | ✅ | Phase 3 §3.4 variants discussed with merge/drop rationale preserved |
| Append-only | ✅ | Packet appended to swarm/awaiting-approval/; not modifying prior entries |

## §10 Estimated Stage 2-6 effort (post-ack)

| Stage | Effort estimate | Session count |
|---|---|---|
| Stage 1 (Ruslan ack + executor-binding fill) | 30-60 min | 1 |
| Stage 2 (agent file creation 5/7/8) | 1-2h | 1 |
| Stage 3 (wiki creation 23/27/31 — 1-2 paragraphs each) | 3-5h | 1-2 (batch) |
| Stage 4 (routing-table.yaml extension) | 30 min | (included in Stage 2 session) |
| Stage 5 (CLAUDE.md update) | 30 min | (included in Stage 2 session) |
| Stage 6 (cycle hook — optional) | 1h | (included or skipped) |
| **TOTAL post-ack** | **~5-9h** | **2-3 sessions** |

Per Stage 2-3 efficiency: server CC autonomous OK with prompt template (analog to this prompt structure) — Phase 4 drafts directly serve as Stage 2 input.

## §11 Final closure

**Packet status:** AWAITING-RUSLAN-ACK (Stage 1 of 6)
**Acker:** Ruslan
**Next action:** Ruslan reviews tier options §2, R12 auto-pair rules §4, IP-1 executor-binding template §5; selects tier + fills ack template §7
**Estimated Ruslan review time:** 20-40 min (reading Phase reports 1-5 referenced — total ~2500 lines of drafts)

---

*Packet closure 2026-05-24. R2 STRICT preserved throughout 7-phase chain. All Foundation infrastructure modifications gated through this AWAITING-APPROVAL packet per Part 6b §I.4 stage_gate convention. Ruslan ack via packet §7 ack template required before Stage 2+ execution.*
