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
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum = curr_sum * 10 + node.val
            if not node.left and not node.right:
                return curr_sum
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        return dfs(root, 0)

            

