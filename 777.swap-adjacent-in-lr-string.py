#
# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        L, R = 0, 0
        for s, e in zip(start, end):
            L += (e == 'L') - (s == 'L')
            R += (s == 'R') - (e == 'R')

            if L < 0 or L > 0 and s == 'R' or R < 0 or R > 0 and s == 'L':
                return False

        return not R and not L
# @lc code=end

