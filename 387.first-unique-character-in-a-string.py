#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        Time complexity : O(N) 
        Space complexity : O(N)
        """
        # build hash map : character and how often it appears
        
        count = {}
        for item in s:
            count[item] =  count[item]+1 if item in count else 1
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
        
# @lc code=end

