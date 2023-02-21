#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
class Solution:
    def subsetsWithDup(self, nums):
        # res = [[]]
        # S.sort()
        # for i in range(len(S)):
        #     if i == 0 or S[i] != S[i - 1]:
        #         l = len(res)
        #     for j in range(len(res) - l, len(res)):
        #         res.append(res[j] + [S[i]])
        # return res
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        与 [39]Combination Sum 相似的解法
        """
        res = []
        nums.sort()
        def dfs(nums, index, res, path):
            if path not in res:
                res.append(path)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                dfs(nums, i + 1, res, path + [nums[i]])

        dfs(nums, 0, res, [])
        return res

        

