import pytest
from solution import Solution

s = Solution()


def test_case1():
    nums = [2, 2, 1, 1, 2, 2, 3, 3, 2, 1]
    assert s.majorityElement(nums) == 2
