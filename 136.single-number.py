#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for item in nums:
            a ^= item
        return a
        
# @lc code=end

