#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        时间复杂度：O(m*n) （m 和 n 分别为矩阵的行数和列数）
        空间复杂度：O(m*n) 
        """
        res = []                                #定义一个顺序列表
        while matrix:
            res += matrix.pop(0)                #每次去除矩阵最上面一行的数据，并添加到顺序列表中
            matrix = list(zip(*matrix))[::-1]   #紧接着逆时针90°旋转矩阵，重复前面的步骤直到矩阵为空
        return res
        
# @lc code=end

