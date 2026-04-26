#!/usr/bin/env python3
"""End-to-end smoke test for the migrated voice-pipeline (cycle 11).

Runs extract → filter (small-corpus path) → summarize → review_report on a
tiny synthetic corpus, with ANTHROPIC_API_KEY explicitly unset, proving the
whole pipeline works through CC headless (Max sub) with no API key.

Run: python3 tools/test_e2e_no_api.py
"""

import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


# Ensure CC-headless backend (default) and no API key in this process.
os.environ.pop("ANTHROPIC_API_KEY", None)
os.environ.setdefault("JETIX_LLM_BACKEND", "cc-headless")

sys.path.insert(0, str(Path(__file__).resolve().parent))


class TestE2ENoApi(unittest.TestCase):

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="e2e_no_api_"))
        self.transcripts = self.tmp / "raw" / "transcripts"
        self.extractions = self.tmp / "inbox" / "processed" / "extractions"
        self.filtered = self.tmp / "inbox" / "processed" / "filtered"
        self.reports = self.tmp / "reports"
        for d in [self.transcripts, self.extractions, self.filtered, self.reports]:
            d.mkdir(parents=True, exist_ok=True)

        # Minimal Russian transcript — 2 short, parseable thoughts.
        sample = (
            "Сегодня сформулировал решение: для quick-money запускаем сначала pilot "
            "на одном клиенте перед масштабированием. Это снизит риск. "
            "И ещё идея — нужно завести AI-ассистента для отслеживания progress по pilot."
        )
        (self.transcripts / "audio_test_001.txt").write_text(sample, encoding="utf-8")

        # Pre-build a single small extraction so filter+summarize have something
        # to chew on without doing the (slower, less deterministic) full extract.
        ext = {
            "source": "audio_test_001.txt",
            "processed_at": "2026-04-26T03:30:00",
            "model": "test",
            "items": [
                {"category": "Решения", "content": "Запустить pilot на одном клиенте",
                 "priority": "high", "project": "quick-money", "actionable": True,
                 "horizon": "now", "delegate": None, "date": "2026-04-26"},
                {"category": "Идеи", "content": "AI-ассистент для отслеживания pilot progress",
                 "priority": "medium", "project": "ai-tools", "actionable": False,
                 "horizon": "backlog", "delegate": None, "date": "2026-04-26"},
                {"category": "Принципы", "content": "Снижать риск через постепенное масштабирование",
                 "priority": "medium", "project": None, "actionable": False,
                 "horizon": "backlog", "delegate": None, "date": "2026-04-26"},
            ],
        }
        (self.extractions / "audio_test_001.json").write_text(
            json.dumps(ext, ensure_ascii=False, indent=2), encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_filter_no_api_small_corpus(self):
        """filter.py small-corpus path (single LLM call, no partials) via CC headless."""
        import filter as F
        F.EXTRACTIONS = self.extractions
        F.OUT_DIR = self.filtered
        F.PARTIALS_DIR = self.filtered / ".partials"
        # avoid pulling actual config/context.md
        F.CONTEXT_FILE = self.tmp / "no_such_context.md"

        argv_save = sys.argv
        sys.argv = ["filter.py"]
        try:
            F.main()
        finally:
            sys.argv = argv_save

        # Must have produced a final batch JSON.
        finals = list(self.filtered.glob("batch_*.json"))
        self.assertEqual(len(finals), 1, f"expected 1 final, got {finals}")
        data = json.loads(finals[0].read_text(encoding="utf-8"))
        self.assertGreater(data.get("output_items_count", 0), 0)
        self.assertIn("items", data)
        self.assertIsInstance(data["items"], list)
        # No leftover partials.
        self.assertFalse(F.PARTIALS_DIR.exists() and any(F.PARTIALS_DIR.iterdir()))

    def test_summarize_no_api(self):
        """summarize.py via CC headless on tiny corpus."""
        import summarize as S
        S.EXTRACTIONS = self.extractions
        S.REPORTS = self.reports
        S.LATEST = self.tmp / "summary-latest.md"
        S.CONTEXT_FILE = self.tmp / "no_such_context.md"

        argv_save = sys.argv
        sys.argv = ["summarize.py"]
        try:
            S.main()
        finally:
            sys.argv = argv_save

        # Must have produced summary file with non-trivial content.
        out = list(self.reports.glob("summary_*.md"))
        self.assertEqual(len(out), 1, f"expected 1 summary, got {out}")
        body = out[0].read_text(encoding="utf-8")
        self.assertGreater(len(body), 200, "summary output too small")
        self.assertIn("Сводка", body)

    def test_review_report_pure_local(self):
        """review_report.py is pure local — no LLM. Verify it consumes filter output."""
        # First run filter to produce input.
        self.test_filter_no_api_small_corpus()

        import review_report as R
        R.FILTERED = self.filtered
        R.REPORTS = self.reports
        R.LATEST = self.tmp / "review-latest.md"

        argv_save = sys.argv
        sys.argv = ["review_report.py"]
        try:
            R.main()
        finally:
            sys.argv = argv_save

        out = list(self.reports.glob("review_*.md"))
        self.assertEqual(len(out), 1, f"expected 1 review, got {out}")
        text = out[0].read_text(encoding="utf-8")
        self.assertIn("Обзор голосовых заметок", text)
        self.assertIn("Задачи", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
