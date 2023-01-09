  #
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, num, target):
        """
        Time complexity : O(n)
        Space complexity : O(n)
        """
        d = {}
        for i, item in enumerate(num):
            if item not in d:
                d[target-item] = i
            else:
                return d[item], i
        return -1, -1



