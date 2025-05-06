import unittest
from solution import Solution


class TestZigzagConversion(unittest.TestCase):
    """Unit tests for LeetCode 6 ‒ Zigzag Conversion."""

    def setUp(self):
        self.sol = Solution()

    # --- Official examples -------------------------------------------------
    def test_examples(self):
        self.assertEqual(
            self.sol.convert("PAYPALISHIRING", 3),
            "PAHNAPLSIIGYIR",
            "Example 1 failed",
        )
        self.assertEqual(
            self.sol.convert("PAYPALISHIRING", 4),
            "PINALSIGYAHRPI",
            "Example 2 failed",
        )
        self.assertEqual(
            self.sol.convert("A", 1),
            "A",
            "Example 3 failed",
        )

    # --- Additional edge/corner cases --------------------------------------
    def test_edge_cases(self):
        # numRows == 1 → unchanged
        self.assertEqual(self.sol.convert("AB", 1), "AB")

        # numRows greater than string length → unchanged
        self.assertEqual(self.sol.convert("ABC", 5), "ABC")

        # Small strings with typical numRows
        self.assertEqual(self.sol.convert("ABCDE", 2), "ACEBD")   # cycle = 2
        self.assertEqual(self.sol.convert("ABCDE", 3), "AEBDC")   # cycle = 4

    # --- Randomized smoke test for larger input ----------------------------
    def test_long_string(self):
        txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        out = self.sol.convert(txt, 5)
        # Ensure output length equals input length and is permutation of characters
        self.assertEqual(len(out), len(txt))
        self.assertCountEqual(out, txt)


if __name__ == "__main__":
    unittest.main()
