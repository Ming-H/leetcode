#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        # 找到根结点的位置，然后递归
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    def sortedArrayToBST2(self, nums):
        if not nums:
            return 
        return self.func(nums, 0, len(nums)-1)
    
    def func(self, nums, left, right):
        if left>right:
            return 
        mid = left + (right-left)//2
        root = TreeNode(nums[mid])
        root.left = self.func(nums, left, mid-1)
        root.right = self.func(nums, mid+1, right) 
        return root 
