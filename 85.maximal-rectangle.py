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
        nums = [0] * (n+1)
        res = 0
        for row in matrix:
            for i in range(n):
                nums[i] = nums[i]+1 if row[i]=='1' else 0 
            stack = [-1]
            for i in range(n+1):
                while nums[i]< nums[stack[-1]]:
                    h = nums[stack.pop()]
                    w = i - stack[-1]-1
                    res = max(res, w*h)
                stack.append(i)
        return res 


