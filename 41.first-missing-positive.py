#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
class Solution:
    def firstMissingPositive(self, nums):
        """
        不能用额外空间，那就只有利用数组本身，跟Counting sort一样，
        利用数组的index来作为数字本身的索引，把正数按照递增顺序依次放到数组中。
        即让A[0]=1, A[1]=2, A[2]=3, ... , 这样一来，最后如果哪个数组元素
        违反了A[i]=i+1即说明i+1就是我们要求的第一个缺失的正数。
        """
        for i in range(len(nums)):
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

 

        

