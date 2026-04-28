---
title: "Tier 2 foundation_generic — 11 hard rules MOC"
date: 2026-04-28
type: tier-2-foundation-generic-moc
F: F8
G: "Foundation generic — mirror of FUNDAMENTAL §6.1 (constitutional)"
R: R-high
created_date: 2026-04-28
---

# Tier 2 foundation_generic — 11 constitutional hard rules

Mirror of `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` §6.1.
Per Pillar C §A.1 invariant: count == 11; each file maps to exactly one
FUNDAMENTAL §6.1 rule via `fundamental_anchor:` frontmatter.

| # | Slug | FUNDAMENTAL §6.1 rule | Part 6b action_class |
|---|---|---|---|
| 1 | [ai-does-not-strategize](ai-does-not-strategize.md) | rule 1 | ai_strategize_or_set_direction |
| 2 | [ai-does-not-execute-architectural-decision](ai-does-not-execute-architectural-decision.md) | rule 2 | ai_execute_architectural_decision |
| 3 | [ai-does-not-set-skill-direction](ai-does-not-set-skill-direction.md) | rule 3 | ai_set_skill_direction |
| 4 | [ai-does-not-claim-persistent-identity](ai-does-not-claim-persistent-identity.md) | rule 4 | ai_claim_persistent_identity |
| 5 | [ai-does-not-claim-skin-in-the-game](ai-does-not-claim-skin-in-the-game.md) | rule 5 | ai_claim_skin_in_the_game |
| 6 | [ai-does-not-aggregate-unstructured-long-term-memory](ai-does-not-aggregate-unstructured-long-term-memory.md) | rule 6 | ai_aggregate_unstructured_long_term_memory |
| 7 | [agents-do-not-negotiate-contradictions-autonomously](agents-do-not-negotiate-contradictions-autonomously.md) | rule 7 | agents_negotiate_contradictions_autonomously |
| 8 | [agent-does-not-evaluate-peer-agent](agent-does-not-evaluate-peer-agent.md) | rule 8 | agent_evaluate_peer_agent |
| 9 | [ai-does-not-self-modify-at-runtime](ai-does-not-self-modify-at-runtime.md) | rule 9 | ai_self_modify_at_runtime |
| 10 | [ai-does-not-impersonate-human-externally](ai-does-not-impersonate-human-externally.md) | rule 10 | ai_impersonate_human_externally |
| 11 | [bypass-blast-radius-categorization-forbidden](bypass-blast-radius-categorization-forbidden.md) | rule 11 | bypass_blast_radius_categorization |

## Sync invariants

- Pillar C foundation_generic ↔ Part 6b `.claude/config/default-deny-table.yaml` constitutional_never_list — count + hash match (lint enforced)
- Pillar C foundation_generic ↔ CLAUDE.md §4.1 inline — hash match (lint enforced)
