#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        Start with n = 1 and build up to the final n. 
        Store the previously computed values in a dp list.
        """
        dp = [None, 1]
        for m in range (2, n + 1):
            j = m - 1
            i = 1
            max_product = 0
            while i <= j:
                max_product = max(max_product,
                         max(i, dp[i]) * max(j, dp[j]))
                j -= 1
                i += 1
            dp.append(max_product)
        return dp[n]

        
# @lc code=end

