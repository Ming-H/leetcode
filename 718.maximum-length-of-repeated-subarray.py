#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, string1: List[int], string2: List[int]) -> int:
        """
        Time Complexity: O(M*N)O(M∗N)
        Space Complexity: O(M*N)O(M∗N)
        """
        m = len(string1)
        n = len(string2)
        #Initializing first row and column with 0 (for ease i intialized everthing 0 :p)
        dp = [[0 for x in range(n + 1)] for y in range(m + 1)]
        final = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if string1[i - 1] == string2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0
                final = max(final, dp[i][j])
        return final



# @lc code=end

