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
        alpha = [0] * 26
        for c in s:
            alpha[ord(c) - 97] += 1
        for c in t:
            alpha[ord(c) - 97] -= 1
            if alpha[ord(c) - 97] < 0:
                return False
        return True




 
# @lc code=end

