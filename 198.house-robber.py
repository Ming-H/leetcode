#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for item in nums:
            last, now = now, max(last + item, now)
        return now

