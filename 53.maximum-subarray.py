#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

        

