#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # maxlevel = 0
        # res = 0
        # def dfs(root, level):
        #     if not root:
        #         return None
        #     maxlevel = max(maxlevel, level)
        #     res = root.val 
        #     if root.left:
        #         level += 1
        #         if level > maxlevel:
        #             res = root.val 
        #         dfs(root.left, level)
        #     if root.right:
        #         level += 1
        #         dfs(root.right, level)
           
        # return res 
        """
        中，右，左
        """
        stack = [root]
        for node in stack:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return node.val

# @lc code=end

