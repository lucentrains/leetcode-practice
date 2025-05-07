

import unittest

# Import the Solution class from solution.py in the same directory
from solution import Solution


class TestReverseInteger(unittest.TestCase):
    """Unit tests for the reverse() method in Solution."""

    def setUp(self):
        self.sol = Solution()

    def test_positive(self):
        """123 should become 321."""
        self.assertEqual(self.sol.reverse(123), 321)

    def test_negative(self):
        """-123 should become -321."""
        self.assertEqual(self.sol.reverse(-123), -321)

    def test_trailing_zero(self):
        """120 should lose the trailing zero and become 21."""
        self.assertEqual(self.sol.reverse(120), 21)

    def test_overflow_positive(self):
        """Largest 32‑bit positive int should overflow and return 0."""
        self.assertEqual(self.sol.reverse(2**31 - 1), 0)

    def test_overflow_negative(self):
        """Smallest 32‑bit negative int should overflow and return 0."""
        self.assertEqual(self.sol.reverse(-2**31), 0)

    def test_single_digit(self):
        """Single‑digit numbers should remain unchanged."""
        self.assertEqual(self.sol.reverse(7), 7)
        self.assertEqual(self.sol.reverse(-5), -5)


if __name__ == "__main__":
    unittest.main()