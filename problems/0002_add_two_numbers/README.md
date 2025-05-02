# 0002. Add Two Numbers

- **Difficulty**: Medium  
- **Link**: <https://leetcode.com/problems/add-two-numbers/>

> **Disclaimer**  
> Problem description © LeetCode LLC.  
> This file contains only a brief summary and original notes; please refer to the official link above for the full text.

---

## Quick Summary

You are given two non-empty singly-linked lists `l1` and `l2` that represent two non-negative integers in **reverse order** (least-significant digit first).  
Each node stores a single digit.  
Return a linked list representing `l1 + l2`, also in reverse order.

---

## Follow-up

How would you handle the case where the input lists are extremely long and cannot fit in memory all at once?

---

## Solution Files

| File                    | Idea / Approach     | Time Complexity | Space Complexity |
|-------------------------|---------------------|-----------------|------------------|
| `solution.py`           | Iterative carry-prop addition | `O(max(m, n))` | `O(max(m, n))` |
| `solution_recursive.py` | Recursive (DFS) addition with carry returned up the call stack | `O(max(m, n))` | `O(max(m, n))` |

*`m` and `n` are the lengths of `l1` and `l2`.*

---

# 日本語サマリ

2 つの **非空の** 単一リンクリスト `l1`, `l2` が与えられ、それぞれが数字を **逆順** に格納している。  
各ノードには 0–9 の 1 桁が入り、先頭が最下位桁を示す。  
両数を加算し、和を同じ形式のリンクリストで返す。

---

## 参照実装

| ファイル | アプローチ               | 計算量 (時間) | 計算量 (メモリ) |
|----------|-------------------------|---------------|-----------------|
| `solution.py` | 走査＋桁上げ (`carry`) を逐次処理 | `O(max(m, n))` | `O(max(m, n))` |
| `solution_recursive.py` | 再帰的に桁上げを伝搬 | `O(max(m, n))` | `O(max(m, n))` |