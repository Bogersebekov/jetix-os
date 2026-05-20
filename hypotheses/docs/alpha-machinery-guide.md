---
title: Alpha-machinery guide — applying OMG Essence к hypothesis tracking
date: 2026-05-20
type: documentation
parent_layer: 6
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: hypotheses-alpha-machinery-guide
R: low
---

# Alpha-machinery Guide

> Practical how-to для применения OMG Essence alphas к hypothesis tracking.

## §1 When to use alphas

**Not every hypothesis needs alpha tracking.** Use them when:
- Hypothesis is **multi-month** (lifecycle: medium / long)
- Multiple stakeholders OR multi-party interaction (catallactic / game-theory regions)
- Complex method/artefact development (software-system + work alphas useful)

**Skip alphas for:** short experiments (1-7d), purely informational hypotheses, или
quick personal-dev tests где tracking overhead > value.

## §2 Choosing alphas per hypothesis category

| Category | Recommended alphas |
|---|---|
| **outreach** | stakeholder (primary) + opportunity |
| **engineering** | software-system + requirements + work |
| **method** | way-of-working + work |
| **pitch** | stakeholder + opportunity (audience-resonance focus) |
| **business** | opportunity + stakeholder + requirements |
| **personal-dev** | way-of-working OR team={ruslan} |
| **partnership** | stakeholder (primary) + team + opportunity |
| **fpf-extension** | way-of-working + requirements + software-system |

## §3 5 регионов стратегирования mapping

Per `hypotheses/_schema/fpf-strategic-regions.yaml` + Левенчук Гл. 6:

### Robinson Crusoe
- stakeholder = self only (skip alpha)
- team = {ruslan} (formed implicit)
- Focus: way-of-working + work
- **Example:** «утренняя медитация улучшает focus» — solo experiment

### Catallactica (most Jetix outreach/business)
- stakeholder = central; multi-state tracking key
- opportunity = explicitly value-prop articulation
- team = multi-party
- **Example:** Partnership hypothesis (H-002 vintage)

### War (adversarial / competitive)
- stakeholder = competitor's stakeholders также tracked
- Track *both sides*: own and opponent's alphas
- **Example:** «competitor X movement в market Y; defensive positioning»

### Game-theory (mixed motives)
- Multiple stakeholders; equilibrium analysis
- team alpha может tracks coalition formation
- **Example:** Founding Circle equity split hypothesis

### Unknown (genuine novelty)
- opportunity alpha слабо defined initially
- way-of-working alpha tracks exploration practice
- **Example:** Deep FPF extension exploration

## §4 Skill workflow

```bash
# Set initial alpha state when adding hypothesis (manual via /hypothesis-update OR direct edit)
/hypothesis-alpha-state H-NNN --alpha stakeholder --state recognized --note "L2 founder partner identified"

# Update as work progresses
/hypothesis-alpha-state H-NNN --alpha stakeholder --state represented --note "direct contact established"
/hypothesis-alpha-state H-NNN --alpha work --state started --note "outreach sequence sent"

# View state trail (auto-appended)
cat hypotheses/alphas/state-graphs/H-NNN-alpha-trail.md
```

## §5 Transition discipline

**Monotonic progression default:** state index must increase per `_schema/alphas.yaml`.

**Reverse allowed только с** `--allow-reverse` flag (e.g., hypothesis discovers stakeholder regressed). Reverse must include detailed note explaining what happened.

**Multi-alpha update:** Multiple alphas can be at different states simultaneously (e.g., team=performing, work=concluded, stakeholder=involved). State of one alpha doesn't constrain others (except via natural dependencies — e.g., work concluded requires requirements addressed).

## §6 Foundation cross-link

Hypothesis alpha progression integrates with Foundation Parts:
- **Part 5** (Compound Learning): learning_extracted at hypothesis closure feeds substrate; alpha trail provides context
- **Part 7** (Project Lifecycle Substrate): stage-gates analogous mechanic; hypothesis closure → potential project bootstrap
- **Part 11** (Strategic Direction Substrate): high-F hypotheses confirmed → strategic insight candidates

## §7 Anti-patterns

- ❌ **Tracking all 7 alphas every hypothesis** — overhead; pick 1-3 relevant
- ❌ **Alpha state without note** — note required для transition context
- ❌ **Bulk alpha transitions** — Default-Deny per skill (R11); per-hypothesis evaluation
- ❌ **Alpha state contradicts hypothesis status** — e.g., status=confirmed but work=initiated; surface к Ruslan для resolution

## §8 Cross-refs

- **Source:** Левенчук Методология 2025 Гл. 4 + OMG Essence 2.0:2024
- **5 regions:** Левенчук Методология 2025 Гл. 6
- **Overview:** `hypotheses/alphas/_alphas-overview.md`
- **Per-alpha docs:** `hypotheses/alphas/*.md`
- **State graphs:** `hypotheses/alphas/state-graphs/*.md`
- **Skill:** `.claude/skills/hypothesis-alpha-state.md`
- **Schema:** `hypotheses/_schema/alphas.yaml`
- **FPF integration:** `hypotheses/docs/fpf-integration.md` (Layer 5 complement)
