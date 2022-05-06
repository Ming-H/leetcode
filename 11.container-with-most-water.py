#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        maxarea = 0
        l = 0
        r = len(height)-1
        while l<=r:
            maxarea = max(maxarea, min(height[l], height[r]) * (r-l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea


