#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
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
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root, res)
        return res 

    def dfs(self, root, res):
        if not root:
            return 
        res.append(root.val)
        for item in root.children:
            self.dfs(item, res)

    def preorder2(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            stack.extend(tmp.children[::-1])
        return res 


# @lc code=end

