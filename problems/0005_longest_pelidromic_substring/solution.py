# Expand Around Center approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(left: int, right: int) -> str:
            p_l = left
            p_r = right
            while p_l < p_r:
                