---
title: "Plan — Monetization Methodology Wave 2 Deeper Mining"
date: 2026-05-14
type: plan-mode-mirror
scope: F5 Wave 2 expansion (server CC autonomous execute)
parent_prompt: prompts/jetix-monetization-phase-5-deeper-mining-2026-05-14.md
parent_deliverable: decisions/JETIX-MONETIZATION-AUDIENCE-COOPERATION-METHODOLOGY-v0-2026-05-14.md
provenance_base_commit: eebdcc2
status: ai-draft-pending-ruslan-revision
prose_authored_by: ai-draft-pending-ruslan-revision
constitutional_anchor: |
  Tier 2 R1 (NO selection / NO ack-forcing / NO Q-evening).
  Tier 2 R2 (no Foundation-path writes / no v0 edit — append-only).
  Tier 2 R6 (provenance per item).
  Tier 2 R11 (Default-Deny).
  Tier 2 R12 (anti-extraction audit per H-M).
  Append-only.
ruslan_directive_2026-05-14: |
  "Вопросы меня не сильно ебут. Не должны о них даже сотреть.
  Сейчас мы собираем информацию чтобы потом на эти вопросы отвечать.
  Все подряд нахуй! Все гипотезы потом тестировать."

  Translation: Wave 2 = catalog ALL variants. NO selection. NO ack-forcing.
  Open Q = hypotheses, не decisions. Breadth > narrowing. Surface > select.
tags:
  - "#type/plan"
  - "#topic/monetization"
  - "#topic/audience-cooperation"
  - "#status/ai-draft-pending"
  - "#priority/critical"
---

# PLAN — Monetization Methodology Wave 2 Deeper Mining

> **Mirror** of Plan-Mode original. Server CC autonomous-execute style; not a Plan-tool gate.
> Wave 2 = DEEPER MINING on top of v0 (commit `1e411ee`). v0 не редактируется (R2 / append-only).

---

## §0 Posture (Wave 2 reaffirm)

- **NO LOCK** на любые H. Все остаются `hypothesis-pool` / `ai-draft-pending`.
- **NO Q-evening** structure — 15 Open Q переклассифицируются как hypothesis clusters.
- **BREADTH > narrowing** — каждое направление расширяется, не сужается.
- **Catalog > recommend** — ни одна selection не делается AI'ем.
- **R12 audit** на каждую новую H-M.
- **Provenance** per item (Tier 2 R6).
- Foundation paths — forbidden (R2).
- Charter / Pitch / Video script — cite only, не edit (R2).

---

## §1 Что делается (8 phases)

| # | Phase | Output | Estimate |
|---|-------|--------|----------|
| 2a | Test designs | 75 how-to-test cards в `reports/monetization-research-2026-05-14/wave2/hypothesis-test-designs/` (5 subdirs H-M/H-A/H-C/H-F/H-O) | 3-5h |
| 2b | Q expansion | 15 Q × ≥4 sub-H = ≥60 sub-hypotheses → `q-expanded-as-hypotheses.md` | 1-2h |
| 2c | Books deep extracts | ≥15 book extracts (Tier 1 must + Tier 2 if time) → `books-deep-extracts/<slug>.md` | 2-4h |
| 2d | Industry numbers deep | ≥20 examples с MAU/ARPU/LTV/CAC/take rate/churn/coop indicators/R12 → `industry-numbers-deep.md` | 1-2h |
| 2e | Path to state per-phase | 6 docs (`phase-1.md..phase-6.md`) с jurisdictional / financial / legal / governance / risks / precedents | 2-3h |
| 2f | Cross-pollination | matrix mermaid + condensed top-20 C/A + top-10 B/R → `cross-pollination-matrix.md` | 1h |
| 2g | New H surfacing | continuous; integrate as found → `new-hypotheses-surfaced-wave2.md` | (integrated) |
| 2h | Main Wave 2 doc + commit + push | `decisions/JETIX-MONETIZATION-METHODOLOGY-WAVE2-DEEPER-MINING-2026-05-14.md` + tag `[monetization-methodology][wave2][deeper-mining]` + push main | 1h |

**Total estimated:** 12-22h (split possible across sessions).

---

## §2 Card schema (per H — Phase 2a)

```markdown
## H-X-NNN — <name>

**Hypothesis statement:** <text>
**Why test:** <signal we'd learn>
**Minimum viable test:**
  - Setup: <что нужно подготовить>
  - Cohort: <кто участвует, N>
  - Duration: <weeks / months>
  - Cost: <€>
**Success metric:** <quantitative threshold>
**Failure metric:** <quantitative kill criterion>
**Confounders:** <что может исказить>
**Precedent test:** <кто-то ещё это тестировал? результат?>
**Phase fit:** <Phase 1 / 2 / 3 / 4+>
**Required L1 fit:** <какой тип partner нужен>
**R12 retest:** <как verify R12 holds during test>
**Cross-pollination:** <какие H блокируют / усиливают>
**Bayesian prior:** <high / medium / low>
**Provenance:** [src: ... | commit eebdcc2]
```

---

## §3 Q expansion schema (Phase 2b)

Per Q (15 total):
- Re-classify Q как hypothesis cluster `HQ-XX-NNN-A..N`
- Min 4 sub-hypotheses per Q
- Each sub-H gets condensed how-to-test entry (subset of full card schema)
- Surface ALL variants (включая ones AI бы «не выбрал»)
- R12 audit на новые monetization sub-H

---

## §4 Books deep extract schema (Phase 2c)

Per book — 1 file `<book-slug>.md`:
- 3-5 ключевых концепций relevant к Jetix
- Где fits в 75 H / 60+ sub-H / 15 Q clusters
- 1-2 mermaid diagrams (where concept визуально насыщенный)
- Direct quotes (mark attribution; paraphrase + cite, no large quotes — copyright respect)
- Open application questions (что нужно тестировать)
- Provenance footer

**Tier 1 (must mine — ≥8):**
1. Castronova — *Synthetic Worlds*
2. van Dreunen — *One Up*
3. Axelrod — *Evolution of Cooperation*
4. Srinivasan — *Network State* (covered via existing wiki; sharpen)
5. Schelling — *Strategy of Conflict*
6. Cialdini — *Influence*
7. Whyte & Whyte — *Mondragón Cooperative Experience*
8. Raymond — *Cathedral and Bazaar*

**Tier 2 (good to have — ≥7 to reach 15+):**
9. Shapiro & Varian — *Information Rules*
10. Christensen — *Innovator's Dilemma*
11. Levy — *Hackers*
12. Doctorow — *Walkaway* (cooperation fiction)
13. Suarez — *Daemon / Freedom* (gamified networked corp fiction)
14. Carse — *Finite and Infinite Games*
15. Ostrom — *Governing the Commons* (8 design principles)
16. Nowak — *SuperCooperators*
17. Henrich — *WEIRDest People in the World*

---

## §5 Industry numbers schema (Phase 2d)

Per example:
- **MAU / DAU** (current public estimate; flag «private» where unknown)
- **ARPU** (Average Revenue Per User)
- **LTV** (Lifetime Value, where derivable)
- **CAC** (Customer Acquisition Cost, where derivable)
- **Take rate** / revenue split
- **Churn / retention**
- **Cooperation indicators** (peer-to-peer / Discord activity / community-generated content rate)
- **R12-equivalent posture** (extracts beyond agreed share? fork-and-leave possible?)

**Targets (~25 candidates → ≥20 with numbers):**
- Patreon / Substack / Twitch / OnlyFans / Discord Boost / Roblox / Steam Workshop / Reddit / Stack Overflow / GitHub Sponsors
- Mr Beast / Дудь / Веритасиум / Lex Fridman / Tim Ferriss / Naval / Stratechery (Ben Thompson)
- Bankless DAO / Gitcoin / Optimism Collective / Nouns DAO
- Mondragón Corp / John Lewis Partnership / REI Co-op / Ocean Spray Cooperative
- Próspera / Estonia e-Residency / Liberland / Seasteading Institute

---

## §6 Per-phase deep-dive schema (Phase 2e)

Per phase (1..6) — 1 file:
- **Membership threshold deep** (sources; comparable orgs at scale)
- **Revenue model deep** (что монетизирует; R12 check at scale)
- **Governance structure deep** (кто решает что; voting / committee / hybrid)
- **Legal jurisdiction deep** (Estonia / Próspera / Liberland / multi-juris)
- **Cultural / brand maintenance** (что happens с brand identity при scale jump)
- **Risks per phase** (что может убить переход)
- **Precedents** (кто реально дошёл)
- **External recognition criteria** (что нужно чтобы «считаться» state)

---

## §7 Cross-pollination matrix schema (Phase 2f)

- Rows × Cols: 135 H entries (75 v0 + ~60 sub-H from Q expansion)
- Cell legend: **C** (Combines well) / **N** (Neutral) / **B** (Blocks / Conflicts) / **A** (Amplifies — strong combo) / **R** (Replaces — same purpose)
- Full matrix не пишется (3D bytes); condensed:
  - Mermaid graph showing top-30 strongest C/A edges
  - Table top-20 strongest C/A combinations
  - Table top-10 strongest B/R conflicts

---

## §8 New H surface protocol (Phase 2g)

Continuous protocol during all phases:
- New direction surfaces → add как `H-X-NNN` (continuing numbering: H-M-019+, H-A-019+, H-C-019+, H-F-011+, H-O-012+, H-N-001+ new buckets)
- Full how-to-test card per §2 schema
- R12 audit if H-M
- Provenance per item
- Log entry in `new-hypotheses-surfaced-wave2.md`

**Hint regions:**
- Cooperation theory × Christianity / Buddhism / Stoicism
- AI-augmented coordination (post-LLM mechanisms)
- Reputation cascade physics (Shannon entropy)
- Cross-species (ant colonies / bee swarms / experimental Tit-for-Tat data)
- Memetic engineering (Dawkins / Dennett)
- Cult mechanics ethical engineering (CrossFit / SoulCycle / Burning Man without harm)
- Indie hacker / bootstrapped SaaS (Pieter Levels / Levels.fyi)
- Influence asymmetries (long-form podcast → listener cooperation)

---

## §9 Constitutional reaffirm (per prompt §5 + §8)

1. **R1 — NO LOCK / NO recommendation phrasing.** «Suggested» → «If tested, would resolve / If pursued, would generate signal».
2. **R2 — NO Foundation writes.** No edits to `swarm/wiki/foundations/`, `principles/`, `shared/schemas/`, `.claude/config/`. Cite only.
3. **R2 — Append-only к v0.** Не модифицировать `JETIX-MONETIZATION-AUDIENCE-COOPERATION-METHODOLOGY-v0-2026-05-14.md`.
4. **R2 — Charter / Pitch / Video LOCKED.** Cite only.
5. **R6 — Provenance per item.** Каждое claim → `[src: ... | commit eebdcc2]`.
6. **R11 — Default-Deny.** Novel actions → categorize at `.claude/config/default-deny-table.yaml`; uncategorized → halt-log-alert.
7. **R12 — anti-extraction audit** на every H-M (new or expanded). Mark explicit pass / concern / fail; surfacing fails не запрещён — это valid hypothesis even if extracts.
8. **CRM disambiguation** = hypothesis (HQ-CR-010-A..N), не resolve.
9. **8th insight Standards Body** = hypothesis (HQ-SB-008-A..N), не promote.
10. **Halt-worthy** → `awaiting-approval/halt-monetization-wave2-2026-05-14.md` + flag.

---

## §10 Phase order + status update protocol

Sequential 2a → 2b → 2c → 2d → 2e → 2f → 2g (continuous) → 2h.

Status updates: 1-line ack per phase milestone в чат («Wave 2 phase 2a done — 75/75 cards»).

If split across sessions: each session starts с TaskList check + read of `MEMORY.md` + this plan-mirror.

---

## §11 Success criteria (Wave 2)

- ≥75 how-to-test cards
- ≥60 sub-H from Q expansion
- ≥15 book deep extracts (≥8 Tier 1)
- ≥20 industry examples с concrete numbers
- 6 phase deep dives
- Cross-pollination matrix (condensed top-50 form acceptable)
- Wave 2 main doc summarizing all expansions
- Commit + push + chat ack
- Total hypothesis count surfaced (v0 + Wave 2) ≥ **150**

---

## §12 What is NOT done (R2 / R1 boundary affirm)

- ❌ NO selection между H-M / H-A / H-C / H-F / H-O variants
- ❌ NO Phase 1 deployment priority recommendation
- ❌ NO «best variant» calculation
- ❌ NO Standards Body H8 promotion
- ❌ NO CRM disambiguation resolution
- ❌ NO Charter / Pitch / Video script edit
- ❌ NO Foundation Parts / principles / schemas edit
- ❌ NO timeline scenario selection (Aggressive / Moderate / Conservative)
- ❌ NO Workshop One Commandment pick
- ❌ NO LOCK signatures

All of the above remain в Ruslan's exclusive authorship territory (Tier 2 R1).

---

## §13 Provenance

- **Parent prompt:** `prompts/jetix-monetization-phase-5-deeper-mining-2026-05-14.md` (Wave 2 trigger; commit `eebdcc2`)
- **Parent v0:** `decisions/JETIX-MONETIZATION-AUDIENCE-COOPERATION-METHODOLOGY-v0-2026-05-14.md` (commit `1e411ee`)
- **Parent canonical (cite only):**
  - `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md`
  - `decisions/JETIX-CORPORATION-2026-05-05.md`
  - `decisions/JETIX-TRM-MODEL-2026-04-30.md`
  - `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md`
  - `decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md` (H6)
  - `decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md` (H7)
  - `decisions/STRATEGIC-INSIGHT-JETIX-PARTNERSHIP-MODEL-2026-05-10.md` (H2)
  - `decisions/STRATEGIC-INSIGHT-BALAJI-NETWORK-STATE-2026-05-10.md`
- **Research base:** `reports/monetization-research-2026-05-14/` (4 files; line counts 114 / 186 / 247 / 185)
- **Constitutional anchors:** Foundation v1.0 LOCKED 2026-04-28; Heptagon LOCKED 2026-05-12; Charter v0 LOCKED 2026-05-12; R12 packet 2026-05-12.

**Plan complete. Execution begins Phase 2a.**
