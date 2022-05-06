#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        if(n <= 0):
            return False
        return((math.log(n) / math.log(4)).is_integer())
        
# @lc code=end

