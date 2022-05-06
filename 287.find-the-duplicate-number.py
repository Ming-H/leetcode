#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # Find the intersection point of the two runners.
        # tortoise = nums[0]
        # hare = nums[0]
        # while True:
        #     tortoise = nums[tortoise]
        #     hare = nums[nums[hare]]
        #     if tortoise == hare:
        #         break
        
        # # Find the "entrance" to the cycle.
        # ptr1 = nums[0]
        # ptr2 = tortoise
        # while ptr1 != ptr2:
        #     ptr1 = nums[ptr1]
        #     ptr2 = nums[ptr2]
        
        # return ptr1
        for item in nums:
            index = abs(item)-1
            if nums[index]<0:
                return abs(item)
            else:
                nums[index] *= -1
        


