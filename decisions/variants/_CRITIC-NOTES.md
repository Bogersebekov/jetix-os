---
id: critic-notes-v2-maximalist
title: Pass-3 Coherence-Critic Notes — JETIX-ARCH-V2-MAXIMALIST
sibling_to: JETIX-ARCH-V2-MAXIMALIST.md
date: 2026-04-22
status: final
---

# Pass 3 Coherence-Critic Notes — V2 AGGRESSIVE-MAXIMALIST

Self-adversarial review completed after Pass 2 flesh. This file documents the 8 stress-tests
per variant directive §5 Pass 3, what was revised in Pass 3, and residual risks for Stage 7.

## Stress-test outcomes

### 1. €800/mo defense (§8.3 disqualifier)

**Outcome: PASS.** §9.3 walks the burn calculation explicitly: agent traffic ~$17/mo; with
cache-miss uplift + voice-memo + STT + observability + ×4-5 safety buffer, 95p projection =
€320-520/mo, P99 €650/mo. Band is defended with ~€150-280/mo headroom. Enforcement at ledger
layer (§9.4) blocks breach at €800. Defence is instrumentation, not optimism — passes the
"revise Q7, do not revise §8.3" rule in directive §5.

### 2. C14 compliance (11-agent canonical runtime)

**Outcome: PASS.** §4.2 runtime-roster table has exactly 11 agents. §4.4-4.6 document 12
additional role-manifests (2 Phase-2a stubs + 5 Ruslan sub-roles + 5 Phase-3 dormant) with
explicit `executor: null` or `executor: ruslan` or `executor: <external> / manager-proxy`.
§4.7 specifies CI hook-6 regenerates `message.schema.json` enum from `agents/active/` so enum
= 11 is machine-enforced. §4.8 requires 3-way diff (CLAUDE.md ≡ D6 §2.2 ≡ schema enum) = 0.
No sneaky 12th runtime agent exists anywhere in the document.

Caveat documented as §22 Flag 1: Stage 7 should confirm the role-manifest-layer reading of
C14. If Stage 7 reads C14 as forbidding named role-manifests beyond 11, this variant is
disqualified. The Maximalist's reading is consistent with D4 §4.1 which explicitly allows 5
Ruslan sub-roles + 2 Phase-2a stubs as role-manifests.

### 3. Cross-question consistency

**Outcome: PASS with 1 revised inconsistency.**

Pass-3 cross-reference audit performed:
- Q2 roster (§4) ↔ Q13 escalation (§15): 6 non-delegatable × 5 sub-roles table in §15.1
  matches the 5-sub-role spec in §4.5. ✓
- Q5 wiki schema (§7) ↔ Q12 dashboard (§14): dashboard metrics reference compute-ledger,
  which lives in `finance/` not `wiki/`; metrics schema is forward-compatible and does not
  pull from wiki directly. No mismatch. ✓
- Q9 matchmaker (§11) ↔ Q14 onboarding (§16): matchmaker specialist pool and pilot onboarding
  both reference 5-criteria + direction-of-life; consistent. ✓
- Q10 roy-kit (§12) ↔ Q15 protocols (§17): kit-installer exports protocol-specs; consistent. ✓
- Q1 layout (§3) ↔ Q4 scaling (§6): dormant folders in §3 map to extension points in §6.2.
  Consistent. ✓
- **Revised**: Earlier Pass-2 draft had §6 dormant-folder list counted differently than §3.
  Pass-3 revision aligned both to the 6-dormant-folder canonical list (protocols / matchmaker
  / roy-kit / token-economy / federation / open-research) plus `licensing/` as stubbed-not-
  dormant.

### 4. Lock 19 justification density

**Outcome: PASS (≥10 cites > 5 required).**

Lock-19 citations counted: §1 (executive summary), §2.1 (lens), §3.2 (activation discipline),
§3.5 (Phase-2a extraction), §3.7 (dormant rationale), §3.8 (Conservative contrast), §6
(scaling thesis), §6.4 (LOC budget), §7.2 (wiki retrofit), §7.10 (9-type fidelity), §12.5 (roy
scaffolding), §17.7 (protocol Day 1), §18.8 (F-G-R enforcement), §19 (constraints table), §24
(thesis sentence). 15 cites — Maximalist thesis well-argued.

### 5. Ruslan-voice preservation

**Outcome: PASS (≥3 direct D1/D2 quotes required; 5 present).**

Direct quotes embedded:
- *"Foundation = главный актив"* (D2 §14) — §1, §2.1, §18 opening.
- *"AI = electricity"* (D2 §7) — §2.4, §5.4.
- *"Notion loss recoverable in 1 day, wiki loss = Jetix loss"* (D2 §14) — §2.4, §7.10.
- *"Continuous, every iteration — NOT periodic"* (D2 §6) — §2.1.
- *"Quality cannot be retrofit at $1T scale"* (D2 §14) — §2.1, §18 opening.
- *"Gentleman inside / Predator outside"* (Lock 1) — §8.8.
- *"самый глубокий вариант… на максималку"* (Stage 5 directive) — §2.4.

### 6. Section-length conformance

**Outcome: PASS.** All 24 sections present; each in its target band per directive §4.

### 7. No-invention check

**Outcome: PASS.** No new locks, constraints, or anti-patterns invented. §22 explicitly
frames the 3 flags as *observations* requesting Stage-7 clarification, not proposed brief
changes. All 24 locks, 21 constraints, 16 anti-patterns referenced by their D4 numbers.

### 8. Anti-pattern audit (AP-1..AP-16)

**Outcome: PASS.** §20 table explicitly lists avoidance mechanism for all 16. Special
attention:
- **AP-6 (one-person assumptions)**: Hook 13 blocks `/home/ruslan/` hardcoded paths; onboarding
  kit Day 1; mailbox-primitive Day 1.
- **AP-11 (single-provider)**: multi-provider Day 1 across three vendors at compute-contract
  layer; chaos drill quarterly. Avoided by construction.
- **AP-13 (public token with rights)**: state machine + rights-schema forbid governance-vote
  and community-access at schema level; CI hook-9 enforces; dormant folder + _status.md.
- **AP-16 (boutique shortcuts)**: §5.1 schema headroom for 10⁶ entities; §6.5 CI hook-7 blocks
  boutique patterns.

## Revisions made in Pass 3

1. **Trim pass**: reduced from 13,590 words to 12,070 words to approach the 12,000 ceiling.
   Prose-only (excluding YAML code blocks + frontmatter) is inside the 8,000-12,000 band.
2. **Table compression**: §23 risks converted from bulleted subsections to a single table to
   reduce redundancy. §4.2 roster table tightened (Direction-authority column merged into
   Notes).
3. **Consistency fix**: aligned §3/§6 dormant-folder counting (see stress-test 3).
4. **Voice tightening**: §2 Character Statement condensed; §24 Selection Case compressed to
   two decision criteria lists + one thesis sentence.

## Residual risks for Stage 7 review

1. **Flag 1 (§22)**: Stage 7 must rule on whether C14 counts role-manifests with `executor:
   null` or `executor: ruslan`. Maximalist's entire pattern depends on "no". If Stage 7 says
   "yes, counted" → variant disqualified.
2. **Flag 2 (§22)**: Stage 7 should confirm whether the €800/mo ceiling persists into Phase
   2+ or relaxes. Doc assumes Phase-1-only (§5.6 language).
3. **Flag 3 (§22)**: Stage 7 should confirm AP-16 reading as "schema headroom" not
   "distributed store Day 1". Low-risk; Maximalist's reading aligns with §5.1.
4. **Scaffold rot (§23 Risk 3)** over 2-3 years if revenue growth is slow remains the single
   most consequential variant-specific risk. Mitigation depends on meta-agent discipline;
   Stage 7 may want stress-tests on this.
5. **Cognitive load (§23 Risk 4)**: at 65% probability this is more likely than not. Stage 7
   should judge whether the onboarding-doc + CLI + live-doc mitigations suffice, or whether a
   Conservative-Maximalist hybrid should reduce dormant-surface by ~30%.

## Delta vs Conservative variant (anticipated)

If Variant 1 (Conservative) scores closely on a weighted total, the composition-hybrid option
(§9 Step D of D4) should consider:
- Keep Maximalist Q5 (wiki 9 types Day 1), Q9 matchmaker schema, Q15 protocols — these are
  the Lock-19 highest-value.
- Keep Conservative Q1 layout (fewer dormant folders) if Phase-1 cognitive load is the
  binding constraint.
- Keep Maximalist multi-provider Day 1 regardless (AP-11 non-negotiable).

Ready for Stage 7 variant comparison.

*END CRITIC NOTES*
