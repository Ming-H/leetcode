#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        rindex = {item:i for i, item in enumerate(s)}
        res = ''
        for i, item in enumerate(s):
            if item not in res:
                while item<res[-1:] and i<rindex[res[-1:]]:
                    res = res[:-1] 
                res += item 
        return res 



# @lc code=end

