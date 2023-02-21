#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0 #到达的最远的位置
        for i, item in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+item)
        return True


# @lc code=end

