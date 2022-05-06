#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Time Complexity: O(M*N)
        Space Complexity: O(1)
        """
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))

        # m, n = len(matrix), len(matrix[0])
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if matrix[i-1][j-1] != matrix[i][j]:
        #             return False 
        # return True






# @lc code=end

