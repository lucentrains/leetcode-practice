# 0008. String to Integer (atoi)

* **Difficulty**: Medium
* **Link**: [https://leetcode.com/problems/string-to-integer-atoi/](https://leetcode.com/problems/string-to-integer-atoi/)

> **Disclaimer**
> Problem description © LeetCode LLC. This README is **only** a concise summary and solution‑note; please see the official problem page for the full wording.

---

## Problem Statement (condensed)

Implement `myAtoi(string s)` that converts the given string to a **32‑bit signed integer** following these rules:

1. **Whitespace** – Skip leading spaces.
2. **Sign** – Optional `'+'` or `'-'`; default is positive.
3. **Digits** – Read consecutive digits (ignoring leading zeros) until a non‑digit or the end of the string.
4. **No digits** – If no digits were read, return `0`.
5. **Clamp** – If the value is outside `[-2³¹, 2³¹ − 1]`, return the nearest bound (`-2³¹` or `2³¹ − 1`).

Return the resulting integer.

### Examples

| # | Input             | Output | Reasoning                       |
| - | ----------------- | ------ | ------------------------------- |
| 1 | `"42"`            | `42`   | Direct parse                    |
| 2 | `"   -042"`       | `-42`  | Whitespace, sign, leading zeros |
| 3 | `"1337c0d3"`      | `1337` | Stop at first non‑digit         |
| 4 | `"0-1"`           | `0`    | Parsing stops after first digit |
| 5 | `"words and 987"` | `0`    | First char is non‑digit         |

### Constraints

* `0 ≤ |s| ≤ 200`
* `s` may contain English letters (upper/lower), digits, space `' '`, `'+'`, `'-'`, and `'.'`.

---

## Intuition

A single linear scan is sufficient. While accumulating the numeric value we must **detect overflow *****before***** it happens**. Because the target range is ±2³¹, we can check

```text
if value > 214748364 or \
   (value == 214748364 and digit > 7):   # 7 for +, 8 for −
    return INT_MAX / INT_MIN accordingly
```

This uses only `O(1)` extra space.

---

## Approach

| # | Idea                  | Sketch                                                                                                     | Time   | Extra Space |
| - | --------------------- | ---------------------------------------------------------------------------------------------------------- | ------ | ----------- |
| 1 | **Single‑pass parse** | Skip spaces → read sign → accumulate digits with overflow guard. Uses 64‑bit temp or explicit bound check. | `O(n)` | `O(1)`      |

### Reference Implementation (Python)

```python
INT_MAX, INT_MIN = 2**31 - 1, -2**31

class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        # 1. skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. sign
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. digits
        num = 0
        while i < n and s[i].isdigit():
            d = ord(s[i]) - 48
            # 4. overflow check before multiplying by 10
            if num > 214748364 or (num == 214748364 and d > (7 if sign > 0 else 8)):
                return INT_MAX if sign > 0 else INT_MIN
            num = num * 10 + d
            i += 1

        return sign * num
```

---

## Tests

`tests.py` should verify edge cases such as:

* Only spaces → `0`
* "+-12" → `0`
* "21474836460" → `2147483647`
* "-91283472332" → `-2147483648`

These capture sign handling, invalid input, and overflow clamping.

---

# 日本語サマリ

以下では、英語セクションと同等の粒度で問題を整理します。

## 問題説明（詳細）

文字列 `s` を読み取り、**32 ビット符号付き整数**（範囲 `[-2³¹, 2³¹‑1]`）に変換する関数 `myAtoi` を作成せよ。手順は次の通り。

1. **空白の除去** ‑ 先頭に連続する半角スペースをすべて読み飛ばす。
2. **符号の決定** ‑ 残りの先頭文字が `'+'` か `'-'` であれば符号とし、どちらでもなければ正数とみなす。
3. **数字の読取り** ‑ 連続する数字を 1 文字ずつ読み取り整数を構築する（先頭の `0` は実際の値には影響しない）。数字以外の文字に遭遇したら読取りを終了する。
4. **数字なしの場合** ‑ 上記手順で 1 桁も数字を読まなかった場合は結果を `0` とする。
5. **範囲外の丸め** ‑ 得られた値が `-2³¹` 未満なら `-2³¹`、`2³¹‑1` を超えるなら `2³¹‑1` に丸める。

最終的に得られた整数を返す。

### 入力例と出力例

| # | 入力文字列             | 返却値    | 補足                 |
| - | ----------------- | ------ | ------------------ |
| 1 | `"42"`            | `42`   | そのまま整数化            |
| 2 | `"   -042"`       | `-42`  | 先頭スペース・負符号・先頭ゼロを処理 |
| 3 | `"1337c0d3"`      | `1337` | 数字列の後ろで非数字で停止      |
| 4 | `"0-1"`           | `0`    | `0` で停止、後続は無視      |
| 5 | `"words and 987"` | `0`    | 先頭が非数字のため `0`      |

### 制約

* `0 ≤ |s| ≤ 200`
* 文字列には英字（大小）、数字、空白、`'+'`、`'-'`、`'.'` が含まれる。

## 考え方

* 文字列を 1 度だけ走査すれば十分。先頭の空白を飛ばしたら、符号・数字読取りを順に実施。
* 10 倍して桁を追加する前に「このまま計算すると `2³¹` を越えるか」を判定して **オーバーフローを事前検知** する。
* Python の `int` は多倍長だが、判定ロジックは C/C++ の 32 ビット制限を模倣する。

## アルゴリズム

1. インデックス `i` を 0 で初期化。
2. `s[i] == ' '` の間 `i++`。
3. 符号を判定し `sign`（±1）を決定。
4. `while s[i].isdigit()` で桁を読取り、`num = num*10 + d`。追加前に以下で丸め確認：

   * `num > 214748364` または
   * `num == 214748364` かつ `d > 7`（正）/ `8`（負）
     なら即座に境界値を返す。
5. ループ終了後 `sign * num` を返却。

## 計算量

* **時間** `O(n)` — 文字列長 n に線形。
* **追加メモリ** `O(1)` — 定数領域のみ使用。

## 参考実装（Python）

英語セクションの `solution.py` と同一。

## テストケース例

```text
""          → 0          # 空文字
"   "       → 0          # 空白のみ
"+-12"       → 0          # 不正な符号
"21474836460" → 2147483647 # 上限超え
"-91283472332" → -2147483648 # 下限超え
```

これらは符号判定、桁溢れ、数字なしを網羅している。
