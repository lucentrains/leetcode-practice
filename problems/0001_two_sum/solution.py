from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Return the indices of the two numbers that add up to ``target``.

        This is the canonical *one-pass hash-map* solution.

        Algorithm
        ----------
        * 1 つずつ要素を走査しながら、  
          `(target - nums[i])` がすでにハッシュ表にあるかをチェック  
        * 見つかればインデックスのペアを返し、  
          見つからなければ ``lookup[num] = i`` として登録する

        Complexity
        ----------
        Time : ``O(n)``
            配列を 1 度だけ走査する
        Space : ``O(n)``
            補数を保存するハッシュ表に最大 *n* 要素入る

        Parameters
        ----------
        nums : List[int]
            The input array of integers.
        target : int
            The target sum to find.

        Returns
        -------
        List[int]
            A list containing the **two indices** whose elements sum to
            ``target``. The order of the two indices is arbitrary.

        Raises
        ------
        ValueError
            If no valid pair exists. (Per LeetCode constraints this
            should never happen.)

        Examples
        --------
        >>> Solution().twoSum([2, 7, 11, 15], 9)
        [0, 1]
        >>> Solution().twoSum([3, 3], 6)
        [0, 1]
        """
        lookup: Dict[int, int] = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i

        # According to the problem statement, this line is never reached.
        raise ValueError("No two sum solution found.")