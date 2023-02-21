#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
class Solution:
    def merge(self, nums):
        """
        Time complexity : O(nlogn)
        Space complexity : O(1) or O(n)
        """
        nums.sort(key=lambda x: x[0])
        res = []
        for item in nums:
            if not res or item[0] > res[-1][-1]:
                res.append(item)
            else:
                res[-1][-1] = max(res[-1][-1], item[1])
        return res 


    