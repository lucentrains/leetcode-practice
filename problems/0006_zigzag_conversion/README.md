思考時間: 9 秒


# 0006. Zigzag Conversion

* **Difficulty**: Medium
* **Link**: [https://leetcode.com/problems/zigzag-conversion/description/](https://leetcode.com/problems/zigzag-conversion/description/)

> **Disclaimer**
> Problem description © LeetCode LLC.
> This README is **only** a concise summary and solution-note; please refer to the official link for the full statement.

---

## Problem Statement (condensed)

Write the characters of a string `s` in a **zig-zag pattern** over `numRows` rows, then read the rows top-to-bottom to obtain a new string.

```
PAYPALISHIRING      (numRows = 3)
P   A   H   N
A P L S I I G   →   PAHNAPLSIIGYIR
Y   I   R
```

If `numRows ≤ 1` **or** `numRows ≥ |s|`, return `s` unchanged.

### Examples

|  #  | Input                               | Output             |
| :-: | ----------------------------------- | ------------------ |
|  1  | `s = "PAYPALISHIRING", numRows = 3` | `"PAHNAPLSIIGYIR"` |
|  2  | `s = "PAYPALISHIRING", numRows = 4` | `"PINALSIGYAHRPI"` |
|  3  | `s = "A", numRows = 1`              | `"A"`              |

<details><summary>Example 2 pattern</summary>

```
P     I    N
A   L S  I G
Y A   H R
P     I
```

</details>

### Constraints

* `1 ≤ |s| ≤ 1000`
* `s` consists of English letters (upper/lower case), `,`, and `.`
* `1 ≤ numRows ≤ 1000`

---

## Intuition

Moving straight down, then diagonally up forms a repeating **cycle** of length

```
cycle = 2 × numRows − 2        (when numRows ≥ 2)
```

For any index `i` in `s`:

```python
row = i % cycle
if row >= numRows:          # upward stroke of the V
    row = cycle - row
```

So the target row is computable in **O(1)** time per character, no 2-D grid needed.

---

## Approaches

|  #  | Idea                       | Sketch                                                                                                                               | Time | Extra Space |
| :-: | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---: | ----------: |
|  1  | **Row buffers**            | Keep `rows = [""] * numRows`; append chars while toggling a `down` flag.                                                             | O(n) |        O(n) |
|  2  | **Arithmetic scan**        | Use the formula above to get `row` for each index, then `rows[row] += c`.                                                            | O(n) |        O(n) |
|  3  | **Index jump (O (1) aux)** | For each row, append chars at indices `row + k·cycle` and the middle diagonal index (when applicable). Uses only the output builder. | O(n) |      O(1)\* |

\* Excluding the output string itself.

---

## Reference Implementations

| Language | File               | Approach        |
| -------- | ------------------ | --------------- |
| Python   | `solution.py`      | Row buffers     |
| Python   | `solution_math.py` | Arithmetic scan |
| C++      | `solution.cpp`     | Index jump      |
| Go       | `solution.go`      | Arithmetic scan |

All run in `O(n)` time (`n = |s|`); memory varies as noted.

---

# 日本語サマリ

### 問題概要

文字列 `s` を **ジグザグパターン**で `numRows` 行に並べ、行を上から順に読み取った文字列を返す。

```
PAYPALISHIRING        (numRows = 3)
P   A   H   N
A P L S I I G   →   PAHNAPLSIIGYIR
Y   I   R
```

* `numRows ≤ 1` または `numRows ≥ |s|` なら変換せず `s` を返す。

### 例

1. `s="PAYPALISHIRING", numRows=3` → `"PAHNAPLSIIGYIR"`
2. `s="PAYPALISHIRING", numRows=4` → `"PINALSIGYAHRPI"`
3. `s="A", numRows=1` → `"A"`

### 制約

* `1 ≤ |s| ≤ 1000`
* `s` は英字・`,`・`.` のみ
* `1 ≤ numRows ≤ 1000`

---

## 発想

* **1周期** は下方向 `numRows`、斜め上方向 `numRows−2` で構成。
  ⇒ 周期長 `cycle = 2×numRows − 2`。
* インデックス `i` が属する行は

```python
row = i % cycle
if row >= numRows:    # 折り返し部分
    row = cycle - row
```

* これにより **O(1)** で行が求まり、一次元走査だけで解ける。

---

## 解法比較

|  #  | アプローチ        | 手順                              | 時間   | 追加メモリ  |
| :-: | ------------ | ------------------------------- | ---- | ------ |
|  1  | 行バッファ法       | 行ごとにバッファを持ち、下→上で方向を反転           | O(n) | O(n)   |
|  2  | 周期算出法        | 上式で行を直接算出してバッファに追加              | O(n) | O(n)   |
|  3  | 行ごとのインデックス飛び | 行を固定し `row + k·cycle` 型の位置を順に追加 | O(n) | O(1)\* |

\* 出力用バッファを除くと **O(1)** でフォローアップ要件を満たす。

---

## 参照実装

| 言語     | ファイル               | 採用手法     |
| ------ | ------------------ | -------- |
| Python | `solution.py`      | 行バッファ法   |
| Python | `solution_math.py` | 周期算出法    |
| C++    | `solution.cpp`     | インデックス飛び |
| Go     | `solution.go`      | 周期算出法    |

いずれも **O(n)** 時間、メモリは上表の通り。
