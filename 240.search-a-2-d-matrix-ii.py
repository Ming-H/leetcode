#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        O(m * logn)
        """
        if not matrix:
            return False
        depth = len(matrix)
        width = len(matrix[0])
        row, col = depth - 1, 0
        while row >= 0 and col < width:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False

        
# @lc code=end

