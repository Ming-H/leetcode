#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def findMode(self, root):
        pre, max_cnt, cur = None, 0, 0
        res = []
        def dfs(node):
            nonlocal pre, max_cnt, cur, res 
            if not node:
                return None 
            dfs(node.left)
            if node.val!=pre:
                cur = 1
            else:
                cur += 1
            if cur == max_cnt:
                res.append(node.val)
            elif cur > max_cnt:
                res = [node.val]
                max_cnt = cur 
            pre = node.val
            dfs(node.right)
        dfs(root)
        return res 






# @lc code=end

