#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time Complexity: O(R*C)
        Space complexity: O(R*C)
        """
        res = 0
        m, n = len(grid), len(grid[0])
        def func(i, j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0:
                return 0 
            grid[i][j] = 0
            return 1 + func(i-1, j) + func(i, j-1) + func(i+1, j) + func(i, j+1)
        for i, j in product(range(m), range(n)):
            if grid[i][j]:
                res = max(res, func(i, j))
        return res 



# @lc code=end

