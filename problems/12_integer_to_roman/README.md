
⸻

Integer to Roman
	•	Difficulty: Medium
	•	Link: https://leetcode.com/problems/integer-to-roman/

Disclaimer
Problem description © LeetCode LLC.
This README is only a concise summary and solution-note; please refer to the official link for the full statement.

⸻

Problem Statement (condensed)

Given an integer, convert it to a Roman numeral.

The Roman numerals are represented by seven different symbols:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

To convert a decimal to a Roman numeral, follow these rules:
	•	If the number starts with 4 or 9, use the subtractive notation, e.g., 4 is represented as IV and 9 as IX.
	•	Otherwise, subtract the highest possible Roman numeral and append that symbol, continuing until the number is reduced to zero.

Example 1:

Input: num = 3749
Output: "MMMDCCXLIX"

Explanation:
	•	3000 = MMM (1000 * 3)
	•	700 = DCC (500 + 100 + 100)
	•	40 = XL (10 less than 50)
	•	9 = IX (1 less than 10)

Example 2:

Input: num = 58
Output: "LVIII"

Explanation:
	•	50 = L
	•	8 = VIII (5 + 3)

Example 3:

Input: num = 1994
Output: "MCMXCIV"

Explanation:
	•	1000 = M
	•	900 = CM
	•	90 = XC
	•	4 = IV

Constraints
	•	1 <= num <= 3999

⸻

Intuition

The Roman numeral system uses a combination of symbols to represent numbers. By subtracting from the highest possible symbol that can fit into the remaining value, we can build the Roman numeral. When the number starts with a 4 or 9, we apply the subtractive notation.

⸻

Approaches

#	Idea	Sketch	Time	Extra Space
1	Greedy Approach	Start from the largest Roman numeral, subtract its value from num, and append it to the result. Repeat until num is 0.	O(n)	O(n)


⸻

Reference Implementations

Language	File	Approach
Python	solution.py	Greedy Approach

All solutions run in O(n) time where n is the length of the Roman numeral string constructed.

⸻

日本語サマリ

問題概要

整数 num をローマ数字に変換してください。

ローマ数字には以下の 7 種類の記号があります：

記号	値
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

変換のルール：
	•	4 や 9 で始まる場合は引き算の形式（例: 4 は IV、9 は IX）を使用します。
	•	それ以外の場合、最大の記号から順に引き、残りの値を変換していきます。

例
	1.	num = 3749 → "MMMDCCXLIX"
	2.	num = 58 → "LVIII"
	3.	num = 1994 → "MCMXCIV"

制約
	•	1 <= num <= 3999

解法

貪欲法を用いて、ローマ数字を最も大きい記号から順に引いていきます。

⸻

参照実装

言語	ファイル	採用手法
Python	solution.py	貪欲法（Greedy）