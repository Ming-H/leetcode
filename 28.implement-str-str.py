#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, s: str, p: str) -> int:
        if len(s) < len(p): # early termination
            return -1
        if not p:
            return 0
        
        i = j = 0
        while j < len(p) and i < len(s): 
            if s[i] != p[j]:
                i = i - j + 1
                j = 0
                continue 
            i += 1
            j += 1
        return i - j if j == len(p) else -1



        
