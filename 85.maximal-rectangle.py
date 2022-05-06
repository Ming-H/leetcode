#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # https://www.cnblogs.com/grandyang/p/4322667.html
        # 84题的扩展
        
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if \
                        row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):  # 注意加1
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans

