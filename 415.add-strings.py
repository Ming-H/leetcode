#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        t1 = 0
        for i in num1:
            t1 *= 10
            t1 += ord(i) - 48


        t2 = 0
        for i in num2:
            t2 *= 10
            t2 += ord(i) - 48

        return str(t1 + t2)

        
# @lc code=end

