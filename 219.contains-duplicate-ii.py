#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # dict = {}
        # for i, v in enumerate(nums):
        #     if v in dict and i-dict[v] <= k:
        #         return True
        #     dict[v] = i
        # return False
        n=len(nums)
        if n==len(set(nums)):
            return False
        for i in range(n):
            for j in range(1,k+1):
                if i+j>=n:
                    break
                if nums[i+j]==nums[i]:
                    return True
        return False
