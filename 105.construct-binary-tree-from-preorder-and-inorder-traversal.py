#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder or not preorder:
            return None
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root


    def build2(self, inorder, preorder):
        map_inorder = {}
        for i, item in enumerate(inorder): 
            map_inorder[item] = i
        def func(low, high):
            if low > high: 
                return None
            root = TreeNode(preorder.pop(0))
            mid = map_inorder[root.val]
            root.left = func(low, mid-1)
            root.right = func(mid+1, high)
            return root
        return func(0, len(inorder)-1)




