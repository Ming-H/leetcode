#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))

    def dfs(self, root: TreeNode):
        """
        dp_node[0] =[rob the current node how much you gain] 
        dp_node[1] =[skip the current node how much you gain]
        """
        if not root:
            return (0, 0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (root.val + left[1] + right[1], 
                max(left[0], left[1]) + max(right[0], right[1]))





