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



    def isSymmetric(self, root):
        if not root:
            return True 
        def func(p, q):
            if not p and not q:
                return True 
            if not p or not q:
                return False
            if p.val == q.val:
                return func(p.left, q.right) and \
                    func(p.right, q.left)
            return False
        return func(root.left, root.right)


