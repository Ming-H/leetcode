#
# @lc app=leetcode id=667 lang=python3
#
# [667] Beautiful Arrangement II
#

# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n) 
        """
        ans = list(range(1, n - k))
        for i in range(k+1):
            if i % 2 == 0:
                ans.append(n-k + i//2)
            else:
                ans.append(n - i//2)

        return ans
# @lc code=end

