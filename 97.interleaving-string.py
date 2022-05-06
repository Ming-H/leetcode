#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # r, c, l= len(s1), len(s2), len(s3)
        # if r+c != l:
        #     return False
        # dp = [True for _ in range(c+1)] 
        # for j in range(1, c+1):
        #     dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
            
        # for i in range(1, r+1):
        #     dp[0] = (dp[0] and s1[i-1] == s3[i-1])
        #     for j in range(1, c+1):
        #         dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or \
        #                         (dp[j-1] and s2[j-1] == s3[i-1+j])
        # return dp[-1]

        # https://blog.csdn.net/qq_34609108/article/details/80605343
            if len(s3)!=len(s1) + len(s2):
                return False
            dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
            for i in range(len(s1)+1):
                for j in range(len(s2)+1):
                    if i==0 and j==0:
                        dp[i][j] = True
                    elif i==0:
                        dp[i][j] = dp[i][j-1] and s2[j-1]==s3[i+j-1]
                    elif j==0:
                        dp[i][j] = dp[i-1][j] and s1[i-1]==s3[i+j-1]
                    else:
                        dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or \
                                            (dp[i][j-1] and s2[j-1]==s3[i+j-1]) 
            return dp[len(s1)][len(s2)]
    

