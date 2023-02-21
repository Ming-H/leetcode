#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        self.addLevel(ans, 0, root)
        return ans
        
    def addLevel(self, ans, level, root):
        if not root:
            return
        if len(ans) <= level:
            ans.append([])
        if not level%2:
            ans[level].append(root.val)
        else:
            ans[level].insert(0,root.val)
        self.addLevel(ans, level + 1, root.left)
        self.addLevel(ans, level + 1, root.right)
        

    # def zigzagLevelOrder2(self, root):
    #     res = []
    #     self.dfs(root, 0, res)
    #     for i in range(len(res)):
    #         if i%2!=0:
    #             res[i].reverse()
    #         else:
    #             continue
    #     return res 

    # def dfs(self, root, level, res):
    #     if not root:
    #         return 
    #     if len(res) < level+1:
    #         res.append([])
    #     res[level].append(root.val)
    #     self.dfs(root.left, level+1, res)
    #     self.dfs(root.right, level+1, res)


        


