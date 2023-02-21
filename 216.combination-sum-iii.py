#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = range(1, 10)
        self.dfs(nums, 0,  k, [], res, n)
        return res
        
    def dfs(self, nums, index, k, path, res, target):
        if k < 0 or target < 0:
            return
        if k == 0 and target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res, target-nums[i])



