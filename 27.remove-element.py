#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        l, r = 0, len(nums)-1
        while l<=r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return l 



    

