#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        # f1 = f2 = 0
        # for x in reversed(cost):
        #     f1, f2 = x + min(f1, f2), f1
        # return min(f1, f2)

        if not cost:
            return 0
        dp = [0] * len(cost)
        dp[0] = cost[0]
        if len(cost) >= 2:
            dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])



        
# @lc code=end

