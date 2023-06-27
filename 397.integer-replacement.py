#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        log(N)
        """
        def helper(n, count):
            if n == 1:
                return count
            if n % 2 == 0:
                return helper(n//2, count+1)
            else:
                return min(helper(n+1, count+1), helper(n-1, count+1))
        return helper(n, 0)


# @lc code=end
