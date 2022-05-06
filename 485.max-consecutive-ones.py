#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maxCount = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 0
                
        return max(count, maxCount)
# @lc code=end

