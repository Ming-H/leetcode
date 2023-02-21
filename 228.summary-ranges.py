#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        for item in nums:
            if not res or item>res[-1][-1]+1:
                res.append([])
            res[-1][1:] = item,
        return ['->'.join(map(str, r)) for r in res]



