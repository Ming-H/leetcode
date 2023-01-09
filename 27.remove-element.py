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
        i = 0
        n = len(nums)-1
        while i<=n:
            if nums[i] == val:
                nums[i] = nums[n]
                n -= 1
            else:
                i += 1
        return i



    

