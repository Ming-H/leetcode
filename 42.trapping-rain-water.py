#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not nums or len(nums)<3:
            return 0 
        res = 0
        left, right = 0, len(nums)-1
        l_max, r_max = nums[left], nums[right]
        while left <= right:
            if nums[left] < nums[right]:
                if nums[left] > l_max:
                    l_max = nums[left]
                else:
                    res += l_max - nums[left]
                left += 1
            else:
                if nums[right] > r_max:
                    r_max = nums[right]
                else:
                    res += r_max - nums[right]
                right -= 1
        return res 

        

