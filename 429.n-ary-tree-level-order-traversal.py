#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        level, res = [root], []
        while level:
            res.append([node.val for node in level])
            tmp = []
            for node in level:
                for item in node.children:
                    tmp.append(item)
            level = [node for node in tmp]
        return res


# @lc code=end
