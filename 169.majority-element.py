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
        cur, cnt = None, 0
        for item in nums:
            if cnt == 0:
                cur = item 
            if cur == item:
                cnt += 1
            else:
                cnt -= 1
        return cur




