from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute‑force solution: check every pair.

        Time  Complexity: O(n²)
        Space Complexity: O(1)

        Args:
            nums   (List[int]): list of integers
            target (int)     : target sum

        Returns:
            List[int]: indices of the two numbers such that they add up to target
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # According to the problem constraints this line is never reached
        raise ValueError("No two sum solution found.")
