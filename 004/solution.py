# 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        i = 0  # Pointer to place next unique number or its second occurrence
        count = 1  # Count occurrences of the current number

        for j in range(1, len(nums)):
            if nums[j] == nums[j - 1]:
                count += 1
            else:
                count = 1  # Reset count for a new unique number

            if count <= 2:  # If the number has appeared 1 or 2 times
                i += 1
                nums[i] = nums[j]

        return i + 1
