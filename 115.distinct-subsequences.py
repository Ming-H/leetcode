#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        dp method
        https://blog.csdn.net/XX_123_1_RJ/article/details/80789223
        dp[i][j] = dp[i][j-1] + dp[i-1][i-j] * (T[i] == S[j])
        """
        m, n = len(s)+1, len(t)+1
        dp = [[1] * n for _ in range(m)]
        for j in range(1, n):
            dp[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1])
        return dp[-1][-1]
        
        # O(n) space  
        # l1, l2 = len(s)+1, len(t)+1
        # cur = [0] * l2
        # cur[0] = 1
        # for i in range(1, l1):
        #     pre = cur[:]
        #     for j in range(1, l2):
        #         cur[j] = pre[j] + pre[j-1]*(s[i-1] == t[j-1])
        # return cur[-1]

