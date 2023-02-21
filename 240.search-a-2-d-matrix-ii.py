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
        O(n * logn)
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i>=0 and j<n:
            if matrix[i][j] ==target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False



        
# @lc code=end

