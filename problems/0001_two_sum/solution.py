from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time:  O(n)
        Space: O(n)
        """
        lookup: dict[int, int] = {}  # 値 -> インデックス

        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i