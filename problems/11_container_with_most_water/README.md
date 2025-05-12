# 0011. Container With Most Water

* **Difficulty**: Medium
* **Link**: [https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/)

> **Disclaimer**
> Problem description © LeetCode LLC.
> This README is **only** a concise summary and solution-note; please refer to the official link for the full statement.

---

## Problem Statement (condensed)

Given an integer array `height`, each element represents the height of a vertical line on the coordinate plane. The two endpoints of the line `i` are `(i, 0)` and `(i, height[i])`. Find two lines that, along with the x-axis, create a container that holds the most water.

Return the maximum water the container can store.

### Examples

|  #  | Input                 | Output |
| :-: | --------------------- | ------ |
|  1  | `[1,8,6,2,5,4,8,3,7]` | `49`   |
|  2  | `[1,1]`               | `1`    |

<details><summary>Example 1 Visualization</summary>

```
[1,8,6,2,5,4,8,3,7]

Vertical lines representation:
  |
  |       |
  |       |  |
  |       |  |  |
  |       |  |  |  |
  |       |  |  |  |  |
  |       |  |  |  |  |     |
| |   | | | | | | | | |
```

Maximum water container area = width (7 units) × height (7 units) = 49.

</details>

### Constraints

* `n == height.length`
* `2 <= n <= 10^5`
* `0 <= height[i] <= 10^4`

---

## Intuition

The goal is to maximize the area, which depends on the height of the shorter line between two points and the distance between them. By starting with two pointers at both ends of the array and moving the pointer of the shorter line inward, the potential for a larger area is systematically explored.

---

## Approaches

|  #  | Idea            | Sketch                                                                                                    | Time | Extra Space |
| :-: | --------------- | --------------------------------------------------------------------------------------------------------- | ---- | ----------- |
|  1  | **Two-pointer** | Start pointers at both ends and move inward based on shorter line height. Keep track of the maximum area. | O(n) | O(1)        |

---

## Reference Implementations

| Language | File          | Approach    |
| -------- | ------------- | ----------- |
| Python   | `solution.py` | Two-pointer |

Runs in `O(n)` time; memory usage is `O(1)`.

---

# 日本語サマリ

### 問題概要

整数配列`height`が与えられ、各要素は座標平面上の垂直な線の高さを示す。2本の線を選び、x軸と共に水を最も多く溜められる容器を作る。

作れる容器の最大の水量を返す。

### 例

1. `[1,8,6,2,5,4,8,3,7]` → `49`
2. `[1,1]` → `1`

### 制約

* `n == height.length`
* `2 <= n <= 10^5`
* `0 <= height[i] <= 10^4`

---

## 発想

面積は2本の線のうち低い方の高さと2本の線の距離によって決まる。配列の両端からポインタを開始し、低い方のポインタを内側に動かすことで、最大面積の可能性を体系的に探索する。

---

## 解法

|  #  | アプローチ   | 手順                             | 時間   | 追加メモリ |
| :-: | ------- | ------------------------------ | ---- | ----- |
|  1  | ツーポインタ法 | 両端にポインタを置き、低い方を内側に動かして最大面積を求める | O(n) | O(1)  |

---

## 参照実装

| 言語     | ファイル          | 採用手法    |
| ------ | ------------- | ------- |
| Python | `solution.py` | ツーポインタ法 |

実行時間は `O(n)`、追加メモリは `O(1)`。
