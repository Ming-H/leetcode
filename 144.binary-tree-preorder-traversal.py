#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    # def preorderTraversal2(self, root: TreeNode) -> List[int]:
    #     res = []
    #     self.helper(root, res)
    #     return res 

    # def helper(self, root, res):
    #     if root:
    #         res.append(root.val)
    #         self.helper(root.left, res)
    #         self.helper(root.right, res)




    

