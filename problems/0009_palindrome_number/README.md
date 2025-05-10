思考時間: 6 秒

# 0009. Palindrome Number

* **Difficulty**: Easy
* **Link**: [https://leetcode.com/problems/palindrome-number/](https://leetcode.com/problems/palindrome-number/)

> **Disclaimer**
> Problem description © LeetCode LLC.
> This README is **only** a concise summary and solution-note; please visit the official link for the full statement.
> The format follows our repository template (see `problem_example.md`).

---

## Problem Statement (condensed)

Return `true` if an integer `x` reads the same backward as forward (palindrome); otherwise return `false`.

### Examples

| #  | Input      | Output  | Explanation     |
| :- | :--------- | :------ | :-------------- |
| 1  | `x = 121`  | `true`  | `121` → `121`   |
| 2  | `x = -121` | `false` | `-121` → `121-` |
| 3  | `x = 10`   | `false` | `10` → `01`     |

### Constraints

* `-2³¹ ≤ x ≤ 2³¹ − 1`

### Follow-up

Solve it **without converting the integer to a string**.

---

## Intuition

* Negative numbers cannot be palindromes (leading `-` has no mirror).
* For non-negative `x`, reverse **only the lower half of the digits** and compare with the remaining upper half:

```
orig = x
rev  = 0
while orig > rev:
    rev  = rev*10 + orig%10
    orig //= 10
```

* When the loop stops, either `orig == rev` (even length) or `orig == rev//10` (odd length).
* This avoids overflow and meets the follow-up.

---

## Approaches

|  #  | Idea                     | Sketch                                                                                  | Time | Extra Space |
| :-: | ------------------------ | --------------------------------------------------------------------------------------- | ---: | ----------: |
|  1  | **String reversal**      | `s = str(x)` → `s == s[::-1]`. Simple but uses `O(d)` memory and fails the follow-up.   | O(d) |        O(d) |
|  2  | **Reverse half (math)**  | Loop above; stop when `orig ≤ rev`; compare (`orig == rev` or `orig == rev//10`).       | O(d) |        O(1) |
|  3  | **Full reverse & guard** | Reverse all digits into `rev`; early-exit if `rev > 2³¹−1`; then compare with original. | O(d) |        O(1) |

`d` = number of digits (≤ 10 for 32-bit integers).

---

## Reference Implementations

| Language | File                  | Approach     |
| -------- | --------------------- | ------------ |
| Python   | `solution.py`         | Reverse half |
| C++      | `solution.cpp` (TBD)  | Reverse half |
| Java     | `Solution.java` (TBD) | Reverse half |

All run in **O(d)** time and **O(1)** extra space.

---

# 日本語サマリ

### 問題概要

整数 `x` が **回文数** かどうか判定せよ。
負数は回文になり得ない（先頭の `-` に対応する末尾が無い）。

### 例

1. `x = 121` → `true`
2. `x = -121` → `false` (`-121` → `121-`)
3. `x = 10` → `false` (`10` → `01`)

### 制約

* `-2³¹ ≤ x ≤ 2³¹ − 1`

#### フォローアップ

文字列に変換せずに解くこと。

---

## 発想

* 非負の `x` について、**下位桁を逆順に取り出して半分だけ** `rev` に積み上げ、
  `x` を半分ずつ削る。`orig ≤ rev` になった時点で停止。
* 長さ偶数なら `orig == rev`、奇数なら中央桁を除いた `orig == rev//10` で回文判定できる。
* 32ビット境界を超える心配がなく、補助メモリは **O(1)**。

---

## 解法比較

|  #  | アプローチ         | 手順 / ポイント                       | 時間   | 補助メモリ |
| :-: | ------------- | ------------------------------- | ---- | ----- |
|  1  | 文字列反転         | 文字列化→反転比較。簡単だが追加メモリ `O(d)`      | O(d) | O(d)  |
|  2  | 下半分だけ反転法      | 桁を1つずつ `rev` へ、`orig ≤ rev` で停止 | O(d) | O(1)  |
|  3  | 全桁反転＋オーバフロー判定 | 全桁を反転し32ビットチェック後比較              | O(d) | O(1)  |

---

## 参照実装

| 言語     | ファイル                 | 採用手法     |
| ------ | -------------------- | -------- |
| Python | `solution.py`        | 下半分だけ反転法 |
| C++    | `solution.cpp` (予定)  | 下半分だけ反転法 |
| Java   | `Solution.java` (予定) | 下半分だけ反転法 |

いずれも **O(d)** 時間、補助メモリ **O(1)** でフォローアップ要件を満たす。
