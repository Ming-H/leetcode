#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True
        

