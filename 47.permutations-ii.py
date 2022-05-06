#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

        
    def dfs(self, nums, path, res):
        if len(nums)==0:
            res.append(list(path))
        pre = None
        for i in range(len(nums)):
            if nums[i]==pre:
                continue
            path.append(nums[i])
            self.dfs(nums[:i]+nums[i+1:], nums[i], path, res)
            path.pop()
            pre = nums[i]
    
