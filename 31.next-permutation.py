#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time complexity : O(n)O(n). In worst case, only two scans of the whole array are needed.
        # Space complexity : O(1)O(1). No extra space is used. In place replacements are done.
        i = len(nums) - 2
        while i>=0 and nums[i]>=nums[i+1]:
                i -= 1
        if i>=0:
            j = len(nums)-1
            while j>=0 and nums[j]<=nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        l, r = i+1, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


