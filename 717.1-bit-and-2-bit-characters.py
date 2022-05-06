#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
# @lc code=end

