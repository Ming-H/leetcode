#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # #计算最长公共子序列的动态规划
        # l1, l2 = len(word1), len(word2)
        # lcs = [[0] * (l1+1) for _ in range(l2+1)]
        # # print(lcs)
        # for i in range(1, l2+1):
        #     for j in range(1, l1+1):
        #         lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], 
        #             lcs[i-1][j-1]+(word2[i-1]==word1[j-1]))
        # return l1 + l2 - 2 * lcs[l2][l1]

        #不计算最长公共子序列的动态规划
        # l1, l2 = len(word1), len(word2)
        # dp = [[0 for i in range(l2+1)] for j in range(l1+1)]
        # for i in range(l1+1):
        #     for j in range(l2+1):
        #         if i==0 or j==0:
        #             dp[i][j] = i+j
        #         elif word1[i-1]==word2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        # return dp[l1][l2]

        # 只用到两行，第一行为dp，第二行为tmp
        l1, l2 = len(word1),len(word2)
        dp = [0 for i in range(l2+1)]
        for i in range(l1+1):
            tmp = [0 for i in range(l2+1)]
            for j in range(l2+1):
                if i==0 or j==0:
                    tmp[j] = i+j
                elif word1[i-1] == word2[j-1]:
                    tmp[j] = dp[j-1]
                else:
                    tmp[j] = min(tmp[j-1], dp[j]) + 1
            dp = tmp
        return dp[l2]









# @lc code=end

