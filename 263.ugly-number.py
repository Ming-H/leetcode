#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num > 0:
            for i in range(2, 6):
                while num % i == 0:
                    num /= i
        return num == 1

# @lc code=end

