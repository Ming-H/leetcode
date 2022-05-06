#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.capitalize() \
                or word == word.lower() \
                or word == word.upper() 
# @lc code=end

