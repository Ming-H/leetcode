#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
class Solution:
    # DP 
    def numTrees(self, n: int) -> int:
        # https://www.cnblogs.com/grandyang/p/4299608.html
        # https://www.jianshu.com/p/c3dd041d3e21
        """
        本题可以采用动态规划的方法来解决。具体公式[F(i, n) = G(i-1) * G(n-i)]。
        给定一个序列1.....n, 来构造一个BST, 我们可以枚举系列中的每个数字i, 然后使
        用i作为根节点，很自然的，子序列1....(i-1)可以构成i的左子树，而(i+1)....n
        可以构成i的右子树，而且左子树和右子树叶都是BST.通过上面的方法，我们可以确保
        所构造的BST都是不同的，因为根节点是不同的。
        """
        res = [0] * (n+1)
        res[0] = 1
        res[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]
        

