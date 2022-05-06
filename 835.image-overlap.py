#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#

# @lc code=start
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """
        Time Complexity: O(N^4)
        Space Complexity: (N^2)
        """
        import numpy as np
        A = np.array(img1)
        B = np.array(img2)

        dim = len(A)
        # extend the matrix to a wider range for the later kernel extraction.
        B_padded = np.pad(B, dim-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(dim*2 - 1):
            for y_shift in range(dim* 2 - 1):
                # extract a kernel from the padded matrix
                kernel = B_padded[x_shift:x_shift+dim, y_shift:y_shift+dim]
                # convolution between A and kernel
                non_zeros = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zeros)

        return max_overlaps


# @lc code=end

