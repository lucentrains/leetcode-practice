# tests.py
import pytest

from solution import Solution as HashMapSolution
from solution_bruteforce import Solution as BruteForceSolution

# ----------------------------
# テストケース（入力, target, 期待するインデックス）
# ----------------------------
TEST_CASES = [
    ([2, 7, 11, 15], 9,  [0, 1]),
    ([3, 2, 4],       6,  [1, 2]),
    ([3, 3],          6,  [0, 1]),
]

# テスト対象となる実装クラス
IMPLEMENTATIONS = [HashMapSolution, BruteForceSolution]

@pytest.mark.parametrize("impl_cls", IMPLEMENTATIONS, ids=lambda cls: cls.__name__)
@pytest.mark.parametrize("nums,target,expected", TEST_CASES)
def test_two_sum(impl_cls, nums, target, expected):
    """Two Sum should return indices that sum to target (order-agnostic)."""
    result = impl_cls().twoSum(nums, target)
    assert set(result) == set(expected), f"{impl_cls.__name__}: got {result}, want {expected}"