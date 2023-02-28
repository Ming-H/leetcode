#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = float('-inf')
        for item in nums:
            curSum = max(item, curSum + item)
            maxSum = max(maxSum, curSum)
        return maxSum


        

