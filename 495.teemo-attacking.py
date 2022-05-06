#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
        Time complexity : O(N)
        Space complexity : O(1)
        """
        n = len(timeSeries)
        if n == 0:
            return 0
        
        total = 0
        for i in range(n - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration

# @lc code=end

