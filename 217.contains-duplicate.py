#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        d = {}
        for item in nums:
            if item not in d:
                d[item] = 1
            else:
                return True
        return False


