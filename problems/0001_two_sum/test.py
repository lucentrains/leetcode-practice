# tests.py
import pytest

# 同じディレクトリに solution.py がある想定
from solution import Solution

# ----------------------------
# テストケース（入力, target, 期待するインデックス）
# ----------------------------
TEST_CASES = [
    ([2, 7, 11, 15], 9,  [0, 1]),
    ([3, 2, 4],       6,  [1, 2]),
    ([3, 3],          6,  [0, 1]),
]

@pytest.mark.parametrize("nums,target,expected", TEST_CASES)
def test_two_sum(nums, target, expected):
    """Two Sum should return indices that sum to target (order-agnostic)."""
    result = Solution().twoSum(nums, target)

    # 結果は順不同で可なので集合比較
    assert set(result) == set(expected), f"got {result}, want {expected}"