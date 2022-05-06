#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:   
        """
        Time complexity : O(N)
        Space complexity : O(1)
        """
        length = len(nums)
        res = [1]*length
        for i in range(1, length):
            res[i] = nums[i - 1] * res[i - 1]
        R = 1
        for i in reversed(range(length)):
            res[i] *= R
            R *= nums[i]
        return res



