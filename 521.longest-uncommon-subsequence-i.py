#
# @lc app=leetcode id=521 lang=python3
#
# [521] Longest Uncommon Subsequence I 
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """
        Time complexity : O(min(x,y))
        Space complexity : O(1)
        """
        if a==b:
            return -1
        return max(len(a), len(b))

# @lc code=end

