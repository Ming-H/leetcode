#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    def bisearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left

    def searchRange(self, nums, target):
        left_index = self.bisearch(nums, target - 0.5)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        return [left_index, self.bisearch(nums, target + 0.5)-1]



        

        

