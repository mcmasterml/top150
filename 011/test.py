import pytest
from solution import Solution


s = Solution()


def testCase01():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert s.maxArea(height) == 49
