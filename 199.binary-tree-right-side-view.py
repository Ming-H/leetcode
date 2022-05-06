#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = {}
        max_depth = -1
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                res.setdefault(depth, node.val)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return [res[depth] for depth in range(max_depth+1)]

    