from typing import List

class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        """
        Retrun the median of two sorted arrays in O(log min(m, n)) time.

        Strategy
        -------
        1. 二分探索を短い配列('nums1')にのみ適用して境界を探す。
        2. "左側の最大 <= 右側の最小" となるパーティションが見つかれば、
            - 奇数合計なら左側最大が中央値
            - 偶数合計なら左右境界2要素の平均
        """
        # 1. 必ずnums1が短い方の配列になるようにする
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        total = m + n
        low, high = 0, m

        NEG_INF, POS_INF = float("-inf"), float("inf")  # ガード値

        # 2. nums1 上で二分探索
        while low <= high:
            cut1 = (low + high) // 2            # nums1 の境界
            cut2 = (total + 1) // 2 - cut1      # nums2 の境界

            # 左右の境界値を取得（端にあたったら +- inf で埋める）
            left1 = NEG_INF if cut1 == 0 else nums1[cut1 - 1]
            right1 = POS_INF if cut1 == m else nums1[cut1]

            left2 = NEG_INF if cut2 == 0 else nums2[cut2 - 1]
            right2 = POS_INF if cut2 == n else nums2[cut2]     
        
            # 3.正しいパーティションか判定
            if left1 <= right2 and left2 <= right1:
                # 4. 中央値を返す
                if (m + n) % 2:                 # 奇数長
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2

            # 5. 条件を満たさない場合は探索範囲を更新
            if left1 > right2:                  # nums1 側が大きすぎる
                high = cut1 - 1                 # 左へ
            else:                               # nums2 側が小さすぎる
                low = cut1 + 1                  # 右へ