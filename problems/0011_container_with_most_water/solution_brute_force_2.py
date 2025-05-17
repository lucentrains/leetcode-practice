from itertools import combinations
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Brute-force O(n²) 解法 ――「何をしているか」が一目で分かるよう、
        手順を 3 ステップに分解して書いています。

        1) すべてのインデックス組 (i, j) を combinations で順番に取り出す
        2) その 2 本で作られる容器の面積 = 低い方の高さ × 幅(j-i) を計算
        3) 最大値を更新し続け、最後に返す
        """
        # インデックスが 0, 1 だけなら面積は 0
        if len(height) < 2:
            return 0

        max_area = 0

        # 1) すべての (i, j) を列挙
        for i, j in combinations(range(len(height)), 2):
            # 2) 各ペアの面積を求める
            shorter_height = min(height[i], height[j])
            width = j - i
            area = shorter_height * width

            # 3) 最大値を記録
            if area > max_area:
                max_area = area

        return max_area