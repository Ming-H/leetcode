#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    def searchRange(self, nums, target):
        def search_left(nums, target):
            left, right = 0, len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid]<target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left 
        def search_right(nums, target):
            left, right = 0, len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid] <= target:  # !!!!!!
                    left = mid + 1
                else:
                    right = mid - 1
            return right
                    
        left, right = search_left(nums, target), \
                                search_right(nums, target)
        return (left, right) if left<=right else [-1, -1]
        



            

            

