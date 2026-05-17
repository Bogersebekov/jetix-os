---
title: AWAITING-APPROVAL packet — Legacy 12-agent roster deprecation (D-05 ack)
date: 2026-05-17
type: awaiting-approval
gate_class: stage_gate
gate_type: irreversible (architectural — affects CLAUDE.md substrate per Pillar A territory)
blast_radius: F3
ack_status: ACKED (Ruslan explicit prompt §0.6 «удалить нахуй»)
ack_record:
  - date: 2026-05-17
    ack_type: explicit-ack-via-prompt
    ack_text: "Ruslan §0.6: «Удалить нахуй — Ruslan explicit. Actions: ... AWAITING-APPROVAL packet для CLAUDE.md change ... Ruslan ack этого prompt'a = ack packet contents.»"
    ack_source: prompts/phase-0-plus-ruslan-acks-2026-05-17.md §0.6
    ack_note: "Ruslan ack via explicit prompt instruction = stage_gate ack per Part 6b §I.4. Packet contents authored brigadier-scribe based on §0.6 explicit instruction list."
parent_decisions:
  - reports/voice-pipeline-2026-05-17-batch/04-detailed-work-plan.md §5 D-05
  - reports/phase-0-fpf-scope/01-jetix-objects-inventory.md OQ-9 + D-mgmt-2
  - reports/phase-0-fpf-scope/04-kasha-cleanup-flags.md CR-08 (12 agents = role-type vs executor-token)
constitutional_posture:
  - R1 — Ruslan = sole strategist; this packet = execution of his ack, not author
  - R2 — CLAUDE.md = Pillar A strategic substrate; packet authored per AWAITING-APPROVAL convention before write
  - R6 — provenance per legacy agent file (git history preserved via git mv, not git rm)
  - Append-only — packet preserves audit trail; CLAUDE.md gets DEPRECATED markers (not deletion)
F: F4
G: legacy-agents-deprecation-packet
R: refuted_if_ROY_swarm_agents_inadvertently_archived_OR_audit_trail_broken_OR_Ruslan_revokes_ack
---

# AWAITING-APPROVAL — Legacy 12-agent roster deprecation

## §1 Scope

**14 agent files** to archive via `git mv .claude/agents/<file>.md .claude/agents/_archived/<file>.md`:

**Phase 1 (3):**
- `manager.md` (MGMT — coordination hub)
- `personal-assistant.md` (OPS — productivity)
- `system-admin.md` (OPS — infrastructure)

**Phase 2 (5):**
- `sales-lead.md` (Sales — coordination)
- `sales-researcher.md` (Sales — prospect research)
- `sales-outreach.md` (Sales — outreach)
- `inbox-processor.md` (Brain — triage)
- `crazy-agent.md` (Meta — creative disruption)

**Phase 3 (2):**
- `knowledge-synth.md` (Brain — synthesis lead)
- `strategist.md` (MGMT — strategic decisions)

**Phase 4 (2):**
- `life-coach.md` (Life — wellness)
- `meta-agent.md` (Meta — system auditing)

**Utility scribes (2):**
- `staging-writer.md` (system-design staging writer)
- `sweep-worker.md` (Notion sweep batch worker)

**TOTAL: 14 files** moved to `.claude/agents/_archived/`.

## §2 NOT in scope (ROY swarm agents — STAY ACTIVE)

**9 ROY swarm agents preserved in `.claude/agents/`:**

| Agent | Function |
|---|---|
| `brigadier.md` | ROY orchestrator (canonical) |
| `engineering-expert.md` | ROY engineering domain |
| `investor-expert.md` | ROY investor domain |
| `mgmt-expert.md` | ROY mgmt / PM domain |
| `philosophy-expert.md` | ROY philosophy domain |
| `systems-expert.md` | ROY systems-thinking domain |
| `project-brigadier.md` | Project mini-swarm orchestrator template |
| `quick-money-brigadier.md` | quick-money project mini-swarm |
| `levenchuk-deep-dive-brigadier.md` | Levenchuk project mini-swarm stub |

Per Ruslan ack §0.6 explicit: «НЕ touch'ать ROY swarm agents (brigadier / engineering-expert / philosophy-expert / systems-expert / mgmt-expert / investor-expert / autoresearch-brigadier / project-brigadier / quick-money-brigadier / levenchuk-deep-dive-brigadier stub) — они active operational.»

Note: prompt mentions `autoresearch-brigadier` in keep-list — file not present in current `.claude/agents/` listing. Safe-treat = preserved per blanket «NOT touch ROY» rule.

## §3 Actions

1. ✅ Write this AWAITING-APPROVAL packet (this file) — DONE 2026-05-17
2. `mkdir -p .claude/agents/_archived/`
3. `git mv .claude/agents/<file>.md .claude/agents/_archived/<file>.md` для каждого of 14 listed files (preserves git history)
4. Update `CLAUDE.md ## Architecture` — change «12 specialized agents» phrasing
5. Update `CLAUDE.md ## Agent Roster` — mark all 14 как `DEPRECATED-2026-05-17 — Ruslan-acked via voice-batch processing` (preserve section per append-only; не delete table)
6. Add `CLAUDE.md ## Active ROY Swarm` new section listing 9 ROY agents (per §2 above)
7. Update `swarm/lib/routing-table.yaml` header comments to flag legacy-roster section deprecated
8. Commit с message «[deprecation][legacy-12-agents] D-05 Ruslan ack — archive 14 files + CLAUDE.md DEPRECATED markers»

## §4 Rationale (Ruslan voiced, per §0.6 + work-plan §5 D-05)

- Legacy 12-agent roster (declared Phase 1-4 в CLAUDE.md 2026-04 baseline) mailboxes stale since 2026-04-15
- ROY swarm (brigadier + 5 experts + 4 sub-brigadiers) operational и dispatching since Phase A bootstrap
- Phase 0 inventory CR-08 / CE-2 flagged «12 agents» как type-token confusion (role-type declarations ≠ running executors)
- Maintaining declared-but-stale roster = ongoing IP-1 violation + ongoing «caña» в L1 audience documentation
- Ruslan voiced through audio_672-673 team-building intent с ROY swarm (FPF cooperation language); legacy 12 НЕ relevant

## §5 Risks & mitigations

| Risk | Mitigation |
|---|---|
| Tool subagent_type references break | Tool list will fall back to claude-default; user reminder noted в commit message |
| External callers ref legacy slugs | `_archived/` preserves files for reference; not deleted |
| Audit trail broken | `git mv` preserves history (NOT `git rm` + `git add`); commit message captures intent |
| ROY swarm accidentally touched | §2 explicit keep-list + brigadier double-check before bash |
| Ruslan changes mind | Reverse via `git mv .claude/agents/_archived/<file>.md .claude/agents/<file>.md` (idempotent) |

## §6 Constitutional discipline

- **CLAUDE.md = Pillar A strategic substrate** per Bundle 5 ack 2026-04-28 → R2 requires AWAITING-APPROVAL packet → this file
- **Ruslan ack via prompt §0.6** = packet content authorization (explicit phrasing «Ruslan ack этого prompt'a = ack packet contents»)
- **Append-only** preserved: CLAUDE.md table marked DEPRECATED, не deleted; agent files moved, не removed
- **Default-Deny** respected: no novel uncategorized action; this is deprecation of declared substrate per existing CR-08 / D-05 pattern

## §7 Acceptance criteria

- [ ] 14 files relocated к `.claude/agents/_archived/` (git mv preserves history)
- [ ] 9 ROY swarm agents untouched в `.claude/agents/`
- [ ] CLAUDE.md ## Architecture phrasing updated
- [ ] CLAUDE.md ## Agent Roster table marked DEPRECATED-2026-05-17 (each row OR section header)
- [ ] CLAUDE.md ## Active ROY Swarm new section added
- [ ] swarm/lib/routing-table.yaml header comment flag
- [ ] git commit with proper message + body capturing rationale
- [ ] This packet remains в swarm/awaiting-approval/ as audit trail (not moved to /processed)

---

*Brigadier scribe authored per Ruslan §0.6 explicit ack. §5.5.5 gate: provenance ✓ inline (prompts/phase-0-plus-ruslan-acks-2026-05-17.md §0.6 + work-plan §5 D-05 + Phase 0 CR-08) / blast_radius F3 (architectural-not-foundation) / R1+R2+R6+append-only preserved ✓ / explicit keep-list ROY ✓ / risk mitigations ✓.*
