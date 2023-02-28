#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, s: str, p: str) -> int:
        if len(s) < len(p): # early termination
            return -1
        if not p:
            return 0
        
        i = j = 0
        while i<len(s) and j<len(p):
            if s[i] != p[j]:
                i = i - j + 1
                j = 0
            else:
                i += 1
                j += 1
        return i - j if j == len(p) else -1


# @lc code=end

