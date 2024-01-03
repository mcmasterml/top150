# 15. 3Sum

# Given an integer array nums,
# return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # # brute force soln.
        # triplets = set()
        # nums.sort()

        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue

        #     for j in range(i + 1, len(nums)):
        #         if j > i + 1 and nums[j] == nums[j-1]:
        #             continue

        #         for k in range(j + 1, len(nums)):
        #             if k > j + 1 and nums[k] == nums[k-1]:
        #                 continue

        #             _sum = nums[i] + nums[j] + nums[k]
        #             if _sum == 0:
        #                 triplets.add((nums[i], nums[j], nums[k]))

        # return [list(triplet) for triplet in triplets]

        # using 2 pointers
        nums.sort()
        result = set()

        if len(nums) < 3:
            return []

        i = 0

        while nums[i] <= 0 and i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1

            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum == 0:
                    result.add(tuple(sorted((nums[i], nums[j], nums[k]))))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1

                elif _sum < 0:
                    j += 1

                else:
                    k -= 1

            while i <= len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1

            i += 1

        triplets = [list(triplet) for triplet in result]

        return triplets
