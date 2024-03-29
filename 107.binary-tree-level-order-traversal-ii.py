#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]: 
        # 参看102，插入位置不同而已
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.insert(0, [node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans

    def levelOrderBottom(self, root):
        res = []
        self.dfs(root, 0, res)
        return res[::-1]

    def dfs(self, root, level, res):
        if not root:
            return 
        if len(res) < level+1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)



    