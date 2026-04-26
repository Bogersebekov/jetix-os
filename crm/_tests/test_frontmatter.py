"""Frontmatter parser + validator tests."""
import datetime as _dt
import sys
import unittest
from pathlib import Path

# Ensure repo root is importable so `from crm._scripts...` resolves.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from crm._scripts import frontmatter as fm  # noqa: E402

FIX = Path(__file__).resolve().parent / "fixtures"


class ParseTests(unittest.TestCase):
    def test_parse_anton_fixture(self):
        data, body = fm.parse_file(FIX / "sample-person-anton.md")
        self.assertEqual(data["slug"], "sample-person-anton")
        self.assertIn("advisor", data["roles"])
        self.assertIn("# Антон Тестов", body)

    def test_dump_roundtrip(self):
        data, body = fm.parse_file(FIX / "sample-person-vladislav.md")
        rendered = fm.dump(data, body)
        data2, body2 = fm.parse_text(rendered)
        self.assertEqual(data2["slug"], data["slug"])
        self.assertEqual(set(data2["roles"]), set(data["roles"]))


class ValidateTests(unittest.TestCase):
    def _base(self):
        return {
            "name": "Test",
            "slug": "test-x",
            "type": "person",
            "roles": ["advisor"],
            "created": "2026-04-26",
            "updated": "2026-04-26",
        }

    def test_valid_minimal(self):
        self.assertEqual(fm.validate(self._base()), [])

    def test_missing_required(self):
        d = self._base()
        del d["roles"]
        errs = fm.validate(d)
        self.assertTrue(any("roles" in e for e in errs))

    def test_invalid_role_enum(self):
        d = self._base()
        d["roles"] = ["xyz"]
        errs = fm.validate(d)
        self.assertTrue(any("xyz" in e for e in errs), msg=f"errors: {errs}")

    def test_bad_slug(self):
        d = self._base()
        d["slug"] = "Bad Slug With Spaces"
        errs = fm.validate(d)
        self.assertTrue(any("slug" in e for e in errs))

    def test_bad_date(self):
        d = self._base()
        d["created"] = "26-04-2026"
        errs = fm.validate(d)
        self.assertTrue(any("created" in e for e in errs))

    def test_telegram_format(self):
        d = self._base()
        d["contact"] = {"telegram": "no_at_sign"}
        errs = fm.validate(d)
        self.assertTrue(any("telegram" in e for e in errs))

    def test_icp_range(self):
        d = self._base()
        d["icp"] = {"azart": 6}
        errs = fm.validate(d)
        self.assertTrue(any("azart" in e for e in errs))

    def test_pipeline_status_enum(self):
        d = self._base()
        d["pipeline"] = {"status": "totally_made_up"}
        errs = fm.validate(d)
        self.assertTrue(any("pipeline.status" in e for e in errs))


class AutofixTests(unittest.TestCase):
    def test_icp_total_autofix(self):
        d = {
            "name": "x", "slug": "x", "type": "person", "roles": ["advisor"],
            "created": "2026-04-26", "updated": "2026-04-26",
            "icp": {"azart": 4, "stable": 5, "adequate": 5, "upward": 4, "total": 99},
        }
        fixed, warnings = fm.autofix(d)
        self.assertEqual(fixed["icp"]["total"], 18)
        self.assertTrue(any("autofixed" in w for w in warnings))

    def test_icp_total_correct_no_warn(self):
        d = {
            "name": "x", "slug": "x", "type": "person", "roles": ["advisor"],
            "created": "2026-04-26", "updated": "2026-04-26",
            "icp": {"azart": 4, "stable": 5, "adequate": 5, "upward": 4, "total": 18},
        }
        _, warnings = fm.autofix(d)
        self.assertEqual(warnings, [])


if __name__ == "__main__":
    unittest.main()
