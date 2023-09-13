#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        Time complexity : O(n)
        Space complexity: O(1)
        """
        maxprofit = 0
        cur = float('inf')
        for item in prices:
            if item > cur:
                maxprofit += item - cur
            cur = item
        return maxprofit
