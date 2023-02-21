#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        if m<0 or n<0:
            return res
        res_matrix = [[0 for i in range(n+1)] for j in range(m+1)]
        res_matrix[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                res_matrix[i][j] += res_matrix[i-1][j]+ \
                                    res_matrix[i][j-1]
        return res_matrix[-1][-1]

        
   


