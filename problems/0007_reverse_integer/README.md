# 0007. Reverse Integer

* **Difficulty**: Medium
* **Link**: [https://leetcode.com/problems/reverse-integer/description/](https://leetcode.com/problems/reverse-integer/description/)

> **Disclaimer**
> Problem description © LeetCode LLC.
> This README is **only** a concise summary and solution‑note; please refer to the official link for the full statement.

---

## Problem Statement (condensed)

Given a **signed 32‑bit integer** `x`, return its digits **reversed**.
If the reversal would push the result outside the range
`[-2^31, 2^31 − 1]`, **return `0` instead**.

**Assume the runtime environment does *not* allow 64‑bit integers.**

### Examples

|  #  | Input      | Output |
| :-: | ---------- | ------ |
|  1  | `x = 123`  | `321`  |
|  2  | `x = -123` | `-321` |
|  3  | `x = 120`  | `21`   |

### Constraints

* `-2^31 ≤ x ≤ 2^31 − 1`

---

## Intuition

*Reversing* a decimal number can be achieved by repeatedly **popping** the
last digit (`pop = x % 10`) and **pushing** it onto a growing result
(`rev = rev × 10 + pop`).
Because the target range fits in 32 bits (signed), we can detect **overflow
*before* it happens** using integer division:

```
if rev  >  INT_MAX // 10 or (
   rev == INT_MAX // 10 and pop > 7):   #  2^31−1 ends with …7
    return 0    # would overflow
```

(The symmetrical check applies for the negative bound.)

Since each digit is processed once, the algorithm runs in `O(log|x|)` time
and `O(1)` extra space.

---

## Approaches

|  #  | Idea / Technique      | Sketch                                                                                                  | Time                | Extra Space |     |        |
| :-: | --------------------- | ------------------------------------------------------------------------------------------------------- | ------------------- | ----------- | --- | ------ |
|  1  | **Pop & Push (Math)** | Loop while `x ≠ 0`: `pop = x % 10`, `x //= 10`, guard overflow, `rev = rev*10 + pop`, keep sign.        | \`O(log             | x           | )\` | `O(1)` |
|  2  | **String reversal**   | Convert to string, slice `[::-1]`, re‑attach sign, cast back to `int`, range‑check. *(Simpler to code)* | `O(L)` (`L` digits) | `O(L)`      |     |        |

---

## Reference Implementations

| Language   | File           | Approach        |
| ---------- | -------------- | --------------- |
| Python     | `solution.py`  | Pop & Push      |
| C++        | `solution.cpp` | Pop & Push      |
| JavaScript | `solution.js`  | String reversal |

All implementations operate in **O(log|x|)** time and meet the 32‑bit
constraint without using 64‑bit integers.

---

# 日本語サマリ

### 問題概要

32 ビット符号付き整数 `x` の桁を反転し、範囲外に
なる場合は `0` を返す。 64 ビット整数は使用できない。

### 直感

桁を 1 つずつ取り出して新しい数を構築する "Pop & Push" が
最も直接的。各ステップで **桁あふれ** を事前チェックすれば安全。

### 解法比較

|  #  | アプローチ      | 手順                                   | 計算量                   |   |                  |
| :-: | ---------- | ------------------------------------ | --------------------- | - | ---------------- |
|  1  | Pop & Push | `x` から末尾桁を取り出し `rev` に積む。あふれ判定を毎回実施。 | 時間 \`O(log            | x | )`、追加メモリ `O(1)\` |
|  2  | 文字列反転      | 符号を除いた文字列を反転し `int()` に戻す。           | 時間 `O(L)`, メモリ `O(L)` |   |                  |

いずれも 32 ビット範囲を超えない場合のみ結果を返す。
