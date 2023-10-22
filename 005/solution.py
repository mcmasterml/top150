# 169. Majority Element

class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        # # Brute Force Soln
        # # O(n^2) time, O(n) space
        # n = len(nums)
        # for i in set(nums):
        #     count = 0
        #     for j in range(n):
        #         if nums[j] == i:
        #             count += 1
        #         if count > (n/2):
        #             return i

        # Boyer-Moore Voting Algorithm
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate
