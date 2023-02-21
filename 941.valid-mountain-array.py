#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False 
        l, r = 0, len(nums)-1
        while l+1<len(nums)-1 and nums[l] < nums[l+1]:
            l += 1
        while r-1>0 and nums[r]<nums[r-1]:
            r -= 1
        return l == r 




# @lc code=end

