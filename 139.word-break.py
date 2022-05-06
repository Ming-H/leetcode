#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        https://www.cnblogs.com/grandyang/p/4257740.html
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i,len(s)):  # 可以从dp的角度想以len(s)作为结束点
                    if s[i:j+1] in wordDict:
                        dp[j+1] = True
        return dp[-1]
        
        # my code
        # d  = {}
        # for item in wordDict:
        #     if item not in d:
        #         d[item] = 1
        #     else:
        #         d[item] += 1
        
        # def dfs(s, d):
        #     if not s:
        #         return True
        #     for i in range(len(s)+1):
        #         if s[:i] in d:
        #             dfs(s[i:], d)
        #     return False

        # return dfs(s, d)
        
        


        