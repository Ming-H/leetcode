#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, isleft = False) -> int:
    #     if not root:
    #         return 0
    #     if not root.left and not root.right:
    #         if isleft:
    #             return root.val 
    #         else:
    #             return 0 
    #     return self.sumOfLeftLeaves(root.left, True) + \
    #         self.sumOfLeftLeaves(root.right, False )

    # def sumOfLeftLeaves2(self, root):
        res = 0
        def dfs(root):
            nonlocal res
            if root:
                if root.left and not root.left.left and not root.left.right:
                    res += root.left.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return res







