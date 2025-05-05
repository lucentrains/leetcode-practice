
0005. Longest Palindromic Substring
	•	Difficulty: Medium
	•	Link: https://leetcode.com/problems/longest-palindromic-substring/

Disclaimer
Problem description © LeetCode LLC.
This file contains only a brief summary and original notes; please refer to the official link above for the full text.

⸻

Quick Summary

Given a string s, return the longest palindromic substring in s.

⸻

Examples

Example 1

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2

Input: s = "cbbd"
Output: "bb"

⸻

Constraints
	•	1 <= s.length <= 1000
	•	s consists of only digits and English letters.

⸻

Follow-up

Can you solve it in O(n²) time using only O(1) space?

⸻

Solution Files

File	Idea	Time	Space
solution.py	Expand Around Center	O(n²)	O(1)
solution_dp.py	Dynamic Programming (2D table)	O(n²)	O(n²)
solution_manacher.py	Manacher’s Algorithm (advanced)	O(n)	O(n)



⸻

日本語サマリ

文字列 s が与えられたとき、最長の回文部分文字列を返す。
「回文」とは前から読んでも後ろから読んでも同じ文字列のこと。

⸻

参照実装

ファイル	アプローチ	時間	メモリ
solution.py	中心展開法（Expand Around Center）	O(n²)	O(1)
solution_dp.py	動的計画法（2次元DP）	O(n²)	O(n²)
solution_manacher.py	Manacherアルゴリズム（上級者向け）	O(n)	O(n)



⸻
