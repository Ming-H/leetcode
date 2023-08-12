#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0

        def count(node, target):
            if not node:
                return 0
            cnt = 1 if node.val == target else 0
            cnt += count(node.left, target - node.val)
            cnt += count(node.right, target - node.val)
            return cnt

        res = count(root, target)
        res += self.pathSum(root.left, target)
        res += self.pathSum(root.right, target)
        return res
