import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from catalog_drift import compare, load_catalog


class CatalogDriftTests(unittest.TestCase):
    def test_disjoint_and_shared_resources_are_explicit(self):
        upstream = {
            "shared": {"id": "shared", "canonical_url": "https://example.org", "status": "verified"},
            "new": {"id": "new", "canonical_url": "https://example.com", "status": "needs-review"},
        }
        local = {
            "shared": {"id": "shared", "canonical_url": "https://example.org", "status": "needs-review"},
            "legacy": {"id": "legacy", "canonical_url": "https://legacy.example", "status": "needs-review"},
        }
        result = compare(upstream, local)
        self.assertEqual(result["shared_ids"], 1)
        self.assertEqual(result["missing_from_local"], ["new"])
        self.assertEqual(result["local_only"], ["legacy"])
        self.assertEqual(result["canonical_url_conflicts"], [])
        self.assertEqual(result["review_metadata_differences"][0]["fields"], ["status"])

    def test_url_conflict_is_distinct_from_metadata_drift(self):
        result = compare(
            {"x": {"id": "x", "canonical_url": "https://primary.example"}},
            {"x": {"id": "x", "canonical_url": "https://other.example"}},
        )
        self.assertEqual(len(result["canonical_url_conflicts"]), 1)

    def test_duplicate_ids_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / "resources.json"
            file.write_text(json.dumps({"resources": [
                {"id": "duplicate"}, {"id": "duplicate"}
            ]}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate resource id"):
                load_catalog(file)


if __name__ == "__main__":
    unittest.main()
