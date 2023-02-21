#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for item in s:
            d[item] = d.get(item, 0) + 1
        for i, item in enumerate(s):
            if d[item] == 1:
                return i 
        return -1 
        
# @lc code=end

