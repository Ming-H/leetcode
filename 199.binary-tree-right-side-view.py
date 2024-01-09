#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
    #     res = {}
    #     max_depth = -1
    #     stack = [(root, 0)]
    #     while stack:
    #         node, depth = stack.pop()
    #         if node:
    #             max_depth = max(max_depth, depth)
    #             res.setdefault(depth, node.val)
    #             stack.append((node.left, depth+1))
    #             stack.append((node.right, depth+1))
    #     return [res[depth] for depth in range(max_depth+1)]

    # def rightSideView2(self, root):
    #     res = []
    #     self.func(root, res, 0)
    #     return res 

    # def func(self, root, res, level):
    #     if not root:
    #         return 
    #     if level == len(res):
    #         res.append(root.val)
    #     self.func(root.right, res, level+1)
    #     self.func(root.left, res, level+1)

    # def rightSideView3(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, level = [], [root]
        while level:
            res.append([node.val for node in level][-1])
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [node for node in tmp if node]
        return res






    