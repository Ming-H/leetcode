#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        这道题目其实就是求从grid的左上角到右下角的所有路径中，最大值最小的路径中的最大值
        """
        m = len(grid)
        l, r = 2*m-2, m*m 
        
        def search(i,j):
            if ele[i][j]:
                return False
            ele[i][j] = 1
            if grid[i][j] <= ans:
                if i == j == m-1:
                    return True
                return any([search(a,b) for a, b in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] 
                                                     if 0 <= a < m and 0 <= b < m])
                               
        for ans in range(max(l,grid[-1][-1]), r):
            ele = [[0] * m for _ in range(m)]
            if search(0, 0):
                return ans
# @lc code=end

