#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        dfs
        """
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1 
       

    def minDepth2(self, root):
        """
        bfs
        """
        if not root:
            return 0
        stack = [root]
        level = 1
        while stack:
            length = len(stack)
            for i in range(length):
                node = stack.pop(0)
                if not node.left and not node.right:
                    return level 
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            level += 1



