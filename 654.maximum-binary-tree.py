#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None 
        maxIndex = nums.index(max(nums))
        root = TreeNode(nums[maxIndex])
        root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex+1:])
        return root 

    def constructMaximumBinaryTree2(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for item in nums:
            cur = TreeNode(item)
            while stack and stack[-1].val < cur.val:
                cur.left = stack.pop()
            if stack:
                stack[-1].right = cur 
            stack.append(cur)
        return stack[0]



# @lc code=end

