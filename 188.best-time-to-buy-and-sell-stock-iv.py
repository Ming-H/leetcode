#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        if k >= len(prices):
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res
        else:
            g = [0] * (k+1)
            l = [0] * (k+1)
            for i in range(len(prices)-1):
                diff = prices[i+1]-prices[i]
                for j in range(k, 0, -1):
                    l[j] = max(g[j-1]+max(diff, 0), l[j]+diff)
                    g[j] = max(l[j], g[j])
            return g[k]
# @lc code=end

