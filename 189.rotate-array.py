#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Time complexity : O(n)
        Space complexity : O(1)
        """
        # def reverse(nums, start, end):
        #     while start<end:
        #         nums[start], nums[end] = nums[end], nums[start]
        #         start += 1
        #         end -= 1
        # k %= len(nums)
        # reverse(nums, 0, len(nums) - 1)
        # reverse(nums, 0, k - 1)
        # reverse(nums, k, len(nums) - 1)
        k %= len(nums)
        def reverse(subnums):
            i, j = 0, len(subnums)-1
            while i<j:
                subnums[i], subnums[j] = subnums[j], subnums[i]
                i += 1
                j -= 1
            return subnums

        nums = reverse(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])


        
