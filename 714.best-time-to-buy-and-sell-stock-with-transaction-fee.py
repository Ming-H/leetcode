#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        sell, buy = 0, float('-inf')
        for i in range(len(prices)):
            sell = max(sell, buy + prices[i] - fee)
            buy = max(buy, sell - prices[i])
        return sell




        
# @lc code=end

