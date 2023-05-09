#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        https://www.cnblogs.com/slurm/p/5345985.html
        使用一个全局变量current_max，记录当前计算得出的最大路径。
        递归的思路：左子树中的最大路径和，右子树中的最大路径和，以
        及左子树中以root.left为起点的最大路径（需要大于零）+右子树
        中以root.right为起点的最大路径（需要大于零）+root.val），
        这三者中的最大值就是最大的路径和

        在递归函数中，如果当前结点不存在，直接返回0。否则就分别对其左右子
        节点调用递归函数，由于路径和有可能为负数，这里当然不希望加上负的
        路径和，所以和0相比，取较大的那个，就是要么不加，加就要加正数。
        然后来更新全局最大值结果 res，就是以左子结点为终点的最大 path 
        之和加上以右子结点为终点的最大 path 之和，还要加上当前结点值，
        这样就组成了一个条完整的路径。而返回值是取 left 和 right 中的
        较大值加上当前结点值，因为返回值的定义是以当前结点为终点的 path 
        之和，所以只能取 left 和 right 中较大的那个值，而不是两个都要
        """
        max_sum = float('-inf')
        def dfs(node):
            nonlocal max_sum 
            if not node:
                return 0
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)
            max_sum = max(max_sum, left_sum + right_sum + node.val)
            return max(left_sum, right_sum) + node.val
        dfs(root)
        return max_sum
        

    
       