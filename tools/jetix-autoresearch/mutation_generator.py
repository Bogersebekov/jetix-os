#!/usr/bin/env python3
"""mutation_generator.py — propose lens-config variant.

Two strategies, switchable per-experiment:
  (a) PROGRAMMATIC — deterministic perturbations of weights / thresholds /
      tier composition. Fast (~ms per propose). Used as default in pilot
      to keep wall-clock bounded.
  (b) LLM — Claude call via tools/lib/cc_helper.claude_call(). Slower
      (~10-30s per propose). Engaged via --llm-share=N (fraction of
      experiments using LLM propose).

Both strategies emit a `mutation` dict with the canonical shape:

    {
        "variant_name": "v00042",
        "strategy": "programmatic" | "llm",
        "changes": [{property, old_value, new_value, rationale}],
        "touched_files": [path_relative_to_repo_root],
        "blast_radius": "Tier-3",  # RUSLAN-LAYER cosmetic-config
        "lens_after": {...},        # full mutated lens config
    }

Mutations only touch the declared mutable_substrate (constitutional_gate
enforces). Programmatic mutations preserve weight normalisation
(sum w_* = 1.0).
"""

import copy
import json
import random
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

WEIGHT_KEYS = ("keyword", "semantic", "domain_element", "recency")


def _normalize_weights(w: Dict[str, float]) -> Dict[str, float]:
    """Renormalize so sum(w) == 1.0; clip to [0.05, 0.85]."""
    clipped = {k: max(0.05, min(0.85, float(v))) for k, v in w.items()}
    total = sum(clipped.values())
    if total == 0:
        return {k: 1.0 / len(clipped) for k in clipped}
    return {k: round(v / total, 4) for k, v in clipped.items()}


def _programmatic_mutation(lens: Dict[str, Any], rng: random.Random) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """Apply one of several deterministic mutation operators."""
    lens_after = copy.deepcopy(lens)
    changes: List[Dict[str, Any]] = []

    op = rng.choice([
        "weight_tweak", "weight_tweak", "weight_tweak",  # weighted toward weight tweaks
        "threshold_tweak", "top_n_tweak",
        "domain_weight_tweak", "tier_swap",
    ])

    if op == "weight_tweak":
        w = dict(lens_after.get("scoring_weights", {}))
        k = rng.choice(WEIGHT_KEYS)
        old = float(w.get(k, 0.25))
        delta = rng.choice([-0.10, -0.05, 0.05, 0.10])
        new = max(0.05, min(0.85, old + delta))
        w[k] = new
        normalized = _normalize_weights(w)
        lens_after["scoring_weights"] = normalized
        changes.append({
            "property": f"scoring_weights.{k}",
            "old_value": round(old, 4),
            "new_value": round(normalized[k], 4),
            "rationale": f"perturb {k} weight by {delta:+.2f} then renormalize",
        })

    elif op == "threshold_tweak":
        old = float(lens_after.get("threshold", 0.60))
        delta = rng.choice([-0.10, -0.05, 0.05, 0.10])
        new = round(max(0.20, min(0.95, old + delta)), 4)
        lens_after["threshold"] = new
        changes.append({
            "property": "threshold",
            "old_value": old,
            "new_value": new,
            "rationale": f"threshold {delta:+.2f}",
        })

    elif op == "top_n_tweak":
        old = int(lens_after.get("top_n", 20))
        delta = rng.choice([-5, -3, 3, 5])
        new = max(5, min(60, old + delta))
        lens_after["top_n"] = new
        changes.append({
            "property": "top_n",
            "old_value": old,
            "new_value": new,
            "rationale": f"top_n {delta:+d}",
        })

    elif op == "domain_weight_tweak":
        dw = dict(lens_after.get("domain_element_weights", {}))
        if dw:
            k = rng.choice(list(dw.keys()))
            old = float(dw[k])
            delta = rng.choice([-0.15, -0.10, 0.10, 0.15])
            new = round(max(0.0, min(1.0, old + delta)), 4)
            dw[k] = new
            lens_after["domain_element_weights"] = dw
            changes.append({
                "property": f"domain_element_weights.{k}",
                "old_value": old,
                "new_value": new,
                "rationale": f"domain weight {delta:+.2f}",
            })
        else:
            return _programmatic_mutation(lens, rng)

    elif op == "tier_swap":
        # Promote a tier-2 keyword to tier-1, or demote a tier-1 to tier-2.
        direction = rng.choice(["promote_t2_to_t1", "demote_t1_to_t2"])
        if direction == "promote_t2_to_t1" and lens_after.get("tier_2_keywords"):
            kw = rng.choice(lens_after["tier_2_keywords"])
            lens_after["tier_2_keywords"] = [k for k in lens_after["tier_2_keywords"] if k != kw]
            lens_after.setdefault("tier_1_keywords", []).append(kw)
            changes.append({
                "property": f"tier_swap.{kw}",
                "old_value": "tier_2",
                "new_value": "tier_1",
                "rationale": "promote keyword from tier-2 to tier-1",
            })
        elif direction == "demote_t1_to_t2" and lens_after.get("tier_1_keywords"):
            kw = rng.choice(lens_after["tier_1_keywords"])
            lens_after["tier_1_keywords"] = [k for k in lens_after["tier_1_keywords"] if k != kw]
            lens_after.setdefault("tier_2_keywords", []).append(kw)
            changes.append({
                "property": f"tier_swap.{kw}",
                "old_value": "tier_1",
                "new_value": "tier_2",
                "rationale": "demote keyword from tier-1 to tier-2",
            })
        else:
            return _programmatic_mutation(lens, rng)

    return lens_after, changes


def _llm_mutation(lens: Dict[str, Any], program_md: str, recent_history: List[Dict[str, Any]],
                  timeout: int = 120) -> Tuple[Dict[str, Any], List[Dict[str, Any]], int]:
    """LLM-propose via cc_helper. Returns (lens_after, changes, prompt_chars)."""
    # Local import keeps this module testable without the helper present.
    import sys
    from pathlib import Path as _Path
    sys.path.insert(0, str(_Path("/home/ruslan/jetix-os")))
    from tools.lib.cc_helper import claude_call  # type: ignore

    history_brief = "\n".join(
        f"- {h.get('variant_name')} verdict={h.get('verdict')} delta={h.get('delta'):+.4f}"
        for h in recent_history[-10:]
    )
    system = (
        "You are a mutation operator for a lens-config search space. "
        "Propose ONE small targeted mutation to the lens config. "
        "Return STRICT JSON only: {\"changes\": [{\"property\":..., \"old_value\":..., \"new_value\":..., \"rationale\":...}], "
        "\"lens_after\": <FULL mutated lens config dict>}. "
        "Do NOT change tier_1_keywords / tier_2_keywords / tier_3_keywords structure (only swap one keyword's tier if useful). "
        "Preserve scoring_weights renormalization (sum=1.0). "
        "Honour the simplicity prior: prefer mechanically distinct over micro-tweak loops. "
        "Avoid re-proposing recent failed variants."
    )
    user = (
        f"PROGRAM (research agenda):\n{program_md}\n\n"
        f"CURRENT LENS:\n{json.dumps(lens, ensure_ascii=False, indent=2)}\n\n"
        f"RECENT HISTORY (last 10):\n{history_brief or '(none)'}\n\n"
        "Propose one mutation."
    )
    raw = claude_call(system=system, user=user, expect_json=True, timeout=timeout)
    payload = json.loads(raw)
    lens_after = payload.get("lens_after") or lens
    changes = payload.get("changes") or []
    return lens_after, changes, len(user) + len(system)


def _diversity_jolt(lens: Dict[str, Any], rng: random.Random) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """Larger combined mutation for escape from local optimum.

    Fires after a consecutive-failure burst. Applies 3 mutations at once:
    full weight reshuffle + threshold reset + tier composition swap. Tracks
    each as a distinct change for DRR transparency.
    """
    lens_after = copy.deepcopy(lens)
    changes: List[Dict[str, Any]] = []

    # 1. Full weight reshuffle (sample fresh distribution, then renormalize).
    new_weights = {k: round(rng.uniform(0.10, 0.50), 4) for k in WEIGHT_KEYS}
    normalized = _normalize_weights(new_weights)
    old_weights = lens_after.get("scoring_weights", {})
    lens_after["scoring_weights"] = normalized
    changes.append({
        "property": "scoring_weights.full_reshuffle",
        "old_value": old_weights,
        "new_value": normalized,
        "rationale": "diversity_jolt: full weight reshuffle to escape local optimum",
    })

    # 2. Threshold reset to a fresh value.
    old_threshold = float(lens_after.get("threshold", 0.60))
    new_threshold = round(rng.uniform(0.30, 0.75), 4)
    lens_after["threshold"] = new_threshold
    changes.append({
        "property": "threshold.diversity_jolt",
        "old_value": old_threshold,
        "new_value": new_threshold,
        "rationale": "diversity_jolt: threshold reset to fresh sample",
    })

    # 3. Tier composition swap (move 2 keywords across tiers).
    for _ in range(2):
        more, swap_changes = _programmatic_mutation(lens_after, rng)
        # Take only the tier_swap result if present, else any.
        lens_after = more
        changes.extend(swap_changes)

    return lens_after, changes


def propose(
    lens: Dict[str, Any],
    hypothesis_config: Dict[str, Any],
    *,
    variant_name: str,
    rng: random.Random,
    strategy: str = "programmatic",
    program_md: str = "",
    recent_history: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Propose one mutation. Returns canonical mutation dict.

    strategy values:
      - "programmatic"     — single small operator (default)
      - "llm"              — Claude proposal via cc_helper
      - "diversity_jolt"   — large combined mutation (escape local optimum)
    """
    recent_history = recent_history or []
    if strategy == "diversity_jolt":
        lens_after, changes = _diversity_jolt(lens, rng)
        actual_strategy = "diversity_jolt"
    elif strategy == "llm":
        try:
            lens_after, changes, _ = _llm_mutation(lens, program_md, recent_history)
            actual_strategy = "llm"
        except Exception as e:
            lens_after, changes = _programmatic_mutation(lens, rng)
            actual_strategy = f"programmatic-fallback({type(e).__name__})"
    else:
        lens_after, changes = _programmatic_mutation(lens, rng)
        actual_strategy = "programmatic"

    # touched_files = the hypothesis-config's mutable_substrate.files (we don't
    # actually write to those files during eval; the lens-after is held in
    # memory and passed to the evaluator). Recording it satisfies the
    # constitutional gate's path-scope check.
    touched_files = list(hypothesis_config.get("mutable_substrate", {}).get("files", []))

    return {
        "variant_name": variant_name,
        "strategy": actual_strategy,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "changes": changes,
        "touched_files": touched_files,
        "blast_radius": hypothesis_config.get("gate", {}).get("blast_radius", "Tier-3"),
        "lens_after": lens_after,
    }
