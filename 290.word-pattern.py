#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        同205 Isomorphic Strings
        """
        s = s.split()
        if len(s)!=len(pattern):
            return False 
        d = {}
        for a, b in zip(pattern, s):
            if a not in d:
                if b in d.values():
                    return False 
                d[a] = b 
            else:
                if d[a] != b:
                    return False 
        return True 
                


# @lc code=end

