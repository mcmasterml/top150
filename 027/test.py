import pytest
from solution import Solution

s = Solution()


def test_case1():

    nums = [3, 2, 2, 3]
    val = 3
    assert s.removeElement(nums, val) == (2, [2, 2, None, None])
