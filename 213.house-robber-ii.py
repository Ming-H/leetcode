#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from operator import not_


class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(nums):
            rob, not_rob = 0, 0
            for item in nums:
                rob, not_rob = not_rob+item, max(rob, not_rob)
            return max(rob, not_rob)
        if not nums:
            return 0
        elif len(nums)==1:
            return nums[0]
        else:
            return max(help(nums[1:]), help(nums[:-1]))


