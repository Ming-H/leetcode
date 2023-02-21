#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, val):
            nonlocal res
            if root:
                dfs(root.left, val*10+root.val)
                dfs(root.right, val*10+root.val)
                if not root.left and not root.right:
                    res += val*10 + root.val
        dfs(root, 0)
        return res


            

