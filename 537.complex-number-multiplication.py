#
# @lc app=leetcode id=537 lang=python3
#
# [537] Complex Number Multiplication
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a1,a2=map(int,a[:-1].split('+'))
        b1,b2=map(int,b[:-1].split('+'))
        return '%d+%di'%(a1*b1-a2*b2,a2*b1+b2*a1)
# @lc code=end

