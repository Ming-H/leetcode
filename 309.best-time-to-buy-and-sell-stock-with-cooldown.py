#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, cooldown = float('-inf'), 0, 0
        for item in prices:
            buy = max(buy, cooldown-item)
            cooldown = max(cooldown, sell)
            sell = max(sell, buy + item)
        return sell
        



# @lc code=end

