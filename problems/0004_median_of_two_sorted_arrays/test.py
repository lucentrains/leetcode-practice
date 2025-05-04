

import unittest
from solution import Solution


class TestMedianOfTwoSortedArrays(unittest.TestCase):
    """Unit tests for Solution.findMedianSortedArrays."""

    def setUp(self):
        self.sol = Solution()

    # === Problem statement examples =========================================
    def test_example_1(self):
        self.assertEqual(self.sol.findMedianSortedArrays([1, 3], [2]), 2.0)

    def test_example_2(self):
        self.assertEqual(self.sol.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    # === Edge cases =========================================================
    def test_first_array_empty(self):
        self.assertEqual(self.sol.findMedianSortedArrays([], [1]), 1.0)

    def test_second_array_empty(self):
        self.assertEqual(self.sol.findMedianSortedArrays([2], []), 2.0)

    def test_all_zeros_even_total(self):
        self.assertEqual(self.sol.findMedianSortedArrays([0, 0], [0, 0]), 0.0)

    # === Negative and positive mix ==========================================
    def test_negative_positive_mix(self):
        result = self.sol.findMedianSortedArrays([-5, 3, 6], [-2, -1, 4])
        self.assertAlmostEqual(result, 1.0)

    # === Large size difference ==============================================
    def test_large_size_difference(self):
        nums1 = list(range(1000))  # 0..999
        nums2 = [1000]
        # Combined length = 1001 => median is element #500 -> 500
        self.assertEqual(self.sol.findMedianSortedArrays(nums1, nums2), 500.0)


if __name__ == "__main__":
    unittest.main()