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
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
# @lc code=end

