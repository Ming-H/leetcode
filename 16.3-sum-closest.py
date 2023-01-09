#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        no duplicate
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[l] + nums[r] + nums[i]
                if s == target:
                    return s 
                if abs(s-target) < abs(res-target):
                    res = s 
                if s < target:
                    l += 1
                else:
                    r -= 1
        return res 

