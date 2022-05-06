#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for token in path.split('/'):
            if token in ('', '.'):
                pass
            elif token == '..':
                if stack: 
                    stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)

            

