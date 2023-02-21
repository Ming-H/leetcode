#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, maxCnt = 0,0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                maxCnt = max(cnt, maxCnt)
                cnt = 0
        return max(cnt, maxCnt)



# @lc code=end

