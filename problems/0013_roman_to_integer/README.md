思考時間: 5 秒

# 0013. Roman to Integer

* **Difficulty**: Easy
* **Link**: [https://leetcode.com/problems/roman-to-integer/](https://leetcode.com/problems/roman-to-integer/)

> **Disclaimer**
> Problem description © LeetCode LLC.
> This README is **only** a concise summary and solution-note; please visit the official link for the full statement.
> Format follows the repository’s existing problem template.

---

## Problem Statement (condensed)

Convert a Roman numeral string `s` to its integer value.

Roman symbols and values:

| Symbol | Value |
| :----: | ----: |
|    I   |     1 |
|    V   |     5 |
|    X   |    10 |
|    L   |    50 |
|    C   |   100 |
|    D   |   500 |
|    M   |  1000 |

Subtractive pairs (six only):

```
IV  4   IX  9
XL 40   XC 90
CD 400  CM 900
```

### Examples

|  #  | Input       | Output | Explanation        |
| :-: | :---------- | -----: | ------------------ |
|  1  | `"III"`     |    `3` | `I + I + I`        |
|  2  | `"LVIII"`   |   `58` | `L + V + III`      |
|  3  | `"MCMXCIV"` | `1994` | `M + CM + XC + IV` |

### Constraints

* `1 ≤ |s| ≤ 15`
* `s` contains only `I,V,X,L,C,D,M` and is a valid numeral in `[1, 3999]`.

---

## Intuition

When a smaller-valued symbol precedes a larger one, it must be **subtracted** instead of added.
Scanning the string and comparing each symbol with the one that follows (or precedes) captures this rule in O(1) extra space.

---

## Approaches

|  #  | Idea / Approach                    | Sketch                                                                                                    | Time | Extra Space |
| :-: | ---------------------------------- | --------------------------------------------------------------------------------------------------------- | ---: | ----------: |
|  1  | **Left-to-right compare next**     | For each index `i`, if `value(s[i]) < value(s[i+1])` subtract, else add.                                  | O(n) |        O(1) |
|  2  | **Right-to-left compare previous** | Start from the end; maintain `prev`. If `value(curr) < prev`, subtract, else add; update `prev`.          | O(n) |        O(1) |
|  3  | **Two-char look-ahead dictionary** | Consume the string with a pointer; first check a 2-char slice (`IV`, `IX`, …) in a map, else single char. | O(n) |        O(1) |

---

## Reference Implementations

| Language       | File           | Approach           |
| -------------- | -------------- | ------------------ |
| Python         | `solution.py`  | Left-to-right scan |
| C++ (optional) | `solution.cpp` | Right-to-left scan |
| Go (optional)  | `solution.go`  | Dictionary parse   |

All solutions run in O(n) time with O(1) auxiliary memory.

---

# 日本語サマリ

### 問題概要

ローマ数字文字列 `s` を整数に変換せよ（範囲 1-3999）。

### ローマ数字の規則

| 記号 | 値 |   |   |   |    |   |    |   |     |   |     |   |      |
| -- | - | - | - | - | -- | - | -- | - | --- | - | --- | - | ---- |
| I  | 1 | V | 5 | X | 10 | L | 50 | C | 100 | D | 500 | M | 1000 |

減算表記は次の 6 通りのみ：IV, IX, XL, XC, CD, CM。

### 解法

1. **左→右走査**：現在値より右隣が大きければ減算、そうでなければ加算。
2. **右→左走査**：直前の加算値より小さければ減算、そうでなければ加算。
   どちらも **O(n)** 時間、追加メモリ **O(1)**。

---

> Place this file at `problems/roman-to-integer/python/README.md` (and parallel language folders as needed)。
