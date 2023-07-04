#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
import collections


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d = collections.Counter(c+d for c in C for d in D)
        return sum(d[-a-b] for a in A for b in B)


# @lc code=end
