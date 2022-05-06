#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 
        locMin = locMax = gloMax = nums[0]
        for item in nums[1:]:
            tmp = locMin
            locMin = min(locMin*item, item, locMax*item) 
            locMax = max(tmp*item, item, locMax*item)
            gloMax = max(gloMax, locMax)
        return gloMax     



