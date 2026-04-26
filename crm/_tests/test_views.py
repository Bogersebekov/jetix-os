"""Views (filter + sort + search) tests using fixtures placed into a tmp CRM tree."""
import shutil
import sys
import tempfile
import unittest
from importlib import reload
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

FIX = Path(__file__).resolve().parent / "fixtures"


class _TmpCRM:
    """Patch crm._scripts.views.* paths to a tmp tree populated from fixtures."""
    def __init__(self):
        self.tmp = tempfile.mkdtemp(prefix="crm-test-")
        self.tmp_root = Path(self.tmp)
        (self.tmp_root / "people").mkdir()
        (self.tmp_root / "orgs").mkdir()
        # Copy fixtures
        shutil.copy(FIX / "sample-person-anton.md", self.tmp_root / "people" / "sample-person-anton.md")
        shutil.copy(FIX / "sample-person-vladislav.md", self.tmp_root / "people" / "sample-person-vladislav.md")
        shutil.copy(FIX / "sample-org-acme.md", self.tmp_root / "orgs" / "sample-org-acme.md")
        # Need _schema dir for frontmatter validation lookups (read from real repo)
        # views.py only reads PEOPLE_DIR/ORGS_DIR; frontmatter.py reads SCHEMA_DIR which
        # is module-level. We patch both.

    def patch(self, views_mod, fm_mod, ib_mod=None):
        views_mod.PEOPLE_DIR = self.tmp_root / "people"
        views_mod.ORGS_DIR = self.tmp_root / "orgs"
        if ib_mod is not None:
            ib_mod.CRM_ROOT = self.tmp_root
            ib_mod.INDEX_PATH = self.tmp_root / "index.md"

    def cleanup(self):
        shutil.rmtree(self.tmp, ignore_errors=True)


class FilterTests(unittest.TestCase):
    def setUp(self):
        from crm._scripts import views, frontmatter
        self.tmp = _TmpCRM()
        self.tmp.patch(views, frontmatter)
        self.views = views

    def tearDown(self):
        self.tmp.cleanup()

    def test_filter_by_role(self):
        recs = self.views.filter_records(["roles=advisor"])
        slugs = [r[1]["slug"] for r in recs]
        self.assertIn("sample-person-anton", slugs)
        self.assertNotIn("sample-person-vladislav", slugs)

    def test_filter_by_country(self):
        recs = self.views.filter_records(["location_country=DE"])
        slugs = [r[1]["slug"] for r in recs]
        self.assertIn("sample-person-anton", slugs)
        self.assertNotIn("sample-person-vladislav", slugs)

    def test_filter_combined(self):
        recs = self.views.filter_records([
            "roles=advisor", "location_country=DE", "icp.startupper=yes",
        ])
        self.assertEqual(len(recs), 1)
        self.assertEqual(recs[0][1]["slug"], "sample-person-anton")

    def test_filter_numeric_gte(self):
        recs = self.views.filter_records(["icp.total>=15"])
        slugs = [r[1]["slug"] for r in recs]
        self.assertIn("sample-person-anton", slugs)

    def test_filter_numeric_lt(self):
        recs = self.views.filter_records(["audience.total_followers<2000"])
        slugs = [r[1]["slug"] for r in recs]
        self.assertIn("sample-person-vladislav", slugs)
        self.assertIn("sample-org-acme", slugs)

    def test_filter_or_in_value(self):
        recs = self.views.filter_records(["pipeline.status=warm,discovery_call"])
        slugs = [r[1]["slug"] for r in recs]
        self.assertIn("sample-person-anton", slugs)
        self.assertIn("sample-person-vladislav", slugs)
        self.assertIn("sample-org-acme", slugs)

    def test_filter_invalid_syntax(self):
        with self.assertRaises(ValueError):
            self.views.filter_records(["bogus syntax"])

    def test_no_orgs_flag(self):
        recs = self.views.filter_records([], include_orgs=False)
        slugs = [r[1]["slug"] for r in recs]
        self.assertNotIn("sample-org-acme", slugs)

    def test_sort_by_icp(self):
        recs = self.views.filter_records([])
        sorted_recs = self.views.sort_records(recs, sort_by="icp", reverse=True)
        first = sorted_recs[0][1]["slug"]
        self.assertEqual(first, "sample-person-anton")


class SearchTests(unittest.TestCase):
    def setUp(self):
        from crm._scripts import views, frontmatter
        self.tmp = _TmpCRM()
        self.tmp.patch(views, frontmatter)
        self.views = views

    def tearDown(self):
        self.tmp.cleanup()

    def test_search_dach(self):
        hits = self.views.search_records("dach")
        slugs = [h[1]["slug"] for h in hits]
        self.assertIn("sample-person-anton", slugs)

    def test_search_empty_returns_empty(self):
        self.assertEqual(self.views.search_records("   "), [])

    def test_search_ranks_by_hits(self):
        hits = self.views.search_records("ai")
        # at least anton should hit; sorted by count desc
        if len(hits) >= 2:
            self.assertGreaterEqual(hits[0][2], hits[-1][2])


if __name__ == "__main__":
    unittest.main()
