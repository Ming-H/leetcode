#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        """
        Time complexity: O(N)
        Space complexity: O(1)
        可以看作异或
        """
        ans = 0
        l,r = 1, 2**(N-1)
        while l<r:
            mid = (l+r)//2
            if mid<K:
                # xor to flip 1 to 0 or 0 to 1
                ans = ans ^ 1
                l = mid +1
            else:
                r = mid
        return ans
# @lc code=end

