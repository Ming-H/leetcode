#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        inorder traverse
        """
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    # def kthSmallest2(self, root, k):
    #     count = []
    #     self.helper(root, count)
    #     return count[k-1]

    # def helper(self, node, count):
    #     if not node:
    #         return
    #     self.helper(node.left, count)
    #     count.append(node.val)
    #     self.helper(node.right, count)

    # def kthSmallest3(self, root, k):
    #     """
    #     binary search
    #     """
    #     n = self.countNodes(root.left)
    #     if k <= n:
    #         return self.kthSmallest3(root.left, k)
    #     elif k > n+1:
    #         # 1 is counted as current node
    #         return self.kthSmallest3(root.right, k-1-n)
    #     return root.val
    # def countNodes(self, root):
    #     if not root:
    #         return 0
    #     return 1 + self.countNodes(root.left) \
    #         + self.countNodes(root.right)
