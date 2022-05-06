#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        https://www.cnblogs.com/grandyang/p/5727892.html
        """
        def binary_count(matrix, target):
            n = len(matrix)
            i, j = n-1, 0
            res = 0
            while i>=0 and j<n:
                if matrix[i][j]<=target:
                    res += i+1 
                    # 当前列的当前位置的上面所有的数字都小于目标值，
                    # 那么 cnt += i+1
                    j += 1
                else:
                    i -= 1
            return res   
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = int((l + r) // 2)
            res = binary_count(matrix, mid)
            if res < k:
                l = mid + 1
            else:
                r = mid
        return l

# @lc code=end

