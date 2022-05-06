#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        DFS method
        """
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
        

