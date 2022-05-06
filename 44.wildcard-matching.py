#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
class Solution:
    # def isMatch(self, s: str, p: str) -> bool:
    #     length = len(s)
    #     if len(p) - p.count('*') > length:
    #         return False
    #     dp = [True] + [False]*length
    #     for i in p:
    #         if i != '*':
    #             for n in reversed(range(length)):
    #                 dp[n+1] = dp[n] and (i == s[n] or i == '?')
    #         else:
    #             for n in range(1, length+1):
    #                 dp[n] = dp[n-1] or dp[n]
    #         dp[0] = dp[0] and i == '*'
    #     return dp[-1]
    def isMatch(self, s, p):
        if s=="" and (p=="" or p.count('*')==len(p)):
            return True
        elif s=="" or p=="":
            return False

        dp=[[False for i in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0]=True

        for i in range(len(s)+1):
            for j in range(len(p)+1):
                if i>0 and j>0:
                    if s[i-1]==p[j-1] or p[j-1]=='?' or p[j-1]=='*':
                        dp[i][j]=dp[i-1][j-1]
                    if p[j-1]=='*':
                        dp[i][j]=dp[i-1][j]
                if j>0 and p[j-1]=="*":
                    dp[i][j]= dp[i][j] or dp[i][j-1]

        return dp[-1][-1]

