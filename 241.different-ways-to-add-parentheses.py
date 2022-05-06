#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        m = {}
        return self.dfs(input, m)
        
    def dfs(self, input, m):
        if input in m:
            return m[input]
        if input.isdigit():
            m[input] = int(input)
            return [int(input)]
        ret = []
        for i, c in enumerate(input):
            if c in "+-*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                ret.extend(eval(str(x)+c+str(y)) for x in l for y in r)
        m[input] = ret
        return ret


        
# @lc code=end

