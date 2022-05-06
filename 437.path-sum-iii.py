#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.helper(root, sum, [sum])

    def helper(self, node, origin, targets):
        if not node: 
            return 0
        cnt = 0
        for t in targets:
            if t==node.val: 
                cnt += 1                                         # count if sum == target
        targets = [t-node.val for t in targets]+[origin]         # update the targets
        return cnt+self.helper(node.left, origin, targets) \
                    +self.helper(node.right, origin, targets)

