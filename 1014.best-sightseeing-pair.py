#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        O(n) Time, O(1) Space
        """
        K = values[0]
        best = float('-inf')
        for j in range(1, len(values)):
            x    = values[j]
            best = max(best, K + x - j )
            K    = max(K   , x + j     )
        return best
# @lc code=end

