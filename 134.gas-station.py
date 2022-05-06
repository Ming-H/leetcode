#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
        s, r = 0, 0
        for i in range(len(gas)):
            if gas[i] + r < cost[i]:
                s, r = i+1, 0
            else:
                r += gas[i]-cost[i]
        return s
# @lc code=end

