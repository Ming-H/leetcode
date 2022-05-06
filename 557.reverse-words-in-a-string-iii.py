#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        两次反转
        """
        return ' '.join(s.split()[::-1])[::-1]
# @lc code=end

