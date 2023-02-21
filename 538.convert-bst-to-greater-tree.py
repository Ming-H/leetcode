#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = 0
        def convert(root):
            nonlocal res 
            if not root:
                return 
            convert(root.right)
            root.val += res 
            res = root.val 
            convert(root.left)
        convert(root)
        return root 








# @lc code=end

