#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        98. Validate Binary Search Tree.
        Keep track of the lo and hi bounds of each node, 
        when passed the leaf nodes, compute hi - lo to get the lowest difference along that path
        """
        def func(root, lower, upper):
            if not root:
                return upper - lower
            left = func(root.left, lower, root.val)
            right = func(root.right, root.val, upper)
            return min(left, right)
        return func(root, float('-inf'), float('inf'))



# @lc code=end

