#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1 or n >= len(s):
            return s
        L = ['']*n
        index, step = 0, 1
        for item in s:
            L[index] += item
            if index == 0:
                step = 1
            elif index == n-1:
                step = -1
            index += step
        return ''.join(L)
# @lc code=end
