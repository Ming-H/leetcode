#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, nums: List[str]) -> int:
        stack = []
        ops = ('/', '+', '*', '-')
        for item in nums:
            if item not in ops:
                stack.append(item)
            else:
                b, a = map(int, (stack.pop(), stack.pop()))
                if item =='+':
                    stack.append(a+b)
                elif item == '-':
                    stack.append(a-b)
                elif item == '*':
                    stack.append(a*b)
                else:
                    stack.append(a/b)
        return int(stack[0])

# @lc code=end

