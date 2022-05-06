#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for item in nums:
            index = abs(item)-1
            if nums[index]<0:
                res.append(abs(item))
            else:
                nums[index] *= -1
        return res
