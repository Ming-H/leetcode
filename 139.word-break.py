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
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]
        

        
        


        