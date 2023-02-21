#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        def firstOrder(root):
            nonlocal res 
            if not root:
                return ''
            res += str(root.val)
            if not root.left and not root.right:
                return 
            res += '('
            firstOrder(root.left)
            res += ')'
            if root.right:
                res += '('
                firstOrder(root.right)
                res += ')'

        firstOrder(root)
        return res 



# @lc code=end

