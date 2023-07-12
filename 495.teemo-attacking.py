#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, nums: List[int], duration: int) -> int:
        if not nums:
            return 0
        res = 0
        for i in range(1, len(nums)):
            res += min(nums[i] - nums[i - 1], duration)
        return res + duration


# @lc code=end
