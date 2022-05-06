#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, Sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == Sum:
            return True
        
        Sum -= root.val

        return self.hasPathSum(root.left, Sum) or \
                        self.hasPathSum(root.right, Sum)
 

 

