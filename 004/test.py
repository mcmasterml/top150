import pytest
from solution import Solution

s = Solution()


def test_case1():
    nums = [1, 1, 1, 2, 2, 3]

    assert s.removeDuplicates(nums) == 5
    assert nums[:5] == [1, 1, 2, 2, 3]
