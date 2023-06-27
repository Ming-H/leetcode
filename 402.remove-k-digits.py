#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        ## 1234, k= 2 => when numbers are in increasing order we need to delete last digits 
        ## 4321 , k = 2 ==> when numbers are in decreasing order, we need to delete first digits
        ## so, we need to preserve increasing sequence and remove decreasing sequence ##
                ## LOGIC ##
                #	1. First think in terms of stack
                #	2. push num into stack IF num it is greater than top of stack
                #	3. ELSE pop all elements less than num
        ## TIME COMPLEXICITY : O(N) 
        ## SPACE COMPLEXICITY : O(N) 
        """
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        while k > 0:
            stack.pop()
            k -= 1
        return ''.join(stack).lstrip('0') or '0'

# @lc code=end
