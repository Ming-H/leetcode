#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        类似于检查两棵树是否一样
        """
        def isSym(L,R):
            if not L and not R: 
                return True
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) \
                        and isSym(L.right, R.left)
            return False
        return isSym(root, root)
    

