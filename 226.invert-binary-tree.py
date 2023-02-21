#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

    def invertTree2(self, root):
        """
        先序遍历
        """
        if not root:
            return None
        queue = [root]
        while queue:
            current = queue.pop(0)
            current.left, current.right = current.right, current.left
            if current.left :
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root


            




