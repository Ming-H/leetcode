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
    def pathSum(self, root: TreeNode, target: int) -> int:
        def func(root, origin, targets):
            if not root:
                return 0
            cnt = 0
            for item in targets:
                if item == root.val:
                    cnt += 1
            targets = [origin] + [item-root.val for item in targets]
            return cnt + func(root.left, origin, targets) + \
                func(root.right, origin, targets)
        return func(root, target, [target])
