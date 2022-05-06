#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity: O(1)
        """
        # maxprofit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i-1]:
        #         maxprofit += prices[i] - prices[i-1]
        # return maxprofit 
        maxprofit = 0
        cur = float('inf')
        for item in prices:
            if item > cur:
                maxprofit += item - cur
            cur = item
        return maxprofit
        
       

