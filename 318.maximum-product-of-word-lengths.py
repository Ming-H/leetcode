#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        Time Complexity : O(n*(N+n)), where n is the length of words 
        and N is the average length of words
        Space Complexity : O(n)
        """
        def check(chars1, chars2):
            for a, b in zip(chars1, chars2):
                if a and b:
                    return True
            return False
        chars, res = [[False]*26 for i in range(len(words))], 0
        for i, item in enumerate(words):
            for ch in item:
                chars[i][ord(ch)-ord('a')] = True
            for j in range(i):
                if not check(chars[i], chars[j]):
                    res = max(res, len(words[i])*len(words[j]))
        return res


# @lc code=end
