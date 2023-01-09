#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        res = 0
        l, r = 0, len(nums)-1
        while l<=r:
            res = max(res, min(nums[l], nums[r])*(r-l))
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        return res 



