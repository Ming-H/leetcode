#
# @lc app=leetcode id=553 lang=python3
#
# [553] Optimal Division
#

# @lc code=start
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = [str(item) for item in nums]
        if len(nums) <= 2:
            return '/'.join(nums)
        return '{}/({})'.format(nums[0], '/'.join(nums[1:]))
# @lc code=end

