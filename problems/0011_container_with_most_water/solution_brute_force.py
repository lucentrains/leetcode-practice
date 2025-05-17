from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Brute-force O(n²) 解法。
        """
        n = len(height)
        if n < 2:
            return 0

        max_area = 0
        for i, h_i in enumerate(height[:-1]):
            for j, h_j in enumerate(height[i + 1:], start=i + 1):
                max_area = max(max_area, min(h_i, h_j) * (j - i))
        return max_area