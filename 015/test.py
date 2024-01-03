from solution import Solution
import pytest

s = Solution()


def testcase01():
    nums = [-1, 0, 1, 2, -1, -4]
    assert s.threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]
