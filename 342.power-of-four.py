#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # [231] Power of Two
        return n > 0 and not (n&(n-1)) and int(sqrt(n)) * int(sqrt(n)) == n

# @lc code=end

