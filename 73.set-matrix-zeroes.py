#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from operator import is_


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        1、行从0开始，如果第一列有元素是0，则列标签为True，列从1开始，如果元素
            是0，则行、列的头置为0
        2、行列均从1开始，如果行列开头为0，则该元素置为0
        3、如果第一个元素为0，则第一行为0
        4、如果列标签为True，第一列为0
        """
        is_col = False 
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if j==0:
                        is_col = True 
                    else:
                        matrix[0][j] = 0 
                        matrix[i][0] = 0 
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0 
        if matrix[0][0]==0:  #顺序不能变
            for j in range(n):
                matrix[0][j] = 0 
        if is_col:  #顺序不能变
            for i in range(m):
                matrix[i][0] = 0 


                


# @lc code=end

