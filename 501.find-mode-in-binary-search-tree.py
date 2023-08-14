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
        pre, max_cnt, cnt = None, 0, 0
        res = []

        def inorder(node):
            nonlocal pre, max_cnt, cnt, res
            if not node:
                return None
            inorder(node.left)
            if node.val != pre:
                cnt = 1
                pre = node.val
            else:
                cnt += 1
            if cnt == max_cnt:
                res.append(node.val)
            elif cnt > max_cnt:
                res = [node.val]
                max_cnt = cnt
            inorder(node.right)
        inorder(root)
        return res


# @lc code=end
