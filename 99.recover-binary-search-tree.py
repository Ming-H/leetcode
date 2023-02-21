#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        The first element is always larger than its next one ，
        while the second element is always smaller than its previous one.
        BST使用中序遍历成为有序数组
        """
        first = None 
        second = None 
        pre = TreeNode(float('-inf'))
        def func(root):
            nonlocal  first, second, pre
            if not root:
                return 
            func(root.left)
            if not first and pre.val>=root.val:
                first = pre
            if first and pre.val>=root.val:
                second = root 
            pre = root 
            func(root.right)
        func(root)
        first.val, second.val = second.val, first.val



 








