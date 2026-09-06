import json, unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from q4_intel import score, rank

class TestQ4Intel(unittest.TestCase):
    def setUp(self):
        data = Path(__file__).parents[1] / "data" / "opportunities.json"
        self.items = json.loads(data.read_text())

    def test_score_range(self):
        for item in self.items:
            s = score(item["scores"])
            self.assertGreaterEqual(s, 0)
            self.assertLessEqual(s, 100)

    def test_rank_descending(self):
        rows = rank(self.items)
        scores = [r["runtime_score_100"] for r in rows]
        self.assertEqual(scores, sorted(scores, reverse=True))

    def test_zero_capital_filter(self):
        rows = rank(self.items, zero_capital=True)
        self.assertTrue(rows)
        self.assertTrue(all(r["capital_band"] == "$0-10" for r in rows))

    def test_q4_filter(self):
        rows = rank(self.items, q4=True)
        self.assertTrue(all(r["scores"]["q4_fit"] >= 8 for r in rows))

if __name__ == "__main__":
    unittest.main()
