# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i1, i2 = 0, 0
        # while (i1 - 1) <= (n + m):
        #     if nums1[i1] < nums2[i2]:
        #         i2 += 1
        #     else:
        #         # swap the items
        #         tmp = nums2[i2]
        #         nums2[i2] = nums1[i1]
        #         nums1[i1] = tmp
        #         i1 += 1

        # # attempt 2
        # i2 = 0
        # for i1 in range(m + n):
        #     if nums1[i1] < nums2[i2]:
        #         i2 += 1
        #     else:
        #         tmp = nums2[i2]
        #         nums2[i2] = nums1[i1]
        #         nums1[i1] = tmp
        #         i2 += 1

        # attempt 3
        # i1 = 0
        # i2 = 0
        # newl = []
        # for j in range(m + n):
        #     try:
        #         if nums1[i1] != 0:
        #             if nums1[i1] < nums2[i2]:
        #                 newl.append(nums1[i1])
        #                 i1 += 1
        #             else:
        #                 newl.append(nums2[i2])
        #                 i2 += 1
        #         else:
        #             newl.append(nums2[i2])
        #     except:
        #         newl.append(nums1[i1])
        # nums1 = newl

        # attempt 4
        A = m - 1
        B = n - 1
        C = m + n - 1

        while (A >= 0) and (B >= 0):
            if nums2[B] > nums1[A]:
                nums1[C] = nums2[B]
                C -= 1
                B -= 1
            else:
                nums1[C] = nums1[A]
                C -= 1
                A -= 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

s = Solution()
s.merge(nums1, 3, nums2, 3)
print(nums1)
