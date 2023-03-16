#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for col in range(n)] for row in range(m)]  
        if m == 1 or n == 1:
            return 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
        
   


