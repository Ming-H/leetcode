#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n 
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a+b 
        return b
        
# @lc code=end

