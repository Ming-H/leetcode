#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        level = [root]
        while level:
            res.append(sum(item.val for item in level) / len([item.val for item in level]))
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [node for node in tmp if node]
        return res 


# @lc code=end

