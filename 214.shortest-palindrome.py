#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # if not s:
        #     return ""
        # n = len(s)
        # for i in range(n, 0, -1):
        #     if s[:i] == s[:i][::-1]:
        #         return s[i:][::-1] + s
        # return s[::-1] + s
        i, n = 0, len(s)
        for j in range(n-1, -1, -1):
            if s[j]==s[i]:
                i += 1
        if i==n:
            return s 
        return s[i:][::-1] + self.shortestPalindrome(s[:i]) + s[i:]

