# 27. Remove Element

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        # k = 0
        # # change all `val` to `None`
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         nums[i] = None

        #         # move these `None` values to the end of the array, if they are None
        #         j = i
        #         while j < (len(nums) - 1):
        #             tmp = nums[j]
        #             j += 1
        #             nums[j-1] = nums[j]
        #             nums[j] = tmp

        #     # increment k
        #     if nums[i] != None:
        #         k += 1

        # return (k, nums)

        # attempt 2:

        i = 0
        j = len(nums) - 1

        while i <= j:
            while nums[j] == val:
                j -= 1
            if nums[i] == val:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1
            else:
                i += 1

        k = i
        return k


nums = [3, 2, 2, 3]

val = 3

s = Solution()
print(s.removeElement(nums, val))
