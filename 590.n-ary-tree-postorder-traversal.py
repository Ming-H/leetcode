#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root, res)
        return res 

    def dfs(self, root, res):
        if not root:
            return 
        for item in root.children:
            self.dfs(item, res)
        res.append(root.val)


    def postorder2(self, root):
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack += root.children
        return res[::-1]



    





# @lc code=end

