#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from sympy import N


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:   
        """
        Time complexity : O(N)
        Space complexity : O(1)
        """
        n = len(nums)
        res = [1] * n 
        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]
        R = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= R
            R *= nums[i]
        return res


        




