#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
class Solution:
    def exist(self, matrix, word):
        if not matrix:
            return False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.dfs(matrix, i, j, word):
                    return True
        return False

    def dfs(self, matrix, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) \
                or matrix[i][j] != word[0]:
            return False
        tmp = matrix[i][j]
        matrix[i][j] = '#'
        res = self.dfs(matrix, i+1, j, word[1:]) or \
            self.dfs(matrix, i-1, j, word[1:]) or \
            self.dfs(matrix, i, j+1, word[1:]) or \
            self.dfs(matrix, i, j-1, word[1:])

        matrix[i][j] = tmp
        return res
