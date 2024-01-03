import pytest
from solution import Solution

s = Solution()


def test_case1():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3

    s.merge(nums1, m, nums2, n)

    assert nums1 == [1, 2, 2, 3, 5, 6]
