#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
class Solution:
    def isMatch(self, text, pattern):
        """
        .表示任何单字符，*表示任意数量的后面的字符
        time: O(TP)
        space: O(TP)
        """
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
