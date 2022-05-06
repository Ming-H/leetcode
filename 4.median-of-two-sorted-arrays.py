#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        Time complexity: O(log(min(m,n))).
        Space complexity: O(1)
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax = 0, m # 对i进行二分查找，找到m的位置，n的位置根据中位数计算
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0: 
                    max_of_left = B[j-1]
                elif j == 0: 
                    max_of_left = A[i-1]
                else: 
                    max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: 
                    min_of_right = B[j]
                elif j == n: 
                    min_of_right = A[i]
                else: 
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

