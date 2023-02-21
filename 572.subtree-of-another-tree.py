#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p and q:
                return p.val == q.val and \
                    isSameTree(p.left, q.left) and \
                    isSameTree(p.right, q.right)
            return p is q #?是否为空

        if not root: 
            return False
        if isSameTree(root, subRoot): 
            return True
        return self.isSubtree(root.left, subRoot) \
            or self.isSubtree(root.right, subRoot)  



# @lc code=end

