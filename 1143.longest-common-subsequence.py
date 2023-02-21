#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        # 做了 padding 处理，使得包含空串的情况（自含了边界情况）
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]




# @lc code=end

