#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:
    """
    Time complexity : O(1) time per query, O(mn) time pre-computation. 
    Space complexity : O(mn).
    """

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        if m==0 or n==0:
            return 
        self.dp = [[0 for j in range(n+1)] for i in range(m+1) ]
        for i in range(m):
            for j in range(n):
                self.dp[i+1][j+1] = self.dp[i+1][j] + \
                                    self.dp[i][j+1] + \
                                    matrix[i][j] - \
                                    self.dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] \
            - self.dp[row2+1][col1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

