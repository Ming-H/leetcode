#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
class Solution:
    def uniquePathsWithObstacles(self, matrix: List[List[int]]) -> int:
        """
        Time Complexity: O(M×N)
        Space Complexity: O(1).
        """
        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0] == 1:
            return 0
        matrix[0][0] = 1
        for i in range(1, m):
            matrix[i][0] = int(matrix[i][0] == 0 and matrix[i-1][0] == 1)
        for j in range(1, n):
            matrix[0][j] = int(matrix[0][j] == 0 and matrix[0][j-1] == 1)
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
                else:
                    matrix[i][j] = 0
        return matrix[m-1][n-1]

        



