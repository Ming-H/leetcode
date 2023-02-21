#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root 
            return node 
        def dfs(root, val, level, depth):
            if not root:
                return 
            if level == depth-1:
                left = root.left 
                root.left = TreeNode(val)
                root.left.left = left 
                right = root.right
                root.right = TreeNode(val)
                root.right.right = right 
            else:
                dfs(root.left, val, level+1, depth)
                dfs(root.right, val, level+1, depth)
        dfs(root, val, 1, depth)
        return root 


# @lc code=end

