class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "IV": 4, 
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        total = 0
        i = 0
        while i < len(s):
            # This is the subtractive case.
            if i < len(s) - 1 and s[i : i + 2] in values:
                total += values[s[i : i + 2]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total