#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, level = [],  [root]
        flag = 0
        while level:
            if flag % 2 == 0:
                res.append([node.val for node in level])
            else:
                res.append([node.val for node in level][::-1])
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [node for node in tmp if node]
            flag += 1
        return res
