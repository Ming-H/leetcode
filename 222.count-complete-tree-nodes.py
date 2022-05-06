#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth: # 左边是满二叉树，右边可能是完全二叉树
            return pow(2, leftDepth) + self.countNodes(root.right)
        else: # 左边是完全二叉树，右边可能是满二叉树
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
    

