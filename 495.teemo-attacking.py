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
        for i in range(len(nums)-1):
            res += min(nums[i+1]-nums[i], duration)
        return res + duration 




# @lc code=end

