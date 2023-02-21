#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        buy = [-prices[0]] + [float('-inf') for _ in range(k)]
        sell = [0] + [float('-inf') for _ in range(k)]
        for i in range(1, n):
            buy[0] = max(buy[0], sell[0] - prices[i])
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j] - prices[i])
                sell[j] = max(sell[j], buy[j - 1] + prices[i]); 
        return max(sell)
# @lc code=end

