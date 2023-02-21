#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        字节
        """
        res = 0
        def func(root):
            nonlocal res 
            if not root:
                return  0 
            left = func(root.left)
            right =func(root.right)
            res = max(res, left + right)
            return max(left, right) + 1
        func(root)
        return res 








# @lc code=end

