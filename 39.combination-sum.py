#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target<0:
            return
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)






