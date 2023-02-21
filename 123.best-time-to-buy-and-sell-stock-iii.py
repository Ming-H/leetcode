#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        将整个操作过程当成4个人在操作，即一个做第一次买，
        一人做第一次卖，一人做第二次买，一人做第二次卖。
        买方的操作收益就是-price。第二次买卖需要依赖于
        第一次买卖的结果，这样可以保证两次买卖的一前一后顺序。
        """
        buy1 = float('-inf')
        buy2 = float('-inf')
        sell1 = 0
        sell2 = 0
        for item in prices:
            buy1 = max(buy1, -item)
            sell1 = max(sell1, buy1 + item)
            buy2 = max(buy2, sell1 - item)
            sell2 = max(sell2, buy2 + item)
        return sell2




