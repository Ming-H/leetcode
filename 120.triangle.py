#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        原文链接：https://blog.csdn.net/u010429424/article/details/69948372
        """
        rows = len(triangle)
        for i in range(1, rows):
            cols = len(triangle[i])
            for j in range(0, cols):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == cols - 1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], \
                                                triangle[i-1][j])
        return min(triangle[rows-1])

# @lc code=end

