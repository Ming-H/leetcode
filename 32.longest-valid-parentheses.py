#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Time complexity : O(n). 
        Space complexity : O(1).
        """
        # ans = 0
        # stack = [-1]
        # for i in range(len(s)):
        #     if s[i]=='(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if len(stack)==0:
        #             stack.append(i)
        #         else:
        #             ans = max(ans, i-stack[-1])
        # return ans

        left, right = 0, 0
        maxlen = 0
        for  item in s:
            if item == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, 2*right)
            elif right>left:
                left = 0
                right = 0

        left, right = 0, 0
        for item in s[::-1]:
            if item == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, 2*left)
            elif left>right:
                left = 0
                right = 0
        return maxlen    
        
        # def maxlong(s, flag):
        #     maxlen = 0
        #     left , right = 0, 0
        #     if flag == 'right':
        #         s = s[::-1]
        #     for item in s:
        #         if item == '(':
        #             left += 1
        #         else:
        #             right += 1
        #         if left == right:
        #             if flag=='left':
        #                 maxlen = max(maxlen, right * 2)
        #             else:
        #                 maxlen = max(maxlen, left * 2)
        #         elif flag == 'left' and right>left:
        #             left, right = 0, 0
        #         elif flag == 'right' and left>right:
        #             left, right = 0, 0
        #     return maxlen
    
        # return max(maxlong(s, 'left'), maxlong(s, 'right'))

