#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))


