# 0004. Median of Two Sorted Arrays

- **Difficulty**: Hard  
- **Link**: <https://leetcode.com/problems/median-of-two-sorted-arrays/>

> **Disclaimer**  
> Problem description © LeetCode LLC.  
> This file contains only a brief summary and original notes; please refer to the official link above for the full text.

---

## Quick Summary

Given **two sorted arrays** `nums1` and `nums2` of sizes `m` and `n`, return **the median** of the combined multiset.  
An `O(log (m+n))` algorithm is required.

---

## Follow-up

- Prove that an \(O(\log(m+n))\) solution must use **binary search** on at least one array.

---

## Solution Files

| File          | Idea (English)                | Time | Space |
|---------------|------------------------------|------|-------|
| `solution.py` | Binary search on partitions  | `O(log min(m,n))` | `O(1)` |

---

# 日本語サマリ

ソート済み配列 `nums1` と `nums2` を **マージせず** に中央値を求める問題。  
短い方の配列に対して二分探索し、**左右のパーティションが必ず昇順になる位置** を探す。  
奇数長の場合は大きい側の最小値、偶数長の場合は左右パーティション最大・最小の平均が中央値。

---

## 参照実装

| ファイル        | アプローチ                       | 時間            | メモリ |
|-----------------|---------------------------------|-----------------|--------|
| `solution.py`   | パーティション二分探索           | `O(log min(m,n))` | `O(1)` |
