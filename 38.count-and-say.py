#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:
    def countAndSay(self, n: int) -> str:
        from itertools import groupby
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in groupby(s))
        return s
        

