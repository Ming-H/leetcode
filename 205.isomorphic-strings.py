#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for a, b in zip(s, t):
            if a not in d:
                if b in d.values():
                    return False 
                d[a] = b 
            else:
                if d[a] != b:
                    return False 
        return True 


        
# @lc code=end

