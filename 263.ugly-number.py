#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num>0:
            for p in 2, 3, 5:
                while num%p == 0:
                    num /= p
        return num==1
        
# @lc code=end

