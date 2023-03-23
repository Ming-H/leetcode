#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        if len(s) != len(t):
            return False
        d = {}
        for item in s:
            d[item] = d.get(item, 0) + 1
        for item in t:
            if item not in d or d[item] == 0:
                return False
            d[item] -= 1
        return True

 
# @lc code=end

