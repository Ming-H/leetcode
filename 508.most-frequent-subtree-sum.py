#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        """
        后序遍历
        Time complexity: O(N)
        Space complexity: O(N)
        """
        d = {}
        Max = 0
        def func(root):
            nonlocal d, Max
            if not root:
                return 0
            left = func(root.left)
            right = func(root.right)
            cur = root.val + left + right
            d[cur] = d.get(cur, 0) + 1
            Max = max(Max, d[cur])
            return cur
            
        func(root)
        res = []
        for key in d:
            if d[key]==Max:
                res.append(key)
        return res





# @lc code=end

