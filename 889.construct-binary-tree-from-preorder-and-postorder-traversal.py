#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        if len(preorder)==1:
            return root 

        for i in range(len(preorder)):
            if preorder[i]==postorder[-1]:
                root_index = i 
        root.right = self.constructFromPrePost(preorder[root_index:], postorder)
        root.left = self.constructFromPrePost(preorder[1:root_index], postorder)
        return root


# @lc code=end

