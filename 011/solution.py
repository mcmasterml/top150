# 11. Container with Most Water

# You are given an integer array height of length n.
# There are n vertical lines drawn such that
# the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Exapmle 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # brute force soln.

        # position1 = -1
        # position2 = -1
        # maxArea = 0

        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         tall = min(height[i], height[j])
        #         area = (j - i) * tall
        #         if area > maxArea:
        #             position1 = i
        #             position2 = j
        #             maxArea = area
        # return maxArea

        # using left/right pointers moving inwards
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if area > maxArea:
                maxArea = area

        return maxArea


s = Solution()


def testCase01():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert s.maxArea(height) == 49


testCase01()
