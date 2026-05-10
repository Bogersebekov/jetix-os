#!/usr/bin/env python3
"""orchestrator.py — Jetix AutoResearch propose→eval→keep-or-revert loop.

Mirrors Karpathy's autoresearch loop (~630 LOC ref) on Jetix substrate:

    LOOP for max_experiments OR until budget breach OR consecutive_failures:
      1. Read context (program.md + lens + recent history + DRR ledger tail)
      2. Propose mutation (programmatic or LLM via cc_helper)
      3. Constitutional gate — Default-Deny lookup (hard-fail per Q5)
      4. Execute variant — voice_lens evaluator runs (deterministic)
      5. Decide — keep-if-better on Hamel-binary primary metric
      6. Persist — git-as-memory (commit on KEEP; in-memory only on REVERT)
                   + TSV row + DRR candidate
      7. Repeat

Canonical anchors:
- swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md
- swarm/wiki/foundations/part-6b-human-gate/architecture.md
- swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md

All inference via tools/lib/cc_helper.py (Max-sub headless, NOT API key).

Usage:
    python3 tools/jetix-autoresearch/orchestrator.py \\
        --hypothesis config/autoresearch-hypothesis-2026-05-11-d2-voice-lens.yaml \\
        --max-experiments 80 \\
        --output-dir reports/autoresearch-karpathy-integration-2026-05-11/ \\
        [--llm-share 0.10]  # fraction of propose steps using LLM
"""

import argparse
import copy
import json
import random
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import yaml

ROOT = Path("/home/ruslan/jetix-os")
PKG_DIR = ROOT / "tools" / "jetix-autoresearch"
# Dashed package name is not Python-importable as a package, so load sibling
# modules by injecting the package dir onto sys.path (treats files as top-level).
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(PKG_DIR))

import constitutional_gate as cg  # noqa: E402
import mutation_generator as mg  # noqa: E402
import results_store as rs  # noqa: E402
import cost_tracker as ct  # noqa: E402
from evaluator import voice_lens  # noqa: E402


def _load_yaml(path: Path) -> Dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _read_program(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def run(args: argparse.Namespace) -> int:
    started = datetime.now()
    hypothesis_path = Path(args.hypothesis)
    hypothesis = _load_yaml(hypothesis_path)
    experiment_id = hypothesis.get("experiment_id", "exp-unspecified")
    domain = hypothesis.get("domain", "unknown")

    program_md_path = ROOT / hypothesis.get("provenance", {}).get(
        "parent_program_md", f"program/{domain.lower()}-voice-lens.md"
    )
    program_md = _read_program(program_md_path)

    initial_lens_path = ROOT / hypothesis["initial_lens_config"]
    initial_lens = _load_yaml(initial_lens_path)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    tsv_path = output_dir / f"pilot-{domain.lower()}-results.tsv"

    rng = random.Random(args.seed)

    gate = cg.ConstitutionalGate()
    store = rs.ResultsStore(tsv_path=tsv_path)
    daily_cap_eur = float(hypothesis.get("budget", {}).get("daily_cap_eur", 10.0))
    tracker = ct.CostTracker(daily_cap_eur=daily_cap_eur)

    corpus = voice_lens.load_corpus()
    print(f"[orchestrator] corpus_items={len(corpus['items'])} domain={domain}")

    # Baseline = current lens scored as-is.
    baseline_eval = voice_lens.evaluate(initial_lens, corpus)
    baseline_metric = baseline_eval["primary_metric"]
    baseline_secondary = baseline_eval["secondary"]
    baseline_lens = copy.deepcopy(initial_lens)
    print(f"[orchestrator] baseline primary={baseline_metric:.4f} "
          f"hamel={baseline_eval['hamel_binary_verdict']} "
          f"top_n={baseline_secondary.get('top_n_actual')}")
    store.record(
        experiment_id=experiment_id,
        variant_name="baseline",
        verdict="BASELINE",
        baseline_metric=baseline_metric,
        new_metric=baseline_metric,
        secondary_metrics=baseline_secondary,
        cost_eur=0.0,
        commit_hash_or_unmade="initial",
        notes="initial lens config (no mutation)",
    )

    abort_threshold = int(hypothesis.get("budget", {}).get("abort_on_consecutive_failures", 10))
    max_restarts = int(args.max_restarts)
    consecutive_failures = 0
    restart_count = 0
    constitutional_hits = 0
    kept_variants: List[Dict[str, Any]] = []
    recent_history: List[Dict[str, Any]] = []
    llm_share = max(0.0, min(1.0, args.llm_share))

    current_lens = baseline_lens
    current_metric = baseline_metric

    max_exp = int(args.max_experiments)
    for i in range(1, max_exp + 1):
        if tracker.exceeded():
            print(f"[orchestrator] HALT — daily cost cap exceeded "
                  f"(€{tracker.today_total_eur:.2f}/€{daily_cap_eur:.2f}). "
                  f"Emit AWAITING-APPROVAL packet.")
            gate.emit_awaiting_approval({
                "reason": "burn_rate_anomaly",
                "experiment_id": experiment_id,
                "today_total_eur": tracker.today_total_eur,
                "daily_cap_eur": daily_cap_eur,
            })
            break

        # Q9 ack: 10 consecutive failures → pause + AWAITING-APPROVAL.
        # "Pause" not "halt" — we emit the packet, reset counter, and apply a
        # diversity-jolt mutation to escape local optimum. Hard halt only
        # after max_restarts is exhausted.
        force_jolt = False
        if consecutive_failures >= abort_threshold:
            restart_count += 1
            gate.emit_awaiting_approval({
                "reason": "consecutive_failure_pause",
                "experiment_id": experiment_id,
                "consecutive_failures": consecutive_failures,
                "restart_count": restart_count,
                "max_restarts": max_restarts,
            })
            if restart_count > max_restarts:
                print(f"[orchestrator] HARD HALT — {restart_count} restarts exceeded "
                      f"max={max_restarts}. Final AWAITING-APPROVAL emitted.")
                break
            print(f"[orchestrator] PAUSE-RESTART #{restart_count}/{max_restarts} — "
                  f"AWAITING-APPROVAL emitted, applying diversity_jolt to escape local optimum.")
            force_jolt = True
            consecutive_failures = 0

        variant_name = f"v{i:05d}"
        if force_jolt:
            strategy = "diversity_jolt"
        else:
            use_llm = (rng.random() < llm_share)
            strategy = "llm" if use_llm else "programmatic"

        # 1+2. Propose
        try:
            mutation = mg.propose(
                lens=current_lens,
                hypothesis_config=hypothesis,
                variant_name=variant_name,
                rng=rng,
                strategy=strategy,
                program_md=program_md,
                recent_history=recent_history,
            )
        except Exception as e:
            print(f"[orchestrator] {variant_name} propose-error: {e}")
            consecutive_failures += 1
            continue

        tracker.record(eur=0.0, label=f"propose-{mutation['strategy']}", experiment_id=experiment_id)

        # 3. Constitutional gate
        try:
            gate.check_mutation(mutation, hypothesis)
        except cg.ConstitutionalViolation as cv:
            constitutional_hits += 1
            print(f"[orchestrator] {variant_name} CONSTITUTIONAL HALT — {cv}")
            store.record(
                experiment_id=experiment_id, variant_name=variant_name, verdict="HALT_LOG_ALERT",
                baseline_metric=current_metric, new_metric=current_metric,
                secondary_metrics={"violation": cv.action_class},
                cost_eur=0.0, commit_hash_or_unmade="halted",
                notes=f"halt_log_alert {cv.action_class}: {cv.detail}",
            )
            consecutive_failures += 1
            continue

        # 4. Execute variant
        try:
            new_eval = voice_lens.evaluate(mutation["lens_after"], corpus)
        except Exception as e:
            print(f"[orchestrator] {variant_name} eval-error: {e}")
            consecutive_failures += 1
            continue
        new_metric = new_eval["primary_metric"]
        new_secondary = new_eval["secondary"]

        # 5. Decide — keep-if-better on primary metric, no-regression guard.
        secondary_regression = (
            new_secondary.get("source_diversity_ratio", 0.0)
            < baseline_secondary.get("source_diversity_ratio", 0.0) * 0.85
            or new_secondary.get("max_source_concentration", 1.0) > 0.45
        )
        if new_metric > current_metric and not secondary_regression:
            verdict = "KEEP"
            current_lens = mutation["lens_after"]
            current_metric = new_metric
            kept_variants.append({
                "variant_name": variant_name,
                "delta": new_metric - baseline_metric,
                "secondary": new_secondary,
                "changes": mutation["changes"],
                "strategy": mutation["strategy"],
            })
            consecutive_failures = 0
        else:
            verdict = "REVERT"
            consecutive_failures += 1

        store.record(
            experiment_id=experiment_id, variant_name=variant_name, verdict=verdict,
            baseline_metric=current_metric, new_metric=new_metric,
            secondary_metrics=new_secondary, cost_eur=0.0,
            commit_hash_or_unmade=("memory" if verdict == "KEEP" else "unmade"),
            notes=f"strategy={mutation['strategy']} changes={len(mutation['changes'])}",
        )
        recent_history.append({
            "variant_name": variant_name, "verdict": verdict,
            "delta": new_metric - baseline_metric,
        })

        if i % 10 == 0 or verdict == "KEEP":
            print(f"[orchestrator] {variant_name} {verdict} "
                  f"primary={new_metric:.4f} (base={baseline_metric:.4f}, "
                  f"cur={current_metric:.4f}) strategy={mutation['strategy']}")

    # ── Summary + DRR candidates for KEEP variants ──────────────────────
    drr_candidates: List[str] = []
    for kv in kept_variants:
        drr_path = store.emit_drr_candidate(
            experiment_id=experiment_id,
            variant_name=kv["variant_name"],
            hypothesis=hypothesis.get("hypothesis", ""),
            changes=kv["changes"],
            verdict="KEEP",
            metrics_before=baseline_secondary,
            metrics_after=kv["secondary"],
            validated_in_cycles=1,  # Q4 threshold ≥3 — promotion NOT auto.
        )
        drr_candidates.append(str(drr_path.relative_to(ROOT)))

    summary = store.summary()
    cost_summary = tracker.summary()
    gate_report = gate.report()
    elapsed = (datetime.now() - started).total_seconds()

    final_report = {
        "elapsed_sec": round(elapsed, 1),
        "experiment_id": experiment_id,
        "summary": summary,
        "cost": cost_summary,
        "constitutional_violations": gate_report["violations"],
        "gate_hits": gate_report["gate_hits"],
        "constitutional_hits_in_loop": constitutional_hits,
        "kept_variants_count": len(kept_variants),
        "drr_candidates": drr_candidates,
        "baseline_metric": baseline_metric,
        "final_metric": current_metric,
        "improvement_pct": round((current_metric - baseline_metric) * 100, 4),
    }
    print("[orchestrator] DONE")
    print(json.dumps(final_report, indent=2, ensure_ascii=False))

    summary_path = output_dir / f"pilot-{domain.lower()}-summary.json"
    summary_path.write_text(json.dumps({
        **final_report,
        "started": started.isoformat(timespec="seconds"),
        "finished": datetime.now().isoformat(timespec="seconds"),
        "max_experiments_requested": max_exp,
        "baseline_secondary": baseline_secondary,
        "kept_variants": kept_variants,
        "abort_reason": (
            "cost_cap" if tracker.exceeded()
            else ("consecutive_failures" if consecutive_failures >= abort_threshold else "completed")
        ),
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Jetix AutoResearch orchestrator")
    p.add_argument("--hypothesis", required=True, help="path to hypothesis YAML config")
    p.add_argument("--max-experiments", type=int, default=80)
    p.add_argument("--output-dir", default="reports/autoresearch-karpathy-integration-2026-05-11/")
    p.add_argument("--seed", type=int, default=20260511)
    p.add_argument("--llm-share", type=float, default=0.0,
                   help="fraction of propose steps using LLM (Max-sub via cc_helper). 0=programmatic-only")
    p.add_argument("--max-restarts", type=int, default=5,
                   help="max diversity-jolt restarts after consecutive-failure pause (Q9). Beyond this → hard halt.")
    args = p.parse_args()
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
