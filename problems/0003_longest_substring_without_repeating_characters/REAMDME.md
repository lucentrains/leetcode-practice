# 0003. Longest Substring Without Repeating Characters

- **Difficulty**: Medium  
- **Link**: <https://leetcode.com/problems/longest-substring-without-repeating-characters/>

> **Disclaimer**  
> Problem description © LeetCode LLC.  
> This file stores only a brief summary and original notes; please see the official link above for the full text.

---

## Quick Summary

Given a string `s`, return the length of the **longest substring** that contains **no duplicate characters**.  
A substring is a contiguous block of characters (unlike a subsequence).

---

## Follow-ups & Variants

| Variant | Idea |
|---------|------|
| **Character set known / small** | Use an integer array of size 128/256 for constant-time character look-ups. |
| **Very long Unicode strings** | Maintain a `dict` mapping `char → last_seen_index`; this scales with the alphabet size. |
| **Return the substring itself** | Track the window’s start & best length in addition to the length counter. |

---

## Solution Files

| File                       | Technique / Idea        | Time Complexity | Space Complexity |
|----------------------------|-------------------------|-----------------|------------------|
| `solution.py`              | Sliding window + hash map (`dict`) | `O(n)` | `O(k)` where `k` = alphabet size |
| `solution_array.py`        | Sliding window + fixed-size array (ASCII) | `O(n)` | `O(1)` |
| `solution_bruteforce.py`   | All substrings + set check (reference only) | `O(n²)` | `O(n)` |

---

# 日本語サマリ

文字列 **`s`** が与えられたとき、  
**重複しない最長部分文字列** の長さを返す。

- **アルゴリズム**: スライディングウィンドウ  
  - `left` と `right` の 2 ポインタでウィンドウを拡張。  
  - 文字の **最新位置** を `dict`/配列で保持し、重複が見つかったら `left` を更新。  
- **計算量**: `O(n)` 時間・`O(k)` メモリ (`k` = 文字集合のサイズ)。

---

## 参照実装

| ファイル | アプローチ | 時間計算量 | メモリ計算量 |
|----------|-----------|------------|--------------|
| `solution.py` | `dict` による最新出現位置 & ウィンドウ境界更新 | `O(n)` | `O(k)` |
| `solution_array.py` | ASCII 配列版 | `O(n)` | `O(1)` |

