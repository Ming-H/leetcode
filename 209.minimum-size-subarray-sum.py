#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        先移动快指针，满足要求时，在移动慢指针
        """
        left = 0
        Sum = 0
        res = float('inf')
        for i in range(len(nums)):
            Sum += nums[i]
            while Sum >= s:
                res = min(res, i+1-left)
                Sum -= nums[left]
                left += 1
        return res if res!=float('inf') else 0  
        
   