#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time complexity : O(n)
        Space complexity : O(n)
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for item in s:
            if item in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[item] != top_element:
                    return False
            else:
                stack.append(item)
        return not stack
        

