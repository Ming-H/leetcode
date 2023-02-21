#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        def dfs(root, level, res):
            if not root:
                return 
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            for item in root.children:
                dfs(item, level+1, res)
        dfs(root, 0, res)
        return res 
    

# @lc code=end

