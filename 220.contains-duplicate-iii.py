#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n=len(nums)
        if t==0 and n==len(set(nums)):
            return False
        for i in range(n):
            for j in range(1, k+1):
                if i+j>=n:
                    break
                if abs(nums[i+j]-nums[i])<=t:
                    return True
        return False


                
        