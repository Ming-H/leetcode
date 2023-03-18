#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.dfs(root, sum, [], res)
        return res
    
    def dfs(self, root, sum, ls, res):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        self.dfs(root.left, sum-root.val, ls+[root.val], res)
        self.dfs(root.right, sum-root.val, ls+[root.val], res)
            



