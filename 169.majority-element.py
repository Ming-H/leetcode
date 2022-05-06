#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        count = 0
        candidate = None
        for item in nums:
            if count == 0:
                candidate = item
            if item == candidate:
                count += 1
            else:
                count -= 1
        return candidate
