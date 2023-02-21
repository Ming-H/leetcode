#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res 
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
        
    def inorderTraversal2(self, root):
        res, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left 
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res 
        
        # res = []
        # cur = root
        # pre = TreeNode()
        # while cur:
        #     if not cur.left:
        #         res.append(cur.val)
        #         cur = cur.right
        #     else:
        #         pre = cur.left 
        #         while pre.right:
        #             pre = pre.right
        #         pre.right = cur
        #         tmp = cur 
        #         cur = cur.left 
        #         tmp.left = None
        # return res 
                
 




