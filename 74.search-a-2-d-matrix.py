#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if m==0 or n==0:
            return 0
        left, right = 0, m*n
        while left < right:
            mid = (left + right) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            if matrix[mid // n][mid % n] < target:
                left = mid + 1
            else:
                right = mid
        return False     
                


# @lc code=end

