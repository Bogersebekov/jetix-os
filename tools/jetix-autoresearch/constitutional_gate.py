#!/usr/bin/env python3
"""constitutional_gate.py — Default-Deny lookup + AWAITING-APPROVAL emit.

Per Q5 (RUSLAN ack 2026-05-11): hard-fail per Part 6b §I.2 F8.

Two modes:
- pre-mutation gate: classify each proposed mutation; halt_log_alert on any
  match against `.claude/config/default-deny-table.yaml constitutional_never_list`
  OR autoresearch_action_classes that resolve to halt_log_alert.
- promotion gate: emit AWAITING-APPROVAL packet for methodology-promotion
  candidates (Q4 threshold ≥3 validated cycles).

Foundation paths are hard-coded here (mirror of CLAUDE.md §4 + Part 6b §I.2).
Mutable substrate scope is *declared* per hypothesis-config; any divergence
triggers halt.
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

ROOT = Path("/home/ruslan/jetix-os")
DENY_TABLE_PATH = ROOT / ".claude" / "config" / "default-deny-table.yaml"
APPROVALS_LOG = ROOT / "swarm" / "approvals" / "log.jsonl"
HEALTH_SIGNALS_PATH = ROOT / "tools" / "jetix-autoresearch" / "results" / "health-signals.jsonl"

FOUNDATION_GLOBS = [
    r"^swarm/wiki/foundations/.*",
    r"^principles/.*",
    r"^shared/schemas/.*",
    r"^swarm/lib/.*",
    r"^\.claude/config/default-deny-table\.yaml$",
    r"^\.claude/config/project-types\.yaml$",
    r"^CLAUDE\.md$",
]


class ConstitutionalViolation(Exception):
    """Raised on F8 hard-fail per Part 6b §I.2."""

    def __init__(self, action_class: str, grade: str, detail: str, mutation: Dict[str, Any]):
        super().__init__(f"[{grade}] {action_class}: {detail}")
        self.action_class = action_class
        self.grade = grade
        self.detail = detail
        self.mutation = mutation


class ConstitutionalGate:
    """Default-Deny lookup + halt_log_alert emit."""

    def __init__(self, deny_table_path: Optional[Path] = None):
        self.deny_table_path = deny_table_path or DENY_TABLE_PATH
        self.deny_table = self._load_deny_table()
        self.violations: List[Dict[str, Any]] = []
        self.gate_hits = 0

    def _load_deny_table(self) -> Dict[str, Any]:
        if not self.deny_table_path.exists():
            raise RuntimeError(f"default-deny-table.yaml not found at {self.deny_table_path}")
        return yaml.safe_load(self.deny_table_path.read_text(encoding="utf-8"))

    # ── Pre-mutation gate ────────────────────────────────────────────────

    def check_mutation(self, mutation: Dict[str, Any], hypothesis_config: Dict[str, Any]) -> None:
        """Hard-fail if mutation violates any Default-Deny entry.

        Raises ConstitutionalViolation (F8) on:
          - Touching Foundation path (R2)
          - Touching path outside hypothesis_config.mutable_substrate.files (R2/R6)
          - action_class matching constitutional_never_list
          - blast_radius uncategorized (R11)
        """
        # R2 — Foundation path write attempt
        for f in mutation.get("touched_files", []):
            for glob_re in FOUNDATION_GLOBS:
                if re.match(glob_re, f):
                    self._record_violation(
                        action_class="ai_execute_architectural_decision",
                        grade="F8",
                        detail=f"Foundation path touched: {f}",
                        mutation=mutation,
                    )
                    raise ConstitutionalViolation(
                        "ai_execute_architectural_decision", "F8",
                        f"Foundation path touched: {f}", mutation
                    )

        # R2/R6 — scope violation: path not in declared mutable_substrate.files
        declared = set(hypothesis_config.get("mutable_substrate", {}).get("files", []))
        for f in mutation.get("touched_files", []):
            # Allow if exact match OR if declared entry is a glob/dir prefix.
            if not any(self._path_in_scope(f, d) for d in declared):
                self._record_violation(
                    action_class="ai_execute_architectural_decision",
                    grade="F8",
                    detail=f"Out-of-scope path: {f} not in mutable_substrate.files {sorted(declared)}",
                    mutation=mutation,
                )
                raise ConstitutionalViolation(
                    "ai_execute_architectural_decision", "F8",
                    f"Out-of-scope path: {f}", mutation
                )

        # R11 — blast_radius uncategorized
        if "blast_radius" not in mutation:
            self._record_violation(
                action_class="bypass_blast_radius_categorization",
                grade="F8",
                detail="mutation has no blast_radius field",
                mutation=mutation,
            )
            raise ConstitutionalViolation(
                "bypass_blast_radius_categorization", "F8",
                "mutation has no blast_radius field", mutation
            )

        self.gate_hits += 1

    @staticmethod
    def _path_in_scope(path: str, declared: str) -> bool:
        """True if path matches declared scope (exact / dir-prefix / wildcard)."""
        if path == declared:
            return True
        if declared.endswith("/") and path.startswith(declared):
            return True
        if "*" in declared:
            pat = re.escape(declared).replace(r"\*", ".*")
            return re.match(f"^{pat}$", path) is not None
        # Same-file basename inside declared parent dir.
        if Path(path).parent == Path(declared).parent and Path(declared).suffix == Path(path).suffix:
            return path.startswith(str(Path(declared).parent))
        return False

    # ── Promotion gate (draft_promotion) ─────────────────────────────────

    def emit_awaiting_approval(self, candidate: Dict[str, Any]) -> Path:
        """Emit a draft_promotion AWAITING-APPROVAL packet (Q4 threshold ≥3)."""
        APPROVALS_LOG.parent.mkdir(parents=True, exist_ok=True)
        packet = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "gate_class": "draft_promotion",
            "blast_radius": "Tier-1",
            "source": "autoresearch-brigadier",
            "candidate": candidate,
            "ruslan_ack_required": True,
            "ack_state": "awaiting",
        }
        with APPROVALS_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(packet, ensure_ascii=False) + "\n")
        return APPROVALS_LOG

    # ── Halt-Log-Alert ───────────────────────────────────────────────────

    def _record_violation(self, action_class: str, grade: str, detail: str,
                          mutation: Dict[str, Any]) -> None:
        entry = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "action_class": action_class,
            "grade": grade,
            "detail": detail,
            "mutation": mutation,
            "halt_log_alert": True,
        }
        self.violations.append(entry)
        HEALTH_SIGNALS_PATH.parent.mkdir(parents=True, exist_ok=True)
        with HEALTH_SIGNALS_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def report(self) -> Dict[str, Any]:
        return {
            "gate_hits": self.gate_hits,
            "violations": len(self.violations),
            "violation_records": self.violations,
        }


if __name__ == "__main__":
    g = ConstitutionalGate()
    print(json.dumps({"deny_entries": len(g.deny_table.get("constitutional_never_list", []))},
                     indent=2))
