## Study Notes

The following topics have been covered so far:

---

### 1. Extracting the Hundreds Digit

```python
n = 12345
hundreds = (n // 100) % 10   # → 3
```

* `n // 100`: floor-divide by 100 to remove the last two digits → `123`
* `(…) % 10`: extract the hundreds digit

**Function Version:**

```python
def hundreds_digit(n: int) -> int:
    return abs(n) // 100 % 10
```

---

### 2. Splitting an Integer into a List of Digits

```python
n = 12345
digits = list(map(int, str(n)))   # → [1, 2, 3, 4, 5]
```

* `str(n)`: convert integer to string
* `map(int, …)`: apply `int()` to each character
* `list(…)`: collect into a list `[1, 2, 3, 4, 5]`

**Alternative Methods:**

```python
# List comprehension
digits = [int(c) for c in str(abs(n))]

# Arithmetic method
def int_to_digits(n: int) -> list[int]:
    if n == 0:
        return [0]
    n = abs(n)
    out = []
    while n:
        out.append(n % 10)
        n //= 10
    return out[::-1]
```

---

### 3. Reversing a List

```python
rev1 = digits[::-1]                # slicing
rev2 = list(reversed(digits))      # built-in reversed()
digits.reverse()                   # in-place reverse
```

* `[::-1]`: slicing to get a reversed copy
* `reversed()`: returns an iterator; wrap with `list()`
* `list.reverse()`: reverses the list in-place

---

### 4. Reversing an Integer to Get `54321`

**Method 1: String Operations**

```python
rev = int(str(n)[::-1])
```

**Method 2: Arithmetic Only**

```python
def reverse_int_math(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n:
        rev = rev * 10 + (n % 10)
        n //= 10
    return sign * rev
```

**Method 3: Generic Function**

```python
def reverse_number(n: int) -> int:
    s = str(n)
    if s[0] == '-':
        return -int(s[:0:-1])
    return int(s[::-1])
```

---

### 5. 32-bit Integer Reversal Problem (LeetCode)

**Problem Statement:**
Given a signed 32‑bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32‑bit integer range \[-2³¹, 2³¹−1], then return 0.

**Example:**
`1534236469` → reversed → `9646324351` → exceeds `2147483647` → returns `0`.

**Sample Solution:**

```python
def reverse_int(x: int) -> int:
    sign = -1 if x < 0 else 1
    s = str(abs(x))[::-1]
    rev = int(s)
    if rev > 2**31 - 1:
        return 0
    return sign * rev
```

---

### 6. Loop Implementation Using `divmod`

```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > 2**31 - 1:
                return 0
        return sign * rev
```

* `divmod(x, 10)` returns `(x // 10, x % 10)`
* `while x:` continues while `x` is non-zero

---

### 7. Meaning of `while x:`

* Integer `0` is False; non-zero is True
* `while x:` is equivalent to `while x != 0:`
* Continues loop until all digits are processed

---

### 8. Optimized Implementation (`log10` + `10**n`)

```python
from math import log10
class Solution:
    def is_32bit(self, x: int) -> bool:
        return -2**31 <= x <= 2**31 - 1
    def reverse(self, x: int) -> int:
        if not self.is_32bit(x): return 0
        if -10 < x < 10: return x
        is_neg = x < 0
        x = abs(x)
        x_len = int(log10(x))
        rev = 0
        while x:
            rev += (x % 10) * 10**x_len
            x_len -= 1
            x //= 10
        if is_neg:
            rev = -rev
        return rev if self.is_32bit(rev) else 0
```

* Eliminates string conversion overhead
* Precompute digit count with `log10` and exponentiation
* `%`, `//`, `**` are implemented in C for performance

---

### 9. Usage of `divmod(x, 10)`

```python
q, r = divmod(123, 10)      # q=12, r=3
int_part, frac_part = divmod(123.456, 1)  # int_part=123.0, frac_part≈0.456
```

* Returns `(quotient, remainder)` or `(integer part, fractional part)`
* Negative numbers: floor division → `divmod(-123, 10)` → `(-13, 7)`
* More concise and slightly faster than separate `//` and `%`

---

## 学習記録

これまで学んだ内容をまとめます。

---

### 1. 100 の位の数字を取り出す

```python
n = 12345
hundreds = (n // 100) % 10   # → 3
```

* `n // 100`: 下3桁を切り捨て → `123`
* `(…) % 10`: 100 の位の一桁を取得

**関数化：**

```python
def hundreds_digit(n: int) -> int:
    return abs(n) // 100 % 10
```

---

### 2. 整数を桁ごとのリストに分解

```python
n = 12345
digits = list(map(int, str(n)))   # → [1, 2, 3, 4, 5]
```

* `str(n)`: 整数を文字列に変換
* `map(int, …)`: 各文字を `int` に変換
* `list(…)`: リスト `[1, 2, 3, 4, 5]` にまとめる

**他の方法：**

```python
# リスト内包表記
digits = [int(c) for c in str(abs(n))]

# 余り演算
def int_to_digits(n: int) -> list[int]:
    if n == 0:
        return [0]
    n = abs(n)
    out = []
    while n:
        out.append(n % 10)
        n //= 10
    return out[::-1]
```

---

### 3. リストを逆順にする

```python
rev1 = digits[::-1]                # スライス
rev2 = list(reversed(digits))      # reversed()
digits.reverse()                   # in-place
```

* `[::-1]`: スライスで逆順コピー
* `reversed()`: イテレータを返すので `list()` でリスト化
* `list.reverse()`: 元リストを直接逆順に変更

---

### 4. 整数を反転して `54321` にする

**方法1: 文字列操作**

```python
rev = int(str(n)[::-1])
```

**方法2: 演算のみ**

```python
def reverse_int_math(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n:
        rev = rev * 10 + (n % 10)
        n //= 10
    return sign * rev
```

**方法3: 汎用関数**

```python
def reverse_number(n: int) -> int:
    s = str(n)
    if s[0] == '-':
        return -int(s[:0:-1])
    return int(s[::-1])
```

---

### 5. 32bit 整数反転問題 (LeetCode)

**問題文：**
有効範囲：\[-2³¹, 2³¹−1]

**例：**
`1534236469` → `9646324351` → 上限 `2147483647` 超過 → `0`

**サンプル解法：**

```python
def reverse_int(x: int) -> int:
    sign = -1 if x < 0 else 1
    s = str(abs(x))[::-1]
    rev = int(s)
    if rev > 2**31 - 1:
        return 0
    return sign * rev
```

---

### 6. `divmod` を使ったループ実装

```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > 2**31 - 1:
                return 0
        return sign * rev
```

* `divmod(x, 10)`: 商と余りを同時取得
* `while x:`: `x != 0` を意味

---

### 7. `while x:` の意味

* 整数 `0` は偽、非ゼロは真
* `while x:` は `while x != 0:` と同じ
* `x` がゼロになるまでループを継続

---

### 8. 高速化実装 (`log10` + `10**n`)

```python
from math import log10
class Solution:
    def is_32bit(self, x: int) -> bool:
        return -2**31 <= x <= 2**31 - 1
    def reverse(self, x: int) -> int:
        if not self.is_32bit(x): return 0
        if -10 < x < 10: return x
        is_neg = x < 0
        x = abs(x)
        x_len = int(log10(x))
        rev = 0
        while x:
            rev += (x % 10) * 10**x_len
            x_len -= 1
            x //= 10
        if is_neg:
            rev = -rev
        return rev if self.is_32bit(rev) else 0
```

* 文字列操作を排除
* `log10` で桁数を事前計算
* `%`, `//`, `**` は C 実装で高速

---

### 9. `divmod(x, 10)` の使い方

```python
q, r = divmod(123, 10)      # q=12, r=3
int_part, frac_part = divmod(123.456, 1)  # int_part=123.0, frac_part≈0.456
```

* `(quotient, remainder)` または `(整数部, 小数部)` を返す
* 負数: floor division ルール → `divmod(-123, 10)` → `(-13, 7)`
* `//` と `%` を別々に呼ぶより簡潔で高速
