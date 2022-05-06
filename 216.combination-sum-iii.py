#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = range(1, 10)
        self.dfs(nums, k, 0, [], res, n)
        return res
        
    def dfs(self, nums, k, index, path, res, target):
        # edge case
        if k < 0 or target < 0:
            return
        # when reaching the end
        if k == 0 and target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res, target-nums[i])


