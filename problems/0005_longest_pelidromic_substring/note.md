# Python における半開区間 `[i, j)`

(右端 **j** を “含まない”；開始 **i** を “含む”)

---

## 1. そのまま `s[i:j]` に渡せる

Python のスライスは **開始を含み・終了を含まない** 仕様です。

```python
s[i:j]   # 文字列、リスト、タプルなどで同じ
```

- 切り出される長さは常に `j - i`。  
  `len(s[i:j]) == j - i` が追加の調整なく成り立つ。  
- `j` を次の区間の開始として共有できるため、重なりや欠けを心配しなくて済む。

---

## 2. オフバイワンバグを避けやすい

- 終点を含める方式だと **+1**／**–1** の調整が頻出し、ミスを誘発しやすい。  
- 半開区間では境界をそのまま引き回すだけ：

  ```python
  while left < right:   # right は “次の位置” だから < で十分
      ...
  ```

---

## 3. 長さ計算・インデックス演算が直感的

| 操作                       | 半開区間での式    | 説明                                      |
| -------------------------- | ----------------- | ----------------------------------------- |
| 区間の長さ                 | `j - i`           | 引き算するだけ。境界を意識しなくてよい。 |
| 次に続く隣接区間             | `[j, k)`          | `j` をそのまま再利用するだけ。             |
| 前の隣接区間               | `[h, i)`          | `i` をそのまま終端として使う。             |

> **イメージ**:
>
> ```
> ├─── [i, j) ───┤├─── [j, k) ───┤
>         ↑ 共通境界 j
> ```

---

## 4. `range()` と同じルールなので一貫性がある

```python
for t in range(i, j):   # i 以上 j 未満を繰り返す
    ...
```

- ループの番兵とスライスの仕様が一致し、“ループで調べた区間をそのまま切り出す” コードが読みやすい。

---

## 5. 空区間を自然に表現できる

- `i == j` のとき、長さ 0 の区間（境界が一致）として明確に示せる。  
- 終点含める方式では空集合の表現に特別処理が必要になる。

---

## 6. 負のインデックスとも相性が良い

- `s[i:-1]` は “末尾の要素を含めず、そのひとつ手前まで” を表す。  
- 終点含める方式だと `-1` が「最後の要素そのもの」を指し、追加の調整を要する。

---

# Half-Open Interval `[i, j)` in Python

(End **j** is _exclusive_; start **i** is _inclusive_)

---

## 1. Directly Works with `s[i:j]`

Python slicing uses an **inclusive start, exclusive end** convention:

```python
s[i:j]   # works for strings, lists, tuples, etc.
```

- The length of the slice is always `j - i`, so  
  `len(s[i:j]) == j - i` holds true without extra adjustment.  
- You can treat `j` as the next interval’s start, avoiding overlap or gaps.

---

## 2. Avoids Off-By-One Bugs

- Inclusive-end intervals often require frequent **+1** or **–1** adjustments, leading to mistakes.  
- With half-open intervals, you simply carry the boundary values forward:

  ```python
  while left < right:   # right is the “next position,” so < is correct
      ...
  ```

---

## 3. Intuitive Length and Index Calculations

| Operation                    | Half-Open Formula | Explanation                             |
| ---------------------------- | ----------------- | --------------------------------------- |
| Interval length              | `j - i`           | Just subtract—no boundary fiddling.     |
| Next adjacent interval       | `[j, k)`          | Reuse `j` as the start of the next one. |
| Previous adjacent interval   | `[h, i)`          | Reuse `i` as the end.                   |

> **Visual**:
>
> ```
> ├─── [i, j) ───┤├─── [j, k) ───┤
>         ↑ shared boundary j
> ```

---

## 4. Consistent with `range()`

```python
for t in range(i, j):   # runs from i up to, but not including, j
    ...
```

- Loop indices and slice boundaries follow the same rule, making code easier to read: “Slice exactly the elements you just iterated over.”

---

## 5. Natural Representation of Empty Intervals

- When `i == j`, the interval is empty (length 0)—it clearly indicates “boundaries have met.”  
- Inclusive-end conventions need special handling to represent an empty range.

---

## 6. Plays Well with Negative Indices

- `s[i:-1]` means “from i up to (but not including) the last element.”  
- With inclusive-end semantics, `-1` refers to the last element itself, forcing extra adjustments.

---

### Summary

- Aligning with Python’s slice and `range()` semantics by using `[start, end)` means all length calculations, loops, and adjacent-interval logic boil down to simple subtraction and reuse of boundaries.  
- The result is **shorter, clearer code** with far fewer off-by-one errors.  
- Many other languages and libraries (C/C++, JavaScript, Rust, etc.) adopt the same “half-open” convention, and most algorithm texts use `[i, j)` notation for that reason.
