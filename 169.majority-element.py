#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
class Solution:
    def majorityElement(self, items: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        cnt = 0
        cur = None
        for item in items:
            if cnt == 0:
                cur = item
            cnt += (1 if item == cur else -1)
        return cur



