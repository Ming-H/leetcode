#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, matrix: List[List[int]]) -> int:
        """
        原文链接：https://blog.csdn.net/u010429424/article/details/69948372
        """
        m = len(matrix)
        for i in range(1, m):
            n = len(matrix[i])
            for j in range(n):
                if j==0:
                    matrix[i][j] += matrix[i-1][j]
                elif j==n-1:
                    matrix[i][j] += matrix[i-1][j-1]
                else:
                    matrix[i][j] += min(matrix[i-1][j-1],\
                        matrix[i-1][j])
        return min(matrix[-1])


# @lc code=end

