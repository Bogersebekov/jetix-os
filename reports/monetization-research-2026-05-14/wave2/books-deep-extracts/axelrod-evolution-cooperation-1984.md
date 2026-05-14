---
book: "Axelrod, Robert — The Evolution of Cooperation"
year: 1984
tier: 1
mined_from: model knowledge + wiki/sources/evolution-cooperation-axelrod
date: 2026-05-14
provenance_base_commit: eebdcc2
---

# Axelrod — *The Evolution of Cooperation* (1984) — Deep Extract

## §1 Author + context

Robert Axelrod — political scientist, University of Michigan. *Evolution of Cooperation* (1984) presents results of his 1980 + 1984 computer tournaments for iterated prisoner's dilemma (IPD). Tit-for-tat strategy (TFT) by Anatol Rapoport won both tournaments against more sophisticated strategies; sparked 40 years of cooperation theory research.

## §2 Five key concepts relevant to Jetix

### Concept 1 — Tit-for-Tat (TFT) Wins IPD

Axelrod's tournament result: TFT (start cooperate; mirror opponent's last move) dominated 14 entries in 1980 + 62 entries in 1984. TFT properties:
1. **Nice** — never first to defect
2. **Retaliating** — punishes defection immediately
3. **Forgiving** — returns to cooperation after one retaliation round
4. **Clear** — simple to understand; opponents can predict

**Jetix mapping:** H-C-001 (rank visibility) + H-C-002 (Season retro) implement TFT mechanic:
- *Nice:* member starts с positive cooperation (Quest joint / mentor offer)
- *Retaliating:* defection signal → temporary cooperation withdrawal (rank visible signal)
- *Forgiving:* Season retro = forgiveness window (forgive after retaliation)
- *Clear:* algorithm transparency (HQ-RA-003-A/B options)

### Concept 2 — Shadow of the Future

Cooperation requires expectation of future interaction. Discount factor δ low (short horizon) → defection rational; δ high (long horizon) → cooperation Nash equilibrium. **Folk theorem of repeated games.**

**Jetix mapping:** Charter LOCKED 10-15y operational horizon (H-C-003) + Seasons 3-month (H-C-002) = 40-60+ iterations. Shadow of future is large. Cooperation should be Nash equilibrium per Axelrod's theorem. **Direct mathematical validation of Charter long-horizon design.**

### Concept 3 — Noise Problem

Real interactions have noise: actions misinterpreted; «defection» occurs accidentally. TFT under noise can spiral into mutual punishment.

**Jetix mapping:** Realm rank algorithm + peer review (per HQ-RA-003-B hybrid) добавляет dispute resolution layer (Tribunal H-F-007); reduces noise-spiral risk. Council mediates Clan-level disputes before formal rank drop (per v0 §3.3).

### Concept 4 — Cluster Cooperation (Group Selection)

Axelrod Ch.8 — cooperative strategies can invade defector populations if they can form clusters. Small clusters of cooperators interacting more with each other than with defectors → cooperation spreads.

**Jetix mapping:** Clan structure (E3, 3-10 members) = cooperative cluster. Charter manifest filter (H-C-008) selects cooperation-oriented partners → Realm forms cooperative cluster against external defector ecosystem. **Axelrod proves this strategy invades and spreads.**

### Concept 5 — Five Conditions for Cooperation

Axelrod's 5 conditions (Ch.10):
1. Future interaction (shadow of future)
2. Recognize past actions (memory)
3. Care enough about future (low δ)
4. Reciprocation possible
5. Cooperate first

**Jetix mapping:** All 5 conditions hold в Realm:
1. Charter 10-15y horizon
2. Rank visibility = memory (H-C-001)
3. Members optimize over Season + Year horizons
4. Quest payout reciprocation explicit
5. Manifest pattern (H-C-008) self-selects for «cooperate first» orientation

## §3 Jetix H mapping

| Jetix H | Axelrod validation |
|---------|---------------------|
| H-C-001 (rank visibility) | Memory layer of TFT |
| H-C-002 (Season retro) | Forgiveness window (avoid spiral) |
| H-C-003 (long-cycle commitment) | Shadow of future, folk theorem |
| H-C-008 (Manifest pattern) | Cooperate-first self-selection |
| H-C-010 (joint Quest split) | Reciprocation payout |
| H-F-007 (Tribunal) | Noise-handling dispute resolution |
| Charter Clan structure | Cooperative cluster invasion strategy |

## §4 Open application questions

- Optimal Season length (3-month per Charter) — does Axelrod theory predict different cadence?
- Noise tolerance threshold — at what defection-signal rate does TFT fail?
- Cluster size — Charter clans 3-10; Axelrod doesn't specify optimal; empirical question for Realm.

## §5 Direct quotes (paraphrased)

> «Cooperation does not require friendship and does not require foresight; it requires conditions of: durability of interaction, recognition of others, and a sufficient stake in the future.» — Axelrod Ch.4, paraphrased.
>
> «Tit-for-tat works because it is nice, provocable, forgiving, and clear.» — Axelrod Ch.6, paraphrased.

## §6 Provenance

[src: Axelrod *Evolution of Cooperation* 1984 Basic Books | wiki/sources/evolution-cooperation-axelrod | commit eebdcc2]
