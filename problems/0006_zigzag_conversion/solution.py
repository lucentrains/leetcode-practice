"""
LeetCode 6. Zigzag Conversion
Approach: Arithmetic scan (cycle math).

Time complexity: O(n)
Space complexity: O(1)  (excluding output string)
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert string to its zigzag form and read row‑by‑row.

        :param s: Input string (1 ≤ len(s) ≤ 1000)
        :param numRows: Number of rows in zigzag pattern (1 ≤ numRows ≤ 1000)
        :return: Zigzag‑read string
        """
        # Trivial cases: no zig‑zagging needed
        if numRows == 1 or numRows >= len(s):
            return s

        cycle = 2 * numRows - 2  # Length of one full zig‑zag cycle
        n = len(s)
        result = []

        for row in range(numRows):
            idx = row
            while idx < n:
                # Character in the current column
                result.append(s[idx])

                # Character on the diagonal (only for middle rows)
                if 0 < row < numRows - 1:
                    diag = idx + cycle - 2 * row
                    if diag < n:
                        result.append(s[diag])

                # Jump to the next character in the same row (next cycle)
                idx += cycle

        return "".join(result)


if __name__ == "__main__":
    # Basic sanity checks
    sol = Solution()
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert sol.convert("A", 1) == "A"
    print("All sample tests passed.")
