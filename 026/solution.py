# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums = list(set(nums))
        return nums
