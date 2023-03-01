#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, nums: List[int]) -> int:
        res = len(nums) * [1]
        for i in range(1, len(nums)):  # from left to right
            if nums[i] > nums[i-1]:
                res[i] = res[i-1] + 1
        for i in range(len(nums)-1, 0, -1):  # from right to left
            if nums[i-1] > nums[i]:
                res[i-1] = max(res[i-1], res[i]+1)
        return sum(res)
            
# @lc code=end

