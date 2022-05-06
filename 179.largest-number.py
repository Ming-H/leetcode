#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
class Solution:
    """
    Input: [3,30,34,5,9]
    Output: "9534330"
    """
    # bubble sort
    def largestNumber(self, nums):
        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(map(str, nums))))

