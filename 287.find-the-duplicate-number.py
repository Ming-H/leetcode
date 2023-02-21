#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for item in nums:
            index = abs(item)-1
            if nums[index]<0:
                return abs(item)
            else:
                nums[index] *= -1




