# 0001. Two Sum

- **Difficulty**: Easy  
- **Link**: <https://leetcode.com/problems/two-sum/>

> **Disclaimer**  
> Problem description © LeetCode LLC.  
> This file contains only a brief summary and original notes; please refer to the official link above for the full text.

---

## Quick Summary

Given an integer array `nums` and an integer `target`, find **two distinct indices** such that `nums[i] + nums[j] = target`.  
Exactly one valid pair exists.

---

## Follow-up

Design an algorithm faster than `O(n²)`.

---

## Solution Files

| File | Idea | Time | Space |
|------|------|------|-------|
| `solution.py` | One-pass hash map | `O(n)` | `O(n)` |
| `solution_bruteforce.py` | Double loop | `O(n²)` | `O(1)` |

---

# 日本語サマリ

整数配列 `nums` と整数 `target` が与えられたとき、  
合計が `target` になる **異なる 2 要素のインデックス** を返す。  
解は一意であり、高速解 (`O(n)`) としてハッシュ法が知られている。

---

## 参照実装

| ファイル | アプローチ | 時間 | メモリ |
|----------|-----------|------|--------|
| `solution.py` | ハッシュ 1 パス | `O(n)` | `O(n)` |
| `solution_bruteforce.py` | 全探索 | `O(n²)` | `O(1)` |