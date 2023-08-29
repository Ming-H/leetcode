#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        !!!!!!!!!!!!!!!!!!!!!!!!
        """
        matrix, l = [], n*n+1
        while l > 1:
            l, r = l - len(matrix), l
            matrix = [range(l, r)] + list(zip(*matrix[::-1]))
        return matrix


# @lc code=end
