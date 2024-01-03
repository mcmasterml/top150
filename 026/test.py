import pytest
from solution import Solution

s = Solution()


def test_case1():
    nums = [1, 1, 2]

    assert s.removeDuplicates(nums) == [1, 2]


def test_case2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    assert s.removeDuplicates(nums) == [0, 1, 2, 3, 4]
