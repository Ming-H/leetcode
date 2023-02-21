#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        参考 Top vote ans
        """
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            return helper(node.left, lower, val) and helper(node.right, val, upper)
        return helper(root)


    # def isValidBST2(self, root: TreeNode) -> bool:
    #     output =[]
    #     self.inorder(root, output)
    #     for i in range(1, len(output)):
    #         if output[i-1]>= output[i]:
    #             return False
    #     return True

    # def inorder(self, root, res):
    #     if not root:
    #         return True  
    #     self.inorder(root.left, res)
    #     res.append(root.val)
    #     self.inorder(root.right, res)

