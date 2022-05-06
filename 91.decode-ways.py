#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
class Solution:
    """
    https://www.jianshu.com/p/6eed356b6627
    """
    def numDecodings(self, s: str) -> int:
        """
        v tells the previous number of ways
        w tells the number of ways
        p is the previous digit
        d is the current digit
        """
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        return w


