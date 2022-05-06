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
        self.dfs(nums, 0, res, [])
        return res
        
    def dfs(self, nums, index, res, path):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            # 这里i+1，不会重复使用
            self.dfs(nums, i + 1, res, path + [nums[i]])

# ————————————————
# 版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/79785548
