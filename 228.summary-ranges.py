#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        for item in nums:
            if not ranges or item > ranges[-1][-1] + 1:
                ranges.append([])
            ranges[-1][1:] = item,
        return ['->'.join(map(str, r)) for r in ranges]

        

