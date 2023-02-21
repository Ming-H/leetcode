#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        1)If the current (sub)tree contains both p and q, 
          then the function result is their LCA. 
        2)If only one of them is in that subtree, 
          then the result is that one of them. 
        3)If neither are in that subtree, the result is null/None/nil.
        """
        if root in (None, p, q): 
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right 





        