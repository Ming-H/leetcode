#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        rindex = {item: i for i, item in enumerate(s)}
        result = ''
        for i, item in enumerate(s):
            if item not in result:
                while item < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += item
        return result

# @lc code=end

