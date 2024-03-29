#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity: O(N * 2^n)
        Space complexity: O(2^n)
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path + [nums[i]], res)



    