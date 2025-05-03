import unittest
from solution import Solution

class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_length_of_longest_substring(self):
        test_cases = [
            ("abcabcbb", 3),   # "abc"
            ("bbbbb", 1),      # "b"
            ("pwwkew", 3),     # "wke"
            ("", 0),                          # empty string
            ("abcdef", 6),                    # all unique
            ("aaaaa", 1),                     # all same
            ("dvdf", 3),                      # overlapping duplicates
            ("anviaj", 5),                    # mixed
            ("abba", 2),                      # duplicate pair in middle
            ("tmmzuxt", 5),                   # common LeetCode test
        ]
        for s, expected in test_cases:
            with self.subTest(s=s):
                result = self.solution.lengthOfLongestSubstring(s)
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()