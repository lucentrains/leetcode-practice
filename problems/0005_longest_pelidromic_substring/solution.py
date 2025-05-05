# Expand Around Center approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length
            tmp = expandAroundCenter(i, i)
            if len(tmp) > len(longest):
                longest = tmp
            # Even length
            tmp = expandAroundCenter(i, i + 1)
            if len(tmp) > len(longest):
                longest = tmp
        return longest


# Dynamic Programming approach
class SolutionDP:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        start = 0
        max_len = 1
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if length > max_len:
                            max_len = length
                            start = i
        return s[start:start + max_len]


# Manacher's Algorithm (Advanced)
class SolutionManacher:
    def longestPalindrome(self, s: str) -> str:
        T = '#'.join(f'^{s}$')
        n = len(T)
        P = [0] * n
        center = right = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right:
                P[i] = min(right - i, P[mirror])

            while T[i + (1 + P[i])] == T[i - (1 + P[i])]:
                P[i] += 1

            if i + P[i] > right:
                center = i
                right = i + P[i]

        max_len = max(P)
        center_index = P.index(max_len)
        start = (center_index - max_len) // 2
        return s[start:start + max_len]
