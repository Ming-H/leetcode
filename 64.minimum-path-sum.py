#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
class Solution:
    def minPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for j in range(1, n):
            matrix[0][j] += matrix[0][j-1]
        for i in range(1, m):
            matrix[i][0] += matrix[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
        return matrix[-1][-1]

            

